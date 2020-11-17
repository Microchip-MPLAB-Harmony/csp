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
    <#assign PORT_GROUP = "PORT_GROUP_"+ n>
    <#assign PORT_GROUP_NAME = "PORT_GROUP_NAME_" + n>
    <#assign PORT_GROUP_EVCTRL = "PORT_GROUP_" + n + "_EVCTRL">
        <#if .vars[PORT_GROUP]!false>
            <#lt>   /************************** GROUP ${.vars[PORT_GROUP_NAME]} Initialization *************************/
            <#assign PORT_DIR = "PORT_GROUP_" + n + "_DIR">
            <#assign PORT_OUT = "PORT_GROUP_" + n + "_OUT">
            <#assign PORT_CTRL = "PORT_GROUP_" + n + "_CTRL">
            <#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
              <#assign PORT_NONSEC = "PORT_GROUP_" + n + "_NONSEC">
            </#if>
                <#if "${.vars[PORT_DIR]}" != "0x0">
                    <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_DIR = ${.vars[PORT_DIR]};
                </#if>
                <#if "${.vars[PORT_OUT]}" != "0x0">
                    <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_OUT = ${.vars[PORT_OUT]};
                </#if>
                <#if "${.vars[PORT_CTRL]}" != "0x0">
                    <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_CTRL = ${.vars[PORT_CTRL]};
                </#if>
                <#list 0..31 as i>
                    <#assign PORT_PINCONFIG = "PORT_GROUP_" + n + "_PINCFG" + i>
                    <#assign PORT_GROUP_PINCFG_INDEX = i>
                    <#if "${.vars[PORT_PINCONFIG]}" != "0x0">
                        <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_PINCFG[${PORT_GROUP_PINCFG_INDEX}] = ${.vars[PORT_PINCONFIG]};
                    </#if>
                </#list>

                <#list 0..15 as i>
                    <#assign PORT_PINMUX = "PORT_GROUP_" + n + "_PMUX"+ i>
                    <#assign PORT_INDEX = i>
                    <#if "${.vars[PORT_PINMUX]}" != "0x0">
                        <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_PMUX[${PORT_INDEX}] = ${.vars[PORT_PINMUX]};
                    </#if>
                </#list>
                <#if .vars[PORT_GROUP_EVCTRL]??>
                <#if "${.vars[PORT_GROUP_EVCTRL]}" != "0x0">
                    <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_EVCTRL = ${.vars[PORT_GROUP_EVCTRL]};
                </#if>
                </#if>

                <#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
                  <#if "${.vars[PORT_NONSEC]}" != "0x0">
                    <#lt>   ${PORT_REG_NAME}_REGS->GROUP[${.vars[PORT_GROUP_NAME]}].PORT_NONSEC = 0x${.vars[PORT_NONSEC]};
                  </#if>
                </#if>
        </#if>
</#list>
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
    return (((port_group_registers_t*)group)->PORT_IN);
}

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

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_GroupWrite(PORT_GROUP group, uint32_t mask, uint32_t value)
{
    /* Write the desired value */
    ((port_group_registers_t*)group)->PORT_OUT = (((port_group_registers_t*)group)->PORT_OUT & (~mask)) | (mask & value);
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
    return (((port_group_registers_t*)group)->PORT_OUT);
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
    ((port_group_registers_t*)group)->PORT_OUTSET = mask;
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
    ((port_group_registers_t*)group)->PORT_OUTCLR = mask;
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
    ((port_group_registers_t*)group)->PORT_OUTTGL = mask;
}

// *****************************************************************************
/* Function:
    void PORT_GroupInputEnable(PORT_GROUP group, uint32_t mask)

  Summary:
    Configures the selected IO pins of a group as input.

  Description:
    This function configures the selected IO pins of a group as input. The pins
    to be configured as input are selected by setting the corresponding bits in
    the mask parameter to 1.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_GroupInputEnable(PORT_GROUP group, uint32_t mask)
{
    ((port_group_registers_t*)group)->PORT_DIRCLR = mask;
}

// *****************************************************************************
/* Function:
    void PORT_GroupOutputEnable(PORT_GROUP group, uint32_t mask)

  Summary:
    Configures the selected IO pins of a group as output.

  Description:
    This function configures the selected IO pins of a group as output. The pins
    to be configured as output are selected by setting the corresponding bits in
    the mask parameter to 1.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_GroupOutputEnable(PORT_GROUP group, uint32_t mask)
{
   ((port_group_registers_t*)group)->PORT_DIRSET = mask;
}

// *****************************************************************************
/* Function:
    void PORT_PinPeripheralFunctionConfig(PORT_PIN pin, PERIPHERAL_FUNCTION function)

  Summary:
    Configures the peripheral function on the selected port pin

  Description:
    This function configures the selected peripheral function on the given port pin.

  Remarks:
    Refer plib_port.h file for more information.
*/

void PORT_PinPeripheralFunctionConfig(PORT_PIN pin, PERIPHERAL_FUNCTION function)
{
    uint32_t pin_pos = (uint32_t) pin;
    uint32_t port_group_num = (pin_pos >> 5);
    uint32_t pin_num = pin - (port_group_num << 5);
    uint32_t periph_func = (uint32_t) function;

    port_group_registers_t* port_group = (port_group_registers_t*)(PORT_BASE_ADDRESS + (port_group_num * 0x80));

    /* For odd pins */
    if (pin_pos & 0x01)
    {
        port_group->PORT_PMUX[(pin_num >> 1)] = (port_group->PORT_PMUX[(pin_num >> 1)] & ~0xF0) | (periph_func << 4);
    }
    /* For even pins */
    else
    {
        port_group->PORT_PMUX[(pin_num >> 1)] = (port_group->PORT_PMUX[(pin_num >> 1)] & ~0x0F) | periph_func;
    }

    /* Enable peripheral control of the pin */
     port_group->PORT_PINCFG[pin_num] |= PORT_PINCFG_PMUXEN_Msk;
}

// *****************************************************************************
/* Function:
    void PORT_PinGPIOConfig(PORT_PIN pin)

  Summary:
    Configures the selected pin as GPIO

  Description:
    This function configures the given pin as GPIO.

  Remarks:
    Refer plib_port.h file for more information.
*/
void PORT_PinGPIOConfig(PORT_PIN pin)
{
    uint32_t pin_pos = (uint32_t) pin;
    uint32_t port_group_num = (pin_pos >> 5);
    uint32_t pin_num = pin - (port_group_num << 5);

    port_group_registers_t* port_group = (port_group_registers_t*)(PORT_BASE_ADDRESS + (port_group_num * 0x80));

    /* Disable peripheral control of the pin */
    port_group->PORT_PINCFG[pin_num] &= ~PORT_PINCFG_PMUXEN_Msk;
}