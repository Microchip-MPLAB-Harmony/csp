/**
 * \brief Header file for SAMC/SAMC21 PAC
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
#ifndef SAMC_SAMC21_PAC_MODULE_H
#define SAMC_SAMC21_PAC_MODULE_H

/** \addtogroup SAMC_SAMC21 Peripheral Access Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_PAC                                   */
/* ========================================================================== */

/* -------- PAC_WRCTRL : (PAC Offset: 0x00) (R/W 32) Write control -------- */
#define PAC_WRCTRL_PERID_Pos                  (0U)                                           /**< (PAC_WRCTRL) Peripheral identifier Position */
#define PAC_WRCTRL_PERID_Msk                  (0xFFFFU << PAC_WRCTRL_PERID_Pos)              /**< (PAC_WRCTRL) Peripheral identifier Mask */
#define PAC_WRCTRL_PERID(value)               (PAC_WRCTRL_PERID_Msk & ((value) << PAC_WRCTRL_PERID_Pos))
#define PAC_WRCTRL_KEY_Pos                    (16U)                                          /**< (PAC_WRCTRL) Peripheral access control key Position */
#define PAC_WRCTRL_KEY_Msk                    (0xFFU << PAC_WRCTRL_KEY_Pos)                  /**< (PAC_WRCTRL) Peripheral access control key Mask */
#define PAC_WRCTRL_KEY(value)                 (PAC_WRCTRL_KEY_Msk & ((value) << PAC_WRCTRL_KEY_Pos))
#define   PAC_WRCTRL_KEY_OFF_Val              (0U)                                           /**< (PAC_WRCTRL) No action  */
#define   PAC_WRCTRL_KEY_CLR_Val              (1U)                                           /**< (PAC_WRCTRL) Clear protection  */
#define   PAC_WRCTRL_KEY_SET_Val              (2U)                                           /**< (PAC_WRCTRL) Set protection  */
#define   PAC_WRCTRL_KEY_SETLCK_Val           (3U)                                           /**< (PAC_WRCTRL) Set and lock protection  */
#define PAC_WRCTRL_KEY_OFF                    (PAC_WRCTRL_KEY_OFF_Val << PAC_WRCTRL_KEY_Pos) /**< (PAC_WRCTRL) No action Position  */
#define PAC_WRCTRL_KEY_CLR                    (PAC_WRCTRL_KEY_CLR_Val << PAC_WRCTRL_KEY_Pos) /**< (PAC_WRCTRL) Clear protection Position  */
#define PAC_WRCTRL_KEY_SET                    (PAC_WRCTRL_KEY_SET_Val << PAC_WRCTRL_KEY_Pos) /**< (PAC_WRCTRL) Set protection Position  */
#define PAC_WRCTRL_KEY_SETLCK                 (PAC_WRCTRL_KEY_SETLCK_Val << PAC_WRCTRL_KEY_Pos) /**< (PAC_WRCTRL) Set and lock protection Position  */
#define PAC_WRCTRL_Msk                        (0x00FFFFFFUL)                                 /**< (PAC_WRCTRL) Register Mask  */

/* -------- PAC_EVCTRL : (PAC Offset: 0x04) (R/W 8) Event control -------- */
#define PAC_EVCTRL_ERREO_Pos                  (0U)                                           /**< (PAC_EVCTRL) Peripheral acess error event output Position */
#define PAC_EVCTRL_ERREO_Msk                  (0x1U << PAC_EVCTRL_ERREO_Pos)                 /**< (PAC_EVCTRL) Peripheral acess error event output Mask */
#define PAC_EVCTRL_ERREO(value)               (PAC_EVCTRL_ERREO_Msk & ((value) << PAC_EVCTRL_ERREO_Pos))
#define PAC_EVCTRL_Msk                        (0x00000001UL)                                 /**< (PAC_EVCTRL) Register Mask  */

/* -------- PAC_INTENCLR : (PAC Offset: 0x08) (R/W 8) Interrupt enable clear -------- */
#define PAC_INTENCLR_ERR_Pos                  (0U)                                           /**< (PAC_INTENCLR) Peripheral access error interrupt disable Position */
#define PAC_INTENCLR_ERR_Msk                  (0x1U << PAC_INTENCLR_ERR_Pos)                 /**< (PAC_INTENCLR) Peripheral access error interrupt disable Mask */
#define PAC_INTENCLR_ERR(value)               (PAC_INTENCLR_ERR_Msk & ((value) << PAC_INTENCLR_ERR_Pos))
#define PAC_INTENCLR_Msk                      (0x00000001UL)                                 /**< (PAC_INTENCLR) Register Mask  */

/* -------- PAC_INTENSET : (PAC Offset: 0x09) (R/W 8) Interrupt enable set -------- */
#define PAC_INTENSET_ERR_Pos                  (0U)                                           /**< (PAC_INTENSET) Peripheral access error interrupt enable Position */
#define PAC_INTENSET_ERR_Msk                  (0x1U << PAC_INTENSET_ERR_Pos)                 /**< (PAC_INTENSET) Peripheral access error interrupt enable Mask */
#define PAC_INTENSET_ERR(value)               (PAC_INTENSET_ERR_Msk & ((value) << PAC_INTENSET_ERR_Pos))
#define PAC_INTENSET_Msk                      (0x00000001UL)                                 /**< (PAC_INTENSET) Register Mask  */

/* -------- PAC_INTFLAGAHB : (PAC Offset: 0x10) (R/W 32) Bridge interrupt flag status -------- */
#define PAC_INTFLAGAHB_FLASH__Pos             (0U)                                           /**< (PAC_INTFLAGAHB) FLASH Position */
#define PAC_INTFLAGAHB_FLASH__Msk             (0x1U << PAC_INTFLAGAHB_FLASH__Pos)            /**< (PAC_INTFLAGAHB) FLASH Mask */
#define PAC_INTFLAGAHB_FLASH_(value)          (PAC_INTFLAGAHB_FLASH__Msk & ((value) << PAC_INTFLAGAHB_FLASH__Pos))
#define PAC_INTFLAGAHB_HSRAMCM0P__Pos         (1U)                                           /**< (PAC_INTFLAGAHB) HSRAMCM0P Position */
#define PAC_INTFLAGAHB_HSRAMCM0P__Msk         (0x1U << PAC_INTFLAGAHB_HSRAMCM0P__Pos)        /**< (PAC_INTFLAGAHB) HSRAMCM0P Mask */
#define PAC_INTFLAGAHB_HSRAMCM0P_(value)      (PAC_INTFLAGAHB_HSRAMCM0P__Msk & ((value) << PAC_INTFLAGAHB_HSRAMCM0P__Pos))
#define PAC_INTFLAGAHB_HSRAMDSU__Pos          (2U)                                           /**< (PAC_INTFLAGAHB) HSRAMDSU Position */
#define PAC_INTFLAGAHB_HSRAMDSU__Msk          (0x1U << PAC_INTFLAGAHB_HSRAMDSU__Pos)         /**< (PAC_INTFLAGAHB) HSRAMDSU Mask */
#define PAC_INTFLAGAHB_HSRAMDSU_(value)       (PAC_INTFLAGAHB_HSRAMDSU__Msk & ((value) << PAC_INTFLAGAHB_HSRAMDSU__Pos))
#define PAC_INTFLAGAHB_HPB1__Pos              (3U)                                           /**< (PAC_INTFLAGAHB) HPB1 Position */
#define PAC_INTFLAGAHB_HPB1__Msk              (0x1U << PAC_INTFLAGAHB_HPB1__Pos)             /**< (PAC_INTFLAGAHB) HPB1 Mask */
#define PAC_INTFLAGAHB_HPB1_(value)           (PAC_INTFLAGAHB_HPB1__Msk & ((value) << PAC_INTFLAGAHB_HPB1__Pos))
#define PAC_INTFLAGAHB_HPB0__Pos              (4U)                                           /**< (PAC_INTFLAGAHB) HPB0 Position */
#define PAC_INTFLAGAHB_HPB0__Msk              (0x1U << PAC_INTFLAGAHB_HPB0__Pos)             /**< (PAC_INTFLAGAHB) HPB0 Mask */
#define PAC_INTFLAGAHB_HPB0_(value)           (PAC_INTFLAGAHB_HPB0__Msk & ((value) << PAC_INTFLAGAHB_HPB0__Pos))
#define PAC_INTFLAGAHB_HPB2__Pos              (5U)                                           /**< (PAC_INTFLAGAHB) HPB2 Position */
#define PAC_INTFLAGAHB_HPB2__Msk              (0x1U << PAC_INTFLAGAHB_HPB2__Pos)             /**< (PAC_INTFLAGAHB) HPB2 Mask */
#define PAC_INTFLAGAHB_HPB2_(value)           (PAC_INTFLAGAHB_HPB2__Msk & ((value) << PAC_INTFLAGAHB_HPB2__Pos))
#define PAC_INTFLAGAHB_LPRAMDMAC__Pos         (6U)                                           /**< (PAC_INTFLAGAHB) LPRAMDMAC Position */
#define PAC_INTFLAGAHB_LPRAMDMAC__Msk         (0x1U << PAC_INTFLAGAHB_LPRAMDMAC__Pos)        /**< (PAC_INTFLAGAHB) LPRAMDMAC Mask */
#define PAC_INTFLAGAHB_LPRAMDMAC_(value)      (PAC_INTFLAGAHB_LPRAMDMAC__Msk & ((value) << PAC_INTFLAGAHB_LPRAMDMAC__Pos))
#define PAC_INTFLAGAHB_DIVAS__Pos             (7U)                                           /**< (PAC_INTFLAGAHB) DIVAS Position */
#define PAC_INTFLAGAHB_DIVAS__Msk             (0x1U << PAC_INTFLAGAHB_DIVAS__Pos)            /**< (PAC_INTFLAGAHB) DIVAS Mask */
#define PAC_INTFLAGAHB_DIVAS_(value)          (PAC_INTFLAGAHB_DIVAS__Msk & ((value) << PAC_INTFLAGAHB_DIVAS__Pos))
#define PAC_INTFLAGAHB_HPB3__Pos              (8U)                                           /**< (PAC_INTFLAGAHB) HPB3 Position */
#define PAC_INTFLAGAHB_HPB3__Msk              (0x1U << PAC_INTFLAGAHB_HPB3__Pos)             /**< (PAC_INTFLAGAHB) HPB3 Mask */
#define PAC_INTFLAGAHB_HPB3_(value)           (PAC_INTFLAGAHB_HPB3__Msk & ((value) << PAC_INTFLAGAHB_HPB3__Pos))
#define PAC_INTFLAGAHB_Msk                    (0x000001FFUL)                                 /**< (PAC_INTFLAGAHB) Register Mask  */

/* -------- PAC_INTFLAGA : (PAC Offset: 0x14) (R/W 32) Peripheral interrupt flag status - Bridge A -------- */
#define PAC_INTFLAGA_PAC__Pos                 (0U)                                           /**< (PAC_INTFLAGA) PAC Position */
#define PAC_INTFLAGA_PAC__Msk                 (0x1U << PAC_INTFLAGA_PAC__Pos)                /**< (PAC_INTFLAGA) PAC Mask */
#define PAC_INTFLAGA_PAC_(value)              (PAC_INTFLAGA_PAC__Msk & ((value) << PAC_INTFLAGA_PAC__Pos))
#define PAC_INTFLAGA_PM__Pos                  (1U)                                           /**< (PAC_INTFLAGA) PM Position */
#define PAC_INTFLAGA_PM__Msk                  (0x1U << PAC_INTFLAGA_PM__Pos)                 /**< (PAC_INTFLAGA) PM Mask */
#define PAC_INTFLAGA_PM_(value)               (PAC_INTFLAGA_PM__Msk & ((value) << PAC_INTFLAGA_PM__Pos))
#define PAC_INTFLAGA_MCLK__Pos                (2U)                                           /**< (PAC_INTFLAGA) MCLK Position */
#define PAC_INTFLAGA_MCLK__Msk                (0x1U << PAC_INTFLAGA_MCLK__Pos)               /**< (PAC_INTFLAGA) MCLK Mask */
#define PAC_INTFLAGA_MCLK_(value)             (PAC_INTFLAGA_MCLK__Msk & ((value) << PAC_INTFLAGA_MCLK__Pos))
#define PAC_INTFLAGA_RSTC__Pos                (3U)                                           /**< (PAC_INTFLAGA) RSTC Position */
#define PAC_INTFLAGA_RSTC__Msk                (0x1U << PAC_INTFLAGA_RSTC__Pos)               /**< (PAC_INTFLAGA) RSTC Mask */
#define PAC_INTFLAGA_RSTC_(value)             (PAC_INTFLAGA_RSTC__Msk & ((value) << PAC_INTFLAGA_RSTC__Pos))
#define PAC_INTFLAGA_OSCCTRL__Pos             (4U)                                           /**< (PAC_INTFLAGA) OSCCTRL Position */
#define PAC_INTFLAGA_OSCCTRL__Msk             (0x1U << PAC_INTFLAGA_OSCCTRL__Pos)            /**< (PAC_INTFLAGA) OSCCTRL Mask */
#define PAC_INTFLAGA_OSCCTRL_(value)          (PAC_INTFLAGA_OSCCTRL__Msk & ((value) << PAC_INTFLAGA_OSCCTRL__Pos))
#define PAC_INTFLAGA_OSC32KCTRL__Pos          (5U)                                           /**< (PAC_INTFLAGA) OSC32KCTRL Position */
#define PAC_INTFLAGA_OSC32KCTRL__Msk          (0x1U << PAC_INTFLAGA_OSC32KCTRL__Pos)         /**< (PAC_INTFLAGA) OSC32KCTRL Mask */
#define PAC_INTFLAGA_OSC32KCTRL_(value)       (PAC_INTFLAGA_OSC32KCTRL__Msk & ((value) << PAC_INTFLAGA_OSC32KCTRL__Pos))
#define PAC_INTFLAGA_SUPC__Pos                (6U)                                           /**< (PAC_INTFLAGA) SUPC Position */
#define PAC_INTFLAGA_SUPC__Msk                (0x1U << PAC_INTFLAGA_SUPC__Pos)               /**< (PAC_INTFLAGA) SUPC Mask */
#define PAC_INTFLAGA_SUPC_(value)             (PAC_INTFLAGA_SUPC__Msk & ((value) << PAC_INTFLAGA_SUPC__Pos))
#define PAC_INTFLAGA_GCLK__Pos                (7U)                                           /**< (PAC_INTFLAGA) GCLK Position */
#define PAC_INTFLAGA_GCLK__Msk                (0x1U << PAC_INTFLAGA_GCLK__Pos)               /**< (PAC_INTFLAGA) GCLK Mask */
#define PAC_INTFLAGA_GCLK_(value)             (PAC_INTFLAGA_GCLK__Msk & ((value) << PAC_INTFLAGA_GCLK__Pos))
#define PAC_INTFLAGA_WDT__Pos                 (8U)                                           /**< (PAC_INTFLAGA) WDT Position */
#define PAC_INTFLAGA_WDT__Msk                 (0x1U << PAC_INTFLAGA_WDT__Pos)                /**< (PAC_INTFLAGA) WDT Mask */
#define PAC_INTFLAGA_WDT_(value)              (PAC_INTFLAGA_WDT__Msk & ((value) << PAC_INTFLAGA_WDT__Pos))
#define PAC_INTFLAGA_RTC__Pos                 (9U)                                           /**< (PAC_INTFLAGA) RTC Position */
#define PAC_INTFLAGA_RTC__Msk                 (0x1U << PAC_INTFLAGA_RTC__Pos)                /**< (PAC_INTFLAGA) RTC Mask */
#define PAC_INTFLAGA_RTC_(value)              (PAC_INTFLAGA_RTC__Msk & ((value) << PAC_INTFLAGA_RTC__Pos))
#define PAC_INTFLAGA_EIC__Pos                 (10U)                                          /**< (PAC_INTFLAGA) EIC Position */
#define PAC_INTFLAGA_EIC__Msk                 (0x1U << PAC_INTFLAGA_EIC__Pos)                /**< (PAC_INTFLAGA) EIC Mask */
#define PAC_INTFLAGA_EIC_(value)              (PAC_INTFLAGA_EIC__Msk & ((value) << PAC_INTFLAGA_EIC__Pos))
#define PAC_INTFLAGA_FREQM__Pos               (11U)                                          /**< (PAC_INTFLAGA) FREQM Position */
#define PAC_INTFLAGA_FREQM__Msk               (0x1U << PAC_INTFLAGA_FREQM__Pos)              /**< (PAC_INTFLAGA) FREQM Mask */
#define PAC_INTFLAGA_FREQM_(value)            (PAC_INTFLAGA_FREQM__Msk & ((value) << PAC_INTFLAGA_FREQM__Pos))
#define PAC_INTFLAGA_TSENS__Pos               (12U)                                          /**< (PAC_INTFLAGA) TSENS Position */
#define PAC_INTFLAGA_TSENS__Msk               (0x1U << PAC_INTFLAGA_TSENS__Pos)              /**< (PAC_INTFLAGA) TSENS Mask */
#define PAC_INTFLAGA_TSENS_(value)            (PAC_INTFLAGA_TSENS__Msk & ((value) << PAC_INTFLAGA_TSENS__Pos))
#define PAC_INTFLAGA_Msk                      (0x00001FFFUL)                                 /**< (PAC_INTFLAGA) Register Mask  */

/* -------- PAC_INTFLAGB : (PAC Offset: 0x18) (R/W 32) Peripheral interrupt flag status - Bridge B -------- */
#define PAC_INTFLAGB_PORT__Pos                (0U)                                           /**< (PAC_INTFLAGB) PORT Position */
#define PAC_INTFLAGB_PORT__Msk                (0x1U << PAC_INTFLAGB_PORT__Pos)               /**< (PAC_INTFLAGB) PORT Mask */
#define PAC_INTFLAGB_PORT_(value)             (PAC_INTFLAGB_PORT__Msk & ((value) << PAC_INTFLAGB_PORT__Pos))
#define PAC_INTFLAGB_DSU__Pos                 (1U)                                           /**< (PAC_INTFLAGB) DSU Position */
#define PAC_INTFLAGB_DSU__Msk                 (0x1U << PAC_INTFLAGB_DSU__Pos)                /**< (PAC_INTFLAGB) DSU Mask */
#define PAC_INTFLAGB_DSU_(value)              (PAC_INTFLAGB_DSU__Msk & ((value) << PAC_INTFLAGB_DSU__Pos))
#define PAC_INTFLAGB_NVMCTRL__Pos             (2U)                                           /**< (PAC_INTFLAGB) NVMCTRL Position */
#define PAC_INTFLAGB_NVMCTRL__Msk             (0x1U << PAC_INTFLAGB_NVMCTRL__Pos)            /**< (PAC_INTFLAGB) NVMCTRL Mask */
#define PAC_INTFLAGB_NVMCTRL_(value)          (PAC_INTFLAGB_NVMCTRL__Msk & ((value) << PAC_INTFLAGB_NVMCTRL__Pos))
#define PAC_INTFLAGB_DMAC__Pos                (3U)                                           /**< (PAC_INTFLAGB) DMAC Position */
#define PAC_INTFLAGB_DMAC__Msk                (0x1U << PAC_INTFLAGB_DMAC__Pos)               /**< (PAC_INTFLAGB) DMAC Mask */
#define PAC_INTFLAGB_DMAC_(value)             (PAC_INTFLAGB_DMAC__Msk & ((value) << PAC_INTFLAGB_DMAC__Pos))
#define PAC_INTFLAGB_MTB__Pos                 (4U)                                           /**< (PAC_INTFLAGB) MTB Position */
#define PAC_INTFLAGB_MTB__Msk                 (0x1U << PAC_INTFLAGB_MTB__Pos)                /**< (PAC_INTFLAGB) MTB Mask */
#define PAC_INTFLAGB_MTB_(value)              (PAC_INTFLAGB_MTB__Msk & ((value) << PAC_INTFLAGB_MTB__Pos))
#define PAC_INTFLAGB_HMATRIXHS__Pos           (5U)                                           /**< (PAC_INTFLAGB) HMATRIXHS Position */
#define PAC_INTFLAGB_HMATRIXHS__Msk           (0x1U << PAC_INTFLAGB_HMATRIXHS__Pos)          /**< (PAC_INTFLAGB) HMATRIXHS Mask */
#define PAC_INTFLAGB_HMATRIXHS_(value)        (PAC_INTFLAGB_HMATRIXHS__Msk & ((value) << PAC_INTFLAGB_HMATRIXHS__Pos))
#define PAC_INTFLAGB_Msk                      (0x0000003FUL)                                 /**< (PAC_INTFLAGB) Register Mask  */

/* -------- PAC_INTFLAGC : (PAC Offset: 0x1C) (R/W 32) Peripheral interrupt flag status - Bridge C -------- */
#define PAC_INTFLAGC_EVSYS__Pos               (0U)                                           /**< (PAC_INTFLAGC) EVSYS Position */
#define PAC_INTFLAGC_EVSYS__Msk               (0x1U << PAC_INTFLAGC_EVSYS__Pos)              /**< (PAC_INTFLAGC) EVSYS Mask */
#define PAC_INTFLAGC_EVSYS_(value)            (PAC_INTFLAGC_EVSYS__Msk & ((value) << PAC_INTFLAGC_EVSYS__Pos))
#define PAC_INTFLAGC_SERCOM0__Pos             (1U)                                           /**< (PAC_INTFLAGC) SERCOM0 Position */
#define PAC_INTFLAGC_SERCOM0__Msk             (0x1U << PAC_INTFLAGC_SERCOM0__Pos)            /**< (PAC_INTFLAGC) SERCOM0 Mask */
#define PAC_INTFLAGC_SERCOM0_(value)          (PAC_INTFLAGC_SERCOM0__Msk & ((value) << PAC_INTFLAGC_SERCOM0__Pos))
#define PAC_INTFLAGC_SERCOM1__Pos             (2U)                                           /**< (PAC_INTFLAGC) SERCOM1 Position */
#define PAC_INTFLAGC_SERCOM1__Msk             (0x1U << PAC_INTFLAGC_SERCOM1__Pos)            /**< (PAC_INTFLAGC) SERCOM1 Mask */
#define PAC_INTFLAGC_SERCOM1_(value)          (PAC_INTFLAGC_SERCOM1__Msk & ((value) << PAC_INTFLAGC_SERCOM1__Pos))
#define PAC_INTFLAGC_SERCOM2__Pos             (3U)                                           /**< (PAC_INTFLAGC) SERCOM2 Position */
#define PAC_INTFLAGC_SERCOM2__Msk             (0x1U << PAC_INTFLAGC_SERCOM2__Pos)            /**< (PAC_INTFLAGC) SERCOM2 Mask */
#define PAC_INTFLAGC_SERCOM2_(value)          (PAC_INTFLAGC_SERCOM2__Msk & ((value) << PAC_INTFLAGC_SERCOM2__Pos))
#define PAC_INTFLAGC_SERCOM3__Pos             (4U)                                           /**< (PAC_INTFLAGC) SERCOM3 Position */
#define PAC_INTFLAGC_SERCOM3__Msk             (0x1U << PAC_INTFLAGC_SERCOM3__Pos)            /**< (PAC_INTFLAGC) SERCOM3 Mask */
#define PAC_INTFLAGC_SERCOM3_(value)          (PAC_INTFLAGC_SERCOM3__Msk & ((value) << PAC_INTFLAGC_SERCOM3__Pos))
#define PAC_INTFLAGC_SERCOM4__Pos             (5U)                                           /**< (PAC_INTFLAGC) SERCOM4 Position */
#define PAC_INTFLAGC_SERCOM4__Msk             (0x1U << PAC_INTFLAGC_SERCOM4__Pos)            /**< (PAC_INTFLAGC) SERCOM4 Mask */
#define PAC_INTFLAGC_SERCOM4_(value)          (PAC_INTFLAGC_SERCOM4__Msk & ((value) << PAC_INTFLAGC_SERCOM4__Pos))
#define PAC_INTFLAGC_SERCOM5__Pos             (6U)                                           /**< (PAC_INTFLAGC) SERCOM5 Position */
#define PAC_INTFLAGC_SERCOM5__Msk             (0x1U << PAC_INTFLAGC_SERCOM5__Pos)            /**< (PAC_INTFLAGC) SERCOM5 Mask */
#define PAC_INTFLAGC_SERCOM5_(value)          (PAC_INTFLAGC_SERCOM5__Msk & ((value) << PAC_INTFLAGC_SERCOM5__Pos))
#define PAC_INTFLAGC_CAN0__Pos                (7U)                                           /**< (PAC_INTFLAGC) CAN0 Position */
#define PAC_INTFLAGC_CAN0__Msk                (0x1U << PAC_INTFLAGC_CAN0__Pos)               /**< (PAC_INTFLAGC) CAN0 Mask */
#define PAC_INTFLAGC_CAN0_(value)             (PAC_INTFLAGC_CAN0__Msk & ((value) << PAC_INTFLAGC_CAN0__Pos))
#define PAC_INTFLAGC_CAN1__Pos                (8U)                                           /**< (PAC_INTFLAGC) CAN1 Position */
#define PAC_INTFLAGC_CAN1__Msk                (0x1U << PAC_INTFLAGC_CAN1__Pos)               /**< (PAC_INTFLAGC) CAN1 Mask */
#define PAC_INTFLAGC_CAN1_(value)             (PAC_INTFLAGC_CAN1__Msk & ((value) << PAC_INTFLAGC_CAN1__Pos))
#define PAC_INTFLAGC_TCC0__Pos                (9U)                                           /**< (PAC_INTFLAGC) TCC0 Position */
#define PAC_INTFLAGC_TCC0__Msk                (0x1U << PAC_INTFLAGC_TCC0__Pos)               /**< (PAC_INTFLAGC) TCC0 Mask */
#define PAC_INTFLAGC_TCC0_(value)             (PAC_INTFLAGC_TCC0__Msk & ((value) << PAC_INTFLAGC_TCC0__Pos))
#define PAC_INTFLAGC_TCC1__Pos                (10U)                                          /**< (PAC_INTFLAGC) TCC1 Position */
#define PAC_INTFLAGC_TCC1__Msk                (0x1U << PAC_INTFLAGC_TCC1__Pos)               /**< (PAC_INTFLAGC) TCC1 Mask */
#define PAC_INTFLAGC_TCC1_(value)             (PAC_INTFLAGC_TCC1__Msk & ((value) << PAC_INTFLAGC_TCC1__Pos))
#define PAC_INTFLAGC_TCC2__Pos                (11U)                                          /**< (PAC_INTFLAGC) TCC2 Position */
#define PAC_INTFLAGC_TCC2__Msk                (0x1U << PAC_INTFLAGC_TCC2__Pos)               /**< (PAC_INTFLAGC) TCC2 Mask */
#define PAC_INTFLAGC_TCC2_(value)             (PAC_INTFLAGC_TCC2__Msk & ((value) << PAC_INTFLAGC_TCC2__Pos))
#define PAC_INTFLAGC_TC0__Pos                 (12U)                                          /**< (PAC_INTFLAGC) TC0 Position */
#define PAC_INTFLAGC_TC0__Msk                 (0x1U << PAC_INTFLAGC_TC0__Pos)                /**< (PAC_INTFLAGC) TC0 Mask */
#define PAC_INTFLAGC_TC0_(value)              (PAC_INTFLAGC_TC0__Msk & ((value) << PAC_INTFLAGC_TC0__Pos))
#define PAC_INTFLAGC_TC1__Pos                 (13U)                                          /**< (PAC_INTFLAGC) TC1 Position */
#define PAC_INTFLAGC_TC1__Msk                 (0x1U << PAC_INTFLAGC_TC1__Pos)                /**< (PAC_INTFLAGC) TC1 Mask */
#define PAC_INTFLAGC_TC1_(value)              (PAC_INTFLAGC_TC1__Msk & ((value) << PAC_INTFLAGC_TC1__Pos))
#define PAC_INTFLAGC_TC2__Pos                 (14U)                                          /**< (PAC_INTFLAGC) TC2 Position */
#define PAC_INTFLAGC_TC2__Msk                 (0x1U << PAC_INTFLAGC_TC2__Pos)                /**< (PAC_INTFLAGC) TC2 Mask */
#define PAC_INTFLAGC_TC2_(value)              (PAC_INTFLAGC_TC2__Msk & ((value) << PAC_INTFLAGC_TC2__Pos))
#define PAC_INTFLAGC_TC3__Pos                 (15U)                                          /**< (PAC_INTFLAGC) TC3 Position */
#define PAC_INTFLAGC_TC3__Msk                 (0x1U << PAC_INTFLAGC_TC3__Pos)                /**< (PAC_INTFLAGC) TC3 Mask */
#define PAC_INTFLAGC_TC3_(value)              (PAC_INTFLAGC_TC3__Msk & ((value) << PAC_INTFLAGC_TC3__Pos))
#define PAC_INTFLAGC_TC4__Pos                 (16U)                                          /**< (PAC_INTFLAGC) TC4 Position */
#define PAC_INTFLAGC_TC4__Msk                 (0x1U << PAC_INTFLAGC_TC4__Pos)                /**< (PAC_INTFLAGC) TC4 Mask */
#define PAC_INTFLAGC_TC4_(value)              (PAC_INTFLAGC_TC4__Msk & ((value) << PAC_INTFLAGC_TC4__Pos))
#define PAC_INTFLAGC_ADC0__Pos                (17U)                                          /**< (PAC_INTFLAGC) ADC0 Position */
#define PAC_INTFLAGC_ADC0__Msk                (0x1U << PAC_INTFLAGC_ADC0__Pos)               /**< (PAC_INTFLAGC) ADC0 Mask */
#define PAC_INTFLAGC_ADC0_(value)             (PAC_INTFLAGC_ADC0__Msk & ((value) << PAC_INTFLAGC_ADC0__Pos))
#define PAC_INTFLAGC_ADC1__Pos                (18U)                                          /**< (PAC_INTFLAGC) ADC1 Position */
#define PAC_INTFLAGC_ADC1__Msk                (0x1U << PAC_INTFLAGC_ADC1__Pos)               /**< (PAC_INTFLAGC) ADC1 Mask */
#define PAC_INTFLAGC_ADC1_(value)             (PAC_INTFLAGC_ADC1__Msk & ((value) << PAC_INTFLAGC_ADC1__Pos))
#define PAC_INTFLAGC_SDADC__Pos               (19U)                                          /**< (PAC_INTFLAGC) SDADC Position */
#define PAC_INTFLAGC_SDADC__Msk               (0x1U << PAC_INTFLAGC_SDADC__Pos)              /**< (PAC_INTFLAGC) SDADC Mask */
#define PAC_INTFLAGC_SDADC_(value)            (PAC_INTFLAGC_SDADC__Msk & ((value) << PAC_INTFLAGC_SDADC__Pos))
#define PAC_INTFLAGC_AC__Pos                  (20U)                                          /**< (PAC_INTFLAGC) AC Position */
#define PAC_INTFLAGC_AC__Msk                  (0x1U << PAC_INTFLAGC_AC__Pos)                 /**< (PAC_INTFLAGC) AC Mask */
#define PAC_INTFLAGC_AC_(value)               (PAC_INTFLAGC_AC__Msk & ((value) << PAC_INTFLAGC_AC__Pos))
#define PAC_INTFLAGC_DAC__Pos                 (21U)                                          /**< (PAC_INTFLAGC) DAC Position */
#define PAC_INTFLAGC_DAC__Msk                 (0x1U << PAC_INTFLAGC_DAC__Pos)                /**< (PAC_INTFLAGC) DAC Mask */
#define PAC_INTFLAGC_DAC_(value)              (PAC_INTFLAGC_DAC__Msk & ((value) << PAC_INTFLAGC_DAC__Pos))
#define PAC_INTFLAGC_PTC__Pos                 (22U)                                          /**< (PAC_INTFLAGC) PTC Position */
#define PAC_INTFLAGC_PTC__Msk                 (0x1U << PAC_INTFLAGC_PTC__Pos)                /**< (PAC_INTFLAGC) PTC Mask */
#define PAC_INTFLAGC_PTC_(value)              (PAC_INTFLAGC_PTC__Msk & ((value) << PAC_INTFLAGC_PTC__Pos))
#define PAC_INTFLAGC_CCL__Pos                 (23U)                                          /**< (PAC_INTFLAGC) CCL Position */
#define PAC_INTFLAGC_CCL__Msk                 (0x1U << PAC_INTFLAGC_CCL__Pos)                /**< (PAC_INTFLAGC) CCL Mask */
#define PAC_INTFLAGC_CCL_(value)              (PAC_INTFLAGC_CCL__Msk & ((value) << PAC_INTFLAGC_CCL__Pos))
#define PAC_INTFLAGC_Msk                      (0x00FFFFFFUL)                                 /**< (PAC_INTFLAGC) Register Mask  */

/* -------- PAC_INTFLAGD : (PAC Offset: 0x20) (R/W 32) Peripheral interrupt flag status - Bridge D -------- */
#define PAC_INTFLAGD_SERCOM6__Pos             (0U)                                           /**< (PAC_INTFLAGD) SERCOM6 Position */
#define PAC_INTFLAGD_SERCOM6__Msk             (0x1U << PAC_INTFLAGD_SERCOM6__Pos)            /**< (PAC_INTFLAGD) SERCOM6 Mask */
#define PAC_INTFLAGD_SERCOM6_(value)          (PAC_INTFLAGD_SERCOM6__Msk & ((value) << PAC_INTFLAGD_SERCOM6__Pos))
#define PAC_INTFLAGD_SERCOM7__Pos             (1U)                                           /**< (PAC_INTFLAGD) SERCOM7 Position */
#define PAC_INTFLAGD_SERCOM7__Msk             (0x1U << PAC_INTFLAGD_SERCOM7__Pos)            /**< (PAC_INTFLAGD) SERCOM7 Mask */
#define PAC_INTFLAGD_SERCOM7_(value)          (PAC_INTFLAGD_SERCOM7__Msk & ((value) << PAC_INTFLAGD_SERCOM7__Pos))
#define PAC_INTFLAGD_TC5__Pos                 (2U)                                           /**< (PAC_INTFLAGD) TC5 Position */
#define PAC_INTFLAGD_TC5__Msk                 (0x1U << PAC_INTFLAGD_TC5__Pos)                /**< (PAC_INTFLAGD) TC5 Mask */
#define PAC_INTFLAGD_TC5_(value)              (PAC_INTFLAGD_TC5__Msk & ((value) << PAC_INTFLAGD_TC5__Pos))
#define PAC_INTFLAGD_TC6__Pos                 (3U)                                           /**< (PAC_INTFLAGD) TC6 Position */
#define PAC_INTFLAGD_TC6__Msk                 (0x1U << PAC_INTFLAGD_TC6__Pos)                /**< (PAC_INTFLAGD) TC6 Mask */
#define PAC_INTFLAGD_TC6_(value)              (PAC_INTFLAGD_TC6__Msk & ((value) << PAC_INTFLAGD_TC6__Pos))
#define PAC_INTFLAGD_TC7__Pos                 (4U)                                           /**< (PAC_INTFLAGD) TC7 Position */
#define PAC_INTFLAGD_TC7__Msk                 (0x1U << PAC_INTFLAGD_TC7__Pos)                /**< (PAC_INTFLAGD) TC7 Mask */
#define PAC_INTFLAGD_TC7_(value)              (PAC_INTFLAGD_TC7__Msk & ((value) << PAC_INTFLAGD_TC7__Pos))
#define PAC_INTFLAGD_Msk                      (0x0000001FUL)                                 /**< (PAC_INTFLAGD) Register Mask  */

/* -------- PAC_STATUSA : (PAC Offset: 0x34) (R/  32) Peripheral write protection status - Bridge A -------- */
#define PAC_STATUSA_PAC__Pos                  (0U)                                           /**< (PAC_STATUSA) PAC APB Protect Enable Position */
#define PAC_STATUSA_PAC__Msk                  (0x1U << PAC_STATUSA_PAC__Pos)                 /**< (PAC_STATUSA) PAC APB Protect Enable Mask */
#define PAC_STATUSA_PAC_(value)               (PAC_STATUSA_PAC__Msk & ((value) << PAC_STATUSA_PAC__Pos))
#define PAC_STATUSA_PM__Pos                   (1U)                                           /**< (PAC_STATUSA) PM APB Protect Enable Position */
#define PAC_STATUSA_PM__Msk                   (0x1U << PAC_STATUSA_PM__Pos)                  /**< (PAC_STATUSA) PM APB Protect Enable Mask */
#define PAC_STATUSA_PM_(value)                (PAC_STATUSA_PM__Msk & ((value) << PAC_STATUSA_PM__Pos))
#define PAC_STATUSA_MCLK__Pos                 (2U)                                           /**< (PAC_STATUSA) MCLK APB Protect Enable Position */
#define PAC_STATUSA_MCLK__Msk                 (0x1U << PAC_STATUSA_MCLK__Pos)                /**< (PAC_STATUSA) MCLK APB Protect Enable Mask */
#define PAC_STATUSA_MCLK_(value)              (PAC_STATUSA_MCLK__Msk & ((value) << PAC_STATUSA_MCLK__Pos))
#define PAC_STATUSA_RSTC__Pos                 (3U)                                           /**< (PAC_STATUSA) RSTC APB Protect Enable Position */
#define PAC_STATUSA_RSTC__Msk                 (0x1U << PAC_STATUSA_RSTC__Pos)                /**< (PAC_STATUSA) RSTC APB Protect Enable Mask */
#define PAC_STATUSA_RSTC_(value)              (PAC_STATUSA_RSTC__Msk & ((value) << PAC_STATUSA_RSTC__Pos))
#define PAC_STATUSA_OSCCTRL__Pos              (4U)                                           /**< (PAC_STATUSA) OSCCTRL APB Protect Enable Position */
#define PAC_STATUSA_OSCCTRL__Msk              (0x1U << PAC_STATUSA_OSCCTRL__Pos)             /**< (PAC_STATUSA) OSCCTRL APB Protect Enable Mask */
#define PAC_STATUSA_OSCCTRL_(value)           (PAC_STATUSA_OSCCTRL__Msk & ((value) << PAC_STATUSA_OSCCTRL__Pos))
#define PAC_STATUSA_OSC32KCTRL__Pos           (5U)                                           /**< (PAC_STATUSA) OSC32KCTRL APB Protect Enable Position */
#define PAC_STATUSA_OSC32KCTRL__Msk           (0x1U << PAC_STATUSA_OSC32KCTRL__Pos)          /**< (PAC_STATUSA) OSC32KCTRL APB Protect Enable Mask */
#define PAC_STATUSA_OSC32KCTRL_(value)        (PAC_STATUSA_OSC32KCTRL__Msk & ((value) << PAC_STATUSA_OSC32KCTRL__Pos))
#define PAC_STATUSA_SUPC__Pos                 (6U)                                           /**< (PAC_STATUSA) SUPC APB Protect Enable Position */
#define PAC_STATUSA_SUPC__Msk                 (0x1U << PAC_STATUSA_SUPC__Pos)                /**< (PAC_STATUSA) SUPC APB Protect Enable Mask */
#define PAC_STATUSA_SUPC_(value)              (PAC_STATUSA_SUPC__Msk & ((value) << PAC_STATUSA_SUPC__Pos))
#define PAC_STATUSA_GCLK__Pos                 (7U)                                           /**< (PAC_STATUSA) GCLK APB Protect Enable Position */
#define PAC_STATUSA_GCLK__Msk                 (0x1U << PAC_STATUSA_GCLK__Pos)                /**< (PAC_STATUSA) GCLK APB Protect Enable Mask */
#define PAC_STATUSA_GCLK_(value)              (PAC_STATUSA_GCLK__Msk & ((value) << PAC_STATUSA_GCLK__Pos))
#define PAC_STATUSA_WDT__Pos                  (8U)                                           /**< (PAC_STATUSA) WDT APB Protect Enable Position */
#define PAC_STATUSA_WDT__Msk                  (0x1U << PAC_STATUSA_WDT__Pos)                 /**< (PAC_STATUSA) WDT APB Protect Enable Mask */
#define PAC_STATUSA_WDT_(value)               (PAC_STATUSA_WDT__Msk & ((value) << PAC_STATUSA_WDT__Pos))
#define PAC_STATUSA_RTC__Pos                  (9U)                                           /**< (PAC_STATUSA) RTC APB Protect Enable Position */
#define PAC_STATUSA_RTC__Msk                  (0x1U << PAC_STATUSA_RTC__Pos)                 /**< (PAC_STATUSA) RTC APB Protect Enable Mask */
#define PAC_STATUSA_RTC_(value)               (PAC_STATUSA_RTC__Msk & ((value) << PAC_STATUSA_RTC__Pos))
#define PAC_STATUSA_EIC__Pos                  (10U)                                          /**< (PAC_STATUSA) EIC APB Protect Enable Position */
#define PAC_STATUSA_EIC__Msk                  (0x1U << PAC_STATUSA_EIC__Pos)                 /**< (PAC_STATUSA) EIC APB Protect Enable Mask */
#define PAC_STATUSA_EIC_(value)               (PAC_STATUSA_EIC__Msk & ((value) << PAC_STATUSA_EIC__Pos))
#define PAC_STATUSA_FREQM__Pos                (11U)                                          /**< (PAC_STATUSA) FREQM APB Protect Enable Position */
#define PAC_STATUSA_FREQM__Msk                (0x1U << PAC_STATUSA_FREQM__Pos)               /**< (PAC_STATUSA) FREQM APB Protect Enable Mask */
#define PAC_STATUSA_FREQM_(value)             (PAC_STATUSA_FREQM__Msk & ((value) << PAC_STATUSA_FREQM__Pos))
#define PAC_STATUSA_TSENS__Pos                (12U)                                          /**< (PAC_STATUSA) TSENS APB Protect Enable Position */
#define PAC_STATUSA_TSENS__Msk                (0x1U << PAC_STATUSA_TSENS__Pos)               /**< (PAC_STATUSA) TSENS APB Protect Enable Mask */
#define PAC_STATUSA_TSENS_(value)             (PAC_STATUSA_TSENS__Msk & ((value) << PAC_STATUSA_TSENS__Pos))
#define PAC_STATUSA_Msk                       (0x00001FFFUL)                                 /**< (PAC_STATUSA) Register Mask  */

/* -------- PAC_STATUSB : (PAC Offset: 0x38) (R/  32) Peripheral write protection status - Bridge B -------- */
#define PAC_STATUSB_PORT__Pos                 (0U)                                           /**< (PAC_STATUSB) PORT APB Protect Enable Position */
#define PAC_STATUSB_PORT__Msk                 (0x1U << PAC_STATUSB_PORT__Pos)                /**< (PAC_STATUSB) PORT APB Protect Enable Mask */
#define PAC_STATUSB_PORT_(value)              (PAC_STATUSB_PORT__Msk & ((value) << PAC_STATUSB_PORT__Pos))
#define PAC_STATUSB_DSU__Pos                  (1U)                                           /**< (PAC_STATUSB) DSU APB Protect Enable Position */
#define PAC_STATUSB_DSU__Msk                  (0x1U << PAC_STATUSB_DSU__Pos)                 /**< (PAC_STATUSB) DSU APB Protect Enable Mask */
#define PAC_STATUSB_DSU_(value)               (PAC_STATUSB_DSU__Msk & ((value) << PAC_STATUSB_DSU__Pos))
#define PAC_STATUSB_NVMCTRL__Pos              (2U)                                           /**< (PAC_STATUSB) NVMCTRL APB Protect Enable Position */
#define PAC_STATUSB_NVMCTRL__Msk              (0x1U << PAC_STATUSB_NVMCTRL__Pos)             /**< (PAC_STATUSB) NVMCTRL APB Protect Enable Mask */
#define PAC_STATUSB_NVMCTRL_(value)           (PAC_STATUSB_NVMCTRL__Msk & ((value) << PAC_STATUSB_NVMCTRL__Pos))
#define PAC_STATUSB_DMAC__Pos                 (3U)                                           /**< (PAC_STATUSB) DMAC APB Protect Enable Position */
#define PAC_STATUSB_DMAC__Msk                 (0x1U << PAC_STATUSB_DMAC__Pos)                /**< (PAC_STATUSB) DMAC APB Protect Enable Mask */
#define PAC_STATUSB_DMAC_(value)              (PAC_STATUSB_DMAC__Msk & ((value) << PAC_STATUSB_DMAC__Pos))
#define PAC_STATUSB_MTB__Pos                  (4U)                                           /**< (PAC_STATUSB) MTB APB Protect Enable Position */
#define PAC_STATUSB_MTB__Msk                  (0x1U << PAC_STATUSB_MTB__Pos)                 /**< (PAC_STATUSB) MTB APB Protect Enable Mask */
#define PAC_STATUSB_MTB_(value)               (PAC_STATUSB_MTB__Msk & ((value) << PAC_STATUSB_MTB__Pos))
#define PAC_STATUSB_HMATRIXHS__Pos            (5U)                                           /**< (PAC_STATUSB) HMATRIXHS APB Protect Enable Position */
#define PAC_STATUSB_HMATRIXHS__Msk            (0x1U << PAC_STATUSB_HMATRIXHS__Pos)           /**< (PAC_STATUSB) HMATRIXHS APB Protect Enable Mask */
#define PAC_STATUSB_HMATRIXHS_(value)         (PAC_STATUSB_HMATRIXHS__Msk & ((value) << PAC_STATUSB_HMATRIXHS__Pos))
#define PAC_STATUSB_Msk                       (0x0000003FUL)                                 /**< (PAC_STATUSB) Register Mask  */

/* -------- PAC_STATUSC : (PAC Offset: 0x3C) (R/  32) Peripheral write protection status - Bridge C -------- */
#define PAC_STATUSC_EVSYS__Pos                (0U)                                           /**< (PAC_STATUSC) EVSYS APB Protect Enable Position */
#define PAC_STATUSC_EVSYS__Msk                (0x1U << PAC_STATUSC_EVSYS__Pos)               /**< (PAC_STATUSC) EVSYS APB Protect Enable Mask */
#define PAC_STATUSC_EVSYS_(value)             (PAC_STATUSC_EVSYS__Msk & ((value) << PAC_STATUSC_EVSYS__Pos))
#define PAC_STATUSC_SERCOM0__Pos              (1U)                                           /**< (PAC_STATUSC) SERCOM0 APB Protect Enable Position */
#define PAC_STATUSC_SERCOM0__Msk              (0x1U << PAC_STATUSC_SERCOM0__Pos)             /**< (PAC_STATUSC) SERCOM0 APB Protect Enable Mask */
#define PAC_STATUSC_SERCOM0_(value)           (PAC_STATUSC_SERCOM0__Msk & ((value) << PAC_STATUSC_SERCOM0__Pos))
#define PAC_STATUSC_SERCOM1__Pos              (2U)                                           /**< (PAC_STATUSC) SERCOM1 APB Protect Enable Position */
#define PAC_STATUSC_SERCOM1__Msk              (0x1U << PAC_STATUSC_SERCOM1__Pos)             /**< (PAC_STATUSC) SERCOM1 APB Protect Enable Mask */
#define PAC_STATUSC_SERCOM1_(value)           (PAC_STATUSC_SERCOM1__Msk & ((value) << PAC_STATUSC_SERCOM1__Pos))
#define PAC_STATUSC_SERCOM2__Pos              (3U)                                           /**< (PAC_STATUSC) SERCOM2 APB Protect Enable Position */
#define PAC_STATUSC_SERCOM2__Msk              (0x1U << PAC_STATUSC_SERCOM2__Pos)             /**< (PAC_STATUSC) SERCOM2 APB Protect Enable Mask */
#define PAC_STATUSC_SERCOM2_(value)           (PAC_STATUSC_SERCOM2__Msk & ((value) << PAC_STATUSC_SERCOM2__Pos))
#define PAC_STATUSC_SERCOM3__Pos              (4U)                                           /**< (PAC_STATUSC) SERCOM3 APB Protect Enable Position */
#define PAC_STATUSC_SERCOM3__Msk              (0x1U << PAC_STATUSC_SERCOM3__Pos)             /**< (PAC_STATUSC) SERCOM3 APB Protect Enable Mask */
#define PAC_STATUSC_SERCOM3_(value)           (PAC_STATUSC_SERCOM3__Msk & ((value) << PAC_STATUSC_SERCOM3__Pos))
#define PAC_STATUSC_SERCOM4__Pos              (5U)                                           /**< (PAC_STATUSC) SERCOM4 APB Protect Enable Position */
#define PAC_STATUSC_SERCOM4__Msk              (0x1U << PAC_STATUSC_SERCOM4__Pos)             /**< (PAC_STATUSC) SERCOM4 APB Protect Enable Mask */
#define PAC_STATUSC_SERCOM4_(value)           (PAC_STATUSC_SERCOM4__Msk & ((value) << PAC_STATUSC_SERCOM4__Pos))
#define PAC_STATUSC_SERCOM5__Pos              (6U)                                           /**< (PAC_STATUSC) SERCOM5 APB Protect Enable Position */
#define PAC_STATUSC_SERCOM5__Msk              (0x1U << PAC_STATUSC_SERCOM5__Pos)             /**< (PAC_STATUSC) SERCOM5 APB Protect Enable Mask */
#define PAC_STATUSC_SERCOM5_(value)           (PAC_STATUSC_SERCOM5__Msk & ((value) << PAC_STATUSC_SERCOM5__Pos))
#define PAC_STATUSC_CAN0__Pos                 (7U)                                           /**< (PAC_STATUSC) CAN0 APB Protect Enable Position */
#define PAC_STATUSC_CAN0__Msk                 (0x1U << PAC_STATUSC_CAN0__Pos)                /**< (PAC_STATUSC) CAN0 APB Protect Enable Mask */
#define PAC_STATUSC_CAN0_(value)              (PAC_STATUSC_CAN0__Msk & ((value) << PAC_STATUSC_CAN0__Pos))
#define PAC_STATUSC_CAN1__Pos                 (8U)                                           /**< (PAC_STATUSC) CAN1 APB Protect Enable Position */
#define PAC_STATUSC_CAN1__Msk                 (0x1U << PAC_STATUSC_CAN1__Pos)                /**< (PAC_STATUSC) CAN1 APB Protect Enable Mask */
#define PAC_STATUSC_CAN1_(value)              (PAC_STATUSC_CAN1__Msk & ((value) << PAC_STATUSC_CAN1__Pos))
#define PAC_STATUSC_TCC0__Pos                 (9U)                                           /**< (PAC_STATUSC) TCC0 APB Protect Enable Position */
#define PAC_STATUSC_TCC0__Msk                 (0x1U << PAC_STATUSC_TCC0__Pos)                /**< (PAC_STATUSC) TCC0 APB Protect Enable Mask */
#define PAC_STATUSC_TCC0_(value)              (PAC_STATUSC_TCC0__Msk & ((value) << PAC_STATUSC_TCC0__Pos))
#define PAC_STATUSC_TCC1__Pos                 (10U)                                          /**< (PAC_STATUSC) TCC1 APB Protect Enable Position */
#define PAC_STATUSC_TCC1__Msk                 (0x1U << PAC_STATUSC_TCC1__Pos)                /**< (PAC_STATUSC) TCC1 APB Protect Enable Mask */
#define PAC_STATUSC_TCC1_(value)              (PAC_STATUSC_TCC1__Msk & ((value) << PAC_STATUSC_TCC1__Pos))
#define PAC_STATUSC_TCC2__Pos                 (11U)                                          /**< (PAC_STATUSC) TCC2 APB Protect Enable Position */
#define PAC_STATUSC_TCC2__Msk                 (0x1U << PAC_STATUSC_TCC2__Pos)                /**< (PAC_STATUSC) TCC2 APB Protect Enable Mask */
#define PAC_STATUSC_TCC2_(value)              (PAC_STATUSC_TCC2__Msk & ((value) << PAC_STATUSC_TCC2__Pos))
#define PAC_STATUSC_TC0__Pos                  (12U)                                          /**< (PAC_STATUSC) TC0 APB Protect Enable Position */
#define PAC_STATUSC_TC0__Msk                  (0x1U << PAC_STATUSC_TC0__Pos)                 /**< (PAC_STATUSC) TC0 APB Protect Enable Mask */
#define PAC_STATUSC_TC0_(value)               (PAC_STATUSC_TC0__Msk & ((value) << PAC_STATUSC_TC0__Pos))
#define PAC_STATUSC_TC1__Pos                  (13U)                                          /**< (PAC_STATUSC) TC1 APB Protect Enable Position */
#define PAC_STATUSC_TC1__Msk                  (0x1U << PAC_STATUSC_TC1__Pos)                 /**< (PAC_STATUSC) TC1 APB Protect Enable Mask */
#define PAC_STATUSC_TC1_(value)               (PAC_STATUSC_TC1__Msk & ((value) << PAC_STATUSC_TC1__Pos))
#define PAC_STATUSC_TC2__Pos                  (14U)                                          /**< (PAC_STATUSC) TC2 APB Protect Enable Position */
#define PAC_STATUSC_TC2__Msk                  (0x1U << PAC_STATUSC_TC2__Pos)                 /**< (PAC_STATUSC) TC2 APB Protect Enable Mask */
#define PAC_STATUSC_TC2_(value)               (PAC_STATUSC_TC2__Msk & ((value) << PAC_STATUSC_TC2__Pos))
#define PAC_STATUSC_TC3__Pos                  (15U)                                          /**< (PAC_STATUSC) TC3 APB Protect Enable Position */
#define PAC_STATUSC_TC3__Msk                  (0x1U << PAC_STATUSC_TC3__Pos)                 /**< (PAC_STATUSC) TC3 APB Protect Enable Mask */
#define PAC_STATUSC_TC3_(value)               (PAC_STATUSC_TC3__Msk & ((value) << PAC_STATUSC_TC3__Pos))
#define PAC_STATUSC_TC4__Pos                  (16U)                                          /**< (PAC_STATUSC) TC4 APB Protect Enable Position */
#define PAC_STATUSC_TC4__Msk                  (0x1U << PAC_STATUSC_TC4__Pos)                 /**< (PAC_STATUSC) TC4 APB Protect Enable Mask */
#define PAC_STATUSC_TC4_(value)               (PAC_STATUSC_TC4__Msk & ((value) << PAC_STATUSC_TC4__Pos))
#define PAC_STATUSC_ADC0__Pos                 (17U)                                          /**< (PAC_STATUSC) ADC0 APB Protect Enable Position */
#define PAC_STATUSC_ADC0__Msk                 (0x1U << PAC_STATUSC_ADC0__Pos)                /**< (PAC_STATUSC) ADC0 APB Protect Enable Mask */
#define PAC_STATUSC_ADC0_(value)              (PAC_STATUSC_ADC0__Msk & ((value) << PAC_STATUSC_ADC0__Pos))
#define PAC_STATUSC_ADC1__Pos                 (18U)                                          /**< (PAC_STATUSC) ADC1 APB Protect Enable Position */
#define PAC_STATUSC_ADC1__Msk                 (0x1U << PAC_STATUSC_ADC1__Pos)                /**< (PAC_STATUSC) ADC1 APB Protect Enable Mask */
#define PAC_STATUSC_ADC1_(value)              (PAC_STATUSC_ADC1__Msk & ((value) << PAC_STATUSC_ADC1__Pos))
#define PAC_STATUSC_SDADC__Pos                (19U)                                          /**< (PAC_STATUSC) SDADC APB Protect Enable Position */
#define PAC_STATUSC_SDADC__Msk                (0x1U << PAC_STATUSC_SDADC__Pos)               /**< (PAC_STATUSC) SDADC APB Protect Enable Mask */
#define PAC_STATUSC_SDADC_(value)             (PAC_STATUSC_SDADC__Msk & ((value) << PAC_STATUSC_SDADC__Pos))
#define PAC_STATUSC_AC__Pos                   (20U)                                          /**< (PAC_STATUSC) AC APB Protect Enable Position */
#define PAC_STATUSC_AC__Msk                   (0x1U << PAC_STATUSC_AC__Pos)                  /**< (PAC_STATUSC) AC APB Protect Enable Mask */
#define PAC_STATUSC_AC_(value)                (PAC_STATUSC_AC__Msk & ((value) << PAC_STATUSC_AC__Pos))
#define PAC_STATUSC_DAC__Pos                  (21U)                                          /**< (PAC_STATUSC) DAC APB Protect Enable Position */
#define PAC_STATUSC_DAC__Msk                  (0x1U << PAC_STATUSC_DAC__Pos)                 /**< (PAC_STATUSC) DAC APB Protect Enable Mask */
#define PAC_STATUSC_DAC_(value)               (PAC_STATUSC_DAC__Msk & ((value) << PAC_STATUSC_DAC__Pos))
#define PAC_STATUSC_PTC__Pos                  (22U)                                          /**< (PAC_STATUSC) PTC APB Protect Enable Position */
#define PAC_STATUSC_PTC__Msk                  (0x1U << PAC_STATUSC_PTC__Pos)                 /**< (PAC_STATUSC) PTC APB Protect Enable Mask */
#define PAC_STATUSC_PTC_(value)               (PAC_STATUSC_PTC__Msk & ((value) << PAC_STATUSC_PTC__Pos))
#define PAC_STATUSC_CCL__Pos                  (23U)                                          /**< (PAC_STATUSC) CCL APB Protect Enable Position */
#define PAC_STATUSC_CCL__Msk                  (0x1U << PAC_STATUSC_CCL__Pos)                 /**< (PAC_STATUSC) CCL APB Protect Enable Mask */
#define PAC_STATUSC_CCL_(value)               (PAC_STATUSC_CCL__Msk & ((value) << PAC_STATUSC_CCL__Pos))
#define PAC_STATUSC_Msk                       (0x00FFFFFFUL)                                 /**< (PAC_STATUSC) Register Mask  */

/* -------- PAC_STATUSD : (PAC Offset: 0x40) (R/  32) Peripheral write protection status - Bridge D -------- */
#define PAC_STATUSD_SERCOM6__Pos              (0U)                                           /**< (PAC_STATUSD) SERCOM6 APB Protect Enable Position */
#define PAC_STATUSD_SERCOM6__Msk              (0x1U << PAC_STATUSD_SERCOM6__Pos)             /**< (PAC_STATUSD) SERCOM6 APB Protect Enable Mask */
#define PAC_STATUSD_SERCOM6_(value)           (PAC_STATUSD_SERCOM6__Msk & ((value) << PAC_STATUSD_SERCOM6__Pos))
#define PAC_STATUSD_SERCOM7__Pos              (1U)                                           /**< (PAC_STATUSD) SERCOM7 APB Protect Enable Position */
#define PAC_STATUSD_SERCOM7__Msk              (0x1U << PAC_STATUSD_SERCOM7__Pos)             /**< (PAC_STATUSD) SERCOM7 APB Protect Enable Mask */
#define PAC_STATUSD_SERCOM7_(value)           (PAC_STATUSD_SERCOM7__Msk & ((value) << PAC_STATUSD_SERCOM7__Pos))
#define PAC_STATUSD_TC5__Pos                  (2U)                                           /**< (PAC_STATUSD) TC5 APB Protect Enable Position */
#define PAC_STATUSD_TC5__Msk                  (0x1U << PAC_STATUSD_TC5__Pos)                 /**< (PAC_STATUSD) TC5 APB Protect Enable Mask */
#define PAC_STATUSD_TC5_(value)               (PAC_STATUSD_TC5__Msk & ((value) << PAC_STATUSD_TC5__Pos))
#define PAC_STATUSD_TC6__Pos                  (3U)                                           /**< (PAC_STATUSD) TC6 APB Protect Enable Position */
#define PAC_STATUSD_TC6__Msk                  (0x1U << PAC_STATUSD_TC6__Pos)                 /**< (PAC_STATUSD) TC6 APB Protect Enable Mask */
#define PAC_STATUSD_TC6_(value)               (PAC_STATUSD_TC6__Msk & ((value) << PAC_STATUSD_TC6__Pos))
#define PAC_STATUSD_TC7__Pos                  (4U)                                           /**< (PAC_STATUSD) TC7 APB Protect Enable Position */
#define PAC_STATUSD_TC7__Msk                  (0x1U << PAC_STATUSD_TC7__Pos)                 /**< (PAC_STATUSD) TC7 APB Protect Enable Mask */
#define PAC_STATUSD_TC7_(value)               (PAC_STATUSD_TC7__Msk & ((value) << PAC_STATUSD_TC7__Pos))
#define PAC_STATUSD_Msk                       (0x0000001FUL)                                 /**< (PAC_STATUSD) Register Mask  */

/** \brief PAC register offsets definitions */
#define PAC_WRCTRL_OFFSET              (0x00)         /**< (PAC_WRCTRL) Write control Offset */
#define PAC_EVCTRL_OFFSET              (0x04)         /**< (PAC_EVCTRL) Event control Offset */
#define PAC_INTENCLR_OFFSET            (0x08)         /**< (PAC_INTENCLR) Interrupt enable clear Offset */
#define PAC_INTENSET_OFFSET            (0x09)         /**< (PAC_INTENSET) Interrupt enable set Offset */
#define PAC_INTFLAGAHB_OFFSET          (0x10)         /**< (PAC_INTFLAGAHB) Bridge interrupt flag status Offset */
#define PAC_INTFLAGA_OFFSET            (0x14)         /**< (PAC_INTFLAGA) Peripheral interrupt flag status - Bridge A Offset */
#define PAC_INTFLAGB_OFFSET            (0x18)         /**< (PAC_INTFLAGB) Peripheral interrupt flag status - Bridge B Offset */
#define PAC_INTFLAGC_OFFSET            (0x1C)         /**< (PAC_INTFLAGC) Peripheral interrupt flag status - Bridge C Offset */
#define PAC_INTFLAGD_OFFSET            (0x20)         /**< (PAC_INTFLAGD) Peripheral interrupt flag status - Bridge D Offset */
#define PAC_STATUSA_OFFSET             (0x34)         /**< (PAC_STATUSA) Peripheral write protection status - Bridge A Offset */
#define PAC_STATUSB_OFFSET             (0x38)         /**< (PAC_STATUSB) Peripheral write protection status - Bridge B Offset */
#define PAC_STATUSC_OFFSET             (0x3C)         /**< (PAC_STATUSC) Peripheral write protection status - Bridge C Offset */
#define PAC_STATUSD_OFFSET             (0x40)         /**< (PAC_STATUSD) Peripheral write protection status - Bridge D Offset */

/** \brief PAC register API structure */
typedef struct
{
  __IO  uint32_t                       PAC_WRCTRL;      /**< Offset: 0x00 (R/W  32) Write control */
  __IO  uint8_t                        PAC_EVCTRL;      /**< Offset: 0x04 (R/W  8) Event control */
  __I   uint8_t                        Reserved1[0x03];
  __IO  uint8_t                        PAC_INTENCLR;    /**< Offset: 0x08 (R/W  8) Interrupt enable clear */
  __IO  uint8_t                        PAC_INTENSET;    /**< Offset: 0x09 (R/W  8) Interrupt enable set */
  __I   uint8_t                        Reserved2[0x06];
  __IO  uint32_t                       PAC_INTFLAGAHB;  /**< Offset: 0x10 (R/W  32) Bridge interrupt flag status */
  __IO  uint32_t                       PAC_INTFLAGA;    /**< Offset: 0x14 (R/W  32) Peripheral interrupt flag status - Bridge A */
  __IO  uint32_t                       PAC_INTFLAGB;    /**< Offset: 0x18 (R/W  32) Peripheral interrupt flag status - Bridge B */
  __IO  uint32_t                       PAC_INTFLAGC;    /**< Offset: 0x1c (R/W  32) Peripheral interrupt flag status - Bridge C */
  __IO  uint32_t                       PAC_INTFLAGD;    /**< Offset: 0x20 (R/W  32) Peripheral interrupt flag status - Bridge D */
  __I   uint8_t                        Reserved3[0x10];
  __I   uint32_t                       PAC_STATUSA;     /**< Offset: 0x34 (R/   32) Peripheral write protection status - Bridge A */
  __I   uint32_t                       PAC_STATUSB;     /**< Offset: 0x38 (R/   32) Peripheral write protection status - Bridge B */
  __I   uint32_t                       PAC_STATUSC;     /**< Offset: 0x3c (R/   32) Peripheral write protection status - Bridge C */
  __I   uint32_t                       PAC_STATUSD;     /**< Offset: 0x40 (R/   32) Peripheral write protection status - Bridge D */
} pac_registers_t;
/** @}  end of Peripheral Access Controller */

#endif /* SAMC_SAMC21_PAC_MODULE_H */

