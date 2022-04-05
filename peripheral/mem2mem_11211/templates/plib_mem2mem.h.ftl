/*******************************************************************************
Interface definition of MEM2MEM PLIB.

Company:
    Microchip Technology Inc.

File Name:
    plib_mem2mem.h

Summary:
    Interface definition of MEM2MEM Plib.

Description:
    This file defines the interface for the MEM2MEM Plib.
    It allows user to transfer data from one memory to another.
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

#ifndef ${MEM2MEM_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define ${MEM2MEM_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END


#define    MEM2MEM_TRANSFER_WIDTH_BYTE      (0U)

#define    MEM2MEM_TRANSFER_WIDTH_HALFWORD  (1U)

#define    MEM2MEM_TRANSFER_WIDTH_WORD      (2U)

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

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

bool ${MEM2MEM_INSTANCE_NAME}_ChannelTransfer( const void *srcAddr, const void *destAddr, size_t blockSize, MEM2MEM_TRANSFER_WIDTH twidth );

void ${MEM2MEM_INSTANCE_NAME}_CallbackRegister( MEM2MEM_CALLBACK callback, uintptr_t context );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif    //PLIB_${MEM2MEM_INSTANCE_NAME}_H