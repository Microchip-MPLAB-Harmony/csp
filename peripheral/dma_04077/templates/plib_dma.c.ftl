<#assign dataSizeSelectionBitsOptions = ["ONE_BYTE_WORD","16_BIT_WORD","32_BIT_WORD"]>
<#assign transferModeSelectionBits = ["ONE_SHOT","REPEATED_ONE_SHOT","CONTINUOUS","REPEATED_CONTINUOUS"]>
<#assign sourceAddressModeBits = ["UNCHANGED", "INCREMENTED", "DECREMENTED"]>
<#assign destinationAddressModeBits = ["UNCHANGED", "INCREMENTED", "DECREMENTED"]>
/*******************************************************************************
  Direct Memory Access Controller (${dmaModuleName}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${dmaModuleName?lower_case}.c

  Summary
    Source for ${dmaModuleName} peripheral library interface Implementation.

  Description
    This file defines the interface to the ${dmaModuleName} peripheral library. This
    library provides access to and control of the ${dmaModuleName} controller.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2014 Microchip Technology Inc. and its subsidiaries.
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

#include "plib_${dmaModuleName?lower_case}.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#list 0..MAX_CHANNEL_COUNT as i>
    <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
    <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
//SPI DMAxCH Data Size Selection options
<#list dataSizeSelectionBitsOptions as options>
#define DMA${i}CH_SIZE_${options}          ((uint32_t)(_DMA${i}CH_SIZE_MASK & ((uint32_t)(${options_index}) << _DMA${i}CH_SIZE_POSITION)))
</#list>

//SPI DMAxCH Transfer Mode Selection options
<#list transferModeSelectionBits as options>
#define DMA${i}CH_TRMODE_${options}          ((uint32_t)(_DMA${i}CH_TRMODE_MASK & ((uint32_t)(${options_index}) << _DMA${i}CH_TRMODE_POSITION)))
</#list>

// DMAxCH Source Address Mode Selection Options
<#list sourceAddressModeBits as options>
#define DMA${i}CH_SAMODE_${options}          ((uint16_t)(_DMA${i}CH_SAMODE_MASK & ((uint16_t)(${options_index}) << _DMA${i}CH_SAMODE_POSITION)))
</#list>

// DMAxCH Destination Address Mode Selection Options
<#list destinationAddressModeBits as options>
#define DMA${i}CH_DAMODE_${options}          ((uint16_t)(_DMA${i}CH_DAMODE_MASK & ((uint16_t)(${options_index}) << _DMA${i}CH_DAMODE_POSITION)))
</#list>

    </#if>
</#list>

// Section: Global Data

<#if dmaIntEnabled == true>
<#list 0..MAX_CHANNEL_COUNT as i>
    <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
    <#assign DMA_CH_INT_ENABLE = "DMA" + i + "_CH__DONEEN">
    <#if .vars[DMA_CH_INT_ENABLE]?has_content && .vars[DMA_CH_INT_ENABLE] == true && .vars[DMA_CH_INT_ENABLE]?has_content && .vars[DMA_CH_INT_ENABLE] == true >
void DMA${i}_InterruptHandler (void);
    </#if>
</#list>
</#if>

volatile static ${dmaModuleName}_CHANNEL_OBJECT  dmaChannelObj[${dmaModuleName}_NUMBER_OF_CHANNELS];

// Section: ${dmaModuleName} PLib Interface Implementations

void ${dmaModuleName}_Initialize( void )
{
    /* Enable the ${dmaModuleName} module */
    DMACONbits.ON = 1U;

    /* Initialize the available channel objects */

<#list 0..MAX_CHANNEL_COUNT as i>
    <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
    <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
            <#lt>    dmaChannelObj[${dmaModuleName}_CHANNEL_${i}].inUse      =    false;
            <#lt>    dmaChannelObj[${dmaModuleName}_CHANNEL_${i}].callback   =    NULL;
            <#lt>    dmaChannelObj[${dmaModuleName}_CHANNEL_${i}].context    =    (uintptr_t)NULL;

    </#if>
</#list>

    DMALOW = 0x${dmaLowAddressLimit}UL;

    DMAHIGH = 0x${dmaHighAddressLimit}UL;

<#list 0..MAX_CHANNEL_COUNT as i>
    <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
    <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
    DMA${i}CH = (<#if .vars["DMA"+i+"_CH__RELOADC"] == true> _DMA${i}CH_RELOADC_MASK
         |</#if><#if .vars["DMA"+i+"_CH__RELOADD"] == true> _DMA${i}CH_RELOADD_MASK
         |</#if><#if .vars["DMA"+i+"_CH__RELOADS"] == true> _DMA${i}CH_RELOADS_MASK
         |</#if><#if .vars["DMA"+i+"_CH__RETEN"] == true> _DMA${i}CH_RETEN_MASK
         |</#if>DMA${i}CH_SAMODE_${sourceAddressModeBits[.vars["DMA"+i+"_CH__SAMODE"]?number]}
         | DMA${i}CH_DAMODE_${destinationAddressModeBits[.vars["DMA"+i+"_CH__DAMODE"]?number]}
         | DMA${i}CH_TRMODE_${transferModeSelectionBits[.vars["DMA"+i+"_CH__TRMODE"]?number]}
         | DMA${i}CH_SIZE_${dataSizeSelectionBitsOptions[.vars["DMA"+i+"_CH__SIZE"]?number]}<#if .vars["DMA"+i+"_CH__DONEEN"] == true>
         | _DMA${i}CH_DONEEN_MASK</#if><#if .vars["DMA"+i+"_CH__HALFEN"] == true>
         | _DMA${i}CH_HALFEN_MASK</#if>);

    DMA${i}SEL = (uint32_t)(0x${.vars["DMA"+i+"_SEL__CHSEL"]} << _DMA${i}SEL_CHSEL_POSITION);
    </#if>
</#list>

<#if dmaIntEnabled == true>
<#lt>    /* Enable ${dmaModuleName} channel interrupts */
<#list 0..MAX_CHANNEL_COUNT as i>
    <#assign DMA_CH_INT_ENABLE = "DMA" + i + "_CH__DONEEN">
    <#if .vars[DMA_CH_INT_ENABLE]?has_content && .vars[DMA_CH_INT_ENABLE] == true>
        <#lt>    // Clearing Channel ${i} Interrupt Flag;
        <#lt>    _DMA${i}IF = 0U;
        <#lt>    // Enabling Channel ${i} Interrupt
        <#lt>    _DMA${i}IE = 1U;
    </#if>
</#list>
</#if>

}

void ${dmaModuleName}_Deinitialize( void )
{
    /* Disable ${dmaModuleName} channel interrupts */
<#list 0..MAX_CHANNEL_COUNT as i>
    <#assign DMA_CH_INT_ENABLE = "DMA" + i + "_CH__DONEEN">
    <#if .vars[DMA_CH_INT_ENABLE]?has_content && .vars[DMA_CH_INT_ENABLE] == true>
        <#lt>    // Clearing Channel ${i} Interrupt Flag;
        <#lt>    _DMA${i}IF = 0U;
        <#lt>    // disabling Channel ${i} Interrupt
        <#lt>    _DMA${i}IE = 0U;
    </#if>
</#list>

<#list 0..MAX_CHANNEL_COUNT as i>
    <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
    <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
    //Disable ${dmaModuleName} Channel ${i}
    DMA${i}CHbits.CHEN = 0U;
    </#if>
</#list>
    /* Disable the ${dmaModuleName} module */
    DMACONbits.ON = 0U;

${dmaRegPorSet}
}

<#if anyChannelEnabled == true>
bool ${dmaModuleName}_ChannelTransfer(${dmaModuleName}_CHANNEL channel, const void *srcAddr, const void *destAddr, uint32_t blockSize)
{
    bool returnStatus = false;
    const uint32_t *XsrcAddr  = (const uint32_t *)srcAddr;
    const uint32_t *XdestAddr = (const uint32_t *)destAddr;

    if(dmaChannelObj[channel].inUse == false)
    {
        switch (channel)
        {
        <#list 0..MAX_CHANNEL_COUNT as i>
            <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
            <#assign DMA_TRIGGER_SOURCE = "DMA" + i + "CH_TRG_SRC">
            <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
            case ${dmaModuleName}_CHANNEL_${i}:
                DMA${i}SRC = (uint32_t)XsrcAddr;
                DMA${i}DST = (uint32_t)XdestAddr;
                DMA${i}CNT = blockSize;
                dmaChannelObj[channel].inUse = true;
                returnStatus = true;

                //Enable ${dmaModuleName} Channel ${i}
                DMA${i}CHbits.CHEN = 1;
                <#if .vars[DMA_TRIGGER_SOURCE]?contains("TX")>
                DMA${i}CHbits.CHREQ = 1U;
                </#if>
                break;

            </#if>
        </#list>
            default:break;
        }
    }

    return returnStatus;
}

void ${dmaModuleName}_ChannelPatternMatchSetup(${dmaModuleName}_CHANNEL channel, uint32_t patternMatchMask, uint32_t patternMatchData)
{
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
        DMA${i}MSK = patternMatchMask;
        DMA${i}PAT = patternMatchData;

        /* Enable Pattern Match */
        DMA${i}CHbits.MATCHEN = 1U;
        break;

        </#if>
    </#list>
        default:break;
    }
}

void ${dmaModuleName}_ChannelEnable(${dmaModuleName}_CHANNEL channel)
{
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
            DMA${i}CHbits.CHEN = 1U;
            dmaChannelObj[channel].inUse = true;
            break;

        </#if>
    </#list>
        default:break;
    }
}

void ${dmaModuleName}_ChannelDisable (${dmaModuleName}_CHANNEL channel)
{
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
            DMA${i}CHbits.CHEN = 0U;
            dmaChannelObj[channel].inUse = false;
            break;

        </#if>
    </#list>
        default: break;
    }
}

void ${dmaModuleName}_ChannelPatternMatchEnable(${dmaModuleName}_CHANNEL channel)
{
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
            DMA${i}CHbits.MATCHEN = 1U;
            break;

        </#if>
    </#list>
        default:break;
    }
}

void ${dmaModuleName}_ChannelPatternMatchDisable(${dmaModuleName}_CHANNEL channel)
{
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
            DMA${i}CHbits.MATCHEN = 0U;
            break;

        </#if>
    </#list>
        default:break;
    }
}

bool ${dmaModuleName}_IsSoftwareRequestPending(${dmaModuleName}_CHANNEL channel)
{
    bool status = false;
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
                status = DMA${i}CHbits.CHREQ;
                break;

        </#if>
    </#list>
        default: break;
    }
    return status;
}

void ${dmaModuleName}_ChannelSoftwareTriggerEnable(${dmaModuleName}_CHANNEL channel)
{
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
            DMA${i}CHbits.CHREQ = 1U;
            break;

        </#if>
    </#list>
        default:break;
    }
}

uint32_t ${dmaModuleName}_ChannelGetTransferredCount(${dmaModuleName}_CHANNEL channel)
{
    uint32_t  count = 0;
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
            count = DMA${i}CNT;
            break;

        </#if>
    </#list>
        default:break;
    }
    return count;
}

bool ${dmaModuleName}_ChannelIsBusy (${dmaModuleName}_CHANNEL channel)
{
    bool busy_check = false;
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
            if ((DMA${i}STATbits.DONE == 0) && (dmaChannelObj[${i}].inUse == true))
            {
                busy_check = true;
            }
            break;

        </#if>
    </#list>
        default:
            break;
    }
    return busy_check;
}

DMA_CHANNEL_CONFIG ${dmaModuleName}_ChannelSettingsGet(${dmaModuleName}_CHANNEL channel)
{
    uint32_t  setting = 0;
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
            setting = DMA${i}CH;
            break;

        </#if>
    </#list>
        default:break;
    }
    return setting;
}

bool ${dmaModuleName}_ChannelSettingsSet(${dmaModuleName}_CHANNEL channel, DMA_CHANNEL_CONFIG setting)
{
    bool status = false;

    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
            DMA${i}CH = setting;
            status = true;
            break;

        </#if>
    </#list>
        default:break;
    }
    return status;
}

<#if dmaIntEnabled == true>
void ${dmaModuleName}_ChannelCallbackRegister(${dmaModuleName}_CHANNEL channel, const ${dmaModuleName}_CHANNEL_CALLBACK eventHandler, const uintptr_t contextHandle)
{
    dmaChannelObj[channel].callback  = eventHandler;

    dmaChannelObj[channel].context   = contextHandle;
}

<#list 0..MAX_CHANNEL_COUNT as i>
    <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
    <#assign DMA_CH_INT_ENABLE = "DMA" + i + "_CH__DONEEN">
    <#if .vars[DMA_CH_INT_ENABLE]?has_content && .vars[DMA_CH_INT_ENABLE] == true && .vars[DMA_CH_INT_ENABLE]?has_content && .vars[DMA_CH_INT_ENABLE] == true >
void __attribute__((used)) DMA${i}_InterruptHandler (void)
{
    volatile ${dmaModuleName}_CHANNEL_OBJECT *chanObj;
    ${dmaModuleName}_TRANSFER_EVENT dmaEvent = ${dmaModuleName}_TRANSFER_EVENT_NONE;

    /* Clear the interrupt flag*/
    _DMA${i}IF = 0U;

    /* Find out the channel object */
    chanObj = &dmaChannelObj[${i}];

    if(DMA${i}STATbits.OVERRUN == 1U)
    {
        dmaEvent = ${dmaModuleName}_OVERRUN_ERROR;
        DMA${i}STATbits.OVERRUN = 0;
        dmaChannelObj[${i}].inUse = false;
    }
    else if(DMA${i}STATbits.MATCH == 1U)
    {
        dmaEvent = ${dmaModuleName}_PATTERN_MATCH;
        DMA${i}STATbits.MATCH = 0U;
        dmaChannelObj[${i}].inUse = false;
    }
    else if(DMA${i}STATbits.DONE == 1U)
    {
        dmaEvent = ${dmaModuleName}_TRANSFER_EVENT_COMPLETE;
        DMA${i}STATbits.DONE = 0U;
        dmaChannelObj[${i}].inUse = false;
    }
    else if(DMA${i}STATbits.HALF == 1U)
    {
        dmaEvent = ${dmaModuleName}_TRANSFER_EVENT_HALF_COMPLETE;
        DMA${i}STATbits.HALF = 0U;
        dmaChannelObj[${i}].inUse = false;
    }
    else
    {
        // nothing to process
    }

    if((chanObj->callback != NULL) && (dmaEvent != ${dmaModuleName}_TRANSFER_EVENT_NONE))
    {
        uintptr_t context = chanObj->context;

        chanObj->callback(dmaEvent, context);
    }
}
    </#if>
</#list>

<#else>
${dmaModuleName}_TRANSFER_EVENT ${dmaModuleName}_ChannelTransferStatusGet(${dmaModuleName}_CHANNEL channel)
{
    ${dmaModuleName}_TRANSFER_EVENT dmaEvent = ${dmaModuleName}_TRANSFER_EVENT_NONE;
    switch (channel)
    {
    <#list 0..MAX_CHANNEL_COUNT as i>
        <#assign DMA_CHANNEL_ENABLE = "DMA" + i + "_CH__CHEN">
        <#if .vars[DMA_CHANNEL_ENABLE]?has_content && .vars[DMA_CHANNEL_ENABLE] == true>
        case ${dmaModuleName}_CHANNEL_${i}:
            if(DMA${i}STATbits.OVERRUN == 1U)
            {
                dmaEvent = ${dmaModuleName}_OVERRUN_ERROR;
                DMA${i}STATbits.OVERRUN = 0U;
            }
            else if(DMA${i}STATbits.MATCH == 1U)
            {
                dmaEvent = ${dmaModuleName}_PATTERN_MATCH;
                DMA${i}STATbits.MATCH = 0U;
            }
            else if(DMA${i}STATbits.DONE == 1U)
            {
                dmaEvent = ${dmaModuleName}_TRANSFER_EVENT_COMPLETE;
                DMA${i}STATbits.DONE = 0U;
            }
            else if(DMA${i}STATbits.HALF == 1U)
            {
                dmaEvent = ${dmaModuleName}_TRANSFER_EVENT_HALF_COMPLETE;
                DMA${i}STATbits.HALF = 0U;
            }
            else
            {
                // nothing to process
            }
            break;

        </#if>
    </#list>
        default:break;
    }
    return dmaEvent;
}

</#if>
</#if>