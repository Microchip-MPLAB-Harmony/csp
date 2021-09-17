/*******************************************************************************
  SYS CLK Static Functions for Clock System Service

  Company:
    Microchip Technology Inc.

  File Name:
    plib_clk.c

  Summary:
    SYS CLK static function implementations for the Clock System Service.

  Description:
    The Clock System Service provides a simple interface to manage the
    oscillators on Microchip microcontrollers. This file defines the static
    implementation for the Clock System Service.

  Remarks:
    Static functions incorporate all system clock configuration settings as
    determined by the user via the Microchip Harmony Configurator GUI.
    It provides static version of the routines, eliminating the need for an
    object ID or object handle.

    Static single-open interfaces also eliminate the need for the open handle.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_clk.h"

#define CLK_READY_RETRIES  8000
#define BTZB_XTAL_NOT_READY ((BTZBSYS_REGS->BTZBSYS_SUBSYS_STATUS_REG1 \
                            & BTZBSYS_SUBSYS_STATUS_REG1_xtal_ready_out_Msk) \
                            != BTZBSYS_SUBSYS_STATUS_REG1_xtal_ready_out_Msk)
#define BTZB_PLL_NOT_LOCKED ((BTZBSYS_REGS->BTZBSYS_SUBSYS_STATUS_REG1 \
                            & BTZBSYS_SUBSYS_CNTRL_REG1_subsys_dbg_bus_sel_top_Msk) \
                            != BTZBSYS_SUBSYS_CNTRL_REG1_subsys_dbg_bus_sel_top_Msk)

// *****************************************************************************
// *****************************************************************************
// Section: File Scope Functions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void CLK_Initialize( void )

  Summary:
    Initializes hardware and internal data structure of the System Clock.

  Description:
    This function initializes the hardware and internal data structure of System
    Clock Service.

  Remarks:
    This is configuration values for the static version of the Clock System
    Service module is determined by the user via the MHC GUI.

    The objective is to eliminate the user's need to be knowledgeable in the
    function of the 'configuration bits' to configure the system oscillators.
*/

void CLK_Initialize( void )
{
    //check CLDO ready
    while ((CFG_REGS->CFG_MISCSTAT & CFG_MISCSTAT_CLDORDY_Msk) == 0);    
    
    // wait for xtal_ready      
    uint32_t clk_ready_tries = 0;
    do
    {
        clk_ready_tries++;
    } while(BTZB_XTAL_NOT_READY && (clk_ready_tries < CLK_READY_RETRIES));
    
    if((clk_ready_tries >= CLK_READY_RETRIES) && BTZB_XTAL_NOT_READY)
    {
        BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG1 |=(BTZBSYS_SUBSYS_CNTRL_REG1_subsys_bypass_xtal_ready_Msk);
        while(BTZB_XTAL_NOT_READY);
    }
       
    // set PLL_enable
    BLE_REGS->BLE_DPLL_RG2 &= ~(0x02);

    // wait for PLL Lock
    clk_ready_tries = 0;
    do
    {
        clk_ready_tries++;
    } while(BTZB_PLL_NOT_LOCKED && (clk_ready_tries < CLK_READY_RETRIES));
    
    if((clk_ready_tries >= CLK_READY_RETRIES) && BTZB_PLL_NOT_LOCKED)
    {
        BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG1 |= BTZBSYS_SUBSYS_CNTRL_REG1_subsys_bypass_pll_lock_Msk;
        while(BTZB_PLL_NOT_LOCKED);
    }

    /* Unlock system for clock configuration */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;


    /* SPLLPWDN     = ${SPLLCON_SPLLPWDN_VALUE}     */
    /* SPLLFLOCK    = ${SPLLCON_SPLLFLOCK_VALUE}    */
    /* SPLLRST      = ${SPLLCON_SPLLRST_VALUE}      */    
    /* SPLLPOSTDIV1 = ${SPLLCON_SPLLPOSTDIV1_VALUE} */
    /* SPLLPOSTDIV2 = ${SPLLCON_SPLLPOSTDIV2_VALUE} */    
    /* SPLL_BYP     = ${SPLLCON_SPLL_BYP_VALUE}     */
    CRU_REGS->CRU_${SPLLCON_REG} = 0x${SPLLCON_VALUE};


    /* OSWEN    = ${OSCCON_OSWEN_VALUE}    */
    /* SOSCEN   = ${OSCCON_SOSCEN_VALUE}   */
    /* CF       = ${OSCCON_CF_VALUE}       */
    /* SLPEN    = ${OSCCON_SLPEN_VALUE}    */
    /* CLKLOCK  = ${OSCCON_CLKLOCK_VALUE}  */
    /* NOSC     = ${OSCCON_NOSC_VALUE}     */
    /* WAKE2SPD = ${OSCCON_WAKE2SPD_VALUE} */
    /* DRMEN    = ${OSCCON_DRMEN_VALUE}    */
    /* FRCDIV   = ${OSCCON_FRCDIV_VALUE}   */
    CRU_REGS->CRU_${OSCCON_REG} = 0x${OSCCON_VALUE};

    CRU_REGS->CRU_OSCCONSET = CRU_OSCCON_OSWEN_Msk;  /* request oscillator switch to occur */

    while(CRU_REGS->CRU_OSCCON & CRU_OSCCON_OSWEN_Msk);        /* wait for indication of successful clock change before proceeding */

<#if CONFIG_SYS_CLK_PBDIV1 != 1>
    <#lt>    /* Peripheral Bus 1 is by default enabled, set its divisor */
    <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV1} */
    <#lt>    CRU_REGS->CRU_${PBREGNAME1} = CRU_PB1DIV_PBDIVON_Msk | CRU_PB1DIV_PBDIV(${CONFIG_SYS_CLK_PBDIV1 - 1});

</#if>
<#if CONFIG_SYS_CLK_PBCLK2_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV2 != 1>
        <#lt>    /* Peripheral Bus 2 is by default enabled, set its divisor */
        <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV2} */
        <#lt>    CRU_REGS->CRU_${PBREGNAME2} = CRU_PB2DIV_PBDIVON_Msk | CRU_PB2DIV_PBDIV(${CONFIG_SYS_CLK_PBDIV2 - 1});

    </#if>
<#else>
    /* Disable Peripheral Bus 2 */
    CRU_REGS->CRU_${PBREGNAME2}CLR = ${PBONMASK2};

</#if>
<#if CONFIG_SYS_CLK_PBCLK3_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV3 != 1>
        <#lt>    /* Peripheral Bus 3 is by default enabled, set its divisor */
        <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV3} */
        <#lt>    CRU_REGS->CRU_${PBREGNAME3} = CRU_PB3DIV_PBDIVON_Msk | CRU_PB3DIV_PBDIV(${CONFIG_SYS_CLK_PBDIV3 - 1});

    </#if>
<#else>
    /* Disable Peripheral Bus 3 */
    CRU_REGS->CRU_${PBREGNAME3}CLR = ${PBONMASK3};

</#if>


<#list 1..NUM_REFOSC_ELEMENTS as i>
    <#assign ENBL = "CONFIG_SYS_CLK_REFCLK"+i+"_ENABLE">
    <#assign REFCONREG = "REFCON"+i+"REG">
    <#assign ROSELVAL = "CONFIG_SYS_CLK_REFCLK_SOURCE"+i>
    <#assign REFTRIMREG = "REFTRIM"+i+"REG">
    <#assign ROTRIMVAL = "CONFIG_SYS_CLK_ROTRIM"+i>
    <#assign ONMASK = "REFOCON_ONMASK"+i>
    <#assign REFCLKOE = "CONFIG_SYS_CLK_REFCLK"+i+"_OE">
    <#assign OEMASK = "REFOCON_OEMASK"+i>
    <#assign REFCONVAL = "REFOCON"+i+"_VALUE">
    <#assign REFOTRIMVAL = "REFO"+i+"TRIM_VALUE">
    <#assign REFOCONRODIV = "CONFIG_SYS_CLK_RODIV"+i>
    <#assign REFOCONRSLP = "CONFIG_SYS_CLK_REFCLK_RSLP" +i>
    <#assign REFOCONSIDL = "CONFIG_SYS_CLK_REFCLK_SIDL" +i>
<#if .vars[ENBL] = true>
    /* Set up Reference Clock ${i} */
        <#lt>    /* REFO${i}CON register */
        <#lt>    /* ROSEL =  ${.vars[ROSELVAL]} */
        <#lt>    /* DIVSWEN = 1 */
        <#lt>    /* RSLP = ${.vars[REFOCONRSLP]?c} */ 
        <#lt>    /* SIDL = ${.vars[REFOCONSIDL]?c} */ 
        <#lt>    /* RODIV = ${.vars[REFOCONRODIV]} */
        <#lt>    CRU_REGS->CRU_${.vars[REFCONREG]} = ${.vars[REFCONVAL]};

    <#if .vars[REFOTRIMVAL] != "0x0">
        <#lt>    /* REFO${i}TRIM register */
        <#lt>    /* ROTRIM = ${.vars[ROTRIMVAL]} */
        <#lt>    CRU_REGS->CRU_${.vars[REFTRIMREG]} = ${.vars[REFOTRIMVAL]};

    </#if>
    <#if (.vars[REFCLKOE]?has_content) && (.vars[REFCLKOE] == true)>
        <#lt>    /* Enable oscillator (ON bit) and Enable Output (OE bit) */
        <#lt>    CRU_REGS->CRU_${.vars[REFCONREG]}SET = ${.vars[OEMASK]} | ${.vars[ONMASK]};

    <#else>
        <#lt>    /* Enable oscillator (ON bit) */
        <#lt>    CRU_REGS->CRU_${.vars[REFCONREG]}SET = ${.vars[ONMASK]};

    </#if>
</#if>
</#list>

    /* Peripheral Clock Generators */
<#list 1..PER_GEN_REG_COUNT as i>
    <#assign CFGPCLKGEN_REG_VALUE = "CFGPCLKGEN" + i + "_REG">
    CFG_REGS->CFG_CFGPCLKGEN${i} = 0x${.vars[CFGPCLKGEN_REG_VALUE]};
</#list>

    /* Peripheral Module Disable Configuration */

<#if PMDLOCK_ENABLE?? && PMDLOCK_ENABLE == true>
    CFG_REGS->CFG_CFGCON0CLR = CFG_CFGCON0_PMDLOCK_Msk;
</#if>

<#list 1..PMD_COUNT + 1 as i>
    <#assign PMDREG_VALUE = "PMD" + i + "_REG_VALUE">
    <#if .vars[PMDREG_VALUE]?? && .vars[PMDREG_VALUE] != "None">
        <#lt>    CFG_REGS->CFG_PMD${i} = 0x${.vars[PMDREG_VALUE]};
    </#if>
</#list>

<#if PMDLOCK_ENABLE?? && PMDLOCK_ENABLE == true>
    CFG_REGS->CFG_CFGCON0SET = CFG_CFGCON0_PMDLOCK_Msk;
</#if>

    /* Lock system since done with clock configuration */
    CFG_REGS->CFG_SYSKEY = 0x33333333;

    // Change src_clk source to PLL CLK
    BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG1 |= 0x00000010;

<#if ZIGBEE_CLOCK_ENABLE == true>
    // set aclb_reset_n[24], bt_en_main_clk[20] zb_en_main_clk[4]
    BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG0 = 0x01100010;
<#elseif BLE_CLOCK_ENABLE == true>
    // set aclb_reset_n[24], bt_en_main_clk[20]
    BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG0 = 0x01100000;
<#else>
    // set aclb_reset_n[24]
    BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG0 = 0x01000000;
</#if>
}
