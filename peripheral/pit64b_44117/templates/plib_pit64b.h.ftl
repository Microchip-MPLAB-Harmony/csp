/*******************************************************************************
  Periodic Interval Timer (${PIT64B_INSTANCE_NAME}) 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${PIT64B_INSTANCE_NAME?lower_case}.h

  Summary:
    Periodic Interval Timer (${PIT64B_INSTANCE_NAME}) PLIB.

  Description:
    This file declares the interface for the Periodic Interval Timer (${PIT64B_INSTANCE_NAME}).
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

#ifndef _PLIB_${PIT64B_INSTANCE_NAME}_H
#define _PLIB_${PIT64B_INSTANCE_NAME}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include <stdbool.h>
#include <stdint.h>

#include "device.h" // static inline macro

#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************

<#if ENABLE_INTERRUPT == true>
// *****************************************************************************
/* ${PIT64B_INSTANCE_NAME} Interrupt Callback Function definition.

  Summary:
    ${PIT64B_INSTANCE_NAME} Interrupt Callback Function definition.

  Description:
    Defines the function signature for the ${PIT64B_INSTANCE_NAME} interrupt callback.

*/

typedef void (*${PIT64B_INSTANCE_NAME}_CALLBACK)(uintptr_t context);
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void ${PIT64B_INSTANCE_NAME}_TimerInitialize(void);

  Summary:
    Initialize ${PIT64B_INSTANCE_NAME} registers per user config.

  Description:
    Initalize the period and, if configured, enable the counter and interrupt.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PIT64B_INSTANCE_NAME}_TimerInitialize(void);

// *****************************************************************************
/* Function:
    void ${PIT64B_INSTANCE_NAME}_TimerRestart(void);

  Summary:
   Restart the ${PIT64B_INSTANCE_NAME} counter.

  Description:
    Signal the ${PIT64B_INSTANCE_NAME} restart the counter.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PIT64B_INSTANCE_NAME}_TimerRestart(void);

// *****************************************************************************
/* Function:
    void ${PIT64B_INSTANCE_NAME}_TimerStart(void);

  Summary:
   Start the ${PIT64B_INSTANCE_NAME} counter.

  Description:
    Start the ${PIT64B_INSTANCE_NAME} counter.  If interrupts are enabled an interrupt will occur
    every time the period value is reached.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PIT64B_INSTANCE_NAME}_TimerStart(void);

// *****************************************************************************
/* Function:
    void ${PIT64B_INSTANCE_NAME}_TimerStop(void);

  Summary:
   Stop the ${PIT64B_INSTANCE_NAME} counter.

  Description:
    Stop the ${PIT64B_INSTANCE_NAME} counter.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PIT64B_INSTANCE_NAME}_TimerStop(void);

// *****************************************************************************
/* Function:
   void ${PIT64B_INSTANCE_NAME}_TimerPeriodSet(uint64_t period);

  Summary:
   Set the timer period value.

  Description:
    Set the timer period value by programming the PIV field in the MR register.

  Precondition:
    None.

  Parameters:
   period       - The period (PIV) value of the ${PIT64B_INSTANCE_NAME}. 
  
  Returns:
    None.
*/
void ${PIT64B_INSTANCE_NAME}_TimerPeriodSet(uint64_t period);

// *****************************************************************************
/* Function:
    uint64_t ${PIT64B_INSTANCE_NAME}_TimerPeriodGet(void);

  Summary:
   Get the timer period value.

  Description:
    Return the period value of the ${PIT64B_INSTANCE_NAME}.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint64_t ${PIT64B_INSTANCE_NAME}_TimerPeriodGet(void);

// *****************************************************************************
/* Function:
    uint64_t ${PIT64B_INSTANCE_NAME}_TimerCounterGet(void);

  Summary:
   Get the timer counter value.

  Description:
    Return the current timer value of the ${PIT64B_INSTANCE_NAME}.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint64_t ${PIT64B_INSTANCE_NAME}_TimerCounterGet(void);


// *****************************************************************************
/* Function:
    uint32_t ${PIT64B_INSTANCE_NAME}_TimerFrequencyGet(void);

  Summary:
    Get the timer clock frequency.

  Description:
    Return the clock frequency of the ${PIT64B_INSTANCE_NAME}.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint32_t ${PIT64B_INSTANCE_NAME}_TimerFrequencyGet(void);

<#if ENABLE_INTERRUPT == false>
// *****************************************************************************
/* Function:
    bool ${PIT64B_INSTANCE_NAME}_TimerPeriodHasExpired(void);

  Summary:
    Return whether or not the Timer Period has expired.

  Description:
    Check the ${PIT64B_INSTANCE_NAME} Status register to determine if period has expired.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    True    - Indicates period has expired
    False   - Indicates period has not expired
*/
bool ${PIT64B_INSTANCE_NAME}_TimerPeriodHasExpired(void);
<#elseif ENABLE_INTERRUPT == true>
// *****************************************************************************
/* Function:
    void ${PIT64B_INSTANCE_NAME}_DelayMs(uint32_t ms);

  Summary:
    Delays processing for x milliseconds.

  Description:
    Delays execution by using  the ${PIT64B_INSTANCE_NAME} timer to determine when given number of
    milliseconds has expired.  

  Precondition:
    ${PIT64B_INSTANCE_NAME} is configured and enabled.  The ${PIT64B_INSTANCE_NAME} interrupt is also enabled.

  Parameters:
    ms      - number of milliseconds to delay
  
  Returns:
    None.
*/
void ${PIT64B_INSTANCE_NAME}_DelayMs(uint32_t ms);

// *****************************************************************************
/* Function:
    void ${PIT64B_INSTANCE_NAME}_TimerCallbackSet(${PIT64B_INSTANCE_NAME}_CALLBACK callback, uintptr_t context);

  Summary:
    Register callback for ${PIT64B_INSTANCE_NAME} interrupt.

  Description:
    When the timer interrupt occurs the given callback will called with the
    given context.

  Precondition:
    None.

  Parameters:
    callback    - Callback function
    context     - paramter to callback function
  
  Returns:
    None.
*/
void ${PIT64B_INSTANCE_NAME}_TimerCallbackSet(${PIT64B_INSTANCE_NAME}_CALLBACK callback, uintptr_t context);

// *****************************************************************************
/* Function:
    void ${PIT64B_INSTANCE_NAME}_ClearInterrupt(void);

  Summary:
    ${PIT64B_INSTANCE_NAME} Clear Interrupt.

  Description:
    Clear the ${PIT64B_INSTANCE_NAME} interrupt.  Meant to be used by external
    interrupt handlers (e.g. FreeRTOS tick hanlder).

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
__STATIC_INLINE void ${PIT64B_INSTANCE_NAME}_ClearInterrupt(void)
{
    (uint32_t)${PIT64B_INSTANCE_NAME}_REGS->PIT64B_ISR;
}
</#if>

#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

#endif

/*******************************************************************************
 End of File
*/
