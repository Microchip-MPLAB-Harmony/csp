/*******************************************************************************
  Resets (${RCON_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${RCON_INSTANCE_NAME?lower_case}.h

  Summary
    ${RCON_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the RCON peripheral library.
    This library provides access to and control of the associated Resets.

  Remarks:
    None.

*******************************************************************************/

#ifndef PLIB_${RCON_INSTANCE_NAME}_H      // Guards against multiple inclusion
#define PLIB_${RCON_INSTANCE_NAME}_H

// Section: Included Files

#include <stdbool.h>
#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END


/**
 * @summary  Identifies the possible reason of device reset.
 * @brief    This enumeration identifies the possible reason of device reset.
 * @remarks  None
 */
typedef enum
{
<#list 0..(RCON_CAUSE_COUNT - 1) as i>
    <#assign RCON_CAUSE = "RCON_CAUSE_" + i>
    RCON_RESET_CAUSE_${.vars[RCON_CAUSE]} = _RCON_${.vars[RCON_CAUSE]}_MASK,

</#list>
} RCON_RESET_CAUSE;

// Section: Interface

/**
 * @brief    Reports the cause of the last reset.
 * @details  This function returns the cause of the last reset. The reset could be due to multiple reasons. The application should compare the returned value against different values in the RCON_RESET_CAUSE enumeration to identify the possible causes.
 * @pre      None
 * @param    None
 * @note     This function can be called multiple times to retrieve the reset cause, but the reset cause bits may be cleared by other operations.
 * @remarks  None
 * @return   RCON_RESET_CAUSE - Identifies type of reset.
 * 
 */
RCON_RESET_CAUSE ${RCON_INSTANCE_NAME}_ResetCauseGet( void );

/**
 * @brief    Clears the particular reset cause status bit.
 * @details  This function clears the particular reset bit in the RCON register. Multiple reasons for a reset can be ORed together and given as an input parameter to clear them simultaneously.
 * @pre      None
 * @param    Reset status needs to be clear
 * @note     This function should be called to clear the reset cause bits after they have been retrieved using ${RCON_INSTANCE_NAME}_ResetCauseGet, to ensure that subsequent resets can be accurately detected.
 * @remarks  None
 * @return   None.
 * 
 */
void ${RCON_INSTANCE_NAME}_ResetCauseClear( RCON_RESET_CAUSE cause );

/**
 * @brief    Clears all reset causes in the ${RCON_INSTANCE_NAME} module
 * @details  This function clears all the reset cause bits in the ${RCON_INSTANCE_NAME} peripheral.
 * @pre      This function should be called after the reset causes have been retrieved and handled.
 * @param    None
 * @note     This function should be called to clear all reset cause bits after they have been retrieved using ${RCON_INSTANCE_NAME}_ResetCauseGet, to ensure that subsequent resets can be accurately detected.
 * 
 * @remarks  Ensure that all reset cause bits are cleared to avoid misinterpretation of future reset causes.
 * @return   None
 * 
 */
void ${RCON_INSTANCE_NAME}_CauseClearAll(void);


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${RCON_INSTANCE_NAME}_H */