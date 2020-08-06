/*******************************************************************************
  SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SPI_INSTANCE_NAME?lower_case}_slave.h

  Summary:
    ${SPI_INSTANCE_NAME} Slave PLIB Header File

  Description:
    This file has prototype of all the interfaces provided for particular
    SPI peripheral.

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2019-2020 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${SPI_INSTANCE_NAME}_SLAVE_H
#define PLIB_${SPI_INSTANCE_NAME}_SLAVE_H

#include "device.h"
#include "plib_spi_slave_common.h"

/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif


/****************************** ${SPI_INSTANCE_NAME} Interface *********************************/

void ${SPI_INSTANCE_NAME}_Initialize (void);
size_t ${SPI_INSTANCE_NAME}_Read(void* pRdBuffer, size_t size);
size_t ${SPI_INSTANCE_NAME}_Write(void* pWrBuffer, size_t size );
size_t ${SPI_INSTANCE_NAME}_ReadCountGet(void);
size_t ${SPI_INSTANCE_NAME}_ReadBufferSizeGet(void);
size_t ${SPI_INSTANCE_NAME}_WriteBufferSizeGet(void);
void ${SPI_INSTANCE_NAME}_CallbackRegister(SPI_SLAVE_CALLBACK callBack, uintptr_t context );
SPI_SLAVE_ERROR ${SPI_INSTANCE_NAME}_ErrorGet(void);
bool ${SPI_INSTANCE_NAME}_IsBusy(void);
<#if SPIS_USE_BUSY_PIN == true>
void ${SPI_INSTANCE_NAME}_Ready(void);
</#if>

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif

#endif // PLIB_${SPI_INSTANCE_NAME}_SLAVE_H
