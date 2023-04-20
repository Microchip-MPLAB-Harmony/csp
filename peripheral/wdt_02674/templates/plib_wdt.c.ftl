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

#include "device.h"
#include "plib_${WDT_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${WDT_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

<#if (CONFIG_FWDTEN?? && CONFIG_FWDTEN == "OFF") || (CONFIG_WDTEN?? && CONFIG_WDTEN == "OFF")>
void ${WDT_INSTANCE_NAME}_Enable( void )
{
    /* ON = 1 */
    WDTCONbits.ON = 1;
}

void ${WDT_INSTANCE_NAME}_Disable( void )
{
    /* ON = 0 */
    WDTCONbits.ON = 0;
}

</#if>
bool ${WDT_INSTANCE_NAME}_IsEnabled( void )
{
    return((bool)WDTCONbits.ON);
}

<#if CONFIG_WINDIS == "NORMAL">
void ${WDT_INSTANCE_NAME}_WindowEnable( void )
{
    /* WDTWINEN = 1 */
    WDTCONbits.WDTWINEN = 1;
}

void ${WDT_INSTANCE_NAME}_WindowDisable( void )
{
    /* WDTWINEN = 0 */
    WDTCONbits.WDTWINEN = 0;
}

</#if>
bool ${WDT_INSTANCE_NAME}_IsWindowEnabled( void )
{
    return((bool)WDTCONbits.WDTWINEN);
}

/* MISRA C-2012 Rule 11.3 violated 1 time below. Deviation record ID - H3_MISRAC_2012_R_11_3_DR_1*/
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
<#if COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
</#if>
#pragma coverity compliance block deviate:1 "MISRA C-2012 Rule 11.3" "H3_MISRAC_2012_R_11_3_DR_1"
</#if>
void ${WDT_INSTANCE_NAME}_Clear( void )
{
    <#-- Below is done family-by-family, as there are differences in clearing WDT -->
    /* Writing specific value to only upper 16 bits of WDTCON register clears WDT counter */
    /* Only write to the upper 16 bits of the register when clearing. */
    /* WDTCLRKEY = 0x5743 */
    volatile uint16_t * wdtclrkey = ( (volatile uint16_t *)&WDTCON ) + 1;
    *wdtclrkey = 0x5743;
}
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 11.3"
<#if COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic pop
</#if>
</#if>
/* MISRAC 2012 deviation block end */