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

<#if EVSYS_INTERRUPT_MODE0 || EVSYS_INTERRUPT_MODE1 || EVSYS_INTERRUPT_MODE2 || EVSYS_INTERRUPT_MODE3 || EVSYS_INTERRUPT_MODE_OTHER>

</#if>

<#if EVSYS_INTERRUPT_MODE0 || EVSYS_INTERRUPT_MODE1 || EVSYS_INTERRUPT_MODE2 || EVSYS_INTERRUPT_MODE3 || EVSYS_INTERRUPT_MODE_OTHER>
	<#lt>typedef enum
	<#lt>{
	<#lt>	EVSYS_INT_EVD = EVSYS_CHINTENSET_EVD_Msk,
	<#lt>	EVSYS_INT_OVERRUN = EVSYS_CHINTENSET_OVR_Msk,

	<#lt>} EVSYS_INT_MASK;

    <#lt>typedef enum
    <#lt>{<#list 0..NUM_SYNC_CHANNELS as i>
    <#lt>	EVSYS_CHANNEL_${i} = ${i},</#list>

    <#lt>} EVSYS_CHANNEL;

	<#lt>typedef void (*EVSYS_CALLBACK)(uintptr_t context, EVSYS_CHANNEL channel, uint32_t int_cause);
    
	<#lt>typedef struct
	<#lt>{
	<#lt>	EVSYS_CALLBACK          callback;
	<#lt>	uintptr_t               context;
	<#lt>} EVSYS_OBJECT ;

</#if>

/***************************** EVSYS API *******************************/
void ${EVSYS_INSTANCE_NAME}_Initialize( void );
<#if EVSYS_INTERRUPT_MODE0 || EVSYS_INTERRUPT_MODE1 || EVSYS_INTERRUPT_MODE2 || EVSYS_INTERRUPT_MODE3 || EVSYS_INTERRUPT_MODE_OTHER>
	<#lt>void ${EVSYS_INSTANCE_NAME}_CallbackRegister( EVSYS_CALLBACK callback, uintptr_t context );
	<#lt>void ${EVSYS_INSTANCE_NAME}_InterruptDisable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interrupt);
	<#lt>void ${EVSYS_INSTANCE_NAME}_InterruptEnable(EVSYS_CHANNEL channel, EVSYS_INT_MASK interrupt);
</#if>

#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif
