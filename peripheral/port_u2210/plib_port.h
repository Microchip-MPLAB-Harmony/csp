/*******************************************************************************
  PORT PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_port.h

  Summary:
    PORT PLIB Header File

  Description:
    This file provides an interface to control and interact with PORT-I/O
    Pin controller module.

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#ifndef PLIB_PORT_H
#define PLIB_PORT_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

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

// *****************************************************************************
/* PORT Channel

  Summary:
    Identifies the port groups available on the device.

  Description:
    This enumeration identifies the port groups available on the device.

  Remarks:
    The caller should not use the constant expressions assigned to any of
    the enumeration constants as these may vary between devices.

    Port group shown here are representative only. Not all ports groups are
    available on all devices.  Refer to the specific device data sheet to
    determine which ports are supported. The MHC will generate this enumeration
    with the port groups that are available on the device.
*/

typedef enum
{
    /* Group A */
    PORT_GROUP_A = PORTA_BASE_ADDRESS,

    /* Group B */
    PORT_GROUP_B = PORTB_BASE_ADDRESS,

    /* Group C */
    PORT_GROUP_C = PORTC_BASE_ADDRESS,

} PORT_GROUP;

// *****************************************************************************
/* PORT Pins

  Summary:
    Identifies the available Ports pins.

  Description:
    This enumeration identifies the available Ports pins.

  Remarks:
    The caller should not use the constant expressions assigned to any of
    the enumeration constants as these may vary between devices.

    Port pins shown here are representative only. Not all ports pins are
    available on all devices.  Refer to the specific device data sheet to
    determine which port pins are supported. The MHC will generate this
    enumeration with the port pins that are available on the device.
*/

typedef enum
{
    /* PA00 pin */
    PORT_PIN_PA00,

    /* PA01 pin */
    PORT_PIN_PA01,

    /* PA02 pin */
    PORT_PIN_PA02,

    /* PA03 pin */
    PORT_PIN_PA03,

    /* PA04 pin */
    PORT_PIN_PA04,

    /* PA05 pin */
    PORT_PIN_PA05,

    /* PA06 pin */
    PORT_PIN_PA06,

    /* PA07 pin */
    PORT_PIN_PA07,

    /* PA08 pin */
    PORT_PIN_PA08,

    /* PA09 pin */
    PORT_PIN_PA09,

    /* PA10 pin */
    PORT_PIN_PA10,

    /* PA11 pin */
    PORT_PIN_PA11,

    /* PA12 pin */
    PORT_PIN_PA12,

    /* PA13 pin */
    PORT_PIN_PA13,

    /* PA14 pin */
    PORT_PIN_PA14,

    /* PA15 pin */
    PORT_PIN_PA15,

    /* PA16 pin */
    PORT_PIN_PA16,

    /* PA17 pin */
    PORT_PIN_PA17,

    /* PA18 pin */
    PORT_PIN_PA18,

    /* PA19 pin */
    PORT_PIN_PA19,

    /* PA20 pin */
    PORT_PIN_PA20,

    /* PA21 pin */
    PORT_PIN_PA21,

    /* PA22 pin */
    PORT_PIN_PA22,

    /* PA23 pin */
    PORT_PIN_PA23,

    /* PA24 pin */
    PORT_PIN_PA24,

    /* PA25 pin */
    PORT_PIN_PA25,

    /* PA26 pin */
    PORT_PIN_PA26,

    /* PA27 pin */
    PORT_PIN_PA27,

    /* PA28 pin */
    PORT_PIN_PA28,

    /* PA29 pin */
    PORT_PIN_PA29,

    /* PA30 pin */
    PORT_PIN_PA30,

    /* PA31 pin */
    PORT_PIN_PA31,

    /* PB00 pin */
    PORT_PIN_PB00,

    /* PB01 pin */
    PORT_PIN_PB01,

    /* PB02 pin */
    PORT_PIN_PB02,

    /* PB03 pin */
    PORT_PIN_PB03,

    /* PB04 pin */
    PORT_PIN_PB04,

    /* PB05 pin */
    PORT_PIN_PB05,

    /* PB06 pin */
    PORT_PIN_PB06,

    /* PB07 pin */
    PORT_PIN_PB07,

    /* PB08 pin */
    PORT_PIN_PB08,

    /* PB09 pin */
    PORT_PIN_PB09,

    /* PB10 pin */
    PORT_PIN_PB10,

    /* PB11 pin */
    PORT_PIN_PB11,

    /* PB12 pin */
    PORT_PIN_PB12,

    /* PB13 pin */
    PORT_PIN_PB13,

    /* PB14 pin */
    PORT_PIN_PB14,

    /* PB15 pin */
    PORT_PIN_PB15,

    /* PB16 pin */
    PORT_PIN_PB16,

    /* PB17 pin */
    PORT_PIN_PB17,

    /* PB18 pin */
    PORT_PIN_PB18,

    /* PB19 pin */
    PORT_PIN_PB19,

    /* PB20 pin */
    PORT_PIN_PB20,

    /* PB21 pin */
    PORT_PIN_PB21,

    /* PB22 pin */
    PORT_PIN_PB22,

    /* PB23 pin */
    PORT_PIN_PB23,

    /* PB24 pin */
    PORT_PIN_PB24,

    /* PB25 pin */
    PORT_PIN_PB25,

    /* PB26 pin */
    PORT_PIN_PB26,

    /* PB27 pin */
    PORT_PIN_PB27,

    /* PB28 pin */
    PORT_PIN_PB28,

    /* PB29 pin */
    PORT_PIN_PB29,

    /* PB30 pin */
    PORT_PIN_PB030,

    /* PB31 pin */
    PORT_PIN_PB031,

    /* PC00 pin */
    PORT_PIN_PC00,

    /* PC01 pin */
    PORT_PIN_PC01,

    /* PC02 pin */
    PORT_PIN_PC02,

    /* PC03 pin */
    PORT_PIN_PC03,

    /* PC04 pin */
    PORT_PIN_PC04,

    /* PC05 pin */
    PORT_PIN_PC05,

    /* PC06 pin */
    PORT_PIN_PC06,

    /* PC07 pin */
    PORT_PIN_PC07,

    /* PC08 pin */
    PORT_PIN_PC08,

    /* PC09 pin */
    PORT_PIN_PC09,

    /* PC10 pin */
    PORT_PIN_PC10,

    /* PC11 pin */
    PORT_PIN_PC11,

    /* PC12 pin */
    PORT_PIN_PC12,

    /* PC13 pin */
    PORT_PIN_PC13,

    /* PC14 pin */
    PORT_PIN_PC14,

    /* PC15 pin */
    PORT_PIN_PC15,

    /* PC16 pin */
    PORT_PIN_PC16,

    /* PC17 pin */
    PORT_PIN_PC17,

    /* PC18 pin */
    PORT_PIN_PC18,

    /* PC19 pin */
    PORT_PIN_PC19,

    /* PC20 pin */
    PORT_PIN_PC20,

    /* PC21 pin */
    PORT_PIN_PC21,

    /* PC22 pin */
    PORT_PIN_PC22,

    /* PC23 pin */
    PORT_PIN_PC23,

    /* PC24 pin */
    PORT_PIN_PC24,

    /* PC25 pin */
    PORT_PIN_PC25,

    /* PC26 pin */
    PORT_PIN_PC26,

    /* PC27 pin */
    PORT_PIN_PC27,

    /* PC28 pin */
    PORT_PIN_PC28,

    /* PC29 pin */
    PORT_PIN_PC29,

    /* PC30 pin */
    PORT_PIN_PC30,

    /* PC31 pin */
    PORT_PIN_PC31,

} PORT_PIN;

// *****************************************************************************
// *****************************************************************************
// Section: Generated API based on pin configurations done in Pin Manager
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void PORT_Initialize(void)

  Summary:
    Initializes the PORT Library.

  Description:
    This function initializes all ports and pins as configured in the
    MHC Pin Manager.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>

    PORT_Initialize();

    </code>

  Remarks:
    The function should be called once before calling any other PORTS PLIB
    functions.
*/

void PORT_Initialize(void);

// *****************************************************************************
// *****************************************************************************
// Section: PORT APIs which operates on one pin at a time
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void PORT_PinWrite(PORT_PIN pin, bool value)

  Summary:
    Writes the specified value to the selected pin.

  Description:
    This function writes/drives the "value" on the selected I/O line/pin.

  Precondition:
    The PORT_Initialize() function should have been called once.

  Parameters:
    pin - One of the IO pins from the enum PORT_PIN.
    value - value to be written on the selected pin.
            true  = set pin to high (1).
            false = clear pin to low (0).

  Returns:
    None.

  Example:
    <code>

    bool value = true;
    PORT_PinWrite(PORT_PIN_PB03, value);

    </code>

  Remarks:
    Calling this function with an input pin with the pull-up/pull-down feature
    enabled will affect the pull-up/pull-down configuration. If the value is
    false, the pull-down will be enabled. If the value is true, the pull-up will
    be enabled.
*/

void PORT_PinWrite(PORT_PIN pin, bool value);

// *****************************************************************************
/* Function:
    bool PORT_PinRead(PORT_PIN pin)

  Summary:
    Read the selected pin value.

  Description:
    This function reads the present state at the selected input pin.  The
    function can also be called to read the value of an output pin if input
    sampling on the output pin is enabled in MHC.If input synchronization on
    the pin is disabled in MHC, the function will cause a 2 PORT Clock cycles
    delay. Enabling the synchronization eliminates the delay but will increase
    power consumption.

  Precondition:
    The PORT_Initialize() function should have been called. Input buffer
    (INEN bit in the Pin Configuration register) should be enabled in MHC.

  Parameters:
    pin - the port pin whose state needs to be read.

  Returns:
    true - the state at the pin is a logic high.
    false - the state at the pin is a logic low.

  Example:
    <code>

    bool value;
    value = PORT_PinRead(PORT_PIN_PB03);

    </code>

  Remarks:
    None.
*/

bool PORT_PinRead(PORT_PIN pin);

// *****************************************************************************
/* Function:
    bool PORT_PinLatchRead(PORT_PIN pin)

  Summary:
    Read the value driven on the selected pin.

  Description:
    This function reads the data driven on the selected I/O line/pin. The
    function does not sample the state of the hardware pin. It only returns the
    value that is written to output register. Refer to the PORT_PinRead()
    function if the state of the output pin needs to be read.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    pin - One of the IO pins from the enum PORT_PIN.

  Returns:
    true - the present value in the output latch is a logic high.
    false - the present value in the output latch is a logic low.

  Example:
    <code>

    bool value;
    value = PORT_PinLatchRead(PORT_PIN_PB03);

    </code>

  Remarks:
    To read actual pin value, PIN_Read API should be used.
*/

bool PORT_PinLatchRead(PORT_PIN pin);

// *****************************************************************************
/* Function:
    void PORT_PinToggle(PORT_PIN pin)

  Summary:
    Toggles the selected pin.

  Description:
    This function toggles/inverts the present value on the selected I/O line/pin.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    pin - One of the IO pins from the enum PORT_PIN.

  Returns:
    None.

  Example:
    <code>

    PORT_PinToggle(PORT_PIN_PB03);

    </code>

  Remarks:
    None.
*/

void PORT_PinToggle(PORT_PIN pin);

// *****************************************************************************
/* Function:
    void PORT_PinSet(PORT_PIN pin)

  Summary:
    Sets the selected pin.

  Description:
    This function drives a logic 1 on the selected I/O line/pin.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    pin - One of the IO pins from the enum PORT_PIN.

  Returns:
    None.

  Example:
    <code>

    PORT_PinSet(PORT_PIN_PB03);

    </code>

  Remarks:
    None.
*/

void PORT_PinSet(PORT_PIN pin);

// *****************************************************************************
/* Function:
    void PORT_PinClear(PORT_PIN pin)

  Summary:
    Clears the selected pin.

  Description:
    This function drives a logic 0 on the selected I/O line/pin.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    pin - One of the IO pins from the enum PORT_PIN.

  Returns:
    None.

  Example:
    <code>

    PORT_PinClear(PORT_PIN_PB03);

    </code>

  Remarks:
    None.
*/

void PORT_PinClear(PORT_PIN pin);

// *****************************************************************************
/* Function:
    void PORT_PinInputEnable(PORT_PIN pin)

  Summary:
    Configures the selected IO pin as input.

  Description:
    This function configures the selected IO pin as input. This function
    override the MHC input output pin settings.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    pin - One of the IO pins from the enum PORT_PIN.

  Returns:
    None.

  Example:
    <code>

    PORT_PinInputEnable(PORT_PIN_PB03);

    </code>

  Remarks:
    None.
*/

void PORT_PinInputEnable(PORT_PIN pin);

// *****************************************************************************
/* Function:
    void PORT_PinOutputEnable(PORT_PIN pin)

  Summary:
    Enables selected IO pin as output.

  Description:
    This function enables selected IO pin as output. Calling this function will
    override the MHC input output pin configuration.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    pin - One of the IO pins from the enum PORT_PIN.

  Returns:
    None.

  Example:
    <code>

    PORT_PinOutputEnable(PORT_PIN_PB03);

    </code>

  Remarks:
    None.
*/

void PORT_PinOutputEnable(PORT_PIN pin);

// *****************************************************************************
// *****************************************************************************
// Section: PORT APIs which operates on multiple pins of a group
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    uint32_t PORT_GroupRead(PORT_GROUP group)

  Summary:
    Read all the I/O pins in the specified port group.

  Description:
    The function reads the hardware pin state of all pins in the specified group
    and returns this as a 32 bit value. Each bit in the 32 bit value represent a
    pin. For example, bit 0 in group 0 will represent pin PA0. Bit 1 will
    represent PA1 and so on. The application should only consider the value of
    the port group pins which are implemented on the device.

  Precondition:
    The PORT_Initialize() function should have been called. Input buffer
    (INEN bit in the Pin Configuration register) should be enabled in MHC.

  Parameters:
    group - One of the IO groups from the enum PORT_GROUP.

  Returns:
    A 32-bit value representing the hardware state of of all the I/O pins in the
    selected port group.

  Example:
    <code>

    uint32_t value;
    value = PORT_Read(PORT_GROUP_C);

    </code>

  Remarks:
    None.
*/

uint32_t PORT_GroupRead(PORT_GROUP group);

// *****************************************************************************
/* Function:
    uint32_t PORT_GroupLatchRead(PORT_GROUP group)

  Summary:
    Read the data driven on all the I/O pins of the selected port group.

  Description:
    The function will return a 32-bit value representing the logic levels being
    driven on the output pins within the group. The function will not sample the
    actual hardware state of the output pin. Each bit in the 32-bit return value
    will represent one of the 32 port pins within the group. The application
    should only consider the value of the pins which are available on the
    device.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    group - One of the IO groups from the enum PORT_GROUP.

  Returns:
    A 32-bit value representing the output state of of all the I/O pins in the
    selected port group.

  Example:
    <code>

    uint32_t value;
    value = PORT_GroupLatchRead(PORT_GROUP_C);

    </code>

  Remarks:
    None.
*/

uint32_t PORT_GroupLatchRead(PORT_GROUP group);

// *****************************************************************************
/* Function:
    void PORT_GroupWrite(PORT_GROUP group, uint32_t mask, uint32_t value);

  Summary:
    Write value on the masked pins of the selected port group.

  Description:
    This function writes the value contained in the value parameter to the
    port group. Port group pins which are configured for output will be updated.
    The mask parameter provides additional control on the bits in the group to
    be affected. Setting a bit to 1 in the mask will cause the corresponding
    bit in the port group to be updated. Clearing a bit in the mask will cause
    that corresponding bit in the group to stay unaffected. For example,
    setting a mask value 0xFFFFFFFF will cause all bits in the port group
    to be updated. Setting a value 0x3 will only cause port group bit 0 and
    bit 1 to be updated.

    For port pins which are not configured for output and have the pull feature
    enabled, this function will affect pull value (pull up or pull down). A bit
    value of 1 will enable the pull up. A bit value of 0 will enable the pull
    down.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    group - One of the IO groups from the enum PORT_GROUP.

    mask  - A 32 bit value in which positions of 0s and 1s decide
             which IO pins of the selected port group will be written.
             1's - Will write to corresponding IO pins.
             0's - Will remain unchanged.

    value - Value which has to be written/driven on the I/O
             lines of the selected port for which mask bits are '1'.
             Values for the corresponding mask bit '0' will be ignored.
             Refer to the function description for effect on pins
             which are not configured for output.

  Returns:
    None.

  Example:
    <code>
    // Write binary value 0011 to the pins PC3, PC2, PC1 and PC0 respectively.
    PORT_GroupWrite(PORT_GROUP_C, 0x0F, 0xF563D453);

    </code>

  Remarks:
    None.
*/

void PORT_GroupWrite(PORT_GROUP group, uint32_t mask, uint32_t value);

// *****************************************************************************
/* Function:
    void PORT_GroupSet(PORT_GROUP group, uint32_t mask)

  Summary:
    Set the selected IO pins of a group.

  Description:
    This function sets (drives a logic high) on the selected output pins of a
    group. The mask parameter control the pins to be updated. A mask bit
    position with a value 1 will cause that corresponding port pin to be set. A
    mask bit position with a value 0 will cause the corresponding port pin to
    stay un-affected.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    group - One of the IO ports from the enum PORT_GROUP.
    mask - A 32 bit value in which a bit represent a pin in the group. If the
    value of the bit is 1, the corresponding port pin will driven to logic 1. If
    the value of the bit is 0. the corresponding port pin will stay un-affected.

  Returns:
    None.

  Example:
    <code>

    // Set PC5 and PC7 pins to 1
    PORT_GroupSet(PORT_GROUP_C, 0x00A0);

    </code>

  Remarks:
    If the port pin within the the group is not configured for output and has
    the pull feature enabled, driving a logic 1 on this pin will cause the pull
    up to be enabled.
*/

void PORT_GroupSet(PORT_GROUP group, uint32_t mask);

// *****************************************************************************
/* Function:
    void PORT_GroupClear(PORT_GROUP group, uint32_t mask)

  Summary:
    Clears the selected IO pins of a group.

  Description:
    This function clears (drives a logic 0) on the selected output pins of a
    group. The mask parameter control the pins to be updated. A mask bit
    position with a value 1 will cause that corresponding port pin to be clear.
    A mask bit position with a value 0 will cause the corresponding port pin to
    stay un-affected.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    group - One of the IO ports from the enum PORT_GROUP.
    mask - A 32 bit value in which a bit represent a pin in the group. If the
    value of the bit is 1, the corresponding port pin will driven to logic 0. If
    the value of the bit is 0. the corresponding port pin will stay un-affected.

  Returns:
    None.

  Example:
    <code>

    // Clear PC5 and PC7 pins to 1
    PORT_GroupClear(PORT_GROUP_C, 0x00A0);

    </code>

  Remarks:
    If the port pin within the the group is not configured for output and has
    the pull feature enabled, driving a logic 0 on this pin will cause the pull
    down to be enabled.
*/

void PORT_GroupClear(PORT_GROUP group, uint32_t mask);

// *****************************************************************************
/* Function:
    void PORT_GroupToggle(PORT_GROUP group, uint32_t mask)

  Summary:
    Toggles the selected IO pins of a group.

  Description:
    This function toggles the selected output pins of a group. The mask
    parameter control the pins to be updated. A mask bit position with a value 1
    will cause that corresponding port pin to be toggled.  A mask bit position
    with a value 0 will cause the corresponding port pin to stay un-affected.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    group - One of the IO ports from the enum PORT_GROUP.
    mask - A 32 bit value in which a bit represent a pin in the group. If the
    value of the bit is 1, the corresponding port pin will be toggled. If the
    value of the bit is 0. the corresponding port pin will stay un-affected.

  Returns:
    None.

  Example:
    <code>

    // Clear PC5 and PC7 pins to 1
    PORT_GroupToggle(PORT_GROUP_C, 0x00A0);

    </code>

  Remarks:
    If the port pin within the the group is not configured for output and has
    the pull feature enabled, driving a logic 0 on this pin will cause the pull
    down to be enabled. Driving a logic 1 on this pin will cause the pull up to
    be enabled.
*/

void PORT_GroupToggle(PORT_GROUP group, uint32_t mask);

// *****************************************************************************
/* Function:
    void PORT_GroupInputEnable(PORT_GROUP group, uint32_t mask)

  Summary:
    Confgiures the selected IO pins of a group as input.

  Description:
    This function configures the selected IO pins of a group as input. The pins
    to be configured as input are selected by setting the corresponding bits in
    the mask parameter to 1.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    group - One or more of the of the IO ports from the enum PORT_GROUP.
    mask - A 32 bit value in which a bit represents a pin in the group. If the
    value of the bit is 1, the corresponding port pin will be configured as
    input. If the value of the bit is 0. the corresponding port pin will stay
    un-affected.

  Returns:
    None.

  Example:
    <code>

    // Make PC5 and PC7 pins as input
    PORT_GroupInputEnable(PORT_GROUP_C, 0x00A0);

    </code>

  Remarks:
   None.
*/

void PORT_GroupInputEnable(PORT_GROUP group, uint32_t mask);

// *****************************************************************************
/* Function:
    void PORT_GroupOutputEnable(PORT_GROUP group, uint32_t mask)

  Summary:
    Confgiures the selected IO pins of a group as output.

  Description:
    This function configures the selected IO pins of a group as output. The pins
    to be configured as output are selected by setting the corresponding bits in
    the mask parameter to 1.

  Precondition:
    The PORT_Initialize() function should have been called.

  Parameters:
    group - One or more of the of the IO ports from the enum PORT_GROUP.
    mask - A 32 bit value in which a bit represents a pin in the group. If the
    value of the bit is 1, the corresponding port pin will be configured as
    output. If the value of the bit is 0. the corresponding port pin will stay
    un-affected.

  Returns:
    None.

  Example:
    <code>

    // Make PC5 and PC7 pins as output
    PORT_GroupOutputEnable(PORT_GROUP_C, 0x00A0);

    </code>

  Remarks:
    None.
*/

void PORT_GroupOutputEnable(PORT_GROUP group, uint32_t mask);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END
#endif // PLIB_PORT_H
