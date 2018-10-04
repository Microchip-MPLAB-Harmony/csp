/*******************************************************************************
  PIO PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pio.h

  Summary:
    PIO PLIB Header File

  Description:
    This library provides an interface to control and interact with Parallel
    Input/Output controller (PIO) module.

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

#ifndef PLIB_PIO_H
#define PLIB_PIO_H

#include "device.h"
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data types and constants
// *****************************************************************************
// *****************************************************************************

<#compress> <#-- To remove unwanted new lines -->

<#-- Create List of all the port pins for enum creation -->

<#assign PORTA_Pin_List = []>
<#assign PORTB_Pin_List = []>
<#assign PORTC_Pin_List = []>
<#assign PORTD_Pin_List = []>
<#assign PORTE_Pin_List = []>

<#list 1..PIO_PIN_TOTAL as i>
    <#assign pinport = "PIN_" + i + "_PIO_PIN">
    <#assign pinchannel = "PIN_" + i + "_PIO_CHANNEL">

    <#if .vars[pinport]?has_content>
        <#if .vars[pinchannel]?has_content>
            <#if .vars[pinchannel] == "A">
                <#assign PORTA_Pin_List = PORTA_Pin_List + [.vars[pinport]]>

            <#elseif .vars[pinchannel] == "B">
                <#assign PORTB_Pin_List = PORTB_Pin_List + [.vars[pinport]]>

            <#elseif .vars[pinchannel] == "C">
                <#assign PORTC_Pin_List = PORTC_Pin_List + [.vars[pinport]]>

            <#elseif .vars[pinchannel] == "D">
                <#assign PORTD_Pin_List = PORTD_Pin_List + [.vars[pinport]]>

            <#elseif .vars[pinchannel] == "E">
                <#assign PORTE_Pin_List = PORTE_Pin_List + [.vars[pinport]]>
            </#if>
        </#if>
    </#if>
</#list>

</#compress>
<#-- Generate Pin Macros for all the GPIO Pins -->
    <#assign GPIO_Name_List = []>
    <#assign GPIO_PortPin_List = []>
    <#assign GPIO_PortChannel_List = []>
    <#assign GPIO_Interrupt_List = []>
    <#list 1..PIO_PIN_TOTAL as i>
        <#assign functype = "PIN_" + i + "_FUNCTION_TYPE">
        <#assign funcname = "PIN_" + i + "_FUNCTION_NAME">
        <#assign pinport = "PIN_" + i + "_PIO_PIN">
        <#assign pinchannel = "PIN_" + i + "_PIO_CHANNEL">
        <#assign interruptType = "PIN_" + i + "_PIO_INTERRUPT">
        <#if .vars[functype]?has_content>
            <#if .vars[functype] == "GPIO">
                <#if .vars[funcname]?has_content>
                    <#if .vars[pinport]?has_content>
                        <#if .vars[pinchannel]?has_content>

                            <#lt>/*** Macros for ${.vars[funcname]} pin ***/
                            <#lt>#define ${.vars[funcname]}_Set()               (PIO${.vars[pinchannel]}_REGS->PIO_SODR = (1<<${.vars[pinport]}))
                            <#lt>#define ${.vars[funcname]}_Clear()             (PIO${.vars[pinchannel]}_REGS->PIO_CODR = (1<<${.vars[pinport]}))
                            <#lt>#define ${.vars[funcname]}_Toggle()            (PIO${.vars[pinchannel]}_REGS->PIO_ODSR ^= (1<<${.vars[pinport]}))
                            <#lt>#define ${.vars[funcname]}_Get()               ((PIO${.vars[pinchannel]}_REGS->PIO_PDSR >> ${.vars[pinport]}) & 0x1)
                            <#lt>#define ${.vars[funcname]}_OutputEnable()      (PIO${.vars[pinchannel]}_REGS->PIO_OER = (1<<${.vars[pinport]}))
                            <#lt>#define ${.vars[funcname]}_InputEnable()       (PIO${.vars[pinchannel]}_REGS->PIO_ODR = (1<<${.vars[pinport]}))
                            <#if .vars[interruptType]?has_content>
                                <#lt>#define ${.vars[funcname]}_InterruptEnable()   (PIO${.vars[pinchannel]}_REGS->PIO_IER = (1<<${.vars[pinport]}))
                                <#lt>#define ${.vars[funcname]}_InterruptDisable()  (PIO${.vars[pinchannel]}_REGS->PIO_IDR = (1<<${.vars[pinport]}))
                            </#if>
                            <#lt>#define ${.vars[funcname]}_PIN                  PIO_PIN_P${.vars[pinchannel]}${.vars[pinport]}
                        </#if>
                    </#if>
                </#if>
            </#if>
        </#if>
    </#list>


// *****************************************************************************
/* PIO Port

  Summary:
    Identifies the available PIO Ports.

  Description:
    This enumeration identifies the available PIO Ports.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all ports are available on all devices.  Refer to the specific
    device data sheet to determine which ports are supported.
*/

typedef enum
{
    <#if PORTA_Pin_List?has_content>
    PIO_PORT_A = PIOA_BASE_ADDRESS,
    </#if>
    <#if PORTB_Pin_List?has_content>
    PIO_PORT_B = PIOB_BASE_ADDRESS,
    </#if>
    <#if PORTC_Pin_List?has_content>
    PIO_PORT_C = PIOC_BASE_ADDRESS,
    </#if>
    <#if PORTD_Pin_List?has_content>
    PIO_PORT_D = PIOD_BASE_ADDRESS,
    </#if>
    <#if PORTE_Pin_List?has_content>
    PIO_PORT_E = PIOE_BASE_ADDRESS
    </#if>
} PIO_PORT;

// *****************************************************************************
/* PIO Port Pins

  Summary:
    Identifies the available PIO port pins.

  Description:
    This enumeration identifies the available PIO port pins.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all pins are available on all devices.  Refer to the specific
    device data sheet to determine which pins are supported.
*/

typedef enum
{
    <#assign PORTA_Pin_List =  PORTA_Pin_List?sort>
    <#list PORTA_Pin_List as pin>
    PIO_PIN_PA${pin} = ${pin},
    </#list>
    <#assign PORTB_Pin_List =  PORTB_Pin_List?sort>
    <#list PORTB_Pin_List as pin>
    PIO_PIN_PB${pin} = ${pin+32},
    </#list>
    <#assign PORTC_Pin_List =  PORTC_Pin_List?sort>
    <#list PORTC_Pin_List as pin>
    PIO_PIN_PC${pin} = ${pin+64},
    </#list>
    <#assign PORTD_Pin_List =  PORTD_Pin_List?sort>
    <#list PORTD_Pin_List as pin>
    PIO_PIN_PD${pin} = ${pin+96},
    </#list>
    <#assign PORTE_Pin_List =  PORTE_Pin_List?sort>
    <#list PORTE_Pin_List as pin>
    PIO_PIN_PE${pin} = ${pin+128},
    </#list>

    /* This element should not be used in any of the PIO APIs.
       It will be used by other modules or application to denote that none of the PIO Pin is used */
    PIO_PIN_NONE = -1

} PIO_PIN;

<#if PIO_A_INTERRUPT_USED == true ||
     PIO_B_INTERRUPT_USED == true ||
     PIO_C_INTERRUPT_USED == true ||
     PIO_D_INTERRUPT_USED == true ||
     PIO_E_INTERRUPT_USED == true >
// *****************************************************************************
/* PIO Pin-Event Handler Function Pointer

   Summary:
    Pointer to a PIO Pin-Event handler function.

   Description:
    This data type defines the required function signature for the
    PIO pin-event handling callback function.  The client must register
    a pointer to an event handling function whose function signature (parameter
    and return value types) match the types specified by this function pointer
    in order to receive calls back from the PLIB when a configured pin event
    occurs.

    The parameters and return values are described here and a partial example
    implementation is provided.

  Parameters:
    context         - Value identifying the context of the client that
                      registered the event handling function

  Returns:
    None.

  Example:
    A function matching this signature:
    <code>
    void APP_PinEventHandler(PIN_NAME pin, uintptr_t context)
    {
        // Do Something
    }
    </code>
    Is registered as follows:
    <code>
    PIO_PinInterruptCallbackRegister(PIO_PIN_PA5, &APP_PinEventHandler, NULL);
    </code>
    <code>

  Remarks:
    The context parameter contains the a handle to the client context,
    provided at the time the event handling function was  registered using the
    PIO_PinInterruptCallbackRegister function. This context handle value is
    passed back to the client as the "context" parameter.  It can be any value
    (such as a pointer to the client's data) necessary to identify the client
    context.

    The event handler function executes in the PLIB's interrupt
    context. It is recommended of the application to not perform process
    intensive or blocking operations with in this function.
*/
typedef  void (*PIO_PIN_CALLBACK) ( PIO_PIN pin, uintptr_t context);
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Generated API based on pin configurations done in Pin Manager
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void PIO_Initialize(void)

  Summary:
    Initialize the PIO library.

  Description:
    This function initializes the PIO library and all ports and pins configured
    in the MCC Pin Manager.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>

    PIO_Initialize();

    </code>

  Remarks:
    None.
*/
void PIO_Initialize(void);

// *****************************************************************************
// *****************************************************************************
// Section: PIO Functions which operates on one pin at a time
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void PIO_PinWrite(PIO_PIN pin, bool value)

  Summary:
    Writes the selected pin.

  Description:
    This function writes/drives the "value" on the selected I/O line/pin.

  Precondition:
    The desired pin must be configured as an output pin.
    PIO_Initialize() must have been called.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN
    value     - value to be written on the selected pin:
                true  = set pin to high (1).
                false = clear pin to low (0).

  Returns:
    None.

  Example:
    <code>
    PIO_PinWrite(PIO_PIN_PB3, true);
    </code>

  Remarks:
    None.
*/
static inline void PIO_PinWrite(PIO_PIN pin, bool value);

// *****************************************************************************
/* Function:
    bool PIO_PinRead(PIO_PIN pin)

  Summary:
    Read the selected pin value.

  Description:
    This function reads the selected pin value.
    it reads the value regardless of pin configuration, whether uniquely as an
    input, or driven by the PIO Controller, or driven by peripheral.

  Precondition:
    Reading the I/O line levels requires the clock of the PIO Controller to be
    enabled, otherwise this API reads the levels present on the I/O line at the
    time the clock was disabled.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN

  Returns:
    Returns the read value of the selected I/O pin.

  Example:
    <code>

    bool value;
    value = PIO_PinRead(PIO_PIN_PB3);

    </code>

  Remarks:
       To read the latched value on this pin, PIO_PinLatchRead API should be used.
*/
static inline bool  PIO_PinRead(PIO_PIN pin);

// *****************************************************************************
/* Function:
    bool PIO_PinLatchRead ( PIO_PIN pin )

  Summary:
    Read the value driven on the selected pin.

  Description:
    This function reads the data driven on the selected I/O line/pin.
    Whatever data is written/driven on I/O line by using any of the PIO PLIB
    APIs, will be read by this API.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN

  Returns:
    Returns the value driven on the selected I/O pin.

  Example:
    <code>

    bool value;
    value = PIO_PinLatchRead(PIO_PIN_PB3);

    </code>

  Remarks:
    To read actual pin value, PIO_PinRead API should be used.
*/
static inline bool PIO_PinLatchRead( PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinToggle(PIO_PIN pin)

  Summary:
    Toggles the selected pin.

  Description:
    This function toggles/inverts the value on the selected I/O line/pin.

  Precondition:
    PIO_Initialize() must have been called.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN

  Returns:
    None.

  Example:
    <code>

    PIO_PinToggle(PIO_PIN_PB3);

    </code>

  Remarks:
    None.
*/
static inline void PIO_PinToggle(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinSet(PIO_PIN pin)

  Summary:
    Sets the selected pin.

  Description:
    This function drives '1' on the selected I/O line/pin.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN

  Returns:
    None.

  Example:
    <code>

    PIO_PinSet(PIO_PIN_PB3);

    </code>

  Remarks:
    None.
*/
static inline void PIO_PinSet(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinClear(PIO_PIN pin)

  Summary:
    Clears the selected pin.

  Description:
    This function drives '0' on the selected I/O line/pin.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN

  Returns:
    None.

  Example:
    <code>

    PIO_PinClear(PIO_PIN_PB3);

    </code>

  Remarks:
    None.
*/
static inline void PIO_PinClear(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinInputEnable(PIO_PIN pin)

  Summary:
    Enables selected IO pin as input.

  Description:
    This function enables selected IO pin as input.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN

  Returns:
    None.

  Example:
    <code>

    PIO_PinInputEnable(PIO_PIN_PB3);

    </code>

  Remarks:
    None.
*/
static inline void PIO_PinInputEnable(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinOutputEnable(PIO_PIN pin)

  Summary:
    Enables selected IO pin as output.

  Description:
    This function enables selected IO pin as output.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN

  Returns:
    None.

  Example:
    <code>

    PIO_PinOutputEnable(PIO_PIN_PB3);

    </code>

  Remarks:
    None.
*/
static inline void PIO_PinOutputEnable(PIO_PIN pin);

<#if PIO_A_INTERRUPT_USED == true ||
     PIO_B_INTERRUPT_USED == true ||
     PIO_C_INTERRUPT_USED == true ||
     PIO_D_INTERRUPT_USED == true ||
     PIO_E_INTERRUPT_USED == true >
// *****************************************************************************
/* Function:
    void PIO_PinInterruptEnable(PIO_PIN pin)

  Summary:
    Enables IO interrupt on selected IO pin.

  Description:
    This function enables interrupt on selected IO pin.

  Precondition:
    None.

  Parameters:
    pin           - One of the IO pins from the enum PIO_PIN

  Returns:
    None.

  Example:
    <code>

    PIO_PinInterruptEnable(PIO_PIN_PB3);

    </code>

  Remarks:
    None.
*/
static inline void PIO_PinInterruptEnable(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinInterruptDisable(PIO_PIN pin)

  Summary:
    Disables IO interrupt on selected IO pin.

  Description:
    This function disables IO interrupt on selected IO pin.

  Precondition:
    None.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN

  Returns:
    None.

  Example:
    <code>

    PIO_PinInterruptDisable(PIO_PIN_PB3);

    </code>

  Remarks:
    None.
*/
static inline void PIO_PinInterruptDisable(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinInterruptCallbackRegister(
        PIO_PIN pin,
        const PIO_PIN_CALLBACK callBack,
        uintptr_t context
    );

  Summary:
    Allows application to register callback for every pin.

  Description:
    This function allows application to register an event handling function
    for the PLIB to call back when I/O interrupt occurs on the selected pin.

    At any point if application wants to stop the callback, it can call this
    function with "eventHandler" value as NULL.

  Precondition:
    The PIO_Initialize function must have been called.

  Parameters:
    pin          - One of the IO pins from the enum PIO_PIN
    eventHandler - Pointer to the event handler function implemented by the user

    context      - The value of parameter will be passed back to the application
                   unchanged, when the eventHandler function is called. It can
                   be used to identify any application specific value.

  Returns:
    None.

  Example:
    <code>

    PIO_PinInterruptCallbackRegister(PIO_PIN_PB3, &APP_PinHandler, NULL);

    </code>

  Remarks:
    None.
*/
void PIO_PinInterruptCallbackRegister(
    PIO_PIN pin,
    const   PIO_PIN_CALLBACK callBack,
    uintptr_t context
);
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: PIO Functions which operates on multiple pins of a port
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    uint32_t PIO_PortRead(PIO_PORT port)

  Summary:
    Read all the I/O lines of the selected port port.

  Description:
    This function reads the live data values on all the I/O lines of the
    selected port.  Bit values returned in each position indicate corresponding
    pin levels.
    1 = Pin is high.
    0 = Pin is low.
    This function reads the value regardless of pin configuration, whether it is
    set as as an input, driven by the PIO Controller, or driven by a peripheral.

  Precondition:
    Reading the I/O line levels requires the clock of the PIO Controller to be
    enabled, otherwise this API reads the levels present on the I/O line at the
    time the clock was disabled.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT

  Returns:
    Returns the read value of all the I/O lines of the selected port port.

  Example:
    <code>

    uint32_t value;
    value = PIO_PortRead(PIO_PORT_C);

    </code>

  Remarks:
    If the port has less than 32-bits, unimplemented pins will read as
    low (0).
    Implemented pins are Right aligned in the 32-bit return value.
*/
uint32_t PIO_PortRead(PIO_PORT port);

// *****************************************************************************
/* Function:
    void PIO_PortWrite(PIO_PORT port, uint32_t mask, uint32_t value);

  Summary:
    Write the value on the masked I/O lines of the selected port.

  Description:
    This function writes the data values driven on selected output lines of the
    selected port.  Bit values in each position indicate corresponding pin
    levels.
    1 = Pin is driven high.
    0 = Pin is driven low.

  Precondition:
    The desired pins lines of the selected port must be setup as output(s).
    PIO_Initialize() must have been called.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT
    mask       - A 32 bit value in which positions of 0s and 1s decide
                 which IO pins of the selected port will be written.
                 1's - Will write to corresponding IO pins.
                 0's - Will remain unchanged.
    value      - Value which has to be written/driven on the I/O
                 lines of the selected port for which mask bits are '1'.
                 Values for the corresponding mask bit '0' will be ignored.
  Returns:
    None.

  Example:
    <code>
    // Write binary value 0011 to the pins PC3, PC2, PC1 and PC0 respectively.
    PIO_PortWrite(PIO_PORT_C, 0x0F, 0xF563D453);

    </code>

  Remarks:
    If the port has less than 32-bits, unimplemented pins will be ignored.

    Implemented pins are Right aligned in the 32-bit value.
*/
void PIO_PortWrite(PIO_PORT port, uint32_t mask, uint32_t value);

// *****************************************************************************
/* Function:
    uint32_t PIO_PortLatchRead ( PIO_PORT port )

  Summary:
    Read the latched value on all the I/O lines of the selected port.

  Description:
    This function reads the latched data values on all the I/O lines of the
    selected port.  Bit values returned in each position indicate corresponding
    pin levels.
    1 = Pin is high.
    0 = Pin is low.

  Precondition:
    None.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT

  Returns:
    Returns the data driven on all the I/O lines of the selected port.

  Example:
    <code>

    uint32_t value;
    value = PIO_PortLatchRead(PIO_PORT_C);

    </code>

  Remarks:
    If the port has less than 32-bits, unimplemented pins will read as
    low (0).
    Implemented pins are Right aligned in the 32-bit return value.
*/
uint32_t PIO_PortLatchRead ( PIO_PORT port );

// *****************************************************************************
/* Function:
    void PIO_PortSet(PIO_PORT port, uint32_t mask)

  Summary:
    Set the selected IO pins of a port.

  Description:
    This function sets (to '1') the selected IO pins of a port.

  Precondition:
    None.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT
    mask       - A 32 bit value in which positions of 0s and 1s decide
                 which IO pins of the selected port will be set.
                 1's - Will set corresponding IO pins to high (to 1).
                 0's - Will remain unchanged.
  Returns:
    None.

  Example:
    <code>

    // Set PC5 and PC7 pins to 1
    PIO_PortSet(PIO_PORT_C, 0x00A0);

    </code>

  Remarks:
    If the port has less than 32-bits, unimplemented pins will be ignored.

    Implemented pins are Right aligned in the 32-bit value.
*/
void PIO_PortSet(PIO_PORT port, uint32_t mask);

// *****************************************************************************
/* Function:
    void PIO_PortClear(PIO_PORT port, uint32_t mask)

  Summary:
    Clear the selected IO pins of a port.

  Description:
    This function clears (to '0') the selected IO pins of a port.

  Precondition:
    None.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT
    mask       - A 32 bit value in which positions of 0s and 1s decide
                 which IO pins of the selected port will be cleared.
                 1's - Will clear corresponding IO pins to low (to 0).
                 0's - Will remain unchanged.
  Returns:
    None.

  Example:
    <code>

    // Clear PC5 and PC7 pins to 0
    PIO_PortClear(PIO_PORT_C, 0x00A0);

    </code>

  Remarks:
    If the port has less than 32-bits, unimplemented pins will be ignored.

    Implemented pins are Right aligned in the 32-bit value.
*/
void PIO_PortClear(PIO_PORT port, uint32_t mask);

// *****************************************************************************
/* Function:
    void PIO_PortToggle(PIO_PORT port, uint32_t mask)

  Summary:
    Toggles the selected IO pins of a port.

  Description:
    This function toggles (or invert) the selected IO pins of a port.

  Precondition:
    PIO_Initialize() must have been called.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT
    mask       - A 32 bit value in which positions of 0s and 1s decide
                 which IO pins of the selected port will be toggled.
                 1's - Will toggle (invert) corresponding IO pins.
                 0's - Will remain unchanged.
  Returns:
    None.

  Example:
    <code>

    // Toggles PC5 and PC7 pins
    PIO_PortToggle(PIO_PORT_C, 0x00A0);

    </code>

  Remarks:
    If the port has less than 32-bits, unimplemented pins will be ignored.

    Implemented pins are Right aligned in the 32-bit value.
*/
void PIO_PortToggle(PIO_PORT port, uint32_t mask);

// *****************************************************************************
/* Function:
    void PIO_PortInputEnable(PIO_PORT port, uint32_t mask)

  Summary:
    Enables selected IO pins of a port as input.

  Description:
    This function enables selected IO pins of a port as input.

  Precondition:
    None.

  Parameters:
    port          - One or more of the of the IO ports from the enum PIO_PORT.
    mask          - A 32 bit value in which positions of 0s and 1s decide
                    which IO pins of the selected port will be setup as inputs.
                    1's - Will set corresponding IO pins as input(s).
                    0's - Will cause the direction of the corresponding IO pins
                          to remain unchanged.
  Returns:
    None.

  Example:
    <code>

    // Make PC5 and PC7 pins as input
    PIO_PortInputEnable(PIO_PORT_C, 0x00A0);

    </code>

  Remarks:
    None.
*/
void PIO_PortInputEnable(PIO_PORT port, uint32_t mask);

// *****************************************************************************
/* Function:
    void PIO_PortOutputEnable(PIO_PORT port, uint32_t mask)

  Summary:
    Enables selected IO pins of a port as output(s).

  Description:
    This function enables selected IO pins of the given port as output(s).

  Precondition:
    None.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT
    mask       - A 32 bit value in which positions of 0s and 1s decide
                 which IO pins of the selected port will be setup as outputs.
                 1's - Will set corresponding IO pins as output(s).
                 0's - Will cause the direction of the corresponding IO pins
                       to remain unchanged.
  Returns:
    None.

  Example:
    <code>

    // Make PC5 and PC7 pins as output
    PIO_PortOutputEnable(PIO_PORT_C, 0x00A0);

    </code>

  Remarks:
    None.
*/
void PIO_PortOutputEnable(PIO_PORT port, uint32_t mask);

<#if PIO_A_INTERRUPT_USED == true ||
     PIO_B_INTERRUPT_USED == true ||
     PIO_C_INTERRUPT_USED == true ||
     PIO_D_INTERRUPT_USED == true ||
     PIO_E_INTERRUPT_USED == true >
// *****************************************************************************
/* Function:
    void PIO_PortInterruptEnable(PIO_PORT port, uint32_t mask)

  Summary:
    Enables IO interrupt on selected IO pins of a port.

  Description:
    This function enables interrupt on selected IO pins of selected port.

  Precondition:
    None.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT

    mask       - Is a 32 bit value in which positions of 0s and 1s decide
                 which IO pins of the selected port will have interrupt
                 enabled.  The bit positions of mask value which are set as 1,
                 IO interrupt of corresponding IO pin of the selected port
                 will be enabled.  The bit positions of mask value which are
                 cleared to 0, IO interrupt of corresponding IO pin of the
                 selected port will remain unchanged.

  Returns:
    None.

  Example:
    <code>

    // Enable IO interrupt for PC5 and PC7 pins
    PIO_PortInterruptEnable(PIO_PORT_C, 0x00A0);

    </code>

  Remarks:
    None.
*/
void PIO_PortInterruptEnable(PIO_PORT port, uint32_t mask);

// *****************************************************************************
/* Function:
    void PIO_PortInterruptDisable(PIO_PORT port, uint32_t mask)

  Summary:
    Disables IO interrupt on selected IO pins of a port.

  Description:
    This function disables IO interrupt on selected IO pins of selected port.

  Precondition:
    None.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT
    mask       - Is a 32 bit value in which positions of 0s and 1s decide
                 which IO pins of the selected port will have interrupt
                 disabled.  The bit positions of mask value which are set as 1,
                 IO interrupt of corresponding IO pin of the selected port
                 will be disabled.  The bit positions of mask value which are
                 cleared to 0, IO interrupt of corresponding IO pin of the
                 selected port will remain unchanged.
  Returns:
    None.

  Example:
    <code>

    // Disable IO interrupt for PB9 and PB1 pins
    PIO_PortInterruptDisable(PIO_PORT_C, 0x0202);

    </code>

  Remarks:
    None.
*/
void PIO_PortInterruptDisable(PIO_PORT port, uint32_t mask);

<#if PIO_A_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER_HEADER
        PIO_CHANNEL="A"
    />
</#if>

<#if PIO_B_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER_HEADER
        PIO_CHANNEL="B"
    />
</#if>

<#if PIO_C_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER_HEADER
        PIO_CHANNEL="C"
    />
</#if>

<#if PIO_D_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER_HEADER
        PIO_CHANNEL="D"
    />
</#if>

<#if PIO_E_INTERRUPT_USED == true>
    <@PIO_ISR_HANDLER_HEADER
        PIO_CHANNEL="E"
    />
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Local Data types and Prototypes
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* PIO Pin Callback Object

  Summary:
    Structure to hold callback related details

  Description:
    This structure is used internally by the PIO PLIB to hold pin specific
    callback details.

  Remarks:
    None.
*/
typedef struct {

    /* target pin */
    PIO_PIN                 pin;

    /* Callback for event on target pin*/
    PIO_PIN_CALLBACK        callback;

    /* Callback Context */
    uintptr_t               context;

} PIO_PIN_CALLBACK_OBJ;

// *****************************************************************************
/* Function:
    void _PIO_Interrupt_Handler ( PIO_PORT port )

  Summary:
    Interrupt handler for a selected port.

  Description:
    This function defines the internal Interrupt handler routine for selected
    PORT Channel.

  Remarks:
    It is an internal function used by the library, user need not call it.
*/
void _PIO_Interrupt_Handler ( PIO_PORT port );

</#if>

<#macro PIO_ISR_HANDLER_HEADER PIO_CHANNEL>
// *****************************************************************************
/* Function:
    void PORT${PIO_CHANNEL}_InterruptHandler (void)

  Summary:
    Interrupt handler for PORT${PIO_CHANNEL}.

  Description:
    This function defines the Interrupt handler for PORT${PIO_CHANNEL}.
    This is the function which by default gets into Interrupt Vector Table.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Remarks:
    User should not call this function.
*/
void PORT${PIO_CHANNEL}_InterruptHandler (void);
</#macro>

#include "plib_pio_pin.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_PIO_H
