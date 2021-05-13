/*******************************************************************************
  Generic Timer PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_generic_timer.h

  Summary
    Generic timer PLIB Header File.

  Description
    This file defines the interface to the Generic timer peripheral library. This
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
#ifndef PLIB_GENERIC_TIMER_H
#define PLIB_GENERIC_TIMER_H

#ifdef __cplusplus  // Provide C++ Compatibility
extern "C" {
#endif //__cplusplus

<#if GENERIC_TIMER_INTERRUPT>   
typedef void (*GENERIC_TIMER_CALLBACK) (void* context);

</#if>
void GENERIC_TIMER_Initialize(void);

uint64_t GENERIC_TIMER_CounterValueGet(void);

uint32_t GENERIC_TIMER_CounterFrequencyGet(void);

void GENERIC_TIMER_DelayMs(uint32_t delay_ms);

void GENERIC_TIMER_DelayUs(uint32_t delay_us);
<#if GENERIC_TIMER_INTERRUPT>

void GENERIC_TIMER_Start(void);

void GENERIC_TIMER_PeriodSet(uint64_t period);

uint64_t GENERIC_TIMER_PeriodGet(void);

void GENERIC_TIMER_Stop(void);
<#if RTOS_INTERRUPT_HANDLER == "">

void GENERIC_TIMER_RegisterCallback(GENERIC_TIMER_CALLBACK pCallback, void* pContext);
</#if>
</#if>

#ifdef __cplusplus
}
#endif //__cplusplus

#endif //PLIB_GENERIC_TIMER_H