/*******************************************************************************
 Configurable Logic Cell (${CLC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CLC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${CLC_INSTANCE_NAME} PLIB Implementation file

  Description:
    This file defines the interface to the CDAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_${CLC_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: File Scope or Global Constants
// *****************************************************************************
// *****************************************************************************
<#if CLC_INTERRUPT_TYPE != "Disabled">
static CLC_CALLBACK_OBJECT ${CLC_INSTANCE_NAME?lower_case}CallbackObject;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${CLC_INSTANCE_NAME} Interface Routines
// *****************************************************************************
// *****************************************************************************
<#compress>
<#assign CLCxGLS = "">
<#list 1..4 as GATEx>
  <#list 1..4 as DSx>
    <#assign GDP = .vars["CLC_GATE" + GATEx + "_DS" + DSx + "_ENABLE"]>
    <#assign GDN = .vars["CLC_GATE" + GATEx + "_DS" + DSx + "_NEG_ENABLE"]>
    <#if GDP>
      <#assign CLCxGLS += ("_" + CLC_INSTANCE_NAME + "GLS_G" + GATEx + "D" + DSx + "T_MASK,")>
    </#if>
    <#if GDN>
      <#assign CLCxGLS += ("_" + CLC_INSTANCE_NAME + "GLS_G" + GATEx + "D" + DSx + "N_MASK,")>
    </#if>
  </#list>
</#list>

<#assign CLCxCON = "">
<#list 1..4 as GATEPOLx>
  <#if .vars["CLC_GATE" + GATEPOLx + "_OUTPUT_POLARITY"]>
    <#assign CLCxCON += "_" + CLC_INSTANCE_NAME +  "CON_G" + GATEPOLx + "POL_MASK,">
  </#if>
</#list>

<#if CLC_LOGIC_CELL_ENABLE>
  <#assign CLCxCON += "_" + CLC_INSTANCE_NAME +  "CON_ON_MASK,">
</#if>

<#if CLC_INTERRUPT_TYPE == "Rising Edge">
  <#assign CLCxCON += "_" + CLC_INSTANCE_NAME +  "CON_INTP_MASK,">
<#elseif CLC_INTERRUPT_TYPE == "Falling Edge">
  <#assign CLCxCON += "_" + CLC_INSTANCE_NAME +  "CON_INTN_MASK,">
</#if>

<#if CLC_PORT_ENABLE>
  <#assign CLCxCON += "_" + CLC_INSTANCE_NAME +  "CON_LCOE_MASK,">
</#if>

<#if CLC_LOGIC_CELL_OUTPUT_POLARITY>
  <#assign CLCxCON += "_" + CLC_INSTANCE_NAME +  "CON_LCPOL_MASK,">
</#if>

<#assign CLC_IFS_REG = "IFS" + CLC_IRQ_REG_INDEX>
</#compress>
void ${CLC_INSTANCE_NAME}_Initialize( void )
{
    /* Configure data sources */
    ${CLC_INSTANCE_NAME}SEL =  (((${CLC_DS1_OUTPUT} << _${CLC_INSTANCE_NAME}SEL_DS1_POSITION) & _${CLC_INSTANCE_NAME}SEL_DS1_MASK) |
                ((${CLC_DS2_OUTPUT} << _${CLC_INSTANCE_NAME}SEL_DS2_POSITION) & _${CLC_INSTANCE_NAME}SEL_DS2_MASK) |
                ((${CLC_DS3_OUTPUT} << _${CLC_INSTANCE_NAME}SEL_DS3_POSITION) & _${CLC_INSTANCE_NAME}SEL_DS3_MASK) |
                ((${CLC_DS4_OUTPUT} << _${CLC_INSTANCE_NAME}SEL_DS4_POSITION) & _${CLC_INSTANCE_NAME}SEL_DS4_MASK));

    /* Configure gates */
    <#if CLCxGLS?has_content>
      <#list CLCxGLS?remove_ending(",")?split(",") as CLCGLSVAL>
        <#if CLCGLSVAL?is_first>
          <#lt>    ${CLC_INSTANCE_NAME}GLS =  (${CLCGLSVAL}<#if CLCGLSVAL?is_last>);<#else> |</#if>
        <#else>
          <#lt>                ${CLCGLSVAL}<#if CLCGLSVAL?is_last>);<#else> |</#if>
        </#if>
      </#list>
    <#else>
      <#lt>    ${CLC_INSTANCE_NAME}GLS = 0x0;
    </#if>

    /* Configure logic cell */
    <#if CLCxCON?has_content>
      <#lt>    ${CLC_INSTANCE_NAME}CON = (((${CLC_LOGIC_CELL_MODE} << _${CLC_INSTANCE_NAME}CON_MODE_POSITION) & _${CLC_INSTANCE_NAME}CON_MODE_MASK)
      <#list CLCxCON?remove_ending(",")?split(",") as CLCxCONVAL>
          <#lt>               | ${CLCxCONVAL} <#if CLCxCONVAL?is_last>);</#if>
      </#list>
    <#else>
      <#lt>    ${CLC_INSTANCE_NAME}CON = ((${CLC_LOGIC_CELL_MODE} << _${CLC_INSTANCE_NAME}CON_MODE_POSITION) & _${CLC_INSTANCE_NAME}CON_MODE_MASK);
    </#if>

}

void ${CLC_INSTANCE_NAME}_Enable(bool enable)
{
  if(enable == true)
  {
    ${CLC_INSTANCE_NAME}CON |= _${CLC_INSTANCE_NAME}CON_ON_MASK;
  }
  else
  {
    ${CLC_INSTANCE_NAME}CON &= ~(_${CLC_INSTANCE_NAME}CON_ON_MASK);
  }
}

<#if CLC_INTERRUPT_TYPE != "Disabled">

void ${CLC_INSTANCE_NAME}_RegisterCallback(CLC_CALLBACK callback, uintptr_t context)
{
    ${CLC_INSTANCE_NAME?lower_case}CallbackObject.callback = callback;
    ${CLC_INSTANCE_NAME?lower_case}CallbackObject.context = context;
}

void  ${CLC_INSTANCE_NAME}_InterruptHandler(void)
{
    ${CLC_IFS_REG}CLR = _${CLC_IFS_REG}_${CLC_INSTANCE_NAME}IF_MASK;
    if((${CLC_INSTANCE_NAME?lower_case}CallbackObject.callback != NULL))
    {
        ${CLC_INSTANCE_NAME?lower_case}CallbackObject.callback(${CLC_INSTANCE_NAME?lower_case}CallbackObject.context);
    }
}
</#if>