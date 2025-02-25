/*******************************************************************************
  OPA Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${moduleName?lower_case}.c

  Summary:
    OPA Source File

  Description:
    None

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
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

// Section: Included Files

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include "device.h"
#include "plib_${moduleName?lower_case}.h"

// Section: ${OPAMP_INSTANCE} Implementation

void  OPA${OPAMP_INSTANCE}_Initialize (void)
{
  
    <#if HIGH_POWER_ENABLE == true>
    OPA${OPAMP_INSTANCE}_HighPowerModeEnable(true);
    </#if> 
    <#if UNITY_GAIN == true>
    OPA${OPAMP_INSTANCE}_UnityGainEnable(true);
    </#if> 
    <#if ENABLE_OPA == true>
    OPA${OPAMP_INSTANCE}_Enable();
    </#if>
  
}

void OPA${OPAMP_INSTANCE}_Deinitialize (void)
{
    OPA${OPAMP_INSTANCE}_Disable();

    AMP${OPAMP_INSTANCE}CON1 = ${CON1_REG_POR};
    AMP${OPAMP_INSTANCE}CON2 = ${CON2_REG_POR};
  
}