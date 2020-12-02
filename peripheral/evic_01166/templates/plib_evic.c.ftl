/*******************************************************************************
  EVIC PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_evic.c

  Summary:
    EVIC PLIB Source File

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

#include "device.h"
#include "plib_evic.h"

<#assign NumOfEnabledExtInt = 0>

<#list 0..4 as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
        <#assign NumOfEnabledExtInt = NumOfEnabledExtInt + 1>
        <#lt>EXT_INT_PIN_CALLBACK_OBJ extInt${i}CbObj;
    </#if>
</#list>
// *****************************************************************************
// *****************************************************************************
// Section: IRQ Implementation
// *****************************************************************************
// *****************************************************************************

void EVIC_Initialize( void )
{
    INTCONSET = _INTCON_MVEC_MASK;

<#-- Note that this list will iterate through all the numbers between EVIC_VECTOR_MIN and MAX,
 but interrupt vectors and hence symbols, won't be present for all the numbers, so existance of symbols is a must-->
    <#lt>    /* Set up priority and subpriority of enabled interrupts */
<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#assign IPCREG = "EVIC_" + i + "_REGNAME">  <#-- IPCx register for given interrupt -->
    <#assign INT_PRIORITY_GENERATE = "EVIC_" + i + "_PRIORITY_GENERATE">
    <#assign PRIOVALUE = "EVIC_" + i + "_PRIORITY">
    <#assign SUBPRIOVALUE = "EVIC_" + i + "_SUBPRIORITY">
    <#assign PRIOVALUE_SHIFTED = "EVIC_" + i + "_PRIVALUE">  <#-- priority, shifted to correct place in IPCx register -->
    <#assign SUBPRIOVALUE_SHIFTED = "EVIC_" + i + "_SUBPRIVALUE">  <#-- subpriority, shifted to correct place in IPCx register -->
    <#assign INT_VECTOR_SUB_IRQ_COUNT = "EVIC_" + i + "_VECTOR_SUB_IRQ_COUNT">
    <#if .vars[INT_VECTOR_SUB_IRQ_COUNT]?? && ((.vars[INT_VECTOR_SUB_IRQ_COUNT] > 1) == true)>
        <#list 0..(.vars[INT_VECTOR_SUB_IRQ_COUNT]) as j>
            <#assign ENABLE = "EVIC_" + i + "_" + j + "_ENABLE">
            <#assign INT_NAME = "EVIC_" + i + "_" + j + "_NAME">
            <#if .vars[ENABLE]?? && .vars[ENABLE] == true>
                <#if !((.vars[INT_PRIORITY_GENERATE]??) && (.vars[INT_PRIORITY_GENERATE] == false))>
                    <#lt>    ${.vars[IPCREG]}SET = 0x${.vars[PRIOVALUE_SHIFTED]} | 0x${.vars[SUBPRIOVALUE_SHIFTED]};  /* ${.vars[INT_NAME]}:  Priority ${.vars[PRIOVALUE]} / Subpriority ${.vars[SUBPRIOVALUE]} */
                </#if>
            </#if>
        </#list>
    <#else>
        <#assign ENABLE = "EVIC_" + i + "_ENABLE">
        <#assign INT_NAME = "EVIC_" + i + "_NAME">
        <#if .vars[ENABLE]?? && .vars[ENABLE] == true>
            <#if !((.vars[INT_PRIORITY_GENERATE]??) && (.vars[INT_PRIORITY_GENERATE] == false))>
                <#lt>    ${.vars[IPCREG]}SET = 0x${.vars[PRIOVALUE_SHIFTED]} | 0x${.vars[SUBPRIOVALUE_SHIFTED]};  /* ${.vars[INT_NAME]}:  Priority ${.vars[PRIOVALUE]} / Subpriority ${.vars[SUBPRIOVALUE]} */
            </#if>
        </#if>
    </#if>
</#list>

<#assign externalInterruptPolarity = "">
<#list EVIC_VECTOR_MIN..EVIC_VECTOR_MAX as i>
    <#assign ENABLE = "EVIC_" + i + "_ENABLE">
    <#assign INT_NAME = "EVIC_" + i + "_NAME">
    <#assign EXTERNAL_INT_POLARITY = "EVIC_" + i + "_EXT_INT_EDGE_POLARITY">
    <#if .vars[ENABLE]?? && .vars[ENABLE] == true && .vars[INT_NAME]?contains("EXTERNAL_")>
        <#assign x = .vars[INT_NAME]?keep_after_last("_")>
        <#lt>    /* Initialize External interrupt ${x} callback object */
        <#lt>    extInt${x}CbObj.callback = NULL;
        <#-- External interrupt edge polarity configuration -->
        <#if .vars[EXTERNAL_INT_POLARITY]?? && .vars[EXTERNAL_INT_POLARITY] == "Rising Edge">
            <#if externalInterruptPolarity == "">
                <#assign externalInterruptPolarity = "_INTCON_INT" + "${x}" + "EP_MASK">
            <#else>
                <#assign externalInterruptPolarity = externalInterruptPolarity + " | " + "_INTCON_INT" + "${x}" + "EP_MASK" >
            </#if>
        </#if>
    </#if>
</#list>

<#if externalInterruptPolarity != "">

    /* Configure External Interrupt Edge Polarity */
    INTCONSET = ${externalInterruptPolarity};
</#if>
}

void EVIC_SourceEnable( INT_SOURCE source )
{
    volatile uint32_t *IECx = (volatile uint32_t *) (&IEC0 + ((0x10 * (source / 32)) / 4));
    volatile uint32_t *IECxSET = (volatile uint32_t *)(IECx + 2);

    *IECxSET = 1 << (source & 0x1f);
}

void EVIC_SourceDisable( INT_SOURCE source )
{
    volatile uint32_t *IECx = (volatile uint32_t *) (&IEC0 + ((0x10 * (source / 32)) / 4));
    volatile uint32_t *IECxCLR = (volatile uint32_t *)(IECx + 1);

    *IECxCLR = 1 << (source & 0x1f);
}

bool EVIC_SourceIsEnabled( INT_SOURCE source )
{
    volatile uint32_t *IECx = (volatile uint32_t *) (&IEC0 + ((0x10 * (source / 32)) / 4));

    return (bool)((*IECx >> (source & 0x1f)) & 0x01);
}

bool EVIC_SourceStatusGet( INT_SOURCE source )
{
    volatile uint32_t *IFSx = (volatile uint32_t *)(&IFS0 + ((0x10 * (source / 32)) / 4));

    return (bool)((*IFSx >> (source & 0x1f)) & 0x1);
}

void EVIC_SourceStatusSet( INT_SOURCE source )
{
    volatile uint32_t *IFSx = (volatile uint32_t *) (&IFS0 + ((0x10 * (source / 32)) / 4));
    volatile uint32_t *IFSxSET = (volatile uint32_t *)(IFSx + 2);

    *IFSxSET = 1 << (source & 0x1f);
}

void EVIC_SourceStatusClear( INT_SOURCE source )
{
    volatile uint32_t *IFSx = (volatile uint32_t *) (&IFS0 + ((0x10 * (source / 32)) / 4));
    volatile uint32_t *IFSxCLR = (volatile uint32_t *)(IFSx + 1);

    *IFSxCLR = 1 << (source & 0x1f);
}

void EVIC_INT_Enable( void )
{
    __builtin_enable_interrupts();
}

bool EVIC_INT_Disable( void )
{
    uint32_t processorStatus;

    /* Save the processor status and then Disable the global interrupt */
    processorStatus = ( uint32_t )__builtin_disable_interrupts();

    /* return the interrupt status */
    return (bool)(processorStatus & 0x01);
}

void EVIC_INT_Restore( bool state )
{
    if (state)
    {
        /* restore the state of CP0 Status register before the disable occurred */
        __builtin_enable_interrupts();
    }
}

<#if 0 < NumOfEnabledExtInt>
void EVIC_ExternalInterruptEnable( EXTERNAL_INT_PIN extIntPin )
{
    IEC0SET = extIntPin;
}
void EVIC_ExternalInterruptDisable( EXTERNAL_INT_PIN extIntPin )
{
    IEC0CLR = extIntPin;
}

bool EVIC_ExternalInterruptCallbackRegister(
    EXTERNAL_INT_PIN extIntPin,
    const EXTERNAL_INT_PIN_CALLBACK callback,
    uintptr_t context
)
{
    bool status = true;
    switch  (extIntPin)
        {
<#list 0..4 as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
        case EXTERNAL_INT_${i}:
            extInt${i}CbObj.callback = callback;
            extInt${i}CbObj.context  = context;
            break;
    </#if>
</#list>
        default:
            status = false;
            break;
        }

    return status;
}

<#list 0..4 as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
// *****************************************************************************
/* Function:
    void EXTERNAL_${i}_InterruptHandler()
  Summary:
    Interrupt Handler for External Interrupt pin ${i}.
  Remarks:
    It is an internal function called from ISR, user should not call it directly.
*/
void EXTERNAL_${i}_InterruptHandler()
{
    IFS0CLR = _IFS0_INT${i}IF_MASK;

    if(extInt${i}CbObj.callback != NULL)
        {
        extInt${i}CbObj.callback (EXTERNAL_INT_${i}, extInt${i}CbObj.context);
        }
    }

    </#if>
</#list>
</#if>
/* End of file */