/*******************************************************************************
  Timer/Counter(${TCC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${TCC_INSTANCE_NAME?lower_case}.h

  Summary
    ${TCC_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the TCC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

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

#ifndef PLIB_${TCC_INSTANCE_NAME}_H       // Guards against multiple inclusion
#define PLIB_${TCC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_tcc_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

/* Total number of TCC channels in a module */
#define ${TCC_INSTANCE_NAME}_NUM_CHANNELS    (${TCC_NUM_CHANNELS}U)

/* TCC Channel numbers

   Summary:
    Identifies channel number within TCC module

   Description:
    This enumeration identifies TCC channel number.

   Remarks:
    None.
*/
typedef enum
{
<#list 0 ..(TCC_NUM_CHANNELS -1) as i >
    <#assign CH_NUM = i>
    ${TCC_INSTANCE_NAME}_CHANNEL${CH_NUM},
</#list>
}${TCC_INSTANCE_NAME}_CHANNEL_NUM;


typedef enum
{
    ${TCC_INSTANCE_NAME}_COMPARE_STATUS_OVF = TCC_INTFLAG_OVF_Msk,
<#list 0 ..(TCC_NUM_CHANNELS -1) as i >
    ${TCC_INSTANCE_NAME}_COMPARE_STATUS_MC_${i} = TCC_INTFLAG_MC${i}_Msk,
</#list>
}${TCC_INSTANCE_NAME}_COMPARE_STATUS;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/


void ${TCC_INSTANCE_NAME}_CompareInitialize( void );

void ${TCC_INSTANCE_NAME}_CompareStart( void );

void ${TCC_INSTANCE_NAME}_CompareStop( void );

uint32_t ${TCC_INSTANCE_NAME}_CompareFrequencyGet( void );

<#if TCC_SIZE = 16>
bool ${TCC_INSTANCE_NAME}_Compare16bitPeriodSet( uint16_t period );

uint16_t ${TCC_INSTANCE_NAME}_Compare16bitPeriodGet( void );

uint16_t ${TCC_INSTANCE_NAME}_Compare16bitCounterGet( void );

void ${TCC_INSTANCE_NAME}_Compare16bitCounterSet( uint16_t count );

bool ${TCC_INSTANCE_NAME}_Compare16bitMatchSet( ${TCC_INSTANCE_NAME}_CHANNEL_NUM channel, uint16_t compareValue );

<#elseif TCC_SIZE = 24>
bool ${TCC_INSTANCE_NAME}_Compare24bitPeriodSet( uint32_t period );

uint32_t ${TCC_INSTANCE_NAME}_Compare24bitPeriodGet( void );

uint32_t ${TCC_INSTANCE_NAME}_Compare24bitCounterGet( void );

void ${TCC_INSTANCE_NAME}_Compare24bitCounterSet( uint32_t count );

bool ${TCC_INSTANCE_NAME}_Compare24bitMatchSet(${TCC_INSTANCE_NAME}_CHANNEL_NUM channel, uint32_t compareValue );

<#elseif TCC_SIZE = 32>
bool ${TCC_INSTANCE_NAME}_Compare32bitPeriodSet( uint32_t period );

uint32_t ${TCC_INSTANCE_NAME}_Compare32bitPeriodGet( void );

uint32_t ${TCC_INSTANCE_NAME}_Compare32bitCounterGet( void );

void ${TCC_INSTANCE_NAME}_Compare32bitCounterSet( uint32_t count );

bool ${TCC_INSTANCE_NAME}_Compare32bitMatchSet(${TCC_INSTANCE_NAME}_CHANNEL_NUM channel, uint32_t compareValue );
</#if>

<#if TCC_COMPARE_INTERRUPT_MODE = true>

void ${TCC_INSTANCE_NAME}_CompareCallbackRegister( TCC_CALLBACK callback, uintptr_t context );

<#else>

uint32_t ${TCC_INSTANCE_NAME}_CompareStatusGet( void );
</#if>

void ${TCC_INSTANCE_NAME}_CompareCommandSet(TCC_COMMAND command);


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${TCC_INSTANCE_NAME}_H */
