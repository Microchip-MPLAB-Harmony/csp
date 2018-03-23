/*******************************************************************************
  Analog Comparator PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${AC_INSTANCE_NAME?lower_case}.h

  Summary:
    AC Header File

  Description:
    This file defines the interface to the AC peripheral library.
    This library provides access to and control of the Analog Comparator.

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
#ifndef PLIB_${AC_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${AC_INSTANCE_NAME}_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include "${__PROCESSOR?lower_case}.h"

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

typedef enum
{
    /* Analog Comparator Output Interrupt */
    AC_OUTPUT_INTERRUPT = 0,

    /* Analog Comparator Window Mode Output Interrupt */
    AC_WIN_INTERRUPT = 1

} AC_INTERRUPTS;

typedef enum
{
    /* Analog Comparator Output - Non Interrupt Mode */
    AC_OUTPUT = 0,

    /* Analog Comparator Output - Interrupt Mode */
    AC_INTERRUPT = 1,

    /* Analog Comparator Output - Window Mode */
    AC_WINDOW_INTERRUPT = 2

} AC_STATUS;

typedef enum
{
<#list 0 ..(AC_NUM_COMPARATORS -1) as i >
    <#assign CH_NUM = i>
    ${AC_INSTANCE_NAME}_CHANNEL${CH_NUM} = ${CH_NUM},
</#list>
}AC_CHANNEL;

typedef void (*${AC_INSTANCE_NAME}_CALLBACK) (uintptr_t context);

typedef struct
{
    AC_CALLBACK callback;
    uintptr_t    context;

} AC_OBJECT ;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${AC_INSTANCE_NAME}_Initialize (void);

void ${AC_INSTANCE_NAME}_Start( AC_CHANNEL channel_id );

bool ${AC_INSTANCE_NAME}_StatusGet ( AC_STATUS status, AC_CHANNEL channel);

void ${AC_INSTANCE_NAME}_CallbackRegister (AC_CALLBACK callback, uintptr_t context);

#endif /* PLIB_${AC_INSTANCE_NAME}_H */
