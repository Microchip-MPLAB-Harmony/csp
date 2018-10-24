/**
 * \brief Header file for SAMC/SAMC21 ADC
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
#ifndef SAMC_SAMC21_ADC_MODULE_H
#define SAMC_SAMC21_ADC_MODULE_H

/** \addtogroup SAMC_SAMC21 Analog Digital Converter
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_ADC                                   */
/* ========================================================================== */

/* -------- ADC_CTRLA : (ADC Offset: 0x00) (R/W 8) Control A -------- */
#define ADC_CTRLA_SWRST_Pos                   (0U)                                           /**< (ADC_CTRLA) Software Reset Position */
#define ADC_CTRLA_SWRST_Msk                   (0x1U << ADC_CTRLA_SWRST_Pos)                  /**< (ADC_CTRLA) Software Reset Mask */
#define ADC_CTRLA_SWRST(value)                (ADC_CTRLA_SWRST_Msk & ((value) << ADC_CTRLA_SWRST_Pos))
#define ADC_CTRLA_ENABLE_Pos                  (1U)                                           /**< (ADC_CTRLA) Enable Position */
#define ADC_CTRLA_ENABLE_Msk                  (0x1U << ADC_CTRLA_ENABLE_Pos)                 /**< (ADC_CTRLA) Enable Mask */
#define ADC_CTRLA_ENABLE(value)               (ADC_CTRLA_ENABLE_Msk & ((value) << ADC_CTRLA_ENABLE_Pos))
#define ADC_CTRLA_SLAVEEN_Pos                 (5U)                                           /**< (ADC_CTRLA) Slave Enable Position */
#define ADC_CTRLA_SLAVEEN_Msk                 (0x1U << ADC_CTRLA_SLAVEEN_Pos)                /**< (ADC_CTRLA) Slave Enable Mask */
#define ADC_CTRLA_SLAVEEN(value)              (ADC_CTRLA_SLAVEEN_Msk & ((value) << ADC_CTRLA_SLAVEEN_Pos))
#define ADC_CTRLA_RUNSTDBY_Pos                (6U)                                           /**< (ADC_CTRLA) Run During Standby Position */
#define ADC_CTRLA_RUNSTDBY_Msk                (0x1U << ADC_CTRLA_RUNSTDBY_Pos)               /**< (ADC_CTRLA) Run During Standby Mask */
#define ADC_CTRLA_RUNSTDBY(value)             (ADC_CTRLA_RUNSTDBY_Msk & ((value) << ADC_CTRLA_RUNSTDBY_Pos))
#define ADC_CTRLA_ONDEMAND_Pos                (7U)                                           /**< (ADC_CTRLA) On Demand Control Position */
#define ADC_CTRLA_ONDEMAND_Msk                (0x1U << ADC_CTRLA_ONDEMAND_Pos)               /**< (ADC_CTRLA) On Demand Control Mask */
#define ADC_CTRLA_ONDEMAND(value)             (ADC_CTRLA_ONDEMAND_Msk & ((value) << ADC_CTRLA_ONDEMAND_Pos))
#define ADC_CTRLA_Msk                         (0x000000E3UL)                                 /**< (ADC_CTRLA) Register Mask  */

/* -------- ADC_CTRLB : (ADC Offset: 0x01) (R/W 8) Control B -------- */
#define ADC_CTRLB_PRESCALER_Pos               (0U)                                           /**< (ADC_CTRLB) Prescaler Configuration Position */
#define ADC_CTRLB_PRESCALER_Msk               (0x7U << ADC_CTRLB_PRESCALER_Pos)              /**< (ADC_CTRLB) Prescaler Configuration Mask */
#define ADC_CTRLB_PRESCALER(value)            (ADC_CTRLB_PRESCALER_Msk & ((value) << ADC_CTRLB_PRESCALER_Pos))
#define   ADC_CTRLB_PRESCALER_DIV2_Val        (0U)                                           /**< (ADC_CTRLB) Peripheral clock divided by 2  */
#define   ADC_CTRLB_PRESCALER_DIV4_Val        (1U)                                           /**< (ADC_CTRLB) Peripheral clock divided by 4  */
#define   ADC_CTRLB_PRESCALER_DIV8_Val        (2U)                                           /**< (ADC_CTRLB) Peripheral clock divided by 8  */
#define   ADC_CTRLB_PRESCALER_DIV16_Val       (3U)                                           /**< (ADC_CTRLB) Peripheral clock divided by 16  */
#define   ADC_CTRLB_PRESCALER_DIV32_Val       (4U)                                           /**< (ADC_CTRLB) Peripheral clock divided by 32  */
#define   ADC_CTRLB_PRESCALER_DIV64_Val       (5U)                                           /**< (ADC_CTRLB) Peripheral clock divided by 64  */
#define   ADC_CTRLB_PRESCALER_DIV128_Val      (6U)                                           /**< (ADC_CTRLB) Peripheral clock divided by 128  */
#define   ADC_CTRLB_PRESCALER_DIV256_Val      (7U)                                           /**< (ADC_CTRLB) Peripheral clock divided by 256  */
#define ADC_CTRLB_PRESCALER_DIV2              (ADC_CTRLB_PRESCALER_DIV2_Val << ADC_CTRLB_PRESCALER_Pos) /**< (ADC_CTRLB) Peripheral clock divided by 2 Position  */
#define ADC_CTRLB_PRESCALER_DIV4              (ADC_CTRLB_PRESCALER_DIV4_Val << ADC_CTRLB_PRESCALER_Pos) /**< (ADC_CTRLB) Peripheral clock divided by 4 Position  */
#define ADC_CTRLB_PRESCALER_DIV8              (ADC_CTRLB_PRESCALER_DIV8_Val << ADC_CTRLB_PRESCALER_Pos) /**< (ADC_CTRLB) Peripheral clock divided by 8 Position  */
#define ADC_CTRLB_PRESCALER_DIV16             (ADC_CTRLB_PRESCALER_DIV16_Val << ADC_CTRLB_PRESCALER_Pos) /**< (ADC_CTRLB) Peripheral clock divided by 16 Position  */
#define ADC_CTRLB_PRESCALER_DIV32             (ADC_CTRLB_PRESCALER_DIV32_Val << ADC_CTRLB_PRESCALER_Pos) /**< (ADC_CTRLB) Peripheral clock divided by 32 Position  */
#define ADC_CTRLB_PRESCALER_DIV64             (ADC_CTRLB_PRESCALER_DIV64_Val << ADC_CTRLB_PRESCALER_Pos) /**< (ADC_CTRLB) Peripheral clock divided by 64 Position  */
#define ADC_CTRLB_PRESCALER_DIV128            (ADC_CTRLB_PRESCALER_DIV128_Val << ADC_CTRLB_PRESCALER_Pos) /**< (ADC_CTRLB) Peripheral clock divided by 128 Position  */
#define ADC_CTRLB_PRESCALER_DIV256            (ADC_CTRLB_PRESCALER_DIV256_Val << ADC_CTRLB_PRESCALER_Pos) /**< (ADC_CTRLB) Peripheral clock divided by 256 Position  */
#define ADC_CTRLB_Msk                         (0x00000007UL)                                 /**< (ADC_CTRLB) Register Mask  */

/* -------- ADC_REFCTRL : (ADC Offset: 0x02) (R/W 8) Reference Control -------- */
#define ADC_REFCTRL_REFSEL_Pos                (0U)                                           /**< (ADC_REFCTRL) Reference Selection Position */
#define ADC_REFCTRL_REFSEL_Msk                (0xFU << ADC_REFCTRL_REFSEL_Pos)               /**< (ADC_REFCTRL) Reference Selection Mask */
#define ADC_REFCTRL_REFSEL(value)             (ADC_REFCTRL_REFSEL_Msk & ((value) << ADC_REFCTRL_REFSEL_Pos))
#define   ADC_REFCTRL_REFSEL_INTREF_Val       (0U)                                           /**< (ADC_REFCTRL) Internal Bandgap Reference  */
#define   ADC_REFCTRL_REFSEL_INTVCC0_Val      (1U)                                           /**< (ADC_REFCTRL) 1/1.6 VDDANA  */
#define   ADC_REFCTRL_REFSEL_INTVCC1_Val      (2U)                                           /**< (ADC_REFCTRL) 1/2 VDDANA  */
#define   ADC_REFCTRL_REFSEL_AREFA_Val        (3U)                                           /**< (ADC_REFCTRL) External Reference  */
#define   ADC_REFCTRL_REFSEL_DAC_Val          (4U)                                           /**< (ADC_REFCTRL) DAC  */
#define   ADC_REFCTRL_REFSEL_INTVCC2_Val      (5U)                                           /**< (ADC_REFCTRL) VDDANA  */
#define ADC_REFCTRL_REFSEL_INTREF             (ADC_REFCTRL_REFSEL_INTREF_Val << ADC_REFCTRL_REFSEL_Pos) /**< (ADC_REFCTRL) Internal Bandgap Reference Position  */
#define ADC_REFCTRL_REFSEL_INTVCC0            (ADC_REFCTRL_REFSEL_INTVCC0_Val << ADC_REFCTRL_REFSEL_Pos) /**< (ADC_REFCTRL) 1/1.6 VDDANA Position  */
#define ADC_REFCTRL_REFSEL_INTVCC1            (ADC_REFCTRL_REFSEL_INTVCC1_Val << ADC_REFCTRL_REFSEL_Pos) /**< (ADC_REFCTRL) 1/2 VDDANA Position  */
#define ADC_REFCTRL_REFSEL_AREFA              (ADC_REFCTRL_REFSEL_AREFA_Val << ADC_REFCTRL_REFSEL_Pos) /**< (ADC_REFCTRL) External Reference Position  */
#define ADC_REFCTRL_REFSEL_DAC                (ADC_REFCTRL_REFSEL_DAC_Val << ADC_REFCTRL_REFSEL_Pos) /**< (ADC_REFCTRL) DAC Position  */
#define ADC_REFCTRL_REFSEL_INTVCC2            (ADC_REFCTRL_REFSEL_INTVCC2_Val << ADC_REFCTRL_REFSEL_Pos) /**< (ADC_REFCTRL) VDDANA Position  */
#define ADC_REFCTRL_REFCOMP_Pos               (7U)                                           /**< (ADC_REFCTRL) Reference Buffer Offset Compensation Enable Position */
#define ADC_REFCTRL_REFCOMP_Msk               (0x1U << ADC_REFCTRL_REFCOMP_Pos)              /**< (ADC_REFCTRL) Reference Buffer Offset Compensation Enable Mask */
#define ADC_REFCTRL_REFCOMP(value)            (ADC_REFCTRL_REFCOMP_Msk & ((value) << ADC_REFCTRL_REFCOMP_Pos))
#define ADC_REFCTRL_Msk                       (0x0000008FUL)                                 /**< (ADC_REFCTRL) Register Mask  */

/* -------- ADC_EVCTRL : (ADC Offset: 0x03) (R/W 8) Event Control -------- */
#define ADC_EVCTRL_FLUSHEI_Pos                (0U)                                           /**< (ADC_EVCTRL) Flush Event Input Enable Position */
#define ADC_EVCTRL_FLUSHEI_Msk                (0x1U << ADC_EVCTRL_FLUSHEI_Pos)               /**< (ADC_EVCTRL) Flush Event Input Enable Mask */
#define ADC_EVCTRL_FLUSHEI(value)             (ADC_EVCTRL_FLUSHEI_Msk & ((value) << ADC_EVCTRL_FLUSHEI_Pos))
#define ADC_EVCTRL_STARTEI_Pos                (1U)                                           /**< (ADC_EVCTRL) Start Conversion Event Input Enable Position */
#define ADC_EVCTRL_STARTEI_Msk                (0x1U << ADC_EVCTRL_STARTEI_Pos)               /**< (ADC_EVCTRL) Start Conversion Event Input Enable Mask */
#define ADC_EVCTRL_STARTEI(value)             (ADC_EVCTRL_STARTEI_Msk & ((value) << ADC_EVCTRL_STARTEI_Pos))
#define ADC_EVCTRL_FLUSHINV_Pos               (2U)                                           /**< (ADC_EVCTRL) Flush Event Invert Enable Position */
#define ADC_EVCTRL_FLUSHINV_Msk               (0x1U << ADC_EVCTRL_FLUSHINV_Pos)              /**< (ADC_EVCTRL) Flush Event Invert Enable Mask */
#define ADC_EVCTRL_FLUSHINV(value)            (ADC_EVCTRL_FLUSHINV_Msk & ((value) << ADC_EVCTRL_FLUSHINV_Pos))
#define ADC_EVCTRL_STARTINV_Pos               (3U)                                           /**< (ADC_EVCTRL) Start Event Invert Enable Position */
#define ADC_EVCTRL_STARTINV_Msk               (0x1U << ADC_EVCTRL_STARTINV_Pos)              /**< (ADC_EVCTRL) Start Event Invert Enable Mask */
#define ADC_EVCTRL_STARTINV(value)            (ADC_EVCTRL_STARTINV_Msk & ((value) << ADC_EVCTRL_STARTINV_Pos))
#define ADC_EVCTRL_RESRDYEO_Pos               (4U)                                           /**< (ADC_EVCTRL) Result Ready Event Out Position */
#define ADC_EVCTRL_RESRDYEO_Msk               (0x1U << ADC_EVCTRL_RESRDYEO_Pos)              /**< (ADC_EVCTRL) Result Ready Event Out Mask */
#define ADC_EVCTRL_RESRDYEO(value)            (ADC_EVCTRL_RESRDYEO_Msk & ((value) << ADC_EVCTRL_RESRDYEO_Pos))
#define ADC_EVCTRL_WINMONEO_Pos               (5U)                                           /**< (ADC_EVCTRL) Window Monitor Event Out Position */
#define ADC_EVCTRL_WINMONEO_Msk               (0x1U << ADC_EVCTRL_WINMONEO_Pos)              /**< (ADC_EVCTRL) Window Monitor Event Out Mask */
#define ADC_EVCTRL_WINMONEO(value)            (ADC_EVCTRL_WINMONEO_Msk & ((value) << ADC_EVCTRL_WINMONEO_Pos))
#define ADC_EVCTRL_Msk                        (0x0000003FUL)                                 /**< (ADC_EVCTRL) Register Mask  */

/* -------- ADC_INTENCLR : (ADC Offset: 0x04) (R/W 8) Interrupt Enable Clear -------- */
#define ADC_INTENCLR_RESRDY_Pos               (0U)                                           /**< (ADC_INTENCLR) Result Ready Interrupt Disable Position */
#define ADC_INTENCLR_RESRDY_Msk               (0x1U << ADC_INTENCLR_RESRDY_Pos)              /**< (ADC_INTENCLR) Result Ready Interrupt Disable Mask */
#define ADC_INTENCLR_RESRDY(value)            (ADC_INTENCLR_RESRDY_Msk & ((value) << ADC_INTENCLR_RESRDY_Pos))
#define ADC_INTENCLR_OVERRUN_Pos              (1U)                                           /**< (ADC_INTENCLR) Overrun Interrupt Disable Position */
#define ADC_INTENCLR_OVERRUN_Msk              (0x1U << ADC_INTENCLR_OVERRUN_Pos)             /**< (ADC_INTENCLR) Overrun Interrupt Disable Mask */
#define ADC_INTENCLR_OVERRUN(value)           (ADC_INTENCLR_OVERRUN_Msk & ((value) << ADC_INTENCLR_OVERRUN_Pos))
#define ADC_INTENCLR_WINMON_Pos               (2U)                                           /**< (ADC_INTENCLR) Window Monitor Interrupt Disable Position */
#define ADC_INTENCLR_WINMON_Msk               (0x1U << ADC_INTENCLR_WINMON_Pos)              /**< (ADC_INTENCLR) Window Monitor Interrupt Disable Mask */
#define ADC_INTENCLR_WINMON(value)            (ADC_INTENCLR_WINMON_Msk & ((value) << ADC_INTENCLR_WINMON_Pos))
#define ADC_INTENCLR_Msk                      (0x00000007UL)                                 /**< (ADC_INTENCLR) Register Mask  */

/* -------- ADC_INTENSET : (ADC Offset: 0x05) (R/W 8) Interrupt Enable Set -------- */
#define ADC_INTENSET_RESRDY_Pos               (0U)                                           /**< (ADC_INTENSET) Result Ready Interrupt Enable Position */
#define ADC_INTENSET_RESRDY_Msk               (0x1U << ADC_INTENSET_RESRDY_Pos)              /**< (ADC_INTENSET) Result Ready Interrupt Enable Mask */
#define ADC_INTENSET_RESRDY(value)            (ADC_INTENSET_RESRDY_Msk & ((value) << ADC_INTENSET_RESRDY_Pos))
#define ADC_INTENSET_OVERRUN_Pos              (1U)                                           /**< (ADC_INTENSET) Overrun Interrupt Enable Position */
#define ADC_INTENSET_OVERRUN_Msk              (0x1U << ADC_INTENSET_OVERRUN_Pos)             /**< (ADC_INTENSET) Overrun Interrupt Enable Mask */
#define ADC_INTENSET_OVERRUN(value)           (ADC_INTENSET_OVERRUN_Msk & ((value) << ADC_INTENSET_OVERRUN_Pos))
#define ADC_INTENSET_WINMON_Pos               (2U)                                           /**< (ADC_INTENSET) Window Monitor Interrupt Enable Position */
#define ADC_INTENSET_WINMON_Msk               (0x1U << ADC_INTENSET_WINMON_Pos)              /**< (ADC_INTENSET) Window Monitor Interrupt Enable Mask */
#define ADC_INTENSET_WINMON(value)            (ADC_INTENSET_WINMON_Msk & ((value) << ADC_INTENSET_WINMON_Pos))
#define ADC_INTENSET_Msk                      (0x00000007UL)                                 /**< (ADC_INTENSET) Register Mask  */

/* -------- ADC_INTFLAG : (ADC Offset: 0x06) (R/W 8) Interrupt Flag Status and Clear -------- */
#define ADC_INTFLAG_RESRDY_Pos                (0U)                                           /**< (ADC_INTFLAG) Result Ready Interrupt Flag Position */
#define ADC_INTFLAG_RESRDY_Msk                (0x1U << ADC_INTFLAG_RESRDY_Pos)               /**< (ADC_INTFLAG) Result Ready Interrupt Flag Mask */
#define ADC_INTFLAG_RESRDY(value)             (ADC_INTFLAG_RESRDY_Msk & ((value) << ADC_INTFLAG_RESRDY_Pos))
#define ADC_INTFLAG_OVERRUN_Pos               (1U)                                           /**< (ADC_INTFLAG) Overrun Interrupt Flag Position */
#define ADC_INTFLAG_OVERRUN_Msk               (0x1U << ADC_INTFLAG_OVERRUN_Pos)              /**< (ADC_INTFLAG) Overrun Interrupt Flag Mask */
#define ADC_INTFLAG_OVERRUN(value)            (ADC_INTFLAG_OVERRUN_Msk & ((value) << ADC_INTFLAG_OVERRUN_Pos))
#define ADC_INTFLAG_WINMON_Pos                (2U)                                           /**< (ADC_INTFLAG) Window Monitor Interrupt Flag Position */
#define ADC_INTFLAG_WINMON_Msk                (0x1U << ADC_INTFLAG_WINMON_Pos)               /**< (ADC_INTFLAG) Window Monitor Interrupt Flag Mask */
#define ADC_INTFLAG_WINMON(value)             (ADC_INTFLAG_WINMON_Msk & ((value) << ADC_INTFLAG_WINMON_Pos))
#define ADC_INTFLAG_Msk                       (0x00000007UL)                                 /**< (ADC_INTFLAG) Register Mask  */

/* -------- ADC_SEQSTATUS : (ADC Offset: 0x07) (R/  8) Sequence Status -------- */
#define ADC_SEQSTATUS_SEQSTATE_Pos            (0U)                                           /**< (ADC_SEQSTATUS) Sequence State Position */
#define ADC_SEQSTATUS_SEQSTATE_Msk            (0x1FU << ADC_SEQSTATUS_SEQSTATE_Pos)          /**< (ADC_SEQSTATUS) Sequence State Mask */
#define ADC_SEQSTATUS_SEQSTATE(value)         (ADC_SEQSTATUS_SEQSTATE_Msk & ((value) << ADC_SEQSTATUS_SEQSTATE_Pos))
#define ADC_SEQSTATUS_SEQBUSY_Pos             (7U)                                           /**< (ADC_SEQSTATUS) Sequence Busy Position */
#define ADC_SEQSTATUS_SEQBUSY_Msk             (0x1U << ADC_SEQSTATUS_SEQBUSY_Pos)            /**< (ADC_SEQSTATUS) Sequence Busy Mask */
#define ADC_SEQSTATUS_SEQBUSY(value)          (ADC_SEQSTATUS_SEQBUSY_Msk & ((value) << ADC_SEQSTATUS_SEQBUSY_Pos))
#define ADC_SEQSTATUS_Msk                     (0x0000009FUL)                                 /**< (ADC_SEQSTATUS) Register Mask  */

/* -------- ADC_INPUTCTRL : (ADC Offset: 0x08) (R/W 16) Input Control -------- */
#define ADC_INPUTCTRL_MUXPOS_Pos              (0U)                                           /**< (ADC_INPUTCTRL) Positive Mux Input Selection Position */
#define ADC_INPUTCTRL_MUXPOS_Msk              (0x1FU << ADC_INPUTCTRL_MUXPOS_Pos)            /**< (ADC_INPUTCTRL) Positive Mux Input Selection Mask */
#define ADC_INPUTCTRL_MUXPOS(value)           (ADC_INPUTCTRL_MUXPOS_Msk & ((value) << ADC_INPUTCTRL_MUXPOS_Pos))
#define   ADC_INPUTCTRL_MUXPOS_AIN0_Val       (0U)                                           /**< (ADC_INPUTCTRL) ADC AIN0 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN1_Val       (1U)                                           /**< (ADC_INPUTCTRL) ADC AIN1 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN2_Val       (2U)                                           /**< (ADC_INPUTCTRL) ADC AIN2 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN3_Val       (3U)                                           /**< (ADC_INPUTCTRL) ADC AIN3 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN4_Val       (4U)                                           /**< (ADC_INPUTCTRL) ADC AIN4 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN5_Val       (5U)                                           /**< (ADC_INPUTCTRL) ADC AIN5 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN6_Val       (6U)                                           /**< (ADC_INPUTCTRL) ADC AIN6 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN7_Val       (7U)                                           /**< (ADC_INPUTCTRL) ADC AIN7 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN8_Val       (8U)                                           /**< (ADC_INPUTCTRL) ADC AIN8 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN9_Val       (9U)                                           /**< (ADC_INPUTCTRL) ADC AIN9 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN10_Val      (10U)                                          /**< (ADC_INPUTCTRL) ADC AIN10 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_AIN11_Val      (11U)                                          /**< (ADC_INPUTCTRL) ADC AIN11 Pin  */
#define   ADC_INPUTCTRL_MUXPOS_TEMP_Val       (24U)                                          /**< (ADC_INPUTCTRL) Temperature Sensor  */
#define   ADC_INPUTCTRL_MUXPOS_BANDGAP_Val    (25U)                                          /**< (ADC_INPUTCTRL) Bandgap Voltage  */
#define   ADC_INPUTCTRL_MUXPOS_SCALEDCOREVCC_Val (26U)                                          /**< (ADC_INPUTCTRL) 1/4 Scaled Core Supply  */
#define   ADC_INPUTCTRL_MUXPOS_SCALEDIOVCC_Val (27U)                                          /**< (ADC_INPUTCTRL) 1/4 Scaled I/O Supply  */
#define   ADC_INPUTCTRL_MUXPOS_DAC_Val        (28U)                                          /**< (ADC_INPUTCTRL) DAC Output  */
#define ADC_INPUTCTRL_MUXPOS_AIN0             (ADC_INPUTCTRL_MUXPOS_AIN0_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN0 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN1             (ADC_INPUTCTRL_MUXPOS_AIN1_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN1 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN2             (ADC_INPUTCTRL_MUXPOS_AIN2_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN2 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN3             (ADC_INPUTCTRL_MUXPOS_AIN3_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN3 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN4             (ADC_INPUTCTRL_MUXPOS_AIN4_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN4 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN5             (ADC_INPUTCTRL_MUXPOS_AIN5_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN5 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN6             (ADC_INPUTCTRL_MUXPOS_AIN6_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN6 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN7             (ADC_INPUTCTRL_MUXPOS_AIN7_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN7 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN8             (ADC_INPUTCTRL_MUXPOS_AIN8_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN8 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN9             (ADC_INPUTCTRL_MUXPOS_AIN9_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN9 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN10            (ADC_INPUTCTRL_MUXPOS_AIN10_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN10 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_AIN11            (ADC_INPUTCTRL_MUXPOS_AIN11_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) ADC AIN11 Pin Position  */
#define ADC_INPUTCTRL_MUXPOS_TEMP             (ADC_INPUTCTRL_MUXPOS_TEMP_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) Temperature Sensor Position  */
#define ADC_INPUTCTRL_MUXPOS_BANDGAP          (ADC_INPUTCTRL_MUXPOS_BANDGAP_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) Bandgap Voltage Position  */
#define ADC_INPUTCTRL_MUXPOS_SCALEDCOREVCC    (ADC_INPUTCTRL_MUXPOS_SCALEDCOREVCC_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) 1/4 Scaled Core Supply Position  */
#define ADC_INPUTCTRL_MUXPOS_SCALEDIOVCC      (ADC_INPUTCTRL_MUXPOS_SCALEDIOVCC_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) 1/4 Scaled I/O Supply Position  */
#define ADC_INPUTCTRL_MUXPOS_DAC              (ADC_INPUTCTRL_MUXPOS_DAC_Val << ADC_INPUTCTRL_MUXPOS_Pos) /**< (ADC_INPUTCTRL) DAC Output Position  */
#define ADC_INPUTCTRL_MUXNEG_Pos              (8U)                                           /**< (ADC_INPUTCTRL) Negative Mux Input Selection Position */
#define ADC_INPUTCTRL_MUXNEG_Msk              (0x1FU << ADC_INPUTCTRL_MUXNEG_Pos)            /**< (ADC_INPUTCTRL) Negative Mux Input Selection Mask */
#define ADC_INPUTCTRL_MUXNEG(value)           (ADC_INPUTCTRL_MUXNEG_Msk & ((value) << ADC_INPUTCTRL_MUXNEG_Pos))
#define   ADC_INPUTCTRL_MUXNEG_AIN0_Val       (0U)                                           /**< (ADC_INPUTCTRL) ADC AIN0 Pin  */
#define   ADC_INPUTCTRL_MUXNEG_AIN1_Val       (1U)                                           /**< (ADC_INPUTCTRL) ADC AIN1 Pin  */
#define   ADC_INPUTCTRL_MUXNEG_AIN2_Val       (2U)                                           /**< (ADC_INPUTCTRL) ADC AIN2 Pin  */
#define   ADC_INPUTCTRL_MUXNEG_AIN3_Val       (3U)                                           /**< (ADC_INPUTCTRL) ADC AIN3 Pin  */
#define   ADC_INPUTCTRL_MUXNEG_AIN4_Val       (4U)                                           /**< (ADC_INPUTCTRL) ADC AIN4 Pin  */
#define   ADC_INPUTCTRL_MUXNEG_AIN5_Val       (5U)                                           /**< (ADC_INPUTCTRL) ADC AIN5 Pin  */
#define   ADC_INPUTCTRL_MUXNEG_GND_Val        (24U)                                          /**< (ADC_INPUTCTRL) Internal Ground  */
#define ADC_INPUTCTRL_MUXNEG_AIN0             (ADC_INPUTCTRL_MUXNEG_AIN0_Val << ADC_INPUTCTRL_MUXNEG_Pos) /**< (ADC_INPUTCTRL) ADC AIN0 Pin Position  */
#define ADC_INPUTCTRL_MUXNEG_AIN1             (ADC_INPUTCTRL_MUXNEG_AIN1_Val << ADC_INPUTCTRL_MUXNEG_Pos) /**< (ADC_INPUTCTRL) ADC AIN1 Pin Position  */
#define ADC_INPUTCTRL_MUXNEG_AIN2             (ADC_INPUTCTRL_MUXNEG_AIN2_Val << ADC_INPUTCTRL_MUXNEG_Pos) /**< (ADC_INPUTCTRL) ADC AIN2 Pin Position  */
#define ADC_INPUTCTRL_MUXNEG_AIN3             (ADC_INPUTCTRL_MUXNEG_AIN3_Val << ADC_INPUTCTRL_MUXNEG_Pos) /**< (ADC_INPUTCTRL) ADC AIN3 Pin Position  */
#define ADC_INPUTCTRL_MUXNEG_AIN4             (ADC_INPUTCTRL_MUXNEG_AIN4_Val << ADC_INPUTCTRL_MUXNEG_Pos) /**< (ADC_INPUTCTRL) ADC AIN4 Pin Position  */
#define ADC_INPUTCTRL_MUXNEG_AIN5             (ADC_INPUTCTRL_MUXNEG_AIN5_Val << ADC_INPUTCTRL_MUXNEG_Pos) /**< (ADC_INPUTCTRL) ADC AIN5 Pin Position  */
#define ADC_INPUTCTRL_MUXNEG_GND              (ADC_INPUTCTRL_MUXNEG_GND_Val << ADC_INPUTCTRL_MUXNEG_Pos) /**< (ADC_INPUTCTRL) Internal Ground Position  */
#define ADC_INPUTCTRL_Msk                     (0x00001F1FUL)                                 /**< (ADC_INPUTCTRL) Register Mask  */

/* -------- ADC_CTRLC : (ADC Offset: 0x0A) (R/W 16) Control C -------- */
#define ADC_CTRLC_DIFFMODE_Pos                (0U)                                           /**< (ADC_CTRLC) Differential Mode Position */
#define ADC_CTRLC_DIFFMODE_Msk                (0x1U << ADC_CTRLC_DIFFMODE_Pos)               /**< (ADC_CTRLC) Differential Mode Mask */
#define ADC_CTRLC_DIFFMODE(value)             (ADC_CTRLC_DIFFMODE_Msk & ((value) << ADC_CTRLC_DIFFMODE_Pos))
#define ADC_CTRLC_LEFTADJ_Pos                 (1U)                                           /**< (ADC_CTRLC) Left-Adjusted Result Position */
#define ADC_CTRLC_LEFTADJ_Msk                 (0x1U << ADC_CTRLC_LEFTADJ_Pos)                /**< (ADC_CTRLC) Left-Adjusted Result Mask */
#define ADC_CTRLC_LEFTADJ(value)              (ADC_CTRLC_LEFTADJ_Msk & ((value) << ADC_CTRLC_LEFTADJ_Pos))
#define ADC_CTRLC_FREERUN_Pos                 (2U)                                           /**< (ADC_CTRLC) Free Running Mode Position */
#define ADC_CTRLC_FREERUN_Msk                 (0x1U << ADC_CTRLC_FREERUN_Pos)                /**< (ADC_CTRLC) Free Running Mode Mask */
#define ADC_CTRLC_FREERUN(value)              (ADC_CTRLC_FREERUN_Msk & ((value) << ADC_CTRLC_FREERUN_Pos))
#define ADC_CTRLC_CORREN_Pos                  (3U)                                           /**< (ADC_CTRLC) Digital Correction Logic Enable Position */
#define ADC_CTRLC_CORREN_Msk                  (0x1U << ADC_CTRLC_CORREN_Pos)                 /**< (ADC_CTRLC) Digital Correction Logic Enable Mask */
#define ADC_CTRLC_CORREN(value)               (ADC_CTRLC_CORREN_Msk & ((value) << ADC_CTRLC_CORREN_Pos))
#define ADC_CTRLC_RESSEL_Pos                  (4U)                                           /**< (ADC_CTRLC) Conversion Result Resolution Position */
#define ADC_CTRLC_RESSEL_Msk                  (0x3U << ADC_CTRLC_RESSEL_Pos)                 /**< (ADC_CTRLC) Conversion Result Resolution Mask */
#define ADC_CTRLC_RESSEL(value)               (ADC_CTRLC_RESSEL_Msk & ((value) << ADC_CTRLC_RESSEL_Pos))
#define   ADC_CTRLC_RESSEL_12BIT_Val          (0U)                                           /**< (ADC_CTRLC) 12-bit result  */
#define   ADC_CTRLC_RESSEL_16BIT_Val          (1U)                                           /**< (ADC_CTRLC) For averaging mode output  */
#define   ADC_CTRLC_RESSEL_10BIT_Val          (2U)                                           /**< (ADC_CTRLC) 10-bit result  */
#define   ADC_CTRLC_RESSEL_8BIT_Val           (3U)                                           /**< (ADC_CTRLC) 8-bit result  */
#define ADC_CTRLC_RESSEL_12BIT                (ADC_CTRLC_RESSEL_12BIT_Val << ADC_CTRLC_RESSEL_Pos) /**< (ADC_CTRLC) 12-bit result Position  */
#define ADC_CTRLC_RESSEL_16BIT                (ADC_CTRLC_RESSEL_16BIT_Val << ADC_CTRLC_RESSEL_Pos) /**< (ADC_CTRLC) For averaging mode output Position  */
#define ADC_CTRLC_RESSEL_10BIT                (ADC_CTRLC_RESSEL_10BIT_Val << ADC_CTRLC_RESSEL_Pos) /**< (ADC_CTRLC) 10-bit result Position  */
#define ADC_CTRLC_RESSEL_8BIT                 (ADC_CTRLC_RESSEL_8BIT_Val << ADC_CTRLC_RESSEL_Pos) /**< (ADC_CTRLC) 8-bit result Position  */
#define ADC_CTRLC_R2R_Pos                     (7U)                                           /**< (ADC_CTRLC) Rail-to-Rail mode enable Position */
#define ADC_CTRLC_R2R_Msk                     (0x1U << ADC_CTRLC_R2R_Pos)                    /**< (ADC_CTRLC) Rail-to-Rail mode enable Mask */
#define ADC_CTRLC_R2R(value)                  (ADC_CTRLC_R2R_Msk & ((value) << ADC_CTRLC_R2R_Pos))
#define ADC_CTRLC_WINMODE_Pos                 (8U)                                           /**< (ADC_CTRLC) Window Monitor Mode Position */
#define ADC_CTRLC_WINMODE_Msk                 (0x7U << ADC_CTRLC_WINMODE_Pos)                /**< (ADC_CTRLC) Window Monitor Mode Mask */
#define ADC_CTRLC_WINMODE(value)              (ADC_CTRLC_WINMODE_Msk & ((value) << ADC_CTRLC_WINMODE_Pos))
#define   ADC_CTRLC_WINMODE_DISABLE_Val       (0U)                                           /**< (ADC_CTRLC) No window mode (default)  */
#define   ADC_CTRLC_WINMODE_MODE1_Val         (1U)                                           /**< (ADC_CTRLC) RESULT > WINLT  */
#define   ADC_CTRLC_WINMODE_MODE2_Val         (2U)                                           /**< (ADC_CTRLC) RESULT < WINUT  */
#define   ADC_CTRLC_WINMODE_MODE3_Val         (3U)                                           /**< (ADC_CTRLC) WINLT < RESULT < WINUT  */
#define   ADC_CTRLC_WINMODE_MODE4_Val         (4U)                                           /**< (ADC_CTRLC) !(WINLT < RESULT < WINUT)  */
#define ADC_CTRLC_WINMODE_DISABLE             (ADC_CTRLC_WINMODE_DISABLE_Val << ADC_CTRLC_WINMODE_Pos) /**< (ADC_CTRLC) No window mode (default) Position  */
#define ADC_CTRLC_WINMODE_MODE1               (ADC_CTRLC_WINMODE_MODE1_Val << ADC_CTRLC_WINMODE_Pos) /**< (ADC_CTRLC) RESULT > WINLT Position  */
#define ADC_CTRLC_WINMODE_MODE2               (ADC_CTRLC_WINMODE_MODE2_Val << ADC_CTRLC_WINMODE_Pos) /**< (ADC_CTRLC) RESULT < WINUT Position  */
#define ADC_CTRLC_WINMODE_MODE3               (ADC_CTRLC_WINMODE_MODE3_Val << ADC_CTRLC_WINMODE_Pos) /**< (ADC_CTRLC) WINLT < RESULT < WINUT Position  */
#define ADC_CTRLC_WINMODE_MODE4               (ADC_CTRLC_WINMODE_MODE4_Val << ADC_CTRLC_WINMODE_Pos) /**< (ADC_CTRLC) !(WINLT < RESULT < WINUT) Position  */
#define ADC_CTRLC_DUALSEL_Pos                 (12U)                                          /**< (ADC_CTRLC) Dual Mode Trigger Selection Position */
#define ADC_CTRLC_DUALSEL_Msk                 (0x3U << ADC_CTRLC_DUALSEL_Pos)                /**< (ADC_CTRLC) Dual Mode Trigger Selection Mask */
#define ADC_CTRLC_DUALSEL(value)              (ADC_CTRLC_DUALSEL_Msk & ((value) << ADC_CTRLC_DUALSEL_Pos))
#define   ADC_CTRLC_DUALSEL_BOTH_Val          (0U)                                           /**< (ADC_CTRLC) Start event or software trigger will start a conversion on both ADCs  */
#define   ADC_CTRLC_DUALSEL_INTERLEAVE_Val    (1U)                                           /**< (ADC_CTRLC) START event or software trigger will alternatingly start a conversion on ADC0 and ADC1  */
#define ADC_CTRLC_DUALSEL_BOTH                (ADC_CTRLC_DUALSEL_BOTH_Val << ADC_CTRLC_DUALSEL_Pos) /**< (ADC_CTRLC) Start event or software trigger will start a conversion on both ADCs Position  */
#define ADC_CTRLC_DUALSEL_INTERLEAVE          (ADC_CTRLC_DUALSEL_INTERLEAVE_Val << ADC_CTRLC_DUALSEL_Pos) /**< (ADC_CTRLC) START event or software trigger will alternatingly start a conversion on ADC0 and ADC1 Position  */
#define ADC_CTRLC_Msk                         (0x000037BFUL)                                 /**< (ADC_CTRLC) Register Mask  */

/* -------- ADC_AVGCTRL : (ADC Offset: 0x0C) (R/W 8) Average Control -------- */
#define ADC_AVGCTRL_SAMPLENUM_Pos             (0U)                                           /**< (ADC_AVGCTRL) Number of Samples to be Collected Position */
#define ADC_AVGCTRL_SAMPLENUM_Msk             (0xFU << ADC_AVGCTRL_SAMPLENUM_Pos)            /**< (ADC_AVGCTRL) Number of Samples to be Collected Mask */
#define ADC_AVGCTRL_SAMPLENUM(value)          (ADC_AVGCTRL_SAMPLENUM_Msk & ((value) << ADC_AVGCTRL_SAMPLENUM_Pos))
#define   ADC_AVGCTRL_SAMPLENUM_1_Val         (0U)                                           /**< (ADC_AVGCTRL) 1 sample  */
#define   ADC_AVGCTRL_SAMPLENUM_2_Val         (1U)                                           /**< (ADC_AVGCTRL) 2 samples  */
#define   ADC_AVGCTRL_SAMPLENUM_4_Val         (2U)                                           /**< (ADC_AVGCTRL) 4 samples  */
#define   ADC_AVGCTRL_SAMPLENUM_8_Val         (3U)                                           /**< (ADC_AVGCTRL) 8 samples  */
#define   ADC_AVGCTRL_SAMPLENUM_16_Val        (4U)                                           /**< (ADC_AVGCTRL) 16 samples  */
#define   ADC_AVGCTRL_SAMPLENUM_32_Val        (5U)                                           /**< (ADC_AVGCTRL) 32 samples  */
#define   ADC_AVGCTRL_SAMPLENUM_64_Val        (6U)                                           /**< (ADC_AVGCTRL) 64 samples  */
#define   ADC_AVGCTRL_SAMPLENUM_128_Val       (7U)                                           /**< (ADC_AVGCTRL) 128 samples  */
#define   ADC_AVGCTRL_SAMPLENUM_256_Val       (8U)                                           /**< (ADC_AVGCTRL) 256 samples  */
#define   ADC_AVGCTRL_SAMPLENUM_512_Val       (9U)                                           /**< (ADC_AVGCTRL) 512 samples  */
#define   ADC_AVGCTRL_SAMPLENUM_1024_Val      (10U)                                          /**< (ADC_AVGCTRL) 1024 samples  */
#define ADC_AVGCTRL_SAMPLENUM_1               (ADC_AVGCTRL_SAMPLENUM_1_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 1 sample Position  */
#define ADC_AVGCTRL_SAMPLENUM_2               (ADC_AVGCTRL_SAMPLENUM_2_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 2 samples Position  */
#define ADC_AVGCTRL_SAMPLENUM_4               (ADC_AVGCTRL_SAMPLENUM_4_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 4 samples Position  */
#define ADC_AVGCTRL_SAMPLENUM_8               (ADC_AVGCTRL_SAMPLENUM_8_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 8 samples Position  */
#define ADC_AVGCTRL_SAMPLENUM_16              (ADC_AVGCTRL_SAMPLENUM_16_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 16 samples Position  */
#define ADC_AVGCTRL_SAMPLENUM_32              (ADC_AVGCTRL_SAMPLENUM_32_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 32 samples Position  */
#define ADC_AVGCTRL_SAMPLENUM_64              (ADC_AVGCTRL_SAMPLENUM_64_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 64 samples Position  */
#define ADC_AVGCTRL_SAMPLENUM_128             (ADC_AVGCTRL_SAMPLENUM_128_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 128 samples Position  */
#define ADC_AVGCTRL_SAMPLENUM_256             (ADC_AVGCTRL_SAMPLENUM_256_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 256 samples Position  */
#define ADC_AVGCTRL_SAMPLENUM_512             (ADC_AVGCTRL_SAMPLENUM_512_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 512 samples Position  */
#define ADC_AVGCTRL_SAMPLENUM_1024            (ADC_AVGCTRL_SAMPLENUM_1024_Val << ADC_AVGCTRL_SAMPLENUM_Pos) /**< (ADC_AVGCTRL) 1024 samples Position  */
#define ADC_AVGCTRL_ADJRES_Pos                (4U)                                           /**< (ADC_AVGCTRL) Adjusting Result / Division Coefficient Position */
#define ADC_AVGCTRL_ADJRES_Msk                (0x7U << ADC_AVGCTRL_ADJRES_Pos)               /**< (ADC_AVGCTRL) Adjusting Result / Division Coefficient Mask */
#define ADC_AVGCTRL_ADJRES(value)             (ADC_AVGCTRL_ADJRES_Msk & ((value) << ADC_AVGCTRL_ADJRES_Pos))
#define ADC_AVGCTRL_Msk                       (0x0000007FUL)                                 /**< (ADC_AVGCTRL) Register Mask  */

/* -------- ADC_SAMPCTRL : (ADC Offset: 0x0D) (R/W 8) Sample Time Control -------- */
#define ADC_SAMPCTRL_SAMPLEN_Pos              (0U)                                           /**< (ADC_SAMPCTRL) Sampling Time Length Position */
#define ADC_SAMPCTRL_SAMPLEN_Msk              (0x3FU << ADC_SAMPCTRL_SAMPLEN_Pos)            /**< (ADC_SAMPCTRL) Sampling Time Length Mask */
#define ADC_SAMPCTRL_SAMPLEN(value)           (ADC_SAMPCTRL_SAMPLEN_Msk & ((value) << ADC_SAMPCTRL_SAMPLEN_Pos))
#define ADC_SAMPCTRL_OFFCOMP_Pos              (7U)                                           /**< (ADC_SAMPCTRL) Comparator Offset Compensation Enable Position */
#define ADC_SAMPCTRL_OFFCOMP_Msk              (0x1U << ADC_SAMPCTRL_OFFCOMP_Pos)             /**< (ADC_SAMPCTRL) Comparator Offset Compensation Enable Mask */
#define ADC_SAMPCTRL_OFFCOMP(value)           (ADC_SAMPCTRL_OFFCOMP_Msk & ((value) << ADC_SAMPCTRL_OFFCOMP_Pos))
#define ADC_SAMPCTRL_Msk                      (0x000000BFUL)                                 /**< (ADC_SAMPCTRL) Register Mask  */

/* -------- ADC_WINLT : (ADC Offset: 0x0E) (R/W 16) Window Monitor Lower Threshold -------- */
#define ADC_WINLT_WINLT_Pos                   (0U)                                           /**< (ADC_WINLT) Window Lower Threshold Position */
#define ADC_WINLT_WINLT_Msk                   (0xFFFFU << ADC_WINLT_WINLT_Pos)               /**< (ADC_WINLT) Window Lower Threshold Mask */
#define ADC_WINLT_WINLT(value)                (ADC_WINLT_WINLT_Msk & ((value) << ADC_WINLT_WINLT_Pos))
#define ADC_WINLT_Msk                         (0x0000FFFFUL)                                 /**< (ADC_WINLT) Register Mask  */

/* -------- ADC_WINUT : (ADC Offset: 0x10) (R/W 16) Window Monitor Upper Threshold -------- */
#define ADC_WINUT_WINUT_Pos                   (0U)                                           /**< (ADC_WINUT) Window Upper Threshold Position */
#define ADC_WINUT_WINUT_Msk                   (0xFFFFU << ADC_WINUT_WINUT_Pos)               /**< (ADC_WINUT) Window Upper Threshold Mask */
#define ADC_WINUT_WINUT(value)                (ADC_WINUT_WINUT_Msk & ((value) << ADC_WINUT_WINUT_Pos))
#define ADC_WINUT_Msk                         (0x0000FFFFUL)                                 /**< (ADC_WINUT) Register Mask  */

/* -------- ADC_GAINCORR : (ADC Offset: 0x12) (R/W 16) Gain Correction -------- */
#define ADC_GAINCORR_GAINCORR_Pos             (0U)                                           /**< (ADC_GAINCORR) Gain Correction Value Position */
#define ADC_GAINCORR_GAINCORR_Msk             (0xFFFU << ADC_GAINCORR_GAINCORR_Pos)          /**< (ADC_GAINCORR) Gain Correction Value Mask */
#define ADC_GAINCORR_GAINCORR(value)          (ADC_GAINCORR_GAINCORR_Msk & ((value) << ADC_GAINCORR_GAINCORR_Pos))
#define ADC_GAINCORR_Msk                      (0x00000FFFUL)                                 /**< (ADC_GAINCORR) Register Mask  */

/* -------- ADC_OFFSETCORR : (ADC Offset: 0x14) (R/W 16) Offset Correction -------- */
#define ADC_OFFSETCORR_OFFSETCORR_Pos         (0U)                                           /**< (ADC_OFFSETCORR) Offset Correction Value Position */
#define ADC_OFFSETCORR_OFFSETCORR_Msk         (0xFFFU << ADC_OFFSETCORR_OFFSETCORR_Pos)      /**< (ADC_OFFSETCORR) Offset Correction Value Mask */
#define ADC_OFFSETCORR_OFFSETCORR(value)      (ADC_OFFSETCORR_OFFSETCORR_Msk & ((value) << ADC_OFFSETCORR_OFFSETCORR_Pos))
#define ADC_OFFSETCORR_Msk                    (0x00000FFFUL)                                 /**< (ADC_OFFSETCORR) Register Mask  */

/* -------- ADC_SWTRIG : (ADC Offset: 0x18) (R/W 8) Software Trigger -------- */
#define ADC_SWTRIG_FLUSH_Pos                  (0U)                                           /**< (ADC_SWTRIG) ADC Flush Position */
#define ADC_SWTRIG_FLUSH_Msk                  (0x1U << ADC_SWTRIG_FLUSH_Pos)                 /**< (ADC_SWTRIG) ADC Flush Mask */
#define ADC_SWTRIG_FLUSH(value)               (ADC_SWTRIG_FLUSH_Msk & ((value) << ADC_SWTRIG_FLUSH_Pos))
#define ADC_SWTRIG_START_Pos                  (1U)                                           /**< (ADC_SWTRIG) Start ADC Conversion Position */
#define ADC_SWTRIG_START_Msk                  (0x1U << ADC_SWTRIG_START_Pos)                 /**< (ADC_SWTRIG) Start ADC Conversion Mask */
#define ADC_SWTRIG_START(value)               (ADC_SWTRIG_START_Msk & ((value) << ADC_SWTRIG_START_Pos))
#define ADC_SWTRIG_Msk                        (0x00000003UL)                                 /**< (ADC_SWTRIG) Register Mask  */

/* -------- ADC_DBGCTRL : (ADC Offset: 0x1C) (R/W 8) Debug Control -------- */
#define ADC_DBGCTRL_DBGRUN_Pos                (0U)                                           /**< (ADC_DBGCTRL) Debug Run Position */
#define ADC_DBGCTRL_DBGRUN_Msk                (0x1U << ADC_DBGCTRL_DBGRUN_Pos)               /**< (ADC_DBGCTRL) Debug Run Mask */
#define ADC_DBGCTRL_DBGRUN(value)             (ADC_DBGCTRL_DBGRUN_Msk & ((value) << ADC_DBGCTRL_DBGRUN_Pos))
#define ADC_DBGCTRL_Msk                       (0x00000001UL)                                 /**< (ADC_DBGCTRL) Register Mask  */

/* -------- ADC_SYNCBUSY : (ADC Offset: 0x20) (R/  16) Synchronization Busy -------- */
#define ADC_SYNCBUSY_SWRST_Pos                (0U)                                           /**< (ADC_SYNCBUSY) SWRST Synchronization Busy Position */
#define ADC_SYNCBUSY_SWRST_Msk                (0x1U << ADC_SYNCBUSY_SWRST_Pos)               /**< (ADC_SYNCBUSY) SWRST Synchronization Busy Mask */
#define ADC_SYNCBUSY_SWRST(value)             (ADC_SYNCBUSY_SWRST_Msk & ((value) << ADC_SYNCBUSY_SWRST_Pos))
#define ADC_SYNCBUSY_ENABLE_Pos               (1U)                                           /**< (ADC_SYNCBUSY) ENABLE Synchronization Busy Position */
#define ADC_SYNCBUSY_ENABLE_Msk               (0x1U << ADC_SYNCBUSY_ENABLE_Pos)              /**< (ADC_SYNCBUSY) ENABLE Synchronization Busy Mask */
#define ADC_SYNCBUSY_ENABLE(value)            (ADC_SYNCBUSY_ENABLE_Msk & ((value) << ADC_SYNCBUSY_ENABLE_Pos))
#define ADC_SYNCBUSY_INPUTCTRL_Pos            (2U)                                           /**< (ADC_SYNCBUSY) INPUTCTRL Synchronization Busy Position */
#define ADC_SYNCBUSY_INPUTCTRL_Msk            (0x1U << ADC_SYNCBUSY_INPUTCTRL_Pos)           /**< (ADC_SYNCBUSY) INPUTCTRL Synchronization Busy Mask */
#define ADC_SYNCBUSY_INPUTCTRL(value)         (ADC_SYNCBUSY_INPUTCTRL_Msk & ((value) << ADC_SYNCBUSY_INPUTCTRL_Pos))
#define ADC_SYNCBUSY_CTRLC_Pos                (3U)                                           /**< (ADC_SYNCBUSY) CTRLC Synchronization Busy Position */
#define ADC_SYNCBUSY_CTRLC_Msk                (0x1U << ADC_SYNCBUSY_CTRLC_Pos)               /**< (ADC_SYNCBUSY) CTRLC Synchronization Busy Mask */
#define ADC_SYNCBUSY_CTRLC(value)             (ADC_SYNCBUSY_CTRLC_Msk & ((value) << ADC_SYNCBUSY_CTRLC_Pos))
#define ADC_SYNCBUSY_AVGCTRL_Pos              (4U)                                           /**< (ADC_SYNCBUSY) AVGCTRL Synchronization Busy Position */
#define ADC_SYNCBUSY_AVGCTRL_Msk              (0x1U << ADC_SYNCBUSY_AVGCTRL_Pos)             /**< (ADC_SYNCBUSY) AVGCTRL Synchronization Busy Mask */
#define ADC_SYNCBUSY_AVGCTRL(value)           (ADC_SYNCBUSY_AVGCTRL_Msk & ((value) << ADC_SYNCBUSY_AVGCTRL_Pos))
#define ADC_SYNCBUSY_SAMPCTRL_Pos             (5U)                                           /**< (ADC_SYNCBUSY) SAMPCTRL Synchronization Busy Position */
#define ADC_SYNCBUSY_SAMPCTRL_Msk             (0x1U << ADC_SYNCBUSY_SAMPCTRL_Pos)            /**< (ADC_SYNCBUSY) SAMPCTRL Synchronization Busy Mask */
#define ADC_SYNCBUSY_SAMPCTRL(value)          (ADC_SYNCBUSY_SAMPCTRL_Msk & ((value) << ADC_SYNCBUSY_SAMPCTRL_Pos))
#define ADC_SYNCBUSY_WINLT_Pos                (6U)                                           /**< (ADC_SYNCBUSY) WINLT Synchronization Busy Position */
#define ADC_SYNCBUSY_WINLT_Msk                (0x1U << ADC_SYNCBUSY_WINLT_Pos)               /**< (ADC_SYNCBUSY) WINLT Synchronization Busy Mask */
#define ADC_SYNCBUSY_WINLT(value)             (ADC_SYNCBUSY_WINLT_Msk & ((value) << ADC_SYNCBUSY_WINLT_Pos))
#define ADC_SYNCBUSY_WINUT_Pos                (7U)                                           /**< (ADC_SYNCBUSY) WINUT Synchronization Busy Position */
#define ADC_SYNCBUSY_WINUT_Msk                (0x1U << ADC_SYNCBUSY_WINUT_Pos)               /**< (ADC_SYNCBUSY) WINUT Synchronization Busy Mask */
#define ADC_SYNCBUSY_WINUT(value)             (ADC_SYNCBUSY_WINUT_Msk & ((value) << ADC_SYNCBUSY_WINUT_Pos))
#define ADC_SYNCBUSY_GAINCORR_Pos             (8U)                                           /**< (ADC_SYNCBUSY) GAINCORR Synchronization Busy Position */
#define ADC_SYNCBUSY_GAINCORR_Msk             (0x1U << ADC_SYNCBUSY_GAINCORR_Pos)            /**< (ADC_SYNCBUSY) GAINCORR Synchronization Busy Mask */
#define ADC_SYNCBUSY_GAINCORR(value)          (ADC_SYNCBUSY_GAINCORR_Msk & ((value) << ADC_SYNCBUSY_GAINCORR_Pos))
#define ADC_SYNCBUSY_OFFSETCORR_Pos           (9U)                                           /**< (ADC_SYNCBUSY) OFFSETCTRL Synchronization Busy Position */
#define ADC_SYNCBUSY_OFFSETCORR_Msk           (0x1U << ADC_SYNCBUSY_OFFSETCORR_Pos)          /**< (ADC_SYNCBUSY) OFFSETCTRL Synchronization Busy Mask */
#define ADC_SYNCBUSY_OFFSETCORR(value)        (ADC_SYNCBUSY_OFFSETCORR_Msk & ((value) << ADC_SYNCBUSY_OFFSETCORR_Pos))
#define ADC_SYNCBUSY_SWTRIG_Pos               (10U)                                          /**< (ADC_SYNCBUSY) SWTRG Synchronization Busy Position */
#define ADC_SYNCBUSY_SWTRIG_Msk               (0x1U << ADC_SYNCBUSY_SWTRIG_Pos)              /**< (ADC_SYNCBUSY) SWTRG Synchronization Busy Mask */
#define ADC_SYNCBUSY_SWTRIG(value)            (ADC_SYNCBUSY_SWTRIG_Msk & ((value) << ADC_SYNCBUSY_SWTRIG_Pos))
#define ADC_SYNCBUSY_Msk                      (0x000007FFUL)                                 /**< (ADC_SYNCBUSY) Register Mask  */

/* -------- ADC_RESULT : (ADC Offset: 0x24) (R/  16) Result -------- */
#define ADC_RESULT_RESULT_Pos                 (0U)                                           /**< (ADC_RESULT) Result Value Position */
#define ADC_RESULT_RESULT_Msk                 (0xFFFFU << ADC_RESULT_RESULT_Pos)             /**< (ADC_RESULT) Result Value Mask */
#define ADC_RESULT_RESULT(value)              (ADC_RESULT_RESULT_Msk & ((value) << ADC_RESULT_RESULT_Pos))
#define ADC_RESULT_Msk                        (0x0000FFFFUL)                                 /**< (ADC_RESULT) Register Mask  */

/* -------- ADC_SEQCTRL : (ADC Offset: 0x28) (R/W 32) Sequence Control -------- */
#define ADC_SEQCTRL_SEQEN_Pos                 (0U)                                           /**< (ADC_SEQCTRL) Enable Positive Input in the Sequence Position */
#define ADC_SEQCTRL_SEQEN_Msk                 (0xFFFFFFFFU << ADC_SEQCTRL_SEQEN_Pos)         /**< (ADC_SEQCTRL) Enable Positive Input in the Sequence Mask */
#define ADC_SEQCTRL_SEQEN(value)              (ADC_SEQCTRL_SEQEN_Msk & ((value) << ADC_SEQCTRL_SEQEN_Pos))
#define ADC_SEQCTRL_Msk                       (0xFFFFFFFFUL)                                 /**< (ADC_SEQCTRL) Register Mask  */

/* -------- ADC_CALIB : (ADC Offset: 0x2C) (R/W 16) Calibration -------- */
#define ADC_CALIB_BIASCOMP_Pos                (0U)                                           /**< (ADC_CALIB) Bias Comparator Scaling Position */
#define ADC_CALIB_BIASCOMP_Msk                (0x7U << ADC_CALIB_BIASCOMP_Pos)               /**< (ADC_CALIB) Bias Comparator Scaling Mask */
#define ADC_CALIB_BIASCOMP(value)             (ADC_CALIB_BIASCOMP_Msk & ((value) << ADC_CALIB_BIASCOMP_Pos))
#define ADC_CALIB_BIASREFBUF_Pos              (8U)                                           /**< (ADC_CALIB) Bias  Reference Buffer Scaling Position */
#define ADC_CALIB_BIASREFBUF_Msk              (0x7U << ADC_CALIB_BIASREFBUF_Pos)             /**< (ADC_CALIB) Bias  Reference Buffer Scaling Mask */
#define ADC_CALIB_BIASREFBUF(value)           (ADC_CALIB_BIASREFBUF_Msk & ((value) << ADC_CALIB_BIASREFBUF_Pos))
#define ADC_CALIB_Msk                         (0x00000707UL)                                 /**< (ADC_CALIB) Register Mask  */

/** \brief ADC register offsets definitions */
#define ADC_CTRLA_OFFSET               (0x00)         /**< (ADC_CTRLA) Control A Offset */
#define ADC_CTRLB_OFFSET               (0x01)         /**< (ADC_CTRLB) Control B Offset */
#define ADC_REFCTRL_OFFSET             (0x02)         /**< (ADC_REFCTRL) Reference Control Offset */
#define ADC_EVCTRL_OFFSET              (0x03)         /**< (ADC_EVCTRL) Event Control Offset */
#define ADC_INTENCLR_OFFSET            (0x04)         /**< (ADC_INTENCLR) Interrupt Enable Clear Offset */
#define ADC_INTENSET_OFFSET            (0x05)         /**< (ADC_INTENSET) Interrupt Enable Set Offset */
#define ADC_INTFLAG_OFFSET             (0x06)         /**< (ADC_INTFLAG) Interrupt Flag Status and Clear Offset */
#define ADC_SEQSTATUS_OFFSET           (0x07)         /**< (ADC_SEQSTATUS) Sequence Status Offset */
#define ADC_INPUTCTRL_OFFSET           (0x08)         /**< (ADC_INPUTCTRL) Input Control Offset */
#define ADC_CTRLC_OFFSET               (0x0A)         /**< (ADC_CTRLC) Control C Offset */
#define ADC_AVGCTRL_OFFSET             (0x0C)         /**< (ADC_AVGCTRL) Average Control Offset */
#define ADC_SAMPCTRL_OFFSET            (0x0D)         /**< (ADC_SAMPCTRL) Sample Time Control Offset */
#define ADC_WINLT_OFFSET               (0x0E)         /**< (ADC_WINLT) Window Monitor Lower Threshold Offset */
#define ADC_WINUT_OFFSET               (0x10)         /**< (ADC_WINUT) Window Monitor Upper Threshold Offset */
#define ADC_GAINCORR_OFFSET            (0x12)         /**< (ADC_GAINCORR) Gain Correction Offset */
#define ADC_OFFSETCORR_OFFSET          (0x14)         /**< (ADC_OFFSETCORR) Offset Correction Offset */
#define ADC_SWTRIG_OFFSET              (0x18)         /**< (ADC_SWTRIG) Software Trigger Offset */
#define ADC_DBGCTRL_OFFSET             (0x1C)         /**< (ADC_DBGCTRL) Debug Control Offset */
#define ADC_SYNCBUSY_OFFSET            (0x20)         /**< (ADC_SYNCBUSY) Synchronization Busy Offset */
#define ADC_RESULT_OFFSET              (0x24)         /**< (ADC_RESULT) Result Offset */
#define ADC_SEQCTRL_OFFSET             (0x28)         /**< (ADC_SEQCTRL) Sequence Control Offset */
#define ADC_CALIB_OFFSET               (0x2C)         /**< (ADC_CALIB) Calibration Offset */

/** \brief ADC register API structure */
typedef struct
{
  __IO  uint8_t                        ADC_CTRLA;       /**< Offset: 0x00 (R/W  8) Control A */
  __IO  uint8_t                        ADC_CTRLB;       /**< Offset: 0x01 (R/W  8) Control B */
  __IO  uint8_t                        ADC_REFCTRL;     /**< Offset: 0x02 (R/W  8) Reference Control */
  __IO  uint8_t                        ADC_EVCTRL;      /**< Offset: 0x03 (R/W  8) Event Control */
  __IO  uint8_t                        ADC_INTENCLR;    /**< Offset: 0x04 (R/W  8) Interrupt Enable Clear */
  __IO  uint8_t                        ADC_INTENSET;    /**< Offset: 0x05 (R/W  8) Interrupt Enable Set */
  __IO  uint8_t                        ADC_INTFLAG;     /**< Offset: 0x06 (R/W  8) Interrupt Flag Status and Clear */
  __I   uint8_t                        ADC_SEQSTATUS;   /**< Offset: 0x07 (R/   8) Sequence Status */
  __IO  uint16_t                       ADC_INPUTCTRL;   /**< Offset: 0x08 (R/W  16) Input Control */
  __IO  uint16_t                       ADC_CTRLC;       /**< Offset: 0x0a (R/W  16) Control C */
  __IO  uint8_t                        ADC_AVGCTRL;     /**< Offset: 0x0c (R/W  8) Average Control */
  __IO  uint8_t                        ADC_SAMPCTRL;    /**< Offset: 0x0d (R/W  8) Sample Time Control */
  __IO  uint16_t                       ADC_WINLT;       /**< Offset: 0x0e (R/W  16) Window Monitor Lower Threshold */
  __IO  uint16_t                       ADC_WINUT;       /**< Offset: 0x10 (R/W  16) Window Monitor Upper Threshold */
  __IO  uint16_t                       ADC_GAINCORR;    /**< Offset: 0x12 (R/W  16) Gain Correction */
  __IO  uint16_t                       ADC_OFFSETCORR;  /**< Offset: 0x14 (R/W  16) Offset Correction */
  __I   uint8_t                        Reserved1[0x02];
  __IO  uint8_t                        ADC_SWTRIG;      /**< Offset: 0x18 (R/W  8) Software Trigger */
  __I   uint8_t                        Reserved2[0x03];
  __IO  uint8_t                        ADC_DBGCTRL;     /**< Offset: 0x1c (R/W  8) Debug Control */
  __I   uint8_t                        Reserved3[0x03];
  __I   uint16_t                       ADC_SYNCBUSY;    /**< Offset: 0x20 (R/   16) Synchronization Busy */
  __I   uint8_t                        Reserved4[0x02];
  __I   uint16_t                       ADC_RESULT;      /**< Offset: 0x24 (R/   16) Result */
  __I   uint8_t                        Reserved5[0x02];
  __IO  uint32_t                       ADC_SEQCTRL;     /**< Offset: 0x28 (R/W  32) Sequence Control */
  __IO  uint16_t                       ADC_CALIB;       /**< Offset: 0x2c (R/W  16) Calibration */
} adc_registers_t;
/** @}  end of Analog Digital Converter */

#endif /* SAMC_SAMC21_ADC_MODULE_H */

