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

#include "plib_clock.h"
#include "device.h"

static void OSCCTRL_Initialize(void)
{<#list 0..1 as x>
<#assign enable = "CONFIG_CLOCK_XOSC" + x + "_ENABLE" >
<#assign cfdPrescalar = "CONFIG_CLOCK_XOSC" + x + "_CFDPRESC" >
<#assign startup = "CONFIG_CLOCK_XOSC" + x + "_STARTUP" >
<#assign imult = "XOSC" + x + "_IMULT" >
<#assign iptat = "XOSC" + x + "_IPTAT" >
<#assign switchBack = "XOSC" + x + "_SWBEN" >
<#assign mode = "XOSC" + x + "_OSCILLATOR_MODE" >
<#assign cfdEnable = "CONFIG_CLOCK_XOSC" + x + "_CFDEN" >
<#assign enalc = "XOSC" + x + "_ENALC" >
<#assign lowBufgain = "XOSC" + x + "_LOWBUFGAIN" >
<#assign onDemand = "CONFIG_CLOCK_XOSC" + x + "_ONDEMAND" >
<#assign runStdby = "CONFIG_CLOCK_XOSC" + x + "_RUNSTDBY" >
<#if .vars[enable] == true>
    /****************** XOSC${x} Initialization   ********************************/

    /* Configure External Oscillator */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_XOSCCTRL[${x}] = OSCCTRL_XOSCCTRL_STARTUP(${.vars[startup]}) | OSCCTRL_XOSCCTRL_IMULT(${.vars[imult]}) | OSCCTRL_XOSCCTRL_IPTAT(${.vars[iptat]})
                                                             ${.vars[runStdby]?then('| OSCCTRL_XOSCCTRL_RUNSTDBY_Msk',' ')}${.vars[switchBack]?then('| OSCCTRL_XOSCCTRL_SWBEN_Msk',' ')}
                                                             ${(.vars[onDemand] == "ENABLE")?then('| OSCCTRL_XOSCCTRL_ONDEMAND_Msk',' ')}
                                                             ${.vars[cfdEnable]?then('| OSCCTRL_XOSCCTRL_CFDEN_Msk | OSCCTRL_XOSCCTRL_CFDPRESC(${.vars[cfdPrescalar]})',' ')}
                                                             ${.vars[enalc]?then('| OSCCTRL_XOSCCTRL_ENALC_Msk',' ')} ${.vars[lowBufgain]?then('| OSCCTRL_XOSCCTRL_LOWBUFGAIN_Msk',' ')}
                                                             ${(.vars[mode] == "1")?then('| OSCCTRL_XOSCCTRL_XTALEN_Msk',' ')} | OSCCTRL_XOSCCTRL_ENABLE_Msk;</@compress>

    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCRDY${x}_Msk) != OSCCTRL_STATUS_XOSCRDY${x}_Msk)
    {
        /* Waiting for the XOSC Ready state */
    }
</#if>
</#list>
}

static void OSC32KCTRL_Initialize(void)
{
<#if CONF_CLOCK_XOSC32K_ENABLE == true>
    /****************** XOSC32K initialization  ******************************/

    /* Configure 32K External Oscillator */
    <@compress single_line=true>OSC32KCTRL_REGS->OSC32KCTRL_XOSC32K = OSC32KCTRL_XOSC32K_STARTUP(${XOSC32K_STARTUP}) | OSC32KCTRL_XOSC32K_ENABLE_Msk | OSC32KCTRL_XOSC32K_CGM(${XOSC32K_CGM})
                                                               ${XOSC32K_RUNSTDBY?then('| OSC32KCTRL_XOSC32K_RUNSTDBY_Msk',' ')}
                                                               ${XOSC32K_EN1K?then('| OSC32KCTRL_XOSC32K_EN1K_Msk',' ')}
                                                               ${XOSC32K_EN32K?then('| OSC32KCTRL_XOSC32K_EN32K_Msk',' ')}
                                                               ${(XOSC32K_ONDEMAND == "ENABLE")?then('| OSC32KCTRL_XOSC32K_ONDEMAND_Msk',' ')}
                                                               ${(XOSC32K_OSCILLATOR_MODE == "1")?then('| OSC32KCTRL_XOSC32K_XTALEN_Msk',' ')};</@compress>

    <#if XOSC32K_CFDEN == true >
    /* Enable clock failure detection */
    OSC32KCTRL_REGS->OSC32KCTRL_CFDCTRL = OSC32KCTRL_CFDCTRL_CFDEN_Msk  ${XOSC32K_CFDPRESC?then('| OSC32KCTRL_CFDCTRL_CFDPRESC_Msk','')} ${XOSC32K_SWBACK?then('| OSC32KCTRL_CFDCTRL_SWBACK_Msk','')};
    </#if>

    while(!((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_XOSC32KRDY_Msk) == OSC32KCTRL_STATUS_XOSC32KRDY_Msk))
    {
        /* Waiting for the XOSC32K Ready state */
    }
</#if>

    OSC32KCTRL_REGS->OSC32KCTRL_RTCCTRL = OSC32KCTRL_RTCCTRL_RTCSEL(${CONFIG_CLOCK_RTC_SRC});
}

<#if CONFIG_CLOCK_DPLL0_ENABLE == true >
static void FDPLL0_Initialize(void)
{
    <#if CONFIG_CLOCK_DPLL0_REF_CLOCK == "0">
    GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_1_INDEX}] = GCLK_PCHCTRL_GEN(${GCLK_ID_1_GENSEL})${GCLK_ID_1_WRITELOCK?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;
    while ((GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_1_INDEX}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
    </#if>

    /****************** DPLL0 Initialization  *********************************/

    /* Configure DPLL    */
    <@compress single_line=true>OSCCTRL_REGS->DPLL[0].OSCCTRL_DPLLCTRLB = OSCCTRL_DPLLCTRLB_FILTER(${CONFIG_CLOCK_DPLL0_FILTER}) |
                                                                   OSCCTRL_DPLLCTRLB_LTIME(${CONFIG_CLOCK_DPLL0_LOCK_TIME})|
                                                                   OSCCTRL_DPLLCTRLB_REFCLK(${CONFIG_CLOCK_DPLL0_REF_CLOCK})
                                                                   ${CONFIG_CLOCK_DPLL0_LOCK_BYPASS?then('| OSCCTRL_DPLLCTRLB_LBYPASS_Msk', ' ')}
                                                                   ${CONFIG_CLOCK_DPLL0_WAKEUP_FAST?then('| OSCCTRL_DPLLCTRLB_WUF_Msk', ' ')}
                                                                   ${CONFIG_CLOCK_DPLL0_DCOEN?then('| OSCCTRL_DPLLCTRLB_DCOEN_Msk | OSCCTRL_DPLLCTRLB_DCOFILTER(${CONFIG_CLOCK_DPLL0_DCOFILTER})', ' ')}
                                                                   ${((CONFIG_CLOCK_DPLL0_REF_CLOCK == "2") || (CONFIG_CLOCK_DPLL0_REF_CLOCK == "3"))?then('| OSCCTRL_DPLLCTRLB_DIV(${CONFIG_CLOCK_DPLL0_DIVIDER})', ' ')};</@compress>


    <@compress single_line=true>OSCCTRL_REGS->DPLL[0].OSCCTRL_DPLLRATIO = OSCCTRL_DPLLRATIO_LDRFRAC(${CONFIG_CLOCK_DPLL0_LDRFRAC_FRACTION}) |
                                                              OSCCTRL_DPLLRATIO_LDR(${CONFIG_CLOCK_DPLL0_LDR_INTEGER});</@compress>

    while((OSCCTRL_REGS->DPLL[0].OSCCTRL_DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_DPLLRATIO_Msk) == OSCCTRL_DPLLSYNCBUSY_DPLLRATIO_Msk)
    {
        /* Waiting for the synchronization */
    }

    /* Enable DPLL */
    OSCCTRL_REGS->DPLL[0].OSCCTRL_DPLLCTRLA = OSCCTRL_DPLLCTRLA_ENABLE_Msk ${(CONFIG_CLOCK_DPLL0_ONDEMAND == "1")?then('| OSCCTRL_DPLLCTRLA_ONDEMAND_Msk',' ')} ${CONFIG_CLOCK_DPLL0_RUNSTDY?then('| OSCCTRL_DPLLCTRLA_RUNSTDBY_Msk','')};

    while((OSCCTRL_REGS->DPLL[0].OSCCTRL_DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_ENABLE_Msk) == OSCCTRL_DPLLSYNCBUSY_ENABLE_Msk )
    {
        /* Waiting for the DPLL enable synchronization */
    }

    while((OSCCTRL_REGS->DPLL[0].OSCCTRL_DPLLSTATUS & (OSCCTRL_DPLLSTATUS_LOCK_Msk | OSCCTRL_DPLLSTATUS_CLKRDY_Msk)) !=
                (OSCCTRL_DPLLSTATUS_LOCK_Msk | OSCCTRL_DPLLSTATUS_CLKRDY_Msk))
    {
        /* Waiting for the Ready state */
    }
}
</#if>

<#if CONFIG_CLOCK_DPLL1_ENABLE == true >
static void FDPLL1_Initialize(void)
{
    <#if CONFIG_CLOCK_DPLL1_REF_CLOCK == "0">
    GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_2_INDEX}] = GCLK_PCHCTRL_GEN(${GCLK_ID_2_GENSEL})${GCLK_ID_2_WRITELOCK?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;
    while ((GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_1_INDEX}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
    </#if>

    /****************** DPLL1 Initialization  *********************************/

    /* Configure DPLL    */
    <@compress single_line=true>OSCCTRL_REGS->DPLL[1].OSCCTRL_DPLLCTRLB = OSCCTRL_DPLLCTRLB_FILTER(${CONFIG_CLOCK_DPLL1_FILTER}) |
                                                                   OSCCTRL_DPLLCTRLB_LTIME(${CONFIG_CLOCK_DPLL1_LOCK_TIME})|
                                                                   OSCCTRL_DPLLCTRLB_REFCLK(${CONFIG_CLOCK_DPLL1_REF_CLOCK})
                                                                   ${CONFIG_CLOCK_DPLL1_LOCK_BYPASS?then('| OSCCTRL_DPLLCTRLB_LBYPASS_Msk', ' ')}
                                                                   ${CONFIG_CLOCK_DPLL1_WAKEUP_FAST?then('| OSCCTRL_DPLLCTRLB_WUF_Msk', ' ')}
                                                                   ${CONFIG_CLOCK_DPLL1_DCOEN?then('| OSCCTRL_DPLLCTRLB_DCOEN_Msk | OSCCTRL_DPLLCTRLB_DCOFILTER(${CONFIG_CLOCK_DPLL1_DCOFILTER})', ' ')}
                                                                   ${((CONFIG_CLOCK_DPLL1_REF_CLOCK == "2") || (CONFIG_CLOCK_DPLL1_REF_CLOCK == "3"))?then('| OSCCTRL_DPLLCTRLB_DIV(${CONFIG_CLOCK_DPLL1_DIVIDER})', ' ')};</@compress>


    <@compress single_line=true>OSCCTRL_REGS->DPLL[1].OSCCTRL_DPLLRATIO = OSCCTRL_DPLLRATIO_LDRFRAC(${CONFIG_CLOCK_DPLL1_LDRFRAC_FRACTION}) |
                                                              OSCCTRL_DPLLRATIO_LDR(${CONFIG_CLOCK_DPLL1_LDR_INTEGER});</@compress>

    while((OSCCTRL_REGS->DPLL[1].OSCCTRL_DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_DPLLRATIO_Msk) == OSCCTRL_DPLLSYNCBUSY_DPLLRATIO_Msk)
    {
        /* Waiting for the synchronization */
    }

    /* Enable DPLL */
    OSCCTRL_REGS->DPLL[1].OSCCTRL_DPLLCTRLA = OSCCTRL_DPLLCTRLA_ENABLE_Msk ${(CONFIG_CLOCK_DPLL1_ONDEMAND == "1")?then('| OSCCTRL_DPLLCTRLA_ONDEMAND_Msk',' ')} ${CONFIG_CLOCK_DPLL1_RUNSTDY?then('| OSCCTRL_DPLLCTRLA_RUNSTDBY_Msk','')};

    while((OSCCTRL_REGS->DPLL[1].OSCCTRL_DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_ENABLE_Msk) == OSCCTRL_DPLLSYNCBUSY_ENABLE_Msk )
    {
        /* Waiting for the DPLL enable synchronization */
    }

    while((OSCCTRL_REGS->DPLL[1].OSCCTRL_DPLLSTATUS & (OSCCTRL_DPLLSTATUS_LOCK_Msk | OSCCTRL_DPLLSTATUS_CLKRDY_Msk)) !=
                (OSCCTRL_DPLLSTATUS_LOCK_Msk | OSCCTRL_DPLLSTATUS_CLKRDY_Msk))
    {
        /* Waiting for the Ready state */
    }
}
</#if>

static void DFLL_Initialize(void)
{
<#if CONFIG_CLOCK_DFLL_ENABLE == true >
<#if CONFIG_CLOCK_DFLL_OPMODE == "1">
    /****************** DFLL Initialization  *********************************/
    GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_0_INDEX}] = GCLK_PCHCTRL_GEN(${GCLK_ID_0_GENSEL})${GCLK_ID_0_WRITELOCK?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;
    while ((GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_0_INDEX}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }

    OSCCTRL_REGS->OSCCTRL_DFLLMUL = OSCCTRL_DFLLMUL_MUL(${CONFIG_CLOCK_DFLL_MUL}) | OSCCTRL_DFLLMUL_FSTEP(${CONFIG_CLOCK_DFLL_FINE}) | OSCCTRL_DFLLMUL_CSTEP(${CONFIG_CLOCK_DFLL_COARSE});
    while((OSCCTRL_REGS->OSCCTRL_DFLLSYNC & OSCCTRL_DFLLSYNC_DFLLMUL_Msk) == OSCCTRL_DFLLSYNC_DFLLMUL_Msk )
    {
        /* Waiting for the DPLL enable synchronization */
    }

    /* Configure DFLL    */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DFLLCTRLB = OSCCTRL_DFLLCTRLB_MODE_Msk
    <#lt>                                    ${CONFIG_CLOCK_DFLL_USB?then('| OSCCTRL_DFLLCTRLB_USBCRM_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_WAIT_LOCK?then('| OSCCTRL_DFLLCTRLB_WAITLOCK_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_BYPASS_COARSE?then('| OSCCTRL_DFLLCTRLB_BPLCKC_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_QUICK_LOCK?then('| OSCCTRL_DFLLCTRLB_QLDIS_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_CHILL_CYCLE?then('| OSCCTRL_DFLLCTRLB_CCDIS_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_LLAW?then('| OSCCTRL_DFLLCTRLB_LLAW_Msk ', ' ')}
    <#lt>                                    ${CONFIG_CLOCK_DFLL_STABLE?then('| OSCCTRL_DFLLCTRLB_STABLE_Msk ', ' ')}
    <#lt>                                    ;</@compress>

    while((OSCCTRL_REGS->OSCCTRL_DFLLSYNC & OSCCTRL_DFLLSYNC_DFLLCTRLB_Msk) == OSCCTRL_DFLLSYNC_DFLLCTRLB_Msk )
    {
        /* Waiting for the DPLL enable synchronization */
    }

    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DFLLCTRLA = OSCCTRL_DFLLCTRLA_ENABLE_Msk
    <#lt>                               ${(CONFIG_CLOCK_DFLL_ONDEMAND == "ENABLE")?then("| OSCCTRL_DFLLCTRLA_ONDEMAND_Msk ", "")}
    <#lt>                               ${CONFIG_CLOCK_DFLL_RUNSTDY?then('| OSCCTRL_DFLLCTRLA_RUNSTDBY_Msk ', ' ')}
    <#lt>                               ;</@compress>

    while((OSCCTRL_REGS->OSCCTRL_DFLLSYNC & OSCCTRL_DFLLSYNC_ENABLE_Msk) == OSCCTRL_DFLLSYNC_ENABLE_Msk )
    {
        /* Waiting for the DPLL enable synchronization */
    }

    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_DFLLRDY_Msk) != OSCCTRL_STATUS_DFLLRDY_Msk)
    {
        /* Waiting for the XOSC Ready state */
    }
<#else>
    <#if (CONFIG_CLOCK_DFLL_ONDEMAND == "0") || CONFIG_CLOCK_DFLL_RUNSTDY>
    <#lt>    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DFLLCTRLA = OSCCTRL_DFLLCTRLA_ENABLE_Msk
        <#lt>                               ${(CONFIG_CLOCK_DFLL_ONDEMAND == "1")?then("| OSCCTRL_DFLLCTRLA_ONDEMAND_Msk ", "")}
        <#lt>                               ${CONFIG_CLOCK_DFLL_RUNSTDY?then('| OSCCTRL_DFLLCTRLA_RUNSTDBY_Msk ', ' ')}
        <#lt>                               ;</@compress>
    </#if>
</#if>
</#if>
}


<#list 0..11 as i>
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
    <@compress single_line=true>GCLK_REGS->GCLK_GENCTRL[${i}] = GCLK_GENCTRL_DIV(${.vars[GCLK_DIVISONVALUE]})
                                                               | GCLK_GENCTRL_SRC(${.vars[GCLK_SRC]})
                                                               ${(.vars[GCLK_DIVISONSELECTION] == "DIV2")?then('| GCLK_GENCTRL_DIVSEL_Msk' , ' ')}
                                                               ${(.vars[GCLK_IMPROVE_DUTYCYCLE])?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                               ${(.vars[GCLK_RUNSTDBY])?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                               <#if .vars[GCLK_OUTPUTENABLE]??>
                                                               ${(.vars[GCLK_OUTPUTENABLE])?then('| GCLK_GENCTRL_OE_Msk', ' ')}
                                                               ${((.vars[GCLK_OUTPUTOFFVALUE] == "HIGH"))?then('| GCLK_GENCTRL_OOV_Msk', ' ')}
                                                               </#if>
                                                               | GCLK_GENCTRL_GENEN_Msk;</@compress>

    while((GCLK_REGS->GCLK_SYNCBUSY & GCLK_SYNCBUSY_GENCTRL_GCLK${i}) == GCLK_SYNCBUSY_GENCTRL_GCLK${i})
    {
        /* wait for the Generator ${i} synchronization */
    }
}

            </#if>
        </#if>
</#list>
void CLOCK_Initialize (void)
{
    /* Function to Initialize the Oscillators */
    OSCCTRL_Initialize();

    /* Function to Initialize the 32KHz Oscillators */
    OSC32KCTRL_Initialize();

${CLK_INIT_LIST}
<#if CONF_CPU_CLOCK_DIVIDER != "1">
    /* selection of the CPU clock Division */
    MCLK_REGS->MCLK_CPUDIV = MCLK_CPUDIV_DIV(${CONF_CPU_CLOCK_DIVIDER});

    while((MCLK_REGS->MCLK_INTFLAG & MCLK_INTFLAG_CKRDY_Msk) != MCLK_INTFLAG_CKRDY_Msk)
    {
        /* Wait for the Main Clock to be Ready */
    }
</#if>

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

    <#if MCLK_AHB_INITIAL_VALUE != "0xFFFFFF">
    /* Configure the AHB Bridge Clocks */
    MCLK_REGS->MCLK_AHBMASK = ${MCLK_AHB_INITIAL_VALUE};

    </#if>
    <#if MCLK_APBA_INITIAL_VALUE != "0x7FF">
    /* Configure the APBA Bridge Clocks */
    MCLK_REGS->MCLK_APBAMASK = ${MCLK_APBA_INITIAL_VALUE};

    </#if>
    <#if MCLK_APBB_INITIAL_VALUE != "0x18056">
    /* Configure the APBB Bridge Clocks */
    MCLK_REGS->MCLK_APBBMASK = ${MCLK_APBB_INITIAL_VALUE};

    </#if>
    <#if MCLK_APBC_INITIAL_VALUE??>
    <#if MCLK_APBC_INITIAL_VALUE != "0x2000">
    /* Configure the APBC Bridge Clocks */
    MCLK_REGS->MCLK_APBCMASK = ${MCLK_APBC_INITIAL_VALUE};

    </#if>
    </#if>
    <#if MCLK_APBD_INITIAL_VALUE??>
    <#if MCLK_APBD_INITIAL_VALUE != "0x0">
    /* Configure the APBD Bridge Clocks */
    MCLK_REGS->MCLK_APBDMASK = ${MCLK_APBD_INITIAL_VALUE};

    </#if>
    </#if>

    <#if CONFIG_CLOCK_DFLL_ENABLE == false>

    /* Disable DFLL */
    OSCCTRL_REGS->OSCCTRL_DFLLCTRLA &= ~(OSCCTRL_DFLLCTRLA_ENABLE_Msk);
    while((OSCCTRL_REGS->OSCCTRL_DFLLSYNC & OSCCTRL_DFLLSYNC_ENABLE_Msk) == OSCCTRL_DFLLSYNC_ENABLE_Msk )
    {
        /* Waiting for the DPLL enable synchronization */
    }
    </#if>
}
