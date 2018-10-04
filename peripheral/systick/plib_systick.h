/*******************************************************************************
  SysTick Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_systick.h

  Summary
    SysTick peripheral library interface.

  Description
    This file defines the interface to the SysTick peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_SYSTICK_H    // Guards against multiple inclusion
#define PLIB_SYSTICK_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/
#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>
// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
/* Callback Function Pointer

   Summary:
    Defines the data type and function signature for the SysTick
    callback function.

   Description:
    This data type defines the function signature for the SysTick
    callback function. SysTick will call back the client's
    function with this signature.

   Precondition:
    SYSTICK_Initialize and SYSTICK_TimerCallbackSet must have been called to set the
    function to be called.

   Parameters:

    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

   Returns:
    None.

   Example:
    <code>
        ticks = 0;

        void MyCallback ( uintptr_t context )
        {
            ticks++;
        }

        SYSTICK_TimerCallbackSet(MyCallback, (uintptr_t) NULL);
    </code>

   Remarks:
    None.
*/
typedef void (*SYSTICK_CALLBACK)(uintptr_t context);


typedef struct
{
    SYSTICK_CALLBACK          callback;
    uintptr_t               context;
} SYSTICK_OBJECT ;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************
/* Function:
    void SYSTICK_Initialize( void )

   Summary:
     Initializes SysTick.

   Description:
     This function initializes the System Timer as configured by the user
     from within the MCC.

   Precondition:
     None.

   Parameters:
    None.

   Returns:
    None.

   Example:
    <code>
        SYSTICK_Initialize();
    </code>
*/
void SYSTICK_TimerInitialize ( void );

// *****************************************************************************
/* Function:
    void SYSTICK_TimerRestart( void )

   Summary:
     Restarts SysTick.

   Description:
     This function Restarts systick timer with preloaded configuration.

   Precondition:
     SYSTICK_Initialize should have been called to set up SysTick..

   Parameters:
    None.

   Returns:
    None.

   Example:
    <code>
        SYSTICK_Initialize();
        SYSTICK_TimerRestart();
    </code>
*/
void SYSTICK_TimerInitialize ( void );

// *****************************************************************************
/* Function:
    void SYSTICK_TimerStart( void )

   Summary:
     Starts System Timer.

   Description:
     This function resets and starts the System Timer

   Precondition:
     SYSTICK_Initialize should have been called to set up SysTick.

   Parameters:
    None.

   Returns:
    None.

   Example:
    <code>
        SYSTICK_Initialize();
        SYSTICK_TimerStart();
    </code>
*/
void SYSTICK_TimerStart ( void );

// *****************************************************************************
/* Function:
    void SYSTICK_TimerStop( void )

   Summary:
     Stops System Timer.

   Description:
     This function stops the System Timer

   Precondition:
     None.

   Parameters:
    None.

   Returns:
    None.

   Example:
    <code>
        SYSTICK_TimerStops();
    </code>
*/
void SYSTICK_TimerStop ( void );

// *****************************************************************************
/* Function:
    void SYSTICK_TimerPeriodSet( void )

   Summary:
     Set the SysTick Load Value

   Description:
     This function is used to update SysTick Load value

   Precondition:
     Systick should be stopped prior to setting up the new Load value
     by calling SYSTICK_TimerStop. This will make sure that the new value
     is used for the next Tick

   Parameters:
    None.

   Returns:
    None.

   Example:
    <code>
        SYSTICK_TimerStop();
        SYSTICK_TimerPeriodSet(0x00004567);
        SYSTICK_TimerStart();
    </code>
*/
void  SYSTICK_TimerPeriodSet ( uint32_t period );

// *****************************************************************************
/* Function:
    uint32_t SYSTICK_TimerPeriodGet( void )

   Summary:
    Get the SysTick Load Value

   Description:
     This function returns the SysTick Load value

   Precondition:
     None

   Parameters:
    None.

   Returns:
    32-bit period value.

   Example:
    <code>
        uint32_t period;

        period = SYSTICK_TimerPeriodGet();

    </code>
*/

uint32_t SYSTICK_TimerPeriodGet ( void );

// *****************************************************************************
/* Function:
    uint32_t SYSTICK_TimerCounterGet( void )

   Summary:
    Get the SysTick current Value

   Description:
     This function returns the SysTick current value

   Precondition:
     32-bit current value

   Parameters:
    None.

   Returns:
    None.

   Example:
    <code>
        uint32_t value;

        value = SYSTICK_TimerCounterGet();

    </code>
*/

uint32_t SYSTICK_TimerCounterGet ( void );

// *****************************************************************************
/* Function:
    uint32_t SYSTICK_TimerFrequencyGet( void )

   Summary:
    Get the SysTick frequency Value

   Description:
     This function returns the SysTick frequency value

   Precondition:
     None.

   Parameters:
    None.

   Returns:
    Systick Frequency value

   Example:
    <code>
        uint32_t frequency;

        frequency = SYSTICK_TimerFrequencyGet();

    </code>
*/
uint32_t SYSTICK_TimerFrequencyGet ( void );


// *****************************************************************************
/* Function:
    uint32_t SYSTICK_TimerPeriodHasExpired( void )

   Summary:
    Returns the current status of the systick

   Description:
     This function is used to identify if the Systick underflow has happened.
     This API can be used in polling mode

   Precondition:
     SYSTICK_Initialize should have been called to set up SysTick.

   Parameters:
    None.

   Returns:
    Systick status

   Example:
    <code>
        SYSTICK_Initialize();
        SYSTICK_TimerStart();

        if(SYSTICK_TimerPeriodHasExpired)
        {
            //application code
        }

    </code>
*/

bool SYSTICK_TimerPeriodHasExpired(void);


// *****************************************************************************
/* Function:
    void SYSTICK_DelayMs ( uint32_t ms )

   Summary:
    Blocking function to generate delay in milliseconds

   Description:
     This function generates accurate delay in units of milliseconds using SysTick timer in interrupt mode

   Precondition:
     SYSTICK_Initialize should have been called to set up SysTick in interrupt mode

   Parameters:
     The delay in units of milliseconds

   Returns:
     None

   Example:
    <code>
        SYSTICK_Initialize();
        SYSTICK_TimerStart();

        // Generates 100ms blocking delay
        SYSTICK_DelayMs(100)

    </code>
*/

void SYSTICK_DelayMs ( uint32_t ms )

// *****************************************************************************
/* Function:
    void  SYSTICK_TimerCallbackSet ( SYSTICK_CALLBACK callback, uintptr_t context )

   Summary:
    Sets the pointer to the function (and it's context) to be called when the
    given systick reaches 0.

   Description:
    This function sets the pointer to a client function to be called "back"
    when systick reaches 0. It also passes a context value
    (usually a pointer to a context structure) that is passed into the
    function when it is called.

    This function is available only in interrupt or non-blocking mode of
    operation.

   Precondition:
    SYSTICK_Initialize must have been called for the associated USART instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined
    by the SYSTICK_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function
    identified by the callback parameter.

   Returns:
    None.

  Example:
    <code>
        SYSTICK_TimerCallbackSet(MyCallback, &myData);
    </code>

  Remarks:
    The context parameter is ignored if the pointer passed is NULL.

    To disable the callback function, pass a NULL for the callback parameter.

*/
void SYSTICK_TimerCallbackSet ( SYSTICK_CALLBACK callback, uintptr_t context );


#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif