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
<#if (core.PRODUCT_FAMILY == "PIC32CX_BZ3")>
#define Power_Down_Control_register_ll (*((volatile uint32_t *)(0x41012430)))
</#if>

<#if DEEP_SLEEP_MODE_EXIST??>
void POWER_Initialize( void )
{
    /* Unlock system */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;

    DSCON_REGS->DSCON_DSCON = 0x${DSCON_VALUE};
    DSCON_REGS->DSCON_DSCON = 0x${DSCON_VALUE};

    /* Lock System */
    CFG_REGS->CFG_SYSKEY = 0;
}
</#if>
void POWER_LowPowerModeEnter (POWER_LOW_POWER_MODE mode)
{
    /* Unlock system */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;

    switch(mode)
    {
        case LOW_POWER_IDLE_MODE: 
                        CRU_REGS->CRU_OSCCONCLR = CRU_OSCCON_SLPEN_Msk;
                        break;
        case LOW_POWER_SLEEP_MODE:
                        CRU_REGS->CRU_OSCCONSET = CRU_OSCCON_SLPEN_Msk;
<#if (core.PRODUCT_FAMILY == "PIC32CX_BZ3")>
                        // Set BT to enter in low power mode
                        Power_Down_Control_register_ll |= 0x20;
                        Power_Down_Control_register_ll |= 0x80;
</#if>
                        break;
<#if DREAM_MODE_EXIST??>               
        case LOW_POWER_DREAM_MODE:
                        CRU_REGS->CRU_OSCCONSET = CRU_OSCCON_SLPEN_Msk | CRU_OSCCON_DRMEN_Msk;
<#if (core.PRODUCT_FAMILY == "PIC32CX_BZ3")>
                        // Set BT to enter in low power mode
                        Power_Down_Control_register_ll |= 0x20;
                        Power_Down_Control_register_ll |= 0x80;
</#if>
                        break;
</#if>                        
<#if DEEP_SLEEP_MODE_EXIST??>                        
        case LOW_POWER_DEEP_SLEEP_MODE:
                        CRU_REGS->CRU_OSCCONSET = CRU_OSCCON_SLPEN_Msk;
                        DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_DSEN_Msk;
                        DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_DSEN_Msk;
                        break;
</#if>
<#if EXTREME_DEEP_SLEEP_MODE_EXIST??>                        
        case LOW_POWER_EXTREME_DEEP_SLEEP_MODE:
                        DSCON_REGS->DSCON_DSCON &= (~DSCON_DSCON_XSEMAEN_Msk); // Disable Extended semaphore register
                        DSCON_REGS->DSCON_DSCON &= (~DSCON_DSCON_XSEMAEN_Msk);
                        DSCON_REGS->DSCON_DSCON &= (~DSCON_DSCON_RTCPWREQ_Msk); // Disable power to RTCC
                        DSCON_REGS->DSCON_DSCON &= (~DSCON_DSCON_RTCPWREQ_Msk);
                        DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_RTCCWDIS_Msk; // Disable wake up from RTCC
                        DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_RTCCWDIS_Msk;
                        
                        CFG_REGS->CFG_CFGCON4 &= (~CFG_CFGCON4_DSWDTEN_Msk); // Disable DSWDT

                        CRU_REGS->CRU_OSCCONSET = CRU_OSCCON_SLPEN_Msk;
                        DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_DSEN_Msk;
                        DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_DSEN_Msk;
                        break;
</#if>
        default: 
                        return;
    }

    /* Lock System */
    CFG_REGS->CFG_SYSKEY = 0;

    /* enter into selected low power mode */
    __WFI();
}

<#if DEEP_SLEEP_MODE_EXIST??>
POWER_DS_WAKEUP_SOURCE POWER_DS_WakeupSourceGet( void )
{
    return (POWER_DS_WAKEUP_SOURCE)(DSCON_REGS->DSCON_DSWAKE);
}

void POWER_DS_SoftwareRestore(void)
{
    /* Unlock system */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;

    DSCON_REGS->DSCON_DSCON &= ~DSCON_DSCON_DSSR_Msk;
    DSCON_REGS->DSCON_DSCON &= ~DSCON_DSCON_DSSR_Msk;

    /* Lock System */
    CFG_REGS->CFG_SYSKEY = 0;
}

// DSCON.RELEASE must be 0 before calling this
void POWER_DS_WakeupSourceClear( POWER_DS_WAKEUP_SOURCE wakeupSource )
{
    DSCON_REGS->DSCON_DSWAKE &= ~wakeupSource;
}

void POWER_DS_ExtendedSemaphoreEnable(void)
{
    /* Unlock system */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;

    DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_XSEMAEN_Msk;
    DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_XSEMAEN_Msk;

    /* Lock System */
    CFG_REGS->CFG_SYSKEY = 0;
}
void POWER_DS_ExtendedSemaphoreDisable(void)
{
    /* Unlock system */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;

    DSCON_REGS->DSCON_DSCON &= (~DSCON_DSCON_XSEMAEN_Msk);
    DSCON_REGS->DSCON_DSCON &= (~DSCON_DSCON_XSEMAEN_Msk);

    /* Lock System */
    CFG_REGS->CFG_SYSKEY = 0;
}
void POWER_DS_RTCC_PowerEnable(void)
{
    /* Unlock system */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;

    DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_RTCPWREQ_Msk;
    DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_RTCPWREQ_Msk;

    /* Lock System */
    CFG_REGS->CFG_SYSKEY = 0;
}
void POWER_DS_RTCC_PowerDisable(void)
{
    /* Unlock system */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;

    DSCON_REGS->DSCON_DSCON &= (~DSCON_DSCON_RTCPWREQ_Msk);
    DSCON_REGS->DSCON_DSCON &= (~DSCON_DSCON_RTCPWREQ_Msk);

    /* Lock System */
    CFG_REGS->CFG_SYSKEY = 0;
}
void POWER_DS_RTCC_WakeupEnable(void)
{
    /* Unlock system */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;

    DSCON_REGS->DSCON_DSCON &= (~DSCON_DSCON_RTCCWDIS_Msk);
    DSCON_REGS->DSCON_DSCON &= (~DSCON_DSCON_RTCCWDIS_Msk);

    /* Lock System */
    CFG_REGS->CFG_SYSKEY = 0;
}
void POWER_DS_RTCC_WakeupDisable(void)
{
    /* Unlock system */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;

    DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_RTCCWDIS_Msk;
    DSCON_REGS->DSCON_DSCON |= DSCON_DSCON_RTCCWDIS_Msk;

    /* Lock System */
    CFG_REGS->CFG_SYSKEY = 0;
}

void POWER_DS_SemaphoreWrite(POWER_DS_SEMAPHORE sema, uint32_t semaValue)
{
    /* Unlock system */
    CFG_REGS->CFG_SYSKEY = 0x00000000;
    CFG_REGS->CFG_SYSKEY = 0xAA996655;
    CFG_REGS->CFG_SYSKEY = 0x556699AA;
    
    if (sema == POWER_DS_SEMAPHORE_1)
    {
        DSCON_REGS->DSCON_DSSEMA1 = semaValue;
        DSCON_REGS->DSCON_DSSEMA1 = semaValue;
    }
    else
    {
        DSCON_REGS->DSCON_DSSEMA1 = semaValue;
        DSCON_REGS->DSCON_DSSEMA1 = semaValue;
    }

    /* Lock System */
    CFG_REGS->CFG_SYSKEY = 0;
}

uint32_t POWER_DS_SemaphoreRead(POWER_DS_SEMAPHORE sema)
{
    if (sema == POWER_DS_SEMAPHORE_1)
    {
        return (DSCON_REGS->DSCON_DSSEMA1);
    }
    else
    {
        return (DSCON_REGS->DSCON_DSXSEMA1);
    }
}
</#if>