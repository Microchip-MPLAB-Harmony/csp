/*******************************************************************************
  Power Manager(${PM_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PM_INSTANCE_NAME?lower_case}.c

  Summary
    ${PM_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the PM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_${PM_INSTANCE_NAME?lower_case}.h"

void ${PM_INSTANCE_NAME}_IdleModeEnter( void )
{
    <#if PM_SLEEP_IDLE_OPTION ? has_content>
    /* Configure Idle Sleep mode */
    SCB->SCR &= ~SCB_SCR_SLEEPDEEP_Msk;
    <@compress single_line=true>${PM_INSTANCE_NAME}_REGS->PM_SLEEP = PM_SLEEP_IDLE(${PM_SLEEP_IDLE_OPTION});</@compress>
    </#if>
    /* Wait for interrupt instruction execution */
    __WFI();
}

void ${PM_INSTANCE_NAME}_StandbyModeEnter( void )
{
    /* Configure Standby Sleep */
    SCB->SCR |= SCB_SCR_SLEEPDEEP_Msk;
    /* Wait for interrupt instruction execution */
    __WFI();
}

PM_RESET_CAUSE ${PM_INSTANCE_NAME}_ResetCauseGet( void )
{
    return (PM_RESET_CAUSE) ${PM_INSTANCE_NAME}_REGS->PM_RCAUSE;
}

