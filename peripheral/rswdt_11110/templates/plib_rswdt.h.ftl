/*******************************************************************************
  Interface definition of RSWDT PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rswdt.h

  Summary:
    Interface definition of the Watch Dog Timer Plib (RSWDT).

  Description:
    This file defines the interface for the RSWDT Plib.
    It allows user to setup timeout duration and restart watch dog timer.
*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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

#ifndef RSWDT${rswdtIndex?string}_H    // Guards against multiple inclusion
#define RSWDT${rswdtIndex?string}_H

#include "${__PROCESSOR?lower_case}.h"
#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus // Provide C++ Compatibility
 extern "C" {
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

<#if rswdtinterruptMode == true>
	<#lt>typedef void (*RSWDT_CALLBACK)(uintptr_t context);
</#if>

<#if rswdtinterruptMode == true>
	<#lt>typedef struct
	<#lt>{
	<#lt>	RSWDT_CALLBACK          callback; 
	<#lt>	uintptr_t               context;
	<#lt>} RSWDT_OBJECT ;
	
	<#lt>RSWDT_OBJECT rswdt;
</#if>
/***************************** RSWDT API *******************************/
void RSWDT${rswdtIndex?string}_Initialize( void );
void RSWDT${rswdtIndex?string}_Clear( void );
<#if rswdtinterruptMode == true>
	<#lt>void RSWDT${rswdtIndex?string}_CallbackRegister( RSWDT_CALLBACK callback, uintptr_t context );
</#if>	

#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif 
