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
// Section: Global Data
// *****************************************************************************
// *****************************************************************************



PAC_CALLBACK_OBJ pacCallbackObject;

// *****************************************************************************
// *****************************************************************************
// Section: PAC Interface Implementations
// *****************************************************************************
// *****************************************************************************

void PAC_Initialize( void )
{
    /* Enable PAC interrupt */
    PAC_REGS->PAC_INTENSET = PAC_INTENSET_ERR_Msk;

}

bool PAC_PeripheralIsProtected( PAC_PERIPHERAL peripheral )
{
    bool status = false;
    uint32_t *statusRegBaseAddr = (uint32_t*) &(PAC_REGS->PAC_STATUSA);

    /* Verify if the peripheral is protected or not */
    status = (bool)((*(statusRegBaseAddr + (peripheral / 32))) & (1 << (peripheral % 32)));

    return status;
}

void PAC_PeripheralProtectSetup( PAC_PERIPHERAL peripheral, PAC_PROTECTION operation )
{
    /* Set Peripheral Access Control */
    PAC_REGS->PAC_WRCTRL = PAC_WRCTRL_PERID(peripheral) | PAC_WRCTRL_KEY(operation);
}

void PAC_CallbackRegister( PAC_CALLBACK callback, uintptr_t context )
{
    pacCallbackObject.callback = callback;

    pacCallbackObject.context = context;
}

void PAC_InterruptHandler( void )
{
    if (pacCallbackObject.callback != NULL)
    {
        pacCallbackObject.callback(pacCallbackObject.context);
    }

    /* Clear all interrupt flags to remove active interrupt requests */
    PAC_REGS->PAC_INTFLAGAHB = PAC_INTFLAGAHB_Msk;
    PAC_REGS->PAC_INTFLAGA = PAC_INTFLAGA_Msk;
    PAC_REGS->PAC_INTFLAGB = PAC_INTFLAGB_Msk;
    PAC_REGS->PAC_INTFLAGC = PAC_INTFLAGC_Msk;
}
