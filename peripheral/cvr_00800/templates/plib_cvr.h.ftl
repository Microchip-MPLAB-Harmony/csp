/*******************************************************************************
  Comparator Voltage Reference (CVR) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CVR_INSTANCE_NAME?lower_case}.h

  Summary:
    CVR PLIB Header File

  Description:
    None

*******************************************************************************/

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

#ifndef PLIB_${CVR_INSTANCE_NAME}_H
#define PLIB_${CVR_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END


// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

/*************************** ${CVR_INSTANCE_NAME} API ***************************/

void ${CVR_INSTANCE_NAME}_Initialize (void);

void ${CVR_INSTANCE_NAME}_Start (void);

void ${CVR_INSTANCE_NAME}_Stop (void);

void ${CVR_INSTANCE_NAME}_UpdateValue (uint8_t value);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // PLIB_${CVR_INSTANCE_NAME}_H
