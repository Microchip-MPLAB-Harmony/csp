/*******************************************************************************
  Periodic Interval Timer (${PERIPH_INSTANCE_NAME}) 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${PERIPH_INSTANCE_NAME?lower_case}.h

  Summary:
    Periodic Interval Timer (${PERIPH_INSTANCE_NAME}) PLIB.

  Description:
    This file declares the interface for the Periodic Interval Timer (${PERIPH_INSTANCE_NAME}).
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef _PLIB_${PERIPH_INSTANCE_NAME}_H
#define _PLIB_${PERIPH_INSTANCE_NAME}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include <stdbool.h>
#include <stdint.h>

#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************

<#if USE_INTERRUPT == true>
// *****************************************************************************
/* ${PERIPH_INSTANCE_NAME} Interrupt Callback Function definition.

  Summary:
    ${PERIPH_INSTANCE_NAME} Interrupt Callback Function definition.

  Description:
    Defines the function signature for the ${PERIPH_INSTANCE_NAME} interrupt callback.

*/

typedef void (*${PERIPH_INSTANCE_NAME}_CALLBACK)(uintptr_t context);
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void ${PERIPH_INSTANCE_NAME}_TimerInitialize(void);

  Summary:
    Initialize ${PERIPH_INSTANCE_NAME} registers per user config.

  Description:
    Initalize the period and, if configured, enable the counter and interrupt.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PERIPH_INSTANCE_NAME}_TimerInitialize(void);

// *****************************************************************************
/* Function:
    void ${PERIPH_INSTANCE_NAME}_TimerRestart(void);

  Summary:
   Restart the ${PERIPH_INSTANCE_NAME} counter.

  Description:
    Signal the ${PERIPH_INSTANCE_NAME} counter to stop, wait for it to stop, then restart the counter.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PERIPH_INSTANCE_NAME}_TimerRestart(void);

// *****************************************************************************
/* Function:
    void ${PERIPH_INSTANCE_NAME}_TimerStart(void);

  Summary:
   Start the ${PERIPH_INSTANCE_NAME} counter.

  Description:
    Start the ${PERIPH_INSTANCE_NAME} counter.  If interrupts are enabled an interrupt will occur
    every time the PIV value is reached.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PERIPH_INSTANCE_NAME}_TimerStart(void);

// *****************************************************************************
/* Function:
    void ${PERIPH_INSTANCE_NAME}_TimerStop(void);

  Summary:
   Stop the ${PERIPH_INSTANCE_NAME} counter.

  Description:
    Stop the ${PERIPH_INSTANCE_NAME} counter.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PERIPH_INSTANCE_NAME}_TimerStop(void);

// *****************************************************************************
/* Function:
   void ${PERIPH_INSTANCE_NAME}_TimerPeriodSet(uint32_t period);

  Summary:
   Set the timer period value.

  Description:
    Set the timer period value by programming the PIV field in the MR register.

  Precondition:
    None.

  Parameters:
   period       - The period (PIV) value of the ${PERIPH_INSTANCE_NAME}. 
  
  Returns:
    None.
*/
void ${PERIPH_INSTANCE_NAME}_TimerPeriodSet(uint32_t period);

// *****************************************************************************
/* Function:
    uint32_t ${PERIPH_INSTANCE_NAME}_TimerPeriodGet(void);

  Summary:
   Get the timer period value.

  Description:
    Return the current PIV value of the ${PERIPH_INSTANCE_NAME}.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint32_t ${PERIPH_INSTANCE_NAME}_TimerPeriodGet(void);

// *****************************************************************************
/* Function:
    uint32_t ${PERIPH_INSTANCE_NAME}_TimerCounterGet(void);

  Summary:
   Get the timer counter value.

  Description:
    Return the current counter (CPIV) value of the ${PERIPH_INSTANCE_NAME}.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint32_t ${PERIPH_INSTANCE_NAME}_TimerCounterGet(void);

// *****************************************************************************
/* Function:
    uint32_t ${PERIPH_INSTANCE_NAME}_TimerFrequencyGet(void);

  Summary:
    Get the timer clock frequency.

  Description:
    Return the clock frequency of the ${PERIPH_INSTANCE_NAME}.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint32_t ${PERIPH_INSTANCE_NAME}_TimerFrequencyGet(void);

<#if USE_INTERRUPT == false>
// *****************************************************************************
/* Function:
    bool ${PERIPH_INSTANCE_NAME}_TimerPeriodHasExpired(void);

  Summary:
    Return whether or not the Timer Period has expired.

  Description:
    Check the ${PERIPH_INSTANCE_NAME} Status register to determine if period has expired.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    True    - Indicates period has expired
    False   - Indicates period has not expired
*/
bool ${PERIPH_INSTANCE_NAME}_TimerPeriodHasExpired(void);
<#elseif USE_INTERRUPT == true>
// *****************************************************************************
/* Function:
    void ${PERIPH_INSTANCE_NAME}_DisableInterrupt();

  Summary:
    Disables the ${PERIPH_INSTANCE_NAME} interrupt.

  Description:
    Disables the generation of the ${PERIPH_INSTANCE_NAME} interrupt.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PERIPH_INSTANCE_NAME}_DisableInterrupt();

// *****************************************************************************
/* Function:
    void ${PERIPH_INSTANCE_NAME}_EnableInterrupt();

  Summary:
    Enables the ${PERIPH_INSTANCE_NAME} interrupt.

  Description:
    Enables the generation of the ${PERIPH_INSTANCE_NAME} interrupt.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PERIPH_INSTANCE_NAME}_EnableInterrupt();

// *****************************************************************************
/* Function:
    void ${PERIPH_INSTANCE_NAME}_DelayMs(uint32_t ms);

  Summary:
    Delays processing for x milliseconds.

  Description:
    Delays execution by using  the ${PERIPH_INSTANCE_NAME} timer to determine when given number of
    milliseconds has expired.  

  Precondition:
    ${PERIPH_INSTANCE_NAME} is configured and enabled.  The ${PERIPH_INSTANCE_NAME} interrupt is also enabled.

  Parameters:
    ms      - number of milliseconds to delay
  
  Returns:
    None.
*/
void ${PERIPH_INSTANCE_NAME}_DelayMs(uint32_t ms);

// *****************************************************************************
/* Function:
    void ${PERIPH_INSTANCE_NAME}_TimerCallbackSet(${PERIPH_INSTANCE_NAME}_CALLBACK callback, uintptr_t context);

  Summary:
    Register callback for ${PERIPH_INSTANCE_NAME} interrupt.

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
void ${PERIPH_INSTANCE_NAME}_TimerCallbackSet(${PERIPH_INSTANCE_NAME}_CALLBACK callback, uintptr_t context);

// *****************************************************************************
/* Function:
    void ${PERIPH_INSTANCE_NAME}_InterruptHandler(void);

  Summary:
    ${PERIPH_INSTANCE_NAME} Interrupt Handler.

  Description:
    Internal ${PERIPH_INSTANCE_NAME} interrupt handler called by interrupt controller.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void ${PERIPH_INSTANCE_NAME}_InterruptHandler(void);
</#if>

#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

#endif

/*******************************************************************************
 End of File
*/
