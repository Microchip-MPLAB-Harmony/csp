/*******************************************************************************
  SERCOM_SPI(SERIAL COMMUNICATION SERIAL PERIPHERAL INTERFACE) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_sercom_spi.h

  Summary
   SERCOM_SPI PLIB Local Header File.

  Description
    This file defines the interface to the SERCOM SPI peripheral library.
    This library provides access to and control of the associated
    peripheral instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef PLIB_SERCOM_SPI_COMMON_H  // Guards against multiple inclusion
#define PLIB_SERCOM_SPI_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

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
/* SPI Clock Phase

  Summary:
    Identifies SPI Clock Phase Options

  Description:
    This enumeration identifies possible SPI Clock Phase Options.

  Remarks:
    None.
*/

typedef enum
{
    /* Input data is valid on clock trailing edge and output data is ready on
       leading edge */
    SPI_CLOCK_PHASE_TRAILING_EDGE,

    /* Input data is valid on clock leading edge and output data is ready on
       trailing edge */
    SPI_CLOCK_PHASE_LEADING_EDGE

} SPI_CLOCK_PHASE;

// *****************************************************************************
/* SPI Clock Polarity

  Summary:
    Identifies SPI Clock Polarity Options

  Description:
    This enumeration identifies possible SPI Clock Polarity Options.

  Remarks:
    None.
*/

typedef enum
{
    /* The inactive state value of clock is logic level zero */
    SPI_CLOCK_POLARITY_IDLE_LOW ,

    /* The inactive state value of clock is logic level one */
    SPI_CLOCK_POLARITY_IDLE_HIGH

} SPI_CLOCK_POLARITY;

// *****************************************************************************
/* SPI Data Bits

  Summary:
    Identifies SPI bits per transfer

  Description:
    This enumeration identifies number of bits per SPI transfer.

  Remarks:
    For 9 bit mode, data should be right aligned in the 16 bit
    memory location.
*/

typedef enum
{
    /* 8 bits per transfer */
    SPI_DATA_BITS_8 ,

    /* 9 bits per transfer */
    SPI_DATA_BITS_9

} SPI_DATA_BITS;

// *****************************************************************************

/* SPI Errors

  Summary:
    Identifies SPI Errors.

  Description:
    This enumeration identifies the possible SPI Errors.

  Remarks:
    None.
*/

typedef enum
{
    /* SPI with out Error */
    SPI_ERROR_NONE= 0,

    /* SPI overflow error */
    SPI_ERROR_OVERFLOW = 4,

} SPI_ERROR;

// *****************************************************************************

/* SPI Transfer Setup Parameters

  Summary:
    Identifies the setup parameters which can be changed dynamically.

  Description
    This structure identifies the possible setup parameters for SPI
    which can be changed dynamically if needed.

  Remarks:
    None.

*/

typedef struct
{
    /* Baud Rate or clock frequency */
    uint32_t            baudRate;

    /* Clock Phase */
    SPI_CLOCK_PHASE     clockPhase;

    /* Clock Polarity */
    SPI_CLOCK_POLARITY  clockPolarity;

    /* Number of bits per transfer */
    SPI_DATA_BITS       dataBits;

} SPI_TRANSFER_SETUP;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* SPI CallBack Function Pointer

  Summary:
    Pointer to a SPI Call back function.

  Description:
    This data type defines the required function signature for the
    SPI event handling callback function. Application must register
    a pointer to an event handling function whose function signature (parameter
    and return value types) match the types specified by this function pointer
    in order to receive event calls back from the PLIB.

    The parameters and return values are described here and a partial example
    implementation is provided.

  Parameters:
    context         - Value identifying the context of the application that
                      registered the event handling function

  Returns:
    None.

  Example:
    <code>
    <code>
        SPI1_CallbackRegister(&APP_SPICallBack, NULL);
        void APP_SPICallBack(uintptr_t contextHandle)
        {
            if( SPI_ERROR_NONE == SPI1_ErrorGet())
            {
                Exchange was completed without error, do something else now.
            }
        }
    </code>

  Remarks:
        The context parameter contains the a handle to the client context,
    provided at the time the event handling function was registered using the
    SPIx_CallbackRegister function. This context handle value is
    passed back to the client as the "context" parameter. It can be any value
    (such as a pointer to the client's data) necessary to identify the client
    context or instance of the client that made the data exchange
    request.

    The event handler function executes in the PLIB's interrupt context. It is
    recommended of the application to not perform process intensive or blocking
    operations with in this function.
*/

typedef void (*SERCOM_SPI_CALLBACK)(uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Local SPI Object****
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* SPI Object

  Summary:
    Defines the data type for the data structures used for peripheral
    operations.

  Description:
    This may be for used for peripheral operations.

  Remarks:
    None.
*/

typedef struct
{
    /* Pointer to the transmitter buffer */
    void *                   txBuffer;

    /* Pointer to the received buffer */
    void *                   rxBuffer;

    size_t                   txSize;

    size_t                   rxSize;

    size_t                   dummySize;

    /* Size of the receive processed exchange size */
    size_t                   rxCount;

    /* Size of the transmit processed exchange size */
    size_t                   txCount;

    /* Exchange busy status of the SPI */
    bool                     transferIsBusy;

    /* SPI Event handler  */
    SERCOM_SPI_CALLBACK      callback;

    /* Context  */
    uintptr_t                context;

    uint32_t                 status;

} SPI_OBJECT;

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif //PLIB_SERCOM_SPI_COMMON_H
