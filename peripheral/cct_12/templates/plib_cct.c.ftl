/*******************************************************************************
  CCT Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${CCT_INSTANCE_NAME?lower_case}.c

  Summary
    ${CCT_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the CCT peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "device.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${CCT_INSTANCE_NAME?lower_case}.h"
#include "peripheral/ecia/plib_ecia.h"

<#compress>
<#assign cct_ctrl = "CCT_CTRL_ACT_Msk">

<#list 0..(CCT_NUM_CMP_CH-1) as n>
    <#assign CCT_CMP_EN = "CCT_ENABLE_COMPARE_" + n>
    <#if .vars[CCT_CMP_EN]?? && .vars[CCT_CMP_EN] == true>
        <#assign CMPX_EN = " | CCT_CTRL_CMP_EN" + n + "_Msk">
        <#assign cct_ctrl = cct_ctrl + CMPX_EN>
    </#if>
</#list>

<#assign cap_ctrl_0 = "">
<#assign cap_ctrl_1 = "">
<#assign ict_mux_val = "">

<#list 0..(CCT_NUM_CAP_CH-1) as n>
    <#if n <= 3>
        <#assign CCT_CAP_EN = "CCT_ENABLE_CAPTURE_" + n>
        <#if .vars[CCT_CAP_EN] == true>

            <#if cap_ctrl_0 != "">
                <#assign cap_ctrl_0 = cap_ctrl_0 + " | CCT_CAP0_CTRL_CAP_EDGE" + n + "(" + .vars["CCT_PIN_EDGE_" + n] + ")">
            <#else>
                <#assign cap_ctrl_0 = "CCT_CAP0_CTRL_CAP_EDGE" + n + "(" + .vars["CCT_PIN_EDGE_" + n] + ")">
            </#if>

            <#assign CCT_CAP_INP_FLTR_EN = "CCT_INPUT_FLTR_EN_" + n>
            <#if .vars[CCT_CAP_INP_FLTR_EN] == false>
                <#assign cap_ctrl_0 = cap_ctrl_0 + " | CCT_CAP0_CTRL_FILTER_BYP" + n + "(1)">
            <#else>
                <#assign cap_ctrl_0 = cap_ctrl_0 + " | CCT_CAP0_CTRL_FCLK_SEL" + n + "(" + .vars["CCT_INPUT_FLTR_DIV_" + n] + ")">
            </#if>

            <#if ict_mux_val != "">
                <#assign ict_mux_val = ict_mux_val + " | CCT_MUX_SEL_CAP" + n + "(" + .vars["CCT_PIN_CAPTURE_" + n] + ")">
            <#else>
                <#assign ict_mux_val = "CCT_MUX_SEL_CAP" + n + "(" + .vars["CCT_PIN_CAPTURE_" + n] + ")">
            </#if>

        </#if>

    <#else>
        <#assign CCT_CAP_EN = "CCT_ENABLE_CAPTURE_" + n>
        <#if .vars[CCT_CAP_EN] == true>

            <#if cap_ctrl_1 != "">
                <#assign cap_ctrl_1 = cap_ctrl_1 + " | CCT_CAP1_CTRL_CAP_EDGE" + n + "(" + .vars["CCT_PIN_EDGE_" + n] + ")">
            <#else>
                <#assign cap_ctrl_1 = "CCT_CAP1_CTRL_CAP_EDGE" + n + "(" + .vars["CCT_PIN_EDGE_" + n] + ")">
            </#if>

            <#assign CCT_CAP_INP_FLTR_EN = "CCT_INPUT_FLTR_EN_" + n>
            <#if .vars[CCT_CAP_INP_FLTR_EN] == false>
                <#assign cap_ctrl_1 = cap_ctrl_1 + " | CCT_CAP1_CTRL_FILTER_BYP" + n + "(1)">
            <#else>
                <#assign cap_ctrl_1 = cap_ctrl_1 + " | CCT_CAP1_CTRL_FCLK_SEL" + n + "(" + .vars["CCT_INPUT_FLTR_DIV_" + n] + ")">
            </#if>

            <#if ict_mux_val != "">
                <#assign ict_mux_val = ict_mux_val + " | CCT_MUX_SEL_CAP" + n + "(" + .vars["CCT_PIN_CAPTURE_" + n] + ")">
            <#else>
                <#assign ict_mux_val = "CCT_MUX_SEL_CAP" + n + "(" + .vars["CCT_PIN_CAPTURE_" + n] + ")">
            </#if>

        </#if>
    </#if>
</#list>
</#compress>

<#if .vars["CCT_OVF_INTERRUPT_EN"] == true>
static CCT_CALLBACK_OBJ ${CCT_INSTANCE_NAME}_OVF_CallbackObject;
</#if>

<#list 0..(CCT_NUM_CAP_CH-1) as n>
<#if .vars["CCT_ENABLE_CAPTURE_" + n] == true && .vars["CCT_CAP_INTERRUPT_EN_" + n] == true>
static CCT_CALLBACK_OBJ ${CCT_INSTANCE_NAME}_CAP${n}_CallbackObject;
</#if>
</#list>

<#list 0..(CCT_NUM_CMP_CH-1) as n>
<#if .vars["CCT_ENABLE_COMPARE_" + n] == true && .vars["CCT_CMP_INTERRUPT_EN_" + n] == true>
static CCT_CALLBACK_OBJ ${CCT_INSTANCE_NAME}_CMP${n}_CallbackObject;
</#if>
</#list>

void ${CCT_INSTANCE_NAME}_Initialize(void)
{
    CCT_REGS->CCT_CTRL |= CCT_CTRL_FREE_RST_Msk;

    while (CCT_REGS->CCT_CTRL & CCT_CTRL_FREE_RST_Msk);

    CCT_REGS->CCT_CTRL = ${cct_ctrl} | CCT_CTRL_TCLK(${CCT_FRT_CLK_SRC_DIV});

    <#if cap_ctrl_0 != "">
    CCT_REGS->CCT_CAP0_CTRL = ${cap_ctrl_0};
    </#if>

    <#if cap_ctrl_1 != "">
    CCT_REGS->CCT_CAP1_CTRL = ${cap_ctrl_1};
    </#if>

    <#if ict_mux_val != "">
    CCT_REGS->CCT_MUX_SEL = ${ict_mux_val};
    </#if>
    
    <#list 0..(CCT_NUM_CMP_CH-1) as n>
    <#assign CCT_CMP_EN = "CCT_ENABLE_COMPARE_" + n>
    <#if .vars[CCT_CMP_EN]?? && .vars[CCT_CMP_EN] == true>
    <#assign CCT_CMP_VAL = "CCT_COMPARE_VALUE_" + n>
    CCT_REGS->CCT_COMP${n} = ${.vars[CCT_CMP_VAL]};
    
    </#if>
    </#list>
}

/* Brings timer block in running state */
void ${CCT_INSTANCE_NAME}_TimerActivate( void )
{
    CCT_REGS->CCT_CTRL |= CCT_CTRL_ACT_Msk;
}

/* Power down timer block and all clocks are gated */
void ${CCT_INSTANCE_NAME}_TimerDeActivate( void )
{
    CCT_REGS->CCT_CTRL &= ~CCT_CTRL_ACT_Msk;
}

/* Start the FRT counter */
void ${CCT_INSTANCE_NAME}_FreeRunningTimerStart( void )
{
    CCT_REGS->CCT_CTRL |= CCT_CTRL_FREE_EN_Msk;
}

/* Stop but do not reset the FRT counter */
void ${CCT_INSTANCE_NAME}_FreeRunningTimerStop( void )
{
    CCT_REGS->CCT_CTRL &= ~CCT_CTRL_FREE_EN_Msk;
}

/* Stop and reset the FRT counter to 0 */
void ${CCT_INSTANCE_NAME}_FreeRunningTimerReset( void )
{
    CCT_REGS->CCT_CTRL |= CCT_CTRL_FREE_RST_Msk;

    while (CCT_REGS->CCT_CTRL & CCT_CTRL_FREE_RST_Msk);
}

uint32_t ${CCT_INSTANCE_NAME}_FreeRunningTimerGet( void )
{
    return CCT_REGS->CCT_FREE_RUN;
}

void ${CCT_INSTANCE_NAME}_FreeRunningTimerSet( uint32_t count)
{
    /* Save current value of FREE_EN bit before stoping the timer */
    uint32_t cct_ctrl = CCT_REGS->CCT_CTRL & CCT_CTRL_FREE_EN_Msk;

    /* Stop the FRT before updating the count */
    CCT_REGS->CCT_CTRL &= ~CCT_CTRL_FREE_EN_Msk;

    CCT_REGS->CCT_FREE_RUN = count;

    /* Re-start the FRT */
    CCT_REGS->CCT_CTRL |= cct_ctrl;
}

void ${CCT_INSTANCE_NAME}_FreqDivSet( uint32_t div )
{
    CCT_REGS->CCT_CTRL = (CCT_REGS->CCT_CTRL & ~CCT_CTRL_TCLK_Msk) | (div << CCT_CTRL_TCLK_Pos);
}

uint32_t ${CCT_INSTANCE_NAME}_FrequencyGet(void)
{
    uint32_t freq_div = (CCT_REGS->CCT_CTRL & CCT_CTRL_TCLK_Msk) >> CCT_CTRL_TCLK_Pos;
    uint32_t freq = 48000000/(freq_div + 1);
    return freq;
}

<#if .vars["CCT_OVF_INTERRUPT_EN"] == true>
void ${CCT_INSTANCE_NAME}_CounterOverflowCallbackRegister( CCT_CALLBACK callback, uintptr_t context )
{
    ${CCT_INSTANCE_NAME}_OVF_CallbackObject.callback = callback;

    ${CCT_INSTANCE_NAME}_OVF_CallbackObject.context = context;
}
</#if>

<#list 0..(CCT_NUM_CAP_CH-1) as n>
<#if .vars["CCT_ENABLE_CAPTURE_" + n] == true>
<#if .vars["CCT_CAP_INTERRUPT_EN_" + n] == true>
void ${CCT_INSTANCE_NAME}_Capture${n}CallbackRegister( CCT_CALLBACK callback, uintptr_t context )
{
    ${CCT_INSTANCE_NAME}_CAP${n}_CallbackObject.callback = callback;

    ${CCT_INSTANCE_NAME}_CAP${n}_CallbackObject.context = context;
}
</#if>

uint32_t ${CCT_INSTANCE_NAME}_CaptureChannel${n}Get( void )
{
    return CCT_REGS->CCT_CAP${n};
}

</#if>
</#list>

<#list 0..(CCT_NUM_CMP_CH-1) as n>
<#if .vars["CCT_ENABLE_COMPARE_" + n] == true>
<#if .vars["CCT_CMP_INTERRUPT_EN_" + n] == true>
void ${CCT_INSTANCE_NAME}_Compare${n}CallbackRegister( CCT_CALLBACK callback, uintptr_t context )
{
    ${CCT_INSTANCE_NAME}_CMP${n}_CallbackObject.callback = callback;

    ${CCT_INSTANCE_NAME}_CMP${n}_CallbackObject.context = context;
}
</#if>

uint32_t ${CCT_INSTANCE_NAME}_CompareChannel${n}PeriodGet( void )
{
    return CCT_REGS->CCT_COMP${n};
}

void ${CCT_INSTANCE_NAME}_CompareChannel${n}PeriodSet( uint32_t period )
{
    CCT_REGS->CCT_COMP${n} = period;
}

void ${CCT_INSTANCE_NAME}_CompareChannel${n}Enable( void )
{
    CCT_REGS->CCT_CTRL |= CCT_CTRL_CMP_EN${n}_Msk;
}

void ${CCT_INSTANCE_NAME}_CompareChannel${n}Disable( void )
{
    CCT_REGS->CCT_CTRL &= ~CCT_CTRL_CMP_EN${n}_Msk;
}

void ${CCT_INSTANCE_NAME}_CompareChannel${n}OutputSet( void )
{
    CCT_REGS->CCT_CTRL = (CCT_REGS->CCT_CTRL & ~(CCT_CTRL_CMP_CLR${n}_Msk)) | CCT_CTRL_CMP_SET${n}_Msk;
}

void ${CCT_INSTANCE_NAME}_CompareChannel${n}OutputClear( void )
{
    CCT_REGS->CCT_CTRL = (CCT_REGS->CCT_CTRL & ~(CCT_CTRL_CMP_SET${n}_Msk)) | CCT_CTRL_CMP_CLR${n}_Msk;
}

void ${CCT_INSTANCE_NAME}_CompareChannel${n}InterruptEnable( void )
{
    <#if .vars["CCT_INTERRUPT_TYPE"] == "AGGREGATE">
    ECIA_GIRQSourceEnable(ECIA_AGG_INT_SRC_CCT_CMP${n});
    <#else>
    ECIA_GIRQSourceEnable(ECIA_DIR_INT_SRC_CCT_CMP${n});
    </#if>        
}

void ${CCT_INSTANCE_NAME}_CompareChannel${n}InterruptDisable( void )
{
    <#if .vars["CCT_INTERRUPT_TYPE"] == "AGGREGATE">
    ECIA_GIRQSourceEnable(ECIA_AGG_INT_SRC_CCT_CMP${n});
    <#else>
    ECIA_GIRQSourceEnable(ECIA_DIR_INT_SRC_CCT_CMP${n});
    </#if>        
}

</#if>
</#list>

<#compress>
<#assign INT_HANDLER_NAME_PREFIX = "">

<#if .vars["CCT_INTERRUPT_TYPE"] == "AGGREGATE">
<#assign INT_HANDLER_NAME_PREFIX = "_GRP">
</#if>
</#compress>

<#if .vars["CCT_OVF_INTERRUPT_EN"] == true>
void CCT${INT_HANDLER_NAME_PREFIX}_InterruptHandler(void)
{
    <#if .vars["CCT_INTERRUPT_TYPE"] == "AGGREGATE">
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_CCT))
    <#else>
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_CCT))
    </#if>
    {
        <#if .vars["CCT_INTERRUPT_TYPE"] == "AGGREGATE">
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_CCT);
        <#else>
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_CCT);
        </#if>
        
        if (${CCT_INSTANCE_NAME}_OVF_CallbackObject.callback != NULL)
        {
            ${CCT_INSTANCE_NAME}_OVF_CallbackObject.callback(${CCT_INSTANCE_NAME}_OVF_CallbackObject.context);
        }
    }
}
</#if>

<#list 0..(CCT_NUM_CAP_CH-1) as n>
<#if .vars["CCT_ENABLE_CAPTURE_" + n] == true && .vars["CCT_CAP_INTERRUPT_EN_" + n] == true>
void CCT_CAP${n}${INT_HANDLER_NAME_PREFIX}_InterruptHandler(void)
{
    <#if .vars["CCT_INTERRUPT_TYPE"] == "AGGREGATE">
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_CCT_CAP${n}))
    <#else>
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_CCT_CAP${n}))
    </#if>
    {
        <#if .vars["CCT_INTERRUPT_TYPE"] == "AGGREGATE">
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_CCT_CAP${n});
        <#else>
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_CCT_CAP${n});
        </#if>
        
        if (${CCT_INSTANCE_NAME}_CAP${n}_CallbackObject.callback != NULL)
        {
            ${CCT_INSTANCE_NAME}_CAP${n}_CallbackObject.callback(${CCT_INSTANCE_NAME}_CAP${n}_CallbackObject.context);
        }
    }
}
</#if>
</#list>

<#list 0..(CCT_NUM_CMP_CH-1) as n>
<#if .vars["CCT_ENABLE_COMPARE_" + n] == true && .vars["CCT_CMP_INTERRUPT_EN_" + n] == true>
void CCT_CMP${n}${INT_HANDLER_NAME_PREFIX}_InterruptHandler(void)
{
    <#if .vars["CCT_INTERRUPT_TYPE"] == "AGGREGATE">
    if (ECIA_GIRQResultGet(ECIA_AGG_INT_SRC_CCT_CMP${n}))
    <#else>
    if (ECIA_GIRQResultGet(ECIA_DIR_INT_SRC_CCT_CMP${n}))
    </#if>
    {
        <#if .vars["CCT_INTERRUPT_TYPE"] == "AGGREGATE">
        ECIA_GIRQSourceClear(ECIA_AGG_INT_SRC_CCT_CMP${n});
        <#else>
        ECIA_GIRQSourceClear(ECIA_DIR_INT_SRC_CCT_CMP${n});
        </#if>
        
        if (${CCT_INSTANCE_NAME}_CMP${n}_CallbackObject.callback != NULL)
        {
            ${CCT_INSTANCE_NAME}_CMP${n}_CallbackObject.callback(${CCT_INSTANCE_NAME}_CMP${n}_CallbackObject.context);
        }
    }
}
</#if>
</#list>