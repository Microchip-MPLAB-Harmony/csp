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
* Copyright (C) 20124 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${TCC_INSTANCE_NAME}_H      // Guards against multiple inclusion
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

typedef enum
{
    ${TCC_INSTANCE_NAME}_TIMER_STATUS_OVF = TCC_INTFLAG_OVF_Msk,
    ${TCC_INSTANCE_NAME}_TIMER_STATUS_MC_1 = TCC_INTFLAG_MC1_Msk,
}${TCC_INSTANCE_NAME}_TIMER_STATUS;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************

void ${TCC_INSTANCE_NAME}_TimerInitialize( void );

void ${TCC_INSTANCE_NAME}_TimerStart( void );

void ${TCC_INSTANCE_NAME}_TimerStop( void );

uint32_t ${TCC_INSTANCE_NAME}_TimerFrequencyGet( void );

<#if TCC_SIZE == 24>

void ${TCC_INSTANCE_NAME}_Timer24bitPeriodSet( uint32_t period );

uint32_t ${TCC_INSTANCE_NAME}_Timer24bitPeriodGet( void );

uint32_t ${TCC_INSTANCE_NAME}_Timer24bitCounterGet( void );

void ${TCC_INSTANCE_NAME}_Timer24bitCounterSet( uint32_t count );

<#if TCC_SYS_TIME_CONNECTED == true>
void ${TCC_INSTANCE_NAME}_Timer24bitCompareSet( uint32_t compare );
</#if>

<#elseif TCC_SIZE == 16>

void ${TCC_INSTANCE_NAME}_Timer16bitPeriodSet( uint16_t period );

uint16_t ${TCC_INSTANCE_NAME}_Timer16bitPeriodGet( void );

uint16_t ${TCC_INSTANCE_NAME}_Timer16bitCounterGet( void );

void ${TCC_INSTANCE_NAME}_Timer16bitCounterSet( uint16_t count );

<#if TCC_SYS_TIME_CONNECTED == true>
void ${TCC_INSTANCE_NAME}_Timer16bitCompareSet( uint16_t compare );
</#if>
</#if>

<#if TCC_TIMER_INTENSET_OVF = true || TCC_TIMER_INTENSET_MC1 == true>
void ${TCC_INSTANCE_NAME}_TimerCallbackRegister( TCC_CALLBACK callback, uintptr_t context );
</#if>

<#if TCC_TIMER_INTENSET_OVF == false>
bool ${TCC_INSTANCE_NAME}_TimerPeriodHasExpired( void );
</#if>

void ${TCC_INSTANCE_NAME}_TimerCommandSet(TCC_COMMAND command);


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${TCC_INSTANCE_NAME}_H */
