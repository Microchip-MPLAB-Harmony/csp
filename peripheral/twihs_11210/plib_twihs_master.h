/*******************************************************************************
  TWIHS Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    twihs_master.h

  Summary
    TWIHS peripheral library interface.

  Description
    This file defines the interface to the TWIHS peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

  Remarks:
    
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef PLIB_TWIHS_MASTER_H   
#define PLIB_TWIHS_MASTER_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/
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
/* TWIHS Transfer Status

   Summary:
    TWIHS Transfer Status data type.

   Description:
    This data type defines the TWIHS Transfer Status.

   Remarks:
    None.
*/

typedef enum
{	
	/* No Error */
    TWIHS_ERROR_NONE,
	
	/* Slave returned Nack */
    TWIHS_ERROR_NACK,
	
} TWIHS_ERROR;

// *****************************************************************************
/* TWIHS State.

   Summary:
    TWIHS PLib Task State.

   Description:
    This data type defines the TWIHS PLib Task State.

   Remarks:
    None.
  
*/

typedef enum {

    /* TWIHS PLib Task Error State */
	TWIHS_STATE_ERROR = -1,
	
	/* TWIHS PLib Task Idle State */
	TWIHS_STATE_IDLE,
	
	/* TWIHS PLib Task Address Send State */
	TWIHS_STATE_ADDR_SEND,
	
	/* TWIHS PLib Task Read Transfer State */
	TWIHS_STATE_TRANSFER_READ,
	
	/* TWIHS PLib Task Write Transfer State */
	TWIHS_STATE_TRANSFER_WRITE,
	
	/* TWIHS PLib Task Transfer Complete State */
	TWIHS_STATE_WAIT_FOR_TXCOMP,
	
	/* TWIHS PLib Task Transfer Done State */
	TWIHS_STATE_TRANSFER_DONE,

} TWIHS_STATE;

// *****************************************************************************
/* TWIHS Callback

   Summary:
    TWIHS Callback Function Pointer.

   Description:
    This data type defines the TWIHS Callback Function Pointer.

   Remarks:
    None.
*/

typedef void (*TWIHS_CALLBACK) 
(   
    /* Transfer context */
    uintptr_t contextHandle 
);

// *****************************************************************************
/* TWIHS PLib Instance Object

   Summary:
    TWIHS PLib Object structure.

   Description:
    This data structure defines the TWIHS PLib Instance Object.

   Remarks:
    None.
*/

typedef struct
{
    /* Number of TRBs */
    uint32_t numTRBs;
	
	/* State */
	TWIHS_STATE state;
	
	/* Transfer status */
    TWIHS_ERROR error;
	
	/* Transfer Event Callback */
	TWIHS_CALLBACK callback;

    /* Transfer context */
    uintptr_t context;	

} TWIHS_OBJ;

// *****************************************************************************
/* Transaction Request Block

   Summary:
    Transaction Request Block Structure.

   Description:
    This data structure defines the Transaction Request Block.

   Remarks:
    None.
*/

typedef struct 
{
    /* TWIHS Clock Speed */
    uint32_t clkSpeed;

} TWIHS_TRANSFER_SETUP;

// *****************************************************************************
/* Transaction Request Block

   Summary:
    Transaction Request Block Structure.

   Description:
    This data structure defines the Transaction Request Block.

   Remarks:
    None.
*/

typedef struct 
{
    /* slave address */
    uint16_t address;
	
	/* read/write transaction*/
	bool read;
	
	/* data length */
	uint8_t length;
	
	/* data buffer pointer */
	uint8_t *pbuffer;

} TWIHS_TRANSACTION_REQUEST_BLOCK;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // PLIB_TWIHS_MASTER_H

/*******************************************************************************
 End of File
*/
