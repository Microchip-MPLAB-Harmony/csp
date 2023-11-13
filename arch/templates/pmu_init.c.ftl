/*******************************************************************************
  PIC32MZW1 PMU MLDO TRIMMING

  File Name:
    pmu_init.c

  Summary:
    PIC32MZW1 boot time PMU mode and output Configuration.

  Description:
    This interface helps configure the PMU in either DC-DC/MLDO mode and also trim
    the voltages in the corresponding mode to the operating range.

 *******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2019 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
 *******************************************************************************/
//DOM-IGNORE-END

#include "device.h"
#include "definitions.h"

/*Bits [15-6] in the SPI Status register have Read data */
#define PMU_SPI_READ_MASK 0xFFFF0000U

// PMU related defines
#define BUCKCFG1_ADDR 0x14U
#define BUCKCFG2_ADDR 0x15U
#define BUCKCFG3_ADDR 0x16U
#define MLDOCFG1_ADDR 0x17U
#define MLDOCFG2_ADDR 0x18U
#define SPI_CMD_OFFSET 24
#define SPI_ADDR_OFFSET 16
#define TREG_DEFAULT 0x16161616U
#define MLDO_ISENSE_CONFIG 0xC07U
#define MLDO_ENABLE 0x00000A80U
#define BUCK_PBYPASS_ENABLE 0x4U
#define BUCK_SCP_TUNE 0x10U
#define MLDOCFG1_DEFAULT_VAL 0x180U
#define PMU_STATUS_SPIRDY 0x80U
#define VREG1_BITS 0x0000001FU
#define VREG2_BITS 0x00001F00U
#define VREG3_BITS 0x001F0000U
#define VREG4_BITS 0x1F000000U
#define CORE_TIMER_FREQ 100000000

#define PIC32MZW1_B0 0xA4
#define PIC32MZW1_A1 0x8C
#define PART_NUM_OFFSET 20
#define PART_NUM_MASK 0x0FF00000U
#define PMUSPI_BUCKCFG1_DEFAULT_VAL     0x5480U
#define PMUSPI_BUCKCFG2_DEFAULT_VAL     0x8C28U
#define PMUSPI_BUCKCFG3_DEFAULT_VAL     0x00C8U
#define PMUSPI_MLDOCFG1_DEFAULT_VAL     0x0287U
#define PMUSPI_MLDOCFG2_DEFAULT_VAL     0x0280U
#define MLDO_HW_BP_EN 0x4U

//Flash Area housing the PMU calibration values
static volatile uint32_t *otp_buckcfg1_data    = (volatile uint32_t *)0xBFC56FE8U;
static volatile uint32_t *otp_buckcfg2_data    = (volatile uint32_t *) 0xBFC56FECU;
static volatile uint32_t *otp_buckcfg3_data    = (volatile uint32_t *) 0xBFC56FF0U;
static volatile uint32_t *otp_mldocfg1_data    = (volatile uint32_t *) 0xBFC56FF4U;
static volatile uint32_t *otp_mldocfg2_data    = (volatile uint32_t *) 0xBFC56FF8U;
static volatile uint32_t *otp_treg3_data       = (volatile uint32_t *)0xBFC56FFCU;

static volatile uint32_t *spi_status_reg   = (volatile uint32_t *)0xBF813E04U;
static volatile uint32_t *spi_cntrl_reg    = (volatile uint32_t *)0xBF813E00U;

/* This register is not used currently, Maybe used in future */
/* static volatile uint32_t *pmu_cmode_reg    = (volatile uint32_t *)0xBF813E20U; */

static uint32_t M_BUCKEN, M_MLDOEN, M_BUCKMODE;
static uint32_t S_BUCKEN, S_MLDOEN, S_BUCKMODE;
static uint32_t O_BUCKEN, O_MLDOEN, O_BUCKMODE, OVEREN;

static void DelayMs(uint32_t delay_ms)
{
    uint32_t startCount, endCount;
    /* Calculate the end count for the given delay */
    endCount=(CORE_TIMER_FREQ / 1000) * delay_ms;
    startCount = _CP0_GET_COUNT();
    while((_CP0_GET_COUNT() - startCount) < endCount)
    {
        /* wait for compare match */
    }
}

static uint32_t SYS_PMU_SPI_READ(uint32_t spi_addr)
{
    uint32_t spi_val , reg_val;
    uint32_t status;
    reg_val = (1UL << SPI_CMD_OFFSET) | (spi_addr << SPI_ADDR_OFFSET);
    *spi_cntrl_reg = reg_val;

    DelayMs(5U);

    while (true)
    {
        status = *spi_status_reg;
        if((status & PMU_STATUS_SPIRDY) != 0U)
        {
            break;
        }
    }
    spi_val = ((status & PMU_SPI_READ_MASK) >> SPI_ADDR_OFFSET);
    return spi_val;
}

static void SYS_PMU_SPI_WRITE(uint32_t spi_addr, uint32_t reg_val)
{
    uint32_t spi_val ;
    uint32_t status;
    reg_val &= 0xFFFFU;
    spi_val = (spi_addr << SPI_ADDR_OFFSET) | reg_val;
    *spi_cntrl_reg = spi_val;
    DelayMs(5U);
    while (true)
    {
        status = *spi_status_reg;
        if((status & PMU_STATUS_SPIRDY) != 0U)
        {
            break;
        }
    }
}

/*This function will configure the PMU with
 *the tune bits from Flash.
 *
 * Flash area to read from
 * 0xBFC56FE0	BLANK
 * 0xBFC56FE4	BLANK
 * 0xBFC56FE8	BUCKCFG1 (vo_tune in bits [13:10] other bits written low
 * 0xBFC56FEC	BUCKCFG2 (default buk_curve value written to bits [6:4], other bits written low.
 * 0xBFC56FF0	BUCKCFG3 (currently BLANK, set aside for possible future use)
 * 0xBFC56FF4	MLDOCFG1 (currently BLANK until we receive MLDO trim pattern and implement calibration on ATE)
 * 0xBFC56FF8	MLDOCFG2 (currently BLANK until we receive MLDO trim pattern and implement calibration on ATE)
 * 0xBFC56FFC	TREG3 (VREG4,3,2,1) values
 *
 * Below are the configurations done here
 * Configure buk_Vo_tune<13:10> in BUCKCFG1, ADDR=0x14 register
 * Configure mldo_vtun<9:6> in the MLDOCFG1, ADDR=0x17 register
 * Configure PLDO1[4:0] in the TREG3 register
 * Configure PLDO2[12:8] in the TREG3 register
 * Configure PLDO3[20:16] in the TREG3 register
 * Configure VREGPLL1[28:24] in the TREG3 register
 */

void PMU_Initialize(void)
{
    uint32_t nvm_flash_data, otp_treg_val;
    uint32_t mldocfg1, mldocfg2, buckcfg1, buckcfg2, buckcfg3;
    uint32_t vreg1, vreg2, vreg3, vreg4;
    uint32_t tmp1, tmp2;

    if(((DEVID & PART_NUM_MASK) >> PART_NUM_OFFSET) == PIC32MZW1_B0)
    {
       tmp1 = RCONbits.POR;
       if((RCONbits.BOR == 1U) || (tmp1 == 1U))
       {
            // SPI Cock (Max=20M), SRC=System(PB1), Div=5
            // Buck Clock SRC=FRC, DIV=8
            // BACWD=0, restriction due to BUG (SG407-110)
            // BACWD=1, is efficient on time but intermittent failures due to (SG407-110) bug
            PMUCLKCTRL = 0x00004885U;

            buckcfg1 = *otp_buckcfg1_data;
            if((buckcfg1 == 0x00000000U) || (buckcfg1 == 0xFFFFFFFFU))
            {
                buckcfg1 = PMUSPI_BUCKCFG1_DEFAULT_VAL;
            }
            SYS_PMU_SPI_WRITE(BUCKCFG1_ADDR, buckcfg1);

            buckcfg2 = *otp_buckcfg2_data;
            if((buckcfg2 == 0x00000000U) || (buckcfg2 == 0xFFFFFFFFU))
            {
                buckcfg2 = PMUSPI_BUCKCFG2_DEFAULT_VAL;
            }
            SYS_PMU_SPI_WRITE(BUCKCFG2_ADDR, buckcfg2);

            buckcfg3 = *otp_buckcfg3_data;
            if((buckcfg3 == 0x00000000U) || (buckcfg3 == 0xFFFFFFFFU))
            {
                buckcfg3 = PMUSPI_BUCKCFG3_DEFAULT_VAL;
            }
            SYS_PMU_SPI_WRITE(BUCKCFG3_ADDR, buckcfg3);

            mldocfg1 = *otp_mldocfg1_data;
            if((mldocfg1 == 0x00000000U) || (mldocfg1 == 0xFFFFFFFFU))
            {
                mldocfg1 = PMUSPI_MLDOCFG1_DEFAULT_VAL;
            }
            SYS_PMU_SPI_WRITE(MLDOCFG1_ADDR, mldocfg1);

            mldocfg2 = *otp_mldocfg2_data;
            if((mldocfg2 == 0x00000000U) || (mldocfg2 == 0xFFFFFFFFU))
            {
                mldocfg2 = PMUSPI_MLDOCFG2_DEFAULT_VAL;
            }
            SYS_PMU_SPI_WRITE(MLDOCFG2_ADDR, mldocfg2);
            (void)SYS_PMU_SPI_READ(MLDOCFG2_ADDR);

            otp_treg_val = *otp_treg3_data;
            if((otp_treg_val == 0xFFFFFFFFU) || (otp_treg_val == 0x00000000U))
            {
                otp_treg_val = TREG_DEFAULT;
            }
            vreg4 = otp_treg_val & VREG1_BITS;
            vreg3 = (otp_treg_val & VREG2_BITS) >> 8;
            vreg2 = (otp_treg_val & VREG3_BITS) >> 16;
            vreg1 = (otp_treg_val & VREG4_BITS) >> 24;

            // Mission mode PMU Mode #1 register

            M_BUCKEN = 1U;
            M_MLDOEN = 0U;
            M_BUCKMODE = 1U; // PMU-Buck PWM Mode
            PMUMODECTRL1 = ((M_BUCKEN << 31) | (M_MLDOEN << 30) | (M_BUCKMODE << 29) |
                    (vreg1 << 24) | (vreg2 << 16) | (vreg3 << 8) | vreg4);

            // Sleep mode PMU Mode #2 register
            // TODO - When available, use the Sleep Mode Calibration values
            S_BUCKEN = 1U;
            S_MLDOEN = 0U;
            S_BUCKMODE = 0U; // PMU-Buck PSM Mode
            PMUMODECTRL2 = ((S_BUCKEN << 31) | (S_MLDOEN << 30) | (S_BUCKMODE << 29) |
                    (vreg1 << 24) | (vreg2 << 16) | (vreg3 << 8) | vreg4);

            // For HUT Code keeping the PMU in SW Override Mode
            // OVEREN = 1, triggers the mode change
            O_BUCKEN = 1U;
            O_MLDOEN = 0U;
            O_BUCKMODE = 1U;
            OVEREN = 1U; // PMU-Buck PWM Mode
            PMUOVERCTRL = ((O_BUCKEN << 31) | (O_MLDOEN << 30) | (O_BUCKMODE << 29) |
                    (OVEREN << 23) | (vreg1 << 24) | (vreg2 << 16) | (vreg3 << 8) | vreg4);

            // Trigger PMU Mode Change, with CLKCTRL.BACWD=0
            PMUOVERCTRLbits.PHWC = 0U;

            // Poll for Buck switching to be complete
            tmp1 = PMUCMODEbits.CBUCKMODE;
            tmp2 = PMUCMODEbits.CMLDOEN;
            while (!((PMUCMODEbits.CBUCKEN != 0U) && (tmp1 != 0U) && (tmp2 == 0U)))
            {
                tmp1 = PMUCMODEbits.CBUCKMODE;
                tmp2 = PMUCMODEbits.CMLDOEN;
            }

            // Post process the Buck switching if Calibration values are not present
            // VTUNE[3:0]=0x0 if no calibration
            buckcfg1 = *otp_buckcfg1_data;
            if((buckcfg1 == 0x00000000U) || (buckcfg1 == 0xFFFFFFFFU))
            {
                SYS_PMU_SPI_WRITE(BUCKCFG1_ADDR, (SYS_PMU_SPI_READ(BUCKCFG1_ADDR) & 0xEBFF));
            }

            // BUCKCFG2 0x8C28 - If no calibration, we need to update buk_scp_tune at the least to 2?b10, so update it o 0x8D28
            buckcfg2 = *otp_buckcfg2_data;
            if((buckcfg2 == 0x00000000U) || (buckcfg2 == 0xFFFFFFFFU))
            {
                SYS_PMU_SPI_WRITE(BUCKCFG2_ADDR, (SYS_PMU_SPI_READ(BUCKCFG2_ADDR) | BUCK_SCP_TUNE));
            }
       }
    }
    else if(((DEVID & PART_NUM_MASK) >> PART_NUM_OFFSET) == PIC32MZW1_A1)
    {
        //PMU_MLDO_Cfg()
        //Read MLDOCFG1 Value
        mldocfg1 = SYS_PMU_SPI_READ(MLDOCFG1_ADDR);
        if(mldocfg1 == 0x0)
        {
            mldocfg1 = *otp_mldocfg1_data;
            if((mldocfg1 == 0xFFFFFFFFU) || (mldocfg1 == 0x00000000U))
            {
                mldocfg1 = MLDOCFG1_DEFAULT_VAL | MLDO_ISENSE_CONFIG;
            }
            else
            {
                mldocfg1 |= MLDO_ISENSE_CONFIG;
            }
        }
        else
        {
            mldocfg1 = *otp_mldocfg1_data | MLDO_ISENSE_CONFIG;
        }
        SYS_PMU_SPI_WRITE(MLDOCFG1_ADDR, mldocfg1);
        /* make sure mldo_cfg2 register is zero, nothing is enabled. */
        mldocfg2 = 0U;
        SYS_PMU_SPI_WRITE(MLDOCFG2_ADDR, mldocfg2);

        //PMU_MLDO_Enable()
        mldocfg2 = SYS_PMU_SPI_READ(MLDOCFG2_ADDR);
        mldocfg2 |= MLDO_ENABLE;
        SYS_PMU_SPI_WRITE(MLDOCFG2_ADDR, mldocfg2);

        //PMU_MLDO_Set_ParallelBypass()
        buckcfg1 = SYS_PMU_SPI_READ(BUCKCFG1_ADDR);
        buckcfg1 |= BUCK_PBYPASS_ENABLE;
        SYS_PMU_SPI_WRITE(BUCKCFG1_ADDR, buckcfg1);

        nvm_flash_data = *otp_treg3_data;
        if((nvm_flash_data == 0xFFFFFFFFU) || (nvm_flash_data == 0x00000000U))
        {
            nvm_flash_data = TREG_DEFAULT;
        }
        vreg4 = nvm_flash_data & VREG1_BITS;
        vreg3 = (nvm_flash_data & VREG2_BITS) >> 8;
        vreg2 = (nvm_flash_data & VREG3_BITS) >> 16;
        vreg1 = (nvm_flash_data & VREG4_BITS) >> 24;

        PMUOVERCTRLbits.OBUCKEN = 0U;	//Disable Buck mode
        PMUOVERCTRLbits.OMLDOEN = 1U;	//Enable MLDO mode

        /* Configure Output Voltage Control Bits */
        PMUOVERCTRLbits.VREG4OCTRL = (uint8_t)vreg4;
        PMUOVERCTRLbits.VREG3OCTRL = (uint8_t)vreg3;
        PMUOVERCTRLbits.VREG2OCTRL = (uint8_t)vreg2;
        PMUOVERCTRLbits.VREG1OCTRL = (uint8_t)vreg1;

        PMUOVERCTRLbits.PHWC = 0U;	//Disable Power-up HW Control
        PMUOVERCTRLbits.OVEREN = 1U;	//set override enable bit
    }
    else if(((DEVID & PART_NUM_MASK) >> PART_NUM_OFFSET) == PIC32MZW1_G)
    {
        nvm_flash_data = *otp_treg3_data;
        if((nvm_flash_data == 0xFFFFFFFFU) || (nvm_flash_data == 0x00000000U))
        {
            nvm_flash_data = TREG_DEFAULT;
        }
        vreg4 = nvm_flash_data & VREG1_BITS;
        vreg3 = (nvm_flash_data & VREG2_BITS) >> 8;
        vreg2 = (nvm_flash_data & VREG3_BITS) >> 16;
        vreg1 = (nvm_flash_data & VREG4_BITS) >> 24;

        PMUOVERCTRLbits.OBUCKEN = 0;	//Disable Buck mode
        PMUOVERCTRLbits.OMLDOEN = 1;	//Enable MLDO mode

        /* Configure Output Voltage Control Bits */
        PMUOVERCTRLbits.VREG4OCTRL = (uint8_t)vreg4;
        PMUOVERCTRLbits.VREG3OCTRL = (uint8_t)vreg3;
        PMUOVERCTRLbits.VREG2OCTRL = (uint8_t)vreg2;
        PMUOVERCTRLbits.VREG1OCTRL = (uint8_t)vreg1;

        PMUOVERCTRLbits.PHWC = 0;	//Disable Power-up HW Control
        PMUOVERCTRLbits.OVEREN = 1;	//set override enable bit

        //Read MLDOCFG1 Value
        mldocfg1 = SYS_PMU_SPI_READ(MLDOCFG1_ADDR);
        nvm_flash_data = *otp_mldocfg1_data;
        if ((nvm_flash_data == 0xFFFFFFFFU) || (nvm_flash_data == 0x0U))
        {
            mldocfg1 |= MLDOCFG1_DEFAULT_VAL | MLDO_ISENSE_CONFIG;
        }
        else
        {
            mldocfg1 |= nvm_flash_data | MLDO_ISENSE_CONFIG;
        }
        SYS_PMU_SPI_WRITE(MLDOCFG1_ADDR, mldocfg1);

        mldocfg2 = SYS_PMU_SPI_READ(MLDOCFG2_ADDR);
        nvm_flash_data = *otp_mldocfg2_data;
        if ((nvm_flash_data == 0xFFFFFFFFU) || (nvm_flash_data == 0x0U))
        {
            mldocfg2 = 0xCA80;
        }
        else
        {
            mldocfg2 = ((*otp_mldocfg2_data) & 0x00008000);
        }
        mldocfg2 |= MLDO_ENABLE;
        SYS_PMU_SPI_WRITE(MLDOCFG2_ADDR, mldocfg2);

        /* Set Band gap temp coefficient*/
        buckcfg3 = SYS_PMU_SPI_READ(BUCKCFG3_ADDR);
        nvm_flash_data = *otp_buckcfg3_data;
        if ((nvm_flash_data == 0xFFFFFFFFU) || (nvm_flash_data == 0x0U))
        {
            buckcfg3 = 0x00C8;
        }
        else
        {
            buckcfg3 |= 0x00C8;
        }
        SYS_PMU_SPI_WRITE(BUCKCFG3_ADDR, buckcfg3);
        //printf("PMU SPI BUCKCFG3 after enabling : %x \n", buckcfg3);

        buckcfg1 = SYS_PMU_SPI_READ(BUCKCFG1_ADDR);
        buckcfg1 |= 0x0001;
        //printf("Enabling mLDO bandgap_en signal\n");
        SYS_PMU_SPI_WRITE(BUCKCFG1_ADDR, buckcfg1);
        buckcfg1 = SYS_PMU_SPI_READ(BUCKCFG1_ADDR);

        //PMU_MLDO_Set_ParallelBypass()

        buckcfg1 = SYS_PMU_SPI_READ(BUCKCFG1_ADDR);
        buckcfg1 |= BUCK_PBYPASS_ENABLE;
        SYS_PMU_SPI_WRITE(BUCKCFG1_ADDR, buckcfg1);
    }
    else
    {
        /* Nothing to process */
    }
}
