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

#include "plib_${RSTC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: RSTC Implementation
// *****************************************************************************
// *****************************************************************************

void ${RSTC_INSTANCE_NAME}_Initialize (void)
{
<#if RSTC_MR_URSTEN_PRESENT == true>
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_MR = (<#rt>
<#t><#if RSTC_MR_URSTEN == "RESET">RSTC_MR_URSTEN_Msk<#else>RSTC_MR_URSTIEN_Msk</#if>
<#t><#if RSTC_MR_ERSTL??> | RSTC_MR_ERSTL(${RSTC_MR_ERSTL}U)</#if>
<#t><#if ENABLE_32K_FAIL_DETECT?? && ENABLE_32K_FAIL_DETECT> | RSTC_MR_SCKSW_Msk</#if>
<#t><#if RSTC_MR_CPUFEN?? && RSTC_MR_CPUFEN> | RSTC_MR_CPUFEN_Msk</#if>
<#rt> | RSTC_MR_KEY_PASSWD);
<#elseif (ENABLE_32K_FAIL_DETECT?? && ENABLE_32K_FAIL_DETECT) || (RSTC_MR_CPUFEN?? && RSTC_MR_CPUFEN)>
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_MR = (<#if ENABLE_32K_FAIL_DETECT?? && ENABLE_32K_FAIL_DETECT>RSTC_MR_SCKSW_Msk</#if><#rt>
<#t><#if RSTC_MR_CPUFEN?? && RSTC_MR_CPUFEN><#if (ENABLE_32K_FAIL_DETECT?? && ENABLE_32K_FAIL_DETECT)> | </#if>RSTC_MR_CPUFEN_Msk</#if>
<#rt> | RSTC_MR_KEY_PASSWD);
</#if>

}

void ${RSTC_INSTANCE_NAME}_Reset (RSTC_RESET_TYPE type)
{
    /* Issue reset command              */
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_CR = RSTC_CR_KEY_PASSWD | type;

    while ((${RSTC_INSTANCE_NAME}_REGS->RSTC_SR& (uint32_t) RSTC_SR_SRCMP_Msk) != 0U)
    {
        /*Wait for processing reset command */
    }
}

RSTC_RESET_CAUSE ${RSTC_INSTANCE_NAME}_ResetCauseGet (void)
{
    return (RSTC_RESET_CAUSE) (${RSTC_INSTANCE_NAME}_REGS->RSTC_SR& RSTC_SR_RSTTYP_Msk);
}

<#if RSTC_MR_URSTEN == "GPIO">
bool ${RSTC_INSTANCE_NAME}_NRSTPinRead (void)
{
    return  ((${RSTC_INSTANCE_NAME}_REGS->RSTC_SR& RSTC_SR_NRSTL_Msk) != 0U);
}
</#if>

<#if RSTC_MR_URSTEN == "INTERRUPT">
static RSTC_OBJECT rstcObj;

void ${RSTC_INSTANCE_NAME}_CallbackRegister (RSTC_CALLBACK callback, uintptr_t context)
{
    rstcObj.callback = callback;
    rstcObj.context = context;
}

void ${RSTC_INSTANCE_NAME}_InterruptHandler( void )
{
    // Clear the interrupt flag
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_SR;

    // Callback user function
    if(rstcObj.callback != NULL)
    {
        rstcObj.callback(rstcObj.context);
    }
}
</#if>
