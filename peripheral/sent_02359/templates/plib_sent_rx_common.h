/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}_common.h
 
  Summary:
    PWM Common Header File
 
  Description:
    This file has prototype of all the interfaces which are common for all the
    SENT peripherals.
 
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

#ifndef PLIB_SENT_RX_COMMON_H
#define PLIB_SENT_RX_COMMON_H

//Section: Included Files
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>


/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif
// Section: Data type Definitions
/** 
  @brief    This data structure used to configure the SENT data packet
*/

typedef struct
{  
    unsigned int crc:4;     /**< Defines the CRC field */
    unsigned int data1:4;   /**< Defines the first data nibble field */       
    unsigned int data2:4;   /**< Defines the second data nibble field */
    unsigned int data3:4;   /**< Defines the third data nibble field */
    unsigned int data4:4;   /**< Defines the fourth data nibble field */
    unsigned int data5:4;   /**< Defines the fifth data nibble field */
    unsigned int data6:4;   /**< Defines the sixth data nibble field */
    unsigned int status:4;  /**< Defines the status field */
}SENT_DATA_RECEIVE;


/**
 @brief    Defines the SENT receive status.
           More than one of these values may be OR'd together to create a complete
           status value.  To test a value of this type, the bit of interest must be
           AND'ed with value and checked to see if the result is non-zero.
*/
typedef enum
{
    SENT_RECEIVE_SYNCTXEN = 0x1,        /**< Synchronization Period Receive Enable bit */
    SENT_RECEIVE_RXIDLE   = 0x2,        /**< Indicates whether The SENTx data bus has been Idle (high) for a period of SYNCMAX or greater */
    SENT_RECEIVE_FRAMEERR = 0x4,        /**< Indicates whether data nibble was received with less than 12 Tick periods or greater than 27 Tick periods */
    SENT_RECEIVE_CRCERR   = 0x8,        /**< Indicates whether a CRC error occurred for the data nibbles in SENTxDATH/L */
    SENT_RECEIVE_NIBBLE1  = 0x10,       /**< Module is receiving Data Nibble 1*/
    SENT_RECEIVE_NIBBLE2  = 0x20,       /**< Module is receiving Data Nibble 2*/
    SENT_RECEIVE_NIBBLE3  = 0x30,       /**< Module is receiving Data Nibble 3*/
    SENT_RECEIVE_NIBBLE4  = 0x40,       /**< Module is receiving Data Nibble 4*/
    SENT_RECEIVE_NIBBLE5  = 0x50,       /**< Module is receiving Data Nibble 5*/
    SENT_RECEIVE_NIBBLE6  = 0x60,       /**< Module is receiving Data Nibble 6*/
    SENT_RECEIVE_CRC      = 0x70,       /**< Module is receiving Data CRC*/
    SENT_RECEIVE_PAUSEPERIOD = 0x80     /**< Indicates whether the module is receiving a Pause period */
    
}SENT_RECEIVE_STATUS;

/**
 @brief    Defines the SENT error code
*/
typedef enum
{
	NO_ERROR,
	CRC_ERROR,
	FRAME_ERROR,
	RX_IDLE_ERROR
	
}SENT_ERROR_CODE;

<#if SENT_INTERRUPT_MODE == true>
/**
 @brief  The SENT_RECEIVE_COMPLETE_CALLBACK typedef defines a function pointer type for a callback function that is invoked when a data reception is complete. 
*/
typedef void (*SENT_RECEIVE_COMPLETE_CALLBACK)(uintptr_t context);
/**
@brief  The SENT_ERROR_CALLBACK typedef defines a function pointer type for a callback function that is invoked when an error is encountered while receiving the data. 
*/
typedef void (*SENT_ERROR_CALLBACK)(uintptr_t context);

// Section: Local: **** Do Not Use ****
typedef struct
{
    //SENT Event handler 
	SENT_RECEIVE_COMPLETE_CALLBACK callback_fn;
	//Context 
    uintptr_t context;
}SENT_RECEIVE_COMPLETE_OBJECT;

typedef struct
{
    //SENT Event handler
	SENT_ERROR_CALLBACK callback_fn;
	//Context
    uintptr_t context;
}SENT_ERROR_OBJECT;
</#if>

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif

#endif // PLIB_SENT_RX_COMMON_H