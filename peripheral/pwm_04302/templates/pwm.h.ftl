<#assign functionHeaderExample = false>
<#assign generateDoxygen = true>
/*******************************************************************************
  ${moduleNameUpperCase} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${fileNameLowerCase}.h

  Summary:
    ${moduleNameUpperCase} PLIB Header File

  Description:
    This file has prototype of all the interfaces provided for particular
    ${moduleNameUpperCase} peripheral.

*******************************************************************************/

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

#ifndef ${moduleNameUpperCase}_H
#define ${moduleNameUpperCase}_H

// Section: Included Files

#include "device.h"
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>

// *****************************************************************************
// *****************************************************************************
// Section: Enum Declarations
// *****************************************************************************
// *****************************************************************************

<#if generateDoxygen>
/**
 @brief    Defines the PWM generators that are selected from the MCC Harmony User 
           Interface for the PWM output controls.
 @details  These macro's represents the different PWM generators available for configuration 
           through the MCC Harmony User Interface. These values correspond to specific hardware PWM generators 
           that can be used for generating PWM outputs. The generated list in the help documentation may not represent 
           all the generators but is based on the user's configuration in the MCC Harmony tool.
           The user should configure the PWM generators according to their application requirements.
           The generated enum list may vary depending on the specific PWM Generators are enabled in User Interface.
*/
</#if>
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
            <#lt>#define    PWM_GENERATOR_${i}      ${i}U      /**< PWM generator ${i}*/
    </#if>
</#list>

typedef uint32_t ${moduleNameUpperCase}_GENERATOR;

<#if generateDoxygen>
/**
 @brief    Defines the PWM generator interrupts that are available for the module to use.
 @details  Defines the PWM generator interrupts that are available for the module to use.
*/
</#if>
#define    PWM_GENERATOR_INTERRUPT_FAULT           1U      /**< PWM Generator Fault Interrupt */ 
#define    PWM_GENERATOR_INTERRUPT_CURRENT_LIMIT   2U      /**< PWM Generator Current Limit Interrupt */
#define    PWM_GENERATOR_INTERRUPT_FEED_FORWARD    3U      /**< PWM Generator Feed Forward Interrupt */
#define    PWM_GENERATOR_INTERRUPT_SYNC            4U      /**< PWM Generator Sync Interrupt */

typedef uint32_t ${moduleNameUpperCase}_GENERATOR_INTERRUPT;

<#if generateDoxygen>
/**
 @brief    Defines the ${moduleNameUpperCase} generator Trigger Compare registers 
           that are available for the module to use.
 @details  These macro's defines the registers used to trigger compare events for the PWM generator. 
           The trigger compare registers (A, B, C) are used to set the conditions for when the PWM generator should update or trigger an event.
           These registers are essential for controlling the timing and synchronization of the PWM signals and the system's response to those signals.
*/
</#if>
#define    PWM_TRIGGER_COMPARE_A    1U         /**< PWM Trigger Compare A Register */
#define    PWM_TRIGGER_COMPARE_B    2U         /**< PWM Trigger Compare B Register */
#define    PWM_TRIGGER_COMPARE_C    3U         /**< PWM Trigger Compare C Register */

typedef uint32_t ${moduleNameUpperCase}_TRIGGER_COMPARE;

<#if generateDoxygen>
/**
 @brief    Defines the PWM generator operating modes that are available.
 @details  These macro's specifies various operating modes for the PWM generator. 
           These modes control how the PWM signal is generated, including independent edge modes, 
           center-aligned modes, and dual-edge modes. 
           Each mode provides different timing characteristics for the PWM signal, 
           which may be useful for applications requiring precise control of the signal's rise, fall, or center alignment.
           The modes available in this enum can be selected based on the specific requirements of the application.
*/
</#if>
#define    PWM_MODE_INDEPENDENT_EDGE                          0x0U       /**< Independent Edge mode*/
#define    PWM_MODE_VARIABLE_PHASE                            0x1U       /**< Variable Phase mode*/
#define    PWM_MODE_INDEPENDENT_EDGE_DUAL_OUTPUT              0x2U       /**< Independent Edge, dual output mode*/
#define    PWM_MODE_CENTER_ALIGNED                            0x4U       /**< Center-Aligned mode*/
#define    PWM_MODE_DOUBLE_UPDATE_CENTER_ALIGNED              0x5U       /**< Double-Update Center-Aligned mode*/
#define    PWM_MODE_DUALEDGE_CTR_ALIGNED_ONE_UPDATE_CYCLE     0x6U       /**< Dual Edge Center-Aligned;one update/cycle mode*/
#define    PWM_MODE_DUALEDGE_CTR_ALIGNED_TWO_UPDATES_CYCLE    0x7U       /**< Dual Edge Center-Aligned;two updates/cycle mode*/

typedef uint32_t ${moduleNameUpperCase}_MODES;

<#if generateDoxygen>
/**
 @brief    Defines the PWM generator output modes that are available.
 @details  These macro's defines the different output configurations for the PWM generator. 
           The output modes control whether the PWM signals are generated in complementary, independent, or push-pull mode. 
           These output modes are essential for driving external devices or circuits, and the choice of output mode 
           depends on the hardware and the requirements of the system being controlled.
*/
</#if>
#define    COMPLEMENTARY_OUTPUT_MODE   0x0U         /**< Complementary mode output mode*/
#define    INDEPENDENT_OUTPUT_MODE     0x1U         /**< Independent mode output mode*/
#define    PUSH_PULL_OUTPUT_MODE       0x2U         /**< Push-Pull mode output mode*/

typedef uint32_t ${moduleNameUpperCase}_OUTPUT_MODES;

<#if generateDoxygen>
/**    
 @brief    Defines the PWM generator Master or Independent source selection.
 @details  These macro's allows the user to select whether the PWM generator will operate in a master or independent source. 
*/
</#if>
#define    PWM_SOURCE_SELECT_INDEPENDENT   0U         /**< PWM select Independent PWM as source */
#define    PWM_SOURCE_SELECT_MASTER        1U         /**< PWM select Master as source */

typedef uint32_t ${moduleNameUpperCase}_SOURCE_SELECT;

<#if generateDoxygen>
/**
 * @brief    Callback function type for  PWM generator End of Conversion (EOC) event.
 * 
 * @details  This typedef defines a function pointer type for a callback function that is
 *           used to handle PWM generator End of Conversion (EOC) event. The callback function 
 *           is called when an Individual PWM Generator EOC event.
 * 
 * @param[in]    pin     - The external interrupt pin that triggered the callback.
 * @param[in]    context - A user-defined context or data passed to the callback function.
 * 
 * @note     The `pin` parameter indicates which external interrupt pin triggered the
 *           callback, and the `context` parameter allows for user-specific data to 
 *           be passed to the callback function.
 * 
 * @b Example:
 * @code
 * void my_callback(${moduleNameUpperCase}_GENERATOR genNum, uintptr_t context) {
 *      
 * }
 * 
 * PWM_GEN_EOC_EVENT_CALLBACK callback = my_callback;
 * @endcode
 */
</#if>
typedef  void (*PWM_GEN_EOC_EVENT_CALLBACK) (${moduleNameUpperCase}_GENERATOR genNum, uintptr_t context);

<#if generateDoxygen>
/**
 @struct   EXT_INT_PIN_CALLBACK_OBJ
 @brief    This structure holds the callback and context information for handling
           events on a specified PWM Generator.
*/
</#if>
typedef struct
{
    PWM_GEN_EOC_EVENT_CALLBACK            callback;
    
    uintptr_t                                   context;
    
}PWM_GEN_EOC_EVENT_CALLBACK_OBJ;

// *****************************************************************************
// *****************************************************************************
// Section: ${moduleNameUpperCase} Peripheral APIs
// *****************************************************************************
// *****************************************************************************

<#if generateDoxygen>
/**
 * @brief    Initializes PWM Peripheral with the given configuration.
 * @details  This function configures the PWM peripheral using predefined initialization parameters.
 * @param    none
 * @return   none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t masterPeriod,masterDutyCycle,masterPhase;
 *    masterPeriod = 0xFFFF;
 *    masterDutyCycle = 0xFF;
 *    masterPhase = 0xF;
 *    ${moduleNameUpperCase}_Initialize();
 * 
 *    ${moduleNameUpperCase}_GeneratorDisable();
 *    ${moduleNameUpperCase}_MasterPeriodSet(masterPeriod);
 *    ${moduleNameUpperCase}_MasterDutyCycleSet(masterDutyCycle);
 *    ${moduleNameUpperCase}_MasterPhaseSet(masterPhase);
 * 
 *    ${moduleNameUpperCase}_GeneratorEnable(${moduleNameUpperCase}_GENERATOR_1);
 * @endcode
    </#if>
 * @remarks  none
 */
</#if>
void ${moduleNameUpperCase}_Initialize(void);

<#if generateDoxygen>
/**
 * @brief    Deinitializes the PWM to its Power-On Reset (POR) state.
 * @details  This function resets the PWM module, setting it back to its POR values. Any configuration
 *           made previously will be lost, and the PWM will be in a state similar to after power-up.
 * @param    none
 * @return   none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *        ${moduleNameUpperCase}_Deinitialize();
 * @endcode
    </#if>
 * @remarks  none
 */
 </#if>
void ${moduleNameUpperCase}_Deinitialize(void);

<#if generatorsInUse == true>
<#if generateDoxygen>
/**
 * @brief      Enables the specific PWM generator.
 * @details    This function activates a PWM generator specified by the argument `genNum`, allowing it to start 
 *             generating PWM signals.
 * @param[in]  genNum - PWM generator number  
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_GeneratorEnable(${moduleNameUpperCase}_GENERATOR_1);
 * @endcode
    </#if>
 * @remarks  none
 */
</#if>
inline static void ${moduleNameUpperCase}_GeneratorEnable(${moduleNameUpperCase}_GENERATOR genNum)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}CONbits.ON = 1U;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }     
}

<#if generateDoxygen>
/**
 * @brief      Disables the specific PWM generator.
 * @details    This function disables the specified PWM generator, stopping it from generating PWM signals.
 * @param[in]  genNum - PWM generator number
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_GeneratorDisable(${moduleNameUpperCase}_GENERATOR_1);
 * @endcode
    </#if>
 * @remarks  none
 */
</#if>
inline static void ${moduleNameUpperCase}_GeneratorDisable(${moduleNameUpperCase}_GENERATOR genNum)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}CONbits.ON = 0U;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }     
}

<#if generateDoxygen>
/**
 * @brief      Sets the operating mode for a specific PWM generator.
 * @details    This function sets the operating mode of the PWM generator selected by the argument `genNum`.
 *             The operating mode determines the behavior of the PWM generator (e.g., edge-aligned or center-aligned).
 * @param[in]  genNum - PWM generator number
 * @param[in]  mode - PWM operating mode
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_ModeSet(${moduleNameUpperCase}_GENERATOR_1, CENTER_ALIGNED);
 * @endcode
    </#if>
 * @remarks  none
 */
</#if>
inline static void ${moduleNameUpperCase}_ModeSet(${moduleNameUpperCase}_GENERATOR genNum, ${moduleNameUpperCase}_MODES mode)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}CONbits.MODSEL = (uint8_t)mode; 
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }     
}

<#if generateDoxygen>
/**
 * @brief      Configures the output mode of a specific PWM generator.
 * @details    This function allows setting the output mode of the PWM signal (e.g., Independent Edge, push-pull, etc.)
 *             for a specific generator. The output mode determines the type of PWM waveform generated.
 * @param[in]  genNum - PWM generator number
 * @param[in]  outputMode - PWM output mode
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_OutputModeSet(${moduleNameUpperCase}_GENERATOR_1, COMPLEMENTARY_OUTPUT_MODE);
 * @endcode
    </#if>
 * @remarks  none
 */
</#if>
inline static void ${moduleNameUpperCase}_OutputModeSet(${moduleNameUpperCase}_GENERATOR genNum, ${moduleNameUpperCase}_OUTPUT_MODES outputMode)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}IOCONbits.PMOD = (uint8_t)outputMode; 
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }     
}

<#if generateDoxygen>
/**
 * @brief    Enables all PWM generators.
 * @details  This function activates all PWM generators in the module, allowing them to start generating PWM signals.
 *           It is useful when enabling the entire module for the first time or after a reset.
 * @param    none
 * @return   none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_Enable();
 * @endcode
    </#if>
 * @remarks  none
 */
</#if>
inline static void ${moduleNameUpperCase}_Enable(void)
{
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
    PG${i}CONbits.ON = 1U;
    </#if>
</#list>
}

<#if generateDoxygen>
/**
 * @brief    Disables all PWM generators.
 * @details  This function deactivates all PWM generators in the module, stopping them from generating PWM signals.
 *           The generators can be re-enabled individually or as a whole.
 * @param    none
 * @return   none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_Disable();
 * @endcode
    </#if>
 * @remarks  none
 */
</#if>
inline static void ${moduleNameUpperCase}_Disable(void)
{
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
    PG${i}CONbits.ON = 0U;
    </#if>
</#list>
}

<#if generateDoxygen>
/**
 * @brief      Sets the period value for the Master Time Base generator.
 * @details    This function allows setting the period for the Master Time Base generator, which controls the overall 
 *             timing of the PWM module.
 * @param[in]  masterPeriod - Period value in count
 * @return     none  
 * @Note       Refer datasheet for valid size of data bits
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t masterPeriod;
 *    masterPeriod = 0xFF;
 *    
 *    ${moduleNameUpperCase}_MasterPeriodSet(masterPeriod);
 * @endcode
    </#if>
 * @remarks  none
 */
</#if>
inline static void ${moduleNameUpperCase}_MasterPeriodSet(uint32_t masterPeriod)
{
    <#if masterHighResolutionModeEnabled == true>
    ${masterPeriodReg} = masterPeriod & 0x000FFFFFUL;
    <#else>
    ${masterPeriodReg} = masterPeriod & 0x000FFFF0UL;
    </#if>
}

<#if generateDoxygen>
/**
 * @brief      Sets the PWM master duty cycle register.
 * @details    This function sets the duty cycle for the Master Time Base generator, which determines the width 
 *             of the PWM signal relative to the period.
 * @param[in]  masterDutyCycle - Master Duty Cycle value
 * @return     none
 * @Note       Refer datasheet for valid size of data bits
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t masterDutyCycle;
 *    masterDutyCycle = 0xFF;
 *    
 *    ${moduleNameUpperCase}_MasterDutyCycleSet(masterDutyCycle);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_MasterDutyCycleSet(uint32_t masterDutyCycle)
{
    <#if masterHighResolutionModeEnabled == true>
    ${masterDutyCycleReg} = masterDutyCycle & 0x000FFFFFUL;;
    <#else>
    ${masterDutyCycleReg} = masterDutyCycle & 0x000FFFF0UL;
    </#if>
}

<#if generateDoxygen>
/**
 * @brief      Sets the phase value for the Master Time Base generator.
 * @details    This function sets the phase for the Master Time Base generator, allowing you to shift the timing 
 *             of the PWM signals generated by the module.
 * @param[in]  masterPhase - Phase value in count
 * @return     none  
 * @Note       Refer datasheet for valid size of data bits
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t masterPhase;
 *    masterPhase = 0xFF;
 *    
 *    ${moduleNameUpperCase}_MasterPhaseSet(masterPhase);
 * @endcode
    </#if>
 * @remarks   none
 */
inline static void ${moduleNameUpperCase}_MasterPhaseSet(uint32_t masterPhase)
{
    <#if masterHighResolutionModeEnabled == true>
    ${masterPhaseReg} = masterPhase & 0x000FFFFFUL;;
    <#else>
    ${masterPhaseReg} = masterPhase & 0x000FFFF0UL;
    </#if>
}

<#if generateDoxygen>
/**
 * @brief      Sets the period for a specific PWM generator's Time Base.
 * @details    This function sets the period for a specific PWM generator, which controls the timing of the PWM signal 
 *             generated by the generator.
 * @param[in]  genNum - PWM generator number
 * @param[in]  period - PWM generator period value in count
 * @return     none  
 * @Note       Refer datasheet for valid size of data bits
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t period;
 *    
 *    period = 0xFFFF;
 *    ${moduleNameUpperCase}_PeriodSet(${moduleNameUpperCase}_GENERATOR_1, period);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_PeriodSet(${moduleNameUpperCase}_GENERATOR genNum,uint32_t period)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_HR_ENABLE = "PG" + i + "_HighResolutionEnable">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                <#if .vars[PWM_GEN_HR_ENABLE]?has_content && .vars[PWM_GEN_HR_ENABLE] == true>
                PG${i}PER = period & 0x000FFFFFUL;;
                <#else>
                PG${i}PER = period & 0x000FFFF0UL;
                </#if>            
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }     
}

<#if generateDoxygen>
/**
 * @brief      Sets the duty cycle for a specific PWM generator.
 * @details    This function sets the duty cycle for the selected PWM generator. The duty cycle controls the 
 *             width of the PWM pulse relative to the period.
 * @param[in]  genNum      - PWM generator number
 * @param[in]  dutyCycle   - PWM generator duty cycle
 * @return     none  
 * @Note       Refer datasheet for valid size of data bits
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t dutyCyle;
 *    
 *    dutyCycle = 0xFF;
 *    ${moduleNameUpperCase}_DutyCycleSet(${moduleNameUpperCase}_GENERATOR_1, dutyCycle);
 * @endcode
    </#if>
 * @remarks    none
 */
</#if>
inline static void ${moduleNameUpperCase}_DutyCycleSet(${moduleNameUpperCase}_GENERATOR genNum,uint32_t dutyCycle)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_HR_ENABLE = "PG" + i + "_HighResolutionEnable">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                <#if .vars[PWM_GEN_HR_ENABLE]?has_content && .vars[PWM_GEN_HR_ENABLE] == true>
                PG${i}DC = dutyCycle & 0x000FFFFFUL;;
                <#else>
                PG${i}DC = dutyCycle & 0x000FFFF0UL;
                </#if>            
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }     
}

<#if generateDoxygen>
/**
 * @brief      This inline function selects the PWM generator source for Phase.
 * @details    This function sets the source of the PWM phase for the specified generator. It allows you to configure
 *             the generator's phase either Master Phase or generator phase itself.
 * @param[in]  genNum - PWM generator number
 * @param[in]  source - PWM generator source select
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_PhaseSelect(${moduleNameUpperCase}_GENERATOR_1, PWM_MASTER);
 * @endcode
    </#if>
 * @remarks    none
 */
</#if>
inline static void ${moduleNameUpperCase}_PhaseSelect(${moduleNameUpperCase}_GENERATOR genNum,${moduleNameUpperCase}_SOURCE_SELECT source)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}CONbits.MPHSEL = (uint8_t)source;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function sets the phase value in count for the PWM generator specific Time Base.
 * @details    This function sets the phase for the specified PWM generator's time base, allowing you to adjust
 *             the signal's phase relative to other signals.
 * @param[in]  genNum - PWM generator number
 * @param[in]  phase - PWM generator phase value in count
 * @return     none  
 * @Note       Refer datasheet for valid size of data bits
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t phase;
 *    
 *    phase = 0xFFFF;
 *    ${moduleNameUpperCase}_PhaseSet(${moduleNameUpperCase}_GENERATOR_1, phase);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_PhaseSet(${moduleNameUpperCase}_GENERATOR genNum,uint32_t phase)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_HR_ENABLE = "PG" + i + "_HighResolutionEnable">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                <#if .vars[PWM_GEN_HR_ENABLE]?has_content && .vars[PWM_GEN_HR_ENABLE] == true>
                PG${i}PHASE = phase & 0x000FFFFFUL;;
                <#else>
                PG${i}PHASE = phase & 0x000FFFF0UL;
                </#if>            
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }     
}

<#if generateDoxygen>
/**
 * @brief      This inline function updates PWM override data bits with the requested value for a 
 *             specific PWM generator selected by the argument \ref PWM_GENERATOR.
 * @details    This function updates the override data of the PWM generator. Override data allows you to manipulate 
 *             the PWM signals for specific generator outputs.
 * @param[in]  genNum          -   PWM generator number
 * @param[in]  overrideData    -   Override data  
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t overrideData;
 *    overrideData = 0x01;
 *    
 *    ${moduleNameUpperCase}_OverrideDataSet(${moduleNameUpperCase}_GENERATOR_1, overrideData);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_OverrideDataSet(${moduleNameUpperCase}_GENERATOR genNum,uint16_t overrideData)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}IOCONbits.OVRDAT = (uint8_t)overrideData;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function updates PWM override high data bit with the requested value for a 
 *             specific PWM generator selected by the argument \ref PWM_GENERATOR.
 * @details    This function allows you to set the high override data bit for the specified PWM generator.
 * @param[in]  genNum              - PWM generator number
 * @param[in]  overrideDataHigh    - Override data  
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    bool overrideDataHigh;
 *    overrideDataHigh = true;
 *    
 *    ${moduleNameUpperCase}_OverrideDataHighSet(${moduleNameUpperCase}_GENERATOR_1, overrideDataHigh);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_OverrideDataHighSet(${moduleNameUpperCase}_GENERATOR genNum,bool overrideDataHigh)
{
    switch(genNum) 
    { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}IOCONbits.OVRDAT = (uint8_t)((PG${i}IOCONbits.OVRDAT & 0x1U) | ((uint8_t)overrideDataHigh << 0x1U));
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function updates PWM override low data bit with the requested value for a 
 *             specific PWM generator selected by the argument \ref PWM_GENERATOR.
 * @details    This function allows you to set the low override data bit for the specified PWM generator. 
 * @param[in]  genNum             - PWM generator number
 * @param[in]  overrideDataLow    - Override data  
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    bool overrideDataLow;
 *    overrideDataLow = true;
 *    
 *    ${moduleNameUpperCase}_OverrideDataLowSet(${moduleNameUpperCase}_GENERATOR_1, overrideDataLow);
 * @endcode
    </#if>
 * @remarks    none
 */
</#if>
inline static void ${moduleNameUpperCase}_OverrideDataLowSet(${moduleNameUpperCase}_GENERATOR genNum,bool overrideDataLow)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}IOCONbits.OVRDAT = (uint8_t)((PG${i}IOCONbits.OVRDAT & 0x2U) | overrideDataLow);
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function gets PWM override value for the PWM Generator selected by the 
 *             argument \ref PWM_GENERATOR.
 * @details    This function retrieves the override data for the specified PWM generator. The override data
 *             affects the behavior of the PWM signal, and this function allows you to read its current value.
 * @param[in]  genNum  -  PWM generator number
 * @return     Override data for the PWM Generator selected by the argument 
 *             ${moduleNameUpperCase}_GENERATOR.  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_GENERATOR genNum;
 *    uint16_t overrideData;
 *    
 *    genNum = ${moduleNameUpperCase}_GENERATOR_1;
 *    overrideData = ${moduleNameUpperCase}_OverrideDataGet(genNum, overrideData);
 * @endcode
    </#if>
 * @remarks    none
 */
</#if>
inline static uint16_t ${moduleNameUpperCase}_OverrideDataGet(${moduleNameUpperCase}_GENERATOR genNum)
{
    uint16_t overrideData = 0x0U;
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                overrideData = PG${i}IOCONbits.OVRDAT;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
    return overrideData;
}

<#if generateDoxygen>
/**
 * @brief      This inline function enables PWM override on PWMH output for specific PWM generator selected 
 *             by the argument \ref PWM_GENERATOR.
 * @details    This function enables the override functionality on the PWMxH output for the specified PWM generator.
 * @param[in]  genNum - PWM generator number  
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_OverrideHighEnable(${moduleNameUpperCase}_GENERATOR_1);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_OverrideHighEnable(${moduleNameUpperCase}_GENERATOR genNum)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}IOCONbits.OVRENH = 1U;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function enables PWM override on PWML output for specific PWM generator selected 
 *             by the argument \ref PWM_GENERATOR.
 * @details    This function enables the override functionality on the PWMxL output for the specified PWM generator.
 * @param[in]  genNum - PWM generator number
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_OverrideLowEnable(${moduleNameUpperCase}_GENERATOR_1);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_OverrideLowEnable(${moduleNameUpperCase}_GENERATOR genNum)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}IOCONbits.OVRENL = 1U;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function disables PWM override on PWMH output for specific PWM generator selected 
 *             by the argument \ref PWM_GENERATOR.
 * @details    This function disables the override functionality on the PWMxH output for the specified PWM generator.
 * @param[in]  genNum - PWM generator number
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_OverrideHighDisable(${moduleNameUpperCase}_GENERATOR_1);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_OverrideHighDisable(${moduleNameUpperCase}_GENERATOR genNum)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}IOCONbits.OVRENH = 0U;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function disables PWM override on PWML output for specific PWM generator selected 
 *             by the argument \ref PWM_GENERATOR.
 * @details    This function disables the override functionality on the PWMxL output for the specified PWM generator.
 * @param[in]  genNum - PWM generator number 
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_OverrideLowDisable(${moduleNameUpperCase}_GENERATOR_1);
 * @endcode
    </#if>
 * @remarks    none
 */
</#if>
inline static void ${moduleNameUpperCase}_OverrideLowDisable(${moduleNameUpperCase}_GENERATOR genNum)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}IOCONbits.OVRENL = 0U;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function updates PWM Deadtime low register with the requested value for a 
 *             specific PWM generator selected by the argument \ref PWM_GENERATOR.
 * @details    Deadtime insertion ensures that there is a gap between turning off one switch and turning on the other in 
 *             a complementary PWM generator configuration. This function sets the lower portion of the deadtime register.
 * @param[in]  genNum      - PWM generator number
 * @param[in]  deadtimeLow - Deadtime low value
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t deadtimeLow;
 *    deadtimeLow = 0x01;
 *    
 *    ${moduleNameUpperCase}_DeadTimeLowSet(${moduleNameUpperCase}_GENERATOR_1, deadtimeLow);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_DeadTimeLowSet(${moduleNameUpperCase}_GENERATOR genNum,uint16_t deadtimeLow)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}DT = (PG${i}DT & 0xFFFF0000UL) | (deadtimeLow & (uint16_t)0x7FFF);
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function updates PWM Deadtime high register with the requested value for a 
 *             specific PWM generator selected by the argument \ref PWM_GENERATOR.
 * @details    This function sets the upper portion of the deadtime register to control the delay between complementary
 *             switching signals for the specified PWM generator.
 * @param[in]  genNum          - PWM generator number
 * @param[in]  deadtimeHigh    - Deadtime high value
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t deadtimeHigh;
 *    deadtimeHigh = 0x01;
 *    
 *    ${moduleNameUpperCase}_DeadTimeHighSet(${moduleNameUpperCase}_GENERATOR_1, deadtimeHigh);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_DeadTimeHighSet(${moduleNameUpperCase}_GENERATOR genNum,uint16_t deadtimeHigh)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}DT = (((uint32_t)deadtimeHigh & (uint16_t)0x7FFF) << 16) | (uint16_t)PG${i}DT;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function updates PWM Deadtime low and high register with the requested value for a 
 *             specific PWM generator selected by the argument \ref PWM_GENERATOR.
 * @details    This function sets both the low and high portions of the deadtime register, which determines the 
 *             delay between complementary switching signals.
 * @param[in]  genNum          - PWM generator number
 * @param[in]  deadtimeHigh    - Deadtime value
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t deadtime;
 *    deadtime = 0x01;
 *    
 *    ${moduleNameUpperCase}_DeadTimeHighSet(${moduleNameUpperCase}_GENERATOR_1, deadtime);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_DeadTimeSet(${moduleNameUpperCase}_GENERATOR genNum,uint16_t deadtime)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                PG${i}DT = (((uint32_t)deadtime & (uint16_t)0x7FFF) << 16) | ((uint32_t)deadtime & (uint16_t)0x7FFF);
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function sets the PWM trigger compare value in count for the PWM Generator 
 *             selected by the argument \ref PWM_GENERATOR.
 * @details    This function sets the trigger compare value for the specified PWM generator, which determines the 
 *             timing for triggering other events or signals.
 * @param[in]  genNum          - PWM generator number
 * @param[in]  trigCompValue   - Trigger compare value in count
 * @return     none  
 * @Note       Refer datasheet for valid size of data bits
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_GENERATOR genNum;
 *    uint16_t trigCompValue;
 *    trigCompValue = 0x01;
 *    
 *    genNum = ${moduleNameUpperCase}_GENERATOR_1;
 *    ${moduleNameUpperCase}_TriggerCompareValueSet(genNum, trigCompValue);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_TriggerCompareValueSet(${moduleNameUpperCase}_GENERATOR genNum,uint32_t trigCompValue)
{
    switch(genNum) {
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_HR_ENABLE = "PG" + i + "_HighResolutionEnable">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                <#if .vars[PWM_GEN_HR_ENABLE]?has_content && .vars[PWM_GEN_HR_ENABLE] == true>
                PG${i}TRIGA = trigCompValue & 0x000FFFFFUL;
                <#else>
                PG${i}TRIGA = trigCompValue & 0x000FFFF0UL;  
                </#if>            
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function enables interrupt requests for the PWM Generator selected by the 
 *             argument \ref ${moduleNameUpperCase}_GENERATOR.   
 * @param[in]  genNum - PWM generator number
 * @param[in]  interrupt - PWM generator interrupt source
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    enum ${moduleNameUpperCase}_GENERATOR genNum;
 *    enum ${moduleNameUpperCase}_GENERATOR_INTERRUPT interrupt;
 *    
 *    genNum = ${moduleNameUpperCase}_GENERATOR_1;
 *    interrupt = ${moduleNameUpperCase}_GENERATOR_INTERRUPT_TRIGGER;
 *    ${moduleNameUpperCase}_GeneratorInterruptEnable(genNum, interrupt);
 * @endcode
    </#if>
 */
</#if>
inline static void ${moduleNameUpperCase}_GeneratorInterruptEnable(${moduleNameUpperCase}_GENERATOR genNum, ${moduleNameUpperCase}_GENERATOR_INTERRUPT interrupt)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                switch(interrupt) { 
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_FAULT:
                                        ${.vars["pg"+i+"intFaultEnableBit"]} = 1U;
                                        break;       
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_CURRENT_LIMIT:
                                        ${.vars["pg"+i+"intCurrentLimitEnableBit"]} = 1U;
                                        break;
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_FEED_FORWARD:
                                        ${.vars["pg"+i+"intFeedForwardEnableBit"]} = 1U;
                                        break;
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_SYNC:
                                        ${.vars["pg"+i+"intSyncEnableBit"]} = 1U;
                                        break;                                                        
                        default:
                            /* Invalid Interrupt type, do nothing */  
                            break;  
                }
                break;   
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function disables interrupt requests for the PWM Generator selected by the 
 *             argument \ref ${moduleNameUpperCase}_GENERATOR.
 * @param[in]  genNum 	 - PWM generator number
 * @param[in]  interrupt - PWM generator interrupt source
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    enum ${moduleNameUpperCase}_GENERATOR genNum;
 *    enum ${moduleNameUpperCase}_GENERATOR_INTERRUPT interrupt;
 *    
 *    genNum = ${moduleNameUpperCase}_GENERATOR_1;
 *    interrupt = ${moduleNameUpperCase}_GENERATOR_INTERRUPT_TRIGGER;
 *    ${moduleNameUpperCase}_GeneratorInterruptDisable(genNum, interrupt);
 * @endcode
    </#if>
 */
</#if>
inline static void ${moduleNameUpperCase}_GeneratorInterruptDisable(${moduleNameUpperCase}_GENERATOR genNum, ${moduleNameUpperCase}_GENERATOR_INTERRUPT interrupt)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                switch(interrupt) { 
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_FAULT:
                                        ${.vars["pg"+i+"intFaultEnableBit"]} = 0U;
                                        break;       
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_CURRENT_LIMIT:
                                        ${.vars["pg"+i+"intCurrentLimitEnableBit"]} = 0U;
                                        break;
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_FEED_FORWARD:
                                        ${.vars["pg"+i+"intFeedForwardEnableBit"]} = 0U;
                                        break;
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_SYNC:
                                        ${.vars["pg"+i+"intSyncEnableBit"]} = 0U;
                                        break;                                                        
                        default:
                            /* Invalid Interrupt type, do nothing */ 
                            break;  
                }
                break;   
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function clears the PWM interrupt status for the PWM Generator selected by the 
 *             argument \ref ${moduleNameUpperCase}_GENERATOR.   
 * @param[in]  genNum 	- PWM generator number
 * @param[in]  interrupt - PWM generator interrupt source
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    enum ${moduleNameUpperCase}_GENERATOR genNum;
 *    enum ${moduleNameUpperCase}_GENERATOR_INTERRUPT interrupt;
 *    
 *    genNum = ${moduleNameUpperCase}_GENERATOR_1;
 *    interrupt = ${moduleNameUpperCase}_GENERATOR_INTERRUPT_TRIGGER;
 *    ${moduleNameUpperCase}_GeneratorEventStatusClear(genNum, interrupt);
 * @endcode
    </#if>
 */
</#if>
inline static void ${moduleNameUpperCase}_GeneratorEventStatusClear(${moduleNameUpperCase}_GENERATOR genNum, ${moduleNameUpperCase}_GENERATOR_INTERRUPT interrupt)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                switch(interrupt) { 
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_FAULT:
                                        ${.vars["pg"+i+"intFaultStatusBit"]} = 0U;
                                        break;
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_CURRENT_LIMIT:
                                        ${.vars["pg"+i+"intCurrentLimitStatusBit"]} = 0U;
                                        break;
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_FEED_FORWARD:
                                        ${.vars["pg"+i+"intFeedForwardStatusBit"]} = 0U;
                                        break;
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_SYNC:
                                        ${.vars["pg"+i+"intSyncStatusBit"]} = 0U;
                                        break;
                        default:
                            /* Invalid Interrupt type, do nothing */  
                            break;  
                }              
                break; 
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

<#if generateDoxygen>
/**
 * @brief      This inline function gets the PWM interrupt status for the PWM Generator selected by the 
 *             argument \ref ${moduleNameUpperCase}_GENERATOR.   
 * @param[in]  genNum 	- PWM generator number
 * @param[in]  interrupt - PWM generator interrupt source
 * @return     true  - Interrupt is pending
 * @return     false - Interrupt is not pending
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    enum ${moduleNameUpperCase}_GENERATOR genNum;
 *    enum ${moduleNameUpperCase}_GENERATOR_INTERRUPT interrupt;
 *    bool status;
 *    
 *    genNum = ${moduleNameUpperCase}_GENERATOR_1;
 *    interrupt = ${moduleNameUpperCase}_GENERATOR_INTERRUPT_TRIGGER;
 *    status = ${moduleNameUpperCase}_GeneratorEventStatusGet(genNum, interrupt);
 * @endcode
    </#if>
 */
</#if>
inline static bool ${moduleNameUpperCase}_GeneratorEventStatusGet(${moduleNameUpperCase}_GENERATOR genNum, ${moduleNameUpperCase}_GENERATOR_INTERRUPT interrupt)
{
    bool status = false;
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
    <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                switch(interrupt) { 
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_FAULT:
                                        status = (${.vars["pg"+i+"intFaultStatusBit"]} != 0U);
                                        break;
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_CURRENT_LIMIT:
                                        status = (${.vars["pg"+i+"intCurrentLimitStatusBit"]} != 0U);
                                        break;
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_FEED_FORWARD:
                                        status = (${.vars["pg"+i+"intFeedForwardStatusBit"]} != 0U);
                                        break;
                        case ${moduleNameUpperCase}_GENERATOR_INTERRUPT_SYNC:
                                        status = (${.vars["pg"+i+"intSyncStatusBit"]} != 0U);
                                        break;
                        default:
                            /* Invalid Interrupt type, do nothing */ 
                            break;  
                }              
                break; 
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
    return status;
}

<#if generateDoxygen>
/**
 * @brief      This inline function requests to update the data registers for specific PWM generator 
 *             selected by the argument \ref ${moduleNameUpperCase}_GENERATOR.
 * @details    This function triggers a software update request for the specified PWM generator. 
 *             The update affects the data registers, and once requested, the update will 
 *             be processed by the system. The function does not return any status, but can 
 *             be used to initiate an update.
 * @param[in]  genNum - PWM generator number
 * @return     none  
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_SoftwareUpdateRequest(${moduleNameUpperCase}_GENERATOR_1);
 * @endcode
    </#if>
 * @remarks    none
 */
</#if>
inline static void ${moduleNameUpperCase}_SoftwareUpdateRequest(${moduleNameUpperCase}_GENERATOR genNum)
{
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                ${.vars["pg"+i+"softwareUpdateRequestBit"]} = 1U;
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }

}

<#if generateDoxygen>
/**
 * @brief      This inline function gets the status of the update request for specific PWM generator 
 *             selected by the argument \ref ${moduleNameUpperCase}_GENERATOR.
 * @details    This function checks whether a software update is currently pending for the 
 *             selected PWM generator. The function returns a boolean value indicating 
 *             whether the update has been requested and is awaiting processing.
 * @param[in]  genNum - PWM generator number
 * @return     true  - Software update is pending
 * @return     false - Software update is not pending 
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    bool status;
 *    
 *    status = ${moduleNameUpperCase}_SoftwareUpdatePending(${moduleNameUpperCase}_GENERATOR_1);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static bool ${moduleNameUpperCase}_SoftwareUpdatePending(${moduleNameUpperCase}_GENERATOR genNum)
{
    bool status = false;
    switch(genNum) { 
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                status = (${.vars["pg"+i+"softwareUpdateReqStatusBit"]} != 0U);
                break;       
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
    return status;
}

<#if trigACompareOptionAvailable == true >
<#if generateDoxygen>
/**
 * @brief      This inline function sets the Trigger A compare value in count for a specific PWM generator 
 *             selected by the argument \ref ${moduleNameUpperCase}_GENERATOR.  
 * @details    This function sets the trigger A compare value for the specified PWM generator, which determines the 
 *             timing for triggering other events or signals.
 * @param[in]  genNum - PWM generator number
 * @param[in]  trigA  - Trigger A compare value in count
 * @return     none  
 * @Note       Refer datasheet for valid size of data bits
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t trigA;
 *    
 *    trigA = 0xF;
 *    ${moduleNameUpperCase}_TriggerACompareValueSet(${moduleNameUpperCase}_GENERATOR_1, trigA);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_TriggerACompareValueSet(${moduleNameUpperCase}_GENERATOR genNum,uint32_t trigA)
{
    switch(genNum) {
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_HR_ENABLE = "PG" + i + "_HighResolutionEnable">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                <#if .vars[PWM_GEN_HR_ENABLE]?has_content && .vars[PWM_GEN_HR_ENABLE] == true>
                PG${i}TRIGA = trigA & 0x800FFFFFUL;
                <#else>
                PG${i}TRIGA = trigA & 0x800FFFF0UL;
                </#if>            
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

</#if>

<#if trigBCompareOptionAvailable == true >
<#if generateDoxygen>
/**
 * @brief      This inline function sets the Trigger B compare value in count for a specific PWM generator 
 *             selected by the argument \ref ${moduleNameUpperCase}_GENERATOR.   
 * @details    This function sets the trigger B compare value for the specified PWM generator, which determines the 
 *             timing for triggering other events or signals.
 * @param[in]  genNum - PWM generator number
 * @param[in]  trigB  - Trigger B compare value in count
 * @return     none  
 * @Note       Refer datasheet for valid size of data bits
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t trigB;
 *    
 *    trigB = 0xF;
 *    ${moduleNameUpperCase}_TriggerBCompareValueSet(${moduleNameUpperCase}_GENERATOR_1, trigB);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_TriggerBCompareValueSet(${moduleNameUpperCase}_GENERATOR genNum,uint32_t trigB)
{
    switch(genNum) {
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">
    <#assign PWM_GEN_HR_ENABLE = "PG" + i + "_HighResolutionEnable">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                <#if .vars[PWM_GEN_HR_ENABLE]?has_content && .vars[PWM_GEN_HR_ENABLE] == true>
                PG${i}TRIGB = trigB & 0x800FFFFFUL;
                <#else>
                PG${i}TRIGB = trigB & 0x800FFFF0UL;
                </#if>            
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

</#if>

<#if trigCCompareOptionAvailable == true >
<#if generateDoxygen>
/**
 * @brief      This inline function sets the Trigger C compare value in count for a specific PWM generator 
 *             selected by the argument \ref ${moduleNameUpperCase}_GENERATOR.
 * @details    This function sets the trigger C compare value for the specified PWM generator, which determines the 
 *             timing for triggering other events or signals.
 * @param[in]  genNum - PWM generator number
 * @param[in]  trigC  - Trigger C compare value in count
 * @return     none  
 * @Note       Refer datasheet for valid size of data bits
    <#if functionHeaderExample == true>
 * 
 * @b Example:
 * @code
 *    uint16_t trigC;
 *    
 *    trigC = 0xF;
 *    ${moduleNameUpperCase}_TriggerCCompareValueSet(${moduleNameUpperCase}_GENERATOR_1, trigC);
 * @endcode
    </#if>
 * @remarks   none
 */
</#if>
inline static void ${moduleNameUpperCase}_TriggerCCompareValueSet(${moduleNameUpperCase}_GENERATOR genNum,uint32_t trigC)
{
    switch(genNum) {
<#list 1..MAX_GENERATOR_COUNT as i>
   <#assign PWM_GEN_ENABLE = "PG" + i + "_ENABLE">   
    <#assign PWM_GEN_HR_ENABLE = "PG" + i + "_HighResolutionEnable">
    <#if .vars[PWM_GEN_ENABLE]?has_content && .vars[PWM_GEN_ENABLE] == true>
        case PWM_GENERATOR_${i}:
                <#if .vars[PWM_GEN_HR_ENABLE]?has_content && .vars[PWM_GEN_HR_ENABLE] == true>
                PG${i}TRIGC = trigC & 0x800FFFFFUL;
                <#else>
                PG${i}TRIGC = trigC & 0x800FFFF0UL;
                </#if>            
                break;
    </#if>
</#list>
        default:
            /* Invalid PWM Generator, do nothing */ 
            break;
    }
}

</#if>
</#if>

<#if intEnabled == true>
<#if generateDoxygen>
/**
 * @brief Registers a callback function for PWM EOC event.
 *
 * @details This function allows the application to register a callback function 
 * that the PLIB will call when a individual PWM generator EOC event has occured. 
 *
 * The function also allows the application to specify a context value 
 * (usually a pointer to a structure or data) that is passed into the callback 
 * function when it is executed. The registered callback will be invoked 
 * from the peripheral interrupt context. Therefore, the callback function should 
 * be lightweight and quick.
 *
 * The callback function must be registered before enabling the PWM Generator.
 *
 * @pre The `PWM_Initialize()` function must have been called. 
 * This function is only available if the library is configured for **interrupt mode**.
 *
 * @param[in] callback A pointer to a function with a calling signature defined 
 *                     by the `PWM_CALLBACK` data type. 
 *                     Setting this to `NULL` disables the callback feature.
 * @param[in] context  A value (usually a pointer) that is passed into the callback 
 *                     function when it is invoked.
 *
 * @return None.
 *
 * @remarks None.
 */
</#if>
bool ${moduleNameUpperCase}_EOCEventCallbackRegister(
    PWM_GENERATOR genNum,
    const PWM_GEN_EOC_EVENT_CALLBACK callback,
    uintptr_t context );
</#if>

</#if> 
#endif //${moduleNameUpperCase}_H

