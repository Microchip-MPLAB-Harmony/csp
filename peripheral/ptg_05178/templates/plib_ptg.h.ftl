<#assign generateDoxygen = true>
/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleNameUpperCase?lower_case}.h
 
  Summary:
    ${moduleNameUpperCase?lower_case} PLIB Header File
 
  Description:
    This file has prototype of all the interfaces provided for particular
    ${moduleNameUpperCase?lower_case} peripheral.
 
*******************************************************************************/
 
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
#ifndef PLIB_PTG_H
#define PLIB_PTG_H

// /cond IGNORE_THIS   ----> DOM will ignore these comments
/* Provide C++ Compatibility */
#ifdef __cplusplus
 
    extern "C" {
 
#endif
// /endcond

// Section: Included Files

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>

/**
* @brief    Defines the ${moduleNameUpperCase} events that are available.
*/
typedef enum
{
	TRIGGER0,         /**<${moduleNameUpperCase} Trigger0 Event */
    TRIGGER1,         /**<${moduleNameUpperCase} Trigger1 Event */
    TRIGGER2,         /**<${moduleNameUpperCase} Trigger2 Event */
    TRIGGER3,         /**<${moduleNameUpperCase} Trigger3 Event */
    WATCHDOGTIMER,    /**<${moduleNameUpperCase} WatchDogTimer Event */
}${moduleNameUpperCase}_EVENTS;

typedef void (*${moduleNameUpperCase}_EVENTS_CALLBACK)(uintptr_t context);

typedef struct
{
    /* ${moduleNameUpperCase} Event handler */
	${moduleNameUpperCase}_EVENTS_CALLBACK callback_fn;
	/* Context */
    uintptr_t context;
}${moduleNameUpperCase}_EVENTS_CALLBACK_OBJECT;

// Section: Macro Definitions

/**
 * @brief    Defines ${moduleNameUpperCase} execution steps
*/
 /* PTGQUE0 */                
#define PTG_STEP0 PTGQUE0bits.STEP0                
#define PTG_STEP1 PTGQUE0bits.STEP1                
 /* PTGQUE1 */                
#define PTG_STEP2 PTGQUE0bits.STEP2                
#define PTG_STEP3 PTGQUE0bits.STEP3                
 /* PTGQUE2 */                
#define PTG_STEP4 PTGQUE1bits.STEP4                
#define PTG_STEP5 PTGQUE1bits.STEP5                
 /* PTGQUE3 */                
#define PTG_STEP6 PTGQUE1bits.STEP6                
#define PTG_STEP7 PTGQUE1bits.STEP7                
 /* PTGQUE4 */                
#define PTG_STEP8 PTGQUE2bits.STEP8                
#define PTG_STEP9 PTGQUE2bits.STEP9                
 /* PTGQUE5 */                
#define PTG_STEP10 PTGQUE2bits.STEP10                
#define PTG_STEP11 PTGQUE2bits.STEP11                
 /* PTGQUE6 */                
#define PTG_STEP12 PTGQUE3bits.STEP12                
#define PTG_STEP13 PTGQUE3bits.STEP13                
 /* PTGQUE7 */                
#define PTG_STEP14 PTGQUE3bits.STEP14                
#define PTG_STEP15 PTGQUE3bits.STEP15                
 /* PTGQUE8 */                
#define PTG_STEP16 PTGQUE4bits.STEP16                
#define PTG_STEP17 PTGQUE4bits.STEP17                
 /* PTGQUE9 */                
#define PTG_STEP18 PTGQUE4bits.STEP18                
#define PTG_STEP19 PTGQUE4bits.STEP19                
 /* PTGQUE10 */                
#define PTG_STEP20 PTGQUE5bits.STEP20                
#define PTG_STEP21 PTGQUE5bits.STEP21                
 /* PTGQUE11 */                
#define PTG_STEP22 PTGQUE5bits.STEP22                
#define PTG_STEP23 PTGQUE5bits.STEP23                
 /* PTGQUE12 */                
#define PTG_STEP24 PTGQUE6bits.STEP24                
#define PTG_STEP25 PTGQUE6bits.STEP25                
 /* PTGQUE13 */                
#define PTG_STEP26 PTGQUE6bits.STEP26                
#define PTG_STEP27 PTGQUE6bits.STEP27                
 /* PTGQUE14 */                
#define PTG_STEP28 PTGQUE7bits.STEP28                
#define PTG_STEP29 PTGQUE7bits.STEP29                
 /* PTGQUE15 */                
#define PTG_STEP30 PTGQUE7bits.STEP30                
#define PTG_STEP31 PTGQUE7bits.STEP31

/**
 @brief    ${moduleNameUpperCase} command macros
*/
#define PTGCTRL  (0x0u << 4u )    //PTGCTRL command        
#define PTGCOPY  (0x1u << 4u )    //PTGCOPY command        
#define PTGADD   (0x1u << 4u )    //PTGADD command        
#define PTGSTRB  (0x2u << 4 )    //PTGSTRB command        
#define PTGWHI  (0x4u << 4u )    //PTGWHI command        
#define PTGWLO  (0x5u << 4u )    //PTGWLO command        
#define PTGIRQ  (0x7u << 4u )    //PTGIRQ command        
#define PTGTRIG  (0x8u << 4u )    //PTGTRIG command        
#define PTGJMP  (0xau << 4u )    //PTGJMP command        
#define PTGJMPC0  (0xcu << 4u )    //PTGJMPC0 command        
#define PTGJMPC1  (0xeu << 4u )    //PTGJMPC1 command

// Section: ${moduleNameUpperCase} Module APIs

/**
 * @brief    Initializes ${moduleNameUpperCase} module 
 *
 * @details  This function initializes the ${moduleNameUpperCase} Peripheral Library (PLIB) of the device 
 * with the values configured in the MCC GUI. Once the peripheral is initialized, 
 * Step Sequence APIs can be used to start the Step Sequence
 *
 * @pre MCC GUI should be configured with the correct values.
 *
 * @param    none
 *
 * @return   none  
 *  
 * @b Example:
 * @code
 *    void main(void)
 *    {
 *    
 *    SYSTEM_Initialize();
 *    ${moduleNameUpperCase}_Enable();
 *    ${moduleNameUpperCase}_StartStepSequence();
 *      while (1)
 *      {      
 *          ${moduleNameUpperCase}_SoftwareTriggerSet();  
 *          bool wdtBit = ${moduleNameUpperCase}_WatchdogTimeoutStatusGet();
 *              if(wdtBit){          
 *                 ${moduleNameUpperCase}_StepSequenceStop();
 *                 ${moduleNameUpperCase}_Disable();
 *                }
 *      }
 *    }
 * @endcode
 * @remarks None
 */
void ${moduleNameUpperCase}_Initialize(void);

/**
 * @brief Deinitializes the ${moduleNameUpperCase} peripheral of the device.
 *
 * @details This function deinitializes the ${moduleNameUpperCase} Peripheral Library (PLIB) of the device, 
 * returning the ${moduleNameUpperCase} peripheral to its default reset state. After calling this function, 
 * the ${moduleNameUpperCase} peripheral will no longer be operational, and any subsequent ${moduleNameUpperCase} operations 
 * will fail until re-initialization using the PTG_Initialize API.
 *
 * @pre The ${moduleNameUpperCase} peripheral must have been initialized using the PTG_Initialize API.
 *
 * @param None
 *
 * @return None
 *
 * @note This function should be called when the ${moduleNameUpperCase} peripheral is no longer required 
 * to release resources and ensure proper reset behavior.
 * 
 * @b Example:
 * @code
 *        ${moduleNameUpperCase}_Deinitialize();
 * @endcode
 * @remarks None
 */
void ${moduleNameUpperCase}_Deinitialize(void);

/**
 * @brief Enables the ${moduleNameUpperCase} peripheral of the device.
 *
 * @details This function enables the ${moduleNameUpperCase} Peripheral Library (PLIB) of the device, 
 * for its desired use
 *
 * @pre The ${moduleNameUpperCase} peripheral must have been initialized using the PTG_Initialize API.
 *
 * @param None
 *
 * @return None
 *
 * @note This function should be called when the ${moduleNameUpperCase} peripheral is required 
 * to enable
 * 
 * @b Example:
 * @code
 *        ${moduleNameUpperCase}_Enable();
 * @endcode
 * @remarks None
 */


void ${moduleNameUpperCase}_Enable (void);

/**
 * @brief Starts the step sequence of the ${moduleNameUpperCase} peripheral of the device.
 *
 * @details This function initiates the step sequence for the ${moduleNameUpperCase} peripheral of the device
 * This process begins the programmed sequence of operations. Ensures the device performs
 * Step Commands in the correct order.
 * 
 * @pre The ${moduleNameUpperCase} peripheral must have been enabled using the PTG_Enable API. The Step Sequence configurations
 * should be carefully made in the MCC GUI
 *
 * @param None
 *
 * @return None
 *
 * @note This function should be called when the ${moduleNameUpperCase} peripheral is required 
 * to start the step sequence
 * 
 * @b Example:
 * @code
 *        ${moduleNameUpperCase}_StepSequenceStart();
 * @endcode
 * @remarks None
 */

void PTG_StepSequenceStart(void);

/**
 * @brief Activates the software trigger of the ${moduleNameUpperCase} peripheral of the device.
 *
 * @details This function initiates the step sequence for the ${moduleNameUpperCase} peripheral of the device
 * This process begins the programmed sequence of operations. Ensures the device performs
 * Step Commands in the correct order.
 * 
 * @pre The ${moduleNameUpperCase} peripheral must have been enabled using the PTG_Enable API. The Step Sequence configurations
 * should be carefully made in the MCC GUI
 *
 * @param None
 *
 * @return None
 *
 * @note This function should be called when the ${moduleNameUpperCase} peripheral is required 
 * to set the software trigger
 * 
 * @b Example:
 * @code
 *        ${moduleNameUpperCase}_SoftwareTriggerSet();
 * @endcode
 * @remarks None
 */

void PTG_SoftwareTriggerSet(void);

/**
 * @brief Clears the software trigger of the ${moduleNameUpperCase} peripheral of the device.
 *
 * @details This function clears the software trigger bit PTGSWT of the PTGCON register
 * 
 * @pre The ${moduleNameUpperCase} peripheral must have been enabled using the PTG_Enable API. The Step Sequence configurations
 * should be carefully made in the MCC GUI
 *
 * @param None
 *
 * @return None
 *
 * @Note This API is added to resolve the Errata issue. After executing the wait for software trigger step command
 * followed by the same command, the PTGSWT bit is not cleared by hardware.
 * 
 * @b Example:
 * @code
 *    ${moduleNameUpperCase}_SoftwareTriggerClear();
 * @endcode
   @remarks None
 */

void ${moduleNameUpperCase}_SoftwareTriggerClear(void);

/**
 * @brief Indicates the status of the watchdog timeout status of the ${moduleNameUpperCase} Peripheral of the device.
 *
 * @details This function displays the current status of the watchdog timeout for the ${moduleNameUpperCase} peripheral
 *  of the device. This information helps monitor whether the watchdog timer has expired. Ensures
 *  timely detection and response to potential system issues.
 * 
 * @pre The ${moduleNameUpperCase} peripheral must have been enabled using the PTG_Enable API. The Step Sequence configurations
 * should be carefully made in the MCC GUI
 *
 * @return   true   - ${moduleNameUpperCase} watchdog timeout occurred
 * @return   false  - ${moduleNameUpperCase} watchdog timeout not occurred  
 *  
 *@b Example:
 * @code
 *    ${moduleNameUpperCase}_WatchdogTimeoutStatusGet();
 * @endcode
 * @remarks None 
 */

bool ${moduleNameUpperCase}_WatchdogTimeoutStatusGet(void);

/**
 * @brief Stops the step sequence of the ${moduleNameUpperCase} peripheral of the device.
 *
 * @details Halts the ongoing step sequence of the ${moduleNameUpperCase} peripheral in the device. This action
 * interrupts the programmed series of operations. Ensures the device ceases its current 
 * step commands immediately
 * 
 * @pre The ${moduleNameUpperCase} peripheral must have been enabled using the PTG_Enable API. The Step Sequence configurations
 * should be carefully made in the MCC GUI and step sequence should be started with the PTG_StepSequenceStart API.
 *
 * @param None
 *
 * @return None
 *
 * @note This function should be called when the ${moduleNameUpperCase} peripheral is required 
 * to stop the step sequence
 * 
 * @b Example:
 * @code
 *        ${moduleNameUpperCase}_StepSequenceStop();
 * @endcode
 * @remarks None
 */
void ${moduleNameUpperCase}_StepSequenceStop(void);

/**
 * @brief Disables the ${moduleNameUpperCase} peripheral of the device.
 *
 * @details This function disables the ${moduleNameUpperCase} Peripheral Library (PLIB) of the device, 
 * for its desired use
 *
 * @pre The ${moduleNameUpperCase} peripheral must have been initialized using the PTG_Initialize API.
 * The peripheral should be enabled using the PTG_Enable() API.
 *
 * @param None
 *
 * @return None
 *
 * @note This function should be called when the ${moduleNameUpperCase} peripheral is required 
 * to disable
 * 
 * @b Example:
 * @code
 *        ${moduleNameUpperCase}_Disable();
 * @endcode
 * @remarks None
 */

void ${moduleNameUpperCase}_Disable(void);

<#if isPtgInterruptEnabled == true>
/**
 * @brief Registers a callback function for ${moduleNameUpperCase} Peripheral events.
 *
 * @details This function allows the application to register a callback function 
 * that the PLIB will call when a particular trigger event has occurred. 
 *
 * The function also allows the application to specify a context value 
 * (usually a pointer to a structure or data) that is passed into the callback 
 * function when it is executed. The registered callback will be invoked 
 * from the peripheral interrupt context. Therefore, the callback function should 
 * be lightweight and quick.
 *
 * The callback function must be registered before initiating step sequence operation.
 *
 * @pre The `PTG_Initialize()` function must have been called. 
 * This function is only available if the library is configured for **interrupt mode**.
 *
 * @param[in] callback A pointer to a function with a calling signature defined 
 *                     by the `PTG_EVENT_CALLBACK` data type.
 *                     Setting this to `NULL` disables the callback feature.
 * @param[in] context  A value (usually a pointer) that is passed into the callback 
 *                     function when it is invoked.
 *
 * @return None.
 * @b Example
 * @code
 * 
 * void MyPTGEventHandler(PTG_EVENTS event, uintptr_t context) 
 *   {
 *		printf("Trigger hit event detected!\n");
 *   }
 *
 *
 * int main() {
 *   PTG_Initialize();
 *   PTG_EventCallbackRegister(PTG_EVENT_TRIGGER_HIT, MyPTGEventHandler, (uintptr_t)NULL);
 *	 PTG_Enable();
 *	 PTG_StepSequenceStart();
 *   
 *   while (1) {
 *       
 *   }
 *
 *   return 0;
 * }
 * @endcode
 *
 * @remarks None.
 */
void ${moduleNameUpperCase}_EventCallbackRegister(PTG_EVENTS event, PTG_EVENTS_CALLBACK callback_fn, uintptr_t context);
</#if>

/* Provide C++ Compatibility */
#ifdef __cplusplus
 
    }
 
#endif
// /endcond
#endif //PLIB_PTG_H
    
/**
 End of File
*/
