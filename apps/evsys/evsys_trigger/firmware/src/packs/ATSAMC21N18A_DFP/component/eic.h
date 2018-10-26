/**
 * \brief Header file for SAMC/SAMC21 EIC
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
#ifndef SAMC_SAMC21_EIC_MODULE_H
#define SAMC_SAMC21_EIC_MODULE_H

/** \addtogroup SAMC_SAMC21 External Interrupt Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_EIC                                   */
/* ========================================================================== */

/* -------- EIC_CTRLA : (EIC Offset: 0x00) (R/W 8) Control A -------- */
#define EIC_CTRLA_SWRST_Pos                   (0U)                                           /**< (EIC_CTRLA) Software Reset Position */
#define EIC_CTRLA_SWRST_Msk                   (0x1U << EIC_CTRLA_SWRST_Pos)                  /**< (EIC_CTRLA) Software Reset Mask */
#define EIC_CTRLA_SWRST(value)                (EIC_CTRLA_SWRST_Msk & ((value) << EIC_CTRLA_SWRST_Pos))
#define EIC_CTRLA_ENABLE_Pos                  (1U)                                           /**< (EIC_CTRLA) Enable Position */
#define EIC_CTRLA_ENABLE_Msk                  (0x1U << EIC_CTRLA_ENABLE_Pos)                 /**< (EIC_CTRLA) Enable Mask */
#define EIC_CTRLA_ENABLE(value)               (EIC_CTRLA_ENABLE_Msk & ((value) << EIC_CTRLA_ENABLE_Pos))
#define EIC_CTRLA_CKSEL_Pos                   (4U)                                           /**< (EIC_CTRLA) Clock Selection Position */
#define EIC_CTRLA_CKSEL_Msk                   (0x1U << EIC_CTRLA_CKSEL_Pos)                  /**< (EIC_CTRLA) Clock Selection Mask */
#define EIC_CTRLA_CKSEL(value)                (EIC_CTRLA_CKSEL_Msk & ((value) << EIC_CTRLA_CKSEL_Pos))
#define   EIC_CTRLA_CKSEL_CLK_GCLK_Val        (0U)                                           /**< (EIC_CTRLA) Clocked by GCLK  */
#define   EIC_CTRLA_CKSEL_CLK_ULP32K_Val      (1U)                                           /**< (EIC_CTRLA) Clocked by ULP32K  */
#define EIC_CTRLA_CKSEL_CLK_GCLK              (EIC_CTRLA_CKSEL_CLK_GCLK_Val << EIC_CTRLA_CKSEL_Pos) /**< (EIC_CTRLA) Clocked by GCLK Position  */
#define EIC_CTRLA_CKSEL_CLK_ULP32K            (EIC_CTRLA_CKSEL_CLK_ULP32K_Val << EIC_CTRLA_CKSEL_Pos) /**< (EIC_CTRLA) Clocked by ULP32K Position  */
#define EIC_CTRLA_Msk                         (0x00000013UL)                                 /**< (EIC_CTRLA) Register Mask  */

/* -------- EIC_NMICTRL : (EIC Offset: 0x01) (R/W 8) Non-Maskable Interrupt Control -------- */
#define EIC_NMICTRL_NMISENSE_Pos              (0U)                                           /**< (EIC_NMICTRL) Non-Maskable Interrupt Sense Configuration Position */
#define EIC_NMICTRL_NMISENSE_Msk              (0x7U << EIC_NMICTRL_NMISENSE_Pos)             /**< (EIC_NMICTRL) Non-Maskable Interrupt Sense Configuration Mask */
#define EIC_NMICTRL_NMISENSE(value)           (EIC_NMICTRL_NMISENSE_Msk & ((value) << EIC_NMICTRL_NMISENSE_Pos))
#define   EIC_NMICTRL_NMISENSE_NONE_Val       (0U)                                           /**< (EIC_NMICTRL) No detection  */
#define   EIC_NMICTRL_NMISENSE_RISE_Val       (1U)                                           /**< (EIC_NMICTRL) Rising-edge detection  */
#define   EIC_NMICTRL_NMISENSE_FALL_Val       (2U)                                           /**< (EIC_NMICTRL) Falling-edge detection  */
#define   EIC_NMICTRL_NMISENSE_BOTH_Val       (3U)                                           /**< (EIC_NMICTRL) Both-edges detection  */
#define   EIC_NMICTRL_NMISENSE_HIGH_Val       (4U)                                           /**< (EIC_NMICTRL) High-level detection  */
#define   EIC_NMICTRL_NMISENSE_LOW_Val        (5U)                                           /**< (EIC_NMICTRL) Low-level detection  */
#define EIC_NMICTRL_NMISENSE_NONE             (EIC_NMICTRL_NMISENSE_NONE_Val << EIC_NMICTRL_NMISENSE_Pos) /**< (EIC_NMICTRL) No detection Position  */
#define EIC_NMICTRL_NMISENSE_RISE             (EIC_NMICTRL_NMISENSE_RISE_Val << EIC_NMICTRL_NMISENSE_Pos) /**< (EIC_NMICTRL) Rising-edge detection Position  */
#define EIC_NMICTRL_NMISENSE_FALL             (EIC_NMICTRL_NMISENSE_FALL_Val << EIC_NMICTRL_NMISENSE_Pos) /**< (EIC_NMICTRL) Falling-edge detection Position  */
#define EIC_NMICTRL_NMISENSE_BOTH             (EIC_NMICTRL_NMISENSE_BOTH_Val << EIC_NMICTRL_NMISENSE_Pos) /**< (EIC_NMICTRL) Both-edges detection Position  */
#define EIC_NMICTRL_NMISENSE_HIGH             (EIC_NMICTRL_NMISENSE_HIGH_Val << EIC_NMICTRL_NMISENSE_Pos) /**< (EIC_NMICTRL) High-level detection Position  */
#define EIC_NMICTRL_NMISENSE_LOW              (EIC_NMICTRL_NMISENSE_LOW_Val << EIC_NMICTRL_NMISENSE_Pos) /**< (EIC_NMICTRL) Low-level detection Position  */
#define EIC_NMICTRL_NMIFILTEN_Pos             (3U)                                           /**< (EIC_NMICTRL) Non-Maskable Interrupt Filter Enable Position */
#define EIC_NMICTRL_NMIFILTEN_Msk             (0x1U << EIC_NMICTRL_NMIFILTEN_Pos)            /**< (EIC_NMICTRL) Non-Maskable Interrupt Filter Enable Mask */
#define EIC_NMICTRL_NMIFILTEN(value)          (EIC_NMICTRL_NMIFILTEN_Msk & ((value) << EIC_NMICTRL_NMIFILTEN_Pos))
#define EIC_NMICTRL_NMIASYNCH_Pos             (4U)                                           /**< (EIC_NMICTRL) Asynchronous Edge Detection Mode Position */
#define EIC_NMICTRL_NMIASYNCH_Msk             (0x1U << EIC_NMICTRL_NMIASYNCH_Pos)            /**< (EIC_NMICTRL) Asynchronous Edge Detection Mode Mask */
#define EIC_NMICTRL_NMIASYNCH(value)          (EIC_NMICTRL_NMIASYNCH_Msk & ((value) << EIC_NMICTRL_NMIASYNCH_Pos))
#define   EIC_NMICTRL_NMIASYNCH_SYNC_Val      (0U)                                           /**< (EIC_NMICTRL) Edge detection is clock synchronously operated  */
#define   EIC_NMICTRL_NMIASYNCH_ASYNC_Val     (1U)                                           /**< (EIC_NMICTRL) Edge detection is clock asynchronously operated  */
#define EIC_NMICTRL_NMIASYNCH_SYNC            (EIC_NMICTRL_NMIASYNCH_SYNC_Val << EIC_NMICTRL_NMIASYNCH_Pos) /**< (EIC_NMICTRL) Edge detection is clock synchronously operated Position  */
#define EIC_NMICTRL_NMIASYNCH_ASYNC           (EIC_NMICTRL_NMIASYNCH_ASYNC_Val << EIC_NMICTRL_NMIASYNCH_Pos) /**< (EIC_NMICTRL) Edge detection is clock asynchronously operated Position  */
#define EIC_NMICTRL_Msk                       (0x0000001FUL)                                 /**< (EIC_NMICTRL) Register Mask  */

/* -------- EIC_NMIFLAG : (EIC Offset: 0x02) (R/W 16) Non-Maskable Interrupt Flag Status and Clear -------- */
#define EIC_NMIFLAG_NMI_Pos                   (0U)                                           /**< (EIC_NMIFLAG) Non-Maskable Interrupt Position */
#define EIC_NMIFLAG_NMI_Msk                   (0x1U << EIC_NMIFLAG_NMI_Pos)                  /**< (EIC_NMIFLAG) Non-Maskable Interrupt Mask */
#define EIC_NMIFLAG_NMI(value)                (EIC_NMIFLAG_NMI_Msk & ((value) << EIC_NMIFLAG_NMI_Pos))
#define EIC_NMIFLAG_Msk                       (0x00000001UL)                                 /**< (EIC_NMIFLAG) Register Mask  */

/* -------- EIC_SYNCBUSY : (EIC Offset: 0x04) (R/  32) Synchronization Busy -------- */
#define EIC_SYNCBUSY_SWRST_Pos                (0U)                                           /**< (EIC_SYNCBUSY) Software Reset Synchronization Busy Status Position */
#define EIC_SYNCBUSY_SWRST_Msk                (0x1U << EIC_SYNCBUSY_SWRST_Pos)               /**< (EIC_SYNCBUSY) Software Reset Synchronization Busy Status Mask */
#define EIC_SYNCBUSY_SWRST(value)             (EIC_SYNCBUSY_SWRST_Msk & ((value) << EIC_SYNCBUSY_SWRST_Pos))
#define EIC_SYNCBUSY_ENABLE_Pos               (1U)                                           /**< (EIC_SYNCBUSY) Enable Synchronization Busy Status Position */
#define EIC_SYNCBUSY_ENABLE_Msk               (0x1U << EIC_SYNCBUSY_ENABLE_Pos)              /**< (EIC_SYNCBUSY) Enable Synchronization Busy Status Mask */
#define EIC_SYNCBUSY_ENABLE(value)            (EIC_SYNCBUSY_ENABLE_Msk & ((value) << EIC_SYNCBUSY_ENABLE_Pos))
#define EIC_SYNCBUSY_Msk                      (0x00000003UL)                                 /**< (EIC_SYNCBUSY) Register Mask  */

/* -------- EIC_EVCTRL : (EIC Offset: 0x08) (R/W 32) Event Control -------- */
#define EIC_EVCTRL_EXTINTEO_Pos               (0U)                                           /**< (EIC_EVCTRL) External Interrupt Event Output Enable Position */
#define EIC_EVCTRL_EXTINTEO_Msk               (0xFFFFU << EIC_EVCTRL_EXTINTEO_Pos)           /**< (EIC_EVCTRL) External Interrupt Event Output Enable Mask */
#define EIC_EVCTRL_EXTINTEO(value)            (EIC_EVCTRL_EXTINTEO_Msk & ((value) << EIC_EVCTRL_EXTINTEO_Pos))
#define EIC_EVCTRL_Msk                        (0x0000FFFFUL)                                 /**< (EIC_EVCTRL) Register Mask  */

/* -------- EIC_INTENCLR : (EIC Offset: 0x0C) (R/W 32) Interrupt Enable Clear -------- */
#define EIC_INTENCLR_EXTINT_Pos               (0U)                                           /**< (EIC_INTENCLR) External Interrupt Enable Position */
#define EIC_INTENCLR_EXTINT_Msk               (0xFFFFU << EIC_INTENCLR_EXTINT_Pos)           /**< (EIC_INTENCLR) External Interrupt Enable Mask */
#define EIC_INTENCLR_EXTINT(value)            (EIC_INTENCLR_EXTINT_Msk & ((value) << EIC_INTENCLR_EXTINT_Pos))
#define EIC_INTENCLR_Msk                      (0x0000FFFFUL)                                 /**< (EIC_INTENCLR) Register Mask  */

/* -------- EIC_INTENSET : (EIC Offset: 0x10) (R/W 32) Interrupt Enable Set -------- */
#define EIC_INTENSET_EXTINT_Pos               (0U)                                           /**< (EIC_INTENSET) External Interrupt Enable Position */
#define EIC_INTENSET_EXTINT_Msk               (0xFFFFU << EIC_INTENSET_EXTINT_Pos)           /**< (EIC_INTENSET) External Interrupt Enable Mask */
#define EIC_INTENSET_EXTINT(value)            (EIC_INTENSET_EXTINT_Msk & ((value) << EIC_INTENSET_EXTINT_Pos))
#define EIC_INTENSET_Msk                      (0x0000FFFFUL)                                 /**< (EIC_INTENSET) Register Mask  */

/* -------- EIC_INTFLAG : (EIC Offset: 0x14) (R/W 32) Interrupt Flag Status and Clear -------- */
#define EIC_INTFLAG_EXTINT_Pos                (0U)                                           /**< (EIC_INTFLAG) External Interrupt Position */
#define EIC_INTFLAG_EXTINT_Msk                (0xFFFFU << EIC_INTFLAG_EXTINT_Pos)            /**< (EIC_INTFLAG) External Interrupt Mask */
#define EIC_INTFLAG_EXTINT(value)             (EIC_INTFLAG_EXTINT_Msk & ((value) << EIC_INTFLAG_EXTINT_Pos))
#define EIC_INTFLAG_Msk                       (0x0000FFFFUL)                                 /**< (EIC_INTFLAG) Register Mask  */

/* -------- EIC_ASYNCH : (EIC Offset: 0x18) (R/W 32) External Interrupt Asynchronous Mode -------- */
#define EIC_ASYNCH_ASYNCH_Pos                 (0U)                                           /**< (EIC_ASYNCH) Asynchronous Edge Detection Mode Position */
#define EIC_ASYNCH_ASYNCH_Msk                 (0xFFFFU << EIC_ASYNCH_ASYNCH_Pos)             /**< (EIC_ASYNCH) Asynchronous Edge Detection Mode Mask */
#define EIC_ASYNCH_ASYNCH(value)              (EIC_ASYNCH_ASYNCH_Msk & ((value) << EIC_ASYNCH_ASYNCH_Pos))
#define   EIC_ASYNCH_ASYNCH_SYNC_Val          (0U)                                           /**< (EIC_ASYNCH) Edge detection is clock synchronously operated  */
#define   EIC_ASYNCH_ASYNCH_ASYNC_Val         (1U)                                           /**< (EIC_ASYNCH) Edge detection is clock asynchronously operated  */
#define EIC_ASYNCH_ASYNCH_SYNC                (EIC_ASYNCH_ASYNCH_SYNC_Val << EIC_ASYNCH_ASYNCH_Pos) /**< (EIC_ASYNCH) Edge detection is clock synchronously operated Position  */
#define EIC_ASYNCH_ASYNCH_ASYNC               (EIC_ASYNCH_ASYNCH_ASYNC_Val << EIC_ASYNCH_ASYNCH_Pos) /**< (EIC_ASYNCH) Edge detection is clock asynchronously operated Position  */
#define EIC_ASYNCH_Msk                        (0x0000FFFFUL)                                 /**< (EIC_ASYNCH) Register Mask  */

/* -------- EIC_CONFIG : (EIC Offset: 0x1C) (R/W 32) External Interrupt Sense Configuration -------- */
#define EIC_CONFIG_SENSE0_Pos                 (0U)                                           /**< (EIC_CONFIG) Input Sense Configuration 0 Position */
#define EIC_CONFIG_SENSE0_Msk                 (0x7U << EIC_CONFIG_SENSE0_Pos)                /**< (EIC_CONFIG) Input Sense Configuration 0 Mask */
#define EIC_CONFIG_SENSE0(value)              (EIC_CONFIG_SENSE0_Msk & ((value) << EIC_CONFIG_SENSE0_Pos))
#define   EIC_CONFIG_SENSE0_NONE_Val          (0U)                                           /**< (EIC_CONFIG) No detection  */
#define   EIC_CONFIG_SENSE0_RISE_Val          (1U)                                           /**< (EIC_CONFIG) Rising edge detection  */
#define   EIC_CONFIG_SENSE0_FALL_Val          (2U)                                           /**< (EIC_CONFIG) Falling edge detection  */
#define   EIC_CONFIG_SENSE0_BOTH_Val          (3U)                                           /**< (EIC_CONFIG) Both edges detection  */
#define   EIC_CONFIG_SENSE0_HIGH_Val          (4U)                                           /**< (EIC_CONFIG) High level detection  */
#define   EIC_CONFIG_SENSE0_LOW_Val           (5U)                                           /**< (EIC_CONFIG) Low level detection  */
#define EIC_CONFIG_SENSE0_NONE                (EIC_CONFIG_SENSE0_NONE_Val << EIC_CONFIG_SENSE0_Pos) /**< (EIC_CONFIG) No detection Position  */
#define EIC_CONFIG_SENSE0_RISE                (EIC_CONFIG_SENSE0_RISE_Val << EIC_CONFIG_SENSE0_Pos) /**< (EIC_CONFIG) Rising edge detection Position  */
#define EIC_CONFIG_SENSE0_FALL                (EIC_CONFIG_SENSE0_FALL_Val << EIC_CONFIG_SENSE0_Pos) /**< (EIC_CONFIG) Falling edge detection Position  */
#define EIC_CONFIG_SENSE0_BOTH                (EIC_CONFIG_SENSE0_BOTH_Val << EIC_CONFIG_SENSE0_Pos) /**< (EIC_CONFIG) Both edges detection Position  */
#define EIC_CONFIG_SENSE0_HIGH                (EIC_CONFIG_SENSE0_HIGH_Val << EIC_CONFIG_SENSE0_Pos) /**< (EIC_CONFIG) High level detection Position  */
#define EIC_CONFIG_SENSE0_LOW                 (EIC_CONFIG_SENSE0_LOW_Val << EIC_CONFIG_SENSE0_Pos) /**< (EIC_CONFIG) Low level detection Position  */
#define EIC_CONFIG_FILTEN0_Pos                (3U)                                           /**< (EIC_CONFIG) Filter Enable 0 Position */
#define EIC_CONFIG_FILTEN0_Msk                (0x1U << EIC_CONFIG_FILTEN0_Pos)               /**< (EIC_CONFIG) Filter Enable 0 Mask */
#define EIC_CONFIG_FILTEN0(value)             (EIC_CONFIG_FILTEN0_Msk & ((value) << EIC_CONFIG_FILTEN0_Pos))
#define EIC_CONFIG_SENSE1_Pos                 (4U)                                           /**< (EIC_CONFIG) Input Sense Configuration 1 Position */
#define EIC_CONFIG_SENSE1_Msk                 (0x7U << EIC_CONFIG_SENSE1_Pos)                /**< (EIC_CONFIG) Input Sense Configuration 1 Mask */
#define EIC_CONFIG_SENSE1(value)              (EIC_CONFIG_SENSE1_Msk & ((value) << EIC_CONFIG_SENSE1_Pos))
#define   EIC_CONFIG_SENSE1_NONE_Val          (0U)                                           /**< (EIC_CONFIG) No detection  */
#define   EIC_CONFIG_SENSE1_RISE_Val          (1U)                                           /**< (EIC_CONFIG) Rising edge detection  */
#define   EIC_CONFIG_SENSE1_FALL_Val          (2U)                                           /**< (EIC_CONFIG) Falling edge detection  */
#define   EIC_CONFIG_SENSE1_BOTH_Val          (3U)                                           /**< (EIC_CONFIG) Both edges detection  */
#define   EIC_CONFIG_SENSE1_HIGH_Val          (4U)                                           /**< (EIC_CONFIG) High level detection  */
#define   EIC_CONFIG_SENSE1_LOW_Val           (5U)                                           /**< (EIC_CONFIG) Low level detection  */
#define EIC_CONFIG_SENSE1_NONE                (EIC_CONFIG_SENSE1_NONE_Val << EIC_CONFIG_SENSE1_Pos) /**< (EIC_CONFIG) No detection Position  */
#define EIC_CONFIG_SENSE1_RISE                (EIC_CONFIG_SENSE1_RISE_Val << EIC_CONFIG_SENSE1_Pos) /**< (EIC_CONFIG) Rising edge detection Position  */
#define EIC_CONFIG_SENSE1_FALL                (EIC_CONFIG_SENSE1_FALL_Val << EIC_CONFIG_SENSE1_Pos) /**< (EIC_CONFIG) Falling edge detection Position  */
#define EIC_CONFIG_SENSE1_BOTH                (EIC_CONFIG_SENSE1_BOTH_Val << EIC_CONFIG_SENSE1_Pos) /**< (EIC_CONFIG) Both edges detection Position  */
#define EIC_CONFIG_SENSE1_HIGH                (EIC_CONFIG_SENSE1_HIGH_Val << EIC_CONFIG_SENSE1_Pos) /**< (EIC_CONFIG) High level detection Position  */
#define EIC_CONFIG_SENSE1_LOW                 (EIC_CONFIG_SENSE1_LOW_Val << EIC_CONFIG_SENSE1_Pos) /**< (EIC_CONFIG) Low level detection Position  */
#define EIC_CONFIG_FILTEN1_Pos                (7U)                                           /**< (EIC_CONFIG) Filter Enable 1 Position */
#define EIC_CONFIG_FILTEN1_Msk                (0x1U << EIC_CONFIG_FILTEN1_Pos)               /**< (EIC_CONFIG) Filter Enable 1 Mask */
#define EIC_CONFIG_FILTEN1(value)             (EIC_CONFIG_FILTEN1_Msk & ((value) << EIC_CONFIG_FILTEN1_Pos))
#define EIC_CONFIG_SENSE2_Pos                 (8U)                                           /**< (EIC_CONFIG) Input Sense Configuration 2 Position */
#define EIC_CONFIG_SENSE2_Msk                 (0x7U << EIC_CONFIG_SENSE2_Pos)                /**< (EIC_CONFIG) Input Sense Configuration 2 Mask */
#define EIC_CONFIG_SENSE2(value)              (EIC_CONFIG_SENSE2_Msk & ((value) << EIC_CONFIG_SENSE2_Pos))
#define   EIC_CONFIG_SENSE2_NONE_Val          (0U)                                           /**< (EIC_CONFIG) No detection  */
#define   EIC_CONFIG_SENSE2_RISE_Val          (1U)                                           /**< (EIC_CONFIG) Rising edge detection  */
#define   EIC_CONFIG_SENSE2_FALL_Val          (2U)                                           /**< (EIC_CONFIG) Falling edge detection  */
#define   EIC_CONFIG_SENSE2_BOTH_Val          (3U)                                           /**< (EIC_CONFIG) Both edges detection  */
#define   EIC_CONFIG_SENSE2_HIGH_Val          (4U)                                           /**< (EIC_CONFIG) High level detection  */
#define   EIC_CONFIG_SENSE2_LOW_Val           (5U)                                           /**< (EIC_CONFIG) Low level detection  */
#define EIC_CONFIG_SENSE2_NONE                (EIC_CONFIG_SENSE2_NONE_Val << EIC_CONFIG_SENSE2_Pos) /**< (EIC_CONFIG) No detection Position  */
#define EIC_CONFIG_SENSE2_RISE                (EIC_CONFIG_SENSE2_RISE_Val << EIC_CONFIG_SENSE2_Pos) /**< (EIC_CONFIG) Rising edge detection Position  */
#define EIC_CONFIG_SENSE2_FALL                (EIC_CONFIG_SENSE2_FALL_Val << EIC_CONFIG_SENSE2_Pos) /**< (EIC_CONFIG) Falling edge detection Position  */
#define EIC_CONFIG_SENSE2_BOTH                (EIC_CONFIG_SENSE2_BOTH_Val << EIC_CONFIG_SENSE2_Pos) /**< (EIC_CONFIG) Both edges detection Position  */
#define EIC_CONFIG_SENSE2_HIGH                (EIC_CONFIG_SENSE2_HIGH_Val << EIC_CONFIG_SENSE2_Pos) /**< (EIC_CONFIG) High level detection Position  */
#define EIC_CONFIG_SENSE2_LOW                 (EIC_CONFIG_SENSE2_LOW_Val << EIC_CONFIG_SENSE2_Pos) /**< (EIC_CONFIG) Low level detection Position  */
#define EIC_CONFIG_FILTEN2_Pos                (11U)                                          /**< (EIC_CONFIG) Filter Enable 2 Position */
#define EIC_CONFIG_FILTEN2_Msk                (0x1U << EIC_CONFIG_FILTEN2_Pos)               /**< (EIC_CONFIG) Filter Enable 2 Mask */
#define EIC_CONFIG_FILTEN2(value)             (EIC_CONFIG_FILTEN2_Msk & ((value) << EIC_CONFIG_FILTEN2_Pos))
#define EIC_CONFIG_SENSE3_Pos                 (12U)                                          /**< (EIC_CONFIG) Input Sense Configuration 3 Position */
#define EIC_CONFIG_SENSE3_Msk                 (0x7U << EIC_CONFIG_SENSE3_Pos)                /**< (EIC_CONFIG) Input Sense Configuration 3 Mask */
#define EIC_CONFIG_SENSE3(value)              (EIC_CONFIG_SENSE3_Msk & ((value) << EIC_CONFIG_SENSE3_Pos))
#define   EIC_CONFIG_SENSE3_NONE_Val          (0U)                                           /**< (EIC_CONFIG) No detection  */
#define   EIC_CONFIG_SENSE3_RISE_Val          (1U)                                           /**< (EIC_CONFIG) Rising edge detection  */
#define   EIC_CONFIG_SENSE3_FALL_Val          (2U)                                           /**< (EIC_CONFIG) Falling edge detection  */
#define   EIC_CONFIG_SENSE3_BOTH_Val          (3U)                                           /**< (EIC_CONFIG) Both edges detection  */
#define   EIC_CONFIG_SENSE3_HIGH_Val          (4U)                                           /**< (EIC_CONFIG) High level detection  */
#define   EIC_CONFIG_SENSE3_LOW_Val           (5U)                                           /**< (EIC_CONFIG) Low level detection  */
#define EIC_CONFIG_SENSE3_NONE                (EIC_CONFIG_SENSE3_NONE_Val << EIC_CONFIG_SENSE3_Pos) /**< (EIC_CONFIG) No detection Position  */
#define EIC_CONFIG_SENSE3_RISE                (EIC_CONFIG_SENSE3_RISE_Val << EIC_CONFIG_SENSE3_Pos) /**< (EIC_CONFIG) Rising edge detection Position  */
#define EIC_CONFIG_SENSE3_FALL                (EIC_CONFIG_SENSE3_FALL_Val << EIC_CONFIG_SENSE3_Pos) /**< (EIC_CONFIG) Falling edge detection Position  */
#define EIC_CONFIG_SENSE3_BOTH                (EIC_CONFIG_SENSE3_BOTH_Val << EIC_CONFIG_SENSE3_Pos) /**< (EIC_CONFIG) Both edges detection Position  */
#define EIC_CONFIG_SENSE3_HIGH                (EIC_CONFIG_SENSE3_HIGH_Val << EIC_CONFIG_SENSE3_Pos) /**< (EIC_CONFIG) High level detection Position  */
#define EIC_CONFIG_SENSE3_LOW                 (EIC_CONFIG_SENSE3_LOW_Val << EIC_CONFIG_SENSE3_Pos) /**< (EIC_CONFIG) Low level detection Position  */
#define EIC_CONFIG_FILTEN3_Pos                (15U)                                          /**< (EIC_CONFIG) Filter Enable 3 Position */
#define EIC_CONFIG_FILTEN3_Msk                (0x1U << EIC_CONFIG_FILTEN3_Pos)               /**< (EIC_CONFIG) Filter Enable 3 Mask */
#define EIC_CONFIG_FILTEN3(value)             (EIC_CONFIG_FILTEN3_Msk & ((value) << EIC_CONFIG_FILTEN3_Pos))
#define EIC_CONFIG_SENSE4_Pos                 (16U)                                          /**< (EIC_CONFIG) Input Sense Configuration 4 Position */
#define EIC_CONFIG_SENSE4_Msk                 (0x7U << EIC_CONFIG_SENSE4_Pos)                /**< (EIC_CONFIG) Input Sense Configuration 4 Mask */
#define EIC_CONFIG_SENSE4(value)              (EIC_CONFIG_SENSE4_Msk & ((value) << EIC_CONFIG_SENSE4_Pos))
#define   EIC_CONFIG_SENSE4_NONE_Val          (0U)                                           /**< (EIC_CONFIG) No detection  */
#define   EIC_CONFIG_SENSE4_RISE_Val          (1U)                                           /**< (EIC_CONFIG) Rising edge detection  */
#define   EIC_CONFIG_SENSE4_FALL_Val          (2U)                                           /**< (EIC_CONFIG) Falling edge detection  */
#define   EIC_CONFIG_SENSE4_BOTH_Val          (3U)                                           /**< (EIC_CONFIG) Both edges detection  */
#define   EIC_CONFIG_SENSE4_HIGH_Val          (4U)                                           /**< (EIC_CONFIG) High level detection  */
#define   EIC_CONFIG_SENSE4_LOW_Val           (5U)                                           /**< (EIC_CONFIG) Low level detection  */
#define EIC_CONFIG_SENSE4_NONE                (EIC_CONFIG_SENSE4_NONE_Val << EIC_CONFIG_SENSE4_Pos) /**< (EIC_CONFIG) No detection Position  */
#define EIC_CONFIG_SENSE4_RISE                (EIC_CONFIG_SENSE4_RISE_Val << EIC_CONFIG_SENSE4_Pos) /**< (EIC_CONFIG) Rising edge detection Position  */
#define EIC_CONFIG_SENSE4_FALL                (EIC_CONFIG_SENSE4_FALL_Val << EIC_CONFIG_SENSE4_Pos) /**< (EIC_CONFIG) Falling edge detection Position  */
#define EIC_CONFIG_SENSE4_BOTH                (EIC_CONFIG_SENSE4_BOTH_Val << EIC_CONFIG_SENSE4_Pos) /**< (EIC_CONFIG) Both edges detection Position  */
#define EIC_CONFIG_SENSE4_HIGH                (EIC_CONFIG_SENSE4_HIGH_Val << EIC_CONFIG_SENSE4_Pos) /**< (EIC_CONFIG) High level detection Position  */
#define EIC_CONFIG_SENSE4_LOW                 (EIC_CONFIG_SENSE4_LOW_Val << EIC_CONFIG_SENSE4_Pos) /**< (EIC_CONFIG) Low level detection Position  */
#define EIC_CONFIG_FILTEN4_Pos                (19U)                                          /**< (EIC_CONFIG) Filter Enable 4 Position */
#define EIC_CONFIG_FILTEN4_Msk                (0x1U << EIC_CONFIG_FILTEN4_Pos)               /**< (EIC_CONFIG) Filter Enable 4 Mask */
#define EIC_CONFIG_FILTEN4(value)             (EIC_CONFIG_FILTEN4_Msk & ((value) << EIC_CONFIG_FILTEN4_Pos))
#define EIC_CONFIG_SENSE5_Pos                 (20U)                                          /**< (EIC_CONFIG) Input Sense Configuration 5 Position */
#define EIC_CONFIG_SENSE5_Msk                 (0x7U << EIC_CONFIG_SENSE5_Pos)                /**< (EIC_CONFIG) Input Sense Configuration 5 Mask */
#define EIC_CONFIG_SENSE5(value)              (EIC_CONFIG_SENSE5_Msk & ((value) << EIC_CONFIG_SENSE5_Pos))
#define   EIC_CONFIG_SENSE5_NONE_Val          (0U)                                           /**< (EIC_CONFIG) No detection  */
#define   EIC_CONFIG_SENSE5_RISE_Val          (1U)                                           /**< (EIC_CONFIG) Rising edge detection  */
#define   EIC_CONFIG_SENSE5_FALL_Val          (2U)                                           /**< (EIC_CONFIG) Falling edge detection  */
#define   EIC_CONFIG_SENSE5_BOTH_Val          (3U)                                           /**< (EIC_CONFIG) Both edges detection  */
#define   EIC_CONFIG_SENSE5_HIGH_Val          (4U)                                           /**< (EIC_CONFIG) High level detection  */
#define   EIC_CONFIG_SENSE5_LOW_Val           (5U)                                           /**< (EIC_CONFIG) Low level detection  */
#define EIC_CONFIG_SENSE5_NONE                (EIC_CONFIG_SENSE5_NONE_Val << EIC_CONFIG_SENSE5_Pos) /**< (EIC_CONFIG) No detection Position  */
#define EIC_CONFIG_SENSE5_RISE                (EIC_CONFIG_SENSE5_RISE_Val << EIC_CONFIG_SENSE5_Pos) /**< (EIC_CONFIG) Rising edge detection Position  */
#define EIC_CONFIG_SENSE5_FALL                (EIC_CONFIG_SENSE5_FALL_Val << EIC_CONFIG_SENSE5_Pos) /**< (EIC_CONFIG) Falling edge detection Position  */
#define EIC_CONFIG_SENSE5_BOTH                (EIC_CONFIG_SENSE5_BOTH_Val << EIC_CONFIG_SENSE5_Pos) /**< (EIC_CONFIG) Both edges detection Position  */
#define EIC_CONFIG_SENSE5_HIGH                (EIC_CONFIG_SENSE5_HIGH_Val << EIC_CONFIG_SENSE5_Pos) /**< (EIC_CONFIG) High level detection Position  */
#define EIC_CONFIG_SENSE5_LOW                 (EIC_CONFIG_SENSE5_LOW_Val << EIC_CONFIG_SENSE5_Pos) /**< (EIC_CONFIG) Low level detection Position  */
#define EIC_CONFIG_FILTEN5_Pos                (23U)                                          /**< (EIC_CONFIG) Filter Enable 5 Position */
#define EIC_CONFIG_FILTEN5_Msk                (0x1U << EIC_CONFIG_FILTEN5_Pos)               /**< (EIC_CONFIG) Filter Enable 5 Mask */
#define EIC_CONFIG_FILTEN5(value)             (EIC_CONFIG_FILTEN5_Msk & ((value) << EIC_CONFIG_FILTEN5_Pos))
#define EIC_CONFIG_SENSE6_Pos                 (24U)                                          /**< (EIC_CONFIG) Input Sense Configuration 6 Position */
#define EIC_CONFIG_SENSE6_Msk                 (0x7U << EIC_CONFIG_SENSE6_Pos)                /**< (EIC_CONFIG) Input Sense Configuration 6 Mask */
#define EIC_CONFIG_SENSE6(value)              (EIC_CONFIG_SENSE6_Msk & ((value) << EIC_CONFIG_SENSE6_Pos))
#define   EIC_CONFIG_SENSE6_NONE_Val          (0U)                                           /**< (EIC_CONFIG) No detection  */
#define   EIC_CONFIG_SENSE6_RISE_Val          (1U)                                           /**< (EIC_CONFIG) Rising edge detection  */
#define   EIC_CONFIG_SENSE6_FALL_Val          (2U)                                           /**< (EIC_CONFIG) Falling edge detection  */
#define   EIC_CONFIG_SENSE6_BOTH_Val          (3U)                                           /**< (EIC_CONFIG) Both edges detection  */
#define   EIC_CONFIG_SENSE6_HIGH_Val          (4U)                                           /**< (EIC_CONFIG) High level detection  */
#define   EIC_CONFIG_SENSE6_LOW_Val           (5U)                                           /**< (EIC_CONFIG) Low level detection  */
#define EIC_CONFIG_SENSE6_NONE                (EIC_CONFIG_SENSE6_NONE_Val << EIC_CONFIG_SENSE6_Pos) /**< (EIC_CONFIG) No detection Position  */
#define EIC_CONFIG_SENSE6_RISE                (EIC_CONFIG_SENSE6_RISE_Val << EIC_CONFIG_SENSE6_Pos) /**< (EIC_CONFIG) Rising edge detection Position  */
#define EIC_CONFIG_SENSE6_FALL                (EIC_CONFIG_SENSE6_FALL_Val << EIC_CONFIG_SENSE6_Pos) /**< (EIC_CONFIG) Falling edge detection Position  */
#define EIC_CONFIG_SENSE6_BOTH                (EIC_CONFIG_SENSE6_BOTH_Val << EIC_CONFIG_SENSE6_Pos) /**< (EIC_CONFIG) Both edges detection Position  */
#define EIC_CONFIG_SENSE6_HIGH                (EIC_CONFIG_SENSE6_HIGH_Val << EIC_CONFIG_SENSE6_Pos) /**< (EIC_CONFIG) High level detection Position  */
#define EIC_CONFIG_SENSE6_LOW                 (EIC_CONFIG_SENSE6_LOW_Val << EIC_CONFIG_SENSE6_Pos) /**< (EIC_CONFIG) Low level detection Position  */
#define EIC_CONFIG_FILTEN6_Pos                (27U)                                          /**< (EIC_CONFIG) Filter Enable 6 Position */
#define EIC_CONFIG_FILTEN6_Msk                (0x1U << EIC_CONFIG_FILTEN6_Pos)               /**< (EIC_CONFIG) Filter Enable 6 Mask */
#define EIC_CONFIG_FILTEN6(value)             (EIC_CONFIG_FILTEN6_Msk & ((value) << EIC_CONFIG_FILTEN6_Pos))
#define EIC_CONFIG_SENSE7_Pos                 (28U)                                          /**< (EIC_CONFIG) Input Sense Configuration 7 Position */
#define EIC_CONFIG_SENSE7_Msk                 (0x7U << EIC_CONFIG_SENSE7_Pos)                /**< (EIC_CONFIG) Input Sense Configuration 7 Mask */
#define EIC_CONFIG_SENSE7(value)              (EIC_CONFIG_SENSE7_Msk & ((value) << EIC_CONFIG_SENSE7_Pos))
#define   EIC_CONFIG_SENSE7_NONE_Val          (0U)                                           /**< (EIC_CONFIG) No detection  */
#define   EIC_CONFIG_SENSE7_RISE_Val          (1U)                                           /**< (EIC_CONFIG) Rising edge detection  */
#define   EIC_CONFIG_SENSE7_FALL_Val          (2U)                                           /**< (EIC_CONFIG) Falling edge detection  */
#define   EIC_CONFIG_SENSE7_BOTH_Val          (3U)                                           /**< (EIC_CONFIG) Both edges detection  */
#define   EIC_CONFIG_SENSE7_HIGH_Val          (4U)                                           /**< (EIC_CONFIG) High level detection  */
#define   EIC_CONFIG_SENSE7_LOW_Val           (5U)                                           /**< (EIC_CONFIG) Low level detection  */
#define EIC_CONFIG_SENSE7_NONE                (EIC_CONFIG_SENSE7_NONE_Val << EIC_CONFIG_SENSE7_Pos) /**< (EIC_CONFIG) No detection Position  */
#define EIC_CONFIG_SENSE7_RISE                (EIC_CONFIG_SENSE7_RISE_Val << EIC_CONFIG_SENSE7_Pos) /**< (EIC_CONFIG) Rising edge detection Position  */
#define EIC_CONFIG_SENSE7_FALL                (EIC_CONFIG_SENSE7_FALL_Val << EIC_CONFIG_SENSE7_Pos) /**< (EIC_CONFIG) Falling edge detection Position  */
#define EIC_CONFIG_SENSE7_BOTH                (EIC_CONFIG_SENSE7_BOTH_Val << EIC_CONFIG_SENSE7_Pos) /**< (EIC_CONFIG) Both edges detection Position  */
#define EIC_CONFIG_SENSE7_HIGH                (EIC_CONFIG_SENSE7_HIGH_Val << EIC_CONFIG_SENSE7_Pos) /**< (EIC_CONFIG) High level detection Position  */
#define EIC_CONFIG_SENSE7_LOW                 (EIC_CONFIG_SENSE7_LOW_Val << EIC_CONFIG_SENSE7_Pos) /**< (EIC_CONFIG) Low level detection Position  */
#define EIC_CONFIG_FILTEN7_Pos                (31U)                                          /**< (EIC_CONFIG) Filter Enable 7 Position */
#define EIC_CONFIG_FILTEN7_Msk                (0x1U << EIC_CONFIG_FILTEN7_Pos)               /**< (EIC_CONFIG) Filter Enable 7 Mask */
#define EIC_CONFIG_FILTEN7(value)             (EIC_CONFIG_FILTEN7_Msk & ((value) << EIC_CONFIG_FILTEN7_Pos))
#define EIC_CONFIG_Msk                        (0xFFFFFFFFUL)                                 /**< (EIC_CONFIG) Register Mask  */

/* -------- EIC_DEBOUNCEN : (EIC Offset: 0x30) (R/W 32) Debouncer Enable -------- */
#define EIC_DEBOUNCEN_DEBOUNCEN_Pos           (0U)                                           /**< (EIC_DEBOUNCEN) Debouncer Enable Position */
#define EIC_DEBOUNCEN_DEBOUNCEN_Msk           (0xFFFFU << EIC_DEBOUNCEN_DEBOUNCEN_Pos)       /**< (EIC_DEBOUNCEN) Debouncer Enable Mask */
#define EIC_DEBOUNCEN_DEBOUNCEN(value)        (EIC_DEBOUNCEN_DEBOUNCEN_Msk & ((value) << EIC_DEBOUNCEN_DEBOUNCEN_Pos))
#define EIC_DEBOUNCEN_Msk                     (0x0000FFFFUL)                                 /**< (EIC_DEBOUNCEN) Register Mask  */

/* -------- EIC_DPRESCALER : (EIC Offset: 0x34) (R/W 32) Debouncer Prescaler -------- */
#define EIC_DPRESCALER_PRESCALER0_Pos         (0U)                                           /**< (EIC_DPRESCALER) Debouncer Prescaler Position */
#define EIC_DPRESCALER_PRESCALER0_Msk         (0x7U << EIC_DPRESCALER_PRESCALER0_Pos)        /**< (EIC_DPRESCALER) Debouncer Prescaler Mask */
#define EIC_DPRESCALER_PRESCALER0(value)      (EIC_DPRESCALER_PRESCALER0_Msk & ((value) << EIC_DPRESCALER_PRESCALER0_Pos))
#define   EIC_DPRESCALER_PRESCALER0_DIV2_Val  (0U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 2  */
#define   EIC_DPRESCALER_PRESCALER0_DIV4_Val  (1U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 4  */
#define   EIC_DPRESCALER_PRESCALER0_DIV8_Val  (2U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 8  */
#define   EIC_DPRESCALER_PRESCALER0_DIV16_Val (3U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 16  */
#define   EIC_DPRESCALER_PRESCALER0_DIV32_Val (4U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 32  */
#define   EIC_DPRESCALER_PRESCALER0_DIV64_Val (5U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 64  */
#define   EIC_DPRESCALER_PRESCALER0_DIV128_Val (6U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 128  */
#define   EIC_DPRESCALER_PRESCALER0_DIV256_Val (7U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 256  */
#define EIC_DPRESCALER_PRESCALER0_DIV2        (EIC_DPRESCALER_PRESCALER0_DIV2_Val << EIC_DPRESCALER_PRESCALER0_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 2 Position  */
#define EIC_DPRESCALER_PRESCALER0_DIV4        (EIC_DPRESCALER_PRESCALER0_DIV4_Val << EIC_DPRESCALER_PRESCALER0_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 4 Position  */
#define EIC_DPRESCALER_PRESCALER0_DIV8        (EIC_DPRESCALER_PRESCALER0_DIV8_Val << EIC_DPRESCALER_PRESCALER0_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 8 Position  */
#define EIC_DPRESCALER_PRESCALER0_DIV16       (EIC_DPRESCALER_PRESCALER0_DIV16_Val << EIC_DPRESCALER_PRESCALER0_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 16 Position  */
#define EIC_DPRESCALER_PRESCALER0_DIV32       (EIC_DPRESCALER_PRESCALER0_DIV32_Val << EIC_DPRESCALER_PRESCALER0_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 32 Position  */
#define EIC_DPRESCALER_PRESCALER0_DIV64       (EIC_DPRESCALER_PRESCALER0_DIV64_Val << EIC_DPRESCALER_PRESCALER0_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 64 Position  */
#define EIC_DPRESCALER_PRESCALER0_DIV128      (EIC_DPRESCALER_PRESCALER0_DIV128_Val << EIC_DPRESCALER_PRESCALER0_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 128 Position  */
#define EIC_DPRESCALER_PRESCALER0_DIV256      (EIC_DPRESCALER_PRESCALER0_DIV256_Val << EIC_DPRESCALER_PRESCALER0_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 256 Position  */
#define EIC_DPRESCALER_STATES0_Pos            (3U)                                           /**< (EIC_DPRESCALER) Debouncer number of states Position */
#define EIC_DPRESCALER_STATES0_Msk            (0x1U << EIC_DPRESCALER_STATES0_Pos)           /**< (EIC_DPRESCALER) Debouncer number of states Mask */
#define EIC_DPRESCALER_STATES0(value)         (EIC_DPRESCALER_STATES0_Msk & ((value) << EIC_DPRESCALER_STATES0_Pos))
#define   EIC_DPRESCALER_STATES0_LFREQ3_Val   (0U)                                           /**< (EIC_DPRESCALER) 3 low frequency samples  */
#define   EIC_DPRESCALER_STATES0_LFREQ7_Val   (1U)                                           /**< (EIC_DPRESCALER) 7 low frequency samples  */
#define EIC_DPRESCALER_STATES0_LFREQ3         (EIC_DPRESCALER_STATES0_LFREQ3_Val << EIC_DPRESCALER_STATES0_Pos) /**< (EIC_DPRESCALER) 3 low frequency samples Position  */
#define EIC_DPRESCALER_STATES0_LFREQ7         (EIC_DPRESCALER_STATES0_LFREQ7_Val << EIC_DPRESCALER_STATES0_Pos) /**< (EIC_DPRESCALER) 7 low frequency samples Position  */
#define EIC_DPRESCALER_PRESCALER1_Pos         (4U)                                           /**< (EIC_DPRESCALER) Debouncer Prescaler Position */
#define EIC_DPRESCALER_PRESCALER1_Msk         (0x7U << EIC_DPRESCALER_PRESCALER1_Pos)        /**< (EIC_DPRESCALER) Debouncer Prescaler Mask */
#define EIC_DPRESCALER_PRESCALER1(value)      (EIC_DPRESCALER_PRESCALER1_Msk & ((value) << EIC_DPRESCALER_PRESCALER1_Pos))
#define   EIC_DPRESCALER_PRESCALER1_DIV2_Val  (0U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 2  */
#define   EIC_DPRESCALER_PRESCALER1_DIV4_Val  (1U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 4  */
#define   EIC_DPRESCALER_PRESCALER1_DIV8_Val  (2U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 8  */
#define   EIC_DPRESCALER_PRESCALER1_DIV16_Val (3U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 16  */
#define   EIC_DPRESCALER_PRESCALER1_DIV32_Val (4U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 32  */
#define   EIC_DPRESCALER_PRESCALER1_DIV64_Val (5U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 64  */
#define   EIC_DPRESCALER_PRESCALER1_DIV128_Val (6U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 128  */
#define   EIC_DPRESCALER_PRESCALER1_DIV256_Val (7U)                                           /**< (EIC_DPRESCALER) EIC clock divided by 256  */
#define EIC_DPRESCALER_PRESCALER1_DIV2        (EIC_DPRESCALER_PRESCALER1_DIV2_Val << EIC_DPRESCALER_PRESCALER1_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 2 Position  */
#define EIC_DPRESCALER_PRESCALER1_DIV4        (EIC_DPRESCALER_PRESCALER1_DIV4_Val << EIC_DPRESCALER_PRESCALER1_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 4 Position  */
#define EIC_DPRESCALER_PRESCALER1_DIV8        (EIC_DPRESCALER_PRESCALER1_DIV8_Val << EIC_DPRESCALER_PRESCALER1_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 8 Position  */
#define EIC_DPRESCALER_PRESCALER1_DIV16       (EIC_DPRESCALER_PRESCALER1_DIV16_Val << EIC_DPRESCALER_PRESCALER1_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 16 Position  */
#define EIC_DPRESCALER_PRESCALER1_DIV32       (EIC_DPRESCALER_PRESCALER1_DIV32_Val << EIC_DPRESCALER_PRESCALER1_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 32 Position  */
#define EIC_DPRESCALER_PRESCALER1_DIV64       (EIC_DPRESCALER_PRESCALER1_DIV64_Val << EIC_DPRESCALER_PRESCALER1_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 64 Position  */
#define EIC_DPRESCALER_PRESCALER1_DIV128      (EIC_DPRESCALER_PRESCALER1_DIV128_Val << EIC_DPRESCALER_PRESCALER1_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 128 Position  */
#define EIC_DPRESCALER_PRESCALER1_DIV256      (EIC_DPRESCALER_PRESCALER1_DIV256_Val << EIC_DPRESCALER_PRESCALER1_Pos) /**< (EIC_DPRESCALER) EIC clock divided by 256 Position  */
#define EIC_DPRESCALER_STATES1_Pos            (7U)                                           /**< (EIC_DPRESCALER) Debouncer number of states Position */
#define EIC_DPRESCALER_STATES1_Msk            (0x1U << EIC_DPRESCALER_STATES1_Pos)           /**< (EIC_DPRESCALER) Debouncer number of states Mask */
#define EIC_DPRESCALER_STATES1(value)         (EIC_DPRESCALER_STATES1_Msk & ((value) << EIC_DPRESCALER_STATES1_Pos))
#define   EIC_DPRESCALER_STATES1_LFREQ3_Val   (0U)                                           /**< (EIC_DPRESCALER) 3 low frequency samples  */
#define   EIC_DPRESCALER_STATES1_LFREQ7_Val   (1U)                                           /**< (EIC_DPRESCALER) 7 low frequency samples  */
#define EIC_DPRESCALER_STATES1_LFREQ3         (EIC_DPRESCALER_STATES1_LFREQ3_Val << EIC_DPRESCALER_STATES1_Pos) /**< (EIC_DPRESCALER) 3 low frequency samples Position  */
#define EIC_DPRESCALER_STATES1_LFREQ7         (EIC_DPRESCALER_STATES1_LFREQ7_Val << EIC_DPRESCALER_STATES1_Pos) /**< (EIC_DPRESCALER) 7 low frequency samples Position  */
#define EIC_DPRESCALER_TICKON_Pos             (16U)                                          /**< (EIC_DPRESCALER) Pin Sampler frequency selection Position */
#define EIC_DPRESCALER_TICKON_Msk             (0x1U << EIC_DPRESCALER_TICKON_Pos)            /**< (EIC_DPRESCALER) Pin Sampler frequency selection Mask */
#define EIC_DPRESCALER_TICKON(value)          (EIC_DPRESCALER_TICKON_Msk & ((value) << EIC_DPRESCALER_TICKON_Pos))
#define   EIC_DPRESCALER_TICKON_CLK_GCLK_EIC_Val (0U)                                           /**< (EIC_DPRESCALER) Clocked by GCLK  */
#define   EIC_DPRESCALER_TICKON_CLK_LFREQ_Val (1U)                                           /**< (EIC_DPRESCALER) Clocked by Low Frequency Clock  */
#define EIC_DPRESCALER_TICKON_CLK_GCLK_EIC    (EIC_DPRESCALER_TICKON_CLK_GCLK_EIC_Val << EIC_DPRESCALER_TICKON_Pos) /**< (EIC_DPRESCALER) Clocked by GCLK Position  */
#define EIC_DPRESCALER_TICKON_CLK_LFREQ       (EIC_DPRESCALER_TICKON_CLK_LFREQ_Val << EIC_DPRESCALER_TICKON_Pos) /**< (EIC_DPRESCALER) Clocked by Low Frequency Clock Position  */
#define EIC_DPRESCALER_Msk                    (0x000100FFUL)                                 /**< (EIC_DPRESCALER) Register Mask  */

/* -------- EIC_PINSTATE : (EIC Offset: 0x38) (R/  32) Pin State -------- */
#define EIC_PINSTATE_PINSTATE_Pos             (0U)                                           /**< (EIC_PINSTATE) Pin State Position */
#define EIC_PINSTATE_PINSTATE_Msk             (0xFFFFU << EIC_PINSTATE_PINSTATE_Pos)         /**< (EIC_PINSTATE) Pin State Mask */
#define EIC_PINSTATE_PINSTATE(value)          (EIC_PINSTATE_PINSTATE_Msk & ((value) << EIC_PINSTATE_PINSTATE_Pos))
#define EIC_PINSTATE_Msk                      (0x0000FFFFUL)                                 /**< (EIC_PINSTATE) Register Mask  */

/** \brief EIC register offsets definitions */
#define EIC_CTRLA_OFFSET               (0x00)         /**< (EIC_CTRLA) Control A Offset */
#define EIC_NMICTRL_OFFSET             (0x01)         /**< (EIC_NMICTRL) Non-Maskable Interrupt Control Offset */
#define EIC_NMIFLAG_OFFSET             (0x02)         /**< (EIC_NMIFLAG) Non-Maskable Interrupt Flag Status and Clear Offset */
#define EIC_SYNCBUSY_OFFSET            (0x04)         /**< (EIC_SYNCBUSY) Synchronization Busy Offset */
#define EIC_EVCTRL_OFFSET              (0x08)         /**< (EIC_EVCTRL) Event Control Offset */
#define EIC_INTENCLR_OFFSET            (0x0C)         /**< (EIC_INTENCLR) Interrupt Enable Clear Offset */
#define EIC_INTENSET_OFFSET            (0x10)         /**< (EIC_INTENSET) Interrupt Enable Set Offset */
#define EIC_INTFLAG_OFFSET             (0x14)         /**< (EIC_INTFLAG) Interrupt Flag Status and Clear Offset */
#define EIC_ASYNCH_OFFSET              (0x18)         /**< (EIC_ASYNCH) External Interrupt Asynchronous Mode Offset */
#define EIC_CONFIG_OFFSET              (0x1C)         /**< (EIC_CONFIG) External Interrupt Sense Configuration Offset */
#define EIC_DEBOUNCEN_OFFSET           (0x30)         /**< (EIC_DEBOUNCEN) Debouncer Enable Offset */
#define EIC_DPRESCALER_OFFSET          (0x34)         /**< (EIC_DPRESCALER) Debouncer Prescaler Offset */
#define EIC_PINSTATE_OFFSET            (0x38)         /**< (EIC_PINSTATE) Pin State Offset */

/** \brief EIC register API structure */
typedef struct
{
  __IO  uint8_t                        EIC_CTRLA;       /**< Offset: 0x00 (R/W  8) Control A */
  __IO  uint8_t                        EIC_NMICTRL;     /**< Offset: 0x01 (R/W  8) Non-Maskable Interrupt Control */
  __IO  uint16_t                       EIC_NMIFLAG;     /**< Offset: 0x02 (R/W  16) Non-Maskable Interrupt Flag Status and Clear */
  __I   uint32_t                       EIC_SYNCBUSY;    /**< Offset: 0x04 (R/   32) Synchronization Busy */
  __IO  uint32_t                       EIC_EVCTRL;      /**< Offset: 0x08 (R/W  32) Event Control */
  __IO  uint32_t                       EIC_INTENCLR;    /**< Offset: 0x0c (R/W  32) Interrupt Enable Clear */
  __IO  uint32_t                       EIC_INTENSET;    /**< Offset: 0x10 (R/W  32) Interrupt Enable Set */
  __IO  uint32_t                       EIC_INTFLAG;     /**< Offset: 0x14 (R/W  32) Interrupt Flag Status and Clear */
  __IO  uint32_t                       EIC_ASYNCH;      /**< Offset: 0x18 (R/W  32) External Interrupt Asynchronous Mode */
  __IO  uint32_t                       EIC_CONFIG[2];   /**< Offset: 0x1c (R/W  32) External Interrupt Sense Configuration */
  __I   uint8_t                        Reserved1[0x0C];
  __IO  uint32_t                       EIC_DEBOUNCEN;   /**< Offset: 0x30 (R/W  32) Debouncer Enable */
  __IO  uint32_t                       EIC_DPRESCALER;  /**< Offset: 0x34 (R/W  32) Debouncer Prescaler */
  __I   uint32_t                       EIC_PINSTATE;    /**< Offset: 0x38 (R/   32) Pin State */
} eic_registers_t;
/** @}  end of External Interrupt Controller */

#endif /* SAMC_SAMC21_EIC_MODULE_H */

