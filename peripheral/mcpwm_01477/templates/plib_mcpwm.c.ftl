/*******************************************************************************
  Motor Control PWM (${MCPWM_INSTANCE_NAME}) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${MCPWM_INSTANCE_NAME?lower_case}.c

  Summary:
    ${MCPWM_INSTANCE_NAME} Source File

  Description:
    None

*******************************************************************************/

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
#include "device.h"
#include "plib_${MCPWM_INSTANCE_NAME?lower_case}.h"

<#--Implementation-->
// *****************************************************************************

// *****************************************************************************
// Section: ${MCPWM_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#if PTCON__SEIEN == true>
MCPWM_OBJECT ${MCPWM_INSTANCE_NAME?lower_case}PriEventObj;
</#if>
<#if STCON__SSEIEN == true>
MCPWM_OBJECT ${MCPWM_INSTANCE_NAME?lower_case}SecEventObj;
</#if>
<#assign interrupt_mode = false>
<#list 1 .. MCPWM_NUM_CHANNELS as i>
<#assign interrupt = "MCPWM_EVIC" + i>
<#if .vars[interrupt] == 1>
<#assign interrupt_mode = true>
</#if>
</#list>
<#if  interrupt_mode == true>
MCPWM_CH_OBJECT ${MCPWM_INSTANCE_NAME?lower_case}Obj[${MCPWM_NUM_CHANNELS}];
</#if>

void ${MCPWM_INSTANCE_NAME}_Initialize (void)
{
    /* PTCON register  */
    /*  SEVTPS  = ${PTCON__SEVTPS} */
    /*  PCLKDIV = ${PTCON__PCLKDIV} */
    /*  SEIEN   = ${PTCON__SEIEN?then('true', 'false')} */
    PTCON = 0x${MCPWM_PTCON};

    /* STCON register  */
    /*  SEVTPS  = ${STCON__SEVTPS} */
    /*  SCLKDIV = ${STCON__SCLKDIV} */
    /*  SSEIEN = ${STCON__SSEIEN?then('true', 'false')} */
    STCON = 0x${MCPWM_STCON};

    PTPER = ${PTPER__PTPER};
    STPER = ${STPER__STPER};
    SEVTCMP = ${SEVTCMP_SEVTCMP};
    SSEVTCMP = ${SSEVTCMP_SEVTCMP};
<#list 1 .. MCPWM_NUM_CHANNELS as i>
<#assign PWM_CH_ENABLE = "MCPWM_CHANNEL" + i>
<#assign PWMCON = "MCPWM_PWMCON" + i>
<#assign IOCON = "MCPWM_IOCON" + i>
<#assign PDC = "PDC" + i + "__PDC">
<#assign SDC = "SDC" + i + "__SDC">
<#assign PHASE = "PHASE" + i + "__PHASE">
<#assign DTR = "DTR" + i + "__DTR">
<#assign ALTDTR = "ALTDTR" + i + "__ALTDTR">
<#assign TRIG = "TRIG" + i + "__TRGCMP">
<#assign STRIG = "STRIG" + i + "__STRGCMP">
<#assign MTBS = "PWMCON" + i + "__MTBS">
<#assign PTDIR = "PWMCON" + i + "__PTDIR">
<#assign ECAM = "PWMCON" + i + "__ECAM">
<#assign DTCP = "PWMCON" + i + "__DTCP">
<#assign DTC = "PWMCON" + i + "__DTC">
<#assign SWAP = "IOCON" + i + "__SWAP">
<#assign PMOD = "IOCON" + i + "__PMOD">
<#assign POLH = "IOCON" + i + "__POLH">
<#assign POLL = "IOCON" + i + "__POLL">
<#assign FLTMOD = "IOCON" + i + "__FLTMOD">
<#assign FLTPOL = "IOCON" + i + "__FLTPOL">
<#assign FLTSRC = "IOCON" + i + "__FLTSRC">
<#assign FLTDAT_PWMH = "IOCON" + i + "__FLTDAT_PWMH">
<#assign FLTDAT_PWML = "IOCON" + i + "__FLTDAT_PWML">
<#assign CLMOD = "IOCON" + i + "__CLMOD">
<#assign CLPOL = "IOCON" + i + "__CLPOL">
<#assign CLSRC = "IOCON" + i + "__CLSRC">
<#assign CLDAT_PWMH = "IOCON" + i + "__CLDAT_PWMH">
<#assign CLDAT_PWML = "IOCON" + i + "__CLDAT_PWML">
<#assign LEBCON = "MCPWM_LEBCON" + i>
<#assign LEB = "LEBDLY"+i+"__LEB">
<#assign ITB = "PWMCON" + i + "__ITB">
<#assign PWMHIEN = "PWMCON" + i + "__PWMHIEN">
<#assign PWMLIEN = "PWMCON" + i + "__PWMLIEN">
<#assign TRGIEN = "PWMCON" + i + "__TRGIEN">
<#assign CLIEN = "PWMCON" + i + "__CLIEN">
<#assign FLTIEN = "PWMCON" + i + "__FLTIEN">
<#assign CLLEBEN = "LEBCON" + i + "__CLLENBEN">
<#assign FLTLEBEN = "LEBCON" + i + "__FLTLEBEN">
<#assign PLF = "LEBCON" + i + "__PLF">
<#assign PLR = "LEBCON" + i + "__PLR">
<#assign PHF = "LEBCON" + i + "__PHF">
<#assign PHR = "LEBCON" + i + "__PHR">
<#assign interrupt = "MCPWM_EVIC" + i>
<#assign iec = "MCPWM_IEC_REG" + i>
<#if .vars[PWM_CH_ENABLE] == true>

    /*********** Channel ${i} Configurations **********/
    /* PWMCON${i} register  */
    /*  MTBS   = ${.vars[MTBS]} */
    /*  PTDIR  =  ${.vars[PTDIR]} */
    /*  ECAM   =  ${.vars[ECAM]} */
    /*  DTCP   =  ${.vars[DTCP]} */
    /*  DTC    =  ${.vars[DTC]} */
    /*  ITB    = ${.vars[ITB]} */
    /*  PWMHIEN =  ${.vars[PWMHIEN]?then('true', 'false')} */
    /*  PWMLIEN = ${.vars[PWMLIEN]?then('true', 'false')} */
    /*  TRGIEN = ${.vars[TRGIEN]?then('true', 'false')} */
    /*  CLIEN = ${.vars[CLIEN]?then('true', 'false')} */
    /*  FLTIEN = ${.vars[FLTIEN]?then('true', 'false')} */
    PWMCON${i} = 0x${.vars[PWMCON]};

    /* IOCON${i} register  */
    /*  SWAP    = ${.vars[SWAP]}*/
    /*  PMOD    = ${.vars[PMOD]}*/
    /*  POLH    = ${.vars[POLH]}*/
    /*  POLL    = ${.vars[POLL]}*/
    /*  FLTDAT  = 0b${.vars[FLTDAT_PWMH] + .vars[FLTDAT_PWML]} */
    /*  FLTMOD  = ${.vars[FLTMOD]} */
    /*  FLTPOL  = ${.vars[FLTPOL]}  */
    /*  FLTSRC  = ${.vars[FLTSRC]}  */
    /*  CLDAT  = 0b${.vars[CLDAT_PWMH] + .vars[CLDAT_PWML]} */
    /*  CLMOD  = ${.vars[CLMOD]} */
    /*  CLPOL  = ${.vars[CLPOL]}  */
    /*  CLSRC  = ${.vars[CLSRC]}  */
    IOCON${i} = 0x${.vars[IOCON]};

    PDC${i} = ${.vars[PDC]};
    SDC${i} = ${.vars[SDC]};
    PHASE${i} = ${.vars[PHASE]};

    /* Dead Time */
    DTR${i} = ${.vars[DTR]};
    ALTDTR${i} = ${.vars[ALTDTR]};

    /* Trigger Generator */
    TRIG${i} = ${.vars[TRIG]};
    STRIG${i} = ${.vars[STRIG]};

    /* leading edge blanking */
    /* LEBCON${i} register  */
    /*  CLLEBEN    = ${.vars[CLLEBEN]?then('true', 'false')}  */
    /*  FLTLEBEN   = ${.vars[FLTLEBEN]?then('true', 'false')} */
    /*  PLF        = ${.vars[PLF]}  */
    /*  PLR        = ${.vars[PLR]}  */
    /*  PHF        = ${.vars[PHF]}  */
    /*  PHR        = ${.vars[PHR]}  */
    LEBCON${i} = 0x${.vars[LEBCON]};
    LEBDLY${i} = ${.vars[LEB]};

    <#if .vars[interrupt] == 1>
    /* Enable interrupt */
    ${.vars[iec]}SET = _${.vars[iec]}_PWM${i}IE_MASK;
    ${MCPWM_INSTANCE_NAME?lower_case}Obj[${i-1}].callback = NULL;
    </#if>
</#if>
</#list>

    <#if PTCON__SEIEN == true>
    /* Enable primary special event interrupt */
    ${MCPWM_IEC_PRI}SET = _${MCPWM_IEC_PRI}_PWMPEVTIE_MASK;
    ${MCPWM_INSTANCE_NAME?lower_case}PriEventObj.callback = NULL;
    </#if>
    <#if STCON__SSEIEN == true>
    /* Enable secondary special event interrupt */
    ${MCPWM_IEC_SEC}SET = _${MCPWM_IEC_SEC}_PWMSEVTIE_MASK;
    ${MCPWM_INSTANCE_NAME?lower_case}SecEventObj.callback = NULL;
    </#if>
}


void ${MCPWM_INSTANCE_NAME}_Start(void)
{
    /* Enable MCPWM module */
    PTCONbits.PTEN = 0x1;
}

void ${MCPWM_INSTANCE_NAME}_Stop(void)
{
    /* Disable MCPWM module */
    PTCONbits.PTEN = 0x0;
}

void ${MCPWM_INSTANCE_NAME}_PrimaryPeriodSet(uint16_t period)
{
    PTPER = period;
}

uint16_t ${MCPWM_INSTANCE_NAME}_PrimaryPeriodGet(void)
{
    return PTPER;
}


void ${MCPWM_INSTANCE_NAME}_SecondaryPeriodSet(uint16_t period)
{
    STPER = period;
}

uint16_t ${MCPWM_INSTANCE_NAME}_SecondaryPeriodGet(void)
{
    return STPER;
}

void ${MCPWM_INSTANCE_NAME}_ChannelPrimaryDutySet(MCPWM_CH_NUM channel, uint16_t duty)
{
    *(&PDC1 + (0x40 * (channel))) = duty;
}

void ${MCPWM_INSTANCE_NAME}_ChannelSecondaryDutySet(MCPWM_CH_NUM channel, uint16_t duty)
{
    *(&SDC1 + (0x40 * (channel))) = duty;
}

void ${MCPWM_INSTANCE_NAME}_ChannelDeadTimeSet(MCPWM_CH_NUM channel, uint16_t high_deadtime, uint16_t low_deadtime)
{
    *(&DTR1 + (0x40 * (channel))) = (high_deadtime & 0x3FFF);
    *(&ALTDTR1 + (0x40 * (channel))) = (low_deadtime & 0x3FFF);
}

void ${MCPWM_INSTANCE_NAME}_ChannelPrimaryTriggerSet(MCPWM_CH_NUM channel, uint16_t trigger)
{
    *(&TRIG1 + (0x40 * (channel))) = trigger;
}

void ${MCPWM_INSTANCE_NAME}_ChannelSecondaryTriggerSet(MCPWM_CH_NUM channel, uint16_t trigger)
{
    *(&STRIG1 + (0x40 * (channel))) = trigger;
}

void ${MCPWM_INSTANCE_NAME}_ChannelLeadingEdgeBlankingDelaySet(MCPWM_CH_NUM channel, uint16_t delay)
{
    *(&LEBDLY1 + (0x40 * (channel))) = delay;
}

<#if PTCON__SEIEN == true>
void PWM_PRI_InterruptHandler(void)
{
    PTCONbits.SEIEN = 0;
    ${MCPWM_IFS_PRI}CLR = _${MCPWM_IFS_PRI}_PWMPEVTIF_MASK;    //Clear IRQ flag
    PTCONbits.SEIEN = 1;

    if( (${MCPWM_INSTANCE_NAME?lower_case}PriEventObj.callback != NULL))
    {
        ${MCPWM_INSTANCE_NAME?lower_case}PriEventObj.callback(${MCPWM_INSTANCE_NAME?lower_case}PriEventObj.context);
    }
}

void ${MCPWM_INSTANCE_NAME}_PrimaryEventCallbackRegister(MCPWM_CALLBACK callback, uintptr_t context)
{
    ${MCPWM_INSTANCE_NAME?lower_case}PriEventObj.callback = callback;
    ${MCPWM_INSTANCE_NAME?lower_case}PriEventObj.context = context;
}
</#if>

<#if STCON__SSEIEN == true>
void PWM_SEC_InterruptHandler(void)
{
    STCONbits.SSEIEN = 0;
    ${MCPWM_IFS_SEC}CLR = _${MCPWM_IFS_SEC}_PWMSEVTIF_MASK;    //Clear IRQ flag
    STCONbits.SSEIEN = 1;

    if( (${MCPWM_INSTANCE_NAME?lower_case}SecEventObj.callback != NULL))
    {
        ${MCPWM_INSTANCE_NAME?lower_case}SecEventObj.callback(${MCPWM_INSTANCE_NAME?lower_case}SecEventObj.context);
    }
}

void ${MCPWM_INSTANCE_NAME}_SecondaryEventCallbackRegister(MCPWM_CALLBACK callback, uintptr_t context)
{
    ${MCPWM_INSTANCE_NAME?lower_case}SecEventObj.callback = callback;
    ${MCPWM_INSTANCE_NAME?lower_case}SecEventObj.context = context;
}
</#if>

<#list 1 .. MCPWM_NUM_CHANNELS as i>
<#assign interrupt = "MCPWM_EVIC" + i>
<#assign ifs = "MCPWM_IFS_REG" + i>
<#assign fault_enable = "PWMCON" + i + "__FLTIEN">
<#assign cl_enable = "PWMCON" + i + "__CLIEN">
<#if .vars[interrupt] == 1>
void PWM${i}_InterruptHandler(void)
{
    MCPWM_CH_STATUS status;
    status = (MCPWM_CH_STATUS)(PWMCON${i} & MCPWM_STATUS_MASK);
    if (PWMCON${i}bits.PWMHIEN && PWMCON${i}bits.PWMHIF)
    {
        PWMCON${i}bits.PWMHIF = 0;
    }
    if (PWMCON${i}bits.PWMLIEN && PWMCON${i}bits.PWMLIF)
    {
        PWMCON${i}bits.PWMLIF = 0;
    }
    if (PWMCON${i}bits.TRGIEN && PWMCON${i}bits.TRGIF)
    {
        PWMCON${i}bits.TRGIF = 0;
    }
    if (PWMCON${i}bits.CLIEN && PWMCON${i}bits.CLIF)
    {
        PWMCON${i}bits.CLIEN = 0;
        PWMCON${i}bits.CLIF = 0;
    }
    if (PWMCON${i}bits.FLTIEN && PWMCON${i}bits.FLTIF)
    {
        PWMCON${i}bits.FLTIEN = 0;
        PWMCON${i}bits.FLTIF = 0;
    }

    ${.vars[ifs]}CLR = _${.vars[ifs]}_PWM${i}IF_MASK;    //Clear IRQ flag

    <#if .vars[cl_enable]>
    PWMCON${i}bits.CLIEN = 1;
    </#if>
    <#if .vars[fault_enable]>
    PWMCON${i}bits.FLTIEN = 1;
    </#if>

    if( (${MCPWM_INSTANCE_NAME?lower_case}Obj[${i - 1}].callback != NULL))
    {
        ${MCPWM_INSTANCE_NAME?lower_case}Obj[${i - 1}].callback(status, ${MCPWM_INSTANCE_NAME?lower_case}Obj[${i - 1}].context);
    }
}

</#if>
</#list>

<#if interrupt_mode == true>
void ${MCPWM_INSTANCE_NAME}_CallbackRegister(MCPWM_CH_NUM channel, MCPWM_CH_CALLBACK callback, uintptr_t context)
{
    ${MCPWM_INSTANCE_NAME?lower_case}Obj[channel].callback = callback;
    ${MCPWM_INSTANCE_NAME?lower_case}Obj[channel].context = context;
}
</#if>
