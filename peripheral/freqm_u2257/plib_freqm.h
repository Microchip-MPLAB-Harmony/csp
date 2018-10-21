/*******************************************************************************
  FREQUENCY METER(FREQM) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_freqm.h

  Summary:
    FREQM Peripheral Library Interface Header File.

  Description:
    This file defines the interface to the FREQM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual plib_freqm<x> headers
    will be generated as required by the MHC (where <x> is the peripheral
    instance number).

    Every interface symbol has a lower-case 'x' in it following the "FREQM"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_FREQMx_H
#define PLIB_FREQMx_H

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
/* FREQM Error

  Summary:
    Identifies the possible FREQM module errors.

  Description:
    This enumeration identifies the possible erros that the FREQM module can
    generate. The FREQMx_ErrorGet() function will return a value of this type.

  Remarks:
    None.
*/

typedef enum
{
    /* No error has occurred */
    FREQM_ERROR_NONE = 0x0,

    /* A measurement overflow has occurred. Measured value is not valid. */
    FREQM_ERROR_OVERFLOW = 0x2

} FREQM_ERROR;

// *****************************************************************************
/* FREQM callback function Pointer

  Summary:
    Pointer to a FREQM CallBack function.

  Description:
    This data type defines the required function signature for the FREQM event
    handling callback function. Application must register a pointer to an event
    handling function whose function signature (parameter and return value
    types) match the types specified by this function pointer in order to
    receive event calls back from the FREQM PLIB.

    The parameters and return values are described here and a partial example
    implementation is provided.

  Parameters:
    context - Value identifying the context of the application that registered
    the event handling function

  Returns:
    None.

  Example:
    <code>

    // This is the callback function that is called when a frequency
    // measurement is complete.

    void FREQMCallBack(uintptr_t contextHandle)
    {
        if( FREQM_ERROR_NONE == FREQMx_ErrorGet())
        {
            // Frequency measurement was completed without any errors. We can
            // call the FREQMx_FrequencyGet() function to obtain the measured
            // value. 

            measuredFrequency = FREQMx_FrequencyGet();
        }
    }
    
    FREQMx_Initialize();
    FREQMx_CallbackRegister(&FREQMCallBack, NULL);
    FREQMx_MeasurementStart();

    </code>

  Remarks:
    The context parameter can contain a handle to the client context, provided
    at the time the event handling function was  registered using the
    FREQM_CallbackRegister function. This context handle value is passed back to
    the client as the "context" parameter.  It can be any value (such as a
    pointer to the client's data) necessary to identify the client context or
    instance  of the client that made the data exchange request.

    The callback function executes in the driver peripheral interrupt context
    when the driver is configured for interrupt mode operation.  It is
    recommended of the application to not perform process intensive or blocking
    operations with in this function.
*/

typedef void (*FREQM_CALLBACK)(uintptr_t context);

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
    void FREQMx_Initialize(void)

  Summary:
    Initializes FREQMx module.

  Description:
    This function initializes FREQM module with the values configured in MHC
    GUI. Once the peripheral is initialized, measurement APIs can be called to
    perfrom frequency measurement. 

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        FREQMx_Initialize();
    </code>

  Remarks:
    This function must be called before any other FREQM function is called.
*/

void FREQMx_Initialize(void);

// *****************************************************************************
/* Function:
    bool FREQMx_MeasurementStart(void)

  Summary:
    This function starts the frequency measurement.

  Description:
    This function starts the frequency measurement. This function is always
    non-blocking. Calling this function when a frequency measurement is already
    in progress will result in a functional no operation. The FREQMx_IsBusy()
    function will return true when a frequency measurement is in progress. The
    completion of the measurement operation is indicated by the FREQMx_IsBusy()
    function returing false or a registered callback function being called.

  Precondition:
    FREQMx module should be initialized with the required configuration
    parameters from the MHC GUI in the FREQM_Initialize() function

  Parameters:
    None

  Returns:
    Returns false if the peripheral is busy

  Example:
    <code>
        bool status = false;
        status = FREQMx_MeasurementStart();
    </code>

  Remarks:
    None.
*/

bool FREQMx_MeasurementStart(void);

// *****************************************************************************
/* Function:
    void FREQMx_CallbackRegister(FREQM_CALLBACK freqmcallback,
                                                            uintptr_t context)

  Summary:
    Allows application to register a callback function.

  Description:
    This function allows the application to register a callback function that
    will be called when a frequency measurement operation has completed. The
    callback feature is only available if the Interrupt operation in the GUI was
    enabled.  If a callback mechanism is desired, then a callback function
    should be registerd via this function before starting a frequency
    measurement. The application can read the measured frequency value and the
    check for errors in the callback function. Calling this function at any time
    with callback function as NULL will disable the callback feature.

  Precondition:
    The FREQMx_Initialize function must have been called. Interrupt option in
    MHC should have been enabled.

  Parameters:
    callBack - Pointer to an application callback function.

    context - The value of parameter will be passed back to the application
    unchanged, when the callback function is called.  It can be used to identify
    any application specific data object that identifies the instance of the
    client module (for example, it may be a pointer to the client modules state
    structure).

  Returns:
    None.

  Example:
    <code> 
    FREQM_ERROR errorValue = FREQM_ERROR_NONE;
    uint32_t measuredFrequency = 0;

    void FREQMCallbackFunction(uintptr_t contextHandle)
    {
        if ( FREQM_ERROR_OVERFLOW == FREQMx_ErrorGet())
        {
            // indication of the overflow condition
        }
        else
        {
            measuredFrequency = FREQMx_FrequencyGet();
        }
    }
 
    FREQMx_Initialize();
    FREQMx_CallbackRegister(FREQMCallbackFunction, NULL);
    FREQMx_MeasurementStart();
    
    </code>

  Remarks:
    The callback mechanism allows the application to implement an event based
    interaction with the library. The application can altenatively use the
    FREQMx_IsBusy function to implement a polling based logic.
*/

void FREQMx_CallbackRegister(FREQM_CALLBACK freqmcallback, uintptr_t context);

// *****************************************************************************
/* Function:
    bool FREQMx_IsBusy(void)

  Summary:
    Returns the measurement status of an on-going frequency measurement
    operation.

  Description:
    This function returns the measurement status of an on-going frequency
    measurement operation.  The function returns true when the
    FREQMx_MeasurementStart() function has been called to start a measurement.
    It returns false, when the  measurement operation has completed.  The
    function should be called after measurement operation was initiated to poll
    the completion of the measurement operation. It also can be used as
    alternate to callback.

  Precondition:
    The FREQMx_Initialize() function must have been called.

  Parameters:
    None.

  Returns:
    true - Module is busy with a measurement.

    false - Module is not busy with a measurement.

  Example:
    <code>
    
    FREQMx_MeasurementStart();
   
    // Wait till the measurement is complete.
    while(FREQMx_IsBusy());

    </code>

  Remarks:
    None.
*/

bool FREQMx_IsBusy(void);

// *****************************************************************************
/* Function:
    uint32_t FREQMx_FrequencyGet(void)

  Summary:
    Returns the measured frequency in Hz.

  Description:
    This function returns the measured frequency in Hz. It should be called when
    a frequency measurement is complete and no errors have occurred. This
    function is non-blocking. In this mode, the function should be called only
    after a callback function was called. The return value of the function is
    only valid if the FREQMx_ErrorGet() function returns FREQM_ERROR_NONE.

  Precondition:
    FREQMx_Initialize() and FREQM_MeasurementStart() functions should be called.

  Parameters:
    None.

  Returns:
    uint32_t - frequency value of the measured clock. The value is only valid if
    the FREQMx_ErrorGet() function returns FREQM_ERROR_NONE.

  Example:
    <code>

    // Refer to the code example of FREQMx_CallbackRegister() function for
    // guidance on interrupt based operation.

    // The following code snippet shows an exampl of non-interrupt based
    // operation.

    FREQMx_Initialize();
    FREQM_MeasurementStart()

    // Wait till the measurement is complete.
    while(FREQMx_IsBusy());

    if(FREQM_ERROR_NONE == FREQMx_ErrorGet())
    {
        measuredFrequency = FREQMx_FrequencyGet();
        // This means there are no errors and the value contained in
        // measuredFrequency is valid.
    }
    </code>

  Remarks:
    None.
*/

uint32_t FREQMx_FrequencyGet(void);

// *****************************************************************************
/* Function:
    FREQM_ERROR FREQMx_ErrorGet(void)

  Summary:
    Returns error that may have occurred during the frequency measurement
    process.

  Description:
    This function returns the error that may have occurred during the frequency
    measurement process. The function returns the error for the last completed
    operation. The value returned by the FREQMx_FrequencyGet() function is valid
    only if this function returns FREQM_ERROR_NONE.

  Precondition:
    FREQMx_Initialize() and FREQM_MeasurementStart() functions should be called.

  Parameters:
    None.

  Returns:
    Errors occurred as listed by FREQMx_ERROR.

  Example:
    <code>
    if (FREQM_ERROR_OVERFLOW  == FREQMx_ErrorGet())
    {
        //Handle overflow error here
    }
    else
    {
        measuredFrequency = FREQMx_FrequencyGet();
    }
    </code>

  Remarks:
    None.
*/

FREQM_ERROR FREQMx_ErrorGet(void);

#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif

#endif /* PLIB_FREQMx_H */
