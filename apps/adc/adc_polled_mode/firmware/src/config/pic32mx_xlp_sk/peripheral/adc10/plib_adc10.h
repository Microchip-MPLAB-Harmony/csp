/*******************************************************************************
  ADC10 Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_adc10.h

  Summary
    ADC10 peripheral library interface.

  Description
    This file defines the interface to the ADC10 peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_ADC10_H    // Guards against multiple inclusion
#define PLIB_ADC10_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/
#include <device.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

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
typedef enum {
    ADC10_MUX_A,
    ADC10_MUX_B
} ADC10_MUX;

typedef enum {
    ADC10_RESULT_BUFFER_0 = 0,
    ADC10_RESULT_BUFFER_1,
    ADC10_RESULT_BUFFER_2,
    ADC10_RESULT_BUFFER_3,
    ADC10_RESULT_BUFFER_4,
    ADC10_RESULT_BUFFER_5,
    ADC10_RESULT_BUFFER_6,
    ADC10_RESULT_BUFFER_7,
    ADC10_RESULT_BUFFER_8,
    ADC10_RESULT_BUFFER_9,
    ADC10_RESULT_BUFFER_10,
    ADC10_RESULT_BUFFER_11,
    ADC10_RESULT_BUFFER_12,
    ADC10_RESULT_BUFFER_13,
    ADC10_RESULT_BUFFER_14,
    ADC10_RESULT_BUFFER_15
}ADC10_RESULT_BUFFER;

typedef enum
{
    ADC10_INPUT_POSITIVE_VDD_DIV_2 = 17,
    ADC10_INPUT_POSITIVE_IVREF = 14,
    ADC10_INPUT_POSITIVE_CTMUT = 13,
    ADC10_INPUT_POSITIVE_AN12 = 12,
    ADC10_INPUT_POSITIVE_AN11 = 11,
    ADC10_INPUT_POSITIVE_AN10 = 10,
    ADC10_INPUT_POSITIVE_AN9 = 9,
    ADC10_INPUT_POSITIVE_AN8 = 8,
    ADC10_INPUT_POSITIVE_AN7 = 7,
    ADC10_INPUT_POSITIVE_AN6 = 6,
    ADC10_INPUT_POSITIVE_AN5 = 5,
    ADC10_INPUT_POSITIVE_AN4 = 4,
    ADC10_INPUT_POSITIVE_AN3 = 3,
    ADC10_INPUT_POSITIVE_AN2 = 2,
    ADC10_INPUT_POSITIVE_AN1 = 1,
    ADC10_INPUT_POSITIVE_AN0 = 0,
}ADC10_INPUT_POSITIVE;

typedef enum
{
    ADC10_INPUT_NEGATIVE_AN1 = 1,
    ADC10_INPUT_NEGATIVE_VREFL = 0,
}ADC10_INPUT_NEGATIVE;

typedef enum
{
    ADC10_INPUT_SCAN_AN0 = 0x1,
    ADC10_INPUT_SCAN_AN1 = 0x2,
    ADC10_INPUT_SCAN_AN2 = 0x4,
    ADC10_INPUT_SCAN_AN3 = 0x8,
    ADC10_INPUT_SCAN_AN4 = 0x10,
    ADC10_INPUT_SCAN_AN5 = 0x20,
    ADC10_INPUT_SCAN_AN6 = 0x40,
    ADC10_INPUT_SCAN_AN7 = 0x80,
    ADC10_INPUT_SCAN_AN8 = 0x100,
    ADC10_INPUT_SCAN_AN9 = 0x200,
    ADC10_INPUT_SCAN_AN10 = 0x400,
    ADC10_INPUT_SCAN_AN11 = 0x800,
    ADC10_INPUT_SCAN_AN12 = 0x1000,
    ADC10_INPUT_SCAN_CTMUT = 0x2000,
    ADC10_INPUT_SCAN_IVREF = 0x4000,
    ADC10_INPUT_SCAN_AVSS = 0x8000,
    ADC10_INPUT_SCAN_VDD_DIV_2 = 0x20000,
}ADC10_INPUTS_SCAN;


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

void ADC10_Initialize (void);

void ADC10_Enable();
void ADC10_Disable();

void ADC10_SamplingStart(void);
void ADC10_ConversionStart(void);

void ADC10_InputSelect(ADC10_MUX muxType, ADC10_INPUT_POSITIVE positiveInput, ADC10_INPUT_NEGATIVE negativeInput );
void ADC10_InputScanSelect(ADC10_INPUTS_SCAN *scanList, uint8_t numChannels);

bool ADC10_ResultIsReady();
uint32_t ADC10_ResultGet(ADC10_RESULT_BUFFER bufferNumber);


// *****************************************************************************

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}
#endif
// DOM-IGNORE-END

#endif //PLIB_ADC10_H

/**
 End of File
*/
