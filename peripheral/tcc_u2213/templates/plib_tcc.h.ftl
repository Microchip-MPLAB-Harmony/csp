/*******************************************************************************
  Data Type definition of Timer/Counter(TCC) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_tcc${TCC_INDEX}.h

  Summary:
    Data Type definition of the TCC Peripheral Interface Plib.

  Description:
    This file defines the Data Types for the TCC Plib.

  Remarks:
    None.

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#ifndef PLIB_TCC${TCC_INDEX}_PWMH
#define PLIB_TCC${TCC_INDEX}_PWMH

#include <stddef.h>
#include <stdbool.h>
#include "plib_tcc.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/*  The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

/* Total number of TCC channels in a module */
#define TCC${TCC_INDEX}_NUM_CHANNELS    (${TCC_NUM_CHANNELS}U)

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
    TCC${TCC_INDEX}_CHANNEL${CH_NUM},
</#list>
}TCC${TCC_INDEX}_CHANNEL_NUM;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************
void TCC${TCC_INDEX}_PWMInitialize();

void TCC${TCC_INDEX}_PWMStart();

void TCC${TCC_INDEX}_PWMStop();

<#if TCC_IS_DEAD_TIME == 1>
void TCC${TCC_INDEX}_PWMDeadTimeSet(uint8_t deadtime_high, uint8_t deadtime_low);
</#if>
void TCC${TCC_INDEX}_PWMForceUpdate(void);

void TCC${TCC_INDEX}_PWMPeriodInterruptEnable();

void TCC${TCC_INDEX}_PWMPeriodInterruptDisable();

uint32_t TCC${TCC_INDEX}_PWMInterruptStatusGet();

void TCC${TCC_INDEX}_PWMCallbackRegister(TCC_CALLBACK callback, uintptr_t context);


<#if TCC_SIZE == 24>
void TCC${TCC_INDEX}_PWMPeriodSet(uint32_t period);

uint32_t TCC${TCC_INDEX}_PWMPeriodGet(void);

void TCC${TCC_INDEX}_PWMCounterSet(uint32_t count);

static inline void TCC${TCC_INDEX}_PWMDutySet(TCC${TCC_INDEX}_CHANNEL_NUM channel, uint32_t duty)
{
    TCC${TCC_INDEX}_REGS->TCC_CCBUF[channel] = duty;
}

<#elseif TCC_SIZE == 16>
void TCC${TCC_INDEX}_PWMPeriodSet(uint16_t period);

uint16_t TCC${TCC_INDEX}_PWMPeriodGet(void);

void TCC${TCC_INDEX}_PWMCounterSet(uint16_t count);

static inline void TCC${TCC_INDEX}_PWMDutySet(TCC${TCC_INDEX}_CHANNEL_NUM channel, uint16_t duty)
{
    TCC${TCC_INDEX}_REGS->TCC_CCBUF[channel] = duty;
}
</#if>
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }
#endif
// DOM-IGNORE-END

#endif /* PLIB_TCC${TCC_INDEX}_PWMH */
