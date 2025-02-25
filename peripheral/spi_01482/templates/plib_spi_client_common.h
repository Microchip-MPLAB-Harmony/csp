/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_spi_client_common.h

  Summary:
    SPI PLIB Client Common Header File

  Description:
    This file has prototype of all the interfaces which are common for all the
    SPI peripherals.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2025-2020 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_SPI_CLIENT_COMMON_H
#define PLIB_SPI_CLIENT_COMMON_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>


/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif

/****************************** SPI Slave Interface *********************************/

/* SPI Client Errors

  Summary:
    Defines the data type for the SPI Client mode errors

  Description:
    This may be used to check the type of error occurred

  Remarks:
    None
*/


/* Error status when no error has occurred */
#define    SPI_CLIENT_ERROR_NONE     (0U)

/* Buffer overflow error has occured */
#define    SPI_CLIENT_ERROR_BUFOVF  (0x00000040UL)

typedef uint32_t SPI_CLIENT_ERROR;

// *****************************************************************************
/* SPI Client Mode CallBack Function Pointer

  Summary:
    Pointer to a SPI Call back function when SPI is configued in client mode.

  Description:
    This data type defines the required function signature for the
    SPI client event handling callback function. Application must register
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
            if( SPI1_ErrorGet() == SPI_CLIENT_ERROR_NONE )
            {
                
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

typedef void (*SPI_CLIENT_CALLBACK)(uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

typedef struct
{
    /* Exchange busy status of the SPI */
    bool                            transferIsBusy;

    /* SPI Event handler */
    SPI_CLIENT_CALLBACK              callback;

    /* Context */
    uintptr_t                       context;

    SPI_CLIENT_ERROR                 errorStatus;

    /* Number of bytes to write in the transmit buffer */
    uint32_t                        nWrBytes;

    /* Index to the number of bytes already written out from the transmit buffer */
    uint32_t                        wrOutIndex;

    /* Index into the receive buffer where the next received byte will be copied */
    uint32_t                        rdInIndex;

    /* Flag to indicate that the RX interrupt is active (being serviced) */
    bool                            rxInterruptActive;

    /* Flag to indicate that CS interrupt has delegated callback responsibility to the SPI receive interrupt */
    bool                            csInterruptPending;

} SPI_CLIENT_OBJECT;

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif

#endif // PLIB_SPI_SLAVE_COMMON_H