/*******************************************************************************
  Digital-to-Analog Converter (DAC) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_dac.c

  Summary:
    DAC PLIB Implementation file

  Description:
    This file defines the interface to the DAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#include "plib_dac.h"
#include "device.h"

						 
/* (DAC DATA) Mask DATA[15:12] Bit */
#define DAC_DATA_MSB_MASK                    (0x0FFFU)

/* (DAC DATA) Mask DATA[3:0] Bit */
#define DAC_DATA_LSB_MASK                    (0xFFF0U)
						 
// *****************************************************************************
// *****************************************************************************
// Section: DAC Implementation
// *****************************************************************************
// *****************************************************************************

void DAC_Initialize (void)
{
	/* Reset DAC Peripheral */
    DAC_REGS->DAC_CTRLA = DAC_CTRLA_SWRST_Msk;
	while (((DAC_REGS->DAC_CTRLA & DAC_CTRLA_SWRST_Msk) == DAC_CTRLA_SWRST_Msk) && ((DAC_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_SWRST_Msk) == DAC_SYNCBUSY_SWRST_Msk));
	
    DAC_REGS->DAC_CTRLB = DAC_CTRLB_REFSEL (1);

	
	
	DAC_REGS->DAC_DACCTRL[1] = DAC_DACCTRL_ENABLE_Msk | DAC_DACCTRL_CCTRL (0x2) | DAC_DACCTRL_REFRESH (0) ;
	DAC_REGS->DAC_EVCTRL = DAC_REGS->DAC_EVCTRL  | DAC_EVCTRL_STARTEI1_Msk;
	
	/* Enable DAC */
    DAC_REGS->DAC_CTRLA |= DAC_CTRLA_ENABLE_Msk;
	while ((DAC_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_ENABLE_Msk) == DAC_SYNCBUSY_ENABLE_Msk);
}

void DAC_DataWrite (DAC_CHANNEL_NUM channel, uint16_t data)
{
	/* Write Data to DATA1 Register for conversion(DATA[11:0]) */
	DAC_REGS->DAC_DATA[1] = DAC_DATA_MSB_MASK & DAC_DATA_DATA(data);
	while ((DAC_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA1_Msk) == DAC_SYNCBUSY_DATA1_Msk);
}

bool DAC_IsReady (DAC_CHANNEL_NUM channel)
{
    return (bool)(((DAC_REGS->DAC_STATUS >> channel) & DAC_STATUS_READY0_Msk) == DAC_STATUS_READY0_Msk);
}