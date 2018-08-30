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

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip micro controller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#ifndef PLIB_CLOCK_H
#define PLIB_CLOCK_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include <stdint.h>
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
    void CLOCK_Initialize (void);

  Summary:
    Initializes all the modules related to the system clock.

  Description:
    This function initializes the clock as defined by the MHC and Clock Manager
    selections. The function will configure the NVM Flash Wait states based on
    the configured CPU operational frequency. It will then configure the
    oscillators.

    For each of the clock sources (External Oscillator, Digital Phase Locked
    Loop, Internal 48MHz Oscillator, External 32KHz oscillator and the Internal
    32KHz oscillator) enabled in MHC, the function will configure the clock
    settings and will then wait till the clock is ready. In case of DPLL, the
    function will wait till a lock is obtained.

    The function will then configure the Generic clock generators based on MHC
    configurations. If a Generic Clock is enabled in MHC, this will be enabled
    in the CLOCK_Initialize() function. The function will apply the CPU clock
    divider and will wait for the Main Clock module to get ready. If the Main
    Clock to the Peripheral APB and AHB interfaces was enabled in MHC, these
    will be enabled in the CLOCK_Initialize() function. If the Peripheral Clock
    Channels were enabled in MHC, these will be enabled in the
    CLOCK_Initialize() function.

    The peripheral AHB and APB main clock and peripheral channel clocks will be
    enabled when the peripheral specific initialize functions are called. This
    will override the setting in MHC. The Generic Clock Generator source for
    desired peripheral channel must be configured in MHC.

  Precondition:
    MHC GUI should be configured with the right values. Incorrect configuration
    of the Clock will result in incorrect peripheral behavior or a non
    functional device.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        CLOCK_Initialize();
    </code>

  Remarks:
    This function should be called before calling other Clock library functions.
*/

void CLOCK_Initialize (void);

<#if CONFIG_CLOCK_XOSC_CFDEN == true>

// *****************************************************************************
/* External Oscillator Callback Function Pointer Type.

  Summary:
    Defines the data type and function signature for the External Oscillator
    callback function.

  Description:
    This data type defines the function signature for the External Oscillator
    callback function. The External Oscillator will call back the client's
    function with this signature when it needs to notify the oscillator failure. 
	The context parameter is an application defined  data object specified 
	at the time of registering the callback function and is returned in the 
	context parameter of the callback function.

  Precondition:
    The CLOCK_Initialize() initialize function should have been called. The
    callback function should have been registered through
    OSCCTRL_CallbackRegister() function.

  Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>

    void MyOscillatorCallback (uintptr_t context )
    {

    }

    // Register the callback function. Specify the context as NULL.
    OSCCTRL_CallbackRegister(MyOscillatorCallback, NULL);

    </code>

  Remarks:
    None.
*/

typedef void (*OSCCTRL_CFD_CALLBACK)(uintptr_t context);

// *****************************************************************************
/* Function:
    void OSCCTRL_CallbackRegister (uintptr_t context);

  Summary:
    Register the function to be called when an External Oscillator or DPLL event
    is generated.

  Description:
    This function registers the callback function to be called when the External
    Oscillator has failed. 

  Precondition:
    The External Oscillator and/or should have been configured in MHC and
    enabled.

  Parameters:
    callback - Pointer to the OSCCTRL_CFD_CALLBACK type of function that will be
    called when the oscillator failed.

    context - Context value to be passed into the callback function when it
    called.

  Returns:
    None.

  Example:
    <code>

    //Refer to the code example provided in the description of the
    //OSCCTRL_CFD_CALLBACK function pointer type.

    </code>

  Remarks:
    None.
*/

void OSCCTRL_CallbackRegister (OSCCTRL_CFD_CALLBACK callback, uintptr_t context);

</#if>

<#if XOSC32K_CFDEN == true >

// *****************************************************************************
/* External 32KHz Oscillator Clock Failure Callback Function Pointer Type.

  Summary:
    Defines the data type and function signature for the External 32KHz Oscillator
    clock failure detection callback function.

  Description:
    This data type defines the function signature for the External 32KHz
    Oscillator clock failure detection callback function. The External 32KHz
    Oscillator will call back the client's function with this signature when it
    needs to notify the client of oscillator failure.  The context parameter is
    an application defined data object specified at the time of registering the
    callback function and is returned in the context parameter of the callback
    function.

  Precondition:
    The CLOCK_Initialize() initialize function should have been called. The
    callback function should have been registered through
    OSC32KCTRL_CallbackRegister() function.

  Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>

    void MyOscillatorFailureCallback (uintptr_t context )
    {
        // This means the 32KHz clock has failed.
    }

    // Register the callback function. Specify the context as NULL.
    OSC32KCTRL_CallbackRegister(MyOscillatorFailureCallback, NULL);

    </code>

  Remarks:
    None.
*/

typedef void (*OSC32KCTRL_CFD_CALLBACK)(uintptr_t context);


// *****************************************************************************
/* Function:
    void OSC32KCTRL_CallbackRegister (OSC32KCTRL_CFD_CALLBACK callback,
                                                    uintptr_t context);

  Summary:
    Register the function to be called when the 32KHz External Oscillator has
    failed.

  Description:
    This function register the function to be called when the 32KHz External
    Oscillator has failed.

  Precondition:
    The 32KHz External Oscillator should have been configured in MHC and
    enabled.

  Parameters:
    callback - Pointer to the OSC32KCTRL_CFD_CALLBACK type of function that will
    be called when a clock failure is detected. This can be NULL, in which case
    no callback will be generated.

    context - Context value to be passed into the callback function when it
    called.

  Returns:
    None.

  Example:
    <code>

    //Refer to the code example provided in the description of the
    //OSC32KCTRL_CFD_CALLBACK function pointer type.

    </code>

  Remarks:
    None.
*/

void OSC32KCTRL_CallbackRegister (OSC32KCTRL_CFD_CALLBACK callback, uintptr_t context);

</#if>

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif /* PLIB_CLOCK_H */

