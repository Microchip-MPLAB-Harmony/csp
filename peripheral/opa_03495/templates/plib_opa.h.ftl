/*******************************************************************************
  OPA PLIB

  Company
    Microchip Technology Inc.

  File Name
  plib_${moduleName?lower_case}.h

  Summary
    OPA PLIB Header File.

  Description
    This file defines the interface to the OPAMP peripheral library.
    This library provides access to and control of the associated OPAMP.

  Remarks:
    None.

*******************************************************************************/
#ifndef PLIB_${moduleName}_H
#define PLIB_${moduleName}_H

// *****************************************************************************
// Section: Included Files
// *****************************************************************************

#include <stdbool.h>
#include <stddef.h>
#include "device.h"
#include "plib_opa_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

/**
 * @ingroup  ${moduleName?lower_case}
 * @brief    Initializes the ${moduleName?lower_case} module
 * @param    none
 * @return   none  
 */
void OPA${OPAMP_INSTANCE}_Initialize (void);

/**
 * @ingroup  ${moduleName?lower_case}
 * @brief    Deinitializes the ${moduleName?lower_case} module
 * @param    none
 * @return   none  
 */
void OPA${OPAMP_INSTANCE}_Deinitialize(void);

/**
 * @ingroup  ${moduleName?lower_case}
 * @brief    This inline function enables OPA1 module
 * @pre      The OPA1_Initialize function should be called for the 
 *           specified OPA1 driver instance.
 * @param    none
 * @return   none  
 */
inline static void OPA${OPAMP_INSTANCE}_Enable( void )
{
    AMP${OPAMP_INSTANCE}CON1bits.AMPEN = 1U; 
}

/**
 * @ingroup  ${moduleName?lower_case}
 * @brief    This inline function disables OPA1 module
 * @param    none
 * @return   none  
 */
inline static void OPA${OPAMP_INSTANCE}_Disable( void )
{
    AMP${OPAMP_INSTANCE}CON1bits.AMPEN = 0U; 
}

/**
 * @brief      This inline function enables/disables unity gain of OPA module
 * @param[in]  enable - true, enables unity gain 
 * @param[in]  enable - false, disables unity gain  
 * @return     none  
 */
inline static void OPA${OPAMP_INSTANCE}_UnityGainEnable( bool enable )
{
    AMP${OPAMP_INSTANCE}CON1bits.UGE = enable;     
}

/**
 * @brief      This inline function enables/disables high power mode of OPA module
 * @param[in]  enable - true, enables High Power Mode
 * @param[in]  enable - false, disables High Power Mode 
 * @return     none  
 */
inline static void OPA${OPAMP_INSTANCE}_HighPowerModeEnable( bool enable )
{
    AMP${OPAMP_INSTANCE}CON1bits.HPEN = enable;     
}

<#if OPA_IOMONITOR_AVAILABLE?? && OPA_IOMONITOR_AVAILABLE == true>

/**
 * @brief      This inline function enables/disables positive input of OPA module to ADC
 * @param[in]  enable - true, enables input Monitor
 * @param[in]  enable - false, disables input Monitor 
 * @return     none  
 */
inline static void OPA${OPAMP_INSTANCE}_InputMonitorEnable( bool enable )
{
    AMP${OPAMP_INSTANCE}CON1bits.IMONEN = enable;     
}

/**
 * @brief      This inline function enables/disables Enables output of OPA module to ADC
 * @param[in]  enable - true, enables output Monitor
 * @param[in]  enable - false, disables output Monitor 
 * @return     none  
 */
inline static void OPA${OPAMP_INSTANCE}_OutputMonitorEnable( bool enable )
{
    AMP${OPAMP_INSTANCE}CON1bits.OMONEN = enable;     
}
</#if>

/**
 * @brief      This inline function enables/disables Enables output of OPA module to ADC
 * @param[in]  input - selected differential input mode
 * @return     none  
 */
inline static void OPA${OPAMP_INSTANCE}_DifferentialInputModeSet(OPA_DIFFERENTIAL_INPUT_MODE input)
{
    AMP${OPAMP_INSTANCE}CON1bits.DIFFCON = input;     
}

/**
 * @brief      This inline function enables/disables Enables output of OPA module to ADC
 * @param[in]  inputType   - selected differential input offset register type
 * @param[in]  unitVoltage - selected unit voltage
 * @return     none  
 * @Note       Unit voltage = trim step voltage 3 mV
 */
inline static void OPA${OPAMP_INSTANCE}_OffsetCorrection(OPA_OFFSET_INPUT_TYPE inputType, OPA_OUTPUT_VOLTAGE_OFFSET_CORRECTION unitVoltage)
{
     switch(inputType)
    {
        case OPA_PMOS_OFFSET_IN_HIGH_POWER_MODE:
            AMP${OPAMP_INSTANCE}CON2bits.POFFSETHP = unitVoltage;
            break;
            
        case OPA_NMOS_OFFSET_IN_HIGH_POWER_MODE:
            AMP${OPAMP_INSTANCE}CON2bits.NOFFSETLP = unitVoltage;
            break;
            
        case OPA_PMOS_OFFSET_IN_LOW_POWER_MODE:
            AMP${OPAMP_INSTANCE}CON2bits.POFFSETHP  = unitVoltage;
            break;
            
        case OPA_NMOS_OFFSET_IN_LOW_POWER_MODE:
            AMP${OPAMP_INSTANCE}CON2bits.NOFFSETLP  = unitVoltage;
            break;
            
        default:
            break;
    }
}


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
#endif
// DOM-IGNORE-END