/*******************************************************************************
  FLEXCOM TWI Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_flexcom_twi_master.h

  Summary
    FLEXCOM TWI peripheral library interface.

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

#ifndef PLIB_FLEXCOM_TWI_MASTER_H
#define PLIB_FLEXCOM_TWI_MASTER_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*
 * This section lists the other files that are included in this file.
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
/* FLEXCOM TWI Transfer Status

   Summary:
    FLEXCOM TWI Transfer Status data type.

   Description:
    This data type defines the FLEXCOM TWI Transfer Status.

   Remarks:
    None.
*/

typedef enum
{
    /* No Error */
    FLEXCOM_TWI_ERROR_NONE,

    /* Slave returned Nack */
    FLEXCOM_TWI_ERROR_NACK

} FLEXCOM_TWI_ERROR;

// *****************************************************************************
/* FLEXCOM TWI State.

   Summary:
    FLEXCOM TWI PLib Task State.

   Description:
    This data type defines the FLEXCOM TWI PLib Task State.

   Remarks:
    None.

*/

typedef enum {

    /* FLEXCOM TWI PLib Task Error State */
    FLEXCOM_TWI_STATE_ERROR = -1,

    /* FLEXCOM TWI PLib Task Idle State */
    FLEXCOM_TWI_STATE_IDLE,

    /* FLEXCOM TWI PLib Task Address Send State */
    FLEXCOM_TWI_STATE_ADDR_SEND,

    /* FLEXCOM TWI PLib Task Read Transfer State */
    FLEXCOM_TWI_STATE_TRANSFER_READ,

    /* FLEXCOM TWI PLib Task Write Transfer State */
    FLEXCOM_TWI_STATE_TRANSFER_WRITE,

    /* FLEXCOM TWI PLib Task Transfer Complete State */
    FLEXCOM_TWI_STATE_WAIT_FOR_TXCOMP,

    /* FLEXCOM TWI PLib Task Transfer Done State */
    FLEXCOM_TWI_STATE_TRANSFER_DONE

} FLEXCOM_TWI_STATE;

// *****************************************************************************
/* FLEXCOM TWI Callback

   Summary:
    FLEXCOM TWI Callback Function Pointer.

   Description:
    This data type defines the FLEXCOM TWI Callback Function Pointer.

   Remarks:
    None.
*/

typedef void (*FLEXCOM_TWI_CALLBACK) (uintptr_t contextHandle);

// *****************************************************************************
/* FLEXCOM TWI PLib Instance Object

   Summary:
    FLEXCOM TWI PLib Object structure.

   Description:
    This data structure defines the FLEXCOM TWI PLib Instance Object.

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
    FLEXCOM_TWI_STATE state;

    /* Transfer status */
    FLEXCOM_TWI_ERROR error;

    /* Transfer Event Callback */
    FLEXCOM_TWI_CALLBACK callback;

    /* Transfer context */
    uintptr_t context;

} FLEXCOM_TWI_OBJ;

// *****************************************************************************
/* Transfer Setup

   Summary:
    Transfer Setup Structure.

   Description:
    This data structure defines the TWI Clock Speed.

   Remarks:
    None.
*/

typedef struct
{
    /* FLEXCOM TWI Clock Speed */
    uint32_t clkSpeed;

} FLEXCOM_TWI_TRANSFER_SETUP;


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_FLEXCOM_TWI_MASTER_H */

/*******************************************************************************
 End of File
*/
