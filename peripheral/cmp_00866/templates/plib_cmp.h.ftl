/*******************************************************************************
  Comparator (CMP) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CMP_INSTANCE_NAME?lower_case}.h

  Summary:
    CMP PLIB Header File

  Description:
    None

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

#ifndef PLIB_${CMP_INSTANCE_NAME}_H
#define PLIB_${CMP_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"

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
<#list 1..CMP_COUNT as i>
    /* CMP${i} Output */
    CMP${i}_OUTPUT_STATUS = _CMSTAT_C${i}OUT_MASK,

</#list>
} CMP_STATUS_SOURCE;

typedef void (*CMP_CALLBACK) (uintptr_t context);

typedef struct
{
    CMP_CALLBACK callback;

    uintptr_t    context;

} CMP_OBJECT;

// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

void ${CMP_INSTANCE_NAME}_Initialize(void);

bool ${CMP_INSTANCE_NAME}_StatusGet(CMP_STATUS_SOURCE source);

<#list 1..CMP_COUNT as i>
<#assign CMP_CMxCON_EVPOL = "CMP_CM" + i + "CON_EVPOL">
<#assign CMP_IFS_REG = "CMP" + i + "_IFS_REG">
void ${CMP_INSTANCE_NAME}_${i}_CompareEnable(void);

void ${CMP_INSTANCE_NAME}_${i}_CompareDisable(void);

<#if CMP_CMxCON_EVPOL != "0">
void ${CMP_INSTANCE_NAME}_${i}_CallbackRegister(CMP_CALLBACK callback, uintptr_t context);

</#if>
</#list>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // PLIB_${CMP_INSTANCE_NAME}_H
