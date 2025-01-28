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
 *              If configured to zero, the PLIB takes the UARTx clock frequency \ref ${moduleName}_FrequencyGet
 * @return      true  - Serial configuration was successful
 * @return      false - The specified serial configuration could not be supported. 
 *              This, for example, could happen if the requested baud is not supported.
 */
</#if>
bool ${moduleName}_SerialSetup( UART_SERIAL_SETUP *setup, uint32_t srcClkFreq );

<#if generateDoxygen>
/**
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
</#if>
bool ${moduleName}_Write( void *buffer, const size_t size );

<#if generateDoxygen>
/**
 * @brief       Submits a read buffer to the given UART peripheral to process
 * @pre         None
 * @param       buffer -	Pointer to the user buffer where received data will be placed.
 * @param       size -	Number of bytes to be received. 
 * @return      true - if the Read transaction is successful or if the requested size is 0.
 * @return      false - if the arguments are not valid or if the device is busy or if an error occurred while receiving data
 */
</#if>
bool ${moduleName}_Read( void *buffer, const size_t size );

<#if generateDoxygen>
/**
 * @brief    Gets the error of the given UART peripheral instance.
 * @pre      None
 * @param    None
 * @return   Errors occurred as listed by @enum UART_ERROR.
 */
</#if>
UART_ERROR ${moduleName}_ErrorGet( void );

<#if generateDoxygen>
/**
 * @brief       Auto-baud once enabled, this API will return the status
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

<#if intEnable == true>
<#if generateDoxygen>
/**
 * @brief       Checks if any current read request in progress
 * @pre         None
 * @param       None
 * @return      true - Read request is in progress. This happens when UARTx_Read is called previously.
 * @return      false - No read request is in progress.
 */
</#if>
bool ${moduleName}_ReadIsBusy( void );

<#if generateDoxygen>
/**
 * @brief       Returns number of data bytes loaded to data buffer from the read register
 * @pre         None
 * @param       None
 * @return      Number of data bytes available in the software buffer to read
 */
</#if>
size_t ${moduleName}_ReadCountGet( void );

<#if generateDoxygen>
/**
 * @brief       Disables the read operation and its interrupt if enabled
 * @pre         None
 * @param       None
 * @return      true - disabled the read operation
 */
</#if>
bool ${moduleName}_ReadAbort(void);

<#if generateDoxygen>
/**
 * @brief       Checks if any current write request in progress
 * @pre         None
 * @param       None
 * @return      true - Write request is in progress. This happens when UARTx_Write is called previously.
 * @return      false - No write request is in progress.
 */
</#if>
bool ${moduleName}_WriteIsBusy( void );

<#if generateDoxygen>
/**
 * @brief       Returns number of data bytes written from the transmit buffer to the transmit register
 * @pre         None
 * @param       None
 * @return      Number of data bytes written from the software buffer to transmit register
 */
</#if>
size_t ${moduleName}_WriteCountGet( void );

<#if generateDoxygen>
/**
 * @brief       Sets the pointer to the function and it's context to be called when the write events occur.
 * @pre         None
 * @param       callback	Pointer to the function to be called when the write transfer has completed. Setting this to NULL will disable the callback feature.
 * @param       context	    A value (usually a pointer) passed (unused) into the function identified by the callback parameter.
 * @return      None
 */
</#if>
void ${moduleName}_WriteCallbackRegister( UART_CALLBACK callback, uintptr_t context );

<#if generateDoxygen>
/**
 * @brief       Sets the pointer to the function and it's context to be called when the read events occur.
 * @pre         None
 * @param       callback	Pointer to the function that will be called when a read request has completed. Setting this to NULL will disable the callback feature.
 * @param       context	    A value (usually a pointer) passed (unused) into the function identified by the callback parameter.
 * @return      None
 */
</#if>
void ${moduleName}_ReadCallbackRegister( UART_CALLBACK callback, uintptr_t context );
<#else>

<#if generateDoxygen>
/**
 * @brief       Reads a byte of data
 * @pre         Receiver readiness must be confirmed using UARTx_ReceiverIsReady
 * @param       None
 * @return      Read byte data
 */
</#if>
int ${moduleName}_ReadByte( void );

<#if generateDoxygen>
/**
 * @brief       Returns the hardware status of the UART Receiver
 * @pre         None
 * @param       None
 * @return      true - Receive hardware FIFO has at least one data available to read
 * @return      false - Receive hardware FIFO is empty
 */
</#if>
bool ${moduleName}_ReceiverIsReady( void );

<#if generateDoxygen>
/**
 * @brief       Writes the data byte into transmit hardware buffer
 * @pre         Call UARTx_TransmitterIsReady to know the availability of space in FIFO
 * @param       data - Byte data to be written
 * @return      None
 */
</#if>
void ${moduleName}_WriteByte( int data );

<#if generateDoxygen>
/**
 * @brief       Checks if there is any empty space in hardware transmit buffer
 * @pre         None
 * @param       None
 * @return      true - transmit hardware FIFO has empty space to accept data.
 * @return      false - transmit hardware FIFO is full.
 */
</#if>
bool ${moduleName}_TransmitterIsReady( void );

</#if>
<#if generateDoxygen>
/**
 * @brief       Checks if no current transmission is in progress
 * @pre         None
 * @param       None
 * @return      true - Transmit is not in progress or complete
 * @return      false - Transmit is in progress
 */
</#if>
bool ${moduleName}_TransmitComplete( void );

// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// /endcond

#endif // PLIB_${moduleName}_H
