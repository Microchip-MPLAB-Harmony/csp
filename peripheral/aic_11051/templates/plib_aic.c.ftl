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
#include "definitions.h"
<#lt><#if __PROCESSOR?matches("SAM9X60.*")>
    <#lt>#include "toolchain_specifics.h"    // __disable_irq, __enable_irq
<#lt></#if>

// *****************************************************************************
// *****************************************************************************
// Section: AIC Implementation
// *****************************************************************************
// *****************************************************************************
extern IrqData  irqData[2];
extern uint32_t irqDataEntryCount;
<#lt><#if AIC_CODE_GENERATION != "NONE" >
void DefaultInterruptHandlerForSpurious( void );
<#lt></#if>

void
INT_Initialize( void )
{   <#-- // DSB/ISB/DMB usage is based on ARM app note 321, section 4.6 -->
<#lt><#if AIC_CODE_GENERATION == "AIC" || AIC_CODE_GENERATION == "SAIC" || AIC_CODE_GENERATION == "AICandSAIC" >
    <#lt><#assign MaxNumPeripherals = AIC_VECTOR_MAX + 1>
    <#lt><#if __PROCESSOR?matches("ATSAMA5.*")>
        <#lt>    const uint32_t      keyGuard = 0xb6d81c4d;
    <#lt></#if>
    <#lt>    const unsigned      MaxNumPeripherals = ${MaxNumPeripherals};
    const unsigned      MaxInterruptDepth = 8;
    uint32_t            ii;
    aic_registers_t *   aicPtr;

    __disable_irq();
    __DMB();                                                // Data Memory Barrier
    __ISB();                                                // Instruction Synchronization Barrier
    <#lt><#if __PROCESSOR?matches("ATSAMA5.*")>
        <#lt><#if SECURE_TO_NONSECURE_REDIRECTION >
            <#lt>    ////// secure to nonSecure redirection
            <#lt>    SFR_REGS->SFR_AICREDIR = (keyGuard ^ SFR_REGS->SFR_SN1) | SFR_AICREDIR_NSAIC_Msk;
        <#lt><#else>
            <#lt>    ////// disable secure to nonSecure redirection
            <#lt>    SFR_REGS->SFR_AICREDIR = (keyGuard ^ SFR_REGS->SFR_SN1) & ~SFR_AICREDIR_NSAIC_Msk;
        <#lt></#if>
    <#lt></#if>
    <#lt><#if AIC_CODE_GENERATION == "AIC" || AIC_CODE_GENERATION == "AICandSAIC" >
    //////
    aicPtr = (aic_registers_t *) AIC_REGS;
    for( ii= 0; ii < MaxNumPeripherals; ++ii )
    {
        aicPtr->AIC_SSR = AIC_SSR_INTSEL( ii );
        aicPtr->AIC_IDCR = AIC_IDCR_Msk;
        <#lt><#if __PROCESSOR?matches("SAM9X60.*")>
            <#lt>        aicPtr->AIC_FFDR = AIC_FFDR_Msk;
            <#lt>        aicPtr->AIC_SVRRDR = AIC_SVRRDR_Msk;
        <#lt></#if>
        __DSB();
        __ISB();
        aicPtr->AIC_ICCR = AIC_ICCR_INTCLR_Msk;
    }
    for( ii = 0; ii < MaxInterruptDepth; ++ii )
    {   // pop all possible nested interrupts from internal hw stack
        aicPtr->AIC_EOICR = AIC_EOICR_ENDIT_Msk;
    }

    <#lt></#if>
    <#lt><#if AIC_CODE_GENERATION == "SAIC" || AIC_CODE_GENERATION == "AICandSAIC" >
    ////// secure registers
    aicPtr = (aic_registers_t *) SAIC_REGS;
    for( ii = 0; ii < MaxNumPeripherals; ++ii )
    {
        aicPtr->AIC_SSR = AIC_SSR_INTSEL( ii );
        aicPtr->AIC_IDCR = AIC_IDCR_Msk;
        __DSB();
        __ISB();
        aicPtr->AIC_ICCR = AIC_ICCR_INTCLR_Msk;
    }
    for( ii = 0; ii < MaxInterruptDepth; ++ii )
    {   // pop all possible nested interrupts from internal hw stack
        aicPtr->AIC_EOICR = AIC_EOICR_ENDIT_Msk;
    }

    <#lt></#if>
    for( ii = 0; ii < irqDataEntryCount; ++ii )
    {   // inspect irqData array in interrupts.c to see the configuration data 
        aicPtr = (aic_registers_t *) irqData[ ii ].targetRegisters;
        aicPtr->AIC_SSR = AIC_SSR_INTSEL( irqData[ ii ].peripheralId );
        aicPtr->AIC_SMR = (aicPtr->AIC_SMR & ~${AIC_SMR_SRCTYPE_SYMBOL}_Msk)  | ${AIC_SMR_SRCTYPE_SYMBOL}( irqData[ ii ].srcType );
        aicPtr->AIC_SMR = (aicPtr->AIC_SMR & ~${AIC_SMR_PRIORITY_SYMBOL}_Msk) | (irqData[ ii ].priority << ${AIC_SMR_PRIORITY_SYMBOL}_Pos);
        aicPtr->AIC_SPU = (uint32_t) DefaultInterruptHandlerForSpurious;
        aicPtr->AIC_SVR = (uint32_t) irqData[ ii ].handler;
        aicPtr->AIC_IECR = AIC_IECR_Msk;
    }
    //////
    __DSB();                                                // Data Synchronization Barrier
<#lt></#if>
    __enable_irq();
    __ISB();                                                // Allow pended interrupts to be recognized immediately
}
