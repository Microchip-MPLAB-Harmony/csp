/*******************************************************************************
  Digital-to-Analog Converter (${DAC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DAC_INSTANCE_NAME?lower_case}.h

  Summary:
    ${DAC_INSTANCE_NAME} PLIB Header file

  Description:
    This file defines the interface to the DAC peripheral library. This
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

#ifndef PLIB_${DAC_INSTANCE_NAME}_H
#define PLIB_${DAC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif

typedef enum
{
    /* Channel 0 */
    DAC_CHANNEL_0,

    /* Channel 1 */
    DAC_CHANNEL_1
} DAC_CHANNEL_NUM;

void ${DAC_INSTANCE_NAME}_Initialize (void);
void ${DAC_INSTANCE_NAME}_DataWrite (DAC_CHANNEL_NUM channel, uint16_t data);
<#if DAC_CHANNEL_0_FILTER>uint16_t ${DAC_INSTANCE_NAME}_Channel0ResultGet (void);</#if>
<#if DAC_CHANNEL_1_FILTER>uint16_t ${DAC_INSTANCE_NAME}_Channel1ResultGet (void);</#if>
bool ${DAC_INSTANCE_NAME}_IsReady (DAC_CHANNEL_NUM channel);

#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif

#endif /* PLIB_${DAC_INSTANCE_NAME}_H */
