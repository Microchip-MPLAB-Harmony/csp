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
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
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

 

 
 


/* Initialize channel in capture mode */
void TC0_CH0_CaptureInitialize (void)
{
    /* Use peripheral clock */
    TC0_REGS->TC_CHANNEL[0].TC_EMR = TC_EMR_NODIVCLK_Msk;
        /* clock selection and capture configurations */
    TC0_REGS->TC_CHANNEL[0].TC_CMR = TC_CMR_LDRA_RISING | TC_CMR_LDRB_FALLING;


    /* external reset event configurations */
    TC0_REGS->TC_CHANNEL[0].TC_CMR |=  TC_CMR_ABETRG_Msk |  TC_CMR_ETRGEDG_FALLING;

}

/* Start the capture mode */
void TC0_CH0_CaptureStart (void)
{
    TC0_REGS->TC_CHANNEL[0].TC_CCR = (TC_CCR_CLKEN_Msk | TC_CCR_SWTRG_Msk);
}

/* Stop the capture mode */
void TC0_CH0_CaptureStop (void)
{
    TC0_REGS->TC_CHANNEL[0].TC_CCR = (TC_CCR_CLKDIS_Msk);
}

uint32_t TC0_CH0_CaptureFrequencyGet()
{
    return (uint32_t)(150000000UL);
}

/* Read last captured value of Capture A */
uint16_t TC0_CH0_CaptureAGet (void)
{
    return TC0_REGS->TC_CHANNEL[0].TC_RA;
}

/* Read last captured value of Capture B */
uint16_t TC0_CH0_CaptureBGet (void)
{
    return TC0_REGS->TC_CHANNEL[0].TC_RB;
}

TC_CAPTURE_STATUS TC0_CH0_CaptureStatusGet(void)
{
    return ((TC0_REGS->TC_CHANNEL[0].TC_SR) & TC_CAPTURE_STATUS_MSK);
}
 

 

 
 
 
 
 

/**
 End of File
*/
