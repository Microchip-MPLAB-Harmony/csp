<#assign generateDoxygen = true>
/*******************************************************************************
  ${moduleNameUpperCase} PLIB Header

  Company:
    Microchip Technology Inc.

  File Name:
    plib_intc.h

  Summary:
    ${moduleNameUpperCase} PLIB Header File

  Description:
    None

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${moduleNameUpperCase}_H
#define PLIB_${moduleNameUpperCase}_H

// Section: Included Files

#include "device.h"
#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END
<#assign numOfEnabledExtInt = 0>

<#list 0..MAX_EXTERNAL_INT_COUNT as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
        <#assign numOfEnabledExtInt = numOfEnabledExtInt + 1>
    </#if>
</#list>

// Section: Data Types

${intSourceIRQList}

<#if generateDoxygen>
/**
 * @brief    Interrupt Source Type Definition
 *
 * Defines the type used to represent interrupt sources in the system. 
 * The value corresponds to various interrupt sources available in the device.
 */
</#if>
typedef uint32_t INT_SOURCE;

<#if 0 < numOfEnabledExtInt>
<#if generateDoxygen>
/**
 @enum     EXTERNAL_INT_PIN
 @brief    This enumeration identifies the external interrupt pins for which 
           interrupt option is enabled in Interrupt Controller.
*/
</#if>
typedef enum
{
<#list 0..MAX_EXTERNAL_INT_COUNT as i>
    <#assign EXT_INT_PIN = "EXTERNAL_" + i + "_EXTERNAL_INTERRUPT_UPDATE">
    <#if .vars[EXT_INT_PIN]?has_content && .vars[EXT_INT_PIN] == true>
        <#lt>    EXTERNAL_INT_${i} = ${i},  /**< External Interrupt ${i} */
    </#if>
</#list>
}EXTERNAL_INT_PIN;

<#if generateDoxygen>
/**
 * @brief    Callback function type for external interrupt pin events.
 * @details  This typedef defines a function pointer type for a callback function that is
 *           used to handle external interrupt pin events. The callback function is called
 *           when an external interrupt occurs on a specified pin.
 * @param[in]    pin     - The external interrupt pin that triggered the callback.
 * @param[in]    context - A user-defined context or data passed to the callback function.
 * 
 * @note     The `pin` parameter indicates which external interrupt pin triggered the
 *           callback, and the `context` parameter allows for user-specific data to 
 *           be passed to the callback function.
 * 
 * @b Example:
 * @code
 * void my_callback(EXTERNAL_INT_PIN pin, uintptr_t context) {
 *      
 * }
 * 
 * EXTERNAL_INT_PIN_CALLBACK callback = my_callback;
 * @endcode
 */
</#if>
typedef  void (*EXTERNAL_INT_PIN_CALLBACK) (EXTERNAL_INT_PIN pin, uintptr_t context);

<#if generateDoxygen>
/**
 @struct   EXT_INT_PIN_CALLBACK_OBJ
 @brief    This structure holds the callback and context information for handling
           events on a specified external interrupt pin.
*/
</#if>
typedef struct {
   
    EXTERNAL_INT_PIN_CALLBACK        callback;     /**< Callback for event on target pin */
    
    uintptr_t                        context;      /**< Callback Context */
    
} EXT_INT_PIN_CALLBACK_OBJ;
</#if>

// Section: Interface Routines

<#if generateDoxygen>
/**
 * @brief   Configures and initializes the interrupt subsystem.
 * @details This function configures and initializes the interrupt subsystem 
 *          appropriately for the current system design.
 * @pre     None.
 * @param   None.
 * @return  None.
 * 
 * @b Example
 * @code
 * ${moduleNameUpperCase}_Initialize();
 * @endcode
 * 
 * @remarks None.
 */
</#if>
void ${moduleNameUpperCase}_Initialize ( void );

<#if generateDoxygen>
/**
 * @brief   Enables the interrupt source.
 * @details This function enables the interrupt source. The interrupt flag is set 
 *          when the interrupt request is sampled. The pending interrupt request will not 
 *          cause further processing if the interrupt is not enabled using this function 
 *          or if interrupts are not enabled.
 * @pre     The ${moduleNameUpperCase}_Initialize() function must have been called first.
 * @param   source One of the possible values from INT_SOURCE.
 * @return  None.
 * @note    This API performs a Read-Modify-Write (RMW) operation on the IECx register. 
 *          To prevent race conditions, please disable global interrupts using 
 *          `${moduleNameUpperCase}_Disable` API before calling this function.
 * 
 * @b Example
 * @code
 * bool prevStatus = ${moduleNameUpperCase}_Disable();
 * ${moduleNameUpperCase}_SourceEnable(INT_SOURCE_INT0);
 * ${moduleNameUpperCase}_Restore(prevStatus);
 * @endcode
 * 
 * @remarks This function implements an operation of the SourceControl feature. 
 *          This feature may not be available on all devices. Please refer to the specific 
 *          device data sheet to determine availability.
 */
</#if>
void ${moduleNameUpperCase}_SourceEnable( INT_SOURCE source );

<#if generateDoxygen>
/**
 * @brief   Disables the interrupt source.
 * @details This function disables the given interrupt source.
 * @pre     The ${moduleNameUpperCase}_Initialize() function must have been called first.
 * @param   source One of the possible values from INT_SOURCE.
 * @return  None.
 * @note    This API performs a Read-Modify-Write (RMW) operation on the IECx register. 
 *          To prevent race conditions, please disable global interrupts using 
 *          `${moduleNameUpperCase}_Disable` API before calling this function.
 *
 * @b Example
 * @code
 * bool prevStatus = ${moduleNameUpperCase}_Disable();
 * ${moduleNameUpperCase}_SourceDisable(INT_SOURCE_INT0);
 * ${moduleNameUpperCase}_Restore(prevStatus);
 * @endcode
 * 
 * @remarks This function implements an operation of the SourceControl feature. 
 *          This feature may not be available on all devices. Please refer to the specific 
 *          device data sheet to determine availability.
 */
</#if>
void ${moduleNameUpperCase}_SourceDisable( INT_SOURCE source );

<#if generateDoxygen>
/**
 * @brief   Gets the enable state of the interrupt source.
 * @details This function gets the enable state of the interrupt source.
 * @pre     The ${moduleNameUpperCase}_Initialize() function must have been called first.
 * @param   source One of the possible values from INT_SOURCE.
 * 
 * @return
 * - true: If the interrupt source is enabled
 * - false: If the interrupt source is disabled
 * 
 * @b Example
 * @code
 * if(${moduleNameUpperCase}_SourceIsEnabled(INT_SOURCE_INT0) != true)
 * {
 *     ${moduleNameUpperCase}_SourceEnable(INT_SOURCE_INT0);
 * }
 * @endcode
 * 
 * @remarks This function implements an operation of the SourceControl feature. 
 *          This feature may not be available on all devices. Please refer to the specific 
 *          device data sheet to determine availability.
 */
</#if>
bool ${moduleNameUpperCase}_SourceIsEnabled( INT_SOURCE source );

<#if generateDoxygen>
/**
 * @brief   Returns the status of the interrupt flag for the selected source.
 * @details This function returns the status of the interrupt flag for the selected 
 *          source. The flag is set when the interrupt request is recognized. The pending 
 *          interrupt request will not cause further processing if the interrupt is not 
 *          enabled using the function ${moduleNameUpperCase}_SourceEnable or if interrupts are not enabled.
 * @pre     The ${moduleNameUpperCase}_Initialize() function must have been called first.
 * @param   source One of the possible values from INT_SOURCE.
 * 
 * @return
 * - true: If the interrupt request is recognized for the source
 * - false: If the interrupt request is not recognized for the source
 * 
 * @b Example
 * @code
 * if(${moduleNameUpperCase}_SourceStatusGet(INT_SOURCE_INT0) != true)
 * {
 *     ${moduleNameUpperCase}_SourceStatusClear(INT_SOURCE_INT0);
 * }
 * @endcode
 * 
 * @remarks This function implements an operation of the SourceFlag feature. 
 *          This feature may not be available on all devices. Please refer to the specific 
 *          device data sheet to determine availability.
 */
</#if>
bool ${moduleNameUpperCase}_SourceStatusGet( INT_SOURCE source );

<#if generateDoxygen>
/**
 * @brief   Sets the status of the interrupt flag for the selected source.
 * @details This function sets the status of the interrupt flag for the selected 
 *          source. 
 * @note    This function will not be used during normal operation of the system. 
 *          It is used to generate test interrupts for debug and testing purposes.
 * @pre     The ${moduleNameUpperCase}_Initialize() function must have been called first.
 * @param   source One of the possible values from INT_SOURCE.
 * @return  None.
 * 
 * @b Example
 * @code
 * ${moduleNameUpperCase}_SourceStatusSet(INT_SOURCE_CORE_TIMER);
 * @endcode
 * 
 * @remarks This function implements an operation of the SourceFlag feature. 
 *          This feature may not be available on all devices. Please refer to the specific 
 *          device data sheet to determine availability.
 */
</#if>
void ${moduleNameUpperCase}_SourceStatusSet( INT_SOURCE source );

<#if generateDoxygen>
/**
 * @brief   Clears the status of the interrupt flag for the selected source.
 * @details This function clears the status of the interrupt flag for the selected 
 *          source. The flag is set when the interrupt request is identified. The pending 
 *          interrupt request will not cause further processing if the interrupt is not 
 *          enabled using the function ${moduleNameUpperCase}_SourceEnable or if interrupts are not enabled.
 * @pre     The ${moduleNameUpperCase}_Initialize() function must have been called first.
 * @param   source One of the possible values from INT_SOURCE.
 * @return  None.
 * 
 * @b Example
 * @code
 * if(${moduleNameUpperCase}_SourceStatusGet(INT_SOURCE_CORE_TIMER) != true)
 * {
 *     ${moduleNameUpperCase}_SourceStatusClear(INT_SOURCE_CORE_TIMER);
 * }
 * @endcode
 * 
 * @remarks This function implements an operation of the SourceFlag feature. 
 *          This feature may not be available on all devices. Please refer to the specific 
 *          device data sheet to determine availability.
 */
</#if>
void ${moduleNameUpperCase}_SourceStatusClear( INT_SOURCE source );

<#if generateDoxygen>
/**
 * @brief   Enables all global interrupts.
 * @details This function enables all global interrupts, allowing the system 
 *          to respond to interrupt requests.
 * @pre     None.
 * @param   None.
 * @return  None.
 * 
 * @b Example
 * @code
 * ${moduleNameUpperCase}_Enable();
 * @endcode
 * 
 * @remarks None.
 */
</#if>
void ${moduleNameUpperCase}_Enable( void );

<#if generateDoxygen>
/**
 * @brief   Saves the current state of global interrupts and then disables all global interrupts.
 * @details This function saves the current state of global interrupts and then 
 *          disables all global interrupts, preventing further interrupts until they are 
 *          explicitly re-enabled. The interrupt status is returned to allow restoring 
 *          the previous interrupt state.
 * @pre     None.
 * @param   None.
 * @return  The interrupt status, which indicates the previous state of the global interrupts.
 * 
 * @b Example
 * @code
 * bool prevStatus = ${moduleNameUpperCase}_Disable();
 * @endcode
 * 
 * @remarks None.
 */
</#if>
bool ${moduleNameUpperCase}_Disable( void );

<#if generateDoxygen>
/**
 * @brief   Restores the state of global interrupts before the disable occurred.
 * @details This function restores the state of global interrupts to the specified 
 *          state that was saved prior to the disable operation. This is typically used 
 *          to re-enable interrupts after they were temporarily disabled.
 * @pre     The state must be previously saved using the ${moduleNameUpperCase}_Disable() function.
 * @param   state The interrupt status to restore, typically obtained from the ${moduleNameUpperCase}_Disable() function.
 * @return  None.
 * 
 * @b Example
 * @code
 * bool prevStatus = ${moduleNameUpperCase}_Disable();
 * ${moduleNameUpperCase}_SourceEnable(INT_SOURCE_INT0);
 * ${moduleNameUpperCase}_Restore(prevStatus);
 * @endcode
 * 
 * @remarks None.
 */
</#if>
void ${moduleNameUpperCase}_Restore( bool state );

<#if 0 < numOfEnabledExtInt>
<#if generateDoxygen>
/**
 * @brief   Registers an event handling function for the PLIB to call back when an external interrupt 
 *          occurs on the selected pin.
 * @details This function allows the application to register an event handler 
 *          function for the PLIB to call back when an external interrupt occurs on the 
 *          selected pin. If at any point the application wants to stop the callback, 
 *          it can call this function with the "callback" parameter set to NULL.
 * 
 * @param[in] extIntPin One of the external interrupt pins from the enum EXTERNAL_INT_PIN.
 * @param[in] callback  Pointer to the event handler function implemented by the user.
 * @param[in] context   The value of this parameter will be passed back to the 
 *                      application unchanged when the event handler function 
 *                      is called. It can be used to identify any application-specific value.
 * @return 
 * - true: Callback was successfully registered.
 * - false: Callback was not registered.
 * 
 * @b Example
 * @code
 * bool status = ${moduleNameUpperCase}_ExternalInterruptCallbackRegister(EXTERNAL_INT_0, myInterruptHandler, contextValue);
 * @endcode
 * 
 * @remarks None.
 */
</#if>
bool ${moduleNameUpperCase}_ExternalInterruptCallbackRegister(
        EXTERNAL_INT_PIN extIntPin,
        const EXTERNAL_INT_PIN_CALLBACK callback,
        uintptr_t context
    );

<#if generateDoxygen>
/**
 * @brief   Enables external interrupt on selected external interrupt pins.
 * @details This function enables external interrupt on selected external interrupt pins.
 * @pre     Interrupt option for the corresponding pins must be enabled in the ${moduleNameUpperCase} manager.
 * @param   extIntPin One or multiple external interrupt pins ORed from the enum EXTERNAL_INT_PIN.
 * @return  None.
 * 
 * @b Example
 * @code
 * ${moduleNameUpperCase}_ExternalInterruptEnable(EXTERNAL_INT_0);
 * @endcode
 * 
 * @remarks None.
 */
</#if>
void ${moduleNameUpperCase}_ExternalInterruptEnable( EXTERNAL_INT_PIN extIntPin );

<#if generateDoxygen>
/**
 * @brief   Disables external interrupt on selected external interrupt pins.
 * @details This function disables external interrupt on selected external interrupt pins.
 * @pre     Interrupt option for the corresponding pins must be enabled in the ${moduleNameUpperCase} manager.
 * @param   extIntPin One or multiple external interrupt pins ORed from the enum EXTERNAL_INT_PIN.
 * @return  None.
 * 
 * @b Example
 * @code
 * ${moduleNameUpperCase}_ExternalInterruptDisable(EXTERNAL_INT_0);
 * @endcode
 * 
 * @remarks None.
 */
</#if>
void ${moduleNameUpperCase}_ExternalInterruptDisable( EXTERNAL_INT_PIN extIntPin );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // PLIB_${moduleNameUpperCase}_H
