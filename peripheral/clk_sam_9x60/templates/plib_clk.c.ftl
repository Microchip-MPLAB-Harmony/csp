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

#include "device.h"
#include "plib_clk.h"

#define PLL_ID_PLLA     0U
#define PLL_ID_UPLL     1U

<#if CLK_GENERATOR_CODE>
/*********************************************************************************
Initialize Slow clock
*********************************************************************************/
static void initSlowClk(void)
{
<#if CLK_OSC32BYP>
    SCKC_REGS->SCKC_CR |= SCKC_CR_OSC32BYP_Msk;
    SCKC_REGS->SCKC_CR &= ~SCKC_CR_OSC32EN_Msk;
<#elseif CLK_OSC32EN>
    SCKC_REGS->SCKC_CR |= SCKC_CR_OSC32EN_Msk;
</#if>
    SCKC_REGS->SCKC_CR = (SCKC_REGS->SCKC_CR & ~SCKC_CR_TD_OSCSEL_Msk) |\
                         SCKC_CR_TD_OSCSEL_${CLK_TD_OSCSEL};
}

/*********************************************************************************
Initialize Main clock
*********************************************************************************/
static void initMainClk(void)
{
    PMC_REGS->CKGR_MOR = CKGR_MOR_MOSCSEL(${CLK_MOSCSEL}) |\
                         CKGR_MOR_KEY_PASSWD |\
                         CKGR_MOR_MOSCXTST(${CLK_MOSCXTST}) |\
                         CKGR_MOR_MOSCRCEN(${CLK_MOSCRCEN?then('1','0')}) |\
                         CKGR_MOR_MOSCXTEN(${CLK_MOSCXTEN?then('1','0')});
}

<#if CLK_PLL_EN>
/*********************************************************************************
Initialize PLLA 
*********************************************************************************/
static void initPLLAClk(void)
{
    PMC_REGS->PMC_PLL_UPDT = PMC_PLL_UPDT_ID(PLL_ID_PLLA);
    PMC_REGS->PMC_PLL_ACR = PMC_PLL_ACR_LOOP_FILTER(0x9);
    PMC_REGS->PMC_PLL_CTRL1 = PMC_PLL_CTRL1_MUL(${CLK_PLL_MUL}) |\
                              PMC_PLL_CTRL1_FRACR(${CLK_PLL_FRACR});
    PMC_REGS->PMC_PLL_UPDT = PMC_PLL_UPDT_UPDATE_Msk | PMC_PLL_UPDT_ID(PLL_ID_PLLA);
    PMC_REGS->PMC_PLL_CTRL0 = PMC_PLL_CTRL0_ENLOCK_Msk |\
                              PMC_PLL_CTRL0_ENPLL_Msk |\
                              PMC_PLL_CTRL0_DIVPMC(${CLK_PLL_DIVPMC}) |\
                              PMC_PLL_CTRL0_ENPLLCK_Msk;
    PMC_REGS->PMC_PLL_UPDT = PMC_PLL_UPDT_UPDATE_Msk | 0;
    while ((PMC_REGS->PMC_PLL_ISR0 & PMC_PLL_ISR0_LOCKA_Msk) != PMC_PLL_ISR0_LOCKA_Msk);

    <#if CLK_PLLA_SS>
    PMC_REGS->PMC_PLL_SSR = PMC_PLL_SSR_ENSPREAD_Msk | PMC_PLL_SSR_STEP(${CLK_PLLA_SS_STEP}) | PMC_PLL_SSR_NSTEP(${CLK_PLLA_SS_NSTEP});
    </#if>
}
</#if>

/*********************************************************************************
Initialize CPU clock 
*********************************************************************************/
static void initCPUClk(void)
{
    PMC_REGS->PMC_CPU_CKR = (PMC_REGS->PMC_CPU_CKR & ~PMC_CPU_CKR_CSS_Msk) | PMC_CPU_CKR_CSS_SLOW_CLK;
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);

    PMC_REGS->PMC_CPU_CKR = (PMC_REGS->PMC_CPU_CKR & ~PMC_CPU_CKR_MDIV_Msk) | PMC_CPU_CKR_MDIV_${CLK_CPU_CKR_MDIV};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);

    PMC_REGS->PMC_CPU_CKR = (PMC_REGS->PMC_CPU_CKR & ~PMC_CPU_CKR_PRES_Msk) | PMC_CPU_CKR_PRES_${CLK_CPU_CKR_PRES};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);

    PMC_REGS->PMC_CPU_CKR = (PMC_REGS->PMC_CPU_CKR & ~PMC_CPU_CKR_CSS_Msk) | PMC_CPU_CKR_CSS_${CLK_CPU_CKR_CSS};
    while ((PMC_REGS->PMC_SR & PMC_SR_MCKRDY_Msk) != PMC_SR_MCKRDY_Msk);
}
</#if>
<#if CLK_UPLL_EN>
<#-- If UPLL is initilazed as part of the generator code, it will be done before CPU clock is updated to MHC configuration -->
<#-- In such case delay should be calculated with ROM code CPU frequency which is set to PLLA with 396 MHz (Datasheet Section 11.3) -->
<#if CLK_GENERATOR_CODE>
    <#assign DELAY_SRC_CLK_FREQUENCY = 396000000>
<#-- If UPLL is initialized after CPU clock is setup, then use whatever cpu clock is configured in MHC -->
<#else>
    <#assign DELAY_SRC_CLK_FREQUENCY = CPU_CLOCK_FREQUENCY>
</#if>    

/*********************************************************************************
Generate Software delay (in multiples of microsecond units) 
*********************************************************************************/
static void swDelayUs(uint32_t delay)
{
    uint32_t i, count;

    /* delay * (CPU_FREQ/1000000) / 6 */
    count = delay *  (${DELAY_SRC_CLK_FREQUENCY}/1000000)/6;

    /* 6 CPU cycles per iteration */
    for (i = 0; i < count; i++)
        __NOP();
}

/*********************************************************************************
Initialize UPLL
*********************************************************************************/
static void initUPLLCLK(void)
{
    /* STEP 1: PMC_PLL_UPDT to target UPLL, startup time of 150us and update disabled */
    PMC_REGS->PMC_PLL_UPDT = PMC_PLL_UPDT_STUPTIM(0x6) |\
                             PMC_PLL_UPDT_UPDATE(0x0) |\
                             PMC_PLL_UPDT_ID(PLL_ID_UPLL);

    /* STEP 2: Set the Analog controls to the values recommended by data sheet */
    PMC_REGS->PMC_PLL_ACR = PMC_PLL_ACR_LOOP_FILTER(0x1B) |\
                            PMC_PLL_ACR_LOCK_THR(0x4) |\
                            PMC_PLL_ACR_CONTROL(0x10);

    /* STEP 3: Set loop paramaters for the fractional PLL */
    PMC_REGS->PMC_PLL_CTRL1 = PMC_PLL_CTRL1_MUL(${CLK_UPLL_MUL}) |\
                              PMC_PLL_CTRL1_FRACR(${CLK_UPLL_FRACR});

    /* STEP 4: Enable UTMI Bandgap */ 
    PMC_REGS->PMC_PLL_ACR |= PMC_PLL_ACR_UTMIBG_Msk;

    /* STEP 5: Wait 10 us */        
    swDelayUs(10);

    /* STEP 6: Enable UTMI Internal Regulator */
    PMC_REGS->PMC_PLL_ACR |= PMC_PLL_ACR_UTMIVR_Msk;

    /* STEP 7: Wait 10 us */        
    swDelayUs(10);

    /* STEP 8: Update the PLL controls */
    PMC_REGS->PMC_PLL_UPDT |= PMC_PLL_UPDT_UPDATE_Msk;

    /* STEP 9: Enable UPLL, lock and PMC clock from UPLL */
    PMC_REGS->PMC_PLL_CTRL0 = PMC_PLL_CTRL0_ENLOCK_Msk |\
                              PMC_PLL_CTRL0_ENPLL_Msk |\
                              PMC_PLL_CTRL0_ENPLLCK_Msk;
    
    /* STEP 10: Wait for the lock bit to rise by polling the PMC_PLL_ISR0 */
    while ((PMC_REGS->PMC_PLL_ISR0 & PMC_PLL_ISR0_LOCKU_Msk) != PMC_PLL_ISR0_LOCKU_Msk);
}
</#if>

/*********************************************************************************
Initialize Programmable clocks 
*********************************************************************************/
static void initProgrammableClk(void)
{
    PMC_REGS->PMC_SCDR |= PMC_SCDR_PCK0_Msk | PMC_SCDR_PCK1_Msk;
<#list 0..1 as i>
<#if .vars["CLK_PCK"+i+"_EN"]>
<#assign css = .vars["CLK_PCK"+i+"_CSS"]>
<#assign pres = .vars["CLK_PCK"+i+"_PRES"]>
    PMC_REGS->PMC_PCK[${i}] = PMC_PCK_CSS_${css} |\
                                PMC_PCK_PRES(${pres});
    PMC_REGS->PMC_SCER |= PMC_SCDR_PCK${i}_Msk;
    while ((PMC_REGS->PMC_SR & PMC_SR_PCKRDY${i}_Msk) != PMC_SR_PCKRDY${i}_Msk);
</#if>
</#list>
}

/*********************************************************************************
Initialize Peripheral clocks
*********************************************************************************/
static void initPeriphClk(void)
{
    struct {
        uint8_t id;
        uint8_t clken;
        uint8_t gclken;
        uint8_t css;
        uint8_t div;
    } periphList[] =
    {
        <#list 0..50 as i>
            <#if .vars["CLK_ID_NAME_"+i]?has_content>
                <#assign name = .vars["CLK_ID_NAME_"+i]>
                <#assign clken = .vars[name+"_CLOCK_ENABLE"]>
                <#if .vars["CLK_"+name+"_GCLKEN"]?has_content && .vars["CLK_"+name+"_GCLKEN"]>
                    <#assign gclken = true>
                <#else>
                    <#assign gclken = false>
                </#if>
                <#if gclken>
                    <#assign gclkcss = .vars["CLK_"+name+"_GCLKCSS"]>
                    <#assign gclkdiv = .vars["CLK_"+name+"_GCLKDIV"]>
                <#else>
                    <#assign gclkcss = "0">
                    <#assign gclkdiv = "0">
                </#if>
                <#if clken || gclken>
                    <#if name == "EXT_MEMORY">
                        <#lt>        { ID_SDRAMC, 1, 0, 0, 0},
                    <#else>
                        <#lt>        { ID_${name}, ${clken?then("1", "0")}, ${gclken?then("1", "0")}, ${gclkcss}, ${gclkdiv}},
                    </#if>
                </#if>
            </#if>
        </#list>
        { ID_PERIPH_MAX + 1, 0, 0, 0, 0}//end of list marker
    };

    int count = sizeof(periphList)/sizeof(periphList[0]);
    for (int i = 0; i < count; i++)
    {
        if (periphList[i].id == (ID_PERIPH_MAX + 1))
        {
            break;
        }

        PMC_REGS->PMC_PCR = PMC_PCR_CMD_Msk |\
                            PMC_PCR_GCLKEN(periphList[i].gclken) |\
                            PMC_PCR_EN(periphList[i].clken) |\
                            PMC_PCR_GCLKDIV(periphList[i].div) |\
                            PMC_PCR_GCLKCSS(periphList[i].css) |\
                            PMC_PCR_PID(periphList[i].id);                
    }

}
<#if CLK_USB_EN>

/*********************************************************************************
Initialize USB OHCI clocks 
*********************************************************************************/
static void initUSBClk ( void )
{    	
    /* Configure USB OHCI clock source and divider */
	PMC_REGS->PMC_USB = PMC_USB_USBDIV(${CLK_USB_USBDIV}) | PMC_USB_USBS_${CLK_USB_USBS};
	
	/* Enable UHP48M and UHP12M OHCI clocks */
    PMC_REGS->PMC_SCER |= PMC_SCER_UHP_Msk;
}
</#if>
<#if CLK_QSPICLK_ENABLE>

/*********************************************************************************
Initialize QSPI Clock
*********************************************************************************/
static void initQSPIClk(void)
{
    PMC_REGS->PMC_SCER |= PMC_SCER_QSPICLK_Msk;
}
</#if>

<#if CLK_GENERATOR_CODE && CLK_DDR_ENABLE>

/*********************************************************************************
Initialize DDR Clock
*********************************************************************************/
static void initDDRClk(void)
{
    PMC_REGS->PMC_SCER |= PMC_SCER_DDRCK_Msk;
}
</#if>

/*********************************************************************************
Clock Initialize
*********************************************************************************/
void CLK_Initialize( void )
{
    <#if CLK_GENERATOR_CODE>
    /* Initialize slow clock generator */
    initSlowClk();

    /* Initialize main clock generator */
    initMainClk();
    <#if CLK_PLL_EN>

    /* Initialize PLLA clock generator */
    initPLLAClk();
    </#if>
    <#if CLK_UPLL_EN>

    /* Initialize UPLLA clock generator */
    initUPLLCLK();
    </#if>

    /* Initialize CPU clock */
    initCPUClk();
    </#if>
    <#if CLK_UPLL_EN && !CLK_GENERATOR_CODE>

    /* Initialize UPLLA clock generator */
    initUPLLCLK();
    </#if>
    
    /* Initialize Programmable clock */
    initProgrammableClk();

    /* Initialize Peripheral clock */
    initPeriphClk();
    <#if CLK_GENERATOR_CODE && CLK_DDR_ENABLE>

    /* Initialize DDR Clock */
    initDDRClk();
    </#if>
    <#if CLK_QSPICLK_ENABLE>

    /* Initialize QSPI Clock */
    initQSPIClk();
    </#if>
    <#if CLK_USB_EN>

    /* Initialize USB Clock */
    initUSBClk();
    </#if>
 
}
