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
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>
<#compress> <#-- To remove unwanted new lines -->

<#-- Initialize variables -->
<#assign TOTAL_NUM_OF_INT_USED = 0>
<#assign portNumCbList = [0]>

<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <@"<#assign GPIO_${.vars[channel]}_NUM_INT_PINS = 0>"?interpret />
        <@"<#assign port${.vars[channel]}IndexStart = 0>"?interpret />
    </#if>
</#list>

<#-- count number of active interrupts for each channel and save it in variable -->
<#list 1..GPIO_PIN_TOTAL as i>
    <#assign pinChannel = "BSP_PIN_" + i + "_PORT_CHANNEL">
    <#assign intConfig = "BSP_PIN_" + i + "_CN">

    <#if .vars[intConfig]?has_content>
        <#if (.vars[intConfig] == "True")>
            <@"<#assign GPIO_${.vars[pinChannel]}_NUM_INT_PINS = GPIO_${.vars[pinChannel]}_NUM_INT_PINS + 1>"?interpret />
            <#assign TOTAL_NUM_OF_INT_USED = TOTAL_NUM_OF_INT_USED + 1>
        </#if>
    </#if>
</#list>
</#compress>

<#-- Create a list of indexes and use it as initialization values for portNumCb array -->
<#if TOTAL_NUM_OF_INT_USED gt 0 >
    <#list 1..GPIO_CHANNEL_TOTAL-1 as i>
        <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
        <#assign prevChannel = "GPIO_CHANNEL_" + (i - 1) + "_NAME">
        <#if .vars[channel]?has_content>
            <@"<#assign port${.vars[channel]}IndexStart = port${.vars[prevChannel]}IndexStart + GPIO_${.vars[prevChannel]}_NUM_INT_PINS>"?interpret />
            <@"<#assign portNumCbList = portNumCbList + [port${.vars[channel]}IndexStart]>"?interpret />
        </#if>
    </#list>
    <#assign portNumCbList = portNumCbList + [TOTAL_NUM_OF_INT_USED] >

    <#lt>/* Array to store callback objects of each configured interrupt */
    <#lt>static volatile GPIO_PIN_CALLBACK_OBJ portPinCbObj[${TOTAL_NUM_OF_INT_USED}];

    <#lt>/* Array to store number of interrupts in each PORT Channel + previous interrupt count */
    <@compress single_line=true>
        <#lt>static uint8_t portNumCb[${GPIO_CHANNEL_TOTAL} + 1] = {
                                                                <#list portNumCbList as i>
                                                                    ${i},
                                                                </#list>
                                                            };
    </@compress>
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
    <#if PRODUCT_FAMILY?contains("PIC32CX_BZ6")>
        <#lt>    /* Disable JTAG since at least one of its pins is configured for Non-JTAG function */
        <#lt>    CFG_REGS->CFG_CFGCON0CLR = CFG_CFGCON0_JTAGEN_Msk;
    <#else>
      <#if (GPIO_PIN_TOTAL == 48)>
        <#if ((BSP_PIN_35_FUNCTION_TYPE == "TDI" || BSP_PIN_35_FUNCTION_TYPE == "") &&
          (BSP_PIN_38_FUNCTION_TYPE == "TDO" || BSP_PIN_38_FUNCTION_TYPE == "") &&
          (BSP_PIN_34_FUNCTION_TYPE == "TCK" || BSP_PIN_34_FUNCTION_TYPE == "") &&
          (BSP_PIN_37_FUNCTION_TYPE == "TMS" || BSP_PIN_37_FUNCTION_TYPE == "")) >
        <#else>
          <#lt>    /* Disable JTAG since at least one of its pins is configured for Non-JTAG function */
          <#lt>    CFG_REGS->CFG_CFGCON0CLR = CFG_CFGCON0_JTAGEN_Msk;

        </#if>
      <#elseif (GPIO_PIN_TOTAL == 32)> <#-- 32 pin devices -->
        <#if ((BSP_PIN_23_FUNCTION_TYPE == "TDI" || BSP_PIN_23_FUNCTION_TYPE == "") &&
          (BSP_PIN_26_FUNCTION_TYPE == "TDO" || BSP_PIN_26_FUNCTION_TYPE == "") &&
          (BSP_PIN_22_FUNCTION_TYPE == "TCK" || BSP_PIN_22_FUNCTION_TYPE == "") &&
          (BSP_PIN_25_FUNCTION_TYPE == "TMS" || BSP_PIN_25_FUNCTION_TYPE == "")) >
        <#else>
          <#lt>    /* Disable JTAG since at least one of its pins is configured for Non-JTAG function */
          <#lt>    CFG_REGS->CFG_CFGCON0CLR = CFG_CFGCON0_JTAGEN_Msk;

        </#if>
      <#elseif (GPIO_PIN_TOTAL == 39)> <#-- 39 pin devices -->
        <#if ((BSP_PIN_6_FUNCTION_TYPE == "TDI" || BSP_PIN_6_FUNCTION_TYPE == "") &&
          (BSP_PIN_13_FUNCTION_TYPE == "TDO" || BSP_PIN_13_FUNCTION_TYPE == "") &&
          (BSP_PIN_39_FUNCTION_TYPE == "TCK" || BSP_PIN_39_FUNCTION_TYPE == "") &&
          (BSP_PIN_12_FUNCTION_TYPE == "TMS" || BSP_PIN_12_FUNCTION_TYPE == "")) >
        <#else>
          <#lt>    /* Disable JTAG since at least one of its pins is configured for Non-JTAG function */
          <#lt>    CFG_REGS->CFG_CFGCON0CLR = CFG_CFGCON0_JTAGEN_Msk;

        </#if>
      <#elseif (GPIO_PIN_TOTAL == 30)> <#-- 30 pin devices -->
        <#if ((BSP_PIN_9_FUNCTION_TYPE == "TDI" || BSP_PIN_9_FUNCTION_TYPE == "") &&
          (BSP_PIN_15_FUNCTION_TYPE == "TDO" || BSP_PIN_15_FUNCTION_TYPE == "") &&
          (BSP_PIN_11_FUNCTION_TYPE == "TCK" || BSP_PIN_11_FUNCTION_TYPE == "") &&
          (BSP_PIN_12_FUNCTION_TYPE == "TMS" || BSP_PIN_12_FUNCTION_TYPE == "")) >
        <#else>
          <#lt>    /* Disable JTAG since at least one of its pins is configured for Non-JTAG function */
          <#lt>    CFG_REGS->CFG_CFGCON0CLR = CFG_CFGCON0_JTAGEN_Msk;

        </#if>
      </#if>
    </#if>
<#assign CFGCON2_SOSCSEL_VAL = false>
<#list 1..GPIO_PIN_TOTAL as i>
    <#assign functype = "BSP_PIN_" + i + "_FUNCTION_TYPE">
    <#assign funcname = "BSP_PIN_" + i + "_FUNCTION_NAME">
    <#assign pinPort = "BSP_PIN_" + i + "_PORT_PIN">
    <#assign pinChannel = "BSP_PIN_" + i + "_PORT_CHANNEL">
    <#if .vars[functype]?has_content && .vars[functype] == "GPIO">
        <#if .vars[funcname]?has_content>
            <#if .vars[pinPort]?has_content && (.vars[pinPort] == 11 || .vars[pinPort] == 12)>
                <#if .vars[pinChannel]?has_content && (.vars[pinChannel] == "A")>
                    <#assign CFGCON2_SOSCSEL_VAL = true>
                </#if>
            </#if>
        </#if>
    </#if>
</#list>
<#if CFGCON2_SOSCSEL_VAL == true>
    <#lt>    /* SOSCSEL - Digital (SCLKI) mode is selected */
    <#lt>    CFG_REGS->CFG_CFGCON2CLR = CFG_CFGCON2_SOSCSEL_Msk;

</#if>
<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#lt>    /* PORT${.vars[channel]} Initialization */
        <#if .vars["SYS_PORT_${.vars[channel]}_ODC"] != "0">
             <#lt>    GPIO${.vars[channel]}_REGS->GPIO_ODCSET = 0x${.vars["SYS_PORT_${.vars[channel]}_ODC"]}U; /* Open Drain Enable */
        </#if>
        <#-- if channel has even one pin configured as output, then generate code for LAT register irrespective of LAT value '0' or '1' -->
        <#if .vars["SYS_PORT_${.vars[channel]}_TRIS"] != "0">
             <#lt>    GPIO${.vars[channel]}_REGS->GPIO_LAT = 0x${.vars["SYS_PORT_${.vars[channel]}_LAT"]}U; /* Initial Latch Value */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_TRIS"] != "0">
             <#lt>    GPIO${.vars[channel]}_REGS->GPIO_TRISCLR = 0x${.vars["SYS_PORT_${.vars[channel]}_TRIS"]}U; /* Direction Control */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_ANSEL"] != "0">
             <#lt>    GPIO${.vars[channel]}_REGS->GPIO_ANSELCLR = 0x${.vars["SYS_PORT_${.vars[channel]}_ANSEL"]}U; /* Digital Mode Enable */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_CNPU"] != "0">
             <#lt>    GPIO${.vars[channel]}_REGS->GPIO_CNPUSET = 0x${.vars["SYS_PORT_${.vars[channel]}_CNPU"]}U; /* Pull-Up Enable */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_CNPD"] != "0">
             <#lt>    GPIO${.vars[channel]}_REGS->GPIO_CNPDSET = 0x${.vars["SYS_PORT_${.vars[channel]}_CNPD"]}U; /* Pull-Down Enable */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_SRCON0"] != "0">
             <#lt>    GPIO${.vars[channel]}_REGS->GPIO_SRCON0SET = 0x${.vars["SYS_PORT_${.vars[channel]}_SRCON0"]}U; /* Slew Rate Control */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_SRCON1"] != "0">
             <#lt>    GPIO${.vars[channel]}_REGS->GPIO_SRCON1SET = 0x${.vars["SYS_PORT_${.vars[channel]}_SRCON1"]}U; /* Slew Rate Control */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_CN_USED"] == true>
            <#lt>    /* Change Notice Enable */
            <#if .vars["SYS_PORT_${.vars[channel]}_CN_STYLE"] == true>
                <#lt>    GPIO${.vars[channel]}_REGS->GPIO_CNCONSET = GPIO_CNCON_ON_Msk | GPIO_CNCON_EDGEDETECT_Msk ;
            <#else>
                <#lt>    GPIO${.vars[channel]}_REGS->GPIO_CNCONSET = GPIO_CNCON_ON_Msk;
                <#lt>    GPIO${.vars[channel]}_REGS->GPIO_PORT;
            </#if>
        </#if>
    </#if>
</#list>

<#if IOLOCK_ENABLE?? && IOLOCK_ENABLE == true>
    <#if USE_PPS_INPUT_0 == true || USE_PPS_OUTPUT_0 == true>
        <#lt>    /* Unlock system for PPS configuration */
        <#lt>    CFG_REGS->CFG_SYSKEY = 0x00000000U;
        <#lt>    CFG_REGS->CFG_SYSKEY = 0xAA996655U;
        <#lt>    CFG_REGS->CFG_SYSKEY = 0x556699AAU;
        <#lt>
        <#lt>    CFG_REGS->CFG_CFGCON0CLR = CFG_CFGCON0_IOLOCK_Msk;
    </#if>
</#if>

<#lt>    /* PPS Input Remapping */
<#list 0..PPS_PIN_COUNT-1 as i>
    <#assign usePPSInputPin = "USE_PPS_INPUT_" + i>
    <#assign inputFunction = "SYS_PORT_PPS_INPUT_FUNCTION_" + i>
    <#assign remapInputPin = "SYS_PORT_PPS_INPUT_PIN_" + i>
    <#if .vars[usePPSInputPin]?has_content>
        <#if .vars[usePPSInputPin] == true>
            <#assign res = .vars[inputFunction]?matches(r"(\w+) \((\w+)\)")>
            <#if res>
                <#lt>    PPS_REGS->PPS_${res?groups[1]} = ${.vars[remapInputPin]}U;
            <#else>
                <#lt>    PPS_REGS->PPS_${.vars[inputFunction]} = ${.vars[remapInputPin]}U;
            </#if>
        </#if>
    </#if>
</#list>

<#lt>    /* PPS Output Remapping */
<#list 0..PPS_PIN_COUNT-1 as i>
    <#assign usePPSOutputPin = "USE_PPS_OUTPUT_" + i>
    <#assign outputFunction = "SYS_PORT_PPS_OUTPUT_FUNCTION_" + i>
    <#assign remapOutputPin = "SYS_PORT_PPS_OUTPUT_PIN_" + i>
    <#if .vars[usePPSOutputPin]?has_content>
        <#if .vars[usePPSOutputPin] == true>
            <#lt>    PPS_REGS->PPS_${.vars[remapOutputPin]} = ${.vars[outputFunction]}U;
        </#if>
    </#if>
</#list>

<#if IOLOCK_ENABLE?? && IOLOCK_ENABLE == true>
    <#if USE_PPS_INPUT_0 == true || USE_PPS_OUTPUT_0 == true>
        <#lt>    /* Lock back the system after PPS configuration */
        <#lt>    CFG_REGS->CFG_CFGCON0SET = CFG_CFGCON0_IOLOCK_Msk;
        <#lt>    CFG_REGS->CFG_SYSKEY = 0x00000000U;
    </#if>
</#if>

<#if TOTAL_NUM_OF_INT_USED gt 0>
    uint32_t i;
    /* Initialize Interrupt Pin data structures */
    <#list 0..GPIO_CHANNEL_TOTAL-1 as i>
        <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
        <#if .vars[channel]?has_content>
            <@"<#assign portCurNumCb_${.vars[channel]} = 0>"?interpret />
        </#if>
    </#list>
    <#list 1..GPIO_PIN_TOTAL as i>
        <#assign intConfig = "BSP_PIN_" + i + "_CN">
        <#assign portChannel = "BSP_PIN_" + i + "_PORT_CHANNEL">
        <#assign portPosition = "BSP_PIN_" + i + "_PORT_PIN">
        <#if .vars[intConfig]?has_content>
            <#if (.vars[intConfig] != "Disabled")>
                <#lt>    portPinCbObj[${.vars["port${.vars[portChannel]}IndexStart"]} + ${.vars["portCurNumCb_${.vars[portChannel]}"]}].pin = GPIO_PIN_R${.vars[portChannel]}${.vars[portPosition]};
                <#lt>    <@"<#assign portCurNumCb_${.vars[portChannel]} = portCurNumCb_${.vars[portChannel]} + 1>"?interpret />
            </#if>
        </#if>
    </#list>
    <#lt>    for(i=0U; i<${TOTAL_NUM_OF_INT_USED}U; i++)
    <#lt>    {
    <#lt>        portPinCbObj[i].callback = NULL;
    <#lt>    }
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
    return ((gpio_registers_t*)port)->GPIO_PORT;
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
    ((gpio_registers_t*)port)->GPIO_LAT = (((gpio_registers_t*)port)->GPIO_LAT & (~mask)) | (mask & value);
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
    return (((gpio_registers_t*)port)->GPIO_LAT);
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
    ((gpio_registers_t*)port)->GPIO_LATSET = mask;
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
    ((gpio_registers_t*)port)->GPIO_LATCLR = mask;
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
    ((gpio_registers_t*)port)->GPIO_LATINV= mask;
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
    ((gpio_registers_t*)port)->GPIO_TRISSET= mask;
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
    ((gpio_registers_t*)port)->GPIO_TRISCLR = mask;
}

<#if TOTAL_NUM_OF_INT_USED gt 0>
// *****************************************************************************
/* Function:
    void GPIO_PortInterruptEnable(GPIO_PORT port, uint32_t mask)

  Summary:
    Enables IO interrupt on selected IO pins of a port.

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_PortInterruptEnable(GPIO_PORT port, uint32_t mask)
{
    ((gpio_registers_t*)port)->GPIO_CNENSET = mask;
}

// *****************************************************************************
/* Function:
    void GPIO_PortInterruptDisable(GPIO_PORT port, uint32_t mask)

  Summary:
    Disables IO interrupt on selected IO pins of a port.

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_PortInterruptDisable(GPIO_PORT port, uint32_t mask)
{
    ((gpio_registers_t*)port)->GPIO_CNENCLR = mask;
}

// *****************************************************************************
// *****************************************************************************
// Section: GPIO APIs which operates on one pin at a time
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void GPIO_PinIntEnable(GPIO_PIN pin, GPIO_INTERRUPT_STYLE style)

  Summary:
    Enables IO interrupt of particular style on selected IO pins of a port.

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_PinIntEnable(GPIO_PIN pin, GPIO_INTERRUPT_STYLE style)
{
    GPIO_PORT port;
    uint32_t mask;

    port = (GPIO_PORT)(GPIOA_BASE_ADDRESS + (0x100U * (pin>>4)));
    mask =  0x1UL << (pin & 0xFU);

    if (style == GPIO_INTERRUPT_ON_MISMATCH)
    {
        ((gpio_registers_t*)port)->GPIO_CNENSET = mask;
    }
    else if (style == GPIO_INTERRUPT_ON_RISING_EDGE)
    {
        ((gpio_registers_t*)port)->GPIO_CNENSET = mask;
        ((gpio_registers_t*)port)->GPIO_CNNECLR = mask;
    }
    else if (style == GPIO_INTERRUPT_ON_FALLING_EDGE)
    {
        ((gpio_registers_t*)port)->GPIO_CNENCLR = mask;
        ((gpio_registers_t*)port)->GPIO_CNNESET = mask;
    }
    else if (style == GPIO_INTERRUPT_ON_BOTH_EDGES)
    {
        ((gpio_registers_t*)port)->GPIO_CNENSET = mask;
        ((gpio_registers_t*)port)->GPIO_CNNESET = mask;
    }
    else
    {
        /* Nothing to do */
    }
}

// *****************************************************************************
/* Function:
    void GPIO_PinIntDisable(GPIO_PIN pin)

  Summary:
    Disables IO interrupt on selected IO pins of a port.

  Remarks:
    See plib_gpio.h for more details.
*/
void GPIO_PinIntDisable(GPIO_PIN pin)
{
    GPIO_PORT port;
    uint32_t mask;

    port = (GPIO_PORT)(GPIOA_BASE_ADDRESS + (0x100U * (pin>>4)));
    mask =  0x1UL << (pin & 0xFU);

    ((gpio_registers_t*)port)->GPIO_CNENCLR = mask;
    ((gpio_registers_t*)port)->GPIO_CNNECLR = mask;
}
// *****************************************************************************
/* Function:
    bool GPIO_PinInterruptCallbackRegister(
        GPIO_PIN pin,
        const GPIO_PIN_CALLBACK callback,
        uintptr_t context
    );

  Summary:
    Allows application to register callback for configured pin.

  Remarks:
    See plib_gpio.h for more details.
*/
bool GPIO_PinInterruptCallbackRegister(
    GPIO_PIN pin,
    const GPIO_PIN_CALLBACK callback,
    uintptr_t context
)
{
    uint8_t i;
    uint8_t portIndex;

    portIndex = (uint8_t)(pin >> 4);

    for(i = portNumCb[portIndex]; i < portNumCb[portIndex +1U]; i++)
    {
        if (portPinCbObj[i].pin == pin)
        {
            portPinCbObj[i].callback = callback;
            portPinCbObj[i].context  = context;
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

<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#if .vars["SYS_PORT_${.vars[channel]}_CN_USED"] == true>

// *****************************************************************************
/* Function:
    void CHANGE_NOTICE_${.vars[channel]}_InterruptHandler(void)

  Summary:
    Interrupt Handler for change notice interrupt for channel ${.vars[channel]}.

  Remarks:
    It is an internal function called from ISR, user should not call it directly.
*/
<#if .vars["SYS_PORT_${.vars[channel]}_CN_STYLE"] == true>
<#-- ISR for edge type interrupt -->
void __attribute__((used)) CHANGE_NOTICE_${.vars[channel]}_InterruptHandler(void)
{
    uint8_t i;
    uint32_t status;
    GPIO_PIN pin;
    uintptr_t context;

    status  = GPIO${.vars[channel]}_REGS->GPIO_CNF;
    GPIO${.vars[channel]}_REGS->GPIO_CNF = 0;

    /* Check pending events and call callback if registered */
    for(i = ${portNumCbList[i]}; i < ${portNumCbList[i+1]}U; i++)
    {
        pin = portPinCbObj[i].pin;

        if((portPinCbObj[i].callback != NULL) && ((status & (1UL << (pin & 0xFU))) != 0U))
        {
            context = portPinCbObj[i].context;

            portPinCbObj[i].callback (pin, context);
        }
    }
}
<#else>
<#-- ISR for mismatch type interrupt -->
void __attribute__((used)) CHANGE_NOTICE_${.vars[channel]}_InterruptHandler(void)
{
    uint8_t i;
    uint32_t status;
    GPIO_PIN pin;
    uintptr_t context;

    status  = GPIO${.vars[channel]}_REGS->GPIO_CNSTAT;
    status &= GPIO${.vars[channel]}_REGS->GPIO_CNEN;

    GPIO${.vars[channel]}_REGS->GPIO_PORT;

    /* Check pending events and call callback if registered */
    for(i = ${portNumCbList[i]}; i < ${portNumCbList[i+1]}U; i++)
    {
        pin = portPinCbObj[i].pin;

        if((portPinCbObj[i].callback != NULL) && ((status & (1UL << (pin & 0xFU))) != 0U))
        {
            context = portPinCbObj[i].context;

            portPinCbObj[i].callback (pin, context);
        }
    }
}
</#if>
        </#if>
    </#if>
</#list>


/*******************************************************************************
 End of File
*/
