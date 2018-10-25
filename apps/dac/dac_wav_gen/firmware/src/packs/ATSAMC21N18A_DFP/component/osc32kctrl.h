/**
 * \brief Header file for SAMC/SAMC21 OSC32KCTRL
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
#ifndef SAMC_SAMC21_OSC32KCTRL_MODULE_H
#define SAMC_SAMC21_OSC32KCTRL_MODULE_H

/** \addtogroup SAMC_SAMC21 32k Oscillators Control
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_OSC32KCTRL                            */
/* ========================================================================== */

/* -------- OSC32KCTRL_INTENCLR : (OSC32KCTRL Offset: 0x00) (R/W 32) Interrupt Enable Clear -------- */
#define OSC32KCTRL_INTENCLR_XOSC32KRDY_Pos    (0U)                                           /**< (OSC32KCTRL_INTENCLR) XOSC32K Ready Interrupt Enable Position */
#define OSC32KCTRL_INTENCLR_XOSC32KRDY_Msk    (0x1U << OSC32KCTRL_INTENCLR_XOSC32KRDY_Pos)   /**< (OSC32KCTRL_INTENCLR) XOSC32K Ready Interrupt Enable Mask */
#define OSC32KCTRL_INTENCLR_XOSC32KRDY(value) (OSC32KCTRL_INTENCLR_XOSC32KRDY_Msk & ((value) << OSC32KCTRL_INTENCLR_XOSC32KRDY_Pos))
#define OSC32KCTRL_INTENCLR_OSC32KRDY_Pos     (1U)                                           /**< (OSC32KCTRL_INTENCLR) OSC32K Ready Interrupt Enable Position */
#define OSC32KCTRL_INTENCLR_OSC32KRDY_Msk     (0x1U << OSC32KCTRL_INTENCLR_OSC32KRDY_Pos)    /**< (OSC32KCTRL_INTENCLR) OSC32K Ready Interrupt Enable Mask */
#define OSC32KCTRL_INTENCLR_OSC32KRDY(value)  (OSC32KCTRL_INTENCLR_OSC32KRDY_Msk & ((value) << OSC32KCTRL_INTENCLR_OSC32KRDY_Pos))
#define OSC32KCTRL_INTENCLR_CLKFAIL_Pos       (2U)                                           /**< (OSC32KCTRL_INTENCLR) XOSC32K Clock Failure Detector Interrupt Enable Position */
#define OSC32KCTRL_INTENCLR_CLKFAIL_Msk       (0x1U << OSC32KCTRL_INTENCLR_CLKFAIL_Pos)      /**< (OSC32KCTRL_INTENCLR) XOSC32K Clock Failure Detector Interrupt Enable Mask */
#define OSC32KCTRL_INTENCLR_CLKFAIL(value)    (OSC32KCTRL_INTENCLR_CLKFAIL_Msk & ((value) << OSC32KCTRL_INTENCLR_CLKFAIL_Pos))
#define OSC32KCTRL_INTENCLR_Msk               (0x00000007UL)                                 /**< (OSC32KCTRL_INTENCLR) Register Mask  */

/* -------- OSC32KCTRL_INTENSET : (OSC32KCTRL Offset: 0x04) (R/W 32) Interrupt Enable Set -------- */
#define OSC32KCTRL_INTENSET_XOSC32KRDY_Pos    (0U)                                           /**< (OSC32KCTRL_INTENSET) XOSC32K Ready Interrupt Enable Position */
#define OSC32KCTRL_INTENSET_XOSC32KRDY_Msk    (0x1U << OSC32KCTRL_INTENSET_XOSC32KRDY_Pos)   /**< (OSC32KCTRL_INTENSET) XOSC32K Ready Interrupt Enable Mask */
#define OSC32KCTRL_INTENSET_XOSC32KRDY(value) (OSC32KCTRL_INTENSET_XOSC32KRDY_Msk & ((value) << OSC32KCTRL_INTENSET_XOSC32KRDY_Pos))
#define OSC32KCTRL_INTENSET_OSC32KRDY_Pos     (1U)                                           /**< (OSC32KCTRL_INTENSET) OSC32K Ready Interrupt Enable Position */
#define OSC32KCTRL_INTENSET_OSC32KRDY_Msk     (0x1U << OSC32KCTRL_INTENSET_OSC32KRDY_Pos)    /**< (OSC32KCTRL_INTENSET) OSC32K Ready Interrupt Enable Mask */
#define OSC32KCTRL_INTENSET_OSC32KRDY(value)  (OSC32KCTRL_INTENSET_OSC32KRDY_Msk & ((value) << OSC32KCTRL_INTENSET_OSC32KRDY_Pos))
#define OSC32KCTRL_INTENSET_CLKFAIL_Pos       (2U)                                           /**< (OSC32KCTRL_INTENSET) XOSC32K Clock Failure Detector Interrupt Enable Position */
#define OSC32KCTRL_INTENSET_CLKFAIL_Msk       (0x1U << OSC32KCTRL_INTENSET_CLKFAIL_Pos)      /**< (OSC32KCTRL_INTENSET) XOSC32K Clock Failure Detector Interrupt Enable Mask */
#define OSC32KCTRL_INTENSET_CLKFAIL(value)    (OSC32KCTRL_INTENSET_CLKFAIL_Msk & ((value) << OSC32KCTRL_INTENSET_CLKFAIL_Pos))
#define OSC32KCTRL_INTENSET_Msk               (0x00000007UL)                                 /**< (OSC32KCTRL_INTENSET) Register Mask  */

/* -------- OSC32KCTRL_INTFLAG : (OSC32KCTRL Offset: 0x08) (R/W 32) Interrupt Flag Status and Clear -------- */
#define OSC32KCTRL_INTFLAG_XOSC32KRDY_Pos     (0U)                                           /**< (OSC32KCTRL_INTFLAG) XOSC32K Ready Position */
#define OSC32KCTRL_INTFLAG_XOSC32KRDY_Msk     (0x1U << OSC32KCTRL_INTFLAG_XOSC32KRDY_Pos)    /**< (OSC32KCTRL_INTFLAG) XOSC32K Ready Mask */
#define OSC32KCTRL_INTFLAG_XOSC32KRDY(value)  (OSC32KCTRL_INTFLAG_XOSC32KRDY_Msk & ((value) << OSC32KCTRL_INTFLAG_XOSC32KRDY_Pos))
#define OSC32KCTRL_INTFLAG_OSC32KRDY_Pos      (1U)                                           /**< (OSC32KCTRL_INTFLAG) OSC32K Ready Position */
#define OSC32KCTRL_INTFLAG_OSC32KRDY_Msk      (0x1U << OSC32KCTRL_INTFLAG_OSC32KRDY_Pos)     /**< (OSC32KCTRL_INTFLAG) OSC32K Ready Mask */
#define OSC32KCTRL_INTFLAG_OSC32KRDY(value)   (OSC32KCTRL_INTFLAG_OSC32KRDY_Msk & ((value) << OSC32KCTRL_INTFLAG_OSC32KRDY_Pos))
#define OSC32KCTRL_INTFLAG_CLKFAIL_Pos        (2U)                                           /**< (OSC32KCTRL_INTFLAG) XOSC32K Clock Failure Detector Position */
#define OSC32KCTRL_INTFLAG_CLKFAIL_Msk        (0x1U << OSC32KCTRL_INTFLAG_CLKFAIL_Pos)       /**< (OSC32KCTRL_INTFLAG) XOSC32K Clock Failure Detector Mask */
#define OSC32KCTRL_INTFLAG_CLKFAIL(value)     (OSC32KCTRL_INTFLAG_CLKFAIL_Msk & ((value) << OSC32KCTRL_INTFLAG_CLKFAIL_Pos))
#define OSC32KCTRL_INTFLAG_Msk                (0x00000007UL)                                 /**< (OSC32KCTRL_INTFLAG) Register Mask  */

/* -------- OSC32KCTRL_STATUS : (OSC32KCTRL Offset: 0x0C) (R/  32) Power and Clocks Status -------- */
#define OSC32KCTRL_STATUS_XOSC32KRDY_Pos      (0U)                                           /**< (OSC32KCTRL_STATUS) XOSC32K Ready Position */
#define OSC32KCTRL_STATUS_XOSC32KRDY_Msk      (0x1U << OSC32KCTRL_STATUS_XOSC32KRDY_Pos)     /**< (OSC32KCTRL_STATUS) XOSC32K Ready Mask */
#define OSC32KCTRL_STATUS_XOSC32KRDY(value)   (OSC32KCTRL_STATUS_XOSC32KRDY_Msk & ((value) << OSC32KCTRL_STATUS_XOSC32KRDY_Pos))
#define OSC32KCTRL_STATUS_OSC32KRDY_Pos       (1U)                                           /**< (OSC32KCTRL_STATUS) OSC32K Ready Position */
#define OSC32KCTRL_STATUS_OSC32KRDY_Msk       (0x1U << OSC32KCTRL_STATUS_OSC32KRDY_Pos)      /**< (OSC32KCTRL_STATUS) OSC32K Ready Mask */
#define OSC32KCTRL_STATUS_OSC32KRDY(value)    (OSC32KCTRL_STATUS_OSC32KRDY_Msk & ((value) << OSC32KCTRL_STATUS_OSC32KRDY_Pos))
#define OSC32KCTRL_STATUS_CLKFAIL_Pos         (2U)                                           /**< (OSC32KCTRL_STATUS) XOSC32K Clock Failure Detector Position */
#define OSC32KCTRL_STATUS_CLKFAIL_Msk         (0x1U << OSC32KCTRL_STATUS_CLKFAIL_Pos)        /**< (OSC32KCTRL_STATUS) XOSC32K Clock Failure Detector Mask */
#define OSC32KCTRL_STATUS_CLKFAIL(value)      (OSC32KCTRL_STATUS_CLKFAIL_Msk & ((value) << OSC32KCTRL_STATUS_CLKFAIL_Pos))
#define OSC32KCTRL_STATUS_CLKSW_Pos           (3U)                                           /**< (OSC32KCTRL_STATUS) XOSC32K Clock switch Position */
#define OSC32KCTRL_STATUS_CLKSW_Msk           (0x1U << OSC32KCTRL_STATUS_CLKSW_Pos)          /**< (OSC32KCTRL_STATUS) XOSC32K Clock switch Mask */
#define OSC32KCTRL_STATUS_CLKSW(value)        (OSC32KCTRL_STATUS_CLKSW_Msk & ((value) << OSC32KCTRL_STATUS_CLKSW_Pos))
#define OSC32KCTRL_STATUS_Msk                 (0x0000000FUL)                                 /**< (OSC32KCTRL_STATUS) Register Mask  */

/* -------- OSC32KCTRL_RTCCTRL : (OSC32KCTRL Offset: 0x10) (R/W 32) Clock selection -------- */
#define OSC32KCTRL_RTCCTRL_RTCSEL_Pos         (0U)                                           /**< (OSC32KCTRL_RTCCTRL) RTC Clock Selection Position */
#define OSC32KCTRL_RTCCTRL_RTCSEL_Msk         (0x7U << OSC32KCTRL_RTCCTRL_RTCSEL_Pos)        /**< (OSC32KCTRL_RTCCTRL) RTC Clock Selection Mask */
#define OSC32KCTRL_RTCCTRL_RTCSEL(value)      (OSC32KCTRL_RTCCTRL_RTCSEL_Msk & ((value) << OSC32KCTRL_RTCCTRL_RTCSEL_Pos))
#define   OSC32KCTRL_RTCCTRL_RTCSEL_ULP1K_Val (0U)                                           /**< (OSC32KCTRL_RTCCTRL) 1.024kHz from 32kHz internal ULP oscillator  */
#define   OSC32KCTRL_RTCCTRL_RTCSEL_ULP32K_Val (1U)                                           /**< (OSC32KCTRL_RTCCTRL) 32.768kHz from 32kHz internal ULP oscillator  */
#define   OSC32KCTRL_RTCCTRL_RTCSEL_OSC1K_Val (2U)                                           /**< (OSC32KCTRL_RTCCTRL) 1.024kHz from 32.768kHz internal oscillator  */
#define   OSC32KCTRL_RTCCTRL_RTCSEL_OSC32K_Val (3U)                                           /**< (OSC32KCTRL_RTCCTRL) 32.768kHz from 32.768kHz internal oscillator  */
#define   OSC32KCTRL_RTCCTRL_RTCSEL_XOSC1K_Val (4U)                                           /**< (OSC32KCTRL_RTCCTRL) 1.024kHz from 32.768kHz internal oscillator  */
#define   OSC32KCTRL_RTCCTRL_RTCSEL_XOSC32K_Val (5U)                                           /**< (OSC32KCTRL_RTCCTRL) 32.768kHz from 32.768kHz external crystal oscillator  */
#define OSC32KCTRL_RTCCTRL_RTCSEL_ULP1K       (OSC32KCTRL_RTCCTRL_RTCSEL_ULP1K_Val << OSC32KCTRL_RTCCTRL_RTCSEL_Pos) /**< (OSC32KCTRL_RTCCTRL) 1.024kHz from 32kHz internal ULP oscillator Position  */
#define OSC32KCTRL_RTCCTRL_RTCSEL_ULP32K      (OSC32KCTRL_RTCCTRL_RTCSEL_ULP32K_Val << OSC32KCTRL_RTCCTRL_RTCSEL_Pos) /**< (OSC32KCTRL_RTCCTRL) 32.768kHz from 32kHz internal ULP oscillator Position  */
#define OSC32KCTRL_RTCCTRL_RTCSEL_OSC1K       (OSC32KCTRL_RTCCTRL_RTCSEL_OSC1K_Val << OSC32KCTRL_RTCCTRL_RTCSEL_Pos) /**< (OSC32KCTRL_RTCCTRL) 1.024kHz from 32.768kHz internal oscillator Position  */
#define OSC32KCTRL_RTCCTRL_RTCSEL_OSC32K      (OSC32KCTRL_RTCCTRL_RTCSEL_OSC32K_Val << OSC32KCTRL_RTCCTRL_RTCSEL_Pos) /**< (OSC32KCTRL_RTCCTRL) 32.768kHz from 32.768kHz internal oscillator Position  */
#define OSC32KCTRL_RTCCTRL_RTCSEL_XOSC1K      (OSC32KCTRL_RTCCTRL_RTCSEL_XOSC1K_Val << OSC32KCTRL_RTCCTRL_RTCSEL_Pos) /**< (OSC32KCTRL_RTCCTRL) 1.024kHz from 32.768kHz internal oscillator Position  */
#define OSC32KCTRL_RTCCTRL_RTCSEL_XOSC32K     (OSC32KCTRL_RTCCTRL_RTCSEL_XOSC32K_Val << OSC32KCTRL_RTCCTRL_RTCSEL_Pos) /**< (OSC32KCTRL_RTCCTRL) 32.768kHz from 32.768kHz external crystal oscillator Position  */
#define OSC32KCTRL_RTCCTRL_Msk                (0x00000007UL)                                 /**< (OSC32KCTRL_RTCCTRL) Register Mask  */

/* -------- OSC32KCTRL_XOSC32K : (OSC32KCTRL Offset: 0x14) (R/W 16) 32kHz External Crystal Oscillator (XOSC32K) Control -------- */
#define OSC32KCTRL_XOSC32K_ENABLE_Pos         (1U)                                           /**< (OSC32KCTRL_XOSC32K) Oscillator Enable Position */
#define OSC32KCTRL_XOSC32K_ENABLE_Msk         (0x1U << OSC32KCTRL_XOSC32K_ENABLE_Pos)        /**< (OSC32KCTRL_XOSC32K) Oscillator Enable Mask */
#define OSC32KCTRL_XOSC32K_ENABLE(value)      (OSC32KCTRL_XOSC32K_ENABLE_Msk & ((value) << OSC32KCTRL_XOSC32K_ENABLE_Pos))
#define OSC32KCTRL_XOSC32K_XTALEN_Pos         (2U)                                           /**< (OSC32KCTRL_XOSC32K) Crystal Oscillator Enable Position */
#define OSC32KCTRL_XOSC32K_XTALEN_Msk         (0x1U << OSC32KCTRL_XOSC32K_XTALEN_Pos)        /**< (OSC32KCTRL_XOSC32K) Crystal Oscillator Enable Mask */
#define OSC32KCTRL_XOSC32K_XTALEN(value)      (OSC32KCTRL_XOSC32K_XTALEN_Msk & ((value) << OSC32KCTRL_XOSC32K_XTALEN_Pos))
#define OSC32KCTRL_XOSC32K_EN32K_Pos          (3U)                                           /**< (OSC32KCTRL_XOSC32K) 32kHz Output Enable Position */
#define OSC32KCTRL_XOSC32K_EN32K_Msk          (0x1U << OSC32KCTRL_XOSC32K_EN32K_Pos)         /**< (OSC32KCTRL_XOSC32K) 32kHz Output Enable Mask */
#define OSC32KCTRL_XOSC32K_EN32K(value)       (OSC32KCTRL_XOSC32K_EN32K_Msk & ((value) << OSC32KCTRL_XOSC32K_EN32K_Pos))
#define OSC32KCTRL_XOSC32K_EN1K_Pos           (4U)                                           /**< (OSC32KCTRL_XOSC32K) 1kHz Output Enable Position */
#define OSC32KCTRL_XOSC32K_EN1K_Msk           (0x1U << OSC32KCTRL_XOSC32K_EN1K_Pos)          /**< (OSC32KCTRL_XOSC32K) 1kHz Output Enable Mask */
#define OSC32KCTRL_XOSC32K_EN1K(value)        (OSC32KCTRL_XOSC32K_EN1K_Msk & ((value) << OSC32KCTRL_XOSC32K_EN1K_Pos))
#define OSC32KCTRL_XOSC32K_RUNSTDBY_Pos       (6U)                                           /**< (OSC32KCTRL_XOSC32K) Run in Standby Position */
#define OSC32KCTRL_XOSC32K_RUNSTDBY_Msk       (0x1U << OSC32KCTRL_XOSC32K_RUNSTDBY_Pos)      /**< (OSC32KCTRL_XOSC32K) Run in Standby Mask */
#define OSC32KCTRL_XOSC32K_RUNSTDBY(value)    (OSC32KCTRL_XOSC32K_RUNSTDBY_Msk & ((value) << OSC32KCTRL_XOSC32K_RUNSTDBY_Pos))
#define OSC32KCTRL_XOSC32K_ONDEMAND_Pos       (7U)                                           /**< (OSC32KCTRL_XOSC32K) On Demand Control Position */
#define OSC32KCTRL_XOSC32K_ONDEMAND_Msk       (0x1U << OSC32KCTRL_XOSC32K_ONDEMAND_Pos)      /**< (OSC32KCTRL_XOSC32K) On Demand Control Mask */
#define OSC32KCTRL_XOSC32K_ONDEMAND(value)    (OSC32KCTRL_XOSC32K_ONDEMAND_Msk & ((value) << OSC32KCTRL_XOSC32K_ONDEMAND_Pos))
#define OSC32KCTRL_XOSC32K_STARTUP_Pos        (8U)                                           /**< (OSC32KCTRL_XOSC32K) Oscillator Start-Up Time Position */
#define OSC32KCTRL_XOSC32K_STARTUP_Msk        (0x7U << OSC32KCTRL_XOSC32K_STARTUP_Pos)       /**< (OSC32KCTRL_XOSC32K) Oscillator Start-Up Time Mask */
#define OSC32KCTRL_XOSC32K_STARTUP(value)     (OSC32KCTRL_XOSC32K_STARTUP_Msk & ((value) << OSC32KCTRL_XOSC32K_STARTUP_Pos))
#define   OSC32KCTRL_XOSC32K_STARTUP_CYCLE1_Val (0U)                                           /**< (OSC32KCTRL_XOSC32K) 0.122 ms  */
#define   OSC32KCTRL_XOSC32K_STARTUP_CYCLE32_Val (1U)                                           /**< (OSC32KCTRL_XOSC32K) 1.068 ms  */
#define   OSC32KCTRL_XOSC32K_STARTUP_CYCLE2048_Val (2U)                                           /**< (OSC32KCTRL_XOSC32K) 62.6 ms  */
#define   OSC32KCTRL_XOSC32K_STARTUP_CYCLE4096_Val (3U)                                           /**< (OSC32KCTRL_XOSC32K) 125 ms  */
#define   OSC32KCTRL_XOSC32K_STARTUP_CYCLE16384_Val (4U)                                           /**< (OSC32KCTRL_XOSC32K) 500 ms  */
#define   OSC32KCTRL_XOSC32K_STARTUP_CYCLE32768_Val (5U)                                           /**< (OSC32KCTRL_XOSC32K) 1000 ms  */
#define   OSC32KCTRL_XOSC32K_STARTUP_CYCLE65536_Val (6U)                                           /**< (OSC32KCTRL_XOSC32K) 2000 ms  */
#define   OSC32KCTRL_XOSC32K_STARTUP_CYCLE131072_Val (7U)                                           /**< (OSC32KCTRL_XOSC32K) 4000 ms  */
#define OSC32KCTRL_XOSC32K_STARTUP_CYCLE1     (OSC32KCTRL_XOSC32K_STARTUP_CYCLE1_Val << OSC32KCTRL_XOSC32K_STARTUP_Pos) /**< (OSC32KCTRL_XOSC32K) 0.122 ms Position  */
#define OSC32KCTRL_XOSC32K_STARTUP_CYCLE32    (OSC32KCTRL_XOSC32K_STARTUP_CYCLE32_Val << OSC32KCTRL_XOSC32K_STARTUP_Pos) /**< (OSC32KCTRL_XOSC32K) 1.068 ms Position  */
#define OSC32KCTRL_XOSC32K_STARTUP_CYCLE2048  (OSC32KCTRL_XOSC32K_STARTUP_CYCLE2048_Val << OSC32KCTRL_XOSC32K_STARTUP_Pos) /**< (OSC32KCTRL_XOSC32K) 62.6 ms Position  */
#define OSC32KCTRL_XOSC32K_STARTUP_CYCLE4096  (OSC32KCTRL_XOSC32K_STARTUP_CYCLE4096_Val << OSC32KCTRL_XOSC32K_STARTUP_Pos) /**< (OSC32KCTRL_XOSC32K) 125 ms Position  */
#define OSC32KCTRL_XOSC32K_STARTUP_CYCLE16384 (OSC32KCTRL_XOSC32K_STARTUP_CYCLE16384_Val << OSC32KCTRL_XOSC32K_STARTUP_Pos) /**< (OSC32KCTRL_XOSC32K) 500 ms Position  */
#define OSC32KCTRL_XOSC32K_STARTUP_CYCLE32768 (OSC32KCTRL_XOSC32K_STARTUP_CYCLE32768_Val << OSC32KCTRL_XOSC32K_STARTUP_Pos) /**< (OSC32KCTRL_XOSC32K) 1000 ms Position  */
#define OSC32KCTRL_XOSC32K_STARTUP_CYCLE65536 (OSC32KCTRL_XOSC32K_STARTUP_CYCLE65536_Val << OSC32KCTRL_XOSC32K_STARTUP_Pos) /**< (OSC32KCTRL_XOSC32K) 2000 ms Position  */
#define OSC32KCTRL_XOSC32K_STARTUP_CYCLE131072 (OSC32KCTRL_XOSC32K_STARTUP_CYCLE131072_Val << OSC32KCTRL_XOSC32K_STARTUP_Pos) /**< (OSC32KCTRL_XOSC32K) 4000 ms Position  */
#define OSC32KCTRL_XOSC32K_WRTLOCK_Pos        (12U)                                          /**< (OSC32KCTRL_XOSC32K) Write Lock Position */
#define OSC32KCTRL_XOSC32K_WRTLOCK_Msk        (0x1U << OSC32KCTRL_XOSC32K_WRTLOCK_Pos)       /**< (OSC32KCTRL_XOSC32K) Write Lock Mask */
#define OSC32KCTRL_XOSC32K_WRTLOCK(value)     (OSC32KCTRL_XOSC32K_WRTLOCK_Msk & ((value) << OSC32KCTRL_XOSC32K_WRTLOCK_Pos))
#define OSC32KCTRL_XOSC32K_Msk                (0x000017DEUL)                                 /**< (OSC32KCTRL_XOSC32K) Register Mask  */

/* -------- OSC32KCTRL_CFDCTRL : (OSC32KCTRL Offset: 0x16) (R/W 8) Clock Failure Detector Control -------- */
#define OSC32KCTRL_CFDCTRL_CFDEN_Pos          (0U)                                           /**< (OSC32KCTRL_CFDCTRL) Clock Failure Detector Enable Position */
#define OSC32KCTRL_CFDCTRL_CFDEN_Msk          (0x1U << OSC32KCTRL_CFDCTRL_CFDEN_Pos)         /**< (OSC32KCTRL_CFDCTRL) Clock Failure Detector Enable Mask */
#define OSC32KCTRL_CFDCTRL_CFDEN(value)       (OSC32KCTRL_CFDCTRL_CFDEN_Msk & ((value) << OSC32KCTRL_CFDCTRL_CFDEN_Pos))
#define OSC32KCTRL_CFDCTRL_SWBACK_Pos         (1U)                                           /**< (OSC32KCTRL_CFDCTRL) Clock Switch Back Position */
#define OSC32KCTRL_CFDCTRL_SWBACK_Msk         (0x1U << OSC32KCTRL_CFDCTRL_SWBACK_Pos)        /**< (OSC32KCTRL_CFDCTRL) Clock Switch Back Mask */
#define OSC32KCTRL_CFDCTRL_SWBACK(value)      (OSC32KCTRL_CFDCTRL_SWBACK_Msk & ((value) << OSC32KCTRL_CFDCTRL_SWBACK_Pos))
#define OSC32KCTRL_CFDCTRL_CFDPRESC_Pos       (2U)                                           /**< (OSC32KCTRL_CFDCTRL) Clock Failure Detector Prescaler Position */
#define OSC32KCTRL_CFDCTRL_CFDPRESC_Msk       (0x1U << OSC32KCTRL_CFDCTRL_CFDPRESC_Pos)      /**< (OSC32KCTRL_CFDCTRL) Clock Failure Detector Prescaler Mask */
#define OSC32KCTRL_CFDCTRL_CFDPRESC(value)    (OSC32KCTRL_CFDCTRL_CFDPRESC_Msk & ((value) << OSC32KCTRL_CFDCTRL_CFDPRESC_Pos))
#define OSC32KCTRL_CFDCTRL_Msk                (0x00000007UL)                                 /**< (OSC32KCTRL_CFDCTRL) Register Mask  */

/* -------- OSC32KCTRL_EVCTRL : (OSC32KCTRL Offset: 0x17) (R/W 8) Event Control -------- */
#define OSC32KCTRL_EVCTRL_CFDEO_Pos           (0U)                                           /**< (OSC32KCTRL_EVCTRL) Clock Failure Detector Event Output Enable Position */
#define OSC32KCTRL_EVCTRL_CFDEO_Msk           (0x1U << OSC32KCTRL_EVCTRL_CFDEO_Pos)          /**< (OSC32KCTRL_EVCTRL) Clock Failure Detector Event Output Enable Mask */
#define OSC32KCTRL_EVCTRL_CFDEO(value)        (OSC32KCTRL_EVCTRL_CFDEO_Msk & ((value) << OSC32KCTRL_EVCTRL_CFDEO_Pos))
#define OSC32KCTRL_EVCTRL_Msk                 (0x00000001UL)                                 /**< (OSC32KCTRL_EVCTRL) Register Mask  */

/* -------- OSC32KCTRL_OSC32K : (OSC32KCTRL Offset: 0x18) (R/W 32) 32kHz Internal Oscillator (OSC32K) Control -------- */
#define OSC32KCTRL_OSC32K_ENABLE_Pos          (1U)                                           /**< (OSC32KCTRL_OSC32K) Oscillator Enable Position */
#define OSC32KCTRL_OSC32K_ENABLE_Msk          (0x1U << OSC32KCTRL_OSC32K_ENABLE_Pos)         /**< (OSC32KCTRL_OSC32K) Oscillator Enable Mask */
#define OSC32KCTRL_OSC32K_ENABLE(value)       (OSC32KCTRL_OSC32K_ENABLE_Msk & ((value) << OSC32KCTRL_OSC32K_ENABLE_Pos))
#define OSC32KCTRL_OSC32K_EN32K_Pos           (2U)                                           /**< (OSC32KCTRL_OSC32K) 32kHz Output Enable Position */
#define OSC32KCTRL_OSC32K_EN32K_Msk           (0x1U << OSC32KCTRL_OSC32K_EN32K_Pos)          /**< (OSC32KCTRL_OSC32K) 32kHz Output Enable Mask */
#define OSC32KCTRL_OSC32K_EN32K(value)        (OSC32KCTRL_OSC32K_EN32K_Msk & ((value) << OSC32KCTRL_OSC32K_EN32K_Pos))
#define OSC32KCTRL_OSC32K_EN1K_Pos            (3U)                                           /**< (OSC32KCTRL_OSC32K) 1kHz Output Enable Position */
#define OSC32KCTRL_OSC32K_EN1K_Msk            (0x1U << OSC32KCTRL_OSC32K_EN1K_Pos)           /**< (OSC32KCTRL_OSC32K) 1kHz Output Enable Mask */
#define OSC32KCTRL_OSC32K_EN1K(value)         (OSC32KCTRL_OSC32K_EN1K_Msk & ((value) << OSC32KCTRL_OSC32K_EN1K_Pos))
#define OSC32KCTRL_OSC32K_RUNSTDBY_Pos        (6U)                                           /**< (OSC32KCTRL_OSC32K) Run in Standby Position */
#define OSC32KCTRL_OSC32K_RUNSTDBY_Msk        (0x1U << OSC32KCTRL_OSC32K_RUNSTDBY_Pos)       /**< (OSC32KCTRL_OSC32K) Run in Standby Mask */
#define OSC32KCTRL_OSC32K_RUNSTDBY(value)     (OSC32KCTRL_OSC32K_RUNSTDBY_Msk & ((value) << OSC32KCTRL_OSC32K_RUNSTDBY_Pos))
#define OSC32KCTRL_OSC32K_ONDEMAND_Pos        (7U)                                           /**< (OSC32KCTRL_OSC32K) On Demand Control Position */
#define OSC32KCTRL_OSC32K_ONDEMAND_Msk        (0x1U << OSC32KCTRL_OSC32K_ONDEMAND_Pos)       /**< (OSC32KCTRL_OSC32K) On Demand Control Mask */
#define OSC32KCTRL_OSC32K_ONDEMAND(value)     (OSC32KCTRL_OSC32K_ONDEMAND_Msk & ((value) << OSC32KCTRL_OSC32K_ONDEMAND_Pos))
#define OSC32KCTRL_OSC32K_STARTUP_Pos         (8U)                                           /**< (OSC32KCTRL_OSC32K) Oscillator Start-Up Time Position */
#define OSC32KCTRL_OSC32K_STARTUP_Msk         (0x7U << OSC32KCTRL_OSC32K_STARTUP_Pos)        /**< (OSC32KCTRL_OSC32K) Oscillator Start-Up Time Mask */
#define OSC32KCTRL_OSC32K_STARTUP(value)      (OSC32KCTRL_OSC32K_STARTUP_Msk & ((value) << OSC32KCTRL_OSC32K_STARTUP_Pos))
#define   OSC32KCTRL_OSC32K_STARTUP_CYCLE3_Val (0U)                                           /**< (OSC32KCTRL_OSC32K) 0.092 ms  */
#define   OSC32KCTRL_OSC32K_STARTUP_CYCLE4_Val (1U)                                           /**< (OSC32KCTRL_OSC32K) 0.122 ms  */
#define   OSC32KCTRL_OSC32K_STARTUP_CYCLE6_Val (2U)                                           /**< (OSC32KCTRL_OSC32K) 0.183 ms  */
#define   OSC32KCTRL_OSC32K_STARTUP_CYCLE10_Val (3U)                                           /**< (OSC32KCTRL_OSC32K) 0.305 ms  */
#define   OSC32KCTRL_OSC32K_STARTUP_CYCLE18_Val (4U)                                           /**< (OSC32KCTRL_OSC32K) 0.549 ms  */
#define   OSC32KCTRL_OSC32K_STARTUP_CYCLE34_Val (5U)                                           /**< (OSC32KCTRL_OSC32K) 1.038 ms  */
#define   OSC32KCTRL_OSC32K_STARTUP_CYCLE66_Val (6U)                                           /**< (OSC32KCTRL_OSC32K) 2.014 ms  */
#define   OSC32KCTRL_OSC32K_STARTUP_CYCLE130_Val (7U)                                           /**< (OSC32KCTRL_OSC32K) 3.967 ms  */
#define OSC32KCTRL_OSC32K_STARTUP_CYCLE3      (OSC32KCTRL_OSC32K_STARTUP_CYCLE3_Val << OSC32KCTRL_OSC32K_STARTUP_Pos) /**< (OSC32KCTRL_OSC32K) 0.092 ms Position  */
#define OSC32KCTRL_OSC32K_STARTUP_CYCLE4      (OSC32KCTRL_OSC32K_STARTUP_CYCLE4_Val << OSC32KCTRL_OSC32K_STARTUP_Pos) /**< (OSC32KCTRL_OSC32K) 0.122 ms Position  */
#define OSC32KCTRL_OSC32K_STARTUP_CYCLE6      (OSC32KCTRL_OSC32K_STARTUP_CYCLE6_Val << OSC32KCTRL_OSC32K_STARTUP_Pos) /**< (OSC32KCTRL_OSC32K) 0.183 ms Position  */
#define OSC32KCTRL_OSC32K_STARTUP_CYCLE10     (OSC32KCTRL_OSC32K_STARTUP_CYCLE10_Val << OSC32KCTRL_OSC32K_STARTUP_Pos) /**< (OSC32KCTRL_OSC32K) 0.305 ms Position  */
#define OSC32KCTRL_OSC32K_STARTUP_CYCLE18     (OSC32KCTRL_OSC32K_STARTUP_CYCLE18_Val << OSC32KCTRL_OSC32K_STARTUP_Pos) /**< (OSC32KCTRL_OSC32K) 0.549 ms Position  */
#define OSC32KCTRL_OSC32K_STARTUP_CYCLE34     (OSC32KCTRL_OSC32K_STARTUP_CYCLE34_Val << OSC32KCTRL_OSC32K_STARTUP_Pos) /**< (OSC32KCTRL_OSC32K) 1.038 ms Position  */
#define OSC32KCTRL_OSC32K_STARTUP_CYCLE66     (OSC32KCTRL_OSC32K_STARTUP_CYCLE66_Val << OSC32KCTRL_OSC32K_STARTUP_Pos) /**< (OSC32KCTRL_OSC32K) 2.014 ms Position  */
#define OSC32KCTRL_OSC32K_STARTUP_CYCLE130    (OSC32KCTRL_OSC32K_STARTUP_CYCLE130_Val << OSC32KCTRL_OSC32K_STARTUP_Pos) /**< (OSC32KCTRL_OSC32K) 3.967 ms Position  */
#define OSC32KCTRL_OSC32K_WRTLOCK_Pos         (12U)                                          /**< (OSC32KCTRL_OSC32K) Write Lock Position */
#define OSC32KCTRL_OSC32K_WRTLOCK_Msk         (0x1U << OSC32KCTRL_OSC32K_WRTLOCK_Pos)        /**< (OSC32KCTRL_OSC32K) Write Lock Mask */
#define OSC32KCTRL_OSC32K_WRTLOCK(value)      (OSC32KCTRL_OSC32K_WRTLOCK_Msk & ((value) << OSC32KCTRL_OSC32K_WRTLOCK_Pos))
#define OSC32KCTRL_OSC32K_CALIB_Pos           (16U)                                          /**< (OSC32KCTRL_OSC32K) Oscillator Calibration Position */
#define OSC32KCTRL_OSC32K_CALIB_Msk           (0x7FU << OSC32KCTRL_OSC32K_CALIB_Pos)         /**< (OSC32KCTRL_OSC32K) Oscillator Calibration Mask */
#define OSC32KCTRL_OSC32K_CALIB(value)        (OSC32KCTRL_OSC32K_CALIB_Msk & ((value) << OSC32KCTRL_OSC32K_CALIB_Pos))
#define OSC32KCTRL_OSC32K_Msk                 (0x007F17CEUL)                                 /**< (OSC32KCTRL_OSC32K) Register Mask  */

/* -------- OSC32KCTRL_OSCULP32K : (OSC32KCTRL Offset: 0x1C) (R/W 32) 32kHz Ultra Low Power Internal Oscillator (OSCULP32K) Control -------- */
#define OSC32KCTRL_OSCULP32K_CALIB_Pos        (8U)                                           /**< (OSC32KCTRL_OSCULP32K) Oscillator Calibration Position */
#define OSC32KCTRL_OSCULP32K_CALIB_Msk        (0x1FU << OSC32KCTRL_OSCULP32K_CALIB_Pos)      /**< (OSC32KCTRL_OSCULP32K) Oscillator Calibration Mask */
#define OSC32KCTRL_OSCULP32K_CALIB(value)     (OSC32KCTRL_OSCULP32K_CALIB_Msk & ((value) << OSC32KCTRL_OSCULP32K_CALIB_Pos))
#define OSC32KCTRL_OSCULP32K_WRTLOCK_Pos      (15U)                                          /**< (OSC32KCTRL_OSCULP32K) Write Lock Position */
#define OSC32KCTRL_OSCULP32K_WRTLOCK_Msk      (0x1U << OSC32KCTRL_OSCULP32K_WRTLOCK_Pos)     /**< (OSC32KCTRL_OSCULP32K) Write Lock Mask */
#define OSC32KCTRL_OSCULP32K_WRTLOCK(value)   (OSC32KCTRL_OSCULP32K_WRTLOCK_Msk & ((value) << OSC32KCTRL_OSCULP32K_WRTLOCK_Pos))
#define OSC32KCTRL_OSCULP32K_Msk              (0x00009F00UL)                                 /**< (OSC32KCTRL_OSCULP32K) Register Mask  */

/** \brief OSC32KCTRL register offsets definitions */
#define OSC32KCTRL_INTENCLR_OFFSET     (0x00)         /**< (OSC32KCTRL_INTENCLR) Interrupt Enable Clear Offset */
#define OSC32KCTRL_INTENSET_OFFSET     (0x04)         /**< (OSC32KCTRL_INTENSET) Interrupt Enable Set Offset */
#define OSC32KCTRL_INTFLAG_OFFSET      (0x08)         /**< (OSC32KCTRL_INTFLAG) Interrupt Flag Status and Clear Offset */
#define OSC32KCTRL_STATUS_OFFSET       (0x0C)         /**< (OSC32KCTRL_STATUS) Power and Clocks Status Offset */
#define OSC32KCTRL_RTCCTRL_OFFSET      (0x10)         /**< (OSC32KCTRL_RTCCTRL) Clock selection Offset */
#define OSC32KCTRL_XOSC32K_OFFSET      (0x14)         /**< (OSC32KCTRL_XOSC32K) 32kHz External Crystal Oscillator (XOSC32K) Control Offset */
#define OSC32KCTRL_CFDCTRL_OFFSET      (0x16)         /**< (OSC32KCTRL_CFDCTRL) Clock Failure Detector Control Offset */
#define OSC32KCTRL_EVCTRL_OFFSET       (0x17)         /**< (OSC32KCTRL_EVCTRL) Event Control Offset */
#define OSC32KCTRL_OSC32K_OFFSET       (0x18)         /**< (OSC32KCTRL_OSC32K) 32kHz Internal Oscillator (OSC32K) Control Offset */
#define OSC32KCTRL_OSCULP32K_OFFSET    (0x1C)         /**< (OSC32KCTRL_OSCULP32K) 32kHz Ultra Low Power Internal Oscillator (OSCULP32K) Control Offset */

/** \brief OSC32KCTRL register API structure */
typedef struct
{
  __IO  uint32_t                       OSC32KCTRL_INTENCLR; /**< Offset: 0x00 (R/W  32) Interrupt Enable Clear */
  __IO  uint32_t                       OSC32KCTRL_INTENSET; /**< Offset: 0x04 (R/W  32) Interrupt Enable Set */
  __IO  uint32_t                       OSC32KCTRL_INTFLAG; /**< Offset: 0x08 (R/W  32) Interrupt Flag Status and Clear */
  __I   uint32_t                       OSC32KCTRL_STATUS; /**< Offset: 0x0c (R/   32) Power and Clocks Status */
  __IO  uint32_t                       OSC32KCTRL_RTCCTRL; /**< Offset: 0x10 (R/W  32) Clock selection */
  __IO  uint16_t                       OSC32KCTRL_XOSC32K; /**< Offset: 0x14 (R/W  16) 32kHz External Crystal Oscillator (XOSC32K) Control */
  __IO  uint8_t                        OSC32KCTRL_CFDCTRL; /**< Offset: 0x16 (R/W  8) Clock Failure Detector Control */
  __IO  uint8_t                        OSC32KCTRL_EVCTRL; /**< Offset: 0x17 (R/W  8) Event Control */
  __IO  uint32_t                       OSC32KCTRL_OSC32K; /**< Offset: 0x18 (R/W  32) 32kHz Internal Oscillator (OSC32K) Control */
  __IO  uint32_t                       OSC32KCTRL_OSCULP32K; /**< Offset: 0x1c (R/W  32) 32kHz Ultra Low Power Internal Oscillator (OSCULP32K) Control */
} osc32kctrl_registers_t;
/** @}  end of 32k Oscillators Control */

#endif /* SAMC_SAMC21_OSC32KCTRL_MODULE_H */

