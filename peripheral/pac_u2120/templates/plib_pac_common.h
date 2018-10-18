/*******************************************************************************
  Peripheral Access Controller(PAC) Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_pac_common.h

  Summary
    PAC Peripheral Library Interface Header File.

  Description
    This file defines the common types for the PAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_PAC_COMMON_H    // Guards against multiple inclusion
#define PLIB_PAC_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************
/* Peripheral Access Control Keys enumeration

  Summary:
    List of available Peripheral Access Control Operations.

  Description:
    This enum identifies the possible PAC operation. This data type is used
    along with the PACx_PeripheralProtect() function and specifies
    the type of access operation that needs to be peformed

  Remarks:
    None.
*/

typedef enum
{
    /* No Action */
    PAC_PROTECTION_OFF,

    /* Clear the peripheral write control protection */
    PAC_PROTECTION_CLEAR,

    /* Set the peripheral write control protection */
    PAC_PROTECTION_SET,

    /* Set and lock the peripheral write control until the next hardware reset */
    PAC_PROTECTION_SET_AND_LOCK,

} PAC_PROTECTION;

// *****************************************************************************
/* Callback function Pointer

  Summary:
    Defines the data type and function signature for the PAC peripheral
    callback function.

  Description:
    This data type defines the function signature for the PAC peripheral
    callback function. The PAC peripheral will call back the function with
    this signature when a access violation has been detected.

  Function:
    void (*PAC_CALLBACK)( uintptr_t context )

  Precondition:
    None.

  Parameters:
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>
      void APP_PACErrorCallback( uintptr_t context )
      {
            // Identify the error.
            if(PACx_PeripheralErrorOccurred())
            {
                // Call the PACx_PeripheralErrorGet() function to
                // identify the error.
            }
            else if(PACx_AHBSlaveErrorOccurred())
            {
                // Call the PACx_AHBSlaveErrorGet() function to
                // identify the error.
            }
      }

      PACx_CallbackRegister(APP_PACErrorCallback, NULL);

    </code>

  Remarks:
    The callback feature is only available when the library was generated with
    interrupt option (in MHC) enabled. The function will execute within an
    interrupt context. Avoid calling computationally intensive or blocking
    functions from within the callback function.
*/

typedef void (*PAC_CALLBACK)( uintptr_t context );

// *****************************************************************************
/* PAC Callback Object

  Summary:
    PAC Peripheral Callback object.

  Description:
    This local data object holds the function signature for the PAC peripheral
    callback function.

  Remarks:
    None.
*/

typedef struct
{
    PAC_CALLBACK callback;

    uintptr_t context;

} PAC_CALLBACK_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_PAC_COMMON_H */
