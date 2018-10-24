/**
 * \brief Header file for SAMC/SAMC21 TCC
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
#ifndef SAMC_SAMC21_TCC_MODULE_H
#define SAMC_SAMC21_TCC_MODULE_H

/** \addtogroup SAMC_SAMC21 Timer Counter Control
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_TCC                                   */
/* ========================================================================== */

/* -------- TCC_CTRLA : (TCC Offset: 0x00) (R/W 32) Control A -------- */
#define TCC_CTRLA_SWRST_Pos                   (0U)                                           /**< (TCC_CTRLA) Software Reset Position */
#define TCC_CTRLA_SWRST_Msk                   (0x1U << TCC_CTRLA_SWRST_Pos)                  /**< (TCC_CTRLA) Software Reset Mask */
#define TCC_CTRLA_SWRST(value)                (TCC_CTRLA_SWRST_Msk & ((value) << TCC_CTRLA_SWRST_Pos))
#define TCC_CTRLA_ENABLE_Pos                  (1U)                                           /**< (TCC_CTRLA) Enable Position */
#define TCC_CTRLA_ENABLE_Msk                  (0x1U << TCC_CTRLA_ENABLE_Pos)                 /**< (TCC_CTRLA) Enable Mask */
#define TCC_CTRLA_ENABLE(value)               (TCC_CTRLA_ENABLE_Msk & ((value) << TCC_CTRLA_ENABLE_Pos))
#define TCC_CTRLA_RESOLUTION_Pos              (5U)                                           /**< (TCC_CTRLA) Enhanced Resolution Position */
#define TCC_CTRLA_RESOLUTION_Msk              (0x3U << TCC_CTRLA_RESOLUTION_Pos)             /**< (TCC_CTRLA) Enhanced Resolution Mask */
#define TCC_CTRLA_RESOLUTION(value)           (TCC_CTRLA_RESOLUTION_Msk & ((value) << TCC_CTRLA_RESOLUTION_Pos))
#define   TCC_CTRLA_RESOLUTION_NONE_Val       (0U)                                           /**< (TCC_CTRLA) Dithering is disabled  */
#define   TCC_CTRLA_RESOLUTION_DITH4_Val      (1U)                                           /**< (TCC_CTRLA) Dithering is done every 16 PWM frames  */
#define   TCC_CTRLA_RESOLUTION_DITH5_Val      (2U)                                           /**< (TCC_CTRLA) Dithering is done every 32 PWM frames  */
#define   TCC_CTRLA_RESOLUTION_DITH6_Val      (3U)                                           /**< (TCC_CTRLA) Dithering is done every 64 PWM frames  */
#define TCC_CTRLA_RESOLUTION_NONE             (TCC_CTRLA_RESOLUTION_NONE_Val << TCC_CTRLA_RESOLUTION_Pos) /**< (TCC_CTRLA) Dithering is disabled Position  */
#define TCC_CTRLA_RESOLUTION_DITH4            (TCC_CTRLA_RESOLUTION_DITH4_Val << TCC_CTRLA_RESOLUTION_Pos) /**< (TCC_CTRLA) Dithering is done every 16 PWM frames Position  */
#define TCC_CTRLA_RESOLUTION_DITH5            (TCC_CTRLA_RESOLUTION_DITH5_Val << TCC_CTRLA_RESOLUTION_Pos) /**< (TCC_CTRLA) Dithering is done every 32 PWM frames Position  */
#define TCC_CTRLA_RESOLUTION_DITH6            (TCC_CTRLA_RESOLUTION_DITH6_Val << TCC_CTRLA_RESOLUTION_Pos) /**< (TCC_CTRLA) Dithering is done every 64 PWM frames Position  */
#define TCC_CTRLA_PRESCALER_Pos               (8U)                                           /**< (TCC_CTRLA) Prescaler Position */
#define TCC_CTRLA_PRESCALER_Msk               (0x7U << TCC_CTRLA_PRESCALER_Pos)              /**< (TCC_CTRLA) Prescaler Mask */
#define TCC_CTRLA_PRESCALER(value)            (TCC_CTRLA_PRESCALER_Msk & ((value) << TCC_CTRLA_PRESCALER_Pos))
#define   TCC_CTRLA_PRESCALER_DIV1_Val        (0U)                                           /**< (TCC_CTRLA) No division  */
#define   TCC_CTRLA_PRESCALER_DIV2_Val        (1U)                                           /**< (TCC_CTRLA) Divide by 2  */
#define   TCC_CTRLA_PRESCALER_DIV4_Val        (2U)                                           /**< (TCC_CTRLA) Divide by 4  */
#define   TCC_CTRLA_PRESCALER_DIV8_Val        (3U)                                           /**< (TCC_CTRLA) Divide by 8  */
#define   TCC_CTRLA_PRESCALER_DIV16_Val       (4U)                                           /**< (TCC_CTRLA) Divide by 16  */
#define   TCC_CTRLA_PRESCALER_DIV64_Val       (5U)                                           /**< (TCC_CTRLA) Divide by 64  */
#define   TCC_CTRLA_PRESCALER_DIV256_Val      (6U)                                           /**< (TCC_CTRLA) Divide by 256  */
#define   TCC_CTRLA_PRESCALER_DIV1024_Val     (7U)                                           /**< (TCC_CTRLA) Divide by 1024  */
#define TCC_CTRLA_PRESCALER_DIV1              (TCC_CTRLA_PRESCALER_DIV1_Val << TCC_CTRLA_PRESCALER_Pos) /**< (TCC_CTRLA) No division Position  */
#define TCC_CTRLA_PRESCALER_DIV2              (TCC_CTRLA_PRESCALER_DIV2_Val << TCC_CTRLA_PRESCALER_Pos) /**< (TCC_CTRLA) Divide by 2 Position  */
#define TCC_CTRLA_PRESCALER_DIV4              (TCC_CTRLA_PRESCALER_DIV4_Val << TCC_CTRLA_PRESCALER_Pos) /**< (TCC_CTRLA) Divide by 4 Position  */
#define TCC_CTRLA_PRESCALER_DIV8              (TCC_CTRLA_PRESCALER_DIV8_Val << TCC_CTRLA_PRESCALER_Pos) /**< (TCC_CTRLA) Divide by 8 Position  */
#define TCC_CTRLA_PRESCALER_DIV16             (TCC_CTRLA_PRESCALER_DIV16_Val << TCC_CTRLA_PRESCALER_Pos) /**< (TCC_CTRLA) Divide by 16 Position  */
#define TCC_CTRLA_PRESCALER_DIV64             (TCC_CTRLA_PRESCALER_DIV64_Val << TCC_CTRLA_PRESCALER_Pos) /**< (TCC_CTRLA) Divide by 64 Position  */
#define TCC_CTRLA_PRESCALER_DIV256            (TCC_CTRLA_PRESCALER_DIV256_Val << TCC_CTRLA_PRESCALER_Pos) /**< (TCC_CTRLA) Divide by 256 Position  */
#define TCC_CTRLA_PRESCALER_DIV1024           (TCC_CTRLA_PRESCALER_DIV1024_Val << TCC_CTRLA_PRESCALER_Pos) /**< (TCC_CTRLA) Divide by 1024 Position  */
#define TCC_CTRLA_RUNSTDBY_Pos                (11U)                                          /**< (TCC_CTRLA) Run in Standby Position */
#define TCC_CTRLA_RUNSTDBY_Msk                (0x1U << TCC_CTRLA_RUNSTDBY_Pos)               /**< (TCC_CTRLA) Run in Standby Mask */
#define TCC_CTRLA_RUNSTDBY(value)             (TCC_CTRLA_RUNSTDBY_Msk & ((value) << TCC_CTRLA_RUNSTDBY_Pos))
#define TCC_CTRLA_PRESCSYNC_Pos               (12U)                                          /**< (TCC_CTRLA) Prescaler and Counter Synchronization Selection Position */
#define TCC_CTRLA_PRESCSYNC_Msk               (0x3U << TCC_CTRLA_PRESCSYNC_Pos)              /**< (TCC_CTRLA) Prescaler and Counter Synchronization Selection Mask */
#define TCC_CTRLA_PRESCSYNC(value)            (TCC_CTRLA_PRESCSYNC_Msk & ((value) << TCC_CTRLA_PRESCSYNC_Pos))
#define   TCC_CTRLA_PRESCSYNC_GCLK_Val        (0U)                                           /**< (TCC_CTRLA) Reload or reset counter on next GCLK  */
#define   TCC_CTRLA_PRESCSYNC_PRESC_Val       (1U)                                           /**< (TCC_CTRLA) Reload or reset counter on next prescaler clock  */
#define   TCC_CTRLA_PRESCSYNC_RESYNC_Val      (2U)                                           /**< (TCC_CTRLA) Reload or reset counter on next GCLK and reset prescaler counter  */
#define TCC_CTRLA_PRESCSYNC_GCLK              (TCC_CTRLA_PRESCSYNC_GCLK_Val << TCC_CTRLA_PRESCSYNC_Pos) /**< (TCC_CTRLA) Reload or reset counter on next GCLK Position  */
#define TCC_CTRLA_PRESCSYNC_PRESC             (TCC_CTRLA_PRESCSYNC_PRESC_Val << TCC_CTRLA_PRESCSYNC_Pos) /**< (TCC_CTRLA) Reload or reset counter on next prescaler clock Position  */
#define TCC_CTRLA_PRESCSYNC_RESYNC            (TCC_CTRLA_PRESCSYNC_RESYNC_Val << TCC_CTRLA_PRESCSYNC_Pos) /**< (TCC_CTRLA) Reload or reset counter on next GCLK and reset prescaler counter Position  */
#define TCC_CTRLA_ALOCK_Pos                   (14U)                                          /**< (TCC_CTRLA) Auto Lock Position */
#define TCC_CTRLA_ALOCK_Msk                   (0x1U << TCC_CTRLA_ALOCK_Pos)                  /**< (TCC_CTRLA) Auto Lock Mask */
#define TCC_CTRLA_ALOCK(value)                (TCC_CTRLA_ALOCK_Msk & ((value) << TCC_CTRLA_ALOCK_Pos))
#define TCC_CTRLA_MSYNC_Pos                   (15U)                                          /**< (TCC_CTRLA) Master Synchronization (only for TCC Slave Instance) Position */
#define TCC_CTRLA_MSYNC_Msk                   (0x1U << TCC_CTRLA_MSYNC_Pos)                  /**< (TCC_CTRLA) Master Synchronization (only for TCC Slave Instance) Mask */
#define TCC_CTRLA_MSYNC(value)                (TCC_CTRLA_MSYNC_Msk & ((value) << TCC_CTRLA_MSYNC_Pos))
#define TCC_CTRLA_DMAOS_Pos                   (23U)                                          /**< (TCC_CTRLA) DMA One-shot Trigger Mode Position */
#define TCC_CTRLA_DMAOS_Msk                   (0x1U << TCC_CTRLA_DMAOS_Pos)                  /**< (TCC_CTRLA) DMA One-shot Trigger Mode Mask */
#define TCC_CTRLA_DMAOS(value)                (TCC_CTRLA_DMAOS_Msk & ((value) << TCC_CTRLA_DMAOS_Pos))
#define TCC_CTRLA_CPTEN0_Pos                  (24U)                                          /**< (TCC_CTRLA) Capture Channel 0 Enable Position */
#define TCC_CTRLA_CPTEN0_Msk                  (0x1U << TCC_CTRLA_CPTEN0_Pos)                 /**< (TCC_CTRLA) Capture Channel 0 Enable Mask */
#define TCC_CTRLA_CPTEN0(value)               (TCC_CTRLA_CPTEN0_Msk & ((value) << TCC_CTRLA_CPTEN0_Pos))
#define TCC_CTRLA_CPTEN1_Pos                  (25U)                                          /**< (TCC_CTRLA) Capture Channel 1 Enable Position */
#define TCC_CTRLA_CPTEN1_Msk                  (0x1U << TCC_CTRLA_CPTEN1_Pos)                 /**< (TCC_CTRLA) Capture Channel 1 Enable Mask */
#define TCC_CTRLA_CPTEN1(value)               (TCC_CTRLA_CPTEN1_Msk & ((value) << TCC_CTRLA_CPTEN1_Pos))
#define TCC_CTRLA_CPTEN2_Pos                  (26U)                                          /**< (TCC_CTRLA) Capture Channel 2 Enable Position */
#define TCC_CTRLA_CPTEN2_Msk                  (0x1U << TCC_CTRLA_CPTEN2_Pos)                 /**< (TCC_CTRLA) Capture Channel 2 Enable Mask */
#define TCC_CTRLA_CPTEN2(value)               (TCC_CTRLA_CPTEN2_Msk & ((value) << TCC_CTRLA_CPTEN2_Pos))
#define TCC_CTRLA_CPTEN3_Pos                  (27U)                                          /**< (TCC_CTRLA) Capture Channel 3 Enable Position */
#define TCC_CTRLA_CPTEN3_Msk                  (0x1U << TCC_CTRLA_CPTEN3_Pos)                 /**< (TCC_CTRLA) Capture Channel 3 Enable Mask */
#define TCC_CTRLA_CPTEN3(value)               (TCC_CTRLA_CPTEN3_Msk & ((value) << TCC_CTRLA_CPTEN3_Pos))
#define TCC_CTRLA_Msk                         (0x0F80FF63UL)                                 /**< (TCC_CTRLA) Register Mask  */

/* -------- TCC_CTRLBCLR : (TCC Offset: 0x04) (R/W 8) Control B Clear -------- */
#define TCC_CTRLBCLR_DIR_Pos                  (0U)                                           /**< (TCC_CTRLBCLR) Counter Direction Position */
#define TCC_CTRLBCLR_DIR_Msk                  (0x1U << TCC_CTRLBCLR_DIR_Pos)                 /**< (TCC_CTRLBCLR) Counter Direction Mask */
#define TCC_CTRLBCLR_DIR(value)               (TCC_CTRLBCLR_DIR_Msk & ((value) << TCC_CTRLBCLR_DIR_Pos))
#define TCC_CTRLBCLR_LUPD_Pos                 (1U)                                           /**< (TCC_CTRLBCLR) Lock Update Position */
#define TCC_CTRLBCLR_LUPD_Msk                 (0x1U << TCC_CTRLBCLR_LUPD_Pos)                /**< (TCC_CTRLBCLR) Lock Update Mask */
#define TCC_CTRLBCLR_LUPD(value)              (TCC_CTRLBCLR_LUPD_Msk & ((value) << TCC_CTRLBCLR_LUPD_Pos))
#define TCC_CTRLBCLR_ONESHOT_Pos              (2U)                                           /**< (TCC_CTRLBCLR) One-Shot Position */
#define TCC_CTRLBCLR_ONESHOT_Msk              (0x1U << TCC_CTRLBCLR_ONESHOT_Pos)             /**< (TCC_CTRLBCLR) One-Shot Mask */
#define TCC_CTRLBCLR_ONESHOT(value)           (TCC_CTRLBCLR_ONESHOT_Msk & ((value) << TCC_CTRLBCLR_ONESHOT_Pos))
#define TCC_CTRLBCLR_IDXCMD_Pos               (3U)                                           /**< (TCC_CTRLBCLR) Ramp Index Command Position */
#define TCC_CTRLBCLR_IDXCMD_Msk               (0x3U << TCC_CTRLBCLR_IDXCMD_Pos)              /**< (TCC_CTRLBCLR) Ramp Index Command Mask */
#define TCC_CTRLBCLR_IDXCMD(value)            (TCC_CTRLBCLR_IDXCMD_Msk & ((value) << TCC_CTRLBCLR_IDXCMD_Pos))
#define   TCC_CTRLBCLR_IDXCMD_DISABLE_Val     (0U)                                           /**< (TCC_CTRLBCLR) Command disabled: Index toggles between cycles A and B  */
#define   TCC_CTRLBCLR_IDXCMD_SET_Val         (1U)                                           /**< (TCC_CTRLBCLR) Set index: cycle B will be forced in the next cycle  */
#define   TCC_CTRLBCLR_IDXCMD_CLEAR_Val       (2U)                                           /**< (TCC_CTRLBCLR) Clear index: cycle A will be forced in the next cycle  */
#define   TCC_CTRLBCLR_IDXCMD_HOLD_Val        (3U)                                           /**< (TCC_CTRLBCLR) Hold index: the next cycle will be the same as the current cycle  */
#define TCC_CTRLBCLR_IDXCMD_DISABLE           (TCC_CTRLBCLR_IDXCMD_DISABLE_Val << TCC_CTRLBCLR_IDXCMD_Pos) /**< (TCC_CTRLBCLR) Command disabled: Index toggles between cycles A and B Position  */
#define TCC_CTRLBCLR_IDXCMD_SET               (TCC_CTRLBCLR_IDXCMD_SET_Val << TCC_CTRLBCLR_IDXCMD_Pos) /**< (TCC_CTRLBCLR) Set index: cycle B will be forced in the next cycle Position  */
#define TCC_CTRLBCLR_IDXCMD_CLEAR             (TCC_CTRLBCLR_IDXCMD_CLEAR_Val << TCC_CTRLBCLR_IDXCMD_Pos) /**< (TCC_CTRLBCLR) Clear index: cycle A will be forced in the next cycle Position  */
#define TCC_CTRLBCLR_IDXCMD_HOLD              (TCC_CTRLBCLR_IDXCMD_HOLD_Val << TCC_CTRLBCLR_IDXCMD_Pos) /**< (TCC_CTRLBCLR) Hold index: the next cycle will be the same as the current cycle Position  */
#define TCC_CTRLBCLR_CMD_Pos                  (5U)                                           /**< (TCC_CTRLBCLR) TCC Command Position */
#define TCC_CTRLBCLR_CMD_Msk                  (0x7U << TCC_CTRLBCLR_CMD_Pos)                 /**< (TCC_CTRLBCLR) TCC Command Mask */
#define TCC_CTRLBCLR_CMD(value)               (TCC_CTRLBCLR_CMD_Msk & ((value) << TCC_CTRLBCLR_CMD_Pos))
#define   TCC_CTRLBCLR_CMD_NONE_Val           (0U)                                           /**< (TCC_CTRLBCLR) No action  */
#define   TCC_CTRLBCLR_CMD_RETRIGGER_Val      (1U)                                           /**< (TCC_CTRLBCLR) Clear start, restart or retrigger  */
#define   TCC_CTRLBCLR_CMD_STOP_Val           (2U)                                           /**< (TCC_CTRLBCLR) Force stop  */
#define   TCC_CTRLBCLR_CMD_UPDATE_Val         (3U)                                           /**< (TCC_CTRLBCLR) Force update or double buffered registers  */
#define   TCC_CTRLBCLR_CMD_READSYNC_Val       (4U)                                           /**< (TCC_CTRLBCLR) Force COUNT read synchronization  */
#define   TCC_CTRLBCLR_CMD_DMAOS_Val          (5U)                                           /**< (TCC_CTRLBCLR) One-shot DMA trigger  */
#define TCC_CTRLBCLR_CMD_NONE                 (TCC_CTRLBCLR_CMD_NONE_Val << TCC_CTRLBCLR_CMD_Pos) /**< (TCC_CTRLBCLR) No action Position  */
#define TCC_CTRLBCLR_CMD_RETRIGGER            (TCC_CTRLBCLR_CMD_RETRIGGER_Val << TCC_CTRLBCLR_CMD_Pos) /**< (TCC_CTRLBCLR) Clear start, restart or retrigger Position  */
#define TCC_CTRLBCLR_CMD_STOP                 (TCC_CTRLBCLR_CMD_STOP_Val << TCC_CTRLBCLR_CMD_Pos) /**< (TCC_CTRLBCLR) Force stop Position  */
#define TCC_CTRLBCLR_CMD_UPDATE               (TCC_CTRLBCLR_CMD_UPDATE_Val << TCC_CTRLBCLR_CMD_Pos) /**< (TCC_CTRLBCLR) Force update or double buffered registers Position  */
#define TCC_CTRLBCLR_CMD_READSYNC             (TCC_CTRLBCLR_CMD_READSYNC_Val << TCC_CTRLBCLR_CMD_Pos) /**< (TCC_CTRLBCLR) Force COUNT read synchronization Position  */
#define TCC_CTRLBCLR_CMD_DMAOS                (TCC_CTRLBCLR_CMD_DMAOS_Val << TCC_CTRLBCLR_CMD_Pos) /**< (TCC_CTRLBCLR) One-shot DMA trigger Position  */
#define TCC_CTRLBCLR_Msk                      (0x000000FFUL)                                 /**< (TCC_CTRLBCLR) Register Mask  */

/* -------- TCC_CTRLBSET : (TCC Offset: 0x05) (R/W 8) Control B Set -------- */
#define TCC_CTRLBSET_DIR_Pos                  (0U)                                           /**< (TCC_CTRLBSET) Counter Direction Position */
#define TCC_CTRLBSET_DIR_Msk                  (0x1U << TCC_CTRLBSET_DIR_Pos)                 /**< (TCC_CTRLBSET) Counter Direction Mask */
#define TCC_CTRLBSET_DIR(value)               (TCC_CTRLBSET_DIR_Msk & ((value) << TCC_CTRLBSET_DIR_Pos))
#define TCC_CTRLBSET_LUPD_Pos                 (1U)                                           /**< (TCC_CTRLBSET) Lock Update Position */
#define TCC_CTRLBSET_LUPD_Msk                 (0x1U << TCC_CTRLBSET_LUPD_Pos)                /**< (TCC_CTRLBSET) Lock Update Mask */
#define TCC_CTRLBSET_LUPD(value)              (TCC_CTRLBSET_LUPD_Msk & ((value) << TCC_CTRLBSET_LUPD_Pos))
#define TCC_CTRLBSET_ONESHOT_Pos              (2U)                                           /**< (TCC_CTRLBSET) One-Shot Position */
#define TCC_CTRLBSET_ONESHOT_Msk              (0x1U << TCC_CTRLBSET_ONESHOT_Pos)             /**< (TCC_CTRLBSET) One-Shot Mask */
#define TCC_CTRLBSET_ONESHOT(value)           (TCC_CTRLBSET_ONESHOT_Msk & ((value) << TCC_CTRLBSET_ONESHOT_Pos))
#define TCC_CTRLBSET_IDXCMD_Pos               (3U)                                           /**< (TCC_CTRLBSET) Ramp Index Command Position */
#define TCC_CTRLBSET_IDXCMD_Msk               (0x3U << TCC_CTRLBSET_IDXCMD_Pos)              /**< (TCC_CTRLBSET) Ramp Index Command Mask */
#define TCC_CTRLBSET_IDXCMD(value)            (TCC_CTRLBSET_IDXCMD_Msk & ((value) << TCC_CTRLBSET_IDXCMD_Pos))
#define   TCC_CTRLBSET_IDXCMD_DISABLE_Val     (0U)                                           /**< (TCC_CTRLBSET) Command disabled: Index toggles between cycles A and B  */
#define   TCC_CTRLBSET_IDXCMD_SET_Val         (1U)                                           /**< (TCC_CTRLBSET) Set index: cycle B will be forced in the next cycle  */
#define   TCC_CTRLBSET_IDXCMD_CLEAR_Val       (2U)                                           /**< (TCC_CTRLBSET) Clear index: cycle A will be forced in the next cycle  */
#define   TCC_CTRLBSET_IDXCMD_HOLD_Val        (3U)                                           /**< (TCC_CTRLBSET) Hold index: the next cycle will be the same as the current cycle  */
#define TCC_CTRLBSET_IDXCMD_DISABLE           (TCC_CTRLBSET_IDXCMD_DISABLE_Val << TCC_CTRLBSET_IDXCMD_Pos) /**< (TCC_CTRLBSET) Command disabled: Index toggles between cycles A and B Position  */
#define TCC_CTRLBSET_IDXCMD_SET               (TCC_CTRLBSET_IDXCMD_SET_Val << TCC_CTRLBSET_IDXCMD_Pos) /**< (TCC_CTRLBSET) Set index: cycle B will be forced in the next cycle Position  */
#define TCC_CTRLBSET_IDXCMD_CLEAR             (TCC_CTRLBSET_IDXCMD_CLEAR_Val << TCC_CTRLBSET_IDXCMD_Pos) /**< (TCC_CTRLBSET) Clear index: cycle A will be forced in the next cycle Position  */
#define TCC_CTRLBSET_IDXCMD_HOLD              (TCC_CTRLBSET_IDXCMD_HOLD_Val << TCC_CTRLBSET_IDXCMD_Pos) /**< (TCC_CTRLBSET) Hold index: the next cycle will be the same as the current cycle Position  */
#define TCC_CTRLBSET_CMD_Pos                  (5U)                                           /**< (TCC_CTRLBSET) TCC Command Position */
#define TCC_CTRLBSET_CMD_Msk                  (0x7U << TCC_CTRLBSET_CMD_Pos)                 /**< (TCC_CTRLBSET) TCC Command Mask */
#define TCC_CTRLBSET_CMD(value)               (TCC_CTRLBSET_CMD_Msk & ((value) << TCC_CTRLBSET_CMD_Pos))
#define   TCC_CTRLBSET_CMD_NONE_Val           (0U)                                           /**< (TCC_CTRLBSET) No action  */
#define   TCC_CTRLBSET_CMD_RETRIGGER_Val      (1U)                                           /**< (TCC_CTRLBSET) Clear start, restart or retrigger  */
#define   TCC_CTRLBSET_CMD_STOP_Val           (2U)                                           /**< (TCC_CTRLBSET) Force stop  */
#define   TCC_CTRLBSET_CMD_UPDATE_Val         (3U)                                           /**< (TCC_CTRLBSET) Force update or double buffered registers  */
#define   TCC_CTRLBSET_CMD_READSYNC_Val       (4U)                                           /**< (TCC_CTRLBSET) Force COUNT read synchronization  */
#define   TCC_CTRLBSET_CMD_DMAOS_Val          (5U)                                           /**< (TCC_CTRLBSET) One-shot DMA trigger  */
#define TCC_CTRLBSET_CMD_NONE                 (TCC_CTRLBSET_CMD_NONE_Val << TCC_CTRLBSET_CMD_Pos) /**< (TCC_CTRLBSET) No action Position  */
#define TCC_CTRLBSET_CMD_RETRIGGER            (TCC_CTRLBSET_CMD_RETRIGGER_Val << TCC_CTRLBSET_CMD_Pos) /**< (TCC_CTRLBSET) Clear start, restart or retrigger Position  */
#define TCC_CTRLBSET_CMD_STOP                 (TCC_CTRLBSET_CMD_STOP_Val << TCC_CTRLBSET_CMD_Pos) /**< (TCC_CTRLBSET) Force stop Position  */
#define TCC_CTRLBSET_CMD_UPDATE               (TCC_CTRLBSET_CMD_UPDATE_Val << TCC_CTRLBSET_CMD_Pos) /**< (TCC_CTRLBSET) Force update or double buffered registers Position  */
#define TCC_CTRLBSET_CMD_READSYNC             (TCC_CTRLBSET_CMD_READSYNC_Val << TCC_CTRLBSET_CMD_Pos) /**< (TCC_CTRLBSET) Force COUNT read synchronization Position  */
#define TCC_CTRLBSET_CMD_DMAOS                (TCC_CTRLBSET_CMD_DMAOS_Val << TCC_CTRLBSET_CMD_Pos) /**< (TCC_CTRLBSET) One-shot DMA trigger Position  */
#define TCC_CTRLBSET_Msk                      (0x000000FFUL)                                 /**< (TCC_CTRLBSET) Register Mask  */

/* -------- TCC_SYNCBUSY : (TCC Offset: 0x08) (R/  32) Synchronization Busy -------- */
#define TCC_SYNCBUSY_SWRST_Pos                (0U)                                           /**< (TCC_SYNCBUSY) Swrst Busy Position */
#define TCC_SYNCBUSY_SWRST_Msk                (0x1U << TCC_SYNCBUSY_SWRST_Pos)               /**< (TCC_SYNCBUSY) Swrst Busy Mask */
#define TCC_SYNCBUSY_SWRST(value)             (TCC_SYNCBUSY_SWRST_Msk & ((value) << TCC_SYNCBUSY_SWRST_Pos))
#define TCC_SYNCBUSY_ENABLE_Pos               (1U)                                           /**< (TCC_SYNCBUSY) Enable Busy Position */
#define TCC_SYNCBUSY_ENABLE_Msk               (0x1U << TCC_SYNCBUSY_ENABLE_Pos)              /**< (TCC_SYNCBUSY) Enable Busy Mask */
#define TCC_SYNCBUSY_ENABLE(value)            (TCC_SYNCBUSY_ENABLE_Msk & ((value) << TCC_SYNCBUSY_ENABLE_Pos))
#define TCC_SYNCBUSY_CTRLB_Pos                (2U)                                           /**< (TCC_SYNCBUSY) Ctrlb Busy Position */
#define TCC_SYNCBUSY_CTRLB_Msk                (0x1U << TCC_SYNCBUSY_CTRLB_Pos)               /**< (TCC_SYNCBUSY) Ctrlb Busy Mask */
#define TCC_SYNCBUSY_CTRLB(value)             (TCC_SYNCBUSY_CTRLB_Msk & ((value) << TCC_SYNCBUSY_CTRLB_Pos))
#define TCC_SYNCBUSY_STATUS_Pos               (3U)                                           /**< (TCC_SYNCBUSY) Status Busy Position */
#define TCC_SYNCBUSY_STATUS_Msk               (0x1U << TCC_SYNCBUSY_STATUS_Pos)              /**< (TCC_SYNCBUSY) Status Busy Mask */
#define TCC_SYNCBUSY_STATUS(value)            (TCC_SYNCBUSY_STATUS_Msk & ((value) << TCC_SYNCBUSY_STATUS_Pos))
#define TCC_SYNCBUSY_COUNT_Pos                (4U)                                           /**< (TCC_SYNCBUSY) Count Busy Position */
#define TCC_SYNCBUSY_COUNT_Msk                (0x1U << TCC_SYNCBUSY_COUNT_Pos)               /**< (TCC_SYNCBUSY) Count Busy Mask */
#define TCC_SYNCBUSY_COUNT(value)             (TCC_SYNCBUSY_COUNT_Msk & ((value) << TCC_SYNCBUSY_COUNT_Pos))
#define TCC_SYNCBUSY_PATT_Pos                 (5U)                                           /**< (TCC_SYNCBUSY) Pattern Busy Position */
#define TCC_SYNCBUSY_PATT_Msk                 (0x1U << TCC_SYNCBUSY_PATT_Pos)                /**< (TCC_SYNCBUSY) Pattern Busy Mask */
#define TCC_SYNCBUSY_PATT(value)              (TCC_SYNCBUSY_PATT_Msk & ((value) << TCC_SYNCBUSY_PATT_Pos))
#define TCC_SYNCBUSY_WAVE_Pos                 (6U)                                           /**< (TCC_SYNCBUSY) Wave Busy Position */
#define TCC_SYNCBUSY_WAVE_Msk                 (0x1U << TCC_SYNCBUSY_WAVE_Pos)                /**< (TCC_SYNCBUSY) Wave Busy Mask */
#define TCC_SYNCBUSY_WAVE(value)              (TCC_SYNCBUSY_WAVE_Msk & ((value) << TCC_SYNCBUSY_WAVE_Pos))
#define TCC_SYNCBUSY_PER_Pos                  (7U)                                           /**< (TCC_SYNCBUSY) Period Busy Position */
#define TCC_SYNCBUSY_PER_Msk                  (0x1U << TCC_SYNCBUSY_PER_Pos)                 /**< (TCC_SYNCBUSY) Period Busy Mask */
#define TCC_SYNCBUSY_PER(value)               (TCC_SYNCBUSY_PER_Msk & ((value) << TCC_SYNCBUSY_PER_Pos))
#define TCC_SYNCBUSY_CC0_Pos                  (8U)                                           /**< (TCC_SYNCBUSY) Compare Channel 0 Busy Position */
#define TCC_SYNCBUSY_CC0_Msk                  (0x1U << TCC_SYNCBUSY_CC0_Pos)                 /**< (TCC_SYNCBUSY) Compare Channel 0 Busy Mask */
#define TCC_SYNCBUSY_CC0(value)               (TCC_SYNCBUSY_CC0_Msk & ((value) << TCC_SYNCBUSY_CC0_Pos))
#define TCC_SYNCBUSY_CC1_Pos                  (9U)                                           /**< (TCC_SYNCBUSY) Compare Channel 1 Busy Position */
#define TCC_SYNCBUSY_CC1_Msk                  (0x1U << TCC_SYNCBUSY_CC1_Pos)                 /**< (TCC_SYNCBUSY) Compare Channel 1 Busy Mask */
#define TCC_SYNCBUSY_CC1(value)               (TCC_SYNCBUSY_CC1_Msk & ((value) << TCC_SYNCBUSY_CC1_Pos))
#define TCC_SYNCBUSY_CC2_Pos                  (10U)                                          /**< (TCC_SYNCBUSY) Compare Channel 2 Busy Position */
#define TCC_SYNCBUSY_CC2_Msk                  (0x1U << TCC_SYNCBUSY_CC2_Pos)                 /**< (TCC_SYNCBUSY) Compare Channel 2 Busy Mask */
#define TCC_SYNCBUSY_CC2(value)               (TCC_SYNCBUSY_CC2_Msk & ((value) << TCC_SYNCBUSY_CC2_Pos))
#define TCC_SYNCBUSY_CC3_Pos                  (11U)                                          /**< (TCC_SYNCBUSY) Compare Channel 3 Busy Position */
#define TCC_SYNCBUSY_CC3_Msk                  (0x1U << TCC_SYNCBUSY_CC3_Pos)                 /**< (TCC_SYNCBUSY) Compare Channel 3 Busy Mask */
#define TCC_SYNCBUSY_CC3(value)               (TCC_SYNCBUSY_CC3_Msk & ((value) << TCC_SYNCBUSY_CC3_Pos))
#define TCC_SYNCBUSY_Msk                      (0x00000FFFUL)                                 /**< (TCC_SYNCBUSY) Register Mask  */

/* -------- TCC_FCTRLA : (TCC Offset: 0x0C) (R/W 32) Recoverable Fault A Configuration -------- */
#define TCC_FCTRLA_SRC_Pos                    (0U)                                           /**< (TCC_FCTRLA) Fault A Source Position */
#define TCC_FCTRLA_SRC_Msk                    (0x3U << TCC_FCTRLA_SRC_Pos)                   /**< (TCC_FCTRLA) Fault A Source Mask */
#define TCC_FCTRLA_SRC(value)                 (TCC_FCTRLA_SRC_Msk & ((value) << TCC_FCTRLA_SRC_Pos))
#define   TCC_FCTRLA_SRC_DISABLE_Val          (0U)                                           /**< (TCC_FCTRLA) Fault input disabled  */
#define   TCC_FCTRLA_SRC_ENABLE_Val           (1U)                                           /**< (TCC_FCTRLA) MCEx (x=0,1) event input  */
#define   TCC_FCTRLA_SRC_INVERT_Val           (2U)                                           /**< (TCC_FCTRLA) Inverted MCEx (x=0,1) event input  */
#define   TCC_FCTRLA_SRC_ALTFAULT_Val         (3U)                                           /**< (TCC_FCTRLA) Alternate fault (A or B) state at the end of the previous period  */
#define TCC_FCTRLA_SRC_DISABLE                (TCC_FCTRLA_SRC_DISABLE_Val << TCC_FCTRLA_SRC_Pos) /**< (TCC_FCTRLA) Fault input disabled Position  */
#define TCC_FCTRLA_SRC_ENABLE                 (TCC_FCTRLA_SRC_ENABLE_Val << TCC_FCTRLA_SRC_Pos) /**< (TCC_FCTRLA) MCEx (x=0,1) event input Position  */
#define TCC_FCTRLA_SRC_INVERT                 (TCC_FCTRLA_SRC_INVERT_Val << TCC_FCTRLA_SRC_Pos) /**< (TCC_FCTRLA) Inverted MCEx (x=0,1) event input Position  */
#define TCC_FCTRLA_SRC_ALTFAULT               (TCC_FCTRLA_SRC_ALTFAULT_Val << TCC_FCTRLA_SRC_Pos) /**< (TCC_FCTRLA) Alternate fault (A or B) state at the end of the previous period Position  */
#define TCC_FCTRLA_KEEP_Pos                   (3U)                                           /**< (TCC_FCTRLA) Fault A Keeper Position */
#define TCC_FCTRLA_KEEP_Msk                   (0x1U << TCC_FCTRLA_KEEP_Pos)                  /**< (TCC_FCTRLA) Fault A Keeper Mask */
#define TCC_FCTRLA_KEEP(value)                (TCC_FCTRLA_KEEP_Msk & ((value) << TCC_FCTRLA_KEEP_Pos))
#define TCC_FCTRLA_QUAL_Pos                   (4U)                                           /**< (TCC_FCTRLA) Fault A Qualification Position */
#define TCC_FCTRLA_QUAL_Msk                   (0x1U << TCC_FCTRLA_QUAL_Pos)                  /**< (TCC_FCTRLA) Fault A Qualification Mask */
#define TCC_FCTRLA_QUAL(value)                (TCC_FCTRLA_QUAL_Msk & ((value) << TCC_FCTRLA_QUAL_Pos))
#define TCC_FCTRLA_BLANK_Pos                  (5U)                                           /**< (TCC_FCTRLA) Fault A Blanking Mode Position */
#define TCC_FCTRLA_BLANK_Msk                  (0x3U << TCC_FCTRLA_BLANK_Pos)                 /**< (TCC_FCTRLA) Fault A Blanking Mode Mask */
#define TCC_FCTRLA_BLANK(value)               (TCC_FCTRLA_BLANK_Msk & ((value) << TCC_FCTRLA_BLANK_Pos))
#define   TCC_FCTRLA_BLANK_START_Val          (0U)                                           /**< (TCC_FCTRLA) Blanking applied from start of the ramp  */
#define   TCC_FCTRLA_BLANK_RISE_Val           (1U)                                           /**< (TCC_FCTRLA) Blanking applied from rising edge of the output waveform  */
#define   TCC_FCTRLA_BLANK_FALL_Val           (2U)                                           /**< (TCC_FCTRLA) Blanking applied from falling edge of the output waveform  */
#define   TCC_FCTRLA_BLANK_BOTH_Val           (3U)                                           /**< (TCC_FCTRLA) Blanking applied from each toggle of the output waveform  */
#define TCC_FCTRLA_BLANK_START                (TCC_FCTRLA_BLANK_START_Val << TCC_FCTRLA_BLANK_Pos) /**< (TCC_FCTRLA) Blanking applied from start of the ramp Position  */
#define TCC_FCTRLA_BLANK_RISE                 (TCC_FCTRLA_BLANK_RISE_Val << TCC_FCTRLA_BLANK_Pos) /**< (TCC_FCTRLA) Blanking applied from rising edge of the output waveform Position  */
#define TCC_FCTRLA_BLANK_FALL                 (TCC_FCTRLA_BLANK_FALL_Val << TCC_FCTRLA_BLANK_Pos) /**< (TCC_FCTRLA) Blanking applied from falling edge of the output waveform Position  */
#define TCC_FCTRLA_BLANK_BOTH                 (TCC_FCTRLA_BLANK_BOTH_Val << TCC_FCTRLA_BLANK_Pos) /**< (TCC_FCTRLA) Blanking applied from each toggle of the output waveform Position  */
#define TCC_FCTRLA_RESTART_Pos                (7U)                                           /**< (TCC_FCTRLA) Fault A Restart Position */
#define TCC_FCTRLA_RESTART_Msk                (0x1U << TCC_FCTRLA_RESTART_Pos)               /**< (TCC_FCTRLA) Fault A Restart Mask */
#define TCC_FCTRLA_RESTART(value)             (TCC_FCTRLA_RESTART_Msk & ((value) << TCC_FCTRLA_RESTART_Pos))
#define TCC_FCTRLA_HALT_Pos                   (8U)                                           /**< (TCC_FCTRLA) Fault A Halt Mode Position */
#define TCC_FCTRLA_HALT_Msk                   (0x3U << TCC_FCTRLA_HALT_Pos)                  /**< (TCC_FCTRLA) Fault A Halt Mode Mask */
#define TCC_FCTRLA_HALT(value)                (TCC_FCTRLA_HALT_Msk & ((value) << TCC_FCTRLA_HALT_Pos))
#define   TCC_FCTRLA_HALT_DISABLE_Val         (0U)                                           /**< (TCC_FCTRLA) Halt action disabled  */
#define   TCC_FCTRLA_HALT_HW_Val              (1U)                                           /**< (TCC_FCTRLA) Hardware halt action  */
#define   TCC_FCTRLA_HALT_SW_Val              (2U)                                           /**< (TCC_FCTRLA) Software halt action  */
#define   TCC_FCTRLA_HALT_NR_Val              (3U)                                           /**< (TCC_FCTRLA) Non-recoverable fault  */
#define TCC_FCTRLA_HALT_DISABLE               (TCC_FCTRLA_HALT_DISABLE_Val << TCC_FCTRLA_HALT_Pos) /**< (TCC_FCTRLA) Halt action disabled Position  */
#define TCC_FCTRLA_HALT_HW                    (TCC_FCTRLA_HALT_HW_Val << TCC_FCTRLA_HALT_Pos) /**< (TCC_FCTRLA) Hardware halt action Position  */
#define TCC_FCTRLA_HALT_SW                    (TCC_FCTRLA_HALT_SW_Val << TCC_FCTRLA_HALT_Pos) /**< (TCC_FCTRLA) Software halt action Position  */
#define TCC_FCTRLA_HALT_NR                    (TCC_FCTRLA_HALT_NR_Val << TCC_FCTRLA_HALT_Pos) /**< (TCC_FCTRLA) Non-recoverable fault Position  */
#define TCC_FCTRLA_CHSEL_Pos                  (10U)                                          /**< (TCC_FCTRLA) Fault A Capture Channel Position */
#define TCC_FCTRLA_CHSEL_Msk                  (0x3U << TCC_FCTRLA_CHSEL_Pos)                 /**< (TCC_FCTRLA) Fault A Capture Channel Mask */
#define TCC_FCTRLA_CHSEL(value)               (TCC_FCTRLA_CHSEL_Msk & ((value) << TCC_FCTRLA_CHSEL_Pos))
#define   TCC_FCTRLA_CHSEL_CC0_Val            (0U)                                           /**< (TCC_FCTRLA) Capture value stored in channel 0  */
#define   TCC_FCTRLA_CHSEL_CC1_Val            (1U)                                           /**< (TCC_FCTRLA) Capture value stored in channel 1  */
#define   TCC_FCTRLA_CHSEL_CC2_Val            (2U)                                           /**< (TCC_FCTRLA) Capture value stored in channel 2  */
#define   TCC_FCTRLA_CHSEL_CC3_Val            (3U)                                           /**< (TCC_FCTRLA) Capture value stored in channel 3  */
#define TCC_FCTRLA_CHSEL_CC0                  (TCC_FCTRLA_CHSEL_CC0_Val << TCC_FCTRLA_CHSEL_Pos) /**< (TCC_FCTRLA) Capture value stored in channel 0 Position  */
#define TCC_FCTRLA_CHSEL_CC1                  (TCC_FCTRLA_CHSEL_CC1_Val << TCC_FCTRLA_CHSEL_Pos) /**< (TCC_FCTRLA) Capture value stored in channel 1 Position  */
#define TCC_FCTRLA_CHSEL_CC2                  (TCC_FCTRLA_CHSEL_CC2_Val << TCC_FCTRLA_CHSEL_Pos) /**< (TCC_FCTRLA) Capture value stored in channel 2 Position  */
#define TCC_FCTRLA_CHSEL_CC3                  (TCC_FCTRLA_CHSEL_CC3_Val << TCC_FCTRLA_CHSEL_Pos) /**< (TCC_FCTRLA) Capture value stored in channel 3 Position  */
#define TCC_FCTRLA_CAPTURE_Pos                (12U)                                          /**< (TCC_FCTRLA) Fault A Capture Action Position */
#define TCC_FCTRLA_CAPTURE_Msk                (0x7U << TCC_FCTRLA_CAPTURE_Pos)               /**< (TCC_FCTRLA) Fault A Capture Action Mask */
#define TCC_FCTRLA_CAPTURE(value)             (TCC_FCTRLA_CAPTURE_Msk & ((value) << TCC_FCTRLA_CAPTURE_Pos))
#define   TCC_FCTRLA_CAPTURE_DISABLE_Val      (0U)                                           /**< (TCC_FCTRLA) No capture  */
#define   TCC_FCTRLA_CAPTURE_CAPT_Val         (1U)                                           /**< (TCC_FCTRLA) Capture on fault  */
#define   TCC_FCTRLA_CAPTURE_CAPTMIN_Val      (2U)                                           /**< (TCC_FCTRLA) Minimum capture  */
#define   TCC_FCTRLA_CAPTURE_CAPTMAX_Val      (3U)                                           /**< (TCC_FCTRLA) Maximum capture  */
#define   TCC_FCTRLA_CAPTURE_LOCMIN_Val       (4U)                                           /**< (TCC_FCTRLA) Minimum local detection  */
#define   TCC_FCTRLA_CAPTURE_LOCMAX_Val       (5U)                                           /**< (TCC_FCTRLA) Maximum local detection  */
#define   TCC_FCTRLA_CAPTURE_DERIV0_Val       (6U)                                           /**< (TCC_FCTRLA) Minimum and maximum local detection  */
#define   TCC_FCTRLA_CAPTURE_CAPTMARK_Val     (7U)                                           /**< (TCC_FCTRLA) Capture with ramp index as MSB value  */
#define TCC_FCTRLA_CAPTURE_DISABLE            (TCC_FCTRLA_CAPTURE_DISABLE_Val << TCC_FCTRLA_CAPTURE_Pos) /**< (TCC_FCTRLA) No capture Position  */
#define TCC_FCTRLA_CAPTURE_CAPT               (TCC_FCTRLA_CAPTURE_CAPT_Val << TCC_FCTRLA_CAPTURE_Pos) /**< (TCC_FCTRLA) Capture on fault Position  */
#define TCC_FCTRLA_CAPTURE_CAPTMIN            (TCC_FCTRLA_CAPTURE_CAPTMIN_Val << TCC_FCTRLA_CAPTURE_Pos) /**< (TCC_FCTRLA) Minimum capture Position  */
#define TCC_FCTRLA_CAPTURE_CAPTMAX            (TCC_FCTRLA_CAPTURE_CAPTMAX_Val << TCC_FCTRLA_CAPTURE_Pos) /**< (TCC_FCTRLA) Maximum capture Position  */
#define TCC_FCTRLA_CAPTURE_LOCMIN             (TCC_FCTRLA_CAPTURE_LOCMIN_Val << TCC_FCTRLA_CAPTURE_Pos) /**< (TCC_FCTRLA) Minimum local detection Position  */
#define TCC_FCTRLA_CAPTURE_LOCMAX             (TCC_FCTRLA_CAPTURE_LOCMAX_Val << TCC_FCTRLA_CAPTURE_Pos) /**< (TCC_FCTRLA) Maximum local detection Position  */
#define TCC_FCTRLA_CAPTURE_DERIV0             (TCC_FCTRLA_CAPTURE_DERIV0_Val << TCC_FCTRLA_CAPTURE_Pos) /**< (TCC_FCTRLA) Minimum and maximum local detection Position  */
#define TCC_FCTRLA_CAPTURE_CAPTMARK           (TCC_FCTRLA_CAPTURE_CAPTMARK_Val << TCC_FCTRLA_CAPTURE_Pos) /**< (TCC_FCTRLA) Capture with ramp index as MSB value Position  */
#define TCC_FCTRLA_BLANKPRESC_Pos             (15U)                                          /**< (TCC_FCTRLA) Fault A Blanking Prescaler Position */
#define TCC_FCTRLA_BLANKPRESC_Msk             (0x1U << TCC_FCTRLA_BLANKPRESC_Pos)            /**< (TCC_FCTRLA) Fault A Blanking Prescaler Mask */
#define TCC_FCTRLA_BLANKPRESC(value)          (TCC_FCTRLA_BLANKPRESC_Msk & ((value) << TCC_FCTRLA_BLANKPRESC_Pos))
#define TCC_FCTRLA_BLANKVAL_Pos               (16U)                                          /**< (TCC_FCTRLA) Fault A Blanking Time Position */
#define TCC_FCTRLA_BLANKVAL_Msk               (0xFFU << TCC_FCTRLA_BLANKVAL_Pos)             /**< (TCC_FCTRLA) Fault A Blanking Time Mask */
#define TCC_FCTRLA_BLANKVAL(value)            (TCC_FCTRLA_BLANKVAL_Msk & ((value) << TCC_FCTRLA_BLANKVAL_Pos))
#define TCC_FCTRLA_FILTERVAL_Pos              (24U)                                          /**< (TCC_FCTRLA) Fault A Filter Value Position */
#define TCC_FCTRLA_FILTERVAL_Msk              (0xFU << TCC_FCTRLA_FILTERVAL_Pos)             /**< (TCC_FCTRLA) Fault A Filter Value Mask */
#define TCC_FCTRLA_FILTERVAL(value)           (TCC_FCTRLA_FILTERVAL_Msk & ((value) << TCC_FCTRLA_FILTERVAL_Pos))
#define TCC_FCTRLA_Msk                        (0x0FFFFFFBUL)                                 /**< (TCC_FCTRLA) Register Mask  */

/* -------- TCC_FCTRLB : (TCC Offset: 0x10) (R/W 32) Recoverable Fault B Configuration -------- */
#define TCC_FCTRLB_SRC_Pos                    (0U)                                           /**< (TCC_FCTRLB) Fault B Source Position */
#define TCC_FCTRLB_SRC_Msk                    (0x3U << TCC_FCTRLB_SRC_Pos)                   /**< (TCC_FCTRLB) Fault B Source Mask */
#define TCC_FCTRLB_SRC(value)                 (TCC_FCTRLB_SRC_Msk & ((value) << TCC_FCTRLB_SRC_Pos))
#define   TCC_FCTRLB_SRC_DISABLE_Val          (0U)                                           /**< (TCC_FCTRLB) Fault input disabled  */
#define   TCC_FCTRLB_SRC_ENABLE_Val           (1U)                                           /**< (TCC_FCTRLB) MCEx (x=0,1) event input  */
#define   TCC_FCTRLB_SRC_INVERT_Val           (2U)                                           /**< (TCC_FCTRLB) Inverted MCEx (x=0,1) event input  */
#define   TCC_FCTRLB_SRC_ALTFAULT_Val         (3U)                                           /**< (TCC_FCTRLB) Alternate fault (A or B) state at the end of the previous period  */
#define TCC_FCTRLB_SRC_DISABLE                (TCC_FCTRLB_SRC_DISABLE_Val << TCC_FCTRLB_SRC_Pos) /**< (TCC_FCTRLB) Fault input disabled Position  */
#define TCC_FCTRLB_SRC_ENABLE                 (TCC_FCTRLB_SRC_ENABLE_Val << TCC_FCTRLB_SRC_Pos) /**< (TCC_FCTRLB) MCEx (x=0,1) event input Position  */
#define TCC_FCTRLB_SRC_INVERT                 (TCC_FCTRLB_SRC_INVERT_Val << TCC_FCTRLB_SRC_Pos) /**< (TCC_FCTRLB) Inverted MCEx (x=0,1) event input Position  */
#define TCC_FCTRLB_SRC_ALTFAULT               (TCC_FCTRLB_SRC_ALTFAULT_Val << TCC_FCTRLB_SRC_Pos) /**< (TCC_FCTRLB) Alternate fault (A or B) state at the end of the previous period Position  */
#define TCC_FCTRLB_KEEP_Pos                   (3U)                                           /**< (TCC_FCTRLB) Fault B Keeper Position */
#define TCC_FCTRLB_KEEP_Msk                   (0x1U << TCC_FCTRLB_KEEP_Pos)                  /**< (TCC_FCTRLB) Fault B Keeper Mask */
#define TCC_FCTRLB_KEEP(value)                (TCC_FCTRLB_KEEP_Msk & ((value) << TCC_FCTRLB_KEEP_Pos))
#define TCC_FCTRLB_QUAL_Pos                   (4U)                                           /**< (TCC_FCTRLB) Fault B Qualification Position */
#define TCC_FCTRLB_QUAL_Msk                   (0x1U << TCC_FCTRLB_QUAL_Pos)                  /**< (TCC_FCTRLB) Fault B Qualification Mask */
#define TCC_FCTRLB_QUAL(value)                (TCC_FCTRLB_QUAL_Msk & ((value) << TCC_FCTRLB_QUAL_Pos))
#define TCC_FCTRLB_BLANK_Pos                  (5U)                                           /**< (TCC_FCTRLB) Fault B Blanking Mode Position */
#define TCC_FCTRLB_BLANK_Msk                  (0x3U << TCC_FCTRLB_BLANK_Pos)                 /**< (TCC_FCTRLB) Fault B Blanking Mode Mask */
#define TCC_FCTRLB_BLANK(value)               (TCC_FCTRLB_BLANK_Msk & ((value) << TCC_FCTRLB_BLANK_Pos))
#define   TCC_FCTRLB_BLANK_START_Val          (0U)                                           /**< (TCC_FCTRLB) Blanking applied from start of the ramp  */
#define   TCC_FCTRLB_BLANK_RISE_Val           (1U)                                           /**< (TCC_FCTRLB) Blanking applied from rising edge of the output waveform  */
#define   TCC_FCTRLB_BLANK_FALL_Val           (2U)                                           /**< (TCC_FCTRLB) Blanking applied from falling edge of the output waveform  */
#define   TCC_FCTRLB_BLANK_BOTH_Val           (3U)                                           /**< (TCC_FCTRLB) Blanking applied from each toggle of the output waveform  */
#define TCC_FCTRLB_BLANK_START                (TCC_FCTRLB_BLANK_START_Val << TCC_FCTRLB_BLANK_Pos) /**< (TCC_FCTRLB) Blanking applied from start of the ramp Position  */
#define TCC_FCTRLB_BLANK_RISE                 (TCC_FCTRLB_BLANK_RISE_Val << TCC_FCTRLB_BLANK_Pos) /**< (TCC_FCTRLB) Blanking applied from rising edge of the output waveform Position  */
#define TCC_FCTRLB_BLANK_FALL                 (TCC_FCTRLB_BLANK_FALL_Val << TCC_FCTRLB_BLANK_Pos) /**< (TCC_FCTRLB) Blanking applied from falling edge of the output waveform Position  */
#define TCC_FCTRLB_BLANK_BOTH                 (TCC_FCTRLB_BLANK_BOTH_Val << TCC_FCTRLB_BLANK_Pos) /**< (TCC_FCTRLB) Blanking applied from each toggle of the output waveform Position  */
#define TCC_FCTRLB_RESTART_Pos                (7U)                                           /**< (TCC_FCTRLB) Fault B Restart Position */
#define TCC_FCTRLB_RESTART_Msk                (0x1U << TCC_FCTRLB_RESTART_Pos)               /**< (TCC_FCTRLB) Fault B Restart Mask */
#define TCC_FCTRLB_RESTART(value)             (TCC_FCTRLB_RESTART_Msk & ((value) << TCC_FCTRLB_RESTART_Pos))
#define TCC_FCTRLB_HALT_Pos                   (8U)                                           /**< (TCC_FCTRLB) Fault B Halt Mode Position */
#define TCC_FCTRLB_HALT_Msk                   (0x3U << TCC_FCTRLB_HALT_Pos)                  /**< (TCC_FCTRLB) Fault B Halt Mode Mask */
#define TCC_FCTRLB_HALT(value)                (TCC_FCTRLB_HALT_Msk & ((value) << TCC_FCTRLB_HALT_Pos))
#define   TCC_FCTRLB_HALT_DISABLE_Val         (0U)                                           /**< (TCC_FCTRLB) Halt action disabled  */
#define   TCC_FCTRLB_HALT_HW_Val              (1U)                                           /**< (TCC_FCTRLB) Hardware halt action  */
#define   TCC_FCTRLB_HALT_SW_Val              (2U)                                           /**< (TCC_FCTRLB) Software halt action  */
#define   TCC_FCTRLB_HALT_NR_Val              (3U)                                           /**< (TCC_FCTRLB) Non-recoverable fault  */
#define TCC_FCTRLB_HALT_DISABLE               (TCC_FCTRLB_HALT_DISABLE_Val << TCC_FCTRLB_HALT_Pos) /**< (TCC_FCTRLB) Halt action disabled Position  */
#define TCC_FCTRLB_HALT_HW                    (TCC_FCTRLB_HALT_HW_Val << TCC_FCTRLB_HALT_Pos) /**< (TCC_FCTRLB) Hardware halt action Position  */
#define TCC_FCTRLB_HALT_SW                    (TCC_FCTRLB_HALT_SW_Val << TCC_FCTRLB_HALT_Pos) /**< (TCC_FCTRLB) Software halt action Position  */
#define TCC_FCTRLB_HALT_NR                    (TCC_FCTRLB_HALT_NR_Val << TCC_FCTRLB_HALT_Pos) /**< (TCC_FCTRLB) Non-recoverable fault Position  */
#define TCC_FCTRLB_CHSEL_Pos                  (10U)                                          /**< (TCC_FCTRLB) Fault B Capture Channel Position */
#define TCC_FCTRLB_CHSEL_Msk                  (0x3U << TCC_FCTRLB_CHSEL_Pos)                 /**< (TCC_FCTRLB) Fault B Capture Channel Mask */
#define TCC_FCTRLB_CHSEL(value)               (TCC_FCTRLB_CHSEL_Msk & ((value) << TCC_FCTRLB_CHSEL_Pos))
#define   TCC_FCTRLB_CHSEL_CC0_Val            (0U)                                           /**< (TCC_FCTRLB) Capture value stored in channel 0  */
#define   TCC_FCTRLB_CHSEL_CC1_Val            (1U)                                           /**< (TCC_FCTRLB) Capture value stored in channel 1  */
#define   TCC_FCTRLB_CHSEL_CC2_Val            (2U)                                           /**< (TCC_FCTRLB) Capture value stored in channel 2  */
#define   TCC_FCTRLB_CHSEL_CC3_Val            (3U)                                           /**< (TCC_FCTRLB) Capture value stored in channel 3  */
#define TCC_FCTRLB_CHSEL_CC0                  (TCC_FCTRLB_CHSEL_CC0_Val << TCC_FCTRLB_CHSEL_Pos) /**< (TCC_FCTRLB) Capture value stored in channel 0 Position  */
#define TCC_FCTRLB_CHSEL_CC1                  (TCC_FCTRLB_CHSEL_CC1_Val << TCC_FCTRLB_CHSEL_Pos) /**< (TCC_FCTRLB) Capture value stored in channel 1 Position  */
#define TCC_FCTRLB_CHSEL_CC2                  (TCC_FCTRLB_CHSEL_CC2_Val << TCC_FCTRLB_CHSEL_Pos) /**< (TCC_FCTRLB) Capture value stored in channel 2 Position  */
#define TCC_FCTRLB_CHSEL_CC3                  (TCC_FCTRLB_CHSEL_CC3_Val << TCC_FCTRLB_CHSEL_Pos) /**< (TCC_FCTRLB) Capture value stored in channel 3 Position  */
#define TCC_FCTRLB_CAPTURE_Pos                (12U)                                          /**< (TCC_FCTRLB) Fault B Capture Action Position */
#define TCC_FCTRLB_CAPTURE_Msk                (0x7U << TCC_FCTRLB_CAPTURE_Pos)               /**< (TCC_FCTRLB) Fault B Capture Action Mask */
#define TCC_FCTRLB_CAPTURE(value)             (TCC_FCTRLB_CAPTURE_Msk & ((value) << TCC_FCTRLB_CAPTURE_Pos))
#define   TCC_FCTRLB_CAPTURE_DISABLE_Val      (0U)                                           /**< (TCC_FCTRLB) No capture  */
#define   TCC_FCTRLB_CAPTURE_CAPT_Val         (1U)                                           /**< (TCC_FCTRLB) Capture on fault  */
#define   TCC_FCTRLB_CAPTURE_CAPTMIN_Val      (2U)                                           /**< (TCC_FCTRLB) Minimum capture  */
#define   TCC_FCTRLB_CAPTURE_CAPTMAX_Val      (3U)                                           /**< (TCC_FCTRLB) Maximum capture  */
#define   TCC_FCTRLB_CAPTURE_LOCMIN_Val       (4U)                                           /**< (TCC_FCTRLB) Minimum local detection  */
#define   TCC_FCTRLB_CAPTURE_LOCMAX_Val       (5U)                                           /**< (TCC_FCTRLB) Maximum local detection  */
#define   TCC_FCTRLB_CAPTURE_DERIV0_Val       (6U)                                           /**< (TCC_FCTRLB) Minimum and maximum local detection  */
#define   TCC_FCTRLB_CAPTURE_CAPTMARK_Val     (7U)                                           /**< (TCC_FCTRLB) Capture with ramp index as MSB value  */
#define TCC_FCTRLB_CAPTURE_DISABLE            (TCC_FCTRLB_CAPTURE_DISABLE_Val << TCC_FCTRLB_CAPTURE_Pos) /**< (TCC_FCTRLB) No capture Position  */
#define TCC_FCTRLB_CAPTURE_CAPT               (TCC_FCTRLB_CAPTURE_CAPT_Val << TCC_FCTRLB_CAPTURE_Pos) /**< (TCC_FCTRLB) Capture on fault Position  */
#define TCC_FCTRLB_CAPTURE_CAPTMIN            (TCC_FCTRLB_CAPTURE_CAPTMIN_Val << TCC_FCTRLB_CAPTURE_Pos) /**< (TCC_FCTRLB) Minimum capture Position  */
#define TCC_FCTRLB_CAPTURE_CAPTMAX            (TCC_FCTRLB_CAPTURE_CAPTMAX_Val << TCC_FCTRLB_CAPTURE_Pos) /**< (TCC_FCTRLB) Maximum capture Position  */
#define TCC_FCTRLB_CAPTURE_LOCMIN             (TCC_FCTRLB_CAPTURE_LOCMIN_Val << TCC_FCTRLB_CAPTURE_Pos) /**< (TCC_FCTRLB) Minimum local detection Position  */
#define TCC_FCTRLB_CAPTURE_LOCMAX             (TCC_FCTRLB_CAPTURE_LOCMAX_Val << TCC_FCTRLB_CAPTURE_Pos) /**< (TCC_FCTRLB) Maximum local detection Position  */
#define TCC_FCTRLB_CAPTURE_DERIV0             (TCC_FCTRLB_CAPTURE_DERIV0_Val << TCC_FCTRLB_CAPTURE_Pos) /**< (TCC_FCTRLB) Minimum and maximum local detection Position  */
#define TCC_FCTRLB_CAPTURE_CAPTMARK           (TCC_FCTRLB_CAPTURE_CAPTMARK_Val << TCC_FCTRLB_CAPTURE_Pos) /**< (TCC_FCTRLB) Capture with ramp index as MSB value Position  */
#define TCC_FCTRLB_BLANKPRESC_Pos             (15U)                                          /**< (TCC_FCTRLB) Fault B Blanking Prescaler Position */
#define TCC_FCTRLB_BLANKPRESC_Msk             (0x1U << TCC_FCTRLB_BLANKPRESC_Pos)            /**< (TCC_FCTRLB) Fault B Blanking Prescaler Mask */
#define TCC_FCTRLB_BLANKPRESC(value)          (TCC_FCTRLB_BLANKPRESC_Msk & ((value) << TCC_FCTRLB_BLANKPRESC_Pos))
#define TCC_FCTRLB_BLANKVAL_Pos               (16U)                                          /**< (TCC_FCTRLB) Fault B Blanking Time Position */
#define TCC_FCTRLB_BLANKVAL_Msk               (0xFFU << TCC_FCTRLB_BLANKVAL_Pos)             /**< (TCC_FCTRLB) Fault B Blanking Time Mask */
#define TCC_FCTRLB_BLANKVAL(value)            (TCC_FCTRLB_BLANKVAL_Msk & ((value) << TCC_FCTRLB_BLANKVAL_Pos))
#define TCC_FCTRLB_FILTERVAL_Pos              (24U)                                          /**< (TCC_FCTRLB) Fault B Filter Value Position */
#define TCC_FCTRLB_FILTERVAL_Msk              (0xFU << TCC_FCTRLB_FILTERVAL_Pos)             /**< (TCC_FCTRLB) Fault B Filter Value Mask */
#define TCC_FCTRLB_FILTERVAL(value)           (TCC_FCTRLB_FILTERVAL_Msk & ((value) << TCC_FCTRLB_FILTERVAL_Pos))
#define TCC_FCTRLB_Msk                        (0x0FFFFFFBUL)                                 /**< (TCC_FCTRLB) Register Mask  */

/* -------- TCC_WEXCTRL : (TCC Offset: 0x14) (R/W 32) Waveform Extension Configuration -------- */
#define TCC_WEXCTRL_OTMX_Pos                  (0U)                                           /**< (TCC_WEXCTRL) Output Matrix Position */
#define TCC_WEXCTRL_OTMX_Msk                  (0x3U << TCC_WEXCTRL_OTMX_Pos)                 /**< (TCC_WEXCTRL) Output Matrix Mask */
#define TCC_WEXCTRL_OTMX(value)               (TCC_WEXCTRL_OTMX_Msk & ((value) << TCC_WEXCTRL_OTMX_Pos))
#define TCC_WEXCTRL_DTIEN0_Pos                (8U)                                           /**< (TCC_WEXCTRL) Dead-time Insertion Generator 0 Enable Position */
#define TCC_WEXCTRL_DTIEN0_Msk                (0x1U << TCC_WEXCTRL_DTIEN0_Pos)               /**< (TCC_WEXCTRL) Dead-time Insertion Generator 0 Enable Mask */
#define TCC_WEXCTRL_DTIEN0(value)             (TCC_WEXCTRL_DTIEN0_Msk & ((value) << TCC_WEXCTRL_DTIEN0_Pos))
#define TCC_WEXCTRL_DTIEN1_Pos                (9U)                                           /**< (TCC_WEXCTRL) Dead-time Insertion Generator 1 Enable Position */
#define TCC_WEXCTRL_DTIEN1_Msk                (0x1U << TCC_WEXCTRL_DTIEN1_Pos)               /**< (TCC_WEXCTRL) Dead-time Insertion Generator 1 Enable Mask */
#define TCC_WEXCTRL_DTIEN1(value)             (TCC_WEXCTRL_DTIEN1_Msk & ((value) << TCC_WEXCTRL_DTIEN1_Pos))
#define TCC_WEXCTRL_DTIEN2_Pos                (10U)                                          /**< (TCC_WEXCTRL) Dead-time Insertion Generator 2 Enable Position */
#define TCC_WEXCTRL_DTIEN2_Msk                (0x1U << TCC_WEXCTRL_DTIEN2_Pos)               /**< (TCC_WEXCTRL) Dead-time Insertion Generator 2 Enable Mask */
#define TCC_WEXCTRL_DTIEN2(value)             (TCC_WEXCTRL_DTIEN2_Msk & ((value) << TCC_WEXCTRL_DTIEN2_Pos))
#define TCC_WEXCTRL_DTIEN3_Pos                (11U)                                          /**< (TCC_WEXCTRL) Dead-time Insertion Generator 3 Enable Position */
#define TCC_WEXCTRL_DTIEN3_Msk                (0x1U << TCC_WEXCTRL_DTIEN3_Pos)               /**< (TCC_WEXCTRL) Dead-time Insertion Generator 3 Enable Mask */
#define TCC_WEXCTRL_DTIEN3(value)             (TCC_WEXCTRL_DTIEN3_Msk & ((value) << TCC_WEXCTRL_DTIEN3_Pos))
#define TCC_WEXCTRL_DTLS_Pos                  (16U)                                          /**< (TCC_WEXCTRL) Dead-time Low Side Outputs Value Position */
#define TCC_WEXCTRL_DTLS_Msk                  (0xFFU << TCC_WEXCTRL_DTLS_Pos)                /**< (TCC_WEXCTRL) Dead-time Low Side Outputs Value Mask */
#define TCC_WEXCTRL_DTLS(value)               (TCC_WEXCTRL_DTLS_Msk & ((value) << TCC_WEXCTRL_DTLS_Pos))
#define TCC_WEXCTRL_DTHS_Pos                  (24U)                                          /**< (TCC_WEXCTRL) Dead-time High Side Outputs Value Position */
#define TCC_WEXCTRL_DTHS_Msk                  (0xFFU << TCC_WEXCTRL_DTHS_Pos)                /**< (TCC_WEXCTRL) Dead-time High Side Outputs Value Mask */
#define TCC_WEXCTRL_DTHS(value)               (TCC_WEXCTRL_DTHS_Msk & ((value) << TCC_WEXCTRL_DTHS_Pos))
#define TCC_WEXCTRL_Msk                       (0xFFFF0F03UL)                                 /**< (TCC_WEXCTRL) Register Mask  */

/* -------- TCC_DRVCTRL : (TCC Offset: 0x18) (R/W 32) Driver Control -------- */
#define TCC_DRVCTRL_NRE0_Pos                  (0U)                                           /**< (TCC_DRVCTRL) Non-Recoverable State 0 Output Enable Position */
#define TCC_DRVCTRL_NRE0_Msk                  (0x1U << TCC_DRVCTRL_NRE0_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 0 Output Enable Mask */
#define TCC_DRVCTRL_NRE0(value)               (TCC_DRVCTRL_NRE0_Msk & ((value) << TCC_DRVCTRL_NRE0_Pos))
#define TCC_DRVCTRL_NRE1_Pos                  (1U)                                           /**< (TCC_DRVCTRL) Non-Recoverable State 1 Output Enable Position */
#define TCC_DRVCTRL_NRE1_Msk                  (0x1U << TCC_DRVCTRL_NRE1_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 1 Output Enable Mask */
#define TCC_DRVCTRL_NRE1(value)               (TCC_DRVCTRL_NRE1_Msk & ((value) << TCC_DRVCTRL_NRE1_Pos))
#define TCC_DRVCTRL_NRE2_Pos                  (2U)                                           /**< (TCC_DRVCTRL) Non-Recoverable State 2 Output Enable Position */
#define TCC_DRVCTRL_NRE2_Msk                  (0x1U << TCC_DRVCTRL_NRE2_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 2 Output Enable Mask */
#define TCC_DRVCTRL_NRE2(value)               (TCC_DRVCTRL_NRE2_Msk & ((value) << TCC_DRVCTRL_NRE2_Pos))
#define TCC_DRVCTRL_NRE3_Pos                  (3U)                                           /**< (TCC_DRVCTRL) Non-Recoverable State 3 Output Enable Position */
#define TCC_DRVCTRL_NRE3_Msk                  (0x1U << TCC_DRVCTRL_NRE3_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 3 Output Enable Mask */
#define TCC_DRVCTRL_NRE3(value)               (TCC_DRVCTRL_NRE3_Msk & ((value) << TCC_DRVCTRL_NRE3_Pos))
#define TCC_DRVCTRL_NRE4_Pos                  (4U)                                           /**< (TCC_DRVCTRL) Non-Recoverable State 4 Output Enable Position */
#define TCC_DRVCTRL_NRE4_Msk                  (0x1U << TCC_DRVCTRL_NRE4_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 4 Output Enable Mask */
#define TCC_DRVCTRL_NRE4(value)               (TCC_DRVCTRL_NRE4_Msk & ((value) << TCC_DRVCTRL_NRE4_Pos))
#define TCC_DRVCTRL_NRE5_Pos                  (5U)                                           /**< (TCC_DRVCTRL) Non-Recoverable State 5 Output Enable Position */
#define TCC_DRVCTRL_NRE5_Msk                  (0x1U << TCC_DRVCTRL_NRE5_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 5 Output Enable Mask */
#define TCC_DRVCTRL_NRE5(value)               (TCC_DRVCTRL_NRE5_Msk & ((value) << TCC_DRVCTRL_NRE5_Pos))
#define TCC_DRVCTRL_NRE6_Pos                  (6U)                                           /**< (TCC_DRVCTRL) Non-Recoverable State 6 Output Enable Position */
#define TCC_DRVCTRL_NRE6_Msk                  (0x1U << TCC_DRVCTRL_NRE6_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 6 Output Enable Mask */
#define TCC_DRVCTRL_NRE6(value)               (TCC_DRVCTRL_NRE6_Msk & ((value) << TCC_DRVCTRL_NRE6_Pos))
#define TCC_DRVCTRL_NRE7_Pos                  (7U)                                           /**< (TCC_DRVCTRL) Non-Recoverable State 7 Output Enable Position */
#define TCC_DRVCTRL_NRE7_Msk                  (0x1U << TCC_DRVCTRL_NRE7_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 7 Output Enable Mask */
#define TCC_DRVCTRL_NRE7(value)               (TCC_DRVCTRL_NRE7_Msk & ((value) << TCC_DRVCTRL_NRE7_Pos))
#define TCC_DRVCTRL_NRV0_Pos                  (8U)                                           /**< (TCC_DRVCTRL) Non-Recoverable State 0 Output Value Position */
#define TCC_DRVCTRL_NRV0_Msk                  (0x1U << TCC_DRVCTRL_NRV0_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 0 Output Value Mask */
#define TCC_DRVCTRL_NRV0(value)               (TCC_DRVCTRL_NRV0_Msk & ((value) << TCC_DRVCTRL_NRV0_Pos))
#define TCC_DRVCTRL_NRV1_Pos                  (9U)                                           /**< (TCC_DRVCTRL) Non-Recoverable State 1 Output Value Position */
#define TCC_DRVCTRL_NRV1_Msk                  (0x1U << TCC_DRVCTRL_NRV1_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 1 Output Value Mask */
#define TCC_DRVCTRL_NRV1(value)               (TCC_DRVCTRL_NRV1_Msk & ((value) << TCC_DRVCTRL_NRV1_Pos))
#define TCC_DRVCTRL_NRV2_Pos                  (10U)                                          /**< (TCC_DRVCTRL) Non-Recoverable State 2 Output Value Position */
#define TCC_DRVCTRL_NRV2_Msk                  (0x1U << TCC_DRVCTRL_NRV2_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 2 Output Value Mask */
#define TCC_DRVCTRL_NRV2(value)               (TCC_DRVCTRL_NRV2_Msk & ((value) << TCC_DRVCTRL_NRV2_Pos))
#define TCC_DRVCTRL_NRV3_Pos                  (11U)                                          /**< (TCC_DRVCTRL) Non-Recoverable State 3 Output Value Position */
#define TCC_DRVCTRL_NRV3_Msk                  (0x1U << TCC_DRVCTRL_NRV3_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 3 Output Value Mask */
#define TCC_DRVCTRL_NRV3(value)               (TCC_DRVCTRL_NRV3_Msk & ((value) << TCC_DRVCTRL_NRV3_Pos))
#define TCC_DRVCTRL_NRV4_Pos                  (12U)                                          /**< (TCC_DRVCTRL) Non-Recoverable State 4 Output Value Position */
#define TCC_DRVCTRL_NRV4_Msk                  (0x1U << TCC_DRVCTRL_NRV4_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 4 Output Value Mask */
#define TCC_DRVCTRL_NRV4(value)               (TCC_DRVCTRL_NRV4_Msk & ((value) << TCC_DRVCTRL_NRV4_Pos))
#define TCC_DRVCTRL_NRV5_Pos                  (13U)                                          /**< (TCC_DRVCTRL) Non-Recoverable State 5 Output Value Position */
#define TCC_DRVCTRL_NRV5_Msk                  (0x1U << TCC_DRVCTRL_NRV5_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 5 Output Value Mask */
#define TCC_DRVCTRL_NRV5(value)               (TCC_DRVCTRL_NRV5_Msk & ((value) << TCC_DRVCTRL_NRV5_Pos))
#define TCC_DRVCTRL_NRV6_Pos                  (14U)                                          /**< (TCC_DRVCTRL) Non-Recoverable State 6 Output Value Position */
#define TCC_DRVCTRL_NRV6_Msk                  (0x1U << TCC_DRVCTRL_NRV6_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 6 Output Value Mask */
#define TCC_DRVCTRL_NRV6(value)               (TCC_DRVCTRL_NRV6_Msk & ((value) << TCC_DRVCTRL_NRV6_Pos))
#define TCC_DRVCTRL_NRV7_Pos                  (15U)                                          /**< (TCC_DRVCTRL) Non-Recoverable State 7 Output Value Position */
#define TCC_DRVCTRL_NRV7_Msk                  (0x1U << TCC_DRVCTRL_NRV7_Pos)                 /**< (TCC_DRVCTRL) Non-Recoverable State 7 Output Value Mask */
#define TCC_DRVCTRL_NRV7(value)               (TCC_DRVCTRL_NRV7_Msk & ((value) << TCC_DRVCTRL_NRV7_Pos))
#define TCC_DRVCTRL_INVEN0_Pos                (16U)                                          /**< (TCC_DRVCTRL) Output Waveform 0 Inversion Position */
#define TCC_DRVCTRL_INVEN0_Msk                (0x1U << TCC_DRVCTRL_INVEN0_Pos)               /**< (TCC_DRVCTRL) Output Waveform 0 Inversion Mask */
#define TCC_DRVCTRL_INVEN0(value)             (TCC_DRVCTRL_INVEN0_Msk & ((value) << TCC_DRVCTRL_INVEN0_Pos))
#define TCC_DRVCTRL_INVEN1_Pos                (17U)                                          /**< (TCC_DRVCTRL) Output Waveform 1 Inversion Position */
#define TCC_DRVCTRL_INVEN1_Msk                (0x1U << TCC_DRVCTRL_INVEN1_Pos)               /**< (TCC_DRVCTRL) Output Waveform 1 Inversion Mask */
#define TCC_DRVCTRL_INVEN1(value)             (TCC_DRVCTRL_INVEN1_Msk & ((value) << TCC_DRVCTRL_INVEN1_Pos))
#define TCC_DRVCTRL_INVEN2_Pos                (18U)                                          /**< (TCC_DRVCTRL) Output Waveform 2 Inversion Position */
#define TCC_DRVCTRL_INVEN2_Msk                (0x1U << TCC_DRVCTRL_INVEN2_Pos)               /**< (TCC_DRVCTRL) Output Waveform 2 Inversion Mask */
#define TCC_DRVCTRL_INVEN2(value)             (TCC_DRVCTRL_INVEN2_Msk & ((value) << TCC_DRVCTRL_INVEN2_Pos))
#define TCC_DRVCTRL_INVEN3_Pos                (19U)                                          /**< (TCC_DRVCTRL) Output Waveform 3 Inversion Position */
#define TCC_DRVCTRL_INVEN3_Msk                (0x1U << TCC_DRVCTRL_INVEN3_Pos)               /**< (TCC_DRVCTRL) Output Waveform 3 Inversion Mask */
#define TCC_DRVCTRL_INVEN3(value)             (TCC_DRVCTRL_INVEN3_Msk & ((value) << TCC_DRVCTRL_INVEN3_Pos))
#define TCC_DRVCTRL_INVEN4_Pos                (20U)                                          /**< (TCC_DRVCTRL) Output Waveform 4 Inversion Position */
#define TCC_DRVCTRL_INVEN4_Msk                (0x1U << TCC_DRVCTRL_INVEN4_Pos)               /**< (TCC_DRVCTRL) Output Waveform 4 Inversion Mask */
#define TCC_DRVCTRL_INVEN4(value)             (TCC_DRVCTRL_INVEN4_Msk & ((value) << TCC_DRVCTRL_INVEN4_Pos))
#define TCC_DRVCTRL_INVEN5_Pos                (21U)                                          /**< (TCC_DRVCTRL) Output Waveform 5 Inversion Position */
#define TCC_DRVCTRL_INVEN5_Msk                (0x1U << TCC_DRVCTRL_INVEN5_Pos)               /**< (TCC_DRVCTRL) Output Waveform 5 Inversion Mask */
#define TCC_DRVCTRL_INVEN5(value)             (TCC_DRVCTRL_INVEN5_Msk & ((value) << TCC_DRVCTRL_INVEN5_Pos))
#define TCC_DRVCTRL_INVEN6_Pos                (22U)                                          /**< (TCC_DRVCTRL) Output Waveform 6 Inversion Position */
#define TCC_DRVCTRL_INVEN6_Msk                (0x1U << TCC_DRVCTRL_INVEN6_Pos)               /**< (TCC_DRVCTRL) Output Waveform 6 Inversion Mask */
#define TCC_DRVCTRL_INVEN6(value)             (TCC_DRVCTRL_INVEN6_Msk & ((value) << TCC_DRVCTRL_INVEN6_Pos))
#define TCC_DRVCTRL_INVEN7_Pos                (23U)                                          /**< (TCC_DRVCTRL) Output Waveform 7 Inversion Position */
#define TCC_DRVCTRL_INVEN7_Msk                (0x1U << TCC_DRVCTRL_INVEN7_Pos)               /**< (TCC_DRVCTRL) Output Waveform 7 Inversion Mask */
#define TCC_DRVCTRL_INVEN7(value)             (TCC_DRVCTRL_INVEN7_Msk & ((value) << TCC_DRVCTRL_INVEN7_Pos))
#define TCC_DRVCTRL_FILTERVAL0_Pos            (24U)                                          /**< (TCC_DRVCTRL) Non-Recoverable Fault Input 0 Filter Value Position */
#define TCC_DRVCTRL_FILTERVAL0_Msk            (0xFU << TCC_DRVCTRL_FILTERVAL0_Pos)           /**< (TCC_DRVCTRL) Non-Recoverable Fault Input 0 Filter Value Mask */
#define TCC_DRVCTRL_FILTERVAL0(value)         (TCC_DRVCTRL_FILTERVAL0_Msk & ((value) << TCC_DRVCTRL_FILTERVAL0_Pos))
#define TCC_DRVCTRL_FILTERVAL1_Pos            (28U)                                          /**< (TCC_DRVCTRL) Non-Recoverable Fault Input 1 Filter Value Position */
#define TCC_DRVCTRL_FILTERVAL1_Msk            (0xFU << TCC_DRVCTRL_FILTERVAL1_Pos)           /**< (TCC_DRVCTRL) Non-Recoverable Fault Input 1 Filter Value Mask */
#define TCC_DRVCTRL_FILTERVAL1(value)         (TCC_DRVCTRL_FILTERVAL1_Msk & ((value) << TCC_DRVCTRL_FILTERVAL1_Pos))
#define TCC_DRVCTRL_Msk                       (0xFFFFFFFFUL)                                 /**< (TCC_DRVCTRL) Register Mask  */

/* -------- TCC_DBGCTRL : (TCC Offset: 0x1E) (R/W 8) Debug Control -------- */
#define TCC_DBGCTRL_DBGRUN_Pos                (0U)                                           /**< (TCC_DBGCTRL) Debug Running Mode Position */
#define TCC_DBGCTRL_DBGRUN_Msk                (0x1U << TCC_DBGCTRL_DBGRUN_Pos)               /**< (TCC_DBGCTRL) Debug Running Mode Mask */
#define TCC_DBGCTRL_DBGRUN(value)             (TCC_DBGCTRL_DBGRUN_Msk & ((value) << TCC_DBGCTRL_DBGRUN_Pos))
#define TCC_DBGCTRL_FDDBD_Pos                 (2U)                                           /**< (TCC_DBGCTRL) Fault Detection on Debug Break Detection Position */
#define TCC_DBGCTRL_FDDBD_Msk                 (0x1U << TCC_DBGCTRL_FDDBD_Pos)                /**< (TCC_DBGCTRL) Fault Detection on Debug Break Detection Mask */
#define TCC_DBGCTRL_FDDBD(value)              (TCC_DBGCTRL_FDDBD_Msk & ((value) << TCC_DBGCTRL_FDDBD_Pos))
#define TCC_DBGCTRL_Msk                       (0x00000005UL)                                 /**< (TCC_DBGCTRL) Register Mask  */

/* -------- TCC_EVCTRL : (TCC Offset: 0x20) (R/W 32) Event Control -------- */
#define TCC_EVCTRL_EVACT0_Pos                 (0U)                                           /**< (TCC_EVCTRL) Timer/counter Input Event0 Action Position */
#define TCC_EVCTRL_EVACT0_Msk                 (0x7U << TCC_EVCTRL_EVACT0_Pos)                /**< (TCC_EVCTRL) Timer/counter Input Event0 Action Mask */
#define TCC_EVCTRL_EVACT0(value)              (TCC_EVCTRL_EVACT0_Msk & ((value) << TCC_EVCTRL_EVACT0_Pos))
#define   TCC_EVCTRL_EVACT0_OFF_Val           (0U)                                           /**< (TCC_EVCTRL) Event action disabled  */
#define   TCC_EVCTRL_EVACT0_RETRIGGER_Val     (1U)                                           /**< (TCC_EVCTRL) Start, restart or re-trigger counter on event  */
#define   TCC_EVCTRL_EVACT0_COUNTEV_Val       (2U)                                           /**< (TCC_EVCTRL) Count on event  */
#define   TCC_EVCTRL_EVACT0_START_Val         (3U)                                           /**< (TCC_EVCTRL) Start counter on event  */
#define   TCC_EVCTRL_EVACT0_INC_Val           (4U)                                           /**< (TCC_EVCTRL) Increment counter on event  */
#define   TCC_EVCTRL_EVACT0_COUNT_Val         (5U)                                           /**< (TCC_EVCTRL) Count on active state of asynchronous event  */
#define   TCC_EVCTRL_EVACT0_STAMP_Val         (6U)                                           /**< (TCC_EVCTRL) Stamp capture  */
#define   TCC_EVCTRL_EVACT0_FAULT_Val         (7U)                                           /**< (TCC_EVCTRL) Non-recoverable fault  */
#define TCC_EVCTRL_EVACT0_OFF                 (TCC_EVCTRL_EVACT0_OFF_Val << TCC_EVCTRL_EVACT0_Pos) /**< (TCC_EVCTRL) Event action disabled Position  */
#define TCC_EVCTRL_EVACT0_RETRIGGER           (TCC_EVCTRL_EVACT0_RETRIGGER_Val << TCC_EVCTRL_EVACT0_Pos) /**< (TCC_EVCTRL) Start, restart or re-trigger counter on event Position  */
#define TCC_EVCTRL_EVACT0_COUNTEV             (TCC_EVCTRL_EVACT0_COUNTEV_Val << TCC_EVCTRL_EVACT0_Pos) /**< (TCC_EVCTRL) Count on event Position  */
#define TCC_EVCTRL_EVACT0_START               (TCC_EVCTRL_EVACT0_START_Val << TCC_EVCTRL_EVACT0_Pos) /**< (TCC_EVCTRL) Start counter on event Position  */
#define TCC_EVCTRL_EVACT0_INC                 (TCC_EVCTRL_EVACT0_INC_Val << TCC_EVCTRL_EVACT0_Pos) /**< (TCC_EVCTRL) Increment counter on event Position  */
#define TCC_EVCTRL_EVACT0_COUNT               (TCC_EVCTRL_EVACT0_COUNT_Val << TCC_EVCTRL_EVACT0_Pos) /**< (TCC_EVCTRL) Count on active state of asynchronous event Position  */
#define TCC_EVCTRL_EVACT0_STAMP               (TCC_EVCTRL_EVACT0_STAMP_Val << TCC_EVCTRL_EVACT0_Pos) /**< (TCC_EVCTRL) Stamp capture Position  */
#define TCC_EVCTRL_EVACT0_FAULT               (TCC_EVCTRL_EVACT0_FAULT_Val << TCC_EVCTRL_EVACT0_Pos) /**< (TCC_EVCTRL) Non-recoverable fault Position  */
#define TCC_EVCTRL_EVACT1_Pos                 (3U)                                           /**< (TCC_EVCTRL) Timer/counter Input Event1 Action Position */
#define TCC_EVCTRL_EVACT1_Msk                 (0x7U << TCC_EVCTRL_EVACT1_Pos)                /**< (TCC_EVCTRL) Timer/counter Input Event1 Action Mask */
#define TCC_EVCTRL_EVACT1(value)              (TCC_EVCTRL_EVACT1_Msk & ((value) << TCC_EVCTRL_EVACT1_Pos))
#define   TCC_EVCTRL_EVACT1_OFF_Val           (0U)                                           /**< (TCC_EVCTRL) Event action disabled  */
#define   TCC_EVCTRL_EVACT1_RETRIGGER_Val     (1U)                                           /**< (TCC_EVCTRL) Re-trigger counter on event  */
#define   TCC_EVCTRL_EVACT1_DIR_Val           (2U)                                           /**< (TCC_EVCTRL) Direction control  */
#define   TCC_EVCTRL_EVACT1_STOP_Val          (3U)                                           /**< (TCC_EVCTRL) Stop counter on event  */
#define   TCC_EVCTRL_EVACT1_DEC_Val           (4U)                                           /**< (TCC_EVCTRL) Decrement counter on event  */
#define   TCC_EVCTRL_EVACT1_PPW_Val           (5U)                                           /**< (TCC_EVCTRL) Period capture value in CC0 register, pulse width capture value in CC1 register  */
#define   TCC_EVCTRL_EVACT1_PWP_Val           (6U)                                           /**< (TCC_EVCTRL) Period capture value in CC1 register, pulse width capture value in CC0 register  */
#define   TCC_EVCTRL_EVACT1_FAULT_Val         (7U)                                           /**< (TCC_EVCTRL) Non-recoverable fault  */
#define TCC_EVCTRL_EVACT1_OFF                 (TCC_EVCTRL_EVACT1_OFF_Val << TCC_EVCTRL_EVACT1_Pos) /**< (TCC_EVCTRL) Event action disabled Position  */
#define TCC_EVCTRL_EVACT1_RETRIGGER           (TCC_EVCTRL_EVACT1_RETRIGGER_Val << TCC_EVCTRL_EVACT1_Pos) /**< (TCC_EVCTRL) Re-trigger counter on event Position  */
#define TCC_EVCTRL_EVACT1_DIR                 (TCC_EVCTRL_EVACT1_DIR_Val << TCC_EVCTRL_EVACT1_Pos) /**< (TCC_EVCTRL) Direction control Position  */
#define TCC_EVCTRL_EVACT1_STOP                (TCC_EVCTRL_EVACT1_STOP_Val << TCC_EVCTRL_EVACT1_Pos) /**< (TCC_EVCTRL) Stop counter on event Position  */
#define TCC_EVCTRL_EVACT1_DEC                 (TCC_EVCTRL_EVACT1_DEC_Val << TCC_EVCTRL_EVACT1_Pos) /**< (TCC_EVCTRL) Decrement counter on event Position  */
#define TCC_EVCTRL_EVACT1_PPW                 (TCC_EVCTRL_EVACT1_PPW_Val << TCC_EVCTRL_EVACT1_Pos) /**< (TCC_EVCTRL) Period capture value in CC0 register, pulse width capture value in CC1 register Position  */
#define TCC_EVCTRL_EVACT1_PWP                 (TCC_EVCTRL_EVACT1_PWP_Val << TCC_EVCTRL_EVACT1_Pos) /**< (TCC_EVCTRL) Period capture value in CC1 register, pulse width capture value in CC0 register Position  */
#define TCC_EVCTRL_EVACT1_FAULT               (TCC_EVCTRL_EVACT1_FAULT_Val << TCC_EVCTRL_EVACT1_Pos) /**< (TCC_EVCTRL) Non-recoverable fault Position  */
#define TCC_EVCTRL_CNTSEL_Pos                 (6U)                                           /**< (TCC_EVCTRL) Timer/counter Output Event Mode Position */
#define TCC_EVCTRL_CNTSEL_Msk                 (0x3U << TCC_EVCTRL_CNTSEL_Pos)                /**< (TCC_EVCTRL) Timer/counter Output Event Mode Mask */
#define TCC_EVCTRL_CNTSEL(value)              (TCC_EVCTRL_CNTSEL_Msk & ((value) << TCC_EVCTRL_CNTSEL_Pos))
#define   TCC_EVCTRL_CNTSEL_START_Val         (0U)                                           /**< (TCC_EVCTRL) An interrupt/event is generated when a new counter cycle starts  */
#define   TCC_EVCTRL_CNTSEL_END_Val           (1U)                                           /**< (TCC_EVCTRL) An interrupt/event is generated when a counter cycle ends  */
#define   TCC_EVCTRL_CNTSEL_BETWEEN_Val       (2U)                                           /**< (TCC_EVCTRL) An interrupt/event is generated when a counter cycle ends, except for the first and last cycles  */
#define   TCC_EVCTRL_CNTSEL_BOUNDARY_Val      (3U)                                           /**< (TCC_EVCTRL) An interrupt/event is generated when a new counter cycle starts or a counter cycle ends  */
#define TCC_EVCTRL_CNTSEL_START               (TCC_EVCTRL_CNTSEL_START_Val << TCC_EVCTRL_CNTSEL_Pos) /**< (TCC_EVCTRL) An interrupt/event is generated when a new counter cycle starts Position  */
#define TCC_EVCTRL_CNTSEL_END                 (TCC_EVCTRL_CNTSEL_END_Val << TCC_EVCTRL_CNTSEL_Pos) /**< (TCC_EVCTRL) An interrupt/event is generated when a counter cycle ends Position  */
#define TCC_EVCTRL_CNTSEL_BETWEEN             (TCC_EVCTRL_CNTSEL_BETWEEN_Val << TCC_EVCTRL_CNTSEL_Pos) /**< (TCC_EVCTRL) An interrupt/event is generated when a counter cycle ends, except for the first and last cycles Position  */
#define TCC_EVCTRL_CNTSEL_BOUNDARY            (TCC_EVCTRL_CNTSEL_BOUNDARY_Val << TCC_EVCTRL_CNTSEL_Pos) /**< (TCC_EVCTRL) An interrupt/event is generated when a new counter cycle starts or a counter cycle ends Position  */
#define TCC_EVCTRL_OVFEO_Pos                  (8U)                                           /**< (TCC_EVCTRL) Overflow/Underflow Output Event Enable Position */
#define TCC_EVCTRL_OVFEO_Msk                  (0x1U << TCC_EVCTRL_OVFEO_Pos)                 /**< (TCC_EVCTRL) Overflow/Underflow Output Event Enable Mask */
#define TCC_EVCTRL_OVFEO(value)               (TCC_EVCTRL_OVFEO_Msk & ((value) << TCC_EVCTRL_OVFEO_Pos))
#define TCC_EVCTRL_TRGEO_Pos                  (9U)                                           /**< (TCC_EVCTRL) Retrigger Output Event Enable Position */
#define TCC_EVCTRL_TRGEO_Msk                  (0x1U << TCC_EVCTRL_TRGEO_Pos)                 /**< (TCC_EVCTRL) Retrigger Output Event Enable Mask */
#define TCC_EVCTRL_TRGEO(value)               (TCC_EVCTRL_TRGEO_Msk & ((value) << TCC_EVCTRL_TRGEO_Pos))
#define TCC_EVCTRL_CNTEO_Pos                  (10U)                                          /**< (TCC_EVCTRL) Timer/counter Output Event Enable Position */
#define TCC_EVCTRL_CNTEO_Msk                  (0x1U << TCC_EVCTRL_CNTEO_Pos)                 /**< (TCC_EVCTRL) Timer/counter Output Event Enable Mask */
#define TCC_EVCTRL_CNTEO(value)               (TCC_EVCTRL_CNTEO_Msk & ((value) << TCC_EVCTRL_CNTEO_Pos))
#define TCC_EVCTRL_TCINV0_Pos                 (12U)                                          /**< (TCC_EVCTRL) Inverted Event 0 Input Enable Position */
#define TCC_EVCTRL_TCINV0_Msk                 (0x1U << TCC_EVCTRL_TCINV0_Pos)                /**< (TCC_EVCTRL) Inverted Event 0 Input Enable Mask */
#define TCC_EVCTRL_TCINV0(value)              (TCC_EVCTRL_TCINV0_Msk & ((value) << TCC_EVCTRL_TCINV0_Pos))
#define TCC_EVCTRL_TCINV1_Pos                 (13U)                                          /**< (TCC_EVCTRL) Inverted Event 1 Input Enable Position */
#define TCC_EVCTRL_TCINV1_Msk                 (0x1U << TCC_EVCTRL_TCINV1_Pos)                /**< (TCC_EVCTRL) Inverted Event 1 Input Enable Mask */
#define TCC_EVCTRL_TCINV1(value)              (TCC_EVCTRL_TCINV1_Msk & ((value) << TCC_EVCTRL_TCINV1_Pos))
#define TCC_EVCTRL_TCEI0_Pos                  (14U)                                          /**< (TCC_EVCTRL) Timer/counter Event 0 Input Enable Position */
#define TCC_EVCTRL_TCEI0_Msk                  (0x1U << TCC_EVCTRL_TCEI0_Pos)                 /**< (TCC_EVCTRL) Timer/counter Event 0 Input Enable Mask */
#define TCC_EVCTRL_TCEI0(value)               (TCC_EVCTRL_TCEI0_Msk & ((value) << TCC_EVCTRL_TCEI0_Pos))
#define TCC_EVCTRL_TCEI1_Pos                  (15U)                                          /**< (TCC_EVCTRL) Timer/counter Event 1 Input Enable Position */
#define TCC_EVCTRL_TCEI1_Msk                  (0x1U << TCC_EVCTRL_TCEI1_Pos)                 /**< (TCC_EVCTRL) Timer/counter Event 1 Input Enable Mask */
#define TCC_EVCTRL_TCEI1(value)               (TCC_EVCTRL_TCEI1_Msk & ((value) << TCC_EVCTRL_TCEI1_Pos))
#define TCC_EVCTRL_MCEI0_Pos                  (16U)                                          /**< (TCC_EVCTRL) Match or Capture Channel 0 Event Input Enable Position */
#define TCC_EVCTRL_MCEI0_Msk                  (0x1U << TCC_EVCTRL_MCEI0_Pos)                 /**< (TCC_EVCTRL) Match or Capture Channel 0 Event Input Enable Mask */
#define TCC_EVCTRL_MCEI0(value)               (TCC_EVCTRL_MCEI0_Msk & ((value) << TCC_EVCTRL_MCEI0_Pos))
#define TCC_EVCTRL_MCEI1_Pos                  (17U)                                          /**< (TCC_EVCTRL) Match or Capture Channel 1 Event Input Enable Position */
#define TCC_EVCTRL_MCEI1_Msk                  (0x1U << TCC_EVCTRL_MCEI1_Pos)                 /**< (TCC_EVCTRL) Match or Capture Channel 1 Event Input Enable Mask */
#define TCC_EVCTRL_MCEI1(value)               (TCC_EVCTRL_MCEI1_Msk & ((value) << TCC_EVCTRL_MCEI1_Pos))
#define TCC_EVCTRL_MCEI2_Pos                  (18U)                                          /**< (TCC_EVCTRL) Match or Capture Channel 2 Event Input Enable Position */
#define TCC_EVCTRL_MCEI2_Msk                  (0x1U << TCC_EVCTRL_MCEI2_Pos)                 /**< (TCC_EVCTRL) Match or Capture Channel 2 Event Input Enable Mask */
#define TCC_EVCTRL_MCEI2(value)               (TCC_EVCTRL_MCEI2_Msk & ((value) << TCC_EVCTRL_MCEI2_Pos))
#define TCC_EVCTRL_MCEI3_Pos                  (19U)                                          /**< (TCC_EVCTRL) Match or Capture Channel 3 Event Input Enable Position */
#define TCC_EVCTRL_MCEI3_Msk                  (0x1U << TCC_EVCTRL_MCEI3_Pos)                 /**< (TCC_EVCTRL) Match or Capture Channel 3 Event Input Enable Mask */
#define TCC_EVCTRL_MCEI3(value)               (TCC_EVCTRL_MCEI3_Msk & ((value) << TCC_EVCTRL_MCEI3_Pos))
#define TCC_EVCTRL_MCEO0_Pos                  (24U)                                          /**< (TCC_EVCTRL) Match or Capture Channel 0 Event Output Enable Position */
#define TCC_EVCTRL_MCEO0_Msk                  (0x1U << TCC_EVCTRL_MCEO0_Pos)                 /**< (TCC_EVCTRL) Match or Capture Channel 0 Event Output Enable Mask */
#define TCC_EVCTRL_MCEO0(value)               (TCC_EVCTRL_MCEO0_Msk & ((value) << TCC_EVCTRL_MCEO0_Pos))
#define TCC_EVCTRL_MCEO1_Pos                  (25U)                                          /**< (TCC_EVCTRL) Match or Capture Channel 1 Event Output Enable Position */
#define TCC_EVCTRL_MCEO1_Msk                  (0x1U << TCC_EVCTRL_MCEO1_Pos)                 /**< (TCC_EVCTRL) Match or Capture Channel 1 Event Output Enable Mask */
#define TCC_EVCTRL_MCEO1(value)               (TCC_EVCTRL_MCEO1_Msk & ((value) << TCC_EVCTRL_MCEO1_Pos))
#define TCC_EVCTRL_MCEO2_Pos                  (26U)                                          /**< (TCC_EVCTRL) Match or Capture Channel 2 Event Output Enable Position */
#define TCC_EVCTRL_MCEO2_Msk                  (0x1U << TCC_EVCTRL_MCEO2_Pos)                 /**< (TCC_EVCTRL) Match or Capture Channel 2 Event Output Enable Mask */
#define TCC_EVCTRL_MCEO2(value)               (TCC_EVCTRL_MCEO2_Msk & ((value) << TCC_EVCTRL_MCEO2_Pos))
#define TCC_EVCTRL_MCEO3_Pos                  (27U)                                          /**< (TCC_EVCTRL) Match or Capture Channel 3 Event Output Enable Position */
#define TCC_EVCTRL_MCEO3_Msk                  (0x1U << TCC_EVCTRL_MCEO3_Pos)                 /**< (TCC_EVCTRL) Match or Capture Channel 3 Event Output Enable Mask */
#define TCC_EVCTRL_MCEO3(value)               (TCC_EVCTRL_MCEO3_Msk & ((value) << TCC_EVCTRL_MCEO3_Pos))
#define TCC_EVCTRL_Msk                        (0x0F0FF7FFUL)                                 /**< (TCC_EVCTRL) Register Mask  */

/* -------- TCC_INTENCLR : (TCC Offset: 0x24) (R/W 32) Interrupt Enable Clear -------- */
#define TCC_INTENCLR_OVF_Pos                  (0U)                                           /**< (TCC_INTENCLR) Overflow Interrupt Enable Position */
#define TCC_INTENCLR_OVF_Msk                  (0x1U << TCC_INTENCLR_OVF_Pos)                 /**< (TCC_INTENCLR) Overflow Interrupt Enable Mask */
#define TCC_INTENCLR_OVF(value)               (TCC_INTENCLR_OVF_Msk & ((value) << TCC_INTENCLR_OVF_Pos))
#define TCC_INTENCLR_TRG_Pos                  (1U)                                           /**< (TCC_INTENCLR) Retrigger Interrupt Enable Position */
#define TCC_INTENCLR_TRG_Msk                  (0x1U << TCC_INTENCLR_TRG_Pos)                 /**< (TCC_INTENCLR) Retrigger Interrupt Enable Mask */
#define TCC_INTENCLR_TRG(value)               (TCC_INTENCLR_TRG_Msk & ((value) << TCC_INTENCLR_TRG_Pos))
#define TCC_INTENCLR_CNT_Pos                  (2U)                                           /**< (TCC_INTENCLR) Counter Interrupt Enable Position */
#define TCC_INTENCLR_CNT_Msk                  (0x1U << TCC_INTENCLR_CNT_Pos)                 /**< (TCC_INTENCLR) Counter Interrupt Enable Mask */
#define TCC_INTENCLR_CNT(value)               (TCC_INTENCLR_CNT_Msk & ((value) << TCC_INTENCLR_CNT_Pos))
#define TCC_INTENCLR_ERR_Pos                  (3U)                                           /**< (TCC_INTENCLR) Error Interrupt Enable Position */
#define TCC_INTENCLR_ERR_Msk                  (0x1U << TCC_INTENCLR_ERR_Pos)                 /**< (TCC_INTENCLR) Error Interrupt Enable Mask */
#define TCC_INTENCLR_ERR(value)               (TCC_INTENCLR_ERR_Msk & ((value) << TCC_INTENCLR_ERR_Pos))
#define TCC_INTENCLR_UFS_Pos                  (10U)                                          /**< (TCC_INTENCLR) Non-Recoverable Update Fault Interrupt Enable Position */
#define TCC_INTENCLR_UFS_Msk                  (0x1U << TCC_INTENCLR_UFS_Pos)                 /**< (TCC_INTENCLR) Non-Recoverable Update Fault Interrupt Enable Mask */
#define TCC_INTENCLR_UFS(value)               (TCC_INTENCLR_UFS_Msk & ((value) << TCC_INTENCLR_UFS_Pos))
#define TCC_INTENCLR_DFS_Pos                  (11U)                                          /**< (TCC_INTENCLR) Non-Recoverable Debug Fault Interrupt Enable Position */
#define TCC_INTENCLR_DFS_Msk                  (0x1U << TCC_INTENCLR_DFS_Pos)                 /**< (TCC_INTENCLR) Non-Recoverable Debug Fault Interrupt Enable Mask */
#define TCC_INTENCLR_DFS(value)               (TCC_INTENCLR_DFS_Msk & ((value) << TCC_INTENCLR_DFS_Pos))
#define TCC_INTENCLR_FAULTA_Pos               (12U)                                          /**< (TCC_INTENCLR) Recoverable Fault A Interrupt Enable Position */
#define TCC_INTENCLR_FAULTA_Msk               (0x1U << TCC_INTENCLR_FAULTA_Pos)              /**< (TCC_INTENCLR) Recoverable Fault A Interrupt Enable Mask */
#define TCC_INTENCLR_FAULTA(value)            (TCC_INTENCLR_FAULTA_Msk & ((value) << TCC_INTENCLR_FAULTA_Pos))
#define TCC_INTENCLR_FAULTB_Pos               (13U)                                          /**< (TCC_INTENCLR) Recoverable Fault B Interrupt Enable Position */
#define TCC_INTENCLR_FAULTB_Msk               (0x1U << TCC_INTENCLR_FAULTB_Pos)              /**< (TCC_INTENCLR) Recoverable Fault B Interrupt Enable Mask */
#define TCC_INTENCLR_FAULTB(value)            (TCC_INTENCLR_FAULTB_Msk & ((value) << TCC_INTENCLR_FAULTB_Pos))
#define TCC_INTENCLR_FAULT0_Pos               (14U)                                          /**< (TCC_INTENCLR) Non-Recoverable Fault 0 Interrupt Enable Position */
#define TCC_INTENCLR_FAULT0_Msk               (0x1U << TCC_INTENCLR_FAULT0_Pos)              /**< (TCC_INTENCLR) Non-Recoverable Fault 0 Interrupt Enable Mask */
#define TCC_INTENCLR_FAULT0(value)            (TCC_INTENCLR_FAULT0_Msk & ((value) << TCC_INTENCLR_FAULT0_Pos))
#define TCC_INTENCLR_FAULT1_Pos               (15U)                                          /**< (TCC_INTENCLR) Non-Recoverable Fault 1 Interrupt Enable Position */
#define TCC_INTENCLR_FAULT1_Msk               (0x1U << TCC_INTENCLR_FAULT1_Pos)              /**< (TCC_INTENCLR) Non-Recoverable Fault 1 Interrupt Enable Mask */
#define TCC_INTENCLR_FAULT1(value)            (TCC_INTENCLR_FAULT1_Msk & ((value) << TCC_INTENCLR_FAULT1_Pos))
#define TCC_INTENCLR_MC0_Pos                  (16U)                                          /**< (TCC_INTENCLR) Match or Capture Channel 0 Interrupt Enable Position */
#define TCC_INTENCLR_MC0_Msk                  (0x1U << TCC_INTENCLR_MC0_Pos)                 /**< (TCC_INTENCLR) Match or Capture Channel 0 Interrupt Enable Mask */
#define TCC_INTENCLR_MC0(value)               (TCC_INTENCLR_MC0_Msk & ((value) << TCC_INTENCLR_MC0_Pos))
#define TCC_INTENCLR_MC1_Pos                  (17U)                                          /**< (TCC_INTENCLR) Match or Capture Channel 1 Interrupt Enable Position */
#define TCC_INTENCLR_MC1_Msk                  (0x1U << TCC_INTENCLR_MC1_Pos)                 /**< (TCC_INTENCLR) Match or Capture Channel 1 Interrupt Enable Mask */
#define TCC_INTENCLR_MC1(value)               (TCC_INTENCLR_MC1_Msk & ((value) << TCC_INTENCLR_MC1_Pos))
#define TCC_INTENCLR_MC2_Pos                  (18U)                                          /**< (TCC_INTENCLR) Match or Capture Channel 2 Interrupt Enable Position */
#define TCC_INTENCLR_MC2_Msk                  (0x1U << TCC_INTENCLR_MC2_Pos)                 /**< (TCC_INTENCLR) Match or Capture Channel 2 Interrupt Enable Mask */
#define TCC_INTENCLR_MC2(value)               (TCC_INTENCLR_MC2_Msk & ((value) << TCC_INTENCLR_MC2_Pos))
#define TCC_INTENCLR_MC3_Pos                  (19U)                                          /**< (TCC_INTENCLR) Match or Capture Channel 3 Interrupt Enable Position */
#define TCC_INTENCLR_MC3_Msk                  (0x1U << TCC_INTENCLR_MC3_Pos)                 /**< (TCC_INTENCLR) Match or Capture Channel 3 Interrupt Enable Mask */
#define TCC_INTENCLR_MC3(value)               (TCC_INTENCLR_MC3_Msk & ((value) << TCC_INTENCLR_MC3_Pos))
#define TCC_INTENCLR_Msk                      (0x000FFC0FUL)                                 /**< (TCC_INTENCLR) Register Mask  */

/* -------- TCC_INTENSET : (TCC Offset: 0x28) (R/W 32) Interrupt Enable Set -------- */
#define TCC_INTENSET_OVF_Pos                  (0U)                                           /**< (TCC_INTENSET) Overflow Interrupt Enable Position */
#define TCC_INTENSET_OVF_Msk                  (0x1U << TCC_INTENSET_OVF_Pos)                 /**< (TCC_INTENSET) Overflow Interrupt Enable Mask */
#define TCC_INTENSET_OVF(value)               (TCC_INTENSET_OVF_Msk & ((value) << TCC_INTENSET_OVF_Pos))
#define TCC_INTENSET_TRG_Pos                  (1U)                                           /**< (TCC_INTENSET) Retrigger Interrupt Enable Position */
#define TCC_INTENSET_TRG_Msk                  (0x1U << TCC_INTENSET_TRG_Pos)                 /**< (TCC_INTENSET) Retrigger Interrupt Enable Mask */
#define TCC_INTENSET_TRG(value)               (TCC_INTENSET_TRG_Msk & ((value) << TCC_INTENSET_TRG_Pos))
#define TCC_INTENSET_CNT_Pos                  (2U)                                           /**< (TCC_INTENSET) Counter Interrupt Enable Position */
#define TCC_INTENSET_CNT_Msk                  (0x1U << TCC_INTENSET_CNT_Pos)                 /**< (TCC_INTENSET) Counter Interrupt Enable Mask */
#define TCC_INTENSET_CNT(value)               (TCC_INTENSET_CNT_Msk & ((value) << TCC_INTENSET_CNT_Pos))
#define TCC_INTENSET_ERR_Pos                  (3U)                                           /**< (TCC_INTENSET) Error Interrupt Enable Position */
#define TCC_INTENSET_ERR_Msk                  (0x1U << TCC_INTENSET_ERR_Pos)                 /**< (TCC_INTENSET) Error Interrupt Enable Mask */
#define TCC_INTENSET_ERR(value)               (TCC_INTENSET_ERR_Msk & ((value) << TCC_INTENSET_ERR_Pos))
#define TCC_INTENSET_UFS_Pos                  (10U)                                          /**< (TCC_INTENSET) Non-Recoverable Update Fault Interrupt Enable Position */
#define TCC_INTENSET_UFS_Msk                  (0x1U << TCC_INTENSET_UFS_Pos)                 /**< (TCC_INTENSET) Non-Recoverable Update Fault Interrupt Enable Mask */
#define TCC_INTENSET_UFS(value)               (TCC_INTENSET_UFS_Msk & ((value) << TCC_INTENSET_UFS_Pos))
#define TCC_INTENSET_DFS_Pos                  (11U)                                          /**< (TCC_INTENSET) Non-Recoverable Debug Fault Interrupt Enable Position */
#define TCC_INTENSET_DFS_Msk                  (0x1U << TCC_INTENSET_DFS_Pos)                 /**< (TCC_INTENSET) Non-Recoverable Debug Fault Interrupt Enable Mask */
#define TCC_INTENSET_DFS(value)               (TCC_INTENSET_DFS_Msk & ((value) << TCC_INTENSET_DFS_Pos))
#define TCC_INTENSET_FAULTA_Pos               (12U)                                          /**< (TCC_INTENSET) Recoverable Fault A Interrupt Enable Position */
#define TCC_INTENSET_FAULTA_Msk               (0x1U << TCC_INTENSET_FAULTA_Pos)              /**< (TCC_INTENSET) Recoverable Fault A Interrupt Enable Mask */
#define TCC_INTENSET_FAULTA(value)            (TCC_INTENSET_FAULTA_Msk & ((value) << TCC_INTENSET_FAULTA_Pos))
#define TCC_INTENSET_FAULTB_Pos               (13U)                                          /**< (TCC_INTENSET) Recoverable Fault B Interrupt Enable Position */
#define TCC_INTENSET_FAULTB_Msk               (0x1U << TCC_INTENSET_FAULTB_Pos)              /**< (TCC_INTENSET) Recoverable Fault B Interrupt Enable Mask */
#define TCC_INTENSET_FAULTB(value)            (TCC_INTENSET_FAULTB_Msk & ((value) << TCC_INTENSET_FAULTB_Pos))
#define TCC_INTENSET_FAULT0_Pos               (14U)                                          /**< (TCC_INTENSET) Non-Recoverable Fault 0 Interrupt Enable Position */
#define TCC_INTENSET_FAULT0_Msk               (0x1U << TCC_INTENSET_FAULT0_Pos)              /**< (TCC_INTENSET) Non-Recoverable Fault 0 Interrupt Enable Mask */
#define TCC_INTENSET_FAULT0(value)            (TCC_INTENSET_FAULT0_Msk & ((value) << TCC_INTENSET_FAULT0_Pos))
#define TCC_INTENSET_FAULT1_Pos               (15U)                                          /**< (TCC_INTENSET) Non-Recoverable Fault 1 Interrupt Enable Position */
#define TCC_INTENSET_FAULT1_Msk               (0x1U << TCC_INTENSET_FAULT1_Pos)              /**< (TCC_INTENSET) Non-Recoverable Fault 1 Interrupt Enable Mask */
#define TCC_INTENSET_FAULT1(value)            (TCC_INTENSET_FAULT1_Msk & ((value) << TCC_INTENSET_FAULT1_Pos))
#define TCC_INTENSET_MC0_Pos                  (16U)                                          /**< (TCC_INTENSET) Match or Capture Channel 0 Interrupt Enable Position */
#define TCC_INTENSET_MC0_Msk                  (0x1U << TCC_INTENSET_MC0_Pos)                 /**< (TCC_INTENSET) Match or Capture Channel 0 Interrupt Enable Mask */
#define TCC_INTENSET_MC0(value)               (TCC_INTENSET_MC0_Msk & ((value) << TCC_INTENSET_MC0_Pos))
#define TCC_INTENSET_MC1_Pos                  (17U)                                          /**< (TCC_INTENSET) Match or Capture Channel 1 Interrupt Enable Position */
#define TCC_INTENSET_MC1_Msk                  (0x1U << TCC_INTENSET_MC1_Pos)                 /**< (TCC_INTENSET) Match or Capture Channel 1 Interrupt Enable Mask */
#define TCC_INTENSET_MC1(value)               (TCC_INTENSET_MC1_Msk & ((value) << TCC_INTENSET_MC1_Pos))
#define TCC_INTENSET_MC2_Pos                  (18U)                                          /**< (TCC_INTENSET) Match or Capture Channel 2 Interrupt Enable Position */
#define TCC_INTENSET_MC2_Msk                  (0x1U << TCC_INTENSET_MC2_Pos)                 /**< (TCC_INTENSET) Match or Capture Channel 2 Interrupt Enable Mask */
#define TCC_INTENSET_MC2(value)               (TCC_INTENSET_MC2_Msk & ((value) << TCC_INTENSET_MC2_Pos))
#define TCC_INTENSET_MC3_Pos                  (19U)                                          /**< (TCC_INTENSET) Match or Capture Channel 3 Interrupt Enable Position */
#define TCC_INTENSET_MC3_Msk                  (0x1U << TCC_INTENSET_MC3_Pos)                 /**< (TCC_INTENSET) Match or Capture Channel 3 Interrupt Enable Mask */
#define TCC_INTENSET_MC3(value)               (TCC_INTENSET_MC3_Msk & ((value) << TCC_INTENSET_MC3_Pos))
#define TCC_INTENSET_Msk                      (0x000FFC0FUL)                                 /**< (TCC_INTENSET) Register Mask  */

/* -------- TCC_INTFLAG : (TCC Offset: 0x2C) (R/W 32) Interrupt Flag Status and Clear -------- */
#define TCC_INTFLAG_OVF_Pos                   (0U)                                           /**< (TCC_INTFLAG) Overflow Position */
#define TCC_INTFLAG_OVF_Msk                   (0x1U << TCC_INTFLAG_OVF_Pos)                  /**< (TCC_INTFLAG) Overflow Mask */
#define TCC_INTFLAG_OVF(value)                (TCC_INTFLAG_OVF_Msk & ((value) << TCC_INTFLAG_OVF_Pos))
#define TCC_INTFLAG_TRG_Pos                   (1U)                                           /**< (TCC_INTFLAG) Retrigger Position */
#define TCC_INTFLAG_TRG_Msk                   (0x1U << TCC_INTFLAG_TRG_Pos)                  /**< (TCC_INTFLAG) Retrigger Mask */
#define TCC_INTFLAG_TRG(value)                (TCC_INTFLAG_TRG_Msk & ((value) << TCC_INTFLAG_TRG_Pos))
#define TCC_INTFLAG_CNT_Pos                   (2U)                                           /**< (TCC_INTFLAG) Counter Position */
#define TCC_INTFLAG_CNT_Msk                   (0x1U << TCC_INTFLAG_CNT_Pos)                  /**< (TCC_INTFLAG) Counter Mask */
#define TCC_INTFLAG_CNT(value)                (TCC_INTFLAG_CNT_Msk & ((value) << TCC_INTFLAG_CNT_Pos))
#define TCC_INTFLAG_ERR_Pos                   (3U)                                           /**< (TCC_INTFLAG) Error Position */
#define TCC_INTFLAG_ERR_Msk                   (0x1U << TCC_INTFLAG_ERR_Pos)                  /**< (TCC_INTFLAG) Error Mask */
#define TCC_INTFLAG_ERR(value)                (TCC_INTFLAG_ERR_Msk & ((value) << TCC_INTFLAG_ERR_Pos))
#define TCC_INTFLAG_UFS_Pos                   (10U)                                          /**< (TCC_INTFLAG) Non-Recoverable Update Fault Position */
#define TCC_INTFLAG_UFS_Msk                   (0x1U << TCC_INTFLAG_UFS_Pos)                  /**< (TCC_INTFLAG) Non-Recoverable Update Fault Mask */
#define TCC_INTFLAG_UFS(value)                (TCC_INTFLAG_UFS_Msk & ((value) << TCC_INTFLAG_UFS_Pos))
#define TCC_INTFLAG_DFS_Pos                   (11U)                                          /**< (TCC_INTFLAG) Non-Recoverable Debug Fault Position */
#define TCC_INTFLAG_DFS_Msk                   (0x1U << TCC_INTFLAG_DFS_Pos)                  /**< (TCC_INTFLAG) Non-Recoverable Debug Fault Mask */
#define TCC_INTFLAG_DFS(value)                (TCC_INTFLAG_DFS_Msk & ((value) << TCC_INTFLAG_DFS_Pos))
#define TCC_INTFLAG_FAULTA_Pos                (12U)                                          /**< (TCC_INTFLAG) Recoverable Fault A Position */
#define TCC_INTFLAG_FAULTA_Msk                (0x1U << TCC_INTFLAG_FAULTA_Pos)               /**< (TCC_INTFLAG) Recoverable Fault A Mask */
#define TCC_INTFLAG_FAULTA(value)             (TCC_INTFLAG_FAULTA_Msk & ((value) << TCC_INTFLAG_FAULTA_Pos))
#define TCC_INTFLAG_FAULTB_Pos                (13U)                                          /**< (TCC_INTFLAG) Recoverable Fault B Position */
#define TCC_INTFLAG_FAULTB_Msk                (0x1U << TCC_INTFLAG_FAULTB_Pos)               /**< (TCC_INTFLAG) Recoverable Fault B Mask */
#define TCC_INTFLAG_FAULTB(value)             (TCC_INTFLAG_FAULTB_Msk & ((value) << TCC_INTFLAG_FAULTB_Pos))
#define TCC_INTFLAG_FAULT0_Pos                (14U)                                          /**< (TCC_INTFLAG) Non-Recoverable Fault 0 Position */
#define TCC_INTFLAG_FAULT0_Msk                (0x1U << TCC_INTFLAG_FAULT0_Pos)               /**< (TCC_INTFLAG) Non-Recoverable Fault 0 Mask */
#define TCC_INTFLAG_FAULT0(value)             (TCC_INTFLAG_FAULT0_Msk & ((value) << TCC_INTFLAG_FAULT0_Pos))
#define TCC_INTFLAG_FAULT1_Pos                (15U)                                          /**< (TCC_INTFLAG) Non-Recoverable Fault 1 Position */
#define TCC_INTFLAG_FAULT1_Msk                (0x1U << TCC_INTFLAG_FAULT1_Pos)               /**< (TCC_INTFLAG) Non-Recoverable Fault 1 Mask */
#define TCC_INTFLAG_FAULT1(value)             (TCC_INTFLAG_FAULT1_Msk & ((value) << TCC_INTFLAG_FAULT1_Pos))
#define TCC_INTFLAG_MC0_Pos                   (16U)                                          /**< (TCC_INTFLAG) Match or Capture 0 Position */
#define TCC_INTFLAG_MC0_Msk                   (0x1U << TCC_INTFLAG_MC0_Pos)                  /**< (TCC_INTFLAG) Match or Capture 0 Mask */
#define TCC_INTFLAG_MC0(value)                (TCC_INTFLAG_MC0_Msk & ((value) << TCC_INTFLAG_MC0_Pos))
#define TCC_INTFLAG_MC1_Pos                   (17U)                                          /**< (TCC_INTFLAG) Match or Capture 1 Position */
#define TCC_INTFLAG_MC1_Msk                   (0x1U << TCC_INTFLAG_MC1_Pos)                  /**< (TCC_INTFLAG) Match or Capture 1 Mask */
#define TCC_INTFLAG_MC1(value)                (TCC_INTFLAG_MC1_Msk & ((value) << TCC_INTFLAG_MC1_Pos))
#define TCC_INTFLAG_MC2_Pos                   (18U)                                          /**< (TCC_INTFLAG) Match or Capture 2 Position */
#define TCC_INTFLAG_MC2_Msk                   (0x1U << TCC_INTFLAG_MC2_Pos)                  /**< (TCC_INTFLAG) Match or Capture 2 Mask */
#define TCC_INTFLAG_MC2(value)                (TCC_INTFLAG_MC2_Msk & ((value) << TCC_INTFLAG_MC2_Pos))
#define TCC_INTFLAG_MC3_Pos                   (19U)                                          /**< (TCC_INTFLAG) Match or Capture 3 Position */
#define TCC_INTFLAG_MC3_Msk                   (0x1U << TCC_INTFLAG_MC3_Pos)                  /**< (TCC_INTFLAG) Match or Capture 3 Mask */
#define TCC_INTFLAG_MC3(value)                (TCC_INTFLAG_MC3_Msk & ((value) << TCC_INTFLAG_MC3_Pos))
#define TCC_INTFLAG_Msk                       (0x000FFC0FUL)                                 /**< (TCC_INTFLAG) Register Mask  */

/* -------- TCC_STATUS : (TCC Offset: 0x30) (R/W 32) Status -------- */
#define TCC_STATUS_STOP_Pos                   (0U)                                           /**< (TCC_STATUS) Stop Position */
#define TCC_STATUS_STOP_Msk                   (0x1U << TCC_STATUS_STOP_Pos)                  /**< (TCC_STATUS) Stop Mask */
#define TCC_STATUS_STOP(value)                (TCC_STATUS_STOP_Msk & ((value) << TCC_STATUS_STOP_Pos))
#define TCC_STATUS_IDX_Pos                    (1U)                                           /**< (TCC_STATUS) Ramp Position */
#define TCC_STATUS_IDX_Msk                    (0x1U << TCC_STATUS_IDX_Pos)                   /**< (TCC_STATUS) Ramp Mask */
#define TCC_STATUS_IDX(value)                 (TCC_STATUS_IDX_Msk & ((value) << TCC_STATUS_IDX_Pos))
#define TCC_STATUS_UFS_Pos                    (2U)                                           /**< (TCC_STATUS) Non-recoverable Update Fault State Position */
#define TCC_STATUS_UFS_Msk                    (0x1U << TCC_STATUS_UFS_Pos)                   /**< (TCC_STATUS) Non-recoverable Update Fault State Mask */
#define TCC_STATUS_UFS(value)                 (TCC_STATUS_UFS_Msk & ((value) << TCC_STATUS_UFS_Pos))
#define TCC_STATUS_DFS_Pos                    (3U)                                           /**< (TCC_STATUS) Non-Recoverable Debug Fault State Position */
#define TCC_STATUS_DFS_Msk                    (0x1U << TCC_STATUS_DFS_Pos)                   /**< (TCC_STATUS) Non-Recoverable Debug Fault State Mask */
#define TCC_STATUS_DFS(value)                 (TCC_STATUS_DFS_Msk & ((value) << TCC_STATUS_DFS_Pos))
#define TCC_STATUS_SLAVE_Pos                  (4U)                                           /**< (TCC_STATUS) Slave Position */
#define TCC_STATUS_SLAVE_Msk                  (0x1U << TCC_STATUS_SLAVE_Pos)                 /**< (TCC_STATUS) Slave Mask */
#define TCC_STATUS_SLAVE(value)               (TCC_STATUS_SLAVE_Msk & ((value) << TCC_STATUS_SLAVE_Pos))
#define TCC_STATUS_PATTBUFV_Pos               (5U)                                           /**< (TCC_STATUS) Pattern Buffer Valid Position */
#define TCC_STATUS_PATTBUFV_Msk               (0x1U << TCC_STATUS_PATTBUFV_Pos)              /**< (TCC_STATUS) Pattern Buffer Valid Mask */
#define TCC_STATUS_PATTBUFV(value)            (TCC_STATUS_PATTBUFV_Msk & ((value) << TCC_STATUS_PATTBUFV_Pos))
#define TCC_STATUS_PERBUFV_Pos                (7U)                                           /**< (TCC_STATUS) Period Buffer Valid Position */
#define TCC_STATUS_PERBUFV_Msk                (0x1U << TCC_STATUS_PERBUFV_Pos)               /**< (TCC_STATUS) Period Buffer Valid Mask */
#define TCC_STATUS_PERBUFV(value)             (TCC_STATUS_PERBUFV_Msk & ((value) << TCC_STATUS_PERBUFV_Pos))
#define TCC_STATUS_FAULTAIN_Pos               (8U)                                           /**< (TCC_STATUS) Recoverable Fault A Input Position */
#define TCC_STATUS_FAULTAIN_Msk               (0x1U << TCC_STATUS_FAULTAIN_Pos)              /**< (TCC_STATUS) Recoverable Fault A Input Mask */
#define TCC_STATUS_FAULTAIN(value)            (TCC_STATUS_FAULTAIN_Msk & ((value) << TCC_STATUS_FAULTAIN_Pos))
#define TCC_STATUS_FAULTBIN_Pos               (9U)                                           /**< (TCC_STATUS) Recoverable Fault B Input Position */
#define TCC_STATUS_FAULTBIN_Msk               (0x1U << TCC_STATUS_FAULTBIN_Pos)              /**< (TCC_STATUS) Recoverable Fault B Input Mask */
#define TCC_STATUS_FAULTBIN(value)            (TCC_STATUS_FAULTBIN_Msk & ((value) << TCC_STATUS_FAULTBIN_Pos))
#define TCC_STATUS_FAULT0IN_Pos               (10U)                                          /**< (TCC_STATUS) Non-Recoverable Fault0 Input Position */
#define TCC_STATUS_FAULT0IN_Msk               (0x1U << TCC_STATUS_FAULT0IN_Pos)              /**< (TCC_STATUS) Non-Recoverable Fault0 Input Mask */
#define TCC_STATUS_FAULT0IN(value)            (TCC_STATUS_FAULT0IN_Msk & ((value) << TCC_STATUS_FAULT0IN_Pos))
#define TCC_STATUS_FAULT1IN_Pos               (11U)                                          /**< (TCC_STATUS) Non-Recoverable Fault1 Input Position */
#define TCC_STATUS_FAULT1IN_Msk               (0x1U << TCC_STATUS_FAULT1IN_Pos)              /**< (TCC_STATUS) Non-Recoverable Fault1 Input Mask */
#define TCC_STATUS_FAULT1IN(value)            (TCC_STATUS_FAULT1IN_Msk & ((value) << TCC_STATUS_FAULT1IN_Pos))
#define TCC_STATUS_FAULTA_Pos                 (12U)                                          /**< (TCC_STATUS) Recoverable Fault A State Position */
#define TCC_STATUS_FAULTA_Msk                 (0x1U << TCC_STATUS_FAULTA_Pos)                /**< (TCC_STATUS) Recoverable Fault A State Mask */
#define TCC_STATUS_FAULTA(value)              (TCC_STATUS_FAULTA_Msk & ((value) << TCC_STATUS_FAULTA_Pos))
#define TCC_STATUS_FAULTB_Pos                 (13U)                                          /**< (TCC_STATUS) Recoverable Fault B State Position */
#define TCC_STATUS_FAULTB_Msk                 (0x1U << TCC_STATUS_FAULTB_Pos)                /**< (TCC_STATUS) Recoverable Fault B State Mask */
#define TCC_STATUS_FAULTB(value)              (TCC_STATUS_FAULTB_Msk & ((value) << TCC_STATUS_FAULTB_Pos))
#define TCC_STATUS_FAULT0_Pos                 (14U)                                          /**< (TCC_STATUS) Non-Recoverable Fault 0 State Position */
#define TCC_STATUS_FAULT0_Msk                 (0x1U << TCC_STATUS_FAULT0_Pos)                /**< (TCC_STATUS) Non-Recoverable Fault 0 State Mask */
#define TCC_STATUS_FAULT0(value)              (TCC_STATUS_FAULT0_Msk & ((value) << TCC_STATUS_FAULT0_Pos))
#define TCC_STATUS_FAULT1_Pos                 (15U)                                          /**< (TCC_STATUS) Non-Recoverable Fault 1 State Position */
#define TCC_STATUS_FAULT1_Msk                 (0x1U << TCC_STATUS_FAULT1_Pos)                /**< (TCC_STATUS) Non-Recoverable Fault 1 State Mask */
#define TCC_STATUS_FAULT1(value)              (TCC_STATUS_FAULT1_Msk & ((value) << TCC_STATUS_FAULT1_Pos))
#define TCC_STATUS_CCBUFV0_Pos                (16U)                                          /**< (TCC_STATUS) Compare Channel 0 Buffer Valid Position */
#define TCC_STATUS_CCBUFV0_Msk                (0x1U << TCC_STATUS_CCBUFV0_Pos)               /**< (TCC_STATUS) Compare Channel 0 Buffer Valid Mask */
#define TCC_STATUS_CCBUFV0(value)             (TCC_STATUS_CCBUFV0_Msk & ((value) << TCC_STATUS_CCBUFV0_Pos))
#define TCC_STATUS_CCBUFV1_Pos                (17U)                                          /**< (TCC_STATUS) Compare Channel 1 Buffer Valid Position */
#define TCC_STATUS_CCBUFV1_Msk                (0x1U << TCC_STATUS_CCBUFV1_Pos)               /**< (TCC_STATUS) Compare Channel 1 Buffer Valid Mask */
#define TCC_STATUS_CCBUFV1(value)             (TCC_STATUS_CCBUFV1_Msk & ((value) << TCC_STATUS_CCBUFV1_Pos))
#define TCC_STATUS_CCBUFV2_Pos                (18U)                                          /**< (TCC_STATUS) Compare Channel 2 Buffer Valid Position */
#define TCC_STATUS_CCBUFV2_Msk                (0x1U << TCC_STATUS_CCBUFV2_Pos)               /**< (TCC_STATUS) Compare Channel 2 Buffer Valid Mask */
#define TCC_STATUS_CCBUFV2(value)             (TCC_STATUS_CCBUFV2_Msk & ((value) << TCC_STATUS_CCBUFV2_Pos))
#define TCC_STATUS_CCBUFV3_Pos                (19U)                                          /**< (TCC_STATUS) Compare Channel 3 Buffer Valid Position */
#define TCC_STATUS_CCBUFV3_Msk                (0x1U << TCC_STATUS_CCBUFV3_Pos)               /**< (TCC_STATUS) Compare Channel 3 Buffer Valid Mask */
#define TCC_STATUS_CCBUFV3(value)             (TCC_STATUS_CCBUFV3_Msk & ((value) << TCC_STATUS_CCBUFV3_Pos))
#define TCC_STATUS_CMP0_Pos                   (24U)                                          /**< (TCC_STATUS) Compare Channel 0 Value Position */
#define TCC_STATUS_CMP0_Msk                   (0x1U << TCC_STATUS_CMP0_Pos)                  /**< (TCC_STATUS) Compare Channel 0 Value Mask */
#define TCC_STATUS_CMP0(value)                (TCC_STATUS_CMP0_Msk & ((value) << TCC_STATUS_CMP0_Pos))
#define TCC_STATUS_CMP1_Pos                   (25U)                                          /**< (TCC_STATUS) Compare Channel 1 Value Position */
#define TCC_STATUS_CMP1_Msk                   (0x1U << TCC_STATUS_CMP1_Pos)                  /**< (TCC_STATUS) Compare Channel 1 Value Mask */
#define TCC_STATUS_CMP1(value)                (TCC_STATUS_CMP1_Msk & ((value) << TCC_STATUS_CMP1_Pos))
#define TCC_STATUS_CMP2_Pos                   (26U)                                          /**< (TCC_STATUS) Compare Channel 2 Value Position */
#define TCC_STATUS_CMP2_Msk                   (0x1U << TCC_STATUS_CMP2_Pos)                  /**< (TCC_STATUS) Compare Channel 2 Value Mask */
#define TCC_STATUS_CMP2(value)                (TCC_STATUS_CMP2_Msk & ((value) << TCC_STATUS_CMP2_Pos))
#define TCC_STATUS_CMP3_Pos                   (27U)                                          /**< (TCC_STATUS) Compare Channel 3 Value Position */
#define TCC_STATUS_CMP3_Msk                   (0x1U << TCC_STATUS_CMP3_Pos)                  /**< (TCC_STATUS) Compare Channel 3 Value Mask */
#define TCC_STATUS_CMP3(value)                (TCC_STATUS_CMP3_Msk & ((value) << TCC_STATUS_CMP3_Pos))
#define TCC_STATUS_Msk                        (0x0F0FFFBFUL)                                 /**< (TCC_STATUS) Register Mask  */

/* -------- TCC_COUNT : (TCC Offset: 0x34) (R/W 32) Count -------- */
#define TCC_COUNT_COUNT_Pos                   (6U)                                           /**< (TCC_COUNT) Counter Value Position */
#define TCC_COUNT_COUNT_Msk                   (0x3FFFFU << TCC_COUNT_COUNT_Pos)              /**< (TCC_COUNT) Counter Value Mask */
#define TCC_COUNT_COUNT(value)                (TCC_COUNT_COUNT_Msk & ((value) << TCC_COUNT_COUNT_Pos))
#define TCC_COUNT_Msk                         (0x00FFFFFFUL)                                 /**< (TCC_COUNT) Register Mask  */

/* -------- TCC_PATT : (TCC Offset: 0x38) (R/W 16) Pattern -------- */
#define TCC_PATT_PGE0_Pos                     (0U)                                           /**< (TCC_PATT) Pattern Generator 0 Output Enable Position */
#define TCC_PATT_PGE0_Msk                     (0x1U << TCC_PATT_PGE0_Pos)                    /**< (TCC_PATT) Pattern Generator 0 Output Enable Mask */
#define TCC_PATT_PGE0(value)                  (TCC_PATT_PGE0_Msk & ((value) << TCC_PATT_PGE0_Pos))
#define TCC_PATT_PGE1_Pos                     (1U)                                           /**< (TCC_PATT) Pattern Generator 1 Output Enable Position */
#define TCC_PATT_PGE1_Msk                     (0x1U << TCC_PATT_PGE1_Pos)                    /**< (TCC_PATT) Pattern Generator 1 Output Enable Mask */
#define TCC_PATT_PGE1(value)                  (TCC_PATT_PGE1_Msk & ((value) << TCC_PATT_PGE1_Pos))
#define TCC_PATT_PGE2_Pos                     (2U)                                           /**< (TCC_PATT) Pattern Generator 2 Output Enable Position */
#define TCC_PATT_PGE2_Msk                     (0x1U << TCC_PATT_PGE2_Pos)                    /**< (TCC_PATT) Pattern Generator 2 Output Enable Mask */
#define TCC_PATT_PGE2(value)                  (TCC_PATT_PGE2_Msk & ((value) << TCC_PATT_PGE2_Pos))
#define TCC_PATT_PGE3_Pos                     (3U)                                           /**< (TCC_PATT) Pattern Generator 3 Output Enable Position */
#define TCC_PATT_PGE3_Msk                     (0x1U << TCC_PATT_PGE3_Pos)                    /**< (TCC_PATT) Pattern Generator 3 Output Enable Mask */
#define TCC_PATT_PGE3(value)                  (TCC_PATT_PGE3_Msk & ((value) << TCC_PATT_PGE3_Pos))
#define TCC_PATT_PGE4_Pos                     (4U)                                           /**< (TCC_PATT) Pattern Generator 4 Output Enable Position */
#define TCC_PATT_PGE4_Msk                     (0x1U << TCC_PATT_PGE4_Pos)                    /**< (TCC_PATT) Pattern Generator 4 Output Enable Mask */
#define TCC_PATT_PGE4(value)                  (TCC_PATT_PGE4_Msk & ((value) << TCC_PATT_PGE4_Pos))
#define TCC_PATT_PGE5_Pos                     (5U)                                           /**< (TCC_PATT) Pattern Generator 5 Output Enable Position */
#define TCC_PATT_PGE5_Msk                     (0x1U << TCC_PATT_PGE5_Pos)                    /**< (TCC_PATT) Pattern Generator 5 Output Enable Mask */
#define TCC_PATT_PGE5(value)                  (TCC_PATT_PGE5_Msk & ((value) << TCC_PATT_PGE5_Pos))
#define TCC_PATT_PGE6_Pos                     (6U)                                           /**< (TCC_PATT) Pattern Generator 6 Output Enable Position */
#define TCC_PATT_PGE6_Msk                     (0x1U << TCC_PATT_PGE6_Pos)                    /**< (TCC_PATT) Pattern Generator 6 Output Enable Mask */
#define TCC_PATT_PGE6(value)                  (TCC_PATT_PGE6_Msk & ((value) << TCC_PATT_PGE6_Pos))
#define TCC_PATT_PGE7_Pos                     (7U)                                           /**< (TCC_PATT) Pattern Generator 7 Output Enable Position */
#define TCC_PATT_PGE7_Msk                     (0x1U << TCC_PATT_PGE7_Pos)                    /**< (TCC_PATT) Pattern Generator 7 Output Enable Mask */
#define TCC_PATT_PGE7(value)                  (TCC_PATT_PGE7_Msk & ((value) << TCC_PATT_PGE7_Pos))
#define TCC_PATT_PGV0_Pos                     (8U)                                           /**< (TCC_PATT) Pattern Generator 0 Output Value Position */
#define TCC_PATT_PGV0_Msk                     (0x1U << TCC_PATT_PGV0_Pos)                    /**< (TCC_PATT) Pattern Generator 0 Output Value Mask */
#define TCC_PATT_PGV0(value)                  (TCC_PATT_PGV0_Msk & ((value) << TCC_PATT_PGV0_Pos))
#define TCC_PATT_PGV1_Pos                     (9U)                                           /**< (TCC_PATT) Pattern Generator 1 Output Value Position */
#define TCC_PATT_PGV1_Msk                     (0x1U << TCC_PATT_PGV1_Pos)                    /**< (TCC_PATT) Pattern Generator 1 Output Value Mask */
#define TCC_PATT_PGV1(value)                  (TCC_PATT_PGV1_Msk & ((value) << TCC_PATT_PGV1_Pos))
#define TCC_PATT_PGV2_Pos                     (10U)                                          /**< (TCC_PATT) Pattern Generator 2 Output Value Position */
#define TCC_PATT_PGV2_Msk                     (0x1U << TCC_PATT_PGV2_Pos)                    /**< (TCC_PATT) Pattern Generator 2 Output Value Mask */
#define TCC_PATT_PGV2(value)                  (TCC_PATT_PGV2_Msk & ((value) << TCC_PATT_PGV2_Pos))
#define TCC_PATT_PGV3_Pos                     (11U)                                          /**< (TCC_PATT) Pattern Generator 3 Output Value Position */
#define TCC_PATT_PGV3_Msk                     (0x1U << TCC_PATT_PGV3_Pos)                    /**< (TCC_PATT) Pattern Generator 3 Output Value Mask */
#define TCC_PATT_PGV3(value)                  (TCC_PATT_PGV3_Msk & ((value) << TCC_PATT_PGV3_Pos))
#define TCC_PATT_PGV4_Pos                     (12U)                                          /**< (TCC_PATT) Pattern Generator 4 Output Value Position */
#define TCC_PATT_PGV4_Msk                     (0x1U << TCC_PATT_PGV4_Pos)                    /**< (TCC_PATT) Pattern Generator 4 Output Value Mask */
#define TCC_PATT_PGV4(value)                  (TCC_PATT_PGV4_Msk & ((value) << TCC_PATT_PGV4_Pos))
#define TCC_PATT_PGV5_Pos                     (13U)                                          /**< (TCC_PATT) Pattern Generator 5 Output Value Position */
#define TCC_PATT_PGV5_Msk                     (0x1U << TCC_PATT_PGV5_Pos)                    /**< (TCC_PATT) Pattern Generator 5 Output Value Mask */
#define TCC_PATT_PGV5(value)                  (TCC_PATT_PGV5_Msk & ((value) << TCC_PATT_PGV5_Pos))
#define TCC_PATT_PGV6_Pos                     (14U)                                          /**< (TCC_PATT) Pattern Generator 6 Output Value Position */
#define TCC_PATT_PGV6_Msk                     (0x1U << TCC_PATT_PGV6_Pos)                    /**< (TCC_PATT) Pattern Generator 6 Output Value Mask */
#define TCC_PATT_PGV6(value)                  (TCC_PATT_PGV6_Msk & ((value) << TCC_PATT_PGV6_Pos))
#define TCC_PATT_PGV7_Pos                     (15U)                                          /**< (TCC_PATT) Pattern Generator 7 Output Value Position */
#define TCC_PATT_PGV7_Msk                     (0x1U << TCC_PATT_PGV7_Pos)                    /**< (TCC_PATT) Pattern Generator 7 Output Value Mask */
#define TCC_PATT_PGV7(value)                  (TCC_PATT_PGV7_Msk & ((value) << TCC_PATT_PGV7_Pos))
#define TCC_PATT_Msk                          (0x0000FFFFUL)                                 /**< (TCC_PATT) Register Mask  */

/* -------- TCC_WAVE : (TCC Offset: 0x3C) (R/W 32) Waveform Control -------- */
#define TCC_WAVE_WAVEGEN_Pos                  (0U)                                           /**< (TCC_WAVE) Waveform Generation Position */
#define TCC_WAVE_WAVEGEN_Msk                  (0x7U << TCC_WAVE_WAVEGEN_Pos)                 /**< (TCC_WAVE) Waveform Generation Mask */
#define TCC_WAVE_WAVEGEN(value)               (TCC_WAVE_WAVEGEN_Msk & ((value) << TCC_WAVE_WAVEGEN_Pos))
#define   TCC_WAVE_WAVEGEN_NFRQ_Val           (0U)                                           /**< (TCC_WAVE) Normal frequency  */
#define   TCC_WAVE_WAVEGEN_MFRQ_Val           (1U)                                           /**< (TCC_WAVE) Match frequency  */
#define   TCC_WAVE_WAVEGEN_NPWM_Val           (2U)                                           /**< (TCC_WAVE) Normal PWM  */
#define   TCC_WAVE_WAVEGEN_DSCRITICAL_Val     (4U)                                           /**< (TCC_WAVE) Dual-slope critical  */
#define   TCC_WAVE_WAVEGEN_DSBOTTOM_Val       (5U)                                           /**< (TCC_WAVE) Dual-slope with interrupt/event condition when COUNT reaches ZERO  */
#define   TCC_WAVE_WAVEGEN_DSBOTH_Val         (6U)                                           /**< (TCC_WAVE) Dual-slope with interrupt/event condition when COUNT reaches ZERO or TOP  */
#define   TCC_WAVE_WAVEGEN_DSTOP_Val          (7U)                                           /**< (TCC_WAVE) Dual-slope with interrupt/event condition when COUNT reaches TOP  */
#define TCC_WAVE_WAVEGEN_NFRQ                 (TCC_WAVE_WAVEGEN_NFRQ_Val << TCC_WAVE_WAVEGEN_Pos) /**< (TCC_WAVE) Normal frequency Position  */
#define TCC_WAVE_WAVEGEN_MFRQ                 (TCC_WAVE_WAVEGEN_MFRQ_Val << TCC_WAVE_WAVEGEN_Pos) /**< (TCC_WAVE) Match frequency Position  */
#define TCC_WAVE_WAVEGEN_NPWM                 (TCC_WAVE_WAVEGEN_NPWM_Val << TCC_WAVE_WAVEGEN_Pos) /**< (TCC_WAVE) Normal PWM Position  */
#define TCC_WAVE_WAVEGEN_DSCRITICAL           (TCC_WAVE_WAVEGEN_DSCRITICAL_Val << TCC_WAVE_WAVEGEN_Pos) /**< (TCC_WAVE) Dual-slope critical Position  */
#define TCC_WAVE_WAVEGEN_DSBOTTOM             (TCC_WAVE_WAVEGEN_DSBOTTOM_Val << TCC_WAVE_WAVEGEN_Pos) /**< (TCC_WAVE) Dual-slope with interrupt/event condition when COUNT reaches ZERO Position  */
#define TCC_WAVE_WAVEGEN_DSBOTH               (TCC_WAVE_WAVEGEN_DSBOTH_Val << TCC_WAVE_WAVEGEN_Pos) /**< (TCC_WAVE) Dual-slope with interrupt/event condition when COUNT reaches ZERO or TOP Position  */
#define TCC_WAVE_WAVEGEN_DSTOP                (TCC_WAVE_WAVEGEN_DSTOP_Val << TCC_WAVE_WAVEGEN_Pos) /**< (TCC_WAVE) Dual-slope with interrupt/event condition when COUNT reaches TOP Position  */
#define TCC_WAVE_RAMP_Pos                     (4U)                                           /**< (TCC_WAVE) Ramp Mode Position */
#define TCC_WAVE_RAMP_Msk                     (0x3U << TCC_WAVE_RAMP_Pos)                    /**< (TCC_WAVE) Ramp Mode Mask */
#define TCC_WAVE_RAMP(value)                  (TCC_WAVE_RAMP_Msk & ((value) << TCC_WAVE_RAMP_Pos))
#define   TCC_WAVE_RAMP_RAMP1_Val             (0U)                                           /**< (TCC_WAVE) RAMP1 operation  */
#define   TCC_WAVE_RAMP_RAMP2A_Val            (1U)                                           /**< (TCC_WAVE) Alternative RAMP2 operation  */
#define   TCC_WAVE_RAMP_RAMP2_Val             (2U)                                           /**< (TCC_WAVE) RAMP2 operation  */
#define   TCC_WAVE_RAMP_RAMP2C_Val            (3U)                                           /**< (TCC_WAVE) Critical RAMP2 operation  */
#define TCC_WAVE_RAMP_RAMP1                   (TCC_WAVE_RAMP_RAMP1_Val << TCC_WAVE_RAMP_Pos) /**< (TCC_WAVE) RAMP1 operation Position  */
#define TCC_WAVE_RAMP_RAMP2A                  (TCC_WAVE_RAMP_RAMP2A_Val << TCC_WAVE_RAMP_Pos) /**< (TCC_WAVE) Alternative RAMP2 operation Position  */
#define TCC_WAVE_RAMP_RAMP2                   (TCC_WAVE_RAMP_RAMP2_Val << TCC_WAVE_RAMP_Pos) /**< (TCC_WAVE) RAMP2 operation Position  */
#define TCC_WAVE_RAMP_RAMP2C                  (TCC_WAVE_RAMP_RAMP2C_Val << TCC_WAVE_RAMP_Pos) /**< (TCC_WAVE) Critical RAMP2 operation Position  */
#define TCC_WAVE_CIPEREN_Pos                  (7U)                                           /**< (TCC_WAVE) Circular period Enable Position */
#define TCC_WAVE_CIPEREN_Msk                  (0x1U << TCC_WAVE_CIPEREN_Pos)                 /**< (TCC_WAVE) Circular period Enable Mask */
#define TCC_WAVE_CIPEREN(value)               (TCC_WAVE_CIPEREN_Msk & ((value) << TCC_WAVE_CIPEREN_Pos))
#define TCC_WAVE_CICCEN0_Pos                  (8U)                                           /**< (TCC_WAVE) Circular Channel 0 Enable Position */
#define TCC_WAVE_CICCEN0_Msk                  (0x1U << TCC_WAVE_CICCEN0_Pos)                 /**< (TCC_WAVE) Circular Channel 0 Enable Mask */
#define TCC_WAVE_CICCEN0(value)               (TCC_WAVE_CICCEN0_Msk & ((value) << TCC_WAVE_CICCEN0_Pos))
#define TCC_WAVE_CICCEN1_Pos                  (9U)                                           /**< (TCC_WAVE) Circular Channel 1 Enable Position */
#define TCC_WAVE_CICCEN1_Msk                  (0x1U << TCC_WAVE_CICCEN1_Pos)                 /**< (TCC_WAVE) Circular Channel 1 Enable Mask */
#define TCC_WAVE_CICCEN1(value)               (TCC_WAVE_CICCEN1_Msk & ((value) << TCC_WAVE_CICCEN1_Pos))
#define TCC_WAVE_CICCEN2_Pos                  (10U)                                          /**< (TCC_WAVE) Circular Channel 2 Enable Position */
#define TCC_WAVE_CICCEN2_Msk                  (0x1U << TCC_WAVE_CICCEN2_Pos)                 /**< (TCC_WAVE) Circular Channel 2 Enable Mask */
#define TCC_WAVE_CICCEN2(value)               (TCC_WAVE_CICCEN2_Msk & ((value) << TCC_WAVE_CICCEN2_Pos))
#define TCC_WAVE_CICCEN3_Pos                  (11U)                                          /**< (TCC_WAVE) Circular Channel 3 Enable Position */
#define TCC_WAVE_CICCEN3_Msk                  (0x1U << TCC_WAVE_CICCEN3_Pos)                 /**< (TCC_WAVE) Circular Channel 3 Enable Mask */
#define TCC_WAVE_CICCEN3(value)               (TCC_WAVE_CICCEN3_Msk & ((value) << TCC_WAVE_CICCEN3_Pos))
#define TCC_WAVE_POL0_Pos                     (16U)                                          /**< (TCC_WAVE) Channel 0 Polarity Position */
#define TCC_WAVE_POL0_Msk                     (0x1U << TCC_WAVE_POL0_Pos)                    /**< (TCC_WAVE) Channel 0 Polarity Mask */
#define TCC_WAVE_POL0(value)                  (TCC_WAVE_POL0_Msk & ((value) << TCC_WAVE_POL0_Pos))
#define TCC_WAVE_POL1_Pos                     (17U)                                          /**< (TCC_WAVE) Channel 1 Polarity Position */
#define TCC_WAVE_POL1_Msk                     (0x1U << TCC_WAVE_POL1_Pos)                    /**< (TCC_WAVE) Channel 1 Polarity Mask */
#define TCC_WAVE_POL1(value)                  (TCC_WAVE_POL1_Msk & ((value) << TCC_WAVE_POL1_Pos))
#define TCC_WAVE_POL2_Pos                     (18U)                                          /**< (TCC_WAVE) Channel 2 Polarity Position */
#define TCC_WAVE_POL2_Msk                     (0x1U << TCC_WAVE_POL2_Pos)                    /**< (TCC_WAVE) Channel 2 Polarity Mask */
#define TCC_WAVE_POL2(value)                  (TCC_WAVE_POL2_Msk & ((value) << TCC_WAVE_POL2_Pos))
#define TCC_WAVE_POL3_Pos                     (19U)                                          /**< (TCC_WAVE) Channel 3 Polarity Position */
#define TCC_WAVE_POL3_Msk                     (0x1U << TCC_WAVE_POL3_Pos)                    /**< (TCC_WAVE) Channel 3 Polarity Mask */
#define TCC_WAVE_POL3(value)                  (TCC_WAVE_POL3_Msk & ((value) << TCC_WAVE_POL3_Pos))
#define TCC_WAVE_SWAP0_Pos                    (24U)                                          /**< (TCC_WAVE) Swap DTI Output Pair 0 Position */
#define TCC_WAVE_SWAP0_Msk                    (0x1U << TCC_WAVE_SWAP0_Pos)                   /**< (TCC_WAVE) Swap DTI Output Pair 0 Mask */
#define TCC_WAVE_SWAP0(value)                 (TCC_WAVE_SWAP0_Msk & ((value) << TCC_WAVE_SWAP0_Pos))
#define TCC_WAVE_SWAP1_Pos                    (25U)                                          /**< (TCC_WAVE) Swap DTI Output Pair 1 Position */
#define TCC_WAVE_SWAP1_Msk                    (0x1U << TCC_WAVE_SWAP1_Pos)                   /**< (TCC_WAVE) Swap DTI Output Pair 1 Mask */
#define TCC_WAVE_SWAP1(value)                 (TCC_WAVE_SWAP1_Msk & ((value) << TCC_WAVE_SWAP1_Pos))
#define TCC_WAVE_SWAP2_Pos                    (26U)                                          /**< (TCC_WAVE) Swap DTI Output Pair 2 Position */
#define TCC_WAVE_SWAP2_Msk                    (0x1U << TCC_WAVE_SWAP2_Pos)                   /**< (TCC_WAVE) Swap DTI Output Pair 2 Mask */
#define TCC_WAVE_SWAP2(value)                 (TCC_WAVE_SWAP2_Msk & ((value) << TCC_WAVE_SWAP2_Pos))
#define TCC_WAVE_SWAP3_Pos                    (27U)                                          /**< (TCC_WAVE) Swap DTI Output Pair 3 Position */
#define TCC_WAVE_SWAP3_Msk                    (0x1U << TCC_WAVE_SWAP3_Pos)                   /**< (TCC_WAVE) Swap DTI Output Pair 3 Mask */
#define TCC_WAVE_SWAP3(value)                 (TCC_WAVE_SWAP3_Msk & ((value) << TCC_WAVE_SWAP3_Pos))
#define TCC_WAVE_Msk                          (0x0F0F0FB7UL)                                 /**< (TCC_WAVE) Register Mask  */

/* -------- TCC_PER : (TCC Offset: 0x40) (R/W 32) Period -------- */
#define TCC_PER_DITHER_Pos                    (0U)                                           /**< (TCC_PER) Dithering Cycle Number Position */
#define TCC_PER_DITHER_Msk                    (0xFU << TCC_PER_DITHER_Pos)                   /**< (TCC_PER) Dithering Cycle Number Mask */
#define TCC_PER_DITHER(value)                 (TCC_PER_DITHER_Msk & ((value) << TCC_PER_DITHER_Pos))
#define TCC_PER_PER_Pos                       (6U)                                           /**< (TCC_PER) Period Value Position */
#define TCC_PER_PER_Msk                       (0x3FFFFU << TCC_PER_PER_Pos)                  /**< (TCC_PER) Period Value Mask */
#define TCC_PER_PER(value)                    (TCC_PER_PER_Msk & ((value) << TCC_PER_PER_Pos))
#define TCC_PER_Msk                           (0x00FFFFFFUL)                                 /**< (TCC_PER) Register Mask  */

/* -------- TCC_CC : (TCC Offset: 0x44) (R/W 32) Compare and Capture -------- */
#define TCC_CC_DITHER_Pos                     (0U)                                           /**< (TCC_CC) Dithering Cycle Number Position */
#define TCC_CC_DITHER_Msk                     (0xFU << TCC_CC_DITHER_Pos)                    /**< (TCC_CC) Dithering Cycle Number Mask */
#define TCC_CC_DITHER(value)                  (TCC_CC_DITHER_Msk & ((value) << TCC_CC_DITHER_Pos))
#define TCC_CC_CC_Pos                         (5U)                                           /**< (TCC_CC) Channel Compare/Capture Value Position */
#define TCC_CC_CC_Msk                         (0x7FFFFU << TCC_CC_CC_Pos)                    /**< (TCC_CC) Channel Compare/Capture Value Mask */
#define TCC_CC_CC(value)                      (TCC_CC_CC_Msk & ((value) << TCC_CC_CC_Pos))  
#define TCC_CC_Msk                            (0x00FFFFFFUL)                                 /**< (TCC_CC) Register Mask  */

/* -------- TCC_PATTBUF : (TCC Offset: 0x64) (R/W 16) Pattern Buffer -------- */
#define TCC_PATTBUF_PGEB0_Pos                 (0U)                                           /**< (TCC_PATTBUF) Pattern Generator 0 Output Enable Buffer Position */
#define TCC_PATTBUF_PGEB0_Msk                 (0x1U << TCC_PATTBUF_PGEB0_Pos)                /**< (TCC_PATTBUF) Pattern Generator 0 Output Enable Buffer Mask */
#define TCC_PATTBUF_PGEB0(value)              (TCC_PATTBUF_PGEB0_Msk & ((value) << TCC_PATTBUF_PGEB0_Pos))
#define TCC_PATTBUF_PGEB1_Pos                 (1U)                                           /**< (TCC_PATTBUF) Pattern Generator 1 Output Enable Buffer Position */
#define TCC_PATTBUF_PGEB1_Msk                 (0x1U << TCC_PATTBUF_PGEB1_Pos)                /**< (TCC_PATTBUF) Pattern Generator 1 Output Enable Buffer Mask */
#define TCC_PATTBUF_PGEB1(value)              (TCC_PATTBUF_PGEB1_Msk & ((value) << TCC_PATTBUF_PGEB1_Pos))
#define TCC_PATTBUF_PGEB2_Pos                 (2U)                                           /**< (TCC_PATTBUF) Pattern Generator 2 Output Enable Buffer Position */
#define TCC_PATTBUF_PGEB2_Msk                 (0x1U << TCC_PATTBUF_PGEB2_Pos)                /**< (TCC_PATTBUF) Pattern Generator 2 Output Enable Buffer Mask */
#define TCC_PATTBUF_PGEB2(value)              (TCC_PATTBUF_PGEB2_Msk & ((value) << TCC_PATTBUF_PGEB2_Pos))
#define TCC_PATTBUF_PGEB3_Pos                 (3U)                                           /**< (TCC_PATTBUF) Pattern Generator 3 Output Enable Buffer Position */
#define TCC_PATTBUF_PGEB3_Msk                 (0x1U << TCC_PATTBUF_PGEB3_Pos)                /**< (TCC_PATTBUF) Pattern Generator 3 Output Enable Buffer Mask */
#define TCC_PATTBUF_PGEB3(value)              (TCC_PATTBUF_PGEB3_Msk & ((value) << TCC_PATTBUF_PGEB3_Pos))
#define TCC_PATTBUF_PGEB4_Pos                 (4U)                                           /**< (TCC_PATTBUF) Pattern Generator 4 Output Enable Buffer Position */
#define TCC_PATTBUF_PGEB4_Msk                 (0x1U << TCC_PATTBUF_PGEB4_Pos)                /**< (TCC_PATTBUF) Pattern Generator 4 Output Enable Buffer Mask */
#define TCC_PATTBUF_PGEB4(value)              (TCC_PATTBUF_PGEB4_Msk & ((value) << TCC_PATTBUF_PGEB4_Pos))
#define TCC_PATTBUF_PGEB5_Pos                 (5U)                                           /**< (TCC_PATTBUF) Pattern Generator 5 Output Enable Buffer Position */
#define TCC_PATTBUF_PGEB5_Msk                 (0x1U << TCC_PATTBUF_PGEB5_Pos)                /**< (TCC_PATTBUF) Pattern Generator 5 Output Enable Buffer Mask */
#define TCC_PATTBUF_PGEB5(value)              (TCC_PATTBUF_PGEB5_Msk & ((value) << TCC_PATTBUF_PGEB5_Pos))
#define TCC_PATTBUF_PGEB6_Pos                 (6U)                                           /**< (TCC_PATTBUF) Pattern Generator 6 Output Enable Buffer Position */
#define TCC_PATTBUF_PGEB6_Msk                 (0x1U << TCC_PATTBUF_PGEB6_Pos)                /**< (TCC_PATTBUF) Pattern Generator 6 Output Enable Buffer Mask */
#define TCC_PATTBUF_PGEB6(value)              (TCC_PATTBUF_PGEB6_Msk & ((value) << TCC_PATTBUF_PGEB6_Pos))
#define TCC_PATTBUF_PGEB7_Pos                 (7U)                                           /**< (TCC_PATTBUF) Pattern Generator 7 Output Enable Buffer Position */
#define TCC_PATTBUF_PGEB7_Msk                 (0x1U << TCC_PATTBUF_PGEB7_Pos)                /**< (TCC_PATTBUF) Pattern Generator 7 Output Enable Buffer Mask */
#define TCC_PATTBUF_PGEB7(value)              (TCC_PATTBUF_PGEB7_Msk & ((value) << TCC_PATTBUF_PGEB7_Pos))
#define TCC_PATTBUF_PGVB0_Pos                 (8U)                                           /**< (TCC_PATTBUF) Pattern Generator 0 Output Enable Position */
#define TCC_PATTBUF_PGVB0_Msk                 (0x1U << TCC_PATTBUF_PGVB0_Pos)                /**< (TCC_PATTBUF) Pattern Generator 0 Output Enable Mask */
#define TCC_PATTBUF_PGVB0(value)              (TCC_PATTBUF_PGVB0_Msk & ((value) << TCC_PATTBUF_PGVB0_Pos))
#define TCC_PATTBUF_PGVB1_Pos                 (9U)                                           /**< (TCC_PATTBUF) Pattern Generator 1 Output Enable Position */
#define TCC_PATTBUF_PGVB1_Msk                 (0x1U << TCC_PATTBUF_PGVB1_Pos)                /**< (TCC_PATTBUF) Pattern Generator 1 Output Enable Mask */
#define TCC_PATTBUF_PGVB1(value)              (TCC_PATTBUF_PGVB1_Msk & ((value) << TCC_PATTBUF_PGVB1_Pos))
#define TCC_PATTBUF_PGVB2_Pos                 (10U)                                          /**< (TCC_PATTBUF) Pattern Generator 2 Output Enable Position */
#define TCC_PATTBUF_PGVB2_Msk                 (0x1U << TCC_PATTBUF_PGVB2_Pos)                /**< (TCC_PATTBUF) Pattern Generator 2 Output Enable Mask */
#define TCC_PATTBUF_PGVB2(value)              (TCC_PATTBUF_PGVB2_Msk & ((value) << TCC_PATTBUF_PGVB2_Pos))
#define TCC_PATTBUF_PGVB3_Pos                 (11U)                                          /**< (TCC_PATTBUF) Pattern Generator 3 Output Enable Position */
#define TCC_PATTBUF_PGVB3_Msk                 (0x1U << TCC_PATTBUF_PGVB3_Pos)                /**< (TCC_PATTBUF) Pattern Generator 3 Output Enable Mask */
#define TCC_PATTBUF_PGVB3(value)              (TCC_PATTBUF_PGVB3_Msk & ((value) << TCC_PATTBUF_PGVB3_Pos))
#define TCC_PATTBUF_PGVB4_Pos                 (12U)                                          /**< (TCC_PATTBUF) Pattern Generator 4 Output Enable Position */
#define TCC_PATTBUF_PGVB4_Msk                 (0x1U << TCC_PATTBUF_PGVB4_Pos)                /**< (TCC_PATTBUF) Pattern Generator 4 Output Enable Mask */
#define TCC_PATTBUF_PGVB4(value)              (TCC_PATTBUF_PGVB4_Msk & ((value) << TCC_PATTBUF_PGVB4_Pos))
#define TCC_PATTBUF_PGVB5_Pos                 (13U)                                          /**< (TCC_PATTBUF) Pattern Generator 5 Output Enable Position */
#define TCC_PATTBUF_PGVB5_Msk                 (0x1U << TCC_PATTBUF_PGVB5_Pos)                /**< (TCC_PATTBUF) Pattern Generator 5 Output Enable Mask */
#define TCC_PATTBUF_PGVB5(value)              (TCC_PATTBUF_PGVB5_Msk & ((value) << TCC_PATTBUF_PGVB5_Pos))
#define TCC_PATTBUF_PGVB6_Pos                 (14U)                                          /**< (TCC_PATTBUF) Pattern Generator 6 Output Enable Position */
#define TCC_PATTBUF_PGVB6_Msk                 (0x1U << TCC_PATTBUF_PGVB6_Pos)                /**< (TCC_PATTBUF) Pattern Generator 6 Output Enable Mask */
#define TCC_PATTBUF_PGVB6(value)              (TCC_PATTBUF_PGVB6_Msk & ((value) << TCC_PATTBUF_PGVB6_Pos))
#define TCC_PATTBUF_PGVB7_Pos                 (15U)                                          /**< (TCC_PATTBUF) Pattern Generator 7 Output Enable Position */
#define TCC_PATTBUF_PGVB7_Msk                 (0x1U << TCC_PATTBUF_PGVB7_Pos)                /**< (TCC_PATTBUF) Pattern Generator 7 Output Enable Mask */
#define TCC_PATTBUF_PGVB7(value)              (TCC_PATTBUF_PGVB7_Msk & ((value) << TCC_PATTBUF_PGVB7_Pos))
#define TCC_PATTBUF_Msk                       (0x0000FFFFUL)                                 /**< (TCC_PATTBUF) Register Mask  */

/* -------- TCC_PERBUF : (TCC Offset: 0x6C) (R/W 32) Period Buffer -------- */
#define TCC_PERBUF_DITHERBUF_Pos              (0U)                                           /**< (TCC_PERBUF) Dithering Buffer Cycle Number Position */
#define TCC_PERBUF_DITHERBUF_Msk              (0xFU << TCC_PERBUF_DITHERBUF_Pos)             /**< (TCC_PERBUF) Dithering Buffer Cycle Number Mask */
#define TCC_PERBUF_DITHERBUF(value)           (TCC_PERBUF_DITHERBUF_Msk & ((value) << TCC_PERBUF_DITHERBUF_Pos))
#define TCC_PERBUF_PERBUF_Pos                 (6U)                                           /**< (TCC_PERBUF) Period Buffer Value Position */
#define TCC_PERBUF_PERBUF_Msk                 (0x3FFFFU << TCC_PERBUF_PERBUF_Pos)            /**< (TCC_PERBUF) Period Buffer Value Mask */
#define TCC_PERBUF_PERBUF(value)              (TCC_PERBUF_PERBUF_Msk & ((value) << TCC_PERBUF_PERBUF_Pos))
#define TCC_PERBUF_Msk                        (0x00FFFFFFUL)                                 /**< (TCC_PERBUF) Register Mask  */

/* -------- TCC_CCBUF : (TCC Offset: 0x70) (R/W 32) Compare and Capture Buffer -------- */
#define TCC_CCBUF_CCBUF_Pos                   (0U)                                           /**< (TCC_CCBUF) Channel Compare/Capture Buffer Value Position */
#define TCC_CCBUF_CCBUF_Msk                   (0xFU << TCC_CCBUF_CCBUF_Pos)                  /**< (TCC_CCBUF) Channel Compare/Capture Buffer Value Mask */
#define TCC_CCBUF_CCBUF(value)                (TCC_CCBUF_CCBUF_Msk & ((value) << TCC_CCBUF_CCBUF_Pos))
#define TCC_CCBUF_DITHERBUF_Pos               (0U)                                           /**< (TCC_CCBUF) Dithering Buffer Cycle Number Position */
#define TCC_CCBUF_DITHERBUF_Msk               (0x1FU << TCC_CCBUF_DITHERBUF_Pos)             /**< (TCC_CCBUF) Dithering Buffer Cycle Number Mask */
#define TCC_CCBUF_DITHERBUF(value)            (TCC_CCBUF_DITHERBUF_Msk & ((value) << TCC_CCBUF_DITHERBUF_Pos))
#define TCC_CCBUF_Msk                         (0x00FFFFFFUL)                                 /**< (TCC_CCBUF) Register Mask  */

/** \brief TCC register offsets definitions */
#define TCC_CTRLA_OFFSET               (0x00)         /**< (TCC_CTRLA) Control A Offset */
#define TCC_CTRLBCLR_OFFSET            (0x04)         /**< (TCC_CTRLBCLR) Control B Clear Offset */
#define TCC_CTRLBSET_OFFSET            (0x05)         /**< (TCC_CTRLBSET) Control B Set Offset */
#define TCC_SYNCBUSY_OFFSET            (0x08)         /**< (TCC_SYNCBUSY) Synchronization Busy Offset */
#define TCC_FCTRLA_OFFSET              (0x0C)         /**< (TCC_FCTRLA) Recoverable Fault A Configuration Offset */
#define TCC_FCTRLB_OFFSET              (0x10)         /**< (TCC_FCTRLB) Recoverable Fault B Configuration Offset */
#define TCC_WEXCTRL_OFFSET             (0x14)         /**< (TCC_WEXCTRL) Waveform Extension Configuration Offset */
#define TCC_DRVCTRL_OFFSET             (0x18)         /**< (TCC_DRVCTRL) Driver Control Offset */
#define TCC_DBGCTRL_OFFSET             (0x1E)         /**< (TCC_DBGCTRL) Debug Control Offset */
#define TCC_EVCTRL_OFFSET              (0x20)         /**< (TCC_EVCTRL) Event Control Offset */
#define TCC_INTENCLR_OFFSET            (0x24)         /**< (TCC_INTENCLR) Interrupt Enable Clear Offset */
#define TCC_INTENSET_OFFSET            (0x28)         /**< (TCC_INTENSET) Interrupt Enable Set Offset */
#define TCC_INTFLAG_OFFSET             (0x2C)         /**< (TCC_INTFLAG) Interrupt Flag Status and Clear Offset */
#define TCC_STATUS_OFFSET              (0x30)         /**< (TCC_STATUS) Status Offset */
#define TCC_COUNT_OFFSET               (0x34)         /**< (TCC_COUNT) Count Offset */
#define TCC_PATT_OFFSET                (0x38)         /**< (TCC_PATT) Pattern Offset */
#define TCC_WAVE_OFFSET                (0x3C)         /**< (TCC_WAVE) Waveform Control Offset */
#define TCC_PER_OFFSET                 (0x40)         /**< (TCC_PER) Period Offset */
#define TCC_CC_OFFSET                  (0x44)         /**< (TCC_CC) Compare and Capture Offset */
#define TCC_PATTBUF_OFFSET             (0x64)         /**< (TCC_PATTBUF) Pattern Buffer Offset */
#define TCC_PERBUF_OFFSET              (0x6C)         /**< (TCC_PERBUF) Period Buffer Offset */
#define TCC_CCBUF_OFFSET               (0x70)         /**< (TCC_CCBUF) Compare and Capture Buffer Offset */

/** \brief TCC register API structure */
typedef struct
{
  __IO  uint32_t                       TCC_CTRLA;       /**< Offset: 0x00 (R/W  32) Control A */
  __IO  uint8_t                        TCC_CTRLBCLR;    /**< Offset: 0x04 (R/W  8) Control B Clear */
  __IO  uint8_t                        TCC_CTRLBSET;    /**< Offset: 0x05 (R/W  8) Control B Set */
  __I   uint8_t                        Reserved1[0x02];
  __I   uint32_t                       TCC_SYNCBUSY;    /**< Offset: 0x08 (R/   32) Synchronization Busy */
  __IO  uint32_t                       TCC_FCTRLA;      /**< Offset: 0x0c (R/W  32) Recoverable Fault A Configuration */
  __IO  uint32_t                       TCC_FCTRLB;      /**< Offset: 0x10 (R/W  32) Recoverable Fault B Configuration */
  __IO  uint32_t                       TCC_WEXCTRL;     /**< Offset: 0x14 (R/W  32) Waveform Extension Configuration */
  __IO  uint32_t                       TCC_DRVCTRL;     /**< Offset: 0x18 (R/W  32) Driver Control */
  __I   uint8_t                        Reserved2[0x02];
  __IO  uint8_t                        TCC_DBGCTRL;     /**< Offset: 0x1e (R/W  8) Debug Control */
  __I   uint8_t                        Reserved3[0x01];
  __IO  uint32_t                       TCC_EVCTRL;      /**< Offset: 0x20 (R/W  32) Event Control */
  __IO  uint32_t                       TCC_INTENCLR;    /**< Offset: 0x24 (R/W  32) Interrupt Enable Clear */
  __IO  uint32_t                       TCC_INTENSET;    /**< Offset: 0x28 (R/W  32) Interrupt Enable Set */
  __IO  uint32_t                       TCC_INTFLAG;     /**< Offset: 0x2c (R/W  32) Interrupt Flag Status and Clear */
  __IO  uint32_t                       TCC_STATUS;      /**< Offset: 0x30 (R/W  32) Status */
  __IO  uint32_t                       TCC_COUNT;       /**< Offset: 0x34 (R/W  32) Count */
  __IO  uint16_t                       TCC_PATT;        /**< Offset: 0x38 (R/W  16) Pattern */
  __I   uint8_t                        Reserved4[0x02];
  __IO  uint32_t                       TCC_WAVE;        /**< Offset: 0x3c (R/W  32) Waveform Control */
  __IO  uint32_t                       TCC_PER;         /**< Offset: 0x40 (R/W  32) Period */
  __IO  uint32_t                       TCC_CC[4];       /**< Offset: 0x44 (R/W  32) Compare and Capture */
  __I   uint8_t                        Reserved5[0x10];
  __IO  uint16_t                       TCC_PATTBUF;     /**< Offset: 0x64 (R/W  16) Pattern Buffer */
  __I   uint8_t                        Reserved6[0x06];
  __IO  uint32_t                       TCC_PERBUF;      /**< Offset: 0x6c (R/W  32) Period Buffer */
  __IO  uint32_t                       TCC_CCBUF[4];    /**< Offset: 0x70 (R/W  32) Compare and Capture Buffer */
} tcc_registers_t;
/** @}  end of Timer Counter Control */

#endif /* SAMC_SAMC21_TCC_MODULE_H */

