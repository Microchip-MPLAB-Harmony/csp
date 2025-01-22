/*******************************************************************************
  Deadman Timer (${DMT_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DMT_INSTANCE_NAME?lower_case}.c

  Summary:
    ${DMT_INSTANCE_NAME} PLIB Implementation file

  Description:
    This file defines the interface to the deadman timer (DMT) peripheral library.
    This library provides ability to clear the DMT counter.

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


// Section: Included Files

#include "plib_${DMT_INSTANCE_NAME?lower_case}.h"

// Section:  Macro Definitions

#define DMT_STEP1_CLEAR 0x40
#define DMT_STEP2_CLEAR 0x08
#define DMT_STATUS_MASK 0xE1

// Section: ${DMT_INSTANCE_NAME} Implementation

void ${DMT_INSTANCE_NAME}_Initialize(void)
{ 
	// Instruction fetch counter limit = ${PSCNT_REG_POR}
	PSCNT = ${PSCNT_REG_POR};
	
	// Window interval limit =  ${PSINTV_REG_POR}
	PSINTV = ${PSINTV_REG_POR};
	
    ${DMT_INSTANCE_NAME}_Enable();
}

void ${DMT_INSTANCE_NAME}_Enable( void )
{
    /* ON = 1 */
    DMTCONbits.ON = 1;
}

void ${DMT_INSTANCE_NAME}_Clear( void )
{
    DMTPRECLRbits.STEP1 = DMT_STEP1_CLEAR;

    DMTCLRbits.STEP2 = DMT_STEP2_CLEAR;
}

bool ${DMT_INSTANCE_NAME}_ClearWindowStatusGet( void )
{
    /* Clear window open status */
    return (bool) DMTSTATbits.WINOPN;
}

uint32_t ${DMT_INSTANCE_NAME}_CounterGet( void )
{
    /* Current counter value */
    return (uint32_t) DMTCNT;
}

uint32_t ${DMT_INSTANCE_NAME}_TimeOutCountGet( void )
{
    /* Maximum count selected */
    return (uint32_t) PSCNT;
}

uint32_t ${DMT_INSTANCE_NAME}_WindowIntervalGet( void )
{
    /* Window interval value */
    return (uint32_t) PSINTV;
}

void ${DMT_INSTANCE_NAME}_PostEventClear(void)
{
	PPPC = 0x4100UL;
	PPC = 0x88UL;
}

uint32_t ${DMT_INSTANCE_NAME}_StatusGet(void) 
{   
    uint32_t status = 0;
    status = (uint32_t)(DMTSTAT & DMT_STATUS_MASK);
    return status;
}