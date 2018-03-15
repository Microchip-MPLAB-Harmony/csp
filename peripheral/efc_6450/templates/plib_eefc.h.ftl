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

#ifndef EEFC${INDEX?string}_H    // Guards against multiple inclusion
#define EEFC${INDEX?string}_H

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

#define EEFC0_ROWSIZE					0x2000
#define EEFC0_PAGESIZE					0x200
#define	EEFC0_LOCKSIZE					0x4000


typedef enum
{
	EEFC_SUCCESS = 0x1,	
	/*In-valid command*/
	EEFC_CMD_ERROR = 0x2,
	/*Flash region is locked*/
	EEFC_LOCK_ERROR = 0x4,
	/*Flash Error*/
	EEFC_FLERR_ERROR = 0x8,
	/*Flash Encountered an ECC error*/
	EEFC_ECC_ERROR = 0xF0000,
} EEFC_STATUS;

<#if eefcEnableInterrupt == true>
	<#lt>typedef void (*EEFC_CALLBACK)(uintptr_t context);
	<#lt>typedef struct
	<#lt>{
		<#lt>	EEFC_CALLBACK          callback;
		<#lt>	uintptr_t               context;
	<#lt>} EEFC_OBJECT ;	
</#if>

void EEFC${INDEX?string}_WriteQuadWord( uint32_t address, uint32_t* data );
void EEFC${INDEX?string}_WritePage( uint32_t address, uint32_t* data );
void EEFC${INDEX?string}_EraseRow( uint32_t address );
EEFC_STATUS EEFC${INDEX?string}_StatusGet( void );
bool EEFC${INDEX?string}_IsBusy(void);
void EEFC${INDEX?string}_RegionLock(uint32_t address);
void EEFC${INDEX?string}_RegionUnlock(uint32_t address);
<#if eefcEnableInterrupt == true>
	<#lt>void EEFC${INDEX?string}_CallbackRegister( EEFC_CALLBACK callback, uintptr_t context );
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif