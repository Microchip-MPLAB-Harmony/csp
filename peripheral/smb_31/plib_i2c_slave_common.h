/*******************************************************************************
  Inter-Integrated Circuit (I2C) Library
  Instance Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_i2c_slave_common.h

  Summary
    I2C slave common peripheral library interface.

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

#ifndef PLIB_I2C_SLAVE_COMMON_H
#define PLIB_I2C_SLAVE_COMMON_H

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

typedef enum
{
    /* No Error */
    I2C_SLAVE_ERROR_NONE,

    /* Bus Collision Error */
    I2C_SLAVE_ERROR_BUS_COLLISION,

} I2C_SLAVE_ERROR;

/* I2C Master is writing to slave */
#define I2C_SLAVE_TRANSFER_DIR_WRITE 0U

/* I2C Master is reading from slave */
#define I2C_SLAVE_TRANSFER_DIR_READ  1U

typedef uint32_t I2C_SLAVE_TRANSFER_DIR;

typedef enum
{
    I2C_SLAVE_ACK_STATUS_RECEIVED_ACK = 0,

    I2C_SLAVE_ACK_STATUS_RECEIVED_NAK,

}I2C_SLAVE_ACK_STATUS;

typedef enum
{
    I2C_SLAVE_TRANSFER_EVENT_NONE = 0,

    I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH,

    I2C_SLAVE_TRANSFER_EVENT_RX_READY,

    I2C_SLAVE_TRANSFER_EVENT_TX_READY,

    I2C_SLAVE_TRANSFER_EVENT_NAK_RECEIVED,

    I2C_SLAVE_TRANSFER_EVENT_STOP_BIT_RECEIVED,

    I2C_SLAVE_TRANSFER_EVENT_ERROR,

}I2C_SLAVE_TRANSFER_EVENT;

typedef bool (*I2C_SLAVE_CALLBACK) (I2C_SLAVE_TRANSFER_EVENT event, uintptr_t contextHandle);

typedef struct
{
    I2C_SLAVE_ERROR         error;
    I2C_SLAVE_CALLBACK      callback;
    uintptr_t               context;
    I2C_SLAVE_TRANSFER_DIR  transferDir;
    uint32_t                txCount;
    uint32_t                rxCount;

} I2C_SLAVE_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif /* PLIB_I2C_SLAVE_COMMON_H */














