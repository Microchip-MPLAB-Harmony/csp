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

#include <stddef.h>
#include "plib_clock.h"
#include "device.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#if CONFIG_CLOCK_XOSC_CFDEN == true>

typedef struct
{
    OSCCTRL_CFD_CALLBACK   callback;
    uintptr_t        context;
} OSCCTRL_OBJECT;

/* Reference Object created for the OSCCTRL */
static volatile OSCCTRL_OBJECT oscctrlObj;

</#if>

<#if XOSC32K_CFDEN == true >

typedef struct
{
    OSC32KCTRL_CFD_CALLBACK   callback;
    uintptr_t        context;
} OSC32KCTRL_OBJECT;

/* Reference Object created for the OSCCTRL */
static volatile OSC32KCTRL_OBJECT osc32kctrlObj;

</#if>

<#if MCLK_INTENSET_CKRDY == true >

typedef struct
{
    MCLK_CKRDY_CALLBACK   callback;
    uintptr_t             context;
} MCLK_OBJECT;

/* Reference Object created for the MCLK */
static volatile MCLK_OBJECT mclkObj;

</#if>

<#if (CONFIG_CLOCK_XOSC_ENABLE == true) || (CONFIG_CLOCK_OSC16M_ENABLE == true &&
((CONFIG_CLOCK_OSC16M_FREQSEL != "0x0") || (CONFIG_CLOCK_OSC16M_RUNSTDBY != false) || (CONFIG_CLOCK_OSC16M_ONDEMAND != "ENABLE")))>
static void OSCCTRL_Initialize(void)
{
<#if CONFIG_CLOCK_OSC16M_ENABLE == true>
<#if (CONFIG_CLOCK_OSC16M_FREQSEL != "0x0") || (CONFIG_CLOCK_OSC16M_RUNSTDBY != false) || (CONFIG_CLOCK_OSC16M_ONDEMAND != "ENABLE")>
    /**************** OSC16M IniTialization *************/
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_OSC16MCTRL = OSCCTRL_OSC16MCTRL_FSEL(${CONFIG_CLOCK_OSC16M_FREQSEL}U)
                                                         ${CONFIG_CLOCK_OSC16M_RUNSTDBY?then('| OSCCTRL_OSC16MCTRL_RUNSTDBY_Msk',' ')}
                                                         ${(CONFIG_CLOCK_OSC16M_ONDEMAND == "ENABLE")?then('| OSCCTRL_OSC16MCTRL_ONDEMAND_Msk',' ')}
                                                         | OSCCTRL_OSC16MCTRL_ENABLE_Msk;</@compress>
</#if>
</#if>
<#if CONFIG_CLOCK_XOSC_ENABLE == true>
/****************** XOSC Initialization   ********************************/

<#if CONFIG_CLOCK_XOSC_CFDEN == true >
/* Selection of the Clock failure detection (CFD) pre scalar */
    OSCCTRL_REGS->OSCCTRL_CFDPRESC = ${CONFIG_CLOCK_XOSC_CFDPRESC}U;
</#if>

/* Configure External Oscillator */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_XOSCCTRL = OSCCTRL_XOSCCTRL_STARTUP(${CONFIG_CLOCK_XOSC_STARTUP}U) | OSCCTRL_XOSCCTRL_GAIN(${CONFIG_CLOCK_XOSC_GAIN}U)
                                                         ${CONFIG_CLOCK_XOSC_RUNSTDBY?then('| OSCCTRL_XOSCCTRL_RUNSTDBY_Msk',' ')}
                                                         ${(CONFIG_CLOCK_XOSC_ONDEMAND == "ENABLE")?then('| OSCCTRL_XOSCCTRL_ONDEMAND_Msk',' ')}
                                                         ${CONFIG_CLOCK_XOSC_CFDEN?then('| OSCCTRL_XOSCCTRL_CFDEN_Msk',' ')}
                                                         ${(XOSC_OSCILLATOR_MODE == "1")?then('| OSCCTRL_XOSCCTRL_XTALEN_Msk',' ')} | OSCCTRL_XOSCCTRL_ENABLE_Msk;</@compress>
    <#if CONFIG_CLOCK_XOSC_ONDEMAND != "ENABLE">
    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCRDY_Msk) != OSCCTRL_STATUS_XOSCRDY_Msk)
    {
        /* Waiting for the XOSC Ready state */
    }
    </#if>

<#if XOSC_AMPGC == true >
/* Setting the Automatic Gain Control */
OSCCTRL_REGS->OSCCTRL_XOSCCTRL |= OSCCTRL_XOSCCTRL_AMPGC_Msk;
</#if>
</#if>
}
</#if>

static void OSC32KCTRL_Initialize(void)
{
<#if CONF_CLOCK_XOSC32K_ENABLE == true>
    /****************** XOSC32K initialization  ******************************/

    /* Configure 32K External Oscillator */
    <@compress single_line=true>OSC32KCTRL_REGS->OSC32KCTRL_XOSC32K = OSC32KCTRL_XOSC32K_STARTUP(${XOSC32K_STARTUP}U) | OSC32KCTRL_XOSC32K_ENABLE_Msk
                                                               ${XOSC32K_RUNSTDBY?then('| OSC32KCTRL_XOSC32K_RUNSTDBY_Msk',' ')}
                                                               ${XOSC32K_EN1K?then('| OSC32KCTRL_XOSC32K_EN1K_Msk',' ')}
                                                               ${XOSC32K_EN32K?then('| OSC32KCTRL_XOSC32K_EN32K_Msk',' ')}
                                                               ${(XOSC32K_ONDEMAND == "ENABLE")?then('| OSC32KCTRL_XOSC32K_ONDEMAND_Msk',' ')}
                                                               ${(XOSC32K_OSCILLATOR_MODE == "1")?then('| OSC32KCTRL_XOSC32K_XTALEN_Msk',' ')};</@compress>

    <#if XOSC32K_CFDEN == true >
    /* Enable clock failure detection */
    OSC32KCTRL_REGS->OSC32KCTRL_CFDCTRL |= OSC32KCTRL_CFDCTRL_CFDEN_Msk  ${XOSC32K_CFDPRESC?then('| OSC32KCTRL_CFDCTRL_CFDPRESC_Msk','')};
    </#if>
    <#if XOSC32K_ONDEMAND != "ENABLE">

    while(!((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_XOSC32KRDY_Msk) == OSC32KCTRL_STATUS_XOSC32KRDY_Msk))
    {
        /* Waiting for the XOSC32K Ready state */
    }
    </#if>
</#if>
    OSC32KCTRL_REGS->OSC32KCTRL_RTCCTRL = OSC32KCTRL_RTCCTRL_RTCSEL(${CONFIG_CLOCK_RTC_SRC}U);
}

<#if CONFIG_CLOCK_DFLL_ENABLE == true >
static void DFLL_Initialize(void)
{
    /****************** DFLL Initialization  *********************************/
    GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_2_INDEX}] = GCLK_PCHCTRL_GEN(${GCLK_ID_2_GENSEL}U)${GCLK_ID_2_WRITELOCK?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;

    while ((GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_2_INDEX}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
    OSCCTRL_REGS->OSCCTRL_DFLLULPRATIO = OSCCTRL_DFLLULPRATIO_RATIO(${CONFIG_CLOCK_DFLL_RATIO}U);

    <#if CONFIG_CLOCK_DFLL_DITHER>
    OSCCTRL_REGS->OSCCTRL_DFLLULPDITHER = OSCCTRL_DFLLULPDITHER_PER(${CONFIG_CLOCK_DFLL_DITHER_PERIOD}U) | OSCCTRL_DFLLULPDITHER_STEP(${CONFIG_CLOCK_DFLL_DITHER_STEP}U);
    </#if>

    /* Configure DFLL    */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DFLLULPCTRL = OSCCTRL_DFLLULPCTRL_ENABLE_Msk
    <#lt>                               ${CONFIG_CLOCK_DFLL_RUNSTDY?then('| OSCCTRL_DFLLULPCTRL_RUNSTDBY_Msk ', ' ')}
    <#lt>                               ${CONFIG_CLOCK_DFLL_DITHER?then('| OSCCTRL_DFLLULPCTRL_DITHER_Msk ', ' ')}
    <#lt>                               ${CONFIG_CLOCK_DFLL_SAFE?then('| OSCCTRL_DFLLULPCTRL_SAFE_Msk ', ' ')}
    <#lt>                               ${CONFIG_CLOCK_DFLL_BINSE?then('| OSCCTRL_DFLLULPCTRL_BINSE_Msk ', ' ')}
    <#lt>                               ${(CONFIG_CLOCK_DFLL_DIV != "0") ?then('| OSCCTRL_DFLLULPCTRL_DIV(${CONFIG_CLOCK_DFLL_DIV}U) ', ' ')}
    <#lt>                               ;</@compress>

    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_DFLLULPRDY_Msk) != OSCCTRL_STATUS_DFLLULPRDY_Msk)
    {
        /* Waiting for the Ready state */
    }

    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_DFLLULPLOCK_Msk) != OSCCTRL_STATUS_DFLLULPLOCK_Msk)
    {
        /* Waiting for DFLL to fully lock to meet clock accuracy */
    }

    <#if CONFIG_CLOCK_DFLL_ONDEMAND == "1">
    OSCCTRL_REGS->OSCCTRL_DFLLULPCTRL |= OSCCTRL_DFLLULPCTRL_ONDEMAND_Msk;
    </#if>
}
</#if>

<#if CONFIG_CLOCK_DPLL_ENABLE == true >
static void FDPLL_Initialize(void)
{
    <#if CONFIG_CLOCK_DPLL_REF_CLOCK == "2">
    GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_0_INDEX}] = GCLK_PCHCTRL_GEN(${GCLK_ID_0_GENSEL}U)${GCLK_ID_0_WRITELOCK?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;
    while ((GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_0_INDEX}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
    </#if>

    /****************** DPLL Initialization  *********************************/

    /* Configure DPLL    */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DPLLCTRLB = OSCCTRL_DPLLCTRLB_FILTER(${CONFIG_CLOCK_DPLL_FILTER}U) |
                                                                   OSCCTRL_DPLLCTRLB_LTIME(${CONFIG_CLOCK_DPLL_LOCK_TIME}U)|
                                                                   OSCCTRL_DPLLCTRLB_REFCLK(${CONFIG_CLOCK_DPLL_REF_CLOCK}U)
                                                                   ${CONFIG_CLOCK_DPLL_LOCK_BYPASS?then('| OSCCTRL_DPLLCTRLB_LBYPASS_Msk', ' ')}
                                                                   ${CONFIG_CLOCK_DPLL_WAKEUP_FAST?then('| OSCCTRL_DPLLCTRLB_WUF_Msk', ' ')}
                                                                   ${CONFIG_CLOCK_DPLL_LOWPOWER_ENABLE?then('| OSCCTRL_DPLLCTRLB_LPEN_Msk', ' ')}
                                                                   ${(CONFIG_CLOCK_DPLL_REF_CLOCK == "1")?then('| OSCCTRL_DPLLCTRLB_DIV(${CONFIG_CLOCK_DPLL_DIVIDER}U)', ' ')};</@compress>


    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DPLLRATIO = OSCCTRL_DPLLRATIO_LDRFRAC(${CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION}U) |
                                                              OSCCTRL_DPLLRATIO_LDR(${CONFIG_CLOCK_DPLL_LDR_INTEGER}U);</@compress>

    while((OSCCTRL_REGS->OSCCTRL_DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_DPLLRATIO_Msk) == OSCCTRL_DPLLSYNCBUSY_DPLLRATIO_Msk)
    {
        /* Waiting for the synchronization */
    }

    <#if CONFIG_CLOCK_DPLL_PRESCALAR != "0">
    /* Selection of the DPLL Pre-Scalar */
   OSCCTRL_REGS->OSCCTRL_DPLLPRESC = OSCCTRL_DPLLPRESC_PRESC(${CONFIG_CLOCK_DPLL_PRESCALAR}U);

    while((OSCCTRL_REGS->OSCCTRL_DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_DPLLPRESC_Msk) == OSCCTRL_DPLLSYNCBUSY_DPLLPRESC_Msk )
    {
        /* Waiting for the synchronization */
    }
    </#if>
    /* Selection of the DPLL Enable */
    OSCCTRL_REGS->OSCCTRL_DPLLCTRLA = OSCCTRL_DPLLCTRLA_ENABLE_Msk ${(CONFIG_CLOCK_DPLL_ONDEMAND == "1")?then('| OSCCTRL_DPLLCTRLA_ONDEMAND_Msk',' ')} ${CONFIG_CLOCK_DPLL_RUNSTDY?then('| OSCCTRL_DPLLCTRLA_RUNSTDBY_Msk','')};

    while((OSCCTRL_REGS->OSCCTRL_DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_ENABLE_Msk) == OSCCTRL_DPLLSYNCBUSY_ENABLE_Msk )
    {
        /* Waiting for the DPLL enable synchronization */
    }
    <#if CONFIG_CLOCK_DPLL_ONDEMAND != "1">

    while((OSCCTRL_REGS->OSCCTRL_DPLLSTATUS & (OSCCTRL_DPLLSTATUS_LOCK_Msk | OSCCTRL_DPLLSTATUS_CLKRDY_Msk)) !=
                (OSCCTRL_DPLLSTATUS_LOCK_Msk | OSCCTRL_DPLLSTATUS_CLKRDY_Msk))
    {
        /* Waiting for the Ready state */
    }
    </#if>
}
</#if>

<#list 0..5 as i>
    <#assign GCLK_INST_NUM = "GCLK_INST_NUM" + i>
        <#if .vars[GCLK_INST_NUM]?has_content>
            <#if (.vars[GCLK_INST_NUM] != false)>
                <#assign GCLK_IMPROVE_DUTYCYCLE = "GCLK_" + i + "_IMPROVE_DUTYCYCLE">
                <#assign GCLK_RUNSTDBY = "GCLK_" + i + "_RUNSTDBY">
                <#assign GCLK_SRC = "GCLK_" + i + "_SRC">
                <#assign NUM_PADS  = GCLK_NUM_PADS>
                <#assign GCLK_OUTPUTENABLE = "GCLK_" + i + "_OUTPUTENABLE">
                <#assign GCLK_OUTPUTOFFVALUE = "GCLK_" + i + "_OUTPUTOFFVALUE">
                <#assign GCLK_DIVISONVALUE = "GCLK_" + i + "_DIV">
                <#assign GCLK_DIVISONSELECTION = "GCLK_" + i + "_DIVSEL">

static void GCLK${i}_Initialize(void)
{
    <#if (i==0)>

<#if CONF_CPU_CLOCK_DIVIDER != '0x01'>
    /* selection of the CPU clock Division */
    MCLK_REGS->MCLK_CPUDIV = MCLK_CPUDIV_CPUDIV(${CONF_CPU_CLOCK_DIVIDER}U);

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
                                                               <#if i < GCLK_NUM_PADS >
                                                               ${(.vars[GCLK_OUTPUTENABLE])?then('| GCLK_GENCTRL_OE_Msk', ' ')}
                                                               ${((.vars[GCLK_OUTPUTOFFVALUE] == "HIGH"))?then('| GCLK_GENCTRL_OOV_Msk', ' ')}
                                                               </#if>
                                                               | GCLK_GENCTRL_GENEN_Msk;</@compress>

    while((GCLK_REGS->GCLK_SYNCBUSY & GCLK_SYNCBUSY_GENCTRL${i}_Msk) == GCLK_SYNCBUSY_GENCTRL${i}_Msk)
    {
        /* wait for the Generator ${i} synchronization */
    }
}

            </#if>
        </#if>
</#list>
void CLOCK_Initialize (void)
{
<#if (CONFIG_CLOCK_XOSC_ENABLE == true) || (CONFIG_CLOCK_OSC16M_ENABLE == true &&
((CONFIG_CLOCK_OSC16M_FREQSEL != "0x0") || (CONFIG_CLOCK_OSC16M_RUNSTDBY != false) || (CONFIG_CLOCK_OSC16M_ONDEMAND != "ENABLE")))>
    /* Function to Initialize the Oscillators */
    OSCCTRL_Initialize();
</#if>

    /* Function to Initialize the 32KHz Oscillators */
    OSC32KCTRL_Initialize();

${CLK_INIT_LIST}
<#if !GCLK_INST_NUM0>
<#if CONF_CPU_CLOCK_DIVIDER != '0x01'>
    /* selection of the CPU clock Division */
    MCLK_REGS->MCLK_CPUDIV = MCLK_CPUDIV_CPUDIV(${CONF_CPU_CLOCK_DIVIDER}U);

    while((MCLK_REGS->MCLK_INTFLAG & MCLK_INTFLAG_CKRDY_Msk) != MCLK_INTFLAG_CKRDY_Msk)
    {
        /* Wait for the Main Clock to be Ready */
    }
</#if>
</#if>
<#if MCLK_SRC != "0">
    MCLK_REGS->MCLK_CTRLA = MCLK_CTRLA_CKSEL_Msk;
</#if>


<#list 1..GCLK_MAX_ID as i>
    <#assign GCLK_ID_CHEN = "GCLK_ID_" + i + "_CHEN">
    <#assign GCLK_ID_INDEX = "GCLK_ID_" + i + "_INDEX">
    <#assign GCLK_ID_NAME = "GCLK_ID_" + i + "_NAME">
    <#assign GCLK_ID_GENSEL = "GCLK_ID_" + i + "_GENSEL">
    <#assign GCLK_ID_WRITELOCK = "GCLK_ID_" + i + "_WRITELOCK">
        <#if .vars[GCLK_ID_CHEN]?has_content>
            <#if (.vars[GCLK_ID_CHEN] != false)>
    /* Selection of the Generator and write Lock for ${.vars[GCLK_ID_NAME]} */
    GCLK_REGS->GCLK_PCHCTRL[${.vars[GCLK_ID_INDEX]}] = GCLK_PCHCTRL_GEN(${.vars[GCLK_ID_GENSEL]}U)${.vars[GCLK_ID_WRITELOCK]?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;

    while ((GCLK_REGS->GCLK_PCHCTRL[${.vars[GCLK_ID_INDEX]}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
    </#if>
    </#if>
</#list>

    <#if MCLK_AHB_INITIAL_VALUE != "0x1fff">
    /* Configure the AHB Bridge Clocks */
    MCLK_REGS->MCLK_AHBMASK = ${MCLK_AHB_INITIAL_VALUE}U;

    </#if>
    <#if MCLK_APBA_INITIAL_VALUE != "0x7fff">
    /* Configure the APBA Bridge Clocks */
    MCLK_REGS->MCLK_APBAMASK = ${MCLK_APBA_INITIAL_VALUE}U;

    </#if>
    <#if MCLK_APBB_INITIAL_VALUE != "0x17">
    /* Configure the APBB Bridge Clocks */
    MCLK_REGS->MCLK_APBBMASK = ${MCLK_APBB_INITIAL_VALUE}U;

    </#if>
    <#if MCLK_APBC_INITIAL_VALUE??>
    <#if MCLK_APBC_INITIAL_VALUE != "0x1fff">
    /* Configure the APBC Bridge Clocks */
    MCLK_REGS->MCLK_APBCMASK = ${MCLK_APBC_INITIAL_VALUE}U;

    </#if>
    </#if>

    <#if CONFIG_CLOCK_OSC16M_ENABLE == false>
    /*Disable internal RC oscillator*/
    OSCCTRL_REGS->OSCCTRL_OSC16MCTRL = 0U;
    </#if>
    <#if CONFIG_CLOCK_XOSC_CFDEN == true>
    /* Enabling the Clock Fail Interrupt  */
    OSCCTRL_REGS->OSCCTRL_INTENSET = OSCCTRL_INTENSET_XOSCFAIL_Msk;

    </#if>
    <#if XOSC32K_CFDEN == true >
    /* Enabling the Clock Failure Interrupt */
    OSC32KCTRL_REGS->OSC32KCTRL_INTENSET = OSC32KCTRL_INTENSET_CLKFAIL_Msk;

    </#if>
    <#if MCLK_INTENSET_CKRDY == true >
    /* Enabling the Clock Ready Interrupt */
    MCLK_REGS->MCLK_INTENSET = MCLK_INTENSET_CKRDY_Msk;
    </#if>
}

<#if CONFIG_CLOCK_XOSC_CFDEN == true>

void OSCCTRL_CallbackRegister(OSCCTRL_CFD_CALLBACK callback, uintptr_t context)
{
    oscctrlObj.callback = callback;
    oscctrlObj.context = context;
}

void __attribute__((used)) OSCCTRL_InterruptHandler(void)
{
    uintptr_t context_var;

    /* Checking for the Clock Fail status */
    if ((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCFAIL_Msk) == OSCCTRL_STATUS_XOSCFAIL_Msk)
    {
        /* Clearing the XOSC Fail Interrupt Flag */
        OSCCTRL_REGS->OSCCTRL_INTFLAG = OSCCTRL_INTFLAG_XOSCFAIL_Msk;

        if (oscctrlObj.callback != NULL)
        {
            context_var = oscctrlObj.context;
            oscctrlObj.callback(context_var);
        }
    }
}

</#if>

<#if XOSC32K_CFDEN == true >

void OSC32KCTRL_CallbackRegister (OSC32KCTRL_CFD_CALLBACK callback, uintptr_t context)
{
    osc32kctrlObj.callback = callback;
    osc32kctrlObj.context = context;
}

void __attribute__((used)) OSC32KCTRL_InterruptHandler(void)
{
    uintptr_t context_var;

    /* Checking for the Clock Failure status */
    if ((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_CLKFAIL_Msk) == OSC32KCTRL_STATUS_CLKFAIL_Msk)
    {
        /* Clearing the Clock Fail Interrupt */
        OSC32KCTRL_REGS->OSC32KCTRL_INTFLAG = OSC32KCTRL_INTFLAG_CLKFAIL_Msk;

        if(osc32kctrlObj.callback != NULL)
        {
            context_var = osc32kctrlObj.context;
            osc32kctrlObj.callback(context_var);
        }
    }
}
</#if>

<#if MCLK_INTENSET_CKRDY == true >

void MCLK_CallbackRegister (MCLK_CKRDY_CALLBACK callback, uintptr_t context)
{
    mclkObj.callback = callback;
    mclkObj.context = context;
}

void __attribute__((used)) MCLK_InterruptHandler(void)
{
    uintptr_t context_var;

    /* Checking for the Clock Ready Interrupt */
    if ((MCLK_REGS->MCLK_INTFLAG & MCLK_INTFLAG_CKRDY_Msk) == MCLK_INTFLAG_CKRDY_Msk)
    {
        /* Clearing the Clock Ready Interrupt */
        MCLK_REGS->MCLK_INTFLAG = MCLK_INTFLAG_CKRDY_Msk;

        if(mclkObj.callback != NULL)
        {
            context_var = mclkObj.context;
            mclkObj.callback(context_var);
        }
    }
}
</#if>
