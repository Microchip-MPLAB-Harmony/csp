/*******************************************************************************
  Analog Comparator Controller (ACC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${ACC_INSTANCE_NAME?lower_case}.h

  Summary
    ACC PLIB Header File.

  Description
    This file defines the interface to the ACC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

/* Guards against multiple inclusion */
#ifndef PLIB_${ACC_INSTANCE_NAME}_H
#define PLIB_${ACC_INSTANCE_NAME}_H

#include <stdbool.h>

#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif /* __cplusplus */

typedef enum
{
    ACC_STATUS_SOURCE_COMPARATOR_OUTPUT = ACC_ISR_SCO_Msk,
    ACC_STATUS_SOURCE_COMPARISON_EDGE = ACC_ISR_CE_Msk,
} ACC_STATUS_SOURCE;

typedef void(*ACC_CALLBACK)(bool output, uintptr_t context);

void ${ACC_INSTANCE_NAME}_Initialize(void);
void ${ACC_INSTANCE_NAME}_Enable(void);
void ${ACC_INSTANCE_NAME}_Disable(void);
<#if ACC_INTERRUPT_ENABLE>
void ${ACC_INSTANCE_NAME}_CallbackRegister(ACC_CALLBACK pCallback, uintptr_t context);
<#else>
bool ${ACC_INSTANCE_NAME}_StatusGet(ACC_STATUS_SOURCE status);
</#if>

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif /* __cplusplus */

#endif /* PLIB_${ACC_INSTANCE_NAME}_H */