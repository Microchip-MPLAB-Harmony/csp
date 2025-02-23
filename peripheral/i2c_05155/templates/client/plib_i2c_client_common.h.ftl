/*******************************************************************************
  I2C Host PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_i2c_client_common.h
 
  Summary:
    I2C Client Common Header File
 
  Description:
    This file has prototype of all the interfaces which are common for all the
    I2C peripherals.
 
*******************************************************************************/
 
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_I2C_CLIENT_COMMON_H
#define PLIB_I2C_CLIENT_COMMON_H

// Section: Included Files

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// Section: Data Types

/**
 * @summary     I2C Error Status data type.
 * @breif       This data type defines the I2C Error States.
 * @remarks     None.
*/
typedef enum
{
    
    I2C_CLIENT_ERROR_NONE,  /* No Error */
    I2C_CLIENT_ERROR_BUS_COLLISION, /* Bus Collision Error */

} I2C_CLIENT_ERROR;

/**  
 * @summary         I2C Client Transfer Direction Enums
 * @breif           Defines the enum for I2C data transfer direction. 
 *                  The transfer direction of this type is returned by the I2Cx_TransferDirGet() function
 * @remarks         None
 */
typedef enum
{
    
    I2C_CLIENT_TRANSFER_DIR_WRITE = 0,      /* I2C Master is writing to client */
    I2C_CLIENT_TRANSFER_DIR_READ  = 1,      /* I2C Master is reading from client */
    
}I2C_CLIENT_TRANSFER_DIR;

/**  
 * @summary         I2C Client Acknowledgement Status Enums
 * @breif           Defines the enum for the I2C client acknowledgement. 
 *                  Enum of this type is returned by the I2Cx_LastByteAckStatusGet() function.
 * @remarks         None
 */
/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 5.2 deviated: Deviation record ID -  H3_MISRAC_2012_R_5_2_DR_1 */
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
    <#if core.COMPILER_CHOICE == "XC32">
    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunknown-pragmas"
    </#if>
    #pragma coverity compliance block deviate "MISRA C-2012 Rule 5.2" "H3_MISRAC_2012_R_5_2_DR_1"
</#if>
typedef enum
{
    
    I2C_CLIENT_ACK_STATUS_RECEIVED_ACK = 0,
    I2C_CLIENT_ACK_STATUS_RECEIVED_NAK,
    
} I2C_CLIENT_ACK_STATUS;
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>

    #pragma coverity compliance end_block "MISRA C-2012 Rule 5.2"
    <#if core.COMPILER_CHOICE == "XC32">
    #pragma GCC diagnostic pop
    </#if>
</#if>
 /* MISRAC 2012 deviation block end */

/**  
 * @summary         I2C Client Transfer Event Enums
 * @breif           Defines the enum for the I2C client transfer event. 
 *                  An event of this type is returned back in the callback by the I2C client PLIB to 
 *                  indicate the transfer event for which the callback has been called.
 * @remarks         None
 */
typedef enum
{
    I2C_CLIENT_TRANSFER_EVENT_NONE = 0,
    I2C_CLIENT_TRANSFER_EVENT_ADDR_MATCH,   /* Address match event */ 
    I2C_CLIENT_TRANSFER_EVENT_RX_READY,     /* Data sent by I2C Master is available */
    I2C_CLIENT_TRANSFER_EVENT_TX_READY,     /* I2C client can respond to data read request from I2C Master */
    I2C_CLIENT_TRANSFER_EVENT_STOP_BIT_RECEIVED,    /* I2C stop bit received */
    I2C_CLIENT_TRANSFER_EVENT_ERROR,

} I2C_CLIENT_TRANSFER_EVENT;

/* I2C Client Callback

   Summary:
    I2C Client Callback Function Pointer.

   Description:
    This data type defines the I2C Client Callback Function Pointer.

   Remarks:
    None.
*/
typedef bool (*I2C_CLIENT_CALLBACK) (I2C_CLIENT_TRANSFER_EVENT event, uintptr_t contextHandle);

// /cond IGNORE_THIS
// Section: Local Objects **** Do Not Use ****

typedef struct
{
    I2C_CLIENT_ERROR         error;
    I2C_CLIENT_CALLBACK      callback;
    uintptr_t               context;
    uint8_t                 lastByteWritten;
} I2C_CLIENT_OBJ;

// /endcond

// /cond IGNORE_THIS
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif /* PLIB_I2C_CLIENT_COMMON_H */















