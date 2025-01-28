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

<#if generateDoxygen>
/**
 * @brief    Initializes given instance of the UART peripheral
 * @pre      None
 * @param    None
 * @return   None
 */
</#if>
void ${moduleName}_Initialize( void );

<#if generateDoxygen>
/**
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
</#if>
bool ${moduleName}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq );

<#if generateDoxygen>
/**
 * @brief    Gets the error of the given UART peripheral instance.
 * @pre      None
 * @param    None
 * @return   Errors occurred as listed in \ref UART_ERROR.
 */
</#if>
UART_ERROR ${moduleName}_ErrorGet( void );

<#if generateDoxygen>
/**
 * @brief       Auto-baud once enabled, this API will retun the status
 * @pre         \ref ${moduleName}_AutoBaudSet has to be called before calling this function
 * @param       None
 * @return      true - if auto-baud is in-progress
 * @return      false - if auto-baud is not in-progress or complete
 */
</#if>
bool ${moduleName}_AutoBaudQuery( void );

<#if generateDoxygen>
/**
 * @brief       Sets the auto-baud detect mode. The auto-baud mode stays enabled until reception 
 *              of sync field (0x55)
 * @pre         None
 * @param       enable - Pass true to enable the auto-baud detect mode
 * @return      None
 */
</#if>
void ${moduleName}_AutoBaudSet( bool enable );

<#if generateDoxygen>
/**
 * @brief       Submits a write buffer to the given UART peripheral to transfer
 * @pre         None
 * @param       buffer - Pointer to the user buffer. This contains the data to be transferred.
 * @param       size - Number of bytes to be transferred. 
 * @return      The API returns the number of bytes actually copied. Depending on the space 
 *              available in the transmit buffer, the number of bytes copied may be less than or 
 *              equal to the requested size.
 */
</#if>
size_t ${moduleName}_Write(uint8_t* pWrBuffer, const size_t size );

<#if generateDoxygen>
/**
 * @brief       Returns number of data bytes written from the transmit buffer to the transmit 
 *              register
 * @pre         None
 * @param       None
 * @return      Number of data bytes written from the software buffer to transmit register
 */
</#if>
size_t ${moduleName}_WriteCountGet(void);

<#if generateDoxygen>
/**
 * @brief       This function returns the number of bytes of free space available 
 *              in the transmit buffer
 * @pre         None
 * @param       None
 * @return      The API returns the number of bytes of free space in the transmit buffer
 */
</#if>
size_t ${moduleName}_WriteFreeBufferCountGet(void);

<#if generateDoxygen>
/**
 * @brief       This function returns the size of the transmit ring buffer, which is same as the 
 *              size of the transmit ring buffer configured in user interface
 * @pre         None
 * @param       None
 * @return      The API returns the size of the transmit ring buffer
 */
</#if>
size_t ${moduleName}_WriteBufferSizeGet(void);

<#if generateDoxygen>
/**
 * @brief       Checks if no current transmission is in progress
 * @pre         None
 * @param       None
 * @return      true - Transmit is not in progress or complete
 * @return      false - Transmit is in progress
 */
</#if>
bool ${moduleName}_TransmitComplete(void);

<#if generateDoxygen>
/**
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
</#if>
bool ${moduleName}_WriteNotificationEnable(bool isEnabled, bool isPersistent);

<#if generateDoxygen>
/**
 * @brief       This API allows the application to set a threshold level on the number of free 
 *              space available in the transmit buffer
 * @pre         None
 * @param       nBytesThreshold - Threshold value for free space in the transmit buffer 
 *              afterwhich a notification must be given
 * @return      None
 */
</#if>
void ${moduleName}_WriteThresholdSet(uint32_t nBytesThreshold);

<#if generateDoxygen>
/**
 * @brief       Sets the pointer to the function and it's context to be called when the write 
 *              events occur.
 * @pre         None
 * @param       callback - Pointer to the function to be called when the write transfer 
 *              has completed. Setting this to NULL will disable the callback feature.             
 * @param       context - A value (usually a pointer) passed (unused) into the function 
 *              identified by the callback parameter.
 * @return      None
 */
</#if>
void ${moduleName}_WriteCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context);

<#if generateDoxygen>
/**
 * @brief       Submits a read buffer to the given UART peripheral to process
 * @pre         None
 * @param       buffer - Pointer to the user buffer where received data will be placed.
 * @param       size - Number of bytes to be received. 
 * @return      Number of bytes read and loaded into software buffer 
 */
</#if>
size_t ${moduleName}_Read(uint8_t* pRdBuffer, const size_t size);

<#if generateDoxygen>
/**
 * @brief       Returns the number of bytes available in the internal receive buffer of the PLIB
 * @pre         None
 * @param       None
 * @return      The API returns the number of bytes pending to be read out from the receive buffer
 */
</#if>
size_t ${moduleName}_ReadCountGet(void);

<#if generateDoxygen>
/**
 * @brief       Returns the number of bytes of free space available in the internal receive buffer
 * @pre         None
 * @param       None
 * @return      The API returns the number of bytes of free space in the receive buffer
 */
</#if>
size_t ${moduleName}_ReadFreeBufferCountGet(void);

<#if generateDoxygen>
/**
 * @brief       Returns the size of the receive ring buffer
 * @pre         None
 * @param       None
 * @return      The API returns the size of the receive ring buffer
 */
</#if>
size_t ${moduleName}_ReadBufferSizeGet(void);

<#if generateDoxygen>
/**
 * @brief       This API lets the application turn the receive notifications on/off
 * @pre         None
 * @param       isEnable - A true value turns on notification, false value turns off notification
 * @param       isPersistent - A true value turns on persistent notifications 
 *                             A false value disables persistent notifications
 * @return      true - indicates notifications were previously enabled
 * @return      false - indicates notifications were prerviously disabled
 */
</#if>
bool ${moduleName}_ReadNotificationEnable(bool isEnabled, bool isPersistent);

<#if generateDoxygen>
/**
 * @brief       This API allows the application to set a threshold level on the number of bytes 
                of data available in the receive buffer
 * @pre         None
 * @param       nBytesThreshold - Threshold value for number of bytes available in the receive 
 *              buffer after which a notification must be given
 * @return      None
 */
</#if>
void ${moduleName}_ReadThresholdSet(uint32_t nBytesThreshold);

<#if generateDoxygen>
/**
 * @brief       Sets the pointer to the function and it's context to be called when the read events
 *              occur.
 * @pre         None
 * @param       callback - Pointer to the function that will be called when a read request has 
 *              completed. Setting this to NULL will disable the callback feature.
 * @param       context - A value (usually a pointer) passed (unused) into the function 
 *              identified by the callback parameter.
 * @return      None
 */
</#if>
void ${moduleName}_ReadCallbackRegister( UART_RING_BUFFER_CALLBACK callback, uintptr_t context);

// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// /endcond

#endif // PLIB_${moduleName}_H
