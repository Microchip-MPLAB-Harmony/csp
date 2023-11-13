/*******************************************************************************
  SERCOM_SPI(SERIAL COMMUNICATION SERIAL PERIPHERAL INTERFACE) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_sercom_spi_slave_common.h

  Summary
   SERCOM SPI Slave common definitions file

  Description
    This file defines the definitions for the SERCOM SPI slave interface.
    This library provides access to and control of the associated
    peripheral instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_SERCOM_SPI_SLAVE_COMMON_H  // Guards against multiple inclusion
#define PLIB_SERCOM_SPI_SLAVE_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include <device.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section:Preprocessor macros
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* SPI slave Error convenience macros */
// *****************************************************************************
// *****************************************************************************
/* Error status when no error has occurred */
#define SPI_SLAVE_ERROR_NONE 0U

/* Buffer overflow error has occured */
#define SPI_SLAVE_ERROR_BUFOVF SERCOM_SPIS_STATUS_BUFOVF_Msk

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* SPI Slave Errors

  Summary:
    Defines the data type for the SPI Slave mode errors

  Description:
    This may be used to check the type of error occurred

  Remarks:
    None
*/
typedef uint32_t SPI_SLAVE_ERROR;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* SPI Slave Mode CallBack Function Pointer

  Summary:
    Pointer to a SPI Call back function when SPI is configued in slave mode.

  Description:
    This data type defines the required function signature for the
    SPI slave event handling callback function. Application must register
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
        SERCOM1_SPI_CallbackRegister(&APP_SPICallBack, NULL);

        void APP_SPICallBack(uintptr_t contextHandle)
        {
            if( SERCOM1_SPI_ErrorGet() == SPI_SLAVE_ERROR_NONE )
            {
                Exchange was completed without error
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

typedef void (*SERCOM_SPI_SLAVE_CALLBACK)(uintptr_t context);

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
    /* Exchange busy status of the SPI */
    bool                            transferIsBusy;

    /* SPI Event handler */
    SERCOM_SPI_SLAVE_CALLBACK       callback;

    /* Context */
    uintptr_t                       context;

    SPI_SLAVE_ERROR                 errorStatus;

    /* Number of bytes to write in the transmit buffer */
    uint32_t                        nWrBytes;

    /* Index to the number of bytes already written out from the transmit buffer */
    uint32_t                        wrOutIndex;

    /* Index into the receive buffer where the next received byte will be copied */
    uint32_t                        rdInIndex;

} SPI_SLAVE_OBJECT;

#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif

#endif //PLIB_SERCOM_SPI_SLAVE_COMMON_H