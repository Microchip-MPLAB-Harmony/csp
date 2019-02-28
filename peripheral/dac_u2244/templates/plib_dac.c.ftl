/*******************************************************************************
  Digital-to-Analog Converter (${DAC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DAC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${DAC_INSTANCE_NAME} PLIB Implementation file

  Description:
    This file defines the interface to the DAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/
// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#include "plib_${DAC_INSTANCE_NAME?lower_case}.h"
#include "device.h"

<#assign DAC_OUT_MODE_AND_REF_SEL = "DAC_CTRLB_REFSEL (" + DAC_REFSEL + ")" + (DAC_OPERATING_MODE == "DIFFERENTIAL")?then(' | DAC_CTRLB_DIFF_Msk ','')>

<#assign DAC_CH_0_CTRL = "DAC_DACCTRL_ENABLE_Msk |" + " DAC_DACCTRL_CCTRL (" + DAC_CHANNEL_0_SPEED + ") " + (DAC_DATA_ADJUSTMENT0 == "LEFT-ADJUSTED")?then('| DAC_DACCTRL_LEFTADJ_Msk','') +
                          "| DAC_DACCTRL_REFRESH (" + DAC_CHANNEL_0_REFRESH + ") " + (DAC_CHANNEL_0_DITHER)?then(' | DAC_DACCTRL_DITHER_Msk ','') + 
						 							(DAC_CHANNEL_0_RSTDBY)?then('| DAC_DACCTRL_RUNSTDBY_Msk','')>
						   
<#assign DAC_CH_1_CTRL = "DAC_DACCTRL_ENABLE_Msk |" + " DAC_DACCTRL_CCTRL (" + DAC_CHANNEL_1_SPEED + ") " + (DAC_DATA_ADJUSTMENT1 == "LEFT-ADJUSTED")?then('| DAC_DACCTRL_LEFTADJ_Msk','') +
                        "| DAC_DACCTRL_REFRESH (" + DAC_CHANNEL_1_REFRESH + ") " +  (DAC_CHANNEL_1_DITHER)?then(' | DAC_DACCTRL_DITHER_Msk ','') + 
						 						(DAC_CHANNEL_1_RSTDBY)?then('| DAC_DACCTRL_RUNSTDBY_Msk','')>					   

<#assign DAC_CH_0_EVE_CTRL = (DAC_CHANNEL_EVENT_EMPTYEO0)?then(' | DAC_EVCTRL_EMPTYEO0_Msk','') + 
							 								(DAC_CHANNEL_EVENT_STARTEI0)?then(' | DAC_EVCTRL_STARTEI0_Msk','') + (DAC_CHANNEL_EVENT_INVEI0)?then(' | DAC_EVCTRL_INVEI0_Msk','')>

<#assign DAC_CH_1_EVE_CTRL = (DAC_CHANNEL_EVENT_EMPTYEO1)?then(' | DAC_EVCTRL_EMPTYEO1_Msk','') + 
							 (DAC_CHANNEL_EVENT_STARTEI1)?then(' | DAC_EVCTRL_STARTEI1_Msk','') + (DAC_CHANNEL_EVENT_INVEI1)?then(' | DAC_EVCTRL_INVEI1_Msk','')>
						 
/* (DAC DATA) Mask DATA[15:12] Bit */
#define DAC_DATA_MSB_MASK                    (0x0FFFU)

/* (DAC DATA) Mask DATA[3:0] Bit */
#define DAC_DATA_LSB_MASK                    (0xFFF0U)
						 
// *****************************************************************************
// *****************************************************************************
// Section: DAC Implementation
// *****************************************************************************
// *****************************************************************************

void ${DAC_INSTANCE_NAME}_Initialize (void)
{
	<#if (DAC_CHANNEL_0_ENABLE || DAC_CHANNEL_1_ENABLE)>
	/* Reset DAC Peripheral */
    ${DAC_INSTANCE_NAME}_REGS->DAC_CTRLA = DAC_CTRLA_SWRST_Msk;
	while (((${DAC_INSTANCE_NAME}_REGS->DAC_CTRLA & DAC_CTRLA_SWRST_Msk) == DAC_CTRLA_SWRST_Msk) && ((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_SWRST_Msk) == DAC_SYNCBUSY_SWRST_Msk));
	
    ${DAC_INSTANCE_NAME}_REGS->DAC_CTRLB = ${DAC_OUT_MODE_AND_REF_SEL};

<#list 0..1 as i>
	<#assign DAC_CH_ENABLED = "DAC_CHANNEL_" + i + "_ENABLE">
	<#assign DAC_CH_CTRL = "DAC_CH_" + i + "_CTRL">
	<#assign DAC_CH_EVE_CTRL = "DAC_CH_" + i + "_EVE_CTRL">
	
    <#if (.vars[DAC_CH_ENABLED] == true)>
	${DAC_INSTANCE_NAME}_REGS->DAC_DACCTRL[${i}] = ${.vars[DAC_CH_CTRL]};
	<#if .vars[DAC_CH_EVE_CTRL]?has_content>
	${DAC_INSTANCE_NAME}_REGS->DAC_EVCTRL = ${DAC_INSTANCE_NAME}_REGS->DAC_EVCTRL ${.vars[DAC_CH_EVE_CTRL]};
	</#if>
	</#if>
</#list>
	
	/* Enable DAC */
    ${DAC_INSTANCE_NAME}_REGS->DAC_CTRLA |= DAC_CTRLA_ENABLE_Msk;
	while ((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_ENABLE_Msk) == DAC_SYNCBUSY_ENABLE_Msk);
	</#if>	
}

void ${DAC_INSTANCE_NAME}_DataWrite (DAC_CHANNEL_NUM channel, uint16_t data)
{
	<#if ((DAC_CHANNEL_0_ENABLE && !DAC_CHANNEL_1_ENABLE) || (DAC_OPERATING_MODE == "DIFFERENTIAL"))>
	<#if DAC_CHANNEL_0_ENABLE && (DAC_DATA_ADJUSTMENT0 == "RIGHT-ADJUSTED")>
	/* Write Data to DATA0 Register for conversion(DATA[11:0]) */
	${DAC_INSTANCE_NAME}_REGS->DAC_DATA[0] = DAC_DATA_MSB_MASK & DAC_DATA_DATA(data);
	while ((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA0_Msk) == DAC_SYNCBUSY_DATA0_Msk);
	<#elseif DAC_CHANNEL_0_ENABLE && (DAC_DATA_ADJUSTMENT0 == "LEFT-ADJUSTED")>
	/* Write Data to DATA0 Register for conversion(DATA[15:4]) */
	${DAC_INSTANCE_NAME}_REGS->DAC_DATA[0] = DAC_DATA_LSB_MASK & DAC_DATA_DATA(data);
	while ((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA0_Msk) == DAC_SYNCBUSY_DATA0_Msk);
	</#if>	
	<#elseif ((!DAC_CHANNEL_0_ENABLE && DAC_CHANNEL_1_ENABLE) && (DAC_OPERATING_MODE != "DIFFERENTIAL"))>
	<#if DAC_CHANNEL_1_ENABLE && (DAC_DATA_ADJUSTMENT1 == "RIGHT-ADJUSTED")>
	/* Write Data to DATA1 Register for conversion(DATA[11:0]) */
	${DAC_INSTANCE_NAME}_REGS->DAC_DATA[1] = DAC_DATA_MSB_MASK & DAC_DATA_DATA(data);
	while ((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA1_Msk) == DAC_SYNCBUSY_DATA1_Msk);
	<#elseif DAC_CHANNEL_1_ENABLE && (DAC_DATA_ADJUSTMENT1 == "LEFT-ADJUSTED")>
	/* Write Data to DATA1 Register for conversion(DATA[15:4]) */
	${DAC_INSTANCE_NAME}_REGS->DAC_DATA[1] = DAC_DATA_LSB_MASK & DAC_DATA_DATA(data);
	while ((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA1_Msk) == DAC_SYNCBUSY_DATA1_Msk);
	</#if>	
	<#elseif (DAC_CHANNEL_0_ENABLE && DAC_CHANNEL_1_ENABLE)>
	if (channel == 0)
	{
		<#if DAC_CHANNEL_0_ENABLE && (DAC_DATA_ADJUSTMENT0 == "RIGHT-ADJUSTED")>
		/* Write Data to DATA0 Register for conversion(DATA[11:0]) */
		${DAC_INSTANCE_NAME}_REGS->DAC_DATA[0] = DAC_DATA_MSB_MASK & DAC_DATA_DATA(data);
		while ((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA0_Msk) == DAC_SYNCBUSY_DATA0_Msk);
		<#elseif DAC_CHANNEL_0_ENABLE && (DAC_DATA_ADJUSTMENT0 == "LEFT-ADJUSTED")>
		/* Write Data to DATA0 Register for conversion(DATA[15:4]) */
		${DAC_INSTANCE_NAME}_REGS->DAC_DATA[0] = DAC_DATA_LSB_MASK & DAC_DATA_DATA(data);
		while ((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA0_Msk) == DAC_SYNCBUSY_DATA0_Msk);
		</#if>
	}
	else if (channel == 1)
	{
		<#if DAC_CHANNEL_1_ENABLE && (DAC_DATA_ADJUSTMENT1 == "RIGHT-ADJUSTED")>
		/* Write Data to DATA1 Register for conversion(DATA[11:0]) */
		${DAC_INSTANCE_NAME}_REGS->DAC_DATA[1] = DAC_DATA_MSB_MASK & DAC_DATA_DATA(data);
		while ((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA1_Msk) == DAC_SYNCBUSY_DATA1_Msk);
		<#elseif DAC_CHANNEL_1_ENABLE && (DAC_DATA_ADJUSTMENT1 == "LEFT-ADJUSTED")>
		/* Write Data to DATA1 Register for conversion(DATA[15:4]) */
		${DAC_INSTANCE_NAME}_REGS->DAC_DATA[1] = DAC_DATA_LSB_MASK & DAC_DATA_DATA(data);
		while ((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA1_Msk) == DAC_SYNCBUSY_DATA1_Msk);
		</#if>
	}
	</#if>
}

bool ${DAC_INSTANCE_NAME}_IsReady (DAC_CHANNEL_NUM channel)
{
    return (bool)(((${DAC_INSTANCE_NAME}_REGS->DAC_STATUS >> channel) & DAC_STATUS_READY0_Msk) == DAC_STATUS_READY0_Msk);
}