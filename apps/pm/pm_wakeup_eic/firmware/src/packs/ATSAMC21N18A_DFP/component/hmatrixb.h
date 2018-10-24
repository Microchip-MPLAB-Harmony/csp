/**
 * \brief Header file for SAMC/SAMC21 HMATRIXB
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
#ifndef SAMC_SAMC21_HMATRIXB_MODULE_H
#define SAMC_SAMC21_HMATRIXB_MODULE_H

/** \addtogroup SAMC_SAMC21 HSB Matrix
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_HMATRIXB                              */
/* ========================================================================== */

/* -------- HMATRIXB_MCFG : (HMATRIXB Offset: 0x00) (R/W 32) Master Configuration -------- */
#define HMATRIXB_MCFG_ULBT_Pos                (0U)                                           /**< (HMATRIXB_MCFG) Undefined Length Burst Type Position */
#define HMATRIXB_MCFG_ULBT_Msk                (0x7U << HMATRIXB_MCFG_ULBT_Pos)               /**< (HMATRIXB_MCFG) Undefined Length Burst Type Mask */
#define HMATRIXB_MCFG_ULBT(value)             (HMATRIXB_MCFG_ULBT_Msk & ((value) << HMATRIXB_MCFG_ULBT_Pos))
#define   HMATRIXB_MCFG_ULBT_INFINITE_Val     (0U)                                           /**< (HMATRIXB_MCFG) Infinite Length  */
#define   HMATRIXB_MCFG_ULBT_SINGLE_Val       (1U)                                           /**< (HMATRIXB_MCFG) Single Access  */
#define   HMATRIXB_MCFG_ULBT_FOUR_BEAT_Val    (2U)                                           /**< (HMATRIXB_MCFG) Four Beat Burst  */
#define   HMATRIXB_MCFG_ULBT_EIGHT_BEAT_Val   (3U)                                           /**< (HMATRIXB_MCFG) Eight Beat Burst  */
#define   HMATRIXB_MCFG_ULBT_SIXTEEN_BEAT_Val (4U)                                           /**< (HMATRIXB_MCFG) Sixteen Beat Burst  */
#define HMATRIXB_MCFG_ULBT_INFINITE           (HMATRIXB_MCFG_ULBT_INFINITE_Val << HMATRIXB_MCFG_ULBT_Pos) /**< (HMATRIXB_MCFG) Infinite Length Position  */
#define HMATRIXB_MCFG_ULBT_SINGLE             (HMATRIXB_MCFG_ULBT_SINGLE_Val << HMATRIXB_MCFG_ULBT_Pos) /**< (HMATRIXB_MCFG) Single Access Position  */
#define HMATRIXB_MCFG_ULBT_FOUR_BEAT          (HMATRIXB_MCFG_ULBT_FOUR_BEAT_Val << HMATRIXB_MCFG_ULBT_Pos) /**< (HMATRIXB_MCFG) Four Beat Burst Position  */
#define HMATRIXB_MCFG_ULBT_EIGHT_BEAT         (HMATRIXB_MCFG_ULBT_EIGHT_BEAT_Val << HMATRIXB_MCFG_ULBT_Pos) /**< (HMATRIXB_MCFG) Eight Beat Burst Position  */
#define HMATRIXB_MCFG_ULBT_SIXTEEN_BEAT       (HMATRIXB_MCFG_ULBT_SIXTEEN_BEAT_Val << HMATRIXB_MCFG_ULBT_Pos) /**< (HMATRIXB_MCFG) Sixteen Beat Burst Position  */
#define HMATRIXB_MCFG_Msk                     (0x00000007UL)                                 /**< (HMATRIXB_MCFG) Register Mask  */

/* -------- HMATRIXB_SCFG : (HMATRIXB Offset: 0x40) (R/W 32) Slave Configuration -------- */
#define HMATRIXB_SCFG_SLOT_CYCLE_Pos          (0U)                                           /**< (HMATRIXB_SCFG) Maximum Number of Allowed Cycles for a Burst Position */
#define HMATRIXB_SCFG_SLOT_CYCLE_Msk          (0xFFU << HMATRIXB_SCFG_SLOT_CYCLE_Pos)        /**< (HMATRIXB_SCFG) Maximum Number of Allowed Cycles for a Burst Mask */
#define HMATRIXB_SCFG_SLOT_CYCLE(value)       (HMATRIXB_SCFG_SLOT_CYCLE_Msk & ((value) << HMATRIXB_SCFG_SLOT_CYCLE_Pos))
#define HMATRIXB_SCFG_DEFMSTR_TYPE_Pos        (16U)                                          /**< (HMATRIXB_SCFG) Default Master Type Position */
#define HMATRIXB_SCFG_DEFMSTR_TYPE_Msk        (0x3U << HMATRIXB_SCFG_DEFMSTR_TYPE_Pos)       /**< (HMATRIXB_SCFG) Default Master Type Mask */
#define HMATRIXB_SCFG_DEFMSTR_TYPE(value)     (HMATRIXB_SCFG_DEFMSTR_TYPE_Msk & ((value) << HMATRIXB_SCFG_DEFMSTR_TYPE_Pos))
#define   HMATRIXB_SCFG_DEFMSTR_TYPE_NO_DEFAULT_Val (0U)                                           /**< (HMATRIXB_SCFG) No Default Master. At the end of current slave access, if no other master request is pending, the slave is deconnected from all masters. This resusts in having a one cycle latency for the first transfer of a burst.  */
#define   HMATRIXB_SCFG_DEFMSTR_TYPE_LAST_DEFAULT_Val (1U)                                           /**< (HMATRIXB_SCFG) Last Default Master At the end of current slave access, if no other master request is pending, the slave stay connected with the last master havingaccessed it.This resusts in not having the one cycle latency when the last master re-trying access on the slave.  */
#define   HMATRIXB_SCFG_DEFMSTR_TYPE_FIXED_DEFAULT_Val (2U)                                           /**< (HMATRIXB_SCFG) Fixed Default Master At the end of current slave access, if no other master request is pending, the slave connects with fixed master which numberis in FIXED_DEFMSTR register.This resusts in not having the one cycle latency when the fixed master re-trying access on the slave.  */
#define HMATRIXB_SCFG_DEFMSTR_TYPE_NO_DEFAULT (HMATRIXB_SCFG_DEFMSTR_TYPE_NO_DEFAULT_Val << HMATRIXB_SCFG_DEFMSTR_TYPE_Pos) /**< (HMATRIXB_SCFG) No Default Master. At the end of current slave access, if no other master request is pending, the slave is deconnected from all masters. This resusts in having a one cycle latency for the first transfer of a burst. Position  */
#define HMATRIXB_SCFG_DEFMSTR_TYPE_LAST_DEFAULT (HMATRIXB_SCFG_DEFMSTR_TYPE_LAST_DEFAULT_Val << HMATRIXB_SCFG_DEFMSTR_TYPE_Pos) /**< (HMATRIXB_SCFG) Last Default Master At the end of current slave access, if no other master request is pending, the slave stay connected with the last master havingaccessed it.This resusts in not having the one cycle latency when the last master re-trying access on the slave. Position  */
#define HMATRIXB_SCFG_DEFMSTR_TYPE_FIXED_DEFAULT (HMATRIXB_SCFG_DEFMSTR_TYPE_FIXED_DEFAULT_Val << HMATRIXB_SCFG_DEFMSTR_TYPE_Pos) /**< (HMATRIXB_SCFG) Fixed Default Master At the end of current slave access, if no other master request is pending, the slave connects with fixed master which numberis in FIXED_DEFMSTR register.This resusts in not having the one cycle latency when the fixed master re-trying access on the slave. Position  */
#define HMATRIXB_SCFG_FIXED_DEFMSTR_Pos       (18U)                                          /**< (HMATRIXB_SCFG) Fixed Index of Default Master Position */
#define HMATRIXB_SCFG_FIXED_DEFMSTR_Msk       (0xFU << HMATRIXB_SCFG_FIXED_DEFMSTR_Pos)      /**< (HMATRIXB_SCFG) Fixed Index of Default Master Mask */
#define HMATRIXB_SCFG_FIXED_DEFMSTR(value)    (HMATRIXB_SCFG_FIXED_DEFMSTR_Msk & ((value) << HMATRIXB_SCFG_FIXED_DEFMSTR_Pos))
#define HMATRIXB_SCFG_ARBT_Pos                (24U)                                          /**< (HMATRIXB_SCFG) Arbitration Type Position */
#define HMATRIXB_SCFG_ARBT_Msk                (0x1U << HMATRIXB_SCFG_ARBT_Pos)               /**< (HMATRIXB_SCFG) Arbitration Type Mask */
#define HMATRIXB_SCFG_ARBT(value)             (HMATRIXB_SCFG_ARBT_Msk & ((value) << HMATRIXB_SCFG_ARBT_Pos))
#define   HMATRIXB_SCFG_ARBT_ROUND_ROBIN_Val  (0U)                                           /**< (HMATRIXB_SCFG) Round-Robin Arbitration  */
#define   HMATRIXB_SCFG_ARBT_FIXED_PRIORITY_Val (1U)                                           /**< (HMATRIXB_SCFG) Fixed Priority Arbitration  */
#define HMATRIXB_SCFG_ARBT_ROUND_ROBIN        (HMATRIXB_SCFG_ARBT_ROUND_ROBIN_Val << HMATRIXB_SCFG_ARBT_Pos) /**< (HMATRIXB_SCFG) Round-Robin Arbitration Position  */
#define HMATRIXB_SCFG_ARBT_FIXED_PRIORITY     (HMATRIXB_SCFG_ARBT_FIXED_PRIORITY_Val << HMATRIXB_SCFG_ARBT_Pos) /**< (HMATRIXB_SCFG) Fixed Priority Arbitration Position  */
#define HMATRIXB_SCFG_Msk                     (0x013F00FFUL)                                 /**< (HMATRIXB_SCFG) Register Mask  */

/* -------- PRS_PRAS : (HMATRIXB Offset: 0x00) (R/W 32) Priority A for Slave -------- */
#define PRS_PRAS_M0PR_Pos                     (0U)                                           /**< (PRS_PRAS) Master 0 Priority Position */
#define PRS_PRAS_M0PR_Msk                     (0xFU << PRS_PRAS_M0PR_Pos)                    /**< (PRS_PRAS) Master 0 Priority Mask */
#define PRS_PRAS_M0PR(value)                  (PRS_PRAS_M0PR_Msk & ((value) << PRS_PRAS_M0PR_Pos))
#define PRS_PRAS_M1PR_Pos                     (4U)                                           /**< (PRS_PRAS) Master 1 Priority Position */
#define PRS_PRAS_M1PR_Msk                     (0xFU << PRS_PRAS_M1PR_Pos)                    /**< (PRS_PRAS) Master 1 Priority Mask */
#define PRS_PRAS_M1PR(value)                  (PRS_PRAS_M1PR_Msk & ((value) << PRS_PRAS_M1PR_Pos))
#define PRS_PRAS_M2PR_Pos                     (8U)                                           /**< (PRS_PRAS) Master 2 Priority Position */
#define PRS_PRAS_M2PR_Msk                     (0xFU << PRS_PRAS_M2PR_Pos)                    /**< (PRS_PRAS) Master 2 Priority Mask */
#define PRS_PRAS_M2PR(value)                  (PRS_PRAS_M2PR_Msk & ((value) << PRS_PRAS_M2PR_Pos))
#define PRS_PRAS_M3PR_Pos                     (12U)                                          /**< (PRS_PRAS) Master 3 Priority Position */
#define PRS_PRAS_M3PR_Msk                     (0xFU << PRS_PRAS_M3PR_Pos)                    /**< (PRS_PRAS) Master 3 Priority Mask */
#define PRS_PRAS_M3PR(value)                  (PRS_PRAS_M3PR_Msk & ((value) << PRS_PRAS_M3PR_Pos))
#define PRS_PRAS_M4PR_Pos                     (16U)                                          /**< (PRS_PRAS) Master 4 Priority Position */
#define PRS_PRAS_M4PR_Msk                     (0xFU << PRS_PRAS_M4PR_Pos)                    /**< (PRS_PRAS) Master 4 Priority Mask */
#define PRS_PRAS_M4PR(value)                  (PRS_PRAS_M4PR_Msk & ((value) << PRS_PRAS_M4PR_Pos))
#define PRS_PRAS_M5PR_Pos                     (20U)                                          /**< (PRS_PRAS) Master 5 Priority Position */
#define PRS_PRAS_M5PR_Msk                     (0xFU << PRS_PRAS_M5PR_Pos)                    /**< (PRS_PRAS) Master 5 Priority Mask */
#define PRS_PRAS_M5PR(value)                  (PRS_PRAS_M5PR_Msk & ((value) << PRS_PRAS_M5PR_Pos))
#define PRS_PRAS_M6PR_Pos                     (24U)                                          /**< (PRS_PRAS) Master 6 Priority Position */
#define PRS_PRAS_M6PR_Msk                     (0xFU << PRS_PRAS_M6PR_Pos)                    /**< (PRS_PRAS) Master 6 Priority Mask */
#define PRS_PRAS_M6PR(value)                  (PRS_PRAS_M6PR_Msk & ((value) << PRS_PRAS_M6PR_Pos))
#define PRS_PRAS_M7PR_Pos                     (28U)                                          /**< (PRS_PRAS) Master 7 Priority Position */
#define PRS_PRAS_M7PR_Msk                     (0xFU << PRS_PRAS_M7PR_Pos)                    /**< (PRS_PRAS) Master 7 Priority Mask */
#define PRS_PRAS_M7PR(value)                  (PRS_PRAS_M7PR_Msk & ((value) << PRS_PRAS_M7PR_Pos))
#define PRS_PRAS_Msk                          (0xFFFFFFFFUL)                                 /**< (PRS_PRAS) Register Mask  */

/* -------- PRS_PRBS : (HMATRIXB Offset: 0x04) (R/W 32) Priority B for Slave -------- */
#define PRS_PRBS_M8PR_Pos                     (0U)                                           /**< (PRS_PRBS) Master 8 Priority Position */
#define PRS_PRBS_M8PR_Msk                     (0xFU << PRS_PRBS_M8PR_Pos)                    /**< (PRS_PRBS) Master 8 Priority Mask */
#define PRS_PRBS_M8PR(value)                  (PRS_PRBS_M8PR_Msk & ((value) << PRS_PRBS_M8PR_Pos))
#define PRS_PRBS_M9PR_Pos                     (4U)                                           /**< (PRS_PRBS) Master 9 Priority Position */
#define PRS_PRBS_M9PR_Msk                     (0xFU << PRS_PRBS_M9PR_Pos)                    /**< (PRS_PRBS) Master 9 Priority Mask */
#define PRS_PRBS_M9PR(value)                  (PRS_PRBS_M9PR_Msk & ((value) << PRS_PRBS_M9PR_Pos))
#define PRS_PRBS_M10PR_Pos                    (8U)                                           /**< (PRS_PRBS) Master 10 Priority Position */
#define PRS_PRBS_M10PR_Msk                    (0xFU << PRS_PRBS_M10PR_Pos)                   /**< (PRS_PRBS) Master 10 Priority Mask */
#define PRS_PRBS_M10PR(value)                 (PRS_PRBS_M10PR_Msk & ((value) << PRS_PRBS_M10PR_Pos))
#define PRS_PRBS_M11PR_Pos                    (12U)                                          /**< (PRS_PRBS) Master 11 Priority Position */
#define PRS_PRBS_M11PR_Msk                    (0xFU << PRS_PRBS_M11PR_Pos)                   /**< (PRS_PRBS) Master 11 Priority Mask */
#define PRS_PRBS_M11PR(value)                 (PRS_PRBS_M11PR_Msk & ((value) << PRS_PRBS_M11PR_Pos))
#define PRS_PRBS_M12PR_Pos                    (16U)                                          /**< (PRS_PRBS) Master 12 Priority Position */
#define PRS_PRBS_M12PR_Msk                    (0xFU << PRS_PRBS_M12PR_Pos)                   /**< (PRS_PRBS) Master 12 Priority Mask */
#define PRS_PRBS_M12PR(value)                 (PRS_PRBS_M12PR_Msk & ((value) << PRS_PRBS_M12PR_Pos))
#define PRS_PRBS_M13PR_Pos                    (20U)                                          /**< (PRS_PRBS) Master 13 Priority Position */
#define PRS_PRBS_M13PR_Msk                    (0xFU << PRS_PRBS_M13PR_Pos)                   /**< (PRS_PRBS) Master 13 Priority Mask */
#define PRS_PRBS_M13PR(value)                 (PRS_PRBS_M13PR_Msk & ((value) << PRS_PRBS_M13PR_Pos))
#define PRS_PRBS_M14PR_Pos                    (24U)                                          /**< (PRS_PRBS) Master 14 Priority Position */
#define PRS_PRBS_M14PR_Msk                    (0xFU << PRS_PRBS_M14PR_Pos)                   /**< (PRS_PRBS) Master 14 Priority Mask */
#define PRS_PRBS_M14PR(value)                 (PRS_PRBS_M14PR_Msk & ((value) << PRS_PRBS_M14PR_Pos))
#define PRS_PRBS_M15PR_Pos                    (28U)                                          /**< (PRS_PRBS) Master 15 Priority Position */
#define PRS_PRBS_M15PR_Msk                    (0xFU << PRS_PRBS_M15PR_Pos)                   /**< (PRS_PRBS) Master 15 Priority Mask */
#define PRS_PRBS_M15PR(value)                 (PRS_PRBS_M15PR_Msk & ((value) << PRS_PRBS_M15PR_Pos))
#define PRS_PRBS_Msk                          (0xFFFFFFFFUL)                                 /**< (PRS_PRBS) Register Mask  */

/* -------- HMATRIXB_MRCR : (HMATRIXB Offset: 0x100) (R/W 32) Master Remap Control -------- */
#define HMATRIXB_MRCR_RCB0_Pos                (0U)                                           /**< (HMATRIXB_MRCR) Remap Command Bit for Master 0 Position */
#define HMATRIXB_MRCR_RCB0_Msk                (0x1U << HMATRIXB_MRCR_RCB0_Pos)               /**< (HMATRIXB_MRCR) Remap Command Bit for Master 0 Mask */
#define HMATRIXB_MRCR_RCB0(value)             (HMATRIXB_MRCR_RCB0_Msk & ((value) << HMATRIXB_MRCR_RCB0_Pos))
#define   HMATRIXB_MRCR_RCB0_DIS_Val          (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB0_ENA_Val          (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB0_DIS                (HMATRIXB_MRCR_RCB0_DIS_Val << HMATRIXB_MRCR_RCB0_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB0_ENA                (HMATRIXB_MRCR_RCB0_ENA_Val << HMATRIXB_MRCR_RCB0_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB1_Pos                (1U)                                           /**< (HMATRIXB_MRCR) Remap Command Bit for Master 1 Position */
#define HMATRIXB_MRCR_RCB1_Msk                (0x1U << HMATRIXB_MRCR_RCB1_Pos)               /**< (HMATRIXB_MRCR) Remap Command Bit for Master 1 Mask */
#define HMATRIXB_MRCR_RCB1(value)             (HMATRIXB_MRCR_RCB1_Msk & ((value) << HMATRIXB_MRCR_RCB1_Pos))
#define   HMATRIXB_MRCR_RCB1_DIS_Val          (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB1_ENA_Val          (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB1_DIS                (HMATRIXB_MRCR_RCB1_DIS_Val << HMATRIXB_MRCR_RCB1_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB1_ENA                (HMATRIXB_MRCR_RCB1_ENA_Val << HMATRIXB_MRCR_RCB1_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB2_Pos                (2U)                                           /**< (HMATRIXB_MRCR) Remap Command Bit for Master 2 Position */
#define HMATRIXB_MRCR_RCB2_Msk                (0x1U << HMATRIXB_MRCR_RCB2_Pos)               /**< (HMATRIXB_MRCR) Remap Command Bit for Master 2 Mask */
#define HMATRIXB_MRCR_RCB2(value)             (HMATRIXB_MRCR_RCB2_Msk & ((value) << HMATRIXB_MRCR_RCB2_Pos))
#define   HMATRIXB_MRCR_RCB2_DIS_Val          (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB2_ENA_Val          (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB2_DIS                (HMATRIXB_MRCR_RCB2_DIS_Val << HMATRIXB_MRCR_RCB2_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB2_ENA                (HMATRIXB_MRCR_RCB2_ENA_Val << HMATRIXB_MRCR_RCB2_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB3_Pos                (3U)                                           /**< (HMATRIXB_MRCR) Remap Command Bit for Master 3 Position */
#define HMATRIXB_MRCR_RCB3_Msk                (0x1U << HMATRIXB_MRCR_RCB3_Pos)               /**< (HMATRIXB_MRCR) Remap Command Bit for Master 3 Mask */
#define HMATRIXB_MRCR_RCB3(value)             (HMATRIXB_MRCR_RCB3_Msk & ((value) << HMATRIXB_MRCR_RCB3_Pos))
#define   HMATRIXB_MRCR_RCB3_DIS_Val          (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB3_ENA_Val          (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB3_DIS                (HMATRIXB_MRCR_RCB3_DIS_Val << HMATRIXB_MRCR_RCB3_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB3_ENA                (HMATRIXB_MRCR_RCB3_ENA_Val << HMATRIXB_MRCR_RCB3_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB4_Pos                (4U)                                           /**< (HMATRIXB_MRCR) Remap Command Bit for Master 4 Position */
#define HMATRIXB_MRCR_RCB4_Msk                (0x1U << HMATRIXB_MRCR_RCB4_Pos)               /**< (HMATRIXB_MRCR) Remap Command Bit for Master 4 Mask */
#define HMATRIXB_MRCR_RCB4(value)             (HMATRIXB_MRCR_RCB4_Msk & ((value) << HMATRIXB_MRCR_RCB4_Pos))
#define   HMATRIXB_MRCR_RCB4_DIS_Val          (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB4_ENA_Val          (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB4_DIS                (HMATRIXB_MRCR_RCB4_DIS_Val << HMATRIXB_MRCR_RCB4_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB4_ENA                (HMATRIXB_MRCR_RCB4_ENA_Val << HMATRIXB_MRCR_RCB4_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB5_Pos                (5U)                                           /**< (HMATRIXB_MRCR) Remap Command Bit for Master 5 Position */
#define HMATRIXB_MRCR_RCB5_Msk                (0x1U << HMATRIXB_MRCR_RCB5_Pos)               /**< (HMATRIXB_MRCR) Remap Command Bit for Master 5 Mask */
#define HMATRIXB_MRCR_RCB5(value)             (HMATRIXB_MRCR_RCB5_Msk & ((value) << HMATRIXB_MRCR_RCB5_Pos))
#define   HMATRIXB_MRCR_RCB5_DIS_Val          (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB5_ENA_Val          (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB5_DIS                (HMATRIXB_MRCR_RCB5_DIS_Val << HMATRIXB_MRCR_RCB5_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB5_ENA                (HMATRIXB_MRCR_RCB5_ENA_Val << HMATRIXB_MRCR_RCB5_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB6_Pos                (6U)                                           /**< (HMATRIXB_MRCR) Remap Command Bit for Master 6 Position */
#define HMATRIXB_MRCR_RCB6_Msk                (0x1U << HMATRIXB_MRCR_RCB6_Pos)               /**< (HMATRIXB_MRCR) Remap Command Bit for Master 6 Mask */
#define HMATRIXB_MRCR_RCB6(value)             (HMATRIXB_MRCR_RCB6_Msk & ((value) << HMATRIXB_MRCR_RCB6_Pos))
#define   HMATRIXB_MRCR_RCB6_DIS_Val          (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB6_ENA_Val          (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB6_DIS                (HMATRIXB_MRCR_RCB6_DIS_Val << HMATRIXB_MRCR_RCB6_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB6_ENA                (HMATRIXB_MRCR_RCB6_ENA_Val << HMATRIXB_MRCR_RCB6_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB7_Pos                (7U)                                           /**< (HMATRIXB_MRCR) Remap Command Bit for Master 7 Position */
#define HMATRIXB_MRCR_RCB7_Msk                (0x1U << HMATRIXB_MRCR_RCB7_Pos)               /**< (HMATRIXB_MRCR) Remap Command Bit for Master 7 Mask */
#define HMATRIXB_MRCR_RCB7(value)             (HMATRIXB_MRCR_RCB7_Msk & ((value) << HMATRIXB_MRCR_RCB7_Pos))
#define   HMATRIXB_MRCR_RCB7_DIS_Val          (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB7_ENA_Val          (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB7_DIS                (HMATRIXB_MRCR_RCB7_DIS_Val << HMATRIXB_MRCR_RCB7_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB7_ENA                (HMATRIXB_MRCR_RCB7_ENA_Val << HMATRIXB_MRCR_RCB7_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB8_Pos                (8U)                                           /**< (HMATRIXB_MRCR) Remap Command Bit for Master 8 Position */
#define HMATRIXB_MRCR_RCB8_Msk                (0x1U << HMATRIXB_MRCR_RCB8_Pos)               /**< (HMATRIXB_MRCR) Remap Command Bit for Master 8 Mask */
#define HMATRIXB_MRCR_RCB8(value)             (HMATRIXB_MRCR_RCB8_Msk & ((value) << HMATRIXB_MRCR_RCB8_Pos))
#define   HMATRIXB_MRCR_RCB8_DIS_Val          (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB8_ENA_Val          (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB8_DIS                (HMATRIXB_MRCR_RCB8_DIS_Val << HMATRIXB_MRCR_RCB8_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB8_ENA                (HMATRIXB_MRCR_RCB8_ENA_Val << HMATRIXB_MRCR_RCB8_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB9_Pos                (9U)                                           /**< (HMATRIXB_MRCR) Remap Command Bit for Master 9 Position */
#define HMATRIXB_MRCR_RCB9_Msk                (0x1U << HMATRIXB_MRCR_RCB9_Pos)               /**< (HMATRIXB_MRCR) Remap Command Bit for Master 9 Mask */
#define HMATRIXB_MRCR_RCB9(value)             (HMATRIXB_MRCR_RCB9_Msk & ((value) << HMATRIXB_MRCR_RCB9_Pos))
#define   HMATRIXB_MRCR_RCB9_DIS_Val          (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB9_ENA_Val          (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB9_DIS                (HMATRIXB_MRCR_RCB9_DIS_Val << HMATRIXB_MRCR_RCB9_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB9_ENA                (HMATRIXB_MRCR_RCB9_ENA_Val << HMATRIXB_MRCR_RCB9_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB10_Pos               (10U)                                          /**< (HMATRIXB_MRCR) Remap Command Bit for Master 10 Position */
#define HMATRIXB_MRCR_RCB10_Msk               (0x1U << HMATRIXB_MRCR_RCB10_Pos)              /**< (HMATRIXB_MRCR) Remap Command Bit for Master 10 Mask */
#define HMATRIXB_MRCR_RCB10(value)            (HMATRIXB_MRCR_RCB10_Msk & ((value) << HMATRIXB_MRCR_RCB10_Pos))
#define   HMATRIXB_MRCR_RCB10_DIS_Val         (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB10_ENA_Val         (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB10_DIS               (HMATRIXB_MRCR_RCB10_DIS_Val << HMATRIXB_MRCR_RCB10_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB10_ENA               (HMATRIXB_MRCR_RCB10_ENA_Val << HMATRIXB_MRCR_RCB10_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB11_Pos               (11U)                                          /**< (HMATRIXB_MRCR) Remap Command Bit for Master 11 Position */
#define HMATRIXB_MRCR_RCB11_Msk               (0x1U << HMATRIXB_MRCR_RCB11_Pos)              /**< (HMATRIXB_MRCR) Remap Command Bit for Master 11 Mask */
#define HMATRIXB_MRCR_RCB11(value)            (HMATRIXB_MRCR_RCB11_Msk & ((value) << HMATRIXB_MRCR_RCB11_Pos))
#define   HMATRIXB_MRCR_RCB11_DIS_Val         (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB11_ENA_Val         (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB11_DIS               (HMATRIXB_MRCR_RCB11_DIS_Val << HMATRIXB_MRCR_RCB11_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB11_ENA               (HMATRIXB_MRCR_RCB11_ENA_Val << HMATRIXB_MRCR_RCB11_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB12_Pos               (12U)                                          /**< (HMATRIXB_MRCR) Remap Command Bit for Master 12 Position */
#define HMATRIXB_MRCR_RCB12_Msk               (0x1U << HMATRIXB_MRCR_RCB12_Pos)              /**< (HMATRIXB_MRCR) Remap Command Bit for Master 12 Mask */
#define HMATRIXB_MRCR_RCB12(value)            (HMATRIXB_MRCR_RCB12_Msk & ((value) << HMATRIXB_MRCR_RCB12_Pos))
#define   HMATRIXB_MRCR_RCB12_DIS_Val         (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB12_ENA_Val         (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB12_DIS               (HMATRIXB_MRCR_RCB12_DIS_Val << HMATRIXB_MRCR_RCB12_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB12_ENA               (HMATRIXB_MRCR_RCB12_ENA_Val << HMATRIXB_MRCR_RCB12_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB13_Pos               (13U)                                          /**< (HMATRIXB_MRCR) Remap Command Bit for Master 13 Position */
#define HMATRIXB_MRCR_RCB13_Msk               (0x1U << HMATRIXB_MRCR_RCB13_Pos)              /**< (HMATRIXB_MRCR) Remap Command Bit for Master 13 Mask */
#define HMATRIXB_MRCR_RCB13(value)            (HMATRIXB_MRCR_RCB13_Msk & ((value) << HMATRIXB_MRCR_RCB13_Pos))
#define   HMATRIXB_MRCR_RCB13_DIS_Val         (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB13_ENA_Val         (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB13_DIS               (HMATRIXB_MRCR_RCB13_DIS_Val << HMATRIXB_MRCR_RCB13_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB13_ENA               (HMATRIXB_MRCR_RCB13_ENA_Val << HMATRIXB_MRCR_RCB13_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB14_Pos               (14U)                                          /**< (HMATRIXB_MRCR) Remap Command Bit for Master 14 Position */
#define HMATRIXB_MRCR_RCB14_Msk               (0x1U << HMATRIXB_MRCR_RCB14_Pos)              /**< (HMATRIXB_MRCR) Remap Command Bit for Master 14 Mask */
#define HMATRIXB_MRCR_RCB14(value)            (HMATRIXB_MRCR_RCB14_Msk & ((value) << HMATRIXB_MRCR_RCB14_Pos))
#define   HMATRIXB_MRCR_RCB14_DIS_Val         (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB14_ENA_Val         (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB14_DIS               (HMATRIXB_MRCR_RCB14_DIS_Val << HMATRIXB_MRCR_RCB14_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB14_ENA               (HMATRIXB_MRCR_RCB14_ENA_Val << HMATRIXB_MRCR_RCB14_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB15_Pos               (15U)                                          /**< (HMATRIXB_MRCR) Remap Command Bit for Master 15 Position */
#define HMATRIXB_MRCR_RCB15_Msk               (0x1U << HMATRIXB_MRCR_RCB15_Pos)              /**< (HMATRIXB_MRCR) Remap Command Bit for Master 15 Mask */
#define HMATRIXB_MRCR_RCB15(value)            (HMATRIXB_MRCR_RCB15_Msk & ((value) << HMATRIXB_MRCR_RCB15_Pos))
#define   HMATRIXB_MRCR_RCB15_DIS_Val         (0U)                                           /**< (HMATRIXB_MRCR) Disable remapped address decoding for master  */
#define   HMATRIXB_MRCR_RCB15_ENA_Val         (1U)                                           /**< (HMATRIXB_MRCR) Enable remapped address decoding for master  */
#define HMATRIXB_MRCR_RCB15_DIS               (HMATRIXB_MRCR_RCB15_DIS_Val << HMATRIXB_MRCR_RCB15_Pos) /**< (HMATRIXB_MRCR) Disable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_RCB15_ENA               (HMATRIXB_MRCR_RCB15_ENA_Val << HMATRIXB_MRCR_RCB15_Pos) /**< (HMATRIXB_MRCR) Enable remapped address decoding for master Position  */
#define HMATRIXB_MRCR_Msk                     (0x0000FFFFUL)                                 /**< (HMATRIXB_MRCR) Register Mask  */

/* -------- HMATRIXB_SFR : (HMATRIXB Offset: 0x110) (R/W 32) Special Function -------- */
#define HMATRIXB_SFR_SFR_Pos                  (0U)                                           /**< (HMATRIXB_SFR) Special Function Register Position */
#define HMATRIXB_SFR_SFR_Msk                  (0xFFFFFFFFU << HMATRIXB_SFR_SFR_Pos)          /**< (HMATRIXB_SFR) Special Function Register Mask */
#define HMATRIXB_SFR_SFR(value)               (HMATRIXB_SFR_SFR_Msk & ((value) << HMATRIXB_SFR_SFR_Pos))
#define HMATRIXB_SFR_Msk                      (0xFFFFFFFFUL)                                 /**< (HMATRIXB_SFR) Register Mask  */

/** \brief HMATRIXB register offsets definitions */
#define HMATRIXB_MCFG_OFFSET           (0x00)         /**< (HMATRIXB_MCFG) Master Configuration Offset */
#define HMATRIXB_SCFG_OFFSET           (0x40)         /**< (HMATRIXB_SCFG) Slave Configuration Offset */
#define PRS_OFFSET                     (0x80)         /**< (PRS)  Offset */
  #define PRS_PRAS_OFFSET                (0x00)         /**< (PRS_PRAS) Priority A for Slave Offset */
  #define PRS_PRBS_OFFSET                (0x04)         /**< (PRS_PRBS) Priority B for Slave Offset */
#define HMATRIXB_MRCR_OFFSET           (0x100)        /**< (HMATRIXB_MRCR) Master Remap Control Offset */
#define HMATRIXB_SFR_OFFSET            (0x110)        /**< (HMATRIXB_SFR) Special Function Offset */

/** \brief PRS register API structure */
typedef struct
{
  __IO  uint32_t                       PRS_PRAS;        /**< Offset: 0x00 (R/W  32) Priority A for Slave */
  __IO  uint32_t                       PRS_PRBS;        /**< Offset: 0x04 (R/W  32) Priority B for Slave */
} prs_registers_t;
#define PRS_NUMBER (4U)

/** \brief HMATRIXB register API structure */
typedef struct
{
  __IO  uint32_t                       HMATRIXB_MCFG[16]; /**< Offset: 0x00 (R/W  32) Master Configuration */
  __IO  uint32_t                       HMATRIXB_SCFG[16]; /**< Offset: 0x40 (R/W  32) Slave Configuration */
        prs_registers_t                PRS[PRS_NUMBER]; /**< Offset: 0x80  */
  __I   uint8_t                        Reserved1[0x60];
  __IO  uint32_t                       HMATRIXB_MRCR;   /**< Offset: 0x100 (R/W  32) Master Remap Control */
  __I   uint8_t                        Reserved2[0x0C];
  __IO  uint32_t                       HMATRIXB_SFR[16]; /**< Offset: 0x110 (R/W  32) Special Function */
} hmatrixb_registers_t;
/** @}  end of HSB Matrix */

#endif /* SAMC_SAMC21_HMATRIXB_MODULE_H */

