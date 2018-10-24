/**
 * \brief Header file for SAMC/SAMC21 NVMCTRL
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
#ifndef SAMC_SAMC21_NVMCTRL_MODULE_H
#define SAMC_SAMC21_NVMCTRL_MODULE_H

/** \addtogroup SAMC_SAMC21 Non-Volatile Memory Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_NVMCTRL                               */
/* ========================================================================== */

/* -------- NVMCTRL_CTRLA : (NVMCTRL Offset: 0x00) (R/W 16) Control A -------- */
#define NVMCTRL_CTRLA_CMD_Pos                 (0U)                                           /**< (NVMCTRL_CTRLA) Command Position */
#define NVMCTRL_CTRLA_CMD_Msk                 (0x7FU << NVMCTRL_CTRLA_CMD_Pos)               /**< (NVMCTRL_CTRLA) Command Mask */
#define NVMCTRL_CTRLA_CMD(value)              (NVMCTRL_CTRLA_CMD_Msk & ((value) << NVMCTRL_CTRLA_CMD_Pos))
#define   NVMCTRL_CTRLA_CMD_ER_Val            (2U)                                           /**< (NVMCTRL_CTRLA) Erase Row - Erases the row addressed by the ADDR register.  */
#define   NVMCTRL_CTRLA_CMD_WP_Val            (4U)                                           /**< (NVMCTRL_CTRLA) Write Page - Writes the contents of the page buffer to the page addressed by the ADDR register.  */
#define   NVMCTRL_CTRLA_CMD_EAR_Val           (5U)                                           /**< (NVMCTRL_CTRLA) Erase Auxiliary Row - Erases the auxiliary row addressed by the ADDR register. This command can be given only when the security bit is not set and only to the user configuration row.  */
#define   NVMCTRL_CTRLA_CMD_WAP_Val           (6U)                                           /**< (NVMCTRL_CTRLA) Write Auxiliary Page - Writes the contents of the page buffer to the page addressed by the ADDR register. This command can be given only when the security bit is not set and only to the user configuration row.  */
#define   NVMCTRL_CTRLA_CMD_SF_Val            (10U)                                          /**< (NVMCTRL_CTRLA) Security Flow Command  */
#define   NVMCTRL_CTRLA_CMD_WL_Val            (15U)                                          /**< (NVMCTRL_CTRLA) Write lockbits  */
#define   NVMCTRL_CTRLA_CMD_RWWEEER_Val       (26U)                                          /**< (NVMCTRL_CTRLA) RWW EEPROM area Erase Row - Erases the row addressed by the ADDR register.  */
#define   NVMCTRL_CTRLA_CMD_RWWEEWP_Val       (28U)                                          /**< (NVMCTRL_CTRLA) RWW EEPROM Write Page - Writes the contents of the page buffer to the page addressed by the ADDR register.  */
#define   NVMCTRL_CTRLA_CMD_LR_Val            (64U)                                          /**< (NVMCTRL_CTRLA) Lock Region - Locks the region containing the address location in the ADDR register.  */
#define   NVMCTRL_CTRLA_CMD_UR_Val            (65U)                                          /**< (NVMCTRL_CTRLA) Unlock Region - Unlocks the region containing the address location in the ADDR register.  */
#define   NVMCTRL_CTRLA_CMD_SPRM_Val          (66U)                                          /**< (NVMCTRL_CTRLA) Sets the power reduction mode.  */
#define   NVMCTRL_CTRLA_CMD_CPRM_Val          (67U)                                          /**< (NVMCTRL_CTRLA) Clears the power reduction mode.  */
#define   NVMCTRL_CTRLA_CMD_PBC_Val           (68U)                                          /**< (NVMCTRL_CTRLA) Page Buffer Clear - Clears the page buffer.  */
#define   NVMCTRL_CTRLA_CMD_SSB_Val           (69U)                                          /**< (NVMCTRL_CTRLA) Set Security Bit - Sets the security bit by writing 0x00 to the first byte in the lockbit row.  */
#define   NVMCTRL_CTRLA_CMD_INVALL_Val        (70U)                                          /**< (NVMCTRL_CTRLA) Invalidate all cache lines.  */
#define NVMCTRL_CTRLA_CMD_ER                  (NVMCTRL_CTRLA_CMD_ER_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Erase Row - Erases the row addressed by the ADDR register. Position  */
#define NVMCTRL_CTRLA_CMD_WP                  (NVMCTRL_CTRLA_CMD_WP_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Write Page - Writes the contents of the page buffer to the page addressed by the ADDR register. Position  */
#define NVMCTRL_CTRLA_CMD_EAR                 (NVMCTRL_CTRLA_CMD_EAR_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Erase Auxiliary Row - Erases the auxiliary row addressed by the ADDR register. This command can be given only when the security bit is not set and only to the user configuration row. Position  */
#define NVMCTRL_CTRLA_CMD_WAP                 (NVMCTRL_CTRLA_CMD_WAP_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Write Auxiliary Page - Writes the contents of the page buffer to the page addressed by the ADDR register. This command can be given only when the security bit is not set and only to the user configuration row. Position  */
#define NVMCTRL_CTRLA_CMD_SF                  (NVMCTRL_CTRLA_CMD_SF_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Security Flow Command Position  */
#define NVMCTRL_CTRLA_CMD_WL                  (NVMCTRL_CTRLA_CMD_WL_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Write lockbits Position  */
#define NVMCTRL_CTRLA_CMD_RWWEEER             (NVMCTRL_CTRLA_CMD_RWWEEER_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) RWW EEPROM area Erase Row - Erases the row addressed by the ADDR register. Position  */
#define NVMCTRL_CTRLA_CMD_RWWEEWP             (NVMCTRL_CTRLA_CMD_RWWEEWP_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) RWW EEPROM Write Page - Writes the contents of the page buffer to the page addressed by the ADDR register. Position  */
#define NVMCTRL_CTRLA_CMD_LR                  (NVMCTRL_CTRLA_CMD_LR_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Lock Region - Locks the region containing the address location in the ADDR register. Position  */
#define NVMCTRL_CTRLA_CMD_UR                  (NVMCTRL_CTRLA_CMD_UR_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Unlock Region - Unlocks the region containing the address location in the ADDR register. Position  */
#define NVMCTRL_CTRLA_CMD_SPRM                (NVMCTRL_CTRLA_CMD_SPRM_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Sets the power reduction mode. Position  */
#define NVMCTRL_CTRLA_CMD_CPRM                (NVMCTRL_CTRLA_CMD_CPRM_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Clears the power reduction mode. Position  */
#define NVMCTRL_CTRLA_CMD_PBC                 (NVMCTRL_CTRLA_CMD_PBC_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Page Buffer Clear - Clears the page buffer. Position  */
#define NVMCTRL_CTRLA_CMD_SSB                 (NVMCTRL_CTRLA_CMD_SSB_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Set Security Bit - Sets the security bit by writing 0x00 to the first byte in the lockbit row. Position  */
#define NVMCTRL_CTRLA_CMD_INVALL              (NVMCTRL_CTRLA_CMD_INVALL_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Invalidate all cache lines. Position  */
#define NVMCTRL_CTRLA_CMDEX_Pos               (8U)                                           /**< (NVMCTRL_CTRLA) Command Execution Position */
#define NVMCTRL_CTRLA_CMDEX_Msk               (0xFFU << NVMCTRL_CTRLA_CMDEX_Pos)             /**< (NVMCTRL_CTRLA) Command Execution Mask */
#define NVMCTRL_CTRLA_CMDEX(value)            (NVMCTRL_CTRLA_CMDEX_Msk & ((value) << NVMCTRL_CTRLA_CMDEX_Pos))
#define   NVMCTRL_CTRLA_CMDEX_KEY_Val         (165U)                                         /**< (NVMCTRL_CTRLA) Execution Key  */
#define NVMCTRL_CTRLA_CMDEX_KEY               (NVMCTRL_CTRLA_CMDEX_KEY_Val << NVMCTRL_CTRLA_CMDEX_Pos) /**< (NVMCTRL_CTRLA) Execution Key Position  */
#define NVMCTRL_CTRLA_Msk                     (0x0000FF7FUL)                                 /**< (NVMCTRL_CTRLA) Register Mask  */

/* -------- NVMCTRL_CTRLB : (NVMCTRL Offset: 0x04) (R/W 32) Control B -------- */
#define NVMCTRL_CTRLB_RWS_Pos                 (1U)                                           /**< (NVMCTRL_CTRLB) NVM Read Wait States Position */
#define NVMCTRL_CTRLB_RWS_Msk                 (0xFU << NVMCTRL_CTRLB_RWS_Pos)                /**< (NVMCTRL_CTRLB) NVM Read Wait States Mask */
#define NVMCTRL_CTRLB_RWS(value)              (NVMCTRL_CTRLB_RWS_Msk & ((value) << NVMCTRL_CTRLB_RWS_Pos))
#define   NVMCTRL_CTRLB_RWS_SINGLE_Val        (0U)                                           /**< (NVMCTRL_CTRLB) Single Auto Wait State  */
#define   NVMCTRL_CTRLB_RWS_HALF_Val          (1U)                                           /**< (NVMCTRL_CTRLB) Half Auto Wait State  */
#define   NVMCTRL_CTRLB_RWS_DUAL_Val          (2U)                                           /**< (NVMCTRL_CTRLB) Dual Auto Wait State  */
#define NVMCTRL_CTRLB_RWS_SINGLE              (NVMCTRL_CTRLB_RWS_SINGLE_Val << NVMCTRL_CTRLB_RWS_Pos) /**< (NVMCTRL_CTRLB) Single Auto Wait State Position  */
#define NVMCTRL_CTRLB_RWS_HALF                (NVMCTRL_CTRLB_RWS_HALF_Val << NVMCTRL_CTRLB_RWS_Pos) /**< (NVMCTRL_CTRLB) Half Auto Wait State Position  */
#define NVMCTRL_CTRLB_RWS_DUAL                (NVMCTRL_CTRLB_RWS_DUAL_Val << NVMCTRL_CTRLB_RWS_Pos) /**< (NVMCTRL_CTRLB) Dual Auto Wait State Position  */
#define NVMCTRL_CTRLB_MANW_Pos                (7U)                                           /**< (NVMCTRL_CTRLB) Manual Write Position */
#define NVMCTRL_CTRLB_MANW_Msk                (0x1U << NVMCTRL_CTRLB_MANW_Pos)               /**< (NVMCTRL_CTRLB) Manual Write Mask */
#define NVMCTRL_CTRLB_MANW(value)             (NVMCTRL_CTRLB_MANW_Msk & ((value) << NVMCTRL_CTRLB_MANW_Pos))
#define NVMCTRL_CTRLB_SLEEPPRM_Pos            (8U)                                           /**< (NVMCTRL_CTRLB) Power Reduction Mode during Sleep Position */
#define NVMCTRL_CTRLB_SLEEPPRM_Msk            (0x3U << NVMCTRL_CTRLB_SLEEPPRM_Pos)           /**< (NVMCTRL_CTRLB) Power Reduction Mode during Sleep Mask */
#define NVMCTRL_CTRLB_SLEEPPRM(value)         (NVMCTRL_CTRLB_SLEEPPRM_Msk & ((value) << NVMCTRL_CTRLB_SLEEPPRM_Pos))
#define   NVMCTRL_CTRLB_SLEEPPRM_WAKEONACCESS_Val (0U)                                           /**< (NVMCTRL_CTRLB) NVM block enters low-power mode when entering sleep.NVM block exits low-power mode upon first access.  */
#define   NVMCTRL_CTRLB_SLEEPPRM_WAKEUPINSTANT_Val (1U)                                           /**< (NVMCTRL_CTRLB) NVM block enters low-power mode when entering sleep.NVM block exits low-power mode when exiting sleep.  */
#define   NVMCTRL_CTRLB_SLEEPPRM_DISABLED_Val (3U)                                           /**< (NVMCTRL_CTRLB) Auto power reduction disabled.  */
#define NVMCTRL_CTRLB_SLEEPPRM_WAKEONACCESS   (NVMCTRL_CTRLB_SLEEPPRM_WAKEONACCESS_Val << NVMCTRL_CTRLB_SLEEPPRM_Pos) /**< (NVMCTRL_CTRLB) NVM block enters low-power mode when entering sleep.NVM block exits low-power mode upon first access. Position  */
#define NVMCTRL_CTRLB_SLEEPPRM_WAKEUPINSTANT  (NVMCTRL_CTRLB_SLEEPPRM_WAKEUPINSTANT_Val << NVMCTRL_CTRLB_SLEEPPRM_Pos) /**< (NVMCTRL_CTRLB) NVM block enters low-power mode when entering sleep.NVM block exits low-power mode when exiting sleep. Position  */
#define NVMCTRL_CTRLB_SLEEPPRM_DISABLED       (NVMCTRL_CTRLB_SLEEPPRM_DISABLED_Val << NVMCTRL_CTRLB_SLEEPPRM_Pos) /**< (NVMCTRL_CTRLB) Auto power reduction disabled. Position  */
#define NVMCTRL_CTRLB_READMODE_Pos            (16U)                                          /**< (NVMCTRL_CTRLB) NVMCTRL Read Mode Position */
#define NVMCTRL_CTRLB_READMODE_Msk            (0x3U << NVMCTRL_CTRLB_READMODE_Pos)           /**< (NVMCTRL_CTRLB) NVMCTRL Read Mode Mask */
#define NVMCTRL_CTRLB_READMODE(value)         (NVMCTRL_CTRLB_READMODE_Msk & ((value) << NVMCTRL_CTRLB_READMODE_Pos))
#define   NVMCTRL_CTRLB_READMODE_NO_MISS_PENALTY_Val (0U)                                           /**< (NVMCTRL_CTRLB) The NVM Controller (cache system) does not insert wait states on a cache miss. Gives the best system performance.  */
#define   NVMCTRL_CTRLB_READMODE_LOW_POWER_Val (1U)                                           /**< (NVMCTRL_CTRLB) Reduces power consumption of the cache system, but inserts a wait state each time there is a cache miss. This mode may not be relevant if CPU performance is required, as the application will be stalled and may lead to increase run time.  */
#define   NVMCTRL_CTRLB_READMODE_DETERMINISTIC_Val (2U)                                           /**< (NVMCTRL_CTRLB) The cache system ensures that a cache hit or miss takes the same amount of time, determined by the number of programmed flash wait states. This mode can be used for real-time applications that require deterministic execution timings.  */
#define NVMCTRL_CTRLB_READMODE_NO_MISS_PENALTY (NVMCTRL_CTRLB_READMODE_NO_MISS_PENALTY_Val << NVMCTRL_CTRLB_READMODE_Pos) /**< (NVMCTRL_CTRLB) The NVM Controller (cache system) does not insert wait states on a cache miss. Gives the best system performance. Position  */
#define NVMCTRL_CTRLB_READMODE_LOW_POWER      (NVMCTRL_CTRLB_READMODE_LOW_POWER_Val << NVMCTRL_CTRLB_READMODE_Pos) /**< (NVMCTRL_CTRLB) Reduces power consumption of the cache system, but inserts a wait state each time there is a cache miss. This mode may not be relevant if CPU performance is required, as the application will be stalled and may lead to increase run time. Position  */
#define NVMCTRL_CTRLB_READMODE_DETERMINISTIC  (NVMCTRL_CTRLB_READMODE_DETERMINISTIC_Val << NVMCTRL_CTRLB_READMODE_Pos) /**< (NVMCTRL_CTRLB) The cache system ensures that a cache hit or miss takes the same amount of time, determined by the number of programmed flash wait states. This mode can be used for real-time applications that require deterministic execution timings. Position  */
#define NVMCTRL_CTRLB_CACHEDIS_Pos            (18U)                                          /**< (NVMCTRL_CTRLB) Cache Disable Position */
#define NVMCTRL_CTRLB_CACHEDIS_Msk            (0x3U << NVMCTRL_CTRLB_CACHEDIS_Pos)           /**< (NVMCTRL_CTRLB) Cache Disable Mask */
#define NVMCTRL_CTRLB_CACHEDIS(value)         (NVMCTRL_CTRLB_CACHEDIS_Msk & ((value) << NVMCTRL_CTRLB_CACHEDIS_Pos))
#define NVMCTRL_CTRLB_Msk                     (0x000F039EUL)                                 /**< (NVMCTRL_CTRLB) Register Mask  */

/* -------- NVMCTRL_PARAM : (NVMCTRL Offset: 0x08) (R/W 32) NVM Parameter -------- */
#define NVMCTRL_PARAM_NVMP_Pos                (0U)                                           /**< (NVMCTRL_PARAM) NVM Pages Position */
#define NVMCTRL_PARAM_NVMP_Msk                (0xFFFFU << NVMCTRL_PARAM_NVMP_Pos)            /**< (NVMCTRL_PARAM) NVM Pages Mask */
#define NVMCTRL_PARAM_NVMP(value)             (NVMCTRL_PARAM_NVMP_Msk & ((value) << NVMCTRL_PARAM_NVMP_Pos))
#define NVMCTRL_PARAM_PSZ_Pos                 (16U)                                          /**< (NVMCTRL_PARAM) Page Size Position */
#define NVMCTRL_PARAM_PSZ_Msk                 (0x7U << NVMCTRL_PARAM_PSZ_Pos)                /**< (NVMCTRL_PARAM) Page Size Mask */
#define NVMCTRL_PARAM_PSZ(value)              (NVMCTRL_PARAM_PSZ_Msk & ((value) << NVMCTRL_PARAM_PSZ_Pos))
#define   NVMCTRL_PARAM_PSZ_8_Val             (0U)                                           /**< (NVMCTRL_PARAM) 8 bytes  */
#define   NVMCTRL_PARAM_PSZ_16_Val            (1U)                                           /**< (NVMCTRL_PARAM) 16 bytes  */
#define   NVMCTRL_PARAM_PSZ_32_Val            (2U)                                           /**< (NVMCTRL_PARAM) 32 bytes  */
#define   NVMCTRL_PARAM_PSZ_64_Val            (3U)                                           /**< (NVMCTRL_PARAM) 64 bytes  */
#define   NVMCTRL_PARAM_PSZ_128_Val           (4U)                                           /**< (NVMCTRL_PARAM) 128 bytes  */
#define   NVMCTRL_PARAM_PSZ_256_Val           (5U)                                           /**< (NVMCTRL_PARAM) 256 bytes  */
#define   NVMCTRL_PARAM_PSZ_512_Val           (6U)                                           /**< (NVMCTRL_PARAM) 512 bytes  */
#define   NVMCTRL_PARAM_PSZ_1024_Val          (7U)                                           /**< (NVMCTRL_PARAM) 1024 bytes  */
#define NVMCTRL_PARAM_PSZ_8                   (NVMCTRL_PARAM_PSZ_8_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 8 bytes Position  */
#define NVMCTRL_PARAM_PSZ_16                  (NVMCTRL_PARAM_PSZ_16_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 16 bytes Position  */
#define NVMCTRL_PARAM_PSZ_32                  (NVMCTRL_PARAM_PSZ_32_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 32 bytes Position  */
#define NVMCTRL_PARAM_PSZ_64                  (NVMCTRL_PARAM_PSZ_64_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 64 bytes Position  */
#define NVMCTRL_PARAM_PSZ_128                 (NVMCTRL_PARAM_PSZ_128_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 128 bytes Position  */
#define NVMCTRL_PARAM_PSZ_256                 (NVMCTRL_PARAM_PSZ_256_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 256 bytes Position  */
#define NVMCTRL_PARAM_PSZ_512                 (NVMCTRL_PARAM_PSZ_512_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 512 bytes Position  */
#define NVMCTRL_PARAM_PSZ_1024                (NVMCTRL_PARAM_PSZ_1024_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 1024 bytes Position  */
#define NVMCTRL_PARAM_RWWEEP_Pos              (20U)                                          /**< (NVMCTRL_PARAM) RWW EEPROM Pages Position */
#define NVMCTRL_PARAM_RWWEEP_Msk              (0xFFFU << NVMCTRL_PARAM_RWWEEP_Pos)           /**< (NVMCTRL_PARAM) RWW EEPROM Pages Mask */
#define NVMCTRL_PARAM_RWWEEP(value)           (NVMCTRL_PARAM_RWWEEP_Msk & ((value) << NVMCTRL_PARAM_RWWEEP_Pos))
#define NVMCTRL_PARAM_Msk                     (0xFFF7FFFFUL)                                 /**< (NVMCTRL_PARAM) Register Mask  */

/* -------- NVMCTRL_INTENCLR : (NVMCTRL Offset: 0x0C) (R/W 8) Interrupt Enable Clear -------- */
#define NVMCTRL_INTENCLR_READY_Pos            (0U)                                           /**< (NVMCTRL_INTENCLR) NVM Ready Interrupt Enable Position */
#define NVMCTRL_INTENCLR_READY_Msk            (0x1U << NVMCTRL_INTENCLR_READY_Pos)           /**< (NVMCTRL_INTENCLR) NVM Ready Interrupt Enable Mask */
#define NVMCTRL_INTENCLR_READY(value)         (NVMCTRL_INTENCLR_READY_Msk & ((value) << NVMCTRL_INTENCLR_READY_Pos))
#define NVMCTRL_INTENCLR_ERROR_Pos            (1U)                                           /**< (NVMCTRL_INTENCLR) Error Interrupt Enable Position */
#define NVMCTRL_INTENCLR_ERROR_Msk            (0x1U << NVMCTRL_INTENCLR_ERROR_Pos)           /**< (NVMCTRL_INTENCLR) Error Interrupt Enable Mask */
#define NVMCTRL_INTENCLR_ERROR(value)         (NVMCTRL_INTENCLR_ERROR_Msk & ((value) << NVMCTRL_INTENCLR_ERROR_Pos))
#define NVMCTRL_INTENCLR_Msk                  (0x00000003UL)                                 /**< (NVMCTRL_INTENCLR) Register Mask  */

/* -------- NVMCTRL_INTENSET : (NVMCTRL Offset: 0x10) (R/W 8) Interrupt Enable Set -------- */
#define NVMCTRL_INTENSET_READY_Pos            (0U)                                           /**< (NVMCTRL_INTENSET) NVM Ready Interrupt Enable Position */
#define NVMCTRL_INTENSET_READY_Msk            (0x1U << NVMCTRL_INTENSET_READY_Pos)           /**< (NVMCTRL_INTENSET) NVM Ready Interrupt Enable Mask */
#define NVMCTRL_INTENSET_READY(value)         (NVMCTRL_INTENSET_READY_Msk & ((value) << NVMCTRL_INTENSET_READY_Pos))
#define NVMCTRL_INTENSET_ERROR_Pos            (1U)                                           /**< (NVMCTRL_INTENSET) Error Interrupt Enable Position */
#define NVMCTRL_INTENSET_ERROR_Msk            (0x1U << NVMCTRL_INTENSET_ERROR_Pos)           /**< (NVMCTRL_INTENSET) Error Interrupt Enable Mask */
#define NVMCTRL_INTENSET_ERROR(value)         (NVMCTRL_INTENSET_ERROR_Msk & ((value) << NVMCTRL_INTENSET_ERROR_Pos))
#define NVMCTRL_INTENSET_Msk                  (0x00000003UL)                                 /**< (NVMCTRL_INTENSET) Register Mask  */

/* -------- NVMCTRL_INTFLAG : (NVMCTRL Offset: 0x14) (R/W 8) Interrupt Flag Status and Clear -------- */
#define NVMCTRL_INTFLAG_READY_Pos             (0U)                                           /**< (NVMCTRL_INTFLAG) NVM Ready Position */
#define NVMCTRL_INTFLAG_READY_Msk             (0x1U << NVMCTRL_INTFLAG_READY_Pos)            /**< (NVMCTRL_INTFLAG) NVM Ready Mask */
#define NVMCTRL_INTFLAG_READY(value)          (NVMCTRL_INTFLAG_READY_Msk & ((value) << NVMCTRL_INTFLAG_READY_Pos))
#define NVMCTRL_INTFLAG_ERROR_Pos             (1U)                                           /**< (NVMCTRL_INTFLAG) Error Position */
#define NVMCTRL_INTFLAG_ERROR_Msk             (0x1U << NVMCTRL_INTFLAG_ERROR_Pos)            /**< (NVMCTRL_INTFLAG) Error Mask */
#define NVMCTRL_INTFLAG_ERROR(value)          (NVMCTRL_INTFLAG_ERROR_Msk & ((value) << NVMCTRL_INTFLAG_ERROR_Pos))
#define NVMCTRL_INTFLAG_Msk                   (0x00000003UL)                                 /**< (NVMCTRL_INTFLAG) Register Mask  */

/* -------- NVMCTRL_STATUS : (NVMCTRL Offset: 0x18) (R/W 16) Status -------- */
#define NVMCTRL_STATUS_PRM_Pos                (0U)                                           /**< (NVMCTRL_STATUS) Power Reduction Mode Position */
#define NVMCTRL_STATUS_PRM_Msk                (0x1U << NVMCTRL_STATUS_PRM_Pos)               /**< (NVMCTRL_STATUS) Power Reduction Mode Mask */
#define NVMCTRL_STATUS_PRM(value)             (NVMCTRL_STATUS_PRM_Msk & ((value) << NVMCTRL_STATUS_PRM_Pos))
#define NVMCTRL_STATUS_LOAD_Pos               (1U)                                           /**< (NVMCTRL_STATUS) NVM Page Buffer Active Loading Position */
#define NVMCTRL_STATUS_LOAD_Msk               (0x1U << NVMCTRL_STATUS_LOAD_Pos)              /**< (NVMCTRL_STATUS) NVM Page Buffer Active Loading Mask */
#define NVMCTRL_STATUS_LOAD(value)            (NVMCTRL_STATUS_LOAD_Msk & ((value) << NVMCTRL_STATUS_LOAD_Pos))
#define NVMCTRL_STATUS_PROGE_Pos              (2U)                                           /**< (NVMCTRL_STATUS) Programming Error Status Position */
#define NVMCTRL_STATUS_PROGE_Msk              (0x1U << NVMCTRL_STATUS_PROGE_Pos)             /**< (NVMCTRL_STATUS) Programming Error Status Mask */
#define NVMCTRL_STATUS_PROGE(value)           (NVMCTRL_STATUS_PROGE_Msk & ((value) << NVMCTRL_STATUS_PROGE_Pos))
#define NVMCTRL_STATUS_LOCKE_Pos              (3U)                                           /**< (NVMCTRL_STATUS) Lock Error Status Position */
#define NVMCTRL_STATUS_LOCKE_Msk              (0x1U << NVMCTRL_STATUS_LOCKE_Pos)             /**< (NVMCTRL_STATUS) Lock Error Status Mask */
#define NVMCTRL_STATUS_LOCKE(value)           (NVMCTRL_STATUS_LOCKE_Msk & ((value) << NVMCTRL_STATUS_LOCKE_Pos))
#define NVMCTRL_STATUS_NVME_Pos               (4U)                                           /**< (NVMCTRL_STATUS) NVM Error Position */
#define NVMCTRL_STATUS_NVME_Msk               (0x1U << NVMCTRL_STATUS_NVME_Pos)              /**< (NVMCTRL_STATUS) NVM Error Mask */
#define NVMCTRL_STATUS_NVME(value)            (NVMCTRL_STATUS_NVME_Msk & ((value) << NVMCTRL_STATUS_NVME_Pos))
#define NVMCTRL_STATUS_SB_Pos                 (8U)                                           /**< (NVMCTRL_STATUS) Security Bit Status Position */
#define NVMCTRL_STATUS_SB_Msk                 (0x1U << NVMCTRL_STATUS_SB_Pos)                /**< (NVMCTRL_STATUS) Security Bit Status Mask */
#define NVMCTRL_STATUS_SB(value)              (NVMCTRL_STATUS_SB_Msk & ((value) << NVMCTRL_STATUS_SB_Pos))
#define NVMCTRL_STATUS_Msk                    (0x0000011FUL)                                 /**< (NVMCTRL_STATUS) Register Mask  */

/* -------- NVMCTRL_ADDR : (NVMCTRL Offset: 0x1C) (R/W 32) Address -------- */
#define NVMCTRL_ADDR_ADDR_Pos                 (0U)                                           /**< (NVMCTRL_ADDR) NVM Address Position */
#define NVMCTRL_ADDR_ADDR_Msk                 (0x3FFFFFU << NVMCTRL_ADDR_ADDR_Pos)           /**< (NVMCTRL_ADDR) NVM Address Mask */
#define NVMCTRL_ADDR_ADDR(value)              (NVMCTRL_ADDR_ADDR_Msk & ((value) << NVMCTRL_ADDR_ADDR_Pos))
#define NVMCTRL_ADDR_Msk                      (0x003FFFFFUL)                                 /**< (NVMCTRL_ADDR) Register Mask  */

/* -------- NVMCTRL_LOCK : (NVMCTRL Offset: 0x20) (R/W 16) Lock Section -------- */
#define NVMCTRL_LOCK_LOCK_Pos                 (0U)                                           /**< (NVMCTRL_LOCK) Region Lock Bits Position */
#define NVMCTRL_LOCK_LOCK_Msk                 (0xFFFFU << NVMCTRL_LOCK_LOCK_Pos)             /**< (NVMCTRL_LOCK) Region Lock Bits Mask */
#define NVMCTRL_LOCK_LOCK(value)              (NVMCTRL_LOCK_LOCK_Msk & ((value) << NVMCTRL_LOCK_LOCK_Pos))
#define NVMCTRL_LOCK_Msk                      (0x0000FFFFUL)                                 /**< (NVMCTRL_LOCK) Register Mask  */

/* -------- NVMCTRL_PBLDATA0 : (NVMCTRL Offset: 0x28) (R/  32) Page Buffer Load Data 0 -------- */
#define NVMCTRL_PBLDATA0_Msk                  (0x00000000UL)                                 /**< (NVMCTRL_PBLDATA0) Register Mask  */

/* -------- NVMCTRL_PBLDATA1 : (NVMCTRL Offset: 0x2C) (R/  32) Page Buffer Load Data 1 -------- */
#define NVMCTRL_PBLDATA1_Msk                  (0x00000000UL)                                 /**< (NVMCTRL_PBLDATA1) Register Mask  */

/** \brief NVMCTRL register offsets definitions */
#define NVMCTRL_CTRLA_OFFSET           (0x00)         /**< (NVMCTRL_CTRLA) Control A Offset */
#define NVMCTRL_CTRLB_OFFSET           (0x04)         /**< (NVMCTRL_CTRLB) Control B Offset */
#define NVMCTRL_PARAM_OFFSET           (0x08)         /**< (NVMCTRL_PARAM) NVM Parameter Offset */
#define NVMCTRL_INTENCLR_OFFSET        (0x0C)         /**< (NVMCTRL_INTENCLR) Interrupt Enable Clear Offset */
#define NVMCTRL_INTENSET_OFFSET        (0x10)         /**< (NVMCTRL_INTENSET) Interrupt Enable Set Offset */
#define NVMCTRL_INTFLAG_OFFSET         (0x14)         /**< (NVMCTRL_INTFLAG) Interrupt Flag Status and Clear Offset */
#define NVMCTRL_STATUS_OFFSET          (0x18)         /**< (NVMCTRL_STATUS) Status Offset */
#define NVMCTRL_ADDR_OFFSET            (0x1C)         /**< (NVMCTRL_ADDR) Address Offset */
#define NVMCTRL_LOCK_OFFSET            (0x20)         /**< (NVMCTRL_LOCK) Lock Section Offset */
#define NVMCTRL_PBLDATA0_OFFSET        (0x28)         /**< (NVMCTRL_PBLDATA0) Page Buffer Load Data 0 Offset */
#define NVMCTRL_PBLDATA1_OFFSET        (0x2C)         /**< (NVMCTRL_PBLDATA1) Page Buffer Load Data 1 Offset */

/** \brief NVMCTRL register API structure */
typedef struct
{
  __IO  uint16_t                       NVMCTRL_CTRLA;   /**< Offset: 0x00 (R/W  16) Control A */
  __I   uint8_t                        Reserved1[0x02];
  __IO  uint32_t                       NVMCTRL_CTRLB;   /**< Offset: 0x04 (R/W  32) Control B */
  __IO  uint32_t                       NVMCTRL_PARAM;   /**< Offset: 0x08 (R/W  32) NVM Parameter */
  __IO  uint8_t                        NVMCTRL_INTENCLR; /**< Offset: 0x0c (R/W  8) Interrupt Enable Clear */
  __I   uint8_t                        Reserved2[0x03];
  __IO  uint8_t                        NVMCTRL_INTENSET; /**< Offset: 0x10 (R/W  8) Interrupt Enable Set */
  __I   uint8_t                        Reserved3[0x03];
  __IO  uint8_t                        NVMCTRL_INTFLAG; /**< Offset: 0x14 (R/W  8) Interrupt Flag Status and Clear */
  __I   uint8_t                        Reserved4[0x03];
  __IO  uint16_t                       NVMCTRL_STATUS;  /**< Offset: 0x18 (R/W  16) Status */
  __I   uint8_t                        Reserved5[0x02];
  __IO  uint32_t                       NVMCTRL_ADDR;    /**< Offset: 0x1c (R/W  32) Address */
  __IO  uint16_t                       NVMCTRL_LOCK;    /**< Offset: 0x20 (R/W  16) Lock Section */
  __I   uint8_t                        Reserved6[0x06];
  __I   uint32_t                       NVMCTRL_PBLDATA0; /**< Offset: 0x28 (R/   32) Page Buffer Load Data 0 */
  __I   uint32_t                       NVMCTRL_PBLDATA1; /**< Offset: 0x2c (R/   32) Page Buffer Load Data 1 */
} nvmctrl_registers_t;
/** @}  end of Non-Volatile Memory Controller */

#endif /* SAMC_SAMC21_NVMCTRL_MODULE_H */

