/*******************************************************************************
  CLOCK PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_clock.h

  Summary:
    CLOCK PLIB Header File.

  Description:
    The Clock PLIB initializes all the oscillators based on the
    requirements.

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

#ifndef PLIB_CLOCK_H
#define PLIB_CLOCK_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include <stdint.h>
<#if (CKGR_MOR_MOSCXTEN && CLOCK_FAILURE_DETECT) || ((SUPC_MR_OSCBYPASS == false) && (SUPC_CR_MDXTALSEL == "1") && SLCK_CLOCK_FREQUENCY_MONITORING_ENABLE == true)>
#include "device.h"
#include <stddef.h>
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
<#if (CKGR_MOR_MOSCXTEN && CLOCK_FAILURE_DETECT)>
#define PMC_STATUS_CFDEV    PMC_SR_CFDEV_Msk
</#if>
<#if ((SUPC_MR_OSCBYPASS == false) && (SUPC_CR_MDXTALSEL == "1") && SLCK_CLOCK_FREQUENCY_MONITORING_ENABLE == true)>
#define PMC_STATUS_XT32KERR PMC_SR_XT32KERR_Msk
</#if>
<#if (CKGR_MOR_MOSCXTEN && CLOCK_FAILURE_DETECT) || ((SUPC_MR_OSCBYPASS == false) && (SUPC_CR_MDXTALSEL == "1") && SLCK_CLOCK_FREQUENCY_MONITORING_ENABLE == true)>
typedef uint32_t PMC_STATUS;

typedef void (*PMC_CALLBACK)(PMC_STATUS status, uintptr_t context);

typedef struct
{
    PMC_CALLBACK    callback;
    uintptr_t       context;
} PMC_CALLBACK_OBJECT;
</#if>

void CLOCK_Initialize (void);
<#if (CKGR_MOR_MOSCXTEN && CLOCK_FAILURE_DETECT) || ((SUPC_MR_OSCBYPASS == false) && (SUPC_CR_MDXTALSEL == "1") && SLCK_CLOCK_FREQUENCY_MONITORING_ENABLE == true)>
void PMC_CallbackRegister(PMC_CALLBACK callback, uintptr_t context);
</#if>

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif /* PLIB_CLOCK_H */