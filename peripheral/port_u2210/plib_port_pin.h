/*******************************************************************************
  PORT PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_port_pin.h

  Summary:
    Interface definition of PORT PLIB Pin related APIs

  Description:
    This file provides an interface to control and interact with PORT-I/O
    Pin related APIs.

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

#ifndef PLIB_PORT_PIN_H
#define PLIB_PORT_PIN_H

// *****************************************************************************
// *****************************************************************************
// Section: PORT Functions which operates on one pin at a time
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* Function:
    void PORT_PinWrite(PORT_PIN pin, bool value)

  Summary:
    Writes the specified value to the selected pin.

  Description:
    This function writes/drives the "value" on the selected I/O line/pin.

  Remarks:
    Refer plib_port.h file for more information.
*/

static inline void PORT_PinWrite(PORT_PIN pin, bool value)
{
    PORT_GroupWrite(PORTA_BASE_ADDRESS + (0x80 * (pin>>5)), (uint32_t)(0x1) << (pin & 0x1f), (uint32_t)(value) << (pin & 0x1f));
}

// *****************************************************************************
/* Function:
    bool PORT_PinRead(PORT_PIN pin)

  Summary:
    Read the selected pin value.

  Description:
    This function reads the present state at the selected input pin.  The
    function can also be called to read the value of an output pin if input
    sampling on the output pin is enabled in MHC. If input synchronization on
    the pin is disabled in MHC, the function will cause a 2 PORT Clock cycles
    delay. Enabling the synchronization eliminates the delay but will increase
    power consumption.

  Remarks:
    Refer plib_port.h file for more information.
*/

bool PORT_PinRead(PORT_PIN pin)
{
    return (bool)((PORT_GroupRead(PORTA_BASE_ADDRESS + (0x80 * (pin>>5))) >> (pin & 0x1F)) & 0x1);
}

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

  Remarks:
    Refer plib_port.h file for more information.
*/

bool PORT_PinLatchRead(PORT_PIN pin)
{
    return (bool)((PORT_GroupLatchRead(PORTA_BASE_ADDRESS + (0x80 * (pin>>5))) >> (pin & 0x1F)) & 0x1);
}

// *****************************************************************************
/* Function:
    void PORT_PinToggle(PORT_PIN pin)

  Summary:
    Toggles the selected pin.

  Description:
    This function toggles/inverts the present value on the selected I/O line/pin.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_PinToggle(PORT_PIN pin)
{
    PORT_GroupToggle(PORTA_BASE_ADDRESS + (0x80 * (pin>>5)), 0x1 << (pin & 0x1F));
}

// *****************************************************************************
/* Function:
    void PORT_PinSet(PORT_PIN pin)

  Summary:
    Sets the selected pin.

  Description:
    This function drives a logic 1 on the selected I/O line/pin.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_PinSet(PORT_PIN pin)
{
    PORT_GroupSet(PORTA_BASE_ADDRESS + (0x80 * (pin>>5)), 0x1 << (pin & 0x1F));
}

// *****************************************************************************
/* Function:
    void PORT_PinClear(PORT_PIN pin)

  Summary:
    Clears the selected pin.

  Description:
    This function drives a logic 0 on the selected I/O line/pin.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_PinClear(PORT_PIN pin)
{
    PORT_GroupClear(PORTA_BASE_ADDRESS + (0x80 * (pin>>5)), 0x1 << (pin & 0x1F));
}

// *****************************************************************************
/* Function:
    void PORT_PinInputEnable(PORT_PIN pin)

  Summary:
    Configures the selected IO pin as input.

  Description:
    This function configures the selected IO pin as input. This function
    override the MHC input output pin settings.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_PinInputEnable(PORT_PIN pin)
{
    PORT_GroupInputEnable(PORTA_BASE_ADDRESS + (0x80 * (pin>>5)), 0x1 << (pin & 0x1F));
}

// *****************************************************************************
/* Function:
    void PORT_PinOutputEnable(PORT_PIN pin)

  Summary:
    Enables selected IO pin as output.

  Description:
    This function enables selected IO pin as output. Calling this function will
    override the MHC input output pin configuration.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_PinOutputEnable(PORT_PIN pin)
{
    PORT_GroupOutputEnable(PORTA_BASE_ADDRESS + (0x80 * (pin>>5)), 0x1 << (pin & 0x1F));
}

#endif // PLIB_PORT_PIN_H