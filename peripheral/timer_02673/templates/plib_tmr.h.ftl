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
* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
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

#define TIMER_CLOCK_FREQUENCY          ${TIMER_CLOCK_FREQ}

<#if TMR_INTERRUPT_MODE == true>
#define TMR_INTERRUPT_PERIOD_IN_US     ${TIMER_PERIOD_US}
typedef struct
{
    uint32_t start;
    uint32_t count;
} TMR_TIMEOUT;
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END


/**
 * @brief    Initializes the TMR module
 *
 * @details  This function initializes the TMR registers based on
 * the selections made in Configuration Options
 *
 * @pre      None
 *
 * @param    None
 *
 * @return   None
 */
void TMR${TMR_INSTANCE_NUMBER}_Initialize(void);

/**
 * @brief    De-initializes the TMR module
 *
 * @details This function de-initializes the timer registers to POR values
 *
 * @pre     None
 *
 * @param   None
 *
 * @return   None
 */
void TMR${TMR_INSTANCE_NUMBER}_Deinitialize(void);

/**
 * @brief    Starts the timer
 *
 * @details  This function starts the timer
 *
 * @pre      Timer should be initialized properly
 *
 * @param    None
 *
 * @return   None
 */
void TMR${TMR_INSTANCE_NUMBER}_Start(void);

/**
 * @brief    Stops the timer
 *
 * @details  This function stops the timer
 *
 * @pre      None
 *
 * @param    None
 *
 * @return   None
 */
void TMR${TMR_INSTANCE_NUMBER}_Stop(void);

/**
 * @brief      Sets the timer period count value
 *
 * @details    This function sets the timer period count value
 *
 * @pre        Timer should be initialized properly
 *
 * @param[in]  period - number of clock counts
 *
 * @return     None
 */
void TMR${TMR_INSTANCE_NUMBER}_PeriodSet(uint32_t period);

/**
 * @brief      Returns the timer period count value
 *
 * @details    This function returns the period count value
 *
 * @pre        Timer should be initialized properly
 *
 * @param      None
 *
 * @return     Number of clock counts
 */
uint32_t TMR${TMR_INSTANCE_NUMBER}_PeriodGet(void);

/**
 * @brief      Returns the timer elasped time value
 *
 * @details    This function returns the timer elasped time value
 *
 * @pre        Timer should be initialized properly
 *
 * @param      None
 *
 * @return     Elapsed count value of the timer
 */
uint32_t TMR${TMR_INSTANCE_NUMBER}_CounterGet(void);

/**
 * @brief      Returns the timer clock frequency
 *
 * @details    This function returns the timer clock ffrequency
 *
 * @pre        Timer should be initialized properly
 *
 * @param      None
 *
 * @return     Timer clock frequency
 */
uint32_t TMR${TMR_INSTANCE_NUMBER}_FrequencyGet(void);
<#if TMR_INTERRUPT_MODE == true>

/**
 * @brief      Returns current tick count
 *
 * @details    This function returns current tick count
 *
 * @pre        Timer should be initialized properly
 *
 * @param      None
 *
 * @return     Current tick count
 *
 * @remarks    None
 */
uint32_t TMR${TMR_INSTANCE_NUMBER}_GetTickCounter(void);

/**
 * @brief      Stores current tick count and delay value in the timeout
 *
 * @details    This function stores current tick count and delay value in the timeout
 *
 * @pre        Timer should be initialized properly
 *
 * @param      timeout - timeout structure stores current tick count and delay value
 * @param      delay_ms - Delay value in millisecond
 *
 * @return     None
 *
 * @remarks    None
 */
void TMR${TMR_INSTANCE_NUMBER}_StartTimeOut (TMR_TIMEOUT* timeout, uint32_t delay_ms);

/**
 * @brief      Resets current tick count in the timeout
 *
 * @details    This function resets current tick count in the timeout
 *
 * @pre        Timer should be initialized properly
 *
 * @param      timeout - timeout structure stores current tick count
 *
 * @return     None
 *
 * @remarks    None
 */
void TMR${TMR_INSTANCE_NUMBER}_ResetTimeOut (TMR_TIMEOUT* timeout);

/**
 * @brief      Checks for timeout
 *
 * @details    This function checks for timeout
 *
 * @pre        Timer should be initialized properly
 *
 * @param      timeout - Pointer to timeout structure
 *
 * @return     Returns true if timeout occurred otherwise false
 *
 * @remarks    None
 */
bool TMR${TMR_INSTANCE_NUMBER}_IsTimeoutReached (TMR_TIMEOUT* timeout);

/**
 * @brief      Enables the timer interrupt
 *
 * @details    This function enables the timer interrupt
 *
 * @pre        Timer should be initialized properly
 *
 * @param      None
 *
 * @remarks   None
 */
void TMR${TMR_INSTANCE_NUMBER}_InterruptEnable(void);

/**
 * @brief      Disables the timer interrupt
 *
 * @details    This function disables the timer interrupt
 *
 * @pre        Timer should be initialized properly
 *
 * @param      None
 *
 * @remarks    None
 */
void TMR${TMR_INSTANCE_NUMBER}_InterruptDisable(void);

/**
 * @brief      Registers a callback function
 * @details    This function allows application to register an event handling
 *             function for the PLIB to call back when external interrupt occurs.
 *             At any point if application wants to stop the callback,
 *             it can call this function with "callback" value as NULL.
 *
 * @pre        Timer should be initialized properly
 *
 * @param[in]  callback  - Pointer to the event handler function implemented by the user
 * @param[in]  context   - The value of parameter will be passed back to the
 *                         application unchanged, when the eventHandler function is called.
 *                         It can be used to identify any application specific value.
 *
 * @return      None
 */
void TMR${TMR_INSTANCE_NUMBER}_CallbackRegister( TMR_CALLBACK callback_fn, uintptr_t context );
<#else>
/**
 * @brief      Checks period expiration
 *
 * @details    This function returns the status of expiration of period
 *
 * @pre        Timer should be initialized properly
 *
 * @param      None
 *
 * @return     Status of period match
 */
bool TMR${TMR_INSTANCE_NUMBER}_PeriodHasExpired(void);
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }
#endif
// DOM-IGNORE-END

#endif /* PLIB_TMR${TMR_INSTANCE_NUMBER}_H */
