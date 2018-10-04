/*******************************************************************************
  SERCOM Universal Synchronous/Asynchronous Receiver/Transmitter PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_sercom_usart.h

  Summary
    Data Type definition of the USART Peripheral Interface Plib.

  Description
    This file defines the Data Types for the USART Plib.

  Remarks:
    None.
*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

// DOM-IGNORE-END

#ifndef PLIB_SERCOM_USART_COMMON_H // Guards against multiple inclusion
#define PLIB_SERCOM_USART_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* USART Errors

  Summary:
    Defines the data type for the USART peripheral errors.

  Description:
    This may be used to check the type of error occurred with the USART
    peripheral during error status.

  Remarks:
    None.
*/

typedef enum
{
    /* Error status when no error has occurred */
    USART_ERROR_NONE,

    /* Error status when parity error has occurred */
    USART_ERROR_PARITY = SERCOM_USART_STATUS_PERR_Msk,

    /* Error status when framing error has occurred */
    USART_ERROR_FRAMING = SERCOM_USART_STATUS_FERR_Msk,

    /* Error status when overrun error has occurred */
    USART_ERROR_OVERRUN = SERCOM_USART_STATUS_BUFOVF_Msk

} USART_ERROR;

// *****************************************************************************
/* Callback Function Pointer

  Summary:
    Defines the data type and function signature for the USART peripheral
    callback function.

  Description:
    This data type defines the function signature for the USART peripheral
    callback function. The USART peripheral will call back the client's
    function with this signature when the USART buffer event has occurred.

  Remarks:
    None.
*/

typedef void (*SERCOM_USART_CALLBACK)( uintptr_t context );

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* USART Serial Configuration

  Summary:
    Defines the data type for the USART serial configurations.

  Description:
    This may be used to set the serial configurations for USART.

  Remarks:
    None.
*/

typedef struct
{
    /*  Baud rate value */
    uint32_t baud;

    /* Value can be 5, 6, 7, 8, 9 */
    uint8_t  charSize;

    /* Separating out the parity enable as a serial parameter */
    bool     parityEnable;

    /* 0 -even parity 1 - odd parity. Only valid if parity enable is true */
    uint8_t  parity;

    /* One or two stop bits */
    uint8_t  stopBits;      // 1 or 2

} USART_SERIAL_SETUP;

// *****************************************************************************
/* SERCOM USART Object

  Summary:
    Defines the data type for the data structures used for
    peripheral operations.

  Description:
    This may be for used for peripheral operations.

  Remarks:
    None.
*/

typedef struct
{
    volatile uint8_t *                   txBuffer;
    volatile size_t                      txSize;
    volatile size_t                      txProcessedSize;
    SERCOM_USART_CALLBACK                txCallback;
    volatile uintptr_t                   txContext;
    volatile bool                        txBusyStatus;

    volatile uint8_t *                   rxBuffer;
    volatile size_t                      rxSize;
    volatile size_t                      rxProcessedSize;
    SERCOM_USART_CALLBACK                rxCallback;
    volatile uintptr_t                   rxContext;
    volatile bool                        rxBusyStatus;

} SERCOM_USART_OBJECT ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif //PLIB_SERCOM_USART_COMMON_H
