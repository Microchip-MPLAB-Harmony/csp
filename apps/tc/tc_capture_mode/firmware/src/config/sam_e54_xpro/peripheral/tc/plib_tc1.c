/*******************************************************************************
  Timer/Counter(TC1) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_TC1.c

  Summary
    TC1 PLIB Implementation File.

  Description
    This file defines the interface to the TC peripheral library. This
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

#include "plib_tc1.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************


TC_CAPTURE_CALLBACK_OBJ TC1_CallbackObject;

// *****************************************************************************
// *****************************************************************************
// Section: TC1 Implementation
// *****************************************************************************
// *****************************************************************************

void TC1_CaptureInitialize( void )
{
    /* Reset TC */
    TC1_REGS->COUNT16.TC_CTRLA = TC_CTRLA_SWRST_Msk;

    while((TC1_REGS->COUNT16.TC_SYNCBUSY & TC_SYNCBUSY_SWRST_Msk) == TC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Configure counter mode, prescaler, standby & on demand mode */
    TC1_REGS->COUNT16.TC_CTRLA = TC_CTRLA_MODE_COUNT16 | TC_CTRLA_PRESCALER_DIV2 | TC_CTRLA_PRESCSYNC_PRESC
                                  | TC_CTRLA_CAPTEN0_Msk | TC_CTRLA_CAPTEN1_Msk  ;


    TC1_REGS->COUNT16.TC_EVCTRL = TC_EVCTRL_EVACT_PPW | TC_EVCTRL_TCEI_Msk;

    /* Clear all interrupt flags */
    TC1_REGS->COUNT16.TC_INTFLAG = TC_INTFLAG_Msk;

    /* Enable Interrupt */
    TC1_REGS->COUNT16.TC_INTENSET = TC_INTENSET_MC0_Msk;
    TC1_CallbackObject.callback = NULL;
}


void TC1_CaptureStart( void )
{
    /* Enable TC */
    TC1_REGS->COUNT16.TC_CTRLA |= TC_CTRLA_ENABLE_Msk;

    while((TC1_REGS->COUNT16.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

void TC1_CaptureStop( void )
{
    /* Disable TC */
    TC1_REGS->COUNT16.TC_CTRLA &= ~TC_CTRLA_ENABLE_Msk;

    while((TC1_REGS->COUNT16.TC_SYNCBUSY & TC_SYNCBUSY_ENABLE_Msk) == TC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Write Synchronization */
    }
}

uint32_t TC1_CaptureFrequencyGet( void )
{
    return (uint32_t)(30000000UL);
}


uint16_t TC1_Capture16bitChannel0Get( void )
{
    return (uint16_t)TC1_REGS->COUNT16.TC_CC[0];
}

uint16_t TC1_Capture16bitChannel1Get( void )
{
    return (uint16_t)TC1_REGS->COUNT16.TC_CC[1];
}

void TC1_CaptureCallbackRegister( TC_CAPTURE_CALLBACK callback, uintptr_t context )
{
    TC1_CallbackObject.callback = callback;
    TC1_CallbackObject.context = context;
}

void TC1_CaptureInterruptHandler( void )
{
    if (TC1_REGS->COUNT16.TC_INTENSET != 0)
    {
        TC_CAPTURE_STATUS status;
        status = (TC_CAPTURE_STATUS) (TC1_REGS->COUNT16.TC_INTFLAG);
        /* Clear all interrupts */
        TC1_REGS->COUNT16.TC_INTFLAG = TC_INTFLAG_Msk;

        if((status != TC_CAPTURE_STATUS_NONE) && TC1_CallbackObject.callback != NULL)
        {
            TC1_CallbackObject.callback(status, TC1_CallbackObject.context);
        }
    }
}

