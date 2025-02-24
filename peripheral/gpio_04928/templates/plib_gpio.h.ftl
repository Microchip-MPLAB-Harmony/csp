/*******************************************************************************
  GPIO PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_gpio.h
 
  Summary:
    gpio PLIB Header File
 
  Description:
    This file has prototype of all the interfaces provided for particular
    gpio peripheral.
 
*******************************************************************************/
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

// Section: Data types and constants

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
                                <#lt>#define ${.vars[funcname]}_Set()               (_LAT${.vars[pinChannel]}${.vars[pinPort]} = 1U)
                                <#lt>#define ${.vars[funcname]}_Clear()             (_LAT${.vars[pinChannel]}${.vars[pinPort]} = 0U)
                                <#lt>#define ${.vars[funcname]}_Toggle()            (_LAT${.vars[pinChannel]}${.vars[pinPort]} ^= 1U)
                                <#lt>#define ${.vars[funcname]}_OutputEnable()      (_TRIS${.vars[pinChannel]}${.vars[pinPort]} = 0U)
                                <#lt>#define ${.vars[funcname]}_InputEnable()       (_TRIS${.vars[pinChannel]}${.vars[pinPort]} = 1U)
                            </#if>
                            <#lt>#define ${.vars[funcname]}_Get()               ((PORT${.vars[pinChannel]} >> ${.vars[pinPort]}) & 0x1)
                            <#lt>#define ${.vars[funcname]}_PIN                 GPIO_PIN_R${.vars[pinChannel]}${.vars[pinPort]}
                            <#if .vars[interruptType]?has_content>
                                <#lt>#define ${.vars[funcname]}_InterruptEnable()   (_CNEN0${.vars[pinChannel]}${.vars[pinPort]} = 1U)
                                <#lt>#define ${.vars[funcname]}_InterruptDisable()  (_CNEN0${.vars[pinChannel]}${.vars[pinPort]} = 0U)
                            </#if>
                        </#if>
                    </#if>
                </#if>
            </#if>
        </#if>
    </#list>  
    
<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#if (.vars["PORT${.vars[channel]}_Pin_List"])?has_content>
                <#lt>#define   GPIO_PORT_${.vars[channel]} (${i}U)
        </#if>
    </#if>
</#list>

/**
 * @brief    GPIO Port Definition
 * This identifies and defines the available GPIO Ports.
 */
typedef uint32_t GPIO_PORT;

/**
* @enum     GPIO_INTERRUPT_STYLES
* @brief    This enumeration identifies the different interrupt styles that can be configured on the pins
*/
typedef enum
{
   GPIO_INTERRUPT_ON_MISMATCH,
   GPIO_INTERRUPT_ON_POSITIVE_EDGE,
   GPIO_INTERRUPT_ON_NEGATIVE_EDGE,
   GPIO_INTERRUPT_ON_ANY_EDGES,
}GPIO_INTERRUPT_STYLE;

<#list 0..GPIO_CHANNEL_TOTAL-1 as i>
    <#assign channel = "GPIO_CHANNEL_" + i + "_NAME">
    <#if .vars[channel]?has_content>
        <#if .vars["PORT${.vars[channel]}_Pin_List"]?has_content>
            <@"<#assign PORT${.vars[channel]}_Pin_List =  PORT${.vars[channel]}_Pin_List?sort>"?interpret />
            <#list .vars["PORT${.vars[channel]}_Pin_List"] as pin>
                <#lt>#define   GPIO_PIN_R${.vars[channel]}${pin}  (${pin+(16*i)}U)
            </#list>
        </#if>
    </#if>
</#list>

/**
 * @brief    GPIO Pins Definition. Identifies and defines the available GPIO Port Pins
 */
typedef uint32_t GPIO_PIN;

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true >
typedef  void (*GPIO_PIN_CALLBACK) (GPIO_PIN pin, uintptr_t context);
</#if>

/**
 * @brief    Initializes the GPIO library
 *
 * @details  This function initializes the GPIO library and all its ports and pins configured
 * in the pin settings.
 *
 * @pre      None
 *
 * @param    None
 *
 * @return   None  
 *
 * @remarks  None
 */
void GPIO_Initialize(void);

// Section: GPIO Functions which operates on multiple pins of a port

/**
 * @brief      Reads all the I/O lines of the selected port.
 *
 * @details    This function reads the live data values on all the I/O lines of the selected port.
 * Bit values returned in each position indicate corresponding pin state.
 *
 * @pre        Reading the I/O line levels requires the clock of the GPIO Controller to be enabled,
 * otherwise this API reads the levels present on the I/O line at the time the clock was enabled.
 *
 * @param[in]  port- One of the possible values from GPIO_PORT
 *
 * @return     Corresponding PORT register value 
 *
 * @remarks    None
 */
uint32_t GPIO_PortRead(GPIO_PORT port);

/**
 * @brief      Write the value on the masked I/O lines of the selected port.
 *
 * @details    This function writes the data values driven on selected output lines of the selected port.
 * Bit values in each position indicate corresponding pin levels.
 *
 * @pre        Selected pins of the port should be made output before writing.
 *
 * @param[in]  port- One of the possible values from GPIO_PORT
 *
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which
 * IO pins of the selected port will be written.
 * @param[in]  value- Desired value to be written on the register
 *
 * @return     None  
 *
 * @remarks    None
 */
void GPIO_PortWrite(GPIO_PORT port, uint32_t mask, uint32_t value);

/**
 * @brief      Read the latched value on all the I/O lines of the selected port.
 *
 * @details    This function reads the latched data values on all the I/O lines of the selected port. 
 * Bit values returned in each position indicate corresponding pin levels.
 *
 * @pre        none
 *
 * @param[in]  port- One of the possible values from GPIO_PORT
 *
 * @return     LAT register value 
 *
 * @remarks    None
 */
uint32_t GPIO_PortLatchRead (GPIO_PORT port );

/**
 * @brief      Set the selected IO pins of a port.
 *
 * @details    This function sets (to '1') the selected IO pins of a port.
 *
 * @pre        Selected pins of the port should be made output before setting.
 *
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which
 * IO pins of the selected port will be written.
 *
 * @return     None  
 *
 * @remarks    None
 */
void GPIO_PortSet(GPIO_PORT port, uint32_t mask);

/**
 * @brief      Clear the selected IO pins of a port.
 *
 * @details    This function clears (to '0') the selected IO pins of a port.
 *
 * @pre        Selected pins of the port should be made output before clearing.
 *
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which
 * IO pins of the selected port will be written.
 *
 * @return     None  
 *
 * @remarks    None
 */
void GPIO_PortClear(GPIO_PORT port, uint32_t mask);

/**
 * @brief      Toggles the selected IO pins of a port.
 *
 * @details    This function toggles (or invert) the selected IO pins of a port.
 *
 * @pre        Selected pins of the port should be made output before toggling.
 *
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO
 * pins of the selected port will be written.
 *
 * @return     None  
 *
 * @remarks    None
 */
void GPIO_PortToggle(GPIO_PORT port, uint32_t mask);

/**
 * @brief      Enables selected IO pins of a port as input.
 *
 * @details    This function enables selected IO pins of a port as input.
 *
 * @pre        None
 *
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins
 * of the selected port will be written.
 *
 * @return     None
 *
 * @remarks    None 
 */
void GPIO_PortInputEnable(GPIO_PORT port, uint32_t mask);

/**
 * @brief      Enables selected IO pins of a port as output(s).
 *
 * @details    This function enables selected IO pins of the given port as output(s).
 *
 * @pre        None
 *
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins
 * of the selected port will be written.
 *
 * @return     None  
 *
 * @remarks    None
 */
void GPIO_PortOutputEnable(GPIO_PORT port, uint32_t mask);

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true>

/**
 * @brief      Enables IO interrupt on selected IO pins of a port.
 *
 * @details    This function enables interrupt on selected IO pins of selected port.
 *
 * @pre        Selected pins of the port should be made input before enabling interrupts.
 *
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be written.
 *
 * @return     None  
 *
 * @remarks    None
 */
void GPIO_PortInterruptEnable(GPIO_PORT port, uint32_t mask);

/**
 * @brief      Disables IO interrupt on selected IO pins of a port.
 *
 * @details    This function disables IO interrupt on selected IO pins of selected port.
 *
 * @pre        Selected pins of the port should be made input before disabling interrupts.
 *
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins
 * of the selected port will be written.
 *
 * @return     None  
 *
 * @remarks    None
 */
void GPIO_PortInterruptDisable(GPIO_PORT port, uint32_t mask);

// Section: Local Data types and Prototypes

/**
* @struct   GPIO_PIN_CALLBACK_OBJ
* @brief   This structure holds the callback and context information for handling
           events on a specified GPIO Pin.
*/
typedef struct {

    /* target pin */
   GPIO_PIN                 pin;

    /* Callback for event on target pin*/
   GPIO_PIN_CALLBACK        callback;

    /* Callback Context */
    uintptr_t               context;

}GPIO_PIN_CALLBACK_OBJ;

</#if>

// Section: GPIO Functions which operates on one pin at a time

/**
 * @brief      Writes the logic level of the selected pin.
 *
 * @details    This function writes/drives the "value" on the selected I/O line/pin.
 * 
 * @pre        Pin must be made output before writing to it.
 *
 * @param[in]  pin- Any possible value from GPIO_PIN
 * @param[in]  value- Desired value to be written on the pin. 0 or 1 
 *
 * @return     None  
 * 
 * @remarks    None
 */
static inline void GPIO_PinWrite(GPIO_PIN pin, bool value)
{
    GPIO_PortWrite((GPIO_PORT)(pin>>4), (uint32_t)(0x1) << (pin & 0xFU), (uint32_t)(value) << (pin & 0xFU));
}

/**
 * @brief      Reads the selected pin value.
 * 
 * @details    This function reads the selected pin value.
 * it reads the value regardless of pin configuration, whether uniquely as an input,
 * or driven by the GPIO Controller, or driven by peripheral.
 * @pre        None
 *
 * @param[in]  pin- Any possible value from GPIO_PIN
 * @param[in]  value- Desired value to be written on the pin. 0 or 1 
 *
 * @return     True- Pin state is HIGH level(1)
 *             False- Pin state is LOW level(0) 
 *
 * @remarks    None
 */
static inline bool GPIO_PinRead(GPIO_PIN pin)
{
    return ((((GPIO_PortRead((GPIO_PORT)(pin>>4))) >> (pin & 0xFU)) & 0x1U) != 0U);
}

/**
 * @brief      Reads the latched value on the selected pin.
 *
 * @details    This function reads the data driven on the selected I/O line/pin.
 * Whatever data is written/driven on I/O line by using any of the GPIO PLIB APIs, will be read by this API.
 *
 * @pre        None
 *
 * @param[in]  pin- Any possible value from GPIO_PIN
 * @param[in]  value- Desired value to be written on the pin. 0 or 1 
 *
 * @return     True- Pin state is HIGH level(1)
 *             False- Pin state is LOW level(0) 
 *
 * @remarks    None
 */
static inline bool GPIO_PinLatchRead(GPIO_PIN pin)
{
    return (((GPIO_PortLatchRead((GPIO_PORT)(pin>>4)) >> (pin & 0xFU)) & 0x1U) != 0U);
}

/**
 * @brief      Toggles the selected pin.
 *
 * @details    This function toggles/inverts the value on the selected I/O line/pin.
 *
 * @pre        Pin must be made output before toggling.
 *
 * @param[in]  pin- One of the possible values from GPIO_PIN
 *
 * @return     None  
 *
 * @remarks    None
 */
static inline void GPIO_PinToggle(GPIO_PIN pin)
{
    GPIO_PortToggle((GPIO_PORT)(pin>>4), 0x1UL << (pin & 0xFU));
}

/**
 * @brief      Sets the selected pin.
 *
 * @details    This function drives '1' on the selected I/O line/pin.
 *
 * @pre        Pin must be made output before setting.
 *
 * @param[in]  pin- One of the possible values from GPIO_PIN
 *
 * @return     None  
 *
 * @remarks    None
 */
static inline void GPIO_PinSet(GPIO_PIN pin)
{
    GPIO_PortSet((GPIO_PORT)(pin>>4), 0x1UL << (pin & 0xFU));
}

/**
 * @brief      Clears the selected pin.
 *
 * @details    This function drives '0' on the selected I/O line/pin.
 *
 * @pre        Pin must be made output before clearing.
 *
 * @param[in]  pin- One of the possible values from GPIO_PIN
 *
 * @return     None  
 *
 * @remarks    None
 */
static inline void GPIO_PinClear(GPIO_PIN pin)
{
    GPIO_PortClear((GPIO_PORT)(pin>>4), 0x1UL << (pin & 0xFU));
}

/**
 * @brief      Enables selected IO pin as Digital input.
 *
 * @details    This function enables selected IO pin as Digital input.
 *
 * @pre        None
 *
 * @param[in]  pin- One of the possible values from GPIO_PIN
 *
 * @return     None  
 *
 * @remarks    None
 */
static inline void GPIO_PinInputEnable(GPIO_PIN pin)
{
    GPIO_PortInputEnable((GPIO_PORT)(pin>>4), 0x1UL << (pin & 0xFU));
}

/**
 * @brief      Enables selected IO pin as Digital output.
 *
 * @details    This function enables selected IO pin as Digital output.
 *
 * @pre        None
 *
 * @param[in]  pin- One of the possible values from GPIO_PIN
 *
 * @return     None  
 *
 * @remarks    None
 */
static inline void GPIO_PinOutputEnable(GPIO_PIN pin)
{
    GPIO_PortOutputEnable((GPIO_PORT)(pin>>4), 0x1UL << (pin & 0xFU));
}

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true >

#define GPIO_PinInterruptEnable(pin)       GPIO_PinIntEnable(pin,GPIO_INTERRUPT_ON_MISMATCH)
#define GPIO_PinInterruptDisable(pin)      GPIO_PinIntDisable(pin)

/**
 * @brief      Enables CN interrupt on selected pin.
 *
 * @pre        Pin must be set as input before enabling interrupt.
 *
 * @param[in]  pin- One of the possible values from GPIO_PIN
 * @param[in]  style- One of the possible values from GPIO_INTERRUPT_STYLE
 *
 * @return     None  
 *
 * @remarks    None
 */
void GPIO_PinIntEnable(GPIO_PIN pin,GPIO_INTERRUPT_STYLE style);

/**
 * @brief      Disables CN interrupt on selected pin.
 *
 * @details    This function disables CN interrupt on selected pin.
 *
 * @pre        Pin must be set as input before disabling interrupt.
 *
 * @param[in]  pin- One of the possible values from GPIO_PIN
 *
 * @return     None
 *
 * @remarks    None 
 */
void GPIO_PinIntDisable(GPIO_PIN pin);

/**
 * @brief      Allows application to register callback for every pin.
 *
 * @details    This function allows application to register an event handling 
 *             function for the PLIB to call back when interrupt occurs 
 *             on the selected pin. At any point if application wants to stop the callback, 
 *             it can call this function with "callback" value as NULL.
 *
 * @param[in]  pin - One of the pins from GPIO_PIN
 * @param[in]  callback  - Pointer to the event handler function implemented by the user
 * @param[in]  context   - The value of parameter will be passed back to the 
 *                         application unchanged, when the eventHandler function is called. 
 *                         It can be used to identify any application specific value.
 *
 * @return     Callback registration status: true  - Callback was successfully registered
 *                                           false - Callback was not registered
 *
 * @remarks    None
 */
bool GPIO_PinInterruptCallbackRegister(
    GPIO_PIN pin,
    const  GPIO_PIN_CALLBACK callback,
    uintptr_t context
);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

   }  

#endif
// DOM-IGNORE-END
#endif // PLIB_GPIO_H
