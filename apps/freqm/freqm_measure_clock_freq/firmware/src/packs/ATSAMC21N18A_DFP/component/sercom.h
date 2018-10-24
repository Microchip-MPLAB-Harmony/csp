/**
 * \brief Component description for PIC32CM/JH21 SERCOM
 *
 * Copyright (c) 2017 Microchip Technology Inc.
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

/* file generated from device description version 2017-07-25T18:00:00Z */
#ifndef _PIC32CM_JH21_SERCOM_COMPONENT_H_
#define _PIC32CM_JH21_SERCOM_COMPONENT_H_

/** \addtogroup PIC32CM_JH21_SERCOM Serial Communication Interface
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SERCOM */
/* ========================================================================== */


#define SERCOM_I2CM_CTRLA_RESETVALUE        (0x00U)                                       /**<  (SERCOM_I2CM_CTRLA) I2CM Control A  Reset Value */

#define SERCOM_I2CM_CTRLA_SWRST_Pos           (0)                                            /**< (SERCOM_I2CM_CTRLA) Software Reset Position */
#define SERCOM_I2CM_CTRLA_SWRST_Msk           (0x1U << SERCOM_I2CM_CTRLA_SWRST_Pos)          /**< (SERCOM_I2CM_CTRLA) Software Reset Mask */
#define SERCOM_I2CM_CTRLA_ENABLE_Pos          (1)                                            /**< (SERCOM_I2CM_CTRLA) Enable Position */
#define SERCOM_I2CM_CTRLA_ENABLE_Msk          (0x1U << SERCOM_I2CM_CTRLA_ENABLE_Pos)         /**< (SERCOM_I2CM_CTRLA) Enable Mask */
#define SERCOM_I2CM_CTRLA_MODE_Pos            (2)                                            /**< (SERCOM_I2CM_CTRLA) Operating Mode Position */
#define SERCOM_I2CM_CTRLA_MODE_Msk            (0x7U << SERCOM_I2CM_CTRLA_MODE_Pos)           /**< (SERCOM_I2CM_CTRLA) Operating Mode Mask */
#define SERCOM_I2CM_CTRLA_MODE(value)         (SERCOM_I2CM_CTRLA_MODE_Msk & ((value) << SERCOM_I2CM_CTRLA_MODE_Pos))
#define SERCOM_I2CM_CTRLA_RUNSTDBY_Pos        (7)                                            /**< (SERCOM_I2CM_CTRLA) Run in Standby Position */
#define SERCOM_I2CM_CTRLA_RUNSTDBY_Msk        (0x1U << SERCOM_I2CM_CTRLA_RUNSTDBY_Pos)       /**< (SERCOM_I2CM_CTRLA) Run in Standby Mask */
#define SERCOM_I2CM_CTRLA_PINOUT_Pos          (16)                                           /**< (SERCOM_I2CM_CTRLA) Pin Usage Position */
#define SERCOM_I2CM_CTRLA_PINOUT_Msk          (0x1U << SERCOM_I2CM_CTRLA_PINOUT_Pos)         /**< (SERCOM_I2CM_CTRLA) Pin Usage Mask */
#define SERCOM_I2CM_CTRLA_SDAHOLD_Pos         (20)                                           /**< (SERCOM_I2CM_CTRLA) SDA Hold Time Position */
#define SERCOM_I2CM_CTRLA_SDAHOLD_Msk         (0x3U << SERCOM_I2CM_CTRLA_SDAHOLD_Pos)        /**< (SERCOM_I2CM_CTRLA) SDA Hold Time Mask */
#define SERCOM_I2CM_CTRLA_SDAHOLD(value)      (SERCOM_I2CM_CTRLA_SDAHOLD_Msk & ((value) << SERCOM_I2CM_CTRLA_SDAHOLD_Pos))
#define SERCOM_I2CM_CTRLA_MEXTTOEN_Pos        (22)                                           /**< (SERCOM_I2CM_CTRLA) Master SCL Low Extend Timeout Position */
#define SERCOM_I2CM_CTRLA_MEXTTOEN_Msk        (0x1U << SERCOM_I2CM_CTRLA_MEXTTOEN_Pos)       /**< (SERCOM_I2CM_CTRLA) Master SCL Low Extend Timeout Mask */
#define SERCOM_I2CM_CTRLA_SEXTTOEN_Pos        (23)                                           /**< (SERCOM_I2CM_CTRLA) Slave SCL Low Extend Timeout Position */
#define SERCOM_I2CM_CTRLA_SEXTTOEN_Msk        (0x1U << SERCOM_I2CM_CTRLA_SEXTTOEN_Pos)       /**< (SERCOM_I2CM_CTRLA) Slave SCL Low Extend Timeout Mask */
#define SERCOM_I2CM_CTRLA_SPEED_Pos           (24)                                           /**< (SERCOM_I2CM_CTRLA) Transfer Speed Position */
#define SERCOM_I2CM_CTRLA_SPEED_Msk           (0x3U << SERCOM_I2CM_CTRLA_SPEED_Pos)          /**< (SERCOM_I2CM_CTRLA) Transfer Speed Mask */
#define SERCOM_I2CM_CTRLA_SPEED(value)        (SERCOM_I2CM_CTRLA_SPEED_Msk & ((value) << SERCOM_I2CM_CTRLA_SPEED_Pos))
#define SERCOM_I2CM_CTRLA_SCLSM_Pos           (27)                                           /**< (SERCOM_I2CM_CTRLA) SCL Clock Stretch Mode Position */
#define SERCOM_I2CM_CTRLA_SCLSM_Msk           (0x1U << SERCOM_I2CM_CTRLA_SCLSM_Pos)          /**< (SERCOM_I2CM_CTRLA) SCL Clock Stretch Mode Mask */
#define SERCOM_I2CM_CTRLA_INACTOUT_Pos        (28)                                           /**< (SERCOM_I2CM_CTRLA) Inactive Time-Out Position */
#define SERCOM_I2CM_CTRLA_INACTOUT_Msk        (0x3U << SERCOM_I2CM_CTRLA_INACTOUT_Pos)       /**< (SERCOM_I2CM_CTRLA) Inactive Time-Out Mask */
#define SERCOM_I2CM_CTRLA_INACTOUT(value)     (SERCOM_I2CM_CTRLA_INACTOUT_Msk & ((value) << SERCOM_I2CM_CTRLA_INACTOUT_Pos))
#define SERCOM_I2CM_CTRLA_LOWTOUTEN_Pos       (30)                                           /**< (SERCOM_I2CM_CTRLA) SCL Low Timeout Enable Position */
#define SERCOM_I2CM_CTRLA_LOWTOUTEN_Msk       (0x1U << SERCOM_I2CM_CTRLA_LOWTOUTEN_Pos)      /**< (SERCOM_I2CM_CTRLA) SCL Low Timeout Enable Mask */
#define SERCOM_I2CM_CTRLA_Msk                 (0x7BF1009FUL)                                 /**< (SERCOM_I2CM_CTRLA) Register Mask  */

#define SERCOM_I2CM_CTRLB_RESETVALUE        (0x00U)                                       /**<  (SERCOM_I2CM_CTRLB) I2CM Control B  Reset Value */

#define SERCOM_I2CM_CTRLB_SMEN_Pos            (8)                                            /**< (SERCOM_I2CM_CTRLB) Smart Mode Enable Position */
#define SERCOM_I2CM_CTRLB_SMEN_Msk            (0x1U << SERCOM_I2CM_CTRLB_SMEN_Pos)           /**< (SERCOM_I2CM_CTRLB) Smart Mode Enable Mask */
#define SERCOM_I2CM_CTRLB_QCEN_Pos            (9)                                            /**< (SERCOM_I2CM_CTRLB) Quick Command Enable Position */
#define SERCOM_I2CM_CTRLB_QCEN_Msk            (0x1U << SERCOM_I2CM_CTRLB_QCEN_Pos)           /**< (SERCOM_I2CM_CTRLB) Quick Command Enable Mask */
#define SERCOM_I2CM_CTRLB_CMD_Pos             (16)                                           /**< (SERCOM_I2CM_CTRLB) Command Position */
#define SERCOM_I2CM_CTRLB_CMD_Msk             (0x3U << SERCOM_I2CM_CTRLB_CMD_Pos)            /**< (SERCOM_I2CM_CTRLB) Command Mask */
#define SERCOM_I2CM_CTRLB_CMD(value)          (SERCOM_I2CM_CTRLB_CMD_Msk & ((value) << SERCOM_I2CM_CTRLB_CMD_Pos))
#define SERCOM_I2CM_CTRLB_ACKACT_Pos          (18)                                           /**< (SERCOM_I2CM_CTRLB) Acknowledge Action Position */
#define SERCOM_I2CM_CTRLB_ACKACT_Msk          (0x1U << SERCOM_I2CM_CTRLB_ACKACT_Pos)         /**< (SERCOM_I2CM_CTRLB) Acknowledge Action Mask */
#define SERCOM_I2CM_CTRLB_Msk                 (0x00070300UL)                                 /**< (SERCOM_I2CM_CTRLB) Register Mask  */

/* -------- SERCOM_I2CM_BAUD : (SERCOM Offset: 0x0c) (R/W 32) I2CM Baud Rate -------- */

#define SERCOM_I2CM_BAUD_RESETVALUE         (0x00U)                                       /**<  (SERCOM_I2CM_BAUD) I2CM Baud Rate  Reset Value */

#define SERCOM_I2CM_BAUD_BAUD_Pos             (0)                                            /**< (SERCOM_I2CM_BAUD) Baud Rate Value Position */
#define SERCOM_I2CM_BAUD_BAUD_Msk             (0xFFU << SERCOM_I2CM_BAUD_BAUD_Pos)           /**< (SERCOM_I2CM_BAUD) Baud Rate Value Mask */
#define SERCOM_I2CM_BAUD_BAUD(value)          (SERCOM_I2CM_BAUD_BAUD_Msk & ((value) << SERCOM_I2CM_BAUD_BAUD_Pos))
#define SERCOM_I2CM_BAUD_BAUDLOW_Pos          (8)                                            /**< (SERCOM_I2CM_BAUD) Baud Rate Value Low Position */
#define SERCOM_I2CM_BAUD_BAUDLOW_Msk          (0xFFU << SERCOM_I2CM_BAUD_BAUDLOW_Pos)        /**< (SERCOM_I2CM_BAUD) Baud Rate Value Low Mask */
#define SERCOM_I2CM_BAUD_BAUDLOW(value)       (SERCOM_I2CM_BAUD_BAUDLOW_Msk & ((value) << SERCOM_I2CM_BAUD_BAUDLOW_Pos))
#define SERCOM_I2CM_BAUD_HSBAUD_Pos           (16)                                           /**< (SERCOM_I2CM_BAUD) High Speed Baud Rate Value Position */
#define SERCOM_I2CM_BAUD_HSBAUD_Msk           (0xFFU << SERCOM_I2CM_BAUD_HSBAUD_Pos)         /**< (SERCOM_I2CM_BAUD) High Speed Baud Rate Value Mask */
#define SERCOM_I2CM_BAUD_HSBAUD(value)        (SERCOM_I2CM_BAUD_HSBAUD_Msk & ((value) << SERCOM_I2CM_BAUD_HSBAUD_Pos))
#define SERCOM_I2CM_BAUD_HSBAUDLOW_Pos        (24)                                           /**< (SERCOM_I2CM_BAUD) High Speed Baud Rate Value Low Position */
#define SERCOM_I2CM_BAUD_HSBAUDLOW_Msk        (0xFFU << SERCOM_I2CM_BAUD_HSBAUDLOW_Pos)      /**< (SERCOM_I2CM_BAUD) High Speed Baud Rate Value Low Mask */
#define SERCOM_I2CM_BAUD_HSBAUDLOW(value)     (SERCOM_I2CM_BAUD_HSBAUDLOW_Msk & ((value) << SERCOM_I2CM_BAUD_HSBAUDLOW_Pos))
#define SERCOM_I2CM_BAUD_Msk                  (0xFFFFFFFFUL)                                 /**< (SERCOM_I2CM_BAUD) Register Mask  */


#define SERCOM_I2CM_INTENCLR_RESETVALUE     (0x00U)                                       /**<  (SERCOM_I2CM_INTENCLR) I2CM Interrupt Enable Clear  Reset Value */

#define SERCOM_I2CM_INTENCLR_MB_Pos           (0)                                            /**< (SERCOM_I2CM_INTENCLR) Master On Bus Interrupt Disable Position */
#define SERCOM_I2CM_INTENCLR_MB_Msk           (0x1U << SERCOM_I2CM_INTENCLR_MB_Pos)          /**< (SERCOM_I2CM_INTENCLR) Master On Bus Interrupt Disable Mask */
#define SERCOM_I2CM_INTENCLR_SB_Pos           (1)                                            /**< (SERCOM_I2CM_INTENCLR) Slave On Bus Interrupt Disable Position */
#define SERCOM_I2CM_INTENCLR_SB_Msk           (0x1U << SERCOM_I2CM_INTENCLR_SB_Pos)          /**< (SERCOM_I2CM_INTENCLR) Slave On Bus Interrupt Disable Mask */
#define SERCOM_I2CM_INTENCLR_ERROR_Pos        (7)                                            /**< (SERCOM_I2CM_INTENCLR) Combined Error Interrupt Disable Position */
#define SERCOM_I2CM_INTENCLR_ERROR_Msk        (0x1U << SERCOM_I2CM_INTENCLR_ERROR_Pos)       /**< (SERCOM_I2CM_INTENCLR) Combined Error Interrupt Disable Mask */
#define SERCOM_I2CM_INTENCLR_Msk              (0x00000083UL)                                 /**< (SERCOM_I2CM_INTENCLR) Register Mask  */


#define SERCOM_I2CM_INTENSET_RESETVALUE     (0x00U)                                       /**<  (SERCOM_I2CM_INTENSET) I2CM Interrupt Enable Set  Reset Value */

#define SERCOM_I2CM_INTENSET_MB_Pos           (0)                                            /**< (SERCOM_I2CM_INTENSET) Master On Bus Interrupt Enable Position */
#define SERCOM_I2CM_INTENSET_MB_Msk           (0x1U << SERCOM_I2CM_INTENSET_MB_Pos)          /**< (SERCOM_I2CM_INTENSET) Master On Bus Interrupt Enable Mask */
#define SERCOM_I2CM_INTENSET_SB_Pos           (1)                                            /**< (SERCOM_I2CM_INTENSET) Slave On Bus Interrupt Enable Position */
#define SERCOM_I2CM_INTENSET_SB_Msk           (0x1U << SERCOM_I2CM_INTENSET_SB_Pos)          /**< (SERCOM_I2CM_INTENSET) Slave On Bus Interrupt Enable Mask */
#define SERCOM_I2CM_INTENSET_ERROR_Pos        (7)                                            /**< (SERCOM_I2CM_INTENSET) Combined Error Interrupt Enable Position */
#define SERCOM_I2CM_INTENSET_ERROR_Msk        (0x1U << SERCOM_I2CM_INTENSET_ERROR_Pos)       /**< (SERCOM_I2CM_INTENSET) Combined Error Interrupt Enable Mask */
#define SERCOM_I2CM_INTENSET_Msk              (0x00000083UL)                                 /**< (SERCOM_I2CM_INTENSET) Register Mask  */


#define SERCOM_I2CM_INTFLAG_RESETVALUE      (0x00U)                                       /**<  (SERCOM_I2CM_INTFLAG) I2CM Interrupt Flag Status and Clear  Reset Value */

#define SERCOM_I2CM_INTFLAG_MB_Pos            (0)                                            /**< (SERCOM_I2CM_INTFLAG) Master On Bus Interrupt Position */
#define SERCOM_I2CM_INTFLAG_MB_Msk            (0x1U << SERCOM_I2CM_INTFLAG_MB_Pos)           /**< (SERCOM_I2CM_INTFLAG) Master On Bus Interrupt Mask */
#define SERCOM_I2CM_INTFLAG_SB_Pos            (1)                                            /**< (SERCOM_I2CM_INTFLAG) Slave On Bus Interrupt Position */
#define SERCOM_I2CM_INTFLAG_SB_Msk            (0x1U << SERCOM_I2CM_INTFLAG_SB_Pos)           /**< (SERCOM_I2CM_INTFLAG) Slave On Bus Interrupt Mask */
#define SERCOM_I2CM_INTFLAG_ERROR_Pos         (7)                                            /**< (SERCOM_I2CM_INTFLAG) Combined Error Interrupt Position */
#define SERCOM_I2CM_INTFLAG_ERROR_Msk         (0x1U << SERCOM_I2CM_INTFLAG_ERROR_Pos)        /**< (SERCOM_I2CM_INTFLAG) Combined Error Interrupt Mask */
#define SERCOM_I2CM_INTFLAG_Msk               (0x00000083UL)                                 /**< (SERCOM_I2CM_INTFLAG) Register Mask  */


#define SERCOM_I2CM_STATUS_RESETVALUE       (0x00U)                                       /**<  (SERCOM_I2CM_STATUS) I2CM Status  Reset Value */

#define SERCOM_I2CM_STATUS_BUSERR_Pos         (0)                                            /**< (SERCOM_I2CM_STATUS) Bus Error Position */
#define SERCOM_I2CM_STATUS_BUSERR_Msk         (0x1U << SERCOM_I2CM_STATUS_BUSERR_Pos)        /**< (SERCOM_I2CM_STATUS) Bus Error Mask */
#define SERCOM_I2CM_STATUS_ARBLOST_Pos        (1)                                            /**< (SERCOM_I2CM_STATUS) Arbitration Lost Position */
#define SERCOM_I2CM_STATUS_ARBLOST_Msk        (0x1U << SERCOM_I2CM_STATUS_ARBLOST_Pos)       /**< (SERCOM_I2CM_STATUS) Arbitration Lost Mask */
#define SERCOM_I2CM_STATUS_RXNACK_Pos         (2)                                            /**< (SERCOM_I2CM_STATUS) Received Not Acknowledge Position */
#define SERCOM_I2CM_STATUS_RXNACK_Msk         (0x1U << SERCOM_I2CM_STATUS_RXNACK_Pos)        /**< (SERCOM_I2CM_STATUS) Received Not Acknowledge Mask */
#define SERCOM_I2CM_STATUS_BUSSTATE_Pos       (4)                                            /**< (SERCOM_I2CM_STATUS) Bus State Position */
#define SERCOM_I2CM_STATUS_BUSSTATE_Msk       (0x3U << SERCOM_I2CM_STATUS_BUSSTATE_Pos)      /**< (SERCOM_I2CM_STATUS) Bus State Mask */
#define SERCOM_I2CM_STATUS_BUSSTATE(value)    (SERCOM_I2CM_STATUS_BUSSTATE_Msk & ((value) << SERCOM_I2CM_STATUS_BUSSTATE_Pos))
#define SERCOM_I2CM_STATUS_LOWTOUT_Pos        (6)                                            /**< (SERCOM_I2CM_STATUS) SCL Low Timeout Position */
#define SERCOM_I2CM_STATUS_LOWTOUT_Msk        (0x1U << SERCOM_I2CM_STATUS_LOWTOUT_Pos)       /**< (SERCOM_I2CM_STATUS) SCL Low Timeout Mask */
#define SERCOM_I2CM_STATUS_CLKHOLD_Pos        (7)                                            /**< (SERCOM_I2CM_STATUS) Clock Hold Position */
#define SERCOM_I2CM_STATUS_CLKHOLD_Msk        (0x1U << SERCOM_I2CM_STATUS_CLKHOLD_Pos)       /**< (SERCOM_I2CM_STATUS) Clock Hold Mask */
#define SERCOM_I2CM_STATUS_MEXTTOUT_Pos       (8)                                            /**< (SERCOM_I2CM_STATUS) Master SCL Low Extend Timeout Position */
#define SERCOM_I2CM_STATUS_MEXTTOUT_Msk       (0x1U << SERCOM_I2CM_STATUS_MEXTTOUT_Pos)      /**< (SERCOM_I2CM_STATUS) Master SCL Low Extend Timeout Mask */
#define SERCOM_I2CM_STATUS_SEXTTOUT_Pos       (9)                                            /**< (SERCOM_I2CM_STATUS) Slave SCL Low Extend Timeout Position */
#define SERCOM_I2CM_STATUS_SEXTTOUT_Msk       (0x1U << SERCOM_I2CM_STATUS_SEXTTOUT_Pos)      /**< (SERCOM_I2CM_STATUS) Slave SCL Low Extend Timeout Mask */
#define SERCOM_I2CM_STATUS_LENERR_Pos         (10)                                           /**< (SERCOM_I2CM_STATUS) Length Error Position */
#define SERCOM_I2CM_STATUS_LENERR_Msk         (0x1U << SERCOM_I2CM_STATUS_LENERR_Pos)        /**< (SERCOM_I2CM_STATUS) Length Error Mask */
#define SERCOM_I2CM_STATUS_Msk                (0x000007F7UL)                                 /**< (SERCOM_I2CM_STATUS) Register Mask  */

#define SERCOM_I2CM_SYNCBUSY_RESETVALUE     (0x00U)                                       /**<  (SERCOM_I2CM_SYNCBUSY) I2CM Synchronization Busy  Reset Value */

#define SERCOM_I2CM_SYNCBUSY_SWRST_Pos        (0)                                            /**< (SERCOM_I2CM_SYNCBUSY) Software Reset Synchronization Busy Position */
#define SERCOM_I2CM_SYNCBUSY_SWRST_Msk        (0x1U << SERCOM_I2CM_SYNCBUSY_SWRST_Pos)       /**< (SERCOM_I2CM_SYNCBUSY) Software Reset Synchronization Busy Mask */
#define SERCOM_I2CM_SYNCBUSY_ENABLE_Pos       (1)                                            /**< (SERCOM_I2CM_SYNCBUSY) SERCOM Enable Synchronization Busy Position */
#define SERCOM_I2CM_SYNCBUSY_ENABLE_Msk       (0x1U << SERCOM_I2CM_SYNCBUSY_ENABLE_Pos)      /**< (SERCOM_I2CM_SYNCBUSY) SERCOM Enable Synchronization Busy Mask */
#define SERCOM_I2CM_SYNCBUSY_SYSOP_Pos        (2)                                            /**< (SERCOM_I2CM_SYNCBUSY) System Operation Synchronization Busy Position */
#define SERCOM_I2CM_SYNCBUSY_SYSOP_Msk        (0x1U << SERCOM_I2CM_SYNCBUSY_SYSOP_Pos)       /**< (SERCOM_I2CM_SYNCBUSY) System Operation Synchronization Busy Mask */
#define SERCOM_I2CM_SYNCBUSY_Msk              (0x00000007UL)                                 /**< (SERCOM_I2CM_SYNCBUSY) Register Mask  */


#define SERCOM_I2CM_ADDR_RESETVALUE         (0x00U)                                       /**<  (SERCOM_I2CM_ADDR) I2CM Address  Reset Value */

#define SERCOM_I2CM_ADDR_ADDR_Pos             (0)                                            /**< (SERCOM_I2CM_ADDR) Address Value Position */
#define SERCOM_I2CM_ADDR_ADDR_Msk             (0x7FFU << SERCOM_I2CM_ADDR_ADDR_Pos)          /**< (SERCOM_I2CM_ADDR) Address Value Mask */
#define SERCOM_I2CM_ADDR_ADDR(value)          (SERCOM_I2CM_ADDR_ADDR_Msk & ((value) << SERCOM_I2CM_ADDR_ADDR_Pos))
#define SERCOM_I2CM_ADDR_LENEN_Pos            (13)                                           /**< (SERCOM_I2CM_ADDR) Length Enable Position */
#define SERCOM_I2CM_ADDR_LENEN_Msk            (0x1U << SERCOM_I2CM_ADDR_LENEN_Pos)           /**< (SERCOM_I2CM_ADDR) Length Enable Mask */
#define SERCOM_I2CM_ADDR_HS_Pos               (14)                                           /**< (SERCOM_I2CM_ADDR) High Speed Mode Position */
#define SERCOM_I2CM_ADDR_HS_Msk               (0x1U << SERCOM_I2CM_ADDR_HS_Pos)              /**< (SERCOM_I2CM_ADDR) High Speed Mode Mask */
#define SERCOM_I2CM_ADDR_TENBITEN_Pos         (15)                                           /**< (SERCOM_I2CM_ADDR) Ten Bit Addressing Enable Position */
#define SERCOM_I2CM_ADDR_TENBITEN_Msk         (0x1U << SERCOM_I2CM_ADDR_TENBITEN_Pos)        /**< (SERCOM_I2CM_ADDR) Ten Bit Addressing Enable Mask */
#define SERCOM_I2CM_ADDR_LEN_Pos              (16)                                           /**< (SERCOM_I2CM_ADDR) Length Position */
#define SERCOM_I2CM_ADDR_LEN_Msk              (0xFFU << SERCOM_I2CM_ADDR_LEN_Pos)            /**< (SERCOM_I2CM_ADDR) Length Mask */
#define SERCOM_I2CM_ADDR_LEN(value)           (SERCOM_I2CM_ADDR_LEN_Msk & ((value) << SERCOM_I2CM_ADDR_LEN_Pos))
#define SERCOM_I2CM_ADDR_Msk                  (0x00FFE7FFUL)                                 /**< (SERCOM_I2CM_ADDR) Register Mask  */

#define SERCOM_I2CM_DATA_RESETVALUE         (0x00U)                                       /**<  (SERCOM_I2CM_DATA) I2CM Data  Reset Value */

#define SERCOM_I2CM_DATA_DATA_Pos             (0)                                            /**< (SERCOM_I2CM_DATA) Data Value Position */
#define SERCOM_I2CM_DATA_DATA_Msk             (0xFFU << SERCOM_I2CM_DATA_DATA_Pos)           /**< (SERCOM_I2CM_DATA) Data Value Mask */
#define SERCOM_I2CM_DATA_DATA(value)          (SERCOM_I2CM_DATA_DATA_Msk & ((value) << SERCOM_I2CM_DATA_DATA_Pos))
#define SERCOM_I2CM_DATA_Msk                  (0x000000FFUL)                                 /**< (SERCOM_I2CM_DATA) Register Mask  */


#define SERCOM_I2CM_DBGCTRL_RESETVALUE      (0x00U)                                       /**<  (SERCOM_I2CM_DBGCTRL) I2CM Debug Control  Reset Value */

#define SERCOM_I2CM_DBGCTRL_DBGSTOP_Pos       (0)                                            /**< (SERCOM_I2CM_DBGCTRL) Debug Mode Position */
#define SERCOM_I2CM_DBGCTRL_DBGSTOP_Msk       (0x1U << SERCOM_I2CM_DBGCTRL_DBGSTOP_Pos)      /**< (SERCOM_I2CM_DBGCTRL) Debug Mode Mask */
#define SERCOM_I2CM_DBGCTRL_Msk               (0x00000001UL)                                 /**< (SERCOM_I2CM_DBGCTRL) Register Mask  */


#define SERCOM_I2CS_CTRLA_RESETVALUE        (0x00U)                                       /**<  (SERCOM_I2CS_CTRLA) I2CS Control A  Reset Value */

#define SERCOM_I2CS_CTRLA_SWRST_Pos           (0)                                            /**< (SERCOM_I2CS_CTRLA) Software Reset Position */
#define SERCOM_I2CS_CTRLA_SWRST_Msk           (0x1U << SERCOM_I2CS_CTRLA_SWRST_Pos)          /**< (SERCOM_I2CS_CTRLA) Software Reset Mask */
#define SERCOM_I2CS_CTRLA_ENABLE_Pos          (1)                                            /**< (SERCOM_I2CS_CTRLA) Enable Position */
#define SERCOM_I2CS_CTRLA_ENABLE_Msk          (0x1U << SERCOM_I2CS_CTRLA_ENABLE_Pos)         /**< (SERCOM_I2CS_CTRLA) Enable Mask */
#define SERCOM_I2CS_CTRLA_MODE_Pos            (2)                                            /**< (SERCOM_I2CS_CTRLA) Operating Mode Position */
#define SERCOM_I2CS_CTRLA_MODE_Msk            (0x7U << SERCOM_I2CS_CTRLA_MODE_Pos)           /**< (SERCOM_I2CS_CTRLA) Operating Mode Mask */
#define SERCOM_I2CS_CTRLA_MODE(value)         (SERCOM_I2CS_CTRLA_MODE_Msk & ((value) << SERCOM_I2CS_CTRLA_MODE_Pos))
#define SERCOM_I2CS_CTRLA_RUNSTDBY_Pos        (7)                                            /**< (SERCOM_I2CS_CTRLA) Run during Standby Position */
#define SERCOM_I2CS_CTRLA_RUNSTDBY_Msk        (0x1U << SERCOM_I2CS_CTRLA_RUNSTDBY_Pos)       /**< (SERCOM_I2CS_CTRLA) Run during Standby Mask */
#define SERCOM_I2CS_CTRLA_PINOUT_Pos          (16)                                           /**< (SERCOM_I2CS_CTRLA) Pin Usage Position */
#define SERCOM_I2CS_CTRLA_PINOUT_Msk          (0x1U << SERCOM_I2CS_CTRLA_PINOUT_Pos)         /**< (SERCOM_I2CS_CTRLA) Pin Usage Mask */
#define SERCOM_I2CS_CTRLA_SDAHOLD_Pos         (20)                                           /**< (SERCOM_I2CS_CTRLA) SDA Hold Time Position */
#define SERCOM_I2CS_CTRLA_SDAHOLD_Msk         (0x3U << SERCOM_I2CS_CTRLA_SDAHOLD_Pos)        /**< (SERCOM_I2CS_CTRLA) SDA Hold Time Mask */
#define SERCOM_I2CS_CTRLA_SDAHOLD(value)      (SERCOM_I2CS_CTRLA_SDAHOLD_Msk & ((value) << SERCOM_I2CS_CTRLA_SDAHOLD_Pos))
#define SERCOM_I2CS_CTRLA_SEXTTOEN_Pos        (23)                                           /**< (SERCOM_I2CS_CTRLA) Slave SCL Low Extend Timeout Position */
#define SERCOM_I2CS_CTRLA_SEXTTOEN_Msk        (0x1U << SERCOM_I2CS_CTRLA_SEXTTOEN_Pos)       /**< (SERCOM_I2CS_CTRLA) Slave SCL Low Extend Timeout Mask */
#define SERCOM_I2CS_CTRLA_SPEED_Pos           (24)                                           /**< (SERCOM_I2CS_CTRLA) Transfer Speed Position */
#define SERCOM_I2CS_CTRLA_SPEED_Msk           (0x3U << SERCOM_I2CS_CTRLA_SPEED_Pos)          /**< (SERCOM_I2CS_CTRLA) Transfer Speed Mask */
#define SERCOM_I2CS_CTRLA_SPEED(value)        (SERCOM_I2CS_CTRLA_SPEED_Msk & ((value) << SERCOM_I2CS_CTRLA_SPEED_Pos))
#define SERCOM_I2CS_CTRLA_SCLSM_Pos           (27)                                           /**< (SERCOM_I2CS_CTRLA) SCL Clock Stretch Mode Position */
#define SERCOM_I2CS_CTRLA_SCLSM_Msk           (0x1U << SERCOM_I2CS_CTRLA_SCLSM_Pos)          /**< (SERCOM_I2CS_CTRLA) SCL Clock Stretch Mode Mask */
#define SERCOM_I2CS_CTRLA_LOWTOUTEN_Pos       (30)                                           /**< (SERCOM_I2CS_CTRLA) SCL Low Timeout Enable Position */
#define SERCOM_I2CS_CTRLA_LOWTOUTEN_Msk       (0x1U << SERCOM_I2CS_CTRLA_LOWTOUTEN_Pos)      /**< (SERCOM_I2CS_CTRLA) SCL Low Timeout Enable Mask */
#define SERCOM_I2CS_CTRLA_Msk                 (0x4BB1009FUL)                                 /**< (SERCOM_I2CS_CTRLA) Register Mask  */


#define SERCOM_I2CS_CTRLB_RESETVALUE        (0x00U)                                       /**<  (SERCOM_I2CS_CTRLB) I2CS Control B  Reset Value */

#define SERCOM_I2CS_CTRLB_SMEN_Pos            (8)                                            /**< (SERCOM_I2CS_CTRLB) Smart Mode Enable Position */
#define SERCOM_I2CS_CTRLB_SMEN_Msk            (0x1U << SERCOM_I2CS_CTRLB_SMEN_Pos)           /**< (SERCOM_I2CS_CTRLB) Smart Mode Enable Mask */
#define SERCOM_I2CS_CTRLB_GCMD_Pos            (9)                                            /**< (SERCOM_I2CS_CTRLB) PMBus Group Command Position */
#define SERCOM_I2CS_CTRLB_GCMD_Msk            (0x1U << SERCOM_I2CS_CTRLB_GCMD_Pos)           /**< (SERCOM_I2CS_CTRLB) PMBus Group Command Mask */
#define SERCOM_I2CS_CTRLB_AACKEN_Pos          (10)                                           /**< (SERCOM_I2CS_CTRLB) Automatic Address Acknowledge Position */
#define SERCOM_I2CS_CTRLB_AACKEN_Msk          (0x1U << SERCOM_I2CS_CTRLB_AACKEN_Pos)         /**< (SERCOM_I2CS_CTRLB) Automatic Address Acknowledge Mask */
#define SERCOM_I2CS_CTRLB_AMODE_Pos           (14)                                           /**< (SERCOM_I2CS_CTRLB) Address Mode Position */
#define SERCOM_I2CS_CTRLB_AMODE_Msk           (0x3U << SERCOM_I2CS_CTRLB_AMODE_Pos)          /**< (SERCOM_I2CS_CTRLB) Address Mode Mask */
#define SERCOM_I2CS_CTRLB_AMODE(value)        (SERCOM_I2CS_CTRLB_AMODE_Msk & ((value) << SERCOM_I2CS_CTRLB_AMODE_Pos))
#define SERCOM_I2CS_CTRLB_CMD_Pos             (16)                                           /**< (SERCOM_I2CS_CTRLB) Command Position */
#define SERCOM_I2CS_CTRLB_CMD_Msk             (0x3U << SERCOM_I2CS_CTRLB_CMD_Pos)            /**< (SERCOM_I2CS_CTRLB) Command Mask */
#define SERCOM_I2CS_CTRLB_CMD(value)          (SERCOM_I2CS_CTRLB_CMD_Msk & ((value) << SERCOM_I2CS_CTRLB_CMD_Pos))
#define SERCOM_I2CS_CTRLB_ACKACT_Pos          (18)                                           /**< (SERCOM_I2CS_CTRLB) Acknowledge Action Position */
#define SERCOM_I2CS_CTRLB_ACKACT_Msk          (0x1U << SERCOM_I2CS_CTRLB_ACKACT_Pos)         /**< (SERCOM_I2CS_CTRLB) Acknowledge Action Mask */
#define SERCOM_I2CS_CTRLB_Msk                 (0x0007C700UL)                                 /**< (SERCOM_I2CS_CTRLB) Register Mask  */


#define SERCOM_I2CS_INTENCLR_RESETVALUE     (0x00U)                                       /**<  (SERCOM_I2CS_INTENCLR) I2CS Interrupt Enable Clear  Reset Value */

#define SERCOM_I2CS_INTENCLR_PREC_Pos         (0)                                            /**< (SERCOM_I2CS_INTENCLR) Stop Received Interrupt Disable Position */
#define SERCOM_I2CS_INTENCLR_PREC_Msk         (0x1U << SERCOM_I2CS_INTENCLR_PREC_Pos)        /**< (SERCOM_I2CS_INTENCLR) Stop Received Interrupt Disable Mask */
#define SERCOM_I2CS_INTENCLR_AMATCH_Pos       (1)                                            /**< (SERCOM_I2CS_INTENCLR) Address Match Interrupt Disable Position */
#define SERCOM_I2CS_INTENCLR_AMATCH_Msk       (0x1U << SERCOM_I2CS_INTENCLR_AMATCH_Pos)      /**< (SERCOM_I2CS_INTENCLR) Address Match Interrupt Disable Mask */
#define SERCOM_I2CS_INTENCLR_DRDY_Pos         (2)                                            /**< (SERCOM_I2CS_INTENCLR) Data Interrupt Disable Position */
#define SERCOM_I2CS_INTENCLR_DRDY_Msk         (0x1U << SERCOM_I2CS_INTENCLR_DRDY_Pos)        /**< (SERCOM_I2CS_INTENCLR) Data Interrupt Disable Mask */
#define SERCOM_I2CS_INTENCLR_ERROR_Pos        (7)                                            /**< (SERCOM_I2CS_INTENCLR) Combined Error Interrupt Disable Position */
#define SERCOM_I2CS_INTENCLR_ERROR_Msk        (0x1U << SERCOM_I2CS_INTENCLR_ERROR_Pos)       /**< (SERCOM_I2CS_INTENCLR) Combined Error Interrupt Disable Mask */
#define SERCOM_I2CS_INTENCLR_Msk              (0x00000087UL)                                 /**< (SERCOM_I2CS_INTENCLR) Register Mask  */


#define SERCOM_I2CS_INTENSET_RESETVALUE     (0x00U)                                       /**<  (SERCOM_I2CS_INTENSET) I2CS Interrupt Enable Set  Reset Value */

#define SERCOM_I2CS_INTENSET_PREC_Pos         (0)                                            /**< (SERCOM_I2CS_INTENSET) Stop Received Interrupt Enable Position */
#define SERCOM_I2CS_INTENSET_PREC_Msk         (0x1U << SERCOM_I2CS_INTENSET_PREC_Pos)        /**< (SERCOM_I2CS_INTENSET) Stop Received Interrupt Enable Mask */
#define SERCOM_I2CS_INTENSET_AMATCH_Pos       (1)                                            /**< (SERCOM_I2CS_INTENSET) Address Match Interrupt Enable Position */
#define SERCOM_I2CS_INTENSET_AMATCH_Msk       (0x1U << SERCOM_I2CS_INTENSET_AMATCH_Pos)      /**< (SERCOM_I2CS_INTENSET) Address Match Interrupt Enable Mask */
#define SERCOM_I2CS_INTENSET_DRDY_Pos         (2)                                            /**< (SERCOM_I2CS_INTENSET) Data Interrupt Enable Position */
#define SERCOM_I2CS_INTENSET_DRDY_Msk         (0x1U << SERCOM_I2CS_INTENSET_DRDY_Pos)        /**< (SERCOM_I2CS_INTENSET) Data Interrupt Enable Mask */
#define SERCOM_I2CS_INTENSET_ERROR_Pos        (7)                                            /**< (SERCOM_I2CS_INTENSET) Combined Error Interrupt Enable Position */
#define SERCOM_I2CS_INTENSET_ERROR_Msk        (0x1U << SERCOM_I2CS_INTENSET_ERROR_Pos)       /**< (SERCOM_I2CS_INTENSET) Combined Error Interrupt Enable Mask */
#define SERCOM_I2CS_INTENSET_Msk              (0x00000087UL)                                 /**< (SERCOM_I2CS_INTENSET) Register Mask  */


#define SERCOM_I2CS_INTFLAG_RESETVALUE      (0x00U)                                       /**<  (SERCOM_I2CS_INTFLAG) I2CS Interrupt Flag Status and Clear  Reset Value */

#define SERCOM_I2CS_INTFLAG_PREC_Pos          (0)                                            /**< (SERCOM_I2CS_INTFLAG) Stop Received Interrupt Position */
#define SERCOM_I2CS_INTFLAG_PREC_Msk          (0x1U << SERCOM_I2CS_INTFLAG_PREC_Pos)         /**< (SERCOM_I2CS_INTFLAG) Stop Received Interrupt Mask */
#define SERCOM_I2CS_INTFLAG_AMATCH_Pos        (1)                                            /**< (SERCOM_I2CS_INTFLAG) Address Match Interrupt Position */
#define SERCOM_I2CS_INTFLAG_AMATCH_Msk        (0x1U << SERCOM_I2CS_INTFLAG_AMATCH_Pos)       /**< (SERCOM_I2CS_INTFLAG) Address Match Interrupt Mask */
#define SERCOM_I2CS_INTFLAG_DRDY_Pos          (2)                                            /**< (SERCOM_I2CS_INTFLAG) Data Interrupt Position */
#define SERCOM_I2CS_INTFLAG_DRDY_Msk          (0x1U << SERCOM_I2CS_INTFLAG_DRDY_Pos)         /**< (SERCOM_I2CS_INTFLAG) Data Interrupt Mask */
#define SERCOM_I2CS_INTFLAG_ERROR_Pos         (7)                                            /**< (SERCOM_I2CS_INTFLAG) Combined Error Interrupt Position */
#define SERCOM_I2CS_INTFLAG_ERROR_Msk         (0x1U << SERCOM_I2CS_INTFLAG_ERROR_Pos)        /**< (SERCOM_I2CS_INTFLAG) Combined Error Interrupt Mask */
#define SERCOM_I2CS_INTFLAG_Msk               (0x00000087UL)                                 /**< (SERCOM_I2CS_INTFLAG) Register Mask  */

#define SERCOM_I2CS_STATUS_RESETVALUE       (0x00U)                                       /**<  (SERCOM_I2CS_STATUS) I2CS Status  Reset Value */

#define SERCOM_I2CS_STATUS_BUSERR_Pos         (0)                                            /**< (SERCOM_I2CS_STATUS) Bus Error Position */
#define SERCOM_I2CS_STATUS_BUSERR_Msk         (0x1U << SERCOM_I2CS_STATUS_BUSERR_Pos)        /**< (SERCOM_I2CS_STATUS) Bus Error Mask */
#define SERCOM_I2CS_STATUS_COLL_Pos           (1)                                            /**< (SERCOM_I2CS_STATUS) Transmit Collision Position */
#define SERCOM_I2CS_STATUS_COLL_Msk           (0x1U << SERCOM_I2CS_STATUS_COLL_Pos)          /**< (SERCOM_I2CS_STATUS) Transmit Collision Mask */
#define SERCOM_I2CS_STATUS_RXNACK_Pos         (2)                                            /**< (SERCOM_I2CS_STATUS) Received Not Acknowledge Position */
#define SERCOM_I2CS_STATUS_RXNACK_Msk         (0x1U << SERCOM_I2CS_STATUS_RXNACK_Pos)        /**< (SERCOM_I2CS_STATUS) Received Not Acknowledge Mask */
#define SERCOM_I2CS_STATUS_DIR_Pos            (3)                                            /**< (SERCOM_I2CS_STATUS) Read/Write Direction Position */
#define SERCOM_I2CS_STATUS_DIR_Msk            (0x1U << SERCOM_I2CS_STATUS_DIR_Pos)           /**< (SERCOM_I2CS_STATUS) Read/Write Direction Mask */
#define SERCOM_I2CS_STATUS_SR_Pos             (4)                                            /**< (SERCOM_I2CS_STATUS) Repeated Start Position */
#define SERCOM_I2CS_STATUS_SR_Msk             (0x1U << SERCOM_I2CS_STATUS_SR_Pos)            /**< (SERCOM_I2CS_STATUS) Repeated Start Mask */
#define SERCOM_I2CS_STATUS_LOWTOUT_Pos        (6)                                            /**< (SERCOM_I2CS_STATUS) SCL Low Timeout Position */
#define SERCOM_I2CS_STATUS_LOWTOUT_Msk        (0x1U << SERCOM_I2CS_STATUS_LOWTOUT_Pos)       /**< (SERCOM_I2CS_STATUS) SCL Low Timeout Mask */
#define SERCOM_I2CS_STATUS_CLKHOLD_Pos        (7)                                            /**< (SERCOM_I2CS_STATUS) Clock Hold Position */
#define SERCOM_I2CS_STATUS_CLKHOLD_Msk        (0x1U << SERCOM_I2CS_STATUS_CLKHOLD_Pos)       /**< (SERCOM_I2CS_STATUS) Clock Hold Mask */
#define SERCOM_I2CS_STATUS_SEXTTOUT_Pos       (9)                                            /**< (SERCOM_I2CS_STATUS) Slave SCL Low Extend Timeout Position */
#define SERCOM_I2CS_STATUS_SEXTTOUT_Msk       (0x1U << SERCOM_I2CS_STATUS_SEXTTOUT_Pos)      /**< (SERCOM_I2CS_STATUS) Slave SCL Low Extend Timeout Mask */
#define SERCOM_I2CS_STATUS_HS_Pos             (10)                                           /**< (SERCOM_I2CS_STATUS) High Speed Position */
#define SERCOM_I2CS_STATUS_HS_Msk             (0x1U << SERCOM_I2CS_STATUS_HS_Pos)            /**< (SERCOM_I2CS_STATUS) High Speed Mask */
#define SERCOM_I2CS_STATUS_Msk                (0x000006DFUL)                                 /**< (SERCOM_I2CS_STATUS) Register Mask  */


#define SERCOM_I2CS_SYNCBUSY_RESETVALUE     (0x00U)                                       /**<  (SERCOM_I2CS_SYNCBUSY) I2CS Synchronization Busy  Reset Value */

#define SERCOM_I2CS_SYNCBUSY_SWRST_Pos        (0)                                            /**< (SERCOM_I2CS_SYNCBUSY) Software Reset Synchronization Busy Position */
#define SERCOM_I2CS_SYNCBUSY_SWRST_Msk        (0x1U << SERCOM_I2CS_SYNCBUSY_SWRST_Pos)       /**< (SERCOM_I2CS_SYNCBUSY) Software Reset Synchronization Busy Mask */
#define SERCOM_I2CS_SYNCBUSY_ENABLE_Pos       (1)                                            /**< (SERCOM_I2CS_SYNCBUSY) SERCOM Enable Synchronization Busy Position */
#define SERCOM_I2CS_SYNCBUSY_ENABLE_Msk       (0x1U << SERCOM_I2CS_SYNCBUSY_ENABLE_Pos)      /**< (SERCOM_I2CS_SYNCBUSY) SERCOM Enable Synchronization Busy Mask */
#define SERCOM_I2CS_SYNCBUSY_Msk              (0x00000003UL)                                 /**< (SERCOM_I2CS_SYNCBUSY) Register Mask  */


#define SERCOM_I2CS_ADDR_RESETVALUE         (0x00U)                                       /**<  (SERCOM_I2CS_ADDR) I2CS Address  Reset Value */

#define SERCOM_I2CS_ADDR_GENCEN_Pos           (0)                                            /**< (SERCOM_I2CS_ADDR) General Call Address Enable Position */
#define SERCOM_I2CS_ADDR_GENCEN_Msk           (0x1U << SERCOM_I2CS_ADDR_GENCEN_Pos)          /**< (SERCOM_I2CS_ADDR) General Call Address Enable Mask */
#define SERCOM_I2CS_ADDR_ADDR_Pos             (1)                                            /**< (SERCOM_I2CS_ADDR) Address Value Position */
#define SERCOM_I2CS_ADDR_ADDR_Msk             (0x3FFU << SERCOM_I2CS_ADDR_ADDR_Pos)          /**< (SERCOM_I2CS_ADDR) Address Value Mask */
#define SERCOM_I2CS_ADDR_ADDR(value)          (SERCOM_I2CS_ADDR_ADDR_Msk & ((value) << SERCOM_I2CS_ADDR_ADDR_Pos))
#define SERCOM_I2CS_ADDR_TENBITEN_Pos         (15)                                           /**< (SERCOM_I2CS_ADDR) Ten Bit Addressing Enable Position */
#define SERCOM_I2CS_ADDR_TENBITEN_Msk         (0x1U << SERCOM_I2CS_ADDR_TENBITEN_Pos)        /**< (SERCOM_I2CS_ADDR) Ten Bit Addressing Enable Mask */
#define SERCOM_I2CS_ADDR_ADDRMASK_Pos         (17)                                           /**< (SERCOM_I2CS_ADDR) Address Mask Position */
#define SERCOM_I2CS_ADDR_ADDRMASK_Msk         (0x3FFU << SERCOM_I2CS_ADDR_ADDRMASK_Pos)      /**< (SERCOM_I2CS_ADDR) Address Mask Mask */
#define SERCOM_I2CS_ADDR_ADDRMASK(value)      (SERCOM_I2CS_ADDR_ADDRMASK_Msk & ((value) << SERCOM_I2CS_ADDR_ADDRMASK_Pos))
#define SERCOM_I2CS_ADDR_Msk                  (0x07FE87FFUL)                                 /**< (SERCOM_I2CS_ADDR) Register Mask  */


#define SERCOM_I2CS_DATA_RESETVALUE         (0x00U)                                       /**<  (SERCOM_I2CS_DATA) I2CS Data  Reset Value */

#define SERCOM_I2CS_DATA_DATA_Pos             (0)                                            /**< (SERCOM_I2CS_DATA) Data Value Position */
#define SERCOM_I2CS_DATA_DATA_Msk             (0xFFU << SERCOM_I2CS_DATA_DATA_Pos)           /**< (SERCOM_I2CS_DATA) Data Value Mask */
#define SERCOM_I2CS_DATA_DATA(value)          (SERCOM_I2CS_DATA_DATA_Msk & ((value) << SERCOM_I2CS_DATA_DATA_Pos))
#define SERCOM_I2CS_DATA_Msk                  (0x000000FFUL)                                 /**< (SERCOM_I2CS_DATA) Register Mask  */

/* -------- SERCOM_SPI_CTRLA : (SERCOM Offset: 0x00) (R/W 32) SPI Control A -------- */


#define SERCOM_SPI_CTRLA_RESETVALUE         (0x00U)                                       /**<  (SERCOM_SPI_CTRLA) SPI Control A  Reset Value */

#define SERCOM_SPI_CTRLA_SWRST_Pos            (0)                                            /**< (SERCOM_SPI_CTRLA) Software Reset Position */
#define SERCOM_SPI_CTRLA_SWRST_Msk            (0x1U << SERCOM_SPI_CTRLA_SWRST_Pos)           /**< (SERCOM_SPI_CTRLA) Software Reset Mask */
#define SERCOM_SPI_CTRLA_ENABLE_Pos           (1)                                            /**< (SERCOM_SPI_CTRLA) Enable Position */
#define SERCOM_SPI_CTRLA_ENABLE_Msk           (0x1U << SERCOM_SPI_CTRLA_ENABLE_Pos)          /**< (SERCOM_SPI_CTRLA) Enable Mask */
#define SERCOM_SPI_CTRLA_MODE_Pos             (2)                                            /**< (SERCOM_SPI_CTRLA) Operating Mode Position */
#define SERCOM_SPI_CTRLA_MODE_Msk             (0x7U << SERCOM_SPI_CTRLA_MODE_Pos)            /**< (SERCOM_SPI_CTRLA) Operating Mode Mask */
#define SERCOM_SPI_CTRLA_MODE(value)          (SERCOM_SPI_CTRLA_MODE_Msk & ((value) << SERCOM_SPI_CTRLA_MODE_Pos))
#define SERCOM_SPI_CTRLA_RUNSTDBY_Pos         (7)                                            /**< (SERCOM_SPI_CTRLA) Run during Standby Position */
#define SERCOM_SPI_CTRLA_RUNSTDBY_Msk         (0x1U << SERCOM_SPI_CTRLA_RUNSTDBY_Pos)        /**< (SERCOM_SPI_CTRLA) Run during Standby Mask */
#define SERCOM_SPI_CTRLA_IBON_Pos             (8)                                            /**< (SERCOM_SPI_CTRLA) Immediate Buffer Overflow Notification Position */
#define SERCOM_SPI_CTRLA_IBON_Msk             (0x1U << SERCOM_SPI_CTRLA_IBON_Pos)            /**< (SERCOM_SPI_CTRLA) Immediate Buffer Overflow Notification Mask */
#define SERCOM_SPI_CTRLA_DOPO_Pos             (16)                                           /**< (SERCOM_SPI_CTRLA) Data Out Pinout Position */
#define SERCOM_SPI_CTRLA_DOPO_Msk             (0x3U << SERCOM_SPI_CTRLA_DOPO_Pos)            /**< (SERCOM_SPI_CTRLA) Data Out Pinout Mask */
#define SERCOM_SPI_CTRLA_DOPO(value)          (SERCOM_SPI_CTRLA_DOPO_Msk & ((value) << SERCOM_SPI_CTRLA_DOPO_Pos))
#define SERCOM_SPI_CTRLA_DIPO_Pos             (20)                                           /**< (SERCOM_SPI_CTRLA) Data In Pinout Position */
#define SERCOM_SPI_CTRLA_DIPO_Msk             (0x3U << SERCOM_SPI_CTRLA_DIPO_Pos)            /**< (SERCOM_SPI_CTRLA) Data In Pinout Mask */
#define SERCOM_SPI_CTRLA_DIPO(value)          (SERCOM_SPI_CTRLA_DIPO_Msk & ((value) << SERCOM_SPI_CTRLA_DIPO_Pos))
#define SERCOM_SPI_CTRLA_FORM_Pos             (24)                                           /**< (SERCOM_SPI_CTRLA) Frame Format Position */
#define SERCOM_SPI_CTRLA_FORM_Msk             (0xFU << SERCOM_SPI_CTRLA_FORM_Pos)            /**< (SERCOM_SPI_CTRLA) Frame Format Mask */
#define SERCOM_SPI_CTRLA_FORM(value)          (SERCOM_SPI_CTRLA_FORM_Msk & ((value) << SERCOM_SPI_CTRLA_FORM_Pos))
#define SERCOM_SPI_CTRLA_CPHA_Pos             (28)                                           /**< (SERCOM_SPI_CTRLA) Clock Phase Position */
#define SERCOM_SPI_CTRLA_CPHA_Msk             (0x1U << SERCOM_SPI_CTRLA_CPHA_Pos)            /**< (SERCOM_SPI_CTRLA) Clock Phase Mask */
#define SERCOM_SPI_CTRLA_CPOL_Pos             (29)                                           /**< (SERCOM_SPI_CTRLA) Clock Polarity Position */
#define SERCOM_SPI_CTRLA_CPOL_Msk             (0x1U << SERCOM_SPI_CTRLA_CPOL_Pos)            /**< (SERCOM_SPI_CTRLA) Clock Polarity Mask */
#define SERCOM_SPI_CTRLA_DORD_Pos             (30)                                           /**< (SERCOM_SPI_CTRLA) Data Order Position */
#define SERCOM_SPI_CTRLA_DORD_Msk             (0x1U << SERCOM_SPI_CTRLA_DORD_Pos)            /**< (SERCOM_SPI_CTRLA) Data Order Mask */
#define SERCOM_SPI_CTRLA_Msk                  (0x7F33019FUL)                                 /**< (SERCOM_SPI_CTRLA) Register Mask  */


#define SERCOM_SPI_CTRLB_RESETVALUE         (0x00U)                                       /**<  (SERCOM_SPI_CTRLB) SPI Control B  Reset Value */

#define SERCOM_SPI_CTRLB_CHSIZE_Pos           (0)                                            /**< (SERCOM_SPI_CTRLB) Character Size Position */
#define SERCOM_SPI_CTRLB_CHSIZE_Msk           (0x7U << SERCOM_SPI_CTRLB_CHSIZE_Pos)          /**< (SERCOM_SPI_CTRLB) Character Size Mask */
#define SERCOM_SPI_CTRLB_CHSIZE(value)        (SERCOM_SPI_CTRLB_CHSIZE_Msk & ((value) << SERCOM_SPI_CTRLB_CHSIZE_Pos))
#define SERCOM_SPI_CTRLB_PLOADEN_Pos          (6)                                            /**< (SERCOM_SPI_CTRLB) Data Preload Enable Position */
#define SERCOM_SPI_CTRLB_PLOADEN_Msk          (0x1U << SERCOM_SPI_CTRLB_PLOADEN_Pos)         /**< (SERCOM_SPI_CTRLB) Data Preload Enable Mask */
#define SERCOM_SPI_CTRLB_SSDE_Pos             (9)                                            /**< (SERCOM_SPI_CTRLB) Slave Select Low Detect Enable Position */
#define SERCOM_SPI_CTRLB_SSDE_Msk             (0x1U << SERCOM_SPI_CTRLB_SSDE_Pos)            /**< (SERCOM_SPI_CTRLB) Slave Select Low Detect Enable Mask */
#define SERCOM_SPI_CTRLB_MSSEN_Pos            (13)                                           /**< (SERCOM_SPI_CTRLB) Master Slave Select Enable Position */
#define SERCOM_SPI_CTRLB_MSSEN_Msk            (0x1U << SERCOM_SPI_CTRLB_MSSEN_Pos)           /**< (SERCOM_SPI_CTRLB) Master Slave Select Enable Mask */
#define SERCOM_SPI_CTRLB_AMODE_Pos            (14)                                           /**< (SERCOM_SPI_CTRLB) Address Mode Position */
#define SERCOM_SPI_CTRLB_AMODE_Msk            (0x3U << SERCOM_SPI_CTRLB_AMODE_Pos)           /**< (SERCOM_SPI_CTRLB) Address Mode Mask */
#define SERCOM_SPI_CTRLB_AMODE(value)         (SERCOM_SPI_CTRLB_AMODE_Msk & ((value) << SERCOM_SPI_CTRLB_AMODE_Pos))
#define SERCOM_SPI_CTRLB_RXEN_Pos             (17)                                           /**< (SERCOM_SPI_CTRLB) Receiver Enable Position */
#define SERCOM_SPI_CTRLB_RXEN_Msk             (0x1U << SERCOM_SPI_CTRLB_RXEN_Pos)            /**< (SERCOM_SPI_CTRLB) Receiver Enable Mask */
#define SERCOM_SPI_CTRLB_Msk                  (0x0002E247UL)                                 /**< (SERCOM_SPI_CTRLB) Register Mask  */


#define SERCOM_SPI_BAUD_RESETVALUE          (0x00U)                                       /**<  (SERCOM_SPI_BAUD) SPI Baud Rate  Reset Value */

#define SERCOM_SPI_BAUD_BAUD_Pos              (0)                                            /**< (SERCOM_SPI_BAUD) Baud Rate Value Position */
#define SERCOM_SPI_BAUD_BAUD_Msk              (0xFFU << SERCOM_SPI_BAUD_BAUD_Pos)            /**< (SERCOM_SPI_BAUD) Baud Rate Value Mask */
#define SERCOM_SPI_BAUD_BAUD(value)           (SERCOM_SPI_BAUD_BAUD_Msk & ((value) << SERCOM_SPI_BAUD_BAUD_Pos))
#define SERCOM_SPI_BAUD_Msk                   (0x000000FFUL)                                 /**< (SERCOM_SPI_BAUD) Register Mask  */


#define SERCOM_SPI_INTENCLR_RESETVALUE      (0x00U)                                       /**<  (SERCOM_SPI_INTENCLR) SPI Interrupt Enable Clear  Reset Value */

#define SERCOM_SPI_INTENCLR_DRE_Pos           (0)                                            /**< (SERCOM_SPI_INTENCLR) Data Register Empty Interrupt Disable Position */
#define SERCOM_SPI_INTENCLR_DRE_Msk           (0x1U << SERCOM_SPI_INTENCLR_DRE_Pos)          /**< (SERCOM_SPI_INTENCLR) Data Register Empty Interrupt Disable Mask */
#define SERCOM_SPI_INTENCLR_TXC_Pos           (1)                                            /**< (SERCOM_SPI_INTENCLR) Transmit Complete Interrupt Disable Position */
#define SERCOM_SPI_INTENCLR_TXC_Msk           (0x1U << SERCOM_SPI_INTENCLR_TXC_Pos)          /**< (SERCOM_SPI_INTENCLR) Transmit Complete Interrupt Disable Mask */
#define SERCOM_SPI_INTENCLR_RXC_Pos           (2)                                            /**< (SERCOM_SPI_INTENCLR) Receive Complete Interrupt Disable Position */
#define SERCOM_SPI_INTENCLR_RXC_Msk           (0x1U << SERCOM_SPI_INTENCLR_RXC_Pos)          /**< (SERCOM_SPI_INTENCLR) Receive Complete Interrupt Disable Mask */
#define SERCOM_SPI_INTENCLR_SSL_Pos           (3)                                            /**< (SERCOM_SPI_INTENCLR) Slave Select Low Interrupt Disable Position */
#define SERCOM_SPI_INTENCLR_SSL_Msk           (0x1U << SERCOM_SPI_INTENCLR_SSL_Pos)          /**< (SERCOM_SPI_INTENCLR) Slave Select Low Interrupt Disable Mask */
#define SERCOM_SPI_INTENCLR_ERROR_Pos         (7)                                            /**< (SERCOM_SPI_INTENCLR) Combined Error Interrupt Disable Position */
#define SERCOM_SPI_INTENCLR_ERROR_Msk         (0x1U << SERCOM_SPI_INTENCLR_ERROR_Pos)        /**< (SERCOM_SPI_INTENCLR) Combined Error Interrupt Disable Mask */
#define SERCOM_SPI_INTENCLR_Msk               (0x0000008FUL)                                 /**< (SERCOM_SPI_INTENCLR) Register Mask  */


#define SERCOM_SPI_INTENSET_RESETVALUE      (0x00U)                                       /**<  (SERCOM_SPI_INTENSET) SPI Interrupt Enable Set  Reset Value */

#define SERCOM_SPI_INTENSET_DRE_Pos           (0)                                            /**< (SERCOM_SPI_INTENSET) Data Register Empty Interrupt Enable Position */
#define SERCOM_SPI_INTENSET_DRE_Msk           (0x1U << SERCOM_SPI_INTENSET_DRE_Pos)          /**< (SERCOM_SPI_INTENSET) Data Register Empty Interrupt Enable Mask */
#define SERCOM_SPI_INTENSET_TXC_Pos           (1)                                            /**< (SERCOM_SPI_INTENSET) Transmit Complete Interrupt Enable Position */
#define SERCOM_SPI_INTENSET_TXC_Msk           (0x1U << SERCOM_SPI_INTENSET_TXC_Pos)          /**< (SERCOM_SPI_INTENSET) Transmit Complete Interrupt Enable Mask */
#define SERCOM_SPI_INTENSET_RXC_Pos           (2)                                            /**< (SERCOM_SPI_INTENSET) Receive Complete Interrupt Enable Position */
#define SERCOM_SPI_INTENSET_RXC_Msk           (0x1U << SERCOM_SPI_INTENSET_RXC_Pos)          /**< (SERCOM_SPI_INTENSET) Receive Complete Interrupt Enable Mask */
#define SERCOM_SPI_INTENSET_SSL_Pos           (3)                                            /**< (SERCOM_SPI_INTENSET) Slave Select Low Interrupt Enable Position */
#define SERCOM_SPI_INTENSET_SSL_Msk           (0x1U << SERCOM_SPI_INTENSET_SSL_Pos)          /**< (SERCOM_SPI_INTENSET) Slave Select Low Interrupt Enable Mask */
#define SERCOM_SPI_INTENSET_ERROR_Pos         (7)                                            /**< (SERCOM_SPI_INTENSET) Combined Error Interrupt Enable Position */
#define SERCOM_SPI_INTENSET_ERROR_Msk         (0x1U << SERCOM_SPI_INTENSET_ERROR_Pos)        /**< (SERCOM_SPI_INTENSET) Combined Error Interrupt Enable Mask */
#define SERCOM_SPI_INTENSET_Msk               (0x0000008FUL)                                 /**< (SERCOM_SPI_INTENSET) Register Mask  */


#define SERCOM_SPI_INTFLAG_RESETVALUE       (0x00U)                                       /**<  (SERCOM_SPI_INTFLAG) SPI Interrupt Flag Status and Clear  Reset Value */

#define SERCOM_SPI_INTFLAG_DRE_Pos            (0)                                            /**< (SERCOM_SPI_INTFLAG) Data Register Empty Interrupt Position */
#define SERCOM_SPI_INTFLAG_DRE_Msk            (0x1U << SERCOM_SPI_INTFLAG_DRE_Pos)           /**< (SERCOM_SPI_INTFLAG) Data Register Empty Interrupt Mask */
#define SERCOM_SPI_INTFLAG_TXC_Pos            (1)                                            /**< (SERCOM_SPI_INTFLAG) Transmit Complete Interrupt Position */
#define SERCOM_SPI_INTFLAG_TXC_Msk            (0x1U << SERCOM_SPI_INTFLAG_TXC_Pos)           /**< (SERCOM_SPI_INTFLAG) Transmit Complete Interrupt Mask */
#define SERCOM_SPI_INTFLAG_RXC_Pos            (2)                                            /**< (SERCOM_SPI_INTFLAG) Receive Complete Interrupt Position */
#define SERCOM_SPI_INTFLAG_RXC_Msk            (0x1U << SERCOM_SPI_INTFLAG_RXC_Pos)           /**< (SERCOM_SPI_INTFLAG) Receive Complete Interrupt Mask */
#define SERCOM_SPI_INTFLAG_SSL_Pos            (3)                                            /**< (SERCOM_SPI_INTFLAG) Slave Select Low Interrupt Flag Position */
#define SERCOM_SPI_INTFLAG_SSL_Msk            (0x1U << SERCOM_SPI_INTFLAG_SSL_Pos)           /**< (SERCOM_SPI_INTFLAG) Slave Select Low Interrupt Flag Mask */
#define SERCOM_SPI_INTFLAG_ERROR_Pos          (7)                                            /**< (SERCOM_SPI_INTFLAG) Combined Error Interrupt Position */
#define SERCOM_SPI_INTFLAG_ERROR_Msk          (0x1U << SERCOM_SPI_INTFLAG_ERROR_Pos)         /**< (SERCOM_SPI_INTFLAG) Combined Error Interrupt Mask */
#define SERCOM_SPI_INTFLAG_Msk                (0x0000008FUL)                                 /**< (SERCOM_SPI_INTFLAG) Register Mask  */


#define SERCOM_SPI_STATUS_RESETVALUE        (0x00U)                                       /**<  (SERCOM_SPI_STATUS) SPI Status  Reset Value */

#define SERCOM_SPI_STATUS_BUFOVF_Pos          (2)                                            /**< (SERCOM_SPI_STATUS) Buffer Overflow Position */
#define SERCOM_SPI_STATUS_BUFOVF_Msk          (0x1U << SERCOM_SPI_STATUS_BUFOVF_Pos)         /**< (SERCOM_SPI_STATUS) Buffer Overflow Mask */
#define SERCOM_SPI_STATUS_Msk                 (0x00000004UL)                                 /**< (SERCOM_SPI_STATUS) Register Mask  */


#define SERCOM_SPI_SYNCBUSY_RESETVALUE      (0x00U)                                       /**<  (SERCOM_SPI_SYNCBUSY) SPI Synchronization Busy  Reset Value */

#define SERCOM_SPI_SYNCBUSY_SWRST_Pos         (0)                                            /**< (SERCOM_SPI_SYNCBUSY) Software Reset Synchronization Busy Position */
#define SERCOM_SPI_SYNCBUSY_SWRST_Msk         (0x1U << SERCOM_SPI_SYNCBUSY_SWRST_Pos)        /**< (SERCOM_SPI_SYNCBUSY) Software Reset Synchronization Busy Mask */
#define SERCOM_SPI_SYNCBUSY_ENABLE_Pos        (1)                                            /**< (SERCOM_SPI_SYNCBUSY) SERCOM Enable Synchronization Busy Position */
#define SERCOM_SPI_SYNCBUSY_ENABLE_Msk        (0x1U << SERCOM_SPI_SYNCBUSY_ENABLE_Pos)       /**< (SERCOM_SPI_SYNCBUSY) SERCOM Enable Synchronization Busy Mask */
#define SERCOM_SPI_SYNCBUSY_CTRLB_Pos         (2)                                            /**< (SERCOM_SPI_SYNCBUSY) CTRLB Synchronization Busy Position */
#define SERCOM_SPI_SYNCBUSY_CTRLB_Msk         (0x1U << SERCOM_SPI_SYNCBUSY_CTRLB_Pos)        /**< (SERCOM_SPI_SYNCBUSY) CTRLB Synchronization Busy Mask */
#define SERCOM_SPI_SYNCBUSY_Msk               (0x00000007UL)                                 /**< (SERCOM_SPI_SYNCBUSY) Register Mask  */


#define SERCOM_SPI_ADDR_RESETVALUE          (0x00U)                                       /**<  (SERCOM_SPI_ADDR) SPI Address  Reset Value */

#define SERCOM_SPI_ADDR_ADDR_Pos              (0)                                            /**< (SERCOM_SPI_ADDR) Address Value Position */
#define SERCOM_SPI_ADDR_ADDR_Msk              (0xFFU << SERCOM_SPI_ADDR_ADDR_Pos)            /**< (SERCOM_SPI_ADDR) Address Value Mask */
#define SERCOM_SPI_ADDR_ADDR(value)           (SERCOM_SPI_ADDR_ADDR_Msk & ((value) << SERCOM_SPI_ADDR_ADDR_Pos))
#define SERCOM_SPI_ADDR_ADDRMASK_Pos          (16)                                           /**< (SERCOM_SPI_ADDR) Address Mask Position */
#define SERCOM_SPI_ADDR_ADDRMASK_Msk          (0xFFU << SERCOM_SPI_ADDR_ADDRMASK_Pos)        /**< (SERCOM_SPI_ADDR) Address Mask Mask */
#define SERCOM_SPI_ADDR_ADDRMASK(value)       (SERCOM_SPI_ADDR_ADDRMASK_Msk & ((value) << SERCOM_SPI_ADDR_ADDRMASK_Pos))
#define SERCOM_SPI_ADDR_Msk                   (0x00FF00FFUL)                                 /**< (SERCOM_SPI_ADDR) Register Mask  */


#define SERCOM_SPI_DATA_RESETVALUE          (0x00U)                                       /**<  (SERCOM_SPI_DATA) SPI Data  Reset Value */

#define SERCOM_SPI_DATA_DATA_Pos              (0)                                            /**< (SERCOM_SPI_DATA) Data Value Position */
#define SERCOM_SPI_DATA_DATA_Msk              (0x1FFU << SERCOM_SPI_DATA_DATA_Pos)           /**< (SERCOM_SPI_DATA) Data Value Mask */
#define SERCOM_SPI_DATA_DATA(value)           (SERCOM_SPI_DATA_DATA_Msk & ((value) << SERCOM_SPI_DATA_DATA_Pos))
#define SERCOM_SPI_DATA_Msk                   (0x000001FFUL)                                 /**< (SERCOM_SPI_DATA) Register Mask  */


#define SERCOM_SPI_DBGCTRL_RESETVALUE       (0x00U)                                       /**<  (SERCOM_SPI_DBGCTRL) SPI Debug Control  Reset Value */

#define SERCOM_SPI_DBGCTRL_DBGSTOP_Pos        (0)                                            /**< (SERCOM_SPI_DBGCTRL) Debug Mode Position */
#define SERCOM_SPI_DBGCTRL_DBGSTOP_Msk        (0x1U << SERCOM_SPI_DBGCTRL_DBGSTOP_Pos)       /**< (SERCOM_SPI_DBGCTRL) Debug Mode Mask */
#define SERCOM_SPI_DBGCTRL_Msk                (0x00000001UL)                                 /**< (SERCOM_SPI_DBGCTRL) Register Mask  */


#define SERCOM_USART_CTRLA_RESETVALUE       (0x00U)                                       /**<  (SERCOM_USART_CTRLA) USART Control A  Reset Value */

#define SERCOM_USART_CTRLA_SWRST_Pos          (0)                                            /**< (SERCOM_USART_CTRLA) Software Reset Position */
#define SERCOM_USART_CTRLA_SWRST_Msk          (0x1U << SERCOM_USART_CTRLA_SWRST_Pos)         /**< (SERCOM_USART_CTRLA) Software Reset Mask */
#define SERCOM_USART_CTRLA_ENABLE_Pos         (1)                                            /**< (SERCOM_USART_CTRLA) Enable Position */
#define SERCOM_USART_CTRLA_ENABLE_Msk         (0x1U << SERCOM_USART_CTRLA_ENABLE_Pos)        /**< (SERCOM_USART_CTRLA) Enable Mask */
#define SERCOM_USART_CTRLA_MODE_Pos           (2)                                            /**< (SERCOM_USART_CTRLA) Operating Mode Position */
#define SERCOM_USART_CTRLA_MODE_Msk           (0x7U << SERCOM_USART_CTRLA_MODE_Pos)          /**< (SERCOM_USART_CTRLA) Operating Mode Mask */
#define SERCOM_USART_CTRLA_MODE(value)        (SERCOM_USART_CTRLA_MODE_Msk & ((value) << SERCOM_USART_CTRLA_MODE_Pos))
#define SERCOM_USART_CTRLA_RUNSTDBY_Pos       (7)                                            /**< (SERCOM_USART_CTRLA) Run during Standby Position */
#define SERCOM_USART_CTRLA_RUNSTDBY_Msk       (0x1U << SERCOM_USART_CTRLA_RUNSTDBY_Pos)      /**< (SERCOM_USART_CTRLA) Run during Standby Mask */
#define SERCOM_USART_CTRLA_IBON_Pos           (8)                                            /**< (SERCOM_USART_CTRLA) Immediate Buffer Overflow Notification Position */
#define SERCOM_USART_CTRLA_IBON_Msk           (0x1U << SERCOM_USART_CTRLA_IBON_Pos)          /**< (SERCOM_USART_CTRLA) Immediate Buffer Overflow Notification Mask */
#define SERCOM_USART_CTRLA_SAMPR_Pos          (13)                                           /**< (SERCOM_USART_CTRLA) Sample Position */
#define SERCOM_USART_CTRLA_SAMPR_Msk          (0x7U << SERCOM_USART_CTRLA_SAMPR_Pos)         /**< (SERCOM_USART_CTRLA) Sample Mask */
#define SERCOM_USART_CTRLA_SAMPR(value)       (SERCOM_USART_CTRLA_SAMPR_Msk & ((value) << SERCOM_USART_CTRLA_SAMPR_Pos))
#define SERCOM_USART_CTRLA_TXPO_Pos           (16)                                           /**< (SERCOM_USART_CTRLA) Transmit Data Pinout Position */
#define SERCOM_USART_CTRLA_TXPO_Msk           (0x3U << SERCOM_USART_CTRLA_TXPO_Pos)          /**< (SERCOM_USART_CTRLA) Transmit Data Pinout Mask */
#define SERCOM_USART_CTRLA_TXPO(value)        (SERCOM_USART_CTRLA_TXPO_Msk & ((value) << SERCOM_USART_CTRLA_TXPO_Pos))
#define SERCOM_USART_CTRLA_RXPO_Pos           (20)                                           /**< (SERCOM_USART_CTRLA) Receive Data Pinout Position */
#define SERCOM_USART_CTRLA_RXPO_Msk           (0x3U << SERCOM_USART_CTRLA_RXPO_Pos)          /**< (SERCOM_USART_CTRLA) Receive Data Pinout Mask */
#define SERCOM_USART_CTRLA_RXPO(value)        (SERCOM_USART_CTRLA_RXPO_Msk & ((value) << SERCOM_USART_CTRLA_RXPO_Pos))
#define SERCOM_USART_CTRLA_SAMPA_Pos          (22)                                           /**< (SERCOM_USART_CTRLA) Sample Adjustment Position */
#define SERCOM_USART_CTRLA_SAMPA_Msk          (0x3U << SERCOM_USART_CTRLA_SAMPA_Pos)         /**< (SERCOM_USART_CTRLA) Sample Adjustment Mask */
#define SERCOM_USART_CTRLA_SAMPA(value)       (SERCOM_USART_CTRLA_SAMPA_Msk & ((value) << SERCOM_USART_CTRLA_SAMPA_Pos))
#define SERCOM_USART_CTRLA_FORM_Pos           (24)                                           /**< (SERCOM_USART_CTRLA) Frame Format Position */
#define SERCOM_USART_CTRLA_FORM_Msk           (0xFU << SERCOM_USART_CTRLA_FORM_Pos)          /**< (SERCOM_USART_CTRLA) Frame Format Mask */
#define SERCOM_USART_CTRLA_FORM(value)        (SERCOM_USART_CTRLA_FORM_Msk & ((value) << SERCOM_USART_CTRLA_FORM_Pos))
#define SERCOM_USART_CTRLA_CMODE_Pos          (28)                                           /**< (SERCOM_USART_CTRLA) Communication Mode Position */
#define SERCOM_USART_CTRLA_CMODE_Msk          (0x1U << SERCOM_USART_CTRLA_CMODE_Pos)         /**< (SERCOM_USART_CTRLA) Communication Mode Mask */
#define SERCOM_USART_CTRLA_CPOL_Pos           (29)                                           /**< (SERCOM_USART_CTRLA) Clock Polarity Position */
#define SERCOM_USART_CTRLA_CPOL_Msk           (0x1U << SERCOM_USART_CTRLA_CPOL_Pos)          /**< (SERCOM_USART_CTRLA) Clock Polarity Mask */
#define SERCOM_USART_CTRLA_DORD_Pos           (30)                                           /**< (SERCOM_USART_CTRLA) Data Order Position */
#define SERCOM_USART_CTRLA_DORD_Msk           (0x1U << SERCOM_USART_CTRLA_DORD_Pos)          /**< (SERCOM_USART_CTRLA) Data Order Mask */
#define SERCOM_USART_CTRLA_Msk                (0x7FF3E19FUL)                                 /**< (SERCOM_USART_CTRLA) Register Mask  */


#define SERCOM_USART_CTRLB_RESETVALUE       (0x00U)                                       /**<  (SERCOM_USART_CTRLB) USART Control B  Reset Value */

#define SERCOM_USART_CTRLB_CHSIZE_Pos         (0)                                            /**< (SERCOM_USART_CTRLB) Character Size Position */
#define SERCOM_USART_CTRLB_CHSIZE_Msk         (0x7U << SERCOM_USART_CTRLB_CHSIZE_Pos)        /**< (SERCOM_USART_CTRLB) Character Size Mask */
#define SERCOM_USART_CTRLB_CHSIZE(value)      (SERCOM_USART_CTRLB_CHSIZE_Msk & ((value) << SERCOM_USART_CTRLB_CHSIZE_Pos))
#define SERCOM_USART_CTRLB_SBMODE_Pos         (6)                                            /**< (SERCOM_USART_CTRLB) Stop Bit Mode Position */
#define SERCOM_USART_CTRLB_SBMODE_Msk         (0x1U << SERCOM_USART_CTRLB_SBMODE_Pos)        /**< (SERCOM_USART_CTRLB) Stop Bit Mode Mask */
#define SERCOM_USART_CTRLB_COLDEN_Pos         (8)                                            /**< (SERCOM_USART_CTRLB) Collision Detection Enable Position */
#define SERCOM_USART_CTRLB_COLDEN_Msk         (0x1U << SERCOM_USART_CTRLB_COLDEN_Pos)        /**< (SERCOM_USART_CTRLB) Collision Detection Enable Mask */
#define SERCOM_USART_CTRLB_SFDE_Pos           (9)                                            /**< (SERCOM_USART_CTRLB) Start of Frame Detection Enable Position */
#define SERCOM_USART_CTRLB_SFDE_Msk           (0x1U << SERCOM_USART_CTRLB_SFDE_Pos)          /**< (SERCOM_USART_CTRLB) Start of Frame Detection Enable Mask */
#define SERCOM_USART_CTRLB_ENC_Pos            (10)                                           /**< (SERCOM_USART_CTRLB) Encoding Format Position */
#define SERCOM_USART_CTRLB_ENC_Msk            (0x1U << SERCOM_USART_CTRLB_ENC_Pos)           /**< (SERCOM_USART_CTRLB) Encoding Format Mask */
#define SERCOM_USART_CTRLB_PMODE_Pos          (13)                                           /**< (SERCOM_USART_CTRLB) Parity Mode Position */
#define SERCOM_USART_CTRLB_PMODE_Msk          (0x1U << SERCOM_USART_CTRLB_PMODE_Pos)         /**< (SERCOM_USART_CTRLB) Parity Mode Mask */
#define SERCOM_USART_CTRLB_TXEN_Pos           (16)                                           /**< (SERCOM_USART_CTRLB) Transmitter Enable Position */
#define SERCOM_USART_CTRLB_TXEN_Msk           (0x1U << SERCOM_USART_CTRLB_TXEN_Pos)          /**< (SERCOM_USART_CTRLB) Transmitter Enable Mask */
#define SERCOM_USART_CTRLB_RXEN_Pos           (17)                                           /**< (SERCOM_USART_CTRLB) Receiver Enable Position */
#define SERCOM_USART_CTRLB_RXEN_Msk           (0x1U << SERCOM_USART_CTRLB_RXEN_Pos)          /**< (SERCOM_USART_CTRLB) Receiver Enable Mask */
#define SERCOM_USART_CTRLB_LINCMD_Pos         (24)                                           /**< (SERCOM_USART_CTRLB) LIN Command Position */
#define SERCOM_USART_CTRLB_LINCMD_Msk         (0x3U << SERCOM_USART_CTRLB_LINCMD_Pos)        /**< (SERCOM_USART_CTRLB) LIN Command Mask */
#define SERCOM_USART_CTRLB_LINCMD(value)      (SERCOM_USART_CTRLB_LINCMD_Msk & ((value) << SERCOM_USART_CTRLB_LINCMD_Pos))
#define SERCOM_USART_CTRLB_Msk                (0x03032747UL)                                 /**< (SERCOM_USART_CTRLB) Register Mask  */

/* -------- SERCOM_USART_CTRLC : (SERCOM Offset: 0x08) (R/W 32) USART Control C -------- */
#define SERCOM_USART_CTRLC_RESETVALUE       (0x00U)                                       /**<  (SERCOM_USART_CTRLC) USART Control C  Reset Value */

#define SERCOM_USART_CTRLC_GTIME_Pos          (0)                                            /**< (SERCOM_USART_CTRLC) RS485 Guard Time Position */
#define SERCOM_USART_CTRLC_GTIME_Msk          (0x7U << SERCOM_USART_CTRLC_GTIME_Pos)         /**< (SERCOM_USART_CTRLC) RS485 Guard Time Mask */
#define SERCOM_USART_CTRLC_GTIME(value)       (SERCOM_USART_CTRLC_GTIME_Msk & ((value) << SERCOM_USART_CTRLC_GTIME_Pos))
#define SERCOM_USART_CTRLC_BRKLEN_Pos         (8)                                            /**< (SERCOM_USART_CTRLC) LIN Master Break Length Position */
#define SERCOM_USART_CTRLC_BRKLEN_Msk         (0x3U << SERCOM_USART_CTRLC_BRKLEN_Pos)        /**< (SERCOM_USART_CTRLC) LIN Master Break Length Mask */
#define SERCOM_USART_CTRLC_BRKLEN(value)      (SERCOM_USART_CTRLC_BRKLEN_Msk & ((value) << SERCOM_USART_CTRLC_BRKLEN_Pos))
#define SERCOM_USART_CTRLC_HDRDLY_Pos         (10)                                           /**< (SERCOM_USART_CTRLC) LIN Master Header Delay Position */
#define SERCOM_USART_CTRLC_HDRDLY_Msk         (0x3U << SERCOM_USART_CTRLC_HDRDLY_Pos)        /**< (SERCOM_USART_CTRLC) LIN Master Header Delay Mask */
#define SERCOM_USART_CTRLC_HDRDLY(value)      (SERCOM_USART_CTRLC_HDRDLY_Msk & ((value) << SERCOM_USART_CTRLC_HDRDLY_Pos))
#define SERCOM_USART_CTRLC_Msk                (0x00000F07UL)                                 /**< (SERCOM_USART_CTRLC) Register Mask  */

/* -------- SERCOM_USART_BAUD : (SERCOM Offset: 0x0c) (R/W 16) USART Baud Rate -------- */


#define SERCOM_USART_BAUD_RESETVALUE        (0x00U)                                       /**<  (SERCOM_USART_BAUD) USART Baud Rate  Reset Value */

#define SERCOM_USART_BAUD_BAUD_Pos            (0)                                            /**< (SERCOM_USART_BAUD) Baud Rate Value Position */
#define SERCOM_USART_BAUD_BAUD_Msk            (0xFFFFU << SERCOM_USART_BAUD_BAUD_Pos)        /**< (SERCOM_USART_BAUD) Baud Rate Value Mask */
#define SERCOM_USART_BAUD_BAUD(value)         (SERCOM_USART_BAUD_BAUD_Msk & ((value) << SERCOM_USART_BAUD_BAUD_Pos))
/* FRAC mode */
#define SERCOM_USART_BAUD_BAUD_FRAC_MODE_Pos            (0)                                            /**< (SERCOM_USART_BAUD) Baud Rate Value Position */
#define SERCOM_USART_BAUD_BAUD_FRAC_MODE_Msk            (0x1FFFU << SERCOM_USART_BAUD_BAUD_Pos)        /**< (SERCOM_USART_BAUD) Baud Rate Value Mask */
#define SERCOM_USART_BAUD_BAUD_FRAC_MODE(value)         (SERCOM_USART_BAUD_BAUD_Msk & ((value) << SERCOM_USART_BAUD_BAUD_Pos))
#define SERCOM_USART_BAUD_FP_Pos                        (13)                                           /**< (SERCOM_USART_BAUD) Fractional Part Position */
#define SERCOM_USART_BAUD_FP_Msk                        (0x7U << SERCOM_USART_BAUD_FP_Pos)             /**< (SERCOM_USART_BAUD) Fractional Part Mask */
#define SERCOM_USART_BAUD_FP(value)                     (SERCOM_USART_BAUD_FP_Msk & ((value) << SERCOM_USART_BAUD_FP_Pos))

/* -------- SERCOM_USART_RXPL : (SERCOM Offset: 0x0e) (R/W 8) USART Receive Pulse Length -------- */

#define SERCOM_USART_RXPL_RESETVALUE        (0x00U)                                       /**<  (SERCOM_USART_RXPL) USART Receive Pulse Length  Reset Value */

#define SERCOM_USART_RXPL_RXPL_Pos            (0)                                            /**< (SERCOM_USART_RXPL) Receive Pulse Length Position */
#define SERCOM_USART_RXPL_RXPL_Msk            (0xFFU << SERCOM_USART_RXPL_RXPL_Pos)          /**< (SERCOM_USART_RXPL) Receive Pulse Length Mask */
#define SERCOM_USART_RXPL_RXPL(value)         (SERCOM_USART_RXPL_RXPL_Msk & ((value) << SERCOM_USART_RXPL_RXPL_Pos))
#define SERCOM_USART_RXPL_Msk                 (0x000000FFUL)                                 /**< (SERCOM_USART_RXPL) Register Mask  */

/* -------- SERCOM_USART_INTENCLR : (SERCOM Offset: 0x14) (R/W 8) USART Interrupt Enable Clear -------- */

#define SERCOM_USART_INTENCLR_RESETVALUE    (0x00U)                                       /**<  (SERCOM_USART_INTENCLR) USART Interrupt Enable Clear  Reset Value */

#define SERCOM_USART_INTENCLR_DRE_Pos         (0)                                            /**< (SERCOM_USART_INTENCLR) Data Register Empty Interrupt Disable Position */
#define SERCOM_USART_INTENCLR_DRE_Msk         (0x1U << SERCOM_USART_INTENCLR_DRE_Pos)        /**< (SERCOM_USART_INTENCLR) Data Register Empty Interrupt Disable Mask */
#define SERCOM_USART_INTENCLR_TXC_Pos         (1)                                            /**< (SERCOM_USART_INTENCLR) Transmit Complete Interrupt Disable Position */
#define SERCOM_USART_INTENCLR_TXC_Msk         (0x1U << SERCOM_USART_INTENCLR_TXC_Pos)        /**< (SERCOM_USART_INTENCLR) Transmit Complete Interrupt Disable Mask */
#define SERCOM_USART_INTENCLR_RXC_Pos         (2)                                            /**< (SERCOM_USART_INTENCLR) Receive Complete Interrupt Disable Position */
#define SERCOM_USART_INTENCLR_RXC_Msk         (0x1U << SERCOM_USART_INTENCLR_RXC_Pos)        /**< (SERCOM_USART_INTENCLR) Receive Complete Interrupt Disable Mask */
#define SERCOM_USART_INTENCLR_RXS_Pos         (3)                                            /**< (SERCOM_USART_INTENCLR) Receive Start Interrupt Disable Position */
#define SERCOM_USART_INTENCLR_RXS_Msk         (0x1U << SERCOM_USART_INTENCLR_RXS_Pos)        /**< (SERCOM_USART_INTENCLR) Receive Start Interrupt Disable Mask */
#define SERCOM_USART_INTENCLR_CTSIC_Pos       (4)                                            /**< (SERCOM_USART_INTENCLR) Clear To Send Input Change Interrupt Disable Position */
#define SERCOM_USART_INTENCLR_CTSIC_Msk       (0x1U << SERCOM_USART_INTENCLR_CTSIC_Pos)      /**< (SERCOM_USART_INTENCLR) Clear To Send Input Change Interrupt Disable Mask */
#define SERCOM_USART_INTENCLR_RXBRK_Pos       (5)                                            /**< (SERCOM_USART_INTENCLR) Break Received Interrupt Disable Position */
#define SERCOM_USART_INTENCLR_RXBRK_Msk       (0x1U << SERCOM_USART_INTENCLR_RXBRK_Pos)      /**< (SERCOM_USART_INTENCLR) Break Received Interrupt Disable Mask */
#define SERCOM_USART_INTENCLR_ERROR_Pos       (7)                                            /**< (SERCOM_USART_INTENCLR) Combined Error Interrupt Disable Position */
#define SERCOM_USART_INTENCLR_ERROR_Msk       (0x1U << SERCOM_USART_INTENCLR_ERROR_Pos)      /**< (SERCOM_USART_INTENCLR) Combined Error Interrupt Disable Mask */
#define SERCOM_USART_INTENCLR_Msk             (0x000000BFUL)                                 /**< (SERCOM_USART_INTENCLR) Register Mask  */

/* -------- SERCOM_USART_INTENSET : (SERCOM Offset: 0x16) (R/W 8) USART Interrupt Enable Set -------- */

#define SERCOM_USART_INTENSET_RESETVALUE    (0x00U)                                       /**<  (SERCOM_USART_INTENSET) USART Interrupt Enable Set  Reset Value */

#define SERCOM_USART_INTENSET_DRE_Pos         (0)                                            /**< (SERCOM_USART_INTENSET) Data Register Empty Interrupt Enable Position */
#define SERCOM_USART_INTENSET_DRE_Msk         (0x1U << SERCOM_USART_INTENSET_DRE_Pos)        /**< (SERCOM_USART_INTENSET) Data Register Empty Interrupt Enable Mask */
#define SERCOM_USART_INTENSET_TXC_Pos         (1)                                            /**< (SERCOM_USART_INTENSET) Transmit Complete Interrupt Enable Position */
#define SERCOM_USART_INTENSET_TXC_Msk         (0x1U << SERCOM_USART_INTENSET_TXC_Pos)        /**< (SERCOM_USART_INTENSET) Transmit Complete Interrupt Enable Mask */
#define SERCOM_USART_INTENSET_RXC_Pos         (2)                                            /**< (SERCOM_USART_INTENSET) Receive Complete Interrupt Enable Position */
#define SERCOM_USART_INTENSET_RXC_Msk         (0x1U << SERCOM_USART_INTENSET_RXC_Pos)        /**< (SERCOM_USART_INTENSET) Receive Complete Interrupt Enable Mask */
#define SERCOM_USART_INTENSET_RXS_Pos         (3)                                            /**< (SERCOM_USART_INTENSET) Receive Start Interrupt Enable Position */
#define SERCOM_USART_INTENSET_RXS_Msk         (0x1U << SERCOM_USART_INTENSET_RXS_Pos)        /**< (SERCOM_USART_INTENSET) Receive Start Interrupt Enable Mask */
#define SERCOM_USART_INTENSET_CTSIC_Pos       (4)                                            /**< (SERCOM_USART_INTENSET) Clear To Send Input Change Interrupt Enable Position */
#define SERCOM_USART_INTENSET_CTSIC_Msk       (0x1U << SERCOM_USART_INTENSET_CTSIC_Pos)      /**< (SERCOM_USART_INTENSET) Clear To Send Input Change Interrupt Enable Mask */
#define SERCOM_USART_INTENSET_RXBRK_Pos       (5)                                            /**< (SERCOM_USART_INTENSET) Break Received Interrupt Enable Position */
#define SERCOM_USART_INTENSET_RXBRK_Msk       (0x1U << SERCOM_USART_INTENSET_RXBRK_Pos)      /**< (SERCOM_USART_INTENSET) Break Received Interrupt Enable Mask */
#define SERCOM_USART_INTENSET_ERROR_Pos       (7)                                            /**< (SERCOM_USART_INTENSET) Combined Error Interrupt Enable Position */
#define SERCOM_USART_INTENSET_ERROR_Msk       (0x1U << SERCOM_USART_INTENSET_ERROR_Pos)      /**< (SERCOM_USART_INTENSET) Combined Error Interrupt Enable Mask */
#define SERCOM_USART_INTENSET_Msk             (0x000000BFUL)                                 /**< (SERCOM_USART_INTENSET) Register Mask  */

/* -------- SERCOM_USART_INTFLAG : (SERCOM Offset: 0x18) (R/W 8) USART Interrupt Flag Status and Clear -------- */

#define SERCOM_USART_INTFLAG_RESETVALUE     (0x00U)                                       /**<  (SERCOM_USART_INTFLAG) USART Interrupt Flag Status and Clear  Reset Value */

#define SERCOM_USART_INTFLAG_DRE_Pos          (0)                                            /**< (SERCOM_USART_INTFLAG) Data Register Empty Interrupt Position */
#define SERCOM_USART_INTFLAG_DRE_Msk          (0x1U << SERCOM_USART_INTFLAG_DRE_Pos)         /**< (SERCOM_USART_INTFLAG) Data Register Empty Interrupt Mask */
#define SERCOM_USART_INTFLAG_TXC_Pos          (1)                                            /**< (SERCOM_USART_INTFLAG) Transmit Complete Interrupt Position */
#define SERCOM_USART_INTFLAG_TXC_Msk          (0x1U << SERCOM_USART_INTFLAG_TXC_Pos)         /**< (SERCOM_USART_INTFLAG) Transmit Complete Interrupt Mask */
#define SERCOM_USART_INTFLAG_RXC_Pos          (2)                                            /**< (SERCOM_USART_INTFLAG) Receive Complete Interrupt Position */
#define SERCOM_USART_INTFLAG_RXC_Msk          (0x1U << SERCOM_USART_INTFLAG_RXC_Pos)         /**< (SERCOM_USART_INTFLAG) Receive Complete Interrupt Mask */
#define SERCOM_USART_INTFLAG_RXS_Pos          (3)                                            /**< (SERCOM_USART_INTFLAG) Receive Start Interrupt Position */
#define SERCOM_USART_INTFLAG_RXS_Msk          (0x1U << SERCOM_USART_INTFLAG_RXS_Pos)         /**< (SERCOM_USART_INTFLAG) Receive Start Interrupt Mask */
#define SERCOM_USART_INTFLAG_CTSIC_Pos        (4)                                            /**< (SERCOM_USART_INTFLAG) Clear To Send Input Change Interrupt Position */
#define SERCOM_USART_INTFLAG_CTSIC_Msk        (0x1U << SERCOM_USART_INTFLAG_CTSIC_Pos)       /**< (SERCOM_USART_INTFLAG) Clear To Send Input Change Interrupt Mask */
#define SERCOM_USART_INTFLAG_RXBRK_Pos        (5)                                            /**< (SERCOM_USART_INTFLAG) Break Received Interrupt Position */
#define SERCOM_USART_INTFLAG_RXBRK_Msk        (0x1U << SERCOM_USART_INTFLAG_RXBRK_Pos)       /**< (SERCOM_USART_INTFLAG) Break Received Interrupt Mask */
#define SERCOM_USART_INTFLAG_ERROR_Pos        (7)                                            /**< (SERCOM_USART_INTFLAG) Combined Error Interrupt Position */
#define SERCOM_USART_INTFLAG_ERROR_Msk        (0x1U << SERCOM_USART_INTFLAG_ERROR_Pos)       /**< (SERCOM_USART_INTFLAG) Combined Error Interrupt Mask */
#define SERCOM_USART_INTFLAG_Msk              (0x000000BFUL)                                 /**< (SERCOM_USART_INTFLAG) Register Mask  */

/* -------- SERCOM_USART_STATUS : (SERCOM Offset: 0x1a) (R/W 16) USART Status -------- */

#define SERCOM_USART_STATUS_RESETVALUE      (0x00U)                                       /**<  (SERCOM_USART_STATUS) USART Status  Reset Value */

#define SERCOM_USART_STATUS_PERR_Pos          (0)                                            /**< (SERCOM_USART_STATUS) Parity Error Position */
#define SERCOM_USART_STATUS_PERR_Msk          (0x1U << SERCOM_USART_STATUS_PERR_Pos)         /**< (SERCOM_USART_STATUS) Parity Error Mask */
#define SERCOM_USART_STATUS_FERR_Pos          (1)                                            /**< (SERCOM_USART_STATUS) Frame Error Position */
#define SERCOM_USART_STATUS_FERR_Msk          (0x1U << SERCOM_USART_STATUS_FERR_Pos)         /**< (SERCOM_USART_STATUS) Frame Error Mask */
#define SERCOM_USART_STATUS_BUFOVF_Pos        (2)                                            /**< (SERCOM_USART_STATUS) Buffer Overflow Position */
#define SERCOM_USART_STATUS_BUFOVF_Msk        (0x1U << SERCOM_USART_STATUS_BUFOVF_Pos)       /**< (SERCOM_USART_STATUS) Buffer Overflow Mask */
#define SERCOM_USART_STATUS_CTS_Pos           (3)                                            /**< (SERCOM_USART_STATUS) Clear To Send Position */
#define SERCOM_USART_STATUS_CTS_Msk           (0x1U << SERCOM_USART_STATUS_CTS_Pos)          /**< (SERCOM_USART_STATUS) Clear To Send Mask */
#define SERCOM_USART_STATUS_ISF_Pos           (4)                                            /**< (SERCOM_USART_STATUS) Inconsistent Sync Field Position */
#define SERCOM_USART_STATUS_ISF_Msk           (0x1U << SERCOM_USART_STATUS_ISF_Pos)          /**< (SERCOM_USART_STATUS) Inconsistent Sync Field Mask */
#define SERCOM_USART_STATUS_COLL_Pos          (5)                                            /**< (SERCOM_USART_STATUS) Collision Detected Position */
#define SERCOM_USART_STATUS_COLL_Msk          (0x1U << SERCOM_USART_STATUS_COLL_Pos)         /**< (SERCOM_USART_STATUS) Collision Detected Mask */
#define SERCOM_USART_STATUS_TXE_Pos           (6)                                            /**< (SERCOM_USART_STATUS) Transmitter Empty Position */
#define SERCOM_USART_STATUS_TXE_Msk           (0x1U << SERCOM_USART_STATUS_TXE_Pos)          /**< (SERCOM_USART_STATUS) Transmitter Empty Mask */
#define SERCOM_USART_STATUS_Msk               (0x0000007FUL)                                 /**< (SERCOM_USART_STATUS) Register Mask  */


#define SERCOM_USART_SYNCBUSY_RESETVALUE    (0x00U)                                       /**<  (SERCOM_USART_SYNCBUSY) USART Synchronization Busy  Reset Value */

#define SERCOM_USART_SYNCBUSY_SWRST_Pos       (0)                                            /**< (SERCOM_USART_SYNCBUSY) Software Reset Synchronization Busy Position */
#define SERCOM_USART_SYNCBUSY_SWRST_Msk       (0x1U << SERCOM_USART_SYNCBUSY_SWRST_Pos)      /**< (SERCOM_USART_SYNCBUSY) Software Reset Synchronization Busy Mask */
#define SERCOM_USART_SYNCBUSY_ENABLE_Pos      (1)                                            /**< (SERCOM_USART_SYNCBUSY) SERCOM Enable Synchronization Busy Position */
#define SERCOM_USART_SYNCBUSY_ENABLE_Msk      (0x1U << SERCOM_USART_SYNCBUSY_ENABLE_Pos)     /**< (SERCOM_USART_SYNCBUSY) SERCOM Enable Synchronization Busy Mask */
#define SERCOM_USART_SYNCBUSY_CTRLB_Pos       (2)                                            /**< (SERCOM_USART_SYNCBUSY) CTRLB Synchronization Busy Position */
#define SERCOM_USART_SYNCBUSY_CTRLB_Msk       (0x1U << SERCOM_USART_SYNCBUSY_CTRLB_Pos)      /**< (SERCOM_USART_SYNCBUSY) CTRLB Synchronization Busy Mask */
#define SERCOM_USART_SYNCBUSY_Msk             (0x00000007UL)                                 /**< (SERCOM_USART_SYNCBUSY) Register Mask  */


#define SERCOM_USART_DATA_RESETVALUE        (0x00U)                                       /**<  (SERCOM_USART_DATA) USART Data  Reset Value */

#define SERCOM_USART_DATA_DATA_Pos            (0)                                            /**< (SERCOM_USART_DATA) Data Value Position */
#define SERCOM_USART_DATA_DATA_Msk            (0x1FFU << SERCOM_USART_DATA_DATA_Pos)         /**< (SERCOM_USART_DATA) Data Value Mask */
#define SERCOM_USART_DATA_DATA(value)         (SERCOM_USART_DATA_DATA_Msk & ((value) << SERCOM_USART_DATA_DATA_Pos))
#define SERCOM_USART_DATA_Msk                 (0x000001FFUL)                                 /**< (SERCOM_USART_DATA) Register Mask  */


#define SERCOM_USART_DBGCTRL_RESETVALUE     (0x00U)                                       /**<  (SERCOM_USART_DBGCTRL) USART Debug Control  Reset Value */

#define SERCOM_USART_DBGCTRL_DBGSTOP_Pos      (0)                                            /**< (SERCOM_USART_DBGCTRL) Debug Mode Position */
#define SERCOM_USART_DBGCTRL_DBGSTOP_Msk      (0x1U << SERCOM_USART_DBGCTRL_DBGSTOP_Pos)     /**< (SERCOM_USART_DBGCTRL) Debug Mode Mask */
#define SERCOM_USART_DBGCTRL_Msk              (0x00000001UL)                                 /**< (SERCOM_USART_DBGCTRL) Register Mask  */

/** \brief SERCOM_I2CM register offsets definitions */
#define SERCOM_I2CM_CTRLA_OFFSET     (0x00)         /**< (SERCOM_I2CM_CTRLA) I2CM Control A Offset */
#define SERCOM_I2CM_CTRLB_OFFSET     (0x04)         /**< (SERCOM_I2CM_CTRLB) I2CM Control B Offset */
#define SERCOM_I2CM_BAUD_OFFSET      (0x0C)         /**< (SERCOM_I2CM_BAUD) I2CM Baud Rate Offset */
#define SERCOM_I2CM_INTENCLR_OFFSET  (0x14)         /**< (SERCOM_I2CM_INTENCLR) I2CM Interrupt Enable Clear Offset */
#define SERCOM_I2CM_INTENSET_OFFSET  (0x16)         /**< (SERCOM_I2CM_INTENSET) I2CM Interrupt Enable Set Offset */
#define SERCOM_I2CM_INTFLAG_OFFSET   (0x18)         /**< (SERCOM_I2CM_INTFLAG) I2CM Interrupt Flag Status and Clear Offset */
#define SERCOM_I2CM_STATUS_OFFSET    (0x1A)         /**< (SERCOM_I2CM_STATUS) I2CM Status Offset */
#define SERCOM_I2CM_SYNCBUSY_OFFSET  (0x1C)         /**< (SERCOM_I2CM_SYNCBUSY) I2CM Synchronization Busy Offset */
#define SERCOM_I2CM_ADDR_OFFSET      (0x24)         /**< (SERCOM_I2CM_ADDR) I2CM Address Offset */
#define SERCOM_I2CM_DATA_OFFSET      (0x28)         /**< (SERCOM_I2CM_DATA) I2CM Data Offset */
#define SERCOM_I2CM_DBGCTRL_OFFSET   (0x30)         /**< (SERCOM_I2CM_DBGCTRL) I2CM Debug Control Offset */
/** \brief SERCOM_I2CS register offsets definitions */
#define SERCOM_I2CS_CTRLA_OFFSET     (0x00)         /**< (SERCOM_I2CS_CTRLA) I2CS Control A Offset */
#define SERCOM_I2CS_CTRLB_OFFSET     (0x04)         /**< (SERCOM_I2CS_CTRLB) I2CS Control B Offset */
#define SERCOM_I2CS_INTENCLR_OFFSET  (0x14)         /**< (SERCOM_I2CS_INTENCLR) I2CS Interrupt Enable Clear Offset */
#define SERCOM_I2CS_INTENSET_OFFSET  (0x16)         /**< (SERCOM_I2CS_INTENSET) I2CS Interrupt Enable Set Offset */
#define SERCOM_I2CS_INTFLAG_OFFSET   (0x18)         /**< (SERCOM_I2CS_INTFLAG) I2CS Interrupt Flag Status and Clear Offset */
#define SERCOM_I2CS_STATUS_OFFSET    (0x1A)         /**< (SERCOM_I2CS_STATUS) I2CS Status Offset */
#define SERCOM_I2CS_SYNCBUSY_OFFSET  (0x1C)         /**< (SERCOM_I2CS_SYNCBUSY) I2CS Synchronization Busy Offset */
#define SERCOM_I2CS_ADDR_OFFSET      (0x24)         /**< (SERCOM_I2CS_ADDR) I2CS Address Offset */
#define SERCOM_I2CS_DATA_OFFSET      (0x28)         /**< (SERCOM_I2CS_DATA) I2CS Data Offset */
/** \brief SERCOM_SPI register offsets definitions */
#define SERCOM_SPI_CTRLA_OFFSET      (0x00)         /**< (SERCOM_SPI_CTRLA) SPI Control A Offset */
#define SERCOM_SPI_CTRLB_OFFSET      (0x04)         /**< (SERCOM_SPI_CTRLB) SPI Control B Offset */
#define SERCOM_SPI_BAUD_OFFSET       (0x0C)         /**< (SERCOM_SPI_BAUD) SPI Baud Rate Offset */
#define SERCOM_SPI_INTENCLR_OFFSET   (0x14)         /**< (SERCOM_SPI_INTENCLR) SPI Interrupt Enable Clear Offset */
#define SERCOM_SPI_INTENSET_OFFSET   (0x16)         /**< (SERCOM_SPI_INTENSET) SPI Interrupt Enable Set Offset */
#define SERCOM_SPI_INTFLAG_OFFSET    (0x18)         /**< (SERCOM_SPI_INTFLAG) SPI Interrupt Flag Status and Clear Offset */
#define SERCOM_SPI_STATUS_OFFSET     (0x1A)         /**< (SERCOM_SPI_STATUS) SPI Status Offset */
#define SERCOM_SPI_SYNCBUSY_OFFSET   (0x1C)         /**< (SERCOM_SPI_SYNCBUSY) SPI Synchronization Busy Offset */
#define SERCOM_SPI_ADDR_OFFSET       (0x24)         /**< (SERCOM_SPI_ADDR) SPI Address Offset */
#define SERCOM_SPI_DATA_OFFSET       (0x28)         /**< (SERCOM_SPI_DATA) SPI Data Offset */
#define SERCOM_SPI_DBGCTRL_OFFSET    (0x30)         /**< (SERCOM_SPI_DBGCTRL) SPI Debug Control Offset */
/** \brief SERCOM_USART register offsets definitions */
#define SERCOM_USART_CTRLA_OFFSET    (0x00)         /**< (SERCOM_USART_CTRLA) USART Control A Offset */
#define SERCOM_USART_CTRLB_OFFSET    (0x04)         /**< (SERCOM_USART_CTRLB) USART Control B Offset */
#define SERCOM_USART_CTRLC_OFFSET    (0x08)         /**< (SERCOM_USART_CTRLC) USART Control C Offset */
#define SERCOM_USART_BAUD_OFFSET     (0x0C)         /**< (SERCOM_USART_BAUD) USART Baud Rate Offset */
#define SERCOM_USART_RXPL_OFFSET     (0x0E)         /**< (SERCOM_USART_RXPL) USART Receive Pulse Length Offset */
#define SERCOM_USART_INTENCLR_OFFSET (0x14)         /**< (SERCOM_USART_INTENCLR) USART Interrupt Enable Clear Offset */
#define SERCOM_USART_INTENSET_OFFSET (0x16)         /**< (SERCOM_USART_INTENSET) USART Interrupt Enable Set Offset */
#define SERCOM_USART_INTFLAG_OFFSET  (0x18)         /**< (SERCOM_USART_INTFLAG) USART Interrupt Flag Status and Clear Offset */
#define SERCOM_USART_STATUS_OFFSET   (0x1A)         /**< (SERCOM_USART_STATUS) USART Status Offset */
#define SERCOM_USART_SYNCBUSY_OFFSET (0x1C)         /**< (SERCOM_USART_SYNCBUSY) USART Synchronization Busy Offset */
#define SERCOM_USART_DATA_OFFSET     (0x28)         /**< (SERCOM_USART_DATA) USART Data Offset */
#define SERCOM_USART_DBGCTRL_OFFSET  (0x30)         /**< (SERCOM_USART_DBGCTRL) USART Debug Control Offset */
/** \brief SERCOM register offsets definitions */

/** \brief SERCOM_I2CM register API structure */
typedef struct
{  /* Serial Communication Interface - I2C Master Mode */
  __IO  uint32_t     CTRLA;         /**< Offset: 0x00 (R/W  32) I2CM Control A */
  __IO  uint32_t     CTRLB;         /**< Offset: 0x04 (R/W  32) I2CM Control B */
  __I   uint8_t                        Reserved1[0x04];
  __IO  uint32_t      BAUD;          /**< Offset: 0x0C (R/W  32) I2CM Baud Rate */
  __I   uint8_t                        Reserved2[0x04];
  __IO  uint8_t  INTENCLR;      /**< Offset: 0x14 (R/W   8) I2CM Interrupt Enable Clear */
  __I   uint8_t                        Reserved3[0x01];
  __IO  uint8_t  INTENSET;      /**< Offset: 0x16 (R/W   8) I2CM Interrupt Enable Set */
  __I   uint8_t                        Reserved4[0x01];
  __IO  uint8_t   INTFLAG;       /**< Offset: 0x18 (R/W   8) I2CM Interrupt Flag Status and Clear */
  __I   uint8_t                        Reserved5[0x01];
  __IO  uint16_t    STATUS;        /**< Offset: 0x1A (R/W  16) I2CM Status */
  __I   uint32_t  SYNCBUSY;      /**< Offset: 0x1C (R/   32) I2CM Synchronization Busy */
  __I   uint8_t                        Reserved6[0x04];
  __IO  uint32_t      ADDR;          /**< Offset: 0x24 (R/W  32) I2CM Address */
  __IO  uint8_t      DATA;          /**< Offset: 0x28 (R/W   8) I2CM Data */
  __I   uint8_t                        Reserved7[0x07];
  __IO  uint8_t   DBGCTRL;       /**< Offset: 0x30 (R/W   8) I2CM Debug Control */
} sercomi2cm_registers_t;

/** \brief SERCOM_I2CS register API structure */
typedef struct
{  /* Serial Communication Interface - I2C Slave Mode */
  __IO  uint32_t     CTRLA;         /**< Offset: 0x00 (R/W  32) I2CS Control A */
  __IO  uint32_t     CTRLB;         /**< Offset: 0x04 (R/W  32) I2CS Control B */
  __I   uint8_t                        Reserved1[0x0C];
  __IO  uint8_t  INTENCLR;      /**< Offset: 0x14 (R/W   8) I2CS Interrupt Enable Clear */
  __I   uint8_t                        Reserved2[0x01];
  __IO  uint8_t  INTENSET;      /**< Offset: 0x16 (R/W   8) I2CS Interrupt Enable Set */
  __I   uint8_t                        Reserved3[0x01];
  __IO  uint8_t   INTFLAG;       /**< Offset: 0x18 (R/W   8) I2CS Interrupt Flag Status and Clear */
  __I   uint8_t                        Reserved4[0x01];
  __IO  uint16_t    STATUS;        /**< Offset: 0x1A (R/W  16) I2CS Status */
  __I   uint32_t  SYNCBUSY;      /**< Offset: 0x1C (R/   32) I2CS Synchronization Busy */
  __I   uint8_t                        Reserved5[0x04];
  __IO  uint32_t      ADDR;          /**< Offset: 0x24 (R/W  32) I2CS Address */
  __IO  uint8_t      DATA;          /**< Offset: 0x28 (R/W   8) I2CS Data */
} sercomi2cs_registers_t;

/** \brief SERCOM_SPI register API structure */
typedef struct
{  /* Serial Communication Interface - SPI Mode */
  __IO  uint32_t      CTRLA;         /**< Offset: 0x00 (R/W  32) SPI Control A */
  __IO  uint32_t      CTRLB;         /**< Offset: 0x04 (R/W  32) SPI Control B */
  __I   uint8_t                        Reserved1[0x04];
  __IO  uint8_t       BAUD;          /**< Offset: 0x0C (R/W   8) SPI Baud Rate */
  __I   uint8_t                        Reserved2[0x07];
  __IO  uint8_t   INTENCLR;      /**< Offset: 0x14 (R/W   8) SPI Interrupt Enable Clear */
  __I   uint8_t                        Reserved3[0x01];
  __IO  uint8_t   INTENSET;      /**< Offset: 0x16 (R/W   8) SPI Interrupt Enable Set */
  __I   uint8_t                        Reserved4[0x01];
  __IO  uint8_t    INTFLAG;       /**< Offset: 0x18 (R/W   8) SPI Interrupt Flag Status and Clear */
  __I   uint8_t                        Reserved5[0x01];
  __IO  uint16_t     STATUS;        /**< Offset: 0x1A (R/W  16) SPI Status */
  __I   uint32_t   SYNCBUSY;      /**< Offset: 0x1C (R/   32) SPI Synchronization Busy */
  __I   uint8_t                        Reserved6[0x04];
  __IO  uint32_t       ADDR;          /**< Offset: 0x24 (R/W  32) SPI Address */
  __IO  uint32_t       DATA;          /**< Offset: 0x28 (R/W  32) SPI Data */
  __I   uint8_t                        Reserved7[0x04];
  __IO  uint8_t    DBGCTRL;       /**< Offset: 0x30 (R/W   8) SPI Debug Control */
} sercomspi_registers_t;

/** \brief SERCOM_USART register API structure */
typedef struct
{  /* Serial Communication Interface - USART Mode */
  __IO  uint32_t    CTRLA;         /**< Offset: 0x00 (R/W  32) USART Control A */
  __IO  uint32_t    CTRLB;         /**< Offset: 0x04 (R/W  32) USART Control B */
  __IO  uint32_t    CTRLC;         /**< Offset: 0x08 (R/W  32) USART Control C */
  __IO  uint16_t     BAUD;          /**< Offset: 0x0C (R/W  16) USART Baud Rate */
  __IO  uint8_t     RXPL;          /**< Offset: 0x0E (R/W   8) USART Receive Pulse Length */
  __I   uint8_t                        Reserved1[0x05];
  __IO  uint8_t INTENCLR;      /**< Offset: 0x14 (R/W   8) USART Interrupt Enable Clear */
  __I   uint8_t                        Reserved2[0x01];
  __IO  uint8_t INTENSET;      /**< Offset: 0x16 (R/W   8) USART Interrupt Enable Set */
  __I   uint8_t                        Reserved3[0x01];
  __IO  uint8_t  INTFLAG;       /**< Offset: 0x18 (R/W   8) USART Interrupt Flag Status and Clear */
  __I   uint8_t                        Reserved4[0x01];
  __IO  uint16_t   STATUS;        /**< Offset: 0x1A (R/W  16) USART Status */
  __I   uint32_t SYNCBUSY;      /**< Offset: 0x1C (R/   32) USART Synchronization Busy */
  __I   uint8_t                        Reserved5[0x08];
  __IO  uint16_t     DATA;          /**< Offset: 0x28 (R/W  16) USART Data */
  __I   uint8_t                        Reserved6[0x06];
  __IO  uint8_t  DBGCTRL;       /**< Offset: 0x30 (R/W   8) USART Debug Control */
} sercomusart_registers_t;

/** \brief SERCOM register API structure */

typedef union
{  /* Serial Communication Interface */
       sercomi2cm_registers_t         I2CM;           /**< Offset: 0x00 Serial Communication Interface - I2C Master Mode */
       sercomi2cs_registers_t         I2CS;           /**< Offset: 0x00 Serial Communication Interface - I2C Slave Mode */
       sercomspi_registers_t          SPI;            /**< Offset: 0x00 Serial Communication Interface - SPI Mode */
       sercomusart_registers_t        USART;          /**< Offset: 0x00 Serial Communication Interface - USART Mode */
} sercom_registers_t;
/** @}  end of Serial Communication Interface */

#endif /* _PIC32CM_JH21_SERCOM_COMPONENT_H_ */
