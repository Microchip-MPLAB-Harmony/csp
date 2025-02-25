/*******************************************************************************
  Deadman Timer (${DMT_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DMT_INSTANCE_NAME?lower_case}.h

  Summary:
    ${DMT_INSTANCE_NAME} PLIB Header file

  Description:
    This file defines the interface to the RTC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#ifndef PLIB_${DMT_INSTANCE_NAME}_H
#define PLIB_${DMT_INSTANCE_NAME}_H

// Section: Included Files

#include <stddef.h>
#include <stdint.h>
#include <stdbool.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// Section: Interface Routines

/**
 * @brief    Initializes the ${DMT_INSTANCE_NAME} module
 * @details  Initializes the ${DMT_INSTANCE_NAME} peripheral of the device.
 * @pre      None
 * @param    None
 * @note     This function must be called only once and before any other ${DMT_INSTANCE_NAME} function is called.
 * 
 * @b Example:
 * @code
 *    PSCNT = 0x1234;   Set the instruction fetch counter limit
 *    PSINTV = 0x5678;  Set the window interval limit
 *    DMT_Initialize();
 * @endcode
 * 
 * remarks   None 
 * @return   None
 * 
 */
void ${DMT_INSTANCE_NAME}_Initialize(void);

/**
 * @brief    Writes the Clear Pattern for DMTPRECLR register. 
 * @details  This function writes the required clear pattern to the DMTPRECLR register to prepare the DMT module for a subsequent clear operation.
 * @pre      This function should be called before calling \ref DMTClear
 * @param    None
 * @note     This function ensures that the DMT module is ready to be cleared. It must be called before the DMTClear function to avoid any unintended behavior.
 * 
 * @b Example:
 * @code
 *        DMTPreClear();
 *        DMTClear();
 * @endcode
 * @remarks  None
 * @return   None
 */
void ${DMT_INSTANCE_NAME}_Clear( void );

/**
 * @brief    Enables the DMT module
 * @details  This function enables the DMT (Dead Man Timer) module, allowing it to start monitoring the system.
 * @pre      The DMT module should be properly initialized before calling this function.
 * @note     Ensure that the DMT module is configured correctly before enabling it to avoid unintended behavior.
 * @param    None
 * 
 * @b Example:
 * @code
 *        DMT_Initialize();  Initialize the DMT module
 *        DMT_Enable();      Enable the DMT module
 * @endcode
 * @return   None
 */
void ${DMT_INSTANCE_NAME}_Enable( void );

/**
 * @brief    Returns the Window Open status
 * @pre      DMT must be enabled using DMT_Enable().
 * @note     This function should be called to ensure that the DMT window is open before attempting to clear the DMT. 
 * @details  This function checks the status of the Window Open bit in the DMT status register and returns whether the window is open or not.
 * @param    None
 * @b Example:
 * @code
 *        uint32_t statusValue = 0;
 *        statusValue = ${DMT_INSTANCE_NAME}_StatusGet();
 * @endcode
 * @return   true  - Window Open status bit is set 
 * @return   false - Window Open status bit is not set

 */
bool ${DMT_INSTANCE_NAME}_ClearWindowStatusGet( void );

/**
 * @brief     Returns the current counter value 
 * @details   This function reads and returns the current value of the DMT counter. 
 * @note      The returned counter value is the raw value from the DMT counter register and does not account for the instructions involved in the call-stack-push, reading the SFR (Special Function Register), and call-stack-pop operations.
 * @pre       Value will not be compensated for the instructions involved in 
 *            call-stack-push, reading SFR and call-stack-pop operations.
 * @param     None
 * @b Example:
 * @code
 *    uint32_t CounterValue = 0;
 *    CounterValue = ${DMT_INSTANCE_NAME}_CounterGet();
 * @endcode
 * @return    Returns the 32 bit counter value
 */
uint32_t ${DMT_INSTANCE_NAME}_CounterGet( void );

/**
 * @brief    Reads the DMT counter register 
 * @details  This function reads and returns the current value of the DMT timeout counter register. The counter value is a 32-bit number representing the current count of the DMT.
 * @pre      DMT must be enabled using DMT_Enable().
 * @note     The returned counter value is the raw value from the DMT timeout counter register and does not account for the instructions involved in the call-stack-push, reading the SFR (Special Function Register), and call-stack-pop operations. Therefore, the value may be slightly different from the exact moment the function is called.
 * @param    None
 * 
 * @b Example:
 * @code
 *        uint32_t WindowCounterValue = 0;
 *        WindowCounterValue = DMT_TimeoutCounterGet();
 * @endcode
 * @return   32-bit timeout counter value
 * @remarks  None
 */
uint32_t ${DMT_INSTANCE_NAME}_TimeOutCountGet( void );

/**
 * @brief    Reads the DMT Window Interval Counter
 * @details  This function reads and returns the current value of the DMT window interval counter. The counter value is a 32-bit number representing the current count within the DMT window interval.
 * @pre      DMT must be enabled using DMT_Enable().
 * @note     The returned counter value is the raw value from the DMT window interval counter register and does not account for the instructions involved in the call-stack-push, reading the SFR (Special Function Register), and call-stack-pop operations. Therefore, the value may be slightly different from the exact moment the function is called.
 * 
 * @b Example:
 * @code
 *        if(DMT_IsWindowOpen())
 *        { 
 *            statement1;
 *            statement2;
 *        }
 * @endcode
 * @param    None
 * @return   32-bit window interval counter value
 * @remarks  None
 */
uint32_t ${DMT_INSTANCE_NAME}_WindowIntervalGet( void );

/**
 * @brief    Performs clear sequence for the DMT Event and all other DMT flags, 
 *           post occurrence of DMT Event.
 * @pre      The DMT event must have occurred, and the system should be in a state where it is safe to clear the DMT flags.
 * @details  This function performs the necessary sequence to clear the DMT event flag and any other related DMT flags. This is typically done after handling a DMT event to reset the DMT status and prepare for future DMT events.
 * @note     Ensure that the DMT event has been properly handled before calling this function to clear the flags. Clearing the flags prematurely may result in loss of important status information.
 * 
 * @b Example:
 * @code
 *        if(DMT_IsPreCleared())
 *        { 
 *            statement1;
 *            statement2;
 *        }
 * @endcode
 * @param    None
 * @return   None 
 * @remarks  None
 */
void DMT_PostEventClear(void);

/**
 * @brief     Gets the DMT status
 * @details   This function reads and returns the current status of the DMT. The status value is a 32-bit number representing various status flags and conditions of the DMT.
 * @param     None
 * @note      The returned status value is the raw value from the DMT status register and may need to be interpreted based on the specific bits defined for the DMT status.
 * 
 * @b Example:
 * @code
 *        uint32_t statusValue = 0;
 *        statusValue = DMT_StatusGet();
 * @endcode  
 * @return    Status value of DMT
 * @remarks   None
 */
uint32_t ${DMT_INSTANCE_NAME}_StatusGet(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${DMT_INSTANCE_NAME}_H */