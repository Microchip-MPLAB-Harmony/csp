/*******************************************************************************
  Interface definition of WDT PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${WDT_INSTANCE_NAME?lower_case}.h

  Summary:
    Interface definition of the Watch Dog Timer Plib (WDT).

  Description:
    This file defines the interface for the WDT Plib.
    It allows user to setup timeout duration and restart watch dog timer.
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

#ifndef PLIB_${WDT_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${WDT_INSTANCE_NAME}_H

// Section: Included Files

#include "device.h"
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// Section: Interface

<#if (CONFIG_FWDT_WDTEN?? && CONFIG_FWDT_WDTEN == "SW")>

/**
 * @brief    Enables the Watchdog Timer.
 * @param    None
 * @return   None
 * This function enables the Watchdog Timer.
 */
void ${WDT_INSTANCE_NAME}_Enable( void );

/**
 * @brief    Disables the Watchdog Timer.
 * @pre      WDT must be enabled using WDT_Enable()
 * @param    None
 * @return   None
 * This function disables the Watchdog Timer.
 */
void ${WDT_INSTANCE_NAME}_Disable( void );
</#if>

/**
 * @brief     Checks if the Watchdog Timer is enabled.
 * @param     None
 * @return    bool - true if enabled, false if disabled.
 * This function returns true if the Watchdog Timer is enabled, false otherwise.
 */
bool ${WDT_INSTANCE_NAME}_IsEnabled( void );

<#if (CONFIG_FWDT_WDTEN?? && CONFIG_FWDT_WDTEN == "SW")>

/**
 * @brief    Enables the window mode of the Watchdog Timer.
 * @pre      This API is generated to enable the Window mode in firmware if the window mode is disabled by setting WINDIS fuse bit to OFF/NORMAL in MHC device configuration.
 * @param    None
 * @return   None
 * This function enables the WDT window mode.
 */
void ${WDT_INSTANCE_NAME}_WindowEnable( void );

/**
 * @brief    Disables the window mode of the Watchdog Timer.
 * @pre      This API is generated to disable the Window mode in firmware if the window mode is disabled by setting WINDIS fuse bit to OFF/NORMAL in MHC device configuration.
 * @param    None
 * @return   None
 * This function disables the WDT window mode.
 */
void ${WDT_INSTANCE_NAME}_WindowDisable( void );
</#if>

/**
 * @brief     Checks if the window mode of the Watchdog Timer is enabled.
 * @param     None
 * @return    bool - true if window mode is enabled, false if disabled.
 * This function returns true if the window mode is enabled, false otherwise.
 */
bool ${WDT_INSTANCE_NAME}_IsWindowEnabled( void );

/**
 * @brief     Clears the Watchdog Timer.
 * @param     None
 * @pre       WDT must be enabled using WDT_Enable().
 * @return    None
 * This function resets the Watchdog Timer to prevent it from expiring.
 */
void ${WDT_INSTANCE_NAME}_Clear( void );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // PLIB_${WDT_INSTANCE_NAME}_H
