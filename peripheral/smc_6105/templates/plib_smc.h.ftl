/*******************************************************************
  Company:
    Microchip Technology Inc.
    Memory System Service SMC Initialization File

  File Name:
    plib_${SMC_INSTANCE_NAME?lower_case}.h

  Summary:
    Static Memory Controller (SMC) peripheral library interface.
    This file contains the source code to initialize the SMC_6498 controller

  Description
    This file defines the interface to the SMC peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual smc<x> headers will be
    generated as required by the MCC (where <x> is the peripheral instance
    number).

    Every interface symbol has a lower-case 'x' in it following the "SMC"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef _PLIB_${SMC_INSTANCE_NAME}_H
#define _PLIB_${SMC_INSTANCE_NAME}_H

#include <stdint.h>         // uint32_t, uintptr_t
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

<#assign SFR_CCFG_EBICSA_EBI_CS = "SFR_CCFG_EBICSA_EBI_CS" + SMC_NAND_CS_NUM + "A">

<#if SMC_SRIER_SRIE == true>
    <#lt>typedef void (* SMC_CALLBACK)( uintptr_t context, uint32_t interruptStatus );
</#if>
<#if PMECC_IER_ERRIE == true>
    <#lt>typedef void (* PMECC_CALLBACK)( uintptr_t context, uint32_t interruptStatus );
</#if>
<#if PMERRLOC_ELIER_DONE == true>
    <#lt>typedef void (* PMERRLOC_CALLBACK)( uintptr_t context, uint32_t interruptStatus );
</#if>

<#if SMC_SRIER_SRIE == true>
    <#lt>void ${SMC_INSTANCE_NAME}_CallbackRegister( SMC_CALLBACK callback, uintptr_t context );
</#if>
void ${SMC_INSTANCE_NAME}_Initialize( void );
<#if .vars[SFR_CCFG_EBICSA_EBI_CS] == true>
uint32_t ${SMC_INSTANCE_NAME}_DataAddressGet(uint8_t chipSelect);
void ${SMC_INSTANCE_NAME}_CommandWrite(uint32_t dataAddress, uint8_t command);
void ${SMC_INSTANCE_NAME}_CommandWrite16(uint32_t dataAddress, uint16_t command);
void ${SMC_INSTANCE_NAME}_AddressWrite(uint32_t dataAddress, uint8_t address);
void ${SMC_INSTANCE_NAME}_AddressWrite16(uint32_t dataAddress, uint16_t address);
void ${SMC_INSTANCE_NAME}_DataWrite(uint32_t dataAddress, uint8_t data);
void ${SMC_INSTANCE_NAME}_DataWrite16(uint32_t dataAddress, uint16_t data);
uint8_t ${SMC_INSTANCE_NAME}_DataRead(uint32_t dataAddress);
uint16_t ${SMC_INSTANCE_NAME}_DataRead16(uint32_t dataAddress);
</#if>

<#if PMECC_CTRL_ENABLE == true>
void ${PMECC_INSTANCE_NAME}_DataPhaseStart(bool writeEnable);
bool ${PMECC_INSTANCE_NAME}_StatusIsBusy(void);
uint8_t ${PMECC_INSTANCE_NAME}_ErrorGet(void);
int16_t ${PMECC_INSTANCE_NAME}_RemainderGet(uint32_t sector, uint32_t remainderIndex);
uint8_t ${PMECC_INSTANCE_NAME}_ECCGet(uint32_t sector, uint32_t byteIndex);
uint32_t ${PMERRLOC_INSTANCE_NAME}_ErrorLocationGet(uint8_t position);
void ${PMERRLOC_INSTANCE_NAME}_ErrorLocationDisable(void);
void ${PMERRLOC_INSTANCE_NAME}_SigmaSet(uint32_t sigmaVal, uint32_t sigmaNum);
uint32_t ${PMERRLOC_INSTANCE_NAME}_ErrorLocationFindNumOfRoots(uint32_t sectorSizeInBits, uint32_t errorNumber);
</#if>
<#if PMECC_IER_ERRIE == true>
    <#lt>void ${PMECC_INSTANCE_NAME}_CallbackRegister( PMECC_CALLBACK callback, uintptr_t context );
</#if>
<#if PMERRLOC_ELIER_DONE == true>
    <#lt>void ${PMERRLOC_INSTANCE_NAME}_CallbackRegister( PMERRLOC_CALLBACK callback, uintptr_t context );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // _PLIB_${SMC_INSTANCE_NAME}_H

/*******************************************************************************
 End of File
*/
