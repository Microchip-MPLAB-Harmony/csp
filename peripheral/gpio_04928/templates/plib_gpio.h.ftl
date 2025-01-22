/**
 * General Purpose Input Output(GPIO) PLIB Header
 * 
 * @file       plib_gpio.h
 * 
 * @defgroup   GPIO driver General Purpose input Output Driver
 * 
 * @brief     dsPIC33A GPIO Module PLIB Header File
*/

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
                                <#lt>#define ${.vars[funcname]}_Set()               (LAT${.vars[pinChannel]} = (1<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_Clear()             (LAT${.vars[pinChannel]} = (0<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_Toggle()            (LAT${.vars[pinChannel]} ^= (1<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_OutputEnable()      (TRIS${.vars[pinChannel]} = (0<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_InputEnable()       (TRIS${.vars[pinChannel]} = (1<<${.vars[pinPort]}))
                            </#if>
                            <#lt>#define ${.vars[funcname]}_Get()               ((PORT${.vars[pinChannel]} >> ${.vars[pinPort]}) & 0x1)
                            <#lt>#define ${.vars[funcname]}_PIN                 GPIO_PIN_R${.vars[pinChannel]}${.vars[pinPort]}
                            <#if .vars[interruptType]?has_content>
                                <#lt>#define ${.vars[funcname]}_InterruptEnable()   (CNEN0${.vars[pinChannel]} = (1<<${.vars[pinPort]}))
                                <#lt>#define ${.vars[funcname]}_InterruptDisable()  (CNEN0${.vars[pinChannel]} = (0<<${.vars[pinPort]}))
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
 * @ingroup  GPIO driver
 * @brief    GPIO Port Definition
 * This identifies and defines the available GPIO Ports.
 */
typedef uint32_t GPIO_PORT;

/**
 @ingroup  GPIO driver
 @enum     GPIO_INTERRUPT_STYLES
 @brief    This enumeration identifies the different interrupt styles that can be configured on the pins
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
 * @ingroup  gpio
 * @brief    GPIO Pins Definition. Identifies and defines the available GPIO Port Pins
 */
typedef uint32_t GPIO_PIN;

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true >
typedef  void (*GPIO_PIN_CALLBACK) (GPIO_PIN pin, uintptr_t context);
</#if>

/**
 * @ingroup  gpio
 * @brief    This function initializes the GPIO library and all ports and pins configured in the MHC Pin Manager.
 * @param    none
 * @return   none  
 */
void GPIO_Initialize(void);

// Section: GPIO Functions which operates on multiple pins of a port

/**
 * @ingroup    gpio
 * @brief      This function reads to the PORT register of the corresponding port.
 * @pre        none
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @return     Corresponding PORT register value 
 */
uint32_t GPIO_PortRead(GPIO_PORT port);

/**
 * @ingroup    gpio
 * @brief      This function writes to the LAT register of the corresponding port and mask with the given value.
 * @pre        Selected pins of the port should be made output before writing.
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be written.
 * @param[in]  value- Desired value to be written on the register
 * @return     none  
 */
void GPIO_PortWrite(GPIO_PORT port, uint32_t mask, uint32_t value);

/**
 * @ingroup    gpio
 * @brief      This function reads to the LAT register of the corresponding port.
 * @pre        none
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @return     LAT register value 
 */
uint32_t GPIO_PortLatchRead (GPIO_PORT port );

/**
 * @ingroup    gpio
 * @brief      This function sets the LAT register of the corresponding port and mask.
 * @pre        Selected pins of the port should be made output before setting.
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be written.
 * @return     none  
 */
void GPIO_PortSet(GPIO_PORT port, uint32_t mask);

/**
 * @ingroup    gpio
 * @brief      This function clears the LAT register of the corresponding port and mask.
 * @pre        Selected pins of the port should be made output before clearing.
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be written.
 * @return     none  
 */
void GPIO_PortClear(GPIO_PORT port, uint32_t mask);

/**
 * @ingroup    gpio
 * @brief      This function inverts the LAT register of the corresponding port and mask.
 * @pre        Selected pins of the port should be made output before toggling.
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be written.
 * @return     none  
 */
void GPIO_PortToggle(GPIO_PORT port, uint32_t mask);

/**
 * @ingroup    gpio
 * @brief      This function sets the TRIS register of the corresponding port and mask. This is to set the direction of the pins as input.
 * @pre        none
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be written.
 * @return     none  
 */
void GPIO_PortInputEnable(GPIO_PORT port, uint32_t mask);

/**
 * @ingroup    gpio
 * @brief      This function clears the TRIS register of the corresponding port and mask. This is to set the direction of the pins as output.
 * @pre        none
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be written.
 * @return     none  
 */
void GPIO_PortOutputEnable(GPIO_PORT port, uint32_t mask);

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true>

/**
 * @ingroup    gpio
 * @brief      This function sets the CNEN0 register of the corresponding port and mask. This is to be able to receive interrupts.
 * @pre        Selected pins of the port should be made input before enabling interrupts.
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be written.
 * @return     none  
 */
void GPIO_PortInterruptEnable(GPIO_PORT port, uint32_t mask);

/**
 * @ingroup    gpio
 * @brief      This function clear the CNEN0 register of the corresponding port and mask. This is to disable receiving interrupts.
 * @pre        Selected pins of the port should be made input before disabling interrupts.
 * @param[in]  port- One of the possible values from GPIO_PORT
 * @param[in]  mask- A 32 bit value in which positions of 0s and 1s decide which IO pins of the selected port will be written.
 * @return     none  
 */
void GPIO_PortInterruptDisable(GPIO_PORT port, uint32_t mask);

// Section: Local Data types and Prototypes

/**
 @ingroup  gpio
 @struct   GPIO_PIN_CALLBACK_OBJ
 @brief    This structure holds the callback and context information for handling
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
 * @ingroup    gpio
 * @brief      This function writes to the selected bit of the corresponding port. 
 * @pre        Pin must be made output before writing to it.
 * @param[in]  pin- Any possible value from GPIO_PIN
 * @param[in]  value- Desired value to be written on the pin. 0 or 1 
 * @return     none  
 */
static inline void GPIO_PinWrite(GPIO_PIN pin, bool value)
{
    GPIO_PortWrite((GPIO_PORT)(pin>>4), (uint32_t)(0x1) << (pin & 0xFU), value);
}

/**
 * @ingroup    gpio
 * @brief      Reads the selected pin value.
 * @pre        none
 * @param[in]  pin- Any possible value from GPIO_PIN
 * @param[in]  value- Desired value to be written on the pin. 0 or 1 
 * @return     True- Pin state is HIGH level(1)
 *             False- Pin state is LOW level(0) 
 */
static inline bool GPIO_PinRead(GPIO_PIN pin)
{
    return (((GPIO_PortRead((GPIO_PORT)(pin>>4))) >> (pin & 0xFU)) & 0x1U);
}

/**
 * @ingroup    gpio
 * @brief      Reads the latched value on the selected pin.
 * @pre        none
 * @param[in]  pin- Any possible value from GPIO_PIN
 * @param[in]  value- Desired value to be written on the pin. 0 or 1 
 * @return     True- Pin state is HIGH level(1)
 *             False- Pin state is LOW level(0) 
 */
static inline bool GPIO_PinLatchRead(GPIO_PIN pin)
{
    return ((GPIO_PortLatchRead((GPIO_PORT)(pin>>4)) >> (pin & 0xFU)) & 0x1U);
}

/**
 * @ingroup    gpio
 * @brief      This function inverts the LAT register bit corresponding to the selected pin.
 * @pre        Pin must be made output before toggling.
 * @param[in]  pin- One of the possible values from GPIO_PIN
 * @return     none  
 */
static inline void GPIO_PinToggle(GPIO_PIN pin)
{
    GPIO_PortToggle((GPIO_PORT)(pin>>4), 0x1UL << (pin & 0xFU));
}

/**
 * @ingroup    gpio
 * @brief      This function sets the LAT register bit corresponding to the selected pin.
 * @pre        Pin must be made output before setting.
 * @param[in]  pin- One of the possible values from GPIO_PIN
 * @return     none  
 */
static inline void GPIO_PinSet(GPIO_PIN pin)
{
    GPIO_PortSet((GPIO_PORT)(pin>>4), 0x1UL << (pin & 0xFU));
}

/**
 * @ingroup    gpio
 * @brief      This function clears the LAT register bit corresponding to the selected pin.
 * @pre        Pin must be made output before clearing.
 * @param[in]  pin- One of the possible values from GPIO_PIN
 * @return     none  
 */
static inline void GPIO_PinClear(GPIO_PIN pin)
{
    GPIO_PortClear((GPIO_PORT)(pin>>4), 0x1UL << (pin & 0xFU));
}

/**
 * @ingroup    gpio
 * @brief      This function sets the TRIS register bit corresponding to the selected pin.
 * @pre        none
 * @param[in]  pin- One of the possible values from GPIO_PIN
 * @return     none  
 */
static inline void GPIO_PinInputEnable(GPIO_PIN pin)
{
    GPIO_PortInputEnable((GPIO_PORT)(pin>>4), 0x1UL << (pin & 0xFU));
}

/**
 * @ingroup    gpio
 * @brief      This function clears the TRIS register bit corresponding to the selected pin.
 * @pre        none
 * @param[in]  pin- One of the possible values from GPIO_PIN
 * @return     none  
 */
static inline void GPIO_PinOutputEnable(GPIO_PIN pin)
{
    GPIO_PortOutputEnable((GPIO_PORT)(pin>>4), 0x1UL << (pin & 0xFU));
}

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true >

#define GPIO_PinInterruptEnable(pin)       GPIO_PinIntEnable(pin,GPIO_INTERRUPT_ON_MISMATCH)
#define GPIO_PinInterruptDisable(pin)      GPIO_PinIntDisable(pin)

/**
 * @ingroup    gpio
 * @brief      This function sets the CNEN0 and CNEN1 register bits corresponding to the selected pin and the selected interrupt style.
 * @pre        Pin must be set as input before enabling interrupt.
 * @param[in]  pin- One of the possible values from GPIO_PIN
 * @param[in]  style- One of the possible values from GPIO_INTERRUPT_STYLE
 * @return     none  
 */
void GPIO_PinIntEnable(GPIO_PIN pin,GPIO_INTERRUPT_STYLE style);

/**
 * @ingroup    gpio
 * @brief      This function clears the CNEN0 and CNEN1 register bits corresponding to the selected pin.
 * @pre        Pin must be set as input before disabling interrupt.
 * @param[in]  pin- One of the possible values from GPIO_PIN
 * @return     none  
 */
void GPIO_PinIntDisable(GPIO_PIN pin);

/**
 * @ingroup    gpio
 * @brief      This function allows application to register an event handling 
 *             function for the PLIB to call back when interrupt occurs 
 *             on the selected pin. At any point if application wants to stop the callback, 
 *             it can call this function with "callback" value as NULL.
 * @param[in]  pin - One of the pins from GPIO_PIN
 * @param[in]  callback  - Pointer to the event handler function implemented by the user
 * @param[in]  context   - The value of parameter will be passed back to the 
 *                         application unchanged, when the eventHandler function is called. 
 *                         It can be used to identify any application specific value.
 * @return     Callback registration status: true  - Callback was successfully registered
 *                                           false - Callback was not registered
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
