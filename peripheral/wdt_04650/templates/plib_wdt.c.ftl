/*******************************************************************************
  WDT Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${WDT_INSTANCE_NAME?lower_case}.c

  Summary:
    WDT Source File

  Description:
    None

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

// Section: Included Files

#include "plib_${WDT_INSTANCE_NAME?lower_case}.h"

// Section: ${WDT_INSTANCE_NAME} Implementation

extern void __builtin_clrwdt(void);

<#if (CONFIG_FWDT_WDTEN?? && CONFIG_FWDT_WDTEN == "SW")>
void ${WDT_INSTANCE_NAME}_Enable( void )
{
    /* ON = 1 */
    WDTCONbits.ON = 1U;
}

void ${WDT_INSTANCE_NAME}_Disable( void )
{
    /* ON = 0 */
    WDTCONbits.ON = 0U;
}

</#if>
bool ${WDT_INSTANCE_NAME}_IsEnabled( void )
{
    return((bool)WDTCONbits.ON);
}

<#if (CONFIG_FWDT_WDTEN?? && CONFIG_FWDT_WDTEN == "SW")>
void ${WDT_INSTANCE_NAME}_WindowEnable( void )
{
    /* WINDIS = 0 */
    WDTCONbits.WINDIS = 0U;
}

void ${WDT_INSTANCE_NAME}_WindowDisable( void )
{
    /* WINDIS = 1 */
    WDTCONbits.WINDIS = 1U;
}
</#if>

bool ${WDT_INSTANCE_NAME}_IsWindowEnabled( void )
{
    return((bool)WDTCONbits.WINDIS);
}
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"

/* Following MISRA-C rules are deviated in the below code block */
/* MISRA C-2012 Rule 8.6 - Deviation record ID - H3_MISRAC_2012_R_8_6_DR_1 */
#pragma coverity compliance block deviate "MISRA C-2012 Rule 8.6"  "H3_MISRAC_2012_R_8_6_DR_1"
</#if>
void ${WDT_INSTANCE_NAME}_Clear( void )
{
  __builtin_clrwdt();
}
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 8.6"
</#if>