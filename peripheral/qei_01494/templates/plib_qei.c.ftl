/*******************************************************************************
  Quadrature Encoder Interface (${QEI_INSTANCE_NAME}) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${QEI_INSTANCE_NAME?lower_case}.c

  Summary:
    ${QEI_INSTANCE_NAME} Source File

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
#include "plib_${QEI_INSTANCE_NAME?lower_case}.h"

<#--Implementation-->
// *****************************************************************************

// *****************************************************************************
// Section: ${QEI_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#assign INTERRUPT_MODE = false>
<#if QEI_QEISTAT?number != 0>
  <#assign INTERRUPT_MODE = true>
</#if>

<#if INTERRUPT_MODE == true>
QEI_CH_OBJECT ${QEI_INSTANCE_NAME?lower_case}Obj;
</#if>

void ${QEI_INSTANCE_NAME}_Initialize (void)
{
<#list QEI_INSTANCE_NUM?number .. QEI_INSTANCE_NUM?number as i>
<#assign QEIICC = "QEI"+i+"ICC__ICCH">
<#assign QEICMPL = "QEI"+i+"CMPL__CMPL">

<#assign CCM = "QEI"+i+"CON__CCM">
<#assign GATEN = "QEI"+i+"CON__GATEN">
<#assign CNTPOL = "QEI"+i+"CON__CNTPOL">
<#assign INTDIV = "QEI"+i+"CON__INTDIV">
<#assign IMV = "QEI"+i+"CON__IMV">
<#assign PIMOD = "QEI"+i+"CON__PIMOD">
<#assign QEISIDL = "QEI"+i+"CON__QEISIDL">

<#assign QEAPOL = "QEI"+i+"IOC__QEAPOL">
<#assign QEBPOL = "QEI"+i+"IOC__QEBPOL">
<#assign IDXPOL = "QEI"+i+"IOC__IDXPOL">
<#assign HOMPOL = "QEI"+i+"IOC__HOMPOL">
<#assign SWPAB = "QEI"+i+"IOC__SWPAB">
<#assign OUTFNC = "QEI"+i+"IOC__OUTFNC">
<#assign QFDIV = "QEI"+i+"IOC__QFDIV">
<#assign FLTREN = "QEI"+i+"IOC__FLTREN">

<#assign IDXIEN = "QEI"+i+"STAT__IDXIEN">
<#assign HOMIEN = "QEI"+i+"STAT__HOMIEN">
<#assign VELOVIEN = "QEI"+i+"STAT__VELOVIEN">
<#assign POSOVIEN = "QEI"+i+"STAT__POSOVIEN">
<#assign PCIIEN = "QEI"+i+"STAT__PCIIEN">
<#assign PCLEQIEN = "QEI"+i+"STAT__PCLEQIEN">
<#assign PCHEQIEN = "QEI"+i+"STAT__PCHEQIEN">

    /* QEI${QEI_INSTANCE_NUM}CON register  */
    /*  CCM    = ${.vars[CCM]} */
    /*  GATEN  = ${.vars[GATEN]} */
    /*  CNTPOL = ${.vars[CNTPOL]} */
    /*  INTDIV = ${.vars[INTDIV]} */
    /*  IMV    = ${.vars[IMV]}  */
    /*  PIMOD  = ${.vars[PIMOD]}  */
    /*  QEISIDL = ${.vars[QEISIDL]} */
    QEI${QEI_INSTANCE_NUM}CON = 0x${QEI_QEICON};

    /* QEI${QEI_INSTANCE_NUM}IOC register  */
    /*  QEAPOL    = ${.vars[QEAPOL]} */
    /*  QEBPOL  = ${.vars[QEBPOL]} */
    /*  IDXPOL = ${.vars[IDXPOL]} */
    /*  HOMPOL = ${.vars[HOMPOL]} */
    /*  SWPAB    = ${.vars[SWPAB]}  */
    /*  OUTFNC  = ${.vars[OUTFNC]}  */
    /*  QFDIV   = ${.vars[QFDIV]}   */
    /*  FLTREN  = ${.vars[FLTREN]}   */
    QEI${QEI_INSTANCE_NUM}IOC = 0x${QEI_QEIIOC};

    QEI${QEI_INSTANCE_NUM}ICC = ${.vars[QEIICC]};
    QEI${QEI_INSTANCE_NUM}CMPL = ${.vars[QEICMPL]};

    /* QEI${QEI_INSTANCE_NUM}STAT register  */
    /*  IDXIEN    = ${.vars[IDXIEN]?then('true', 'false')} */
    /*  HOMIEN  = ${.vars[HOMIEN]?then('true', 'false')} */
    /*  VELOVIEN = ${.vars[VELOVIEN]?then('true', 'false')} */
    /*  POSOVIEN = ${.vars[POSOVIEN]?then('true', 'false')} */
    /*  PCIIEN    = ${.vars[PCIIEN]?then('true', 'false')}  */
    /*  PCLEQIEN  = ${.vars[PCLEQIEN]?then('true', 'false')}    */
    /*  PCHEQIEN = ${.vars[PCHEQIEN]?then('true', 'false')}     */
    QEI${QEI_INSTANCE_NUM}STAT = 0x${QEI_QEISTAT};
    <#if QEI_QEISTAT?number != 0>
    ${QEI_IEC_REG}SET = _${QEI_IEC_REG}_QEI${QEI_INSTANCE_NUM}IE_MASK;
    </#if>

</#list>
}


void ${QEI_INSTANCE_NAME}_Start()
{
    /* Enable QEI channel */
    QEI${QEI_INSTANCE_NUM}CON |= _QEI${QEI_INSTANCE_NUM}CON_QEIEN_MASK;
}

void ${QEI_INSTANCE_NAME}_Stop()
{
    /* Disable QEI channel */
    QEI${QEI_INSTANCE_NUM}CON &= ~_QEI${QEI_INSTANCE_NUM}CON_QEIEN_MASK;
}

uint32_t ${QEI_INSTANCE_NAME}_PulseIntervalGet()
{
    return (INT${QEI_INSTANCE_NUM}HLD);
}

void ${QEI_INSTANCE_NAME}_PositionWindowSet(uint32_t high_threshold, uint32_t low_threshold)
{
    QEI${QEI_INSTANCE_NUM}ICC  = high_threshold;
    QEI${QEI_INSTANCE_NUM}CMPL = low_threshold;
}

<#if INTERRUPT_MODE == true>
void ${QEI_INSTANCE_NAME}_CallbackRegister(QEI_CALLBACK callback, uintptr_t context)
{
    ${QEI_INSTANCE_NAME?lower_case}Obj.callback = callback;

    ${QEI_INSTANCE_NAME?lower_case}Obj.context = context;
}
</#if>

<#if INTERRUPT_MODE == true>
void QEI${QEI_INSTANCE_NUM}_InterruptHandler(void)
{
    QEI_STATUS status = (QEI_STATUS)(QEI${QEI_INSTANCE_NUM}STAT & QEI_STATUS_MASK);
    ${QEI_IFS_REG}CLR = _${QEI_IFS_REG}_QEI${QEI_INSTANCE_NUM}IF_MASK;
    if( (${QEI_INSTANCE_NAME?lower_case}Obj.callback != NULL))
    {
        ${QEI_INSTANCE_NAME?lower_case}Obj.callback(status, ${QEI_INSTANCE_NAME?lower_case}Obj.context);
    }
}
</#if>
