/*******************************************************************************
  TCC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TCC_INSTANCE_NAME?lower_case}.c

  Summary
    ${TCC_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the TCC peripheral library.  This
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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${TCC_INSTANCE_NAME?lower_case}.h"

<#compress>
<#assign TCC_INTERRUPT = false>
<#assign TCC_WAVE_VAL = "">
<#assign TCC_WEXCTRL_DT_VAL = "">
<#assign TCC_DRVCTRL_FAULT_VAL = "">
<#assign TCC_PATT_VAL = "">
<#assign TCC_EVCTRL_VAL = "">
<#assign TCC_INTENSET_VAL = "">
<#assign TCC_CTRLB_DIR = "">
<#assign TCC_WAVE_VAL = "TCC_WAVE_WAVEGEN_" + TCC_WAVE_WAVEGEN>

<#if (TCC_WAVE_WAVEGEN == "NPWM")>
    <#-- Ramp -->
    <#assign TCC_WAVE_VAL = TCC_WAVE_VAL + " | TCC_WAVE_RAMP_" + TCC_WAVE_RAMP>
</#if>

<#list 0..(TCC_NUM_CHANNELS-1) as i>
<#assign CH_NUM = i >
<#assign TCC_POLARITY = "TCC_"+i+"_WAVE_POL">
<#assign TCC_POLARITY_NPWM = "TCC_"+i+"_WAVE_POL_NPWM">
<#assign TCC_MCEO = "TCC_EVCTRL_MCEO_" + i>
<#assign TCC_MCEI = "TCC_EVCTRL_MCEI_" + i>
<#assign TCC_INT_MC = "TCC_INTENSET_MC_" + i>
<#-- Dead Time -->
<#if TCC_IS_DEAD_TIME gte 1 && i < TCC_NUM_OUTPUTS/2>
    <#assign TCC_DT_ENABLE = "TCC_"+i+"_WEXCTRL_DTIEN">
    <#if .vars[TCC_DT_ENABLE] == true>
        <#if TCC_WEXCTRL_DT_VAL != "">
            <#assign TCC_WEXCTRL_DT_VAL = TCC_WEXCTRL_DT_VAL + " | TCC_WEXCTRL_DTIEN"+i+"_Msk">
        <#else>
            <#assign TCC_WEXCTRL_DT_VAL = "TCC_WEXCTRL_DTIEN"+i+"_Msk">
        </#if>
    </#if>
</#if> <#-- Dead Time End -->

<#-- swap -->
<#if TCC_IS_SWAP == 1 && i < TCC_NUM_OUTPUTS/2>
    <#assign TCC_SWAP_ENABLE = "TCC_"+i+"_WAVE_SWAP">
    <#if .vars[TCC_SWAP_ENABLE] == true>
        <#if TCC_WAVE_VAL != "">
            <#assign TCC_WAVE_VAL = TCC_WAVE_VAL + " \n \t \t | TCC_WAVE_SWAP"+i+"_Msk">
        <#else>
            <#assign TCC_WAVE_VAL = "TCC_WAVE_SWAP"+i+"_Msk">
        </#if>
    </#if>
</#if> <#-- Swap End -->
<#-- circular buffer -->
<#if TCC_WAVE_WAVEGEN == "DSBOTH" && i < (TCC_NUM_OUTPUTS/2)?floor>
    <#assign TCC_CICC_ENABLE = "TCC_"+i+"_WAVE_CICCEN">
    <#if .vars[TCC_CICC_ENABLE] == true>
        <#if TCC_WAVE_VAL != "">
            <#assign TCC_WAVE_VAL = TCC_WAVE_VAL + " \n \t \t | TCC_WAVE_CICCEN"+i+"_Msk">
        <#else>
            <#assign TCC_WAVE_VAL = "TCC_WAVE_CICCEN"+i+"_Msk">
        </#if>
    </#if> 
</#if> <#-- circular buffer End -->
<#-- polarity -->
<#if (TCC_WAVE_WAVEGEN == "DSBOTTOM") || (TCC_WAVE_WAVEGEN == "DSBOTH") || (TCC_WAVE_WAVEGEN == "DSTOP") >
    <#if .vars[TCC_POLARITY] == "1">
        <#if TCC_WAVE_VAL != "">
            <#assign TCC_WAVE_VAL = TCC_WAVE_VAL + " | TCC_WAVE_POL"+i+"_Msk">
        <#else>
            <#assign TCC_WAVE_VAL = "TCC_WAVE_POL"+i+"_Msk">
        </#if>
    </#if>
<#elseif (TCC_WAVE_WAVEGEN == "NPWM")>
<#if .vars[TCC_POLARITY_NPWM] == "1">
    <#if TCC_WAVE_VAL != "">
        <#assign TCC_WAVE_VAL = TCC_WAVE_VAL + " | TCC_WAVE_POL"+i+"_Msk">
    <#else>
        <#assign TCC_WAVE_VAL = "TCC_WAVE_POL"+i+"_Msk">
    </#if>
   
</#if>
</#if>
<#-- polarity end -->
<#-- Events -->
<#if .vars[TCC_MCEO] == true>
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + "\n \t \t | TCC_EVCTRL_MCEO"+i+"_Msk">
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_MCEO"+i+"_Msk">
    </#if>
</#if>

<#if .vars[TCC_MCEI] == true>
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + "\n \t \t | TCC_EVCTRL_MCEI"+i+"_Msk">
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_MCEI"+i+"_Msk">
    </#if>
</#if>


<#if .vars[TCC_INT_MC] == true>
    <#if TCC_INTENSET_VAL != "">
        <#assign TCC_INTENSET_VAL = TCC_INTENSET_VAL + " \n \t \t | TCC_INTENSET_MC"+i+"_Msk">
    <#else>
        <#assign TCC_INTENSET_VAL = "TCC_INTENSET_MC"+i+"_Msk">
    </#if>
    <#assign TCC_INTERRUPT = true>
</#if>
</#list>

<#if TCC_WAVE_WAVEGEN == "NPWM">
    <#if TCC_CTRLBSET_DIR == true>
        <#assign TCC_CTRLB_DIR = "TCC_CTRLBSET_DIR_Msk">
    </#if>
</#if>

<#-- Fault -->
<#list 0..(TCC_NUM_OUTPUTS-1) as i>
<#assign CH_NUM = i >
<#assign TCC_FAULT_POLARITY = "TCC_"+i+"_DRVCTRL_NRE_NRV">
<#if .vars[TCC_FAULT_POLARITY] == "1">
    <#if TCC_DRVCTRL_FAULT_VAL != "">
        <#assign TCC_DRVCTRL_FAULT_VAL = TCC_DRVCTRL_FAULT_VAL + "\n\t\t | TCC_DRVCTRL_NRE"+i+"_Msk | TCC_DRVCTRL_NRV"+i+"_Msk">
    <#else>
        <#assign TCC_DRVCTRL_FAULT_VAL = "TCC_DRVCTRL_NRE"+i+"_Msk | TCC_DRVCTRL_NRV"+i+"_Msk">
    </#if>
<#elseif .vars[TCC_FAULT_POLARITY] == "0">
    <#if TCC_DRVCTRL_FAULT_VAL != "">
        <#assign TCC_DRVCTRL_FAULT_VAL = TCC_DRVCTRL_FAULT_VAL + "\n\t\t | TCC_DRVCTRL_NRE"+i+"_Msk">
    <#else>
        <#assign TCC_DRVCTRL_FAULT_VAL = "TCC_DRVCTRL_NRE"+i+"_Msk">
    </#if>
</#if>
</#list>

<#-- Invert outputs -->
<#assign TCC_DRVCTRL_INVEN = "">
<#list 0..(TCC_NUM_OUTPUTS-1) as i>
<#assign CH_NUM = i>
<#assign TCC_INVEN = "TCC_DRVCTRL_INVEN" + i>
<#if .vars[TCC_INVEN] == true> 
    <#if TCC_DRVCTRL_INVEN != "">
        <#assign TCC_DRVCTRL_INVEN = TCC_DRVCTRL_INVEN + "\n\t\t | TCC_DRVCTRL_INVEN"+i+"_Msk">
    <#else>
        <#assign TCC_DRVCTRL_INVEN = "TCC_DRVCTRL_INVEN" + i + "_Msk">
    </#if>
</#if>    
</#list>

<#-- Pattern Generation -->
<#if TCC_IS_PG == 1>
<#list 0..(TCC_NUM_OUTPUTS-1) as i>
<#assign CH_NUM = i >
<#assign TCC_PATT_PGE = "TCC_"+i+"PATT_PGE">
<#assign TCC_PATT_PGV = "TCC_"+i+"PATT_PGV">
<#if .vars[TCC_PATT_PGE] == true>
    <#if .vars[TCC_PATT_PGV] == "1">
        <#if TCC_PATT_VAL != "">
            <#assign TCC_PATT_VAL = TCC_PATT_VAL + " \n \t \t | TCC_PATT_PGE"+i+"_Msk | TCC_PATT_PGV"+i+"_Msk">
        <#else>
            <#assign TCC_PATT_VAL = "TCC_PATT_PGE"+i+"_Msk | TCC_PATT_PGV"+i+"_Msk">
        </#if>
    <#else>
        <#if TCC_PATT_VAL != "">
            <#assign TCC_PATT_VAL = TCC_PATT_VAL + " \n \t \t | TCC_PATT_PGE"+i+"_Msk">
        <#else>
            <#assign TCC_PATT_VAL = "TCC_PATT_PGE"+i+"_Msk">
        </#if>
    </#if>
</#if>
</#list>
</#if>

<#if TCC_INTENSET_OVF == true>
    <#assign TCC_INTERRUPT = true>
    <#if TCC_INTENSET_VAL != "">
        <#assign TCC_INTENSET_VAL = TCC_INTENSET_VAL + " \n \t \t | TCC_INTENSET_OVF_Msk">
    <#else>
        <#assign TCC_INTENSET_VAL = "TCC_INTENSET_OVF_Msk">
    </#if>
</#if>
<#if TCC_INTENSET_FAULT0 == true>
    <#assign TCC_INTERRUPT = true>
    <#if TCC_INTENSET_VAL != "">
        <#assign TCC_INTENSET_VAL = TCC_INTENSET_VAL + " \n \t \t | TCC_INTENSET_FAULT0_Msk">
    <#else>
        <#assign TCC_INTENSET_VAL = "TCC_INTENSET_FAULT0_Msk">
    </#if>
</#if>
<#if TCC_INTENSET_FAULT1 == true>
    <#assign TCC_INTERRUPT = true>
    <#if TCC_INTENSET_VAL != "">
        <#assign TCC_INTENSET_VAL = TCC_INTENSET_VAL + " \n \t \t | TCC_INTENSET_FAULT1_Msk">
    <#else>
        <#assign TCC_INTENSET_VAL = "TCC_INTENSET_FAULT1_Msk">
    </#if>
</#if>
<#if TCC_WEXCTRL_DT_VAL?has_content>
<#assign TCC_WEXCTRL_DT_VAL = TCC_WEXCTRL_DT_VAL + "\n \t \t | TCC_WEXCTRL_DTLS(${TCC_WEXCTRL_DTLS}UL) | TCC_WEXCTRL_DTHS(${TCC_WEXCTRL_DTHS}UL)">
</#if>

<#if TCC_EVCTRL_OVFEO == true>
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_OVFEO_Msk">
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_OVFEO_Msk">
    </#if>
</#if>

<#if TCC_EVCTRL_EVACT0 != "OFF">
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + "\n \t \t | TCC_EVCTRL_TCEI0_Msk | TCC_EVCTRL_EVACT0_" + TCC_EVCTRL_EVACT0>
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_TCEI0_Msk | TCC_EVCTRL_EVACT0_" + TCC_EVCTRL_EVACT0>
    </#if>
    <#if TCC_EVCTRL_TCINV0 == true>
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCINV0_Msk">
    </#if>
</#if>

<#if TCC_EVCTRL_EVACT1 != "OFF">
    <#if TCC_EVCTRL_VAL != "">
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + "\n \t \t | TCC_EVCTRL_TCEI1_Msk | TCC_EVCTRL_EVACT1_"+TCC_EVCTRL_EVACT1>
    <#else>
        <#assign TCC_EVCTRL_VAL = "TCC_EVCTRL_TCEI1_Msk | TCC_EVCTRL_EVACT1_"+TCC_EVCTRL_EVACT1>
    </#if>
    <#if TCC_EVCTRL_TCINV1 == true>
        <#assign TCC_EVCTRL_VAL = TCC_EVCTRL_VAL + " | TCC_EVCTRL_TCINV1_Msk">
    </#if>
</#if>

</#compress>

<#if TCC_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
    <#lt>volatile static TCC_CALLBACK_OBJECT ${TCC_INSTANCE_NAME}_CallbackObj;
</#if>

/* Initialize TCC module */
void ${TCC_INSTANCE_NAME}_PWMInitialize(void)
{
    /* Reset TCC */
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_SWRST_Msk;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_SWRST_Msk) == TCC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for sync */
    }
    /* Clock prescaler */
<#if TCC_SLAVE_MODE == true>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_MSYNC_Msk | TCC_CTRLA_PRESCALER_${TCC_CTRLA_PRESCALER} 
                            | TCC_CTRLA_PRESCSYNC_${TCC_CTRLA_PRESCYNC} ${(TCC_CTRLA_RUNSTDBY == true)?then('| (TCC_CTRLA_RUNSTDBY_Msk)', '')};
<#else>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA = TCC_CTRLA_PRESCALER_${TCC_CTRLA_PRESCALER} 
                            | TCC_CTRLA_PRESCSYNC_${TCC_CTRLA_PRESCYNC} ${(TCC_CTRLA_RUNSTDBY == true)?then('| (TCC_CTRLA_RUNSTDBY_Msk)', '')};
</#if>
<#if TCC_CTRLB_DIR?has_content && TCC_SLAVE_MODE == false>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET = (uint8_t)(${TCC_CTRLB_DIR});
</#if>
<#if TCC_IS_OTM == 1>
    ${TCC_INSTANCE_NAME}_REGS->TCC_WEXCTRL = TCC_WEXCTRL_OTMX(${TCC_WEXCTRL_OTMX}UL);
</#if>
<#if TCC_WEXCTRL_DT_VAL?has_content && TCC_IS_DEAD_TIME gte 1>
    /* Dead time configurations */
    ${TCC_INSTANCE_NAME}_REGS->TCC_WEXCTRL |= ${TCC_WEXCTRL_DT_VAL};
</#if>

<#if TCC_WAVE_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_WAVE = ${TCC_WAVE_VAL};
</#if>

<#if (TCC_WAVE_WAVEGEN == "NPWM")>
    <#if (TCC_WAVE_RAMP == "RAMP2" || TCC_WAVE_RAMP == "RAMP2A") && TCC_WAVE_CIPEREN == true>
    ${TCC_INSTANCE_NAME}_REGS->TCC_WAVE |= TCC_WAVE_CIPEREN_Msk;
    </#if>
    <#if TCC_WAVE_RAMP == "RAMP2A">
    ${TCC_INSTANCE_NAME}_REGS->TCC_WAVE |= TCC_WAVE_CICCEN0_Msk;
    </#if>    
</#if>

    /* Configure duty cycle values */
<#list 0..(TCC_NUM_CHANNELS-1) as i>
    <#assign TCC_CC = "TCC_"+i+"_CC">
    <#assign CH_NUM = i>
    ${TCC_INSTANCE_NAME}_REGS->TCC_CC[${i}] = ${.vars[TCC_CC]}U;
</#list>
<#if TCC_SLAVE_MODE == false>
    ${TCC_INSTANCE_NAME}_REGS->TCC_PER = ${TCC_PER_PER}U;
</#if>

<#if TCC_PATT_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_PATT =${TCC_PATT_VAL};
</#if>
<#if TCC_DRVCTRL_INVEN?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_DRVCTRL = ${TCC_DRVCTRL_INVEN};
</#if>    

<#if TCC_EVCTRL_EVACT0 == "FAULT" || TCC_EVCTRL_EVACT1 == "FAULT">
    ${TCC_INSTANCE_NAME}_REGS->TCC_DRVCTRL |= TCC_DRVCTRL_FILTERVAL0(${TCC_DRVCTRL_FILTERVAL}UL)
          | TCC_DRVCTRL_FILTERVAL1(${TCC_DRVCTRL_FILTERVAL1}UL)<#rt>
                <#lt><#if TCC_DRVCTRL_FAULT_VAL?has_content>| ${TCC_DRVCTRL_FAULT_VAL}</#if>;
</#if>
<#if TCC_INTENSET_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTENSET = ${TCC_INTENSET_VAL};
</#if>

<#if TCC_EVCTRL_VAL?has_content>
    ${TCC_INSTANCE_NAME}_REGS->TCC_EVCTRL = ${TCC_EVCTRL_VAL};
</#if>
    while (${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY != 0U)
    {
        /* Wait for sync */
    }
}


/* Start the PWM generation */
void ${TCC_INSTANCE_NAME}_PWMStart(void)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA |= TCC_CTRLA_ENABLE_Msk;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_ENABLE_Msk) == TCC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for sync */
    }
}

/* Stop the PWM generation */
void ${TCC_INSTANCE_NAME}_PWMStop (void)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLA &= ~TCC_CTRLA_ENABLE_Msk;
    while((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_ENABLE_Msk) == TCC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for sync */
    }
}

/* Configure PWM period */
<#if TCC_SIZE == 24>
bool ${TCC_INSTANCE_NAME}_PWM24bitPeriodSet (uint32_t period)
{
    bool status = false;
    if ((${TCC_INSTANCE_NAME}_REGS->TCC_STATUS & (TCC_STATUS_${TCC_PBUF_REG_NAME}V_Msk)) == 0U)
    {
        ${TCC_INSTANCE_NAME}_REGS->TCC_${TCC_PBUF_REG_NAME} = period & 0xFFFFFFU;
        status = true;
    }    
    return status;
}

<#elseif TCC_SIZE == 16>
bool ${TCC_INSTANCE_NAME}_PWM16bitPeriodSet (uint16_t period)
{
    bool status = false;
    if ((${TCC_INSTANCE_NAME}_REGS->TCC_STATUS & (TCC_STATUS_${TCC_PBUF_REG_NAME}V_Msk)) == 0U)
    {
        ${TCC_INSTANCE_NAME}_REGS->TCC_${TCC_PBUF_REG_NAME} = period;
        status = true;
    }    
    return status;
}
<#elseif TCC_SIZE == 32>
bool ${TCC_INSTANCE_NAME}_PWM32bitPeriodSet (uint32_t period)
{
    bool status = false;
    if ((${TCC_INSTANCE_NAME}_REGS->TCC_STATUS & (TCC_STATUS_${TCC_PBUF_REG_NAME}V_Msk)) == 0U)
    {
        ${TCC_INSTANCE_NAME}_REGS->TCC_${TCC_PBUF_REG_NAME} = period;
        status = true;
    }    
    return status;
}
</#if>

/* Read TCC period */
<#if TCC_SIZE == 24>
uint32_t ${TCC_INSTANCE_NAME}_PWM24bitPeriodGet (void)
{
    while ((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_PER_Msk) == TCC_SYNCBUSY_PER_Msk)
    {
        /* Wait for sync */
    }
    return (${TCC_INSTANCE_NAME}_REGS->TCC_PER & 0xFFFFFFU);
}
<#elseif TCC_SIZE == 16>
uint16_t ${TCC_INSTANCE_NAME}_PWM16bitPeriodGet (void)
{
    while ((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_PER_Msk) == TCC_SYNCBUSY_PER_Msk)
    {
        /* Wait for sync */
    }
    return (uint16_t)${TCC_INSTANCE_NAME}_REGS->TCC_PER;
}
<#elseif TCC_SIZE == 32>
uint32_t ${TCC_INSTANCE_NAME}_PWM32bitPeriodGet (void)
{
    while ((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_PER_Msk) == TCC_SYNCBUSY_PER_Msk)
    {
        /* Wait for sync */
    }
    return (${TCC_INSTANCE_NAME}_REGS->TCC_PER);
}
</#if>

<#if TCC_IS_DEAD_TIME gte 1>
/* Configure dead time */
void ${TCC_INSTANCE_NAME}_PWMDeadTimeSet (uint8_t deadtime_high, uint8_t deadtime_low)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_WEXCTRL &= ~(TCC_WEXCTRL_DTHS_Msk | TCC_WEXCTRL_DTLS_Msk);
    ${TCC_INSTANCE_NAME}_REGS->TCC_WEXCTRL |= TCC_WEXCTRL_DTHS((uint32_t)deadtime_high) | TCC_WEXCTRL_DTLS((uint32_t)deadtime_low);
}
</#if>

<#if TCC_IS_PG == 1>
bool ${TCC_INSTANCE_NAME}_PWMPatternSet(uint8_t pattern_enable, uint8_t pattern_output)
{
    bool status = false;
    if ((${TCC_INSTANCE_NAME}_REGS->TCC_STATUS & (TCC_STATUS_${TCC_PATBUF_REG_NAME}V_Msk)) == 0U)
    {
        ${TCC_INSTANCE_NAME}_REGS->TCC_${TCC_PATBUF_REG_NAME} = (uint16_t)(pattern_enable | ((uint32_t)pattern_output << 8U));
        status = true;
    }   
    return status; 
}

</#if>


<#if TCC_SIZE == 24>
/* Get the current counter value */
uint32_t ${TCC_INSTANCE_NAME}_PWM24bitCounterGet( void )
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

/* Set the counter*/
void ${TCC_INSTANCE_NAME}_PWM24bitCounterSet (uint32_t countVal)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_COUNT = countVal & 0xFFFFFFU;
    while ((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_COUNT_Msk) == TCC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for sync */
    }
}
<#elseif TCC_SIZE == 16>
/* Get the current counter value */
uint16_t ${TCC_INSTANCE_NAME}_PWM16bitCounterGet( void )
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

/* Set the counter*/
void ${TCC_INSTANCE_NAME}_PWM16bitCounterSet (uint16_t countVal)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_COUNT = countVal;
    while ((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_COUNT_Msk) == TCC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for sync */
    }
}
<#elseif TCC_SIZE == 32>
/* Get the current counter value */
uint32_t ${TCC_INSTANCE_NAME}_PWM32bitCounterGet( void )
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

/* Set the counter*/
void ${TCC_INSTANCE_NAME}_PWM32bitCounterSet (uint32_t countVal)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_COUNT = countVal;
    while ((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_COUNT_Msk) == TCC_SYNCBUSY_COUNT_Msk)
    {
        /* Wait for sync */
    }
}
</#if>

/* Enable forced synchronous update */
void ${TCC_INSTANCE_NAME}_PWMForceUpdate(void)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_CTRLBSET |= (uint8_t)TCC_CTRLBCLR_CMD_UPDATE;
    while ((${TCC_INSTANCE_NAME}_REGS->TCC_SYNCBUSY & TCC_SYNCBUSY_CTRLB_Msk) == TCC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for sync */
    }
}

/* Enable the period interrupt - overflow or underflow interrupt */
void ${TCC_INSTANCE_NAME}_PWMPeriodInterruptEnable(void)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTENSET = TCC_INTENSET_OVF_Msk;
}

/* Disable the period interrupt - overflow or underflow interrupt */
void ${TCC_INSTANCE_NAME}_PWMPeriodInterruptDisable(void)
{
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTENCLR = TCC_INTENCLR_OVF_Msk;
}

<#if TCC_INTERRUPT == true>
    <#lt> /* Register callback function */
    <#lt>void ${TCC_INSTANCE_NAME}_PWMCallbackRegister(TCC_CALLBACK callback, uintptr_t context)
    <#lt>{
    <#lt>    ${TCC_INSTANCE_NAME}_CallbackObj.callback_fn = callback;
    <#lt>    ${TCC_INSTANCE_NAME}_CallbackObj.context = context;
    <#lt>}

    <#if TCC_NUM_INT_LINES != 0>
        <#if TCC_INTENSET_OVF == true || TCC_INTENSET_FAULT0 == true || TCC_INTENSET_FAULT1 == true>
            <#lt>/* Interrupt Handler */
            <#lt>void __attribute__((used)) ${TCC_INSTANCE_NAME}_OTHER_InterruptHandler(void)
            <#lt>{
            <#lt>    uint32_t status;
            <#lt>    /* Additional local variable to prevent MISRA C violations (Rule 13.x) */
            <#lt>    uintptr_t context;
            <#lt>    context = ${TCC_INSTANCE_NAME}_CallbackObj.context;            
            <#lt>    status = (${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG & 0xFFFFU);
            <#lt>    /* Clear interrupt flags */
            <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = 0xFFFFU;
            <#lt>    (void)${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
            <#lt>    if (${TCC_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
            <#lt>    {
            <#lt>        ${TCC_INSTANCE_NAME}_CallbackObj.callback_fn(status, context);
            <#lt>    }

            <#lt>}
        </#if>

        <#list 0..(TCC_NUM_CHANNELS-1) as i>
        <#assign TCC_INT_MC = "TCC_INTENSET_MC_" + i>
            <#if .vars[TCC_INT_MC] == true>
                <#lt>/* Interrupt Handler */
                <#lt>void __attribute__((used)) ${TCC_INSTANCE_NAME}_MC${i}_InterruptHandler(void)
                <#lt>{
                <#lt>    uint32_t status;
                <#lt>    /* Additional local variable to prevent MISRA C violations (Rule 13.x) */
                <#lt>    uintptr_t context;
                <#lt>    context = ${TCC_INSTANCE_NAME}_CallbackObj.context;                
                <#lt>    status = TCC_INTFLAG_MC${i}_Msk;
                <#lt>    /* Clear interrupt flags */
                <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_MC${i}_Msk;
                <#lt>    (void)${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
                <#lt>    if (${TCC_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
                <#lt>    {
                <#lt>        ${TCC_INSTANCE_NAME}_CallbackObj.callback_fn(status, context);
                <#lt>    }

                <#lt>}
            </#if>
        </#list>

    <#else>  <#-- TCC_NUM_INT_LINES -->
        <#lt>/* Interrupt Handler */
        <#lt>void __attribute__((used)) ${TCC_INSTANCE_NAME}_InterruptHandler(void)
        <#lt>{
        <#lt>    uint32_t status;
        <#lt>    /* Additional local variable to prevent MISRA C violations (Rule 13.x) */
        <#lt>    uintptr_t context;
        <#lt>    context = ${TCC_INSTANCE_NAME}_CallbackObj.context;        
        <#lt>    status = ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
        <#lt>    /* Clear interrupt flags */
        <#lt>    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = TCC_INTFLAG_Msk;
        <#lt>    (void)${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
        <#lt>    if (${TCC_INSTANCE_NAME}_CallbackObj.callback_fn != NULL)
        <#lt>    {
        <#lt>        ${TCC_INSTANCE_NAME}_CallbackObj.callback_fn(status, context);
        <#lt>    }

        <#lt>}
    </#if> <#-- TCC_NUM_INT_LINES -->

<#else>
/* Read interrupt flags */
uint32_t ${TCC_INSTANCE_NAME}_PWMInterruptStatusGet(void)
{
    uint32_t interrupt_status;
    interrupt_status = ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
    /* Clear interrupt flags */
    ${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG = interrupt_status;
    (void)${TCC_INSTANCE_NAME}_REGS->TCC_INTFLAG;
    return interrupt_status;
}
</#if>


/**
 End of File
*/
