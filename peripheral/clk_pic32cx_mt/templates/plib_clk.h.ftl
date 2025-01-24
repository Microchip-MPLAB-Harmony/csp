/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_CLK_H
#define PLIB_CLK_H

#include <stddef.h>
#include <stdbool.h>
#include "device.h"

#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif

// *****************************************************************************
// *****************************************************************************
// Section: CLK Module System Interface Routines
// *****************************************************************************
// *****************************************************************************
<#compress>
<#assign PCK_USED = false>
<#list 0..CLK_NUM_PCKS-1 as i>
<#if .vars["CLK_SCER_PCK"+i]>
<#assign PCK_USED = true>
</#if>
</#list>
</#compress>

typedef uint32_t ID_PERIPH;

<#if PCK_USED>
typedef enum
{
    ${PCK_CLK_SRC_ENUM}
}PCK_CLK_SRC;
</#if>

typedef enum
{
    ${GCLK_SRC_ENUM}
}GCLK_SRC;

<#if CPU_CORE_ID == 0>
typedef enum
{
    PLLA = 0U,
    PLLB,
    PLLC
}PLL_ID;

typedef enum
{
    ${CPU0_CLK_SRC_ENUM}
}CPU0_CLK_SRC;

<#if CLK_SCER_CPCK??>
typedef enum
{
    ${CPU1_CLK_SRC_ENUM}
}CPU1_CLK_SRC;
</#if>

typedef enum
{
    PLLA_CLK_SRC_TD_SLOW_CLK,
    PLLA_CLK_SRC_MAINCK,
}PLLA_CLK_SRC;

typedef enum
{
    PLLB_CLK_SRC_PLLACK0,
    PLLB_CLK_SRC_MAINCK,
}PLLB_CLK_SRC;

typedef enum
{
    PLLC_CLK_SRC_PLLACK0,
    PLLC_CLK_SRC_MAINCK,
}PLLC_CLK_SRC;

typedef enum
{
    ${CPU0_CLK_PRES_ENUM}
}CPU0_CLK_PRESCALER;

<#if CLK_SCER_CPCK??>
typedef enum
{
    ${CPU1_CLK_PRES_ENUM}
}CPU1_CLK_PRESCALER;
</#if>

<#compress>
<#assign PLL_USED = false>
<#assign PLL_LIST = ["PLLA", "PLLB", "PLLC"]>
<#list PLL_LIST as PLL_NAME>
    <#assign ENPLL = .vars["CLK_" + PLL_NAME + "_ENPLL"]>
    <#if ENPLL>
        <#assign PLL_USED = true>
    </#if>
</#list>
</#compress>

void CLK_TDSCLKSelectXTAL(void);

void CLK_EnableMainRCOscillator(void);

void CLK_DisableMainRCOscillator(void);

void CLK_EnableMainXTALOscillator(void);

void CLK_DisableMainXTALOscillator(void);

void CLK_MainOscillatorSelectXTAL(void);

void CLK_MainOscillatorSelectRC(void);

<#if PLL_USED>
void CLK_PLLEnable(PLL_ID pllID);

void CLK_PLLDisable(PLL_ID pllID);

<#if ALLOW_CLK_CONFIG?? &&  ALLOW_CLK_CONFIG>
void CLK_PLLConfig(PLL_ID pllID, uint8_t clkSrc, uint32_t mul, uint32_t fracr, uint8_t output0Div, uint8_t output1Div);
</#if>
</#if>

<#if ALLOW_CLK_CONFIG?? &&  ALLOW_CLK_CONFIG>
void CLK_Core0ClkConfig(CPU0_CLK_SRC clkSrc, CPU0_CLK_PRESCALER prescaler, bool mck0DivBy2, bool mck0Div2By2);
</#if>

void CLK_Core1BusMasterClkEnable(void);

void CLK_Core1BusMasterClkDisable(void);

<#if CLK_SCER_CPCK??>
<#if ALLOW_CLK_CONFIG?? &&  ALLOW_CLK_CONFIG>
void CLK_Core1ClkConfig(CPU1_CLK_SRC clkSrc, CPU1_CLK_PRESCALER prescaler, bool mck1DivBy2 );
</#if>

void CLK_Core1ProcessorClkEnable(void);

void CLK_Core1ProcessorClkDisable(void);
</#if>
</#if><#-- CPU_CORE_ID -->

<#-- Below listed APIs will be generated in both CPU0 and CPU1 projects -->

<#if PCK_USED>
void CLK_PCKConfig(uint8_t pckID, PCK_CLK_SRC clkSrc, uint8_t prescaler);

void CLK_PCKOutputEnable(uint8_t pckID);

void CLK_PCKOutputDisable(uint8_t pckID);
</#if>

<#if ALLOW_CLK_CONFIG?? &&  ALLOW_CLK_CONFIG>
uint32_t CLK_PeripheralClockConfigGet(ID_PERIPH periphID);

void CLK_PeripheralClockConfigSet(ID_PERIPH periphID, bool periphClkEn, bool gclkEn, GCLK_SRC gclkSrc, uint8_t gclkDiv);
</#if>

// *****************************************************************************
/* Function:
    void CLOCK_Initialize ( void )

  Summary:
    Initializes hardware of the System Clock and Peripheral Clock.

  Description:
    This function initializes the hardware of System Clock and Peripheral Clocks.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    Example 1: Do not alter the configuration bit settings
    CLOCK_Initialize ( );

    </code>

  Remarks:
    None.
*/

void CLOCK_Initialize ( void );

#ifdef __cplusplus
}
#endif

#endif //PLIB_CLK_H