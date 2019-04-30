/*******************************************************************************
  Timer/Counter(TC6) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_tc6.c

  Summary
    TC6 PLIB Implementation File.

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

#include "plib_tc6.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: TC6 Implementation
// *****************************************************************************
// *****************************************************************************

/* Initialize TC module in Compare Mode */
void TC6_CompareInitialize( void )
{
    /* Reset TC */
    TC6_REGS->COUNT16.TC_CTRLA = TC_CTRLA_SWRST_Msk;

    while((TC6_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }

    /* Configure counter mode & prescaler */
    TC6_REGS->COUNT16.TC_CTRLA = TC_CTRLA_MODE_COUNT16 | TC_CTRLA_PRESCALER_DIV64 | TC_CTRLA_WAVEGEN_MFRQ ;

    
    TC6_REGS->COUNT16.TC_CC[0] = 10000U;
    
    /* Clear all interrupt flags */
    TC6_REGS->COUNT16.TC_INTFLAG = TC_INTFLAG_Msk;

    

    while((TC6_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

/* Enable the counter */
void TC6_CompareStart( void )
{
    TC6_REGS->COUNT16.TC_CTRLA |= TC_CTRLA_ENABLE_Msk;
    while((TC6_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

/* Disable the counter */
void TC6_CompareStop( void )
{
    TC6_REGS->COUNT16.TC_CTRLA &= ~TC_CTRLA_ENABLE_Msk;
    while((TC6_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

uint32_t TC6_CompareFrequencyGet( void )
{
    return (uint32_t)(750000UL);
}

/* Get the current counter value */
uint16_t TC6_Compare16bitCounterGet( void )
{
    /* Write command to force COUNT register read synchronization */
    TC6_REGS->COUNT16.TC_READREQ = TC_READREQ_RREQ_Msk | TC_COUNT16_COUNT_REG_OFST;

    while((TC6_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }

    /* Read current count value */
    return (uint16_t)TC6_REGS->COUNT16.TC_COUNT;
}

/* Configure counter value */
void TC6_Compare16bitCounterSet( uint16_t count )
{
    TC6_REGS->COUNT16.TC_COUNT = count;

    while((TC6_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

/* Configure period value */
void TC6_Compare16bitPeriodSet( uint16_t period )
{
    /* Configure period value */
    TC6_REGS->COUNT16.TC_CC[0] = period;
    while((TC6_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
}

/* Read period value */
uint16_t TC6_Compare16bitPeriodGet( void )
{
    /* Write command to force CC register read synchronization */
    TC6_REGS->COUNT16.TC_READREQ = TC_READREQ_RREQ_Msk | TC_COUNT16_CC_REG_OFST;

    while((TC6_REGS->COUNT16.TC_STATUS & TC_STATUS_SYNCBUSY_Msk))
    {
        /* Wait for Write Synchronization */
    }
    /* Get period value */
    return (uint16_t)TC6_REGS->COUNT16.TC_CC[0];
}





/* Get interrupt flag status */
TC_COMPARE_STATUS TC6_CompareStatusGet( void )
{
    TC_COMPARE_STATUS compare_status;
    compare_status = ((TC6_REGS->COUNT16.TC_INTFLAG) & TC_COMPARE_STATUS_MSK);
    /* Clear timer overflow interrupt */
    TC6_REGS->COUNT16.TC_INTFLAG = TC_COMPARE_STATUS_MSK;
    return compare_status;
}



