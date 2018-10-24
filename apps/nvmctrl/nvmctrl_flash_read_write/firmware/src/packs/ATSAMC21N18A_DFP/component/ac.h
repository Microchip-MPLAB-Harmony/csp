/**
 * \brief Header file for SAMC/SAMC21 AC
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
#ifndef SAMC_SAMC21_AC_MODULE_H
#define SAMC_SAMC21_AC_MODULE_H

/** \addtogroup SAMC_SAMC21 Analog Comparators
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_AC                                    */
/* ========================================================================== */

/* -------- AC_CTRLA : (AC Offset: 0x00) (R/W 8) Control A -------- */
#define AC_CTRLA_SWRST_Pos                    (0U)                                           /**< (AC_CTRLA) Software Reset Position */
#define AC_CTRLA_SWRST_Msk                    (0x1U << AC_CTRLA_SWRST_Pos)                   /**< (AC_CTRLA) Software Reset Mask */
#define AC_CTRLA_SWRST(value)                 (AC_CTRLA_SWRST_Msk & ((value) << AC_CTRLA_SWRST_Pos))
#define AC_CTRLA_ENABLE_Pos                   (1U)                                           /**< (AC_CTRLA) Enable Position */
#define AC_CTRLA_ENABLE_Msk                   (0x1U << AC_CTRLA_ENABLE_Pos)                  /**< (AC_CTRLA) Enable Mask */
#define AC_CTRLA_ENABLE(value)                (AC_CTRLA_ENABLE_Msk & ((value) << AC_CTRLA_ENABLE_Pos))
#define AC_CTRLA_Msk                          (0x00000003UL)                                 /**< (AC_CTRLA) Register Mask  */

/* -------- AC_CTRLB : (AC Offset: 0x01) ( /W 8) Control B -------- */
#define AC_CTRLB_START0_Pos                   (0U)                                           /**< (AC_CTRLB) Comparator 0 Start Comparison Position */
#define AC_CTRLB_START0_Msk                   (0x1U << AC_CTRLB_START0_Pos)                  /**< (AC_CTRLB) Comparator 0 Start Comparison Mask */
#define AC_CTRLB_START0(value)                (AC_CTRLB_START0_Msk & ((value) << AC_CTRLB_START0_Pos))
#define AC_CTRLB_START1_Pos                   (1U)                                           /**< (AC_CTRLB) Comparator 1 Start Comparison Position */
#define AC_CTRLB_START1_Msk                   (0x1U << AC_CTRLB_START1_Pos)                  /**< (AC_CTRLB) Comparator 1 Start Comparison Mask */
#define AC_CTRLB_START1(value)                (AC_CTRLB_START1_Msk & ((value) << AC_CTRLB_START1_Pos))
#define AC_CTRLB_START2_Pos                   (2U)                                           /**< (AC_CTRLB) Comparator 2 Start Comparison Position */
#define AC_CTRLB_START2_Msk                   (0x1U << AC_CTRLB_START2_Pos)                  /**< (AC_CTRLB) Comparator 2 Start Comparison Mask */
#define AC_CTRLB_START2(value)                (AC_CTRLB_START2_Msk & ((value) << AC_CTRLB_START2_Pos))
#define AC_CTRLB_START3_Pos                   (3U)                                           /**< (AC_CTRLB) Comparator 3 Start Comparison Position */
#define AC_CTRLB_START3_Msk                   (0x1U << AC_CTRLB_START3_Pos)                  /**< (AC_CTRLB) Comparator 3 Start Comparison Mask */
#define AC_CTRLB_START3(value)                (AC_CTRLB_START3_Msk & ((value) << AC_CTRLB_START3_Pos))
#define AC_CTRLB_Msk                          (0x0000000FUL)                                 /**< (AC_CTRLB) Register Mask  */

/* -------- AC_EVCTRL : (AC Offset: 0x02) (R/W 16) Event Control -------- */
#define AC_EVCTRL_COMPEO0_Pos                 (0U)                                           /**< (AC_EVCTRL) Comparator 0 Event Output Enable Position */
#define AC_EVCTRL_COMPEO0_Msk                 (0x1U << AC_EVCTRL_COMPEO0_Pos)                /**< (AC_EVCTRL) Comparator 0 Event Output Enable Mask */
#define AC_EVCTRL_COMPEO0(value)              (AC_EVCTRL_COMPEO0_Msk & ((value) << AC_EVCTRL_COMPEO0_Pos))
#define AC_EVCTRL_COMPEO1_Pos                 (1U)                                           /**< (AC_EVCTRL) Comparator 1 Event Output Enable Position */
#define AC_EVCTRL_COMPEO1_Msk                 (0x1U << AC_EVCTRL_COMPEO1_Pos)                /**< (AC_EVCTRL) Comparator 1 Event Output Enable Mask */
#define AC_EVCTRL_COMPEO1(value)              (AC_EVCTRL_COMPEO1_Msk & ((value) << AC_EVCTRL_COMPEO1_Pos))
#define AC_EVCTRL_COMPEO2_Pos                 (2U)                                           /**< (AC_EVCTRL) Comparator 2 Event Output Enable Position */
#define AC_EVCTRL_COMPEO2_Msk                 (0x1U << AC_EVCTRL_COMPEO2_Pos)                /**< (AC_EVCTRL) Comparator 2 Event Output Enable Mask */
#define AC_EVCTRL_COMPEO2(value)              (AC_EVCTRL_COMPEO2_Msk & ((value) << AC_EVCTRL_COMPEO2_Pos))
#define AC_EVCTRL_COMPEO3_Pos                 (3U)                                           /**< (AC_EVCTRL) Comparator 3 Event Output Enable Position */
#define AC_EVCTRL_COMPEO3_Msk                 (0x1U << AC_EVCTRL_COMPEO3_Pos)                /**< (AC_EVCTRL) Comparator 3 Event Output Enable Mask */
#define AC_EVCTRL_COMPEO3(value)              (AC_EVCTRL_COMPEO3_Msk & ((value) << AC_EVCTRL_COMPEO3_Pos))
#define AC_EVCTRL_WINEO0_Pos                  (4U)                                           /**< (AC_EVCTRL) Window 0 Event Output Enable Position */
#define AC_EVCTRL_WINEO0_Msk                  (0x1U << AC_EVCTRL_WINEO0_Pos)                 /**< (AC_EVCTRL) Window 0 Event Output Enable Mask */
#define AC_EVCTRL_WINEO0(value)               (AC_EVCTRL_WINEO0_Msk & ((value) << AC_EVCTRL_WINEO0_Pos))
#define AC_EVCTRL_WINEO1_Pos                  (5U)                                           /**< (AC_EVCTRL) Window 1 Event Output Enable Position */
#define AC_EVCTRL_WINEO1_Msk                  (0x1U << AC_EVCTRL_WINEO1_Pos)                 /**< (AC_EVCTRL) Window 1 Event Output Enable Mask */
#define AC_EVCTRL_WINEO1(value)               (AC_EVCTRL_WINEO1_Msk & ((value) << AC_EVCTRL_WINEO1_Pos))
#define AC_EVCTRL_COMPEI0_Pos                 (8U)                                           /**< (AC_EVCTRL) Comparator 0 Event Input Enable Position */
#define AC_EVCTRL_COMPEI0_Msk                 (0x1U << AC_EVCTRL_COMPEI0_Pos)                /**< (AC_EVCTRL) Comparator 0 Event Input Enable Mask */
#define AC_EVCTRL_COMPEI0(value)              (AC_EVCTRL_COMPEI0_Msk & ((value) << AC_EVCTRL_COMPEI0_Pos))
#define AC_EVCTRL_COMPEI1_Pos                 (9U)                                           /**< (AC_EVCTRL) Comparator 1 Event Input Enable Position */
#define AC_EVCTRL_COMPEI1_Msk                 (0x1U << AC_EVCTRL_COMPEI1_Pos)                /**< (AC_EVCTRL) Comparator 1 Event Input Enable Mask */
#define AC_EVCTRL_COMPEI1(value)              (AC_EVCTRL_COMPEI1_Msk & ((value) << AC_EVCTRL_COMPEI1_Pos))
#define AC_EVCTRL_COMPEI2_Pos                 (10U)                                          /**< (AC_EVCTRL) Comparator 2 Event Input Enable Position */
#define AC_EVCTRL_COMPEI2_Msk                 (0x1U << AC_EVCTRL_COMPEI2_Pos)                /**< (AC_EVCTRL) Comparator 2 Event Input Enable Mask */
#define AC_EVCTRL_COMPEI2(value)              (AC_EVCTRL_COMPEI2_Msk & ((value) << AC_EVCTRL_COMPEI2_Pos))
#define AC_EVCTRL_COMPEI3_Pos                 (11U)                                          /**< (AC_EVCTRL) Comparator 3 Event Input Enable Position */
#define AC_EVCTRL_COMPEI3_Msk                 (0x1U << AC_EVCTRL_COMPEI3_Pos)                /**< (AC_EVCTRL) Comparator 3 Event Input Enable Mask */
#define AC_EVCTRL_COMPEI3(value)              (AC_EVCTRL_COMPEI3_Msk & ((value) << AC_EVCTRL_COMPEI3_Pos))
#define AC_EVCTRL_INVEI0_Pos                  (12U)                                          /**< (AC_EVCTRL) Comparator 0 Input Event Invert Enable Position */
#define AC_EVCTRL_INVEI0_Msk                  (0x1U << AC_EVCTRL_INVEI0_Pos)                 /**< (AC_EVCTRL) Comparator 0 Input Event Invert Enable Mask */
#define AC_EVCTRL_INVEI0(value)               (AC_EVCTRL_INVEI0_Msk & ((value) << AC_EVCTRL_INVEI0_Pos))
#define AC_EVCTRL_INVEI1_Pos                  (13U)                                          /**< (AC_EVCTRL) Comparator 1 Input Event Invert Enable Position */
#define AC_EVCTRL_INVEI1_Msk                  (0x1U << AC_EVCTRL_INVEI1_Pos)                 /**< (AC_EVCTRL) Comparator 1 Input Event Invert Enable Mask */
#define AC_EVCTRL_INVEI1(value)               (AC_EVCTRL_INVEI1_Msk & ((value) << AC_EVCTRL_INVEI1_Pos))
#define AC_EVCTRL_INVEI2_Pos                  (14U)                                          /**< (AC_EVCTRL) Comparator 2 Input Event Invert Enable Position */
#define AC_EVCTRL_INVEI2_Msk                  (0x1U << AC_EVCTRL_INVEI2_Pos)                 /**< (AC_EVCTRL) Comparator 2 Input Event Invert Enable Mask */
#define AC_EVCTRL_INVEI2(value)               (AC_EVCTRL_INVEI2_Msk & ((value) << AC_EVCTRL_INVEI2_Pos))
#define AC_EVCTRL_INVEI3_Pos                  (15U)                                          /**< (AC_EVCTRL) Comparator 3 Input Event Invert Enable Position */
#define AC_EVCTRL_INVEI3_Msk                  (0x1U << AC_EVCTRL_INVEI3_Pos)                 /**< (AC_EVCTRL) Comparator 3 Input Event Invert Enable Mask */
#define AC_EVCTRL_INVEI3(value)               (AC_EVCTRL_INVEI3_Msk & ((value) << AC_EVCTRL_INVEI3_Pos))
#define AC_EVCTRL_Msk                         (0x0000FF3FUL)                                 /**< (AC_EVCTRL) Register Mask  */

/* -------- AC_INTENCLR : (AC Offset: 0x04) (R/W 8) Interrupt Enable Clear -------- */
#define AC_INTENCLR_COMP0_Pos                 (0U)                                           /**< (AC_INTENCLR) Comparator 0 Interrupt Enable Position */
#define AC_INTENCLR_COMP0_Msk                 (0x1U << AC_INTENCLR_COMP0_Pos)                /**< (AC_INTENCLR) Comparator 0 Interrupt Enable Mask */
#define AC_INTENCLR_COMP0(value)              (AC_INTENCLR_COMP0_Msk & ((value) << AC_INTENCLR_COMP0_Pos))
#define AC_INTENCLR_COMP1_Pos                 (1U)                                           /**< (AC_INTENCLR) Comparator 1 Interrupt Enable Position */
#define AC_INTENCLR_COMP1_Msk                 (0x1U << AC_INTENCLR_COMP1_Pos)                /**< (AC_INTENCLR) Comparator 1 Interrupt Enable Mask */
#define AC_INTENCLR_COMP1(value)              (AC_INTENCLR_COMP1_Msk & ((value) << AC_INTENCLR_COMP1_Pos))
#define AC_INTENCLR_COMP2_Pos                 (2U)                                           /**< (AC_INTENCLR) Comparator 2 Interrupt Enable Position */
#define AC_INTENCLR_COMP2_Msk                 (0x1U << AC_INTENCLR_COMP2_Pos)                /**< (AC_INTENCLR) Comparator 2 Interrupt Enable Mask */
#define AC_INTENCLR_COMP2(value)              (AC_INTENCLR_COMP2_Msk & ((value) << AC_INTENCLR_COMP2_Pos))
#define AC_INTENCLR_COMP3_Pos                 (3U)                                           /**< (AC_INTENCLR) Comparator 3 Interrupt Enable Position */
#define AC_INTENCLR_COMP3_Msk                 (0x1U << AC_INTENCLR_COMP3_Pos)                /**< (AC_INTENCLR) Comparator 3 Interrupt Enable Mask */
#define AC_INTENCLR_COMP3(value)              (AC_INTENCLR_COMP3_Msk & ((value) << AC_INTENCLR_COMP3_Pos))
#define AC_INTENCLR_WIN0_Pos                  (4U)                                           /**< (AC_INTENCLR) Window 0 Interrupt Enable Position */
#define AC_INTENCLR_WIN0_Msk                  (0x1U << AC_INTENCLR_WIN0_Pos)                 /**< (AC_INTENCLR) Window 0 Interrupt Enable Mask */
#define AC_INTENCLR_WIN0(value)               (AC_INTENCLR_WIN0_Msk & ((value) << AC_INTENCLR_WIN0_Pos))
#define AC_INTENCLR_WIN1_Pos                  (5U)                                           /**< (AC_INTENCLR) Window 1 Interrupt Enable Position */
#define AC_INTENCLR_WIN1_Msk                  (0x1U << AC_INTENCLR_WIN1_Pos)                 /**< (AC_INTENCLR) Window 1 Interrupt Enable Mask */
#define AC_INTENCLR_WIN1(value)               (AC_INTENCLR_WIN1_Msk & ((value) << AC_INTENCLR_WIN1_Pos))
#define AC_INTENCLR_Msk                       (0x0000003FUL)                                 /**< (AC_INTENCLR) Register Mask  */

/* -------- AC_INTENSET : (AC Offset: 0x05) (R/W 8) Interrupt Enable Set -------- */
#define AC_INTENSET_COMP0_Pos                 (0U)                                           /**< (AC_INTENSET) Comparator 0 Interrupt Enable Position */
#define AC_INTENSET_COMP0_Msk                 (0x1U << AC_INTENSET_COMP0_Pos)                /**< (AC_INTENSET) Comparator 0 Interrupt Enable Mask */
#define AC_INTENSET_COMP0(value)              (AC_INTENSET_COMP0_Msk & ((value) << AC_INTENSET_COMP0_Pos))
#define AC_INTENSET_COMP1_Pos                 (1U)                                           /**< (AC_INTENSET) Comparator 1 Interrupt Enable Position */
#define AC_INTENSET_COMP1_Msk                 (0x1U << AC_INTENSET_COMP1_Pos)                /**< (AC_INTENSET) Comparator 1 Interrupt Enable Mask */
#define AC_INTENSET_COMP1(value)              (AC_INTENSET_COMP1_Msk & ((value) << AC_INTENSET_COMP1_Pos))
#define AC_INTENSET_COMP2_Pos                 (2U)                                           /**< (AC_INTENSET) Comparator 2 Interrupt Enable Position */
#define AC_INTENSET_COMP2_Msk                 (0x1U << AC_INTENSET_COMP2_Pos)                /**< (AC_INTENSET) Comparator 2 Interrupt Enable Mask */
#define AC_INTENSET_COMP2(value)              (AC_INTENSET_COMP2_Msk & ((value) << AC_INTENSET_COMP2_Pos))
#define AC_INTENSET_COMP3_Pos                 (3U)                                           /**< (AC_INTENSET) Comparator 3 Interrupt Enable Position */
#define AC_INTENSET_COMP3_Msk                 (0x1U << AC_INTENSET_COMP3_Pos)                /**< (AC_INTENSET) Comparator 3 Interrupt Enable Mask */
#define AC_INTENSET_COMP3(value)              (AC_INTENSET_COMP3_Msk & ((value) << AC_INTENSET_COMP3_Pos))
#define AC_INTENSET_WIN0_Pos                  (4U)                                           /**< (AC_INTENSET) Window 0 Interrupt Enable Position */
#define AC_INTENSET_WIN0_Msk                  (0x1U << AC_INTENSET_WIN0_Pos)                 /**< (AC_INTENSET) Window 0 Interrupt Enable Mask */
#define AC_INTENSET_WIN0(value)               (AC_INTENSET_WIN0_Msk & ((value) << AC_INTENSET_WIN0_Pos))
#define AC_INTENSET_WIN1_Pos                  (5U)                                           /**< (AC_INTENSET) Window 1 Interrupt Enable Position */
#define AC_INTENSET_WIN1_Msk                  (0x1U << AC_INTENSET_WIN1_Pos)                 /**< (AC_INTENSET) Window 1 Interrupt Enable Mask */
#define AC_INTENSET_WIN1(value)               (AC_INTENSET_WIN1_Msk & ((value) << AC_INTENSET_WIN1_Pos))
#define AC_INTENSET_Msk                       (0x0000003FUL)                                 /**< (AC_INTENSET) Register Mask  */

/* -------- AC_INTFLAG : (AC Offset: 0x06) (R/W 8) Interrupt Flag Status and Clear -------- */
#define AC_INTFLAG_COMP0_Pos                  (0U)                                           /**< (AC_INTFLAG) Comparator 0 Position */
#define AC_INTFLAG_COMP0_Msk                  (0x1U << AC_INTFLAG_COMP0_Pos)                 /**< (AC_INTFLAG) Comparator 0 Mask */
#define AC_INTFLAG_COMP0(value)               (AC_INTFLAG_COMP0_Msk & ((value) << AC_INTFLAG_COMP0_Pos))
#define AC_INTFLAG_COMP1_Pos                  (1U)                                           /**< (AC_INTFLAG) Comparator 1 Position */
#define AC_INTFLAG_COMP1_Msk                  (0x1U << AC_INTFLAG_COMP1_Pos)                 /**< (AC_INTFLAG) Comparator 1 Mask */
#define AC_INTFLAG_COMP1(value)               (AC_INTFLAG_COMP1_Msk & ((value) << AC_INTFLAG_COMP1_Pos))
#define AC_INTFLAG_COMP2_Pos                  (2U)                                           /**< (AC_INTFLAG) Comparator 2 Position */
#define AC_INTFLAG_COMP2_Msk                  (0x1U << AC_INTFLAG_COMP2_Pos)                 /**< (AC_INTFLAG) Comparator 2 Mask */
#define AC_INTFLAG_COMP2(value)               (AC_INTFLAG_COMP2_Msk & ((value) << AC_INTFLAG_COMP2_Pos))
#define AC_INTFLAG_COMP3_Pos                  (3U)                                           /**< (AC_INTFLAG) Comparator 3 Position */
#define AC_INTFLAG_COMP3_Msk                  (0x1U << AC_INTFLAG_COMP3_Pos)                 /**< (AC_INTFLAG) Comparator 3 Mask */
#define AC_INTFLAG_COMP3(value)               (AC_INTFLAG_COMP3_Msk & ((value) << AC_INTFLAG_COMP3_Pos))
#define AC_INTFLAG_WIN0_Pos                   (4U)                                           /**< (AC_INTFLAG) Window 0 Position */
#define AC_INTFLAG_WIN0_Msk                   (0x1U << AC_INTFLAG_WIN0_Pos)                  /**< (AC_INTFLAG) Window 0 Mask */
#define AC_INTFLAG_WIN0(value)                (AC_INTFLAG_WIN0_Msk & ((value) << AC_INTFLAG_WIN0_Pos))
#define AC_INTFLAG_WIN1_Pos                   (5U)                                           /**< (AC_INTFLAG) Window 1 Position */
#define AC_INTFLAG_WIN1_Msk                   (0x1U << AC_INTFLAG_WIN1_Pos)                  /**< (AC_INTFLAG) Window 1 Mask */
#define AC_INTFLAG_WIN1(value)                (AC_INTFLAG_WIN1_Msk & ((value) << AC_INTFLAG_WIN1_Pos))
#define AC_INTFLAG_Msk                        (0x0000003FUL)                                 /**< (AC_INTFLAG) Register Mask  */

/* -------- AC_STATUSA : (AC Offset: 0x07) (R/  8) Status A -------- */
#define AC_STATUSA_STATE0_Pos                 (0U)                                           /**< (AC_STATUSA) Comparator 0 Current State Position */
#define AC_STATUSA_STATE0_Msk                 (0x1U << AC_STATUSA_STATE0_Pos)                /**< (AC_STATUSA) Comparator 0 Current State Mask */
#define AC_STATUSA_STATE0(value)              (AC_STATUSA_STATE0_Msk & ((value) << AC_STATUSA_STATE0_Pos))
#define AC_STATUSA_STATE1_Pos                 (1U)                                           /**< (AC_STATUSA) Comparator 1 Current State Position */
#define AC_STATUSA_STATE1_Msk                 (0x1U << AC_STATUSA_STATE1_Pos)                /**< (AC_STATUSA) Comparator 1 Current State Mask */
#define AC_STATUSA_STATE1(value)              (AC_STATUSA_STATE1_Msk & ((value) << AC_STATUSA_STATE1_Pos))
#define AC_STATUSA_STATE2_Pos                 (2U)                                           /**< (AC_STATUSA) Comparator 2 Current State Position */
#define AC_STATUSA_STATE2_Msk                 (0x1U << AC_STATUSA_STATE2_Pos)                /**< (AC_STATUSA) Comparator 2 Current State Mask */
#define AC_STATUSA_STATE2(value)              (AC_STATUSA_STATE2_Msk & ((value) << AC_STATUSA_STATE2_Pos))
#define AC_STATUSA_STATE3_Pos                 (3U)                                           /**< (AC_STATUSA) Comparator 3 Current State Position */
#define AC_STATUSA_STATE3_Msk                 (0x1U << AC_STATUSA_STATE3_Pos)                /**< (AC_STATUSA) Comparator 3 Current State Mask */
#define AC_STATUSA_STATE3(value)              (AC_STATUSA_STATE3_Msk & ((value) << AC_STATUSA_STATE3_Pos))
#define AC_STATUSA_WSTATE0_Pos                (4U)                                           /**< (AC_STATUSA) Window 0 Current State Position */
#define AC_STATUSA_WSTATE0_Msk                (0x3U << AC_STATUSA_WSTATE0_Pos)               /**< (AC_STATUSA) Window 0 Current State Mask */
#define AC_STATUSA_WSTATE0(value)             (AC_STATUSA_WSTATE0_Msk & ((value) << AC_STATUSA_WSTATE0_Pos))
#define   AC_STATUSA_WSTATE0_ABOVE_Val        (0U)                                           /**< (AC_STATUSA) Signal is above window  */
#define   AC_STATUSA_WSTATE0_INSIDE_Val       (1U)                                           /**< (AC_STATUSA) Signal is inside window  */
#define   AC_STATUSA_WSTATE0_BELOW_Val        (2U)                                           /**< (AC_STATUSA) Signal is below window  */
#define AC_STATUSA_WSTATE0_ABOVE              (AC_STATUSA_WSTATE0_ABOVE_Val << AC_STATUSA_WSTATE0_Pos) /**< (AC_STATUSA) Signal is above window Position  */
#define AC_STATUSA_WSTATE0_INSIDE             (AC_STATUSA_WSTATE0_INSIDE_Val << AC_STATUSA_WSTATE0_Pos) /**< (AC_STATUSA) Signal is inside window Position  */
#define AC_STATUSA_WSTATE0_BELOW              (AC_STATUSA_WSTATE0_BELOW_Val << AC_STATUSA_WSTATE0_Pos) /**< (AC_STATUSA) Signal is below window Position  */
#define AC_STATUSA_WSTATE1_Pos                (6U)                                           /**< (AC_STATUSA) Window 1 Current State Position */
#define AC_STATUSA_WSTATE1_Msk                (0x3U << AC_STATUSA_WSTATE1_Pos)               /**< (AC_STATUSA) Window 1 Current State Mask */
#define AC_STATUSA_WSTATE1(value)             (AC_STATUSA_WSTATE1_Msk & ((value) << AC_STATUSA_WSTATE1_Pos))
#define   AC_STATUSA_WSTATE1_ABOVE_Val        (0U)                                           /**< (AC_STATUSA) Signal is above window  */
#define   AC_STATUSA_WSTATE1_INSIDE_Val       (1U)                                           /**< (AC_STATUSA) Signal is inside window  */
#define   AC_STATUSA_WSTATE1_BELOW_Val        (2U)                                           /**< (AC_STATUSA) Signal is below window  */
#define AC_STATUSA_WSTATE1_ABOVE              (AC_STATUSA_WSTATE1_ABOVE_Val << AC_STATUSA_WSTATE1_Pos) /**< (AC_STATUSA) Signal is above window Position  */
#define AC_STATUSA_WSTATE1_INSIDE             (AC_STATUSA_WSTATE1_INSIDE_Val << AC_STATUSA_WSTATE1_Pos) /**< (AC_STATUSA) Signal is inside window Position  */
#define AC_STATUSA_WSTATE1_BELOW              (AC_STATUSA_WSTATE1_BELOW_Val << AC_STATUSA_WSTATE1_Pos) /**< (AC_STATUSA) Signal is below window Position  */
#define AC_STATUSA_Msk                        (0x000000FFUL)                                 /**< (AC_STATUSA) Register Mask  */

/* -------- AC_STATUSB : (AC Offset: 0x08) (R/  8) Status B -------- */
#define AC_STATUSB_READY0_Pos                 (0U)                                           /**< (AC_STATUSB) Comparator 0 Ready Position */
#define AC_STATUSB_READY0_Msk                 (0x1U << AC_STATUSB_READY0_Pos)                /**< (AC_STATUSB) Comparator 0 Ready Mask */
#define AC_STATUSB_READY0(value)              (AC_STATUSB_READY0_Msk & ((value) << AC_STATUSB_READY0_Pos))
#define AC_STATUSB_READY1_Pos                 (1U)                                           /**< (AC_STATUSB) Comparator 1 Ready Position */
#define AC_STATUSB_READY1_Msk                 (0x1U << AC_STATUSB_READY1_Pos)                /**< (AC_STATUSB) Comparator 1 Ready Mask */
#define AC_STATUSB_READY1(value)              (AC_STATUSB_READY1_Msk & ((value) << AC_STATUSB_READY1_Pos))
#define AC_STATUSB_READY2_Pos                 (2U)                                           /**< (AC_STATUSB) Comparator 2 Ready Position */
#define AC_STATUSB_READY2_Msk                 (0x1U << AC_STATUSB_READY2_Pos)                /**< (AC_STATUSB) Comparator 2 Ready Mask */
#define AC_STATUSB_READY2(value)              (AC_STATUSB_READY2_Msk & ((value) << AC_STATUSB_READY2_Pos))
#define AC_STATUSB_READY3_Pos                 (3U)                                           /**< (AC_STATUSB) Comparator 3 Ready Position */
#define AC_STATUSB_READY3_Msk                 (0x1U << AC_STATUSB_READY3_Pos)                /**< (AC_STATUSB) Comparator 3 Ready Mask */
#define AC_STATUSB_READY3(value)              (AC_STATUSB_READY3_Msk & ((value) << AC_STATUSB_READY3_Pos))
#define AC_STATUSB_Msk                        (0x0000000FUL)                                 /**< (AC_STATUSB) Register Mask  */

/* -------- AC_DBGCTRL : (AC Offset: 0x09) (R/W 8) Debug Control -------- */
#define AC_DBGCTRL_DBGRUN_Pos                 (0U)                                           /**< (AC_DBGCTRL) Debug Run Position */
#define AC_DBGCTRL_DBGRUN_Msk                 (0x1U << AC_DBGCTRL_DBGRUN_Pos)                /**< (AC_DBGCTRL) Debug Run Mask */
#define AC_DBGCTRL_DBGRUN(value)              (AC_DBGCTRL_DBGRUN_Msk & ((value) << AC_DBGCTRL_DBGRUN_Pos))
#define AC_DBGCTRL_Msk                        (0x00000001UL)                                 /**< (AC_DBGCTRL) Register Mask  */

/* -------- AC_WINCTRL : (AC Offset: 0x0A) (R/W 8) Window Control -------- */
#define AC_WINCTRL_WEN0_Pos                   (0U)                                           /**< (AC_WINCTRL) Window 0 Mode Enable Position */
#define AC_WINCTRL_WEN0_Msk                   (0x1U << AC_WINCTRL_WEN0_Pos)                  /**< (AC_WINCTRL) Window 0 Mode Enable Mask */
#define AC_WINCTRL_WEN0(value)                (AC_WINCTRL_WEN0_Msk & ((value) << AC_WINCTRL_WEN0_Pos))
#define AC_WINCTRL_WINTSEL0_Pos               (1U)                                           /**< (AC_WINCTRL) Window 0 Interrupt Selection Position */
#define AC_WINCTRL_WINTSEL0_Msk               (0x3U << AC_WINCTRL_WINTSEL0_Pos)              /**< (AC_WINCTRL) Window 0 Interrupt Selection Mask */
#define AC_WINCTRL_WINTSEL0(value)            (AC_WINCTRL_WINTSEL0_Msk & ((value) << AC_WINCTRL_WINTSEL0_Pos))
#define   AC_WINCTRL_WINTSEL0_ABOVE_Val       (0U)                                           /**< (AC_WINCTRL) Interrupt on signal above window  */
#define   AC_WINCTRL_WINTSEL0_INSIDE_Val      (1U)                                           /**< (AC_WINCTRL) Interrupt on signal inside window  */
#define   AC_WINCTRL_WINTSEL0_BELOW_Val       (2U)                                           /**< (AC_WINCTRL) Interrupt on signal below window  */
#define   AC_WINCTRL_WINTSEL0_OUTSIDE_Val     (3U)                                           /**< (AC_WINCTRL) Interrupt on signal outside window  */
#define AC_WINCTRL_WINTSEL0_ABOVE             (AC_WINCTRL_WINTSEL0_ABOVE_Val << AC_WINCTRL_WINTSEL0_Pos) /**< (AC_WINCTRL) Interrupt on signal above window Position  */
#define AC_WINCTRL_WINTSEL0_INSIDE            (AC_WINCTRL_WINTSEL0_INSIDE_Val << AC_WINCTRL_WINTSEL0_Pos) /**< (AC_WINCTRL) Interrupt on signal inside window Position  */
#define AC_WINCTRL_WINTSEL0_BELOW             (AC_WINCTRL_WINTSEL0_BELOW_Val << AC_WINCTRL_WINTSEL0_Pos) /**< (AC_WINCTRL) Interrupt on signal below window Position  */
#define AC_WINCTRL_WINTSEL0_OUTSIDE           (AC_WINCTRL_WINTSEL0_OUTSIDE_Val << AC_WINCTRL_WINTSEL0_Pos) /**< (AC_WINCTRL) Interrupt on signal outside window Position  */
#define AC_WINCTRL_WEN1_Pos                   (4U)                                           /**< (AC_WINCTRL) Window 1 Mode Enable Position */
#define AC_WINCTRL_WEN1_Msk                   (0x1U << AC_WINCTRL_WEN1_Pos)                  /**< (AC_WINCTRL) Window 1 Mode Enable Mask */
#define AC_WINCTRL_WEN1(value)                (AC_WINCTRL_WEN1_Msk & ((value) << AC_WINCTRL_WEN1_Pos))
#define AC_WINCTRL_WINTSEL1_Pos               (5U)                                           /**< (AC_WINCTRL) Window 1 Interrupt Selection Position */
#define AC_WINCTRL_WINTSEL1_Msk               (0x3U << AC_WINCTRL_WINTSEL1_Pos)              /**< (AC_WINCTRL) Window 1 Interrupt Selection Mask */
#define AC_WINCTRL_WINTSEL1(value)            (AC_WINCTRL_WINTSEL1_Msk & ((value) << AC_WINCTRL_WINTSEL1_Pos))
#define   AC_WINCTRL_WINTSEL1_ABOVE_Val       (0U)                                           /**< (AC_WINCTRL) Interrupt on signal above window  */
#define   AC_WINCTRL_WINTSEL1_INSIDE_Val      (1U)                                           /**< (AC_WINCTRL) Interrupt on signal inside window  */
#define   AC_WINCTRL_WINTSEL1_BELOW_Val       (2U)                                           /**< (AC_WINCTRL) Interrupt on signal below window  */
#define   AC_WINCTRL_WINTSEL1_OUTSIDE_Val     (3U)                                           /**< (AC_WINCTRL) Interrupt on signal outside window  */
#define AC_WINCTRL_WINTSEL1_ABOVE             (AC_WINCTRL_WINTSEL1_ABOVE_Val << AC_WINCTRL_WINTSEL1_Pos) /**< (AC_WINCTRL) Interrupt on signal above window Position  */
#define AC_WINCTRL_WINTSEL1_INSIDE            (AC_WINCTRL_WINTSEL1_INSIDE_Val << AC_WINCTRL_WINTSEL1_Pos) /**< (AC_WINCTRL) Interrupt on signal inside window Position  */
#define AC_WINCTRL_WINTSEL1_BELOW             (AC_WINCTRL_WINTSEL1_BELOW_Val << AC_WINCTRL_WINTSEL1_Pos) /**< (AC_WINCTRL) Interrupt on signal below window Position  */
#define AC_WINCTRL_WINTSEL1_OUTSIDE           (AC_WINCTRL_WINTSEL1_OUTSIDE_Val << AC_WINCTRL_WINTSEL1_Pos) /**< (AC_WINCTRL) Interrupt on signal outside window Position  */
#define AC_WINCTRL_Msk                        (0x00000077UL)                                 /**< (AC_WINCTRL) Register Mask  */

/* -------- AC_SCALER : (AC Offset: 0x0C) (R/W 8) Scaler n -------- */
#define AC_SCALER_VALUE_Pos                   (0U)                                           /**< (AC_SCALER) Scaler Value Position */
#define AC_SCALER_VALUE_Msk                   (0x3FU << AC_SCALER_VALUE_Pos)                 /**< (AC_SCALER) Scaler Value Mask */
#define AC_SCALER_VALUE(value)                (AC_SCALER_VALUE_Msk & ((value) << AC_SCALER_VALUE_Pos))
#define AC_SCALER_Msk                         (0x0000003FUL)                                 /**< (AC_SCALER) Register Mask  */

/* -------- AC_COMPCTRL : (AC Offset: 0x10) (R/W 32) Comparator Control n -------- */
#define AC_COMPCTRL_ENABLE_Pos                (1U)                                           /**< (AC_COMPCTRL) Enable Position */
#define AC_COMPCTRL_ENABLE_Msk                (0x1U << AC_COMPCTRL_ENABLE_Pos)               /**< (AC_COMPCTRL) Enable Mask */
#define AC_COMPCTRL_ENABLE(value)             (AC_COMPCTRL_ENABLE_Msk & ((value) << AC_COMPCTRL_ENABLE_Pos))
#define AC_COMPCTRL_SINGLE_Pos                (2U)                                           /**< (AC_COMPCTRL) Single-Shot Mode Position */
#define AC_COMPCTRL_SINGLE_Msk                (0x1U << AC_COMPCTRL_SINGLE_Pos)               /**< (AC_COMPCTRL) Single-Shot Mode Mask */
#define AC_COMPCTRL_SINGLE(value)             (AC_COMPCTRL_SINGLE_Msk & ((value) << AC_COMPCTRL_SINGLE_Pos))
#define AC_COMPCTRL_INTSEL_Pos                (3U)                                           /**< (AC_COMPCTRL) Interrupt Selection Position */
#define AC_COMPCTRL_INTSEL_Msk                (0x3U << AC_COMPCTRL_INTSEL_Pos)               /**< (AC_COMPCTRL) Interrupt Selection Mask */
#define AC_COMPCTRL_INTSEL(value)             (AC_COMPCTRL_INTSEL_Msk & ((value) << AC_COMPCTRL_INTSEL_Pos))
#define   AC_COMPCTRL_INTSEL_TOGGLE_Val       (0U)                                           /**< (AC_COMPCTRL) Interrupt on comparator output toggle  */
#define   AC_COMPCTRL_INTSEL_RISING_Val       (1U)                                           /**< (AC_COMPCTRL) Interrupt on comparator output rising  */
#define   AC_COMPCTRL_INTSEL_FALLING_Val      (2U)                                           /**< (AC_COMPCTRL) Interrupt on comparator output falling  */
#define   AC_COMPCTRL_INTSEL_EOC_Val          (3U)                                           /**< (AC_COMPCTRL) Interrupt on end of comparison (single-shot mode only)  */
#define AC_COMPCTRL_INTSEL_TOGGLE             (AC_COMPCTRL_INTSEL_TOGGLE_Val << AC_COMPCTRL_INTSEL_Pos) /**< (AC_COMPCTRL) Interrupt on comparator output toggle Position  */
#define AC_COMPCTRL_INTSEL_RISING             (AC_COMPCTRL_INTSEL_RISING_Val << AC_COMPCTRL_INTSEL_Pos) /**< (AC_COMPCTRL) Interrupt on comparator output rising Position  */
#define AC_COMPCTRL_INTSEL_FALLING            (AC_COMPCTRL_INTSEL_FALLING_Val << AC_COMPCTRL_INTSEL_Pos) /**< (AC_COMPCTRL) Interrupt on comparator output falling Position  */
#define AC_COMPCTRL_INTSEL_EOC                (AC_COMPCTRL_INTSEL_EOC_Val << AC_COMPCTRL_INTSEL_Pos) /**< (AC_COMPCTRL) Interrupt on end of comparison (single-shot mode only) Position  */
#define AC_COMPCTRL_RUNSTDBY_Pos              (6U)                                           /**< (AC_COMPCTRL) Run in Standby Position */
#define AC_COMPCTRL_RUNSTDBY_Msk              (0x1U << AC_COMPCTRL_RUNSTDBY_Pos)             /**< (AC_COMPCTRL) Run in Standby Mask */
#define AC_COMPCTRL_RUNSTDBY(value)           (AC_COMPCTRL_RUNSTDBY_Msk & ((value) << AC_COMPCTRL_RUNSTDBY_Pos))
#define AC_COMPCTRL_MUXNEG_Pos                (8U)                                           /**< (AC_COMPCTRL) Negative Input Mux Selection Position */
#define AC_COMPCTRL_MUXNEG_Msk                (0x7U << AC_COMPCTRL_MUXNEG_Pos)               /**< (AC_COMPCTRL) Negative Input Mux Selection Mask */
#define AC_COMPCTRL_MUXNEG(value)             (AC_COMPCTRL_MUXNEG_Msk & ((value) << AC_COMPCTRL_MUXNEG_Pos))
#define   AC_COMPCTRL_MUXNEG_PIN0_Val         (0U)                                           /**< (AC_COMPCTRL) I/O pin 0  */
#define   AC_COMPCTRL_MUXNEG_PIN1_Val         (1U)                                           /**< (AC_COMPCTRL) I/O pin 1  */
#define   AC_COMPCTRL_MUXNEG_PIN2_Val         (2U)                                           /**< (AC_COMPCTRL) I/O pin 2  */
#define   AC_COMPCTRL_MUXNEG_PIN3_Val         (3U)                                           /**< (AC_COMPCTRL) I/O pin 3  */
#define   AC_COMPCTRL_MUXNEG_GND_Val          (4U)                                           /**< (AC_COMPCTRL) Ground  */
#define   AC_COMPCTRL_MUXNEG_VSCALE_Val       (5U)                                           /**< (AC_COMPCTRL) VDD scaler  */
#define   AC_COMPCTRL_MUXNEG_BANDGAP_Val      (6U)                                           /**< (AC_COMPCTRL) Internal bandgap voltage  */
#define   AC_COMPCTRL_MUXNEG_DAC_Val          (7U)                                           /**< (AC_COMPCTRL) DAC output  */
#define AC_COMPCTRL_MUXNEG_PIN0               (AC_COMPCTRL_MUXNEG_PIN0_Val << AC_COMPCTRL_MUXNEG_Pos) /**< (AC_COMPCTRL) I/O pin 0 Position  */
#define AC_COMPCTRL_MUXNEG_PIN1               (AC_COMPCTRL_MUXNEG_PIN1_Val << AC_COMPCTRL_MUXNEG_Pos) /**< (AC_COMPCTRL) I/O pin 1 Position  */
#define AC_COMPCTRL_MUXNEG_PIN2               (AC_COMPCTRL_MUXNEG_PIN2_Val << AC_COMPCTRL_MUXNEG_Pos) /**< (AC_COMPCTRL) I/O pin 2 Position  */
#define AC_COMPCTRL_MUXNEG_PIN3               (AC_COMPCTRL_MUXNEG_PIN3_Val << AC_COMPCTRL_MUXNEG_Pos) /**< (AC_COMPCTRL) I/O pin 3 Position  */
#define AC_COMPCTRL_MUXNEG_GND                (AC_COMPCTRL_MUXNEG_GND_Val << AC_COMPCTRL_MUXNEG_Pos) /**< (AC_COMPCTRL) Ground Position  */
#define AC_COMPCTRL_MUXNEG_VSCALE             (AC_COMPCTRL_MUXNEG_VSCALE_Val << AC_COMPCTRL_MUXNEG_Pos) /**< (AC_COMPCTRL) VDD scaler Position  */
#define AC_COMPCTRL_MUXNEG_BANDGAP            (AC_COMPCTRL_MUXNEG_BANDGAP_Val << AC_COMPCTRL_MUXNEG_Pos) /**< (AC_COMPCTRL) Internal bandgap voltage Position  */
#define AC_COMPCTRL_MUXNEG_DAC                (AC_COMPCTRL_MUXNEG_DAC_Val << AC_COMPCTRL_MUXNEG_Pos) /**< (AC_COMPCTRL) DAC output Position  */
#define AC_COMPCTRL_MUXPOS_Pos                (12U)                                          /**< (AC_COMPCTRL) Positive Input Mux Selection Position */
#define AC_COMPCTRL_MUXPOS_Msk                (0x7U << AC_COMPCTRL_MUXPOS_Pos)               /**< (AC_COMPCTRL) Positive Input Mux Selection Mask */
#define AC_COMPCTRL_MUXPOS(value)             (AC_COMPCTRL_MUXPOS_Msk & ((value) << AC_COMPCTRL_MUXPOS_Pos))
#define   AC_COMPCTRL_MUXPOS_PIN0_Val         (0U)                                           /**< (AC_COMPCTRL) I/O pin 0  */
#define   AC_COMPCTRL_MUXPOS_PIN1_Val         (1U)                                           /**< (AC_COMPCTRL) I/O pin 1  */
#define   AC_COMPCTRL_MUXPOS_PIN2_Val         (2U)                                           /**< (AC_COMPCTRL) I/O pin 2  */
#define   AC_COMPCTRL_MUXPOS_PIN3_Val         (3U)                                           /**< (AC_COMPCTRL) I/O pin 3  */
#define   AC_COMPCTRL_MUXPOS_VSCALE_Val       (4U)                                           /**< (AC_COMPCTRL) VDD Scaler  */
#define AC_COMPCTRL_MUXPOS_PIN0               (AC_COMPCTRL_MUXPOS_PIN0_Val << AC_COMPCTRL_MUXPOS_Pos) /**< (AC_COMPCTRL) I/O pin 0 Position  */
#define AC_COMPCTRL_MUXPOS_PIN1               (AC_COMPCTRL_MUXPOS_PIN1_Val << AC_COMPCTRL_MUXPOS_Pos) /**< (AC_COMPCTRL) I/O pin 1 Position  */
#define AC_COMPCTRL_MUXPOS_PIN2               (AC_COMPCTRL_MUXPOS_PIN2_Val << AC_COMPCTRL_MUXPOS_Pos) /**< (AC_COMPCTRL) I/O pin 2 Position  */
#define AC_COMPCTRL_MUXPOS_PIN3               (AC_COMPCTRL_MUXPOS_PIN3_Val << AC_COMPCTRL_MUXPOS_Pos) /**< (AC_COMPCTRL) I/O pin 3 Position  */
#define AC_COMPCTRL_MUXPOS_VSCALE             (AC_COMPCTRL_MUXPOS_VSCALE_Val << AC_COMPCTRL_MUXPOS_Pos) /**< (AC_COMPCTRL) VDD Scaler Position  */
#define AC_COMPCTRL_SWAP_Pos                  (15U)                                          /**< (AC_COMPCTRL) Swap Inputs and Invert Position */
#define AC_COMPCTRL_SWAP_Msk                  (0x1U << AC_COMPCTRL_SWAP_Pos)                 /**< (AC_COMPCTRL) Swap Inputs and Invert Mask */
#define AC_COMPCTRL_SWAP(value)               (AC_COMPCTRL_SWAP_Msk & ((value) << AC_COMPCTRL_SWAP_Pos))
#define AC_COMPCTRL_SPEED_Pos                 (16U)                                          /**< (AC_COMPCTRL) Speed Selection Position */
#define AC_COMPCTRL_SPEED_Msk                 (0x3U << AC_COMPCTRL_SPEED_Pos)                /**< (AC_COMPCTRL) Speed Selection Mask */
#define AC_COMPCTRL_SPEED(value)              (AC_COMPCTRL_SPEED_Msk & ((value) << AC_COMPCTRL_SPEED_Pos))
#define   AC_COMPCTRL_SPEED_LOW_Val           (0U)                                           /**< (AC_COMPCTRL) Low speed  */
#define   AC_COMPCTRL_SPEED_HIGH_Val          (3U)                                           /**< (AC_COMPCTRL) High speed  */
#define AC_COMPCTRL_SPEED_LOW                 (AC_COMPCTRL_SPEED_LOW_Val << AC_COMPCTRL_SPEED_Pos) /**< (AC_COMPCTRL) Low speed Position  */
#define AC_COMPCTRL_SPEED_HIGH                (AC_COMPCTRL_SPEED_HIGH_Val << AC_COMPCTRL_SPEED_Pos) /**< (AC_COMPCTRL) High speed Position  */
#define AC_COMPCTRL_HYSTEN_Pos                (19U)                                          /**< (AC_COMPCTRL) Hysteresis Enable Position */
#define AC_COMPCTRL_HYSTEN_Msk                (0x1U << AC_COMPCTRL_HYSTEN_Pos)               /**< (AC_COMPCTRL) Hysteresis Enable Mask */
#define AC_COMPCTRL_HYSTEN(value)             (AC_COMPCTRL_HYSTEN_Msk & ((value) << AC_COMPCTRL_HYSTEN_Pos))
#define AC_COMPCTRL_FLEN_Pos                  (24U)                                          /**< (AC_COMPCTRL) Filter Length Position */
#define AC_COMPCTRL_FLEN_Msk                  (0x7U << AC_COMPCTRL_FLEN_Pos)                 /**< (AC_COMPCTRL) Filter Length Mask */
#define AC_COMPCTRL_FLEN(value)               (AC_COMPCTRL_FLEN_Msk & ((value) << AC_COMPCTRL_FLEN_Pos))
#define   AC_COMPCTRL_FLEN_OFF_Val            (0U)                                           /**< (AC_COMPCTRL) No filtering  */
#define   AC_COMPCTRL_FLEN_MAJ3_Val           (1U)                                           /**< (AC_COMPCTRL) 3-bit majority function (2 of 3)  */
#define   AC_COMPCTRL_FLEN_MAJ5_Val           (2U)                                           /**< (AC_COMPCTRL) 5-bit majority function (3 of 5)  */
#define AC_COMPCTRL_FLEN_OFF                  (AC_COMPCTRL_FLEN_OFF_Val << AC_COMPCTRL_FLEN_Pos) /**< (AC_COMPCTRL) No filtering Position  */
#define AC_COMPCTRL_FLEN_MAJ3                 (AC_COMPCTRL_FLEN_MAJ3_Val << AC_COMPCTRL_FLEN_Pos) /**< (AC_COMPCTRL) 3-bit majority function (2 of 3) Position  */
#define AC_COMPCTRL_FLEN_MAJ5                 (AC_COMPCTRL_FLEN_MAJ5_Val << AC_COMPCTRL_FLEN_Pos) /**< (AC_COMPCTRL) 5-bit majority function (3 of 5) Position  */
#define AC_COMPCTRL_OUT_Pos                   (28U)                                          /**< (AC_COMPCTRL) Output Position */
#define AC_COMPCTRL_OUT_Msk                   (0x3U << AC_COMPCTRL_OUT_Pos)                  /**< (AC_COMPCTRL) Output Mask */
#define AC_COMPCTRL_OUT(value)                (AC_COMPCTRL_OUT_Msk & ((value) << AC_COMPCTRL_OUT_Pos))
#define   AC_COMPCTRL_OUT_OFF_Val             (0U)                                           /**< (AC_COMPCTRL) The output of COMPn is not routed to the COMPn I/O port  */
#define   AC_COMPCTRL_OUT_ASYNC_Val           (1U)                                           /**< (AC_COMPCTRL) The asynchronous output of COMPn is routed to the COMPn I/O port  */
#define   AC_COMPCTRL_OUT_SYNC_Val            (2U)                                           /**< (AC_COMPCTRL) The synchronous output (including filtering) of COMPn is routed to the COMPn I/O port  */
#define AC_COMPCTRL_OUT_OFF                   (AC_COMPCTRL_OUT_OFF_Val << AC_COMPCTRL_OUT_Pos) /**< (AC_COMPCTRL) The output of COMPn is not routed to the COMPn I/O port Position  */
#define AC_COMPCTRL_OUT_ASYNC                 (AC_COMPCTRL_OUT_ASYNC_Val << AC_COMPCTRL_OUT_Pos) /**< (AC_COMPCTRL) The asynchronous output of COMPn is routed to the COMPn I/O port Position  */
#define AC_COMPCTRL_OUT_SYNC                  (AC_COMPCTRL_OUT_SYNC_Val << AC_COMPCTRL_OUT_Pos) /**< (AC_COMPCTRL) The synchronous output (including filtering) of COMPn is routed to the COMPn I/O port Position  */
#define AC_COMPCTRL_Msk                       (0x370BF75EUL)                                 /**< (AC_COMPCTRL) Register Mask  */

/* -------- AC_SYNCBUSY : (AC Offset: 0x20) (R/  32) Synchronization Busy -------- */
#define AC_SYNCBUSY_SWRST_Pos                 (0U)                                           /**< (AC_SYNCBUSY) Software Reset Synchronization Busy Position */
#define AC_SYNCBUSY_SWRST_Msk                 (0x1U << AC_SYNCBUSY_SWRST_Pos)                /**< (AC_SYNCBUSY) Software Reset Synchronization Busy Mask */
#define AC_SYNCBUSY_SWRST(value)              (AC_SYNCBUSY_SWRST_Msk & ((value) << AC_SYNCBUSY_SWRST_Pos))
#define AC_SYNCBUSY_ENABLE_Pos                (1U)                                           /**< (AC_SYNCBUSY) Enable Synchronization Busy Position */
#define AC_SYNCBUSY_ENABLE_Msk                (0x1U << AC_SYNCBUSY_ENABLE_Pos)               /**< (AC_SYNCBUSY) Enable Synchronization Busy Mask */
#define AC_SYNCBUSY_ENABLE(value)             (AC_SYNCBUSY_ENABLE_Msk & ((value) << AC_SYNCBUSY_ENABLE_Pos))
#define AC_SYNCBUSY_WINCTRL_Pos               (2U)                                           /**< (AC_SYNCBUSY) WINCTRL Synchronization Busy Position */
#define AC_SYNCBUSY_WINCTRL_Msk               (0x1U << AC_SYNCBUSY_WINCTRL_Pos)              /**< (AC_SYNCBUSY) WINCTRL Synchronization Busy Mask */
#define AC_SYNCBUSY_WINCTRL(value)            (AC_SYNCBUSY_WINCTRL_Msk & ((value) << AC_SYNCBUSY_WINCTRL_Pos))
#define AC_SYNCBUSY_COMPCTRL0_Pos             (3U)                                           /**< (AC_SYNCBUSY) COMPCTRL 0 Synchronization Busy Position */
#define AC_SYNCBUSY_COMPCTRL0_Msk             (0x1U << AC_SYNCBUSY_COMPCTRL0_Pos)            /**< (AC_SYNCBUSY) COMPCTRL 0 Synchronization Busy Mask */
#define AC_SYNCBUSY_COMPCTRL0(value)          (AC_SYNCBUSY_COMPCTRL0_Msk & ((value) << AC_SYNCBUSY_COMPCTRL0_Pos))
#define AC_SYNCBUSY_COMPCTRL1_Pos             (4U)                                           /**< (AC_SYNCBUSY) COMPCTRL 1 Synchronization Busy Position */
#define AC_SYNCBUSY_COMPCTRL1_Msk             (0x1U << AC_SYNCBUSY_COMPCTRL1_Pos)            /**< (AC_SYNCBUSY) COMPCTRL 1 Synchronization Busy Mask */
#define AC_SYNCBUSY_COMPCTRL1(value)          (AC_SYNCBUSY_COMPCTRL1_Msk & ((value) << AC_SYNCBUSY_COMPCTRL1_Pos))
#define AC_SYNCBUSY_COMPCTRL2_Pos             (5U)                                           /**< (AC_SYNCBUSY) COMPCTRL 2 Synchronization Busy Position */
#define AC_SYNCBUSY_COMPCTRL2_Msk             (0x1U << AC_SYNCBUSY_COMPCTRL2_Pos)            /**< (AC_SYNCBUSY) COMPCTRL 2 Synchronization Busy Mask */
#define AC_SYNCBUSY_COMPCTRL2(value)          (AC_SYNCBUSY_COMPCTRL2_Msk & ((value) << AC_SYNCBUSY_COMPCTRL2_Pos))
#define AC_SYNCBUSY_COMPCTRL3_Pos             (6U)                                           /**< (AC_SYNCBUSY) COMPCTRL 3 Synchronization Busy Position */
#define AC_SYNCBUSY_COMPCTRL3_Msk             (0x1U << AC_SYNCBUSY_COMPCTRL3_Pos)            /**< (AC_SYNCBUSY) COMPCTRL 3 Synchronization Busy Mask */
#define AC_SYNCBUSY_COMPCTRL3(value)          (AC_SYNCBUSY_COMPCTRL3_Msk & ((value) << AC_SYNCBUSY_COMPCTRL3_Pos))
#define AC_SYNCBUSY_Msk                       (0x0000007FUL)                                 /**< (AC_SYNCBUSY) Register Mask  */

/** \brief AC register offsets definitions */
#define AC_CTRLA_OFFSET                (0x00)         /**< (AC_CTRLA) Control A Offset */
#define AC_CTRLB_OFFSET                (0x01)         /**< (AC_CTRLB) Control B Offset */
#define AC_EVCTRL_OFFSET               (0x02)         /**< (AC_EVCTRL) Event Control Offset */
#define AC_INTENCLR_OFFSET             (0x04)         /**< (AC_INTENCLR) Interrupt Enable Clear Offset */
#define AC_INTENSET_OFFSET             (0x05)         /**< (AC_INTENSET) Interrupt Enable Set Offset */
#define AC_INTFLAG_OFFSET              (0x06)         /**< (AC_INTFLAG) Interrupt Flag Status and Clear Offset */
#define AC_STATUSA_OFFSET              (0x07)         /**< (AC_STATUSA) Status A Offset */
#define AC_STATUSB_OFFSET              (0x08)         /**< (AC_STATUSB) Status B Offset */
#define AC_DBGCTRL_OFFSET              (0x09)         /**< (AC_DBGCTRL) Debug Control Offset */
#define AC_WINCTRL_OFFSET              (0x0A)         /**< (AC_WINCTRL) Window Control Offset */
#define AC_SCALER_OFFSET               (0x0C)         /**< (AC_SCALER) Scaler n Offset */
#define AC_COMPCTRL_OFFSET             (0x10)         /**< (AC_COMPCTRL) Comparator Control n Offset */
#define AC_SYNCBUSY_OFFSET             (0x20)         /**< (AC_SYNCBUSY) Synchronization Busy Offset */

/** \brief AC register API structure */
typedef struct
{
  __IO  uint8_t                        AC_CTRLA;        /**< Offset: 0x00 (R/W  8) Control A */
  __O   uint8_t                        AC_CTRLB;        /**< Offset: 0x01 ( /W  8) Control B */
  __IO  uint16_t                       AC_EVCTRL;       /**< Offset: 0x02 (R/W  16) Event Control */
  __IO  uint8_t                        AC_INTENCLR;     /**< Offset: 0x04 (R/W  8) Interrupt Enable Clear */
  __IO  uint8_t                        AC_INTENSET;     /**< Offset: 0x05 (R/W  8) Interrupt Enable Set */
  __IO  uint8_t                        AC_INTFLAG;      /**< Offset: 0x06 (R/W  8) Interrupt Flag Status and Clear */
  __I   uint8_t                        AC_STATUSA;      /**< Offset: 0x07 (R/   8) Status A */
  __I   uint8_t                        AC_STATUSB;      /**< Offset: 0x08 (R/   8) Status B */
  __IO  uint8_t                        AC_DBGCTRL;      /**< Offset: 0x09 (R/W  8) Debug Control */
  __IO  uint8_t                        AC_WINCTRL;      /**< Offset: 0x0a (R/W  8) Window Control */
  __I   uint8_t                        Reserved1[0x01];
  __IO  uint8_t                        AC_SCALER[4];    /**< Offset: 0x0c (R/W  8) Scaler n */
  __IO  uint32_t                       AC_COMPCTRL[4];  /**< Offset: 0x10 (R/W  32) Comparator Control n */
  __I   uint32_t                       AC_SYNCBUSY;     /**< Offset: 0x20 (R/   32) Synchronization Busy */
} ac_registers_t;
/** @}  end of Analog Comparators */

#endif /* SAMC_SAMC21_AC_MODULE_H */

