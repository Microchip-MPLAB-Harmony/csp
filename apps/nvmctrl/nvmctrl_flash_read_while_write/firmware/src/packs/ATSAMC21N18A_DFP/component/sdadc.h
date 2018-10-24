/**
 * \brief Header file for SAMC/SAMC21 SDADC
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
#ifndef SAMC_SAMC21_SDADC_MODULE_H
#define SAMC_SAMC21_SDADC_MODULE_H

/** \addtogroup SAMC_SAMC21 Sigma-Delta Analog Digital Converter
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_SDADC                                 */
/* ========================================================================== */

/* -------- SDADC_CTRLA : (SDADC Offset: 0x00) (R/W 8) Control A -------- */
#define SDADC_CTRLA_SWRST_Pos                 (0U)                                           /**< (SDADC_CTRLA) Software Reset Position */
#define SDADC_CTRLA_SWRST_Msk                 (0x1U << SDADC_CTRLA_SWRST_Pos)                /**< (SDADC_CTRLA) Software Reset Mask */
#define SDADC_CTRLA_SWRST(value)              (SDADC_CTRLA_SWRST_Msk & ((value) << SDADC_CTRLA_SWRST_Pos))
#define SDADC_CTRLA_ENABLE_Pos                (1U)                                           /**< (SDADC_CTRLA) Enable Position */
#define SDADC_CTRLA_ENABLE_Msk                (0x1U << SDADC_CTRLA_ENABLE_Pos)               /**< (SDADC_CTRLA) Enable Mask */
#define SDADC_CTRLA_ENABLE(value)             (SDADC_CTRLA_ENABLE_Msk & ((value) << SDADC_CTRLA_ENABLE_Pos))
#define SDADC_CTRLA_RUNSTDBY_Pos              (6U)                                           /**< (SDADC_CTRLA) Run during Standby Position */
#define SDADC_CTRLA_RUNSTDBY_Msk              (0x1U << SDADC_CTRLA_RUNSTDBY_Pos)             /**< (SDADC_CTRLA) Run during Standby Mask */
#define SDADC_CTRLA_RUNSTDBY(value)           (SDADC_CTRLA_RUNSTDBY_Msk & ((value) << SDADC_CTRLA_RUNSTDBY_Pos))
#define SDADC_CTRLA_ONDEMAND_Pos              (7U)                                           /**< (SDADC_CTRLA) On Demand Control Position */
#define SDADC_CTRLA_ONDEMAND_Msk              (0x1U << SDADC_CTRLA_ONDEMAND_Pos)             /**< (SDADC_CTRLA) On Demand Control Mask */
#define SDADC_CTRLA_ONDEMAND(value)           (SDADC_CTRLA_ONDEMAND_Msk & ((value) << SDADC_CTRLA_ONDEMAND_Pos))
#define SDADC_CTRLA_Msk                       (0x000000C3UL)                                 /**< (SDADC_CTRLA) Register Mask  */

/* -------- SDADC_REFCTRL : (SDADC Offset: 0x01) (R/W 8) Reference Control -------- */
#define SDADC_REFCTRL_REFSEL_Pos              (0U)                                           /**< (SDADC_REFCTRL) Reference Selection Position */
#define SDADC_REFCTRL_REFSEL_Msk              (0x3U << SDADC_REFCTRL_REFSEL_Pos)             /**< (SDADC_REFCTRL) Reference Selection Mask */
#define SDADC_REFCTRL_REFSEL(value)           (SDADC_REFCTRL_REFSEL_Msk & ((value) << SDADC_REFCTRL_REFSEL_Pos))
#define   SDADC_REFCTRL_REFSEL_INTREF_Val     (0U)                                           /**< (SDADC_REFCTRL) Internal Bandgap Reference  */
#define   SDADC_REFCTRL_REFSEL_AREFB_Val      (1U)                                           /**< (SDADC_REFCTRL) External Reference  */
#define   SDADC_REFCTRL_REFSEL_DAC_Val        (2U)                                           /**< (SDADC_REFCTRL) Internal DAC Output  */
#define   SDADC_REFCTRL_REFSEL_INTVCC_Val     (3U)                                           /**< (SDADC_REFCTRL) VDDANA  */
#define SDADC_REFCTRL_REFSEL_INTREF           (SDADC_REFCTRL_REFSEL_INTREF_Val << SDADC_REFCTRL_REFSEL_Pos) /**< (SDADC_REFCTRL) Internal Bandgap Reference Position  */
#define SDADC_REFCTRL_REFSEL_AREFB            (SDADC_REFCTRL_REFSEL_AREFB_Val << SDADC_REFCTRL_REFSEL_Pos) /**< (SDADC_REFCTRL) External Reference Position  */
#define SDADC_REFCTRL_REFSEL_DAC              (SDADC_REFCTRL_REFSEL_DAC_Val << SDADC_REFCTRL_REFSEL_Pos) /**< (SDADC_REFCTRL) Internal DAC Output Position  */
#define SDADC_REFCTRL_REFSEL_INTVCC           (SDADC_REFCTRL_REFSEL_INTVCC_Val << SDADC_REFCTRL_REFSEL_Pos) /**< (SDADC_REFCTRL) VDDANA Position  */
#define SDADC_REFCTRL_REFRANGE_Pos            (4U)                                           /**< (SDADC_REFCTRL) Reference Range Position */
#define SDADC_REFCTRL_REFRANGE_Msk            (0x3U << SDADC_REFCTRL_REFRANGE_Pos)           /**< (SDADC_REFCTRL) Reference Range Mask */
#define SDADC_REFCTRL_REFRANGE(value)         (SDADC_REFCTRL_REFRANGE_Msk & ((value) << SDADC_REFCTRL_REFRANGE_Pos))
#define SDADC_REFCTRL_ONREFBUF_Pos            (7U)                                           /**< (SDADC_REFCTRL) Reference Buffer Position */
#define SDADC_REFCTRL_ONREFBUF_Msk            (0x1U << SDADC_REFCTRL_ONREFBUF_Pos)           /**< (SDADC_REFCTRL) Reference Buffer Mask */
#define SDADC_REFCTRL_ONREFBUF(value)         (SDADC_REFCTRL_ONREFBUF_Msk & ((value) << SDADC_REFCTRL_ONREFBUF_Pos))
#define SDADC_REFCTRL_Msk                     (0x000000B3UL)                                 /**< (SDADC_REFCTRL) Register Mask  */

/* -------- SDADC_CTRLB : (SDADC Offset: 0x02) (R/W 16) Control B -------- */
#define SDADC_CTRLB_PRESCALER_Pos             (0U)                                           /**< (SDADC_CTRLB) Prescaler Configuration Position */
#define SDADC_CTRLB_PRESCALER_Msk             (0xFFU << SDADC_CTRLB_PRESCALER_Pos)           /**< (SDADC_CTRLB) Prescaler Configuration Mask */
#define SDADC_CTRLB_PRESCALER(value)          (SDADC_CTRLB_PRESCALER_Msk & ((value) << SDADC_CTRLB_PRESCALER_Pos))
#define   SDADC_CTRLB_PRESCALER_DIV2_Val      (0U)                                           /**< (SDADC_CTRLB) Peripheral clock divided by 2  */
#define   SDADC_CTRLB_PRESCALER_DIV4_Val      (1U)                                           /**< (SDADC_CTRLB) Peripheral clock divided by 4  */
#define   SDADC_CTRLB_PRESCALER_DIV8_Val      (2U)                                           /**< (SDADC_CTRLB) Peripheral clock divided by 8  */
#define   SDADC_CTRLB_PRESCALER_DIV16_Val     (3U)                                           /**< (SDADC_CTRLB) Peripheral clock divided by 16  */
#define   SDADC_CTRLB_PRESCALER_DIV32_Val     (4U)                                           /**< (SDADC_CTRLB) Peripheral clock divided by 32  */
#define   SDADC_CTRLB_PRESCALER_DIV64_Val     (5U)                                           /**< (SDADC_CTRLB) Peripheral clock divided by 64  */
#define   SDADC_CTRLB_PRESCALER_DIV128_Val    (6U)                                           /**< (SDADC_CTRLB) Peripheral clock divided by 128  */
#define   SDADC_CTRLB_PRESCALER_DIV256_Val    (7U)                                           /**< (SDADC_CTRLB) Peripheral clock divided by 256  */
#define SDADC_CTRLB_PRESCALER_DIV2            (SDADC_CTRLB_PRESCALER_DIV2_Val << SDADC_CTRLB_PRESCALER_Pos) /**< (SDADC_CTRLB) Peripheral clock divided by 2 Position  */
#define SDADC_CTRLB_PRESCALER_DIV4            (SDADC_CTRLB_PRESCALER_DIV4_Val << SDADC_CTRLB_PRESCALER_Pos) /**< (SDADC_CTRLB) Peripheral clock divided by 4 Position  */
#define SDADC_CTRLB_PRESCALER_DIV8            (SDADC_CTRLB_PRESCALER_DIV8_Val << SDADC_CTRLB_PRESCALER_Pos) /**< (SDADC_CTRLB) Peripheral clock divided by 8 Position  */
#define SDADC_CTRLB_PRESCALER_DIV16           (SDADC_CTRLB_PRESCALER_DIV16_Val << SDADC_CTRLB_PRESCALER_Pos) /**< (SDADC_CTRLB) Peripheral clock divided by 16 Position  */
#define SDADC_CTRLB_PRESCALER_DIV32           (SDADC_CTRLB_PRESCALER_DIV32_Val << SDADC_CTRLB_PRESCALER_Pos) /**< (SDADC_CTRLB) Peripheral clock divided by 32 Position  */
#define SDADC_CTRLB_PRESCALER_DIV64           (SDADC_CTRLB_PRESCALER_DIV64_Val << SDADC_CTRLB_PRESCALER_Pos) /**< (SDADC_CTRLB) Peripheral clock divided by 64 Position  */
#define SDADC_CTRLB_PRESCALER_DIV128          (SDADC_CTRLB_PRESCALER_DIV128_Val << SDADC_CTRLB_PRESCALER_Pos) /**< (SDADC_CTRLB) Peripheral clock divided by 128 Position  */
#define SDADC_CTRLB_PRESCALER_DIV256          (SDADC_CTRLB_PRESCALER_DIV256_Val << SDADC_CTRLB_PRESCALER_Pos) /**< (SDADC_CTRLB) Peripheral clock divided by 256 Position  */
#define SDADC_CTRLB_OSR_Pos                   (8U)                                           /**< (SDADC_CTRLB) Over Sampling Ratio Position */
#define SDADC_CTRLB_OSR_Msk                   (0x7U << SDADC_CTRLB_OSR_Pos)                  /**< (SDADC_CTRLB) Over Sampling Ratio Mask */
#define SDADC_CTRLB_OSR(value)                (SDADC_CTRLB_OSR_Msk & ((value) << SDADC_CTRLB_OSR_Pos))
#define   SDADC_CTRLB_OSR_OSR64_Val           (0U)                                           /**< (SDADC_CTRLB) Over Sampling Ratio is 64  */
#define   SDADC_CTRLB_OSR_OSR128_Val          (1U)                                           /**< (SDADC_CTRLB) Over Sampling Ratio is 128  */
#define   SDADC_CTRLB_OSR_OSR256_Val          (2U)                                           /**< (SDADC_CTRLB) Over Sampling Ratio is 256  */
#define   SDADC_CTRLB_OSR_OSR512_Val          (3U)                                           /**< (SDADC_CTRLB) Over Sampling Ratio is 512  */
#define   SDADC_CTRLB_OSR_OSR1024_Val         (4U)                                           /**< (SDADC_CTRLB) Over Sampling Ratio is 1024  */
#define SDADC_CTRLB_OSR_OSR64                 (SDADC_CTRLB_OSR_OSR64_Val << SDADC_CTRLB_OSR_Pos) /**< (SDADC_CTRLB) Over Sampling Ratio is 64 Position  */
#define SDADC_CTRLB_OSR_OSR128                (SDADC_CTRLB_OSR_OSR128_Val << SDADC_CTRLB_OSR_Pos) /**< (SDADC_CTRLB) Over Sampling Ratio is 128 Position  */
#define SDADC_CTRLB_OSR_OSR256                (SDADC_CTRLB_OSR_OSR256_Val << SDADC_CTRLB_OSR_Pos) /**< (SDADC_CTRLB) Over Sampling Ratio is 256 Position  */
#define SDADC_CTRLB_OSR_OSR512                (SDADC_CTRLB_OSR_OSR512_Val << SDADC_CTRLB_OSR_Pos) /**< (SDADC_CTRLB) Over Sampling Ratio is 512 Position  */
#define SDADC_CTRLB_OSR_OSR1024               (SDADC_CTRLB_OSR_OSR1024_Val << SDADC_CTRLB_OSR_Pos) /**< (SDADC_CTRLB) Over Sampling Ratio is 1024 Position  */
#define SDADC_CTRLB_SKPCNT_Pos                (12U)                                          /**< (SDADC_CTRLB) Skip Sample Count Position */
#define SDADC_CTRLB_SKPCNT_Msk                (0xFU << SDADC_CTRLB_SKPCNT_Pos)               /**< (SDADC_CTRLB) Skip Sample Count Mask */
#define SDADC_CTRLB_SKPCNT(value)             (SDADC_CTRLB_SKPCNT_Msk & ((value) << SDADC_CTRLB_SKPCNT_Pos))
#define SDADC_CTRLB_Msk                       (0x0000F7FFUL)                                 /**< (SDADC_CTRLB) Register Mask  */

/* -------- SDADC_EVCTRL : (SDADC Offset: 0x04) (R/W 8) Event Control -------- */
#define SDADC_EVCTRL_FLUSHEI_Pos              (0U)                                           /**< (SDADC_EVCTRL) Flush Event Input Enable Position */
#define SDADC_EVCTRL_FLUSHEI_Msk              (0x1U << SDADC_EVCTRL_FLUSHEI_Pos)             /**< (SDADC_EVCTRL) Flush Event Input Enable Mask */
#define SDADC_EVCTRL_FLUSHEI(value)           (SDADC_EVCTRL_FLUSHEI_Msk & ((value) << SDADC_EVCTRL_FLUSHEI_Pos))
#define SDADC_EVCTRL_STARTEI_Pos              (1U)                                           /**< (SDADC_EVCTRL) Start Conversion Event Input Enable Position */
#define SDADC_EVCTRL_STARTEI_Msk              (0x1U << SDADC_EVCTRL_STARTEI_Pos)             /**< (SDADC_EVCTRL) Start Conversion Event Input Enable Mask */
#define SDADC_EVCTRL_STARTEI(value)           (SDADC_EVCTRL_STARTEI_Msk & ((value) << SDADC_EVCTRL_STARTEI_Pos))
#define SDADC_EVCTRL_FLUSHINV_Pos             (2U)                                           /**< (SDADC_EVCTRL) Flush Event Invert Enable Position */
#define SDADC_EVCTRL_FLUSHINV_Msk             (0x1U << SDADC_EVCTRL_FLUSHINV_Pos)            /**< (SDADC_EVCTRL) Flush Event Invert Enable Mask */
#define SDADC_EVCTRL_FLUSHINV(value)          (SDADC_EVCTRL_FLUSHINV_Msk & ((value) << SDADC_EVCTRL_FLUSHINV_Pos))
#define SDADC_EVCTRL_STARTINV_Pos             (3U)                                           /**< (SDADC_EVCTRL) Satrt Event Invert Enable Position */
#define SDADC_EVCTRL_STARTINV_Msk             (0x1U << SDADC_EVCTRL_STARTINV_Pos)            /**< (SDADC_EVCTRL) Satrt Event Invert Enable Mask */
#define SDADC_EVCTRL_STARTINV(value)          (SDADC_EVCTRL_STARTINV_Msk & ((value) << SDADC_EVCTRL_STARTINV_Pos))
#define SDADC_EVCTRL_RESRDYEO_Pos             (4U)                                           /**< (SDADC_EVCTRL) Result Ready Event Out Position */
#define SDADC_EVCTRL_RESRDYEO_Msk             (0x1U << SDADC_EVCTRL_RESRDYEO_Pos)            /**< (SDADC_EVCTRL) Result Ready Event Out Mask */
#define SDADC_EVCTRL_RESRDYEO(value)          (SDADC_EVCTRL_RESRDYEO_Msk & ((value) << SDADC_EVCTRL_RESRDYEO_Pos))
#define SDADC_EVCTRL_WINMONEO_Pos             (5U)                                           /**< (SDADC_EVCTRL) Window Monitor Event Out Position */
#define SDADC_EVCTRL_WINMONEO_Msk             (0x1U << SDADC_EVCTRL_WINMONEO_Pos)            /**< (SDADC_EVCTRL) Window Monitor Event Out Mask */
#define SDADC_EVCTRL_WINMONEO(value)          (SDADC_EVCTRL_WINMONEO_Msk & ((value) << SDADC_EVCTRL_WINMONEO_Pos))
#define SDADC_EVCTRL_Msk                      (0x0000003FUL)                                 /**< (SDADC_EVCTRL) Register Mask  */

/* -------- SDADC_INTENCLR : (SDADC Offset: 0x05) (R/W 8) Interrupt Enable Clear -------- */
#define SDADC_INTENCLR_RESRDY_Pos             (0U)                                           /**< (SDADC_INTENCLR) Result Ready Interrupt Disable Position */
#define SDADC_INTENCLR_RESRDY_Msk             (0x1U << SDADC_INTENCLR_RESRDY_Pos)            /**< (SDADC_INTENCLR) Result Ready Interrupt Disable Mask */
#define SDADC_INTENCLR_RESRDY(value)          (SDADC_INTENCLR_RESRDY_Msk & ((value) << SDADC_INTENCLR_RESRDY_Pos))
#define SDADC_INTENCLR_OVERRUN_Pos            (1U)                                           /**< (SDADC_INTENCLR) Overrun Interrupt Disable Position */
#define SDADC_INTENCLR_OVERRUN_Msk            (0x1U << SDADC_INTENCLR_OVERRUN_Pos)           /**< (SDADC_INTENCLR) Overrun Interrupt Disable Mask */
#define SDADC_INTENCLR_OVERRUN(value)         (SDADC_INTENCLR_OVERRUN_Msk & ((value) << SDADC_INTENCLR_OVERRUN_Pos))
#define SDADC_INTENCLR_WINMON_Pos             (2U)                                           /**< (SDADC_INTENCLR) Window Monitor Interrupt Disable Position */
#define SDADC_INTENCLR_WINMON_Msk             (0x1U << SDADC_INTENCLR_WINMON_Pos)            /**< (SDADC_INTENCLR) Window Monitor Interrupt Disable Mask */
#define SDADC_INTENCLR_WINMON(value)          (SDADC_INTENCLR_WINMON_Msk & ((value) << SDADC_INTENCLR_WINMON_Pos))
#define SDADC_INTENCLR_Msk                    (0x00000007UL)                                 /**< (SDADC_INTENCLR) Register Mask  */

/* -------- SDADC_INTENSET : (SDADC Offset: 0x06) (R/W 8) Interrupt Enable Set -------- */
#define SDADC_INTENSET_RESRDY_Pos             (0U)                                           /**< (SDADC_INTENSET) Result Ready Interrupt Enable Position */
#define SDADC_INTENSET_RESRDY_Msk             (0x1U << SDADC_INTENSET_RESRDY_Pos)            /**< (SDADC_INTENSET) Result Ready Interrupt Enable Mask */
#define SDADC_INTENSET_RESRDY(value)          (SDADC_INTENSET_RESRDY_Msk & ((value) << SDADC_INTENSET_RESRDY_Pos))
#define SDADC_INTENSET_OVERRUN_Pos            (1U)                                           /**< (SDADC_INTENSET) Overrun Interrupt Enable Position */
#define SDADC_INTENSET_OVERRUN_Msk            (0x1U << SDADC_INTENSET_OVERRUN_Pos)           /**< (SDADC_INTENSET) Overrun Interrupt Enable Mask */
#define SDADC_INTENSET_OVERRUN(value)         (SDADC_INTENSET_OVERRUN_Msk & ((value) << SDADC_INTENSET_OVERRUN_Pos))
#define SDADC_INTENSET_WINMON_Pos             (2U)                                           /**< (SDADC_INTENSET) Window Monitor Interrupt Enable Position */
#define SDADC_INTENSET_WINMON_Msk             (0x1U << SDADC_INTENSET_WINMON_Pos)            /**< (SDADC_INTENSET) Window Monitor Interrupt Enable Mask */
#define SDADC_INTENSET_WINMON(value)          (SDADC_INTENSET_WINMON_Msk & ((value) << SDADC_INTENSET_WINMON_Pos))
#define SDADC_INTENSET_Msk                    (0x00000007UL)                                 /**< (SDADC_INTENSET) Register Mask  */

/* -------- SDADC_INTFLAG : (SDADC Offset: 0x07) (R/W 8) Interrupt Flag Status and Clear -------- */
#define SDADC_INTFLAG_RESRDY_Pos              (0U)                                           /**< (SDADC_INTFLAG) Result Ready Interrupt Flag Position */
#define SDADC_INTFLAG_RESRDY_Msk              (0x1U << SDADC_INTFLAG_RESRDY_Pos)             /**< (SDADC_INTFLAG) Result Ready Interrupt Flag Mask */
#define SDADC_INTFLAG_RESRDY(value)           (SDADC_INTFLAG_RESRDY_Msk & ((value) << SDADC_INTFLAG_RESRDY_Pos))
#define SDADC_INTFLAG_OVERRUN_Pos             (1U)                                           /**< (SDADC_INTFLAG) Overrun Interrupt Flag Position */
#define SDADC_INTFLAG_OVERRUN_Msk             (0x1U << SDADC_INTFLAG_OVERRUN_Pos)            /**< (SDADC_INTFLAG) Overrun Interrupt Flag Mask */
#define SDADC_INTFLAG_OVERRUN(value)          (SDADC_INTFLAG_OVERRUN_Msk & ((value) << SDADC_INTFLAG_OVERRUN_Pos))
#define SDADC_INTFLAG_WINMON_Pos              (2U)                                           /**< (SDADC_INTFLAG) Window Monitor Interrupt Flag Position */
#define SDADC_INTFLAG_WINMON_Msk              (0x1U << SDADC_INTFLAG_WINMON_Pos)             /**< (SDADC_INTFLAG) Window Monitor Interrupt Flag Mask */
#define SDADC_INTFLAG_WINMON(value)           (SDADC_INTFLAG_WINMON_Msk & ((value) << SDADC_INTFLAG_WINMON_Pos))
#define SDADC_INTFLAG_Msk                     (0x00000007UL)                                 /**< (SDADC_INTFLAG) Register Mask  */

/* -------- SDADC_SEQSTATUS : (SDADC Offset: 0x08) (R/  8) Sequence Status -------- */
#define SDADC_SEQSTATUS_SEQSTATE_Pos          (0U)                                           /**< (SDADC_SEQSTATUS) Sequence State Position */
#define SDADC_SEQSTATUS_SEQSTATE_Msk          (0xFU << SDADC_SEQSTATUS_SEQSTATE_Pos)         /**< (SDADC_SEQSTATUS) Sequence State Mask */
#define SDADC_SEQSTATUS_SEQSTATE(value)       (SDADC_SEQSTATUS_SEQSTATE_Msk & ((value) << SDADC_SEQSTATUS_SEQSTATE_Pos))
#define SDADC_SEQSTATUS_SEQBUSY_Pos           (7U)                                           /**< (SDADC_SEQSTATUS) Sequence Busy Position */
#define SDADC_SEQSTATUS_SEQBUSY_Msk           (0x1U << SDADC_SEQSTATUS_SEQBUSY_Pos)          /**< (SDADC_SEQSTATUS) Sequence Busy Mask */
#define SDADC_SEQSTATUS_SEQBUSY(value)        (SDADC_SEQSTATUS_SEQBUSY_Msk & ((value) << SDADC_SEQSTATUS_SEQBUSY_Pos))
#define SDADC_SEQSTATUS_Msk                   (0x0000008FUL)                                 /**< (SDADC_SEQSTATUS) Register Mask  */

/* -------- SDADC_INPUTCTRL : (SDADC Offset: 0x09) (R/W 8) Input Control -------- */
#define SDADC_INPUTCTRL_MUXSEL_Pos            (0U)                                           /**< (SDADC_INPUTCTRL) SDADC Input Selection Position */
#define SDADC_INPUTCTRL_MUXSEL_Msk            (0xFU << SDADC_INPUTCTRL_MUXSEL_Pos)           /**< (SDADC_INPUTCTRL) SDADC Input Selection Mask */
#define SDADC_INPUTCTRL_MUXSEL(value)         (SDADC_INPUTCTRL_MUXSEL_Msk & ((value) << SDADC_INPUTCTRL_MUXSEL_Pos))
#define   SDADC_INPUTCTRL_MUXSEL_AIN0_Val     (0U)                                           /**< (SDADC_INPUTCTRL) SDADC AIN0 Pin  */
#define   SDADC_INPUTCTRL_MUXSEL_AIN1_Val     (1U)                                           /**< (SDADC_INPUTCTRL) SDADC AIN1 Pin  */
#define   SDADC_INPUTCTRL_MUXSEL_AIN2_Val     (2U)                                           /**< (SDADC_INPUTCTRL) SDADC AIN2 Pin  */
#define SDADC_INPUTCTRL_MUXSEL_AIN0           (SDADC_INPUTCTRL_MUXSEL_AIN0_Val << SDADC_INPUTCTRL_MUXSEL_Pos) /**< (SDADC_INPUTCTRL) SDADC AIN0 Pin Position  */
#define SDADC_INPUTCTRL_MUXSEL_AIN1           (SDADC_INPUTCTRL_MUXSEL_AIN1_Val << SDADC_INPUTCTRL_MUXSEL_Pos) /**< (SDADC_INPUTCTRL) SDADC AIN1 Pin Position  */
#define SDADC_INPUTCTRL_MUXSEL_AIN2           (SDADC_INPUTCTRL_MUXSEL_AIN2_Val << SDADC_INPUTCTRL_MUXSEL_Pos) /**< (SDADC_INPUTCTRL) SDADC AIN2 Pin Position  */
#define SDADC_INPUTCTRL_Msk                   (0x0000000FUL)                                 /**< (SDADC_INPUTCTRL) Register Mask  */

/* -------- SDADC_CTRLC : (SDADC Offset: 0x0A) (R/W 8) Control C -------- */
#define SDADC_CTRLC_FREERUN_Pos               (0U)                                           /**< (SDADC_CTRLC) Free Running Mode Position */
#define SDADC_CTRLC_FREERUN_Msk               (0x1U << SDADC_CTRLC_FREERUN_Pos)              /**< (SDADC_CTRLC) Free Running Mode Mask */
#define SDADC_CTRLC_FREERUN(value)            (SDADC_CTRLC_FREERUN_Msk & ((value) << SDADC_CTRLC_FREERUN_Pos))
#define SDADC_CTRLC_Msk                       (0x00000001UL)                                 /**< (SDADC_CTRLC) Register Mask  */

/* -------- SDADC_WINCTRL : (SDADC Offset: 0x0B) (R/W 8) Window Monitor Control -------- */
#define SDADC_WINCTRL_WINMODE_Pos             (0U)                                           /**< (SDADC_WINCTRL) Window Monitor Mode Position */
#define SDADC_WINCTRL_WINMODE_Msk             (0x7U << SDADC_WINCTRL_WINMODE_Pos)            /**< (SDADC_WINCTRL) Window Monitor Mode Mask */
#define SDADC_WINCTRL_WINMODE(value)          (SDADC_WINCTRL_WINMODE_Msk & ((value) << SDADC_WINCTRL_WINMODE_Pos))
#define SDADC_WINCTRL_Msk                     (0x00000007UL)                                 /**< (SDADC_WINCTRL) Register Mask  */

/* -------- SDADC_WINLT : (SDADC Offset: 0x0C) (R/W 32) Window Monitor Lower Threshold -------- */
#define SDADC_WINLT_WINLT_Pos                 (0U)                                           /**< (SDADC_WINLT) Window Lower Threshold Position */
#define SDADC_WINLT_WINLT_Msk                 (0xFFFFFFU << SDADC_WINLT_WINLT_Pos)           /**< (SDADC_WINLT) Window Lower Threshold Mask */
#define SDADC_WINLT_WINLT(value)              (SDADC_WINLT_WINLT_Msk & ((value) << SDADC_WINLT_WINLT_Pos))
#define SDADC_WINLT_Msk                       (0x00FFFFFFUL)                                 /**< (SDADC_WINLT) Register Mask  */

/* -------- SDADC_WINUT : (SDADC Offset: 0x10) (R/W 32) Window Monitor Upper Threshold -------- */
#define SDADC_WINUT_WINUT_Pos                 (0U)                                           /**< (SDADC_WINUT) Window Upper Threshold Position */
#define SDADC_WINUT_WINUT_Msk                 (0xFFFFFFU << SDADC_WINUT_WINUT_Pos)           /**< (SDADC_WINUT) Window Upper Threshold Mask */
#define SDADC_WINUT_WINUT(value)              (SDADC_WINUT_WINUT_Msk & ((value) << SDADC_WINUT_WINUT_Pos))
#define SDADC_WINUT_Msk                       (0x00FFFFFFUL)                                 /**< (SDADC_WINUT) Register Mask  */

/* -------- SDADC_OFFSETCORR : (SDADC Offset: 0x14) (R/W 32) Offset Correction -------- */
#define SDADC_OFFSETCORR_OFFSETCORR_Pos       (0U)                                           /**< (SDADC_OFFSETCORR) Offset Correction Value Position */
#define SDADC_OFFSETCORR_OFFSETCORR_Msk       (0xFFFFFFU << SDADC_OFFSETCORR_OFFSETCORR_Pos) /**< (SDADC_OFFSETCORR) Offset Correction Value Mask */
#define SDADC_OFFSETCORR_OFFSETCORR(value)    (SDADC_OFFSETCORR_OFFSETCORR_Msk & ((value) << SDADC_OFFSETCORR_OFFSETCORR_Pos))
#define SDADC_OFFSETCORR_Msk                  (0x00FFFFFFUL)                                 /**< (SDADC_OFFSETCORR) Register Mask  */

/* -------- SDADC_GAINCORR : (SDADC Offset: 0x18) (R/W 16) Gain Correction -------- */
#define SDADC_GAINCORR_GAINCORR_Pos           (0U)                                           /**< (SDADC_GAINCORR) Gain Correction Value Position */
#define SDADC_GAINCORR_GAINCORR_Msk           (0x3FFFU << SDADC_GAINCORR_GAINCORR_Pos)       /**< (SDADC_GAINCORR) Gain Correction Value Mask */
#define SDADC_GAINCORR_GAINCORR(value)        (SDADC_GAINCORR_GAINCORR_Msk & ((value) << SDADC_GAINCORR_GAINCORR_Pos))
#define SDADC_GAINCORR_Msk                    (0x00003FFFUL)                                 /**< (SDADC_GAINCORR) Register Mask  */

/* -------- SDADC_SHIFTCORR : (SDADC Offset: 0x1A) (R/W 8) Shift Correction -------- */
#define SDADC_SHIFTCORR_SHIFTCORR_Pos         (0U)                                           /**< (SDADC_SHIFTCORR) Shift Correction Value Position */
#define SDADC_SHIFTCORR_SHIFTCORR_Msk         (0xFU << SDADC_SHIFTCORR_SHIFTCORR_Pos)        /**< (SDADC_SHIFTCORR) Shift Correction Value Mask */
#define SDADC_SHIFTCORR_SHIFTCORR(value)      (SDADC_SHIFTCORR_SHIFTCORR_Msk & ((value) << SDADC_SHIFTCORR_SHIFTCORR_Pos))
#define SDADC_SHIFTCORR_Msk                   (0x0000000FUL)                                 /**< (SDADC_SHIFTCORR) Register Mask  */

/* -------- SDADC_SWTRIG : (SDADC Offset: 0x1C) (R/W 8) Software Trigger -------- */
#define SDADC_SWTRIG_FLUSH_Pos                (0U)                                           /**< (SDADC_SWTRIG) SDADC Flush Position */
#define SDADC_SWTRIG_FLUSH_Msk                (0x1U << SDADC_SWTRIG_FLUSH_Pos)               /**< (SDADC_SWTRIG) SDADC Flush Mask */
#define SDADC_SWTRIG_FLUSH(value)             (SDADC_SWTRIG_FLUSH_Msk & ((value) << SDADC_SWTRIG_FLUSH_Pos))
#define SDADC_SWTRIG_START_Pos                (1U)                                           /**< (SDADC_SWTRIG) Start SDADC Conversion Position */
#define SDADC_SWTRIG_START_Msk                (0x1U << SDADC_SWTRIG_START_Pos)               /**< (SDADC_SWTRIG) Start SDADC Conversion Mask */
#define SDADC_SWTRIG_START(value)             (SDADC_SWTRIG_START_Msk & ((value) << SDADC_SWTRIG_START_Pos))
#define SDADC_SWTRIG_Msk                      (0x00000003UL)                                 /**< (SDADC_SWTRIG) Register Mask  */

/* -------- SDADC_SYNCBUSY : (SDADC Offset: 0x20) (R/  32) Synchronization Busy -------- */
#define SDADC_SYNCBUSY_SWRST_Pos              (0U)                                           /**< (SDADC_SYNCBUSY) SWRST Synchronization Busy Position */
#define SDADC_SYNCBUSY_SWRST_Msk              (0x1U << SDADC_SYNCBUSY_SWRST_Pos)             /**< (SDADC_SYNCBUSY) SWRST Synchronization Busy Mask */
#define SDADC_SYNCBUSY_SWRST(value)           (SDADC_SYNCBUSY_SWRST_Msk & ((value) << SDADC_SYNCBUSY_SWRST_Pos))
#define SDADC_SYNCBUSY_ENABLE_Pos             (1U)                                           /**< (SDADC_SYNCBUSY) ENABLE Synchronization Busy Position */
#define SDADC_SYNCBUSY_ENABLE_Msk             (0x1U << SDADC_SYNCBUSY_ENABLE_Pos)            /**< (SDADC_SYNCBUSY) ENABLE Synchronization Busy Mask */
#define SDADC_SYNCBUSY_ENABLE(value)          (SDADC_SYNCBUSY_ENABLE_Msk & ((value) << SDADC_SYNCBUSY_ENABLE_Pos))
#define SDADC_SYNCBUSY_CTRLC_Pos              (2U)                                           /**< (SDADC_SYNCBUSY) CTRLC Synchronization Busy Position */
#define SDADC_SYNCBUSY_CTRLC_Msk              (0x1U << SDADC_SYNCBUSY_CTRLC_Pos)             /**< (SDADC_SYNCBUSY) CTRLC Synchronization Busy Mask */
#define SDADC_SYNCBUSY_CTRLC(value)           (SDADC_SYNCBUSY_CTRLC_Msk & ((value) << SDADC_SYNCBUSY_CTRLC_Pos))
#define SDADC_SYNCBUSY_INPUTCTRL_Pos          (3U)                                           /**< (SDADC_SYNCBUSY) INPUTCTRL Synchronization Busy Position */
#define SDADC_SYNCBUSY_INPUTCTRL_Msk          (0x1U << SDADC_SYNCBUSY_INPUTCTRL_Pos)         /**< (SDADC_SYNCBUSY) INPUTCTRL Synchronization Busy Mask */
#define SDADC_SYNCBUSY_INPUTCTRL(value)       (SDADC_SYNCBUSY_INPUTCTRL_Msk & ((value) << SDADC_SYNCBUSY_INPUTCTRL_Pos))
#define SDADC_SYNCBUSY_WINCTRL_Pos            (4U)                                           /**< (SDADC_SYNCBUSY) WINCTRL Synchronization Busy Position */
#define SDADC_SYNCBUSY_WINCTRL_Msk            (0x1U << SDADC_SYNCBUSY_WINCTRL_Pos)           /**< (SDADC_SYNCBUSY) WINCTRL Synchronization Busy Mask */
#define SDADC_SYNCBUSY_WINCTRL(value)         (SDADC_SYNCBUSY_WINCTRL_Msk & ((value) << SDADC_SYNCBUSY_WINCTRL_Pos))
#define SDADC_SYNCBUSY_WINLT_Pos              (5U)                                           /**< (SDADC_SYNCBUSY) WINLT Synchronization Busy Position */
#define SDADC_SYNCBUSY_WINLT_Msk              (0x1U << SDADC_SYNCBUSY_WINLT_Pos)             /**< (SDADC_SYNCBUSY) WINLT Synchronization Busy Mask */
#define SDADC_SYNCBUSY_WINLT(value)           (SDADC_SYNCBUSY_WINLT_Msk & ((value) << SDADC_SYNCBUSY_WINLT_Pos))
#define SDADC_SYNCBUSY_WINUT_Pos              (6U)                                           /**< (SDADC_SYNCBUSY) WINUT Synchronization Busy Position */
#define SDADC_SYNCBUSY_WINUT_Msk              (0x1U << SDADC_SYNCBUSY_WINUT_Pos)             /**< (SDADC_SYNCBUSY) WINUT Synchronization Busy Mask */
#define SDADC_SYNCBUSY_WINUT(value)           (SDADC_SYNCBUSY_WINUT_Msk & ((value) << SDADC_SYNCBUSY_WINUT_Pos))
#define SDADC_SYNCBUSY_OFFSETCORR_Pos         (7U)                                           /**< (SDADC_SYNCBUSY) OFFSETCTRL Synchronization Busy Position */
#define SDADC_SYNCBUSY_OFFSETCORR_Msk         (0x1U << SDADC_SYNCBUSY_OFFSETCORR_Pos)        /**< (SDADC_SYNCBUSY) OFFSETCTRL Synchronization Busy Mask */
#define SDADC_SYNCBUSY_OFFSETCORR(value)      (SDADC_SYNCBUSY_OFFSETCORR_Msk & ((value) << SDADC_SYNCBUSY_OFFSETCORR_Pos))
#define SDADC_SYNCBUSY_GAINCORR_Pos           (8U)                                           /**< (SDADC_SYNCBUSY) GAINCORR Synchronization Busy Position */
#define SDADC_SYNCBUSY_GAINCORR_Msk           (0x1U << SDADC_SYNCBUSY_GAINCORR_Pos)          /**< (SDADC_SYNCBUSY) GAINCORR Synchronization Busy Mask */
#define SDADC_SYNCBUSY_GAINCORR(value)        (SDADC_SYNCBUSY_GAINCORR_Msk & ((value) << SDADC_SYNCBUSY_GAINCORR_Pos))
#define SDADC_SYNCBUSY_SHIFTCORR_Pos          (9U)                                           /**< (SDADC_SYNCBUSY) SHIFTCORR Synchronization Busy Position */
#define SDADC_SYNCBUSY_SHIFTCORR_Msk          (0x1U << SDADC_SYNCBUSY_SHIFTCORR_Pos)         /**< (SDADC_SYNCBUSY) SHIFTCORR Synchronization Busy Mask */
#define SDADC_SYNCBUSY_SHIFTCORR(value)       (SDADC_SYNCBUSY_SHIFTCORR_Msk & ((value) << SDADC_SYNCBUSY_SHIFTCORR_Pos))
#define SDADC_SYNCBUSY_SWTRIG_Pos             (10U)                                          /**< (SDADC_SYNCBUSY) SWTRG Synchronization Busy Position */
#define SDADC_SYNCBUSY_SWTRIG_Msk             (0x1U << SDADC_SYNCBUSY_SWTRIG_Pos)            /**< (SDADC_SYNCBUSY) SWTRG Synchronization Busy Mask */
#define SDADC_SYNCBUSY_SWTRIG(value)          (SDADC_SYNCBUSY_SWTRIG_Msk & ((value) << SDADC_SYNCBUSY_SWTRIG_Pos))
#define SDADC_SYNCBUSY_ANACTRL_Pos            (11U)                                          /**< (SDADC_SYNCBUSY) ANACTRL Synchronization Busy Position */
#define SDADC_SYNCBUSY_ANACTRL_Msk            (0x1U << SDADC_SYNCBUSY_ANACTRL_Pos)           /**< (SDADC_SYNCBUSY) ANACTRL Synchronization Busy Mask */
#define SDADC_SYNCBUSY_ANACTRL(value)         (SDADC_SYNCBUSY_ANACTRL_Msk & ((value) << SDADC_SYNCBUSY_ANACTRL_Pos))
#define SDADC_SYNCBUSY_Msk                    (0x00000FFFUL)                                 /**< (SDADC_SYNCBUSY) Register Mask  */

/* -------- SDADC_RESULT : (SDADC Offset: 0x24) (R/  32) Result -------- */
#define SDADC_RESULT_RESULT_Pos               (0U)                                           /**< (SDADC_RESULT) Result Value Position */
#define SDADC_RESULT_RESULT_Msk               (0xFFFFFFU << SDADC_RESULT_RESULT_Pos)         /**< (SDADC_RESULT) Result Value Mask */
#define SDADC_RESULT_RESULT(value)            (SDADC_RESULT_RESULT_Msk & ((value) << SDADC_RESULT_RESULT_Pos))
#define SDADC_RESULT_RESERVED_Pos             (24U)                                          /**< (SDADC_RESULT) Reserved Position */
#define SDADC_RESULT_RESERVED_Msk             (0xFFU << SDADC_RESULT_RESERVED_Pos)           /**< (SDADC_RESULT) Reserved Mask */
#define SDADC_RESULT_RESERVED(value)          (SDADC_RESULT_RESERVED_Msk & ((value) << SDADC_RESULT_RESERVED_Pos))
#define SDADC_RESULT_Msk                      (0xFFFFFFFFUL)                                 /**< (SDADC_RESULT) Register Mask  */

/* -------- SDADC_SEQCTRL : (SDADC Offset: 0x28) (R/W 8) Sequence Control -------- */
#define SDADC_SEQCTRL_SEQEN_Pos               (0U)                                           /**< (SDADC_SEQCTRL) Enable Positive Input in the Sequence Position */
#define SDADC_SEQCTRL_SEQEN_Msk               (0x7U << SDADC_SEQCTRL_SEQEN_Pos)              /**< (SDADC_SEQCTRL) Enable Positive Input in the Sequence Mask */
#define SDADC_SEQCTRL_SEQEN(value)            (SDADC_SEQCTRL_SEQEN_Msk & ((value) << SDADC_SEQCTRL_SEQEN_Pos))
#define SDADC_SEQCTRL_Msk                     (0x00000007UL)                                 /**< (SDADC_SEQCTRL) Register Mask  */

/* -------- SDADC_ANACTRL : (SDADC Offset: 0x2C) (R/W 8) Analog Control -------- */
#define SDADC_ANACTRL_CTRSDADC_Pos            (0U)                                           /**< (SDADC_ANACTRL) SDADC Control Position */
#define SDADC_ANACTRL_CTRSDADC_Msk            (0x3FU << SDADC_ANACTRL_CTRSDADC_Pos)          /**< (SDADC_ANACTRL) SDADC Control Mask */
#define SDADC_ANACTRL_CTRSDADC(value)         (SDADC_ANACTRL_CTRSDADC_Msk & ((value) << SDADC_ANACTRL_CTRSDADC_Pos))
#define SDADC_ANACTRL_ONCHOP_Pos              (6U)                                           /**< (SDADC_ANACTRL) Chopper Position */
#define SDADC_ANACTRL_ONCHOP_Msk              (0x1U << SDADC_ANACTRL_ONCHOP_Pos)             /**< (SDADC_ANACTRL) Chopper Mask */
#define SDADC_ANACTRL_ONCHOP(value)           (SDADC_ANACTRL_ONCHOP_Msk & ((value) << SDADC_ANACTRL_ONCHOP_Pos))
#define SDADC_ANACTRL_BUFTEST_Pos             (7U)                                           /**< (SDADC_ANACTRL) BUFTEST Position */
#define SDADC_ANACTRL_BUFTEST_Msk             (0x1U << SDADC_ANACTRL_BUFTEST_Pos)            /**< (SDADC_ANACTRL) BUFTEST Mask */
#define SDADC_ANACTRL_BUFTEST(value)          (SDADC_ANACTRL_BUFTEST_Msk & ((value) << SDADC_ANACTRL_BUFTEST_Pos))
#define SDADC_ANACTRL_Msk                     (0x000000FFUL)                                 /**< (SDADC_ANACTRL) Register Mask  */

/* -------- SDADC_DBGCTRL : (SDADC Offset: 0x2E) (R/W 8) Debug Control -------- */
#define SDADC_DBGCTRL_DBGRUN_Pos              (0U)                                           /**< (SDADC_DBGCTRL) Debug Run Position */
#define SDADC_DBGCTRL_DBGRUN_Msk              (0x1U << SDADC_DBGCTRL_DBGRUN_Pos)             /**< (SDADC_DBGCTRL) Debug Run Mask */
#define SDADC_DBGCTRL_DBGRUN(value)           (SDADC_DBGCTRL_DBGRUN_Msk & ((value) << SDADC_DBGCTRL_DBGRUN_Pos))
#define SDADC_DBGCTRL_Msk                     (0x00000001UL)                                 /**< (SDADC_DBGCTRL) Register Mask  */

/** \brief SDADC register offsets definitions */
#define SDADC_CTRLA_OFFSET             (0x00)         /**< (SDADC_CTRLA) Control A Offset */
#define SDADC_REFCTRL_OFFSET           (0x01)         /**< (SDADC_REFCTRL) Reference Control Offset */
#define SDADC_CTRLB_OFFSET             (0x02)         /**< (SDADC_CTRLB) Control B Offset */
#define SDADC_EVCTRL_OFFSET            (0x04)         /**< (SDADC_EVCTRL) Event Control Offset */
#define SDADC_INTENCLR_OFFSET          (0x05)         /**< (SDADC_INTENCLR) Interrupt Enable Clear Offset */
#define SDADC_INTENSET_OFFSET          (0x06)         /**< (SDADC_INTENSET) Interrupt Enable Set Offset */
#define SDADC_INTFLAG_OFFSET           (0x07)         /**< (SDADC_INTFLAG) Interrupt Flag Status and Clear Offset */
#define SDADC_SEQSTATUS_OFFSET         (0x08)         /**< (SDADC_SEQSTATUS) Sequence Status Offset */
#define SDADC_INPUTCTRL_OFFSET         (0x09)         /**< (SDADC_INPUTCTRL) Input Control Offset */
#define SDADC_CTRLC_OFFSET             (0x0A)         /**< (SDADC_CTRLC) Control C Offset */
#define SDADC_WINCTRL_OFFSET           (0x0B)         /**< (SDADC_WINCTRL) Window Monitor Control Offset */
#define SDADC_WINLT_OFFSET             (0x0C)         /**< (SDADC_WINLT) Window Monitor Lower Threshold Offset */
#define SDADC_WINUT_OFFSET             (0x10)         /**< (SDADC_WINUT) Window Monitor Upper Threshold Offset */
#define SDADC_OFFSETCORR_OFFSET        (0x14)         /**< (SDADC_OFFSETCORR) Offset Correction Offset */
#define SDADC_GAINCORR_OFFSET          (0x18)         /**< (SDADC_GAINCORR) Gain Correction Offset */
#define SDADC_SHIFTCORR_OFFSET         (0x1A)         /**< (SDADC_SHIFTCORR) Shift Correction Offset */
#define SDADC_SWTRIG_OFFSET            (0x1C)         /**< (SDADC_SWTRIG) Software Trigger Offset */
#define SDADC_SYNCBUSY_OFFSET          (0x20)         /**< (SDADC_SYNCBUSY) Synchronization Busy Offset */
#define SDADC_RESULT_OFFSET            (0x24)         /**< (SDADC_RESULT) Result Offset */
#define SDADC_SEQCTRL_OFFSET           (0x28)         /**< (SDADC_SEQCTRL) Sequence Control Offset */
#define SDADC_ANACTRL_OFFSET           (0x2C)         /**< (SDADC_ANACTRL) Analog Control Offset */
#define SDADC_DBGCTRL_OFFSET           (0x2E)         /**< (SDADC_DBGCTRL) Debug Control Offset */

/** \brief SDADC register API structure */
typedef struct
{
  __IO  uint8_t                        SDADC_CTRLA;     /**< Offset: 0x00 (R/W  8) Control A */
  __IO  uint8_t                        SDADC_REFCTRL;   /**< Offset: 0x01 (R/W  8) Reference Control */
  __IO  uint16_t                       SDADC_CTRLB;     /**< Offset: 0x02 (R/W  16) Control B */
  __IO  uint8_t                        SDADC_EVCTRL;    /**< Offset: 0x04 (R/W  8) Event Control */
  __IO  uint8_t                        SDADC_INTENCLR;  /**< Offset: 0x05 (R/W  8) Interrupt Enable Clear */
  __IO  uint8_t                        SDADC_INTENSET;  /**< Offset: 0x06 (R/W  8) Interrupt Enable Set */
  __IO  uint8_t                        SDADC_INTFLAG;   /**< Offset: 0x07 (R/W  8) Interrupt Flag Status and Clear */
  __I   uint8_t                        SDADC_SEQSTATUS; /**< Offset: 0x08 (R/   8) Sequence Status */
  __IO  uint8_t                        SDADC_INPUTCTRL; /**< Offset: 0x09 (R/W  8) Input Control */
  __IO  uint8_t                        SDADC_CTRLC;     /**< Offset: 0x0a (R/W  8) Control C */
  __IO  uint8_t                        SDADC_WINCTRL;   /**< Offset: 0x0b (R/W  8) Window Monitor Control */
  __IO  uint32_t                       SDADC_WINLT;     /**< Offset: 0x0c (R/W  32) Window Monitor Lower Threshold */
  __IO  uint32_t                       SDADC_WINUT;     /**< Offset: 0x10 (R/W  32) Window Monitor Upper Threshold */
  __IO  uint32_t                       SDADC_OFFSETCORR; /**< Offset: 0x14 (R/W  32) Offset Correction */
  __IO  uint16_t                       SDADC_GAINCORR;  /**< Offset: 0x18 (R/W  16) Gain Correction */
  __IO  uint8_t                        SDADC_SHIFTCORR; /**< Offset: 0x1a (R/W  8) Shift Correction */
  __I   uint8_t                        Reserved1[0x01];
  __IO  uint8_t                        SDADC_SWTRIG;    /**< Offset: 0x1c (R/W  8) Software Trigger */
  __I   uint8_t                        Reserved2[0x03];
  __I   uint32_t                       SDADC_SYNCBUSY;  /**< Offset: 0x20 (R/   32) Synchronization Busy */
  __I   uint32_t                       SDADC_RESULT;    /**< Offset: 0x24 (R/   32) Result */
  __IO  uint8_t                        SDADC_SEQCTRL;   /**< Offset: 0x28 (R/W  8) Sequence Control */
  __I   uint8_t                        Reserved3[0x03];
  __IO  uint8_t                        SDADC_ANACTRL;   /**< Offset: 0x2c (R/W  8) Analog Control */
  __I   uint8_t                        Reserved4[0x01];
  __IO  uint8_t                        SDADC_DBGCTRL;   /**< Offset: 0x2e (R/W  8) Debug Control */
} sdadc_registers_t;
/** @}  end of Sigma-Delta Analog Digital Converter */

#endif /* SAMC_SAMC21_SDADC_MODULE_H */

