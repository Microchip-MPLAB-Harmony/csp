<#--
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
-->

<#if (USART_7816_ENABLE == true)>
void ${SERCOM_INSTANCE_NAME}_ISO7816_Icc_Power_On( void );

void ${SERCOM_INSTANCE_NAME}_ISO7816_Icc_Power_Off( void );

bool ${SERCOM_INSTANCE_NAME}_ISO7816_Card_Detect( void );

void ${SERCOM_INSTANCE_NAME}_ISO7816_Vcc_Enable( void );

void ${SERCOM_INSTANCE_NAME}_ISO7816_Vcc_Disable( void );

void ${SERCOM_INSTANCE_NAME}_ISO7816_Cold_Reset( void );

void ${SERCOM_INSTANCE_NAME}_ISO7816_Warm_Reset( void );

void ${SERCOM_INSTANCE_NAME}_ISO7816_Decode_Atr( uint8_t *p_atr );

uint8_t ${SERCOM_INSTANCE_NAME}_ISO7816_Data_Read_Atr( uint8_t *p_atr );

uint16_t ${SERCOM_INSTANCE_NAME}_ISO7816_Xfr_Block_Tpdu( uint8_t *apdu_cmd_buffer, uint8_t *apdu_res_buffer, const size_t apdu_cmd_length );

</#if>
