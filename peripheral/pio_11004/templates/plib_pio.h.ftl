/*******************************************************************************
  PIO PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pio.h

  Summary:
    PIO PLIB Header File

  Description:
    This library provides an interface to control and interact with Parallel
    Input/Output controller (PIO) module.

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

#ifndef PLIB_PIO_H
#define PLIB_PIO_H

#include "device.h"
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

<#assign PORTA_Pin_List = []>
<#assign PORTB_Pin_List = []>
<#assign PORTC_Pin_List = []>
<#assign PORTD_Pin_List = []>
<#assign PORTE_Pin_List = []>

<#list 1..PIO_PIN_TOTAL as i>
    <#assign pinport = "PIN_" + i + "_PIO_PIN">
    <#assign pinchannel = "PIN_" + i + "_PIO_CHANNEL">

    <#if .vars[pinport]?has_content>
        <#if .vars[pinchannel]?has_content>
            <#if .vars[pinchannel] == "A">
                <#assign PORTA_Pin_List = PORTA_Pin_List + [.vars[pinport]]>

            <#elseif .vars[pinchannel] == "B">
                <#assign PORTB_Pin_List = PORTB_Pin_List + [.vars[pinport]]>

            <#elseif .vars[pinchannel] == "C">
                <#assign PORTC_Pin_List = PORTC_Pin_List + [.vars[pinport]]>

            <#elseif .vars[pinchannel] == "D">
                <#assign PORTD_Pin_List = PORTD_Pin_List + [.vars[pinport]]>

            <#elseif .vars[pinchannel] == "E">
                <#assign PORTE_Pin_List = PORTE_Pin_List + [.vars[pinport]]>
            </#if>
        </#if>
    </#if>
</#list>

</#compress>
<#-- Generate Pin Macros for all the GPIO Pins -->
    <#assign GPIO_Name_List = []>
    <#assign GPIO_PortPin_List = []>
    <#assign GPIO_PortChannel_List = []>
    <#assign GPIO_Interrupt_List = []>
    <#list 1..PIO_PIN_TOTAL as i>
        <#assign functype = "PIN_" + i + "_FUNCTION_TYPE">
        <#assign funcname = "PIN_" + i + "_FUNCTION_NAME">
        <#assign pinport = "PIN_" + i + "_PIO_PIN">
        <#assign pinchannel = "PIN_" + i + "_PIO_CHANNEL">
        <#assign interruptType = "PIN_" + i + "_PIO_INTERRUPT">
        <#if .vars[functype]?has_content>
            <#if .vars[functype] == "GPIO">
                <#if .vars[funcname]?has_content>
                    <#if .vars[pinport]?has_content>
                        <#if .vars[pinchannel]?has_content>

                            <#lt>/*** Macros for ${.vars[funcname]} pin ***/
                            <#lt>#define ${.vars[funcname]}_Set()               (PIO${.vars[pinchannel]}_REGS->PIO_SODR = (1<<${.vars[pinport]}))
                            <#lt>#define ${.vars[funcname]}_Clear()             (PIO${.vars[pinchannel]}_REGS->PIO_CODR = (1<<${.vars[pinport]}))
                            <#lt>#define ${.vars[funcname]}_Toggle()            (PIO${.vars[pinchannel]}_REGS->PIO_ODSR ^= (1<<${.vars[pinport]}))
                            <#lt>#define ${.vars[funcname]}_Get()               ((PIO${.vars[pinchannel]}_REGS->PIO_PDSR >> ${.vars[pinport]}) & 0x1)
                            <#lt>#define ${.vars[funcname]}_OutputEnable()      (PIO${.vars[pinchannel]}_REGS->PIO_OER = (1<<${.vars[pinport]}))
                            <#lt>#define ${.vars[funcname]}_InputEnable()       (PIO${.vars[pinchannel]}_REGS->PIO_ODR = (1<<${.vars[pinport]}))
                            <#if .vars[interruptType]?has_content>
                                <#lt>#define ${.vars[funcname]}_InterruptEnable()   (PIO${.vars[pinchannel]}_REGS->PIO_IER = (1<<${.vars[pinport]}))
                                <#lt>#define ${.vars[funcname]}_InterruptDisable()  (PIO${.vars[pinchannel]}_REGS->PIO_IDR = (1<<${.vars[pinport]}))
                            </#if>
                            <#lt>#define ${.vars[funcname]}_PIN                  PIO_PIN_P${.vars[pinchannel]}${.vars[pinport]}
                        </#if>
                    </#if>
                </#if>
            </#if>
        </#if>
    </#list>


// *****************************************************************************
/* PIO Port

  Summary:
    Identifies the available PIO Ports.

  Description:
    This enumeration identifies the available PIO Ports.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all ports are available on all devices.  Refer to the specific
    device data sheet to determine which ports are supported.
*/

typedef enum
{
    <#if PORTA_Pin_List?has_content>
    PIO_PORT_A = PIOA_BASE_ADDRESS,
    </#if>
    <#if PORTB_Pin_List?has_content>
    PIO_PORT_B = PIOB_BASE_ADDRESS,
    </#if>
    <#if PORTC_Pin_List?has_content>
    PIO_PORT_C = PIOC_BASE_ADDRESS,
    </#if>
    <#if PORTD_Pin_List?has_content>
    PIO_PORT_D = PIOD_BASE_ADDRESS,
    </#if>
    <#if PORTE_Pin_List?has_content>
    PIO_PORT_E = PIOE_BASE_ADDRESS
    </#if>
} PIO_PORT;

// *****************************************************************************
/* PIO Port Pins

  Summary:
    Identifies the available PIO port pins.

  Description:
    This enumeration identifies the available PIO port pins.

  Remarks:
    The caller should not rely on the specific numbers assigned to any of
    these values as they may change from one processor to the next.

    Not all pins are available on all devices.  Refer to the specific
    device data sheet to determine which pins are supported.
*/

typedef enum
{
    <#assign PORTA_Pin_List =  PORTA_Pin_List?sort>
    <#list PORTA_Pin_List as pin>
    PIO_PIN_PA${pin} = ${pin},
    </#list>
    <#assign PORTB_Pin_List =  PORTB_Pin_List?sort>
    <#list PORTB_Pin_List as pin>
    PIO_PIN_PB${pin} = ${pin+32},
    </#list>
    <#assign PORTC_Pin_List =  PORTC_Pin_List?sort>
    <#list PORTC_Pin_List as pin>
    PIO_PIN_PC${pin} = ${pin+64},
    </#list>
    <#assign PORTD_Pin_List =  PORTD_Pin_List?sort>
    <#list PORTD_Pin_List as pin>
    PIO_PIN_PD${pin} = ${pin+96},
    </#list>
    <#assign PORTE_Pin_List =  PORTE_Pin_List?sort>
    <#list PORTE_Pin_List as pin>
    PIO_PIN_PE${pin} = ${pin+128},
    </#list>

    /* This element should not be used in any of the PIO APIs.
       It will be used by other modules or application to denote that none of the PIO Pin is used */
    PIO_PIN_NONE = -1

} PIO_PIN;

<#if INTERRUPT_ACTIVE >
typedef  void (*PIO_PIN_CALLBACK) ( PIO_PIN pin, uintptr_t context);
</#if>

void PIO_Initialize(void);

// *****************************************************************************
// *****************************************************************************
// Section: PIO Functions which operates on multiple pins of a port
// *****************************************************************************
// *****************************************************************************

uint32_t PIO_PortRead(PIO_PORT port);

void PIO_PortWrite(PIO_PORT port, uint32_t mask, uint32_t value);

uint32_t PIO_PortLatchRead ( PIO_PORT port );

void PIO_PortSet(PIO_PORT port, uint32_t mask);

void PIO_PortClear(PIO_PORT port, uint32_t mask);

void PIO_PortToggle(PIO_PORT port, uint32_t mask);

void PIO_PortInputEnable(PIO_PORT port, uint32_t mask);

void PIO_PortOutputEnable(PIO_PORT port, uint32_t mask);

<#if INTERRUPT_ACTIVE >
void PIO_PortInterruptEnable(PIO_PORT port, uint32_t mask);

void PIO_PortInterruptDisable(PIO_PORT port, uint32_t mask);

// *****************************************************************************
// *****************************************************************************
// Section: Local Data types and Prototypes
// *****************************************************************************
// *****************************************************************************

typedef struct {

    /* target pin */
    PIO_PIN                 pin;

    /* Callback for event on target pin*/
    PIO_PIN_CALLBACK        callback;

    /* Callback Context */
    uintptr_t               context;

} PIO_PIN_CALLBACK_OBJ;

</#if>
// *****************************************************************************
// *****************************************************************************
// Section: PIO Functions which operates on one pin at a time
// *****************************************************************************
// *****************************************************************************

static inline void PIO_PinWrite(PIO_PIN pin, bool value)
{
    PIO_PortWrite((PIO_PORT)(PIOA_BASE_ADDRESS + (0x200 * (pin>>5))), (uint32_t)(0x1) << (pin & 0x1f), (uint32_t)(value) << (pin & 0x1f));
}

static inline bool PIO_PinRead(PIO_PIN pin)
{
    return (bool)((PIO_PortRead((PIO_PORT)(PIOA_BASE_ADDRESS + (0x200 * (pin>>5)))) >> (pin & 0x1F)) & 0x1);
}

static inline bool PIO_PinLatchRead(PIO_PIN pin)
{
    return (bool)((PIO_PortLatchRead((PIO_PORT)(PIOA_BASE_ADDRESS + (0x200 * (pin>>5)))) >> (pin & 0x1F)) & 0x1);
}

static inline void PIO_PinToggle(PIO_PIN pin)
{
    PIO_PortToggle((PIO_PORT)(PIOA_BASE_ADDRESS + (0x200 * (pin>>5))), 0x1 << (pin & 0x1F));
}

static inline void PIO_PinSet(PIO_PIN pin)
{
    PIO_PortSet((PIO_PORT)(PIOA_BASE_ADDRESS + (0x200 * (pin>>5))), 0x1 << (pin & 0x1F));
}

static inline void PIO_PinClear(PIO_PIN pin)
{
    PIO_PortClear((PIO_PORT)(PIOA_BASE_ADDRESS + (0x200 * (pin>>5))), 0x1 << (pin & 0x1F));
}

static inline void PIO_PinInputEnable(PIO_PIN pin)
{
    PIO_PortInputEnable((PIO_PORT)(PIOA_BASE_ADDRESS + (0x200 * (pin>>5))), 0x1 << (pin & 0x1F));
}

static inline void PIO_PinOutputEnable(PIO_PIN pin)
{
    PIO_PortOutputEnable((PIO_PORT)(PIOA_BASE_ADDRESS + (0x200 * (pin>>5))), 0x1 << (pin & 0x1F));
}

<#if INTERRUPT_ACTIVE >
static inline void PIO_PinInterruptEnable(PIO_PIN pin)
{
    PIO_PortInterruptEnable((PIO_PORT)(PIOA_BASE_ADDRESS + (0x200 * (pin>>5))), 0x1 << (pin & 0x1F));
}

static inline void PIO_PinInterruptDisable(PIO_PIN pin)
{
    PIO_PortInterruptDisable((PIO_PORT)(PIOA_BASE_ADDRESS + (0x200 * (pin>>5))), 0x1 << (pin & 0x1F));
}

bool PIO_PinInterruptCallbackRegister(
    PIO_PIN pin,
    const   PIO_PIN_CALLBACK callBack,
    uintptr_t context
);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_PIO_H
