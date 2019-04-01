/*******************************************************************************
  Reset Controller(${RSTC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${RSTC_INSTANCE_NAME?lower_case}.c

  Summary
    ${RSTC_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the RSTC peripheral library.
    This library provides access to and control of the associated
    Reset Controller.

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

#include "plib_${RSTC_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${RSTC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
<#if RSTC_WAKEUP_PIN_NUMBER??>
void RSTC_Initialize(void)
{
    <#if RSTC_DEBOUNCE != "0x00">
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_WKDBCONF = RSTC_WKDBCONF_WKDBCNT(${RSTC_DEBOUNCE});
    </#if>
    <#if WAKEUP_POLARITY_VALUE != "0">
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_WKPOL= RSTC_WKPOL_WKPOL(0x${WAKEUP_POLARITY_VALUE});
    </#if>
    <#if WAKEUP_ENABLE_VALUE != "0">
    ${RSTC_INSTANCE_NAME}_REGS->RSTC_WKEN = RSTC_WKEN_WKEN(0x${WAKEUP_ENABLE_VALUE});
    </#if>
}

RSTC_WAKEUP_CAUSE RSTC_WakeupCauseGet (void)
{
    return (RSTC_WAKEUP_CAUSE) (${RSTC_INSTANCE_NAME}_REGS->RSTC_WKCAUSE);
}

</#if>
RSTC_RESET_CAUSE ${RSTC_INSTANCE_NAME}_ResetCauseGet( void )
{
    return ( RSTC_RESET_CAUSE ) ${RSTC_INSTANCE_NAME}_REGS->RSTC_RCAUSE;
}

<#if RSTC_BKUPEXIT_LENGTH??>
RSTC_BKUPEXIT_CAUSE RSTC_BackupExitCauseGet (void)
{
    return ( RSTC_BKUPEXIT_CAUSE ) RSTC_REGS->RSTC_BKUPEXIT;
}
</#if>
