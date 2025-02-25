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
#ifndef PLIB_SENT_TX_COMMON_H
#define PLIB_SENT_TX_COMMON_H

//Section: Included Files
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif

// Section: Data Type Definitions
/** 
  @brief    This data type is used to configure the SENT data packet
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
}SENT_DATA_TRANSMIT;

// Section: Enum Declarations

/**
 @brief   Defines the sent transmission mode (Asynchronous and Synchronous)
*/
typedef enum 
{
  SENT_TRANSMIT_ASYNCHRONOUS,
  SENT_TRANSMIT_SYNCHRONOUS
}SENT_TRANSMIT_MODE;

/**
 @brief    Defines the SENT transmit status.
           More than one of these values may be OR'd together to create a complete
           status value.  To test a value of this type, the bit of interest must be
           AND'ed with value and checked to see if the result is non-zero.
*/
typedef enum
{
    SENT_TRANSMIT_SYNCTXEN = 0x1,      /**< Synchronization Period Status Transmit Enable bit */    
    SENT_TRANSMIT_NIBBLE1 = 0x10,      /**< Module is transmitting Data Nibble 1 */
    SENT_TRANSMIT_NIBBLE2 = 0x20,      /**< Module is transmitting Data Nibble 2 */   
    SENT_TRANSMIT_NIBBLE3 = 0x30,      /**< Module is transmitting Data Nibble 3 */
    SENT_TRANSMIT_NIBBLE4 = 0x40,      /**< Module is transmitting Data Nibble 4 */
    SENT_TRANSMIT_NIBBLE5 = 0x50,      /**< Module is transmitting Data Nibble 5 */ 
    SENT_TRANSMIT_NIBBLE6 = 0x60,      /**< Module is transmitting Data Nibble 6 */
    SENT_TRANSMIT_CRC     = 0x70,      /**< Module is transmitting Data CRC */
    SENT_TRANSMIT_PAUSEPERIOD = 0x80   /**< Indicates whether the module is transmitting a Pause period */
    
}SENT_TRANSMIT_STATUS;
<#if SENT_INTERRUPT_MODE == true>
/**
  @brief  The SENT_TRANSMIT_COMPLETE_CALLBACK typedef defines a function pointer type for a callback function that is invoked when a data transmission is complete. This callback function takes two parameters:
		1. context: A user-defined context value that can be used to pass additional information to the callback function. This is typically a pointer cast to an integer type. 
*/
typedef void (*SENT_TRANSMIT_COMPLETE_CALLBACK)(uintptr_t context);

// Section: Local: **** Do Not Use ****

typedef struct
{
    //SPI Event handler 
	SENT_TRANSMIT_COMPLETE_CALLBACK callback_fn;
	//Context 
    uintptr_t context;
}SENT_TRANSMIT_COMPLETE_OBJECT;
</#if>

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif

#endif // PLIB_SENT_TX_COMMON_H