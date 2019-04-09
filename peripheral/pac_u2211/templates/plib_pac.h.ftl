/*******************************************************************************
  Peripheral Access Controller(PAC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PAC_INSTANCE_NAME?lower_case}.h

  Summary
    PAC PLIB Header File.

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

#ifndef PLIB_${PAC_INSTANCE_NAME}_H  // Guards against multiple inclusion
#define PLIB_${PAC_INSTANCE_NAME}_H

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
    /* Clear the peripheral write control protection */
    PAC_PROTECTION_CLEAR,

    /* Set the peripheral write control protection */
    PAC_PROTECTION_SET,

} PAC_PROTECTION;

typedef enum
{
<#list 0..PAC_PERI_COUNT as i>
    <#assign PAC_PERI_NAME = "PAC_" + i + "_PERI_NAME">
        <#if .vars[PAC_PERI_NAME]?has_content>
    <#lt>    /* Instance Id for Peripheral ${.vars[PAC_PERI_NAME]} */
    <#lt>    PAC_PERIPHERAL_${.vars[PAC_PERI_NAME]} = ID_${.vars[PAC_PERI_NAME]},

        </#if>
</#list>
    PAC_PERIPHERAL_NONE = -1

} PAC_PERIPHERAL;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

bool ${PAC_INSTANCE_NAME}_PeripheralIsProtected( PAC_PERIPHERAL peripheral );

void ${PAC_INSTANCE_NAME}_PeripheralProtectSetup( PAC_PERIPHERAL peripheral, PAC_PROTECTION operation );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_${PAC_INSTANCE_NAME}_H */