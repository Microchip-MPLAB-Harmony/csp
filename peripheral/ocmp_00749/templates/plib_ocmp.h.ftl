/*******************************************************************************
  Output Compare (OCMP) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${OCMP_INSTANCE_NAME?lower_case}.h

  Summary:
    OCMP PLIB Header File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${OCMP_INSTANCE_NAME}_H
#define PLIB_${OCMP_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"
#include "plib_ocmp_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END


// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************
<#assign mode = OCMP_OCxCON_OCM?number>

/*************************** ${OCMP_INSTANCE_NAME} API ****************************************/
// *****************************************************************************
/* Function:
   void ${OCMP_INSTANCE_NAME}_Initialize (void)

  Summary:
    Initialization function ${OCMP_INSTANCE_NAME} peripheral

  Description:
    This function initializes the ${OCMP_INSTANCE_NAME} peripheral with user input
	from the configurator.

  Parameters:
    void

  Returns:
    void
*/
void ${OCMP_INSTANCE_NAME}_Initialize (void);

// *****************************************************************************
/* Function:
   void ${OCMP_INSTANCE_NAME}_Enable (void)

  Summary:
    Enable function ${OCMP_INSTANCE_NAME} peripheral

  Description:
    This function enables the ${OCMP_INSTANCE_NAME} peripheral

  Parameters:
    void

  Returns:
    void
*/
void ${OCMP_INSTANCE_NAME}_Enable (void);

// *****************************************************************************
/* Function:
   void ${OCMP_INSTANCE_NAME}_Disable (void)

  Summary:
    Disable function ${OCMP_INSTANCE_NAME} peripheral

  Description:
    This function disables the ${OCMP_INSTANCE_NAME} peripheral.

  Parameters:
    void

  Returns:
    void
*/
void ${OCMP_INSTANCE_NAME}_Disable (void);

<#if mode == 7>
// *****************************************************************************
/* Function:
   bool ${OCMP_INSTANCE_NAME}_FaultStatusGet (void)

  Summary:
    Get ${OCMP_INSTANCE_NAME} status

  Description:
    Returns the current state of PWM Fault Condition status bit

  Parameters:
    void

  Returns:
    bool
*/
bool ${OCMP_INSTANCE_NAME}_FaultStatusGet (void);
</#if>

<#if mode lt 6>
<#if OCMP_OCxCON_OC32 == "1">
void ${OCMP_INSTANCE_NAME}_CompareValueSet (uint32_t value);
<#else>
void ${OCMP_INSTANCE_NAME}_CompareValueSet (uint16_t value);
</#if>
</#if>

<#if OCMP_OCxCON_OC32 == "1">
uint32_t ${OCMP_INSTANCE_NAME}_CompareValueGet (void);
<#else>
uint16_t ${OCMP_INSTANCE_NAME}_CompareValueGet (void);
</#if>

<#if mode gt 3 >
<#if OCMP_OCxCON_OC32 == "1">
uint32_t ${OCMP_INSTANCE_NAME}_CompareSecondaryValueGet (void);
void ${OCMP_INSTANCE_NAME}_CompareSecondaryValueSet (uint32_t value);
<#else>
uint16_t ${OCMP_INSTANCE_NAME}_CompareSecondaryValueGet (void);
void ${OCMP_INSTANCE_NAME}_CompareSecondaryValueSet (uint16_t value);
</#if>
</#if>

<#if OCMP_INTERRUPT_ENABLE == true>
// *****************************************************************************
/* Function:
  void ${OCMP_INSTANCE_NAME}_CallbackRegister( OCMP_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a ocmp interrupt.

  Description:
    This function sets the callback function that will be called when the OCMP
    conditions are met.

  Precondition:
    None.

  Parameters:
    *callback   - a pointer to the function to be called when value is reached.
                  Use NULL to Un Register the compare callback

    context     - a pointer to user defined data to be used when the callback
                  function is called. NULL can be passed in if no data needed.

  Returns:
    void
*/
void ${OCMP_INSTANCE_NAME}_CallbackRegister(OCMP_CALLBACK callback, uintptr_t context);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // PLIB_${OCMP_INSTANCE_NAME}_H
