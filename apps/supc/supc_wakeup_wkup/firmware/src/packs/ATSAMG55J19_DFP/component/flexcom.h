/**
 * \brief Header file for SAMG/SAMG55 FLEXCOM
 *
 * Copyright (c) 2017-2019 Microchip Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

/* file generated from device description version 2019-05-09T03:59:29Z */
#ifndef SAMG_SAMG55_FLEXCOM_MODULE_H
#define SAMG_SAMG55_FLEXCOM_MODULE_H

/** \addtogroup SAMG_SAMG55 Flexible Serial Communication
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_FLEXCOM                               */
/* ========================================================================== */

/* -------- FLEXCOM_MR : (FLEXCOM Offset: 0x00) (R/W 32) FLEXCOM Mode register -------- */
#define FLEXCOM_MR_OPMODE_Pos                 (0U)                                           /**< (FLEXCOM_MR) FLEXCOM Operating Mode Position */
#define FLEXCOM_MR_OPMODE_Msk                 (0x3U << FLEXCOM_MR_OPMODE_Pos)                /**< (FLEXCOM_MR) FLEXCOM Operating Mode Mask */
#define FLEXCOM_MR_OPMODE(value)              (FLEXCOM_MR_OPMODE_Msk & ((value) << FLEXCOM_MR_OPMODE_Pos))
#define   FLEXCOM_MR_OPMODE_NO_COM_Val        (0U)                                           /**< (FLEXCOM_MR) No communication  */
#define   FLEXCOM_MR_OPMODE_USART_Val         (1U)                                           /**< (FLEXCOM_MR) All related USART related protocols are selected (RS232, RS485, IrDA, ISO7816, LIN,)All SPI/TWI related registers are not accessible and have no impact on IOs.  */
#define   FLEXCOM_MR_OPMODE_SPI_Val           (2U)                                           /**< (FLEXCOM_MR) SPI operating mode is selected.All USART/TWI related registers are not accessible and have no impact on IOs.  */
#define   FLEXCOM_MR_OPMODE_TWI_Val           (3U)                                           /**< (FLEXCOM_MR) All related TWI protocols are selected (TWI, SMBUS). All USART/SPI related registers are not accessible and have no impact on IOs.  */
#define FLEXCOM_MR_OPMODE_NO_COM              (FLEXCOM_MR_OPMODE_NO_COM_Val << FLEXCOM_MR_OPMODE_Pos) /**< (FLEXCOM_MR) No communication Position  */
#define FLEXCOM_MR_OPMODE_USART               (FLEXCOM_MR_OPMODE_USART_Val << FLEXCOM_MR_OPMODE_Pos) /**< (FLEXCOM_MR) All related USART related protocols are selected (RS232, RS485, IrDA, ISO7816, LIN,)All SPI/TWI related registers are not accessible and have no impact on IOs. Position  */
#define FLEXCOM_MR_OPMODE_SPI                 (FLEXCOM_MR_OPMODE_SPI_Val << FLEXCOM_MR_OPMODE_Pos) /**< (FLEXCOM_MR) SPI operating mode is selected.All USART/TWI related registers are not accessible and have no impact on IOs. Position  */
#define FLEXCOM_MR_OPMODE_TWI                 (FLEXCOM_MR_OPMODE_TWI_Val << FLEXCOM_MR_OPMODE_Pos) /**< (FLEXCOM_MR) All related TWI protocols are selected (TWI, SMBUS). All USART/SPI related registers are not accessible and have no impact on IOs. Position  */
#define FLEXCOM_MR_Msk                        (0x00000003UL)                                 /**< (FLEXCOM_MR) Register Mask  */

/* -------- FLEXCOM_RHR : (FLEXCOM Offset: 0x10) (R/  32) FLEXCOM Receive Holding Register -------- */
#define FLEXCOM_RHR_RXDATA_Pos                (0U)                                           /**< (FLEXCOM_RHR) Receive Data Position */
#define FLEXCOM_RHR_RXDATA_Msk                (0xFFFFU << FLEXCOM_RHR_RXDATA_Pos)            /**< (FLEXCOM_RHR) Receive Data Mask */
#define FLEXCOM_RHR_RXDATA(value)             (FLEXCOM_RHR_RXDATA_Msk & ((value) << FLEXCOM_RHR_RXDATA_Pos))
#define FLEXCOM_RHR_Msk                       (0x0000FFFFUL)                                 /**< (FLEXCOM_RHR) Register Mask  */

/* -------- FLEXCOM_THR : (FLEXCOM Offset: 0x20) (R/W 32) FLEXCOM Transmit Holding Register -------- */
#define FLEXCOM_THR_TXDATA_Pos                (0U)                                           /**< (FLEXCOM_THR) Transmit Data Position */
#define FLEXCOM_THR_TXDATA_Msk                (0xFFFFU << FLEXCOM_THR_TXDATA_Pos)            /**< (FLEXCOM_THR) Transmit Data Mask */
#define FLEXCOM_THR_TXDATA(value)             (FLEXCOM_THR_TXDATA_Msk & ((value) << FLEXCOM_THR_TXDATA_Pos))
#define FLEXCOM_THR_Msk                       (0x0000FFFFUL)                                 /**< (FLEXCOM_THR) Register Mask  */

/** \brief FLEXCOM register offsets definitions */
#define FLEXCOM_MR_OFFSET              (0x00)         /**< (FLEXCOM_MR) FLEXCOM Mode register Offset */
#define FLEXCOM_RHR_OFFSET             (0x10)         /**< (FLEXCOM_RHR) FLEXCOM Receive Holding Register Offset */
#define FLEXCOM_THR_OFFSET             (0x20)         /**< (FLEXCOM_THR) FLEXCOM Transmit Holding Register Offset */

/** \brief FLEXCOM register API structure */
typedef struct
{
  __IO  uint32_t                       FLEXCOM_MR;      /**< Offset: 0x00 (R/W  32) FLEXCOM Mode register */
  __I   uint8_t                        Reserved1[0x0C];
  __I   uint32_t                       FLEXCOM_RHR;     /**< Offset: 0x10 (R/   32) FLEXCOM Receive Holding Register */
  __I   uint8_t                        Reserved2[0x0C];
  __IO  uint32_t                       FLEXCOM_THR;     /**< Offset: 0x20 (R/W  32) FLEXCOM Transmit Holding Register */
} flexcom_registers_t;
/** @}  end of Flexible Serial Communication */

#endif /* SAMG_SAMG55_FLEXCOM_MODULE_H */

