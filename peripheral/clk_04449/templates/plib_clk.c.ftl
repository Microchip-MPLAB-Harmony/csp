<#assign monIntTypes = ["rdy", "mon", "fail", "warn"]>
<#assign pllClockSources = ["PGC","FRC","BFRC","POSC","","","","","","REFI1","REFI2"]>
<#assign clkgenClockSources = ["PGC","FRC","BFRC","POSC","LPRC","PLL1_FOUT","PLL2_FOUT","PLL1_VCO","PLL2_VCO","REFI1","REFI2"]>
<#assign clkmonClockSources = []>
<#assign maxClockGenWoRefClk = maxClockGen-2>
<#list 1..maxClockGenWoRefClk as i>
    <#assign clkmonClockSources = clkmonClockSources + ["CLOCK_GEN${i}"]>
</#list>
<#assign clkmonClockSources = clkmonClockSources+["PLL1_FOUT","PLL1_VCO","PLL2_FOUT","PLL2_VCO","","PGC","FRC","BFRC","POSC","LPRC","","","","","REFI1","REFI2"]>
<#assign clkmonCntDivOptions = ["DIV_BY_1","DIV_BY_2","DIV_BY_4",""]>
/*******************************************************************************
  Clock PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_clk.c
 
  Summary:
    Clock PLIB Source File
 
  Description:
    None
 
*******************************************************************************/
 
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

// Section: Includes
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include "device.h"
#include "interrupts.h"
#include "plib_clk.h"
#include "plib_clk_common.h"

// Section: Macro Definitions

<#list 1..maxPllGen as i>
<#if (.vars["pll"+i+"Enable"]??) && (.vars["pll"+i+"Enable"])>
//CLOCK PLLxCON NOSC options
<#list pllClockSources as options>
<#if options != "">
#define PLL${i}CON_NOSC_${options}          ((uint32_t)(_PLL${i}CON_NOSC_MASK & ((uint32_t)(${options_index}) << _PLL${i}CON_NOSC_POSITION))) 
</#if>
</#list>
<#list pllClockSources as options>
<#if options != "">
<#if .vars["pll"+i+"CON__FSCMEN"]?number == 1>

//CLOCK PLLxCON BOSC options
<#break>
</#if>
</#if>
</#list>
<#list pllClockSources as options>
<#if options != "">
#define PLL${i}CON_BOSC_${options}          ((uint32_t)(_PLL${i}CON_BOSC_MASK & ((uint32_t)(${options_index}) << _PLL${i}CON_BOSC_POSITION))) 
</#if>
</#list>

//CLOCK PLLxCON PLLPRE set
#define PLL${i}DIV_PLLPRE_SET(value)          ((uint32_t)(_PLL${i}DIV_PLLPRE_MASK & ((uint32_t)(value) << _PLL${i}DIV_PLLPRE_POSITION))) 
//CLOCK PLLxCON PLLFBDIV set
#define PLL${i}DIV_PLLFBDIV_SET(value)          ((uint32_t)(_PLL${i}DIV_PLLFBDIV_MASK & ((uint32_t)(value) << _PLL${i}DIV_PLLFBDIV_POSITION))) 
//CLOCK PLLxCON POSTDIV1 set
#define PLL${i}DIV_POSTDIV1_SET(value)          ((uint32_t)(_PLL${i}DIV_POSTDIV1_MASK & ((uint32_t)(value) << _PLL${i}DIV_POSTDIV1_POSITION))) 
//CLOCK PLLxCON POSTDIV2 set
#define PLL${i}DIV_POSTDIV2_SET(value)          ((uint32_t)(_PLL${i}DIV_POSTDIV2_MASK & ((uint32_t)(value) << _PLL${i}DIV_POSTDIV2_POSITION))) 

//CLOCK VCOxDIV INTDIV set
#define VCO${i}DIV_INTDIV_SET(value)          ((uint32_t)(_VCO${i}DIV_INTDIV_MASK & ((uint32_t)(value) << _VCO${i}DIV_INTDIV_POSITION))) 

</#if>
</#list>
<#list 1..maxClockGen as i>
<#if (.vars["clkGen"+i+"Enable"]??) && (.vars["clkGen"+i+"Enable"])>
//CLOCK CLKxCON NOSC options
<#list clkgenClockSources as options>
<#if options != "">
#define CLK${i}CON_NOSC_${options}          ((uint32_t)(_CLK${i}CON_NOSC_MASK & ((uint32_t)(${options_index}) << _CLK${i}CON_NOSC_POSITION))) 
</#if>
</#list>
<#list clkgenClockSources as options>
<#if options != "">
<#if .vars["clkGen"+i+"CON__FSCMEN"]?number == 1>

//CLOCK CLKxCON BOSC options
<#break>
</#if>
</#if>
</#list>
<#list clkgenClockSources as options>
<#if options != "">
#define CLK${i}CON_BOSC_${options}          ((uint32_t)(_CLK${i}CON_BOSC_MASK & ((uint32_t)(${options_index}) << _CLK${i}CON_BOSC_POSITION))) 
</#if>
</#list>

//CLOCK CLKxCON INTDIV set
#define CLK${i}DIV_INTDIV_SET(value)          ((uint32_t)(_CLK${i}DIV_INTDIV_MASK & ((uint32_t)(value) << _CLK${i}DIV_INTDIV_POSITION))) 
//CLOCK CLKONxCON FRACDIV set
#define CLK${i}DIV_FRACDIV_SET(value)          ((uint32_t)(_CLK${i}DIV_FRACDIV_MASK & ((uint32_t)(value) << _CLK${i}DIV_FRACDIV_POSITION))) 

</#if>
</#list>
<#if useClockMonitor>
<#list 1..maxClockMon as i>
//CLOCK CMxCON CNTDIV options
<#list clkmonCntDivOptions as options>
<#if options != "">
#define CM${i}CON_CNTDIV_${options}          ((uint32_t)(_CM${i}CON_CNTDIV_MASK & ((uint32_t)(${options_index}) << _CM${i}CON_CNTDIV_POSITION))) 
</#if>
</#list>
<#list clkmonClockSources as options>
<#if options != "">

//CLOCK CMxSEL CNTSEL options
<#break>
</#if>
</#list>
<#list clkmonClockSources as options>
<#if options != "">
#define CM${i}SEL_CNTSEL_${options}          ((uint32_t)(_CM${i}SEL_CNTSEL_MASK & ((uint32_t)(${options_index}) << _CM${i}SEL_CNTSEL_POSITION))) 
</#if>
</#list>
<#list clkmonClockSources as options>
<#if options != "">

//CLOCK CMxSEL WINSEL options
<#break>
</#if>
</#list>
<#list clkmonClockSources as options>
<#if options != "">
#define CM${i}SEL_WINSEL_${options}          ((uint32_t)(_CM${i}SEL_WINSEL_MASK & ((uint32_t)(${options_index}) << _CM${i}SEL_WINSEL_POSITION))) 
</#if>
</#list>

</#list>
</#if>

// Section: ISR declaration
<#if clockFailIntEnable == true>
void ${clkfailIsrHandlerName}(void);
</#if>
<#if useClockMonitor>
<#list monIntTypes as type>
<#list 1..maxClockMon as i>
<#if (.vars["cm"+i+"Enable"]??) && (.vars["cm"+i+"Enable"] == true)>
<#if (.vars["cm"+i+type+"IntEnable"]??) && (.vars["cm"+i+type+"IntEnable"] == true)>
<#if (.vars["c"+i+type+"IsrHandlerName"]??) && (.vars["c"+i+type+"InterruptFlagBit"]??)>
void ${.vars["c"+i+type+"IsrHandlerName"]}(void);
</#if>
</#if>
</#if>
</#list>
</#list>
</#if>

// Section: Static Variables

<#if useClockMonitor>
<#list monIntTypes as type>
<#list 1..maxClockMon as i>
<#if (.vars["cm"+i+type+"IntEnable"]??) &&  (.vars["cm"+i+type+"IntEnable"]== true)>
volatile static CLOCK_Monitor${type?capitalize}Object cm${type}Obj[${maxClockMon}];
<#break>
</#if>
</#list>
</#list>
</#if>

<#if clockFailIntEnable == true>
volatile static CLOCK_CombinedFailObject clkGenObj;
</#if>

void CLOCK_Initialize(void)
{
    /*  
        System Clock Source                             :  ${sysClockSourceComment}
        System/Generator 1 frequency (Fosc)             :  ${sysClockFrequencyComment} MHz
        
        <#list 1..maxClockGen as i>
        <#if (i > 1) && (.vars["clkGen"+i+"Enable"]??) && (.vars["clkGen"+i+"Enable"])>
        Clock Generator ${i} frequency                     : ${.vars["clkGen"+i+"OutFrequencyInMHz"]} MHz
        </#if>
        </#list>
        
        <#list 1..maxPllGen as i>
		<#if (.vars["pll"+i+"Enable"]??) && (.vars["pll"+i+"Enable"])>
        PLL ${i} frequency                                 : ${.vars["pll"+i+"OutFrequencyInMHz"]} MHz
        PLL ${i} VCO Out frequency                         : ${.vars["pll"+i+"VcoFrequencyInMHz"]} MHz
		</#if>
        </#list>

    */
    <#if primaryClockUsed>
    //Primary oscillator settings 
    OSCCFGbits.POSCMD = ${poscmdValue}U;
    </#if>
    <#if clkoUsed>
    OSCCFGbits.POSCIOFNC = 1U;
    </#if>
    <#if primaryClockUsed>
    OSCCTRLbits.POSCEN = 1U;
    while(OSCCTRLbits.POSCRDY == 0U){};
    </#if>
    
    <#list 1..maxPllGen as i>
	<#if (.vars["pll"+i+"Enable"]??) && (.vars["pll"+i+"Enable"])>
    //PLL ${i} settings
    PLL${i}CON = (_PLL${i}CON_ON_MASK
                |PLL${i}CON_NOSC_${pllClockSources[.vars["pll"+i+"CON__NOSC"]?number]}
                |PLL${i}CON_BOSC_${pllClockSources[.vars["pll"+i+"CON__BOSC"]?number]}<#if .vars["pll"+i+"CON__FSCMEN"]?number == 1>
                |_PLL${i}CON_FSCMEN_MASK</#if>);
    PLL${i}DIV = (PLL${i}DIV_PLLPRE_SET(${.vars["pll"+i+"DIV__PLLPRE"]?number})
                 |PLL${i}DIV_PLLFBDIV_SET(${.vars["pll"+i+"DIV__PLLFBDIV"]?number})
                 |PLL${i}DIV_POSTDIV1_SET(${.vars["pll"+i+"DIV__POSTDIV1"]?number})
                 |PLL${i}DIV_POSTDIV2_SET(${.vars["pll"+i+"DIV__POSTDIV2"]?number}));
    //Enable PLL Input and Feedback Divider update
    PLL${i}CONbits.PLLSWEN = 1U;
#ifndef __MPLAB_DEBUGGER_SIMULATOR 
    while (PLL${i}CONbits.PLLSWEN == 1){};
#endif
    PLL${i}CONbits.FOUTSWEN = 1U;
#ifndef __MPLAB_DEBUGGER_SIMULATOR 
    while (PLL${i}CONbits.FOUTSWEN == 1U){};
#endif
    //Enable clock switching
    PLL${i}CONbits.OSWEN = 1U;
#ifndef __MPLAB_DEBUGGER_SIMULATOR    
    //Wait for switching
    while(PLL${i}CONbits.OSWEN == 1U){}; 
    //Wait for clock to be ready
    while(OSCCTRLbits.PLL${i}RDY == 0U){}; 
#endif  
	</#if>
    <#if (.vars["pll"+i+"Enable"]??) && (.vars["pll"+i+"Enable"])>
    //Configure VCO Divider 
    VCO${i}DIV = VCO${i}DIV_INTDIV_SET(${.vars["vco"+i+"DIV__INTDIV"]?number});
    //Enable PLL VCO divider
    PLL${i}CONbits.DIVSWEN = 1U;
#ifndef __MPLAB_DEBUGGER_SIMULATOR    
    //Wait for setup complete
    while(PLL${i}CONbits.DIVSWEN == 1U){}; 
#endif
    
	</#if>
    </#list>
    <#list 1..maxClockGen as i>
    <#if (.vars["clkGen"+i+"Enable"]??) && (.vars["clkGen"+i+"Enable"] == true)>
    //Clock Generator ${i} settings
    CLK${i}CON = (_CLK${i}CON_ON_MASK
                |_CLK${i}CON_OE_MASK
                |CLK${i}CON_NOSC_${clkgenClockSources[.vars["clkGen"+i+"CON__NOSC"]?number]}
                |CLK${i}CON_BOSC_${clkgenClockSources[.vars["clkGen"+i+"CON__BOSC"]?number]}<#if .vars["clkGen"+i+"CON__FSCMEN"]?number == 1>
                |_CLK${i}CON_FSCMEN_MASK</#if>);
    <#if (.vars["clkGen"+i+"IsDividerEnabled"]??) && (.vars["clkGen"+i+"IsDividerEnabled"] == true)>
    CLK${i}DIV = (CLK${i}DIV_INTDIV_SET(${.vars["clkGen"+i+"DIV__INTDIV"]?number})
                 |CLK${i}DIV_FRACDIV_SET(${.vars["clkGen"+i+"DIV__FRACDIV"]?number}));
    //Enable divide factors
    CLK${i}CONbits.DIVSWEN = 1U; 
#ifndef __MPLAB_DEBUGGER_SIMULATOR
    //Wait for divide factors to get updated
    while(CLK${i}CONbits.DIVSWEN == 1U){};
#endif
    </#if>
    //Enable clock switching
    CLK${i}CONbits.OSWEN = 1U;
#ifndef __MPLAB_DEBUGGER_SIMULATOR    
    //Wait for clock switching complete
    while(CLK${i}CONbits.OSWEN == 1U){};
#endif

    </#if>
    </#list>   
    <#if clockFailIntEnable == true> 
    //Enable clock failure interrupt
    ${clkfailInterruptFlagBit} = 0U; 
    ${clkfailInterruptEnableBit} = 1U;
    
    </#if>
    <#if useClockMonitor>
    <#list 1..maxClockMon as i>
    <#if (.vars["cm"+i+"Enable"]??) && (.vars["cm"+i+"Enable"] == true)>
    //Clock Monitor ${i} settings
    CM${i}CONbits.ON = 0U;
    CM${i}WINPR = 0x${.vars["cm"+i+"WINPRValue"]}UL;
    CM${i}HFAIL = 0x${.vars["cm"+i+"HFAILValue"]}UL;
    CM${i}LFAIL = 0x${.vars["cm"+i+"LFAILValue"]}UL;
    CM${i}HWARN = 0x${.vars["cm"+i+"HWARNValue"]}UL;
    CM${i}LWARN = 0x${.vars["cm"+i+"LWARNValue"]}UL;
    CM${i}SAT = 0x${.vars["cm"+i+"SATValue"]}UL;
    CM${i}BUF = ${.vars["cm"+i+"BUFValue"]}UL;
    CM${i}SEL = (CM${i}SEL_CNTSEL_${clkmonClockSources[.vars["CM"+i+"SEL__CNTSEL"]?number]}
                |CM${i}SEL_WINSEL_${clkmonClockSources[.vars["CM"+i+"SEL__WINSEL"]?number]});
    CM${i}CON = CM${i}CON_CNTDIV_${clkmonCntDivOptions[.vars["CM"+i+"CON__CNTDIV"]?number]};
    
    </#if>
    </#list>
    <#list monIntTypes as type>
    <#list 1..maxClockMon as i>
    <#if (.vars["cm"+i+"Enable"]??) && (.vars["cm"+i+"Enable"] == true)>
    <#if (.vars["cm"+i+type+"IntEnable"]??) &&  (.vars["cm"+i+type+"IntEnable"] == true)>
    <#if (.vars["c"+i+type+"InterruptFlagBit"]??)>
	${.vars["c"+i+type+"InterruptFlagBit"]} = 0U;
	</#if>
	<#if (.vars["c"+i+type+"InterruptEnableBit"]??)>
    ${.vars["c"+i+type+"InterruptEnableBit"]} = 1U;
    </#if>
	</#if>
	</#if>
    </#list>
    </#list>

    <#list 1..maxClockMon as i>
    <#if (.vars["cm"+i+"Enable"]??) && (.vars["cm"+i+"Enable"] == true)>
    <#if (.vars["cm"+i+"EnableInitStage"] == true)>
    CM${i}CONbits.ON = 1U;
    </#if>
    </#if>
    </#list>
    </#if>
}

<#if clockFailIntEnable == true>
void CLOCK_CombinedClockFailCallbackRegister(CLOCK_CombinedFailCallback callback, uintptr_t context)
{
    if(NULL != callback)
    {
        clkGenObj.callback = callback;
        clkGenObj.context = context;
    }
}
</#if>
<#if useClockMonitor>
<#list monIntTypes as type>
<#list 1..maxClockMon as i>
<#if (.vars["cm"+i+"Enable"]??) && (.vars["cm"+i+"Enable"] == true)>
<#if (.vars["cm"+i+type+"IntEnable"]??) &&  (.vars["cm"+i+type+"IntEnable"]== true)>

void CLOCK_Monitor${type?capitalize}CallbackRegister(CLOCK_MONITOR monitor, CLOCK_Monitor${type?capitalize}Callback callback, uintptr_t context)
{
    switch(monitor)
    {
        <#list 1..maxClockMon as i>
        <#if (.vars["cm"+i+"Enable"]??) && (.vars["cm"+i+"Enable"] == true)>
        <#if (.vars["cm"+i+type+"IntEnable"]??) &&  (.vars["cm"+i+type+"IntEnable"]== true)>
        case CLOCK_MONITOR_${i}:
            if(NULL != callback)
            {
                cm${type}Obj[${i-1}].callback = callback;
                cm${type}Obj[${i-1}].context = context;
            }
            break;
        </#if>
        </#if>
        </#list>
        default:
            break;
    }
}  
<#break>
</#if>
</#if>
</#list>
</#list>
</#if>
 
<#if clockFailIntEnable == true>
void ${clkfailIsrHandlerName}(void)
{
    if(NULL != clkGenObj.callback)
    {
        (*clkGenObj.callback)(clkGenObj.context);
    } 
    // clear clock fail status  
    CLKFAIL =  0x0U;
    // clear the CLOCK interrupt flag
    ${clkfailInterruptFlagBit} = 0U;
}

</#if>
<#if useClockMonitor>
<#list monIntTypes as type>
<#list 1..maxClockMon as i>
<#if (.vars["cm"+i+"Enable"]??) && (.vars["cm"+i+"Enable"] == true)>
<#if (.vars["cm"+i+type+"IntEnable"]??) && (.vars["cm"+i+type+"IntEnable"] == true)>
<#if (.vars["c"+i+type+"IsrHandlerName"]??) && (.vars["c"+i+type+"InterruptFlagBit"]??)>
void ${.vars["c"+i+type+"IsrHandlerName"]}(void)
{
    if(NULL != cm${type}Obj[${i-1}].callback)
    {
        (*cm${type}Obj[${i-1}].callback)(cm${type}Obj[${i-1}].context);
    }
    ${.vars["c"+i+type+"InterruptFlagBit"]} = 0U;
}

</#if>
</#if>
</#if>
</#list>
</#list>
</#if>
