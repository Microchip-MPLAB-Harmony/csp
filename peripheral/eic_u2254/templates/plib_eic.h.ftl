/*******************************************************************************
  External Interrupt Controller (EIC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_eic${EIC_INDEX}.h

  Summary
    EIC PLIB Header File.

  Description
    This file defines the interface to the EIC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

/* Guards against multiple inclusion */
#ifndef PLIB_EIC${EIC_INDEX}_H
#define PLIB_EIC${EIC_INDEX}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part of it.
*/

// *****************************************************************************
/* EIC Pins

  Summary:
    Identifies the available EIC pins.

  Description:
    This enumeration identifies all the available EIC pins. Not all pins will be
    implemented in a device. The pins described here are for documentation
    purposes only. The MHC will generate this enumeration with the enabled EIC
    pins only. The application should not use the constant value that are
    assigned to enumeration constants as this may vary between devices.

  Remarks:
    None.
*/

typedef enum
{
<#list 0..EIC_INT_COUNT as i>
    <#assign EIC_INT_CHANNEL = "EIC_CHAN_" + i>
        <#if .vars[EIC_INT_CHANNEL]?has_content>
            <#if (.vars[EIC_INT_CHANNEL] != false)>
    <#lt>    /* External Interrupt Controller Pin ${i} */
    <#lt>    EIC_PIN_${i} = ${i},

            </#if>
        </#if>
</#list>
    EIC_PIN_MAX = 16

} EIC_PIN;

// *****************************************************************************
/* EIC Interrupt Pin Callback Function Pointer Type

  Summary:
    Defines the data type and function signature of the EIC peripheral callback
    function.

  Description:
    This data type defines the function signature for the EIC peripheral
    callback function. The EIC peripheral will call back the client's function
    with this signature when an interrupt condition has been sensed on the pin.
    The EIC library allows the application to register a callback function for
    each enabled external interrupt.

  Function:
    void (*EIC_CALLBACK)(uintptr_t context )

  Precondition:
    EIC${EIC_INDEX}_Initialize must have been called for the given EIC
    peripheral instance and EIC${EIC_INDEX}_CallbackRegister must have been
    called to set the function to be called.

  Parameters:
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>

    void EIC_Pin0Callback (uintptr_t context)
    {
        // This means an interrupt condition has been sensed on EIC Pin 0.
    }

    EIC${EIC_INDEX}_CallbackRegister(EIC_PIN_0, EIC_Pin0Callback, 0);
    </code>

  Remarks:
    None.
*/

typedef void (*EIC_CALLBACK) (uintptr_t context);

// *****************************************************************************
/* EIC NMI Interrupt Pin Callback Function Pointer Type

  Summary:
    Defines the data type and function signature of the EIC peripheral NMI
    callback function.

  Description:
    This data type defines the function signature of the EIC peripheral NMI
    callback function. The EIC peripheral will call back the client's function
    with this signature when an interrupt condition has been sensed on the NMI
    pin.

  Function:
    void (*EIC_NMI_CALLBACK)(uintptr_t context )

  Precondition:
    EIC${EIC_INDEX}_Initialize must have been called for the given EIC
    peripheral instance and EIC${EIC_INDEX}_NMICallbackRegister must have been
    called to set the function to be called.

  Parameters:
    context - Allows the caller to provide a context value (usually a pointer
    to the callers context for multi-instance clients).

  Returns:
    None.

  Example:
    <code>

    void EIC_NMICallback (uintptr_t context)
    {
        // This means an interrupt condition has been sensed on the NMI Pin.
    }

    EIC${EIC_INDEX}_NMICallbackRegister(EIC_NMICallback, 0);
    </code>

  Remarks:
    None.
*/

typedef void (*EIC_NMI_CALLBACK) (uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
    this interface.
*/

// *****************************************************************************
/* Function:
    void EIC${EIC_INDEX}_Initialize (void);

  Summary:
    Initializes given instance of EIC peripheral.

  Description:
    This function initializes given instance of EIC peripheral of the device
    with the values configured in MHC GUI.

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    EIC${EIC_INDEX}_Initialize();
    </code>

  Remarks:
    This function should only be called once during system initialization
    before any other EIC function is called.
*/

void EIC${EIC_INDEX}_Initialize (void);

// *****************************************************************************
/* Function:
    void EIC${EIC_INDEX}_InterruptEnable (EIC_PIN pin, bool enable)

  Summary:
    Enables and disables interrupts on a pin.

  Description
    This function enables or disables interrupts on an external interrupt pin.
    When enabled, the interrupt pin sense will be configured as per the
    configuration set in MHC.

   Precondition:
    EIC${EIC_INDEX}_Initialize() function must have been called for the
    associated instance.

   Parameters:
    pin - EIC Pin number

    enable - If true, interrupt sensing on the pin will be enabled. If false,
    interrupt sensing on the pin will be disabled.

   Returns:
    None

   Example:
    <code>
    EIC${EIC_INDEX}_Initialize();
    EIC${EIC_INDEX}_InterruptEnable(EIC_PIN_3, true);
    </code>

  Remarks:
    None.
*/

void EIC${EIC_INDEX}_InterruptEnable (EIC_PIN pin, bool enable);

// *****************************************************************************
/* Function:
    void EIC${EIC_INDEX}_CallbackRegister (EIC_PIN pin, EIC_CALLBACK callback
                                            uintptr_t context);

  Summary:
    Registers the function to be called when an interrupt condition has been
    sensed on the pin.

  Description
    This function registers the callback function to be called when an interrupt
    condition has been sensed on the pin. A unique callback function can be
    registered for each pin.

    When an interrupt condition has been sensed on the pin, the library will
    call the registered callback function and will then clear the interrupt
    condition when the callback function exits.

  Precondition:
    EIC${EIC_INDEX}_Initialize() must have been called first for the associated
    instance.

  Parameters:
    pin - EIC Pin number

    callback - callback function pointer. Setting this to NULL will disable the
    callback feature.

    context - An application defined context value that will be passed to the
    callback function.

  Returns:
    None.

  Example:
    <code>
    // Refer to the description of the EIC_CALLBACK data type for details on API
    // usage.
    </code>

  Remarks:
    Context value can be set to NULL, if not required.
*/

void EIC${EIC_INDEX}_CallbackRegister(EIC_PIN pin, EIC_CALLBACK callback, uintptr_t context);

// *****************************************************************************
/* Function:
    void EIC${EIC_INDEX}_NMICallbackRegister (EIC_NMI_CALLBACK callback, uintptr_t context);

  Summary:
    Registers the function to be called when an interrupt condition has been
    sensed on the NMI pin.

  Description
    This function registers the callback function to be called when an interrupt
    condition has been sensed on the NMI pin.

  Precondition:
    EIC${EIC_INDEX}_Initialize() must have been called first for the associated
    instance.

  Parameters:
    callback - callback function pointer. Setting this to NULL will disable the
    callback feature.

    context - Allows the caller to provide a context value

  Returns:
    None.

  Example:
    <code>
    // Refer to the description of the EIC_NMI_CALLBACK data type for details on
    // API usage.
    </code>

  Remarks:
    None.
*/

void EIC${EIC_INDEX}_NMICallbackRegister(EIC_NMI_CALLBACK callback, uintptr_t context);

// *****************************************************************************
/* Function:
    bool EIC${EIC_INDEX}_PinDebounceStateGet ( EIC_PIN pin )

  Summary:
    Gets the De-bounce state of the EIC Pin.

  Description
    This function gets the De-bounced state of the EIC Pin.

  Precondition:
    EIC${EIC_INDEX}_Initialize() must have been called first for the associated
    instance. The debounce feature should have been enabled in MHC on the
    desired pin.

  Parameters:
    pin - EIC Pin number

  Returns:
    true - If the EIC Pin De-bounce state is set.
    false - If the EIC Pin De-bounce state is not set

  Example:
    <code>
    if (true == EIC${EIC_INDEX}_PinDebounceStateGet(EIC_PIN_3))
    {
        // EIC pin 3 was debounced..
    }
    </code>

  Remarks:
    None.
*/

bool EIC${EIC_INDEX}_PinDebounceStateGet (EIC_PIN pin);

// *****************************************************************************
/* Function:
    void EIC${EIC_INDEX}_InterruptHandler ( void )

  Summary:
    External Interrupt Controller (EIC) Interrupt Handler.

  Description
    This EIC Interrupt handler function handles interrupts on EIC_PIN_0 to
    EIC_PIN_15.

  Precondition:
    EIC${EIC_INDEX}_Initialize() must have been called first for the associated
    instance.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        EIC${EIC_INDEX}_InterruptHandler());
    </code>

  Remarks:
    User should not call this function, this function will be called
    automatically when interrupt condition occurs.
*/

void EIC${EIC_INDEX}_InterruptHandler(void);

// *****************************************************************************
/* Function:
    void NMI${EIC_INDEX}_InterruptHandler ( void )

  Summary:
    External Interrupt Controller (EIC) NMI Interrupt Handler.

  Description
    This EIC Interrupt handler function handles interrupts on NMI Pin

  Precondition:
    EIC${EIC_INDEX}_Initialize() must have been called first for the associated
    instance.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        NMI${EIC_INDEX}_InterruptHandler();
    </code>

  Remarks:
    User should not call this function, this function will be called
    automatically when interrupt condition occurs.
*/

void NMI${EIC_INDEX}_InterruptHandler(void);

#endif /* PLIB_EIC${EIC_INDEX}_H */
