/******************************************************************************* External Interrupt Controller (EIC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${EIC_INSTANCE_NAME?lower_case}.h

  Summary
    EIC PLIB Header File.

  Description
    This file defines the interface to the EIC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

/* Guards against multiple inclusion */
#ifndef PLIB_${EIC_INSTANCE_NAME}_H
#define PLIB_${EIC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part of it.
*/
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
/* EIC Secure Pin Count */
#define EXTINT_COUNT                        (${EIC_INT_COUNT}U)
<#else>
/* EIC Pin Count */
#define EXTINT_COUNT                        (${EIC_INT_COUNT}U)
</#if>

typedef enum
{
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
<#list 0..EIC_INT_COUNT as i>
    <#assign EIC_INT_CHANNEL = "EIC_CHAN_" + i>
    <#assign EIC_NON_SEC_CHANNEL = "EIC_NONSEC_" + i>
        <#if .vars[EIC_INT_CHANNEL]?has_content>
            <#if (.vars[EIC_INT_CHANNEL] != false) && .vars[EIC_NON_SEC_CHANNEL] == "SECURE">
    <#lt>    /* External Interrupt Controller Pin ${i} */
    <#lt>    EIC_PIN_${i} = ${i},
            </#if>
            </#if>
</#list>
<#else>
<#list 0..EIC_INT_COUNT as i>
    <#assign EIC_INT_CHANNEL = "EIC_CHAN_" + i>
        <#if .vars[EIC_INT_CHANNEL]?has_content>
            <#if (.vars[EIC_INT_CHANNEL] != false)>
    <#lt>    /* External Interrupt Controller Pin ${i} */
    <#lt>    EIC_PIN_${i} = ${i},

            </#if>
        </#if>
</#list>
</#if>
    EIC_PIN_MAX = 16

} EIC_PIN;

<#if EIC_INT != "0">

typedef void (*EIC_CALLBACK) (uintptr_t context);

typedef struct
{
    /* External Interrupt Pin Callback Handler */
    EIC_CALLBACK    callback;

    /* External Interrupt Pin Client context */
    uintptr_t       context;

    /* External Interrupt Pin number */
    EIC_PIN         eicPinNo;

} EIC_CALLBACK_OBJ;
</#if>

<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
<#if (NMI_IS_NON_SECURE == "SECURE") && (NMI_CTRL == true)>
typedef void (*EIC_NMI_CALLBACK) (uintptr_t context);

typedef struct
{
    /* NMI Callback Handler */
    EIC_NMI_CALLBACK callback;

    /* NMI Client context */
    uintptr_t       context;

} EIC_NMI_CALLBACK_OBJ;
</#if>
<#else>
<#if NMI_CTRL == true>
typedef void (*EIC_NMI_CALLBACK) (uintptr_t context);

typedef struct
{
    /* NMI Callback Handler */
    EIC_NMI_CALLBACK callback;

    /* NMI Client context */
    uintptr_t       context;

} EIC_NMI_CALLBACK_OBJ;
</#if>
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
    this interface.
*/

void ${EIC_INSTANCE_NAME}_Initialize (void);
<#if EIC_INT != "0">
void ${EIC_INSTANCE_NAME}_InterruptEnable (EIC_PIN pin);
void ${EIC_INSTANCE_NAME}_InterruptDisable (EIC_PIN pin);
void ${EIC_INSTANCE_NAME}_CallbackRegister(EIC_PIN pin, EIC_CALLBACK callback, uintptr_t context);

</#if>
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
<#if (NMI_IS_NON_SECURE == "SECURE") && (NMI_CTRL == true)>
void ${EIC_INSTANCE_NAME}_NMICallbackRegister(EIC_NMI_CALLBACK callback, uintptr_t context);
</#if>
<#else>
<#if NMI_CTRL == true>
void ${EIC_INSTANCE_NAME}_NMICallbackRegister(EIC_NMI_CALLBACK callback, uintptr_t context);
</#if>
</#if>

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif /* PLIB_${EIC_INSTANCE_NAME}_H */
