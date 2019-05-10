/**
 * \brief Header file for SAMG/SAMG55 UHP
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
#ifndef SAMG_SAMG55_UHP_MODULE_H
#define SAMG_SAMG55_UHP_MODULE_H

/** \addtogroup SAMG_SAMG55 USB Host Port
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_UHP                                   */
/* ========================================================================== */

/* -------- UHP_HCREVISION : (UHP Offset: 0x00) (R/  32) OHCI Revision Number Register -------- */
#define UHP_HCREVISION_REV_Pos                (0U)                                           /**< (UHP_HCREVISION) OHCI revision number Position */
#define UHP_HCREVISION_REV_Msk                (0xFFU << UHP_HCREVISION_REV_Pos)              /**< (UHP_HCREVISION) OHCI revision number Mask */
#define UHP_HCREVISION_REV(value)             (UHP_HCREVISION_REV_Msk & ((value) << UHP_HCREVISION_REV_Pos))
#define UHP_HCREVISION_Msk                    (0x000000FFUL)                                 /**< (UHP_HCREVISION) Register Mask  */

/* -------- UHP_HCCONTROL : (UHP Offset: 0x04) (R/W 32) HC Operating Mode Register -------- */
#define UHP_HCCONTROL_CBSR_Pos                (0U)                                           /**< (UHP_HCCONTROL) Control/bulk service ratio Position */
#define UHP_HCCONTROL_CBSR_Msk                (0x3U << UHP_HCCONTROL_CBSR_Pos)               /**< (UHP_HCCONTROL) Control/bulk service ratio Mask */
#define UHP_HCCONTROL_CBSR(value)             (UHP_HCCONTROL_CBSR_Msk & ((value) << UHP_HCCONTROL_CBSR_Pos))
#define UHP_HCCONTROL_PLE_Pos                 (2U)                                           /**< (UHP_HCCONTROL) Periodic list enable Position */
#define UHP_HCCONTROL_PLE_Msk                 (0x1U << UHP_HCCONTROL_PLE_Pos)                /**< (UHP_HCCONTROL) Periodic list enable Mask */
#define UHP_HCCONTROL_PLE(value)              (UHP_HCCONTROL_PLE_Msk & ((value) << UHP_HCCONTROL_PLE_Pos))
#define UHP_HCCONTROL_IE_Pos                  (3U)                                           /**< (UHP_HCCONTROL) Isochronous enable Position */
#define UHP_HCCONTROL_IE_Msk                  (0x1U << UHP_HCCONTROL_IE_Pos)                 /**< (UHP_HCCONTROL) Isochronous enable Mask */
#define UHP_HCCONTROL_IE(value)               (UHP_HCCONTROL_IE_Msk & ((value) << UHP_HCCONTROL_IE_Pos))
#define UHP_HCCONTROL_CLE_Pos                 (4U)                                           /**< (UHP_HCCONTROL) Control list enable Position */
#define UHP_HCCONTROL_CLE_Msk                 (0x1U << UHP_HCCONTROL_CLE_Pos)                /**< (UHP_HCCONTROL) Control list enable Mask */
#define UHP_HCCONTROL_CLE(value)              (UHP_HCCONTROL_CLE_Msk & ((value) << UHP_HCCONTROL_CLE_Pos))
#define UHP_HCCONTROL_BLE_Pos                 (5U)                                           /**< (UHP_HCCONTROL) Bulk list enable Position */
#define UHP_HCCONTROL_BLE_Msk                 (0x1U << UHP_HCCONTROL_BLE_Pos)                /**< (UHP_HCCONTROL) Bulk list enable Mask */
#define UHP_HCCONTROL_BLE(value)              (UHP_HCCONTROL_BLE_Msk & ((value) << UHP_HCCONTROL_BLE_Pos))
#define UHP_HCCONTROL_HCFS_Pos                (6U)                                           /**< (UHP_HCCONTROL) Host controller functional state Position */
#define UHP_HCCONTROL_HCFS_Msk                (0x3U << UHP_HCCONTROL_HCFS_Pos)               /**< (UHP_HCCONTROL) Host controller functional state Mask */
#define UHP_HCCONTROL_HCFS(value)             (UHP_HCCONTROL_HCFS_Msk & ((value) << UHP_HCCONTROL_HCFS_Pos))
#define UHP_HCCONTROL_IR_Pos                  (8U)                                           /**< (UHP_HCCONTROL) Interrupt routing Position */
#define UHP_HCCONTROL_IR_Msk                  (0x1U << UHP_HCCONTROL_IR_Pos)                 /**< (UHP_HCCONTROL) Interrupt routing Mask */
#define UHP_HCCONTROL_IR(value)               (UHP_HCCONTROL_IR_Msk & ((value) << UHP_HCCONTROL_IR_Pos))
#define UHP_HCCONTROL_RWC_Pos                 (9U)                                           /**< (UHP_HCCONTROL) Remote wake-up connected Position */
#define UHP_HCCONTROL_RWC_Msk                 (0x1U << UHP_HCCONTROL_RWC_Pos)                /**< (UHP_HCCONTROL) Remote wake-up connected Mask */
#define UHP_HCCONTROL_RWC(value)              (UHP_HCCONTROL_RWC_Msk & ((value) << UHP_HCCONTROL_RWC_Pos))
#define UHP_HCCONTROL_RWE_Pos                 (10U)                                          /**< (UHP_HCCONTROL) Remote wake-up enable Position */
#define UHP_HCCONTROL_RWE_Msk                 (0x1U << UHP_HCCONTROL_RWE_Pos)                /**< (UHP_HCCONTROL) Remote wake-up enable Mask */
#define UHP_HCCONTROL_RWE(value)              (UHP_HCCONTROL_RWE_Msk & ((value) << UHP_HCCONTROL_RWE_Pos))
#define UHP_HCCONTROL_Msk                     (0x000007FFUL)                                 /**< (UHP_HCCONTROL) Register Mask  */

/* -------- UHP_HCCOMMANDSTATUS : (UHP Offset: 0x08) (R/W 32) HC Command and Status Register -------- */
#define UHP_HCCOMMANDSTATUS_HCR_Pos           (0U)                                           /**< (UHP_HCCOMMANDSTATUS) Host controller reset (read/write) Position */
#define UHP_HCCOMMANDSTATUS_HCR_Msk           (0x1U << UHP_HCCOMMANDSTATUS_HCR_Pos)          /**< (UHP_HCCOMMANDSTATUS) Host controller reset (read/write) Mask */
#define UHP_HCCOMMANDSTATUS_HCR(value)        (UHP_HCCOMMANDSTATUS_HCR_Msk & ((value) << UHP_HCCOMMANDSTATUS_HCR_Pos))
#define UHP_HCCOMMANDSTATUS_CLF_Pos           (1U)                                           /**< (UHP_HCCOMMANDSTATUS) Control list filled (read/write) Position */
#define UHP_HCCOMMANDSTATUS_CLF_Msk           (0x1U << UHP_HCCOMMANDSTATUS_CLF_Pos)          /**< (UHP_HCCOMMANDSTATUS) Control list filled (read/write) Mask */
#define UHP_HCCOMMANDSTATUS_CLF(value)        (UHP_HCCOMMANDSTATUS_CLF_Msk & ((value) << UHP_HCCOMMANDSTATUS_CLF_Pos))
#define UHP_HCCOMMANDSTATUS_BLF_Pos           (2U)                                           /**< (UHP_HCCOMMANDSTATUS) Bulk list filled (read/write) Position */
#define UHP_HCCOMMANDSTATUS_BLF_Msk           (0x1U << UHP_HCCOMMANDSTATUS_BLF_Pos)          /**< (UHP_HCCOMMANDSTATUS) Bulk list filled (read/write) Mask */
#define UHP_HCCOMMANDSTATUS_BLF(value)        (UHP_HCCOMMANDSTATUS_BLF_Msk & ((value) << UHP_HCCOMMANDSTATUS_BLF_Pos))
#define UHP_HCCOMMANDSTATUS_OCR_Pos           (3U)                                           /**< (UHP_HCCOMMANDSTATUS) Ownership change request (read/write) Position */
#define UHP_HCCOMMANDSTATUS_OCR_Msk           (0x1U << UHP_HCCOMMANDSTATUS_OCR_Pos)          /**< (UHP_HCCOMMANDSTATUS) Ownership change request (read/write) Mask */
#define UHP_HCCOMMANDSTATUS_OCR(value)        (UHP_HCCOMMANDSTATUS_OCR_Msk & ((value) << UHP_HCCOMMANDSTATUS_OCR_Pos))
#define UHP_HCCOMMANDSTATUS_SOC_Pos           (16U)                                          /**< (UHP_HCCOMMANDSTATUS) Scheduling overrun count (read-only) Position */
#define UHP_HCCOMMANDSTATUS_SOC_Msk           (0x3U << UHP_HCCOMMANDSTATUS_SOC_Pos)          /**< (UHP_HCCOMMANDSTATUS) Scheduling overrun count (read-only) Mask */
#define UHP_HCCOMMANDSTATUS_SOC(value)        (UHP_HCCOMMANDSTATUS_SOC_Msk & ((value) << UHP_HCCOMMANDSTATUS_SOC_Pos))
#define UHP_HCCOMMANDSTATUS_Msk               (0x0003000FUL)                                 /**< (UHP_HCCOMMANDSTATUS) Register Mask  */

/* -------- UHP_HCINTERRUPTSTATUS : (UHP Offset: 0x0C) (R/W 32) HC Interrupt and Status Register -------- */
#define UHP_HCINTERRUPTSTATUS_SO_Pos          (0U)                                           /**< (UHP_HCINTERRUPTSTATUS) Scheduling overrun (read/write, write '1' to clear) Position */
#define UHP_HCINTERRUPTSTATUS_SO_Msk          (0x1U << UHP_HCINTERRUPTSTATUS_SO_Pos)         /**< (UHP_HCINTERRUPTSTATUS) Scheduling overrun (read/write, write '1' to clear) Mask */
#define UHP_HCINTERRUPTSTATUS_SO(value)       (UHP_HCINTERRUPTSTATUS_SO_Msk & ((value) << UHP_HCINTERRUPTSTATUS_SO_Pos))
#define UHP_HCINTERRUPTSTATUS_WDH_Pos         (1U)                                           /**< (UHP_HCINTERRUPTSTATUS) Write done head (read/write, write '1' to clear) Position */
#define UHP_HCINTERRUPTSTATUS_WDH_Msk         (0x1U << UHP_HCINTERRUPTSTATUS_WDH_Pos)        /**< (UHP_HCINTERRUPTSTATUS) Write done head (read/write, write '1' to clear) Mask */
#define UHP_HCINTERRUPTSTATUS_WDH(value)      (UHP_HCINTERRUPTSTATUS_WDH_Msk & ((value) << UHP_HCINTERRUPTSTATUS_WDH_Pos))
#define UHP_HCINTERRUPTSTATUS_SF_Pos          (2U)                                           /**< (UHP_HCINTERRUPTSTATUS) Start of frame (read/write, write '1' to clear) Position */
#define UHP_HCINTERRUPTSTATUS_SF_Msk          (0x1U << UHP_HCINTERRUPTSTATUS_SF_Pos)         /**< (UHP_HCINTERRUPTSTATUS) Start of frame (read/write, write '1' to clear) Mask */
#define UHP_HCINTERRUPTSTATUS_SF(value)       (UHP_HCINTERRUPTSTATUS_SF_Msk & ((value) << UHP_HCINTERRUPTSTATUS_SF_Pos))
#define UHP_HCINTERRUPTSTATUS_RD_Pos          (3U)                                           /**< (UHP_HCINTERRUPTSTATUS) Resume detected (read/write, write '1' to clear) Position */
#define UHP_HCINTERRUPTSTATUS_RD_Msk          (0x1U << UHP_HCINTERRUPTSTATUS_RD_Pos)         /**< (UHP_HCINTERRUPTSTATUS) Resume detected (read/write, write '1' to clear) Mask */
#define UHP_HCINTERRUPTSTATUS_RD(value)       (UHP_HCINTERRUPTSTATUS_RD_Msk & ((value) << UHP_HCINTERRUPTSTATUS_RD_Pos))
#define UHP_HCINTERRUPTSTATUS_UE_Pos          (4U)                                           /**< (UHP_HCINTERRUPTSTATUS) Unrecoverable error (read/write, write '1' to clear) Position */
#define UHP_HCINTERRUPTSTATUS_UE_Msk          (0x1U << UHP_HCINTERRUPTSTATUS_UE_Pos)         /**< (UHP_HCINTERRUPTSTATUS) Unrecoverable error (read/write, write '1' to clear) Mask */
#define UHP_HCINTERRUPTSTATUS_UE(value)       (UHP_HCINTERRUPTSTATUS_UE_Msk & ((value) << UHP_HCINTERRUPTSTATUS_UE_Pos))
#define UHP_HCINTERRUPTSTATUS_FNO_Pos         (5U)                                           /**< (UHP_HCINTERRUPTSTATUS) Frame number overflow (read/write, write '1' to clear) Position */
#define UHP_HCINTERRUPTSTATUS_FNO_Msk         (0x1U << UHP_HCINTERRUPTSTATUS_FNO_Pos)        /**< (UHP_HCINTERRUPTSTATUS) Frame number overflow (read/write, write '1' to clear) Mask */
#define UHP_HCINTERRUPTSTATUS_FNO(value)      (UHP_HCINTERRUPTSTATUS_FNO_Msk & ((value) << UHP_HCINTERRUPTSTATUS_FNO_Pos))
#define UHP_HCINTERRUPTSTATUS_RHSC_Pos        (6U)                                           /**< (UHP_HCINTERRUPTSTATUS) Root hub status change (read/write, write '1' to clear) Position */
#define UHP_HCINTERRUPTSTATUS_RHSC_Msk        (0x1U << UHP_HCINTERRUPTSTATUS_RHSC_Pos)       /**< (UHP_HCINTERRUPTSTATUS) Root hub status change (read/write, write '1' to clear) Mask */
#define UHP_HCINTERRUPTSTATUS_RHSC(value)     (UHP_HCINTERRUPTSTATUS_RHSC_Msk & ((value) << UHP_HCINTERRUPTSTATUS_RHSC_Pos))
#define UHP_HCINTERRUPTSTATUS_OC_Pos          (30U)                                          /**< (UHP_HCINTERRUPTSTATUS) Ownership change (read-only) Position */
#define UHP_HCINTERRUPTSTATUS_OC_Msk          (0x1U << UHP_HCINTERRUPTSTATUS_OC_Pos)         /**< (UHP_HCINTERRUPTSTATUS) Ownership change (read-only) Mask */
#define UHP_HCINTERRUPTSTATUS_OC(value)       (UHP_HCINTERRUPTSTATUS_OC_Msk & ((value) << UHP_HCINTERRUPTSTATUS_OC_Pos))
#define UHP_HCINTERRUPTSTATUS_Msk             (0x4000007FUL)                                 /**< (UHP_HCINTERRUPTSTATUS) Register Mask  */

/* -------- UHP_HCINTERRUPTENABLE : (UHP Offset: 0x10) (R/W 32) HC Interrupt Enable Register -------- */
#define UHP_HCINTERRUPTENABLE_SO_Pos          (0U)                                           /**< (UHP_HCINTERRUPTENABLE) Scheduling overrun (read/write, write '1' to set) Position */
#define UHP_HCINTERRUPTENABLE_SO_Msk          (0x1U << UHP_HCINTERRUPTENABLE_SO_Pos)         /**< (UHP_HCINTERRUPTENABLE) Scheduling overrun (read/write, write '1' to set) Mask */
#define UHP_HCINTERRUPTENABLE_SO(value)       (UHP_HCINTERRUPTENABLE_SO_Msk & ((value) << UHP_HCINTERRUPTENABLE_SO_Pos))
#define UHP_HCINTERRUPTENABLE_WDH_Pos         (1U)                                           /**< (UHP_HCINTERRUPTENABLE) Write done head (read/write, write '1' to set) Position */
#define UHP_HCINTERRUPTENABLE_WDH_Msk         (0x1U << UHP_HCINTERRUPTENABLE_WDH_Pos)        /**< (UHP_HCINTERRUPTENABLE) Write done head (read/write, write '1' to set) Mask */
#define UHP_HCINTERRUPTENABLE_WDH(value)      (UHP_HCINTERRUPTENABLE_WDH_Msk & ((value) << UHP_HCINTERRUPTENABLE_WDH_Pos))
#define UHP_HCINTERRUPTENABLE_SF_Pos          (2U)                                           /**< (UHP_HCINTERRUPTENABLE) Start of frame (read/write, write '1' to set) Position */
#define UHP_HCINTERRUPTENABLE_SF_Msk          (0x1U << UHP_HCINTERRUPTENABLE_SF_Pos)         /**< (UHP_HCINTERRUPTENABLE) Start of frame (read/write, write '1' to set) Mask */
#define UHP_HCINTERRUPTENABLE_SF(value)       (UHP_HCINTERRUPTENABLE_SF_Msk & ((value) << UHP_HCINTERRUPTENABLE_SF_Pos))
#define UHP_HCINTERRUPTENABLE_RD_Pos          (3U)                                           /**< (UHP_HCINTERRUPTENABLE) Resume detected (read/write, write '1' to set) Position */
#define UHP_HCINTERRUPTENABLE_RD_Msk          (0x1U << UHP_HCINTERRUPTENABLE_RD_Pos)         /**< (UHP_HCINTERRUPTENABLE) Resume detected (read/write, write '1' to set) Mask */
#define UHP_HCINTERRUPTENABLE_RD(value)       (UHP_HCINTERRUPTENABLE_RD_Msk & ((value) << UHP_HCINTERRUPTENABLE_RD_Pos))
#define UHP_HCINTERRUPTENABLE_UE_Pos          (4U)                                           /**< (UHP_HCINTERRUPTENABLE) Unrecoverable error (read/write, write '1' to set) Position */
#define UHP_HCINTERRUPTENABLE_UE_Msk          (0x1U << UHP_HCINTERRUPTENABLE_UE_Pos)         /**< (UHP_HCINTERRUPTENABLE) Unrecoverable error (read/write, write '1' to set) Mask */
#define UHP_HCINTERRUPTENABLE_UE(value)       (UHP_HCINTERRUPTENABLE_UE_Msk & ((value) << UHP_HCINTERRUPTENABLE_UE_Pos))
#define UHP_HCINTERRUPTENABLE_FNO_Pos         (5U)                                           /**< (UHP_HCINTERRUPTENABLE) Frame number overflow (read/write, write '1' to set) Position */
#define UHP_HCINTERRUPTENABLE_FNO_Msk         (0x1U << UHP_HCINTERRUPTENABLE_FNO_Pos)        /**< (UHP_HCINTERRUPTENABLE) Frame number overflow (read/write, write '1' to set) Mask */
#define UHP_HCINTERRUPTENABLE_FNO(value)      (UHP_HCINTERRUPTENABLE_FNO_Msk & ((value) << UHP_HCINTERRUPTENABLE_FNO_Pos))
#define UHP_HCINTERRUPTENABLE_RHSC_Pos        (6U)                                           /**< (UHP_HCINTERRUPTENABLE) Root hub status change (read/write, write '1' to set) Position */
#define UHP_HCINTERRUPTENABLE_RHSC_Msk        (0x1U << UHP_HCINTERRUPTENABLE_RHSC_Pos)       /**< (UHP_HCINTERRUPTENABLE) Root hub status change (read/write, write '1' to set) Mask */
#define UHP_HCINTERRUPTENABLE_RHSC(value)     (UHP_HCINTERRUPTENABLE_RHSC_Msk & ((value) << UHP_HCINTERRUPTENABLE_RHSC_Pos))
#define UHP_HCINTERRUPTENABLE_OC_Pos          (30U)                                          /**< (UHP_HCINTERRUPTENABLE) Ownership change (read-only) Position */
#define UHP_HCINTERRUPTENABLE_OC_Msk          (0x1U << UHP_HCINTERRUPTENABLE_OC_Pos)         /**< (UHP_HCINTERRUPTENABLE) Ownership change (read-only) Mask */
#define UHP_HCINTERRUPTENABLE_OC(value)       (UHP_HCINTERRUPTENABLE_OC_Msk & ((value) << UHP_HCINTERRUPTENABLE_OC_Pos))
#define UHP_HCINTERRUPTENABLE_MIE_Pos         (31U)                                          /**< (UHP_HCINTERRUPTENABLE) Master interrupt enable (read/write, write '1' to set) Position */
#define UHP_HCINTERRUPTENABLE_MIE_Msk         (0x1U << UHP_HCINTERRUPTENABLE_MIE_Pos)        /**< (UHP_HCINTERRUPTENABLE) Master interrupt enable (read/write, write '1' to set) Mask */
#define UHP_HCINTERRUPTENABLE_MIE(value)      (UHP_HCINTERRUPTENABLE_MIE_Msk & ((value) << UHP_HCINTERRUPTENABLE_MIE_Pos))
#define UHP_HCINTERRUPTENABLE_Msk             (0xC000007FUL)                                 /**< (UHP_HCINTERRUPTENABLE) Register Mask  */

/* -------- UHP_HCINTERRUPTDISABLE : (UHP Offset: 0x14) (R/W 32) HC Interrupt Disable Register -------- */
#define UHP_HCINTERRUPTDISABLE_SO_Pos         (0U)                                           /**< (UHP_HCINTERRUPTDISABLE) Scheduling overrun (read/write) Position */
#define UHP_HCINTERRUPTDISABLE_SO_Msk         (0x1U << UHP_HCINTERRUPTDISABLE_SO_Pos)        /**< (UHP_HCINTERRUPTDISABLE) Scheduling overrun (read/write) Mask */
#define UHP_HCINTERRUPTDISABLE_SO(value)      (UHP_HCINTERRUPTDISABLE_SO_Msk & ((value) << UHP_HCINTERRUPTDISABLE_SO_Pos))
#define UHP_HCINTERRUPTDISABLE_WDH_Pos        (1U)                                           /**< (UHP_HCINTERRUPTDISABLE) Write done head (read/write) Position */
#define UHP_HCINTERRUPTDISABLE_WDH_Msk        (0x1U << UHP_HCINTERRUPTDISABLE_WDH_Pos)       /**< (UHP_HCINTERRUPTDISABLE) Write done head (read/write) Mask */
#define UHP_HCINTERRUPTDISABLE_WDH(value)     (UHP_HCINTERRUPTDISABLE_WDH_Msk & ((value) << UHP_HCINTERRUPTDISABLE_WDH_Pos))
#define UHP_HCINTERRUPTDISABLE_SF_Pos         (2U)                                           /**< (UHP_HCINTERRUPTDISABLE) Start of frame (read/write) Position */
#define UHP_HCINTERRUPTDISABLE_SF_Msk         (0x1U << UHP_HCINTERRUPTDISABLE_SF_Pos)        /**< (UHP_HCINTERRUPTDISABLE) Start of frame (read/write) Mask */
#define UHP_HCINTERRUPTDISABLE_SF(value)      (UHP_HCINTERRUPTDISABLE_SF_Msk & ((value) << UHP_HCINTERRUPTDISABLE_SF_Pos))
#define UHP_HCINTERRUPTDISABLE_RD_Pos         (3U)                                           /**< (UHP_HCINTERRUPTDISABLE) Resume detected (read/write) Position */
#define UHP_HCINTERRUPTDISABLE_RD_Msk         (0x1U << UHP_HCINTERRUPTDISABLE_RD_Pos)        /**< (UHP_HCINTERRUPTDISABLE) Resume detected (read/write) Mask */
#define UHP_HCINTERRUPTDISABLE_RD(value)      (UHP_HCINTERRUPTDISABLE_RD_Msk & ((value) << UHP_HCINTERRUPTDISABLE_RD_Pos))
#define UHP_HCINTERRUPTDISABLE_UE_Pos         (4U)                                           /**< (UHP_HCINTERRUPTDISABLE) Unrecoverable error (read/write) Position */
#define UHP_HCINTERRUPTDISABLE_UE_Msk         (0x1U << UHP_HCINTERRUPTDISABLE_UE_Pos)        /**< (UHP_HCINTERRUPTDISABLE) Unrecoverable error (read/write) Mask */
#define UHP_HCINTERRUPTDISABLE_UE(value)      (UHP_HCINTERRUPTDISABLE_UE_Msk & ((value) << UHP_HCINTERRUPTDISABLE_UE_Pos))
#define UHP_HCINTERRUPTDISABLE_FNO_Pos        (5U)                                           /**< (UHP_HCINTERRUPTDISABLE) Frame number overflow (read/write) Position */
#define UHP_HCINTERRUPTDISABLE_FNO_Msk        (0x1U << UHP_HCINTERRUPTDISABLE_FNO_Pos)       /**< (UHP_HCINTERRUPTDISABLE) Frame number overflow (read/write) Mask */
#define UHP_HCINTERRUPTDISABLE_FNO(value)     (UHP_HCINTERRUPTDISABLE_FNO_Msk & ((value) << UHP_HCINTERRUPTDISABLE_FNO_Pos))
#define UHP_HCINTERRUPTDISABLE_RHSC_Pos       (6U)                                           /**< (UHP_HCINTERRUPTDISABLE) Root hub status change (read/write) Position */
#define UHP_HCINTERRUPTDISABLE_RHSC_Msk       (0x1U << UHP_HCINTERRUPTDISABLE_RHSC_Pos)      /**< (UHP_HCINTERRUPTDISABLE) Root hub status change (read/write) Mask */
#define UHP_HCINTERRUPTDISABLE_RHSC(value)    (UHP_HCINTERRUPTDISABLE_RHSC_Msk & ((value) << UHP_HCINTERRUPTDISABLE_RHSC_Pos))
#define UHP_HCINTERRUPTDISABLE_OC_Pos         (30U)                                          /**< (UHP_HCINTERRUPTDISABLE) Ownership change (read-only) Position */
#define UHP_HCINTERRUPTDISABLE_OC_Msk         (0x1U << UHP_HCINTERRUPTDISABLE_OC_Pos)        /**< (UHP_HCINTERRUPTDISABLE) Ownership change (read-only) Mask */
#define UHP_HCINTERRUPTDISABLE_OC(value)      (UHP_HCINTERRUPTDISABLE_OC_Msk & ((value) << UHP_HCINTERRUPTDISABLE_OC_Pos))
#define UHP_HCINTERRUPTDISABLE_MIE_Pos        (31U)                                          /**< (UHP_HCINTERRUPTDISABLE) Master interrupt enable (read/write) Position */
#define UHP_HCINTERRUPTDISABLE_MIE_Msk        (0x1U << UHP_HCINTERRUPTDISABLE_MIE_Pos)       /**< (UHP_HCINTERRUPTDISABLE) Master interrupt enable (read/write) Mask */
#define UHP_HCINTERRUPTDISABLE_MIE(value)     (UHP_HCINTERRUPTDISABLE_MIE_Msk & ((value) << UHP_HCINTERRUPTDISABLE_MIE_Pos))
#define UHP_HCINTERRUPTDISABLE_Msk            (0xC000007FUL)                                 /**< (UHP_HCINTERRUPTDISABLE) Register Mask  */

/* -------- UHP_HCHCCA : (UHP Offset: 0x18) (R/W 32) HC HCCA Address Register -------- */
#define UHP_HCHCCA_HCCA_Pos                   (8U)                                           /**< (UHP_HCHCCA) Physical address of the beginning of the HCCA Position */
#define UHP_HCHCCA_HCCA_Msk                   (0xFFFFFFU << UHP_HCHCCA_HCCA_Pos)             /**< (UHP_HCHCCA) Physical address of the beginning of the HCCA Mask */
#define UHP_HCHCCA_HCCA(value)                (UHP_HCHCCA_HCCA_Msk & ((value) << UHP_HCHCCA_HCCA_Pos))
#define UHP_HCHCCA_Msk                        (0xFFFFFF00UL)                                 /**< (UHP_HCHCCA) Register Mask  */

/* -------- UHP_HCPERIODCURRENTED : (UHP Offset: 0x1C) (R/  32) HC Current Periodic Register -------- */
#define UHP_HCPERIODCURRENTED_PCED_Pos        (4U)                                           /**< (UHP_HCPERIODCURRENTED) Physical address of the current ED on the periodic ED list Position */
#define UHP_HCPERIODCURRENTED_PCED_Msk        (0xFFFFFFFU << UHP_HCPERIODCURRENTED_PCED_Pos) /**< (UHP_HCPERIODCURRENTED) Physical address of the current ED on the periodic ED list Mask */
#define UHP_HCPERIODCURRENTED_PCED(value)     (UHP_HCPERIODCURRENTED_PCED_Msk & ((value) << UHP_HCPERIODCURRENTED_PCED_Pos))
#define UHP_HCPERIODCURRENTED_Msk             (0xFFFFFFF0UL)                                 /**< (UHP_HCPERIODCURRENTED) Register Mask  */

/* -------- UHP_HCCONTROLHEADED : (UHP Offset: 0x20) (R/W 32) HC Head Control Register -------- */
#define UHP_HCCONTROLHEADED_CHED_Pos          (4U)                                           /**< (UHP_HCCONTROLHEADED) Physical address of the head ED on the control ED list Position */
#define UHP_HCCONTROLHEADED_CHED_Msk          (0xFFFFFFFU << UHP_HCCONTROLHEADED_CHED_Pos)   /**< (UHP_HCCONTROLHEADED) Physical address of the head ED on the control ED list Mask */
#define UHP_HCCONTROLHEADED_CHED(value)       (UHP_HCCONTROLHEADED_CHED_Msk & ((value) << UHP_HCCONTROLHEADED_CHED_Pos))
#define UHP_HCCONTROLHEADED_Msk               (0xFFFFFFF0UL)                                 /**< (UHP_HCCONTROLHEADED) Register Mask  */

/* -------- UHP_HCCONTROLCURRENTED : (UHP Offset: 0x24) (R/W 32) HC Current Control Register -------- */
#define UHP_HCCONTROLCURRENTED_CCED_Pos       (4U)                                           /**< (UHP_HCCONTROLCURRENTED) Physical address of the current ED on the control ED list Position */
#define UHP_HCCONTROLCURRENTED_CCED_Msk       (0xFFFFFFFU << UHP_HCCONTROLCURRENTED_CCED_Pos) /**< (UHP_HCCONTROLCURRENTED) Physical address of the current ED on the control ED list Mask */
#define UHP_HCCONTROLCURRENTED_CCED(value)    (UHP_HCCONTROLCURRENTED_CCED_Msk & ((value) << UHP_HCCONTROLCURRENTED_CCED_Pos))
#define UHP_HCCONTROLCURRENTED_Msk            (0xFFFFFFF0UL)                                 /**< (UHP_HCCONTROLCURRENTED) Register Mask  */

/* -------- UHP_HCBULKHEADED : (UHP Offset: 0x28) (R/W 32) HC Head Bulk Register -------- */
#define UHP_HCBULKHEADED_BHED_Pos             (4U)                                           /**< (UHP_HCBULKHEADED) Physical address of the head ED on the bulk ED list Position */
#define UHP_HCBULKHEADED_BHED_Msk             (0xFFFFFFFU << UHP_HCBULKHEADED_BHED_Pos)      /**< (UHP_HCBULKHEADED) Physical address of the head ED on the bulk ED list Mask */
#define UHP_HCBULKHEADED_BHED(value)          (UHP_HCBULKHEADED_BHED_Msk & ((value) << UHP_HCBULKHEADED_BHED_Pos))
#define UHP_HCBULKHEADED_Msk                  (0xFFFFFFF0UL)                                 /**< (UHP_HCBULKHEADED) Register Mask  */

/* -------- UHP_HCBULKCURRENTED : (UHP Offset: 0x2C) (R/W 32) HC Current Bulk Register -------- */
#define UHP_HCBULKCURRENTED_BCED_Pos          (4U)                                           /**< (UHP_HCBULKCURRENTED) Physical address of the current ED on the bulk ED list Position */
#define UHP_HCBULKCURRENTED_BCED_Msk          (0xFFFFFFFU << UHP_HCBULKCURRENTED_BCED_Pos)   /**< (UHP_HCBULKCURRENTED) Physical address of the current ED on the bulk ED list Mask */
#define UHP_HCBULKCURRENTED_BCED(value)       (UHP_HCBULKCURRENTED_BCED_Msk & ((value) << UHP_HCBULKCURRENTED_BCED_Pos))
#define UHP_HCBULKCURRENTED_Msk               (0xFFFFFFF0UL)                                 /**< (UHP_HCBULKCURRENTED) Register Mask  */

/* -------- UHP_HCDONEHEAD : (UHP Offset: 0x30) (R/  32) HC Head Done Register -------- */
#define UHP_HCDONEHEAD_DH_Pos                 (4U)                                           /**< (UHP_HCDONEHEAD) Physical address of the last TD that has added to the done queue Position */
#define UHP_HCDONEHEAD_DH_Msk                 (0xFFFFFFFU << UHP_HCDONEHEAD_DH_Pos)          /**< (UHP_HCDONEHEAD) Physical address of the last TD that has added to the done queue Mask */
#define UHP_HCDONEHEAD_DH(value)              (UHP_HCDONEHEAD_DH_Msk & ((value) << UHP_HCDONEHEAD_DH_Pos))
#define UHP_HCDONEHEAD_Msk                    (0xFFFFFFF0UL)                                 /**< (UHP_HCDONEHEAD) Register Mask  */

/* -------- UHP_HCFMINTERVAL : (UHP Offset: 0x34) (R/W 32) HC Frame Interval Register -------- */
#define UHP_HCFMINTERVAL_FRAMEINTERVAL_Pos    (0U)                                           /**< (UHP_HCFMINTERVAL) Frame interval Position */
#define UHP_HCFMINTERVAL_FRAMEINTERVAL_Msk    (0x3FFFU << UHP_HCFMINTERVAL_FRAMEINTERVAL_Pos) /**< (UHP_HCFMINTERVAL) Frame interval Mask */
#define UHP_HCFMINTERVAL_FRAMEINTERVAL(value) (UHP_HCFMINTERVAL_FRAMEINTERVAL_Msk & ((value) << UHP_HCFMINTERVAL_FRAMEINTERVAL_Pos))
#define UHP_HCFMINTERVAL_FSMPS_Pos            (16U)                                          /**< (UHP_HCFMINTERVAL) Largest data packet Position */
#define UHP_HCFMINTERVAL_FSMPS_Msk            (0x7FFFU << UHP_HCFMINTERVAL_FSMPS_Pos)        /**< (UHP_HCFMINTERVAL) Largest data packet Mask */
#define UHP_HCFMINTERVAL_FSMPS(value)         (UHP_HCFMINTERVAL_FSMPS_Msk & ((value) << UHP_HCFMINTERVAL_FSMPS_Pos))
#define UHP_HCFMINTERVAL_FIT_Pos              (31U)                                          /**< (UHP_HCFMINTERVAL) Frame interval toggle Position */
#define UHP_HCFMINTERVAL_FIT_Msk              (0x1U << UHP_HCFMINTERVAL_FIT_Pos)             /**< (UHP_HCFMINTERVAL) Frame interval toggle Mask */
#define UHP_HCFMINTERVAL_FIT(value)           (UHP_HCFMINTERVAL_FIT_Msk & ((value) << UHP_HCFMINTERVAL_FIT_Pos))
#define UHP_HCFMINTERVAL_Msk                  (0xFFFF3FFFUL)                                 /**< (UHP_HCFMINTERVAL) Register Mask  */

/* -------- UHP_HCFMREMAINING : (UHP Offset: 0x38) (R/  32) HC Frame Remaining Register -------- */
#define UHP_HCFMREMAINING_FR_Pos              (0U)                                           /**< (UHP_HCFMREMAINING) Frame remaining Position */
#define UHP_HCFMREMAINING_FR_Msk              (0x3FFFU << UHP_HCFMREMAINING_FR_Pos)          /**< (UHP_HCFMREMAINING) Frame remaining Mask */
#define UHP_HCFMREMAINING_FR(value)           (UHP_HCFMREMAINING_FR_Msk & ((value) << UHP_HCFMREMAINING_FR_Pos))
#define UHP_HCFMREMAINING_FRT_Pos             (31U)                                          /**< (UHP_HCFMREMAINING) Frame remaining toggle Position */
#define UHP_HCFMREMAINING_FRT_Msk             (0x1U << UHP_HCFMREMAINING_FRT_Pos)            /**< (UHP_HCFMREMAINING) Frame remaining toggle Mask */
#define UHP_HCFMREMAINING_FRT(value)          (UHP_HCFMREMAINING_FRT_Msk & ((value) << UHP_HCFMREMAINING_FRT_Pos))
#define UHP_HCFMREMAINING_Msk                 (0x80003FFFUL)                                 /**< (UHP_HCFMREMAINING) Register Mask  */

/* -------- UHP_HCFMNUMBER : (UHP Offset: 0x3C) (R/  32) HC Frame Number Register -------- */
#define UHP_HCFMNUMBER_FN_Pos                 (0U)                                           /**< (UHP_HCFMNUMBER) Frame number Position */
#define UHP_HCFMNUMBER_FN_Msk                 (0xFFFFU << UHP_HCFMNUMBER_FN_Pos)             /**< (UHP_HCFMNUMBER) Frame number Mask */
#define UHP_HCFMNUMBER_FN(value)              (UHP_HCFMNUMBER_FN_Msk & ((value) << UHP_HCFMNUMBER_FN_Pos))
#define UHP_HCFMNUMBER_Msk                    (0x0000FFFFUL)                                 /**< (UHP_HCFMNUMBER) Register Mask  */

/* -------- UHP_HCPERIODICSTART : (UHP Offset: 0x40) (R/W 32) HC Periodic Start Register -------- */
#define UHP_HCPERIODICSTART_PS_Pos            (0U)                                           /**< (UHP_HCPERIODICSTART) Periodic start Position */
#define UHP_HCPERIODICSTART_PS_Msk            (0x3FFFU << UHP_HCPERIODICSTART_PS_Pos)        /**< (UHP_HCPERIODICSTART) Periodic start Mask */
#define UHP_HCPERIODICSTART_PS(value)         (UHP_HCPERIODICSTART_PS_Msk & ((value) << UHP_HCPERIODICSTART_PS_Pos))
#define UHP_HCPERIODICSTART_Msk               (0x00003FFFUL)                                 /**< (UHP_HCPERIODICSTART) Register Mask  */

/* -------- UHP_HCLSTHRESHOLD : (UHP Offset: 0x44) (R/W 32) HC Low-Speed Threshold Register -------- */
#define UHP_HCLSTHRESHOLD_LST_Pos             (0U)                                           /**< (UHP_HCLSTHRESHOLD) Low-speed threshold Position */
#define UHP_HCLSTHRESHOLD_LST_Msk             (0x3FFFU << UHP_HCLSTHRESHOLD_LST_Pos)         /**< (UHP_HCLSTHRESHOLD) Low-speed threshold Mask */
#define UHP_HCLSTHRESHOLD_LST(value)          (UHP_HCLSTHRESHOLD_LST_Msk & ((value) << UHP_HCLSTHRESHOLD_LST_Pos))
#define UHP_HCLSTHRESHOLD_Msk                 (0x00003FFFUL)                                 /**< (UHP_HCLSTHRESHOLD) Register Mask  */

/* -------- UHP_HCRHDESCRIPTORA : (UHP Offset: 0x48) (R/W 32) HC Root Hub A Register -------- */
#define UHP_HCRHDESCRIPTORA_NDP_Pos           (0U)                                           /**< (UHP_HCRHDESCRIPTORA) Number of downstream ports (read-only) Position */
#define UHP_HCRHDESCRIPTORA_NDP_Msk           (0xFFU << UHP_HCRHDESCRIPTORA_NDP_Pos)         /**< (UHP_HCRHDESCRIPTORA) Number of downstream ports (read-only) Mask */
#define UHP_HCRHDESCRIPTORA_NDP(value)        (UHP_HCRHDESCRIPTORA_NDP_Msk & ((value) << UHP_HCRHDESCRIPTORA_NDP_Pos))
#define UHP_HCRHDESCRIPTORA_PSM_Pos           (8U)                                           /**< (UHP_HCRHDESCRIPTORA) Power switching mode (read/write) Position */
#define UHP_HCRHDESCRIPTORA_PSM_Msk           (0x1U << UHP_HCRHDESCRIPTORA_PSM_Pos)          /**< (UHP_HCRHDESCRIPTORA) Power switching mode (read/write) Mask */
#define UHP_HCRHDESCRIPTORA_PSM(value)        (UHP_HCRHDESCRIPTORA_PSM_Msk & ((value) << UHP_HCRHDESCRIPTORA_PSM_Pos))
#define UHP_HCRHDESCRIPTORA_NPS_Pos           (9U)                                           /**< (UHP_HCRHDESCRIPTORA) No power switching (read/write) Position */
#define UHP_HCRHDESCRIPTORA_NPS_Msk           (0x1U << UHP_HCRHDESCRIPTORA_NPS_Pos)          /**< (UHP_HCRHDESCRIPTORA) No power switching (read/write) Mask */
#define UHP_HCRHDESCRIPTORA_NPS(value)        (UHP_HCRHDESCRIPTORA_NPS_Msk & ((value) << UHP_HCRHDESCRIPTORA_NPS_Pos))
#define UHP_HCRHDESCRIPTORA_DT_Pos            (10U)                                          /**< (UHP_HCRHDESCRIPTORA) Device type (read-only) Position */
#define UHP_HCRHDESCRIPTORA_DT_Msk            (0x1U << UHP_HCRHDESCRIPTORA_DT_Pos)           /**< (UHP_HCRHDESCRIPTORA) Device type (read-only) Mask */
#define UHP_HCRHDESCRIPTORA_DT(value)         (UHP_HCRHDESCRIPTORA_DT_Msk & ((value) << UHP_HCRHDESCRIPTORA_DT_Pos))
#define UHP_HCRHDESCRIPTORA_OCPM_Pos          (11U)                                          /**< (UHP_HCRHDESCRIPTORA) Overcurrent protection mode (read/write) Position */
#define UHP_HCRHDESCRIPTORA_OCPM_Msk          (0x1U << UHP_HCRHDESCRIPTORA_OCPM_Pos)         /**< (UHP_HCRHDESCRIPTORA) Overcurrent protection mode (read/write) Mask */
#define UHP_HCRHDESCRIPTORA_OCPM(value)       (UHP_HCRHDESCRIPTORA_OCPM_Msk & ((value) << UHP_HCRHDESCRIPTORA_OCPM_Pos))
#define UHP_HCRHDESCRIPTORA_NOCP_Pos          (12U)                                          /**< (UHP_HCRHDESCRIPTORA) No overcurrent protection (read/write) Position */
#define UHP_HCRHDESCRIPTORA_NOCP_Msk          (0x1U << UHP_HCRHDESCRIPTORA_NOCP_Pos)         /**< (UHP_HCRHDESCRIPTORA) No overcurrent protection (read/write) Mask */
#define UHP_HCRHDESCRIPTORA_NOCP(value)       (UHP_HCRHDESCRIPTORA_NOCP_Msk & ((value) << UHP_HCRHDESCRIPTORA_NOCP_Pos))
#define UHP_HCRHDESCRIPTORA_POTPG_Pos         (24U)                                          /**< (UHP_HCRHDESCRIPTORA) Power-on to power-good time (read/write) Position */
#define UHP_HCRHDESCRIPTORA_POTPG_Msk         (0xFFU << UHP_HCRHDESCRIPTORA_POTPG_Pos)       /**< (UHP_HCRHDESCRIPTORA) Power-on to power-good time (read/write) Mask */
#define UHP_HCRHDESCRIPTORA_POTPG(value)      (UHP_HCRHDESCRIPTORA_POTPG_Msk & ((value) << UHP_HCRHDESCRIPTORA_POTPG_Pos))
#define UHP_HCRHDESCRIPTORA_Msk               (0xFF001FFFUL)                                 /**< (UHP_HCRHDESCRIPTORA) Register Mask  */

/* -------- UHP_HCRHDESCRIPTORB : (UHP Offset: 0x4C) (R/W 32) HC Root Hub B Register -------- */
#define UHP_HCRHDESCRIPTORB_DR0_Pos           (0U)                                           /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR0_Msk           (0x1U << UHP_HCRHDESCRIPTORB_DR0_Pos)          /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR0(value)        (UHP_HCRHDESCRIPTORB_DR0_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR0_Pos))
#define UHP_HCRHDESCRIPTORB_DR1_Pos           (1U)                                           /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR1_Msk           (0x1U << UHP_HCRHDESCRIPTORB_DR1_Pos)          /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR1(value)        (UHP_HCRHDESCRIPTORB_DR1_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR1_Pos))
#define UHP_HCRHDESCRIPTORB_DR2_Pos           (2U)                                           /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR2_Msk           (0x1U << UHP_HCRHDESCRIPTORB_DR2_Pos)          /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR2(value)        (UHP_HCRHDESCRIPTORB_DR2_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR2_Pos))
#define UHP_HCRHDESCRIPTORB_DR3_Pos           (3U)                                           /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR3_Msk           (0x1U << UHP_HCRHDESCRIPTORB_DR3_Pos)          /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR3(value)        (UHP_HCRHDESCRIPTORB_DR3_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR3_Pos))
#define UHP_HCRHDESCRIPTORB_DR4_Pos           (4U)                                           /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR4_Msk           (0x1U << UHP_HCRHDESCRIPTORB_DR4_Pos)          /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR4(value)        (UHP_HCRHDESCRIPTORB_DR4_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR4_Pos))
#define UHP_HCRHDESCRIPTORB_DR5_Pos           (5U)                                           /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR5_Msk           (0x1U << UHP_HCRHDESCRIPTORB_DR5_Pos)          /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR5(value)        (UHP_HCRHDESCRIPTORB_DR5_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR5_Pos))
#define UHP_HCRHDESCRIPTORB_DR6_Pos           (6U)                                           /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR6_Msk           (0x1U << UHP_HCRHDESCRIPTORB_DR6_Pos)          /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR6(value)        (UHP_HCRHDESCRIPTORB_DR6_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR6_Pos))
#define UHP_HCRHDESCRIPTORB_DR7_Pos           (7U)                                           /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR7_Msk           (0x1U << UHP_HCRHDESCRIPTORB_DR7_Pos)          /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR7(value)        (UHP_HCRHDESCRIPTORB_DR7_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR7_Pos))
#define UHP_HCRHDESCRIPTORB_DR8_Pos           (8U)                                           /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR8_Msk           (0x1U << UHP_HCRHDESCRIPTORB_DR8_Pos)          /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR8(value)        (UHP_HCRHDESCRIPTORB_DR8_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR8_Pos))
#define UHP_HCRHDESCRIPTORB_DR9_Pos           (9U)                                           /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR9_Msk           (0x1U << UHP_HCRHDESCRIPTORB_DR9_Pos)          /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR9(value)        (UHP_HCRHDESCRIPTORB_DR9_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR9_Pos))
#define UHP_HCRHDESCRIPTORB_DR10_Pos          (10U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR10_Msk          (0x1U << UHP_HCRHDESCRIPTORB_DR10_Pos)         /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR10(value)       (UHP_HCRHDESCRIPTORB_DR10_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR10_Pos))
#define UHP_HCRHDESCRIPTORB_DR11_Pos          (11U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR11_Msk          (0x1U << UHP_HCRHDESCRIPTORB_DR11_Pos)         /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR11(value)       (UHP_HCRHDESCRIPTORB_DR11_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR11_Pos))
#define UHP_HCRHDESCRIPTORB_DR12_Pos          (12U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR12_Msk          (0x1U << UHP_HCRHDESCRIPTORB_DR12_Pos)         /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR12(value)       (UHP_HCRHDESCRIPTORB_DR12_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR12_Pos))
#define UHP_HCRHDESCRIPTORB_DR13_Pos          (13U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR13_Msk          (0x1U << UHP_HCRHDESCRIPTORB_DR13_Pos)         /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR13(value)       (UHP_HCRHDESCRIPTORB_DR13_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR13_Pos))
#define UHP_HCRHDESCRIPTORB_DR14_Pos          (14U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR14_Msk          (0x1U << UHP_HCRHDESCRIPTORB_DR14_Pos)         /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR14(value)       (UHP_HCRHDESCRIPTORB_DR14_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR14_Pos))
#define UHP_HCRHDESCRIPTORB_DR15_Pos          (15U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_DR15_Msk          (0x1U << UHP_HCRHDESCRIPTORB_DR15_Pos)         /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_DR15(value)       (UHP_HCRHDESCRIPTORB_DR15_Msk & ((value) << UHP_HCRHDESCRIPTORB_DR15_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM0_Pos         (16U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM0_Msk         (0x1U << UHP_HCRHDESCRIPTORB_PPCM0_Pos)        /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM0(value)      (UHP_HCRHDESCRIPTORB_PPCM0_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM0_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM1_Pos         (17U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM1_Msk         (0x1U << UHP_HCRHDESCRIPTORB_PPCM1_Pos)        /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM1(value)      (UHP_HCRHDESCRIPTORB_PPCM1_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM1_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM2_Pos         (18U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM2_Msk         (0x1U << UHP_HCRHDESCRIPTORB_PPCM2_Pos)        /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM2(value)      (UHP_HCRHDESCRIPTORB_PPCM2_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM2_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM3_Pos         (19U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM3_Msk         (0x1U << UHP_HCRHDESCRIPTORB_PPCM3_Pos)        /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM3(value)      (UHP_HCRHDESCRIPTORB_PPCM3_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM3_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM4_Pos         (20U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM4_Msk         (0x1U << UHP_HCRHDESCRIPTORB_PPCM4_Pos)        /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM4(value)      (UHP_HCRHDESCRIPTORB_PPCM4_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM4_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM5_Pos         (21U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM5_Msk         (0x1U << UHP_HCRHDESCRIPTORB_PPCM5_Pos)        /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM5(value)      (UHP_HCRHDESCRIPTORB_PPCM5_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM5_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM6_Pos         (22U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM6_Msk         (0x1U << UHP_HCRHDESCRIPTORB_PPCM6_Pos)        /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM6(value)      (UHP_HCRHDESCRIPTORB_PPCM6_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM6_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM7_Pos         (23U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM7_Msk         (0x1U << UHP_HCRHDESCRIPTORB_PPCM7_Pos)        /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM7(value)      (UHP_HCRHDESCRIPTORB_PPCM7_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM7_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM8_Pos         (24U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM8_Msk         (0x1U << UHP_HCRHDESCRIPTORB_PPCM8_Pos)        /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM8(value)      (UHP_HCRHDESCRIPTORB_PPCM8_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM8_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM9_Pos         (25U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM9_Msk         (0x1U << UHP_HCRHDESCRIPTORB_PPCM9_Pos)        /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM9(value)      (UHP_HCRHDESCRIPTORB_PPCM9_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM9_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM10_Pos        (26U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM10_Msk        (0x1U << UHP_HCRHDESCRIPTORB_PPCM10_Pos)       /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM10(value)     (UHP_HCRHDESCRIPTORB_PPCM10_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM10_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM11_Pos        (27U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM11_Msk        (0x1U << UHP_HCRHDESCRIPTORB_PPCM11_Pos)       /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM11(value)     (UHP_HCRHDESCRIPTORB_PPCM11_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM11_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM12_Pos        (28U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM12_Msk        (0x1U << UHP_HCRHDESCRIPTORB_PPCM12_Pos)       /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM12(value)     (UHP_HCRHDESCRIPTORB_PPCM12_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM12_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM13_Pos        (29U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM13_Msk        (0x1U << UHP_HCRHDESCRIPTORB_PPCM13_Pos)       /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM13(value)     (UHP_HCRHDESCRIPTORB_PPCM13_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM13_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM14_Pos        (30U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM14_Msk        (0x1U << UHP_HCRHDESCRIPTORB_PPCM14_Pos)       /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM14(value)     (UHP_HCRHDESCRIPTORB_PPCM14_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM14_Pos))
#define UHP_HCRHDESCRIPTORB_PPCM15_Pos        (31U)                                          /**< (UHP_HCRHDESCRIPTORB)  Position */
#define UHP_HCRHDESCRIPTORB_PPCM15_Msk        (0x1U << UHP_HCRHDESCRIPTORB_PPCM15_Pos)       /**< (UHP_HCRHDESCRIPTORB)  Mask */
#define UHP_HCRHDESCRIPTORB_PPCM15(value)     (UHP_HCRHDESCRIPTORB_PPCM15_Msk & ((value) << UHP_HCRHDESCRIPTORB_PPCM15_Pos))
#define UHP_HCRHDESCRIPTORB_Msk               (0xFFFFFFFFUL)                                 /**< (UHP_HCRHDESCRIPTORB) Register Mask  */

/* -------- UHP_HCRHSTATUS : (UHP Offset: 0x50) (R/W 32) HC Root Hub Status Register -------- */
#define UHP_HCRHSTATUS_LPS_Pos                (0U)                                           /**< (UHP_HCRHSTATUS) Local power status (read/write) Position */
#define UHP_HCRHSTATUS_LPS_Msk                (0x1U << UHP_HCRHSTATUS_LPS_Pos)               /**< (UHP_HCRHSTATUS) Local power status (read/write) Mask */
#define UHP_HCRHSTATUS_LPS(value)             (UHP_HCRHSTATUS_LPS_Msk & ((value) << UHP_HCRHSTATUS_LPS_Pos))
#define UHP_HCRHSTATUS_OCI_Pos                (1U)                                           /**< (UHP_HCRHSTATUS) Overcurrent indicator (read-only) Position */
#define UHP_HCRHSTATUS_OCI_Msk                (0x1U << UHP_HCRHSTATUS_OCI_Pos)               /**< (UHP_HCRHSTATUS) Overcurrent indicator (read-only) Mask */
#define UHP_HCRHSTATUS_OCI(value)             (UHP_HCRHSTATUS_OCI_Msk & ((value) << UHP_HCRHSTATUS_OCI_Pos))
#define UHP_HCRHSTATUS_DRWE_Pos               (15U)                                          /**< (UHP_HCRHSTATUS) Device remote wake-up enable (read/write) Position */
#define UHP_HCRHSTATUS_DRWE_Msk               (0x1U << UHP_HCRHSTATUS_DRWE_Pos)              /**< (UHP_HCRHSTATUS) Device remote wake-up enable (read/write) Mask */
#define UHP_HCRHSTATUS_DRWE(value)            (UHP_HCRHSTATUS_DRWE_Msk & ((value) << UHP_HCRHSTATUS_DRWE_Pos))
#define UHP_HCRHSTATUS_LPSC_Pos               (16U)                                          /**< (UHP_HCRHSTATUS) Local power status change (read/write) Position */
#define UHP_HCRHSTATUS_LPSC_Msk               (0x1U << UHP_HCRHSTATUS_LPSC_Pos)              /**< (UHP_HCRHSTATUS) Local power status change (read/write) Mask */
#define UHP_HCRHSTATUS_LPSC(value)            (UHP_HCRHSTATUS_LPSC_Msk & ((value) << UHP_HCRHSTATUS_LPSC_Pos))
#define UHP_HCRHSTATUS_OCIC_Pos               (17U)                                          /**< (UHP_HCRHSTATUS) Overcurrent indication change (read/write) Position */
#define UHP_HCRHSTATUS_OCIC_Msk               (0x1U << UHP_HCRHSTATUS_OCIC_Pos)              /**< (UHP_HCRHSTATUS) Overcurrent indication change (read/write) Mask */
#define UHP_HCRHSTATUS_OCIC(value)            (UHP_HCRHSTATUS_OCIC_Msk & ((value) << UHP_HCRHSTATUS_OCIC_Pos))
#define UHP_HCRHSTATUS_CRWE_Pos               (31U)                                          /**< (UHP_HCRHSTATUS) Clear remote wake-up enable (read/write) Position */
#define UHP_HCRHSTATUS_CRWE_Msk               (0x1U << UHP_HCRHSTATUS_CRWE_Pos)              /**< (UHP_HCRHSTATUS) Clear remote wake-up enable (read/write) Mask */
#define UHP_HCRHSTATUS_CRWE(value)            (UHP_HCRHSTATUS_CRWE_Msk & ((value) << UHP_HCRHSTATUS_CRWE_Pos))
#define UHP_HCRHSTATUS_Msk                    (0x80038003UL)                                 /**< (UHP_HCRHSTATUS) Register Mask  */

/* -------- UHP_HCRHPORTSTATUS : (UHP Offset: 0x54) (R/W 32) HC Port 1 Status and Control Register 0 -------- */
#define UHP_HCRHPORTSTATUS_CCS_CPE_Pos        (0U)                                           /**< (UHP_HCRHPORTSTATUS)  Position */
#define UHP_HCRHPORTSTATUS_CCS_CPE_Msk        (0x1U << UHP_HCRHPORTSTATUS_CCS_CPE_Pos)       /**< (UHP_HCRHPORTSTATUS)  Mask */
#define UHP_HCRHPORTSTATUS_CCS_CPE(value)     (UHP_HCRHPORTSTATUS_CCS_CPE_Msk & ((value) << UHP_HCRHPORTSTATUS_CCS_CPE_Pos))
#define UHP_HCRHPORTSTATUS_PES_SPE_Pos        (1U)                                           /**< (UHP_HCRHPORTSTATUS)  Position */
#define UHP_HCRHPORTSTATUS_PES_SPE_Msk        (0x1U << UHP_HCRHPORTSTATUS_PES_SPE_Pos)       /**< (UHP_HCRHPORTSTATUS)  Mask */
#define UHP_HCRHPORTSTATUS_PES_SPE(value)     (UHP_HCRHPORTSTATUS_PES_SPE_Msk & ((value) << UHP_HCRHPORTSTATUS_PES_SPE_Pos))
#define UHP_HCRHPORTSTATUS_PSS_SPS_Pos        (2U)                                           /**< (UHP_HCRHPORTSTATUS)  Position */
#define UHP_HCRHPORTSTATUS_PSS_SPS_Msk        (0x1U << UHP_HCRHPORTSTATUS_PSS_SPS_Pos)       /**< (UHP_HCRHPORTSTATUS)  Mask */
#define UHP_HCRHPORTSTATUS_PSS_SPS(value)     (UHP_HCRHPORTSTATUS_PSS_SPS_Msk & ((value) << UHP_HCRHPORTSTATUS_PSS_SPS_Pos))
#define UHP_HCRHPORTSTATUS_POCI_CSS_Pos       (3U)                                           /**< (UHP_HCRHPORTSTATUS)  Position */
#define UHP_HCRHPORTSTATUS_POCI_CSS_Msk       (0x1U << UHP_HCRHPORTSTATUS_POCI_CSS_Pos)      /**< (UHP_HCRHPORTSTATUS)  Mask */
#define UHP_HCRHPORTSTATUS_POCI_CSS(value)    (UHP_HCRHPORTSTATUS_POCI_CSS_Msk & ((value) << UHP_HCRHPORTSTATUS_POCI_CSS_Pos))
#define UHP_HCRHPORTSTATUS_PRS_SPR_Pos        (4U)                                           /**< (UHP_HCRHPORTSTATUS)  Position */
#define UHP_HCRHPORTSTATUS_PRS_SPR_Msk        (0x1U << UHP_HCRHPORTSTATUS_PRS_SPR_Pos)       /**< (UHP_HCRHPORTSTATUS)  Mask */
#define UHP_HCRHPORTSTATUS_PRS_SPR(value)     (UHP_HCRHPORTSTATUS_PRS_SPR_Msk & ((value) << UHP_HCRHPORTSTATUS_PRS_SPR_Pos))
#define UHP_HCRHPORTSTATUS_PPS_SPP_Pos        (8U)                                           /**< (UHP_HCRHPORTSTATUS)  Position */
#define UHP_HCRHPORTSTATUS_PPS_SPP_Msk        (0x1U << UHP_HCRHPORTSTATUS_PPS_SPP_Pos)       /**< (UHP_HCRHPORTSTATUS)  Mask */
#define UHP_HCRHPORTSTATUS_PPS_SPP(value)     (UHP_HCRHPORTSTATUS_PPS_SPP_Msk & ((value) << UHP_HCRHPORTSTATUS_PPS_SPP_Pos))
#define UHP_HCRHPORTSTATUS_LSDA_CPP_Pos       (9U)                                           /**< (UHP_HCRHPORTSTATUS)  Position */
#define UHP_HCRHPORTSTATUS_LSDA_CPP_Msk       (0x1U << UHP_HCRHPORTSTATUS_LSDA_CPP_Pos)      /**< (UHP_HCRHPORTSTATUS)  Mask */
#define UHP_HCRHPORTSTATUS_LSDA_CPP(value)    (UHP_HCRHPORTSTATUS_LSDA_CPP_Msk & ((value) << UHP_HCRHPORTSTATUS_LSDA_CPP_Pos))
#define UHP_HCRHPORTSTATUS_CSC_Pos            (16U)                                          /**< (UHP_HCRHPORTSTATUS) Port 1 connect status change (read/write, write '1' to clear) Position */
#define UHP_HCRHPORTSTATUS_CSC_Msk            (0x1U << UHP_HCRHPORTSTATUS_CSC_Pos)           /**< (UHP_HCRHPORTSTATUS) Port 1 connect status change (read/write, write '1' to clear) Mask */
#define UHP_HCRHPORTSTATUS_CSC(value)         (UHP_HCRHPORTSTATUS_CSC_Msk & ((value) << UHP_HCRHPORTSTATUS_CSC_Pos))
#define UHP_HCRHPORTSTATUS_PESC_Pos           (17U)                                          /**< (UHP_HCRHPORTSTATUS) Port 1 enable status change (read/write, write '1' to clear) Position */
#define UHP_HCRHPORTSTATUS_PESC_Msk           (0x1U << UHP_HCRHPORTSTATUS_PESC_Pos)          /**< (UHP_HCRHPORTSTATUS) Port 1 enable status change (read/write, write '1' to clear) Mask */
#define UHP_HCRHPORTSTATUS_PESC(value)        (UHP_HCRHPORTSTATUS_PESC_Msk & ((value) << UHP_HCRHPORTSTATUS_PESC_Pos))
#define UHP_HCRHPORTSTATUS_PSSC_Pos           (18U)                                          /**< (UHP_HCRHPORTSTATUS) Port 1 suspend status change (read/write, write '1' to clear) Position */
#define UHP_HCRHPORTSTATUS_PSSC_Msk           (0x1U << UHP_HCRHPORTSTATUS_PSSC_Pos)          /**< (UHP_HCRHPORTSTATUS) Port 1 suspend status change (read/write, write '1' to clear) Mask */
#define UHP_HCRHPORTSTATUS_PSSC(value)        (UHP_HCRHPORTSTATUS_PSSC_Msk & ((value) << UHP_HCRHPORTSTATUS_PSSC_Pos))
#define UHP_HCRHPORTSTATUS_OCIC_Pos           (19U)                                          /**< (UHP_HCRHPORTSTATUS) Port 1 overcurrent indicator change (read/write) Position */
#define UHP_HCRHPORTSTATUS_OCIC_Msk           (0x1U << UHP_HCRHPORTSTATUS_OCIC_Pos)          /**< (UHP_HCRHPORTSTATUS) Port 1 overcurrent indicator change (read/write) Mask */
#define UHP_HCRHPORTSTATUS_OCIC(value)        (UHP_HCRHPORTSTATUS_OCIC_Msk & ((value) << UHP_HCRHPORTSTATUS_OCIC_Pos))
#define UHP_HCRHPORTSTATUS_PRSC_Pos           (20U)                                          /**< (UHP_HCRHPORTSTATUS) Port 1 reset status change (read/write, write '1' to clear) Position */
#define UHP_HCRHPORTSTATUS_PRSC_Msk           (0x1U << UHP_HCRHPORTSTATUS_PRSC_Pos)          /**< (UHP_HCRHPORTSTATUS) Port 1 reset status change (read/write, write '1' to clear) Mask */
#define UHP_HCRHPORTSTATUS_PRSC(value)        (UHP_HCRHPORTSTATUS_PRSC_Msk & ((value) << UHP_HCRHPORTSTATUS_PRSC_Pos))
#define UHP_HCRHPORTSTATUS_Msk                (0x001F031FUL)                                 /**< (UHP_HCRHPORTSTATUS) Register Mask  */

/** \brief UHP register offsets definitions */
#define UHP_HCREVISION_OFFSET          (0x00)         /**< (UHP_HCREVISION) OHCI Revision Number Register Offset */
#define UHP_HCCONTROL_OFFSET           (0x04)         /**< (UHP_HCCONTROL) HC Operating Mode Register Offset */
#define UHP_HCCOMMANDSTATUS_OFFSET     (0x08)         /**< (UHP_HCCOMMANDSTATUS) HC Command and Status Register Offset */
#define UHP_HCINTERRUPTSTATUS_OFFSET   (0x0C)         /**< (UHP_HCINTERRUPTSTATUS) HC Interrupt and Status Register Offset */
#define UHP_HCINTERRUPTENABLE_OFFSET   (0x10)         /**< (UHP_HCINTERRUPTENABLE) HC Interrupt Enable Register Offset */
#define UHP_HCINTERRUPTDISABLE_OFFSET  (0x14)         /**< (UHP_HCINTERRUPTDISABLE) HC Interrupt Disable Register Offset */
#define UHP_HCHCCA_OFFSET              (0x18)         /**< (UHP_HCHCCA) HC HCCA Address Register Offset */
#define UHP_HCPERIODCURRENTED_OFFSET   (0x1C)         /**< (UHP_HCPERIODCURRENTED) HC Current Periodic Register Offset */
#define UHP_HCCONTROLHEADED_OFFSET     (0x20)         /**< (UHP_HCCONTROLHEADED) HC Head Control Register Offset */
#define UHP_HCCONTROLCURRENTED_OFFSET  (0x24)         /**< (UHP_HCCONTROLCURRENTED) HC Current Control Register Offset */
#define UHP_HCBULKHEADED_OFFSET        (0x28)         /**< (UHP_HCBULKHEADED) HC Head Bulk Register Offset */
#define UHP_HCBULKCURRENTED_OFFSET     (0x2C)         /**< (UHP_HCBULKCURRENTED) HC Current Bulk Register Offset */
#define UHP_HCDONEHEAD_OFFSET          (0x30)         /**< (UHP_HCDONEHEAD) HC Head Done Register Offset */
#define UHP_HCFMINTERVAL_OFFSET        (0x34)         /**< (UHP_HCFMINTERVAL) HC Frame Interval Register Offset */
#define UHP_HCFMREMAINING_OFFSET       (0x38)         /**< (UHP_HCFMREMAINING) HC Frame Remaining Register Offset */
#define UHP_HCFMNUMBER_OFFSET          (0x3C)         /**< (UHP_HCFMNUMBER) HC Frame Number Register Offset */
#define UHP_HCPERIODICSTART_OFFSET     (0x40)         /**< (UHP_HCPERIODICSTART) HC Periodic Start Register Offset */
#define UHP_HCLSTHRESHOLD_OFFSET       (0x44)         /**< (UHP_HCLSTHRESHOLD) HC Low-Speed Threshold Register Offset */
#define UHP_HCRHDESCRIPTORA_OFFSET     (0x48)         /**< (UHP_HCRHDESCRIPTORA) HC Root Hub A Register Offset */
#define UHP_HCRHDESCRIPTORB_OFFSET     (0x4C)         /**< (UHP_HCRHDESCRIPTORB) HC Root Hub B Register Offset */
#define UHP_HCRHSTATUS_OFFSET          (0x50)         /**< (UHP_HCRHSTATUS) HC Root Hub Status Register Offset */
#define UHP_HCRHPORTSTATUS_OFFSET      (0x54)         /**< (UHP_HCRHPORTSTATUS) HC Port 1 Status and Control Register 0 Offset */

/** \brief UHP register API structure */
typedef struct
{
  __I   uint32_t                       UHP_HCREVISION;  /**< Offset: 0x00 (R/   32) OHCI Revision Number Register */
  __IO  uint32_t                       UHP_HCCONTROL;   /**< Offset: 0x04 (R/W  32) HC Operating Mode Register */
  __IO  uint32_t                       UHP_HCCOMMANDSTATUS; /**< Offset: 0x08 (R/W  32) HC Command and Status Register */
  __IO  uint32_t                       UHP_HCINTERRUPTSTATUS; /**< Offset: 0x0c (R/W  32) HC Interrupt and Status Register */
  __IO  uint32_t                       UHP_HCINTERRUPTENABLE; /**< Offset: 0x10 (R/W  32) HC Interrupt Enable Register */
  __IO  uint32_t                       UHP_HCINTERRUPTDISABLE; /**< Offset: 0x14 (R/W  32) HC Interrupt Disable Register */
  __IO  uint32_t                       UHP_HCHCCA;      /**< Offset: 0x18 (R/W  32) HC HCCA Address Register */
  __I   uint32_t                       UHP_HCPERIODCURRENTED; /**< Offset: 0x1c (R/   32) HC Current Periodic Register */
  __IO  uint32_t                       UHP_HCCONTROLHEADED; /**< Offset: 0x20 (R/W  32) HC Head Control Register */
  __IO  uint32_t                       UHP_HCCONTROLCURRENTED; /**< Offset: 0x24 (R/W  32) HC Current Control Register */
  __IO  uint32_t                       UHP_HCBULKHEADED; /**< Offset: 0x28 (R/W  32) HC Head Bulk Register */
  __IO  uint32_t                       UHP_HCBULKCURRENTED; /**< Offset: 0x2c (R/W  32) HC Current Bulk Register */
  __I   uint32_t                       UHP_HCDONEHEAD;  /**< Offset: 0x30 (R/   32) HC Head Done Register */
  __IO  uint32_t                       UHP_HCFMINTERVAL; /**< Offset: 0x34 (R/W  32) HC Frame Interval Register */
  __I   uint32_t                       UHP_HCFMREMAINING; /**< Offset: 0x38 (R/   32) HC Frame Remaining Register */
  __I   uint32_t                       UHP_HCFMNUMBER;  /**< Offset: 0x3c (R/   32) HC Frame Number Register */
  __IO  uint32_t                       UHP_HCPERIODICSTART; /**< Offset: 0x40 (R/W  32) HC Periodic Start Register */
  __IO  uint32_t                       UHP_HCLSTHRESHOLD; /**< Offset: 0x44 (R/W  32) HC Low-Speed Threshold Register */
  __IO  uint32_t                       UHP_HCRHDESCRIPTORA; /**< Offset: 0x48 (R/W  32) HC Root Hub A Register */
  __IO  uint32_t                       UHP_HCRHDESCRIPTORB; /**< Offset: 0x4c (R/W  32) HC Root Hub B Register */
  __IO  uint32_t                       UHP_HCRHSTATUS;  /**< Offset: 0x50 (R/W  32) HC Root Hub Status Register */
  __IO  uint32_t                       UHP_HCRHPORTSTATUS[2]; /**< Offset: 0x54 (R/W  32) HC Port 1 Status and Control Register 0 */
} uhp_registers_t;
/** @}  end of USB Host Port */

#endif /* SAMG_SAMG55_UHP_MODULE_H */

