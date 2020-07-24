/*******************************************************************************
 Configurable Logic Cell (${CLC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CLC_INSTANCE_NAME?lower_case}.h

  Summary:
    ${CLC_INSTANCE_NAME} PLIB Header file

  Description:
    This file defines the interface to the CDAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${CLC_INSTANCE_NAME}_H     // Guards against multiple inclusion
#define PLIB_${CLC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
  #include <stdbool.h>
  #include "plib_clc_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void ${CLC_INSTANCE_NAME}_Initialize(void);

  Summary:
    Initialize ${CLC_INSTANCE_NAME} registers per user config.

  Description:
    Initalize ${CLC_INSTANCE_NAME} peripheral.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.
*/
void ${CLC_INSTANCE_NAME}_Initialize( void );

// *****************************************************************************
/* Function:
   void ${CLC_INSTANCE_NAME}_Enable(bool enable);

  Summary:
    Enable or Disable ${CLC_INSTANCE_NAME} instance.

  Description:
    This API will enable or disable ${CLC_INSTANCE_NAME} instance by enabling or
    disabling its logic cell.

  Precondition:
    None.

  Parameters:
    enable - True value will enable the logic cell and False value will disable it

  Returns:
    None.
*/
void ${CLC_INSTANCE_NAME}_Enable(bool enable);
<#if CLC_INTERRUPT_TYPE != "Disabled">


// *****************************************************************************
/* Function:
    void ${CLC_INSTANCE_NAME}_CallbackRegister(CLC_CALLBACK callback, uintptr_t context);

  Summary:
    Register callback for ${CLC_INSTANCE_NAME} interrupt.

  Description:
      When the  ${CLC_INSTANCE_NAME} interrupt occurs the given callback will be called with the
      given context.

  Precondition:
    None.

  Parameters:
    callback    - Callback function
    context     - paramter to callback function

  Returns:
    None.
*/
void ${CLC_INSTANCE_NAME}_RegisterCallback(CLC_CALLBACK callback, uintptr_t context);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // PLIB_${CLC_INSTANCE_NAME}_H