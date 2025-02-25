/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}_common.h
 
  Summary:
    ADC Common Header File
 
  Description:
    This file has prototype of all the interfaces which are common for all the
    ADC peripherals.
 
*******************************************************************************/
 
/*******************************************************************************
* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_ADC_COMMON_H
#define PLIB_ADC_COMMON_H

#include <stdint.h>

// /cond IGNORE_THIS
/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif
// /endcond

// Section: Common Definitions

/**
 @enum     ADC_PWM_TRIGGERS
 @brief    Defines the PWM triggers that are available in each individual PWM.
*/
typedef enum
{
    ADC_PWM_TRIGGER_1 = 1,     /**< PWM TRIGGER 1 */
    ADC_PWM_TRIGGER_2 = 2,     /**< PWM TRIGGER 2 */
} ADC_PWM_TRIGGERS;

/** 
  @brief    Callback function prototype for ADC Channel conversion complete interrupt
*/
typedef void (*ADC_CHANNEL_CALLBACK)(uint32_t result, uintptr_t context);

/** 
  @brief    Callback function prototype for ADC Comparator event
*/
typedef void (*ADC_CMP_CALLBACK)(uintptr_t context);

/**
 * @brief    Defines the interrupt priority values.
*/
typedef enum 
{
	INTERRUPT_PRIORITY_1,
	INTERRUPT_PRIORITY_2,
	INTERRUPT_PRIORITY_3,
	INTERRUPT_PRIORITY_4,
	INTERRUPT_PRIORITY_5,
	INTERRUPT_PRIORITY_6,
	INTERRUPT_PRIORITY_7,
	INTERRUPT_MAX_PRIORITY
} INTERRUPT_PRIORITY;

// /cond IGNORE_THIS
// Section: Local Objects **** Do Not Use ****

typedef struct
{
    ADC_CHANNEL_CALLBACK            callback;
    uintptr_t                       context;
} ADC_CHANNEL_OBJECT;

typedef struct
{
    ADC_CMP_CALLBACK                callback;
    uintptr_t                       context;
} ADC_CMP_OBJECT;


// /endcond

// /cond IGNORE_THIS
/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif
// /endcond

#endif  //PLIB_ADC_COMMON_H
