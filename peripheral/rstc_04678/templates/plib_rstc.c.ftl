/*******************************************************************************
  Reset Controller (RSTC) Peripheral Library(PLIB) Source file

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RSTC_INSTANCE_NAME?lower_case}.c

  Summary:
    RSTC Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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
#include <stddef.h>
#include "plib_${RSTC_INSTANCE_NAME?lower_case}.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: RSTC Implementation
// *****************************************************************************
// *****************************************************************************
<#assign RESET_MD_SLCK_CYCLES = 2>
#define NUM_RESET_MD_CLOCK_CYCLES ${RESET_MD_SLCK_CYCLES}U
#define RESET_WAIT_COUNT  ((${CPU_CLOCK_FREQUENCY}U / 32000U) * NUM_RESET_MD_CLOCK_CYCLES)
<#if INTERRUPT_ENABLE>


typedef struct
{
    RSTC_CALLBACK pCallback;
    uintptr_t context;
}rstcCallback_t;


static rstcCallback_t rstcCallbackObj;
</#if>
<#if CPU_CORE_ID?? && CPU_CORE_ID == 0>

void ${RSTC_INSTANCE_NAME}_Initialize (void)
{
    if(RSTC_PMCResetStatusGet())
    {
        ${RSTC_INSTANCE_NAME}_REGS->RSTC_MR = ( RSTC_MR_KEY_PASSWD<#if RSTC_MR_ERSTL??> | RSTC_MR_ERSTL(${RSTC_MR_ERSTL}U)</#if><#if RSTC_MR_PWRSW??> | RSTC_MR_PWRSW(${RSTC_MR_PWRSW}U)</#if>
<#list RSTC_MODE_BITS?split(":") as MODE>
<#if .vars["RSTC_MR_" + MODE]>
                                | RSTC_MR_${MODE}_Msk
</#if>
</#list>
<#if RSTC_MR_URSTEN == "Reset">
                                | RSTC_MR_URSTEN_Msk
<#elseif  RSTC_MR_URSTEN == "Interrupt">
                                | RSTC_MR_URSTIEN_Msk
</#if>
                            );
<#if RSTC_MR_CPEREN?? && RSTC_MR_CPEREN>
        for(uint32_t i = 0U; i < RESET_WAIT_COUNT; i++)
        {
            /* Wait for ${RESET_MD_SLCK_CYCLES} MD_SLCK cycles after deasserting reset */
        }
</#if>
    }
}
</#if>

void ${RSTC_INSTANCE_NAME}_Reset (RSTC_RESET_TYPE type)
{
    /* Issue reset command              */
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_CR = (RSTC_CR_KEY_PASSWD | (uint32_t)type);
    while ((${RSTC_INSTANCE_NAME}_REGS->RSTC_SR & (uint32_t) RSTC_SR_SRCMP_Msk) != 0U)
    {
        /*Wait for processing reset command */
    }
}


RSTC_RESET_CAUSE ${RSTC_INSTANCE_NAME}_ResetCauseGet (void)
{
    return (${RSTC_INSTANCE_NAME}_REGS->RSTC_SR & RSTC_SR_RSTTYP_Msk);
}
<#if RSTC_MR_URSTEN == "No action">


bool ${RSTC_INSTANCE_NAME}_NRSTPinRead (void)
{
    return  (bool) (${RSTC_INSTANCE_NAME}_REGS->RSTC_SR& RSTC_SR_NRSTL_Msk);
}
</#if>
<#if RSTC_MR_CPROCEN??>


void ${RSTC_INSTANCE_NAME}_CoProcessorEnable(bool enable)
{
    uint32_t reg = ${RSTC_INSTANCE_NAME}_REGS->RSTC_MR & ~(RSTC_MR_KEY_Msk | RSTC_MR_CPROCEN_Msk);
    if(enable)
    {
        reg |= RSTC_MR_CPROCEN_Msk;
    }
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_MR = RSTC_MR_KEY_PASSWD | reg;
    for(uint32_t i = 0U; i < RESET_WAIT_COUNT; i++)
    {
        /* Wait for ${RESET_MD_SLCK_CYCLES} MD_SLCK cycles after deasserting reset */
    }
}
</#if>
<#if RSTC_MR_CPEREN??>


void ${RSTC_INSTANCE_NAME}_CoProcessorPeripheralEnable(bool enable)
{
    uint32_t reg = ${RSTC_INSTANCE_NAME}_REGS->RSTC_MR & ~(RSTC_MR_KEY_Msk | RSTC_MR_CPEREN_Msk);
    if(enable)
    {
        reg |= RSTC_MR_CPEREN_Msk;
    }
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_MR = (RSTC_MR_KEY_PASSWD | reg);
    for(uint32_t i = 0U; i < RESET_WAIT_COUNT; i++)
    {
        /* Wait for ${RESET_MD_SLCK_CYCLES} MD_SLCK cycles after deasserting reset */
    }
}
</#if>

bool ${RSTC_INSTANCE_NAME}_PMCResetStatusGet(void)
{
    bool pmc_reset = true;
        /* Reset cause is WDT0 and WDT0 do not reset PMC */
    if ((((${RSTC_INSTANCE_NAME}_REGS->RSTC_SR & RSTC_SR_RSTTYP_Msk) == RSTC_SR_RSTTYP_WDT0_RST) &&
         ((${RSTC_INSTANCE_NAME}_REGS->RSTC_MR & RSTC_MR_WDTPMC0_Msk) == 0U)) ||

        /* Reset cause is WDT1 and WDT1 do not reset PMC */
        (((${RSTC_INSTANCE_NAME}_REGS->RSTC_SR & RSTC_SR_RSTTYP_Msk) == RSTC_SR_RSTTYP_WDT1_RST) &&
         ((${RSTC_INSTANCE_NAME}_REGS->RSTC_MR & RSTC_MR_WDTPMC1_Msk) == 0U)) ||

        /* Reset cause is SW and SW reset do not reset PMC */
        (((${RSTC_INSTANCE_NAME}_REGS->RSTC_SR & RSTC_SR_RSTTYP_Msk) == RSTC_SR_RSTTYP_SOFT_RST) &&
         ((${RSTC_INSTANCE_NAME}_REGS->RSTC_MR & RSTC_MR_SFTPMCRS_Msk) == 0U)))
    {
        pmc_reset = false;
    }
    return pmc_reset;
}

<#if INTERRUPT_ENABLE>


void ${RSTC_INSTANCE_NAME}_CallbackRegister(RSTC_CALLBACK pCallback, uintptr_t context)
{
    rstcCallbackObj.pCallback = pCallback;
    rstcCallbackObj.context = context;
}


void ${RSTC_INSTANCE_NAME}_InterruptHandler(void)
{
    // Clear the interrupt flag
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_SR;

    if (rstcCallbackObj.pCallback != NULL)
    {
        rstcCallbackObj.pCallback(rstcCallbackObj.context);
    }
}
</#if>