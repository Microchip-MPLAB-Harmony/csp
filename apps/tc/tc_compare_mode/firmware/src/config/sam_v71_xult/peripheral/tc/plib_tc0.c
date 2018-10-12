/*******************************************************************************
  TC Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_tc0.c

  Summary
    TC peripheral library source file.

  Description
    This file implements the interface to the TC peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

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

/*  This section lists the other files that are included in this file.
*/
#include "device.h"
#include "plib_tc0.h"

 

 
 

 


/* Initialize channel in compare mode */
void TC0_CH0_CompareInitialize (void)
{
    /* clock selection and waveform selection */
    TC0_REGS->TC_CHANNEL[0].TC_CMR = TC_CMR_TCCLKS_TIMER_CLOCK4 | TC_CMR_WAVSEL_UP_RC | TC_CMR_WAVE_Msk | \
                TC_CMR_ACPA_TOGGLE | TC_CMR_ACPC_CLEAR | TC_CMR_AEEVT_CLEAR | \
                TC_CMR_BCPB_SET | TC_CMR_BCPC_CLEAR | TC_CMR_BEEVT_CLEAR ;


    /* external reset event configurations */
    TC0_REGS->TC_CHANNEL[0].TC_CMR |= TC_CMR_ENETRG_Msk | TC_CMR_EEVT_XC0 | \
                TC_CMR_EEVTEDG_NONE;

    /* write period */
    TC0_REGS->TC_CHANNEL[0].TC_RC = 11719U;

    /* write compare values */
    TC0_REGS->TC_CHANNEL[0].TC_RA = 2929U;
    TC0_REGS->TC_CHANNEL[0].TC_RB = 3000U;

}

/* Start the compare mode */
void TC0_CH0_CompareStart (void)
{
    TC0_REGS->TC_CHANNEL[0].TC_CCR = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
}

/* Stop the compare mode */
void TC0_CH0_CompareStop (void)
{
    TC0_REGS->TC_CHANNEL[0].TC_CCR = (TC_CCR_CLKDIS_Msk);
}

uint32_t TC0_CH0_CompareFrequencyGet()
{
    return (uint32_t)(1171875UL);
}

/* Configure the period value */
void TC0_CH0_ComparePeriodSet (uint16_t period)
{
    TC0_REGS->TC_CHANNEL[0].TC_RC = period;
}

/* Read the period value */
uint16_t TC0_CH0_ComparePeriodGet (void)
{
    return TC0_REGS->TC_CHANNEL[0].TC_RC;
}

/* Set the compare A value */
void TC0_CH0_CompareASet (uint16_t value)
{
    TC0_REGS->TC_CHANNEL[0].TC_RA = value;
}

/* Set the compare B value */
void TC0_CH0_CompareBSet (uint16_t value)
{
    TC0_REGS->TC_CHANNEL[0].TC_RB = value;
}

TC_COMPARE_STATUS TC0_CH0_CompareStatusGet(void)
{
    return ((TC0_REGS->TC_CHANNEL[0].TC_SR) & TC_COMPARE_STATUS_MSK);
}
 

 
 
 
 
 

/**
 End of File
*/
