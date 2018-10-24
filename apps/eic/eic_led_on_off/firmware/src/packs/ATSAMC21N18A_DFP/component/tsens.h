/**
 * \brief Header file for SAMC/SAMC21 TSENS
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
#ifndef SAMC_SAMC21_TSENS_MODULE_H
#define SAMC_SAMC21_TSENS_MODULE_H

/** \addtogroup SAMC_SAMC21 Temperature Sensor
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_TSENS                                 */
/* ========================================================================== */

/* -------- TSENS_CTRLA : (TSENS Offset: 0x00) (R/W 8) Control A Register -------- */
#define TSENS_CTRLA_SWRST_Pos                 (0U)                                           /**< (TSENS_CTRLA) Software Reset Position */
#define TSENS_CTRLA_SWRST_Msk                 (0x1U << TSENS_CTRLA_SWRST_Pos)                /**< (TSENS_CTRLA) Software Reset Mask */
#define TSENS_CTRLA_SWRST(value)              (TSENS_CTRLA_SWRST_Msk & ((value) << TSENS_CTRLA_SWRST_Pos))
#define TSENS_CTRLA_ENABLE_Pos                (1U)                                           /**< (TSENS_CTRLA) Enable Position */
#define TSENS_CTRLA_ENABLE_Msk                (0x1U << TSENS_CTRLA_ENABLE_Pos)               /**< (TSENS_CTRLA) Enable Mask */
#define TSENS_CTRLA_ENABLE(value)             (TSENS_CTRLA_ENABLE_Msk & ((value) << TSENS_CTRLA_ENABLE_Pos))
#define TSENS_CTRLA_RUNSTDBY_Pos              (6U)                                           /**< (TSENS_CTRLA) Run in Standby Position */
#define TSENS_CTRLA_RUNSTDBY_Msk              (0x1U << TSENS_CTRLA_RUNSTDBY_Pos)             /**< (TSENS_CTRLA) Run in Standby Mask */
#define TSENS_CTRLA_RUNSTDBY(value)           (TSENS_CTRLA_RUNSTDBY_Msk & ((value) << TSENS_CTRLA_RUNSTDBY_Pos))
#define TSENS_CTRLA_Msk                       (0x00000043UL)                                 /**< (TSENS_CTRLA) Register Mask  */

/* -------- TSENS_CTRLB : (TSENS Offset: 0x01) ( /W 8) Control B Register -------- */
#define TSENS_CTRLB_START_Pos                 (0U)                                           /**< (TSENS_CTRLB) Start Measurement Position */
#define TSENS_CTRLB_START_Msk                 (0x1U << TSENS_CTRLB_START_Pos)                /**< (TSENS_CTRLB) Start Measurement Mask */
#define TSENS_CTRLB_START(value)              (TSENS_CTRLB_START_Msk & ((value) << TSENS_CTRLB_START_Pos))
#define TSENS_CTRLB_Msk                       (0x00000001UL)                                 /**< (TSENS_CTRLB) Register Mask  */

/* -------- TSENS_CTRLC : (TSENS Offset: 0x02) (R/W 8) Control C Register -------- */
#define TSENS_CTRLC_WINMODE_Pos               (0U)                                           /**< (TSENS_CTRLC) Window Monitor Mode Position */
#define TSENS_CTRLC_WINMODE_Msk               (0x7U << TSENS_CTRLC_WINMODE_Pos)              /**< (TSENS_CTRLC) Window Monitor Mode Mask */
#define TSENS_CTRLC_WINMODE(value)            (TSENS_CTRLC_WINMODE_Msk & ((value) << TSENS_CTRLC_WINMODE_Pos))
#define   TSENS_CTRLC_WINMODE_DISABLE_Val     (0U)                                           /**< (TSENS_CTRLC) No window mode (default)  */
#define   TSENS_CTRLC_WINMODE_ABOVE_Val       (1U)                                           /**< (TSENS_CTRLC) VALUE greater than WINLT  */
#define   TSENS_CTRLC_WINMODE_BELOW_Val       (2U)                                           /**< (TSENS_CTRLC) VALUE less than WINUT  */
#define   TSENS_CTRLC_WINMODE_INSIDE_Val      (3U)                                           /**< (TSENS_CTRLC) VALUE greater than WINLT and VALUE less than WINUT  */
#define   TSENS_CTRLC_WINMODE_OUTSIDE_Val     (4U)                                           /**< (TSENS_CTRLC) VALUE less than WINLT or VALUE greater than WINUT  */
#define   TSENS_CTRLC_WINMODE_HYST_ABOVE_Val  (5U)                                           /**< (TSENS_CTRLC) VALUE greater than WINUT with hysteresis to WINLT  */
#define   TSENS_CTRLC_WINMODE_HYST_BELOW_Val  (6U)                                           /**< (TSENS_CTRLC) VALUE less than WINLST with hysteresis to WINUT  */
#define TSENS_CTRLC_WINMODE_DISABLE           (TSENS_CTRLC_WINMODE_DISABLE_Val << TSENS_CTRLC_WINMODE_Pos) /**< (TSENS_CTRLC) No window mode (default) Position  */
#define TSENS_CTRLC_WINMODE_ABOVE             (TSENS_CTRLC_WINMODE_ABOVE_Val << TSENS_CTRLC_WINMODE_Pos) /**< (TSENS_CTRLC) VALUE greater than WINLT Position  */
#define TSENS_CTRLC_WINMODE_BELOW             (TSENS_CTRLC_WINMODE_BELOW_Val << TSENS_CTRLC_WINMODE_Pos) /**< (TSENS_CTRLC) VALUE less than WINUT Position  */
#define TSENS_CTRLC_WINMODE_INSIDE            (TSENS_CTRLC_WINMODE_INSIDE_Val << TSENS_CTRLC_WINMODE_Pos) /**< (TSENS_CTRLC) VALUE greater than WINLT and VALUE less than WINUT Position  */
#define TSENS_CTRLC_WINMODE_OUTSIDE           (TSENS_CTRLC_WINMODE_OUTSIDE_Val << TSENS_CTRLC_WINMODE_Pos) /**< (TSENS_CTRLC) VALUE less than WINLT or VALUE greater than WINUT Position  */
#define TSENS_CTRLC_WINMODE_HYST_ABOVE        (TSENS_CTRLC_WINMODE_HYST_ABOVE_Val << TSENS_CTRLC_WINMODE_Pos) /**< (TSENS_CTRLC) VALUE greater than WINUT with hysteresis to WINLT Position  */
#define TSENS_CTRLC_WINMODE_HYST_BELOW        (TSENS_CTRLC_WINMODE_HYST_BELOW_Val << TSENS_CTRLC_WINMODE_Pos) /**< (TSENS_CTRLC) VALUE less than WINLST with hysteresis to WINUT Position  */
#define TSENS_CTRLC_FREERUN_Pos               (4U)                                           /**< (TSENS_CTRLC) Free Running Measurement Position */
#define TSENS_CTRLC_FREERUN_Msk               (0x1U << TSENS_CTRLC_FREERUN_Pos)              /**< (TSENS_CTRLC) Free Running Measurement Mask */
#define TSENS_CTRLC_FREERUN(value)            (TSENS_CTRLC_FREERUN_Msk & ((value) << TSENS_CTRLC_FREERUN_Pos))
#define TSENS_CTRLC_Msk                       (0x00000017UL)                                 /**< (TSENS_CTRLC) Register Mask  */

/* -------- TSENS_EVCTRL : (TSENS Offset: 0x03) (R/W 8) Event Control Register -------- */
#define TSENS_EVCTRL_STARTEI_Pos              (0U)                                           /**< (TSENS_EVCTRL) Start Conversion Event Input Enable Position */
#define TSENS_EVCTRL_STARTEI_Msk              (0x1U << TSENS_EVCTRL_STARTEI_Pos)             /**< (TSENS_EVCTRL) Start Conversion Event Input Enable Mask */
#define TSENS_EVCTRL_STARTEI(value)           (TSENS_EVCTRL_STARTEI_Msk & ((value) << TSENS_EVCTRL_STARTEI_Pos))
#define TSENS_EVCTRL_STARTINV_Pos             (1U)                                           /**< (TSENS_EVCTRL) Start Conversion Event Invert Enable Position */
#define TSENS_EVCTRL_STARTINV_Msk             (0x1U << TSENS_EVCTRL_STARTINV_Pos)            /**< (TSENS_EVCTRL) Start Conversion Event Invert Enable Mask */
#define TSENS_EVCTRL_STARTINV(value)          (TSENS_EVCTRL_STARTINV_Msk & ((value) << TSENS_EVCTRL_STARTINV_Pos))
#define TSENS_EVCTRL_WINEO_Pos                (2U)                                           /**< (TSENS_EVCTRL) Window Monitor Event Out Position */
#define TSENS_EVCTRL_WINEO_Msk                (0x1U << TSENS_EVCTRL_WINEO_Pos)               /**< (TSENS_EVCTRL) Window Monitor Event Out Mask */
#define TSENS_EVCTRL_WINEO(value)             (TSENS_EVCTRL_WINEO_Msk & ((value) << TSENS_EVCTRL_WINEO_Pos))
#define TSENS_EVCTRL_Msk                      (0x00000007UL)                                 /**< (TSENS_EVCTRL) Register Mask  */

/* -------- TSENS_INTENCLR : (TSENS Offset: 0x04) (R/W 8) Interrupt Enable Clear Register -------- */
#define TSENS_INTENCLR_RESRDY_Pos             (0U)                                           /**< (TSENS_INTENCLR) Result Ready Interrupt Enable Position */
#define TSENS_INTENCLR_RESRDY_Msk             (0x1U << TSENS_INTENCLR_RESRDY_Pos)            /**< (TSENS_INTENCLR) Result Ready Interrupt Enable Mask */
#define TSENS_INTENCLR_RESRDY(value)          (TSENS_INTENCLR_RESRDY_Msk & ((value) << TSENS_INTENCLR_RESRDY_Pos))
#define TSENS_INTENCLR_OVERRUN_Pos            (1U)                                           /**< (TSENS_INTENCLR) Overrun Interrupt Enable Position */
#define TSENS_INTENCLR_OVERRUN_Msk            (0x1U << TSENS_INTENCLR_OVERRUN_Pos)           /**< (TSENS_INTENCLR) Overrun Interrupt Enable Mask */
#define TSENS_INTENCLR_OVERRUN(value)         (TSENS_INTENCLR_OVERRUN_Msk & ((value) << TSENS_INTENCLR_OVERRUN_Pos))
#define TSENS_INTENCLR_WINMON_Pos             (2U)                                           /**< (TSENS_INTENCLR) Window Monitor Interrupt Enable Position */
#define TSENS_INTENCLR_WINMON_Msk             (0x1U << TSENS_INTENCLR_WINMON_Pos)            /**< (TSENS_INTENCLR) Window Monitor Interrupt Enable Mask */
#define TSENS_INTENCLR_WINMON(value)          (TSENS_INTENCLR_WINMON_Msk & ((value) << TSENS_INTENCLR_WINMON_Pos))
#define TSENS_INTENCLR_OVF_Pos                (3U)                                           /**< (TSENS_INTENCLR) Overflow Interrupt Enable Position */
#define TSENS_INTENCLR_OVF_Msk                (0x1U << TSENS_INTENCLR_OVF_Pos)               /**< (TSENS_INTENCLR) Overflow Interrupt Enable Mask */
#define TSENS_INTENCLR_OVF(value)             (TSENS_INTENCLR_OVF_Msk & ((value) << TSENS_INTENCLR_OVF_Pos))
#define TSENS_INTENCLR_Msk                    (0x0000000FUL)                                 /**< (TSENS_INTENCLR) Register Mask  */

/* -------- TSENS_INTENSET : (TSENS Offset: 0x05) (R/W 8) Interrupt Enable Set Register -------- */
#define TSENS_INTENSET_RESRDY_Pos             (0U)                                           /**< (TSENS_INTENSET) Result Ready Interrupt Enable Position */
#define TSENS_INTENSET_RESRDY_Msk             (0x1U << TSENS_INTENSET_RESRDY_Pos)            /**< (TSENS_INTENSET) Result Ready Interrupt Enable Mask */
#define TSENS_INTENSET_RESRDY(value)          (TSENS_INTENSET_RESRDY_Msk & ((value) << TSENS_INTENSET_RESRDY_Pos))
#define TSENS_INTENSET_OVERRUN_Pos            (1U)                                           /**< (TSENS_INTENSET) Overrun Interrupt Enable Position */
#define TSENS_INTENSET_OVERRUN_Msk            (0x1U << TSENS_INTENSET_OVERRUN_Pos)           /**< (TSENS_INTENSET) Overrun Interrupt Enable Mask */
#define TSENS_INTENSET_OVERRUN(value)         (TSENS_INTENSET_OVERRUN_Msk & ((value) << TSENS_INTENSET_OVERRUN_Pos))
#define TSENS_INTENSET_WINMON_Pos             (2U)                                           /**< (TSENS_INTENSET) Window Monitor Interrupt Enable Position */
#define TSENS_INTENSET_WINMON_Msk             (0x1U << TSENS_INTENSET_WINMON_Pos)            /**< (TSENS_INTENSET) Window Monitor Interrupt Enable Mask */
#define TSENS_INTENSET_WINMON(value)          (TSENS_INTENSET_WINMON_Msk & ((value) << TSENS_INTENSET_WINMON_Pos))
#define TSENS_INTENSET_OVF_Pos                (3U)                                           /**< (TSENS_INTENSET) Overflow Interrupt Enable Position */
#define TSENS_INTENSET_OVF_Msk                (0x1U << TSENS_INTENSET_OVF_Pos)               /**< (TSENS_INTENSET) Overflow Interrupt Enable Mask */
#define TSENS_INTENSET_OVF(value)             (TSENS_INTENSET_OVF_Msk & ((value) << TSENS_INTENSET_OVF_Pos))
#define TSENS_INTENSET_Msk                    (0x0000000FUL)                                 /**< (TSENS_INTENSET) Register Mask  */

/* -------- TSENS_INTFLAG : (TSENS Offset: 0x06) (R/W 8) Interrupt Flag Status and Clear Register -------- */
#define TSENS_INTFLAG_RESRDY_Pos              (0U)                                           /**< (TSENS_INTFLAG) Result Ready Position */
#define TSENS_INTFLAG_RESRDY_Msk              (0x1U << TSENS_INTFLAG_RESRDY_Pos)             /**< (TSENS_INTFLAG) Result Ready Mask */
#define TSENS_INTFLAG_RESRDY(value)           (TSENS_INTFLAG_RESRDY_Msk & ((value) << TSENS_INTFLAG_RESRDY_Pos))
#define TSENS_INTFLAG_OVERRUN_Pos             (1U)                                           /**< (TSENS_INTFLAG) Overrun Position */
#define TSENS_INTFLAG_OVERRUN_Msk             (0x1U << TSENS_INTFLAG_OVERRUN_Pos)            /**< (TSENS_INTFLAG) Overrun Mask */
#define TSENS_INTFLAG_OVERRUN(value)          (TSENS_INTFLAG_OVERRUN_Msk & ((value) << TSENS_INTFLAG_OVERRUN_Pos))
#define TSENS_INTFLAG_WINMON_Pos              (2U)                                           /**< (TSENS_INTFLAG) Window Monitor Position */
#define TSENS_INTFLAG_WINMON_Msk              (0x1U << TSENS_INTFLAG_WINMON_Pos)             /**< (TSENS_INTFLAG) Window Monitor Mask */
#define TSENS_INTFLAG_WINMON(value)           (TSENS_INTFLAG_WINMON_Msk & ((value) << TSENS_INTFLAG_WINMON_Pos))
#define TSENS_INTFLAG_OVF_Pos                 (3U)                                           /**< (TSENS_INTFLAG) Overflow Position */
#define TSENS_INTFLAG_OVF_Msk                 (0x1U << TSENS_INTFLAG_OVF_Pos)                /**< (TSENS_INTFLAG) Overflow Mask */
#define TSENS_INTFLAG_OVF(value)              (TSENS_INTFLAG_OVF_Msk & ((value) << TSENS_INTFLAG_OVF_Pos))
#define TSENS_INTFLAG_Msk                     (0x0000000FUL)                                 /**< (TSENS_INTFLAG) Register Mask  */

/* -------- TSENS_STATUS : (TSENS Offset: 0x07) (R/  8) Status Register -------- */
#define TSENS_STATUS_OVF_Pos                  (0U)                                           /**< (TSENS_STATUS) Result Overflow Position */
#define TSENS_STATUS_OVF_Msk                  (0x1U << TSENS_STATUS_OVF_Pos)                 /**< (TSENS_STATUS) Result Overflow Mask */
#define TSENS_STATUS_OVF(value)               (TSENS_STATUS_OVF_Msk & ((value) << TSENS_STATUS_OVF_Pos))
#define TSENS_STATUS_Msk                      (0x00000001UL)                                 /**< (TSENS_STATUS) Register Mask  */

/* -------- TSENS_SYNCBUSY : (TSENS Offset: 0x08) (R/  32) Synchronization Busy Register -------- */
#define TSENS_SYNCBUSY_SWRST_Pos              (0U)                                           /**< (TSENS_SYNCBUSY) Software Reset Busy Position */
#define TSENS_SYNCBUSY_SWRST_Msk              (0x1U << TSENS_SYNCBUSY_SWRST_Pos)             /**< (TSENS_SYNCBUSY) Software Reset Busy Mask */
#define TSENS_SYNCBUSY_SWRST(value)           (TSENS_SYNCBUSY_SWRST_Msk & ((value) << TSENS_SYNCBUSY_SWRST_Pos))
#define TSENS_SYNCBUSY_ENABLE_Pos             (1U)                                           /**< (TSENS_SYNCBUSY) Enable Busy Position */
#define TSENS_SYNCBUSY_ENABLE_Msk             (0x1U << TSENS_SYNCBUSY_ENABLE_Pos)            /**< (TSENS_SYNCBUSY) Enable Busy Mask */
#define TSENS_SYNCBUSY_ENABLE(value)          (TSENS_SYNCBUSY_ENABLE_Msk & ((value) << TSENS_SYNCBUSY_ENABLE_Pos))
#define TSENS_SYNCBUSY_Msk                    (0x00000003UL)                                 /**< (TSENS_SYNCBUSY) Register Mask  */

/* -------- TSENS_VALUE : (TSENS Offset: 0x0C) (R/  32) Value Register -------- */
#define TSENS_VALUE_VALUE_Pos                 (0U)                                           /**< (TSENS_VALUE) Measurement Value Position */
#define TSENS_VALUE_VALUE_Msk                 (0xFFFFFFU << TSENS_VALUE_VALUE_Pos)           /**< (TSENS_VALUE) Measurement Value Mask */
#define TSENS_VALUE_VALUE(value)              (TSENS_VALUE_VALUE_Msk & ((value) << TSENS_VALUE_VALUE_Pos))
#define TSENS_VALUE_Msk                       (0x00FFFFFFUL)                                 /**< (TSENS_VALUE) Register Mask  */

/* -------- TSENS_WINLT : (TSENS Offset: 0x10) (R/W 32) Window Monitor Lower Threshold Register -------- */
#define TSENS_WINLT_WINLT_Pos                 (0U)                                           /**< (TSENS_WINLT) Window Lower Threshold Position */
#define TSENS_WINLT_WINLT_Msk                 (0xFFFFFFU << TSENS_WINLT_WINLT_Pos)           /**< (TSENS_WINLT) Window Lower Threshold Mask */
#define TSENS_WINLT_WINLT(value)              (TSENS_WINLT_WINLT_Msk & ((value) << TSENS_WINLT_WINLT_Pos))
#define TSENS_WINLT_Msk                       (0x00FFFFFFUL)                                 /**< (TSENS_WINLT) Register Mask  */

/* -------- TSENS_WINUT : (TSENS Offset: 0x14) (R/W 32) Window Monitor Upper Threshold Register -------- */
#define TSENS_WINUT_WINUT_Pos                 (0U)                                           /**< (TSENS_WINUT) Window Upper Threshold Position */
#define TSENS_WINUT_WINUT_Msk                 (0xFFFFFFU << TSENS_WINUT_WINUT_Pos)           /**< (TSENS_WINUT) Window Upper Threshold Mask */
#define TSENS_WINUT_WINUT(value)              (TSENS_WINUT_WINUT_Msk & ((value) << TSENS_WINUT_WINUT_Pos))
#define TSENS_WINUT_Msk                       (0x00FFFFFFUL)                                 /**< (TSENS_WINUT) Register Mask  */

/* -------- TSENS_GAIN : (TSENS Offset: 0x18) (R/W 32) Gain Register -------- */
#define TSENS_GAIN_GAIN_Pos                   (0U)                                           /**< (TSENS_GAIN) Time Amplifier Gain Position */
#define TSENS_GAIN_GAIN_Msk                   (0xFFFFFFU << TSENS_GAIN_GAIN_Pos)             /**< (TSENS_GAIN) Time Amplifier Gain Mask */
#define TSENS_GAIN_GAIN(value)                (TSENS_GAIN_GAIN_Msk & ((value) << TSENS_GAIN_GAIN_Pos))
#define TSENS_GAIN_Msk                        (0x00FFFFFFUL)                                 /**< (TSENS_GAIN) Register Mask  */

/* -------- TSENS_OFFSET : (TSENS Offset: 0x1C) (R/W 32) Offset Register -------- */
#define TSENS_OFFSET_OFFSETC_Pos              (0U)                                           /**< (TSENS_OFFSET) Offset Correction Position */
#define TSENS_OFFSET_OFFSETC_Msk              (0xFFFFFFU << TSENS_OFFSET_OFFSETC_Pos)        /**< (TSENS_OFFSET) Offset Correction Mask */
#define TSENS_OFFSET_OFFSETC(value)           (TSENS_OFFSET_OFFSETC_Msk & ((value) << TSENS_OFFSET_OFFSETC_Pos))
#define TSENS_OFFSET_Msk                      (0x00FFFFFFUL)                                 /**< (TSENS_OFFSET) Register Mask  */

/* -------- TSENS_CAL : (TSENS Offset: 0x20) (R/W 32) Calibration Register -------- */
#define TSENS_CAL_FCAL_Pos                    (0U)                                           /**< (TSENS_CAL) Frequency Calibration Position */
#define TSENS_CAL_FCAL_Msk                    (0x3FU << TSENS_CAL_FCAL_Pos)                  /**< (TSENS_CAL) Frequency Calibration Mask */
#define TSENS_CAL_FCAL(value)                 (TSENS_CAL_FCAL_Msk & ((value) << TSENS_CAL_FCAL_Pos))
#define TSENS_CAL_TCAL_Pos                    (8U)                                           /**< (TSENS_CAL) Temperature Calibration Position */
#define TSENS_CAL_TCAL_Msk                    (0x3FU << TSENS_CAL_TCAL_Pos)                  /**< (TSENS_CAL) Temperature Calibration Mask */
#define TSENS_CAL_TCAL(value)                 (TSENS_CAL_TCAL_Msk & ((value) << TSENS_CAL_TCAL_Pos))
#define TSENS_CAL_Msk                         (0x00003F3FUL)                                 /**< (TSENS_CAL) Register Mask  */

/* -------- TSENS_DBGCTRL : (TSENS Offset: 0x24) (R/W 8) Debug Control Register -------- */
#define TSENS_DBGCTRL_DBGRUN_Pos              (0U)                                           /**< (TSENS_DBGCTRL) Debug Run Position */
#define TSENS_DBGCTRL_DBGRUN_Msk              (0x1U << TSENS_DBGCTRL_DBGRUN_Pos)             /**< (TSENS_DBGCTRL) Debug Run Mask */
#define TSENS_DBGCTRL_DBGRUN(value)           (TSENS_DBGCTRL_DBGRUN_Msk & ((value) << TSENS_DBGCTRL_DBGRUN_Pos))
#define TSENS_DBGCTRL_Msk                     (0x00000001UL)                                 /**< (TSENS_DBGCTRL) Register Mask  */

/** \brief TSENS register offsets definitions */
#define TSENS_CTRLA_OFFSET             (0x00)         /**< (TSENS_CTRLA) Control A Register Offset */
#define TSENS_CTRLB_OFFSET             (0x01)         /**< (TSENS_CTRLB) Control B Register Offset */
#define TSENS_CTRLC_OFFSET             (0x02)         /**< (TSENS_CTRLC) Control C Register Offset */
#define TSENS_EVCTRL_OFFSET            (0x03)         /**< (TSENS_EVCTRL) Event Control Register Offset */
#define TSENS_INTENCLR_OFFSET          (0x04)         /**< (TSENS_INTENCLR) Interrupt Enable Clear Register Offset */
#define TSENS_INTENSET_OFFSET          (0x05)         /**< (TSENS_INTENSET) Interrupt Enable Set Register Offset */
#define TSENS_INTFLAG_OFFSET           (0x06)         /**< (TSENS_INTFLAG) Interrupt Flag Status and Clear Register Offset */
#define TSENS_STATUS_OFFSET            (0x07)         /**< (TSENS_STATUS) Status Register Offset */
#define TSENS_SYNCBUSY_OFFSET          (0x08)         /**< (TSENS_SYNCBUSY) Synchronization Busy Register Offset */
#define TSENS_VALUE_OFFSET             (0x0C)         /**< (TSENS_VALUE) Value Register Offset */
#define TSENS_WINLT_OFFSET             (0x10)         /**< (TSENS_WINLT) Window Monitor Lower Threshold Register Offset */
#define TSENS_WINUT_OFFSET             (0x14)         /**< (TSENS_WINUT) Window Monitor Upper Threshold Register Offset */
#define TSENS_GAIN_OFFSET              (0x18)         /**< (TSENS_GAIN) Gain Register Offset */
#define TSENS_OFFSET_OFFSET            (0x1C)         /**< (TSENS_OFFSET) Offset Register Offset */
#define TSENS_CAL_OFFSET               (0x20)         /**< (TSENS_CAL) Calibration Register Offset */
#define TSENS_DBGCTRL_OFFSET           (0x24)         /**< (TSENS_DBGCTRL) Debug Control Register Offset */

/** \brief TSENS register API structure */
typedef struct
{
  __IO  uint8_t                        TSENS_CTRLA;     /**< Offset: 0x00 (R/W  8) Control A Register */
  __O   uint8_t                        TSENS_CTRLB;     /**< Offset: 0x01 ( /W  8) Control B Register */
  __IO  uint8_t                        TSENS_CTRLC;     /**< Offset: 0x02 (R/W  8) Control C Register */
  __IO  uint8_t                        TSENS_EVCTRL;    /**< Offset: 0x03 (R/W  8) Event Control Register */
  __IO  uint8_t                        TSENS_INTENCLR;  /**< Offset: 0x04 (R/W  8) Interrupt Enable Clear Register */
  __IO  uint8_t                        TSENS_INTENSET;  /**< Offset: 0x05 (R/W  8) Interrupt Enable Set Register */
  __IO  uint8_t                        TSENS_INTFLAG;   /**< Offset: 0x06 (R/W  8) Interrupt Flag Status and Clear Register */
  __I   uint8_t                        TSENS_STATUS;    /**< Offset: 0x07 (R/   8) Status Register */
  __I   uint32_t                       TSENS_SYNCBUSY;  /**< Offset: 0x08 (R/   32) Synchronization Busy Register */
  __I   uint32_t                       TSENS_VALUE;     /**< Offset: 0x0c (R/   32) Value Register */
  __IO  uint32_t                       TSENS_WINLT;     /**< Offset: 0x10 (R/W  32) Window Monitor Lower Threshold Register */
  __IO  uint32_t                       TSENS_WINUT;     /**< Offset: 0x14 (R/W  32) Window Monitor Upper Threshold Register */
  __IO  uint32_t                       TSENS_GAIN;      /**< Offset: 0x18 (R/W  32) Gain Register */
  __IO  uint32_t                       TSENS_OFFSET;    /**< Offset: 0x1c (R/W  32) Offset Register */
  __IO  uint32_t                       TSENS_CAL;       /**< Offset: 0x20 (R/W  32) Calibration Register */
  __IO  uint8_t                        TSENS_DBGCTRL;   /**< Offset: 0x24 (R/W  8) Debug Control Register */
} tsens_registers_t;
/** @}  end of Temperature Sensor */

#endif /* SAMC_SAMC21_TSENS_MODULE_H */

