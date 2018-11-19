/*******************************************************************************
  FREQUENCY METER(FREQM) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_freqm.h

  Summary:
    FREQM PLIB Header File.

  Description:
    This file defines the interface to the FREQM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

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

#ifndef PLIB_FREQM_H    // Guards against multiple inclusion
#define PLIB_FREQM_H

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
    This enumeration identifies the possible errors that the FREQM module can
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
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
this interface.
*/

// *****************************************************************************
/* Function:
    void FREQM_Initialize (void);

  Summary:
    Initializes FREQM module.

  Description:
    This function initializes FREQM module with the values
	configured in MHC GUI. Once the peripheral is initialized, measurement APIs
	can be called to perform frequency measurement.

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        FREQM_Initialize();
    </code>

  Remarks:
    This function must be called before any other FREQM function is called.
*/

void FREQM_Initialize (void);

// *****************************************************************************
/* Function:
    void FREQM_MeasurementStart();

  Summary:
    This function starts the frequency measurement.

  Description:
    This function starts the frequency measurement. This function is always
    non-blocking. Calling this function when a frequency measurement is already
    in progress will result in a functional no operation. The FREQM_IsBusy()
    function will return true when a frequency measurement is in progress. The
    completion of the measurement operation is indicated by the FREQM_IsBusy()
    function returning false or a registered callback function being called.

    Starting a measurement will reset all module errors and other status flags.

  Precondition:
    FREQM module should be initialized with the required configuration
    parameters from the MHC GUI in the FREQM_Initialize() function

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        FREQM_MeasurementStart();
    </code>

  Remarks:
    None.
*/

void FREQM_MeasurementStart(void);


// *****************************************************************************
/* Function:
    uint32_t FREQM_FrequencyGet()

  Summary:
    Returns the measured frequency in Hz.

  Description:
    This function returns the measured frequency in Hz. It should be called when
    a frequency measurement is complete and no errors have occurred. This
    function is non-blocking when the library is generated for interrupt
    operation. In interrupt mode, the function should be called only after a
    callback function was called or after the FREQM_IsBusy()
    function returns false indicating that an on-going frequency measurement
    operation has completed.

    The function will block when the library is generated for non-interrupt
    operation.  The function will block till the frequency measurement operation
    has completed. In this case, the return value of the function is only valid
    if the FREQM_ErrorGet() function returns FREQM_ERROR_NONE.

  Precondition:
    FREQM_Initialize() and FREQM_MeasurementStart functions should
    be called.

  Parameters:
    None.

  Returns:
    uint32_t - frequency value of the measured clock. The value is only valid if
    the FREQM_ErrorGet() function returns FREQM_ERROR_NONE.

  Example:
    <code>

    // Refer to the code example of FREQM_CallbackRegister() function for
    // guidance on interrupt based operation.

    // The following code snippet shows an example of non-interrupt based
    // operation.

    FREQM_Initialize();
    FREQM_MeasurementStart()

    // The following function call will block.
    measuredFrequency = FREQM_FrequencyGet();

    if(FREQM_ErrorGet() == FREQM_ERROR_NONE)
    {
        // This means there are no errors and the value contained in
        // measuredFrequency is valid.
    }
    </code>

  Remarks:
    None.
*/

uint32_t FREQM_FrequencyGet();

// *****************************************************************************
/* Function:
    FREQM_ERROR FREQM_ErrorGet( void )

  Summary:
    Returns error that may have occurred during the frequency measurement
    process.

  Description:
    This function returns the error that may have occurred during the frequency
    measurement process. The function returns the error for the last completed
    operation. The value returned by the FREQM_FrequencyGet()
    function is valid only if this function returns FREQM_ERROR_NONE.

  Precondition:
    FREQM_Initialize and FREQM_MeasurementStart
    functions must have been called.

  Parameters:
    None.

  Returns:
    Errors occurred as listed by FREQM_ERROR.

  Example:
    <code>
    if (FREQM_ErrorGet() == FREQM_ERROR_OVERFLOW)
    {
        //Handle overflow error here
    }
    else
    {
        measuredFrequency = FREQM_FrequencyGet();
    }
    </code>

  Remarks:
    Module errors are reset when the FREQM_MeasurementStart()
    function is called.
*/

FREQM_ERROR FREQM_ErrorGet( void );


 #ifdef __cplusplus // Provide C++ Compatibility
 }
 #endif

#endif /* PLIB_FREQM_H */
