/*******************************************************************************
  FLEXCOM TWI Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_flexcom_twi_slave_common.h

  Summary
    FLEXCOM TWI Slave common peripheral library interface.

  Description
    This file defines the interface to the FLEXCOM TWI peripheral library. This
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

#ifndef PLIB_FLEXCOM_TWI_SLAVE_COMMON_H
#define PLIB_FLEXCOM_TWI_SLAVE_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

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
// *****************************************************************************
/* FLEXCOM TWI Transfer type

  Summary:
    List of transfer direction.

  Description:
    This enum defines the I2C transfer direction.

  Remarks:
    None.
*/

typedef enum
{
    /* FLEXCOM TWI Master is writing to slave */
    FLEXCOM_TWI_SLAVE_TRANSFER_DIR_WRITE = 0,

    /* FLEXCOM TWI Master is reading from slave */
    FLEXCOM_TWI_SLAVE_TRANSFER_DIR_READ  = 1,
}FLEXCOM_TWI_SLAVE_TRANSFER_DIR;

// *****************************************************************************
/* FLEXCOM TWI status flags

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
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_SVACC     = TWI_SR_SVACC_Msk,
	
	/* End of slave access flag */
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_EOSACC    = TWI_SR_EOSACC_Msk,
    
	/* TWI transfer direction is read */
	FLEXCOM_TWI_SLAVE_STATUS_FLAG_SVREAD    = TWI_SR_SVREAD_Msk,
	
	/* Transmitter is ready */
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_TXRDY     = TWI_SR_TXRDY_Msk,
	
	/* Receiver has an unread character */
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_RXRDY     = TWI_SR_RXRDY_Msk,
	
	/* NACK received from master */
	FLEXCOM_TWI_SLAVE_STATUS_FLAG_NACK    	= TWI_SR_NACK_Msk,
	
	/* Stop condtion or start condition with other slave address detected */
    FLEXCOM_TWI_SLAVE_STATUS_FLAG_TXCOMP    = TWI_SR_TXCOMP_Msk,
}FLEXCOM_TWI_SLAVE_STATUS_FLAG;

// *****************************************************************************
/* FLEXCOM TWI slave ACK status

  Summary:
	This enum defines ACK/NACK status received from master

  Description:
    This enum defines ACK/NACK status received from master

  Remarks:
    None.
*/

typedef enum
{
	/* Received ACK from I2C master */
    FLEXCOM_TWI_SLAVE_ACK_STATUS_RECEIVED_ACK = 0,
	
	/* Received NACK from I2C master */
    FLEXCOM_TWI_SLAVE_ACK_STATUS_RECEIVED_NAK,
}FLEXCOM_TWI_SLAVE_ACK_STATUS;

// *****************************************************************************
/* FLEXCOM TWI slave transfer event

  Summary:
	This enum defines list of possible events

  Description:
    This enum defines list of possible events passed to the application callback

  Remarks:
    None.
*/

typedef enum
{
    FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_NONE = 0,

    /* Address match event */
    FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_ADDR_MATCH,

    /* Data sent by I2C Master is available */
    FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_RX_READY,

    /* I2C slave can respond to data read request from I2C Master */
    FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_TX_READY,

	/* I2C stop condition received or start condtion with other slave address detected */
    FLEXCOM_TWI_SLAVE_TRANSFER_EVENT_TRANSMISSION_COMPLETE,

}FLEXCOM_TWI_SLAVE_TRANSFER_EVENT;

// *****************************************************************************
/* FLEXCOM TWI Slave Callback

   Summary:
    FLEXCOM TWI Slave Callback Function Pointer.

   Description:
    This data type defines the FLEXCOM TWI Slave Callback Function Pointer.

   Remarks:
    None.
*/

typedef bool (*FLEXCOM_TWI_SLAVE_CALLBACK) ( FLEXCOM_TWI_SLAVE_TRANSFER_EVENT event, uintptr_t contextHandle );

// *****************************************************************************
/* FLEXCOM TWI Slave PLIB Instance Object

   Summary:
    FLEXCOM TWI Slave PLIB Object structure.

   Description:
    This data structure defines the FLEXCOM TWI Slave PLIB Instance Object.

   Remarks:
    None.
*/

typedef struct
{
    bool                                isBusy;

    bool                                isAddrMatchEventNotified;

    bool                                isFirstTxPending;

    /* Transfer Event Callback */
    FLEXCOM_TWI_SLAVE_CALLBACK          callback;

    /* Transfer context */
    uintptr_t                           context;

} FLEXCOM_TWI_SLAVE_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_FLEXCOM_TWI_SLAVE_COMMON_H */
