/**
 * \brief Header file for SAMC/SAMC21 PM
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
#ifndef SAMC_SAMC21_PM_MODULE_H
#define SAMC_SAMC21_PM_MODULE_H

/** \addtogroup SAMC_SAMC21 Power Manager
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_PM                                    */
/* ========================================================================== */

/* -------- PM_SLEEPCFG : (PM Offset: 0x01) (R/W 8) Sleep Configuration -------- */
#define PM_SLEEPCFG_SLEEPMODE_Pos             (0U)                                           /**< (PM_SLEEPCFG) Sleep Mode Position */
#define PM_SLEEPCFG_SLEEPMODE_Msk             (0x7U << PM_SLEEPCFG_SLEEPMODE_Pos)            /**< (PM_SLEEPCFG) Sleep Mode Mask */
#define PM_SLEEPCFG_SLEEPMODE(value)          (PM_SLEEPCFG_SLEEPMODE_Msk & ((value) << PM_SLEEPCFG_SLEEPMODE_Pos))
#define   PM_SLEEPCFG_SLEEPMODE_IDLE0_Val     (0U)                                           /**< (PM_SLEEPCFG) CPU clock is OFF  */
#define   PM_SLEEPCFG_SLEEPMODE_IDLE1_Val     (1U)                                           /**< (PM_SLEEPCFG) AHB clock is OFF  */
#define   PM_SLEEPCFG_SLEEPMODE_IDLE2_Val     (2U)                                           /**< (PM_SLEEPCFG) APB clock are OFF  */
#define   PM_SLEEPCFG_SLEEPMODE_STANDBY_Val   (4U)                                           /**< (PM_SLEEPCFG) All Clocks are OFF  */
#define   PM_SLEEPCFG_SLEEPMODE_BACKUP_Val    (5U)                                           /**< (PM_SLEEPCFG) Only Backup domain is powered ON  */
#define   PM_SLEEPCFG_SLEEPMODE_OFF_Val       (6U)                                           /**< (PM_SLEEPCFG) All power domains are powered OFF  */
#define PM_SLEEPCFG_SLEEPMODE_IDLE0           (PM_SLEEPCFG_SLEEPMODE_IDLE0_Val << PM_SLEEPCFG_SLEEPMODE_Pos) /**< (PM_SLEEPCFG) CPU clock is OFF Position  */
#define PM_SLEEPCFG_SLEEPMODE_IDLE1           (PM_SLEEPCFG_SLEEPMODE_IDLE1_Val << PM_SLEEPCFG_SLEEPMODE_Pos) /**< (PM_SLEEPCFG) AHB clock is OFF Position  */
#define PM_SLEEPCFG_SLEEPMODE_IDLE2           (PM_SLEEPCFG_SLEEPMODE_IDLE2_Val << PM_SLEEPCFG_SLEEPMODE_Pos) /**< (PM_SLEEPCFG) APB clock are OFF Position  */
#define PM_SLEEPCFG_SLEEPMODE_STANDBY         (PM_SLEEPCFG_SLEEPMODE_STANDBY_Val << PM_SLEEPCFG_SLEEPMODE_Pos) /**< (PM_SLEEPCFG) All Clocks are OFF Position  */
#define PM_SLEEPCFG_SLEEPMODE_BACKUP          (PM_SLEEPCFG_SLEEPMODE_BACKUP_Val << PM_SLEEPCFG_SLEEPMODE_Pos) /**< (PM_SLEEPCFG) Only Backup domain is powered ON Position  */
#define PM_SLEEPCFG_SLEEPMODE_OFF             (PM_SLEEPCFG_SLEEPMODE_OFF_Val << PM_SLEEPCFG_SLEEPMODE_Pos) /**< (PM_SLEEPCFG) All power domains are powered OFF Position  */
#define PM_SLEEPCFG_Msk                       (0x00000007UL)                                 /**< (PM_SLEEPCFG) Register Mask  */

/* -------- PM_STDBYCFG : (PM Offset: 0x08) (R/W 16) Standby Configuration -------- */
#define PM_STDBYCFG_VREGSMOD_Pos              (6U)                                           /**< (PM_STDBYCFG) Voltage Regulator Standby mode Position */
#define PM_STDBYCFG_VREGSMOD_Msk              (0x3U << PM_STDBYCFG_VREGSMOD_Pos)             /**< (PM_STDBYCFG) Voltage Regulator Standby mode Mask */
#define PM_STDBYCFG_VREGSMOD(value)           (PM_STDBYCFG_VREGSMOD_Msk & ((value) << PM_STDBYCFG_VREGSMOD_Pos))
#define   PM_STDBYCFG_VREGSMOD_AUTO_Val       (0U)                                           /**< (PM_STDBYCFG) Automatic mode  */
#define   PM_STDBYCFG_VREGSMOD_PERFORMANCE_Val (1U)                                           /**< (PM_STDBYCFG) Performance oriented  */
#define   PM_STDBYCFG_VREGSMOD_LP_Val         (2U)                                           /**< (PM_STDBYCFG) Low Power oriented  */
#define PM_STDBYCFG_VREGSMOD_AUTO             (PM_STDBYCFG_VREGSMOD_AUTO_Val << PM_STDBYCFG_VREGSMOD_Pos) /**< (PM_STDBYCFG) Automatic mode Position  */
#define PM_STDBYCFG_VREGSMOD_PERFORMANCE      (PM_STDBYCFG_VREGSMOD_PERFORMANCE_Val << PM_STDBYCFG_VREGSMOD_Pos) /**< (PM_STDBYCFG) Performance oriented Position  */
#define PM_STDBYCFG_VREGSMOD_LP               (PM_STDBYCFG_VREGSMOD_LP_Val << PM_STDBYCFG_VREGSMOD_Pos) /**< (PM_STDBYCFG) Low Power oriented Position  */
#define PM_STDBYCFG_BBIASHS_Pos               (10U)                                          /**< (PM_STDBYCFG) Back Bias for HMCRAMCHS Position */
#define PM_STDBYCFG_BBIASHS_Msk               (0x3U << PM_STDBYCFG_BBIASHS_Pos)              /**< (PM_STDBYCFG) Back Bias for HMCRAMCHS Mask */
#define PM_STDBYCFG_BBIASHS(value)            (PM_STDBYCFG_BBIASHS_Msk & ((value) << PM_STDBYCFG_BBIASHS_Pos))
#define PM_STDBYCFG_Msk                       (0x00000CC0UL)                                 /**< (PM_STDBYCFG) Register Mask  */

/** \brief PM register offsets definitions */
#define PM_SLEEPCFG_OFFSET             (0x01)         /**< (PM_SLEEPCFG) Sleep Configuration Offset */
#define PM_STDBYCFG_OFFSET             (0x08)         /**< (PM_STDBYCFG) Standby Configuration Offset */

/** \brief PM register API structure */
typedef struct
{
  __I   uint8_t                        Reserved1[0x01];
  __IO  uint8_t                        PM_SLEEPCFG;     /**< Offset: 0x01 (R/W  8) Sleep Configuration */
  __I   uint8_t                        Reserved2[0x06];
  __IO  uint16_t                       PM_STDBYCFG;     /**< Offset: 0x08 (R/W  16) Standby Configuration */
} pm_registers_t;
/** @}  end of Power Manager */

#endif /* SAMC_SAMC21_PM_MODULE_H */

