/*******************************************************************************
  Random Number Generator (${RNG_INSTANCE_NAME}) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RNG_INSTANCE_NAME}.h

  Summary:
    ${RNG_INSTANCE_NAME} PLIB Header File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${RNG_INSTANCE_NAME}_H
#define PLIB_${RNG_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END


// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

/*************************** ${RNG_INSTANCE_NAME} API ******************************************/
// *****************************************************************************

void ${RNG_INSTANCE_NAME}_Initialize (void);

/* TRNG functions */
void ${RNG_INSTANCE_NAME}_TrngEnable(void);
void ${RNG_INSTANCE_NAME}_TrngDisable(void);
void ${RNG_INSTANCE_NAME}_WaitForTrngCnt(void);
uint32_t ${RNG_INSTANCE_NAME}_Seed1Get (void);
uint32_t ${RNG_INSTANCE_NAME}_Seed2Get (void);

/* PRNG functions */
void ${RNG_INSTANCE_NAME}_PrngEnable(void);
void ${RNG_INSTANCE_NAME}_PrngDisable(void);
void ${RNG_INSTANCE_NAME}_LoadSet (void);
bool ${RNG_INSTANCE_NAME}_LoadGet (void);
void ${RNG_INSTANCE_NAME}_Poly1Set (uint32_t poly);
void ${RNG_INSTANCE_NAME}_Poly2Set (uint32_t poly);
uint32_t ${RNG_INSTANCE_NAME}_Poly1Get (void);
uint32_t ${RNG_INSTANCE_NAME}_Poly2Get (void);
void ${RNG_INSTANCE_NAME}_NumGen1Set (uint32_t numgen);
void ${RNG_INSTANCE_NAME}_NumGen2Set (uint32_t poly);
uint32_t ${RNG_INSTANCE_NAME}_NumGen1Get (void);
uint32_t ${RNG_INSTANCE_NAME}_NumGen2Get (void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // PLIB_${RNG_INSTANCE_NAME}_H
