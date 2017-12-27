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

#include "plib_eefc.h"

uint16_t EEFC_GetRowSize( void )
{
	return (0x2000);
}

void EEFC_EraseRow( uint32_t address )
{
	volatile uint16_t page_number;

	/*Calculate the Page number to be passed for FARG register*/
	page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;
	<#if eefcEnableInterrupt == true>
		<#lt>_EFC_REGS->EEFC_FMR |= EEFC_FMR_FRDY;
	</#if>
	/* Issue the FLASH erase operation*/
	_EFC_REGS->EEFC_FCR.w = (EEFC_FCR_FCMD_EPA|EEFC_FCR_FARG(page_number|0x2)|EEFC_FCR_FKEY_PASSWD);

}

void EEFC_WritePage( uint32_t address, uint32_t* data )
{
	volatile uint16_t page_number;
	/*Calculate the Page number to be passed for FARG register*/
	page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;

	for (int i = 0; i < IFLASH_PAGE_SIZE; i += 4)
	{
	*((uint32_t *)( IFLASH_ADDR + ( page_number * IFLASH_PAGE_SIZE ) + i )) =	*(( data++ ));
	}
	<#if eefcEnableInterrupt == true>
		<#lt>	_EFC_REGS->EEFC_FMR |= EEFC_FMR_FRDY;
	</#if>
	/* Issue the FLASH write operation*/
	_EFC_REGS->EEFC_FCR.w = (EEFC_FCR_FCMD_WP | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);

}

void EEFC_WriteQuadWord( uint32_t address, uint32_t* data )
{
	if((address & 0x0000000f))
	{
	return;
	}
	volatile uint16_t page_number;

	/*Calculate the Page number to be passed for FARG register*/
	page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;

	for (int i = 0; i < 16; i += 4)
	{
	*((uint32_t *)(( address ) + i )) =	*((uint32_t *)( data++ ));
	}
	<#if eefcEnableInterrupt == true>
		<#lt>	_EFC_REGS->EEFC_FMR |= EEFC_FMR_FRDY;
	</#if>
	/* Issue the FLASH write operation*/
	_EFC_REGS->EEFC_FCR.w = (EEFC_FCR_FCMD_WP | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);
	//status = _EFC_REGS->EEFC_FSR.w;
	/*Wait for the FLASH operation to complete*/

}

uint16_t EEFC_GetPageSize( void )
{
	return 0x200;
}
EEFC_STATUS EEFC_StatusGet( void )
{
	uint32_t status =  _EFC_REGS->EEFC_FSR.w;
	if (status & EEFC_FSR_FLERR_Msk)
	{
		return EEFC_ERROR;
	}
	else if (status & EEFC_FSR_FLOCKE_Msk)
	{
		return EEFC_LOCK_ERROR;
	}
	else if (status & 0x000f0000)
	{
		return EEFC_ECC_ERROR;
	}
	else if (status & EEFC_FSR_FRDY_Msk)
	{
		return EEFC_SUCCESS;
	}
	return EEFC_BUSY;
}

bool EEFC_IsBusy( void )
{
	return(_EFC_REGS->EEFC_FSR.w & EEFC_FSR_FRDY_Msk);
}

uint16_t EEFC_GetLockRegionSize( void )
{
	return(IFLASH_SIZE / 128);
}

void EEFC_RegionLock(uint32_t address)
{
	volatile uint16_t page_number;
	/*Calculate the Page number to be passed for FARG register*/
	page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;
	<#if eefcEnableInterrupt == true>
		<#lt>	_EFC_REGS->EEFC_FMR |= EEFC_FMR_FRDY;
	</#if>
	_EFC_REGS->EEFC_FCR.w = (EEFC_FCR_FCMD_SLB | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);
}

void EEFC_RegionUnlock(uint32_t address)
{
	volatile uint16_t page_number;
	/*Calculate the Page number to be passed for FARG register*/
	page_number = (address - IFLASH_ADDR) / IFLASH_PAGE_SIZE;
	<#if eefcEnableInterrupt == true>
		<#lt>	_EFC_REGS->EEFC_FMR |= EEFC_FMR_FRDY;
	</#if>
	_EFC_REGS->EEFC_FCR.w = (EEFC_FCR_FCMD_CLB | EEFC_FCR_FARG(page_number)| EEFC_FCR_FKEY_PASSWD);
}

<#if eefcEnableInterrupt == true>
	<#lt>void EEFC_CallbackRegister( EEFC_CALLBACK callback, uintptr_t context )
	<#lt>{
	<#lt>	eefc.callback = callback;
	<#lt>	eefc.context = context;
	<#lt>}
</#if>
