/**
 * ${moduleName} Generated PLIB Header File
 * 
 * @file      plib_${moduleName?lower_case}.h
 *            
 * @ingroup   uart_plib
 *            
 * @brief     This is the generated plib header file for the ${moduleName}
 *
 * @skipline  Harmony Chip support Package Version  {core.libVersion}
 *            
 * @skipline  Device : {core.deviceName}
*/

//{core.disclaimer}

#ifndef PLIB_${moduleName}_H
#define PLIB_${moduleName}_H

// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// /endcond

// Section: Included Files

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "plib_uart_common.h"

// Section: Macro Definitions

#define ${moduleName}_FrequencyGet()    (uint32_t)(${uartClkFreq}UL)

// Section: ${moduleName} PLIB Routines

/**
 * @ingroup  uart_plib
 * @brief    Initializes given instance of the UART peripheral
 * @pre      None
 * @param    None
 * @return   None
 */
void ${moduleName}_Initialize( void );

/**
 * @ingroup     uart_plib
 * @brief       Writes data to the given UART peripheral instance
 * @pre         None
 * @param[in]   serialSetup - Pointer to serial configuration data structure
 * @param[in]   clkFrequency - Input clock frequency to the Baud Rate Generator. 
 *              If configured to zero, the PLIB takes the UARTx clock frequency \ref ${moduleName}_FrequencyGet
 * @return      true  - Serial configuration was successful
 * @return      false - The specified serial configuration could not be supported. 
 *              This, for example, could happen if the requested baud is not supported.
 */
bool ${moduleName}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq );

/**
 * @ingroup     uart_plib
 * @brief       Submits a write buffer to the given UART peripheral to transfer
 * @pre         None
 * @param       buffer - Pointer to the user buffer. This contains the data to be transferred.
 * @param       size - Number of bytes to be transferred. 
 * @return[Blocking mode] true - Specified number of bytes were transferred successfully or if 
 *                        the size requested is 0
 * @return[Blocking mode] false - Arguments are not valid
 * @return[Non-blocking mode] true - Request was placed successfully (in interrupt mode) or if 
 *                        the specified number of bytes were transferred or if the size requested is 0
 * @return[Non-blocking mode] false - Arguments are not valid or if the peripheral is busy with 
 *                        another request.
 */
bool ${moduleName}_Write( void *buffer, const size_t size );

/**
 * @ingroup     uart_plib
 * @brief       Submits a read buffer to the given UART peripheral to process
 * @pre         None
 * @param       buffer -	Pointer to the user buffer where received data will be placed.
 * @param       size -	Number of bytes to be received. 
 * @return      true - if the Read transaction is successful or if the requested size is 0.
 * @return      false - if the arguments are not valid or if the device is busy or if an error occurred while receiving data
 */
bool ${moduleName}_Read( void *buffer, const size_t size );

/**
 * @ingroup  uart_plib
 * @brief    Gets the error of the given UART peripheral instance.
 * @pre      None
 * @param    None
 * @return   Errors occurred as listed by @enum UART_ERROR.
 */
UART_ERROR ${moduleName}_ErrorGet( void );

/**
 * @ingroup     uart_plib
 * @brief       Auto-baud once enabled, this API will return the status
 * @pre         \ref ${moduleName}_AutoBaudSet has to be called before calling this function
 * @param       None
 * @return      true - if auto-baud is in-progress
 * @return      false - if auto-baud is not in-progress or complete
 */
bool ${moduleName}_AutoBaudQuery( void );

/**
 * @ingroup     uart_plib
 * @brief       Sets the auto-baud detect mode. The auto-baud mode stays enabled until reception 
 *              of sync field (0x55)
 * @pre         None
 * @param       enable - Pass true to enable the auto-baud detect mode
 * @return      None
 */
void ${moduleName}_AutoBaudSet( bool enable );

<#if intEnable == true>
/**
 * @ingroup     uart_plib
 * @brief       Checks if any current read request in progress
 * @pre         None
 * @param       None
 * @return      true - Read request is in progress. This happens when UARTx_Read is called previously.
 * @return      false - No read request is in progress.
 */
bool ${moduleName}_ReadIsBusy( void );

/**
 * @ingroup     uart_plib
 * @brief       Returns number of data bytes loaded to data buffer from the read register
 * @pre         None
 * @param       None
 * @return      Number of data bytes available in the software buffer to read
 */
size_t ${moduleName}_ReadCountGet( void );

/**
 * @ingroup     uart_plib
 * @brief       Disables the read operation and its interrupt if enabled
 * @pre         None
 * @param       None
 * @return      true - disabled the read operation
 */
bool ${moduleName}_ReadAbort(void);

/**
 * @ingroup     uart_plib
 * @brief       Checks if any current write request in progress
 * @pre         None
 * @param       None
 * @return      true - Write request is in progress. This happens when UARTx_Write is called previously.
 * @return      false - No write request is in progress.
 */
bool ${moduleName}_WriteIsBusy( void );

/**
 * @ingroup     uart_plib
 * @brief       Returns number of data bytes written from the transmit buffer to the transmit register
 * @pre         None
 * @param       None
 * @return      Number of data bytes written from the software buffer to transmit register
 */
size_t ${moduleName}_WriteCountGet( void );

/**
 * @ingroup     uart_plib
 * @brief       Sets the pointer to the function and it's context to be called when the write events occur.
 * @pre         None
 * @param       callback	Pointer to the function to be called when the write transfer has completed. Setting this to NULL will disable the callback feature.
 * @param       context	    A value (usually a pointer) passed (unused) into the function identified by the callback parameter.
 * @return      None
 */
void ${moduleName}_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context );

/**
 * @ingroup     uart_plib
 * @brief       Sets the pointer to the function and it's context to be called when the read events occur.
 * @pre         None
 * @param       callback	Pointer to the function that will be called when a read request has completed. Setting this to NULL will disable the callback feature.
 * @param       context	    A value (usually a pointer) passed (unused) into the function identified by the callback parameter.
 * @return      None
 */
void ${moduleName}_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context );
<#else>

/**
 * @ingroup     uart_plib
 * @brief       Reads a byte of data
 * @pre         Receiver readiness must be confirmed using UARTx_ReceiverIsReady
 * @param       None
 * @return      Read byte data
 */
int ${moduleName}_ReadByte( void );

/**
 * @ingroup     uart_plib
 * @brief       Returns the hardware status of the UART Receiver
 * @pre         None
 * @param       None
 * @return      true - Receive hardware FIFO has at least one data available to read
 * @return      false - Receive hardware FIFO is empty
 */
bool ${moduleName}_ReceiverIsReady( void );

/**
 * @ingroup     uart_plib
 * @brief       Writes the data byte into transmit hardware buffer
 * @pre         Call UARTx_TransmitterIsReady to know the availability of space in FIFO
 * @param       data - Byte data to be written
 * @return      None
 */
void ${moduleName}_WriteByte( int data );

/**
 * @ingroup     uart_plib
 * @brief       Checks if there is any empty space in hardware transmit buffer
 * @pre         None
 * @param       None
 * @return      true - transmit hardware FIFO has empty space to accept data.
 * @return      false - transmit hardware FIFO is full.
 */
bool ${moduleName}_TransmitterIsReady( void );

</#if>
/**
 * @ingroup     uart_plib
 * @brief       Checks if no current transmission is in progress
 * @pre         None
 * @param       None
 * @return      true - Transmit is not in progress or complete
 * @return      false - Transmit is in progress
 */
bool ${moduleName}_TransmitComplete( void );

// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// /endcond

#endif // PLIB_${moduleName}_H
