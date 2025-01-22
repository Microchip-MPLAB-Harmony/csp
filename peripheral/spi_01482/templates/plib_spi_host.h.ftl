<#assign generateDoxygen = true>
/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SPI_INSTANCE_NAME?lower_case}_host.h

  Summary:
    ${SPI_INSTANCE_NAME} Host PLIB Header File

  Description:
    This file has prototype of all the interfaces provided for particular
    SPI peripheral.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${SPI_INSTANCE_NAME}_HOST_H
#define PLIB_${SPI_INSTANCE_NAME}_HOST_H

#include "device.h"
#include <stddef.h>
#include "plib_spi_host_common.h"

/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif

// Section: Macro Definitions

/**
* @brief  This macro returns SPI clock frequency 
*/
#define ${SPI_INSTANCE_NAME}_FrequencyGet()    (uint32_t)(${SPI_Clock_Frequency}UL)

/****************************** ${SPI_INSTANCE_NAME} Interface *********************************/

<#if generateDoxygen>
/**
 * @brief Initializes the SPI peripheral of the device.
 *
 * @details This function initializes the SPI Peripheral Library (PLIB) of the device 
 * with the values configured in the MCC GUI. Once the peripheral is initialized, 
 * transfer APIs can be used to transfer the data.
 *
 * @pre MCC GUI should be configured with the correct values.
 *
 * @param None
 *
 * @return None
 *
 * @note This function must be called only once and before any other SPI function is called.
 *
 * @b Example
 * @code
 * SPI1_Initialize();
 * @endcode
 */
</#if>
void ${SPI_INSTANCE_NAME}_Initialize ( void );

<#if generateDoxygen>
/**
 * @brief Deinitializes the SPI peripheral of the device.
 *
 * @details This function deinitializes the SPI Peripheral Library (PLIB) of the device, 
 * returning the SPI peripheral to its default reset state. After calling this function, 
 * the SPI peripheral will no longer be operational, and any subsequent SPI operations 
 * will fail until re-initialization using the SPIx_Initialize API.
 *
 * @pre The SPI peripheral must have been initialized using the SPIx_Initialize API.
 *
 * @param None
 *
 * @return None
 *
 * @note This function should be called when the SPI peripheral is no longer required 
 * to release resources and ensure proper reset behavior.
 *
 * @b Example
 * @code
 * SPI1_Initialize();
 * SPI1_Deinitialize();
 * @endcode
 */
</#if>
void ${SPI_INSTANCE_NAME}_Deinitialize ( void );

<#if generateDoxygen>
/**
 * @brief Write and read data on the SPI peripheral.
 *
 * @details This function transmits "txSize" number of bytes and receives "rxSize" number 
 * of bytes on the SPI peripheral. Data pointed to by `pTransmitData` is transmitted, and 
 * received data is saved in the location pointed to by `pReceiveData`. The function 
 * transfers the maximum of "txSize" or "rxSize" data units until completion.
 *
 * - When **interrupts are disabled**, this function is blocking. It will not return 
 *   until all requested data has been transferred. Upon successful completion, the 
 *   function returns `true`.
 * - When **interrupts are enabled**, this function is non-blocking. It returns 
 *   immediately, while the transfer continues in the SPI interrupt. The transmit and 
 *   receive buffers are owned by the library until the transfer is complete. Only one 
 *   transfer is allowed at a time. Completion can be monitored using a callback function 
 *   or polling with `SPIx_IsBusy`.
 *
 * @note For non-blocking mode, a callback must be registered prior to calling this 
 * function if completion notifications are required.
 *
 * @pre The `SPIx_Initialize` function must have been called. If the SPI instance is 
 * configured for interrupt mode and callback is needed, it must be registered using 
 * `SPIx_CallbackRegister` before calling this function.
 *
 * @param[in] pTransmitData Pointer to the data to be transmitted. Set this to `NULL` 
 *                          if only data reception is needed. The size of this buffer 
 *                          should match `txSize`.
 * @param[in] txSize Number of bytes to be transmitted. This value is the byte size 
 *                   of the buffer, irrespective of 8/16/32-bit transfer mode.
 * @param[out] pReceiveData Pointer to the location where the received data is stored. 
 *                          Ensure sufficient memory is allocated for `rxSize` bytes. 
 *                          Set this to `NULL` if only data transmission is required.
 * @param[in] rxSize Number of bytes to be received. Must be at least the sum of 
 *                   `txSize` plus any additional bytes to receive. For example, 
 *                   if 3 bytes are transmitted and 10 bytes are to be received, 
 *                   `rxSize` must be 13.
 *
 * @return 
 * - `true`  - In blocking mode, all requested data was transmitted and received. 
 *             In non-blocking mode, the request was successfully accepted for processing.
 * - `false` - If both `pTransmitData` and `pReceiveData` are `NULL`, or both `txSize` 
 *             and `rxSize` are 0. It also returns `false` if `txSize` is non-zero but 
 *             `pTransmitData` is `NULL`, or `rxSize` is non-zero but `pReceiveData` 
 *             is `NULL`. In non-blocking mode, the function fails if a transfer is 
 *             already in progress.
 *
 * @b Example
 *
 * @b Non-blocking Mode:
 * @code
 * // Example of SPIx_WriteRead() in interrupt mode with a callback function.
 *
 * uint8_t txBuffer[4];
 * uint8_t rxBuffer[10];
 * size_t txSize = 4;
 * size_t rxSize = 10;
 *
 * void APP_SPITransferHandler(uintptr_t context)
 * {
 *     // Transfer completed without error; take appropriate action.
 * }
 *
 * SPI1_Initialize();
 * SPI1_CallbackRegister(&APP_SPITransferHandler, (uintptr_t)NULL);
 *
 * if (SPI1_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize))
 * {
 *     - Request accepted successfully.
 * }
 * else
 * {
 *     - Request not accepted; retry with correct arguments.
 * }
 * @endcode
 *
 * @b Blocking Mode:
 * @code
 * // Example of SPIx_WriteRead() in blocking mode (non-interrupt).
 *
 * uint8_t txBuffer[4];
 * uint8_t rxBuffer[10];
 * size_t txSize = 4;
 * size_t rxSize = 10;
 *
 * SPI1_Initialize();
 *
 * - This call blocks until the transfer completes.
 * SPI1_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize);
 * @endcode
 *
 * @remarks None.
 */
</#if>
bool ${SPI_INSTANCE_NAME}_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize);

<#if generateDoxygen>
/**
 * @brief Writes data to the SPI peripheral.
 *
 * @details This function writes "txSize" number of bytes to the SPI peripheral. The data 
 * pointed to by `pWrBuffer` is transmitted. 
 *
 * - When **interrupts are disabled**, the function is blocking. It will not return 
 *   until all the requested data has been transmitted. Upon successful completion, 
 *   the function returns `true`.
 * - When **interrupts are enabled**, the function is non-blocking. It returns 
 *   immediately, and the data transfer continues in the SPI peripheral interrupt. 
 *   The application-specified transmit buffer is owned by the library until the transfer 
 *   is complete. The buffer should not be modified by the application during this period.
 *
 * Only one transfer is allowed at any time. Transfer completion can be monitored 
 * using a callback function (registered before calling `SPIx_Write()`) or by polling 
 * the `SPIx_IsBusy()` function.
 *
 * @pre The `SPIx_Initialize` function must have been called.
 *
 * @note For SPI host mode, if interrupts are enabled and transfer completion needs 
 * to be communicated back to the application, a callback must be registered using 
 * `SPIx_CallbackRegister()` prior to calling this function.
 *
 * @param[in] pWrBuffer Pointer to the buffer containing the data to be transmitted. 
 *                      In **interrupt mode**, this buffer should not be modified 
 *                      after calling the function and before the callback function 
 *                      has been executed or `SPIx_IsBusy()` returns `false`.
 * @param[in] txSize Number of bytes to be transmitted. This value is the byte size 
 *                   of the buffer, irrespective of 8/16/32-bit transfer mode.
 *
 * @return 
 * - `true`  - If configured for non-interrupt mode, the requested data was successfully 
 *             transmitted. If configured for interrupt mode, the transfer request was 
 *             accepted and will be processed in the interrupt.
 * - `false` - If `pWrBuffer` is `NULL` or `txSize` is 0. In interrupt mode, the function 
 *             also returns `false` if a transfer is already in progress.
 *
 * @b Example
 * @code
 * uint8_t txBuffer[4];
 * size_t txSize = 4;
 *
 * void APP_SPITransferHandler(uintptr_t context)
 * {
 *     - Transfer completed successfully; take appropriate action.
 * }
 *
 * SPI1_Initialize();
 * SPI1_CallbackRegister(&APP_SPITransferHandler, (uintptr_t)NULL);
 *
 * if (SPI1_Write(&txBuffer, txSize))
 * {
 *     - Request accepted successfully.
 * }
 * else
 * {
 *     - Request not accepted; retry with correct arguments.
 * }
 * @endcode
 * @remarks None.
 */
</#if>
bool ${SPI_INSTANCE_NAME}_Write(void* pTransmitData, size_t txSize);

<#if generateDoxygen>
/**
 * @brief Reads data on the SPI peripheral.
 *
 * @details This function reads "rxSize" number of bytes from the SPI peripheral. The 
 * received data is stored in the buffer pointed to by `pRdBuffer`.
 *
 * - When **interrupts are disabled**, the function is blocking and will not return 
 *   until all the requested data has been received. Upon successful completion, 
 *   the function returns `true`.
 * - When **interrupts are enabled**, the function is non-blocking and returns 
 *   immediately. The data transfer continues in the SPI peripheral interrupt. 
 *   The receive buffer provided to the function is owned by the PLIB until the 
 *   transfer is complete and must not be modified by the application.
 *
 * Only one transfer is allowed at any time. Transfer completion can be monitored 
 * using a callback function (registered before calling `SPIx_Read()`) or by polling 
 * the `SPIx_IsBusy()` function.
 *
 * @pre The `SPIx_Initialize` function must have been called.
 *
 * @note If interrupts are enabled, a callback must be registered using 
 * `SPIx_CallbackRegister()` to receive transfer completion status.
 *
 * @param[out] pRdBuffer Pointer to the buffer where the received data will be stored. 
 *                       In **interrupt mode**, this buffer must not be modified 
 *                       until the transfer is complete and the callback has been called 
 *                       or `SPIx_IsBusy()` returns `false`.
 * @param[in] rxSize Number of bytes to be received. This value is the byte size 
 *                   of the buffer, irrespective of 8/16/32-bit transfer mode.
 *
 * @return 
 * - `true`  - If configured for non-interrupt mode, the requested data has been received. 
 *             If configured for interrupt mode, the transfer request was accepted 
 *             successfully and will be processed in the interrupt.
 * - `false` - If `pRdBuffer` is `NULL` or `rxSize` is 0. In interrupt mode, the function 
 *             also returns `false` if a transfer is already in progress.
 *
 * @b Example
 *
 * @b SPI @b Read @b Example:
 * @code
 * uint8_t rxBuffer[10];
 * size_t rxSize = 10;
 *
 * void SPIEventHandler(uintptr_t context)
 * {
 *     - Transfer was completed successfully; take appropriate action.
 * }
 *
 * SPI1_Initialize();
 * SPI1_CallbackRegister(SPIEventHandler, (uintptr_t)0);
 *
 * if (SPI1_Read(&rxBuffer, rxSize))
 * {
 *     - Request was accepted successfully.
 * }
 * else
 * {
 *     - Request was not accepted; retry with correct arguments.
 * }
 * @endcode
 *
 * @remarks None.
 */
</#if>
bool ${SPI_INSTANCE_NAME}_Read(void* pReceiveData, size_t rxSize);

<#if generateDoxygen>
/**
 * @brief Configures SPI operational parameters at runtime.
 *
 * @details This function allows the application to change the SPI operational parameters 
 * at runtime. The application can thus override the MCC-defined configuration for these 
 * parameters. The parameters are specified via the `SPI_TRANSFER_SETUP` structure. 
 * Each member of this structure should be initialized to the desired value.
 *
 * This function is particularly useful in scenarios where multiple SPI slaves are 
 * connected on the same SPI bus, each requiring different operational parameters. 
 * The function can configure the SPI Host to meet the communication needs of the 
 * current SPI slave. 
 *
 * @note Calling this function will affect any ongoing communication. The application 
 * must ensure that there is no ongoing communication on the SPI before calling this function.
 *
 * @pre SPI must first be initialized using `SPIx_Initialize()`.
 *
 * @param[in] setup Pointer to a `SPI_TRANSFER_SETUP` structure containing the operational 
 *                  parameters. Each parameter must be specified, even if the parameter 
 *                  does not need to change.
 * @param[in] spiSourceClock SPI peripheral clock source frequency. If configured to 0, 
 *                           the PLIB takes the peripheral clock frequency from MCC.
 *
 * @return 
 * - `true`  - Setup was successful.
 * - `false` - Setup failed because the `spiSourceClock` and SPI clock frequencies 
 *             result in a baud rate that is out of the valid range.
 *
 * @b Example
 * @code
 * SPI_TRANSFER_SETUP setup;
 * setup.clockFrequency = 1000000;
 * setup.clockPhase = SPI_CLOCK_PHASE_TRAILING_EDGE;
 * setup.clockPolarity = SPI_CLOCK_POLARITY_IDLE_LOW;
 * setup.dataBits = SPI_DATA_BITS_8;
 *
 * - Assuming 30 MHz as peripheral input clock frequency
 * if (SPI1_TransferSetup(&setup, 30000000) == false)
 * {
 *     - This means setup could not be done, debug the reason.
 * }
 * @endcode
 *
 * @note The application needs to call this function only if the operational parameters 
 * need to differ from those configured in MCC.
 */
</#if>
bool ${SPI_INSTANCE_NAME}_TransferSetup (SPI_TRANSFER_SETUP *setup, uint32_t spiSourceClock);

<#if generateDoxygen>
/**
 * @brief Returns the transfer status of the SPI peripheral.
 *
 * @details This function returns the current transfer status of the last 
 * successful Write or Read request on the SPI peripheral. It can be used to check 
 * whether the SPI peripheral is still busy with a transfer or if the transfer 
 * has been completed.
 *
 * @pre None.
 *
 * @param None.
 *
 * @return Returns the current transfer status:
 * - `true`  - Transfer is still in progress.
 * - `false` - Transfer is completed.
 *
 * @b Example
 *
 * @code
 * - Check if the SPI transfer has completed
 * if (SPI1_IsTransmitterBusy() == false)
 * {
 *     - Data Transfer is complete, perform the next operation
 * }
 * @endcode
 *
 * @remarks None.
 */
</#if>
bool ${SPI_INSTANCE_NAME}_IsTransmitterBusy (void);

<#if SPI_INTERRUPT_MODE == true>
<#if generateDoxygen>
/**
 * @brief Returns the transfer status of the SPI peripheral.
 *
 * @details In **host mode**, this function returns `true` if the SPI peripheral 
 * is busy with a transfer. The application can use this function to check the 
 * SPI peripheral status before initiating another data transfer operation. 
 *
 * The library does not allow a data transfer operation to start if another transfer 
 * operation is already in progress.
 *
 * This function can be used as an alternative to the callback function when the library 
 * operates in interrupt mode, allowing the application to implement a synchronous interface.
 *
 * @pre The `SPIx_Initialize()` function must have been called, and the SPI peripheral 
 * must have been configured for **interrupt mode** operation in MCC.
 *
 * @param None
 *
 * @return 
 * - `true`  - Transfer is currently in progress (**host mode**) or the chip select 
 *             is in an active state (**slave mode**).
 * - `false` - Transfer is completed (**host mode**) or the chip select is in 
 *             an inactive state (**slave mode**).
 *
 * @b Example
 *
 * @b SPI @b Transfer @b Status @b Example:
 * @code
 * uint8_t dataBuffer[20];
 *
 * SPI1_Initialize();
 * SPI1_Write(dataBuffer, 20);
 *
 * while (SPI1_IsBusy() == true)
 * {
 *     - Wait here until the transfer is complete.
 * }
 * @endcode
 *
 * @remarks None.
 */
</#if>
bool ${SPI_INSTANCE_NAME}_IsBusy(void);

<#if generateDoxygen>
/**
 * @brief Registers a callback function for SPI transfer completion events.
 *
 * @details This function allows the application to register a callback function 
 * that the PLIB will call when a requested data transfer operation has completed. 
 *
 * The function also allows the application to specify a context value 
 * (usually a pointer to a structure or data) that is passed into the callback 
 * function when it is executed. The registered callback will be invoked 
 * from the peripheral interrupt context. Therefore, the callback function should 
 * be lightweight and quick.
 *
 * The callback function must be registered before initiating any transfer operation.
 *
 * @pre The `SPIx_Initialize()` function must have been called. 
 * This function is only available if the library is configured for **interrupt mode**.
 *
 * @param[in] callback A pointer to a function with a calling signature defined 
 *                     by the `SPI_CALLBACK` or `SPI_SLAVE_CALLBACK` data type. 
 *                     Setting this to `NULL` disables the callback feature.
 * @param[in] context  A value (usually a pointer) that is passed into the callback 
 *                     function when it is invoked.
 *
 * @return None.
 *
 * @b Example
 *
 * @b SPI Host Mode(Non-blocking):
 * @code
 * uint8_t txBuffer[4];
 * uint8_t rxBuffer[10];
 * size_t txSize = 4;
 * size_t rxSize = 10;
 * bool reqAccepted;
 *
 * void APP_SPITransferHandler(uintptr_t context)
 * {
 * 
 * }
 *
 * SPI1_Initialize();
 * SPI1_CallbackRegister(&APP_SPITransferHandler, (uintptr_t)NULL);
 *
 * if (SPI1_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize))
 * {
 *     
 * }
 * else
 * {
 *     
 * }
 * @endcode
 *
 * @remarks None.
 */
</#if>
void ${SPI_INSTANCE_NAME}_CallbackRegister(SPI_CALLBACK callback, uintptr_t context);
</#if>

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif

#endif // PLIB_${SPI_INSTANCE_NAME}_HOST_H
