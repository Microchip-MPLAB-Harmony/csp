/*******************************************************************************
  Divide Square Root Accelerator (${DIVAS_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DIVAS_INSTANCE_NAME?lower_case}.h

  Summary:
    ${DIVAS_INSTANCE_NAME} PLIB Header File

  Description:
    This file defines the interface to the DIVAS peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

// DOM-IGNORE-BEGIN
#ifndef PLIB_${DIVAS_INSTANCE_NAME}_H
#define PLIB_${DIVAS_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#ifdef __cplusplus // Provide C++ Compatibility
extern "C"
{
#endif

// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
<#if DIVAS_DLZ == false>
void ${DIVAS_INSTANCE_NAME}_Initialize(void);

</#if>
/* 32-bit Square Root */
uint32_t ${DIVAS_INSTANCE_NAME}_SquareRoot (uint32_t number);
<#if DIVAS_DIV_OVERLOAD == false>

/* 32-bit Signed division, return quotient */
int32_t ${DIVAS_INSTANCE_NAME}_DivSigned(int32_t numerator, int32_t denominator);

/* 32-bit Unsigned division, return quotient */
uint32_t ${DIVAS_INSTANCE_NAME}_DivUnsigned(uint32_t numerator, uint32_t denominator);

/* 32-bit Signed division, return quotient and remainder as 64-bit number */
uint64_t ${DIVAS_INSTANCE_NAME}_DivmodSigned(int32_t numerator, int32_t denominator);

/* 32-bit Unsigned division, return quotient and remainder as 64-bit result */
uint64_t ${DIVAS_INSTANCE_NAME}_DivmodUnsigned(uint32_t numerator, uint32_t denominator);
</#if>
#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif /* PLIB_${DIVAS_INSTANCE_NAME}_H */
