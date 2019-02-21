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

#ifndef _PLIB_${CMP_INSTANCE_NAME}_H
#define _PLIB_${CMP_INSTANCE_NAME}_H

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
    /*CMP Output*/
    CMP1_OUTPUT_STATUS = _CMSTAT_C1OUT_MASK,
    CMP2_OUTPUT_STATUS = _CMSTAT_C2OUT_MASK,
    CMP3_OUTPUT_STATUS = _CMSTAT_C3OUT_MASK,
    CMP4_OUTPUT_STATUS = _CMSTAT_C4OUT_MASK,
    CMP5_OUTPUT_STATUS = _CMSTAT_C5OUT_MASK,

} CMP_STATUS_SOURCE;

typedef void (*CMP_CALLBACK) (uintptr_t context);

typedef struct
{    
    CMP_CALLBACK callback;
	uintptr_t    context;
	
} CMP_OBJECT ;

// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

void ${CMP_INSTANCE_NAME}_Initialize (void);

void ${CMP_INSTANCE_NAME}_1_CompareEnable (void);
void ${CMP_INSTANCE_NAME}_2_CompareEnable (void);
void ${CMP_INSTANCE_NAME}_3_CompareEnable (void);
void ${CMP_INSTANCE_NAME}_4_CompareEnable (void);
void ${CMP_INSTANCE_NAME}_5_CompareEnable (void);

void ${CMP_INSTANCE_NAME}_1_CompareDisable (void);
void ${CMP_INSTANCE_NAME}_2_CompareDisable (void);
void ${CMP_INSTANCE_NAME}_3_CompareDisable (void);
void ${CMP_INSTANCE_NAME}_4_CompareDisable (void);
void ${CMP_INSTANCE_NAME}_5_CompareDisable (void);

bool ${CMP_INSTANCE_NAME}_StatusGet (CMP_STATUS_SOURCE source);
<#list 1..5 as i>
<#assign CMP_CMxCON_EVPOL = "CMP_" + i + "_CON_EVPOL">
<#if .vars[CMP_CMxCON_EVPOL] != "0">

CMP_OBJECT cmp${i}Obj;
void ${CMP_INSTANCE_NAME}_${i}_CallbackRegister(CMP_CALLBACK callback, uintptr_t context);
</#if>
</#list>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // _PLIB_${CMP_INSTANCE_NAME}_H
