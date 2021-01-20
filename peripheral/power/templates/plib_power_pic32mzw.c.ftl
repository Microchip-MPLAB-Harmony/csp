/*******************************************************************************
  Resets (Power) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_power.c

  Summary
    Power PLIB Implementation File.

  Description
    This file defines the interface to the DSCTRL peripheral library.
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
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER SOURCED, EVEN IF MICROCHIP HAS
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

#include "plib_power.h"

// *****************************************************************************
// *****************************************************************************
// Section: Power Implementation
// *****************************************************************************
// *****************************************************************************
<#if DEEP_SLEEP_MODE_EXIST??>
void POWER_Initialize( void )
{
    /* unlock system */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;

    DSCON = 0x${DSCON_VALUE};
    DSCON = 0x${DSCON_VALUE};

    SYSKEY = 0;
}
</#if>
void POWER_LowPowerModeEnter (POWER_LOW_POWER_MODE mode)
{
    /* Unlock system */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;

    switch(mode)
    {
        case LOW_POWER_IDLE_MODE: 
                        OSCCONCLR = _OSCCON_SLPEN_MASK;
                        break;
        case LOW_POWER_SLEEP_MODE:
                        OSCCONSET = _OSCCON_SLPEN_MASK;
                        break;
<#if DREAM_MODE_EXIST??>               
        case LOW_POWER_DREAM_MODE:
                        OSCCONSET = _OSCCON_SLPEN_MASK | _OSCCON_DRMEN_MASK;
                        break;
</#if>                        
<#if DEEP_SLEEP_MODE_EXIST??>                        
        case LOW_POWER_DEEP_SLEEP_MODE:
                        OSCCONSET = _OSCCON_SLPEN_MASK;
                        DSCONbits.DSEN = 1;
                        DSCONbits.DSEN = 1;
                        while(DSCONbits.DSEN == 0);
                        break;
</#if>
        default: 
                        return;
    }

    SYSKEY = 0x0;

    /* enter into selected low power mode */
    asm volatile("wait");
}

<#if DEEP_SLEEP_MODE_EXIST??>
POWER_DS_WAKEUP_SOURCE POWER_DS_WakeupSourceGet( void )
{
    return (POWER_DS_WAKEUP_SOURCE)(DSWAKE);
}

void POWER_DS_SoftwareRestore(void)
{
    /* unlock system */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;

    DSCONbits.DSSR= 0;
    DSCONbits.DSSR = 0;

    SYSKEY = 0;
}

// DSCON.RELEASE must be 0 before calling this
void POWER_DS_WakeupSourceClear( POWER_DS_WAKEUP_SOURCE wakeupSource )
{
    DSWAKE &= ~wakeupSource;
}

void POWER_DS_SemaphoreWrite(uint32_t sema1Value)
{
    /* unlock system */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;
    DSSEMA1 = sema1Value;
    DSSEMA1 = sema1Value;
}

uint32_t POWER_DS_SemaphoreRead(void)
{
    return DSSEMA1;
}

<#if DS_EXTENDED_REG_ENABLE == true>
void POWER_DS_ExtendedSemaphoreWrite(POWER_DS_EXTENDED_SEMAPHORE xsema, uint32_t xsemaValue)
{
    /* unlock system */
    SYSKEY = 0x00000000;
    SYSKEY = 0xAA996655;
    SYSKEY = 0x556699AA;
    *((volatile uint32_t *)(&DSXSEMA1)+ xsema) = xsemaValue;
    *((volatile uint32_t *)(&DSXSEMA1)+ xsema) = xsemaValue;
}

uint32_t POWER_DS_ExtendedSemaphoreRead(POWER_DS_EXTENDED_SEMAPHORE xsema)
{
    return (*((volatile uint32_t *)(&DSXSEMA1)+ xsema));
}
</#if>
</#if>