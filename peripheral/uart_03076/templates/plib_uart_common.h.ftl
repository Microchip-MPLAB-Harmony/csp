/**
 * UART Generated PLIB Types Header File
 * 
 * @file      plib_uart_common.h
 *            
 * @defgroup  uart_plib uart_plib_doc
 *            
 * @brief     Universal Asynchronous Receiver Transmitter PLIB using dsPIC MCUs
 *
 * @skipline  Harmony Chip support Package Version  {core.libVersion}
 *            
 * @skipline  Device : {core.deviceName}
*/

//{core.disclaimer}

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
  @ingroup  uart_plib
  @brief    This macro defines the hardware receive FIFO depth
*/
#define UART_RXFIFO_DEPTH       (9U)

/** 
  @ingroup  uart_plib
  @brief    These macro defines the parity types supported 
*/
#define    UART_PARITY_NONE    (0x00U)
#define    UART_PARITY_EVEN    (0x02U)
#define    UART_PARITY_ODD     (0x04U)
/* Force the compiler to reserve 32-bit space for each enum */
#define    UART_PARITY_INVALID (0xFFFFFFFFU)
typedef uint32_t UART_PARITY;

/** 
  @ingroup  uart_plib
  @brief    These macro defines the data width types supported
*/
#define    UART_DATA_8_BIT   (0x00U)
#define    UART_DATA_7_BIT   (0x01U)
/* Force the compiler to reserve 32-bit memory for each enum */
#define    UART_DATA_INVALID (0xFFFFFFFFU)
typedef uint32_t UART_DATA;

/** 
  @ingroup  uart_plib
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
  @ingroup  uart_plib
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
  @ingroup  uart_plib
  @brief    These macro defines UART errors supported by PLIB
*/
#define    UART_ERROR_NONE      (0U)
#define    UART_ERROR_OVERRUN   (0x02U)
#define    UART_ERROR_FRAMING   (0x08U)
#define    UART_ERROR_PARITY    (0x04U)

typedef uint32_t UART_ERROR;

/** 
  @ingroup  uart_plib
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