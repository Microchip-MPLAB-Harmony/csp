/**
 * \brief Header file for SAMG/SAMG55 PMC
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
#ifndef SAMG_SAMG55_PMC_MODULE_H
#define SAMG_SAMG55_PMC_MODULE_H

/** \addtogroup SAMG_SAMG55 Power Management Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_PMC                                   */
/* ========================================================================== */

/* -------- PMC_SCER : (PMC Offset: 0x00) ( /W 32) System Clock Enable Register -------- */
#define PMC_SCER_UHP_Pos                      (6U)                                           /**< (PMC_SCER) USB Host Port Clock Enable Position */
#define PMC_SCER_UHP_Msk                      (0x1U << PMC_SCER_UHP_Pos)                     /**< (PMC_SCER) USB Host Port Clock Enable Mask */
#define PMC_SCER_UHP(value)                   (PMC_SCER_UHP_Msk & ((value) << PMC_SCER_UHP_Pos))
#define PMC_SCER_UDP_Pos                      (7U)                                           /**< (PMC_SCER) USB Device Port Clock Enable Position */
#define PMC_SCER_UDP_Msk                      (0x1U << PMC_SCER_UDP_Pos)                     /**< (PMC_SCER) USB Device Port Clock Enable Mask */
#define PMC_SCER_UDP(value)                   (PMC_SCER_UDP_Msk & ((value) << PMC_SCER_UDP_Pos))
#define PMC_SCER_PCK0_Pos                     (8U)                                           /**< (PMC_SCER) Programmable Clock 0 Output Enable Position */
#define PMC_SCER_PCK0_Msk                     (0x1U << PMC_SCER_PCK0_Pos)                    /**< (PMC_SCER) Programmable Clock 0 Output Enable Mask */
#define PMC_SCER_PCK0(value)                  (PMC_SCER_PCK0_Msk & ((value) << PMC_SCER_PCK0_Pos))
#define PMC_SCER_PCK1_Pos                     (9U)                                           /**< (PMC_SCER) Programmable Clock 1 Output Enable Position */
#define PMC_SCER_PCK1_Msk                     (0x1U << PMC_SCER_PCK1_Pos)                    /**< (PMC_SCER) Programmable Clock 1 Output Enable Mask */
#define PMC_SCER_PCK1(value)                  (PMC_SCER_PCK1_Msk & ((value) << PMC_SCER_PCK1_Pos))
#define PMC_SCER_PCK2_Pos                     (10U)                                          /**< (PMC_SCER) Programmable Clock 2 Output Enable Position */
#define PMC_SCER_PCK2_Msk                     (0x1U << PMC_SCER_PCK2_Pos)                    /**< (PMC_SCER) Programmable Clock 2 Output Enable Mask */
#define PMC_SCER_PCK2(value)                  (PMC_SCER_PCK2_Msk & ((value) << PMC_SCER_PCK2_Pos))
#define PMC_SCER_PCK3_Pos                     (11U)                                          /**< (PMC_SCER) Programmable Clock 3 Output Enable Position */
#define PMC_SCER_PCK3_Msk                     (0x1U << PMC_SCER_PCK3_Pos)                    /**< (PMC_SCER) Programmable Clock 3 Output Enable Mask */
#define PMC_SCER_PCK3(value)                  (PMC_SCER_PCK3_Msk & ((value) << PMC_SCER_PCK3_Pos))
#define PMC_SCER_PCK4_Pos                     (12U)                                          /**< (PMC_SCER) Programmable Clock 4 Output Enable Position */
#define PMC_SCER_PCK4_Msk                     (0x1U << PMC_SCER_PCK4_Pos)                    /**< (PMC_SCER) Programmable Clock 4 Output Enable Mask */
#define PMC_SCER_PCK4(value)                  (PMC_SCER_PCK4_Msk & ((value) << PMC_SCER_PCK4_Pos))
#define PMC_SCER_PCK5_Pos                     (13U)                                          /**< (PMC_SCER) Programmable Clock 5 Output Enable Position */
#define PMC_SCER_PCK5_Msk                     (0x1U << PMC_SCER_PCK5_Pos)                    /**< (PMC_SCER) Programmable Clock 5 Output Enable Mask */
#define PMC_SCER_PCK5(value)                  (PMC_SCER_PCK5_Msk & ((value) << PMC_SCER_PCK5_Pos))
#define PMC_SCER_PCK6_Pos                     (14U)                                          /**< (PMC_SCER) Programmable Clock 6 Output Enable Position */
#define PMC_SCER_PCK6_Msk                     (0x1U << PMC_SCER_PCK6_Pos)                    /**< (PMC_SCER) Programmable Clock 6 Output Enable Mask */
#define PMC_SCER_PCK6(value)                  (PMC_SCER_PCK6_Msk & ((value) << PMC_SCER_PCK6_Pos))
#define PMC_SCER_PCK7_Pos                     (15U)                                          /**< (PMC_SCER) Programmable Clock 7 Output Enable Position */
#define PMC_SCER_PCK7_Msk                     (0x1U << PMC_SCER_PCK7_Pos)                    /**< (PMC_SCER) Programmable Clock 7 Output Enable Mask */
#define PMC_SCER_PCK7(value)                  (PMC_SCER_PCK7_Msk & ((value) << PMC_SCER_PCK7_Pos))
#define PMC_SCER_Msk                          (0x0000FFC0UL)                                 /**< (PMC_SCER) Register Mask  */

/* -------- PMC_SCDR : (PMC Offset: 0x04) ( /W 32) System Clock Disable Register -------- */
#define PMC_SCDR_UHP_Pos                      (6U)                                           /**< (PMC_SCDR) USB Host Port Clock Disable Position */
#define PMC_SCDR_UHP_Msk                      (0x1U << PMC_SCDR_UHP_Pos)                     /**< (PMC_SCDR) USB Host Port Clock Disable Mask */
#define PMC_SCDR_UHP(value)                   (PMC_SCDR_UHP_Msk & ((value) << PMC_SCDR_UHP_Pos))
#define PMC_SCDR_UDP_Pos                      (7U)                                           /**< (PMC_SCDR)  Position */
#define PMC_SCDR_UDP_Msk                      (0x1U << PMC_SCDR_UDP_Pos)                     /**< (PMC_SCDR)  Mask */
#define PMC_SCDR_UDP(value)                   (PMC_SCDR_UDP_Msk & ((value) << PMC_SCDR_UDP_Pos))
#define PMC_SCDR_PCK0_Pos                     (8U)                                           /**< (PMC_SCDR) Programmable Clock 0 Output Disable Position */
#define PMC_SCDR_PCK0_Msk                     (0x1U << PMC_SCDR_PCK0_Pos)                    /**< (PMC_SCDR) Programmable Clock 0 Output Disable Mask */
#define PMC_SCDR_PCK0(value)                  (PMC_SCDR_PCK0_Msk & ((value) << PMC_SCDR_PCK0_Pos))
#define PMC_SCDR_PCK1_Pos                     (9U)                                           /**< (PMC_SCDR) Programmable Clock 1 Output Disable Position */
#define PMC_SCDR_PCK1_Msk                     (0x1U << PMC_SCDR_PCK1_Pos)                    /**< (PMC_SCDR) Programmable Clock 1 Output Disable Mask */
#define PMC_SCDR_PCK1(value)                  (PMC_SCDR_PCK1_Msk & ((value) << PMC_SCDR_PCK1_Pos))
#define PMC_SCDR_PCK2_Pos                     (10U)                                          /**< (PMC_SCDR) Programmable Clock 2 Output Disable Position */
#define PMC_SCDR_PCK2_Msk                     (0x1U << PMC_SCDR_PCK2_Pos)                    /**< (PMC_SCDR) Programmable Clock 2 Output Disable Mask */
#define PMC_SCDR_PCK2(value)                  (PMC_SCDR_PCK2_Msk & ((value) << PMC_SCDR_PCK2_Pos))
#define PMC_SCDR_PCK3_Pos                     (11U)                                          /**< (PMC_SCDR) Programmable Clock 3 Output Disable Position */
#define PMC_SCDR_PCK3_Msk                     (0x1U << PMC_SCDR_PCK3_Pos)                    /**< (PMC_SCDR) Programmable Clock 3 Output Disable Mask */
#define PMC_SCDR_PCK3(value)                  (PMC_SCDR_PCK3_Msk & ((value) << PMC_SCDR_PCK3_Pos))
#define PMC_SCDR_PCK4_Pos                     (12U)                                          /**< (PMC_SCDR) Programmable Clock 4 Output Disable Position */
#define PMC_SCDR_PCK4_Msk                     (0x1U << PMC_SCDR_PCK4_Pos)                    /**< (PMC_SCDR) Programmable Clock 4 Output Disable Mask */
#define PMC_SCDR_PCK4(value)                  (PMC_SCDR_PCK4_Msk & ((value) << PMC_SCDR_PCK4_Pos))
#define PMC_SCDR_PCK5_Pos                     (13U)                                          /**< (PMC_SCDR) Programmable Clock 5 Output Disable Position */
#define PMC_SCDR_PCK5_Msk                     (0x1U << PMC_SCDR_PCK5_Pos)                    /**< (PMC_SCDR) Programmable Clock 5 Output Disable Mask */
#define PMC_SCDR_PCK5(value)                  (PMC_SCDR_PCK5_Msk & ((value) << PMC_SCDR_PCK5_Pos))
#define PMC_SCDR_PCK6_Pos                     (14U)                                          /**< (PMC_SCDR) Programmable Clock 6 Output Disable Position */
#define PMC_SCDR_PCK6_Msk                     (0x1U << PMC_SCDR_PCK6_Pos)                    /**< (PMC_SCDR) Programmable Clock 6 Output Disable Mask */
#define PMC_SCDR_PCK6(value)                  (PMC_SCDR_PCK6_Msk & ((value) << PMC_SCDR_PCK6_Pos))
#define PMC_SCDR_PCK7_Pos                     (15U)                                          /**< (PMC_SCDR) Programmable Clock 7 Output Disable Position */
#define PMC_SCDR_PCK7_Msk                     (0x1U << PMC_SCDR_PCK7_Pos)                    /**< (PMC_SCDR) Programmable Clock 7 Output Disable Mask */
#define PMC_SCDR_PCK7(value)                  (PMC_SCDR_PCK7_Msk & ((value) << PMC_SCDR_PCK7_Pos))
#define PMC_SCDR_Msk                          (0x0000FFC0UL)                                 /**< (PMC_SCDR) Register Mask  */

/* -------- PMC_SCSR : (PMC Offset: 0x08) (R/  32) System Clock Status Register -------- */
#define PMC_SCSR_UHP_Pos                      (6U)                                           /**< (PMC_SCSR) USB Host Port Clock Status Position */
#define PMC_SCSR_UHP_Msk                      (0x1U << PMC_SCSR_UHP_Pos)                     /**< (PMC_SCSR) USB Host Port Clock Status Mask */
#define PMC_SCSR_UHP(value)                   (PMC_SCSR_UHP_Msk & ((value) << PMC_SCSR_UHP_Pos))
#define PMC_SCSR_UDP_Pos                      (7U)                                           /**< (PMC_SCSR)  Position */
#define PMC_SCSR_UDP_Msk                      (0x1U << PMC_SCSR_UDP_Pos)                     /**< (PMC_SCSR)  Mask */
#define PMC_SCSR_UDP(value)                   (PMC_SCSR_UDP_Msk & ((value) << PMC_SCSR_UDP_Pos))
#define PMC_SCSR_PCK0_Pos                     (8U)                                           /**< (PMC_SCSR) Programmable Clock 0 Output Status Position */
#define PMC_SCSR_PCK0_Msk                     (0x1U << PMC_SCSR_PCK0_Pos)                    /**< (PMC_SCSR) Programmable Clock 0 Output Status Mask */
#define PMC_SCSR_PCK0(value)                  (PMC_SCSR_PCK0_Msk & ((value) << PMC_SCSR_PCK0_Pos))
#define PMC_SCSR_PCK1_Pos                     (9U)                                           /**< (PMC_SCSR) Programmable Clock 1 Output Status Position */
#define PMC_SCSR_PCK1_Msk                     (0x1U << PMC_SCSR_PCK1_Pos)                    /**< (PMC_SCSR) Programmable Clock 1 Output Status Mask */
#define PMC_SCSR_PCK1(value)                  (PMC_SCSR_PCK1_Msk & ((value) << PMC_SCSR_PCK1_Pos))
#define PMC_SCSR_PCK2_Pos                     (10U)                                          /**< (PMC_SCSR) Programmable Clock 2 Output Status Position */
#define PMC_SCSR_PCK2_Msk                     (0x1U << PMC_SCSR_PCK2_Pos)                    /**< (PMC_SCSR) Programmable Clock 2 Output Status Mask */
#define PMC_SCSR_PCK2(value)                  (PMC_SCSR_PCK2_Msk & ((value) << PMC_SCSR_PCK2_Pos))
#define PMC_SCSR_PCK3_Pos                     (11U)                                          /**< (PMC_SCSR) Programmable Clock 3 Output Status Position */
#define PMC_SCSR_PCK3_Msk                     (0x1U << PMC_SCSR_PCK3_Pos)                    /**< (PMC_SCSR) Programmable Clock 3 Output Status Mask */
#define PMC_SCSR_PCK3(value)                  (PMC_SCSR_PCK3_Msk & ((value) << PMC_SCSR_PCK3_Pos))
#define PMC_SCSR_PCK4_Pos                     (12U)                                          /**< (PMC_SCSR) Programmable Clock 4 Output Status Position */
#define PMC_SCSR_PCK4_Msk                     (0x1U << PMC_SCSR_PCK4_Pos)                    /**< (PMC_SCSR) Programmable Clock 4 Output Status Mask */
#define PMC_SCSR_PCK4(value)                  (PMC_SCSR_PCK4_Msk & ((value) << PMC_SCSR_PCK4_Pos))
#define PMC_SCSR_PCK5_Pos                     (13U)                                          /**< (PMC_SCSR) Programmable Clock 5 Output Status Position */
#define PMC_SCSR_PCK5_Msk                     (0x1U << PMC_SCSR_PCK5_Pos)                    /**< (PMC_SCSR) Programmable Clock 5 Output Status Mask */
#define PMC_SCSR_PCK5(value)                  (PMC_SCSR_PCK5_Msk & ((value) << PMC_SCSR_PCK5_Pos))
#define PMC_SCSR_PCK6_Pos                     (14U)                                          /**< (PMC_SCSR) Programmable Clock 6 Output Status Position */
#define PMC_SCSR_PCK6_Msk                     (0x1U << PMC_SCSR_PCK6_Pos)                    /**< (PMC_SCSR) Programmable Clock 6 Output Status Mask */
#define PMC_SCSR_PCK6(value)                  (PMC_SCSR_PCK6_Msk & ((value) << PMC_SCSR_PCK6_Pos))
#define PMC_SCSR_PCK7_Pos                     (15U)                                          /**< (PMC_SCSR) Programmable Clock 7 Output Status Position */
#define PMC_SCSR_PCK7_Msk                     (0x1U << PMC_SCSR_PCK7_Pos)                    /**< (PMC_SCSR) Programmable Clock 7 Output Status Mask */
#define PMC_SCSR_PCK7(value)                  (PMC_SCSR_PCK7_Msk & ((value) << PMC_SCSR_PCK7_Pos))
#define PMC_SCSR_Msk                          (0x0000FFC0UL)                                 /**< (PMC_SCSR) Register Mask  */

/* -------- PMC_PCER0 : (PMC Offset: 0x10) ( /W 32) Peripheral Clock Enable Register 0 -------- */
#define PMC_PCER0_PID8_Pos                    (8U)                                           /**< (PMC_PCER0) Peripheral Clock 8 Enable Position */
#define PMC_PCER0_PID8_Msk                    (0x1U << PMC_PCER0_PID8_Pos)                   /**< (PMC_PCER0) Peripheral Clock 8 Enable Mask */
#define PMC_PCER0_PID8(value)                 (PMC_PCER0_PID8_Msk & ((value) << PMC_PCER0_PID8_Pos))
#define PMC_PCER0_PID9_Pos                    (9U)                                           /**< (PMC_PCER0) Peripheral Clock 9 Enable Position */
#define PMC_PCER0_PID9_Msk                    (0x1U << PMC_PCER0_PID9_Pos)                   /**< (PMC_PCER0) Peripheral Clock 9 Enable Mask */
#define PMC_PCER0_PID9(value)                 (PMC_PCER0_PID9_Msk & ((value) << PMC_PCER0_PID9_Pos))
#define PMC_PCER0_PID10_Pos                   (10U)                                          /**< (PMC_PCER0) Peripheral Clock 10 Enable Position */
#define PMC_PCER0_PID10_Msk                   (0x1U << PMC_PCER0_PID10_Pos)                  /**< (PMC_PCER0) Peripheral Clock 10 Enable Mask */
#define PMC_PCER0_PID10(value)                (PMC_PCER0_PID10_Msk & ((value) << PMC_PCER0_PID10_Pos))
#define PMC_PCER0_PID11_Pos                   (11U)                                          /**< (PMC_PCER0) Peripheral Clock 11 Enable Position */
#define PMC_PCER0_PID11_Msk                   (0x1U << PMC_PCER0_PID11_Pos)                  /**< (PMC_PCER0) Peripheral Clock 11 Enable Mask */
#define PMC_PCER0_PID11(value)                (PMC_PCER0_PID11_Msk & ((value) << PMC_PCER0_PID11_Pos))
#define PMC_PCER0_PID12_Pos                   (12U)                                          /**< (PMC_PCER0) Peripheral Clock 12 Enable Position */
#define PMC_PCER0_PID12_Msk                   (0x1U << PMC_PCER0_PID12_Pos)                  /**< (PMC_PCER0) Peripheral Clock 12 Enable Mask */
#define PMC_PCER0_PID12(value)                (PMC_PCER0_PID12_Msk & ((value) << PMC_PCER0_PID12_Pos))
#define PMC_PCER0_PID13_Pos                   (13U)                                          /**< (PMC_PCER0) Peripheral Clock 13 Enable Position */
#define PMC_PCER0_PID13_Msk                   (0x1U << PMC_PCER0_PID13_Pos)                  /**< (PMC_PCER0) Peripheral Clock 13 Enable Mask */
#define PMC_PCER0_PID13(value)                (PMC_PCER0_PID13_Msk & ((value) << PMC_PCER0_PID13_Pos))
#define PMC_PCER0_PID14_Pos                   (14U)                                          /**< (PMC_PCER0) Peripheral Clock 14 Enable Position */
#define PMC_PCER0_PID14_Msk                   (0x1U << PMC_PCER0_PID14_Pos)                  /**< (PMC_PCER0) Peripheral Clock 14 Enable Mask */
#define PMC_PCER0_PID14(value)                (PMC_PCER0_PID14_Msk & ((value) << PMC_PCER0_PID14_Pos))
#define PMC_PCER0_PID15_Pos                   (15U)                                          /**< (PMC_PCER0) Peripheral Clock 15 Enable Position */
#define PMC_PCER0_PID15_Msk                   (0x1U << PMC_PCER0_PID15_Pos)                  /**< (PMC_PCER0) Peripheral Clock 15 Enable Mask */
#define PMC_PCER0_PID15(value)                (PMC_PCER0_PID15_Msk & ((value) << PMC_PCER0_PID15_Pos))
#define PMC_PCER0_PID16_Pos                   (16U)                                          /**< (PMC_PCER0) Peripheral Clock 16 Enable Position */
#define PMC_PCER0_PID16_Msk                   (0x1U << PMC_PCER0_PID16_Pos)                  /**< (PMC_PCER0) Peripheral Clock 16 Enable Mask */
#define PMC_PCER0_PID16(value)                (PMC_PCER0_PID16_Msk & ((value) << PMC_PCER0_PID16_Pos))
#define PMC_PCER0_PID17_Pos                   (17U)                                          /**< (PMC_PCER0) Peripheral Clock 17 Enable Position */
#define PMC_PCER0_PID17_Msk                   (0x1U << PMC_PCER0_PID17_Pos)                  /**< (PMC_PCER0) Peripheral Clock 17 Enable Mask */
#define PMC_PCER0_PID17(value)                (PMC_PCER0_PID17_Msk & ((value) << PMC_PCER0_PID17_Pos))
#define PMC_PCER0_PID18_Pos                   (18U)                                          /**< (PMC_PCER0) Peripheral Clock 18 Enable Position */
#define PMC_PCER0_PID18_Msk                   (0x1U << PMC_PCER0_PID18_Pos)                  /**< (PMC_PCER0) Peripheral Clock 18 Enable Mask */
#define PMC_PCER0_PID18(value)                (PMC_PCER0_PID18_Msk & ((value) << PMC_PCER0_PID18_Pos))
#define PMC_PCER0_PID19_Pos                   (19U)                                          /**< (PMC_PCER0) Peripheral Clock 19 Enable Position */
#define PMC_PCER0_PID19_Msk                   (0x1U << PMC_PCER0_PID19_Pos)                  /**< (PMC_PCER0) Peripheral Clock 19 Enable Mask */
#define PMC_PCER0_PID19(value)                (PMC_PCER0_PID19_Msk & ((value) << PMC_PCER0_PID19_Pos))
#define PMC_PCER0_PID20_Pos                   (20U)                                          /**< (PMC_PCER0) Peripheral Clock 20 Enable Position */
#define PMC_PCER0_PID20_Msk                   (0x1U << PMC_PCER0_PID20_Pos)                  /**< (PMC_PCER0) Peripheral Clock 20 Enable Mask */
#define PMC_PCER0_PID20(value)                (PMC_PCER0_PID20_Msk & ((value) << PMC_PCER0_PID20_Pos))
#define PMC_PCER0_PID21_Pos                   (21U)                                          /**< (PMC_PCER0) Peripheral Clock 21 Enable Position */
#define PMC_PCER0_PID21_Msk                   (0x1U << PMC_PCER0_PID21_Pos)                  /**< (PMC_PCER0) Peripheral Clock 21 Enable Mask */
#define PMC_PCER0_PID21(value)                (PMC_PCER0_PID21_Msk & ((value) << PMC_PCER0_PID21_Pos))
#define PMC_PCER0_PID22_Pos                   (22U)                                          /**< (PMC_PCER0) Peripheral Clock 22 Enable Position */
#define PMC_PCER0_PID22_Msk                   (0x1U << PMC_PCER0_PID22_Pos)                  /**< (PMC_PCER0) Peripheral Clock 22 Enable Mask */
#define PMC_PCER0_PID22(value)                (PMC_PCER0_PID22_Msk & ((value) << PMC_PCER0_PID22_Pos))
#define PMC_PCER0_PID23_Pos                   (23U)                                          /**< (PMC_PCER0) Peripheral Clock 23 Enable Position */
#define PMC_PCER0_PID23_Msk                   (0x1U << PMC_PCER0_PID23_Pos)                  /**< (PMC_PCER0) Peripheral Clock 23 Enable Mask */
#define PMC_PCER0_PID23(value)                (PMC_PCER0_PID23_Msk & ((value) << PMC_PCER0_PID23_Pos))
#define PMC_PCER0_PID24_Pos                   (24U)                                          /**< (PMC_PCER0) Peripheral Clock 24 Enable Position */
#define PMC_PCER0_PID24_Msk                   (0x1U << PMC_PCER0_PID24_Pos)                  /**< (PMC_PCER0) Peripheral Clock 24 Enable Mask */
#define PMC_PCER0_PID24(value)                (PMC_PCER0_PID24_Msk & ((value) << PMC_PCER0_PID24_Pos))
#define PMC_PCER0_PID25_Pos                   (25U)                                          /**< (PMC_PCER0) Peripheral Clock 25 Enable Position */
#define PMC_PCER0_PID25_Msk                   (0x1U << PMC_PCER0_PID25_Pos)                  /**< (PMC_PCER0) Peripheral Clock 25 Enable Mask */
#define PMC_PCER0_PID25(value)                (PMC_PCER0_PID25_Msk & ((value) << PMC_PCER0_PID25_Pos))
#define PMC_PCER0_PID26_Pos                   (26U)                                          /**< (PMC_PCER0) Peripheral Clock 26 Enable Position */
#define PMC_PCER0_PID26_Msk                   (0x1U << PMC_PCER0_PID26_Pos)                  /**< (PMC_PCER0) Peripheral Clock 26 Enable Mask */
#define PMC_PCER0_PID26(value)                (PMC_PCER0_PID26_Msk & ((value) << PMC_PCER0_PID26_Pos))
#define PMC_PCER0_PID27_Pos                   (27U)                                          /**< (PMC_PCER0) Peripheral Clock 27 Enable Position */
#define PMC_PCER0_PID27_Msk                   (0x1U << PMC_PCER0_PID27_Pos)                  /**< (PMC_PCER0) Peripheral Clock 27 Enable Mask */
#define PMC_PCER0_PID27(value)                (PMC_PCER0_PID27_Msk & ((value) << PMC_PCER0_PID27_Pos))
#define PMC_PCER0_PID28_Pos                   (28U)                                          /**< (PMC_PCER0) Peripheral Clock 28 Enable Position */
#define PMC_PCER0_PID28_Msk                   (0x1U << PMC_PCER0_PID28_Pos)                  /**< (PMC_PCER0) Peripheral Clock 28 Enable Mask */
#define PMC_PCER0_PID28(value)                (PMC_PCER0_PID28_Msk & ((value) << PMC_PCER0_PID28_Pos))
#define PMC_PCER0_PID29_Pos                   (29U)                                          /**< (PMC_PCER0) Peripheral Clock 29 Enable Position */
#define PMC_PCER0_PID29_Msk                   (0x1U << PMC_PCER0_PID29_Pos)                  /**< (PMC_PCER0) Peripheral Clock 29 Enable Mask */
#define PMC_PCER0_PID29(value)                (PMC_PCER0_PID29_Msk & ((value) << PMC_PCER0_PID29_Pos))
#define PMC_PCER0_Msk                         (0x3FFFFF00UL)                                 /**< (PMC_PCER0) Register Mask  */

/* -------- PMC_PCDR0 : (PMC Offset: 0x14) ( /W 32) Peripheral Clock Disable Register 0 -------- */
#define PMC_PCDR0_PID8_Pos                    (8U)                                           /**< (PMC_PCDR0) Peripheral Clock 8 Disable Position */
#define PMC_PCDR0_PID8_Msk                    (0x1U << PMC_PCDR0_PID8_Pos)                   /**< (PMC_PCDR0) Peripheral Clock 8 Disable Mask */
#define PMC_PCDR0_PID8(value)                 (PMC_PCDR0_PID8_Msk & ((value) << PMC_PCDR0_PID8_Pos))
#define PMC_PCDR0_PID9_Pos                    (9U)                                           /**< (PMC_PCDR0) Peripheral Clock 9 Disable Position */
#define PMC_PCDR0_PID9_Msk                    (0x1U << PMC_PCDR0_PID9_Pos)                   /**< (PMC_PCDR0) Peripheral Clock 9 Disable Mask */
#define PMC_PCDR0_PID9(value)                 (PMC_PCDR0_PID9_Msk & ((value) << PMC_PCDR0_PID9_Pos))
#define PMC_PCDR0_PID10_Pos                   (10U)                                          /**< (PMC_PCDR0) Peripheral Clock 10 Disable Position */
#define PMC_PCDR0_PID10_Msk                   (0x1U << PMC_PCDR0_PID10_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 10 Disable Mask */
#define PMC_PCDR0_PID10(value)                (PMC_PCDR0_PID10_Msk & ((value) << PMC_PCDR0_PID10_Pos))
#define PMC_PCDR0_PID11_Pos                   (11U)                                          /**< (PMC_PCDR0) Peripheral Clock 11 Disable Position */
#define PMC_PCDR0_PID11_Msk                   (0x1U << PMC_PCDR0_PID11_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 11 Disable Mask */
#define PMC_PCDR0_PID11(value)                (PMC_PCDR0_PID11_Msk & ((value) << PMC_PCDR0_PID11_Pos))
#define PMC_PCDR0_PID12_Pos                   (12U)                                          /**< (PMC_PCDR0) Peripheral Clock 12 Disable Position */
#define PMC_PCDR0_PID12_Msk                   (0x1U << PMC_PCDR0_PID12_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 12 Disable Mask */
#define PMC_PCDR0_PID12(value)                (PMC_PCDR0_PID12_Msk & ((value) << PMC_PCDR0_PID12_Pos))
#define PMC_PCDR0_PID13_Pos                   (13U)                                          /**< (PMC_PCDR0) Peripheral Clock 13 Disable Position */
#define PMC_PCDR0_PID13_Msk                   (0x1U << PMC_PCDR0_PID13_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 13 Disable Mask */
#define PMC_PCDR0_PID13(value)                (PMC_PCDR0_PID13_Msk & ((value) << PMC_PCDR0_PID13_Pos))
#define PMC_PCDR0_PID14_Pos                   (14U)                                          /**< (PMC_PCDR0) Peripheral Clock 14 Disable Position */
#define PMC_PCDR0_PID14_Msk                   (0x1U << PMC_PCDR0_PID14_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 14 Disable Mask */
#define PMC_PCDR0_PID14(value)                (PMC_PCDR0_PID14_Msk & ((value) << PMC_PCDR0_PID14_Pos))
#define PMC_PCDR0_PID15_Pos                   (15U)                                          /**< (PMC_PCDR0) Peripheral Clock 15 Disable Position */
#define PMC_PCDR0_PID15_Msk                   (0x1U << PMC_PCDR0_PID15_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 15 Disable Mask */
#define PMC_PCDR0_PID15(value)                (PMC_PCDR0_PID15_Msk & ((value) << PMC_PCDR0_PID15_Pos))
#define PMC_PCDR0_PID16_Pos                   (16U)                                          /**< (PMC_PCDR0) Peripheral Clock 16 Disable Position */
#define PMC_PCDR0_PID16_Msk                   (0x1U << PMC_PCDR0_PID16_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 16 Disable Mask */
#define PMC_PCDR0_PID16(value)                (PMC_PCDR0_PID16_Msk & ((value) << PMC_PCDR0_PID16_Pos))
#define PMC_PCDR0_PID17_Pos                   (17U)                                          /**< (PMC_PCDR0) Peripheral Clock 17 Disable Position */
#define PMC_PCDR0_PID17_Msk                   (0x1U << PMC_PCDR0_PID17_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 17 Disable Mask */
#define PMC_PCDR0_PID17(value)                (PMC_PCDR0_PID17_Msk & ((value) << PMC_PCDR0_PID17_Pos))
#define PMC_PCDR0_PID18_Pos                   (18U)                                          /**< (PMC_PCDR0) Peripheral Clock 18 Disable Position */
#define PMC_PCDR0_PID18_Msk                   (0x1U << PMC_PCDR0_PID18_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 18 Disable Mask */
#define PMC_PCDR0_PID18(value)                (PMC_PCDR0_PID18_Msk & ((value) << PMC_PCDR0_PID18_Pos))
#define PMC_PCDR0_PID19_Pos                   (19U)                                          /**< (PMC_PCDR0) Peripheral Clock 19 Disable Position */
#define PMC_PCDR0_PID19_Msk                   (0x1U << PMC_PCDR0_PID19_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 19 Disable Mask */
#define PMC_PCDR0_PID19(value)                (PMC_PCDR0_PID19_Msk & ((value) << PMC_PCDR0_PID19_Pos))
#define PMC_PCDR0_PID20_Pos                   (20U)                                          /**< (PMC_PCDR0) Peripheral Clock 20 Disable Position */
#define PMC_PCDR0_PID20_Msk                   (0x1U << PMC_PCDR0_PID20_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 20 Disable Mask */
#define PMC_PCDR0_PID20(value)                (PMC_PCDR0_PID20_Msk & ((value) << PMC_PCDR0_PID20_Pos))
#define PMC_PCDR0_PID21_Pos                   (21U)                                          /**< (PMC_PCDR0) Peripheral Clock 21 Disable Position */
#define PMC_PCDR0_PID21_Msk                   (0x1U << PMC_PCDR0_PID21_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 21 Disable Mask */
#define PMC_PCDR0_PID21(value)                (PMC_PCDR0_PID21_Msk & ((value) << PMC_PCDR0_PID21_Pos))
#define PMC_PCDR0_PID22_Pos                   (22U)                                          /**< (PMC_PCDR0) Peripheral Clock 22 Disable Position */
#define PMC_PCDR0_PID22_Msk                   (0x1U << PMC_PCDR0_PID22_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 22 Disable Mask */
#define PMC_PCDR0_PID22(value)                (PMC_PCDR0_PID22_Msk & ((value) << PMC_PCDR0_PID22_Pos))
#define PMC_PCDR0_PID23_Pos                   (23U)                                          /**< (PMC_PCDR0) Peripheral Clock 23 Disable Position */
#define PMC_PCDR0_PID23_Msk                   (0x1U << PMC_PCDR0_PID23_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 23 Disable Mask */
#define PMC_PCDR0_PID23(value)                (PMC_PCDR0_PID23_Msk & ((value) << PMC_PCDR0_PID23_Pos))
#define PMC_PCDR0_PID24_Pos                   (24U)                                          /**< (PMC_PCDR0) Peripheral Clock 24 Disable Position */
#define PMC_PCDR0_PID24_Msk                   (0x1U << PMC_PCDR0_PID24_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 24 Disable Mask */
#define PMC_PCDR0_PID24(value)                (PMC_PCDR0_PID24_Msk & ((value) << PMC_PCDR0_PID24_Pos))
#define PMC_PCDR0_PID25_Pos                   (25U)                                          /**< (PMC_PCDR0) Peripheral Clock 25 Disable Position */
#define PMC_PCDR0_PID25_Msk                   (0x1U << PMC_PCDR0_PID25_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 25 Disable Mask */
#define PMC_PCDR0_PID25(value)                (PMC_PCDR0_PID25_Msk & ((value) << PMC_PCDR0_PID25_Pos))
#define PMC_PCDR0_PID26_Pos                   (26U)                                          /**< (PMC_PCDR0) Peripheral Clock 26 Disable Position */
#define PMC_PCDR0_PID26_Msk                   (0x1U << PMC_PCDR0_PID26_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 26 Disable Mask */
#define PMC_PCDR0_PID26(value)                (PMC_PCDR0_PID26_Msk & ((value) << PMC_PCDR0_PID26_Pos))
#define PMC_PCDR0_PID27_Pos                   (27U)                                          /**< (PMC_PCDR0) Peripheral Clock 27 Disable Position */
#define PMC_PCDR0_PID27_Msk                   (0x1U << PMC_PCDR0_PID27_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 27 Disable Mask */
#define PMC_PCDR0_PID27(value)                (PMC_PCDR0_PID27_Msk & ((value) << PMC_PCDR0_PID27_Pos))
#define PMC_PCDR0_PID28_Pos                   (28U)                                          /**< (PMC_PCDR0) Peripheral Clock 28 Disable Position */
#define PMC_PCDR0_PID28_Msk                   (0x1U << PMC_PCDR0_PID28_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 28 Disable Mask */
#define PMC_PCDR0_PID28(value)                (PMC_PCDR0_PID28_Msk & ((value) << PMC_PCDR0_PID28_Pos))
#define PMC_PCDR0_PID29_Pos                   (29U)                                          /**< (PMC_PCDR0) Peripheral Clock 29 Disable Position */
#define PMC_PCDR0_PID29_Msk                   (0x1U << PMC_PCDR0_PID29_Pos)                  /**< (PMC_PCDR0) Peripheral Clock 29 Disable Mask */
#define PMC_PCDR0_PID29(value)                (PMC_PCDR0_PID29_Msk & ((value) << PMC_PCDR0_PID29_Pos))
#define PMC_PCDR0_Msk                         (0x3FFFFF00UL)                                 /**< (PMC_PCDR0) Register Mask  */

/* -------- PMC_PCSR0 : (PMC Offset: 0x18) (R/  32) Peripheral Clock Status Register 0 -------- */
#define PMC_PCSR0_PID8_Pos                    (8U)                                           /**< (PMC_PCSR0) Peripheral Clock 8 Status Position */
#define PMC_PCSR0_PID8_Msk                    (0x1U << PMC_PCSR0_PID8_Pos)                   /**< (PMC_PCSR0) Peripheral Clock 8 Status Mask */
#define PMC_PCSR0_PID8(value)                 (PMC_PCSR0_PID8_Msk & ((value) << PMC_PCSR0_PID8_Pos))
#define PMC_PCSR0_PID9_Pos                    (9U)                                           /**< (PMC_PCSR0) Peripheral Clock 9 Status Position */
#define PMC_PCSR0_PID9_Msk                    (0x1U << PMC_PCSR0_PID9_Pos)                   /**< (PMC_PCSR0) Peripheral Clock 9 Status Mask */
#define PMC_PCSR0_PID9(value)                 (PMC_PCSR0_PID9_Msk & ((value) << PMC_PCSR0_PID9_Pos))
#define PMC_PCSR0_PID10_Pos                   (10U)                                          /**< (PMC_PCSR0) Peripheral Clock 10 Status Position */
#define PMC_PCSR0_PID10_Msk                   (0x1U << PMC_PCSR0_PID10_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 10 Status Mask */
#define PMC_PCSR0_PID10(value)                (PMC_PCSR0_PID10_Msk & ((value) << PMC_PCSR0_PID10_Pos))
#define PMC_PCSR0_PID11_Pos                   (11U)                                          /**< (PMC_PCSR0) Peripheral Clock 11 Status Position */
#define PMC_PCSR0_PID11_Msk                   (0x1U << PMC_PCSR0_PID11_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 11 Status Mask */
#define PMC_PCSR0_PID11(value)                (PMC_PCSR0_PID11_Msk & ((value) << PMC_PCSR0_PID11_Pos))
#define PMC_PCSR0_PID12_Pos                   (12U)                                          /**< (PMC_PCSR0) Peripheral Clock 12 Status Position */
#define PMC_PCSR0_PID12_Msk                   (0x1U << PMC_PCSR0_PID12_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 12 Status Mask */
#define PMC_PCSR0_PID12(value)                (PMC_PCSR0_PID12_Msk & ((value) << PMC_PCSR0_PID12_Pos))
#define PMC_PCSR0_PID13_Pos                   (13U)                                          /**< (PMC_PCSR0) Peripheral Clock 13 Status Position */
#define PMC_PCSR0_PID13_Msk                   (0x1U << PMC_PCSR0_PID13_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 13 Status Mask */
#define PMC_PCSR0_PID13(value)                (PMC_PCSR0_PID13_Msk & ((value) << PMC_PCSR0_PID13_Pos))
#define PMC_PCSR0_PID14_Pos                   (14U)                                          /**< (PMC_PCSR0) Peripheral Clock 14 Status Position */
#define PMC_PCSR0_PID14_Msk                   (0x1U << PMC_PCSR0_PID14_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 14 Status Mask */
#define PMC_PCSR0_PID14(value)                (PMC_PCSR0_PID14_Msk & ((value) << PMC_PCSR0_PID14_Pos))
#define PMC_PCSR0_PID15_Pos                   (15U)                                          /**< (PMC_PCSR0) Peripheral Clock 15 Status Position */
#define PMC_PCSR0_PID15_Msk                   (0x1U << PMC_PCSR0_PID15_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 15 Status Mask */
#define PMC_PCSR0_PID15(value)                (PMC_PCSR0_PID15_Msk & ((value) << PMC_PCSR0_PID15_Pos))
#define PMC_PCSR0_PID16_Pos                   (16U)                                          /**< (PMC_PCSR0) Peripheral Clock 16 Status Position */
#define PMC_PCSR0_PID16_Msk                   (0x1U << PMC_PCSR0_PID16_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 16 Status Mask */
#define PMC_PCSR0_PID16(value)                (PMC_PCSR0_PID16_Msk & ((value) << PMC_PCSR0_PID16_Pos))
#define PMC_PCSR0_PID17_Pos                   (17U)                                          /**< (PMC_PCSR0) Peripheral Clock 17 Status Position */
#define PMC_PCSR0_PID17_Msk                   (0x1U << PMC_PCSR0_PID17_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 17 Status Mask */
#define PMC_PCSR0_PID17(value)                (PMC_PCSR0_PID17_Msk & ((value) << PMC_PCSR0_PID17_Pos))
#define PMC_PCSR0_PID18_Pos                   (18U)                                          /**< (PMC_PCSR0) Peripheral Clock 18 Status Position */
#define PMC_PCSR0_PID18_Msk                   (0x1U << PMC_PCSR0_PID18_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 18 Status Mask */
#define PMC_PCSR0_PID18(value)                (PMC_PCSR0_PID18_Msk & ((value) << PMC_PCSR0_PID18_Pos))
#define PMC_PCSR0_PID19_Pos                   (19U)                                          /**< (PMC_PCSR0) Peripheral Clock 19 Status Position */
#define PMC_PCSR0_PID19_Msk                   (0x1U << PMC_PCSR0_PID19_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 19 Status Mask */
#define PMC_PCSR0_PID19(value)                (PMC_PCSR0_PID19_Msk & ((value) << PMC_PCSR0_PID19_Pos))
#define PMC_PCSR0_PID20_Pos                   (20U)                                          /**< (PMC_PCSR0) Peripheral Clock 20 Status Position */
#define PMC_PCSR0_PID20_Msk                   (0x1U << PMC_PCSR0_PID20_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 20 Status Mask */
#define PMC_PCSR0_PID20(value)                (PMC_PCSR0_PID20_Msk & ((value) << PMC_PCSR0_PID20_Pos))
#define PMC_PCSR0_PID21_Pos                   (21U)                                          /**< (PMC_PCSR0) Peripheral Clock 21 Status Position */
#define PMC_PCSR0_PID21_Msk                   (0x1U << PMC_PCSR0_PID21_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 21 Status Mask */
#define PMC_PCSR0_PID21(value)                (PMC_PCSR0_PID21_Msk & ((value) << PMC_PCSR0_PID21_Pos))
#define PMC_PCSR0_PID22_Pos                   (22U)                                          /**< (PMC_PCSR0) Peripheral Clock 22 Status Position */
#define PMC_PCSR0_PID22_Msk                   (0x1U << PMC_PCSR0_PID22_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 22 Status Mask */
#define PMC_PCSR0_PID22(value)                (PMC_PCSR0_PID22_Msk & ((value) << PMC_PCSR0_PID22_Pos))
#define PMC_PCSR0_PID23_Pos                   (23U)                                          /**< (PMC_PCSR0) Peripheral Clock 23 Status Position */
#define PMC_PCSR0_PID23_Msk                   (0x1U << PMC_PCSR0_PID23_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 23 Status Mask */
#define PMC_PCSR0_PID23(value)                (PMC_PCSR0_PID23_Msk & ((value) << PMC_PCSR0_PID23_Pos))
#define PMC_PCSR0_PID24_Pos                   (24U)                                          /**< (PMC_PCSR0) Peripheral Clock 24 Status Position */
#define PMC_PCSR0_PID24_Msk                   (0x1U << PMC_PCSR0_PID24_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 24 Status Mask */
#define PMC_PCSR0_PID24(value)                (PMC_PCSR0_PID24_Msk & ((value) << PMC_PCSR0_PID24_Pos))
#define PMC_PCSR0_PID25_Pos                   (25U)                                          /**< (PMC_PCSR0) Peripheral Clock 25 Status Position */
#define PMC_PCSR0_PID25_Msk                   (0x1U << PMC_PCSR0_PID25_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 25 Status Mask */
#define PMC_PCSR0_PID25(value)                (PMC_PCSR0_PID25_Msk & ((value) << PMC_PCSR0_PID25_Pos))
#define PMC_PCSR0_PID26_Pos                   (26U)                                          /**< (PMC_PCSR0) Peripheral Clock 26 Status Position */
#define PMC_PCSR0_PID26_Msk                   (0x1U << PMC_PCSR0_PID26_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 26 Status Mask */
#define PMC_PCSR0_PID26(value)                (PMC_PCSR0_PID26_Msk & ((value) << PMC_PCSR0_PID26_Pos))
#define PMC_PCSR0_PID27_Pos                   (27U)                                          /**< (PMC_PCSR0) Peripheral Clock 27 Status Position */
#define PMC_PCSR0_PID27_Msk                   (0x1U << PMC_PCSR0_PID27_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 27 Status Mask */
#define PMC_PCSR0_PID27(value)                (PMC_PCSR0_PID27_Msk & ((value) << PMC_PCSR0_PID27_Pos))
#define PMC_PCSR0_PID28_Pos                   (28U)                                          /**< (PMC_PCSR0) Peripheral Clock 28 Status Position */
#define PMC_PCSR0_PID28_Msk                   (0x1U << PMC_PCSR0_PID28_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 28 Status Mask */
#define PMC_PCSR0_PID28(value)                (PMC_PCSR0_PID28_Msk & ((value) << PMC_PCSR0_PID28_Pos))
#define PMC_PCSR0_PID29_Pos                   (29U)                                          /**< (PMC_PCSR0) Peripheral Clock 29 Status Position */
#define PMC_PCSR0_PID29_Msk                   (0x1U << PMC_PCSR0_PID29_Pos)                  /**< (PMC_PCSR0) Peripheral Clock 29 Status Mask */
#define PMC_PCSR0_PID29(value)                (PMC_PCSR0_PID29_Msk & ((value) << PMC_PCSR0_PID29_Pos))
#define PMC_PCSR0_Msk                         (0x3FFFFF00UL)                                 /**< (PMC_PCSR0) Register Mask  */

/* -------- CKGR_MOR : (PMC Offset: 0x20) (R/W 32) Main Oscillator Register -------- */
#define CKGR_MOR_MOSCXTEN_Pos                 (0U)                                           /**< (CKGR_MOR) Main Crystal Oscillator Enable Position */
#define CKGR_MOR_MOSCXTEN_Msk                 (0x1U << CKGR_MOR_MOSCXTEN_Pos)                /**< (CKGR_MOR) Main Crystal Oscillator Enable Mask */
#define CKGR_MOR_MOSCXTEN(value)              (CKGR_MOR_MOSCXTEN_Msk & ((value) << CKGR_MOR_MOSCXTEN_Pos))
#define CKGR_MOR_MOSCXTBY_Pos                 (1U)                                           /**< (CKGR_MOR) Main Crystal Oscillator Bypass Position */
#define CKGR_MOR_MOSCXTBY_Msk                 (0x1U << CKGR_MOR_MOSCXTBY_Pos)                /**< (CKGR_MOR) Main Crystal Oscillator Bypass Mask */
#define CKGR_MOR_MOSCXTBY(value)              (CKGR_MOR_MOSCXTBY_Msk & ((value) << CKGR_MOR_MOSCXTBY_Pos))
#define CKGR_MOR_WAITMODE_Pos                 (2U)                                           /**< (CKGR_MOR) Wait Mode Command (Write-only) Position */
#define CKGR_MOR_WAITMODE_Msk                 (0x1U << CKGR_MOR_WAITMODE_Pos)                /**< (CKGR_MOR) Wait Mode Command (Write-only) Mask */
#define CKGR_MOR_WAITMODE(value)              (CKGR_MOR_WAITMODE_Msk & ((value) << CKGR_MOR_WAITMODE_Pos))
#define CKGR_MOR_MOSCRCEN_Pos                 (3U)                                           /**< (CKGR_MOR) Main On-Chip RC Oscillator Enable Position */
#define CKGR_MOR_MOSCRCEN_Msk                 (0x1U << CKGR_MOR_MOSCRCEN_Pos)                /**< (CKGR_MOR) Main On-Chip RC Oscillator Enable Mask */
#define CKGR_MOR_MOSCRCEN(value)              (CKGR_MOR_MOSCRCEN_Msk & ((value) << CKGR_MOR_MOSCRCEN_Pos))
#define CKGR_MOR_MOSCRCF_Pos                  (4U)                                           /**< (CKGR_MOR) Main On-Chip RC Oscillator Frequency Selection Position */
#define CKGR_MOR_MOSCRCF_Msk                  (0x7U << CKGR_MOR_MOSCRCF_Pos)                 /**< (CKGR_MOR) Main On-Chip RC Oscillator Frequency Selection Mask */
#define CKGR_MOR_MOSCRCF(value)               (CKGR_MOR_MOSCRCF_Msk & ((value) << CKGR_MOR_MOSCRCF_Pos))
#define   CKGR_MOR_MOSCRCF_8_MHz_Val          (0U)                                           /**< (CKGR_MOR) The Fast RC Oscillator frequency is at 8 MHz (default)  */
#define   CKGR_MOR_MOSCRCF_16_MHz_Val         (1U)                                           /**< (CKGR_MOR) The Fast RC Oscillator frequency is at 16 MHz  */
#define   CKGR_MOR_MOSCRCF_24_MHz_Val         (2U)                                           /**< (CKGR_MOR) The Fast RC Oscillator frequency is at 24 MHz  */
#define CKGR_MOR_MOSCRCF_8_MHz                (CKGR_MOR_MOSCRCF_8_MHz_Val << CKGR_MOR_MOSCRCF_Pos) /**< (CKGR_MOR) The Fast RC Oscillator frequency is at 8 MHz (default) Position  */
#define CKGR_MOR_MOSCRCF_16_MHz               (CKGR_MOR_MOSCRCF_16_MHz_Val << CKGR_MOR_MOSCRCF_Pos) /**< (CKGR_MOR) The Fast RC Oscillator frequency is at 16 MHz Position  */
#define CKGR_MOR_MOSCRCF_24_MHz               (CKGR_MOR_MOSCRCF_24_MHz_Val << CKGR_MOR_MOSCRCF_Pos) /**< (CKGR_MOR) The Fast RC Oscillator frequency is at 24 MHz Position  */
#define CKGR_MOR_MOSCXTST_Pos                 (8U)                                           /**< (CKGR_MOR) Main Crystal Oscillator Start-up Time Position */
#define CKGR_MOR_MOSCXTST_Msk                 (0xFFU << CKGR_MOR_MOSCXTST_Pos)               /**< (CKGR_MOR) Main Crystal Oscillator Start-up Time Mask */
#define CKGR_MOR_MOSCXTST(value)              (CKGR_MOR_MOSCXTST_Msk & ((value) << CKGR_MOR_MOSCXTST_Pos))
#define CKGR_MOR_KEY_Pos                      (16U)                                          /**< (CKGR_MOR) Write Access Password Position */
#define CKGR_MOR_KEY_Msk                      (0xFFU << CKGR_MOR_KEY_Pos)                    /**< (CKGR_MOR) Write Access Password Mask */
#define CKGR_MOR_KEY(value)                   (CKGR_MOR_KEY_Msk & ((value) << CKGR_MOR_KEY_Pos))
#define   CKGR_MOR_KEY_PASSWD_Val             (55U)                                          /**< (CKGR_MOR) Writing any other value in this field aborts the write operation.Always reads as 0.  */
#define CKGR_MOR_KEY_PASSWD                   (CKGR_MOR_KEY_PASSWD_Val << CKGR_MOR_KEY_Pos)  /**< (CKGR_MOR) Writing any other value in this field aborts the write operation.Always reads as 0. Position  */
#define CKGR_MOR_MOSCSEL_Pos                  (24U)                                          /**< (CKGR_MOR) Main Oscillator Selection Position */
#define CKGR_MOR_MOSCSEL_Msk                  (0x1U << CKGR_MOR_MOSCSEL_Pos)                 /**< (CKGR_MOR) Main Oscillator Selection Mask */
#define CKGR_MOR_MOSCSEL(value)               (CKGR_MOR_MOSCSEL_Msk & ((value) << CKGR_MOR_MOSCSEL_Pos))
#define CKGR_MOR_CFDEN_Pos                    (25U)                                          /**< (CKGR_MOR) Clock Failure Detector Enable Position */
#define CKGR_MOR_CFDEN_Msk                    (0x1U << CKGR_MOR_CFDEN_Pos)                   /**< (CKGR_MOR) Clock Failure Detector Enable Mask */
#define CKGR_MOR_CFDEN(value)                 (CKGR_MOR_CFDEN_Msk & ((value) << CKGR_MOR_CFDEN_Pos))
#define CKGR_MOR_Msk                          (0x03FFFF7FUL)                                 /**< (CKGR_MOR) Register Mask  */

/* -------- CKGR_MCFR : (PMC Offset: 0x24) (R/W 32) Main Clock Frequency Register -------- */
#define CKGR_MCFR_MAINF_Pos                   (0U)                                           /**< (CKGR_MCFR) Main Clock Frequency Position */
#define CKGR_MCFR_MAINF_Msk                   (0xFFFFU << CKGR_MCFR_MAINF_Pos)               /**< (CKGR_MCFR) Main Clock Frequency Mask */
#define CKGR_MCFR_MAINF(value)                (CKGR_MCFR_MAINF_Msk & ((value) << CKGR_MCFR_MAINF_Pos))
#define CKGR_MCFR_MAINFRDY_Pos                (16U)                                          /**< (CKGR_MCFR) Main Clock Frequency Measure Ready Position */
#define CKGR_MCFR_MAINFRDY_Msk                (0x1U << CKGR_MCFR_MAINFRDY_Pos)               /**< (CKGR_MCFR) Main Clock Frequency Measure Ready Mask */
#define CKGR_MCFR_MAINFRDY(value)             (CKGR_MCFR_MAINFRDY_Msk & ((value) << CKGR_MCFR_MAINFRDY_Pos))
#define CKGR_MCFR_RCMEAS_Pos                  (20U)                                          /**< (CKGR_MCFR) RC Oscillator Frequency Measure (write-only) Position */
#define CKGR_MCFR_RCMEAS_Msk                  (0x1U << CKGR_MCFR_RCMEAS_Pos)                 /**< (CKGR_MCFR) RC Oscillator Frequency Measure (write-only) Mask */
#define CKGR_MCFR_RCMEAS(value)               (CKGR_MCFR_RCMEAS_Msk & ((value) << CKGR_MCFR_RCMEAS_Pos))
#define CKGR_MCFR_Msk                         (0x0011FFFFUL)                                 /**< (CKGR_MCFR) Register Mask  */

/* -------- CKGR_PLLAR : (PMC Offset: 0x28) (R/W 32) PLLA Register -------- */
#define CKGR_PLLAR_PLLAEN_Pos                 (0U)                                           /**< (CKGR_PLLAR) PLLA Control Position */
#define CKGR_PLLAR_PLLAEN_Msk                 (0xFFU << CKGR_PLLAR_PLLAEN_Pos)               /**< (CKGR_PLLAR) PLLA Control Mask */
#define CKGR_PLLAR_PLLAEN(value)              (CKGR_PLLAR_PLLAEN_Msk & ((value) << CKGR_PLLAR_PLLAEN_Pos))
#define CKGR_PLLAR_PLLACOUNT_Pos              (8U)                                           /**< (CKGR_PLLAR) PLLA Counter Position */
#define CKGR_PLLAR_PLLACOUNT_Msk              (0x3FU << CKGR_PLLAR_PLLACOUNT_Pos)            /**< (CKGR_PLLAR) PLLA Counter Mask */
#define CKGR_PLLAR_PLLACOUNT(value)           (CKGR_PLLAR_PLLACOUNT_Msk & ((value) << CKGR_PLLAR_PLLACOUNT_Pos))
#define CKGR_PLLAR_MULA_Pos                   (16U)                                          /**< (CKGR_PLLAR) PLLA Multiplier Position */
#define CKGR_PLLAR_MULA_Msk                   (0x1FFFU << CKGR_PLLAR_MULA_Pos)               /**< (CKGR_PLLAR) PLLA Multiplier Mask */
#define CKGR_PLLAR_MULA(value)                (CKGR_PLLAR_MULA_Msk & ((value) << CKGR_PLLAR_MULA_Pos))
#define CKGR_PLLAR_ZERO_Pos                   (29U)                                          /**< (CKGR_PLLAR) Must Be Written to 0 Position */
#define CKGR_PLLAR_ZERO_Msk                   (0x1U << CKGR_PLLAR_ZERO_Pos)                  /**< (CKGR_PLLAR) Must Be Written to 0 Mask */
#define CKGR_PLLAR_ZERO(value)                (CKGR_PLLAR_ZERO_Msk & ((value) << CKGR_PLLAR_ZERO_Pos))
#define CKGR_PLLAR_Msk                        (0x3FFF3FFFUL)                                 /**< (CKGR_PLLAR) Register Mask  */

/* -------- CKGR_PLLBR : (PMC Offset: 0x2C) (R/W 32) PLLB Register -------- */
#define CKGR_PLLBR_PLLBEN_Pos                 (0U)                                           /**< (CKGR_PLLBR) PLLB Control Position */
#define CKGR_PLLBR_PLLBEN_Msk                 (0xFFU << CKGR_PLLBR_PLLBEN_Pos)               /**< (CKGR_PLLBR) PLLB Control Mask */
#define CKGR_PLLBR_PLLBEN(value)              (CKGR_PLLBR_PLLBEN_Msk & ((value) << CKGR_PLLBR_PLLBEN_Pos))
#define CKGR_PLLBR_PLLBCOUNT_Pos              (8U)                                           /**< (CKGR_PLLBR) PLLB Counter Position */
#define CKGR_PLLBR_PLLBCOUNT_Msk              (0x3FU << CKGR_PLLBR_PLLBCOUNT_Pos)            /**< (CKGR_PLLBR) PLLB Counter Mask */
#define CKGR_PLLBR_PLLBCOUNT(value)           (CKGR_PLLBR_PLLBCOUNT_Msk & ((value) << CKGR_PLLBR_PLLBCOUNT_Pos))
#define CKGR_PLLBR_MULB_Pos                   (16U)                                          /**< (CKGR_PLLBR) PLLB Multiplier Position */
#define CKGR_PLLBR_MULB_Msk                   (0x7FFU << CKGR_PLLBR_MULB_Pos)                /**< (CKGR_PLLBR) PLLB Multiplier Mask */
#define CKGR_PLLBR_MULB(value)                (CKGR_PLLBR_MULB_Msk & ((value) << CKGR_PLLBR_MULB_Pos))
#define CKGR_PLLBR_ZERO_Pos                   (29U)                                          /**< (CKGR_PLLBR) Must Be Written to 0 Position */
#define CKGR_PLLBR_ZERO_Msk                   (0x1U << CKGR_PLLBR_ZERO_Pos)                  /**< (CKGR_PLLBR) Must Be Written to 0 Mask */
#define CKGR_PLLBR_ZERO(value)                (CKGR_PLLBR_ZERO_Msk & ((value) << CKGR_PLLBR_ZERO_Pos))
#define CKGR_PLLBR_Msk                        (0x27FF3FFFUL)                                 /**< (CKGR_PLLBR) Register Mask  */

/* -------- PMC_MCKR : (PMC Offset: 0x30) (R/W 32) Master Clock Register -------- */
#define PMC_MCKR_CSS_Pos                      (0U)                                           /**< (PMC_MCKR) Master Clock Source Selection Position */
#define PMC_MCKR_CSS_Msk                      (0x3U << PMC_MCKR_CSS_Pos)                     /**< (PMC_MCKR) Master Clock Source Selection Mask */
#define PMC_MCKR_CSS(value)                   (PMC_MCKR_CSS_Msk & ((value) << PMC_MCKR_CSS_Pos))
#define   PMC_MCKR_CSS_SLOW_CLK_Val           (0U)                                           /**< (PMC_MCKR) Slow Clock is selected  */
#define   PMC_MCKR_CSS_MAIN_CLK_Val           (1U)                                           /**< (PMC_MCKR) Main Clock is selected  */
#define   PMC_MCKR_CSS_PLLA_CLK_Val           (2U)                                           /**< (PMC_MCKR) PLLA Clock is selected  */
#define   PMC_MCKR_CSS_PLLB_CLK_Val           (3U)                                           /**< (PMC_MCKR) PLLBClock is selected  */
#define PMC_MCKR_CSS_SLOW_CLK                 (PMC_MCKR_CSS_SLOW_CLK_Val << PMC_MCKR_CSS_Pos) /**< (PMC_MCKR) Slow Clock is selected Position  */
#define PMC_MCKR_CSS_MAIN_CLK                 (PMC_MCKR_CSS_MAIN_CLK_Val << PMC_MCKR_CSS_Pos) /**< (PMC_MCKR) Main Clock is selected Position  */
#define PMC_MCKR_CSS_PLLA_CLK                 (PMC_MCKR_CSS_PLLA_CLK_Val << PMC_MCKR_CSS_Pos) /**< (PMC_MCKR) PLLA Clock is selected Position  */
#define PMC_MCKR_CSS_PLLB_CLK                 (PMC_MCKR_CSS_PLLB_CLK_Val << PMC_MCKR_CSS_Pos) /**< (PMC_MCKR) PLLBClock is selected Position  */
#define PMC_MCKR_PRES_Pos                     (4U)                                           /**< (PMC_MCKR) Processor Clock Prescaler Position */
#define PMC_MCKR_PRES_Msk                     (0x7U << PMC_MCKR_PRES_Pos)                    /**< (PMC_MCKR) Processor Clock Prescaler Mask */
#define PMC_MCKR_PRES(value)                  (PMC_MCKR_PRES_Msk & ((value) << PMC_MCKR_PRES_Pos))
#define   PMC_MCKR_PRES_CLK_1_Val             (0U)                                           /**< (PMC_MCKR) Selected clock  */
#define   PMC_MCKR_PRES_CLK_2_Val             (1U)                                           /**< (PMC_MCKR) Selected clock divided by 2  */
#define   PMC_MCKR_PRES_CLK_4_Val             (2U)                                           /**< (PMC_MCKR) Selected clock divided by 4  */
#define   PMC_MCKR_PRES_CLK_8_Val             (3U)                                           /**< (PMC_MCKR) Selected clock divided by 8  */
#define   PMC_MCKR_PRES_CLK_16_Val            (4U)                                           /**< (PMC_MCKR) Selected clock divided by 16  */
#define   PMC_MCKR_PRES_CLK_32_Val            (5U)                                           /**< (PMC_MCKR) Selected clock divided by 32  */
#define   PMC_MCKR_PRES_CLK_64_Val            (6U)                                           /**< (PMC_MCKR) Selected clock divided by 64  */
#define   PMC_MCKR_PRES_CLK_3_Val             (7U)                                           /**< (PMC_MCKR) Selected clock divided by 3  */
#define PMC_MCKR_PRES_CLK_1                   (PMC_MCKR_PRES_CLK_1_Val << PMC_MCKR_PRES_Pos) /**< (PMC_MCKR) Selected clock Position  */
#define PMC_MCKR_PRES_CLK_2                   (PMC_MCKR_PRES_CLK_2_Val << PMC_MCKR_PRES_Pos) /**< (PMC_MCKR) Selected clock divided by 2 Position  */
#define PMC_MCKR_PRES_CLK_4                   (PMC_MCKR_PRES_CLK_4_Val << PMC_MCKR_PRES_Pos) /**< (PMC_MCKR) Selected clock divided by 4 Position  */
#define PMC_MCKR_PRES_CLK_8                   (PMC_MCKR_PRES_CLK_8_Val << PMC_MCKR_PRES_Pos) /**< (PMC_MCKR) Selected clock divided by 8 Position  */
#define PMC_MCKR_PRES_CLK_16                  (PMC_MCKR_PRES_CLK_16_Val << PMC_MCKR_PRES_Pos) /**< (PMC_MCKR) Selected clock divided by 16 Position  */
#define PMC_MCKR_PRES_CLK_32                  (PMC_MCKR_PRES_CLK_32_Val << PMC_MCKR_PRES_Pos) /**< (PMC_MCKR) Selected clock divided by 32 Position  */
#define PMC_MCKR_PRES_CLK_64                  (PMC_MCKR_PRES_CLK_64_Val << PMC_MCKR_PRES_Pos) /**< (PMC_MCKR) Selected clock divided by 64 Position  */
#define PMC_MCKR_PRES_CLK_3                   (PMC_MCKR_PRES_CLK_3_Val << PMC_MCKR_PRES_Pos) /**< (PMC_MCKR) Selected clock divided by 3 Position  */
#define PMC_MCKR_PLLADIV2_Pos                 (12U)                                          /**< (PMC_MCKR) PLLA Divisor by 2 Position */
#define PMC_MCKR_PLLADIV2_Msk                 (0x1U << PMC_MCKR_PLLADIV2_Pos)                /**< (PMC_MCKR) PLLA Divisor by 2 Mask */
#define PMC_MCKR_PLLADIV2(value)              (PMC_MCKR_PLLADIV2_Msk & ((value) << PMC_MCKR_PLLADIV2_Pos))
#define PMC_MCKR_PLLBDIV2_Pos                 (13U)                                          /**< (PMC_MCKR)  Position */
#define PMC_MCKR_PLLBDIV2_Msk                 (0x1U << PMC_MCKR_PLLBDIV2_Pos)                /**< (PMC_MCKR)  Mask */
#define PMC_MCKR_PLLBDIV2(value)              (PMC_MCKR_PLLBDIV2_Msk & ((value) << PMC_MCKR_PLLBDIV2_Pos))
#define PMC_MCKR_Msk                          (0x00003073UL)                                 /**< (PMC_MCKR) Register Mask  */

/* -------- PMC_USB : (PMC Offset: 0x38) (R/W 32) USB Clock Register -------- */
#define PMC_USB_USBS_Pos                      (0U)                                           /**< (PMC_USB) USB Input Clock Selection Position */
#define PMC_USB_USBS_Msk                      (0x1U << PMC_USB_USBS_Pos)                     /**< (PMC_USB) USB Input Clock Selection Mask */
#define PMC_USB_USBS(value)                   (PMC_USB_USBS_Msk & ((value) << PMC_USB_USBS_Pos))
#define PMC_USB_USBDIV_Pos                    (8U)                                           /**< (PMC_USB) Divider for USB Clock Position */
#define PMC_USB_USBDIV_Msk                    (0xFU << PMC_USB_USBDIV_Pos)                   /**< (PMC_USB) Divider for USB Clock Mask */
#define PMC_USB_USBDIV(value)                 (PMC_USB_USBDIV_Msk & ((value) << PMC_USB_USBDIV_Pos))
#define PMC_USB_Msk                           (0x00000F01UL)                                 /**< (PMC_USB) Register Mask  */

/* -------- PMC_PCK : (PMC Offset: 0x40) (R/W 32) Programmable Clock 0 Register 0 -------- */
#define PMC_PCK_CSS_Pos                       (0U)                                           /**< (PMC_PCK) Master Clock Source Selection Position */
#define PMC_PCK_CSS_Msk                       (0x7U << PMC_PCK_CSS_Pos)                      /**< (PMC_PCK) Master Clock Source Selection Mask */
#define PMC_PCK_CSS(value)                    (PMC_PCK_CSS_Msk & ((value) << PMC_PCK_CSS_Pos))
#define   PMC_PCK_CSS_SLOW_CLK_Val            (0U)                                           /**< (PMC_PCK) Slow Clock is selected  */
#define   PMC_PCK_CSS_MAIN_CLK_Val            (1U)                                           /**< (PMC_PCK) Main Clock is selected  */
#define   PMC_PCK_CSS_PLLA_CLK_Val            (2U)                                           /**< (PMC_PCK) PLLA Clock is selected  */
#define   PMC_PCK_CSS_PLLB_CLK_Val            (3U)                                           /**< (PMC_PCK) PLLB Clock is selected  */
#define   PMC_PCK_CSS_MCK_Val                 (4U)                                           /**< (PMC_PCK) Master Clock is selected  */
#define PMC_PCK_CSS_SLOW_CLK                  (PMC_PCK_CSS_SLOW_CLK_Val << PMC_PCK_CSS_Pos)  /**< (PMC_PCK) Slow Clock is selected Position  */
#define PMC_PCK_CSS_MAIN_CLK                  (PMC_PCK_CSS_MAIN_CLK_Val << PMC_PCK_CSS_Pos)  /**< (PMC_PCK) Main Clock is selected Position  */
#define PMC_PCK_CSS_PLLA_CLK                  (PMC_PCK_CSS_PLLA_CLK_Val << PMC_PCK_CSS_Pos)  /**< (PMC_PCK) PLLA Clock is selected Position  */
#define PMC_PCK_CSS_PLLB_CLK                  (PMC_PCK_CSS_PLLB_CLK_Val << PMC_PCK_CSS_Pos)  /**< (PMC_PCK) PLLB Clock is selected Position  */
#define PMC_PCK_CSS_MCK                       (PMC_PCK_CSS_MCK_Val << PMC_PCK_CSS_Pos)       /**< (PMC_PCK) Master Clock is selected Position  */
#define PMC_PCK_PRES_Pos                      (4U)                                           /**< (PMC_PCK) Programmable Clock Prescaler Position */
#define PMC_PCK_PRES_Msk                      (0xFFU << PMC_PCK_PRES_Pos)                    /**< (PMC_PCK) Programmable Clock Prescaler Mask */
#define PMC_PCK_PRES(value)                   (PMC_PCK_PRES_Msk & ((value) << PMC_PCK_PRES_Pos))
#define PMC_PCK_Msk                           (0x00000FF7UL)                                 /**< (PMC_PCK) Register Mask  */

/* -------- PMC_IER : (PMC Offset: 0x60) ( /W 32) Interrupt Enable Register -------- */
#define PMC_IER_MOSCXTS_Pos                   (0U)                                           /**< (PMC_IER) Main Crystal Oscillator Status Interrupt Enable Position */
#define PMC_IER_MOSCXTS_Msk                   (0x1U << PMC_IER_MOSCXTS_Pos)                  /**< (PMC_IER) Main Crystal Oscillator Status Interrupt Enable Mask */
#define PMC_IER_MOSCXTS(value)                (PMC_IER_MOSCXTS_Msk & ((value) << PMC_IER_MOSCXTS_Pos))
#define PMC_IER_LOCKA_Pos                     (1U)                                           /**< (PMC_IER) PLLA Lock Interrupt Enable Position */
#define PMC_IER_LOCKA_Msk                     (0x1U << PMC_IER_LOCKA_Pos)                    /**< (PMC_IER) PLLA Lock Interrupt Enable Mask */
#define PMC_IER_LOCKA(value)                  (PMC_IER_LOCKA_Msk & ((value) << PMC_IER_LOCKA_Pos))
#define PMC_IER_LOCKB_Pos                     (2U)                                           /**< (PMC_IER) PLLB Lock Interrupt Enable Position */
#define PMC_IER_LOCKB_Msk                     (0x1U << PMC_IER_LOCKB_Pos)                    /**< (PMC_IER) PLLB Lock Interrupt Enable Mask */
#define PMC_IER_LOCKB(value)                  (PMC_IER_LOCKB_Msk & ((value) << PMC_IER_LOCKB_Pos))
#define PMC_IER_MCKRDY_Pos                    (3U)                                           /**< (PMC_IER) Master Clock Ready Interrupt Enable Position */
#define PMC_IER_MCKRDY_Msk                    (0x1U << PMC_IER_MCKRDY_Pos)                   /**< (PMC_IER) Master Clock Ready Interrupt Enable Mask */
#define PMC_IER_MCKRDY(value)                 (PMC_IER_MCKRDY_Msk & ((value) << PMC_IER_MCKRDY_Pos))
#define PMC_IER_PCKRDY0_Pos                   (8U)                                           /**< (PMC_IER) Programmable Clock Ready 0 Interrupt Enable Position */
#define PMC_IER_PCKRDY0_Msk                   (0x1U << PMC_IER_PCKRDY0_Pos)                  /**< (PMC_IER) Programmable Clock Ready 0 Interrupt Enable Mask */
#define PMC_IER_PCKRDY0(value)                (PMC_IER_PCKRDY0_Msk & ((value) << PMC_IER_PCKRDY0_Pos))
#define PMC_IER_PCKRDY1_Pos                   (9U)                                           /**< (PMC_IER) Programmable Clock Ready 1 Interrupt Enable Position */
#define PMC_IER_PCKRDY1_Msk                   (0x1U << PMC_IER_PCKRDY1_Pos)                  /**< (PMC_IER) Programmable Clock Ready 1 Interrupt Enable Mask */
#define PMC_IER_PCKRDY1(value)                (PMC_IER_PCKRDY1_Msk & ((value) << PMC_IER_PCKRDY1_Pos))
#define PMC_IER_PCKRDY2_Pos                   (10U)                                          /**< (PMC_IER) Programmable Clock Ready 2 Interrupt Enable Position */
#define PMC_IER_PCKRDY2_Msk                   (0x1U << PMC_IER_PCKRDY2_Pos)                  /**< (PMC_IER) Programmable Clock Ready 2 Interrupt Enable Mask */
#define PMC_IER_PCKRDY2(value)                (PMC_IER_PCKRDY2_Msk & ((value) << PMC_IER_PCKRDY2_Pos))
#define PMC_IER_PCKRDY3_Pos                   (11U)                                          /**< (PMC_IER) Programmable Clock Ready 3 Interrupt Enable Position */
#define PMC_IER_PCKRDY3_Msk                   (0x1U << PMC_IER_PCKRDY3_Pos)                  /**< (PMC_IER) Programmable Clock Ready 3 Interrupt Enable Mask */
#define PMC_IER_PCKRDY3(value)                (PMC_IER_PCKRDY3_Msk & ((value) << PMC_IER_PCKRDY3_Pos))
#define PMC_IER_PCKRDY4_Pos                   (12U)                                          /**< (PMC_IER) Programmable Clock Ready 4 Interrupt Enable Position */
#define PMC_IER_PCKRDY4_Msk                   (0x1U << PMC_IER_PCKRDY4_Pos)                  /**< (PMC_IER) Programmable Clock Ready 4 Interrupt Enable Mask */
#define PMC_IER_PCKRDY4(value)                (PMC_IER_PCKRDY4_Msk & ((value) << PMC_IER_PCKRDY4_Pos))
#define PMC_IER_PCKRDY5_Pos                   (13U)                                          /**< (PMC_IER) Programmable Clock Ready 5 Interrupt Enable Position */
#define PMC_IER_PCKRDY5_Msk                   (0x1U << PMC_IER_PCKRDY5_Pos)                  /**< (PMC_IER) Programmable Clock Ready 5 Interrupt Enable Mask */
#define PMC_IER_PCKRDY5(value)                (PMC_IER_PCKRDY5_Msk & ((value) << PMC_IER_PCKRDY5_Pos))
#define PMC_IER_PCKRDY6_Pos                   (14U)                                          /**< (PMC_IER) Programmable Clock Ready 6 Interrupt Enable Position */
#define PMC_IER_PCKRDY6_Msk                   (0x1U << PMC_IER_PCKRDY6_Pos)                  /**< (PMC_IER) Programmable Clock Ready 6 Interrupt Enable Mask */
#define PMC_IER_PCKRDY6(value)                (PMC_IER_PCKRDY6_Msk & ((value) << PMC_IER_PCKRDY6_Pos))
#define PMC_IER_PCKRDY7_Pos                   (15U)                                          /**< (PMC_IER) Programmable Clock Ready 7 Interrupt Enable Position */
#define PMC_IER_PCKRDY7_Msk                   (0x1U << PMC_IER_PCKRDY7_Pos)                  /**< (PMC_IER) Programmable Clock Ready 7 Interrupt Enable Mask */
#define PMC_IER_PCKRDY7(value)                (PMC_IER_PCKRDY7_Msk & ((value) << PMC_IER_PCKRDY7_Pos))
#define PMC_IER_MOSCSELS_Pos                  (16U)                                          /**< (PMC_IER) Main Oscillator Selection Status Interrupt Enable Position */
#define PMC_IER_MOSCSELS_Msk                  (0x1U << PMC_IER_MOSCSELS_Pos)                 /**< (PMC_IER) Main Oscillator Selection Status Interrupt Enable Mask */
#define PMC_IER_MOSCSELS(value)               (PMC_IER_MOSCSELS_Msk & ((value) << PMC_IER_MOSCSELS_Pos))
#define PMC_IER_MOSCRCS_Pos                   (17U)                                          /**< (PMC_IER) Main On-Chip RC Status Interrupt Enable Position */
#define PMC_IER_MOSCRCS_Msk                   (0x1U << PMC_IER_MOSCRCS_Pos)                  /**< (PMC_IER) Main On-Chip RC Status Interrupt Enable Mask */
#define PMC_IER_MOSCRCS(value)                (PMC_IER_MOSCRCS_Msk & ((value) << PMC_IER_MOSCRCS_Pos))
#define PMC_IER_CFDEV_Pos                     (18U)                                          /**< (PMC_IER) Clock Failure Detector Event Interrupt Enable Position */
#define PMC_IER_CFDEV_Msk                     (0x1U << PMC_IER_CFDEV_Pos)                    /**< (PMC_IER) Clock Failure Detector Event Interrupt Enable Mask */
#define PMC_IER_CFDEV(value)                  (PMC_IER_CFDEV_Msk & ((value) << PMC_IER_CFDEV_Pos))
#define PMC_IER_Msk                           (0x0007FF0FUL)                                 /**< (PMC_IER) Register Mask  */

/* -------- PMC_IDR : (PMC Offset: 0x64) ( /W 32) Interrupt Disable Register -------- */
#define PMC_IDR_MOSCXTS_Pos                   (0U)                                           /**< (PMC_IDR) Main Crystal Oscillator Status Interrupt Disable Position */
#define PMC_IDR_MOSCXTS_Msk                   (0x1U << PMC_IDR_MOSCXTS_Pos)                  /**< (PMC_IDR) Main Crystal Oscillator Status Interrupt Disable Mask */
#define PMC_IDR_MOSCXTS(value)                (PMC_IDR_MOSCXTS_Msk & ((value) << PMC_IDR_MOSCXTS_Pos))
#define PMC_IDR_LOCKA_Pos                     (1U)                                           /**< (PMC_IDR) PLLA Lock Interrupt Disable Position */
#define PMC_IDR_LOCKA_Msk                     (0x1U << PMC_IDR_LOCKA_Pos)                    /**< (PMC_IDR) PLLA Lock Interrupt Disable Mask */
#define PMC_IDR_LOCKA(value)                  (PMC_IDR_LOCKA_Msk & ((value) << PMC_IDR_LOCKA_Pos))
#define PMC_IDR_LOCKB_Pos                     (2U)                                           /**< (PMC_IDR) PLLB Lock Interrupt Disable Position */
#define PMC_IDR_LOCKB_Msk                     (0x1U << PMC_IDR_LOCKB_Pos)                    /**< (PMC_IDR) PLLB Lock Interrupt Disable Mask */
#define PMC_IDR_LOCKB(value)                  (PMC_IDR_LOCKB_Msk & ((value) << PMC_IDR_LOCKB_Pos))
#define PMC_IDR_MCKRDY_Pos                    (3U)                                           /**< (PMC_IDR) Master Clock Ready Interrupt Disable Position */
#define PMC_IDR_MCKRDY_Msk                    (0x1U << PMC_IDR_MCKRDY_Pos)                   /**< (PMC_IDR) Master Clock Ready Interrupt Disable Mask */
#define PMC_IDR_MCKRDY(value)                 (PMC_IDR_MCKRDY_Msk & ((value) << PMC_IDR_MCKRDY_Pos))
#define PMC_IDR_PCKRDY0_Pos                   (8U)                                           /**< (PMC_IDR) Programmable Clock Ready 0 Interrupt Disable Position */
#define PMC_IDR_PCKRDY0_Msk                   (0x1U << PMC_IDR_PCKRDY0_Pos)                  /**< (PMC_IDR) Programmable Clock Ready 0 Interrupt Disable Mask */
#define PMC_IDR_PCKRDY0(value)                (PMC_IDR_PCKRDY0_Msk & ((value) << PMC_IDR_PCKRDY0_Pos))
#define PMC_IDR_PCKRDY1_Pos                   (9U)                                           /**< (PMC_IDR) Programmable Clock Ready 1 Interrupt Disable Position */
#define PMC_IDR_PCKRDY1_Msk                   (0x1U << PMC_IDR_PCKRDY1_Pos)                  /**< (PMC_IDR) Programmable Clock Ready 1 Interrupt Disable Mask */
#define PMC_IDR_PCKRDY1(value)                (PMC_IDR_PCKRDY1_Msk & ((value) << PMC_IDR_PCKRDY1_Pos))
#define PMC_IDR_PCKRDY2_Pos                   (10U)                                          /**< (PMC_IDR) Programmable Clock Ready 2 Interrupt Disable Position */
#define PMC_IDR_PCKRDY2_Msk                   (0x1U << PMC_IDR_PCKRDY2_Pos)                  /**< (PMC_IDR) Programmable Clock Ready 2 Interrupt Disable Mask */
#define PMC_IDR_PCKRDY2(value)                (PMC_IDR_PCKRDY2_Msk & ((value) << PMC_IDR_PCKRDY2_Pos))
#define PMC_IDR_PCKRDY3_Pos                   (11U)                                          /**< (PMC_IDR) Programmable Clock Ready 3 Interrupt Disable Position */
#define PMC_IDR_PCKRDY3_Msk                   (0x1U << PMC_IDR_PCKRDY3_Pos)                  /**< (PMC_IDR) Programmable Clock Ready 3 Interrupt Disable Mask */
#define PMC_IDR_PCKRDY3(value)                (PMC_IDR_PCKRDY3_Msk & ((value) << PMC_IDR_PCKRDY3_Pos))
#define PMC_IDR_PCKRDY4_Pos                   (12U)                                          /**< (PMC_IDR) Programmable Clock Ready 4 Interrupt Disable Position */
#define PMC_IDR_PCKRDY4_Msk                   (0x1U << PMC_IDR_PCKRDY4_Pos)                  /**< (PMC_IDR) Programmable Clock Ready 4 Interrupt Disable Mask */
#define PMC_IDR_PCKRDY4(value)                (PMC_IDR_PCKRDY4_Msk & ((value) << PMC_IDR_PCKRDY4_Pos))
#define PMC_IDR_PCKRDY5_Pos                   (13U)                                          /**< (PMC_IDR) Programmable Clock Ready 5 Interrupt Disable Position */
#define PMC_IDR_PCKRDY5_Msk                   (0x1U << PMC_IDR_PCKRDY5_Pos)                  /**< (PMC_IDR) Programmable Clock Ready 5 Interrupt Disable Mask */
#define PMC_IDR_PCKRDY5(value)                (PMC_IDR_PCKRDY5_Msk & ((value) << PMC_IDR_PCKRDY5_Pos))
#define PMC_IDR_PCKRDY6_Pos                   (14U)                                          /**< (PMC_IDR) Programmable Clock Ready 6 Interrupt Disable Position */
#define PMC_IDR_PCKRDY6_Msk                   (0x1U << PMC_IDR_PCKRDY6_Pos)                  /**< (PMC_IDR) Programmable Clock Ready 6 Interrupt Disable Mask */
#define PMC_IDR_PCKRDY6(value)                (PMC_IDR_PCKRDY6_Msk & ((value) << PMC_IDR_PCKRDY6_Pos))
#define PMC_IDR_PCKRDY7_Pos                   (15U)                                          /**< (PMC_IDR) Programmable Clock Ready 7 Interrupt Disable Position */
#define PMC_IDR_PCKRDY7_Msk                   (0x1U << PMC_IDR_PCKRDY7_Pos)                  /**< (PMC_IDR) Programmable Clock Ready 7 Interrupt Disable Mask */
#define PMC_IDR_PCKRDY7(value)                (PMC_IDR_PCKRDY7_Msk & ((value) << PMC_IDR_PCKRDY7_Pos))
#define PMC_IDR_MOSCSELS_Pos                  (16U)                                          /**< (PMC_IDR) Main Oscillator Selection Status Interrupt Disable Position */
#define PMC_IDR_MOSCSELS_Msk                  (0x1U << PMC_IDR_MOSCSELS_Pos)                 /**< (PMC_IDR) Main Oscillator Selection Status Interrupt Disable Mask */
#define PMC_IDR_MOSCSELS(value)               (PMC_IDR_MOSCSELS_Msk & ((value) << PMC_IDR_MOSCSELS_Pos))
#define PMC_IDR_MOSCRCS_Pos                   (17U)                                          /**< (PMC_IDR) Main On-Chip RC Status Interrupt Disable Position */
#define PMC_IDR_MOSCRCS_Msk                   (0x1U << PMC_IDR_MOSCRCS_Pos)                  /**< (PMC_IDR) Main On-Chip RC Status Interrupt Disable Mask */
#define PMC_IDR_MOSCRCS(value)                (PMC_IDR_MOSCRCS_Msk & ((value) << PMC_IDR_MOSCRCS_Pos))
#define PMC_IDR_CFDEV_Pos                     (18U)                                          /**< (PMC_IDR) Clock Failure Detector Event Interrupt Disable Position */
#define PMC_IDR_CFDEV_Msk                     (0x1U << PMC_IDR_CFDEV_Pos)                    /**< (PMC_IDR) Clock Failure Detector Event Interrupt Disable Mask */
#define PMC_IDR_CFDEV(value)                  (PMC_IDR_CFDEV_Msk & ((value) << PMC_IDR_CFDEV_Pos))
#define PMC_IDR_Msk                           (0x0007FF0FUL)                                 /**< (PMC_IDR) Register Mask  */

/* -------- PMC_SR : (PMC Offset: 0x68) (R/  32) Status Register -------- */
#define PMC_SR_MOSCXTS_Pos                    (0U)                                           /**< (PMC_SR) Main Crystal Oscillator Status Position */
#define PMC_SR_MOSCXTS_Msk                    (0x1U << PMC_SR_MOSCXTS_Pos)                   /**< (PMC_SR) Main Crystal Oscillator Status Mask */
#define PMC_SR_MOSCXTS(value)                 (PMC_SR_MOSCXTS_Msk & ((value) << PMC_SR_MOSCXTS_Pos))
#define PMC_SR_LOCKA_Pos                      (1U)                                           /**< (PMC_SR) PLLA Lock Status Position */
#define PMC_SR_LOCKA_Msk                      (0x1U << PMC_SR_LOCKA_Pos)                     /**< (PMC_SR) PLLA Lock Status Mask */
#define PMC_SR_LOCKA(value)                   (PMC_SR_LOCKA_Msk & ((value) << PMC_SR_LOCKA_Pos))
#define PMC_SR_LOCKB_Pos                      (2U)                                           /**< (PMC_SR) PLLB Lock Status Position */
#define PMC_SR_LOCKB_Msk                      (0x1U << PMC_SR_LOCKB_Pos)                     /**< (PMC_SR) PLLB Lock Status Mask */
#define PMC_SR_LOCKB(value)                   (PMC_SR_LOCKB_Msk & ((value) << PMC_SR_LOCKB_Pos))
#define PMC_SR_MCKRDY_Pos                     (3U)                                           /**< (PMC_SR) Master Clock Status Position */
#define PMC_SR_MCKRDY_Msk                     (0x1U << PMC_SR_MCKRDY_Pos)                    /**< (PMC_SR) Master Clock Status Mask */
#define PMC_SR_MCKRDY(value)                  (PMC_SR_MCKRDY_Msk & ((value) << PMC_SR_MCKRDY_Pos))
#define PMC_SR_OSCSELS_Pos                    (7U)                                           /**< (PMC_SR) Slow Clock Oscillator Selection Position */
#define PMC_SR_OSCSELS_Msk                    (0x1U << PMC_SR_OSCSELS_Pos)                   /**< (PMC_SR) Slow Clock Oscillator Selection Mask */
#define PMC_SR_OSCSELS(value)                 (PMC_SR_OSCSELS_Msk & ((value) << PMC_SR_OSCSELS_Pos))
#define PMC_SR_PCKRDY0_Pos                    (8U)                                           /**< (PMC_SR) Programmable Clock Ready Status Position */
#define PMC_SR_PCKRDY0_Msk                    (0x1U << PMC_SR_PCKRDY0_Pos)                   /**< (PMC_SR) Programmable Clock Ready Status Mask */
#define PMC_SR_PCKRDY0(value)                 (PMC_SR_PCKRDY0_Msk & ((value) << PMC_SR_PCKRDY0_Pos))
#define PMC_SR_PCKRDY1_Pos                    (9U)                                           /**< (PMC_SR) Programmable Clock Ready Status Position */
#define PMC_SR_PCKRDY1_Msk                    (0x1U << PMC_SR_PCKRDY1_Pos)                   /**< (PMC_SR) Programmable Clock Ready Status Mask */
#define PMC_SR_PCKRDY1(value)                 (PMC_SR_PCKRDY1_Msk & ((value) << PMC_SR_PCKRDY1_Pos))
#define PMC_SR_PCKRDY2_Pos                    (10U)                                          /**< (PMC_SR) Programmable Clock Ready Status Position */
#define PMC_SR_PCKRDY2_Msk                    (0x1U << PMC_SR_PCKRDY2_Pos)                   /**< (PMC_SR) Programmable Clock Ready Status Mask */
#define PMC_SR_PCKRDY2(value)                 (PMC_SR_PCKRDY2_Msk & ((value) << PMC_SR_PCKRDY2_Pos))
#define PMC_SR_PCKRDY3_Pos                    (11U)                                          /**< (PMC_SR) Programmable Clock Ready Status Position */
#define PMC_SR_PCKRDY3_Msk                    (0x1U << PMC_SR_PCKRDY3_Pos)                   /**< (PMC_SR) Programmable Clock Ready Status Mask */
#define PMC_SR_PCKRDY3(value)                 (PMC_SR_PCKRDY3_Msk & ((value) << PMC_SR_PCKRDY3_Pos))
#define PMC_SR_PCKRDY4_Pos                    (12U)                                          /**< (PMC_SR) Programmable Clock Ready Status Position */
#define PMC_SR_PCKRDY4_Msk                    (0x1U << PMC_SR_PCKRDY4_Pos)                   /**< (PMC_SR) Programmable Clock Ready Status Mask */
#define PMC_SR_PCKRDY4(value)                 (PMC_SR_PCKRDY4_Msk & ((value) << PMC_SR_PCKRDY4_Pos))
#define PMC_SR_PCKRDY5_Pos                    (13U)                                          /**< (PMC_SR) Programmable Clock Ready Status Position */
#define PMC_SR_PCKRDY5_Msk                    (0x1U << PMC_SR_PCKRDY5_Pos)                   /**< (PMC_SR) Programmable Clock Ready Status Mask */
#define PMC_SR_PCKRDY5(value)                 (PMC_SR_PCKRDY5_Msk & ((value) << PMC_SR_PCKRDY5_Pos))
#define PMC_SR_PCKRDY6_Pos                    (14U)                                          /**< (PMC_SR) Programmable Clock Ready Status Position */
#define PMC_SR_PCKRDY6_Msk                    (0x1U << PMC_SR_PCKRDY6_Pos)                   /**< (PMC_SR) Programmable Clock Ready Status Mask */
#define PMC_SR_PCKRDY6(value)                 (PMC_SR_PCKRDY6_Msk & ((value) << PMC_SR_PCKRDY6_Pos))
#define PMC_SR_PCKRDY7_Pos                    (15U)                                          /**< (PMC_SR) Programmable Clock Ready Status Position */
#define PMC_SR_PCKRDY7_Msk                    (0x1U << PMC_SR_PCKRDY7_Pos)                   /**< (PMC_SR) Programmable Clock Ready Status Mask */
#define PMC_SR_PCKRDY7(value)                 (PMC_SR_PCKRDY7_Msk & ((value) << PMC_SR_PCKRDY7_Pos))
#define PMC_SR_MOSCSELS_Pos                   (16U)                                          /**< (PMC_SR) Main Oscillator Selection Status Position */
#define PMC_SR_MOSCSELS_Msk                   (0x1U << PMC_SR_MOSCSELS_Pos)                  /**< (PMC_SR) Main Oscillator Selection Status Mask */
#define PMC_SR_MOSCSELS(value)                (PMC_SR_MOSCSELS_Msk & ((value) << PMC_SR_MOSCSELS_Pos))
#define PMC_SR_MOSCRCS_Pos                    (17U)                                          /**< (PMC_SR) Main On-Chip RC Oscillator Status Position */
#define PMC_SR_MOSCRCS_Msk                    (0x1U << PMC_SR_MOSCRCS_Pos)                   /**< (PMC_SR) Main On-Chip RC Oscillator Status Mask */
#define PMC_SR_MOSCRCS(value)                 (PMC_SR_MOSCRCS_Msk & ((value) << PMC_SR_MOSCRCS_Pos))
#define PMC_SR_CFDEV_Pos                      (18U)                                          /**< (PMC_SR) Clock Failure Detector Event Position */
#define PMC_SR_CFDEV_Msk                      (0x1U << PMC_SR_CFDEV_Pos)                     /**< (PMC_SR) Clock Failure Detector Event Mask */
#define PMC_SR_CFDEV(value)                   (PMC_SR_CFDEV_Msk & ((value) << PMC_SR_CFDEV_Pos))
#define PMC_SR_CFDS_Pos                       (19U)                                          /**< (PMC_SR) Clock Failure Detector Status Position */
#define PMC_SR_CFDS_Msk                       (0x1U << PMC_SR_CFDS_Pos)                      /**< (PMC_SR) Clock Failure Detector Status Mask */
#define PMC_SR_CFDS(value)                    (PMC_SR_CFDS_Msk & ((value) << PMC_SR_CFDS_Pos))
#define PMC_SR_FOS_Pos                        (20U)                                          /**< (PMC_SR) Clock Failure Detector Fault Output Status Position */
#define PMC_SR_FOS_Msk                        (0x1U << PMC_SR_FOS_Pos)                       /**< (PMC_SR) Clock Failure Detector Fault Output Status Mask */
#define PMC_SR_FOS(value)                     (PMC_SR_FOS_Msk & ((value) << PMC_SR_FOS_Pos))
#define PMC_SR_Msk                            (0x001FFF8FUL)                                 /**< (PMC_SR) Register Mask  */

/* -------- PMC_IMR : (PMC Offset: 0x6C) (R/  32) Interrupt Mask Register -------- */
#define PMC_IMR_MOSCXTS_Pos                   (0U)                                           /**< (PMC_IMR) Main Crystal Oscillator Status Interrupt Mask Position */
#define PMC_IMR_MOSCXTS_Msk                   (0x1U << PMC_IMR_MOSCXTS_Pos)                  /**< (PMC_IMR) Main Crystal Oscillator Status Interrupt Mask Mask */
#define PMC_IMR_MOSCXTS(value)                (PMC_IMR_MOSCXTS_Msk & ((value) << PMC_IMR_MOSCXTS_Pos))
#define PMC_IMR_LOCKA_Pos                     (1U)                                           /**< (PMC_IMR) PLLA Lock Interrupt Mask Position */
#define PMC_IMR_LOCKA_Msk                     (0x1U << PMC_IMR_LOCKA_Pos)                    /**< (PMC_IMR) PLLA Lock Interrupt Mask Mask */
#define PMC_IMR_LOCKA(value)                  (PMC_IMR_LOCKA_Msk & ((value) << PMC_IMR_LOCKA_Pos))
#define PMC_IMR_LOCKB_Pos                     (2U)                                           /**< (PMC_IMR) PLLB Lock Interrupt Mask Position */
#define PMC_IMR_LOCKB_Msk                     (0x1U << PMC_IMR_LOCKB_Pos)                    /**< (PMC_IMR) PLLB Lock Interrupt Mask Mask */
#define PMC_IMR_LOCKB(value)                  (PMC_IMR_LOCKB_Msk & ((value) << PMC_IMR_LOCKB_Pos))
#define PMC_IMR_MCKRDY_Pos                    (3U)                                           /**< (PMC_IMR) Master Clock Ready Interrupt Mask Position */
#define PMC_IMR_MCKRDY_Msk                    (0x1U << PMC_IMR_MCKRDY_Pos)                   /**< (PMC_IMR) Master Clock Ready Interrupt Mask Mask */
#define PMC_IMR_MCKRDY(value)                 (PMC_IMR_MCKRDY_Msk & ((value) << PMC_IMR_MCKRDY_Pos))
#define PMC_IMR_PCKRDY0_Pos                   (8U)                                           /**< (PMC_IMR) Programmable Clock Ready 0 Interrupt Mask Position */
#define PMC_IMR_PCKRDY0_Msk                   (0x1U << PMC_IMR_PCKRDY0_Pos)                  /**< (PMC_IMR) Programmable Clock Ready 0 Interrupt Mask Mask */
#define PMC_IMR_PCKRDY0(value)                (PMC_IMR_PCKRDY0_Msk & ((value) << PMC_IMR_PCKRDY0_Pos))
#define PMC_IMR_PCKRDY1_Pos                   (9U)                                           /**< (PMC_IMR) Programmable Clock Ready 1 Interrupt Mask Position */
#define PMC_IMR_PCKRDY1_Msk                   (0x1U << PMC_IMR_PCKRDY1_Pos)                  /**< (PMC_IMR) Programmable Clock Ready 1 Interrupt Mask Mask */
#define PMC_IMR_PCKRDY1(value)                (PMC_IMR_PCKRDY1_Msk & ((value) << PMC_IMR_PCKRDY1_Pos))
#define PMC_IMR_PCKRDY2_Pos                   (10U)                                          /**< (PMC_IMR) Programmable Clock Ready 2 Interrupt Mask Position */
#define PMC_IMR_PCKRDY2_Msk                   (0x1U << PMC_IMR_PCKRDY2_Pos)                  /**< (PMC_IMR) Programmable Clock Ready 2 Interrupt Mask Mask */
#define PMC_IMR_PCKRDY2(value)                (PMC_IMR_PCKRDY2_Msk & ((value) << PMC_IMR_PCKRDY2_Pos))
#define PMC_IMR_PCKRDY3_Pos                   (11U)                                          /**< (PMC_IMR) Programmable Clock Ready 3 Interrupt Mask Position */
#define PMC_IMR_PCKRDY3_Msk                   (0x1U << PMC_IMR_PCKRDY3_Pos)                  /**< (PMC_IMR) Programmable Clock Ready 3 Interrupt Mask Mask */
#define PMC_IMR_PCKRDY3(value)                (PMC_IMR_PCKRDY3_Msk & ((value) << PMC_IMR_PCKRDY3_Pos))
#define PMC_IMR_PCKRDY4_Pos                   (12U)                                          /**< (PMC_IMR) Programmable Clock Ready 4 Interrupt Mask Position */
#define PMC_IMR_PCKRDY4_Msk                   (0x1U << PMC_IMR_PCKRDY4_Pos)                  /**< (PMC_IMR) Programmable Clock Ready 4 Interrupt Mask Mask */
#define PMC_IMR_PCKRDY4(value)                (PMC_IMR_PCKRDY4_Msk & ((value) << PMC_IMR_PCKRDY4_Pos))
#define PMC_IMR_PCKRDY5_Pos                   (13U)                                          /**< (PMC_IMR) Programmable Clock Ready 5 Interrupt Mask Position */
#define PMC_IMR_PCKRDY5_Msk                   (0x1U << PMC_IMR_PCKRDY5_Pos)                  /**< (PMC_IMR) Programmable Clock Ready 5 Interrupt Mask Mask */
#define PMC_IMR_PCKRDY5(value)                (PMC_IMR_PCKRDY5_Msk & ((value) << PMC_IMR_PCKRDY5_Pos))
#define PMC_IMR_PCKRDY6_Pos                   (14U)                                          /**< (PMC_IMR) Programmable Clock Ready 6 Interrupt Mask Position */
#define PMC_IMR_PCKRDY6_Msk                   (0x1U << PMC_IMR_PCKRDY6_Pos)                  /**< (PMC_IMR) Programmable Clock Ready 6 Interrupt Mask Mask */
#define PMC_IMR_PCKRDY6(value)                (PMC_IMR_PCKRDY6_Msk & ((value) << PMC_IMR_PCKRDY6_Pos))
#define PMC_IMR_MOSCSELS_Pos                  (16U)                                          /**< (PMC_IMR) Main Oscillator Selection Status Interrupt Mask Position */
#define PMC_IMR_MOSCSELS_Msk                  (0x1U << PMC_IMR_MOSCSELS_Pos)                 /**< (PMC_IMR) Main Oscillator Selection Status Interrupt Mask Mask */
#define PMC_IMR_MOSCSELS(value)               (PMC_IMR_MOSCSELS_Msk & ((value) << PMC_IMR_MOSCSELS_Pos))
#define PMC_IMR_MOSCRCS_Pos                   (17U)                                          /**< (PMC_IMR) Main On-Chip RC Status Interrupt Mask Position */
#define PMC_IMR_MOSCRCS_Msk                   (0x1U << PMC_IMR_MOSCRCS_Pos)                  /**< (PMC_IMR) Main On-Chip RC Status Interrupt Mask Mask */
#define PMC_IMR_MOSCRCS(value)                (PMC_IMR_MOSCRCS_Msk & ((value) << PMC_IMR_MOSCRCS_Pos))
#define PMC_IMR_CFDEV_Pos                     (18U)                                          /**< (PMC_IMR) Clock Failure Detector Event Interrupt Mask Position */
#define PMC_IMR_CFDEV_Msk                     (0x1U << PMC_IMR_CFDEV_Pos)                    /**< (PMC_IMR) Clock Failure Detector Event Interrupt Mask Mask */
#define PMC_IMR_CFDEV(value)                  (PMC_IMR_CFDEV_Msk & ((value) << PMC_IMR_CFDEV_Pos))
#define PMC_IMR_PCKRDY7_Pos                   (15U)                                          /**< (PMC_IMR) Programmable Clock Ready 7 Interrupt Mask Position */
#define PMC_IMR_PCKRDY7_Msk                   (0x1U << PMC_IMR_PCKRDY7_Pos)                  /**< (PMC_IMR) Programmable Clock Ready 7 Interrupt Mask Mask */
#define PMC_IMR_PCKRDY7(value)                (PMC_IMR_PCKRDY7_Msk & ((value) << PMC_IMR_PCKRDY7_Pos))
#define PMC_IMR_Msk                           (0x0007FF0FUL)                                 /**< (PMC_IMR) Register Mask  */

/* -------- PMC_FSMR : (PMC Offset: 0x70) (R/W 32) Fast Startup Mode Register -------- */
#define PMC_FSMR_FSTT0_Pos                    (0U)                                           /**< (PMC_FSMR) Fast Startup Input Enable 0 Position */
#define PMC_FSMR_FSTT0_Msk                    (0x1U << PMC_FSMR_FSTT0_Pos)                   /**< (PMC_FSMR) Fast Startup Input Enable 0 Mask */
#define PMC_FSMR_FSTT0(value)                 (PMC_FSMR_FSTT0_Msk & ((value) << PMC_FSMR_FSTT0_Pos))
#define PMC_FSMR_FSTT1_Pos                    (1U)                                           /**< (PMC_FSMR) Fast Startup Input Enable 1 Position */
#define PMC_FSMR_FSTT1_Msk                    (0x1U << PMC_FSMR_FSTT1_Pos)                   /**< (PMC_FSMR) Fast Startup Input Enable 1 Mask */
#define PMC_FSMR_FSTT1(value)                 (PMC_FSMR_FSTT1_Msk & ((value) << PMC_FSMR_FSTT1_Pos))
#define PMC_FSMR_FSTT2_Pos                    (2U)                                           /**< (PMC_FSMR) Fast Startup Input Enable 2 Position */
#define PMC_FSMR_FSTT2_Msk                    (0x1U << PMC_FSMR_FSTT2_Pos)                   /**< (PMC_FSMR) Fast Startup Input Enable 2 Mask */
#define PMC_FSMR_FSTT2(value)                 (PMC_FSMR_FSTT2_Msk & ((value) << PMC_FSMR_FSTT2_Pos))
#define PMC_FSMR_FSTT3_Pos                    (3U)                                           /**< (PMC_FSMR) Fast Startup Input Enable 3 Position */
#define PMC_FSMR_FSTT3_Msk                    (0x1U << PMC_FSMR_FSTT3_Pos)                   /**< (PMC_FSMR) Fast Startup Input Enable 3 Mask */
#define PMC_FSMR_FSTT3(value)                 (PMC_FSMR_FSTT3_Msk & ((value) << PMC_FSMR_FSTT3_Pos))
#define PMC_FSMR_FSTT4_Pos                    (4U)                                           /**< (PMC_FSMR) Fast Startup Input Enable 4 Position */
#define PMC_FSMR_FSTT4_Msk                    (0x1U << PMC_FSMR_FSTT4_Pos)                   /**< (PMC_FSMR) Fast Startup Input Enable 4 Mask */
#define PMC_FSMR_FSTT4(value)                 (PMC_FSMR_FSTT4_Msk & ((value) << PMC_FSMR_FSTT4_Pos))
#define PMC_FSMR_FSTT5_Pos                    (5U)                                           /**< (PMC_FSMR) Fast Startup Input Enable 5 Position */
#define PMC_FSMR_FSTT5_Msk                    (0x1U << PMC_FSMR_FSTT5_Pos)                   /**< (PMC_FSMR) Fast Startup Input Enable 5 Mask */
#define PMC_FSMR_FSTT5(value)                 (PMC_FSMR_FSTT5_Msk & ((value) << PMC_FSMR_FSTT5_Pos))
#define PMC_FSMR_FSTT6_Pos                    (6U)                                           /**< (PMC_FSMR) Fast Startup Input Enable 6 Position */
#define PMC_FSMR_FSTT6_Msk                    (0x1U << PMC_FSMR_FSTT6_Pos)                   /**< (PMC_FSMR) Fast Startup Input Enable 6 Mask */
#define PMC_FSMR_FSTT6(value)                 (PMC_FSMR_FSTT6_Msk & ((value) << PMC_FSMR_FSTT6_Pos))
#define PMC_FSMR_FSTT7_Pos                    (7U)                                           /**< (PMC_FSMR) Fast Startup Input Enable 7 Position */
#define PMC_FSMR_FSTT7_Msk                    (0x1U << PMC_FSMR_FSTT7_Pos)                   /**< (PMC_FSMR) Fast Startup Input Enable 7 Mask */
#define PMC_FSMR_FSTT7(value)                 (PMC_FSMR_FSTT7_Msk & ((value) << PMC_FSMR_FSTT7_Pos))
#define PMC_FSMR_FSTT8_Pos                    (8U)                                           /**< (PMC_FSMR) Fast Startup Input Enable 8 Position */
#define PMC_FSMR_FSTT8_Msk                    (0x1U << PMC_FSMR_FSTT8_Pos)                   /**< (PMC_FSMR) Fast Startup Input Enable 8 Mask */
#define PMC_FSMR_FSTT8(value)                 (PMC_FSMR_FSTT8_Msk & ((value) << PMC_FSMR_FSTT8_Pos))
#define PMC_FSMR_FSTT9_Pos                    (9U)                                           /**< (PMC_FSMR) Fast Startup Input Enable 9 Position */
#define PMC_FSMR_FSTT9_Msk                    (0x1U << PMC_FSMR_FSTT9_Pos)                   /**< (PMC_FSMR) Fast Startup Input Enable 9 Mask */
#define PMC_FSMR_FSTT9(value)                 (PMC_FSMR_FSTT9_Msk & ((value) << PMC_FSMR_FSTT9_Pos))
#define PMC_FSMR_FSTT10_Pos                   (10U)                                          /**< (PMC_FSMR) Fast Startup Input Enable 10 Position */
#define PMC_FSMR_FSTT10_Msk                   (0x1U << PMC_FSMR_FSTT10_Pos)                  /**< (PMC_FSMR) Fast Startup Input Enable 10 Mask */
#define PMC_FSMR_FSTT10(value)                (PMC_FSMR_FSTT10_Msk & ((value) << PMC_FSMR_FSTT10_Pos))
#define PMC_FSMR_FSTT11_Pos                   (11U)                                          /**< (PMC_FSMR) Fast Startup Input Enable 11 Position */
#define PMC_FSMR_FSTT11_Msk                   (0x1U << PMC_FSMR_FSTT11_Pos)                  /**< (PMC_FSMR) Fast Startup Input Enable 11 Mask */
#define PMC_FSMR_FSTT11(value)                (PMC_FSMR_FSTT11_Msk & ((value) << PMC_FSMR_FSTT11_Pos))
#define PMC_FSMR_FSTT12_Pos                   (12U)                                          /**< (PMC_FSMR) Fast Startup Input Enable 12 Position */
#define PMC_FSMR_FSTT12_Msk                   (0x1U << PMC_FSMR_FSTT12_Pos)                  /**< (PMC_FSMR) Fast Startup Input Enable 12 Mask */
#define PMC_FSMR_FSTT12(value)                (PMC_FSMR_FSTT12_Msk & ((value) << PMC_FSMR_FSTT12_Pos))
#define PMC_FSMR_FSTT13_Pos                   (13U)                                          /**< (PMC_FSMR) Fast Startup Input Enable 13 Position */
#define PMC_FSMR_FSTT13_Msk                   (0x1U << PMC_FSMR_FSTT13_Pos)                  /**< (PMC_FSMR) Fast Startup Input Enable 13 Mask */
#define PMC_FSMR_FSTT13(value)                (PMC_FSMR_FSTT13_Msk & ((value) << PMC_FSMR_FSTT13_Pos))
#define PMC_FSMR_FSTT14_Pos                   (14U)                                          /**< (PMC_FSMR) Fast Startup Input Enable 14 Position */
#define PMC_FSMR_FSTT14_Msk                   (0x1U << PMC_FSMR_FSTT14_Pos)                  /**< (PMC_FSMR) Fast Startup Input Enable 14 Mask */
#define PMC_FSMR_FSTT14(value)                (PMC_FSMR_FSTT14_Msk & ((value) << PMC_FSMR_FSTT14_Pos))
#define PMC_FSMR_FSTT15_Pos                   (15U)                                          /**< (PMC_FSMR) Fast Startup Input Enable 15 Position */
#define PMC_FSMR_FSTT15_Msk                   (0x1U << PMC_FSMR_FSTT15_Pos)                  /**< (PMC_FSMR) Fast Startup Input Enable 15 Mask */
#define PMC_FSMR_FSTT15(value)                (PMC_FSMR_FSTT15_Msk & ((value) << PMC_FSMR_FSTT15_Pos))
#define PMC_FSMR_RTTAL_Pos                    (16U)                                          /**< (PMC_FSMR) RTT Alarm Enable Position */
#define PMC_FSMR_RTTAL_Msk                    (0x1U << PMC_FSMR_RTTAL_Pos)                   /**< (PMC_FSMR) RTT Alarm Enable Mask */
#define PMC_FSMR_RTTAL(value)                 (PMC_FSMR_RTTAL_Msk & ((value) << PMC_FSMR_RTTAL_Pos))
#define PMC_FSMR_RTCAL_Pos                    (17U)                                          /**< (PMC_FSMR) RTC Alarm Enable Position */
#define PMC_FSMR_RTCAL_Msk                    (0x1U << PMC_FSMR_RTCAL_Pos)                   /**< (PMC_FSMR) RTC Alarm Enable Mask */
#define PMC_FSMR_RTCAL(value)                 (PMC_FSMR_RTCAL_Msk & ((value) << PMC_FSMR_RTCAL_Pos))
#define PMC_FSMR_USBAL_Pos                    (18U)                                          /**< (PMC_FSMR) USB Alarm Enable Position */
#define PMC_FSMR_USBAL_Msk                    (0x1U << PMC_FSMR_USBAL_Pos)                   /**< (PMC_FSMR) USB Alarm Enable Mask */
#define PMC_FSMR_USBAL(value)                 (PMC_FSMR_USBAL_Msk & ((value) << PMC_FSMR_USBAL_Pos))
#define PMC_FSMR_LPM_Pos                      (20U)                                          /**< (PMC_FSMR) Low-power Mode Position */
#define PMC_FSMR_LPM_Msk                      (0x1U << PMC_FSMR_LPM_Pos)                     /**< (PMC_FSMR) Low-power Mode Mask */
#define PMC_FSMR_LPM(value)                   (PMC_FSMR_LPM_Msk & ((value) << PMC_FSMR_LPM_Pos))
#define PMC_FSMR_FLPM_Pos                     (21U)                                          /**< (PMC_FSMR) Flash Low-power Mode Position */
#define PMC_FSMR_FLPM_Msk                     (0x3U << PMC_FSMR_FLPM_Pos)                    /**< (PMC_FSMR) Flash Low-power Mode Mask */
#define PMC_FSMR_FLPM(value)                  (PMC_FSMR_FLPM_Msk & ((value) << PMC_FSMR_FLPM_Pos))
#define   PMC_FSMR_FLPM_FLASH_STANDBY_Val     (0U)                                           /**< (PMC_FSMR) Flash is in Standby Mode when system enters Wait Mode  */
#define   PMC_FSMR_FLPM_FLASH_DEEP_POWERDOWN_Val (1U)                                           /**< (PMC_FSMR) Flash is in Deep-power-down mode when system enters Wait Mode  */
#define   PMC_FSMR_FLPM_FLASH_IDLE_Val        (2U)                                           /**< (PMC_FSMR) Idle mode  */
#define PMC_FSMR_FLPM_FLASH_STANDBY           (PMC_FSMR_FLPM_FLASH_STANDBY_Val << PMC_FSMR_FLPM_Pos) /**< (PMC_FSMR) Flash is in Standby Mode when system enters Wait Mode Position  */
#define PMC_FSMR_FLPM_FLASH_DEEP_POWERDOWN    (PMC_FSMR_FLPM_FLASH_DEEP_POWERDOWN_Val << PMC_FSMR_FLPM_Pos) /**< (PMC_FSMR) Flash is in Deep-power-down mode when system enters Wait Mode Position  */
#define PMC_FSMR_FLPM_FLASH_IDLE              (PMC_FSMR_FLPM_FLASH_IDLE_Val << PMC_FSMR_FLPM_Pos) /**< (PMC_FSMR) Idle mode Position  */
#define PMC_FSMR_FFLPM_Pos                    (23U)                                          /**< (PMC_FSMR) Force Flash Low-power Mode Position */
#define PMC_FSMR_FFLPM_Msk                    (0x1U << PMC_FSMR_FFLPM_Pos)                   /**< (PMC_FSMR) Force Flash Low-power Mode Mask */
#define PMC_FSMR_FFLPM(value)                 (PMC_FSMR_FFLPM_Msk & ((value) << PMC_FSMR_FFLPM_Pos))
#define PMC_FSMR_Msk                          (0x00F7FFFFUL)                                 /**< (PMC_FSMR) Register Mask  */

/* -------- PMC_FSPR : (PMC Offset: 0x74) (R/W 32) Fast Startup Polarity Register -------- */
#define PMC_FSPR_FSTP0_Pos                    (0U)                                           /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP0_Msk                    (0x1U << PMC_FSPR_FSTP0_Pos)                   /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP0(value)                 (PMC_FSPR_FSTP0_Msk & ((value) << PMC_FSPR_FSTP0_Pos))
#define PMC_FSPR_FSTP1_Pos                    (1U)                                           /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP1_Msk                    (0x1U << PMC_FSPR_FSTP1_Pos)                   /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP1(value)                 (PMC_FSPR_FSTP1_Msk & ((value) << PMC_FSPR_FSTP1_Pos))
#define PMC_FSPR_FSTP2_Pos                    (2U)                                           /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP2_Msk                    (0x1U << PMC_FSPR_FSTP2_Pos)                   /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP2(value)                 (PMC_FSPR_FSTP2_Msk & ((value) << PMC_FSPR_FSTP2_Pos))
#define PMC_FSPR_FSTP3_Pos                    (3U)                                           /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP3_Msk                    (0x1U << PMC_FSPR_FSTP3_Pos)                   /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP3(value)                 (PMC_FSPR_FSTP3_Msk & ((value) << PMC_FSPR_FSTP3_Pos))
#define PMC_FSPR_FSTP4_Pos                    (4U)                                           /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP4_Msk                    (0x1U << PMC_FSPR_FSTP4_Pos)                   /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP4(value)                 (PMC_FSPR_FSTP4_Msk & ((value) << PMC_FSPR_FSTP4_Pos))
#define PMC_FSPR_FSTP5_Pos                    (5U)                                           /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP5_Msk                    (0x1U << PMC_FSPR_FSTP5_Pos)                   /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP5(value)                 (PMC_FSPR_FSTP5_Msk & ((value) << PMC_FSPR_FSTP5_Pos))
#define PMC_FSPR_FSTP6_Pos                    (6U)                                           /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP6_Msk                    (0x1U << PMC_FSPR_FSTP6_Pos)                   /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP6(value)                 (PMC_FSPR_FSTP6_Msk & ((value) << PMC_FSPR_FSTP6_Pos))
#define PMC_FSPR_FSTP7_Pos                    (7U)                                           /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP7_Msk                    (0x1U << PMC_FSPR_FSTP7_Pos)                   /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP7(value)                 (PMC_FSPR_FSTP7_Msk & ((value) << PMC_FSPR_FSTP7_Pos))
#define PMC_FSPR_FSTP8_Pos                    (8U)                                           /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP8_Msk                    (0x1U << PMC_FSPR_FSTP8_Pos)                   /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP8(value)                 (PMC_FSPR_FSTP8_Msk & ((value) << PMC_FSPR_FSTP8_Pos))
#define PMC_FSPR_FSTP9_Pos                    (9U)                                           /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP9_Msk                    (0x1U << PMC_FSPR_FSTP9_Pos)                   /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP9(value)                 (PMC_FSPR_FSTP9_Msk & ((value) << PMC_FSPR_FSTP9_Pos))
#define PMC_FSPR_FSTP10_Pos                   (10U)                                          /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP10_Msk                   (0x1U << PMC_FSPR_FSTP10_Pos)                  /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP10(value)                (PMC_FSPR_FSTP10_Msk & ((value) << PMC_FSPR_FSTP10_Pos))
#define PMC_FSPR_FSTP11_Pos                   (11U)                                          /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP11_Msk                   (0x1U << PMC_FSPR_FSTP11_Pos)                  /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP11(value)                (PMC_FSPR_FSTP11_Msk & ((value) << PMC_FSPR_FSTP11_Pos))
#define PMC_FSPR_FSTP12_Pos                   (12U)                                          /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP12_Msk                   (0x1U << PMC_FSPR_FSTP12_Pos)                  /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP12(value)                (PMC_FSPR_FSTP12_Msk & ((value) << PMC_FSPR_FSTP12_Pos))
#define PMC_FSPR_FSTP13_Pos                   (13U)                                          /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP13_Msk                   (0x1U << PMC_FSPR_FSTP13_Pos)                  /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP13(value)                (PMC_FSPR_FSTP13_Msk & ((value) << PMC_FSPR_FSTP13_Pos))
#define PMC_FSPR_FSTP14_Pos                   (14U)                                          /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP14_Msk                   (0x1U << PMC_FSPR_FSTP14_Pos)                  /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP14(value)                (PMC_FSPR_FSTP14_Msk & ((value) << PMC_FSPR_FSTP14_Pos))
#define PMC_FSPR_FSTP15_Pos                   (15U)                                          /**< (PMC_FSPR) Fast Startup Input Polarityx Position */
#define PMC_FSPR_FSTP15_Msk                   (0x1U << PMC_FSPR_FSTP15_Pos)                  /**< (PMC_FSPR) Fast Startup Input Polarityx Mask */
#define PMC_FSPR_FSTP15(value)                (PMC_FSPR_FSTP15_Msk & ((value) << PMC_FSPR_FSTP15_Pos))
#define PMC_FSPR_Msk                          (0x0000FFFFUL)                                 /**< (PMC_FSPR) Register Mask  */

/* -------- PMC_FOCR : (PMC Offset: 0x78) ( /W 32) Fault Output Clear Register -------- */
#define PMC_FOCR_FOCLR_Pos                    (0U)                                           /**< (PMC_FOCR) Fault Output Clear Position */
#define PMC_FOCR_FOCLR_Msk                    (0x1U << PMC_FOCR_FOCLR_Pos)                   /**< (PMC_FOCR) Fault Output Clear Mask */
#define PMC_FOCR_FOCLR(value)                 (PMC_FOCR_FOCLR_Msk & ((value) << PMC_FOCR_FOCLR_Pos))
#define PMC_FOCR_Msk                          (0x00000001UL)                                 /**< (PMC_FOCR) Register Mask  */

/* -------- PMC_WPMR : (PMC Offset: 0xE4) (R/W 32) Write Protection Mode Register -------- */
#define PMC_WPMR_WPEN_Pos                     (0U)                                           /**< (PMC_WPMR) Write Protection Enable Position */
#define PMC_WPMR_WPEN_Msk                     (0x1U << PMC_WPMR_WPEN_Pos)                    /**< (PMC_WPMR) Write Protection Enable Mask */
#define PMC_WPMR_WPEN(value)                  (PMC_WPMR_WPEN_Msk & ((value) << PMC_WPMR_WPEN_Pos))
#define PMC_WPMR_WPKEY_Pos                    (8U)                                           /**< (PMC_WPMR) Write Protection Key Position */
#define PMC_WPMR_WPKEY_Msk                    (0xFFFFFFU << PMC_WPMR_WPKEY_Pos)              /**< (PMC_WPMR) Write Protection Key Mask */
#define PMC_WPMR_WPKEY(value)                 (PMC_WPMR_WPKEY_Msk & ((value) << PMC_WPMR_WPKEY_Pos))
#define   PMC_WPMR_WPKEY_PASSWD_Val           (5262659U)                                     /**< (PMC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit. Always reads as 0.  */
#define PMC_WPMR_WPKEY_PASSWD                 (PMC_WPMR_WPKEY_PASSWD_Val << PMC_WPMR_WPKEY_Pos) /**< (PMC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit. Always reads as 0. Position  */
#define PMC_WPMR_Msk                          (0xFFFFFF01UL)                                 /**< (PMC_WPMR) Register Mask  */

/* -------- PMC_WPSR : (PMC Offset: 0xE8) (R/  32) Write Protection Status Register -------- */
#define PMC_WPSR_WPVS_Pos                     (0U)                                           /**< (PMC_WPSR) Write Protection Violation Status Position */
#define PMC_WPSR_WPVS_Msk                     (0x1U << PMC_WPSR_WPVS_Pos)                    /**< (PMC_WPSR) Write Protection Violation Status Mask */
#define PMC_WPSR_WPVS(value)                  (PMC_WPSR_WPVS_Msk & ((value) << PMC_WPSR_WPVS_Pos))
#define PMC_WPSR_WPVSRC_Pos                   (8U)                                           /**< (PMC_WPSR) Write Protection Violation Source Position */
#define PMC_WPSR_WPVSRC_Msk                   (0xFFFFU << PMC_WPSR_WPVSRC_Pos)               /**< (PMC_WPSR) Write Protection Violation Source Mask */
#define PMC_WPSR_WPVSRC(value)                (PMC_WPSR_WPVSRC_Msk & ((value) << PMC_WPSR_WPVSRC_Pos))
#define PMC_WPSR_Msk                          (0x00FFFF01UL)                                 /**< (PMC_WPSR) Register Mask  */

/* -------- PMC_PCER1 : (PMC Offset: 0x100) ( /W 32) Peripheral Clock Enable Register 1 -------- */
#define PMC_PCER1_PID47_Pos                   (15U)                                          /**< (PMC_PCER1) Peripheral Clock 47 Enable Position */
#define PMC_PCER1_PID47_Msk                   (0x1U << PMC_PCER1_PID47_Pos)                  /**< (PMC_PCER1) Peripheral Clock 47 Enable Mask */
#define PMC_PCER1_PID47(value)                (PMC_PCER1_PID47_Msk & ((value) << PMC_PCER1_PID47_Pos))
#define PMC_PCER1_PID48_Pos                   (16U)                                          /**< (PMC_PCER1) Peripheral Clock 48 Enable Position */
#define PMC_PCER1_PID48_Msk                   (0x1U << PMC_PCER1_PID48_Pos)                  /**< (PMC_PCER1) Peripheral Clock 48 Enable Mask */
#define PMC_PCER1_PID48(value)                (PMC_PCER1_PID48_Msk & ((value) << PMC_PCER1_PID48_Pos))
#define PMC_PCER1_PID49_Pos                   (17U)                                          /**< (PMC_PCER1) Peripheral Clock 49 Enable Position */
#define PMC_PCER1_PID49_Msk                   (0x1U << PMC_PCER1_PID49_Pos)                  /**< (PMC_PCER1) Peripheral Clock 49 Enable Mask */
#define PMC_PCER1_PID49(value)                (PMC_PCER1_PID49_Msk & ((value) << PMC_PCER1_PID49_Pos))
#define PMC_PCER1_Msk                         (0x00038000UL)                                 /**< (PMC_PCER1) Register Mask  */

/* -------- PMC_PCDR1 : (PMC Offset: 0x104) ( /W 32) Peripheral Clock Disable Register 1 -------- */
#define PMC_PCDR1_PID47_Pos                   (15U)                                          /**< (PMC_PCDR1) Peripheral Clock 47 Disable Position */
#define PMC_PCDR1_PID47_Msk                   (0x1U << PMC_PCDR1_PID47_Pos)                  /**< (PMC_PCDR1) Peripheral Clock 47 Disable Mask */
#define PMC_PCDR1_PID47(value)                (PMC_PCDR1_PID47_Msk & ((value) << PMC_PCDR1_PID47_Pos))
#define PMC_PCDR1_PID48_Pos                   (16U)                                          /**< (PMC_PCDR1) Peripheral Clock 48 Disable Position */
#define PMC_PCDR1_PID48_Msk                   (0x1U << PMC_PCDR1_PID48_Pos)                  /**< (PMC_PCDR1) Peripheral Clock 48 Disable Mask */
#define PMC_PCDR1_PID48(value)                (PMC_PCDR1_PID48_Msk & ((value) << PMC_PCDR1_PID48_Pos))
#define PMC_PCDR1_PID49_Pos                   (17U)                                          /**< (PMC_PCDR1) Peripheral Clock 49 Disable Position */
#define PMC_PCDR1_PID49_Msk                   (0x1U << PMC_PCDR1_PID49_Pos)                  /**< (PMC_PCDR1) Peripheral Clock 49 Disable Mask */
#define PMC_PCDR1_PID49(value)                (PMC_PCDR1_PID49_Msk & ((value) << PMC_PCDR1_PID49_Pos))
#define PMC_PCDR1_Msk                         (0x00038000UL)                                 /**< (PMC_PCDR1) Register Mask  */

/* -------- PMC_PCSR1 : (PMC Offset: 0x108) (R/  32) Peripheral Clock Status Register 1 -------- */
#define PMC_PCSR1_PID47_Pos                   (15U)                                          /**< (PMC_PCSR1) Peripheral Clock 47 Status Position */
#define PMC_PCSR1_PID47_Msk                   (0x1U << PMC_PCSR1_PID47_Pos)                  /**< (PMC_PCSR1) Peripheral Clock 47 Status Mask */
#define PMC_PCSR1_PID47(value)                (PMC_PCSR1_PID47_Msk & ((value) << PMC_PCSR1_PID47_Pos))
#define PMC_PCSR1_PID48_Pos                   (16U)                                          /**< (PMC_PCSR1) Peripheral Clock 48 Status Position */
#define PMC_PCSR1_PID48_Msk                   (0x1U << PMC_PCSR1_PID48_Pos)                  /**< (PMC_PCSR1) Peripheral Clock 48 Status Mask */
#define PMC_PCSR1_PID48(value)                (PMC_PCSR1_PID48_Msk & ((value) << PMC_PCSR1_PID48_Pos))
#define PMC_PCSR1_PID49_Pos                   (17U)                                          /**< (PMC_PCSR1) Peripheral Clock 49 Status Position */
#define PMC_PCSR1_PID49_Msk                   (0x1U << PMC_PCSR1_PID49_Pos)                  /**< (PMC_PCSR1) Peripheral Clock 49 Status Mask */
#define PMC_PCSR1_PID49(value)                (PMC_PCSR1_PID49_Msk & ((value) << PMC_PCSR1_PID49_Pos))
#define PMC_PCSR1_Msk                         (0x00038000UL)                                 /**< (PMC_PCSR1) Register Mask  */

/* -------- PMC_PCR : (PMC Offset: 0x10C) (R/W 32) Peripheral Control Register -------- */
#define PMC_PCR_PID_Pos                       (0U)                                           /**< (PMC_PCR) Peripheral ID Position */
#define PMC_PCR_PID_Msk                       (0x3FU << PMC_PCR_PID_Pos)                     /**< (PMC_PCR) Peripheral ID Mask */
#define PMC_PCR_PID(value)                    (PMC_PCR_PID_Msk & ((value) << PMC_PCR_PID_Pos))
#define PMC_PCR_CMD_Pos                       (12U)                                          /**< (PMC_PCR) Command Position */
#define PMC_PCR_CMD_Msk                       (0x1U << PMC_PCR_CMD_Pos)                      /**< (PMC_PCR) Command Mask */
#define PMC_PCR_CMD(value)                    (PMC_PCR_CMD_Msk & ((value) << PMC_PCR_CMD_Pos))
#define PMC_PCR_DIV_Pos                       (16U)                                          /**< (PMC_PCR) Divisor Value Position */
#define PMC_PCR_DIV_Msk                       (0x3U << PMC_PCR_DIV_Pos)                      /**< (PMC_PCR) Divisor Value Mask */
#define PMC_PCR_DIV(value)                    (PMC_PCR_DIV_Msk & ((value) << PMC_PCR_DIV_Pos))
#define   PMC_PCR_DIV_PERIPH_DIV_MCK_Val      (0U)                                           /**< (PMC_PCR) Peripheral clock is MCK  */
#define   PMC_PCR_DIV_PERIPH_DIV2_MCK_Val     (1U)                                           /**< (PMC_PCR) Peripheral clock is MCK/2  */
#define   PMC_PCR_DIV_PERIPH_DIV4_MCK_Val     (2U)                                           /**< (PMC_PCR) Peripheral clock is MCK/4  */
#define   PMC_PCR_DIV_PERIPH_DIV8_MCK_Val     (3U)                                           /**< (PMC_PCR) Peripheral clock is MCK/8  */
#define PMC_PCR_DIV_PERIPH_DIV_MCK            (PMC_PCR_DIV_PERIPH_DIV_MCK_Val << PMC_PCR_DIV_Pos) /**< (PMC_PCR) Peripheral clock is MCK Position  */
#define PMC_PCR_DIV_PERIPH_DIV2_MCK           (PMC_PCR_DIV_PERIPH_DIV2_MCK_Val << PMC_PCR_DIV_Pos) /**< (PMC_PCR) Peripheral clock is MCK/2 Position  */
#define PMC_PCR_DIV_PERIPH_DIV4_MCK           (PMC_PCR_DIV_PERIPH_DIV4_MCK_Val << PMC_PCR_DIV_Pos) /**< (PMC_PCR) Peripheral clock is MCK/4 Position  */
#define PMC_PCR_DIV_PERIPH_DIV8_MCK           (PMC_PCR_DIV_PERIPH_DIV8_MCK_Val << PMC_PCR_DIV_Pos) /**< (PMC_PCR) Peripheral clock is MCK/8 Position  */
#define PMC_PCR_EN_Pos                        (28U)                                          /**< (PMC_PCR) Enable Position */
#define PMC_PCR_EN_Msk                        (0x1U << PMC_PCR_EN_Pos)                       /**< (PMC_PCR) Enable Mask */
#define PMC_PCR_EN(value)                     (PMC_PCR_EN_Msk & ((value) << PMC_PCR_EN_Pos))
#define PMC_PCR_Msk                           (0x1003103FUL)                                 /**< (PMC_PCR) Register Mask  */

/* -------- PMC_OCR : (PMC Offset: 0x110) (R/W 32) Oscillator Calibration Register -------- */
#define PMC_OCR_CAL8_Pos                      (0U)                                           /**< (PMC_OCR) RC Oscillator Calibration bits for 8 MHz Position */
#define PMC_OCR_CAL8_Msk                      (0x7FU << PMC_OCR_CAL8_Pos)                    /**< (PMC_OCR) RC Oscillator Calibration bits for 8 MHz Mask */
#define PMC_OCR_CAL8(value)                   (PMC_OCR_CAL8_Msk & ((value) << PMC_OCR_CAL8_Pos))
#define PMC_OCR_SEL8_Pos                      (7U)                                           /**< (PMC_OCR) Selection of RC Oscillator Calibration bits for 8 MHz Position */
#define PMC_OCR_SEL8_Msk                      (0x1U << PMC_OCR_SEL8_Pos)                     /**< (PMC_OCR) Selection of RC Oscillator Calibration bits for 8 MHz Mask */
#define PMC_OCR_SEL8(value)                   (PMC_OCR_SEL8_Msk & ((value) << PMC_OCR_SEL8_Pos))
#define PMC_OCR_CAL16_Pos                     (8U)                                           /**< (PMC_OCR) RC Oscillator Calibration bits for 16 MHz Position */
#define PMC_OCR_CAL16_Msk                     (0x7FU << PMC_OCR_CAL16_Pos)                   /**< (PMC_OCR) RC Oscillator Calibration bits for 16 MHz Mask */
#define PMC_OCR_CAL16(value)                  (PMC_OCR_CAL16_Msk & ((value) << PMC_OCR_CAL16_Pos))
#define PMC_OCR_SEL16_Pos                     (15U)                                          /**< (PMC_OCR) Selection of RC Oscillator Calibration bits for 16 MHz Position */
#define PMC_OCR_SEL16_Msk                     (0x1U << PMC_OCR_SEL16_Pos)                    /**< (PMC_OCR) Selection of RC Oscillator Calibration bits for 16 MHz Mask */
#define PMC_OCR_SEL16(value)                  (PMC_OCR_SEL16_Msk & ((value) << PMC_OCR_SEL16_Pos))
#define PMC_OCR_CAL24_Pos                     (16U)                                          /**< (PMC_OCR) RC Oscillator Calibration bits for 24 MHz Position */
#define PMC_OCR_CAL24_Msk                     (0x7FU << PMC_OCR_CAL24_Pos)                   /**< (PMC_OCR) RC Oscillator Calibration bits for 24 MHz Mask */
#define PMC_OCR_CAL24(value)                  (PMC_OCR_CAL24_Msk & ((value) << PMC_OCR_CAL24_Pos))
#define PMC_OCR_SEL24_Pos                     (23U)                                          /**< (PMC_OCR) Selection of RC Oscillator Calibration bits for 24 MHz Position */
#define PMC_OCR_SEL24_Msk                     (0x1U << PMC_OCR_SEL24_Pos)                    /**< (PMC_OCR) Selection of RC Oscillator Calibration bits for 24 MHz Mask */
#define PMC_OCR_SEL24(value)                  (PMC_OCR_SEL24_Msk & ((value) << PMC_OCR_SEL24_Pos))
#define PMC_OCR_Msk                           (0x00FFFFFFUL)                                 /**< (PMC_OCR) Register Mask  */

/* -------- PMC_SLPWK_ER0 : (PMC Offset: 0x114) ( /W 32) SleepWalking Enable Register 0 -------- */
#define PMC_SLPWK_ER0_PID8_Pos                (8U)                                           /**< (PMC_SLPWK_ER0) Peripheral 8 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID8_Msk                (0x1U << PMC_SLPWK_ER0_PID8_Pos)               /**< (PMC_SLPWK_ER0) Peripheral 8 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID8(value)             (PMC_SLPWK_ER0_PID8_Msk & ((value) << PMC_SLPWK_ER0_PID8_Pos))
#define PMC_SLPWK_ER0_PID9_Pos                (9U)                                           /**< (PMC_SLPWK_ER0) Peripheral 9 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID9_Msk                (0x1U << PMC_SLPWK_ER0_PID9_Pos)               /**< (PMC_SLPWK_ER0) Peripheral 9 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID9(value)             (PMC_SLPWK_ER0_PID9_Msk & ((value) << PMC_SLPWK_ER0_PID9_Pos))
#define PMC_SLPWK_ER0_PID10_Pos               (10U)                                          /**< (PMC_SLPWK_ER0) Peripheral 10 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID10_Msk               (0x1U << PMC_SLPWK_ER0_PID10_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 10 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID10(value)            (PMC_SLPWK_ER0_PID10_Msk & ((value) << PMC_SLPWK_ER0_PID10_Pos))
#define PMC_SLPWK_ER0_PID11_Pos               (11U)                                          /**< (PMC_SLPWK_ER0) Peripheral 11 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID11_Msk               (0x1U << PMC_SLPWK_ER0_PID11_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 11 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID11(value)            (PMC_SLPWK_ER0_PID11_Msk & ((value) << PMC_SLPWK_ER0_PID11_Pos))
#define PMC_SLPWK_ER0_PID12_Pos               (12U)                                          /**< (PMC_SLPWK_ER0) Peripheral 12 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID12_Msk               (0x1U << PMC_SLPWK_ER0_PID12_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 12 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID12(value)            (PMC_SLPWK_ER0_PID12_Msk & ((value) << PMC_SLPWK_ER0_PID12_Pos))
#define PMC_SLPWK_ER0_PID13_Pos               (13U)                                          /**< (PMC_SLPWK_ER0) Peripheral 13 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID13_Msk               (0x1U << PMC_SLPWK_ER0_PID13_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 13 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID13(value)            (PMC_SLPWK_ER0_PID13_Msk & ((value) << PMC_SLPWK_ER0_PID13_Pos))
#define PMC_SLPWK_ER0_PID14_Pos               (14U)                                          /**< (PMC_SLPWK_ER0) Peripheral 14 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID14_Msk               (0x1U << PMC_SLPWK_ER0_PID14_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 14 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID14(value)            (PMC_SLPWK_ER0_PID14_Msk & ((value) << PMC_SLPWK_ER0_PID14_Pos))
#define PMC_SLPWK_ER0_PID15_Pos               (15U)                                          /**< (PMC_SLPWK_ER0) Peripheral 15 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID15_Msk               (0x1U << PMC_SLPWK_ER0_PID15_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 15 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID15(value)            (PMC_SLPWK_ER0_PID15_Msk & ((value) << PMC_SLPWK_ER0_PID15_Pos))
#define PMC_SLPWK_ER0_PID16_Pos               (16U)                                          /**< (PMC_SLPWK_ER0) Peripheral 16 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID16_Msk               (0x1U << PMC_SLPWK_ER0_PID16_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 16 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID16(value)            (PMC_SLPWK_ER0_PID16_Msk & ((value) << PMC_SLPWK_ER0_PID16_Pos))
#define PMC_SLPWK_ER0_PID17_Pos               (17U)                                          /**< (PMC_SLPWK_ER0) Peripheral 17 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID17_Msk               (0x1U << PMC_SLPWK_ER0_PID17_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 17 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID17(value)            (PMC_SLPWK_ER0_PID17_Msk & ((value) << PMC_SLPWK_ER0_PID17_Pos))
#define PMC_SLPWK_ER0_PID18_Pos               (18U)                                          /**< (PMC_SLPWK_ER0) Peripheral 18 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID18_Msk               (0x1U << PMC_SLPWK_ER0_PID18_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 18 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID18(value)            (PMC_SLPWK_ER0_PID18_Msk & ((value) << PMC_SLPWK_ER0_PID18_Pos))
#define PMC_SLPWK_ER0_PID19_Pos               (19U)                                          /**< (PMC_SLPWK_ER0) Peripheral 19 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID19_Msk               (0x1U << PMC_SLPWK_ER0_PID19_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 19 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID19(value)            (PMC_SLPWK_ER0_PID19_Msk & ((value) << PMC_SLPWK_ER0_PID19_Pos))
#define PMC_SLPWK_ER0_PID20_Pos               (20U)                                          /**< (PMC_SLPWK_ER0) Peripheral 20 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID20_Msk               (0x1U << PMC_SLPWK_ER0_PID20_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 20 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID20(value)            (PMC_SLPWK_ER0_PID20_Msk & ((value) << PMC_SLPWK_ER0_PID20_Pos))
#define PMC_SLPWK_ER0_PID21_Pos               (21U)                                          /**< (PMC_SLPWK_ER0) Peripheral 21 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID21_Msk               (0x1U << PMC_SLPWK_ER0_PID21_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 21 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID21(value)            (PMC_SLPWK_ER0_PID21_Msk & ((value) << PMC_SLPWK_ER0_PID21_Pos))
#define PMC_SLPWK_ER0_PID22_Pos               (22U)                                          /**< (PMC_SLPWK_ER0) Peripheral 22 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID22_Msk               (0x1U << PMC_SLPWK_ER0_PID22_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 22 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID22(value)            (PMC_SLPWK_ER0_PID22_Msk & ((value) << PMC_SLPWK_ER0_PID22_Pos))
#define PMC_SLPWK_ER0_PID23_Pos               (23U)                                          /**< (PMC_SLPWK_ER0) Peripheral 23 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID23_Msk               (0x1U << PMC_SLPWK_ER0_PID23_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 23 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID23(value)            (PMC_SLPWK_ER0_PID23_Msk & ((value) << PMC_SLPWK_ER0_PID23_Pos))
#define PMC_SLPWK_ER0_PID24_Pos               (24U)                                          /**< (PMC_SLPWK_ER0) Peripheral 24 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID24_Msk               (0x1U << PMC_SLPWK_ER0_PID24_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 24 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID24(value)            (PMC_SLPWK_ER0_PID24_Msk & ((value) << PMC_SLPWK_ER0_PID24_Pos))
#define PMC_SLPWK_ER0_PID25_Pos               (25U)                                          /**< (PMC_SLPWK_ER0) Peripheral 25 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID25_Msk               (0x1U << PMC_SLPWK_ER0_PID25_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 25 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID25(value)            (PMC_SLPWK_ER0_PID25_Msk & ((value) << PMC_SLPWK_ER0_PID25_Pos))
#define PMC_SLPWK_ER0_PID26_Pos               (26U)                                          /**< (PMC_SLPWK_ER0) Peripheral 26 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID26_Msk               (0x1U << PMC_SLPWK_ER0_PID26_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 26 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID26(value)            (PMC_SLPWK_ER0_PID26_Msk & ((value) << PMC_SLPWK_ER0_PID26_Pos))
#define PMC_SLPWK_ER0_PID27_Pos               (27U)                                          /**< (PMC_SLPWK_ER0) Peripheral 27 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID27_Msk               (0x1U << PMC_SLPWK_ER0_PID27_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 27 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID27(value)            (PMC_SLPWK_ER0_PID27_Msk & ((value) << PMC_SLPWK_ER0_PID27_Pos))
#define PMC_SLPWK_ER0_PID28_Pos               (28U)                                          /**< (PMC_SLPWK_ER0) Peripheral 28 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID28_Msk               (0x1U << PMC_SLPWK_ER0_PID28_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 28 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID28(value)            (PMC_SLPWK_ER0_PID28_Msk & ((value) << PMC_SLPWK_ER0_PID28_Pos))
#define PMC_SLPWK_ER0_PID29_Pos               (29U)                                          /**< (PMC_SLPWK_ER0) Peripheral 29 SleepWalking Enable Position */
#define PMC_SLPWK_ER0_PID29_Msk               (0x1U << PMC_SLPWK_ER0_PID29_Pos)              /**< (PMC_SLPWK_ER0) Peripheral 29 SleepWalking Enable Mask */
#define PMC_SLPWK_ER0_PID29(value)            (PMC_SLPWK_ER0_PID29_Msk & ((value) << PMC_SLPWK_ER0_PID29_Pos))
#define PMC_SLPWK_ER0_Msk                     (0x3FFFFF00UL)                                 /**< (PMC_SLPWK_ER0) Register Mask  */

/* -------- PMC_SLPWK_DR0 : (PMC Offset: 0x118) ( /W 32) SleepWalking Disable Register 0 -------- */
#define PMC_SLPWK_DR0_PID8_Pos                (8U)                                           /**< (PMC_SLPWK_DR0) Peripheral 8 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID8_Msk                (0x1U << PMC_SLPWK_DR0_PID8_Pos)               /**< (PMC_SLPWK_DR0) Peripheral 8 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID8(value)             (PMC_SLPWK_DR0_PID8_Msk & ((value) << PMC_SLPWK_DR0_PID8_Pos))
#define PMC_SLPWK_DR0_PID9_Pos                (9U)                                           /**< (PMC_SLPWK_DR0) Peripheral 9 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID9_Msk                (0x1U << PMC_SLPWK_DR0_PID9_Pos)               /**< (PMC_SLPWK_DR0) Peripheral 9 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID9(value)             (PMC_SLPWK_DR0_PID9_Msk & ((value) << PMC_SLPWK_DR0_PID9_Pos))
#define PMC_SLPWK_DR0_PID10_Pos               (10U)                                          /**< (PMC_SLPWK_DR0) Peripheral 10 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID10_Msk               (0x1U << PMC_SLPWK_DR0_PID10_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 10 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID10(value)            (PMC_SLPWK_DR0_PID10_Msk & ((value) << PMC_SLPWK_DR0_PID10_Pos))
#define PMC_SLPWK_DR0_PID11_Pos               (11U)                                          /**< (PMC_SLPWK_DR0) Peripheral 11 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID11_Msk               (0x1U << PMC_SLPWK_DR0_PID11_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 11 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID11(value)            (PMC_SLPWK_DR0_PID11_Msk & ((value) << PMC_SLPWK_DR0_PID11_Pos))
#define PMC_SLPWK_DR0_PID12_Pos               (12U)                                          /**< (PMC_SLPWK_DR0) Peripheral 12 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID12_Msk               (0x1U << PMC_SLPWK_DR0_PID12_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 12 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID12(value)            (PMC_SLPWK_DR0_PID12_Msk & ((value) << PMC_SLPWK_DR0_PID12_Pos))
#define PMC_SLPWK_DR0_PID13_Pos               (13U)                                          /**< (PMC_SLPWK_DR0) Peripheral 13 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID13_Msk               (0x1U << PMC_SLPWK_DR0_PID13_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 13 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID13(value)            (PMC_SLPWK_DR0_PID13_Msk & ((value) << PMC_SLPWK_DR0_PID13_Pos))
#define PMC_SLPWK_DR0_PID14_Pos               (14U)                                          /**< (PMC_SLPWK_DR0) Peripheral 14 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID14_Msk               (0x1U << PMC_SLPWK_DR0_PID14_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 14 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID14(value)            (PMC_SLPWK_DR0_PID14_Msk & ((value) << PMC_SLPWK_DR0_PID14_Pos))
#define PMC_SLPWK_DR0_PID15_Pos               (15U)                                          /**< (PMC_SLPWK_DR0) Peripheral 15 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID15_Msk               (0x1U << PMC_SLPWK_DR0_PID15_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 15 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID15(value)            (PMC_SLPWK_DR0_PID15_Msk & ((value) << PMC_SLPWK_DR0_PID15_Pos))
#define PMC_SLPWK_DR0_PID16_Pos               (16U)                                          /**< (PMC_SLPWK_DR0) Peripheral 16 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID16_Msk               (0x1U << PMC_SLPWK_DR0_PID16_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 16 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID16(value)            (PMC_SLPWK_DR0_PID16_Msk & ((value) << PMC_SLPWK_DR0_PID16_Pos))
#define PMC_SLPWK_DR0_PID17_Pos               (17U)                                          /**< (PMC_SLPWK_DR0) Peripheral 17 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID17_Msk               (0x1U << PMC_SLPWK_DR0_PID17_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 17 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID17(value)            (PMC_SLPWK_DR0_PID17_Msk & ((value) << PMC_SLPWK_DR0_PID17_Pos))
#define PMC_SLPWK_DR0_PID18_Pos               (18U)                                          /**< (PMC_SLPWK_DR0) Peripheral 18 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID18_Msk               (0x1U << PMC_SLPWK_DR0_PID18_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 18 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID18(value)            (PMC_SLPWK_DR0_PID18_Msk & ((value) << PMC_SLPWK_DR0_PID18_Pos))
#define PMC_SLPWK_DR0_PID19_Pos               (19U)                                          /**< (PMC_SLPWK_DR0) Peripheral 19 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID19_Msk               (0x1U << PMC_SLPWK_DR0_PID19_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 19 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID19(value)            (PMC_SLPWK_DR0_PID19_Msk & ((value) << PMC_SLPWK_DR0_PID19_Pos))
#define PMC_SLPWK_DR0_PID20_Pos               (20U)                                          /**< (PMC_SLPWK_DR0) Peripheral 20 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID20_Msk               (0x1U << PMC_SLPWK_DR0_PID20_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 20 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID20(value)            (PMC_SLPWK_DR0_PID20_Msk & ((value) << PMC_SLPWK_DR0_PID20_Pos))
#define PMC_SLPWK_DR0_PID21_Pos               (21U)                                          /**< (PMC_SLPWK_DR0) Peripheral 21 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID21_Msk               (0x1U << PMC_SLPWK_DR0_PID21_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 21 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID21(value)            (PMC_SLPWK_DR0_PID21_Msk & ((value) << PMC_SLPWK_DR0_PID21_Pos))
#define PMC_SLPWK_DR0_PID22_Pos               (22U)                                          /**< (PMC_SLPWK_DR0) Peripheral 22 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID22_Msk               (0x1U << PMC_SLPWK_DR0_PID22_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 22 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID22(value)            (PMC_SLPWK_DR0_PID22_Msk & ((value) << PMC_SLPWK_DR0_PID22_Pos))
#define PMC_SLPWK_DR0_PID23_Pos               (23U)                                          /**< (PMC_SLPWK_DR0) Peripheral 23 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID23_Msk               (0x1U << PMC_SLPWK_DR0_PID23_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 23 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID23(value)            (PMC_SLPWK_DR0_PID23_Msk & ((value) << PMC_SLPWK_DR0_PID23_Pos))
#define PMC_SLPWK_DR0_PID24_Pos               (24U)                                          /**< (PMC_SLPWK_DR0) Peripheral 24 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID24_Msk               (0x1U << PMC_SLPWK_DR0_PID24_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 24 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID24(value)            (PMC_SLPWK_DR0_PID24_Msk & ((value) << PMC_SLPWK_DR0_PID24_Pos))
#define PMC_SLPWK_DR0_PID25_Pos               (25U)                                          /**< (PMC_SLPWK_DR0) Peripheral 25 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID25_Msk               (0x1U << PMC_SLPWK_DR0_PID25_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 25 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID25(value)            (PMC_SLPWK_DR0_PID25_Msk & ((value) << PMC_SLPWK_DR0_PID25_Pos))
#define PMC_SLPWK_DR0_PID26_Pos               (26U)                                          /**< (PMC_SLPWK_DR0) Peripheral 26 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID26_Msk               (0x1U << PMC_SLPWK_DR0_PID26_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 26 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID26(value)            (PMC_SLPWK_DR0_PID26_Msk & ((value) << PMC_SLPWK_DR0_PID26_Pos))
#define PMC_SLPWK_DR0_PID27_Pos               (27U)                                          /**< (PMC_SLPWK_DR0) Peripheral 27 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID27_Msk               (0x1U << PMC_SLPWK_DR0_PID27_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 27 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID27(value)            (PMC_SLPWK_DR0_PID27_Msk & ((value) << PMC_SLPWK_DR0_PID27_Pos))
#define PMC_SLPWK_DR0_PID28_Pos               (28U)                                          /**< (PMC_SLPWK_DR0) Peripheral 28 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID28_Msk               (0x1U << PMC_SLPWK_DR0_PID28_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 28 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID28(value)            (PMC_SLPWK_DR0_PID28_Msk & ((value) << PMC_SLPWK_DR0_PID28_Pos))
#define PMC_SLPWK_DR0_PID29_Pos               (29U)                                          /**< (PMC_SLPWK_DR0) Peripheral 29 SleepWalking Disable Position */
#define PMC_SLPWK_DR0_PID29_Msk               (0x1U << PMC_SLPWK_DR0_PID29_Pos)              /**< (PMC_SLPWK_DR0) Peripheral 29 SleepWalking Disable Mask */
#define PMC_SLPWK_DR0_PID29(value)            (PMC_SLPWK_DR0_PID29_Msk & ((value) << PMC_SLPWK_DR0_PID29_Pos))
#define PMC_SLPWK_DR0_Msk                     (0x3FFFFF00UL)                                 /**< (PMC_SLPWK_DR0) Register Mask  */

/* -------- PMC_SLPWK_SR0 : (PMC Offset: 0x11C) (R/  32) SleepWalking Status Register 0 -------- */
#define PMC_SLPWK_SR0_PID8_Pos                (8U)                                           /**< (PMC_SLPWK_SR0) Peripheral 8 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID8_Msk                (0x1U << PMC_SLPWK_SR0_PID8_Pos)               /**< (PMC_SLPWK_SR0) Peripheral 8 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID8(value)             (PMC_SLPWK_SR0_PID8_Msk & ((value) << PMC_SLPWK_SR0_PID8_Pos))
#define PMC_SLPWK_SR0_PID9_Pos                (9U)                                           /**< (PMC_SLPWK_SR0) Peripheral 9 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID9_Msk                (0x1U << PMC_SLPWK_SR0_PID9_Pos)               /**< (PMC_SLPWK_SR0) Peripheral 9 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID9(value)             (PMC_SLPWK_SR0_PID9_Msk & ((value) << PMC_SLPWK_SR0_PID9_Pos))
#define PMC_SLPWK_SR0_PID10_Pos               (10U)                                          /**< (PMC_SLPWK_SR0) Peripheral 10 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID10_Msk               (0x1U << PMC_SLPWK_SR0_PID10_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 10 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID10(value)            (PMC_SLPWK_SR0_PID10_Msk & ((value) << PMC_SLPWK_SR0_PID10_Pos))
#define PMC_SLPWK_SR0_PID11_Pos               (11U)                                          /**< (PMC_SLPWK_SR0) Peripheral 11 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID11_Msk               (0x1U << PMC_SLPWK_SR0_PID11_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 11 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID11(value)            (PMC_SLPWK_SR0_PID11_Msk & ((value) << PMC_SLPWK_SR0_PID11_Pos))
#define PMC_SLPWK_SR0_PID12_Pos               (12U)                                          /**< (PMC_SLPWK_SR0) Peripheral 12 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID12_Msk               (0x1U << PMC_SLPWK_SR0_PID12_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 12 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID12(value)            (PMC_SLPWK_SR0_PID12_Msk & ((value) << PMC_SLPWK_SR0_PID12_Pos))
#define PMC_SLPWK_SR0_PID13_Pos               (13U)                                          /**< (PMC_SLPWK_SR0) Peripheral 13 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID13_Msk               (0x1U << PMC_SLPWK_SR0_PID13_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 13 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID13(value)            (PMC_SLPWK_SR0_PID13_Msk & ((value) << PMC_SLPWK_SR0_PID13_Pos))
#define PMC_SLPWK_SR0_PID14_Pos               (14U)                                          /**< (PMC_SLPWK_SR0) Peripheral 14 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID14_Msk               (0x1U << PMC_SLPWK_SR0_PID14_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 14 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID14(value)            (PMC_SLPWK_SR0_PID14_Msk & ((value) << PMC_SLPWK_SR0_PID14_Pos))
#define PMC_SLPWK_SR0_PID15_Pos               (15U)                                          /**< (PMC_SLPWK_SR0) Peripheral 15 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID15_Msk               (0x1U << PMC_SLPWK_SR0_PID15_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 15 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID15(value)            (PMC_SLPWK_SR0_PID15_Msk & ((value) << PMC_SLPWK_SR0_PID15_Pos))
#define PMC_SLPWK_SR0_PID16_Pos               (16U)                                          /**< (PMC_SLPWK_SR0) Peripheral 16 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID16_Msk               (0x1U << PMC_SLPWK_SR0_PID16_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 16 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID16(value)            (PMC_SLPWK_SR0_PID16_Msk & ((value) << PMC_SLPWK_SR0_PID16_Pos))
#define PMC_SLPWK_SR0_PID17_Pos               (17U)                                          /**< (PMC_SLPWK_SR0) Peripheral 17 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID17_Msk               (0x1U << PMC_SLPWK_SR0_PID17_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 17 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID17(value)            (PMC_SLPWK_SR0_PID17_Msk & ((value) << PMC_SLPWK_SR0_PID17_Pos))
#define PMC_SLPWK_SR0_PID18_Pos               (18U)                                          /**< (PMC_SLPWK_SR0) Peripheral 18 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID18_Msk               (0x1U << PMC_SLPWK_SR0_PID18_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 18 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID18(value)            (PMC_SLPWK_SR0_PID18_Msk & ((value) << PMC_SLPWK_SR0_PID18_Pos))
#define PMC_SLPWK_SR0_PID19_Pos               (19U)                                          /**< (PMC_SLPWK_SR0) Peripheral 19 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID19_Msk               (0x1U << PMC_SLPWK_SR0_PID19_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 19 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID19(value)            (PMC_SLPWK_SR0_PID19_Msk & ((value) << PMC_SLPWK_SR0_PID19_Pos))
#define PMC_SLPWK_SR0_PID20_Pos               (20U)                                          /**< (PMC_SLPWK_SR0) Peripheral 20 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID20_Msk               (0x1U << PMC_SLPWK_SR0_PID20_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 20 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID20(value)            (PMC_SLPWK_SR0_PID20_Msk & ((value) << PMC_SLPWK_SR0_PID20_Pos))
#define PMC_SLPWK_SR0_PID21_Pos               (21U)                                          /**< (PMC_SLPWK_SR0) Peripheral 21 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID21_Msk               (0x1U << PMC_SLPWK_SR0_PID21_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 21 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID21(value)            (PMC_SLPWK_SR0_PID21_Msk & ((value) << PMC_SLPWK_SR0_PID21_Pos))
#define PMC_SLPWK_SR0_PID22_Pos               (22U)                                          /**< (PMC_SLPWK_SR0) Peripheral 22 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID22_Msk               (0x1U << PMC_SLPWK_SR0_PID22_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 22 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID22(value)            (PMC_SLPWK_SR0_PID22_Msk & ((value) << PMC_SLPWK_SR0_PID22_Pos))
#define PMC_SLPWK_SR0_PID23_Pos               (23U)                                          /**< (PMC_SLPWK_SR0) Peripheral 23 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID23_Msk               (0x1U << PMC_SLPWK_SR0_PID23_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 23 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID23(value)            (PMC_SLPWK_SR0_PID23_Msk & ((value) << PMC_SLPWK_SR0_PID23_Pos))
#define PMC_SLPWK_SR0_PID24_Pos               (24U)                                          /**< (PMC_SLPWK_SR0) Peripheral 24 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID24_Msk               (0x1U << PMC_SLPWK_SR0_PID24_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 24 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID24(value)            (PMC_SLPWK_SR0_PID24_Msk & ((value) << PMC_SLPWK_SR0_PID24_Pos))
#define PMC_SLPWK_SR0_PID25_Pos               (25U)                                          /**< (PMC_SLPWK_SR0) Peripheral 25 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID25_Msk               (0x1U << PMC_SLPWK_SR0_PID25_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 25 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID25(value)            (PMC_SLPWK_SR0_PID25_Msk & ((value) << PMC_SLPWK_SR0_PID25_Pos))
#define PMC_SLPWK_SR0_PID26_Pos               (26U)                                          /**< (PMC_SLPWK_SR0) Peripheral 26 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID26_Msk               (0x1U << PMC_SLPWK_SR0_PID26_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 26 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID26(value)            (PMC_SLPWK_SR0_PID26_Msk & ((value) << PMC_SLPWK_SR0_PID26_Pos))
#define PMC_SLPWK_SR0_PID27_Pos               (27U)                                          /**< (PMC_SLPWK_SR0) Peripheral 27 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID27_Msk               (0x1U << PMC_SLPWK_SR0_PID27_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 27 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID27(value)            (PMC_SLPWK_SR0_PID27_Msk & ((value) << PMC_SLPWK_SR0_PID27_Pos))
#define PMC_SLPWK_SR0_PID28_Pos               (28U)                                          /**< (PMC_SLPWK_SR0) Peripheral 28 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID28_Msk               (0x1U << PMC_SLPWK_SR0_PID28_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 28 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID28(value)            (PMC_SLPWK_SR0_PID28_Msk & ((value) << PMC_SLPWK_SR0_PID28_Pos))
#define PMC_SLPWK_SR0_PID29_Pos               (29U)                                          /**< (PMC_SLPWK_SR0) Peripheral 29 SleepWalking Status Position */
#define PMC_SLPWK_SR0_PID29_Msk               (0x1U << PMC_SLPWK_SR0_PID29_Pos)              /**< (PMC_SLPWK_SR0) Peripheral 29 SleepWalking Status Mask */
#define PMC_SLPWK_SR0_PID29(value)            (PMC_SLPWK_SR0_PID29_Msk & ((value) << PMC_SLPWK_SR0_PID29_Pos))
#define PMC_SLPWK_SR0_Msk                     (0x3FFFFF00UL)                                 /**< (PMC_SLPWK_SR0) Register Mask  */

/* -------- PMC_SLPWK_ASR0 : (PMC Offset: 0x120) (R/  32) SleepWalking Activity Status Register 0 -------- */
#define PMC_SLPWK_ASR0_PID8_Pos               (8U)                                           /**< (PMC_SLPWK_ASR0) Peripheral 8 Activity Status Position */
#define PMC_SLPWK_ASR0_PID8_Msk               (0x1U << PMC_SLPWK_ASR0_PID8_Pos)              /**< (PMC_SLPWK_ASR0) Peripheral 8 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID8(value)            (PMC_SLPWK_ASR0_PID8_Msk & ((value) << PMC_SLPWK_ASR0_PID8_Pos))
#define PMC_SLPWK_ASR0_PID9_Pos               (9U)                                           /**< (PMC_SLPWK_ASR0) Peripheral 9 Activity Status Position */
#define PMC_SLPWK_ASR0_PID9_Msk               (0x1U << PMC_SLPWK_ASR0_PID9_Pos)              /**< (PMC_SLPWK_ASR0) Peripheral 9 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID9(value)            (PMC_SLPWK_ASR0_PID9_Msk & ((value) << PMC_SLPWK_ASR0_PID9_Pos))
#define PMC_SLPWK_ASR0_PID10_Pos              (10U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 10 Activity Status Position */
#define PMC_SLPWK_ASR0_PID10_Msk              (0x1U << PMC_SLPWK_ASR0_PID10_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 10 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID10(value)           (PMC_SLPWK_ASR0_PID10_Msk & ((value) << PMC_SLPWK_ASR0_PID10_Pos))
#define PMC_SLPWK_ASR0_PID11_Pos              (11U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 11 Activity Status Position */
#define PMC_SLPWK_ASR0_PID11_Msk              (0x1U << PMC_SLPWK_ASR0_PID11_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 11 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID11(value)           (PMC_SLPWK_ASR0_PID11_Msk & ((value) << PMC_SLPWK_ASR0_PID11_Pos))
#define PMC_SLPWK_ASR0_PID12_Pos              (12U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 12 Activity Status Position */
#define PMC_SLPWK_ASR0_PID12_Msk              (0x1U << PMC_SLPWK_ASR0_PID12_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 12 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID12(value)           (PMC_SLPWK_ASR0_PID12_Msk & ((value) << PMC_SLPWK_ASR0_PID12_Pos))
#define PMC_SLPWK_ASR0_PID13_Pos              (13U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 13 Activity Status Position */
#define PMC_SLPWK_ASR0_PID13_Msk              (0x1U << PMC_SLPWK_ASR0_PID13_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 13 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID13(value)           (PMC_SLPWK_ASR0_PID13_Msk & ((value) << PMC_SLPWK_ASR0_PID13_Pos))
#define PMC_SLPWK_ASR0_PID14_Pos              (14U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 14 Activity Status Position */
#define PMC_SLPWK_ASR0_PID14_Msk              (0x1U << PMC_SLPWK_ASR0_PID14_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 14 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID14(value)           (PMC_SLPWK_ASR0_PID14_Msk & ((value) << PMC_SLPWK_ASR0_PID14_Pos))
#define PMC_SLPWK_ASR0_PID15_Pos              (15U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 15 Activity Status Position */
#define PMC_SLPWK_ASR0_PID15_Msk              (0x1U << PMC_SLPWK_ASR0_PID15_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 15 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID15(value)           (PMC_SLPWK_ASR0_PID15_Msk & ((value) << PMC_SLPWK_ASR0_PID15_Pos))
#define PMC_SLPWK_ASR0_PID16_Pos              (16U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 16 Activity Status Position */
#define PMC_SLPWK_ASR0_PID16_Msk              (0x1U << PMC_SLPWK_ASR0_PID16_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 16 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID16(value)           (PMC_SLPWK_ASR0_PID16_Msk & ((value) << PMC_SLPWK_ASR0_PID16_Pos))
#define PMC_SLPWK_ASR0_PID17_Pos              (17U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 17 Activity Status Position */
#define PMC_SLPWK_ASR0_PID17_Msk              (0x1U << PMC_SLPWK_ASR0_PID17_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 17 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID17(value)           (PMC_SLPWK_ASR0_PID17_Msk & ((value) << PMC_SLPWK_ASR0_PID17_Pos))
#define PMC_SLPWK_ASR0_PID18_Pos              (18U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 18 Activity Status Position */
#define PMC_SLPWK_ASR0_PID18_Msk              (0x1U << PMC_SLPWK_ASR0_PID18_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 18 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID18(value)           (PMC_SLPWK_ASR0_PID18_Msk & ((value) << PMC_SLPWK_ASR0_PID18_Pos))
#define PMC_SLPWK_ASR0_PID19_Pos              (19U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 19 Activity Status Position */
#define PMC_SLPWK_ASR0_PID19_Msk              (0x1U << PMC_SLPWK_ASR0_PID19_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 19 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID19(value)           (PMC_SLPWK_ASR0_PID19_Msk & ((value) << PMC_SLPWK_ASR0_PID19_Pos))
#define PMC_SLPWK_ASR0_PID20_Pos              (20U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 20 Activity Status Position */
#define PMC_SLPWK_ASR0_PID20_Msk              (0x1U << PMC_SLPWK_ASR0_PID20_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 20 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID20(value)           (PMC_SLPWK_ASR0_PID20_Msk & ((value) << PMC_SLPWK_ASR0_PID20_Pos))
#define PMC_SLPWK_ASR0_PID21_Pos              (21U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 21 Activity Status Position */
#define PMC_SLPWK_ASR0_PID21_Msk              (0x1U << PMC_SLPWK_ASR0_PID21_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 21 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID21(value)           (PMC_SLPWK_ASR0_PID21_Msk & ((value) << PMC_SLPWK_ASR0_PID21_Pos))
#define PMC_SLPWK_ASR0_PID22_Pos              (22U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 22 Activity Status Position */
#define PMC_SLPWK_ASR0_PID22_Msk              (0x1U << PMC_SLPWK_ASR0_PID22_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 22 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID22(value)           (PMC_SLPWK_ASR0_PID22_Msk & ((value) << PMC_SLPWK_ASR0_PID22_Pos))
#define PMC_SLPWK_ASR0_PID23_Pos              (23U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 23 Activity Status Position */
#define PMC_SLPWK_ASR0_PID23_Msk              (0x1U << PMC_SLPWK_ASR0_PID23_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 23 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID23(value)           (PMC_SLPWK_ASR0_PID23_Msk & ((value) << PMC_SLPWK_ASR0_PID23_Pos))
#define PMC_SLPWK_ASR0_PID24_Pos              (24U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 24 Activity Status Position */
#define PMC_SLPWK_ASR0_PID24_Msk              (0x1U << PMC_SLPWK_ASR0_PID24_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 24 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID24(value)           (PMC_SLPWK_ASR0_PID24_Msk & ((value) << PMC_SLPWK_ASR0_PID24_Pos))
#define PMC_SLPWK_ASR0_PID25_Pos              (25U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 25 Activity Status Position */
#define PMC_SLPWK_ASR0_PID25_Msk              (0x1U << PMC_SLPWK_ASR0_PID25_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 25 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID25(value)           (PMC_SLPWK_ASR0_PID25_Msk & ((value) << PMC_SLPWK_ASR0_PID25_Pos))
#define PMC_SLPWK_ASR0_PID26_Pos              (26U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 26 Activity Status Position */
#define PMC_SLPWK_ASR0_PID26_Msk              (0x1U << PMC_SLPWK_ASR0_PID26_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 26 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID26(value)           (PMC_SLPWK_ASR0_PID26_Msk & ((value) << PMC_SLPWK_ASR0_PID26_Pos))
#define PMC_SLPWK_ASR0_PID27_Pos              (27U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 27 Activity Status Position */
#define PMC_SLPWK_ASR0_PID27_Msk              (0x1U << PMC_SLPWK_ASR0_PID27_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 27 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID27(value)           (PMC_SLPWK_ASR0_PID27_Msk & ((value) << PMC_SLPWK_ASR0_PID27_Pos))
#define PMC_SLPWK_ASR0_PID28_Pos              (28U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 28 Activity Status Position */
#define PMC_SLPWK_ASR0_PID28_Msk              (0x1U << PMC_SLPWK_ASR0_PID28_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 28 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID28(value)           (PMC_SLPWK_ASR0_PID28_Msk & ((value) << PMC_SLPWK_ASR0_PID28_Pos))
#define PMC_SLPWK_ASR0_PID29_Pos              (29U)                                          /**< (PMC_SLPWK_ASR0) Peripheral 29 Activity Status Position */
#define PMC_SLPWK_ASR0_PID29_Msk              (0x1U << PMC_SLPWK_ASR0_PID29_Pos)             /**< (PMC_SLPWK_ASR0) Peripheral 29 Activity Status Mask */
#define PMC_SLPWK_ASR0_PID29(value)           (PMC_SLPWK_ASR0_PID29_Msk & ((value) << PMC_SLPWK_ASR0_PID29_Pos))
#define PMC_SLPWK_ASR0_Msk                    (0x3FFFFF00UL)                                 /**< (PMC_SLPWK_ASR0) Register Mask  */

/* -------- PMC_PMMR : (PMC Offset: 0x130) (R/W 32) PLL Maximum Multiplier Value Register -------- */
#define PMC_PMMR_PLLA_MMAX_Pos                (0U)                                           /**< (PMC_PMMR) PLLA Maximum Allowed Multiplier Value Position */
#define PMC_PMMR_PLLA_MMAX_Msk                (0x7FFU << PMC_PMMR_PLLA_MMAX_Pos)             /**< (PMC_PMMR) PLLA Maximum Allowed Multiplier Value Mask */
#define PMC_PMMR_PLLA_MMAX(value)             (PMC_PMMR_PLLA_MMAX_Msk & ((value) << PMC_PMMR_PLLA_MMAX_Pos))
#define PMC_PMMR_PLLB_MMAX_Pos                (16U)                                          /**< (PMC_PMMR) PLLB Maximum Allowed Multiplier Value Position */
#define PMC_PMMR_PLLB_MMAX_Msk                (0x7FFU << PMC_PMMR_PLLB_MMAX_Pos)             /**< (PMC_PMMR) PLLB Maximum Allowed Multiplier Value Mask */
#define PMC_PMMR_PLLB_MMAX(value)             (PMC_PMMR_PLLB_MMAX_Msk & ((value) << PMC_PMMR_PLLB_MMAX_Pos))
#define PMC_PMMR_Msk                          (0x07FF07FFUL)                                 /**< (PMC_PMMR) Register Mask  */

/** \brief PMC register offsets definitions */
#define PMC_SCER_OFFSET                (0x00)         /**< (PMC_SCER) System Clock Enable Register Offset */
#define PMC_SCDR_OFFSET                (0x04)         /**< (PMC_SCDR) System Clock Disable Register Offset */
#define PMC_SCSR_OFFSET                (0x08)         /**< (PMC_SCSR) System Clock Status Register Offset */
#define PMC_PCER0_OFFSET               (0x10)         /**< (PMC_PCER0) Peripheral Clock Enable Register 0 Offset */
#define PMC_PCDR0_OFFSET               (0x14)         /**< (PMC_PCDR0) Peripheral Clock Disable Register 0 Offset */
#define PMC_PCSR0_OFFSET               (0x18)         /**< (PMC_PCSR0) Peripheral Clock Status Register 0 Offset */
#define CKGR_MOR_OFFSET                (0x20)         /**< (CKGR_MOR) Main Oscillator Register Offset */
#define CKGR_MCFR_OFFSET               (0x24)         /**< (CKGR_MCFR) Main Clock Frequency Register Offset */
#define CKGR_PLLAR_OFFSET              (0x28)         /**< (CKGR_PLLAR) PLLA Register Offset */
#define CKGR_PLLBR_OFFSET              (0x2C)         /**< (CKGR_PLLBR) PLLB Register Offset */
#define PMC_MCKR_OFFSET                (0x30)         /**< (PMC_MCKR) Master Clock Register Offset */
#define PMC_USB_OFFSET                 (0x38)         /**< (PMC_USB) USB Clock Register Offset */
#define PMC_PCK_OFFSET                 (0x40)         /**< (PMC_PCK) Programmable Clock 0 Register 0 Offset */
#define PMC_IER_OFFSET                 (0x60)         /**< (PMC_IER) Interrupt Enable Register Offset */
#define PMC_IDR_OFFSET                 (0x64)         /**< (PMC_IDR) Interrupt Disable Register Offset */
#define PMC_SR_OFFSET                  (0x68)         /**< (PMC_SR) Status Register Offset */
#define PMC_IMR_OFFSET                 (0x6C)         /**< (PMC_IMR) Interrupt Mask Register Offset */
#define PMC_FSMR_OFFSET                (0x70)         /**< (PMC_FSMR) Fast Startup Mode Register Offset */
#define PMC_FSPR_OFFSET                (0x74)         /**< (PMC_FSPR) Fast Startup Polarity Register Offset */
#define PMC_FOCR_OFFSET                (0x78)         /**< (PMC_FOCR) Fault Output Clear Register Offset */
#define PMC_WPMR_OFFSET                (0xE4)         /**< (PMC_WPMR) Write Protection Mode Register Offset */
#define PMC_WPSR_OFFSET                (0xE8)         /**< (PMC_WPSR) Write Protection Status Register Offset */
#define PMC_PCER1_OFFSET               (0x100)        /**< (PMC_PCER1) Peripheral Clock Enable Register 1 Offset */
#define PMC_PCDR1_OFFSET               (0x104)        /**< (PMC_PCDR1) Peripheral Clock Disable Register 1 Offset */
#define PMC_PCSR1_OFFSET               (0x108)        /**< (PMC_PCSR1) Peripheral Clock Status Register 1 Offset */
#define PMC_PCR_OFFSET                 (0x10C)        /**< (PMC_PCR) Peripheral Control Register Offset */
#define PMC_OCR_OFFSET                 (0x110)        /**< (PMC_OCR) Oscillator Calibration Register Offset */
#define PMC_SLPWK_ER0_OFFSET           (0x114)        /**< (PMC_SLPWK_ER0) SleepWalking Enable Register 0 Offset */
#define PMC_SLPWK_DR0_OFFSET           (0x118)        /**< (PMC_SLPWK_DR0) SleepWalking Disable Register 0 Offset */
#define PMC_SLPWK_SR0_OFFSET           (0x11C)        /**< (PMC_SLPWK_SR0) SleepWalking Status Register 0 Offset */
#define PMC_SLPWK_ASR0_OFFSET          (0x120)        /**< (PMC_SLPWK_ASR0) SleepWalking Activity Status Register 0 Offset */
#define PMC_PMMR_OFFSET                (0x130)        /**< (PMC_PMMR) PLL Maximum Multiplier Value Register Offset */

/** \brief PMC register API structure */
typedef struct
{
  __O   uint32_t                       PMC_SCER;        /**< Offset: 0x00 ( /W  32) System Clock Enable Register */
  __O   uint32_t                       PMC_SCDR;        /**< Offset: 0x04 ( /W  32) System Clock Disable Register */
  __I   uint32_t                       PMC_SCSR;        /**< Offset: 0x08 (R/   32) System Clock Status Register */
  __I   uint8_t                        Reserved1[0x04];
  __O   uint32_t                       PMC_PCER0;       /**< Offset: 0x10 ( /W  32) Peripheral Clock Enable Register 0 */
  __O   uint32_t                       PMC_PCDR0;       /**< Offset: 0x14 ( /W  32) Peripheral Clock Disable Register 0 */
  __I   uint32_t                       PMC_PCSR0;       /**< Offset: 0x18 (R/   32) Peripheral Clock Status Register 0 */
  __I   uint8_t                        Reserved2[0x04];
  __IO  uint32_t                       CKGR_MOR;        /**< Offset: 0x20 (R/W  32) Main Oscillator Register */
  __IO  uint32_t                       CKGR_MCFR;       /**< Offset: 0x24 (R/W  32) Main Clock Frequency Register */
  __IO  uint32_t                       CKGR_PLLAR;      /**< Offset: 0x28 (R/W  32) PLLA Register */
  __IO  uint32_t                       CKGR_PLLBR;      /**< Offset: 0x2c (R/W  32) PLLB Register */
  __IO  uint32_t                       PMC_MCKR;        /**< Offset: 0x30 (R/W  32) Master Clock Register */
  __I   uint8_t                        Reserved3[0x04];
  __IO  uint32_t                       PMC_USB;         /**< Offset: 0x38 (R/W  32) USB Clock Register */
  __I   uint8_t                        Reserved4[0x04];
  __IO  uint32_t                       PMC_PCK[8];      /**< Offset: 0x40 (R/W  32) Programmable Clock 0 Register 0 */
  __O   uint32_t                       PMC_IER;         /**< Offset: 0x60 ( /W  32) Interrupt Enable Register */
  __O   uint32_t                       PMC_IDR;         /**< Offset: 0x64 ( /W  32) Interrupt Disable Register */
  __I   uint32_t                       PMC_SR;          /**< Offset: 0x68 (R/   32) Status Register */
  __I   uint32_t                       PMC_IMR;         /**< Offset: 0x6c (R/   32) Interrupt Mask Register */
  __IO  uint32_t                       PMC_FSMR;        /**< Offset: 0x70 (R/W  32) Fast Startup Mode Register */
  __IO  uint32_t                       PMC_FSPR;        /**< Offset: 0x74 (R/W  32) Fast Startup Polarity Register */
  __O   uint32_t                       PMC_FOCR;        /**< Offset: 0x78 ( /W  32) Fault Output Clear Register */
  __I   uint8_t                        Reserved5[0x68];
  __IO  uint32_t                       PMC_WPMR;        /**< Offset: 0xe4 (R/W  32) Write Protection Mode Register */
  __I   uint32_t                       PMC_WPSR;        /**< Offset: 0xe8 (R/   32) Write Protection Status Register */
  __I   uint8_t                        Reserved6[0x14];
  __O   uint32_t                       PMC_PCER1;       /**< Offset: 0x100 ( /W  32) Peripheral Clock Enable Register 1 */
  __O   uint32_t                       PMC_PCDR1;       /**< Offset: 0x104 ( /W  32) Peripheral Clock Disable Register 1 */
  __I   uint32_t                       PMC_PCSR1;       /**< Offset: 0x108 (R/   32) Peripheral Clock Status Register 1 */
  __IO  uint32_t                       PMC_PCR;         /**< Offset: 0x10c (R/W  32) Peripheral Control Register */
  __IO  uint32_t                       PMC_OCR;         /**< Offset: 0x110 (R/W  32) Oscillator Calibration Register */
  __O   uint32_t                       PMC_SLPWK_ER0;   /**< Offset: 0x114 ( /W  32) SleepWalking Enable Register 0 */
  __O   uint32_t                       PMC_SLPWK_DR0;   /**< Offset: 0x118 ( /W  32) SleepWalking Disable Register 0 */
  __I   uint32_t                       PMC_SLPWK_SR0;   /**< Offset: 0x11c (R/   32) SleepWalking Status Register 0 */
  __I   uint32_t                       PMC_SLPWK_ASR0;  /**< Offset: 0x120 (R/   32) SleepWalking Activity Status Register 0 */
  __I   uint8_t                        Reserved7[0x0C];
  __IO  uint32_t                       PMC_PMMR;        /**< Offset: 0x130 (R/W  32) PLL Maximum Multiplier Value Register */
} pmc_registers_t;
/** @}  end of Power Management Controller */

#endif /* SAMG_SAMG55_PMC_MODULE_H */

