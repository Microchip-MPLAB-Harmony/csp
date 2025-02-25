/*******************************************************************************
  CBG PLIB

  Company
    Microchip Technology Inc.

  File Name
  plib_${CBG_INSTANCE?lower_case}.h

  Summary
    CBG PLIB Header File.

  Description
    This file defines the interface to the CBG peripheral library.
    This library provides access to and control of the associated CBG.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_${CBG_INSTANCE}_H
#define PLIB_${CBG_INSTANCE}_H

// *****************************************************************************
// Section: Included Files
// *****************************************************************************

#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

/**
 * @brief    Initializes the ${CBG_INSTANCE} module
 * @details  Initializes the ${CBG_INSTANCE} peripheral of the device.
 * @pre      None
 * @param    None
 * @note     This function must be called only once and before any other ${CBG_INSTANCE} function is called.
 * 
 * @b Example:
 * @code
 *    IBIASCON = 0;  When there are no generator
 *    IBIASCON = 0x9  when steady current generators are selected
 *    CBG_Initialize();
 * @endcode
 * 
 * @remarks   None 
 * @return   None
 * 
 */
void ${CBG_INSTANCE}_Initialize (void);

/**
 * @brief Deinitializes the ${CBG_INSTANCE} peripheral of the device.
 *
 * @details This function deinitializes the ${CBG_INSTANCE} Peripheral Library (PLIB) of the device, 
 * returning the ${CBG_INSTANCE} peripheral to its default reset state. After calling this function, 
 * the ${CBG_INSTANCE} peripheral will no longer be operational.
 * 
 * @pre The ${CBG_INSTANCE} peripheral must have been initialized using the ${CBG_INSTANCE}_Initialize API.
 * 
 * @param None
 * 
 * @return None
 *
 * @note This function should be called when the ${CBG_INSTANCE} peripheral is no longer required 
 * to release resources and ensure proper reset behavior.
 *
 * @b Example
 * @code
 * ${CBG_INSTANCE}_Initialize();
 * Perform CBG operations here
 * ${CBG_INSTANCE}_Deinitialize();
 * @endcode
 *
 * @remarks None
 */
void ${CBG_INSTANCE}_Deinitialize(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
#endif
// DOM-IGNORE-END