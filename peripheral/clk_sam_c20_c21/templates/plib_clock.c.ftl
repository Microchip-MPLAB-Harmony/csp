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

<#if CONFIG_CLOCK_XOSC_CFDEN == true>

typedef struct
{
    OSCCTRL_CFD_CALLBACK   callback;
    uintptr_t        context;
} OSCCTRL_OBJECT;

/* Reference Object created for the OSCCTRL */
OSCCTRL_OBJECT oscctrlObj;

</#if>

<#if XOSC32K_CFDEN == true >

typedef struct
{
    OSC32KCTRL_CFD_CALLBACK   callback;
    uintptr_t        context;
} OSC32KCTRL_OBJECT;

/* Reference Object created for the OSCCTRL */
OSC32KCTRL_OBJECT osc32kctrlObj;

</#if>

static void OSCCTRL_Initialize(void)
{
<#if CONFIG_CLOCK_XOSC_ENABLE == true>
    /****************** XOSC Initialization   ********************************/

	<#if CONFIG_CLOCK_XOSC_CFDEN == true >
	/* Selection of the Clock failure detection (CFD) pre scalar */
	OSCCTRL_REGS->OSCCTRL_CFDPRESC = ${CONFIG_CLOCK_XOSC_CFDPRESC};
    </#if>

    /* Configure External Oscillator */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_XOSCCTRL = OSCCTRL_XOSCCTRL_STARTUP(${CONFIG_CLOCK_XOSC_STARTUP}) | OSCCTRL_XOSCCTRL_GAIN(${CONFIG_CLOCK_XOSC_GAIN})
                                                             ${CONFIG_CLOCK_XOSC_RUNSTDBY?then('| OSCCTRL_XOSCCTRL_RUNSTDBY_Msk',' ')}
															 ${(CONFIG_CLOCK_XOSC_ONDEMAND == "ENABLE")?then('| OSCCTRL_XOSCCTRL_ONDEMAND_Msk',' ')}
															 ${CONFIG_CLOCK_XOSC_CFDEN?then('| OSCCTRL_XOSCCTRL_CFDEN_Msk',' ')}
															 ${(XOSC_OSCILLATOR_MODE == "1")?then('| OSCCTRL_XOSCCTRL_XTALEN_Msk',' ')} | OSCCTRL_XOSCCTRL_ENABLE_Msk;</@compress>

    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCRDY_Msk) != OSCCTRL_STATUS_XOSCRDY_Msk)
    {
        /* Waiting for the XOSC Ready state */
    }

    <#if XOSC_AMPGC == true >
    /* Setting the Automatic Gain Control */
    OSCCTRL_REGS->OSCCTRL_XOSCCTRL |= OSCCTRL_XOSCCTRL_AMPGC_Msk;
    </#if>
</#if>
<#if CONFIG_CLOCK_OSC48M_ENABLE == true>
    <#if CALIBRATION_ROW == "0">
    uint32_t calibValue = (uint32_t)(((*(uint64_t*)0x806020) >> 19 ) & 0x3fffff);
    <#else>
    uint32_t calibValue = (uint32_t)(((*(uint64_t*)0x806020) >> 41 ) & 0x3fffff);
    </#if>
    OSCCTRL_REGS->OSCCTRL_CAL48M = calibValue;
	<#if (CONFIG_CLOCK_OSC48M_RUNSTDY == true) || (CONFIG_CLOCK_OSC48M_ONDEMAND == "ENABLE")>
    /* Configure 48MHz Oscillator */
	<@compress single_line=true>OSCCTRL_REGS->OSCCTRL_OSC48MCTRL = OSCCTRL_REGS->OSCCTRL_OSC48MCTRL
                                                             ${CONFIG_CLOCK_OSC48M_RUNSTDY?then('| OSCCTRL_OSC48MCTRL_RUNSTDBY_Msk',' ')}
															 ${(CONFIG_CLOCK_OSC48M_ONDEMAND == "ENABLE")?then('| OSCCTRL_OSC48MCTRL_ONDEMAND_Msk',' ')};</@compress>
	</#if>

	<#if CONFIG_CLOCK_OSC48M_STARTUP != "7">
    /* Selection of the StartUp Delay */
    OSCCTRL_REGS->OSCCTRL_OSC48MSTUP = OSCCTRL_OSC48MSTUP_STARTUP(${CONFIG_CLOCK_OSC48M_STARTUP});
	</#if>

	<#if CONFIG_CLOCK_OSC48M_DIV != "11">
    /* Selection of the Division Value */
    OSCCTRL_REGS->OSCCTRL_OSC48MDIV = OSCCTRL_OSC48MDIV_DIV(${CONFIG_CLOCK_OSC48M_DIV});

    while((OSCCTRL_REGS->OSCCTRL_OSC48MSYNCBUSY & OSCCTRL_OSC48MSYNCBUSY_OSC48MDIV_Msk) == OSCCTRL_OSC48MSYNCBUSY_OSC48MDIV_Msk)
    {
        /* Waiting for the synchronization */
    }

    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_OSC48MRDY_Msk) != OSCCTRL_STATUS_OSC48MRDY_Msk)
    {
        /* Waiting for the OSC48M Ready state */
    }
	</#if>
</#if>
}

static void OSC32KCTRL_Initialize(void)
{
<#if CONF_CLOCK_XOSC32K_ENABLE == true>
    /****************** XOSC32K initialization  ******************************/

    /* Configure 32K External Oscillator */
    <@compress single_line=true>OSC32KCTRL_REGS->OSC32KCTRL_XOSC32K = OSC32KCTRL_XOSC32K_STARTUP(${XOSC32K_STARTUP}) | OSC32KCTRL_XOSC32K_ENABLE_Msk
                                                               ${XOSC32K_RUNSTDBY?then('| OSC32KCTRL_XOSC32K_RUNSTDBY_Msk',' ')}
                                                               ${XOSC32K_EN1K?then('| OSC32KCTRL_XOSC32K_EN1K_Msk',' ')}
                                                               ${XOSC32K_EN32K?then('| OSC32KCTRL_XOSC32K_EN32K_Msk',' ')}
															   ${(XOSC32K_ONDEMAND == "ENABLE")?then('| OSC32KCTRL_XOSC32K_ONDEMAND_Msk',' ')}
															   ${(XOSC32K_OSCILLATOR_MODE == "1")?then('| OSC32KCTRL_XOSC32K_XTALEN_Msk',' ')};</@compress>

    <#if XOSC32K_CFDEN == true >
    /* Enable clock failure detection */
    OSC32KCTRL_REGS->OSC32KCTRL_CFDCTRL |= OSC32KCTRL_CFDCTRL_CFDEN_Msk  ${XOSC32K_CFDPRESC?then('| OSC32KCTRL_CFDCTRL_CFDPRESC_Msk','')};

    </#if>

    while(!((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_XOSC32KRDY_Msk) == OSC32KCTRL_STATUS_XOSC32KRDY_Msk))
    {
        /* Waiting for the XOSC32K Ready state */
    }
</#if>
<#if CONF_CLOCK_OSC32K_ENABLE =true>
    /****************** OSC32K Initialization  ******************************/

   uint32_t calibValue = (((*(uint32_t*)0x806020) >> 12 ) & 0x7f);

    /* Configure 32K RC oscillator */
    <@compress single_line=true>OSC32KCTRL_REGS->OSC32KCTRL_OSC32K = OSC32KCTRL_OSC32K_CALIB(calibValue)
                                                              | OSC32KCTRL_OSC32K_STARTUP(${OSC32K_STARTUP}) | OSC32KCTRL_OSC32K_ENABLE_Msk
                                                              ${OSC32K_RUNSTDBY?then('| OSC32KCTRL_OSC32K_RUNSTDBY_Msk',' ')}
                                                              ${OSC32K_EN1K?then('| OSC32KCTRL_OSC32K_EN1K_Msk',' ')}
                                                              ${OSC32K_EN32K?then('| OSC32KCTRL_OSC32K_EN32K_Msk',' ')}
															  ${(OSC32K_ONDEMAND == "ENABLE")?then('| OSC32KCTRL_OSC32K_ONDEMAND_Msk',' ')};</@compress>

    while(!((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_OSC32KRDY_Msk) == OSC32KCTRL_STATUS_OSC32KRDY_Msk))
    {
        /* Waiting for the OSC32K Ready state */
    }
<#else>
	OSC32KCTRL_REGS->OSC32KCTRL_OSC32K = 0x0;
</#if>

	OSC32KCTRL_REGS->OSC32KCTRL_RTCCTRL = OSC32KCTRL_RTCCTRL_RTCSEL(${CONFIG_CLOCK_RTC_SRC});
}

<#if CONFIG_CLOCK_DPLL_ENABLE == true >
static void FDPLL_Initialize(void)
{
	<#if CONFIG_CLOCK_DPLL_REF_CLOCK == "2">
	GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_0_INDEX}] = GCLK_PCHCTRL_GEN(${GCLK_ID_0_GENSEL})${GCLK_ID_0_WRITELOCK?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;
	while ((GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_0_INDEX}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
	</#if>

    /****************** DPLL Initialization  *********************************/

    /* Configure DPLL    */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DPLLCTRLB = OSCCTRL_DPLLCTRLB_FILTER(${CONFIG_CLOCK_DPLL_FILTER}) |
                                                                   OSCCTRL_DPLLCTRLB_LTIME(${CONFIG_CLOCK_DPLL_LOCK_TIME})|
																   OSCCTRL_DPLLCTRLB_REFCLK(${CONFIG_CLOCK_DPLL_REF_CLOCK})
                                                                   ${CONFIG_CLOCK_DPLL_LOCK_BYPASS?then('| OSCCTRL_DPLLCTRLB_LBYPASS_Msk', ' ')}
                                                                   ${CONFIG_CLOCK_DPLL_WAKEUP_FAST?then('| OSCCTRL_DPLLCTRLB_WUF_Msk', ' ')}
                                                                   ${CONFIG_CLOCK_DPLL_LOWPOWER_ENABLE?then('| OSCCTRL_DPLLCTRLB_LPEN_Msk', ' ')}
																   ${(CONFIG_CLOCK_DPLL_REF_CLOCK == "1")?then('| OSCCTRL_DPLLCTRLB_DIV(${CONFIG_CLOCK_DPLL_DIVIDER})', ' ')};</@compress>


    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DPLLRATIO = OSCCTRL_DPLLRATIO_LDRFRAC(${CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION}) |
                                                              OSCCTRL_DPLLRATIO_LDR(${CONFIG_CLOCK_DPLL_LDR_INTEGER});</@compress>

    while((OSCCTRL_REGS->OSCCTRL_DPLLSYNCBUSY & OSCCTRL_DPLLSYNCBUSY_DPLLRATIO_Msk) == OSCCTRL_DPLLSYNCBUSY_DPLLRATIO_Msk)
    {
        /* Waiting for the synchronization */
    }

	<#if CONFIG_CLOCK_DPLL_PRESCALAR != "0">
    /* Selection of the DPLL Pre-Scalar */
   OSCCTRL_REGS->OSCCTRL_DPLLPRESC = OSCCTRL_DPLLPRESC_PRESC(${CONFIG_CLOCK_DPLL_PRESCALAR});

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

    while((OSCCTRL_REGS->OSCCTRL_DPLLSTATUS & (OSCCTRL_DPLLSTATUS_LOCK_Msk | OSCCTRL_DPLLSTATUS_CLKRDY_Msk)) !=
                (OSCCTRL_DPLLSTATUS_LOCK_Msk | OSCCTRL_DPLLSTATUS_CLKRDY_Msk))
    {
        /* Waiting for the Ready state */
    }
}
</#if>

<#list 0..8 as i>
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
    <@compress single_line=true>GCLK_REGS->GCLK_GENCTRL[${i}] = GCLK_GENCTRL_DIV(${.vars[GCLK_DIVISONVALUE]})
                                                               | GCLK_GENCTRL_SRC(${.vars[GCLK_SRC]})
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
    /* Function to Initialize the Oscillators */
    OSCCTRL_Initialize();

    /* Function to Initialize the 32KHz Oscillators */
    OSC32KCTRL_Initialize();

${CLK_INIT_LIST}

<#if CONF_CPU_CLOCK_DIVIDER != '0x01'>
    /* selection of the CPU clock Division */
    MCLK_REGS->MCLK_CPUDIV = MCLK_CPUDIV_CPUDIV(${CONF_CPU_CLOCK_DIVIDER});

    while((MCLK_REGS->MCLK_INTFLAG & MCLK_INTFLAG_CKRDY_Msk) != MCLK_INTFLAG_CKRDY_Msk)
    {
        /* Wait for the Main Clock to be Ready */
    }
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
    GCLK_REGS->GCLK_PCHCTRL[${.vars[GCLK_ID_INDEX]}] = GCLK_PCHCTRL_GEN(${.vars[GCLK_ID_GENSEL]})${.vars[GCLK_ID_WRITELOCK]?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;

    while ((GCLK_REGS->GCLK_PCHCTRL[${.vars[GCLK_ID_INDEX]}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
    </#if>
    </#if>
</#list>

	<#if MCLK_AHB_INITIAL_VALUE != "0x3cff">
    /* Configure the AHB Bridge Clocks */
    MCLK_REGS->MCLK_AHBMASK = ${MCLK_AHB_INITIAL_VALUE};

    </#if>
    <#if MCLK_APBA_INITIAL_VALUE != "0xfff">
    /* Configure the APBA Bridge Clocks */
    MCLK_REGS->MCLK_APBAMASK = ${MCLK_APBA_INITIAL_VALUE};

    </#if>
    <#if MCLK_APBB_INITIAL_VALUE != "0x7">
    /* Configure the APBB Bridge Clocks */
    MCLK_REGS->MCLK_APBBMASK = ${MCLK_APBB_INITIAL_VALUE};

    </#if>
    <#if MCLK_APBC_INITIAL_VALUE != "0x0">
    <#if MCLK_APBC_INITIAL_VALUE??>
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

    <#if CONFIG_CLOCK_OSC48M_ENABLE == false>
    /*Disable RC oscillator*/
    
    OSCCTRL_REGS->OSCCTRL_OSC48MCTRL = 0x0;
    </#if>
}

<#if CONFIG_CLOCK_XOSC_CFDEN == true>

void OSCCTRL_CallbackRegister(OSCCTRL_CFD_CALLBACK callback, uintptr_t context)
{
    oscctrlObj.callback = callback;
    oscctrlObj.context = context;

    /* Enabling the Clock Fail Interrupt  */
    OSCCTRL_REGS->OSCCTRL_INTENSET = OSCCTRL_INTENSET_XOSCFAIL_Msk;
}

void OSCCTRL_Handler(void)
{
    /* Checking for the Clock Fail status */
    if ((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCFAIL_Msk) == OSCCTRL_STATUS_XOSCFAIL_Msk)
    {
        if (oscctrlObj.callback != NULL)
        {
            oscctrlObj.callback(oscctrlObj.context);
        }

        /* Clearing the XOSC Fail Interrupt Flag */
        OSCCTRL_REGS->OSCCTRL_INTFLAG = OSCCTRL_INTFLAG_XOSCFAIL_Msk;
    }
}

</#if>

<#if XOSC32K_CFDEN == true >

void OSC32KCTRL_CallbackRegister (OSC32KCTRL_CFD_CALLBACK callback, uintptr_t context)
{
    osc32kctrlObj.callback = callback;
    osc32kctrlObj.context = context;

   /* Enabling the Clock Failure Interrupt */
    OSC32KCTRL_REGS->OSC32KCTRL_INTENSET = OSC32KCTRL_INTENSET_CLKFAIL_Msk;
}

void OSC32KCTRL_Handler(void)
{
    /* Checking for the Clock Failure status */
    if ((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_CLKFAIL_Msk) == OSC32KCTRL_STATUS_CLKFAIL_Msk)
    {

        if(osc32kctrlObj.callback != NULL)
        {
            osc32kctrlObj.callback(osc32kctrlObj.context);
        }

       /* Clearing the Clock Fail Interrupt */
        OSC32KCTRL_REGS->OSC32KCTRL_INTFLAG = OSC32KCTRL_INTFLAG_CLKFAIL_Msk;
    }
}
</#if>
