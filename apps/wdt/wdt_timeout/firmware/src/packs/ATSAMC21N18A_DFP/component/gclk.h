/**
 * \brief Header file for SAMC/SAMC21 GCLK
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
#ifndef SAMC_SAMC21_GCLK_MODULE_H
#define SAMC_SAMC21_GCLK_MODULE_H

/** \addtogroup SAMC_SAMC21 Generic Clock Generator
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_GCLK                                  */
/* ========================================================================== */

/* -------- GCLK_CTRLA : (GCLK Offset: 0x00) (R/W 8) Control -------- */
#define GCLK_CTRLA_SWRST_Pos                  (0U)                                           /**< (GCLK_CTRLA) Software Reset Position */
#define GCLK_CTRLA_SWRST_Msk                  (0x1U << GCLK_CTRLA_SWRST_Pos)                 /**< (GCLK_CTRLA) Software Reset Mask */
#define GCLK_CTRLA_SWRST(value)               (GCLK_CTRLA_SWRST_Msk & ((value) << GCLK_CTRLA_SWRST_Pos))
#define GCLK_CTRLA_Msk                        (0x00000001UL)                                 /**< (GCLK_CTRLA) Register Mask  */

/* -------- GCLK_SYNCBUSY : (GCLK Offset: 0x04) (R/  32) Synchronization Busy -------- */
#define GCLK_SYNCBUSY_SWRST_Pos               (0U)                                           /**< (GCLK_SYNCBUSY) Software Reset Synchroniation Busy bit Position */
#define GCLK_SYNCBUSY_SWRST_Msk               (0x1U << GCLK_SYNCBUSY_SWRST_Pos)              /**< (GCLK_SYNCBUSY) Software Reset Synchroniation Busy bit Mask */
#define GCLK_SYNCBUSY_SWRST(value)            (GCLK_SYNCBUSY_SWRST_Msk & ((value) << GCLK_SYNCBUSY_SWRST_Pos))
#define GCLK_SYNCBUSY_GENCTRL0_Pos            (2U)                                           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 0 Synchronization Busy bits Position */
#define GCLK_SYNCBUSY_GENCTRL0_Msk            (0x1U << GCLK_SYNCBUSY_GENCTRL0_Pos)           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 0 Synchronization Busy bits Mask */
#define GCLK_SYNCBUSY_GENCTRL0(value)         (GCLK_SYNCBUSY_GENCTRL0_Msk & ((value) << GCLK_SYNCBUSY_GENCTRL0_Pos))
#define   GCLK_SYNCBUSY_GENCTRL0_GCLK0_Val    (1U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 0  */
#define   GCLK_SYNCBUSY_GENCTRL0_GCLK1_Val    (2U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 1  */
#define   GCLK_SYNCBUSY_GENCTRL0_GCLK2_Val    (4U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 2  */
#define   GCLK_SYNCBUSY_GENCTRL0_GCLK3_Val    (8U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 3  */
#define   GCLK_SYNCBUSY_GENCTRL0_GCLK4_Val    (16U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 4  */
#define   GCLK_SYNCBUSY_GENCTRL0_GCLK5_Val    (32U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 5  */
#define   GCLK_SYNCBUSY_GENCTRL0_GCLK6_Val    (64U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 6  */
#define   GCLK_SYNCBUSY_GENCTRL0_GCLK7_Val    (128U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 7  */
#define   GCLK_SYNCBUSY_GENCTRL0_GCLK8_Val    (256U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 8  */
#define GCLK_SYNCBUSY_GENCTRL0_GCLK0          (GCLK_SYNCBUSY_GENCTRL0_GCLK0_Val << GCLK_SYNCBUSY_GENCTRL0_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 0 Position  */
#define GCLK_SYNCBUSY_GENCTRL0_GCLK1          (GCLK_SYNCBUSY_GENCTRL0_GCLK1_Val << GCLK_SYNCBUSY_GENCTRL0_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 1 Position  */
#define GCLK_SYNCBUSY_GENCTRL0_GCLK2          (GCLK_SYNCBUSY_GENCTRL0_GCLK2_Val << GCLK_SYNCBUSY_GENCTRL0_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 2 Position  */
#define GCLK_SYNCBUSY_GENCTRL0_GCLK3          (GCLK_SYNCBUSY_GENCTRL0_GCLK3_Val << GCLK_SYNCBUSY_GENCTRL0_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 3 Position  */
#define GCLK_SYNCBUSY_GENCTRL0_GCLK4          (GCLK_SYNCBUSY_GENCTRL0_GCLK4_Val << GCLK_SYNCBUSY_GENCTRL0_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 4 Position  */
#define GCLK_SYNCBUSY_GENCTRL0_GCLK5          (GCLK_SYNCBUSY_GENCTRL0_GCLK5_Val << GCLK_SYNCBUSY_GENCTRL0_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 5 Position  */
#define GCLK_SYNCBUSY_GENCTRL0_GCLK6          (GCLK_SYNCBUSY_GENCTRL0_GCLK6_Val << GCLK_SYNCBUSY_GENCTRL0_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 6 Position  */
#define GCLK_SYNCBUSY_GENCTRL0_GCLK7          (GCLK_SYNCBUSY_GENCTRL0_GCLK7_Val << GCLK_SYNCBUSY_GENCTRL0_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 7 Position  */
#define GCLK_SYNCBUSY_GENCTRL0_GCLK8          (GCLK_SYNCBUSY_GENCTRL0_GCLK8_Val << GCLK_SYNCBUSY_GENCTRL0_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 8 Position  */
#define GCLK_SYNCBUSY_GENCTRL1_Pos            (3U)                                           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 1 Synchronization Busy bits Position */
#define GCLK_SYNCBUSY_GENCTRL1_Msk            (0x1U << GCLK_SYNCBUSY_GENCTRL1_Pos)           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 1 Synchronization Busy bits Mask */
#define GCLK_SYNCBUSY_GENCTRL1(value)         (GCLK_SYNCBUSY_GENCTRL1_Msk & ((value) << GCLK_SYNCBUSY_GENCTRL1_Pos))
#define   GCLK_SYNCBUSY_GENCTRL1_GCLK0_Val    (1U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 0  */
#define   GCLK_SYNCBUSY_GENCTRL1_GCLK1_Val    (2U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 1  */
#define   GCLK_SYNCBUSY_GENCTRL1_GCLK2_Val    (4U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 2  */
#define   GCLK_SYNCBUSY_GENCTRL1_GCLK3_Val    (8U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 3  */
#define   GCLK_SYNCBUSY_GENCTRL1_GCLK4_Val    (16U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 4  */
#define   GCLK_SYNCBUSY_GENCTRL1_GCLK5_Val    (32U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 5  */
#define   GCLK_SYNCBUSY_GENCTRL1_GCLK6_Val    (64U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 6  */
#define   GCLK_SYNCBUSY_GENCTRL1_GCLK7_Val    (128U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 7  */
#define   GCLK_SYNCBUSY_GENCTRL1_GCLK8_Val    (256U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 8  */
#define GCLK_SYNCBUSY_GENCTRL1_GCLK0          (GCLK_SYNCBUSY_GENCTRL1_GCLK0_Val << GCLK_SYNCBUSY_GENCTRL1_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 0 Position  */
#define GCLK_SYNCBUSY_GENCTRL1_GCLK1          (GCLK_SYNCBUSY_GENCTRL1_GCLK1_Val << GCLK_SYNCBUSY_GENCTRL1_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 1 Position  */
#define GCLK_SYNCBUSY_GENCTRL1_GCLK2          (GCLK_SYNCBUSY_GENCTRL1_GCLK2_Val << GCLK_SYNCBUSY_GENCTRL1_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 2 Position  */
#define GCLK_SYNCBUSY_GENCTRL1_GCLK3          (GCLK_SYNCBUSY_GENCTRL1_GCLK3_Val << GCLK_SYNCBUSY_GENCTRL1_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 3 Position  */
#define GCLK_SYNCBUSY_GENCTRL1_GCLK4          (GCLK_SYNCBUSY_GENCTRL1_GCLK4_Val << GCLK_SYNCBUSY_GENCTRL1_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 4 Position  */
#define GCLK_SYNCBUSY_GENCTRL1_GCLK5          (GCLK_SYNCBUSY_GENCTRL1_GCLK5_Val << GCLK_SYNCBUSY_GENCTRL1_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 5 Position  */
#define GCLK_SYNCBUSY_GENCTRL1_GCLK6          (GCLK_SYNCBUSY_GENCTRL1_GCLK6_Val << GCLK_SYNCBUSY_GENCTRL1_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 6 Position  */
#define GCLK_SYNCBUSY_GENCTRL1_GCLK7          (GCLK_SYNCBUSY_GENCTRL1_GCLK7_Val << GCLK_SYNCBUSY_GENCTRL1_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 7 Position  */
#define GCLK_SYNCBUSY_GENCTRL1_GCLK8          (GCLK_SYNCBUSY_GENCTRL1_GCLK8_Val << GCLK_SYNCBUSY_GENCTRL1_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 8 Position  */
#define GCLK_SYNCBUSY_GENCTRL2_Pos            (4U)                                           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 2 Synchronization Busy bits Position */
#define GCLK_SYNCBUSY_GENCTRL2_Msk            (0x1U << GCLK_SYNCBUSY_GENCTRL2_Pos)           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 2 Synchronization Busy bits Mask */
#define GCLK_SYNCBUSY_GENCTRL2(value)         (GCLK_SYNCBUSY_GENCTRL2_Msk & ((value) << GCLK_SYNCBUSY_GENCTRL2_Pos))
#define   GCLK_SYNCBUSY_GENCTRL2_GCLK0_Val    (1U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 0  */
#define   GCLK_SYNCBUSY_GENCTRL2_GCLK1_Val    (2U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 1  */
#define   GCLK_SYNCBUSY_GENCTRL2_GCLK2_Val    (4U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 2  */
#define   GCLK_SYNCBUSY_GENCTRL2_GCLK3_Val    (8U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 3  */
#define   GCLK_SYNCBUSY_GENCTRL2_GCLK4_Val    (16U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 4  */
#define   GCLK_SYNCBUSY_GENCTRL2_GCLK5_Val    (32U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 5  */
#define   GCLK_SYNCBUSY_GENCTRL2_GCLK6_Val    (64U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 6  */
#define   GCLK_SYNCBUSY_GENCTRL2_GCLK7_Val    (128U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 7  */
#define   GCLK_SYNCBUSY_GENCTRL2_GCLK8_Val    (256U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 8  */
#define GCLK_SYNCBUSY_GENCTRL2_GCLK0          (GCLK_SYNCBUSY_GENCTRL2_GCLK0_Val << GCLK_SYNCBUSY_GENCTRL2_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 0 Position  */
#define GCLK_SYNCBUSY_GENCTRL2_GCLK1          (GCLK_SYNCBUSY_GENCTRL2_GCLK1_Val << GCLK_SYNCBUSY_GENCTRL2_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 1 Position  */
#define GCLK_SYNCBUSY_GENCTRL2_GCLK2          (GCLK_SYNCBUSY_GENCTRL2_GCLK2_Val << GCLK_SYNCBUSY_GENCTRL2_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 2 Position  */
#define GCLK_SYNCBUSY_GENCTRL2_GCLK3          (GCLK_SYNCBUSY_GENCTRL2_GCLK3_Val << GCLK_SYNCBUSY_GENCTRL2_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 3 Position  */
#define GCLK_SYNCBUSY_GENCTRL2_GCLK4          (GCLK_SYNCBUSY_GENCTRL2_GCLK4_Val << GCLK_SYNCBUSY_GENCTRL2_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 4 Position  */
#define GCLK_SYNCBUSY_GENCTRL2_GCLK5          (GCLK_SYNCBUSY_GENCTRL2_GCLK5_Val << GCLK_SYNCBUSY_GENCTRL2_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 5 Position  */
#define GCLK_SYNCBUSY_GENCTRL2_GCLK6          (GCLK_SYNCBUSY_GENCTRL2_GCLK6_Val << GCLK_SYNCBUSY_GENCTRL2_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 6 Position  */
#define GCLK_SYNCBUSY_GENCTRL2_GCLK7          (GCLK_SYNCBUSY_GENCTRL2_GCLK7_Val << GCLK_SYNCBUSY_GENCTRL2_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 7 Position  */
#define GCLK_SYNCBUSY_GENCTRL2_GCLK8          (GCLK_SYNCBUSY_GENCTRL2_GCLK8_Val << GCLK_SYNCBUSY_GENCTRL2_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 8 Position  */
#define GCLK_SYNCBUSY_GENCTRL3_Pos            (5U)                                           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 3 Synchronization Busy bits Position */
#define GCLK_SYNCBUSY_GENCTRL3_Msk            (0x1U << GCLK_SYNCBUSY_GENCTRL3_Pos)           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 3 Synchronization Busy bits Mask */
#define GCLK_SYNCBUSY_GENCTRL3(value)         (GCLK_SYNCBUSY_GENCTRL3_Msk & ((value) << GCLK_SYNCBUSY_GENCTRL3_Pos))
#define   GCLK_SYNCBUSY_GENCTRL3_GCLK0_Val    (1U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 0  */
#define   GCLK_SYNCBUSY_GENCTRL3_GCLK1_Val    (2U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 1  */
#define   GCLK_SYNCBUSY_GENCTRL3_GCLK2_Val    (4U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 2  */
#define   GCLK_SYNCBUSY_GENCTRL3_GCLK3_Val    (8U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 3  */
#define   GCLK_SYNCBUSY_GENCTRL3_GCLK4_Val    (16U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 4  */
#define   GCLK_SYNCBUSY_GENCTRL3_GCLK5_Val    (32U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 5  */
#define   GCLK_SYNCBUSY_GENCTRL3_GCLK6_Val    (64U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 6  */
#define   GCLK_SYNCBUSY_GENCTRL3_GCLK7_Val    (128U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 7  */
#define   GCLK_SYNCBUSY_GENCTRL3_GCLK8_Val    (256U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 8  */
#define GCLK_SYNCBUSY_GENCTRL3_GCLK0          (GCLK_SYNCBUSY_GENCTRL3_GCLK0_Val << GCLK_SYNCBUSY_GENCTRL3_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 0 Position  */
#define GCLK_SYNCBUSY_GENCTRL3_GCLK1          (GCLK_SYNCBUSY_GENCTRL3_GCLK1_Val << GCLK_SYNCBUSY_GENCTRL3_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 1 Position  */
#define GCLK_SYNCBUSY_GENCTRL3_GCLK2          (GCLK_SYNCBUSY_GENCTRL3_GCLK2_Val << GCLK_SYNCBUSY_GENCTRL3_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 2 Position  */
#define GCLK_SYNCBUSY_GENCTRL3_GCLK3          (GCLK_SYNCBUSY_GENCTRL3_GCLK3_Val << GCLK_SYNCBUSY_GENCTRL3_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 3 Position  */
#define GCLK_SYNCBUSY_GENCTRL3_GCLK4          (GCLK_SYNCBUSY_GENCTRL3_GCLK4_Val << GCLK_SYNCBUSY_GENCTRL3_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 4 Position  */
#define GCLK_SYNCBUSY_GENCTRL3_GCLK5          (GCLK_SYNCBUSY_GENCTRL3_GCLK5_Val << GCLK_SYNCBUSY_GENCTRL3_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 5 Position  */
#define GCLK_SYNCBUSY_GENCTRL3_GCLK6          (GCLK_SYNCBUSY_GENCTRL3_GCLK6_Val << GCLK_SYNCBUSY_GENCTRL3_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 6 Position  */
#define GCLK_SYNCBUSY_GENCTRL3_GCLK7          (GCLK_SYNCBUSY_GENCTRL3_GCLK7_Val << GCLK_SYNCBUSY_GENCTRL3_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 7 Position  */
#define GCLK_SYNCBUSY_GENCTRL3_GCLK8          (GCLK_SYNCBUSY_GENCTRL3_GCLK8_Val << GCLK_SYNCBUSY_GENCTRL3_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 8 Position  */
#define GCLK_SYNCBUSY_GENCTRL4_Pos            (6U)                                           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 4 Synchronization Busy bits Position */
#define GCLK_SYNCBUSY_GENCTRL4_Msk            (0x1U << GCLK_SYNCBUSY_GENCTRL4_Pos)           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 4 Synchronization Busy bits Mask */
#define GCLK_SYNCBUSY_GENCTRL4(value)         (GCLK_SYNCBUSY_GENCTRL4_Msk & ((value) << GCLK_SYNCBUSY_GENCTRL4_Pos))
#define   GCLK_SYNCBUSY_GENCTRL4_GCLK0_Val    (1U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 0  */
#define   GCLK_SYNCBUSY_GENCTRL4_GCLK1_Val    (2U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 1  */
#define   GCLK_SYNCBUSY_GENCTRL4_GCLK2_Val    (4U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 2  */
#define   GCLK_SYNCBUSY_GENCTRL4_GCLK3_Val    (8U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 3  */
#define   GCLK_SYNCBUSY_GENCTRL4_GCLK4_Val    (16U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 4  */
#define   GCLK_SYNCBUSY_GENCTRL4_GCLK5_Val    (32U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 5  */
#define   GCLK_SYNCBUSY_GENCTRL4_GCLK6_Val    (64U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 6  */
#define   GCLK_SYNCBUSY_GENCTRL4_GCLK7_Val    (128U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 7  */
#define   GCLK_SYNCBUSY_GENCTRL4_GCLK8_Val    (256U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 8  */
#define GCLK_SYNCBUSY_GENCTRL4_GCLK0          (GCLK_SYNCBUSY_GENCTRL4_GCLK0_Val << GCLK_SYNCBUSY_GENCTRL4_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 0 Position  */
#define GCLK_SYNCBUSY_GENCTRL4_GCLK1          (GCLK_SYNCBUSY_GENCTRL4_GCLK1_Val << GCLK_SYNCBUSY_GENCTRL4_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 1 Position  */
#define GCLK_SYNCBUSY_GENCTRL4_GCLK2          (GCLK_SYNCBUSY_GENCTRL4_GCLK2_Val << GCLK_SYNCBUSY_GENCTRL4_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 2 Position  */
#define GCLK_SYNCBUSY_GENCTRL4_GCLK3          (GCLK_SYNCBUSY_GENCTRL4_GCLK3_Val << GCLK_SYNCBUSY_GENCTRL4_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 3 Position  */
#define GCLK_SYNCBUSY_GENCTRL4_GCLK4          (GCLK_SYNCBUSY_GENCTRL4_GCLK4_Val << GCLK_SYNCBUSY_GENCTRL4_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 4 Position  */
#define GCLK_SYNCBUSY_GENCTRL4_GCLK5          (GCLK_SYNCBUSY_GENCTRL4_GCLK5_Val << GCLK_SYNCBUSY_GENCTRL4_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 5 Position  */
#define GCLK_SYNCBUSY_GENCTRL4_GCLK6          (GCLK_SYNCBUSY_GENCTRL4_GCLK6_Val << GCLK_SYNCBUSY_GENCTRL4_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 6 Position  */
#define GCLK_SYNCBUSY_GENCTRL4_GCLK7          (GCLK_SYNCBUSY_GENCTRL4_GCLK7_Val << GCLK_SYNCBUSY_GENCTRL4_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 7 Position  */
#define GCLK_SYNCBUSY_GENCTRL4_GCLK8          (GCLK_SYNCBUSY_GENCTRL4_GCLK8_Val << GCLK_SYNCBUSY_GENCTRL4_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 8 Position  */
#define GCLK_SYNCBUSY_GENCTRL5_Pos            (7U)                                           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 5 Synchronization Busy bits Position */
#define GCLK_SYNCBUSY_GENCTRL5_Msk            (0x1U << GCLK_SYNCBUSY_GENCTRL5_Pos)           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 5 Synchronization Busy bits Mask */
#define GCLK_SYNCBUSY_GENCTRL5(value)         (GCLK_SYNCBUSY_GENCTRL5_Msk & ((value) << GCLK_SYNCBUSY_GENCTRL5_Pos))
#define   GCLK_SYNCBUSY_GENCTRL5_GCLK0_Val    (1U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 0  */
#define   GCLK_SYNCBUSY_GENCTRL5_GCLK1_Val    (2U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 1  */
#define   GCLK_SYNCBUSY_GENCTRL5_GCLK2_Val    (4U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 2  */
#define   GCLK_SYNCBUSY_GENCTRL5_GCLK3_Val    (8U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 3  */
#define   GCLK_SYNCBUSY_GENCTRL5_GCLK4_Val    (16U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 4  */
#define   GCLK_SYNCBUSY_GENCTRL5_GCLK5_Val    (32U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 5  */
#define   GCLK_SYNCBUSY_GENCTRL5_GCLK6_Val    (64U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 6  */
#define   GCLK_SYNCBUSY_GENCTRL5_GCLK7_Val    (128U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 7  */
#define   GCLK_SYNCBUSY_GENCTRL5_GCLK8_Val    (256U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 8  */
#define GCLK_SYNCBUSY_GENCTRL5_GCLK0          (GCLK_SYNCBUSY_GENCTRL5_GCLK0_Val << GCLK_SYNCBUSY_GENCTRL5_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 0 Position  */
#define GCLK_SYNCBUSY_GENCTRL5_GCLK1          (GCLK_SYNCBUSY_GENCTRL5_GCLK1_Val << GCLK_SYNCBUSY_GENCTRL5_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 1 Position  */
#define GCLK_SYNCBUSY_GENCTRL5_GCLK2          (GCLK_SYNCBUSY_GENCTRL5_GCLK2_Val << GCLK_SYNCBUSY_GENCTRL5_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 2 Position  */
#define GCLK_SYNCBUSY_GENCTRL5_GCLK3          (GCLK_SYNCBUSY_GENCTRL5_GCLK3_Val << GCLK_SYNCBUSY_GENCTRL5_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 3 Position  */
#define GCLK_SYNCBUSY_GENCTRL5_GCLK4          (GCLK_SYNCBUSY_GENCTRL5_GCLK4_Val << GCLK_SYNCBUSY_GENCTRL5_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 4 Position  */
#define GCLK_SYNCBUSY_GENCTRL5_GCLK5          (GCLK_SYNCBUSY_GENCTRL5_GCLK5_Val << GCLK_SYNCBUSY_GENCTRL5_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 5 Position  */
#define GCLK_SYNCBUSY_GENCTRL5_GCLK6          (GCLK_SYNCBUSY_GENCTRL5_GCLK6_Val << GCLK_SYNCBUSY_GENCTRL5_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 6 Position  */
#define GCLK_SYNCBUSY_GENCTRL5_GCLK7          (GCLK_SYNCBUSY_GENCTRL5_GCLK7_Val << GCLK_SYNCBUSY_GENCTRL5_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 7 Position  */
#define GCLK_SYNCBUSY_GENCTRL5_GCLK8          (GCLK_SYNCBUSY_GENCTRL5_GCLK8_Val << GCLK_SYNCBUSY_GENCTRL5_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 8 Position  */
#define GCLK_SYNCBUSY_GENCTRL6_Pos            (8U)                                           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 6 Synchronization Busy bits Position */
#define GCLK_SYNCBUSY_GENCTRL6_Msk            (0x1U << GCLK_SYNCBUSY_GENCTRL6_Pos)           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 6 Synchronization Busy bits Mask */
#define GCLK_SYNCBUSY_GENCTRL6(value)         (GCLK_SYNCBUSY_GENCTRL6_Msk & ((value) << GCLK_SYNCBUSY_GENCTRL6_Pos))
#define   GCLK_SYNCBUSY_GENCTRL6_GCLK0_Val    (1U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 0  */
#define   GCLK_SYNCBUSY_GENCTRL6_GCLK1_Val    (2U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 1  */
#define   GCLK_SYNCBUSY_GENCTRL6_GCLK2_Val    (4U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 2  */
#define   GCLK_SYNCBUSY_GENCTRL6_GCLK3_Val    (8U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 3  */
#define   GCLK_SYNCBUSY_GENCTRL6_GCLK4_Val    (16U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 4  */
#define   GCLK_SYNCBUSY_GENCTRL6_GCLK5_Val    (32U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 5  */
#define   GCLK_SYNCBUSY_GENCTRL6_GCLK6_Val    (64U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 6  */
#define   GCLK_SYNCBUSY_GENCTRL6_GCLK7_Val    (128U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 7  */
#define   GCLK_SYNCBUSY_GENCTRL6_GCLK8_Val    (256U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 8  */
#define GCLK_SYNCBUSY_GENCTRL6_GCLK0          (GCLK_SYNCBUSY_GENCTRL6_GCLK0_Val << GCLK_SYNCBUSY_GENCTRL6_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 0 Position  */
#define GCLK_SYNCBUSY_GENCTRL6_GCLK1          (GCLK_SYNCBUSY_GENCTRL6_GCLK1_Val << GCLK_SYNCBUSY_GENCTRL6_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 1 Position  */
#define GCLK_SYNCBUSY_GENCTRL6_GCLK2          (GCLK_SYNCBUSY_GENCTRL6_GCLK2_Val << GCLK_SYNCBUSY_GENCTRL6_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 2 Position  */
#define GCLK_SYNCBUSY_GENCTRL6_GCLK3          (GCLK_SYNCBUSY_GENCTRL6_GCLK3_Val << GCLK_SYNCBUSY_GENCTRL6_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 3 Position  */
#define GCLK_SYNCBUSY_GENCTRL6_GCLK4          (GCLK_SYNCBUSY_GENCTRL6_GCLK4_Val << GCLK_SYNCBUSY_GENCTRL6_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 4 Position  */
#define GCLK_SYNCBUSY_GENCTRL6_GCLK5          (GCLK_SYNCBUSY_GENCTRL6_GCLK5_Val << GCLK_SYNCBUSY_GENCTRL6_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 5 Position  */
#define GCLK_SYNCBUSY_GENCTRL6_GCLK6          (GCLK_SYNCBUSY_GENCTRL6_GCLK6_Val << GCLK_SYNCBUSY_GENCTRL6_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 6 Position  */
#define GCLK_SYNCBUSY_GENCTRL6_GCLK7          (GCLK_SYNCBUSY_GENCTRL6_GCLK7_Val << GCLK_SYNCBUSY_GENCTRL6_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 7 Position  */
#define GCLK_SYNCBUSY_GENCTRL6_GCLK8          (GCLK_SYNCBUSY_GENCTRL6_GCLK8_Val << GCLK_SYNCBUSY_GENCTRL6_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 8 Position  */
#define GCLK_SYNCBUSY_GENCTRL7_Pos            (9U)                                           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 7 Synchronization Busy bits Position */
#define GCLK_SYNCBUSY_GENCTRL7_Msk            (0x1U << GCLK_SYNCBUSY_GENCTRL7_Pos)           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 7 Synchronization Busy bits Mask */
#define GCLK_SYNCBUSY_GENCTRL7(value)         (GCLK_SYNCBUSY_GENCTRL7_Msk & ((value) << GCLK_SYNCBUSY_GENCTRL7_Pos))
#define   GCLK_SYNCBUSY_GENCTRL7_GCLK0_Val    (1U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 0  */
#define   GCLK_SYNCBUSY_GENCTRL7_GCLK1_Val    (2U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 1  */
#define   GCLK_SYNCBUSY_GENCTRL7_GCLK2_Val    (4U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 2  */
#define   GCLK_SYNCBUSY_GENCTRL7_GCLK3_Val    (8U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 3  */
#define   GCLK_SYNCBUSY_GENCTRL7_GCLK4_Val    (16U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 4  */
#define   GCLK_SYNCBUSY_GENCTRL7_GCLK5_Val    (32U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 5  */
#define   GCLK_SYNCBUSY_GENCTRL7_GCLK6_Val    (64U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 6  */
#define   GCLK_SYNCBUSY_GENCTRL7_GCLK7_Val    (128U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 7  */
#define   GCLK_SYNCBUSY_GENCTRL7_GCLK8_Val    (256U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 8  */
#define GCLK_SYNCBUSY_GENCTRL7_GCLK0          (GCLK_SYNCBUSY_GENCTRL7_GCLK0_Val << GCLK_SYNCBUSY_GENCTRL7_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 0 Position  */
#define GCLK_SYNCBUSY_GENCTRL7_GCLK1          (GCLK_SYNCBUSY_GENCTRL7_GCLK1_Val << GCLK_SYNCBUSY_GENCTRL7_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 1 Position  */
#define GCLK_SYNCBUSY_GENCTRL7_GCLK2          (GCLK_SYNCBUSY_GENCTRL7_GCLK2_Val << GCLK_SYNCBUSY_GENCTRL7_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 2 Position  */
#define GCLK_SYNCBUSY_GENCTRL7_GCLK3          (GCLK_SYNCBUSY_GENCTRL7_GCLK3_Val << GCLK_SYNCBUSY_GENCTRL7_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 3 Position  */
#define GCLK_SYNCBUSY_GENCTRL7_GCLK4          (GCLK_SYNCBUSY_GENCTRL7_GCLK4_Val << GCLK_SYNCBUSY_GENCTRL7_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 4 Position  */
#define GCLK_SYNCBUSY_GENCTRL7_GCLK5          (GCLK_SYNCBUSY_GENCTRL7_GCLK5_Val << GCLK_SYNCBUSY_GENCTRL7_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 5 Position  */
#define GCLK_SYNCBUSY_GENCTRL7_GCLK6          (GCLK_SYNCBUSY_GENCTRL7_GCLK6_Val << GCLK_SYNCBUSY_GENCTRL7_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 6 Position  */
#define GCLK_SYNCBUSY_GENCTRL7_GCLK7          (GCLK_SYNCBUSY_GENCTRL7_GCLK7_Val << GCLK_SYNCBUSY_GENCTRL7_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 7 Position  */
#define GCLK_SYNCBUSY_GENCTRL7_GCLK8          (GCLK_SYNCBUSY_GENCTRL7_GCLK8_Val << GCLK_SYNCBUSY_GENCTRL7_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 8 Position  */
#define GCLK_SYNCBUSY_GENCTRL8_Pos            (10U)                                          /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 8 Synchronization Busy bits Position */
#define GCLK_SYNCBUSY_GENCTRL8_Msk            (0x1U << GCLK_SYNCBUSY_GENCTRL8_Pos)           /**< (GCLK_SYNCBUSY) Generic Clock Generator Control 8 Synchronization Busy bits Mask */
#define GCLK_SYNCBUSY_GENCTRL8(value)         (GCLK_SYNCBUSY_GENCTRL8_Msk & ((value) << GCLK_SYNCBUSY_GENCTRL8_Pos))
#define   GCLK_SYNCBUSY_GENCTRL8_GCLK0_Val    (1U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 0  */
#define   GCLK_SYNCBUSY_GENCTRL8_GCLK1_Val    (2U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 1  */
#define   GCLK_SYNCBUSY_GENCTRL8_GCLK2_Val    (4U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 2  */
#define   GCLK_SYNCBUSY_GENCTRL8_GCLK3_Val    (8U)                                           /**< (GCLK_SYNCBUSY) Generic clock generator 3  */
#define   GCLK_SYNCBUSY_GENCTRL8_GCLK4_Val    (16U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 4  */
#define   GCLK_SYNCBUSY_GENCTRL8_GCLK5_Val    (32U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 5  */
#define   GCLK_SYNCBUSY_GENCTRL8_GCLK6_Val    (64U)                                          /**< (GCLK_SYNCBUSY) Generic clock generator 6  */
#define   GCLK_SYNCBUSY_GENCTRL8_GCLK7_Val    (128U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 7  */
#define   GCLK_SYNCBUSY_GENCTRL8_GCLK8_Val    (256U)                                         /**< (GCLK_SYNCBUSY) Generic clock generator 8  */
#define GCLK_SYNCBUSY_GENCTRL8_GCLK0          (GCLK_SYNCBUSY_GENCTRL8_GCLK0_Val << GCLK_SYNCBUSY_GENCTRL8_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 0 Position  */
#define GCLK_SYNCBUSY_GENCTRL8_GCLK1          (GCLK_SYNCBUSY_GENCTRL8_GCLK1_Val << GCLK_SYNCBUSY_GENCTRL8_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 1 Position  */
#define GCLK_SYNCBUSY_GENCTRL8_GCLK2          (GCLK_SYNCBUSY_GENCTRL8_GCLK2_Val << GCLK_SYNCBUSY_GENCTRL8_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 2 Position  */
#define GCLK_SYNCBUSY_GENCTRL8_GCLK3          (GCLK_SYNCBUSY_GENCTRL8_GCLK3_Val << GCLK_SYNCBUSY_GENCTRL8_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 3 Position  */
#define GCLK_SYNCBUSY_GENCTRL8_GCLK4          (GCLK_SYNCBUSY_GENCTRL8_GCLK4_Val << GCLK_SYNCBUSY_GENCTRL8_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 4 Position  */
#define GCLK_SYNCBUSY_GENCTRL8_GCLK5          (GCLK_SYNCBUSY_GENCTRL8_GCLK5_Val << GCLK_SYNCBUSY_GENCTRL8_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 5 Position  */
#define GCLK_SYNCBUSY_GENCTRL8_GCLK6          (GCLK_SYNCBUSY_GENCTRL8_GCLK6_Val << GCLK_SYNCBUSY_GENCTRL8_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 6 Position  */
#define GCLK_SYNCBUSY_GENCTRL8_GCLK7          (GCLK_SYNCBUSY_GENCTRL8_GCLK7_Val << GCLK_SYNCBUSY_GENCTRL8_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 7 Position  */
#define GCLK_SYNCBUSY_GENCTRL8_GCLK8          (GCLK_SYNCBUSY_GENCTRL8_GCLK8_Val << GCLK_SYNCBUSY_GENCTRL8_Pos) /**< (GCLK_SYNCBUSY) Generic clock generator 8 Position  */
#define GCLK_SYNCBUSY_Msk                     (0x000007FDUL)                                 /**< (GCLK_SYNCBUSY) Register Mask  */

/* -------- GCLK_GENCTRL : (GCLK Offset: 0x20) (R/W 32) Generic Clock Generator Control -------- */
#define GCLK_GENCTRL_SRC_Pos                  (0U)                                           /**< (GCLK_GENCTRL) Source Select Position */
#define GCLK_GENCTRL_SRC_Msk                  (0x7U << GCLK_GENCTRL_SRC_Pos)                 /**< (GCLK_GENCTRL) Source Select Mask */
#define GCLK_GENCTRL_SRC(value)               (GCLK_GENCTRL_SRC_Msk & ((value) << GCLK_GENCTRL_SRC_Pos))
#define   GCLK_GENCTRL_SRC_XOSC_Val           (0U)                                           /**< (GCLK_GENCTRL) XOSC oscillator output  */
#define   GCLK_GENCTRL_SRC_GCLKIN_Val         (1U)                                           /**< (GCLK_GENCTRL) Generator input pad  */
#define   GCLK_GENCTRL_SRC_GCLKGEN1_Val       (2U)                                           /**< (GCLK_GENCTRL) Generic clock generator 1 output  */
#define   GCLK_GENCTRL_SRC_OSCULP32K_Val      (3U)                                           /**< (GCLK_GENCTRL) OSCULP32K oscillator output  */
#define   GCLK_GENCTRL_SRC_OSC32K_Val         (4U)                                           /**< (GCLK_GENCTRL) OSC32K oscillator output  */
#define   GCLK_GENCTRL_SRC_XOSC32K_Val        (5U)                                           /**< (GCLK_GENCTRL) XOSC32K oscillator output  */
#define   GCLK_GENCTRL_SRC_OSC48M_Val         (6U)                                           /**< (GCLK_GENCTRL) OSC48M oscillator output  */
#define   GCLK_GENCTRL_SRC_DPLL96M_Val        (7U)                                           /**< (GCLK_GENCTRL) DPLL96M output  */
#define GCLK_GENCTRL_SRC_XOSC                 (GCLK_GENCTRL_SRC_XOSC_Val << GCLK_GENCTRL_SRC_Pos) /**< (GCLK_GENCTRL) XOSC oscillator output Position  */
#define GCLK_GENCTRL_SRC_GCLKIN               (GCLK_GENCTRL_SRC_GCLKIN_Val << GCLK_GENCTRL_SRC_Pos) /**< (GCLK_GENCTRL) Generator input pad Position  */
#define GCLK_GENCTRL_SRC_GCLKGEN1             (GCLK_GENCTRL_SRC_GCLKGEN1_Val << GCLK_GENCTRL_SRC_Pos) /**< (GCLK_GENCTRL) Generic clock generator 1 output Position  */
#define GCLK_GENCTRL_SRC_OSCULP32K            (GCLK_GENCTRL_SRC_OSCULP32K_Val << GCLK_GENCTRL_SRC_Pos) /**< (GCLK_GENCTRL) OSCULP32K oscillator output Position  */
#define GCLK_GENCTRL_SRC_OSC32K               (GCLK_GENCTRL_SRC_OSC32K_Val << GCLK_GENCTRL_SRC_Pos) /**< (GCLK_GENCTRL) OSC32K oscillator output Position  */
#define GCLK_GENCTRL_SRC_XOSC32K              (GCLK_GENCTRL_SRC_XOSC32K_Val << GCLK_GENCTRL_SRC_Pos) /**< (GCLK_GENCTRL) XOSC32K oscillator output Position  */
#define GCLK_GENCTRL_SRC_OSC48M               (GCLK_GENCTRL_SRC_OSC48M_Val << GCLK_GENCTRL_SRC_Pos) /**< (GCLK_GENCTRL) OSC48M oscillator output Position  */
#define GCLK_GENCTRL_SRC_DPLL96M              (GCLK_GENCTRL_SRC_DPLL96M_Val << GCLK_GENCTRL_SRC_Pos) /**< (GCLK_GENCTRL) DPLL96M output Position  */
#define GCLK_GENCTRL_GENEN_Pos                (8U)                                           /**< (GCLK_GENCTRL) Generic Clock Generator Enable Position */
#define GCLK_GENCTRL_GENEN_Msk                (0x1U << GCLK_GENCTRL_GENEN_Pos)               /**< (GCLK_GENCTRL) Generic Clock Generator Enable Mask */
#define GCLK_GENCTRL_GENEN(value)             (GCLK_GENCTRL_GENEN_Msk & ((value) << GCLK_GENCTRL_GENEN_Pos))
#define GCLK_GENCTRL_IDC_Pos                  (9U)                                           /**< (GCLK_GENCTRL) Improve Duty Cycle Position */
#define GCLK_GENCTRL_IDC_Msk                  (0x1U << GCLK_GENCTRL_IDC_Pos)                 /**< (GCLK_GENCTRL) Improve Duty Cycle Mask */
#define GCLK_GENCTRL_IDC(value)               (GCLK_GENCTRL_IDC_Msk & ((value) << GCLK_GENCTRL_IDC_Pos))
#define GCLK_GENCTRL_OOV_Pos                  (10U)                                          /**< (GCLK_GENCTRL) Output Off Value Position */
#define GCLK_GENCTRL_OOV_Msk                  (0x1U << GCLK_GENCTRL_OOV_Pos)                 /**< (GCLK_GENCTRL) Output Off Value Mask */
#define GCLK_GENCTRL_OOV(value)               (GCLK_GENCTRL_OOV_Msk & ((value) << GCLK_GENCTRL_OOV_Pos))
#define GCLK_GENCTRL_OE_Pos                   (11U)                                          /**< (GCLK_GENCTRL) Output Enable Position */
#define GCLK_GENCTRL_OE_Msk                   (0x1U << GCLK_GENCTRL_OE_Pos)                  /**< (GCLK_GENCTRL) Output Enable Mask */
#define GCLK_GENCTRL_OE(value)                (GCLK_GENCTRL_OE_Msk & ((value) << GCLK_GENCTRL_OE_Pos))
#define GCLK_GENCTRL_DIVSEL_Pos               (12U)                                          /**< (GCLK_GENCTRL) Divide Selection Position */
#define GCLK_GENCTRL_DIVSEL_Msk               (0x1U << GCLK_GENCTRL_DIVSEL_Pos)              /**< (GCLK_GENCTRL) Divide Selection Mask */
#define GCLK_GENCTRL_DIVSEL(value)            (GCLK_GENCTRL_DIVSEL_Msk & ((value) << GCLK_GENCTRL_DIVSEL_Pos))
#define   GCLK_GENCTRL_DIVSEL_DIV1_Val        (0U)                                           /**< (GCLK_GENCTRL) Divide input directly by divider factor  */
#define   GCLK_GENCTRL_DIVSEL_DIV2_Val        (1U)                                           /**< (GCLK_GENCTRL) Divide input by 2^(divider factor+ 1)  */
#define GCLK_GENCTRL_DIVSEL_DIV1              (GCLK_GENCTRL_DIVSEL_DIV1_Val << GCLK_GENCTRL_DIVSEL_Pos) /**< (GCLK_GENCTRL) Divide input directly by divider factor Position  */
#define GCLK_GENCTRL_DIVSEL_DIV2              (GCLK_GENCTRL_DIVSEL_DIV2_Val << GCLK_GENCTRL_DIVSEL_Pos) /**< (GCLK_GENCTRL) Divide input by 2^(divider factor+ 1) Position  */
#define GCLK_GENCTRL_RUNSTDBY_Pos             (13U)                                          /**< (GCLK_GENCTRL) Run in Standby Position */
#define GCLK_GENCTRL_RUNSTDBY_Msk             (0x1U << GCLK_GENCTRL_RUNSTDBY_Pos)            /**< (GCLK_GENCTRL) Run in Standby Mask */
#define GCLK_GENCTRL_RUNSTDBY(value)          (GCLK_GENCTRL_RUNSTDBY_Msk & ((value) << GCLK_GENCTRL_RUNSTDBY_Pos))
#define GCLK_GENCTRL_DIV_Pos                  (16U)                                          /**< (GCLK_GENCTRL) Division Factor Position */
#define GCLK_GENCTRL_DIV_Msk                  (0xFFFFU << GCLK_GENCTRL_DIV_Pos)              /**< (GCLK_GENCTRL) Division Factor Mask */
#define GCLK_GENCTRL_DIV(value)               (GCLK_GENCTRL_DIV_Msk & ((value) << GCLK_GENCTRL_DIV_Pos))
#define GCLK_GENCTRL_Msk                      (0xFFFF3F07UL)                                 /**< (GCLK_GENCTRL) Register Mask  */

/* -------- GCLK_PCHCTRL : (GCLK Offset: 0x80) (R/W 32) Peripheral Clock Control -------- */
#define GCLK_PCHCTRL_GEN_Pos                  (0U)                                           /**< (GCLK_PCHCTRL) Generic Clock Generator Position */
#define GCLK_PCHCTRL_GEN_Msk                  (0xFU << GCLK_PCHCTRL_GEN_Pos)                 /**< (GCLK_PCHCTRL) Generic Clock Generator Mask */
#define GCLK_PCHCTRL_GEN(value)               (GCLK_PCHCTRL_GEN_Msk & ((value) << GCLK_PCHCTRL_GEN_Pos))
#define   GCLK_PCHCTRL_GEN_GCLK0_Val          (0U)                                           /**< (GCLK_PCHCTRL) Generic clock generator 0  */
#define   GCLK_PCHCTRL_GEN_GCLK1_Val          (1U)                                           /**< (GCLK_PCHCTRL) Generic clock generator 1  */
#define   GCLK_PCHCTRL_GEN_GCLK2_Val          (2U)                                           /**< (GCLK_PCHCTRL) Generic clock generator 2  */
#define   GCLK_PCHCTRL_GEN_GCLK3_Val          (3U)                                           /**< (GCLK_PCHCTRL) Generic clock generator 3  */
#define   GCLK_PCHCTRL_GEN_GCLK4_Val          (4U)                                           /**< (GCLK_PCHCTRL) Generic clock generator 4  */
#define   GCLK_PCHCTRL_GEN_GCLK5_Val          (5U)                                           /**< (GCLK_PCHCTRL) Generic clock generator 5  */
#define   GCLK_PCHCTRL_GEN_GCLK6_Val          (6U)                                           /**< (GCLK_PCHCTRL) Generic clock generator 6  */
#define   GCLK_PCHCTRL_GEN_GCLK7_Val          (7U)                                           /**< (GCLK_PCHCTRL) Generic clock generator 7  */
#define   GCLK_PCHCTRL_GEN_GCLK8_Val          (8U)                                           /**< (GCLK_PCHCTRL) Generic clock generator 8  */
#define GCLK_PCHCTRL_GEN_GCLK0                (GCLK_PCHCTRL_GEN_GCLK0_Val << GCLK_PCHCTRL_GEN_Pos) /**< (GCLK_PCHCTRL) Generic clock generator 0 Position  */
#define GCLK_PCHCTRL_GEN_GCLK1                (GCLK_PCHCTRL_GEN_GCLK1_Val << GCLK_PCHCTRL_GEN_Pos) /**< (GCLK_PCHCTRL) Generic clock generator 1 Position  */
#define GCLK_PCHCTRL_GEN_GCLK2                (GCLK_PCHCTRL_GEN_GCLK2_Val << GCLK_PCHCTRL_GEN_Pos) /**< (GCLK_PCHCTRL) Generic clock generator 2 Position  */
#define GCLK_PCHCTRL_GEN_GCLK3                (GCLK_PCHCTRL_GEN_GCLK3_Val << GCLK_PCHCTRL_GEN_Pos) /**< (GCLK_PCHCTRL) Generic clock generator 3 Position  */
#define GCLK_PCHCTRL_GEN_GCLK4                (GCLK_PCHCTRL_GEN_GCLK4_Val << GCLK_PCHCTRL_GEN_Pos) /**< (GCLK_PCHCTRL) Generic clock generator 4 Position  */
#define GCLK_PCHCTRL_GEN_GCLK5                (GCLK_PCHCTRL_GEN_GCLK5_Val << GCLK_PCHCTRL_GEN_Pos) /**< (GCLK_PCHCTRL) Generic clock generator 5 Position  */
#define GCLK_PCHCTRL_GEN_GCLK6                (GCLK_PCHCTRL_GEN_GCLK6_Val << GCLK_PCHCTRL_GEN_Pos) /**< (GCLK_PCHCTRL) Generic clock generator 6 Position  */
#define GCLK_PCHCTRL_GEN_GCLK7                (GCLK_PCHCTRL_GEN_GCLK7_Val << GCLK_PCHCTRL_GEN_Pos) /**< (GCLK_PCHCTRL) Generic clock generator 7 Position  */
#define GCLK_PCHCTRL_GEN_GCLK8                (GCLK_PCHCTRL_GEN_GCLK8_Val << GCLK_PCHCTRL_GEN_Pos) /**< (GCLK_PCHCTRL) Generic clock generator 8 Position  */
#define GCLK_PCHCTRL_CHEN_Pos                 (6U)                                           /**< (GCLK_PCHCTRL) Channel Enable Position */
#define GCLK_PCHCTRL_CHEN_Msk                 (0x1U << GCLK_PCHCTRL_CHEN_Pos)                /**< (GCLK_PCHCTRL) Channel Enable Mask */
#define GCLK_PCHCTRL_CHEN(value)              (GCLK_PCHCTRL_CHEN_Msk & ((value) << GCLK_PCHCTRL_CHEN_Pos))
#define GCLK_PCHCTRL_WRTLOCK_Pos              (7U)                                           /**< (GCLK_PCHCTRL) Write Lock Position */
#define GCLK_PCHCTRL_WRTLOCK_Msk              (0x1U << GCLK_PCHCTRL_WRTLOCK_Pos)             /**< (GCLK_PCHCTRL) Write Lock Mask */
#define GCLK_PCHCTRL_WRTLOCK(value)           (GCLK_PCHCTRL_WRTLOCK_Msk & ((value) << GCLK_PCHCTRL_WRTLOCK_Pos))
#define GCLK_PCHCTRL_Msk                      (0x000000CFUL)                                 /**< (GCLK_PCHCTRL) Register Mask  */

/** \brief GCLK register offsets definitions */
#define GCLK_CTRLA_OFFSET              (0x00)         /**< (GCLK_CTRLA) Control Offset */
#define GCLK_SYNCBUSY_OFFSET           (0x04)         /**< (GCLK_SYNCBUSY) Synchronization Busy Offset */
#define GCLK_GENCTRL_OFFSET            (0x20)         /**< (GCLK_GENCTRL) Generic Clock Generator Control Offset */
#define GCLK_PCHCTRL_OFFSET            (0x80)         /**< (GCLK_PCHCTRL) Peripheral Clock Control Offset */

/** \brief GCLK register API structure */
typedef struct
{
  __IO  uint8_t                        GCLK_CTRLA;      /**< Offset: 0x00 (R/W  8) Control */
  __I   uint8_t                        Reserved1[0x03];
  __I   uint32_t                       GCLK_SYNCBUSY;   /**< Offset: 0x04 (R/   32) Synchronization Busy */
  __I   uint8_t                        Reserved2[0x18];
  __IO  uint32_t                       GCLK_GENCTRL[9]; /**< Offset: 0x20 (R/W  32) Generic Clock Generator Control */
  __I   uint8_t                        Reserved3[0x3C];
  __IO  uint32_t                       GCLK_PCHCTRL[46]; /**< Offset: 0x80 (R/W  32) Peripheral Clock Control */
} gclk_registers_t;
/** @}  end of Generic Clock Generator */

#endif /* SAMC_SAMC21_GCLK_MODULE_H */

