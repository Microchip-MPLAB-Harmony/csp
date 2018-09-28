/*******************************************************************************
Interface definition of RTT PLIB.

Company:
	Microchip Technology Inc.

File Name:
	plib_rtt.c

Summary:
	Interface definition of RTT Plib.

Description:
	This file defines the interface for the RTT Plib.
	It allows user to Program, Erase and lock the on-chip FLASH memory.
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

#include "device.h"
#include "plib_rtt.h"

RTT_OBJECT rtt;
	
void RTT_Initialize(void)
{
	RTT_REGS->RTT_MR = RTT_MR_RTTRST_Msk;
	RTT_REGS->RTT_MR = RTT_MR_RTPRES(32768) | RTT_MR_RTTDIS_Msk  | RTT_MR_ALMIEN_Msk;
}

void RTT_Enable(void)
{
	RTT_REGS->RTT_MR|= RTT_MR_RTTRST_Msk;
	RTT_REGS->RTT_MR&= ~(RTT_MR_RTTDIS_Msk);
}

void RTT_Disable(void)
{
	RTT_REGS->RTT_MR|= RTT_MR_RTTDIS_Msk;
}

void RTT_PrescalarUpdate(uint16_t prescale)
{
	uint32_t rtt_mr = RTT_REGS->RTT_MR;
	uint32_t flag = rtt_mr & RTT_MR_RTTINCIEN_Msk;
	rtt_mr &= ~(RTT_MR_RTPRES_Msk | RTT_MR_RTTINCIEN_Msk);
	RTT_REGS->RTT_MR = rtt_mr | prescale | RTT_MR_RTTRST_Msk;
	if (flag)
	{
		RTT_REGS->RTT_MR|=  RTT_MR_RTTINCIEN_Msk;
	}
}

void RTT_AlarmValueSet(uint32_t alarm)
{
	uint32_t flag = 0;
	flag = RTT_REGS->RTT_MR& (RTT_MR_ALMIEN_Msk);
	RTT_REGS->RTT_MR&= ~(RTT_MR_ALMIEN_Msk);
	RTT_REGS->RTT_AR = alarm;
	if (flag)
	{
		RTT_REGS->RTT_MR|= RTT_MR_ALMIEN_Msk;
	}
}
void RTT_EnableInterrupt (RTT_INTERRUPT_TYPE type)
{
	RTT_REGS->RTT_MR|= type;
}
void RTT_DisableInterrupt(RTT_INTERRUPT_TYPE type)
{
	RTT_REGS->RTT_MR&= ~(type);
}
void RTT_CallbackRegister( RTT_CALLBACK callback, uintptr_t context )
{
	rtt.callback = callback;
	rtt.context = context;
} 
 
uint32_t RTT_TimerValueGet(void)
{
	uint32_t rtt_val = RTT_REGS->RTT_VR;
	while (rtt_val != RTT_REGS->RTT_VR) 
	{
		rtt_val = RTT_REGS->RTT_VR;
	}
	return rtt_val;
}

uint32_t RTT_FrequencyGet(void)
{
	uint32_t flag = 0;
	
	flag =  (RTT_REGS->RTT_MR) & (RTT_MR_RTC1HZ_Msk);
	
	if (flag)
	{
		return 1000;
	}
	else
	{
		flag = (RTT_REGS->RTT_MR) & (RTT_MR_RTPRES_Msk);
		if (flag == 0)
		{
			return (32768 / 65536);
		}
		else
		{
			return (32768 / flag); 
		}
	}
}

void RTT_InterruptHandler()
{
	volatile uint32_t status = RTT_REGS->RTT_SR;
	uint32_t flags = RTT_REGS->RTT_MR;
	RTT_REGS->RTT_MR&= ~(RTT_MR_ALMIEN_Msk | RTT_MR_RTTINCIEN_Msk);
	if(flags & RTT_MR_RTTINCIEN_Msk)
	{
		if(status & RTT_SR_RTTINC_Msk)
		{
			if (rtt.callback != NULL)
			{
				rtt.callback(RTT_PERIODIC, rtt.context);
			}
		}
		RTT_REGS->RTT_MR|= (RTT_MR_RTTINCIEN_Msk);
	}
	if(flags & RTT_MR_ALMIEN_Msk)
	{
		if(status & RTT_SR_ALMS_Msk)
		{
			if (rtt.callback != NULL)
			{
				rtt.callback(RTT_ALARM, rtt.context);
			}
		}
		RTT_REGS->RTT_MR|= (RTT_MR_ALMIEN_Msk);
	}	
}
