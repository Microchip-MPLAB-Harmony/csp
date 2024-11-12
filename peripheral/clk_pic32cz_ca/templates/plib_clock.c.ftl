/*******************************************************************************
 CLOCK PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_clock.c

  Summary:
    CLOCK PLIB Implementation File.

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

#include "plib_clock.h"
#include "device.h"

<#if CONFIG_CLOCK_XOSC_ENABLE == true>
static void OSCCTRL_Initialize(void)
{
<#assign agcEnable = "CONFIG_CLOCK_XOSC_AGC_ENABLE" >
<#assign cfdPrescalar = "CONFIG_CLOCK_XOSC_CFDPRESC" >
<#assign startup = "CONFIG_CLOCK_XOSC_STARTUP" >
<#assign switchBack = "CONFIG_CLOCK_XOSC_SWBEN" >
<#assign mode = "XOSC_OSCILLATOR_MODE" >
<#assign cfdEnable = "CONFIG_CLOCK_XOSC_CFDEN" >
<#assign UsbHsDiv = "CONFIG_CLOCK_XOSC_USBHSDIV" >
<#assign onDemand = "CONFIG_CLOCK_XOSC_ONDEMAND" >
    /****************** XOSC Initialization ********************************/

    /* Configure External Oscillator */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_XOSCCTRLA = OSCCTRL_XOSCCTRLA_STARTUP(${.vars[startup]}U)
                                                             ${.vars[switchBack]?then('| OSCCTRL_XOSCCTRLA_SWBEN_Msk',' ')}${.vars[agcEnable]?then(' | OSCCTRL_XOSCCTRLA_AGC_Msk',' ')}
                                                             ${(.vars[onDemand] == "ENABLE")?then('| OSCCTRL_XOSCCTRLA_ONDEMAND_Msk',' ')}
                                                             ${.vars[cfdEnable]?then('| OSCCTRL_XOSCCTRLA_CFDEN_Msk | OSCCTRL_XOSCCTRLA_CFDPRESC(${.vars[cfdPrescalar]}U)',' ')}
                                                             ${(.vars[UsbHsDiv] != "0x0")?then('| OSCCTRL_XOSCCTRLA_USBHSDIV(${.vars[UsbHsDiv]}U)',' ')}
                                                             ${(.vars[mode] == "1")?then('| OSCCTRL_XOSCCTRLA_XTALEN_Msk',' ')} | OSCCTRL_XOSCCTRLA_ENABLE_Msk;</@compress>
    <#if .vars[onDemand] != "ENABLE">
    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCRDY_Msk) != OSCCTRL_STATUS_XOSCRDY_Msk)
    {
        /* Waiting for the XOSC Ready state */
    }
    </#if>
}
</#if>

static void OSC32KCTRL_Initialize(void)
{
<#if CONF_CLOCK_XOSC32K_ENABLE == true>
    /****************** XOSC32K initialization  ******************************/

    /* Configure 32K External Oscillator */
    <@compress single_line=true>OSC32KCTRL_REGS->OSC32KCTRL_XOSC32K = OSC32KCTRL_XOSC32K_STARTUP(${XOSC32K_STARTUP}U) | OSC32KCTRL_XOSC32K_ENABLE_Msk | OSC32KCTRL_XOSC32K_CGM(${XOSC32K_CGM}U)
                                                               ${(XOSC32K_ONDEMAND == "ENABLE")?then('| OSC32KCTRL_XOSC32K_ONDEMAND_Msk',' ')}
                                                               ${XOSC32K_ENSL?then('| OSC32KCTRL_XOSC32K_ENSL_Msk',' ')}
                                                               ${XOSC32K_BOOST?then('| OSC32KCTRL_XOSC32K_BOOST_Msk',' ')}
                                                               ${(XOSC32K_OSCILLATOR_MODE == "1")?then('| OSC32KCTRL_XOSC32K_XTALEN_Msk',' ')};</@compress>

    <#if XOSC32K_CFDEN == true >
    /* Enable clock failure detection */
    OSC32KCTRL_REGS->OSC32KCTRL_CFDCTRL = OSC32KCTRL_CFDCTRL_CFDEN_Msk  ${XOSC32K_CFDPRESC?then('| OSC32KCTRL_CFDCTRL_CFDPRESC_Msk','')} ${XOSC32K_SWBACK?then('| OSC32KCTRL_CFDCTRL_SWBACK_Msk','')};
    </#if>
    <#if XOSC32K_ONDEMAND != "ENABLE">
    while(!((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_XOSC32KRDY_Msk) == OSC32KCTRL_STATUS_XOSC32KRDY_Msk))
    {
        /* Waiting for the XOSC32K Ready state */
    }
    </#if>
</#if>

    OSC32KCTRL_REGS->OSC32KCTRL_CLKSELCTRL = OSC32KCTRL_CLKSELCTRL_RTCSEL(${CONFIG_CLOCK_RTC_SRC}U);
}

<#if CONFIG_CLOCK_PLL0_ENABLE == true >
static void PLL0_Initialize(void)
{
    /* Enable Additional Voltage Regulator */
    SUPC_REGS->SUPC_VREGCTRL |= SUPC_VREGCTRL_AVREGEN(4U);
    while ((SUPC_REGS->SUPC_STATUS & (4U << SUPC_STATUS_ADDVREGRDY_Pos)) != (4U << SUPC_STATUS_ADDVREGRDY_Pos))
    {
        /* Do Nothing */
    }

    <#if CONFIG_CLOCK_PLL0_REF_CLOCK == "0">
    GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_1_INDEX}] = GCLK_PCHCTRL_GEN(${GCLK_ID_1_GENSEL}U)${GCLK_ID_1_WRITELOCK?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;
    while ((GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_1_INDEX}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
    </#if>

    /****************** PLL0 Initialization  *********************************/

    /* Configure PLL0 */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_PLL0REFDIV = OSCCTRL_PLL0REFDIV_REFDIV(${CONFIG_CLOCK_PLL0_PLLREFDIV_REFDIV}U);</@compress>
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_PLL0FBDIV = OSCCTRL_PLL0FBDIV_FBDIV(${CONFIG_CLOCK_PLL0_PLLFBDIV_FBDIV}U);</@compress>

    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_FRACDIV0 = OSCCTRL_FRACDIV0_REMDIV(${CONFIG_CLOCK_PLL0_FRACDIV_REMDIV}U) |
                                                                 OSCCTRL_FRACDIV0_INTDIV(${CONFIG_CLOCK_PLL0_FRACDIV_INTDIV}U);</@compress>
    while((OSCCTRL_REGS->OSCCTRL_SYNCBUSY & OSCCTRL_SYNCBUSY_FRACDIV0_Msk) == OSCCTRL_SYNCBUSY_FRACDIV0_Msk)
    {
        /* Waiting for the synchronization */
    }

    <#assign OSCCTRL_PLL0POSTDIVA_VALUE = "">
    <#list 0..4 as i>
    <#assign PLL0_PLLPOSTDIVA_OUTEN = "CONFIG_CLOCK_PLL0_PLLPOSTDIVA_OUTEN" + i>
    <#assign CONFIG_CLOCK_PLL0_PLLPOSTDIVA_POSTDIV = "CONFIG_CLOCK_PLL0_PLLPOSTDIVA_POSTDIV" + i>
    <#assign OSCCTRL_PLL0POSTDIVA_POSTDIV = "OSCCTRL_PLL0POSTDIVA_POSTDIV" + i>
        <#if .vars[PLL0_PLLPOSTDIVA_OUTEN]?? && .vars[PLL0_PLLPOSTDIVA_OUTEN] == true>
            <#if OSCCTRL_PLL0POSTDIVA_VALUE != "">
                <#assign OSCCTRL_PLL0POSTDIVA_VALUE = OSCCTRL_PLL0POSTDIVA_VALUE + " | " + "OSCCTRL_PLL0POSTDIVA_OUTEN" + i + "_Msk" + " | " + OSCCTRL_PLL0POSTDIVA_POSTDIV + "(" + .vars[CONFIG_CLOCK_PLL0_PLLPOSTDIVA_POSTDIV] + "U)">
            <#else>
                <#assign OSCCTRL_PLL0POSTDIVA_VALUE = "OSCCTRL_PLL0POSTDIVA_OUTEN" + i + "_Msk" + " | " + OSCCTRL_PLL0POSTDIVA_POSTDIV + "(" + .vars[CONFIG_CLOCK_PLL0_PLLPOSTDIVA_POSTDIV] + "U)">
            </#if>
        </#if>
    </#list>
    <#if OSCCTRL_PLL0POSTDIVA_VALUE?has_content>
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_PLL0POSTDIVA = ${OSCCTRL_PLL0POSTDIVA_VALUE};</@compress>
    </#if>

    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_PLL0CTRL |= OSCCTRL_PLL0CTRL_BWSEL(${CONFIG_CLOCK_PLL0_BWSEL}U) | OSCCTRL_PLL0CTRL_REFSEL(${CONFIG_CLOCK_PLL0_REF_CLOCK}U)
                                                                 ${(CONFIG_CLOCK_PLL0_ONDEMAND == "1")?then('| OSCCTRL_PLL0CTRL_ONDEMAND_Msk',' ')}
                                                                 | OSCCTRL_PLL0CTRL_ENABLE_Msk;</@compress>
    <#if CONFIG_CLOCK_PLL0_ONDEMAND != "1">

    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_PLL0LOCK_Msk) != OSCCTRL_STATUS_PLL0LOCK_Msk)
    {
        /* Waiting for the Ready state */
    }
    </#if>
}
</#if>

<#if CONFIG_CLOCK_PLL1_ENABLE == true >
static void PLL1_Initialize(void)
{
    /* Enable Additional Voltage Regulator */
    SUPC_REGS->SUPC_VREGCTRL |= SUPC_VREGCTRL_AVREGEN(4U);
    while ((SUPC_REGS->SUPC_STATUS & (4U << SUPC_STATUS_ADDVREGRDY_Pos)) != (4U << SUPC_STATUS_ADDVREGRDY_Pos))
    {
        /* Do Nothing */
    }

    <#if CONFIG_CLOCK_PLL1_REF_CLOCK == "0">
    GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_1_INDEX}] = GCLK_PCHCTRL_GEN(${GCLK_ID_1_GENSEL})${GCLK_ID_1_WRITELOCK?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;
    while ((GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_1_INDEX}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
    </#if>

    /****************** PLL1 Initialization  *********************************/

    /* Configure PLL1 */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_PLL1REFDIV = OSCCTRL_PLL1REFDIV_REFDIV(${CONFIG_CLOCK_PLL1_PLLREFDIV_REFDIV}U);</@compress>
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_PLL1FBDIV = OSCCTRL_PLL1FBDIV_FBDIV(${CONFIG_CLOCK_PLL1_PLLFBDIV_FBDIV}U);</@compress>

    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_FRACDIV1 = OSCCTRL_FRACDIV1_REMDIV(${CONFIG_CLOCK_PLL1_FRACDIV_REMDIV}U) |
                                                                 OSCCTRL_FRACDIV1_INTDIV(${CONFIG_CLOCK_PLL1_FRACDIV_INTDIV}U);</@compress>
    while((OSCCTRL_REGS->OSCCTRL_SYNCBUSY & OSCCTRL_SYNCBUSY_FRACDIV1_Msk) == OSCCTRL_SYNCBUSY_FRACDIV1_Msk)
    {
        /* Waiting for the synchronization */
    }

    <#assign OSCCTRL_PLL1POSTDIVA_VALUE = "">
    <#list 0..4 as i>
    <#assign PLL1_PLLPOSTDIVA_OUTEN = "CONFIG_CLOCK_PLL1_PLLPOSTDIVA_OUTEN" + i>
    <#assign CONFIG_CLOCK_PLL1_PLLPOSTDIVA_POSTDIV = "CONFIG_CLOCK_PLL1_PLLPOSTDIVA_POSTDIV" + i>
    <#assign OSCCTRL_PLL1POSTDIVA_POSTDIV = "OSCCTRL_PLL1POSTDIVA_POSTDIV" + i>
        <#if .vars[PLL1_PLLPOSTDIVA_OUTEN]?? && .vars[PLL1_PLLPOSTDIVA_OUTEN] == true>
            <#if OSCCTRL_PLL1POSTDIVA_VALUE != "">
                <#assign OSCCTRL_PLL1POSTDIVA_VALUE = OSCCTRL_PLL1POSTDIVA_VALUE + " | " + "OSCCTRL_PLL1POSTDIVA_OUTEN" + i + "_Msk" + " | " + OSCCTRL_PLL1POSTDIVA_POSTDIV + "(" + .vars[CONFIG_CLOCK_PLL1_PLLPOSTDIVA_POSTDIV] + "U)">
            <#else>
                <#assign OSCCTRL_PLL1POSTDIVA_VALUE = "OSCCTRL_PLL1POSTDIVA_OUTEN" + i + "_Msk" + " | " + OSCCTRL_PLL1POSTDIVA_POSTDIV + "(" + .vars[CONFIG_CLOCK_PLL1_PLLPOSTDIVA_POSTDIV] + "U)">
            </#if>
        </#if>
    </#list>
    <#if OSCCTRL_PLL1POSTDIVA_VALUE?has_content>
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_PLL1POSTDIVA = ${OSCCTRL_PLL1POSTDIVA_VALUE};</@compress>
    </#if>

    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_PLL1CTRL |= OSCCTRL_PLL1CTRL_BWSEL(${CONFIG_CLOCK_PLL1_BWSEL}U) | OSCCTRL_PLL1CTRL_REFSEL(${CONFIG_CLOCK_PLL1_REF_CLOCK}U)
                                                                 ${(CONFIG_CLOCK_PLL1_ONDEMAND == "1")?then('| OSCCTRL_PLL1CTRL_ONDEMAND_Msk',' ')}
                                                                 | OSCCTRL_PLL1CTRL_ENABLE_Msk;</@compress>
    <#if CONFIG_CLOCK_PLL1_ONDEMAND != "1">

    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_PLL1LOCK_Msk) != OSCCTRL_STATUS_PLL1LOCK_Msk)
    {
        /* Waiting for the Ready state */
    }
    </#if>
}
</#if>
<#assign GEN_CODE_DFLL = CONFIG_CLOCK_DFLL_ENABLE && (CONFIG_CLOCK_DFLL_OPMODE == "1" || CONFIG_CLOCK_DFLL_ONDEMAND == "0")>
<#if GEN_CODE_DFLL>
static void DFLL_Initialize(void)
{
<#if CONFIG_CLOCK_DFLL_ENABLE == true >
<#if CONFIG_CLOCK_DFLL_OPMODE == "1">
    /****************** DFLL Initialization  *********************************/
    <#if CONFIG_CLOCK_DFLL_USB == false>
    GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_0_INDEX}] = GCLK_PCHCTRL_GEN(${GCLK_ID_0_GENSEL})${GCLK_ID_0_WRITELOCK?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;
    while ((GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_0_INDEX}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
    </#if>

    OSCCTRL_REGS->OSCCTRL_DFLLMUL = OSCCTRL_DFLLMUL_MUL(${CONFIG_CLOCK_DFLL_MUL}U) | OSCCTRL_DFLLMUL_STEP(${CONFIG_CLOCK_DFLL_STEP}U);
    while((OSCCTRL_REGS->OSCCTRL_SYNCBUSY & OSCCTRL_SYNCBUSY_DFLLMUL_Msk) == OSCCTRL_SYNCBUSY_DFLLMUL_Msk )
    {
        /* Waiting for the DFLLMUL synchronization */
    }

    /* Configure DFLL    */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DFLLCTRLB = OSCCTRL_DFLLCTRLB_LOOPEN(${CONFIG_CLOCK_DFLL_OPMODE}U)
    <#lt>                                    ${CONFIG_CLOCK_DFLL_USB?then('| OSCCTRL_DFLLCTRLB_USBCRM_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_WAIT_LOCK?then('| OSCCTRL_DFLLCTRLB_WAITLOCK_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_QUICK_LOCK?then('| OSCCTRL_DFLLCTRLB_QLDIS_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_CHILL_CYCLE?then('| OSCCTRL_DFLLCTRLB_CCDIS_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_LLAW?then('| OSCCTRL_DFLLCTRLB_LLAW_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_STABLE?then('| OSCCTRL_DFLLCTRLB_STABLE_Msk ', ' ')}
    <#lt>                                    ;</@compress>

    while((OSCCTRL_REGS->OSCCTRL_SYNCBUSY & OSCCTRL_SYNCBUSY_DFLLCTRLB_Msk) == OSCCTRL_SYNCBUSY_DFLLCTRLB_Msk )
    {
        /* Waiting for the DFLLCTRLB synchronization */
    }

    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DFLLCTRLA = OSCCTRL_DFLLCTRLA_ENABLE_Msk;</@compress>

    while((OSCCTRL_REGS->OSCCTRL_SYNCBUSY & OSCCTRL_SYNCBUSY_DFLLENABLE_Msk) == OSCCTRL_SYNCBUSY_DFLLENABLE_Msk )
    {
        /* Waiting for the DFLL48M enable synchronization */
    }
    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_DFLLRDY_Msk) != OSCCTRL_STATUS_DFLLRDY_Msk)
    {
        /* Waiting for the DFLL Ready state */
    }
    <#if CONFIG_CLOCK_DFLL_ONDEMAND == "1">
    OSCCTRL_REGS->OSCCTRL_DFLLCTRLA |= OSCCTRL_DFLLCTRLA_ONDEMAND_Msk;
    </#if>
<#else>
    <#if (CONFIG_CLOCK_DFLL_ONDEMAND == "0")>
    <#lt>    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DFLLCTRLA = OSCCTRL_DFLLCTRLA_ENABLE_Msk
        <#lt>                               ${(CONFIG_CLOCK_DFLL_ONDEMAND == "1")?then("| OSCCTRL_DFLLCTRLA_ONDEMAND_Msk ", "")}
        <#lt>                               ;</@compress>
    </#if>
</#if>
</#if>
}
</#if>

<#list 0..15 as i>
    <#assign GCLK_INST_NUM = "GCLK_INST_NUM" + i>
        <#if .vars[GCLK_INST_NUM]?has_content>
            <#if (.vars[GCLK_INST_NUM] != false)>
                <#assign GCLK_IMPROVE_DUTYCYCLE = "GCLK_" + i + "_IMPROVE_DUTYCYCLE">
                <#assign GCLK_RUNSTDBY = "GCLK_" + i + "_RUNSTDBY">
                <#assign GCLK_SRC = "GCLK_" + i + "_SRC">
                <#assign GCLK_OUTPUTENABLE = "GCLK_" + i + "_OUTPUTENABLE">
                <#assign GCLK_OUTPUTOFFVALUE = "GCLK_" + i + "_OUTPUTOFFVALUE">
                <#assign GCLK_DIVISONVALUE = "GCLK_" + i + "_DIV">
                <#assign GCLK_DIVISONSELECTION = "GCLK_" + i + "_DIVSEL">
static void GCLK${i}_Initialize(void)
{
    <#if (i==0)>

<#if CONF_MCLK_CLKDIV0 != "0x01">
    /* Selection of the Clock Domain Division Factor */
    MCLK_REGS->MCLK_CLKDIV[0] = MCLK_CLKDIV_DIV(${CONF_MCLK_CLKDIV0}U);

    while((MCLK_REGS->MCLK_INTFLAG & MCLK_INTFLAG_CKRDY_Msk) != MCLK_INTFLAG_CKRDY_Msk)
    {
        /* Wait for the Main Clock to be Ready */
    }
</#if>
<#if CONF_MCLK_CLKDIV1 != "0x01">
    /* Selection of the Clock Domain Division Factor */
    MCLK_REGS->MCLK_CLKDIV[1] = MCLK_CLKDIV_DIV(${CONF_MCLK_CLKDIV1}U);

    while((MCLK_REGS->MCLK_INTFLAG & MCLK_INTFLAG_CKRDY_Msk) != MCLK_INTFLAG_CKRDY_Msk)
    {
        /* Wait for the Main Clock to be Ready */
    }
</#if>
    </#if>
    <@compress single_line=true>GCLK_REGS->GCLK_GENCTRL[${i}] = GCLK_GENCTRL_DIV(${.vars[GCLK_DIVISONVALUE]}U)
                                                               | GCLK_GENCTRL_SRC(${.vars[GCLK_SRC]}U)
                                                               ${(.vars[GCLK_DIVISONSELECTION] == "DIV2")?then('| GCLK_GENCTRL_DIVSEL_Msk' , ' ')}
                                                               ${(.vars[GCLK_IMPROVE_DUTYCYCLE])?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                               ${(.vars[GCLK_RUNSTDBY])?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                               <#if .vars[GCLK_OUTPUTENABLE]??>
                                                               ${(.vars[GCLK_OUTPUTENABLE])?then('| GCLK_GENCTRL_OE_Msk', ' ')}
                                                               ${((.vars[GCLK_OUTPUTOFFVALUE] == "HIGH"))?then('| GCLK_GENCTRL_OOV_Msk', ' ')}
                                                               </#if>
                                                               | GCLK_GENCTRL_GENEN_Msk;</@compress>

    while((GCLK_REGS->GCLK_SYNCBUSY & GCLK_SYNCBUSY_GENCTRL${i}_Msk) == GCLK_SYNCBUSY_GENCTRL${i}_Msk)
    {
        /* Wait for the Generator ${i} synchronization */
    }
}

            </#if>
        </#if>
</#list>

void CLOCK_Initialize (void)
{
<#if CONFIG_CLOCK_XOSC_ENABLE == true>
    /* Function to Initialize the Oscillators */
    OSCCTRL_Initialize();
</#if>

    /* Function to Initialize the 32KHz Oscillators */
    OSC32KCTRL_Initialize();

<#list CLK_INIT_LIST?split("\n") as list_entry>
<#if !list_entry?contains("DFLL") || GEN_CODE_DFLL>
${list_entry}
</#if>
</#list>


<#list 3..GCLK_MAX_ID as i>
    <#assign GCLK_ID_CHEN = "GCLK_ID_" + i + "_CHEN">
    <#assign GCLK_ID_INDEX = "GCLK_ID_" + i + "_INDEX">
    <#assign GCLK_ID_NAME = "GCLK_ID_" + i + "_NAME">
    <#assign GCLK_ID_GENSEL = "GCLK_ID_" + i + "_GENSEL">
    <#assign GCLK_ID_WRITELOCK = "GCLK_ID_" + i + "_WRITELOCK">
        <#if .vars[GCLK_ID_CHEN]?has_content>
            <#if (.vars[GCLK_ID_CHEN] != false)>
    /* Selection of the Generator and write Lock for ${.vars[GCLK_ID_NAME]} */
    GCLK_REGS->GCLK_PCHCTRL[${.vars[GCLK_ID_INDEX]}] = GCLK_PCHCTRL_GEN(${.vars[GCLK_ID_GENSEL]})${.vars[GCLK_ID_WRITELOCK]?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;

    while ((GCLK_REGS->GCLK_PCHCTRL[${.vars[GCLK_ID_INDEX]}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
    </#if>
    </#if>
</#list>
<#if CONFIG_CLOCK_DFLL_ENABLE == false>

    /* Disable DFLL */
    OSCCTRL_REGS->OSCCTRL_DFLLCTRLA &= ~(OSCCTRL_DFLLCTRLA_ENABLE_Msk);
    while((OSCCTRL_REGS->OSCCTRL_SYNCBUSY & OSCCTRL_SYNCBUSY_DFLLENABLE_Msk) == OSCCTRL_SYNCBUSY_DFLLENABLE_Msk)
    {
        /* Waiting for the DFLL48M enable synchronization */
    }
</#if>
}
