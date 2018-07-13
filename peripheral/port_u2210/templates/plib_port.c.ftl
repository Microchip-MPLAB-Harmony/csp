/*******************************************************************************
  PORT PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_port.c

  Summary:
    Interface definition of PORT PLIB

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_port.h"

// *****************************************************************************
// *****************************************************************************
// Section: PORT Implementation
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

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_Initialize(void)
{
<#list 0..PORT_GROUP_COUNT as n>
    <#assign PORT_GROUP_INDEX = n>
    <#assign PORT_GROUP = "PORT_GROUP_"+ n>
        <#if .vars[PORT_GROUP]!false>
        <#lt>   /*************************** GROUP ${PORT_GROUP_INDEX} Initialization ****************************/
        <#assign PORT_DIR = "PORT_GROUP_" + n + "_DIR">
        <#assign PORT_CTRL = "PORT_GROUP_" + n + "_CTRL">
        <#if "${.vars[PORT_DIR]}" != "0x00000000">
            <#lt>   PORT_REGS->PORT_GROUP[${PORT_GROUP_INDEX}].DIR = ${.vars[PORT_DIR]};
        </#if>
        <#if "${.vars[PORT_CTRL]}" != "0x00000000">
            <#lt>   PORT_REGS->PORT_GROUP[${PORT_GROUP_INDEX}].CTRL = ${.vars[PORT_CTRL]};
        </#if>
        <#list 0..31 as i>
        <#assign PORT_PINCONFIG_PMUXEN = "PORT_GROUP_" + n + "_PINCFG"+ i +"_PMUXEN">
        <#assign PORT_PINCONFIG_INEN = "PORT_GROUP_" + n + "_PINCFG"+ i +"_INEN">
        <#assign PORT_PINCONFIG_DRVSTR = "PORT_GROUP_" + n + "_PINCFG"+ i +"_DRVSTR">
        <#assign PORT_PINCONFIG_PULLEN = "PORT_GROUP_" + n + "_PINCFG"+ i +"_PULLEN">
        <#assign PORT_INDEX = i>
            <#if .vars[PORT_PINCONFIG_PMUXEN]!"true">
                <#lt>   PORT_REGS->PORT_GROUP[${PORT_GROUP_INDEX}].PINCFG[${PORT_INDEX}] = PORT_GROUP_PINCFG_PMUXEN_Msk;
            </#if>
            <#if .vars[PORT_PINCONFIG_INEN]!"true">
                <#lt>   PORT_REGS->PORT_GROUP[${PORT_GROUP_INDEX}].PINCFG[${PORT_INDEX}] |= PORT_GROUP_PINCFG_INEN_Msk;
            </#if>
            <#if .vars[PORT_PINCONFIG_PULLEN]!"true">
                <#lt>   PORT_REGS->PORT_GROUP[${PORT_GROUP_INDEX}].PINCFG[${PORT_INDEX}] |= PORT_GROUP_PINCFG_PULLEN_Msk;
            </#if>
            <#if .vars[PORT_PINCONFIG_DRVSTR]!"true">
                <#lt>   PORT_REGS->PORT_GROUP[${PORT_GROUP_INDEX}].PINCFG[${PORT_INDEX}] |= PORT_GROUP_PINCFG_DRVSTR_Msk;
            </#if>
        </#list>
        <#list 0..15 as i>
        <#assign PORT_PINMUX = "PORT_GROUP_" + n + "_PMUX"+ i>
        <#assign PORT_INDEX = i>
        <#if "${.vars[PORT_PINMUX]}" != "0x00">
            <#lt>   PORT_REGS->PORT_GROUP[${PORT_GROUP_INDEX}].PMUX[${PORT_INDEX}] = ${.vars[PORT_PINMUX]};
        </#if>
        </#list>
        </#if>
</#list>
}

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

void PORT_PinWrite(PORT_PIN pin, bool value)
{
    uint32_t group = 0;

    group = pin / 32;
    pin =  pin % 32;

    if (value == false)
    {
        PORT_REGS->PORT_GROUP[group].OUTCLR = 1 << pin;
    }
    else
    {
        PORT_REGS->PORT_GROUP[group].OUTSET = 1 << pin;
    }
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
    uint32_t group = 0;

    group = pin / 32;
    pin =  pin % 32;

    return (bool)((PORT_REGS->PORT_GROUP[group].IN >> pin) & 0x01);
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
    uint32_t group = 0;

    group = pin / 32;
    pin =  pin % 32;

    return (bool)((PORT_REGS->PORT_GROUP[group].OUT >> pin) & 0x01);
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
    uint32_t group = 0;

    group = pin / 32;
    pin =  pin % 32;

    PORT_REGS->PORT_GROUP[group].OUTTGL = 1 << pin;
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
    uint32_t group= 0;

    group = pin / 32;
    pin =  pin % 32;

    PORT_REGS->PORT_GROUP[group].OUTSET = 1 << pin;
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
    uint32_t group = 0;

    group = pin / 32;
    pin =  pin % 32;

    PORT_REGS->PORT_GROUP[group].OUTCLR = 1 << pin;
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
    uint32_t group = 0;

    group = pin / 32;
    pin =  pin % 32;

    PORT_REGS->PORT_GROUP[group].DIRCLR = 1 << pin;
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
    uint32_t group = 0;

    group = pin / 32;
    pin =  pin % 32;

    PORT_REGS->PORT_GROUP[group].DIRSET = 1 << pin;
}

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

  Remarks:
    Refer plib_port.h file for more information.
*/

uint32_t PORT_GroupRead(PORT_GROUP group)
{
    return (PORT_REGS->PORT_GROUP[group].IN);
}

// *****************************************************************************
/* Function:
    void PORT_GroupWrite(PORT_GROUP group, uint32_t value);

  Summary:
    Write value on all the pins of the selected port group.

  Description:
    This function writes value to the entire port group. Port group pins which
    are configured for output will updated with corresponding value.

    For port pins which are not configured for output and have the pull feature
    enabled, this function will affect pull value (pull up or pull down). A bit
    value of 1 will enable the pull up. A bit value of 0 will enable the pull
    down.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_GroupWrite(PORT_GROUP group, uint32_t value)
{
    /* Write the desired value */
    PORT_REGS->PORT_GROUP[group].OUT = value;
}

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

  Remarks:
    Refer plib_port.h file for more information.
*/

uint32_t PORT_GroupLatchRead(PORT_GROUP group)
{
    return (PORT_REGS->PORT_GROUP[group].OUT);
}

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

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_GroupSet(PORT_GROUP group, uint32_t mask)
{
    PORT_REGS->PORT_GROUP[group].OUTSET = mask;
}

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

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_GroupClear(PORT_GROUP group, uint32_t mask)
{
    PORT_REGS->PORT_GROUP[group].OUTCLR = mask;
}

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

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_GroupToggle(PORT_GROUP group, uint32_t mask)
{
    PORT_REGS->PORT_GROUP[group].OUTTGL = mask;
}

// *****************************************************************************
/* Function:
    void PORT_GroupInputEnable(PORT_GROUP group, uint32_t mask)

  Summary:
    Confgiures the selected IO pins of a group as input.

  Description:
    This function configures the selected IO pins of a group as input. The pins
    to be configured as input are selected by setting the corresponding bits in
    the mask parameter to 1.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_GroupInputEnable(PORT_GROUP group, uint32_t mask)
{
    PORT_REGS->PORT_GROUP[group].DIRCLR = mask;
}

// *****************************************************************************
/* Function:
    void PORT_GroupOutputEnable(PORT_GROUP group, uint32_t mask)

  Summary:
    Confgiures the selected IO pins of a group as output.

  Description:
    This function configures the selected IO pins of a group as output. The pins
    to be configured as output are selected by setting the corresponding bits in
    the mask parameter to 1.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_GroupOutputEnable(PORT_GROUP group, uint32_t mask)
{
    PORT_REGS->PORT_GROUP[group].DIRSET = mask;
}