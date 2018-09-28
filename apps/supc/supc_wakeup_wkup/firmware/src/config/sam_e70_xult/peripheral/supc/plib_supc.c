/*******************************************************************************
  Supply Controller (SUPC) Peripheral Library (PLIB) 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_supc.c

  Summary:
    SUPC Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "plib_supc.h"

static void WaitEntryClockSetup (bool xtal_disable);


// *****************************************************************************
// *****************************************************************************
// Section: SUPC Implementation
// *****************************************************************************
// *****************************************************************************

void SUPC_Initialize (void)
{
	SUPC_REGS->SUPC_SMMR = SUPC_SMMR_SMSMPL_SMD;
	
	SUPC_REGS->SUPC_MR = (SUPC_MR_KEY_PASSWD | SUPC_MR_ONREG_ONREG_USED | SUPC_MR_BODRSTEN_ENABLE  | SUPC_MR_BKUPRETON_Msk);  
	
	SUPC_REGS->SUPC_WUMR = (SUPC_WUMR_LPDBC(0)    \
							| SUPC_WUMR_WKUPDBC(2)   );	
    
    SUPC_REGS->SUPC_WUIR = SUPC_WUIR_WKUPEN7_ENABLE | SUPC_WUIR_WKUPT7_HIGH;
}

void SUPC_SleepModeEnter (void)
{
    SCB->SCR &= (uint32_t)~SCB_SCR_SLEEPDEEP_Msk;

	/* Enable Interrupt */
	__DMB();
    __enable_irq();
	
	/* Enter Sleep 	*/
	__DSB();
    __WFI();
}

void SUPC_WaitModeEnter (WAITMODE_FLASH_STATE flash_lpm, WAITMODE_WKUP_SOURCE source)
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
    PMC_REGS->PMC_FSMR = (flash_lpm | source);
	
	/* Set Flash Wait State at 0	*/
    EFC_REGS->EEFC_FMR = EEFC_FMR_FWS(0) | EEFC_FMR_CLOE_Msk;

	/* Set HCLK = MCK by configuring MDIV to 0	*/
	 PMC_REGS->PMC_MCKR = ( PMC_REGS->PMC_MCKR & ~PMC_MCKR_MDIV_Msk) | PMC_MCKR_MDIV_EQ_PCK;
	
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
	CLK_Initialize();
	
	
	/* Enable CPU Interrupt	*/
	__DMB();
    __enable_irq();	
}

void SUPC_BackupModeEnter (void)
{
    SCB->SCR |= SCB_SCR_SLEEPDEEP_Msk;

	/* Switch off voltage regulator	*/
    SUPC_REGS->SUPC_CR |= (SUPC_CR_KEY_PASSWD | SUPC_CR_VROFF_Msk); 

	/* Enable CPU Interrupt	*/
	__DMB();
    __enable_irq();

	/* Enter Backup	*/
	__DSB();	
	__WFI();	
}


uint32_t SUPC_GPBRRead (GPBR_REGS_INDEX reg)
{
    return GPBR_REGS->SYS_GPBR[reg];
}

void SUPC_GPBRWrite (GPBR_REGS_INDEX reg, uint32_t data)
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
	PMC_REGS->CKGR_PLLAR = CKGR_PLLAR_ONE_Msk | CKGR_PLLAR_MULA(0);	
	
	/* Disable UPLL Clock */
	PMC_REGS->CKGR_UCKR &= ~CKGR_UCKR_UPLLEN_Msk;
	
	/* Disable Crystal	*/
	if(xtal_disable)
    {
		PMC_REGS->CKGR_MOR = (PMC_REGS->CKGR_MOR & ~CKGR_MOR_MOSCXTEN_Msk) | CKGR_MOR_KEY_PASSWD;
    }
}
