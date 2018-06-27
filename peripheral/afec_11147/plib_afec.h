/*******************************************************************************
  AFEC Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_afec.h

  Summary
    AFEC peripheral library interface.

  Description
    This file defines the interface to the AFEC peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual afec<x> headers will be
    generated as required by the MCC (where <x> is the peripheral instance
    number).

    Every interface symbol has a lower-case 'x' in it following the "AFEC"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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

#ifndef PLIB_AFEC_H    // Guards against multiple inclusion
#define PLIB_AFEC_H


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
    Identifies AFEC channel mask

   Description:
    This enumeration identifies AFEC channel mask. This may be ORed together to
    enable/disable multiple channels.

   Remarks:
    None.
*/
typedef enum
{
    AFEC_CH0_MASK = (1U << 0U),
    AFEC_CH1_MASK = (1U << 1U),
    AFEC_CH2_MASK = (1U << 2U),
    AFEC_CH3_MASK = (1U << 3U),
    AFEC_CH4_MASK = (1U << 4U),
    AFEC_CH5_MASK = (1U << 5U),
    AFEC_CH6_MASK = (1U << 6U),
    AFEC_CH7_MASK = (1U << 7U),
    AFEC_CH8_MASK = (1U << 8U),
    AFEC_CH9_MASK = (1U << 9U),
    AFEC_CH10_MASK = (1U << 10U),
    AFEC_CH11_MASK = (1U << 11U)
}AFEC_CHANNEL_MASK;
// *****************************************************************************

/* Analog channel numbers

   Summary:
    Identifies AFEC channel number

   Description:
    This enumeration identifies AFEC channel numbers. This may be used as
    argument of function to identify channel number.

   Remarks:
    None.
*/
typedef enum
{
    AFEC_CH0 = 0U,
    AFEC_CH1,
    AFEC_CH2,
    AFEC_CH3,
    AFEC_CH4,
    AFEC_CH5,
    AFEC_CH6,
    AFEC_CH7,
    AFEC_CH8,
    AFEC_CH9,
    AFEC_CH10,
    AFEC_CH11
}AFEC_CHANNEL_NUM;
// *****************************************************************************

/* Programmable gain value

   Summary:
    Identifies programmable gain setting

   Description:
    This enumeration identifies ADC gain of built-in programmable gain amplifier.
    This may be used as argument of function to set the gain.

   Remarks:
    None.
*/
typedef enum
{
    AFEC_CHANNEL_GAIN_X1,
    AFEC_CHANNEL_GAIN_X2,
    AFEC_CHANNEL_GAIN_X4
}AFEC_CHANNEL_GAIN;
// *****************************************************************************

/* Interrupt sources mask

   Summary:
    Identifies channel interrupt sources mask

   Description:
    This enumeration identifies AFEC channel end of conversion (EOC) interrupt sources mask.
    This may be ORed together to enable/disable multiple interrupts.

   Remarks:
    None.
*/
typedef enum
{
    AFEC_INTERRUPT_EOC_0_MASK = (1U << 0U),
    AFEC_INTERRUPT_EOC_1_MASK = (1U << 1U),
    AFEC_INTERRUPT_EOC_2_MASK = (1U << 2U),
    AFEC_INTERRUPT_EOC_3_MASK = (1U << 3U),
    AFEC_INTERRUPT_EOC_4_MASK = (1U << 4U),
    AFEC_INTERRUPT_EOC_5_MASK = (1U << 5U),
    AFEC_INTERRUPT_EOC_6_MASK = (1U << 6U),
    AFEC_INTERRUPT_EOC_7_MASK = (1U << 7U),
    AFEC_INTERRUPT_EOC_8_MASK = (1U << 8U),
    AFEC_INTERRUPT_EOC_9_MASK = (1U << 9U),
    AFEC_INTERRUPT_EOC_10_MASK = (1U << 10U),
    AFEC_INTERRUPT_EOC_11_MASK = (1U << 11U)
}AFEC_INTERRUPT_MASK;

// *****************************************************************************
/* Callback Function Pointer

   Summary:
    Defines the function pointer data type and function signature for the afec peripheral
    callback function.

   Description:
    This data type defines the function pointer and function signature for the afec peripheral
    callback function. The afec peripheral will call back the client's
    function with this signature at the end of conversion.

   Function:
    void (*AFEC_CALLBACK)( uintptr_t context )

   Precondition:
    AFEC_Initialize must have been called for the given afec peripheral
    instance and AFEC_CallbackRegister must have been called to set the
    function to be called.

   Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

   Returns:
    None.

   Example:
    <code>
    void AFEC_ChCallback (uintptr_t context);

    AFEC_CallbackRegister(AFEC_ChCallback, NULL);
    </code>

    Remarks:
    None.
*/

typedef void (*AFEC_CALLBACK)( uintptr_t context);
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
    AFEC_CALLBACK callback_fn;
    uintptr_t context;
}AFEC_CALLBACK_OBJECT;

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
    void AFECx_Initialize (void);

  Summary:
    Initializes given instance of AFEC peripheral.

  Description:
    This function initializes given instance of AFEC peripheral of the device with the values
    configured in MCC GUI. Once the peripheral is initialized, peripheral can be used for conversion.

  Precondition:
    MCC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        AFEC0_Initialize();
    </code>

  Remarks:
    This function must be called before any other AFEC function is
    called.

    This function should only be called once during system
    initialization.
*/
void AFECx_Initialize (void);

// *****************************************************************************

/* Function:
    void AFECx_ChannelsEnable (AFEC_CHANNEL_MASK channelsMask);

  Summary:
    Enables the ADC channels

  Description:
    This function enables channels specified in channelsMask

  Precondition:
    AFECx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channelsMask - set of channel numbers

  Returns:
    None.

  Example:
    <code>
        AFEC0_Initialize();
        AFEC0_ChannelsEnable(AFEC_CH0_MASK | AFEC_CH3_MASK);
    </code>

  Remarks:
    This function does not disable channels which are not included in the channel mask.
*/
void AFECx_ChannelsEnable (AFEC_CHANNEL_MASK channelsMask);

// *****************************************************************************

/* Function:
    void AFECx_ChannelsDisable (AFEC_CHANNEL_MASK channelsMask);

  Summary:
    Disables the ADC channels

  Description:
    This function disables channels specified in channelsMask

  Precondition:
    AFECx_Initialize() must have been called first for the associated instance.

  Parameters:
    channelsMask - set of channel numbers

  Returns:
    None.

  Example:
    <code>
        AFEC0_Initialize();
        AFEC0_ChannelsDisable(AFEC_CH0_MASK | AFEC_CH3_MASK);
    </code>

  Remarks:
    This function does not enable channels which are not included in the channel mask.
*/
void AFECx_ChannelsDisable (AFEC_CHANNEL_MASK channelsMask);

// *****************************************************************************

/* Function:
    void AFECx_ChannelsInterruptEnable (AFEC_INTERRUPT_MASK channelsInterruptMask);

  Summary:
    Enables the ADC interrupt sources

  Description:
    This function enables interrupt sources specified in channelsInterruptMask.

  Precondition:
    AFECx_Initialize() must have been called first for the associated instance.

  Parameters:
    channelsInterruptMask - interrupt sources

  Returns:
    None.

  Example:
    <code>
        AFEC0_Initialize();
        AFEC0_ChannelsInterruptEnable(AFEC_INTERRUPT_EOC_0_MASK);
    </code>

  Remarks:
    This function does not disable interrupts which are not included in the mask.
*/
void AFECx_ChannelsInterruptEnable (AFEC_INTERRUPT_MASK channelsInterruptMask);

// *****************************************************************************
/* Function:
    void AFECx_ChannelsInterruptDisable (AFEC_INTERRUPT_MASK channelsInterruptMask);

  Summary:
    Disables the ADC interrupt sources

  Description:
    This function disables interrupt sources specified in  channelsInterruptMask.

  Precondition:
    AFECx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channelsInterruptMask - interrupt  sources

  Returns:
    None.

  Example:
    <code>
        AFEC0_Initialize();
        AFEC0_ChannelsInterruptDisable(AFEC_INTERRUPT_EOC_0_MASK);
    </code>

  Remarks:
    This function does not enable interrupts which are not included in the mask.
*/
void AFECx_ChannelsInterruptDisable (AFEC_INTERRUPT_MASK channelsInterruptMask);
// *****************************************************************************
/* Function:
    void AFECx_ConversionStart();

  Summary:
    Starts the ADC conversion of all the enabled channels with the software trigger

  Description:
    This function starts ADC conversion of all the enabled channels. Trigger is common for all the
    enabled channels. And channels are converted in sequential order or in user decided order based on
    configuration.

  Precondition:
    AFECx_Initialize() function must have been called first for the associated instance and channels must have been enabled using
    AFECx_ChannelsEnable() function.

  Parameters:
    None

  Returns:
    None.

  Example:
    <code>
        AFEC0_Initialize();
        AFEC0_ChannelsEnable(AFEC_CH0);
        AFEC0_ConversionStart();
    </code>

  Remarks:
      This function should be called only when SW trigger for conversion is selected.
*/
void AFECx_ConversionStart(void);
// *****************************************************************************

/* Function:
    bool AFECx_ChannelResultIsReady(AFEC_CHANNEL channel);

  Summary:
    Returns the status of the channel conversion

  Description:
    This function returns the status of the channel whether conversion is complete and result is
    available

  Precondition:
    AFECx_Initialize() function must have been called first for the associated instance.

  Parameters:
    channel - channel number

  Returns:
    bool - status of the channel
    false: channel is disabled or conversion is not yet finished
    true: channel is enabled and result is available

  Example:
    <code>
        bool ch_status;
        AFEC0_Initialize();
        AFEC0_ChannelsEnable(AFEC_CH0);
        AFEC0_ConversionStart();
        ch_status = AFEC0_ChannelResultIsReady(AFEC_CH0);
    </code>

  Remarks:
    None
*/
bool AFECx_ChannelResultIsReady(AFEC_CHANNEL_NUM channel);
// *****************************************************************************

/* Function:
    uint16_t AFECx_ChannelResultGet (AFEC_CHANNEL channel);

  Summary:
    Reads the conversion result of the channel

  Description:
    This function reads the conversion result of the channel

  Precondition:
    AFECx_Initialize() must have been called first for the associated instance. And conversion must have been started.

  Parameters:
    channel - channel number

  Returns:
    uint16_t - conversion result

  Example:
    <code>
        uint16_t result;
        bool status;
        AFEC0_Initialize();
        AFEC0_ChannelsEnable(AFEC_CH0);
        AFEC0_ConversionStart();
        status = AFEC0_ChannelResultIsReady(AFEC_CH0);
        if (status)
        {
            result = AFEC0_ChannelResultGet(AFEC_CH0);
        }
    </code>

  Remarks:
     This function can be called from interrupt or by polling the status when result is available.
     User should decode the result based on result sign mode (signed or unsigned result) and result
     resolution (12, 13, 14, 15 or 16 bit result) configuration.
*/
uint16_t AFECx_ChannelResultGet(AFEC_CHANNEL_NUM channel);

// *****************************************************************************

/* Function:
    void AFECx_ConversionSequenceSet (AFEC_CHANNEL *channelList, uint8_t numChannel);

  Summary:
    Sets the user sequence of the channel conversion

  Description:
    This function sets the order in which channels are converted.

  Precondition:
    AFECx_Initialize() must have been called first for the associate instance.
    Conversion should not be ongoing while changing the sequence.

  Parameters:
    *channelList - pointer to the list of the channels which describes the order of conversion
    numChannel - Number of enabled channels in the list

  Returns:
    None.

  Example:
    <code>
        AFEC_CHANNEL seq_order[4] = {AFEC_CH3, AFEC_CH5, AFEC_CH1, AFEC_CH2};
        AFEC0_Initialize();
        AFEC0_ConversionSequenceSet(seq_order, 0x4);
        AFEC0_ChannelsEnable(AFEC_CH0_MASK | AFEC_CH1_MASK | AFEC_CH2_MASK | AFEC_CH3_MASK);
    </code>

  Remarks:
    Conversion order is set in this function and remains valid until user configures new conversion sequence order
    or reinitializes the peripheral.
    Array pointed to by *channelList must be valid during the call to this function. This function copies
    the array data into AFEC HW registers.
*/
void AFECx_ConversionSequenceSet(AFEC_CHANNEL_NUM *channelList, uint8_t numChannel);
// *****************************************************************************

/* Function:
    void AFECx_ChannelGainSet (AFEC_CHANNEL channel, AFEC_CHANNEL_GAIN gain);

  Summary:
    Writes the gain of the channel

  Description:
    This function writes the gain of the channel

  Precondition:
    AFECx_Initialize() must have been called first for the associated instance.

  Parameters:
    channel - channel number
    gain - channel gain of the amplifier

  Returns:
    None.

  Example:
    <code>
        AFEC0_Initialize();
        AFEC0_ChannelGainSet(AFEC_CH0, AFEC_CHANNEL_GAIN_2X);
    </code>

  Remarks:
    Input voltage range reduces as gain increases.
    For gain = 1, range is (0) to (Vref)
    For gain = 2, range is (Vref/4) to (3 * Vref/4)
    For gain = 4, range is (3 * Vref/8) to (5 * Vref/8)
*/
void AFECx_ChannelGainSet(AFEC_CHANNEL_NUM channel, AFEC_CHANNEL_GAIN gain);
// *****************************************************************************

/* Function:
    void AFECx_ChannelOffsetSet (AFEC_CHANNEL channel, uint16_t offset);

  Summary:
    Writes the channel offset

  Description
    This function writes the offset value for the channel. This offset value is added to the
    value of sample to get the full range output (0 to Vref). Normally, this value should be set to Vref/2 in 10-bit format.

  Precondition:
    AFECx_Initialize() must have been called first for the associated instance.

  Parameters:
    channel - channel number
    offset - 10-bit offset generated by internal DAC

  Returns:
    None.

  Example:
    <code>
        AFEC0_Initialize();
        AFEC0_ChannelOffsetSet(AFEC_CH0, 512U);
    </code>

  Remarks:
    Offset should be set at the initialization. If this function is called when conversion is on-going, offset will be
    applied from the next conversion.
    Offset is added to the sample value and thus offset limits the input voltage range.
    Offset less than Vref/2 will result in ADC saturation for input voltage greater than Vref/2.
*/
void AFECx_ChannelOffsetSet(AFEC_CHANNEL_NUM channel, uint16_t offset);
// *****************************************************************************

/* Function:
    void AFECx_CallbackRegister (AFECx_CALLBACK callback, uintptr_t context);

  Summary:
    Registers the function to be called from interrupt

  Description
    This function registers the callback function to be called from interrupt

  Precondition:
    AFECx_Initialize() must have been called first for the associated instance.

  Parameters:
    callback - callback function pointer
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
        void AFECx_Callback_Fn(uintptr_t context);

        AFEC0_Initialize();
        AFEC0_CallbackRegister(AFEC_Callback_Fn, NULL);
    </code>

  Remarks:
    Context value can be set to NULL if not required.
    To disable callback function, pass NULL for the callback parameter.
*/
void AFECx_CallbackRegister(AFEC_CALLBACK callback, uintptr_t context);



// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_AFEC_H

/**
 End of File
*/

