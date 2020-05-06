/*******************************************************************************
  Interface definition of ${CMCC_INSTANCE_NAME} PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CMCC_INSTANCE_NAME?lower_case}.h

  Summary:
    Interface definition of the ${CMCC_INSTANCE_NAME}(Cortex M Cache Controller) Peripheral Library

  Description:
    This file defines the interface for the ${CMCC_INSTANCE_NAME} Plib.
*******************************************************************************/

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

#ifndef PLIB_CMCC_H    // Guards against multiple inclusion
#define PLIB_CMCC_H


#ifdef __cplusplus // Provide C++ Compatibility
	extern "C" {
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

#define ${CMCC_INSTANCE_NAME}_NO_OF_WAYS     4
#define ${CMCC_INSTANCE_NAME}_LINE_PER_WAY   64
#define ${CMCC_INSTANCE_NAME}_LINE_SIZE      16
#define ${CMCC_INSTANCE_NAME}_WAY_SIZE       1024

/***************************** CMCC API *******************************/
void ${CMCC_INSTANCE_NAME}_Disable (void );
<#if CMCC_CCFG_EXISTS>
void ${CMCC_INSTANCE_NAME}_EnableDCache (void );
void ${CMCC_INSTANCE_NAME}_DisableDCache (void );
void ${CMCC_INSTANCE_NAME}_EnableICache (void );
void ${CMCC_INSTANCE_NAME}_DisableICache (void );
</#if>

void ${CMCC_INSTANCE_NAME}_InvalidateAll (void );

#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

#endif