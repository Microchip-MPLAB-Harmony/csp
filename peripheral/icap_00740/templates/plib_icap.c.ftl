/*******************************************************************************
  Input Capture (${ICAP_INSTANCE_NAME}) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${ICAP_INSTANCE_NAME?lower_case}.c

  Summary:
    ${ICAP_INSTANCE_NAME} Source File

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
#include "plib_${ICAP_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#assign INDEX = ICAP_INSTANCE_NUM>
<#if ICAP_NUM_INT_LINES == 1>
    <#if ICAP_ERROR_INTERRUPT_ENABLE?c == "true" || ICAP_INTERRUPT_ENABLE?c == "true">
        <#lt>static volatile ICAP_OBJECT ${ICAP_INSTANCE_NAME?lower_case}Obj;
    </#if>
<#else>
    <#if ICAP_ERROR_INTERRUPT_ENABLE?c == "true">
        <#lt>static volatile ICAP_OBJECT ${ICAP_INSTANCE_NAME?lower_case}errObj;
    </#if>
    <#if ICAP_INTERRUPT_ENABLE?c == "true">
        <#lt>static volatile ICAP_OBJECT ${ICAP_INSTANCE_NAME?lower_case}Obj;
    </#if>
</#if>
<#--Implementation-->
// *****************************************************************************

// *****************************************************************************
// Section: ${ICAP_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#assign ICAP_IEC_REG_VAL = "">

<#if ERROR_IEC_REG??>
    <#if ICAPx_IEC_REG == ERROR_IEC_REG>
        <#if ICAP_INTERRUPT_ENABLE?c == 'true'>
            <#assign ICAP_IEC_REG_VAL = "_"+ICAPx_IEC_REG+"_IC"+INDEX+"IE_MASK">
        </#if>
        <#if ICAP_ERROR_INTERRUPT_ENABLE?c == 'true'>
            <#if ICAP_IEC_REG_VAL != "">
                <#assign ICAP_IEC_REG_VAL = ICAP_IEC_REG_VAL + " | _"+ICAPx_IEC_REG+"_IC"+INDEX+"EIE_MASK">
            <#else>
                <#assign ICAP_IEC_REG_VAL = "_"+ICAPx_IEC_REG+"_IC"+INDEX+"EIE_MASK">
            </#if>
        </#if>
    </#if>
</#if>

void ${ICAP_INSTANCE_NAME}_Initialize (void)
{
    /*Setup IC${INDEX}CON    */
    /*ICM     = ${ICAP_ICxCON_ICM}        */
    /*ICI     = ${ICAP_ICxCON_ICI}        */
  <#if ICAP_CFGCON_ICACLK??>
    /*ICTMR = ${ICAP_CFGCON_ICACLK?then('${ICAP_ICxCON_ICTMR_ALT}','${ICAP_ICxCON_ICTMR}')}*/
  <#else>
    /*ICTMR = ${ICAP_ICxCON_ICTMR}*/
  </#if>
    /*C32     = ${ICAP_ICxCON_C32}        */
    /*FEDGE = ${ICAP_ICxCON_FEDGE}        */
    /*SIDL     = ${ICAP_ICxCON_SIDL?then('true', 'false')}    */

    IC${INDEX}CON = 0x${ICxCON_VALUE};

    <#if ICAP_CFGCON_ICACLK?? && ICAP_CFGCON_ICACLK?c == 'true'>
    /* unlock system for configuration */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;
    ${ICAP_CFG_REG_NAME} |= ${ICAP_CFGCON_ICACLK_MASK};
    /* Lock system since done with configuration */
    SYSKEY = 0x33333333;
    </#if>

<#if ERROR_IEC_REG??>
    <#if (ICAPx_IEC_REG == ERROR_IEC_REG) && ICAP_IEC_REG_VAL?has_content>
        ${ICAPx_IEC_REG}SET = ${ICAP_IEC_REG_VAL};
    <#else>
        <#if ICAP_INTERRUPT_ENABLE?c == 'true'>
        ${ICAPx_IEC_REG}SET = _${ICAPx_IEC_REG}_IC${INDEX}IE_MASK;
        </#if>
        <#if ICAP_ERROR_INTERRUPT_ENABLE?c == 'true'>
        ${ERROR_IEC_REG}SET = _${ERROR_IEC_REG}_IC${INDEX}EIE_MASK;
        </#if>
    </#if>
<#else>
    <#if ICAP_INTERRUPT_ENABLE?c == 'true'>
    ${ICAPx_IEC_REG}SET = _${ICAPx_IEC_REG}_IC${INDEX}IE_MASK;
    </#if>
</#if>
}


void ${ICAP_INSTANCE_NAME}_Enable (void)
{
    IC${INDEX}CONSET = _IC${INDEX}CON_ON_MASK;
}


void ${ICAP_INSTANCE_NAME}_Disable (void)
{
    IC${INDEX}CONCLR = _IC${INDEX}CON_ON_MASK;
}

<#if ICAP_ICxCON_C32 == "1">
uint32_t ${ICAP_INSTANCE_NAME}_CaptureBufferRead (void)
{
    return IC${INDEX}BUF;
}
<#else>
uint16_t ${ICAP_INSTANCE_NAME}_CaptureBufferRead (void)
{
    return (uint16_t)IC${INDEX}BUF;
}
</#if>

<#assign ICAP_Interrupt = false>
    <#if ICAP_NUM_INT_LINES == 1 && (ICAP_INTERRUPT_ENABLE?c == "true" || ICAP_ERROR_INTERRUPT_ENABLE?c == "true")>
      <#assign ICAP_Interrupt = true>
    <#else>
      <#if ICAP_INTERRUPT_ENABLE?c == "true">
        <#assign ICAP_Interrupt = true>
      </#if>
    </#if>

<#if ICAP_Interrupt == true>

void ${ICAP_INSTANCE_NAME}_CallbackRegister(ICAP_CALLBACK callback, uintptr_t context)
{
    ${ICAP_INSTANCE_NAME?lower_case}Obj.callback = callback;
    ${ICAP_INSTANCE_NAME?lower_case}Obj.context = context;
}

void __attribute__((used)) INPUT_CAPTURE_${INDEX}_InterruptHandler(void)
{
<#if ICAP_NUM_INT_LINES == 1>
    uint32_t iec_reg_read = ${ICAPx_IEC_REG};
    <#if ERROR_IEC_REG??>
    uint32_t error_reg_read = ${ERROR_IEC_REG};
    </#if>
</#if>
    uintptr_t context = ${ICAP_INSTANCE_NAME?lower_case}Obj.context;
    if( (${ICAP_INSTANCE_NAME?lower_case}Obj.callback != NULL))
    {
        ${ICAP_INSTANCE_NAME?lower_case}Obj.callback(context);
    }
<#if ICAP_NUM_INT_LINES == 1>
    if (((${ICAPx_IFS_REG} & _${ICAPx_IFS_REG}_IC${INDEX}IF_MASK) != 0U) &&
        ((iec_reg_read & _${ICAPx_IEC_REG}_IC${INDEX}IE_MASK) != 0U))
    {
        ${ICAPx_IFS_REG}CLR = _${ICAPx_IFS_REG}_IC${INDEX}IF_MASK;    //Clear IRQ flag
    }
    <#if ERROR_IEC_REG??>
    if (((${ERROR_IFS_REG} & _${ERROR_IFS_REG}_IC${INDEX}EIF_MASK) != 0U) &&
        ((error_reg_read & _${ERROR_IEC_REG}_IC${INDEX}EIE_MASK) != 0U))
    {
        ${ERROR_IFS_REG}CLR = _${ERROR_IFS_REG}_IC${INDEX}EIF_MASK;    //Clear IRQ flag
    }
    </#if>
<#else>
    ${ICAPx_IFS_REG}CLR = _${ICAPx_IFS_REG}_IC${INDEX}IF_MASK;    //Clear IRQ flag
</#if>

}
</#if>

<#if ICAP_INTERRUPT_ENABLE?c == "false">

bool ${ICAP_INSTANCE_NAME}_CaptureStatusGet (void)
{
    bool status = false;
    status = (((IC${INDEX}CON >> ICAP_STATUS_BUFNOTEMPTY) & 0x1U) != 0U);
    return status;
}
</#if>
<#if ICAP_NUM_INT_LINES != 1 && ICAP_ERROR_INTERRUPT_ENABLE?c == "true">

void ${ICAP_INSTANCE_NAME}_ErrorCallbackRegister(ICAP_CALLBACK callback, uintptr_t context)
{
    ${ICAP_INSTANCE_NAME?lower_case}errObj.callback = callback;
    ${ICAP_INSTANCE_NAME?lower_case}errObj.context = context;
}

void __attribute__((used)) INPUT_CAPTURE_${INDEX}_ERROR_InterruptHandler(void)
{
    if( (${ICAP_INSTANCE_NAME?lower_case}errObj.callback != NULL))
    {
        ${ICAP_INSTANCE_NAME?lower_case}errObj.callback(${ICAP_INSTANCE_NAME?lower_case}errObj.context);
    }
    ${ERROR_IFS_REG}CLR = _${ERROR_IFS_REG}_IC${INDEX}EIF_MASK;    //Clear IRQ flag
}
</#if>
<#if ICAP_ERROR_INTERRUPT_ENABLE?c == "false">

bool ${ICAP_INSTANCE_NAME}_ErrorStatusGet (void)
{
    bool status = false;
    status = (((IC${INDEX}CON >> ICAP_STATUS_OVERFLOW) & 0x1U) != 0U);
    return status;
}
</#if>
