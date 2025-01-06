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
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

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
static volatile QEI_CH_OBJECT ${QEI_INSTANCE_NAME?lower_case}Obj;
</#if>

void ${QEI_INSTANCE_NAME}_Initialize (void)
{

<#assign QEIICC = "QEI"+QEI_INSTANCE_NUM+"ICC__ICCH">
<#assign QEICMPL = "QEI"+QEI_INSTANCE_NUM+"CMPL__CMPL">

<#assign CCM = "QEI"+QEI_INSTANCE_NUM+"CON__CCM">
<#assign GATEN = "QEI"+QEI_INSTANCE_NUM+"CON__GATEN">
<#assign CNTPOL = "QEI"+QEI_INSTANCE_NUM+"CON__CNTPOL">
<#assign INTDIV = "QEI"+QEI_INSTANCE_NUM+"CON__INTDIV">
<#assign IMV = "QEI"+QEI_INSTANCE_NUM+"CON__IMV">
<#assign PIMOD = "QEI"+QEI_INSTANCE_NUM+"CON__PIMOD">
<#assign QEISIDL = "QEI"+QEI_INSTANCE_NUM+"CON__QEISIDL">

<#assign QEAPOL = "QEI"+QEI_INSTANCE_NUM+"IOC__QEAPOL">
<#assign QEBPOL = "QEI"+QEI_INSTANCE_NUM+"IOC__QEBPOL">
<#assign IDXPOL = "QEI"+QEI_INSTANCE_NUM+"IOC__IDXPOL">
<#assign HOMPOL = "QEI"+QEI_INSTANCE_NUM+"IOC__HOMPOL">
<#assign SWPAB = "QEI"+QEI_INSTANCE_NUM+"IOC__SWPAB">
<#assign OUTFNC = "QEI"+QEI_INSTANCE_NUM+"IOC__OUTFNC">
<#assign QFDIV = "QEI"+QEI_INSTANCE_NUM+"IOC__QFDIV">
<#assign FLTREN = "QEI"+QEI_INSTANCE_NUM+"IOC__FLTREN">

<#assign IDXIEN = "QEI"+QEI_INSTANCE_NUM+"STAT__IDXIEN">
<#assign HOMIEN = "QEI"+QEI_INSTANCE_NUM+"STAT__HOMIEN">
<#assign VELOVIEN = "QEI"+QEI_INSTANCE_NUM+"STAT__VELOVIEN">
<#assign POSOVIEN = "QEI"+QEI_INSTANCE_NUM+"STAT__POSOVIEN">
<#assign PCIIEN = "QEI"+QEI_INSTANCE_NUM+"STAT__PCIIEN">
<#assign PCLEQIEN = "QEI"+QEI_INSTANCE_NUM+"STAT__PCLEQIEN">
<#assign PCHEQIEN = "QEI"+QEI_INSTANCE_NUM+"STAT__PCHEQIEN">

    /* QEI${QEI_INSTANCE_NUM}CON register  */
    /*  CCM    = ${.vars[CCM]} */
    /*  GATEN  = ${.vars[GATEN]} */
    /*  CNTPOL = ${.vars[CNTPOL]} */
    /*  INTDIV = ${.vars[INTDIV]} */
    /*  IMV    = ${.vars[IMV]}  */
    /*  PIMOD  = ${.vars[PIMOD]}  */
    /*  QEISIDL = ${.vars[QEISIDL]} */
    ${QEI_INSTANCE_NAME}_REGS->QEI_QEICON = 0x${QEI_QEICON};

    /* QEI${QEI_INSTANCE_NUM}IOC register  */
    /*  QEAPOL    = ${.vars[QEAPOL]} */
    /*  QEBPOL  = ${.vars[QEBPOL]} */
    /*  IDXPOL = ${.vars[IDXPOL]} */
    /*  HOMPOL = ${.vars[HOMPOL]} */
    /*  SWPAB    = ${.vars[SWPAB]}  */
    /*  OUTFNC  = ${.vars[OUTFNC]}  */
    /*  QFDIV   = ${.vars[QFDIV]}   */
    /*  FLTREN  = ${.vars[FLTREN]}   */
    ${QEI_INSTANCE_NAME}_REGS->QEI_QEIIOC = 0x${QEI_QEIIOC};

    ${QEI_INSTANCE_NAME}_REGS->QEI_QEIICC = ${.vars[QEIICC]}U;
    ${QEI_INSTANCE_NAME}_REGS->QEI_QEICMPL = ${.vars[QEICMPL]}U;

    /* QEI${QEI_INSTANCE_NUM}STAT register  */
    /*  IDXIEN    = ${.vars[IDXIEN]?then('true', 'false')} */
    /*  HOMIEN  = ${.vars[HOMIEN]?then('true', 'false')} */
    /*  VELOVIEN = ${.vars[VELOVIEN]?then('true', 'false')} */
    /*  POSOVIEN = ${.vars[POSOVIEN]?then('true', 'false')} */
    /*  PCIIEN    = ${.vars[PCIIEN]?then('true', 'false')}  */
    /*  PCLEQIEN  = ${.vars[PCLEQIEN]?then('true', 'false')}    */
    /*  PCHEQIEN = ${.vars[PCHEQIEN]?then('true', 'false')}     */
    ${QEI_INSTANCE_NAME}_REGS->QEI_QEISTAT = 0x${QEI_QEISTAT};
}


void ${QEI_INSTANCE_NAME}_Start(void)
{
    /* Enable QEI channel */
    ${QEI_INSTANCE_NAME}_REGS->QEI_QEICONSET = QEI_QEICON_ON_Msk;
}

void ${QEI_INSTANCE_NAME}_Stop(void)
{
    /* Disable QEI channel */
    ${QEI_INSTANCE_NAME}_REGS->QEI_QEICONCLR = QEI_QEICON_ON_Msk;
}

uint32_t ${QEI_INSTANCE_NAME}_PulseIntervalGet(void)
{
    return ${QEI_INSTANCE_NAME}_REGS->QEI_INTHLD;
}

void ${QEI_INSTANCE_NAME}_PositionWindowSet(uint32_t high_threshold, uint32_t low_threshold)
{
    ${QEI_INSTANCE_NAME}_REGS->QEI_QEIICC   = high_threshold;
    ${QEI_INSTANCE_NAME}_REGS->QEI_QEICMPL  = low_threshold;
}

void ${QEI_INSTANCE_NAME}_PositionCountSet(uint32_t position_count)
{
    ${QEI_INSTANCE_NAME}_REGS->QEI_POSCNT = position_count;
}

void ${QEI_INSTANCE_NAME}_VelocityCountSet(uint32_t velocity_count)
{
    ${QEI_INSTANCE_NAME}_REGS->QEI_VELCNT = velocity_count;
}

<#if INTERRUPT_MODE == true>
void ${QEI_INSTANCE_NAME}_CallbackRegister(QEI_CALLBACK callback, uintptr_t context)
{
    ${QEI_INSTANCE_NAME?lower_case}Obj.callback = callback;

    ${QEI_INSTANCE_NAME?lower_case}Obj.context = context;
}
</#if>

<#if INTERRUPT_MODE == true>
void __attribute__((used)) QEI${QEI_INSTANCE_NUM}_InterruptHandler(void)
{
    /* Additional local variable to prevent MISRA C violations (Rule 13.x) */
    uintptr_t context = ${QEI_INSTANCE_NAME?lower_case}Obj.context;
    QEI_STATUS status = (${QEI_INSTANCE_NAME}_REGS->QEI_QEISTAT & (uint32_t)QEI_STATUS_MASK);

    if( (${QEI_INSTANCE_NAME?lower_case}Obj.callback != NULL))
    {
        ${QEI_INSTANCE_NAME?lower_case}Obj.callback(status, context);
    }
}
</#if>
