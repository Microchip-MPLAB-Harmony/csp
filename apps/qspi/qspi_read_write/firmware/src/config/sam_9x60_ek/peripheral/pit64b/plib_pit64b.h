/*******************************************************************************
  Periodic Interval Timer (PIT64B) 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pit64b.h

  Summary:
    Periodic Interval Timer (PIT64B) PLIB.

  Description:
    This file declares the interface for the Periodic Interval Timer (PIT64B).
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

#ifndef _PLIB_PIT64B_H
#define _PLIB_PIT64B_H


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

// *****************************************************************************
/* PIT64B Interrupt Callback Function definition.

  Summary:
    PIT64B Interrupt Callback Function definition.

  Description:
    Defines the function signature for the PIT64B interrupt callback.

*/

typedef void (*PIT64B_CALLBACK)(uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void PIT64B_TimerInitialize(void);

  Summary:
    Initialize PIT64B registers per user config.

  Description:
    Initalize the period and, if configured, enable the counter and interrupt.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void PIT64B_TimerInitialize(void);

// *****************************************************************************
/* Function:
    void PIT64B_TimerRestart(void);

  Summary:
   Restart the PIT64B counter.

  Description:
    Signal the PIT64B restart the counter.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void PIT64B_TimerRestart(void);

// *****************************************************************************
/* Function:
    void PIT64B_TimerStart(void);

  Summary:
   Start the PIT64B counter.

  Description:
    Start the PIT64B counter.  If interrupts are enabled an interrupt will occur
    every time the period value is reached.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void PIT64B_TimerStart(void);

// *****************************************************************************
/* Function:
    void PIT64B_TimerStop(void);

  Summary:
   Stop the PIT64B counter.

  Description:
    Stop the PIT64B counter.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void PIT64B_TimerStop(void);

// *****************************************************************************
/* Function:
   void PIT64B_TimerPeriodSet(uint64_t period);

  Summary:
   Set the timer period value.

  Description:
    Set the timer period value by programming the PIV field in the MR register.

  Precondition:
    None.

  Parameters:
   period       - The period (PIV) value of the PIT64B. 
  
  Returns:
    None.
*/
void PIT64B_TimerPeriodSet(uint64_t period);

// *****************************************************************************
/* Function:
    uint64_t PIT64B_TimerPeriodGet(void);

  Summary:
   Get the timer period value.

  Description:
    Return the period value of the PIT64B.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint64_t PIT64B_TimerPeriodGet(void);

// *****************************************************************************
/* Function:
    uint64_t PIT64B_TimerCounterGet(void);

  Summary:
   Get the timer counter value.

  Description:
    Return the current timer value of the PIT64B.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint64_t PIT64B_TimerCounterGet(void);


// *****************************************************************************
/* Function:
    uint32_t PIT64B_TimerFrequencyGet(void);

  Summary:
    Get the timer clock frequency.

  Description:
    Return the clock frequency of the PIT64B.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint32_t PIT64B_TimerFrequencyGet(void);

// *****************************************************************************
/* Function:
    void PIT64B_DelayMs(uint32_t ms);

  Summary:
    Delays processing for x milliseconds.

  Description:
    Delays execution by using  the PIT64B timer to determine when given number of
    milliseconds has expired.  

  Precondition:
    PIT64B is configured and enabled.  The PIT64B interrupt is also enabled.

  Parameters:
    ms      - number of milliseconds to delay
  
  Returns:
    None.
*/
void PIT64B_DelayMs(uint32_t ms);

// *****************************************************************************
/* Function:
    void PIT64B_TimerCallbackSet(PIT64B_CALLBACK callback, uintptr_t context);

  Summary:
    Register callback for PIT64B interrupt.

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
void PIT64B_TimerCallbackSet(PIT64B_CALLBACK callback, uintptr_t context);

// *****************************************************************************
/* Function:
    void PIT64B_InterruptHandler(void);

  Summary:
    PIT64B Interrupt Handler.

  Description:
    Internal PIT64B interrupt handler called by interrupt controller.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void PIT64B_InterruptHandler(void);

// *****************************************************************************
/* Function:
    void PIT64B_ClearInterrupt(void);

  Summary:
    PIT64B Clear Interrupt.

  Description:
    Clear the PIT64B interrupt.  Meant to be used by external
    interrupt handlers (e.g. FreeRTOS tick hanlder).

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
__STATIC_INLINE void PIT64B_ClearInterrupt(void)
{
    (uint32_t)PIT64B_REGS->PIT64B_ISR;
}

#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

#endif

/*******************************************************************************
 End of File
*/
