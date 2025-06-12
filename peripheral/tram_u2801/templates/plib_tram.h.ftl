/*******************************************************************************
  Interface definition of TRAM PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${TRAM_INSTANCE_NAME?lower_case}.h

  Summary:
    Interface definition of the TrustRam Plib (TRAM).

  Description:
    This file defines the interface for the TRAM Plib.
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

#ifndef ${TRAM_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define ${TRAM_INSTANCE_NAME}_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#ifdef __cplusplus // Provide C++ Compatibility
 extern "C" {
#endif


// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

/***************************** TRAM API *******************************/
void ${TRAM_INSTANCE_NAME}_Initialize( void );

bool ${TRAM_INSTANCE_NAME}_Enable(bool en);

bool ${TRAM_INSTANCE_NAME}_RAMSet(uint32_t ramIndex, uint32_t data);

bool ${TRAM_INSTANCE_NAME}_RAMGet(uint32_t ramIndex, uint32_t *data);

void ${TRAM_INSTANCE_NAME}_DataScrambleKeySet(uint32_t dsckey);

void ${TRAM_INSTANCE_NAME}_DataScrambleEnable(bool enable);

#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif 
