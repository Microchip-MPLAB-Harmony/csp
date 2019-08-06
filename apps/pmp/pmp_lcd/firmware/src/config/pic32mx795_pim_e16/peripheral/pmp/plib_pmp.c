/*******************************************************************************
  Parallel Master Port(PMP) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_pmp.c

  Summary
    PMP PLIB Implementation File.

  Description
    This file defines the interface to the PMP peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_pmp.h"

// *****************************************************************************
// *****************************************************************************
// Section: PMP Interface Routines
// *****************************************************************************
// *****************************************************************************

void PMP_Initialize( void )
{
    /* Stop PMP module and clear control register */
    PMCONCLR = _PMCON_ON_MASK;

    /* Configure PMP operation mode */
    PMMODEbits.MODE = 0x2;


    PMCONSET = _PMCON_PTRDEN_MASK;

    PMCONbits.RDSP = 0x1;

    PMCONSET = _PMCON_PTWREN_MASK;

    PMCONbits.WRSP = 0x1;

    PMMODEbits.WAITB = 0x3;

    PMMODEbits.WAITM = 0xf;

    PMMODEbits.WAITE = 0x3;

    /* Configure chip select function */
    PMCONbits.CSF = 0x0;

    PMCONbits.CS1P = 0x0;

    PMCONbits.CS2P = 0x0;

    /* Enable PMP module */
    PMCONSET = _PMCON_ON_MASK;
}

void PMP_AddressSet( uint32_t address )
{
    PMADDR = address;
}

uint32_t PMP_AddressGet( void )
{
    return PMADDR;
}

void PMP_MasterSend( uint32_t data )
{
    PMDIN = data;
}

uint32_t PMP_MasterReceive( void )
{
    return PMDIN;
}

bool PMP_PortIsBusy( void )
{
    return (bool) (PMMODE & _PMMODE_BUSY_MASK);
}

void PMP_AddressPortEnable( uint32_t portfunctions )
{
    PMAENSET = (((uint32_t)(portfunctions)) << (_PMAEN_PTEN_POSITION)) & _PMAEN_PTEN_MASK;
}

void PMP_AddressPortDisable( uint32_t portfunctions )
{
    PMAENCLR = (((uint32_t)(portfunctions)) << (_PMAEN_PTEN_POSITION)) & _PMAEN_PTEN_MASK;
}
