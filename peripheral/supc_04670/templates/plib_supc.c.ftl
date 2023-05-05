/*******************************************************************************
  Supply Controller (SUPC) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SUPC_INSTANCE_NAME?lower_case}.c

  Summary:
    SUPC Source File

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_${SUPC_INSTANCE_NAME?lower_case}.h"
<#if CPU_CORE_ID?? && CPU_CORE_ID == 0>
#include "peripheral/clk/plib_clk.h"
#include "peripheral/sefc/plib_sefc0.h"
#include "peripheral/sefc/plib_sefc1.h"
#include "peripheral/rstc/plib_rstc.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#if SUPC_WUMR>
<#compress>
<#assign SUPC_WUIR = "">
<#assign WKUP_INPUTS = "SUPC_WKUP_INPUTS">
<#list 0.. (.vars[WKUP_INPUTS] - 1) as i>
<#assign SUPC_WUIR_WKUPEN = "SUPC_WUIR_WKUPEN" + i>
<#assign SUPC_WUIR_WKUPT = "SUPC_WUIR_WKUPT" + i>
<#if .vars[SUPC_WUIR_WKUPEN] == true>
    <#if SUPC_WUIR != "">
        <#assign SUPC_WUIR = SUPC_WUIR + " | \n\t\t" + "SUPC_WUIR_WKUPEN" + i +"_Msk | SUPC_WUIR_WKUPT" + i + "_${.vars[SUPC_WUIR_WKUPT]}">
    <#else>
        <#assign SUPC_WUIR = "SUPC_WUIR_WKUPEN" + i +"_Msk | SUPC_WUIR_WKUPT" + i + "_${.vars[SUPC_WUIR_WKUPT]}">
    </#if>
</#if>
</#list>
</#compress>
</#if>
<#compress>
<#assign SUPC_IER = "">
<#list 0..4 as i>
<#assign SUPC_IER_LPDBC = "SUPC_IER_LPDBC" + i>
<#if .vars[SUPC_IER_LPDBC] == true>
    <#if SUPC_IER != "">
        <#assign SUPC_IER = SUPC_IER + " | SUPC_IER_LPDBC" + i + "_Msk">
    <#else>
        <#assign SUPC_IER = "SUPC_IER_LPDBC" + i + "_Msk">
    </#if>
</#if>
</#list>
<#if SUPC_IER_VDD3V3SMEV == true>
    <#if SUPC_IER != "">
        <#assign SUPC_IER = SUPC_IER + " | SUPC_IER_VDD3V3SMEV_Msk">
    <#else>
        <#assign SUPC_IER = "SUPC_IER_VDD3V3SMEV_Msk">
    </#if>
</#if>
<#if SUPC_IER_VBATSMEV == true>
    <#if SUPC_IER != "">
        <#assign SUPC_IER = SUPC_IER + " | SUPC_IER_VBATSMEV_Msk">
    <#else>
        <#assign SUPC_IER = "SUPC_IER_VBATSMEV_Msk">
    </#if>
</#if>
</#compress>


static void WaitEntryClockSetup(bool xtal_disable)
{
    uint8_t count = 0U;
    uint32_t reg = 0U;

    /* Enable the RC Oscillator */
    PMC_REGS->CKGR_MOR |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCEN_Msk;

    /* Wait until the RC oscillator clock is ready. */
    while((PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk) != PMC_SR_MOSCRCS_Msk)
    {
        /* Nothing to do */
    }

    /* Switch Main Clock (MAINCK) to the RC Oscillator clock */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCSEL_Msk) | CKGR_MOR_KEY_PASSWD;

    /* Wait for Main Clock Selection Status */
    while((PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk)
    {
        /* Nothing to do */
    }

    /* Program PMC_CPU_CKR.CSS and MCK dividers and Wait for PMC_SR.MCKRDY to be set    */
    reg = (PMC_REGS->PMC_CPU_CKR & ~(PMC_CPU_CKR_CSS_Msk |
                                     PMC_CPU_CKR_RATIO_MCK0DIV_Msk |
                                     PMC_CPU_CKR_RATIO_MCK0DIV2_Msk));

    <@compress single_line=true>reg |= (PMC_CPU_CKR_CSS_MAINCK
        ${CLK_CPU_CKR_RATIO_MCK0DIV?string(" | PMC_CPU_CKR_RATIO_MCK0DIV_Msk","")}
        ${CLK_CPU_CKR_RATIO_MCK0DIV2?string(" | PMC_CPU_CKR_RATIO_MCK0DIV2_Msk", "")});</@compress>
    PMC_REGS->PMC_CPU_CKR = reg;
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Wait for status MCKRDY */
    }

    /* Disable PLL Clock */
    for (count = 0U; count < 3U; count++)
    {
        PMC_REGS->PMC_PLL_UPDT = (PMC_REGS->PMC_PLL_UPDT & ~PMC_PLL_UPDT_Msk) | PMC_PLL_UPDT_ID(count);
        PMC_REGS->PMC_PLL_UPDT |= PMC_PLL_UPDT_UPDATE_Msk;
        PMC_REGS->PMC_PLL_CTRL0 &= ~PMC_PLL_CTRL0_ENPLL_Msk;
    }

    /* Disable Crystal  */
    if(xtal_disable)
    {
        PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTEN_Msk) | CKGR_MOR_KEY_PASSWD;
    }
}

// *****************************************************************************
// *****************************************************************************
// Section: ${SUPC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************


void ${SUPC_INSTANCE_NAME}_Initialize(void)
{
    if(RSTC_PMCResetStatusGet())
    {
<#if SUPC_SMMR_VDD3V3SMSMPL != "0x0">
        <@compress single_line=true>${SUPC_INSTANCE_NAME}_REGS->SUPC_SMMR = SUPC_SMMR_VDD3V3SMSMPL(${SUPC_SMMR_VDD3V3SMSMPL}) | SUPC_SMMR_VDD3V3SMTH(${SUPC_SMMR_VDD3V3SMTH}) | SUPC_SMMR_VDD3V3SMPWRM(${SUPC_SMMR_VDD3V3SMPWRM})
                                                                        ${SUPC_SMMR_VDD3V3SMRSTEN?then('| SUPC_SMMR_VDD3V3SMRSTEN_Msk', '')};</@compress>
<#else>
        ${SUPC_INSTANCE_NAME}_REGS->SUPC_SMMR = SUPC_SMMR_VDD3V3SMSMPL_DISABLED;
</#if>

        <@compress single_line=true>${SUPC_INSTANCE_NAME}_REGS->SUPC_MR = (${SUPC_INSTANCE_NAME}_REGS->SUPC_MR & ~SUPC_MR_Msk) | (${SUPC_INSTANCE_NAME}_REGS->SUPC_MR & SUPC_MR_OSCBYPASS_Msk) | SUPC_MR_KEY_PASSWD
                                                                      ${SUPC_MR_IO_BACKUP_ISO?then('| SUPC_MR_IO_BACKUP_ISO_Msk', '')}
                                                                      ${SUPC_MR_CORSMDIS?then('| SUPC_MR_CORSMDIS_Msk', '')}
                                                                      ${SUPC_MR_CORSMRSTEN?then('| SUPC_MR_CORSMRSTEN_Msk', '')}
                                                                      ${SUPC_MR_VREGDIS?then('', '| SUPC_MR_VREGDIS_Msk')}
                                                                      ${SUPC_MR_CORSMM?then('', '| SUPC_MR_CORSMM_Msk')};</@compress>

<#if SUPC_EMR_COREBGEN || SUPC_EMR_FULLGPBRC || SUPC_EMR_FLRSGPBR>
        <@compress single_line=true>${SUPC_INSTANCE_NAME}_REGS->SUPC_EMR = (${SUPC_INSTANCE_NAME}_REGS->SUPC_EMR & ~SUPC_EMR_Msk)
                                                                      ${SUPC_EMR_COREBGEN?then('| SUPC_EMR_COREBGEN_Msk', '')}
                                                                      ${SUPC_EMR_FULLGPBRC?then('| SUPC_EMR_FULLGPBRC_Msk', '')}
                                                                      ${SUPC_EMR_FLRSGPBR?then('| SUPC_EMR_FLRSGPBR_Msk', '')};</@compress>

</#if>
<#if SUPC_BMR_RTTWKEN || SUPC_BMR_RTCWKEN || SUPC_BMR_VBATWKEN || SUPC_BMR_FWUPEN || SUPC_BMR_CORPORWKEN || SUPC_BMR_VDD3V3SMWKEN || SUPC_BMR_VBATREN || SUPC_BMR_MRTCOUT || SUPC_BMR_BADXTWKEN>
        <@compress single_line=true>${SUPC_INSTANCE_NAME}_REGS->SUPC_BMR = (${SUPC_INSTANCE_NAME}_REGS->SUPC_BMR & ~SUPC_BMR_Msk) | SUPC_BMR_KEY_PASSWD
                                                                      ${SUPC_BMR_RTTWKEN?then('| SUPC_BMR_RTTWKEN_Msk', '')}
                                                                      ${SUPC_BMR_RTCWKEN?then('| SUPC_BMR_RTCWKEN_Msk', '')}
                                                                      ${SUPC_BMR_VBATWKEN?then('| SUPC_BMR_VBATWKEN_Msk', '')}
                                                                      ${SUPC_BMR_FWUPEN?then('| SUPC_BMR_FWUPEN_Msk', '')}
                                                                      ${SUPC_BMR_CORPORWKEN?then('| SUPC_BMR_CORPORWKEN_Msk', '')}
                                                                      ${SUPC_BMR_VDD3V3SMWKEN?then('| SUPC_BMR_VDD3V3SMWKEN_Msk', '')}
                                                                      ${SUPC_BMR_VBATREN?then('| SUPC_BMR_VBATREN_Msk', '')}
                                                                      ${SUPC_BMR_MRTCOUT?then('| SUPC_BMR_MRTCOUT_Msk', '')}
                                                                      ${SUPC_BMR_BADXTWKEN?then('| SUPC_BMR_BADXTWKEN_Msk', '')};</@compress>

</#if>
<#if SUPC_WUMR>
        <@compress single_line=true>${SUPC_INSTANCE_NAME}_REGS->SUPC_WUMR = SUPC_WUMR_LPDBC0(${SUPC_WUMR_LPDBC0}) | SUPC_WUMR_LPDBC1(${SUPC_WUMR_LPDBC1}) | SUPC_WUMR_LPDBC2(${SUPC_WUMR_LPDBC2}) | SUPC_WUMR_LPDBC3(${SUPC_WUMR_LPDBC3}) | SUPC_WUMR_LPDBC4(${SUPC_WUMR_LPDBC4})
                                                                        | SUPC_WUMR_WKUPDBC(${SUPC_WUMR_WKUPDBC})
                                                                        | SUPC_WUMR_FWUPDBC(${SUPC_WUMR_FWUPDBC})
                                                                        ${SUPC_WUMR_LPDBCEN0?then('| SUPC_WUMR_LPDBCEN0_Msk', '')}
                                                                        ${SUPC_WUMR_LPDBCEN1?then('| SUPC_WUMR_LPDBCEN1_Msk', '')}
                                                                        ${SUPC_WUMR_LPDBCEN2?then('| SUPC_WUMR_LPDBCEN2_Msk', '')}
                                                                        ${SUPC_WUMR_LPDBCEN3?then('| SUPC_WUMR_LPDBCEN3_Msk', '')}
                                                                        ${SUPC_WUMR_LPDBCEN4?then('| SUPC_WUMR_LPDBCEN4_Msk', '')};</@compress>

    <#if SUPC_WUIR != "">
        <#lt>       ${SUPC_INSTANCE_NAME}_REGS->SUPC_WUIR = ${SUPC_WUIR};

    </#if>
    <#if SUPC_IER != "">
        <#lt>       ${SUPC_INSTANCE_NAME}_REGS->SUPC_IER = ${SUPC_IER};

    </#if>
</#if>
    }
}

void ${SUPC_INSTANCE_NAME}_SleepModeEnter(void)
{
    SCB->SCR &= (uint32_t)~SCB_SCR_SLEEPDEEP_Msk;

    /* Enable Interrupt */
    __DMB();
    __enable_irq();

    /* Enter Sleep  */
    __DSB();
    __WFI();
}

void ${SUPC_INSTANCE_NAME}_WaitModeEnter(WAITMODE_FLASH_STATE flash_lpm, WAITMODE_WKUP_SOURCE source)
{
    uint32_t i;

    /* Disable CPU Interrupt */
    __disable_irq();
    __DMB();

    /* Setup Clock for wait mode entry */
    WaitEntryClockSetup((flash_lpm == WAITMODE_FLASH_DEEPSLEEP));

    /* Enable CPU Interrupt */
    __DMB();
    __enable_irq();

    /* FLASH  Low power mode and Wakeup source */
    PMC_REGS->PMC_FSMR = ((uint32_t) flash_lpm | (uint32_t) source);

    /* Set Flash Wait State at 0 */
    SEFC0_REGS->SEFC_EEFC_FMR = SEFC_EEFC_FMR_FWS(0) | SEFC_EEFC_FMR_CLOE_Msk;
    SEFC1_REGS->SEFC_EEFC_FMR = SEFC_EEFC_FMR_FWS(0) | SEFC_EEFC_FMR_CLOE_Msk;

    /* Set the WAITMODE bit */
    PMC_REGS->CKGR_MOR |= (CKGR_MOR_KEY_PASSWD | CKGR_MOR_WAITMODE_Msk);

    /* Waiting for Master Clock Ready MCKRDY = 1 */
    while((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk)
    {
        /* Nothing to do */
    }

    /* Waiting for MOSCRCEN bit is cleared is strongly recommended
     * to ensure that the core will not execute undesired instructions
     */
    for (i = 0; i < 500U; i++)
    {
       __NOP();
    }

    while((PMC_REGS->CKGR_MOR & CKGR_MOR_MOSCRCEN_Msk) != CKGR_MOR_MOSCRCEN_Msk)
    {
        /* Nothing to do */
    }

    /* Disable CPU Interrupt */
    __disable_irq();
    __DMB();

    /* Restore Clock Setting */
    SEFC0_Initialize();
    SEFC1_Initialize();
    CLK_Initialize();

    /* Enable CPU Interrupt */
    __DMB();
    __enable_irq();
}

void ${SUPC_INSTANCE_NAME}_BackupModeEnter(void)
{
    SCB->SCR |= SCB_SCR_SLEEPDEEP_Msk;

<#if SUPC_CR_VROFF>
    /* Switch off voltage regulator */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_CR |= SUPC_CR_KEY_PASSWD | SUPC_CR_VROFF_Msk;

</#if>
    /* Enable CPU Interrupt */
    __DMB();
    __enable_irq();

    /* Enter Backup */
    __DSB();
    __WFI();
}

<#if SUPC_IER_VDD3V3SMEV || SUPC_IER_VBATSMEV || SUPC_IER_LPDBC0 || SUPC_IER_LPDBC1 || SUPC_IER_LPDBC2 || SUPC_IER_LPDBC3 || SUPC_IER_LPDBC4>
static SUPC_OBJECT supcObj;

void ${SUPC_INSTANCE_NAME}_CallbackRegister(SUPC_CALLBACK callback, uintptr_t context)
{
    supcObj.callback = callback;
    supcObj.context = context;
}

void ${SUPC_INSTANCE_NAME}_InterruptHandler(void)
{
    uint32_t supc_status = ${SUPC_INSTANCE_NAME}_REGS->SUPC_ISR;

    /* Callback user function */
    if(supcObj.callback != NULL)
    {
        supcObj.callback(supc_status, supcObj.context);
    }
}
</#if>
</#if>
uint32_t ${SUPC_INSTANCE_NAME}_GPBRRead(GPBR_REGS_INDEX reg)
{
    return GPBR_REGS->SYS_GPBR[reg];
}

void ${SUPC_INSTANCE_NAME}_GPBRWrite(GPBR_REGS_INDEX reg, uint32_t data)
{
    GPBR_REGS->SYS_GPBR[reg] = data;
}
