/*******************************************************************************
 Interface definition of EFC PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_nmic.h

 Summary:
    Interface definition of NMIC Plib.

 Description:
    This file defines the interface for the NMIC Plib.
    It allows user to configure the sources for Non-maskable interrupt.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2016 released Microchip Technology Inc.  All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).
You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef ${NMIC_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define ${NMIC_INSTANCE_NAME}_H

#include <stdint.h>
#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END



// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

typedef void (*NMIC_CALLBACK)(uintptr_t context, uint32_t int_cause);

typedef enum
{
<#list 0..NUM_NMIC_SOURCE-1 as i>
    <#assign NMIC_ENUM_CAPTION = "NMIC_SOURCE_" + i >
    ${.vars[NMIC_ENUM_CAPTION]?replace("SOURCE", "SRC")} = NMIC_ISR_NMI${i}_Msk,
</#list>
} NMIC_SOURCE;

typedef struct
{
    NMIC_CALLBACK          callback;
    uintptr_t              context;
} NMIC_OBJECT ;
/***************************** NMIC API *******************************/
void ${NMIC_INSTANCE_NAME}_Initialize( void );
void ${NMIC_INSTANCE_NAME}_CallbackRegister( NMIC_CALLBACK callback, uintptr_t context );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif
