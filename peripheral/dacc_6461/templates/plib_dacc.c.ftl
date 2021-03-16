/*******************************************************************************
  Digital-to-Analog Converter Controller (DACC) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DACC_INSTANCE_NAME?lower_case}.c

  Summary:
    DACC Source File

  Description:
    None

*******************************************************************************/

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

#include "device.h"
#include "plib_${DACC_INSTANCE_NAME?lower_case}.h"

<#assign DACC_CHER_CH = "">
<#list 0..(DACC_NUM_CHANNELS - 1) as i>
<#assign DACC_CH_ENABLE = "DACC_CHER_CH" + i>
    <#if .vars[DACC_CH_ENABLE] == true>
        <#if DACC_CHER_CH != "">
            <#assign DACC_CHER_CH = DACC_CHER_CH + " | " + "DACC_CHER_CH" + i + "_Msk">
        <#else>
            <#assign DACC_CHER_CH = "DACC_CHER_CH" + i + "_Msk">
        </#if>
    </#if>
</#list>
<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: DACC Implementation
// *****************************************************************************
// *****************************************************************************

void ${DACC_INSTANCE_NAME}_Initialize(void)
{
<#if (DACC_CHER_CH0 || DACC_CHER_CH1 || DACC_CHER_CH2)>
    /* Reset DACC Peripheral */
    ${DACC_INSTANCE_NAME}_REGS->DACC_CR = DACC_CR_SWRST_Msk;

    ${DACC_INSTANCE_NAME}_REGS->DACC_MR = DACC_MR_STARTUP(${DACC_MR_STARTUP})<#rt>
    <#lt><#if CONVERSION_MODE_CH == "MAX_SPEED_MODE"> | DACC_MR_MAXS_Msk</#if><#rt>
    <#lt><#if CONVERSION_MODE_CH == "TRIGGER_MODE"> | DACC_MR_TRGSEL_${DACC_TRIGR_TRGSEL} | DACC_MR_TRGEN_Msk</#if><#rt>
    <#lt><#if DACC_MR_TAG_ENABLE == true> | DACC_MR_TAG_Msk</#if><#rt>
    <#lt> | DACC_MR_ONE_Msk;

    <#if DACC_CHER_CH?has_content>
    /* Enable DAC Channel */
    ${DACC_INSTANCE_NAME}_REGS->DACC_CHER = ${DACC_CHER_CH};
    </#if>
</#if>
}

bool ${DACC_INSTANCE_NAME}_IsReady(void)
{
    return (bool)((${DACC_INSTANCE_NAME}_REGS->DACC_ISR & DACC_ISR_TXRDY_Msk) == DACC_ISR_TXRDY_Msk);
}

<#if DACC_MR_TAG_ENABLE == true>
void ${DACC_INSTANCE_NAME}_ChannelDataWrite(DACC_CHANNEL_NUM channel, uint16_t data)
{
    ${DACC_INSTANCE_NAME}_REGS->DACC_CDR = ((data & 0xFFF) | (channel << 12));
}
<#else>
void ${DACC_INSTANCE_NAME}_ChannelSelect(DACC_CHANNEL_NUM channel)
{
    ${DACC_INSTANCE_NAME}_REGS->DACC_MR = (${DACC_INSTANCE_NAME}_REGS->DACC_MR & ~DACC_MR_USER_SEL_Msk) | DACC_MR_USER_SEL(channel);
}

void ${DACC_INSTANCE_NAME}_DataWrite(uint16_t data)
{
    ${DACC_INSTANCE_NAME}_REGS->DACC_CDR = data;
}
</#if>
