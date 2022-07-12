/*******************************************************************************
  AIC PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_aic.h

  Summary:
    Function implementations for the AIC PLIB.

  Description:
    This PLIB provides a simple interface to configure the Advanced Interrupt
    Controller.

*******************************************************************************/

//DOM-IGNORE-BEGIN
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
//DOM-IGNORE-END
#include <device.h>
#include "definitions.h"
#include "interrupts.h"

// *****************************************************************************
// *****************************************************************************
// Section: Local defines
// *****************************************************************************
// *****************************************************************************
<#if __PROCESSOR?matches("ATSAMA5.*")>
#define AICREDIR_KEY_GUARD 0xB6D81C4DU
</#if>

typedef void (*pfn_handler_t)(void);

// *****************************************************************************
// *****************************************************************************
// Section: Local Variables
// *****************************************************************************
// *****************************************************************************
/* data for irq register initialization */
static struct
{
    uint32_t        peripheralId;
    pfn_handler_t   handler;
    uint32_t        srcType;
    uint32_t        priority;
}irqData[] =
{
<#lt><#list AIC_VECTOR_MIN..AIC_VECTOR_MAX as ii>
    <#lt><#assign AIC_FIRST_NAME_KEY =  "AIC_FIRST_NAME_KEY" + ii?string >
    <#lt><#if .vars[AIC_FIRST_NAME_KEY]?has_content>
        <#lt><#assign AIC_FIRST_NAME = .vars[AIC_FIRST_NAME_KEY]>
        <#lt><#assign AIC_HANDLER = AIC_FIRST_NAME + "_INTERRUPT_HANDLER">
        <#lt><#assign AIC_ENABLE =  AIC_FIRST_NAME + "_INTERRUPT_ENABLE">
        <#lt><#if .vars[AIC_HANDLER]?? && .vars[AIC_ENABLE]?? && .vars[AIC_ENABLE]>
            <#lt><#assign AIC_MAP_TYPE = AIC_FIRST_NAME + "_INTERRUPT_MAP_TYPE">
            <#lt><#assign AIC_SRC_TYPE = AIC_FIRST_NAME + "_INTERRUPT_SRC_TYPE">
            <#lt><#assign AIC_PRIORITY = AIC_FIRST_NAME + "_INTERRUPT_PRIORITY">
            <#lt><#assign PERIPH_ID = (ii + "U,")?right_pad(5)>
            <#lt><#assign AIC_HANDLER_STR   = (.vars[AIC_HANDLER]  + ",")?right_pad(28) >
            <#lt><#assign AIC_SRC_TYPE_STR  = ("AIC_SMR_SRCTYPE_"  + .vars[AIC_SRC_TYPE] + "_Val,")?right_pad(42)>
            <#lt><#assign AIC_PRIORITY_STR  = .vars[AIC_PRIORITY] + "U">
            <#lt>    { ${PERIPH_ID}${AIC_HANDLER_STR}${AIC_SRC_TYPE_STR}${AIC_PRIORITY_STR} }<#sep>,</#sep>
        <#lt></#if>
    <#lt></#if>
<#lt></#list>
};

// *****************************************************************************
// *****************************************************************************
// Section: AIC Implementation
// *****************************************************************************
// *****************************************************************************

void AIC_INT_Initialize( void )
{
    const uint32_t MaxNumPeripherals = ${AIC_VECTOR_MAX + 1}U;
    const uint32_t MaxInterruptDepth = 8U;
    uint32_t ii;
    uint32_t irqDataEntryCount = sizeof(irqData) / sizeof(irqData[0]);

    __disable_irq();
    __DMB();
    __ISB();
<#if __PROCESSOR?matches("ATSAMA5.*")>
    /* All interrupts are managed by non secure AIC */
    SFR_REGS->SFR_AICREDIR = (AICREDIR_KEY_GUARD ^ SFR_REGS->SFR_SN1) | SFR_AICREDIR_NSAIC_Msk;
</#if>

    /* Disable all interrupts */
    for( ii= 0; ii < MaxNumPeripherals; ++ii )
    {
        AIC_REGS->AIC_SSR = AIC_SSR_INTSEL(ii);
        AIC_REGS->AIC_IDCR = AIC_IDCR_Msk;
<#if __PROCESSOR?matches("SAM9X.*")>
        AIC_REGS->AIC_FFDR = AIC_FFDR_Msk;
        AIC_REGS->AIC_SVRRDR = AIC_SVRRDR_Msk;
</#if>
        __DSB();
        __ISB();
        AIC_REGS->AIC_ICCR = AIC_ICCR_INTCLR_Msk;
    }

    /* pop all possible nested interrupts from internal hw stack */
    for( ii = 0; ii < MaxInterruptDepth; ++ii )
    {
        AIC_REGS->AIC_EOICR = AIC_EOICR_ENDIT_Msk;
    }

    /* Configure active interrupts */
    for( ii = 0; ii < irqDataEntryCount; ++ii )
    {
        AIC_REGS->AIC_SSR = AIC_SSR_INTSEL(irqData[ii].peripheralId);
        AIC_REGS->AIC_SMR = (AIC_REGS->AIC_SMR & ~AIC_SMR_SRCTYPE_Msk) | AIC_SMR_SRCTYPE( irqData[ii].srcType );
        AIC_REGS->AIC_SMR = (AIC_REGS->AIC_SMR & ~AIC_SMR_${AIC_SMR_PRIORITY_SYMBOL}_Msk) | AIC_SMR_${AIC_SMR_PRIORITY_SYMBOL}(irqData[ii].priority);
        AIC_REGS->AIC_SPU = (uint32_t) SPURIOUS_INTERRUPT_Handler;
        AIC_REGS->AIC_SVR = (uint32_t) irqData[ii].handler;
        AIC_REGS->AIC_IECR = AIC_IECR_Msk;
    }

    __DSB();
    __enable_irq();
    __ISB();
}

void AIC_INT_IrqEnable( void )
{
    __DMB();
    __enable_irq();
}

bool AIC_INT_IrqDisable( void )
{
    /* Add a volatile qualifier to the return value to prevent the compiler from optimizing out this function */
    volatile bool previousValue = ((CPSR_I_Msk & __get_CPSR()) != 0U);
    __disable_irq();
    __DMB();
    return( previousValue );
}

void AIC_INT_IrqRestore( bool state )
{
    if(state)
    {
        __DMB();
        __enable_irq();
    }
    else
    {
        __disable_irq();
        __DMB();
    }
}
