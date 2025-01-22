/*******************************************************************************
  Peripheral Access Controller (PAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PAC_INSTANCE_NAME?lower_case}.c

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
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

#include "plib_${PAC_INSTANCE_NAME?lower_case}.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

bool PAC_PeripheralIsProtected(PAC_PERIPHERAL peripheral)
{
    bool status = false;
    volatile uint32_t *PACCONx;
    uint32_t periMask;
    uint32_t lockBitMask;
    uint32_t writeEnableBitMask;
    uint32_t LockBit;
    uint32_t writeEnableBit;

    if (peripheral < 16U) 
    {
        PACCONx = (volatile uint32_t *)((uint32_t)&PACCON1);
        periMask = (uint32_t)peripheral;
    } 
    else 
    {
        PACCONx = (volatile uint32_t *)((uint32_t)&PACCON2);
        periMask = (uint32_t)peripheral - 16U; 
    }
    lockBitMask = periMask;        
    writeEnableBitMask = periMask + 16U; 
    
    LockBit = ((*PACCONx >> lockBitMask) & 0x1U);
    writeEnableBit = ((*PACCONx >> writeEnableBitMask) & 0x1U);
    
    if((LockBit == 1U) || (writeEnableBit == 0U))
    {
         status = true;
    }
    return status;
}

void PAC_PeripheralProtectSetup(PAC_PERIPHERAL peripheral, PAC_PROTECTION operation)
{
    volatile uint32_t *PACCONx;
    uint32_t periMask;
    uint32_t lockBitMask;
    uint32_t writeEnableBitMask;

    if (peripheral < 16U) 
    {
        PACCONx = (volatile uint32_t *)((uint32_t)&PACCON1);
        periMask = (uint32_t)peripheral;
    } 
    else 
    {
        PACCONx = (volatile uint32_t *)((uint32_t)&PACCON2);
        periMask = (uint32_t)peripheral - 16U; 
    }
    lockBitMask = periMask;        
    writeEnableBitMask = periMask + 16U; 

    switch (operation)
    {
        case PAC_PROTECTION_SET:
            *PACCONx &= ~(1U << writeEnableBitMask);
            break;

        case PAC_PROTECTION_SET_AND_LOCK:
            *PACCONx |= (1U << lockBitMask); 
            *PACCONx &= ~(1U << writeEnableBitMask); 
            break;

        case PAC_PROTECTION_CLEAR:
            *PACCONx |= (1U << writeEnableBitMask);
            break;

        default:
            break;
    }
}