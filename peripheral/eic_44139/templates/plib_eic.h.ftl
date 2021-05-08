/*******************************************************************************
  External Interrupt Controller (EIC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${EIC_INSTANCE_NAME?lower_case}.h

  Summary
    EIC PLIB Header File.

  Description
    This file defines the interface to the EIC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

/* Guards against multiple inclusion */
#ifndef PLIB_${EIC_INSTANCE_NAME}_H
#define PLIB_${EIC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include <stdbool.h>

#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif /* __cplusplus */

#define TOTAL_EIC_PINS ${EIC_NUM_INTERRUPTS}U


typedef enum
{
<#list 0..EIC_NUM_INTERRUPTS - 1 as index>
    EIC_PIN_${index} = ${index}U${(index == EIC_NUM_INTERRUPTS - 1)?string("", ",")}
</#list>  
}EIC_PIN;


typedef enum
{
  EIC_POLARITY_FALLING_EDGE = 0U,
  EIC_POLARITY_ACTIVE_LOW = 0U,
  EIC_POLARITY_RISING_EDGE = 1U,
  EIC_POLARITY_ACTIVE_HIGH = 1U
}EIC_POLARITY;


typedef enum
{
  EIC_DETECTION_EDGE,
  EIC_DETECTION_LEVEL
}EIC_DETECTION;


typedef void (*EIC_CALLBACK) (void* context);


void ${EIC_INSTANCE_NAME}_Initialize(void);
bool ${EIC_INSTANCE_NAME}_RegisterCallback(EIC_PIN pin, EIC_CALLBACK callback, void* context);
bool ${EIC_INSTANCE_NAME}_EnableInterrupt(EIC_PIN pin);
bool ${EIC_INSTANCE_NAME}_DisableInterrupt(EIC_PIN pin);
bool ${EIC_INSTANCE_NAME}_SetPolarity(EIC_PIN pin, EIC_POLARITY polarity);
bool ${EIC_INSTANCE_NAME}_FreezeConfiguration(EIC_PIN pin);

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif /* __cplusplus */

#endif /* PLIB_${EIC_INSTANCE_NAME}_H */
