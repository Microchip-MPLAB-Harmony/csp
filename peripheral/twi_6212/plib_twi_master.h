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
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_TWI_MASTER_H
#define PLIB_TWI_MASTER_H

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
  /* No Error */
    TWI_ERROR_NONE,

  /* Slave returned Nack */
    TWI_ERROR_NACK,

} TWI_ERROR;

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
    uint16_t address;
    uint8_t *writeBuffer;
    uint8_t *readBuffer;
    size_t  writeSize;
    size_t  readSize;
    size_t  writeCount;
    size_t  readCount;

    /* State */
    volatile TWI_STATE state;

    /* Transfer status */
    volatile TWI_ERROR error;

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
    /* TWI Clock Speed */
    uint32_t clkSpeed;

} TWI_TRANSFER_SETUP;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_TWI_MASTER_H
