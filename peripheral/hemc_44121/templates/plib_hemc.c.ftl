/*****************************************************************************
  Company:
    Microchip Technology Inc.

  File Name:
    plib_${HEMC_INSTANCE_NAME?lower_case}.c

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
#include "plib_${HEMC_INSTANCE_NAME?lower_case}.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: HEMC Implementation
// *****************************************************************************
// *****************************************************************************

<#if USE_HSDRAM>
void SW_DelayUs(uint32_t delay)
{
    uint32_t i, count;

    /* delay * (CPU_FREQ/1000000) / 6 */
    count = delay *  (${HSDRAMC_CPU_CLK_FREQ}/1000000)/6;

    /* 6 CPU cycles per iteration */
    for (i = 0; i < count; i++)
        __NOP();
}


void ${HSDRAMC_INSTANCE_NAME}_Initialize( void )
{
    uint8_t i;
    uint16_t *pSdramBaseAddress = (uint16_t *)0x${SDRAMC_START_ADDRESS};

    /* Step 1:
     * Configure SDRAM features and timing parameters */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_CR = HSDRAMC_CR_NC_${HSDRAMC_CR__NC} | HSDRAMC_CR_NR_${HSDRAMC_CR__NR} | HSDRAMC_CR_NB_${HSDRAMC_CR__NB}<#if HSDRAMC_CR_DBW == "16-bits"> | HSDRAMC_CR_DBW_Msk </#if> \
                                                | HSDRAMC_CR_CAS(${HSDRAMC_CR_CAS}) ;

    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_SDR = HSDRAMC_SDR_TRAS(${HSDRAMC_SDR_TRAS}) |  HSDRAMC_SDR_TRP(${HSDRAMC_SDR_TRP}) |  HSDRAMC_SDR_TRC_TRFC(${HSDRAMC_SDR_TRC_TRFC}) \
                                                | HSDRAMC_SDR_TRCD(${HSDRAMC_SDR_TRCD}) | HSDRAMC_SDR_TWR(${HSDRAMC_SDR_TWR}) | HSDRAMC_SDR_TXSR(${HSDRAMC_SDR_TXSR});
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_CFR1= HSDRAMC_CFR1_TMRD(${HSDRAMC_CFR1_TMRD}) | HSDRAMC_CFR1_UNAL_Msk;

    /* Step 2:
     * A pause of at least 200 us must be observed before a signal toggle */
    SW_DelayUs(200);

    /* Step 3:
     * Issue a NOP command to the SDRAM device by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Write to any SDRAM address to acknowledge this command. Now the clock which drives SDRAM device is enabled */

    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_NOP;
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 4:
     * Issue an All banks precharge command by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Write to any SDRAM address to acknowledge this command. */

    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_ALLBANKS_PRECHARGE;
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 5:
     * Issue 8 Auto Refresh(CBR) cycles by writing to the Mode Register.
     * Read back the Mode Register and add a memory barrier assembly instruction just after the read.
     * Perform a write access to any SDRAM address 8 times. */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_AUTO_REFRESH;
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR;
    __DMB();
    for (i = 0; i < 8; i++)
    {
        *pSdramBaseAddress = i;
    }

    /* Step 6:
     * Issue Mode Register Set(MRS) to program the parameters of the SDRAM device, in particular CAS latency and burst length */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_LOAD_MODEREG;
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR;
    __DMB();
    *((uint16_t *)(pSdramBaseAddress + 0x${HSDRAMC_MRS_VALUE})) = 0;

    /* Step 7:
     * Transition the SDRAM to NORMAL mode. Read back the Mode
     * Register and add a memory barrier assembly instruction just after the
     * read. Perform a write access to any SDRAM address. */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR = HSDRAMC_MR_MODE_NORMAL;
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_MR;
    __DMB();
    *pSdramBaseAddress = 0x0;

    /* Step 8:
     * Configure the Refresh Timer Register. */
    ${HSDRAMC_INSTANCE_NAME}_REGS->HSDRAMC_TR = ${HSDRAMC_TR_COUNT};

}
</#if>

void ${HSMC_INSTANCE_NAME}_Initialize( void )
{
<#list 0..(HSMC_CHIP_SELECT_COUNT - 1) as i>
    <#assign HSMC_IN_USE = "USE_HSMC_" + i>
    <#assign HSMC_CHIP_SELECT = "HSMC_CHIP_SELECT" + i>
    <#assign HSMC_DATA_BUS_CS = "HSMC_DATA_BUS_CS" + i>
    <#assign HSMC_NWE_SETUP_CS = "HSMC_NWE_SETUP_CS" + i>
    <#assign HSMC_NCS_WR_SETUP_CS = "HSMC_NCS_WR_SETUP_CS" + i>
    <#assign HSMC_NRD_SETUP_CS = "HSMC_NRD_SETUP_CS" + i>
    <#assign HSMC_NCS_RD_SETUP_CS = "HSMC_NCS_RD_SETUP_CS" + i>
    <#assign HSMC_NWE_PULSE_CS = "HSMC_NWE_PULSE_CS" + i>
    <#assign HSMC_NCS_WR_PULSE_CS = "HSMC_NCS_WR_PULSE_CS" + i>
    <#assign HSMC_NRD_PULSE_CS = "HSMC_NRD_PULSE_CS" + i>
    <#assign HSMC_NCS_RD_PULSE_CS = "HSMC_NCS_RD_PULSE_CS" +i>
    <#assign HSMC_NWE_CYCLE_CS = "HSMC_NWE_CYCLE_CS" + i>
    <#assign HSMC_NRD_CYCLE_CS = "HSMC_NRD_CYCLE_CS" + i>
    <#assign HSMC_NWAIT_MODE_CS = "HSMC_NWAIT_MODE_CS" +i>
    <#assign HSMC_WRITE_MODE_CS = "HSMC_WRITE_ENABLE_MODE_CS" + i>
    <#assign HSMC_READ_MODE_CS = "HSMC_READ_ENABLE_MODE_CS" + i>
    <#assign HSMC_RMW = "HSMC_MODE_RMW" + i>
    <#if .vars[HSMC_IN_USE]>
    <#if .vars[HSMC_CHIP_SELECT]?has_content>

    <#if (.vars[HSMC_CHIP_SELECT] != false)>

    /* Chip Select CS${i} Timings */
    /* Setup HSMC SETUP register */
    ${HSMC_INSTANCE_NAME}_REGS->HSMC_SETUP${i}= HSMC_SETUP${i}_NWE_SETUP(${.vars[HSMC_NWE_SETUP_CS]}) | HSMC_SETUP${i}_NCS_WR_SETUP(${.vars[HSMC_NCS_WR_SETUP_CS]}) | HSMC_SETUP${i}_NRD_SETUP(${.vars[HSMC_NRD_SETUP_CS]}) | HSMC_SETUP${i}_NCS_RD_SETUP(${.vars[HSMC_NCS_RD_SETUP_CS]});

    /* Setup HSMC CYCLE register */
    ${HSMC_INSTANCE_NAME}_REGS->HSMC_CYCLE${i}= HSMC_CYCLE${i}_NWE_CYCLE(${.vars[HSMC_NWE_CYCLE_CS]}) | HSMC_CYCLE${i}_NRD_CYCLE(${.vars[HSMC_NRD_CYCLE_CS]});

    /* Setup HSMC_PULSE register */
    ${HSMC_INSTANCE_NAME}_REGS->HSMC_PULSE${i}= HSMC_PULSE${i}_NWE_PULSE(${.vars[HSMC_NWE_PULSE_CS]}) | HSMC_PULSE${i}_NCS_WR_PULSE(${.vars[HSMC_NCS_WR_PULSE_CS]}) | HSMC_PULSE${i}_NRD_PULSE(${.vars[HSMC_NRD_PULSE_CS]}) | HSMC_PULSE${i}_NCS_RD_PULSE(${.vars[HSMC_NCS_RD_PULSE_CS]});

    /* Setup HSMC MODE register */
    ${HSMC_INSTANCE_NAME}_REGS->HSMC_MODE${i}= HSMC_MODE${i}_EXNW_MODE(${.vars[HSMC_DATA_BUS_CS]}) <#if (.vars[HSMC_WRITE_MODE_CS] == true)>| HSMC_MODE${i}_WRITE_MODE_Msk</#if> <#if (.vars[HSMC_READ_MODE_CS] == true)>| HSMC_MODE${i}_READ_MODE_Msk</#if> <#if (.vars[HSMC_RMW] == true)>| HSMC_MODE${i}_RMW_ENABLE_Msk</#if>;
    </#if>
    </#if>
    </#if>
</#list>

<#if HSMC_WRITE_PROTECTION>
    /* Enable Write Protection */
    ${HSMC_INSTANCE_NAME}_REGS->HSMC_WPMR = (HSMC_WPMR_WPKEY_PASSWD | HSMC_WPMR_WPEN_Msk);
</#if>
}
void ${HEMC_INSTANCE_NAME}_Initialize( void )
{
  <#list 0..5 as i>
  <#assign HEMC_TYPE = "CS_" + i + "_MEMORY_TYPE" >
  <#assign HEMC_BANK =  "CS_" + i + "_MEMORY_BANK_SIZE">
  <#assign HEMC_ADDRESS = "CS_" + i + "_MEMORY_BASE" >
    <#if (.vars[HEMC_ADDRESS] != "3ffff") || (i = 0)>
    ${HEMC_INSTANCE_NAME}_REGS->HEMC_CR_NCS${i} = HEMC_CR_NCS${i}_TYPE(${.vars[HEMC_TYPE]}) | HEMC_CR_NCS${i}_ADDBASE(0x${.vars[HEMC_ADDRESS]}) | HEMC_CR_NCS${i}_BANKSIZE(${.vars[HEMC_BANK]});
    </#if>
  </#list>
  <#if USE_HSDRAM>
    ${HSDRAMC_INSTANCE_NAME}_Initialize();
  </#if>
    ${HSMC_INSTANCE_NAME}_Initialize();

} /* ${HEMC_INSTANCE_NAME}_Initialize */
/*******************************************************************************
 End of File
*/
