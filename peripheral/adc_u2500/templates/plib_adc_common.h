/*******************************************************************************
  Analog-to-Digital Converter(ADC) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_adc_common.h

  Summary
    ADC Peripheral Library Interface Header File.

  Description
    This file defines the common types for the ADC peripheral library. This
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

    /* ADC pin AIN12 */
    ADC_POSINPUT_AIN12 = ADC_INPUTCTRL_MUXPOS_AIN12,

    /* ADC pin AIN13 */
    ADC_POSINPUT_AIN13 = ADC_INPUTCTRL_MUXPOS_AIN13,

    /* ADC pin AIN14 */
    ADC_POSINPUT_AIN14 = ADC_INPUTCTRL_MUXPOS_AIN14,

    /* ADC pin AIN15 */
    ADC_POSINPUT_AIN15 = ADC_INPUTCTRL_MUXPOS_AIN15,

    /* ADC pin AIN16 */
    ADC_POSINPUT_AIN16 = ADC_INPUTCTRL_MUXPOS_AIN16,

        /* ADC pin AIN17 */
    ADC_POSINPUT_AIN17 = ADC_INPUTCTRL_MUXPOS_AIN17,

        /* ADC pin AIN18 */
    ADC_POSINPUT_AIN18 = ADC_INPUTCTRL_MUXPOS_AIN18,

        /* ADC pin AIN19 */
    ADC_POSINPUT_AIN19 = ADC_INPUTCTRL_MUXPOS_AIN19,

        /* ADC pin AIN20 */
    ADC_POSINPUT_AIN20 = ADC_INPUTCTRL_MUXPOS_AIN20,

        /* ADC pin AIN21 */
    ADC_POSINPUT_AIN21 = ADC_INPUTCTRL_MUXPOS_AIN21,

        /* ADC pin AIN22 */
    ADC_POSINPUT_AIN22 = ADC_INPUTCTRL_MUXPOS_AIN22,

        /* ADC pin AIN23 */
    ADC_POSINPUT_AIN23 = ADC_INPUTCTRL_MUXPOS_AIN23,

    /* ADC pin SCALEDCOREVCC */
    ADC_POSINPUT_SCALEDCOREVCC = ADC_INPUTCTRL_MUXPOS_SCALEDCOREVCC,

    /* ADC pin SCALEDVBAT */
    ADC_POSINPUT_SCALEDVBAT = ADC_INPUTCTRL_MUXPOS_SCALEDVBAT,

    /* ADC pin SCALEDIOVCC */
    ADC_POSINPUT_SCALEDIOVCC = ADC_INPUTCTRL_MUXPOS_SCALEDIOVCC,

    /* ADC pin BANDGAP */
    ADC_POSINPUT_BANDGAP = ADC_INPUTCTRL_MUXPOS_BANDGAP,

    /* ADC pin PTAT */
    ADC_POSINPUT_PTAT = ADC_INPUTCTRL_MUXPOS_PTAT,

    /* ADC pin CTAT */
    ADC_POSINPUT_CTAT = ADC_INPUTCTRL_MUXPOS_CTAT,

    /* ADC pin DAC */
    ADC_POSINPUT_DAC = ADC_INPUTCTRL_MUXPOS_DAC,

    /* ADC pin DAC */
    ADC_POSINPUT_PTC = ADC_INPUTCTRL_MUXPOS_PTC,

} ADC_POSINPUT;

// *****************************************************************************

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


typedef enum
{
    ADC_STATUS_RESRDY = ADC_INTFLAG_RESRDY_Msk,
    ADC_STATUS_WINMON = ADC_INTFLAG_WINMON_Msk,
    /* Force compiler to reserve 32-bit for this enum */
    ADC_STATUS_INVALID = 0xFFFFFFFF
}ADC_STATUS;
// *****************************************************************************


typedef void (*ADC_CALLBACK)(ADC_STATUS status, uintptr_t context);


typedef struct
{
    ADC_CALLBACK callback;

    uintptr_t context;

} ADC_CALLBACK_OBJ;



// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_ADC_COMMON_H*/
