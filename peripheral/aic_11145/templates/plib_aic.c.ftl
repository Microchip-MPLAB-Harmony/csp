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
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
//DOM-IGNORE-END
#include "definitions.h"

// *****************************************************************************
// *****************************************************************************
// Section: AIC Implementation
// *****************************************************************************
// *****************************************************************************
<#if AIC_CODE_GENERATION != "NONE" >
void DefaultInterruptHandler(               void );
void DefaultInterruptHandlerForSpurious(    void );
<#if NUM_SHARED_VECTORS?? >
<#list 0..(NUM_SHARED_VECTORS - 1) as ii>
<#assign SHARED_VECTOR_NAME =  "SHARED_VECTOR_" + ii?string >
<#assign PROTOTYPE = "void " + .vars[ SHARED_VECTOR_NAME ] + "_SharedHandler( ">
${PROTOTYPE?right_pad(44)}void );
</#list>
</#if>
</#if>

void
INT_Initialize( void )
{   <#-- // DSB/ISB/DMB usage is based on ARM app note 321, section 4.6 -->
    <#if AIC_CODE_GENERATION == "AIC" || AIC_CODE_GENERATION == "SAIC" || AIC_CODE_GENERATION == "AICandSAIC" >
    const unsigned      MaxInterruptDepth = 8;
    const unsigned      MaxNumPeripherals = 0x7F;           // 127
    const uint32_t      keyGuard = 0xb6d81c4d;
    aic_registers_t *   aicPtr;

    __disable_irq();
    __DMB();                                                // Data Memory Barrier
    __ISB();                                                // Instruction Synchronization Barrier

    <#if SECURE_TO_NONSECURE_REDIRECTION >
    ////// secure to nonSecure redirection
    SFR_REGS->SFR_AICREDIR = (keyGuard ^ SFR_REGS->SFR_SN1) | SFR_AICREDIR_NSAIC_Msk;
    <#else>
    ////// disable secure to nonSecure redirection
    SFR_REGS->SFR_AICREDIR = (keyGuard ^ SFR_REGS->SFR_SN1) & ~SFR_AICREDIR_NSAIC_Msk;
    </#if>
    <#if AIC_CODE_GENERATION == "AIC" || AIC_CODE_GENERATION == "AICandSAIC" >
    ////// nonsecure register initializations
    aicPtr = (aic_registers_t *) AIC_REGS;
    for( unsigned periphId = 0; periphId < MaxNumPeripherals; ++periphId )
    {
        aicPtr->AIC_SSR = AIC_SSR_INTSEL( periphId );
        aicPtr->AIC_IDCR = AIC_IDCR_Msk;
        __DSB();
        __ISB();
        aicPtr->AIC_ICCR = AIC_ICCR_INTCLR_Msk;
    }
    for( unsigned ii = 0; ii < MaxInterruptDepth; ++ii )
    {   // pop all possible nested interrupts from internal hw stack
        aicPtr->AIC_EOICR = AIC_EOICR_ENDIT_Msk;
    }

    aicPtr->AIC_SPU = (uint32_t) DefaultInterruptHandlerForSpurious;
    for( unsigned periphId = 1; periphId < MaxNumPeripherals; ++periphId )
    {
        aicPtr->AIC_SVR = (uint32_t) DefaultInterruptHandler;
    }
    </#if>
    <#if AIC_CODE_GENERATION == "SAIC" || AIC_CODE_GENERATION == "AICandSAIC" >
    ////// secure register initializations
    aicPtr = (aic_registers_t *) SAIC_REGS;
    for( unsigned periphId = 0; periphId < MaxNumPeripherals; ++periphId )
    {
        aicPtr->AIC_SSR = AIC_SSR_INTSEL( periphId );
        aicPtr->AIC_IDCR = AIC_IDCR_Msk;
        __DSB();
        __ISB();
        aicPtr->AIC_ICCR = AIC_ICCR_INTCLR_Msk;
    }
    for( unsigned ii = 0; ii < MaxInterruptDepth; ++ii )
    {   // pop all possible nested interrupts from internal hw stack
        aicPtr->AIC_EOICR = AIC_EOICR_ENDIT_Msk;
    }

    aicPtr->AIC_SPU = (uint32_t) DefaultInterruptHandlerForSpurious;
    for( unsigned periphId = 1; periphId < MaxNumPeripherals; ++periphId )
    {
        aicPtr->AIC_SVR = (uint32_t) DefaultInterruptHandler;
    }
    </#if>

<#list AIC_VECTOR_MIN..AIC_VECTOR_MAX as ii>
    <#assign AIC_FIRST_NAME_KEY =  "AIC_FIRST_NAME_KEY" + ii?string >
    <#if .vars[AIC_FIRST_NAME_KEY]?has_content>
        <#assign AIC_FIRST_NAME = .vars[AIC_FIRST_NAME_KEY]>
        <#assign AIC_MAP_TYPE = AIC_FIRST_NAME + "_INTERRUPT_MAP_TYPE">
        <#assign AIC_VECTOR =   AIC_FIRST_NAME + "_INTERRUPT_VECTOR">
        <#assign AIC_ENABLE =   AIC_FIRST_NAME + "_INTERRUPT_ENABLE">
        <#assign AIC_SRC_TYPE = AIC_FIRST_NAME + "_INTERRUPT_SRC_TYPE">
        <#assign AIC_PRIORITY = AIC_FIRST_NAME + "_INTERRUPT_PRIORITY">
        <#assign AIC_HANDLER =  AIC_FIRST_NAME + "_INTERRUPT_HANDLER">
        <#if .vars[AIC_VECTOR]?? && .vars[AIC_ENABLE]?? && .vars[AIC_ENABLE]>
    ////// ${.vars[AIC_VECTOR]} as configured by MCC
            <#if (.vars[AIC_MAP_TYPE]?string == "NonSecure") || (.vars[AIC_MAP_TYPE]?string == "Redirected")>
    aicPtr = (aic_registers_t *) AIC_REGS;
            <#else>
    aicPtr = (aic_registers_t *) SAIC_REGS;
            </#if>
    aicPtr->AIC_SSR = AIC_SSR_INTSEL( ${.vars[AIC_VECTOR]} );
    aicPtr->AIC_SMR = (aicPtr->AIC_SMR & ~AIC_SMR_SRCTYPE_Msk) | AIC_SMR_SRCTYPE( AIC_SMR_SRCTYPE_${.vars[AIC_SRC_TYPE]}_Val );
    aicPtr->AIC_SMR = (aicPtr->AIC_SMR & ~AIC_SMR_PRIORITY_Msk) | ((uint32_t) AIC_SMR_PRIORITY_${.vars[AIC_PRIORITY]}_Val << AIC_SMR_PRIORITY_Pos);
    aicPtr->AIC_SVR = (uint32_t) ${.vars[AIC_HANDLER]};
    aicPtr->AIC_IECR = AIC_IECR_Msk;
            
        </#if>
    </#if>
</#list>
    //////
    __DSB();                                                // Data Synchronization Barrier
    </#if>
    __enable_irq();
    __ISB();                                                // Allow pended interrupts to be recognized immediately
}
