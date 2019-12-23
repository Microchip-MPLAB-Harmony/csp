/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (SERCOM I2C) Library
  Instance Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_sercom_i2c_slave_common.h

  Summary
    SERCOM I2C Slave Common definitions file.

  Description
    This file defines the definitions for the SERCOM I2C Slave interface. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:

*******************************************************************************/
// DOM-IGNORE-BEGIN
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

#ifndef PLIB_SERCOM_I2C_SLAVE_COMMON_H
#define PLIB_SERCOM_I2C_SLAVE_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include "device.h"

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

// *****************************************************************************
/* SERCOM I2C Transfer type

  Summary:
    List of transfer direction.

  Description:
    This enum defines the I2C transfer direction.

  Remarks:
    None.
*/

typedef enum
{
    /* I2C Master is writing to slave */
    SERCOM_I2C_SLAVE_TRANSFER_DIR_WRITE = 0,

    /* I2C Master is reading from slave */
    SERCOM_I2C_SLAVE_TRANSFER_DIR_READ  = 1,
}SERCOM_I2C_SLAVE_TRANSFER_DIR;

typedef enum
{
    SERCOM_I2C_SLAVE_ACK_ACTION_SEND_ACK = 0,
    SERCOM_I2C_SLAVE_ACK_ACTION_SEND_NAK,
}SERCOM_I2C_SLAVE_ACK_ACTION_SEND;

typedef enum
{
    SERCOM_I2C_SLAVE_INTFLAG_PREC = SERCOM_I2CS_INTFLAG_PREC_Msk,
    SERCOM_I2C_SLAVE_INTFLAG_AMATCH = SERCOM_I2CS_INTFLAG_AMATCH_Msk,
    SERCOM_I2C_SLAVE_INTFLAG_DRDY = SERCOM_I2CS_INTFLAG_DRDY_Msk,
        SERCOM_I2C_SLAVE_INTFLAG_ERROR = SERCOM_I2CS_INTFLAG_ERROR_Msk,
}SERCOM_I2C_SLAVE_INTFLAG;

typedef enum
{
    SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_ACK = 0,
    SERCOM_I2C_SLAVE_ACK_STATUS_RECEIVED_NAK,
}SERCOM_I2C_SLAVE_ACK_STATUS;

typedef enum
{
    SERCOM_I2C_SLAVE_TRANSFER_EVENT_NONE = 0,
    SERCOM_I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH,
	
	/* Data sent by I2C Master is available */
    SERCOM_I2C_SLAVE_TRANSFER_EVENT_RX_READY,
	
	/* I2C slave can respond to data read request from I2C Master */
    SERCOM_I2C_SLAVE_TRANSFER_EVENT_TX_READY,
	
    SERCOM_I2C_SLAVE_TRANSFER_EVENT_STOP_BIT_RECEIVED,
    SERCOM_I2C_SLAVE_TRANSFER_EVENT_ERROR,
}SERCOM_I2C_SLAVE_TRANSFER_EVENT;

typedef enum
{
    SERCOM_I2C_SLAVE_COMMAND_SEND_ACK = 0,
    SERCOM_I2C_SLAVE_COMMAND_SEND_NAK,
    SERCOM_I2C_SLAVE_COMMAND_RECEIVE_ACK_NAK,
    SERCOM_I2C_SLAVE_COMMAND_WAIT_FOR_START,
}SERCOM_I2C_SLAVE_COMMAND;

typedef enum
{
    SERCOM_I2C_SLAVE_ERROR_BUSERR = SERCOM_I2CS_STATUS_BUSERR_Msk,
    SERCOM_I2C_SLAVE_ERROR_COLL = SERCOM_I2CS_STATUS_COLL_Msk,
    SERCOM_I2C_SLAVE_ERROR_LOWTOUT = SERCOM_I2CS_STATUS_LOWTOUT_Msk,
    SERCOM_I2C_SLAVE_ERROR_SEXTTOUT = SERCOM_I2CS_STATUS_SEXTTOUT_Msk,
    SERCOM_I2C_SLAVE_ERROR_ALL = (SERCOM_I2C_SLAVE_ERROR_BUSERR | SERCOM_I2C_SLAVE_ERROR_COLL  | SERCOM_I2C_SLAVE_ERROR_LOWTOUT  | SERCOM_I2C_SLAVE_ERROR_SEXTTOUT)
}SERCOM_I2C_SLAVE_ERROR;

// *****************************************************************************
/* SERCOM I2C Callback

   Summary:
    SERCOM I2C Callback Function Pointer.

   Description:
    This data type defines the SERCOM I2C Callback Function Pointer.

   Remarks:
    None.
*/

typedef bool (*SERCOM_I2C_SLAVE_CALLBACK) ( SERCOM_I2C_SLAVE_TRANSFER_EVENT event, uintptr_t contextHandle );

// *****************************************************************************
/* SERCOM I2C PLib Instance Object

   Summary:
    SERCOM I2C PLib Object structure.

   Description:
    This data structure defines the SERCOM I2C PLib Instance Object.

   Remarks:
    None.
*/

typedef struct
{
    bool                        isBusy;

    bool                        isRepeatedStart;

    bool                        isFirstRxAfterAddressPending;

    /* Transfer Event Callback */
    SERCOM_I2C_SLAVE_CALLBACK   callback;

    /* Transfer context */
    uintptr_t                   context;

} SERCOM_I2C_SLAVE_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_SERCOM_I2C_SLAVE_COMMON_H */
