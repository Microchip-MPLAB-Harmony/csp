/*******************************************************************************
  SYS PORTS Static Functions for PORTS System Service

  Company:
    Microchip Technology Inc.

  File Name:
    plib_gpio.c

  Summary:
    GPIO function implementations for the GPIO PLIB.

  Description:
    The GPIO PLIB provides a simple interface to manage peripheral
    input-output controller.

*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
//DOM-IGNORE-END

#include "plib_gpio.h"
<#compress> <#-- To remove unwanted new lines -->

<#-- Initialize variables -->
<#assign TOTAL_NUM_OF_INT_USED = 0>

<#-- count number of active interrupts and save it in variable -->
<#list 1..CN_PIN_TOTAL as i>
    <#assign intConfig = "BSP_PIN_" + i + "_CN">
    <#if .vars[intConfig]?has_content>
        <#if (.vars[intConfig] == "True")>
            <#assign TOTAL_NUM_OF_INT_USED = TOTAL_NUM_OF_INT_USED + 1>
        </#if>
    </#if>
</#list>
</#compress>

<#-- Create a list of indexes and use it as initialization values for portNumCb array -->
<#if TOTAL_NUM_OF_INT_USED gt 0 >
    <#lt>#define TOTAL_NUM_OF_INT_USED ${TOTAL_NUM_OF_INT_USED}
    <#lt>/* Array to store pin objects of each configured interrupt */
    <#lt>GPIO_PIN_CALLBACK_OBJ cnPinObj[TOTAL_NUM_OF_INT_USED] =
                                <#lt>    {
                                <#list 1..CN_PIN_TOTAL as i>
                                    <#assign intConfig = "BSP_PIN_" + i + "_CN">
                                    <#assign gpioPin = "CN_PIN_" + i + "_NAME">
                                    <#if (.vars[intConfig]?has_content) && (.vars[intConfig] == "True")>
                                        <#lt>        {.cnPin = CN${i}_PIN , .gpioPin = ${.vars[gpioPin]}, .callback = NULL },
                                    </#if>
                                </#list>
                                <#lt>    };
</#if>


/******************************************************************************
  Function:
    GPIO_Initialize ( void )

  Summary:
    Initialize the GPIO library.

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_Initialize ( void )
{
<#if SYS_PORT_AD1PCFG != "0">
        <#lt>    AD1PCFGSET = 0x${.vars["SYS_PORT_AD1PCFG"]}; /* Digital Mode Enable */
</#if>

<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#lt>    /* PORT${.vars[channel]} Initialization */
        <#if .vars["SYS_PORT_${.vars[channel]}_ODC"] != "0">
             <#lt>    ODC${.vars[channel]}SET = 0x${.vars["SYS_PORT_${.vars[channel]}_ODC"]}; /* Open Drain Enable */
        </#if>
        <#-- if channel has even one pin configured as output, then generate code for LAT register irrespective of LAT value '0' or '1' -->
        <#if .vars["SYS_PORT_${.vars[channel]}_TRIS"] != "0">
             <#lt>    LAT${.vars[channel]} = 0x${.vars["SYS_PORT_${.vars[channel]}_LAT"]}; /* Initial Latch Value */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_TRIS"] != "0">
             <#lt>    TRIS${.vars[channel]}CLR = 0x${.vars["SYS_PORT_${.vars[channel]}_TRIS"]}; /* Direction Control */
        </#if>

    </#if>
</#list>

<#if SYS_PORT_CNPUE != "0">
        <#lt>    CNPUESET = 0x${SYS_PORT_CNPUE}; /* Pull-Up Enable */
</#if>
<#if SYS_PORT_ATLEAST_ONE_CN_USED == true>
        <#lt>    /* Change Notice Enable */
        <#lt>    CNCONSET = _CNCON_ON_MASK;
        <#lt>    IEC${SYS_PORT_IFS_REG_INDEX}SET = _IEC${SYS_PORT_IFS_REG_INDEX}_CNIE_MASK;

    uint8_t i, bitPosition;
    uint32_t latestPortValue, mask;

    /* save the initial pin value for CN pins */
    for(i = 0; i < TOTAL_NUM_OF_INT_USED; i++)
    {
        latestPortValue = *(volatile uint32_t *)(&PORT${GPIO_CHANNEL_0_NAME} + ((cnPinObj[i].gpioPin >> 4) * 0x10));
        bitPosition = cnPinObj[i].gpioPin % 16;
        mask = 1 << bitPosition;
        cnPinObj[i].prevPinValue = (bool)((latestPortValue & mask) >> bitPosition);
    }

</#if>
}

// *****************************************************************************
// *****************************************************************************
// Section: GPIO APIs which operates on multiple pins of a port
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    uint32_t GPIO_PortRead ( GPIO_PORT port )

  Summary:
    Read all the I/O lines of the selected port.

  Description:
    This function reads the live data values on all the I/O lines of the
    selected port.  Bit values returned in each position indicate corresponding
    pin levels.
    1 = Pin is high.
    0 = Pin is low.

    This function reads the value regardless of pin configuration, whether it is
    set as as an input, driven by the GPIO Controller, or driven by a peripheral.

  Remarks:
    If the port has less than 32-bits, unimplemented pins will read as
    low (0).
    Implemented pins are Right aligned in the 32-bit return value.
*/
uint32_t GPIO_PortRead(GPIO_PORT port)
{
    return (*(volatile uint32_t *)(&PORT${GPIO_CHANNEL_0_NAME} + (port * 0x10)));
}

// *****************************************************************************
/* Function:
    void GPIO_PortWrite (GPIO_PORT port, uint32_t mask, uint32_t value);

  Summary:
    Write the value on the masked I/O lines of the selected port.

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_PortWrite(GPIO_PORT port, uint32_t mask, uint32_t value)
{
    *(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME} + (port * 0x10)) = (*(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME} + (port * 0x10)) & (~mask)) | (mask & value);
}

// *****************************************************************************
/* Function:
    uint32_t GPIO_PortLatchRead ( GPIO_PORT port )

  Summary:
    Read the latched value on all the I/O lines of the selected port.

  Remarks:
    See plib_gpio.h for more details.
*/
uint32_t GPIO_PortLatchRead(GPIO_PORT port)
{
    return (*(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME} + (port * 0x10)));
}

// *****************************************************************************
/* Function:
    void GPIO_PortSet ( GPIO_PORT port, uint32_t mask )

  Summary:
    Set the selected IO pins of a port.

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_PortSet(GPIO_PORT port, uint32_t mask)
{
    *(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME}SET + (port * 0x10)) = mask;
}

// *****************************************************************************
/* Function:
    void GPIO_PortClear ( GPIO_PORT port, uint32_t mask )

  Summary:
    Clear the selected IO pins of a port.

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_PortClear(GPIO_PORT port, uint32_t mask)
{
    *(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME}CLR + (port * 0x10)) = mask;
}

// *****************************************************************************
/* Function:
    void GPIO_PortToggle ( GPIO_PORT port, uint32_t mask )

  Summary:
    Toggles the selected IO pins of a port.

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_PortToggle(GPIO_PORT port, uint32_t mask)
{
    *(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME}INV + (port * 0x10))= mask;
}

// *****************************************************************************
/* Function:
    void GPIO_PortInputEnable ( GPIO_PORT port, uint32_t mask )

  Summary:
    Enables selected IO pins of a port as input.

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_PortInputEnable(GPIO_PORT port, uint32_t mask)
{
    *(volatile uint32_t *)(&TRIS${GPIO_CHANNEL_0_NAME}SET + (port * 0x10)) = mask;
}

// *****************************************************************************
/* Function:
    void GPIO_PortOutputEnable ( GPIO_PORT port, uint32_t mask )

  Summary:
    Enables selected IO pins of a port as output(s).

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_PortOutputEnable(GPIO_PORT port, uint32_t mask)
{
    *(volatile uint32_t *)(&TRIS${GPIO_CHANNEL_0_NAME}CLR + (port * 0x10)) = mask;
}

<#if TOTAL_NUM_OF_INT_USED gt 0>

void GPIO_PinInterruptEnable(CN_PIN cnPin)
{
    CNENSET = cnPin;
}

void GPIO_PinInterruptDisable(CN_PIN cnPin)
{
    CNENCLR = cnPin;
}

// *****************************************************************************
// *****************************************************************************
// Section: GPIO APIs which operates on one pin at a time
// *****************************************************************************
// *****************************************************************************
bool GPIO_PinInterruptCallbackRegister(
    CN_PIN cnPin,
    const GPIO_PIN_CALLBACK callback,
    uintptr_t context
)
{
    uint8_t i;

    for(i = 0; i < TOTAL_NUM_OF_INT_USED; i++)
    {
        if (cnPinObj[i].cnPin == cnPin)
        {
            cnPinObj[i].callback = callback;
            cnPinObj[i].context  = context;
            return true;
        }
    }
    return false;
}

// *****************************************************************************
// *****************************************************************************
// Section: Local Function Implementation
// *****************************************************************************
// *****************************************************************************
</#if>

<#if TOTAL_NUM_OF_INT_USED gt 0>
/* Function:
    void CHANGE_NOTICE_InterruptHandler()

  Summary:
    Interrupt Handler for change notice interrupt.

  Remarks:
	It is an internal function called from ISR, user should not call it directly.
*/
void CHANGE_NOTICE_InterruptHandler()
{
    uint8_t i, bitPosition;
    uint32_t latestPortValue, mask;
    bool currPinValue;

    /* Check which CN interrupt has occurred and call callback if registered */
    for(i = 0; i < TOTAL_NUM_OF_INT_USED; i++)
    {
        latestPortValue = *(volatile uint32_t *)(&PORT${GPIO_CHANNEL_0_NAME} + ((cnPinObj[i].gpioPin >> 4) * 0x10));
        bitPosition = cnPinObj[i].gpioPin % 16;
        mask = 1 << bitPosition;
        currPinValue = (bool)((latestPortValue & mask) >> bitPosition);
        if((cnPinObj[i].prevPinValue != currPinValue) && (cnPinObj[i].callback != NULL))
        {
            cnPinObj[i].prevPinValue = currPinValue;
            cnPinObj[i].callback (cnPinObj[i].cnPin, cnPinObj[i].context);
        }
    }
    IFS${SYS_PORT_IFS_REG_INDEX}CLR = _IFS${SYS_PORT_IFS_REG_INDEX}_CNIF_MASK;
}
</#if>

/*******************************************************************************
 End of File
*/
