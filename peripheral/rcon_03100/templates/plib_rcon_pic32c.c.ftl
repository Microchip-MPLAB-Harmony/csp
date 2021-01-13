/*******************************************************************************
  Resets (${RCON_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${RCON_INSTANCE_NAME?lower_case}.c

  Summary
    ${RCON_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the RCON peripheral library.
    This library provides access to and control of the associated Resets.

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

#include "plib_${RCON_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${RCON_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

RCON_RESET_CAUSE ${RCON_INSTANCE_NAME}_ResetCauseGet( void )
{
    return (RCON_RESET_CAUSE)(RCON_REGS->RCON_RCON);
}

void ${RCON_INSTANCE_NAME}_ResetCauseClear( RCON_RESET_CAUSE cause )
{
    /* Clear reset cause status flag */
    RCON_REGS->RCON_RCONCLR = cause;
}

void __attribute__((noreturn)) ${RCON_INSTANCE_NAME}_SoftwareReset( void )
{   
    /* Unlock System */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;

    RCON_REGS->RCON_RSWRSTSET = RCON_RSWRST_SWRST_Msk;

    /* Read RSWRST register to trigger reset */
    RCON_REGS->RCON_RSWRST;

    /* Prevent any unwanted code execution until reset occurs */
    while(1);
}