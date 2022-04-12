/*******************************************************************************
  GPIO PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_gpio.h

  Summary:
    GPIO PLIB Header File

  Description:
    This file provides an interface to control and interact with GPIO-I/O
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

#ifndef PLIB_GPIO_H
#define PLIB_GPIO_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

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
<#list 1..GPIO_PIN_MAX_INDEX as i>
<#assign functype = "PIN_" + i + "_FUNCTION_TYPE">
<#assign funcname = "PIN_" + i + "_FUNCTION_NAME">
<#assign ctrlRegNum = "PIN_" + i + "_GPIO_CTRL_REG_NUM">
<#assign ctrlRegIndex = "PIN_" + i + "_GPIO_CTRL_REG_INDEX">
<#assign pinName = "GPIO_PIN_NAME_" + i>
<#if .vars[functype]?has_content>
    <#if .vars[funcname]?has_content>
        <#if .vars[ctrlRegNum]?has_content>
            <#if .vars[ctrlRegIndex]?has_content>
                <#if !(.vars[functype]?starts_with("SWITCH_") | .vars[functype]?starts_with("LED_"))>
                    <#lt>/*** Macros for ${.vars[funcname]} pin ***/
                    <#if .vars[functype] == "GPIO">
                        <#lt>#define ${.vars[funcname]}_Set()               (GPIO_REGS->GPIO_CTRL${.vars[ctrlRegNum]}[${.vars[ctrlRegIndex]}] |= GPIO_CTRL0_ALT_GPIO_DATA_Msk)
                        <#lt>#define ${.vars[funcname]}_Clear()             (GPIO_REGS->GPIO_CTRL${.vars[ctrlRegNum]}[${.vars[ctrlRegIndex]}] &= ~GPIO_CTRL0_ALT_GPIO_DATA_Msk)
                        <#lt>#define ${.vars[funcname]}_Toggle()            (GPIO_REGS->GPIO_CTRL${.vars[ctrlRegNum]}[${.vars[ctrlRegIndex]}] ^= GPIO_CTRL0_ALT_GPIO_DATA_Msk)
                        <#lt>#define ${.vars[funcname]}_OutputEnable()      (GPIO_REGS->GPIO_CTRL${.vars[ctrlRegNum]}[${.vars[ctrlRegIndex]}] |= GPIO_CTRL0_GPIO_DIR_Msk)
                        <#lt>#define ${.vars[funcname]}_InputEnable()       (GPIO_REGS->GPIO_CTRL${.vars[ctrlRegNum]}[${.vars[ctrlRegIndex]}] &= ~GPIO_CTRL0_GPIO_DIR_Msk)
                    </#if>
                    <#lt>#define ${.vars[funcname]}_Get()               ((GPIO_REGS->GPIO_CTRL${.vars[ctrlRegNum]}[${.vars[ctrlRegIndex]}] & GPIO_CTRL0_GPIO_INP_Msk)? 1 : 0)
                    <#lt>#define ${.vars[funcname]}_PIN                  ${.vars[pinName]}
                </#if>
            </#if>
        </#if>
    </#if>
</#if>
</#list>

// *****************************************************************************
/* GPIO Pins

  Summary:
    Identifies the available GPIO pins.

  Description:
    This enumeration identifies all the GPIO pins that are available on this
    device.

  Remarks:
    The caller should not use the constant expressions assigned to any of
    the enumeration constants as these may vary between devices.

    GPIO pins shown here are the ones available on the selected device. Not
    all GPIO pins within a GPIO group are implemented. Refer to the device
    specific datasheet for more details.
*/

typedef enum
{
<#list 0..GPIO_PIN_MAX_GPIO_PINS as k>
  <#assign GPIO_PIN_INDEX = "GPIO_PIN_INDEX_" + k>
  <#assign GPIO_PIN_PAD = "GPIO_PIN_PAD_" + k>
      <#if .vars[GPIO_PIN_PAD]?has_content>
          <#if (.vars[GPIO_PIN_PAD] != "None")>
              <#lt>    /* ${.vars[GPIO_PIN_PAD]} pin */
              <#lt>    GPIO_PIN_${.vars[GPIO_PIN_PAD]} = ${.vars[GPIO_PIN_INDEX]}U,
          </#if>
      </#if>
</#list>

/* This element should not be used in any of the GPIO APIs.
 * It will be used by other modules or application to denote that none of
 * the GPIO Pin is used */
<#lt>    GPIO_PIN_NONE = 65535U,

} GPIO_PIN;

typedef enum
{
<#list 0..GPIO_NUM_GROUPS-1 as i>
    GPIO_GROUP_${i} = ${i},
</#list>
} GPIO_GROUP;

typedef enum
{
    GPIO_INP_ENABLE = 0,
    GPIO_INP_DISABLE = GPIO_CTRL0_INP_DIS(0x1U),
}GPIO_INP_READ;

typedef enum
{
    ${GPIO_MUX_FUNC_ENUM_LIST}
}GPIO_FUNCTION;

typedef enum
{
    GPIO_DIR_INPUT = 0,
    GPIO_DIR_OUTPUT = GPIO_CTRL0_GPIO_DIR(0x1U)
}GPIO_DIR;

typedef enum {
    GPIO_ALT_OUT_EN = 0,
    GPIO_ALT_OUT_DIS = GPIO_CTRL0_GPIO_OUT_SEL(0x1U),
} GPIO_ALT_OUT;

typedef enum
{
    GPIO_POLARITY_NON_INVERTED = 0,
    GPIO_POLARITY_INVERTED = GPIO_CTRL0_POL(0x1U),
}GPIO_POLARITY;

typedef enum
{
    GPIO_OUTPUT_BUFFER_TYPE_PUSH_PULL = 0,
    GPIO_OUTPUT_BUFFER_TYPE_OPEN_DRAIN = GPIO_CTRL0_OUT_BUFF_TYPE(0x1U),
}GPIO_OUTPUT_BUFFER_TYPE;

typedef enum
{
    ${GPIO_PU_PD_ENUM_LIST}
}GPIO_PULL_TYPE;

typedef enum
{
    GPIO_SLEW_RATE_SLOW = 0,
    GPIO_SLEW_RATE_FAST = 1
}GPIO_SLEW_RATE;

typedef enum {
    GPIO_DRV_STR_LEVEL0 = GPIO_CTRL2P0_DRIV_STREN_LEVEL0,
    GPIO_DRV_STR_LEVEL1 = GPIO_CTRL2P0_DRIV_STREN_LEVEL1,
    GPIO_DRV_STR_LEVEL2 = GPIO_CTRL2P0_DRIV_STREN_LEVEL2,
    GPIO_DRV_STR_LEVEL3 = GPIO_CTRL2P0_DRIV_STREN_LEVEL3,
} GPIO_DRV;

typedef enum
{
    GPIO_INTDET_TYPE_LOW_LEVEL = 0,
    GPIO_INTDET_TYPE_HIGH_LEVEL = ((uint32_t)0x01U << GPIO_CTRL0_INTR_DET_Pos),
    GPIO_INTDET_TYPE_DISABLED = ((uint32_t)0x04U << GPIO_CTRL0_INTR_DET_Pos),
    GPIO_INTDET_TYPE_RISING_EDGE = ((uint32_t)0x0DU << GPIO_CTRL0_INTR_DET_Pos),
    GPIO_INTDET_TYPE_FALLING_EDGE = ((uint32_t)0x0EU << GPIO_CTRL0_INTR_DET_Pos),
    GPIO_INTDET_TYPE_EITHER_EDGE = ((uint32_t)0x0FU << GPIO_CTRL0_INTR_DET_Pos),
}GPIO_INTDET_TYPE;

typedef enum {
    GPIO_PWR_VTR = 0,
    GPIO_PWR_VCC = GPIO_CTRL0_PWR_GATING(0x1U),
    GPIO_PWR_UNPWRD = GPIO_CTRL0_PWR_GATING(0x2U),
} GPIO_PWRGATE;

typedef enum {
    GPIO_PROP_PU_PD = 0ul,
    GPIO_PROP_PWR_GATE,
    GPIO_PROP_INT_DET,
    GPIO_PROP_OBUFF_TYPE,
    GPIO_PROP_DIR,
    GPIO_PROP_OUT_SRC,
    GPIO_PROP_POLARITY,
    GPIO_PROP_MUX_SEL,
    GPIO_PROP_INP_EN_DIS,
    GPIO_PROP_ALL,
} GPIO_PROPERTY;


<#assign GPIO_ATLEAST_ONE_INTERRUPT_USED = false>

<#list 1..(GPIO_PIN_MAX_INDEX) as i>
<#assign PIN_INTERRUPT_DETECT = "PIN_" + i + "_INTDET">
<#if .vars[PIN_INTERRUPT_DETECT] != "">
<#assign GPIO_ATLEAST_ONE_INTERRUPT_USED = true>
</#if>
</#list>

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true >
typedef  void (*GPIO_PIN_CALLBACK) ( GPIO_PIN pin, uintptr_t context);

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
// Section: Generated API based on pin configurations done in Pin Manager
// *****************************************************************************
// *****************************************************************************

void GPIO_Initialize(void);
void GPIO_PinDirConfig(GPIO_PIN pin, GPIO_DIR dir);
void GPIO_PinInputEnable(GPIO_PIN pin);
void GPIO_PinInputDisable(GPIO_PIN pin);
void GPIO_PinInputConfig(GPIO_PIN pin, GPIO_INP_READ inpEn);
void GPIO_PinGroupOutputEnable(GPIO_PIN pin);
void GPIO_PinGroupOutputDisable(GPIO_PIN pin);
void GPIO_PinGroupOutputConfig(GPIO_PIN pin, GPIO_ALT_OUT altOutputEn);
void GPIO_PinSet(GPIO_PIN pin);
void GPIO_PinClear(GPIO_PIN pin);
void GPIO_PinToggle(GPIO_PIN pin);
uint8_t GPIO_PinRead(GPIO_PIN pin);
void GPIO_GroupSet(GPIO_GROUP group, uint32_t mask);
void GPIO_GroupClear(GPIO_GROUP group, uint32_t mask);
void GPIO_GroupToggle(GPIO_GROUP group, uint32_t mask);
uint32_t GPIO_GroupRead(GPIO_GROUP group, uint32_t mask);
void GPIO_GroupPinSet(GPIO_PIN pin);
void GPIO_GroupPinClear(GPIO_PIN pin);
void GPIO_GroupPinToggle(GPIO_PIN pin);
uint32_t GPIO_GroupPinRead(GPIO_PIN pin);
void GPIO_PinMUXConfig(GPIO_PIN pin, GPIO_FUNCTION function);
void GPIO_PinPolarityConfig(GPIO_PIN pin, GPIO_POLARITY polarity);
void GPIO_PinOuputBufferTypeConfig(GPIO_PIN pin, GPIO_OUTPUT_BUFFER_TYPE bufferType);
void GPIO_PinPullUpPullDownConfig(GPIO_PIN pin, GPIO_PULL_TYPE pullType);
void GPIO_PinSlewRateConfig(GPIO_PIN pin, GPIO_SLEW_RATE slewRate);
void GPIO_PinIntDetectConfig(GPIO_PIN pin, GPIO_INTDET_TYPE intDet);
void GPIO_PinPwrGateConfig(GPIO_PIN pin, GPIO_PWRGATE pwrGate);
void GPIO_DrvStrConfig(GPIO_PIN pin, GPIO_DRV drvStrn);
void GPIO_PropertySet( GPIO_PIN pin, GPIO_PROPERTY gpioProp, const uint32_t propMask );

<#if GPIO_ATLEAST_ONE_INTERRUPT_USED == true >
bool GPIO_PinInterruptCallbackRegister(
    GPIO_PIN pin,
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
