/*******************************************************************************
  ADCHS Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_adchs_common.h

  Summary
    Commonly needed stuff for the ADCHS peripheral libraries interfaces.

  Description
    This file defines several items commonly needed by the interfaces to 
    the ADCHS peripheral libraries.

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

#ifndef PLIB_ADCHS_COMMON_H    // Guards against multiple inclusion
#define PLIB_ADCHS_COMMON_H


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

// *****************************************************************************
typedef enum
{
    ADCHS_CH0_MASK = (1U << 0U),
    ADCHS_CH1_MASK = (1U << 1U),
    ADCHS_CH2_MASK = (1U << 2U),
    ADCHS_CH3_MASK = (1U << 3U),
    ADCHS_CH4_MASK = (1U << 4U),
    ADCHS_CH5_MASK = (1U << 5U),
    ADCHS_CH6_MASK = (1U << 6U),
    ADCHS_CH7_MASK = (1U << 7U),
    ADCHS_CH8_MASK = (1U << 8U),
    ADCHS_CH9_MASK = (1U << 9U),
    ADCHS_CH10_MASK = (1U << 10U),
    ADCHS_CH11_MASK = (1U << 11U),
    ADCHS_CH12_MASK = (1U << 12U),
    ADCHS_CH13_MASK = (1U << 13U),
    ADCHS_CH14_MASK = (1U << 14U),
    ADCHS_CH15_MASK = (1U << 15U),
    ADCHS_CH16_MASK = (1U << 16U),
    ADCHS_CH17_MASK = (1U << 17U),
    ADCHS_CH18_MASK = (1U << 18U),
    ADCHS_CH19_MASK = (1U << 19U),
    ADCHS_CH20_MASK = (1U << 20U),
    ADCHS_CH21_MASK = (1U << 21U),
    ADCHS_CH22_MASK = (1U << 22U),
    ADCHS_CH23_MASK = (1U << 23U),
    ADCHS_CH24_MASK = (1U << 24U),
    ADCHS_CH25_MASK = (1U << 25U),
    ADCHS_CH26_MASK = (1U << 26U),
    ADCHS_CH27_MASK = (1U << 27U),
    ADCHS_CH28_MASK = (1U << 28U),
    ADCHS_CH29_MASK = (1U << 29U),
    ADCHS_CH30_MASK = (1U << 30U),
    ADCHS_CH31_MASK = (1U << 31U)
}ADCHS_CHANNEL_MASK;

typedef enum
{
    ADCHS_CH0 = 0U,
    ADCHS_CH1,
    ADCHS_CH2,
    ADCHS_CH3,
    ADCHS_CH4,
    ADCHS_CH5,
    ADCHS_CH6,
    ADCHS_CH7,
    ADCHS_CH8,
    ADCHS_CH9,
    ADCHS_CH10,
    ADCHS_CH11,
    ADCHS_CH12,
    ADCHS_CH13,
    ADCHS_CH14,
    ADCHS_CH15,
    ADCHS_CH16,
    ADCHS_CH17,
    ADCHS_CH18,
    ADCHS_CH19,
    ADCHS_CH20,
    ADCHS_CH21,
    ADCHS_CH22,
    ADCHS_CH23,
    ADCHS_CH24,
    ADCHS_CH25,
    ADCHS_CH26,
    ADCHS_CH27,
    ADCHS_CH28,
    ADCHS_CH29,
    ADCHS_CH30,
    ADCHS_CH31,
}ADCHS_CHANNEL_NUM;

// *****************************************************************************

typedef enum
{
    ADCHS_INTERRUPT_EOC_0_MASK = (1U << 0U),
    ADCHS_INTERRUPT_EOC_1_MASK = (1U << 1U),
    ADCHS_INTERRUPT_EOC_2_MASK = (1U << 2U),
    ADCHS_INTERRUPT_EOC_3_MASK = (1U << 3U),
    ADCHS_INTERRUPT_EOC_4_MASK = (1U << 4U),
    ADCHS_INTERRUPT_EOC_5_MASK = (1U << 5U),
    ADCHS_INTERRUPT_EOC_6_MASK = (1U << 6U),
    ADCHS_INTERRUPT_EOC_7_MASK = (1U << 7U),
    ADCHS_INTERRUPT_EOC_8_MASK = (1U << 8U),
    ADCHS_INTERRUPT_EOC_9_MASK = (1U << 9U),
    ADCHS_INTERRUPT_EOC_10_MASK = (1U << 10U),
    ADCHS_INTERRUPT_EOC_11_MASK = (1U << 11U),
    ADCHS_INTERRUPT_EOC_12_MASK = (1U << 12U),
    ADCHS_INTERRUPT_EOC_13_MASK = (1U << 13U),
    ADCHS_INTERRUPT_EOC_14_MASK = (1U << 14U),
    ADCHS_INTERRUPT_EOC_15_MASK = (1U << 15U),
    ADCHS_INTERRUPT_EOC_16_MASK = (1U << 16U),
    ADCHS_INTERRUPT_EOC_17_MASK = (1U << 17U),
    ADCHS_INTERRUPT_EOC_18_MASK = (1U << 18U),
    ADCHS_INTERRUPT_EOC_19_MASK = (1U << 19U),
    ADCHS_INTERRUPT_EOC_20_MASK = (1U << 20U),
    ADCHS_INTERRUPT_EOC_21_MASK = (1U << 21U),
    ADCHS_INTERRUPT_EOC_22_MASK = (1U << 22U),
    ADCHS_INTERRUPT_EOC_23_MASK = (1U << 23U),
    ADCHS_INTERRUPT_EOC_24_MASK = (1U << 24U),
    ADCHS_INTERRUPT_EOC_25_MASK = (1U << 25U),
    ADCHS_INTERRUPT_EOC_26_MASK = (1U << 26U),
    ADCHS_INTERRUPT_EOC_27_MASK = (1U << 27U),
    ADCHS_INTERRUPT_EOC_28_MASK = (1U << 28U),
    ADCHS_INTERRUPT_EOC_29_MASK = (1U << 29U),
    ADCHS_INTERRUPT_EOC_30_MASK = (1U << 30U),
    ADCHS_INTERRUPT_EOC_31_MASK = (1U << 31U),
}ADCHS_INTERRUPT_MASK;

// *****************************************************************************

typedef void (*ADCHS_CALLBACK)( uintptr_t context);
// *****************************************************************************

typedef struct
{
    ADCHS_CALLBACK callback_fn;
    uintptr_t context;
}ADCHS_CALLBACK_OBJECT;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //PLIB_ADCHS_COMMMON_H

/**
 End of File
*/

