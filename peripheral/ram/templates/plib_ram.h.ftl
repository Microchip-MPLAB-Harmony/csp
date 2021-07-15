/*******************************************************************************
  (${RAM_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RAM_INSTANCE_NAME?lower_case}.h

  Summary:
    ${RAM_INSTANCE_NAME} PLIB Header file

  Description:
    This file defines the interface to the RAM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#ifndef PLIB_${RAM_INSTANCE_NAME}_H
#define PLIB_${RAM_INSTANCE_NAME}_H

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
#include "device.h"

#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif

bool ${RAM_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address );

bool ${RAM_INSTANCE_NAME}_Write( uint32_t *data, uint32_t length, uint32_t address );

bool ${RAM_INSTANCE_NAME}_IsBusy(void);

#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif

#endif /* PLIB_${RAM_INSTANCE_NAME}_H */
