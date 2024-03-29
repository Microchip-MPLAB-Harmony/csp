/*******************************************************************************
  Digital-to-Analog Converter Controller (DACC) Peripheral Library (PLIB) header
  file

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DACC_INSTANCE_NAME?lower_case}.h

  Summary:
    DACC PLIB Header File

  Description:
    None

*******************************************************************************/

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

#ifndef PLIB_${DACC_INSTANCE_NAME}_H
#define PLIB_${DACC_INSTANCE_NAME}_H

#include "device.h"
#include "plib_dacc_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END



// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

/****************************** DACC API *********************************/
void ${DACC_INSTANCE_NAME}_Initialize(void);

bool ${DACC_INSTANCE_NAME}_IsReady(void);

<#if DACC_MR_TAG_ENABLE == true>
void ${DACC_INSTANCE_NAME}_ChannelDataWrite(DACC_CHANNEL_NUM channel, uint16_t data);
<#else>
void ${DACC_INSTANCE_NAME}_ChannelSelect(DACC_CHANNEL_NUM channel);

void ${DACC_INSTANCE_NAME}_DataWrite(uint16_t data);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_${DACC_INSTANCE_NAME}_H
