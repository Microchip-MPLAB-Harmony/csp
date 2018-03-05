/*******************************************************************************
  Interface definition of SYSTICK PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_systick.h

  Summary:
    Interface definition of the System Timer Plib (SYSTICK).

  Description:
    This file defines the interface for the SYSTICK Plib.
*******************************************************************************/

/*******************************************************************************
Copyright (c) 2016 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/

#ifndef PLIB_SYSTICK_H    // Guards against multiple inclusion
#define PLIB_SYSTICK_H 

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus // Provide C++ Compatibility
	extern "C" {
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

<#if USE_SYSTICK_INTERRUPT == true>
	<#lt>typedef void (*SYSTICK_CALLBACK)(uintptr_t context);
</#if>

<#if USE_SYSTICK_INTERRUPT == true>
	<#lt>typedef struct
	<#lt>{
	<#lt>	SYSTICK_CALLBACK          callback; 
	<#lt>	uintptr_t               context;
	<#lt>} SYSTICK_OBJECT ;
	
	<#lt>SYSTICK_OBJECT systick;
</#if>
/***************************** SYSTICK API *******************************/
void SYSTICK_TimerInitialize ( void );
void SYSTICK_TimerStart ( void );
void SYSTICK_TimerStop ( void );
void SYSTICK_TimerPeriodSet ( uint32_t period );
uint32_t SYSTICK_TimerPeriodGet ( void );
uint32_t SYSTICK_TimerCounterGet ( void );
uint32_t SYSTICK_TimerFrequencyGet ( void );
<#if USE_SYSTICK_INTERRUPT == false>
	<#lt>bool SYSTICK_TimerExpired(void);
</#if>
<#if USE_SYSTICK_INTERRUPT == true>
	<#lt>void SYSTICK_TimerCallbackSet ( SYSTICK_CALLBACK callback, uintptr_t context );
</#if>	
#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif 
