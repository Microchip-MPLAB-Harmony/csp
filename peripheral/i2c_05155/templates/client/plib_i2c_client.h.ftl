<#assign showExample = false>
<#assign showDocument = true>
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

#ifndef PLIB_${moduleName}_CLIENT_H
#define PLIB_${moduleName}_CLIENT_H

// Section: Included Files

#include "plib_i2c_client_common.h"

// /cond IGNORE_THIS
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// /endcond

// Section: Interface Routines

<#if showDocument>
/** 
 * @brief           Initializes the instance of the I2C peripheral operating in I2C mode.
 * @description     This function initializes the given instance of the I2C peripheral as
 *                  configured by the user from the MHC.
 * @pre             None
 * @param           None
 * @returns         None
<#if showExample>
   @example
    <code>
        ${moduleName}_Initialize();
    </code>
</#if>
 * @remarks         Stops the I2C if it was already running and reinitializes it
 */
</#if>
void ${moduleName}_Initialize(void);

<#if showDocument>
/** 
 * @brief           De-initializes the instance of the I2C peripheral
 * @description     This function resets the used registers to POR values
 *                  configured by the user from the MHC.
 * @pre             None
 * @param           None
 * @returns         None
<#if showExample>
   @example
    <code>
        ${moduleName}_Deinitialize();
    </code>
</#if>
 */
</#if>
void ${moduleName}_Deinitialize(void);

<#if showDocument>
/**
 * @breif           Sets the pointer to the function (and it's context) to be called when the
 *                  given I2C's transfer events occur.
 *
 * @description     This function sets the pointer to a host function to be called "back" when
 *                  the given I2C's transfer events occur. It also passes a context value
 *                  (usually a pointer to a context structure) that is passed into the function
 *                  when it is called. The specified callback function will be called from the
 *                  peripheral interrupt context.
 *
 * @pre             ${moduleName}_Initialize must have been called for the associated
 *                  I2C instance.
 * @param           callback -      A pointer to a function with a calling signature defined by
 *                                  the I2C_CALLBACK data type. Setting this to NULL
 *                                  disables the callback feature.
 *                  contextHandle - A value (usually a pointer) passed (unused) into the
 *                                  function identified by the callback parameter.
 * @return          None.
<#if showExample>
 * @example:
    <code>
        Refer to the description of the I2C_CALLBACK data type for
        example usage.
    </code>
</#if>
 * @remarks         None
*/
</#if>
void ${moduleName}_CallbackRegister(I2C_CLIENT_CALLBACK callback, uintptr_t contextHandle);

<#if showDocument>
/**
 * @breif           Returns the Peripheral busy status.
 * 
 * @description     This function ture if the I2C ${moduleName}I2C module is busy with a
 *                  transfer. The application can use the function to check if I2C
 *                  ${moduleName}I2C module is busy before calling any of the data transfer
 *                  functions. The library does not allow a data transfer operation if another
 *                  transfer operation is already in progress.
 * @pre             ${moduleName}_Initialize must have been called for the
 *                  associated I2C instance.
 * @param           None.
 * @return          true - Busy.
 *                  false - Not busy.
<#if showExample>
 * @example:
 <
    <code>
        uint8_t myData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!'};

        wait for the current transfer to complete
        while(${moduleName}_IsBusy( ));

        perform the next transfer
        if(!${moduleName}_Write( SLAVE_ADDR, &myData[0], NUM_BYTES ))
        {
            error handling
        }

    </code>
</#if>
 * @remarks          None
*/
</#if>
bool ${moduleName}_IsBusy(void);

<#if showDocument>
/**
 * @breif       This function returns the I2C data byte
 * @description This function returns read data byte post address match
 * @pre         ${moduleName}_Initialize must have been called for the
 *              associated I2C instance.
 * @param       None.
 * @return      Returns one byte of data read from the receive register 
<#if showExample>
 * @example:
    <code>
    uint8_t readData;
    readData = ${moduleName}_ReadByte();
    </code>
</#if>
 * @remarks      None
*/
</#if>
uint8_t ${moduleName}_ReadByte(void);

<#if showDocument>
/**
 * @breif       Writes byte data
 * @description This function writes one byte of data into I2C bus
 * @pre         ${moduleName}_Initialize must have been called for the
 *              associated I2C instance.
 * @param       wrByte - byte data to be written
 * @return      None
<#if showExample>
 * @example:
    <code>
    uint8_t writeData = 'A';
    ${moduleName}_WriteByte(writeData);
    </code>
</#if>
 * @remarks      None
*/
</#if>
void ${moduleName}_WriteByte(uint8_t wrByte);

<#if showDocument>
/**
 * @breif       Read/Write request status   
 * @description This function returns if the request direction is read or write
 * @pre         ${moduleName}_Initialize must have been called for the
 *              associated I2C instance.
 * @param       wrByte - byte data to be written
 * @return      None
<#if showExample>
 * @example:
    <code>
    I2C_CLIENT_TRANSFER_DIR transferDir;
    bool APP_I2C_CLIENT_Callback ( I2C_CLIENT_TRANSFER_EVENT event, uintptr_t contextHandle )
    {
        bool isSuccess = true;
        switch(event)
        {
            case I2C_CLIENT_TRANSFER_EVENT_ADDR_MATCH:                           
                transferDir = I2C1_TransferDirGet();        
                break;    
            case I2C_CLIENT_TRANSFER_EVENT_RX_READY:
                // handle RX ready event by reading the received data
                break;
            case I2C_CLIENT_TRANSFER_EVENT_TX_READY:
                // handle TX ready event by writing data to I2C master
                break;                  
        }
    } 
    </code>
</#if>
 * @remarks      None
*/
</#if>
I2C_CLIENT_TRANSFER_DIR ${moduleName}_TransferDirGet(void);

<#if showDocument>
/**
 * @breif       Writes byte data
 * @description This function returns the ACK status of the last byte written to the I2C master
 * @pre         ${moduleName}_Initialize must have been called for the
 *              associated I2C instance.
 * @param       I2C_CLIENT_ACK_STATUS_RECEIVED_ACK - I2C master acknowledged the last byte 
 *              I2C_CLIENT_ACK_STATUS_RECEIVED_NAK - I2C master sent NAK 
 * @return      None
<#if showExample>
 * @example:
    <code>
    bool APP_I2C_CLIENT_Callback ( I2C_CLIENT_TRANSFER_EVENT event, uintptr_t contextHandle )
    {
        bool isSuccess = true;
        switch(event)
        {
            case I2C_CLIENT_TRANSFER_EVENT_ADDR_MATCH:                   
                transferDir = I2C1_TransferDirGet();
                break;
            case I2C_SLAVE_TRANSFER_EVENT_RX_READY:
                // handle RX ready event by reading the received data
                break;
            case I2C_CLIENT_TRANSFER_EVENT_TX_READY:
                if (I2C1_LastByteAckStatusGet() == I2C_CLIENT_ACK_STATUS_RECEIVED_ACK)
                {
                    // Last byte is ACK'd by I2C master. Continue writing more data.
                    I2C1_WriteByte(data);
                }
                else
                {
                    // Last byte is NAK'd by I2C master. Transfer complete.
                }
                break;                                      
        }
    }  
    </code>
</#if>
 * @remarks      None
*/
</#if>
I2C_CLIENT_ACK_STATUS ${moduleName}_LastByteAckStatusGet(void);

<#if showDocument>
/**
 * @breif       Returns the error occured during transfer.
 * @description This function returns the error during transfer.
 * @pre         ${moduleName}_Initialize must have been called for the
 *              associated I2C instance.
 * @param       None.
 * @return      Returns an I2C_CLIENT_ERROR type of status identifying the error that has
 *              occurred.
<#if showExample>
 * @example:
    <code>
    if(I2C_ERROR_NONE == ${moduleName}_ErrorGet())
    {
        I2C transfer is completed, go to next state.
    }
    </code>
</#if>
 * @remarks      None
*/
</#if>
I2C_CLIENT_ERROR ${moduleName}_ErrorGet(void);


// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// /endcond

#endif /* PLIB_${moduleName}_CLIENT_H */