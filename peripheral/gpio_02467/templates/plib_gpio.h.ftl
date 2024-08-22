/*******************************************************************************
  GPIO PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_gpio.h UUUUUUUUU

  Summary:
    GPIO PLIB Header File

  Description:
    This library provides an interface to control and interact with Parallel
    Input/Output controller (GPIO) module.

*******************************************************************************/

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

#ifndef PLIB_GPIO_H
#define PLIB_GPIO_H

#include <device.h>
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

<#assign GPIO_ATLEAST_ONE_INTERRUPT_USED = false>

<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#assign GPIO_ATLEAST_ONE_INTERRUPT_USED = GPIO_ATLEAST_ONE_INTERRUPT_USED || .vars["SYS_PORT_${.vars[channel]}_CN_USED"]>
    </#if>
</#list>

<#-- Create List of all the port pins for enum creation -->

<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <@"<#assign PORT${.vars[channel]}_Pin_List = []>"?interpret />
    </#if>
</#list>

<#list 1..GPIO_PIN_TOTAL as i>
    <#assign pinPort = "BSP_PIN_" + i + "_PORT_PIN">
    <#assign pinChannel = "BSP_PIN_" + i + "_PORT_CHANNEL">

    <#if .vars[pinPort]?has_content>
        <#if .vars[pinChannel]?has_content && .vars[pinChannel] != "None">
                <@"<#assign PORT${.vars[pinChannel]}_Pin_List = PORT${.vars[pinChannel]}_Pin_List + [.vars[pinPort]]>"?interpret />
        </#if>
    </#if>
</#list>

</#compress>
<#-- Generate Pin Macros for Port pins with Custom name -->
    <#list 1..GPIO_PIN_TOTAL as i>
        <#assign functype = "BSP_PIN_" + i + "_FUNCTION_TYPE">
        <#assign funcname = "BSP_PIN_" + i + "_FUNCTION_NAME">
        <#assign pinPort = "BSP_PIN_" + i + "_PORT_PIN">
        <#assign pinChannel = "BSP_PIN_" + i + "_PORT_CHANNEL">
        <#assign interruptType = "BSP_PIN_" + i + "_CN">
        <#if .vars[functype]?has_content>
            <#if .vars[funcname]?has_content>
                <#if .vars[pinPort]?has_content>
                    <#if .vars[pinChannel]?has_content>
                        <#if !(.vars[functype]?starts_with("SWITCH_") | .vars[functype]?starts_with("LED_") | .vars[functype]?starts_with("VBUS_"))>

                            <#lt>/*** Macros for ${.vars[funcname]} pin ***/
                            <#if .vars[functype] == "GPIO">
                                <#lt>#define ${.vars[funcname]}_Set()               (LAT${.vars[pinChannel]}SET = (1U<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_Clear()             (LAT${.vars[pinChannel]}CLR = (1U<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_Toggle()            (LAT${.vars[pinChannel]}INV= (1U<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_OutputEnable()      (TRIS${.vars[pinChannel]}CLR = (1U<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_InputEnable()       (TRIS${.vars[pinChannel]}SET = (1U<<${.vars[pinPort]}))
                            </#if>
                            <#lt>#define ${.vars[funcname]}_Get()               ((PORT${.vars[pinChannel]} >> ${.vars[pinPort]}) & 0x1U)
                            <#lt>#define ${.vars[funcname]}_GetLatch()          ((LAT${.vars[pinChannel]} >> ${.vars[pinPort]}) & 0x1U)
                            <#lt>#define ${.vars[funcname]}_PIN                  GPIO_PIN_R${.vars[pinChannel]}${.vars[pinPort]}
                            <#if .vars[interruptType]?has_content>
                                <#lt>#define ${.vars[funcname]}_InterruptEnable()   (CNEN${.vars[pinChannel]}SET = (1U<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_InterruptDisable()  (CNEN${.vars[pinChannel]}CLR = (1U<<${.vars[pinPort]}))
                            </#if>
                        </#if>
                    </#if>
                </#if>
            </#if>
        </#if>
    </#list>


// *****************************************************************************
/* GPIO Port

  Summary:
    Identifies the available GPIO Ports.

  Description:
    This enumeration identifies the available GPIO Ports.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all ports are available on all devices.  Refer to the specific
    device data sheet to determine which ports are supported.
*/


<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#if (.vars["PORT${.vars[channel]}_Pin_List"])?has_content>
                <#lt>#define    GPIO_PORT_${.vars[channel]}  (${i})
        </#if>
    </#if>
</#list>
typedef uint32_t GPIO_PORT;

typedef enum
{
    GPIO_INTERRUPT_ON_MISMATCH,
    GPIO_INTERRUPT_ON_RISING_EDGE,
    GPIO_INTERRUPT_ON_FALLING_EDGE,
    GPIO_INTERRUPT_ON_BOTH_EDGES,
}GPIO_INTERRUPT_STYLE;

// *****************************************************************************
/* GPIO Port Pins

  Summary:
    Identifies the available GPIO port pins.

  Description:
    This enumeration identifies the available GPIO port pins.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all pins are available on all devices.  Refer to the specific
    device data sheet to determine which pins are supported.
*/


<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#if .vars["PORT${.vars[channel]}_Pin_List"]?has_content>
            <@"<#assign PORT${.vars[channel]}_Pin_List =  PORT${.vars[channel]}_Pin_List?sort>"?interpret />
            <#list .vars["PORT${.vars[channel]}_Pin_List"] as pin>
                <#lt>#define     GPIO_PIN_R${.vars[channel]}${pin}  (${pin+(16*i)}U)
            </#list>
        </#if>
    </#if>
</#list>

    /* This element should not be used in any of the GPIO APIs.
       It will be used by other modules or application to denote that none of the GPIO Pin is used */
#define    GPIO_PIN_NONE   (-1)

typedef uint32_t GPIO_PIN;

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true >
typedef  void (*GPIO_PIN_CALLBACK) ( GPIO_PIN pin, uintptr_t context);
</#if>

void GPIO_Initialize(void);

// *****************************************************************************
// *****************************************************************************
// Section: GPIO Functions which operates on multiple pins of a port
// *****************************************************************************
// *****************************************************************************

uint32_t GPIO_PortRead(GPIO_PORT port);

void GPIO_PortWrite(GPIO_PORT port, uint32_t mask, uint32_t value);

uint32_t GPIO_PortLatchRead ( GPIO_PORT port );

void GPIO_PortSet(GPIO_PORT port, uint32_t mask);

void GPIO_PortClear(GPIO_PORT port, uint32_t mask);

void GPIO_PortToggle(GPIO_PORT port, uint32_t mask);

void GPIO_PortInputEnable(GPIO_PORT port, uint32_t mask);

void GPIO_PortOutputEnable(GPIO_PORT port, uint32_t mask);

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true >
void GPIO_PortInterruptEnable(GPIO_PORT port, uint32_t mask);

void GPIO_PortInterruptDisable(GPIO_PORT port, uint32_t mask);

// *****************************************************************************
// *****************************************************************************
// Section: Local Data types and Prototypes
// *****************************************************************************
// *****************************************************************************

typedef struct {

    /* target pin */
    GPIO_PIN                 pin;

    /* Callback for event on target pin*/
    GPIO_PIN_CALLBACK        callback;

    /* Callback Context */
    uintptr_t               context;

} GPIO_PIN_CALLBACK_OBJ;

</#if>
// *****************************************************************************
// *****************************************************************************
// Section: GPIO Functions which operates on one pin at a time
// *****************************************************************************
// *****************************************************************************

static inline void GPIO_PinWrite(GPIO_PIN pin, bool value)
{
     uint32_t xvalue = (uint32_t)value;
    GPIO_PortWrite((pin>>4U), (uint32_t)(0x1U) << (pin & 0xFU), (xvalue) << (pin & 0xFU));
}

static inline bool GPIO_PinRead(GPIO_PIN pin)
{
    return ((((GPIO_PortRead((GPIO_PORT)(pin>>4U))) >> (pin & 0xFU)) & 0x1U) != 0U);
}

static inline bool GPIO_PinLatchRead(GPIO_PIN pin)
{
    return (((GPIO_PortLatchRead((GPIO_PORT)(pin>>4U)) >> (pin & 0xFU)) & 0x1U) != 0U);
}

static inline void GPIO_PinToggle(GPIO_PIN pin)
{
    GPIO_PortToggle((pin>>4U), (uint32_t)0x1U << (pin & 0xFU));
}

static inline void GPIO_PinSet(GPIO_PIN pin)
{
    GPIO_PortSet((pin>>4U), (uint32_t)0x1U << (pin & 0xFU));
}

static inline void GPIO_PinClear(GPIO_PIN pin)
{
    GPIO_PortClear((pin>>4U), (uint32_t)0x1U << (pin & 0xFU));
}

static inline void GPIO_PinInputEnable(GPIO_PIN pin)
{
    GPIO_PortInputEnable((pin>>4U), (uint32_t)0x1U << (pin & 0xFU));
}

static inline void GPIO_PinOutputEnable(GPIO_PIN pin)
{
    GPIO_PortOutputEnable((pin>>4U), (uint32_t)0x1U << (pin & 0xFU));
}

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true >
#define GPIO_PinInterruptEnable(pin)       GPIO_PinIntEnable(pin, GPIO_INTERRUPT_ON_MISMATCH)
#define GPIO_PinInterruptDisable(pin)      GPIO_PinIntDisable(pin)

void GPIO_PinIntEnable(GPIO_PIN pin, GPIO_INTERRUPT_STYLE style);
void GPIO_PinIntDisable(GPIO_PIN pin);

bool GPIO_PinInterruptCallbackRegister(
    GPIO_PIN pin,
    const   GPIO_PIN_CALLBACK callback,
    uintptr_t context
);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_GPIO_H
