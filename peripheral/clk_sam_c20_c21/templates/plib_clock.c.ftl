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
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "plib_clock.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: MACRO DEFINATIONS
// *****************************************************************************
// *****************************************************************************

#define MCLK_AHB_CLOCK_INITIAL_VALUE  (${MCLK_AHB_INITIAL_VALUE})

#define MCLK_APBA_CLOCK_INITIAL_VALUE  (${MCLK_APBA_INITIAL_VALUE})

#define MCLK_APBB_CLOCK_INITIAL_VALUE  (${MCLK_APBB_INITIAL_VALUE})

#define MCLK_APBC_CLOCK_INITIAL_VALUE  (${MCLK_APBC_INITIAL_VALUE})

#define MCLK_APBD_CLOCK_INITIAL_VALUE  (${MCLK_APBD_INITIAL_VALUE})
<#if XOSC_INTERRUPT_MODE = true || DPLL_INTERRUPT_MODE = true>

// *****************************************************************************
/*OSCCTRL Object

  Summary:
    Defines the data type for the data structures used for Oscillator controller
    operations.

  Description:
    This may be for used for OSCCTRL operations.

  Remarks:
    None.
*/
typedef struct
{

    /* OSCCTRL callback Handler */
    OSCCTRL_CALLBACK   callback;

    /* client context*/
    uintptr_t        context;

}OSCCTRL_OBJECT;

/* Reference Object created for the OSCCTRL */
OSCCTRL_OBJECT oscctrlObj;

</#if>
<#if XOSC32K_INTERRUPT_MODE = true >
// *****************************************************************************
/*OSC32KCTRL Object

  Summary:
    Defines the data type for the data structures used for 32KHz Oscillator
    Controller Operations.

  Description:
    This may be for used for OSC32KCTRL operations.

  Remarks:
    None.
*/
typedef struct
{

    /* OSC32KCTRL Callback Handler */
    OSC32KCTRL_CFD_CALLBACK   callback;

    /* client context*/
    uintptr_t        context;

}OSC32KCTRL_OBJECT;

/* Reference Object created for the OSCCTRL */
OSC32KCTRL_OBJECT osc32kctrlObj;

</#if>

static void OSCCTRL_Initialize(void)
{
<#if CONFIG_CLOCK_XOSC_ENABLE = true>
    /****************** XOSC Initialization   ********************************/

	<#if CONFIG_CLOCK_XOSC_CFDEN = true >

    /* Selection of the Clock failure detection (CFD) pre scalar */
    OSCCTRL_REGS->OSCCTRL_CFDPRESC = ${CONFIG_CLOCK_XOSC_CFDPRESC};

    </#if>
	
    /* Selection of the startup time ,StandBy */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_XOSCCTRL = OSCCTRL_XOSCCTRL_STARTUP(${CONFIG_CLOCK_XOSC_STARTUP}) | OSCCTRL_XOSCCTRL_GAIN(${CONFIG_CLOCK_XOSC_GAIN})
                                                             ${CONFIG_CLOCK_XOSC_RUNSTDBY?then('| OSCCTRL_XOSCCTRL_RUNSTDBY_Msk',' ')}
															 ${(CONFIG_CLOCK_XOSC_ONDEMAND == "1")?then('| OSCCTRL_XOSCCTRL_ONDEMAND_Msk',' ')}
															 ${CONFIG_CLOCK_XOSC_CFDEN?then('| OSCCTRL_XOSCCTRL_CFDEN_Msk',' ')}
															 ${(XOSC_OSCILLATOR_MODE == "1")?then('| OSCCTRL_XOSCCTRL_XTALEN_Msk',' ')} | OSCCTRL_XOSCCTRL_ENABLE_Msk;</@compress>

    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCRDY_Msk) != OSCCTRL_STATUS_XOSCRDY_Msk)
    {
        /* Waiting for the XOSC Ready state */
    }

    <#if XOSC_AMPGC = true >
    /* Setting the Automatic Gain Control */
    OSCCTRL_REGS->OSCCTRL_XOSCCTRL |= OSCCTRL_XOSCCTRL_AMPGC_Msk;
    </#if>
</#if>

<#if CONFIG_CLOCK_OSC48M_ENABLE = true>

    /****************** OSC48M Initialization  *******************************/

	<#if CONFIG_CLOCK_OSC48M_RUNSTDY == true || CONFIG_CLOCK_OSC48M_ONDEMAND == "1">
	/* Selection of the ONDEMAND and RUN StandBy */
	<#if CONFIG_CLOCK_OSC48M_RUNSTDY == true>
    OSCCTRL_REGS->OSCCTRL_OSC48MCTRL |= OSCCTRL_OSC48MCTRL_RUNSTDBY_Msk ${(CONFIG_CLOCK_OSC48M_ONDEMAND == "1")?then('| OSCCTRL_OSC48MCTRL_ONDEMAND_Msk',' ')};
	<#else>
	OSCCTRL_REGS->OSCCTRL_OSC48MCTRL |= OSCCTRL_OSC48MCTRL_ONDEMAND_Msk;
	</#if>
	</#if>
	
	<#if CONFIG_CLOCK_OSC48M_STARTUP != "7" || CONFIG_CLOCK_OSC48M_DIV != "11">
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
	</#if>
    while((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_OSC48MRDY_Msk) != OSCCTRL_STATUS_OSC48MRDY_Msk)
    {
        /* Waiting for the OSC48M Ready state */
    }
	
	</#if>
<#else>
	OSCCTRL_REGS->OSCCTRL_OSC48MCTRL = 0x0;
</#if>

}

static void OSC32KCTRL_Initialize(void)
{
<#if CONF_CLOCK_XOSC32K_ENABLE = true>
    /****************** XOSC32K initialization  ******************************/

    /* Selection of the Startup time , standby mode , 1K output ,32k output */
    <@compress single_line=true>OSC32KCTRL_REGS->OSC32KCTRL_XOSC32K = OSC32KCTRL_XOSC32K_STARTUP(${XOSC32K_STARTUP}) | OSC32KCTRL_XOSC32K_ENABLE_Msk
                                                               ${XOSC32K_RUNSTDBY?then('| OSC32KCTRL_XOSC32K_RUNSTDBY_Msk',' ')}
                                                               ${XOSC32K_EN1K?then('| OSC32KCTRL_XOSC32K_EN1K_Msk',' ')}
                                                               ${XOSC32K_EN32K?then('| OSC32KCTRL_XOSC32K_EN32K_Msk',' ')}
															   ${(XOSC32K_ONDEMAND == "1")?then('| OSC32KCTRL_XOSC32K_ONDEMAND_Msk',' ')}
															   ${(XOSC32K_OSCILLATOR_MODE == "1")?then('| OSC32KCTRL_XOSC32K_XTALEN_Msk',' ')};</@compress>
															   
    <#if XOSC32K_CFDEN = true >
    /* Selection of the CFD enable and Pre scalar */
    OSC32KCTRL_REGS->OSC32KCTRL_CFDCTRL |= OSC32KCTRL_CFDCTRL_CFDEN_Msk  ${XOSC32K_CFDPRESC?then('| OSC32KCTRL_CFDCTRL_CFDPRESC_Msk','')};

    </#if>

    while(!((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_XOSC32KRDY_Msk) == OSC32KCTRL_STATUS_XOSC32KRDY_Msk))
    {
        /* Waiting for the XOSC32K Ready state */
    }
</#if>
<#if CONF_CLOCK_OSC32K_ENABLE =true>
    /****************** OSC32K Initialization  ******************************/

    /*
     * Selection of the Startup time , 1K output , 32K output standby
     * and on demand
     */
    <@compress single_line=true>OSC32KCTRL_REGS->OSC32KCTRL_OSC32K = OSC32KCTRL_OSC32K_STARTUP(${OSC32K_STARTUP}) | OSC32KCTRL_OSC32K_ENABLE_Msk
                                                              ${OSC32K_RUNSTDBY?then('| OSC32KCTRL_OSC32K_RUNSTDBY_Msk',' ')}
                                                              ${OSC32K_EN1K?then('| OSC32KCTRL_OSC32K_EN1K_Msk',' ')}
                                                              ${OSC32K_EN32K?then('| OSC32KCTRL_OSC32K_EN32K_Msk',' ')}
															  ${(OSC32K_ONDEMAND == "1")?then('| OSC32KCTRL_OSC32K_ONDEMAND_Msk',' ')};</@compress>

    while(!((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_OSC32KRDY_Msk) == OSC32KCTRL_STATUS_OSC32KRDY_Msk))
    {
        /* Waiting for the OSC32K Ready state */
    }
<#else>
	OSC32KCTRL_REGS->OSC32KCTRL_OSC32K = 0x0;
</#if>

    <#if CONFIG_CLOCK_OSCULP32K_CALIB_ENABLE = true >
    /* User Selection of the Calibration Value */
    OSC32KCTRL_REGS->OSC32KCTRL_OSCULP32K = OSC32KCTRL_OSCULP32K_CALIB(${OSCULP32K_CALIB_VALUE});
    </#if>
}

<#if CONFIG_CLOCK_DPLL_ENABLE = true >
static void OSCCTRL_DPLLInitialize(void)
{
	<#if CONFIG_CLOCK_DPLL_REF_CLOCK == "2">
	GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_22_INDEX}] = GCLK_PCHCTRL_GEN(${GCLK_ID_22_GENSEL})${GCLK_ID_22_WRITELOCK?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;
	while ((GCLK_REGS->GCLK_PCHCTRL[${GCLK_ID_22_INDEX}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
	</#if>
	
    /****************** DPLL Initialization  *********************************/

    /*
     * Selection of Lock Bypass , Lock Time ,WakeUp Fast , Filter ,Run Standby
     * and Low Power Enable
     */
    <@compress single_line=true>OSCCTRL_REGS->OSCCTRL_DPLLCTRLB = OSCCTRL_DPLLCTRLB_FILTER(${CONFIG_CLOCK_DPLL_FILTER}) |
                                                                   OSCCTRL_DPLLCTRLB_LTIME(${CONFIG_CLOCK_DPLL_LOCK_TIME})|
																   OSCCTRL_DPLLCTRLB_REFCLK(${CONFIG_CLOCK_DPLL_REF_CLOCK}) 
                                                                   ${CONFIG_CLOCK_DPLL_LOCK_BYPASS?then('| OSCCTRL_DPLLCTRLB_LBYPASS_Msk', ' ')}
                                                                   ${CONFIG_CLOCK_DPLL_WAKEUP_FAST?then('| OSCCTRL_DPLLCTRLB_WUF_Msk', ' ')}
                                                                   ${CONFIG_CLOCK_DPLL_LOWPOWER_ENABLE?then('| OSCCTRL_DPLLCTRLB_LPEN_Msk', ' ')}
																   ${(CONFIG_CLOCK_DPLL_REF_CLOCK == "1")?then('| OSCCTRL_DPLLCTRLB_DIV(${CONFIG_CLOCK_DPLL_DIVIDER})', ' ')};</@compress>


    /* Selection of the Integer and Fractional part of the LDR ratio */
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

// *****************************************************************************
/* Function:
    void CLOCK_Initialize (void);

  Summary:
    Initializes all the modules related to the system clock.

  Description:
    This function initializes the clock as defined by the MHC and Clock Manager
    selections. The function will configure the NVM Flash Wait states based on
    the configured CPU operational frequency. It will then configure the
    oscillators.

    For each of the clock sources (External Oscillator, Digital Phase Locked
    Loop, Internal 48MHz Oscillator, External 32KHz oscillator and the Internal
    32KHz oscillator) enabled in MHC, the function will configure the clock
    settings and will then wait till the clock is ready. In case of DPLL, the
    function will wait till a lock is obtained.

    The function will then configure the Generic clock generators based on MHC
    configurations. If a Generic Clock is enabled in MHC, this will be enabled
    in the CLOCK_Initialize() function. The function will apply the CPU clock
    divider and will wait for the Main Clock module to get ready. If the Main
    Clock to the Peripheral APB and AHB interfaces was enabled in MHC, these
    will be enabled in the CLOCK_Initialize() function. If the Peripheral Clock
    Channels and mclk clocks were enabled in MHC, these will be enabled in the
    CLOCK_Initialize() function.

    The peripheral AHB and APB main clock and peripheral channel clocks will be
    enabled when the peripheral specific initialize functions are called. This
    will override the setting in MHC. The Generic Clock Generator source for
    desired peripheral channel must be configured in MHC.

   Remarks:
    Refer plib_clock.h file for more information.
*/
void CLOCK_Initialize (void)
{
    /* NVM Wait States */
    NVMCTRL_REGS->NVMCTRL_CTRLB |= NVMCTRL_CTRLB_RWS(NVMCTRL_CTRLB_RWS_SINGLE_Val);

    /* Function to Initialize the Oscillators */
    OSCCTRL_Initialize();

    /* Function to Initialize the 32KHz Oscillators */
    OSC32KCTRL_Initialize();
	
	/* Function to Initialize DPLL */
	<#if CONFIG_CLOCK_DPLL_ENABLE = true >
	<#if CONFIG_CLOCK_DPLL_REF_CLOCK != "2">
	OSCCTRL_DPLLInitialize();
	</#if>
	</#if>
	
    /* Software reset the module to ensure it is re-initialized correctly */
    GCLK_REGS->GCLK_CTRLA = GCLK_CTRLA_SWRST_Msk;

    while ((GCLK_REGS->GCLK_CTRLA & GCLK_CTRLA_SWRST_Msk) == GCLK_CTRLA_SWRST_Msk)
    {
        /* Wait for reset to complete */
    }

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
				<#assign GCLK_DPLL = "GCLK_ID_22_GENSEL">
    /* GCLK Generator ${i} Initialization */
    <@compress single_line=true>GCLK_REGS->GCLK_GENCTRL[${i}] = GCLK_GENCTRL_DIV(${.vars[GCLK_DIVISONVALUE]})
                                                               | GCLK_GENCTRL_SRC(${.vars[GCLK_SRC]})
                                                               ${(.vars[GCLK_DIVISONSELECTION] == "DIV2")?then('| GCLK_GENCTRL_DIVSEL_Msk' , ' ')}
                                                               ${(.vars[GCLK_IMPROVE_DUTYCYCLE])?then('| GCLK_GENCTRL_IDC_Msk', ' ')}
                                                               ${(.vars[GCLK_RUNSTDBY])?then('| GCLK_GENCTRL_RUNSTDBY_Msk', ' ')}
															   ${(.vars[GCLK_OUTPUTENABLE])?then('| GCLK_GENCTRL_OE_Msk', ' ')}
															   ${((.vars[GCLK_OUTPUTOFFVALUE] == "HIGH"))?then('| GCLK_GENCTRL_OOV_Msk', ' ')}
                                                               | GCLK_GENCTRL_GENEN_Msk;</@compress>

    while((GCLK_REGS->GCLK_SYNCBUSY & GCLK_SYNCBUSY_GENCTRL${i}_Msk) == GCLK_SYNCBUSY_GENCTRL${i}_Msk)
    {
        /* wait for the Generator ${i} synchronization */
    }
	
	<#if CONFIG_CLOCK_DPLL_REF_CLOCK == "2" && .vars[GCLK_DPLL] == ("0x" + i?string)>
	OSCCTRL_DPLLInitialize();
	</#if>
	
            </#if>
        </#if>
</#list>

    /* selection of the CPU clock Division */
    MCLK_REGS->MCLK_CPUDIV = MCLK_CPUDIV_CPUDIV(${CONF_CPU_CLOCK_DIVIDER});

    while((MCLK_REGS->MCLK_INTFLAG & MCLK_INTFLAG_CKRDY_Msk) != MCLK_INTFLAG_CKRDY_Msk)
    {
        /* Wait for the Main Clock to be Ready */
    }
	
<#list 0..GCLK_MAX_ID as i>
    <#assign GCLK_ID_CHEN = "GCLK_ID_" + i + "_CHEN">
    <#assign GCLK_ID_INDEX = "GCLK_ID_" + i + "_INDEX">
    <#assign GCLK_ID_NAME = "GCLK_ID_" + i + "_NAME">
    <#assign GCLK_ID_GENSEL = "GCLK_ID_" + i + "_GENSEL">
    <#assign GCLK_ID_WRITELOCK = "GCLK_ID_" + i + "_WRITELOCK">
        <#if .vars[GCLK_ID_CHEN]?has_content>
            <#if (.vars[GCLK_ID_CHEN] != false)>
	<#if CONFIG_CLOCK_DPLL_REF_CLOCK == "2" && i == 22>
	<#else>
	/* Selection of the Generator and write Lock for ${.vars[GCLK_ID_NAME]} */
    GCLK_REGS->GCLK_PCHCTRL[${.vars[GCLK_ID_INDEX]}] = GCLK_PCHCTRL_GEN(${.vars[GCLK_ID_GENSEL]})${.vars[GCLK_ID_WRITELOCK]?then(' | GCLK_PCHCTRL_WRTLOCK_Msk', ' ')} | GCLK_PCHCTRL_CHEN_Msk;

    while ((GCLK_REGS->GCLK_PCHCTRL[${.vars[GCLK_ID_INDEX]}] & GCLK_PCHCTRL_CHEN_Msk) != GCLK_PCHCTRL_CHEN_Msk)
    {
        /* Wait for synchronization */
    }
	</#if>
            </#if>
        </#if>
</#list>

	OSC32KCTRL_REGS->OSC32KCTRL_RTCCTRL = OSC32KCTRL_RTCCTRL_RTCSEL(${CONFIG_CLOCK_RTC_SRC});
	
    /* Configure the AHB Bridge Clocks */
    MCLK_REGS->MCLK_AHBMASK = MCLK_AHB_CLOCK_INITIAL_VALUE;

    /* Configure the APBA Bridge Clocks */
    MCLK_REGS->MCLK_APBAMASK = MCLK_APBA_CLOCK_INITIAL_VALUE;

    /* Configure the APBB Bridge Clocks */
    MCLK_REGS->MCLK_APBBMASK = MCLK_APBB_CLOCK_INITIAL_VALUE;

    /* Configure the APBC Bridge Clocks */
    MCLK_REGS->MCLK_APBCMASK = MCLK_APBC_CLOCK_INITIAL_VALUE;

    /* Configure the APBD Bridge Clocks */
    MCLK_REGS->MCLK_APBDMASK = MCLK_APBD_CLOCK_INITIAL_VALUE;
}



<#if CONFIG_CLOCK_XOSC_ENABLE = true>

// *****************************************************************************
/* Function:
    void OSCCTRL_XOSCEnable (bool enable);

  Summary:
    Enables and disables the External Oscillator.

  Description:
    This function enables or disables the external oscillator. The application
    may need to disable the oscillator to reduce power consumption.

    After enabling the external oscillator, the OSCCTRL_XOSCIsReady() function
    must be called to check if the oscillator is ready.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSCCTRL_XOSCEnable( bool enable )
{
    if(enable)
    {
        /* Enabling the XOSC */
        OSCCTRL_REGS->OSCCTRL_XOSCCTRL |= 1 << OSCCTRL_XOSCCTRL_ENABLE_Pos;
    }
    else
    {
        /* Disabling the XOSC */
        OSCCTRL_REGS->OSCCTRL_XOSCCTRL &= ~(1 << OSCCTRL_XOSCCTRL_ENABLE_Pos);
    }
}

// *****************************************************************************
/* Function:
    bool OSCCTRL_XOSCIsReady ( void );

  Summary:
    Indicates readiness of the external oscillator.

  Description:
    This function returns true if the external oscillator is ready to be used.
    Once enabled, the oscillator will need a certain amount of time to stabilize
    on the correct frequency.  The oscillator output during this stabilization
    is masked. The function returns true once the external clock or crystal
    oscillator is stable and ready to be used as clock source.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSCCTRL_XOSCIsReady( void )
{
    bool xoscReadyStatus = false;

    /* Checking for the XOSC Ready state */
    if((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCRDY_Msk) == OSCCTRL_STATUS_XOSCRDY_Msk)
    {
        xoscReadyStatus = true;
    }

    return xoscReadyStatus;
}
<#if CONFIG_CLOCK_XOSC_CFDEN = true >

// *****************************************************************************
/* Function:
    bool OSCCTRL_XOSCFailureIsActive( void );

  Summary:
    Indicates the XOSC failure status.

  Description:
    This function returns true if a failure is currently being detected on the
    external oscillator.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSCCTRL_XOSCFailureIsActive( void )
{
    bool failureActiveStatus = false;

    /* Checking for the XOSC Failure Detection */
    if((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCFAIL_Msk) == OSCCTRL_STATUS_XOSCFAIL_Msk)
    {
        failureActiveStatus = true;
    }

    return failureActiveStatus;
}

// *****************************************************************************
/* Function:
    bool OSCCTRL_XOSCSafeClockIsActive( void );

  Summary:
    Indicates the XOSC Clock is replaced by the safe clock

  Description:
    This function returns true if the Clock Failure detection system has
    detected a failure and the system has now switched to the safe clock.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSCCTRL_XOSCSafeClockIsActive( void )
{
    bool safeClockActiveStatus = false;

    /* Checking for the XOSC Switching to provide a safe Clock */
    if((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCCKSW_Msk) == OSCCTRL_STATUS_XOSCCKSW_Msk)
    {
        safeClockActiveStatus = true;
    }

    return safeClockActiveStatus;
}

// *****************************************************************************
/* Function:
    void OSCCTRL_XOSCMainClockRevert( void );

  Summary:
    Switches the system back to the external oscillator.

  Description:
    This function will switch the system clock from the safe clock to the
    external oscillator. This function should be called when the application is
    able to verify that the external oscillator is functional.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSCCTRL_XOSCMainClockRevert( void )
{
    /* Selection of the Switch Back option */
    OSCCTRL_REGS->OSCCTRL_XOSCCTRL |= OSCCTRL_XOSCCTRL_SWBEN_Msk ;
}

</#if>

</#if>
<#if CONFIG_CLOCK_OSC48M_ENABLE = true>
// *****************************************************************************
/* Function:
    void OSCCTRL_OSC48MEnable( bool enable );

  Summary:
    Enables and disables the Internal 48MHz Oscillator.

  Description:
    This function enables or disables the Internal 48MHz oscillator.This function
    could be called to disable the oscillator to save power.

    After enabling the oscillator, the OSCCTRL_OSC48MIsReady() function must
    called to call to check if the oscillator has stabilized.

   Remarks:
    Refer plib_clock.h file for more information.
*/
void OSCCTRL_OSC48MEnable( bool enable )
{
    if(enable)
    {
        /* Enabling the OSC48M */
        OSCCTRL_REGS->OSCCTRL_OSC48MCTRL |= 1 << OSCCTRL_OSC48MCTRL_ENABLE_Pos;
    }
    else
    {
        /* Disabling the OSC48M */
        OSCCTRL_REGS->OSCCTRL_OSC48MCTRL &= ~(1 << OSCCTRL_OSC48MCTRL_ENABLE_Pos);
    }
}

// *****************************************************************************
/* Function:
    bool OSCCTRL_OSC48MIsReady( void );

  Summary:
    Indicates readiness of the internal 48MHz oscillator.

  Description:
    This function returns true if the internal 48MHz oscillator is ready to be
    used.  Once enabled, the oscillator will need a certain amount of time to
    stabilize on the correct frequency.  The oscillator output during this
    stabilization is masked. The function returns true once the internal 48MHz
    oscillator is stable and ready to be used as clock source.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSCCTRL_OSC48MIsReady( void )
{
    bool osc48mReadyStatus = false;

    /* Checking for the OSC48M Ready state */
    if((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_OSC48MRDY_Msk) == OSCCTRL_STATUS_OSC48MRDY_Msk)
    {
        osc48mReadyStatus = true;
    }

    return osc48mReadyStatus;
}

</#if>
<#if CONFIG_CLOCK_DPLL_ENABLE = true >

// *****************************************************************************
/* Function:
    void OSCCTRL_DPLLEnable( bool enable );

  Summary:
    Enables or disables the Digital Phase Locked Loop (DPLL).

  Description:
    This function enables or disables the DPLL. This function could be called to
    disable the DPLL while entering the available sleep modes and re-enabling it
    exiting from the sleep mode.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSCCTRL_DPLLEnable( bool enable )
{
    if(enable)
    {
        /* Enabling the DPLL  */
        OSCCTRL_REGS->OSCCTRL_DPLLCTRLA |= 1 << OSCCTRL_DPLLCTRLA_ENABLE_Pos;
    }
    else
    {
        /* Disabling the DPLL  */
        OSCCTRL_REGS->OSCCTRL_DPLLCTRLA &= ~(1 << OSCCTRL_DPLLCTRLA_ENABLE_Pos);
    }
}

// *****************************************************************************
/* Function:
    bool OSCCTRL_DPLLIsLocked( void );

  Summary:
    Returns the lock status of the DPLL.

  Description:
    This function returns the lock status of the DPLL. When locked, the DPLL
    output is stable.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSCCTRL_DPLLIsLocked( void )
{
    bool dpllLockedStatus = false;

    /* Checking for the DPLL Lock Status */
    if((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_DPLLLCKR_Msk) == OSCCTRL_STATUS_DPLLLCKR_Msk)
    {
        dpllLockedStatus = true;
    }

    return dpllLockedStatus;
}

</#if>
<#if XOSC_INTERRUPT_MODE = true || DPLL_INTERRUPT_MODE = true >

// *****************************************************************************
/* Function:
    void OSCCTRL_CallbackRegister (OSCCTRL_CALLBACK callback, uintptr_t context);

  Summary:
    Register the function to be called when an External Oscillator or DPLL event
    is generated.

  Description:
    This function registers the callback function to be called when the External
    Oscillator has failed or when the DPLL has lost lock or when the DPLL has
    achieved lock. The event type is passed into the callback function when the
    function is called.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSCCTRL_CallbackRegister(OSCCTRL_CALLBACK callback, uintptr_t context)
{
    oscctrlObj.callback = callback;

    oscctrlObj.context = context;

<#if XOSC_INTERRUPT_MODE = true >
    /* Enabling the Clock Fail Interrupt  */
    OSCCTRL_REGS->OSCCTRL_INTENSET = OSCCTRL_INTENSET_XOSCFAIL_Msk;

    </#if>
    <#if DPLL_INTERRUPT_MODE = true >
    /* Enabling the DPLL Lock Fall and Rise Edge Interrupts */
    OSCCTRL_REGS->OSCCTRL_INTENSET = OSCCTRL_INTENSET_DPLLLCKF_Msk | OSCCTRL_INTENSET_DPLLLCKR_Msk ;

</#if>
}

// *****************************************************************************
/* Function:
    void OSCCTRL_Handler(void);

  Summary:
    Handler that handles the XOSC and DPLL Interrupts.

  Description:
    This Function is called from the handler to handle the XOSC Failure and DPLL
    lock based on the Interrupts.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSCCTRL_Handler(void)
{
    <#if XOSC_INTERRUPT_MODE = true >
    /* Checking for the Clock Fail status */
    if ((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_XOSCFAIL_Msk) == OSCCTRL_STATUS_XOSCFAIL_Msk)
    {
        if (oscctrlObj.callback != NULL)
        {
            oscctrlObj.callback(OSCCTRL_EVENT_CLOCK_FAIL, oscctrlObj.context);
        }

        /* Clearing the XOSC Fail Interrupt Flag */
        OSCCTRL_REGS->OSCCTRL_INTFLAG = OSCCTRL_INTFLAG_XOSCFAIL_Msk;
    }

    </#if>
    <#if DPLL_INTERRUPT_MODE = true >
    /* Checking for the DPLL Lock Fail status */
    if ((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_DPLLLCKF_Msk) == OSCCTRL_STATUS_DPLLLCKF_Msk)
    {
        if (oscctrlObj.callback != NULL)
        {
            oscctrlObj.callback(OSCCTRL_EVENT_DPLL_LOCK_FAIL, oscctrlObj.context);
        }

        /* Clearing the DPLL Lock Fail Interrupt Flag */
        OSCCTRL_REGS->OSCCTRL_INTFLAG = OSCCTRL_INTFLAG_DPLLLCKF_Msk;
    }

    /* Checking for the DPLL Locked status */
    if ((OSCCTRL_REGS->OSCCTRL_STATUS & OSCCTRL_STATUS_DPLLLCKR_Msk) == OSCCTRL_STATUS_DPLLLCKR_Msk)
    {
        if (oscctrlObj.callback != NULL)
        {
            oscctrlObj.callback(OSCCTRL_EVENT_PLL_LOCKED, oscctrlObj.context);
        }

        /* Clearing the DPLL Locked Interrupt Flag */
        OSCCTRL_REGS->OSCCTRL_INTFLAG = OSCCTRL_INTFLAG_DPLLLCKR_Msk;
    }
    </#if>
}

</#if>

<#if CONF_CLOCK_XOSC32K_ENABLE = true >

// *****************************************************************************
/* Function:
    void OSC32KCTRL_XOSC32KEnable( bool enable );

  Summary:
    Enables and disables the External 32KHz Oscillator.

  Description:
    This function enables or disables the external 32KHz oscillator. This
    function could be called to disable the oscillator to save power.

    After enabling the oscillator, the OSC32KCTRL_XOSC32KIsReady() function must
    be called to check if the oscillator has stabilized.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSC32KCTRL_XOSC32KEnable( bool enable )
{
    if(enable)
    {
        /* Enabling the XOSC32K */
        OSC32KCTRL_REGS->OSC32KCTRL_XOSC32K |= 1 << OSC32KCTRL_XOSC32K_ENABLE_Pos;
    }
    else
    {
        /* Disabling the XOSC32K */
        OSC32KCTRL_REGS->OSC32KCTRL_XOSC32K &= ~(1 << OSC32KCTRL_XOSC32K_ENABLE_Pos);
    }
}

// *****************************************************************************
/* Function:
    bool OSC32KCTRL_XOSC32KIsReady( void );

  Summary:
    Indicates readiness of the external 32KHz oscillator.

  Description:
    This function returns true if the external 32KHz oscillator is ready to be
    used.  Once enabled, the oscillator will need a certain amount of time to
    stabilize on the correct frequency.  The oscillator output during this
    stabilization is masked. The function returns true once the external clock
    or crystal oscillator is stable and ready to be used as clock source.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSC32KCTRL_XOSC32KIsReady( void )
{
    bool xosc32kReadyStatus = false;

    /* Checking for the XOSC32K Ready state */
    if((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_XOSC32KRDY_Msk) == OSC32KCTRL_STATUS_XOSC32KRDY_Msk)
    {
        xosc32kReadyStatus = true;
    }

    return xosc32kReadyStatus;
}
<#if XOSC32K_CFDEN = true >

// *****************************************************************************
/* Function:
    bool OSCCTRL_XOSC32KFailureIsActive( void );

  Summary:
    Indicates the XOSC32K failure status.

  Description:
    This function returns true if a failure is currently being detected on the
    external 32K oscillator.
   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSC32KCTRL_XOSC32KFailureIsActive( void )
{
    bool failureActiveStatus = false;

    /* Checking for the XOSC32K Clock Failure Detection */
    if((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_CLKFAIL_Msk) == OSC32KCTRL_STATUS_CLKFAIL_Msk)
    {
        failureActiveStatus = true;
    }

    return failureActiveStatus;
}

// *****************************************************************************
/* Function:
    bool OSCCTRL_XOSC32KSafeClockIsActive( void );

  Summary:
    Indicates the XOSC32K Clock is replaced by the safe clock

  Description:
    This function returns true if the Clock Failure detection system has
    detected a failure and the system has now switched to the safe clock.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSC32KCTRL_XOSC32KSafeClockIsActive( void )
{
    bool safeClockActiveStatus = false;

    if((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSCCTRL_STATUS_XOSCCKSW_Msk) == OSCCTRL_STATUS_XOSCCKSW_Msk)
    {
        /* Checking for the XOSC32K Switch and provides a safe Clock */
        safeClockActiveStatus = true;
    }

    return safeClockActiveStatus;
}

// *****************************************************************************
/* Function:
    void OSCCTRL_XOSC32KMainClockRevert( void );

  Summary:
    Switches the system back to the external oscillator.

  Description:
    This function will switch the system clock from the safe clock to the
    external oscillator. This function should be called when the application is
    able to verify that the external oscillator is functional.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSC32KCTRL_XOSC32KMainClockRevert( void )
{
    /* Selection of the Switch Back option */
    OSC32KCTRL_REGS->OSC32KCTRL_CFDCTRL |= OSC32KCTRL_CFDCTRL_SWBACK_Msk ;
}

</#if>
</#if>
<#if CONF_CLOCK_OSC32K_ENABLE = true >

// *****************************************************************************
/* Function:
    void OSC32KCTRL_OSC32KEnable( bool enable );

  Summary:
    Enables and disables the Internal 32KHz Oscillator.

  Description:
    This function enables or disables the Internal 32KHz oscillator. This function
    could be called to disable the oscillator to reduce power.

    After enabling the oscillator, the OSC32KCTRL_OSC32KIsReady() function must
    called to call to check if the oscillator has stabilized.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSC32KCTRL_OSC32KEnable( bool enable )
{
    if(enable)
    {
        /* Enabling the OSC32K*/
        OSC32KCTRL_REGS->OSC32KCTRL_OSC32K |= 1 << OSC32KCTRL_OSC32K_ENABLE_Msk;
    }
    else
    {
        /* Disabling the OSC32K */
        OSC32KCTRL_REGS->OSC32KCTRL_OSC32K &= ~(1 << OSC32KCTRL_OSC32K_ENABLE_Msk);
    }
}

// *****************************************************************************
/* Function:
    bool OSC32KCTRL_OSC32KIsReady( void );

  Summary:
    Indicates readiness of the internal 32KHz oscillator.

  Description:
    This function returns true if the internal 32KHz oscillator is ready to be
    used. Once enabled, the oscillator will need a certain amount of time to
    stabilize on the correct frequency.  The oscillator output during this
    stabilization is masked. The function returns true once the internal 32KHz
    oscillator is stable and ready to be used as clock source.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool OSC32KCTRL_OSC32KIsReady( void )
{
    bool osc32kReadyStatus = false;

    /* Waiting for the XOSC32K Ready state */
    if((OSC32KCTRL_REGS->OSC32KCTRL_STATUS & OSC32KCTRL_STATUS_OSC32KRDY_Msk) == OSC32KCTRL_STATUS_OSC32KRDY_Msk)
    {

        osc32kReadyStatus = true;
    }

    return osc32kReadyStatus;
}

</#if>
<#if XOSC32K_INTERRUPT_MODE = true >

// *****************************************************************************
/* Function:
    void OSC32KCTRL_CallbackRegister (OSC32KCTRL_CFD_CALLBACK callback,
                                                    uintptr_t context);

  Summary:
    Register the function to be called when the 32KHz External Oscillator has
    failed.

  Description:
    This function register the function to be called when the 32KHz External
    Oscillator has failed.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void OSC32KCTRL_CallbackRegister (OSC32KCTRL_CFD_CALLBACK callback, uintptr_t context)
{
    osc32kctrlObj.callback = callback;

    osc32kctrlObj.context = context;

   /* Enabling the Clock Failure Interrupt */
    OSC32KCTRL_REGS->OSC32KCTRL_INTENSET = OSC32KCTRL_INTENSET_CLKFAIL_Msk;

}

// *****************************************************************************
/* Function:
    void OSC32KCTRL_Handler(void);

  Summary:
    Handler that handles the XOSC32K Interrupts.

  Description:
    This Function is called from the handler to handle the XOSC32K Failure
    Interrupts.

   Remarks:
    Refer plib_clock.h file for more information.
*/

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

// *****************************************************************************
// *****************************************************************************
// Section: GCLK Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void GCLK_GeneratorEnable(GCLK_GENERATOR gclk, bool enable);

  Summary:
    Enables or disables the GCLK Generator.

  Description:
    This function will enable or disable the selected generic clock generator.
    The generator to be modified is specified by gclk parameter. A generator may
    be disabled to save power while entering a low power mode and enabled again
    when peripheral operation needs to be resumed.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void GCLK_GeneratorEnable(GCLK_GENERATOR gclk, bool enable)
{
    if(enable)
    {
         GCLK_REGS->GCLK_GENCTRL[gclk] |= 1 << GCLK_GENCTRL_GENEN_Pos;
    }
    else
    {
         GCLK_REGS->GCLK_GENCTRL[gclk] &= ~(1 << GCLK_GENCTRL_GENEN_Pos);
    }
}

// *****************************************************************************
/* Function:
    void GCLK_PeripheralChannelEnable (GCLK_PERIPHERAL_CHANNEL peripheralChannel,
                                       bool enable);

  Summary:
    Enables or disables the Peripheral Clock Channel.

  Description:
    This function will enable or disable the specified peripheral channel.
    Enabling the peripheral clock channel will enable the core clock that is
    required for peripheral to function. The peripheral clock channel may be
    disable to stop the clock to a peripheral to save power.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void GCLK_PeripheralChannelEnable (GCLK_PERIPHERAL_CHANNEL peripheralChannel, bool enable)
{
    if(enable)
    {
        /* Enabling the peripheral Channel */
        GCLK_REGS->GCLK_PCHCTRL[peripheralChannel] |= 1 << GCLK_PCHCTRL_CHEN_Pos;
    }
    else
    {
        GCLK_REGS->GCLK_PCHCTRL[peripheralChannel] &= ~(1 << GCLK_PCHCTRL_CHEN_Pos);
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: MCLK IMPLEMENTATION
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void MCLK_APBClockEnable ( MCLK_APB_CLOCK peripheral, bool enable );

  Summary:
    Enables or disables APB Clock.

  Description:
    This function will enable or disable the APB clock for the selected
    peripheral given by the peripheral parameter. Enabling the peripheral APB
    clock makes the peripheral register accessible.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void MCLK_APBClockEnable ( MCLK_APB_CLOCK peripheral, bool enable )
{
    uint32_t bridgeMask = peripheral/32;

    uint32_t mclkClockPos = peripheral%32;

    /* Base Address of the APB Bridge */
    volatile uint32_t *apbBridgeAddr = (volatile uint32_t *)0x40000814;

    apbBridgeAddr = apbBridgeAddr + bridgeMask;

    if(enable)
    {
        *apbBridgeAddr |= 1 << mclkClockPos;
    }
    else
    {
        *apbBridgeAddr &= ~(1 << mclkClockPos);
    }

}

// *****************************************************************************
/* Function:
    void MCLK_AHBClockEnable ( MCLK_AHB_CLOCK ahbClock, bool enable );

  Summary:
    Enables or disables AHB Clock.

  Description:
    This function will enable or disable the AHB clock for the selected
    peripheral. Peripherals such CAN and DMAC use the AHB to access other memory
    regions. Enabling the AHB clock enables this access.

   Remarks:
    Refer plib_clock.h file for more information.
*/

void MCLK_AHBClockEnable ( MCLK_AHB_CLOCK ahbClock, bool enable )
{
    if(enable)
    {
        MCLK_REGS->MCLK_AHBMASK |= ahbClock;
    }
    else
    {
        MCLK_REGS->MCLK_AHBMASK &= ~(ahbClock);
    }
}

// *****************************************************************************
/* Function:
    bool MCLK_ClockIsReady ( void );

  Summary:
    Returns the status of the Main Clock (MCLK).

  Description:
    This function returns true if the Main clock is ready. If the CPU clock
    divide values are changed, there is some delay involved till the new setting
    become active. This function can be called to check the readiness of the
    MCLK in such a case.

   Remarks:
    Refer plib_clock.h file for more information.
*/

bool MCLK_ClockIsReady ( void )
{
    bool clockReadyStatus = false;

    /* Check for the Clock Ready */
    if((MCLK_REGS->MCLK_INTFLAG & MCLK_INTFLAG_CKRDY_Msk) == MCLK_INTFLAG_CKRDY_Msk)
    {
        clockReadyStatus = true;
    }

    return clockReadyStatus;
}
