/*******************************************************************************
  ADC Peripheral Library Interface Common Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_adc_common.h

  Summary
    ADC peripheral library common interface.

  Description
    This file defines the common interface to the ADC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_ADC_COMMON_H    // Guards against multiple inclusion
#define PLIB_ADC_COMMON_H


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

/* Identifies ADC channel mask */
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

/* Analog channel numbers */
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

/* Interrupt sources number */
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

/* Callback Function Pointer */
typedef void (*ADC_CALLBACK)( uintptr_t context);

/* Callback structure */
typedef struct
{
    ADC_CALLBACK callback_fn;
    uintptr_t context;
}ADC_CALLBACK_OBJECT;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_ADC_COMMMON_H

/**
 End of File
*/
