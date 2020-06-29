/*******************************************************************************
  SERIAL COMMUNICATION SERIAL PERIPHERAL INTERFACE (${SERCOM_INSTANCE_NAME}_SPI ) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SERCOM_INSTANCE_NAME?lower_case}_spi_slave.h

  Summary
   ${SERCOM_INSTANCE_NAME} SPI Slave PLIB Header File.

  Description
    This file defines the interface to the SERCOM SPI Slave peripheral library.
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

#ifndef PLIB_${SERCOM_INSTANCE_NAME}_SPI_SLAVE_H // Guards against multiple inclusion
#define PLIB_${SERCOM_INSTANCE_NAME}_SPI_SLAVE_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_sercom_spi_slave_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

extern "C" {

#endif

// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

/* The following functions make up the methods (set of possible operations) of
this interface.
*/

void ${SERCOM_INSTANCE_NAME}_SPI_Initialize (void);
size_t ${SERCOM_INSTANCE_NAME}_SPI_Read(void* pRdBuffer, size_t size);
size_t ${SERCOM_INSTANCE_NAME}_SPI_Write(void* pWrBuffer, size_t size );
size_t ${SERCOM_INSTANCE_NAME}_SPI_ReadCountGet(void);
size_t ${SERCOM_INSTANCE_NAME}_SPI_ReadBufferSizeGet(void);
size_t ${SERCOM_INSTANCE_NAME}_SPI_WriteBufferSizeGet(void);
void ${SERCOM_INSTANCE_NAME}_SPI_CallbackRegister(SERCOM_SPI_SLAVE_CALLBACK callBack, uintptr_t context );
SPI_SLAVE_ERROR ${SERCOM_INSTANCE_NAME}_SPI_ErrorGet(void);
bool ${SERCOM_INSTANCE_NAME}_SPI_IsBusy(void);
<#if SPIS_USE_BUSY_PIN == true>
void ${SERCOM_INSTANCE_NAME}_SPI_Ready(void);
</#if>


#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif /* PLIB_${SERCOM_INSTANCE_NAME}_SPI_SLAVE_H */