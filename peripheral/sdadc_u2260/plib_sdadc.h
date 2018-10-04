/*******************************************************************************
  SDADC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_sdadc.h

  Summary:
    SDADC PLIB Header file

  Description:
    This file defines the interface to the SDADC peripheral library. This
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

#ifndef PLIB_SDADCx_H
#define PLIB_SDADCx_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
/* Callback Function Pointer

   Summary:
    Defines the function pointer data type and function signature for the SDADC peripheral
    callback function.

   Description:
    This data type defines the function pointer and function signature for the SDADC peripheral
    callback function. The SDADC peripheral will call back the client's
    function with this signature at the end of conversion.

   Function:
    void (*SDADC_CALLBACK)( uintptr_t context )

   Precondition:
    SDADC_Initialize must have been called for the given SDADC peripheral
    instance and SDADC_CallbackRegister must have been called to set the
    function to be called.

   Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

   Returns:
    None.

   Example:
    <code>
    void SDADC_ChCallback (uintptr_t context);

    SDADC_CallbackRegister(SDADC_ChCallback, NULL);
    </code>

    Remarks:
    None.
*/

typedef void (*SDADC_CALLBACK)( uintptr_t context);
// *****************************************************************************
/* Callback structure

   Summary:
    Callback structure

   Description:
    This stores the callback function pointer and context

   Remarks:
    None.
*/
typedef struct
{
    SDADC_CALLBACK callback;
    uintptr_t context;
}SDADC_CALLBACK_OBJECT;


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
    void SDADCx_Initialize( void );

  Summary:
    Initializes given instance of SDADC peripheral.

  Description:
    This function initializes given instance of SDADC peripheral of the device
    with the values configured in MCC GUI. Once the peripheral is initialized,
    peripheral can be used for conversion.

  Precondition:
    MCC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        SDADCx_Initialize();
    </code>

  Remarks:
    This function must be called before any other SDADC function is called.
    This function should only be called once during system initialization.
*/
void SDADCx_Initialize( void );

// *****************************************************************************
/* Function:
    void SDADCx_ConversionStart(void);

  Summary:
    Starts the SDADC conversion with the software trigger.

  Description:
    This function triggers the SDADC conversion of the enabled channels.

  Precondition:
    SDADCx_Initialize() function must have been called first for the
    associated instance.
    Also channel should be selected for associated instance.

  Parameters:
    None

  Returns:
    None.

  Example:
    <code>
        SDADCx_Initialize();
        SDADCx_ConversionStart();
    </code>

  Remarks:
    This function should be called only when SW trigger for conversion
    is selected.
*/
void SDADCx_ConversionStart( void );

// *****************************************************************************
/* Function:
    bool SDADCx_ConversionResultIsReady( void );

  Summary:
    Returns the status of the conversion.

  Description:
    This function returns the status of whether conversion is complete.

  Precondition:
    SDADCx_Initialize() function must have been called first for the
    associated instance.
    Also conversion must have been started.

  Parameters:
    None.

  Returns:
    True  - Conversion is not yet finished or not started yet
    False - Conversion is complete

  Example:
    <code>
        bool sdadcConversionStatus;
        SDADCx_Initialize();
        SDADCx_ConversionStart();
        sdadcConversionStatus = SDADCx_ConversionResultIsReady();
    </code>

  Remarks:
    This function should be called only after conversion is started.
*/
bool SDADCx_ConversionResultIsReady( void );

// *****************************************************************************
/* Function:
    int16_t SDADCx_ConversionResultGet( void );

  Summary:
    Returns the conversion result.

  Description:
    This function returns the result of completed conversion.

  Precondition:
    SDADCx_Initialize() function must have been called first for the
    associated instance.And conversion must have been started.
    Also check whether result is ready to read.

  Parameters:
    None.

  Returns:
    int16_t - 16 bit signed conversion result.

  Example:
    <code>
        int16_t sdadcResult = 0;
        SDADCx_Initialize();
        SDADCx_ConversionStart();
        sdadcResult = SDADCx_ConversionResultGet();
    </code>

  Remarks:
    This function can be called from interrupt or by polling the status when
    result is available.
*/
int16_t SDADCx_ConversionResultGet( void );

// *****************************************************************************
/* Function:
    bool SDADCx_ConversionSequenceIsFinished( void );

  Summary:
    Returns the status of automatic sequence conversion.

  Description:
    This function checks the status of the conversion sequence. 

  Precondition:
    SDADCx_Initialize() function must have been called first for the
    associated instance.And conversion must have been started.

  Parameters:
    None.

  Returns:
    true - all the enabled channels in the sequence have finished conversion
    false - sequence conversion is ongoing

  Example:
    <code>
        bool seq_status;
        SDADCx_Initialize();
        SDADCx_ConversionStart();
        seq_status = SDADCx_ConversionSequenceIsFinished();
    </code>

  Remarks:
    This function is valid only if auto sequence feature is enabled. 
*/
bool SDADCx_ConversionSequenceIsFinished( void );

// *****************************************************************************
/* Function:
    void SDADCx_ComparisonWindowSet(int16_t low_threshold, int16_t high_threshold);

  Summary:
    Returns the status of automatic sequence conversion.

  Description:
    This function configures the window threshold values. 

  Precondition:
    SDADCx_Initialize() function must have been called first for the
    associated instance.

  Parameters:
    low_threshold - 16-bit signed value for lower threshold
    high_threshold - 16-bit signed value for upper threshold

  Returns:
    None

  Example:
    <code>
        SDADCx_Initialize();
        SDADCx_ComparisonWindowSet(0x1000, 0x3000);
    </code>

  Remarks:
    This function is valid only if window monitor feature is enabled. 
    16-bit signed values are written in the register as 24-bit by left shifting by 8 bits. 
*/
void SDADCx_ComparisonWindowSet(int16_t low_threshold, int16_t high_threshold);

// *****************************************************************************
/* Function:
    void SDADCx_CallbackRegister(SDADC_CALLBACK callback, uintptr_t context);

  Summary:
    Registers the function to be called from interrupt.

  Description
    This function registers the callback function to be called from interrupt.

  Precondition:
    SDADCx_Initialize() must have been called first.

  Parameters:
    callback - callback function pointer
    context  - Allows the caller to provide a context value (usually a pointer
               to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
      void SDADC_Callback_Fn( uintptr_t context );

      SDADCx_Initialize();
      SDADCx_CallbackRegister(SDADC_Callback_Fn, NULL);
    </code>

  Remarks:
    Context value can be set to NULL if not required.
    To disable callback function, pass NULL for the callback parameter.
*/

void SDADCx_CallbackRegister(SDADC_CALLBACK callback, uintptr_t context);

    // DOM-IGNORE-BEGIN
    #ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_SDADCx_H */