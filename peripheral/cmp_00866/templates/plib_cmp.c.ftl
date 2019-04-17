/*******************************************************************************
  Comparator (CMP) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CMP_INSTANCE_NAME?lower_case}.c

  Summary:
    CMP Source File

  Description:
    None

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

#include "plib_${CMP_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${CMP_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${CMP_INSTANCE_NAME}_Initialize(void)
{
<#list 1..CMP_COUNT as i>
    /*  Setup CM${i}CON    */
    <#assign CMP_CMxCON_CCH = "CMP_CM" + i + "CON_CCH">
    <#assign CMP_CMxCON_CREF = "CMP_CM" + i + "CON_CREF">
    <#assign CMP_CMxCON_EVPOL = "CMP_CM" + i + "CON_EVPOL">
    <#assign CMP_CMxCON_CPOL = "CMP_CM" + i + "CON_CPOL">
    <#assign CMP_CMxCON_COE = "CMP_CM" + i + "CON_COE">
    <#assign CMP_CMxCON_VALUE = "CM" + i + "CON_VALUE">
    <#assign CMP_IEC_REG = "CMP" + i + "_IEC_REG">
    /*  CCH     = ${.vars[CMP_CMxCON_CCH]}    */
    /*  CREF    = ${.vars[CMP_CMxCON_CREF]}    */
    /*  EVPOL   = ${.vars[CMP_CMxCON_EVPOL]}    */
    /*  CPOL    = ${.vars[CMP_CMxCON_CPOL]?then('true', 'false')}    */
    /*  COE     = ${.vars[CMP_CMxCON_COE]?then('true', 'false')}    */
    CM${i}CON = 0x${.vars[CMP_CMxCON_VALUE]};

    <#if .vars[CMP_CMxCON_EVPOL] != "0">
        <#lt>    /* Enable Comparator ${i} Interrupt */
        <#lt>    ${.vars[CMP_IEC_REG]}SET = _${.vars[CMP_IEC_REG]}_${CMP_INSTANCE_NAME}${i}IE_MASK;

    </#if>
</#list>
<#if CMP_CMSTAT_SIDL??>
<#if CMP_CMSTAT_SIDL == true>
    /* Set Idle Control */
    CMSTATSET = _CMSTAT_SIDL_MASK;
<#else>
    /* Clear Idle Control */
    CMSTATCLR = _CMSTAT_SIDL_MASK;
</#if>
</#if>
}

bool ${CMP_INSTANCE_NAME}_StatusGet(CMP_STATUS_SOURCE ch_status)
{
    return ((CMSTAT & ch_status)?true:false);
}

<#list 1..CMP_COUNT as i>
<#assign CMP_CMxCON_EVPOL = "CMP_CM" + i + "CON_EVPOL">
<#assign CMP_IFS_REG = "CMP" + i + "_IFS_REG">
void ${CMP_INSTANCE_NAME}_${i}_CompareEnable(void)
{
    CM${i}CONSET = _CM${i}CON_ON_MASK;
}

void ${CMP_INSTANCE_NAME}_${i}_CompareDisable(void)
{
    CM${i}CONCLR = _CM${i}CON_ON_MASK;
}

<#if CMP_CMxCON_EVPOL != "0">
CMP_OBJECT cmp${i}Obj;

void ${CMP_INSTANCE_NAME}_${i}_CallbackRegister(CMP_CALLBACK callback, uintptr_t context)
{
    cmp${i}Obj.callback = callback;

    cmp${i}Obj.context = context;
}

void COMPARATOR_${i}_InterruptHandler(void)
{
    ${.vars[CMP_IFS_REG]}CLR = _${.vars[CMP_IFS_REG]}_${CMP_INSTANCE_NAME}${i}IF_MASK; //Clear IRQ flag

    if(cmp${i}Obj.callback != NULL)
    {
        cmp${i}Obj.callback(cmp${i}Obj.context);
    }
}

</#if>
</#list>
