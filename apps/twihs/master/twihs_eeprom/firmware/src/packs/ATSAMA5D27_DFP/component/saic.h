/**
 * \brief Header file for SAMA5D2/SAMA5D2 SAIC
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

/* file generated from device description version 2018-10-15T17:19:05Z */
#ifndef SAMA5D2_SAMA5D2_SAIC_MODULE_H
#define SAMA5D2_SAMA5D2_SAIC_MODULE_H

/** \addtogroup SAMA5D2_SAMA5D2 Secure Advanced Interrupt Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMA5D2_SAIC                                 */
/* ========================================================================== */

/* -------- AIC_SSR : (SAIC Offset: 0x00) (R/W 32) Source Select Register -------- */
#define AIC_SSR_INTSEL_Pos                    (0U)                                           /**< (AIC_SSR) Interrupt Line Selection Position */
#define AIC_SSR_INTSEL_Msk                    (0x7FU << AIC_SSR_INTSEL_Pos)                  /**< (AIC_SSR) Interrupt Line Selection Mask */
#define AIC_SSR_INTSEL(value)                 (AIC_SSR_INTSEL_Msk & ((value) << AIC_SSR_INTSEL_Pos))
#define AIC_SSR_Msk                           (0x0000007FUL)                                 /**< (AIC_SSR) Register Mask  */

/* -------- AIC_SMR : (SAIC Offset: 0x04) (R/W 32) Source Mode Register -------- */
#define AIC_SMR_PRIOR_Pos                     (0U)                                           /**< (AIC_SMR) Priority Level Position */
#define AIC_SMR_PRIOR_Msk                     (0x7U << AIC_SMR_PRIOR_Pos)                    /**< (AIC_SMR) Priority Level Mask */
#define AIC_SMR_PRIOR(value)                  (AIC_SMR_PRIOR_Msk & ((value) << AIC_SMR_PRIOR_Pos))
#define AIC_SMR_SRCTYPE_Pos                   (5U)                                           /**< (AIC_SMR) Interrupt Source Type Position */
#define AIC_SMR_SRCTYPE_Msk                   (0x3U << AIC_SMR_SRCTYPE_Pos)                  /**< (AIC_SMR) Interrupt Source Type Mask */
#define AIC_SMR_SRCTYPE(value)                (AIC_SMR_SRCTYPE_Msk & ((value) << AIC_SMR_SRCTYPE_Pos))
#define   AIC_SMR_SRCTYPE_INT_LEVEL_SENSITIVE_Val (0U)                                           /**< (AIC_SMR) High-level sensitive for internal sourceLow-level sensitive for external source  */
#define   AIC_SMR_SRCTYPE_EXT_NEGATIVE_EDGE_Val (1U)                                           /**< (AIC_SMR) Negative-edge triggered for external source  */
#define   AIC_SMR_SRCTYPE_EXT_HIGH_LEVEL_Val  (2U)                                           /**< (AIC_SMR) High-level sensitive for internal sourceHigh-level sensitive for external source  */
#define   AIC_SMR_SRCTYPE_EXT_POSITIVE_EDGE_Val (3U)                                           /**< (AIC_SMR) Positive-edge triggered for external source  */
#define AIC_SMR_SRCTYPE_INT_LEVEL_SENSITIVE   (AIC_SMR_SRCTYPE_INT_LEVEL_SENSITIVE_Val << AIC_SMR_SRCTYPE_Pos) /**< (AIC_SMR) High-level sensitive for internal sourceLow-level sensitive for external source Position  */
#define AIC_SMR_SRCTYPE_EXT_NEGATIVE_EDGE     (AIC_SMR_SRCTYPE_EXT_NEGATIVE_EDGE_Val << AIC_SMR_SRCTYPE_Pos) /**< (AIC_SMR) Negative-edge triggered for external source Position  */
#define AIC_SMR_SRCTYPE_EXT_HIGH_LEVEL        (AIC_SMR_SRCTYPE_EXT_HIGH_LEVEL_Val << AIC_SMR_SRCTYPE_Pos) /**< (AIC_SMR) High-level sensitive for internal sourceHigh-level sensitive for external source Position  */
#define AIC_SMR_SRCTYPE_EXT_POSITIVE_EDGE     (AIC_SMR_SRCTYPE_EXT_POSITIVE_EDGE_Val << AIC_SMR_SRCTYPE_Pos) /**< (AIC_SMR) Positive-edge triggered for external source Position  */
#define AIC_SMR_Msk                           (0x00000067UL)                                 /**< (AIC_SMR) Register Mask  */

/* -------- AIC_SVR : (SAIC Offset: 0x08) (R/W 32) Source Vector Register -------- */
#define AIC_SVR_VECTOR_Pos                    (0U)                                           /**< (AIC_SVR) Source Vector Position */
#define AIC_SVR_VECTOR_Msk                    (0xFFFFFFFFU << AIC_SVR_VECTOR_Pos)            /**< (AIC_SVR) Source Vector Mask */
#define AIC_SVR_VECTOR(value)                 (AIC_SVR_VECTOR_Msk & ((value) << AIC_SVR_VECTOR_Pos))
#define AIC_SVR_Msk                           (0xFFFFFFFFUL)                                 /**< (AIC_SVR) Register Mask  */

/* -------- AIC_IVR : (SAIC Offset: 0x10) (R/  32) Interrupt Vector Register -------- */
#define AIC_IVR_IRQV_Pos                      (0U)                                           /**< (AIC_IVR) Interrupt Vector Register Position */
#define AIC_IVR_IRQV_Msk                      (0xFFFFFFFFU << AIC_IVR_IRQV_Pos)              /**< (AIC_IVR) Interrupt Vector Register Mask */
#define AIC_IVR_IRQV(value)                   (AIC_IVR_IRQV_Msk & ((value) << AIC_IVR_IRQV_Pos))
#define AIC_IVR_Msk                           (0xFFFFFFFFUL)                                 /**< (AIC_IVR) Register Mask  */

/* -------- AIC_FVR : (SAIC Offset: 0x14) (R/  32) FIQ Vector Register -------- */
#define AIC_FVR_FIQV_Pos                      (0U)                                           /**< (AIC_FVR) FIQ Vector Register Position */
#define AIC_FVR_FIQV_Msk                      (0xFFFFFFFFU << AIC_FVR_FIQV_Pos)              /**< (AIC_FVR) FIQ Vector Register Mask */
#define AIC_FVR_FIQV(value)                   (AIC_FVR_FIQV_Msk & ((value) << AIC_FVR_FIQV_Pos))
#define AIC_FVR_Msk                           (0xFFFFFFFFUL)                                 /**< (AIC_FVR) Register Mask  */

/* -------- AIC_ISR : (SAIC Offset: 0x18) (R/  32) Interrupt Status Register -------- */
#define AIC_ISR_IRQID_Pos                     (0U)                                           /**< (AIC_ISR) Current Interrupt Identifier Position */
#define AIC_ISR_IRQID_Msk                     (0x7FU << AIC_ISR_IRQID_Pos)                   /**< (AIC_ISR) Current Interrupt Identifier Mask */
#define AIC_ISR_IRQID(value)                  (AIC_ISR_IRQID_Msk & ((value) << AIC_ISR_IRQID_Pos))
#define AIC_ISR_Msk                           (0x0000007FUL)                                 /**< (AIC_ISR) Register Mask  */

/* -------- AIC_IPR0 : (SAIC Offset: 0x20) (R/  32) Interrupt Pending Register 0 -------- */
#define AIC_IPR0_FIQ_Pos                      (0U)                                           /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_FIQ_Msk                      (0x1U << AIC_IPR0_FIQ_Pos)                     /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_FIQ(value)                   (AIC_IPR0_FIQ_Msk & ((value) << AIC_IPR0_FIQ_Pos))
#define AIC_IPR0_PID1_Pos                     (1U)                                           /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID1_Msk                     (0x1U << AIC_IPR0_PID1_Pos)                    /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID1(value)                  (AIC_IPR0_PID1_Msk & ((value) << AIC_IPR0_PID1_Pos))
#define AIC_IPR0_PID2_Pos                     (2U)                                           /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID2_Msk                     (0x1U << AIC_IPR0_PID2_Pos)                    /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID2(value)                  (AIC_IPR0_PID2_Msk & ((value) << AIC_IPR0_PID2_Pos))
#define AIC_IPR0_PID3_Pos                     (3U)                                           /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID3_Msk                     (0x1U << AIC_IPR0_PID3_Pos)                    /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID3(value)                  (AIC_IPR0_PID3_Msk & ((value) << AIC_IPR0_PID3_Pos))
#define AIC_IPR0_PID4_Pos                     (4U)                                           /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID4_Msk                     (0x1U << AIC_IPR0_PID4_Pos)                    /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID4(value)                  (AIC_IPR0_PID4_Msk & ((value) << AIC_IPR0_PID4_Pos))
#define AIC_IPR0_PID5_Pos                     (5U)                                           /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID5_Msk                     (0x1U << AIC_IPR0_PID5_Pos)                    /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID5(value)                  (AIC_IPR0_PID5_Msk & ((value) << AIC_IPR0_PID5_Pos))
#define AIC_IPR0_PID6_Pos                     (6U)                                           /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID6_Msk                     (0x1U << AIC_IPR0_PID6_Pos)                    /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID6(value)                  (AIC_IPR0_PID6_Msk & ((value) << AIC_IPR0_PID6_Pos))
#define AIC_IPR0_PID7_Pos                     (7U)                                           /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID7_Msk                     (0x1U << AIC_IPR0_PID7_Pos)                    /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID7(value)                  (AIC_IPR0_PID7_Msk & ((value) << AIC_IPR0_PID7_Pos))
#define AIC_IPR0_PID8_Pos                     (8U)                                           /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID8_Msk                     (0x1U << AIC_IPR0_PID8_Pos)                    /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID8(value)                  (AIC_IPR0_PID8_Msk & ((value) << AIC_IPR0_PID8_Pos))
#define AIC_IPR0_PID9_Pos                     (9U)                                           /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID9_Msk                     (0x1U << AIC_IPR0_PID9_Pos)                    /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID9(value)                  (AIC_IPR0_PID9_Msk & ((value) << AIC_IPR0_PID9_Pos))
#define AIC_IPR0_PID10_Pos                    (10U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID10_Msk                    (0x1U << AIC_IPR0_PID10_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID10(value)                 (AIC_IPR0_PID10_Msk & ((value) << AIC_IPR0_PID10_Pos))
#define AIC_IPR0_PID11_Pos                    (11U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID11_Msk                    (0x1U << AIC_IPR0_PID11_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID11(value)                 (AIC_IPR0_PID11_Msk & ((value) << AIC_IPR0_PID11_Pos))
#define AIC_IPR0_PID12_Pos                    (12U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID12_Msk                    (0x1U << AIC_IPR0_PID12_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID12(value)                 (AIC_IPR0_PID12_Msk & ((value) << AIC_IPR0_PID12_Pos))
#define AIC_IPR0_PID13_Pos                    (13U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID13_Msk                    (0x1U << AIC_IPR0_PID13_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID13(value)                 (AIC_IPR0_PID13_Msk & ((value) << AIC_IPR0_PID13_Pos))
#define AIC_IPR0_PID14_Pos                    (14U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID14_Msk                    (0x1U << AIC_IPR0_PID14_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID14(value)                 (AIC_IPR0_PID14_Msk & ((value) << AIC_IPR0_PID14_Pos))
#define AIC_IPR0_PID15_Pos                    (15U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID15_Msk                    (0x1U << AIC_IPR0_PID15_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID15(value)                 (AIC_IPR0_PID15_Msk & ((value) << AIC_IPR0_PID15_Pos))
#define AIC_IPR0_PID16_Pos                    (16U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID16_Msk                    (0x1U << AIC_IPR0_PID16_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID16(value)                 (AIC_IPR0_PID16_Msk & ((value) << AIC_IPR0_PID16_Pos))
#define AIC_IPR0_PID17_Pos                    (17U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID17_Msk                    (0x1U << AIC_IPR0_PID17_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID17(value)                 (AIC_IPR0_PID17_Msk & ((value) << AIC_IPR0_PID17_Pos))
#define AIC_IPR0_PID18_Pos                    (18U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID18_Msk                    (0x1U << AIC_IPR0_PID18_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID18(value)                 (AIC_IPR0_PID18_Msk & ((value) << AIC_IPR0_PID18_Pos))
#define AIC_IPR0_PID19_Pos                    (19U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID19_Msk                    (0x1U << AIC_IPR0_PID19_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID19(value)                 (AIC_IPR0_PID19_Msk & ((value) << AIC_IPR0_PID19_Pos))
#define AIC_IPR0_PID20_Pos                    (20U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID20_Msk                    (0x1U << AIC_IPR0_PID20_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID20(value)                 (AIC_IPR0_PID20_Msk & ((value) << AIC_IPR0_PID20_Pos))
#define AIC_IPR0_PID21_Pos                    (21U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID21_Msk                    (0x1U << AIC_IPR0_PID21_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID21(value)                 (AIC_IPR0_PID21_Msk & ((value) << AIC_IPR0_PID21_Pos))
#define AIC_IPR0_PID22_Pos                    (22U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID22_Msk                    (0x1U << AIC_IPR0_PID22_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID22(value)                 (AIC_IPR0_PID22_Msk & ((value) << AIC_IPR0_PID22_Pos))
#define AIC_IPR0_PID23_Pos                    (23U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID23_Msk                    (0x1U << AIC_IPR0_PID23_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID23(value)                 (AIC_IPR0_PID23_Msk & ((value) << AIC_IPR0_PID23_Pos))
#define AIC_IPR0_PID24_Pos                    (24U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID24_Msk                    (0x1U << AIC_IPR0_PID24_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID24(value)                 (AIC_IPR0_PID24_Msk & ((value) << AIC_IPR0_PID24_Pos))
#define AIC_IPR0_PID25_Pos                    (25U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID25_Msk                    (0x1U << AIC_IPR0_PID25_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID25(value)                 (AIC_IPR0_PID25_Msk & ((value) << AIC_IPR0_PID25_Pos))
#define AIC_IPR0_PID26_Pos                    (26U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID26_Msk                    (0x1U << AIC_IPR0_PID26_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID26(value)                 (AIC_IPR0_PID26_Msk & ((value) << AIC_IPR0_PID26_Pos))
#define AIC_IPR0_PID27_Pos                    (27U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID27_Msk                    (0x1U << AIC_IPR0_PID27_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID27(value)                 (AIC_IPR0_PID27_Msk & ((value) << AIC_IPR0_PID27_Pos))
#define AIC_IPR0_PID28_Pos                    (28U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID28_Msk                    (0x1U << AIC_IPR0_PID28_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID28(value)                 (AIC_IPR0_PID28_Msk & ((value) << AIC_IPR0_PID28_Pos))
#define AIC_IPR0_PID29_Pos                    (29U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID29_Msk                    (0x1U << AIC_IPR0_PID29_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID29(value)                 (AIC_IPR0_PID29_Msk & ((value) << AIC_IPR0_PID29_Pos))
#define AIC_IPR0_PID30_Pos                    (30U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID30_Msk                    (0x1U << AIC_IPR0_PID30_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID30(value)                 (AIC_IPR0_PID30_Msk & ((value) << AIC_IPR0_PID30_Pos))
#define AIC_IPR0_PID31_Pos                    (31U)                                          /**< (AIC_IPR0) Interrupt Pending Position */
#define AIC_IPR0_PID31_Msk                    (0x1U << AIC_IPR0_PID31_Pos)                   /**< (AIC_IPR0) Interrupt Pending Mask */
#define AIC_IPR0_PID31(value)                 (AIC_IPR0_PID31_Msk & ((value) << AIC_IPR0_PID31_Pos))
#define AIC_IPR0_Msk                          (0xFFFFFFFFUL)                                 /**< (AIC_IPR0) Register Mask  */

/* -------- AIC_IPR1 : (SAIC Offset: 0x24) (R/  32) Interrupt Pending Register 1 -------- */
#define AIC_IPR1_PID32_Pos                    (0U)                                           /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID32_Msk                    (0x1U << AIC_IPR1_PID32_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID32(value)                 (AIC_IPR1_PID32_Msk & ((value) << AIC_IPR1_PID32_Pos))
#define AIC_IPR1_PID33_Pos                    (1U)                                           /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID33_Msk                    (0x1U << AIC_IPR1_PID33_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID33(value)                 (AIC_IPR1_PID33_Msk & ((value) << AIC_IPR1_PID33_Pos))
#define AIC_IPR1_PID34_Pos                    (2U)                                           /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID34_Msk                    (0x1U << AIC_IPR1_PID34_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID34(value)                 (AIC_IPR1_PID34_Msk & ((value) << AIC_IPR1_PID34_Pos))
#define AIC_IPR1_PID35_Pos                    (3U)                                           /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID35_Msk                    (0x1U << AIC_IPR1_PID35_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID35(value)                 (AIC_IPR1_PID35_Msk & ((value) << AIC_IPR1_PID35_Pos))
#define AIC_IPR1_PID36_Pos                    (4U)                                           /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID36_Msk                    (0x1U << AIC_IPR1_PID36_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID36(value)                 (AIC_IPR1_PID36_Msk & ((value) << AIC_IPR1_PID36_Pos))
#define AIC_IPR1_PID37_Pos                    (5U)                                           /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID37_Msk                    (0x1U << AIC_IPR1_PID37_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID37(value)                 (AIC_IPR1_PID37_Msk & ((value) << AIC_IPR1_PID37_Pos))
#define AIC_IPR1_PID38_Pos                    (6U)                                           /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID38_Msk                    (0x1U << AIC_IPR1_PID38_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID38(value)                 (AIC_IPR1_PID38_Msk & ((value) << AIC_IPR1_PID38_Pos))
#define AIC_IPR1_PID39_Pos                    (7U)                                           /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID39_Msk                    (0x1U << AIC_IPR1_PID39_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID39(value)                 (AIC_IPR1_PID39_Msk & ((value) << AIC_IPR1_PID39_Pos))
#define AIC_IPR1_PID40_Pos                    (8U)                                           /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID40_Msk                    (0x1U << AIC_IPR1_PID40_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID40(value)                 (AIC_IPR1_PID40_Msk & ((value) << AIC_IPR1_PID40_Pos))
#define AIC_IPR1_PID41_Pos                    (9U)                                           /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID41_Msk                    (0x1U << AIC_IPR1_PID41_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID41(value)                 (AIC_IPR1_PID41_Msk & ((value) << AIC_IPR1_PID41_Pos))
#define AIC_IPR1_PID42_Pos                    (10U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID42_Msk                    (0x1U << AIC_IPR1_PID42_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID42(value)                 (AIC_IPR1_PID42_Msk & ((value) << AIC_IPR1_PID42_Pos))
#define AIC_IPR1_PID43_Pos                    (11U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID43_Msk                    (0x1U << AIC_IPR1_PID43_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID43(value)                 (AIC_IPR1_PID43_Msk & ((value) << AIC_IPR1_PID43_Pos))
#define AIC_IPR1_PID44_Pos                    (12U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID44_Msk                    (0x1U << AIC_IPR1_PID44_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID44(value)                 (AIC_IPR1_PID44_Msk & ((value) << AIC_IPR1_PID44_Pos))
#define AIC_IPR1_PID45_Pos                    (13U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID45_Msk                    (0x1U << AIC_IPR1_PID45_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID45(value)                 (AIC_IPR1_PID45_Msk & ((value) << AIC_IPR1_PID45_Pos))
#define AIC_IPR1_PID46_Pos                    (14U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID46_Msk                    (0x1U << AIC_IPR1_PID46_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID46(value)                 (AIC_IPR1_PID46_Msk & ((value) << AIC_IPR1_PID46_Pos))
#define AIC_IPR1_PID47_Pos                    (15U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID47_Msk                    (0x1U << AIC_IPR1_PID47_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID47(value)                 (AIC_IPR1_PID47_Msk & ((value) << AIC_IPR1_PID47_Pos))
#define AIC_IPR1_PID48_Pos                    (16U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID48_Msk                    (0x1U << AIC_IPR1_PID48_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID48(value)                 (AIC_IPR1_PID48_Msk & ((value) << AIC_IPR1_PID48_Pos))
#define AIC_IPR1_PID49_Pos                    (17U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID49_Msk                    (0x1U << AIC_IPR1_PID49_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID49(value)                 (AIC_IPR1_PID49_Msk & ((value) << AIC_IPR1_PID49_Pos))
#define AIC_IPR1_PID50_Pos                    (18U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID50_Msk                    (0x1U << AIC_IPR1_PID50_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID50(value)                 (AIC_IPR1_PID50_Msk & ((value) << AIC_IPR1_PID50_Pos))
#define AIC_IPR1_PID51_Pos                    (19U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID51_Msk                    (0x1U << AIC_IPR1_PID51_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID51(value)                 (AIC_IPR1_PID51_Msk & ((value) << AIC_IPR1_PID51_Pos))
#define AIC_IPR1_PID52_Pos                    (20U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID52_Msk                    (0x1U << AIC_IPR1_PID52_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID52(value)                 (AIC_IPR1_PID52_Msk & ((value) << AIC_IPR1_PID52_Pos))
#define AIC_IPR1_PID53_Pos                    (21U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID53_Msk                    (0x1U << AIC_IPR1_PID53_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID53(value)                 (AIC_IPR1_PID53_Msk & ((value) << AIC_IPR1_PID53_Pos))
#define AIC_IPR1_PID54_Pos                    (22U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID54_Msk                    (0x1U << AIC_IPR1_PID54_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID54(value)                 (AIC_IPR1_PID54_Msk & ((value) << AIC_IPR1_PID54_Pos))
#define AIC_IPR1_PID55_Pos                    (23U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID55_Msk                    (0x1U << AIC_IPR1_PID55_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID55(value)                 (AIC_IPR1_PID55_Msk & ((value) << AIC_IPR1_PID55_Pos))
#define AIC_IPR1_PID56_Pos                    (24U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID56_Msk                    (0x1U << AIC_IPR1_PID56_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID56(value)                 (AIC_IPR1_PID56_Msk & ((value) << AIC_IPR1_PID56_Pos))
#define AIC_IPR1_PID57_Pos                    (25U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID57_Msk                    (0x1U << AIC_IPR1_PID57_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID57(value)                 (AIC_IPR1_PID57_Msk & ((value) << AIC_IPR1_PID57_Pos))
#define AIC_IPR1_PID58_Pos                    (26U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID58_Msk                    (0x1U << AIC_IPR1_PID58_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID58(value)                 (AIC_IPR1_PID58_Msk & ((value) << AIC_IPR1_PID58_Pos))
#define AIC_IPR1_PID59_Pos                    (27U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID59_Msk                    (0x1U << AIC_IPR1_PID59_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID59(value)                 (AIC_IPR1_PID59_Msk & ((value) << AIC_IPR1_PID59_Pos))
#define AIC_IPR1_PID60_Pos                    (28U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID60_Msk                    (0x1U << AIC_IPR1_PID60_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID60(value)                 (AIC_IPR1_PID60_Msk & ((value) << AIC_IPR1_PID60_Pos))
#define AIC_IPR1_PID61_Pos                    (29U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID61_Msk                    (0x1U << AIC_IPR1_PID61_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID61(value)                 (AIC_IPR1_PID61_Msk & ((value) << AIC_IPR1_PID61_Pos))
#define AIC_IPR1_PID62_Pos                    (30U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID62_Msk                    (0x1U << AIC_IPR1_PID62_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID62(value)                 (AIC_IPR1_PID62_Msk & ((value) << AIC_IPR1_PID62_Pos))
#define AIC_IPR1_PID63_Pos                    (31U)                                          /**< (AIC_IPR1) Interrupt Pending Position */
#define AIC_IPR1_PID63_Msk                    (0x1U << AIC_IPR1_PID63_Pos)                   /**< (AIC_IPR1) Interrupt Pending Mask */
#define AIC_IPR1_PID63(value)                 (AIC_IPR1_PID63_Msk & ((value) << AIC_IPR1_PID63_Pos))
#define AIC_IPR1_Msk                          (0xFFFFFFFFUL)                                 /**< (AIC_IPR1) Register Mask  */

/* -------- AIC_IPR2 : (SAIC Offset: 0x28) (R/  32) Interrupt Pending Register 2 -------- */
#define AIC_IPR2_PID64_Pos                    (0U)                                           /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID64_Msk                    (0x1U << AIC_IPR2_PID64_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID64(value)                 (AIC_IPR2_PID64_Msk & ((value) << AIC_IPR2_PID64_Pos))
#define AIC_IPR2_PID65_Pos                    (1U)                                           /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID65_Msk                    (0x1U << AIC_IPR2_PID65_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID65(value)                 (AIC_IPR2_PID65_Msk & ((value) << AIC_IPR2_PID65_Pos))
#define AIC_IPR2_PID66_Pos                    (2U)                                           /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID66_Msk                    (0x1U << AIC_IPR2_PID66_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID66(value)                 (AIC_IPR2_PID66_Msk & ((value) << AIC_IPR2_PID66_Pos))
#define AIC_IPR2_PID67_Pos                    (3U)                                           /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID67_Msk                    (0x1U << AIC_IPR2_PID67_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID67(value)                 (AIC_IPR2_PID67_Msk & ((value) << AIC_IPR2_PID67_Pos))
#define AIC_IPR2_PID68_Pos                    (4U)                                           /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID68_Msk                    (0x1U << AIC_IPR2_PID68_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID68(value)                 (AIC_IPR2_PID68_Msk & ((value) << AIC_IPR2_PID68_Pos))
#define AIC_IPR2_PID69_Pos                    (5U)                                           /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID69_Msk                    (0x1U << AIC_IPR2_PID69_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID69(value)                 (AIC_IPR2_PID69_Msk & ((value) << AIC_IPR2_PID69_Pos))
#define AIC_IPR2_PID70_Pos                    (6U)                                           /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID70_Msk                    (0x1U << AIC_IPR2_PID70_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID70(value)                 (AIC_IPR2_PID70_Msk & ((value) << AIC_IPR2_PID70_Pos))
#define AIC_IPR2_PID71_Pos                    (7U)                                           /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID71_Msk                    (0x1U << AIC_IPR2_PID71_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID71(value)                 (AIC_IPR2_PID71_Msk & ((value) << AIC_IPR2_PID71_Pos))
#define AIC_IPR2_PID72_Pos                    (8U)                                           /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID72_Msk                    (0x1U << AIC_IPR2_PID72_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID72(value)                 (AIC_IPR2_PID72_Msk & ((value) << AIC_IPR2_PID72_Pos))
#define AIC_IPR2_PID73_Pos                    (9U)                                           /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID73_Msk                    (0x1U << AIC_IPR2_PID73_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID73(value)                 (AIC_IPR2_PID73_Msk & ((value) << AIC_IPR2_PID73_Pos))
#define AIC_IPR2_SYS_Pos                      (10U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_SYS_Msk                      (0x1U << AIC_IPR2_SYS_Pos)                     /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_SYS(value)                   (AIC_IPR2_SYS_Msk & ((value) << AIC_IPR2_SYS_Pos))
#define AIC_IPR2_PID75_Pos                    (11U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID75_Msk                    (0x1U << AIC_IPR2_PID75_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID75(value)                 (AIC_IPR2_PID75_Msk & ((value) << AIC_IPR2_PID75_Pos))
#define AIC_IPR2_PID76_Pos                    (12U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID76_Msk                    (0x1U << AIC_IPR2_PID76_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID76(value)                 (AIC_IPR2_PID76_Msk & ((value) << AIC_IPR2_PID76_Pos))
#define AIC_IPR2_PID77_Pos                    (13U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID77_Msk                    (0x1U << AIC_IPR2_PID77_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID77(value)                 (AIC_IPR2_PID77_Msk & ((value) << AIC_IPR2_PID77_Pos))
#define AIC_IPR2_PID78_Pos                    (14U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID78_Msk                    (0x1U << AIC_IPR2_PID78_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID78(value)                 (AIC_IPR2_PID78_Msk & ((value) << AIC_IPR2_PID78_Pos))
#define AIC_IPR2_PID79_Pos                    (15U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID79_Msk                    (0x1U << AIC_IPR2_PID79_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID79(value)                 (AIC_IPR2_PID79_Msk & ((value) << AIC_IPR2_PID79_Pos))
#define AIC_IPR2_PID80_Pos                    (16U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID80_Msk                    (0x1U << AIC_IPR2_PID80_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID80(value)                 (AIC_IPR2_PID80_Msk & ((value) << AIC_IPR2_PID80_Pos))
#define AIC_IPR2_PID81_Pos                    (17U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID81_Msk                    (0x1U << AIC_IPR2_PID81_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID81(value)                 (AIC_IPR2_PID81_Msk & ((value) << AIC_IPR2_PID81_Pos))
#define AIC_IPR2_PID82_Pos                    (18U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID82_Msk                    (0x1U << AIC_IPR2_PID82_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID82(value)                 (AIC_IPR2_PID82_Msk & ((value) << AIC_IPR2_PID82_Pos))
#define AIC_IPR2_PID83_Pos                    (19U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID83_Msk                    (0x1U << AIC_IPR2_PID83_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID83(value)                 (AIC_IPR2_PID83_Msk & ((value) << AIC_IPR2_PID83_Pos))
#define AIC_IPR2_PID84_Pos                    (20U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID84_Msk                    (0x1U << AIC_IPR2_PID84_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID84(value)                 (AIC_IPR2_PID84_Msk & ((value) << AIC_IPR2_PID84_Pos))
#define AIC_IPR2_PID85_Pos                    (21U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID85_Msk                    (0x1U << AIC_IPR2_PID85_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID85(value)                 (AIC_IPR2_PID85_Msk & ((value) << AIC_IPR2_PID85_Pos))
#define AIC_IPR2_PID86_Pos                    (22U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID86_Msk                    (0x1U << AIC_IPR2_PID86_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID86(value)                 (AIC_IPR2_PID86_Msk & ((value) << AIC_IPR2_PID86_Pos))
#define AIC_IPR2_PID87_Pos                    (23U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID87_Msk                    (0x1U << AIC_IPR2_PID87_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID87(value)                 (AIC_IPR2_PID87_Msk & ((value) << AIC_IPR2_PID87_Pos))
#define AIC_IPR2_PID88_Pos                    (24U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID88_Msk                    (0x1U << AIC_IPR2_PID88_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID88(value)                 (AIC_IPR2_PID88_Msk & ((value) << AIC_IPR2_PID88_Pos))
#define AIC_IPR2_PID89_Pos                    (25U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID89_Msk                    (0x1U << AIC_IPR2_PID89_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID89(value)                 (AIC_IPR2_PID89_Msk & ((value) << AIC_IPR2_PID89_Pos))
#define AIC_IPR2_PID90_Pos                    (26U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID90_Msk                    (0x1U << AIC_IPR2_PID90_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID90(value)                 (AIC_IPR2_PID90_Msk & ((value) << AIC_IPR2_PID90_Pos))
#define AIC_IPR2_PID91_Pos                    (27U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID91_Msk                    (0x1U << AIC_IPR2_PID91_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID91(value)                 (AIC_IPR2_PID91_Msk & ((value) << AIC_IPR2_PID91_Pos))
#define AIC_IPR2_PID92_Pos                    (28U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID92_Msk                    (0x1U << AIC_IPR2_PID92_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID92(value)                 (AIC_IPR2_PID92_Msk & ((value) << AIC_IPR2_PID92_Pos))
#define AIC_IPR2_PID93_Pos                    (29U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID93_Msk                    (0x1U << AIC_IPR2_PID93_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID93(value)                 (AIC_IPR2_PID93_Msk & ((value) << AIC_IPR2_PID93_Pos))
#define AIC_IPR2_PID94_Pos                    (30U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID94_Msk                    (0x1U << AIC_IPR2_PID94_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID94(value)                 (AIC_IPR2_PID94_Msk & ((value) << AIC_IPR2_PID94_Pos))
#define AIC_IPR2_PID95_Pos                    (31U)                                          /**< (AIC_IPR2) Interrupt Pending Position */
#define AIC_IPR2_PID95_Msk                    (0x1U << AIC_IPR2_PID95_Pos)                   /**< (AIC_IPR2) Interrupt Pending Mask */
#define AIC_IPR2_PID95(value)                 (AIC_IPR2_PID95_Msk & ((value) << AIC_IPR2_PID95_Pos))
#define AIC_IPR2_Msk                          (0xFFFFFFFFUL)                                 /**< (AIC_IPR2) Register Mask  */

/* -------- AIC_IPR3 : (SAIC Offset: 0x2C) (R/  32) Interrupt Pending Register 3 -------- */
#define AIC_IPR3_PID96_Pos                    (0U)                                           /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID96_Msk                    (0x1U << AIC_IPR3_PID96_Pos)                   /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID96(value)                 (AIC_IPR3_PID96_Msk & ((value) << AIC_IPR3_PID96_Pos))
#define AIC_IPR3_PID97_Pos                    (1U)                                           /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID97_Msk                    (0x1U << AIC_IPR3_PID97_Pos)                   /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID97(value)                 (AIC_IPR3_PID97_Msk & ((value) << AIC_IPR3_PID97_Pos))
#define AIC_IPR3_PID98_Pos                    (2U)                                           /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID98_Msk                    (0x1U << AIC_IPR3_PID98_Pos)                   /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID98(value)                 (AIC_IPR3_PID98_Msk & ((value) << AIC_IPR3_PID98_Pos))
#define AIC_IPR3_PID99_Pos                    (3U)                                           /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID99_Msk                    (0x1U << AIC_IPR3_PID99_Pos)                   /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID99(value)                 (AIC_IPR3_PID99_Msk & ((value) << AIC_IPR3_PID99_Pos))
#define AIC_IPR3_PID100_Pos                   (4U)                                           /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID100_Msk                   (0x1U << AIC_IPR3_PID100_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID100(value)                (AIC_IPR3_PID100_Msk & ((value) << AIC_IPR3_PID100_Pos))
#define AIC_IPR3_PID101_Pos                   (5U)                                           /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID101_Msk                   (0x1U << AIC_IPR3_PID101_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID101(value)                (AIC_IPR3_PID101_Msk & ((value) << AIC_IPR3_PID101_Pos))
#define AIC_IPR3_PID102_Pos                   (6U)                                           /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID102_Msk                   (0x1U << AIC_IPR3_PID102_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID102(value)                (AIC_IPR3_PID102_Msk & ((value) << AIC_IPR3_PID102_Pos))
#define AIC_IPR3_PID103_Pos                   (7U)                                           /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID103_Msk                   (0x1U << AIC_IPR3_PID103_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID103(value)                (AIC_IPR3_PID103_Msk & ((value) << AIC_IPR3_PID103_Pos))
#define AIC_IPR3_PID104_Pos                   (8U)                                           /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID104_Msk                   (0x1U << AIC_IPR3_PID104_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID104(value)                (AIC_IPR3_PID104_Msk & ((value) << AIC_IPR3_PID104_Pos))
#define AIC_IPR3_PID105_Pos                   (9U)                                           /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID105_Msk                   (0x1U << AIC_IPR3_PID105_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID105(value)                (AIC_IPR3_PID105_Msk & ((value) << AIC_IPR3_PID105_Pos))
#define AIC_IPR3_PID106_Pos                   (10U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID106_Msk                   (0x1U << AIC_IPR3_PID106_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID106(value)                (AIC_IPR3_PID106_Msk & ((value) << AIC_IPR3_PID106_Pos))
#define AIC_IPR3_PID107_Pos                   (11U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID107_Msk                   (0x1U << AIC_IPR3_PID107_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID107(value)                (AIC_IPR3_PID107_Msk & ((value) << AIC_IPR3_PID107_Pos))
#define AIC_IPR3_PID108_Pos                   (12U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID108_Msk                   (0x1U << AIC_IPR3_PID108_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID108(value)                (AIC_IPR3_PID108_Msk & ((value) << AIC_IPR3_PID108_Pos))
#define AIC_IPR3_PID109_Pos                   (13U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID109_Msk                   (0x1U << AIC_IPR3_PID109_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID109(value)                (AIC_IPR3_PID109_Msk & ((value) << AIC_IPR3_PID109_Pos))
#define AIC_IPR3_PID110_Pos                   (14U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID110_Msk                   (0x1U << AIC_IPR3_PID110_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID110(value)                (AIC_IPR3_PID110_Msk & ((value) << AIC_IPR3_PID110_Pos))
#define AIC_IPR3_PID111_Pos                   (15U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID111_Msk                   (0x1U << AIC_IPR3_PID111_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID111(value)                (AIC_IPR3_PID111_Msk & ((value) << AIC_IPR3_PID111_Pos))
#define AIC_IPR3_PID112_Pos                   (16U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID112_Msk                   (0x1U << AIC_IPR3_PID112_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID112(value)                (AIC_IPR3_PID112_Msk & ((value) << AIC_IPR3_PID112_Pos))
#define AIC_IPR3_PID113_Pos                   (17U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID113_Msk                   (0x1U << AIC_IPR3_PID113_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID113(value)                (AIC_IPR3_PID113_Msk & ((value) << AIC_IPR3_PID113_Pos))
#define AIC_IPR3_PID114_Pos                   (18U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID114_Msk                   (0x1U << AIC_IPR3_PID114_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID114(value)                (AIC_IPR3_PID114_Msk & ((value) << AIC_IPR3_PID114_Pos))
#define AIC_IPR3_PID115_Pos                   (19U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID115_Msk                   (0x1U << AIC_IPR3_PID115_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID115(value)                (AIC_IPR3_PID115_Msk & ((value) << AIC_IPR3_PID115_Pos))
#define AIC_IPR3_PID116_Pos                   (20U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID116_Msk                   (0x1U << AIC_IPR3_PID116_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID116(value)                (AIC_IPR3_PID116_Msk & ((value) << AIC_IPR3_PID116_Pos))
#define AIC_IPR3_PID117_Pos                   (21U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID117_Msk                   (0x1U << AIC_IPR3_PID117_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID117(value)                (AIC_IPR3_PID117_Msk & ((value) << AIC_IPR3_PID117_Pos))
#define AIC_IPR3_PID118_Pos                   (22U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID118_Msk                   (0x1U << AIC_IPR3_PID118_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID118(value)                (AIC_IPR3_PID118_Msk & ((value) << AIC_IPR3_PID118_Pos))
#define AIC_IPR3_PID119_Pos                   (23U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID119_Msk                   (0x1U << AIC_IPR3_PID119_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID119(value)                (AIC_IPR3_PID119_Msk & ((value) << AIC_IPR3_PID119_Pos))
#define AIC_IPR3_PID120_Pos                   (24U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID120_Msk                   (0x1U << AIC_IPR3_PID120_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID120(value)                (AIC_IPR3_PID120_Msk & ((value) << AIC_IPR3_PID120_Pos))
#define AIC_IPR3_PID121_Pos                   (25U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID121_Msk                   (0x1U << AIC_IPR3_PID121_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID121(value)                (AIC_IPR3_PID121_Msk & ((value) << AIC_IPR3_PID121_Pos))
#define AIC_IPR3_PID122_Pos                   (26U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID122_Msk                   (0x1U << AIC_IPR3_PID122_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID122(value)                (AIC_IPR3_PID122_Msk & ((value) << AIC_IPR3_PID122_Pos))
#define AIC_IPR3_PID123_Pos                   (27U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID123_Msk                   (0x1U << AIC_IPR3_PID123_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID123(value)                (AIC_IPR3_PID123_Msk & ((value) << AIC_IPR3_PID123_Pos))
#define AIC_IPR3_PID124_Pos                   (28U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID124_Msk                   (0x1U << AIC_IPR3_PID124_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID124(value)                (AIC_IPR3_PID124_Msk & ((value) << AIC_IPR3_PID124_Pos))
#define AIC_IPR3_PID125_Pos                   (29U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID125_Msk                   (0x1U << AIC_IPR3_PID125_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID125(value)                (AIC_IPR3_PID125_Msk & ((value) << AIC_IPR3_PID125_Pos))
#define AIC_IPR3_PID126_Pos                   (30U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID126_Msk                   (0x1U << AIC_IPR3_PID126_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID126(value)                (AIC_IPR3_PID126_Msk & ((value) << AIC_IPR3_PID126_Pos))
#define AIC_IPR3_PID127_Pos                   (31U)                                          /**< (AIC_IPR3) Interrupt Pending Position */
#define AIC_IPR3_PID127_Msk                   (0x1U << AIC_IPR3_PID127_Pos)                  /**< (AIC_IPR3) Interrupt Pending Mask */
#define AIC_IPR3_PID127(value)                (AIC_IPR3_PID127_Msk & ((value) << AIC_IPR3_PID127_Pos))
#define AIC_IPR3_Msk                          (0xFFFFFFFFUL)                                 /**< (AIC_IPR3) Register Mask  */

/* -------- AIC_IMR : (SAIC Offset: 0x30) (R/  32) Interrupt Mask Register -------- */
#define AIC_IMR_INTM_Pos                      (0U)                                           /**< (AIC_IMR) Interrupt Mask Position */
#define AIC_IMR_INTM_Msk                      (0x1U << AIC_IMR_INTM_Pos)                     /**< (AIC_IMR) Interrupt Mask Mask */
#define AIC_IMR_INTM(value)                   (AIC_IMR_INTM_Msk & ((value) << AIC_IMR_INTM_Pos))
#define AIC_IMR_Msk                           (0x00000001UL)                                 /**< (AIC_IMR) Register Mask  */

/* -------- AIC_CISR : (SAIC Offset: 0x34) (R/  32) Core Interrupt Status Register -------- */
#define AIC_CISR_NFIQ_Pos                     (0U)                                           /**< (AIC_CISR) NFIQ Status Position */
#define AIC_CISR_NFIQ_Msk                     (0x1U << AIC_CISR_NFIQ_Pos)                    /**< (AIC_CISR) NFIQ Status Mask */
#define AIC_CISR_NFIQ(value)                  (AIC_CISR_NFIQ_Msk & ((value) << AIC_CISR_NFIQ_Pos))
#define AIC_CISR_NIRQ_Pos                     (1U)                                           /**< (AIC_CISR) NIRQ Status Position */
#define AIC_CISR_NIRQ_Msk                     (0x1U << AIC_CISR_NIRQ_Pos)                    /**< (AIC_CISR) NIRQ Status Mask */
#define AIC_CISR_NIRQ(value)                  (AIC_CISR_NIRQ_Msk & ((value) << AIC_CISR_NIRQ_Pos))
#define AIC_CISR_Msk                          (0x00000003UL)                                 /**< (AIC_CISR) Register Mask  */

/* -------- AIC_EOICR : (SAIC Offset: 0x38) ( /W 32) End of Interrupt Command Register -------- */
#define AIC_EOICR_ENDIT_Pos                   (0U)                                           /**< (AIC_EOICR) Interrupt Processing Complete Command Position */
#define AIC_EOICR_ENDIT_Msk                   (0x1U << AIC_EOICR_ENDIT_Pos)                  /**< (AIC_EOICR) Interrupt Processing Complete Command Mask */
#define AIC_EOICR_ENDIT(value)                (AIC_EOICR_ENDIT_Msk & ((value) << AIC_EOICR_ENDIT_Pos))
#define AIC_EOICR_Msk                         (0x00000001UL)                                 /**< (AIC_EOICR) Register Mask  */

/* -------- AIC_SPU : (SAIC Offset: 0x3C) (R/W 32) Spurious Interrupt Vector Register -------- */
#define AIC_SPU_SIVR_Pos                      (0U)                                           /**< (AIC_SPU) Spurious Interrupt Vector Register Position */
#define AIC_SPU_SIVR_Msk                      (0xFFFFFFFFU << AIC_SPU_SIVR_Pos)              /**< (AIC_SPU) Spurious Interrupt Vector Register Mask */
#define AIC_SPU_SIVR(value)                   (AIC_SPU_SIVR_Msk & ((value) << AIC_SPU_SIVR_Pos))
#define AIC_SPU_Msk                           (0xFFFFFFFFUL)                                 /**< (AIC_SPU) Register Mask  */

/* -------- AIC_IECR : (SAIC Offset: 0x40) ( /W 32) Interrupt Enable Command Register -------- */
#define AIC_IECR_INTEN_Pos                    (0U)                                           /**< (AIC_IECR) Interrupt Enable Position */
#define AIC_IECR_INTEN_Msk                    (0x1U << AIC_IECR_INTEN_Pos)                   /**< (AIC_IECR) Interrupt Enable Mask */
#define AIC_IECR_INTEN(value)                 (AIC_IECR_INTEN_Msk & ((value) << AIC_IECR_INTEN_Pos))
#define AIC_IECR_Msk                          (0x00000001UL)                                 /**< (AIC_IECR) Register Mask  */

/* -------- AIC_IDCR : (SAIC Offset: 0x44) ( /W 32) Interrupt Disable Command Register -------- */
#define AIC_IDCR_INTD_Pos                     (0U)                                           /**< (AIC_IDCR) Interrupt Disable Position */
#define AIC_IDCR_INTD_Msk                     (0x1U << AIC_IDCR_INTD_Pos)                    /**< (AIC_IDCR) Interrupt Disable Mask */
#define AIC_IDCR_INTD(value)                  (AIC_IDCR_INTD_Msk & ((value) << AIC_IDCR_INTD_Pos))
#define AIC_IDCR_Msk                          (0x00000001UL)                                 /**< (AIC_IDCR) Register Mask  */

/* -------- AIC_ICCR : (SAIC Offset: 0x48) ( /W 32) Interrupt Clear Command Register -------- */
#define AIC_ICCR_INTCLR_Pos                   (0U)                                           /**< (AIC_ICCR) Interrupt Clear Position */
#define AIC_ICCR_INTCLR_Msk                   (0x1U << AIC_ICCR_INTCLR_Pos)                  /**< (AIC_ICCR) Interrupt Clear Mask */
#define AIC_ICCR_INTCLR(value)                (AIC_ICCR_INTCLR_Msk & ((value) << AIC_ICCR_INTCLR_Pos))
#define AIC_ICCR_Msk                          (0x00000001UL)                                 /**< (AIC_ICCR) Register Mask  */

/* -------- AIC_ISCR : (SAIC Offset: 0x4C) ( /W 32) Interrupt Set Command Register -------- */
#define AIC_ISCR_INTSET_Pos                   (0U)                                           /**< (AIC_ISCR) Interrupt Set Position */
#define AIC_ISCR_INTSET_Msk                   (0x1U << AIC_ISCR_INTSET_Pos)                  /**< (AIC_ISCR) Interrupt Set Mask */
#define AIC_ISCR_INTSET(value)                (AIC_ISCR_INTSET_Msk & ((value) << AIC_ISCR_INTSET_Pos))
#define AIC_ISCR_Msk                          (0x00000001UL)                                 /**< (AIC_ISCR) Register Mask  */

/* -------- AIC_DCR : (SAIC Offset: 0x6C) (R/W 32) Debug Control Register -------- */
#define AIC_DCR_PROT_Pos                      (0U)                                           /**< (AIC_DCR) Protection Mode Position */
#define AIC_DCR_PROT_Msk                      (0x1U << AIC_DCR_PROT_Pos)                     /**< (AIC_DCR) Protection Mode Mask */
#define AIC_DCR_PROT(value)                   (AIC_DCR_PROT_Msk & ((value) << AIC_DCR_PROT_Pos))
#define AIC_DCR_GMSK_Pos                      (1U)                                           /**< (AIC_DCR) General Interrupt Mask Position */
#define AIC_DCR_GMSK_Msk                      (0x1U << AIC_DCR_GMSK_Pos)                     /**< (AIC_DCR) General Interrupt Mask Mask */
#define AIC_DCR_GMSK(value)                   (AIC_DCR_GMSK_Msk & ((value) << AIC_DCR_GMSK_Pos))
#define AIC_DCR_Msk                           (0x00000003UL)                                 /**< (AIC_DCR) Register Mask  */

/* -------- AIC_WPMR : (SAIC Offset: 0xE4) (R/W 32) Write Protection Mode Register -------- */
#define AIC_WPMR_WPEN_Pos                     (0U)                                           /**< (AIC_WPMR) Write Protection Enable Position */
#define AIC_WPMR_WPEN_Msk                     (0x1U << AIC_WPMR_WPEN_Pos)                    /**< (AIC_WPMR) Write Protection Enable Mask */
#define AIC_WPMR_WPEN(value)                  (AIC_WPMR_WPEN_Msk & ((value) << AIC_WPMR_WPEN_Pos))
#define AIC_WPMR_WPKEY_Pos                    (8U)                                           /**< (AIC_WPMR) Write Protection Key Position */
#define AIC_WPMR_WPKEY_Msk                    (0xFFFFFFU << AIC_WPMR_WPKEY_Pos)              /**< (AIC_WPMR) Write Protection Key Mask */
#define AIC_WPMR_WPKEY(value)                 (AIC_WPMR_WPKEY_Msk & ((value) << AIC_WPMR_WPKEY_Pos))
#define   AIC_WPMR_WPKEY_PASSWD_Val           (4278595U)                                     /**< (AIC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0.  */
#define AIC_WPMR_WPKEY_PASSWD                 (AIC_WPMR_WPKEY_PASSWD_Val << AIC_WPMR_WPKEY_Pos) /**< (AIC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0. Position  */
#define AIC_WPMR_Msk                          (0xFFFFFF01UL)                                 /**< (AIC_WPMR) Register Mask  */

/* -------- AIC_WPSR : (SAIC Offset: 0xE8) (R/  32) Write Protection Status Register -------- */
#define AIC_WPSR_WPVS_Pos                     (0U)                                           /**< (AIC_WPSR) Write Protection Violation Status Position */
#define AIC_WPSR_WPVS_Msk                     (0x1U << AIC_WPSR_WPVS_Pos)                    /**< (AIC_WPSR) Write Protection Violation Status Mask */
#define AIC_WPSR_WPVS(value)                  (AIC_WPSR_WPVS_Msk & ((value) << AIC_WPSR_WPVS_Pos))
#define AIC_WPSR_WPVSRC_Pos                   (8U)                                           /**< (AIC_WPSR) Write Protection Violation Source Position */
#define AIC_WPSR_WPVSRC_Msk                   (0xFFFFU << AIC_WPSR_WPVSRC_Pos)               /**< (AIC_WPSR) Write Protection Violation Source Mask */
#define AIC_WPSR_WPVSRC(value)                (AIC_WPSR_WPVSRC_Msk & ((value) << AIC_WPSR_WPVSRC_Pos))
#define AIC_WPSR_Msk                          (0x00FFFF01UL)                                 /**< (AIC_WPSR) Register Mask  */

/* -------- AIC_VERSION : (SAIC Offset: 0xFC) (R/  32) AIC Version Register -------- */
#define AIC_VERSION_VERSION_Pos               (0U)                                           /**< (AIC_VERSION) Version of the Hardware Module Position */
#define AIC_VERSION_VERSION_Msk               (0xFFFU << AIC_VERSION_VERSION_Pos)            /**< (AIC_VERSION) Version of the Hardware Module Mask */
#define AIC_VERSION_VERSION(value)            (AIC_VERSION_VERSION_Msk & ((value) << AIC_VERSION_VERSION_Pos))
#define AIC_VERSION_MFN_Pos                   (16U)                                          /**< (AIC_VERSION) Metal Fix Number Position */
#define AIC_VERSION_MFN_Msk                   (0x7U << AIC_VERSION_MFN_Pos)                  /**< (AIC_VERSION) Metal Fix Number Mask */
#define AIC_VERSION_MFN(value)                (AIC_VERSION_MFN_Msk & ((value) << AIC_VERSION_MFN_Pos))
#define AIC_VERSION_Msk                       (0x00070FFFUL)                                 /**< (AIC_VERSION) Register Mask  */

/** \brief SAIC register offsets definitions */
#define AIC_SSR_OFFSET                 (0x00)         /**< (AIC_SSR) Source Select Register Offset */
#define AIC_SMR_OFFSET                 (0x04)         /**< (AIC_SMR) Source Mode Register Offset */
#define AIC_SVR_OFFSET                 (0x08)         /**< (AIC_SVR) Source Vector Register Offset */
#define AIC_IVR_OFFSET                 (0x10)         /**< (AIC_IVR) Interrupt Vector Register Offset */
#define AIC_FVR_OFFSET                 (0x14)         /**< (AIC_FVR) FIQ Vector Register Offset */
#define AIC_ISR_OFFSET                 (0x18)         /**< (AIC_ISR) Interrupt Status Register Offset */
#define AIC_IPR0_OFFSET                (0x20)         /**< (AIC_IPR0) Interrupt Pending Register 0 Offset */
#define AIC_IPR1_OFFSET                (0x24)         /**< (AIC_IPR1) Interrupt Pending Register 1 Offset */
#define AIC_IPR2_OFFSET                (0x28)         /**< (AIC_IPR2) Interrupt Pending Register 2 Offset */
#define AIC_IPR3_OFFSET                (0x2C)         /**< (AIC_IPR3) Interrupt Pending Register 3 Offset */
#define AIC_IMR_OFFSET                 (0x30)         /**< (AIC_IMR) Interrupt Mask Register Offset */
#define AIC_CISR_OFFSET                (0x34)         /**< (AIC_CISR) Core Interrupt Status Register Offset */
#define AIC_EOICR_OFFSET               (0x38)         /**< (AIC_EOICR) End of Interrupt Command Register Offset */
#define AIC_SPU_OFFSET                 (0x3C)         /**< (AIC_SPU) Spurious Interrupt Vector Register Offset */
#define AIC_IECR_OFFSET                (0x40)         /**< (AIC_IECR) Interrupt Enable Command Register Offset */
#define AIC_IDCR_OFFSET                (0x44)         /**< (AIC_IDCR) Interrupt Disable Command Register Offset */
#define AIC_ICCR_OFFSET                (0x48)         /**< (AIC_ICCR) Interrupt Clear Command Register Offset */
#define AIC_ISCR_OFFSET                (0x4C)         /**< (AIC_ISCR) Interrupt Set Command Register Offset */
#define AIC_DCR_OFFSET                 (0x6C)         /**< (AIC_DCR) Debug Control Register Offset */
#define AIC_WPMR_OFFSET                (0xE4)         /**< (AIC_WPMR) Write Protection Mode Register Offset */
#define AIC_WPSR_OFFSET                (0xE8)         /**< (AIC_WPSR) Write Protection Status Register Offset */
#define AIC_VERSION_OFFSET             (0xFC)         /**< (AIC_VERSION) AIC Version Register Offset */

/** \brief SAIC register API structure */
typedef struct
{
  __IO  uint32_t                       AIC_SSR;         /**< Offset: 0x00 (R/W  32) Source Select Register */
  __IO  uint32_t                       AIC_SMR;         /**< Offset: 0x04 (R/W  32) Source Mode Register */
  __IO  uint32_t                       AIC_SVR;         /**< Offset: 0x08 (R/W  32) Source Vector Register */
  __I   uint8_t                        Reserved1[0x04];
  __I   uint32_t                       AIC_IVR;         /**< Offset: 0x10 (R/   32) Interrupt Vector Register */
  __I   uint32_t                       AIC_FVR;         /**< Offset: 0x14 (R/   32) FIQ Vector Register */
  __I   uint32_t                       AIC_ISR;         /**< Offset: 0x18 (R/   32) Interrupt Status Register */
  __I   uint8_t                        Reserved2[0x04];
  __I   uint32_t                       AIC_IPR0;        /**< Offset: 0x20 (R/   32) Interrupt Pending Register 0 */
  __I   uint32_t                       AIC_IPR1;        /**< Offset: 0x24 (R/   32) Interrupt Pending Register 1 */
  __I   uint32_t                       AIC_IPR2;        /**< Offset: 0x28 (R/   32) Interrupt Pending Register 2 */
  __I   uint32_t                       AIC_IPR3;        /**< Offset: 0x2c (R/   32) Interrupt Pending Register 3 */
  __I   uint32_t                       AIC_IMR;         /**< Offset: 0x30 (R/   32) Interrupt Mask Register */
  __I   uint32_t                       AIC_CISR;        /**< Offset: 0x34 (R/   32) Core Interrupt Status Register */
  __O   uint32_t                       AIC_EOICR;       /**< Offset: 0x38 ( /W  32) End of Interrupt Command Register */
  __IO  uint32_t                       AIC_SPU;         /**< Offset: 0x3c (R/W  32) Spurious Interrupt Vector Register */
  __O   uint32_t                       AIC_IECR;        /**< Offset: 0x40 ( /W  32) Interrupt Enable Command Register */
  __O   uint32_t                       AIC_IDCR;        /**< Offset: 0x44 ( /W  32) Interrupt Disable Command Register */
  __O   uint32_t                       AIC_ICCR;        /**< Offset: 0x48 ( /W  32) Interrupt Clear Command Register */
  __O   uint32_t                       AIC_ISCR;        /**< Offset: 0x4c ( /W  32) Interrupt Set Command Register */
  __I   uint8_t                        Reserved3[0x1C];
  __IO  uint32_t                       AIC_DCR;         /**< Offset: 0x6c (R/W  32) Debug Control Register */
  __I   uint8_t                        Reserved4[0x74];
  __IO  uint32_t                       AIC_WPMR;        /**< Offset: 0xe4 (R/W  32) Write Protection Mode Register */
  __I   uint32_t                       AIC_WPSR;        /**< Offset: 0xe8 (R/   32) Write Protection Status Register */
  __I   uint8_t                        Reserved5[0x10];
  __I   uint32_t                       AIC_VERSION;     /**< Offset: 0xfc (R/   32) AIC Version Register */
} saic_registers_t;
/** @}  end of Secure Advanced Interrupt Controller */

#endif /* SAMA5D2_SAMA5D2_SAIC_MODULE_H */

