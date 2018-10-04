/*******************************************************************************
  Analog-to-Digital Converter(ADC) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_adc.h

  Summary
    ADC Peripheral Library Interface Header File.

  Description
    This file defines the interface to the ADC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual plib_adc<x> headers
    will be generated as required by the MHC (where <x> is the peripheral
    instance number).

    Every interface symbol has a lower-case 'x' in it following the "ADC"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.

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

#ifndef PLIB_ADCx_H    // Guards against multiple inclusion
#define PLIB_ADCx_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************
/* ADC positive MUX input selection enum.

  Summary:
    Identifies ADC positive input pin to select.

  Description:
    Enum for the possible positive MUX input selections for the ADC.

  Remarks:
    None.
*/

typedef enum
{
    /* ADC pin AIN0 */
    ADC_POSINPUT_AIN0 = ADC_INPUTCTRL_MUXPOS_AIN0,

    /* ADC pin AIN1 */
    ADC_POSINPUT_AIN1 = ADC_INPUTCTRL_MUXPOS_AIN1,

    /* ADC pin AIN2 */
    ADC_POSINPUT_AIN2 = ADC_INPUTCTRL_MUXPOS_AIN2,

    /* ADC pin AIN3 */
    ADC_POSINPUT_AIN3 = ADC_INPUTCTRL_MUXPOS_AIN3,

    /* ADC pin AIN4 */
    ADC_POSINPUT_AIN4 = ADC_INPUTCTRL_MUXPOS_AIN4,

    /* ADC pin AIN5 */
    ADC_POSINPUT_AIN5 = ADC_INPUTCTRL_MUXPOS_AIN5,

    /* ADC pin AIN6 */
    ADC_POSINPUT_AIN6 = ADC_INPUTCTRL_MUXPOS_AIN6,

    /* ADC pin AIN7 */
    ADC_POSINPUT_AIN7 = ADC_INPUTCTRL_MUXPOS_AIN7,

    /* ADC pin AIN8 */
    ADC_POSINPUT_AIN8 = ADC_INPUTCTRL_MUXPOS_AIN8,

    /* ADC pin AIN9 */
    ADC_POSINPUT_AIN9 = ADC_INPUTCTRL_MUXPOS_AIN9,

    /* ADC pin AIN10 */
    ADC_POSINPUT_AIN10 = ADC_INPUTCTRL_MUXPOS_AIN10,

    /* ADC pin AIN11 */
    ADC_POSINPUT_AIN11 = ADC_INPUTCTRL_MUXPOS_AIN11,

    /* ADC pin TEMP */
    ADC_POSINPUT_TEMP = ADC_INPUTCTRL_MUXPOS_TEMP,

    /* ADC pin BANDGAP */
    ADC_POSINPUT_BANDGAP = ADC_INPUTCTRL_MUXPOS_BANDGAP,

    /* ADC pin SCALEDCOREVCC */
    ADC_POSINPUT_SCALEDCOREVCC = ADC_INPUTCTRL_MUXPOS_SCALEDCOREVCC,

    /* ADC pin SCALEDIOVCC */
    ADC_POSINPUT_SCALEDIOVCC = ADC_INPUTCTRL_MUXPOS_SCALEDIOVCC,

    /* ADC pin DAC */
    ADC_POSINPUT_DAC = ADC_INPUTCTRL_MUXPOS_DAC,

} ADC_POSINPUT;

// *****************************************************************************
/* ADC negative MUX input selection enum

  Summary:
    Identifies ADC negative input pin to select.

  Description:
    Enum for the possible negative MUX input selections for the ADC.

  Remarks:
    None.
*/

typedef enum
{
    /* ADC pin AIN0 */
    ADC_NEGINPUT_AIN0 = ADC_INPUTCTRL_MUXNEG_AIN0,

    /* ADC pin AIN1 */
    ADC_NEGINPUT_AIN1 = ADC_INPUTCTRL_MUXNEG_AIN1,

    /* ADC pin AIN2 */
    ADC_NEGINPUT_AIN2 = ADC_INPUTCTRL_MUXNEG_AIN2,

    /* ADC pin AIN3 */
    ADC_NEGINPUT_AIN3 = ADC_INPUTCTRL_MUXNEG_AIN3,

    /* ADC pin AIN4 */
    ADC_NEGINPUT_AIN4 = ADC_INPUTCTRL_MUXNEG_AIN4,

    /* ADC pin AIN5 */
    ADC_NEGINPUT_AIN5 = ADC_INPUTCTRL_MUXNEG_AIN5,

    /* ADC pin GND */
    ADC_NEGINPUT_GND = ADC_INPUTCTRL_MUXNEG(0x18u),

} ADC_NEGINPUT;
// *****************************************************************************

/* Callback function Pointer

  Summary:
    Defines the data type and function signature for the adc peripheral
    callback function.

  Description:
    This data type defines the function signature for the adc peripheral
    callback function. The adc peripheral will call back the client's
    function with this signature at the end of conversion.

  Function:
    void (*ADC_CALLBACK)( uintptr_t context );

  Precondition:
    ADCx_Initialize() must have been called for the given adc
    peripheral instance and ADCx_CallbackRegister() must have been
    called to set the function to be called.

  Parameters:
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).
    status - interrupt status.

  Returns:
    None.

  Example:
    <code>
      void ADCx_ResultReadyCallback( uintptr_t context )
      {
          uint16_t adcResult = 0;
          adcResult = ADCx_ConversionResultGet();
      }
      ADCx_CallbackRegister(ADCx_ResultReadyCallback, uintptr_t(NULL));
    </code>

  Remarks:
    The callback feature is only available when the library was generated with
    interrupt option (in MHC) enabled.
*/

typedef void (*ADC_CALLBACK)(uintptr_t context);


// *****************************************************************************
/* ADC Callback Object

  Summary:
    ADC peripheral callback object.

  Description:
    This local data object holds the function signature for the ADC peripheral
    callback function for RESRDY interrupt.

  Remarks:
    None.
*/

typedef struct
{
    ADC_CALLBACK callback;

    uintptr_t context;

} ADC_CALLBACK_OBJ;

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
    void ADCx_Initialize( void );

  Summary:
    Initializes given instance of ADC peripheral.

  Description:
    This function initializes given instance of ADC peripheral of the device
    with the values configured in MHC GUI. Once the peripheral is initialized,
    peripheral can be used for conversion.

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      ADCx_Initialize();
    </code>

  Remarks:
    This function must be called before any other ADC function is called.
    This function should only be called once during system initialization.
*/

void ADCx_Initialize( void );

// *****************************************************************************
/* Function:
    void ADCx_ChannelSelect( ADC_POSINPUT positiveInput,
                             ADC_NEGINPUT negativeInput );

  Summary:
    Selects ADC input channel.

  Description:
    This function selects ADC channel to use.

  Precondition:
    ADCx_Initialize() function must have been called first for the
    associated instance.

  Parameters:
    positiveInput - selected positive input pin.
    negativeInput - selected negative input pin.

  Returns:
    None.

  Example:
    <code>
      ADCx_Initialize();
      ADCx_ChannelSelect(ADC_POSINPUT_AIN0, ADC_NEGINPUT_GND);
    </code>

  Remarks:
    None.
*/

void ADCx_ChannelSelect( ADC_POSINPUT positiveInput, ADC_NEGINPUT negativeInput );

// *****************************************************************************
/* Function:
    void ADCx_ConversionStart( void );

  Summary:
    Starts the ADC conversion with the software trigger.

  Description:
    This function triggers the ADC conversion of the selected channel

  Precondition:
    ADCx_Initialize() function must have been called first for the
    associated instance.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
      ADCx_Initialize();
      ADCx_ConversionStart();
    </code>

  Remarks:
    This function should be called only when SW trigger for conversion
    is selected.
*/

void ADCx_ConversionStart( void );

// *****************************************************************************
/* Function:
    bool ADCx_ConversionStatusGet( void );

  Summary:
    Returns the status of the conversion of the channel.

  Description:
    This function returns the status of whether channel conversion is complete

  Precondition:
    ADCx_Initialize() function must have been called first for the
    associated instance.
    Also conversion must have been started.

  Parameters:
    None.

  Returns:
    adcConversionStatus - Conversion status of the channel
                          false - Conversion is not finished or not started yet
                          true  - Conversion is complete

  Example:
    <code>
      bool adcConversionStatus = false;
      ADCx_Initialize();
      ADCx_ConversionStart();
      adcConversionStatus = ADCx_ConversionStatusGet();
    </code>

  Remarks:
    This function should be called only after conversion is started.
*/

bool ADCx_ConversionStatusGet( void );

// *****************************************************************************
/* Function:
    uint16_t ADCx_ConversionResultGet( void );

  Summary:
    Returns the conversion result of the channel.

  Description:
    This function returns the result of completed conversion of the channel.

  Precondition:
    ADCx_Initialize() function must have been called first for the
    associated instance.And conversion must have been started.
    Also check whether result is ready to read.

  Parameters:
    None.

  Returns:
    adcResult - conversion result of the channel.

  Example:
    <code>
      uint16_t adcResult = 0;
      ADCx_Initialize();
      ADCx_ConversionStart();
      while(!ADCx_ConversionStatusGet());
      adcResult = ADCx_ConversionResultGet();
    </code>

  Remarks:
    This function can be called from interrupt or by polling the status when
    result is available. Result resolution and alignment depends on the GUI configuration.
*/

uint16_t ADCx_ConversionResultGet( void );

// *****************************************************************************
/* Function:
    void ADCx_CallbackRegister( ADC_CALLBACK callback, uintptr_t context );

  Summary:
    Registers the function to be called from interrupt.

  Description
    This function registers the callback function to be called from interrupt.

  Precondition:
    Interrupt option in MHC should have been enabled.

  Parameters:
    callback - callback function pointer
    context  - Allows the caller to provide a context value (usually a pointer
               to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
      void ADCx_ResultReadyCallback( uintptr_t context )
      {
          uint16_t adcResult = 0;
          adcResult = ADCx_ConversionResultGet();
      }

      ADCx_Initialize();
      ADCx_CallbackRegister(ADCx_ResultReadyCallback, (uintptr_t)NULL);
    </code>

  Remarks:
    Context value can be set to NULL is not required.
    To disable callback function, pass NULL for the callback parameter.
*/

void ADCx_CallbackRegister( ADC_CALLBACK callback, uintptr_t context );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_ADCx_H*/
