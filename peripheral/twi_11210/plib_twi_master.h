/*******************************************************************************
  TWI Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    twi_master.h

  Summary
    TWI peripheral library interface.

  Description
    This file defines the interface to the TWI peripheral library.  This 
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

#ifndef PLIB_TWI_MASTER_H   
#define PLIB_TWI_MASTER_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

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
/* TWI Transfer Status

   Summary:
    TWI Transfer Status data type.

   Description:
    This data type defines the TWI Transfer Status.

   Remarks:
    None.
*/

typedef enum
{	
	/* Busy*/
    TWI_TRANSFER_BUSY,
	
	/* Transfer Successful */
    TWI_TRANSFER_SUCCESS,
	
	/* Transfer Error */
    TWI_TRANSFER_ERROR,
	
} TWI_TRANSFER_STATUS;

// *****************************************************************************
/* TWI State.

   Summary:
    TWI PLib Task State.

   Description:
    This data type defines the TWI PLib Task State.

   Remarks:
    None.
  
*/

typedef enum {

    /* TWI PLib Task Error State */
	TWI_STATE_ERROR = -1,
	
	/* TWI PLib Task Idle State */
	TWI_STATE_IDLE,
	
	/* TWI PLib Task Address Send State */
	TWI_STATE_ADDR_SEND,
	
	/* TWI PLib Task Read Transfer State */
	TWI_STATE_TRANSFER_READ,
	
	/* TWI PLib Task Write Transfer State */
	TWI_STATE_TRANSFER_WRITE,
	
	/* TWI PLib Task Transfer Complete State */
	TWI_STATE_WAIT_FOR_TXCOMP,
	
	/* TWI PLib Task Transfer Done State */
	TWI_STATE_TRANSFER_DONE,

} TWI_STATE;

// *****************************************************************************
/* TWI Callback

   Summary:
    TWI Callback Function Pointer.

   Description:
    This data type defines the TWI Callback Function Pointer.

   Remarks:
    None.
*/

typedef void (*TWI_CALLBACK) 
( 
    /* Transfer event */
    TWI_TRANSFER_STATUS  event,   
  
    /* Transfer context */
    uintptr_t contextHandle 
);

// *****************************************************************************
/* TWI PLib Instance Object

   Summary:
    TWI PLib Object structure.

   Description:
    This data structure defines the TWI PLib Instance Object.

   Remarks:
    None.
*/

typedef struct
{
    /* Number of TRBs */
    uint32_t numTRBs;
	
	/* State */
	TWI_STATE state;
	
	/* Transfer status */
    TWI_TRANSFER_STATUS status;
	
	/* Transfer Event Callback */
	TWI_CALLBACK callback;

    /* Transfer context */
    uintptr_t context;	

} TWI_OBJ; 

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

} TWI_TRANSACTION_REQUEST_BLOCK;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif // PLIB_TWI_MASTER_H

/*******************************************************************************
 End of File
*/
