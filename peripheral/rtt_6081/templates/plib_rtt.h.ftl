/*******************************************************************************
 Interface definition of RTT PLIB.
 
 Company:
	Microchip Technology Inc.
	
 File Name:
	plib_rtt.h
	
 Summary:
	Interface definition of RTT Plib.
	
 Description:
	This file defines the interface for the RTT Plib.
	It allows user to start, stop and configure the on-chip real time timer.
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

#ifndef ${RTT_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define ${RTT_INSTANCE_NAME}_H

#include <stdint.h>
#include <stddef.h>
#include "plib_rtt_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
	extern "C" {
#endif
// DOM-IGNORE-END

void ${RTT_INSTANCE_NAME}_Initialize(void);
void ${RTT_INSTANCE_NAME}_Enable(void);
void ${RTT_INSTANCE_NAME}_Disable(void);
void ${RTT_INSTANCE_NAME}_PrescalarUpdate(uint16_t prescale);

<#if rttINCIEN == true || rttALMIEN == true>
	<#lt>void ${RTT_INSTANCE_NAME}_AlarmValueSet(uint32_t alarm);
	<#lt>void ${RTT_INSTANCE_NAME}_EnableInterrupt (RTT_INTERRUPT_TYPE type);
	<#lt>void ${RTT_INSTANCE_NAME}_DisableInterrupt(RTT_INTERRUPT_TYPE type);
</#if>
uint32_t ${RTT_INSTANCE_NAME}_TimerValueGet(void);
uint32_t ${RTT_INSTANCE_NAME}_FrequencyGet(void); 
<#if rttINCIEN == true || rttALMIEN == true>
	<#lt>void ${RTT_INSTANCE_NAME}_CallbackRegister( RTT_CALLBACK callback, uintptr_t context );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif
