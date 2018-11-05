/**
 * \brief Header file for SAMC/SAMC21 TC
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
#ifndef SAMC_SAMC21_TC_MODULE_H
#define SAMC_SAMC21_TC_MODULE_H

/** \addtogroup SAMC_SAMC21 Basic Timer Counter
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_TC                                    */
/* ========================================================================== */

/* -------- TC_CTRLA : (TC Offset: 0x00) (R/W 32) Control A -------- */
#define TC_CTRLA_SWRST_Pos                    (0U)                                           /**< (TC_CTRLA) Software Reset Position */
#define TC_CTRLA_SWRST_Msk                    (0x1U << TC_CTRLA_SWRST_Pos)                   /**< (TC_CTRLA) Software Reset Mask */
#define TC_CTRLA_SWRST(value)                 (TC_CTRLA_SWRST_Msk & ((value) << TC_CTRLA_SWRST_Pos))
#define TC_CTRLA_ENABLE_Pos                   (1U)                                           /**< (TC_CTRLA) Enable Position */
#define TC_CTRLA_ENABLE_Msk                   (0x1U << TC_CTRLA_ENABLE_Pos)                  /**< (TC_CTRLA) Enable Mask */
#define TC_CTRLA_ENABLE(value)                (TC_CTRLA_ENABLE_Msk & ((value) << TC_CTRLA_ENABLE_Pos))
#define TC_CTRLA_MODE_Pos                     (2U)                                           /**< (TC_CTRLA) Timer Counter Mode Position */
#define TC_CTRLA_MODE_Msk                     (0x3U << TC_CTRLA_MODE_Pos)                    /**< (TC_CTRLA) Timer Counter Mode Mask */
#define TC_CTRLA_MODE(value)                  (TC_CTRLA_MODE_Msk & ((value) << TC_CTRLA_MODE_Pos))
#define   TC_CTRLA_MODE_COUNT16_Val           (0U)                                           /**< (TC_CTRLA) Counter in 16-bit mode  */
#define   TC_CTRLA_MODE_COUNT8_Val            (1U)                                           /**< (TC_CTRLA) Counter in 8-bit mode  */
#define   TC_CTRLA_MODE_COUNT32_Val           (2U)                                           /**< (TC_CTRLA) Counter in 32-bit mode  */
#define TC_CTRLA_MODE_COUNT16                 (TC_CTRLA_MODE_COUNT16_Val << TC_CTRLA_MODE_Pos) /**< (TC_CTRLA) Counter in 16-bit mode Position  */
#define TC_CTRLA_MODE_COUNT8                  (TC_CTRLA_MODE_COUNT8_Val << TC_CTRLA_MODE_Pos) /**< (TC_CTRLA) Counter in 8-bit mode Position  */
#define TC_CTRLA_MODE_COUNT32                 (TC_CTRLA_MODE_COUNT32_Val << TC_CTRLA_MODE_Pos) /**< (TC_CTRLA) Counter in 32-bit mode Position  */
#define TC_CTRLA_PRESCSYNC_Pos                (4U)                                           /**< (TC_CTRLA) Prescaler and Counter Synchronization Position */
#define TC_CTRLA_PRESCSYNC_Msk                (0x3U << TC_CTRLA_PRESCSYNC_Pos)               /**< (TC_CTRLA) Prescaler and Counter Synchronization Mask */
#define TC_CTRLA_PRESCSYNC(value)             (TC_CTRLA_PRESCSYNC_Msk & ((value) << TC_CTRLA_PRESCSYNC_Pos))
#define   TC_CTRLA_PRESCSYNC_GCLK_Val         (0U)                                           /**< (TC_CTRLA) Reload or reset the counter on next generic clock  */
#define   TC_CTRLA_PRESCSYNC_PRESC_Val        (1U)                                           /**< (TC_CTRLA) Reload or reset the counter on next prescaler clock  */
#define   TC_CTRLA_PRESCSYNC_RESYNC_Val       (2U)                                           /**< (TC_CTRLA) Reload or reset the counter on next generic clock and reset the prescaler counter  */
#define TC_CTRLA_PRESCSYNC_GCLK               (TC_CTRLA_PRESCSYNC_GCLK_Val << TC_CTRLA_PRESCSYNC_Pos) /**< (TC_CTRLA) Reload or reset the counter on next generic clock Position  */
#define TC_CTRLA_PRESCSYNC_PRESC              (TC_CTRLA_PRESCSYNC_PRESC_Val << TC_CTRLA_PRESCSYNC_Pos) /**< (TC_CTRLA) Reload or reset the counter on next prescaler clock Position  */
#define TC_CTRLA_PRESCSYNC_RESYNC             (TC_CTRLA_PRESCSYNC_RESYNC_Val << TC_CTRLA_PRESCSYNC_Pos) /**< (TC_CTRLA) Reload or reset the counter on next generic clock and reset the prescaler counter Position  */
#define TC_CTRLA_RUNSTDBY_Pos                 (6U)                                           /**< (TC_CTRLA) Run during Standby Position */
#define TC_CTRLA_RUNSTDBY_Msk                 (0x1U << TC_CTRLA_RUNSTDBY_Pos)                /**< (TC_CTRLA) Run during Standby Mask */
#define TC_CTRLA_RUNSTDBY(value)              (TC_CTRLA_RUNSTDBY_Msk & ((value) << TC_CTRLA_RUNSTDBY_Pos))
#define TC_CTRLA_ONDEMAND_Pos                 (7U)                                           /**< (TC_CTRLA) Clock On Demand Position */
#define TC_CTRLA_ONDEMAND_Msk                 (0x1U << TC_CTRLA_ONDEMAND_Pos)                /**< (TC_CTRLA) Clock On Demand Mask */
#define TC_CTRLA_ONDEMAND(value)              (TC_CTRLA_ONDEMAND_Msk & ((value) << TC_CTRLA_ONDEMAND_Pos))
#define TC_CTRLA_PRESCALER_Pos                (8U)                                           /**< (TC_CTRLA) Prescaler Position */
#define TC_CTRLA_PRESCALER_Msk                (0x7U << TC_CTRLA_PRESCALER_Pos)               /**< (TC_CTRLA) Prescaler Mask */
#define TC_CTRLA_PRESCALER(value)             (TC_CTRLA_PRESCALER_Msk & ((value) << TC_CTRLA_PRESCALER_Pos))
#define   TC_CTRLA_PRESCALER_DIV1_Val         (0U)                                           /**< (TC_CTRLA) Prescaler: GCLK_TC  */
#define   TC_CTRLA_PRESCALER_DIV2_Val         (1U)                                           /**< (TC_CTRLA) Prescaler: GCLK_TC/2  */
#define   TC_CTRLA_PRESCALER_DIV4_Val         (2U)                                           /**< (TC_CTRLA) Prescaler: GCLK_TC/4  */
#define   TC_CTRLA_PRESCALER_DIV8_Val         (3U)                                           /**< (TC_CTRLA) Prescaler: GCLK_TC/8  */
#define   TC_CTRLA_PRESCALER_DIV16_Val        (4U)                                           /**< (TC_CTRLA) Prescaler: GCLK_TC/16  */
#define   TC_CTRLA_PRESCALER_DIV64_Val        (5U)                                           /**< (TC_CTRLA) Prescaler: GCLK_TC/64  */
#define   TC_CTRLA_PRESCALER_DIV256_Val       (6U)                                           /**< (TC_CTRLA) Prescaler: GCLK_TC/256  */
#define   TC_CTRLA_PRESCALER_DIV1024_Val      (7U)                                           /**< (TC_CTRLA) Prescaler: GCLK_TC/1024  */
#define TC_CTRLA_PRESCALER_DIV1               (TC_CTRLA_PRESCALER_DIV1_Val << TC_CTRLA_PRESCALER_Pos) /**< (TC_CTRLA) Prescaler: GCLK_TC Position  */
#define TC_CTRLA_PRESCALER_DIV2               (TC_CTRLA_PRESCALER_DIV2_Val << TC_CTRLA_PRESCALER_Pos) /**< (TC_CTRLA) Prescaler: GCLK_TC/2 Position  */
#define TC_CTRLA_PRESCALER_DIV4               (TC_CTRLA_PRESCALER_DIV4_Val << TC_CTRLA_PRESCALER_Pos) /**< (TC_CTRLA) Prescaler: GCLK_TC/4 Position  */
#define TC_CTRLA_PRESCALER_DIV8               (TC_CTRLA_PRESCALER_DIV8_Val << TC_CTRLA_PRESCALER_Pos) /**< (TC_CTRLA) Prescaler: GCLK_TC/8 Position  */
#define TC_CTRLA_PRESCALER_DIV16              (TC_CTRLA_PRESCALER_DIV16_Val << TC_CTRLA_PRESCALER_Pos) /**< (TC_CTRLA) Prescaler: GCLK_TC/16 Position  */
#define TC_CTRLA_PRESCALER_DIV64              (TC_CTRLA_PRESCALER_DIV64_Val << TC_CTRLA_PRESCALER_Pos) /**< (TC_CTRLA) Prescaler: GCLK_TC/64 Position  */
#define TC_CTRLA_PRESCALER_DIV256             (TC_CTRLA_PRESCALER_DIV256_Val << TC_CTRLA_PRESCALER_Pos) /**< (TC_CTRLA) Prescaler: GCLK_TC/256 Position  */
#define TC_CTRLA_PRESCALER_DIV1024            (TC_CTRLA_PRESCALER_DIV1024_Val << TC_CTRLA_PRESCALER_Pos) /**< (TC_CTRLA) Prescaler: GCLK_TC/1024 Position  */
#define TC_CTRLA_ALOCK_Pos                    (11U)                                          /**< (TC_CTRLA) Auto Lock Position */
#define TC_CTRLA_ALOCK_Msk                    (0x1U << TC_CTRLA_ALOCK_Pos)                   /**< (TC_CTRLA) Auto Lock Mask */
#define TC_CTRLA_ALOCK(value)                 (TC_CTRLA_ALOCK_Msk & ((value) << TC_CTRLA_ALOCK_Pos))
#define TC_CTRLA_CAPTEN0_Pos                  (16U)                                          /**< (TC_CTRLA) Capture Channel 0 Enable Position */
#define TC_CTRLA_CAPTEN0_Msk                  (0x1U << TC_CTRLA_CAPTEN0_Pos)                 /**< (TC_CTRLA) Capture Channel 0 Enable Mask */
#define TC_CTRLA_CAPTEN0(value)               (TC_CTRLA_CAPTEN0_Msk & ((value) << TC_CTRLA_CAPTEN0_Pos))
#define TC_CTRLA_CAPTEN1_Pos                  (17U)                                          /**< (TC_CTRLA) Capture Channel 1 Enable Position */
#define TC_CTRLA_CAPTEN1_Msk                  (0x1U << TC_CTRLA_CAPTEN1_Pos)                 /**< (TC_CTRLA) Capture Channel 1 Enable Mask */
#define TC_CTRLA_CAPTEN1(value)               (TC_CTRLA_CAPTEN1_Msk & ((value) << TC_CTRLA_CAPTEN1_Pos))
#define TC_CTRLA_COPEN0_Pos                   (20U)                                          /**< (TC_CTRLA) Capture On Pin 0 Enable Position */
#define TC_CTRLA_COPEN0_Msk                   (0x1U << TC_CTRLA_COPEN0_Pos)                  /**< (TC_CTRLA) Capture On Pin 0 Enable Mask */
#define TC_CTRLA_COPEN0(value)                (TC_CTRLA_COPEN0_Msk & ((value) << TC_CTRLA_COPEN0_Pos))
#define TC_CTRLA_COPEN1_Pos                   (21U)                                          /**< (TC_CTRLA) Capture On Pin 1 Enable Position */
#define TC_CTRLA_COPEN1_Msk                   (0x1U << TC_CTRLA_COPEN1_Pos)                  /**< (TC_CTRLA) Capture On Pin 1 Enable Mask */
#define TC_CTRLA_COPEN1(value)                (TC_CTRLA_COPEN1_Msk & ((value) << TC_CTRLA_COPEN1_Pos))
#define TC_CTRLA_CAPTMODE0_Pos                (24U)                                          /**< (TC_CTRLA) Capture Mode Channel 0 Position */
#define TC_CTRLA_CAPTMODE0_Msk                (0x3U << TC_CTRLA_CAPTMODE0_Pos)               /**< (TC_CTRLA) Capture Mode Channel 0 Mask */
#define TC_CTRLA_CAPTMODE0(value)             (TC_CTRLA_CAPTMODE0_Msk & ((value) << TC_CTRLA_CAPTMODE0_Pos))
#define   TC_CTRLA_CAPTMODE0_DEFAULT_Val      (0U)                                           /**< (TC_CTRLA) Default capture  */
#define   TC_CTRLA_CAPTMODE0_CAPTMIN_Val      (1U)                                           /**< (TC_CTRLA) Minimum capture  */
#define   TC_CTRLA_CAPTMODE0_CAPTMAX_Val      (2U)                                           /**< (TC_CTRLA) Maximum capture  */
#define TC_CTRLA_CAPTMODE0_DEFAULT            (TC_CTRLA_CAPTMODE0_DEFAULT_Val << TC_CTRLA_CAPTMODE0_Pos) /**< (TC_CTRLA) Default capture Position  */
#define TC_CTRLA_CAPTMODE0_CAPTMIN            (TC_CTRLA_CAPTMODE0_CAPTMIN_Val << TC_CTRLA_CAPTMODE0_Pos) /**< (TC_CTRLA) Minimum capture Position  */
#define TC_CTRLA_CAPTMODE0_CAPTMAX            (TC_CTRLA_CAPTMODE0_CAPTMAX_Val << TC_CTRLA_CAPTMODE0_Pos) /**< (TC_CTRLA) Maximum capture Position  */
#define TC_CTRLA_CAPTMODE1_Pos                (27U)                                          /**< (TC_CTRLA) Capture mode Channel 1 Position */
#define TC_CTRLA_CAPTMODE1_Msk                (0x3U << TC_CTRLA_CAPTMODE1_Pos)               /**< (TC_CTRLA) Capture mode Channel 1 Mask */
#define TC_CTRLA_CAPTMODE1(value)             (TC_CTRLA_CAPTMODE1_Msk & ((value) << TC_CTRLA_CAPTMODE1_Pos))
#define   TC_CTRLA_CAPTMODE1_DEFAULT_Val      (0U)                                           /**< (TC_CTRLA) Default capture  */
#define   TC_CTRLA_CAPTMODE1_CAPTMIN_Val      (1U)                                           /**< (TC_CTRLA) Minimum capture  */
#define   TC_CTRLA_CAPTMODE1_CAPTMAX_Val      (2U)                                           /**< (TC_CTRLA) Maximum capture  */
#define TC_CTRLA_CAPTMODE1_DEFAULT            (TC_CTRLA_CAPTMODE1_DEFAULT_Val << TC_CTRLA_CAPTMODE1_Pos) /**< (TC_CTRLA) Default capture Position  */
#define TC_CTRLA_CAPTMODE1_CAPTMIN            (TC_CTRLA_CAPTMODE1_CAPTMIN_Val << TC_CTRLA_CAPTMODE1_Pos) /**< (TC_CTRLA) Minimum capture Position  */
#define TC_CTRLA_CAPTMODE1_CAPTMAX            (TC_CTRLA_CAPTMODE1_CAPTMAX_Val << TC_CTRLA_CAPTMODE1_Pos) /**< (TC_CTRLA) Maximum capture Position  */
#define TC_CTRLA_Msk                          (0x1B330FFFUL)                                 /**< (TC_CTRLA) Register Mask  */

/* -------- TC_CTRLBCLR : (TC Offset: 0x04) (R/W 8) Control B Clear -------- */
#define TC_CTRLBCLR_DIR_Pos                   (0U)                                           /**< (TC_CTRLBCLR) Counter Direction Position */
#define TC_CTRLBCLR_DIR_Msk                   (0x1U << TC_CTRLBCLR_DIR_Pos)                  /**< (TC_CTRLBCLR) Counter Direction Mask */
#define TC_CTRLBCLR_DIR(value)                (TC_CTRLBCLR_DIR_Msk & ((value) << TC_CTRLBCLR_DIR_Pos))
#define TC_CTRLBCLR_LUPD_Pos                  (1U)                                           /**< (TC_CTRLBCLR) Lock Update Position */
#define TC_CTRLBCLR_LUPD_Msk                  (0x1U << TC_CTRLBCLR_LUPD_Pos)                 /**< (TC_CTRLBCLR) Lock Update Mask */
#define TC_CTRLBCLR_LUPD(value)               (TC_CTRLBCLR_LUPD_Msk & ((value) << TC_CTRLBCLR_LUPD_Pos))
#define TC_CTRLBCLR_ONESHOT_Pos               (2U)                                           /**< (TC_CTRLBCLR) One-Shot on Counter Position */
#define TC_CTRLBCLR_ONESHOT_Msk               (0x1U << TC_CTRLBCLR_ONESHOT_Pos)              /**< (TC_CTRLBCLR) One-Shot on Counter Mask */
#define TC_CTRLBCLR_ONESHOT(value)            (TC_CTRLBCLR_ONESHOT_Msk & ((value) << TC_CTRLBCLR_ONESHOT_Pos))
#define TC_CTRLBCLR_CMD_Pos                   (5U)                                           /**< (TC_CTRLBCLR) Command Position */
#define TC_CTRLBCLR_CMD_Msk                   (0x7U << TC_CTRLBCLR_CMD_Pos)                  /**< (TC_CTRLBCLR) Command Mask */
#define TC_CTRLBCLR_CMD(value)                (TC_CTRLBCLR_CMD_Msk & ((value) << TC_CTRLBCLR_CMD_Pos))
#define   TC_CTRLBCLR_CMD_NONE_Val            (0U)                                           /**< (TC_CTRLBCLR) No action  */
#define   TC_CTRLBCLR_CMD_RETRIGGER_Val       (1U)                                           /**< (TC_CTRLBCLR) Force a start, restart or retrigger  */
#define   TC_CTRLBCLR_CMD_STOP_Val            (2U)                                           /**< (TC_CTRLBCLR) Force a stop  */
#define   TC_CTRLBCLR_CMD_UPDATE_Val          (3U)                                           /**< (TC_CTRLBCLR) Force update of double-buffered register  */
#define   TC_CTRLBCLR_CMD_READSYNC_Val        (4U)                                           /**< (TC_CTRLBCLR) Force a read synchronization of COUNT  */
#define   TC_CTRLBCLR_CMD_DMAOS_Val           (5U)                                           /**< (TC_CTRLBCLR) One-shot DMA trigger  */
#define TC_CTRLBCLR_CMD_NONE                  (TC_CTRLBCLR_CMD_NONE_Val << TC_CTRLBCLR_CMD_Pos) /**< (TC_CTRLBCLR) No action Position  */
#define TC_CTRLBCLR_CMD_RETRIGGER             (TC_CTRLBCLR_CMD_RETRIGGER_Val << TC_CTRLBCLR_CMD_Pos) /**< (TC_CTRLBCLR) Force a start, restart or retrigger Position  */
#define TC_CTRLBCLR_CMD_STOP                  (TC_CTRLBCLR_CMD_STOP_Val << TC_CTRLBCLR_CMD_Pos) /**< (TC_CTRLBCLR) Force a stop Position  */
#define TC_CTRLBCLR_CMD_UPDATE                (TC_CTRLBCLR_CMD_UPDATE_Val << TC_CTRLBCLR_CMD_Pos) /**< (TC_CTRLBCLR) Force update of double-buffered register Position  */
#define TC_CTRLBCLR_CMD_READSYNC              (TC_CTRLBCLR_CMD_READSYNC_Val << TC_CTRLBCLR_CMD_Pos) /**< (TC_CTRLBCLR) Force a read synchronization of COUNT Position  */
#define TC_CTRLBCLR_CMD_DMAOS                 (TC_CTRLBCLR_CMD_DMAOS_Val << TC_CTRLBCLR_CMD_Pos) /**< (TC_CTRLBCLR) One-shot DMA trigger Position  */
#define TC_CTRLBCLR_Msk                       (0x000000E7UL)                                 /**< (TC_CTRLBCLR) Register Mask  */

/* -------- TC_CTRLBSET : (TC Offset: 0x05) (R/W 8) Control B Set -------- */
#define TC_CTRLBSET_DIR_Pos                   (0U)                                           /**< (TC_CTRLBSET) Counter Direction Position */
#define TC_CTRLBSET_DIR_Msk                   (0x1U << TC_CTRLBSET_DIR_Pos)                  /**< (TC_CTRLBSET) Counter Direction Mask */
#define TC_CTRLBSET_DIR(value)                (TC_CTRLBSET_DIR_Msk & ((value) << TC_CTRLBSET_DIR_Pos))
#define TC_CTRLBSET_LUPD_Pos                  (1U)                                           /**< (TC_CTRLBSET) Lock Update Position */
#define TC_CTRLBSET_LUPD_Msk                  (0x1U << TC_CTRLBSET_LUPD_Pos)                 /**< (TC_CTRLBSET) Lock Update Mask */
#define TC_CTRLBSET_LUPD(value)               (TC_CTRLBSET_LUPD_Msk & ((value) << TC_CTRLBSET_LUPD_Pos))
#define TC_CTRLBSET_ONESHOT_Pos               (2U)                                           /**< (TC_CTRLBSET) One-Shot on Counter Position */
#define TC_CTRLBSET_ONESHOT_Msk               (0x1U << TC_CTRLBSET_ONESHOT_Pos)              /**< (TC_CTRLBSET) One-Shot on Counter Mask */
#define TC_CTRLBSET_ONESHOT(value)            (TC_CTRLBSET_ONESHOT_Msk & ((value) << TC_CTRLBSET_ONESHOT_Pos))
#define TC_CTRLBSET_CMD_Pos                   (5U)                                           /**< (TC_CTRLBSET) Command Position */
#define TC_CTRLBSET_CMD_Msk                   (0x7U << TC_CTRLBSET_CMD_Pos)                  /**< (TC_CTRLBSET) Command Mask */
#define TC_CTRLBSET_CMD(value)                (TC_CTRLBSET_CMD_Msk & ((value) << TC_CTRLBSET_CMD_Pos))
#define   TC_CTRLBSET_CMD_NONE_Val            (0U)                                           /**< (TC_CTRLBSET) No action  */
#define   TC_CTRLBSET_CMD_RETRIGGER_Val       (1U)                                           /**< (TC_CTRLBSET) Force a start, restart or retrigger  */
#define   TC_CTRLBSET_CMD_STOP_Val            (2U)                                           /**< (TC_CTRLBSET) Force a stop  */
#define   TC_CTRLBSET_CMD_UPDATE_Val          (3U)                                           /**< (TC_CTRLBSET) Force update of double-buffered register  */
#define   TC_CTRLBSET_CMD_READSYNC_Val        (4U)                                           /**< (TC_CTRLBSET) Force a read synchronization of COUNT  */
#define   TC_CTRLBSET_CMD_DMAOS_Val           (5U)                                           /**< (TC_CTRLBSET) One-shot DMA trigger  */
#define TC_CTRLBSET_CMD_NONE                  (TC_CTRLBSET_CMD_NONE_Val << TC_CTRLBSET_CMD_Pos) /**< (TC_CTRLBSET) No action Position  */
#define TC_CTRLBSET_CMD_RETRIGGER             (TC_CTRLBSET_CMD_RETRIGGER_Val << TC_CTRLBSET_CMD_Pos) /**< (TC_CTRLBSET) Force a start, restart or retrigger Position  */
#define TC_CTRLBSET_CMD_STOP                  (TC_CTRLBSET_CMD_STOP_Val << TC_CTRLBSET_CMD_Pos) /**< (TC_CTRLBSET) Force a stop Position  */
#define TC_CTRLBSET_CMD_UPDATE                (TC_CTRLBSET_CMD_UPDATE_Val << TC_CTRLBSET_CMD_Pos) /**< (TC_CTRLBSET) Force update of double-buffered register Position  */
#define TC_CTRLBSET_CMD_READSYNC              (TC_CTRLBSET_CMD_READSYNC_Val << TC_CTRLBSET_CMD_Pos) /**< (TC_CTRLBSET) Force a read synchronization of COUNT Position  */
#define TC_CTRLBSET_CMD_DMAOS                 (TC_CTRLBSET_CMD_DMAOS_Val << TC_CTRLBSET_CMD_Pos) /**< (TC_CTRLBSET) One-shot DMA trigger Position  */
#define TC_CTRLBSET_Msk                       (0x000000E7UL)                                 /**< (TC_CTRLBSET) Register Mask  */

/* -------- TC_EVCTRL : (TC Offset: 0x06) (R/W 16) Event Control -------- */
#define TC_EVCTRL_EVACT_Pos                   (0U)                                           /**< (TC_EVCTRL) Event Action Position */
#define TC_EVCTRL_EVACT_Msk                   (0x7U << TC_EVCTRL_EVACT_Pos)                  /**< (TC_EVCTRL) Event Action Mask */
#define TC_EVCTRL_EVACT(value)                (TC_EVCTRL_EVACT_Msk & ((value) << TC_EVCTRL_EVACT_Pos))
#define   TC_EVCTRL_EVACT_OFF_Val             (0U)                                           /**< (TC_EVCTRL) Event action disabled  */
#define   TC_EVCTRL_EVACT_RETRIGGER_Val       (1U)                                           /**< (TC_EVCTRL) Start, restart or retrigger TC on event  */
#define   TC_EVCTRL_EVACT_COUNT_Val           (2U)                                           /**< (TC_EVCTRL) Count on event  */
#define   TC_EVCTRL_EVACT_START_Val           (3U)                                           /**< (TC_EVCTRL) Start TC on event  */
#define   TC_EVCTRL_EVACT_STAMP_Val           (4U)                                           /**< (TC_EVCTRL) Time stamp capture  */
#define   TC_EVCTRL_EVACT_PPW_Val             (5U)                                           /**< (TC_EVCTRL) Period catured in CC0, pulse width in CC1  */
#define   TC_EVCTRL_EVACT_PWP_Val             (6U)                                           /**< (TC_EVCTRL) Period catured in CC1, pulse width in CC0  */
#define   TC_EVCTRL_EVACT_PW_Val              (7U)                                           /**< (TC_EVCTRL) Pulse width capture  */
#define TC_EVCTRL_EVACT_OFF                   (TC_EVCTRL_EVACT_OFF_Val << TC_EVCTRL_EVACT_Pos) /**< (TC_EVCTRL) Event action disabled Position  */
#define TC_EVCTRL_EVACT_RETRIGGER             (TC_EVCTRL_EVACT_RETRIGGER_Val << TC_EVCTRL_EVACT_Pos) /**< (TC_EVCTRL) Start, restart or retrigger TC on event Position  */
#define TC_EVCTRL_EVACT_COUNT                 (TC_EVCTRL_EVACT_COUNT_Val << TC_EVCTRL_EVACT_Pos) /**< (TC_EVCTRL) Count on event Position  */
#define TC_EVCTRL_EVACT_START                 (TC_EVCTRL_EVACT_START_Val << TC_EVCTRL_EVACT_Pos) /**< (TC_EVCTRL) Start TC on event Position  */
#define TC_EVCTRL_EVACT_STAMP                 (TC_EVCTRL_EVACT_STAMP_Val << TC_EVCTRL_EVACT_Pos) /**< (TC_EVCTRL) Time stamp capture Position  */
#define TC_EVCTRL_EVACT_PPW                   (TC_EVCTRL_EVACT_PPW_Val << TC_EVCTRL_EVACT_Pos) /**< (TC_EVCTRL) Period catured in CC0, pulse width in CC1 Position  */
#define TC_EVCTRL_EVACT_PWP                   (TC_EVCTRL_EVACT_PWP_Val << TC_EVCTRL_EVACT_Pos) /**< (TC_EVCTRL) Period catured in CC1, pulse width in CC0 Position  */
#define TC_EVCTRL_EVACT_PW                    (TC_EVCTRL_EVACT_PW_Val << TC_EVCTRL_EVACT_Pos) /**< (TC_EVCTRL) Pulse width capture Position  */
#define TC_EVCTRL_TCINV_Pos                   (4U)                                           /**< (TC_EVCTRL) TC Event Input Polarity Position */
#define TC_EVCTRL_TCINV_Msk                   (0x1U << TC_EVCTRL_TCINV_Pos)                  /**< (TC_EVCTRL) TC Event Input Polarity Mask */
#define TC_EVCTRL_TCINV(value)                (TC_EVCTRL_TCINV_Msk & ((value) << TC_EVCTRL_TCINV_Pos))
#define TC_EVCTRL_TCEI_Pos                    (5U)                                           /**< (TC_EVCTRL) TC Event Enable Position */
#define TC_EVCTRL_TCEI_Msk                    (0x1U << TC_EVCTRL_TCEI_Pos)                   /**< (TC_EVCTRL) TC Event Enable Mask */
#define TC_EVCTRL_TCEI(value)                 (TC_EVCTRL_TCEI_Msk & ((value) << TC_EVCTRL_TCEI_Pos))
#define TC_EVCTRL_OVFEO_Pos                   (8U)                                           /**< (TC_EVCTRL) Event Output Enable Position */
#define TC_EVCTRL_OVFEO_Msk                   (0x1U << TC_EVCTRL_OVFEO_Pos)                  /**< (TC_EVCTRL) Event Output Enable Mask */
#define TC_EVCTRL_OVFEO(value)                (TC_EVCTRL_OVFEO_Msk & ((value) << TC_EVCTRL_OVFEO_Pos))
#define TC_EVCTRL_MCEO0_Pos                   (12U)                                          /**< (TC_EVCTRL) MC Event Output Enable 0 Position */
#define TC_EVCTRL_MCEO0_Msk                   (0x1U << TC_EVCTRL_MCEO0_Pos)                  /**< (TC_EVCTRL) MC Event Output Enable 0 Mask */
#define TC_EVCTRL_MCEO0(value)                (TC_EVCTRL_MCEO0_Msk & ((value) << TC_EVCTRL_MCEO0_Pos))
#define TC_EVCTRL_MCEO1_Pos                   (13U)                                          /**< (TC_EVCTRL) MC Event Output Enable 1 Position */
#define TC_EVCTRL_MCEO1_Msk                   (0x1U << TC_EVCTRL_MCEO1_Pos)                  /**< (TC_EVCTRL) MC Event Output Enable 1 Mask */
#define TC_EVCTRL_MCEO1(value)                (TC_EVCTRL_MCEO1_Msk & ((value) << TC_EVCTRL_MCEO1_Pos))
#define TC_EVCTRL_Msk                         (0x00003137UL)                                 /**< (TC_EVCTRL) Register Mask  */

/* -------- TC_INTENCLR : (TC Offset: 0x08) (R/W 8) Interrupt Enable Clear -------- */
#define TC_INTENCLR_OVF_Pos                   (0U)                                           /**< (TC_INTENCLR) OVF Interrupt Disable Position */
#define TC_INTENCLR_OVF_Msk                   (0x1U << TC_INTENCLR_OVF_Pos)                  /**< (TC_INTENCLR) OVF Interrupt Disable Mask */
#define TC_INTENCLR_OVF(value)                (TC_INTENCLR_OVF_Msk & ((value) << TC_INTENCLR_OVF_Pos))
#define TC_INTENCLR_ERR_Pos                   (1U)                                           /**< (TC_INTENCLR) ERR Interrupt Disable Position */
#define TC_INTENCLR_ERR_Msk                   (0x1U << TC_INTENCLR_ERR_Pos)                  /**< (TC_INTENCLR) ERR Interrupt Disable Mask */
#define TC_INTENCLR_ERR(value)                (TC_INTENCLR_ERR_Msk & ((value) << TC_INTENCLR_ERR_Pos))
#define TC_INTENCLR_MC0_Pos                   (4U)                                           /**< (TC_INTENCLR) MC Interrupt Disable 0 Position */
#define TC_INTENCLR_MC0_Msk                   (0x1U << TC_INTENCLR_MC0_Pos)                  /**< (TC_INTENCLR) MC Interrupt Disable 0 Mask */
#define TC_INTENCLR_MC0(value)                (TC_INTENCLR_MC0_Msk & ((value) << TC_INTENCLR_MC0_Pos))
#define TC_INTENCLR_MC1_Pos                   (5U)                                           /**< (TC_INTENCLR) MC Interrupt Disable 1 Position */
#define TC_INTENCLR_MC1_Msk                   (0x1U << TC_INTENCLR_MC1_Pos)                  /**< (TC_INTENCLR) MC Interrupt Disable 1 Mask */
#define TC_INTENCLR_MC1(value)                (TC_INTENCLR_MC1_Msk & ((value) << TC_INTENCLR_MC1_Pos))
#define TC_INTENCLR_Msk                       (0x00000033UL)                                 /**< (TC_INTENCLR) Register Mask  */

/* -------- TC_INTENSET : (TC Offset: 0x09) (R/W 8) Interrupt Enable Set -------- */
#define TC_INTENSET_OVF_Pos                   (0U)                                           /**< (TC_INTENSET) OVF Interrupt Enable Position */
#define TC_INTENSET_OVF_Msk                   (0x1U << TC_INTENSET_OVF_Pos)                  /**< (TC_INTENSET) OVF Interrupt Enable Mask */
#define TC_INTENSET_OVF(value)                (TC_INTENSET_OVF_Msk & ((value) << TC_INTENSET_OVF_Pos))
#define TC_INTENSET_ERR_Pos                   (1U)                                           /**< (TC_INTENSET) ERR Interrupt Enable Position */
#define TC_INTENSET_ERR_Msk                   (0x1U << TC_INTENSET_ERR_Pos)                  /**< (TC_INTENSET) ERR Interrupt Enable Mask */
#define TC_INTENSET_ERR(value)                (TC_INTENSET_ERR_Msk & ((value) << TC_INTENSET_ERR_Pos))
#define TC_INTENSET_MC0_Pos                   (4U)                                           /**< (TC_INTENSET) MC Interrupt Enable 0 Position */
#define TC_INTENSET_MC0_Msk                   (0x1U << TC_INTENSET_MC0_Pos)                  /**< (TC_INTENSET) MC Interrupt Enable 0 Mask */
#define TC_INTENSET_MC0(value)                (TC_INTENSET_MC0_Msk & ((value) << TC_INTENSET_MC0_Pos))
#define TC_INTENSET_MC1_Pos                   (5U)                                           /**< (TC_INTENSET) MC Interrupt Enable 1 Position */
#define TC_INTENSET_MC1_Msk                   (0x1U << TC_INTENSET_MC1_Pos)                  /**< (TC_INTENSET) MC Interrupt Enable 1 Mask */
#define TC_INTENSET_MC1(value)                (TC_INTENSET_MC1_Msk & ((value) << TC_INTENSET_MC1_Pos))
#define TC_INTENSET_Msk                       (0x00000033UL)                                 /**< (TC_INTENSET) Register Mask  */

/* -------- TC_INTFLAG : (TC Offset: 0x0A) (R/W 8) Interrupt Flag Status and Clear -------- */
#define TC_INTFLAG_OVF_Pos                    (0U)                                           /**< (TC_INTFLAG) OVF Interrupt Flag Position */
#define TC_INTFLAG_OVF_Msk                    (0x1U << TC_INTFLAG_OVF_Pos)                   /**< (TC_INTFLAG) OVF Interrupt Flag Mask */
#define TC_INTFLAG_OVF(value)                 (TC_INTFLAG_OVF_Msk & ((value) << TC_INTFLAG_OVF_Pos))
#define TC_INTFLAG_ERR_Pos                    (1U)                                           /**< (TC_INTFLAG) ERR Interrupt Flag Position */
#define TC_INTFLAG_ERR_Msk                    (0x1U << TC_INTFLAG_ERR_Pos)                   /**< (TC_INTFLAG) ERR Interrupt Flag Mask */
#define TC_INTFLAG_ERR(value)                 (TC_INTFLAG_ERR_Msk & ((value) << TC_INTFLAG_ERR_Pos))
#define TC_INTFLAG_MC0_Pos                    (4U)                                           /**< (TC_INTFLAG) MC Interrupt Flag 0 Position */
#define TC_INTFLAG_MC0_Msk                    (0x1U << TC_INTFLAG_MC0_Pos)                   /**< (TC_INTFLAG) MC Interrupt Flag 0 Mask */
#define TC_INTFLAG_MC0(value)                 (TC_INTFLAG_MC0_Msk & ((value) << TC_INTFLAG_MC0_Pos))
#define TC_INTFLAG_MC1_Pos                    (5U)                                           /**< (TC_INTFLAG) MC Interrupt Flag 1 Position */
#define TC_INTFLAG_MC1_Msk                    (0x1U << TC_INTFLAG_MC1_Pos)                   /**< (TC_INTFLAG) MC Interrupt Flag 1 Mask */
#define TC_INTFLAG_MC1(value)                 (TC_INTFLAG_MC1_Msk & ((value) << TC_INTFLAG_MC1_Pos))
#define TC_INTFLAG_Msk                        (0x00000033UL)                                 /**< (TC_INTFLAG) Register Mask  */

/* -------- TC_STATUS : (TC Offset: 0x0B) (R/W 8) Status -------- */
#define TC_STATUS_STOP_Pos                    (0U)                                           /**< (TC_STATUS) Stop Status Flag Position */
#define TC_STATUS_STOP_Msk                    (0x1U << TC_STATUS_STOP_Pos)                   /**< (TC_STATUS) Stop Status Flag Mask */
#define TC_STATUS_STOP(value)                 (TC_STATUS_STOP_Msk & ((value) << TC_STATUS_STOP_Pos))
#define TC_STATUS_SLAVE_Pos                   (1U)                                           /**< (TC_STATUS) Slave Status Flag Position */
#define TC_STATUS_SLAVE_Msk                   (0x1U << TC_STATUS_SLAVE_Pos)                  /**< (TC_STATUS) Slave Status Flag Mask */
#define TC_STATUS_SLAVE(value)                (TC_STATUS_SLAVE_Msk & ((value) << TC_STATUS_SLAVE_Pos))
#define TC_STATUS_PERBUFV_Pos                 (3U)                                           /**< (TC_STATUS) Synchronization Busy Status Position */
#define TC_STATUS_PERBUFV_Msk                 (0x1U << TC_STATUS_PERBUFV_Pos)                /**< (TC_STATUS) Synchronization Busy Status Mask */
#define TC_STATUS_PERBUFV(value)              (TC_STATUS_PERBUFV_Msk & ((value) << TC_STATUS_PERBUFV_Pos))
#define TC_STATUS_CCBUFV0_Pos                 (4U)                                           /**< (TC_STATUS) Compare channel buffer 0 valid Position */
#define TC_STATUS_CCBUFV0_Msk                 (0x1U << TC_STATUS_CCBUFV0_Pos)                /**< (TC_STATUS) Compare channel buffer 0 valid Mask */
#define TC_STATUS_CCBUFV0(value)              (TC_STATUS_CCBUFV0_Msk & ((value) << TC_STATUS_CCBUFV0_Pos))
#define TC_STATUS_CCBUFV1_Pos                 (5U)                                           /**< (TC_STATUS) Compare channel buffer 1 valid Position */
#define TC_STATUS_CCBUFV1_Msk                 (0x1U << TC_STATUS_CCBUFV1_Pos)                /**< (TC_STATUS) Compare channel buffer 1 valid Mask */
#define TC_STATUS_CCBUFV1(value)              (TC_STATUS_CCBUFV1_Msk & ((value) << TC_STATUS_CCBUFV1_Pos))
#define TC_STATUS_Msk                         (0x0000003BUL)                                 /**< (TC_STATUS) Register Mask  */

/* -------- TC_WAVE : (TC Offset: 0x0C) (R/W 8) Waveform Generation Control -------- */
#define TC_WAVE_WAVEGEN_Pos                   (0U)                                           /**< (TC_WAVE) Waveform Generation Mode Position */
#define TC_WAVE_WAVEGEN_Msk                   (0x3U << TC_WAVE_WAVEGEN_Pos)                  /**< (TC_WAVE) Waveform Generation Mode Mask */
#define TC_WAVE_WAVEGEN(value)                (TC_WAVE_WAVEGEN_Msk & ((value) << TC_WAVE_WAVEGEN_Pos))
#define   TC_WAVE_WAVEGEN_NFRQ_Val            (0U)                                           /**< (TC_WAVE) Normal frequency  */
#define   TC_WAVE_WAVEGEN_MFRQ_Val            (1U)                                           /**< (TC_WAVE) Match frequency  */
#define   TC_WAVE_WAVEGEN_NPWM_Val            (2U)                                           /**< (TC_WAVE) Normal PWM  */
#define   TC_WAVE_WAVEGEN_MPWM_Val            (3U)                                           /**< (TC_WAVE) Match PWM  */
#define TC_WAVE_WAVEGEN_NFRQ                  (TC_WAVE_WAVEGEN_NFRQ_Val << TC_WAVE_WAVEGEN_Pos) /**< (TC_WAVE) Normal frequency Position  */
#define TC_WAVE_WAVEGEN_MFRQ                  (TC_WAVE_WAVEGEN_MFRQ_Val << TC_WAVE_WAVEGEN_Pos) /**< (TC_WAVE) Match frequency Position  */
#define TC_WAVE_WAVEGEN_NPWM                  (TC_WAVE_WAVEGEN_NPWM_Val << TC_WAVE_WAVEGEN_Pos) /**< (TC_WAVE) Normal PWM Position  */
#define TC_WAVE_WAVEGEN_MPWM                  (TC_WAVE_WAVEGEN_MPWM_Val << TC_WAVE_WAVEGEN_Pos) /**< (TC_WAVE) Match PWM Position  */
#define TC_WAVE_Msk                           (0x00000003UL)                                 /**< (TC_WAVE) Register Mask  */

/* -------- TC_DRVCTRL : (TC Offset: 0x0D) (R/W 8) Control C -------- */
#define TC_DRVCTRL_INVEN0_Pos                 (0U)                                           /**< (TC_DRVCTRL) Output Waveform Invert Enable 0 Position */
#define TC_DRVCTRL_INVEN0_Msk                 (0x1U << TC_DRVCTRL_INVEN0_Pos)                /**< (TC_DRVCTRL) Output Waveform Invert Enable 0 Mask */
#define TC_DRVCTRL_INVEN0(value)              (TC_DRVCTRL_INVEN0_Msk & ((value) << TC_DRVCTRL_INVEN0_Pos))
#define TC_DRVCTRL_INVEN1_Pos                 (1U)                                           /**< (TC_DRVCTRL) Output Waveform Invert Enable 1 Position */
#define TC_DRVCTRL_INVEN1_Msk                 (0x1U << TC_DRVCTRL_INVEN1_Pos)                /**< (TC_DRVCTRL) Output Waveform Invert Enable 1 Mask */
#define TC_DRVCTRL_INVEN1(value)              (TC_DRVCTRL_INVEN1_Msk & ((value) << TC_DRVCTRL_INVEN1_Pos))
#define TC_DRVCTRL_Msk                        (0x00000003UL)                                 /**< (TC_DRVCTRL) Register Mask  */

/* -------- TC_DBGCTRL : (TC Offset: 0x0F) (R/W 8) Debug Control -------- */
#define TC_DBGCTRL_DBGRUN_Pos                 (0U)                                           /**< (TC_DBGCTRL) Run During Debug Position */
#define TC_DBGCTRL_DBGRUN_Msk                 (0x1U << TC_DBGCTRL_DBGRUN_Pos)                /**< (TC_DBGCTRL) Run During Debug Mask */
#define TC_DBGCTRL_DBGRUN(value)              (TC_DBGCTRL_DBGRUN_Msk & ((value) << TC_DBGCTRL_DBGRUN_Pos))
#define TC_DBGCTRL_Msk                        (0x00000001UL)                                 /**< (TC_DBGCTRL) Register Mask  */

/* -------- TC_SYNCBUSY : (TC Offset: 0x10) (R/  32) Synchronization Status -------- */
#define TC_SYNCBUSY_SWRST_Pos                 (0U)                                           /**< (TC_SYNCBUSY) swrst Position */
#define TC_SYNCBUSY_SWRST_Msk                 (0x1U << TC_SYNCBUSY_SWRST_Pos)                /**< (TC_SYNCBUSY) swrst Mask */
#define TC_SYNCBUSY_SWRST(value)              (TC_SYNCBUSY_SWRST_Msk & ((value) << TC_SYNCBUSY_SWRST_Pos))
#define TC_SYNCBUSY_ENABLE_Pos                (1U)                                           /**< (TC_SYNCBUSY) enable Position */
#define TC_SYNCBUSY_ENABLE_Msk                (0x1U << TC_SYNCBUSY_ENABLE_Pos)               /**< (TC_SYNCBUSY) enable Mask */
#define TC_SYNCBUSY_ENABLE(value)             (TC_SYNCBUSY_ENABLE_Msk & ((value) << TC_SYNCBUSY_ENABLE_Pos))
#define TC_SYNCBUSY_CTRLB_Pos                 (2U)                                           /**< (TC_SYNCBUSY) CTRLB Position */
#define TC_SYNCBUSY_CTRLB_Msk                 (0x1U << TC_SYNCBUSY_CTRLB_Pos)                /**< (TC_SYNCBUSY) CTRLB Mask */
#define TC_SYNCBUSY_CTRLB(value)              (TC_SYNCBUSY_CTRLB_Msk & ((value) << TC_SYNCBUSY_CTRLB_Pos))
#define TC_SYNCBUSY_STATUS_Pos                (3U)                                           /**< (TC_SYNCBUSY) STATUS Position */
#define TC_SYNCBUSY_STATUS_Msk                (0x1U << TC_SYNCBUSY_STATUS_Pos)               /**< (TC_SYNCBUSY) STATUS Mask */
#define TC_SYNCBUSY_STATUS(value)             (TC_SYNCBUSY_STATUS_Msk & ((value) << TC_SYNCBUSY_STATUS_Pos))
#define TC_SYNCBUSY_COUNT_Pos                 (4U)                                           /**< (TC_SYNCBUSY) Counter Position */
#define TC_SYNCBUSY_COUNT_Msk                 (0x1U << TC_SYNCBUSY_COUNT_Pos)                /**< (TC_SYNCBUSY) Counter Mask */
#define TC_SYNCBUSY_COUNT(value)              (TC_SYNCBUSY_COUNT_Msk & ((value) << TC_SYNCBUSY_COUNT_Pos))
#define TC_SYNCBUSY_PER_Pos                   (5U)                                           /**< (TC_SYNCBUSY) Period Position */
#define TC_SYNCBUSY_PER_Msk                   (0x1U << TC_SYNCBUSY_PER_Pos)                  /**< (TC_SYNCBUSY) Period Mask */
#define TC_SYNCBUSY_PER(value)                (TC_SYNCBUSY_PER_Msk & ((value) << TC_SYNCBUSY_PER_Pos))
#define TC_SYNCBUSY_CC0_Pos                   (6U)                                           /**< (TC_SYNCBUSY) Compare Channel 0 Position */
#define TC_SYNCBUSY_CC0_Msk                   (0x1U << TC_SYNCBUSY_CC0_Pos)                  /**< (TC_SYNCBUSY) Compare Channel 0 Mask */
#define TC_SYNCBUSY_CC0(value)                (TC_SYNCBUSY_CC0_Msk & ((value) << TC_SYNCBUSY_CC0_Pos))
#define TC_SYNCBUSY_CC1_Pos                   (7U)                                           /**< (TC_SYNCBUSY) Compare Channel 1 Position */
#define TC_SYNCBUSY_CC1_Msk                   (0x1U << TC_SYNCBUSY_CC1_Pos)                  /**< (TC_SYNCBUSY) Compare Channel 1 Mask */
#define TC_SYNCBUSY_CC1(value)                (TC_SYNCBUSY_CC1_Msk & ((value) << TC_SYNCBUSY_CC1_Pos))
#define TC_SYNCBUSY_Msk                       (0x000000FFUL)                                 /**< (TC_SYNCBUSY) Register Mask  */

/* -------- TC_COUNT : (TC Offset: 0x14) (R/W 8) COUNT8 Count -------- */
#define TC_COUNT_COUNT_Pos                    (0U)                                           /**< (TC_COUNT) Counter Value Position */
#define TC_COUNT_COUNT_Msk                    (0xFFU << TC_COUNT_COUNT_Pos)                  /**< (TC_COUNT) Counter Value Mask */
#define TC_COUNT_COUNT(value)                 (TC_COUNT_COUNT_Msk & ((value) << TC_COUNT_COUNT_Pos))
#define TC_COUNT_Msk                          (0x000000FFUL)                                 /**< (TC_COUNT) Register Mask  */

/* -------- TC_PER : (TC Offset: 0x1B) (R/W 8) COUNT8 Period -------- */
#define TC_PER_PER_Pos                        (0U)                                           /**< (TC_PER) Period Value Position */
#define TC_PER_PER_Msk                        (0xFFU << TC_PER_PER_Pos)                      /**< (TC_PER) Period Value Mask */
#define TC_PER_PER(value)                     (TC_PER_PER_Msk & ((value) << TC_PER_PER_Pos))
#define TC_PER_Msk                            (0x000000FFUL)                                 /**< (TC_PER) Register Mask  */

/* -------- TC_CC : (TC Offset: 0x1C) (R/W 8) COUNT8 Compare and Capture -------- */
#define TC_CC_CC_Pos                          (0U)                                           /**< (TC_CC) Counter/Compare Value Position */
#define TC_CC_CC_Msk                          (0xFFU << TC_CC_CC_Pos)                        /**< (TC_CC) Counter/Compare Value Mask */
#define TC_CC_CC(value)                       (TC_CC_CC_Msk & ((value) << TC_CC_CC_Pos))    
#define TC_CC_Msk                             (0x000000FFUL)                                 /**< (TC_CC) Register Mask  */

/* -------- TC_PERBUF : (TC Offset: 0x2F) (R/W 8) COUNT8 Period Buffer -------- */
#define TC_PERBUF_PERBUF_Pos                  (0U)                                           /**< (TC_PERBUF) Period Buffer Value Position */
#define TC_PERBUF_PERBUF_Msk                  (0xFFU << TC_PERBUF_PERBUF_Pos)                /**< (TC_PERBUF) Period Buffer Value Mask */
#define TC_PERBUF_PERBUF(value)               (TC_PERBUF_PERBUF_Msk & ((value) << TC_PERBUF_PERBUF_Pos))
#define TC_PERBUF_Msk                         (0x000000FFUL)                                 /**< (TC_PERBUF) Register Mask  */

/* -------- TC_CCBUF : (TC Offset: 0x30) (R/W 8) COUNT8 Compare and Capture Buffer -------- */
#define TC_CCBUF_CCBUF_Pos                    (0U)                                           /**< (TC_CCBUF) Counter/Compare Buffer Value Position */
#define TC_CCBUF_CCBUF_Msk                    (0xFFU << TC_CCBUF_CCBUF_Pos)                  /**< (TC_CCBUF) Counter/Compare Buffer Value Mask */
#define TC_CCBUF_CCBUF(value)                 (TC_CCBUF_CCBUF_Msk & ((value) << TC_CCBUF_CCBUF_Pos))
#define TC_CCBUF_Msk                          (0x000000FFUL)                                 /**< (TC_CCBUF) Register Mask  */

/** \brief TC register offsets definitions */
#define TC_CTRLA_OFFSET                (0x00)         /**< (TC_CTRLA) Control A Offset */
#define TC_CTRLBCLR_OFFSET             (0x04)         /**< (TC_CTRLBCLR) Control B Clear Offset */
#define TC_CTRLBSET_OFFSET             (0x05)         /**< (TC_CTRLBSET) Control B Set Offset */
#define TC_EVCTRL_OFFSET               (0x06)         /**< (TC_EVCTRL) Event Control Offset */
#define TC_INTENCLR_OFFSET             (0x08)         /**< (TC_INTENCLR) Interrupt Enable Clear Offset */
#define TC_INTENSET_OFFSET             (0x09)         /**< (TC_INTENSET) Interrupt Enable Set Offset */
#define TC_INTFLAG_OFFSET              (0x0A)         /**< (TC_INTFLAG) Interrupt Flag Status and Clear Offset */
#define TC_STATUS_OFFSET               (0x0B)         /**< (TC_STATUS) Status Offset */
#define TC_WAVE_OFFSET                 (0x0C)         /**< (TC_WAVE) Waveform Generation Control Offset */
#define TC_DRVCTRL_OFFSET              (0x0D)         /**< (TC_DRVCTRL) Control C Offset */
#define TC_DBGCTRL_OFFSET              (0x0F)         /**< (TC_DBGCTRL) Debug Control Offset */
#define TC_SYNCBUSY_OFFSET             (0x10)         /**< (TC_SYNCBUSY) Synchronization Status Offset */
#define TC_COUNT_OFFSET                (0x14)         /**< (TC_COUNT) COUNT8 Count Offset */
#define TC_PER_OFFSET                  (0x1B)         /**< (TC_PER) COUNT8 Period Offset */
#define TC_CC_OFFSET                   (0x1C)         /**< (TC_CC) COUNT8 Compare and Capture Offset */
#define TC_PERBUF_OFFSET               (0x2F)         /**< (TC_PERBUF) COUNT8 Period Buffer Offset */
#define TC_CCBUF_OFFSET                (0x30)         /**< (TC_CCBUF) COUNT8 Compare and Capture Buffer Offset */

/** \brief TC register API structure */
typedef struct
{
  __IO  uint32_t                       TC_CTRLA;        /**< Offset: 0x00 (R/W  32) Control A */
  __IO  uint8_t                        TC_CTRLBCLR;     /**< Offset: 0x04 (R/W  8) Control B Clear */
  __IO  uint8_t                        TC_CTRLBSET;     /**< Offset: 0x05 (R/W  8) Control B Set */
  __IO  uint16_t                       TC_EVCTRL;       /**< Offset: 0x06 (R/W  16) Event Control */
  __IO  uint8_t                        TC_INTENCLR;     /**< Offset: 0x08 (R/W  8) Interrupt Enable Clear */
  __IO  uint8_t                        TC_INTENSET;     /**< Offset: 0x09 (R/W  8) Interrupt Enable Set */
  __IO  uint8_t                        TC_INTFLAG;      /**< Offset: 0x0a (R/W  8) Interrupt Flag Status and Clear */
  __IO  uint8_t                        TC_STATUS;       /**< Offset: 0x0b (R/W  8) Status */
  __IO  uint8_t                        TC_WAVE;         /**< Offset: 0x0c (R/W  8) Waveform Generation Control */
  __IO  uint8_t                        TC_DRVCTRL;      /**< Offset: 0x0d (R/W  8) Control C */
  __I   uint8_t                        Reserved1[0x01];
  __IO  uint8_t                        TC_DBGCTRL;      /**< Offset: 0x0f (R/W  8) Debug Control */
  __I   uint32_t                       TC_SYNCBUSY;     /**< Offset: 0x10 (R/   32) Synchronization Status */
  __IO  uint8_t                        TC_COUNT;        /**< Offset: 0x14 (R/W  8) COUNT8 Count */
  __I   uint8_t                        Reserved2[0x06];
  __IO  uint8_t                        TC_PER;          /**< Offset: 0x1b (R/W  8) COUNT8 Period */
  __IO  uint8_t                        TC_CC[2];        /**< Offset: 0x1c (R/W  8) COUNT8 Compare and Capture */
  __I   uint8_t                        Reserved3[0x11];
  __IO  uint8_t                        TC_PERBUF;       /**< Offset: 0x2f (R/W  8) COUNT8 Period Buffer */
  __IO  uint8_t                        TC_CCBUF[2];     /**< Offset: 0x30 (R/W  8) COUNT8 Compare and Capture Buffer */
} tc_count8_registers_t;

/** \brief TC_COUNT16 hardware registers */
typedef struct { /* 16-bit Counter Mode */
  __IO uint32_t         TC_CTRLA;       /**< \brief Offset: 0x00 (R/W 32) Control A */
  __IO uint8_t          TC_CTRLBCLR;    /**< \brief Offset: 0x04 (R/W  8) Control B Clear */
  __IO uint8_t          TC_CTRLBSET;    /**< \brief Offset: 0x05 (R/W  8) Control B Set */
  __IO uint16_t         TC_EVCTRL;      /**< \brief Offset: 0x06 (R/W 16) Event Control */
  __IO uint8_t          TC_INTENCLR;    /**< \brief Offset: 0x08 (R/W  8) Interrupt Enable Clear */
  __IO uint8_t          TC_INTENSET;    /**< \brief Offset: 0x09 (R/W  8) Interrupt Enable Set */
  __IO uint8_t          TC_INTFLAG;     /**< \brief Offset: 0x0A (R/W  8) Interrupt Flag Status and Clear */
  __IO uint8_t          TC_STATUS;      /**< \brief Offset: 0x0B (R/W  8) Status */
  __IO uint8_t          TC_WAVE;        /**< \brief Offset: 0x0C (R/W  8) Waveform Generation Control */
  __IO uint8_t          TC_DRVCTRL;     /**< \brief Offset: 0x0D (R/W  8) Control C */
  __I  uint8_t          Reserved1[0x1];
  __IO uint8_t          TC_DBGCTRL;     /**< \brief Offset: 0x0F (R/W  8) Debug Control */
  __I  uint32_t         TC_SYNCBUSY;    /**< \brief Offset: 0x10 (R/  32) Synchronization Status */
  __IO uint16_t         TC_COUNT;       /**< \brief Offset: 0x14 (R/W 16) COUNT16 Count */
  __I  uint8_t          Reserved2[0x6];
  __IO uint16_t         TC_CC[2];       /**< \brief Offset: 0x1C (R/W 16) COUNT16 Compare and Capture */
  __I  uint8_t          Reserved3[0x10];
  __IO uint16_t         TC_CCBUF[2];    /**< \brief Offset: 0x30 (R/W 16) COUNT16 Compare and Capture Buffer */
} tc_count16_registers_t;

typedef struct { /* 32-bit Counter Mode */
  __IO uint32_t         TC_CTRLA;       /**< \brief Offset: 0x00 (R/W 32) Control A */
  __IO uint8_t          TC_CTRLBCLR;    /**< \brief Offset: 0x04 (R/W  8) Control B Clear */
  __IO uint8_t          TC_CTRLBSET;    /**< \brief Offset: 0x05 (R/W  8) Control B Set */
  __IO uint16_t         TC_EVCTRL;      /**< \brief Offset: 0x06 (R/W 16) Event Control */
  __IO uint8_t          TC_INTENCLR;    /**< \brief Offset: 0x08 (R/W  8) Interrupt Enable Clear */
  __IO uint8_t          TC_INTENSET;    /**< \brief Offset: 0x09 (R/W  8) Interrupt Enable Set */
  __IO uint8_t          TC_INTFLAG;     /**< \brief Offset: 0x0A (R/W  8) Interrupt Flag Status and Clear */
  __IO uint8_t          TC_STATUS;      /**< \brief Offset: 0x0B (R/W  8) Status */
  __IO uint8_t          TC_WAVE;        /**< \brief Offset: 0x0C (R/W  8) Waveform Generation Control */
  __IO uint8_t          TC_DRVCTRL;     /**< \brief Offset: 0x0D (R/W  8) Control C */
  __I  uint8_t          Reserved1[0x1];
  __IO uint8_t          TC_DBGCTRL;     /**< \brief Offset: 0x0F (R/W  8) Debug Control */
  __I  uint32_t         TC_SYNCBUSY;    /**< \brief Offset: 0x10 (R/  32) Synchronization Status */
  __IO uint32_t         TC_COUNT;       /**< \brief Offset: 0x14 (R/W 32) COUNT32 Count */
  __I  uint8_t          Reserved2[0x4];
  __IO uint32_t         TC_CC[2];       /**< \brief Offset: 0x1C (R/W 32) COUNT32 Compare and Capture */
  __I  uint8_t          Reserved3[0xC];
  __IO uint32_t         TC_CCBUF[2];    /**< \brief Offset: 0x30 (R/W 32) COUNT32 Compare and Capture Buffer */
} tc_count32_registers_t;


typedef union
{
    tc_count8_registers_t    COUNT8;
    tc_count16_registers_t   COUNT16;
    tc_count32_registers_t   COUNT32;
}tc_registers_t;

/** @}  end of Basic Timer Counter */
#endif /* SAMC_SAMC21_TC_MODULE_H */

