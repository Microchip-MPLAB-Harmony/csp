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

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <sys/attribs.h>

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
	AFEC_CHANNEL_GAIN_1X,
	AFEC_CHANNEL_GAIN_2X,
	AFEC_CHANNEL_GAIN_4X
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
    void (*AFEC_CALLBACK)( uintptr_t context, AFEC_INTERRUPT_MASK event_status )

   Precondition:
    AFEC_Initialize must have been called for the given afec peripheral 
    instance and AFEC_ChannelCallbackSet must have been called to set the 
    function to be called.

   Parameters:
    context  - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).
	
	event_status - mask of the channels for which conversion result is ready
	at the time of calling the callback function
  
   Returns:
    None.

   Example:
    <code>
	void AFEC_ChCallback (uintptr_t context, AFEC_INTERRUPT_MASK event_status);
	
	AFEC_ChannelCallbackSet(AFEC_ChCallback, NULL);
    </code>

    Remarks:
    None.
*/

typedef void (*AFEC_CALLBACK)( uintptr_t context, AFEC_INTERRUPT_MASK event_status );


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_AFEC_H

/**
 End of File
*/

