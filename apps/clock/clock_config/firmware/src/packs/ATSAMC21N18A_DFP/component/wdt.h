/**
 * \brief Header file for SAMC/SAMC21 WDT
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
#ifndef SAMC_SAMC21_WDT_MODULE_H
#define SAMC_SAMC21_WDT_MODULE_H

/** \addtogroup SAMC_SAMC21 Watchdog Timer
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_WDT                                   */
/* ========================================================================== */

/* -------- WDT_CTRLA : (WDT Offset: 0x00) (R/W 8) Control -------- */
#define WDT_CTRLA_ENABLE_Pos                  (1U)                                           /**< (WDT_CTRLA) Enable Position */
#define WDT_CTRLA_ENABLE_Msk                  (0x1U << WDT_CTRLA_ENABLE_Pos)                 /**< (WDT_CTRLA) Enable Mask */
#define WDT_CTRLA_ENABLE(value)               (WDT_CTRLA_ENABLE_Msk & ((value) << WDT_CTRLA_ENABLE_Pos))
#define WDT_CTRLA_WEN_Pos                     (2U)                                           /**< (WDT_CTRLA) Watchdog Timer Window Mode Enable Position */
#define WDT_CTRLA_WEN_Msk                     (0x1U << WDT_CTRLA_WEN_Pos)                    /**< (WDT_CTRLA) Watchdog Timer Window Mode Enable Mask */
#define WDT_CTRLA_WEN(value)                  (WDT_CTRLA_WEN_Msk & ((value) << WDT_CTRLA_WEN_Pos))
#define WDT_CTRLA_ALWAYSON_Pos                (7U)                                           /**< (WDT_CTRLA) Always-On Position */
#define WDT_CTRLA_ALWAYSON_Msk                (0x1U << WDT_CTRLA_ALWAYSON_Pos)               /**< (WDT_CTRLA) Always-On Mask */
#define WDT_CTRLA_ALWAYSON(value)             (WDT_CTRLA_ALWAYSON_Msk & ((value) << WDT_CTRLA_ALWAYSON_Pos))
#define WDT_CTRLA_Msk                         (0x00000086UL)                                 /**< (WDT_CTRLA) Register Mask  */

/* -------- WDT_CONFIG : (WDT Offset: 0x01) (R/W 8) Configuration -------- */
#define WDT_CONFIG_PER_Pos                    (0U)                                           /**< (WDT_CONFIG) Time-Out Period Position */
#define WDT_CONFIG_PER_Msk                    (0xFU << WDT_CONFIG_PER_Pos)                   /**< (WDT_CONFIG) Time-Out Period Mask */
#define WDT_CONFIG_PER(value)                 (WDT_CONFIG_PER_Msk & ((value) << WDT_CONFIG_PER_Pos))
#define   WDT_CONFIG_PER_CYC8_Val             (0U)                                           /**< (WDT_CONFIG) 8 clock cycles  */
#define   WDT_CONFIG_PER_CYC16_Val            (1U)                                           /**< (WDT_CONFIG) 16 clock cycles  */
#define   WDT_CONFIG_PER_CYC32_Val            (2U)                                           /**< (WDT_CONFIG) 32 clock cycles  */
#define   WDT_CONFIG_PER_CYC64_Val            (3U)                                           /**< (WDT_CONFIG) 64 clock cycles  */
#define   WDT_CONFIG_PER_CYC128_Val           (4U)                                           /**< (WDT_CONFIG) 128 clock cycles  */
#define   WDT_CONFIG_PER_CYC256_Val           (5U)                                           /**< (WDT_CONFIG) 256 clock cycles  */
#define   WDT_CONFIG_PER_CYC512_Val           (6U)                                           /**< (WDT_CONFIG) 512 clock cycles  */
#define   WDT_CONFIG_PER_CYC1024_Val          (7U)                                           /**< (WDT_CONFIG) 1024 clock cycles  */
#define   WDT_CONFIG_PER_CYC2048_Val          (8U)                                           /**< (WDT_CONFIG) 2048 clock cycles  */
#define   WDT_CONFIG_PER_CYC4096_Val          (9U)                                           /**< (WDT_CONFIG) 4096 clock cycles  */
#define   WDT_CONFIG_PER_CYC8192_Val          (10U)                                          /**< (WDT_CONFIG) 8192 clock cycles  */
#define   WDT_CONFIG_PER_CYC16384_Val         (11U)                                          /**< (WDT_CONFIG) 16384 clock cycles  */
#define WDT_CONFIG_PER_CYC8                   (WDT_CONFIG_PER_CYC8_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 8 clock cycles Position  */
#define WDT_CONFIG_PER_CYC16                  (WDT_CONFIG_PER_CYC16_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 16 clock cycles Position  */
#define WDT_CONFIG_PER_CYC32                  (WDT_CONFIG_PER_CYC32_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 32 clock cycles Position  */
#define WDT_CONFIG_PER_CYC64                  (WDT_CONFIG_PER_CYC64_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 64 clock cycles Position  */
#define WDT_CONFIG_PER_CYC128                 (WDT_CONFIG_PER_CYC128_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 128 clock cycles Position  */
#define WDT_CONFIG_PER_CYC256                 (WDT_CONFIG_PER_CYC256_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 256 clock cycles Position  */
#define WDT_CONFIG_PER_CYC512                 (WDT_CONFIG_PER_CYC512_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 512 clock cycles Position  */
#define WDT_CONFIG_PER_CYC1024                (WDT_CONFIG_PER_CYC1024_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 1024 clock cycles Position  */
#define WDT_CONFIG_PER_CYC2048                (WDT_CONFIG_PER_CYC2048_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 2048 clock cycles Position  */
#define WDT_CONFIG_PER_CYC4096                (WDT_CONFIG_PER_CYC4096_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 4096 clock cycles Position  */
#define WDT_CONFIG_PER_CYC8192                (WDT_CONFIG_PER_CYC8192_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 8192 clock cycles Position  */
#define WDT_CONFIG_PER_CYC16384               (WDT_CONFIG_PER_CYC16384_Val << WDT_CONFIG_PER_Pos) /**< (WDT_CONFIG) 16384 clock cycles Position  */
#define WDT_CONFIG_WINDOW_Pos                 (4U)                                           /**< (WDT_CONFIG) Window Mode Time-Out Period Position */
#define WDT_CONFIG_WINDOW_Msk                 (0xFU << WDT_CONFIG_WINDOW_Pos)                /**< (WDT_CONFIG) Window Mode Time-Out Period Mask */
#define WDT_CONFIG_WINDOW(value)              (WDT_CONFIG_WINDOW_Msk & ((value) << WDT_CONFIG_WINDOW_Pos))
#define   WDT_CONFIG_WINDOW_CYC8_Val          (0U)                                           /**< (WDT_CONFIG) 8 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC16_Val         (1U)                                           /**< (WDT_CONFIG) 16 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC32_Val         (2U)                                           /**< (WDT_CONFIG) 32 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC64_Val         (3U)                                           /**< (WDT_CONFIG) 64 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC128_Val        (4U)                                           /**< (WDT_CONFIG) 128 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC256_Val        (5U)                                           /**< (WDT_CONFIG) 256 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC512_Val        (6U)                                           /**< (WDT_CONFIG) 512 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC1024_Val       (7U)                                           /**< (WDT_CONFIG) 1024 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC2048_Val       (8U)                                           /**< (WDT_CONFIG) 2048 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC4096_Val       (9U)                                           /**< (WDT_CONFIG) 4096 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC8192_Val       (10U)                                          /**< (WDT_CONFIG) 8192 clock cycles  */
#define   WDT_CONFIG_WINDOW_CYC16384_Val      (11U)                                          /**< (WDT_CONFIG) 16384 clock cycles  */
#define WDT_CONFIG_WINDOW_CYC8                (WDT_CONFIG_WINDOW_CYC8_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 8 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC16               (WDT_CONFIG_WINDOW_CYC16_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 16 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC32               (WDT_CONFIG_WINDOW_CYC32_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 32 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC64               (WDT_CONFIG_WINDOW_CYC64_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 64 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC128              (WDT_CONFIG_WINDOW_CYC128_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 128 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC256              (WDT_CONFIG_WINDOW_CYC256_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 256 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC512              (WDT_CONFIG_WINDOW_CYC512_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 512 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC1024             (WDT_CONFIG_WINDOW_CYC1024_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 1024 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC2048             (WDT_CONFIG_WINDOW_CYC2048_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 2048 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC4096             (WDT_CONFIG_WINDOW_CYC4096_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 4096 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC8192             (WDT_CONFIG_WINDOW_CYC8192_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 8192 clock cycles Position  */
#define WDT_CONFIG_WINDOW_CYC16384            (WDT_CONFIG_WINDOW_CYC16384_Val << WDT_CONFIG_WINDOW_Pos) /**< (WDT_CONFIG) 16384 clock cycles Position  */
#define WDT_CONFIG_Msk                        (0x000000FFUL)                                 /**< (WDT_CONFIG) Register Mask  */

/* -------- WDT_EWCTRL : (WDT Offset: 0x02) (R/W 8) Early Warning Interrupt Control -------- */
#define WDT_EWCTRL_EWOFFSET_Pos               (0U)                                           /**< (WDT_EWCTRL) Early Warning Interrupt Time Offset Position */
#define WDT_EWCTRL_EWOFFSET_Msk               (0xFU << WDT_EWCTRL_EWOFFSET_Pos)              /**< (WDT_EWCTRL) Early Warning Interrupt Time Offset Mask */
#define WDT_EWCTRL_EWOFFSET(value)            (WDT_EWCTRL_EWOFFSET_Msk & ((value) << WDT_EWCTRL_EWOFFSET_Pos))
#define   WDT_EWCTRL_EWOFFSET_CYC8_Val        (0U)                                           /**< (WDT_EWCTRL) 8 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC16_Val       (1U)                                           /**< (WDT_EWCTRL) 16 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC32_Val       (2U)                                           /**< (WDT_EWCTRL) 32 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC64_Val       (3U)                                           /**< (WDT_EWCTRL) 64 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC128_Val      (4U)                                           /**< (WDT_EWCTRL) 128 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC256_Val      (5U)                                           /**< (WDT_EWCTRL) 256 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC512_Val      (6U)                                           /**< (WDT_EWCTRL) 512 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC1024_Val     (7U)                                           /**< (WDT_EWCTRL) 1024 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC2048_Val     (8U)                                           /**< (WDT_EWCTRL) 2048 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC4096_Val     (9U)                                           /**< (WDT_EWCTRL) 4096 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC8192_Val     (10U)                                          /**< (WDT_EWCTRL) 8192 clock cycles  */
#define   WDT_EWCTRL_EWOFFSET_CYC16384_Val    (11U)                                          /**< (WDT_EWCTRL) 16384 clock cycles  */
#define WDT_EWCTRL_EWOFFSET_CYC8              (WDT_EWCTRL_EWOFFSET_CYC8_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 8 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC16             (WDT_EWCTRL_EWOFFSET_CYC16_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 16 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC32             (WDT_EWCTRL_EWOFFSET_CYC32_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 32 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC64             (WDT_EWCTRL_EWOFFSET_CYC64_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 64 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC128            (WDT_EWCTRL_EWOFFSET_CYC128_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 128 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC256            (WDT_EWCTRL_EWOFFSET_CYC256_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 256 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC512            (WDT_EWCTRL_EWOFFSET_CYC512_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 512 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC1024           (WDT_EWCTRL_EWOFFSET_CYC1024_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 1024 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC2048           (WDT_EWCTRL_EWOFFSET_CYC2048_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 2048 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC4096           (WDT_EWCTRL_EWOFFSET_CYC4096_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 4096 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC8192           (WDT_EWCTRL_EWOFFSET_CYC8192_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 8192 clock cycles Position  */
#define WDT_EWCTRL_EWOFFSET_CYC16384          (WDT_EWCTRL_EWOFFSET_CYC16384_Val << WDT_EWCTRL_EWOFFSET_Pos) /**< (WDT_EWCTRL) 16384 clock cycles Position  */
#define WDT_EWCTRL_Msk                        (0x0000000FUL)                                 /**< (WDT_EWCTRL) Register Mask  */

/* -------- WDT_INTENCLR : (WDT Offset: 0x04) (R/W 8) Interrupt Enable Clear -------- */
#define WDT_INTENCLR_EW_Pos                   (0U)                                           /**< (WDT_INTENCLR) Early Warning Interrupt Enable Position */
#define WDT_INTENCLR_EW_Msk                   (0x1U << WDT_INTENCLR_EW_Pos)                  /**< (WDT_INTENCLR) Early Warning Interrupt Enable Mask */
#define WDT_INTENCLR_EW(value)                (WDT_INTENCLR_EW_Msk & ((value) << WDT_INTENCLR_EW_Pos))
#define WDT_INTENCLR_Msk                      (0x00000001UL)                                 /**< (WDT_INTENCLR) Register Mask  */

/* -------- WDT_INTENSET : (WDT Offset: 0x05) (R/W 8) Interrupt Enable Set -------- */
#define WDT_INTENSET_EW_Pos                   (0U)                                           /**< (WDT_INTENSET) Early Warning Interrupt Enable Position */
#define WDT_INTENSET_EW_Msk                   (0x1U << WDT_INTENSET_EW_Pos)                  /**< (WDT_INTENSET) Early Warning Interrupt Enable Mask */
#define WDT_INTENSET_EW(value)                (WDT_INTENSET_EW_Msk & ((value) << WDT_INTENSET_EW_Pos))
#define WDT_INTENSET_Msk                      (0x00000001UL)                                 /**< (WDT_INTENSET) Register Mask  */

/* -------- WDT_INTFLAG : (WDT Offset: 0x06) (R/W 8) Interrupt Flag Status and Clear -------- */
#define WDT_INTFLAG_EW_Pos                    (0U)                                           /**< (WDT_INTFLAG) Early Warning Position */
#define WDT_INTFLAG_EW_Msk                    (0x1U << WDT_INTFLAG_EW_Pos)                   /**< (WDT_INTFLAG) Early Warning Mask */
#define WDT_INTFLAG_EW(value)                 (WDT_INTFLAG_EW_Msk & ((value) << WDT_INTFLAG_EW_Pos))
#define WDT_INTFLAG_Msk                       (0x00000001UL)                                 /**< (WDT_INTFLAG) Register Mask  */

/* -------- WDT_SYNCBUSY : (WDT Offset: 0x08) (R/  32) Synchronization Busy -------- */
#define WDT_SYNCBUSY_ENABLE_Pos               (1U)                                           /**< (WDT_SYNCBUSY) Enable Busy Position */
#define WDT_SYNCBUSY_ENABLE_Msk               (0x1U << WDT_SYNCBUSY_ENABLE_Pos)              /**< (WDT_SYNCBUSY) Enable Busy Mask */
#define WDT_SYNCBUSY_ENABLE(value)            (WDT_SYNCBUSY_ENABLE_Msk & ((value) << WDT_SYNCBUSY_ENABLE_Pos))
#define WDT_SYNCBUSY_WEN_Pos                  (2U)                                           /**< (WDT_SYNCBUSY) Window Enable Busy Position */
#define WDT_SYNCBUSY_WEN_Msk                  (0x1U << WDT_SYNCBUSY_WEN_Pos)                 /**< (WDT_SYNCBUSY) Window Enable Busy Mask */
#define WDT_SYNCBUSY_WEN(value)               (WDT_SYNCBUSY_WEN_Msk & ((value) << WDT_SYNCBUSY_WEN_Pos))
#define WDT_SYNCBUSY_ALWAYSON_Pos             (3U)                                           /**< (WDT_SYNCBUSY) Always-On Busy Position */
#define WDT_SYNCBUSY_ALWAYSON_Msk             (0x1U << WDT_SYNCBUSY_ALWAYSON_Pos)            /**< (WDT_SYNCBUSY) Always-On Busy Mask */
#define WDT_SYNCBUSY_ALWAYSON(value)          (WDT_SYNCBUSY_ALWAYSON_Msk & ((value) << WDT_SYNCBUSY_ALWAYSON_Pos))
#define WDT_SYNCBUSY_CLEAR_Pos                (4U)                                           /**< (WDT_SYNCBUSY) Clear Busy Position */
#define WDT_SYNCBUSY_CLEAR_Msk                (0x1U << WDT_SYNCBUSY_CLEAR_Pos)               /**< (WDT_SYNCBUSY) Clear Busy Mask */
#define WDT_SYNCBUSY_CLEAR(value)             (WDT_SYNCBUSY_CLEAR_Msk & ((value) << WDT_SYNCBUSY_CLEAR_Pos))
#define WDT_SYNCBUSY_Msk                      (0x0000001EUL)                                 /**< (WDT_SYNCBUSY) Register Mask  */

/* -------- WDT_CLEAR : (WDT Offset: 0x0C) ( /W 8) Clear -------- */
#define WDT_CLEAR_CLEAR_Pos                   (0U)                                           /**< (WDT_CLEAR) Watchdog Clear Position */
#define WDT_CLEAR_CLEAR_Msk                   (0xFFU << WDT_CLEAR_CLEAR_Pos)                 /**< (WDT_CLEAR) Watchdog Clear Mask */
#define WDT_CLEAR_CLEAR(value)                (WDT_CLEAR_CLEAR_Msk & ((value) << WDT_CLEAR_CLEAR_Pos))
#define   WDT_CLEAR_CLEAR_KEY_Val             (165U)                                         /**< (WDT_CLEAR) Clear Key  */
#define WDT_CLEAR_CLEAR_KEY                   (WDT_CLEAR_CLEAR_KEY_Val << WDT_CLEAR_CLEAR_Pos) /**< (WDT_CLEAR) Clear Key Position  */
#define WDT_CLEAR_Msk                         (0x000000FFUL)                                 /**< (WDT_CLEAR) Register Mask  */

/** \brief WDT register offsets definitions */
#define WDT_CTRLA_OFFSET               (0x00)         /**< (WDT_CTRLA) Control Offset */
#define WDT_CONFIG_OFFSET              (0x01)         /**< (WDT_CONFIG) Configuration Offset */
#define WDT_EWCTRL_OFFSET              (0x02)         /**< (WDT_EWCTRL) Early Warning Interrupt Control Offset */
#define WDT_INTENCLR_OFFSET            (0x04)         /**< (WDT_INTENCLR) Interrupt Enable Clear Offset */
#define WDT_INTENSET_OFFSET            (0x05)         /**< (WDT_INTENSET) Interrupt Enable Set Offset */
#define WDT_INTFLAG_OFFSET             (0x06)         /**< (WDT_INTFLAG) Interrupt Flag Status and Clear Offset */
#define WDT_SYNCBUSY_OFFSET            (0x08)         /**< (WDT_SYNCBUSY) Synchronization Busy Offset */
#define WDT_CLEAR_OFFSET               (0x0C)         /**< (WDT_CLEAR) Clear Offset */

/** \brief WDT register API structure */
typedef struct
{
  __IO  uint8_t                        WDT_CTRLA;       /**< Offset: 0x00 (R/W  8) Control */
  __IO  uint8_t                        WDT_CONFIG;      /**< Offset: 0x01 (R/W  8) Configuration */
  __IO  uint8_t                        WDT_EWCTRL;      /**< Offset: 0x02 (R/W  8) Early Warning Interrupt Control */
  __I   uint8_t                        Reserved1[0x01];
  __IO  uint8_t                        WDT_INTENCLR;    /**< Offset: 0x04 (R/W  8) Interrupt Enable Clear */
  __IO  uint8_t                        WDT_INTENSET;    /**< Offset: 0x05 (R/W  8) Interrupt Enable Set */
  __IO  uint8_t                        WDT_INTFLAG;     /**< Offset: 0x06 (R/W  8) Interrupt Flag Status and Clear */
  __I   uint8_t                        Reserved2[0x01];
  __I   uint32_t                       WDT_SYNCBUSY;    /**< Offset: 0x08 (R/   32) Synchronization Busy */
  __O   uint8_t                        WDT_CLEAR;       /**< Offset: 0x0c ( /W  8) Clear */
} wdt_registers_t;
/** @}  end of Watchdog Timer */

#endif /* SAMC_SAMC21_WDT_MODULE_H */

