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
    <#if (PRODUCT_FAMILY == 'PIC32MZW')>
        <#if __PROCESSOR?contains("WFI")>
            <#if ((BSP_PIN_48_FUNCTION_TYPE == "TDI" || BSP_PIN_48_FUNCTION_TYPE == "") &&
                (BSP_PIN_49_FUNCTION_TYPE == "TDO" || BSP_PIN_49_FUNCTION_TYPE == "") &&
                (BSP_PIN_47_FUNCTION_TYPE == "TCK" || BSP_PIN_47_FUNCTION_TYPE == "") &&
                (BSP_PIN_46_FUNCTION_TYPE == "TMS" || BSP_PIN_46_FUNCTION_TYPE == "")) >
            <#else>
                <#lt>    /* Disable JTAG since at least one of its pins is configured for Non-JTAG function */
                <#lt>    CFGCON0bits.JTAGEN = 0U;
            </#if>
        <#else>
            <#if ((BSP_PIN_56_FUNCTION_TYPE == "TDI" || BSP_PIN_56_FUNCTION_TYPE == "") &&
                (BSP_PIN_57_FUNCTION_TYPE == "TDO" || BSP_PIN_57_FUNCTION_TYPE == "") &&
                (BSP_PIN_118_FUNCTION_TYPE == "TCK" || BSP_PIN_118_FUNCTION_TYPE == "") &&
                (BSP_PIN_119_FUNCTION_TYPE == "TMS" || BSP_PIN_119_FUNCTION_TYPE == "")) >
            <#else>
                <#lt>    /* Disable JTAG since at least one of its pins is configured for Non-JTAG function */
                <#lt>    CFGCON0bits.JTAGEN = 0U;
            </#if>
        </#if>
    </#if>

<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#lt>    /* PORT${.vars[channel]} Initialization */
        <#if .vars["SYS_PORT_${.vars[channel]}_ODC"] != "0">
             <#lt>    ODC${.vars[channel]}SET = 0x${.vars["SYS_PORT_${.vars[channel]}_ODC"]}U; /* Open Drain Enable */
        </#if>
        <#-- if channel has even one pin configured as output, then generate code for LAT register irrespective of LAT value '0' or '1' -->
        <#if .vars["SYS_PORT_${.vars[channel]}_TRIS"] != "0">
             <#lt>    LAT${.vars[channel]} = 0x${.vars["SYS_PORT_${.vars[channel]}_LAT"]}U; /* Initial Latch Value */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_TRIS"] != "0">
             <#lt>    TRIS${.vars[channel]}CLR = 0x${.vars["SYS_PORT_${.vars[channel]}_TRIS"]}U; /* Direction Control */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_ANSEL"] != "0">
             <#lt>    ANSEL${.vars[channel]}CLR = 0x${.vars["SYS_PORT_${.vars[channel]}_ANSEL"]}U; /* Digital Mode Enable */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_CNPU"] != "0">
             <#lt>    CNPU${.vars[channel]}SET = 0x${.vars["SYS_PORT_${.vars[channel]}_CNPU"]}U; /* Pull-Up Enable */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_CNPD"] != "0">
             <#lt>    CNPD${.vars[channel]}SET = 0x${.vars["SYS_PORT_${.vars[channel]}_CNPD"]}U; /* Pull-Down Enable */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_SRCON0"] != "0">
             <#lt>    SRCON0${.vars[channel]}SET = 0x${.vars["SYS_PORT_${.vars[channel]}_SRCON0"]}U; /* Slew Rate Control */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_SRCON1"] != "0">
             <#lt>    SRCON1${.vars[channel]}SET = 0x${.vars["SYS_PORT_${.vars[channel]}_SRCON1"]}U; /* Slew Rate Control */
        </#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_CN_USED"] == true>

            <#lt>    /* Change Notice Enable */
            <#if .vars["SYS_PORT_${.vars[channel]}_CN_STYLE"] == true>
                <#lt>    CNCON${.vars[channel]}SET = _CNCON${.vars[channel]}_EDGEDETECT_MASK | _CNCON${.vars[channel]}_ON_MASK;
            <#else>
                <#lt>    CNCON${.vars[channel]}SET = _CNCON${.vars[channel]}_ON_MASK;
                <#lt>    PORT${.vars[channel]};
            </#if>
            <#lt>    IEC${SYS_PORT_IFS_REG_INDEX}SET = _IEC${SYS_PORT_IFS_REG_INDEX}_CN${.vars[channel]}IE_MASK;
        </#if>
    </#if>
</#list>

<#if IOLOCK_ENABLE?? && IOLOCK_ENABLE == true>
    <#if USE_PPS_INPUT_0 == true || USE_PPS_OUTPUT_0 == true>
        <#lt>    /* Unlock system for PPS configuration */
        <#lt>    SYSKEY = 0x00000000U;
        <#lt>    SYSKEY = 0xAA996655U;
        <#lt>    SYSKEY = 0x556699AAU;

        <#if PRODUCT_FAMILY != 'PIC32MZW'>
            <#lt>    CFGCONbits.IOLOCK = 0U;
        <#else>
            <#lt>    CFGCON0bits.IOLOCK = 0U;
        </#if>
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
                <#lt>    ${res?groups[1]}R = ${.vars[remapInputPin]};
            <#else>
                <#lt>    ${.vars[inputFunction]}R = ${.vars[remapInputPin]};
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
            <#lt>    ${.vars[remapOutputPin]}R = ${.vars[outputFunction]};
        </#if>
    </#if>
</#list>

<#if IOLOCK_ENABLE?? && IOLOCK_ENABLE == true>
    <#if USE_PPS_INPUT_0 == true || USE_PPS_OUTPUT_0 == true>
        /* Lock back the system after PPS configuration */
        <#if PRODUCT_FAMILY != 'PIC32MZW'>
            <#lt>    CFGCONbits.IOLOCK = 1U;
        <#else>
            <#lt>    CFGCON0bits.IOLOCK = 1U;
        </#if>

        <#lt>    SYSKEY = 0x00000000U;
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
    return (*(volatile uint32_t *)(&PORT${GPIO_CHANNEL_0_NAME} + (port * 0x40U)));
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
    *(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME} + (port * 0x40U)) = (*(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME} + (port * 0x40U)) & (~mask)) | (mask & value);
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
    return (*(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME} + (port * 0x40U)));
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
    *(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME}SET + (port * 0x40U)) = mask;
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
    *(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME}CLR + (port * 0x40U)) = mask;
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
    *(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME}INV + (port * 0x40U))= mask;
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
    *(volatile uint32_t *)(&TRIS${GPIO_CHANNEL_0_NAME}SET + (port * 0x40U)) = mask;
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
    *(volatile uint32_t *)(&TRIS${GPIO_CHANNEL_0_NAME}CLR + (port * 0x40U)) = mask;
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
    *(volatile uint32_t *)(&CNEN${GPIO_CHANNEL_0_NAME}SET + (port * 0x40U)) = mask;
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
    *(volatile uint32_t *)(&CNEN${GPIO_CHANNEL_0_NAME}CLR + (port * 0x40U)) = mask;
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

    port = (GPIO_PORT)(pin>>4U);
    mask =  0x1UL << (pin & 0xFU);

    if (style == GPIO_INTERRUPT_ON_MISMATCH)
    {
        *(volatile uint32_t *)(&CNEN${GPIO_CHANNEL_0_NAME}SET + (port * 0x40U)) = mask;
    }
    else if (style == GPIO_INTERRUPT_ON_RISING_EDGE)
    {
        *(volatile uint32_t *)(&CNEN${GPIO_CHANNEL_0_NAME}SET + (port * 0x40U)) = mask;
        *(volatile uint32_t *)(&CNNE${GPIO_CHANNEL_0_NAME}CLR + (port * 0x40U)) = mask;
    }
    else if (style == GPIO_INTERRUPT_ON_FALLING_EDGE)
    {
        *(volatile uint32_t *)(&CNEN${GPIO_CHANNEL_0_NAME}CLR + (port * 0x40U)) = mask;
        *(volatile uint32_t *)(&CNNE${GPIO_CHANNEL_0_NAME}SET + (port * 0x40U)) = mask;
    }
    else if (style == GPIO_INTERRUPT_ON_BOTH_EDGES)
    {
        *(volatile uint32_t *)(&CNEN${GPIO_CHANNEL_0_NAME}SET + (port * 0x40U)) = mask;
        *(volatile uint32_t *)(&CNNE${GPIO_CHANNEL_0_NAME}SET + (port * 0x40U)) = mask;
    }
    else
    {
        /* Nothing to process */
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

    port = (GPIO_PORT)(pin>>4U);
    mask =  0x1UL << (pin & 0xFU);

    *(volatile uint32_t *)(&CNEN${GPIO_CHANNEL_0_NAME}CLR + (port * 0x40U)) = mask;
    *(volatile uint32_t *)(&CNNE${GPIO_CHANNEL_0_NAME}CLR + (port * 0x40U)) = mask;
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

    portIndex = (uint8_t)(pin >> 4U);

    for(i = portNumCb[portIndex]; i < portNumCb[portIndex +1]; i++)
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

    status  = CNF${.vars[channel]};
    CNF${.vars[channel]} = 0U;

    IFS${SYS_PORT_IFS_REG_INDEX}CLR = _IFS${SYS_PORT_IFS_REG_INDEX}_CN${.vars[channel]}IF_MASK;

    /* Check pending events and call callback if registered */
    for(i = ${portNumCbList[i]}; i < ${portNumCbList[i+1]}; i++)
    {
        pin = portPinCbObj[i].pin;

        if((portPinCbObj[i].callback != NULL) && ((status & ((uint32_t)1U << (pin & 0xFU))) != 0U))
        {
            context = portPinCbObj[i].context;

            portPinCbObj[i].callback (pin, context);
        }
    }
}
<#else>    <#-- ISR for mismatch type interrupt -->
void __attribute__((used)) CHANGE_NOTICE_${.vars[channel]}_InterruptHandler(void)
{
    uint8_t i;
    uint32_t status;
    GPIO_PIN pin;
    uintptr_t context;

    status  = CNSTAT${.vars[channel]};
    status &= CNEN${.vars[channel]};

    PORT${.vars[channel]};
    IFS${SYS_PORT_IFS_REG_INDEX}CLR = _IFS${SYS_PORT_IFS_REG_INDEX}_CN${.vars[channel]}IF_MASK;

    /* Check pending events and call callback if registered */
    for(i = ${portNumCbList[i]}; i < ${portNumCbList[i+1]}; i++)
    {
        pin = portPinCbObj[i].pin;

        if((portPinCbObj[i].callback != NULL) && ((status & ((uint32_t)1U << (pin & 0xFU))) != 0U))
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
