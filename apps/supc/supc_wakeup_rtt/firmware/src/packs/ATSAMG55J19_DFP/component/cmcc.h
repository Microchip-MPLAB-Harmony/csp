/**
 * \brief Header file for SAMG/SAMG55 CMCC
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
#ifndef SAMG_SAMG55_CMCC_MODULE_H
#define SAMG_SAMG55_CMCC_MODULE_H

/** \addtogroup SAMG_SAMG55 Cortex-M Cache Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_CMCC                                  */
/* ========================================================================== */

/* -------- CMCC_TYPE : (CMCC Offset: 0x00) (R/  32) Cache Controller Type Register -------- */
#define CMCC_TYPE_AP_Pos                      (0U)                                           /**< (CMCC_TYPE) Access Port Access Allowed Position */
#define CMCC_TYPE_AP_Msk                      (0x1U << CMCC_TYPE_AP_Pos)                     /**< (CMCC_TYPE) Access Port Access Allowed Mask */
#define CMCC_TYPE_AP(value)                   (CMCC_TYPE_AP_Msk & ((value) << CMCC_TYPE_AP_Pos))
#define CMCC_TYPE_GCLK_Pos                    (1U)                                           /**< (CMCC_TYPE) Dynamic Clock Gating Supported Position */
#define CMCC_TYPE_GCLK_Msk                    (0x1U << CMCC_TYPE_GCLK_Pos)                   /**< (CMCC_TYPE) Dynamic Clock Gating Supported Mask */
#define CMCC_TYPE_GCLK(value)                 (CMCC_TYPE_GCLK_Msk & ((value) << CMCC_TYPE_GCLK_Pos))
#define CMCC_TYPE_RANDP_Pos                   (2U)                                           /**< (CMCC_TYPE) Random Selection Policy Supported Position */
#define CMCC_TYPE_RANDP_Msk                   (0x1U << CMCC_TYPE_RANDP_Pos)                  /**< (CMCC_TYPE) Random Selection Policy Supported Mask */
#define CMCC_TYPE_RANDP(value)                (CMCC_TYPE_RANDP_Msk & ((value) << CMCC_TYPE_RANDP_Pos))
#define CMCC_TYPE_LRUP_Pos                    (3U)                                           /**< (CMCC_TYPE) Least Recently Used Policy Supported Position */
#define CMCC_TYPE_LRUP_Msk                    (0x1U << CMCC_TYPE_LRUP_Pos)                   /**< (CMCC_TYPE) Least Recently Used Policy Supported Mask */
#define CMCC_TYPE_LRUP(value)                 (CMCC_TYPE_LRUP_Msk & ((value) << CMCC_TYPE_LRUP_Pos))
#define CMCC_TYPE_RRP_Pos                     (4U)                                           /**< (CMCC_TYPE) Random Selection Policy Supported Position */
#define CMCC_TYPE_RRP_Msk                     (0x1U << CMCC_TYPE_RRP_Pos)                    /**< (CMCC_TYPE) Random Selection Policy Supported Mask */
#define CMCC_TYPE_RRP(value)                  (CMCC_TYPE_RRP_Msk & ((value) << CMCC_TYPE_RRP_Pos))
#define CMCC_TYPE_WAYNUM_Pos                  (5U)                                           /**< (CMCC_TYPE) Number of Ways Position */
#define CMCC_TYPE_WAYNUM_Msk                  (0x3U << CMCC_TYPE_WAYNUM_Pos)                 /**< (CMCC_TYPE) Number of Ways Mask */
#define CMCC_TYPE_WAYNUM(value)               (CMCC_TYPE_WAYNUM_Msk & ((value) << CMCC_TYPE_WAYNUM_Pos))
#define   CMCC_TYPE_WAYNUM_DMAPPED_Val        (0U)                                           /**< (CMCC_TYPE) Direct Mapped Cache  */
#define   CMCC_TYPE_WAYNUM_ARCH2WAY_Val       (1U)                                           /**< (CMCC_TYPE) 2-way set associative  */
#define   CMCC_TYPE_WAYNUM_ARCH4WAY_Val       (2U)                                           /**< (CMCC_TYPE) 4-way set associative  */
#define   CMCC_TYPE_WAYNUM_ARCH8WAY_Val       (3U)                                           /**< (CMCC_TYPE) 8-way set associative  */
#define CMCC_TYPE_WAYNUM_DMAPPED              (CMCC_TYPE_WAYNUM_DMAPPED_Val << CMCC_TYPE_WAYNUM_Pos) /**< (CMCC_TYPE) Direct Mapped Cache Position  */
#define CMCC_TYPE_WAYNUM_ARCH2WAY             (CMCC_TYPE_WAYNUM_ARCH2WAY_Val << CMCC_TYPE_WAYNUM_Pos) /**< (CMCC_TYPE) 2-way set associative Position  */
#define CMCC_TYPE_WAYNUM_ARCH4WAY             (CMCC_TYPE_WAYNUM_ARCH4WAY_Val << CMCC_TYPE_WAYNUM_Pos) /**< (CMCC_TYPE) 4-way set associative Position  */
#define CMCC_TYPE_WAYNUM_ARCH8WAY             (CMCC_TYPE_WAYNUM_ARCH8WAY_Val << CMCC_TYPE_WAYNUM_Pos) /**< (CMCC_TYPE) 8-way set associative Position  */
#define CMCC_TYPE_LCKDOWN_Pos                 (7U)                                           /**< (CMCC_TYPE) Lockdown Supported Position */
#define CMCC_TYPE_LCKDOWN_Msk                 (0x1U << CMCC_TYPE_LCKDOWN_Pos)                /**< (CMCC_TYPE) Lockdown Supported Mask */
#define CMCC_TYPE_LCKDOWN(value)              (CMCC_TYPE_LCKDOWN_Msk & ((value) << CMCC_TYPE_LCKDOWN_Pos))
#define CMCC_TYPE_CSIZE_Pos                   (8U)                                           /**< (CMCC_TYPE) Data Cache Size Position */
#define CMCC_TYPE_CSIZE_Msk                   (0x7U << CMCC_TYPE_CSIZE_Pos)                  /**< (CMCC_TYPE) Data Cache Size Mask */
#define CMCC_TYPE_CSIZE(value)                (CMCC_TYPE_CSIZE_Msk & ((value) << CMCC_TYPE_CSIZE_Pos))
#define   CMCC_TYPE_CSIZE_CSIZE_1KB_Val       (0U)                                           /**< (CMCC_TYPE) Data cache size is 1 Kbyte  */
#define   CMCC_TYPE_CSIZE_CSIZE_2KB_Val       (1U)                                           /**< (CMCC_TYPE) Data cache size is 2 Kbytes  */
#define   CMCC_TYPE_CSIZE_CSIZE_4KB_Val       (2U)                                           /**< (CMCC_TYPE) Data cache size is 4 Kbytes  */
#define   CMCC_TYPE_CSIZE_CSIZE_8KB_Val       (3U)                                           /**< (CMCC_TYPE) Data cache size is 8 Kbytes  */
#define CMCC_TYPE_CSIZE_CSIZE_1KB             (CMCC_TYPE_CSIZE_CSIZE_1KB_Val << CMCC_TYPE_CSIZE_Pos) /**< (CMCC_TYPE) Data cache size is 1 Kbyte Position  */
#define CMCC_TYPE_CSIZE_CSIZE_2KB             (CMCC_TYPE_CSIZE_CSIZE_2KB_Val << CMCC_TYPE_CSIZE_Pos) /**< (CMCC_TYPE) Data cache size is 2 Kbytes Position  */
#define CMCC_TYPE_CSIZE_CSIZE_4KB             (CMCC_TYPE_CSIZE_CSIZE_4KB_Val << CMCC_TYPE_CSIZE_Pos) /**< (CMCC_TYPE) Data cache size is 4 Kbytes Position  */
#define CMCC_TYPE_CSIZE_CSIZE_8KB             (CMCC_TYPE_CSIZE_CSIZE_8KB_Val << CMCC_TYPE_CSIZE_Pos) /**< (CMCC_TYPE) Data cache size is 8 Kbytes Position  */
#define CMCC_TYPE_CLSIZE_Pos                  (11U)                                          /**< (CMCC_TYPE) Cache LIne Size Position */
#define CMCC_TYPE_CLSIZE_Msk                  (0x7U << CMCC_TYPE_CLSIZE_Pos)                 /**< (CMCC_TYPE) Cache LIne Size Mask */
#define CMCC_TYPE_CLSIZE(value)               (CMCC_TYPE_CLSIZE_Msk & ((value) << CMCC_TYPE_CLSIZE_Pos))
#define   CMCC_TYPE_CLSIZE_CLSIZE_1KB_Val     (0U)                                           /**< (CMCC_TYPE) Cache line size is 4 bytes  */
#define   CMCC_TYPE_CLSIZE_CLSIZE_2KB_Val     (1U)                                           /**< (CMCC_TYPE) Cache line size is 8 bytes  */
#define   CMCC_TYPE_CLSIZE_CLSIZE_4KB_Val     (2U)                                           /**< (CMCC_TYPE) Cache line size is 16 bytes  */
#define   CMCC_TYPE_CLSIZE_CLSIZE_8KB_Val     (3U)                                           /**< (CMCC_TYPE) Cache line size is 32 bytes  */
#define CMCC_TYPE_CLSIZE_CLSIZE_1KB           (CMCC_TYPE_CLSIZE_CLSIZE_1KB_Val << CMCC_TYPE_CLSIZE_Pos) /**< (CMCC_TYPE) Cache line size is 4 bytes Position  */
#define CMCC_TYPE_CLSIZE_CLSIZE_2KB           (CMCC_TYPE_CLSIZE_CLSIZE_2KB_Val << CMCC_TYPE_CLSIZE_Pos) /**< (CMCC_TYPE) Cache line size is 8 bytes Position  */
#define CMCC_TYPE_CLSIZE_CLSIZE_4KB           (CMCC_TYPE_CLSIZE_CLSIZE_4KB_Val << CMCC_TYPE_CLSIZE_Pos) /**< (CMCC_TYPE) Cache line size is 16 bytes Position  */
#define CMCC_TYPE_CLSIZE_CLSIZE_8KB           (CMCC_TYPE_CLSIZE_CLSIZE_8KB_Val << CMCC_TYPE_CLSIZE_Pos) /**< (CMCC_TYPE) Cache line size is 32 bytes Position  */
#define CMCC_TYPE_Msk                         (0x00003FFFUL)                                 /**< (CMCC_TYPE) Register Mask  */

/* -------- CMCC_CFG : (CMCC Offset: 0x04) (R/W 32) Cache Controller Configuration Register -------- */
#define CMCC_CFG_GCLKDIS_Pos                  (0U)                                           /**< (CMCC_CFG) Disable Clock Gating Position */
#define CMCC_CFG_GCLKDIS_Msk                  (0x1U << CMCC_CFG_GCLKDIS_Pos)                 /**< (CMCC_CFG) Disable Clock Gating Mask */
#define CMCC_CFG_GCLKDIS(value)               (CMCC_CFG_GCLKDIS_Msk & ((value) << CMCC_CFG_GCLKDIS_Pos))
#define CMCC_CFG_ICDIS_Pos                    (1U)                                           /**< (CMCC_CFG)  Position */
#define CMCC_CFG_ICDIS_Msk                    (0x1U << CMCC_CFG_ICDIS_Pos)                   /**< (CMCC_CFG)  Mask */
#define CMCC_CFG_ICDIS(value)                 (CMCC_CFG_ICDIS_Msk & ((value) << CMCC_CFG_ICDIS_Pos))
#define CMCC_CFG_DCDIS_Pos                    (2U)                                           /**< (CMCC_CFG)  Position */
#define CMCC_CFG_DCDIS_Msk                    (0x1U << CMCC_CFG_DCDIS_Pos)                   /**< (CMCC_CFG)  Mask */
#define CMCC_CFG_DCDIS(value)                 (CMCC_CFG_DCDIS_Msk & ((value) << CMCC_CFG_DCDIS_Pos))
#define CMCC_CFG_PRGCSIZE_Pos                 (4U)                                           /**< (CMCC_CFG)  Position */
#define CMCC_CFG_PRGCSIZE_Msk                 (0x7U << CMCC_CFG_PRGCSIZE_Pos)                /**< (CMCC_CFG)  Mask */
#define CMCC_CFG_PRGCSIZE(value)              (CMCC_CFG_PRGCSIZE_Msk & ((value) << CMCC_CFG_PRGCSIZE_Pos))
#define CMCC_CFG_Msk                          (0x00000077UL)                                 /**< (CMCC_CFG) Register Mask  */

/* -------- CMCC_CTRL : (CMCC Offset: 0x08) ( /W 32) Cache Controller Control Register -------- */
#define CMCC_CTRL_CEN_Pos                     (0U)                                           /**< (CMCC_CTRL) Cache Controller Enable Position */
#define CMCC_CTRL_CEN_Msk                     (0x1U << CMCC_CTRL_CEN_Pos)                    /**< (CMCC_CTRL) Cache Controller Enable Mask */
#define CMCC_CTRL_CEN(value)                  (CMCC_CTRL_CEN_Msk & ((value) << CMCC_CTRL_CEN_Pos))
#define CMCC_CTRL_Msk                         (0x00000001UL)                                 /**< (CMCC_CTRL) Register Mask  */

/* -------- CMCC_SR : (CMCC Offset: 0x0C) (R/  32) Cache Controller Status Register -------- */
#define CMCC_SR_CSTS_Pos                      (0U)                                           /**< (CMCC_SR) Cache Controller Status Position */
#define CMCC_SR_CSTS_Msk                      (0x1U << CMCC_SR_CSTS_Pos)                     /**< (CMCC_SR) Cache Controller Status Mask */
#define CMCC_SR_CSTS(value)                   (CMCC_SR_CSTS_Msk & ((value) << CMCC_SR_CSTS_Pos))
#define CMCC_SR_Msk                           (0x00000001UL)                                 /**< (CMCC_SR) Register Mask  */

/* -------- CMCC_MAINT0 : (CMCC Offset: 0x20) ( /W 32) Cache Controller Maintenance Register 0 -------- */
#define CMCC_MAINT0_INVALL_Pos                (0U)                                           /**< (CMCC_MAINT0) Cache Controller Invalidate All Position */
#define CMCC_MAINT0_INVALL_Msk                (0x1U << CMCC_MAINT0_INVALL_Pos)               /**< (CMCC_MAINT0) Cache Controller Invalidate All Mask */
#define CMCC_MAINT0_INVALL(value)             (CMCC_MAINT0_INVALL_Msk & ((value) << CMCC_MAINT0_INVALL_Pos))
#define CMCC_MAINT0_Msk                       (0x00000001UL)                                 /**< (CMCC_MAINT0) Register Mask  */

/* -------- CMCC_MAINT1 : (CMCC Offset: 0x24) ( /W 32) Cache Controller Maintenance Register 1 -------- */
#define CMCC_MAINT1_INDEX_Pos                 (4U)                                           /**< (CMCC_MAINT1) Invalidate Index Position */
#define CMCC_MAINT1_INDEX_Msk                 (0x1FU << CMCC_MAINT1_INDEX_Pos)               /**< (CMCC_MAINT1) Invalidate Index Mask */
#define CMCC_MAINT1_INDEX(value)              (CMCC_MAINT1_INDEX_Msk & ((value) << CMCC_MAINT1_INDEX_Pos))
#define CMCC_MAINT1_WAY_Pos                   (30U)                                          /**< (CMCC_MAINT1) Invalidate Way Position */
#define CMCC_MAINT1_WAY_Msk                   (0x3U << CMCC_MAINT1_WAY_Pos)                  /**< (CMCC_MAINT1) Invalidate Way Mask */
#define CMCC_MAINT1_WAY(value)                (CMCC_MAINT1_WAY_Msk & ((value) << CMCC_MAINT1_WAY_Pos))
#define   CMCC_MAINT1_WAY_WAY0_Val            (0U)                                           /**< (CMCC_MAINT1) Way 0 is selection for index invalidation  */
#define   CMCC_MAINT1_WAY_WAY1_Val            (1U)                                           /**< (CMCC_MAINT1) Way 1 is selection for index invalidation  */
#define   CMCC_MAINT1_WAY_WAY2_Val            (2U)                                           /**< (CMCC_MAINT1) Way 2 is selection for index invalidation  */
#define   CMCC_MAINT1_WAY_WAY3_Val            (3U)                                           /**< (CMCC_MAINT1) Way 3 is selection for index invalidation  */
#define CMCC_MAINT1_WAY_WAY0                  (CMCC_MAINT1_WAY_WAY0_Val << CMCC_MAINT1_WAY_Pos) /**< (CMCC_MAINT1) Way 0 is selection for index invalidation Position  */
#define CMCC_MAINT1_WAY_WAY1                  (CMCC_MAINT1_WAY_WAY1_Val << CMCC_MAINT1_WAY_Pos) /**< (CMCC_MAINT1) Way 1 is selection for index invalidation Position  */
#define CMCC_MAINT1_WAY_WAY2                  (CMCC_MAINT1_WAY_WAY2_Val << CMCC_MAINT1_WAY_Pos) /**< (CMCC_MAINT1) Way 2 is selection for index invalidation Position  */
#define CMCC_MAINT1_WAY_WAY3                  (CMCC_MAINT1_WAY_WAY3_Val << CMCC_MAINT1_WAY_Pos) /**< (CMCC_MAINT1) Way 3 is selection for index invalidation Position  */
#define CMCC_MAINT1_Msk                       (0xC00001F0UL)                                 /**< (CMCC_MAINT1) Register Mask  */

/* -------- CMCC_MCFG : (CMCC Offset: 0x28) (R/W 32) Cache Controller Monitor Configuration Register -------- */
#define CMCC_MCFG_MODE_Pos                    (0U)                                           /**< (CMCC_MCFG) Cache Controller Monitor Counter Mode Position */
#define CMCC_MCFG_MODE_Msk                    (0x3U << CMCC_MCFG_MODE_Pos)                   /**< (CMCC_MCFG) Cache Controller Monitor Counter Mode Mask */
#define CMCC_MCFG_MODE(value)                 (CMCC_MCFG_MODE_Msk & ((value) << CMCC_MCFG_MODE_Pos))
#define   CMCC_MCFG_MODE_CYCLE_COUNT_Val      (0U)                                           /**< (CMCC_MCFG) Cycle counter  */
#define   CMCC_MCFG_MODE_IHIT_COUNT_Val       (1U)                                           /**< (CMCC_MCFG) Instruction hit counter  */
#define   CMCC_MCFG_MODE_DHIT_COUNT_Val       (2U)                                           /**< (CMCC_MCFG) Data hit counter  */
#define CMCC_MCFG_MODE_CYCLE_COUNT            (CMCC_MCFG_MODE_CYCLE_COUNT_Val << CMCC_MCFG_MODE_Pos) /**< (CMCC_MCFG) Cycle counter Position  */
#define CMCC_MCFG_MODE_IHIT_COUNT             (CMCC_MCFG_MODE_IHIT_COUNT_Val << CMCC_MCFG_MODE_Pos) /**< (CMCC_MCFG) Instruction hit counter Position  */
#define CMCC_MCFG_MODE_DHIT_COUNT             (CMCC_MCFG_MODE_DHIT_COUNT_Val << CMCC_MCFG_MODE_Pos) /**< (CMCC_MCFG) Data hit counter Position  */
#define CMCC_MCFG_Msk                         (0x00000003UL)                                 /**< (CMCC_MCFG) Register Mask  */

/* -------- CMCC_MEN : (CMCC Offset: 0x2C) (R/W 32) Cache Controller Monitor Enable Register -------- */
#define CMCC_MEN_MENABLE_Pos                  (0U)                                           /**< (CMCC_MEN) Cache Controller Monitor Enable Position */
#define CMCC_MEN_MENABLE_Msk                  (0x1U << CMCC_MEN_MENABLE_Pos)                 /**< (CMCC_MEN) Cache Controller Monitor Enable Mask */
#define CMCC_MEN_MENABLE(value)               (CMCC_MEN_MENABLE_Msk & ((value) << CMCC_MEN_MENABLE_Pos))
#define CMCC_MEN_Msk                          (0x00000001UL)                                 /**< (CMCC_MEN) Register Mask  */

/* -------- CMCC_MCTRL : (CMCC Offset: 0x30) ( /W 32) Cache Controller Monitor Control Register -------- */
#define CMCC_MCTRL_SWRST_Pos                  (0U)                                           /**< (CMCC_MCTRL) Monitor Position */
#define CMCC_MCTRL_SWRST_Msk                  (0x1U << CMCC_MCTRL_SWRST_Pos)                 /**< (CMCC_MCTRL) Monitor Mask */
#define CMCC_MCTRL_SWRST(value)               (CMCC_MCTRL_SWRST_Msk & ((value) << CMCC_MCTRL_SWRST_Pos))
#define CMCC_MCTRL_Msk                        (0x00000001UL)                                 /**< (CMCC_MCTRL) Register Mask  */

/* -------- CMCC_MSR : (CMCC Offset: 0x34) (R/  32) Cache Controller Monitor Status Register -------- */
#define CMCC_MSR_EVENT_CNT_Pos                (0U)                                           /**< (CMCC_MSR) Monitor Event Counter Position */
#define CMCC_MSR_EVENT_CNT_Msk                (0xFFFFFFFFU << CMCC_MSR_EVENT_CNT_Pos)        /**< (CMCC_MSR) Monitor Event Counter Mask */
#define CMCC_MSR_EVENT_CNT(value)             (CMCC_MSR_EVENT_CNT_Msk & ((value) << CMCC_MSR_EVENT_CNT_Pos))
#define CMCC_MSR_Msk                          (0xFFFFFFFFUL)                                 /**< (CMCC_MSR) Register Mask  */

/** \brief CMCC register offsets definitions */
#define CMCC_TYPE_OFFSET               (0x00)         /**< (CMCC_TYPE) Cache Controller Type Register Offset */
#define CMCC_CFG_OFFSET                (0x04)         /**< (CMCC_CFG) Cache Controller Configuration Register Offset */
#define CMCC_CTRL_OFFSET               (0x08)         /**< (CMCC_CTRL) Cache Controller Control Register Offset */
#define CMCC_SR_OFFSET                 (0x0C)         /**< (CMCC_SR) Cache Controller Status Register Offset */
#define CMCC_MAINT0_OFFSET             (0x20)         /**< (CMCC_MAINT0) Cache Controller Maintenance Register 0 Offset */
#define CMCC_MAINT1_OFFSET             (0x24)         /**< (CMCC_MAINT1) Cache Controller Maintenance Register 1 Offset */
#define CMCC_MCFG_OFFSET               (0x28)         /**< (CMCC_MCFG) Cache Controller Monitor Configuration Register Offset */
#define CMCC_MEN_OFFSET                (0x2C)         /**< (CMCC_MEN) Cache Controller Monitor Enable Register Offset */
#define CMCC_MCTRL_OFFSET              (0x30)         /**< (CMCC_MCTRL) Cache Controller Monitor Control Register Offset */
#define CMCC_MSR_OFFSET                (0x34)         /**< (CMCC_MSR) Cache Controller Monitor Status Register Offset */

/** \brief CMCC register API structure */
typedef struct
{
  __I   uint32_t                       CMCC_TYPE;       /**< Offset: 0x00 (R/   32) Cache Controller Type Register */
  __IO  uint32_t                       CMCC_CFG;        /**< Offset: 0x04 (R/W  32) Cache Controller Configuration Register */
  __O   uint32_t                       CMCC_CTRL;       /**< Offset: 0x08 ( /W  32) Cache Controller Control Register */
  __I   uint32_t                       CMCC_SR;         /**< Offset: 0x0c (R/   32) Cache Controller Status Register */
  __I   uint8_t                        Reserved1[0x10];
  __O   uint32_t                       CMCC_MAINT0;     /**< Offset: 0x20 ( /W  32) Cache Controller Maintenance Register 0 */
  __O   uint32_t                       CMCC_MAINT1;     /**< Offset: 0x24 ( /W  32) Cache Controller Maintenance Register 1 */
  __IO  uint32_t                       CMCC_MCFG;       /**< Offset: 0x28 (R/W  32) Cache Controller Monitor Configuration Register */
  __IO  uint32_t                       CMCC_MEN;        /**< Offset: 0x2c (R/W  32) Cache Controller Monitor Enable Register */
  __O   uint32_t                       CMCC_MCTRL;      /**< Offset: 0x30 ( /W  32) Cache Controller Monitor Control Register */
  __I   uint32_t                       CMCC_MSR;        /**< Offset: 0x34 (R/   32) Cache Controller Monitor Status Register */
} cmcc_registers_t;
/** @}  end of Cortex-M Cache Controller */

#endif /* SAMG_SAMG55_CMCC_MODULE_H */

