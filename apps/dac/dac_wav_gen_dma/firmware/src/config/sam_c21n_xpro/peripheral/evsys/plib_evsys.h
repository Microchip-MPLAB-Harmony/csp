/*******************************************************************************
  Interface definition of EVSYS PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_evsys.h

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

#ifndef EVSYS_H    // Guards against multiple inclusion
#define EVSYS_H

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

typedef void (*EVSYS_CALLBACK)(uint32_t int_cause, uintptr_t context);

typedef enum
{
	EVSYS_INT_OVERRUN = EVSYS_INTENSET_OVR0_Msk,
	EVSYS_INT_EVENT_DETECT = EVSYS_INTENSET_EVD0_Msk,
} EVSYS_INT_MASK;

typedef enum
{
    /* EVSYS Channel 0 */
    EVSYS_CHANNEL_0 = 0,
} EVSYS_CHANNEL;

typedef struct
{
	EVSYS_CALLBACK          callback;
	uintptr_t               context;
} EVSYS_OBJECT ;
/***************************** EVSYS API *******************************/
void EVSYS_Initialize( void );
void EVSYS_CallbackRegister( EVSYS_CHANNEL channel, EVSYS_CALLBACK callback, uintptr_t context );
void EVSYS_InterruptDisable( EVSYS_CHANNEL channel, EVSYS_INT_MASK interrupt );
void EVSYS_InterruptEnable( EVSYS_CHANNEL channel,EVSYS_INT_MASK interrupt );

#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif
