/*******************************************************************************
  ADC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_adc.h

  Summary
    ADC peripheral library interface.

  Description
    This file defines the interface to the ADC peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual adc<x> headers will be
    generated as required by the MHC (where <x> is the peripheral instance
    number). 

    Every interface symbol has a lower-case 'x' in it following the "ADC"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used (E.g. Single adc instance adc<x> will be replaced to adc (x is none), 
    Multiple adc instance adc<x> is replaced to adc0 or adc1, etc.).
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

#ifndef PLIB_ADC_H    // Guards against multiple inclusion
#define PLIB_ADC_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

extern "C" {

#endif

// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/*  The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

/* Analog channel mask

   Summary:
    Identifies ADC channel mask

   Description:
    This enumeration identifies ADC channel mask. This may be ORed together to
    enable/disable multiple channels.

   Remarks:
    None.
*/
typedef enum
{
    ADC_CH0_MASK = (1U << 0U),
    ADC_CH1_MASK = (1U << 1U),
    ADC_CH2_MASK = (1U << 2U),
    ADC_CH3_MASK = (1U << 3U),
    ADC_CH4_MASK = (1U << 4U),
    ADC_CH5_MASK = (1U << 5U),
    ADC_CH6_MASK = (1U << 6U),
    ADC_CH7_MASK = (1U << 7U),
    ADC_CH8_MASK = (1U << 8U),
    ADC_CH9_MASK = (1U << 9U),
    ADC_CH10_MASK = (1U << 10U),
    ADC_CH11_MASK = (1U << 11U)
}ADC_CHANNEL_MASK;

// *****************************************************************************

/* Analog channel numbers

   Summary:
    Identifies ADC channel number

   Description:
    This enumeration identifies ADC channel numbers. This may be used as
    argument of function to identify channel number.

   Remarks:
    None.
*/
typedef enum
{
    ADC_CH0 = 0U,
    ADC_CH1,
    ADC_CH2,
    ADC_CH3,
    ADC_CH4,
    ADC_CH5,
    ADC_CH6,
    ADC_CH7,
    ADC_CH8,
    ADC_CH9,
    ADC_CH10,
    ADC_CH11
}ADC_CHANNEL_NUM;

// *****************************************************************************

/* Interrupt sources number

   Summary:
    Identifies interrupt sources number

   Description:
    This enumeration identifies ADC channel end of conversion (EOC)  and Comparison event
    interrupt sources number. This may be ORed together to enable/disable multiple interrupts.

   Remarks:
    None.
*/
typedef enum
{
    ADC_INTERRUPT_EOC_0_MASK = (1U << 0U),
    ADC_INTERRUPT_EOC_1_MASK = (1U << 1U),
    ADC_INTERRUPT_EOC_2_MASK = (1U << 2U),
    ADC_INTERRUPT_EOC_3_MASK = (1U << 3U),
    ADC_INTERRUPT_EOC_4_MASK = (1U << 4U),
    ADC_INTERRUPT_EOC_5_MASK = (1U << 5U),
    ADC_INTERRUPT_EOC_6_MASK = (1U << 6U),
    ADC_INTERRUPT_EOC_7_MASK = (1U << 7U),
    ADC_INTERRUPT_EOC_8_MASK = (1U << 8U),
    ADC_INTERRUPT_EOC_9_MASK = (1U << 9U),
    ADC_INTERRUPT_EOC_10_MASK = (1U << 10U),
    ADC_INTERRUPT_EOC_11_MASK = (1U << 11U),
    ADC_INTERRUPT_COMPE_MASK = (1U << 26U)
}ADC_INTERRUPT_MASK;

// *****************************************************************************
/* Callback Function Pointer

   Summary:
    Defines the function pointer data type and function signature for the adc peripheral
    callback function.

   Description:
    This data type defines the function pointer and function signature for the adc peripheral
    callback function. The adc peripheral will call back the client's
    function with this signature at the end of conversion.

   Function:
    void (*ADC_CALLBACK)( uintptr_t context )

   Precondition:
    ADCx_Initialize must have been called for the given adc peripheral
    instance and ADCx_CallbackRegister must have been called to set the
    function to be called.

   Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

   Returns:
    None.

   Example:
    <code>
    void ADCx_ChCallback (uintptr_t context);

    ADCx_CallbackRegister(ADC_ChCallback, NULL);
    </code>

    Remarks:
    None.
*/

typedef void (*ADC_CALLBACK)( uintptr_t context);
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
    ADC_CALLBACK callback_fn;
    uintptr_t context;
}ADC_CALLBACK_OBJECT;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// ****************************************************************************
/* Function:
    void ADCx_Initialize (void)

  Summary:
    Initializes given instance of ADC peripheral.

  Description:
    This function initializes given instance of ADC peripheral of the device with the values
    configured in MHC GUI. Once the peripheral is initialized, peripheral can be used for conversion.

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
    This function must be called before any other ADC function is
    called.

    This function should only be called once during system
    initialization.
*/
void ADCx_Initialize (void);

// *****************************************************************************

/* Function:
    void ADCx_ChannelsEnable (ADC_CHANNEL_MASK channelsMask)

  Summary:
    Enables the ADC channels

  Description:
    This function enables channels specified in channelsMask

  Precondition:
    ADCx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channelsMask - set of channel numbers

  Returns:
    None.

  Example:
    <code>
        ADCx_Initialize();
        ADCx_ChannelsEnable(ADC_CH0_MASK | ADC_CH3_MASK);
    </code>

  Remarks:
    This function does not disable channels which are not included in the channel mask.
*/
void ADCx_ChannelsEnable (ADC_CHANNEL_MASK channelsMask);

// *****************************************************************************

/* Function:
    void ADCx_ChannelsDisable (ADC_CHANNEL_MASK channelsMask)

  Summary:
    Disables the ADC channels

  Description:
    This function disables channels specified in channelsMask

  Precondition:
    ADCx_Initialize() must have been called first for the associated instance.

  Parameters:
    channelsMask - set of channel numbers

  Returns:
    None.

  Example:
    <code>
        ADCx_Initialize();
        ADCx_ChannelsDisable(ADC_CH0_MASK | ADC_CH3_MASK);
    </code>

  Remarks:
    This function does not enable channels which are not included in the channel mask.
*/
void ADCx_ChannelsDisable (ADC_CHANNEL_MASK channelsMask);

// *****************************************************************************

/* Function:
    void ADCx_ChannelsInterruptEnable(ADC_INTERRUPT_MASK channelsInterruptMask)

  Summary:
    Enables the ADC interrupt sources

  Description:
    This function enables interrupt sources specified in channelsInterruptMask.

  Precondition:
    ADCx_Initialize() must have been called first for the associated instance.

  Parameters:
    channelsInterruptMask - interrupt sources

  Returns:
    None.

  Example:
    <code>
        ADCx_Initialize();
        ADCx_ChannelsInterruptEnable(ADC_INTERRUPT_EOC_0_MASK);
    </code>

  Remarks:
    This function does not disable interrupts which are not included in the mask.
*/
void ADCx_ChannelsInterruptEnable(ADC_INTERRUPT_MASK channelsInterruptMask);

// *****************************************************************************
/* Function:
    void ADCx_ChannelsInterruptDisable(ADC_INTERRUPT_MASK channelsInterruptMask)

  Summary:
    Disables the ADC interrupt sources

  Description:
    This function disables interrupt sources specified in channelsInterruptMask.

  Precondition:
    ADCx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channelsInterruptMask - interrupt  sources

  Returns:
    None.

  Example:
    <code>
        ADCx_Initialize();
        ADCx_ChannelsInterruptDisable(ADC_INTERRUPT_EOC_0_MASK);
    </code>

  Remarks:
    This function does not disable interrupts which are not included in the mask.
*/
void ADCx_ChannelsInterruptDisable(ADC_INTERRUPT_MASK channelsInterruptMask);

// *****************************************************************************
/* Function:
    void ADCx_ConversionStart()

  Summary:
    Starts the ADC conversion of all the enabled channels with the software trigger

  Description:
    This function starts ADC conversion of all the enabled channels. Trigger is common for all the
    enabled channels. And channels are converted in sequential order or in user decided order based on
    configuration.

  Precondition:
    ADCx_Initialize() function must have been called first for the associated instance and channels must have been enabled using
    ADCx_ChannelsEnable() function.

  Parameters:
    None

  Returns:
    None.

  Example:
    <code>
        ADCx_Initialize();
        ADCx_ChannelsEnable(ADC_CH0);
        ADCx_ConversionStart();
    </code>

  Remarks:
      This function should be called only when SW trigger for conversion is selected.
*/
void ADCx_ConversionStart(void);
// *****************************************************************************

/* Function:
    bool ADCx_ChannelResultIsReady(ADC_CHANNEL_NUM channel)

  Summary:
    Returns the status of the channel conversion

  Description:
    This function returns the status of the channel whether conversion is complete
    and result is available

  Precondition:
    ADCx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channel - Channel number

  Returns:
    bool - status of the channel
    false: channel is disabled or conversion is not yet finished
    true: channel is enabled and result is available

  Example:
    <code>
        bool ch_status;
        ADCx_Initialize();
        ADCx_ChannelsEnable(ADC_CH0);
        ADCx_ConversionStart();
        ch_status = ADCx_ChannelResultIsReady(ADC_CH0);
    </code>

  Remarks:
    None
*/
bool ADCx_ChannelResultIsReady(ADC_CHANNEL_NUM channel);

// *****************************************************************************

/* Function:
    uint16_t ADCx_ChannelResultGet (ADC_CHANNEL channel)

  Summary:
    Reads the conversion result of the channel

  Description:
    This function reads the conversion result of the channel

  Precondition:
    ADCx_Initialize() must have been called first for the associated instance.
    And conversion must have been started.

  Parameters:
    channel - channel number

  Returns:
    uint16_t - conversion result

  Example:
    <code>
        uint16_t result;
        bool status;
        ADCx_Initialize();
        ADCx_ChannelsEnable(ADC_CH0);
        ADCx_ConversionStart();
        status = ADCx_ChannelResultIsReady(ADC_CH0);
        if (status)
        {
            result = ADCx_ChannelResultGet(ADC_CH0);
        }
    </code>

  Remarks:
     This function can be called from interrupt or by polling the status when result is available.
     User should decode the result based on result sign mode (signed or unsigned result) and result
     resolution (12, 13 or 14 bit result) configuration.
*/
uint16_t ADCx_ChannelResultGet(ADC_CHANNEL_NUM channel);

// *****************************************************************************

/* Function:
    void ADCx_ConversionSequenceSet (ADC_CHANNEL *channelList, uint8_t numChannel)

  Summary:
    Sets the user sequence of the channel conversion

  Description:
    This function sets the order in which channels are converted.

  Precondition:
    ADCx_Initialize() must have been called first for the associate instance.
    Conversion should not be ongoing while changing the sequence.

  Parameters:
    *channelList - pointer to the list of the channels which describes the order of conversion
    numChannel - Number of enabled channels in the list

  Returns:
    None.

  Example:
    <code>
        ADC_CHANNEL seq_order[4] = {ADC_CH3, ADC_CH5, ADC_CH1, ADC_CH2};
        ADCx_Initialize();
        ADCx_ConversionSequenceSet(seq_order, 0x4);
        ADCx_ChannelsEnable(ADC_CH0_MASK | ADC_CH1_MASK | ADC_CH2_MASK | ADC_CH3_MASK);
    </code>

  Remarks:
    Conversion order is set in this function and remains valid until user configures new conversion sequence order
    or reinitializes the peripheral.
    Array pointed to by *channelList must be valid during the call to this function. This function copies
    the array data into ADC HW registers.
*/
void ADCx_ConversionSequenceSet(ADC_CHANNEL_NUM *channelList, uint8_t numChannel);

// *****************************************************************************

/* Function:
    void ADCx_ComparisonWindowSet(uint16_t lowThreshold, uint16_t highThreshold)

  Summary:
    Sets Low threshold and High threshold in comparison window.

  Description:
    This function sets Low threshold and High threshold in compare window 
    for comparison functions defined in comparison mode.

  Precondition:
    ADCx_Initialize() function must have been called first for the associated instance
    and channels must have been enabled using ADC_ChannelsEnable() function.

  Parameters:
    lowThreshold - Low threshold to be compared as per settings of comparison mode
    highThreshold - High threshold to be compared as per settings of comparison mode

  Returns:
    None.

  Example:
    <code>
        ADCx_Initialize();
        ADCx_ChannelsEnable(ADC_CH0);
        ADCx_ComparisonWindowSet(100, 500);
    </code>

  Remarks:
    None.
*/
void ADCx_ComparisonWindowSet(uint16_t lowThreshold, uint16_t highThreshold);

// *****************************************************************************

/* Function:
    bool ADCx_ComparisonEventResultIsReady(void)

  Summary:
    Returns the status of the Comparison event

  Description:
    This function returns the status of the Comparison event whether comparison event
    has occurred and result is available

  Precondition:
    ADCx_Initialize() function must have been called first for the associated instance.

  Parameters:
    void - None

  Returns:
    bool - status of the comparison event
    false: No comparison event
    true: At least one comparison event has occurred

  Example:
    <code>
        bool comp_event;
        ADCx_Initialize();
        ADCx_ChannelsEnable(ADC_CH0);
        ADCx_ConversionStart();
        comp_event = ADCx_ComparisonEventResultIsReady();
        if (comp_event)
        {
            result = ADCx_ChannelResultGet(ADC_CH0);
        }
    </code>

  Remarks:
    None
*/
bool ADCx_ComparisonEventResultIsReady(void);

// *****************************************************************************
/* Function:
    void ADCx_ComparisonRestart(void)

  Summary:
    Restart the comparison function.

  Description:
    This function restarts the comparison function. And it stops the conversion result storage
    until the next comparison match.

  Precondition:
    ADCx_Initialize() function must have been called first for the associated instance
    and channels must have been enabled using ADC_ChannelsEnable() function.

  Parameters:
    None

  Returns:
    None.

  Example:
    <code>
        bool comp_event;
        ADCx_Initialize();
        ADCx_ChannelsEnable(ADC_CH0);
        ADCx_ConversionStart();
        comp_event = ADCx_ComparisonEventResultIsReady();
        if (comp_event)
        {
            result = ADCx_ChannelResultGet(ADC_CH0);
			ADCx_ComparisonRestart();
        }
    </code>

  Remarks:
      This function stops the conversion result storage until the next comparison match.
*/
void ADCx_ComparisonRestart(void);

// *****************************************************************************

/* Function:
    void ADCx_CallbackRegister (ADC_CALLBACK callback, uintptr_t context);

  Summary:
    Registers the function to be called from interrupt

  Description
    This function registers the callback function to be called from interrupt

  Precondition:
    ADCx_Initialize() must have been called first for the associated instance.

  Parameters:
    callback - callback function pointer
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
        void ADCx_Callback_Fn(uintptr_t context);

        ADCx_Initialize();
        ADCx_CallbackRegister(ADC_Callback_Fn, NULL);
    </code>

  Remarks:
    Context value can be set to NULL if not required.
    To disable callback function, pass NULL for the callback parameter.
*/
void ADCx_CallbackRegister(ADC_CALLBACK callback, uintptr_t context);



// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_ADC_H

/**
 End of File
*/

