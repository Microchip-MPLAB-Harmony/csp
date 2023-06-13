/*******************************************************************************
Interface definition of ${QMSPI_INSTANCE_NAME} SPI Mode PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_${QMSPI_INSTANCE_NAME?lower_case}_spi.h

 Summary:
    Interface definition of the Quad Serial Peripheral Interface Plib (${QMSPI_INSTANCE_NAME})
    configured in SPI mode.

 Description:
    This file defines the interface for the ${QMSPI_INSTANCE_NAME} Plib.
    It allows user to setup ${QMSPI_INSTANCE_NAME} and transfer data to and from slave devices
    attached.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${QMSPI_INSTANCE_NAME}_SPI_H // Guards against multiple inclusion
#define PLIB_${QMSPI_INSTANCE_NAME}_SPI_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_qmspi_spi_common.h"

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
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
<#if QMSPI_DESCRIPTOR_MODE_EN?? && QMSPI_DESCRIPTOR_MODE_EN == true>
typedef struct
{
    uint32_t                transfer_length;
    uint8_t                 interface_mode;
    bool                    rx_en;
    uint8_t                 rx_dma_ch_num;
    uint32_t                rx_des_addr;
    bool                    rx_addr_inc;
    bool                    tx_en;
    uint8_t                 tx_dma_ch_num;
    uint32_t                tx_src_addr;
    bool                    tx_addr_inc;
    bool                    is_desc_last;
    bool                    close_transfer_en;
    uint8_t                 next_desc_num;
} QMSPI_SPI_DMA_TRANS_DESC;
</#if>

void ${QMSPI_INSTANCE_NAME}_SPI_Initialize(void);
bool ${QMSPI_INSTANCE_NAME}_SPI_TransferSetup (QMSPI_SPI_TRANSFER_SETUP *setup);
bool ${QMSPI_INSTANCE_NAME}_SPI_Write(void* pTransmitData, size_t txSize);
bool ${QMSPI_INSTANCE_NAME}_SPI_Read(void* pReceiveData, size_t rxSize);
bool ${QMSPI_INSTANCE_NAME}_SPI_WriteRead (void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize);
bool ${QMSPI_INSTANCE_NAME}_SPI_IsTransmitterBusy(void);
<#if QMSPI_INTERRUPT_MODE == true || QMSPI_DMA_EN == true>
void ${QMSPI_INSTANCE_NAME}_SPI_CallbackRegister(QMSPI_SPI_CALLBACK callback, uintptr_t context);
bool ${QMSPI_INSTANCE_NAME}_SPI_IsBusy (void);
</#if>

<#if QMSPI_DESCRIPTOR_MODE_EN?? && QMSPI_DESCRIPTOR_MODE_EN == true>
void QMSPI_TransferDescriptorSetup(uint8_t descNum, QMSPI_SPI_DMA_TRANS_DESC desc);
</#if>



// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_${QMSPI_INSTANCE_NAME}_SPI_H */
