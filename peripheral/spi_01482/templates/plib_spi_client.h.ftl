<#assign generateDoxygen = true>
/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SPI_INSTANCE_NAME?lower_case}_client.h

  Summary:
    ${SPI_INSTANCE_NAME} Client PLIB Header File

  Description:
    This file has prototype of all the interfaces provided for particular
    SPI peripheral.

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

#ifndef PLIB_${SPI_INSTANCE_NAME}_CLIENT_H
#define PLIB_${SPI_INSTANCE_NAME}_CLIENT_H

#include "device.h"
#include <stddef.h>
#include "plib_spi_client_common.h"

/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif


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
 *
 * @remarks None.
 */
</#if>
void ${SPI_INSTANCE_NAME}_Initialize (void);

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
 * - Perform SPI operations here
 * SPI1_Deinitialize();
 * @endcode
 *
 * @remarks None.
 */
</#if>
void ${SPI_INSTANCE_NAME}_Deinitialize ( void );

<#if generateDoxygen>
/**
 * @brief Reads data from the PLIB's internal buffer to the application buffer.
 *
 * @details This function reads "rxSize" number of bytes from the SPI module's internal buffer 
 * and copies them into the application's buffer specified by @p pRdBuffer. The function returns 
 * the actual number of bytes copied to the application buffer. If 16-bit or 32-bit modes are supported, 
 * the size and return value will be specified in terms of 16-bit or 32-bit words.
 *
 * The SPIx_ReadCountGet API can be used to determine the number of bytes available in the internal buffer. 
 * The application must call this API from the callback function to ensure proper handling of the 
 * received data.
 *
 * @pre 
 * - The SPIx_Initialize function must have been called.
 * - A callback must have been registered using the SPIx_CallbackRegister API to be notified when 
 *   the transfer is complete.
 *
 * @param[out] pRdBuffer Pointer to the buffer where the data from the PLIB's internal buffer will be copied.
 * @param[in]  rxSize    Number of bytes to copy. If 16-bit or 32-bit transfer modes are supported, 
 *                       this value must be specified in terms of 16-bit or 32-bit words.
 *
 * @return Returns the number of bytes (or words in 16-bit/32-bit mode) actually copied into the @p pRdBuffer.
 *
 * @b Example
 * @code
 * uint8_t APP_RxData[10];
 *
 * void SPIEventHandler(uintptr_t context)
 * {
 *     if (SPI1_ErrorGet() == SPI_CLIENT_ERROR_NONE)
 *     {
 *         - Read out the received data. This could be meaningful data if SPI master is
 *         - writing to client or it could be dummy data if SPI master is reading from client.
 *         - However, irrespective of whether client is expecting meaningful data or dummy
 *         - data from master, SPI client must always read out the data to clear the PLIB's
 *         - internal receive buffer.
 *
 *         appData.nBytesRead = SPI1_Read(APP_RxData, SPI1_ReadCountGet());
 *     }
 *     else
 *     {
 *         - Handle error
 *     }
 * }
 *
 * SPI1_CallbackRegister(SPIEventHandler, (uintptr_t)0);
 * @endcode
 *
 * @remarks None.
 */
</#if>
size_t ${SPI_INSTANCE_NAME}_Read(void* pRdBuffer, size_t size);

<#if generateDoxygen>
/**
 * @brief Writes data to the SPI peripheral.
 *
 * @details This function writes "txSize" number of bytes to the SPI module. The data pointed 
 * to by @p pWrBuffer is copied into the PLIB's internal buffer. The actual data transfer occurs 
 * when the SPI master initiates a transfer. Upon completion of the transfer, a registered 
 * callback function is invoked to notify the application.
 *
 * This function returns immediately after copying the data into the PLIB's internal buffer. 
 * The application must ensure that a callback is registered to receive a notification when the 
 * transfer completes.
 *
 * @pre
 * - The SPIx_Initialize function must have been called.
 * - A callback must have been registered using the SPIx_CallbackRegister API to be notified 
 *   upon transfer completion.
 *
 * @param[in] pWrBuffer Pointer to the buffer containing the data to be copied to the PLIB's internal buffer.
 * @param[in] txSize    Number of bytes to copy. If 16-bit or 32-bit transfer modes are supported, 
 *                      this value must be specified in terms of 16-bit or 32-bit words.
 *
 * @return Returns the number of bytes (or words in 16-bit/32-bit mode) actually copied into the 
 *         PLIB's internal buffer.
 *
 * @b Example
 * @code
 * uint8_t APP_TxData[4];
 * uint8_t APP_RxData[10];
 * size_t txSize = 4;
 *
 * void SPIEventHandler(uintptr_t context)
 * {
 *     if (SPI1_ErrorGet() == SPI_CLIENT_ERROR_NONE)
 *     {
 *         - Read out the received data. This could be meaningful data if SPI master is
 *         - writing to client or it could be dummy data if SPI master is reading from client.
 *         - However, irrespective of whether client is expecting meaningful data or dummy
 *         - data from master, SPI client must always read out the data to clear the PLIB's
 *         - internal receive buffer.
 *
 *         appData.nBytesRead = SPI1_Read(APP_RxData, SPI1_ReadCountGet());
 *     }
 *     else
 *     {
 *         - Handle error
 *     }
 * }
 *
 * SPI1_CallbackRegister(SPIEventHandler, (uintptr_t)0);
 * SPI1_Write(APP_TxData, txSize);
 * @endcode
 *
 * @remarks 
 * - This function returns immediately after copying data to the PLIB's internal buffer. 
 * - A data transfer is considered complete when the Chip Select line is driven to an inactive 
 *   state by the SPI master.
 */
</#if>
size_t ${SPI_INSTANCE_NAME}_Write(void* pWrBuffer, size_t size );

<#if generateDoxygen>
/**
 * @brief Returns the number of bytes pending to be read out from the PLIB's internal buffer.
 *
 * @details This function returns the number of unread bytes available in the SPI client PLIB's 
 * internal receive buffer. The application can call this API to determine the number of bytes 
 * available in the buffer before calling the SPIx_Read function to read the data. This allows 
 * the application to know how much data is available for reading.
 *
 * @pre The SPIx_Initialize function must have been called.
 *
 * @param[in] None
 *
 * @return Returns the number of bytes available in the PLIB's internal receive buffer. 
 *         If 16/32 bit modes are supported, the return value is specified in terms of 
 *         16/32 bit words.
 *
 * @b Example
 * @code
 * uint8_t APP_RxData[10];
 * size_t nBytesAvailable;
 * size_t nBytesRead;
 *
 * void SPIEventHandler(uintptr_t context)
 * {
 *     if (SPI1_ErrorGet() == SPI_CLIENT_ERROR_NONE)
 *     {
 *         - Get the number of unread bytes available in the internal buffer
 *         nBytesAvailable = SPI1_ReadCountGet();
 *         
 *         - Read the available data from the buffer
 *         nBytesRead = SPI1_Read(APP_RxData, nBytesAvailable);
 *     }
 *     else
 *     {
 *         - Handle error
 *     }
 * }
 *
 * SPI1_CallbackRegister(SPIEventHandler, (uintptr_t) 0);
 * @endcode
 *
 * @remarks None.
 */
</#if>
size_t ${SPI_INSTANCE_NAME}_ReadCountGet(void);

<#if generateDoxygen>
/**
 * @brief Returns the size of the PLIB's internal receive buffer.
 *
 * @details This function returns the size of the SPI PLIB's internal receive buffer. The 
 * receive buffer size is configured in the MCC (MPLAB Code Configurator) and will be the same 
 * as the configured value. This can be useful to determine the maximum capacity of the 
 * buffer before attempting data transfers.
 *
 * @pre None.
 *
 * @param[in] None
 *
 * @return Returns the size of the PLIB's internal receive buffer.
 *
 * @b Example
 * @code
 * size_t rxBufferSize;
 *
 * - Get the size of the internal receive buffer
 * rxBufferSize = SPI1_ReadBufferSizeGet();
 * @endcode
 *
 * @remarks None.
 */
</#if>
size_t ${SPI_INSTANCE_NAME}_ReadBufferSizeGet(void);

<#if generateDoxygen>
/**
 * @brief Returns the size of the PLIB's internal transmit buffer.
 *
 * @details This function returns the size of the SPI PLIB's internal transmit buffer. The 
 * transmit buffer size is configured in the MCC (MPLAB Code Configurator) and will be the same 
 * as the configured value. This can be useful to determine the maximum capacity of the 
 * buffer before attempting data transfers.
 *
 * @pre None.
 *
 * @param[in] None
 *
 * @return Returns the size of the PLIB's internal transmit buffer.
 *
 * @b Example
 * @code
 * size_t txBufferSize;
 *
 * - Get the size of the internal transmit buffer
 * txBufferSize = SPI1_WriteBufferSizeGet();
 * @endcode
 *
 * @remarks None.
 */
</#if>
size_t ${SPI_INSTANCE_NAME}_WriteBufferSizeGet(void);

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
 *                     by the `SPI_CALLBACK` or `SPI_CLIENT_CALLBACK` data type. 
 *                     Setting this to `NULL` disables the callback feature.
 * @param[in] context  A value (usually a pointer) that is passed into the callback 
 *                     function when it is invoked.
 *
 * @return None.
 *
 * @b Example
 *
 * @b SPI @b Master @b Mode @b (Non-blocking):
 * @code
 * uint8_t APP_RxData[10];
 * size_t nBytesAvailable;
 * size_t nBytesRead;
 * 
 * void SPIEventHandler(uintptr_t context )
 * {
 *     if (SPI1_ErrorGet() == SPI_CLIENT_ERROR_NONE)
 *     {
 *         nBytesAvailable = SPI1_ReadCountGet();
 * 
 *         nBytesRead = SPI1_Read(APP_RxData, nBytesAvailable);
 *     }
 *     else
 *     {
 *         - Handle error
 *     }
 * 
 * }
 * 
 * SPI1_CallbackRegister(SPIEventHandler, (uintptr_t) 0);
 * @endcode
 *
 * @remarks None.
 */
</#if>
void ${SPI_INSTANCE_NAME}_CallbackRegister(SPI_CLIENT_CALLBACK callBack, uintptr_t context );

<#if generateDoxygen>
/**
 * @brief Returns the status of the last SPI transfer.
 *
 * @details This function returns the error status of the last SPI transfer. The application 
 * must check the status of the transfer in the application callback and take appropriate action 
 * if there is an error during the data transfer. Calling this API clears the error status flags.
 *
 * @pre The SPIx_Initialize() function must have been called before calling this API.
 *
 * @param[in] None
 *
 * @return Returns the SPI client error status, indicating any issues during the last transfer.
 *         Possible return values are from the SPI_CLIENT_ERROR enumeration, including SPI_CLIENT_ERROR_NONE.
 *
 * @b Example
 * @code
 * void SPIEventHandler(uintptr_t context)
 * {
 *     if (SPI1_ErrorGet() == SPI_CLIENT_ERROR_NONE)
 *     {
 *         nBytesAvailable = SPI1_ReadCountGet();
 *         nBytesRead = SPI1_Read(APP_RxData, nBytesAvailable);
 *     }
 *     else
 *     {
 *         - Handle error
 *     }
 * }
 *
 * SPI1_CallbackRegister(SPIEventHandler, (uintptr_t) 0);
 * @endcode
 *
 * @remarks None.
 */
</#if>
SPI_CLIENT_ERROR ${SPI_INSTANCE_NAME}_ErrorGet(void);

<#if generateDoxygen>
/**
 * @brief Returns the transfer status of the SPI.
 *
 * @details In client mode, this function returns true if the SPI client is busy with a data transfer. 
 * The status is returned as true when the SPI chip select is driven to the active state by the SPI master. 
 * The status is returned as false when the SPI chip select is driven to the inactive state, indicating that 
 * the transfer is complete.
 *
 * @pre The SPIx_Initialize() function must have been called once, and the module should be configured 
 *      for interrupt mode operation in MCC.
 *
 * @param[in] None
 *
 * @return Returns true if the SPI transfer is in progress (in master mode) or if the chip select is in 
 *         the active state (in client mode). Returns false when the transfer is completed (in master mode) 
 *         or when the chip select is in the inactive state (in client mode).
 *
 * @b Example
 * @code
 * while (SPI1_IsBusy() == true)
 * {
 *     - Wait here till the chip select is asserted by the SPI master
 * }
 * @endcode
 *
 * @remarks None.
 */
</#if>
bool ${SPI_INSTANCE_NAME}_IsBusy(void);

<#if SPIS_USE_BUSY_PIN == true>
<#if generateDoxygen>
/**
 * @brief Drives the SPI client busy line to the ready (not busy) state.
 *
 * @details This function drives the SPI client's busy line to the ready (inactive) state. 
 * The busy line is driven to the active (busy) state when the chip select is asserted by the SPI master. 
 * Once the data transfer is complete and the chip select is deasserted, a callback is given to the application. 
 * The application can then parse the received data and prepare a response for the SPI master. 
 * Once the response is ready, the SPI client can call this function to release the busy line, 
 * indicating to the SPI master that the client is no longer busy. The SPI master must wait for the busy line 
 * to be inactive before initiating a new transfer.
 *
 * @pre The SPIx_Initialize() function must have been called.
 *
 * @param[in] None
 *
 * @return None
 *
 * @b Example
 * @code
 * uint8_t APP_TxData[10];
 * size_t nBytesRead;
 *
 * void SPIEventHandler(uintptr_t context )
 * {
 *     if (SPI1_ErrorGet() == SPI_CLIENT_ERROR_NONE)
 *     {
 *         nBytesRead = SPI1_Read(APP_RxData, SPI1_ReadCountGet());
 *         
 *         switch(APP_RxData[0])
 *         {
 *             case APP_CMD_WRITE:
 *                 - Keep the busy line asserted until write operation is complete
 *                 appData.status.busy = 1;
 *                 state = APP_STATE_WRITE;
 *                 break;
 *             case APP_CMD_READ:
 *                 - Provide the requested data and drive the busy line inactive
 *                 SPI1_Write(APP_TxData, 10);
 *                 break;
 *         }
 *         
 *         if (appData.status.busy == 0)
 *         {
 *             - Indicate to SPI Master that the client is ready for data transfer
 *             SPI1_Ready();
 *         }
 *     }
 * }
 * @endcode
 *
 * @remarks This API is available only if the Busy signal feature is enabled in MCC.
 */
</#if>
void ${SPI_INSTANCE_NAME}_Ready(void);
</#if>

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif

#endif // PLIB_${SPI_INSTANCE_NAME}_CLIENT_H
