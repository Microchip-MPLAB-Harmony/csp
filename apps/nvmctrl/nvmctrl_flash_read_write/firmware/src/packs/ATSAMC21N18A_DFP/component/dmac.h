/**
 * \brief Header file for SAMC/SAMC21 DMAC
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
#ifndef SAMC_SAMC21_DMAC_MODULE_H
#define SAMC_SAMC21_DMAC_MODULE_H

/** \addtogroup SAMC_SAMC21 Direct Memory Access Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_DMAC                                  */
/* ========================================================================== */

/* -------- DMAC_CTRL : (DMAC Offset: 0x00) (R/W 16) Control -------- */
#define DMAC_CTRL_SWRST_Pos                   (0U)                                           /**< (DMAC_CTRL) Software Reset Position */
#define DMAC_CTRL_SWRST_Msk                   (0x1U << DMAC_CTRL_SWRST_Pos)                  /**< (DMAC_CTRL) Software Reset Mask */
#define DMAC_CTRL_SWRST(value)                (DMAC_CTRL_SWRST_Msk & ((value) << DMAC_CTRL_SWRST_Pos))
#define DMAC_CTRL_DMAENABLE_Pos               (1U)                                           /**< (DMAC_CTRL) DMA Enable Position */
#define DMAC_CTRL_DMAENABLE_Msk               (0x1U << DMAC_CTRL_DMAENABLE_Pos)              /**< (DMAC_CTRL) DMA Enable Mask */
#define DMAC_CTRL_DMAENABLE(value)            (DMAC_CTRL_DMAENABLE_Msk & ((value) << DMAC_CTRL_DMAENABLE_Pos))
#define DMAC_CTRL_CRCENABLE_Pos               (2U)                                           /**< (DMAC_CTRL) CRC Enable Position */
#define DMAC_CTRL_CRCENABLE_Msk               (0x1U << DMAC_CTRL_CRCENABLE_Pos)              /**< (DMAC_CTRL) CRC Enable Mask */
#define DMAC_CTRL_CRCENABLE(value)            (DMAC_CTRL_CRCENABLE_Msk & ((value) << DMAC_CTRL_CRCENABLE_Pos))
#define DMAC_CTRL_LVLEN0_Pos                  (8U)                                           /**< (DMAC_CTRL) Priority Level 0 Enable Position */
#define DMAC_CTRL_LVLEN0_Msk                  (0x1U << DMAC_CTRL_LVLEN0_Pos)                 /**< (DMAC_CTRL) Priority Level 0 Enable Mask */
#define DMAC_CTRL_LVLEN0(value)               (DMAC_CTRL_LVLEN0_Msk & ((value) << DMAC_CTRL_LVLEN0_Pos))
#define DMAC_CTRL_LVLEN1_Pos                  (9U)                                           /**< (DMAC_CTRL) Priority Level 1 Enable Position */
#define DMAC_CTRL_LVLEN1_Msk                  (0x1U << DMAC_CTRL_LVLEN1_Pos)                 /**< (DMAC_CTRL) Priority Level 1 Enable Mask */
#define DMAC_CTRL_LVLEN1(value)               (DMAC_CTRL_LVLEN1_Msk & ((value) << DMAC_CTRL_LVLEN1_Pos))
#define DMAC_CTRL_LVLEN2_Pos                  (10U)                                          /**< (DMAC_CTRL) Priority Level 2 Enable Position */
#define DMAC_CTRL_LVLEN2_Msk                  (0x1U << DMAC_CTRL_LVLEN2_Pos)                 /**< (DMAC_CTRL) Priority Level 2 Enable Mask */
#define DMAC_CTRL_LVLEN2(value)               (DMAC_CTRL_LVLEN2_Msk & ((value) << DMAC_CTRL_LVLEN2_Pos))
#define DMAC_CTRL_LVLEN3_Pos                  (11U)                                          /**< (DMAC_CTRL) Priority Level 3 Enable Position */
#define DMAC_CTRL_LVLEN3_Msk                  (0x1U << DMAC_CTRL_LVLEN3_Pos)                 /**< (DMAC_CTRL) Priority Level 3 Enable Mask */
#define DMAC_CTRL_LVLEN3(value)               (DMAC_CTRL_LVLEN3_Msk & ((value) << DMAC_CTRL_LVLEN3_Pos))
#define DMAC_CTRL_Msk                         (0x00000F07UL)                                 /**< (DMAC_CTRL) Register Mask  */

/* -------- DMAC_CRCCTRL : (DMAC Offset: 0x02) (R/W 16) CRC Control -------- */
#define DMAC_CRCCTRL_CRCBEATSIZE_Pos          (0U)                                           /**< (DMAC_CRCCTRL) CRC Beat Size Position */
#define DMAC_CRCCTRL_CRCBEATSIZE_Msk          (0x3U << DMAC_CRCCTRL_CRCBEATSIZE_Pos)         /**< (DMAC_CRCCTRL) CRC Beat Size Mask */
#define DMAC_CRCCTRL_CRCBEATSIZE(value)       (DMAC_CRCCTRL_CRCBEATSIZE_Msk & ((value) << DMAC_CRCCTRL_CRCBEATSIZE_Pos))
#define   DMAC_CRCCTRL_CRCBEATSIZE_BYTE_Val   (0U)                                           /**< (DMAC_CRCCTRL) 8-bit bus transfer  */
#define   DMAC_CRCCTRL_CRCBEATSIZE_HWORD_Val  (1U)                                           /**< (DMAC_CRCCTRL) 16-bit bus transfer  */
#define   DMAC_CRCCTRL_CRCBEATSIZE_WORD_Val   (2U)                                           /**< (DMAC_CRCCTRL) 32-bit bus transfer  */
#define DMAC_CRCCTRL_CRCBEATSIZE_BYTE         (DMAC_CRCCTRL_CRCBEATSIZE_BYTE_Val << DMAC_CRCCTRL_CRCBEATSIZE_Pos) /**< (DMAC_CRCCTRL) 8-bit bus transfer Position  */
#define DMAC_CRCCTRL_CRCBEATSIZE_HWORD        (DMAC_CRCCTRL_CRCBEATSIZE_HWORD_Val << DMAC_CRCCTRL_CRCBEATSIZE_Pos) /**< (DMAC_CRCCTRL) 16-bit bus transfer Position  */
#define DMAC_CRCCTRL_CRCBEATSIZE_WORD         (DMAC_CRCCTRL_CRCBEATSIZE_WORD_Val << DMAC_CRCCTRL_CRCBEATSIZE_Pos) /**< (DMAC_CRCCTRL) 32-bit bus transfer Position  */
#define DMAC_CRCCTRL_CRCPOLY_Pos              (2U)                                           /**< (DMAC_CRCCTRL) CRC Polynomial Type Position */
#define DMAC_CRCCTRL_CRCPOLY_Msk              (0x3U << DMAC_CRCCTRL_CRCPOLY_Pos)             /**< (DMAC_CRCCTRL) CRC Polynomial Type Mask */
#define DMAC_CRCCTRL_CRCPOLY(value)           (DMAC_CRCCTRL_CRCPOLY_Msk & ((value) << DMAC_CRCCTRL_CRCPOLY_Pos))
#define   DMAC_CRCCTRL_CRCPOLY_CRC16_Val      (0U)                                           /**< (DMAC_CRCCTRL) CRC-16 (CRC-CCITT)  */
#define   DMAC_CRCCTRL_CRCPOLY_CRC32_Val      (1U)                                           /**< (DMAC_CRCCTRL) CRC32 (IEEE 802.3)  */
#define DMAC_CRCCTRL_CRCPOLY_CRC16            (DMAC_CRCCTRL_CRCPOLY_CRC16_Val << DMAC_CRCCTRL_CRCPOLY_Pos) /**< (DMAC_CRCCTRL) CRC-16 (CRC-CCITT) Position  */
#define DMAC_CRCCTRL_CRCPOLY_CRC32            (DMAC_CRCCTRL_CRCPOLY_CRC32_Val << DMAC_CRCCTRL_CRCPOLY_Pos) /**< (DMAC_CRCCTRL) CRC32 (IEEE 802.3) Position  */
#define DMAC_CRCCTRL_CRCSRC_Pos               (8U)                                           /**< (DMAC_CRCCTRL) CRC Input Source Position */
#define DMAC_CRCCTRL_CRCSRC_Msk               (0x3FU << DMAC_CRCCTRL_CRCSRC_Pos)             /**< (DMAC_CRCCTRL) CRC Input Source Mask */
#define DMAC_CRCCTRL_CRCSRC(value)            (DMAC_CRCCTRL_CRCSRC_Msk & ((value) << DMAC_CRCCTRL_CRCSRC_Pos))
#define   DMAC_CRCCTRL_CRCSRC_NOACT_Val       (0U)                                           /**< (DMAC_CRCCTRL) No action  */
#define   DMAC_CRCCTRL_CRCSRC_IO_Val          (1U)                                           /**< (DMAC_CRCCTRL) I/O interface  */
#define DMAC_CRCCTRL_CRCSRC_NOACT             (DMAC_CRCCTRL_CRCSRC_NOACT_Val << DMAC_CRCCTRL_CRCSRC_Pos) /**< (DMAC_CRCCTRL) No action Position  */
#define DMAC_CRCCTRL_CRCSRC_IO                (DMAC_CRCCTRL_CRCSRC_IO_Val << DMAC_CRCCTRL_CRCSRC_Pos) /**< (DMAC_CRCCTRL) I/O interface Position  */
#define DMAC_CRCCTRL_Msk                      (0x00003F0FUL)                                 /**< (DMAC_CRCCTRL) Register Mask  */

/* -------- DMAC_CRCDATAIN : (DMAC Offset: 0x04) (R/W 32) CRC Data Input -------- */
#define DMAC_CRCDATAIN_CRCDATAIN_Pos          (0U)                                           /**< (DMAC_CRCDATAIN) CRC Data Input Position */
#define DMAC_CRCDATAIN_CRCDATAIN_Msk          (0xFFFFFFFFU << DMAC_CRCDATAIN_CRCDATAIN_Pos)  /**< (DMAC_CRCDATAIN) CRC Data Input Mask */
#define DMAC_CRCDATAIN_CRCDATAIN(value)       (DMAC_CRCDATAIN_CRCDATAIN_Msk & ((value) << DMAC_CRCDATAIN_CRCDATAIN_Pos))
#define DMAC_CRCDATAIN_Msk                    (0xFFFFFFFFUL)                                 /**< (DMAC_CRCDATAIN) Register Mask  */

/* -------- DMAC_CRCCHKSUM : (DMAC Offset: 0x08) (R/W 32) CRC Checksum -------- */
#define DMAC_CRCCHKSUM_CRCCHKSUM_Pos          (0U)                                           /**< (DMAC_CRCCHKSUM) CRC Checksum Position */
#define DMAC_CRCCHKSUM_CRCCHKSUM_Msk          (0xFFFFFFFFU << DMAC_CRCCHKSUM_CRCCHKSUM_Pos)  /**< (DMAC_CRCCHKSUM) CRC Checksum Mask */
#define DMAC_CRCCHKSUM_CRCCHKSUM(value)       (DMAC_CRCCHKSUM_CRCCHKSUM_Msk & ((value) << DMAC_CRCCHKSUM_CRCCHKSUM_Pos))
#define DMAC_CRCCHKSUM_Msk                    (0xFFFFFFFFUL)                                 /**< (DMAC_CRCCHKSUM) Register Mask  */

/* -------- DMAC_CRCSTATUS : (DMAC Offset: 0x0C) (R/W 8) CRC Status -------- */
#define DMAC_CRCSTATUS_CRCBUSY_Pos            (0U)                                           /**< (DMAC_CRCSTATUS) CRC Module Busy Position */
#define DMAC_CRCSTATUS_CRCBUSY_Msk            (0x1U << DMAC_CRCSTATUS_CRCBUSY_Pos)           /**< (DMAC_CRCSTATUS) CRC Module Busy Mask */
#define DMAC_CRCSTATUS_CRCBUSY(value)         (DMAC_CRCSTATUS_CRCBUSY_Msk & ((value) << DMAC_CRCSTATUS_CRCBUSY_Pos))
#define DMAC_CRCSTATUS_CRCZERO_Pos            (1U)                                           /**< (DMAC_CRCSTATUS) CRC Zero Position */
#define DMAC_CRCSTATUS_CRCZERO_Msk            (0x1U << DMAC_CRCSTATUS_CRCZERO_Pos)           /**< (DMAC_CRCSTATUS) CRC Zero Mask */
#define DMAC_CRCSTATUS_CRCZERO(value)         (DMAC_CRCSTATUS_CRCZERO_Msk & ((value) << DMAC_CRCSTATUS_CRCZERO_Pos))
#define DMAC_CRCSTATUS_Msk                    (0x00000003UL)                                 /**< (DMAC_CRCSTATUS) Register Mask  */

/* -------- DMAC_DBGCTRL : (DMAC Offset: 0x0D) (R/W 8) Debug Control -------- */
#define DMAC_DBGCTRL_DBGRUN_Pos               (0U)                                           /**< (DMAC_DBGCTRL) Debug Run Position */
#define DMAC_DBGCTRL_DBGRUN_Msk               (0x1U << DMAC_DBGCTRL_DBGRUN_Pos)              /**< (DMAC_DBGCTRL) Debug Run Mask */
#define DMAC_DBGCTRL_DBGRUN(value)            (DMAC_DBGCTRL_DBGRUN_Msk & ((value) << DMAC_DBGCTRL_DBGRUN_Pos))
#define DMAC_DBGCTRL_Msk                      (0x00000001UL)                                 /**< (DMAC_DBGCTRL) Register Mask  */

/* -------- DMAC_SWTRIGCTRL : (DMAC Offset: 0x10) (R/W 32) Software Trigger Control -------- */
#define DMAC_SWTRIGCTRL_SWTRIG0_Pos           (0U)                                           /**< (DMAC_SWTRIGCTRL) Channel 0 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG0_Msk           (0x1U << DMAC_SWTRIGCTRL_SWTRIG0_Pos)          /**< (DMAC_SWTRIGCTRL) Channel 0 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG0(value)        (DMAC_SWTRIGCTRL_SWTRIG0_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG0_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG1_Pos           (1U)                                           /**< (DMAC_SWTRIGCTRL) Channel 1 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG1_Msk           (0x1U << DMAC_SWTRIGCTRL_SWTRIG1_Pos)          /**< (DMAC_SWTRIGCTRL) Channel 1 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG1(value)        (DMAC_SWTRIGCTRL_SWTRIG1_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG1_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG2_Pos           (2U)                                           /**< (DMAC_SWTRIGCTRL) Channel 2 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG2_Msk           (0x1U << DMAC_SWTRIGCTRL_SWTRIG2_Pos)          /**< (DMAC_SWTRIGCTRL) Channel 2 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG2(value)        (DMAC_SWTRIGCTRL_SWTRIG2_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG2_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG3_Pos           (3U)                                           /**< (DMAC_SWTRIGCTRL) Channel 3 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG3_Msk           (0x1U << DMAC_SWTRIGCTRL_SWTRIG3_Pos)          /**< (DMAC_SWTRIGCTRL) Channel 3 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG3(value)        (DMAC_SWTRIGCTRL_SWTRIG3_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG3_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG4_Pos           (4U)                                           /**< (DMAC_SWTRIGCTRL) Channel 4 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG4_Msk           (0x1U << DMAC_SWTRIGCTRL_SWTRIG4_Pos)          /**< (DMAC_SWTRIGCTRL) Channel 4 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG4(value)        (DMAC_SWTRIGCTRL_SWTRIG4_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG4_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG5_Pos           (5U)                                           /**< (DMAC_SWTRIGCTRL) Channel 5 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG5_Msk           (0x1U << DMAC_SWTRIGCTRL_SWTRIG5_Pos)          /**< (DMAC_SWTRIGCTRL) Channel 5 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG5(value)        (DMAC_SWTRIGCTRL_SWTRIG5_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG5_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG6_Pos           (6U)                                           /**< (DMAC_SWTRIGCTRL) Channel 6 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG6_Msk           (0x1U << DMAC_SWTRIGCTRL_SWTRIG6_Pos)          /**< (DMAC_SWTRIGCTRL) Channel 6 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG6(value)        (DMAC_SWTRIGCTRL_SWTRIG6_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG6_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG7_Pos           (7U)                                           /**< (DMAC_SWTRIGCTRL) Channel 7 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG7_Msk           (0x1U << DMAC_SWTRIGCTRL_SWTRIG7_Pos)          /**< (DMAC_SWTRIGCTRL) Channel 7 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG7(value)        (DMAC_SWTRIGCTRL_SWTRIG7_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG7_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG8_Pos           (8U)                                           /**< (DMAC_SWTRIGCTRL) Channel 8 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG8_Msk           (0x1U << DMAC_SWTRIGCTRL_SWTRIG8_Pos)          /**< (DMAC_SWTRIGCTRL) Channel 8 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG8(value)        (DMAC_SWTRIGCTRL_SWTRIG8_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG8_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG9_Pos           (9U)                                           /**< (DMAC_SWTRIGCTRL) Channel 9 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG9_Msk           (0x1U << DMAC_SWTRIGCTRL_SWTRIG9_Pos)          /**< (DMAC_SWTRIGCTRL) Channel 9 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG9(value)        (DMAC_SWTRIGCTRL_SWTRIG9_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG9_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG10_Pos          (10U)                                          /**< (DMAC_SWTRIGCTRL) Channel 10 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG10_Msk          (0x1U << DMAC_SWTRIGCTRL_SWTRIG10_Pos)         /**< (DMAC_SWTRIGCTRL) Channel 10 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG10(value)       (DMAC_SWTRIGCTRL_SWTRIG10_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG10_Pos))
#define DMAC_SWTRIGCTRL_SWTRIG11_Pos          (11U)                                          /**< (DMAC_SWTRIGCTRL) Channel 11 Software Trigger Position */
#define DMAC_SWTRIGCTRL_SWTRIG11_Msk          (0x1U << DMAC_SWTRIGCTRL_SWTRIG11_Pos)         /**< (DMAC_SWTRIGCTRL) Channel 11 Software Trigger Mask */
#define DMAC_SWTRIGCTRL_SWTRIG11(value)       (DMAC_SWTRIGCTRL_SWTRIG11_Msk & ((value) << DMAC_SWTRIGCTRL_SWTRIG11_Pos))
#define DMAC_SWTRIGCTRL_Msk                   (0x00000FFFUL)                                 /**< (DMAC_SWTRIGCTRL) Register Mask  */

/* -------- DMAC_PRICTRL0 : (DMAC Offset: 0x14) (R/W 32) Priority Control 0 -------- */
#define DMAC_PRICTRL0_LVLPRI0_Pos             (0U)                                           /**< (DMAC_PRICTRL0) Level 0 Channel Priority Number Position */
#define DMAC_PRICTRL0_LVLPRI0_Msk             (0xFU << DMAC_PRICTRL0_LVLPRI0_Pos)            /**< (DMAC_PRICTRL0) Level 0 Channel Priority Number Mask */
#define DMAC_PRICTRL0_LVLPRI0(value)          (DMAC_PRICTRL0_LVLPRI0_Msk & ((value) << DMAC_PRICTRL0_LVLPRI0_Pos))
#define DMAC_PRICTRL0_RRLVLEN0_Pos            (7U)                                           /**< (DMAC_PRICTRL0) Level 0 Round-Robin Scheduling Enable Position */
#define DMAC_PRICTRL0_RRLVLEN0_Msk            (0x1U << DMAC_PRICTRL0_RRLVLEN0_Pos)           /**< (DMAC_PRICTRL0) Level 0 Round-Robin Scheduling Enable Mask */
#define DMAC_PRICTRL0_RRLVLEN0(value)         (DMAC_PRICTRL0_RRLVLEN0_Msk & ((value) << DMAC_PRICTRL0_RRLVLEN0_Pos))
#define   DMAC_PRICTRL0_RRLVLEN0_STATIC_LVL_Val (0U)                                           /**< (DMAC_PRICTRL0) Static arbitration scheme for channels with level 3 priority  */
#define   DMAC_PRICTRL0_RRLVLEN0_ROUND_ROBIN_LVL_Val (1U)                                           /**< (DMAC_PRICTRL0) Round-robin arbitration scheme for channels with level 3 priority  */
#define DMAC_PRICTRL0_RRLVLEN0_STATIC_LVL     (DMAC_PRICTRL0_RRLVLEN0_STATIC_LVL_Val << DMAC_PRICTRL0_RRLVLEN0_Pos) /**< (DMAC_PRICTRL0) Static arbitration scheme for channels with level 3 priority Position  */
#define DMAC_PRICTRL0_RRLVLEN0_ROUND_ROBIN_LVL (DMAC_PRICTRL0_RRLVLEN0_ROUND_ROBIN_LVL_Val << DMAC_PRICTRL0_RRLVLEN0_Pos) /**< (DMAC_PRICTRL0) Round-robin arbitration scheme for channels with level 3 priority Position  */
#define DMAC_PRICTRL0_LVLPRI1_Pos             (8U)                                           /**< (DMAC_PRICTRL0) Level 1 Channel Priority Number Position */
#define DMAC_PRICTRL0_LVLPRI1_Msk             (0xFU << DMAC_PRICTRL0_LVLPRI1_Pos)            /**< (DMAC_PRICTRL0) Level 1 Channel Priority Number Mask */
#define DMAC_PRICTRL0_LVLPRI1(value)          (DMAC_PRICTRL0_LVLPRI1_Msk & ((value) << DMAC_PRICTRL0_LVLPRI1_Pos))
#define DMAC_PRICTRL0_RRLVLEN1_Pos            (15U)                                          /**< (DMAC_PRICTRL0) Level 1 Round-Robin Scheduling Enable Position */
#define DMAC_PRICTRL0_RRLVLEN1_Msk            (0x1U << DMAC_PRICTRL0_RRLVLEN1_Pos)           /**< (DMAC_PRICTRL0) Level 1 Round-Robin Scheduling Enable Mask */
#define DMAC_PRICTRL0_RRLVLEN1(value)         (DMAC_PRICTRL0_RRLVLEN1_Msk & ((value) << DMAC_PRICTRL0_RRLVLEN1_Pos))
#define DMAC_PRICTRL0_LVLPRI2_Pos             (16U)                                          /**< (DMAC_PRICTRL0) Level 2 Channel Priority Number Position */
#define DMAC_PRICTRL0_LVLPRI2_Msk             (0xFU << DMAC_PRICTRL0_LVLPRI2_Pos)            /**< (DMAC_PRICTRL0) Level 2 Channel Priority Number Mask */
#define DMAC_PRICTRL0_LVLPRI2(value)          (DMAC_PRICTRL0_LVLPRI2_Msk & ((value) << DMAC_PRICTRL0_LVLPRI2_Pos))
#define DMAC_PRICTRL0_RRLVLEN2_Pos            (23U)                                          /**< (DMAC_PRICTRL0) Level 2 Round-Robin Scheduling Enable Position */
#define DMAC_PRICTRL0_RRLVLEN2_Msk            (0x1U << DMAC_PRICTRL0_RRLVLEN2_Pos)           /**< (DMAC_PRICTRL0) Level 2 Round-Robin Scheduling Enable Mask */
#define DMAC_PRICTRL0_RRLVLEN2(value)         (DMAC_PRICTRL0_RRLVLEN2_Msk & ((value) << DMAC_PRICTRL0_RRLVLEN2_Pos))
#define DMAC_PRICTRL0_LVLPRI3_Pos             (24U)                                          /**< (DMAC_PRICTRL0) Level 3 Channel Priority Number Position */
#define DMAC_PRICTRL0_LVLPRI3_Msk             (0xFU << DMAC_PRICTRL0_LVLPRI3_Pos)            /**< (DMAC_PRICTRL0) Level 3 Channel Priority Number Mask */
#define DMAC_PRICTRL0_LVLPRI3(value)          (DMAC_PRICTRL0_LVLPRI3_Msk & ((value) << DMAC_PRICTRL0_LVLPRI3_Pos))
#define DMAC_PRICTRL0_RRLVLEN3_Pos            (31U)                                          /**< (DMAC_PRICTRL0) Level 3 Round-Robin Scheduling Enable Position */
#define DMAC_PRICTRL0_RRLVLEN3_Msk            (0x1U << DMAC_PRICTRL0_RRLVLEN3_Pos)           /**< (DMAC_PRICTRL0) Level 3 Round-Robin Scheduling Enable Mask */
#define DMAC_PRICTRL0_RRLVLEN3(value)         (DMAC_PRICTRL0_RRLVLEN3_Msk & ((value) << DMAC_PRICTRL0_RRLVLEN3_Pos))
#define DMAC_PRICTRL0_Msk                     (0x8F8F8F8FUL)                                 /**< (DMAC_PRICTRL0) Register Mask  */

/* -------- DMAC_INTPEND : (DMAC Offset: 0x20) (R/W 16) Interrupt Pending -------- */
#define DMAC_INTPEND_ID_Pos                   (0U)                                           /**< (DMAC_INTPEND) Channel ID Position */
#define DMAC_INTPEND_ID_Msk                   (0xFU << DMAC_INTPEND_ID_Pos)                  /**< (DMAC_INTPEND) Channel ID Mask */
#define DMAC_INTPEND_ID(value)                (DMAC_INTPEND_ID_Msk & ((value) << DMAC_INTPEND_ID_Pos))
#define DMAC_INTPEND_TERR_Pos                 (8U)                                           /**< (DMAC_INTPEND) Transfer Error Position */
#define DMAC_INTPEND_TERR_Msk                 (0x1U << DMAC_INTPEND_TERR_Pos)                /**< (DMAC_INTPEND) Transfer Error Mask */
#define DMAC_INTPEND_TERR(value)              (DMAC_INTPEND_TERR_Msk & ((value) << DMAC_INTPEND_TERR_Pos))
#define DMAC_INTPEND_TCMPL_Pos                (9U)                                           /**< (DMAC_INTPEND) Transfer Complete Position */
#define DMAC_INTPEND_TCMPL_Msk                (0x1U << DMAC_INTPEND_TCMPL_Pos)               /**< (DMAC_INTPEND) Transfer Complete Mask */
#define DMAC_INTPEND_TCMPL(value)             (DMAC_INTPEND_TCMPL_Msk & ((value) << DMAC_INTPEND_TCMPL_Pos))
#define DMAC_INTPEND_SUSP_Pos                 (10U)                                          /**< (DMAC_INTPEND) Channel Suspend Position */
#define DMAC_INTPEND_SUSP_Msk                 (0x1U << DMAC_INTPEND_SUSP_Pos)                /**< (DMAC_INTPEND) Channel Suspend Mask */
#define DMAC_INTPEND_SUSP(value)              (DMAC_INTPEND_SUSP_Msk & ((value) << DMAC_INTPEND_SUSP_Pos))
#define DMAC_INTPEND_FERR_Pos                 (13U)                                          /**< (DMAC_INTPEND) Fetch Error Position */
#define DMAC_INTPEND_FERR_Msk                 (0x1U << DMAC_INTPEND_FERR_Pos)                /**< (DMAC_INTPEND) Fetch Error Mask */
#define DMAC_INTPEND_FERR(value)              (DMAC_INTPEND_FERR_Msk & ((value) << DMAC_INTPEND_FERR_Pos))
#define DMAC_INTPEND_BUSY_Pos                 (14U)                                          /**< (DMAC_INTPEND) Busy Position */
#define DMAC_INTPEND_BUSY_Msk                 (0x1U << DMAC_INTPEND_BUSY_Pos)                /**< (DMAC_INTPEND) Busy Mask */
#define DMAC_INTPEND_BUSY(value)              (DMAC_INTPEND_BUSY_Msk & ((value) << DMAC_INTPEND_BUSY_Pos))
#define DMAC_INTPEND_PEND_Pos                 (15U)                                          /**< (DMAC_INTPEND) Pending Position */
#define DMAC_INTPEND_PEND_Msk                 (0x1U << DMAC_INTPEND_PEND_Pos)                /**< (DMAC_INTPEND) Pending Mask */
#define DMAC_INTPEND_PEND(value)              (DMAC_INTPEND_PEND_Msk & ((value) << DMAC_INTPEND_PEND_Pos))
#define DMAC_INTPEND_Msk                      (0x0000E70FUL)                                 /**< (DMAC_INTPEND) Register Mask  */

/* -------- DMAC_INTSTATUS : (DMAC Offset: 0x24) (R/  32) Interrupt Status -------- */
#define DMAC_INTSTATUS_CHINT0_Pos             (0U)                                           /**< (DMAC_INTSTATUS) Channel 0 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT0_Msk             (0x1U << DMAC_INTSTATUS_CHINT0_Pos)            /**< (DMAC_INTSTATUS) Channel 0 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT0(value)          (DMAC_INTSTATUS_CHINT0_Msk & ((value) << DMAC_INTSTATUS_CHINT0_Pos))
#define DMAC_INTSTATUS_CHINT1_Pos             (1U)                                           /**< (DMAC_INTSTATUS) Channel 1 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT1_Msk             (0x1U << DMAC_INTSTATUS_CHINT1_Pos)            /**< (DMAC_INTSTATUS) Channel 1 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT1(value)          (DMAC_INTSTATUS_CHINT1_Msk & ((value) << DMAC_INTSTATUS_CHINT1_Pos))
#define DMAC_INTSTATUS_CHINT2_Pos             (2U)                                           /**< (DMAC_INTSTATUS) Channel 2 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT2_Msk             (0x1U << DMAC_INTSTATUS_CHINT2_Pos)            /**< (DMAC_INTSTATUS) Channel 2 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT2(value)          (DMAC_INTSTATUS_CHINT2_Msk & ((value) << DMAC_INTSTATUS_CHINT2_Pos))
#define DMAC_INTSTATUS_CHINT3_Pos             (3U)                                           /**< (DMAC_INTSTATUS) Channel 3 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT3_Msk             (0x1U << DMAC_INTSTATUS_CHINT3_Pos)            /**< (DMAC_INTSTATUS) Channel 3 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT3(value)          (DMAC_INTSTATUS_CHINT3_Msk & ((value) << DMAC_INTSTATUS_CHINT3_Pos))
#define DMAC_INTSTATUS_CHINT4_Pos             (4U)                                           /**< (DMAC_INTSTATUS) Channel 4 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT4_Msk             (0x1U << DMAC_INTSTATUS_CHINT4_Pos)            /**< (DMAC_INTSTATUS) Channel 4 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT4(value)          (DMAC_INTSTATUS_CHINT4_Msk & ((value) << DMAC_INTSTATUS_CHINT4_Pos))
#define DMAC_INTSTATUS_CHINT5_Pos             (5U)                                           /**< (DMAC_INTSTATUS) Channel 5 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT5_Msk             (0x1U << DMAC_INTSTATUS_CHINT5_Pos)            /**< (DMAC_INTSTATUS) Channel 5 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT5(value)          (DMAC_INTSTATUS_CHINT5_Msk & ((value) << DMAC_INTSTATUS_CHINT5_Pos))
#define DMAC_INTSTATUS_CHINT6_Pos             (6U)                                           /**< (DMAC_INTSTATUS) Channel 6 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT6_Msk             (0x1U << DMAC_INTSTATUS_CHINT6_Pos)            /**< (DMAC_INTSTATUS) Channel 6 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT6(value)          (DMAC_INTSTATUS_CHINT6_Msk & ((value) << DMAC_INTSTATUS_CHINT6_Pos))
#define DMAC_INTSTATUS_CHINT7_Pos             (7U)                                           /**< (DMAC_INTSTATUS) Channel 7 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT7_Msk             (0x1U << DMAC_INTSTATUS_CHINT7_Pos)            /**< (DMAC_INTSTATUS) Channel 7 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT7(value)          (DMAC_INTSTATUS_CHINT7_Msk & ((value) << DMAC_INTSTATUS_CHINT7_Pos))
#define DMAC_INTSTATUS_CHINT8_Pos             (8U)                                           /**< (DMAC_INTSTATUS) Channel 8 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT8_Msk             (0x1U << DMAC_INTSTATUS_CHINT8_Pos)            /**< (DMAC_INTSTATUS) Channel 8 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT8(value)          (DMAC_INTSTATUS_CHINT8_Msk & ((value) << DMAC_INTSTATUS_CHINT8_Pos))
#define DMAC_INTSTATUS_CHINT9_Pos             (9U)                                           /**< (DMAC_INTSTATUS) Channel 9 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT9_Msk             (0x1U << DMAC_INTSTATUS_CHINT9_Pos)            /**< (DMAC_INTSTATUS) Channel 9 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT9(value)          (DMAC_INTSTATUS_CHINT9_Msk & ((value) << DMAC_INTSTATUS_CHINT9_Pos))
#define DMAC_INTSTATUS_CHINT10_Pos            (10U)                                          /**< (DMAC_INTSTATUS) Channel 10 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT10_Msk            (0x1U << DMAC_INTSTATUS_CHINT10_Pos)           /**< (DMAC_INTSTATUS) Channel 10 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT10(value)         (DMAC_INTSTATUS_CHINT10_Msk & ((value) << DMAC_INTSTATUS_CHINT10_Pos))
#define DMAC_INTSTATUS_CHINT11_Pos            (11U)                                          /**< (DMAC_INTSTATUS) Channel 11 Pending Interrupt Position */
#define DMAC_INTSTATUS_CHINT11_Msk            (0x1U << DMAC_INTSTATUS_CHINT11_Pos)           /**< (DMAC_INTSTATUS) Channel 11 Pending Interrupt Mask */
#define DMAC_INTSTATUS_CHINT11(value)         (DMAC_INTSTATUS_CHINT11_Msk & ((value) << DMAC_INTSTATUS_CHINT11_Pos))
#define DMAC_INTSTATUS_Msk                    (0x00000FFFUL)                                 /**< (DMAC_INTSTATUS) Register Mask  */

/* -------- DMAC_BUSYCH : (DMAC Offset: 0x28) (R/  32) Busy Channels -------- */
#define DMAC_BUSYCH_BUSYCH0_Pos               (0U)                                           /**< (DMAC_BUSYCH) Busy Channel 0 Position */
#define DMAC_BUSYCH_BUSYCH0_Msk               (0x1U << DMAC_BUSYCH_BUSYCH0_Pos)              /**< (DMAC_BUSYCH) Busy Channel 0 Mask */
#define DMAC_BUSYCH_BUSYCH0(value)            (DMAC_BUSYCH_BUSYCH0_Msk & ((value) << DMAC_BUSYCH_BUSYCH0_Pos))
#define DMAC_BUSYCH_BUSYCH1_Pos               (1U)                                           /**< (DMAC_BUSYCH) Busy Channel 1 Position */
#define DMAC_BUSYCH_BUSYCH1_Msk               (0x1U << DMAC_BUSYCH_BUSYCH1_Pos)              /**< (DMAC_BUSYCH) Busy Channel 1 Mask */
#define DMAC_BUSYCH_BUSYCH1(value)            (DMAC_BUSYCH_BUSYCH1_Msk & ((value) << DMAC_BUSYCH_BUSYCH1_Pos))
#define DMAC_BUSYCH_BUSYCH2_Pos               (2U)                                           /**< (DMAC_BUSYCH) Busy Channel 2 Position */
#define DMAC_BUSYCH_BUSYCH2_Msk               (0x1U << DMAC_BUSYCH_BUSYCH2_Pos)              /**< (DMAC_BUSYCH) Busy Channel 2 Mask */
#define DMAC_BUSYCH_BUSYCH2(value)            (DMAC_BUSYCH_BUSYCH2_Msk & ((value) << DMAC_BUSYCH_BUSYCH2_Pos))
#define DMAC_BUSYCH_BUSYCH3_Pos               (3U)                                           /**< (DMAC_BUSYCH) Busy Channel 3 Position */
#define DMAC_BUSYCH_BUSYCH3_Msk               (0x1U << DMAC_BUSYCH_BUSYCH3_Pos)              /**< (DMAC_BUSYCH) Busy Channel 3 Mask */
#define DMAC_BUSYCH_BUSYCH3(value)            (DMAC_BUSYCH_BUSYCH3_Msk & ((value) << DMAC_BUSYCH_BUSYCH3_Pos))
#define DMAC_BUSYCH_BUSYCH4_Pos               (4U)                                           /**< (DMAC_BUSYCH) Busy Channel 4 Position */
#define DMAC_BUSYCH_BUSYCH4_Msk               (0x1U << DMAC_BUSYCH_BUSYCH4_Pos)              /**< (DMAC_BUSYCH) Busy Channel 4 Mask */
#define DMAC_BUSYCH_BUSYCH4(value)            (DMAC_BUSYCH_BUSYCH4_Msk & ((value) << DMAC_BUSYCH_BUSYCH4_Pos))
#define DMAC_BUSYCH_BUSYCH5_Pos               (5U)                                           /**< (DMAC_BUSYCH) Busy Channel 5 Position */
#define DMAC_BUSYCH_BUSYCH5_Msk               (0x1U << DMAC_BUSYCH_BUSYCH5_Pos)              /**< (DMAC_BUSYCH) Busy Channel 5 Mask */
#define DMAC_BUSYCH_BUSYCH5(value)            (DMAC_BUSYCH_BUSYCH5_Msk & ((value) << DMAC_BUSYCH_BUSYCH5_Pos))
#define DMAC_BUSYCH_BUSYCH6_Pos               (6U)                                           /**< (DMAC_BUSYCH) Busy Channel 6 Position */
#define DMAC_BUSYCH_BUSYCH6_Msk               (0x1U << DMAC_BUSYCH_BUSYCH6_Pos)              /**< (DMAC_BUSYCH) Busy Channel 6 Mask */
#define DMAC_BUSYCH_BUSYCH6(value)            (DMAC_BUSYCH_BUSYCH6_Msk & ((value) << DMAC_BUSYCH_BUSYCH6_Pos))
#define DMAC_BUSYCH_BUSYCH7_Pos               (7U)                                           /**< (DMAC_BUSYCH) Busy Channel 7 Position */
#define DMAC_BUSYCH_BUSYCH7_Msk               (0x1U << DMAC_BUSYCH_BUSYCH7_Pos)              /**< (DMAC_BUSYCH) Busy Channel 7 Mask */
#define DMAC_BUSYCH_BUSYCH7(value)            (DMAC_BUSYCH_BUSYCH7_Msk & ((value) << DMAC_BUSYCH_BUSYCH7_Pos))
#define DMAC_BUSYCH_BUSYCH8_Pos               (8U)                                           /**< (DMAC_BUSYCH) Busy Channel 8 Position */
#define DMAC_BUSYCH_BUSYCH8_Msk               (0x1U << DMAC_BUSYCH_BUSYCH8_Pos)              /**< (DMAC_BUSYCH) Busy Channel 8 Mask */
#define DMAC_BUSYCH_BUSYCH8(value)            (DMAC_BUSYCH_BUSYCH8_Msk & ((value) << DMAC_BUSYCH_BUSYCH8_Pos))
#define DMAC_BUSYCH_BUSYCH9_Pos               (9U)                                           /**< (DMAC_BUSYCH) Busy Channel 9 Position */
#define DMAC_BUSYCH_BUSYCH9_Msk               (0x1U << DMAC_BUSYCH_BUSYCH9_Pos)              /**< (DMAC_BUSYCH) Busy Channel 9 Mask */
#define DMAC_BUSYCH_BUSYCH9(value)            (DMAC_BUSYCH_BUSYCH9_Msk & ((value) << DMAC_BUSYCH_BUSYCH9_Pos))
#define DMAC_BUSYCH_BUSYCH10_Pos              (10U)                                          /**< (DMAC_BUSYCH) Busy Channel 10 Position */
#define DMAC_BUSYCH_BUSYCH10_Msk              (0x1U << DMAC_BUSYCH_BUSYCH10_Pos)             /**< (DMAC_BUSYCH) Busy Channel 10 Mask */
#define DMAC_BUSYCH_BUSYCH10(value)           (DMAC_BUSYCH_BUSYCH10_Msk & ((value) << DMAC_BUSYCH_BUSYCH10_Pos))
#define DMAC_BUSYCH_BUSYCH11_Pos              (11U)                                          /**< (DMAC_BUSYCH) Busy Channel 11 Position */
#define DMAC_BUSYCH_BUSYCH11_Msk              (0x1U << DMAC_BUSYCH_BUSYCH11_Pos)             /**< (DMAC_BUSYCH) Busy Channel 11 Mask */
#define DMAC_BUSYCH_BUSYCH11(value)           (DMAC_BUSYCH_BUSYCH11_Msk & ((value) << DMAC_BUSYCH_BUSYCH11_Pos))
#define DMAC_BUSYCH_Msk                       (0x00000FFFUL)                                 /**< (DMAC_BUSYCH) Register Mask  */

/* -------- DMAC_PENDCH : (DMAC Offset: 0x2C) (R/  32) Pending Channels -------- */
#define DMAC_PENDCH_PENDCH0_Pos               (0U)                                           /**< (DMAC_PENDCH) Pending Channel 0 Position */
#define DMAC_PENDCH_PENDCH0_Msk               (0x1U << DMAC_PENDCH_PENDCH0_Pos)              /**< (DMAC_PENDCH) Pending Channel 0 Mask */
#define DMAC_PENDCH_PENDCH0(value)            (DMAC_PENDCH_PENDCH0_Msk & ((value) << DMAC_PENDCH_PENDCH0_Pos))
#define DMAC_PENDCH_PENDCH1_Pos               (1U)                                           /**< (DMAC_PENDCH) Pending Channel 1 Position */
#define DMAC_PENDCH_PENDCH1_Msk               (0x1U << DMAC_PENDCH_PENDCH1_Pos)              /**< (DMAC_PENDCH) Pending Channel 1 Mask */
#define DMAC_PENDCH_PENDCH1(value)            (DMAC_PENDCH_PENDCH1_Msk & ((value) << DMAC_PENDCH_PENDCH1_Pos))
#define DMAC_PENDCH_PENDCH2_Pos               (2U)                                           /**< (DMAC_PENDCH) Pending Channel 2 Position */
#define DMAC_PENDCH_PENDCH2_Msk               (0x1U << DMAC_PENDCH_PENDCH2_Pos)              /**< (DMAC_PENDCH) Pending Channel 2 Mask */
#define DMAC_PENDCH_PENDCH2(value)            (DMAC_PENDCH_PENDCH2_Msk & ((value) << DMAC_PENDCH_PENDCH2_Pos))
#define DMAC_PENDCH_PENDCH3_Pos               (3U)                                           /**< (DMAC_PENDCH) Pending Channel 3 Position */
#define DMAC_PENDCH_PENDCH3_Msk               (0x1U << DMAC_PENDCH_PENDCH3_Pos)              /**< (DMAC_PENDCH) Pending Channel 3 Mask */
#define DMAC_PENDCH_PENDCH3(value)            (DMAC_PENDCH_PENDCH3_Msk & ((value) << DMAC_PENDCH_PENDCH3_Pos))
#define DMAC_PENDCH_PENDCH4_Pos               (4U)                                           /**< (DMAC_PENDCH) Pending Channel 4 Position */
#define DMAC_PENDCH_PENDCH4_Msk               (0x1U << DMAC_PENDCH_PENDCH4_Pos)              /**< (DMAC_PENDCH) Pending Channel 4 Mask */
#define DMAC_PENDCH_PENDCH4(value)            (DMAC_PENDCH_PENDCH4_Msk & ((value) << DMAC_PENDCH_PENDCH4_Pos))
#define DMAC_PENDCH_PENDCH5_Pos               (5U)                                           /**< (DMAC_PENDCH) Pending Channel 5 Position */
#define DMAC_PENDCH_PENDCH5_Msk               (0x1U << DMAC_PENDCH_PENDCH5_Pos)              /**< (DMAC_PENDCH) Pending Channel 5 Mask */
#define DMAC_PENDCH_PENDCH5(value)            (DMAC_PENDCH_PENDCH5_Msk & ((value) << DMAC_PENDCH_PENDCH5_Pos))
#define DMAC_PENDCH_PENDCH6_Pos               (6U)                                           /**< (DMAC_PENDCH) Pending Channel 6 Position */
#define DMAC_PENDCH_PENDCH6_Msk               (0x1U << DMAC_PENDCH_PENDCH6_Pos)              /**< (DMAC_PENDCH) Pending Channel 6 Mask */
#define DMAC_PENDCH_PENDCH6(value)            (DMAC_PENDCH_PENDCH6_Msk & ((value) << DMAC_PENDCH_PENDCH6_Pos))
#define DMAC_PENDCH_PENDCH7_Pos               (7U)                                           /**< (DMAC_PENDCH) Pending Channel 7 Position */
#define DMAC_PENDCH_PENDCH7_Msk               (0x1U << DMAC_PENDCH_PENDCH7_Pos)              /**< (DMAC_PENDCH) Pending Channel 7 Mask */
#define DMAC_PENDCH_PENDCH7(value)            (DMAC_PENDCH_PENDCH7_Msk & ((value) << DMAC_PENDCH_PENDCH7_Pos))
#define DMAC_PENDCH_PENDCH8_Pos               (8U)                                           /**< (DMAC_PENDCH) Pending Channel 8 Position */
#define DMAC_PENDCH_PENDCH8_Msk               (0x1U << DMAC_PENDCH_PENDCH8_Pos)              /**< (DMAC_PENDCH) Pending Channel 8 Mask */
#define DMAC_PENDCH_PENDCH8(value)            (DMAC_PENDCH_PENDCH8_Msk & ((value) << DMAC_PENDCH_PENDCH8_Pos))
#define DMAC_PENDCH_PENDCH9_Pos               (9U)                                           /**< (DMAC_PENDCH) Pending Channel 9 Position */
#define DMAC_PENDCH_PENDCH9_Msk               (0x1U << DMAC_PENDCH_PENDCH9_Pos)              /**< (DMAC_PENDCH) Pending Channel 9 Mask */
#define DMAC_PENDCH_PENDCH9(value)            (DMAC_PENDCH_PENDCH9_Msk & ((value) << DMAC_PENDCH_PENDCH9_Pos))
#define DMAC_PENDCH_PENDCH10_Pos              (10U)                                          /**< (DMAC_PENDCH) Pending Channel 10 Position */
#define DMAC_PENDCH_PENDCH10_Msk              (0x1U << DMAC_PENDCH_PENDCH10_Pos)             /**< (DMAC_PENDCH) Pending Channel 10 Mask */
#define DMAC_PENDCH_PENDCH10(value)           (DMAC_PENDCH_PENDCH10_Msk & ((value) << DMAC_PENDCH_PENDCH10_Pos))
#define DMAC_PENDCH_PENDCH11_Pos              (11U)                                          /**< (DMAC_PENDCH) Pending Channel 11 Position */
#define DMAC_PENDCH_PENDCH11_Msk              (0x1U << DMAC_PENDCH_PENDCH11_Pos)             /**< (DMAC_PENDCH) Pending Channel 11 Mask */
#define DMAC_PENDCH_PENDCH11(value)           (DMAC_PENDCH_PENDCH11_Msk & ((value) << DMAC_PENDCH_PENDCH11_Pos))
#define DMAC_PENDCH_Msk                       (0x00000FFFUL)                                 /**< (DMAC_PENDCH) Register Mask  */

/* -------- DMAC_ACTIVE : (DMAC Offset: 0x30) (R/  32) Active Channel and Levels -------- */
#define DMAC_ACTIVE_LVLEX0_Pos                (0U)                                           /**< (DMAC_ACTIVE) Level 0 Channel Trigger Request Executing Position */
#define DMAC_ACTIVE_LVLEX0_Msk                (0x1U << DMAC_ACTIVE_LVLEX0_Pos)               /**< (DMAC_ACTIVE) Level 0 Channel Trigger Request Executing Mask */
#define DMAC_ACTIVE_LVLEX0(value)             (DMAC_ACTIVE_LVLEX0_Msk & ((value) << DMAC_ACTIVE_LVLEX0_Pos))
#define DMAC_ACTIVE_LVLEX1_Pos                (1U)                                           /**< (DMAC_ACTIVE) Level 1 Channel Trigger Request Executing Position */
#define DMAC_ACTIVE_LVLEX1_Msk                (0x1U << DMAC_ACTIVE_LVLEX1_Pos)               /**< (DMAC_ACTIVE) Level 1 Channel Trigger Request Executing Mask */
#define DMAC_ACTIVE_LVLEX1(value)             (DMAC_ACTIVE_LVLEX1_Msk & ((value) << DMAC_ACTIVE_LVLEX1_Pos))
#define DMAC_ACTIVE_LVLEX2_Pos                (2U)                                           /**< (DMAC_ACTIVE) Level 2 Channel Trigger Request Executing Position */
#define DMAC_ACTIVE_LVLEX2_Msk                (0x1U << DMAC_ACTIVE_LVLEX2_Pos)               /**< (DMAC_ACTIVE) Level 2 Channel Trigger Request Executing Mask */
#define DMAC_ACTIVE_LVLEX2(value)             (DMAC_ACTIVE_LVLEX2_Msk & ((value) << DMAC_ACTIVE_LVLEX2_Pos))
#define DMAC_ACTIVE_LVLEX3_Pos                (3U)                                           /**< (DMAC_ACTIVE) Level 3 Channel Trigger Request Executing Position */
#define DMAC_ACTIVE_LVLEX3_Msk                (0x1U << DMAC_ACTIVE_LVLEX3_Pos)               /**< (DMAC_ACTIVE) Level 3 Channel Trigger Request Executing Mask */
#define DMAC_ACTIVE_LVLEX3(value)             (DMAC_ACTIVE_LVLEX3_Msk & ((value) << DMAC_ACTIVE_LVLEX3_Pos))
#define DMAC_ACTIVE_ID_Pos                    (8U)                                           /**< (DMAC_ACTIVE) Active Channel ID Position */
#define DMAC_ACTIVE_ID_Msk                    (0x1FU << DMAC_ACTIVE_ID_Pos)                  /**< (DMAC_ACTIVE) Active Channel ID Mask */
#define DMAC_ACTIVE_ID(value)                 (DMAC_ACTIVE_ID_Msk & ((value) << DMAC_ACTIVE_ID_Pos))
#define DMAC_ACTIVE_ABUSY_Pos                 (15U)                                          /**< (DMAC_ACTIVE) Active Channel Busy Position */
#define DMAC_ACTIVE_ABUSY_Msk                 (0x1U << DMAC_ACTIVE_ABUSY_Pos)                /**< (DMAC_ACTIVE) Active Channel Busy Mask */
#define DMAC_ACTIVE_ABUSY(value)              (DMAC_ACTIVE_ABUSY_Msk & ((value) << DMAC_ACTIVE_ABUSY_Pos))
#define DMAC_ACTIVE_BTCNT_Pos                 (16U)                                          /**< (DMAC_ACTIVE) Active Channel Block Transfer Count Position */
#define DMAC_ACTIVE_BTCNT_Msk                 (0xFFFFU << DMAC_ACTIVE_BTCNT_Pos)             /**< (DMAC_ACTIVE) Active Channel Block Transfer Count Mask */
#define DMAC_ACTIVE_BTCNT(value)              (DMAC_ACTIVE_BTCNT_Msk & ((value) << DMAC_ACTIVE_BTCNT_Pos))
#define DMAC_ACTIVE_Msk                       (0xFFFF9F0FUL)                                 /**< (DMAC_ACTIVE) Register Mask  */

/* -------- DMAC_BASEADDR : (DMAC Offset: 0x34) (R/W 32) Descriptor Memory Section Base Address -------- */
#define DMAC_BASEADDR_BASEADDR_Pos            (0U)                                           /**< (DMAC_BASEADDR) Descriptor Memory Base Address Position */
#define DMAC_BASEADDR_BASEADDR_Msk            (0xFFFFFFFFU << DMAC_BASEADDR_BASEADDR_Pos)    /**< (DMAC_BASEADDR) Descriptor Memory Base Address Mask */
#define DMAC_BASEADDR_BASEADDR(value)         (DMAC_BASEADDR_BASEADDR_Msk & ((value) << DMAC_BASEADDR_BASEADDR_Pos))
#define DMAC_BASEADDR_Msk                     (0xFFFFFFFFUL)                                 /**< (DMAC_BASEADDR) Register Mask  */

/* -------- DMAC_WRBADDR : (DMAC Offset: 0x38) (R/W 32) Write-Back Memory Section Base Address -------- */
#define DMAC_WRBADDR_WRBADDR_Pos              (0U)                                           /**< (DMAC_WRBADDR) Write-Back Memory Base Address Position */
#define DMAC_WRBADDR_WRBADDR_Msk              (0xFFFFFFFFU << DMAC_WRBADDR_WRBADDR_Pos)      /**< (DMAC_WRBADDR) Write-Back Memory Base Address Mask */
#define DMAC_WRBADDR_WRBADDR(value)           (DMAC_WRBADDR_WRBADDR_Msk & ((value) << DMAC_WRBADDR_WRBADDR_Pos))
#define DMAC_WRBADDR_Msk                      (0xFFFFFFFFUL)                                 /**< (DMAC_WRBADDR) Register Mask  */

/* -------- DMAC_CHID : (DMAC Offset: 0x3F) (R/W 8) Channel ID -------- */
#define DMAC_CHID_ID_Pos                      (0U)                                           /**< (DMAC_CHID) Channel ID Position */
#define DMAC_CHID_ID_Msk                      (0xFU << DMAC_CHID_ID_Pos)                     /**< (DMAC_CHID) Channel ID Mask */
#define DMAC_CHID_ID(value)                   (DMAC_CHID_ID_Msk & ((value) << DMAC_CHID_ID_Pos))
#define DMAC_CHID_Msk                         (0x0000000FUL)                                 /**< (DMAC_CHID) Register Mask  */

/* -------- DMAC_CHCTRLA : (DMAC Offset: 0x40) (R/W 8) Channel Control A -------- */
#define DMAC_CHCTRLA_SWRST_Pos                (0U)                                           /**< (DMAC_CHCTRLA) Channel Software Reset Position */
#define DMAC_CHCTRLA_SWRST_Msk                (0x1U << DMAC_CHCTRLA_SWRST_Pos)               /**< (DMAC_CHCTRLA) Channel Software Reset Mask */
#define DMAC_CHCTRLA_SWRST(value)             (DMAC_CHCTRLA_SWRST_Msk & ((value) << DMAC_CHCTRLA_SWRST_Pos))
#define DMAC_CHCTRLA_ENABLE_Pos               (1U)                                           /**< (DMAC_CHCTRLA) Channel Enable Position */
#define DMAC_CHCTRLA_ENABLE_Msk               (0x1U << DMAC_CHCTRLA_ENABLE_Pos)              /**< (DMAC_CHCTRLA) Channel Enable Mask */
#define DMAC_CHCTRLA_ENABLE(value)            (DMAC_CHCTRLA_ENABLE_Msk & ((value) << DMAC_CHCTRLA_ENABLE_Pos))
#define DMAC_CHCTRLA_RUNSTDBY_Pos             (6U)                                           /**< (DMAC_CHCTRLA) Channel run in standby Position */
#define DMAC_CHCTRLA_RUNSTDBY_Msk             (0x1U << DMAC_CHCTRLA_RUNSTDBY_Pos)            /**< (DMAC_CHCTRLA) Channel run in standby Mask */
#define DMAC_CHCTRLA_RUNSTDBY(value)          (DMAC_CHCTRLA_RUNSTDBY_Msk & ((value) << DMAC_CHCTRLA_RUNSTDBY_Pos))
#define DMAC_CHCTRLA_Msk                      (0x00000043UL)                                 /**< (DMAC_CHCTRLA) Register Mask  */

/* -------- DMAC_CHCTRLB : (DMAC Offset: 0x44) (R/W 32) Channel Control B -------- */
#define DMAC_CHCTRLB_EVACT_Pos                (0U)                                           /**< (DMAC_CHCTRLB) Event Input Action Position */
#define DMAC_CHCTRLB_EVACT_Msk                (0x7U << DMAC_CHCTRLB_EVACT_Pos)               /**< (DMAC_CHCTRLB) Event Input Action Mask */
#define DMAC_CHCTRLB_EVACT(value)             (DMAC_CHCTRLB_EVACT_Msk & ((value) << DMAC_CHCTRLB_EVACT_Pos))
#define   DMAC_CHCTRLB_EVACT_NOACT_Val        (0U)                                           /**< (DMAC_CHCTRLB) No action  */
#define   DMAC_CHCTRLB_EVACT_TRIG_Val         (1U)                                           /**< (DMAC_CHCTRLB) Transfer and periodic transfer trigger  */
#define   DMAC_CHCTRLB_EVACT_CTRIG_Val        (2U)                                           /**< (DMAC_CHCTRLB) Conditional transfer trigger  */
#define   DMAC_CHCTRLB_EVACT_CBLOCK_Val       (3U)                                           /**< (DMAC_CHCTRLB) Conditional block transfer  */
#define   DMAC_CHCTRLB_EVACT_SUSPEND_Val      (4U)                                           /**< (DMAC_CHCTRLB) Channel suspend operation  */
#define   DMAC_CHCTRLB_EVACT_RESUME_Val       (5U)                                           /**< (DMAC_CHCTRLB) Channel resume operation  */
#define   DMAC_CHCTRLB_EVACT_SSKIP_Val        (6U)                                           /**< (DMAC_CHCTRLB) Skip next block suspend action  */
#define DMAC_CHCTRLB_EVACT_NOACT              (DMAC_CHCTRLB_EVACT_NOACT_Val << DMAC_CHCTRLB_EVACT_Pos) /**< (DMAC_CHCTRLB) No action Position  */
#define DMAC_CHCTRLB_EVACT_TRIG               (DMAC_CHCTRLB_EVACT_TRIG_Val << DMAC_CHCTRLB_EVACT_Pos) /**< (DMAC_CHCTRLB) Transfer and periodic transfer trigger Position  */
#define DMAC_CHCTRLB_EVACT_CTRIG              (DMAC_CHCTRLB_EVACT_CTRIG_Val << DMAC_CHCTRLB_EVACT_Pos) /**< (DMAC_CHCTRLB) Conditional transfer trigger Position  */
#define DMAC_CHCTRLB_EVACT_CBLOCK             (DMAC_CHCTRLB_EVACT_CBLOCK_Val << DMAC_CHCTRLB_EVACT_Pos) /**< (DMAC_CHCTRLB) Conditional block transfer Position  */
#define DMAC_CHCTRLB_EVACT_SUSPEND            (DMAC_CHCTRLB_EVACT_SUSPEND_Val << DMAC_CHCTRLB_EVACT_Pos) /**< (DMAC_CHCTRLB) Channel suspend operation Position  */
#define DMAC_CHCTRLB_EVACT_RESUME             (DMAC_CHCTRLB_EVACT_RESUME_Val << DMAC_CHCTRLB_EVACT_Pos) /**< (DMAC_CHCTRLB) Channel resume operation Position  */
#define DMAC_CHCTRLB_EVACT_SSKIP              (DMAC_CHCTRLB_EVACT_SSKIP_Val << DMAC_CHCTRLB_EVACT_Pos) /**< (DMAC_CHCTRLB) Skip next block suspend action Position  */
#define DMAC_CHCTRLB_EVIE_Pos                 (3U)                                           /**< (DMAC_CHCTRLB) Channel Event Input Enable Position */
#define DMAC_CHCTRLB_EVIE_Msk                 (0x1U << DMAC_CHCTRLB_EVIE_Pos)                /**< (DMAC_CHCTRLB) Channel Event Input Enable Mask */
#define DMAC_CHCTRLB_EVIE(value)              (DMAC_CHCTRLB_EVIE_Msk & ((value) << DMAC_CHCTRLB_EVIE_Pos))
#define DMAC_CHCTRLB_EVOE_Pos                 (4U)                                           /**< (DMAC_CHCTRLB) Channel Event Output Enable Position */
#define DMAC_CHCTRLB_EVOE_Msk                 (0x1U << DMAC_CHCTRLB_EVOE_Pos)                /**< (DMAC_CHCTRLB) Channel Event Output Enable Mask */
#define DMAC_CHCTRLB_EVOE(value)              (DMAC_CHCTRLB_EVOE_Msk & ((value) << DMAC_CHCTRLB_EVOE_Pos))
#define DMAC_CHCTRLB_LVL_Pos                  (5U)                                           /**< (DMAC_CHCTRLB) Channel Arbitration Level Position */
#define DMAC_CHCTRLB_LVL_Msk                  (0x3U << DMAC_CHCTRLB_LVL_Pos)                 /**< (DMAC_CHCTRLB) Channel Arbitration Level Mask */
#define DMAC_CHCTRLB_LVL(value)               (DMAC_CHCTRLB_LVL_Msk & ((value) << DMAC_CHCTRLB_LVL_Pos))
#define   DMAC_CHCTRLB_LVL_LVL0_Val           (0U)                                           /**< (DMAC_CHCTRLB) Channel Priority Level 0  */
#define   DMAC_CHCTRLB_LVL_LVL1_Val           (1U)                                           /**< (DMAC_CHCTRLB) Channel Priority Level 1  */
#define   DMAC_CHCTRLB_LVL_LVL2_Val           (2U)                                           /**< (DMAC_CHCTRLB) Channel Priority Level 2  */
#define   DMAC_CHCTRLB_LVL_LVL3_Val           (3U)                                           /**< (DMAC_CHCTRLB) Channel Priority Level 3  */
#define DMAC_CHCTRLB_LVL_LVL0                 (DMAC_CHCTRLB_LVL_LVL0_Val << DMAC_CHCTRLB_LVL_Pos) /**< (DMAC_CHCTRLB) Channel Priority Level 0 Position  */
#define DMAC_CHCTRLB_LVL_LVL1                 (DMAC_CHCTRLB_LVL_LVL1_Val << DMAC_CHCTRLB_LVL_Pos) /**< (DMAC_CHCTRLB) Channel Priority Level 1 Position  */
#define DMAC_CHCTRLB_LVL_LVL2                 (DMAC_CHCTRLB_LVL_LVL2_Val << DMAC_CHCTRLB_LVL_Pos) /**< (DMAC_CHCTRLB) Channel Priority Level 2 Position  */
#define DMAC_CHCTRLB_LVL_LVL3                 (DMAC_CHCTRLB_LVL_LVL3_Val << DMAC_CHCTRLB_LVL_Pos) /**< (DMAC_CHCTRLB) Channel Priority Level 3 Position  */
#define DMAC_CHCTRLB_TRIGSRC_Pos              (8U)                                           /**< (DMAC_CHCTRLB) Trigger Source Position */
#define DMAC_CHCTRLB_TRIGSRC_Msk              (0x3FU << DMAC_CHCTRLB_TRIGSRC_Pos)            /**< (DMAC_CHCTRLB) Trigger Source Mask */
#define DMAC_CHCTRLB_TRIGSRC(value)           (DMAC_CHCTRLB_TRIGSRC_Msk & ((value) << DMAC_CHCTRLB_TRIGSRC_Pos))
#define   DMAC_CHCTRLB_TRIGSRC_DISABLE_Val    (0U)                                           /**< (DMAC_CHCTRLB) Only software/event triggers  */
#define   DMAC_CHCTRLB_TRIGSRC_TSENS_Val      (1U)                                           /**< (DMAC_CHCTRLB) TSENS Result Ready Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM0_RX_Val (2U)                                           /**< (DMAC_CHCTRLB) SERCOM0 RX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM0_TX_Val (3U)                                           /**< (DMAC_CHCTRLB) SERCOM0 TX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM1_RX_Val (4U)                                           /**< (DMAC_CHCTRLB) SERCOM1 RX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM1_TX_Val (5U)                                           /**< (DMAC_CHCTRLB) SERCOM1 TX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM2_RX_Val (6U)                                           /**< (DMAC_CHCTRLB) SERCOM2 RX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM2_TX_Val (7U)                                           /**< (DMAC_CHCTRLB) SERCOM2 TX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM3_RX_Val (8U)                                           /**< (DMAC_CHCTRLB) SERCOM3 RX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM3_TX_Val (9U)                                           /**< (DMAC_CHCTRLB) SERCOM3 TX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM4_RX_Val (10U)                                          /**< (DMAC_CHCTRLB) SERCOM4 RX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM4_TX_Val (11U)                                          /**< (DMAC_CHCTRLB) SERCOM4 TX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM5_RX_Val (12U)                                          /**< (DMAC_CHCTRLB) SERCOM5 RX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM5_TX_Val (13U)                                          /**< (DMAC_CHCTRLB) SERCOM5 TX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_CAN0_DEBUG_Val (14U)                                          /**< (DMAC_CHCTRLB) CAN0 Debug Trigger Reserved  */
#define   DMAC_CHCTRLB_TRIGSRC_CAN1_DEBUG_Val (15U)                                          /**< (DMAC_CHCTRLB) CAN1 Debug Trigger Reserved  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC0_OVF_Val   (16U)                                          /**< (DMAC_CHCTRLB) TCC0 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC0_MC0_Val   (17U)                                          /**< (DMAC_CHCTRLB) TCC0 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC0_MC1_Val   (18U)                                          /**< (DMAC_CHCTRLB) TCC0 Match/Compare 1 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC0_MC2_Val   (19U)                                          /**< (DMAC_CHCTRLB) TCC0 Match/Compare 2 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC0_MC3_Val   (20U)                                          /**< (DMAC_CHCTRLB) TCC0 Match/Compare 3 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC1_OVF_Val   (21U)                                          /**< (DMAC_CHCTRLB) TCC1 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC1_MC0_Val   (22U)                                          /**< (DMAC_CHCTRLB) TCC1 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC1_MC1_Val   (23U)                                          /**< (DMAC_CHCTRLB) TCC1 Match/Compare 1 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC2_OVF_Val   (24U)                                          /**< (DMAC_CHCTRLB) TCC2 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC2_MC0_Val   (25U)                                          /**< (DMAC_CHCTRLB) TCC2 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TCC2_MC1_Val   (26U)                                          /**< (DMAC_CHCTRLB) TCC2 Match/Compare 1 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC0_OVF_Val    (27U)                                          /**< (DMAC_CHCTRLB) TC0 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC0_MC0_Val    (28U)                                          /**< (DMAC_CHCTRLB) TC0 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC0_MC1_Val    (29U)                                          /**< (DMAC_CHCTRLB) TC0 Match/Compare 1 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC1_OVF_Val    (30U)                                          /**< (DMAC_CHCTRLB) TC1 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC1_MC0_Val    (31U)                                          /**< (DMAC_CHCTRLB) TC1 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC1_MC1_Val    (32U)                                          /**< (DMAC_CHCTRLB) TC1 Match/Compare 1 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC2_OVF_Val    (33U)                                          /**< (DMAC_CHCTRLB) TC2 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC2_MC0_Val    (34U)                                          /**< (DMAC_CHCTRLB) TC2 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC2_MC1_Val    (35U)                                          /**< (DMAC_CHCTRLB) TC2 Match/Compare 1 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC3_OVF_Val    (36U)                                          /**< (DMAC_CHCTRLB) TC3 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC3_MC0_Val    (37U)                                          /**< (DMAC_CHCTRLB) TC3 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC3_MC1_Val    (38U)                                          /**< (DMAC_CHCTRLB) TC3 Match/Compare 1 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC4_OVF_Val    (39U)                                          /**< (DMAC_CHCTRLB) TC4 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC4_MC0_Val    (40U)                                          /**< (DMAC_CHCTRLB) TC4 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC4_MC1_Val    (41U)                                          /**< (DMAC_CHCTRLB) TC4 Match/Compare 1 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_ADC0_RESRDY_Val (42U)                                          /**< (DMAC_CHCTRLB) ADC0 Result Ready Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_ADC1_RESRDY_Val (43U)                                          /**< (DMAC_CHCTRLB) ADC1 Result Ready Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SDADC_RESRDY_Val (44U)                                          /**< (DMAC_CHCTRLB) SDADC Result Ready Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_DAC_EMPTY_Val  (45U)                                          /**< (DMAC_CHCTRLB) DAC Empty Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_PTC_EOC_Val    (46U)                                          /**< (DMAC_CHCTRLB) PTC End of Conversion Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_PTC_WCOMP_Val  (47U)                                          /**< (DMAC_CHCTRLB) PTC Window Compare Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_PTC_SEQ_Val    (48U)                                          /**< (DMAC_CHCTRLB) PTC Sequence Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM6_RX_Val (49U)                                          /**< (DMAC_CHCTRLB) SERCOM6 RX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM6_TX_Val (50U)                                          /**< (DMAC_CHCTRLB) SERCOM6 TX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM7_RX_Val (51U)                                          /**< (DMAC_CHCTRLB) SERCOM7 RX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_SERCOM7_TX_Val (52U)                                          /**< (DMAC_CHCTRLB) SERCOM7 TX Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC5_OVF_Val    (53U)                                          /**< (DMAC_CHCTRLB) TC5 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC5_MC0_Val    (54U)                                          /**< (DMAC_CHCTRLB) TC5 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC5_MC1_Val    (55U)                                          /**< (DMAC_CHCTRLB) TC5 Match/Compare 1 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC6_OVF_Val    (56U)                                          /**< (DMAC_CHCTRLB) TC6 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC6_MC0_Val    (57U)                                          /**< (DMAC_CHCTRLB) TC6 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC6_MC1_Val    (58U)                                          /**< (DMAC_CHCTRLB) TC6 Match/Compare 1 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC7_OVF_Val    (59U)                                          /**< (DMAC_CHCTRLB) TC7 Overflow Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC7_MC0_Val    (60U)                                          /**< (DMAC_CHCTRLB) TC7 Match/Compare 0 Trigger  */
#define   DMAC_CHCTRLB_TRIGSRC_TC7_MC1_Val    (61U)                                          /**< (DMAC_CHCTRLB) TC7 Match/Compare 1 Trigger  */
#define DMAC_CHCTRLB_TRIGSRC_DISABLE          (DMAC_CHCTRLB_TRIGSRC_DISABLE_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) Only software/event triggers Position  */
#define DMAC_CHCTRLB_TRIGSRC_TSENS            (DMAC_CHCTRLB_TRIGSRC_TSENS_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TSENS Result Ready Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM0_RX       (DMAC_CHCTRLB_TRIGSRC_SERCOM0_RX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM0 RX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM0_TX       (DMAC_CHCTRLB_TRIGSRC_SERCOM0_TX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM0 TX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM1_RX       (DMAC_CHCTRLB_TRIGSRC_SERCOM1_RX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM1 RX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM1_TX       (DMAC_CHCTRLB_TRIGSRC_SERCOM1_TX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM1 TX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM2_RX       (DMAC_CHCTRLB_TRIGSRC_SERCOM2_RX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM2 RX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM2_TX       (DMAC_CHCTRLB_TRIGSRC_SERCOM2_TX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM2 TX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM3_RX       (DMAC_CHCTRLB_TRIGSRC_SERCOM3_RX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM3 RX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM3_TX       (DMAC_CHCTRLB_TRIGSRC_SERCOM3_TX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM3 TX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM4_RX       (DMAC_CHCTRLB_TRIGSRC_SERCOM4_RX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM4 RX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM4_TX       (DMAC_CHCTRLB_TRIGSRC_SERCOM4_TX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM4 TX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM5_RX       (DMAC_CHCTRLB_TRIGSRC_SERCOM5_RX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM5 RX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM5_TX       (DMAC_CHCTRLB_TRIGSRC_SERCOM5_TX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM5 TX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_CAN0_DEBUG       (DMAC_CHCTRLB_TRIGSRC_CAN0_DEBUG_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) CAN0 Debug Trigger Reserved Position  */
#define DMAC_CHCTRLB_TRIGSRC_CAN1_DEBUG       (DMAC_CHCTRLB_TRIGSRC_CAN1_DEBUG_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) CAN1 Debug Trigger Reserved Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC0_OVF         (DMAC_CHCTRLB_TRIGSRC_TCC0_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC0 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC0_MC0         (DMAC_CHCTRLB_TRIGSRC_TCC0_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC0 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC0_MC1         (DMAC_CHCTRLB_TRIGSRC_TCC0_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC0 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC0_MC2         (DMAC_CHCTRLB_TRIGSRC_TCC0_MC2_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC0 Match/Compare 2 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC0_MC3         (DMAC_CHCTRLB_TRIGSRC_TCC0_MC3_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC0 Match/Compare 3 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC1_OVF         (DMAC_CHCTRLB_TRIGSRC_TCC1_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC1 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC1_MC0         (DMAC_CHCTRLB_TRIGSRC_TCC1_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC1 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC1_MC1         (DMAC_CHCTRLB_TRIGSRC_TCC1_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC1 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC2_OVF         (DMAC_CHCTRLB_TRIGSRC_TCC2_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC2 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC2_MC0         (DMAC_CHCTRLB_TRIGSRC_TCC2_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC2 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TCC2_MC1         (DMAC_CHCTRLB_TRIGSRC_TCC2_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TCC2 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC0_OVF          (DMAC_CHCTRLB_TRIGSRC_TC0_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC0 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC0_MC0          (DMAC_CHCTRLB_TRIGSRC_TC0_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC0 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC0_MC1          (DMAC_CHCTRLB_TRIGSRC_TC0_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC0 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC1_OVF          (DMAC_CHCTRLB_TRIGSRC_TC1_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC1 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC1_MC0          (DMAC_CHCTRLB_TRIGSRC_TC1_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC1 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC1_MC1          (DMAC_CHCTRLB_TRIGSRC_TC1_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC1 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC2_OVF          (DMAC_CHCTRLB_TRIGSRC_TC2_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC2 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC2_MC0          (DMAC_CHCTRLB_TRIGSRC_TC2_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC2 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC2_MC1          (DMAC_CHCTRLB_TRIGSRC_TC2_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC2 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC3_OVF          (DMAC_CHCTRLB_TRIGSRC_TC3_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC3 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC3_MC0          (DMAC_CHCTRLB_TRIGSRC_TC3_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC3 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC3_MC1          (DMAC_CHCTRLB_TRIGSRC_TC3_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC3 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC4_OVF          (DMAC_CHCTRLB_TRIGSRC_TC4_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC4 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC4_MC0          (DMAC_CHCTRLB_TRIGSRC_TC4_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC4 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC4_MC1          (DMAC_CHCTRLB_TRIGSRC_TC4_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC4 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_ADC0_RESRDY      (DMAC_CHCTRLB_TRIGSRC_ADC0_RESRDY_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) ADC0 Result Ready Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_ADC1_RESRDY      (DMAC_CHCTRLB_TRIGSRC_ADC1_RESRDY_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) ADC1 Result Ready Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SDADC_RESRDY     (DMAC_CHCTRLB_TRIGSRC_SDADC_RESRDY_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SDADC Result Ready Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_DAC_EMPTY        (DMAC_CHCTRLB_TRIGSRC_DAC_EMPTY_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) DAC Empty Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_PTC_EOC          (DMAC_CHCTRLB_TRIGSRC_PTC_EOC_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) PTC End of Conversion Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_PTC_WCOMP        (DMAC_CHCTRLB_TRIGSRC_PTC_WCOMP_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) PTC Window Compare Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_PTC_SEQ          (DMAC_CHCTRLB_TRIGSRC_PTC_SEQ_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) PTC Sequence Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM6_RX       (DMAC_CHCTRLB_TRIGSRC_SERCOM6_RX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM6 RX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM6_TX       (DMAC_CHCTRLB_TRIGSRC_SERCOM6_TX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM6 TX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM7_RX       (DMAC_CHCTRLB_TRIGSRC_SERCOM7_RX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM7 RX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_SERCOM7_TX       (DMAC_CHCTRLB_TRIGSRC_SERCOM7_TX_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) SERCOM7 TX Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC5_OVF          (DMAC_CHCTRLB_TRIGSRC_TC5_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC5 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC5_MC0          (DMAC_CHCTRLB_TRIGSRC_TC5_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC5 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC5_MC1          (DMAC_CHCTRLB_TRIGSRC_TC5_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC5 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC6_OVF          (DMAC_CHCTRLB_TRIGSRC_TC6_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC6 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC6_MC0          (DMAC_CHCTRLB_TRIGSRC_TC6_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC6 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC6_MC1          (DMAC_CHCTRLB_TRIGSRC_TC6_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC6 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC7_OVF          (DMAC_CHCTRLB_TRIGSRC_TC7_OVF_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC7 Overflow Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC7_MC0          (DMAC_CHCTRLB_TRIGSRC_TC7_MC0_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC7 Match/Compare 0 Trigger Position  */
#define DMAC_CHCTRLB_TRIGSRC_TC7_MC1          (DMAC_CHCTRLB_TRIGSRC_TC7_MC1_Val << DMAC_CHCTRLB_TRIGSRC_Pos) /**< (DMAC_CHCTRLB) TC7 Match/Compare 1 Trigger Position  */
#define DMAC_CHCTRLB_TRIGACT_Pos              (22U)                                          /**< (DMAC_CHCTRLB) Trigger Action Position */
#define DMAC_CHCTRLB_TRIGACT_Msk              (0x3U << DMAC_CHCTRLB_TRIGACT_Pos)             /**< (DMAC_CHCTRLB) Trigger Action Mask */
#define DMAC_CHCTRLB_TRIGACT(value)           (DMAC_CHCTRLB_TRIGACT_Msk & ((value) << DMAC_CHCTRLB_TRIGACT_Pos))
#define   DMAC_CHCTRLB_TRIGACT_BLOCK_Val      (0U)                                           /**< (DMAC_CHCTRLB) One trigger required for each block transfer  */
#define   DMAC_CHCTRLB_TRIGACT_BEAT_Val       (2U)                                           /**< (DMAC_CHCTRLB) One trigger required for each beat transfer  */
#define   DMAC_CHCTRLB_TRIGACT_TRANSACTION_Val (3U)                                           /**< (DMAC_CHCTRLB) One trigger required for each transaction  */
#define DMAC_CHCTRLB_TRIGACT_BLOCK            (DMAC_CHCTRLB_TRIGACT_BLOCK_Val << DMAC_CHCTRLB_TRIGACT_Pos) /**< (DMAC_CHCTRLB) One trigger required for each block transfer Position  */
#define DMAC_CHCTRLB_TRIGACT_BEAT             (DMAC_CHCTRLB_TRIGACT_BEAT_Val << DMAC_CHCTRLB_TRIGACT_Pos) /**< (DMAC_CHCTRLB) One trigger required for each beat transfer Position  */
#define DMAC_CHCTRLB_TRIGACT_TRANSACTION      (DMAC_CHCTRLB_TRIGACT_TRANSACTION_Val << DMAC_CHCTRLB_TRIGACT_Pos) /**< (DMAC_CHCTRLB) One trigger required for each transaction Position  */
#define DMAC_CHCTRLB_CMD_Pos                  (24U)                                          /**< (DMAC_CHCTRLB) Software Command Position */
#define DMAC_CHCTRLB_CMD_Msk                  (0x3U << DMAC_CHCTRLB_CMD_Pos)                 /**< (DMAC_CHCTRLB) Software Command Mask */
#define DMAC_CHCTRLB_CMD(value)               (DMAC_CHCTRLB_CMD_Msk & ((value) << DMAC_CHCTRLB_CMD_Pos))
#define   DMAC_CHCTRLB_CMD_NOACT_Val          (0U)                                           /**< (DMAC_CHCTRLB) No action  */
#define   DMAC_CHCTRLB_CMD_SUSPEND_Val        (1U)                                           /**< (DMAC_CHCTRLB) Channel suspend operation  */
#define   DMAC_CHCTRLB_CMD_RESUME_Val         (2U)                                           /**< (DMAC_CHCTRLB) Channel resume operation  */
#define DMAC_CHCTRLB_CMD_NOACT                (DMAC_CHCTRLB_CMD_NOACT_Val << DMAC_CHCTRLB_CMD_Pos) /**< (DMAC_CHCTRLB) No action Position  */
#define DMAC_CHCTRLB_CMD_SUSPEND              (DMAC_CHCTRLB_CMD_SUSPEND_Val << DMAC_CHCTRLB_CMD_Pos) /**< (DMAC_CHCTRLB) Channel suspend operation Position  */
#define DMAC_CHCTRLB_CMD_RESUME               (DMAC_CHCTRLB_CMD_RESUME_Val << DMAC_CHCTRLB_CMD_Pos) /**< (DMAC_CHCTRLB) Channel resume operation Position  */
#define DMAC_CHCTRLB_Msk                      (0x03C03F7FUL)                                 /**< (DMAC_CHCTRLB) Register Mask  */

/* -------- DMAC_CHINTENCLR : (DMAC Offset: 0x4C) (R/W 8) Channel Interrupt Enable Clear -------- */
#define DMAC_CHINTENCLR_TERR_Pos              (0U)                                           /**< (DMAC_CHINTENCLR) Channel Transfer Error Interrupt Enable Position */
#define DMAC_CHINTENCLR_TERR_Msk              (0x1U << DMAC_CHINTENCLR_TERR_Pos)             /**< (DMAC_CHINTENCLR) Channel Transfer Error Interrupt Enable Mask */
#define DMAC_CHINTENCLR_TERR(value)           (DMAC_CHINTENCLR_TERR_Msk & ((value) << DMAC_CHINTENCLR_TERR_Pos))
#define DMAC_CHINTENCLR_TCMPL_Pos             (1U)                                           /**< (DMAC_CHINTENCLR) Channel Transfer Complete Interrupt Enable Position */
#define DMAC_CHINTENCLR_TCMPL_Msk             (0x1U << DMAC_CHINTENCLR_TCMPL_Pos)            /**< (DMAC_CHINTENCLR) Channel Transfer Complete Interrupt Enable Mask */
#define DMAC_CHINTENCLR_TCMPL(value)          (DMAC_CHINTENCLR_TCMPL_Msk & ((value) << DMAC_CHINTENCLR_TCMPL_Pos))
#define DMAC_CHINTENCLR_SUSP_Pos              (2U)                                           /**< (DMAC_CHINTENCLR) Channel Suspend Interrupt Enable Position */
#define DMAC_CHINTENCLR_SUSP_Msk              (0x1U << DMAC_CHINTENCLR_SUSP_Pos)             /**< (DMAC_CHINTENCLR) Channel Suspend Interrupt Enable Mask */
#define DMAC_CHINTENCLR_SUSP(value)           (DMAC_CHINTENCLR_SUSP_Msk & ((value) << DMAC_CHINTENCLR_SUSP_Pos))
#define DMAC_CHINTENCLR_Msk                   (0x00000007UL)                                 /**< (DMAC_CHINTENCLR) Register Mask  */

/* -------- DMAC_CHINTENSET : (DMAC Offset: 0x4D) (R/W 8) Channel Interrupt Enable Set -------- */
#define DMAC_CHINTENSET_TERR_Pos              (0U)                                           /**< (DMAC_CHINTENSET) Channel Transfer Error Interrupt Enable Position */
#define DMAC_CHINTENSET_TERR_Msk              (0x1U << DMAC_CHINTENSET_TERR_Pos)             /**< (DMAC_CHINTENSET) Channel Transfer Error Interrupt Enable Mask */
#define DMAC_CHINTENSET_TERR(value)           (DMAC_CHINTENSET_TERR_Msk & ((value) << DMAC_CHINTENSET_TERR_Pos))
#define DMAC_CHINTENSET_TCMPL_Pos             (1U)                                           /**< (DMAC_CHINTENSET) Channel Transfer Complete Interrupt Enable Position */
#define DMAC_CHINTENSET_TCMPL_Msk             (0x1U << DMAC_CHINTENSET_TCMPL_Pos)            /**< (DMAC_CHINTENSET) Channel Transfer Complete Interrupt Enable Mask */
#define DMAC_CHINTENSET_TCMPL(value)          (DMAC_CHINTENSET_TCMPL_Msk & ((value) << DMAC_CHINTENSET_TCMPL_Pos))
#define DMAC_CHINTENSET_SUSP_Pos              (2U)                                           /**< (DMAC_CHINTENSET) Channel Suspend Interrupt Enable Position */
#define DMAC_CHINTENSET_SUSP_Msk              (0x1U << DMAC_CHINTENSET_SUSP_Pos)             /**< (DMAC_CHINTENSET) Channel Suspend Interrupt Enable Mask */
#define DMAC_CHINTENSET_SUSP(value)           (DMAC_CHINTENSET_SUSP_Msk & ((value) << DMAC_CHINTENSET_SUSP_Pos))
#define DMAC_CHINTENSET_Msk                   (0x00000007UL)                                 /**< (DMAC_CHINTENSET) Register Mask  */

/* -------- DMAC_CHINTFLAG : (DMAC Offset: 0x4E) (R/W 8) Channel Interrupt Flag Status and Clear -------- */
#define DMAC_CHINTFLAG_TERR_Pos               (0U)                                           /**< (DMAC_CHINTFLAG) Channel Transfer Error Position */
#define DMAC_CHINTFLAG_TERR_Msk               (0x1U << DMAC_CHINTFLAG_TERR_Pos)              /**< (DMAC_CHINTFLAG) Channel Transfer Error Mask */
#define DMAC_CHINTFLAG_TERR(value)            (DMAC_CHINTFLAG_TERR_Msk & ((value) << DMAC_CHINTFLAG_TERR_Pos))
#define DMAC_CHINTFLAG_TCMPL_Pos              (1U)                                           /**< (DMAC_CHINTFLAG) Channel Transfer Complete Position */
#define DMAC_CHINTFLAG_TCMPL_Msk              (0x1U << DMAC_CHINTFLAG_TCMPL_Pos)             /**< (DMAC_CHINTFLAG) Channel Transfer Complete Mask */
#define DMAC_CHINTFLAG_TCMPL(value)           (DMAC_CHINTFLAG_TCMPL_Msk & ((value) << DMAC_CHINTFLAG_TCMPL_Pos))
#define DMAC_CHINTFLAG_SUSP_Pos               (2U)                                           /**< (DMAC_CHINTFLAG) Channel Suspend Position */
#define DMAC_CHINTFLAG_SUSP_Msk               (0x1U << DMAC_CHINTFLAG_SUSP_Pos)              /**< (DMAC_CHINTFLAG) Channel Suspend Mask */
#define DMAC_CHINTFLAG_SUSP(value)            (DMAC_CHINTFLAG_SUSP_Msk & ((value) << DMAC_CHINTFLAG_SUSP_Pos))
#define DMAC_CHINTFLAG_Msk                    (0x00000007UL)                                 /**< (DMAC_CHINTFLAG) Register Mask  */

/* -------- DMAC_CHSTATUS : (DMAC Offset: 0x4F) (R/  8) Channel Status -------- */
#define DMAC_CHSTATUS_PEND_Pos                (0U)                                           /**< (DMAC_CHSTATUS) Channel Pending Position */
#define DMAC_CHSTATUS_PEND_Msk                (0x1U << DMAC_CHSTATUS_PEND_Pos)               /**< (DMAC_CHSTATUS) Channel Pending Mask */
#define DMAC_CHSTATUS_PEND(value)             (DMAC_CHSTATUS_PEND_Msk & ((value) << DMAC_CHSTATUS_PEND_Pos))
#define DMAC_CHSTATUS_BUSY_Pos                (1U)                                           /**< (DMAC_CHSTATUS) Channel Busy Position */
#define DMAC_CHSTATUS_BUSY_Msk                (0x1U << DMAC_CHSTATUS_BUSY_Pos)               /**< (DMAC_CHSTATUS) Channel Busy Mask */
#define DMAC_CHSTATUS_BUSY(value)             (DMAC_CHSTATUS_BUSY_Msk & ((value) << DMAC_CHSTATUS_BUSY_Pos))
#define DMAC_CHSTATUS_FERR_Pos                (2U)                                           /**< (DMAC_CHSTATUS) Channel Fetch Error Position */
#define DMAC_CHSTATUS_FERR_Msk                (0x1U << DMAC_CHSTATUS_FERR_Pos)               /**< (DMAC_CHSTATUS) Channel Fetch Error Mask */
#define DMAC_CHSTATUS_FERR(value)             (DMAC_CHSTATUS_FERR_Msk & ((value) << DMAC_CHSTATUS_FERR_Pos))
#define DMAC_CHSTATUS_Msk                     (0x00000007UL)                                 /**< (DMAC_CHSTATUS) Register Mask  */

/** \brief DMAC register offsets definitions */
#define DMAC_CTRL_OFFSET               (0x00)         /**< (DMAC_CTRL) Control Offset */
#define DMAC_CRCCTRL_OFFSET            (0x02)         /**< (DMAC_CRCCTRL) CRC Control Offset */
#define DMAC_CRCDATAIN_OFFSET          (0x04)         /**< (DMAC_CRCDATAIN) CRC Data Input Offset */
#define DMAC_CRCCHKSUM_OFFSET          (0x08)         /**< (DMAC_CRCCHKSUM) CRC Checksum Offset */
#define DMAC_CRCSTATUS_OFFSET          (0x0C)         /**< (DMAC_CRCSTATUS) CRC Status Offset */
#define DMAC_DBGCTRL_OFFSET            (0x0D)         /**< (DMAC_DBGCTRL) Debug Control Offset */
#define DMAC_SWTRIGCTRL_OFFSET         (0x10)         /**< (DMAC_SWTRIGCTRL) Software Trigger Control Offset */
#define DMAC_PRICTRL0_OFFSET           (0x14)         /**< (DMAC_PRICTRL0) Priority Control 0 Offset */
#define DMAC_INTPEND_OFFSET            (0x20)         /**< (DMAC_INTPEND) Interrupt Pending Offset */
#define DMAC_INTSTATUS_OFFSET          (0x24)         /**< (DMAC_INTSTATUS) Interrupt Status Offset */
#define DMAC_BUSYCH_OFFSET             (0x28)         /**< (DMAC_BUSYCH) Busy Channels Offset */
#define DMAC_PENDCH_OFFSET             (0x2C)         /**< (DMAC_PENDCH) Pending Channels Offset */
#define DMAC_ACTIVE_OFFSET             (0x30)         /**< (DMAC_ACTIVE) Active Channel and Levels Offset */
#define DMAC_BASEADDR_OFFSET           (0x34)         /**< (DMAC_BASEADDR) Descriptor Memory Section Base Address Offset */
#define DMAC_WRBADDR_OFFSET            (0x38)         /**< (DMAC_WRBADDR) Write-Back Memory Section Base Address Offset */
#define DMAC_CHID_OFFSET               (0x3F)         /**< (DMAC_CHID) Channel ID Offset */
#define DMAC_CHCTRLA_OFFSET            (0x40)         /**< (DMAC_CHCTRLA) Channel Control A Offset */
#define DMAC_CHCTRLB_OFFSET            (0x44)         /**< (DMAC_CHCTRLB) Channel Control B Offset */
#define DMAC_CHINTENCLR_OFFSET         (0x4C)         /**< (DMAC_CHINTENCLR) Channel Interrupt Enable Clear Offset */
#define DMAC_CHINTENSET_OFFSET         (0x4D)         /**< (DMAC_CHINTENSET) Channel Interrupt Enable Set Offset */
#define DMAC_CHINTFLAG_OFFSET          (0x4E)         /**< (DMAC_CHINTFLAG) Channel Interrupt Flag Status and Clear Offset */
#define DMAC_CHSTATUS_OFFSET           (0x4F)         /**< (DMAC_CHSTATUS) Channel Status Offset */


/** \brief DMAC register API structure */
typedef struct
{
  __IO  uint16_t                       DMAC_CTRL;       /**< Offset: 0x00 (R/W  16) Control */
  __IO  uint16_t                       DMAC_CRCCTRL;    /**< Offset: 0x02 (R/W  16) CRC Control */
  __IO  uint32_t                       DMAC_CRCDATAIN;  /**< Offset: 0x04 (R/W  32) CRC Data Input */
  __IO  uint32_t                       DMAC_CRCCHKSUM;  /**< Offset: 0x08 (R/W  32) CRC Checksum */
  __IO  uint8_t                        DMAC_CRCSTATUS;  /**< Offset: 0x0c (R/W  8) CRC Status */
  __IO  uint8_t                        DMAC_DBGCTRL;    /**< Offset: 0x0d (R/W  8) Debug Control */
  __I   uint8_t                        Reserved1[0x02];
  __IO  uint32_t                       DMAC_SWTRIGCTRL; /**< Offset: 0x10 (R/W  32) Software Trigger Control */
  __IO  uint32_t                       DMAC_PRICTRL0;   /**< Offset: 0x14 (R/W  32) Priority Control 0 */
  __I   uint8_t                        Reserved2[0x08];
  __IO  uint16_t                       DMAC_INTPEND;    /**< Offset: 0x20 (R/W  16) Interrupt Pending */
  __I   uint8_t                        Reserved3[0x02];
  __I   uint32_t                       DMAC_INTSTATUS;  /**< Offset: 0x24 (R/   32) Interrupt Status */
  __I   uint32_t                       DMAC_BUSYCH;     /**< Offset: 0x28 (R/   32) Busy Channels */
  __I   uint32_t                       DMAC_PENDCH;     /**< Offset: 0x2c (R/   32) Pending Channels */
  __I   uint32_t                       DMAC_ACTIVE;     /**< Offset: 0x30 (R/   32) Active Channel and Levels */
  __IO  uint32_t                       DMAC_BASEADDR;   /**< Offset: 0x34 (R/W  32) Descriptor Memory Section Base Address */
  __IO  uint32_t                       DMAC_WRBADDR;    /**< Offset: 0x38 (R/W  32) Write-Back Memory Section Base Address */
  __I   uint8_t                        Reserved4[0x03];
  __IO  uint8_t                        DMAC_CHID;       /**< Offset: 0x3f (R/W  8) Channel ID */
  __IO  uint8_t                        DMAC_CHCTRLA;    /**< Offset: 0x40 (R/W  8) Channel Control A */
  __I   uint8_t                        Reserved5[0x03];
  __IO  uint32_t                       DMAC_CHCTRLB;    /**< Offset: 0x44 (R/W  32) Channel Control B */
  __I   uint8_t                        Reserved6[0x04];
  __IO  uint8_t                        DMAC_CHINTENCLR; /**< Offset: 0x4c (R/W  8) Channel Interrupt Enable Clear */
  __IO  uint8_t                        DMAC_CHINTENSET; /**< Offset: 0x4d (R/W  8) Channel Interrupt Enable Set */
  __IO  uint8_t                        DMAC_CHINTFLAG;  /**< Offset: 0x4e (R/W  8) Channel Interrupt Flag Status and Clear */
  __I   uint8_t                        DMAC_CHSTATUS;   /**< Offset: 0x4f (R/   8) Channel Status */
} dmac_registers_t;
/** @}  end of Direct Memory Access Controller */

/* -------- DMAC_DESCRIPTOR_BTCTRL : (DMAC Offset: 0x00) (R/W 16) Block Transfer Control -------- */
#define DMAC_DESCRIPTOR_BTCTRL_VALID_Pos      (0)                                            /**< (DMAC_DESCRIPTOR_BTCTRL) Descriptor Valid Position */
#define DMAC_DESCRIPTOR_BTCTRL_VALID_Msk      (0x1U << DMAC_DESCRIPTOR_BTCTRL_VALID_Pos)     /**< (DMAC_DESCRIPTOR_BTCTRL) Descriptor Valid Mask */
#define DMAC_DESCRIPTOR_BTCTRL_EVOSEL_Pos     (1)                                            /**< (DMAC_DESCRIPTOR_BTCTRL) Event Output Selection Position */
#define DMAC_DESCRIPTOR_BTCTRL_EVOSEL_Msk     (0x3U << DMAC_DESCRIPTOR_BTCTRL_EVOSEL_Pos)    /**< (DMAC_DESCRIPTOR_BTCTRL) Event Output Selection Mask */
#define DMAC_DESCRIPTOR_BTCTRL_EVOSEL(value)  (DMAC_DESCRIPTOR_BTCTRL_EVOSEL_Msk & ((value) << DMAC_DESCRIPTOR_BTCTRL_EVOSEL_Pos))
#define   DMAC_DESCRIPTOR_BTCTRL_EVOSEL_DISABLE_Val (0x0U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Event generation disabled  */
#define   DMAC_DESCRIPTOR_BTCTRL_EVOSEL_BLOCK_Val (0x1U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Event strobe when block transfer complete  */
#define   DMAC_DESCRIPTOR_BTCTRL_EVOSEL_BEAT_Val (0x3U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Event strobe when beat transfer complete  */
#define DMAC_DESCRIPTOR_BTCTRL_EVOSEL_DISABLE (DMAC_DESCRIPTOR_BTCTRL_EVOSEL_DISABLE_Val << DMAC_DESCRIPTOR_BTCTRL_EVOSEL_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Event generation disabled Position  */
#define DMAC_DESCRIPTOR_BTCTRL_EVOSEL_BLOCK   (DMAC_DESCRIPTOR_BTCTRL_EVOSEL_BLOCK_Val << DMAC_DESCRIPTOR_BTCTRL_EVOSEL_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Event strobe when block transfer complete Position  */
#define DMAC_DESCRIPTOR_BTCTRL_EVOSEL_BEAT    (DMAC_DESCRIPTOR_BTCTRL_EVOSEL_BEAT_Val << DMAC_DESCRIPTOR_BTCTRL_EVOSEL_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Event strobe when beat transfer complete Position  */
#define DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_Pos   (3)                                            /**< (DMAC_DESCRIPTOR_BTCTRL) Block Action Position */
#define DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_Msk   (0x3U << DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Block Action Mask */
#define DMAC_DESCRIPTOR_BTCTRL_BLOCKACT(value) (DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_Msk & ((value) << DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_Pos))
#define   DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_NOACT_Val (0x0U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Channel will be disabled if it is the last block transfer in the transaction  */
#define   DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_INT_Val (0x1U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Channel will be disabled if it is the last block transfer in the transaction and block interrupt  */
#define   DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_SUSPEND_Val (0x2U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Channel suspend operation is completed  */
#define   DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_BOTH_Val (0x3U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Both channel suspend operation and block interrupt  */
#define DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_NOACT (DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_NOACT_Val << DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Channel will be disabled if it is the last block transfer in the transaction Position  */
#define DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_INT   (DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_INT_Val << DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Channel will be disabled if it is the last block transfer in the transaction and block interrupt Position  */
#define DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_SUSPEND (DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_SUSPEND_Val << DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Channel suspend operation is completed Position  */
#define DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_BOTH  (DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_BOTH_Val << DMAC_DESCRIPTOR_BTCTRL_BLOCKACT_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Both channel suspend operation and block interrupt Position  */
#define DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Pos   (8)                                            /**< (DMAC_DESCRIPTOR_BTCTRL) Beat Size Position */
#define DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Msk   (0x3U << DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Beat Size Mask */
#define DMAC_DESCRIPTOR_BTCTRL_BEATSIZE(value) (DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Msk & ((value) << DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Pos))
#define   DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_BYTE_Val (0x0U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) 8-bit bus transfer  */
#define   DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_HWORD_Val (0x1U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) 16-bit bus transfer  */
#define   DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_WORD_Val (0x2U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) 32-bit bus transfer  */
#define DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_BYTE  (DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_BYTE_Val << DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) 8-bit bus transfer Position  */
#define DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_HWORD (DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_HWORD_Val << DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) 16-bit bus transfer Position  */
#define DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_WORD  (DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_WORD_Val << DMAC_DESCRIPTOR_BTCTRL_BEATSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) 32-bit bus transfer Position  */
#define DMAC_DESCRIPTOR_BTCTRL_SRCINC_Pos     (10)                                           /**< (DMAC_DESCRIPTOR_BTCTRL) Source Address Increment Enable Position */
#define DMAC_DESCRIPTOR_BTCTRL_SRCINC_Msk     (0x1U << DMAC_DESCRIPTOR_BTCTRL_SRCINC_Pos)    /**< (DMAC_DESCRIPTOR_BTCTRL) Source Address Increment Enable Mask */
#define DMAC_DESCRIPTOR_BTCTRL_DSTINC_Pos     (11)                                           /**< (DMAC_DESCRIPTOR_BTCTRL) Destination Address Increment Enable Position */
#define DMAC_DESCRIPTOR_BTCTRL_DSTINC_Msk     (0x1U << DMAC_DESCRIPTOR_BTCTRL_DSTINC_Pos)    /**< (DMAC_DESCRIPTOR_BTCTRL) Destination Address Increment Enable Mask */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSEL_Pos    (12)                                           /**< (DMAC_DESCRIPTOR_BTCTRL) Step Selection Position */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSEL_Msk    (0x1U << DMAC_DESCRIPTOR_BTCTRL_STEPSEL_Pos)   /**< (DMAC_DESCRIPTOR_BTCTRL) Step Selection Mask */
#define   DMAC_DESCRIPTOR_BTCTRL_STEPSEL_DST_Val (0x0U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Step size settings apply to the destination address  */
#define   DMAC_DESCRIPTOR_BTCTRL_STEPSEL_SRC_Val (0x1U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Step size settings apply to the source address  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSEL_DST    (DMAC_DESCRIPTOR_BTCTRL_STEPSEL_DST_Val << DMAC_DESCRIPTOR_BTCTRL_STEPSEL_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Step size settings apply to the destination address Position  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSEL_SRC    (DMAC_DESCRIPTOR_BTCTRL_STEPSEL_SRC_Val << DMAC_DESCRIPTOR_BTCTRL_STEPSEL_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Step size settings apply to the source address Position  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos   (13)                                           /**< (DMAC_DESCRIPTOR_BTCTRL) Address Increment Step Size Position */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Msk   (0x7U << DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Address Increment Step Size Mask */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE(value) (DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Msk & ((value) << DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos))
#define   DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X1_Val (0x0U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 1  */
#define   DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X2_Val (0x1U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 2  */
#define   DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X4_Val (0x2U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 4  */
#define   DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X8_Val (0x3U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 8  */
#define   DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X16_Val (0x4U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 16  */
#define   DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X32_Val (0x5U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 32  */
#define   DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X64_Val (0x6U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 64  */
#define   DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X128_Val (0x7U)                                         /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 128  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X1    (DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X1_Val << DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 1 Position  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X2    (DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X2_Val << DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 2 Position  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X4    (DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X4_Val << DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 4 Position  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X8    (DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X8_Val << DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 8 Position  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X16   (DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X16_Val << DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 16 Position  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X32   (DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X32_Val << DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 32 Position  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X64   (DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X64_Val << DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 64 Position  */
#define DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X128  (DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_X128_Val << DMAC_DESCRIPTOR_BTCTRL_STEPSIZE_Pos)  /**< (DMAC_DESCRIPTOR_BTCTRL) Next ADDR = ADDR + (BEATSIZE+1) * 128 Position  */
#define DMAC_DESCRIPTOR_BTCTRL_Msk            (0x0000FF1FUL)                                 /**< (DMAC_DESCRIPTOR_BTCTRL) Register Mask  */

/* -------- DMAC_DESCRIPTOR_BTCNT : (DMAC Offset: 0x02) (R/W 16) Block Transfer Count -------- */
#define DMAC_DESCRIPTOR_BTCNT_BTCNT_Pos       (0)                                            /**< (DMAC_DESCRIPTOR_BTCNT) Block Transfer Count Position */
#define DMAC_DESCRIPTOR_BTCNT_BTCNT_Msk       (0xFFFFU << DMAC_DESCRIPTOR_BTCNT_BTCNT_Pos)   /**< (DMAC_DESCRIPTOR_BTCNT) Block Transfer Count Mask */
#define DMAC_DESCRIPTOR_BTCNT_BTCNT(value)    (DMAC_DESCRIPTOR_BTCNT_BTCNT_Msk & ((value) << DMAC_DESCRIPTOR_BTCNT_BTCNT_Pos))
#define DMAC_DESCRIPTOR_BTCNT_Msk             (0x0000FFFFUL)                                 /**< (DMAC_DESCRIPTOR_BTCNT) Register Mask  */

/* -------- DMAC_DESCRIPTOR_SRCADDR : (DMAC Offset: 0x04) (R/W 32) Block Transfer Source Address -------- */
#define DMAC_DESCRIPTOR_SRCADDR_SRCADDR_Pos   (0)                                            /**< (DMAC_DESCRIPTOR_SRCADDR) Transfer Source Address Position */
#define DMAC_DESCRIPTOR_SRCADDR_SRCADDR_Msk   (0xFFFFFFFFU << DMAC_DESCRIPTOR_SRCADDR_SRCADDR_Pos)  /**< (DMAC_DESCRIPTOR_SRCADDR) Transfer Source Address Mask */
#define DMAC_DESCRIPTOR_SRCADDR_SRCADDR(value) (DMAC_DESCRIPTOR_SRCADDR_SRCADDR_Msk & ((value) << DMAC_DESCRIPTOR_SRCADDR_SRCADDR_Pos))
#define DMAC_DESCRIPTOR_SRCADDR_Msk           (0xFFFFFFFFUL)                                 /**< (DMAC_DESCRIPTOR_SRCADDR) Register Mask  */

/* -------- DMAC_DESCRIPTOR_DSTADDR : (DMAC Offset: 0x08) (R/W 32) Block Transfer Destination Address -------- */
#define DMAC_DESCRIPTOR_DSTADDR_DSTADDR_Pos   (0)                                            /**< (DMAC_DESCRIPTOR_DSTADDR) Transfer Destination Address Position */
#define DMAC_DESCRIPTOR_DSTADDR_DSTADDR_Msk   (0xFFFFFFFFU << DMAC_DESCRIPTOR_DSTADDR_DSTADDR_Pos)  /**< (DMAC_DESCRIPTOR_DSTADDR) Transfer Destination Address Mask */
#define DMAC_DESCRIPTOR_DSTADDR_DSTADDR(value) (DMAC_DESCRIPTOR_DSTADDR_DSTADDR_Msk & ((value) << DMAC_DESCRIPTOR_DSTADDR_DSTADDR_Pos))
#define DMAC_DESCRIPTOR_DSTADDR_Msk           (0xFFFFFFFFUL)                                 /**< (DMAC_DESCRIPTOR_DSTADDR) Register Mask  */

/* -------- DMAC_DESCRIPTOR_DESCADDR : (DMAC Offset: 0x0c) (R/W 32) Next Descriptor Address -------- */
#define DMAC_DESCRIPTOR_DESCADDR_DESCADDR_Pos (0)                                            /**< (DMAC_DESCRIPTOR_DESCADDR) Next Descriptor Address Position */
#define DMAC_DESCRIPTOR_DESCADDR_DESCADDR_Msk (0xFFFFFFFFU << DMAC_DESCRIPTOR_DESCADDR_DESCADDR_Pos)  /**< (DMAC_DESCRIPTOR_DESCADDR) Next Descriptor Address Mask */
#define DMAC_DESCRIPTOR_DESCADDR_DESCADDR(value) (DMAC_DESCRIPTOR_DESCADDR_DESCADDR_Msk & ((value) << DMAC_DESCRIPTOR_DESCADDR_DESCADDR_Pos))
#define DMAC_DESCRIPTOR_DESCADDR_Msk          (0xFFFFFFFFUL)                                 /**< (DMAC_DESCRIPTOR_DESCADDR) Register Mask  */



typedef struct
{  /* Direct Memory Access Controller */
  __IO  uint16_t BTCTRL;        /**< Offset: 0x00 (R/W  16) Block Transfer Control */
  __IO  uint16_t BTCNT;         /**< Offset: 0x02 (R/W  16) Block Transfer Count */
  __IO  uint32_t SRCADDR;       /**< Offset: 0x04 (R/W  32) Block Transfer Source Address */
  __IO  uint32_t DSTADDR;       /**< Offset: 0x08 (R/W  32) Block Transfer Destination Address */
  __IO  uint32_t DESCADDR;      /**< Offset: 0x0C (R/W  32) Next Descriptor Address */
} dmacdescriptor_registers_t;

#endif /* SAMC_SAMC21_DMAC_MODULE_H */

