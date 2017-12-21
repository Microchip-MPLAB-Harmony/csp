/*******************************************************************************
 Interface definition of EEFC PLIB.
 
 Company:
	Microchip Technology Inc.
	
 File Name:
	plib_EEFC.h
	
 Summary:
	Interface definition of EEFC Plib.
	
 Description:
	This file defines the interface for the EEFC Plib.
	It allows user to Program, Erase and lock the on-chip FLASH memory.
*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef _EEFC_H    // Guards against multiple inclusion
#define _EEFC_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/*  This section lists the other files that are included in this file.
*/
/* This section lists the other files that are included in this file.
*/

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
	extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

typedef enum
{
/* FLASH operation completed successfully */
EEFC_SUCCESS = 0x1,
/* FLASH operation lead to an error */
EEFC_ERROR = 0x2,
/*Flash region is locked*/
EEFC_LOCK_ERROR = 0x3,
/*Flash Encountered an ECC error*/
EEFC_ECC_ERROR = 0x4,
/*Flash Operation is not complete*/
EEFC_BUSY = 0x5
} EEFC_STATUS;

<#if eefcEnableInterrupt == true>
	<#lt>typedef struct
	<#lt>{
		<#lt>	EEFC_CALLBACK          callback;
		<#lt>	uintptr_t               context;
	<#lt>} EEFC_OBJECT ;

	<#lt>EEFC_OBJECT eefc;
	<#lt>typedef void (*EEFC_CALLBACK)(uintptr_t context);
</#if>

void EEFC_WriteQuadWord( uint32_t address, uint32_t* data );
void EEFC_WritePage( uint32_t address, uint32_t* data );
void EEFC_EraseRow( uint32_t address );
bool EEFC_IsBusy( void );
uint16_t EEFC_GetPageSize( void );
uint16_t EEFC_GetRowSize( void );
uint16_t EEFC_GetLockRegionSize( void );
EEFC_STATUS EEFC_StatusGet( void );
void EEFC_RegionLock(uint32_t address);
void EEFC_RegionUnlock(uint32_t address);
<#if eefcEnableInterrupt == true>
	<#lt>void EEFC_CallbackRegister( EEFC_CALLBACK callback, uintptr_t context );
</#if>

<#if eefcEnableInterrupt == true>
<#lt>void inline EEFC_OPR_Handler( void )
<#lt>{
	<#lt>	if(eefc.callback != NULL)
	<#lt>        {
		<#lt>            eefc.callback(eefc.context);
	<#lt>        }
<#lt>}
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END
#endif