/**
 * \brief Header file for SAMC/SAMC21 EVSYS
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
#ifndef SAMC_SAMC21_EVSYS_MODULE_H
#define SAMC_SAMC21_EVSYS_MODULE_H

/** \addtogroup SAMC_SAMC21 Event System Interface
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_EVSYS                                 */
/* ========================================================================== */

/* -------- EVSYS_CTRLA : (EVSYS Offset: 0x00) (R/W 8) Control -------- */
#define EVSYS_CTRLA_SWRST_Pos                 (0U)                                           /**< (EVSYS_CTRLA) Software Reset Position */
#define EVSYS_CTRLA_SWRST_Msk                 (0x1U << EVSYS_CTRLA_SWRST_Pos)                /**< (EVSYS_CTRLA) Software Reset Mask */
#define EVSYS_CTRLA_SWRST(value)              (EVSYS_CTRLA_SWRST_Msk & ((value) << EVSYS_CTRLA_SWRST_Pos))
#define EVSYS_CTRLA_Msk                       (0x00000001UL)                                 /**< (EVSYS_CTRLA) Register Mask  */

/* -------- EVSYS_CHSTATUS : (EVSYS Offset: 0x0C) (R/  32) Channel Status -------- */
#define EVSYS_CHSTATUS_USRRDY0_Pos            (0U)                                           /**< (EVSYS_CHSTATUS) Channel 0 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY0_Msk            (0x1U << EVSYS_CHSTATUS_USRRDY0_Pos)           /**< (EVSYS_CHSTATUS) Channel 0 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY0(value)         (EVSYS_CHSTATUS_USRRDY0_Msk & ((value) << EVSYS_CHSTATUS_USRRDY0_Pos))
#define EVSYS_CHSTATUS_USRRDY1_Pos            (1U)                                           /**< (EVSYS_CHSTATUS) Channel 1 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY1_Msk            (0x1U << EVSYS_CHSTATUS_USRRDY1_Pos)           /**< (EVSYS_CHSTATUS) Channel 1 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY1(value)         (EVSYS_CHSTATUS_USRRDY1_Msk & ((value) << EVSYS_CHSTATUS_USRRDY1_Pos))
#define EVSYS_CHSTATUS_USRRDY2_Pos            (2U)                                           /**< (EVSYS_CHSTATUS) Channel 2 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY2_Msk            (0x1U << EVSYS_CHSTATUS_USRRDY2_Pos)           /**< (EVSYS_CHSTATUS) Channel 2 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY2(value)         (EVSYS_CHSTATUS_USRRDY2_Msk & ((value) << EVSYS_CHSTATUS_USRRDY2_Pos))
#define EVSYS_CHSTATUS_USRRDY3_Pos            (3U)                                           /**< (EVSYS_CHSTATUS) Channel 3 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY3_Msk            (0x1U << EVSYS_CHSTATUS_USRRDY3_Pos)           /**< (EVSYS_CHSTATUS) Channel 3 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY3(value)         (EVSYS_CHSTATUS_USRRDY3_Msk & ((value) << EVSYS_CHSTATUS_USRRDY3_Pos))
#define EVSYS_CHSTATUS_USRRDY4_Pos            (4U)                                           /**< (EVSYS_CHSTATUS) Channel 4 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY4_Msk            (0x1U << EVSYS_CHSTATUS_USRRDY4_Pos)           /**< (EVSYS_CHSTATUS) Channel 4 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY4(value)         (EVSYS_CHSTATUS_USRRDY4_Msk & ((value) << EVSYS_CHSTATUS_USRRDY4_Pos))
#define EVSYS_CHSTATUS_USRRDY5_Pos            (5U)                                           /**< (EVSYS_CHSTATUS) Channel 5 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY5_Msk            (0x1U << EVSYS_CHSTATUS_USRRDY5_Pos)           /**< (EVSYS_CHSTATUS) Channel 5 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY5(value)         (EVSYS_CHSTATUS_USRRDY5_Msk & ((value) << EVSYS_CHSTATUS_USRRDY5_Pos))
#define EVSYS_CHSTATUS_USRRDY6_Pos            (6U)                                           /**< (EVSYS_CHSTATUS) Channel 6 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY6_Msk            (0x1U << EVSYS_CHSTATUS_USRRDY6_Pos)           /**< (EVSYS_CHSTATUS) Channel 6 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY6(value)         (EVSYS_CHSTATUS_USRRDY6_Msk & ((value) << EVSYS_CHSTATUS_USRRDY6_Pos))
#define EVSYS_CHSTATUS_USRRDY7_Pos            (7U)                                           /**< (EVSYS_CHSTATUS) Channel 7 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY7_Msk            (0x1U << EVSYS_CHSTATUS_USRRDY7_Pos)           /**< (EVSYS_CHSTATUS) Channel 7 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY7(value)         (EVSYS_CHSTATUS_USRRDY7_Msk & ((value) << EVSYS_CHSTATUS_USRRDY7_Pos))
#define EVSYS_CHSTATUS_USRRDY8_Pos            (8U)                                           /**< (EVSYS_CHSTATUS) Channel 8 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY8_Msk            (0x1U << EVSYS_CHSTATUS_USRRDY8_Pos)           /**< (EVSYS_CHSTATUS) Channel 8 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY8(value)         (EVSYS_CHSTATUS_USRRDY8_Msk & ((value) << EVSYS_CHSTATUS_USRRDY8_Pos))
#define EVSYS_CHSTATUS_USRRDY9_Pos            (9U)                                           /**< (EVSYS_CHSTATUS) Channel 9 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY9_Msk            (0x1U << EVSYS_CHSTATUS_USRRDY9_Pos)           /**< (EVSYS_CHSTATUS) Channel 9 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY9(value)         (EVSYS_CHSTATUS_USRRDY9_Msk & ((value) << EVSYS_CHSTATUS_USRRDY9_Pos))
#define EVSYS_CHSTATUS_USRRDY10_Pos           (10U)                                          /**< (EVSYS_CHSTATUS) Channel 10 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY10_Msk           (0x1U << EVSYS_CHSTATUS_USRRDY10_Pos)          /**< (EVSYS_CHSTATUS) Channel 10 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY10(value)        (EVSYS_CHSTATUS_USRRDY10_Msk & ((value) << EVSYS_CHSTATUS_USRRDY10_Pos))
#define EVSYS_CHSTATUS_USRRDY11_Pos           (11U)                                          /**< (EVSYS_CHSTATUS) Channel 11 User Ready Position */
#define EVSYS_CHSTATUS_USRRDY11_Msk           (0x1U << EVSYS_CHSTATUS_USRRDY11_Pos)          /**< (EVSYS_CHSTATUS) Channel 11 User Ready Mask */
#define EVSYS_CHSTATUS_USRRDY11(value)        (EVSYS_CHSTATUS_USRRDY11_Msk & ((value) << EVSYS_CHSTATUS_USRRDY11_Pos))
#define EVSYS_CHSTATUS_CHBUSY0_Pos            (16U)                                          /**< (EVSYS_CHSTATUS) Channel 0 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY0_Msk            (0x1U << EVSYS_CHSTATUS_CHBUSY0_Pos)           /**< (EVSYS_CHSTATUS) Channel 0 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY0(value)         (EVSYS_CHSTATUS_CHBUSY0_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY0_Pos))
#define EVSYS_CHSTATUS_CHBUSY1_Pos            (17U)                                          /**< (EVSYS_CHSTATUS) Channel 1 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY1_Msk            (0x1U << EVSYS_CHSTATUS_CHBUSY1_Pos)           /**< (EVSYS_CHSTATUS) Channel 1 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY1(value)         (EVSYS_CHSTATUS_CHBUSY1_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY1_Pos))
#define EVSYS_CHSTATUS_CHBUSY2_Pos            (18U)                                          /**< (EVSYS_CHSTATUS) Channel 2 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY2_Msk            (0x1U << EVSYS_CHSTATUS_CHBUSY2_Pos)           /**< (EVSYS_CHSTATUS) Channel 2 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY2(value)         (EVSYS_CHSTATUS_CHBUSY2_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY2_Pos))
#define EVSYS_CHSTATUS_CHBUSY3_Pos            (19U)                                          /**< (EVSYS_CHSTATUS) Channel 3 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY3_Msk            (0x1U << EVSYS_CHSTATUS_CHBUSY3_Pos)           /**< (EVSYS_CHSTATUS) Channel 3 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY3(value)         (EVSYS_CHSTATUS_CHBUSY3_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY3_Pos))
#define EVSYS_CHSTATUS_CHBUSY4_Pos            (20U)                                          /**< (EVSYS_CHSTATUS) Channel 4 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY4_Msk            (0x1U << EVSYS_CHSTATUS_CHBUSY4_Pos)           /**< (EVSYS_CHSTATUS) Channel 4 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY4(value)         (EVSYS_CHSTATUS_CHBUSY4_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY4_Pos))
#define EVSYS_CHSTATUS_CHBUSY5_Pos            (21U)                                          /**< (EVSYS_CHSTATUS) Channel 5 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY5_Msk            (0x1U << EVSYS_CHSTATUS_CHBUSY5_Pos)           /**< (EVSYS_CHSTATUS) Channel 5 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY5(value)         (EVSYS_CHSTATUS_CHBUSY5_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY5_Pos))
#define EVSYS_CHSTATUS_CHBUSY6_Pos            (22U)                                          /**< (EVSYS_CHSTATUS) Channel 6 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY6_Msk            (0x1U << EVSYS_CHSTATUS_CHBUSY6_Pos)           /**< (EVSYS_CHSTATUS) Channel 6 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY6(value)         (EVSYS_CHSTATUS_CHBUSY6_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY6_Pos))
#define EVSYS_CHSTATUS_CHBUSY7_Pos            (23U)                                          /**< (EVSYS_CHSTATUS) Channel 7 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY7_Msk            (0x1U << EVSYS_CHSTATUS_CHBUSY7_Pos)           /**< (EVSYS_CHSTATUS) Channel 7 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY7(value)         (EVSYS_CHSTATUS_CHBUSY7_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY7_Pos))
#define EVSYS_CHSTATUS_CHBUSY8_Pos            (24U)                                          /**< (EVSYS_CHSTATUS) Channel 8 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY8_Msk            (0x1U << EVSYS_CHSTATUS_CHBUSY8_Pos)           /**< (EVSYS_CHSTATUS) Channel 8 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY8(value)         (EVSYS_CHSTATUS_CHBUSY8_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY8_Pos))
#define EVSYS_CHSTATUS_CHBUSY9_Pos            (25U)                                          /**< (EVSYS_CHSTATUS) Channel 9 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY9_Msk            (0x1U << EVSYS_CHSTATUS_CHBUSY9_Pos)           /**< (EVSYS_CHSTATUS) Channel 9 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY9(value)         (EVSYS_CHSTATUS_CHBUSY9_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY9_Pos))
#define EVSYS_CHSTATUS_CHBUSY10_Pos           (26U)                                          /**< (EVSYS_CHSTATUS) Channel 10 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY10_Msk           (0x1U << EVSYS_CHSTATUS_CHBUSY10_Pos)          /**< (EVSYS_CHSTATUS) Channel 10 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY10(value)        (EVSYS_CHSTATUS_CHBUSY10_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY10_Pos))
#define EVSYS_CHSTATUS_CHBUSY11_Pos           (27U)                                          /**< (EVSYS_CHSTATUS) Channel 11 Busy Position */
#define EVSYS_CHSTATUS_CHBUSY11_Msk           (0x1U << EVSYS_CHSTATUS_CHBUSY11_Pos)          /**< (EVSYS_CHSTATUS) Channel 11 Busy Mask */
#define EVSYS_CHSTATUS_CHBUSY11(value)        (EVSYS_CHSTATUS_CHBUSY11_Msk & ((value) << EVSYS_CHSTATUS_CHBUSY11_Pos))
#define EVSYS_CHSTATUS_Msk                    (0x0FFF0FFFUL)                                 /**< (EVSYS_CHSTATUS) Register Mask  */

/* -------- EVSYS_INTENCLR : (EVSYS Offset: 0x10) (R/W 32) Interrupt Enable Clear -------- */
#define EVSYS_INTENCLR_OVR0_Pos               (0U)                                           /**< (EVSYS_INTENCLR) Channel 0 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR0_Msk               (0x1U << EVSYS_INTENCLR_OVR0_Pos)              /**< (EVSYS_INTENCLR) Channel 0 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR0(value)            (EVSYS_INTENCLR_OVR0_Msk & ((value) << EVSYS_INTENCLR_OVR0_Pos))
#define EVSYS_INTENCLR_OVR1_Pos               (1U)                                           /**< (EVSYS_INTENCLR) Channel 1 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR1_Msk               (0x1U << EVSYS_INTENCLR_OVR1_Pos)              /**< (EVSYS_INTENCLR) Channel 1 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR1(value)            (EVSYS_INTENCLR_OVR1_Msk & ((value) << EVSYS_INTENCLR_OVR1_Pos))
#define EVSYS_INTENCLR_OVR2_Pos               (2U)                                           /**< (EVSYS_INTENCLR) Channel 2 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR2_Msk               (0x1U << EVSYS_INTENCLR_OVR2_Pos)              /**< (EVSYS_INTENCLR) Channel 2 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR2(value)            (EVSYS_INTENCLR_OVR2_Msk & ((value) << EVSYS_INTENCLR_OVR2_Pos))
#define EVSYS_INTENCLR_OVR3_Pos               (3U)                                           /**< (EVSYS_INTENCLR) Channel 3 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR3_Msk               (0x1U << EVSYS_INTENCLR_OVR3_Pos)              /**< (EVSYS_INTENCLR) Channel 3 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR3(value)            (EVSYS_INTENCLR_OVR3_Msk & ((value) << EVSYS_INTENCLR_OVR3_Pos))
#define EVSYS_INTENCLR_OVR4_Pos               (4U)                                           /**< (EVSYS_INTENCLR) Channel 4 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR4_Msk               (0x1U << EVSYS_INTENCLR_OVR4_Pos)              /**< (EVSYS_INTENCLR) Channel 4 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR4(value)            (EVSYS_INTENCLR_OVR4_Msk & ((value) << EVSYS_INTENCLR_OVR4_Pos))
#define EVSYS_INTENCLR_OVR5_Pos               (5U)                                           /**< (EVSYS_INTENCLR) Channel 5 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR5_Msk               (0x1U << EVSYS_INTENCLR_OVR5_Pos)              /**< (EVSYS_INTENCLR) Channel 5 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR5(value)            (EVSYS_INTENCLR_OVR5_Msk & ((value) << EVSYS_INTENCLR_OVR5_Pos))
#define EVSYS_INTENCLR_OVR6_Pos               (6U)                                           /**< (EVSYS_INTENCLR) Channel 6 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR6_Msk               (0x1U << EVSYS_INTENCLR_OVR6_Pos)              /**< (EVSYS_INTENCLR) Channel 6 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR6(value)            (EVSYS_INTENCLR_OVR6_Msk & ((value) << EVSYS_INTENCLR_OVR6_Pos))
#define EVSYS_INTENCLR_OVR7_Pos               (7U)                                           /**< (EVSYS_INTENCLR) Channel 7 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR7_Msk               (0x1U << EVSYS_INTENCLR_OVR7_Pos)              /**< (EVSYS_INTENCLR) Channel 7 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR7(value)            (EVSYS_INTENCLR_OVR7_Msk & ((value) << EVSYS_INTENCLR_OVR7_Pos))
#define EVSYS_INTENCLR_OVR8_Pos               (8U)                                           /**< (EVSYS_INTENCLR) Channel 8 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR8_Msk               (0x1U << EVSYS_INTENCLR_OVR8_Pos)              /**< (EVSYS_INTENCLR) Channel 8 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR8(value)            (EVSYS_INTENCLR_OVR8_Msk & ((value) << EVSYS_INTENCLR_OVR8_Pos))
#define EVSYS_INTENCLR_OVR9_Pos               (9U)                                           /**< (EVSYS_INTENCLR) Channel 9 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR9_Msk               (0x1U << EVSYS_INTENCLR_OVR9_Pos)              /**< (EVSYS_INTENCLR) Channel 9 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR9(value)            (EVSYS_INTENCLR_OVR9_Msk & ((value) << EVSYS_INTENCLR_OVR9_Pos))
#define EVSYS_INTENCLR_OVR10_Pos              (10U)                                          /**< (EVSYS_INTENCLR) Channel 10 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR10_Msk              (0x1U << EVSYS_INTENCLR_OVR10_Pos)             /**< (EVSYS_INTENCLR) Channel 10 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR10(value)           (EVSYS_INTENCLR_OVR10_Msk & ((value) << EVSYS_INTENCLR_OVR10_Pos))
#define EVSYS_INTENCLR_OVR11_Pos              (11U)                                          /**< (EVSYS_INTENCLR) Channel 11 Overrun Interrupt Enable Position */
#define EVSYS_INTENCLR_OVR11_Msk              (0x1U << EVSYS_INTENCLR_OVR11_Pos)             /**< (EVSYS_INTENCLR) Channel 11 Overrun Interrupt Enable Mask */
#define EVSYS_INTENCLR_OVR11(value)           (EVSYS_INTENCLR_OVR11_Msk & ((value) << EVSYS_INTENCLR_OVR11_Pos))
#define EVSYS_INTENCLR_EVD0_Pos               (16U)                                          /**< (EVSYS_INTENCLR) Channel 0 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD0_Msk               (0x1U << EVSYS_INTENCLR_EVD0_Pos)              /**< (EVSYS_INTENCLR) Channel 0 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD0(value)            (EVSYS_INTENCLR_EVD0_Msk & ((value) << EVSYS_INTENCLR_EVD0_Pos))
#define EVSYS_INTENCLR_EVD1_Pos               (17U)                                          /**< (EVSYS_INTENCLR) Channel 1 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD1_Msk               (0x1U << EVSYS_INTENCLR_EVD1_Pos)              /**< (EVSYS_INTENCLR) Channel 1 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD1(value)            (EVSYS_INTENCLR_EVD1_Msk & ((value) << EVSYS_INTENCLR_EVD1_Pos))
#define EVSYS_INTENCLR_EVD2_Pos               (18U)                                          /**< (EVSYS_INTENCLR) Channel 2 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD2_Msk               (0x1U << EVSYS_INTENCLR_EVD2_Pos)              /**< (EVSYS_INTENCLR) Channel 2 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD2(value)            (EVSYS_INTENCLR_EVD2_Msk & ((value) << EVSYS_INTENCLR_EVD2_Pos))
#define EVSYS_INTENCLR_EVD3_Pos               (19U)                                          /**< (EVSYS_INTENCLR) Channel 3 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD3_Msk               (0x1U << EVSYS_INTENCLR_EVD3_Pos)              /**< (EVSYS_INTENCLR) Channel 3 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD3(value)            (EVSYS_INTENCLR_EVD3_Msk & ((value) << EVSYS_INTENCLR_EVD3_Pos))
#define EVSYS_INTENCLR_EVD4_Pos               (20U)                                          /**< (EVSYS_INTENCLR) Channel 4 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD4_Msk               (0x1U << EVSYS_INTENCLR_EVD4_Pos)              /**< (EVSYS_INTENCLR) Channel 4 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD4(value)            (EVSYS_INTENCLR_EVD4_Msk & ((value) << EVSYS_INTENCLR_EVD4_Pos))
#define EVSYS_INTENCLR_EVD5_Pos               (21U)                                          /**< (EVSYS_INTENCLR) Channel 5 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD5_Msk               (0x1U << EVSYS_INTENCLR_EVD5_Pos)              /**< (EVSYS_INTENCLR) Channel 5 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD5(value)            (EVSYS_INTENCLR_EVD5_Msk & ((value) << EVSYS_INTENCLR_EVD5_Pos))
#define EVSYS_INTENCLR_EVD6_Pos               (22U)                                          /**< (EVSYS_INTENCLR) Channel 6 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD6_Msk               (0x1U << EVSYS_INTENCLR_EVD6_Pos)              /**< (EVSYS_INTENCLR) Channel 6 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD6(value)            (EVSYS_INTENCLR_EVD6_Msk & ((value) << EVSYS_INTENCLR_EVD6_Pos))
#define EVSYS_INTENCLR_EVD7_Pos               (23U)                                          /**< (EVSYS_INTENCLR) Channel 7 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD7_Msk               (0x1U << EVSYS_INTENCLR_EVD7_Pos)              /**< (EVSYS_INTENCLR) Channel 7 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD7(value)            (EVSYS_INTENCLR_EVD7_Msk & ((value) << EVSYS_INTENCLR_EVD7_Pos))
#define EVSYS_INTENCLR_EVD8_Pos               (24U)                                          /**< (EVSYS_INTENCLR) Channel 8 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD8_Msk               (0x1U << EVSYS_INTENCLR_EVD8_Pos)              /**< (EVSYS_INTENCLR) Channel 8 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD8(value)            (EVSYS_INTENCLR_EVD8_Msk & ((value) << EVSYS_INTENCLR_EVD8_Pos))
#define EVSYS_INTENCLR_EVD9_Pos               (25U)                                          /**< (EVSYS_INTENCLR) Channel 9 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD9_Msk               (0x1U << EVSYS_INTENCLR_EVD9_Pos)              /**< (EVSYS_INTENCLR) Channel 9 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD9(value)            (EVSYS_INTENCLR_EVD9_Msk & ((value) << EVSYS_INTENCLR_EVD9_Pos))
#define EVSYS_INTENCLR_EVD10_Pos              (26U)                                          /**< (EVSYS_INTENCLR) Channel 10 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD10_Msk              (0x1U << EVSYS_INTENCLR_EVD10_Pos)             /**< (EVSYS_INTENCLR) Channel 10 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD10(value)           (EVSYS_INTENCLR_EVD10_Msk & ((value) << EVSYS_INTENCLR_EVD10_Pos))
#define EVSYS_INTENCLR_EVD11_Pos              (27U)                                          /**< (EVSYS_INTENCLR) Channel 11 Event Detection Interrupt Enable Position */
#define EVSYS_INTENCLR_EVD11_Msk              (0x1U << EVSYS_INTENCLR_EVD11_Pos)             /**< (EVSYS_INTENCLR) Channel 11 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENCLR_EVD11(value)           (EVSYS_INTENCLR_EVD11_Msk & ((value) << EVSYS_INTENCLR_EVD11_Pos))
#define EVSYS_INTENCLR_Msk                    (0x0FFF0FFFUL)                                 /**< (EVSYS_INTENCLR) Register Mask  */

/* -------- EVSYS_INTENSET : (EVSYS Offset: 0x14) (R/W 32) Interrupt Enable Set -------- */
#define EVSYS_INTENSET_OVR0_Pos               (0U)                                           /**< (EVSYS_INTENSET) Channel 0 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR0_Msk               (0x1U << EVSYS_INTENSET_OVR0_Pos)              /**< (EVSYS_INTENSET) Channel 0 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR0(value)            (EVSYS_INTENSET_OVR0_Msk & ((value) << EVSYS_INTENSET_OVR0_Pos))
#define EVSYS_INTENSET_OVR1_Pos               (1U)                                           /**< (EVSYS_INTENSET) Channel 1 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR1_Msk               (0x1U << EVSYS_INTENSET_OVR1_Pos)              /**< (EVSYS_INTENSET) Channel 1 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR1(value)            (EVSYS_INTENSET_OVR1_Msk & ((value) << EVSYS_INTENSET_OVR1_Pos))
#define EVSYS_INTENSET_OVR2_Pos               (2U)                                           /**< (EVSYS_INTENSET) Channel 2 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR2_Msk               (0x1U << EVSYS_INTENSET_OVR2_Pos)              /**< (EVSYS_INTENSET) Channel 2 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR2(value)            (EVSYS_INTENSET_OVR2_Msk & ((value) << EVSYS_INTENSET_OVR2_Pos))
#define EVSYS_INTENSET_OVR3_Pos               (3U)                                           /**< (EVSYS_INTENSET) Channel 3 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR3_Msk               (0x1U << EVSYS_INTENSET_OVR3_Pos)              /**< (EVSYS_INTENSET) Channel 3 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR3(value)            (EVSYS_INTENSET_OVR3_Msk & ((value) << EVSYS_INTENSET_OVR3_Pos))
#define EVSYS_INTENSET_OVR4_Pos               (4U)                                           /**< (EVSYS_INTENSET) Channel 4 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR4_Msk               (0x1U << EVSYS_INTENSET_OVR4_Pos)              /**< (EVSYS_INTENSET) Channel 4 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR4(value)            (EVSYS_INTENSET_OVR4_Msk & ((value) << EVSYS_INTENSET_OVR4_Pos))
#define EVSYS_INTENSET_OVR5_Pos               (5U)                                           /**< (EVSYS_INTENSET) Channel 5 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR5_Msk               (0x1U << EVSYS_INTENSET_OVR5_Pos)              /**< (EVSYS_INTENSET) Channel 5 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR5(value)            (EVSYS_INTENSET_OVR5_Msk & ((value) << EVSYS_INTENSET_OVR5_Pos))
#define EVSYS_INTENSET_OVR6_Pos               (6U)                                           /**< (EVSYS_INTENSET) Channel 6 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR6_Msk               (0x1U << EVSYS_INTENSET_OVR6_Pos)              /**< (EVSYS_INTENSET) Channel 6 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR6(value)            (EVSYS_INTENSET_OVR6_Msk & ((value) << EVSYS_INTENSET_OVR6_Pos))
#define EVSYS_INTENSET_OVR7_Pos               (7U)                                           /**< (EVSYS_INTENSET) Channel 7 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR7_Msk               (0x1U << EVSYS_INTENSET_OVR7_Pos)              /**< (EVSYS_INTENSET) Channel 7 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR7(value)            (EVSYS_INTENSET_OVR7_Msk & ((value) << EVSYS_INTENSET_OVR7_Pos))
#define EVSYS_INTENSET_OVR8_Pos               (8U)                                           /**< (EVSYS_INTENSET) Channel 8 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR8_Msk               (0x1U << EVSYS_INTENSET_OVR8_Pos)              /**< (EVSYS_INTENSET) Channel 8 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR8(value)            (EVSYS_INTENSET_OVR8_Msk & ((value) << EVSYS_INTENSET_OVR8_Pos))
#define EVSYS_INTENSET_OVR9_Pos               (9U)                                           /**< (EVSYS_INTENSET) Channel 9 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR9_Msk               (0x1U << EVSYS_INTENSET_OVR9_Pos)              /**< (EVSYS_INTENSET) Channel 9 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR9(value)            (EVSYS_INTENSET_OVR9_Msk & ((value) << EVSYS_INTENSET_OVR9_Pos))
#define EVSYS_INTENSET_OVR10_Pos              (10U)                                          /**< (EVSYS_INTENSET) Channel 10 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR10_Msk              (0x1U << EVSYS_INTENSET_OVR10_Pos)             /**< (EVSYS_INTENSET) Channel 10 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR10(value)           (EVSYS_INTENSET_OVR10_Msk & ((value) << EVSYS_INTENSET_OVR10_Pos))
#define EVSYS_INTENSET_OVR11_Pos              (11U)                                          /**< (EVSYS_INTENSET) Channel 11 Overrun Interrupt Enable Position */
#define EVSYS_INTENSET_OVR11_Msk              (0x1U << EVSYS_INTENSET_OVR11_Pos)             /**< (EVSYS_INTENSET) Channel 11 Overrun Interrupt Enable Mask */
#define EVSYS_INTENSET_OVR11(value)           (EVSYS_INTENSET_OVR11_Msk & ((value) << EVSYS_INTENSET_OVR11_Pos))
#define EVSYS_INTENSET_EVD0_Pos               (16U)                                          /**< (EVSYS_INTENSET) Channel 0 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD0_Msk               (0x1U << EVSYS_INTENSET_EVD0_Pos)              /**< (EVSYS_INTENSET) Channel 0 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD0(value)            (EVSYS_INTENSET_EVD0_Msk & ((value) << EVSYS_INTENSET_EVD0_Pos))
#define EVSYS_INTENSET_EVD1_Pos               (17U)                                          /**< (EVSYS_INTENSET) Channel 1 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD1_Msk               (0x1U << EVSYS_INTENSET_EVD1_Pos)              /**< (EVSYS_INTENSET) Channel 1 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD1(value)            (EVSYS_INTENSET_EVD1_Msk & ((value) << EVSYS_INTENSET_EVD1_Pos))
#define EVSYS_INTENSET_EVD2_Pos               (18U)                                          /**< (EVSYS_INTENSET) Channel 2 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD2_Msk               (0x1U << EVSYS_INTENSET_EVD2_Pos)              /**< (EVSYS_INTENSET) Channel 2 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD2(value)            (EVSYS_INTENSET_EVD2_Msk & ((value) << EVSYS_INTENSET_EVD2_Pos))
#define EVSYS_INTENSET_EVD3_Pos               (19U)                                          /**< (EVSYS_INTENSET) Channel 3 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD3_Msk               (0x1U << EVSYS_INTENSET_EVD3_Pos)              /**< (EVSYS_INTENSET) Channel 3 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD3(value)            (EVSYS_INTENSET_EVD3_Msk & ((value) << EVSYS_INTENSET_EVD3_Pos))
#define EVSYS_INTENSET_EVD4_Pos               (20U)                                          /**< (EVSYS_INTENSET) Channel 4 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD4_Msk               (0x1U << EVSYS_INTENSET_EVD4_Pos)              /**< (EVSYS_INTENSET) Channel 4 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD4(value)            (EVSYS_INTENSET_EVD4_Msk & ((value) << EVSYS_INTENSET_EVD4_Pos))
#define EVSYS_INTENSET_EVD5_Pos               (21U)                                          /**< (EVSYS_INTENSET) Channel 5 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD5_Msk               (0x1U << EVSYS_INTENSET_EVD5_Pos)              /**< (EVSYS_INTENSET) Channel 5 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD5(value)            (EVSYS_INTENSET_EVD5_Msk & ((value) << EVSYS_INTENSET_EVD5_Pos))
#define EVSYS_INTENSET_EVD6_Pos               (22U)                                          /**< (EVSYS_INTENSET) Channel 6 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD6_Msk               (0x1U << EVSYS_INTENSET_EVD6_Pos)              /**< (EVSYS_INTENSET) Channel 6 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD6(value)            (EVSYS_INTENSET_EVD6_Msk & ((value) << EVSYS_INTENSET_EVD6_Pos))
#define EVSYS_INTENSET_EVD7_Pos               (23U)                                          /**< (EVSYS_INTENSET) Channel 7 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD7_Msk               (0x1U << EVSYS_INTENSET_EVD7_Pos)              /**< (EVSYS_INTENSET) Channel 7 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD7(value)            (EVSYS_INTENSET_EVD7_Msk & ((value) << EVSYS_INTENSET_EVD7_Pos))
#define EVSYS_INTENSET_EVD8_Pos               (24U)                                          /**< (EVSYS_INTENSET) Channel 8 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD8_Msk               (0x1U << EVSYS_INTENSET_EVD8_Pos)              /**< (EVSYS_INTENSET) Channel 8 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD8(value)            (EVSYS_INTENSET_EVD8_Msk & ((value) << EVSYS_INTENSET_EVD8_Pos))
#define EVSYS_INTENSET_EVD9_Pos               (25U)                                          /**< (EVSYS_INTENSET) Channel 9 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD9_Msk               (0x1U << EVSYS_INTENSET_EVD9_Pos)              /**< (EVSYS_INTENSET) Channel 9 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD9(value)            (EVSYS_INTENSET_EVD9_Msk & ((value) << EVSYS_INTENSET_EVD9_Pos))
#define EVSYS_INTENSET_EVD10_Pos              (26U)                                          /**< (EVSYS_INTENSET) Channel 10 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD10_Msk              (0x1U << EVSYS_INTENSET_EVD10_Pos)             /**< (EVSYS_INTENSET) Channel 10 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD10(value)           (EVSYS_INTENSET_EVD10_Msk & ((value) << EVSYS_INTENSET_EVD10_Pos))
#define EVSYS_INTENSET_EVD11_Pos              (27U)                                          /**< (EVSYS_INTENSET) Channel 11 Event Detection Interrupt Enable Position */
#define EVSYS_INTENSET_EVD11_Msk              (0x1U << EVSYS_INTENSET_EVD11_Pos)             /**< (EVSYS_INTENSET) Channel 11 Event Detection Interrupt Enable Mask */
#define EVSYS_INTENSET_EVD11(value)           (EVSYS_INTENSET_EVD11_Msk & ((value) << EVSYS_INTENSET_EVD11_Pos))
#define EVSYS_INTENSET_Msk                    (0x0FFF0FFFUL)                                 /**< (EVSYS_INTENSET) Register Mask  */

/* -------- EVSYS_INTFLAG : (EVSYS Offset: 0x18) (R/W 32) Interrupt Flag Status and Clear -------- */
#define EVSYS_INTFLAG_OVR0_Pos                (0U)                                           /**< (EVSYS_INTFLAG) Channel 0 Overrun Position */
#define EVSYS_INTFLAG_OVR0_Msk                (0x1U << EVSYS_INTFLAG_OVR0_Pos)               /**< (EVSYS_INTFLAG) Channel 0 Overrun Mask */
#define EVSYS_INTFLAG_OVR0(value)             (EVSYS_INTFLAG_OVR0_Msk & ((value) << EVSYS_INTFLAG_OVR0_Pos))
#define EVSYS_INTFLAG_OVR1_Pos                (1U)                                           /**< (EVSYS_INTFLAG) Channel 1 Overrun Position */
#define EVSYS_INTFLAG_OVR1_Msk                (0x1U << EVSYS_INTFLAG_OVR1_Pos)               /**< (EVSYS_INTFLAG) Channel 1 Overrun Mask */
#define EVSYS_INTFLAG_OVR1(value)             (EVSYS_INTFLAG_OVR1_Msk & ((value) << EVSYS_INTFLAG_OVR1_Pos))
#define EVSYS_INTFLAG_OVR2_Pos                (2U)                                           /**< (EVSYS_INTFLAG) Channel 2 Overrun Position */
#define EVSYS_INTFLAG_OVR2_Msk                (0x1U << EVSYS_INTFLAG_OVR2_Pos)               /**< (EVSYS_INTFLAG) Channel 2 Overrun Mask */
#define EVSYS_INTFLAG_OVR2(value)             (EVSYS_INTFLAG_OVR2_Msk & ((value) << EVSYS_INTFLAG_OVR2_Pos))
#define EVSYS_INTFLAG_OVR3_Pos                (3U)                                           /**< (EVSYS_INTFLAG) Channel 3 Overrun Position */
#define EVSYS_INTFLAG_OVR3_Msk                (0x1U << EVSYS_INTFLAG_OVR3_Pos)               /**< (EVSYS_INTFLAG) Channel 3 Overrun Mask */
#define EVSYS_INTFLAG_OVR3(value)             (EVSYS_INTFLAG_OVR3_Msk & ((value) << EVSYS_INTFLAG_OVR3_Pos))
#define EVSYS_INTFLAG_OVR4_Pos                (4U)                                           /**< (EVSYS_INTFLAG) Channel 4 Overrun Position */
#define EVSYS_INTFLAG_OVR4_Msk                (0x1U << EVSYS_INTFLAG_OVR4_Pos)               /**< (EVSYS_INTFLAG) Channel 4 Overrun Mask */
#define EVSYS_INTFLAG_OVR4(value)             (EVSYS_INTFLAG_OVR4_Msk & ((value) << EVSYS_INTFLAG_OVR4_Pos))
#define EVSYS_INTFLAG_OVR5_Pos                (5U)                                           /**< (EVSYS_INTFLAG) Channel 5 Overrun Position */
#define EVSYS_INTFLAG_OVR5_Msk                (0x1U << EVSYS_INTFLAG_OVR5_Pos)               /**< (EVSYS_INTFLAG) Channel 5 Overrun Mask */
#define EVSYS_INTFLAG_OVR5(value)             (EVSYS_INTFLAG_OVR5_Msk & ((value) << EVSYS_INTFLAG_OVR5_Pos))
#define EVSYS_INTFLAG_OVR6_Pos                (6U)                                           /**< (EVSYS_INTFLAG) Channel 6 Overrun Position */
#define EVSYS_INTFLAG_OVR6_Msk                (0x1U << EVSYS_INTFLAG_OVR6_Pos)               /**< (EVSYS_INTFLAG) Channel 6 Overrun Mask */
#define EVSYS_INTFLAG_OVR6(value)             (EVSYS_INTFLAG_OVR6_Msk & ((value) << EVSYS_INTFLAG_OVR6_Pos))
#define EVSYS_INTFLAG_OVR7_Pos                (7U)                                           /**< (EVSYS_INTFLAG) Channel 7 Overrun Position */
#define EVSYS_INTFLAG_OVR7_Msk                (0x1U << EVSYS_INTFLAG_OVR7_Pos)               /**< (EVSYS_INTFLAG) Channel 7 Overrun Mask */
#define EVSYS_INTFLAG_OVR7(value)             (EVSYS_INTFLAG_OVR7_Msk & ((value) << EVSYS_INTFLAG_OVR7_Pos))
#define EVSYS_INTFLAG_OVR8_Pos                (8U)                                           /**< (EVSYS_INTFLAG) Channel 8 Overrun Position */
#define EVSYS_INTFLAG_OVR8_Msk                (0x1U << EVSYS_INTFLAG_OVR8_Pos)               /**< (EVSYS_INTFLAG) Channel 8 Overrun Mask */
#define EVSYS_INTFLAG_OVR8(value)             (EVSYS_INTFLAG_OVR8_Msk & ((value) << EVSYS_INTFLAG_OVR8_Pos))
#define EVSYS_INTFLAG_OVR9_Pos                (9U)                                           /**< (EVSYS_INTFLAG) Channel 9 Overrun Position */
#define EVSYS_INTFLAG_OVR9_Msk                (0x1U << EVSYS_INTFLAG_OVR9_Pos)               /**< (EVSYS_INTFLAG) Channel 9 Overrun Mask */
#define EVSYS_INTFLAG_OVR9(value)             (EVSYS_INTFLAG_OVR9_Msk & ((value) << EVSYS_INTFLAG_OVR9_Pos))
#define EVSYS_INTFLAG_OVR10_Pos               (10U)                                          /**< (EVSYS_INTFLAG) Channel 10 Overrun Position */
#define EVSYS_INTFLAG_OVR10_Msk               (0x1U << EVSYS_INTFLAG_OVR10_Pos)              /**< (EVSYS_INTFLAG) Channel 10 Overrun Mask */
#define EVSYS_INTFLAG_OVR10(value)            (EVSYS_INTFLAG_OVR10_Msk & ((value) << EVSYS_INTFLAG_OVR10_Pos))
#define EVSYS_INTFLAG_OVR11_Pos               (11U)                                          /**< (EVSYS_INTFLAG) Channel 11 Overrun Position */
#define EVSYS_INTFLAG_OVR11_Msk               (0x1U << EVSYS_INTFLAG_OVR11_Pos)              /**< (EVSYS_INTFLAG) Channel 11 Overrun Mask */
#define EVSYS_INTFLAG_OVR11(value)            (EVSYS_INTFLAG_OVR11_Msk & ((value) << EVSYS_INTFLAG_OVR11_Pos))
#define EVSYS_INTFLAG_EVD0_Pos                (16U)                                          /**< (EVSYS_INTFLAG) Channel 0 Event Detection Position */
#define EVSYS_INTFLAG_EVD0_Msk                (0x1U << EVSYS_INTFLAG_EVD0_Pos)               /**< (EVSYS_INTFLAG) Channel 0 Event Detection Mask */
#define EVSYS_INTFLAG_EVD0(value)             (EVSYS_INTFLAG_EVD0_Msk & ((value) << EVSYS_INTFLAG_EVD0_Pos))
#define EVSYS_INTFLAG_EVD1_Pos                (17U)                                          /**< (EVSYS_INTFLAG) Channel 1 Event Detection Position */
#define EVSYS_INTFLAG_EVD1_Msk                (0x1U << EVSYS_INTFLAG_EVD1_Pos)               /**< (EVSYS_INTFLAG) Channel 1 Event Detection Mask */
#define EVSYS_INTFLAG_EVD1(value)             (EVSYS_INTFLAG_EVD1_Msk & ((value) << EVSYS_INTFLAG_EVD1_Pos))
#define EVSYS_INTFLAG_EVD2_Pos                (18U)                                          /**< (EVSYS_INTFLAG) Channel 2 Event Detection Position */
#define EVSYS_INTFLAG_EVD2_Msk                (0x1U << EVSYS_INTFLAG_EVD2_Pos)               /**< (EVSYS_INTFLAG) Channel 2 Event Detection Mask */
#define EVSYS_INTFLAG_EVD2(value)             (EVSYS_INTFLAG_EVD2_Msk & ((value) << EVSYS_INTFLAG_EVD2_Pos))
#define EVSYS_INTFLAG_EVD3_Pos                (19U)                                          /**< (EVSYS_INTFLAG) Channel 3 Event Detection Position */
#define EVSYS_INTFLAG_EVD3_Msk                (0x1U << EVSYS_INTFLAG_EVD3_Pos)               /**< (EVSYS_INTFLAG) Channel 3 Event Detection Mask */
#define EVSYS_INTFLAG_EVD3(value)             (EVSYS_INTFLAG_EVD3_Msk & ((value) << EVSYS_INTFLAG_EVD3_Pos))
#define EVSYS_INTFLAG_EVD4_Pos                (20U)                                          /**< (EVSYS_INTFLAG) Channel 4 Event Detection Position */
#define EVSYS_INTFLAG_EVD4_Msk                (0x1U << EVSYS_INTFLAG_EVD4_Pos)               /**< (EVSYS_INTFLAG) Channel 4 Event Detection Mask */
#define EVSYS_INTFLAG_EVD4(value)             (EVSYS_INTFLAG_EVD4_Msk & ((value) << EVSYS_INTFLAG_EVD4_Pos))
#define EVSYS_INTFLAG_EVD5_Pos                (21U)                                          /**< (EVSYS_INTFLAG) Channel 5 Event Detection Position */
#define EVSYS_INTFLAG_EVD5_Msk                (0x1U << EVSYS_INTFLAG_EVD5_Pos)               /**< (EVSYS_INTFLAG) Channel 5 Event Detection Mask */
#define EVSYS_INTFLAG_EVD5(value)             (EVSYS_INTFLAG_EVD5_Msk & ((value) << EVSYS_INTFLAG_EVD5_Pos))
#define EVSYS_INTFLAG_EVD6_Pos                (22U)                                          /**< (EVSYS_INTFLAG) Channel 6 Event Detection Position */
#define EVSYS_INTFLAG_EVD6_Msk                (0x1U << EVSYS_INTFLAG_EVD6_Pos)               /**< (EVSYS_INTFLAG) Channel 6 Event Detection Mask */
#define EVSYS_INTFLAG_EVD6(value)             (EVSYS_INTFLAG_EVD6_Msk & ((value) << EVSYS_INTFLAG_EVD6_Pos))
#define EVSYS_INTFLAG_EVD7_Pos                (23U)                                          /**< (EVSYS_INTFLAG) Channel 7 Event Detection Position */
#define EVSYS_INTFLAG_EVD7_Msk                (0x1U << EVSYS_INTFLAG_EVD7_Pos)               /**< (EVSYS_INTFLAG) Channel 7 Event Detection Mask */
#define EVSYS_INTFLAG_EVD7(value)             (EVSYS_INTFLAG_EVD7_Msk & ((value) << EVSYS_INTFLAG_EVD7_Pos))
#define EVSYS_INTFLAG_EVD8_Pos                (24U)                                          /**< (EVSYS_INTFLAG) Channel 8 Event Detection Position */
#define EVSYS_INTFLAG_EVD8_Msk                (0x1U << EVSYS_INTFLAG_EVD8_Pos)               /**< (EVSYS_INTFLAG) Channel 8 Event Detection Mask */
#define EVSYS_INTFLAG_EVD8(value)             (EVSYS_INTFLAG_EVD8_Msk & ((value) << EVSYS_INTFLAG_EVD8_Pos))
#define EVSYS_INTFLAG_EVD9_Pos                (25U)                                          /**< (EVSYS_INTFLAG) Channel 9 Event Detection Position */
#define EVSYS_INTFLAG_EVD9_Msk                (0x1U << EVSYS_INTFLAG_EVD9_Pos)               /**< (EVSYS_INTFLAG) Channel 9 Event Detection Mask */
#define EVSYS_INTFLAG_EVD9(value)             (EVSYS_INTFLAG_EVD9_Msk & ((value) << EVSYS_INTFLAG_EVD9_Pos))
#define EVSYS_INTFLAG_EVD10_Pos               (26U)                                          /**< (EVSYS_INTFLAG) Channel 10 Event Detection Position */
#define EVSYS_INTFLAG_EVD10_Msk               (0x1U << EVSYS_INTFLAG_EVD10_Pos)              /**< (EVSYS_INTFLAG) Channel 10 Event Detection Mask */
#define EVSYS_INTFLAG_EVD10(value)            (EVSYS_INTFLAG_EVD10_Msk & ((value) << EVSYS_INTFLAG_EVD10_Pos))
#define EVSYS_INTFLAG_EVD11_Pos               (27U)                                          /**< (EVSYS_INTFLAG) Channel 11 Event Detection Position */
#define EVSYS_INTFLAG_EVD11_Msk               (0x1U << EVSYS_INTFLAG_EVD11_Pos)              /**< (EVSYS_INTFLAG) Channel 11 Event Detection Mask */
#define EVSYS_INTFLAG_EVD11(value)            (EVSYS_INTFLAG_EVD11_Msk & ((value) << EVSYS_INTFLAG_EVD11_Pos))
#define EVSYS_INTFLAG_Msk                     (0x0FFF0FFFUL)                                 /**< (EVSYS_INTFLAG) Register Mask  */

/* -------- EVSYS_SWEVT : (EVSYS Offset: 0x1C) ( /W 32) Software Event -------- */
#define EVSYS_SWEVT_CHANNEL0_Pos              (0U)                                           /**< (EVSYS_SWEVT) Channel 0 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL0_Msk              (0x1U << EVSYS_SWEVT_CHANNEL0_Pos)             /**< (EVSYS_SWEVT) Channel 0 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL0(value)           (EVSYS_SWEVT_CHANNEL0_Msk & ((value) << EVSYS_SWEVT_CHANNEL0_Pos))
#define EVSYS_SWEVT_CHANNEL1_Pos              (1U)                                           /**< (EVSYS_SWEVT) Channel 1 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL1_Msk              (0x1U << EVSYS_SWEVT_CHANNEL1_Pos)             /**< (EVSYS_SWEVT) Channel 1 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL1(value)           (EVSYS_SWEVT_CHANNEL1_Msk & ((value) << EVSYS_SWEVT_CHANNEL1_Pos))
#define EVSYS_SWEVT_CHANNEL2_Pos              (2U)                                           /**< (EVSYS_SWEVT) Channel 2 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL2_Msk              (0x1U << EVSYS_SWEVT_CHANNEL2_Pos)             /**< (EVSYS_SWEVT) Channel 2 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL2(value)           (EVSYS_SWEVT_CHANNEL2_Msk & ((value) << EVSYS_SWEVT_CHANNEL2_Pos))
#define EVSYS_SWEVT_CHANNEL3_Pos              (3U)                                           /**< (EVSYS_SWEVT) Channel 3 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL3_Msk              (0x1U << EVSYS_SWEVT_CHANNEL3_Pos)             /**< (EVSYS_SWEVT) Channel 3 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL3(value)           (EVSYS_SWEVT_CHANNEL3_Msk & ((value) << EVSYS_SWEVT_CHANNEL3_Pos))
#define EVSYS_SWEVT_CHANNEL4_Pos              (4U)                                           /**< (EVSYS_SWEVT) Channel 4 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL4_Msk              (0x1U << EVSYS_SWEVT_CHANNEL4_Pos)             /**< (EVSYS_SWEVT) Channel 4 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL4(value)           (EVSYS_SWEVT_CHANNEL4_Msk & ((value) << EVSYS_SWEVT_CHANNEL4_Pos))
#define EVSYS_SWEVT_CHANNEL5_Pos              (5U)                                           /**< (EVSYS_SWEVT) Channel 5 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL5_Msk              (0x1U << EVSYS_SWEVT_CHANNEL5_Pos)             /**< (EVSYS_SWEVT) Channel 5 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL5(value)           (EVSYS_SWEVT_CHANNEL5_Msk & ((value) << EVSYS_SWEVT_CHANNEL5_Pos))
#define EVSYS_SWEVT_CHANNEL6_Pos              (6U)                                           /**< (EVSYS_SWEVT) Channel 6 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL6_Msk              (0x1U << EVSYS_SWEVT_CHANNEL6_Pos)             /**< (EVSYS_SWEVT) Channel 6 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL6(value)           (EVSYS_SWEVT_CHANNEL6_Msk & ((value) << EVSYS_SWEVT_CHANNEL6_Pos))
#define EVSYS_SWEVT_CHANNEL7_Pos              (7U)                                           /**< (EVSYS_SWEVT) Channel 7 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL7_Msk              (0x1U << EVSYS_SWEVT_CHANNEL7_Pos)             /**< (EVSYS_SWEVT) Channel 7 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL7(value)           (EVSYS_SWEVT_CHANNEL7_Msk & ((value) << EVSYS_SWEVT_CHANNEL7_Pos))
#define EVSYS_SWEVT_CHANNEL8_Pos              (8U)                                           /**< (EVSYS_SWEVT) Channel 8 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL8_Msk              (0x1U << EVSYS_SWEVT_CHANNEL8_Pos)             /**< (EVSYS_SWEVT) Channel 8 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL8(value)           (EVSYS_SWEVT_CHANNEL8_Msk & ((value) << EVSYS_SWEVT_CHANNEL8_Pos))
#define EVSYS_SWEVT_CHANNEL9_Pos              (9U)                                           /**< (EVSYS_SWEVT) Channel 9 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL9_Msk              (0x1U << EVSYS_SWEVT_CHANNEL9_Pos)             /**< (EVSYS_SWEVT) Channel 9 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL9(value)           (EVSYS_SWEVT_CHANNEL9_Msk & ((value) << EVSYS_SWEVT_CHANNEL9_Pos))
#define EVSYS_SWEVT_CHANNEL10_Pos             (10U)                                          /**< (EVSYS_SWEVT) Channel 10 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL10_Msk             (0x1U << EVSYS_SWEVT_CHANNEL10_Pos)            /**< (EVSYS_SWEVT) Channel 10 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL10(value)          (EVSYS_SWEVT_CHANNEL10_Msk & ((value) << EVSYS_SWEVT_CHANNEL10_Pos))
#define EVSYS_SWEVT_CHANNEL11_Pos             (11U)                                          /**< (EVSYS_SWEVT) Channel 11 Software Selection Position */
#define EVSYS_SWEVT_CHANNEL11_Msk             (0x1U << EVSYS_SWEVT_CHANNEL11_Pos)            /**< (EVSYS_SWEVT) Channel 11 Software Selection Mask */
#define EVSYS_SWEVT_CHANNEL11(value)          (EVSYS_SWEVT_CHANNEL11_Msk & ((value) << EVSYS_SWEVT_CHANNEL11_Pos))
#define EVSYS_SWEVT_Msk                       (0x00000FFFUL)                                 /**< (EVSYS_SWEVT) Register Mask  */

/* -------- EVSYS_CHANNEL : (EVSYS Offset: 0x20) (R/W 32) Channel n -------- */
#define EVSYS_CHANNEL_EVGEN_Pos               (0U)                                           /**< (EVSYS_CHANNEL) Event Generator Selection Position */
#define EVSYS_CHANNEL_EVGEN_Msk               (0x7FU << EVSYS_CHANNEL_EVGEN_Pos)             /**< (EVSYS_CHANNEL) Event Generator Selection Mask */
#define EVSYS_CHANNEL_EVGEN(value)            (EVSYS_CHANNEL_EVGEN_Msk & ((value) << EVSYS_CHANNEL_EVGEN_Pos))
#define EVSYS_CHANNEL_PATH_Pos                (8U)                                           /**< (EVSYS_CHANNEL) Path Selection Position */
#define EVSYS_CHANNEL_PATH_Msk                (0x3U << EVSYS_CHANNEL_PATH_Pos)               /**< (EVSYS_CHANNEL) Path Selection Mask */
#define EVSYS_CHANNEL_PATH(value)             (EVSYS_CHANNEL_PATH_Msk & ((value) << EVSYS_CHANNEL_PATH_Pos))
#define   EVSYS_CHANNEL_PATH_SYNCHRONOUS_Val  (0U)                                           /**< (EVSYS_CHANNEL) Synchronous path  */
#define   EVSYS_CHANNEL_PATH_RESYNCHRONIZED_Val (1U)                                           /**< (EVSYS_CHANNEL) Resynchronized path  */
#define   EVSYS_CHANNEL_PATH_ASYNCHRONOUS_Val (2U)                                           /**< (EVSYS_CHANNEL) Asynchronous path  */
#define EVSYS_CHANNEL_PATH_SYNCHRONOUS        (EVSYS_CHANNEL_PATH_SYNCHRONOUS_Val << EVSYS_CHANNEL_PATH_Pos) /**< (EVSYS_CHANNEL) Synchronous path Position  */
#define EVSYS_CHANNEL_PATH_RESYNCHRONIZED     (EVSYS_CHANNEL_PATH_RESYNCHRONIZED_Val << EVSYS_CHANNEL_PATH_Pos) /**< (EVSYS_CHANNEL) Resynchronized path Position  */
#define EVSYS_CHANNEL_PATH_ASYNCHRONOUS       (EVSYS_CHANNEL_PATH_ASYNCHRONOUS_Val << EVSYS_CHANNEL_PATH_Pos) /**< (EVSYS_CHANNEL) Asynchronous path Position  */
#define EVSYS_CHANNEL_EDGSEL_Pos              (10U)                                          /**< (EVSYS_CHANNEL) Edge Detection Selection Position */
#define EVSYS_CHANNEL_EDGSEL_Msk              (0x3U << EVSYS_CHANNEL_EDGSEL_Pos)             /**< (EVSYS_CHANNEL) Edge Detection Selection Mask */
#define EVSYS_CHANNEL_EDGSEL(value)           (EVSYS_CHANNEL_EDGSEL_Msk & ((value) << EVSYS_CHANNEL_EDGSEL_Pos))
#define   EVSYS_CHANNEL_EDGSEL_NO_EVT_OUTPUT_Val (0U)                                           /**< (EVSYS_CHANNEL) No event output when using the resynchronized or synchronous path  */
#define   EVSYS_CHANNEL_EDGSEL_RISING_EDGE_Val (1U)                                           /**< (EVSYS_CHANNEL) Event detection only on the rising edge of the signal from the event generator when using the resynchronized or synchronous path  */
#define   EVSYS_CHANNEL_EDGSEL_FALLING_EDGE_Val (2U)                                           /**< (EVSYS_CHANNEL) Event detection only on the falling edge of the signal from the event generator when using the resynchronized or synchronous path  */
#define   EVSYS_CHANNEL_EDGSEL_BOTH_EDGES_Val (3U)                                           /**< (EVSYS_CHANNEL) Event detection on rising and falling edges of the signal from the event generator when using the resynchronized or synchronous path  */
#define EVSYS_CHANNEL_EDGSEL_NO_EVT_OUTPUT    (EVSYS_CHANNEL_EDGSEL_NO_EVT_OUTPUT_Val << EVSYS_CHANNEL_EDGSEL_Pos) /**< (EVSYS_CHANNEL) No event output when using the resynchronized or synchronous path Position  */
#define EVSYS_CHANNEL_EDGSEL_RISING_EDGE      (EVSYS_CHANNEL_EDGSEL_RISING_EDGE_Val << EVSYS_CHANNEL_EDGSEL_Pos) /**< (EVSYS_CHANNEL) Event detection only on the rising edge of the signal from the event generator when using the resynchronized or synchronous path Position  */
#define EVSYS_CHANNEL_EDGSEL_FALLING_EDGE     (EVSYS_CHANNEL_EDGSEL_FALLING_EDGE_Val << EVSYS_CHANNEL_EDGSEL_Pos) /**< (EVSYS_CHANNEL) Event detection only on the falling edge of the signal from the event generator when using the resynchronized or synchronous path Position  */
#define EVSYS_CHANNEL_EDGSEL_BOTH_EDGES       (EVSYS_CHANNEL_EDGSEL_BOTH_EDGES_Val << EVSYS_CHANNEL_EDGSEL_Pos) /**< (EVSYS_CHANNEL) Event detection on rising and falling edges of the signal from the event generator when using the resynchronized or synchronous path Position  */
#define EVSYS_CHANNEL_RUNSTDBY_Pos            (14U)                                          /**< (EVSYS_CHANNEL) Run in standby Position */
#define EVSYS_CHANNEL_RUNSTDBY_Msk            (0x1U << EVSYS_CHANNEL_RUNSTDBY_Pos)           /**< (EVSYS_CHANNEL) Run in standby Mask */
#define EVSYS_CHANNEL_RUNSTDBY(value)         (EVSYS_CHANNEL_RUNSTDBY_Msk & ((value) << EVSYS_CHANNEL_RUNSTDBY_Pos))
#define EVSYS_CHANNEL_ONDEMAND_Pos            (15U)                                          /**< (EVSYS_CHANNEL) Generic Clock On Demand Position */
#define EVSYS_CHANNEL_ONDEMAND_Msk            (0x1U << EVSYS_CHANNEL_ONDEMAND_Pos)           /**< (EVSYS_CHANNEL) Generic Clock On Demand Mask */
#define EVSYS_CHANNEL_ONDEMAND(value)         (EVSYS_CHANNEL_ONDEMAND_Msk & ((value) << EVSYS_CHANNEL_ONDEMAND_Pos))
#define EVSYS_CHANNEL_Msk                     (0x0000CF7FUL)                                 /**< (EVSYS_CHANNEL) Register Mask  */

/* -------- EVSYS_USER : (EVSYS Offset: 0x80) (R/W 32) User Multiplexer n -------- */
#define EVSYS_USER_CHANNEL_Pos                (0U)                                           /**< (EVSYS_USER) Channel Event Selection Position */
#define EVSYS_USER_CHANNEL_Msk                (0x1FU << EVSYS_USER_CHANNEL_Pos)              /**< (EVSYS_USER) Channel Event Selection Mask */
#define EVSYS_USER_CHANNEL(value)             (EVSYS_USER_CHANNEL_Msk & ((value) << EVSYS_USER_CHANNEL_Pos))
#define EVSYS_USER_Msk                        (0x0000001FUL)                                 /**< (EVSYS_USER) Register Mask  */

/** \brief EVSYS register offsets definitions */
#define EVSYS_CTRLA_OFFSET             (0x00)         /**< (EVSYS_CTRLA) Control Offset */
#define EVSYS_CHSTATUS_OFFSET          (0x0C)         /**< (EVSYS_CHSTATUS) Channel Status Offset */
#define EVSYS_INTENCLR_OFFSET          (0x10)         /**< (EVSYS_INTENCLR) Interrupt Enable Clear Offset */
#define EVSYS_INTENSET_OFFSET          (0x14)         /**< (EVSYS_INTENSET) Interrupt Enable Set Offset */
#define EVSYS_INTFLAG_OFFSET           (0x18)         /**< (EVSYS_INTFLAG) Interrupt Flag Status and Clear Offset */
#define EVSYS_SWEVT_OFFSET             (0x1C)         /**< (EVSYS_SWEVT) Software Event Offset */
#define EVSYS_CHANNEL_OFFSET           (0x20)         /**< (EVSYS_CHANNEL) Channel n Offset */
#define EVSYS_USER_OFFSET              (0x80)         /**< (EVSYS_USER) User Multiplexer n Offset */

/** \brief EVSYS register API structure */
typedef struct
{
  __IO  uint8_t                        EVSYS_CTRLA;     /**< Offset: 0x00 (R/W  8) Control */
  __I   uint8_t                        Reserved1[0x0B];
  __I   uint32_t                       EVSYS_CHSTATUS;  /**< Offset: 0x0c (R/   32) Channel Status */
  __IO  uint32_t                       EVSYS_INTENCLR;  /**< Offset: 0x10 (R/W  32) Interrupt Enable Clear */
  __IO  uint32_t                       EVSYS_INTENSET;  /**< Offset: 0x14 (R/W  32) Interrupt Enable Set */
  __IO  uint32_t                       EVSYS_INTFLAG;   /**< Offset: 0x18 (R/W  32) Interrupt Flag Status and Clear */
  __O   uint32_t                       EVSYS_SWEVT;     /**< Offset: 0x1c ( /W  32) Software Event */
  __IO  uint32_t                       EVSYS_CHANNEL[12]; /**< Offset: 0x20 (R/W  32) Channel n */
  __I   uint8_t                        Reserved2[0x30];
  __IO  uint32_t                       EVSYS_USER[50];  /**< Offset: 0x80 (R/W  32) User Multiplexer n */
} evsys_registers_t;
/** @}  end of Event System Interface */

#endif /* SAMC_SAMC21_EVSYS_MODULE_H */

