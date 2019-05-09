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


void ${ADCHS_INSTANCE_NAME}_Initialize()
{
    ADCCON1bits.ON = 0;

<#list 0..((ADCHS_NUM_CLASS1_SIGNALS) - 1) as i>
    <#assign ADCHS_CH_ENABLE = "ADCHS_"+ i + "_ENABLE">
    <#assign ADCHS_TIME = "ADCHS_ADCTIME" + i>
    <#if .vars[ADCHS_CH_ENABLE] == true>
    ADC${i}CFG = DEVADC${i};
    ADC${i}TIME = 0x${.vars[ADCHS_TIME]};

    </#if>
</#list>

<#if ADCHS_7_ENABLE == true>
    ADC7CFG = DEVADC7;
</#if>

    ADCCON1 = 0x${ADCHS_ADCCON1};
    ADCCON2 = 0x${ADCHS_ADCCON2};
    ADCCON3 = 0x${ADCHS_ADCCON3};

    ADCTRGMODE = 0x${ADCHS_ADCTRGMODE};

    <#if ADCHS_ADCTRG1??>ADCTRG1 = 0x${ADCHS_ADCTRG1}; </#if>
    <#if ADCHS_ADCTRG2??>ADCTRG2 = 0x${ADCHS_ADCTRG2}; </#if>
    <#if ADCHS_ADCTRG3??>ADCTRG3 = 0x${ADCHS_ADCTRG3}; </#if>
    <#if ADCHS_ADCTRG4??>ADCTRG4 = 0x${ADCHS_ADCTRG4}; </#if>
    <#if ADCHS_ADCTRG5??>ADCTRG5 = 0x${ADCHS_ADCTRG5}; </#if>
    <#if ADCHS_ADCTRG6??>ADCTRG6 = 0x${ADCHS_ADCTRG6}; </#if>
    <#if ADCHS_ADCTRG7??>ADCTRG7 = 0x${ADCHS_ADCTRG7}; </#if>

    ADCTRGSNS = 0x${ADCHS_ADCTRGSNS};

    ADCIMCON1 = 0x${ADCHS_ADCIMCON1};
    <#if ADCHS_ADCIMCON2??>ADCIMCON2 = 0x${ADCHS_ADCIMCON2}; </#if>
    <#if ADCHS_ADCIMCON3??>ADCIMCON3 = 0x${ADCHS_ADCIMCON3}; </#if>
    <#if ADCHS_ADCIMCON4??>ADCIMCON4 = 0x${ADCHS_ADCIMCON4}; </#if>

    /* Input scan */
    ADCCSS1 = 0x${ADCHS_ADCCSS1};
    ADCCSS2 = 0x${ADCHS_ADCCSS2};

<#if ADCHS_INTERRUPT == true>
    /* Result interrupt enable */
    ADCGIRQEN1 = 0x${ADCHS_ADCGIRQEN1};
    ADCGIRQEN2 = 0x${ADCHS_ADCGIRQEN2};

    /* Interrupt Enable */
    <#if ADCHS_IEC0_REG??>
    ${ADCHS_IEC0_REG}SET = 0x${ADCHS_IEC0};
    </#if>
    <#if ADCHS_IEC1_REG??>
    ${ADCHS_IEC1_REG}SET = 0x${ADCHS_IEC1};
    </#if>
    <#if ADCHS_IEC2_REG??>
    ${ADCHS_IEC2_REG}SET = 0x${ADCHS_IEC2};
    </#if>
</#if>
    /* Turn ON ADC */
    ADCCON1bits.ON = 1;
    while(!ADCCON2bits.BGVRRDY); // Wait until the reference voltage is ready
    while(ADCCON2bits.REFFLT); // Wait if there is a fault with the reference voltage

<#list 0..((ADCHS_NUM_CLASS1_SIGNALS) - 1) as i>
    <#assign ADCHS_CH_ENABLE = "ADCHS_"+ i + "_ENABLE">
    <#if .vars[ADCHS_CH_ENABLE] == true>
    /* ADC ${i} */
    ADCANCONbits.ANEN${i} = 1;      // Enable the clock to analog bias
    while(!ADCANCONbits.WKRDY${i}); // Wait until ADC is ready
    ADCCON3bits.DIGEN${i} = 1;      // Enable ADC

    </#if>
</#list>
<#if ADCHS_7_ENABLE == true>
    /* ADC 7 */
    ADCANCONbits.ANEN7 = 1;      // Enable the clock to analog bias
    while(!ADCANCONbits.WKRDY7); // Wait until ADC is ready
    ADCCON3bits.DIGEN7 = 1;      // Enable ADC
</#if>
}


/* Enable ADCHS channels */
void ${ADCHS_INSTANCE_NAME}_ModulesEnable (ADCHS_MODULE_MASK moduleMask)
{
    ADCCON3 |= (moduleMask << 16);
}

/* Disable ADCHS channels */
void ${ADCHS_INSTANCE_NAME}_ModulesDisable (ADCHS_MODULE_MASK moduleMask)
{
    ADCCON3 &= ~(moduleMask << 16);
}


void ${ADCHS_INSTANCE_NAME}_ChannelResultInterruptEnable (ADCHS_CHANNEL_NUM channel)
{
    if (channel < ADCHS_CHANNEL_32)
    {
        ADCGIRQEN1 |= 0x01 << channel;
    }
    else
    {
        ADCGIRQEN2 |= 0x01 << (channel - 32);
    }
}

void ${ADCHS_INSTANCE_NAME}_ChannelResultInterruptDisable (ADCHS_CHANNEL_NUM channel)
{
    if (channel < ADCHS_CHANNEL_32)
    {
        ADCGIRQEN1 &= ~(0x01 << channel);
    }
    else
    {
        ADCGIRQEN2 &= ~(0x01 << (channel - 32));
    }
}

void ${ADCHS_INSTANCE_NAME}_ChannelEarlyInterruptEnable (ADCHS_CHANNEL_NUM channel)
{
    if (channel < ADCHS_CHANNEL_32)
    {
        ADCEIEN1 |= (0x01 << channel);
    }
    else
    {
        ADCEIEN2 |= (0x01 << (channel - 32));
    }
}

void ${ADCHS_INSTANCE_NAME}_ChannelEarlyInterruptDisable (ADCHS_CHANNEL_NUM channel)
{
    if (channel < ADCHS_CHANNEL_32)
    {
        ADCEIEN1 &= ~(0x01 << channel);
    }
    else
    {
        ADCEIEN2 &= ~(0x01 << (channel - 32));
    }
}

void ADCHS_GlobalEdgeConversionStart(void)
{
    ADCCON3bits.GSWTRG = 1;
}

void ADCHS_GlobalLevelConversionStart(void)
{
    ADCCON3bits.GLSWTRG = 1;
}

void ADCHS_ChannelConversionStart(ADCHS_CHANNEL_NUM channel)
{
    ADCCON3bits.ADINSEL = channel;
    ADCCON3bits.RQCNVRT = 1;
}


/*Check if conversion result is available */
bool ${ADCHS_INSTANCE_NAME}_ChannelResultIsReady(ADCHS_CHANNEL_NUM channel)
{
    bool status;
    if (channel < ADCHS_CHANNEL_32)
    {
        status = (ADCDSTAT1 >> channel) & 0x01;
    }
    else
    {
        status = (ADCDSTAT2 >> (channel - 32)) & 0x01;
    }
    return status;
}

/* Read the conversion result */
uint16_t ${ADCHS_INSTANCE_NAME}_ChannelResultGet(ADCHS_CHANNEL_NUM channel)
{
<#if __PROCESSOR?contains("PIC32MZ")>
    return (*((&ADCDATA0) + channel));
</#if>
<#if __PROCESSOR?contains("PIC32MK")>
    return (uint16_t) (*((&ADCDATA0) + (channel << 2)));
</#if>
}

<#if ADCHS_INTERRUPT == true>
void ${ADCHS_INSTANCE_NAME}_CallbackRegister(ADCHS_CHANNEL_NUM channel, ADCHS_CALLBACK callback, uintptr_t context)
{
    ${ADCHS_INSTANCE_NAME}_CallbackObj[channel].callback_fn = callback;
    ${ADCHS_INSTANCE_NAME}_CallbackObj[channel].context = context;
}
</#if>

<#list 0..31 as i>
<#assign ADCHS_DATA_INTERRUPT_ENABLE = "ADCGIRQEN1__AGIEN" + i>
<#if .vars[ADCHS_DATA_INTERRUPT_ENABLE]?? && .vars[ADCHS_DATA_INTERRUPT_ENABLE] == true>
void ADC_DATA${i}_InterruptHandler(void)
{
    if (${ADCHS_INSTANCE_NAME}_CallbackObj[${i}].callback_fn != NULL)
    {
      ${ADCHS_INSTANCE_NAME}_CallbackObj[${i}].callback_fn(ADCHS_CH${i}, ${ADCHS_INSTANCE_NAME}_CallbackObj[${i}].context);
    }

<#if __PROCESSOR?contains("PIC32MZ")>
<#if i < ADCHS_IFS0_NUM_IRQ>
    IFS${ADCHS_IFS_START_INDEX}CLR = _IFS${ADCHS_IFS_START_INDEX}_ADCD${i}IF_MASK;
<#elseif (i gt ADCHS_IFS0_NUM_IRQ) && (i < ADCHS_IFS1_NUM_IRQ)>
    IFS${ADCHS_IFS_START_INDEX + 1}CLR = _IFS${ADCHS_IFS_START_INDEX+1}_ADCD${i}IF_MASK;
</#if>
</#if>

<#if __PROCESSOR?contains("PIC32MK")>
<#if i < ADCHS_IFS0_NUM_IRQ>
    IFS${ADCHS_IFS_START_INDEX}CLR = _IFS${ADCHS_IFS_START_INDEX}_AD1D${i}IF_MASK;
<#elseif (i gt ADCHS_IFS0_NUM_IRQ) && (i < ADCHS_IFS1_NUM_IRQ)>
    IFS${ADCHS_IFS_START_INDEX + 1}CLR = _IFS${ADCHS_IFS_START_INDEX+1}_AD1D${i}IF_MASK;
</#if>
</#if>
}
</#if>
</#list>

<#list 32..((ADCHS_NUM_SIGNALS) - 1) as i>
<#assign ADCHS_DATA_INTERRUPT_ENABLE = "ADCGIRQEN2__AGIEN" + i>
<#if .vars[ADCHS_DATA_INTERRUPT_ENABLE]?? &&.vars[ADCHS_DATA_INTERRUPT_ENABLE] == true>
void ADC_DATA${i}_InterruptHandler(void)
{
    if (${ADCHS_INSTANCE_NAME}_CallbackObj[${i}].callback_fn != NULL)
    {
        ${ADCHS_INSTANCE_NAME}_CallbackObj[${i}].callback_fn(ADCHS_CH${i}, ${ADCHS_INSTANCE_NAME}_CallbackObj[${i}].context);
    }
<#if __PROCESSOR?contains("PIC32MZ")>
<#if i < ADCHS_IFS0_NUM_IRQ>
    IFS${ADCHS_IFS_START_INDEX}CLR = _IFS${ADCHS_IFS_START_INDEX}_ADCD${i}IF_MASK;
<#elseif (i gt ADCHS_IFS0_NUM_IRQ) && (i < ADCHS_IFS1_NUM_IRQ)>
    IFS${ADCHS_IFS_START_INDEX + 1}CLR = _IFS${ADCHS_IFS_START_INDEX+1}_ADCD${i}IF_MASK;
<#else>
    IFS${ADCHS_IFS_START_INDEX + 2}CLR = _IFS${ADCHS_IFS_START_INDEX+2}_ADCD${i}IF_MASK;
</#if>
</#if>

<#if __PROCESSOR?contains("PIC32MK")>
<#if i < ADCHS_IFS0_NUM_IRQ>
    IFS${ADCHS_IFS_START_INDEX}CLR = _IFS${ADCHS_IFS_START_INDEX}_AD1D${i}IF_MASK;
<#elseif (i gt ADCHS_IFS0_NUM_IRQ) && (i < ADCHS_IFS1_NUM_IRQ)>
    IFS${ADCHS_IFS_START_INDEX + 1}CLR = _IFS${ADCHS_IFS_START_INDEX+1}_AD1D${i}IF_MASK;
<#else>
    IFS${ADCHS_IFS_START_INDEX + 2}CLR = _IFS${ADCHS_IFS_START_INDEX+2}_AD1D${i}IF_MASK;
</#if>
</#if>
}
</#if>
</#list>
