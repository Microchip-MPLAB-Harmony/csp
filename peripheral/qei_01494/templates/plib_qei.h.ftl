/*******************************************************************************
  Quadrature Encoder Interface (QEI) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${QEI_INSTANCE_NAME?lower_case}.h

  Summary:
    QEI PLIB Header File

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

#ifndef _PLIB_${QEI_INSTANCE_NAME}_H
#define _PLIB_${QEI_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"
#include "plib_qei_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END


// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

// *************************** ${QEI_INSTANCE_NAME} API ***************************************/
// *****************************************************************************
<#assign INTERRUPT_MODE = false>
<#if QEI_QEISTAT?number != 0>
  <#assign INTERRUPT_MODE = true>
</#if>

void ${QEI_INSTANCE_NAME}_Initialize (void);

void ${QEI_INSTANCE_NAME}_Start();

void ${QEI_INSTANCE_NAME}_Stop();

__STATIC_INLINE uint32_t ${QEI_INSTANCE_NAME}_PositionGet()
{
    return (POS${QEI_INSTANCE_NUM}CNT);
}

__STATIC_INLINE uint32_t ${QEI_INSTANCE_NAME}_VelocityGet()
{
    return (VEL${QEI_INSTANCE_NUM}CNT);
}

__STATIC_INLINE uint32_t ${QEI_INSTANCE_NAME}_RevolutionsGet()
{
    return (INDX${QEI_INSTANCE_NUM}CNT);
}

uint32_t ${QEI_INSTANCE_NAME}_PulseIntervalGet();

void ${QEI_INSTANCE_NAME}_PositionWindowSet(uint32_t high_threshold, uint32_t low_threshold);

<#if INTERRUPT_MODE == true>
void ${QEI_INSTANCE_NAME}_CallbackRegister(QEI_CALLBACK callback, uintptr_t context);
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // _PLIB_${QEI_INSTANCE_NAME}_H
