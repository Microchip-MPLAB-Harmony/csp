/**
 * OPAMP Generated PLIB Types Header File
 * 
 * @file      plib_opa_common.h          
 *            
 * @brief     Operational Amplifier PLIB using dsPIC MCUs
 *
 * @skipline  Harmony Chip support Package Version  {core.libVersion}
 *            
 * @skipline  Device : {core.deviceName}
*/


//{core.disclaimer}

#ifndef PLIB_OPA_COMMON_H
#define PLIB_OPA_COMMON_H

/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif

typedef enum
{ 
    OPA_DIFFERENTIAL_INPUT_NMOS_PMOS_PAIR   = 0,    /**< Use both NMOS and PMOS differential input pair */
    OPA_DIFFERENTIAL_INPUT_NMOS_INPUT_PAIR  = 1,    /**< Turn NMOS differntial input pair ON and turn PMOS differential input pair off */
    OPA_DIFFERENTIAL_INPUT_PMOS_INPUT_PAIR  = 2,    /**< Turn PMOS differntial input pair ON and turn NMOS differential input pair off */
    OPA_DIFFERENTIAL_INPUT_NONE             = 3     /**< No differential input pair selected */

}  OPA_DIFFERENTIAL_INPUT_MODE; 

typedef enum
{
    OPA_PMOS_OFFSET_IN_HIGH_POWER_MODE,     /**< Offset Correction for PMOS Differential Input Pair (High-Power mode) */
    OPA_NMOS_OFFSET_IN_HIGH_POWER_MODE,     /**< Offset Correction for NMOS Differential Input Pair (High-Power mode) */
    OPA_PMOS_OFFSET_IN_LOW_POWER_MODE,      /**< Offset Correction for PMOS Differential Input Pair (Low-Power mode) */
    OPA_NMOS_OFFSET_IN_LOW_POWER_MODE       /**< Offset Correction for NMOS Differential Input Pair (Low-Power mode) */

} OPA_OFFSET_INPUT_TYPE;


typedef enum
{

   ${OFFSET_CORRECTION}

} OPA_OUTPUT_VOLTAGE_OFFSET_CORRECTION;

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif

#endif // PLIB_OPA_COMMON_H