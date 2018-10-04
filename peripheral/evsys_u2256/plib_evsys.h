/*******************************************************************************
  Event System(EVSYS) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_evsys.h

  Summary:
    EVSYS Peripheral Library Interface Header File.

  Description:
    This file defines the interface to the EVSYS peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    This header is for documentation only.  The actual plib_evsys<x> headers
    will be generated as required by the MHC (where <x> is the peripheral
    instance number).

    Every interface symbol has a lower-case 'x' in it following the "EVSYS"
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
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

#ifndef PLIB_EVSYSx_H
#define PLIB_EVSYSx_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include <stdint.h>
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
// *****************************************************************************

// *****************************************************************************
/* EVSYS Interrupt Mask

  Summary:
    Identifies the triggered Event system interrupt.

  Description:
    This enumeration identifies the possible interrupt source that the EVSYS module 
    can generate. The EVSYS callback will receive a value of this type.

  Remarks:
    None.
*/

typedef enum 
{
	EVSYS_INT_OVERRUN0 = EVSYS_INTENSET_OVR0,          
	EVSYS_INT_OVERRUN1 = EVSYS_INTENSET_OVR1,          
	EVSYS_INT_OVERRUN2 = EVSYS_INTENSET_OVR2,  
	EVSYS_INT_OVERRUN3 = EVSYS_INTENSET_OVR3,          
	EVSYS_INT_OVERRUN4 = EVSYS_INTENSET_OVR4,          
	EVSYS_INT_OVERRUN5 = EVSYS_INTENSET_OVR5, 
	EVSYS_INT_OVERRUN6 = EVSYS_INTENSET_OVR6,          
	EVSYS_INT_OVERRUN7 = EVSYS_INTENSET_OVR7,          
	EVSYS_INT_OVERRUN8 = EVSYS_INTENSET_OVR8, 
	EVSYS_INT_OVERRUN9 = EVSYS_INTENSET_OVR9,          
	EVSYS_INT_OVERRUN10 = EVSYS_INTENSET_OVR10,          
	EVSYS_INT_OVERRUN11 = EVSYS_INTENSET_OVR11, 	
	EVSYS_INT_EVENT0 = EVSYS_INTENSET_EVD0,          
	EVSYS_INT_EVENT1 = EVSYS_INTENSET_EVD1,          
	EVSYS_INT_EVENT2 = EVSYS_INTENSET_EVD2,  
	EVSYS_INT_EVENT3 = EVSYS_INTENSET_EVD3,          
	EVSYS_INT_EVENT4 = EVSYS_INTENSET_EVD4,          
	EVSYS_INT_EVENT5 = EVSYS_INTENSET_EVD5, 
	EVSYS_INT_EVENT6 = EVSYS_INTENSET_EVD6,          
	EVSYS_INT_EVENT7 = EVSYS_INTENSET_EVD7,          
	EVSYS_INT_EVENT8 = EVSYS_INTENSET_EVD8, 
	EVSYS_INT_EVENT9 = EVSYS_INTENSET_EVD9,          
	EVSYS_INT_EVENT10 = EVSYS_INTENSET_EVD10,          
	EVSYS_INT_EVENT11 = EVSYS_INTENSET_EVD11 	
} EVSYS_INT_MASK;

// *****************************************************************************
/* Evsys callback function Pointer

  Summary:
    Pointer to a EVSYS CallBack function.

  Description:
    This data type defines the required function signature for the EVSYS event
    handling callback function. Application must register a pointer to an event
    handling function whose function signature (parameter and return value
    types) match the types specified by this function pointer in order to
    receive event calls back from the EVSYS PLIB.

    The parameters and return values are described here and a partial example
    implementation is provided.

  Parameters:
    context - Value identifying the context of the application that registered
    the event handling function
    int_cause - the reason for the interrupt

  Returns:
    None.

  Example:
    <code>

    // This is the callback function that is called when an Event
    // interrupt is triggered.

    void evsysCallBack(uintptr_t contextHandle, uint32_t int_cause)
    {
        if( int_cause & EVSYS_INTENSET_EVD1)
        {
            // Event detected on channel 1
        }
        if( int_cause & EVSYS_INTENSET_EVD2)
        {
            // Event detected on channel 2
        }
        
    }
    
    EVSYSx_Initialize();
    EVSYSx_CallbackRegister(&evsysCallBack, NULL);

    </code>

  Remarks:
    The context parameter can contain a handle to the client context, provided
    at the time the event handling function was  registered using the
    EVSYS_CallbackRegister function. This context handle value is passed back to
    the client as the "context" parameter.  It can be any value (such as a
    pointer to the client's data) necessary to identify the client context or
    instance  of the client that made the data exchange request.

    The callback function executes in the driver peripheral interrupt context
    when the driver is configured for interrupt mode operation.  It is
    recommended of the application to not perform process intensive or blocking
    operations with in this function.
*/

typedef void (*EVSYS_CALLBACK)(uintptr_t context, uint32_t int_cause);

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
    void EVSYSx_Initialize (void);

  Summary:
    Initializes EVSYSx module.

  Description:
    This function initializes EVSYS module with the values configured in MHC
    GUI.  

  Precondition:
    MHC GUI should be configured with the right values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        EVSYSx_Initialize();
    </code>

  Remarks:
    None.
*/

void EVSYSx_Initialize (void);

// *****************************************************************************
/* Function:
    void EVSYSx_InterruptEnable(EVSYS_INT_MASK interrupt);

  Summary:
    Enables evsys interrupt.

  Description:
    This function enables the specified evsys interrupt.

  Precondition:
    EVSYSx module should be initialized with the required configuration
    parameters from the MHC GUI in the EVSYSx_Initialize() function

  Parameters:
    interrupt -  Interrupt to be enabled

  Returns:
    None

  Example:
    <code>
        // Enable Event System channel 2 Event Detection interrupt 
        EVSYSx_InterruptEnable(EVSYS_INTENSET_EVD2);
    </code>

  Remarks:
    Interrupts configuration will be generated in EVSYSx_Initialize() 
    function as per user settings in MHC.
    The EVSYSx_InterruptEnable and EVSYSx_InterruptDisable API should be used
    to enable and disable interrupt at run time.
*/

void EVSYSx_InterruptEnable(EVSYS_INT_MASK interrupt);

// *****************************************************************************
/* Function:
    void EVSYSx_InterruptDisable(EVSYS_INT_MASK interrupt);

  Summary:
    Disables evsys interrupt.

  Description:
    This function disables the specified evsys interrupt.

  Precondition:
    EVSYSx module should be initialized with the required configuration
    parameters from the MHC GUI in the EVSYSx_Initialize() function

  Parameters:
    interrupt -  Interrupt to be Disabled

  Returns:
    None

  Example:
    <code>
        // Disable Event System channel 2 Event Detection interrupt 
        EVSYSx_InterruptDisable(EVSYS_INTENSET_EVD2);
    </code>

  Remarks:
        Interrupts configuration will be generated in EVSYSx_Initialize() 
    function as per user settings in MHC.
    The EVSYSx_InterruptEnable and EVSYSx_InterruptDisable API should be used
    to enable and disable interrupt at run time.
*/

void EVSYSx_InterruptDisable(EVSYS_INT_MASK interrupt);

// *****************************************************************************
/* Function:
    void EVSYSx_CallbackRegister( EVSYS_CALLBACK callback, uintptr_t context );

  Summary:
    Allows application to register a callback function.

  Description:
    This function allows the application to register a callback function that
    will be called when a event system interrupt has triggered. The
    callback feature is only available if the Interrupt operation in the GUI was
    enabled.  If a callback mechanism is desired, then a callback function
    should be registerd via this function before enabling other peripherals
    Calling this function at any time with callback function as NULL will 
    disable the callback feature.

  Precondition:
    The EVSYSx_Initialize function must have been called. Interrupt option in
    MHC should have been enabled.

  Parameters:
    callBack - Pointer to an application callback function.

    context - The value of parameter will be passed back to the application
    unchanged, when the callback function is called.  It can be used to identify
    any application specific data object that identifies the instance of the
    client module (for example, it may be a pointer to the client modules state
    structure).

  Returns:
    None.

  Example:
    <code>

    // This is the callback function that is called when an Event
    // interrupt is triggered.

    void evsysCallBack(uintptr_t contextHandle, uint32_t int_cause)
    {
        if( int_cause & EVSYS_INTENSET_EVD1)
        {
            // Event detected on channel 1
        }
        if( int_cause & EVSYS_INTENSET_EVD2)
        {
            // Event detected on channel 2
        }
        
    }
    
    EVSYSx_Initialize();
    EVSYSx_CallbackRegister(&evsysCallBack, NULL);

    </code>

  Remarks:
    The callback mechanism allows the application to implement an event based
    interaction with the library.
*/

void EVSYSx_CallbackRegister( EVSYS_CALLBACK callback, uintptr_t context );


 #ifdef __cplusplus // Provide C++ Compatibility
 }
 #endif

#endif /* PLIB_EVSYSx_H */
