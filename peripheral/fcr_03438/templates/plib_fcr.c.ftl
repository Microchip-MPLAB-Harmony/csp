/*******************************************************************************
  Non-Volatile Memory Controller(${FCR_INSTANCE_NAME}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FCR_INSTANCE_NAME?lower_case}.c

  Summary:
    Interface definition of ${FCR_INSTANCE_NAME} Plib.

  Description:
    This file defines the interface for the ${FCR_INSTANCE_NAME} Plib.
    It allows user to Program, Erase and lock the on-chip Non Volatile Flash
    Memory.
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

#include <string.h>
#include "plib_${FCR_INSTANCE_NAME?lower_case}.h"

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Interface Functions                                               */
/* ************************************************************************** */
/* ************************************************************************** */

void ${FCR_INSTANCE_NAME}_Initialize( void )
{
    ${FCR_INSTANCE_NAME}_REGS->FCR_CTRLA =
                  <#if FCR_AUTOWS == false>
<#lt>                     ((${FCR_INSTANCE_NAME}_REGS->FCR_CTRLA) & (FCR_CTRLA_ARB_Msk | FCR_CTRLA_RDBUFWS_Msk)) | \
<#lt>                     FCR_CTRLA_FWS(${FCR_FWS}) | \
                  <#else>
<#lt>                     ((${FCR_INSTANCE_NAME}_REGS->FCR_CTRLA) & (FCR_CTRLA_ARB_Msk | FCR_CTRLA_RDBUFWS_Msk | FCR_CTRLA_FWS_Msk)) | \
                  </#if>
<#lt>                     FCR_CTRLA_ADRWS(${FCR_ADRWS?then('1', '0')}) | \
<#lt>                     FCR_CTRLA_AUTOWS(${FCR_AUTOWS?then('1', '0')});
}

bool ${FCR_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    memcpy((void *)data, (void *)(address), length);

    return true;
}