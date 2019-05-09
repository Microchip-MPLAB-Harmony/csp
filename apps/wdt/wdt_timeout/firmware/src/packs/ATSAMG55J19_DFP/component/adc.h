/**
 * \brief Header file for SAMG/SAMG55 ADC
 *
 * Copyright (c) 2017-2019 Microchip Technology Inc.
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

/* file generated from device description version 2019-05-09T03:59:29Z */
#ifndef SAMG_SAMG55_ADC_MODULE_H
#define SAMG_SAMG55_ADC_MODULE_H

/** \addtogroup SAMG_SAMG55 Analog-to-Digital Converter
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_ADC                                   */
/* ========================================================================== */

/* -------- ADC_CR : (ADC Offset: 0x00) ( /W 32) Control Register -------- */
#define ADC_CR_SWRST_Pos                      (0U)                                           /**< (ADC_CR) Software Reset Position */
#define ADC_CR_SWRST_Msk                      (0x1U << ADC_CR_SWRST_Pos)                     /**< (ADC_CR) Software Reset Mask */
#define ADC_CR_SWRST(value)                   (ADC_CR_SWRST_Msk & ((value) << ADC_CR_SWRST_Pos))
#define ADC_CR_START_Pos                      (1U)                                           /**< (ADC_CR) Start Conversion Position */
#define ADC_CR_START_Msk                      (0x1U << ADC_CR_START_Pos)                     /**< (ADC_CR) Start Conversion Mask */
#define ADC_CR_START(value)                   (ADC_CR_START_Msk & ((value) << ADC_CR_START_Pos))
#define ADC_CR_CMPRST_Pos                     (4U)                                           /**< (ADC_CR) Comparison Restart Position */
#define ADC_CR_CMPRST_Msk                     (0x1U << ADC_CR_CMPRST_Pos)                    /**< (ADC_CR) Comparison Restart Mask */
#define ADC_CR_CMPRST(value)                  (ADC_CR_CMPRST_Msk & ((value) << ADC_CR_CMPRST_Pos))
#define ADC_CR_Msk                            (0x00000013UL)                                 /**< (ADC_CR) Register Mask  */

/* -------- ADC_MR : (ADC Offset: 0x04) (R/W 32) Mode Register -------- */
#define ADC_MR_TRGEN_Pos                      (0U)                                           /**< (ADC_MR) Trigger Enable Position */
#define ADC_MR_TRGEN_Msk                      (0x1U << ADC_MR_TRGEN_Pos)                     /**< (ADC_MR) Trigger Enable Mask */
#define ADC_MR_TRGEN(value)                   (ADC_MR_TRGEN_Msk & ((value) << ADC_MR_TRGEN_Pos))
#define   ADC_MR_TRGEN_DIS_Val                (0U)                                           /**< (ADC_MR) Hardware triggers are disabled. Starting a conversion is only possible by software.  */
#define   ADC_MR_TRGEN_EN_Val                 (1U)                                           /**< (ADC_MR) Hardware trigger selected by TRGSEL field is enabled.  */
#define ADC_MR_TRGEN_DIS                      (ADC_MR_TRGEN_DIS_Val << ADC_MR_TRGEN_Pos)     /**< (ADC_MR) Hardware triggers are disabled. Starting a conversion is only possible by software. Position  */
#define ADC_MR_TRGEN_EN                       (ADC_MR_TRGEN_EN_Val << ADC_MR_TRGEN_Pos)      /**< (ADC_MR) Hardware trigger selected by TRGSEL field is enabled. Position  */
#define ADC_MR_TRGSEL_Pos                     (1U)                                           /**< (ADC_MR) Trigger Selection Position */
#define ADC_MR_TRGSEL_Msk                     (0x7U << ADC_MR_TRGSEL_Pos)                    /**< (ADC_MR) Trigger Selection Mask */
#define ADC_MR_TRGSEL(value)                  (ADC_MR_TRGSEL_Msk & ((value) << ADC_MR_TRGSEL_Pos))
#define   ADC_MR_TRGSEL_ADC_TRIG0_Val         (0U)                                           /**< (ADC_MR) ADTRG External trigger  */
#define   ADC_MR_TRGSEL_ADC_TRIG1_Val         (1U)                                           /**< (ADC_MR) TIOA0 Output of the Timer Counter Channel 0  */
#define   ADC_MR_TRGSEL_ADC_TRIG2_Val         (2U)                                           /**< (ADC_MR) TIOA1 Output of the Timer Counter Channel 1  */
#define   ADC_MR_TRGSEL_ADC_TRIG3_Val         (3U)                                           /**< (ADC_MR) TIOA2 Output of the Timer Counter Channel 2  */
#define   ADC_MR_TRGSEL_ADC_TRIG4_Val         (4U)                                           /**< (ADC_MR) RTCOUT0  */
#define   ADC_MR_TRGSEL_ADC_TRIG5_Val         (5U)                                           /**< (ADC_MR) RTT 16-Bit prescaler output  */
#define   ADC_MR_TRGSEL_ADC_TRIG6_Val         (6U)                                           /**< (ADC_MR) RTTEVENT  */
#define   ADC_MR_TRGSEL_ADC_TRIG7_Val         (7U)                                           /**< (ADC_MR) -  */
#define ADC_MR_TRGSEL_ADC_TRIG0               (ADC_MR_TRGSEL_ADC_TRIG0_Val << ADC_MR_TRGSEL_Pos) /**< (ADC_MR) ADTRG External trigger Position  */
#define ADC_MR_TRGSEL_ADC_TRIG1               (ADC_MR_TRGSEL_ADC_TRIG1_Val << ADC_MR_TRGSEL_Pos) /**< (ADC_MR) TIOA0 Output of the Timer Counter Channel 0 Position  */
#define ADC_MR_TRGSEL_ADC_TRIG2               (ADC_MR_TRGSEL_ADC_TRIG2_Val << ADC_MR_TRGSEL_Pos) /**< (ADC_MR) TIOA1 Output of the Timer Counter Channel 1 Position  */
#define ADC_MR_TRGSEL_ADC_TRIG3               (ADC_MR_TRGSEL_ADC_TRIG3_Val << ADC_MR_TRGSEL_Pos) /**< (ADC_MR) TIOA2 Output of the Timer Counter Channel 2 Position  */
#define ADC_MR_TRGSEL_ADC_TRIG4               (ADC_MR_TRGSEL_ADC_TRIG4_Val << ADC_MR_TRGSEL_Pos) /**< (ADC_MR) RTCOUT0 Position  */
#define ADC_MR_TRGSEL_ADC_TRIG5               (ADC_MR_TRGSEL_ADC_TRIG5_Val << ADC_MR_TRGSEL_Pos) /**< (ADC_MR) RTT 16-Bit prescaler output Position  */
#define ADC_MR_TRGSEL_ADC_TRIG6               (ADC_MR_TRGSEL_ADC_TRIG6_Val << ADC_MR_TRGSEL_Pos) /**< (ADC_MR) RTTEVENT Position  */
#define ADC_MR_TRGSEL_ADC_TRIG7               (ADC_MR_TRGSEL_ADC_TRIG7_Val << ADC_MR_TRGSEL_Pos) /**< (ADC_MR) - Position  */
#define ADC_MR_SLEEP_Pos                      (5U)                                           /**< (ADC_MR) Sleep Mode Position */
#define ADC_MR_SLEEP_Msk                      (0x1U << ADC_MR_SLEEP_Pos)                     /**< (ADC_MR) Sleep Mode Mask */
#define ADC_MR_SLEEP(value)                   (ADC_MR_SLEEP_Msk & ((value) << ADC_MR_SLEEP_Pos))
#define   ADC_MR_SLEEP_NORMAL_Val             (0U)                                           /**< (ADC_MR) Normal Mode: The ADC core and reference voltage circuitry are kept ON between conversions.  */
#define   ADC_MR_SLEEP_SLEEP_Val              (1U)                                           /**< (ADC_MR) Sleep Mode: The wake-up time can be modified by programming FWUP bit.  */
#define ADC_MR_SLEEP_NORMAL                   (ADC_MR_SLEEP_NORMAL_Val << ADC_MR_SLEEP_Pos)  /**< (ADC_MR) Normal Mode: The ADC core and reference voltage circuitry are kept ON between conversions. Position  */
#define ADC_MR_SLEEP_SLEEP                    (ADC_MR_SLEEP_SLEEP_Val << ADC_MR_SLEEP_Pos)   /**< (ADC_MR) Sleep Mode: The wake-up time can be modified by programming FWUP bit. Position  */
#define ADC_MR_FWUP_Pos                       (6U)                                           /**< (ADC_MR) Fast Wake Up Position */
#define ADC_MR_FWUP_Msk                       (0x1U << ADC_MR_FWUP_Pos)                      /**< (ADC_MR) Fast Wake Up Mask */
#define ADC_MR_FWUP(value)                    (ADC_MR_FWUP_Msk & ((value) << ADC_MR_FWUP_Pos))
#define   ADC_MR_FWUP_OFF_Val                 (0U)                                           /**< (ADC_MR) If SLEEP is 1, then both ADC core and reference voltage circuitry are OFF between conversions  */
#define   ADC_MR_FWUP_ON_Val                  (1U)                                           /**< (ADC_MR) If SLEEP is 1, then Fast Wake-up Sleep mode: The voltage reference is ON between conversions and ADC core is OFF  */
#define ADC_MR_FWUP_OFF                       (ADC_MR_FWUP_OFF_Val << ADC_MR_FWUP_Pos)       /**< (ADC_MR) If SLEEP is 1, then both ADC core and reference voltage circuitry are OFF between conversions Position  */
#define ADC_MR_FWUP_ON                        (ADC_MR_FWUP_ON_Val << ADC_MR_FWUP_Pos)        /**< (ADC_MR) If SLEEP is 1, then Fast Wake-up Sleep mode: The voltage reference is ON between conversions and ADC core is OFF Position  */
#define ADC_MR_FREERUN_Pos                    (7U)                                           /**< (ADC_MR) Free Run Mode Position */
#define ADC_MR_FREERUN_Msk                    (0x1U << ADC_MR_FREERUN_Pos)                   /**< (ADC_MR) Free Run Mode Mask */
#define ADC_MR_FREERUN(value)                 (ADC_MR_FREERUN_Msk & ((value) << ADC_MR_FREERUN_Pos))
#define   ADC_MR_FREERUN_OFF_Val              (0U)                                           /**< (ADC_MR) Normal Mode  */
#define   ADC_MR_FREERUN_ON_Val               (1U)                                           /**< (ADC_MR) Free Run Mode: Never wait for any trigger.  */
#define ADC_MR_FREERUN_OFF                    (ADC_MR_FREERUN_OFF_Val << ADC_MR_FREERUN_Pos) /**< (ADC_MR) Normal Mode Position  */
#define ADC_MR_FREERUN_ON                     (ADC_MR_FREERUN_ON_Val << ADC_MR_FREERUN_Pos)  /**< (ADC_MR) Free Run Mode: Never wait for any trigger. Position  */
#define ADC_MR_PRESCAL_Pos                    (8U)                                           /**< (ADC_MR) Prescaler Rate Selection Position */
#define ADC_MR_PRESCAL_Msk                    (0xFFU << ADC_MR_PRESCAL_Pos)                  /**< (ADC_MR) Prescaler Rate Selection Mask */
#define ADC_MR_PRESCAL(value)                 (ADC_MR_PRESCAL_Msk & ((value) << ADC_MR_PRESCAL_Pos))
#define ADC_MR_STARTUP_Pos                    (16U)                                          /**< (ADC_MR) Start Up Time Position */
#define ADC_MR_STARTUP_Msk                    (0xFU << ADC_MR_STARTUP_Pos)                   /**< (ADC_MR) Start Up Time Mask */
#define ADC_MR_STARTUP(value)                 (ADC_MR_STARTUP_Msk & ((value) << ADC_MR_STARTUP_Pos))
#define   ADC_MR_STARTUP_SUT0_Val             (0U)                                           /**< (ADC_MR) 0 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT8_Val             (1U)                                           /**< (ADC_MR) 8 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT16_Val            (2U)                                           /**< (ADC_MR) 16 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT24_Val            (3U)                                           /**< (ADC_MR) 24 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT64_Val            (4U)                                           /**< (ADC_MR) 64 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT80_Val            (5U)                                           /**< (ADC_MR) 80 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT96_Val            (6U)                                           /**< (ADC_MR) 96 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT112_Val           (7U)                                           /**< (ADC_MR) 112 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT512_Val           (8U)                                           /**< (ADC_MR) 512 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT576_Val           (9U)                                           /**< (ADC_MR) 576 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT640_Val           (10U)                                          /**< (ADC_MR) 640 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT704_Val           (11U)                                          /**< (ADC_MR) 704 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT768_Val           (12U)                                          /**< (ADC_MR) 768 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT832_Val           (13U)                                          /**< (ADC_MR) 832 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT896_Val           (14U)                                          /**< (ADC_MR) 896 periods of ADCCLK  */
#define   ADC_MR_STARTUP_SUT960_Val           (15U)                                          /**< (ADC_MR) 960 periods of ADCCLK  */
#define ADC_MR_STARTUP_SUT0                   (ADC_MR_STARTUP_SUT0_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 0 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT8                   (ADC_MR_STARTUP_SUT8_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 8 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT16                  (ADC_MR_STARTUP_SUT16_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 16 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT24                  (ADC_MR_STARTUP_SUT24_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 24 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT64                  (ADC_MR_STARTUP_SUT64_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 64 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT80                  (ADC_MR_STARTUP_SUT80_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 80 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT96                  (ADC_MR_STARTUP_SUT96_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 96 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT112                 (ADC_MR_STARTUP_SUT112_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 112 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT512                 (ADC_MR_STARTUP_SUT512_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 512 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT576                 (ADC_MR_STARTUP_SUT576_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 576 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT640                 (ADC_MR_STARTUP_SUT640_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 640 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT704                 (ADC_MR_STARTUP_SUT704_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 704 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT768                 (ADC_MR_STARTUP_SUT768_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 768 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT832                 (ADC_MR_STARTUP_SUT832_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 832 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT896                 (ADC_MR_STARTUP_SUT896_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 896 periods of ADCCLK Position  */
#define ADC_MR_STARTUP_SUT960                 (ADC_MR_STARTUP_SUT960_Val << ADC_MR_STARTUP_Pos) /**< (ADC_MR) 960 periods of ADCCLK Position  */
#define ADC_MR_SETTLING_Pos                   (20U)                                          /**< (ADC_MR) Analog Settling Time Position */
#define ADC_MR_SETTLING_Msk                   (0x3U << ADC_MR_SETTLING_Pos)                  /**< (ADC_MR) Analog Settling Time Mask */
#define ADC_MR_SETTLING(value)                (ADC_MR_SETTLING_Msk & ((value) << ADC_MR_SETTLING_Pos))
#define   ADC_MR_SETTLING_AST3_Val            (0U)                                           /**< (ADC_MR) 3 periods of ADCCLK  */
#define   ADC_MR_SETTLING_AST5_Val            (1U)                                           /**< (ADC_MR) 5 periods of ADCCLK  */
#define   ADC_MR_SETTLING_AST9_Val            (2U)                                           /**< (ADC_MR) 9 periods of ADCCLK  */
#define   ADC_MR_SETTLING_AST17_Val           (3U)                                           /**< (ADC_MR) 17 periods of ADCCLK  */
#define ADC_MR_SETTLING_AST3                  (ADC_MR_SETTLING_AST3_Val << ADC_MR_SETTLING_Pos) /**< (ADC_MR) 3 periods of ADCCLK Position  */
#define ADC_MR_SETTLING_AST5                  (ADC_MR_SETTLING_AST5_Val << ADC_MR_SETTLING_Pos) /**< (ADC_MR) 5 periods of ADCCLK Position  */
#define ADC_MR_SETTLING_AST9                  (ADC_MR_SETTLING_AST9_Val << ADC_MR_SETTLING_Pos) /**< (ADC_MR) 9 periods of ADCCLK Position  */
#define ADC_MR_SETTLING_AST17                 (ADC_MR_SETTLING_AST17_Val << ADC_MR_SETTLING_Pos) /**< (ADC_MR) 17 periods of ADCCLK Position  */
#define ADC_MR_ANACH_Pos                      (23U)                                          /**< (ADC_MR) Analog Change Position */
#define ADC_MR_ANACH_Msk                      (0x1U << ADC_MR_ANACH_Pos)                     /**< (ADC_MR) Analog Change Mask */
#define ADC_MR_ANACH(value)                   (ADC_MR_ANACH_Msk & ((value) << ADC_MR_ANACH_Pos))
#define   ADC_MR_ANACH_NONE_Val               (0U)                                           /**< (ADC_MR) No analog change on channel switching: DIFF0, and OFF0 are used for all channels.  */
#define   ADC_MR_ANACH_ALLOWED_Val            (1U)                                           /**< (ADC_MR) Allows different analog settings for each channel. See ADC_COR registers.  */
#define ADC_MR_ANACH_NONE                     (ADC_MR_ANACH_NONE_Val << ADC_MR_ANACH_Pos)    /**< (ADC_MR) No analog change on channel switching: DIFF0, and OFF0 are used for all channels. Position  */
#define ADC_MR_ANACH_ALLOWED                  (ADC_MR_ANACH_ALLOWED_Val << ADC_MR_ANACH_Pos) /**< (ADC_MR) Allows different analog settings for each channel. See ADC_COR registers. Position  */
#define ADC_MR_TRACKTIM_Pos                   (24U)                                          /**< (ADC_MR) Tracking Time Position */
#define ADC_MR_TRACKTIM_Msk                   (0xFU << ADC_MR_TRACKTIM_Pos)                  /**< (ADC_MR) Tracking Time Mask */
#define ADC_MR_TRACKTIM(value)                (ADC_MR_TRACKTIM_Msk & ((value) << ADC_MR_TRACKTIM_Pos))
#define ADC_MR_TRANSFER_Pos                   (28U)                                          /**< (ADC_MR) Transfer Period Position */
#define ADC_MR_TRANSFER_Msk                   (0x3U << ADC_MR_TRANSFER_Pos)                  /**< (ADC_MR) Transfer Period Mask */
#define ADC_MR_TRANSFER(value)                (ADC_MR_TRANSFER_Msk & ((value) << ADC_MR_TRANSFER_Pos))
#define ADC_MR_USEQ_Pos                       (31U)                                          /**< (ADC_MR) Use Sequence Enable Position */
#define ADC_MR_USEQ_Msk                       (0x1U << ADC_MR_USEQ_Pos)                      /**< (ADC_MR) Use Sequence Enable Mask */
#define ADC_MR_USEQ(value)                    (ADC_MR_USEQ_Msk & ((value) << ADC_MR_USEQ_Pos))
#define   ADC_MR_USEQ_NUM_ORDER_Val           (0U)                                           /**< (ADC_MR) Normal Mode: The controller converts channels in a simple numeric order depending only on the channel index.  */
#define   ADC_MR_USEQ_REG_ORDER_Val           (1U)                                           /**< (ADC_MR) User Sequence Mode: The sequence respects what is defined in ADC_SEQR1 register and can be used to convert the same channel several times.  */
#define ADC_MR_USEQ_NUM_ORDER                 (ADC_MR_USEQ_NUM_ORDER_Val << ADC_MR_USEQ_Pos) /**< (ADC_MR) Normal Mode: The controller converts channels in a simple numeric order depending only on the channel index. Position  */
#define ADC_MR_USEQ_REG_ORDER                 (ADC_MR_USEQ_REG_ORDER_Val << ADC_MR_USEQ_Pos) /**< (ADC_MR) User Sequence Mode: The sequence respects what is defined in ADC_SEQR1 register and can be used to convert the same channel several times. Position  */
#define ADC_MR_Msk                            (0xBFBFFFEFUL)                                 /**< (ADC_MR) Register Mask  */

/* -------- ADC_SEQR1 : (ADC Offset: 0x08) (R/W 32) Channel Sequence Register 1 -------- */
#define ADC_SEQR1_USCH1_Pos                   (0U)                                           /**< (ADC_SEQR1) User Sequence Number 1 Position */
#define ADC_SEQR1_USCH1_Msk                   (0xFU << ADC_SEQR1_USCH1_Pos)                  /**< (ADC_SEQR1) User Sequence Number 1 Mask */
#define ADC_SEQR1_USCH1(value)                (ADC_SEQR1_USCH1_Msk & ((value) << ADC_SEQR1_USCH1_Pos))
#define ADC_SEQR1_USCH2_Pos                   (4U)                                           /**< (ADC_SEQR1) User Sequence Number 2 Position */
#define ADC_SEQR1_USCH2_Msk                   (0xFU << ADC_SEQR1_USCH2_Pos)                  /**< (ADC_SEQR1) User Sequence Number 2 Mask */
#define ADC_SEQR1_USCH2(value)                (ADC_SEQR1_USCH2_Msk & ((value) << ADC_SEQR1_USCH2_Pos))
#define ADC_SEQR1_USCH3_Pos                   (8U)                                           /**< (ADC_SEQR1) User Sequence Number 3 Position */
#define ADC_SEQR1_USCH3_Msk                   (0xFU << ADC_SEQR1_USCH3_Pos)                  /**< (ADC_SEQR1) User Sequence Number 3 Mask */
#define ADC_SEQR1_USCH3(value)                (ADC_SEQR1_USCH3_Msk & ((value) << ADC_SEQR1_USCH3_Pos))
#define ADC_SEQR1_USCH4_Pos                   (12U)                                          /**< (ADC_SEQR1) User Sequence Number 4 Position */
#define ADC_SEQR1_USCH4_Msk                   (0xFU << ADC_SEQR1_USCH4_Pos)                  /**< (ADC_SEQR1) User Sequence Number 4 Mask */
#define ADC_SEQR1_USCH4(value)                (ADC_SEQR1_USCH4_Msk & ((value) << ADC_SEQR1_USCH4_Pos))
#define ADC_SEQR1_USCH5_Pos                   (16U)                                          /**< (ADC_SEQR1) User Sequence Number 5 Position */
#define ADC_SEQR1_USCH5_Msk                   (0xFU << ADC_SEQR1_USCH5_Pos)                  /**< (ADC_SEQR1) User Sequence Number 5 Mask */
#define ADC_SEQR1_USCH5(value)                (ADC_SEQR1_USCH5_Msk & ((value) << ADC_SEQR1_USCH5_Pos))
#define ADC_SEQR1_USCH6_Pos                   (20U)                                          /**< (ADC_SEQR1) User Sequence Number 6 Position */
#define ADC_SEQR1_USCH6_Msk                   (0xFU << ADC_SEQR1_USCH6_Pos)                  /**< (ADC_SEQR1) User Sequence Number 6 Mask */
#define ADC_SEQR1_USCH6(value)                (ADC_SEQR1_USCH6_Msk & ((value) << ADC_SEQR1_USCH6_Pos))
#define ADC_SEQR1_USCH7_Pos                   (24U)                                          /**< (ADC_SEQR1) User Sequence Number 7 Position */
#define ADC_SEQR1_USCH7_Msk                   (0xFU << ADC_SEQR1_USCH7_Pos)                  /**< (ADC_SEQR1) User Sequence Number 7 Mask */
#define ADC_SEQR1_USCH7(value)                (ADC_SEQR1_USCH7_Msk & ((value) << ADC_SEQR1_USCH7_Pos))
#define ADC_SEQR1_Msk                         (0x0FFFFFFFUL)                                 /**< (ADC_SEQR1) Register Mask  */

/* -------- ADC_CHER : (ADC Offset: 0x10) ( /W 32) Channel Enable Register -------- */
#define ADC_CHER_CH0_Pos                      (0U)                                           /**< (ADC_CHER) Channel 0 Enable Position */
#define ADC_CHER_CH0_Msk                      (0x1U << ADC_CHER_CH0_Pos)                     /**< (ADC_CHER) Channel 0 Enable Mask */
#define ADC_CHER_CH0(value)                   (ADC_CHER_CH0_Msk & ((value) << ADC_CHER_CH0_Pos))
#define ADC_CHER_CH1_Pos                      (1U)                                           /**< (ADC_CHER) Channel 1 Enable Position */
#define ADC_CHER_CH1_Msk                      (0x1U << ADC_CHER_CH1_Pos)                     /**< (ADC_CHER) Channel 1 Enable Mask */
#define ADC_CHER_CH1(value)                   (ADC_CHER_CH1_Msk & ((value) << ADC_CHER_CH1_Pos))
#define ADC_CHER_CH2_Pos                      (2U)                                           /**< (ADC_CHER) Channel 2 Enable Position */
#define ADC_CHER_CH2_Msk                      (0x1U << ADC_CHER_CH2_Pos)                     /**< (ADC_CHER) Channel 2 Enable Mask */
#define ADC_CHER_CH2(value)                   (ADC_CHER_CH2_Msk & ((value) << ADC_CHER_CH2_Pos))
#define ADC_CHER_CH3_Pos                      (3U)                                           /**< (ADC_CHER) Channel 3 Enable Position */
#define ADC_CHER_CH3_Msk                      (0x1U << ADC_CHER_CH3_Pos)                     /**< (ADC_CHER) Channel 3 Enable Mask */
#define ADC_CHER_CH3(value)                   (ADC_CHER_CH3_Msk & ((value) << ADC_CHER_CH3_Pos))
#define ADC_CHER_CH4_Pos                      (4U)                                           /**< (ADC_CHER) Channel 4 Enable Position */
#define ADC_CHER_CH4_Msk                      (0x1U << ADC_CHER_CH4_Pos)                     /**< (ADC_CHER) Channel 4 Enable Mask */
#define ADC_CHER_CH4(value)                   (ADC_CHER_CH4_Msk & ((value) << ADC_CHER_CH4_Pos))
#define ADC_CHER_CH5_Pos                      (5U)                                           /**< (ADC_CHER) Channel 5 Enable Position */
#define ADC_CHER_CH5_Msk                      (0x1U << ADC_CHER_CH5_Pos)                     /**< (ADC_CHER) Channel 5 Enable Mask */
#define ADC_CHER_CH5(value)                   (ADC_CHER_CH5_Msk & ((value) << ADC_CHER_CH5_Pos))
#define ADC_CHER_CH6_Pos                      (6U)                                           /**< (ADC_CHER) Channel 6 Enable Position */
#define ADC_CHER_CH6_Msk                      (0x1U << ADC_CHER_CH6_Pos)                     /**< (ADC_CHER) Channel 6 Enable Mask */
#define ADC_CHER_CH6(value)                   (ADC_CHER_CH6_Msk & ((value) << ADC_CHER_CH6_Pos))
#define ADC_CHER_CH7_Pos                      (7U)                                           /**< (ADC_CHER) Channel 7 Enable Position */
#define ADC_CHER_CH7_Msk                      (0x1U << ADC_CHER_CH7_Pos)                     /**< (ADC_CHER) Channel 7 Enable Mask */
#define ADC_CHER_CH7(value)                   (ADC_CHER_CH7_Msk & ((value) << ADC_CHER_CH7_Pos))
#define ADC_CHER_Msk                          (0x000000FFUL)                                 /**< (ADC_CHER) Register Mask  */

/* -------- ADC_CHDR : (ADC Offset: 0x14) ( /W 32) Channel Disable Register -------- */
#define ADC_CHDR_CH0_Pos                      (0U)                                           /**< (ADC_CHDR) Channel 0 Disable Position */
#define ADC_CHDR_CH0_Msk                      (0x1U << ADC_CHDR_CH0_Pos)                     /**< (ADC_CHDR) Channel 0 Disable Mask */
#define ADC_CHDR_CH0(value)                   (ADC_CHDR_CH0_Msk & ((value) << ADC_CHDR_CH0_Pos))
#define ADC_CHDR_CH1_Pos                      (1U)                                           /**< (ADC_CHDR) Channel 1 Disable Position */
#define ADC_CHDR_CH1_Msk                      (0x1U << ADC_CHDR_CH1_Pos)                     /**< (ADC_CHDR) Channel 1 Disable Mask */
#define ADC_CHDR_CH1(value)                   (ADC_CHDR_CH1_Msk & ((value) << ADC_CHDR_CH1_Pos))
#define ADC_CHDR_CH2_Pos                      (2U)                                           /**< (ADC_CHDR) Channel 2 Disable Position */
#define ADC_CHDR_CH2_Msk                      (0x1U << ADC_CHDR_CH2_Pos)                     /**< (ADC_CHDR) Channel 2 Disable Mask */
#define ADC_CHDR_CH2(value)                   (ADC_CHDR_CH2_Msk & ((value) << ADC_CHDR_CH2_Pos))
#define ADC_CHDR_CH3_Pos                      (3U)                                           /**< (ADC_CHDR) Channel 3 Disable Position */
#define ADC_CHDR_CH3_Msk                      (0x1U << ADC_CHDR_CH3_Pos)                     /**< (ADC_CHDR) Channel 3 Disable Mask */
#define ADC_CHDR_CH3(value)                   (ADC_CHDR_CH3_Msk & ((value) << ADC_CHDR_CH3_Pos))
#define ADC_CHDR_CH4_Pos                      (4U)                                           /**< (ADC_CHDR) Channel 4 Disable Position */
#define ADC_CHDR_CH4_Msk                      (0x1U << ADC_CHDR_CH4_Pos)                     /**< (ADC_CHDR) Channel 4 Disable Mask */
#define ADC_CHDR_CH4(value)                   (ADC_CHDR_CH4_Msk & ((value) << ADC_CHDR_CH4_Pos))
#define ADC_CHDR_CH5_Pos                      (5U)                                           /**< (ADC_CHDR) Channel 5 Disable Position */
#define ADC_CHDR_CH5_Msk                      (0x1U << ADC_CHDR_CH5_Pos)                     /**< (ADC_CHDR) Channel 5 Disable Mask */
#define ADC_CHDR_CH5(value)                   (ADC_CHDR_CH5_Msk & ((value) << ADC_CHDR_CH5_Pos))
#define ADC_CHDR_CH6_Pos                      (6U)                                           /**< (ADC_CHDR) Channel 6 Disable Position */
#define ADC_CHDR_CH6_Msk                      (0x1U << ADC_CHDR_CH6_Pos)                     /**< (ADC_CHDR) Channel 6 Disable Mask */
#define ADC_CHDR_CH6(value)                   (ADC_CHDR_CH6_Msk & ((value) << ADC_CHDR_CH6_Pos))
#define ADC_CHDR_CH7_Pos                      (7U)                                           /**< (ADC_CHDR) Channel 7 Disable Position */
#define ADC_CHDR_CH7_Msk                      (0x1U << ADC_CHDR_CH7_Pos)                     /**< (ADC_CHDR) Channel 7 Disable Mask */
#define ADC_CHDR_CH7(value)                   (ADC_CHDR_CH7_Msk & ((value) << ADC_CHDR_CH7_Pos))
#define ADC_CHDR_Msk                          (0x000000FFUL)                                 /**< (ADC_CHDR) Register Mask  */

/* -------- ADC_CHSR : (ADC Offset: 0x18) (R/  32) Channel Status Register -------- */
#define ADC_CHSR_CH0_Pos                      (0U)                                           /**< (ADC_CHSR) Channel 0 Status Position */
#define ADC_CHSR_CH0_Msk                      (0x1U << ADC_CHSR_CH0_Pos)                     /**< (ADC_CHSR) Channel 0 Status Mask */
#define ADC_CHSR_CH0(value)                   (ADC_CHSR_CH0_Msk & ((value) << ADC_CHSR_CH0_Pos))
#define ADC_CHSR_CH1_Pos                      (1U)                                           /**< (ADC_CHSR) Channel 1 Status Position */
#define ADC_CHSR_CH1_Msk                      (0x1U << ADC_CHSR_CH1_Pos)                     /**< (ADC_CHSR) Channel 1 Status Mask */
#define ADC_CHSR_CH1(value)                   (ADC_CHSR_CH1_Msk & ((value) << ADC_CHSR_CH1_Pos))
#define ADC_CHSR_CH2_Pos                      (2U)                                           /**< (ADC_CHSR) Channel 2 Status Position */
#define ADC_CHSR_CH2_Msk                      (0x1U << ADC_CHSR_CH2_Pos)                     /**< (ADC_CHSR) Channel 2 Status Mask */
#define ADC_CHSR_CH2(value)                   (ADC_CHSR_CH2_Msk & ((value) << ADC_CHSR_CH2_Pos))
#define ADC_CHSR_CH3_Pos                      (3U)                                           /**< (ADC_CHSR) Channel 3 Status Position */
#define ADC_CHSR_CH3_Msk                      (0x1U << ADC_CHSR_CH3_Pos)                     /**< (ADC_CHSR) Channel 3 Status Mask */
#define ADC_CHSR_CH3(value)                   (ADC_CHSR_CH3_Msk & ((value) << ADC_CHSR_CH3_Pos))
#define ADC_CHSR_CH4_Pos                      (4U)                                           /**< (ADC_CHSR) Channel 4 Status Position */
#define ADC_CHSR_CH4_Msk                      (0x1U << ADC_CHSR_CH4_Pos)                     /**< (ADC_CHSR) Channel 4 Status Mask */
#define ADC_CHSR_CH4(value)                   (ADC_CHSR_CH4_Msk & ((value) << ADC_CHSR_CH4_Pos))
#define ADC_CHSR_CH5_Pos                      (5U)                                           /**< (ADC_CHSR) Channel 5 Status Position */
#define ADC_CHSR_CH5_Msk                      (0x1U << ADC_CHSR_CH5_Pos)                     /**< (ADC_CHSR) Channel 5 Status Mask */
#define ADC_CHSR_CH5(value)                   (ADC_CHSR_CH5_Msk & ((value) << ADC_CHSR_CH5_Pos))
#define ADC_CHSR_CH6_Pos                      (6U)                                           /**< (ADC_CHSR) Channel 6 Status Position */
#define ADC_CHSR_CH6_Msk                      (0x1U << ADC_CHSR_CH6_Pos)                     /**< (ADC_CHSR) Channel 6 Status Mask */
#define ADC_CHSR_CH6(value)                   (ADC_CHSR_CH6_Msk & ((value) << ADC_CHSR_CH6_Pos))
#define ADC_CHSR_CH7_Pos                      (7U)                                           /**< (ADC_CHSR) Channel 7 Status Position */
#define ADC_CHSR_CH7_Msk                      (0x1U << ADC_CHSR_CH7_Pos)                     /**< (ADC_CHSR) Channel 7 Status Mask */
#define ADC_CHSR_CH7(value)                   (ADC_CHSR_CH7_Msk & ((value) << ADC_CHSR_CH7_Pos))
#define ADC_CHSR_Msk                          (0x000000FFUL)                                 /**< (ADC_CHSR) Register Mask  */

/* -------- ADC_LCDR : (ADC Offset: 0x20) (R/  32) Last Converted Data Register -------- */
#define ADC_LCDR_LDATA_Pos                    (0U)                                           /**< (ADC_LCDR) Last Data Converted Position */
#define ADC_LCDR_LDATA_Msk                    (0xFFFFU << ADC_LCDR_LDATA_Pos)                /**< (ADC_LCDR) Last Data Converted Mask */
#define ADC_LCDR_LDATA(value)                 (ADC_LCDR_LDATA_Msk & ((value) << ADC_LCDR_LDATA_Pos))
#define ADC_LCDR_CHNBOSR_Pos                  (24U)                                          /**< (ADC_LCDR) Channel Number in Oversampling Mode Position */
#define ADC_LCDR_CHNBOSR_Msk                  (0x1FU << ADC_LCDR_CHNBOSR_Pos)                /**< (ADC_LCDR) Channel Number in Oversampling Mode Mask */
#define ADC_LCDR_CHNBOSR(value)               (ADC_LCDR_CHNBOSR_Msk & ((value) << ADC_LCDR_CHNBOSR_Pos))
#define ADC_LCDR_Msk                          (0x1F00FFFFUL)                                 /**< (ADC_LCDR) Register Mask  */

/* -------- ADC_IER : (ADC Offset: 0x24) ( /W 32) Interrupt Enable Register -------- */
#define ADC_IER_EOC0_Pos                      (0U)                                           /**< (ADC_IER) End of Conversion Interrupt Enable 0 Position */
#define ADC_IER_EOC0_Msk                      (0x1U << ADC_IER_EOC0_Pos)                     /**< (ADC_IER) End of Conversion Interrupt Enable 0 Mask */
#define ADC_IER_EOC0(value)                   (ADC_IER_EOC0_Msk & ((value) << ADC_IER_EOC0_Pos))
#define ADC_IER_EOC1_Pos                      (1U)                                           /**< (ADC_IER) End of Conversion Interrupt Enable 1 Position */
#define ADC_IER_EOC1_Msk                      (0x1U << ADC_IER_EOC1_Pos)                     /**< (ADC_IER) End of Conversion Interrupt Enable 1 Mask */
#define ADC_IER_EOC1(value)                   (ADC_IER_EOC1_Msk & ((value) << ADC_IER_EOC1_Pos))
#define ADC_IER_EOC2_Pos                      (2U)                                           /**< (ADC_IER) End of Conversion Interrupt Enable 2 Position */
#define ADC_IER_EOC2_Msk                      (0x1U << ADC_IER_EOC2_Pos)                     /**< (ADC_IER) End of Conversion Interrupt Enable 2 Mask */
#define ADC_IER_EOC2(value)                   (ADC_IER_EOC2_Msk & ((value) << ADC_IER_EOC2_Pos))
#define ADC_IER_EOC3_Pos                      (3U)                                           /**< (ADC_IER) End of Conversion Interrupt Enable 3 Position */
#define ADC_IER_EOC3_Msk                      (0x1U << ADC_IER_EOC3_Pos)                     /**< (ADC_IER) End of Conversion Interrupt Enable 3 Mask */
#define ADC_IER_EOC3(value)                   (ADC_IER_EOC3_Msk & ((value) << ADC_IER_EOC3_Pos))
#define ADC_IER_EOC4_Pos                      (4U)                                           /**< (ADC_IER) End of Conversion Interrupt Enable 4 Position */
#define ADC_IER_EOC4_Msk                      (0x1U << ADC_IER_EOC4_Pos)                     /**< (ADC_IER) End of Conversion Interrupt Enable 4 Mask */
#define ADC_IER_EOC4(value)                   (ADC_IER_EOC4_Msk & ((value) << ADC_IER_EOC4_Pos))
#define ADC_IER_EOC5_Pos                      (5U)                                           /**< (ADC_IER) End of Conversion Interrupt Enable 5 Position */
#define ADC_IER_EOC5_Msk                      (0x1U << ADC_IER_EOC5_Pos)                     /**< (ADC_IER) End of Conversion Interrupt Enable 5 Mask */
#define ADC_IER_EOC5(value)                   (ADC_IER_EOC5_Msk & ((value) << ADC_IER_EOC5_Pos))
#define ADC_IER_EOC6_Pos                      (6U)                                           /**< (ADC_IER) End of Conversion Interrupt Enable 6 Position */
#define ADC_IER_EOC6_Msk                      (0x1U << ADC_IER_EOC6_Pos)                     /**< (ADC_IER) End of Conversion Interrupt Enable 6 Mask */
#define ADC_IER_EOC6(value)                   (ADC_IER_EOC6_Msk & ((value) << ADC_IER_EOC6_Pos))
#define ADC_IER_EOC7_Pos                      (7U)                                           /**< (ADC_IER) End of Conversion Interrupt Enable 7 Position */
#define ADC_IER_EOC7_Msk                      (0x1U << ADC_IER_EOC7_Pos)                     /**< (ADC_IER) End of Conversion Interrupt Enable 7 Mask */
#define ADC_IER_EOC7(value)                   (ADC_IER_EOC7_Msk & ((value) << ADC_IER_EOC7_Pos))
#define ADC_IER_LCCHG_Pos                     (19U)                                          /**< (ADC_IER) Last Channel Change Interrupt Enable Position */
#define ADC_IER_LCCHG_Msk                     (0x1U << ADC_IER_LCCHG_Pos)                    /**< (ADC_IER) Last Channel Change Interrupt Enable Mask */
#define ADC_IER_LCCHG(value)                  (ADC_IER_LCCHG_Msk & ((value) << ADC_IER_LCCHG_Pos))
#define ADC_IER_DRDY_Pos                      (24U)                                          /**< (ADC_IER) Data Ready Interrupt Enable Position */
#define ADC_IER_DRDY_Msk                      (0x1U << ADC_IER_DRDY_Pos)                     /**< (ADC_IER) Data Ready Interrupt Enable Mask */
#define ADC_IER_DRDY(value)                   (ADC_IER_DRDY_Msk & ((value) << ADC_IER_DRDY_Pos))
#define ADC_IER_GOVRE_Pos                     (25U)                                          /**< (ADC_IER) General Overrun Error Interrupt Enable Position */
#define ADC_IER_GOVRE_Msk                     (0x1U << ADC_IER_GOVRE_Pos)                    /**< (ADC_IER) General Overrun Error Interrupt Enable Mask */
#define ADC_IER_GOVRE(value)                  (ADC_IER_GOVRE_Msk & ((value) << ADC_IER_GOVRE_Pos))
#define ADC_IER_COMPE_Pos                     (26U)                                          /**< (ADC_IER) Comparison Event Interrupt Enable Position */
#define ADC_IER_COMPE_Msk                     (0x1U << ADC_IER_COMPE_Pos)                    /**< (ADC_IER) Comparison Event Interrupt Enable Mask */
#define ADC_IER_COMPE(value)                  (ADC_IER_COMPE_Msk & ((value) << ADC_IER_COMPE_Pos))
#define ADC_IER_ENDRX_Pos                     (27U)                                          /**< (ADC_IER) End of Receive Buffer Interrupt Enable Position */
#define ADC_IER_ENDRX_Msk                     (0x1U << ADC_IER_ENDRX_Pos)                    /**< (ADC_IER) End of Receive Buffer Interrupt Enable Mask */
#define ADC_IER_ENDRX(value)                  (ADC_IER_ENDRX_Msk & ((value) << ADC_IER_ENDRX_Pos))
#define ADC_IER_RXBUFF_Pos                    (28U)                                          /**< (ADC_IER) Receive Buffer Full Interrupt Enable Position */
#define ADC_IER_RXBUFF_Msk                    (0x1U << ADC_IER_RXBUFF_Pos)                   /**< (ADC_IER) Receive Buffer Full Interrupt Enable Mask */
#define ADC_IER_RXBUFF(value)                 (ADC_IER_RXBUFF_Msk & ((value) << ADC_IER_RXBUFF_Pos))
#define ADC_IER_Msk                           (0x1F0800FFUL)                                 /**< (ADC_IER) Register Mask  */

/* -------- ADC_IDR : (ADC Offset: 0x28) ( /W 32) Interrupt Disable Register -------- */
#define ADC_IDR_EOC0_Pos                      (0U)                                           /**< (ADC_IDR) End of Conversion Interrupt Disable 0 Position */
#define ADC_IDR_EOC0_Msk                      (0x1U << ADC_IDR_EOC0_Pos)                     /**< (ADC_IDR) End of Conversion Interrupt Disable 0 Mask */
#define ADC_IDR_EOC0(value)                   (ADC_IDR_EOC0_Msk & ((value) << ADC_IDR_EOC0_Pos))
#define ADC_IDR_EOC1_Pos                      (1U)                                           /**< (ADC_IDR) End of Conversion Interrupt Disable 1 Position */
#define ADC_IDR_EOC1_Msk                      (0x1U << ADC_IDR_EOC1_Pos)                     /**< (ADC_IDR) End of Conversion Interrupt Disable 1 Mask */
#define ADC_IDR_EOC1(value)                   (ADC_IDR_EOC1_Msk & ((value) << ADC_IDR_EOC1_Pos))
#define ADC_IDR_EOC2_Pos                      (2U)                                           /**< (ADC_IDR) End of Conversion Interrupt Disable 2 Position */
#define ADC_IDR_EOC2_Msk                      (0x1U << ADC_IDR_EOC2_Pos)                     /**< (ADC_IDR) End of Conversion Interrupt Disable 2 Mask */
#define ADC_IDR_EOC2(value)                   (ADC_IDR_EOC2_Msk & ((value) << ADC_IDR_EOC2_Pos))
#define ADC_IDR_EOC3_Pos                      (3U)                                           /**< (ADC_IDR) End of Conversion Interrupt Disable 3 Position */
#define ADC_IDR_EOC3_Msk                      (0x1U << ADC_IDR_EOC3_Pos)                     /**< (ADC_IDR) End of Conversion Interrupt Disable 3 Mask */
#define ADC_IDR_EOC3(value)                   (ADC_IDR_EOC3_Msk & ((value) << ADC_IDR_EOC3_Pos))
#define ADC_IDR_EOC4_Pos                      (4U)                                           /**< (ADC_IDR) End of Conversion Interrupt Disable 4 Position */
#define ADC_IDR_EOC4_Msk                      (0x1U << ADC_IDR_EOC4_Pos)                     /**< (ADC_IDR) End of Conversion Interrupt Disable 4 Mask */
#define ADC_IDR_EOC4(value)                   (ADC_IDR_EOC4_Msk & ((value) << ADC_IDR_EOC4_Pos))
#define ADC_IDR_EOC5_Pos                      (5U)                                           /**< (ADC_IDR) End of Conversion Interrupt Disable 5 Position */
#define ADC_IDR_EOC5_Msk                      (0x1U << ADC_IDR_EOC5_Pos)                     /**< (ADC_IDR) End of Conversion Interrupt Disable 5 Mask */
#define ADC_IDR_EOC5(value)                   (ADC_IDR_EOC5_Msk & ((value) << ADC_IDR_EOC5_Pos))
#define ADC_IDR_EOC6_Pos                      (6U)                                           /**< (ADC_IDR) End of Conversion Interrupt Disable 6 Position */
#define ADC_IDR_EOC6_Msk                      (0x1U << ADC_IDR_EOC6_Pos)                     /**< (ADC_IDR) End of Conversion Interrupt Disable 6 Mask */
#define ADC_IDR_EOC6(value)                   (ADC_IDR_EOC6_Msk & ((value) << ADC_IDR_EOC6_Pos))
#define ADC_IDR_EOC7_Pos                      (7U)                                           /**< (ADC_IDR) End of Conversion Interrupt Disable 7 Position */
#define ADC_IDR_EOC7_Msk                      (0x1U << ADC_IDR_EOC7_Pos)                     /**< (ADC_IDR) End of Conversion Interrupt Disable 7 Mask */
#define ADC_IDR_EOC7(value)                   (ADC_IDR_EOC7_Msk & ((value) << ADC_IDR_EOC7_Pos))
#define ADC_IDR_LCCHG_Pos                     (19U)                                          /**< (ADC_IDR) Last Channel Change Interrupt Disable Position */
#define ADC_IDR_LCCHG_Msk                     (0x1U << ADC_IDR_LCCHG_Pos)                    /**< (ADC_IDR) Last Channel Change Interrupt Disable Mask */
#define ADC_IDR_LCCHG(value)                  (ADC_IDR_LCCHG_Msk & ((value) << ADC_IDR_LCCHG_Pos))
#define ADC_IDR_DRDY_Pos                      (24U)                                          /**< (ADC_IDR) Data Ready Interrupt Disable Position */
#define ADC_IDR_DRDY_Msk                      (0x1U << ADC_IDR_DRDY_Pos)                     /**< (ADC_IDR) Data Ready Interrupt Disable Mask */
#define ADC_IDR_DRDY(value)                   (ADC_IDR_DRDY_Msk & ((value) << ADC_IDR_DRDY_Pos))
#define ADC_IDR_GOVRE_Pos                     (25U)                                          /**< (ADC_IDR) General Overrun Error Interrupt Disable Position */
#define ADC_IDR_GOVRE_Msk                     (0x1U << ADC_IDR_GOVRE_Pos)                    /**< (ADC_IDR) General Overrun Error Interrupt Disable Mask */
#define ADC_IDR_GOVRE(value)                  (ADC_IDR_GOVRE_Msk & ((value) << ADC_IDR_GOVRE_Pos))
#define ADC_IDR_COMPE_Pos                     (26U)                                          /**< (ADC_IDR) Comparison Event Interrupt Disable Position */
#define ADC_IDR_COMPE_Msk                     (0x1U << ADC_IDR_COMPE_Pos)                    /**< (ADC_IDR) Comparison Event Interrupt Disable Mask */
#define ADC_IDR_COMPE(value)                  (ADC_IDR_COMPE_Msk & ((value) << ADC_IDR_COMPE_Pos))
#define ADC_IDR_ENDRX_Pos                     (27U)                                          /**< (ADC_IDR) End of Receive Buffer Interrupt Disable Position */
#define ADC_IDR_ENDRX_Msk                     (0x1U << ADC_IDR_ENDRX_Pos)                    /**< (ADC_IDR) End of Receive Buffer Interrupt Disable Mask */
#define ADC_IDR_ENDRX(value)                  (ADC_IDR_ENDRX_Msk & ((value) << ADC_IDR_ENDRX_Pos))
#define ADC_IDR_RXBUFF_Pos                    (28U)                                          /**< (ADC_IDR) Receive Buffer Full Interrupt Disable Position */
#define ADC_IDR_RXBUFF_Msk                    (0x1U << ADC_IDR_RXBUFF_Pos)                   /**< (ADC_IDR) Receive Buffer Full Interrupt Disable Mask */
#define ADC_IDR_RXBUFF(value)                 (ADC_IDR_RXBUFF_Msk & ((value) << ADC_IDR_RXBUFF_Pos))
#define ADC_IDR_Msk                           (0x1F0800FFUL)                                 /**< (ADC_IDR) Register Mask  */

/* -------- ADC_IMR : (ADC Offset: 0x2C) (R/  32) Interrupt Mask Register -------- */
#define ADC_IMR_EOC0_Pos                      (0U)                                           /**< (ADC_IMR) End of Conversion Interrupt Mask 0 Position */
#define ADC_IMR_EOC0_Msk                      (0x1U << ADC_IMR_EOC0_Pos)                     /**< (ADC_IMR) End of Conversion Interrupt Mask 0 Mask */
#define ADC_IMR_EOC0(value)                   (ADC_IMR_EOC0_Msk & ((value) << ADC_IMR_EOC0_Pos))
#define ADC_IMR_EOC1_Pos                      (1U)                                           /**< (ADC_IMR) End of Conversion Interrupt Mask 1 Position */
#define ADC_IMR_EOC1_Msk                      (0x1U << ADC_IMR_EOC1_Pos)                     /**< (ADC_IMR) End of Conversion Interrupt Mask 1 Mask */
#define ADC_IMR_EOC1(value)                   (ADC_IMR_EOC1_Msk & ((value) << ADC_IMR_EOC1_Pos))
#define ADC_IMR_EOC2_Pos                      (2U)                                           /**< (ADC_IMR) End of Conversion Interrupt Mask 2 Position */
#define ADC_IMR_EOC2_Msk                      (0x1U << ADC_IMR_EOC2_Pos)                     /**< (ADC_IMR) End of Conversion Interrupt Mask 2 Mask */
#define ADC_IMR_EOC2(value)                   (ADC_IMR_EOC2_Msk & ((value) << ADC_IMR_EOC2_Pos))
#define ADC_IMR_EOC3_Pos                      (3U)                                           /**< (ADC_IMR) End of Conversion Interrupt Mask 3 Position */
#define ADC_IMR_EOC3_Msk                      (0x1U << ADC_IMR_EOC3_Pos)                     /**< (ADC_IMR) End of Conversion Interrupt Mask 3 Mask */
#define ADC_IMR_EOC3(value)                   (ADC_IMR_EOC3_Msk & ((value) << ADC_IMR_EOC3_Pos))
#define ADC_IMR_EOC4_Pos                      (4U)                                           /**< (ADC_IMR) End of Conversion Interrupt Mask 4 Position */
#define ADC_IMR_EOC4_Msk                      (0x1U << ADC_IMR_EOC4_Pos)                     /**< (ADC_IMR) End of Conversion Interrupt Mask 4 Mask */
#define ADC_IMR_EOC4(value)                   (ADC_IMR_EOC4_Msk & ((value) << ADC_IMR_EOC4_Pos))
#define ADC_IMR_EOC5_Pos                      (5U)                                           /**< (ADC_IMR) End of Conversion Interrupt Mask 5 Position */
#define ADC_IMR_EOC5_Msk                      (0x1U << ADC_IMR_EOC5_Pos)                     /**< (ADC_IMR) End of Conversion Interrupt Mask 5 Mask */
#define ADC_IMR_EOC5(value)                   (ADC_IMR_EOC5_Msk & ((value) << ADC_IMR_EOC5_Pos))
#define ADC_IMR_EOC6_Pos                      (6U)                                           /**< (ADC_IMR) End of Conversion Interrupt Mask 6 Position */
#define ADC_IMR_EOC6_Msk                      (0x1U << ADC_IMR_EOC6_Pos)                     /**< (ADC_IMR) End of Conversion Interrupt Mask 6 Mask */
#define ADC_IMR_EOC6(value)                   (ADC_IMR_EOC6_Msk & ((value) << ADC_IMR_EOC6_Pos))
#define ADC_IMR_EOC7_Pos                      (7U)                                           /**< (ADC_IMR) End of Conversion Interrupt Mask 7 Position */
#define ADC_IMR_EOC7_Msk                      (0x1U << ADC_IMR_EOC7_Pos)                     /**< (ADC_IMR) End of Conversion Interrupt Mask 7 Mask */
#define ADC_IMR_EOC7(value)                   (ADC_IMR_EOC7_Msk & ((value) << ADC_IMR_EOC7_Pos))
#define ADC_IMR_LCCHG_Pos                     (19U)                                          /**< (ADC_IMR) Last Channel Change Interrupt Mask Position */
#define ADC_IMR_LCCHG_Msk                     (0x1U << ADC_IMR_LCCHG_Pos)                    /**< (ADC_IMR) Last Channel Change Interrupt Mask Mask */
#define ADC_IMR_LCCHG(value)                  (ADC_IMR_LCCHG_Msk & ((value) << ADC_IMR_LCCHG_Pos))
#define ADC_IMR_DRDY_Pos                      (24U)                                          /**< (ADC_IMR) Data Ready Interrupt Mask Position */
#define ADC_IMR_DRDY_Msk                      (0x1U << ADC_IMR_DRDY_Pos)                     /**< (ADC_IMR) Data Ready Interrupt Mask Mask */
#define ADC_IMR_DRDY(value)                   (ADC_IMR_DRDY_Msk & ((value) << ADC_IMR_DRDY_Pos))
#define ADC_IMR_GOVRE_Pos                     (25U)                                          /**< (ADC_IMR) General Overrun Error Interrupt Mask Position */
#define ADC_IMR_GOVRE_Msk                     (0x1U << ADC_IMR_GOVRE_Pos)                    /**< (ADC_IMR) General Overrun Error Interrupt Mask Mask */
#define ADC_IMR_GOVRE(value)                  (ADC_IMR_GOVRE_Msk & ((value) << ADC_IMR_GOVRE_Pos))
#define ADC_IMR_COMPE_Pos                     (26U)                                          /**< (ADC_IMR) Comparison Event Interrupt Mask Position */
#define ADC_IMR_COMPE_Msk                     (0x1U << ADC_IMR_COMPE_Pos)                    /**< (ADC_IMR) Comparison Event Interrupt Mask Mask */
#define ADC_IMR_COMPE(value)                  (ADC_IMR_COMPE_Msk & ((value) << ADC_IMR_COMPE_Pos))
#define ADC_IMR_ENDRX_Pos                     (27U)                                          /**< (ADC_IMR) End of Receive Buffer Interrupt Mask Position */
#define ADC_IMR_ENDRX_Msk                     (0x1U << ADC_IMR_ENDRX_Pos)                    /**< (ADC_IMR) End of Receive Buffer Interrupt Mask Mask */
#define ADC_IMR_ENDRX(value)                  (ADC_IMR_ENDRX_Msk & ((value) << ADC_IMR_ENDRX_Pos))
#define ADC_IMR_RXBUFF_Pos                    (28U)                                          /**< (ADC_IMR) Receive Buffer Full Interrupt Mask Position */
#define ADC_IMR_RXBUFF_Msk                    (0x1U << ADC_IMR_RXBUFF_Pos)                   /**< (ADC_IMR) Receive Buffer Full Interrupt Mask Mask */
#define ADC_IMR_RXBUFF(value)                 (ADC_IMR_RXBUFF_Msk & ((value) << ADC_IMR_RXBUFF_Pos))
#define ADC_IMR_Msk                           (0x1F0800FFUL)                                 /**< (ADC_IMR) Register Mask  */

/* -------- ADC_ISR : (ADC Offset: 0x30) (R/  32) Interrupt Status Register -------- */
#define ADC_ISR_EOC0_Pos                      (0U)                                           /**< (ADC_ISR) End of Conversion 0 (automatically set / cleared) Position */
#define ADC_ISR_EOC0_Msk                      (0x1U << ADC_ISR_EOC0_Pos)                     /**< (ADC_ISR) End of Conversion 0 (automatically set / cleared) Mask */
#define ADC_ISR_EOC0(value)                   (ADC_ISR_EOC0_Msk & ((value) << ADC_ISR_EOC0_Pos))
#define ADC_ISR_EOC1_Pos                      (1U)                                           /**< (ADC_ISR) End of Conversion 1 (automatically set / cleared) Position */
#define ADC_ISR_EOC1_Msk                      (0x1U << ADC_ISR_EOC1_Pos)                     /**< (ADC_ISR) End of Conversion 1 (automatically set / cleared) Mask */
#define ADC_ISR_EOC1(value)                   (ADC_ISR_EOC1_Msk & ((value) << ADC_ISR_EOC1_Pos))
#define ADC_ISR_EOC2_Pos                      (2U)                                           /**< (ADC_ISR) End of Conversion 2 (automatically set / cleared) Position */
#define ADC_ISR_EOC2_Msk                      (0x1U << ADC_ISR_EOC2_Pos)                     /**< (ADC_ISR) End of Conversion 2 (automatically set / cleared) Mask */
#define ADC_ISR_EOC2(value)                   (ADC_ISR_EOC2_Msk & ((value) << ADC_ISR_EOC2_Pos))
#define ADC_ISR_EOC3_Pos                      (3U)                                           /**< (ADC_ISR) End of Conversion 3 (automatically set / cleared) Position */
#define ADC_ISR_EOC3_Msk                      (0x1U << ADC_ISR_EOC3_Pos)                     /**< (ADC_ISR) End of Conversion 3 (automatically set / cleared) Mask */
#define ADC_ISR_EOC3(value)                   (ADC_ISR_EOC3_Msk & ((value) << ADC_ISR_EOC3_Pos))
#define ADC_ISR_EOC4_Pos                      (4U)                                           /**< (ADC_ISR) End of Conversion 4 (automatically set / cleared) Position */
#define ADC_ISR_EOC4_Msk                      (0x1U << ADC_ISR_EOC4_Pos)                     /**< (ADC_ISR) End of Conversion 4 (automatically set / cleared) Mask */
#define ADC_ISR_EOC4(value)                   (ADC_ISR_EOC4_Msk & ((value) << ADC_ISR_EOC4_Pos))
#define ADC_ISR_EOC5_Pos                      (5U)                                           /**< (ADC_ISR) End of Conversion 5 (automatically set / cleared) Position */
#define ADC_ISR_EOC5_Msk                      (0x1U << ADC_ISR_EOC5_Pos)                     /**< (ADC_ISR) End of Conversion 5 (automatically set / cleared) Mask */
#define ADC_ISR_EOC5(value)                   (ADC_ISR_EOC5_Msk & ((value) << ADC_ISR_EOC5_Pos))
#define ADC_ISR_EOC6_Pos                      (6U)                                           /**< (ADC_ISR) End of Conversion 6 (automatically set / cleared) Position */
#define ADC_ISR_EOC6_Msk                      (0x1U << ADC_ISR_EOC6_Pos)                     /**< (ADC_ISR) End of Conversion 6 (automatically set / cleared) Mask */
#define ADC_ISR_EOC6(value)                   (ADC_ISR_EOC6_Msk & ((value) << ADC_ISR_EOC6_Pos))
#define ADC_ISR_EOC7_Pos                      (7U)                                           /**< (ADC_ISR) End of Conversion 7 (automatically set / cleared) Position */
#define ADC_ISR_EOC7_Msk                      (0x1U << ADC_ISR_EOC7_Pos)                     /**< (ADC_ISR) End of Conversion 7 (automatically set / cleared) Mask */
#define ADC_ISR_EOC7(value)                   (ADC_ISR_EOC7_Msk & ((value) << ADC_ISR_EOC7_Pos))
#define ADC_ISR_LCCHG_Pos                     (19U)                                          /**< (ADC_ISR) Last Channel Change (cleared on read) Position */
#define ADC_ISR_LCCHG_Msk                     (0x1U << ADC_ISR_LCCHG_Pos)                    /**< (ADC_ISR) Last Channel Change (cleared on read) Mask */
#define ADC_ISR_LCCHG(value)                  (ADC_ISR_LCCHG_Msk & ((value) << ADC_ISR_LCCHG_Pos))
#define ADC_ISR_DRDY_Pos                      (24U)                                          /**< (ADC_ISR) Data Ready (automatically set / cleared) Position */
#define ADC_ISR_DRDY_Msk                      (0x1U << ADC_ISR_DRDY_Pos)                     /**< (ADC_ISR) Data Ready (automatically set / cleared) Mask */
#define ADC_ISR_DRDY(value)                   (ADC_ISR_DRDY_Msk & ((value) << ADC_ISR_DRDY_Pos))
#define ADC_ISR_GOVRE_Pos                     (25U)                                          /**< (ADC_ISR) General Overrun Error (cleared on read) Position */
#define ADC_ISR_GOVRE_Msk                     (0x1U << ADC_ISR_GOVRE_Pos)                    /**< (ADC_ISR) General Overrun Error (cleared on read) Mask */
#define ADC_ISR_GOVRE(value)                  (ADC_ISR_GOVRE_Msk & ((value) << ADC_ISR_GOVRE_Pos))
#define ADC_ISR_COMPE_Pos                     (26U)                                          /**< (ADC_ISR) Comparison Event (cleared on read) Position */
#define ADC_ISR_COMPE_Msk                     (0x1U << ADC_ISR_COMPE_Pos)                    /**< (ADC_ISR) Comparison Event (cleared on read) Mask */
#define ADC_ISR_COMPE(value)                  (ADC_ISR_COMPE_Msk & ((value) << ADC_ISR_COMPE_Pos))
#define ADC_ISR_ENDRX_Pos                     (27U)                                          /**< (ADC_ISR) End of Receive Transfer (cleared by writing ADC_RCR or ADC_RNCR) Position */
#define ADC_ISR_ENDRX_Msk                     (0x1U << ADC_ISR_ENDRX_Pos)                    /**< (ADC_ISR) End of Receive Transfer (cleared by writing ADC_RCR or ADC_RNCR) Mask */
#define ADC_ISR_ENDRX(value)                  (ADC_ISR_ENDRX_Msk & ((value) << ADC_ISR_ENDRX_Pos))
#define ADC_ISR_RXBUFF_Pos                    (28U)                                          /**< (ADC_ISR) Receive Buffer Full (cleared by writing ADC_RCR or ADC_RNCR) Position */
#define ADC_ISR_RXBUFF_Msk                    (0x1U << ADC_ISR_RXBUFF_Pos)                   /**< (ADC_ISR) Receive Buffer Full (cleared by writing ADC_RCR or ADC_RNCR) Mask */
#define ADC_ISR_RXBUFF(value)                 (ADC_ISR_RXBUFF_Msk & ((value) << ADC_ISR_RXBUFF_Pos))
#define ADC_ISR_Msk                           (0x1F0800FFUL)                                 /**< (ADC_ISR) Register Mask  */

/* -------- ADC_LCTMR : (ADC Offset: 0x34) (R/W 32) Last Channel Trigger Mode Register -------- */
#define ADC_LCTMR_DUALTRIG_Pos                (0U)                                           /**< (ADC_LCTMR) Dual Trigger ON Position */
#define ADC_LCTMR_DUALTRIG_Msk                (0x1U << ADC_LCTMR_DUALTRIG_Pos)               /**< (ADC_LCTMR) Dual Trigger ON Mask */
#define ADC_LCTMR_DUALTRIG(value)             (ADC_LCTMR_DUALTRIG_Msk & ((value) << ADC_LCTMR_DUALTRIG_Pos))
#define ADC_LCTMR_CMPMOD_Pos                  (4U)                                           /**< (ADC_LCTMR) Last Channel Comparison Mode Position */
#define ADC_LCTMR_CMPMOD_Msk                  (0x3U << ADC_LCTMR_CMPMOD_Pos)                 /**< (ADC_LCTMR) Last Channel Comparison Mode Mask */
#define ADC_LCTMR_CMPMOD(value)               (ADC_LCTMR_CMPMOD_Msk & ((value) << ADC_LCTMR_CMPMOD_Pos))
#define   ADC_LCTMR_CMPMOD_LOW_Val            (0U)                                           /**< (ADC_LCTMR) Generates an event when the converted data is lower than the low threshold of the window.  */
#define   ADC_LCTMR_CMPMOD_HIGH_Val           (1U)                                           /**< (ADC_LCTMR) Generates an event when the converted data is higher than the high threshold of the window.  */
#define   ADC_LCTMR_CMPMOD_IN_Val             (2U)                                           /**< (ADC_LCTMR) Generates an event when the converted data is in the comparison window.  */
#define   ADC_LCTMR_CMPMOD_OUT_Val            (3U)                                           /**< (ADC_LCTMR) Generates an event when the converted data is out of the comparison window.  */
#define ADC_LCTMR_CMPMOD_LOW                  (ADC_LCTMR_CMPMOD_LOW_Val << ADC_LCTMR_CMPMOD_Pos) /**< (ADC_LCTMR) Generates an event when the converted data is lower than the low threshold of the window. Position  */
#define ADC_LCTMR_CMPMOD_HIGH                 (ADC_LCTMR_CMPMOD_HIGH_Val << ADC_LCTMR_CMPMOD_Pos) /**< (ADC_LCTMR) Generates an event when the converted data is higher than the high threshold of the window. Position  */
#define ADC_LCTMR_CMPMOD_IN                   (ADC_LCTMR_CMPMOD_IN_Val << ADC_LCTMR_CMPMOD_Pos) /**< (ADC_LCTMR) Generates an event when the converted data is in the comparison window. Position  */
#define ADC_LCTMR_CMPMOD_OUT                  (ADC_LCTMR_CMPMOD_OUT_Val << ADC_LCTMR_CMPMOD_Pos) /**< (ADC_LCTMR) Generates an event when the converted data is out of the comparison window. Position  */
#define ADC_LCTMR_Msk                         (0x00000031UL)                                 /**< (ADC_LCTMR) Register Mask  */

/* -------- ADC_LCCWR : (ADC Offset: 0x38) (R/W 32) Last Channel Compare Window Register -------- */
#define ADC_LCCWR_LOWTHRES_Pos                (0U)                                           /**< (ADC_LCCWR) Low Threshold Position */
#define ADC_LCCWR_LOWTHRES_Msk                (0xFFFU << ADC_LCCWR_LOWTHRES_Pos)             /**< (ADC_LCCWR) Low Threshold Mask */
#define ADC_LCCWR_LOWTHRES(value)             (ADC_LCCWR_LOWTHRES_Msk & ((value) << ADC_LCCWR_LOWTHRES_Pos))
#define ADC_LCCWR_HIGHTHRES_Pos               (16U)                                          /**< (ADC_LCCWR) High Threshold Position */
#define ADC_LCCWR_HIGHTHRES_Msk               (0xFFFU << ADC_LCCWR_HIGHTHRES_Pos)            /**< (ADC_LCCWR) High Threshold Mask */
#define ADC_LCCWR_HIGHTHRES(value)            (ADC_LCCWR_HIGHTHRES_Msk & ((value) << ADC_LCCWR_HIGHTHRES_Pos))
#define ADC_LCCWR_Msk                         (0x0FFF0FFFUL)                                 /**< (ADC_LCCWR) Register Mask  */

/* -------- ADC_OVER : (ADC Offset: 0x3C) (R/  32) Overrun Status Register -------- */
#define ADC_OVER_OVRE0_Pos                    (0U)                                           /**< (ADC_OVER) Overrun Error 0 Position */
#define ADC_OVER_OVRE0_Msk                    (0x1U << ADC_OVER_OVRE0_Pos)                   /**< (ADC_OVER) Overrun Error 0 Mask */
#define ADC_OVER_OVRE0(value)                 (ADC_OVER_OVRE0_Msk & ((value) << ADC_OVER_OVRE0_Pos))
#define ADC_OVER_OVRE1_Pos                    (1U)                                           /**< (ADC_OVER) Overrun Error 1 Position */
#define ADC_OVER_OVRE1_Msk                    (0x1U << ADC_OVER_OVRE1_Pos)                   /**< (ADC_OVER) Overrun Error 1 Mask */
#define ADC_OVER_OVRE1(value)                 (ADC_OVER_OVRE1_Msk & ((value) << ADC_OVER_OVRE1_Pos))
#define ADC_OVER_OVRE2_Pos                    (2U)                                           /**< (ADC_OVER) Overrun Error 2 Position */
#define ADC_OVER_OVRE2_Msk                    (0x1U << ADC_OVER_OVRE2_Pos)                   /**< (ADC_OVER) Overrun Error 2 Mask */
#define ADC_OVER_OVRE2(value)                 (ADC_OVER_OVRE2_Msk & ((value) << ADC_OVER_OVRE2_Pos))
#define ADC_OVER_OVRE3_Pos                    (3U)                                           /**< (ADC_OVER) Overrun Error 3 Position */
#define ADC_OVER_OVRE3_Msk                    (0x1U << ADC_OVER_OVRE3_Pos)                   /**< (ADC_OVER) Overrun Error 3 Mask */
#define ADC_OVER_OVRE3(value)                 (ADC_OVER_OVRE3_Msk & ((value) << ADC_OVER_OVRE3_Pos))
#define ADC_OVER_OVRE4_Pos                    (4U)                                           /**< (ADC_OVER) Overrun Error 4 Position */
#define ADC_OVER_OVRE4_Msk                    (0x1U << ADC_OVER_OVRE4_Pos)                   /**< (ADC_OVER) Overrun Error 4 Mask */
#define ADC_OVER_OVRE4(value)                 (ADC_OVER_OVRE4_Msk & ((value) << ADC_OVER_OVRE4_Pos))
#define ADC_OVER_OVRE5_Pos                    (5U)                                           /**< (ADC_OVER) Overrun Error 5 Position */
#define ADC_OVER_OVRE5_Msk                    (0x1U << ADC_OVER_OVRE5_Pos)                   /**< (ADC_OVER) Overrun Error 5 Mask */
#define ADC_OVER_OVRE5(value)                 (ADC_OVER_OVRE5_Msk & ((value) << ADC_OVER_OVRE5_Pos))
#define ADC_OVER_OVRE6_Pos                    (6U)                                           /**< (ADC_OVER) Overrun Error 6 Position */
#define ADC_OVER_OVRE6_Msk                    (0x1U << ADC_OVER_OVRE6_Pos)                   /**< (ADC_OVER) Overrun Error 6 Mask */
#define ADC_OVER_OVRE6(value)                 (ADC_OVER_OVRE6_Msk & ((value) << ADC_OVER_OVRE6_Pos))
#define ADC_OVER_OVRE7_Pos                    (7U)                                           /**< (ADC_OVER) Overrun Error 7 Position */
#define ADC_OVER_OVRE7_Msk                    (0x1U << ADC_OVER_OVRE7_Pos)                   /**< (ADC_OVER) Overrun Error 7 Mask */
#define ADC_OVER_OVRE7(value)                 (ADC_OVER_OVRE7_Msk & ((value) << ADC_OVER_OVRE7_Pos))
#define ADC_OVER_Msk                          (0x000000FFUL)                                 /**< (ADC_OVER) Register Mask  */

/* -------- ADC_EMR : (ADC Offset: 0x40) (R/W 32) Extended Mode Register -------- */
#define ADC_EMR_CMPMODE_Pos                   (0U)                                           /**< (ADC_EMR) Comparison Mode Position */
#define ADC_EMR_CMPMODE_Msk                   (0x3U << ADC_EMR_CMPMODE_Pos)                  /**< (ADC_EMR) Comparison Mode Mask */
#define ADC_EMR_CMPMODE(value)                (ADC_EMR_CMPMODE_Msk & ((value) << ADC_EMR_CMPMODE_Pos))
#define   ADC_EMR_CMPMODE_LOW_Val             (0U)                                           /**< (ADC_EMR) Generates an event when the converted data is lower than the low threshold of the window.  */
#define   ADC_EMR_CMPMODE_HIGH_Val            (1U)                                           /**< (ADC_EMR) Generates an event when the converted data is higher than the high threshold of the window.  */
#define   ADC_EMR_CMPMODE_IN_Val              (2U)                                           /**< (ADC_EMR) Generates an event when the converted data is in the comparison window.  */
#define   ADC_EMR_CMPMODE_OUT_Val             (3U)                                           /**< (ADC_EMR) Generates an event when the converted data is out of the comparison window.  */
#define ADC_EMR_CMPMODE_LOW                   (ADC_EMR_CMPMODE_LOW_Val << ADC_EMR_CMPMODE_Pos) /**< (ADC_EMR) Generates an event when the converted data is lower than the low threshold of the window. Position  */
#define ADC_EMR_CMPMODE_HIGH                  (ADC_EMR_CMPMODE_HIGH_Val << ADC_EMR_CMPMODE_Pos) /**< (ADC_EMR) Generates an event when the converted data is higher than the high threshold of the window. Position  */
#define ADC_EMR_CMPMODE_IN                    (ADC_EMR_CMPMODE_IN_Val << ADC_EMR_CMPMODE_Pos) /**< (ADC_EMR) Generates an event when the converted data is in the comparison window. Position  */
#define ADC_EMR_CMPMODE_OUT                   (ADC_EMR_CMPMODE_OUT_Val << ADC_EMR_CMPMODE_Pos) /**< (ADC_EMR) Generates an event when the converted data is out of the comparison window. Position  */
#define ADC_EMR_CMPTYPE_Pos                   (2U)                                           /**< (ADC_EMR) Comparison Type Position */
#define ADC_EMR_CMPTYPE_Msk                   (0x1U << ADC_EMR_CMPTYPE_Pos)                  /**< (ADC_EMR) Comparison Type Mask */
#define ADC_EMR_CMPTYPE(value)                (ADC_EMR_CMPTYPE_Msk & ((value) << ADC_EMR_CMPTYPE_Pos))
#define   ADC_EMR_CMPTYPE_FLAG_ONLY_Val       (0U)                                           /**< (ADC_EMR) Any conversion is performed and comparison function drives the COMPE flag.  */
#define   ADC_EMR_CMPTYPE_START_CONDITION_Val (1U)                                           /**< (ADC_EMR) Comparison conditions must be met to start the storage of all conversions until the CMPRST bit is set.  */
#define ADC_EMR_CMPTYPE_FLAG_ONLY             (ADC_EMR_CMPTYPE_FLAG_ONLY_Val << ADC_EMR_CMPTYPE_Pos) /**< (ADC_EMR) Any conversion is performed and comparison function drives the COMPE flag. Position  */
#define ADC_EMR_CMPTYPE_START_CONDITION       (ADC_EMR_CMPTYPE_START_CONDITION_Val << ADC_EMR_CMPTYPE_Pos) /**< (ADC_EMR) Comparison conditions must be met to start the storage of all conversions until the CMPRST bit is set. Position  */
#define ADC_EMR_CMPSEL_Pos                    (4U)                                           /**< (ADC_EMR) Comparison Selected Channel Position */
#define ADC_EMR_CMPSEL_Msk                    (0xFU << ADC_EMR_CMPSEL_Pos)                   /**< (ADC_EMR) Comparison Selected Channel Mask */
#define ADC_EMR_CMPSEL(value)                 (ADC_EMR_CMPSEL_Msk & ((value) << ADC_EMR_CMPSEL_Pos))
#define ADC_EMR_CMPALL_Pos                    (9U)                                           /**< (ADC_EMR) Compare All Channels Position */
#define ADC_EMR_CMPALL_Msk                    (0x1U << ADC_EMR_CMPALL_Pos)                   /**< (ADC_EMR) Compare All Channels Mask */
#define ADC_EMR_CMPALL(value)                 (ADC_EMR_CMPALL_Msk & ((value) << ADC_EMR_CMPALL_Pos))
#define ADC_EMR_CMPFILTER_Pos                 (12U)                                          /**< (ADC_EMR) Compare Event Filtering Position */
#define ADC_EMR_CMPFILTER_Msk                 (0x3U << ADC_EMR_CMPFILTER_Pos)                /**< (ADC_EMR) Compare Event Filtering Mask */
#define ADC_EMR_CMPFILTER(value)              (ADC_EMR_CMPFILTER_Msk & ((value) << ADC_EMR_CMPFILTER_Pos))
#define ADC_EMR_OSR_Pos                       (16U)                                          /**< (ADC_EMR) Over Sampling Rate Position */
#define ADC_EMR_OSR_Msk                       (0x7U << ADC_EMR_OSR_Pos)                      /**< (ADC_EMR) Over Sampling Rate Mask */
#define ADC_EMR_OSR(value)                    (ADC_EMR_OSR_Msk & ((value) << ADC_EMR_OSR_Pos))
#define   ADC_EMR_OSR_NO_AVERAGE_Val          (0U)                                           /**< (ADC_EMR) No averaging. ADC sample rate is maximum.  */
#define   ADC_EMR_OSR_OSR4_Val                (1U)                                           /**< (ADC_EMR) 1-bit enhanced resolution by averaging. ADC sample rate divided by 4.  */
#define   ADC_EMR_OSR_OSR16_Val               (2U)                                           /**< (ADC_EMR) 2-bit enhanced resolution by averaging. ADC sample rate divided by 16.  */
#define   ADC_EMR_OSR_OSR64_Val               (3U)                                           /**< (ADC_EMR) 3-bit enhanced resolution by averaging. ADC sample rate divided by 64.  */
#define   ADC_EMR_OSR_OSR256_Val              (4U)                                           /**< (ADC_EMR) 4-bit enhanced resolution by averaging. ADC sample rate divided by 256.  */
#define ADC_EMR_OSR_NO_AVERAGE                (ADC_EMR_OSR_NO_AVERAGE_Val << ADC_EMR_OSR_Pos) /**< (ADC_EMR) No averaging. ADC sample rate is maximum. Position  */
#define ADC_EMR_OSR_OSR4                      (ADC_EMR_OSR_OSR4_Val << ADC_EMR_OSR_Pos)      /**< (ADC_EMR) 1-bit enhanced resolution by averaging. ADC sample rate divided by 4. Position  */
#define ADC_EMR_OSR_OSR16                     (ADC_EMR_OSR_OSR16_Val << ADC_EMR_OSR_Pos)     /**< (ADC_EMR) 2-bit enhanced resolution by averaging. ADC sample rate divided by 16. Position  */
#define ADC_EMR_OSR_OSR64                     (ADC_EMR_OSR_OSR64_Val << ADC_EMR_OSR_Pos)     /**< (ADC_EMR) 3-bit enhanced resolution by averaging. ADC sample rate divided by 64. Position  */
#define ADC_EMR_OSR_OSR256                    (ADC_EMR_OSR_OSR256_Val << ADC_EMR_OSR_Pos)    /**< (ADC_EMR) 4-bit enhanced resolution by averaging. ADC sample rate divided by 256. Position  */
#define ADC_EMR_ASTE_Pos                      (20U)                                          /**< (ADC_EMR) Averaging on Single Trigger Event Position */
#define ADC_EMR_ASTE_Msk                      (0x1U << ADC_EMR_ASTE_Pos)                     /**< (ADC_EMR) Averaging on Single Trigger Event Mask */
#define ADC_EMR_ASTE(value)                   (ADC_EMR_ASTE_Msk & ((value) << ADC_EMR_ASTE_Pos))
#define   ADC_EMR_ASTE_MULTI_TRIG_AVERAGE_Val (0U)                                           /**< (ADC_EMR) The average requests several trigger events.  */
#define   ADC_EMR_ASTE_SINGLE_TRIG_AVERAGE_Val (1U)                                           /**< (ADC_EMR) The average requests only one trigger event.  */
#define ADC_EMR_ASTE_MULTI_TRIG_AVERAGE       (ADC_EMR_ASTE_MULTI_TRIG_AVERAGE_Val << ADC_EMR_ASTE_Pos) /**< (ADC_EMR) The average requests several trigger events. Position  */
#define ADC_EMR_ASTE_SINGLE_TRIG_AVERAGE      (ADC_EMR_ASTE_SINGLE_TRIG_AVERAGE_Val << ADC_EMR_ASTE_Pos) /**< (ADC_EMR) The average requests only one trigger event. Position  */
#define ADC_EMR_SRCCLK_Pos                    (21U)                                          /**< (ADC_EMR) External Clock Selection Position */
#define ADC_EMR_SRCCLK_Msk                    (0x1U << ADC_EMR_SRCCLK_Pos)                   /**< (ADC_EMR) External Clock Selection Mask */
#define ADC_EMR_SRCCLK(value)                 (ADC_EMR_SRCCLK_Msk & ((value) << ADC_EMR_SRCCLK_Pos))
#define   ADC_EMR_SRCCLK_PERIPH_CLK_Val       (0U)                                           /**< (ADC_EMR) The peripheral clock is the source for the ADC prescaler.  */
#define   ADC_EMR_SRCCLK_PMC_PCK_Val          (1U)                                           /**< (ADC_EMR) PMC PCKx is the source clock for the ADC prescaler, thus the ADC clock can be independent of the core/peripheral clock.  */
#define ADC_EMR_SRCCLK_PERIPH_CLK             (ADC_EMR_SRCCLK_PERIPH_CLK_Val << ADC_EMR_SRCCLK_Pos) /**< (ADC_EMR) The peripheral clock is the source for the ADC prescaler. Position  */
#define ADC_EMR_SRCCLK_PMC_PCK                (ADC_EMR_SRCCLK_PMC_PCK_Val << ADC_EMR_SRCCLK_Pos) /**< (ADC_EMR) PMC PCKx is the source clock for the ADC prescaler, thus the ADC clock can be independent of the core/peripheral clock. Position  */
#define ADC_EMR_TAG_Pos                       (24U)                                          /**< (ADC_EMR) Tag of the ADC_LCDR Position */
#define ADC_EMR_TAG_Msk                       (0x1U << ADC_EMR_TAG_Pos)                      /**< (ADC_EMR) Tag of the ADC_LCDR Mask */
#define ADC_EMR_TAG(value)                    (ADC_EMR_TAG_Msk & ((value) << ADC_EMR_TAG_Pos))
#define ADC_EMR_Msk                           (0x013732F7UL)                                 /**< (ADC_EMR) Register Mask  */

/* -------- ADC_CWR : (ADC Offset: 0x44) (R/W 32) Compare Window Register -------- */
#define ADC_CWR_LOWTHRES_Pos                  (0U)                                           /**< (ADC_CWR) Low Threshold Position */
#define ADC_CWR_LOWTHRES_Msk                  (0xFFFFU << ADC_CWR_LOWTHRES_Pos)              /**< (ADC_CWR) Low Threshold Mask */
#define ADC_CWR_LOWTHRES(value)               (ADC_CWR_LOWTHRES_Msk & ((value) << ADC_CWR_LOWTHRES_Pos))
#define ADC_CWR_HIGHTHRES_Pos                 (16U)                                          /**< (ADC_CWR) High Threshold Position */
#define ADC_CWR_HIGHTHRES_Msk                 (0xFFFFU << ADC_CWR_HIGHTHRES_Pos)             /**< (ADC_CWR) High Threshold Mask */
#define ADC_CWR_HIGHTHRES(value)              (ADC_CWR_HIGHTHRES_Msk & ((value) << ADC_CWR_HIGHTHRES_Pos))
#define ADC_CWR_Msk                           (0xFFFFFFFFUL)                                 /**< (ADC_CWR) Register Mask  */

/* -------- ADC_COR : (ADC Offset: 0x4C) (R/W 32) Channel Offset Register -------- */
#define ADC_COR_OFF0_Pos                      (0U)                                           /**< (ADC_COR) Offset for Channel 0 Position */
#define ADC_COR_OFF0_Msk                      (0x1U << ADC_COR_OFF0_Pos)                     /**< (ADC_COR) Offset for Channel 0 Mask */
#define ADC_COR_OFF0(value)                   (ADC_COR_OFF0_Msk & ((value) << ADC_COR_OFF0_Pos))
#define ADC_COR_OFF1_Pos                      (1U)                                           /**< (ADC_COR) Offset for Channel 1 Position */
#define ADC_COR_OFF1_Msk                      (0x1U << ADC_COR_OFF1_Pos)                     /**< (ADC_COR) Offset for Channel 1 Mask */
#define ADC_COR_OFF1(value)                   (ADC_COR_OFF1_Msk & ((value) << ADC_COR_OFF1_Pos))
#define ADC_COR_OFF2_Pos                      (2U)                                           /**< (ADC_COR) Offset for Channel 2 Position */
#define ADC_COR_OFF2_Msk                      (0x1U << ADC_COR_OFF2_Pos)                     /**< (ADC_COR) Offset for Channel 2 Mask */
#define ADC_COR_OFF2(value)                   (ADC_COR_OFF2_Msk & ((value) << ADC_COR_OFF2_Pos))
#define ADC_COR_OFF3_Pos                      (3U)                                           /**< (ADC_COR) Offset for Channel 3 Position */
#define ADC_COR_OFF3_Msk                      (0x1U << ADC_COR_OFF3_Pos)                     /**< (ADC_COR) Offset for Channel 3 Mask */
#define ADC_COR_OFF3(value)                   (ADC_COR_OFF3_Msk & ((value) << ADC_COR_OFF3_Pos))
#define ADC_COR_OFF4_Pos                      (4U)                                           /**< (ADC_COR) Offset for Channel 4 Position */
#define ADC_COR_OFF4_Msk                      (0x1U << ADC_COR_OFF4_Pos)                     /**< (ADC_COR) Offset for Channel 4 Mask */
#define ADC_COR_OFF4(value)                   (ADC_COR_OFF4_Msk & ((value) << ADC_COR_OFF4_Pos))
#define ADC_COR_OFF5_Pos                      (5U)                                           /**< (ADC_COR) Offset for Channel 5 Position */
#define ADC_COR_OFF5_Msk                      (0x1U << ADC_COR_OFF5_Pos)                     /**< (ADC_COR) Offset for Channel 5 Mask */
#define ADC_COR_OFF5(value)                   (ADC_COR_OFF5_Msk & ((value) << ADC_COR_OFF5_Pos))
#define ADC_COR_OFF6_Pos                      (6U)                                           /**< (ADC_COR) Offset for Channel 6 Position */
#define ADC_COR_OFF6_Msk                      (0x1U << ADC_COR_OFF6_Pos)                     /**< (ADC_COR) Offset for Channel 6 Mask */
#define ADC_COR_OFF6(value)                   (ADC_COR_OFF6_Msk & ((value) << ADC_COR_OFF6_Pos))
#define ADC_COR_OFF7_Pos                      (7U)                                           /**< (ADC_COR) Offset for Channel 7 Position */
#define ADC_COR_OFF7_Msk                      (0x1U << ADC_COR_OFF7_Pos)                     /**< (ADC_COR) Offset for Channel 7 Mask */
#define ADC_COR_OFF7(value)                   (ADC_COR_OFF7_Msk & ((value) << ADC_COR_OFF7_Pos))
#define ADC_COR_DIFF0_Pos                     (16U)                                          /**< (ADC_COR) Differential Inputs for Channel 0 Position */
#define ADC_COR_DIFF0_Msk                     (0x1U << ADC_COR_DIFF0_Pos)                    /**< (ADC_COR) Differential Inputs for Channel 0 Mask */
#define ADC_COR_DIFF0(value)                  (ADC_COR_DIFF0_Msk & ((value) << ADC_COR_DIFF0_Pos))
#define ADC_COR_DIFF1_Pos                     (17U)                                          /**< (ADC_COR) Differential Inputs for Channel 1 Position */
#define ADC_COR_DIFF1_Msk                     (0x1U << ADC_COR_DIFF1_Pos)                    /**< (ADC_COR) Differential Inputs for Channel 1 Mask */
#define ADC_COR_DIFF1(value)                  (ADC_COR_DIFF1_Msk & ((value) << ADC_COR_DIFF1_Pos))
#define ADC_COR_DIFF2_Pos                     (18U)                                          /**< (ADC_COR) Differential Inputs for Channel 2 Position */
#define ADC_COR_DIFF2_Msk                     (0x1U << ADC_COR_DIFF2_Pos)                    /**< (ADC_COR) Differential Inputs for Channel 2 Mask */
#define ADC_COR_DIFF2(value)                  (ADC_COR_DIFF2_Msk & ((value) << ADC_COR_DIFF2_Pos))
#define ADC_COR_DIFF3_Pos                     (19U)                                          /**< (ADC_COR) Differential Inputs for Channel 3 Position */
#define ADC_COR_DIFF3_Msk                     (0x1U << ADC_COR_DIFF3_Pos)                    /**< (ADC_COR) Differential Inputs for Channel 3 Mask */
#define ADC_COR_DIFF3(value)                  (ADC_COR_DIFF3_Msk & ((value) << ADC_COR_DIFF3_Pos))
#define ADC_COR_DIFF4_Pos                     (20U)                                          /**< (ADC_COR) Differential Inputs for Channel 4 Position */
#define ADC_COR_DIFF4_Msk                     (0x1U << ADC_COR_DIFF4_Pos)                    /**< (ADC_COR) Differential Inputs for Channel 4 Mask */
#define ADC_COR_DIFF4(value)                  (ADC_COR_DIFF4_Msk & ((value) << ADC_COR_DIFF4_Pos))
#define ADC_COR_DIFF5_Pos                     (21U)                                          /**< (ADC_COR) Differential Inputs for Channel 5 Position */
#define ADC_COR_DIFF5_Msk                     (0x1U << ADC_COR_DIFF5_Pos)                    /**< (ADC_COR) Differential Inputs for Channel 5 Mask */
#define ADC_COR_DIFF5(value)                  (ADC_COR_DIFF5_Msk & ((value) << ADC_COR_DIFF5_Pos))
#define ADC_COR_DIFF6_Pos                     (22U)                                          /**< (ADC_COR) Differential Inputs for Channel 6 Position */
#define ADC_COR_DIFF6_Msk                     (0x1U << ADC_COR_DIFF6_Pos)                    /**< (ADC_COR) Differential Inputs for Channel 6 Mask */
#define ADC_COR_DIFF6(value)                  (ADC_COR_DIFF6_Msk & ((value) << ADC_COR_DIFF6_Pos))
#define ADC_COR_DIFF7_Pos                     (23U)                                          /**< (ADC_COR) Differential Inputs for Channel 7 Position */
#define ADC_COR_DIFF7_Msk                     (0x1U << ADC_COR_DIFF7_Pos)                    /**< (ADC_COR) Differential Inputs for Channel 7 Mask */
#define ADC_COR_DIFF7(value)                  (ADC_COR_DIFF7_Msk & ((value) << ADC_COR_DIFF7_Pos))
#define ADC_COR_Msk                           (0x00FF00FFUL)                                 /**< (ADC_COR) Register Mask  */

/* -------- ADC_CDR : (ADC Offset: 0x50) (R/  32) Channel Data Register 0 -------- */
#define ADC_CDR_DATA_Pos                      (0U)                                           /**< (ADC_CDR) Converted Data Position */
#define ADC_CDR_DATA_Msk                      (0xFFFFU << ADC_CDR_DATA_Pos)                  /**< (ADC_CDR) Converted Data Mask */
#define ADC_CDR_DATA(value)                   (ADC_CDR_DATA_Msk & ((value) << ADC_CDR_DATA_Pos))
#define ADC_CDR_Msk                           (0x0000FFFFUL)                                 /**< (ADC_CDR) Register Mask  */

/* -------- ADC_ACR : (ADC Offset: 0x94) (R/W 32) Analog Control Register -------- */
#define ADC_ACR_AUTOTEST_Pos                  (30U)                                          /**< (ADC_ACR) ADC Auto-test modes Position */
#define ADC_ACR_AUTOTEST_Msk                  (0x3U << ADC_ACR_AUTOTEST_Pos)                 /**< (ADC_ACR) ADC Auto-test modes Mask */
#define ADC_ACR_AUTOTEST(value)               (ADC_ACR_AUTOTEST_Msk & ((value) << ADC_ACR_AUTOTEST_Pos))
#define   ADC_ACR_AUTOTEST_NO_AUTOTEST_Val    (0U)                                           /**< (ADC_ACR) No auto test, normal mode of operation  */
#define   ADC_ACR_AUTOTEST_OFFSET_ERROR_Val   (1U)                                           /**< (ADC_ACR) Offset Error test (refer to ADC cell datasheet)  */
#define   ADC_ACR_AUTOTEST_GAIN_ERROR_HIGH_Val (2U)                                           /**< (ADC_ACR) Gain Error (high code) test (refer to ADC cell datasheet)  */
#define   ADC_ACR_AUTOTEST_GAIN_ERROR_LOW_Val (3U)                                           /**< (ADC_ACR) Gain Error (low code) test (refer to ADC cell datasheet)  */
#define ADC_ACR_AUTOTEST_NO_AUTOTEST          (ADC_ACR_AUTOTEST_NO_AUTOTEST_Val << ADC_ACR_AUTOTEST_Pos) /**< (ADC_ACR) No auto test, normal mode of operation Position  */
#define ADC_ACR_AUTOTEST_OFFSET_ERROR         (ADC_ACR_AUTOTEST_OFFSET_ERROR_Val << ADC_ACR_AUTOTEST_Pos) /**< (ADC_ACR) Offset Error test (refer to ADC cell datasheet) Position  */
#define ADC_ACR_AUTOTEST_GAIN_ERROR_HIGH      (ADC_ACR_AUTOTEST_GAIN_ERROR_HIGH_Val << ADC_ACR_AUTOTEST_Pos) /**< (ADC_ACR) Gain Error (high code) test (refer to ADC cell datasheet) Position  */
#define ADC_ACR_AUTOTEST_GAIN_ERROR_LOW       (ADC_ACR_AUTOTEST_GAIN_ERROR_LOW_Val << ADC_ACR_AUTOTEST_Pos) /**< (ADC_ACR) Gain Error (low code) test (refer to ADC cell datasheet) Position  */
#define ADC_ACR_Msk                           (0xC0000000UL)                                 /**< (ADC_ACR) Register Mask  */

/* -------- ADC_WPMR : (ADC Offset: 0xE4) (R/W 32) Write Protection Mode Register -------- */
#define ADC_WPMR_WPEN_Pos                     (0U)                                           /**< (ADC_WPMR) Write Protection Enable Position */
#define ADC_WPMR_WPEN_Msk                     (0x1U << ADC_WPMR_WPEN_Pos)                    /**< (ADC_WPMR) Write Protection Enable Mask */
#define ADC_WPMR_WPEN(value)                  (ADC_WPMR_WPEN_Msk & ((value) << ADC_WPMR_WPEN_Pos))
#define ADC_WPMR_WPKEY_Pos                    (8U)                                           /**< (ADC_WPMR) Write Protection Key Position */
#define ADC_WPMR_WPKEY_Msk                    (0xFFFFFFU << ADC_WPMR_WPKEY_Pos)              /**< (ADC_WPMR) Write Protection Key Mask */
#define ADC_WPMR_WPKEY(value)                 (ADC_WPMR_WPKEY_Msk & ((value) << ADC_WPMR_WPKEY_Pos))
#define   ADC_WPMR_WPKEY_PASSWD_Val           (4277315U)                                     /**< (ADC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0  */
#define ADC_WPMR_WPKEY_PASSWD                 (ADC_WPMR_WPKEY_PASSWD_Val << ADC_WPMR_WPKEY_Pos) /**< (ADC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0 Position  */
#define ADC_WPMR_Msk                          (0xFFFFFF01UL)                                 /**< (ADC_WPMR) Register Mask  */

/* -------- ADC_WPSR : (ADC Offset: 0xE8) (R/  32) Write Protection Status Register -------- */
#define ADC_WPSR_WPVS_Pos                     (0U)                                           /**< (ADC_WPSR) Write Protection Violation Status Position */
#define ADC_WPSR_WPVS_Msk                     (0x1U << ADC_WPSR_WPVS_Pos)                    /**< (ADC_WPSR) Write Protection Violation Status Mask */
#define ADC_WPSR_WPVS(value)                  (ADC_WPSR_WPVS_Msk & ((value) << ADC_WPSR_WPVS_Pos))
#define ADC_WPSR_WPVSRC_Pos                   (8U)                                           /**< (ADC_WPSR) Write Protection Violation Source Position */
#define ADC_WPSR_WPVSRC_Msk                   (0xFFFFU << ADC_WPSR_WPVSRC_Pos)               /**< (ADC_WPSR) Write Protection Violation Source Mask */
#define ADC_WPSR_WPVSRC(value)                (ADC_WPSR_WPVSRC_Msk & ((value) << ADC_WPSR_WPVSRC_Pos))
#define ADC_WPSR_Msk                          (0x00FFFF01UL)                                 /**< (ADC_WPSR) Register Mask  */

/* -------- ADC_RPR : (ADC Offset: 0x100) (R/W 32) Receive Pointer Register -------- */
#define ADC_RPR_RXPTR_Pos                     (0U)                                           /**< (ADC_RPR) Receive Pointer Register Position */
#define ADC_RPR_RXPTR_Msk                     (0xFFFFFFFFU << ADC_RPR_RXPTR_Pos)             /**< (ADC_RPR) Receive Pointer Register Mask */
#define ADC_RPR_RXPTR(value)                  (ADC_RPR_RXPTR_Msk & ((value) << ADC_RPR_RXPTR_Pos))
#define ADC_RPR_Msk                           (0xFFFFFFFFUL)                                 /**< (ADC_RPR) Register Mask  */

/* -------- ADC_RCR : (ADC Offset: 0x104) (R/W 32) Receive Counter Register -------- */
#define ADC_RCR_RXCTR_Pos                     (0U)                                           /**< (ADC_RCR) Receive Counter Register Position */
#define ADC_RCR_RXCTR_Msk                     (0xFFFFU << ADC_RCR_RXCTR_Pos)                 /**< (ADC_RCR) Receive Counter Register Mask */
#define ADC_RCR_RXCTR(value)                  (ADC_RCR_RXCTR_Msk & ((value) << ADC_RCR_RXCTR_Pos))
#define ADC_RCR_Msk                           (0x0000FFFFUL)                                 /**< (ADC_RCR) Register Mask  */

/* -------- ADC_RNPR : (ADC Offset: 0x110) (R/W 32) Receive Next Pointer Register -------- */
#define ADC_RNPR_RXNPTR_Pos                   (0U)                                           /**< (ADC_RNPR) Receive Next Pointer Position */
#define ADC_RNPR_RXNPTR_Msk                   (0xFFFFFFFFU << ADC_RNPR_RXNPTR_Pos)           /**< (ADC_RNPR) Receive Next Pointer Mask */
#define ADC_RNPR_RXNPTR(value)                (ADC_RNPR_RXNPTR_Msk & ((value) << ADC_RNPR_RXNPTR_Pos))
#define ADC_RNPR_Msk                          (0xFFFFFFFFUL)                                 /**< (ADC_RNPR) Register Mask  */

/* -------- ADC_RNCR : (ADC Offset: 0x114) (R/W 32) Receive Next Counter Register -------- */
#define ADC_RNCR_RXNCTR_Pos                   (0U)                                           /**< (ADC_RNCR) Receive Next Counter Position */
#define ADC_RNCR_RXNCTR_Msk                   (0xFFFFU << ADC_RNCR_RXNCTR_Pos)               /**< (ADC_RNCR) Receive Next Counter Mask */
#define ADC_RNCR_RXNCTR(value)                (ADC_RNCR_RXNCTR_Msk & ((value) << ADC_RNCR_RXNCTR_Pos))
#define ADC_RNCR_Msk                          (0x0000FFFFUL)                                 /**< (ADC_RNCR) Register Mask  */

/* -------- ADC_PTCR : (ADC Offset: 0x120) ( /W 32) Transfer Control Register -------- */
#define ADC_PTCR_RXTEN_Pos                    (0U)                                           /**< (ADC_PTCR) Receiver Transfer Enable Position */
#define ADC_PTCR_RXTEN_Msk                    (0x1U << ADC_PTCR_RXTEN_Pos)                   /**< (ADC_PTCR) Receiver Transfer Enable Mask */
#define ADC_PTCR_RXTEN(value)                 (ADC_PTCR_RXTEN_Msk & ((value) << ADC_PTCR_RXTEN_Pos))
#define ADC_PTCR_RXTDIS_Pos                   (1U)                                           /**< (ADC_PTCR) Receiver Transfer Disable Position */
#define ADC_PTCR_RXTDIS_Msk                   (0x1U << ADC_PTCR_RXTDIS_Pos)                  /**< (ADC_PTCR) Receiver Transfer Disable Mask */
#define ADC_PTCR_RXTDIS(value)                (ADC_PTCR_RXTDIS_Msk & ((value) << ADC_PTCR_RXTDIS_Pos))
#define ADC_PTCR_TXTEN_Pos                    (8U)                                           /**< (ADC_PTCR) Transmitter Transfer Enable Position */
#define ADC_PTCR_TXTEN_Msk                    (0x1U << ADC_PTCR_TXTEN_Pos)                   /**< (ADC_PTCR) Transmitter Transfer Enable Mask */
#define ADC_PTCR_TXTEN(value)                 (ADC_PTCR_TXTEN_Msk & ((value) << ADC_PTCR_TXTEN_Pos))
#define ADC_PTCR_TXTDIS_Pos                   (9U)                                           /**< (ADC_PTCR) Transmitter Transfer Disable Position */
#define ADC_PTCR_TXTDIS_Msk                   (0x1U << ADC_PTCR_TXTDIS_Pos)                  /**< (ADC_PTCR) Transmitter Transfer Disable Mask */
#define ADC_PTCR_TXTDIS(value)                (ADC_PTCR_TXTDIS_Msk & ((value) << ADC_PTCR_TXTDIS_Pos))
#define ADC_PTCR_RXCBEN_Pos                   (16U)                                          /**< (ADC_PTCR) Receiver Circular Buffer Enable Position */
#define ADC_PTCR_RXCBEN_Msk                   (0x1U << ADC_PTCR_RXCBEN_Pos)                  /**< (ADC_PTCR) Receiver Circular Buffer Enable Mask */
#define ADC_PTCR_RXCBEN(value)                (ADC_PTCR_RXCBEN_Msk & ((value) << ADC_PTCR_RXCBEN_Pos))
#define ADC_PTCR_RXCBDIS_Pos                  (17U)                                          /**< (ADC_PTCR) Receiver Circular Buffer Disable Position */
#define ADC_PTCR_RXCBDIS_Msk                  (0x1U << ADC_PTCR_RXCBDIS_Pos)                 /**< (ADC_PTCR) Receiver Circular Buffer Disable Mask */
#define ADC_PTCR_RXCBDIS(value)               (ADC_PTCR_RXCBDIS_Msk & ((value) << ADC_PTCR_RXCBDIS_Pos))
#define ADC_PTCR_TXCBEN_Pos                   (18U)                                          /**< (ADC_PTCR) Transmitter Circular Buffer Enable Position */
#define ADC_PTCR_TXCBEN_Msk                   (0x1U << ADC_PTCR_TXCBEN_Pos)                  /**< (ADC_PTCR) Transmitter Circular Buffer Enable Mask */
#define ADC_PTCR_TXCBEN(value)                (ADC_PTCR_TXCBEN_Msk & ((value) << ADC_PTCR_TXCBEN_Pos))
#define ADC_PTCR_TXCBDIS_Pos                  (19U)                                          /**< (ADC_PTCR) Transmitter Circular Buffer Disable Position */
#define ADC_PTCR_TXCBDIS_Msk                  (0x1U << ADC_PTCR_TXCBDIS_Pos)                 /**< (ADC_PTCR) Transmitter Circular Buffer Disable Mask */
#define ADC_PTCR_TXCBDIS(value)               (ADC_PTCR_TXCBDIS_Msk & ((value) << ADC_PTCR_TXCBDIS_Pos))
#define ADC_PTCR_ERRCLR_Pos                   (24U)                                          /**< (ADC_PTCR) Transfer Bus Error Clear Position */
#define ADC_PTCR_ERRCLR_Msk                   (0x1U << ADC_PTCR_ERRCLR_Pos)                  /**< (ADC_PTCR) Transfer Bus Error Clear Mask */
#define ADC_PTCR_ERRCLR(value)                (ADC_PTCR_ERRCLR_Msk & ((value) << ADC_PTCR_ERRCLR_Pos))
#define ADC_PTCR_Msk                          (0x010F0303UL)                                 /**< (ADC_PTCR) Register Mask  */

/* -------- ADC_PTSR : (ADC Offset: 0x124) (R/  32) Transfer Status Register -------- */
#define ADC_PTSR_RXTEN_Pos                    (0U)                                           /**< (ADC_PTSR) Receiver Transfer Enable Position */
#define ADC_PTSR_RXTEN_Msk                    (0x1U << ADC_PTSR_RXTEN_Pos)                   /**< (ADC_PTSR) Receiver Transfer Enable Mask */
#define ADC_PTSR_RXTEN(value)                 (ADC_PTSR_RXTEN_Msk & ((value) << ADC_PTSR_RXTEN_Pos))
#define ADC_PTSR_TXTEN_Pos                    (8U)                                           /**< (ADC_PTSR) Transmitter Transfer Enable Position */
#define ADC_PTSR_TXTEN_Msk                    (0x1U << ADC_PTSR_TXTEN_Pos)                   /**< (ADC_PTSR) Transmitter Transfer Enable Mask */
#define ADC_PTSR_TXTEN(value)                 (ADC_PTSR_TXTEN_Msk & ((value) << ADC_PTSR_TXTEN_Pos))
#define ADC_PTSR_RXCBEN_Pos                   (16U)                                          /**< (ADC_PTSR) Receiver Circular Buffer Enable Position */
#define ADC_PTSR_RXCBEN_Msk                   (0x1U << ADC_PTSR_RXCBEN_Pos)                  /**< (ADC_PTSR) Receiver Circular Buffer Enable Mask */
#define ADC_PTSR_RXCBEN(value)                (ADC_PTSR_RXCBEN_Msk & ((value) << ADC_PTSR_RXCBEN_Pos))
#define ADC_PTSR_TXCBEN_Pos                   (18U)                                          /**< (ADC_PTSR) Transmitter Circular Buffer Enable Position */
#define ADC_PTSR_TXCBEN_Msk                   (0x1U << ADC_PTSR_TXCBEN_Pos)                  /**< (ADC_PTSR) Transmitter Circular Buffer Enable Mask */
#define ADC_PTSR_TXCBEN(value)                (ADC_PTSR_TXCBEN_Msk & ((value) << ADC_PTSR_TXCBEN_Pos))
#define ADC_PTSR_ERR_Pos                      (24U)                                          /**< (ADC_PTSR) Transfer Bus Error Position */
#define ADC_PTSR_ERR_Msk                      (0x1U << ADC_PTSR_ERR_Pos)                     /**< (ADC_PTSR) Transfer Bus Error Mask */
#define ADC_PTSR_ERR(value)                   (ADC_PTSR_ERR_Msk & ((value) << ADC_PTSR_ERR_Pos))
#define ADC_PTSR_Msk                          (0x01050101UL)                                 /**< (ADC_PTSR) Register Mask  */

/** \brief ADC register offsets definitions */
#define ADC_CR_OFFSET                  (0x00)         /**< (ADC_CR) Control Register Offset */
#define ADC_MR_OFFSET                  (0x04)         /**< (ADC_MR) Mode Register Offset */
#define ADC_SEQR1_OFFSET               (0x08)         /**< (ADC_SEQR1) Channel Sequence Register 1 Offset */
#define ADC_CHER_OFFSET                (0x10)         /**< (ADC_CHER) Channel Enable Register Offset */
#define ADC_CHDR_OFFSET                (0x14)         /**< (ADC_CHDR) Channel Disable Register Offset */
#define ADC_CHSR_OFFSET                (0x18)         /**< (ADC_CHSR) Channel Status Register Offset */
#define ADC_LCDR_OFFSET                (0x20)         /**< (ADC_LCDR) Last Converted Data Register Offset */
#define ADC_IER_OFFSET                 (0x24)         /**< (ADC_IER) Interrupt Enable Register Offset */
#define ADC_IDR_OFFSET                 (0x28)         /**< (ADC_IDR) Interrupt Disable Register Offset */
#define ADC_IMR_OFFSET                 (0x2C)         /**< (ADC_IMR) Interrupt Mask Register Offset */
#define ADC_ISR_OFFSET                 (0x30)         /**< (ADC_ISR) Interrupt Status Register Offset */
#define ADC_LCTMR_OFFSET               (0x34)         /**< (ADC_LCTMR) Last Channel Trigger Mode Register Offset */
#define ADC_LCCWR_OFFSET               (0x38)         /**< (ADC_LCCWR) Last Channel Compare Window Register Offset */
#define ADC_OVER_OFFSET                (0x3C)         /**< (ADC_OVER) Overrun Status Register Offset */
#define ADC_EMR_OFFSET                 (0x40)         /**< (ADC_EMR) Extended Mode Register Offset */
#define ADC_CWR_OFFSET                 (0x44)         /**< (ADC_CWR) Compare Window Register Offset */
#define ADC_COR_OFFSET                 (0x4C)         /**< (ADC_COR) Channel Offset Register Offset */
#define ADC_CDR_OFFSET                 (0x50)         /**< (ADC_CDR) Channel Data Register 0 Offset */
#define ADC_ACR_OFFSET                 (0x94)         /**< (ADC_ACR) Analog Control Register Offset */
#define ADC_WPMR_OFFSET                (0xE4)         /**< (ADC_WPMR) Write Protection Mode Register Offset */
#define ADC_WPSR_OFFSET                (0xE8)         /**< (ADC_WPSR) Write Protection Status Register Offset */
#define ADC_RPR_OFFSET                 (0x100)        /**< (ADC_RPR) Receive Pointer Register Offset */
#define ADC_RCR_OFFSET                 (0x104)        /**< (ADC_RCR) Receive Counter Register Offset */
#define ADC_RNPR_OFFSET                (0x110)        /**< (ADC_RNPR) Receive Next Pointer Register Offset */
#define ADC_RNCR_OFFSET                (0x114)        /**< (ADC_RNCR) Receive Next Counter Register Offset */
#define ADC_PTCR_OFFSET                (0x120)        /**< (ADC_PTCR) Transfer Control Register Offset */
#define ADC_PTSR_OFFSET                (0x124)        /**< (ADC_PTSR) Transfer Status Register Offset */

/** \brief ADC register API structure */
typedef struct
{
  __O   uint32_t                       ADC_CR;          /**< Offset: 0x00 ( /W  32) Control Register */
  __IO  uint32_t                       ADC_MR;          /**< Offset: 0x04 (R/W  32) Mode Register */
  __IO  uint32_t                       ADC_SEQR1;       /**< Offset: 0x08 (R/W  32) Channel Sequence Register 1 */
  __I   uint8_t                        Reserved1[0x04];
  __O   uint32_t                       ADC_CHER;        /**< Offset: 0x10 ( /W  32) Channel Enable Register */
  __O   uint32_t                       ADC_CHDR;        /**< Offset: 0x14 ( /W  32) Channel Disable Register */
  __I   uint32_t                       ADC_CHSR;        /**< Offset: 0x18 (R/   32) Channel Status Register */
  __I   uint8_t                        Reserved2[0x04];
  __I   uint32_t                       ADC_LCDR;        /**< Offset: 0x20 (R/   32) Last Converted Data Register */
  __O   uint32_t                       ADC_IER;         /**< Offset: 0x24 ( /W  32) Interrupt Enable Register */
  __O   uint32_t                       ADC_IDR;         /**< Offset: 0x28 ( /W  32) Interrupt Disable Register */
  __I   uint32_t                       ADC_IMR;         /**< Offset: 0x2c (R/   32) Interrupt Mask Register */
  __I   uint32_t                       ADC_ISR;         /**< Offset: 0x30 (R/   32) Interrupt Status Register */
  __IO  uint32_t                       ADC_LCTMR;       /**< Offset: 0x34 (R/W  32) Last Channel Trigger Mode Register */
  __IO  uint32_t                       ADC_LCCWR;       /**< Offset: 0x38 (R/W  32) Last Channel Compare Window Register */
  __I   uint32_t                       ADC_OVER;        /**< Offset: 0x3c (R/   32) Overrun Status Register */
  __IO  uint32_t                       ADC_EMR;         /**< Offset: 0x40 (R/W  32) Extended Mode Register */
  __IO  uint32_t                       ADC_CWR;         /**< Offset: 0x44 (R/W  32) Compare Window Register */
  __I   uint8_t                        Reserved3[0x04];
  __IO  uint32_t                       ADC_COR;         /**< Offset: 0x4c (R/W  32) Channel Offset Register */
  __I   uint32_t                       ADC_CDR[8];      /**< Offset: 0x50 (R/   32) Channel Data Register 0 */
  __I   uint8_t                        Reserved4[0x24];
  __IO  uint32_t                       ADC_ACR;         /**< Offset: 0x94 (R/W  32) Analog Control Register */
  __I   uint8_t                        Reserved5[0x4C];
  __IO  uint32_t                       ADC_WPMR;        /**< Offset: 0xe4 (R/W  32) Write Protection Mode Register */
  __I   uint32_t                       ADC_WPSR;        /**< Offset: 0xe8 (R/   32) Write Protection Status Register */
  __I   uint8_t                        Reserved6[0x14];
  __IO  uint32_t                       ADC_RPR;         /**< Offset: 0x100 (R/W  32) Receive Pointer Register */
  __IO  uint32_t                       ADC_RCR;         /**< Offset: 0x104 (R/W  32) Receive Counter Register */
  __I   uint8_t                        Reserved7[0x08];
  __IO  uint32_t                       ADC_RNPR;        /**< Offset: 0x110 (R/W  32) Receive Next Pointer Register */
  __IO  uint32_t                       ADC_RNCR;        /**< Offset: 0x114 (R/W  32) Receive Next Counter Register */
  __I   uint8_t                        Reserved8[0x08];
  __O   uint32_t                       ADC_PTCR;        /**< Offset: 0x120 ( /W  32) Transfer Control Register */
  __I   uint32_t                       ADC_PTSR;        /**< Offset: 0x124 (R/   32) Transfer Status Register */
} adc_registers_t;
/** @}  end of Analog-to-Digital Converter */

#endif /* SAMG_SAMG55_ADC_MODULE_H */

