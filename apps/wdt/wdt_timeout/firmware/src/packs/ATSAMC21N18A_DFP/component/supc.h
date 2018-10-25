/**
 * \brief Header file for SAMC/SAMC21 SUPC
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
#ifndef SAMC_SAMC21_SUPC_MODULE_H
#define SAMC_SAMC21_SUPC_MODULE_H

/** \addtogroup SAMC_SAMC21 Supply Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_SUPC                                  */
/* ========================================================================== */

/* -------- SUPC_INTENCLR : (SUPC Offset: 0x00) (R/W 32) Interrupt Enable Clear -------- */
#define SUPC_INTENCLR_BODVDDRDY_Pos           (0U)                                           /**< (SUPC_INTENCLR) BODVDD Ready Position */
#define SUPC_INTENCLR_BODVDDRDY_Msk           (0x1U << SUPC_INTENCLR_BODVDDRDY_Pos)          /**< (SUPC_INTENCLR) BODVDD Ready Mask */
#define SUPC_INTENCLR_BODVDDRDY(value)        (SUPC_INTENCLR_BODVDDRDY_Msk & ((value) << SUPC_INTENCLR_BODVDDRDY_Pos))
#define SUPC_INTENCLR_BODVDDDET_Pos           (1U)                                           /**< (SUPC_INTENCLR) BODVDD Detection Position */
#define SUPC_INTENCLR_BODVDDDET_Msk           (0x1U << SUPC_INTENCLR_BODVDDDET_Pos)          /**< (SUPC_INTENCLR) BODVDD Detection Mask */
#define SUPC_INTENCLR_BODVDDDET(value)        (SUPC_INTENCLR_BODVDDDET_Msk & ((value) << SUPC_INTENCLR_BODVDDDET_Pos))
#define SUPC_INTENCLR_BVDDSRDY_Pos            (2U)                                           /**< (SUPC_INTENCLR) BODVDD Synchronization Ready Position */
#define SUPC_INTENCLR_BVDDSRDY_Msk            (0x1U << SUPC_INTENCLR_BVDDSRDY_Pos)           /**< (SUPC_INTENCLR) BODVDD Synchronization Ready Mask */
#define SUPC_INTENCLR_BVDDSRDY(value)         (SUPC_INTENCLR_BVDDSRDY_Msk & ((value) << SUPC_INTENCLR_BVDDSRDY_Pos))
#define SUPC_INTENCLR_BODCORERDY_Pos          (3U)                                           /**< (SUPC_INTENCLR) BODCORE Ready Position */
#define SUPC_INTENCLR_BODCORERDY_Msk          (0x1U << SUPC_INTENCLR_BODCORERDY_Pos)         /**< (SUPC_INTENCLR) BODCORE Ready Mask */
#define SUPC_INTENCLR_BODCORERDY(value)       (SUPC_INTENCLR_BODCORERDY_Msk & ((value) << SUPC_INTENCLR_BODCORERDY_Pos))
#define SUPC_INTENCLR_BODCOREDET_Pos          (4U)                                           /**< (SUPC_INTENCLR) BODCORE Detection Position */
#define SUPC_INTENCLR_BODCOREDET_Msk          (0x1U << SUPC_INTENCLR_BODCOREDET_Pos)         /**< (SUPC_INTENCLR) BODCORE Detection Mask */
#define SUPC_INTENCLR_BODCOREDET(value)       (SUPC_INTENCLR_BODCOREDET_Msk & ((value) << SUPC_INTENCLR_BODCOREDET_Pos))
#define SUPC_INTENCLR_BCORESRDY_Pos           (5U)                                           /**< (SUPC_INTENCLR) BODCORE Synchronization Ready Position */
#define SUPC_INTENCLR_BCORESRDY_Msk           (0x1U << SUPC_INTENCLR_BCORESRDY_Pos)          /**< (SUPC_INTENCLR) BODCORE Synchronization Ready Mask */
#define SUPC_INTENCLR_BCORESRDY(value)        (SUPC_INTENCLR_BCORESRDY_Msk & ((value) << SUPC_INTENCLR_BCORESRDY_Pos))
#define SUPC_INTENCLR_VREG33RDY_Pos           (6U)                                           /**< (SUPC_INTENCLR) VREG33 Ready Position */
#define SUPC_INTENCLR_VREG33RDY_Msk           (0x1U << SUPC_INTENCLR_VREG33RDY_Pos)          /**< (SUPC_INTENCLR) VREG33 Ready Mask */
#define SUPC_INTENCLR_VREG33RDY(value)        (SUPC_INTENCLR_VREG33RDY_Msk & ((value) << SUPC_INTENCLR_VREG33RDY_Pos))
#define SUPC_INTENCLR_Msk                     (0x0000007FUL)                                 /**< (SUPC_INTENCLR) Register Mask  */

/* -------- SUPC_INTENSET : (SUPC Offset: 0x04) (R/W 32) Interrupt Enable Set -------- */
#define SUPC_INTENSET_BODVDDRDY_Pos           (0U)                                           /**< (SUPC_INTENSET) BODVDD Ready Position */
#define SUPC_INTENSET_BODVDDRDY_Msk           (0x1U << SUPC_INTENSET_BODVDDRDY_Pos)          /**< (SUPC_INTENSET) BODVDD Ready Mask */
#define SUPC_INTENSET_BODVDDRDY(value)        (SUPC_INTENSET_BODVDDRDY_Msk & ((value) << SUPC_INTENSET_BODVDDRDY_Pos))
#define SUPC_INTENSET_BODVDDDET_Pos           (1U)                                           /**< (SUPC_INTENSET) BODVDD Detection Position */
#define SUPC_INTENSET_BODVDDDET_Msk           (0x1U << SUPC_INTENSET_BODVDDDET_Pos)          /**< (SUPC_INTENSET) BODVDD Detection Mask */
#define SUPC_INTENSET_BODVDDDET(value)        (SUPC_INTENSET_BODVDDDET_Msk & ((value) << SUPC_INTENSET_BODVDDDET_Pos))
#define SUPC_INTENSET_BVDDSRDY_Pos            (2U)                                           /**< (SUPC_INTENSET) BODVDD Synchronization Ready Position */
#define SUPC_INTENSET_BVDDSRDY_Msk            (0x1U << SUPC_INTENSET_BVDDSRDY_Pos)           /**< (SUPC_INTENSET) BODVDD Synchronization Ready Mask */
#define SUPC_INTENSET_BVDDSRDY(value)         (SUPC_INTENSET_BVDDSRDY_Msk & ((value) << SUPC_INTENSET_BVDDSRDY_Pos))
#define SUPC_INTENSET_BODCORERDY_Pos          (3U)                                           /**< (SUPC_INTENSET) BODCORE Ready Position */
#define SUPC_INTENSET_BODCORERDY_Msk          (0x1U << SUPC_INTENSET_BODCORERDY_Pos)         /**< (SUPC_INTENSET) BODCORE Ready Mask */
#define SUPC_INTENSET_BODCORERDY(value)       (SUPC_INTENSET_BODCORERDY_Msk & ((value) << SUPC_INTENSET_BODCORERDY_Pos))
#define SUPC_INTENSET_BODCOREDET_Pos          (4U)                                           /**< (SUPC_INTENSET) BODCORE Detection Position */
#define SUPC_INTENSET_BODCOREDET_Msk          (0x1U << SUPC_INTENSET_BODCOREDET_Pos)         /**< (SUPC_INTENSET) BODCORE Detection Mask */
#define SUPC_INTENSET_BODCOREDET(value)       (SUPC_INTENSET_BODCOREDET_Msk & ((value) << SUPC_INTENSET_BODCOREDET_Pos))
#define SUPC_INTENSET_BCORESRDY_Pos           (5U)                                           /**< (SUPC_INTENSET) BODCORE Synchronization Ready Position */
#define SUPC_INTENSET_BCORESRDY_Msk           (0x1U << SUPC_INTENSET_BCORESRDY_Pos)          /**< (SUPC_INTENSET) BODCORE Synchronization Ready Mask */
#define SUPC_INTENSET_BCORESRDY(value)        (SUPC_INTENSET_BCORESRDY_Msk & ((value) << SUPC_INTENSET_BCORESRDY_Pos))
#define SUPC_INTENSET_VREG33RDY_Pos           (6U)                                           /**< (SUPC_INTENSET) VREG33 Ready Position */
#define SUPC_INTENSET_VREG33RDY_Msk           (0x1U << SUPC_INTENSET_VREG33RDY_Pos)          /**< (SUPC_INTENSET) VREG33 Ready Mask */
#define SUPC_INTENSET_VREG33RDY(value)        (SUPC_INTENSET_VREG33RDY_Msk & ((value) << SUPC_INTENSET_VREG33RDY_Pos))
#define SUPC_INTENSET_Msk                     (0x0000007FUL)                                 /**< (SUPC_INTENSET) Register Mask  */

/* -------- SUPC_INTFLAG : (SUPC Offset: 0x08) (R/W 32) Interrupt Flag Status and Clear -------- */
#define SUPC_INTFLAG_BODVDDRDY_Pos            (0U)                                           /**< (SUPC_INTFLAG) BODVDD Ready Position */
#define SUPC_INTFLAG_BODVDDRDY_Msk            (0x1U << SUPC_INTFLAG_BODVDDRDY_Pos)           /**< (SUPC_INTFLAG) BODVDD Ready Mask */
#define SUPC_INTFLAG_BODVDDRDY(value)         (SUPC_INTFLAG_BODVDDRDY_Msk & ((value) << SUPC_INTFLAG_BODVDDRDY_Pos))
#define SUPC_INTFLAG_BODVDDDET_Pos            (1U)                                           /**< (SUPC_INTFLAG) BODVDD Detection Position */
#define SUPC_INTFLAG_BODVDDDET_Msk            (0x1U << SUPC_INTFLAG_BODVDDDET_Pos)           /**< (SUPC_INTFLAG) BODVDD Detection Mask */
#define SUPC_INTFLAG_BODVDDDET(value)         (SUPC_INTFLAG_BODVDDDET_Msk & ((value) << SUPC_INTFLAG_BODVDDDET_Pos))
#define SUPC_INTFLAG_BVDDSRDY_Pos             (2U)                                           /**< (SUPC_INTFLAG) BODVDD Synchronization Ready Position */
#define SUPC_INTFLAG_BVDDSRDY_Msk             (0x1U << SUPC_INTFLAG_BVDDSRDY_Pos)            /**< (SUPC_INTFLAG) BODVDD Synchronization Ready Mask */
#define SUPC_INTFLAG_BVDDSRDY(value)          (SUPC_INTFLAG_BVDDSRDY_Msk & ((value) << SUPC_INTFLAG_BVDDSRDY_Pos))
#define SUPC_INTFLAG_BODCORERDY_Pos           (3U)                                           /**< (SUPC_INTFLAG) BODCORE Ready Position */
#define SUPC_INTFLAG_BODCORERDY_Msk           (0x1U << SUPC_INTFLAG_BODCORERDY_Pos)          /**< (SUPC_INTFLAG) BODCORE Ready Mask */
#define SUPC_INTFLAG_BODCORERDY(value)        (SUPC_INTFLAG_BODCORERDY_Msk & ((value) << SUPC_INTFLAG_BODCORERDY_Pos))
#define SUPC_INTFLAG_BODCOREDET_Pos           (4U)                                           /**< (SUPC_INTFLAG) BODCORE Detection Position */
#define SUPC_INTFLAG_BODCOREDET_Msk           (0x1U << SUPC_INTFLAG_BODCOREDET_Pos)          /**< (SUPC_INTFLAG) BODCORE Detection Mask */
#define SUPC_INTFLAG_BODCOREDET(value)        (SUPC_INTFLAG_BODCOREDET_Msk & ((value) << SUPC_INTFLAG_BODCOREDET_Pos))
#define SUPC_INTFLAG_BCORESRDY_Pos            (5U)                                           /**< (SUPC_INTFLAG) BODCORE Synchronization Ready Position */
#define SUPC_INTFLAG_BCORESRDY_Msk            (0x1U << SUPC_INTFLAG_BCORESRDY_Pos)           /**< (SUPC_INTFLAG) BODCORE Synchronization Ready Mask */
#define SUPC_INTFLAG_BCORESRDY(value)         (SUPC_INTFLAG_BCORESRDY_Msk & ((value) << SUPC_INTFLAG_BCORESRDY_Pos))
#define SUPC_INTFLAG_VREG33RDY_Pos            (6U)                                           /**< (SUPC_INTFLAG) VREG33 Ready Position */
#define SUPC_INTFLAG_VREG33RDY_Msk            (0x1U << SUPC_INTFLAG_VREG33RDY_Pos)           /**< (SUPC_INTFLAG) VREG33 Ready Mask */
#define SUPC_INTFLAG_VREG33RDY(value)         (SUPC_INTFLAG_VREG33RDY_Msk & ((value) << SUPC_INTFLAG_VREG33RDY_Pos))
#define SUPC_INTFLAG_Msk                      (0x0000007FUL)                                 /**< (SUPC_INTFLAG) Register Mask  */

/* -------- SUPC_STATUS : (SUPC Offset: 0x0C) (R/  32) Power and Clocks Status -------- */
#define SUPC_STATUS_BODVDDRDY_Pos             (0U)                                           /**< (SUPC_STATUS) BODVDD Ready Position */
#define SUPC_STATUS_BODVDDRDY_Msk             (0x1U << SUPC_STATUS_BODVDDRDY_Pos)            /**< (SUPC_STATUS) BODVDD Ready Mask */
#define SUPC_STATUS_BODVDDRDY(value)          (SUPC_STATUS_BODVDDRDY_Msk & ((value) << SUPC_STATUS_BODVDDRDY_Pos))
#define SUPC_STATUS_BODVDDDET_Pos             (1U)                                           /**< (SUPC_STATUS) BODVDD Detection Position */
#define SUPC_STATUS_BODVDDDET_Msk             (0x1U << SUPC_STATUS_BODVDDDET_Pos)            /**< (SUPC_STATUS) BODVDD Detection Mask */
#define SUPC_STATUS_BODVDDDET(value)          (SUPC_STATUS_BODVDDDET_Msk & ((value) << SUPC_STATUS_BODVDDDET_Pos))
#define SUPC_STATUS_BVDDSRDY_Pos              (2U)                                           /**< (SUPC_STATUS) BODVDD Synchronization Ready Position */
#define SUPC_STATUS_BVDDSRDY_Msk              (0x1U << SUPC_STATUS_BVDDSRDY_Pos)             /**< (SUPC_STATUS) BODVDD Synchronization Ready Mask */
#define SUPC_STATUS_BVDDSRDY(value)           (SUPC_STATUS_BVDDSRDY_Msk & ((value) << SUPC_STATUS_BVDDSRDY_Pos))
#define SUPC_STATUS_BODCORERDY_Pos            (3U)                                           /**< (SUPC_STATUS) BODCORE Ready Position */
#define SUPC_STATUS_BODCORERDY_Msk            (0x1U << SUPC_STATUS_BODCORERDY_Pos)           /**< (SUPC_STATUS) BODCORE Ready Mask */
#define SUPC_STATUS_BODCORERDY(value)         (SUPC_STATUS_BODCORERDY_Msk & ((value) << SUPC_STATUS_BODCORERDY_Pos))
#define SUPC_STATUS_BODCOREDET_Pos            (4U)                                           /**< (SUPC_STATUS) BODCORE Detection Position */
#define SUPC_STATUS_BODCOREDET_Msk            (0x1U << SUPC_STATUS_BODCOREDET_Pos)           /**< (SUPC_STATUS) BODCORE Detection Mask */
#define SUPC_STATUS_BODCOREDET(value)         (SUPC_STATUS_BODCOREDET_Msk & ((value) << SUPC_STATUS_BODCOREDET_Pos))
#define SUPC_STATUS_BCORESRDY_Pos             (5U)                                           /**< (SUPC_STATUS) BODCORE Synchronization Ready Position */
#define SUPC_STATUS_BCORESRDY_Msk             (0x1U << SUPC_STATUS_BCORESRDY_Pos)            /**< (SUPC_STATUS) BODCORE Synchronization Ready Mask */
#define SUPC_STATUS_BCORESRDY(value)          (SUPC_STATUS_BCORESRDY_Msk & ((value) << SUPC_STATUS_BCORESRDY_Pos))
#define SUPC_STATUS_VREG33RDY_Pos             (6U)                                           /**< (SUPC_STATUS) VREG33 Ready Position */
#define SUPC_STATUS_VREG33RDY_Msk             (0x1U << SUPC_STATUS_VREG33RDY_Pos)            /**< (SUPC_STATUS) VREG33 Ready Mask */
#define SUPC_STATUS_VREG33RDY(value)          (SUPC_STATUS_VREG33RDY_Msk & ((value) << SUPC_STATUS_VREG33RDY_Pos))
#define SUPC_STATUS_Msk                       (0x0000007FUL)                                 /**< (SUPC_STATUS) Register Mask  */

/* -------- SUPC_BODVDD : (SUPC Offset: 0x10) (R/W 32) BODVDD Control -------- */
#define SUPC_BODVDD_ENABLE_Pos                (1U)                                           /**< (SUPC_BODVDD) Enable Position */
#define SUPC_BODVDD_ENABLE_Msk                (0x1U << SUPC_BODVDD_ENABLE_Pos)               /**< (SUPC_BODVDD) Enable Mask */
#define SUPC_BODVDD_ENABLE(value)             (SUPC_BODVDD_ENABLE_Msk & ((value) << SUPC_BODVDD_ENABLE_Pos))
#define SUPC_BODVDD_HYST_Pos                  (2U)                                           /**< (SUPC_BODVDD) Hysteresis Enable Position */
#define SUPC_BODVDD_HYST_Msk                  (0x1U << SUPC_BODVDD_HYST_Pos)                 /**< (SUPC_BODVDD) Hysteresis Enable Mask */
#define SUPC_BODVDD_HYST(value)               (SUPC_BODVDD_HYST_Msk & ((value) << SUPC_BODVDD_HYST_Pos))
#define SUPC_BODVDD_ACTION_Pos                (3U)                                           /**< (SUPC_BODVDD) Action when Threshold Crossed Position */
#define SUPC_BODVDD_ACTION_Msk                (0x3U << SUPC_BODVDD_ACTION_Pos)               /**< (SUPC_BODVDD) Action when Threshold Crossed Mask */
#define SUPC_BODVDD_ACTION(value)             (SUPC_BODVDD_ACTION_Msk & ((value) << SUPC_BODVDD_ACTION_Pos))
#define   SUPC_BODVDD_ACTION_NONE_Val         (0U)                                           /**< (SUPC_BODVDD) No action  */
#define   SUPC_BODVDD_ACTION_RESET_Val        (1U)                                           /**< (SUPC_BODVDD) The BODVDD generates a reset  */
#define   SUPC_BODVDD_ACTION_INT_Val          (2U)                                           /**< (SUPC_BODVDD) The BODVDD generates an interrupt  */
#define SUPC_BODVDD_ACTION_NONE               (SUPC_BODVDD_ACTION_NONE_Val << SUPC_BODVDD_ACTION_Pos) /**< (SUPC_BODVDD) No action Position  */
#define SUPC_BODVDD_ACTION_RESET              (SUPC_BODVDD_ACTION_RESET_Val << SUPC_BODVDD_ACTION_Pos) /**< (SUPC_BODVDD) The BODVDD generates a reset Position  */
#define SUPC_BODVDD_ACTION_INT                (SUPC_BODVDD_ACTION_INT_Val << SUPC_BODVDD_ACTION_Pos) /**< (SUPC_BODVDD) The BODVDD generates an interrupt Position  */
#define SUPC_BODVDD_STDBYCFG_Pos              (5U)                                           /**< (SUPC_BODVDD) Configuration in Standby mode Position */
#define SUPC_BODVDD_STDBYCFG_Msk              (0x1U << SUPC_BODVDD_STDBYCFG_Pos)             /**< (SUPC_BODVDD) Configuration in Standby mode Mask */
#define SUPC_BODVDD_STDBYCFG(value)           (SUPC_BODVDD_STDBYCFG_Msk & ((value) << SUPC_BODVDD_STDBYCFG_Pos))
#define SUPC_BODVDD_RUNSTDBY_Pos              (6U)                                           /**< (SUPC_BODVDD) Run during Standby Position */
#define SUPC_BODVDD_RUNSTDBY_Msk              (0x1U << SUPC_BODVDD_RUNSTDBY_Pos)             /**< (SUPC_BODVDD) Run during Standby Mask */
#define SUPC_BODVDD_RUNSTDBY(value)           (SUPC_BODVDD_RUNSTDBY_Msk & ((value) << SUPC_BODVDD_RUNSTDBY_Pos))
#define SUPC_BODVDD_ACTCFG_Pos                (8U)                                           /**< (SUPC_BODVDD) Configuration in Active mode Position */
#define SUPC_BODVDD_ACTCFG_Msk                (0x1U << SUPC_BODVDD_ACTCFG_Pos)               /**< (SUPC_BODVDD) Configuration in Active mode Mask */
#define SUPC_BODVDD_ACTCFG(value)             (SUPC_BODVDD_ACTCFG_Msk & ((value) << SUPC_BODVDD_ACTCFG_Pos))
#define SUPC_BODVDD_PSEL_Pos                  (12U)                                          /**< (SUPC_BODVDD) Prescaler Select Position */
#define SUPC_BODVDD_PSEL_Msk                  (0xFU << SUPC_BODVDD_PSEL_Pos)                 /**< (SUPC_BODVDD) Prescaler Select Mask */
#define SUPC_BODVDD_PSEL(value)               (SUPC_BODVDD_PSEL_Msk & ((value) << SUPC_BODVDD_PSEL_Pos))
#define   SUPC_BODVDD_PSEL_DIV2_Val           (0U)                                           /**< (SUPC_BODVDD) Divide clock by 2  */
#define   SUPC_BODVDD_PSEL_DIV4_Val           (1U)                                           /**< (SUPC_BODVDD) Divide clock by 4  */
#define   SUPC_BODVDD_PSEL_DIV8_Val           (2U)                                           /**< (SUPC_BODVDD) Divide clock by 8  */
#define   SUPC_BODVDD_PSEL_DIV16_Val          (3U)                                           /**< (SUPC_BODVDD) Divide clock by 16  */
#define   SUPC_BODVDD_PSEL_DIV32_Val          (4U)                                           /**< (SUPC_BODVDD) Divide clock by 32  */
#define   SUPC_BODVDD_PSEL_DIV64_Val          (5U)                                           /**< (SUPC_BODVDD) Divide clock by 64  */
#define   SUPC_BODVDD_PSEL_DIV128_Val         (6U)                                           /**< (SUPC_BODVDD) Divide clock by 128  */
#define   SUPC_BODVDD_PSEL_DIV256_Val         (7U)                                           /**< (SUPC_BODVDD) Divide clock by 256  */
#define   SUPC_BODVDD_PSEL_DIV512_Val         (8U)                                           /**< (SUPC_BODVDD) Divide clock by 512  */
#define   SUPC_BODVDD_PSEL_DIV1024_Val        (9U)                                           /**< (SUPC_BODVDD) Divide clock by 1024  */
#define   SUPC_BODVDD_PSEL_DIV2048_Val        (10U)                                          /**< (SUPC_BODVDD) Divide clock by 2048  */
#define   SUPC_BODVDD_PSEL_DIV4096_Val        (11U)                                          /**< (SUPC_BODVDD) Divide clock by 4096  */
#define   SUPC_BODVDD_PSEL_DIV8192_Val        (12U)                                          /**< (SUPC_BODVDD) Divide clock by 8192  */
#define   SUPC_BODVDD_PSEL_DIV16384_Val       (13U)                                          /**< (SUPC_BODVDD) Divide clock by 16384  */
#define   SUPC_BODVDD_PSEL_DIV32768_Val       (14U)                                          /**< (SUPC_BODVDD) Divide clock by 32768  */
#define   SUPC_BODVDD_PSEL_DIV65536_Val       (15U)                                          /**< (SUPC_BODVDD) Divide clock by 65536  */
#define SUPC_BODVDD_PSEL_DIV2                 (SUPC_BODVDD_PSEL_DIV2_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 2 Position  */
#define SUPC_BODVDD_PSEL_DIV4                 (SUPC_BODVDD_PSEL_DIV4_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 4 Position  */
#define SUPC_BODVDD_PSEL_DIV8                 (SUPC_BODVDD_PSEL_DIV8_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 8 Position  */
#define SUPC_BODVDD_PSEL_DIV16                (SUPC_BODVDD_PSEL_DIV16_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 16 Position  */
#define SUPC_BODVDD_PSEL_DIV32                (SUPC_BODVDD_PSEL_DIV32_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 32 Position  */
#define SUPC_BODVDD_PSEL_DIV64                (SUPC_BODVDD_PSEL_DIV64_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 64 Position  */
#define SUPC_BODVDD_PSEL_DIV128               (SUPC_BODVDD_PSEL_DIV128_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 128 Position  */
#define SUPC_BODVDD_PSEL_DIV256               (SUPC_BODVDD_PSEL_DIV256_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 256 Position  */
#define SUPC_BODVDD_PSEL_DIV512               (SUPC_BODVDD_PSEL_DIV512_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 512 Position  */
#define SUPC_BODVDD_PSEL_DIV1024              (SUPC_BODVDD_PSEL_DIV1024_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 1024 Position  */
#define SUPC_BODVDD_PSEL_DIV2048              (SUPC_BODVDD_PSEL_DIV2048_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 2048 Position  */
#define SUPC_BODVDD_PSEL_DIV4096              (SUPC_BODVDD_PSEL_DIV4096_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 4096 Position  */
#define SUPC_BODVDD_PSEL_DIV8192              (SUPC_BODVDD_PSEL_DIV8192_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 8192 Position  */
#define SUPC_BODVDD_PSEL_DIV16384             (SUPC_BODVDD_PSEL_DIV16384_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 16384 Position  */
#define SUPC_BODVDD_PSEL_DIV32768             (SUPC_BODVDD_PSEL_DIV32768_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 32768 Position  */
#define SUPC_BODVDD_PSEL_DIV65536             (SUPC_BODVDD_PSEL_DIV65536_Val << SUPC_BODVDD_PSEL_Pos) /**< (SUPC_BODVDD) Divide clock by 65536 Position  */
#define SUPC_BODVDD_LEVEL_Pos                 (16U)                                          /**< (SUPC_BODVDD) Threshold Level for VDD Position */
#define SUPC_BODVDD_LEVEL_Msk                 (0x3FU << SUPC_BODVDD_LEVEL_Pos)               /**< (SUPC_BODVDD) Threshold Level for VDD Mask */
#define SUPC_BODVDD_LEVEL(value)              (SUPC_BODVDD_LEVEL_Msk & ((value) << SUPC_BODVDD_LEVEL_Pos))
#define SUPC_BODVDD_Msk                       (0x003FF17EUL)                                 /**< (SUPC_BODVDD) Register Mask  */

/* -------- SUPC_BODCORE : (SUPC Offset: 0x14) (R/W 32) BODCORE Control -------- */
#define SUPC_BODCORE_ENABLE_Pos               (1U)                                           /**< (SUPC_BODCORE) Enable Position */
#define SUPC_BODCORE_ENABLE_Msk               (0x1U << SUPC_BODCORE_ENABLE_Pos)              /**< (SUPC_BODCORE) Enable Mask */
#define SUPC_BODCORE_ENABLE(value)            (SUPC_BODCORE_ENABLE_Msk & ((value) << SUPC_BODCORE_ENABLE_Pos))
#define SUPC_BODCORE_HYST_Pos                 (2U)                                           /**< (SUPC_BODCORE) Hysteresis Enable Position */
#define SUPC_BODCORE_HYST_Msk                 (0x1U << SUPC_BODCORE_HYST_Pos)                /**< (SUPC_BODCORE) Hysteresis Enable Mask */
#define SUPC_BODCORE_HYST(value)              (SUPC_BODCORE_HYST_Msk & ((value) << SUPC_BODCORE_HYST_Pos))
#define SUPC_BODCORE_ACTION_Pos               (3U)                                           /**< (SUPC_BODCORE) Action when Threshold Crossed Position */
#define SUPC_BODCORE_ACTION_Msk               (0x3U << SUPC_BODCORE_ACTION_Pos)              /**< (SUPC_BODCORE) Action when Threshold Crossed Mask */
#define SUPC_BODCORE_ACTION(value)            (SUPC_BODCORE_ACTION_Msk & ((value) << SUPC_BODCORE_ACTION_Pos))
#define   SUPC_BODCORE_ACTION_NONE_Val        (0U)                                           /**< (SUPC_BODCORE) No action  */
#define   SUPC_BODCORE_ACTION_RESET_Val       (1U)                                           /**< (SUPC_BODCORE) The BODCORE generates a reset  */
#define   SUPC_BODCORE_ACTION_INT_Val         (2U)                                           /**< (SUPC_BODCORE) The BODCORE generates an interrupt  */
#define SUPC_BODCORE_ACTION_NONE              (SUPC_BODCORE_ACTION_NONE_Val << SUPC_BODCORE_ACTION_Pos) /**< (SUPC_BODCORE) No action Position  */
#define SUPC_BODCORE_ACTION_RESET             (SUPC_BODCORE_ACTION_RESET_Val << SUPC_BODCORE_ACTION_Pos) /**< (SUPC_BODCORE) The BODCORE generates a reset Position  */
#define SUPC_BODCORE_ACTION_INT               (SUPC_BODCORE_ACTION_INT_Val << SUPC_BODCORE_ACTION_Pos) /**< (SUPC_BODCORE) The BODCORE generates an interrupt Position  */
#define SUPC_BODCORE_STDBYCFG_Pos             (5U)                                           /**< (SUPC_BODCORE) Configuration in Standby mode Position */
#define SUPC_BODCORE_STDBYCFG_Msk             (0x1U << SUPC_BODCORE_STDBYCFG_Pos)            /**< (SUPC_BODCORE) Configuration in Standby mode Mask */
#define SUPC_BODCORE_STDBYCFG(value)          (SUPC_BODCORE_STDBYCFG_Msk & ((value) << SUPC_BODCORE_STDBYCFG_Pos))
#define SUPC_BODCORE_RUNSTDBY_Pos             (6U)                                           /**< (SUPC_BODCORE) Run during Standby Position */
#define SUPC_BODCORE_RUNSTDBY_Msk             (0x1U << SUPC_BODCORE_RUNSTDBY_Pos)            /**< (SUPC_BODCORE) Run during Standby Mask */
#define SUPC_BODCORE_RUNSTDBY(value)          (SUPC_BODCORE_RUNSTDBY_Msk & ((value) << SUPC_BODCORE_RUNSTDBY_Pos))
#define SUPC_BODCORE_ACTCFG_Pos               (8U)                                           /**< (SUPC_BODCORE) Configuration in Active mode Position */
#define SUPC_BODCORE_ACTCFG_Msk               (0x1U << SUPC_BODCORE_ACTCFG_Pos)              /**< (SUPC_BODCORE) Configuration in Active mode Mask */
#define SUPC_BODCORE_ACTCFG(value)            (SUPC_BODCORE_ACTCFG_Msk & ((value) << SUPC_BODCORE_ACTCFG_Pos))
#define SUPC_BODCORE_PSEL_Pos                 (12U)                                          /**< (SUPC_BODCORE) Prescaler Select Position */
#define SUPC_BODCORE_PSEL_Msk                 (0xFU << SUPC_BODCORE_PSEL_Pos)                /**< (SUPC_BODCORE) Prescaler Select Mask */
#define SUPC_BODCORE_PSEL(value)              (SUPC_BODCORE_PSEL_Msk & ((value) << SUPC_BODCORE_PSEL_Pos))
#define   SUPC_BODCORE_PSEL_DIV2_Val          (0U)                                           /**< (SUPC_BODCORE) Divide clock by 2  */
#define   SUPC_BODCORE_PSEL_DIV4_Val          (1U)                                           /**< (SUPC_BODCORE) Divide clock by 4  */
#define   SUPC_BODCORE_PSEL_DIV8_Val          (2U)                                           /**< (SUPC_BODCORE) Divide clock by 8  */
#define   SUPC_BODCORE_PSEL_DIV16_Val         (3U)                                           /**< (SUPC_BODCORE) Divide clock by 16  */
#define   SUPC_BODCORE_PSEL_DIV32_Val         (4U)                                           /**< (SUPC_BODCORE) Divide clock by 32  */
#define   SUPC_BODCORE_PSEL_DIV64_Val         (5U)                                           /**< (SUPC_BODCORE) Divide clock by 64  */
#define   SUPC_BODCORE_PSEL_DIV128_Val        (6U)                                           /**< (SUPC_BODCORE) Divide clock by 128  */
#define   SUPC_BODCORE_PSEL_DIV256_Val        (7U)                                           /**< (SUPC_BODCORE) Divide clock by 256  */
#define   SUPC_BODCORE_PSEL_DIV512_Val        (8U)                                           /**< (SUPC_BODCORE) Divide clock by 512  */
#define   SUPC_BODCORE_PSEL_DIV1024_Val       (9U)                                           /**< (SUPC_BODCORE) Divide clock by 1024  */
#define   SUPC_BODCORE_PSEL_DIV2048_Val       (10U)                                          /**< (SUPC_BODCORE) Divide clock by 2048  */
#define   SUPC_BODCORE_PSEL_DIV4096_Val       (11U)                                          /**< (SUPC_BODCORE) Divide clock by 4096  */
#define   SUPC_BODCORE_PSEL_DIV8192_Val       (12U)                                          /**< (SUPC_BODCORE) Divide clock by 8192  */
#define   SUPC_BODCORE_PSEL_DIV16384_Val      (13U)                                          /**< (SUPC_BODCORE) Divide clock by 16384  */
#define   SUPC_BODCORE_PSEL_DIV32768_Val      (14U)                                          /**< (SUPC_BODCORE) Divide clock by 32768  */
#define   SUPC_BODCORE_PSEL_DIV65536_Val      (15U)                                          /**< (SUPC_BODCORE) Divide clock by 65536  */
#define SUPC_BODCORE_PSEL_DIV2                (SUPC_BODCORE_PSEL_DIV2_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 2 Position  */
#define SUPC_BODCORE_PSEL_DIV4                (SUPC_BODCORE_PSEL_DIV4_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 4 Position  */
#define SUPC_BODCORE_PSEL_DIV8                (SUPC_BODCORE_PSEL_DIV8_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 8 Position  */
#define SUPC_BODCORE_PSEL_DIV16               (SUPC_BODCORE_PSEL_DIV16_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 16 Position  */
#define SUPC_BODCORE_PSEL_DIV32               (SUPC_BODCORE_PSEL_DIV32_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 32 Position  */
#define SUPC_BODCORE_PSEL_DIV64               (SUPC_BODCORE_PSEL_DIV64_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 64 Position  */
#define SUPC_BODCORE_PSEL_DIV128              (SUPC_BODCORE_PSEL_DIV128_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 128 Position  */
#define SUPC_BODCORE_PSEL_DIV256              (SUPC_BODCORE_PSEL_DIV256_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 256 Position  */
#define SUPC_BODCORE_PSEL_DIV512              (SUPC_BODCORE_PSEL_DIV512_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 512 Position  */
#define SUPC_BODCORE_PSEL_DIV1024             (SUPC_BODCORE_PSEL_DIV1024_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 1024 Position  */
#define SUPC_BODCORE_PSEL_DIV2048             (SUPC_BODCORE_PSEL_DIV2048_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 2048 Position  */
#define SUPC_BODCORE_PSEL_DIV4096             (SUPC_BODCORE_PSEL_DIV4096_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 4096 Position  */
#define SUPC_BODCORE_PSEL_DIV8192             (SUPC_BODCORE_PSEL_DIV8192_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 8192 Position  */
#define SUPC_BODCORE_PSEL_DIV16384            (SUPC_BODCORE_PSEL_DIV16384_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 16384 Position  */
#define SUPC_BODCORE_PSEL_DIV32768            (SUPC_BODCORE_PSEL_DIV32768_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 32768 Position  */
#define SUPC_BODCORE_PSEL_DIV65536            (SUPC_BODCORE_PSEL_DIV65536_Val << SUPC_BODCORE_PSEL_Pos) /**< (SUPC_BODCORE) Divide clock by 65536 Position  */
#define SUPC_BODCORE_LEVEL_Pos                (16U)                                          /**< (SUPC_BODCORE) Threshold Level Position */
#define SUPC_BODCORE_LEVEL_Msk                (0x3FU << SUPC_BODCORE_LEVEL_Pos)              /**< (SUPC_BODCORE) Threshold Level Mask */
#define SUPC_BODCORE_LEVEL(value)             (SUPC_BODCORE_LEVEL_Msk & ((value) << SUPC_BODCORE_LEVEL_Pos))
#define SUPC_BODCORE_Msk                      (0x003FF17EUL)                                 /**< (SUPC_BODCORE) Register Mask  */

/* -------- SUPC_VREG : (SUPC Offset: 0x18) (R/W 32) VREG Control -------- */
#define SUPC_VREG_ENABLE_Pos                  (1U)                                           /**< (SUPC_VREG) Enable Position */
#define SUPC_VREG_ENABLE_Msk                  (0x1U << SUPC_VREG_ENABLE_Pos)                 /**< (SUPC_VREG) Enable Mask */
#define SUPC_VREG_ENABLE(value)               (SUPC_VREG_ENABLE_Msk & ((value) << SUPC_VREG_ENABLE_Pos))
#define SUPC_VREG_RUNSTDBY_Pos                (6U)                                           /**< (SUPC_VREG) Run during Standby Position */
#define SUPC_VREG_RUNSTDBY_Msk                (0x1U << SUPC_VREG_RUNSTDBY_Pos)               /**< (SUPC_VREG) Run during Standby Mask */
#define SUPC_VREG_RUNSTDBY(value)             (SUPC_VREG_RUNSTDBY_Msk & ((value) << SUPC_VREG_RUNSTDBY_Pos))
#define SUPC_VREG_Msk                         (0x00000042UL)                                 /**< (SUPC_VREG) Register Mask  */

/* -------- SUPC_VREF : (SUPC Offset: 0x1C) (R/W 32) VREF Control -------- */
#define SUPC_VREF_TSEN_Pos                    (1U)                                           /**< (SUPC_VREF) Temperature Sensor Output Enable Position */
#define SUPC_VREF_TSEN_Msk                    (0x1U << SUPC_VREF_TSEN_Pos)                   /**< (SUPC_VREF) Temperature Sensor Output Enable Mask */
#define SUPC_VREF_TSEN(value)                 (SUPC_VREF_TSEN_Msk & ((value) << SUPC_VREF_TSEN_Pos))
#define SUPC_VREF_VREFOE_Pos                  (2U)                                           /**< (SUPC_VREF) Voltage Reference Output Enable Position */
#define SUPC_VREF_VREFOE_Msk                  (0x1U << SUPC_VREF_VREFOE_Pos)                 /**< (SUPC_VREF) Voltage Reference Output Enable Mask */
#define SUPC_VREF_VREFOE(value)               (SUPC_VREF_VREFOE_Msk & ((value) << SUPC_VREF_VREFOE_Pos))
#define SUPC_VREF_RUNSTDBY_Pos                (6U)                                           /**< (SUPC_VREF) Run during Standby Position */
#define SUPC_VREF_RUNSTDBY_Msk                (0x1U << SUPC_VREF_RUNSTDBY_Pos)               /**< (SUPC_VREF) Run during Standby Mask */
#define SUPC_VREF_RUNSTDBY(value)             (SUPC_VREF_RUNSTDBY_Msk & ((value) << SUPC_VREF_RUNSTDBY_Pos))
#define SUPC_VREF_ONDEMAND_Pos                (7U)                                           /**< (SUPC_VREF) On Demand Control Position */
#define SUPC_VREF_ONDEMAND_Msk                (0x1U << SUPC_VREF_ONDEMAND_Pos)               /**< (SUPC_VREF) On Demand Control Mask */
#define SUPC_VREF_ONDEMAND(value)             (SUPC_VREF_ONDEMAND_Msk & ((value) << SUPC_VREF_ONDEMAND_Pos))
#define SUPC_VREF_SEL_Pos                     (16U)                                          /**< (SUPC_VREF) Voltage Reference Selection Position */
#define SUPC_VREF_SEL_Msk                     (0xFU << SUPC_VREF_SEL_Pos)                    /**< (SUPC_VREF) Voltage Reference Selection Mask */
#define SUPC_VREF_SEL(value)                  (SUPC_VREF_SEL_Msk & ((value) << SUPC_VREF_SEL_Pos))
#define   SUPC_VREF_SEL_1V024_Val             (0U)                                           /**< (SUPC_VREF) 1.024V voltage reference typical value  */
#define   SUPC_VREF_SEL_2V048_Val             (2U)                                           /**< (SUPC_VREF) 2.048V voltage reference typical value  */
#define   SUPC_VREF_SEL_4V096_Val             (3U)                                           /**< (SUPC_VREF) 4.096V voltage reference typical value  */
#define SUPC_VREF_SEL_1V024                   (SUPC_VREF_SEL_1V024_Val << SUPC_VREF_SEL_Pos) /**< (SUPC_VREF) 1.024V voltage reference typical value Position  */
#define SUPC_VREF_SEL_2V048                   (SUPC_VREF_SEL_2V048_Val << SUPC_VREF_SEL_Pos) /**< (SUPC_VREF) 2.048V voltage reference typical value Position  */
#define SUPC_VREF_SEL_4V096                   (SUPC_VREF_SEL_4V096_Val << SUPC_VREF_SEL_Pos) /**< (SUPC_VREF) 4.096V voltage reference typical value Position  */
#define SUPC_VREF_Msk                         (0x000F00C6UL)                                 /**< (SUPC_VREF) Register Mask  */

/* -------- SUPC_VREG33 : (SUPC Offset: 0x20) (R/W 32) VREG33 Control -------- */
#define SUPC_VREG33_ENABLE_Pos                (1U)                                           /**< (SUPC_VREG33) VREG33 Enable Position */
#define SUPC_VREG33_ENABLE_Msk                (0x1U << SUPC_VREG33_ENABLE_Pos)               /**< (SUPC_VREG33) VREG33 Enable Mask */
#define SUPC_VREG33_ENABLE(value)             (SUPC_VREG33_ENABLE_Msk & ((value) << SUPC_VREG33_ENABLE_Pos))
#define SUPC_VREG33_ENRDY_Pos                 (2U)                                           /**< (SUPC_VREG33) VREG33 Ready Enable Position */
#define SUPC_VREG33_ENRDY_Msk                 (0x1U << SUPC_VREG33_ENRDY_Pos)                /**< (SUPC_VREG33) VREG33 Ready Enable Mask */
#define SUPC_VREG33_ENRDY(value)              (SUPC_VREG33_ENRDY_Msk & ((value) << SUPC_VREG33_ENRDY_Pos))
#define SUPC_VREG33_BYPASS_Pos                (3U)                                           /**< (SUPC_VREG33) VREG33 Bypass Position */
#define SUPC_VREG33_BYPASS_Msk                (0x1U << SUPC_VREG33_BYPASS_Pos)               /**< (SUPC_VREG33) VREG33 Bypass Mask */
#define SUPC_VREG33_BYPASS(value)             (SUPC_VREG33_BYPASS_Msk & ((value) << SUPC_VREG33_BYPASS_Pos))
#define SUPC_VREG33_ISOEN_Pos                 (4U)                                           /**< (SUPC_VREG33) Isolation Enable Position */
#define SUPC_VREG33_ISOEN_Msk                 (0x1U << SUPC_VREG33_ISOEN_Pos)                /**< (SUPC_VREG33) Isolation Enable Mask */
#define SUPC_VREG33_ISOEN(value)              (SUPC_VREG33_ISOEN_Msk & ((value) << SUPC_VREG33_ISOEN_Pos))
#define SUPC_VREG33_Msk                       (0x0000001EUL)                                 /**< (SUPC_VREG33) Register Mask  */

/** \brief SUPC register offsets definitions */
#define SUPC_INTENCLR_OFFSET           (0x00)         /**< (SUPC_INTENCLR) Interrupt Enable Clear Offset */
#define SUPC_INTENSET_OFFSET           (0x04)         /**< (SUPC_INTENSET) Interrupt Enable Set Offset */
#define SUPC_INTFLAG_OFFSET            (0x08)         /**< (SUPC_INTFLAG) Interrupt Flag Status and Clear Offset */
#define SUPC_STATUS_OFFSET             (0x0C)         /**< (SUPC_STATUS) Power and Clocks Status Offset */
#define SUPC_BODVDD_OFFSET             (0x10)         /**< (SUPC_BODVDD) BODVDD Control Offset */
#define SUPC_BODCORE_OFFSET            (0x14)         /**< (SUPC_BODCORE) BODCORE Control Offset */
#define SUPC_VREG_OFFSET               (0x18)         /**< (SUPC_VREG) VREG Control Offset */
#define SUPC_VREF_OFFSET               (0x1C)         /**< (SUPC_VREF) VREF Control Offset */
#define SUPC_VREG33_OFFSET             (0x20)         /**< (SUPC_VREG33) VREG33 Control Offset */

/** \brief SUPC register API structure */
typedef struct
{
  __IO  uint32_t                       SUPC_INTENCLR;   /**< Offset: 0x00 (R/W  32) Interrupt Enable Clear */
  __IO  uint32_t                       SUPC_INTENSET;   /**< Offset: 0x04 (R/W  32) Interrupt Enable Set */
  __IO  uint32_t                       SUPC_INTFLAG;    /**< Offset: 0x08 (R/W  32) Interrupt Flag Status and Clear */
  __I   uint32_t                       SUPC_STATUS;     /**< Offset: 0x0c (R/   32) Power and Clocks Status */
  __IO  uint32_t                       SUPC_BODVDD;     /**< Offset: 0x10 (R/W  32) BODVDD Control */
  __IO  uint32_t                       SUPC_BODCORE;    /**< Offset: 0x14 (R/W  32) BODCORE Control */
  __IO  uint32_t                       SUPC_VREG;       /**< Offset: 0x18 (R/W  32) VREG Control */
  __IO  uint32_t                       SUPC_VREF;       /**< Offset: 0x1c (R/W  32) VREF Control */
  __IO  uint32_t                       SUPC_VREG33;     /**< Offset: 0x20 (R/W  32) VREG33 Control */
} supc_registers_t;
/** @}  end of Supply Controller */

#endif /* SAMC_SAMC21_SUPC_MODULE_H */

