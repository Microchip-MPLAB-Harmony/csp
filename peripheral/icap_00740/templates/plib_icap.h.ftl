/*******************************************************************************
  Input Capture (ICAP) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_icap${INDEX}.h

  Summary:
    ICAP PLIB Header File

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

#ifndef _PLIB_ICAP${INDEX}_H
#define _PLIB_ICAP${INDEX}_H

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

// *************************** ICAP${INDEX} API ***************************************/
// *****************************************************************************
/* Function:
   void ICAP${INDEX}_Initialize (void)

  Summary:
    Initialization function ICAP${INDEX} peripheral

  Description:
    This function initializes the ICAP${INDEX} peripheral with user input 
	from the configurator.

  Parameters:
    none

  Returns:
    void
*/
void ICAP${INDEX}_Initialize (void);

// *****************************************************************************
/* Function:
   void ICAP${INDEX}_CaptureEnable (void)

  Summary:
    Enable function for the ICAP${INDEX} peripheral

  Description:
    This function enables the ICAP${INDEX} peripheral.

  Parameters:
    none

  Returns:
    void
*/
void ICAP${INDEX}_CaptureEnable (void);

// *****************************************************************************
/* Function:
   void ICAP${INDEX}_CaptureDisable (void)

  Summary:
    Disable function for the ICAP${INDEX} peripheral

  Description:
    This function disables the ICAP${INDEX} peripheral.

  Parameters:
    none

  Returns:
    void
*/
void ICAP${INDEX}_CaptureDisable (void);

// *****************************************************************************
/* Function:
   uint32_t ICAP${INDEX}_BufferRead (void)

  Summary:
    Read buffer function ICAP${INDEX} peripheral

  Description:
    This function will return the value contained in the ICAP${INDEX} peripheral 
	buffer.

  Parameters:
    none

  Returns:
    uint32_t
*/
uint32_t ICAP${INDEX}_CaptureBufferRead (void);

// *****************************************************************************
/* Function:
   void ICAP${INDEX}_StatusGet (void)

  Summary:
    ICAP${INDEX} status

  Description:
    Returns the current state overflow or buffer not empty flags

  Parameters:
    source	overFlow, buffNotEmpty

  Returns:
    bool
*/
bool ICAP${INDEX}_StatusGet (ICAP_STATUS_SOURCE source);
<#if ICAP_INTERRUPT_ENABLE?c == "true">

// *****************************************************************************
/* Function:
  void INPUT_CAPTURE_${INDEX}_Tasks( void )
  Summary:
    Interrupt handler.
  Description:
    This function does the PLIB-specific actions, and is called by the actual handler
    function.
  Precondition:
    None.
  Parameters:
    None.
  Returns:
    void
*/
void INPUT_CAPTURE_${INDEX}_Tasks (void);
// *****************************************************************************
/* Function:
  void ICAP${INDEX}_CallbackRegister( ICAP_CALLBACK callback, uintptr_t context )

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
void ICAP${INDEX}_CallbackRegister(ICAP_CALLBACK callback, uintptr_t context);
</#if>
<#if ICAP_ERROR_INTERRUPT_ENABLE?c == "true">

// *****************************************************************************
/* Function:
  void ICAP${INDEX}_Error_CallbackRegister( ICAP_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a icap error interrupt.

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
void ICAP${INDEX}_Error_CallbackRegister(ICAP_CALLBACK callback, uintptr_t context);
// *****************************************************************************
/* Function:
  void INPUT_CAPTURE_${INDEX}_ERROR_Tasks (void)
  Summary:
    Error interrupt handler.
  Description:
    This function does the PLIB-specific actions, and is called by the actual handler
    function.
  Precondition:
    None.
  Parameters:
    None.
  Returns:
    void
*/
void INPUT_CAPTURE_${INDEX}_ERROR_Tasks (void);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // _PLIB_ICAP${INDEX}_H
