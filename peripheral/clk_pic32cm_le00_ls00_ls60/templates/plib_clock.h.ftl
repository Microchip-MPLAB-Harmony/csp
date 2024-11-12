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
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

    Register the callback function. Specify the context as NULL.
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

    Refer to the code example provided in the description of the
    OSCCTRL_CFD_CALLBACK function pointer type.

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
        This means the 32KHz clock has failed.
    }

    Register the callback function. Specify the context as NULL.
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

    Refer to the code example provided in the description of the
    OSC32KCTRL_CFD_CALLBACK function pointer type.

    </code>

  Remarks:
    None.
*/

void OSC32KCTRL_CallbackRegister (OSC32KCTRL_CFD_CALLBACK callback, uintptr_t context);

</#if>

<#if MCLK_INTENSET_CKRDY == true >

// *****************************************************************************
/* Main Clock Ready Callback Function Pointer Type.

  Summary:
    Defines the data type and function signature for the Main Clock Ready callback function.

  Description:
    This data type defines the function signature for the Main Clock Ready callback function.
    The Main Clock will call back the client's function with this signature when it
    needs to notify the client of oscillator failure.  The context parameter is
    an application defined data object specified at the time of registering the
    callback function and is returned in the context parameter of the callback
    function.

  Precondition:
    The CLOCK_Initialize() initialize function should have been called. The
    callback function should have been registered through
    MCLK_CallbackRegister() function.

  Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>

    void MyMCLKReadyCallback (uintptr_t context )
    {
        This means the MCLK clock is ready.
    }

    Register the callback function. Specify the context as NULL.
    MCLK_CallbackRegister(MyMCLKReadyCallback, NULL);

    </code>

  Remarks:
    None.
*/

typedef void (*MCLK_CKRDY_CALLBACK)(uintptr_t context);


// *****************************************************************************
/* Function:
    void MCLK_CallbackRegister (MCLK_CKRDY_CALLBACK callback, uintptr_t context)

  Summary:
    Register the function to be called when the MCLK is ready.

  Description:
    This function register the function to be called when the MCLK is ready.

  Precondition:
    The MCLK should have been configured in MHC and enabled.

  Parameters:
    callback - Pointer to the MCLK_CKRDY_CALLBACK type of function that will
    be called when a clock failure is detected. This can be NULL, in which case
    no callback will be generated.

    context - Context value to be passed into the callback function when it
    called.

  Returns:
    None.

  Example:
    <code>

    Refer to the code example provided in the description of the
    MCLK_CKRDY_CALLBACK function pointer type.

    </code>

  Remarks:
    None.
*/

void MCLK_CallbackRegister (MCLK_CKRDY_CALLBACK callback, uintptr_t context);

</#if>

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif /* PLIB_CLOCK_H */