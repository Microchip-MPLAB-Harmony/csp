/**
 * \brief Component description for PIC32CM/JH21 RTC
 *
 * Copyright (c) 2017 Microchip Technology Inc.
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

/* file generated from device description version 2017-07-25T18:00:00Z */
#ifndef _PIC32CM_JH21_RTC_COMPONENT_H_
#define _PIC32CM_JH21_RTC_COMPONENT_H_


/** \addtogroup PIC32CM_JH21_RTC Real-Time Counter
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR RTC */
/* ========================================================================== */


#define RTC_MODE2_ALARM_ALARM_RESETVALUE    (0x00U)                                       /**<  (RTC_MODE2_ALARM_ALARM) MODE2_ALARM Alarm n Value  Reset Value */

#define RTC_MODE2_ALARM_ALARM_SECOND_Pos      (0)                                            /**< (RTC_MODE2_ALARM_ALARM) Second Position */
#define RTC_MODE2_ALARM_ALARM_SECOND_Msk      (0x3FU << RTC_MODE2_ALARM_ALARM_SECOND_Pos)    /**< (RTC_MODE2_ALARM_ALARM) Second Mask */
#define RTC_MODE2_ALARM_ALARM_SECOND(value)   (RTC_MODE2_ALARM_ALARM_SECOND_Msk & ((value) << RTC_MODE2_ALARM_ALARM_SECOND_Pos))
#define RTC_MODE2_ALARM_ALARM_MINUTE_Pos      (6)                                            /**< (RTC_MODE2_ALARM_ALARM) Minute Position */
#define RTC_MODE2_ALARM_ALARM_MINUTE_Msk      (0x3FU << RTC_MODE2_ALARM_ALARM_MINUTE_Pos)    /**< (RTC_MODE2_ALARM_ALARM) Minute Mask */
#define RTC_MODE2_ALARM_ALARM_MINUTE(value)   (RTC_MODE2_ALARM_ALARM_MINUTE_Msk & ((value) << RTC_MODE2_ALARM_ALARM_MINUTE_Pos))
#define RTC_MODE2_ALARM_ALARM_HOUR_Pos        (12)                                           /**< (RTC_MODE2_ALARM_ALARM) Hour Position */
#define RTC_MODE2_ALARM_ALARM_HOUR_Msk        (0x1FU << RTC_MODE2_ALARM_ALARM_HOUR_Pos)      /**< (RTC_MODE2_ALARM_ALARM) Hour Mask */
#define RTC_MODE2_ALARM_ALARM_HOUR(value)     (RTC_MODE2_ALARM_ALARM_HOUR_Msk & ((value) << RTC_MODE2_ALARM_ALARM_HOUR_Pos))
#define   RTC_MODE2_ALARM_ALARM_HOUR_AM_Val   (0x0U)                                         /**< (RTC_MODE2_ALARM_ALARM) Morning hour  */
#define   RTC_MODE2_ALARM_ALARM_HOUR_PM_Val   (0x10U)                                        /**< (RTC_MODE2_ALARM_ALARM) Afternoon hour  */
#define RTC_MODE2_ALARM_ALARM_HOUR_AM         (RTC_MODE2_ALARM_ALARM_HOUR_AM_Val << RTC_MODE2_ALARM_ALARM_HOUR_Pos)  /**< (RTC_MODE2_ALARM_ALARM) Morning hour Position  */
#define RTC_MODE2_ALARM_ALARM_HOUR_PM         (RTC_MODE2_ALARM_ALARM_HOUR_PM_Val << RTC_MODE2_ALARM_ALARM_HOUR_Pos)  /**< (RTC_MODE2_ALARM_ALARM) Afternoon hour Position  */
#define RTC_MODE2_ALARM_ALARM_DAY_Pos         (17)                                           /**< (RTC_MODE2_ALARM_ALARM) Day Position */
#define RTC_MODE2_ALARM_ALARM_DAY_Msk         (0x1FU << RTC_MODE2_ALARM_ALARM_DAY_Pos)       /**< (RTC_MODE2_ALARM_ALARM) Day Mask */
#define RTC_MODE2_ALARM_ALARM_DAY(value)      (RTC_MODE2_ALARM_ALARM_DAY_Msk & ((value) << RTC_MODE2_ALARM_ALARM_DAY_Pos))
#define RTC_MODE2_ALARM_ALARM_MONTH_Pos       (22)                                           /**< (RTC_MODE2_ALARM_ALARM) Month Position */
#define RTC_MODE2_ALARM_ALARM_MONTH_Msk       (0xFU << RTC_MODE2_ALARM_ALARM_MONTH_Pos)      /**< (RTC_MODE2_ALARM_ALARM) Month Mask */
#define RTC_MODE2_ALARM_ALARM_MONTH(value)    (RTC_MODE2_ALARM_ALARM_MONTH_Msk & ((value) << RTC_MODE2_ALARM_ALARM_MONTH_Pos))
#define RTC_MODE2_ALARM_ALARM_YEAR_Pos        (26)                                           /**< (RTC_MODE2_ALARM_ALARM) Year Position */
#define RTC_MODE2_ALARM_ALARM_YEAR_Msk        (0x3FU << RTC_MODE2_ALARM_ALARM_YEAR_Pos)      /**< (RTC_MODE2_ALARM_ALARM) Year Mask */
#define RTC_MODE2_ALARM_ALARM_YEAR(value)     (RTC_MODE2_ALARM_ALARM_YEAR_Msk & ((value) << RTC_MODE2_ALARM_ALARM_YEAR_Pos))
#define RTC_MODE2_ALARM_ALARM_Msk             (0xFFFFFFFFUL)                                 /**< (RTC_MODE2_ALARM_ALARM) Register Mask  */


#define RTC_MODE2_ALARM_MASK_RESETVALUE     (0x00U)                                       /**<  (RTC_MODE2_ALARM_MASK) MODE2_ALARM Alarm n Mask  Reset Value */

#define RTC_MODE2_ALARM_MASK_SEL_Pos          (0)                                            /**< (RTC_MODE2_ALARM_MASK) Alarm Mask Selection Position */
#define RTC_MODE2_ALARM_MASK_SEL_Msk          (0x7U << RTC_MODE2_ALARM_MASK_SEL_Pos)         /**< (RTC_MODE2_ALARM_MASK) Alarm Mask Selection Mask */
#define RTC_MODE2_ALARM_MASK_SEL(value)       (RTC_MODE2_ALARM_MASK_SEL_Msk & ((value) << RTC_MODE2_ALARM_MASK_SEL_Pos))
#define   RTC_MODE2_ALARM_MASK_SEL_OFF_Val    (0x0U)                                         /**< (RTC_MODE2_ALARM_MASK) Alarm Disabled  */
#define   RTC_MODE2_ALARM_MASK_SEL_SS_Val     (0x1U)                                         /**< (RTC_MODE2_ALARM_MASK) Match seconds only  */
#define   RTC_MODE2_ALARM_MASK_SEL_MMSS_Val   (0x2U)                                         /**< (RTC_MODE2_ALARM_MASK) Match seconds and minutes only  */
#define   RTC_MODE2_ALARM_MASK_SEL_HHMMSS_Val (0x3U)                                         /**< (RTC_MODE2_ALARM_MASK) Match seconds, minutes, and hours only  */
#define   RTC_MODE2_ALARM_MASK_SEL_DDHHMMSS_Val (0x4U)                                         /**< (RTC_MODE2_ALARM_MASK) Match seconds, minutes, hours, and days only  */
#define   RTC_MODE2_ALARM_MASK_SEL_MMDDHHMMSS_Val (0x5U)                                         /**< (RTC_MODE2_ALARM_MASK) Match seconds, minutes, hours, days, and months only  */
#define   RTC_MODE2_ALARM_MASK_SEL_YYMMDDHHMMSS_Val (0x6U)                                         /**< (RTC_MODE2_ALARM_MASK) Match seconds, minutes, hours, days, months, and years  */
#define RTC_MODE2_ALARM_MASK_SEL_OFF          (RTC_MODE2_ALARM_MASK_SEL_OFF_Val << RTC_MODE2_ALARM_MASK_SEL_Pos)  /**< (RTC_MODE2_ALARM_MASK) Alarm Disabled Position  */
#define RTC_MODE2_ALARM_MASK_SEL_SS           (RTC_MODE2_ALARM_MASK_SEL_SS_Val << RTC_MODE2_ALARM_MASK_SEL_Pos)  /**< (RTC_MODE2_ALARM_MASK) Match seconds only Position  */
#define RTC_MODE2_ALARM_MASK_SEL_MMSS         (RTC_MODE2_ALARM_MASK_SEL_MMSS_Val << RTC_MODE2_ALARM_MASK_SEL_Pos)  /**< (RTC_MODE2_ALARM_MASK) Match seconds and minutes only Position  */
#define RTC_MODE2_ALARM_MASK_SEL_HHMMSS       (RTC_MODE2_ALARM_MASK_SEL_HHMMSS_Val << RTC_MODE2_ALARM_MASK_SEL_Pos)  /**< (RTC_MODE2_ALARM_MASK) Match seconds, minutes, and hours only Position  */
#define RTC_MODE2_ALARM_MASK_SEL_DDHHMMSS     (RTC_MODE2_ALARM_MASK_SEL_DDHHMMSS_Val << RTC_MODE2_ALARM_MASK_SEL_Pos)  /**< (RTC_MODE2_ALARM_MASK) Match seconds, minutes, hours, and days only Position  */
#define RTC_MODE2_ALARM_MASK_SEL_MMDDHHMMSS   (RTC_MODE2_ALARM_MASK_SEL_MMDDHHMMSS_Val << RTC_MODE2_ALARM_MASK_SEL_Pos)  /**< (RTC_MODE2_ALARM_MASK) Match seconds, minutes, hours, days, and months only Position  */
#define RTC_MODE2_ALARM_MASK_SEL_YYMMDDHHMMSS (RTC_MODE2_ALARM_MASK_SEL_YYMMDDHHMMSS_Val << RTC_MODE2_ALARM_MASK_SEL_Pos)  /**< (RTC_MODE2_ALARM_MASK) Match seconds, minutes, hours, days, months, and years Position  */
#define RTC_MODE2_ALARM_MASK_Msk              (0x00000007UL)                                 /**< (RTC_MODE2_ALARM_MASK) Register Mask  */


#define RTC_MODE0_CTRLA_RESETVALUE          (0x00U)                                       /**<  (RTC_MODE0_CTRLA) MODE0 Control A  Reset Value */

#define RTC_MODE0_CTRLA_SWRST_Pos             (0)                                            /**< (RTC_MODE0_CTRLA) Software Reset Position */
#define RTC_MODE0_CTRLA_SWRST_Msk             (0x1U << RTC_MODE0_CTRLA_SWRST_Pos)            /**< (RTC_MODE0_CTRLA) Software Reset Mask */
#define RTC_MODE0_CTRLA_ENABLE_Pos            (1)                                            /**< (RTC_MODE0_CTRLA) Enable Position */
#define RTC_MODE0_CTRLA_ENABLE_Msk            (0x1U << RTC_MODE0_CTRLA_ENABLE_Pos)           /**< (RTC_MODE0_CTRLA) Enable Mask */
#define RTC_MODE0_CTRLA_MODE_Pos              (2)                                            /**< (RTC_MODE0_CTRLA) Operating Mode Position */
#define RTC_MODE0_CTRLA_MODE_Msk              (0x3U << RTC_MODE0_CTRLA_MODE_Pos)             /**< (RTC_MODE0_CTRLA) Operating Mode Mask */
#define RTC_MODE0_CTRLA_MODE(value)           (RTC_MODE0_CTRLA_MODE_Msk & ((value) << RTC_MODE0_CTRLA_MODE_Pos))
#define   RTC_MODE0_CTRLA_MODE_COUNT32_Val    (0x0U)                                         /**< (RTC_MODE0_CTRLA) Mode 0: 32-bit Counter  */
#define   RTC_MODE0_CTRLA_MODE_COUNT16_Val    (0x1U)                                         /**< (RTC_MODE0_CTRLA) Mode 1: 16-bit Counter  */
#define   RTC_MODE0_CTRLA_MODE_CLOCK_Val      (0x2U)                                         /**< (RTC_MODE0_CTRLA) Mode 2: Clock/Calendar  */
#define RTC_MODE0_CTRLA_MODE_COUNT32          (RTC_MODE0_CTRLA_MODE_COUNT32_Val << RTC_MODE0_CTRLA_MODE_Pos)  /**< (RTC_MODE0_CTRLA) Mode 0: 32-bit Counter Position  */
#define RTC_MODE0_CTRLA_MODE_COUNT16          (RTC_MODE0_CTRLA_MODE_COUNT16_Val << RTC_MODE0_CTRLA_MODE_Pos)  /**< (RTC_MODE0_CTRLA) Mode 1: 16-bit Counter Position  */
#define RTC_MODE0_CTRLA_MODE_CLOCK            (RTC_MODE0_CTRLA_MODE_CLOCK_Val << RTC_MODE0_CTRLA_MODE_Pos)  /**< (RTC_MODE0_CTRLA) Mode 2: Clock/Calendar Position  */
#define RTC_MODE0_CTRLA_MATCHCLR_Pos          (7)                                            /**< (RTC_MODE0_CTRLA) Clear on Match Position */
#define RTC_MODE0_CTRLA_MATCHCLR_Msk          (0x1U << RTC_MODE0_CTRLA_MATCHCLR_Pos)         /**< (RTC_MODE0_CTRLA) Clear on Match Mask */
#define RTC_MODE0_CTRLA_PRESCALER_Pos         (8)                                            /**< (RTC_MODE0_CTRLA) Prescaler Position */
#define RTC_MODE0_CTRLA_PRESCALER_Msk         (0xFU << RTC_MODE0_CTRLA_PRESCALER_Pos)        /**< (RTC_MODE0_CTRLA) Prescaler Mask */
#define RTC_MODE0_CTRLA_PRESCALER(value)      (RTC_MODE0_CTRLA_PRESCALER_Msk & ((value) << RTC_MODE0_CTRLA_PRESCALER_Pos))
#define   RTC_MODE0_CTRLA_PRESCALER_OFF_Val   (0x0U)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/1  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV1_Val  (0x1U)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/1  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV2_Val  (0x2U)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/2  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV4_Val  (0x3U)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/4  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV8_Val  (0x4U)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/8  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV16_Val (0x5U)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/16  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV32_Val (0x6U)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/32  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV64_Val (0x7U)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/64  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV128_Val (0x8U)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/128  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV256_Val (0x9U)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/256  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV512_Val (0xAU)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/512  */
#define   RTC_MODE0_CTRLA_PRESCALER_DIV1024_Val (0xBU)                                         /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/1024  */
#define RTC_MODE0_CTRLA_PRESCALER_OFF         (RTC_MODE0_CTRLA_PRESCALER_OFF_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/1 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV1        (RTC_MODE0_CTRLA_PRESCALER_DIV1_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/1 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV2        (RTC_MODE0_CTRLA_PRESCALER_DIV2_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/2 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV4        (RTC_MODE0_CTRLA_PRESCALER_DIV4_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/4 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV8        (RTC_MODE0_CTRLA_PRESCALER_DIV8_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/8 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV16       (RTC_MODE0_CTRLA_PRESCALER_DIV16_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/16 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV32       (RTC_MODE0_CTRLA_PRESCALER_DIV32_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/32 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV64       (RTC_MODE0_CTRLA_PRESCALER_DIV64_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/64 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV128      (RTC_MODE0_CTRLA_PRESCALER_DIV128_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/128 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV256      (RTC_MODE0_CTRLA_PRESCALER_DIV256_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/256 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV512      (RTC_MODE0_CTRLA_PRESCALER_DIV512_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/512 Position  */
#define RTC_MODE0_CTRLA_PRESCALER_DIV1024     (RTC_MODE0_CTRLA_PRESCALER_DIV1024_Val << RTC_MODE0_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE0_CTRLA) CLK_RTC_CNT = GCLK_RTC/1024 Position  */
#define RTC_MODE0_CTRLA_COUNTSYNC_Pos         (15)                                           /**< (RTC_MODE0_CTRLA) Count Read Synchronization Enable Position */
#define RTC_MODE0_CTRLA_COUNTSYNC_Msk         (0x1U << RTC_MODE0_CTRLA_COUNTSYNC_Pos)        /**< (RTC_MODE0_CTRLA) Count Read Synchronization Enable Mask */
#define RTC_MODE0_CTRLA_Msk                   (0x00008F8FUL)                                 /**< (RTC_MODE0_CTRLA) Register Mask  */


#define RTC_MODE0_EVCTRL_RESETVALUE         (0x00U)                                       /**<  (RTC_MODE0_EVCTRL) MODE0 Event Control  Reset Value */

#define RTC_MODE0_EVCTRL_PEREO0_Pos           (0)                                            /**< (RTC_MODE0_EVCTRL) Periodic Interval 0 Event Output Enable Position */
#define RTC_MODE0_EVCTRL_PEREO0_Msk           (0x1U << RTC_MODE0_EVCTRL_PEREO0_Pos)          /**< (RTC_MODE0_EVCTRL) Periodic Interval 0 Event Output Enable Mask */
#define RTC_MODE0_EVCTRL_PEREO1_Pos           (1)                                            /**< (RTC_MODE0_EVCTRL) Periodic Interval 1 Event Output Enable Position */
#define RTC_MODE0_EVCTRL_PEREO1_Msk           (0x1U << RTC_MODE0_EVCTRL_PEREO1_Pos)          /**< (RTC_MODE0_EVCTRL) Periodic Interval 1 Event Output Enable Mask */
#define RTC_MODE0_EVCTRL_PEREO2_Pos           (2)                                            /**< (RTC_MODE0_EVCTRL) Periodic Interval 2 Event Output Enable Position */
#define RTC_MODE0_EVCTRL_PEREO2_Msk           (0x1U << RTC_MODE0_EVCTRL_PEREO2_Pos)          /**< (RTC_MODE0_EVCTRL) Periodic Interval 2 Event Output Enable Mask */
#define RTC_MODE0_EVCTRL_PEREO3_Pos           (3)                                            /**< (RTC_MODE0_EVCTRL) Periodic Interval 3 Event Output Enable Position */
#define RTC_MODE0_EVCTRL_PEREO3_Msk           (0x1U << RTC_MODE0_EVCTRL_PEREO3_Pos)          /**< (RTC_MODE0_EVCTRL) Periodic Interval 3 Event Output Enable Mask */
#define RTC_MODE0_EVCTRL_PEREO4_Pos           (4)                                            /**< (RTC_MODE0_EVCTRL) Periodic Interval 4 Event Output Enable Position */
#define RTC_MODE0_EVCTRL_PEREO4_Msk           (0x1U << RTC_MODE0_EVCTRL_PEREO4_Pos)          /**< (RTC_MODE0_EVCTRL) Periodic Interval 4 Event Output Enable Mask */
#define RTC_MODE0_EVCTRL_PEREO5_Pos           (5)                                            /**< (RTC_MODE0_EVCTRL) Periodic Interval 5 Event Output Enable Position */
#define RTC_MODE0_EVCTRL_PEREO5_Msk           (0x1U << RTC_MODE0_EVCTRL_PEREO5_Pos)          /**< (RTC_MODE0_EVCTRL) Periodic Interval 5 Event Output Enable Mask */
#define RTC_MODE0_EVCTRL_PEREO6_Pos           (6)                                            /**< (RTC_MODE0_EVCTRL) Periodic Interval 6 Event Output Enable Position */
#define RTC_MODE0_EVCTRL_PEREO6_Msk           (0x1U << RTC_MODE0_EVCTRL_PEREO6_Pos)          /**< (RTC_MODE0_EVCTRL) Periodic Interval 6 Event Output Enable Mask */
#define RTC_MODE0_EVCTRL_PEREO7_Pos           (7)                                            /**< (RTC_MODE0_EVCTRL) Periodic Interval 7 Event Output Enable Position */
#define RTC_MODE0_EVCTRL_PEREO7_Msk           (0x1U << RTC_MODE0_EVCTRL_PEREO7_Pos)          /**< (RTC_MODE0_EVCTRL) Periodic Interval 7 Event Output Enable Mask */
#define RTC_MODE0_EVCTRL_CMPEO0_Pos           (8)                                            /**< (RTC_MODE0_EVCTRL) Compare 0 Event Output Enable Position */
#define RTC_MODE0_EVCTRL_CMPEO0_Msk           (0x1U << RTC_MODE0_EVCTRL_CMPEO0_Pos)          /**< (RTC_MODE0_EVCTRL) Compare 0 Event Output Enable Mask */
#define RTC_MODE0_EVCTRL_OVFEO_Pos            (15)                                           /**< (RTC_MODE0_EVCTRL) Overflow Event Output Enable Position */
#define RTC_MODE0_EVCTRL_OVFEO_Msk            (0x1U << RTC_MODE0_EVCTRL_OVFEO_Pos)           /**< (RTC_MODE0_EVCTRL) Overflow Event Output Enable Mask */
#define RTC_MODE0_EVCTRL_Msk                  (0x000081FFUL)                                 /**< (RTC_MODE0_EVCTRL) Register Mask  */
#define RTC_MODE0_EVCTRL_PEREO_Pos            (0)                                            /**< (RTC_MODE0_EVCTRL Position) Periodic Interval x Event Output Enable */
#define RTC_MODE0_EVCTRL_PEREO_Msk            (0xFFU << RTC_MODE0_EVCTRL_PEREO_Pos)          /**< (RTC_MODE0_EVCTRL Mask) PEREO */
#define RTC_MODE0_EVCTRL_PEREO(value)         (RTC_MODE0_EVCTRL_PEREO_Msk & ((value) << RTC_MODE0_EVCTRL_PEREO_Pos))


#define RTC_MODE0_INTENCLR_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE0_INTENCLR) MODE0 Interrupt Enable Clear  Reset Value */

#define RTC_MODE0_INTENCLR_PER0_Pos           (0)                                            /**< (RTC_MODE0_INTENCLR) Periodic Interval 0 Interrupt Enable Position */
#define RTC_MODE0_INTENCLR_PER0_Msk           (0x1U << RTC_MODE0_INTENCLR_PER0_Pos)          /**< (RTC_MODE0_INTENCLR) Periodic Interval 0 Interrupt Enable Mask */
#define RTC_MODE0_INTENCLR_PER1_Pos           (1)                                            /**< (RTC_MODE0_INTENCLR) Periodic Interval 1 Interrupt Enable Position */
#define RTC_MODE0_INTENCLR_PER1_Msk           (0x1U << RTC_MODE0_INTENCLR_PER1_Pos)          /**< (RTC_MODE0_INTENCLR) Periodic Interval 1 Interrupt Enable Mask */
#define RTC_MODE0_INTENCLR_PER2_Pos           (2)                                            /**< (RTC_MODE0_INTENCLR) Periodic Interval 2 Interrupt Enable Position */
#define RTC_MODE0_INTENCLR_PER2_Msk           (0x1U << RTC_MODE0_INTENCLR_PER2_Pos)          /**< (RTC_MODE0_INTENCLR) Periodic Interval 2 Interrupt Enable Mask */
#define RTC_MODE0_INTENCLR_PER3_Pos           (3)                                            /**< (RTC_MODE0_INTENCLR) Periodic Interval 3 Interrupt Enable Position */
#define RTC_MODE0_INTENCLR_PER3_Msk           (0x1U << RTC_MODE0_INTENCLR_PER3_Pos)          /**< (RTC_MODE0_INTENCLR) Periodic Interval 3 Interrupt Enable Mask */
#define RTC_MODE0_INTENCLR_PER4_Pos           (4)                                            /**< (RTC_MODE0_INTENCLR) Periodic Interval 4 Interrupt Enable Position */
#define RTC_MODE0_INTENCLR_PER4_Msk           (0x1U << RTC_MODE0_INTENCLR_PER4_Pos)          /**< (RTC_MODE0_INTENCLR) Periodic Interval 4 Interrupt Enable Mask */
#define RTC_MODE0_INTENCLR_PER5_Pos           (5)                                            /**< (RTC_MODE0_INTENCLR) Periodic Interval 5 Interrupt Enable Position */
#define RTC_MODE0_INTENCLR_PER5_Msk           (0x1U << RTC_MODE0_INTENCLR_PER5_Pos)          /**< (RTC_MODE0_INTENCLR) Periodic Interval 5 Interrupt Enable Mask */
#define RTC_MODE0_INTENCLR_PER6_Pos           (6)                                            /**< (RTC_MODE0_INTENCLR) Periodic Interval 6 Interrupt Enable Position */
#define RTC_MODE0_INTENCLR_PER6_Msk           (0x1U << RTC_MODE0_INTENCLR_PER6_Pos)          /**< (RTC_MODE0_INTENCLR) Periodic Interval 6 Interrupt Enable Mask */
#define RTC_MODE0_INTENCLR_PER7_Pos           (7)                                            /**< (RTC_MODE0_INTENCLR) Periodic Interval 7 Interrupt Enable Position */
#define RTC_MODE0_INTENCLR_PER7_Msk           (0x1U << RTC_MODE0_INTENCLR_PER7_Pos)          /**< (RTC_MODE0_INTENCLR) Periodic Interval 7 Interrupt Enable Mask */
#define RTC_MODE0_INTENCLR_CMP0_Pos           (8)                                            /**< (RTC_MODE0_INTENCLR) Compare 0 Interrupt Enable Position */
#define RTC_MODE0_INTENCLR_CMP0_Msk           (0x1U << RTC_MODE0_INTENCLR_CMP0_Pos)          /**< (RTC_MODE0_INTENCLR) Compare 0 Interrupt Enable Mask */
#define RTC_MODE0_INTENCLR_OVF_Pos            (15)                                           /**< (RTC_MODE0_INTENCLR) Overflow Interrupt Enable Position */
#define RTC_MODE0_INTENCLR_OVF_Msk            (0x1U << RTC_MODE0_INTENCLR_OVF_Pos)           /**< (RTC_MODE0_INTENCLR) Overflow Interrupt Enable Mask */
#define RTC_MODE0_INTENCLR_Msk                (0x000081FFUL)                                 /**< (RTC_MODE0_INTENCLR) Register Mask  */
#define RTC_MODE0_INTENCLR_PER_Pos            (0)                                            /**< (RTC_MODE0_INTENCLR Position) Periodic Interval x Interrupt Enable */
#define RTC_MODE0_INTENCLR_PER_Msk            (0xFFU << RTC_MODE0_INTENCLR_PER_Pos)          /**< (RTC_MODE0_INTENCLR Mask) PER */
#define RTC_MODE0_INTENCLR_PER(value)         (RTC_MODE0_INTENCLR_PER_Msk & ((value) << RTC_MODE0_INTENCLR_PER_Pos))


#define RTC_MODE0_INTENSET_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE0_INTENSET) MODE0 Interrupt Enable Set  Reset Value */

#define RTC_MODE0_INTENSET_PER0_Pos           (0)                                            /**< (RTC_MODE0_INTENSET) Periodic Interval 0 Interrupt Enable Position */
#define RTC_MODE0_INTENSET_PER0_Msk           (0x1U << RTC_MODE0_INTENSET_PER0_Pos)          /**< (RTC_MODE0_INTENSET) Periodic Interval 0 Interrupt Enable Mask */
#define RTC_MODE0_INTENSET_PER1_Pos           (1)                                            /**< (RTC_MODE0_INTENSET) Periodic Interval 1 Interrupt Enable Position */
#define RTC_MODE0_INTENSET_PER1_Msk           (0x1U << RTC_MODE0_INTENSET_PER1_Pos)          /**< (RTC_MODE0_INTENSET) Periodic Interval 1 Interrupt Enable Mask */
#define RTC_MODE0_INTENSET_PER2_Pos           (2)                                            /**< (RTC_MODE0_INTENSET) Periodic Interval 2 Interrupt Enable Position */
#define RTC_MODE0_INTENSET_PER2_Msk           (0x1U << RTC_MODE0_INTENSET_PER2_Pos)          /**< (RTC_MODE0_INTENSET) Periodic Interval 2 Interrupt Enable Mask */
#define RTC_MODE0_INTENSET_PER3_Pos           (3)                                            /**< (RTC_MODE0_INTENSET) Periodic Interval 3 Interrupt Enable Position */
#define RTC_MODE0_INTENSET_PER3_Msk           (0x1U << RTC_MODE0_INTENSET_PER3_Pos)          /**< (RTC_MODE0_INTENSET) Periodic Interval 3 Interrupt Enable Mask */
#define RTC_MODE0_INTENSET_PER4_Pos           (4)                                            /**< (RTC_MODE0_INTENSET) Periodic Interval 4 Interrupt Enable Position */
#define RTC_MODE0_INTENSET_PER4_Msk           (0x1U << RTC_MODE0_INTENSET_PER4_Pos)          /**< (RTC_MODE0_INTENSET) Periodic Interval 4 Interrupt Enable Mask */
#define RTC_MODE0_INTENSET_PER5_Pos           (5)                                            /**< (RTC_MODE0_INTENSET) Periodic Interval 5 Interrupt Enable Position */
#define RTC_MODE0_INTENSET_PER5_Msk           (0x1U << RTC_MODE0_INTENSET_PER5_Pos)          /**< (RTC_MODE0_INTENSET) Periodic Interval 5 Interrupt Enable Mask */
#define RTC_MODE0_INTENSET_PER6_Pos           (6)                                            /**< (RTC_MODE0_INTENSET) Periodic Interval 6 Interrupt Enable Position */
#define RTC_MODE0_INTENSET_PER6_Msk           (0x1U << RTC_MODE0_INTENSET_PER6_Pos)          /**< (RTC_MODE0_INTENSET) Periodic Interval 6 Interrupt Enable Mask */
#define RTC_MODE0_INTENSET_PER7_Pos           (7)                                            /**< (RTC_MODE0_INTENSET) Periodic Interval 7 Interrupt Enable Position */
#define RTC_MODE0_INTENSET_PER7_Msk           (0x1U << RTC_MODE0_INTENSET_PER7_Pos)          /**< (RTC_MODE0_INTENSET) Periodic Interval 7 Interrupt Enable Mask */
#define RTC_MODE0_INTENSET_CMP0_Pos           (8)                                            /**< (RTC_MODE0_INTENSET) Compare 0 Interrupt Enable Position */
#define RTC_MODE0_INTENSET_CMP0_Msk           (0x1U << RTC_MODE0_INTENSET_CMP0_Pos)          /**< (RTC_MODE0_INTENSET) Compare 0 Interrupt Enable Mask */
#define RTC_MODE0_INTENSET_OVF_Pos            (15)                                           /**< (RTC_MODE0_INTENSET) Overflow Interrupt Enable Position */
#define RTC_MODE0_INTENSET_OVF_Msk            (0x1U << RTC_MODE0_INTENSET_OVF_Pos)           /**< (RTC_MODE0_INTENSET) Overflow Interrupt Enable Mask */
#define RTC_MODE0_INTENSET_Msk                (0x000081FFUL)                                 /**< (RTC_MODE0_INTENSET) Register Mask  */
#define RTC_MODE0_INTENSET_PER_Pos            (0)                                            /**< (RTC_MODE0_INTENSET Position) Periodic Interval x Interrupt Enable */
#define RTC_MODE0_INTENSET_PER_Msk            (0xFFU << RTC_MODE0_INTENSET_PER_Pos)          /**< (RTC_MODE0_INTENSET Mask) PER */
#define RTC_MODE0_INTENSET_PER(value)         (RTC_MODE0_INTENSET_PER_Msk & ((value) << RTC_MODE0_INTENSET_PER_Pos))


#define RTC_MODE0_INTFLAG_RESETVALUE        (0x00U)                                       /**<  (RTC_MODE0_INTFLAG) MODE0 Interrupt Flag Status and Clear  Reset Value */

#define RTC_MODE0_INTFLAG_PER0_Pos            (0)                                            /**< (RTC_MODE0_INTFLAG) Periodic Interval 0 Position */
#define RTC_MODE0_INTFLAG_PER0_Msk            (0x1U << RTC_MODE0_INTFLAG_PER0_Pos)           /**< (RTC_MODE0_INTFLAG) Periodic Interval 0 Mask */
#define RTC_MODE0_INTFLAG_PER1_Pos            (1)                                            /**< (RTC_MODE0_INTFLAG) Periodic Interval 1 Position */
#define RTC_MODE0_INTFLAG_PER1_Msk            (0x1U << RTC_MODE0_INTFLAG_PER1_Pos)           /**< (RTC_MODE0_INTFLAG) Periodic Interval 1 Mask */
#define RTC_MODE0_INTFLAG_PER2_Pos            (2)                                            /**< (RTC_MODE0_INTFLAG) Periodic Interval 2 Position */
#define RTC_MODE0_INTFLAG_PER2_Msk            (0x1U << RTC_MODE0_INTFLAG_PER2_Pos)           /**< (RTC_MODE0_INTFLAG) Periodic Interval 2 Mask */
#define RTC_MODE0_INTFLAG_PER3_Pos            (3)                                            /**< (RTC_MODE0_INTFLAG) Periodic Interval 3 Position */
#define RTC_MODE0_INTFLAG_PER3_Msk            (0x1U << RTC_MODE0_INTFLAG_PER3_Pos)           /**< (RTC_MODE0_INTFLAG) Periodic Interval 3 Mask */
#define RTC_MODE0_INTFLAG_PER4_Pos            (4)                                            /**< (RTC_MODE0_INTFLAG) Periodic Interval 4 Position */
#define RTC_MODE0_INTFLAG_PER4_Msk            (0x1U << RTC_MODE0_INTFLAG_PER4_Pos)           /**< (RTC_MODE0_INTFLAG) Periodic Interval 4 Mask */
#define RTC_MODE0_INTFLAG_PER5_Pos            (5)                                            /**< (RTC_MODE0_INTFLAG) Periodic Interval 5 Position */
#define RTC_MODE0_INTFLAG_PER5_Msk            (0x1U << RTC_MODE0_INTFLAG_PER5_Pos)           /**< (RTC_MODE0_INTFLAG) Periodic Interval 5 Mask */
#define RTC_MODE0_INTFLAG_PER6_Pos            (6)                                            /**< (RTC_MODE0_INTFLAG) Periodic Interval 6 Position */
#define RTC_MODE0_INTFLAG_PER6_Msk            (0x1U << RTC_MODE0_INTFLAG_PER6_Pos)           /**< (RTC_MODE0_INTFLAG) Periodic Interval 6 Mask */
#define RTC_MODE0_INTFLAG_PER7_Pos            (7)                                            /**< (RTC_MODE0_INTFLAG) Periodic Interval 7 Position */
#define RTC_MODE0_INTFLAG_PER7_Msk            (0x1U << RTC_MODE0_INTFLAG_PER7_Pos)           /**< (RTC_MODE0_INTFLAG) Periodic Interval 7 Mask */
#define RTC_MODE0_INTFLAG_CMP0_Pos            (8)                                            /**< (RTC_MODE0_INTFLAG) Compare 0 Position */
#define RTC_MODE0_INTFLAG_CMP0_Msk            (0x1U << RTC_MODE0_INTFLAG_CMP0_Pos)           /**< (RTC_MODE0_INTFLAG) Compare 0 Mask */
#define RTC_MODE0_INTFLAG_OVF_Pos             (15)                                           /**< (RTC_MODE0_INTFLAG) Overflow Position */
#define RTC_MODE0_INTFLAG_OVF_Msk             (0x1U << RTC_MODE0_INTFLAG_OVF_Pos)            /**< (RTC_MODE0_INTFLAG) Overflow Mask */
#define RTC_MODE0_INTFLAG_Msk                 (0x000081FFUL)                                 /**< (RTC_MODE0_INTFLAG) Register Mask  */
#define RTC_MODE0_INTFLAG_PER_Pos             (0)                                            /**< (RTC_MODE0_INTFLAG Position) Periodic Interval x */
#define RTC_MODE0_INTFLAG_PER_Msk             (0xFFU << RTC_MODE0_INTFLAG_PER_Pos)           /**< (RTC_MODE0_INTFLAG Mask) PER */
#define RTC_MODE0_INTFLAG_PER(value)          (RTC_MODE0_INTFLAG_PER_Msk & ((value) << RTC_MODE0_INTFLAG_PER_Pos))


#define RTC_MODE0_DBGCTRL_RESETVALUE        (0x00U)                                       /**<  (RTC_MODE0_DBGCTRL) Debug Control  Reset Value */

#define RTC_MODE0_DBGCTRL_DBGRUN_Pos          (0)                                            /**< (RTC_MODE0_DBGCTRL) Run During Debug Position */
#define RTC_MODE0_DBGCTRL_DBGRUN_Msk          (0x1U << RTC_MODE0_DBGCTRL_DBGRUN_Pos)         /**< (RTC_MODE0_DBGCTRL) Run During Debug Mask */
#define RTC_MODE0_DBGCTRL_Msk                 (0x00000001UL)                                 /**< (RTC_MODE0_DBGCTRL) Register Mask  */

#define RTC_MODE0_SYNCBUSY_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE0_SYNCBUSY) MODE0 Synchronization Busy Status  Reset Value */

#define RTC_MODE0_SYNCBUSY_SWRST_Pos          (0)                                            /**< (RTC_MODE0_SYNCBUSY) Software Reset Busy Position */
#define RTC_MODE0_SYNCBUSY_SWRST_Msk          (0x1U << RTC_MODE0_SYNCBUSY_SWRST_Pos)         /**< (RTC_MODE0_SYNCBUSY) Software Reset Busy Mask */
#define RTC_MODE0_SYNCBUSY_ENABLE_Pos         (1)                                            /**< (RTC_MODE0_SYNCBUSY) Enable Bit Busy Position */
#define RTC_MODE0_SYNCBUSY_ENABLE_Msk         (0x1U << RTC_MODE0_SYNCBUSY_ENABLE_Pos)        /**< (RTC_MODE0_SYNCBUSY) Enable Bit Busy Mask */
#define RTC_MODE0_SYNCBUSY_FREQCORR_Pos       (2)                                            /**< (RTC_MODE0_SYNCBUSY) FREQCORR Register Busy Position */
#define RTC_MODE0_SYNCBUSY_FREQCORR_Msk       (0x1U << RTC_MODE0_SYNCBUSY_FREQCORR_Pos)      /**< (RTC_MODE0_SYNCBUSY) FREQCORR Register Busy Mask */
#define RTC_MODE0_SYNCBUSY_COUNT_Pos          (3)                                            /**< (RTC_MODE0_SYNCBUSY) COUNT Register Busy Position */
#define RTC_MODE0_SYNCBUSY_COUNT_Msk          (0x1U << RTC_MODE0_SYNCBUSY_COUNT_Pos)         /**< (RTC_MODE0_SYNCBUSY) COUNT Register Busy Mask */
#define RTC_MODE0_SYNCBUSY_COMP0_Pos          (5)                                            /**< (RTC_MODE0_SYNCBUSY) COMP 0 Register Busy Position */
#define RTC_MODE0_SYNCBUSY_COMP0_Msk          (0x1U << RTC_MODE0_SYNCBUSY_COMP0_Pos)         /**< (RTC_MODE0_SYNCBUSY) COMP 0 Register Busy Mask */
#define RTC_MODE0_SYNCBUSY_COUNTSYNC_Pos      (15)                                           /**< (RTC_MODE0_SYNCBUSY) Count Read Synchronization Enable Bit Busy Position */
#define RTC_MODE0_SYNCBUSY_COUNTSYNC_Msk      (0x1U << RTC_MODE0_SYNCBUSY_COUNTSYNC_Pos)     /**< (RTC_MODE0_SYNCBUSY) Count Read Synchronization Enable Bit Busy Mask */
#define RTC_MODE0_SYNCBUSY_Msk                (0x0000802FUL)                                 /**< (RTC_MODE0_SYNCBUSY) Register Mask  */


#define RTC_MODE0_FREQCORR_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE0_FREQCORR) Frequency Correction  Reset Value */

#define RTC_MODE0_FREQCORR_VALUE_Pos          (0)                                            /**< (RTC_MODE0_FREQCORR) Correction Value Position */
#define RTC_MODE0_FREQCORR_VALUE_Msk          (0x7FU << RTC_MODE0_FREQCORR_VALUE_Pos)        /**< (RTC_MODE0_FREQCORR) Correction Value Mask */
#define RTC_MODE0_FREQCORR_VALUE(value)       (RTC_MODE0_FREQCORR_VALUE_Msk & ((value) << RTC_MODE0_FREQCORR_VALUE_Pos))
#define RTC_MODE0_FREQCORR_SIGN_Pos           (7)                                            /**< (RTC_MODE0_FREQCORR) Correction Sign Position */
#define RTC_MODE0_FREQCORR_SIGN_Msk           (0x1U << RTC_MODE0_FREQCORR_SIGN_Pos)          /**< (RTC_MODE0_FREQCORR) Correction Sign Mask */
#define RTC_MODE0_FREQCORR_Msk                (0x000000FFUL)                                 /**< (RTC_MODE0_FREQCORR) Register Mask  */


#define RTC_MODE0_COUNT_RESETVALUE          (0x00U)                                       /**<  (RTC_MODE0_COUNT) MODE0 Counter Value  Reset Value */

#define RTC_MODE0_COUNT_COUNT_Pos             (0)                                            /**< (RTC_MODE0_COUNT) Counter Value Position */
#define RTC_MODE0_COUNT_COUNT_Msk             (0xFFFFFFFFU << RTC_MODE0_COUNT_COUNT_Pos)     /**< (RTC_MODE0_COUNT) Counter Value Mask */
#define RTC_MODE0_COUNT_COUNT(value)          (RTC_MODE0_COUNT_COUNT_Msk & ((value) << RTC_MODE0_COUNT_COUNT_Pos))
#define RTC_MODE0_COUNT_Msk                   (0xFFFFFFFFUL)                                 /**< (RTC_MODE0_COUNT) Register Mask  */


#define RTC_MODE0_COMP_RESETVALUE           (0x00U)                                       /**<  (RTC_MODE0_COMP) MODE0 Compare n Value  Reset Value */

#define RTC_MODE0_COMP_COMP_Pos               (0)                                            /**< (RTC_MODE0_COMP) Compare Value Position */
#define RTC_MODE0_COMP_COMP_Msk               (0xFFFFFFFFU << RTC_MODE0_COMP_COMP_Pos)       /**< (RTC_MODE0_COMP) Compare Value Mask */
#define RTC_MODE0_COMP_COMP(value)            (RTC_MODE0_COMP_COMP_Msk & ((value) << RTC_MODE0_COMP_COMP_Pos))
#define RTC_MODE0_COMP_Msk                    (0xFFFFFFFFUL)                                 /**< (RTC_MODE0_COMP) Register Mask  */


#define RTC_MODE1_CTRLA_RESETVALUE          (0x00U)                                       /**<  (RTC_MODE1_CTRLA) MODE1 Control A  Reset Value */

#define RTC_MODE1_CTRLA_SWRST_Pos             (0)                                            /**< (RTC_MODE1_CTRLA) Software Reset Position */
#define RTC_MODE1_CTRLA_SWRST_Msk             (0x1U << RTC_MODE1_CTRLA_SWRST_Pos)            /**< (RTC_MODE1_CTRLA) Software Reset Mask */
#define RTC_MODE1_CTRLA_ENABLE_Pos            (1)                                            /**< (RTC_MODE1_CTRLA) Enable Position */
#define RTC_MODE1_CTRLA_ENABLE_Msk            (0x1U << RTC_MODE1_CTRLA_ENABLE_Pos)           /**< (RTC_MODE1_CTRLA) Enable Mask */
#define RTC_MODE1_CTRLA_MODE_Pos              (2)                                            /**< (RTC_MODE1_CTRLA) Operating Mode Position */
#define RTC_MODE1_CTRLA_MODE_Msk              (0x3U << RTC_MODE1_CTRLA_MODE_Pos)             /**< (RTC_MODE1_CTRLA) Operating Mode Mask */
#define RTC_MODE1_CTRLA_MODE(value)           (RTC_MODE1_CTRLA_MODE_Msk & ((value) << RTC_MODE1_CTRLA_MODE_Pos))
#define   RTC_MODE1_CTRLA_MODE_COUNT32_Val    (0x0U)                                         /**< (RTC_MODE1_CTRLA) Mode 0: 32-bit Counter  */
#define   RTC_MODE1_CTRLA_MODE_COUNT16_Val    (0x1U)                                         /**< (RTC_MODE1_CTRLA) Mode 1: 16-bit Counter  */
#define   RTC_MODE1_CTRLA_MODE_CLOCK_Val      (0x2U)                                         /**< (RTC_MODE1_CTRLA) Mode 2: Clock/Calendar  */
#define RTC_MODE1_CTRLA_MODE_COUNT32          (RTC_MODE1_CTRLA_MODE_COUNT32_Val << RTC_MODE1_CTRLA_MODE_Pos)  /**< (RTC_MODE1_CTRLA) Mode 0: 32-bit Counter Position  */
#define RTC_MODE1_CTRLA_MODE_COUNT16          (RTC_MODE1_CTRLA_MODE_COUNT16_Val << RTC_MODE1_CTRLA_MODE_Pos)  /**< (RTC_MODE1_CTRLA) Mode 1: 16-bit Counter Position  */
#define RTC_MODE1_CTRLA_MODE_CLOCK            (RTC_MODE1_CTRLA_MODE_CLOCK_Val << RTC_MODE1_CTRLA_MODE_Pos)  /**< (RTC_MODE1_CTRLA) Mode 2: Clock/Calendar Position  */
#define RTC_MODE1_CTRLA_PRESCALER_Pos         (8)                                            /**< (RTC_MODE1_CTRLA) Prescaler Position */
#define RTC_MODE1_CTRLA_PRESCALER_Msk         (0xFU << RTC_MODE1_CTRLA_PRESCALER_Pos)        /**< (RTC_MODE1_CTRLA) Prescaler Mask */
#define RTC_MODE1_CTRLA_PRESCALER(value)      (RTC_MODE1_CTRLA_PRESCALER_Msk & ((value) << RTC_MODE1_CTRLA_PRESCALER_Pos))
#define   RTC_MODE1_CTRLA_PRESCALER_OFF_Val   (0x0U)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/1  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV1_Val  (0x1U)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/1  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV2_Val  (0x2U)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/2  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV4_Val  (0x3U)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/4  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV8_Val  (0x4U)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/8  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV16_Val (0x5U)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/16  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV32_Val (0x6U)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/32  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV64_Val (0x7U)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/64  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV128_Val (0x8U)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/128  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV256_Val (0x9U)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/256  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV512_Val (0xAU)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/512  */
#define   RTC_MODE1_CTRLA_PRESCALER_DIV1024_Val (0xBU)                                         /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/1024  */
#define RTC_MODE1_CTRLA_PRESCALER_OFF         (RTC_MODE1_CTRLA_PRESCALER_OFF_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/1 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV1        (RTC_MODE1_CTRLA_PRESCALER_DIV1_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/1 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV2        (RTC_MODE1_CTRLA_PRESCALER_DIV2_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/2 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV4        (RTC_MODE1_CTRLA_PRESCALER_DIV4_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/4 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV8        (RTC_MODE1_CTRLA_PRESCALER_DIV8_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/8 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV16       (RTC_MODE1_CTRLA_PRESCALER_DIV16_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/16 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV32       (RTC_MODE1_CTRLA_PRESCALER_DIV32_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/32 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV64       (RTC_MODE1_CTRLA_PRESCALER_DIV64_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/64 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV128      (RTC_MODE1_CTRLA_PRESCALER_DIV128_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/128 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV256      (RTC_MODE1_CTRLA_PRESCALER_DIV256_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/256 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV512      (RTC_MODE1_CTRLA_PRESCALER_DIV512_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/512 Position  */
#define RTC_MODE1_CTRLA_PRESCALER_DIV1024     (RTC_MODE1_CTRLA_PRESCALER_DIV1024_Val << RTC_MODE1_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE1_CTRLA) CLK_RTC_CNT = GCLK_RTC/1024 Position  */
#define RTC_MODE1_CTRLA_COUNTSYNC_Pos         (15)                                           /**< (RTC_MODE1_CTRLA) Count Read Synchronization Enable Position */
#define RTC_MODE1_CTRLA_COUNTSYNC_Msk         (0x1U << RTC_MODE1_CTRLA_COUNTSYNC_Pos)        /**< (RTC_MODE1_CTRLA) Count Read Synchronization Enable Mask */
#define RTC_MODE1_CTRLA_Msk                   (0x00008F0FUL)                                 /**< (RTC_MODE1_CTRLA) Register Mask  */


#define RTC_MODE1_EVCTRL_RESETVALUE         (0x00U)                                       /**<  (RTC_MODE1_EVCTRL) MODE1 Event Control  Reset Value */

#define RTC_MODE1_EVCTRL_PEREO0_Pos           (0)                                            /**< (RTC_MODE1_EVCTRL) Periodic Interval 0 Event Output Enable Position */
#define RTC_MODE1_EVCTRL_PEREO0_Msk           (0x1U << RTC_MODE1_EVCTRL_PEREO0_Pos)          /**< (RTC_MODE1_EVCTRL) Periodic Interval 0 Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_PEREO1_Pos           (1)                                            /**< (RTC_MODE1_EVCTRL) Periodic Interval 1 Event Output Enable Position */
#define RTC_MODE1_EVCTRL_PEREO1_Msk           (0x1U << RTC_MODE1_EVCTRL_PEREO1_Pos)          /**< (RTC_MODE1_EVCTRL) Periodic Interval 1 Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_PEREO2_Pos           (2)                                            /**< (RTC_MODE1_EVCTRL) Periodic Interval 2 Event Output Enable Position */
#define RTC_MODE1_EVCTRL_PEREO2_Msk           (0x1U << RTC_MODE1_EVCTRL_PEREO2_Pos)          /**< (RTC_MODE1_EVCTRL) Periodic Interval 2 Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_PEREO3_Pos           (3)                                            /**< (RTC_MODE1_EVCTRL) Periodic Interval 3 Event Output Enable Position */
#define RTC_MODE1_EVCTRL_PEREO3_Msk           (0x1U << RTC_MODE1_EVCTRL_PEREO3_Pos)          /**< (RTC_MODE1_EVCTRL) Periodic Interval 3 Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_PEREO4_Pos           (4)                                            /**< (RTC_MODE1_EVCTRL) Periodic Interval 4 Event Output Enable Position */
#define RTC_MODE1_EVCTRL_PEREO4_Msk           (0x1U << RTC_MODE1_EVCTRL_PEREO4_Pos)          /**< (RTC_MODE1_EVCTRL) Periodic Interval 4 Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_PEREO5_Pos           (5)                                            /**< (RTC_MODE1_EVCTRL) Periodic Interval 5 Event Output Enable Position */
#define RTC_MODE1_EVCTRL_PEREO5_Msk           (0x1U << RTC_MODE1_EVCTRL_PEREO5_Pos)          /**< (RTC_MODE1_EVCTRL) Periodic Interval 5 Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_PEREO6_Pos           (6)                                            /**< (RTC_MODE1_EVCTRL) Periodic Interval 6 Event Output Enable Position */
#define RTC_MODE1_EVCTRL_PEREO6_Msk           (0x1U << RTC_MODE1_EVCTRL_PEREO6_Pos)          /**< (RTC_MODE1_EVCTRL) Periodic Interval 6 Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_PEREO7_Pos           (7)                                            /**< (RTC_MODE1_EVCTRL) Periodic Interval 7 Event Output Enable Position */
#define RTC_MODE1_EVCTRL_PEREO7_Msk           (0x1U << RTC_MODE1_EVCTRL_PEREO7_Pos)          /**< (RTC_MODE1_EVCTRL) Periodic Interval 7 Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_CMPEO0_Pos           (8)                                            /**< (RTC_MODE1_EVCTRL) Compare 0 Event Output Enable Position */
#define RTC_MODE1_EVCTRL_CMPEO0_Msk           (0x1U << RTC_MODE1_EVCTRL_CMPEO0_Pos)          /**< (RTC_MODE1_EVCTRL) Compare 0 Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_CMPEO1_Pos           (9)                                            /**< (RTC_MODE1_EVCTRL) Compare 1 Event Output Enable Position */
#define RTC_MODE1_EVCTRL_CMPEO1_Msk           (0x1U << RTC_MODE1_EVCTRL_CMPEO1_Pos)          /**< (RTC_MODE1_EVCTRL) Compare 1 Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_OVFEO_Pos            (15)                                           /**< (RTC_MODE1_EVCTRL) Overflow Event Output Enable Position */
#define RTC_MODE1_EVCTRL_OVFEO_Msk            (0x1U << RTC_MODE1_EVCTRL_OVFEO_Pos)           /**< (RTC_MODE1_EVCTRL) Overflow Event Output Enable Mask */
#define RTC_MODE1_EVCTRL_Msk                  (0x000083FFUL)                                 /**< (RTC_MODE1_EVCTRL) Register Mask  */
#define RTC_MODE1_EVCTRL_PEREO_Pos            (0)                                            /**< (RTC_MODE1_EVCTRL Position) Periodic Interval x Event Output Enable */
#define RTC_MODE1_EVCTRL_PEREO_Msk            (0xFFU << RTC_MODE1_EVCTRL_PEREO_Pos)          /**< (RTC_MODE1_EVCTRL Mask) PEREO */
#define RTC_MODE1_EVCTRL_PEREO(value)         (RTC_MODE1_EVCTRL_PEREO_Msk & ((value) << RTC_MODE1_EVCTRL_PEREO_Pos))
#define RTC_MODE1_EVCTRL_CMPEO_Pos            (8)                                            /**< (RTC_MODE1_EVCTRL Position) Compare x Event Output Enable */
#define RTC_MODE1_EVCTRL_CMPEO_Msk            (0x3U << RTC_MODE1_EVCTRL_CMPEO_Pos)           /**< (RTC_MODE1_EVCTRL Mask) CMPEO */
#define RTC_MODE1_EVCTRL_CMPEO(value)         (RTC_MODE1_EVCTRL_CMPEO_Msk & ((value) << RTC_MODE1_EVCTRL_CMPEO_Pos))


#define RTC_MODE1_INTENCLR_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE1_INTENCLR) MODE1 Interrupt Enable Clear  Reset Value */

#define RTC_MODE1_INTENCLR_PER0_Pos           (0)                                            /**< (RTC_MODE1_INTENCLR) Periodic Interval 0 Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_PER0_Msk           (0x1U << RTC_MODE1_INTENCLR_PER0_Pos)          /**< (RTC_MODE1_INTENCLR) Periodic Interval 0 Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_PER1_Pos           (1)                                            /**< (RTC_MODE1_INTENCLR) Periodic Interval 1 Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_PER1_Msk           (0x1U << RTC_MODE1_INTENCLR_PER1_Pos)          /**< (RTC_MODE1_INTENCLR) Periodic Interval 1 Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_PER2_Pos           (2)                                            /**< (RTC_MODE1_INTENCLR) Periodic Interval 2 Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_PER2_Msk           (0x1U << RTC_MODE1_INTENCLR_PER2_Pos)          /**< (RTC_MODE1_INTENCLR) Periodic Interval 2 Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_PER3_Pos           (3)                                            /**< (RTC_MODE1_INTENCLR) Periodic Interval 3 Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_PER3_Msk           (0x1U << RTC_MODE1_INTENCLR_PER3_Pos)          /**< (RTC_MODE1_INTENCLR) Periodic Interval 3 Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_PER4_Pos           (4)                                            /**< (RTC_MODE1_INTENCLR) Periodic Interval 4 Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_PER4_Msk           (0x1U << RTC_MODE1_INTENCLR_PER4_Pos)          /**< (RTC_MODE1_INTENCLR) Periodic Interval 4 Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_PER5_Pos           (5)                                            /**< (RTC_MODE1_INTENCLR) Periodic Interval 5 Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_PER5_Msk           (0x1U << RTC_MODE1_INTENCLR_PER5_Pos)          /**< (RTC_MODE1_INTENCLR) Periodic Interval 5 Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_PER6_Pos           (6)                                            /**< (RTC_MODE1_INTENCLR) Periodic Interval 6 Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_PER6_Msk           (0x1U << RTC_MODE1_INTENCLR_PER6_Pos)          /**< (RTC_MODE1_INTENCLR) Periodic Interval 6 Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_PER7_Pos           (7)                                            /**< (RTC_MODE1_INTENCLR) Periodic Interval 7 Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_PER7_Msk           (0x1U << RTC_MODE1_INTENCLR_PER7_Pos)          /**< (RTC_MODE1_INTENCLR) Periodic Interval 7 Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_CMP0_Pos           (8)                                            /**< (RTC_MODE1_INTENCLR) Compare 0 Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_CMP0_Msk           (0x1U << RTC_MODE1_INTENCLR_CMP0_Pos)          /**< (RTC_MODE1_INTENCLR) Compare 0 Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_CMP1_Pos           (9)                                            /**< (RTC_MODE1_INTENCLR) Compare 1 Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_CMP1_Msk           (0x1U << RTC_MODE1_INTENCLR_CMP1_Pos)          /**< (RTC_MODE1_INTENCLR) Compare 1 Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_OVF_Pos            (15)                                           /**< (RTC_MODE1_INTENCLR) Overflow Interrupt Enable Position */
#define RTC_MODE1_INTENCLR_OVF_Msk            (0x1U << RTC_MODE1_INTENCLR_OVF_Pos)           /**< (RTC_MODE1_INTENCLR) Overflow Interrupt Enable Mask */
#define RTC_MODE1_INTENCLR_Msk                (0x000083FFUL)                                 /**< (RTC_MODE1_INTENCLR) Register Mask  */
#define RTC_MODE1_INTENCLR_PER_Pos            (0)                                            /**< (RTC_MODE1_INTENCLR Position) Periodic Interval x Interrupt Enable */
#define RTC_MODE1_INTENCLR_PER_Msk            (0xFFU << RTC_MODE1_INTENCLR_PER_Pos)          /**< (RTC_MODE1_INTENCLR Mask) PER */
#define RTC_MODE1_INTENCLR_PER(value)         (RTC_MODE1_INTENCLR_PER_Msk & ((value) << RTC_MODE1_INTENCLR_PER_Pos))
#define RTC_MODE1_INTENCLR_CMP_Pos            (8)                                            /**< (RTC_MODE1_INTENCLR Position) Compare x Interrupt Enable */
#define RTC_MODE1_INTENCLR_CMP_Msk            (0x3U << RTC_MODE1_INTENCLR_CMP_Pos)           /**< (RTC_MODE1_INTENCLR Mask) CMP */
#define RTC_MODE1_INTENCLR_CMP(value)         (RTC_MODE1_INTENCLR_CMP_Msk & ((value) << RTC_MODE1_INTENCLR_CMP_Pos))


#define RTC_MODE1_INTENSET_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE1_INTENSET) MODE1 Interrupt Enable Set  Reset Value */

#define RTC_MODE1_INTENSET_PER0_Pos           (0)                                            /**< (RTC_MODE1_INTENSET) Periodic Interval 0 Interrupt Enable Position */
#define RTC_MODE1_INTENSET_PER0_Msk           (0x1U << RTC_MODE1_INTENSET_PER0_Pos)          /**< (RTC_MODE1_INTENSET) Periodic Interval 0 Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_PER1_Pos           (1)                                            /**< (RTC_MODE1_INTENSET) Periodic Interval 1 Interrupt Enable Position */
#define RTC_MODE1_INTENSET_PER1_Msk           (0x1U << RTC_MODE1_INTENSET_PER1_Pos)          /**< (RTC_MODE1_INTENSET) Periodic Interval 1 Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_PER2_Pos           (2)                                            /**< (RTC_MODE1_INTENSET) Periodic Interval 2 Interrupt Enable Position */
#define RTC_MODE1_INTENSET_PER2_Msk           (0x1U << RTC_MODE1_INTENSET_PER2_Pos)          /**< (RTC_MODE1_INTENSET) Periodic Interval 2 Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_PER3_Pos           (3)                                            /**< (RTC_MODE1_INTENSET) Periodic Interval 3 Interrupt Enable Position */
#define RTC_MODE1_INTENSET_PER3_Msk           (0x1U << RTC_MODE1_INTENSET_PER3_Pos)          /**< (RTC_MODE1_INTENSET) Periodic Interval 3 Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_PER4_Pos           (4)                                            /**< (RTC_MODE1_INTENSET) Periodic Interval 4 Interrupt Enable Position */
#define RTC_MODE1_INTENSET_PER4_Msk           (0x1U << RTC_MODE1_INTENSET_PER4_Pos)          /**< (RTC_MODE1_INTENSET) Periodic Interval 4 Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_PER5_Pos           (5)                                            /**< (RTC_MODE1_INTENSET) Periodic Interval 5 Interrupt Enable Position */
#define RTC_MODE1_INTENSET_PER5_Msk           (0x1U << RTC_MODE1_INTENSET_PER5_Pos)          /**< (RTC_MODE1_INTENSET) Periodic Interval 5 Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_PER6_Pos           (6)                                            /**< (RTC_MODE1_INTENSET) Periodic Interval 6 Interrupt Enable Position */
#define RTC_MODE1_INTENSET_PER6_Msk           (0x1U << RTC_MODE1_INTENSET_PER6_Pos)          /**< (RTC_MODE1_INTENSET) Periodic Interval 6 Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_PER7_Pos           (7)                                            /**< (RTC_MODE1_INTENSET) Periodic Interval 7 Interrupt Enable Position */
#define RTC_MODE1_INTENSET_PER7_Msk           (0x1U << RTC_MODE1_INTENSET_PER7_Pos)          /**< (RTC_MODE1_INTENSET) Periodic Interval 7 Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_CMP0_Pos           (8)                                            /**< (RTC_MODE1_INTENSET) Compare 0 Interrupt Enable Position */
#define RTC_MODE1_INTENSET_CMP0_Msk           (0x1U << RTC_MODE1_INTENSET_CMP0_Pos)          /**< (RTC_MODE1_INTENSET) Compare 0 Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_CMP1_Pos           (9)                                            /**< (RTC_MODE1_INTENSET) Compare 1 Interrupt Enable Position */
#define RTC_MODE1_INTENSET_CMP1_Msk           (0x1U << RTC_MODE1_INTENSET_CMP1_Pos)          /**< (RTC_MODE1_INTENSET) Compare 1 Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_OVF_Pos            (15)                                           /**< (RTC_MODE1_INTENSET) Overflow Interrupt Enable Position */
#define RTC_MODE1_INTENSET_OVF_Msk            (0x1U << RTC_MODE1_INTENSET_OVF_Pos)           /**< (RTC_MODE1_INTENSET) Overflow Interrupt Enable Mask */
#define RTC_MODE1_INTENSET_Msk                (0x000083FFUL)                                 /**< (RTC_MODE1_INTENSET) Register Mask  */
#define RTC_MODE1_INTENSET_PER_Pos            (0)                                            /**< (RTC_MODE1_INTENSET Position) Periodic Interval x Interrupt Enable */
#define RTC_MODE1_INTENSET_PER_Msk            (0xFFU << RTC_MODE1_INTENSET_PER_Pos)          /**< (RTC_MODE1_INTENSET Mask) PER */
#define RTC_MODE1_INTENSET_PER(value)         (RTC_MODE1_INTENSET_PER_Msk & ((value) << RTC_MODE1_INTENSET_PER_Pos))
#define RTC_MODE1_INTENSET_CMP_Pos            (8)                                            /**< (RTC_MODE1_INTENSET Position) Compare x Interrupt Enable */
#define RTC_MODE1_INTENSET_CMP_Msk            (0x3U << RTC_MODE1_INTENSET_CMP_Pos)           /**< (RTC_MODE1_INTENSET Mask) CMP */
#define RTC_MODE1_INTENSET_CMP(value)         (RTC_MODE1_INTENSET_CMP_Msk & ((value) << RTC_MODE1_INTENSET_CMP_Pos))


#define RTC_MODE1_INTFLAG_RESETVALUE        (0x00U)                                       /**<  (RTC_MODE1_INTFLAG) MODE1 Interrupt Flag Status and Clear  Reset Value */

#define RTC_MODE1_INTFLAG_PER0_Pos            (0)                                            /**< (RTC_MODE1_INTFLAG) Periodic Interval 0 Position */
#define RTC_MODE1_INTFLAG_PER0_Msk            (0x1U << RTC_MODE1_INTFLAG_PER0_Pos)           /**< (RTC_MODE1_INTFLAG) Periodic Interval 0 Mask */
#define RTC_MODE1_INTFLAG_PER1_Pos            (1)                                            /**< (RTC_MODE1_INTFLAG) Periodic Interval 1 Position */
#define RTC_MODE1_INTFLAG_PER1_Msk            (0x1U << RTC_MODE1_INTFLAG_PER1_Pos)           /**< (RTC_MODE1_INTFLAG) Periodic Interval 1 Mask */
#define RTC_MODE1_INTFLAG_PER2_Pos            (2)                                            /**< (RTC_MODE1_INTFLAG) Periodic Interval 2 Position */
#define RTC_MODE1_INTFLAG_PER2_Msk            (0x1U << RTC_MODE1_INTFLAG_PER2_Pos)           /**< (RTC_MODE1_INTFLAG) Periodic Interval 2 Mask */
#define RTC_MODE1_INTFLAG_PER3_Pos            (3)                                            /**< (RTC_MODE1_INTFLAG) Periodic Interval 3 Position */
#define RTC_MODE1_INTFLAG_PER3_Msk            (0x1U << RTC_MODE1_INTFLAG_PER3_Pos)           /**< (RTC_MODE1_INTFLAG) Periodic Interval 3 Mask */
#define RTC_MODE1_INTFLAG_PER4_Pos            (4)                                            /**< (RTC_MODE1_INTFLAG) Periodic Interval 4 Position */
#define RTC_MODE1_INTFLAG_PER4_Msk            (0x1U << RTC_MODE1_INTFLAG_PER4_Pos)           /**< (RTC_MODE1_INTFLAG) Periodic Interval 4 Mask */
#define RTC_MODE1_INTFLAG_PER5_Pos            (5)                                            /**< (RTC_MODE1_INTFLAG) Periodic Interval 5 Position */
#define RTC_MODE1_INTFLAG_PER5_Msk            (0x1U << RTC_MODE1_INTFLAG_PER5_Pos)           /**< (RTC_MODE1_INTFLAG) Periodic Interval 5 Mask */
#define RTC_MODE1_INTFLAG_PER6_Pos            (6)                                            /**< (RTC_MODE1_INTFLAG) Periodic Interval 6 Position */
#define RTC_MODE1_INTFLAG_PER6_Msk            (0x1U << RTC_MODE1_INTFLAG_PER6_Pos)           /**< (RTC_MODE1_INTFLAG) Periodic Interval 6 Mask */
#define RTC_MODE1_INTFLAG_PER7_Pos            (7)                                            /**< (RTC_MODE1_INTFLAG) Periodic Interval 7 Position */
#define RTC_MODE1_INTFLAG_PER7_Msk            (0x1U << RTC_MODE1_INTFLAG_PER7_Pos)           /**< (RTC_MODE1_INTFLAG) Periodic Interval 7 Mask */
#define RTC_MODE1_INTFLAG_CMP0_Pos            (8)                                            /**< (RTC_MODE1_INTFLAG) Compare 0 Position */
#define RTC_MODE1_INTFLAG_CMP0_Msk            (0x1U << RTC_MODE1_INTFLAG_CMP0_Pos)           /**< (RTC_MODE1_INTFLAG) Compare 0 Mask */
#define RTC_MODE1_INTFLAG_CMP1_Pos            (9)                                            /**< (RTC_MODE1_INTFLAG) Compare 1 Position */
#define RTC_MODE1_INTFLAG_CMP1_Msk            (0x1U << RTC_MODE1_INTFLAG_CMP1_Pos)           /**< (RTC_MODE1_INTFLAG) Compare 1 Mask */
#define RTC_MODE1_INTFLAG_OVF_Pos             (15)                                           /**< (RTC_MODE1_INTFLAG) Overflow Position */
#define RTC_MODE1_INTFLAG_OVF_Msk             (0x1U << RTC_MODE1_INTFLAG_OVF_Pos)            /**< (RTC_MODE1_INTFLAG) Overflow Mask */
#define RTC_MODE1_INTFLAG_Msk                 (0x000083FFUL)                                 /**< (RTC_MODE1_INTFLAG) Register Mask  */
#define RTC_MODE1_INTFLAG_PER_Pos             (0)                                            /**< (RTC_MODE1_INTFLAG Position) Periodic Interval x */
#define RTC_MODE1_INTFLAG_PER_Msk             (0xFFU << RTC_MODE1_INTFLAG_PER_Pos)           /**< (RTC_MODE1_INTFLAG Mask) PER */
#define RTC_MODE1_INTFLAG_PER(value)          (RTC_MODE1_INTFLAG_PER_Msk & ((value) << RTC_MODE1_INTFLAG_PER_Pos))
#define RTC_MODE1_INTFLAG_CMP_Pos             (8)                                            /**< (RTC_MODE1_INTFLAG Position) Compare x */
#define RTC_MODE1_INTFLAG_CMP_Msk             (0x3U << RTC_MODE1_INTFLAG_CMP_Pos)            /**< (RTC_MODE1_INTFLAG Mask) CMP */
#define RTC_MODE1_INTFLAG_CMP(value)          (RTC_MODE1_INTFLAG_CMP_Msk & ((value) << RTC_MODE1_INTFLAG_CMP_Pos))


#define RTC_MODE1_DBGCTRL_RESETVALUE        (0x00U)                                       /**<  (RTC_MODE1_DBGCTRL) Debug Control  Reset Value */

#define RTC_MODE1_DBGCTRL_DBGRUN_Pos          (0)                                            /**< (RTC_MODE1_DBGCTRL) Run During Debug Position */
#define RTC_MODE1_DBGCTRL_DBGRUN_Msk          (0x1U << RTC_MODE1_DBGCTRL_DBGRUN_Pos)         /**< (RTC_MODE1_DBGCTRL) Run During Debug Mask */
#define RTC_MODE1_DBGCTRL_Msk                 (0x00000001UL)                                 /**< (RTC_MODE1_DBGCTRL) Register Mask  */


#define RTC_MODE1_SYNCBUSY_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE1_SYNCBUSY) MODE1 Synchronization Busy Status  Reset Value */

#define RTC_MODE1_SYNCBUSY_SWRST_Pos          (0)                                            /**< (RTC_MODE1_SYNCBUSY) Software Reset Bit Busy Position */
#define RTC_MODE1_SYNCBUSY_SWRST_Msk          (0x1U << RTC_MODE1_SYNCBUSY_SWRST_Pos)         /**< (RTC_MODE1_SYNCBUSY) Software Reset Bit Busy Mask */
#define RTC_MODE1_SYNCBUSY_ENABLE_Pos         (1)                                            /**< (RTC_MODE1_SYNCBUSY) Enable Bit Busy Position */
#define RTC_MODE1_SYNCBUSY_ENABLE_Msk         (0x1U << RTC_MODE1_SYNCBUSY_ENABLE_Pos)        /**< (RTC_MODE1_SYNCBUSY) Enable Bit Busy Mask */
#define RTC_MODE1_SYNCBUSY_FREQCORR_Pos       (2)                                            /**< (RTC_MODE1_SYNCBUSY) FREQCORR Register Busy Position */
#define RTC_MODE1_SYNCBUSY_FREQCORR_Msk       (0x1U << RTC_MODE1_SYNCBUSY_FREQCORR_Pos)      /**< (RTC_MODE1_SYNCBUSY) FREQCORR Register Busy Mask */
#define RTC_MODE1_SYNCBUSY_COUNT_Pos          (3)                                            /**< (RTC_MODE1_SYNCBUSY) COUNT Register Busy Position */
#define RTC_MODE1_SYNCBUSY_COUNT_Msk          (0x1U << RTC_MODE1_SYNCBUSY_COUNT_Pos)         /**< (RTC_MODE1_SYNCBUSY) COUNT Register Busy Mask */
#define RTC_MODE1_SYNCBUSY_PER_Pos            (4)                                            /**< (RTC_MODE1_SYNCBUSY) PER Register Busy Position */
#define RTC_MODE1_SYNCBUSY_PER_Msk            (0x1U << RTC_MODE1_SYNCBUSY_PER_Pos)           /**< (RTC_MODE1_SYNCBUSY) PER Register Busy Mask */
#define RTC_MODE1_SYNCBUSY_COMP0_Pos          (5)                                            /**< (RTC_MODE1_SYNCBUSY) COMP 0 Register Busy Position */
#define RTC_MODE1_SYNCBUSY_COMP0_Msk          (0x1U << RTC_MODE1_SYNCBUSY_COMP0_Pos)         /**< (RTC_MODE1_SYNCBUSY) COMP 0 Register Busy Mask */
#define RTC_MODE1_SYNCBUSY_COMP1_Pos          (6)                                            /**< (RTC_MODE1_SYNCBUSY) COMP 1 Register Busy Position */
#define RTC_MODE1_SYNCBUSY_COMP1_Msk          (0x1U << RTC_MODE1_SYNCBUSY_COMP1_Pos)         /**< (RTC_MODE1_SYNCBUSY) COMP 1 Register Busy Mask */
#define RTC_MODE1_SYNCBUSY_COUNTSYNC_Pos      (15)                                           /**< (RTC_MODE1_SYNCBUSY) Count Read Synchronization Enable Bit Busy Position */
#define RTC_MODE1_SYNCBUSY_COUNTSYNC_Msk      (0x1U << RTC_MODE1_SYNCBUSY_COUNTSYNC_Pos)     /**< (RTC_MODE1_SYNCBUSY) Count Read Synchronization Enable Bit Busy Mask */
#define RTC_MODE1_SYNCBUSY_Msk                (0x0000807FUL)                                 /**< (RTC_MODE1_SYNCBUSY) Register Mask  */
#define RTC_MODE1_SYNCBUSY_COMP_Pos           (5)                                            /**< (RTC_MODE1_SYNCBUSY Position) COMP x Register Busy */
#define RTC_MODE1_SYNCBUSY_COMP_Msk           (0x3U << RTC_MODE1_SYNCBUSY_COMP_Pos)          /**< (RTC_MODE1_SYNCBUSY Mask) COMP */
#define RTC_MODE1_SYNCBUSY_COMP(value)        (RTC_MODE1_SYNCBUSY_COMP_Msk & ((value) << RTC_MODE1_SYNCBUSY_COMP_Pos))


#define RTC_MODE1_FREQCORR_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE1_FREQCORR) Frequency Correction  Reset Value */

#define RTC_MODE1_FREQCORR_VALUE_Pos          (0)                                            /**< (RTC_MODE1_FREQCORR) Correction Value Position */
#define RTC_MODE1_FREQCORR_VALUE_Msk          (0x7FU << RTC_MODE1_FREQCORR_VALUE_Pos)        /**< (RTC_MODE1_FREQCORR) Correction Value Mask */
#define RTC_MODE1_FREQCORR_VALUE(value)       (RTC_MODE1_FREQCORR_VALUE_Msk & ((value) << RTC_MODE1_FREQCORR_VALUE_Pos))
#define RTC_MODE1_FREQCORR_SIGN_Pos           (7)                                            /**< (RTC_MODE1_FREQCORR) Correction Sign Position */
#define RTC_MODE1_FREQCORR_SIGN_Msk           (0x1U << RTC_MODE1_FREQCORR_SIGN_Pos)          /**< (RTC_MODE1_FREQCORR) Correction Sign Mask */
#define RTC_MODE1_FREQCORR_Msk                (0x000000FFUL)                                 /**< (RTC_MODE1_FREQCORR) Register Mask  */


#define RTC_MODE1_COUNT_RESETVALUE          (0x00U)                                       /**<  (RTC_MODE1_COUNT) MODE1 Counter Value  Reset Value */

#define RTC_MODE1_COUNT_COUNT_Pos             (0)                                            /**< (RTC_MODE1_COUNT) Counter Value Position */
#define RTC_MODE1_COUNT_COUNT_Msk             (0xFFFFU << RTC_MODE1_COUNT_COUNT_Pos)         /**< (RTC_MODE1_COUNT) Counter Value Mask */
#define RTC_MODE1_COUNT_COUNT(value)          (RTC_MODE1_COUNT_COUNT_Msk & ((value) << RTC_MODE1_COUNT_COUNT_Pos))
#define RTC_MODE1_COUNT_Msk                   (0x0000FFFFUL)                                 /**< (RTC_MODE1_COUNT) Register Mask  */


#define RTC_MODE1_PER_RESETVALUE            (0x00U)                                       /**<  (RTC_MODE1_PER) MODE1 Counter Period  Reset Value */

#define RTC_MODE1_PER_PER_Pos                 (0)                                            /**< (RTC_MODE1_PER) Counter Period Position */
#define RTC_MODE1_PER_PER_Msk                 (0xFFFFU << RTC_MODE1_PER_PER_Pos)             /**< (RTC_MODE1_PER) Counter Period Mask */
#define RTC_MODE1_PER_PER(value)              (RTC_MODE1_PER_PER_Msk & ((value) << RTC_MODE1_PER_PER_Pos))
#define RTC_MODE1_PER_Msk                     (0x0000FFFFUL)                                 /**< (RTC_MODE1_PER) Register Mask  */


#define RTC_MODE1_COMP_RESETVALUE           (0x00U)                                       /**<  (RTC_MODE1_COMP) MODE1 Compare n Value  Reset Value */

#define RTC_MODE1_COMP_COMP_Pos               (0)                                            /**< (RTC_MODE1_COMP) Compare Value Position */
#define RTC_MODE1_COMP_COMP_Msk               (0xFFFFU << RTC_MODE1_COMP_COMP_Pos)           /**< (RTC_MODE1_COMP) Compare Value Mask */
#define RTC_MODE1_COMP_COMP(value)            (RTC_MODE1_COMP_COMP_Msk & ((value) << RTC_MODE1_COMP_COMP_Pos))
#define RTC_MODE1_COMP_Msk                    (0x0000FFFFUL)                                 /**< (RTC_MODE1_COMP) Register Mask  */

#define RTC_MODE2_CTRLA_RESETVALUE          (0x00U)                                       /**<  (RTC_MODE2_CTRLA) MODE2 Control A  Reset Value */

#define RTC_MODE2_CTRLA_SWRST_Pos             (0)                                            /**< (RTC_MODE2_CTRLA) Software Reset Position */
#define RTC_MODE2_CTRLA_SWRST_Msk             (0x1U << RTC_MODE2_CTRLA_SWRST_Pos)            /**< (RTC_MODE2_CTRLA) Software Reset Mask */
#define RTC_MODE2_CTRLA_ENABLE_Pos            (1)                                            /**< (RTC_MODE2_CTRLA) Enable Position */
#define RTC_MODE2_CTRLA_ENABLE_Msk            (0x1U << RTC_MODE2_CTRLA_ENABLE_Pos)           /**< (RTC_MODE2_CTRLA) Enable Mask */
#define RTC_MODE2_CTRLA_MODE_Pos              (2)                                            /**< (RTC_MODE2_CTRLA) Operating Mode Position */
#define RTC_MODE2_CTRLA_MODE_Msk              (0x3U << RTC_MODE2_CTRLA_MODE_Pos)             /**< (RTC_MODE2_CTRLA) Operating Mode Mask */
#define RTC_MODE2_CTRLA_MODE(value)           (RTC_MODE2_CTRLA_MODE_Msk & ((value) << RTC_MODE2_CTRLA_MODE_Pos))
#define   RTC_MODE2_CTRLA_MODE_COUNT32_Val    (0x0U)                                         /**< (RTC_MODE2_CTRLA) Mode 0: 32-bit Counter  */
#define   RTC_MODE2_CTRLA_MODE_COUNT16_Val    (0x1U)                                         /**< (RTC_MODE2_CTRLA) Mode 1: 16-bit Counter  */
#define   RTC_MODE2_CTRLA_MODE_CLOCK_Val      (0x2U)                                         /**< (RTC_MODE2_CTRLA) Mode 2: Clock/Calendar  */
#define RTC_MODE2_CTRLA_MODE_COUNT32          (RTC_MODE2_CTRLA_MODE_COUNT32_Val << RTC_MODE2_CTRLA_MODE_Pos)  /**< (RTC_MODE2_CTRLA) Mode 0: 32-bit Counter Position  */
#define RTC_MODE2_CTRLA_MODE_COUNT16          (RTC_MODE2_CTRLA_MODE_COUNT16_Val << RTC_MODE2_CTRLA_MODE_Pos)  /**< (RTC_MODE2_CTRLA) Mode 1: 16-bit Counter Position  */
#define RTC_MODE2_CTRLA_MODE_CLOCK            (RTC_MODE2_CTRLA_MODE_CLOCK_Val << RTC_MODE2_CTRLA_MODE_Pos)  /**< (RTC_MODE2_CTRLA) Mode 2: Clock/Calendar Position  */
#define RTC_MODE2_CTRLA_CLKREP_Pos            (6)                                            /**< (RTC_MODE2_CTRLA) Clock Representation Position */
#define RTC_MODE2_CTRLA_CLKREP_Msk            (0x1U << RTC_MODE2_CTRLA_CLKREP_Pos)           /**< (RTC_MODE2_CTRLA) Clock Representation Mask */
#define RTC_MODE2_CTRLA_MATCHCLR_Pos          (7)                                            /**< (RTC_MODE2_CTRLA) Clear on Match Position */
#define RTC_MODE2_CTRLA_MATCHCLR_Msk          (0x1U << RTC_MODE2_CTRLA_MATCHCLR_Pos)         /**< (RTC_MODE2_CTRLA) Clear on Match Mask */
#define RTC_MODE2_CTRLA_PRESCALER_Pos         (8)                                            /**< (RTC_MODE2_CTRLA) Prescaler Position */
#define RTC_MODE2_CTRLA_PRESCALER_Msk         (0xFU << RTC_MODE2_CTRLA_PRESCALER_Pos)        /**< (RTC_MODE2_CTRLA) Prescaler Mask */
#define RTC_MODE2_CTRLA_PRESCALER(value)      (RTC_MODE2_CTRLA_PRESCALER_Msk & ((value) << RTC_MODE2_CTRLA_PRESCALER_Pos))
#define   RTC_MODE2_CTRLA_PRESCALER_OFF_Val   (0x0U)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/1  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV1_Val  (0x1U)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/1  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV2_Val  (0x2U)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/2  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV4_Val  (0x3U)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/4  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV8_Val  (0x4U)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/8  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV16_Val (0x5U)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/16  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV32_Val (0x6U)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/32  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV64_Val (0x7U)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/64  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV128_Val (0x8U)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/128  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV256_Val (0x9U)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/256  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV512_Val (0xAU)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/512  */
#define   RTC_MODE2_CTRLA_PRESCALER_DIV1024_Val (0xBU)                                         /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/1024  */
#define RTC_MODE2_CTRLA_PRESCALER_OFF         (RTC_MODE2_CTRLA_PRESCALER_OFF_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/1 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV1        (RTC_MODE2_CTRLA_PRESCALER_DIV1_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/1 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV2        (RTC_MODE2_CTRLA_PRESCALER_DIV2_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/2 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV4        (RTC_MODE2_CTRLA_PRESCALER_DIV4_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/4 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV8        (RTC_MODE2_CTRLA_PRESCALER_DIV8_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/8 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV16       (RTC_MODE2_CTRLA_PRESCALER_DIV16_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/16 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV32       (RTC_MODE2_CTRLA_PRESCALER_DIV32_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/32 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV64       (RTC_MODE2_CTRLA_PRESCALER_DIV64_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/64 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV128      (RTC_MODE2_CTRLA_PRESCALER_DIV128_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/128 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV256      (RTC_MODE2_CTRLA_PRESCALER_DIV256_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/256 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV512      (RTC_MODE2_CTRLA_PRESCALER_DIV512_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/512 Position  */
#define RTC_MODE2_CTRLA_PRESCALER_DIV1024     (RTC_MODE2_CTRLA_PRESCALER_DIV1024_Val << RTC_MODE2_CTRLA_PRESCALER_Pos)  /**< (RTC_MODE2_CTRLA) CLK_RTC_CNT = GCLK_RTC/1024 Position  */
#define RTC_MODE2_CTRLA_CLOCKSYNC_Pos         (15)                                           /**< (RTC_MODE2_CTRLA) Clock Read Synchronization Enable Position */
#define RTC_MODE2_CTRLA_CLOCKSYNC_Msk         (0x1U << RTC_MODE2_CTRLA_CLOCKSYNC_Pos)        /**< (RTC_MODE2_CTRLA) Clock Read Synchronization Enable Mask */
#define RTC_MODE2_CTRLA_Msk                   (0x00008FCFUL)                                 /**< (RTC_MODE2_CTRLA) Register Mask  */


#define RTC_MODE2_EVCTRL_RESETVALUE         (0x00U)                                       /**<  (RTC_MODE2_EVCTRL) MODE2 Event Control  Reset Value */

#define RTC_MODE2_EVCTRL_PEREO0_Pos           (0)                                            /**< (RTC_MODE2_EVCTRL) Periodic Interval 0 Event Output Enable Position */
#define RTC_MODE2_EVCTRL_PEREO0_Msk           (0x1U << RTC_MODE2_EVCTRL_PEREO0_Pos)          /**< (RTC_MODE2_EVCTRL) Periodic Interval 0 Event Output Enable Mask */
#define RTC_MODE2_EVCTRL_PEREO1_Pos           (1)                                            /**< (RTC_MODE2_EVCTRL) Periodic Interval 1 Event Output Enable Position */
#define RTC_MODE2_EVCTRL_PEREO1_Msk           (0x1U << RTC_MODE2_EVCTRL_PEREO1_Pos)          /**< (RTC_MODE2_EVCTRL) Periodic Interval 1 Event Output Enable Mask */
#define RTC_MODE2_EVCTRL_PEREO2_Pos           (2)                                            /**< (RTC_MODE2_EVCTRL) Periodic Interval 2 Event Output Enable Position */
#define RTC_MODE2_EVCTRL_PEREO2_Msk           (0x1U << RTC_MODE2_EVCTRL_PEREO2_Pos)          /**< (RTC_MODE2_EVCTRL) Periodic Interval 2 Event Output Enable Mask */
#define RTC_MODE2_EVCTRL_PEREO3_Pos           (3)                                            /**< (RTC_MODE2_EVCTRL) Periodic Interval 3 Event Output Enable Position */
#define RTC_MODE2_EVCTRL_PEREO3_Msk           (0x1U << RTC_MODE2_EVCTRL_PEREO3_Pos)          /**< (RTC_MODE2_EVCTRL) Periodic Interval 3 Event Output Enable Mask */
#define RTC_MODE2_EVCTRL_PEREO4_Pos           (4)                                            /**< (RTC_MODE2_EVCTRL) Periodic Interval 4 Event Output Enable Position */
#define RTC_MODE2_EVCTRL_PEREO4_Msk           (0x1U << RTC_MODE2_EVCTRL_PEREO4_Pos)          /**< (RTC_MODE2_EVCTRL) Periodic Interval 4 Event Output Enable Mask */
#define RTC_MODE2_EVCTRL_PEREO5_Pos           (5)                                            /**< (RTC_MODE2_EVCTRL) Periodic Interval 5 Event Output Enable Position */
#define RTC_MODE2_EVCTRL_PEREO5_Msk           (0x1U << RTC_MODE2_EVCTRL_PEREO5_Pos)          /**< (RTC_MODE2_EVCTRL) Periodic Interval 5 Event Output Enable Mask */
#define RTC_MODE2_EVCTRL_PEREO6_Pos           (6)                                            /**< (RTC_MODE2_EVCTRL) Periodic Interval 6 Event Output Enable Position */
#define RTC_MODE2_EVCTRL_PEREO6_Msk           (0x1U << RTC_MODE2_EVCTRL_PEREO6_Pos)          /**< (RTC_MODE2_EVCTRL) Periodic Interval 6 Event Output Enable Mask */
#define RTC_MODE2_EVCTRL_PEREO7_Pos           (7)                                            /**< (RTC_MODE2_EVCTRL) Periodic Interval 7 Event Output Enable Position */
#define RTC_MODE2_EVCTRL_PEREO7_Msk           (0x1U << RTC_MODE2_EVCTRL_PEREO7_Pos)          /**< (RTC_MODE2_EVCTRL) Periodic Interval 7 Event Output Enable Mask */
#define RTC_MODE2_EVCTRL_ALARMEO0_Pos         (8)                                            /**< (RTC_MODE2_EVCTRL) Alarm 0 Event Output Enable Position */
#define RTC_MODE2_EVCTRL_ALARMEO0_Msk         (0x1U << RTC_MODE2_EVCTRL_ALARMEO0_Pos)        /**< (RTC_MODE2_EVCTRL) Alarm 0 Event Output Enable Mask */
#define RTC_MODE2_EVCTRL_OVFEO_Pos            (15)                                           /**< (RTC_MODE2_EVCTRL) Overflow Event Output Enable Position */
#define RTC_MODE2_EVCTRL_OVFEO_Msk            (0x1U << RTC_MODE2_EVCTRL_OVFEO_Pos)           /**< (RTC_MODE2_EVCTRL) Overflow Event Output Enable Mask */
#define RTC_MODE2_EVCTRL_Msk                  (0x000081FFUL)                                 /**< (RTC_MODE2_EVCTRL) Register Mask  */
#define RTC_MODE2_EVCTRL_PEREO_Pos            (0)                                            /**< (RTC_MODE2_EVCTRL Position) Periodic Interval x Event Output Enable */
#define RTC_MODE2_EVCTRL_PEREO_Msk            (0xFFU << RTC_MODE2_EVCTRL_PEREO_Pos)          /**< (RTC_MODE2_EVCTRL Mask) PEREO */
#define RTC_MODE2_EVCTRL_PEREO(value)         (RTC_MODE2_EVCTRL_PEREO_Msk & ((value) << RTC_MODE2_EVCTRL_PEREO_Pos))


#define RTC_MODE2_INTENCLR_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE2_INTENCLR) MODE2 Interrupt Enable Clear  Reset Value */

#define RTC_MODE2_INTENCLR_PER0_Pos           (0)                                            /**< (RTC_MODE2_INTENCLR) Periodic Interval 0 Interrupt Enable Position */
#define RTC_MODE2_INTENCLR_PER0_Msk           (0x1U << RTC_MODE2_INTENCLR_PER0_Pos)          /**< (RTC_MODE2_INTENCLR) Periodic Interval 0 Interrupt Enable Mask */
#define RTC_MODE2_INTENCLR_PER1_Pos           (1)                                            /**< (RTC_MODE2_INTENCLR) Periodic Interval 1 Interrupt Enable Position */
#define RTC_MODE2_INTENCLR_PER1_Msk           (0x1U << RTC_MODE2_INTENCLR_PER1_Pos)          /**< (RTC_MODE2_INTENCLR) Periodic Interval 1 Interrupt Enable Mask */
#define RTC_MODE2_INTENCLR_PER2_Pos           (2)                                            /**< (RTC_MODE2_INTENCLR) Periodic Interval 2 Interrupt Enable Position */
#define RTC_MODE2_INTENCLR_PER2_Msk           (0x1U << RTC_MODE2_INTENCLR_PER2_Pos)          /**< (RTC_MODE2_INTENCLR) Periodic Interval 2 Interrupt Enable Mask */
#define RTC_MODE2_INTENCLR_PER3_Pos           (3)                                            /**< (RTC_MODE2_INTENCLR) Periodic Interval 3 Interrupt Enable Position */
#define RTC_MODE2_INTENCLR_PER3_Msk           (0x1U << RTC_MODE2_INTENCLR_PER3_Pos)          /**< (RTC_MODE2_INTENCLR) Periodic Interval 3 Interrupt Enable Mask */
#define RTC_MODE2_INTENCLR_PER4_Pos           (4)                                            /**< (RTC_MODE2_INTENCLR) Periodic Interval 4 Interrupt Enable Position */
#define RTC_MODE2_INTENCLR_PER4_Msk           (0x1U << RTC_MODE2_INTENCLR_PER4_Pos)          /**< (RTC_MODE2_INTENCLR) Periodic Interval 4 Interrupt Enable Mask */
#define RTC_MODE2_INTENCLR_PER5_Pos           (5)                                            /**< (RTC_MODE2_INTENCLR) Periodic Interval 5 Interrupt Enable Position */
#define RTC_MODE2_INTENCLR_PER5_Msk           (0x1U << RTC_MODE2_INTENCLR_PER5_Pos)          /**< (RTC_MODE2_INTENCLR) Periodic Interval 5 Interrupt Enable Mask */
#define RTC_MODE2_INTENCLR_PER6_Pos           (6)                                            /**< (RTC_MODE2_INTENCLR) Periodic Interval 6 Interrupt Enable Position */
#define RTC_MODE2_INTENCLR_PER6_Msk           (0x1U << RTC_MODE2_INTENCLR_PER6_Pos)          /**< (RTC_MODE2_INTENCLR) Periodic Interval 6 Interrupt Enable Mask */
#define RTC_MODE2_INTENCLR_PER7_Pos           (7)                                            /**< (RTC_MODE2_INTENCLR) Periodic Interval 7 Interrupt Enable Position */
#define RTC_MODE2_INTENCLR_PER7_Msk           (0x1U << RTC_MODE2_INTENCLR_PER7_Pos)          /**< (RTC_MODE2_INTENCLR) Periodic Interval 7 Interrupt Enable Mask */
#define RTC_MODE2_INTENCLR_ALARM0_Pos         (8)                                            /**< (RTC_MODE2_INTENCLR) Alarm 0 Interrupt Enable Position */
#define RTC_MODE2_INTENCLR_ALARM0_Msk         (0x1U << RTC_MODE2_INTENCLR_ALARM0_Pos)        /**< (RTC_MODE2_INTENCLR) Alarm 0 Interrupt Enable Mask */
#define RTC_MODE2_INTENCLR_OVF_Pos            (15)                                           /**< (RTC_MODE2_INTENCLR) Overflow Interrupt Enable Position */
#define RTC_MODE2_INTENCLR_OVF_Msk            (0x1U << RTC_MODE2_INTENCLR_OVF_Pos)           /**< (RTC_MODE2_INTENCLR) Overflow Interrupt Enable Mask */
#define RTC_MODE2_INTENCLR_Msk                (0x000081FFUL)                                 /**< (RTC_MODE2_INTENCLR) Register Mask  */
#define RTC_MODE2_INTENCLR_PER_Pos            (0)                                            /**< (RTC_MODE2_INTENCLR Position) Periodic Interval x Interrupt Enable */
#define RTC_MODE2_INTENCLR_PER_Msk            (0xFFU << RTC_MODE2_INTENCLR_PER_Pos)          /**< (RTC_MODE2_INTENCLR Mask) PER */
#define RTC_MODE2_INTENCLR_PER(value)         (RTC_MODE2_INTENCLR_PER_Msk & ((value) << RTC_MODE2_INTENCLR_PER_Pos))


#define RTC_MODE2_INTENSET_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE2_INTENSET) MODE2 Interrupt Enable Set  Reset Value */

#define RTC_MODE2_INTENSET_PER0_Pos           (0)                                            /**< (RTC_MODE2_INTENSET) Periodic Interval 0 Enable Position */
#define RTC_MODE2_INTENSET_PER0_Msk           (0x1U << RTC_MODE2_INTENSET_PER0_Pos)          /**< (RTC_MODE2_INTENSET) Periodic Interval 0 Enable Mask */
#define RTC_MODE2_INTENSET_PER1_Pos           (1)                                            /**< (RTC_MODE2_INTENSET) Periodic Interval 1 Enable Position */
#define RTC_MODE2_INTENSET_PER1_Msk           (0x1U << RTC_MODE2_INTENSET_PER1_Pos)          /**< (RTC_MODE2_INTENSET) Periodic Interval 1 Enable Mask */
#define RTC_MODE2_INTENSET_PER2_Pos           (2)                                            /**< (RTC_MODE2_INTENSET) Periodic Interval 2 Enable Position */
#define RTC_MODE2_INTENSET_PER2_Msk           (0x1U << RTC_MODE2_INTENSET_PER2_Pos)          /**< (RTC_MODE2_INTENSET) Periodic Interval 2 Enable Mask */
#define RTC_MODE2_INTENSET_PER3_Pos           (3)                                            /**< (RTC_MODE2_INTENSET) Periodic Interval 3 Enable Position */
#define RTC_MODE2_INTENSET_PER3_Msk           (0x1U << RTC_MODE2_INTENSET_PER3_Pos)          /**< (RTC_MODE2_INTENSET) Periodic Interval 3 Enable Mask */
#define RTC_MODE2_INTENSET_PER4_Pos           (4)                                            /**< (RTC_MODE2_INTENSET) Periodic Interval 4 Enable Position */
#define RTC_MODE2_INTENSET_PER4_Msk           (0x1U << RTC_MODE2_INTENSET_PER4_Pos)          /**< (RTC_MODE2_INTENSET) Periodic Interval 4 Enable Mask */
#define RTC_MODE2_INTENSET_PER5_Pos           (5)                                            /**< (RTC_MODE2_INTENSET) Periodic Interval 5 Enable Position */
#define RTC_MODE2_INTENSET_PER5_Msk           (0x1U << RTC_MODE2_INTENSET_PER5_Pos)          /**< (RTC_MODE2_INTENSET) Periodic Interval 5 Enable Mask */
#define RTC_MODE2_INTENSET_PER6_Pos           (6)                                            /**< (RTC_MODE2_INTENSET) Periodic Interval 6 Enable Position */
#define RTC_MODE2_INTENSET_PER6_Msk           (0x1U << RTC_MODE2_INTENSET_PER6_Pos)          /**< (RTC_MODE2_INTENSET) Periodic Interval 6 Enable Mask */
#define RTC_MODE2_INTENSET_PER7_Pos           (7)                                            /**< (RTC_MODE2_INTENSET) Periodic Interval 7 Enable Position */
#define RTC_MODE2_INTENSET_PER7_Msk           (0x1U << RTC_MODE2_INTENSET_PER7_Pos)          /**< (RTC_MODE2_INTENSET) Periodic Interval 7 Enable Mask */
#define RTC_MODE2_INTENSET_ALARM0_Pos         (8)                                            /**< (RTC_MODE2_INTENSET) Alarm 0 Interrupt Enable Position */
#define RTC_MODE2_INTENSET_ALARM0_Msk         (0x1U << RTC_MODE2_INTENSET_ALARM0_Pos)        /**< (RTC_MODE2_INTENSET) Alarm 0 Interrupt Enable Mask */
#define RTC_MODE2_INTENSET_OVF_Pos            (15)                                           /**< (RTC_MODE2_INTENSET) Overflow Interrupt Enable Position */
#define RTC_MODE2_INTENSET_OVF_Msk            (0x1U << RTC_MODE2_INTENSET_OVF_Pos)           /**< (RTC_MODE2_INTENSET) Overflow Interrupt Enable Mask */
#define RTC_MODE2_INTENSET_Msk                (0x000081FFUL)                                 /**< (RTC_MODE2_INTENSET) Register Mask  */
#define RTC_MODE2_INTENSET_PER_Pos            (0)                                            /**< (RTC_MODE2_INTENSET Position) Periodic Interval x Enable */
#define RTC_MODE2_INTENSET_PER_Msk            (0xFFU << RTC_MODE2_INTENSET_PER_Pos)          /**< (RTC_MODE2_INTENSET Mask) PER */
#define RTC_MODE2_INTENSET_PER(value)         (RTC_MODE2_INTENSET_PER_Msk & ((value) << RTC_MODE2_INTENSET_PER_Pos))


#define RTC_MODE2_INTFLAG_RESETVALUE        (0x00U)                                       /**<  (RTC_MODE2_INTFLAG) MODE2 Interrupt Flag Status and Clear  Reset Value */

#define RTC_MODE2_INTFLAG_PER0_Pos            (0)                                            /**< (RTC_MODE2_INTFLAG) Periodic Interval 0 Position */
#define RTC_MODE2_INTFLAG_PER0_Msk            (0x1U << RTC_MODE2_INTFLAG_PER0_Pos)           /**< (RTC_MODE2_INTFLAG) Periodic Interval 0 Mask */
#define RTC_MODE2_INTFLAG_PER1_Pos            (1)                                            /**< (RTC_MODE2_INTFLAG) Periodic Interval 1 Position */
#define RTC_MODE2_INTFLAG_PER1_Msk            (0x1U << RTC_MODE2_INTFLAG_PER1_Pos)           /**< (RTC_MODE2_INTFLAG) Periodic Interval 1 Mask */
#define RTC_MODE2_INTFLAG_PER2_Pos            (2)                                            /**< (RTC_MODE2_INTFLAG) Periodic Interval 2 Position */
#define RTC_MODE2_INTFLAG_PER2_Msk            (0x1U << RTC_MODE2_INTFLAG_PER2_Pos)           /**< (RTC_MODE2_INTFLAG) Periodic Interval 2 Mask */
#define RTC_MODE2_INTFLAG_PER3_Pos            (3)                                            /**< (RTC_MODE2_INTFLAG) Periodic Interval 3 Position */
#define RTC_MODE2_INTFLAG_PER3_Msk            (0x1U << RTC_MODE2_INTFLAG_PER3_Pos)           /**< (RTC_MODE2_INTFLAG) Periodic Interval 3 Mask */
#define RTC_MODE2_INTFLAG_PER4_Pos            (4)                                            /**< (RTC_MODE2_INTFLAG) Periodic Interval 4 Position */
#define RTC_MODE2_INTFLAG_PER4_Msk            (0x1U << RTC_MODE2_INTFLAG_PER4_Pos)           /**< (RTC_MODE2_INTFLAG) Periodic Interval 4 Mask */
#define RTC_MODE2_INTFLAG_PER5_Pos            (5)                                            /**< (RTC_MODE2_INTFLAG) Periodic Interval 5 Position */
#define RTC_MODE2_INTFLAG_PER5_Msk            (0x1U << RTC_MODE2_INTFLAG_PER5_Pos)           /**< (RTC_MODE2_INTFLAG) Periodic Interval 5 Mask */
#define RTC_MODE2_INTFLAG_PER6_Pos            (6)                                            /**< (RTC_MODE2_INTFLAG) Periodic Interval 6 Position */
#define RTC_MODE2_INTFLAG_PER6_Msk            (0x1U << RTC_MODE2_INTFLAG_PER6_Pos)           /**< (RTC_MODE2_INTFLAG) Periodic Interval 6 Mask */
#define RTC_MODE2_INTFLAG_PER7_Pos            (7)                                            /**< (RTC_MODE2_INTFLAG) Periodic Interval 7 Position */
#define RTC_MODE2_INTFLAG_PER7_Msk            (0x1U << RTC_MODE2_INTFLAG_PER7_Pos)           /**< (RTC_MODE2_INTFLAG) Periodic Interval 7 Mask */
#define RTC_MODE2_INTFLAG_ALARM0_Pos          (8)                                            /**< (RTC_MODE2_INTFLAG) Alarm 0 Position */
#define RTC_MODE2_INTFLAG_ALARM0_Msk          (0x1U << RTC_MODE2_INTFLAG_ALARM0_Pos)         /**< (RTC_MODE2_INTFLAG) Alarm 0 Mask */
#define RTC_MODE2_INTFLAG_OVF_Pos             (15)                                           /**< (RTC_MODE2_INTFLAG) Overflow Position */
#define RTC_MODE2_INTFLAG_OVF_Msk             (0x1U << RTC_MODE2_INTFLAG_OVF_Pos)            /**< (RTC_MODE2_INTFLAG) Overflow Mask */
#define RTC_MODE2_INTFLAG_Msk                 (0x000081FFUL)                                 /**< (RTC_MODE2_INTFLAG) Register Mask  */
#define RTC_MODE2_INTFLAG_PER_Pos             (0)                                            /**< (RTC_MODE2_INTFLAG Position) Periodic Interval x */
#define RTC_MODE2_INTFLAG_PER_Msk             (0xFFU << RTC_MODE2_INTFLAG_PER_Pos)           /**< (RTC_MODE2_INTFLAG Mask) PER */
#define RTC_MODE2_INTFLAG_PER(value)          (RTC_MODE2_INTFLAG_PER_Msk & ((value) << RTC_MODE2_INTFLAG_PER_Pos))


#define RTC_MODE2_DBGCTRL_RESETVALUE        (0x00U)                                       /**<  (RTC_MODE2_DBGCTRL) Debug Control  Reset Value */

#define RTC_MODE2_DBGCTRL_DBGRUN_Pos          (0)                                            /**< (RTC_MODE2_DBGCTRL) Run During Debug Position */
#define RTC_MODE2_DBGCTRL_DBGRUN_Msk          (0x1U << RTC_MODE2_DBGCTRL_DBGRUN_Pos)         /**< (RTC_MODE2_DBGCTRL) Run During Debug Mask */
#define RTC_MODE2_DBGCTRL_Msk                 (0x00000001UL)                                 /**< (RTC_MODE2_DBGCTRL) Register Mask  */




#define RTC_MODE2_SYNCBUSY_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE2_SYNCBUSY) MODE2 Synchronization Busy Status  Reset Value */

#define RTC_MODE2_SYNCBUSY_SWRST_Pos          (0)                                            /**< (RTC_MODE2_SYNCBUSY) Software Reset Bit Busy Position */
#define RTC_MODE2_SYNCBUSY_SWRST_Msk          (0x1U << RTC_MODE2_SYNCBUSY_SWRST_Pos)         /**< (RTC_MODE2_SYNCBUSY) Software Reset Bit Busy Mask */
#define RTC_MODE2_SYNCBUSY_ENABLE_Pos         (1)                                            /**< (RTC_MODE2_SYNCBUSY) Enable Bit Busy Position */
#define RTC_MODE2_SYNCBUSY_ENABLE_Msk         (0x1U << RTC_MODE2_SYNCBUSY_ENABLE_Pos)        /**< (RTC_MODE2_SYNCBUSY) Enable Bit Busy Mask */
#define RTC_MODE2_SYNCBUSY_FREQCORR_Pos       (2)                                            /**< (RTC_MODE2_SYNCBUSY) FREQCORR Register Busy Position */
#define RTC_MODE2_SYNCBUSY_FREQCORR_Msk       (0x1U << RTC_MODE2_SYNCBUSY_FREQCORR_Pos)      /**< (RTC_MODE2_SYNCBUSY) FREQCORR Register Busy Mask */
#define RTC_MODE2_SYNCBUSY_CLOCK_Pos          (3)                                            /**< (RTC_MODE2_SYNCBUSY) CLOCK Register Busy Position */
#define RTC_MODE2_SYNCBUSY_CLOCK_Msk          (0x1U << RTC_MODE2_SYNCBUSY_CLOCK_Pos)         /**< (RTC_MODE2_SYNCBUSY) CLOCK Register Busy Mask */
#define RTC_MODE2_SYNCBUSY_ALARM0_Pos         (5)                                            /**< (RTC_MODE2_SYNCBUSY) ALARM 0 Register Busy Position */
#define RTC_MODE2_SYNCBUSY_ALARM0_Msk         (0x1U << RTC_MODE2_SYNCBUSY_ALARM0_Pos)        /**< (RTC_MODE2_SYNCBUSY) ALARM 0 Register Busy Mask */
#define RTC_MODE2_SYNCBUSY_MASK0_Pos          (11)                                           /**< (RTC_MODE2_SYNCBUSY) MASK 0 Register Busy Position */
#define RTC_MODE2_SYNCBUSY_MASK0_Msk          (0x1U << RTC_MODE2_SYNCBUSY_MASK0_Pos)         /**< (RTC_MODE2_SYNCBUSY) MASK 0 Register Busy Mask */
#define RTC_MODE2_SYNCBUSY_CLOCKSYNC_Pos      (15)                                           /**< (RTC_MODE2_SYNCBUSY) Clock Read Synchronization Enable Bit Busy Position */
#define RTC_MODE2_SYNCBUSY_CLOCKSYNC_Msk      (0x1U << RTC_MODE2_SYNCBUSY_CLOCKSYNC_Pos)     /**< (RTC_MODE2_SYNCBUSY) Clock Read Synchronization Enable Bit Busy Mask */
#define RTC_MODE2_SYNCBUSY_Msk                (0x0000882FUL)                                 /**< (RTC_MODE2_SYNCBUSY) Register Mask  */




#define RTC_MODE2_FREQCORR_RESETVALUE       (0x00U)                                       /**<  (RTC_MODE2_FREQCORR) Frequency Correction  Reset Value */

#define RTC_MODE2_FREQCORR_VALUE_Pos          (0)                                            /**< (RTC_MODE2_FREQCORR) Correction Value Position */
#define RTC_MODE2_FREQCORR_VALUE_Msk          (0x7FU << RTC_MODE2_FREQCORR_VALUE_Pos)        /**< (RTC_MODE2_FREQCORR) Correction Value Mask */
#define RTC_MODE2_FREQCORR_VALUE(value)       (RTC_MODE2_FREQCORR_VALUE_Msk & ((value) << RTC_MODE2_FREQCORR_VALUE_Pos))
#define RTC_MODE2_FREQCORR_SIGN_Pos           (7)                                            /**< (RTC_MODE2_FREQCORR) Correction Sign Position */
#define RTC_MODE2_FREQCORR_SIGN_Msk           (0x1U << RTC_MODE2_FREQCORR_SIGN_Pos)          /**< (RTC_MODE2_FREQCORR) Correction Sign Mask */
#define RTC_MODE2_FREQCORR_Msk                (0x000000FFUL)                                 /**< (RTC_MODE2_FREQCORR) Register Mask  */



#define RTC_MODE2_CLOCK_RESETVALUE          (0x00U)                                       /**<  (RTC_MODE2_CLOCK) MODE2 Clock Value  Reset Value */

#define RTC_MODE2_CLOCK_SECOND_Pos            (0)                                            /**< (RTC_MODE2_CLOCK) Second Position */
#define RTC_MODE2_CLOCK_SECOND_Msk            (0x3FU << RTC_MODE2_CLOCK_SECOND_Pos)          /**< (RTC_MODE2_CLOCK) Second Mask */
#define RTC_MODE2_CLOCK_SECOND(value)         (RTC_MODE2_CLOCK_SECOND_Msk & ((value) << RTC_MODE2_CLOCK_SECOND_Pos))
#define RTC_MODE2_CLOCK_MINUTE_Pos            (6)                                            /**< (RTC_MODE2_CLOCK) Minute Position */
#define RTC_MODE2_CLOCK_MINUTE_Msk            (0x3FU << RTC_MODE2_CLOCK_MINUTE_Pos)          /**< (RTC_MODE2_CLOCK) Minute Mask */
#define RTC_MODE2_CLOCK_MINUTE(value)         (RTC_MODE2_CLOCK_MINUTE_Msk & ((value) << RTC_MODE2_CLOCK_MINUTE_Pos))
#define RTC_MODE2_CLOCK_HOUR_Pos              (12)                                           /**< (RTC_MODE2_CLOCK) Hour Position */
#define RTC_MODE2_CLOCK_HOUR_Msk              (0x1FU << RTC_MODE2_CLOCK_HOUR_Pos)            /**< (RTC_MODE2_CLOCK) Hour Mask */
#define RTC_MODE2_CLOCK_HOUR(value)           (RTC_MODE2_CLOCK_HOUR_Msk & ((value) << RTC_MODE2_CLOCK_HOUR_Pos))
#define   RTC_MODE2_CLOCK_HOUR_AM_Val         (0x0U)                                         /**< (RTC_MODE2_CLOCK) AM when CLKREP in 12-hour  */
#define   RTC_MODE2_CLOCK_HOUR_PM_Val         (0x10U)                                        /**< (RTC_MODE2_CLOCK) PM when CLKREP in 12-hour  */
#define RTC_MODE2_CLOCK_HOUR_AM               (RTC_MODE2_CLOCK_HOUR_AM_Val << RTC_MODE2_CLOCK_HOUR_Pos)  /**< (RTC_MODE2_CLOCK) AM when CLKREP in 12-hour Position  */
#define RTC_MODE2_CLOCK_HOUR_PM               (RTC_MODE2_CLOCK_HOUR_PM_Val << RTC_MODE2_CLOCK_HOUR_Pos)  /**< (RTC_MODE2_CLOCK) PM when CLKREP in 12-hour Position  */
#define RTC_MODE2_CLOCK_DAY_Pos               (17)                                           /**< (RTC_MODE2_CLOCK) Day Position */
#define RTC_MODE2_CLOCK_DAY_Msk               (0x1FU << RTC_MODE2_CLOCK_DAY_Pos)             /**< (RTC_MODE2_CLOCK) Day Mask */
#define RTC_MODE2_CLOCK_DAY(value)            (RTC_MODE2_CLOCK_DAY_Msk & ((value) << RTC_MODE2_CLOCK_DAY_Pos))
#define RTC_MODE2_CLOCK_MONTH_Pos             (22)                                           /**< (RTC_MODE2_CLOCK) Month Position */
#define RTC_MODE2_CLOCK_MONTH_Msk             (0xFU << RTC_MODE2_CLOCK_MONTH_Pos)            /**< (RTC_MODE2_CLOCK) Month Mask */
#define RTC_MODE2_CLOCK_MONTH(value)          (RTC_MODE2_CLOCK_MONTH_Msk & ((value) << RTC_MODE2_CLOCK_MONTH_Pos))
#define RTC_MODE2_CLOCK_YEAR_Pos              (26)                                           /**< (RTC_MODE2_CLOCK) Year Position */
#define RTC_MODE2_CLOCK_YEAR_Msk              (0x3FU << RTC_MODE2_CLOCK_YEAR_Pos)            /**< (RTC_MODE2_CLOCK) Year Mask */
#define RTC_MODE2_CLOCK_YEAR(value)           (RTC_MODE2_CLOCK_YEAR_Msk & ((value) << RTC_MODE2_CLOCK_YEAR_Pos))
#define RTC_MODE2_CLOCK_Msk                   (0xFFFFFFFFUL)                                 /**< (RTC_MODE2_CLOCK) Register Mask  */

/** \brief MODE2_ALARM register offsets definitions */
#define RTC_MODE2_ALARM_ALARM_OFFSET (0x00)         /**< (RTC_MODE2_ALARM_ALARM) MODE2_ALARM Alarm n Value Offset */
#define RTC_MODE2_ALARM_MASK_OFFSET  (0x04)         /**< (RTC_MODE2_ALARM_MASK) MODE2_ALARM Alarm n Mask Offset */
/** \brief RTC_MODE0 register offsets definitions */
#define RTC_MODE0_CTRLA_OFFSET       (0x00)         /**< (RTC_MODE0_CTRLA) MODE0 Control A Offset */
#define RTC_MODE0_EVCTRL_OFFSET      (0x04)         /**< (RTC_MODE0_EVCTRL) MODE0 Event Control Offset */
#define RTC_MODE0_INTENCLR_OFFSET    (0x08)         /**< (RTC_MODE0_INTENCLR) MODE0 Interrupt Enable Clear Offset */
#define RTC_MODE0_INTENSET_OFFSET    (0x0A)         /**< (RTC_MODE0_INTENSET) MODE0 Interrupt Enable Set Offset */
#define RTC_MODE0_INTFLAG_OFFSET     (0x0C)         /**< (RTC_MODE0_INTFLAG) MODE0 Interrupt Flag Status and Clear Offset */
#define RTC_MODE0_DBGCTRL_OFFSET     (0x0E)         /**< (RTC_MODE0_DBGCTRL) Debug Control Offset */
#define RTC_MODE0_SYNCBUSY_OFFSET    (0x10)         /**< (RTC_MODE0_SYNCBUSY) MODE0 Synchronization Busy Status Offset */
#define RTC_MODE0_FREQCORR_OFFSET    (0x14)         /**< (RTC_MODE0_FREQCORR) Frequency Correction Offset */
#define RTC_MODE0_COUNT_OFFSET       (0x18)         /**< (RTC_MODE0_COUNT) MODE0 Counter Value Offset */
#define RTC_MODE0_COMP_OFFSET        (0x20)         /**< (RTC_MODE0_COMP) MODE0 Compare n Value Offset */
/** \brief RTC_MODE1 register offsets definitions */
#define RTC_MODE1_CTRLA_OFFSET       (0x00)         /**< (RTC_MODE1_CTRLA) MODE1 Control A Offset */
#define RTC_MODE1_EVCTRL_OFFSET      (0x04)         /**< (RTC_MODE1_EVCTRL) MODE1 Event Control Offset */
#define RTC_MODE1_INTENCLR_OFFSET    (0x08)         /**< (RTC_MODE1_INTENCLR) MODE1 Interrupt Enable Clear Offset */
#define RTC_MODE1_INTENSET_OFFSET    (0x0A)         /**< (RTC_MODE1_INTENSET) MODE1 Interrupt Enable Set Offset */
#define RTC_MODE1_INTFLAG_OFFSET     (0x0C)         /**< (RTC_MODE1_INTFLAG) MODE1 Interrupt Flag Status and Clear Offset */
#define RTC_MODE1_DBGCTRL_OFFSET     (0x0E)         /**< (RTC_MODE1_DBGCTRL) Debug Control Offset */
#define RTC_MODE1_SYNCBUSY_OFFSET    (0x10)         /**< (RTC_MODE1_SYNCBUSY) MODE1 Synchronization Busy Status Offset */
#define RTC_MODE1_FREQCORR_OFFSET    (0x14)         /**< (RTC_MODE1_FREQCORR) Frequency Correction Offset */
#define RTC_MODE1_COUNT_OFFSET       (0x18)         /**< (RTC_MODE1_COUNT) MODE1 Counter Value Offset */
#define RTC_MODE1_PER_OFFSET         (0x1C)         /**< (RTC_MODE1_PER) MODE1 Counter Period Offset */
#define RTC_MODE1_COMP_OFFSET        (0x20)         /**< (RTC_MODE1_COMP) MODE1 Compare n Value Offset */
/** \brief RTC_MODE2 register offsets definitions */
#define RTC_MODE2_CTRLA_OFFSET       (0x00)         /**< (RTC_MODE2_CTRLA) MODE2 Control A Offset */
#define RTC_MODE2_EVCTRL_OFFSET      (0x04)         /**< (RTC_MODE2_EVCTRL) MODE2 Event Control Offset */
#define RTC_MODE2_INTENCLR_OFFSET    (0x08)         /**< (RTC_MODE2_INTENCLR) MODE2 Interrupt Enable Clear Offset */
#define RTC_MODE2_INTENSET_OFFSET    (0x0A)         /**< (RTC_MODE2_INTENSET) MODE2 Interrupt Enable Set Offset */
#define RTC_MODE2_INTFLAG_OFFSET     (0x0C)         /**< (RTC_MODE2_INTFLAG) MODE2 Interrupt Flag Status and Clear Offset */
#define RTC_MODE2_DBGCTRL_OFFSET     (0x0E)         /**< (RTC_MODE2_DBGCTRL) Debug Control Offset */
#define RTC_MODE2_SYNCBUSY_OFFSET    (0x10)         /**< (RTC_MODE2_SYNCBUSY) MODE2 Synchronization Busy Status Offset */
#define RTC_MODE2_FREQCORR_OFFSET    (0x14)         /**< (RTC_MODE2_FREQCORR) Frequency Correction Offset */
#define RTC_MODE2_CLOCK_OFFSET       (0x18)         /**< (RTC_MODE2_CLOCK) MODE2 Clock Value Offset */
/** \brief RTC register offsets definitions */



/** \brief RTC_MODE0 register API structure */
typedef struct
{  /* Real-Time Counter - 32-bit Counter with Single 32-bit Compare */
  __IO  uint16_t       CTRLA;         /**< Offset: 0x00 (R/W  16) MODE0 Control A */
  __I   uint8_t                        Reserved1[0x02];
  __IO  uint32_t      EVCTRL;        /**< Offset: 0x04 (R/W  32) MODE0 Event Control */
  __IO  uint16_t    INTENCLR;      /**< Offset: 0x08 (R/W  16) MODE0 Interrupt Enable Clear */
  __IO  uint16_t    INTENSET;      /**< Offset: 0x0A (R/W  16) MODE0 Interrupt Enable Set */
  __IO  uint16_t     INTFLAG;       /**< Offset: 0x0C (R/W  16) MODE0 Interrupt Flag Status and Clear */
  __IO  uint8_t     DBGCTRL;       /**< Offset: 0x0E (R/W   8) Debug Control */
  __I   uint8_t                        Reserved2[0x01];
  __I   uint32_t    SYNCBUSY;      /**< Offset: 0x10 (R/   32) MODE0 Synchronization Busy Status */
  __IO  uint8_t    FREQCORR;      /**< Offset: 0x14 (R/W   8) Frequency Correction */
  __I   uint8_t                        Reserved3[0x03];
  __IO  uint32_t       COUNT;         /**< Offset: 0x18 (R/W  32) MODE0 Counter Value */
  __I   uint8_t                        Reserved4[0x04];
  __IO  uint32_t        COMP;          /**< Offset: 0x20 (R/W  32) MODE0 Compare n Value */
} rtcmode0_registers_t;

/** \brief RTC_MODE1 register API structure */
typedef struct
{  /* Real-Time Counter - 16-bit Counter with Two 16-bit Compares */
  __IO  uint16_t       CTRLA;         /**< Offset: 0x00 (R/W  16) MODE1 Control A */
  __I   uint8_t                        Reserved1[0x02];
  __IO  uint32_t      EVCTRL;        /**< Offset: 0x04 (R/W  32) MODE1 Event Control */
  __IO  uint16_t    INTENCLR;      /**< Offset: 0x08 (R/W  16) MODE1 Interrupt Enable Clear */
  __IO  uint16_t    INTENSET;      /**< Offset: 0x0A (R/W  16) MODE1 Interrupt Enable Set */
  __IO  uint16_t     INTFLAG;       /**< Offset: 0x0C (R/W  16) MODE1 Interrupt Flag Status and Clear */
  __IO  uint8_t     DBGCTRL;       /**< Offset: 0x0E (R/W   8) Debug Control */
  __I   uint8_t                        Reserved2[0x01];
  __I   uint32_t    SYNCBUSY;      /**< Offset: 0x10 (R/   32) MODE1 Synchronization Busy Status */
  __IO  uint8_t    FREQCORR;      /**< Offset: 0x14 (R/W   8) Frequency Correction */
  __I   uint8_t                        Reserved3[0x03];
  __IO  uint16_t       COUNT;         /**< Offset: 0x18 (R/W  16) MODE1 Counter Value */
  __I   uint8_t                        Reserved4[0x02];
  __IO  uint16_t         PER;           /**< Offset: 0x1C (R/W  16) MODE1 Counter Period */
  __I   uint8_t                        Reserved5[0x02];
  __IO  uint16_t        COMP[2];       /**< Offset: 0x20 (R/W  16) MODE1 Compare n Value */
} rtcmode1_registers_t;

/** \brief RTC_MODE2 register API structure */
typedef struct
{  /* Real-Time Counter - Clock/Calendar with Alarm */
  __IO  uint16_t                         CTRLA;         /**< Offset: 0x00 (R/W  16) MODE2 Control A */
  __I   uint8_t                        Reserved1[0x02];
  __IO  uint32_t                         EVCTRL;        /**< Offset: 0x04 (R/W  32) MODE2 Event Control */
  __IO  uint16_t                        INTENCLR;      /**< Offset: 0x08 (R/W  16) MODE2 Interrupt Enable Clear */
  __IO  uint16_t                        INTENSET;      /**< Offset: 0x0A (R/W  16) MODE2 Interrupt Enable Set */
  __IO  uint16_t                        INTFLAG;       /**< Offset: 0x0C (R/W  16) MODE2 Interrupt Flag Status and Clear */
  __IO  uint8_t                         DBGCTRL;       /**< Offset: 0x0E (R/W   8) Debug Control */
  __I   uint8_t                        Reserved2[0x01];
  __I   uint32_t                        SYNCBUSY;      /**< Offset: 0x10 (R/   32) MODE2 Synchronization Busy Status */
  __IO  uint8_t                        FREQCORR;      /**< Offset: 0x14 (R/W   8) Frequency Correction */
  __I   uint8_t                        Reserved3[0x03];
  __IO  uint32_t                        CLOCK;         /**< Offset: 0x18 (R/W  32) MODE2 Clock Value */
  __I   uint8_t                        Reserved4[0x04];
  __IO  uint32_t                        Mode2Alarm;     /**< Offset: 0x20  */
  __IO  uint8_t                         Mode2AlarmMask;  /**< Offest: 0x24  */ 

} rtcmode2_registers_t;

/** \brief RTC register API structure */

typedef union
{  /* Real-Time Counter */
       rtcmode0_registers_t           MODE0;          /**< Offset: 0x00 Real-Time Counter - 32-bit Counter with Single 32-bit Compare */
       rtcmode1_registers_t           MODE1;          /**< Offset: 0x00 Real-Time Counter - 16-bit Counter with Two 16-bit Compares */
       rtcmode2_registers_t           MODE2;          /**< Offset: 0x00 Real-Time Counter - Clock/Calendar with Alarm */
} rtc_registers_t;
/** @}  end of Real-Time Counter */

#endif /* _PIC32CM_JH21_RTC_COMPONENT_H_ */
