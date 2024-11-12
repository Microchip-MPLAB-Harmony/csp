/*******************************************************************************
  Non-Volatile Memory Controller(${FCR_INSTANCE_NAME}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FCR_INSTANCE_NAME?lower_case}.c

  Summary:
    Interface definition of ${FCR_INSTANCE_NAME} Plib.

  Description:
    This file defines the interface for the ${FCR_INSTANCE_NAME} Plib.
    It allows user to Program, Erase and lock the on-chip Non Volatile Flash
    Memory.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <string.h>
#include "plib_${FCR_INSTANCE_NAME?lower_case}.h"

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Interface Functions                                               */
/* ************************************************************************** */
/* ************************************************************************** */

void ${FCR_INSTANCE_NAME}_Initialize( void )
{
    /* Flash wait state initialization is performed at the start of the SYS_Initialize routine */
}

bool ${FCR_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    uint32_t *pAddress = (uint32_t *)address;
   (void)memcpy(data,pAddress,length);

    return true;
}

<#if FCR_CRC == true>
bool FCR_CRCCalculate (uint32_t startAddress, size_t length, uint32_t crcSeed, uint32_t * crc)
{
	// Clear CRC Registers
    ${FCR_INSTANCE_NAME}_REGS->FCR_CRCCTRL |= FCR_CRCCTRL_CRCRST(1U);
    while((${FCR_INSTANCE_NAME}_REGS->FCR_CRCCTRL & FCR_CRCCTRL_CRCRST_Msk) == 1U)
    {
        /* Wait for the FCR Operation to Complete */
    }
    
    // Register Setup
    ${FCR_INSTANCE_NAME}_REGS->FCR_CRCMODE =    FCR_CRCMODE_PLEN32(1U) | FCR_CRCMODE_RIN(1U) | FCR_CRCMODE_ROUT(1U);

    ${FCR_INSTANCE_NAME}_REGS->FCR_CRCPOLY  =    FCR_CRCPOLY_CRCPOLY(0x04C11DB7U);
    ${FCR_INSTANCE_NAME}_REGS->FCR_CRCIV    =    FCR_CRCIV_CRCIV(crcSeed);
    ${FCR_INSTANCE_NAME}_REGS->FCR_CRCMADR  =    FCR_CRCMADR_CRCMADR(startAddress);
    ${FCR_INSTANCE_NAME}_REGS->FCR_CRCMLEN  =    FCR_CRCMLEN_CRCMLEN(length);

    // Start CRC calculation
    ${FCR_INSTANCE_NAME}_REGS->FCR_CRCCTRL |=    FCR_CRCCTRL_CRCEN(0x1U);
    while((${FCR_INSTANCE_NAME}_REGS->FCR_INTFLAG & FCR_INTFLAG_CRCDONE_Msk) == 0U)
    {
        /* Wait for the FCR Operation to Complete */
    }
    
    /* Reading the resultant crc value from the CRCACC register */
    *crc = (uint32_t) ${FCR_INSTANCE_NAME}_REGS->FCR_CRCACC;
    
    return true;
}
</#if>