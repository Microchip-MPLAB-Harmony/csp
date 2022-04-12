/*******************************************************************************
  PWM Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_mem2mem_common.h

  Summary
    MEM2MEM peripheral library interface.

  Description
    This file defines the interface to the PWM peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

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

#ifndef PLIB_MEM2MEM_COMMON_H    // Guards against multiple inclusion
#define PLIB_MEM2MEM_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus  // Provide C++ Compatibility
extern "C" {
#endif

// *****************************************************************************
// *****************************************************************************
// Section: Preprocessor macros
// *****************************************************************************
// *****************************************************************************
#define    MEM2MEM_TRANSFER_WIDTH_BYTE      (0U)

#define    MEM2MEM_TRANSFER_WIDTH_HALFWORD  (1U)

#define    MEM2MEM_TRANSFER_WIDTH_WORD      (2U)

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
typedef uint32_t MEM2MEM_TRANSFER_WIDTH;

typedef enum
{
    /* Data was transferred successfully. */
    MEM2MEM_TRANSFER_EVENT_COMPLETE,

    /* Error while processing the request */
    MEM2MEM_TRANSFER_EVENT_ERROR

} MEM2MEM_TRANSFER_EVENT;

typedef void (*MEM2MEM_CALLBACK)( MEM2MEM_TRANSFER_EVENT event, uintptr_t context );

typedef struct
{
    MEM2MEM_CALLBACK    callback;
    uintptr_t           context;

} MEM2MEM_OBJECT;

#ifdef __cplusplus // Provide C++ Compatibility
    }
#endif

#endif //PLIB_MEM2MEM_COMMON_H
