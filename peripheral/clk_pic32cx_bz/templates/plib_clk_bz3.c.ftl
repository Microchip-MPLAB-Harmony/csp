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
<#if PRODUCT_FAMILY?contains("PIC32CX_BZ6")>
static void CLOCK_RF_Write_Reg(uint8_t addr, uint16_t value)
{
    BLE_REGS->BLE_SPI_REG_ADDR = addr;
    BLE_REGS->BLE_SPI_WR_DATA = value;
    BLE_REGS->BLE_RFPWRMGMT |= 0x00100000U;
    while ((BLE_REGS->BLE_RFPWRMGMT & 0x00100000U) != 0U)
    {
        /* Do nothing */
    }
}
</#if>
// *****************************************************************************
/* Function:
    void CLOCK_Initialize( void )

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

void CLOCK_Initialize( void )
{
    //check CLDO ready
    while ((CFG_REGS->CFG_MISCSTAT & CFG_MISCSTAT_CLDORDY_Msk) == 0U)
    {
        /* Nothing to do */
    }
<#if PRODUCT_FAMILY?contains("PIC32CX_BZ6")>
    CLOCK_RF_Write_Reg(0x27U, 0x2078U);

    //Current Oscillator is 8MHz FRC or 16MHz POSC
    if ((CRU_REGS->CRU_OSCCON & CRU_OSCCON_COSC_Msk) != CRU_OSCCON_COSC_SPLL)
    {
        //Setup 128MHz PLL
        CLOCK_RF_Write_Reg(0x2EU, 0x4328U);

        /* MISRAC 2012 deviation block start */
        /* MISRA C-2012 Rule 11.1 deviated 1 time. Deviation record ID -  H3_MISRAC_2012_R_11_1_DR_1 */
        <#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
        <#if COMPILER_CHOICE == "XC32">
        #pragma GCC diagnostic push
        #pragma GCC diagnostic ignored "-Wunknown-pragmas"
        </#if>
        #pragma coverity compliance block deviate:1 "MISRA C-2012 Rule 11.1" "H3_MISRAC_2012_R_11_1_DR_1"

        </#if>
        /* Configure Prefetch, Wait States by calling the ROM function whose address is available at address 0xF2D0 */
        typedef void (*FUNC_PCHE_SETUP)(uint32_t setup);
        (void)((FUNC_PCHE_SETUP)(*(uint32_t*)0xF2D0))((PCHE_REGS->PCHE_CHECON & (~(PCHE_CHECON_PFMWS_Msk | PCHE_CHECON_ADRWS_Msk | PCHE_CHECON_PREFEN_Msk)))
                                        | (PCHE_CHECON_PFMWS(${CONFIG_CHECON_PFMWS}) | PCHE_CHECON_PREFEN(${CONFIG_CHECON_PREFEN}) | PCHE_CHECON_ADRWS(${CONFIG_CHECON_ADRWS})));
        <#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>

        #pragma coverity compliance end_block "MISRA C-2012 Rule 11.1"
        <#if COMPILER_CHOICE == "XC32">
        #pragma GCC diagnostic pop
        </#if>
        /* MISRA C-2012 Rule 11.1 deviation block end  */
    </#if>
    }
</#if>
    
<#if ((CoreSeries?contains("PIC32WM_BZ36")) || (CoreSeries?contains("PIC32CXBZ36")))>
    /* MISRAC 2012 deviation block start */
    /* MISRA C-2012 Rule 11.1 deviated 1 time. Deviation record ID -  H3_MISRAC_2012_R_11_1_DR_1 */
    <#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunknown-pragmas"
    #pragma coverity compliance block deviate:1 "MISRA C-2012 Rule 11.1" "H3_MISRAC_2012_R_11_1_DR_1"
    </#if>

    /* Configure Prefetch, Wait States by calling the ROM function whose address is available at address 0xF2D0 */
    typedef void (*FUNC_PCHE_SETUP)(uint32_t setup);
    (void)((FUNC_PCHE_SETUP)(*(uint32_t*)0xF2D0))((PCHE_REGS->PCHE_CHECON & (~(PCHE_CHECON_PFMWS_Msk | PCHE_CHECON_ADRWS_Msk | PCHE_CHECON_PREFEN_Msk)))
                                    | (PCHE_CHECON_PFMWS(${CONFIG_CHECON_PFMWS}) | PCHE_CHECON_PREFEN(${CONFIG_CHECON_PREFEN})  | PCHE_CHECON_ADRWS(${CONFIG_CHECON_ADRWS})));

    <#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
    #pragma coverity compliance end_block "MISRA C-2012 Rule 11.1"
    #pragma GCC diagnostic pop
    </#if>
    /* MISRAC 2012 deviation block end */	
</#if>

<#if !((PRODUCT_FAMILY?contains("PIC32CX_BZ6")) || (CoreSeries?contains("PIC32WM_BZ36")) || (CoreSeries?contains("PIC32CXBZ36")))>
	//programming 4ms delay -  programming subsys_xtal_ready_delay
    //check xtal spec for delay required
    BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG1 = ((BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG1 & ~BTZBSYS_SUBSYS_CNTRL_REG1_subsys_xtal_ready_delay_Msk)
                                                | ((0x01UL) << BTZBSYS_SUBSYS_CNTRL_REG1_subsys_xtal_ready_delay_Pos));
</#if>
    //wait for crystal ready
    while((BTZBSYS_REGS->BTZBSYS_SUBSYS_STATUS_REG1 & BTZBSYS_SUBSYS_STATUS_REG1_xtal_ready_out_Msk) != BTZBSYS_SUBSYS_STATUS_REG1_xtal_ready_out_Msk)
    {
        /* Nothing to do */
    }
    CFG_REGS->CFG_SYSKEY = 0x00000000U; // Write junk to lock it if it is already unlocked
    CFG_REGS->CFG_SYSKEY = 0xAA996655U;
    CFG_REGS->CFG_SYSKEY = 0x556699AAU;
    CRU_REGS->CRU_OSCCON = 0x200U;// switch to XO

    //Enable oscillator switch from COSC to NOSC
    CRU_REGS->CRU_OSCCONSET = CRU_OSCCON_OSWEN_Msk;

    //wait for successful clock change before continuing
    while ((CRU_REGS->CRU_OSCCON & CRU_OSCCON_OSWEN_Msk) != 0U)
    {
        /* Nothing to do */
    }

    //set PLL_disable
     BLE_REGS->BLE_DPLL_RG2 |= 0x02U;

    // set PLL_enable
    BLE_REGS->BLE_DPLL_RG2 &= ((uint8_t)~(0x02U));

    // Set MISC[24]=0, CLKGEN_PLLRST = 0
    CFG_REGS->CFG_MISCSTAT  &= 0x00FFFFFFU;
<#if PRODUCT_FAMILY?contains("PIC32CX_BZ3") || PRODUCT_FAMILY?contains("PIC32CX_BZ6")>
    // Setting CPU QoS and FC QoS to same priority
    <#if PRODUCT_FAMILY?contains("PIC32CX_BZ3")>
        CFG_REGS->CFG_CFGPGQOS = (CFG_REGS->CFG_CFGPGQOS & ~(CFG_CFGPGQOS_FCQOS_Msk | CFG_CFGPGQOS_CPUQOS_Msk)) | ((0x03UL << CFG_CFGPGQOS_FCQOS_Pos) | (0x03UL << CFG_CFGPGQOS_CPUQOS_Pos));
    <#elseif PRODUCT_FAMILY?contains("PIC32CX_BZ6")>
        CFG_REGS->CFG_CFGPGQOS1 = (CFG_REGS->CFG_CFGPGQOS1 & ~(CFG_CFGPGQOS1_FCQOS_Msk | CFG_CFGPGQOS1_CPUQOS_Msk)) | ((0x03UL << CFG_CFGPGQOS1_FCQOS_Pos) | (0x03UL << CFG_CFGPGQOS1_CPUQOS_Pos));
    </#if>
</#if>

    //programming delay for pll lock - 500 us
    //32 us steps - check pll spec for final value
    BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG3 = ((BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG3 & ~BTZBSYS_SUBSYS_CNTRL_REG3_subsys_pll_ready_delay_Msk )
                                                   | ((0x02UL) << BTZBSYS_SUBSYS_CNTRL_REG3_subsys_pll_ready_delay_Pos));

    /* Unlock system for clock configuration */
    CFG_REGS->CFG_SYSKEY = 0x00000000U;
    CFG_REGS->CFG_SYSKEY = 0xAA996655U;
    CFG_REGS->CFG_SYSKEY = 0x556699AAU;


    /* SPLLPWDN     = ${SPLLCON_SPLLPWDN_VALUE}     */
    /* SPLLFLOCK    = ${SPLLCON_SPLLFLOCK_VALUE}    */
    /* SPLLRST      = ${SPLLCON_SPLLRST_VALUE}      */
    /* SPLLPOSTDIV1 = ${SPLLCON_SPLLPOSTDIV1_VALUE} */
    /* SPLLPOSTDIV2 = ${SPLLCON_SPLLPOSTDIV2_VALUE} */
    /* SPLL_BYP     = ${SPLLCON_SPLL_BYP_VALUE}     */
    CRU_REGS->CRU_${SPLLCON_REG} = 0x${SPLLCON_VALUE}U;

    //wait for PLL Lock
    while((BTZBSYS_REGS -> BTZBSYS_SUBSYS_STATUS_REG1 & 0x03U) != 0x03U)
    {
        /* Nothing to do */
    }

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

    while((CRU_REGS->CRU_OSCCON & CRU_OSCCON_OSWEN_Msk) != 0U)       /* wait for indication of successful clock change before proceeding */
    {
        /* Nothing to do */
    }
<#if CONFIG_SYS_CLK_PBDIV1 != 1>
    <#lt>    /* Peripheral Bus 1 is by default enabled, set its divisor */
    <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV1} */
    <#lt>    CRU_REGS->CRU_${PBREGNAME1} = CRU_PB1DIV_PBDIVON_Msk | CRU_PB1DIV_PBDIV(${CONFIG_SYS_CLK_PBDIV1 - 1}U);

</#if>
<#if CONFIG_SYS_CLK_PBCLK2_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV2 != 1>
        <#lt>    /* Peripheral Bus 2 is by default enabled, set its divisor */
        <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV2} */
        <#lt>    CRU_REGS->CRU_${PBREGNAME2} = CRU_PB2DIV_PBDIVON_Msk | CRU_PB2DIV_PBDIV(${CONFIG_SYS_CLK_PBDIV2 - 1}U);

    </#if>
<#else>
    /* Disable Peripheral Bus 2 */
    CRU_REGS->CRU_${PBREGNAME2}CLR = ${PBONMASK2};

</#if>
<#if CONFIG_SYS_CLK_PBCLK3_ENABLE == true>
    <#if CONFIG_SYS_CLK_PBDIV3 != 1>
        <#lt>    /* Peripheral Bus 3 is by default enabled, set its divisor */
        <#lt>    /* PBDIV = ${CONFIG_SYS_CLK_PBDIV3} */
        <#lt>    CRU_REGS->CRU_${PBREGNAME3} = CRU_PB3DIV_PBDIVON_Msk | CRU_PB3DIV_PBDIV(${CONFIG_SYS_CLK_PBDIV3 - 1}U);

    </#if>
<#else>
    /* Disable Peripheral Bus 3 */
    CRU_REGS->CRU_${PBREGNAME3}CLR = ${PBONMASK3}U;

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
        <#lt>    CRU_REGS->CRU_${.vars[REFCONREG]} = ${.vars[REFCONVAL]}U;

    <#if .vars[REFOTRIMVAL] != "0x0">
        <#lt>    /* REFO${i}TRIM register */
        <#lt>    /* ROTRIM = ${.vars[ROTRIMVAL]} */
        <#lt>    CRU_REGS->CRU_${.vars[REFTRIMREG]} = ${.vars[REFOTRIMVAL]}U;

    </#if>
    <#if (.vars[REFCLKOE]?has_content) && (.vars[REFCLKOE] == true)>
        <#lt>    /* Enable oscillator (ON bit) and Enable Output (OE bit) */
        <#lt>    CRU_REGS->CRU_${.vars[REFCONREG]}SET = ${.vars[OEMASK]}U | ${.vars[ONMASK]}U;

    <#else>
        <#lt>    /* Enable oscillator (ON bit) */
        <#lt>    CRU_REGS->CRU_${.vars[REFCONREG]}SET = ${.vars[ONMASK]}U;

    </#if>
</#if>
</#list>

    /* Peripheral Clock Generators */
<#list 1..PER_GEN_REG_COUNT as i>
    <#assign CFGPCLKGEN_REG_VALUE = "CFGPCLKGEN" + i + "_REG">
    CFG_REGS->CFG_CFGPCLKGEN${i} = 0x${.vars[CFGPCLKGEN_REG_VALUE]}U;
</#list>

    /* Peripheral Module Disable Configuration */

<#if PMDLOCK_ENABLE?? && PMDLOCK_ENABLE == true>
    CFG_REGS->CFG_CFGCON0CLR = CFG_CFGCON0_PMDLOCK_Msk;
</#if>

<#list 1..PMD_COUNT + 1 as i>
    <#assign PMDREG_VALUE = "PMD" + i + "_REG_VALUE">
    <#if .vars[PMDREG_VALUE]?? && .vars[PMDREG_VALUE] != "None">
        <#lt>    CFG_REGS->CFG_PMD${i} = 0x${.vars[PMDREG_VALUE]}U;
    </#if>
</#list>

<#if PMDLOCK_ENABLE?? && PMDLOCK_ENABLE == true>
    CFG_REGS->CFG_CFGCON0SET = CFG_CFGCON0_PMDLOCK_Msk;
</#if>

    // Change src_clk source to PLL CLK
    BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG1 |= 0x00000010U;

<#if ZIGBEE_CLOCK_ENABLE == true>
    // set aclb_reset_n[24], bt_en_main_clk[20] zb_en_main_clk[4]
    BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG0 |= 0x01100010U;
<#elseif BLE_CLOCK_ENABLE == true>
    // set aclb_reset_n[24], bt_en_main_clk[20]
    BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG0 |= 0x01100000U;
<#else>
    // set aclb_reset_n[24]
    BTZBSYS_REGS->BTZBSYS_SUBSYS_CNTRL_REG0 |= 0x01000000U;
</#if>

<#if USBPLL_ENABLE??>
<#if USBPLL_ENABLE == true>
        /* Configure UPLL */
        /* UPLLBSWSEL   = ${UPLLCON_UPLLBSWSEL_VALUE} */
        /* UPLLPWDN     = ${UPLLCON_UPLLPWDN_VALUE} */
        /* UPLLPOSTDIV1 = ${UPLLCON_UPLLPOSTDIV1_VALUE} */
        /* UPLLFLOCK    = ${UPLLCON_UPLLFLOCK_VALUE} */
        /* UPLLRST      = ${UPLLCON_UPLLRST_VALUE} */
        /* UPLLFBDIV    = ${UPLLCON_UPLLFBDIV_VALUE} */
        /* UPLLREFDIV   = ${UPLLCON_UPLLREFDIV_VALUE} */
        /* UPLL_BYP     = ${UPLLCON_UPLL_BYP_VALUE} */
        CRU_REGS->CRU_${UPLLCON_REG} = 0x${UPLLCON_VALUE};
<#else>
        /* Power down the UPLL */
        CRU_REGS->CRU_${UPLLCON_REG} = CRU_UPLLCON_UPLLPWDN_Msk;
</#if>
</#if>

<#if EPLL_ENABLE??>
<#if EPLL_ENABLE == true>
        /* Configure EPLL */
        /* EPLLBSWSEL   = ${EPLLCON_EPLLBSWSEL_VALUE} */
        /* EPLLPWDN     = ${EPLLCON_EPLLPWDN_VALUE} */
        /* EPLLPOSTDIV1 = ${EPLLCON_EPLLPOSTDIV1_VALUE} */
        /* EPLLFLOCK    = ${EPLLCON_EPLLFLOCK_VALUE} */
        /* EPLLRST      = ${EPLLCON_EPLLRST_VALUE} */
        /* EPLLFBDIV    = ${EPLLCON_EPLLFBDIV_VALUE} */
        /* EPLLREFDIV   = ${EPLLCON_EPLLREFDIV_VALUE} */
        /* EPLL_BYP     = ${EPLLCON_EPLL_BYP_VALUE} */
        CRU_REGS->CRU_${EPLLCON_REG} = 0x${EPLLCON_VALUE}U;

        /* EPLLPOSTDIV2 = ${EPLLPOSTDIV2} */
        CRU_REGS->CRU_APLLCON = ${EPLLPOSTDIV2}U;
        CFG_REGS->CFG_CFGCON0SET = CFG_CFGCON0_EPLLHWMD_Msk;
<#else>
        /* Power down the EPLL */
        CRU_REGS->CRU_${EPLLCON_REG} = CRU_EPLLCON_EPLLPWDN_Msk;
</#if>
</#if>

<#if BTPLL_ENABLE??>
<#if BTPLL_ENABLE == true>
        /* Configure BYPLL */
        /* BTPLLBSWSEL   = ${BTPLLCON_BTPLLBSWSEL_VALUE} */
        /* BTPLLPWDN     = ${BTPLLCON_BTPLLPWDN_VALUE} */
        /* BTPLLPOSTDIV1 = ${BTPLLCON_BTPLLPOSTDIV1_VALUE} */
        /* BTPLLFLOCK    = ${BTPLLCON_BTPLLFLOCK_VALUE} */
        /* BTPLLRST      = ${BTPLLCON_BTPLLRST_VALUE} */
        /* BTPLLFBDIV    = ${BTPLLCON_BTPLLFBDIV_VALUE} */
        /* BTPLLREFDIV   = ${BTPLLCON_BTPLLREFDIV_VALUE} */
        /* BTCLKOUTEN    = ${BTPLLCON_BTCLKOUTEN_VALUE} */
        /* BTPLLICLK     = ${BTPLLCON_BTPLLCLK_VALUE} */
        /* BTPLL_BYP     = ${BTPLLCON_BTPLL_BYP_VALUE} */
        ${BTPLLCON_REG} = 0x${BTPLLCON_VALUE};
<#else>
        /* Power down the BTPLL */
        BTPLLCONbits.BTPLLPWDN = 1U;
</#if>
</#if>
    /* Lock system since done with clock configuration */
    CFG_REGS->CFG_SYSKEY = 0x33333333U;
}
