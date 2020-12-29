/*******************************************************************************
  Timer/Counter(${TCC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${TCC_INSTANCE_NAME?lower_case}.c

  Summary
    ${TCC_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the TCC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${TCC_INSTANCE_NAME?lower_case}.h"

<#assign TCC_CTRLBSET_VAL = "">
<#assign TCC_DRVCTRL_VAL = "">
<#assign TCC_EVCTRL_VAL = "">
<#assign TCC_INTENSET_VAL = "">
<#if TCC_COMPARE_CTRLBSET_DIR == "1">
    <#assign TCC_CTRLBSET_VAL = "TCC_CTRLBSET_DIR_Msk">
</#if>
<#if TCC_COMPARE_CTRLBSET_ONESHOT == true>
    <#if TCC_CTRLBSET_VAL != "">
        <#assign TCC_CTRLBSET_VAL = TCC_CTRLBSET_VAL + " | TCC_CTRLBSET_ONESHOT_Msk">
    <#else>
        <#assign TCC_CTRLBSET_VAL = "TCC_CTRLBSET_ONESHOT_Msk">
    </#if>
</#if>
<#if TCC_COMPARE_CTRLBSET_LUPD == false>
    <#if TCC_CTRLBSET_VAL != "">
        <#assign TCC_CTRLBSET_VAL = TCC_CTRLBSET_VAL + " | TCC_CTRLBSET_LUPD_Msk">
    <#else>
        <#assign TCC_CTRLBSET_VAL = "TCC_CTRLBSET_LUPD_Msk">
    </#if>
</#if>

<#-- Invert outputs -->
<#list 0..(TCC_NUM_OUTPUTS-1) as i>
<#assign CH_NUM = i>
<#assign TCC_INVEN = "TCC_COMPARE_DRVCTRL_INVEN" + i>
<#if .vars[TCC_INVEN] == true> 
    <#if TCC_DRVCTRL_VAL != "">
        <#assign TCC_DRVCTRL_VAL = TCC_DRVCTRL_VAL + "\n\t\t | TCC_DRVCTRL_INVEN"+i+"_Msk">
    <#else>
        <#assign TCC_DRVCTRL_VAL = "TCC_DRVCTRL_INVEN" + i + "_Msk">
    </#if>
</#if>    
</#list>

<#if TCC_COMPARE_INTENSET_OVF == true>
    <#assign TCC_INTENSET_VAL = "TCC_INTENSET_OVF_Msk">
</#if>

<#list 0..(TCC_NUM_CHANNELS-1) as i>
<#assign CH_NUM = i>
<#assign TCC_COMP_INTERRUPT = "TCC_COMPARE_INTENSET_MC" + i>
<#if .vars[TCC_COMP_INTERRUPT] == true>
    <#if TCC_INTENSET_VAL != "">
        <#assign TCC_INTENSET_VAL = TCC_INTENSET_VAL + " | TCC_INTENSET_MC"+i+"_Msk">
    <#else>
        <#assign TCC_INTENSET_VAL = "TCC_INTENSET_MC"+i+"_Msk">
    </#if>
</#if>
</#list>

<#if TCC_COMPARE_EVCTRL_OVFEO == true>
    <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_OVFEO_Msk">
</#if>

<#list 0..(TCC_NUM_CHANNELS-1) as i>
<#assign CH_NUM = i>
<#assign TCC_COMP_EVENT = "TCC_COMPARE_EVCTRL_MCEO" + i>
<#if .vars[TCC_COMP_EVENT] == true>
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_MCEO"+i+"_Msk">
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_MCEO"+i+"_Msk">
    </#if>
</#if>
</#list>

<#if TCC_COMPARE_EVCTRL_EVACT0 != "OFF">
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCEI0_Msk | TCC_EVCTRL_EVACT0_"+TCC_COMPARE_EVCTRL_EVACT0>
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_TCEI0_Msk | TCC_EVCTRL_EVACT0_"+TCC_COMPARE_EVCTRL_EVACT0>
    </#if>
    <#if TCC_COMPARE_EVCTRL_TCINV0 == true>
    <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCINV0_Msk">
    </#if>
</#if>
<#if TCC_COMPARE_EVCTRL_EVACT1 != "OFF">
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCEI1_Msk | TCC_EVCTRL_EVACT1_"+TCC_COMPARE_EVCTRL_EVACT1>
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_TCEI1_Msk | TCC_EVCTRL_EVACT1_"+TCC_COMPARE_EVCTRL_EVACT1>
    </#if>
    <#if TCC_COMPARE_EVCTRL_TCINV1 == true>
    <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCINV1_Msk">
    </#if>
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#if TCC_COMPARE_INTERRUPT_MODE = true>
static TCC_CALLBACK_OBJECT ${TCC_INSTANCE_NAME}_CallbackObject;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${TCC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

/* Initialize TCC module in Compare Mode */
void ${TCC_INSTANCE_NAME}_CompareInitialize( void )
{
    /* Reset TCC */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_SWRST_Msk;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_SWRST_Msk) == TCC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Configure counter mode & prescaler */
<#if TCC_SLAVE_MODE == true>
    <@compress single_line=true>${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER_${TCC_CTRLA_PRESCALER}
                                | TCC_CTRLA_PRESCSYNC_PRESC | TCC_CTRLA_MSYNC_Msk
                                ${TCC_CTRLA_RUNSTDBY?then('| TCC_CTRLA_RUNSTDBY_Msk', '')};</@compress>
<#else>
    <@compress single_line=true>${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER_${TCC_CTRLA_PRESCALER}
                                | TCC_CTRLA_PRESCSYNC_PRESC
                                ${TCC_CTRLA_RUNSTDBY?then('| TCC_CTRLA_RUNSTDBY_Msk', '')};</@compress>
</#if>
    /* Configure waveform generation mode */
    ${TCC_INSTANCE_NAME}_REGS->TCC_WAVE = TCC_WAVE_WAVEGEN_${TCC_COMPARE_WAVE_WAVEGEN};

    <#if TCC_IS_OTM == 1>
    ${TCC_INSTANCE_NAME}_REGS->TCC_WEXCTRL = TCC_WEXCTRL_OTMX(${TCC_COMPARE_WEXCTRL_OTMX}UL);
    </#if>    

    <#if TCC_CTRLBSET_VAL?has_content>
    /* Configure timer one shot mode & direction */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET = (uint8_t)(${TCC_CTRLBSET_VAL});
    </#if>

    <#if TCC_DRVCTRL_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_DRVCTRL = (${TCC_DRVCTRL_VAL});
    </#if>
    
    ${TCC_INSTANCE_NAME}_REGS->TCC_PER = ${TCC_COMPARE_PERIOD}U;
    
<#list 0..(TCC_NUM_CHANNELS-1) as i>
    <#assign TCC_CC = "TCC_COMPARE_CC"+i>
    <#assign CH_NUM = i>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CC[${i}] = ${.vars[TCC_CC]}U;
</#list>    

    /* Clear all interrupt flags */
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_Msk;

    <#if TCC_COMPARE_INTERRUPT_MODE = true>
    /* Enable period Interrupt */
    ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn = NULL;
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTENSET =(${TCC_INTENSET_VAL});
    </#if>

    <#if TCC_EVCTRL_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_EVCTRL = (${TCC_EVCTRL_VAL});
    </#if>
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY) != 0U)
    {
        /* Wait for Write Synchronization */
    }
}

/* Enable the counter */
void ${TCC_INSTANCE_NAME}_CompareStart( void )
{
<#if TCC_COMPARE_CTRLBSET_ONESHOT == true>
    /* In one-shot mode, first disable the TCC and then enable */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA &= ~TCC_CTRLA_ENABLE_Msk;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_ENABLE_Msk) == TCC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
</#if>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA |= TCC_CTRLA_ENABLE_Msk;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_ENABLE_Msk) == TCC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Disable the counter */
void ${TCC_INSTANCE_NAME}_CompareStop( void )
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA &= ~TCC_CTRLA_ENABLE_Msk;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_ENABLE_Msk) == TCC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

uint32_t ${TCC_INSTANCE_NAME}_CompareFrequencyGet( void )
{
    return (uint32_t)${TCC_MODULE_FREQUENCY};
}

void ${TCC_INSTANCE_NAME}_CompareCommandSet(TCC_COMMAND command)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET = (uint8_t)((uint32_t)command << TCC_CTRLBSET_CMD_Pos);
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY) != 0U)
    {
        /* Wait for Write Synchronization */
    }    
}

<#if TCC_SIZE = 16>
/* Get the current counter value */
uint16_t ${TCC_INSTANCE_NAME}_Compare16bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET |= (uint8_t)TCC_CTRLBSET_CMD_READSYNC;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_CTRLB_Msk) == TCC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    while((${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET & TCC_CTRLBSET_CMD_Msk) != 0U)
    {
        /* Wait for CMD to become zero */
    }

    /* Read current count value */
    return (uint16_t)${TCC_INSTANCE_NAME}_REGS->TCC_COUNT;
}

/* Configure counter value */
void ${TCC_INSTANCE_NAME}_Compare16bitCounterSet( uint16_t count )
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_COUNT = count;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_COUNT_Msk) == TCC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure period value */
bool ${TCC_INSTANCE_NAME}_Compare16bitPeriodSet( uint16_t period )
{
    bool status = false;
    <#if TCC_COMPARE_CTRLBSET_LUPD == true>
    if((${TCC_INSTANCE_NAME}_REGS->TCC_STATUS & TCC_STATUS_${TCC_PBUF_REG_NAME}V_Msk) == 0U)
    {
        /* Configure period value */
        ${TCC_INSTANCE_NAME}_REGS->TCC_${TCC_PBUF_REG_NAME} = period;
        status = true;
    }
    <#else>
    /* Configure period value */
    ${TCC_INSTANCE_NAME}_REGS->TCC_PER = period;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_PER_Msk) == TCC_SYNCBUSY_PER_Msk)
    {
        /* Wait for Write Synchronization */
    }    
    status = true;
    </#if>
    return status;
}

/* Read period value */
uint16_t ${TCC_INSTANCE_NAME}_Compare16bitPeriodGet( void )
{
    /* Get period value */
    return (uint16_t)${TCC_INSTANCE_NAME}_REGS->TCC_PER;
}


/* Configure duty cycle value */
bool ${TCC_INSTANCE_NAME}_Compare16bitMatchSet(${TCC_INSTANCE_NAME}_CHANNEL_NUM channel, uint16_t compareValue )
{
    bool status = false;
<#if TCC_COMPARE_CTRLBSET_LUPD == true>
    if ((${TCC_INSTANCE_NAME}_REGS->TCC_STATUS & (1UL << (TCC_STATUS_${TCC_CBUF_REG_NAME}V0_Pos + (uint32_t)channel))) == 0U)
    {
        /* Set new compare value for compare channel */
        ${TCC_INSTANCE_NAME}_REGS->TCC_${TCC_CBUF_REG_NAME}[channel] = compareValue & 0xFFFFFFU;
        status = true;
    }
<#else>
    /* Set new compare value for compare channel */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CC[channel] = compareValue & 0xFFFFFFU;
    while(((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY) & (1UL << (TCC_SYNCBUSY_CC0_Pos + (uint32_t)channel))) != 0U)
    {
        /* Wait for Write Synchronization */
    }    
    status = true;
</#if>
    return status;
}


<#elseif TCC_SIZE == 24>
/* Get the current counter value */
uint32_t ${TCC_INSTANCE_NAME}_Compare24bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET |= (uint8_t)TCC_CTRLBSET_CMD_READSYNC;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_CTRLB_Msk) == TCC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for Write Synchronization */
    }

    while((${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET & TCC_CTRLBSET_CMD_Msk) != 0U)
    {
        /* Wait for CMD to become zero */
    }

    /* Read current count value */
    return ${TCC_INSTANCE_NAME}_REGS->TCC_COUNT;
}

/* Configure counter value */
void ${TCC_INSTANCE_NAME}_Compare24bitCounterSet( uint32_t count )
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_COUNT = count;

    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_COUNT_Msk) == TCC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure period value */
bool ${TCC_INSTANCE_NAME}_Compare24bitPeriodSet( uint32_t period )
{
    bool status = false;
    <#if TCC_COMPARE_CTRLBSET_LUPD == true>
    if((${TCC_INSTANCE_NAME}_REGS->TCC_STATUS & TCC_STATUS_${TCC_PBUF_REG_NAME}V_Msk) == 0U)
    {
        /* Configure period value */
        ${TCC_INSTANCE_NAME}_REGS->TCC_${TCC_PBUF_REG_NAME} = period & 0xFFFFFFU;
        status = true;
    }
    <#else>
    /* Configure period value */
    ${TCC_INSTANCE_NAME}_REGS->TCC_PER = period & 0xFFFFFFU;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_PER_Msk) == TCC_SYNCBUSY_PER_Msk)
    {
        /* Wait for Write Synchronization */
    }    
    status = true;
    </#if>
    return status;
}

/* Read period value */
uint32_t ${TCC_INSTANCE_NAME}_Compare24bitPeriodGet( void )
{
    /* Get period value */
    return ${TCC_INSTANCE_NAME}_REGS->TCC_PER;
}

/* Configure duty cycle value */
bool ${TCC_INSTANCE_NAME}_Compare24bitMatchSet(${TCC_INSTANCE_NAME}_CHANNEL_NUM channel, uint32_t compareValue )
{
    bool status = false;
<#if TCC_COMPARE_CTRLBSET_LUPD == true>
    if ((${TCC_INSTANCE_NAME}_REGS->TCC_STATUS & (1UL << (TCC_STATUS_${TCC_CBUF_REG_NAME}V0_Pos + (uint32_t)channel))) == 0U)
    {
        /* Set new compare value for compare channel */
        ${TCC_INSTANCE_NAME}_REGS->TCC_${TCC_CBUF_REG_NAME}[channel] = compareValue & 0xFFFFFFU;
        status = true;
    }
<#else>
    /* Set new compare value for compare channel */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CC[channel] = compareValue & 0xFFFFFFU;
    while(((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY) & (1UL << (TCC_SYNCBUSY_CC0_Pos + (uint32_t)channel))) != 0U)
    {
        /* Wait for Write Synchronization */
    }    
    status = true;
</#if>
    return status;
}
</#if>

<#if TCC_COMPARE_INTERRUPT_MODE = true>
/* Register callback function */
void ${TCC_INSTANCE_NAME}_CompareCallbackRegister( TCC_CALLBACK callback, uintptr_t context )
{
    ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn = callback;

    ${TCC_INSTANCE_NAME}_CallbackObject.context = context;
}

<#-- Single interrupt line -->
<#if TCC_NUM_INT_LINES == 0>
/* Compare match interrupt handler */
void ${TCC_INSTANCE_NAME}_InterruptHandler( void )
{
    uint32_t status;
    status = ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
    /* clear period interrupt */
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_Msk;
    if(${TCC_INSTANCE_NAME}_CallbackObject.callback_fn != NULL)
    {
        ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn(status, ${TCC_INSTANCE_NAME}_CallbackObject.context);
    }
}

<#-- Multiple interrupt lines -->
<#else>
        <#if TCC_COMPARE_INTENSET_OVF == true >
            <#lt>/* Interrupt Handler */
            <#lt>void ${TCC_INSTANCE_NAME}_InterruptHandler(void)
            <#lt>{
            <#lt>    uint32_t status;
            <#lt>    status = (uint32_t)(${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG & 0xFFFFU);
            <#lt>    /* Clear interrupt flags */
            <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = 0xFFFFU;
            <#lt>    if (${TCC_INSTANCE_NAME}_CallbackObject.callback_fn != NULL)
            <#lt>    {
            <#lt>        ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn(status, ${TCC_INSTANCE_NAME}_CallbackObject.context);
            <#lt>    }

            <#lt>}
        </#if>

        <#list 0..(TCC_NUM_CHANNELS-1) as i>
        <#assign TCC_INT_MC = "TCC_COMPARE_INTENSET_MC" + i>
            <#if .vars[TCC_INT_MC] == true>
                <#lt>/* Interrupt Handler */
                <#lt>void ${TCC_INSTANCE_NAME}_MC${i}_InterruptHandler(void)
                <#lt>{
                <#lt>    uint32_t status;
                <#lt>    status = (uint32_t)TCC_INTFLAG_MC${i}_Msk;
                <#lt>    /* Clear interrupt flags */
                <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_MC${i}_Msk;
                <#lt>    if (${TCC_INSTANCE_NAME}_CallbackObject.callback_fn != NULL)
                <#lt>    {
                <#lt>        ${TCC_INSTANCE_NAME}_CallbackObject.callback_fn(status, ${TCC_INSTANCE_NAME}_CallbackObject.context);
                <#lt>    }

                <#lt>}
            </#if>
        </#list>
</#if>  <#-- End of TCC_NUM_INT_LINES -->

<#-- Interrupt mode is disabled -->
<#else>

uint32_t ${TCC_INSTANCE_NAME}_CompareStatusGet( void )
{
    uint32_t compare_status;
    compare_status = ((${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG));
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = compare_status;
    return compare_status;
}
</#if>
