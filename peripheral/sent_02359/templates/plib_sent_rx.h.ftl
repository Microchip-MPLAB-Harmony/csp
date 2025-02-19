<#assign generateDoxygen = true>
/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}.h
 
  Summary:
    ${moduleName?lower_case} PLIB Header File
 
  Description:
    This file has prototype of all the interfaces provided for particular
    ${moduleName?lower_case} peripheral.
 
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

#ifndef SENT${SENT_INSTANCE}_H
#define SENT${SENT_INSTANCE}_H

// /cond IGNORE_THIS   ----> DOM will ignore these comments
/* Provide C++ Compatibility */
#ifdef __cplusplus
 
    extern "C" {
 
#endif
// /endcond

// Section: Included Files

#include <xc.h>
#include <stdbool.h>
#include <stdint.h>
#include "plib_sent_rx_common.h"

// Section: SENT${SENT_INSTANCE} PLIB Routines
 
/**
 * @brief Initializes the SENT${SENT_INSTANCE} peripheral of the device.
 *
 * @details This function initializes the SENT${SENT_INSTANCE} Peripheral Library (PLIB) of the device 
 * with the values configured in the MCC GUI. Once the peripheral is initialized, 
 * APIs can be used to transfer the data and receive the data.
 *
 * @pre MCC GUI should be configured with the correct values.
 *
 * @param None
 *
 * @return None
 *
 * @note This function must be called only once and before any other SENT${SENT_INSTANCE} receive/transfer function is called.
 *
 * @b Example:
 * @code
 *    struct SENT_DATA_TRANSMIT data;
 *    data.data1 = 0x01;
 *    data.data2 = 0x02;
 *    data.data3 = 0x03;
 *    data.status = 0x00;
 *    SENT${SENT_INSTANCE}_Initialize();
 *    SENT${SENT_INSTANCE}_Transmit(data);
 * @endcode
 * 
 * remarks None
 */
void SENT${SENT_INSTANCE}_Initialize(void);

/**
 * @brief Deinitializes the SENT${SENT_INSTANCE} peripheral of the device.
 *
 * @details This function deinitializes the SENT${SENT_INSTANCE} Peripheral Library (PLIB) of the device, 
 * returning the SENT${SENT_INSTANCE} peripheral to its default reset state. After calling this function, 
 * the SENT${SENT_INSTANCE} peripheral will no longer be operational, and any subsequent SENT${SENT_INSTANCE} operations 
 * will fail until re-initialization using the SENT${SENT_INSTANCE}_Initialize API.
 *
 * @pre The SENT${SENT_INSTANCE} peripheral must have been initialized using the SENT${SENT_INSTANCE}_Initialize API.
 *
 * @param None
 *
 * @return None
 *
 * @note This function should be called when the SENT${SENT_INSTANCE} peripheral is no longer required 
 * to release resources and ensure proper reset behavior.
 *
 * @b Example
 * @code
 * SENT${SENT_INSTANCE}_Initialize();
 * SENT${SENT_INSTANCE}_Enable();
 * SENT${SENT_INSTANCE}_Deinitialize();
 * @endcode
 *
 * @remarks None
 */
void SENT${SENT_INSTANCE}_Deinitialize(void);


/**
 * @brief Enables the SENT${SENT_INSTANCE} peripheral of the device.
 *
 * @details This function enables the SENT${SENT_INSTANCE} Peripheral Library (PLIB) of the device, 
 * for its desired use.
 *
 * @pre The SENT${SENT_INSTANCE} peripheral must have been initialized using the SENT${SENT_INSTANCE}_Initialize API.
 *
 * @param None
 *
 * @return None
 *
 * @note This function should be called when the SENT${SENT_INSTANCE} peripheral is required 
 * to start operation
 *
 * @b Example
 * @code
 * SENT${SENT_INSTANCE}_Initialize();
 * SENT${SENT_INSTANCE}_Enable();
 * @endcode
 *
 * @remarks None
 */
void SENT${SENT_INSTANCE}_Enable(void);

/**
 * @brief Disables the SENT${SENT_INSTANCE} peripheral of the device.
 *
 * @details This function disables the SENT${SENT_INSTANCE} Peripheral Library (PLIB) of the device, 
 * for its desired use
 *
 * @pre The SENT${SENT_INSTANCE} peripheral must have been initialized using the SENT${SENT_INSTANCE}_Initialize API.
 * The peripheral should be enabled using the SENT${SENT_INSTANCE}_Enable() API.
 *
 * @param None
 *
 * @return None
 *
 * @note This function should be called when the SENT${SENT_INSTANCE} peripheral is required 
 * to disable
 * 
 * @b Example:
 * @code
 *        SENT${SENT_INSTANCE}_Disable();
 * @endcode
 * @remarks None
 */
void SENT${SENT_INSTANCE}_Disable(void);

/**
 *
 * @brief    Reads the received data from transmitter
 *
 * @details  This function is responsible for receiving data transmitted for the
 * specified SENT instance. The function will handle the reception process and return the
 * received data.
 *
 * @pre  The SENT${SENT_INSTANCE} peripheral must have been initialized using the SENT${SENT_INSTANCE}_Initialize API.
 * The peripheral should be enabled using the SENT${SENT_INSTANCE}_Enable() API.
 * @param    none
 *
 * @return   \ref SENT_DATA_RECEIVE - Received data structure
 * 
 * @b Example:
 * @code
 *    SENT${SENT_INSTANCE}_Initialize();
 *    while(SENT${SENT_INSTANCE}_IsDataReceived());
 *    struct SENT_DATA_RECEIVE sentData = SENT${SENT_INSTANCE}_Receive(void);
 * @endcode
 * @remarks None
    
 */
SENT_DATA_RECEIVE SENT${SENT_INSTANCE}_Receive(void);

/**
 * @brief     Checks if data has been received for SENT Peripheral.
 *
 * @details   The function returns a boolean value indicating whether new data has been successfully
 * received and is available for processing. 
 *
 * @pre   The SENT${SENT_INSTANCE} peripheral must have been initialized using the SENT${SENT_INSTANCE}_Initialize API.
 * The peripheral should be enabled using the SENT${SENT_INSTANCE}_Enable() API.
 *
 * @param    none
 * @return   true   - SENT${SENT_INSTANCE} receive completed
 * @return   false  - SENT${SENT_INSTANCE} receive not completed
   
 * 
 * @b Example:
 * @code
 *    struct SENT_DATA_RECEIVE data;
 *    SENT${SENT_INSTANCE}_Initialize();
 *    data = SENT${SENT_INSTANCE}_Receive();
 *    while(!SENT${SENT_INSTANCE}_IsDataReceived());
 *    {
 *    }
 * @endcode
 * @remarks None 
 */
 bool SENT${SENT_INSTANCE}_IsDataReceived(void);

/**
 * @brief    Retrieves the current receive status SENT peripheral.
 *
 * @details  The function indicates the current status of the data reception process.
 * This status can provide information about whether data has been successfully received,
 * if there are any errors, or if the reception is still in progress.
 * @param    none
 * @return   Returns the SENT${SENT_INSTANCE} module reception status \ref SENT${SENT_INSTANCE}_RECEIVE_STATUS
 *  
 *@b Example:
 * @code
 *    struct SENT_DATA_RECEIVE data;
 *    enum SENT_RECEIVE_STATUS status;
 *    SENT${SENT_INSTANCE}_Initialize();
 *    data = SENT${SENT_INSTANCE}_Receive(data);
 *    while(!SENT${SENT_INSTANCE}_IsDataReceived());
 *    enum SENT${SENT_INSTANCE}_RECEIVE_STATUS status = SENT${SENT_INSTANCE}_ReceiveStatusGet();
 * @endcode
 * @remarks None   
 */
SENT_RECEIVE_STATUS SENT${SENT_INSTANCE}_ReceiveStatusGet(void);

/** 
 * @brief    Returns the type of reception error
 * @details  This function returns the most recent error code that was recorded during reception.
 *
 * @param    none
 * @return   Returns the SENT${SENT_INSTANCE} module reception error \ref SENT_ERROR_CODE
 *
 * @note 	 Ensure that the SENT instance is properly initialized and configured before calling this function.
 *
 * @b Example:
 * @code
 *	SENT_ERROR_CODE errorCode = ReceiveErrorGet();
 * 	if (errorCode != NO_ERROR) {
 *     
 * }
 * @endcode
 *
 * @remarks None
 */
 SENT_ERROR_CODE ReceiveErrorGet(void);

<#if SENT_INTERRUPT_MODE == true>
/**
 * @brief      Registers a callback function to be called upon the completion of data reception for the SENT${SENT_INSTANCE} Peripheral
 * @details    This function registers a callback upon completion of data reception. The callback function allows the user to define
 * custom actions to be taken when data reception is complete, such as processing the received data or signaling other parts of the application.
 *
 * @param[in] callback_fn The user-defined callback function to be registered. This function should match the
 *                        signature defined by `SENT_RECEIVE_COMPLETE_CALLBACK`.
 * @param[in] context     A user-defined context value that will be passed to the callback function when it is invoked.
 *                        This can be used to provide additional information or state to the callback function.
 *
 * @return     none 
 *
 * @note Ensure that the SENT instance is properly initialized and configured before calling this function.
 * The function does not perform any error checking related to the initialization state of the SENT instance.
 *
 * @b Example: 
 * @code
 * void MyReceiveCompleteCallback(uintptr_t context) {
 *     
 *     
 * }
 *
 *		SENT${SENT_INSTANCE}_Initialize();
 *      SENT${SENT_INSTANCE}_ReceiveCompleteCallbackRegister(MyReceiveCompleteCallback, (uintptr_t)myContext);
 * }
 * @endcode
 * @remarks     None  
 */
void SENT${SENT_INSTANCE}_ReceiveCompleteCallbackRegister(SENT_RECEIVE_COMPLETE_CALLBACK callback_fn, uintptr_t context);

/**
 * @brief      Registers a callback function to be called upon encountering an error during data reception for the SENT${SENT_INSTANCE} Peripheral
 * @details    This function registers a callback upon encountering an error during data reception. The callback function allows the user to define
 * custom actions to be taken when error occurs, such as processing the received data or signaling other parts of the application.
 *
 * @param[in] callback_fn The user-defined callback function to be registered. This function should match the
 *                        signature defined by `SENT_ERROR_CALLBACK`.
 * @param[in] context     A user-defined context value that will be passed to the callback function when it is invoked.
 *                        This can be used to provide additional information or state to the callback function.
 *
 * @return     none 
 *
 * @note Ensure that the SENT instance is properly initialized and configured before calling this function.
 * The function does not perform any error checking related to the initialization state of the SENT instance.
 *
 * @b Example:
 * @code
 * void MyErrorReceiveCompleteCallback(uintptr_t context) {
 *     
 *     
 * }
 *
 * 		SENT${SENT_INSTANCE}_Initialize();
 *      SENT${SENT_INSTANCE}_ReceiveCompleteCallbackRegister(MyReceiveCompleteCallback, (uintptr_t)myContext);
 * 
 * @endcode
 * @remarks     None  
 */
void SENT${SENT_INSTANCE}_ErrorCallbackRegister(SENT_ERROR_CALLBACK callback_fn, uintptr_t context);
</#if>

// /cond IGNORE_THIS
/* Provide C++ Compatibility */
#ifdef __cplusplus
 
    }
 
#endif
// /endcond

#endif  // SENT${SENT_INSTANCE}_H
/**
 End of File
*/
