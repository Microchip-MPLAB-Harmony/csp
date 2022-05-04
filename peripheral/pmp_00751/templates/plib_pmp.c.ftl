/*******************************************************************************
  Parallel Master Port(${PMP_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PMP_INSTANCE_NAME?lower_case}.c

  Summary
    ${PMP_INSTANCE_NAME} PLIB Implementation File.

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
#include "plib_${PMP_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${PMP_INSTANCE_NAME} Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${PMP_INSTANCE_NAME}_Initialize( void )
{
    /* Stop PMP module and clear control register */
    PMCONCLR = _PMCON_ON_MASK;

    /* Configure PMP operation mode */
    PMMODEbits.MODE = ${PMMODE_MODE};

<#if PMMODE_MODE16?has_content>
    /* 8/16 - bit data transfer */
    PMMODEbits.MODE16 = ${PMMODE_MODE16};
</#if>

<#if PMMODE_READ_STROBE == true>
    PMCONSET = _PMCON_PTRDEN_MASK;

    PMCONbits.RDSP = ${PMCON_RDSP};
</#if>

<#if PMMODE_WRITE_STROBE == true>
    PMCONSET = _PMCON_PTWREN_MASK;

    PMCONbits.WRSP = ${PMCON_WRSP};
</#if>

    PMMODEbits.WAITB = ${PMMODE_WAITB};

    PMMODEbits.WAITM = ${PMMODE_WAITM};

    PMMODEbits.WAITE = ${PMMODE_WAITE};

    /* Configure chip select function */
    PMCONbits.CSF = ${PMCON_CSF};

    PMCONbits.CS1P = ${PMCON_CS1P};

<#if PMCON_CS2P??>
    PMCONbits.CS2P = ${PMCON_CS2P};

</#if>
<#if PMMODE_ADDRESSPORT_ENABLE == true>
    PMADDR = 0;

    PMAENSET = (((uint32_t)((0xFFFF >> (16 - ${PMMODE_ADDRESS_PORT_BITWIDTH})))) << (_PMAEN_PTEN_POSITION)) & _PMAEN_PTEN_MASK;

    /* Auto increment mode enable */
    PMMODEbits.INCM = ${PMMODE_INCM};

</#if>
    /* Enable PMP module */
    PMCONSET = _PMCON_ON_MASK;
}

void ${PMP_INSTANCE_NAME}_AddressSet( uint32_t address )
{
    PMADDR = address;
}

uint32_t ${PMP_INSTANCE_NAME}_AddressGet( void )
{
    return PMADDR;
}

void ${PMP_INSTANCE_NAME}_MasterSend( uint32_t data )
{
    PMDIN = data;
}

uint32_t ${PMP_INSTANCE_NAME}_MasterReceive( void )
{
    return PMDIN;
}

bool ${PMP_INSTANCE_NAME}_PortIsBusy( void )
{
    return ((PMMODE & _PMMODE_BUSY_MASK) != 0U);
}

void ${PMP_INSTANCE_NAME}_AddressPortEnable( uint32_t portfunctions )
{
    PMAENSET = (((uint32_t)(portfunctions)) << (_PMAEN_PTEN_POSITION)) & _PMAEN_PTEN_MASK;
}

void ${PMP_INSTANCE_NAME}_AddressPortDisable( uint32_t portfunctions )
{
    PMAENCLR = ((((uint32_t)(portfunctions)) << (_PMAEN_PTEN_POSITION)) & _PMAEN_PTEN_MASK);
}
