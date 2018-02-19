/*******************************************************************************
Interface definition of EEFC PLIB.

Company:
	Microchip Technology Inc.

File Name:
	plib_rtt.c

Summary:
	Interface definition of EEFC Plib.

Description:
	This file defines the interface for the EEFC Plib.
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

#include "plib_rtt${INDEX?string}.h"

void RTT${INDEX?string}_Initialize(void)
{
	_RTT_REGS->RTT_MR.w = RTT_MR_RTTRST_Msk;
	_RTT_REGS->RTT_MR.w = RTT_MR_RTPRES(${rttRTPRES}) | RTT_MR_RTTDIS_Msk ${rttINCIEN?then(' | RTT_MR_RTTINCIEN_Msk','')}${rttALMIEN?then(' | RTT_MR_ALMIEN_Msk','')}${rttRTC1HZ?then(' | RTT_MR_RTC1HZ_Msk','')};
}

void RTT${INDEX?string}_Enable(void)
{
	_RTT_REGS->RTT_MR.w |= RTT_MR_RTTRST_Msk;
	_RTT_REGS->RTT_MR.w &= ~(RTT_MR_RTTDIS_Msk);
}

void RTT${INDEX?string}_Disable(void)
{
	_RTT_REGS->RTT_MR.w |= RTT_MR_RTTDIS_Msk;
}

void RTT${INDEX?string}_PrescalarUpdate(uint16_t prescale)
{
	uint32_t rtt_mr = _RTT_REGS->RTT_MR.w;
	uint32_t flag = rtt_mr & RTT_MR_RTTINCIEN_Msk;
	rtt_mr &= ~(RTT_MR_RTPRES_Msk | RTT_MR_RTTINCIEN_Msk);
	_RTT_REGS->RTT_MR.w = rtt_mr | prescale | RTT_MR_RTTRST_Msk;
	if (flag)
	{
		_RTT_REGS->RTT_MR.w |=  RTT_MR_RTTINCIEN_Msk;
	}
}

<#if rttINCIEN == true || rttALMIEN == true>
	<#lt>void RTT${INDEX?string}_AlarmValueSet(uint32_t alarm)
	<#lt>{
	<#lt>	uint32_t flag = 0;
	<#lt>	flag = _RTT_REGS->RTT_MR.w & (RTT_MR_ALMIEN_Msk);
	<#lt>	_RTT_REGS->RTT_MR.w &= ~(RTT_MR_ALMIEN_Msk);
	<#lt>	_RTT_REGS->RTT_AR.w = alarm;
	<#lt>	if (flag)
	<#lt>	{
	<#lt>		_RTT_REGS->RTT_MR.w |= RTT_MR_ALMIEN_Msk;
	<#lt>	}
	<#lt>	
	<#lt>}
	<#lt>
	<#lt>void RTT${INDEX?string}_EnableInterrupt (RTT_INTERRUPT_TYPE type)
	<#lt>{
	<#lt>	_RTT_REGS->RTT_MR.w |= type;
	<#lt>}
	<#lt>
	<#lt>void RTT${INDEX?string}_DisableInterrupt(RTT_INTERRUPT_TYPE type)
	<#lt>{
	<#lt>	_RTT_REGS->RTT_MR.w &= ~(type);
	<#lt>}
	<#lt>
	<#lt>void RTT${INDEX?string}_CallbackRegister( RTT_CALLBACK callback, uintptr_t context )
	<#lt>{
	<#lt>	rtt.callback = callback;
	<#lt>	rtt.context = context;
	<#lt>} 
</#if>
 
uint32_t RTT${INDEX?string}_TimerValueGet(void)
{
	uint32_t rtt_val = _RTT_REGS->RTT_VR.w;
	while (rtt_val != _RTT_REGS->RTT_VR.w) 
	{
		rtt_val = _RTT_REGS->RTT_VR.w;
	}
	return rtt_val;
}

uint32_t RTT${INDEX?string}_FrequencyGet(void)
{
	uint32_t flag = 0;
	
	flag =  (_RTT_REGS->RTT_MR.w) & (RTT_MR_RTC1HZ_Msk);
	
	if (flag)
	{
		return 1000;
	}
	else
	{
		flag = (_RTT_REGS->RTT_MR.w) & (RTT_MR_RTPRES_Msk);
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
<#if rttINCIEN == true || rttALMIEN == true>

	<#lt>void RTT${INDEX?string}_InterruptHandler()
	<#lt>{
	<#lt>	volatile uint32_t status = _RTT_REGS->RTT_SR.w;
	<#lt>	uint32_t flags = _RTT_REGS->RTT_MR.w;
	<#lt>	_RTT_REGS->RTT_MR.w &= ~(RTT_MR_ALMIEN_Msk | RTT_MR_RTTINCIEN_Msk);
	<#lt>	if(flags & RTT_MR_RTTINCIEN_Msk)
	<#lt>	{
	<#lt>		if(status & RTT_SR_RTTINC_Msk)
	<#lt>		{
	<#lt>			rtt.callback(rtt.context, RTT_PERIODIC);
	<#lt>		}
	<#lt>		_RTT_REGS->RTT_MR.w |= (RTT_MR_RTTINCIEN_Msk);
	<#lt>	}
	<#lt>	if(flags & RTT_MR_ALMIEN_Msk)
	<#lt>	{
	<#lt>		if(status & RTT_SR_ALMS_Msk)
	<#lt>		{
	<#lt>			rtt.callback(rtt.context, RTT_ALARM);
	<#lt>		}
	<#lt>		_RTT_REGS->RTT_MR.w |= (RTT_MR_ALMIEN_Msk);
	<#lt>	}	
	<#lt>}
</#if>