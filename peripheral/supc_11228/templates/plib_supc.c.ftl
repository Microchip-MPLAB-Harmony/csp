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

#include "plib_${SUPC_INSTANCE_NAME?lower_case}.h"
#include "peripheral/clock/plib_clock.h"
#include "peripheral/efc/plib_efc.h"

static void WaitEntryClockSetup (bool xtal_disable);

<#compress>
<#assign SUPC_WUIR = "">
<#assign WKUP_INPUTS = "SUPC_WKUP_INPUTS">

<#list 0.. (.vars[WKUP_INPUTS] - 1) as i>
<#assign SUPC_WUIR_WKUPEN = "SUPC_WUIR_WKUPEN" + i>
<#assign SUPC_WUIR_WKUPT = "SUPC_WUIR_WKUPT" + i>

<#if .vars[SUPC_WUIR_WKUPEN] == true>

    <#if SUPC_WUIR != "">
        <#assign SUPC_WUIR = SUPC_WUIR + " | \n\t\t" + "SUPC_WUIR_WKUPEN" + i +"_ENABLE | SUPC_WUIR_WKUPT" + i + "_${.vars[SUPC_WUIR_WKUPT]}">
    <#else>
        <#assign SUPC_WUIR = "SUPC_WUIR_WKUPEN" + i +"_ENABLE | SUPC_WUIR_WKUPT" + i + "_${.vars[SUPC_WUIR_WKUPT]}">
    </#if>

</#if>

</#list>
</#compress>

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: SUPC Implementation
// *****************************************************************************
// *****************************************************************************

void ${SUPC_INSTANCE_NAME}_Initialize (void)
{
    <#if SM_ENABLE>
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_SMMR = (SUPC_SMMR_SMSMPL${SUPC_SMMR_SMSMPL} | SUPC_SMMR_SMTH(${SUPC_SMMR_SMTH}) ${SUPC_SMMR_SMIEN?then('| SUPC_SMMR_SMIEN_Msk', '')} ${SUPC_SMMR_SMRSTEN?then('| SUPC_SMMR_SMRSTEN_ENABLE', '')}); 
    <#else>
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_SMMR = SUPC_SMMR_SMSMPL_SMD;
    </#if>
    
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_MR = (SUPC_MR_KEY_PASSWD | SUPC_MR_ONE_Msk | SUPC_MR_ONEA_Msk ${SUPC_MR_BODRSTEN?then('| SUPC_MR_BODRSTEN_ENABLE', '')} ${SUPC_MR_BODDIS?then('', '| SUPC_MR_BODDIS_DISABLE')} ${SUPC_CTPSWITCH?then('| SUPC_MR_CTPSWITCH_Msk', '')} ${SUPC_CDPSWITCH?then('| SUPC_MR_CDPSWITCH_Msk', '')});  
    
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_WUMR = (SUPC_WUMR_LPDBC(${SUPC_WUMR_LPDBC}) ${SUPC_WUMR_LPDBCEN0?then('| SUPC_WUMR_LPDBCEN0_ENABLE', '')} ${SUPC_WUMR_LPDBCEN1?then('| SUPC_WUMR_LPDBCEN1_ENABLE', '')} ${SUPC_WUMR_LPDBCCLR?then('| SUPC_WUMR_LPDBCCLR_ENABLE', '')} \
                            | SUPC_WUMR_WKUPDBC(${SUPC_WUMR_WKUPDBC}) ${SUPC_WUMR_RTCEN?then('| SUPC_WUMR_RTCEN_ENABLE ', '')} ${SUPC_WUMR_RTTEN?then('| SUPC_WUMR_RTTEN_ENABLE', '')} ${SUPC_WUMR_SMEN?then('| SUPC_WUMR_SMEN_ENABLE', '')});	
    
    <#if SUPC_WUIR != "">	
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_WUIR = ${SUPC_WUIR};
    </#if>
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_PWMR = SUPC_PWMR_KEY_PASSWD ${SUPC_SRAM0?then('| SUPC_PWMR_SRAM0ON_Msk', '')} ${SUPC_SRAM1?then('| SUPC_PWMR_SRAM1ON_Msk', '')} ${SUPC_SRAM2?then('| SUPC_PWMR_SRAM2ON_Msk', '')} ${SUPC_SRAM3?then('| SUPC_PWMR_SRAM3ON_Msk', '')} ${SUPC_SRAM4?then('| SUPC_PWMR_SRAM4ON_Msk', '')} ${SUPC_SRAM5?then('| SUPC_PWMR_SRAM5ON_Msk', '')} ${SUPC_SRAM6?then('| SUPC_PWMR_SRAM6ON_Msk', '')} ${SUPC_STUPTIME?then('| SUPC_PWMR_STUPTIME_Msk', '')} ${SUPC_DPRAMON?then('| SUPC_PWMR_DPRAMON_Msk', '')};
}

void ${SUPC_INSTANCE_NAME}_SleepModeEnter (void)
{
    SCB->SCR &= (uint32_t)~SCB_SCR_SLEEPDEEP_Msk;

    /* Enable Interrupt */
    __DMB();
    __enable_irq();
    
    /* Enter Sleep 	*/
    __DSB();
    __WFI();
}

void ${SUPC_INSTANCE_NAME}_WaitModeEnter (WAITMODE_FLASH_STATE flash_lpm, WAITMODE_WKUP_SOURCE source)
{
    uint32_t i;
 
    /* Disable CPU Interrupt	*/
    __disable_irq();
    __DMB();

    /* Setup Clock for wait mode entry	*/	
    WaitEntryClockSetup((flash_lpm == PMC_FSMR_FLPM_FLASH_DEEP_POWERDOWN));
    
    /* Enable CPU Interrupt	*/
    __DMB();
    __enable_irq();
    
    /* FLASH  Low power mode and Wakeup source	*/
    PMC_REGS->PMC_FSMR = ((uint32_t) flash_lpm | (uint32_t) source);
    
    /* Set Flash Wait State at 0	*/
    EFC_REGS->EEFC_FMR = EEFC_FMR_FWS(0) | EEFC_FMR_CLOE_Msk;
    
    /* Set the WAITMODE bit	*/
    PMC_REGS->CKGR_MOR |= (CKGR_MOR_KEY_PASSWD | CKGR_MOR_WAITMODE_Msk);
    
    /* Waiting for Master Clock Ready MCKRDY = 1 */
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);
            
    /* Waiting for MOSCRCEN bit is cleared is strongly recommended
    * to ensure that the core will not execute undesired instructions
    */
    for (i = 0; i < 500; i++) 
    {
       __NOP();
    }
    
    while ((PMC_REGS->CKGR_MOR & CKGR_MOR_MOSCRCEN_Msk) != CKGR_MOR_MOSCRCEN_Msk);
    
    /* Disable CPU Interrupt	*/
    __disable_irq();
    __DMB();

    /* Restore Clock Setting	*/
    EFC_Initialize();
    CLOCK_Initialize();
    
    
    /* Enable CPU Interrupt	*/
    __DMB();
    __enable_irq();	
}

void ${SUPC_INSTANCE_NAME}_BackupModeEnter (void)
{
    SCB->SCR |= SCB_SCR_SLEEPDEEP_Msk;

    /* Switch off voltage regulator	*/
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_CR |= (SUPC_CR_KEY_PASSWD | SUPC_CR_VROFF_Msk); 

    /* Enable CPU Interrupt	*/
    __DMB();
    __enable_irq();

    /* Enter Backup	*/
    __DSB();	
    __WFI();	
}

<#if SUPC_SMMR_SMIEN>
SUPC_OBJECT supcObj;

void ${SUPC_INSTANCE_NAME}_CallbackRegister (SUPC_CALLBACK callback, uintptr_t context)
{
    supcObj.callback = callback;
    supcObj.context = context;
}

void ${SUPC_INSTANCE_NAME}_InterruptHandler (void)
{
       // Callback user function
    if(supcObj.callback != NULL)
    {
        supcObj.callback (supcObj.context);		
    }
}
</#if>

uint32_t ${SUPC_INSTANCE_NAME}_GPBRRead (GPBR_REGS_INDEX reg)
{
    return GPBR_REGS->SYS_GPBR[reg];
}

void ${SUPC_INSTANCE_NAME}_GPBRWrite (GPBR_REGS_INDEX reg, uint32_t data)
{
    GPBR_REGS->SYS_GPBR[reg] = data;
}

void WaitEntryClockSetup(bool xtal_disable)
{
    /* Enable the RC Oscillator */
    PMC_REGS->CKGR_MOR |= CKGR_MOR_KEY_PASSWD | CKGR_MOR_MOSCRCEN_Msk;

    /* Wait until the RC oscillator clock is ready. */
    while( (PMC_REGS->PMC_SR & PMC_SR_MOSCRCS_Msk) != PMC_SR_MOSCRCS_Msk )
    {
    }
    
    /* Switch Main Clock (MAINCK) to the RC Oscillator clock */
    PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCSEL_Msk) | CKGR_MOR_KEY_PASSWD;

    /* Wait for Main Clock Selection Status */
    while ((PMC_REGS->PMC_SR & PMC_SR_MOSCSELS_Msk) != PMC_SR_MOSCSELS_Msk);
    
    /* If Master clock source is PLL, switch to MAIN clock	*/
    if ( (PMC_REGS->PMC_MCKR & PMC_MCKR_CSS_Msk) > PMC_MCKR_CSS_MAIN_CLK) 
    {
        PMC_REGS->PMC_MCKR = (PMC_REGS->PMC_MCKR & ~PMC_MCKR_CSS_Msk) | PMC_MCKR_CSS_MAIN_CLK;
    
        while ( (PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk )
        {
        }	
    }
    
    /* Disable PLLA Clock */
    PMC_REGS->CKGR_PLLAR = CKGR_PLLAR_ZERO_Msk | CKGR_PLLAR_MULA(0);

    /* Disable PLLB Clock */
    PMC_REGS->CKGR_PLLBR = CKGR_PLLBR_ZERO_Msk | CKGR_PLLBR_MULB(0);	
    
    /* Disable Crystal	*/
    if(xtal_disable)
    {
        PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTEN_Msk) | CKGR_MOR_KEY_PASSWD;
    }
}
