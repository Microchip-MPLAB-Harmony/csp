/**
 * General Purpose Input Output(GPIO) PLIB Implementation
 * 
 * @file      plib_gpio.c
 * 
 * @ingroup   gpio
 * 
 * @brief     dsPIC33A GPIO Module PLIB Source File
*/

#include "plib_gpio.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>
/**
* @brief   Offset value between registers LAT, TRIS, PORT 
*/
<#lt>#define OFFSET_REG (uint32_t)${REGISTER_OFFSET}UL 

/**
* @brief  Offset value between two interrupt registers CNEN0, CNEN1, CNCON
*/
<#lt>#define OFFSET_INT (uint32_t)${CN_INTERRUPT_OFFSET}UL 
 
<#if USE_PPS_INPUT_0 == true || USE_PPS_OUTPUT_0 == true>
/**
* @brief   Macro to lock registers for PPS configuration.
*/
#define PINS_PPSLock()           (${PPSPinsLockBit} = 1)

/**
* @brief   Macro to unlock registers for PPS configuration.
*/
#define PINS_PPSUnlock()         (${PPSPinsLockBit} = 0)
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
    <#lt>volatile static GPIO_PIN_CALLBACK_OBJ portPinCbObj[${TOTAL_NUM_OF_INT_USED}];

    <#lt>/* Array to store number of interrupts in each PORT Channel + previous interrupt count */
    <@compress single_line=true>
        <#lt>static uint8_t portNumCb[${GPIO_CHANNEL_TOTAL} + 1] = {
                                                                <#list portNumCbList as i>
                                                                    ${i},
                                                                </#list>
                                                            };
    </@compress>
</#if>



<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#assign channelIfs = "GPIO_CHANNEL_" + i + "_IFS">
    <#if .vars[channel]?has_content>
		<#if .vars["SYS_PORT_${.vars[channel]}_CN_USED"] == true>
void CN${.vars[channel]}_InterruptHandler(void);
</#if>
</#if>
</#list>


void GPIO_Initialize ( void )
{
<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
	<#assign channelIfs = "GPIO_CHANNEL_" + i + "_IFS">
	<#assign isChannelConfigured = "GPIO_CHANNEL_"+ .vars[channel] +"_CONFIG">
    <#if .vars[channel]?has_content>
		<#if .vars[isChannelConfigured]?has_content && .vars[isChannelConfigured] == true>
		<#lt>     /*PORT${.vars[channel]} Initialization */
		</#if>
        <#if .vars["SYS_PORT_${.vars[channel]}_ODC"] != .vars["SYS_PORT_${.vars[channel]}_ODC_INIT_VAL"]>
             <#lt>    ODC${.vars[channel]} = 0x${.vars["SYS_PORT_${.vars[channel]}_ODC"]}U; /* Open Drain Enable */
	    </#if>
        <#-- if channel has even one pin configured as output, then generate code for LAT register irrespective of LAT value '0' or '1' -->
        <#if .vars["SYS_PORT_${.vars[channel]}_TRIS"] != .vars["SYS_PORT_${.vars[channel]}_TRIS_INIT_VAL"]>
             <#lt>    LAT${.vars[channel]} = 0x${.vars["SYS_PORT_${.vars[channel]}_LAT"]}U; /* Initial Latch Value */
        </#if>
		<#if .vars["SYS_PORT_${.vars[channel]}_CNPU"] != .vars["SYS_PORT_${.vars[channel]}_CNPU_INIT_VAL"]>
             <#lt>    CNPU${.vars[channel]}= 0x${.vars["SYS_PORT_${.vars[channel]}_CNPU"]}U; /* Pull-Up Enable */
        </#if>
		<#if .vars["SYS_PORT_${.vars[channel]}_CNPD"] != .vars["SYS_PORT_${.vars[channel]}_CNPD_INIT_VAL"]>
             <#lt>    CNPD${.vars[channel]} = 0x${.vars["SYS_PORT_${.vars[channel]}_CNPD"]}U; /* Pull-Down Enable */
        </#if>
		<#if .vars["SYS_PORT_${.vars[channel]}_TRIS"] != .vars["SYS_PORT_${.vars[channel]}_TRIS_INIT_VAL"]>
             <#lt>    TRIS${.vars[channel]} = 0x${.vars["SYS_PORT_${.vars[channel]}_TRIS"]}U; /* Direction Control */
        </#if>
		<#if .vars["SYS_PORT_${.vars[channel]}_ANSEL"] != .vars["SYS_PORT_${.vars[channel]}_ANSEL_INIT_VAL"]>
             <#lt>    ANSEL${.vars[channel]}= 0x${.vars["SYS_PORT_${.vars[channel]}_ANSEL"]}U; /* Digital Mode Enable */
        </#if>
		<#if .vars["SYS_PORT_${.vars[channel]}_CN_USED"] == true>
		
			<#lt>    /* Change Notice Enable */
            <#if .vars["SYS_PORT_${.vars[channel]}_CN_STYLE"] == true>
				<#lt>    CNCON${.vars[channel]} = _CNCON${.vars[channel]}_CNSTYLE_MASK | _CNCON${.vars[channel]}_ON_MASK;
            <#else>
                <#lt>    CNCON${.vars[channel]} = _CNCON${.vars[channel]}_ON_MASK;
                <#lt>    PORT${.vars[channel]};
            </#if>
			<#if .vars[channelIfs]?has_content>
                <#lt>    IEC${.vars[channelIfs]}bits.CN${.vars[channel]}IE = 1;
			</#if>
        </#if>
    </#if>
</#list>    

<#if USE_PPS_INPUT_0 == true || USE_PPS_OUTPUT_0 == true>
    <#lt>    /* Unlock system for PPS configuration */
    <#lt>    PINS_PPSUnlock();
</#if>

<#if USE_PPS_INPUT_0 == true>
	<#lt> /* PPS Input Mapping */
</#if>
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

<#if USE_PPS_OUTPUT_0 == true>
	<#lt> /* PPS Output Mapping */
</#if>
<#list 0..PPS_PIN_COUNT-1 as i>
    <#assign usePPSOutputPin = "USE_PPS_OUTPUT_" + i>
    <#assign outputFunction = "SYS_PORT_PPS_OUTPUT_FUNCTION_" + i>
    <#assign remapOutputPin = "SYS_PORT_PPS_OUTPUT_PIN_" + i>
    <#if .vars[usePPSOutputPin]?has_content>
        <#if .vars[usePPSOutputPin] == true>
			<#lt>    ${.vars[remapOutputPin]} = ${.vars[outputFunction]};
        </#if>
    </#if>
</#list>

<#if USE_PPS_INPUT_0 == true || USE_PPS_OUTPUT_0 == true>
    <#lt>    /* Lock back the system after PPS configuration */
    <#lt>    PINS_PPSLock();
        
</#if>

<#if TOTAL_NUM_OF_INT_USED gt 0>
    uint32_t cb_index;
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
				<#assign portIndexStart = .vars["port${.vars[portChannel]}IndexStart"]>
				<#assign portCurNumCb = .vars["portCurNumCb_${.vars[portChannel]}"]>
				<#assign combSym = portIndexStart + portCurNumCb>
                <#lt>    portPinCbObj[${combSym}].pin = GPIO_PIN_R${.vars[portChannel]}${.vars[portPosition]};
                <#lt>    <@"<#assign portCurNumCb_${.vars[portChannel]} = portCurNumCb_${.vars[portChannel]} + 1>"?interpret />
            </#if>
        </#if>
    </#list>
    <#lt>    for(cb_index=0U; cb_index<${TOTAL_NUM_OF_INT_USED}U; cb_index++)
    <#lt>    {
    <#lt>        portPinCbObj[cb_index].callback = NULL;
    <#lt>    }
</#if>
}

// Section: GPIO APIs which operates on multiple pins of a port

uint32_t  GPIO_PortRead(GPIO_PORT port)
{
    return (*(volatile uint32_t *)((uint32_t)&PORT${GPIO_CHANNEL_0_NAME} + (port * OFFSET_REG)));
}

void  GPIO_PortWrite(GPIO_PORT port, uint32_t mask, uint32_t value)
{
    if (value == (uint32_t)0x1) {
        *(volatile uint32_t *)((uint32_t)&LAT${GPIO_CHANNEL_0_NAME} + (port * OFFSET_REG)) = (*(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME} + (port * OFFSET_REG)) & (~mask)) | (mask);
    } 
    else if (value == (uint32_t)0x0) {
        *(volatile uint32_t *)((uint32_t)&LAT${GPIO_CHANNEL_0_NAME} + (port * OFFSET_REG)) = (*(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME} + (port * OFFSET_REG)) & (~mask));
    }
	else{
		*(volatile uint32_t *)((uint32_t)&LAT${GPIO_CHANNEL_0_NAME} + (port * OFFSET_REG)) = (*(volatile uint32_t *)(&LAT${GPIO_CHANNEL_0_NAME} + (port * OFFSET_REG)) & (~mask)) | (value);
	}
}

uint32_t  GPIO_PortLatchRead(GPIO_PORT port)
{
    return (*(volatile uint32_t *)((uint32_t)&LAT${GPIO_CHANNEL_0_NAME} + (port * OFFSET_REG)));
}

void  GPIO_PortSet(GPIO_PORT port, uint32_t mask)
{
	*(volatile uint32_t *)((uint32_t)&LATA +(port * OFFSET_REG)) |= mask;
}

void  GPIO_PortClear(GPIO_PORT port, uint32_t mask)
{
	*(volatile uint32_t *)((uint32_t)&LATA + (port * OFFSET_REG)) &= ~mask;
}

void  GPIO_PortToggle(GPIO_PORT port, uint32_t mask)
{
	*(volatile uint32_t *)((uint32_t)&LATA +(port * OFFSET_REG)) ^= mask;
}

void  GPIO_PortInputEnable(GPIO_PORT port, uint32_t mask)
{
	*(volatile uint32_t *)((uint32_t)&TRISA +(port * OFFSET_REG)) |= mask;
}

void  GPIO_PortOutputEnable(GPIO_PORT port, uint32_t mask)
{
	*(volatile uint32_t *)((uint32_t)&TRISA + (port * OFFSET_REG)) &= ~mask;
}

<#if TOTAL_NUM_OF_INT_USED gt 0>

void  GPIO_PortInterruptEnable(GPIO_PORT port, uint32_t mask)
{
	*(volatile uint32_t *)((uint32_t)&CNEN0A +(port * OFFSET_INT)) |= mask;
}

void  GPIO_PortInterruptDisable(GPIO_PORT port, uint32_t mask)
{
	*(volatile uint32_t *)((uint32_t)&CNEN0A + (port * OFFSET_INT)) &= ~mask;
}

// Section: GPIO APIs which operates on one pin at a time

void  GPIO_PinIntEnable(GPIO_PIN pin, GPIO_INTERRUPT_STYLE style)
{
    GPIO_PORT port;
    uint32_t mask;
    port = (GPIO_PORT)(pin>>4);
    mask =  (uint32_t)0x1U << (pin & 0xFU);

    if (style == GPIO_INTERRUPT_ON_MISMATCH){
        *(volatile uint32_t *)((uint32_t)&CNEN0A + (port * OFFSET_INT)) |= mask;
    }
        
    else if (style == GPIO_INTERRUPT_ON_POSITIVE_EDGE)
    {
        *(volatile uint32_t *)((uint32_t)&CNEN0A +(port * OFFSET_INT)) |= mask;
		*(volatile uint32_t *)((uint32_t)&CNEN1A +(port * OFFSET_INT)) &= ~mask;
    }
	else if (style == GPIO_INTERRUPT_ON_NEGATIVE_EDGE)
    {
        *(volatile uint32_t *)((uint32_t)&CNEN1A +(port * OFFSET_INT)) |=  mask;
        *(volatile uint32_t *)((uint32_t)&CNEN0A +(port * OFFSET_INT)) &= ~mask;
    }
	else if (style == GPIO_INTERRUPT_ON_ANY_EDGES)
	{
		*(volatile uint32_t *)((uint32_t)&CNEN1A +(port * OFFSET_INT)) |= mask;
		*(volatile uint32_t *)((uint32_t)&CNEN0A +(port * OFFSET_INT)) |= mask;
	}
    else
    {
        //Nothing to process
    }
}

void  GPIO_PinIntDisable(GPIO_PIN pin)
{
    GPIO_PORT port;
    uint32_t mask;

    port = (GPIO_PORT)(pin>>4);
    mask =  (uint32_t)0x1U << (pin & 0xFU);

    *(volatile uint32_t *)((uint32_t)&CNEN0A + (port * OFFSET_INT)) &= ~mask;
    *(volatile uint32_t *)((uint32_t)&CNEN1A + (port * OFFSET_INT)) &= ~mask;
}

bool GPIO_PinInterruptCallbackRegister(
    GPIO_PIN pin,
    const GPIO_PIN_CALLBACK callback,
    uintptr_t context
)
{
    uint8_t cb_index;
    uint8_t portIndex;

    portIndex = (uint8_t)(pin >> 4);

    for(cb_index = portNumCb[portIndex]; cb_index < portNumCb[portIndex +1]; cb_index++)
    {
        if (portPinCbObj[cb_index].pin == pin)
        {
            portPinCbObj[cb_index].callback = callback;
            portPinCbObj[cb_index].context  = context;
            return true;
        }
    }
    return false;
}

// Section: Local Function Implementation
</#if>
<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#assign channelIfs = "GPIO_CHANNEL_" + i + "_IFS">
    <#if .vars[channel]?has_content>
        <#if .vars["SYS_PORT_${.vars[channel]}_CN_USED"] == true>

<#if .vars["SYS_PORT_${.vars[channel]}_CN_STYLE"] == true>
<#-- ISR for edge type interrupt -->
void __attribute__((used)) CN${.vars[channel]}_InterruptHandler(void)
{
    uint8_t cb_index;
    uint32_t status;
    GPIO_PIN pin;
    uintptr_t context;

    status  = CNF${.vars[channel]};
    CNF${.vars[channel]} = 0;
	
    <#if .vars[channelIfs]?has_content>
    IFS${.vars[channelIfs]}bits.CN${.vars[channel]}IF = 0;
	</#if>
    /* Check pending events and call callback if registered */
    for(cb_index = ${portNumCbList[i]}U; cb_index < ${portNumCbList[i+1]}U; cb_index++)
    {
        pin = portPinCbObj[cb_index].pin;

        if((portPinCbObj[cb_index].callback != NULL) && (status & (1 << (pin & 0xFU))))
        {
            context = portPinCbObj[cb_index].context;

            portPinCbObj[cb_index].callback (pin, context);
        }
    }
}
<#else>    <#-- ISR for mismatch type interrupt -->
void __attribute__((used)) CN${.vars[channel]}_InterruptHandler(void)
{
    uint8_t cb_index;
    uint32_t status;
    GPIO_PIN pin;
    uintptr_t context;

    status  = CNSTAT${.vars[channel]};
    status &= CNEN0${.vars[channel]};

    PORT${.vars[channel]};
	<#if .vars[channelIfs]?has_content>
    IFS${.vars[channelIfs]}bits.CN${.vars[channel]}IF = 0;
	</#if>

    /* Check pending events and call callback if registered */
    for(cb_index = ${portNumCbList[i]}U; cb_index< ${portNumCbList[i+1]}U; cb_index++)
    {
        pin = portPinCbObj[cb_index].pin;

        if((portPinCbObj[cb_index].callback != NULL) && ((status & (1UL << (pin & 0xFU))) != 0U))
        {
            context = portPinCbObj[cb_index].context;
            portPinCbObj[cb_index].callback (pin, context);
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
