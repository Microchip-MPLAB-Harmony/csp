/**
 * \brief Header file for SAMC/SAMC21 DAC
 *
 * Copyright (c) 2017-2018 Microchip Technology Inc.
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

/* file generated from device description version 2018-06-27T08:27:01Z */
#ifndef SAMC_SAMC21_DAC_MODULE_H
#define SAMC_SAMC21_DAC_MODULE_H

/** \addtogroup SAMC_SAMC21 Digital Analog Converter
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_DAC                                   */
/* ========================================================================== */

/* -------- DAC_CTRLA : (DAC Offset: 0x00) (R/W 8) Control A -------- */
#define DAC_CTRLA_SWRST_Pos                   (0U)                                           /**< (DAC_CTRLA) Software Reset Position */
#define DAC_CTRLA_SWRST_Msk                   (0x1U << DAC_CTRLA_SWRST_Pos)                  /**< (DAC_CTRLA) Software Reset Mask */
#define DAC_CTRLA_SWRST(value)                (DAC_CTRLA_SWRST_Msk & ((value) << DAC_CTRLA_SWRST_Pos))
#define DAC_CTRLA_ENABLE_Pos                  (1U)                                           /**< (DAC_CTRLA) Enable Position */
#define DAC_CTRLA_ENABLE_Msk                  (0x1U << DAC_CTRLA_ENABLE_Pos)                 /**< (DAC_CTRLA) Enable Mask */
#define DAC_CTRLA_ENABLE(value)               (DAC_CTRLA_ENABLE_Msk & ((value) << DAC_CTRLA_ENABLE_Pos))
#define DAC_CTRLA_RUNSTDBY_Pos                (6U)                                           /**< (DAC_CTRLA) Run in Standby Position */
#define DAC_CTRLA_RUNSTDBY_Msk                (0x1U << DAC_CTRLA_RUNSTDBY_Pos)               /**< (DAC_CTRLA) Run in Standby Mask */
#define DAC_CTRLA_RUNSTDBY(value)             (DAC_CTRLA_RUNSTDBY_Msk & ((value) << DAC_CTRLA_RUNSTDBY_Pos))
#define DAC_CTRLA_Msk                         (0x00000043UL)                                 /**< (DAC_CTRLA) Register Mask  */

/* -------- DAC_CTRLB : (DAC Offset: 0x01) (R/W 8) Control B -------- */
#define DAC_CTRLB_EOEN_Pos                    (0U)                                           /**< (DAC_CTRLB) External Output Enable Position */
#define DAC_CTRLB_EOEN_Msk                    (0x1U << DAC_CTRLB_EOEN_Pos)                   /**< (DAC_CTRLB) External Output Enable Mask */
#define DAC_CTRLB_EOEN(value)                 (DAC_CTRLB_EOEN_Msk & ((value) << DAC_CTRLB_EOEN_Pos))
#define DAC_CTRLB_IOEN_Pos                    (1U)                                           /**< (DAC_CTRLB) Internal Output Enable Position */
#define DAC_CTRLB_IOEN_Msk                    (0x1U << DAC_CTRLB_IOEN_Pos)                   /**< (DAC_CTRLB) Internal Output Enable Mask */
#define DAC_CTRLB_IOEN(value)                 (DAC_CTRLB_IOEN_Msk & ((value) << DAC_CTRLB_IOEN_Pos))
#define DAC_CTRLB_LEFTADJ_Pos                 (2U)                                           /**< (DAC_CTRLB) Left Adjusted Data Position */
#define DAC_CTRLB_LEFTADJ_Msk                 (0x1U << DAC_CTRLB_LEFTADJ_Pos)                /**< (DAC_CTRLB) Left Adjusted Data Mask */
#define DAC_CTRLB_LEFTADJ(value)              (DAC_CTRLB_LEFTADJ_Msk & ((value) << DAC_CTRLB_LEFTADJ_Pos))
#define DAC_CTRLB_VPD_Pos                     (3U)                                           /**< (DAC_CTRLB) Voltage Pump Disable Position */
#define DAC_CTRLB_VPD_Msk                     (0x1U << DAC_CTRLB_VPD_Pos)                    /**< (DAC_CTRLB) Voltage Pump Disable Mask */
#define DAC_CTRLB_VPD(value)                  (DAC_CTRLB_VPD_Msk & ((value) << DAC_CTRLB_VPD_Pos))
#define DAC_CTRLB_DITHER_Pos                  (5U)                                           /**< (DAC_CTRLB) Dither Enable Position */
#define DAC_CTRLB_DITHER_Msk                  (0x1U << DAC_CTRLB_DITHER_Pos)                 /**< (DAC_CTRLB) Dither Enable Mask */
#define DAC_CTRLB_DITHER(value)               (DAC_CTRLB_DITHER_Msk & ((value) << DAC_CTRLB_DITHER_Pos))
#define DAC_CTRLB_REFSEL_Pos                  (6U)                                           /**< (DAC_CTRLB) Reference Selection Position */
#define DAC_CTRLB_REFSEL_Msk                  (0x3U << DAC_CTRLB_REFSEL_Pos)                 /**< (DAC_CTRLB) Reference Selection Mask */
#define DAC_CTRLB_REFSEL(value)               (DAC_CTRLB_REFSEL_Msk & ((value) << DAC_CTRLB_REFSEL_Pos))
#define   DAC_CTRLB_REFSEL_INT1V_Val          (0U)                                           /**< (DAC_CTRLB) Internal 1.0V reference  */
#define   DAC_CTRLB_REFSEL_AVCC_Val           (1U)                                           /**< (DAC_CTRLB) AVCC  */
#define   DAC_CTRLB_REFSEL_VREFP_Val          (2U)                                           /**< (DAC_CTRLB) External reference  */
#define DAC_CTRLB_REFSEL_INT1V                (DAC_CTRLB_REFSEL_INT1V_Val << DAC_CTRLB_REFSEL_Pos) /**< (DAC_CTRLB) Internal 1.0V reference Position  */
#define DAC_CTRLB_REFSEL_AVCC                 (DAC_CTRLB_REFSEL_AVCC_Val << DAC_CTRLB_REFSEL_Pos) /**< (DAC_CTRLB) AVCC Position  */
#define DAC_CTRLB_REFSEL_VREFP                (DAC_CTRLB_REFSEL_VREFP_Val << DAC_CTRLB_REFSEL_Pos) /**< (DAC_CTRLB) External reference Position  */
#define DAC_CTRLB_Msk                         (0x000000EFUL)                                 /**< (DAC_CTRLB) Register Mask  */

/* -------- DAC_EVCTRL : (DAC Offset: 0x02) (R/W 8) Event Control -------- */
#define DAC_EVCTRL_STARTEI_Pos                (0U)                                           /**< (DAC_EVCTRL) Start Conversion Event Input Position */
#define DAC_EVCTRL_STARTEI_Msk                (0x1U << DAC_EVCTRL_STARTEI_Pos)               /**< (DAC_EVCTRL) Start Conversion Event Input Mask */
#define DAC_EVCTRL_STARTEI(value)             (DAC_EVCTRL_STARTEI_Msk & ((value) << DAC_EVCTRL_STARTEI_Pos))
#define DAC_EVCTRL_EMPTYEO_Pos                (1U)                                           /**< (DAC_EVCTRL) Data Buffer Empty Event Output Position */
#define DAC_EVCTRL_EMPTYEO_Msk                (0x1U << DAC_EVCTRL_EMPTYEO_Pos)               /**< (DAC_EVCTRL) Data Buffer Empty Event Output Mask */
#define DAC_EVCTRL_EMPTYEO(value)             (DAC_EVCTRL_EMPTYEO_Msk & ((value) << DAC_EVCTRL_EMPTYEO_Pos))
#define DAC_EVCTRL_INVEI_Pos                  (2U)                                           /**< (DAC_EVCTRL) Invert Event Input Position */
#define DAC_EVCTRL_INVEI_Msk                  (0x1U << DAC_EVCTRL_INVEI_Pos)                 /**< (DAC_EVCTRL) Invert Event Input Mask */
#define DAC_EVCTRL_INVEI(value)               (DAC_EVCTRL_INVEI_Msk & ((value) << DAC_EVCTRL_INVEI_Pos))
#define DAC_EVCTRL_Msk                        (0x00000007UL)                                 /**< (DAC_EVCTRL) Register Mask  */

/* -------- DAC_INTENCLR : (DAC Offset: 0x04) (R/W 8) Interrupt Enable Clear -------- */
#define DAC_INTENCLR_UNDERRUN_Pos             (0U)                                           /**< (DAC_INTENCLR) Underrun Interrupt Enable Position */
#define DAC_INTENCLR_UNDERRUN_Msk             (0x1U << DAC_INTENCLR_UNDERRUN_Pos)            /**< (DAC_INTENCLR) Underrun Interrupt Enable Mask */
#define DAC_INTENCLR_UNDERRUN(value)          (DAC_INTENCLR_UNDERRUN_Msk & ((value) << DAC_INTENCLR_UNDERRUN_Pos))
#define DAC_INTENCLR_EMPTY_Pos                (1U)                                           /**< (DAC_INTENCLR) Data Buffer Empty Interrupt Enable Position */
#define DAC_INTENCLR_EMPTY_Msk                (0x1U << DAC_INTENCLR_EMPTY_Pos)               /**< (DAC_INTENCLR) Data Buffer Empty Interrupt Enable Mask */
#define DAC_INTENCLR_EMPTY(value)             (DAC_INTENCLR_EMPTY_Msk & ((value) << DAC_INTENCLR_EMPTY_Pos))
#define DAC_INTENCLR_Msk                      (0x00000003UL)                                 /**< (DAC_INTENCLR) Register Mask  */

/* -------- DAC_INTENSET : (DAC Offset: 0x05) (R/W 8) Interrupt Enable Set -------- */
#define DAC_INTENSET_UNDERRUN_Pos             (0U)                                           /**< (DAC_INTENSET) Underrun Interrupt Enable Position */
#define DAC_INTENSET_UNDERRUN_Msk             (0x1U << DAC_INTENSET_UNDERRUN_Pos)            /**< (DAC_INTENSET) Underrun Interrupt Enable Mask */
#define DAC_INTENSET_UNDERRUN(value)          (DAC_INTENSET_UNDERRUN_Msk & ((value) << DAC_INTENSET_UNDERRUN_Pos))
#define DAC_INTENSET_EMPTY_Pos                (1U)                                           /**< (DAC_INTENSET) Data Buffer Empty Interrupt Enable Position */
#define DAC_INTENSET_EMPTY_Msk                (0x1U << DAC_INTENSET_EMPTY_Pos)               /**< (DAC_INTENSET) Data Buffer Empty Interrupt Enable Mask */
#define DAC_INTENSET_EMPTY(value)             (DAC_INTENSET_EMPTY_Msk & ((value) << DAC_INTENSET_EMPTY_Pos))
#define DAC_INTENSET_Msk                      (0x00000003UL)                                 /**< (DAC_INTENSET) Register Mask  */

/* -------- DAC_INTFLAG : (DAC Offset: 0x06) (R/W 8) Interrupt Flag Status and Clear -------- */
#define DAC_INTFLAG_UNDERRUN_Pos              (0U)                                           /**< (DAC_INTFLAG) Underrun Position */
#define DAC_INTFLAG_UNDERRUN_Msk              (0x1U << DAC_INTFLAG_UNDERRUN_Pos)             /**< (DAC_INTFLAG) Underrun Mask */
#define DAC_INTFLAG_UNDERRUN(value)           (DAC_INTFLAG_UNDERRUN_Msk & ((value) << DAC_INTFLAG_UNDERRUN_Pos))
#define DAC_INTFLAG_EMPTY_Pos                 (1U)                                           /**< (DAC_INTFLAG) Data Buffer Empty Position */
#define DAC_INTFLAG_EMPTY_Msk                 (0x1U << DAC_INTFLAG_EMPTY_Pos)                /**< (DAC_INTFLAG) Data Buffer Empty Mask */
#define DAC_INTFLAG_EMPTY(value)              (DAC_INTFLAG_EMPTY_Msk & ((value) << DAC_INTFLAG_EMPTY_Pos))
#define DAC_INTFLAG_Msk                       (0x00000003UL)                                 /**< (DAC_INTFLAG) Register Mask  */

/* -------- DAC_STATUS : (DAC Offset: 0x07) (R/  8) Status -------- */
#define DAC_STATUS_READY_Pos                  (0U)                                           /**< (DAC_STATUS) Ready Position */
#define DAC_STATUS_READY_Msk                  (0x1U << DAC_STATUS_READY_Pos)                 /**< (DAC_STATUS) Ready Mask */
#define DAC_STATUS_READY(value)               (DAC_STATUS_READY_Msk & ((value) << DAC_STATUS_READY_Pos))
#define DAC_STATUS_Msk                        (0x00000001UL)                                 /**< (DAC_STATUS) Register Mask  */

/* -------- DAC_DATA : (DAC Offset: 0x08) ( /W 16) Data -------- */
#define DAC_DATA_DATA_Pos                     (0U)                                           /**< (DAC_DATA) Data value to be converted Position */
#define DAC_DATA_DATA_Msk                     (0xFFFFU << DAC_DATA_DATA_Pos)                 /**< (DAC_DATA) Data value to be converted Mask */
#define DAC_DATA_DATA(value)                  (DAC_DATA_DATA_Msk & ((value) << DAC_DATA_DATA_Pos))
#define DAC_DATA_Msk                          (0x0000FFFFUL)                                 /**< (DAC_DATA) Register Mask  */

/* -------- DAC_DATABUF : (DAC Offset: 0x0C) ( /W 16) Data Buffer -------- */
#define DAC_DATABUF_DATABUF_Pos               (0U)                                           /**< (DAC_DATABUF) Data Buffer Position */
#define DAC_DATABUF_DATABUF_Msk               (0xFFFFU << DAC_DATABUF_DATABUF_Pos)           /**< (DAC_DATABUF) Data Buffer Mask */
#define DAC_DATABUF_DATABUF(value)            (DAC_DATABUF_DATABUF_Msk & ((value) << DAC_DATABUF_DATABUF_Pos))
#define DAC_DATABUF_Msk                       (0x0000FFFFUL)                                 /**< (DAC_DATABUF) Register Mask  */

/* -------- DAC_SYNCBUSY : (DAC Offset: 0x10) (R/  32) Synchronization Busy -------- */
#define DAC_SYNCBUSY_SWRST_Pos                (0U)                                           /**< (DAC_SYNCBUSY) Software Reset Position */
#define DAC_SYNCBUSY_SWRST_Msk                (0x1U << DAC_SYNCBUSY_SWRST_Pos)               /**< (DAC_SYNCBUSY) Software Reset Mask */
#define DAC_SYNCBUSY_SWRST(value)             (DAC_SYNCBUSY_SWRST_Msk & ((value) << DAC_SYNCBUSY_SWRST_Pos))
#define DAC_SYNCBUSY_ENABLE_Pos               (1U)                                           /**< (DAC_SYNCBUSY) Enable Position */
#define DAC_SYNCBUSY_ENABLE_Msk               (0x1U << DAC_SYNCBUSY_ENABLE_Pos)              /**< (DAC_SYNCBUSY) Enable Mask */
#define DAC_SYNCBUSY_ENABLE(value)            (DAC_SYNCBUSY_ENABLE_Msk & ((value) << DAC_SYNCBUSY_ENABLE_Pos))
#define DAC_SYNCBUSY_DATA_Pos                 (2U)                                           /**< (DAC_SYNCBUSY) Data Position */
#define DAC_SYNCBUSY_DATA_Msk                 (0x1U << DAC_SYNCBUSY_DATA_Pos)                /**< (DAC_SYNCBUSY) Data Mask */
#define DAC_SYNCBUSY_DATA(value)              (DAC_SYNCBUSY_DATA_Msk & ((value) << DAC_SYNCBUSY_DATA_Pos))
#define DAC_SYNCBUSY_DATABUF_Pos              (3U)                                           /**< (DAC_SYNCBUSY) Data Buffer Position */
#define DAC_SYNCBUSY_DATABUF_Msk              (0x1U << DAC_SYNCBUSY_DATABUF_Pos)             /**< (DAC_SYNCBUSY) Data Buffer Mask */
#define DAC_SYNCBUSY_DATABUF(value)           (DAC_SYNCBUSY_DATABUF_Msk & ((value) << DAC_SYNCBUSY_DATABUF_Pos))
#define DAC_SYNCBUSY_Msk                      (0x0000000FUL)                                 /**< (DAC_SYNCBUSY) Register Mask  */

/* -------- DAC_DBGCTRL : (DAC Offset: 0x14) (R/W 8) Debug Control -------- */
#define DAC_DBGCTRL_DBGRUN_Pos                (0U)                                           /**< (DAC_DBGCTRL) Debug Run Position */
#define DAC_DBGCTRL_DBGRUN_Msk                (0x1U << DAC_DBGCTRL_DBGRUN_Pos)               /**< (DAC_DBGCTRL) Debug Run Mask */
#define DAC_DBGCTRL_DBGRUN(value)             (DAC_DBGCTRL_DBGRUN_Msk & ((value) << DAC_DBGCTRL_DBGRUN_Pos))
#define DAC_DBGCTRL_Msk                       (0x00000001UL)                                 /**< (DAC_DBGCTRL) Register Mask  */

/** \brief DAC register offsets definitions */
#define DAC_CTRLA_OFFSET               (0x00)         /**< (DAC_CTRLA) Control A Offset */
#define DAC_CTRLB_OFFSET               (0x01)         /**< (DAC_CTRLB) Control B Offset */
#define DAC_EVCTRL_OFFSET              (0x02)         /**< (DAC_EVCTRL) Event Control Offset */
#define DAC_INTENCLR_OFFSET            (0x04)         /**< (DAC_INTENCLR) Interrupt Enable Clear Offset */
#define DAC_INTENSET_OFFSET            (0x05)         /**< (DAC_INTENSET) Interrupt Enable Set Offset */
#define DAC_INTFLAG_OFFSET             (0x06)         /**< (DAC_INTFLAG) Interrupt Flag Status and Clear Offset */
#define DAC_STATUS_OFFSET              (0x07)         /**< (DAC_STATUS) Status Offset */
#define DAC_DATA_OFFSET                (0x08)         /**< (DAC_DATA) Data Offset */
#define DAC_DATABUF_OFFSET             (0x0C)         /**< (DAC_DATABUF) Data Buffer Offset */
#define DAC_SYNCBUSY_OFFSET            (0x10)         /**< (DAC_SYNCBUSY) Synchronization Busy Offset */
#define DAC_DBGCTRL_OFFSET             (0x14)         /**< (DAC_DBGCTRL) Debug Control Offset */

/** \brief DAC register API structure */
typedef struct
{
  __IO  uint8_t                        DAC_CTRLA;       /**< Offset: 0x00 (R/W  8) Control A */
  __IO  uint8_t                        DAC_CTRLB;       /**< Offset: 0x01 (R/W  8) Control B */
  __IO  uint8_t                        DAC_EVCTRL;      /**< Offset: 0x02 (R/W  8) Event Control */
  __I   uint8_t                        Reserved1[0x01];
  __IO  uint8_t                        DAC_INTENCLR;    /**< Offset: 0x04 (R/W  8) Interrupt Enable Clear */
  __IO  uint8_t                        DAC_INTENSET;    /**< Offset: 0x05 (R/W  8) Interrupt Enable Set */
  __IO  uint8_t                        DAC_INTFLAG;     /**< Offset: 0x06 (R/W  8) Interrupt Flag Status and Clear */
  __I   uint8_t                        DAC_STATUS;      /**< Offset: 0x07 (R/   8) Status */
  __O   uint16_t                       DAC_DATA;        /**< Offset: 0x08 ( /W  16) Data */
  __I   uint8_t                        Reserved2[0x02];
  __O   uint16_t                       DAC_DATABUF;     /**< Offset: 0x0c ( /W  16) Data Buffer */
  __I   uint8_t                        Reserved3[0x02];
  __I   uint32_t                       DAC_SYNCBUSY;    /**< Offset: 0x10 (R/   32) Synchronization Busy */
  __IO  uint8_t                        DAC_DBGCTRL;     /**< Offset: 0x14 (R/W  8) Debug Control */
} dac_registers_t;
/** @}  end of Digital Analog Converter */

#endif /* SAMC_SAMC21_DAC_MODULE_H */

