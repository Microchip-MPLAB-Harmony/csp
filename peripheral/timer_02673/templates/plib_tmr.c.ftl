<#assign preScalarOptions = ["1_1","1_8","1_64","1_256"]>
<#assign clockSelectionOptions = ["STANDARD","EXTERNAL"]>

/*******************************************************************************
  TMR Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_tmr${TMR_INSTANCE_NUMBER}.c

  Summary
    TMR${TMR_INSTANCE_NUMBER} peripheral library source file.

  Description
    This file implements the interface to the TMR peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*/
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "stdbool.h"
#include "device.h"
#include "plib_tmr${TMR_INSTANCE_NUMBER}.h"
<#if core.CoreSysIntFile == true & TMR_INTERRUPT_MODE == true>
#include "interrupts.h"
</#if>

<#if TMR_INTERRUPT_MODE == true>
volatile static TIMER_OBJECT tmr${TMR_INSTANCE_NUMBER}Obj;
void T${TMR_INSTANCE_NUMBER}_InterruptHandler (void);
</#if>

// Section: Macro Definitions

#define TIMER_CLOCK_FREQUENCY          ${TIMER_CLOCK_FREQ}

//Timer Pre-Scalar options
<#list preScalarOptions as options>
#define T${TMR_INSTANCE_NUMBER}CON_TCKPS_${options}      ((uint32_t)(_T${TMR_INSTANCE_NUMBER}CON_TCKPS_MASK & ((uint32_t)(${options_index}) << _T${TMR_INSTANCE_NUMBER}CON_TCKPS_POSITION))) 
</#list>

//Clock selection options
<#list clockSelectionOptions as options>
#define T${TMR_INSTANCE_NUMBER}CON_SRC_SEL_${options}      ((uint32_t)(_T${TMR_INSTANCE_NUMBER}CON_TCS_MASK & ((uint32_t)(${options_index}) << _T${TMR_INSTANCE_NUMBER}CON_TCS_POSITION))) 
</#list>

void TMR${TMR_INSTANCE_NUMBER}_Initialize(void)
{
    /* Disable Timer */
    T${TMR_INSTANCE_NUMBER}CONbits.ON = 0;

	<#if TCON_SRC_SEL=="0" & TCON_PRE_SCALER =="0" & TCON_TSYNC =="0" & TCON_TWDIS =="0" & TCON_TGATE == "0">
	T${TMR_INSTANCE_NUMBER}CON = 0x0U;
	<#else>
    T${TMR_INSTANCE_NUMBER}CON = (T${TMR_INSTANCE_NUMBER}CON_TCKPS_${preScalarOptions[TCON_PRE_SCALER?number]}<#if TCON_TGATE == "1" & TCON_SRC_SEL == "0">
	        |_T${TMR_INSTANCE_NUMBER}CON_TGATE_MASK</#if>
			| T${TMR_INSTANCE_NUMBER}CON_SRC_SEL_${clockSelectionOptions[TCON_SRC_SEL?number]}<#if TCON_TSYNC == "1" & TCON_SRC_SEL=="1">
			|_T${TMR_INSTANCE_NUMBER}CON_TSYNC_MASK</#if><#if TCON_TWDIS == "1" & TCON_TSYNC == "0">
			|_T${TMR_INSTANCE_NUMBER}CON_TMWDIS_MASK</#if>);
	</#if>	
    /* Clear counter */
    TMR${TMR_INSTANCE_NUMBER} = 0x0U;

    /*Set period */
    PR${TMR_INSTANCE_NUMBER} = 0x${TIMER_PERIOD}U; /* Decimal Equivalent ${PERIOD_REG_COMMENT} */

    <#if TMR_INTERRUPT_MODE == true>
    /* Setup TMR1 Interrupt */
    TMR${TMR_INSTANCE_NUMBER}_InterruptEnable();  /* Enable interrupt on the way out */
    </#if>
}

void TMR${TMR_INSTANCE_NUMBER}_Deinitialize(void)
{
	/* Stopping the timer */
	TMR${TMR_INSTANCE_NUMBER}_Stop();
	
	/* Deinitializing the registers to POR values */
	T${TMR_INSTANCE_NUMBER}CON = ${TCON_REG_POR};
	TMR${TMR_INSTANCE_NUMBER}  = ${TMR_REG_POR};
	PR${TMR_INSTANCE_NUMBER}   = ${PR_REG_POR};
}
	
void TMR${TMR_INSTANCE_NUMBER}_Start (void)
{
    T${TMR_INSTANCE_NUMBER}CONbits.ON = 1;
}

void TMR${TMR_INSTANCE_NUMBER}_Stop (void)
{
    T${TMR_INSTANCE_NUMBER}CONbits.ON = 0;
}


void TMR${TMR_INSTANCE_NUMBER}_PeriodSet(uint32_t period)
{
    PR${TMR_INSTANCE_NUMBER} = period;
}


uint32_t TMR${TMR_INSTANCE_NUMBER}_PeriodGet(void)
{
    return PR${TMR_INSTANCE_NUMBER};
}


uint32_t TMR${TMR_INSTANCE_NUMBER}_CounterGet(void)
{
    return TMR${TMR_INSTANCE_NUMBER};
}

uint32_t TMR${TMR_INSTANCE_NUMBER}_FrequencyGet(void)
{
    return TIMER_CLOCK_FREQUENCY;
}

<#if TMR_INTERRUPT_MODE == true>
void __attribute__((used)) ${TMR_INTERRUPT_HANDLER} (void)
{
    uint32_t status = _T${TMR_INSTANCE_NUMBER}IF;
    _T${TMR_INSTANCE_NUMBER}IF = 0;

    if((tmr${TMR_INSTANCE_NUMBER}Obj.callback_fn != NULL))
    {
        uintptr_t context = tmr${TMR_INSTANCE_NUMBER}Obj.context;
        tmr${TMR_INSTANCE_NUMBER}Obj.callback_fn(status, context);
    }
}


void TMR${TMR_INSTANCE_NUMBER}_InterruptEnable(void)
{
    _T${TMR_INSTANCE_NUMBER}IE = 1;
}


void TMR${TMR_INSTANCE_NUMBER}_InterruptDisable(void)
{
     _T${TMR_INSTANCE_NUMBER}IE = 0;
}


void TMR${TMR_INSTANCE_NUMBER}_CallbackRegister( TMR_CALLBACK callback_fn, uintptr_t context )
{
    /* - Save callback_fn and context in local memory */
    tmr${TMR_INSTANCE_NUMBER}Obj.callback_fn = callback_fn;
    tmr${TMR_INSTANCE_NUMBER}Obj.context = context;
}
<#else>
bool TMR${TMR_INSTANCE_NUMBER}_PeriodHasExpired(void)
{
	bool status;
	status = (_T${TMR_INSTANCE_NUMBER}IF != 0U);
    _T${TMR_INSTANCE_NUMBER}IF = 0;
	
	return status;
}
</#if>
