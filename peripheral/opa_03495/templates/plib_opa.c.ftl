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
// Section: Included Files

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include "device.h"
#include "plib_${moduleName?lower_case}.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

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

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END