/*******************************************************************************
  Resets (RCON) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_rcon.h

  Summary
    RCON PLIB Header File.

  Description
    This file defines the interface to the RCON peripheral library.
    This library provides access to and control of the associated Resets.

  Remarks:
    None.

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

#ifndef PLIB_RCON_H      // Guards against multiple inclusion
#define PLIB_RCON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdbool.h>
#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

typedef enum
{
    RCON_RESET_CAUSE_POR = _RCON_POR_MASK,

    RCON_RESET_CAUSE_BOR = _RCON_BOR_MASK,

    RCON_RESET_CAUSE_IDLE = _RCON_IDLE_MASK,

    RCON_RESET_CAUSE_SLEEP = _RCON_SLEEP_MASK,

    RCON_RESET_CAUSE_WDTO = _RCON_WDTO_MASK,

    RCON_RESET_CAUSE_SWR = _RCON_SWR_MASK,

    RCON_RESET_CAUSE_EXTR = _RCON_EXTR_MASK,

    RCON_RESET_CAUSE_VREGS = _RCON_VREGS_MASK,

    RCON_RESET_CAUSE_CMR = _RCON_CMR_MASK,

    RCON_RESET_CAUSE_HVDR = _RCON_HVDR_MASK,

} RCON_RESET_CAUSE;

// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

RCON_RESET_CAUSE RCON_ResetCauseGet( void );

void RCON_ResetCauseClear( RCON_RESET_CAUSE cause );

void RCON_SoftwareReset( void );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_RCON_H */
