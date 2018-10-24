/**
 * \brief Header file for SAMC/SAMC21 MCLK
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
#ifndef SAMC_SAMC21_MCLK_MODULE_H
#define SAMC_SAMC21_MCLK_MODULE_H

/** \addtogroup SAMC_SAMC21 Main Clock
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_MCLK                                  */
/* ========================================================================== */

/* -------- MCLK_INTENCLR : (MCLK Offset: 0x01) (R/W 8) Interrupt Enable Clear -------- */
#define MCLK_INTENCLR_CKRDY_Pos               (0U)                                           /**< (MCLK_INTENCLR) Clock Ready Interrupt Enable Position */
#define MCLK_INTENCLR_CKRDY_Msk               (0x1U << MCLK_INTENCLR_CKRDY_Pos)              /**< (MCLK_INTENCLR) Clock Ready Interrupt Enable Mask */
#define MCLK_INTENCLR_CKRDY(value)            (MCLK_INTENCLR_CKRDY_Msk & ((value) << MCLK_INTENCLR_CKRDY_Pos))
#define MCLK_INTENCLR_Msk                     (0x00000001UL)                                 /**< (MCLK_INTENCLR) Register Mask  */

/* -------- MCLK_INTENSET : (MCLK Offset: 0x02) (R/W 8) Interrupt Enable Set -------- */
#define MCLK_INTENSET_CKRDY_Pos               (0U)                                           /**< (MCLK_INTENSET) Clock Ready Interrupt Enable Position */
#define MCLK_INTENSET_CKRDY_Msk               (0x1U << MCLK_INTENSET_CKRDY_Pos)              /**< (MCLK_INTENSET) Clock Ready Interrupt Enable Mask */
#define MCLK_INTENSET_CKRDY(value)            (MCLK_INTENSET_CKRDY_Msk & ((value) << MCLK_INTENSET_CKRDY_Pos))
#define MCLK_INTENSET_Msk                     (0x00000001UL)                                 /**< (MCLK_INTENSET) Register Mask  */

/* -------- MCLK_INTFLAG : (MCLK Offset: 0x03) (R/W 8) Interrupt Flag Status and Clear -------- */
#define MCLK_INTFLAG_CKRDY_Pos                (0U)                                           /**< (MCLK_INTFLAG) Clock Ready Position */
#define MCLK_INTFLAG_CKRDY_Msk                (0x1U << MCLK_INTFLAG_CKRDY_Pos)               /**< (MCLK_INTFLAG) Clock Ready Mask */
#define MCLK_INTFLAG_CKRDY(value)             (MCLK_INTFLAG_CKRDY_Msk & ((value) << MCLK_INTFLAG_CKRDY_Pos))
#define MCLK_INTFLAG_Msk                      (0x00000001UL)                                 /**< (MCLK_INTFLAG) Register Mask  */

/* -------- MCLK_CPUDIV : (MCLK Offset: 0x04) (R/W 8) CPU Clock Division -------- */
#define MCLK_CPUDIV_CPUDIV_Pos                (0U)                                           /**< (MCLK_CPUDIV) CPU Clock Division Factor Position */
#define MCLK_CPUDIV_CPUDIV_Msk                (0xFFU << MCLK_CPUDIV_CPUDIV_Pos)              /**< (MCLK_CPUDIV) CPU Clock Division Factor Mask */
#define MCLK_CPUDIV_CPUDIV(value)             (MCLK_CPUDIV_CPUDIV_Msk & ((value) << MCLK_CPUDIV_CPUDIV_Pos))
#define   MCLK_CPUDIV_CPUDIV_DIV1_Val         (1U)                                           /**< (MCLK_CPUDIV) Divide by 1  */
#define   MCLK_CPUDIV_CPUDIV_DIV2_Val         (2U)                                           /**< (MCLK_CPUDIV) Divide by 2  */
#define   MCLK_CPUDIV_CPUDIV_DIV4_Val         (4U)                                           /**< (MCLK_CPUDIV) Divide by 4  */
#define   MCLK_CPUDIV_CPUDIV_DIV8_Val         (8U)                                           /**< (MCLK_CPUDIV) Divide by 8  */
#define   MCLK_CPUDIV_CPUDIV_DIV16_Val        (16U)                                          /**< (MCLK_CPUDIV) Divide by 16  */
#define   MCLK_CPUDIV_CPUDIV_DIV32_Val        (32U)                                          /**< (MCLK_CPUDIV) Divide by 32  */
#define   MCLK_CPUDIV_CPUDIV_DIV64_Val        (64U)                                          /**< (MCLK_CPUDIV) Divide by 64  */
#define   MCLK_CPUDIV_CPUDIV_DIV128_Val       (128U)                                         /**< (MCLK_CPUDIV) Divide by 128  */
#define MCLK_CPUDIV_CPUDIV_DIV1               (MCLK_CPUDIV_CPUDIV_DIV1_Val << MCLK_CPUDIV_CPUDIV_Pos) /**< (MCLK_CPUDIV) Divide by 1 Position  */
#define MCLK_CPUDIV_CPUDIV_DIV2               (MCLK_CPUDIV_CPUDIV_DIV2_Val << MCLK_CPUDIV_CPUDIV_Pos) /**< (MCLK_CPUDIV) Divide by 2 Position  */
#define MCLK_CPUDIV_CPUDIV_DIV4               (MCLK_CPUDIV_CPUDIV_DIV4_Val << MCLK_CPUDIV_CPUDIV_Pos) /**< (MCLK_CPUDIV) Divide by 4 Position  */
#define MCLK_CPUDIV_CPUDIV_DIV8               (MCLK_CPUDIV_CPUDIV_DIV8_Val << MCLK_CPUDIV_CPUDIV_Pos) /**< (MCLK_CPUDIV) Divide by 8 Position  */
#define MCLK_CPUDIV_CPUDIV_DIV16              (MCLK_CPUDIV_CPUDIV_DIV16_Val << MCLK_CPUDIV_CPUDIV_Pos) /**< (MCLK_CPUDIV) Divide by 16 Position  */
#define MCLK_CPUDIV_CPUDIV_DIV32              (MCLK_CPUDIV_CPUDIV_DIV32_Val << MCLK_CPUDIV_CPUDIV_Pos) /**< (MCLK_CPUDIV) Divide by 32 Position  */
#define MCLK_CPUDIV_CPUDIV_DIV64              (MCLK_CPUDIV_CPUDIV_DIV64_Val << MCLK_CPUDIV_CPUDIV_Pos) /**< (MCLK_CPUDIV) Divide by 64 Position  */
#define MCLK_CPUDIV_CPUDIV_DIV128             (MCLK_CPUDIV_CPUDIV_DIV128_Val << MCLK_CPUDIV_CPUDIV_Pos) /**< (MCLK_CPUDIV) Divide by 128 Position  */
#define MCLK_CPUDIV_Msk                       (0x000000FFUL)                                 /**< (MCLK_CPUDIV) Register Mask  */

/* -------- MCLK_AHBMASK : (MCLK Offset: 0x10) (R/W 32) AHB Mask -------- */
#define MCLK_AHBMASK_HPB0__Pos                (0U)                                           /**< (MCLK_AHBMASK) HPB0 AHB Clock Mask Position */
#define MCLK_AHBMASK_HPB0__Msk                (0x1U << MCLK_AHBMASK_HPB0__Pos)               /**< (MCLK_AHBMASK) HPB0 AHB Clock Mask Mask */
#define MCLK_AHBMASK_HPB0_(value)             (MCLK_AHBMASK_HPB0__Msk & ((value) << MCLK_AHBMASK_HPB0__Pos))
#define MCLK_AHBMASK_HPB1__Pos                (1U)                                           /**< (MCLK_AHBMASK) HPB1 AHB Clock Mask Position */
#define MCLK_AHBMASK_HPB1__Msk                (0x1U << MCLK_AHBMASK_HPB1__Pos)               /**< (MCLK_AHBMASK) HPB1 AHB Clock Mask Mask */
#define MCLK_AHBMASK_HPB1_(value)             (MCLK_AHBMASK_HPB1__Msk & ((value) << MCLK_AHBMASK_HPB1__Pos))
#define MCLK_AHBMASK_HPB2__Pos                (2U)                                           /**< (MCLK_AHBMASK) HPB2 AHB Clock Mask Position */
#define MCLK_AHBMASK_HPB2__Msk                (0x1U << MCLK_AHBMASK_HPB2__Pos)               /**< (MCLK_AHBMASK) HPB2 AHB Clock Mask Mask */
#define MCLK_AHBMASK_HPB2_(value)             (MCLK_AHBMASK_HPB2__Msk & ((value) << MCLK_AHBMASK_HPB2__Pos))
#define MCLK_AHBMASK_DSU__Pos                 (3U)                                           /**< (MCLK_AHBMASK) DSU AHB Clock Mask Position */
#define MCLK_AHBMASK_DSU__Msk                 (0x1U << MCLK_AHBMASK_DSU__Pos)                /**< (MCLK_AHBMASK) DSU AHB Clock Mask Mask */
#define MCLK_AHBMASK_DSU_(value)              (MCLK_AHBMASK_DSU__Msk & ((value) << MCLK_AHBMASK_DSU__Pos))
#define MCLK_AHBMASK_HMATRIXHS__Pos           (4U)                                           /**< (MCLK_AHBMASK) HMATRIXHS AHB Clock Mask Position */
#define MCLK_AHBMASK_HMATRIXHS__Msk           (0x1U << MCLK_AHBMASK_HMATRIXHS__Pos)          /**< (MCLK_AHBMASK) HMATRIXHS AHB Clock Mask Mask */
#define MCLK_AHBMASK_HMATRIXHS_(value)        (MCLK_AHBMASK_HMATRIXHS__Msk & ((value) << MCLK_AHBMASK_HMATRIXHS__Pos))
#define MCLK_AHBMASK_NVMCTRL__Pos             (5U)                                           /**< (MCLK_AHBMASK) NVMCTRL AHB Clock Mask Position */
#define MCLK_AHBMASK_NVMCTRL__Msk             (0x1U << MCLK_AHBMASK_NVMCTRL__Pos)            /**< (MCLK_AHBMASK) NVMCTRL AHB Clock Mask Mask */
#define MCLK_AHBMASK_NVMCTRL_(value)          (MCLK_AHBMASK_NVMCTRL__Msk & ((value) << MCLK_AHBMASK_NVMCTRL__Pos))
#define MCLK_AHBMASK_HSRAM__Pos               (6U)                                           /**< (MCLK_AHBMASK) HSRAM AHB Clock Mask Position */
#define MCLK_AHBMASK_HSRAM__Msk               (0x1U << MCLK_AHBMASK_HSRAM__Pos)              /**< (MCLK_AHBMASK) HSRAM AHB Clock Mask Mask */
#define MCLK_AHBMASK_HSRAM_(value)            (MCLK_AHBMASK_HSRAM__Msk & ((value) << MCLK_AHBMASK_HSRAM__Pos))
#define MCLK_AHBMASK_DMAC__Pos                (7U)                                           /**< (MCLK_AHBMASK) DMAC AHB Clock Mask Position */
#define MCLK_AHBMASK_DMAC__Msk                (0x1U << MCLK_AHBMASK_DMAC__Pos)               /**< (MCLK_AHBMASK) DMAC AHB Clock Mask Mask */
#define MCLK_AHBMASK_DMAC_(value)             (MCLK_AHBMASK_DMAC__Msk & ((value) << MCLK_AHBMASK_DMAC__Pos))
#define MCLK_AHBMASK_CAN0__Pos                (8U)                                           /**< (MCLK_AHBMASK) CAN0 AHB Clock Mask Position */
#define MCLK_AHBMASK_CAN0__Msk                (0x1U << MCLK_AHBMASK_CAN0__Pos)               /**< (MCLK_AHBMASK) CAN0 AHB Clock Mask Mask */
#define MCLK_AHBMASK_CAN0_(value)             (MCLK_AHBMASK_CAN0__Msk & ((value) << MCLK_AHBMASK_CAN0__Pos))
#define MCLK_AHBMASK_CAN1__Pos                (9U)                                           /**< (MCLK_AHBMASK) CAN1 AHB Clock Mask Position */
#define MCLK_AHBMASK_CAN1__Msk                (0x1U << MCLK_AHBMASK_CAN1__Pos)               /**< (MCLK_AHBMASK) CAN1 AHB Clock Mask Mask */
#define MCLK_AHBMASK_CAN1_(value)             (MCLK_AHBMASK_CAN1__Msk & ((value) << MCLK_AHBMASK_CAN1__Pos))
#define MCLK_AHBMASK_PAC__Pos                 (10U)                                          /**< (MCLK_AHBMASK) PAC AHB Clock Mask Position */
#define MCLK_AHBMASK_PAC__Msk                 (0x1U << MCLK_AHBMASK_PAC__Pos)                /**< (MCLK_AHBMASK) PAC AHB Clock Mask Mask */
#define MCLK_AHBMASK_PAC_(value)              (MCLK_AHBMASK_PAC__Msk & ((value) << MCLK_AHBMASK_PAC__Pos))
#define MCLK_AHBMASK_NVMCTRL_PICACHU__Pos     (11U)                                          /**< (MCLK_AHBMASK) NVMCTRL_PICACHU AHB Clock Mask Position */
#define MCLK_AHBMASK_NVMCTRL_PICACHU__Msk     (0x1U << MCLK_AHBMASK_NVMCTRL_PICACHU__Pos)    /**< (MCLK_AHBMASK) NVMCTRL_PICACHU AHB Clock Mask Mask */
#define MCLK_AHBMASK_NVMCTRL_PICACHU_(value)  (MCLK_AHBMASK_NVMCTRL_PICACHU__Msk & ((value) << MCLK_AHBMASK_NVMCTRL_PICACHU__Pos))
#define MCLK_AHBMASK_DIVAS__Pos               (12U)                                          /**< (MCLK_AHBMASK) DIVAS AHB Clock Mask Position */
#define MCLK_AHBMASK_DIVAS__Msk               (0x1U << MCLK_AHBMASK_DIVAS__Pos)              /**< (MCLK_AHBMASK) DIVAS AHB Clock Mask Mask */
#define MCLK_AHBMASK_DIVAS_(value)            (MCLK_AHBMASK_DIVAS__Msk & ((value) << MCLK_AHBMASK_DIVAS__Pos))
#define MCLK_AHBMASK_HPB3__Pos                (13U)                                          /**< (MCLK_AHBMASK) HPB3 AHB Clock Mask Position */
#define MCLK_AHBMASK_HPB3__Msk                (0x1U << MCLK_AHBMASK_HPB3__Pos)               /**< (MCLK_AHBMASK) HPB3 AHB Clock Mask Mask */
#define MCLK_AHBMASK_HPB3_(value)             (MCLK_AHBMASK_HPB3__Msk & ((value) << MCLK_AHBMASK_HPB3__Pos))
#define MCLK_AHBMASK_Msk                      (0x00003FFFUL)                                 /**< (MCLK_AHBMASK) Register Mask  */

/* -------- MCLK_APBAMASK : (MCLK Offset: 0x14) (R/W 32) APBA Mask -------- */
#define MCLK_APBAMASK_PAC__Pos                (0U)                                           /**< (MCLK_APBAMASK) PAC APB Clock Enable Position */
#define MCLK_APBAMASK_PAC__Msk                (0x1U << MCLK_APBAMASK_PAC__Pos)               /**< (MCLK_APBAMASK) PAC APB Clock Enable Mask */
#define MCLK_APBAMASK_PAC_(value)             (MCLK_APBAMASK_PAC__Msk & ((value) << MCLK_APBAMASK_PAC__Pos))
#define MCLK_APBAMASK_PM__Pos                 (1U)                                           /**< (MCLK_APBAMASK) PM APB Clock Enable Position */
#define MCLK_APBAMASK_PM__Msk                 (0x1U << MCLK_APBAMASK_PM__Pos)                /**< (MCLK_APBAMASK) PM APB Clock Enable Mask */
#define MCLK_APBAMASK_PM_(value)              (MCLK_APBAMASK_PM__Msk & ((value) << MCLK_APBAMASK_PM__Pos))
#define MCLK_APBAMASK_MCLK__Pos               (2U)                                           /**< (MCLK_APBAMASK) MCLK APB Clock Enable Position */
#define MCLK_APBAMASK_MCLK__Msk               (0x1U << MCLK_APBAMASK_MCLK__Pos)              /**< (MCLK_APBAMASK) MCLK APB Clock Enable Mask */
#define MCLK_APBAMASK_MCLK_(value)            (MCLK_APBAMASK_MCLK__Msk & ((value) << MCLK_APBAMASK_MCLK__Pos))
#define MCLK_APBAMASK_RSTC__Pos               (3U)                                           /**< (MCLK_APBAMASK) RSTC APB Clock Enable Position */
#define MCLK_APBAMASK_RSTC__Msk               (0x1U << MCLK_APBAMASK_RSTC__Pos)              /**< (MCLK_APBAMASK) RSTC APB Clock Enable Mask */
#define MCLK_APBAMASK_RSTC_(value)            (MCLK_APBAMASK_RSTC__Msk & ((value) << MCLK_APBAMASK_RSTC__Pos))
#define MCLK_APBAMASK_OSCCTRL__Pos            (4U)                                           /**< (MCLK_APBAMASK) OSCCTRL APB Clock Enable Position */
#define MCLK_APBAMASK_OSCCTRL__Msk            (0x1U << MCLK_APBAMASK_OSCCTRL__Pos)           /**< (MCLK_APBAMASK) OSCCTRL APB Clock Enable Mask */
#define MCLK_APBAMASK_OSCCTRL_(value)         (MCLK_APBAMASK_OSCCTRL__Msk & ((value) << MCLK_APBAMASK_OSCCTRL__Pos))
#define MCLK_APBAMASK_OSC32KCTRL__Pos         (5U)                                           /**< (MCLK_APBAMASK) OSC32KCTRL APB Clock Enable Position */
#define MCLK_APBAMASK_OSC32KCTRL__Msk         (0x1U << MCLK_APBAMASK_OSC32KCTRL__Pos)        /**< (MCLK_APBAMASK) OSC32KCTRL APB Clock Enable Mask */
#define MCLK_APBAMASK_OSC32KCTRL_(value)      (MCLK_APBAMASK_OSC32KCTRL__Msk & ((value) << MCLK_APBAMASK_OSC32KCTRL__Pos))
#define MCLK_APBAMASK_SUPC__Pos               (6U)                                           /**< (MCLK_APBAMASK) SUPC APB Clock Enable Position */
#define MCLK_APBAMASK_SUPC__Msk               (0x1U << MCLK_APBAMASK_SUPC__Pos)              /**< (MCLK_APBAMASK) SUPC APB Clock Enable Mask */
#define MCLK_APBAMASK_SUPC_(value)            (MCLK_APBAMASK_SUPC__Msk & ((value) << MCLK_APBAMASK_SUPC__Pos))
#define MCLK_APBAMASK_GCLK__Pos               (7U)                                           /**< (MCLK_APBAMASK) GCLK APB Clock Enable Position */
#define MCLK_APBAMASK_GCLK__Msk               (0x1U << MCLK_APBAMASK_GCLK__Pos)              /**< (MCLK_APBAMASK) GCLK APB Clock Enable Mask */
#define MCLK_APBAMASK_GCLK_(value)            (MCLK_APBAMASK_GCLK__Msk & ((value) << MCLK_APBAMASK_GCLK__Pos))
#define MCLK_APBAMASK_WDT__Pos                (8U)                                           /**< (MCLK_APBAMASK) WDT APB Clock Enable Position */
#define MCLK_APBAMASK_WDT__Msk                (0x1U << MCLK_APBAMASK_WDT__Pos)               /**< (MCLK_APBAMASK) WDT APB Clock Enable Mask */
#define MCLK_APBAMASK_WDT_(value)             (MCLK_APBAMASK_WDT__Msk & ((value) << MCLK_APBAMASK_WDT__Pos))
#define MCLK_APBAMASK_RTC__Pos                (9U)                                           /**< (MCLK_APBAMASK) RTC APB Clock Enable Position */
#define MCLK_APBAMASK_RTC__Msk                (0x1U << MCLK_APBAMASK_RTC__Pos)               /**< (MCLK_APBAMASK) RTC APB Clock Enable Mask */
#define MCLK_APBAMASK_RTC_(value)             (MCLK_APBAMASK_RTC__Msk & ((value) << MCLK_APBAMASK_RTC__Pos))
#define MCLK_APBAMASK_EIC__Pos                (10U)                                          /**< (MCLK_APBAMASK) EIC APB Clock Enable Position */
#define MCLK_APBAMASK_EIC__Msk                (0x1U << MCLK_APBAMASK_EIC__Pos)               /**< (MCLK_APBAMASK) EIC APB Clock Enable Mask */
#define MCLK_APBAMASK_EIC_(value)             (MCLK_APBAMASK_EIC__Msk & ((value) << MCLK_APBAMASK_EIC__Pos))
#define MCLK_APBAMASK_FREQM__Pos              (11U)                                          /**< (MCLK_APBAMASK) FREQM APB Clock Enable Position */
#define MCLK_APBAMASK_FREQM__Msk              (0x1U << MCLK_APBAMASK_FREQM__Pos)             /**< (MCLK_APBAMASK) FREQM APB Clock Enable Mask */
#define MCLK_APBAMASK_FREQM_(value)           (MCLK_APBAMASK_FREQM__Msk & ((value) << MCLK_APBAMASK_FREQM__Pos))
#define MCLK_APBAMASK_TSENS__Pos              (12U)                                          /**< (MCLK_APBAMASK) TSENS APB Clock Enable Position */
#define MCLK_APBAMASK_TSENS__Msk              (0x1U << MCLK_APBAMASK_TSENS__Pos)             /**< (MCLK_APBAMASK) TSENS APB Clock Enable Mask */
#define MCLK_APBAMASK_TSENS_(value)           (MCLK_APBAMASK_TSENS__Msk & ((value) << MCLK_APBAMASK_TSENS__Pos))
#define MCLK_APBAMASK_Msk                     (0x00001FFFUL)                                 /**< (MCLK_APBAMASK) Register Mask  */

/* -------- MCLK_APBBMASK : (MCLK Offset: 0x18) (R/W 32) APBB Mask -------- */
#define MCLK_APBBMASK_PORT__Pos               (0U)                                           /**< (MCLK_APBBMASK) PORT APB Clock Enable Position */
#define MCLK_APBBMASK_PORT__Msk               (0x1U << MCLK_APBBMASK_PORT__Pos)              /**< (MCLK_APBBMASK) PORT APB Clock Enable Mask */
#define MCLK_APBBMASK_PORT_(value)            (MCLK_APBBMASK_PORT__Msk & ((value) << MCLK_APBBMASK_PORT__Pos))
#define MCLK_APBBMASK_DSU__Pos                (1U)                                           /**< (MCLK_APBBMASK) DSU APB Clock Enable Position */
#define MCLK_APBBMASK_DSU__Msk                (0x1U << MCLK_APBBMASK_DSU__Pos)               /**< (MCLK_APBBMASK) DSU APB Clock Enable Mask */
#define MCLK_APBBMASK_DSU_(value)             (MCLK_APBBMASK_DSU__Msk & ((value) << MCLK_APBBMASK_DSU__Pos))
#define MCLK_APBBMASK_NVMCTRL__Pos            (2U)                                           /**< (MCLK_APBBMASK) NVMCTRL APB Clock Enable Position */
#define MCLK_APBBMASK_NVMCTRL__Msk            (0x1U << MCLK_APBBMASK_NVMCTRL__Pos)           /**< (MCLK_APBBMASK) NVMCTRL APB Clock Enable Mask */
#define MCLK_APBBMASK_NVMCTRL_(value)         (MCLK_APBBMASK_NVMCTRL__Msk & ((value) << MCLK_APBBMASK_NVMCTRL__Pos))
#define MCLK_APBBMASK_HMATRIXHS__Pos          (5U)                                           /**< (MCLK_APBBMASK) HMATRIXHS APB Clock Enable Position */
#define MCLK_APBBMASK_HMATRIXHS__Msk          (0x1U << MCLK_APBBMASK_HMATRIXHS__Pos)         /**< (MCLK_APBBMASK) HMATRIXHS APB Clock Enable Mask */
#define MCLK_APBBMASK_HMATRIXHS_(value)       (MCLK_APBBMASK_HMATRIXHS__Msk & ((value) << MCLK_APBBMASK_HMATRIXHS__Pos))
#define MCLK_APBBMASK_Msk                     (0x00000027UL)                                 /**< (MCLK_APBBMASK) Register Mask  */

/* -------- MCLK_APBCMASK : (MCLK Offset: 0x1C) (R/W 32) APBC Mask -------- */
#define MCLK_APBCMASK_EVSYS__Pos              (0U)                                           /**< (MCLK_APBCMASK) EVSYS APB Clock Enable Position */
#define MCLK_APBCMASK_EVSYS__Msk              (0x1U << MCLK_APBCMASK_EVSYS__Pos)             /**< (MCLK_APBCMASK) EVSYS APB Clock Enable Mask */
#define MCLK_APBCMASK_EVSYS_(value)           (MCLK_APBCMASK_EVSYS__Msk & ((value) << MCLK_APBCMASK_EVSYS__Pos))
#define MCLK_APBCMASK_SERCOM0__Pos            (1U)                                           /**< (MCLK_APBCMASK) SERCOM0 APB Clock Enable Position */
#define MCLK_APBCMASK_SERCOM0__Msk            (0x1U << MCLK_APBCMASK_SERCOM0__Pos)           /**< (MCLK_APBCMASK) SERCOM0 APB Clock Enable Mask */
#define MCLK_APBCMASK_SERCOM0_(value)         (MCLK_APBCMASK_SERCOM0__Msk & ((value) << MCLK_APBCMASK_SERCOM0__Pos))
#define MCLK_APBCMASK_SERCOM1__Pos            (2U)                                           /**< (MCLK_APBCMASK) SERCOM1 APB Clock Enable Position */
#define MCLK_APBCMASK_SERCOM1__Msk            (0x1U << MCLK_APBCMASK_SERCOM1__Pos)           /**< (MCLK_APBCMASK) SERCOM1 APB Clock Enable Mask */
#define MCLK_APBCMASK_SERCOM1_(value)         (MCLK_APBCMASK_SERCOM1__Msk & ((value) << MCLK_APBCMASK_SERCOM1__Pos))
#define MCLK_APBCMASK_SERCOM2__Pos            (3U)                                           /**< (MCLK_APBCMASK) SERCOM2 APB Clock Enable Position */
#define MCLK_APBCMASK_SERCOM2__Msk            (0x1U << MCLK_APBCMASK_SERCOM2__Pos)           /**< (MCLK_APBCMASK) SERCOM2 APB Clock Enable Mask */
#define MCLK_APBCMASK_SERCOM2_(value)         (MCLK_APBCMASK_SERCOM2__Msk & ((value) << MCLK_APBCMASK_SERCOM2__Pos))
#define MCLK_APBCMASK_SERCOM3__Pos            (4U)                                           /**< (MCLK_APBCMASK) SERCOM3 APB Clock Enable Position */
#define MCLK_APBCMASK_SERCOM3__Msk            (0x1U << MCLK_APBCMASK_SERCOM3__Pos)           /**< (MCLK_APBCMASK) SERCOM3 APB Clock Enable Mask */
#define MCLK_APBCMASK_SERCOM3_(value)         (MCLK_APBCMASK_SERCOM3__Msk & ((value) << MCLK_APBCMASK_SERCOM3__Pos))
#define MCLK_APBCMASK_SERCOM4__Pos            (5U)                                           /**< (MCLK_APBCMASK) SERCOM4 APB Clock Enable Position */
#define MCLK_APBCMASK_SERCOM4__Msk            (0x1U << MCLK_APBCMASK_SERCOM4__Pos)           /**< (MCLK_APBCMASK) SERCOM4 APB Clock Enable Mask */
#define MCLK_APBCMASK_SERCOM4_(value)         (MCLK_APBCMASK_SERCOM4__Msk & ((value) << MCLK_APBCMASK_SERCOM4__Pos))
#define MCLK_APBCMASK_SERCOM5__Pos            (6U)                                           /**< (MCLK_APBCMASK) SERCOM5 APB Clock Enable Position */
#define MCLK_APBCMASK_SERCOM5__Msk            (0x1U << MCLK_APBCMASK_SERCOM5__Pos)           /**< (MCLK_APBCMASK) SERCOM5 APB Clock Enable Mask */
#define MCLK_APBCMASK_SERCOM5_(value)         (MCLK_APBCMASK_SERCOM5__Msk & ((value) << MCLK_APBCMASK_SERCOM5__Pos))
#define MCLK_APBCMASK_TCC0__Pos               (9U)                                           /**< (MCLK_APBCMASK) TCC0 APB Clock Enable Position */
#define MCLK_APBCMASK_TCC0__Msk               (0x1U << MCLK_APBCMASK_TCC0__Pos)              /**< (MCLK_APBCMASK) TCC0 APB Clock Enable Mask */
#define MCLK_APBCMASK_TCC0_(value)            (MCLK_APBCMASK_TCC0__Msk & ((value) << MCLK_APBCMASK_TCC0__Pos))
#define MCLK_APBCMASK_TCC1__Pos               (10U)                                          /**< (MCLK_APBCMASK) TCC1 APB Clock Enable Position */
#define MCLK_APBCMASK_TCC1__Msk               (0x1U << MCLK_APBCMASK_TCC1__Pos)              /**< (MCLK_APBCMASK) TCC1 APB Clock Enable Mask */
#define MCLK_APBCMASK_TCC1_(value)            (MCLK_APBCMASK_TCC1__Msk & ((value) << MCLK_APBCMASK_TCC1__Pos))
#define MCLK_APBCMASK_TCC2__Pos               (11U)                                          /**< (MCLK_APBCMASK) TCC2 APB Clock Enable Position */
#define MCLK_APBCMASK_TCC2__Msk               (0x1U << MCLK_APBCMASK_TCC2__Pos)              /**< (MCLK_APBCMASK) TCC2 APB Clock Enable Mask */
#define MCLK_APBCMASK_TCC2_(value)            (MCLK_APBCMASK_TCC2__Msk & ((value) << MCLK_APBCMASK_TCC2__Pos))
#define MCLK_APBCMASK_TC0__Pos                (12U)                                          /**< (MCLK_APBCMASK) TC0 APB Clock Enable Position */
#define MCLK_APBCMASK_TC0__Msk                (0x1U << MCLK_APBCMASK_TC0__Pos)               /**< (MCLK_APBCMASK) TC0 APB Clock Enable Mask */
#define MCLK_APBCMASK_TC0_(value)             (MCLK_APBCMASK_TC0__Msk & ((value) << MCLK_APBCMASK_TC0__Pos))
#define MCLK_APBCMASK_TC1__Pos                (13U)                                          /**< (MCLK_APBCMASK) TC1 APB Clock Enable Position */
#define MCLK_APBCMASK_TC1__Msk                (0x1U << MCLK_APBCMASK_TC1__Pos)               /**< (MCLK_APBCMASK) TC1 APB Clock Enable Mask */
#define MCLK_APBCMASK_TC1_(value)             (MCLK_APBCMASK_TC1__Msk & ((value) << MCLK_APBCMASK_TC1__Pos))
#define MCLK_APBCMASK_TC2__Pos                (14U)                                          /**< (MCLK_APBCMASK) TC2 APB Clock Enable Position */
#define MCLK_APBCMASK_TC2__Msk                (0x1U << MCLK_APBCMASK_TC2__Pos)               /**< (MCLK_APBCMASK) TC2 APB Clock Enable Mask */
#define MCLK_APBCMASK_TC2_(value)             (MCLK_APBCMASK_TC2__Msk & ((value) << MCLK_APBCMASK_TC2__Pos))
#define MCLK_APBCMASK_TC3__Pos                (15U)                                          /**< (MCLK_APBCMASK) TC3 APB Clock Enable Position */
#define MCLK_APBCMASK_TC3__Msk                (0x1U << MCLK_APBCMASK_TC3__Pos)               /**< (MCLK_APBCMASK) TC3 APB Clock Enable Mask */
#define MCLK_APBCMASK_TC3_(value)             (MCLK_APBCMASK_TC3__Msk & ((value) << MCLK_APBCMASK_TC3__Pos))
#define MCLK_APBCMASK_TC4__Pos                (16U)                                          /**< (MCLK_APBCMASK) TC4 APB Clock Enable Position */
#define MCLK_APBCMASK_TC4__Msk                (0x1U << MCLK_APBCMASK_TC4__Pos)               /**< (MCLK_APBCMASK) TC4 APB Clock Enable Mask */
#define MCLK_APBCMASK_TC4_(value)             (MCLK_APBCMASK_TC4__Msk & ((value) << MCLK_APBCMASK_TC4__Pos))
#define MCLK_APBCMASK_ADC0__Pos               (17U)                                          /**< (MCLK_APBCMASK) ADC0 APB Clock Enable Position */
#define MCLK_APBCMASK_ADC0__Msk               (0x1U << MCLK_APBCMASK_ADC0__Pos)              /**< (MCLK_APBCMASK) ADC0 APB Clock Enable Mask */
#define MCLK_APBCMASK_ADC0_(value)            (MCLK_APBCMASK_ADC0__Msk & ((value) << MCLK_APBCMASK_ADC0__Pos))
#define MCLK_APBCMASK_ADC1__Pos               (18U)                                          /**< (MCLK_APBCMASK) ADC1 APB Clock Enable Position */
#define MCLK_APBCMASK_ADC1__Msk               (0x1U << MCLK_APBCMASK_ADC1__Pos)              /**< (MCLK_APBCMASK) ADC1 APB Clock Enable Mask */
#define MCLK_APBCMASK_ADC1_(value)            (MCLK_APBCMASK_ADC1__Msk & ((value) << MCLK_APBCMASK_ADC1__Pos))
#define MCLK_APBCMASK_SDADC__Pos              (19U)                                          /**< (MCLK_APBCMASK) SDADC APB Clock Enable Position */
#define MCLK_APBCMASK_SDADC__Msk              (0x1U << MCLK_APBCMASK_SDADC__Pos)             /**< (MCLK_APBCMASK) SDADC APB Clock Enable Mask */
#define MCLK_APBCMASK_SDADC_(value)           (MCLK_APBCMASK_SDADC__Msk & ((value) << MCLK_APBCMASK_SDADC__Pos))
#define MCLK_APBCMASK_AC__Pos                 (20U)                                          /**< (MCLK_APBCMASK) AC APB Clock Enable Position */
#define MCLK_APBCMASK_AC__Msk                 (0x1U << MCLK_APBCMASK_AC__Pos)                /**< (MCLK_APBCMASK) AC APB Clock Enable Mask */
#define MCLK_APBCMASK_AC_(value)              (MCLK_APBCMASK_AC__Msk & ((value) << MCLK_APBCMASK_AC__Pos))
#define MCLK_APBCMASK_DAC__Pos                (21U)                                          /**< (MCLK_APBCMASK) DAC APB Clock Enable Position */
#define MCLK_APBCMASK_DAC__Msk                (0x1U << MCLK_APBCMASK_DAC__Pos)               /**< (MCLK_APBCMASK) DAC APB Clock Enable Mask */
#define MCLK_APBCMASK_DAC_(value)             (MCLK_APBCMASK_DAC__Msk & ((value) << MCLK_APBCMASK_DAC__Pos))
#define MCLK_APBCMASK_PTC__Pos                (22U)                                          /**< (MCLK_APBCMASK) PTC APB Clock Enable Position */
#define MCLK_APBCMASK_PTC__Msk                (0x1U << MCLK_APBCMASK_PTC__Pos)               /**< (MCLK_APBCMASK) PTC APB Clock Enable Mask */
#define MCLK_APBCMASK_PTC_(value)             (MCLK_APBCMASK_PTC__Msk & ((value) << MCLK_APBCMASK_PTC__Pos))
#define MCLK_APBCMASK_CCL__Pos                (23U)                                          /**< (MCLK_APBCMASK) CCL APB Clock Enable Position */
#define MCLK_APBCMASK_CCL__Msk                (0x1U << MCLK_APBCMASK_CCL__Pos)               /**< (MCLK_APBCMASK) CCL APB Clock Enable Mask */
#define MCLK_APBCMASK_CCL_(value)             (MCLK_APBCMASK_CCL__Msk & ((value) << MCLK_APBCMASK_CCL__Pos))
#define MCLK_APBCMASK_Msk                     (0x00FFFE7FUL)                                 /**< (MCLK_APBCMASK) Register Mask  */

/* -------- MCLK_APBDMASK : (MCLK Offset: 0x20) (R/W 32) APBD Mask -------- */
#define MCLK_APBDMASK_SERCOM6__Pos            (0U)                                           /**< (MCLK_APBDMASK) SERCOM6 APB Clock Enable Position */
#define MCLK_APBDMASK_SERCOM6__Msk            (0x1U << MCLK_APBDMASK_SERCOM6__Pos)           /**< (MCLK_APBDMASK) SERCOM6 APB Clock Enable Mask */
#define MCLK_APBDMASK_SERCOM6_(value)         (MCLK_APBDMASK_SERCOM6__Msk & ((value) << MCLK_APBDMASK_SERCOM6__Pos))
#define MCLK_APBDMASK_SERCOM7__Pos            (1U)                                           /**< (MCLK_APBDMASK) SERCOM7 APB Clock Enable Position */
#define MCLK_APBDMASK_SERCOM7__Msk            (0x1U << MCLK_APBDMASK_SERCOM7__Pos)           /**< (MCLK_APBDMASK) SERCOM7 APB Clock Enable Mask */
#define MCLK_APBDMASK_SERCOM7_(value)         (MCLK_APBDMASK_SERCOM7__Msk & ((value) << MCLK_APBDMASK_SERCOM7__Pos))
#define MCLK_APBDMASK_TC5__Pos                (2U)                                           /**< (MCLK_APBDMASK) TC5 APB Clock Enable Position */
#define MCLK_APBDMASK_TC5__Msk                (0x1U << MCLK_APBDMASK_TC5__Pos)               /**< (MCLK_APBDMASK) TC5 APB Clock Enable Mask */
#define MCLK_APBDMASK_TC5_(value)             (MCLK_APBDMASK_TC5__Msk & ((value) << MCLK_APBDMASK_TC5__Pos))
#define MCLK_APBDMASK_TC6__Pos                (3U)                                           /**< (MCLK_APBDMASK) TC6 APB Clock Enable Position */
#define MCLK_APBDMASK_TC6__Msk                (0x1U << MCLK_APBDMASK_TC6__Pos)               /**< (MCLK_APBDMASK) TC6 APB Clock Enable Mask */
#define MCLK_APBDMASK_TC6_(value)             (MCLK_APBDMASK_TC6__Msk & ((value) << MCLK_APBDMASK_TC6__Pos))
#define MCLK_APBDMASK_TC7__Pos                (4U)                                           /**< (MCLK_APBDMASK) TC7 APB Clock Enable Position */
#define MCLK_APBDMASK_TC7__Msk                (0x1U << MCLK_APBDMASK_TC7__Pos)               /**< (MCLK_APBDMASK) TC7 APB Clock Enable Mask */
#define MCLK_APBDMASK_TC7_(value)             (MCLK_APBDMASK_TC7__Msk & ((value) << MCLK_APBDMASK_TC7__Pos))
#define MCLK_APBDMASK_Msk                     (0x0000001FUL)                                 /**< (MCLK_APBDMASK) Register Mask  */

/** \brief MCLK register offsets definitions */
#define MCLK_INTENCLR_OFFSET           (0x01)         /**< (MCLK_INTENCLR) Interrupt Enable Clear Offset */
#define MCLK_INTENSET_OFFSET           (0x02)         /**< (MCLK_INTENSET) Interrupt Enable Set Offset */
#define MCLK_INTFLAG_OFFSET            (0x03)         /**< (MCLK_INTFLAG) Interrupt Flag Status and Clear Offset */
#define MCLK_CPUDIV_OFFSET             (0x04)         /**< (MCLK_CPUDIV) CPU Clock Division Offset */
#define MCLK_AHBMASK_OFFSET            (0x10)         /**< (MCLK_AHBMASK) AHB Mask Offset */
#define MCLK_APBAMASK_OFFSET           (0x14)         /**< (MCLK_APBAMASK) APBA Mask Offset */
#define MCLK_APBBMASK_OFFSET           (0x18)         /**< (MCLK_APBBMASK) APBB Mask Offset */
#define MCLK_APBCMASK_OFFSET           (0x1C)         /**< (MCLK_APBCMASK) APBC Mask Offset */
#define MCLK_APBDMASK_OFFSET           (0x20)         /**< (MCLK_APBDMASK) APBD Mask Offset */

/** \brief MCLK register API structure */
typedef struct
{
  __I   uint8_t                        Reserved1[0x01];
  __IO  uint8_t                        MCLK_INTENCLR;   /**< Offset: 0x01 (R/W  8) Interrupt Enable Clear */
  __IO  uint8_t                        MCLK_INTENSET;   /**< Offset: 0x02 (R/W  8) Interrupt Enable Set */
  __IO  uint8_t                        MCLK_INTFLAG;    /**< Offset: 0x03 (R/W  8) Interrupt Flag Status and Clear */
  __IO  uint8_t                        MCLK_CPUDIV;     /**< Offset: 0x04 (R/W  8) CPU Clock Division */
  __I   uint8_t                        Reserved2[0x0B];
  __IO  uint32_t                       MCLK_AHBMASK;    /**< Offset: 0x10 (R/W  32) AHB Mask */
  __IO  uint32_t                       MCLK_APBAMASK;   /**< Offset: 0x14 (R/W  32) APBA Mask */
  __IO  uint32_t                       MCLK_APBBMASK;   /**< Offset: 0x18 (R/W  32) APBB Mask */
  __IO  uint32_t                       MCLK_APBCMASK;   /**< Offset: 0x1c (R/W  32) APBC Mask */
  __IO  uint32_t                       MCLK_APBDMASK;   /**< Offset: 0x20 (R/W  32) APBD Mask */
} mclk_registers_t;
/** @}  end of Main Clock */

#endif /* SAMC_SAMC21_MCLK_MODULE_H */

