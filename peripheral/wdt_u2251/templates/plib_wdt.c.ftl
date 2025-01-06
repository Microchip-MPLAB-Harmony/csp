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

<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${WDT_INSTANCE_NAME?lower_case}.h"

<#if WDT_EW_ENABLE = true>
static volatile WDT_CALLBACK_OBJECT ${WDT_INSTANCE_NAME?lower_case}CallbackObj;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${WDT_INSTANCE_NAME} Interface Implementations
// *****************************************************************************
// *****************************************************************************

void ${WDT_INSTANCE_NAME}_Enable( void )
{
    /* Checking if Always On Bit is Enabled */
    if((${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA & WDT_CTRLA_ALWAYSON_Msk) != WDT_CTRLA_ALWAYSON_Msk)
    {
        /* Enable Watchdog Timer */
        ${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA |= (uint8_t)WDT_CTRLA_ENABLE_Msk;

        /* Wait for synchronization */
        while(${WDT_INSTANCE_NAME}_REGS->WDT_SYNCBUSY != 0U)
        {

        }
    }
<#if WDT_EW_ENABLE = true>

    /* Enable early warning interrupt */
    ${WDT_INSTANCE_NAME}_REGS->WDT_INTENSET = (uint8_t)WDT_INTENSET_EW_Msk;
</#if>
}

/* This function is used to disable the Watchdog Timer */
void ${WDT_INSTANCE_NAME}_Disable( void )
{
    /* Wait for synchronization */
    while(${WDT_INSTANCE_NAME}_REGS->WDT_SYNCBUSY != 0U)
    {

    }

    /* Disable Watchdog Timer */
    ${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA &= (uint8_t)(~WDT_CTRLA_ENABLE_Msk);

    /* Wait for synchronization */
    while(${WDT_INSTANCE_NAME}_REGS->WDT_SYNCBUSY != 0U)
    {

    }
<#if WDT_EW_ENABLE = true>

    /* Disable Early Watchdog Interrupt */
    ${WDT_INSTANCE_NAME}_REGS->WDT_INTENCLR = (uint8_t)WDT_INTENCLR_EW_Msk;
</#if>
}

void ${WDT_INSTANCE_NAME}_EnableWindowMode( void )
{
    while(WDT_REGS->WDT_SYNCBUSY != 0U)
    {

    }

    /* Window mode can be changed only if peripheral is disabled or ALWAYS ON bit is set */
    if(((${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA & WDT_CTRLA_ENABLE_Msk) == 0U) || ((${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA & WDT_CTRLA_ALWAYSON_Msk) != 0U))
    {
        /* Enable window mode */
        ${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA |= (uint8_t)WDT_CTRLA_WEN_Msk;
    }

    while(WDT_REGS->WDT_SYNCBUSY != 0U)
    {

    }
}

void ${WDT_INSTANCE_NAME}_DisableWindowMode( void )
{
    while(WDT_REGS->WDT_SYNCBUSY != 0U)
    {

    }

    /* Window mode can be changed only if peripheral is disabled or ALWAYS ON bit is set */
    if(((${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA & WDT_CTRLA_ENABLE_Msk) == 0U) || ((${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA & WDT_CTRLA_ALWAYSON_Msk) != 0U))
    {
        /* Disable window mode */
        ${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA &= (uint8_t)(~WDT_CTRLA_WEN_Msk);
    }

    while(WDT_REGS->WDT_SYNCBUSY != 0U)
    {

    }
}

bool ${WDT_INSTANCE_NAME}_IsEnabled(void)
{
    return ((${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA & (WDT_CTRLA_ALWAYSON_Msk | WDT_CTRLA_ENABLE_Msk)) != 0U);
}

bool ${WDT_INSTANCE_NAME}_IsAlwaysOn(void)
{
    return ((${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA & WDT_CTRLA_ALWAYSON_Msk) != 0U);
}

bool ${WDT_INSTANCE_NAME}_IsWindowModeEnabled(void)
{
    return ((${WDT_INSTANCE_NAME}_REGS->WDT_CTRLA & WDT_CTRLA_WEN_Msk) != 0U);
}


void ${WDT_INSTANCE_NAME}_TimeoutPeriodSet(uint8_t TimeoutPeriod)
{
    /* Set WDT timeout period */
    ${WDT_INSTANCE_NAME}_REGS->WDT_CONFIG = (${WDT_INSTANCE_NAME}_REGS->WDT_CONFIG & (uint8_t)~WDT_CONFIG_PER_Msk) | (TimeoutPeriod & (uint8_t)WDT_CONFIG_PER_Msk);
}

/* If application intends to stay in active mode after clearing WDT, then use WDT_Clear API to clear the WDT. This avoids CPU from waiting or stalling for Synchronization.
 * If application intends to enter low power mode after clearing WDT, then use the WDT_ClearWithSync API to clear the WDT.
 */
void ${WDT_INSTANCE_NAME}_Clear( void )
{
    if ((${WDT_INSTANCE_NAME}_REGS->WDT_SYNCBUSY & WDT_SYNCBUSY_CLEAR_Msk) != WDT_SYNCBUSY_CLEAR_Msk)
    {
        /* Clear WDT and reset the WDT timer before the
        timeout occurs */
        ${WDT_INSTANCE_NAME}_REGS->WDT_CLEAR = (uint8_t)WDT_CLEAR_CLEAR_KEY;
    }
}

/* This API must be used if application intends to enter low power mode after clearing WDT.
 * It waits for write synchronization to complete as the device must not enter low power mode
 * while write sync is in progress.
 */
void ${WDT_INSTANCE_NAME}_ClearWithSync( void )
{
    /* Wait for synchronization */
    while(${WDT_INSTANCE_NAME}_REGS->WDT_SYNCBUSY != 0U)
    {

    }

    /* Clear WDT and reset the WDT timer before the
    timeout occurs */
    ${WDT_INSTANCE_NAME}_REGS->WDT_CLEAR = (uint8_t)WDT_CLEAR_CLEAR_KEY;

    /* Wait for synchronization */
    while(${WDT_INSTANCE_NAME}_REGS->WDT_SYNCBUSY != 0U)
    {

    }
}

<#if WDT_EW_ENABLE = true>
void ${WDT_INSTANCE_NAME}_CallbackRegister( WDT_CALLBACK callback, uintptr_t context)
{
    ${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback = callback;

    ${WDT_INSTANCE_NAME?lower_case}CallbackObj.context = context;
}

void __attribute__((used)) ${WDT_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Clear Early Watchdog Interrupt */
    ${WDT_INSTANCE_NAME}_REGS->WDT_INTFLAG = (uint8_t)WDT_INTFLAG_EW_Msk;

    if( ${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback != NULL )
    {
        uintptr_t context = ${WDT_INSTANCE_NAME?lower_case}CallbackObj.context;
        ${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback(context);
    }
}
</#if>
