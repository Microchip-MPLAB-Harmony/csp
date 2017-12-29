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
Copyright (c) 2016 released Microchip Technology Inc.  All rights reserved.
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
	RTT->RTT_MR = RTT_MR_RTTRST;
	RTT->RTT_MR = RTT_MR_RTPRES(${rttRTPRES}) | RTT_MR_RTTDIS ${rttINCIEN?then(' | RTT_MR_RTTINCIEN','')}${rttALMIEN?then(' | RTT_MR_ALMIEN','')}${rttRTC1HZ?then(' | RTT_MR_RTC1HZ','')};
}

void RTT${INDEX?string}_Enable(void)
{
	RTT->RTT_MR |= RTT_MR_RTTRST;
	RTT->RTT_MR &= ~(RTT_MR_RTTDIS);
}

void RTT${INDEX?string}_Disable(void)
{
	RTT->RTT_MR |= RTT_MR_RTTDIS;
}

void RTT${INDEX?string}_PrescalarUpdate(uint16_t prescale)
{
	uint32_t rtt_mr = RTT->RTT_MR;
	uint32_t flag = rtt_mr & RTT_MR_RTTINCIEN_Msk;
	rtt_mr &= ~(RTT_MR_RTPRES_Msk | RTT_MR_RTTINCIEN_Msk);
	RTT->RTT_MR = rtt_mr | prescale | RTT_MR_RTTRST;
	if (flag)
	{
		RTT->RTT_MR |=  RTT_MR_RTTINCIEN_Msk;
	}
}

<#if rttINCIEN == true || rttALMIEN == true>
	<#lt>void RTT${INDEX?string}_AlarmValueSet(uint32_t alarm)
	<#lt>{
	<#lt>	uint32_t flag = 0;
	<#lt>	flag = RTT->RTT_MR & (RTT_MR_ALMIEN_Msk);
	<#lt>	RTT->RTT_MR &= ~(RTT_MR_ALMIEN_Msk);
	<#lt>	RTT->RTT_AR = alarm;
	<#lt>	if (flag)
	<#lt>	{
	<#lt>		RTT->RTT_MR |= RTT_MR_ALMIEN_Msk;
	<#lt>	}
	<#lt>	
	<#lt>}
	<#lt>
	<#lt>void RTT${INDEX?string}_EnableInterrupt (RTT_INTERRUPT_TYPE type)
	<#lt>{
	<#lt>	RTT->RTT_MR |= type;
	<#lt>}
	<#lt>
	<#lt>void RTT${INDEX?string}_DisableInterrupt(RTT_INTERRUPT_TYPE type)
	<#lt>{
	<#lt>	RTT->RTT_MR &= ~(type);
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
	uint32_t rtt_val = RTT->RTT_VR;
	while (rtt_val != RTT->RTT_VR) 
	{
		rtt_val = RTT->RTT_VR;
	}
	return rtt_val;
}

uint32_t RTT${INDEX?string}_FrequencyGet(void)
{
	uint32_t flag = 0;
	
	flag =  (RTT->RTT_MR) & (RTT_MR_RTC1HZ_Msk);
	
	if (flag)
	{
		return 1000;
	}
	else
	{
		flag = (RTT->RTT_MR) & (RTT_MR_RTPRES_Msk);
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
