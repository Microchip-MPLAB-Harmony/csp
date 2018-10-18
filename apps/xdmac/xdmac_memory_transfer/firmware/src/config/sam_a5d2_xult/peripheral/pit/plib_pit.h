/*******************************************************************************
  Periodic Interval Timer (PIT) 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pit.h

  Summary:
    Periodic Interval Timer (PIT) PLIB.

  Description:
    This file declares the interface for the Periodic Interval Timer (PIT).
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

#ifndef _PLIB_PIT_H
#define _PLIB_PIT_H


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


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void PIT_TimerInitialize(void);

  Summary:
    Initialize PIT registers per user config.

  Description:
    Initalize the period and, if configured, enable the counter and interrupt.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void PIT_TimerInitialize(void);

// *****************************************************************************
/* Function:
    void PIT_TimerRestart(void);

  Summary:
   Restart the PIT counter.

  Description:
    Signal the PIT counter to stop, wait for it to stop, then restart the counter.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void PIT_TimerRestart(void);

// *****************************************************************************
/* Function:
    void PIT_TimerStart(void);

  Summary:
   Start the PIT counter.

  Description:
    Start the PIT counter.  If interrupts are enabled an interrupt will occur
    every time the PIV value is reached.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void PIT_TimerStart(void);

// *****************************************************************************
/* Function:
    void PIT_TimerStop(void);

  Summary:
   Stop the PIT counter.

  Description:
    Stop the PIT counter.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void PIT_TimerStop(void);

// *****************************************************************************
/* Function:
   void PIT_TimerPeriodSet(uint32_t period);

  Summary:
   Set the timer period value.

  Description:
    Set the timer period value by programming the PIV field in the MR register.

  Precondition:
    None.

  Parameters:
   period       - The period (PIV) value of the PIT. 
  
  Returns:
    None.
*/
void PIT_TimerPeriodSet(uint32_t period);

// *****************************************************************************
/* Function:
    uint32_t PIT_TimerPeriodGet(void);

  Summary:
   Get the timer period value.

  Description:
    Return the current PIV value of the PIT.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint32_t PIT_TimerPeriodGet(void);

// *****************************************************************************
/* Function:
    uint32_t PIT_TimerCounterGet(void);

  Summary:
   Get the timer counter value.

  Description:
    Return the current counter (CPIV) value of the PIT.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint32_t PIT_TimerCounterGet(void);


// *****************************************************************************
/* Function:
    void PIT_TimerCompareSet(void);

  Summary:
   Set the timer comparison value.

  Description:
    Provide a future PIT count value for comparison purposes.  When PIT timer
    counter is greater than or equal to the value an event will be created.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
void PIT_TimerCompareSet( uint16_t compare );


// *****************************************************************************
/* Function:
    uint32_t PIT_TimerFrequencyGet(void);

  Summary:
    Get the timer clock frequency.

  Description:
    Return the clock frequency of the PIT.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.
*/
uint32_t PIT_TimerFrequencyGet(void);

// *****************************************************************************
/* Function:
    bool PIT_TimerPeriodHasExpired(void);

  Summary:
    Return whether or not the Timer Period has expired.

  Description:
    Check the PIT Status register to determine if period has expired.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    True    - Indicates period has expired
    False   - Indicates period has not expired
*/
bool PIT_TimerPeriodHasExpired(void);

#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

#endif

/*******************************************************************************
 End of File
*/
