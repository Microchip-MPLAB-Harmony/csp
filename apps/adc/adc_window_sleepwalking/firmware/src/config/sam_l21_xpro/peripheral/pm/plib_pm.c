/*******************************************************************************
  Power Manager(PM) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_pm.c

  Summary
    PM PLIB Implementation File.

  Description
    This file defines the interface to the PM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

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
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_pm.h"
void PM_Initialize( void )
{
    /* Configure PM */
    PM_REGS->PM_STDBYCFG = PM_STDBYCFG_BBIASLP(0)| PM_STDBYCFG_BBIASHS(0)| PM_STDBYCFG_LINKPD(0)| PM_STDBYCFG_VREGSMOD(0)| PM_STDBYCFG_DPGPD1_Msk| PM_STDBYCFG_DPGPD0_Msk| PM_STDBYCFG_PDCFG(0);

    /* Clear INTFLAG.PLRDY */
    PM_REGS->PM_INTFLAG |= PM_INTENCLR_PLRDY_Msk;

    /* Configure performance level */
    PM_REGS->PM_PLCFG = PM_PLCFG_PLSEL_PL2;

    /* Wait for performance level transition to complete */
    while(!(PM_REGS->PM_INTFLAG & PM_INTFLAG_PLRDY_Msk));
}

void PM_IdleModeEnter( void )
{
    /* Configure Idle Sleep mode */
    PM_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_IDLE_Val;

    /* Ensure that SLEEPMODE bits are configured with the given value */
    while (!(PM_REGS->PM_SLEEPCFG & PM_SLEEPCFG_SLEEPMODE_IDLE_Val));

    /* Wait for interrupt instruction execution */
    __WFI();
}

void PM_StandbyModeEnter( void )
{
    /* Configure Standby Sleep */
    PM_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_STANDBY_Val;

    /* Ensure that SLEEPMODE bits are configured with the given value */
    while (!(PM_REGS->PM_SLEEPCFG & PM_SLEEPCFG_SLEEPMODE_STANDBY_Val));

    /* Wait for interrupt instruction execution */
    __WFI();
}

void PM_BackupModeEnter( void )
{
    /* Configure Backup Sleep */
    PM_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_BACKUP_Val;

    /* Ensure that SLEEPMODE bits are configured with the given value */
    while (!(PM_REGS->PM_SLEEPCFG & PM_SLEEPCFG_SLEEPMODE_BACKUP_Val));

    /* Wait for interrupt instruction execution */
    __WFI();
}

void PM_OffModeEnter( void )
{
    /* Configure Off Sleep */
    PM_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_OFF_Val;

    /* Ensure that SLEEPMODE bits are configured with the given value */
    while (!(PM_REGS->PM_SLEEPCFG & PM_SLEEPCFG_SLEEPMODE_OFF_Val));

    /* Wait for interrupt instruction execution */
    __WFI();
}

/* ********Important Note********
 * When IORET is enabled, SWD access to the device will not be
 * available after waking up from Backup sleep until
 * the bit is cleared by the application.
 */
void PM_IO_RetentionSet( void )
{
    PM_REGS->PM_CTRLA |= PM_CTRLA_IORET_Msk;
}

void PM_IO_RetentionClear( void )
{
    PM_REGS->PM_CTRLA &= (~PM_CTRLA_IORET_Msk);
}

bool PM_ConfigurePerformanceLevel(PLCFG_PLSEL plsel)
{
    bool status = false;

    /* Write the value only if Performance Level Disable is not set */
    if (!(PM_REGS->PM_PLCFG & PM_PLCFG_PLDIS_Msk))
    {
        if((PM_REGS->PM_PLCFG & PM_PLCFG_PLSEL_Msk) != plsel)
        {
            /* Clear INTFLAG.PLRDY */
            PM_REGS->PM_INTFLAG |= PM_INTENCLR_PLRDY_Msk;

            /* Write PLSEL bits */
            PM_REGS->PM_PLCFG  = plsel;

            /* Wait for performance level transition to complete */
            while(!(PM_REGS->PM_INTFLAG & PM_INTFLAG_PLRDY_Msk));

            status = true;
        }
    }

    return status;
}

