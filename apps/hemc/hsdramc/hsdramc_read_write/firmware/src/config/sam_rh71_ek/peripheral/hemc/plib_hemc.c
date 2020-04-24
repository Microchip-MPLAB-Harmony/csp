/*****************************************************************************
  Company:
    Microchip Technology Inc.

  File Name:
    plib_hemc.c

  Summary:
    HEMC PLIB Source file

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/
#include <string.h>
#include "device.h"
#include "plib_hemc.h"


// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: HEMC Implementation
// *****************************************************************************
// *****************************************************************************

void SW_DelayUs(uint32_t delay)
{
    uint32_t i, count;

    /* delay * (CPU_FREQ/1000000) / 6 */
    count = delay *  (100000000/1000000)/6;

    /* 6 CPU cycles per iteration */
    for (i = 0; i < count; i++)
        __NOP();
}


void HSDRAMC_Initialize( void )
{
    uint8_t i;
    uint16_t *pSdramBaseAddress = (uint16_t *)0x64000000;

    /* Step 1:
     * Configure SDRAM features and timing parameters */
    HSDRAMC_REGS->HSDRAMC_CR = HSDRAMC_CR_NC_COL9 | HSDRAMC_CR_NR_ROW13 | HSDRAMC_CR_NB_BANK4\
                                                | HSDRAMC_CR_CAS(3) ;

    HSDRAMC_REGS->HSDRAMC_SDR = HSDRAMC_SDR_TRAS(5) |  HSDRAMC_SDR_TRP(2) |  HSDRAMC_SDR_TRC_TRFC(6) \
                                                | HSDRAMC_SDR_TRCD(2) | HSDRAMC_SDR_TWR(2) | HSDRAMC_SDR_TXSR(7);
    HSDRAMC_REGS->HSDRAMC_CFR1= HSDRAMC_CFR1_TMRD(2) | HSDRAMC_CFR1_UNAL_Msk;

    /* Step 2:
     * A pause of at least 200 us must be observed before a signal toggle */
    SW_DelayUs(200);

    /* Step 3:
     * Issue a NOP command to the SDRAM device by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Write to any SDRAM address to acknowledge this command. Now the clock which drives SDRAM device is enabled */

    HSDRAMC_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_NOP;
    HSDRAMC_REGS->HSDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 4:
     * Issue an All banks precharge command by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Write to any SDRAM address to acknowledge this command. */

    HSDRAMC_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_ALLBANKS_PRECHARGE;
    HSDRAMC_REGS->HSDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 5:
     * Issue 8 Auto Refresh(CBR) cycles by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Perform a write access to any SDRAM address 8 times. */
    HSDRAMC_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_AUTO_REFRESH;
    HSDRAMC_REGS->HSDRAMC_MR;
    __DMB();
    for (i = 0; i < 8; i++)
    {
        *pSdramBaseAddress = i;
    }

    /* Step 6:
     * Issue Mode Register Set(MRS) to program the parameters of the SDRAM device, in particular CAS latency and burst length */
    HSDRAMC_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_LOAD_MODEREG;
    HSDRAMC_REGS->HSDRAMC_MR;
    __DMB();
    *((uint16_t *)(pSdramBaseAddress + 0x0)) = 0;

    /* Step 7:
     * Transition the SDRAM to NORMAL mode. Read back the Mode
     * Register and add a memory barrier assembly instruction just after the
     * read. Perform a write access to any SDRAM address. */
    HSDRAMC_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_NORMAL;
    HSDRAMC_REGS->HSDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 8:
     * Configure the Refresh Timer Register. */
    HSDRAMC_REGS->HSDRAMC_TR = 195;


}

void HSMC_Initialize( void )
{






}
void HEMC_Initialize( void )
{
    /* Read NCS0 Pin configuration for HECC */
    uint8_t eccEnableDefault = ( (HEMC_REGS->HEMC_HECC_CR0 & HEMC_HECC_CR0_ENABLE_Msk) >> HEMC_HECC_CR0_ENABLE_Pos);
    uint8_t eccAlgoDefault = ( (HEMC_REGS->HEMC_HECC_CR0 & HEMC_HECC_CR0_ECC12_ENABLE_Msk) >> HEMC_HECC_CR0_ECC12_ENABLE_Pos);

    /* Enable NCS0 configuration modification through registers */
    HEMC_REGS->HEMC_CR_NCS0 |= HEMC_CR_NCS0_WRITE_ECC_CONF(1);

    HEMC_REGS->HEMC_CR_NCS0 = HEMC_CR_NCS0_TYPE(0) |
                              HEMC_CR_NCS0_ADDBASE(0x3ffff) |
                              HEMC_CR_NCS0_BANKSIZE(0x1F) |
                              HEMC_CR_NCS0_WRITE_ECC_CONF(1) |
                              HEMC_CR_NCS0_ECC_ENABLE(eccEnableDefault) |
                              HEMC_CR_NCS0_ECC12_ENABLE(eccAlgoDefault);

    HEMC_REGS->HEMC_CR_NCS4 = HEMC_CR_NCS4_TYPE(1) |
                              HEMC_CR_NCS4_ADDBASE(0x1000) |
                              HEMC_CR_NCS4_BANKSIZE(0xC);
    HSDRAMC_Initialize();
    HSMC_Initialize();




} /* HEMC_Initialize */

// *****************************************************************************
/* Function:
    void HEMC_HeccGetStatus(void)

   Summary:
    Get the HECC status of the HEMC peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    Current status of the HEMC peripheral.
*/
HEMC_HECC_STATUS HEMC_HeccGetStatus(void)
{
    return (HEMC_HECC_STATUS)(HEMC_REGS->HEMC_HECC_SR);
}

// *****************************************************************************
/* Function:
    uint32_t* HEMC_HeccGetFailAddress(void)

   Summary:
    Get the last fail address were ECC error occurs in a HEMC memory.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    Pointer of fail address were fixable or unfixable error occured in a HEMC memory.
*/
uint32_t* HEMC_HeccGetFailAddress(void)
{
    return (uint32_t*)(HEMC_REGS->HEMC_HECC_FAILAR);
}

// *****************************************************************************
/* Function:
    void HEMC_HeccResetCounters(void)

   Summary:
    Reset Fix and NoFix error counters of the HEMC peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None
*/
void HEMC_HeccResetCounters(void)
{
    HEMC_REGS->HEMC_HECC_CR0 |= (HEMC_HECC_CR0_RST_FIX_CPT_Msk | HEMC_HECC_CR0_RST_NOFIX_CPT_Msk);
    HEMC_REGS->HEMC_HECC_CR1 |= (HEMC_HECC_CR1_RST_FIX_CPT_Msk | HEMC_HECC_CR1_RST_NOFIX_CPT_Msk);
    HEMC_REGS->HEMC_HECC_CR2 |= (HEMC_HECC_CR2_RST_FIX_CPT_Msk | HEMC_HECC_CR2_RST_NOFIX_CPT_Msk);
}


/*******************************************************************************
 End of File
*/
