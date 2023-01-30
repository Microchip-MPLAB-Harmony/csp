/*******************************************************************************
  Data Type definition of RTOS Timer PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RTOS_TMR_INSTANCE_NAME?lower_case}_tmr.h

  Summary:
    Data Type definition of the RTOS Timer Peripheral Interface Plib.

  Description:
    This file defines the Data Types for the RTOS Timer Plib.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${RTOS_TMR_INSTANCE_NAME}_H
#define PLIB_${RTOS_TMR_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdint.h>
#include "device.h"
#include "plib_rtos_tmr_common.h"

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

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
void ${RTOS_TMR_INSTANCE_NAME}Timer_Initialize(void);

void ${RTOS_TMR_INSTANCE_NAME}Timer_Start(void);

void ${RTOS_TMR_INSTANCE_NAME}Timer_Stop(void);

void ${RTOS_TMR_INSTANCE_NAME}Timer_Halt(void);

void ${RTOS_TMR_INSTANCE_NAME}Timer_Resume(void);

void ${RTOS_TMR_INSTANCE_NAME}Timer_PeriodSet(uint32_t period);

uint32_t ${RTOS_TMR_INSTANCE_NAME}Timer_PeriodGet(void);

uint32_t ${RTOS_TMR_INSTANCE_NAME}Timer_CounterGet(void);

uint32_t ${RTOS_TMR_INSTANCE_NAME}Timer_FrequencyGet(void);

void ${RTOS_TMR_INSTANCE_NAME}Timer_CallbackRegister( RTOS_TMR_CALLBACK callback_fn, uintptr_t context );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }
#endif
// DOM-IGNORE-END

#endif /* PLIB_${RTOS_TMR_INSTANCE_NAME}_H */
