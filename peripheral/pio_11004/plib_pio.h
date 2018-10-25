/*******************************************************************************
  PIO PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pio.h

  Summary:
    PIO PLIB Documentation File

  Description:
    This library provides documentation of all the interface to control and
    interact with Parallel Input/Output controller (PIO) module.

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

#ifndef PLIB_PIOx_H
#define PLIB_PIOx_H

// *****************************************************************************
// *****************************************************************************
// Section: Data types and constants
// *****************************************************************************
// *****************************************************************************

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
    PIO_PORT_A,
    PIO_PORT_B,
    PIO_PORT_C,
    PIO_PORT_D,
    PIO_PORT_E
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
    PIO_PIN_PA0,
    PIO_PIN_PA1,
    PIO_PIN_PA2,
    PIO_PIN_PA3,
    PIO_PIN_PA4,
    PIO_PIN_PA5,
    PIO_PIN_PA6,
    PIO_PIN_PA7,
    PIO_PIN_PA8,
    PIO_PIN_PA9,
    PIO_PIN_PA10,
    PIO_PIN_PA11,
    PIO_PIN_PA12,
    PIO_PIN_PA13,
    PIO_PIN_PA14,
    PIO_PIN_PA15,
    PIO_PIN_PA16,
    PIO_PIN_PA17,
    PIO_PIN_PA18,
    PIO_PIN_PA19,
    PIO_PIN_PA20,
    PIO_PIN_PA21,
    PIO_PIN_PA22,
    PIO_PIN_PA23,
    PIO_PIN_PA24,
    PIO_PIN_PA25,
    PIO_PIN_PA26,
    PIO_PIN_PA27,
    PIO_PIN_PA28,
    PIO_PIN_PA29,
    PIO_PIN_PA30,
    PIO_PIN_PA31,
    PIO_PIN_PB0,
    PIO_PIN_PB1,
    PIO_PIN_PB2,
    PIO_PIN_PB3,
    PIO_PIN_PB4,
    PIO_PIN_PB5,
    PIO_PIN_PB6,
    PIO_PIN_PB7,
    PIO_PIN_PB8,
    PIO_PIN_PB9,
    PIO_PIN_PB12,
    PIO_PIN_PB13,
    PIO_PIN_PC0,
    PIO_PIN_PC1,
    PIO_PIN_PC2,
    PIO_PIN_PC3,
    PIO_PIN_PC4,
    PIO_PIN_PC5,
    PIO_PIN_PC6,
    PIO_PIN_PC7,
    PIO_PIN_PC8,
    PIO_PIN_PC9,
    PIO_PIN_PC10,
    PIO_PIN_PC11,
    PIO_PIN_PC12,
    PIO_PIN_PC13,
    PIO_PIN_PC14,
    PIO_PIN_PC15,
    PIO_PIN_PC16,
    PIO_PIN_PC17,
    PIO_PIN_PC18,
    PIO_PIN_PC19,
    PIO_PIN_PC20,
    PIO_PIN_PC21,
    PIO_PIN_PC22,
    PIO_PIN_PC23,
    PIO_PIN_PC24,
    PIO_PIN_PC25,
    PIO_PIN_PC26,
    PIO_PIN_PC27,
    PIO_PIN_PC28,
    PIO_PIN_PC29,
    PIO_PIN_PC30,
    PIO_PIN_PC31,
    PIO_PIN_PD0,
    PIO_PIN_PD1,
    PIO_PIN_PD2,
    PIO_PIN_PD3,
    PIO_PIN_PD4,
    PIO_PIN_PD5,
    PIO_PIN_PD6,
    PIO_PIN_PD7,
    PIO_PIN_PD8,
    PIO_PIN_PD9,
    PIO_PIN_PD10,
    PIO_PIN_PD11,
    PIO_PIN_PD12,
    PIO_PIN_PD13,
    PIO_PIN_PD14,
    PIO_PIN_PD15,
    PIO_PIN_PD16,
    PIO_PIN_PD17,
    PIO_PIN_PD18,
    PIO_PIN_PD19,
    PIO_PIN_PD20,
    PIO_PIN_PD21,
    PIO_PIN_PD22,
    PIO_PIN_PD23,
    PIO_PIN_PD24,
    PIO_PIN_PD25,
    PIO_PIN_PD26,
    PIO_PIN_PD27,
    PIO_PIN_PD28,
    PIO_PIN_PD29,
    PIO_PIN_PD30,
    PIO_PIN_PD31,
    PIO_PIN_PE0,
    PIO_PIN_PE1,
    PIO_PIN_PE2,
    PIO_PIN_PE3,
    PIO_PIN_PE4,
    PIO_PIN_PE5,

    /* This element should not be used in any of the PIO APIs.
       It will be used by other modules or application to denote that none of the PIO Pin is used */
    PIO_PIN_NONE

} PIO_PIN;

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
    pin - One of the IO pins from the enum PIO_PIN
    context - Value identifying the context of the client that registered the
              event handling function

  Returns:
    None.

  Example:
    A function matching this signature:
    <code>
        void APP_PinEventHandler(PIO_PIN pin, uintptr_t context)
        {
            // Do Something
        }
    </code>
    Is registered as follows:
    <code>
        PIO_PinInterruptCallbackRegister(PIO_PIN_PA5, &APP_PinEventHandler, NULL);
    </code>

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
    in the MHC Pin Manager.

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
    - 1 - Pin is high.
    - 0 - Pin is low.
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
    If the port has less than 32-bits, unimplemented pins will read as low (0).

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
    - 1 - Pin is driven high.
    - 0 - Pin is driven low.

  Precondition:
    The desired pins lines of the selected port must be setup as output(s) in
    MHC Pin Manager.

    PIO_Initialize() must have been called.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT
    mask       - A 32 bit value in which positions of 0s and 1s decide
                 which IO pins of the selected port will be written.
                 - 1's - Will write to corresponding IO pins.
                 - 0's - Will remain unchanged.
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
    - 1 - Pin is high.
    - 0 - Pin is low.

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
                 - 1's - Will set corresponding IO pins to high (to 1).
                 - 0's - Will remain unchanged.
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
                 - 1's - Will clear corresponding IO pins to low (to 0).
                 - 0's - Will remain unchanged.
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
                 - 1's - Will toggle (invert) corresponding IO pins.
                 - 0's - Will remain unchanged.
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
                    - 1's - Will set corresponding IO pins as input(s).
                    - 0's - Will cause the direction of the corresponding IO pins
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
                 - 1's - Will set corresponding IO pins as output(s).
                 - 0's - Will cause the direction of the corresponding IO pins
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

// *****************************************************************************
/* Function:
    void PIO_PortInterruptEnable(PIO_PORT port, uint32_t mask)

  Summary:
    Enables IO interrupt on selected IO pins of a port.

  Description:
    This function enables interrupt on selected IO pins of selected port.

  Precondition:
    Corresponding pins must be configured in interrupt mode in MHC Pin Manager.

    PIO_Initialize() must have been called.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT

    mask       - Is a 32 bit value in which positions of 0s and 1s decide
                 which IO pins of the selected port will have interrupt
                 enabled.
                 - The bit positions of mask value which are set as 1, IO
                   interrupt of corresponding IO pin of the selected port will
                   be enabled.
                 - The bit positions of mask value which are cleared to 0, IO
                   interrupt of corresponding IO pin of the selected port will
                   remain unchanged.
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
    Corresponding pins must be configured in interrupt mode in MHC Pin Manager.

    PIO_Initialize() must have been called.

  Parameters:
    port       - One of the IO ports from the enum PIO_PORT
    mask       - Is a 32 bit value in which positions of 0s and 1s decide
                 which IO pins of the selected port will have interrupt
                 disabled.
                 - The bit positions of mask value which are set as 1, IO
                   interrupt of corresponding IO pin of the selected port will
                   be disabled.
                 - The bit positions of mask value which are cleared to 0, IO
                   interrupt of corresponding IO pin of the selected port will
                   remain unchanged.
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
    The desired pin must be configured as an output pin in MHC Pin Manager.

    PIO_Initialize() must have been called.

  Parameters:
    pin       - One of the IO pins from the enum PIO_PIN
    value     - value to be written on the selected pin:
                - true - set pin to high (1).
                - false - clear pin to low (0).

  Returns:
    None.

  Example:
    <code>
        PIO_PinWrite(PIO_PIN_PB3, true);
    </code>

  Remarks:
    None.
*/
void PIO_PinWrite(PIO_PIN pin, bool value);

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
bool PIO_PinRead(PIO_PIN pin);

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
bool PIO_PinLatchRead( PIO_PIN pin);

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
void PIO_PinToggle(PIO_PIN pin);

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
void PIO_PinSet(PIO_PIN pin);

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
void PIO_PinClear(PIO_PIN pin);

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
void PIO_PinInputEnable(PIO_PIN pin);

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
void PIO_PinOutputEnable(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinInterruptEnable(PIO_PIN pin)

  Summary:
    Enables IO interrupt on selected IO pin.

  Description:
    This function enables interrupt on selected IO pin.

  Precondition:
    Corresponding pin must be configured in interrupt mode in MHC Pin Manager.

    PIO_Initialize() must have been called.

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
void PIO_PinInterruptEnable(PIO_PIN pin);

// *****************************************************************************
/* Function:
    void PIO_PinInterruptDisable(PIO_PIN pin)

  Summary:
    Disables IO interrupt on selected IO pin.

  Description:
    This function disables IO interrupt on selected IO pin.

  Precondition:
    Corresponding pin must be configured in interrupt mode in MHC Pin Manager.

    PIO_Initialize() must have been called.

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
void PIO_PinInterruptDisable(PIO_PIN pin);

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
    Corresponding pin must be configured in interrupt mode in MHC Pin Manager.

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
    const PIO_PIN_CALLBACK callBack,
    uintptr_t context
);

#endif // PLIB_PIOx_H