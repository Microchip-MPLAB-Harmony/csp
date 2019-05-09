/**
 * \brief Header file for SAMG/SAMG55 MATRIX
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
#ifndef SAMG_SAMG55_MATRIX_MODULE_H
#define SAMG_SAMG55_MATRIX_MODULE_H

/** \addtogroup SAMG_SAMG55 AHB Bus Matrix
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_MATRIX                                */
/* ========================================================================== */

/* -------- MATRIX_MCFG : (MATRIX Offset: 0x00) (R/W 32) Master Configuration Register 0 -------- */
#define MATRIX_MCFG_ULBT_Pos                  (0U)                                           /**< (MATRIX_MCFG) Undefined Length Burst Type Position */
#define MATRIX_MCFG_ULBT_Msk                  (0x7U << MATRIX_MCFG_ULBT_Pos)                 /**< (MATRIX_MCFG) Undefined Length Burst Type Mask */
#define MATRIX_MCFG_ULBT(value)               (MATRIX_MCFG_ULBT_Msk & ((value) << MATRIX_MCFG_ULBT_Pos))
#define   MATRIX_MCFG_ULBT_UNLIMITED_Val      (0U)                                           /**< (MATRIX_MCFG) No predicted end of burst is generated and therefore INCR bursts coming from this master cannot be broken.  */
#define   MATRIX_MCFG_ULBT_SINGLE_Val         (1U)                                           /**< (MATRIX_MCFG) The undefined length burst is treated as a succession of single access allowing rearbitration at each beat of the INCR burst.  */
#define   MATRIX_MCFG_ULBT_4_BEAT_Val         (2U)                                           /**< (MATRIX_MCFG) The undefined length burst is split into a 4-beat bursts allowing rearbitration at each 4-beat burst end.  */
#define   MATRIX_MCFG_ULBT_8_BEAT_Val         (3U)                                           /**< (MATRIX_MCFG) The undefined length burst is split into 8-beat bursts allowing rearbitration at each 8-beat burst end.  */
#define   MATRIX_MCFG_ULBT_16_BEAT_Val        (4U)                                           /**< (MATRIX_MCFG) The undefined length burst is split into 16-beat bursts allowing rearbitration at each 16-beat burst end.  */
#define MATRIX_MCFG_ULBT_UNLIMITED            (MATRIX_MCFG_ULBT_UNLIMITED_Val << MATRIX_MCFG_ULBT_Pos) /**< (MATRIX_MCFG) No predicted end of burst is generated and therefore INCR bursts coming from this master cannot be broken. Position  */
#define MATRIX_MCFG_ULBT_SINGLE               (MATRIX_MCFG_ULBT_SINGLE_Val << MATRIX_MCFG_ULBT_Pos) /**< (MATRIX_MCFG) The undefined length burst is treated as a succession of single access allowing rearbitration at each beat of the INCR burst. Position  */
#define MATRIX_MCFG_ULBT_4_BEAT               (MATRIX_MCFG_ULBT_4_BEAT_Val << MATRIX_MCFG_ULBT_Pos) /**< (MATRIX_MCFG) The undefined length burst is split into a 4-beat bursts allowing rearbitration at each 4-beat burst end. Position  */
#define MATRIX_MCFG_ULBT_8_BEAT               (MATRIX_MCFG_ULBT_8_BEAT_Val << MATRIX_MCFG_ULBT_Pos) /**< (MATRIX_MCFG) The undefined length burst is split into 8-beat bursts allowing rearbitration at each 8-beat burst end. Position  */
#define MATRIX_MCFG_ULBT_16_BEAT              (MATRIX_MCFG_ULBT_16_BEAT_Val << MATRIX_MCFG_ULBT_Pos) /**< (MATRIX_MCFG) The undefined length burst is split into 16-beat bursts allowing rearbitration at each 16-beat burst end. Position  */
#define MATRIX_MCFG_Msk                       (0x00000007UL)                                 /**< (MATRIX_MCFG) Register Mask  */

/* -------- MATRIX_SCFG : (MATRIX Offset: 0x40) (R/W 32) Slave Configuration Register 0 -------- */
#define MATRIX_SCFG_SLOT_CYCLE_Pos            (0U)                                           /**< (MATRIX_SCFG) Maximum Number of Allowed Cycles for a Burst Position */
#define MATRIX_SCFG_SLOT_CYCLE_Msk            (0xFFU << MATRIX_SCFG_SLOT_CYCLE_Pos)          /**< (MATRIX_SCFG) Maximum Number of Allowed Cycles for a Burst Mask */
#define MATRIX_SCFG_SLOT_CYCLE(value)         (MATRIX_SCFG_SLOT_CYCLE_Msk & ((value) << MATRIX_SCFG_SLOT_CYCLE_Pos))
#define MATRIX_SCFG_DEFMSTR_TYPE_Pos          (16U)                                          /**< (MATRIX_SCFG) Default Master Type Position */
#define MATRIX_SCFG_DEFMSTR_TYPE_Msk          (0x3U << MATRIX_SCFG_DEFMSTR_TYPE_Pos)         /**< (MATRIX_SCFG) Default Master Type Mask */
#define MATRIX_SCFG_DEFMSTR_TYPE(value)       (MATRIX_SCFG_DEFMSTR_TYPE_Msk & ((value) << MATRIX_SCFG_DEFMSTR_TYPE_Pos))
#define   MATRIX_SCFG_DEFMSTR_TYPE_NO_DEFAULT_Val (0U)                                           /**< (MATRIX_SCFG) At the end of current slave access, if no other master request is pending, the slave is disconnected from all masters.This results in having a one cycle latency for the first access of a burst transfer or for a single access.  */
#define   MATRIX_SCFG_DEFMSTR_TYPE_LAST_Val   (1U)                                           /**< (MATRIX_SCFG) At the end of current slave access, if no other master request is pending, the slave stays connected to the last master having accessed it.This results in not having the one cycle latency when the last master tries to access the slave again.  */
#define   MATRIX_SCFG_DEFMSTR_TYPE_FIXED_Val  (2U)                                           /**< (MATRIX_SCFG) At the end of the current slave access, if no other master request is pending, the slave connects to the fixed master the number that has been written in the FIXED_DEFMSTR field.This results in not having the one cycle latency when the fixed master tries to access the slave again.  */
#define MATRIX_SCFG_DEFMSTR_TYPE_NO_DEFAULT   (MATRIX_SCFG_DEFMSTR_TYPE_NO_DEFAULT_Val << MATRIX_SCFG_DEFMSTR_TYPE_Pos) /**< (MATRIX_SCFG) At the end of current slave access, if no other master request is pending, the slave is disconnected from all masters.This results in having a one cycle latency for the first access of a burst transfer or for a single access. Position  */
#define MATRIX_SCFG_DEFMSTR_TYPE_LAST         (MATRIX_SCFG_DEFMSTR_TYPE_LAST_Val << MATRIX_SCFG_DEFMSTR_TYPE_Pos) /**< (MATRIX_SCFG) At the end of current slave access, if no other master request is pending, the slave stays connected to the last master having accessed it.This results in not having the one cycle latency when the last master tries to access the slave again. Position  */
#define MATRIX_SCFG_DEFMSTR_TYPE_FIXED        (MATRIX_SCFG_DEFMSTR_TYPE_FIXED_Val << MATRIX_SCFG_DEFMSTR_TYPE_Pos) /**< (MATRIX_SCFG) At the end of the current slave access, if no other master request is pending, the slave connects to the fixed master the number that has been written in the FIXED_DEFMSTR field.This results in not having the one cycle latency when the fixed master tries to access the slave again. Position  */
#define MATRIX_SCFG_FIXED_DEFMSTR_Pos         (18U)                                          /**< (MATRIX_SCFG) Fixed Default Master Position */
#define MATRIX_SCFG_FIXED_DEFMSTR_Msk         (0x7U << MATRIX_SCFG_FIXED_DEFMSTR_Pos)        /**< (MATRIX_SCFG) Fixed Default Master Mask */
#define MATRIX_SCFG_FIXED_DEFMSTR(value)      (MATRIX_SCFG_FIXED_DEFMSTR_Msk & ((value) << MATRIX_SCFG_FIXED_DEFMSTR_Pos))
#define MATRIX_SCFG_Msk                       (0x001F00FFUL)                                 /**< (MATRIX_SCFG) Register Mask  */

/* -------- MATRIX_PRAS0 : (MATRIX Offset: 0x80) (R/W 32) Priority Register A for Slave 0 -------- */
#define MATRIX_PRAS0_M0PR_Pos                 (0U)                                           /**< (MATRIX_PRAS0) Master 0 Priority Position */
#define MATRIX_PRAS0_M0PR_Msk                 (0x3U << MATRIX_PRAS0_M0PR_Pos)                /**< (MATRIX_PRAS0) Master 0 Priority Mask */
#define MATRIX_PRAS0_M0PR(value)              (MATRIX_PRAS0_M0PR_Msk & ((value) << MATRIX_PRAS0_M0PR_Pos))
#define MATRIX_PRAS0_M1PR_Pos                 (4U)                                           /**< (MATRIX_PRAS0) Master 1 Priority Position */
#define MATRIX_PRAS0_M1PR_Msk                 (0x3U << MATRIX_PRAS0_M1PR_Pos)                /**< (MATRIX_PRAS0) Master 1 Priority Mask */
#define MATRIX_PRAS0_M1PR(value)              (MATRIX_PRAS0_M1PR_Msk & ((value) << MATRIX_PRAS0_M1PR_Pos))
#define MATRIX_PRAS0_M2PR_Pos                 (8U)                                           /**< (MATRIX_PRAS0) Master 2 Priority Position */
#define MATRIX_PRAS0_M2PR_Msk                 (0x3U << MATRIX_PRAS0_M2PR_Pos)                /**< (MATRIX_PRAS0) Master 2 Priority Mask */
#define MATRIX_PRAS0_M2PR(value)              (MATRIX_PRAS0_M2PR_Msk & ((value) << MATRIX_PRAS0_M2PR_Pos))
#define MATRIX_PRAS0_M3PR_Pos                 (12U)                                          /**< (MATRIX_PRAS0) Master 3 Priority Position */
#define MATRIX_PRAS0_M3PR_Msk                 (0x3U << MATRIX_PRAS0_M3PR_Pos)                /**< (MATRIX_PRAS0) Master 3 Priority Mask */
#define MATRIX_PRAS0_M3PR(value)              (MATRIX_PRAS0_M3PR_Msk & ((value) << MATRIX_PRAS0_M3PR_Pos))
#define MATRIX_PRAS0_Msk                      (0x00003333UL)                                 /**< (MATRIX_PRAS0) Register Mask  */

/* -------- MATRIX_PRAS1 : (MATRIX Offset: 0x88) (R/W 32) Priority Register A for Slave 1 -------- */
#define MATRIX_PRAS1_M0PR_Pos                 (0U)                                           /**< (MATRIX_PRAS1) Master 0 Priority Position */
#define MATRIX_PRAS1_M0PR_Msk                 (0x3U << MATRIX_PRAS1_M0PR_Pos)                /**< (MATRIX_PRAS1) Master 0 Priority Mask */
#define MATRIX_PRAS1_M0PR(value)              (MATRIX_PRAS1_M0PR_Msk & ((value) << MATRIX_PRAS1_M0PR_Pos))
#define MATRIX_PRAS1_M1PR_Pos                 (4U)                                           /**< (MATRIX_PRAS1) Master 1 Priority Position */
#define MATRIX_PRAS1_M1PR_Msk                 (0x3U << MATRIX_PRAS1_M1PR_Pos)                /**< (MATRIX_PRAS1) Master 1 Priority Mask */
#define MATRIX_PRAS1_M1PR(value)              (MATRIX_PRAS1_M1PR_Msk & ((value) << MATRIX_PRAS1_M1PR_Pos))
#define MATRIX_PRAS1_M2PR_Pos                 (8U)                                           /**< (MATRIX_PRAS1) Master 2 Priority Position */
#define MATRIX_PRAS1_M2PR_Msk                 (0x3U << MATRIX_PRAS1_M2PR_Pos)                /**< (MATRIX_PRAS1) Master 2 Priority Mask */
#define MATRIX_PRAS1_M2PR(value)              (MATRIX_PRAS1_M2PR_Msk & ((value) << MATRIX_PRAS1_M2PR_Pos))
#define MATRIX_PRAS1_M3PR_Pos                 (12U)                                          /**< (MATRIX_PRAS1) Master 3 Priority Position */
#define MATRIX_PRAS1_M3PR_Msk                 (0x3U << MATRIX_PRAS1_M3PR_Pos)                /**< (MATRIX_PRAS1) Master 3 Priority Mask */
#define MATRIX_PRAS1_M3PR(value)              (MATRIX_PRAS1_M3PR_Msk & ((value) << MATRIX_PRAS1_M3PR_Pos))
#define MATRIX_PRAS1_Msk                      (0x00003333UL)                                 /**< (MATRIX_PRAS1) Register Mask  */

/* -------- MATRIX_PRAS2 : (MATRIX Offset: 0x90) (R/W 32) Priority Register A for Slave 2 -------- */
#define MATRIX_PRAS2_M0PR_Pos                 (0U)                                           /**< (MATRIX_PRAS2) Master 0 Priority Position */
#define MATRIX_PRAS2_M0PR_Msk                 (0x3U << MATRIX_PRAS2_M0PR_Pos)                /**< (MATRIX_PRAS2) Master 0 Priority Mask */
#define MATRIX_PRAS2_M0PR(value)              (MATRIX_PRAS2_M0PR_Msk & ((value) << MATRIX_PRAS2_M0PR_Pos))
#define MATRIX_PRAS2_M1PR_Pos                 (4U)                                           /**< (MATRIX_PRAS2) Master 1 Priority Position */
#define MATRIX_PRAS2_M1PR_Msk                 (0x3U << MATRIX_PRAS2_M1PR_Pos)                /**< (MATRIX_PRAS2) Master 1 Priority Mask */
#define MATRIX_PRAS2_M1PR(value)              (MATRIX_PRAS2_M1PR_Msk & ((value) << MATRIX_PRAS2_M1PR_Pos))
#define MATRIX_PRAS2_M2PR_Pos                 (8U)                                           /**< (MATRIX_PRAS2) Master 2 Priority Position */
#define MATRIX_PRAS2_M2PR_Msk                 (0x3U << MATRIX_PRAS2_M2PR_Pos)                /**< (MATRIX_PRAS2) Master 2 Priority Mask */
#define MATRIX_PRAS2_M2PR(value)              (MATRIX_PRAS2_M2PR_Msk & ((value) << MATRIX_PRAS2_M2PR_Pos))
#define MATRIX_PRAS2_M3PR_Pos                 (12U)                                          /**< (MATRIX_PRAS2) Master 3 Priority Position */
#define MATRIX_PRAS2_M3PR_Msk                 (0x3U << MATRIX_PRAS2_M3PR_Pos)                /**< (MATRIX_PRAS2) Master 3 Priority Mask */
#define MATRIX_PRAS2_M3PR(value)              (MATRIX_PRAS2_M3PR_Msk & ((value) << MATRIX_PRAS2_M3PR_Pos))
#define MATRIX_PRAS2_Msk                      (0x00003333UL)                                 /**< (MATRIX_PRAS2) Register Mask  */

/* -------- MATRIX_PRAS3 : (MATRIX Offset: 0x98) (R/W 32) Priority Register A for Slave 3 -------- */
#define MATRIX_PRAS3_M0PR_Pos                 (0U)                                           /**< (MATRIX_PRAS3) Master 0 Priority Position */
#define MATRIX_PRAS3_M0PR_Msk                 (0x3U << MATRIX_PRAS3_M0PR_Pos)                /**< (MATRIX_PRAS3) Master 0 Priority Mask */
#define MATRIX_PRAS3_M0PR(value)              (MATRIX_PRAS3_M0PR_Msk & ((value) << MATRIX_PRAS3_M0PR_Pos))
#define MATRIX_PRAS3_M1PR_Pos                 (4U)                                           /**< (MATRIX_PRAS3) Master 1 Priority Position */
#define MATRIX_PRAS3_M1PR_Msk                 (0x3U << MATRIX_PRAS3_M1PR_Pos)                /**< (MATRIX_PRAS3) Master 1 Priority Mask */
#define MATRIX_PRAS3_M1PR(value)              (MATRIX_PRAS3_M1PR_Msk & ((value) << MATRIX_PRAS3_M1PR_Pos))
#define MATRIX_PRAS3_M2PR_Pos                 (8U)                                           /**< (MATRIX_PRAS3) Master 2 Priority Position */
#define MATRIX_PRAS3_M2PR_Msk                 (0x3U << MATRIX_PRAS3_M2PR_Pos)                /**< (MATRIX_PRAS3) Master 2 Priority Mask */
#define MATRIX_PRAS3_M2PR(value)              (MATRIX_PRAS3_M2PR_Msk & ((value) << MATRIX_PRAS3_M2PR_Pos))
#define MATRIX_PRAS3_M3PR_Pos                 (12U)                                          /**< (MATRIX_PRAS3) Master 3 Priority Position */
#define MATRIX_PRAS3_M3PR_Msk                 (0x3U << MATRIX_PRAS3_M3PR_Pos)                /**< (MATRIX_PRAS3) Master 3 Priority Mask */
#define MATRIX_PRAS3_M3PR(value)              (MATRIX_PRAS3_M3PR_Msk & ((value) << MATRIX_PRAS3_M3PR_Pos))
#define MATRIX_PRAS3_Msk                      (0x00003333UL)                                 /**< (MATRIX_PRAS3) Register Mask  */

/* -------- CCFG_SYSIO : (MATRIX Offset: 0x114) (R/W 32) System I/O Configuration Register -------- */
#define CCFG_SYSIO_SYSIO4_Pos                 (4U)                                           /**< (CCFG_SYSIO) PB4 or TDI Assignment Position */
#define CCFG_SYSIO_SYSIO4_Msk                 (0x1U << CCFG_SYSIO_SYSIO4_Pos)                /**< (CCFG_SYSIO) PB4 or TDI Assignment Mask */
#define CCFG_SYSIO_SYSIO4(value)              (CCFG_SYSIO_SYSIO4_Msk & ((value) << CCFG_SYSIO_SYSIO4_Pos))
#define CCFG_SYSIO_SYSIO5_Pos                 (5U)                                           /**< (CCFG_SYSIO) PB5 or TDO/TRACESWO Assignment Position */
#define CCFG_SYSIO_SYSIO5_Msk                 (0x1U << CCFG_SYSIO_SYSIO5_Pos)                /**< (CCFG_SYSIO) PB5 or TDO/TRACESWO Assignment Mask */
#define CCFG_SYSIO_SYSIO5(value)              (CCFG_SYSIO_SYSIO5_Msk & ((value) << CCFG_SYSIO_SYSIO5_Pos))
#define CCFG_SYSIO_SYSIO6_Pos                 (6U)                                           /**< (CCFG_SYSIO) PB6 or TMS/SWDIO Assignment Position */
#define CCFG_SYSIO_SYSIO6_Msk                 (0x1U << CCFG_SYSIO_SYSIO6_Pos)                /**< (CCFG_SYSIO) PB6 or TMS/SWDIO Assignment Mask */
#define CCFG_SYSIO_SYSIO6(value)              (CCFG_SYSIO_SYSIO6_Msk & ((value) << CCFG_SYSIO_SYSIO6_Pos))
#define CCFG_SYSIO_SYSIO7_Pos                 (7U)                                           /**< (CCFG_SYSIO) PB7 or TCK/SWCLK Assignment Position */
#define CCFG_SYSIO_SYSIO7_Msk                 (0x1U << CCFG_SYSIO_SYSIO7_Pos)                /**< (CCFG_SYSIO) PB7 or TCK/SWCLK Assignment Mask */
#define CCFG_SYSIO_SYSIO7(value)              (CCFG_SYSIO_SYSIO7_Msk & ((value) << CCFG_SYSIO_SYSIO7_Pos))
#define CCFG_SYSIO_SYSIO10_Pos                (10U)                                          /**< (CCFG_SYSIO) PA21 or DM Assignment Position */
#define CCFG_SYSIO_SYSIO10_Msk                (0x1U << CCFG_SYSIO_SYSIO10_Pos)               /**< (CCFG_SYSIO) PA21 or DM Assignment Mask */
#define CCFG_SYSIO_SYSIO10(value)             (CCFG_SYSIO_SYSIO10_Msk & ((value) << CCFG_SYSIO_SYSIO10_Pos))
#define CCFG_SYSIO_SYSIO11_Pos                (11U)                                          /**< (CCFG_SYSIO) PA22 or DP Assignment Position */
#define CCFG_SYSIO_SYSIO11_Msk                (0x1U << CCFG_SYSIO_SYSIO11_Pos)               /**< (CCFG_SYSIO) PA22 or DP Assignment Mask */
#define CCFG_SYSIO_SYSIO11(value)             (CCFG_SYSIO_SYSIO11_Msk & ((value) << CCFG_SYSIO_SYSIO11_Pos))
#define CCFG_SYSIO_SYSIO12_Pos                (12U)                                          /**< (CCFG_SYSIO) PB12 or ERASE Assignment Position */
#define CCFG_SYSIO_SYSIO12_Msk                (0x1U << CCFG_SYSIO_SYSIO12_Pos)               /**< (CCFG_SYSIO) PB12 or ERASE Assignment Mask */
#define CCFG_SYSIO_SYSIO12(value)             (CCFG_SYSIO_SYSIO12_Msk & ((value) << CCFG_SYSIO_SYSIO12_Pos))
#define CCFG_SYSIO_Msk                        (0x00001CF0UL)                                 /**< (CCFG_SYSIO) Register Mask  */

/* -------- CCFG_DYNCKG : (MATRIX Offset: 0x118) (R/W 32) Dynamic Clock Gating Register -------- */
#define CCFG_DYNCKG_MATCKG_Pos                (0U)                                           /**< (CCFG_DYNCKG) MATRIX Dynamic Clock Gating Position */
#define CCFG_DYNCKG_MATCKG_Msk                (0x1U << CCFG_DYNCKG_MATCKG_Pos)               /**< (CCFG_DYNCKG) MATRIX Dynamic Clock Gating Mask */
#define CCFG_DYNCKG_MATCKG(value)             (CCFG_DYNCKG_MATCKG_Msk & ((value) << CCFG_DYNCKG_MATCKG_Pos))
#define CCFG_DYNCKG_BRIDCKG_Pos               (1U)                                           /**< (CCFG_DYNCKG) Bridge Dynamic Clock Gating Enable Position */
#define CCFG_DYNCKG_BRIDCKG_Msk               (0x1U << CCFG_DYNCKG_BRIDCKG_Pos)              /**< (CCFG_DYNCKG) Bridge Dynamic Clock Gating Enable Mask */
#define CCFG_DYNCKG_BRIDCKG(value)            (CCFG_DYNCKG_BRIDCKG_Msk & ((value) << CCFG_DYNCKG_BRIDCKG_Pos))
#define CCFG_DYNCKG_EFCCKG_Pos                (2U)                                           /**< (CCFG_DYNCKG) EFC Dynamic Clock Gating Enable Position */
#define CCFG_DYNCKG_EFCCKG_Msk                (0x1U << CCFG_DYNCKG_EFCCKG_Pos)               /**< (CCFG_DYNCKG) EFC Dynamic Clock Gating Enable Mask */
#define CCFG_DYNCKG_EFCCKG(value)             (CCFG_DYNCKG_EFCCKG_Msk & ((value) << CCFG_DYNCKG_EFCCKG_Pos))
#define CCFG_DYNCKG_Msk                       (0x00000007UL)                                 /**< (CCFG_DYNCKG) Register Mask  */

/* -------- CCFG_I2SCLKSEL : (MATRIX Offset: 0x11C) (R/W 32) I2S Clock Source Selection Register -------- */
#define CCFG_I2SCLKSEL_CLKSEL0_Pos            (0U)                                           /**< (CCFG_I2SCLKSEL) I2S0 Clock Source Position */
#define CCFG_I2SCLKSEL_CLKSEL0_Msk            (0x1U << CCFG_I2SCLKSEL_CLKSEL0_Pos)           /**< (CCFG_I2SCLKSEL) I2S0 Clock Source Mask */
#define CCFG_I2SCLKSEL_CLKSEL0(value)         (CCFG_I2SCLKSEL_CLKSEL0_Msk & ((value) << CCFG_I2SCLKSEL_CLKSEL0_Pos))
#define CCFG_I2SCLKSEL_CLKSEL1_Pos            (1U)                                           /**< (CCFG_I2SCLKSEL) I2S1 Clock Source Position */
#define CCFG_I2SCLKSEL_CLKSEL1_Msk            (0x1U << CCFG_I2SCLKSEL_CLKSEL1_Pos)           /**< (CCFG_I2SCLKSEL) I2S1 Clock Source Mask */
#define CCFG_I2SCLKSEL_CLKSEL1(value)         (CCFG_I2SCLKSEL_CLKSEL1_Msk & ((value) << CCFG_I2SCLKSEL_CLKSEL1_Pos))
#define CCFG_I2SCLKSEL_Msk                    (0x00000003UL)                                 /**< (CCFG_I2SCLKSEL) Register Mask  */

/* -------- CCFG_USBMR : (MATRIX Offset: 0x120) (R/W 32) USB Management Register -------- */
#define CCFG_USBMR_USBMODE_Pos                (0U)                                           /**< (CCFG_USBMR) USB Mode Selection Position */
#define CCFG_USBMR_USBMODE_Msk                (0x1U << CCFG_USBMR_USBMODE_Pos)               /**< (CCFG_USBMR) USB Mode Selection Mask */
#define CCFG_USBMR_USBMODE(value)             (CCFG_USBMR_USBMODE_Msk & ((value) << CCFG_USBMR_USBMODE_Pos))
#define CCFG_USBMR_USBHTSSC_Pos               (1U)                                           /**< (CCFG_USBMR) USB Transceiver Suspend Software Control Position */
#define CCFG_USBMR_USBHTSSC_Msk               (0x1U << CCFG_USBMR_USBHTSSC_Pos)              /**< (CCFG_USBMR) USB Transceiver Suspend Software Control Mask */
#define CCFG_USBMR_USBHTSSC(value)            (CCFG_USBMR_USBHTSSC_Msk & ((value) << CCFG_USBMR_USBHTSSC_Pos))
#define CCFG_USBMR_USBHTSC_Pos                (2U)                                           /**< (CCFG_USBMR) USB Host Transceiver Suspend Control Position */
#define CCFG_USBMR_USBHTSC_Msk                (0x1U << CCFG_USBMR_USBHTSC_Pos)               /**< (CCFG_USBMR) USB Host Transceiver Suspend Control Mask */
#define CCFG_USBMR_USBHTSC(value)             (CCFG_USBMR_USBHTSC_Msk & ((value) << CCFG_USBMR_USBHTSC_Pos))
#define CCFG_USBMR_Msk                        (0x00000007UL)                                 /**< (CCFG_USBMR) Register Mask  */

/* -------- MATRIX_WPMR : (MATRIX Offset: 0x1E4) (R/W 32) Write Protection Mode Register -------- */
#define MATRIX_WPMR_WPEN_Pos                  (0U)                                           /**< (MATRIX_WPMR) Write Protection Enable Position */
#define MATRIX_WPMR_WPEN_Msk                  (0x1U << MATRIX_WPMR_WPEN_Pos)                 /**< (MATRIX_WPMR) Write Protection Enable Mask */
#define MATRIX_WPMR_WPEN(value)               (MATRIX_WPMR_WPEN_Msk & ((value) << MATRIX_WPMR_WPEN_Pos))
#define MATRIX_WPMR_WPKEY_Pos                 (8U)                                           /**< (MATRIX_WPMR) Write Protection Key Position */
#define MATRIX_WPMR_WPKEY_Msk                 (0xFFFFFFU << MATRIX_WPMR_WPKEY_Pos)           /**< (MATRIX_WPMR) Write Protection Key Mask */
#define MATRIX_WPMR_WPKEY(value)              (MATRIX_WPMR_WPKEY_Msk & ((value) << MATRIX_WPMR_WPKEY_Pos))
#define   MATRIX_WPMR_WPKEY_PASSWD_Val        (5062996U)                                     /**< (MATRIX_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit. Always reads as 0.  */
#define MATRIX_WPMR_WPKEY_PASSWD              (MATRIX_WPMR_WPKEY_PASSWD_Val << MATRIX_WPMR_WPKEY_Pos) /**< (MATRIX_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit. Always reads as 0. Position  */
#define MATRIX_WPMR_Msk                       (0xFFFFFF01UL)                                 /**< (MATRIX_WPMR) Register Mask  */

/* -------- MATRIX_WPSR : (MATRIX Offset: 0x1E8) (R/  32) Write Protection Status Register -------- */
#define MATRIX_WPSR_WPVS_Pos                  (0U)                                           /**< (MATRIX_WPSR) Write Protection Violation Status Position */
#define MATRIX_WPSR_WPVS_Msk                  (0x1U << MATRIX_WPSR_WPVS_Pos)                 /**< (MATRIX_WPSR) Write Protection Violation Status Mask */
#define MATRIX_WPSR_WPVS(value)               (MATRIX_WPSR_WPVS_Msk & ((value) << MATRIX_WPSR_WPVS_Pos))
#define MATRIX_WPSR_WPVSRC_Pos                (8U)                                           /**< (MATRIX_WPSR) Write Protection Violation Source Position */
#define MATRIX_WPSR_WPVSRC_Msk                (0xFFFFU << MATRIX_WPSR_WPVSRC_Pos)            /**< (MATRIX_WPSR) Write Protection Violation Source Mask */
#define MATRIX_WPSR_WPVSRC(value)             (MATRIX_WPSR_WPVSRC_Msk & ((value) << MATRIX_WPSR_WPVSRC_Pos))
#define MATRIX_WPSR_Msk                       (0x00FFFF01UL)                                 /**< (MATRIX_WPSR) Register Mask  */

/** \brief MATRIX register offsets definitions */
#define MATRIX_MCFG_OFFSET             (0x00)         /**< (MATRIX_MCFG) Master Configuration Register 0 Offset */
#define MATRIX_SCFG_OFFSET             (0x40)         /**< (MATRIX_SCFG) Slave Configuration Register 0 Offset */
#define MATRIX_PRAS0_OFFSET            (0x80)         /**< (MATRIX_PRAS0) Priority Register A for Slave 0 Offset */
#define MATRIX_PRAS1_OFFSET            (0x88)         /**< (MATRIX_PRAS1) Priority Register A for Slave 1 Offset */
#define MATRIX_PRAS2_OFFSET            (0x90)         /**< (MATRIX_PRAS2) Priority Register A for Slave 2 Offset */
#define MATRIX_PRAS3_OFFSET            (0x98)         /**< (MATRIX_PRAS3) Priority Register A for Slave 3 Offset */
#define CCFG_SYSIO_OFFSET              (0x114)        /**< (CCFG_SYSIO) System I/O Configuration Register Offset */
#define CCFG_DYNCKG_OFFSET             (0x118)        /**< (CCFG_DYNCKG) Dynamic Clock Gating Register Offset */
#define CCFG_I2SCLKSEL_OFFSET          (0x11C)        /**< (CCFG_I2SCLKSEL) I2S Clock Source Selection Register Offset */
#define CCFG_USBMR_OFFSET              (0x120)        /**< (CCFG_USBMR) USB Management Register Offset */
#define MATRIX_WPMR_OFFSET             (0x1E4)        /**< (MATRIX_WPMR) Write Protection Mode Register Offset */
#define MATRIX_WPSR_OFFSET             (0x1E8)        /**< (MATRIX_WPSR) Write Protection Status Register Offset */

/** \brief MATRIX register API structure */
typedef struct
{
  __IO  uint32_t                       MATRIX_MCFG[3];  /**< Offset: 0x00 (R/W  32) Master Configuration Register 0 */
  __I   uint8_t                        Reserved1[0x34];
  __IO  uint32_t                       MATRIX_SCFG[4];  /**< Offset: 0x40 (R/W  32) Slave Configuration Register 0 */
  __I   uint8_t                        Reserved2[0x30];
  __IO  uint32_t                       MATRIX_PRAS0;    /**< Offset: 0x80 (R/W  32) Priority Register A for Slave 0 */
  __I   uint8_t                        Reserved3[0x04];
  __IO  uint32_t                       MATRIX_PRAS1;    /**< Offset: 0x88 (R/W  32) Priority Register A for Slave 1 */
  __I   uint8_t                        Reserved4[0x04];
  __IO  uint32_t                       MATRIX_PRAS2;    /**< Offset: 0x90 (R/W  32) Priority Register A for Slave 2 */
  __I   uint8_t                        Reserved5[0x04];
  __IO  uint32_t                       MATRIX_PRAS3;    /**< Offset: 0x98 (R/W  32) Priority Register A for Slave 3 */
  __I   uint8_t                        Reserved6[0x78];
  __IO  uint32_t                       CCFG_SYSIO;      /**< Offset: 0x114 (R/W  32) System I/O Configuration Register */
  __IO  uint32_t                       CCFG_DYNCKG;     /**< Offset: 0x118 (R/W  32) Dynamic Clock Gating Register */
  __IO  uint32_t                       CCFG_I2SCLKSEL;  /**< Offset: 0x11c (R/W  32) I2S Clock Source Selection Register */
  __IO  uint32_t                       CCFG_USBMR;      /**< Offset: 0x120 (R/W  32) USB Management Register */
  __I   uint8_t                        Reserved7[0xC0];
  __IO  uint32_t                       MATRIX_WPMR;     /**< Offset: 0x1e4 (R/W  32) Write Protection Mode Register */
  __I   uint32_t                       MATRIX_WPSR;     /**< Offset: 0x1e8 (R/   32) Write Protection Status Register */
} matrix_registers_t;
/** @}  end of AHB Bus Matrix */

#endif /* SAMG_SAMG55_MATRIX_MODULE_H */

