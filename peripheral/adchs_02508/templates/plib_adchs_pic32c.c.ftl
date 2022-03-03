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

#define ADCHS_CHANNEL_32  (32U)

// *****************************************************************************
// *****************************************************************************
// Section: ${ADCHS_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if ADCHS_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
    <#lt>ADCHS_CALLBACK_OBJECT ${ADCHS_INSTANCE_NAME}_CallbackObj[${ADCHS_NUM_SIGNALS - 1}];
</#if>

<#if ADCCON2__EOSIEN == true>
    <#lt>/* Object to hold callback function and context for end of scan interrupt*/
    <#lt>ADCHS_EOS_CALLBACK_OBJECT ${ADCHS_INSTANCE_NAME}_EOSCallbackObj;
</#if>

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
    while(!((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCANCON & ADCHS_ADCANCON_WKRDY${i}_Msk)); // Wait until ADC is ready
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON3 |= ADCHS_ADCCON3_DIGEN${i}_Msk;       // Enable ADC

    </#if>
</#list>
</#if>
<#if ADCHS_7_ENABLE == true>
    /* ADC 7 */
    ${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCANCON |= ADCHS_ADCANCON_ANEN7_Msk;      // Enable the clock to analog bias
    while(!((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCANCON & ADCHS_ADCANCON_WKRDY7_Msk))); // Wait until ADC is ready
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
    return (uint16_t) (*((&${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCDATA0) + ((uint32_t)channel << 2U)));
}

<#if ADCHS_INTERRUPT == true>
void ${ADCHS_INSTANCE_NAME}_CallbackRegister(ADCHS_CHANNEL_NUM channel, ADCHS_CALLBACK callback, uintptr_t context)
{
    ${ADCHS_INSTANCE_NAME}_CallbackObj[channel].callback_fn = callback;
    ${ADCHS_INSTANCE_NAME}_CallbackObj[channel].context = context;
}
</#if>

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

    <#if ADCCON2__EOSIEN == true>
    if ((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON2 & ADCHS_ADCCON2_EOSIEN_Msk) &&
        ((${ADCHS_INSTANCE_NAME}_REGS->ADCHS_ADCCON2 & ADCHS_ADCCON2_EOSRDY_Msk)))
    {
        if (${ADCHS_INSTANCE_NAME}_EOSCallbackObj.callback_fn != NULL)
        {
            ${ADCHS_INSTANCE_NAME}_EOSCallbackObj.callback_fn(${ADCHS_INSTANCE_NAME}_EOSCallbackObj.context);
        }
    }
    </#if>

    <#if ADCHS_INTERRUPT == true>
    /* Check pending events and call callback if registered */
    for(i = 0; i < ${ADCHS_NUM_SIGNALS}; i++)
    {
        if((status & (1 << i)) && (${ADCHS_INSTANCE_NAME}_CallbackObj[i].callback_fn != NULL))
        {
            ${ADCHS_INSTANCE_NAME}_CallbackObj[i].callback_fn((ADCHS_CHANNEL_NUM)i, ${ADCHS_INSTANCE_NAME}_CallbackObj[i].context);
        }
    }
    </#if>
}
</#if>
