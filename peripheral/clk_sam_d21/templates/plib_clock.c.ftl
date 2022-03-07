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
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#if SYSCTRL_INTERRUPT_ENABLE_VAL?? && SYSCTRL_INTERRUPT_ENABLE_VAL != "0x0">
static SYSCTRL_CALLBACK_OBJECT SYSCTRL_CallbackObj;

</#if>
static void SYSCTRL_Initialize(void)
{
<#if CONFIG_CLOCK_XOSC_ENABLE == true>
    /* Configure External Oscillator */
    <@compress single_line=true>SYSCTRL_REGS->SYSCTRL_XOSC = SYSCTRL_XOSC_STARTUP(${CONFIG_CLOCK_XOSC_STARTUP}U) | SYSCTRL_XOSC_GAIN(${CONFIG_CLOCK_XOSC_GAIN}U)
                                                             ${CONFIG_CLOCK_XOSC_RUNSTDBY?then('| SYSCTRL_XOSC_RUNSTDBY_Msk',' ')}
                                                             ${(CONFIG_CLOCK_XOSC_ONDEMAND == "ENABLE")?then('| SYSCTRL_XOSC_ONDEMAND_Msk',' ')}
                                                             ${(XOSC_OSCILLATOR_MODE == "1")?then('| SYSCTRL_XOSC_XTALEN_Msk',' ')} | SYSCTRL_XOSC_ENABLE_Msk;</@compress>
    <#if CONFIG_CLOCK_XOSC_ONDEMAND != "ENABLE">
    while((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_XOSCRDY_Msk) != SYSCTRL_PCLKSR_XOSCRDY_Msk)
    {
        /* Waiting for the XOSC Ready state */
    }
    </#if>

    <#if XOSC_AMPGC == true>
    /* Setting the Automatic Gain Control */
    SYSCTRL_REGS->SYSCTRL_XOSC |= SYSCTRL_XOSC_AMPGC_Msk;
    </#if>
</#if>
<#if ((CONFIG_CLOCK_OSC8M_ENABLE == true) && (CONFIG_CLOCK_OSC8M_RUNSTDY == true || CONFIG_CLOCK_OSC8M_ONDEMAND == "ENABLE" || CONFIG_CLOCK_OSC8M_PRES != "0x3"))>

    /* Configure 8MHz Oscillator */
    <@compress single_line=true>SYSCTRL_REGS->SYSCTRL_OSC8M = (SYSCTRL_REGS->SYSCTRL_OSC8M & (SYSCTRL_OSC8M_CALIB_Msk | SYSCTRL_OSC8M_FRANGE_Msk)) | SYSCTRL_OSC8M_ENABLE_Msk | SYSCTRL_OSC8M_PRESC(${CONFIG_CLOCK_OSC8M_PRES}U)
                                                             ${CONFIG_CLOCK_OSC8M_RUNSTDY?then('| SYSCTRL_OSC8M_RUNSTDBY_Msk',' ')}
                                                             ${(CONFIG_CLOCK_OSC8M_ONDEMAND == "ENABLE")?then('| SYSCTRL_OSC8M_ONDEMAND_Msk',' ')};</@compress>
    <#if CONFIG_CLOCK_OSC8M_ONDEMAND != "ENABLE">

    while((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_OSC8MRDY_Msk) != SYSCTRL_PCLKSR_OSC8MRDY_Msk)
    {
        /* Waiting for the OSC8M Ready state */
    }
    </#if>
</#if>
<#if CONF_CLOCK_XOSC32K_ENABLE == true>
    /****************** XOSC32K initialization  ******************************/

    /* Configure 32K External Oscillator */
    <@compress single_line=true>SYSCTRL_REGS->SYSCTRL_XOSC32K = SYSCTRL_XOSC32K_STARTUP(${XOSC32K_STARTUP}U) | SYSCTRL_XOSC32K_ENABLE_Msk
                                                               ${XOSC32K_RUNSTDBY?then('| SYSCTRL_XOSC32K_RUNSTDBY_Msk',' ')}
                                                               ${XOSC32K_EN32K?then('| SYSCTRL_XOSC32K_EN32K_Msk',' ')}
                                                               ${(XOSC32K_ONDEMAND == "ENABLE")?then('| SYSCTRL_XOSC32K_ONDEMAND_Msk',' ')}
                                                               ${(XOSC32K_OSCILLATOR_MODE == "1")?then('| SYSCTRL_XOSC32K_XTALEN_Msk',' ')};</@compress>
    <#if XOSC32K_ONDEMAND != "ENABLE">
    while(!((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_XOSC32KRDY_Msk) == SYSCTRL_PCLKSR_XOSC32KRDY_Msk))
    {
        /* Waiting for the XOSC32K Ready state */
    }

    </#if>
</#if>
<#if CONF_CLOCK_OSC32K_ENABLE == true>
    /****************** OSC32K Initialization  ******************************/
    uint32_t calibValue = (uint32_t)(((*(uint64_t*)0x806020U) >> 38U ) & 0x7FU);
    /* Configure 32K RC oscillator */
    <@compress single_line=true>SYSCTRL_REGS->SYSCTRL_OSC32K = SYSCTRL_OSC32K_CALIB(calibValue) |
                                                              SYSCTRL_OSC32K_STARTUP(${OSC32K_STARTUP}U) | SYSCTRL_OSC32K_ENABLE_Msk
                                                              ${OSC32K_RUNSTDBY?then('| SYSCTRL_OSC32K_RUNSTDBY_Msk',' ')}
                                                              ${OSC32K_EN32K?then('| SYSCTRL_OSC32K_EN32K_Msk',' ')}
                                                              ${(OSC32K_ONDEMAND == "ENABLE")?then('| SYSCTRL_OSC32K_ONDEMAND_Msk',' ')};</@compress>
    <#if OSC32K_ONDEMAND != "ENABLE">
    while(!((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_OSC32KRDY_Msk) == SYSCTRL_PCLKSR_OSC32KRDY_Msk))
    {
        /* Waiting for the OSC32K Ready state */
    }
    </#if>
<#else>
    SYSCTRL_REGS->SYSCTRL_OSC32K = 0x0U;
</#if>
}

<#if CONFIG_CLOCK_DPLL_ENABLE == true >
static void FDPLL_Initialize(void)
{
    <#if CONFIG_CLOCK_DPLL_REF_CLOCK == "0x2">
    GCLK_REGS->GCLK_CLKCTRL = GCLK_CLKCTRL_GEN(${GCLK_ID_1_GENSEL})${GCLK_ID_1_WRITELOCK?then(' | GCLK_CLKCTRL_WRTLOCK_Msk', ' ')} | GCLK_CLKCTRL_CLKEN_Msk | GCLK_CLKCTRL_ID(${GCLK_ID_1_INDEX});
    </#if>

    /****************** DPLL Initialization  *********************************/

    /* Configure DPLL    */
    <@compress single_line=true>SYSCTRL_REGS->SYSCTRL_DPLLCTRLB = SYSCTRL_DPLLCTRLB_FILTER(${CONFIG_CLOCK_DPLL_FILTER}U) |
                                                                  SYSCTRL_DPLLCTRLB_LTIME(${CONFIG_CLOCK_DPLL_LOCK_TIME}U)|
                                                                  SYSCTRL_DPLLCTRLB_REFCLK(${CONFIG_CLOCK_DPLL_REF_CLOCK}U)
                                                                  ${CONFIG_CLOCK_DPLL_LOCK_BYPASS?then('| SYSCTRL_DPLLCTRLB_LBYPASS_Msk', ' ')}
                                                                  ${CONFIG_CLOCK_DPLL_WAKEUP_FAST?then('| SYSCTRL_DPLLCTRLB_WUF_Msk', ' ')}
                                                                  ${CONFIG_CLOCK_DPLL_LOWPOWER_ENABLE?then('| SYSCTRL_DPLLCTRLB_LPEN_Msk', ' ')}
                                                                  ${(CONFIG_CLOCK_DPLL_REF_CLOCK == "0x1")?then('| SYSCTRL_DPLLCTRLB_DIV(${CONFIG_CLOCK_DPLL_DIVIDER}U)', ' ')};</@compress>


    <@compress single_line=true>SYSCTRL_REGS->SYSCTRL_DPLLRATIO = SYSCTRL_DPLLRATIO_LDRFRAC(${CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION}U) |
                                                                  SYSCTRL_DPLLRATIO_LDR(${CONFIG_CLOCK_DPLL_LDR_INTEGER}U);</@compress>

    /* Selection of the DPLL Enable */
    SYSCTRL_REGS->SYSCTRL_DPLLCTRLA = SYSCTRL_DPLLCTRLA_ENABLE_Msk ${(CONFIG_CLOCK_DPLL_ONDEMAND == "1")?then('| SYSCTRL_DPLLCTRLA_ONDEMAND_Msk',' ')} ${CONFIG_CLOCK_DPLL_RUNSTDY?then('| SYSCTRL_DPLLCTRLA_RUNSTDBY_Msk','')};
    <#if CONFIG_CLOCK_DPLL_ONDEMAND != "1">

    while((SYSCTRL_REGS->SYSCTRL_DPLLSTATUS & (SYSCTRL_DPLLSTATUS_LOCK_Msk | SYSCTRL_DPLLSTATUS_CLKRDY_Msk)) !=
                (SYSCTRL_DPLLSTATUS_LOCK_Msk | SYSCTRL_DPLLSTATUS_CLKRDY_Msk))
    {
        /* Waiting for the Ready state */
    }
    </#if>
}
</#if>

<#if CONFIG_CLOCK_DFLL_ENABLE == true >
static void DFLL_Initialize(void)
{
    /****************** DFLL Initialization  *********************************/
    SYSCTRL_REGS->SYSCTRL_DFLLCTRL &= (uint16_t)(~SYSCTRL_DFLLCTRL_ONDEMAND_Msk);

    while((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_DFLLRDY_Msk) != SYSCTRL_PCLKSR_DFLLRDY_Msk)
    {
        /* Waiting for the Ready state */
    }

    /*Load Calibration Value*/
    uint32_t calibCoarse = (((*(uint32_t*)0x806024U) >> 26U ) & 0x3FU);
    calibCoarse = (((calibCoarse) == 0x3FU) ? 0x1FU : (calibCoarse));

    <@compress single_line=true>SYSCTRL_REGS->SYSCTRL_DFLLVAL = SYSCTRL_DFLLVAL_COARSE(calibCoarse) |
                                                                SYSCTRL_DFLLVAL_FINE(512U);</@compress>

    <#if CONFIG_CLOCK_DFLL_OPMODE == "1">
    <#if CONFIG_CLOCK_DFLL_USB == false>
    GCLK_REGS->GCLK_CLKCTRL = GCLK_CLKCTRL_GEN(${GCLK_ID_0_GENSEL}U)${GCLK_ID_0_WRITELOCK?then(' | GCLK_CLKCTRL_WRTLOCK_Msk', ' ')} | GCLK_CLKCTRL_CLKEN_Msk | GCLK_CLKCTRL_ID(${GCLK_ID_0_INDEX}U);
    </#if>
    while((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_DFLLRDY_Msk) != SYSCTRL_PCLKSR_DFLLRDY_Msk)
    {
        /* Waiting for the Ready state */
    }
    SYSCTRL_REGS->SYSCTRL_DFLLMUL = SYSCTRL_DFLLMUL_MUL(${CONFIG_CLOCK_DFLL_MUL}U) | SYSCTRL_DFLLMUL_FSTEP(${CONFIG_CLOCK_DFLL_FINE}U) | SYSCTRL_DFLLMUL_CSTEP(${CONFIG_CLOCK_DFLL_COARSE}U);

    </#if>
    while((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_DFLLRDY_Msk) != SYSCTRL_PCLKSR_DFLLRDY_Msk)
    {
        /* Waiting for the Ready state */
    }

    /* Configure DFLL    */
    <@compress single_line=true>SYSCTRL_REGS->SYSCTRL_DFLLCTRL = SYSCTRL_DFLLCTRL_ENABLE_Msk ${(CONFIG_CLOCK_DFLL_OPMODE == "1")?then('| SYSCTRL_DFLLCTRL_MODE_Msk ', ' ')}
    <#lt>                               ${(CONFIG_CLOCK_DFLL_ONDEMAND == "1")?then("| SYSCTRL_DFLLCTRL_ONDEMAND_Msk ", "")}
    <#lt>                               ${CONFIG_CLOCK_DFLL_USB?then('| SYSCTRL_DFLLCTRL_USBCRM_Msk ', ' ')}
    <#lt>                               ${CONFIG_CLOCK_DFLL_WAIT_LOCK?then('| SYSCTRL_DFLLCTRL_WAITLOCK_Msk ', ' ')}
    <#lt>                               ${CONFIG_CLOCK_DFLL_BYPASS_COARSE?then('| SYSCTRL_DFLLCTRL_BPLCKC_Msk ', ' ')}
    <#lt>                               ${CONFIG_CLOCK_DFLL_QUICK_LOCK?then('| SYSCTRL_DFLLCTRL_QLDIS_Msk ', ' ')}
    <#lt>                               ${CONFIG_CLOCK_DFLL_CHILL_CYCLE?then('| SYSCTRL_DFLLCTRL_CCDIS_Msk ', ' ')}
    <#lt>                               ${CONFIG_CLOCK_DFLL_LLAW?then('| SYSCTRL_DFLLCTRL_LLAW_Msk ', ' ')}
    <#lt>                               ${CONFIG_CLOCK_DFLL_STABLE?then('| SYSCTRL_DFLLCTRL_STABLE_Msk ', ' ')}
    <#lt>                               ;</@compress>

    <#if CONFIG_CLOCK_DFLL_OPMODE == "1" && CONFIG_CLOCK_DFLL_USB == false>
    while((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_DFLLLCKF_Msk) != SYSCTRL_PCLKSR_DFLLLCKF_Msk)
    {
        /* Waiting for DFLL to fully lock to meet clock accuracy */
    }
    <#elseif CONFIG_CLOCK_DFLL_ONDEMAND != "1">
    while((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_DFLLRDY_Msk) != SYSCTRL_PCLKSR_DFLLRDY_Msk)
    {
        /* Waiting for DFLL to be ready */
    }
    </#if>
}
</#if>

<#list 0..8 as i>
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

<#if (CONF_CPU_CLOCK_DIVIDER != "0")>
    /* selection of the CPU clock Division */
    PM_REGS->PM_CPUSEL = PM_CPUSEL_CPUDIV(${CONF_CPU_CLOCK_DIVIDER});
</#if>
    </#if>
    <@compress single_line=true>GCLK_REGS->GCLK_GENCTRL = GCLK_GENCTRL_SRC(${.vars[GCLK_SRC]}U)
                                                               ${(.vars[GCLK_DIVISONSELECTION] == "DIV2")?then('| GCLK_GENCTRL_DIVSEL_Msk' , ' ')}
                                                               ${(.vars[GCLK_IMPROVE_DUTYCYCLE])?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                               ${(.vars[GCLK_RUNSTDBY])?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
                                                               <#if i < GCLK_NUM_PADS >
                                                               ${(.vars[GCLK_OUTPUTENABLE])?then('| GCLK_GENCTRL_OE_Msk', ' ')}
                                                               ${((.vars[GCLK_OUTPUTOFFVALUE] == "HIGH"))?then('| GCLK_GENCTRL_OOV_Msk', ' ')}
                                                               </#if>
                                                               | GCLK_GENCTRL_GENEN_Msk
                                                               | GCLK_GENCTRL_ID(${i}U);</@compress>

    <#if (.vars[GCLK_DIVISONVALUE] > 1)>
    GCLK_REGS->GCLK_GENDIV = GCLK_GENDIV_DIV(${.vars[GCLK_DIVISONVALUE]}U) | GCLK_GENDIV_ID(${i}U);
    </#if>
    while((GCLK_REGS->GCLK_STATUS & GCLK_STATUS_SYNCBUSY_Msk) == GCLK_STATUS_SYNCBUSY_Msk)
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
    SYSCTRL_Initialize();

${CLK_INIT_LIST}

<#list 2..GCLK_MAX_ID as i>
    <#assign GCLK_ID_CHEN = "GCLK_ID_" + i + "_CHEN">
    <#assign GCLK_ID_INDEX = "GCLK_ID_" + i + "_INDEX">
    <#assign GCLK_ID_NAME = "GCLK_ID_" + i + "_NAME">
    <#assign GCLK_ID_GENSEL = "GCLK_ID_" + i + "_GENSEL">
    <#assign GCLK_ID_WRITELOCK = "GCLK_ID_" + i + "_WRITELOCK">
        <#if .vars[GCLK_ID_CHEN]?has_content>
            <#if (.vars[GCLK_ID_CHEN] != false)>
    /* Selection of the Generator and write Lock for ${.vars[GCLK_ID_NAME]} */
    GCLK_REGS->GCLK_CLKCTRL = GCLK_CLKCTRL_ID(${.vars[GCLK_ID_INDEX]}U) | GCLK_CLKCTRL_GEN(${.vars[GCLK_ID_GENSEL]}U)${.vars[GCLK_ID_WRITELOCK]?then(' | GCLK_CLKCTRL_WRTLOCK_Msk', ' ')} | GCLK_CLKCTRL_CLKEN_Msk;
    </#if>
    </#if>
</#list>
    <#if PM_APBA_DIV != "0">

    /* Configure APBA Divider */
    PM_REGS->PM_APBASEL = ${PM_APBA_DIV}U;
    </#if>
    <#if PM_APBB_DIV != "0">

    /* Configure APBB Divider */
    PM_REGS->PM_APBBSEL = ${PM_APBB_DIV}U;
    </#if>
    <#if PM_APBC_DIV != "0">

    /* Configure APBC Divider */
    PM_REGS->PM_APBCSEL = ${PM_APBC_DIV}U;
    </#if>

    <#if PM_AHB_INITIAL_VALUE != "0x7f">
    /* Configure the AHB Bridge Clocks */
    PM_REGS->PM_AHBMASK = ${PM_AHB_INITIAL_VALUE}U;

    </#if>
    <#if PM_APBA_INITIAL_VALUE != "0x7f">
    /* Configure the APBA Bridge Clocks */
    PM_REGS->PM_APBAMASK = ${PM_APBA_INITIAL_VALUE}U;

    </#if>
    <#if PM_APBB_INITIAL_VALUE != "0x7f">
    /* Configure the APBB Bridge Clocks */
    PM_REGS->PM_APBBMASK = ${PM_APBB_INITIAL_VALUE}U;

    </#if>
    <#if PM_APBC_INITIAL_VALUE != "0x10000">
    <#if PM_APBC_INITIAL_VALUE??>
    /* Configure the APBC Bridge Clocks */
    PM_REGS->PM_APBCMASK = ${PM_APBC_INITIAL_VALUE}U;

    </#if>
    </#if>
    <#if PM_APBD_INITIAL_VALUE??>
    <#if PM_APBD_INITIAL_VALUE != "0x0">
    /* Configure the APBD Bridge Clocks */
    PM_REGS->PM_APBDMASK = ${PM_APBD_INITIAL_VALUE}U;

    </#if>
    </#if>

<#if CONFIG_CLOCK_OSC8M_ENABLE == false>
    /*Disable RC oscillator*/
    SYSCTRL_REGS->SYSCTRL_OSC8M = 0x0U;
</#if>
<#if SYSCTRL_INTERRUPT_ENABLE_VAL?? && SYSCTRL_INTERRUPT_ENABLE_VAL != "0x0">

    SYSCTRL_REGS->SYSCTRL_INTENSET = ${SYSCTRL_INTERRUPT_ENABLE_VAL}U;
</#if>
}
<#if SYSCTRL_INTERRUPT_ENABLE_VAL?? && SYSCTRL_INTERRUPT_ENABLE_VAL != "0x0">

void SYSCTRL_CallbackRegister(SYSCTRL_CALLBACK callback, uintptr_t context)
{
    SYSCTRL_CallbackObj.callback = callback;
    SYSCTRL_CallbackObj.context = context;
}

void SYSCTRL_InterruptHandler(void)
{
<#if SYSCTRL_INTERRUPT_XOSCRDY>
    if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_XOSCRDY_Msk) == SYSCTRL_INTFLAG_XOSCRDY_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_XOSCRDY_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_XOSCRDY_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_XOSC32KRDY>
<#if SYSCTRL_INTERRUPT_XOSCRDY>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_XOSC32KRDY_Msk) == SYSCTRL_INTFLAG_XOSC32KRDY_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_XOSC32KRDY_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_XOSC32KRDY_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_OSC32KRDY>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_OSC32KRDY_Msk) == SYSCTRL_INTFLAG_OSC32KRDY_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_OSC32KRDY_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_OSC32KRDY_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_OSC8MRDY>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_OSC8MRDY_Msk) == SYSCTRL_INTFLAG_OSC8MRDY_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_OSC8MRDY_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_OSC8MRDY_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_DFLLRDY>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_DFLLRDY_Msk) == SYSCTRL_INTFLAG_DFLLRDY_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_DFLLRDY_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_DFLLRDY_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_DFLLOOB>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY ||
     SYSCTRL_INTERRUPT_DFLLRDY>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_DFLLOOB_Msk) == SYSCTRL_INTFLAG_DFLLOOB_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_DFLLOOB_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_DFLLOOB_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_DFLLLCKF>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY ||
     SYSCTRL_INTERRUPT_DFLLRDY || SYSCTRL_INTERRUPT_DFLLOOB>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_DFLLLCKF_Msk) == SYSCTRL_INTFLAG_DFLLLCKF_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_DFLLLCKF_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_DFLLLCKF_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_DFLLLCKC>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY ||
     SYSCTRL_INTERRUPT_DFLLRDY || SYSCTRL_INTERRUPT_DFLLOOB || SYSCTRL_INTERRUPT_DFLLLCKF>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_DFLLLCKC_Msk) == SYSCTRL_INTFLAG_DFLLLCKC_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_DFLLLCKC_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_DFLLLCKC_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_DFLLRCS>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY ||
     SYSCTRL_INTERRUPT_DFLLRDY || SYSCTRL_INTERRUPT_DFLLOOB || SYSCTRL_INTERRUPT_DFLLLCKF || SYSCTRL_INTERRUPT_DFLLLCKC>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_DFLLRCS_Msk) == SYSCTRL_INTFLAG_DFLLRCS_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_DFLLRCS_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_DFLLRCS_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_BOD33RDY>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY ||
     SYSCTRL_INTERRUPT_DFLLRDY || SYSCTRL_INTERRUPT_DFLLOOB || SYSCTRL_INTERRUPT_DFLLLCKF || SYSCTRL_INTERRUPT_DFLLLCKC ||
     SYSCTRL_INTERRUPT_DFLLRCS>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_BOD33RDY_Msk) == SYSCTRL_INTFLAG_BOD33RDY_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_BOD33RDY_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_BOD33RDY_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_BOD33DET>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY ||
     SYSCTRL_INTERRUPT_DFLLRDY || SYSCTRL_INTERRUPT_DFLLOOB || SYSCTRL_INTERRUPT_DFLLLCKF || SYSCTRL_INTERRUPT_DFLLLCKC ||
     SYSCTRL_INTERRUPT_DFLLRCS || SYSCTRL_INTERRUPT_BOD33RDY>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_BOD33DET_Msk) == SYSCTRL_INTFLAG_BOD33DET_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_BOD33DET_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_BOD33DET_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_B33SRDY>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY ||
     SYSCTRL_INTERRUPT_DFLLRDY || SYSCTRL_INTERRUPT_DFLLOOB || SYSCTRL_INTERRUPT_DFLLLCKF || SYSCTRL_INTERRUPT_DFLLLCKC ||
     SYSCTRL_INTERRUPT_DFLLRCS || SYSCTRL_INTERRUPT_BOD33RDY || SYSCTRL_INTERRUPT_BOD33DET>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_B33SRDY_Msk) == SYSCTRL_INTFLAG_B33SRDY_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_B33SRDY_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_B33SRDY_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_DPLLLCKR>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY ||
     SYSCTRL_INTERRUPT_DFLLRDY || SYSCTRL_INTERRUPT_DFLLOOB || SYSCTRL_INTERRUPT_DFLLLCKF || SYSCTRL_INTERRUPT_DFLLLCKC ||
     SYSCTRL_INTERRUPT_DFLLRCS || SYSCTRL_INTERRUPT_BOD33RDY || SYSCTRL_INTERRUPT_BOD33DET || SYSCTRL_INTERRUPT_B33SRDY>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_DPLLLCKR_Msk) == SYSCTRL_INTFLAG_DPLLLCKR_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_DPLLLCKR_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_DPLLLCKR_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_DPLLLCKF>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY ||
     SYSCTRL_INTERRUPT_DFLLRDY || SYSCTRL_INTERRUPT_DFLLOOB || SYSCTRL_INTERRUPT_DFLLLCKF || SYSCTRL_INTERRUPT_DFLLLCKC ||
     SYSCTRL_INTERRUPT_DFLLRCS || SYSCTRL_INTERRUPT_BOD33RDY || SYSCTRL_INTERRUPT_BOD33DET || SYSCTRL_INTERRUPT_B33SRDY ||
     SYSCTRL_INTERRUPT_DPLLLCKR>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_DPLLLCKF_Msk) == SYSCTRL_INTFLAG_DPLLLCKF_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_DPLLLCKF_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_DPLLLCKF_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
<#if SYSCTRL_INTERRUPT_DPLLLTO>
<#if SYSCTRL_INTERRUPT_XOSCRDY || SYSCTRL_INTERRUPT_XOSC32KRDY || SYSCTRL_INTERRUPT_OSC32KRDY || SYSCTRL_INTERRUPT_OSC8MRDY ||
     SYSCTRL_INTERRUPT_DFLLRDY || SYSCTRL_INTERRUPT_DFLLOOB || SYSCTRL_INTERRUPT_DFLLLCKF || SYSCTRL_INTERRUPT_DFLLLCKC ||
     SYSCTRL_INTERRUPT_DFLLRCS || SYSCTRL_INTERRUPT_BOD33RDY || SYSCTRL_INTERRUPT_BOD33DET || SYSCTRL_INTERRUPT_B33SRDY ||
     SYSCTRL_INTERRUPT_DPLLLCKR || SYSCTRL_INTERRUPT_DPLLLCKF>
    else <#else>    </#if>if ((SYSCTRL_REGS->SYSCTRL_INTFLAG & SYSCTRL_INTFLAG_DPLLLTO_Msk) == SYSCTRL_INTFLAG_DPLLLTO_Msk)
    {
        SYSCTRL_REGS->SYSCTRL_INTFLAG |= SYSCTRL_INTFLAG_DPLLLTO_Msk;

        if(SYSCTRL_CallbackObj.callback != NULL)
        {
            SYSCTRL_CallbackObj.callback(SYSCTRL_INTFLAG_DPLLLTO_Msk, SYSCTRL_CallbackObj.context);
        }
    }
</#if>
}
</#if>
