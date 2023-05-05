/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Instance Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_smb_master_common.h

  Summary
    I2C peripheral library master mode common interface.

  Description
    This file defines the interface to the I2C peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:

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

#ifndef PLIB_SMB_MASTER_COMMON_H
#define PLIB_SMB_MASTER_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

/* No Error */
#define I2C_SMB_HOST_ERROR_NONE 0U

/* Slave returned Nack */
#define I2C_SMB_HOST_ERROR_NACK 1U

/* Bus Collision Error */
#define I2C_SMB_HOST_ERROR_BUS_COLLISION 2U

/* Bus Arbitration lost Error */
#define I2C_SMB_HOST_ERROR_ARBITRATION_LOST 4U

/* Timeout related Error */
#define I2C_SMB_HOST_ERROR_TIMEOUT 8U

/* PEC Error */
#define I2C_SMB_HOST_ERROR_PEC 16U

typedef uint32_t I2C_SMB_HOST_ERROR;

#define I2C_SMB_HOST_TRANSFER_TYPE_WRITE 0U

#define I2C_SMB_HOST_TRANSFER_TYPE_READ 1U

typedef uint32_t I2C_SMB_HOST_TRANSFER_TYPE;

typedef enum
{
    I2C_SMB_HOST_STATE_IDLE,

    I2C_SMB_HOST_STATE_TRANSMIT,

    I2C_SMB_HOST_STATE_RECEIVE,

} I2C_SMB_HOST_STATE;

typedef enum
{
    I2C_SMB_HOST_PROTOCOL_WR_BYTE,

    I2C_SMB_HOST_PROTOCOL_WR_WORD,

    I2C_SMB_HOST_PROTOCOL_WR_BLK,

    I2C_SMB_HOST_PROTOCOL_RD_BYTE,

    I2C_SMB_HOST_PROTOCOL_RD_WORD,

    I2C_SMB_HOST_PROTOCOL_RD_BLK,

    I2C_SMB_HOST_PROTOCOL_WR_BLK_RD_BLK,

} I2C_SMB_HOST_PROTOCOL;

typedef enum
{
    I2C_SMB_HOST_TRANSFER_EVENT_NONE = 0,

    I2C_SMB_HOST_TRANSFER_EVENT_RX_READY,

    I2C_SMB_HOST_TRANSFER_EVENT_NAK_RECEIVED,

    I2C_SMB_HOST_TRANSFER_EVENT_ERROR,

    I2C_SMB_HOST_TRANSFER_EVENT_DONE,

}I2C_SMB_HOST_TRANSFER_EVENT;


typedef void (*I2C_SMB_HOST_CALLBACK) (I2C_SMB_HOST_TRANSFER_EVENT event, uintptr_t contextHandle);

typedef struct
{
    uint16_t                address;
    uint8_t*                writeBuffer;
    uint8_t*                readBuffer;
    size_t                  writeSize;
    size_t                  readSize;
    size_t                  writeCount;
    size_t                  readCount;
    I2C_SMB_HOST_STATE      state;
    I2C_SMB_HOST_ERROR      error;
    I2C_SMB_HOST_CALLBACK   callback;
    uintptr_t               context;
    uint32_t                dmaRdBytes;
    bool                    dmaDirChange;
    I2C_SMB_HOST_PROTOCOL   protocol;

} I2C_SMB_HOST_OBJ;

typedef struct
{
    /* I2C Clock Speed */
    uint32_t clkSpeed;

} I2C_SMB_HOST_TRANSFER_SETUP;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif /* PLIB_SMB_MASTER_COMMON_H */














