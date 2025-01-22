/*******************************************************************************
  TMR Peripheral Library Interface Header Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_tmr${TMR_INSTANCE_NUMBER}.h

  Summary
    TMR${TMR_INSTANCE_NUMBER} peripheral library header source file.

  Description
    This file implements the interface to the TMR peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*/

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

#ifndef PLIB_TMR${TMR_INSTANCE_NUMBER}_H
#define PLIB_TMR${TMR_INSTANCE_NUMBER}_H

#include <stddef.h>
#include <stdint.h>
#include "device.h"
#include "plib_tmr_common.h"


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup  timer
 * @brief    Initializes the TMR module
 * @return   none
 */
</#if>

void TMR${TMR_INSTANCE_NUMBER}_Initialize(void);
<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup  timer
 * @brief    De-initializes the TMR module
 * @return   none
 */
</#if>

void TMR${TMR_INSTANCE_NUMBER}_Deinitialize(void);
<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup  timer
 * @brief    Starts the timer
 * @return   none
 */
</#if>

void TMR${TMR_INSTANCE_NUMBER}_Start(void);
<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup  timer
 * @brief    Stops the timer
 * @return   none
 */
</#if>
 
void TMR${TMR_INSTANCE_NUMBER}_Stop(void);
<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup    timer
 * @brief      Sets the timer period count value
 * @param[in]  period - number of clock counts
 * @return     none
 */
</#if>
 
void TMR${TMR_INSTANCE_NUMBER}_PeriodSet(uint32_t period);
<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup    timer
 * @brief      Returns the timer period count value
 * @return     Number of clock counts
 */
</#if>
 
uint32_t TMR${TMR_INSTANCE_NUMBER}_PeriodGet(void);
<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup    timer
 * @brief      Returns the timer elasped time value
 * @return     Elapsed count value of the timer
 */
</#if>
 
uint32_t TMR${TMR_INSTANCE_NUMBER}_CounterGet(void);
<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup    timer
 * @brief      Returns the timer clock frequency
 * @return     Timer clock frequency
 */
</#if>

uint32_t TMR${TMR_INSTANCE_NUMBER}_FrequencyGet(void);
<#if TMR_INTERRUPT_MODE == true>
<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup    timer
 * @brief      Enables the timer interrupt
 */
</#if>

void TMR${TMR_INSTANCE_NUMBER}_InterruptEnable(void);
<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup    timer
 * @brief      Disables the timer interrupt
 */
</#if>

void TMR${TMR_INSTANCE_NUMBER}_InterruptDisable(void);
<#assign generateDoxygen = true>
<#if generateDoxygen>
/**
 * @ingroup    timer
 * @brief      This function allows application to register an event handling 
 *             function for the PLIB to call back when external interrupt occurs. 
 *             At any point if application wants to stop the callback, 
 *             it can call this function with "callback" value as NULL.
 * @param[in]  callback  - Pointer to the event handler function implemented by the user
 * @param[in]  context   - The value of parameter will be passed back to the 
 *                         application unchanged, when the eventHandler function is called. 
 *                         It can be used to identify any application specific value.
 */
</#if>

void TMR${TMR_INSTANCE_NUMBER}_CallbackRegister( TMR_CALLBACK callback_fn, uintptr_t context );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }
#endif
// DOM-IGNORE-END

#endif /* PLIB_TMR${TMR_INSTANCE_NUMBER}_H */
