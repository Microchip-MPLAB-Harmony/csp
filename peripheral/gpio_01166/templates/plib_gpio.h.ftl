/*******************************************************************************
  GPIO PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_gpio.h

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
                                <#lt>#define ${.vars[funcname]}_Set()               (LAT${.vars[pinChannel]}SET = (1<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_Clear()             (LAT${.vars[pinChannel]}CLR = (1<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_Toggle()            (LAT${.vars[pinChannel]}INV= (1<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_OutputEnable()      (TRIS${.vars[pinChannel]}CLR = (1<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_InputEnable()       (TRIS${.vars[pinChannel]}SET = (1<<${.vars[pinPort]}))
                            </#if>
                            <#lt>#define ${.vars[funcname]}_Get()               ((PORT${.vars[pinChannel]} >> ${.vars[pinPort]}) & 0x1)
                            <#lt>#define ${.vars[funcname]}_PIN                  GPIO_PIN_R${.vars[pinChannel]}${.vars[pinPort]}
                            <#if .vars[interruptType]?has_content>
                                <#lt>#define ${.vars[funcname]}_InterruptEnable()   (CNEN${.vars[pinChannel]}SET = (1<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_InterruptDisable()  (CNEN${.vars[pinChannel]}CLR = (1<<${.vars[pinPort]}))
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
                <#lt>#define    GPIO_PORT_${.vars[channel]}   (${i})
        </#if>
    </#if>
</#list>
typedef uint32_t GPIO_PORT;

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
                <#lt>#define    GPIO_PIN_R${.vars[channel]}${pin}   (${pin+(16*i)})
            </#list>
        </#if>
    </#if>
</#list>

    /* This element should not be used in any of the GPIO APIs.
       It will be used by other modules or application to denote that none of the GPIO Pin is used */
#define    GPIO_PIN_NONE     (-1)

typedef uint32_t GPIO_PIN;

typedef enum
{
<#list 0..CN_PIN_TOTAL-1 as i>
  CN${i}_PIN = 1 << ${i},
</#list>
}CN_PIN;

<#if SYS_PORT_ATLEAST_ONE_CN_USED == true >
typedef  void (*GPIO_PIN_CALLBACK) ( CN_PIN cnPin, uintptr_t context);
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

<#if SYS_PORT_ATLEAST_ONE_CN_USED == true >
void GPIO_PinInterruptEnable(CN_PIN cnPin);

void GPIO_PinInterruptDisable(CN_PIN cnPin);

// *****************************************************************************
// *****************************************************************************
// Section: Local Data types and Prototypes
// *****************************************************************************
// *****************************************************************************

typedef struct {

    /* CN Pin number */
    CN_PIN                  cnPin;

    /* Corresponding GPIO pin name */
    GPIO_PIN                gpioPin;

    /* previous port pin value, need to be stored to check if it has changed later */
    bool                    prevPinValue;

    /* Callback for event on target pin*/
    GPIO_PIN_CALLBACK       callback;

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
    GPIO_PortWrite((GPIO_PORT)(pin>>4), (uint32_t)(0x1UL) << (pin & 0xFU), (uint32_t)(value) << (pin & 0xFU));
}

static inline bool GPIO_PinRead(GPIO_PIN pin)
{
    return (bool)(((GPIO_PortRead((GPIO_PORT)(pin>>4U))) >> (pin & 0xFU)) & 0x1U);
}

static inline bool GPIO_PinLatchRead(GPIO_PIN pin)
{
    return (bool)((GPIO_PortLatchRead((GPIO_PORT)(pin>>4U)) >> (pin & 0xFU)) & 0x1U);
}

static inline void GPIO_PinToggle(GPIO_PIN pin)
{
    GPIO_PortToggle((GPIO_PORT)(pin>>4U), 0x1UL << (pin & 0xFU));
}

static inline void GPIO_PinSet(GPIO_PIN pin)
{
    GPIO_PortSet((GPIO_PORT)(pin>>4U), 0x1UL << (pin & 0xFU));
}

static inline void GPIO_PinClear(GPIO_PIN pin)
{
    GPIO_PortClear((GPIO_PORT)(pin>>4U), 0x1UL << (pin & 0xFU));
}

static inline void GPIO_PinInputEnable(GPIO_PIN pin)
{
    GPIO_PortInputEnable((GPIO_PORT)(pin>>4U), 0x1UL << (pin & 0xFU));
}

static inline void GPIO_PinOutputEnable(GPIO_PIN pin)
{
    GPIO_PortOutputEnable((GPIO_PORT)(pin>>4U), 0x1UL << (pin & 0xFU));
}

<#if SYS_PORT_ATLEAST_ONE_CN_USED == true >
bool GPIO_PinInterruptCallbackRegister(
    CN_PIN cnPin,
    const GPIO_PIN_CALLBACK callback,
    uintptr_t context
);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_GPIO_H
