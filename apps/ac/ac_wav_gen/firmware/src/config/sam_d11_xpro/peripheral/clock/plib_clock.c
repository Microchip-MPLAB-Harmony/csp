/*******************************************************************************
  CLOCK PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_clock.c

  Summary:
    CLOCK PLIB Implementation File.

  Description:
    None

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_clock.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: CLOCK Interface Routines
// *****************************************************************************
// *****************************************************************************

static void SYSCTRL_Initialize( void )
{
    /****************** OSC32K Initialization  ******************************/
    uint32_t calibValue = (uint32_t)(((*(uint64_t*)0x806020) >> 38 ) & 0x7f);

    /* Configure 32K RC oscillator */
    SYSCTRL_REGS->SYSCTRL_OSC32K = SYSCTRL_OSC32K_CALIB(calibValue) | SYSCTRL_OSC32K_STARTUP(0) | SYSCTRL_OSC32K_ENABLE_Msk | SYSCTRL_OSC32K_EN32K_Msk ;

    while(!((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_OSC32KRDY_Msk) == SYSCTRL_PCLKSR_OSC32KRDY_Msk))
    {
        /* Waiting for the OSC32K Ready state */
    }
}


static void DFLL_Initialize( void )
{
    /****************** DFLL Initialization  *********************************/

    SYSCTRL_REGS->SYSCTRL_DFLLCTRL &= ~SYSCTRL_DFLLCTRL_ONDEMAND_Msk;

    while((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_DFLLRDY_Msk) != SYSCTRL_PCLKSR_DFLLRDY_Msk)
    {
        /* Waiting for the Ready state */
    }

    /* Load Calibration Value */
    uint8_t calibCoarse = (uint8_t)(((*(uint32_t*)0x806024) >> 26 ) & 0x3f);
    calibCoarse = (((calibCoarse) == 0x3F) ? 0x1F : (calibCoarse));
    uint16_t calibFine = (uint16_t)(((*(uint32_t*)0x806028)) & 0x3ff);

    SYSCTRL_REGS->SYSCTRL_DFLLVAL = SYSCTRL_DFLLVAL_COARSE(calibCoarse) | SYSCTRL_DFLLVAL_FINE(calibFine);


    /* Configure DFLL */
    SYSCTRL_REGS->SYSCTRL_DFLLCTRL = SYSCTRL_DFLLCTRL_ENABLE_Msk ;

    while((SYSCTRL_REGS->SYSCTRL_PCLKSR & SYSCTRL_PCLKSR_DFLLRDY_Msk) != SYSCTRL_PCLKSR_DFLLRDY_Msk)
    {
        /* Waiting for DFLL to be ready */
    }
}


static void GCLK0_Initialize( void )
{
    
    GCLK_REGS->GCLK_GENCTRL = GCLK_GENCTRL_SRC(7) | GCLK_GENCTRL_GENEN_Msk | GCLK_GENCTRL_ID(0);

    while((GCLK_REGS->GCLK_STATUS & GCLK_STATUS_SYNCBUSY_Msk) == GCLK_STATUS_SYNCBUSY_Msk)
    {
        /* wait for the Generator 0 synchronization */
    }
}


static void GCLK1_Initialize( void )
{
    GCLK_REGS->GCLK_GENCTRL = GCLK_GENCTRL_SRC(4) | GCLK_GENCTRL_GENEN_Msk | GCLK_GENCTRL_ID(1);

    while((GCLK_REGS->GCLK_STATUS & GCLK_STATUS_SYNCBUSY_Msk) == GCLK_STATUS_SYNCBUSY_Msk)
    {
        /* wait for the Generator 1 synchronization */
    }
}

void CLOCK_Initialize( void )
{
    /* Function to Initialize the Oscillators */
    SYSCTRL_Initialize();

    DFLL_Initialize();
    GCLK1_Initialize();
    GCLK0_Initialize();


    /* Selection of the Generator and write Lock for EIC */
    GCLK_REGS->GCLK_CLKCTRL = GCLK_CLKCTRL_ID(5) | GCLK_CLKCTRL_GEN(0x0)  | GCLK_CLKCTRL_CLKEN_Msk;

    /* Selection of the Generator and write Lock for TC1 TC2 */
    GCLK_REGS->GCLK_CLKCTRL = GCLK_CLKCTRL_ID(18) | GCLK_CLKCTRL_GEN(0x0)  | GCLK_CLKCTRL_CLKEN_Msk;

    /* Selection of the Generator and write Lock for AC_DIG */
    GCLK_REGS->GCLK_CLKCTRL = GCLK_CLKCTRL_ID(20) | GCLK_CLKCTRL_GEN(0x0)  | GCLK_CLKCTRL_CLKEN_Msk;

    /* Selection of the Generator and write Lock for AC_ANA */
    GCLK_REGS->GCLK_CLKCTRL = GCLK_CLKCTRL_ID(21) | GCLK_CLKCTRL_GEN(0x1)  | GCLK_CLKCTRL_CLKEN_Msk;

    /* Selection of the Generator and write Lock for DAC */
    GCLK_REGS->GCLK_CLKCTRL = GCLK_CLKCTRL_ID(22) | GCLK_CLKCTRL_GEN(0x0)  | GCLK_CLKCTRL_CLKEN_Msk;


    /* Configure the APBC Bridge Clocks */
    PM_REGS->PM_APBCMASK = 0x740;


    /* Disable RC oscillator */
    SYSCTRL_REGS->SYSCTRL_OSC8M = 0x0;
}
