/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}_common.h
 
  Summary:
    UART Common Header File
 
  Description:
    This file has prototype of all the interfaces which are common for all the
    UART peripherals.
 
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

#ifndef PLIB_UART_COMMON_H
#define PLIB_UART_COMMON_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

// /cond IGNORE_THIS
/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif
// /endcond

// Section: Common Definitions

/** 
  @brief    This macro defines the hardware receive FIFO depth
*/
#define UART_RXFIFO_DEPTH       (9U)

/** 
  @brief    These macro defines the parity types supported 
*/
#define    UART_PARITY_NONE    (0x00U)
#define    UART_PARITY_EVEN    (0x02U)
#define    UART_PARITY_ODD     (0x04U)
/* Force the compiler to reserve 32-bit space for each enum */
#define    UART_PARITY_INVALID (0xFFFFFFFFU)
typedef uint32_t UART_PARITY;

/** 
  @brief    These macro defines the data width types supported
*/
#define    UART_DATA_8_BIT   (0x00U)
#define    UART_DATA_7_BIT   (0x01U)
/* Force the compiler to reserve 32-bit memory for each enum */
#define    UART_DATA_INVALID (0xFFFFFFFFU)
typedef uint32_t UART_DATA;

/** 
  @brief    These macro defines the stop bit settings supported in the PLIB
*/
#define    UART_STOP_2_SENT_1_CHECKED   (0x03U)
#define    UART_STOP_2_SENT_2_CHECKED   (0x02U)
#define    UART_STOP_1_5_SENT_1_5_CHECKED   (0x01U)
#define    UART_STOP_1_SENT_1_CHECKED   (0x00U)
/* Force the compiler to reserve 32-bit memory for each enum */
#define    UART_STOP_INVALID  (0xFFFFFFFFU)
typedef uint32_t UART_STOP;

/** 
  @brief    Data type containing the serial settings used by UARTx_SerialSetup API
*/
typedef struct
{
    uint32_t baudRate;
    UART_PARITY parity;
    UART_DATA dataWidth;
    UART_STOP stopBits;
} UART_SERIAL_SETUP;

/** 
  @brief    These macro defines UART errors supported by PLIB
*/
#define    UART_ERROR_NONE      (0U)
#define    UART_ERROR_OVERRUN   (0x02U)
#define    UART_ERROR_FRAMING   (0x08U)
#define    UART_ERROR_PARITY    (0x04U)

typedef uint32_t UART_ERROR;

/** 
  @brief    Callback function prototype
*/
typedef void (* UART_CALLBACK)( uintptr_t context );

// /cond IGNORE_THIS
// Section: Local Objects **** Do Not Use ****

typedef struct
{
    void *                  txBuffer;
    size_t                  txSize;
    size_t                  txProcessedSize;
    UART_CALLBACK           txCallback;
    uintptr_t               txContext;
    bool                    txBusyStatus;
    void *                  rxBuffer;
    size_t                  rxSize;
    size_t                  rxProcessedSize;
    UART_CALLBACK           rxCallback;
    uintptr_t               rxContext;
    bool                    rxBusyStatus;
    volatile UART_ERROR     errors;

} UART_OBJECT ;

typedef enum
{
    /* Threshold number of bytes are available in the receive ring buffer */
    UART_EVENT_READ_THRESHOLD_REACHED = 0,
    /* Receive ring buffer is full. Application must read the data out to avoid missing data on the next RX interrupt. */
    UART_EVENT_READ_BUFFER_FULL,
    /* USART error. Application must call the UARTx_ErrorGet API to get the type of error and clear the error. */
    UART_EVENT_READ_ERROR,
    /* Threshold number of free space is available in the transmit ring buffer */
    UART_EVENT_WRITE_THRESHOLD_REACHED,
} UART_EVENT;

typedef void (* UART_RING_BUFFER_CALLBACK)(UART_EVENT event, uintptr_t context );

typedef struct
{
    UART_RING_BUFFER_CALLBACK                           wrCallback;
    uintptr_t                                           wrContext;
    uint32_t                                            wrInIndex;
    uint32_t                                            wrOutIndex;
    uint32_t                                            wrThreshold;
    bool                                                isWrNotificationEnabled;
    bool                                                isWrNotifyPersistently;
    uint32_t                                            wrBufferSize;
    UART_RING_BUFFER_CALLBACK                           rdCallback;
    uintptr_t                                           rdContext;
    uint32_t                                            rdInIndex;
    uint32_t                                            rdOutIndex;
    uint32_t                                            rdBufferSize;
    bool                                                isRdNotificationEnabled;
    uint32_t                                            rdThreshold;
    bool                                                isRdNotifyPersistently;
    UART_ERROR                                          errors;
} UART_RING_BUFFER_OBJECT;

// /endcond

// /cond IGNORE_THIS
/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif
// /endcond

#endif // PLIB_UART_COMMON_H

/*******************************************************************************
 End of File
*/