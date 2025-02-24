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
 * @brief    Initializes the OPA${OPAMP_INSTANCE} module
 * @details  This function initializes the OPA${OPAMP_INSTANCE} module, setting it up for operation according to the predefined configuration.
 * @pre      This function should be called before any other OPA${OPAMP_INSTANCE} functions are used.
 * @param    None
 * @note     This function must be called only once and before any other OPA${OPAMP_INSTANCE} function is called.
 * @remarks  Ensure that the OPA${OPAMP_INSTANCE} module is properly configured before calling this function.
 * @return   None
 * 
 */
void OPA${OPAMP_INSTANCE}_Initialize (void);

/**
 * @brief    Deinitializes the OPA${OPAMP_INSTANCE} module
 * @details  This function deinitializes the OPA${OPAMP_INSTANCE} module, resetting it to its default state and disabling its operation.
 * @pre      This function should be called to properly shut down the OPA${OPAMP_INSTANCE} module before system power-down or reconfiguration.
 * @param    None
 * @note     This function should be called to release any resources allocated by the OPA${OPAMP_INSTANCE} module.
 * @remarks  Ensure that any necessary cleanup or state saving is performed before calling this function.
 * @return   None
 * 
 */
void OPA${OPAMP_INSTANCE}_Deinitialize(void);

/**
 * @brief    This inline function enables the OPA${OPAMP_INSTANCE} module
 * @details  This function sets the enable bit for the OPA${OPAMP_INSTANCE} module, allowing it to start operation.
 * @pre      The OPA${OPAMP_INSTANCE}_Initialize function should be called for the specified OPA${OPAMP_INSTANCE} driver instance before calling this function.
 * @param    None
 * @note     Ensure that the OPA${OPAMP_INSTANCE} module is properly initialized before enabling it.
 * @remarks  This function directly sets the enable bit in the control register of the OPA${OPAMP_INSTANCE} module.
 * @return   None
 * 
 */
inline static void OPA${OPAMP_INSTANCE}_Enable( void )
{
    AMP${OPAMP_INSTANCE}CON1bits.AMPEN = 1U; 
}

/**
 * @brief    This inline function disables the OPA${OPAMP_INSTANCE} module
 * @details  This function clears the enable bit for the OPA${OPAMP_INSTANCE} module, stopping its operation.
 * @pre      The OPA${OPAMP_INSTANCE} module should be enabled and operational before calling this function.
 * @param    None
 * @note     Ensure that any necessary cleanup or state saving is performed before disabling the OPA${OPAMP_INSTANCE} module.
 * @remarks  None
 * @return   None
 * 
 */
inline static void OPA${OPAMP_INSTANCE}_Disable( void )
{
    AMP${OPAMP_INSTANCE}CON1bits.AMPEN = 0U; 
}

/**
 * @brief    This inline function enables or disables unity gain for the OPA${OPAMP_INSTANCE} module
 * @details  This function sets or clears the unity gain enable bit for the OPA${OPAMP_INSTANCE} module based on the input parameter.
 * @param[in]  enable - If true, enables unity gain; if false, disables unity gain.
 * @note     Ensure that the OPA${OPAMP_INSTANCE} module is properly initialized before configuring unity gain.
 * @remarks  None
 * @return   None
 * 
 */
inline static void OPA${OPAMP_INSTANCE}_UnityGainEnable( bool enable )
{
    AMP${OPAMP_INSTANCE}CON1bits.UGE = (uint8_t)enable;     
}

/**
 * @brief    This inline function enables or disables High Power Mode for the OPA${OPAMP_INSTANCE} module
 * @details  This function sets or clears the High Power Mode enable bit for the OPA${OPAMP_INSTANCE} module based on the input parameter.
 * @param[in]  enable - If true, enables High Power Mode; if false, disables High Power Mode.
 * @note     Ensure that the OPA${OPAMP_INSTANCE} module is properly initialized before configuring High Power Mode.
 * @remarks  None
 * @return   None
 * 
 */
inline static void OPA${OPAMP_INSTANCE}_HighPowerModeEnable( bool enable )
{
    AMP${OPAMP_INSTANCE}CON1bits.HPEN = (uint8_t)enable;     
}

<#if OPA_IOMONITOR_AVAILABLE?? && OPA_IOMONITOR_AVAILABLE == true>

/**
 * @brief      This inline function enables or disables the output of the OPA${OPAMP_INSTANCE} module to the ADC
 * @details    This function sets or clears the output monitor enable bit for the OPA${OPAMP_INSTANCE} module based on the input parameter.
 * @param[in]  enable - If true, enables the output monitor; if false, disables the output monitor.
 * @note       Ensure that the OPA${OPAMP_INSTANCE} module is properly initialized before configuring the output monitor.
 * @remarks    None
 * @return     None
 * 
 */
inline static void OPA${OPAMP_INSTANCE}_OutputMonitorEnable( bool enable )
{
    AMP${OPAMP_INSTANCE}CON1bits.OMONEN = (uint8_t)enable;     
}
</#if>

/**
 * @brief      This inline function sets the differential input mode for the OPA${OPAMP_INSTANCE} module
 * @details    This function configures the differential input mode for the OPA${OPAMP_INSTANCE} module by setting the appropriate bits in the control register.
 * @param[in]  input - The selected differential input mode. This parameter should be of type OPA_DIFFERENTIAL_INPUT_MODE.
 * @note       Ensure that the OPA${OPAMP_INSTANCE} module is properly initialized before configuring the differential input mode.
 * @remarks    None
 * @return     None
 * 
 */
inline static void OPA${OPAMP_INSTANCE}_DifferentialInputModeSet(OPA_DIFFERENTIAL_INPUT_MODE input)
{
    AMP${OPAMP_INSTANCE}CON1bits.DIFFCON = (uint8_t)input;     
}

/**
 * @brief      This inline function enables/disables Enables output of OPA module to ADC
 * @param[in]  inputType   - selected differential input offset register type
 * @param[in]  unitVoltage - selected unit voltage
 * @return     None  
 * @Note       Unit voltage = trim step voltage 3 mV
 */
inline static void OPA${OPAMP_INSTANCE}_OffsetCorrection(OPA_OFFSET_INPUT_TYPE inputType, OPA_OUTPUT_VOLTAGE_OFFSET_CORRECTION unitVoltage)
{
     switch(inputType)
    {
        case OPA_PMOS_OFFSET_IN_HIGH_POWER_MODE:
            AMP${OPAMP_INSTANCE}CON2bits.POFFSETHP = (uint8_t)unitVoltage;
            break;
            
        case OPA_NMOS_OFFSET_IN_HIGH_POWER_MODE:
            AMP${OPAMP_INSTANCE}CON2bits.NOFFSETLP = (uint8_t)unitVoltage;
            break;
            
        case OPA_PMOS_OFFSET_IN_LOW_POWER_MODE:
            AMP${OPAMP_INSTANCE}CON2bits.POFFSETHP  = (uint8_t)unitVoltage;
            break;
            
        case OPA_NMOS_OFFSET_IN_LOW_POWER_MODE:
            AMP${OPAMP_INSTANCE}CON2bits.NOFFSETLP  = (uint8_t)unitVoltage;
            break;
            
        default:
            /*Do Nothing*/
            break;
    }
}


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
#endif
// DOM-IGNORE-END