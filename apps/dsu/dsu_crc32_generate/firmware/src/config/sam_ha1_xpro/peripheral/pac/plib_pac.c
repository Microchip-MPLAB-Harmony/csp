/*******************************************************************************
  Peripheral Access Controller (PAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_pac.c

  Summary
    Source for PAC peripheral library interface Implementation.

  Description
    This file defines the interface to the PAC peripheral library. This
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_pac.h"

// *****************************************************************************
// *****************************************************************************
// Section: MACROS Definitions
// *****************************************************************************
// *****************************************************************************

#define PAC_INSTANCE_OFFSET        (0x1000000)

// *****************************************************************************
// *****************************************************************************
// Section: PAC Implementations
// *****************************************************************************
// *****************************************************************************

bool PAC_PeripheralIsProtected( PAC_PERIPHERAL peripheral )
{
    bool status = false;
    uint32_t pacAddress = PAC0_BASE_ADDRESS + (PAC_INSTANCE_OFFSET * (peripheral >> 5));
    uint32_t periMask = PAC_WPSET_WP_Pos << (peripheral & 0x1f);

    /* Check if peripheral is protected or not */
    if((((pac_registers_t *)pacAddress)->PAC_WPSET & periMask) == periMask)
    {
        status = true;
    }

    return status;
}

void PAC_PeripheralProtectSetup( PAC_PERIPHERAL peripheral, PAC_PROTECTION operation )
{
    uint32_t pacAddress = PAC0_BASE_ADDRESS + (PAC_INSTANCE_OFFSET * (peripheral >> 5));
    uint32_t periMask = PAC_WPSET_WP_Pos << (peripheral & 0x1f);

    if(operation == PAC_PROTECTION_SET)
    {
        /* Lock the Peripheral interface */
        ((pac_registers_t *)pacAddress)->PAC_WPSET = periMask;
    }
    else if(operation == PAC_PROTECTION_CLEAR)
    {
        /* Unlock the Peripheral interface */
        ((pac_registers_t *)pacAddress)->PAC_WPCLR = periMask;
    }
}
