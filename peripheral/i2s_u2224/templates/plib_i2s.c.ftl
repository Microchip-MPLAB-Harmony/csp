/*******************************************************************************
  I2S PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${I2S_INSTANCE_NAME?lower_case}.c

  Summary:
    ${I2S_INSTANCE_NAME} Source File

  Description:
    This file has the implementation of all the interfaces provided for one
    particular instance of the Inter-IC Sound Controller (I2S) peripheral.

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

#include "plib_${I2S_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${I2S_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${I2S_INSTANCE_NAME}_Initialize ( void )
{
    // enable CLK_I2S_APB clock so we can write to I2S registers
    MCLK_REGS->MCLK_APBDMASK |= MCLK_APBDMASK_I2S_Msk;

    // configure clock unit 0
    ${I2S_INSTANCE_NAME}_REGS->I2S_CLKCTRL[0] =
<#if I2S_CLKCTRL_0_MCKOUTDIV != 0>
                                            I2S_CLKCTRL_MCKOUTDIV(${I2S_CLKCTRL_0_MCKOUTDIV}-1) |
</#if>
<#if I2S_CLKCTRL_0_MCKDIV != 0>
                                            I2S_CLKCTRL_MCKDIV(${I2S_CLKCTRL_0_MCKDIV}-1) |
</#if>
                                            I2S_CLKCTRL_MCKEN(1-${I2S_CLKCTRL_0_CLKMODE}) |
                                            I2S_CLKCTRL_MCKSEL(${I2S_CLKCTRL_0_CLKMODE}) |
                                            I2S_CLKCTRL_SCKSEL(${I2S_CLKCTRL_0_CLKMODE}) |
                                            I2S_CLKCTRL_FSOUTINV(${I2S_CLKCTRL_0_FSOUTINV}) |
                                            I2S_CLKCTRL_FSINV(${I2S_CLKCTRL_0_FSINV}) |
                                            I2S_CLKCTRL_FSSEL(${I2S_CLKCTRL_0_CLKMODE}) |
                                            I2S_CLKCTRL_BITDELAY(${I2S_CLKCTRL_0_BITDELAY}) |
                                            I2S_CLKCTRL_NBSLOTS(1) |        // always 2 slots for I2S
                                            I2S_CLKCTRL_SLOTSIZE(${I2S_CLKCTRL_0_SLOTSIZE});

<#if I2S_NUM_GENERIC_CLOCKS == 2>
    // configure clock unit 1
    ${I2S_INSTANCE_NAME}_REGS->I2S_CLKCTRL[1] =
<#if I2S_CLKCTRL_1_MCKOUTDIV != 0>
                                            I2S_CLKCTRL_MCKOUTDIV(${I2S_CLKCTRL_1_MCKOUTDIV}-1) |
</#if>
<#if I2S_CLKCTRL_1_MCKDIV != 0>
                                            I2S_CLKCTRL_MCKDIV(${I2S_CLKCTRL_1_MCKDIV}-1) |
</#if>
                                            I2S_CLKCTRL_MCKEN(1-${I2S_CLKCTRL_1_CLKMODE}) |
                                            I2S_CLKCTRL_MCKSEL(${I2S_CLKCTRL_1_CLKMODE}) |
                                            I2S_CLKCTRL_SCKSEL(${I2S_CLKCTRL_1_CLKMODE}) |
                                            I2S_CLKCTRL_FSOUTINV(${I2S_CLKCTRL_1_FSOUTINV}) |
                                            I2S_CLKCTRL_FSINV(${I2S_CLKCTRL_1_FSINV}) |
                                            I2S_CLKCTRL_FSSEL(${I2S_CLKCTRL_1_CLKMODE}) |
                                            I2S_CLKCTRL_BITDELAY(${I2S_CLKCTRL_1_BITDELAY}) |
                                            I2S_CLKCTRL_NBSLOTS(1) |        // always 2 slots for I2S
                                            I2S_CLKCTRL_SLOTSIZE(${I2S_CLKCTRL_1_SLOTSIZE});
</#if>

    // configure TX serializer
    ${I2S_INSTANCE_NAME}_REGS->I2S_TXCTRL = I2S_TXCTRL_MONO(${I2S_TXCTRL_MONO}) |
                                            I2S_TXCTRL_WORDADJ(${I2S_TXCTRL_WORDADJ}) |
                                            I2S_TXCTRL_DATASIZE(${I2S_TXCTRL_DATASIZE}) |
                                            I2S_TXCTRL_SLOTADJ(${I2S_TXCTRL_SLOTADJ}) |
                                            I2S_TXCTRL_CLKSEL(${I2S_TXCTRL_CLKSEL}) |
                                            I2S_TXCTRL_SERMODE(I2S_TXCTRL_SERMODE_TX_Val);

    // configure RX serializer
    ${I2S_INSTANCE_NAME}_REGS->I2S_RXCTRL = I2S_RXCTRL_MONO(${I2S_RXCTRL_MONO}) |
                                            I2S_RXCTRL_WORDADJ(${I2S_RXCTRL_WORDADJ}) |
                                            I2S_RXCTRL_DATASIZE(${I2S_RXCTRL_DATASIZE}) |
                                            I2S_RXCTRL_SLOTADJ(${I2S_RXCTRL_SLOTADJ}) |
                                            I2S_RXCTRL_CLKSEL(${I2S_RXCTRL_CLKSEL}) |
                                            I2S_RXCTRL_SERMODE(I2S_RXCTRL_SERMODE_RX_Val);

    // enable the desired components
    ${I2S_INSTANCE_NAME}_REGS->I2S_CTRLA =  I2S_CTRLA_RXEN(${I2S_RX_SERIALIZER_ENABLE?then('1', '0')}) |
                                            I2S_CTRLA_TXEN(${I2S_TX_SERIALIZER_ENABLE?then('1', '0')}) |
                                            I2S_CTRLA_CKEN0(${I2S_CLKCTRL_0_ENABLE?then('1', '0')})
<#if I2S_NUM_GENERIC_CLOCKS == 2>
                                          | I2S_CTRLA_CKEN1(${I2S_CLKCTRL_1_ENABLE?then('1', '0')})
</#if>   
    // and the I2S module
                                          | I2S_CTRLA_ENABLE_Msk;
}

<#if I2S_LRCLK_INVERT== "1">
uint32_t ${I2S_INSTANCE_NAME}_LRCLK_Get(void)
{
    // for inverted (e.g. left-justified format), will sync on high to low transition
    volatile uint32_t ret = 1-${I2S_LRCLK_PIN_DEFINE};
    return ret;    
}
<#else>
uint32_t ${I2S_INSTANCE_NAME}_LRCLK_Get(void)
{
    // for I2S format, will sync on low to high transition
    volatile uint32_t ret = ${I2S_LRCLK_PIN_DEFINE};
    return ret;    
}
</#if>


