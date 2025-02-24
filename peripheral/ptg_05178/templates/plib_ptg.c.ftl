<#assign WdtTimeoutOptions=["DISABLED","8","16","32","64","128","256","512"]>
<#assign InputTriggerMode=["MODE_0","MODE_1","MODE_2","MODE_3"]>
<#assign ClockPrescalarOptions = []>
<#list 1..32 as i>
    <#assign ClockPrescalarOptions = ClockPrescalarOptions + [i]>
</#list>
<#assign MaxTrigger = 3>
/*******************************************************************************
  ${moduleNameUpperCase?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleNameUpperCase?lower_case}.c
 
  Summary:
    ${moduleNameUpperCase?lower_case} PLIB Source File
 
  Description:
    None
 
*******************************************************************************/
 
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

// Section: Included Files
#include <stdlib.h>
#include <stdbool.h>
#include "device.h"
#include "plib_${moduleNameLowerCase}.h"
<#if core.CoreSysIntFile == true & isPtgInterruptEnabled == true>
#include "interrupts.h"
</#if>

//Section: Data Type Definitions

<#if isPtgInterruptEnabled == true>
volatile static PTG_EVENTS_CALLBACK_OBJECT trigger0Obj;
volatile static PTG_EVENTS_CALLBACK_OBJECT trigger1Obj;
volatile static PTG_EVENTS_CALLBACK_OBJECT trigger2Obj;
volatile static PTG_EVENTS_CALLBACK_OBJECT trigger3Obj;
volatile static PTG_EVENTS_CALLBACK_OBJECT triggerWdtObj;
</#if>

//Section: Macro Definitions

<#list WdtTimeoutOptions as options>
#define PTGCON_PTGWDT_TIMEOUT_${options}      ((uint32_t)(_PTGCON_PTGWDT_MASK & ((uint32_t)(${options_index}) <<_PTGCON_PTGWDT_POSITION))) 
</#list>

<#list InputTriggerMode as options>
#define PTGCON_PTGITM_${options}      ((uint32_t)(_PTGCON_PTGITM_MASK & ((uint32_t)(${options_index}) <<_PTGCON_PTGITM_POSITION))) 
</#list>

<#list ClockPrescalarOptions as options>
#define PTGCON_PTGDIV_DIVIDE_BY_${options}    ((uint32_t)(_PTGCON_PTGDIV_MASK & ((uint32_t)(${options_index}) <<_PTGCON_PTGDIV_POSITION)))
</#list>

// Section: PTG PLIB Routines
void ${moduleNameUpperCase}_Initialize (void)
{
	PTGCON = (PTGCON_PTGWDT_TIMEOUT_${WdtTimeoutOptions[PTG_CON__PTGWDT?number]}
			|PTGCON_PTGITM_${InputTriggerMode[PTG_CON__PTGITM?number]}
			|PTGCON_PTGDIV_DIVIDE_BY_${ClockPrescalarOptions[PTG_CON__PTGDIV?number]});
			
	PTGBTE   = 0x${PTGBTE}UL;
	PTGHOLD  = 0x${PTGHOLD}UL;
	PTGT0LIM = 0x${PTGT0LIM}UL;
	PTGT1LIM = 0x${PTGT1LIM}UL;
	PTGSDLIM = 0x${PTGSDLIM}UL;
    PTGC0LIM = 0x${PTGC0LIM}UL;
	PTGC1LIM = 0x${PTGC1LIM}UL;
	PTGADJ   = 0x${PTGADJ}UL;
	PTGQPTR  = 0x${PTGQPTR}UL;
	

  /** 
   Step Commands 
  */

    <#list 0..maxStepSequence as j >
	<#if (.vars["STEP"+j+"_COMMAND"]??) && (.vars["STEP"+j+"_OPTIONS"]??) &&(.vars["STEP"+j+"_OPTION_VALUE"]??)>
	<#lt> PTG_STEP${j} = ${.vars["STEP"+j+"_COMMAND"]} | 0x${.vars["STEP" + j+ "_OPTION_VALUE"]}U; //${.vars["STEP" + j + "_OPTIONS"]}
	</#if>
	</#list>

    <#if PTG0Interrupt == true>
	//Clear  interrupt flag  
    ${zeroInterruptFlagBit} = 0;
    //Enable  interrupt
    ${zeroInterruptEnableBit} = 1;
	</#if>
	<#if  PTG1Interrupt == true>
	//Clear  interrupt flag  
    ${oneInterruptFlagBit} = 0;
    //Enable  interrupt
    ${oneInterruptEnableBit} = 1;
	</#if>
	<#if  PTG2Interrupt == true>
	//Clear  interrupt flag  
    ${twoInterruptFlagBit} = 0;
    //Enable  interrupt
    ${twoInterruptEnableBit} = 1;
	</#if>
	<#if  PTG3Interrupt == true>
	//Clear  interrupt flag  
    ${threeInterruptFlagBit} = 0;
    //Enable  interrupt
    ${threeInterruptEnableBit} = 1;
	</#if>
	<#if PTGWDTInterrupt == true>
	//Clear  interrupt flag  
    ${wdtInterruptFlagBit} = 0;
    //Enable  interrupt
    ${wdtInterruptEnableBit} = 1;
	</#if>
	
}

void ${moduleNameUpperCase}_Deinitialize (void)
{
    ${moduleNameUpperCase}_Disable();
	<#if PTG0Interrupt == true>
	${zeroInterruptFlagBit} = 0;
	${zeroInterruptEnableBit} = 0;
	</#if>
	<#if  PTG1Interrupt == true>
	${oneInterruptFlagBit} = 0;
	${oneInterruptEnableBit} = 0;
	</#if>
	<#if  PTG2Interrupt == true>
	${twoInterruptFlagBit} = 0;
	${twoInterruptEnableBit} = 0;
	</#if>
	<#if  PTG3Interrupt == true>
	${threeInterruptFlagBit} = 0;
	${threeInterruptEnableBit} = 0;
	</#if>
	<#if PTGWDTInterrupt == true>
	${wdtInterruptFlagBit} = 0;
	${wdtInterruptEnableBit} = 0;
	</#if>
	
${regPorSet}
}

void ${moduleNameUpperCase}_Enable (void)
{
    ${moduleNameUpperCase}CONbits.ON = 1;
}

void ${moduleNameUpperCase}_StepSequenceStart (void)
{
    ${moduleNameUpperCase}CONbits.${moduleNameUpperCase}STRT = 1; 
}

void ${moduleNameUpperCase}_SoftwareTriggerSet (void)
{
    ${moduleNameUpperCase}CONbits.${moduleNameUpperCase}SWT = 1;    
}

void ${moduleNameUpperCase}_SoftwareTriggerClear (void)
{
    ${moduleNameUpperCase}CONbits.${moduleNameUpperCase}SWT = 0;    
}

bool ${moduleNameUpperCase}_WatchdogTimeoutStatusGet (void)
{
    return (bool)${moduleNameUpperCase}CONbits.${moduleNameUpperCase}WDTO;
}

void ${moduleNameUpperCase}_StepSequenceStop (void)
{
    ${moduleNameUpperCase}CONbits.${moduleNameUpperCase}STRT = 0;
}   

void ${moduleNameUpperCase}_Disable (void)
{
    ${moduleNameUpperCase}CONbits.ON = 0;
}

<#if isPtgInterruptEnabled == true>
void ${moduleNameUpperCase}_EventCallbackRegister(${moduleNameUpperCase}_EVENTS event, PTG_EVENTS_CALLBACK callback_fn, uintptr_t context)
{
    switch(event)
   {
	<#list 0..MaxTrigger as i>
	case TRIGGER${i}:
		trigger${i}Obj.callback_fn = callback_fn;
		trigger${i}Obj.context = context;
		break;
	</#list>
	
	case WATCHDOGTIMER:
		triggerWdtObj.callback_fn = callback_fn;
		triggerWdtObj.context = context;
		break;
	default:
		/* Nothing to process */
		break;
	}
}
</#if>
<#if PTG0Interrupt == true>
void __attribute__ ( ( used ) ) ${zeroIsrHandlerName}( void )

{
    if(trigger0Obj.callback_fn != NULL)
    {
        uintptr_t context = trigger0Obj.context;
		trigger0Obj.callback_fn(context);
    }
	${zeroInterruptFlagBit} = 0;
}
</#if>
<#if  PTG1Interrupt == true> 
void __attribute__ ( ( used ) ) ${oneIsrHandlerName}( void )

{
    if(trigger1Obj.callback_fn != NULL)
    {
        uintptr_t context = trigger1Obj.context;
		trigger1Obj.callback_fn(context);
    }
	${oneInterruptFlagBit} = 0;
}
</#if>
<#if  PTG2Interrupt == true>
void __attribute__ ( ( used ) ) ${twoIsrHandlerName}( void )

{
    if(trigger2Obj.callback_fn != NULL)
    {
        uintptr_t context = trigger2Obj.context;
		trigger2Obj.callback_fn(context);
    }
	${twoInterruptFlagBit} = 0;
}
</#if>
<#if  PTG3Interrupt == true>
void __attribute__ ( ( used ) ) ${threeIsrHandlerName}( void )

{
    if(trigger3Obj.callback_fn != NULL)
    {
        uintptr_t context = trigger3Obj.context;
		trigger3Obj.callback_fn(context);
    }
	${threeInterruptFlagBit} = 0;
}
</#if>
<#if PTGWDTInterrupt == true>
void __attribute__ ( ( used ) ) ${wdtIsrHandlerName}( void )

{
    if(triggerWdtObj.callback_fn != NULL)
    {
        uintptr_t context = triggerWdtObj.context;
		triggerWdtObj.callback_fn(context);
    }
	${wdtInterruptFlagBit} = 0;
}
</#if>

