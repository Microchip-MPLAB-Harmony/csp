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

/* file generated from device description version 2018-10-05T01:07:33Z */
#ifndef SAMA5D2_SAMA5D2_SAIC_MODULE_H
#define SAMA5D2_SAMA5D2_SAIC_MODULE_H

/** \addtogroup SAMA5D2_SAMA5D2 Secure Advanced Interrupt Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMA5D2_SAIC                                 */
/* ========================================================================== */

/* -------- SAIC_SSR : (SAIC Offset: 0x00) (R/W 32) Source Select Register -------- */
#define SAIC_SSR_INTSEL_Pos                   (0U)                                           /**< (SAIC_SSR) Interrupt Line Selection Position */
#define SAIC_SSR_INTSEL_Msk                   (0x7FU << SAIC_SSR_INTSEL_Pos)                 /**< (SAIC_SSR) Interrupt Line Selection Mask */
#define SAIC_SSR_INTSEL(value)                (SAIC_SSR_INTSEL_Msk & ((value) << SAIC_SSR_INTSEL_Pos))
#define SAIC_SSR_Msk                          (0x0000007FUL)                                 /**< (SAIC_SSR) Register Mask  */

/* -------- SAIC_SMR : (SAIC Offset: 0x04) (R/W 32) Source Mode Register -------- */
#define SAIC_SMR_PRIORITY_Pos                 (0U)                                           /**< (SAIC_SMR) Priority Level Position */
#define SAIC_SMR_PRIORITY_Msk                 (0x7U << SAIC_SMR_PRIORITY_Pos)                /**< (SAIC_SMR) Priority Level Mask */
#define SAIC_SMR_PRIORITY(value)              (SAIC_SMR_PRIORITY_Msk & ((value) << SAIC_SMR_PRIORITY_Pos))
#define   SAIC_SMR_PRIORITY_MINIMUM_Val       (0U)                                           /**< (SAIC_SMR) Minimum priority  */
#define   SAIC_SMR_PRIORITY_VERY_LOW_Val      (1U)                                           /**< (SAIC_SMR) Very low priority  */
#define   SAIC_SMR_PRIORITY_LOW_Val           (2U)                                           /**< (SAIC_SMR) Low priority  */
#define   SAIC_SMR_PRIORITY_MEDIUM_LOW_Val    (3U)                                           /**< (SAIC_SMR) Medium priority  */
#define   SAIC_SMR_PRIORITY_MEDIUM_HIGH_Val   (4U)                                           /**< (SAIC_SMR) Medium-high priority  */
#define   SAIC_SMR_PRIORITY_HIGH_Val          (5U)                                           /**< (SAIC_SMR) High priority  */
#define   SAIC_SMR_PRIORITY_VERY_HIGH_Val     (6U)                                           /**< (SAIC_SMR) Very high priority  */
#define   SAIC_SMR_PRIORITY_MAXIMUM_Val       (7U)                                           /**< (SAIC_SMR) Maximum priority  */
#define SAIC_SMR_PRIORITY_MINIMUM             (SAIC_SMR_PRIORITY_MINIMUM_Val << SAIC_SMR_PRIORITY_Pos) /**< (SAIC_SMR) Minimum priority Position  */
#define SAIC_SMR_PRIORITY_VERY_LOW            (SAIC_SMR_PRIORITY_VERY_LOW_Val << SAIC_SMR_PRIORITY_Pos) /**< (SAIC_SMR) Very low priority Position  */
#define SAIC_SMR_PRIORITY_LOW                 (SAIC_SMR_PRIORITY_LOW_Val << SAIC_SMR_PRIORITY_Pos) /**< (SAIC_SMR) Low priority Position  */
#define SAIC_SMR_PRIORITY_MEDIUM_LOW          (SAIC_SMR_PRIORITY_MEDIUM_LOW_Val << SAIC_SMR_PRIORITY_Pos) /**< (SAIC_SMR) Medium priority Position  */
#define SAIC_SMR_PRIORITY_MEDIUM_HIGH         (SAIC_SMR_PRIORITY_MEDIUM_HIGH_Val << SAIC_SMR_PRIORITY_Pos) /**< (SAIC_SMR) Medium-high priority Position  */
#define SAIC_SMR_PRIORITY_HIGH                (SAIC_SMR_PRIORITY_HIGH_Val << SAIC_SMR_PRIORITY_Pos) /**< (SAIC_SMR) High priority Position  */
#define SAIC_SMR_PRIORITY_VERY_HIGH           (SAIC_SMR_PRIORITY_VERY_HIGH_Val << SAIC_SMR_PRIORITY_Pos) /**< (SAIC_SMR) Very high priority Position  */
#define SAIC_SMR_PRIORITY_MAXIMUM             (SAIC_SMR_PRIORITY_MAXIMUM_Val << SAIC_SMR_PRIORITY_Pos) /**< (SAIC_SMR) Maximum priority Position  */
#define SAIC_SMR_SRCTYPE_Pos                  (5U)                                           /**< (SAIC_SMR) Interrupt Source Type Position */
#define SAIC_SMR_SRCTYPE_Msk                  (0x3U << SAIC_SMR_SRCTYPE_Pos)                 /**< (SAIC_SMR) Interrupt Source Type Mask */
#define SAIC_SMR_SRCTYPE(value)               (SAIC_SMR_SRCTYPE_Msk & ((value) << SAIC_SMR_SRCTYPE_Pos))
#define   SAIC_SMR_SRCTYPE_INT_LEVEL_SENSITIVE_Val (0U)                                           /**< (SAIC_SMR) High-level sensitive for internal source. Low-level sensitive for external source  */
#define   SAIC_SMR_SRCTYPE_EXT_NEGATIVE_EDGE_Val (1U)                                           /**< (SAIC_SMR) Negative-edge triggered for external source  */
#define   SAIC_SMR_SRCTYPE_EXT_HIGH_LEVEL_Val (2U)                                           /**< (SAIC_SMR) High-level sensitive for internal source. High-level sensitive for external source  */
#define   SAIC_SMR_SRCTYPE_EXT_POSITIVE_EDGE_Val (3U)                                           /**< (SAIC_SMR) Positive-edge triggered for external source  */
#define SAIC_SMR_SRCTYPE_INT_LEVEL_SENSITIVE  (SAIC_SMR_SRCTYPE_INT_LEVEL_SENSITIVE_Val << SAIC_SMR_SRCTYPE_Pos) /**< (SAIC_SMR) High-level sensitive for internal source. Low-level sensitive for external source Position  */
#define SAIC_SMR_SRCTYPE_EXT_NEGATIVE_EDGE    (SAIC_SMR_SRCTYPE_EXT_NEGATIVE_EDGE_Val << SAIC_SMR_SRCTYPE_Pos) /**< (SAIC_SMR) Negative-edge triggered for external source Position  */
#define SAIC_SMR_SRCTYPE_EXT_HIGH_LEVEL       (SAIC_SMR_SRCTYPE_EXT_HIGH_LEVEL_Val << SAIC_SMR_SRCTYPE_Pos) /**< (SAIC_SMR) High-level sensitive for internal source. High-level sensitive for external source Position  */
#define SAIC_SMR_SRCTYPE_EXT_POSITIVE_EDGE    (SAIC_SMR_SRCTYPE_EXT_POSITIVE_EDGE_Val << SAIC_SMR_SRCTYPE_Pos) /**< (SAIC_SMR) Positive-edge triggered for external source Position  */
#define SAIC_SMR_Msk                          (0x00000067UL)                                 /**< (SAIC_SMR) Register Mask  */

/* -------- SAIC_SVR : (SAIC Offset: 0x08) (R/W 32) Source Vector Register -------- */
#define SAIC_SVR_VECTOR_Pos                   (0U)                                           /**< (SAIC_SVR) Source Vector Position */
#define SAIC_SVR_VECTOR_Msk                   (0xFFFFFFFFU << SAIC_SVR_VECTOR_Pos)           /**< (SAIC_SVR) Source Vector Mask */
#define SAIC_SVR_VECTOR(value)                (SAIC_SVR_VECTOR_Msk & ((value) << SAIC_SVR_VECTOR_Pos))
#define SAIC_SVR_Msk                          (0xFFFFFFFFUL)                                 /**< (SAIC_SVR) Register Mask  */

/* -------- SAIC_IVR : (SAIC Offset: 0x10) (R/  32) Interrupt Vector Register -------- */
#define SAIC_IVR_IRQV_Pos                     (0U)                                           /**< (SAIC_IVR) Interrupt Vector Register Position */
#define SAIC_IVR_IRQV_Msk                     (0xFFFFFFFFU << SAIC_IVR_IRQV_Pos)             /**< (SAIC_IVR) Interrupt Vector Register Mask */
#define SAIC_IVR_IRQV(value)                  (SAIC_IVR_IRQV_Msk & ((value) << SAIC_IVR_IRQV_Pos))
#define SAIC_IVR_Msk                          (0xFFFFFFFFUL)                                 /**< (SAIC_IVR) Register Mask  */

/* -------- SAIC_FVR : (SAIC Offset: 0x14) (R/  32) FIQ Vector Register -------- */
#define SAIC_FVR_FIQV_Pos                     (0U)                                           /**< (SAIC_FVR) FIQ Vector Register Position */
#define SAIC_FVR_FIQV_Msk                     (0xFFFFFFFFU << SAIC_FVR_FIQV_Pos)             /**< (SAIC_FVR) FIQ Vector Register Mask */
#define SAIC_FVR_FIQV(value)                  (SAIC_FVR_FIQV_Msk & ((value) << SAIC_FVR_FIQV_Pos))
#define SAIC_FVR_Msk                          (0xFFFFFFFFUL)                                 /**< (SAIC_FVR) Register Mask  */

/* -------- SAIC_ISR : (SAIC Offset: 0x18) (R/  32) Interrupt Status Register -------- */
#define SAIC_ISR_IRQID_Pos                    (0U)                                           /**< (SAIC_ISR) Current Interrupt Identifier Position */
#define SAIC_ISR_IRQID_Msk                    (0x7FU << SAIC_ISR_IRQID_Pos)                  /**< (SAIC_ISR) Current Interrupt Identifier Mask */
#define SAIC_ISR_IRQID(value)                 (SAIC_ISR_IRQID_Msk & ((value) << SAIC_ISR_IRQID_Pos))
#define SAIC_ISR_Msk                          (0x0000007FUL)                                 /**< (SAIC_ISR) Register Mask  */

/* -------- SAIC_IPR0 : (SAIC Offset: 0x20) (R/  32) Interrupt Pending Register 0 -------- */
#define SAIC_IPR0_PID0_SAIC_FIQ_Pos           (0U)                                           /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID0_SAIC_FIQ_Msk           (0x1U << SAIC_IPR0_PID0_SAIC_FIQ_Pos)          /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID0_SAIC_FIQ(value)        (SAIC_IPR0_PID0_SAIC_FIQ_Msk & ((value) << SAIC_IPR0_PID0_SAIC_FIQ_Pos))
#define SAIC_IPR0_PID2_PMU_Pos                (2U)                                           /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID2_PMU_Msk                (0x1U << SAIC_IPR0_PID2_PMU_Pos)               /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID2_PMU(value)             (SAIC_IPR0_PID2_PMU_Msk & ((value) << SAIC_IPR0_PID2_PMU_Pos))
#define SAIC_IPR0_PID3_PIT_Pos                (3U)                                           /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID3_PIT_Msk                (0x1U << SAIC_IPR0_PID3_PIT_Pos)               /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID3_PIT(value)             (SAIC_IPR0_PID3_PIT_Msk & ((value) << SAIC_IPR0_PID3_PIT_Pos))
#define SAIC_IPR0_PID4_WDT_Pos                (4U)                                           /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID4_WDT_Msk                (0x1U << SAIC_IPR0_PID4_WDT_Pos)               /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID4_WDT(value)             (SAIC_IPR0_PID4_WDT_Msk & ((value) << SAIC_IPR0_PID4_WDT_Pos))
#define SAIC_IPR0_PID5_GMAC_Pos               (5U)                                           /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID5_GMAC_Msk               (0x1U << SAIC_IPR0_PID5_GMAC_Pos)              /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID5_GMAC(value)            (SAIC_IPR0_PID5_GMAC_Msk & ((value) << SAIC_IPR0_PID5_GMAC_Pos))
#define SAIC_IPR0_PID6_XDMAC0_Pos             (6U)                                           /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID6_XDMAC0_Msk             (0x1U << SAIC_IPR0_PID6_XDMAC0_Pos)            /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID6_XDMAC0(value)          (SAIC_IPR0_PID6_XDMAC0_Msk & ((value) << SAIC_IPR0_PID6_XDMAC0_Pos))
#define SAIC_IPR0_PID7_XDMAC1_Pos             (7U)                                           /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID7_XDMAC1_Msk             (0x1U << SAIC_IPR0_PID7_XDMAC1_Pos)            /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID7_XDMAC1(value)          (SAIC_IPR0_PID7_XDMAC1_Msk & ((value) << SAIC_IPR0_PID7_XDMAC1_Pos))
#define SAIC_IPR0_PID8_ICM_Pos                (8U)                                           /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID8_ICM_Msk                (0x1U << SAIC_IPR0_PID8_ICM_Pos)               /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID8_ICM(value)             (SAIC_IPR0_PID8_ICM_Msk & ((value) << SAIC_IPR0_PID8_ICM_Pos))
#define SAIC_IPR0_PID9_AES_Pos                (9U)                                           /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID9_AES_Msk                (0x1U << SAIC_IPR0_PID9_AES_Pos)               /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID9_AES(value)             (SAIC_IPR0_PID9_AES_Msk & ((value) << SAIC_IPR0_PID9_AES_Pos))
#define SAIC_IPR0_PID10_AESB_Pos              (10U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID10_AESB_Msk              (0x1U << SAIC_IPR0_PID10_AESB_Pos)             /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID10_AESB(value)           (SAIC_IPR0_PID10_AESB_Msk & ((value) << SAIC_IPR0_PID10_AESB_Pos))
#define SAIC_IPR0_PID11_TDES_Pos              (11U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID11_TDES_Msk              (0x1U << SAIC_IPR0_PID11_TDES_Pos)             /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID11_TDES(value)           (SAIC_IPR0_PID11_TDES_Msk & ((value) << SAIC_IPR0_PID11_TDES_Pos))
#define SAIC_IPR0_PID12_SHA_Pos               (12U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID12_SHA_Msk               (0x1U << SAIC_IPR0_PID12_SHA_Pos)              /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID12_SHA(value)            (SAIC_IPR0_PID12_SHA_Msk & ((value) << SAIC_IPR0_PID12_SHA_Pos))
#define SAIC_IPR0_PID13_MPDDRC_Pos            (13U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID13_MPDDRC_Msk            (0x1U << SAIC_IPR0_PID13_MPDDRC_Pos)           /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID13_MPDDRC(value)         (SAIC_IPR0_PID13_MPDDRC_Msk & ((value) << SAIC_IPR0_PID13_MPDDRC_Pos))
#define SAIC_IPR0_PID14_MATRIX1_Pos           (14U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID14_MATRIX1_Msk           (0x1U << SAIC_IPR0_PID14_MATRIX1_Pos)          /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID14_MATRIX1(value)        (SAIC_IPR0_PID14_MATRIX1_Msk & ((value) << SAIC_IPR0_PID14_MATRIX1_Pos))
#define SAIC_IPR0_PID15_MATRIX0_Pos           (15U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID15_MATRIX0_Msk           (0x1U << SAIC_IPR0_PID15_MATRIX0_Pos)          /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID15_MATRIX0(value)        (SAIC_IPR0_PID15_MATRIX0_Msk & ((value) << SAIC_IPR0_PID15_MATRIX0_Pos))
#define SAIC_IPR0_PID16_SECUMOD_Pos           (16U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID16_SECUMOD_Msk           (0x1U << SAIC_IPR0_PID16_SECUMOD_Pos)          /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID16_SECUMOD(value)        (SAIC_IPR0_PID16_SECUMOD_Msk & ((value) << SAIC_IPR0_PID16_SECUMOD_Pos))
#define SAIC_IPR0_PID17_HSMC_Pos              (17U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID17_HSMC_Msk              (0x1U << SAIC_IPR0_PID17_HSMC_Pos)             /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID17_HSMC(value)           (SAIC_IPR0_PID17_HSMC_Msk & ((value) << SAIC_IPR0_PID17_HSMC_Pos))
#define SAIC_IPR0_PID18_PIOA_Pos              (18U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID18_PIOA_Msk              (0x1U << SAIC_IPR0_PID18_PIOA_Pos)             /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID18_PIOA(value)           (SAIC_IPR0_PID18_PIOA_Msk & ((value) << SAIC_IPR0_PID18_PIOA_Pos))
#define SAIC_IPR0_PID19_FLEXCOM0_Pos          (19U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID19_FLEXCOM0_Msk          (0x1U << SAIC_IPR0_PID19_FLEXCOM0_Pos)         /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID19_FLEXCOM0(value)       (SAIC_IPR0_PID19_FLEXCOM0_Msk & ((value) << SAIC_IPR0_PID19_FLEXCOM0_Pos))
#define SAIC_IPR0_PID20_FLEXCOM1_Pos          (20U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID20_FLEXCOM1_Msk          (0x1U << SAIC_IPR0_PID20_FLEXCOM1_Pos)         /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID20_FLEXCOM1(value)       (SAIC_IPR0_PID20_FLEXCOM1_Msk & ((value) << SAIC_IPR0_PID20_FLEXCOM1_Pos))
#define SAIC_IPR0_PID22_FLEXCOM3_Pos          (22U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID22_FLEXCOM3_Msk          (0x1U << SAIC_IPR0_PID22_FLEXCOM3_Pos)         /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID22_FLEXCOM3(value)       (SAIC_IPR0_PID22_FLEXCOM3_Msk & ((value) << SAIC_IPR0_PID22_FLEXCOM3_Pos))
#define SAIC_IPR0_PID23_FLEXCOM4_Pos          (23U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID23_FLEXCOM4_Msk          (0x1U << SAIC_IPR0_PID23_FLEXCOM4_Pos)         /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID23_FLEXCOM4(value)       (SAIC_IPR0_PID23_FLEXCOM4_Msk & ((value) << SAIC_IPR0_PID23_FLEXCOM4_Pos))
#define SAIC_IPR0_PID24_UART0_Pos             (24U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID24_UART0_Msk             (0x1U << SAIC_IPR0_PID24_UART0_Pos)            /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID24_UART0(value)          (SAIC_IPR0_PID24_UART0_Msk & ((value) << SAIC_IPR0_PID24_UART0_Pos))
#define SAIC_IPR0_PID25_UART1_Pos             (25U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID25_UART1_Msk             (0x1U << SAIC_IPR0_PID25_UART1_Pos)            /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID25_UART1(value)          (SAIC_IPR0_PID25_UART1_Msk & ((value) << SAIC_IPR0_PID25_UART1_Pos))
#define SAIC_IPR0_PID26_UART2_Pos             (26U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID26_UART2_Msk             (0x1U << SAIC_IPR0_PID26_UART2_Pos)            /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID26_UART2(value)          (SAIC_IPR0_PID26_UART2_Msk & ((value) << SAIC_IPR0_PID26_UART2_Pos))
#define SAIC_IPR0_PID27_UART3_Pos             (27U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID27_UART3_Msk             (0x1U << SAIC_IPR0_PID27_UART3_Pos)            /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID27_UART3(value)          (SAIC_IPR0_PID27_UART3_Msk & ((value) << SAIC_IPR0_PID27_UART3_Pos))
#define SAIC_IPR0_PID28_UART4_Pos             (28U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID28_UART4_Msk             (0x1U << SAIC_IPR0_PID28_UART4_Pos)            /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID28_UART4(value)          (SAIC_IPR0_PID28_UART4_Msk & ((value) << SAIC_IPR0_PID28_UART4_Pos))
#define SAIC_IPR0_PID29_TWIHS0_Pos            (29U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID29_TWIHS0_Msk            (0x1U << SAIC_IPR0_PID29_TWIHS0_Pos)           /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID29_TWIHS0(value)         (SAIC_IPR0_PID29_TWIHS0_Msk & ((value) << SAIC_IPR0_PID29_TWIHS0_Pos))
#define SAIC_IPR0_PID30_TWIHS1_Pos            (30U)                                          /**< (SAIC_IPR0) Interrupt Pending Position */
#define SAIC_IPR0_PID30_TWIHS1_Msk            (0x1U << SAIC_IPR0_PID30_TWIHS1_Pos)           /**< (SAIC_IPR0) Interrupt Pending Mask */
#define SAIC_IPR0_PID30_TWIHS1(value)         (SAIC_IPR0_PID30_TWIHS1_Msk & ((value) << SAIC_IPR0_PID30_TWIHS1_Pos))
#define SAIC_IPR0_Msk                         (0x7FDFFFFDUL)                                 /**< (SAIC_IPR0) Register Mask  */

/* -------- SAIC_IPR1 : (SAIC Offset: 0x24) (R/  32) Interrupt Pending Register 1 -------- */
#define SAIC_IPR1_PID32_SDMMC1_Pos            (0U)                                           /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID32_SDMMC1_Msk            (0x1U << SAIC_IPR1_PID32_SDMMC1_Pos)           /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID32_SDMMC1(value)         (SAIC_IPR1_PID32_SDMMC1_Msk & ((value) << SAIC_IPR1_PID32_SDMMC1_Pos))
#define SAIC_IPR1_PID33_SPI0_Pos              (1U)                                           /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID33_SPI0_Msk              (0x1U << SAIC_IPR1_PID33_SPI0_Pos)             /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID33_SPI0(value)           (SAIC_IPR1_PID33_SPI0_Msk & ((value) << SAIC_IPR1_PID33_SPI0_Pos))
#define SAIC_IPR1_PID34_SPI1_Pos              (2U)                                           /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID34_SPI1_Msk              (0x1U << SAIC_IPR1_PID34_SPI1_Pos)             /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID34_SPI1(value)           (SAIC_IPR1_PID34_SPI1_Msk & ((value) << SAIC_IPR1_PID34_SPI1_Pos))
#define SAIC_IPR1_PID35_TC0_Pos               (3U)                                           /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID35_TC0_Msk               (0x1U << SAIC_IPR1_PID35_TC0_Pos)              /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID35_TC0(value)            (SAIC_IPR1_PID35_TC0_Msk & ((value) << SAIC_IPR1_PID35_TC0_Pos))
#define SAIC_IPR1_PID36_TC1_Pos               (4U)                                           /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID36_TC1_Msk               (0x1U << SAIC_IPR1_PID36_TC1_Pos)              /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID36_TC1(value)            (SAIC_IPR1_PID36_TC1_Msk & ((value) << SAIC_IPR1_PID36_TC1_Pos))
#define SAIC_IPR1_PID38_PWM_Pos               (6U)                                           /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID38_PWM_Msk               (0x1U << SAIC_IPR1_PID38_PWM_Pos)              /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID38_PWM(value)            (SAIC_IPR1_PID38_PWM_Msk & ((value) << SAIC_IPR1_PID38_PWM_Pos))
#define SAIC_IPR1_PID40_ADC_Pos               (8U)                                           /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID40_ADC_Msk               (0x1U << SAIC_IPR1_PID40_ADC_Pos)              /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID40_ADC(value)            (SAIC_IPR1_PID40_ADC_Msk & ((value) << SAIC_IPR1_PID40_ADC_Pos))
#define SAIC_IPR1_PID41_UHPHS_Pos             (9U)                                           /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID41_UHPHS_Msk             (0x1U << SAIC_IPR1_PID41_UHPHS_Pos)            /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID41_UHPHS(value)          (SAIC_IPR1_PID41_UHPHS_Msk & ((value) << SAIC_IPR1_PID41_UHPHS_Pos))
#define SAIC_IPR1_PID42_UDPHS_Pos             (10U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID42_UDPHS_Msk             (0x1U << SAIC_IPR1_PID42_UDPHS_Pos)            /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID42_UDPHS(value)          (SAIC_IPR1_PID42_UDPHS_Msk & ((value) << SAIC_IPR1_PID42_UDPHS_Pos))
#define SAIC_IPR1_PID43_SSC0_Pos              (11U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID43_SSC0_Msk              (0x1U << SAIC_IPR1_PID43_SSC0_Pos)             /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID43_SSC0(value)           (SAIC_IPR1_PID43_SSC0_Msk & ((value) << SAIC_IPR1_PID43_SSC0_Pos))
#define SAIC_IPR1_PID44_SSC1_Pos              (12U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID44_SSC1_Msk              (0x1U << SAIC_IPR1_PID44_SSC1_Pos)             /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID44_SSC1(value)           (SAIC_IPR1_PID44_SSC1_Msk & ((value) << SAIC_IPR1_PID44_SSC1_Pos))
#define SAIC_IPR1_PID45_LCDC_Pos              (13U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID45_LCDC_Msk              (0x1U << SAIC_IPR1_PID45_LCDC_Pos)             /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID45_LCDC(value)           (SAIC_IPR1_PID45_LCDC_Msk & ((value) << SAIC_IPR1_PID45_LCDC_Pos))
#define SAIC_IPR1_PID46_ISC_Pos               (14U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID46_ISC_Msk               (0x1U << SAIC_IPR1_PID46_ISC_Pos)              /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID46_ISC(value)            (SAIC_IPR1_PID46_ISC_Msk & ((value) << SAIC_IPR1_PID46_ISC_Pos))
#define SAIC_IPR1_PID47_TRNG_Pos              (15U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID47_TRNG_Msk              (0x1U << SAIC_IPR1_PID47_TRNG_Pos)             /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID47_TRNG(value)           (SAIC_IPR1_PID47_TRNG_Msk & ((value) << SAIC_IPR1_PID47_TRNG_Pos))
#define SAIC_IPR1_PID48_PDMIC_Pos             (16U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID48_PDMIC_Msk             (0x1U << SAIC_IPR1_PID48_PDMIC_Pos)            /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID48_PDMIC(value)          (SAIC_IPR1_PID48_PDMIC_Msk & ((value) << SAIC_IPR1_PID48_PDMIC_Pos))
#define SAIC_IPR1_PID50_SFC_Pos               (18U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID50_SFC_Msk               (0x1U << SAIC_IPR1_PID50_SFC_Pos)              /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID50_SFC(value)            (SAIC_IPR1_PID50_SFC_Msk & ((value) << SAIC_IPR1_PID50_SFC_Pos))
#define SAIC_IPR1_PID51_SECURAM_Pos           (19U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID51_SECURAM_Msk           (0x1U << SAIC_IPR1_PID51_SECURAM_Pos)          /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID51_SECURAM(value)        (SAIC_IPR1_PID51_SECURAM_Msk & ((value) << SAIC_IPR1_PID51_SECURAM_Pos))
#define SAIC_IPR1_PID52_QSPI0_Pos             (20U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID52_QSPI0_Msk             (0x1U << SAIC_IPR1_PID52_QSPI0_Pos)            /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID52_QSPI0(value)          (SAIC_IPR1_PID52_QSPI0_Msk & ((value) << SAIC_IPR1_PID52_QSPI0_Pos))
#define SAIC_IPR1_PID53_QSPI1_Pos             (21U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID53_QSPI1_Msk             (0x1U << SAIC_IPR1_PID53_QSPI1_Pos)            /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID53_QSPI1(value)          (SAIC_IPR1_PID53_QSPI1_Msk & ((value) << SAIC_IPR1_PID53_QSPI1_Pos))
#define SAIC_IPR1_PID54_I2SC0_Pos             (22U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID54_I2SC0_Msk             (0x1U << SAIC_IPR1_PID54_I2SC0_Pos)            /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID54_I2SC0(value)          (SAIC_IPR1_PID54_I2SC0_Msk & ((value) << SAIC_IPR1_PID54_I2SC0_Pos))
#define SAIC_IPR1_PID55_I2SC1_Pos             (23U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID55_I2SC1_Msk             (0x1U << SAIC_IPR1_PID55_I2SC1_Pos)            /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID55_I2SC1(value)          (SAIC_IPR1_PID55_I2SC1_Msk & ((value) << SAIC_IPR1_PID55_I2SC1_Pos))
#define SAIC_IPR1_PID56_MCAN0_Pos             (24U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID56_MCAN0_Msk             (0x1U << SAIC_IPR1_PID56_MCAN0_Pos)            /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID56_MCAN0(value)          (SAIC_IPR1_PID56_MCAN0_Msk & ((value) << SAIC_IPR1_PID56_MCAN0_Pos))
#define SAIC_IPR1_PID58_PTC_Pos               (26U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID58_PTC_Msk               (0x1U << SAIC_IPR1_PID58_PTC_Pos)              /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID58_PTC(value)            (SAIC_IPR1_PID58_PTC_Msk & ((value) << SAIC_IPR1_PID58_PTC_Pos))
#define SAIC_IPR1_PID59_CLASSD_Pos            (27U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID59_CLASSD_Msk            (0x1U << SAIC_IPR1_PID59_CLASSD_Pos)           /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID59_CLASSD(value)         (SAIC_IPR1_PID59_CLASSD_Msk & ((value) << SAIC_IPR1_PID59_CLASSD_Pos))
#define SAIC_IPR1_PID63_L2CC_Pos              (31U)                                          /**< (SAIC_IPR1) Interrupt Pending Position */
#define SAIC_IPR1_PID63_L2CC_Msk              (0x1U << SAIC_IPR1_PID63_L2CC_Pos)             /**< (SAIC_IPR1) Interrupt Pending Mask */
#define SAIC_IPR1_PID63_L2CC(value)           (SAIC_IPR1_PID63_L2CC_Msk & ((value) << SAIC_IPR1_PID63_L2CC_Pos))
#define SAIC_IPR1_Msk                         (0x8DFDFF5FUL)                                 /**< (SAIC_IPR1) Register Mask  */

/* -------- SAIC_IPR2 : (SAIC Offset: 0x28) (R/  32) Interrupt Pending Register 2 -------- */
#define SAIC_IPR2_PID64_MCAN0_INT1_Pos        (0U)                                           /**< (SAIC_IPR2) Interrupt Pending Position */
#define SAIC_IPR2_PID64_MCAN0_INT1_Msk        (0x1U << SAIC_IPR2_PID64_MCAN0_INT1_Pos)       /**< (SAIC_IPR2) Interrupt Pending Mask */
#define SAIC_IPR2_PID64_MCAN0_INT1(value)     (SAIC_IPR2_PID64_MCAN0_INT1_Msk & ((value) << SAIC_IPR2_PID64_MCAN0_INT1_Pos))
#define SAIC_IPR2_PID66_GMAC_Q1_Pos           (2U)                                           /**< (SAIC_IPR2) Interrupt Pending Position */
#define SAIC_IPR2_PID66_GMAC_Q1_Msk           (0x1U << SAIC_IPR2_PID66_GMAC_Q1_Pos)          /**< (SAIC_IPR2) Interrupt Pending Mask */
#define SAIC_IPR2_PID66_GMAC_Q1(value)        (SAIC_IPR2_PID66_GMAC_Q1_Msk & ((value) << SAIC_IPR2_PID66_GMAC_Q1_Pos))
#define SAIC_IPR2_PID67_GMAC_Q2_Pos           (3U)                                           /**< (SAIC_IPR2) Interrupt Pending Position */
#define SAIC_IPR2_PID67_GMAC_Q2_Msk           (0x1U << SAIC_IPR2_PID67_GMAC_Q2_Pos)          /**< (SAIC_IPR2) Interrupt Pending Mask */
#define SAIC_IPR2_PID67_GMAC_Q2(value)        (SAIC_IPR2_PID67_GMAC_Q2_Msk & ((value) << SAIC_IPR2_PID67_GMAC_Q2_Pos))
#define SAIC_IPR2_PID68_PIOB_Pos              (4U)                                           /**< (SAIC_IPR2) Interrupt Pending Position */
#define SAIC_IPR2_PID68_PIOB_Msk              (0x1U << SAIC_IPR2_PID68_PIOB_Pos)             /**< (SAIC_IPR2) Interrupt Pending Mask */
#define SAIC_IPR2_PID68_PIOB(value)           (SAIC_IPR2_PID68_PIOB_Msk & ((value) << SAIC_IPR2_PID68_PIOB_Pos))
#define SAIC_IPR2_PID69_PIOC_Pos              (5U)                                           /**< (SAIC_IPR2) Interrupt Pending Position */
#define SAIC_IPR2_PID69_PIOC_Msk              (0x1U << SAIC_IPR2_PID69_PIOC_Pos)             /**< (SAIC_IPR2) Interrupt Pending Mask */
#define SAIC_IPR2_PID69_PIOC(value)           (SAIC_IPR2_PID69_PIOC_Msk & ((value) << SAIC_IPR2_PID69_PIOC_Pos))
#define SAIC_IPR2_PID70_PIOD_Pos              (6U)                                           /**< (SAIC_IPR2) Interrupt Pending Position */
#define SAIC_IPR2_PID70_PIOD_Msk              (0x1U << SAIC_IPR2_PID70_PIOD_Pos)             /**< (SAIC_IPR2) Interrupt Pending Mask */
#define SAIC_IPR2_PID70_PIOD(value)           (SAIC_IPR2_PID70_PIOD_Msk & ((value) << SAIC_IPR2_PID70_PIOD_Pos))
#define SAIC_IPR2_PID72_SDMMC1_TIMER_Pos      (8U)                                           /**< (SAIC_IPR2) Interrupt Pending Position */
#define SAIC_IPR2_PID72_SDMMC1_TIMER_Msk      (0x1U << SAIC_IPR2_PID72_SDMMC1_TIMER_Pos)     /**< (SAIC_IPR2) Interrupt Pending Mask */
#define SAIC_IPR2_PID72_SDMMC1_TIMER(value)   (SAIC_IPR2_PID72_SDMMC1_TIMER_Msk & ((value) << SAIC_IPR2_PID72_SDMMC1_TIMER_Pos))
#define SAIC_IPR2_PID74_SYSC_Pos              (10U)                                          /**< (SAIC_IPR2) Interrupt Pending Position */
#define SAIC_IPR2_PID74_SYSC_Msk              (0x1U << SAIC_IPR2_PID74_SYSC_Pos)             /**< (SAIC_IPR2) Interrupt Pending Mask */
#define SAIC_IPR2_PID74_SYSC(value)           (SAIC_IPR2_PID74_SYSC_Msk & ((value) << SAIC_IPR2_PID74_SYSC_Pos))
#define SAIC_IPR2_PID75_ACC_Pos               (11U)                                          /**< (SAIC_IPR2) Interrupt Pending Position */
#define SAIC_IPR2_PID75_ACC_Msk               (0x1U << SAIC_IPR2_PID75_ACC_Pos)              /**< (SAIC_IPR2) Interrupt Pending Mask */
#define SAIC_IPR2_PID75_ACC(value)            (SAIC_IPR2_PID75_ACC_Msk & ((value) << SAIC_IPR2_PID75_ACC_Pos))
#define SAIC_IPR2_PID76_RXLP_Pos              (12U)                                          /**< (SAIC_IPR2) Interrupt Pending Position */
#define SAIC_IPR2_PID76_RXLP_Msk              (0x1U << SAIC_IPR2_PID76_RXLP_Pos)             /**< (SAIC_IPR2) Interrupt Pending Mask */
#define SAIC_IPR2_PID76_RXLP(value)           (SAIC_IPR2_PID76_RXLP_Msk & ((value) << SAIC_IPR2_PID76_RXLP_Pos))
#define SAIC_IPR2_Msk                         (0x00001D7DUL)                                 /**< (SAIC_IPR2) Register Mask  */

/* -------- SAIC_IMR : (SAIC Offset: 0x30) (R/  32) Interrupt Mask Register -------- */
#define SAIC_IMR_INTM_Pos                     (0U)                                           /**< (SAIC_IMR) Interrupt Mask Position */
#define SAIC_IMR_INTM_Msk                     (0x1U << SAIC_IMR_INTM_Pos)                    /**< (SAIC_IMR) Interrupt Mask Mask */
#define SAIC_IMR_INTM(value)                  (SAIC_IMR_INTM_Msk & ((value) << SAIC_IMR_INTM_Pos))
#define SAIC_IMR_Msk                          (0x00000001UL)                                 /**< (SAIC_IMR) Register Mask  */

/* -------- SAIC_CISR : (SAIC Offset: 0x34) (R/  32) Core Interrupt Status Register -------- */
#define SAIC_CISR_NFIQ_Pos                    (0U)                                           /**< (SAIC_CISR) NFIQ Status Position */
#define SAIC_CISR_NFIQ_Msk                    (0x1U << SAIC_CISR_NFIQ_Pos)                   /**< (SAIC_CISR) NFIQ Status Mask */
#define SAIC_CISR_NFIQ(value)                 (SAIC_CISR_NFIQ_Msk & ((value) << SAIC_CISR_NFIQ_Pos))
#define SAIC_CISR_NIRQ_Pos                    (1U)                                           /**< (SAIC_CISR) NIRQ Status Position */
#define SAIC_CISR_NIRQ_Msk                    (0x1U << SAIC_CISR_NIRQ_Pos)                   /**< (SAIC_CISR) NIRQ Status Mask */
#define SAIC_CISR_NIRQ(value)                 (SAIC_CISR_NIRQ_Msk & ((value) << SAIC_CISR_NIRQ_Pos))
#define SAIC_CISR_Msk                         (0x00000003UL)                                 /**< (SAIC_CISR) Register Mask  */

/* -------- SAIC_EOICR : (SAIC Offset: 0x38) ( /W 32) End of Interrupt Command Register -------- */
#define SAIC_EOICR_ENDIT_Pos                  (0U)                                           /**< (SAIC_EOICR) Interrupt Processing Complete Command Position */
#define SAIC_EOICR_ENDIT_Msk                  (0x1U << SAIC_EOICR_ENDIT_Pos)                 /**< (SAIC_EOICR) Interrupt Processing Complete Command Mask */
#define SAIC_EOICR_ENDIT(value)               (SAIC_EOICR_ENDIT_Msk & ((value) << SAIC_EOICR_ENDIT_Pos))
#define SAIC_EOICR_Msk                        (0x00000001UL)                                 /**< (SAIC_EOICR) Register Mask  */

/* -------- SAIC_SPU : (SAIC Offset: 0x3C) (R/W 32) Spurious Interrupt Vector Register -------- */
#define SAIC_SPU_SIVR_Pos                     (0U)                                           /**< (SAIC_SPU) Spurious Interrupt Vector Register Position */
#define SAIC_SPU_SIVR_Msk                     (0xFFFFFFFFU << SAIC_SPU_SIVR_Pos)             /**< (SAIC_SPU) Spurious Interrupt Vector Register Mask */
#define SAIC_SPU_SIVR(value)                  (SAIC_SPU_SIVR_Msk & ((value) << SAIC_SPU_SIVR_Pos))
#define SAIC_SPU_Msk                          (0xFFFFFFFFUL)                                 /**< (SAIC_SPU) Register Mask  */

/* -------- SAIC_IECR : (SAIC Offset: 0x40) ( /W 32) Interrupt Enable Command Register -------- */
#define SAIC_IECR_INTEN_Pos                   (0U)                                           /**< (SAIC_IECR) Interrupt Enable Position */
#define SAIC_IECR_INTEN_Msk                   (0x1U << SAIC_IECR_INTEN_Pos)                  /**< (SAIC_IECR) Interrupt Enable Mask */
#define SAIC_IECR_INTEN(value)                (SAIC_IECR_INTEN_Msk & ((value) << SAIC_IECR_INTEN_Pos))
#define SAIC_IECR_Msk                         (0x00000001UL)                                 /**< (SAIC_IECR) Register Mask  */

/* -------- SAIC_IDCR : (SAIC Offset: 0x44) ( /W 32) Interrupt Disable Command Register -------- */
#define SAIC_IDCR_INTD_Pos                    (0U)                                           /**< (SAIC_IDCR) Interrupt Disable Position */
#define SAIC_IDCR_INTD_Msk                    (0x1U << SAIC_IDCR_INTD_Pos)                   /**< (SAIC_IDCR) Interrupt Disable Mask */
#define SAIC_IDCR_INTD(value)                 (SAIC_IDCR_INTD_Msk & ((value) << SAIC_IDCR_INTD_Pos))
#define SAIC_IDCR_Msk                         (0x00000001UL)                                 /**< (SAIC_IDCR) Register Mask  */

/* -------- SAIC_ICCR : (SAIC Offset: 0x48) ( /W 32) Interrupt Clear Command Register -------- */
#define SAIC_ICCR_INTCLR_Pos                  (0U)                                           /**< (SAIC_ICCR) Interrupt Clear Position */
#define SAIC_ICCR_INTCLR_Msk                  (0x1U << SAIC_ICCR_INTCLR_Pos)                 /**< (SAIC_ICCR) Interrupt Clear Mask */
#define SAIC_ICCR_INTCLR(value)               (SAIC_ICCR_INTCLR_Msk & ((value) << SAIC_ICCR_INTCLR_Pos))
#define SAIC_ICCR_Msk                         (0x00000001UL)                                 /**< (SAIC_ICCR) Register Mask  */

/* -------- SAIC_ISCR : (SAIC Offset: 0x4C) ( /W 32) Interrupt Set Command Register -------- */
#define SAIC_ISCR_INTSET_Pos                  (0U)                                           /**< (SAIC_ISCR) Interrupt Set Position */
#define SAIC_ISCR_INTSET_Msk                  (0x1U << SAIC_ISCR_INTSET_Pos)                 /**< (SAIC_ISCR) Interrupt Set Mask */
#define SAIC_ISCR_INTSET(value)               (SAIC_ISCR_INTSET_Msk & ((value) << SAIC_ISCR_INTSET_Pos))
#define SAIC_ISCR_Msk                         (0x00000001UL)                                 /**< (SAIC_ISCR) Register Mask  */

/* -------- SAIC_DCR : (SAIC Offset: 0x6C) (R/W 32) Debug Control Register -------- */
#define SAIC_DCR_PROT_Pos                     (0U)                                           /**< (SAIC_DCR) Protection Mode Position */
#define SAIC_DCR_PROT_Msk                     (0x1U << SAIC_DCR_PROT_Pos)                    /**< (SAIC_DCR) Protection Mode Mask */
#define SAIC_DCR_PROT(value)                  (SAIC_DCR_PROT_Msk & ((value) << SAIC_DCR_PROT_Pos))
#define SAIC_DCR_GMSK_Pos                     (1U)                                           /**< (SAIC_DCR) General Interrupt Mask Position */
#define SAIC_DCR_GMSK_Msk                     (0x1U << SAIC_DCR_GMSK_Pos)                    /**< (SAIC_DCR) General Interrupt Mask Mask */
#define SAIC_DCR_GMSK(value)                  (SAIC_DCR_GMSK_Msk & ((value) << SAIC_DCR_GMSK_Pos))
#define SAIC_DCR_Msk                          (0x00000003UL)                                 /**< (SAIC_DCR) Register Mask  */

/* -------- SAIC_WPMR : (SAIC Offset: 0xE4) (R/W 32) Write Protection Mode Register -------- */
#define SAIC_WPMR_WPEN_Pos                    (0U)                                           /**< (SAIC_WPMR) Write Protection Enable Position */
#define SAIC_WPMR_WPEN_Msk                    (0x1U << SAIC_WPMR_WPEN_Pos)                   /**< (SAIC_WPMR) Write Protection Enable Mask */
#define SAIC_WPMR_WPEN(value)                 (SAIC_WPMR_WPEN_Msk & ((value) << SAIC_WPMR_WPEN_Pos))
#define SAIC_WPMR_WPKEY_Pos                   (8U)                                           /**< (SAIC_WPMR) Write Protection Key Position */
#define SAIC_WPMR_WPKEY_Msk                   (0xFFFFFFU << SAIC_WPMR_WPKEY_Pos)             /**< (SAIC_WPMR) Write Protection Key Mask */
#define SAIC_WPMR_WPKEY(value)                (SAIC_WPMR_WPKEY_Msk & ((value) << SAIC_WPMR_WPKEY_Pos))
#define   SAIC_WPMR_WPKEY_PASSWD_Val          (4278595U)                                     /**< (SAIC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0.  */
#define SAIC_WPMR_WPKEY_PASSWD                (SAIC_WPMR_WPKEY_PASSWD_Val << SAIC_WPMR_WPKEY_Pos) /**< (SAIC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0. Position  */
#define SAIC_WPMR_Msk                         (0xFFFFFF01UL)                                 /**< (SAIC_WPMR) Register Mask  */

/* -------- SAIC_WPSR : (SAIC Offset: 0xE8) (R/  32) Write Protection Status Register -------- */
#define SAIC_WPSR_WPVS_Pos                    (0U)                                           /**< (SAIC_WPSR) Write Protection Violation Status Position */
#define SAIC_WPSR_WPVS_Msk                    (0x1U << SAIC_WPSR_WPVS_Pos)                   /**< (SAIC_WPSR) Write Protection Violation Status Mask */
#define SAIC_WPSR_WPVS(value)                 (SAIC_WPSR_WPVS_Msk & ((value) << SAIC_WPSR_WPVS_Pos))
#define SAIC_WPSR_WPVSRC_Pos                  (8U)                                           /**< (SAIC_WPSR) Write Protection Violation Source Position */
#define SAIC_WPSR_WPVSRC_Msk                  (0xFFFFU << SAIC_WPSR_WPVSRC_Pos)              /**< (SAIC_WPSR) Write Protection Violation Source Mask */
#define SAIC_WPSR_WPVSRC(value)               (SAIC_WPSR_WPVSRC_Msk & ((value) << SAIC_WPSR_WPVSRC_Pos))
#define SAIC_WPSR_Msk                         (0x00FFFF01UL)                                 /**< (SAIC_WPSR) Register Mask  */

/* -------- SAIC_VERSION : (SAIC Offset: 0xFC) (R/  32) AIC Version Register -------- */
#define SAIC_VERSION_VERSION_Pos              (0U)                                           /**< (SAIC_VERSION) Version of the Hardware Module Position */
#define SAIC_VERSION_VERSION_Msk              (0xFFFU << SAIC_VERSION_VERSION_Pos)           /**< (SAIC_VERSION) Version of the Hardware Module Mask */
#define SAIC_VERSION_VERSION(value)           (SAIC_VERSION_VERSION_Msk & ((value) << SAIC_VERSION_VERSION_Pos))
#define SAIC_VERSION_MFN_Pos                  (16U)                                          /**< (SAIC_VERSION) Metal Fix Number Position */
#define SAIC_VERSION_MFN_Msk                  (0x7U << SAIC_VERSION_MFN_Pos)                 /**< (SAIC_VERSION) Metal Fix Number Mask */
#define SAIC_VERSION_MFN(value)               (SAIC_VERSION_MFN_Msk & ((value) << SAIC_VERSION_MFN_Pos))
#define SAIC_VERSION_Msk                      (0x00070FFFUL)                                 /**< (SAIC_VERSION) Register Mask  */

/** \brief SAIC register offsets definitions */
#define SAIC_SSR_OFFSET                (0x00)         /**< (SAIC_SSR) Source Select Register Offset */
#define SAIC_SMR_OFFSET                (0x04)         /**< (SAIC_SMR) Source Mode Register Offset */
#define SAIC_SVR_OFFSET                (0x08)         /**< (SAIC_SVR) Source Vector Register Offset */
#define SAIC_IVR_OFFSET                (0x10)         /**< (SAIC_IVR) Interrupt Vector Register Offset */
#define SAIC_FVR_OFFSET                (0x14)         /**< (SAIC_FVR) FIQ Vector Register Offset */
#define SAIC_ISR_OFFSET                (0x18)         /**< (SAIC_ISR) Interrupt Status Register Offset */
#define SAIC_IPR0_OFFSET               (0x20)         /**< (SAIC_IPR0) Interrupt Pending Register 0 Offset */
#define SAIC_IPR1_OFFSET               (0x24)         /**< (SAIC_IPR1) Interrupt Pending Register 1 Offset */
#define SAIC_IPR2_OFFSET               (0x28)         /**< (SAIC_IPR2) Interrupt Pending Register 2 Offset */
#define SAIC_IMR_OFFSET                (0x30)         /**< (SAIC_IMR) Interrupt Mask Register Offset */
#define SAIC_CISR_OFFSET               (0x34)         /**< (SAIC_CISR) Core Interrupt Status Register Offset */
#define SAIC_EOICR_OFFSET              (0x38)         /**< (SAIC_EOICR) End of Interrupt Command Register Offset */
#define SAIC_SPU_OFFSET                (0x3C)         /**< (SAIC_SPU) Spurious Interrupt Vector Register Offset */
#define SAIC_IECR_OFFSET               (0x40)         /**< (SAIC_IECR) Interrupt Enable Command Register Offset */
#define SAIC_IDCR_OFFSET               (0x44)         /**< (SAIC_IDCR) Interrupt Disable Command Register Offset */
#define SAIC_ICCR_OFFSET               (0x48)         /**< (SAIC_ICCR) Interrupt Clear Command Register Offset */
#define SAIC_ISCR_OFFSET               (0x4C)         /**< (SAIC_ISCR) Interrupt Set Command Register Offset */
#define SAIC_DCR_OFFSET                (0x6C)         /**< (SAIC_DCR) Debug Control Register Offset */
#define SAIC_WPMR_OFFSET               (0xE4)         /**< (SAIC_WPMR) Write Protection Mode Register Offset */
#define SAIC_WPSR_OFFSET               (0xE8)         /**< (SAIC_WPSR) Write Protection Status Register Offset */
#define SAIC_VERSION_OFFSET            (0xFC)         /**< (SAIC_VERSION) AIC Version Register Offset */

/** \brief SAIC register API structure */
typedef struct
{
  __IO  uint32_t                       SAIC_SSR;        /**< Offset: 0x00 (R/W  32) Source Select Register */
  __IO  uint32_t                       SAIC_SMR;        /**< Offset: 0x04 (R/W  32) Source Mode Register */
  __IO  uint32_t                       SAIC_SVR;        /**< Offset: 0x08 (R/W  32) Source Vector Register */
  __I   uint8_t                        Reserved1[0x04];
  __I   uint32_t                       SAIC_IVR;        /**< Offset: 0x10 (R/   32) Interrupt Vector Register */
  __I   uint32_t                       SAIC_FVR;        /**< Offset: 0x14 (R/   32) FIQ Vector Register */
  __I   uint32_t                       SAIC_ISR;        /**< Offset: 0x18 (R/   32) Interrupt Status Register */
  __I   uint8_t                        Reserved2[0x04];
  __I   uint32_t                       SAIC_IPR0;       /**< Offset: 0x20 (R/   32) Interrupt Pending Register 0 */
  __I   uint32_t                       SAIC_IPR1;       /**< Offset: 0x24 (R/   32) Interrupt Pending Register 1 */
  __I   uint32_t                       SAIC_IPR2;       /**< Offset: 0x28 (R/   32) Interrupt Pending Register 2 */
  __I   uint8_t                        Reserved3[0x04];
  __I   uint32_t                       SAIC_IMR;        /**< Offset: 0x30 (R/   32) Interrupt Mask Register */
  __I   uint32_t                       SAIC_CISR;       /**< Offset: 0x34 (R/   32) Core Interrupt Status Register */
  __O   uint32_t                       SAIC_EOICR;      /**< Offset: 0x38 ( /W  32) End of Interrupt Command Register */
  __IO  uint32_t                       SAIC_SPU;        /**< Offset: 0x3c (R/W  32) Spurious Interrupt Vector Register */
  __O   uint32_t                       SAIC_IECR;       /**< Offset: 0x40 ( /W  32) Interrupt Enable Command Register */
  __O   uint32_t                       SAIC_IDCR;       /**< Offset: 0x44 ( /W  32) Interrupt Disable Command Register */
  __O   uint32_t                       SAIC_ICCR;       /**< Offset: 0x48 ( /W  32) Interrupt Clear Command Register */
  __O   uint32_t                       SAIC_ISCR;       /**< Offset: 0x4c ( /W  32) Interrupt Set Command Register */
  __I   uint8_t                        Reserved4[0x1C];
  __IO  uint32_t                       SAIC_DCR;        /**< Offset: 0x6c (R/W  32) Debug Control Register */
  __I   uint8_t                        Reserved5[0x74];
  __IO  uint32_t                       SAIC_WPMR;       /**< Offset: 0xe4 (R/W  32) Write Protection Mode Register */
  __I   uint32_t                       SAIC_WPSR;       /**< Offset: 0xe8 (R/   32) Write Protection Status Register */
  __I   uint8_t                        Reserved6[0x10];
  __I   uint32_t                       SAIC_VERSION;    /**< Offset: 0xfc (R/   32) AIC Version Register */
} saic_registers_t;
/** @}  end of Secure Advanced Interrupt Controller */

#endif /* SAMA5D2_SAMA5D2_SAIC_MODULE_H */

