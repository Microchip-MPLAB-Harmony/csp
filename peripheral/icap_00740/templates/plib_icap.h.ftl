/*******************************************************************************
  Input Capture (ICAP) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${ICAP_INSTANCE_NAME?lower_case}.h

  Summary:
    ICAP PLIB Header File

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

#ifndef _PLIB_${ICAP_INSTANCE_NAME}_H
#define _PLIB_${ICAP_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"
#include "plib_icap_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END


// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

// *************************** ${ICAP_INSTANCE_NAME} API ***************************************/
// *****************************************************************************
/* Function:
   void ${ICAP_INSTANCE_NAME}_Initialize (void)

  Summary:
    Initialization function ${ICAP_INSTANCE_NAME} peripheral

  Description:
    This function initializes the ${ICAP_INSTANCE_NAME} peripheral with user input
    from the configurator.

  Parameters:
    none

  Returns:
    void
*/
void ${ICAP_INSTANCE_NAME}_Initialize (void);

// *****************************************************************************
/* Function:
   void ${ICAP_INSTANCE_NAME}_Enable (void)

  Summary:
    Enable function for the ${ICAP_INSTANCE_NAME} peripheral

  Description:
    This function enables the ${ICAP_INSTANCE_NAME} peripheral.

  Parameters:
    none

  Returns:
    void
*/
void ${ICAP_INSTANCE_NAME}_Enable (void);

// *****************************************************************************
/* Function:
   void ${ICAP_INSTANCE_NAME}_Disable (void)

  Summary:
    Disable function for the ${ICAP_INSTANCE_NAME} peripheral

  Description:
    This function disables the ${ICAP_INSTANCE_NAME} peripheral.

  Parameters:
    none

  Returns:
    void
*/
void ${ICAP_INSTANCE_NAME}_Disable (void);

<#if ICAP_ICxCON_C32 == "1">
// *****************************************************************************
/* Function:
   uint32_t ${ICAP_INSTANCE_NAME}_CaptureBufferRead (void)

  Summary:
    Read buffer function ${ICAP_INSTANCE_NAME} peripheral

  Description:
    This function will return the value contained in the ${ICAP_INSTANCE_NAME} peripheral
    buffer.

  Parameters:
    none

  Returns:
    uint32_t
*/
uint32_t ${ICAP_INSTANCE_NAME}_CaptureBufferRead (void);

<#else>
// *****************************************************************************
/* Function:
   uint16_t ${ICAP_INSTANCE_NAME}_CaptureBufferRead (void)

  Summary:
    Read buffer function ${ICAP_INSTANCE_NAME} peripheral

  Description:
    This function will return the value contained in the ${ICAP_INSTANCE_NAME} peripheral
    buffer.

  Parameters:
    none

  Returns:
    uint16_t
*/
uint16_t ${ICAP_INSTANCE_NAME}_CaptureBufferRead (void);
</#if>

<#if ICAP_INTERRUPT_ENABLE?c == "true">
// *****************************************************************************
/* Function:
  void ${ICAP_INSTANCE_NAME}_CallbackRegister( ICAP_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a icap interrupt.

  Description:
    This function sets the callback function that will be called when the ICAP
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
void ${ICAP_INSTANCE_NAME}_CallbackRegister(ICAP_CALLBACK callback, uintptr_t context);

<#else>
// *****************************************************************************
/* Function:
   void ${ICAP_INSTANCE_NAME}_CaptureStatusGet (void)

  Summary:
    ${ICAP_INSTANCE_NAME} status

  Description:
    Returns the current state overflow or buffer not empty flags

  Parameters:
    None

  Returns:
    bool
*/
bool ${ICAP_INSTANCE_NAME}_CaptureStatusGet (void);

</#if>

<#if ICAP_ERROR_INTERRUPT_ENABLE?c == "true">
// *****************************************************************************
/* Function:
  void ${ICAP_INSTANCE_NAME}_ErrorCallbackRegister( ICAP_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a icap error interrupt.

  Description:
    This function sets the callback function that will be called when the ICAP
    conditions are met.

  Precondition:
    None.

  Parameters:
    *callback   - a pointer to the function to be called when value is reached.
                  Use NULL to Unregister the compare callback

    context     - a pointer to user defined data to be used when the callback
                  function is called. NULL can be passed in if no data needed.

  Returns:
    void
*/
void ${ICAP_INSTANCE_NAME}_ErrorCallbackRegister(ICAP_CALLBACK callback, uintptr_t context);

<#else>
// *****************************************************************************
/* Function:
   void ${ICAP_INSTANCE_NAME}_ErrorStatusGet (void)

  Summary:
    ${ICAP_INSTANCE_NAME} status

  Description:
    Returns the current state of overflow

  Parameters:
    None

  Returns:
    bool
*/
bool ${ICAP_INSTANCE_NAME}_ErrorStatusGet (void);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // _PLIB_${ICAP_INSTANCE_NAME}_H
