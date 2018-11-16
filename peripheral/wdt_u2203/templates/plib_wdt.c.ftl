/*******************************************************************************
  Watchdog Timer PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${WDT_INSTANCE_NAME?lower_case}.c

  Summary:
    Interface definition of ${WDT_INSTANCE_NAME} PLIB.

  Description:
    This file defines the interface for the WDT Plib.
    It allows user to setup timeout duration and restart watch dog timer.
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

#include "plib_${WDT_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

<#if WDT_EW_ENABLE = true>
WDT_CALLBACK_OBJECT ${WDT_INSTANCE_NAME?lower_case}CallbackObj;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${WDT_INSTANCE_NAME} Interface Implementations
// *****************************************************************************
// *****************************************************************************

void ${WDT_INSTANCE_NAME}_Enable( void )
{
    /* Checking if Always On Bit is Enabled */
    if((${WDT_INSTANCE_NAME}_REGS->WDT_CTRL & WDT_CTRL_ALWAYSON_Msk) != WDT_CTRL_ALWAYSON_Msk)
    {
        /* Enable Watchdog Timer */
        ${WDT_INSTANCE_NAME}_REGS->WDT_CTRL |= WDT_CTRL_ENABLE_Msk;

        /* Wait for synchronization */
        while(${WDT_INSTANCE_NAME}_REGS->WDT_STATUS);
    }
<#if WDT_EW_ENABLE = true>

    /* Enable early warning interrupt */
    ${WDT_INSTANCE_NAME}_REGS->WDT_INTENSET = WDT_INTENSET_EW_Msk;
</#if>
}

void ${WDT_INSTANCE_NAME}_Disable( void )
{
    /* Disable Watchdog Timer */
    ${WDT_INSTANCE_NAME}_REGS->WDT_CTRL &= ~(WDT_CTRL_ENABLE_Msk);
<#if WDT_EW_ENABLE = true>

    /* Disable Early Watchdog Interrupt */
    ${WDT_INSTANCE_NAME}_REGS->WDT_INTENCLR = WDT_INTENCLR_EW_Msk;
</#if>
}

void ${WDT_INSTANCE_NAME}_Clear( void )
{
    /* Clear WDT and reset the WDT timer before the
       timeout occurs */
    ${WDT_INSTANCE_NAME}_REGS->WDT_CLEAR = WDT_CLEAR_CLEAR_KEY;

    /* Wait for synchronization */
    while(${WDT_INSTANCE_NAME}_REGS->WDT_STATUS);
}

<#if WDT_EW_ENABLE = true>
void ${WDT_INSTANCE_NAME}_CallbackRegister( WDT_CALLBACK callback, uintptr_t context )
{
    ${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback = callback;

    ${WDT_INSTANCE_NAME?lower_case}CallbackObj.context = context;
}

void ${WDT_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Clear Early Watchdog Interrupt */
    ${WDT_INSTANCE_NAME}_REGS->WDT_INTFLAG = WDT_INTFLAG_EW_Msk;

    if(${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback != NULL)
    {
        ${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback(${WDT_INSTANCE_NAME?lower_case}CallbackObj.context);
    }
}
</#if>
