/*******************************************************************************
  PWM Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${PWM_INSTANCE_NAME}.c

  Summary
    ${PWM_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the PWM peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

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

/*  This section lists the other files that are included in this file.
*/
#include "device.h"
#include "plib_${PWM_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#compress>
<#assign PWM_FPE_VAL = "">
<#assign PWM_FPV1_VAL = "">
<#assign PWM_FPV2_VAL = "">
<#assign PWM_INTERRUPT = false>
<#assign PWM_ELMR0_VAL = "">
<#assign PWM_ELMR1_VAL = "">
<#assign PWM_SCM_VAL = "">


<#list 0..3 as i>
<#assign CH_NUM = i >
<#assign PWM_CH_ENABLE = "PWM_CH_"+ i +"_ENABLE">
<#assign PWM_CH_SYNCENABLE = "PWM_CH_"+i+"_SYNCENABLE">
<#assign PWM_Fault_Enable = "PWM_CH_"+i+"_FAULT_ENABLE">
<#assign PWM_FPE = "PWM_CH_"+i+"_FPE">
<#assign PWM_FPV_FPVL = "PWM_FAULT_"+i+"_FPV_FPVL">
<#assign PWM_FPV_FPVH = "PWM_FAULT_"+i+"_FPV_FPVH">
<#assign PWM_IER1_CHID = "PWM_CH_"+i+"_IER1_CHID">
<#assign PWM_IER1_FCHID = "PWM_FAULT_"+i+"_IER1_FCHID">

<#-- Fault configuration preparation -->
<#if .vars[PWM_CH_ENABLE] == true && .vars[PWM_Fault_Enable] == true>
    <#if PWM_FPE_VAL != "">
        <#assign PWM_FPE_VAL = PWM_FPE_VAL + " | \n\t\t (0x1UL << (${.vars[PWM_FPE]}U + (PWM_FPE_FPE${CH_NUM}_Pos)))">
    <#else>
        <#assign PWM_FPE_VAL = "(0x1UL << (${.vars[PWM_FPE]}U + (PWM_FPE_FPE${CH_NUM}_Pos)))">
    </#if>
    <#-- Register values of PWM_FPV1 and PWM_FPV2 -->
    <#if .vars[PWM_FPV_FPVH] != "2">
        <#if PWM_FPV1_VAL != "">
            <#assign PWM_FPV1_VAL = PWM_FPV1_VAL + "\n\t\t | (${.vars[PWM_FPV_FPVH]}U << PWM_FPV1_FPVH${CH_NUM}_Pos)">
        <#else>
            <#assign PWM_FPV1_VAL = "(${.vars[PWM_FPV_FPVH]}U << PWM_FPV1_FPVH${CH_NUM}_Pos)">
        </#if>
    <#else>
        <#if PWM_FPV2_VAL != "">
            <#assign PWM_FPV2_VAL = PWM_FPV2_VAL + " | (PWM_FPV2_FPZH${CH_NUM}_Msk)">
        <#else>
            <#assign PWM_FPV2_VAL = "(PWM_FPV2_FPZH${CH_NUM}_Msk)">
        </#if>
    </#if>
    <#if .vars[PWM_FPV_FPVL] != "2">
        <#if PWM_FPV1_VAL != "">
            <#assign PWM_FPV1_VAL = PWM_FPV1_VAL + " | (${.vars[PWM_FPV_FPVL]}UL << PWM_FPV1_FPVL${CH_NUM}_Pos)">
        <#else>
            <#assign PWM_FPV1_VAL = "(${.vars[PWM_FPV_FPVH]}UL << PWM_FPV1_FPVH${CH_NUM}_Pos)">
        </#if>
    <#else>
        <#if PWM_FPV2_VAL != "">
            <#assign PWM_FPV2_VAL = PWM_FPV2_VAL + " | (PWM_FPV2_FPZL${CH_NUM}_Msk)">
        <#else>
            <#assign PWM_FPV2_VAL = "(PWM_FPV2_FPZH${CH_NUM}_Msk)">
        </#if>
    </#if>
</#if>

<#if .vars[PWM_CH_ENABLE] == true && (.vars[PWM_IER1_CHID] == true || .vars[PWM_IER1_FCHID] == true)>
    <#assign PWM_INTERRUPT = true>
</#if>

<#if .vars[PWM_CH_ENABLE] == true && .vars[PWM_CH_SYNCENABLE] == true>
    <#if PWM_SCM_VAL != "">
        <#assign PWM_SCM_VAL = PWM_SCM_VAL + "| PWM_SCM_SYNC${CH_NUM}_Msk">
    <#else>
        <#assign PWM_SCM_VAL = "PWM_SCM_SYNC0_Msk | PWM_SCM_SYNC${CH_NUM}_Msk">
    </#if>
</#if>
</#list>

<#list 0..7 as i>
<#-- Fault event preparation -->
<#assign COMPARE_ID = i>
<#assign PWM_CMPM_CEN = "PWM_COMP_"+i+"_CMPM_CEN">
<#assign PWM_ELMR0_CSEL = "PWM_COMP_"+i+"_ELMR0_CSEL">
<#assign PWM_ELMR1_CSEL = "PWM_COMP_"+i+"_ELMR1_CSEL">
<#if .vars[PWM_CMPM_CEN] == true>
    <#if .vars[PWM_ELMR0_CSEL]?? && .vars[PWM_ELMR0_CSEL] == true>
        <#if PWM_ELMR0_VAL != "">
            <#assign PWM_ELMR0_VAL = PWM_ELMR0_VAL + " | PWM_ELMR_CSEL${COMPARE_ID}_Msk">
        <#else>
            <#assign PWM_ELMR0_VAL = "PWM_ELMR_CSEL${COMPARE_ID}_Msk">
        </#if>
    </#if>
    <#if .vars[PWM_ELMR1_CSEL]?? && .vars[PWM_ELMR1_CSEL] == true>
        <#if PWM_ELMR1_VAL != "">
            <#assign PWM_ELMR1_VAL = PWM_ELMR1_VAL + " | PWM_ELMR_CSEL${COMPARE_ID}_Msk">
        <#else>
            <#assign PWM_ELMR1_VAL = "PWM_ELMR_CSEL${COMPARE_ID}_Msk">
        </#if>
    </#if>
</#if>
</#list>
</#compress>

<#if PWM_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
    <#lt>volatile static PWM_CALLBACK_OBJECT ${PWM_INSTANCE_NAME}_CallbackObj;
</#if>

/* Initialize enabled PWM channels */
void ${PWM_INSTANCE_NAME}_Initialize (void)
{
<#if PWM_CLK_A_ENABLE == true && PWM_CLK_B_ENABLE == true>
    /* Clock configuration */
    ${PWM_INSTANCE_NAME}_REGS->PWM_CLK = PWM_CLK_PREA_${PWM_CLK_PREA} | PWM_CLK_DIVA(${PWM_CLK_DIVA}U) |
        PWM_CLK_PREB_${PWM_CLK_PREB} | PWM_CLK_DIVB(${PWM_CLK_DIVB}U);
<#elseif PWM_CLK_A_ENABLE == true>
    /* Clock configuration */
    ${PWM_INSTANCE_NAME}_REGS->PWM_CLK = PWM_CLK_PREA_${PWM_CLK_PREA} | PWM_CLK_DIVA(${PWM_CLK_DIVA});
<#elseif PWM_CLK_B_ENABLE == true>
    /* Clock configuration */
    ${PWM_INSTANCE_NAME}_REGS->PWM_CLK = PWM_CLK_PREB_${PWM_CLK_PREB} | PWM_CLK_DIVB(${PWM_CLK_DIVB});
</#if>
<#if PWM_SCM_VAL?has_content >

    /* Synchronous channels configuration */
    ${PWM_INSTANCE_NAME}_REGS->PWM_SCM = ${PWM_SCM_VAL} | PWM_SCM_UPDM_${PWM_SCM_UPDM};
    ${PWM_INSTANCE_NAME}_REGS->PWM_SCUP = PWM_SCUP_UPR(${PWM_SCUP_UPR}U);
</#if>
<#list 0..3 as i>
<#assign CH_NUM = i >
<#assign PWM_CH_ENABLE = "PWM_CH_"+ i +"_ENABLE">
<#assign PWM_CH_SYNC_ENABLE = "PWM_CH_"+i+"_SYNCENABLE">
<#assign PWM_CMR_CPRE = "PWM_CH_"+i+"_CMR_CPRE">
<#assign PWM_CMR_CALG = "PWM_CH_"+i+"_CMR_CALG">
<#assign PWM_CMR_UPDS = "PWM_CH_"+i+"_CMR_UPDS">
<#assign PWM_CMR_CES = "PWM_CH_"+i+"_CMR_CES">
<#assign PWM_CMR_CPOL = "PWM_CH_"+i+"_CMR_CPOL">
<#assign PWM_CPRD = "PWM_CH_"+i+"_CPRD">
<#assign PWM_CDTY = "PWM_CH_"+i+"_CDTY">
<#assign PWM_CMR_DTE = "PWM_CH_"+i+"_CMR_DTE">
<#assign PWM_DT_DTL = "PWM_CH_"+i+"_DT_DTL">
<#assign PWM_DT_DTH = "PWM_CH_"+i+"_DT_DTH">
<#assign PWM_Fault_Enable = "PWM_CH_"+i+"_FAULT_ENABLE">
<#assign PWM_FPE = "PWM_CH_"+i+"_FPE">
<#assign PWM_IER1_CHID = "PWM_CH_"+i+"_IER1_CHID">
<#assign PWM_IER1_FCHID = "PWM_FAULT_"+i+"_IER1_FCHID">
    <#if .vars[PWM_CH_ENABLE] == true>

    /************** Channel ${CH_NUM} *************************/
        <#if .vars[PWM_CH_SYNC_ENABLE] == false>
            <#lt>    /* PWM channel mode configurations */
            <#if .vars[PWM_CMR_CALG] == "LEFT_ALIGNED">
                <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[${CH_NUM}].PWM_CMR = PWM_CMR_CPRE_${.vars[PWM_CMR_CPRE]} | PWM_CMR_CALG_${.vars[PWM_CMR_CALG]}
                    | PWM_CMR_CPOL_${.vars[PWM_CMR_CPOL]} ${.vars[PWM_CMR_DTE]?then('| (PWM_CMR_DTE_Msk)', '')};
            <#else>
                <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[${CH_NUM}].PWM_CMR = PWM_CMR_CPRE_${.vars[PWM_CMR_CPRE]} | PWM_CMR_CALG_${.vars[PWM_CMR_CALG]}
                    | PWM_CMR_CPOL_${.vars[PWM_CMR_CPOL]} | PWM_CMR_UPDS_${.vars[PWM_CMR_UPDS]} \
                    | PWM_CMR_CES_${.vars[PWM_CMR_CES]} ${.vars[PWM_CMR_DTE]?then('| (PWM_CMR_DTE_Msk)', '')};
            </#if>

            <#lt>    /* PWM period */
            <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[${CH_NUM}].PWM_CPRD = ${.vars[PWM_CPRD]}U;
        </#if>

        <#lt>    /* PWM duty cycle */
        <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[${CH_NUM}].PWM_CDTY = ${.vars[PWM_CDTY]}U;
        <#if .vars[PWM_CMR_DTE] == true>
            <#if .vars[PWM_CH_SYNC_ENABLE] == true>
                <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[${CH_NUM}].PWM_CMR = PWM_CMR_DTE_Msk;
            </#if>
            <#lt>    /* Dead time */
            <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[${CH_NUM}].PWM_DT = (${.vars[PWM_DT_DTL]}UL << PWM_DT_DTL_Pos) | (${.vars[PWM_DT_DTH]}U);
        </#if> <#-- PWM_CMR_DTE -->
        <#if PWM_INTERRUPT == true>
        <#lt>    /* Enable counter event */
        <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_IER1 = 0x${PWM_IER1_REG};
        <#lt>    ${PWM_INSTANCE_NAME}_CallbackObj.callback_fn = NULL;
        </#if>
    </#if> <#-- PWM_CH_ENABLE -->
</#list>
<#if PWM_FPE_VAL?has_content>

    /*************************** Fault ************************/
    /* Enable fault input */
    ${PWM_INSTANCE_NAME}_REGS->PWM_FPE = ${PWM_FPE_VAL};
    <#if PWM_FPV1_VAL?has_content>
    <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_FPV1 = ${PWM_FPV1_VAL};
    </#if>
    <#if PWM_FPV2_VAL?has_content>
    <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_FPV2 = ${PWM_FPV2_VAL};
    <#else>
    <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_FPV2 = 0x0;
    </#if>
    /* Fault mode configuration */
    ${PWM_INSTANCE_NAME}_REGS->PWM_FMR = PWM_FMR_FFIL(0x${PWM_FMR_FFIL_VAL?upper_case}) | PWM_FMR_FPOL(0x${PWM_FMR_FPOL_VAL?upper_case}) | PWM_FMR_FMOD(0x${PWM_FMR_FMOD_VAL?upper_case});
</#if>
<#list 0..7 as i>
<#assign PWM_CMPM_CEN = "PWM_COMP_"+i+"_CMPM_CEN">
<#assign PWM_CMPV_CV = "PWM_COMP_"+i+"_CMPV_CV">
<#assign PWM_CMPV_CVM = "PWM_COMP_"+i+"_CMPV_CVM">
<#assign PWM_CMPM_CTR = "PWM_COMP_"+i+"_CMPM_CTR">
<#assign PWM_CMPM_CPR = "PWM_COMP_"+i+"_CMPM_CPR">
<#assign PWM_CMPM_CUPR = "PWM_COMP_"+i+"_CMPM_CUPR">
<#assign COMP_ID = i>
    <#if .vars[PWM_CMPM_CEN] == true>

    /************* Compare Unit ${COMP_ID} **************************/
    <#lt>    /* Compare unit configurations */
    <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_CMP[${COMP_ID}].PWM_CMPM = PWM_CMPM_CEN_Msk | PWM_CMPM_CTR(${.vars[PWM_CMPM_CTR]}U) | PWM_CMPM_CPR(${.vars[PWM_CMPM_CPR]}U)
                    | PWM_CMPM_CUPR(${.vars[PWM_CMPM_CUPR]}U);
    <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_CMP[${COMP_ID}].PWM_CMPV = PWM_CMPV_CV(${.vars[PWM_CMPV_CV]}U) | PWM_CMPV_CVM_${.vars[PWM_CMPV_CVM]};
    </#if>
</#list>
    <#if PWM_ELMR0_VAL?has_content>

    <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_ELMR[0] = ${PWM_ELMR0_VAL};
    </#if>
    <#if PWM_ELMR1_VAL?has_content>

    <#lt>    ${PWM_INSTANCE_NAME}_REGS->PWM_ELMR[1] = ${PWM_ELMR1_VAL};
    </#if>
}

/* Start the PWM generation */
void ${PWM_INSTANCE_NAME}_ChannelsStart (PWM_CHANNEL_MASK channelMask)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_ENA = (uint32_t)channelMask;
}

/* Stop the PWM generation */
void ${PWM_INSTANCE_NAME}_ChannelsStop (PWM_CHANNEL_MASK channelMask)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_DIS = (uint32_t)channelMask;
}

/* configure PWM period */
void ${PWM_INSTANCE_NAME}_ChannelPeriodSet (PWM_CHANNEL_NUM channel, uint16_t period)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_CPRDUPD = period;
}

/* Read PWM period */
uint16_t ${PWM_INSTANCE_NAME}_ChannelPeriodGet (PWM_CHANNEL_NUM channel)
{
    return (uint16_t)${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_CPRD;
}

/* Configure dead time */
void ${PWM_INSTANCE_NAME}_ChannelDeadTimeSet (PWM_CHANNEL_NUM channel, uint16_t deadtime_high, uint16_t deadtime_low)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CH_NUM[channel].PWM_DTUPD = (((uint32_t)deadtime_low << PWM_DT_DTL_Pos) | deadtime_high);
}

/* Configure compare unit value */
void ${PWM_INSTANCE_NAME}_CompareValueSet (PWM_COMPARE cmp_unit, uint16_t cmp_value)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_CMP[cmp_unit].PWM_CMPVUPD = cmp_value;
}

/* Enable counter event */
void ${PWM_INSTANCE_NAME}_ChannelCounterEventEnable (PWM_CHANNEL_MASK channelMask)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_IER1 = (uint32_t)channelMask;
}

/* Disable counter event */
void ${PWM_INSTANCE_NAME}_ChannelCounterEventDisable (PWM_CHANNEL_MASK channelMask)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_IDR1 = (uint32_t)channelMask;
}


/* Enable synchronous update */
void ${PWM_INSTANCE_NAME}_SyncUpdateEnable (void)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_SCUC = PWM_SCUC_UPDULOCK_Msk;
}

/* Clear the fault status */
void ${PWM_INSTANCE_NAME}_FaultStatusClear(PWM_FAULT_ID fault_id)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_FCR = 0x1UL << (uint32_t)fault_id;
}

/* Override PWM outputs */
void ${PWM_INSTANCE_NAME}_ChannelOverrideEnable(PWM_CHANNEL_NUM channel)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_OS &= ~((1UL << (uint32_t)channel) | (1UL << ((uint32_t)channel + 16U)));

}

/* Disable override of PWM outputs */
void ${PWM_INSTANCE_NAME}_ChannelOverrideDisable(PWM_CHANNEL_NUM channel)
{
    ${PWM_INSTANCE_NAME}_REGS->PWM_OS |= ((1UL << (uint32_t)channel) | (1UL << ((uint32_t)channel + 16U)));
}

<#if PWM_INTERRUPT == true>
    <#lt> /* Register callback function */
    <#lt>void ${PWM_INSTANCE_NAME}_CallbackRegister(PWM_CALLBACK callback, uintptr_t context)
    <#lt>{
    <#lt>    ${PWM_INSTANCE_NAME}_CallbackObj.callback_fn = callback;
    <#lt>    ${PWM_INSTANCE_NAME}_CallbackObj.context = context;
    <#lt>}

    <#lt>/* Interrupt Handler */
    <#lt>void __attribute__((used)) ${PWM_INSTANCE_NAME}_InterruptHandler(void)
    <#lt>{
    <#lt>    uint32_t status = ${PWM_INSTANCE_NAME}_REGS->PWM_ISR1;

    <#lt>    /* Additional temporary variable used to prevent MISRA violations (Rule 13.x) */
    <#lt>    uintptr_t context = ${PWM_INSTANCE_NAME}_CallbackObj.context;

    <#lt>    if (${PWM_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
    <#lt>    {
    <#lt>        ${PWM_INSTANCE_NAME}_CallbackObj.callback_fn(status, context);
    <#lt>    }
    <#lt>}

<#else>

/* Check the status of counter event */
bool ${PWM_INSTANCE_NAME}_ChannelCounterEventStatusGet (PWM_CHANNEL_NUM channel)
{
    bool pwm_status;
    pwm_status = (bool)(((${PWM_INSTANCE_NAME}_REGS->PWM_ISR1 >> (uint32_t)channel) & 0x1U) != 0U);
    return pwm_status;
}
</#if>

/**
 End of File
*/
