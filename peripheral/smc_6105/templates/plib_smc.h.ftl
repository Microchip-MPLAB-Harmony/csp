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

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

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
