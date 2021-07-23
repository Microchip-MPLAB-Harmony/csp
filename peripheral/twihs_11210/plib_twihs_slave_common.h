/*******************************************************************************
  TWIHS Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_twihs_slave_common.h

  Summary
    TWIHS Slave peripheral library interface.

  Description
    This file defines the interface to the TWIHS peripheral library.  This
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

#ifndef PLIB_TWIHS_SLAVE_COMMON_H
#define PLIB_TWIHS_SLAVE_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdbool.h>
#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
/* TWIHS Transfer type

  Summary:
    List of transfer direction.

  Description:
    This enum defines the I2C transfer direction.

  Remarks:
    None.
*/

typedef enum
{
    /* TWIHS Master is writing to slave */
    TWIHS_SLAVE_TRANSFER_DIR_WRITE = 0,

    /* TWIHS Master is reading from slave */
    TWIHS_SLAVE_TRANSFER_DIR_READ  = 1,
}TWIHS_SLAVE_TRANSFER_DIR;

// *****************************************************************************
/* TWIHS status flags

  Summary:
	This enum defines the list of possible I2C slave events

  Description:
    This enum defines the list of possible I2C slave events

  Remarks:
    None.
*/
typedef enum
{
	/* Slave Access flag */
    TWIHS_SLAVE_STATUS_FLAG_SVACC   = TWIHS_SR_SVACC_Msk,
	
	/* End of slave access flag */
    TWIHS_SLAVE_STATUS_FLAG_EOSACC  = TWIHS_SR_EOSACC_Msk,
	
	/* TWIHS transfer direction is read */
    TWIHS_SLAVE_STATUS_FLAG_SVREAD  = TWIHS_SR_SVREAD_Msk,
	
	/* Transmitter is ready */
    TWIHS_SLAVE_STATUS_FLAG_TXRDY   = TWIHS_SR_TXRDY_Msk,
	
	/* Receiver has an unread character */
    TWIHS_SLAVE_STATUS_FLAG_RXRDY   = TWIHS_SR_RXRDY_Msk,
	
	/* NACK received from master */
	TWIHS_SLAVE_STATUS_FLAG_NACK    = TWIHS_SR_NACK_Msk,
	
	/* Stop condtion or start condition with other slave address detected */
    TWIHS_SLAVE_STATUS_FLAG_TXCOMP  = TWIHS_SR_TXCOMP_Msk,
}TWIHS_SLAVE_STATUS_FLAG;

// *****************************************************************************
/* TWIHS slave ACK status

  Summary:
	This enum defines ACK/NACK status received from master

  Description:
    This enum defines ACK/NACK status received from master

  Remarks:
    None.
*/
typedef enum
{
    TWIHS_SLAVE_ACK_STATUS_RECEIVED_ACK = 0,
    TWIHS_SLAVE_ACK_STATUS_RECEIVED_NAK,
}TWIHS_SLAVE_ACK_STATUS;

// *****************************************************************************
/* TWIHS slave transfer event

  Summary:
	This enum defines list of possible events

  Description:
    This enum defines list of possible events passed to the application callback

  Remarks:
    None.
*/
typedef enum
{
    TWIHS_SLAVE_TRANSFER_EVENT_NONE = 0,

    /* Address match event */
    TWIHS_SLAVE_TRANSFER_EVENT_ADDR_MATCH,

    /* Data sent by I2C Master is available */
    TWIHS_SLAVE_TRANSFER_EVENT_RX_READY,

    /* I2C slave can respond to data read request from I2C Master */
    TWIHS_SLAVE_TRANSFER_EVENT_TX_READY,

	/* I2C stop condition received or start condtion with other slave address detected */
    TWIHS_SLAVE_TRANSFER_EVENT_TRANSMISSION_COMPLETE,

}TWIHS_SLAVE_TRANSFER_EVENT;

// *****************************************************************************
/* TWIHS Slave Callback

   Summary:
    TWIHS Slave Callback Function Pointer.

   Description:
    This data type defines the TWIHS Slave Callback Function Pointer.

   Remarks:
    None.
*/

typedef bool (*TWIHS_SLAVE_CALLBACK) ( TWIHS_SLAVE_TRANSFER_EVENT event, uintptr_t contextHandle );

// *****************************************************************************
/* TWIHS Slave PLIB Instance Object

   Summary:
    TWIHS Slave PLIB Object structure.

   Description:
    This data structure defines the TWIHS Slave PLIB Instance Object.

   Remarks:
    None.
*/

typedef struct
{
    bool                        isBusy;

    bool                        isAddrMatchEventNotified;

    bool                        isFirstTxPending;

    /* Transfer Event Callback */
    TWIHS_SLAVE_CALLBACK        callback;

    /* Transfer context */
    uintptr_t                   context;

} TWIHS_SLAVE_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // PLIB_TWIHS_SLAVE_COMMON_H
