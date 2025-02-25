/*******************************************************************************
  I2C PLIB Host
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_i2c_host_common.h
 
  Summary:
    I2C Host Common Header File
 
  Description:
    This file has prototype of all the interfaces which are common for all the
    I2C peripherals.
 
*******************************************************************************/
 
/*******************************************************************************
* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_I2C_HOST_COMMON_H
#define PLIB_I2C_HOST_COMMON_H

// Section: Included Files

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// /endcond

// Section: Data Types

/**
 * @summary     I2C Error Status data type.
 * @breif       This data type defines the I2C Error States.
 * @remarks     None.
*/
typedef enum
{
    I2C_ERROR_NONE,
    I2C_ERROR_NACK,
    I2C_ERROR_BUS_COLLISION,
} I2C_ERROR;

/**  
 * @summary        I2C Transfer Type.
 * @breif          This data type defines the I2C Transfer Type
 * @remarks        None
 */
typedef enum
{
    I2C_TRANSFER_TYPE_WRITE = 0U,
    I2C_TRANSFER_TYPE_READ = 1U

}I2C_TRANSFER_TYPE;

/** 
 * @summary     I2C PLib Task State.
 * @breif       This data type defines the I2C PLib Task State.
 * @remarks     None
 */
typedef enum
{
    I2C_STATE_START_CONDITION,
    I2C_STATE_ADDR_BYTE_1_SEND,
    I2C_STATE_ADDR_BYTE_2_SEND,
    I2C_STATE_READ_10BIT_MODE,
    I2C_STATE_ADDR_BYTE_1_SEND_10BIT_ONLY,
    I2C_STATE_WRITE,
    I2C_STATE_READ,
    I2C_STATE_READ_BYTE,
    I2C_STATE_WAIT_ACK_COMPLETE,
    I2C_STATE_WAIT_STOP_CONDITION_COMPLETE,
    I2C_STATE_IDLE,
} I2C_STATE;

/** 
 * @ summary      I2C Callback Function Pointer.
 * @ breif        This data type defines the I2C Callback Function Pointer.
 * @ remarks      None
 **/
typedef void (*I2C_CALLBACK) (uintptr_t contextHandle);

/**
 *  @summary        I2C Transfer Setup Data Structure
 *  @breif          This data structure defines the I2C Transfer Setup Data
 *  @remarks        None
*/
typedef struct
{
    /* I2C Clock Speed */
    uint32_t clkSpeed;

} I2C_TRANSFER_SETUP;

// /cond IGNORE_THIS
// Section: Local Objects **** Do Not Use ****
typedef struct
{
    uint16_t                address;
    uint8_t*                writeBuffer;
    uint8_t*                readBuffer;
    size_t                  writeSize;
    size_t                  readSize;
    size_t                  writeCount;
    size_t                  readCount;
    bool                    forcedWrite;
    I2C_TRANSFER_TYPE       transferType;
    I2C_STATE               state;
    I2C_ERROR               error;
    I2C_CALLBACK            callback;
    uintptr_t               context;

} I2C_HOST_OBJ;

// /endcond

// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// /endcond

#endif /* PLIB_I2C_HOST_COMMON_H */















