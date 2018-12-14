/*******************************************************************************
  Position Decoder(${PDEC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PDEC_INSTANCE_NAME?lower_case}.h

  Summary
    ${PDEC_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the PDEC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_${PDEC_INSTANCE_NAME}_H      // Guards against multiple inclusion
#define PLIB_${PDEC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_pdec_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

#define ${PDEC_INSTANCE_NAME}_ANGULAR_COUNTER_BITS    ${PDEC_CTRLA_ANGULAR}U

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/

// *****************************************************************************
<#assign PDEC_INTERRUPT = false>
<#if PDEC_INTENSET_OVF || PDEC_INTENSET_VLC || PDEC_INTENSET_DIR || PDEC_INTENSET_MC_0 || PDEC_INTENSET_MC_1>
    <#assign PDEC_INTERRUPT = true>
</#if>
void ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}Initialize( void );

void ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}Start( void );

void ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}Stop( void );

int16_t ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}PositionGet( void );

<#if PDEC_INTERRUPT == true>
void ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}CallbackRegister( PDEC_${PDEC_CTRLA_MODE}_CALLBACK callback, uintptr_t context );
<#else>
PDEC_QDEC_STATUS ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}StatusGet(void);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${PDEC_INSTANCE_NAME}_H */
