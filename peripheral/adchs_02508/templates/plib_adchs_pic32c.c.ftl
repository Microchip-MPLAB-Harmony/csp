/*******************************************************************************
  ADCHS Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${ADCHS_INSTANCE_NAME?lower_case}.c

  Summary
    ${ADCHS_INSTANCE_NAME} peripheral library source.

  Description
    This file implements the ADCHS peripheral library.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_${ADCHS_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

#define ADCHS_CHANNEL_32  (32U)

// *****************************************************************************
// *****************************************************************************
// Section: ${ADCHS_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if ADCHS_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
    <#lt>static ADCHS_CALLBACK_OBJECT ${ADCHS_INSTANCE_NAME}_CallbackObj[${ADCHS_NUM_SIGNALS - 1}];
</#if>

<#if ADCCON2__EOSIEN == true>
    <#lt>/* Object to hold callback function and context for end of scan interrupt*/
    <#lt>static ADCHS_EOS_CALLBACK_OBJECT ${ADCHS_INSTANCE_NAME}_EOSCallbackObj;
</#if>

<#compress> <#-- To remove unwanted new lines -->
<#assign ADCHS_MAX_FILTER_NUM = 0>

<#list 1..(ADCHS_NUM_FILTERS) as i>
<#assign ADCFLTR_AFEN = "ADCFLTR" + i + "__AFEN">
<#assign ADCHS_DFx_INT_ENABLED = "ADCHS_DF" + i + "_INT_ENABLED">
<#if .vars[ADCFLTR_AFEN] == true && .vars[ADCHS_DFx_INT_ENABLED] == true>
<#assign ADCHS_MAX_FILTER_NUM = i>
</#if>
</#list>

<#if ADCHS_MAX_FILTER_NUM gt 0>
static ADCHS_DF_CALLBACK_OBJECT ${ADCHS_INSTANCE_NAME}_DFCallbackObj[${ADCHS_MAX_FILTER_NUM}];
</#if>

<#assign ADCHS_MAX_COMPARATOR_NUM = 0>

<#list 1..(ADCHS_NUM_COMPARATORS) as i>
<#assign ADCHS_ADCCMPCON_ENDCMP = "ADCCMPCON" + i + "__ENDCMP">
<#assign ADCHS_DCx_INT_ENABLED = "ADCHS_DC" + i + "_INT_ENABLED">
<#if .vars[ADCHS_ADCCMPCON_ENDCMP] == true && .vars[ADCHS_DCx_INT_ENABLED] == true>
<#assign ADCHS_MAX_COMPARATOR_NUM = i>
</#if>
</#list>

<#if ADCHS_MAX_COMPARATOR_NUM gt 0>
static ADCHS_DC_CALLBACK_OBJECT ${ADCHS_INSTANCE_NAME}_DCCallbackObj[${ADCHS_MAX_COMPARATOR_NUM}];
</#if>
</#compress>

void ${ADCHS_INSTANCE_NAME}_Initialize(void)
{
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON1 = 0;

    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON1 = 0x${ADCHS_ADCCON1};
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON2 = 0x${ADCHS_ADCCON2};
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 = 0x${ADCHS_ADCCON3};

    <#if ADCHS_ADCTRG1??>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCTRG1 = 0x${ADCHS_ADCTRG1}; </#if>
    <#if ADCHS_ADCTRG2??>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCTRG2 = 0x${ADCHS_ADCTRG2}; </#if>
    <#if ADCHS_ADCTRG3??>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCTRG3 = 0x${ADCHS_ADCTRG3}; </#if>
    <#if ADCHS_ADCTRG4??>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCTRG4 = 0x${ADCHS_ADCTRG4}; </#if>
    <#if ADCHS_ADCTRG5??>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCTRG5 = 0x${ADCHS_ADCTRG5}; </#if>
    <#if ADCHS_ADCTRG6??>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCTRG6 = 0x${ADCHS_ADCTRG6}; </#if>
    <#if ADCHS_ADCTRG7??>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCTRG7 = 0x${ADCHS_ADCTRG7}; </#if>

    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCTRGSNS = 0x${ADCHS_ADCTRGSNS};

    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCIMCON1 = 0x${ADCHS_ADCIMCON1};
    <#if ADCHS_ADCIMCON2??>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCIMCON2 = 0x${ADCHS_ADCIMCON2}; </#if>
    <#if ADCHS_ADCIMCON3??>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCIMCON3 = 0x${ADCHS_ADCIMCON3}; </#if>
    <#if ADCHS_ADCIMCON4??>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCIMCON4 = 0x${ADCHS_ADCIMCON4}; </#if>

    /* Input scan */
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCSS1 = 0x${ADCHS_ADCCSS1};
    <#if ADCHS_NUM_SIGNALS gt 31>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCSS2 = 0x${ADCHS_ADCCSS2}; </#if>

<#compress> <#-- To remove unwanted new lines -->
<#list 1..(ADCHS_NUM_COMPARATORS) as i>
<#assign ADCHS_ADCCMPEN = "ADCHS_ADCCMPEN" + i>
<#assign ADCHS_ADCCMP = "ADCHS_ADCCMP" + i>
<#assign ADCHS_ADCCMPCON = "ADCHS_ADCCMPCON" + i>

<#if .vars[ADCHS_ADCCMPEN] != "0">
    ADCHS_REGS->ADCHS_ADCCMPEN${i} = 0x${.vars[ADCHS_ADCCMPEN]?upper_case};
</#if>

<#if .vars[ADCHS_ADCCMP] != "0">
    ADCHS_REGS->ADCHS_ADCCMP${i} = 0x${.vars[ADCHS_ADCCMP]?upper_case};
</#if>

<#if .vars[ADCHS_ADCCMPCON] != "0">
    ADCHS_REGS->ADCHS_ADCCMPCON${i} = 0x${.vars[ADCHS_ADCCMPCON]?upper_case};
</#if>
</#list>
</#compress>

<#compress> <#-- To remove unwanted new lines -->
<#list 1..(ADCHS_NUM_FILTERS) as i>
<#assign ADCHS_ADCFLTR = "ADCHS_ADCFLTR" + i>
<#if .vars[ADCHS_ADCFLTR] != "0">
    ADCHS_REGS->ADCHS_ADCFLTR${i} = 0x${.vars[ADCHS_ADCFLTR]?upper_case}U;
</#if>

</#list>
</#compress>

<#if ADCHS_INTERRUPT == true>
    /* Result interrupt enable */
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCGIRQEN1 = 0x${ADCHS_ADCGIRQEN1};
    <#if ADCHS_NUM_SIGNALS gt 31>${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCGIRQEN2 = 0x${ADCHS_ADCGIRQEN2};</#if>
</#if>

    /* Turn ON ADC */
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON1 |= ADCHS_ADCCON1_ON_Msk;
    while((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON2 & ADCHS_ADCCON2_BGVRRDY_Msk) == ADCHS_ADCCON2_BGVRRDY_Msk) 
    {
        // Wait until the reference voltage is ready
    }
    
    while((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON2 & ADCHS_ADCCON2_REFFLT_Msk) == ADCHS_ADCCON2_REFFLT_Msk) 
    {
        // Wait if there is a fault with the reference voltage
    }

<#if ADCHS_NUM_CLASS1_SIGNALS != 0>
<#list 0..((ADCHS_NUM_CLASS1_SIGNALS) - 1) as i>
    <#assign ADCHS_CH_ENABLE = "ADCHS_"+ i + "_ENABLE">
    <#if .vars[ADCHS_CH_ENABLE] == true>
    /* ADC ${i} */
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCANCON |= ADCHS_ADCANCON_ANEN${i}_Msk;      // Enable the clock to analog bias
    while(((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCANCON & ADCHS_ADCANCON_WKRDY${i}_Msk) == 0U) // Wait until ADC is ready
    {
        /* Nothing to do */    
    }
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 |= ADCHS_ADCCON3_DIGEN${i}_Msk;       // Enable ADC

    </#if>
</#list>
</#if>
<#if ADCHS_7_ENABLE == true>
    /* ADC 7 */
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCANCON |= ADCHS_ADCANCON_ANEN7_Msk;      // Enable the clock to analog bias
    while(((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCANCON & ADCHS_ADCANCON_WKRDY7_Msk)) == 0U) // Wait until ADC is ready
    {
        /* Nothing to do */    
    }
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 |= ADCHS_ADCCON3_DIGEN7_Msk;       // Enable ADC
</#if>
}


/* Enable ADCHS channels */
void ${ADCHS_INSTANCE_NAME}_ModulesEnable (ADCHS_MODULE_MASK moduleMask)
{
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 |= ((uint32_t)moduleMask << 16U);
}

/* Disable ADCHS channels */
void ${ADCHS_INSTANCE_NAME}_ModulesDisable (ADCHS_MODULE_MASK moduleMask)
{
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 &= ~((uint32_t)moduleMask << 16U);
}


void ${ADCHS_INSTANCE_NAME}_ChannelResultInterruptEnable (ADCHS_CHANNEL_NUM channel)
{
    if ((uint32_t)channel < ADCHS_CHANNEL_32)
    {
        ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCGIRQEN1 |= 0x01UL << (uint32_t)channel;
    }
    <#if ADCHS_NUM_SIGNALS gt 31>
    else
    {
        ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCGIRQEN2 |= 0x01 << (channel - 32);
    }
    </#if>
}

void ${ADCHS_INSTANCE_NAME}_ChannelResultInterruptDisable (ADCHS_CHANNEL_NUM channel)
{
    if ((uint32_t)channel < ADCHS_CHANNEL_32)
    {
        ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCGIRQEN1 &= ~(0x01UL << (uint32_t)channel);
    }
    <#if ADCHS_NUM_SIGNALS gt 31>
    else
    {
        ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCGIRQEN2 &= ~(0x01 << (channel - 32));
    }
    </#if>
}


void ADCHS_GlobalEdgeConversionStart(void)
{
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 |= ADCHS_ADCCON3_GSWTRG_Msk;
}

void ADCHS_GlobalLevelConversionStart(void)
{
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 = ADCHS_ADCCON3_GLSWTRG_Msk;
}

void ADCHS_GlobalLevelConversionStop(void)
{
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 &= ~ADCHS_ADCCON3_GLSWTRG_Msk;
}

void ADCHS_ChannelConversionStart(ADCHS_CHANNEL_NUM channel)
{
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 &= ~(ADCHS_ADCCON3_ADINSEL_Msk);
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 |= (((uint32_t)channel << ADCHS_ADCCON3_ADINSEL_Pos) | ADCHS_ADCCON3_RQCNVRT_Msk);
}


/*Check if conversion result is available */
bool ${ADCHS_INSTANCE_NAME}_ChannelResultIsReady(ADCHS_CHANNEL_NUM channel)
{
    bool status = false;
    if ((uint32_t)channel < ADCHS_CHANNEL_32)
    {
        status = ((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCDSTAT1 >> (uint32_t)channel) & 0x01U) != 0U;
    }
    <#if ADCHS_NUM_SIGNALS gt 31>
    else
    {
        status = (${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCDSTAT2 >> (channel - 32)) & 0x01;
    }
    </#if>
    return status;
}

/* Read the conversion result */
uint16_t ${ADCHS_INSTANCE_NAME}_ChannelResultGet(ADCHS_CHANNEL_NUM channel)
{
    uint32_t channel_addr = ADCHS_BASE_ADDRESS + ADCHS_ADCDATA0_REG_OFST + ((uint32_t)channel << 4U);
	return (uint16_t)(*(uint32_t*)channel_addr);   
}

<#if ADCHS_INTERRUPT == true>
void ${ADCHS_INSTANCE_NAME}_CallbackRegister(ADCHS_CHANNEL_NUM channel, ADCHS_CALLBACK callback, uintptr_t context)
{
    ${ADCHS_INSTANCE_NAME}_CallbackObj[channel].callback_fn = callback;
    ${ADCHS_INSTANCE_NAME}_CallbackObj[channel].context = context;
}
</#if>

<#list 1..(ADCHS_NUM_COMPARATORS) as i>
<#assign ADCHS_ADCCMPCON_ENDCMP = "ADCCMPCON" + i + "__ENDCMP">
<#assign ADCHS_DCx_INT_ENABLED = "ADCHS_DC" + i + "_INT_ENABLED">
<#assign ADCHS_DCx_IFS_REG = "ADCHS_DC" + i + "_IFS_REG">
<#if .vars[ADCHS_ADCCMPCON_ENDCMP] == true>
void ${ADCHS_INSTANCE_NAME}_Comparator${i}Enable(void)
{
    ADCHS_REGS->ADCHS_ADCCMPCON${i} |= ADCHS_ADCCMPCON${i}_ENDCMP_Msk;
}
void ${ADCHS_INSTANCE_NAME}_Comparator${i}Disable(void)
{
    ADCHS_REGS->ADCHS_ADCCMPCON${i} &= ~ADCHS_ADCCMPCON${i}_ENDCMP_Msk;
}
void ${ADCHS_INSTANCE_NAME}_Comparator${i}LimitSet(uint16_t low_threshold, uint16_t high_threshold)
{
    ADCHS_REGS->ADCHS_ADCCMP${i} = (ADCHS_ADCCMP${i}_ADCMPHI((uint32_t)high_threshold) | ADCHS_ADCCMP${i}_ADCMPLO(low_threshold));
}
void ${ADCHS_INSTANCE_NAME}_Comparator${i}EventModeSet(ADCHS_CMP_EVENT_MODE eventMode)
{
    ADCHS_REGS->ADCHS_ADCCMPCON${i} = (ADCHS_REGS->ADCHS_ADCCMPCON${i} & ~(ADCHS_CMP_EVENT_MODE_IEBTWN | ADCHS_CMP_EVENT_MODE_IEHIHI | ADCHS_CMP_EVENT_MODE_IEHILO | ADCHS_CMP_EVENT_MODE_IELOHI | ADCHS_CMP_EVENT_MODE_IELOLO)) | (eventMode);
}
uint8_t ${ADCHS_INSTANCE_NAME}_Comparator${i}AnalogInputIDGet(void)
{
    return (uint8_t)((ADCHS_REGS->ADCHS_ADCCMPCON${i} & ADCHS_ADCCMPCON1_CMPINID0_Msk) >> ADCHS_ADCCMPCON1_CMPINID0_Pos);
}

<#if .vars[ADCHS_DCx_INT_ENABLED] == true>
void ${ADCHS_INSTANCE_NAME}_Comparator${i}CallbackRegister(ADCHS_DC_CALLBACK callback, uintptr_t context)
{
    ${ADCHS_INSTANCE_NAME}_DCCallbackObj[${i-1}].callback_fn = callback;
    ${ADCHS_INSTANCE_NAME}_DCCallbackObj[${i-1}].context = context;
}
<#else>
bool ${ADCHS_INSTANCE_NAME}_Comparator${i}StatusGet(void)
{
    return (ADCHS_REGS->ADCHS_ADCCMPCON${i} & ADCHS_ADCCMPCON${i}_DCMPED_Msk);
}
</#if>

</#if>
</#list>

<#list 1..(ADCHS_NUM_FILTERS) as i>
<#assign ADCFLTR_AFEN = "ADCFLTR" + i + "__AFEN">
<#assign ADCHS_DFx_INT_ENABLED = "ADCHS_DF" + i + "_INT_ENABLED">
<#assign ADCHS_DFx_IFS_REG = "ADCHS_DF" + i + "_IFS_REG">
<#if .vars[ADCFLTR_AFEN] == true>
uint16_t ${ADCHS_INSTANCE_NAME}_Filter${i}DataGet(void)
{
    return (uint16_t)(ADCHS_REGS->ADCHS_ADCFLTR${i} & ADCHS_ADCFLTR${i}_FLT_DATA${i-1}_Msk);
}
<#if .vars[ADCHS_DFx_INT_ENABLED] == true>
void ${ADCHS_INSTANCE_NAME}_Filter${i}CallbackRegister(ADCHS_DF_CALLBACK callback, uintptr_t context)
{
    ${ADCHS_INSTANCE_NAME}_DFCallbackObj[${i-1}].callback_fn = callback;
    ${ADCHS_INSTANCE_NAME}_DFCallbackObj[${i-1}].context = context;
}
<#else>
bool ${ADCHS_INSTANCE_NAME}_Filter${i}IsReady(void)
{
    return ADCHS_REGS->ADCHS_ADCFLTR${i} & ADCHS_ADCFLTR${i}_AFIF_Msk;
}
</#if>
</#if>
</#list>

<#if ADCCON2__EOSIEN == true>
void ${ADCHS_INSTANCE_NAME}_EOSCallbackRegister(ADCHS_EOS_CALLBACK callback, uintptr_t context)
{
    ${ADCHS_INSTANCE_NAME}_EOSCallbackObj.callback_fn = callback;
    ${ADCHS_INSTANCE_NAME}_EOSCallbackObj.context = context;
}

<#else>
bool ${ADCHS_INSTANCE_NAME}_EOSStatusGet(void)
{
    return (bool)(((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON2 & ADCHS_ADCCON2_EOSRDY_Msk) 
                    >> ADCHS_ADCCON2_EOSRDY_Pos) != 0U);
}
</#if>

<#if ADCHS_INTERRUPT == true || ADCCON2__EOSIEN == true>
void ADCHS_InterruptHandler( void )
{
    <#if ADCHS_INTERRUPT == true>
    uint8_t i;
    uint32_t status;

    status  = ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCDSTAT1;
    status &= ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCGIRQEN1;
    </#if>
	
	<#if ADCHS_MAX_COMPARATOR_NUM gt 0>
	ADCHS_CHANNEL_NUM channelId;
	</#if>

    <#if ADCCON2__EOSIEN == true>
    if (((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON2 & ADCHS_ADCCON2_EOSIEN_Msk) != 0U) &&
        (((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON2 & ADCHS_ADCCON2_EOSRDY_Msk))!= 0U))
    {
        if (${ADCHS_INSTANCE_NAME}_EOSCallbackObj.callback_fn != NULL)
        {
            ${ADCHS_INSTANCE_NAME}_EOSCallbackObj.callback_fn(${ADCHS_INSTANCE_NAME}_EOSCallbackObj.context);
        }
    }
    </#if>

    <#if ADCHS_INTERRUPT == true>
    /* Check pending events and call callback if registered */
    for(i = 0U; i < ${ADCHS_NUM_SIGNALS - 1}U; i++)
    {
        if(((status & (1UL << i)) != 0U) && (${ADCHS_INSTANCE_NAME}_CallbackObj[i].callback_fn != NULL))
        {
            ${ADCHS_INSTANCE_NAME}_CallbackObj[i].callback_fn((ADCHS_CHANNEL_NUM)i, ${ADCHS_INSTANCE_NAME}_CallbackObj[i].context);
        }
    }
    </#if>
	
	<#list 1..(ADCHS_NUM_COMPARATORS) as i>
	<#assign ADCHS_ADCCMPCON_ENDCMP = "ADCCMPCON" + i + "__ENDCMP">
	<#assign ADCHS_DCx_INT_ENABLED = "ADCHS_DC" + i + "_INT_ENABLED">
	<#if .vars[ADCHS_ADCCMPCON_ENDCMP] == true && .vars[ADCHS_DCx_INT_ENABLED] == true>
	
	if ((ADCHS_REGS->ADCHS_ADCCMPCON${i} & ADCHS_ADCCMPCON${i}_DCMPED_Msk) != 0U)
	{
		channelId = (ADCHS_REGS->ADCHS_ADCCMPCON${i} & ADCHS_ADCCMPCON1_CMPINID0_Msk) >> ADCHS_ADCCMPCON1_CMPINID0_Pos;

		if (${ADCHS_INSTANCE_NAME}_DCCallbackObj[${i-1}].callback_fn != NULL)
		{
		  ${ADCHS_INSTANCE_NAME}_DCCallbackObj[${i-1}].callback_fn(channelId, ${ADCHS_INSTANCE_NAME}_DCCallbackObj[${i-1}].context);
		}
	}	
	</#if>
	</#list>
	
	<#list 1..(ADCHS_NUM_FILTERS) as i>
	<#assign ADCFLTR_AFEN = "ADCFLTR" + i + "__AFEN">
	<#assign ADCHS_DFx_INT_ENABLED = "ADCHS_DF" + i + "_INT_ENABLED">
	<#if .vars[ADCFLTR_AFEN] == true && .vars[ADCHS_DFx_INT_ENABLED] == true>
	if (${ADCHS_INSTANCE_NAME}_DFCallbackObj[${i-1}].callback_fn != NULL)
    {
		${ADCHS_INSTANCE_NAME}_DFCallbackObj[${i-1}].callback_fn(${ADCHS_INSTANCE_NAME}_DFCallbackObj[${i-1}].context);
    }
	</#if>
	</#list>
}
</#if>
