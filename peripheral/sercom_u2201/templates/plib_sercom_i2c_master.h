/*******************************************************************************
  Serial Communication Interface Inter-Integrated Circuit (SERCOM I2C) Library
  Instance Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_sercom_i2c_master.h

  Summary
    SERCOM I2C peripheral library interface.

  Description
    This file defines the interface to the SERCOM I2C peripheral library. This
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

#ifndef PLIB_SERCOM_I2C_MASTER_H
#define PLIB_SERCOM_I2C_MASTER_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*
 * This section lists the other files that are included in this file.
 */

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

// *****************************************************************************
/*
  Summary:
    List of transfer direction.

  Description:
    This enum defines the I2C transfer direction.

  Remarks:
    None.
*/

enum
{
    I2C_TRANSFER_WRITE = 0,
    I2C_TRANSFER_READ  = 1,
};

// *****************************************************************************
/* SERCOM I2C Error.

  Summary:
    Defines the possible errors that the SERCOM I2C peripheral can generate.

  Description:
    This enum defines the possible error the SERCOM I2C peripheral can generate.
    An error of this type is returned by the SERCOMx_I2C_ErrorGet() function.

  Remarks:
    None.
*/

typedef enum
{
    /* No error has occurred. */
    SERCOM_I2C_ERROR_NONE,

    /* A bus transaction was NAK'ed */
    SERCOM_I2C_ERROR_NAK,

    /* A bus error has occurred. */
    SERCOM_I2C_ERROR_BUS,

} SERCOM_I2C_ERROR;

// *****************************************************************************
/* SERCOM I2C State.

   Summary:
    SERCOM I2C PLib Task State.

   Description:
    This data type defines the SERCOM I2C PLib Task State.

   Remarks:
    None.

*/

typedef enum {

    /* SERCOM PLib Task Error State */
    SERCOM_I2C_STATE_ERROR = -1,

    /* SERCOM PLib Task Idle State */
    SERCOM_I2C_STATE_IDLE,

    /* SERCOM PLib Task Address Send State */
    SERCOM_I2C_STATE_ADDR_SEND,

    SERCOM_I2C_REINITIATE_TRANSFER,
    /* SERCOM PLib Task Read Transfer State */
    SERCOM_I2C_STATE_TRANSFER_READ,

    /* SERCOM PLib Task Write Transfer State */
    SERCOM_I2C_STATE_TRANSFER_WRITE,

    /* SERCOM PLib Task Transfer Done State */
    SERCOM_I2C_STATE_TRANSFER_DONE,

} SERCOM_I2C_STATE;

// *****************************************************************************
/* SERCOM I2C Callback

   Summary:
    SERCOM I2C Callback Function Pointer.

   Description:
    This data type defines the SERCOM I2C Callback Function Pointer.

   Remarks:
    None.
*/

typedef void (*SERCOM_I2C_CALLBACK)
(
    /*Transfer context*/
    uintptr_t contextHandle

);

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

    uint16_t address;

    uint8_t *writeBuffer;

    uint8_t    *readBuffer;

    size_t  writeSize;

    size_t  readSize;

    size_t  writeCount;

    size_t  readCount;

    /* State */
    SERCOM_I2C_STATE state;

    /* Transfer status */
    SERCOM_I2C_ERROR error;

    /* Transfer Event Callback */
    SERCOM_I2C_CALLBACK callback;

    /* Transfer context */
    uintptr_t context;

} SERCOM_I2C_OBJ;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_SERCOM_I2C_MASTER_H */