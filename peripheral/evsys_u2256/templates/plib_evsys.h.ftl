/*******************************************************************************
  Interface definition of EVSYS PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${EVSYS_INSTANCE_NAME?lower_case}.h

  Summary:
    Interface definition of the Event System Plib (EVSYS).

  Description:
    This file defines the interface for the EVSYS Plib.
    It allows user to setup event generators and users.
*******************************************************************************/

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

#ifndef ${EVSYS_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define ${EVSYS_INSTANCE_NAME}_H

#include "device.h"
#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus // Provide C++ Compatibility
 extern "C" {
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

<#if EVSYS_INTERRUPT_MODE == true>
	<#lt>typedef void (*EVSYS_CALLBACK)(uint32_t int_cause, uintptr_t context);
</#if>

<#if EVSYS_INTERRUPT_MODE == true>
	<#lt>typedef enum
	<#lt>{
	<#lt>	EVSYS_INT_OVERRUN = EVSYS_INTENSET_OVR0_Msk,
	<#lt>	EVSYS_INT_EVENT_DETECT = EVSYS_INTENSET_EVD0_Msk,
	<#lt>} EVSYS_INT_MASK;
<#assign TOTAL_CHANNEL = EVSYS_CHANNEL_NUMBER?number >

    <#lt>typedef enum
	<#lt>{
        <#list 0..TOTAL_CHANNEL as i>
            <#assign CHANNEL_ENABLE    = "EVSYS_CHANNEL_"  + i>
            <#if .vars[CHANNEL_ENABLE]?has_content>
            <#if (.vars[CHANNEL_ENABLE] == true)>
        <#lt>    /* EVSYS Channel ${i} */
        <#lt>    EVSYS_CHANNEL_${i} = ${i},
            </#if>
            </#if>
        </#list>
	<#lt>} EVSYS_CHANNEL;

	<#lt>typedef struct
	<#lt>{
	<#lt>	EVSYS_CALLBACK          callback;
	<#lt>	uintptr_t               context;
	<#lt>} EVSYS_OBJECT ;
</#if>
/***************************** EVSYS API *******************************/
void ${EVSYS_INSTANCE_NAME}_Initialize( void );
<#if EVSYS_INTERRUPT_MODE == true>
	<#lt>void ${EVSYS_INSTANCE_NAME}_CallbackRegister( EVSYS_CHANNEL channel, EVSYS_CALLBACK callback, uintptr_t context );
	<#lt>void ${EVSYS_INSTANCE_NAME}_InterruptDisable( EVSYS_CHANNEL channel, EVSYS_INT_MASK interrupt );
	<#lt>void ${EVSYS_INSTANCE_NAME}_InterruptEnable( EVSYS_CHANNEL channel,EVSYS_INT_MASK interrupt );
</#if>

#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif
