/*******************************************************************************
  Capture/Compare/PWM/Timer Modules (CCP) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CCP_INSTANCE_NAME?lower_case}.h

  Summary:
    CCP PLIB Header File

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

#ifndef PLIB_${CCP_INSTANCE_NAME}_H
#define PLIB_${CCP_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"
#include "plib_ccp_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END


// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

// *************************** ${CCP_INSTANCE_NAME} API ***************************************/
// *****************************************************************************
/* Function:
   void ${CCP_INSTANCE_NAME}_CaptureInitialize (void)

  Summary:
    Initialization function ${CCP_INSTANCE_NAME} peripheral

  Description:
    This function initializes the ${CCP_INSTANCE_NAME} peripheral with user input
    from the configurator.

  Parameters:
    none

  Returns:
    void
*/
void ${CCP_INSTANCE_NAME}_CaptureInitialize (void);

// *****************************************************************************
/* Function:
   void ${CCP_INSTANCE_NAME}_CaptureStart (void)

  Summary:
    Enable function for the ${CCP_INSTANCE_NAME} peripheral

  Description:
    This function enables the ${CCP_INSTANCE_NAME} peripheral.

  Parameters:
    none

  Returns:
    void
*/
void ${CCP_INSTANCE_NAME}_CaptureStart (void);

// *****************************************************************************
/* Function:
   void ${CCP_INSTANCE_NAME}_CaptureStop (void)

  Summary:
    Disable function for the ${CCP_INSTANCE_NAME} peripheral

  Description:
    This function disables the ${CCP_INSTANCE_NAME} peripheral.

  Parameters:
    none

  Returns:
    void
*/
void ${CCP_INSTANCE_NAME}_CaptureStop (void);

<#if CCP_CCPCON1_T32 == true>
// *****************************************************************************
/* Function:
   uint32_t ${CCP_INSTANCE_NAME}_Capture32bitBufferRead (void)

  Summary:
    Read buffer function ${CCP_INSTANCE_NAME} peripheral

  Description:
    This function will return the value contained in the ${CCP_INSTANCE_NAME} peripheral
    buffer.

  Parameters:
    none

  Returns:
    uint32_t
*/
uint32_t ${CCP_INSTANCE_NAME}_Capture32bitBufferRead (void);

<#else>
// *****************************************************************************
/* Function:
   uint16_t ${CCP_INSTANCE_NAME}_Capture16bitBufferRead (void)

  Summary:
    Read buffer function ${CCP_INSTANCE_NAME} peripheral

  Description:
    This function will return the value contained in the ${CCP_INSTANCE_NAME} peripheral
    buffer.

  Parameters:
    none

  Returns:
    uint16_t
*/
uint16_t ${CCP_INSTANCE_NAME}_Capture16bitBufferRead (void);
</#if>

<#if CCP_CAP_INTERRUPT == true>
// *****************************************************************************
/* Function:
  void ${CCP_INSTANCE_NAME}_CaptureCallbackRegister( CCP_CAPTURE_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a icap interrupt.

  Description:
    This function sets the callback function that will be called when the CCP
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
void ${CCP_INSTANCE_NAME}_CaptureCallbackRegister(CCP_CAPTURE_CALLBACK callback, uintptr_t context);

<#else>
// *****************************************************************************
/* Function:
   void ${CCP_INSTANCE_NAME}_CaptureStatusGet (void)

  Summary:
    ${CCP_INSTANCE_NAME} status

  Description:
    Returns the current state overflow or buffer not empty flags

  Parameters:
    None

  Returns:
    bool
*/
bool ${CCP_INSTANCE_NAME}_CaptureStatusGet (void);

</#if>

<#if CCP_TIMER_INTERRUPT == true>
// *****************************************************************************
/* Function:
  void ${CCP_INSTANCE_NAME}_TimerCallbackRegister( CCP_TIMER_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a icap interrupt.

  Description:
    This function sets the callback function that will be called when the CCP
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
void ${CCP_INSTANCE_NAME}_TimerCallbackRegister(CCP_TIMER_CALLBACK callback, uintptr_t context);
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // _PLIB_${CCP_INSTANCE_NAME}_H
