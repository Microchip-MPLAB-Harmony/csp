/*******************************************************************************
  ADC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADC_INSTANCE_NAME?lower_case}.c

  Summary
    ${ADC_INSTANCE_NAME} peripheral library source.

  Description
    This file implements the ADC peripheral library.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
#include "device.h"
#include "plib_${ADC_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${ADC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

/* Load ADC calibration constant */
#define ADC_CALIB_FCCFG65           *((uint32_t*)0x0A007184)

<#if ADC_CTLINTENSET != "0">
ADC_GLOBAL_CALLBACK_OBJECT ${ADC_INSTANCE_NAME}_GlobalCallbackObj;
</#if>

<#if ADC_CORE_CORE_INT_ENABLED == true>
ADC_CORE_CALLBACK_OBJECT ${ADC_INSTANCE_NAME}_CoreCallbackObj[${ADC_NUM_SAR_CORES}];
</#if>

void ${ADC_INSTANCE_NAME}_Initialize(void)
{
    /* Copy calibration value for all the enabled ADC cores */
    <#list 0..(ADC_NUM_SAR_CORES-1) as n>
    <#assign ADC_CORE_ENABLED    = "ADC_CORE_" + n + "_ENABLE">
    <#if .vars[ADC_CORE_ENABLED] == true>
    ${ADC_INSTANCE_NAME}_REGS->CONFIG[${n}].ADC_CALCTRL = ADC_CALIB_FCCFG65;
    </#if>
    </#list>

    <#if ADC_CTRLA != "0">
    /*
    ONDEMAND = ${ADC_GLOBAL_CTRLA_ONDEMAND?c}
    RUNSTDBY = ${ADC_GLOBAL_CTRLA_RUNSTDBY?c}
    ANAEN = 1
    */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA = 0x${ADC_CTRLA?upper_case};
    </#if>

    <#if ADC_CTRLD != "0">
    /*
    VREFSEL = ${ADC_GLOBAL_CTRLD_VREFSEL}
    WKUPEXP = ${ADC_GLOBAL_CTRLD_WKUPEXP}
    CTLCKDIV = ${ADC_GLOBAL_CTRLD_CTLCKDIV}
    */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLD = 0x${ADC_CTRLD?upper_case};
    </#if>

    <#if ADC_CTLINTENSET != "0">
    /* Enable ADC Global interrupts -
    PFFHFUL = ${ADC_GLOBAL_CTLINTENSET_PFFHFUL?c}
    PFFRDY = ${ADC_GLOBAL_CTLINTENSET_PFFRDY?c}
    PFFOVF = ${ADC_GLOBAL_CTLINTENSET_PFFOVF?c}
    PFFUNF = ${ADC_GLOBAL_CTLINTENSET_PFFUNF?c}
    VREFRDY = ${ADC_GLOBAL_CTLINTENSET_VREFRDY?c}
    VREFUPD = ${ADC_GLOBAL_CTLINTENSET_VREFUPD?c}
    */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTLINTENSET = 0x${ADC_CTLINTENSET?upper_case};
    </#if>

    <#list 0..(ADC_NUM_SAR_CORES-1) as n>
        <#assign ADC_CORE_ENABLED    = "ADC_CORE_" + n + "_ENABLE">
        <#assign ADC_INTENSET        = "ADC_CORE_" + n + "_ADC_INTENSET">
        <#assign ADC_CORCTRL         = "ADC_CORE_" + n + "_ADC_CORCTRL">
        <#assign ADC_CHNCFG1         = "ADC_CORE_" + n + "_ADC_CHNCFG1">
        <#assign ADC_CHNCFG2         = "ADC_CORE_" + n + "_ADC_CHNCFG2">
        <#assign ADC_CHNCFG3         = "ADC_CORE_" + n + "_ADC_CHNCFG3">
        <#assign ADC_CHNCFG4         = "ADC_CORE_" + n + "_ADC_CHNCFG4">
        <#assign ADC_CHNCFG5         = "ADC_CORE_" + n + "_ADC_CHNCFG5">
        <#assign ADC_CMPCTRL         = "ADC_CORE_" + n + "_ADC_CMPCTRL">
        <#assign ADC_FLTCTRL         = "ADC_CORE_" + n + "_ADC_FLTCTRL">
        <#assign ADC_EVCTRL          = "ADC_CORE_" + n + "_ADC_EVCTRL">

        <#assign ADC_INTENSET_EOSRDY = "ADC_CORE_" + n + "_INTENSET_EOSRDY">
        <#assign ADC_INTENSET_CHNERRC = "ADC_CORE_" + n + "_INTENSET_CHNERRC">
        <#assign ADC_INTENSET_FLTRDY = "ADC_CORE_" + n + "_INTENSET_FLTRDY">
        <#assign ADC_INTENSET_CMPHIT = "ADC_CORE_" + n + "_INTENSET_CMPHIT">

        <#assign ADC_CORCTRL_ADCDIV = "ADC_CORE_" + n + "_CORCTRL_ADCDIV">
        <#assign ADC_CORCTRL_STRGLVL = "ADC_CORE_" + n + "_CORCTRL_STRGLVL">
        <#assign ADC_CORCTRL_STRGSRC = "ADC_CORE_" + n + "_CORCTRL_STRGSRC">
        <#assign ADC_CORCTRL_EIRQOVR = "ADC_CORE_" + n + "_CORCTRL_EIRQOVR">
        <#assign ADC_CORCTRL_EIS = "ADC_CORE_" + n + "_CORCTRL_EIS">
        <#assign ADC_CORCTRL_SELRES = "ADC_CORE_" + n + "_CORCTRL_SELRES">
        <#assign ADC_CORCTRL_SAMC = "ADC_CORE_" + n + "_CORCTRL_SAMC">

        <#assign ADC_EVCTRL_CMPEO = "ADC_CORE_" + n + "_EVCTRL_CMPEO">
        <#assign ADC_EVCTRL_RESRDYEO = "ADC_CORE_" + n + "_EVCTRL_RESRDYEO">
        <#assign ADC_EVCTRL_STARTEI = "ADC_CORE_" + n + "_EVCTRL_STARTEI">

        <#assign ADC_CMPCTRL_IEHIHI = "ADC_CORE_" + n + "_CMPCTRL_IEHIHI">
        <#assign ADC_CMPCTRL_IEHILO = "ADC_CORE_" + n + "_CMPCTRL_IEHILO">
        <#assign ADC_CMPCTRL_ADCMPHI = "ADC_CORE_" + n + "_CMPCTRL_ADCMPHI">
        <#assign ADC_CMPCTRL_IEBTWN = "ADC_CORE_" + n + "_CMPCTRL_IEBTWN">
        <#assign ADC_CMPCTRL_IELOHI = "ADC_CORE_" + n + "_CMPCTRL_IELOHI">
        <#assign ADC_CMPCTRL_IELOLO = "ADC_CORE_" + n + "_CMPCTRL_IELOLO">
        <#assign ADC_CMPCTRL_CMPEN = "ADC_CORE_" + n + "_CMPCTRL_CMPEN">
        <#assign ADC_CMPCTRL_ADCMPLO = "ADC_CORE_" + n + "_CMPCTRL_ADCMPLO">

        <#assign ADC_FLTCTRL_FLTCHNID = "ADC_CORE_" + n + "_FLTCTRL_FLTCHNID">
        <#assign ADC_FLTCTRL_FLTEN = "ADC_CORE_" + n + "_FLTCTRL_FLTEN">
        <#assign ADC_FLTCTRL_FMODE = "ADC_CORE_" + n + "_FLTCTRL_FMODE">
        <#assign ADC_FLTCTRL_OVRSAM = "ADC_CORE_" + n + "_FLTCTRL_OVRSAM">

        <#if .vars[ADC_CORE_ENABLED] == true>
            <#if .vars[ADC_INTENSET] != "0">
            <#lt>    /* Enable ADC Core ${n} interrupts
            <#lt>       EOSRDY = ${.vars[ADC_INTENSET_EOSRDY]?c}
            <#lt>       CHNERRC = ${.vars[ADC_INTENSET_CHNERRC]?c}
            <#lt>       FLTRDY = ${.vars[ADC_INTENSET_FLTRDY]?c}
            <#lt>       CMPHIT = ${.vars[ADC_INTENSET_CMPHIT]?c}
            <#lt>    */
            <#lt>    ${ADC_INSTANCE_NAME}_REGS->INT[${n}].ADC_INTENSET = 0x${.vars[ADC_INTENSET]?upper_case};
            </#if>

            <#if .vars[ADC_CORCTRL] != "0">
            <#lt>    /* Configure ADC Core ${n} Control Register
            <#lt>       ADCDIV = ${.vars[ADC_CORCTRL_ADCDIV]}
            <#lt>       STRGLVL = ${.vars[ADC_CORCTRL_STRGLVL]}
            <#lt>       STRGSRC = ${.vars[ADC_CORCTRL_STRGSRC]}
            <#lt>       EIRQOVR = ${.vars[ADC_CORCTRL_EIRQOVR]?c}
            <#lt>       EIS = ${.vars[ADC_CORCTRL_EIS]}
            <#lt>       SELRES = ${.vars[ADC_CORCTRL_SELRES]}
            <#lt>       SAMC = ${.vars[ADC_CORCTRL_SAMC]}
            <#lt>    */
            <#lt>    ${ADC_INSTANCE_NAME}_REGS->CONFIG[${n}].ADC_CORCTRL = 0x${.vars[ADC_CORCTRL]?upper_case};
            </#if>

            <#if .vars[ADC_CHNCFG1] != "0">
            <#lt>    /* Configure ADC Core ${n} Channel Configuration Register 1 */
            <#lt>    ${ADC_INSTANCE_NAME}_REGS->CONFIG[${n}].ADC_CHNCFG1 = 0x${.vars[ADC_CHNCFG1]?upper_case};
            </#if>

            <#if .vars[ADC_CHNCFG2] != "0">
            <#lt>    /* Configure ADC Core ${n} Channel Configuration Register 2 */
            <#lt>    ${ADC_INSTANCE_NAME}_REGS->CONFIG[${n}].ADC_CHNCFG2 = 0x${.vars[ADC_CHNCFG2]?upper_case};
            </#if>

            <#if .vars[ADC_CHNCFG3] != "0">
            <#lt>    /* Configure ADC Core ${n} Channel Configuration Register 3 */
            <#lt>    ${ADC_INSTANCE_NAME}_REGS->CONFIG[${n}].ADC_CHNCFG3 = 0x${.vars[ADC_CHNCFG3]?upper_case};
            </#if>

            <#if .vars[ADC_CHNCFG4] != "0">
            <#lt>    /* Configure ADC Core ${n} Channel Configuration Register 4 */
            <#lt>    ${ADC_INSTANCE_NAME}_REGS->CONFIG[${n}].ADC_CHNCFG4 = 0x${.vars[ADC_CHNCFG4]?upper_case};
            </#if>

            <#if .vars[ADC_CHNCFG5] != "0">
            <#lt>    /* Configure ADC Core ${n} Channel Configuration Register 5 */
            <#lt>    ${ADC_INSTANCE_NAME}_REGS->CONFIG[${n}].ADC_CHNCFG5 = 0x${.vars[ADC_CHNCFG5]?upper_case};
            </#if>

            <#if .vars[ADC_EVCTRL] != "0">
            <#lt>    /* Configure ADC Core ${n} Event Control Register
            <#lt>       CMPEO = ${.vars[ADC_EVCTRL_CMPEO]?c}
            <#lt>       RESRDYEO = ${.vars[ADC_EVCTRL_RESRDYEO]?c}
            <#lt>       STARTEI = ${.vars[ADC_EVCTRL_STARTEI]?c}
            <#lt>    */
            <#lt>    ${ADC_INSTANCE_NAME}_REGS->CONFIG[${n}].ADC_EVCTRL = 0x${.vars[ADC_EVCTRL]?upper_case};
            </#if>

            <#if .vars[ADC_CMPCTRL] != "0">
            <#lt>    /* Configure ADC Core ${n} Comparator Control Register
            <#lt>       IEHILO = ${.vars[ADC_CMPCTRL_IEHIHI]?c}
            <#lt>       IEHILO = ${.vars[ADC_CMPCTRL_IEHILO]?c}
            <#lt>       ADCMPHI = ${.vars[ADC_CMPCTRL_ADCMPHI]}
            <#lt>       IEBTWN = ${.vars[ADC_CMPCTRL_IEBTWN]?c}
            <#lt>       IELOHI = ${.vars[ADC_CMPCTRL_IELOHI]?c}
            <#lt>       IELOLO = ${.vars[ADC_CMPCTRL_IELOLO]?c}
            <#lt>       CMPEN = ${.vars[ADC_CMPCTRL_CMPEN]?c}
            <#lt>       ADCMPLO = ${.vars[ADC_CMPCTRL_ADCMPLO]}
            <#lt>    */
					<#if ADC_NUM_SAR_CORES == 1 >
						${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL = 0x${.vars[ADC_CMPCTRL]?upper_case};
					<#else>
						${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL[${n}] = 0x${.vars[ADC_CMPCTRL]?upper_case};
					</#if>	
            </#if>

            <#if .vars[ADC_FLTCTRL] != "0">
            <#lt>    /* Configure ADC Core ${n} Filter Control Register
            <#lt>       FLTCHNID = ${.vars[ADC_FLTCTRL_FLTCHNID]}
            <#lt>       FLTEN = ${.vars[ADC_FLTCTRL_FLTEN]?c}
            <#lt>       FMODE = ${.vars[ADC_FLTCTRL_FMODE]}
            <#lt>       OVRSAM = ${.vars[ADC_FLTCTRL_OVRSAM]}
            <#lt>    */
                    <#if ADC_NUM_SAR_CORES == 1>
						${ADC_INSTANCE_NAME}_REGS->ADC_FLTCTRL = 0x${.vars[ADC_FLTCTRL]?upper_case};
					<#else>
						${ADC_INSTANCE_NAME}_REGS->ADC_FLTCTRL[${n}] = 0x${.vars[ADC_FLTCTRL]?upper_case};
					</#if>	
            </#if>
        </#if>
    </#list>

    <#if ADC_PFFCTRL != "0">
    ${ADC_INSTANCE_NAME}_REGS->ADC_PFFCTRL = 0x${ADC_PFFCTRL?upper_case};
    </#if>

    <#if ADC_CTRLC != "0">
    /*
	<#if ADC_GLOBAL_CTRLC_COREINTERLEAVED?? >
    COREINTERLEAVED = ${ADC_GLOBAL_CTRLC_COREINTERLEAVED}
	</#if>
    CNT = ${ADC_GLOBAL_CTRLC_CNT}
    */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLC = 0x${ADC_CTRLC?upper_case};
    </#if>

    /* Analog and bias circuitry enable for the ADC SAR Core n (ANLEN) */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLD |= 0x${ADC_CTRLD__ANLEN?upper_case}U;

    /* Enable the ADC Core n modules digital interface (CHNEN) */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLD |= 0x${ADC_CTRLD__CHNEN}U;

    /*Enable ADC module */
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLA |= ADC_CTRLA_ENABLE_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }

    /* Wait for WKUPEXP delay to expire after which ADC SAR Core n is Ready (CRDY) */
    while ((${ADC_INSTANCE_NAME}_REGS->ADC_CTLINTFLAG & 0x${ADC_CTLINTFLAG__CRDY?upper_case}U) == 0U)
    {

    }

    /* Wait for voltage reference to be stable */
    while ((${ADC_INSTANCE_NAME}_REGS->ADC_CTLINTFLAG & ADC_CTLINTFLAG_VREFRDY_Msk) == 0U)
    {

    }

}

<#if ADC_NUM_SAR_CORES == 1>
/* Enable channel compare mode */
void ${ADC_INSTANCE_NAME}_CompareEnable(ADC_CHANNEL_NUM channel)
{
	${ADC_INSTANCE_NAME}_Disable();

	${ADC_INSTANCE_NAME}_REGS->CONFIG[0].ADC_CHNCFG1 |= (1UL << (uint32_t)channel);

	${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL |= ADC_CMPCTRL_CMPEN_Msk;
	
	${ADC_INSTANCE_NAME}_Enable();
}
	
/* Disable channel compare mode */
void ${ADC_INSTANCE_NAME}_CompareDisable(ADC_CHANNEL_NUM channel)
{
	${ADC_INSTANCE_NAME}_Disable();

	${ADC_INSTANCE_NAME}_REGS->CONFIG[0].ADC_CHNCFG1 &= ~(1UL << (uint32_t)channel);

	${ADC_INSTANCE_NAME}_Enable();
}

/* Configure window comparison threshold values */
void ${ADC_INSTANCE_NAME}_CompareWinThresholdSet(uint16_t low_threshold, uint16_t high_threshold)
{
	${ADC_INSTANCE_NAME}_Disable();

	${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL = (${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL & ~(ADC_CMPCTRL_ADCMPHI_Msk | ADC_CMPCTRL_ADCMPLO_Msk)) | ((low_threshold << ADC_CMPCTRL_ADCMPLO_Pos) | (high_threshold << ADC_CMPCTRL_ADCMPHI_Pos));

	${ADC_INSTANCE_NAME}_Enable();
}

/* Configure window comparison event mode */
void ${ADC_INSTANCE_NAME}_CompareWinModeSet(ADC_CMPCTRL mode)
{
	${ADC_INSTANCE_NAME}_Disable();
	
	${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL = (${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL & ~(ADC_CMPCTRL_IELOLO_Msk | ADC_CMPCTRL_IELOHI_Msk | ADC_CMPCTRL_IEBTWN_Msk | ADC_CMPCTRL_IEHILO_Msk | ADC_CMPCTRL_IEHIHI_Msk)) | mode;
	
	${ADC_INSTANCE_NAME}_Enable();
}

void ${ADC_INSTANCE_NAME}_CoreInterruptsEnable(ADC_CORE_INT interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->INT[0].ADC_INTENSET = interruptMask;
}

void ${ADC_INSTANCE_NAME}_CoreInterruptsDisable(ADC_CORE_INT interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->INT[0].ADC_INTENCLR = interruptMask;
}

ADC_CORE_INT ${ADC_INSTANCE_NAME}_CoreInterruptsStatusGet(void)
{
    return ${ADC_INSTANCE_NAME}_REGS->INT[0].ADC_INTFLAG;
}

void ${ADC_INSTANCE_NAME}_CoreInterruptsStatusClear(ADC_CORE_INT interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->INT[0].ADC_INTFLAG = interruptMask;
}

void ${ADC_INSTANCE_NAME}_SoftwareControlledConversionEnable(ADC_CHANNEL_NUM channel)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB = (${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB & ~(ADC_CTRLB_ADCHSEL_Msk)) | ((uint32_t)channel << ADC_CTRLB_ADCHSEL_Pos);

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }

    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB |= ADC_CTRLB_SWCNVEN_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }
}

bool ${ADC_INSTANCE_NAME}_ChannelResultIsReady(ADC_CHANNEL_NUM channel)
{
    return (bool)((${ADC_INSTANCE_NAME}_REGS->INT[0].ADC_INTFLAG & (1UL << (ADC_INTFLAG_CHRDY_Pos + (uint32_t)channel))) != 0U);
}

bool ${ADC_INSTANCE_NAME}_EOSStatusGet(void)
{
    return (bool)((${ADC_INSTANCE_NAME}_REGS->INT[0].ADC_INTFLAG & ADC_INTFLAG_EOSRDY_Msk) == ADC_INTFLAG_EOSRDY_Msk);
}

/* Read the conversion result for the given channel */
uint32_t ${ADC_INSTANCE_NAME}_ResultGet(ADC_CHANNEL_NUM channel)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CORCHDATAID = (${ADC_INSTANCE_NAME}_REGS->ADC_CORCHDATAID & ~(ADC_CORCHDATAID_CHRDYID_Msk)) | ((uint32_t)channel);

    return ${ADC_INSTANCE_NAME}_REGS->ADC_CHRDYDAT;
}
<#else>
/* Enable channel compare mode */
void ${ADC_INSTANCE_NAME}_CompareEnable(ADC_CORE_NUM core, ADC_CHANNEL_NUM channel)
{
	${ADC_INSTANCE_NAME}_Disable();

	${ADC_INSTANCE_NAME}_REGS->CONFIG[core].ADC_CHNCFG1 |= (1UL << (uint32_t)channel);

	${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL[core] |= ADC_CMPCTRL_CMPEN_Msk;
	
	${ADC_INSTANCE_NAME}_Enable();
}


/* Disable channel compare mode */
void ${ADC_INSTANCE_NAME}_CompareDisable(ADC_CORE_NUM core, ADC_CHANNEL_NUM channel)
{
	${ADC_INSTANCE_NAME}_Disable();

	${ADC_INSTANCE_NAME}_REGS->CONFIG[core].ADC_CHNCFG1 &= ~(1UL << (uint32_t)channel);

	${ADC_INSTANCE_NAME}_Enable();
}

/* Configure window comparison threshold values */
void ${ADC_INSTANCE_NAME}_CompareWinThresholdSet(ADC_CORE_NUM core, uint16_t low_threshold, uint16_t high_threshold)
{
	${ADC_INSTANCE_NAME}_Disable();

	${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL[core] = (${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL[core] & ~(ADC_CMPCTRL_ADCMPHI_Msk | ADC_CMPCTRL_ADCMPLO_Msk)) | ((low_threshold << ADC_CMPCTRL_ADCMPLO_Pos) | (high_threshold << ADC_CMPCTRL_ADCMPHI_Pos));
	
	${ADC_INSTANCE_NAME}_Enable();
}

/* Configure window comparison event mode */
void ${ADC_INSTANCE_NAME}_CompareWinModeSet(ADC_CORE_NUM core, ADC_CMPCTRL mode)
{
	${ADC_INSTANCE_NAME}_Disable();
	
	${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL[core] = (${ADC_INSTANCE_NAME}_REGS->ADC_CMPCTRL[core] & ~(ADC_CMPCTRL_IELOLO_Msk | ADC_CMPCTRL_IELOHI_Msk | ADC_CMPCTRL_IEBTWN_Msk | ADC_CMPCTRL_IEHILO_Msk | ADC_CMPCTRL_IEHIHI_Msk)) | mode;
	
	${ADC_INSTANCE_NAME}_Enable();
}

void ${ADC_INSTANCE_NAME}_CoreInterruptsEnable(ADC_CORE_NUM core, ADC_CORE_INT interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->INT[core].ADC_INTENSET = interruptMask;
}

void ${ADC_INSTANCE_NAME}_CoreInterruptsDisable(ADC_CORE_NUM core, ADC_CORE_INT interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->INT[core].ADC_INTENCLR = interruptMask;
}

ADC_CORE_INT ${ADC_INSTANCE_NAME}_CoreInterruptsStatusGet(ADC_CORE_NUM core)
{
    return ${ADC_INSTANCE_NAME}_REGS->INT[core].ADC_INTFLAG;
}

void ${ADC_INSTANCE_NAME}_CoreInterruptsStatusClear(ADC_CORE_NUM core, ADC_CORE_INT interruptMask)
{
    ${ADC_INSTANCE_NAME}_REGS->INT[core].ADC_INTFLAG = interruptMask;
}

void ${ADC_INSTANCE_NAME}_SoftwareControlledConversionEnable(ADC_CORE_NUM core, ADC_CHANNEL_NUM channel)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB = (${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB & ~(ADC_CTRLB_ADCORSEL_Msk | ADC_CTRLB_ADCHSEL_Msk)) | (((uint32_t)core << ADC_CTRLB_ADCORSEL_Pos) | ((uint32_t)channel << ADC_CTRLB_ADCHSEL_Pos));

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }

    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB |= ADC_CTRLB_SWCNVEN_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }
}

bool ${ADC_INSTANCE_NAME}_ChannelResultIsReady(ADC_CORE_NUM core, ADC_CHANNEL_NUM channel)
{
    return (bool)((${ADC_INSTANCE_NAME}_REGS->INT[core].ADC_INTFLAG & (1UL << (ADC_INTFLAG_CHRDY_Pos + (uint32_t)channel))) != 0U);
}

bool ${ADC_INSTANCE_NAME}_EOSStatusGet(ADC_CORE_NUM core)
{
    return (bool)((${ADC_INSTANCE_NAME}_REGS->INT[core].ADC_INTFLAG & ADC_INTFLAG_EOSRDY_Msk) == ADC_INTFLAG_EOSRDY_Msk);
}

/* Read the conversion result for the given core, channel */
uint32_t ${ADC_INSTANCE_NAME}_ResultGet( ADC_CORE_NUM core, ADC_CHANNEL_NUM channel)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CORCHDATAID = (${ADC_INSTANCE_NAME}_REGS->ADC_CORCHDATAID & ~(ADC_CORCHDATAID_CORDYID_Msk | ADC_CORCHDATAID_CHRDYID_Msk)) | (((uint32_t)core << ADC_CORCHDATAID_CORDYID_Pos) | (uint32_t)channel);

    return ${ADC_INSTANCE_NAME}_REGS->ADC_CHRDYDAT;
}
</#if>

ADC_GLOBAL_INT ${ADC_INSTANCE_NAME}_GlobalInterruptsStatusGet(void)
{
    return ${ADC_INSTANCE_NAME}_REGS->ADC_CTLINTFLAG;
}

void ${ADC_INSTANCE_NAME}_GlobalEdgeConversionStart(void)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB |= ADC_CTRLB_GSWTRG_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }
}

void ${ADC_INSTANCE_NAME}_GlobalLevelConversionStart(void)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB |= ADC_CTRLB_LSWTRG_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }
}

void ${ADC_INSTANCE_NAME}_GlobalLevelConversionStop(void)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB &= ~ADC_CTRLB_LSWTRG_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }
}

void ${ADC_INSTANCE_NAME}_SyncTriggerEnable(void)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB |= (1UL<<11U);

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }
}

void ${ADC_INSTANCE_NAME}_SyncTriggerDisable(void)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB &= ~(1UL<<11U);

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }
}


void ${ADC_INSTANCE_NAME}_SyncTriggerCounterSet(uint16_t counterVal)
{
    ${ADC_INSTANCE_NAME}_Disable();

    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLC = (${ADC_INSTANCE_NAME}_REGS->ADC_CTRLC & ~ADC_CTRLC_CNT_Msk) | (counterVal);

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }

    ${ADC_INSTANCE_NAME}_Enable();
}

void ${ADC_INSTANCE_NAME}_ChannelSamplingStart(void)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB |= ADC_CTRLB_SAMP_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }
}

void ${ADC_INSTANCE_NAME}_ChannelSamplingStop(void)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB &= ~ADC_CTRLB_SAMP_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }
}

void ${ADC_INSTANCE_NAME}_ChannelConversionStart(void)
{
    ${ADC_INSTANCE_NAME}_REGS->ADC_CTRLB |= ADC_CTRLB_RQCNVRT_Msk;

    while((${ADC_INSTANCE_NAME}_REGS->ADC_SYNCBUSY) != 0U)
    {
        /* Wait for Synchronization */
    }
}

<#if ADC_PFFCTRL != "0">
/* Read the conversion result for the given core, channel */
uint32_t ${ADC_INSTANCE_NAME}_FIFORead( void )
{
    return ${ADC_INSTANCE_NAME}_REGS->ADC_PFFDATA;
}

/* Read the conversion result for the given core, channel */
uint32_t ${ADC_INSTANCE_NAME}_FIFOBufferRead( uint32_t* pBuffer, uint32_t size )
{
    uint32_t count = 0;

    while ((${ADC_INSTANCE_NAME}_REGS->ADC_CTLINTFLAG & ADC_CTLINTFLAG_PFFRDY_Msk) && (count < size))
    {
        pBuffer[count++] = ${ADC_INSTANCE_NAME}_REGS->ADC_PFFDATA;
    }

    return count;
}
</#if>


<#if ADC_CTLINTENSET != "0">
void ${ADC_INSTANCE_NAME}_GlobalCallbackRegister(ADC_GLOBAL_CALLBACK callback, uintptr_t context)
{
    ${ADC_INSTANCE_NAME}_GlobalCallbackObj.callback = callback;
    ${ADC_INSTANCE_NAME}_GlobalCallbackObj.context = context;
}
</#if>

<#list 0..(ADC_NUM_SAR_CORES-1) as n>
        <#assign ADC_CORE_INT_ENABLED    = "ADC_CORE_" + n + "_ADC_INTENSET">
        <#if .vars[ADC_CORE_INT_ENABLED] != "0">
        <#lt>void ${ADC_INSTANCE_NAME}_CORE${n}CallbackRegister(ADC_CORE_CALLBACK callback, uintptr_t context)
        <#lt>{
        <#lt>   ${ADC_INSTANCE_NAME}_CoreCallbackObj[${n}].callback = callback;
        <#lt>   ${ADC_INSTANCE_NAME}_CoreCallbackObj[${n}].context = context;
        <#lt>}
        </#if>
</#list>

<#if ADC_CTLINTENSET != "0">
void ${ADC_INSTANCE_NAME}_GLOBAL_InterruptHandler( void )
{
    uint32_t status;

    status = ${ADC_INSTANCE_NAME}_REGS->ADC_CTLINTFLAG;

    /* Disable VREFRDY and CRRDYn interrupts to prevent continuous firing of ISR */
    if (status & (ADC_CTLINTFLAG_VREFRDY_Msk | ADC_CTLINTFLAG_CRRDY_Msk))
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_CTLINTENCLR = status & (ADC_CTLINTFLAG_VREFRDY_Msk | ADC_CTLINTFLAG_CRRDY_Msk);
    }

    /* ACK VREFUPD, PFFUNF and PFFOVM interrupts by clearing (writing 1) the interrupt flags */
    if (status & (ADC_CTLINTFLAG_VREFUPD_Msk | ADC_CTLINTFLAG_PFFUNF_Msk | ADC_CTLINTFLAG_PFFOVF_Msk))
    {
        ${ADC_INSTANCE_NAME}_REGS->ADC_CTLINTFLAG = status & (ADC_CTLINTFLAG_VREFUPD_Msk | ADC_CTLINTFLAG_PFFUNF_Msk | ADC_CTLINTFLAG_PFFOVF_Msk);
    }

    if (${ADC_INSTANCE_NAME}_GlobalCallbackObj.callback != NULL)
    {
        ${ADC_INSTANCE_NAME}_GlobalCallbackObj.callback(status, ${ADC_INSTANCE_NAME}_GlobalCallbackObj.context);
    }
}
</#if>

<#list 0..(ADC_NUM_SAR_CORES-1) as n>
        <#assign ADC_CORE_INT_ENABLED    = "ADC_CORE_" + n + "_ADC_INTENSET">
        <#if .vars[ADC_CORE_INT_ENABLED] != "0">
        <#lt>void ${ADC_INSTANCE_NAME}_CORE${n+1}_InterruptHandler( void )
        <#lt>{
        <#lt>   uint32_t status;

        <#lt>   status = ${ADC_INSTANCE_NAME}_REGS->INT[${n}].ADC_INTFLAG;

        <#lt>   /* Clear interrupt flag */
        <#lt>   ${ADC_INSTANCE_NAME}_REGS->INT[${n}].ADC_INTFLAG = status;

        <#lt>   if (${ADC_INSTANCE_NAME}_CoreCallbackObj[${n}].callback != NULL)
        <#lt>   {
        <#lt>       ${ADC_INSTANCE_NAME}_CoreCallbackObj[${n}].callback(status, ${ADC_INSTANCE_NAME}_CoreCallbackObj[${n}].context);
        <#lt>   }
        <#lt>}
        </#if>
</#list>


