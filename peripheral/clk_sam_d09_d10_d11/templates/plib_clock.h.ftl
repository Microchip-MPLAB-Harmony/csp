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

#ifndef PLIB_CLOCK_H  // Guards against multiple inclusion
#define PLIB_CLOCK_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
<#if SYSCTRL_INTERRUPT_ENABLE_VAL?? && SYSCTRL_INTERRUPT_ENABLE_VAL != "0x0">
#include "device.h"
</#if>

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

<#if SYSCTRL_INTERRUPT_ENABLE_VAL?? && SYSCTRL_INTERRUPT_ENABLE_VAL != "0x0">
typedef enum
{
<#if SYSCTRL_INTERRUPT_XOSCRDY>
    SYSCTRL_INTERRUPT_XOSCRDY_MASK = SYSCTRL_INTFLAG_XOSCRDY_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_XOSC32KRDY>
    SYSCTRL_INTERRUPT_XOSC32KRDY_MASK = SYSCTRL_INTFLAG_XOSC32KRDY_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_OSC32KRDY>
    SYSCTRL_INTERRUPT_OSC32KRDY_MASK = SYSCTRL_INTFLAG_OSC32KRDY_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_OSC8MRDY>
    SYSCTRL_INTERRUPT_OSC8MRDY_MASK = SYSCTRL_INTFLAG_OSC8MRDY_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_DFLLRDY>
    SYSCTRL_INTERRUPT_DFLLRDY_MASK = SYSCTRL_INTFLAG_DFLLRDY_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_DFLLOOB>
    SYSCTRL_INTERRUPT_DFLLOOB_MASK = SYSCTRL_INTFLAG_DFLLOOB_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_DFLLLCKF>
    SYSCTRL_INTERRUPT_DFLLLCKF_MASK = SYSCTRL_INTFLAG_DFLLLCKF_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_DFLLLCKC>
    SYSCTRL_INTERRUPT_DFLLLCKC_MASK = SYSCTRL_INTFLAG_DFLLLCKC_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_DFLLRCS>
    SYSCTRL_INTERRUPT_DFLLRCS_MASK = SYSCTRL_INTFLAG_DFLLRCS_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_BOD33RDY>
    SYSCTRL_INTERRUPT_BOD33RDY_MASK = SYSCTRL_INTFLAG_BOD33RDY_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_BOD33DET>
    SYSCTRL_INTERRUPT_BOD33DET_MASK = SYSCTRL_INTFLAG_BOD33DET_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_B33SRDY>
    SYSCTRL_INTERRUPT_B33SRDY_MASK = SYSCTRL_INTFLAG_B33SRDY_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_DPLLLCKR>
    SYSCTRL_INTERRUPT_DPLLLCKR_MASK = SYSCTRL_INTFLAG_DPLLLCKR_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_DPLLLCKF>
    SYSCTRL_INTERRUPT_DPLLLCKF_MASK = SYSCTRL_INTFLAG_DPLLLCKF_Msk,
</#if>
<#if SYSCTRL_INTERRUPT_DPLLLTO>
    SYSCTRL_INTERRUPT_DPLLLTO_MASK = SYSCTRL_INTFLAG_DPLLLTO_Msk
</#if>
} SYSCTRL_INTERRUPT_MASK;

typedef void (*SYSCTRL_CALLBACK)(SYSCTRL_INTERRUPT_MASK interruptMask, uintptr_t context);

typedef struct
{
    SYSCTRL_CALLBACK    callback;
    uintptr_t           context;
} SYSCTRL_CALLBACK_OBJECT;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void CLOCK_Initialize( void );
<#if SYSCTRL_INTERRUPT_ENABLE_VAL?? && SYSCTRL_INTERRUPT_ENABLE_VAL != "0x0">
void SYSCTRL_CallbackRegister(SYSCTRL_CALLBACK callback, uintptr_t context);
</#if>

#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif

#endif /* PLIB_CLOCK_H */

