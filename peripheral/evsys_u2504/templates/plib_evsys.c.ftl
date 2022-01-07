/*******************************************************************************
  EVSYS Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${EVSYS_INSTANCE_NAME?lower_case}.c

  Summary:
    EVSYS Source File

  Description:
    None

*******************************************************************************/

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

#include "plib_${EVSYS_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#assign EVSYS_REG_NAME = EVSYS_INSTANCE_NAME>
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
    <#assign EVSYS_REG_NAME = EVSYS_INSTANCE_NAME + "_SEC">
</#if>


<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
<#if INTERRUPT_ACTIVE>
<#assign CONFIGURED_SYNC_CHANNEL = 0>
    <#list 0..NUM_SYNC_CHANNELS as i>
        <#assign EVSYS_CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
        <#if .vars[EVSYS_CHANNEL_ENABLE]?has_content>
            <#if .vars[EVSYS_CHANNEL_ENABLE] == true>
                <#assign EVSYS_NONSEC_VAL = "EVSYS_NONSEC_" + i >
                <#if .vars[EVSYS_NONSEC_VAL]?has_content>
                    <#if .vars[EVSYS_NONSEC_VAL] == "SECURE">
                        <#assign CONFIGURED_SYNC_CHANNEL = i + 1>
                    </#if>
                </#if>
            </#if>
        </#if>
    </#list>
    <#if CONFIGURED_SYNC_CHANNEL != 0>
        <#lt>EVSYS_OBJECT evsys[${CONFIGURED_SYNC_CHANNEL}];
    </#if>
</#if>
<#else>
<#if INTERRUPT_ACTIVE>
<#assign CONFIGURED_SYNC_CHANNEL = 0>
    <#list 0..NUM_SYNC_CHANNELS as i>
        <#assign EVSYS_CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
        <#if .vars[EVSYS_CHANNEL_ENABLE]?has_content>
            <#if .vars[EVSYS_CHANNEL_ENABLE] == true>
                <#assign CONFIGURED_SYNC_CHANNEL = i + 1>
            </#if>
        </#if>
    </#list>
    <#if CONFIGURED_SYNC_CHANNEL != 0>
        <#lt>EVSYS_OBJECT evsys[${CONFIGURED_SYNC_CHANNEL}];
    </#if>
</#if>
</#if>

void ${EVSYS_INSTANCE_NAME}_Initialize( void )
{
<#if EVSYS_CHANNEL_SCHEDULING == "1">
    ${EVSYS_REG_NAME}_REGS->EVSYS_PRICTRL = EVSYS_PRICTRL_RREN_Msk;
</#if>
<#assign TOTAL_CHANNEL = EVSYS_CHANNEL_NUMBER?number >
<#assign TOTAL_USER = EVSYS_USER_NUMBER?number >
    /*Event Channel User Configuration*/
<#list 0..TOTAL_USER as i>
    <#assign CHANNEL = "EVSYS_USER_" + i >
    <#if .vars[CHANNEL]?has_content>
    <#if .vars[CHANNEL] != '0'>
    ${EVSYS_REG_NAME}_REGS->EVSYS_USER[${i}] = EVSYS_USER_CHANNEL(${.vars[CHANNEL]});
    </#if>
    </#if>
</#list>
<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
    <#if EVSYS_NONSEC_USER0 != '0'>

    <#if EVSYS_NONSEC_USER_REG == true>
    ${EVSYS_REG_NAME}_REGS->EVSYS_NONSECUSER0 = 0x${EVSYS_NONSEC_USER0};
    <#else>
    ${EVSYS_REG_NAME}_REGS->EVSYS_NONSECUSER[0] = 0x${EVSYS_NONSEC_USER0};
    </#if>
    </#if>
<#if TOTAL_USER gt 31>
    <#if EVSYS_NONSEC_USER1 != '0'>
    <#if EVSYS_NONSEC_USER_REG == true>
    ${EVSYS_REG_NAME}_REGS->EVSYS_NONSECUSER1 = 0x${EVSYS_NONSEC_USER1};
    <#else>
    ${EVSYS_REG_NAME}_REGS->EVSYS_NONSECUSER[1] = 0x${EVSYS_NONSEC_USER1};
    </#if>
    </#if>
</#if>
</#if>

<#list 0..TOTAL_CHANNEL as i>
    <#assign CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
    <#assign GENERATOR = "EVSYS_CHANNEL_" + i + "_GENERATOR">
    <#assign PATH = "EVSYS_CHANNEL_" + i + "_PATH">
    <#assign EDGE = "EVSYS_CHANNEL_" + i + "_EDGE">
    <#assign ONDEMAND = "EVSYS_CHANNEL_" + i + "_ONDEMAND">
    <#assign RUNSTANDBY = "EVSYS_CHANNEL_" + i + "_RUNSTANDBY">
    <#if i < NUM_SYNC_CHANNELS>
        <#assign EVD = "EVSYS_CHANNEL_" + i + "_EVENT">
        <#assign OVERRUN = "EVSYS_CHANNEL_" + i + "_OVERRUN">
    </#if>
    <#if .vars[CHANNEL_ENABLE]?has_content>
    <#if (.vars[CHANNEL_ENABLE] != false)>
    /* Event Channel ${i} Configuration */
    ${EVSYS_REG_NAME}_REGS->CHANNEL[${i}].EVSYS_CHANNEL = EVSYS_CHANNEL_EVGEN(${.vars[GENERATOR]}) | EVSYS_CHANNEL_PATH(${.vars[PATH]}) | EVSYS_CHANNEL_EDGSEL(${.vars[EDGE]}) \
                                    ${(.vars[RUNSTANDBY])?then('| EVSYS_CHANNEL_RUNSTDBY_Msk', '')} ${(.vars[ONDEMAND])?then('| EVSYS_CHANNEL_ONDEMAND_Msk', '')};
    <#if .vars[PATH] != '2' >
    <#if (.vars[EVD] || .vars[OVERRUN])>
    <#if .vars[EVD]>
    ${EVSYS_REG_NAME}_REGS->CHANNEL[${i}].EVSYS_CHINTENSET = EVSYS_CHINTENSET_EVD_Msk ${(.vars[OVERRUN])?then('| EVSYS_CHINTENSET_OVR_Msk', '')};
    <#else>
    ${EVSYS_REG_NAME}_REGS->CHANNEL[${i}].EVSYS_CHINTENSET = EVSYS_CHINTENSET_OVR_Msk;
    </#if>
    </#if>
    </#if>
    </#if>
    </#if>
</#list>
    <#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
    <#if EVSYS_NONSEC != "0">
    ${EVSYS_REG_NAME}_REGS->EVSYS_NONSECCHAN = 0x${EVSYS_NONSEC};
    </#if>
    </#if>
}

<#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
    <#list 0..EVSYS_CHANNEL_NUMBER as i>
    <#assign CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
    <#assign EVSYS_NONSEC = "EVSYS_NONSEC_" + i >
    <#if .vars[CHANNEL_ENABLE]?has_content && .vars[CHANNEL_ENABLE] != false>
    <#if .vars[EVSYS_NONSEC]?has_content && .vars[EVSYS_NONSEC] == "SECURE">
    <#lt>void ${EVSYS_INSTANCE_NAME}_GeneratorEnable(EVSYS_CHANNEL channel, uint8_t generator)
    <#lt>{
    <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL = (${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL & ~EVSYS_CHANNEL_EVGEN_Msk) | EVSYS_CHANNEL_EVGEN(generator);
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_GeneratorDisable(EVSYS_CHANNEL channel)
    <#lt>{
    <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL = (${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL & ~EVSYS_CHANNEL_EVGEN_Msk);
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_UserEnable(EVSYS_CHANNEL channel, uint8_t user)
    <#lt>{
    <#lt>   ${EVSYS_REG_NAME}_REGS->EVSYS_USER[user] = EVSYS_USER_CHANNEL((channel + 1));
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_UserDisable(uint8_t user)
    <#lt>{
    <#lt>   ${EVSYS_REG_NAME}_REGS->EVSYS_USER[user] = 0x0;
    <#lt>}
    <#break>
    </#if>
    </#if>
    </#list>
<#else>
    <#list 0..EVSYS_CHANNEL_NUMBER as i>
    <#assign CHANNEL_ENABLE = "EVSYS_CHANNEL_" + i >
    <#if .vars[CHANNEL_ENABLE]?has_content && .vars[CHANNEL_ENABLE] != false>
    <#lt>void ${EVSYS_INSTANCE_NAME}_GeneratorEnable(EVSYS_CHANNEL channel, uint8_t generator)
    <#lt>{
    <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL = (${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL & ~EVSYS_CHANNEL_EVGEN_Msk) | EVSYS_CHANNEL_EVGEN(generator);
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_GeneratorDisable(EVSYS_CHANNEL channel)
    <#lt>{
    <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL = (${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHANNEL & ~EVSYS_CHANNEL_EVGEN_Msk);
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_UserEnable(EVSYS_CHANNEL channel, uint8_t user)
    <#lt>{
    <#lt>   ${EVSYS_REG_NAME}_REGS->EVSYS_USER[user] = EVSYS_USER_CHANNEL((channel + 1));
    <#lt>}

    <#lt>void ${EVSYS_INSTANCE_NAME}_UserDisable(uint8_t user)
    <#lt>{
    <#lt>   ${EVSYS_REG_NAME}_REGS->EVSYS_USER[user] = 0x0;
    <#lt>}
    <#break>
    </#if>
    </#list>
</#if>

<#if INTERRUPT_ACTIVE>
    <#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
        <#list 0..NUM_SYNC_CHANNELS as i>
            <#assign EVSYS_NONSEC = "EVSYS_NONSEC_" + i >
            <#if .vars[EVSYS_NONSEC]?has_content>
                <#if .vars[EVSYS_NONSEC] == "SECURE">

                    <#lt>void ${EVSYS_INSTANCE_NAME}_InterruptEnable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interruptMask)
                    <#lt>{
                    <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTENSET = interruptMask;
                    <#lt>}

                    <#lt>void ${EVSYS_INSTANCE_NAME}_InterruptDisable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interruptMask)
                    <#lt>{
                    <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTENCLR = interruptMask;
                    <#lt>}

                    <#lt>void ${EVSYS_INSTANCE_NAME}_CallbackRegister(EVSYS_CHANNEL channel, EVSYS_CALLBACK callback, uintptr_t context )
                    <#lt>{
                    <#lt>   evsys[channel].callback = callback;
                    <#lt>   evsys[channel].context = context;
                    <#lt>}
                    <#break>
                </#if>
            </#if>
        </#list>

    <#else>
        <#lt>void ${EVSYS_INSTANCE_NAME}_InterruptEnable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interruptMask)
        <#lt>{
        <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTENSET = interruptMask;
        <#lt>}

        <#lt>void ${EVSYS_INSTANCE_NAME}_InterruptDisable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interruptMask)
        <#lt>{
        <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTENCLR = interruptMask;
        <#lt>}

        <#lt>void ${EVSYS_INSTANCE_NAME}_CallbackRegister(EVSYS_CHANNEL channel, EVSYS_CALLBACK callback, uintptr_t context )
        <#lt>{
        <#lt>   evsys[channel].callback = callback;
        <#lt>   evsys[channel].context = context;
        <#lt>}
    </#if>
    <#if __TRUSTZONE_ENABLED?? && __TRUSTZONE_ENABLED == "true">
        <#list 0..NUM_SYNC_CHANNELS as x>
            <#assign INTERRUPT_MODE = "EVSYS_INTERRUPT_MODE" + x>
            <#if .vars[INTERRUPT_MODE]??>
                <#if .vars[INTERRUPT_MODE]>
                    <#assign EVSYS_NONSEC = "EVSYS_NONSEC_" + x >
                    <#if .vars[EVSYS_NONSEC]?has_content>
                        <#if .vars[EVSYS_NONSEC] == "SECURE">
                            <#lt>void ${EVSYS_INSTANCE_NAME}_${x}_InterruptHandler( void )
                            <#lt>{
                            <#lt>   volatile uint32_t status = ${EVSYS_REG_NAME}_REGS->CHANNEL[${x}].EVSYS_CHINTFLAG;
                            <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[${x}].EVSYS_CHINTFLAG = EVSYS_CHINTFLAG_Msk;
                            <#lt>   if(evsys[${x}].callback != NULL)
                            <#lt>   {
                            <#lt>       evsys[${x}].callback(status, evsys[${x}].context);
                            <#lt>   }
                            <#lt>}
                        </#if>
                    </#if>
                </#if>
            </#if>
        </#list>
    <#else>
        <#list 0..EVSYS_INT_LINES-1 as x>
            <#assign EVENT_SYSTEM_INT_NAME  = "EVSYS_INT_NAME_"  + x>
            <#assign res =.vars[EVENT_SYSTEM_INT_NAME]?matches(r"(\d+)")>
            <#assign res2 =.vars[EVENT_SYSTEM_INT_NAME]?matches(r"(\d+)_(\d+)")>
            <#if res>
                <#assign INTERRUPT_MODE = "EVSYS_INTERRUPT_MODE" + (res?groups[1])?number>
                <#if .vars[INTERRUPT_MODE]?? && (.vars[INTERRUPT_MODE] == true)>
                    <#lt>void ${EVSYS_INSTANCE_NAME}_${res?groups[1]}_InterruptHandler( void )
                    <#lt>{
                    <#lt>   volatile uint32_t status = ${EVSYS_REG_NAME}_REGS->CHANNEL[${res?groups[1]}].EVSYS_CHINTFLAG;
                    <#lt>   ${EVSYS_REG_NAME}_REGS->CHANNEL[${res?groups[1]}].EVSYS_CHINTFLAG = EVSYS_CHINTFLAG_Msk;
                    <#lt>   if(evsys[${res?groups[1]}].callback != NULL)
                    <#lt>   {
                    <#lt>       evsys[${res?groups[1]}].callback(status, evsys[${res?groups[1]}].context);
                    <#lt>   }
                    <#lt>}
                </#if>
            <#elseif res2 >
                <#assign GENERATE_ISR = false>
                <#list (res2?groups[1])?number..(res2?groups[2])?number as y>
                    <#assign INTERRUPT_MODE = "EVSYS_INTERRUPT_MODE" + y>
                    <#if .vars[INTERRUPT_MODE]?? && (.vars[INTERRUPT_MODE] == true)>
                        <#assign GENERATE_ISR = true>
                        <#break>
                    </#if>
                </#list>
                <#if GENERATE_ISR == true>
                    <#lt>void ${EVSYS_INSTANCE_NAME}_${.vars[EVENT_SYSTEM_INT_NAME]}_InterruptHandler( void )
                    <#lt>{
                    <#lt>    uint8_t channel = 0;

                    <#lt>    for(channel = ${res2?groups[1]}; channel <= ${res2?groups[2]}; channel++)
                    <#lt>    {
                    <#lt>        if ((${EVSYS_INSTANCE_NAME}_REGS->EVSYS_INTSTATUS >> channel) & 0x1)
                    <#lt>        {
                    <#lt>           volatile uint32_t status = ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTFLAG;
                    <#lt>           if(evsys[channel].callback != NULL)
                    <#lt>           {
                    <#lt>               evsys[channel].callback(status, evsys[channel].context);
                    <#lt>           }
                    <#lt>           ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTFLAG = EVSYS_CHINTFLAG_Msk;
                    <#lt>        }
                    <#lt>    }
                    <#lt>}
                </#if>
            <#elseif .vars[EVENT_SYSTEM_INT_NAME] == "OTHER">
                <#if EVSYS_INTERRUPT_MODE_OTHER??>
                    <#if EVSYS_INTERRUPT_MODE_OTHER>
                        <#lt>void ${EVSYS_INSTANCE_NAME}_OTHER_InterruptHandler( void )
                        <#lt>{
                        <#lt>   uint8_t channel;
                        <#lt>   for(channel = 4; channel <= ${EVSYS_INTERRUPT_MAX_CHANNEL}; channel++)
                        <#lt>   {
                        <#lt>       if ((${EVSYS_REG_NAME}_REGS->EVSYS_INTSTATUS >> channel) & 0x1)
                        <#lt>       {
                        <#lt>           volatile uint32_t status = ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTFLAG;
                        <#lt>           if(evsys[channel].callback != NULL)
                        <#lt>           {
                        <#lt>               evsys[channel].callback(status, evsys[channel].context);
                        <#lt>           }
                        <#lt>           ${EVSYS_REG_NAME}_REGS->CHANNEL[channel].EVSYS_CHINTFLAG = EVSYS_CHINTFLAG_Msk;
                        <#lt>       }
                        <#lt>   }
                        <#lt>}
                    </#if>
                </#if>
            </#if>
        </#list>
    </#if>
</#if>