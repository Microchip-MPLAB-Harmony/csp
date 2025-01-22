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


// *****************************************************************************
// Section: Included Files
// *****************************************************************************

#include <stdbool.h>
#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

<#assign generateDoxygen = false>
<#if generateDoxygen>
/**
 * @ingroup  rcon
 * @brief    Initializes the RCON module
 * @return   none
 */
</#if>

typedef enum
{
<#list 0..(RCON_CAUSE_COUNT - 1) as i>
    <#assign RCON_CAUSE = "RCON_CAUSE_" + i>
    RCON_RESET_CAUSE_${.vars[RCON_CAUSE]} = _RCON_${.vars[RCON_CAUSE]}_MASK,

</#list>
} RCON_RESET_CAUSE;
<#assign generateDoxygen = false>
<#if generateDoxygen>
/**
 * @brief    This enumeration identifies the possible reason of device reset.
 * Identifies the possible reason of device reset.
 */
 </#if>

// *****************************************************************************
// Section: Interface
// *****************************************************************************

<#assign generateDoxygen = false>
<#if generateDoxygen>
 /**
 * @brief    This function returns the cause of the last reset. The reset could be due to multiple reasons. The application should compare the returned value against different values in the RCON_RESET_CAUSE enumeration to identify the possible causes.
 * @param    None
 * @return   RCON_RESET_CAUSE - Identifies type of reset.
 * @pre      None
 * Reports the cause of the last reset.
 */
 </#if>
RCON_RESET_CAUSE ${RCON_INSTANCE_NAME}_ResetCauseGet( void );

<#assign generateDoxygen = false>
<#if generateDoxygen>
/**
 * @brief    This function clears the particular reset bit in the RCON register. Multiple reasons for a reset can be ORed together and given as an input parameter to clear them simultaneously.
 * @param    Reset status needs to be clear
 * @return   None
 * @pre      None
 * Clears the particular reset cause status bit.
 */
 </#if>
void ${RCON_INSTANCE_NAME}_ResetCauseClear( RCON_RESET_CAUSE cause );

<#assign generateDoxygen = false>
<#if generateDoxygen>
/**
 * @brief    Clears the Reset Cause register
 * @return   none  
 */
</#if>
void ${RCON_INSTANCE_NAME}_CauseClearAll(void);


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${RCON_INSTANCE_NAME}_H */