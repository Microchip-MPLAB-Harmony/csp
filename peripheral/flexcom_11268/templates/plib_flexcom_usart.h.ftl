/*******************************************************************************
  ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${FLEXCOM_INSTANCE_NAME?lower_case}_${FLEXCOM_MODE?lower_case}.h

  Summary
    ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} peripheral library interface.

  Description
    This file defines the interface to the ${FLEXCOM_INSTANCE_NAME} ${FLEXCOM_MODE} peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

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

#ifndef PLIB_${FLEXCOM_INSTANCE_NAME}_${FLEXCOM_MODE}_H // Guards against multiple inclusion
#define PLIB_${FLEXCOM_INSTANCE_NAME}_${FLEXCOM_MODE}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_flexcom_usart_local.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

<#--Interface To Use-->
// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
#define ${FLEXCOM_INSTANCE_NAME}_USART_FrequencyGet()    (uint32_t)(${FLEX_USART_CLOCK_FREQ}UL)

<#if FLEXCOM_USART_MR_USART_MODE == "LIN_MASTER" || FLEXCOM_USART_MR_USART_MODE == "LIN_SLAVE">
/****************************** ${FLEXCOM_INSTANCE_NAME} LIN USART API *********************************/
typedef enum
{
    FLEXCOM_LIN_NACT_PUBLISH = FLEX_US_LINMR_NACT_PUBLISH_Val,
    FLEXCOM_LIN_NACT_SUBSCRIBE = FLEX_US_LINMR_NACT_SUBSCRIBE_Val,
    FLEXCOM_LIN_NACT_IGNORE = FLEX_US_LINMR_NACT_IGNORE_Val,

} FLEXCOM_LIN_NACT;

typedef enum
{
    FLEXCOM_LIN_DATA_LEN_DLC = FLEX_US_LINMR_DLM(0U),
    FLEXCOM_LIN_DATA_LEN_IDENTIFIER = FLEX_US_LINMR_DLM(1U),
} FLEXCOM_LIN_DATA_LEN;

typedef enum
{
    FLEXCOM_LIN_2_0_ENHANCHED_CHECKSUM = FLEX_US_LINMR_CHKTYP(0U) ,
    FLEXCOM_LIN_1_3_CLASSIC_CHECKSUM = FLEX_US_LINMR_CHKTYP(1U) ,
} FLEXCOM_LIN_CHECKSUM_TYPE;

typedef void (* FLEXCOM_LIN_CALLBACK)(uintptr_t context );

typedef struct
{
    FLEXCOM_LIN_CALLBACK idCallback;
    
    uintptr_t idContext;
    
    FLEXCOM_LIN_CALLBACK tranferCallback;
    
    uintptr_t tranferContext;
    
    FLEXCOM_LIN_CALLBACK breakCallback;
    
    uintptr_t breakContext;

} FLEXCOM_LIN_CALLBACK_OBJECT;

</#if>
/****************************** ${FLEXCOM_INSTANCE_NAME} USART API *********************************/

void ${FLEXCOM_INSTANCE_NAME}_USART_Initialize( void );

FLEXCOM_USART_ERROR ${FLEXCOM_INSTANCE_NAME}_USART_ErrorGet( void );

bool ${FLEXCOM_INSTANCE_NAME}_USART_SerialSetup( FLEXCOM_USART_SERIAL_SETUP *setup, uint32_t srcClkFreq );

bool ${FLEXCOM_INSTANCE_NAME}_USART_Write( void *buffer, const size_t size );

bool ${FLEXCOM_INSTANCE_NAME}_USART_Read( void *buffer, const size_t size );

<#if FLEXCOM_USART_INTERRUPT_MODE_ENABLE == false>
uint8_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadByte(void);

void ${FLEXCOM_INSTANCE_NAME}_USART_WriteByte(uint8_t data);

bool ${FLEXCOM_INSTANCE_NAME}_USART_TransmitterIsReady( void );

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReceiverIsReady( void );

<#else>
bool ${FLEXCOM_INSTANCE_NAME}_USART_WriteIsBusy( void );

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadIsBusy( void );

size_t ${FLEXCOM_INSTANCE_NAME}_USART_WriteCountGet( void );

size_t ${FLEXCOM_INSTANCE_NAME}_USART_ReadCountGet( void );

bool ${FLEXCOM_INSTANCE_NAME}_USART_ReadAbort(void);

void ${FLEXCOM_INSTANCE_NAME}_USART_WriteCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context );

void ${FLEXCOM_INSTANCE_NAME}_USART_ReadCallbackRegister( FLEXCOM_USART_CALLBACK callback, uintptr_t context );

</#if>
bool ${FLEXCOM_INSTANCE_NAME}_USART_TransmitComplete( void );

<#if FLEXCOM_USART_MR_USART_MODE == "IRDA">
void ${FLEXCOM_INSTANCE_NAME}_USART_IrDA_DirectionSet(FLEXCOM_IRDA_DIR dir);

</#if>
<#if FLEXCOM_USART_MR_USART_MODE == "IS07816_T_0">
void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Icc_Power_On( void );

void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Icc_Power_Off( void );

bool ${FLEXCOM_INSTANCE_NAME}_ISO7816_Card_Detect( void );

void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Vcc_Enable( void );

void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Vcc_Disable( void );

void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Warm_Reset( void );

void ${FLEXCOM_INSTANCE_NAME}_ISO7816_Decode_Atr( uint8_t *p_atr, uint8_t size);

uint8_t ${FLEXCOM_INSTANCE_NAME}_ISO7816_Data_Read_Atr( uint8_t *p_atr );

uint16_t ${FLEXCOM_INSTANCE_NAME}_ISO7816_Xfr_Block_Tpdu( uint8_t *apdu_cmd_buffer, uint8_t *apdu_res_buffer, const size_t apdu_cmd_length );

</#if>
<#if FLEXCOM_USART_MR_USART_MODE == "LIN_MASTER" || FLEXCOM_USART_MR_USART_MODE == "LIN_SLAVE">
void ${FLEXCOM_INSTANCE_NAME}_LIN_NodeActionSet( FLEXCOM_LIN_NACT action );

bool ${FLEXCOM_INSTANCE_NAME}_LIN_IdentifierWrite( uint8_t id);

uint8_t ${FLEXCOM_INSTANCE_NAME}_LIN_IdentifierRead( void);

void ${FLEXCOM_INSTANCE_NAME}_LIN_ParityEnable(bool parityEnable);

void ${FLEXCOM_INSTANCE_NAME}_LIN_ChecksumEnable(bool checksumEnable);

void ${FLEXCOM_INSTANCE_NAME}_LIN_ChecksumTypeSet(FLEXCOM_LIN_CHECKSUM_TYPE checksumType);

<#if FLEXCOM_USART_MR_USART_MODE == "LIN_MASTER">
void ${FLEXCOM_INSTANCE_NAME}_LIN_FrameSlotEnable(bool frameSlotEnable);

</#if>
void ${FLEXCOM_INSTANCE_NAME}_LIN_DataLenModeSet(FLEXCOM_LIN_DATA_LEN dataLenMode);

void ${FLEXCOM_INSTANCE_NAME}_LIN_ResponseDataLenSet(uint8_t len);

uint8_t ${FLEXCOM_INSTANCE_NAME}_LIN_TransferComplete(void);

void FLEXCOM1_LINIdCallbackRegister( FLEXCOM_LIN_CALLBACK callback, uintptr_t context);

void FLEXCOM1_LINTcCallbackRegister( FLEXCOM_LIN_CALLBACK callback, uintptr_t context);

void FLEXCOM1_LINBreakCallbackRegister( FLEXCOM_LIN_CALLBACK callback, uintptr_t context);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif //PLIB_${FLEXCOM_INSTANCE_NAME}_${FLEXCOM_MODE}_H
