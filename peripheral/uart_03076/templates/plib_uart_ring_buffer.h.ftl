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

// Section: Included Files

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "plib_uart_common.h"

// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// /endcond

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
 *              If configured to zero, the PLIB takes the UARTx clock frequency 
 *              \ref ${moduleName}_FrequencyGet
 * @return      true  - Serial configuration was successful
 * @return      false - The specified serial configuration could not be supported. 
 *              This, for example, could happen if the requested baud is not supported.
 */
bool ${moduleName}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq );

/**
 * @ingroup  uart_plib
 * @brief    Gets the error of the given UART peripheral instance.
 * @pre      None
 * @param    None
 * @return   Errors occurred as listed in \ref UART_ERROR.
 */
UART_ERROR ${moduleName}_ErrorGet( void );

/**
 * @ingroup     uart_plib
 * @brief       Auto-baud once enabled, this API will retun the status
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

/**
 * @ingroup     uart_plib
 * @brief       Submits a write buffer to the given UART peripheral to transfer
 * @pre         None
 * @param       buffer - Pointer to the user buffer. This contains the data to be transferred.
 * @param       size - Number of bytes to be transferred. 
 * @return      The API returns the number of bytes actually copied. Depending on the space 
 *              available in the transmit buffer, the number of bytes copied may be less than or 
 *              equal to the requested size.
 */
size_t ${moduleName}_Write(uint8_t* pWrBuffer, const size_t size );

/**
 * @ingroup     uart_plib
 * @brief       Returns number of data bytes written from the transmit buffer to the transmit 
 *              register
 * @pre         None
 * @param       None
 * @return      Number of data bytes written from the software buffer to transmit register
 */
size_t ${moduleName}_WriteCountGet(void);

/**
 * @ingroup     uart_plib
 * @brief       This function returns the number of bytes of free space available 
 *              in the transmit buffer
 * @pre         None
 * @param       None
 * @return      The API returns the number of bytes of free space in the transmit buffer
 */
size_t ${moduleName}_WriteFreeBufferCountGet(void);

/**
 * @ingroup     uart_plib
 * @brief       This function returns the size of the transmit ring buffer, which is same as the 
 *              size of the transmit ring buffer configured in user interface
 * @pre         None
 * @param       None
 * @return      The API returns the size of the transmit ring buffer
 */
size_t ${moduleName}_WriteBufferSizeGet(void);

/**
 * @ingroup     uart_plib
 * @brief       Checks if no current transmission is in progress
 * @pre         None
 * @param       None
 * @return      true - Transmit is not in progress or complete
 * @return      false - Transmit is in progress
 */
bool ${moduleName}_TransmitComplete(void);

/**
 * @ingroup     uart_plib
 * @brief       This API allows the application to enable or disable transmit notifications. 
 *              Further the application can choose to get notified persistently until the 
 *              threshold condition is true.
 * @pre         None
 * @param       isEnabled - A true value turns on notification, false value turns off notification
 * @param       isPersistent -	A true value turns on persistent notification. 
 *                              A false value disables persistent notifications
 * @return      true - indicates notifications were previously enabled
 * @return      false - indicates notifications were previously disabled
 */
bool ${moduleName}_WriteNotificationEnable(bool isEnabled, bool isPersistent);

/**
 * @ingroup     uart_plib
 * @brief       This API allows the application to set a threshold level on the number of free 
 *              space available in the transmit buffer
 * @pre         None
 * @param       nBytesThreshold - Threshold value for free space in the transmit buffer 
 *              afterwhich a notification must be given
 * @return      None
 */
void ${moduleName}_WriteThresholdSet(uint32_t nBytesThreshold);

/**
 * @ingroup     uart_plib
 * @brief       Sets the pointer to the function and it's context to be called when the write 
 *              events occur.
 * @pre         None
 * @param       callback - Pointer to the function to be called when the write transfer 
 *              has completed. Setting this to NULL will disable the callback feature.             
 * @param       context - A value (usually a pointer) passed (unused) into the function 
 *              identified by the callback parameter.
 * @return      None
 */
void ${moduleName}_WriteCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context);

/**
 * @ingroup     uart_plib
 * @brief       Submits a read buffer to the given UART peripheral to process
 * @pre         None
 * @param       buffer - Pointer to the user buffer where received data will be placed.
 * @param       size - Number of bytes to be received. 
 * @return      Number of bytes read and loaded into software buffer 
 */
size_t ${moduleName}_Read(uint8_t* pRdBuffer, const size_t size);

/**
 * @ingroup     uart_plib
 * @brief       Returns the number of bytes available in the internal receive buffer of the PLIB
 * @pre         None
 * @param       None
 * @return      The API returns the number of bytes pending to be read out from the receive buffer
 */
size_t ${moduleName}_ReadCountGet(void);

/**
 * @ingroup     uart_plib
 * @brief       Returns the number of bytes of free space available in the internal receive buffer
 * @pre         None
 * @param       None
 * @return      The API returns the number of bytes of free space in the receive buffer
 */
size_t ${moduleName}_ReadFreeBufferCountGet(void);

/**
 * @ingroup     uart_plib
 * @brief       Returns the size of the receive ring buffer
 * @pre         None
 * @param       None
 * @return      The API returns the size of the receive ring buffer
 */
size_t ${moduleName}_ReadBufferSizeGet(void);

/**
 * @ingroup     uart_plib
 * @brief       This API lets the application turn the receive notifications on/off
 * @pre         None
 * @param       isEnable - A true value turns on notification, false value turns off notification
 * @param       isPersistent - A true value turns on persistent notifications 
 *                             A false value disables persistent notifications
 * @return      true - indicates notifications were previously enabled
 * @return      false - indicates notifications were prerviously disabled
 */
bool ${moduleName}_ReadNotificationEnable(bool isEnabled, bool isPersistent);

/**
 * @ingroup     uart_plib
 * @brief       This API allows the application to set a threshold level on the number of bytes 
                of data available in the receive buffer
 * @pre         None
 * @param       nBytesThreshold - Threshold value for number of bytes available in the receive 
 *              buffer after which a notification must be given
 * @return      None
 */
void ${moduleName}_ReadThresholdSet(uint32_t nBytesThreshold);

/**
 * @ingroup     uart_plib
 * @brief       Sets the pointer to the function and it's context to be called when the read events
 *              occur.
 * @pre         None
 * @param       callback - Pointer to the function that will be called when a read request has 
 *              completed. Setting this to NULL will disable the callback feature.
 * @param       context - A value (usually a pointer) passed (unused) into the function 
 *              identified by the callback parameter.
 * @return      None
 */
void ${moduleName}_ReadCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context);

// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// /endcond

#endif // PLIB_${moduleName}_H
