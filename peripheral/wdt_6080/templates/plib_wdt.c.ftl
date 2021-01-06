/*******************************************************************************
  WDT Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_wdt.c

  Summary:
    WDT Source File

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

#include "device.h"
#include "plib_${WDT_INSTANCE_NAME?lower_case}.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>
<#if WDT_CR_LOCKMR??>

#define WDT_CLK_DELAY  ((3 * ${CPU_CLOCK_FREQUENCY}) / 32768)
</#if>
<#if wdtinterruptMode == true>

  <#lt>WDT_OBJECT wdt;
</#if>

void ${WDT_INSTANCE_NAME}_Initialize( void )
{
<#if WDT_CR_LOCKMR??>
    /* Until LOCK bit is set, watchdog can be disabled or enabled. If it is disabled (for eg, by bootloader),
     * WDD and WDV fields in MR cannot be modified, so enable it before proceeding.
     * NOTE: If lock bit is already set, these operations have no effect on WDT.
     */
    if (${WDT_INSTANCE_NAME}_REGS->WDT_MR & WDT_MR_WDDIS_Msk)
    {
        /* Enable Watchdog */
        ${WDT_INSTANCE_NAME}_REGS->WDT_MR &= ~(WDT_MR_WDDIS_Msk);

        /* Wait for 3 WDT clk cycles before any further update to MR */
        for(uint32_t count = 0; count < WDT_CLK_DELAY; count++);
    }
</#if>

    ${WDT_INSTANCE_NAME}_REGS->WDT_MR = WDT_MR_WDD (${wdtWDD}) | WDT_MR_WDV(${wdtWDV}) \
              ${wdtdebugHalt?then(' | WDT_MR_WDDBGHLT_Msk','')}${wdtidleHalt?then(' | WDT_MR_WDIDLEHLT_Msk','')}<#if WDT_MR_WDRPROC??>${(WDT_MR_WDRPROC != "0")?then(' | WDT_MR_WDRPROC_Msk','')}</#if>${wdtEnableReset?then(' | WDT_MR_WDRSTEN_Msk','')}${wdtinterruptMode?then(' | WDT_MR_WDFIEN_Msk','')};
<#if WDT_CR_LOCKMR??>
<#if WDT_CR_LOCKMR == true>

    /* Lock WDT MR register */
    ${WDT_INSTANCE_NAME}_REGS->WDT_CR = (WDT_CR_KEY_PASSWD | WDT_CR_LOCKMR_Msk);
</#if>
</#if>

}

void ${WDT_INSTANCE_NAME}_Clear(void)
{
   ${WDT_INSTANCE_NAME}_REGS->WDT_CR = (WDT_CR_KEY_PASSWD | WDT_CR_WDRSTT_Msk);
}

<#if wdtinterruptMode == true>
    <#lt>void ${WDT_INSTANCE_NAME}_CallbackRegister( WDT_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>   wdt.callback = callback;
    <#lt>   wdt.context = context;
    <#lt>}
</#if>

<#if wdtinterruptMode == true>
   <#lt>void ${WDT_INSTANCE_NAME}_InterruptHandler( void )
   <#lt>{
   <#lt>   ${WDT_INSTANCE_NAME}_REGS->WDT_SR;
   <#lt>    if(wdt.callback != NULL)
    <#lt>   {
    <#lt>       wdt.callback(wdt.context);
    <#lt>   }
  <#lt>}
</#if>
