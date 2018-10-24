/**
 * \brief Header file for SAMC/SAMC21 CAN
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
#ifndef SAMC_SAMC21_CAN_MODULE_H
#define SAMC_SAMC21_CAN_MODULE_H

/** \addtogroup SAMC_SAMC21 Control Area Network
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_CAN                                   */
/* ========================================================================== */

/* -------- CAN_CREL : (CAN Offset: 0x00) (R/  32) Core Release -------- */
#define CAN_CREL_SUBSTEP_Pos                  (20U)                                          /**< (CAN_CREL) Sub-step of Core Release Position */
#define CAN_CREL_SUBSTEP_Msk                  (0xFU << CAN_CREL_SUBSTEP_Pos)                 /**< (CAN_CREL) Sub-step of Core Release Mask */
#define CAN_CREL_SUBSTEP(value)               (CAN_CREL_SUBSTEP_Msk & ((value) << CAN_CREL_SUBSTEP_Pos))
#define CAN_CREL_STEP_Pos                     (24U)                                          /**< (CAN_CREL) Step of Core Release Position */
#define CAN_CREL_STEP_Msk                     (0xFU << CAN_CREL_STEP_Pos)                    /**< (CAN_CREL) Step of Core Release Mask */
#define CAN_CREL_STEP(value)                  (CAN_CREL_STEP_Msk & ((value) << CAN_CREL_STEP_Pos))
#define CAN_CREL_REL_Pos                      (28U)                                          /**< (CAN_CREL) Core Release Position */
#define CAN_CREL_REL_Msk                      (0xFU << CAN_CREL_REL_Pos)                     /**< (CAN_CREL) Core Release Mask */
#define CAN_CREL_REL(value)                   (CAN_CREL_REL_Msk & ((value) << CAN_CREL_REL_Pos))
#define CAN_CREL_Msk                          (0xFFF00000UL)                                 /**< (CAN_CREL) Register Mask  */

/* -------- CAN_ENDN : (CAN Offset: 0x04) (R/  32) Endian -------- */
#define CAN_ENDN_ETV_Pos                      (0U)                                           /**< (CAN_ENDN) Endianness Test Value Position */
#define CAN_ENDN_ETV_Msk                      (0xFFFFFFFFU << CAN_ENDN_ETV_Pos)              /**< (CAN_ENDN) Endianness Test Value Mask */
#define CAN_ENDN_ETV(value)                   (CAN_ENDN_ETV_Msk & ((value) << CAN_ENDN_ETV_Pos))
#define CAN_ENDN_Msk                          (0xFFFFFFFFUL)                                 /**< (CAN_ENDN) Register Mask  */

/* -------- CAN_MRCFG : (CAN Offset: 0x08) (R/W 32) Message RAM Configuration -------- */
#define CAN_MRCFG_QOS_Pos                     (0U)                                           /**< (CAN_MRCFG) Quality of Service Position */
#define CAN_MRCFG_QOS_Msk                     (0x3U << CAN_MRCFG_QOS_Pos)                    /**< (CAN_MRCFG) Quality of Service Mask */
#define CAN_MRCFG_QOS(value)                  (CAN_MRCFG_QOS_Msk & ((value) << CAN_MRCFG_QOS_Pos))
#define   CAN_MRCFG_QOS_DISABLE_Val           (0U)                                           /**< (CAN_MRCFG) Background (no sensitive operation)  */
#define   CAN_MRCFG_QOS_LOW_Val               (1U)                                           /**< (CAN_MRCFG) Sensitive Bandwidth  */
#define   CAN_MRCFG_QOS_MEDIUM_Val            (2U)                                           /**< (CAN_MRCFG) Sensitive Latency  */
#define   CAN_MRCFG_QOS_HIGH_Val              (3U)                                           /**< (CAN_MRCFG) Critical Latency  */
#define CAN_MRCFG_QOS_DISABLE                 (CAN_MRCFG_QOS_DISABLE_Val << CAN_MRCFG_QOS_Pos) /**< (CAN_MRCFG) Background (no sensitive operation) Position  */
#define CAN_MRCFG_QOS_LOW                     (CAN_MRCFG_QOS_LOW_Val << CAN_MRCFG_QOS_Pos)   /**< (CAN_MRCFG) Sensitive Bandwidth Position  */
#define CAN_MRCFG_QOS_MEDIUM                  (CAN_MRCFG_QOS_MEDIUM_Val << CAN_MRCFG_QOS_Pos) /**< (CAN_MRCFG) Sensitive Latency Position  */
#define CAN_MRCFG_QOS_HIGH                    (CAN_MRCFG_QOS_HIGH_Val << CAN_MRCFG_QOS_Pos)  /**< (CAN_MRCFG) Critical Latency Position  */
#define CAN_MRCFG_Msk                         (0x00000003UL)                                 /**< (CAN_MRCFG) Register Mask  */

/* -------- CAN_DBTP : (CAN Offset: 0x0C) (R/W 32) Fast Bit Timing and Prescaler -------- */
#define CAN_DBTP_DSJW_Pos                     (0U)                                           /**< (CAN_DBTP) Data (Re)Synchronization Jump Width Position */
#define CAN_DBTP_DSJW_Msk                     (0xFU << CAN_DBTP_DSJW_Pos)                    /**< (CAN_DBTP) Data (Re)Synchronization Jump Width Mask */
#define CAN_DBTP_DSJW(value)                  (CAN_DBTP_DSJW_Msk & ((value) << CAN_DBTP_DSJW_Pos))
#define CAN_DBTP_DTSEG2_Pos                   (4U)                                           /**< (CAN_DBTP) Data time segment after sample point Position */
#define CAN_DBTP_DTSEG2_Msk                   (0xFU << CAN_DBTP_DTSEG2_Pos)                  /**< (CAN_DBTP) Data time segment after sample point Mask */
#define CAN_DBTP_DTSEG2(value)                (CAN_DBTP_DTSEG2_Msk & ((value) << CAN_DBTP_DTSEG2_Pos))
#define CAN_DBTP_DTSEG1_Pos                   (8U)                                           /**< (CAN_DBTP) Data time segment before sample point Position */
#define CAN_DBTP_DTSEG1_Msk                   (0x1FU << CAN_DBTP_DTSEG1_Pos)                 /**< (CAN_DBTP) Data time segment before sample point Mask */
#define CAN_DBTP_DTSEG1(value)                (CAN_DBTP_DTSEG1_Msk & ((value) << CAN_DBTP_DTSEG1_Pos))
#define CAN_DBTP_DBRP_Pos                     (16U)                                          /**< (CAN_DBTP) Data Baud Rate Prescaler Position */
#define CAN_DBTP_DBRP_Msk                     (0x1FU << CAN_DBTP_DBRP_Pos)                   /**< (CAN_DBTP) Data Baud Rate Prescaler Mask */
#define CAN_DBTP_DBRP(value)                  (CAN_DBTP_DBRP_Msk & ((value) << CAN_DBTP_DBRP_Pos))
#define CAN_DBTP_TDC_Pos                      (23U)                                          /**< (CAN_DBTP) Tranceiver Delay Compensation Position */
#define CAN_DBTP_TDC_Msk                      (0x1U << CAN_DBTP_TDC_Pos)                     /**< (CAN_DBTP) Tranceiver Delay Compensation Mask */
#define CAN_DBTP_TDC(value)                   (CAN_DBTP_TDC_Msk & ((value) << CAN_DBTP_TDC_Pos))
#define CAN_DBTP_Msk                          (0x009F1FFFUL)                                 /**< (CAN_DBTP) Register Mask  */

/* -------- CAN_TEST : (CAN Offset: 0x10) (R/W 32) Test -------- */
#define CAN_TEST_LBCK_Pos                     (4U)                                           /**< (CAN_TEST) Loop Back Mode Position */
#define CAN_TEST_LBCK_Msk                     (0x1U << CAN_TEST_LBCK_Pos)                    /**< (CAN_TEST) Loop Back Mode Mask */
#define CAN_TEST_LBCK(value)                  (CAN_TEST_LBCK_Msk & ((value) << CAN_TEST_LBCK_Pos))
#define CAN_TEST_TX_Pos                       (5U)                                           /**< (CAN_TEST) Control of Transmit Pin Position */
#define CAN_TEST_TX_Msk                       (0x3U << CAN_TEST_TX_Pos)                      /**< (CAN_TEST) Control of Transmit Pin Mask */
#define CAN_TEST_TX(value)                    (CAN_TEST_TX_Msk & ((value) << CAN_TEST_TX_Pos))
#define   CAN_TEST_TX_CORE_Val                (0U)                                           /**< (CAN_TEST) TX controlled by CAN core  */
#define   CAN_TEST_TX_SAMPLE_Val              (1U)                                           /**< (CAN_TEST) TX monitoring sample point  */
#define   CAN_TEST_TX_DOMINANT_Val            (2U)                                           /**< (CAN_TEST) Dominant (0) level at pin CAN_TX  */
#define   CAN_TEST_TX_RECESSIVE_Val           (3U)                                           /**< (CAN_TEST) Recessive (1) level at pin CAN_TX  */
#define CAN_TEST_TX_CORE                      (CAN_TEST_TX_CORE_Val << CAN_TEST_TX_Pos)      /**< (CAN_TEST) TX controlled by CAN core Position  */
#define CAN_TEST_TX_SAMPLE                    (CAN_TEST_TX_SAMPLE_Val << CAN_TEST_TX_Pos)    /**< (CAN_TEST) TX monitoring sample point Position  */
#define CAN_TEST_TX_DOMINANT                  (CAN_TEST_TX_DOMINANT_Val << CAN_TEST_TX_Pos)  /**< (CAN_TEST) Dominant (0) level at pin CAN_TX Position  */
#define CAN_TEST_TX_RECESSIVE                 (CAN_TEST_TX_RECESSIVE_Val << CAN_TEST_TX_Pos) /**< (CAN_TEST) Recessive (1) level at pin CAN_TX Position  */
#define CAN_TEST_RX_Pos                       (7U)                                           /**< (CAN_TEST) Receive Pin Position */
#define CAN_TEST_RX_Msk                       (0x1U << CAN_TEST_RX_Pos)                      /**< (CAN_TEST) Receive Pin Mask */
#define CAN_TEST_RX(value)                    (CAN_TEST_RX_Msk & ((value) << CAN_TEST_RX_Pos))
#define CAN_TEST_Msk                          (0x000000F0UL)                                 /**< (CAN_TEST) Register Mask  */

/* -------- CAN_RWD : (CAN Offset: 0x14) (R/W 32) RAM Watchdog -------- */
#define CAN_RWD_WDC_Pos                       (0U)                                           /**< (CAN_RWD) Watchdog Configuration Position */
#define CAN_RWD_WDC_Msk                       (0xFFU << CAN_RWD_WDC_Pos)                     /**< (CAN_RWD) Watchdog Configuration Mask */
#define CAN_RWD_WDC(value)                    (CAN_RWD_WDC_Msk & ((value) << CAN_RWD_WDC_Pos))
#define CAN_RWD_WDV_Pos                       (8U)                                           /**< (CAN_RWD) Watchdog Value Position */
#define CAN_RWD_WDV_Msk                       (0xFFU << CAN_RWD_WDV_Pos)                     /**< (CAN_RWD) Watchdog Value Mask */
#define CAN_RWD_WDV(value)                    (CAN_RWD_WDV_Msk & ((value) << CAN_RWD_WDV_Pos))
#define CAN_RWD_Msk                           (0x0000FFFFUL)                                 /**< (CAN_RWD) Register Mask  */

/* -------- CAN_CCCR : (CAN Offset: 0x18) (R/W 32) CC Control -------- */
#define CAN_CCCR_INIT_Pos                     (0U)                                           /**< (CAN_CCCR) Initialization Position */
#define CAN_CCCR_INIT_Msk                     (0x1U << CAN_CCCR_INIT_Pos)                    /**< (CAN_CCCR) Initialization Mask */
#define CAN_CCCR_INIT(value)                  (CAN_CCCR_INIT_Msk & ((value) << CAN_CCCR_INIT_Pos))
#define CAN_CCCR_CCE_Pos                      (1U)                                           /**< (CAN_CCCR) Configuration Change Enable Position */
#define CAN_CCCR_CCE_Msk                      (0x1U << CAN_CCCR_CCE_Pos)                     /**< (CAN_CCCR) Configuration Change Enable Mask */
#define CAN_CCCR_CCE(value)                   (CAN_CCCR_CCE_Msk & ((value) << CAN_CCCR_CCE_Pos))
#define CAN_CCCR_ASM_Pos                      (2U)                                           /**< (CAN_CCCR) ASM Restricted Operation Mode Position */
#define CAN_CCCR_ASM_Msk                      (0x1U << CAN_CCCR_ASM_Pos)                     /**< (CAN_CCCR) ASM Restricted Operation Mode Mask */
#define CAN_CCCR_ASM(value)                   (CAN_CCCR_ASM_Msk & ((value) << CAN_CCCR_ASM_Pos))
#define CAN_CCCR_CSA_Pos                      (3U)                                           /**< (CAN_CCCR) Clock Stop Acknowledge Position */
#define CAN_CCCR_CSA_Msk                      (0x1U << CAN_CCCR_CSA_Pos)                     /**< (CAN_CCCR) Clock Stop Acknowledge Mask */
#define CAN_CCCR_CSA(value)                   (CAN_CCCR_CSA_Msk & ((value) << CAN_CCCR_CSA_Pos))
#define CAN_CCCR_CSR_Pos                      (4U)                                           /**< (CAN_CCCR) Clock Stop Request Position */
#define CAN_CCCR_CSR_Msk                      (0x1U << CAN_CCCR_CSR_Pos)                     /**< (CAN_CCCR) Clock Stop Request Mask */
#define CAN_CCCR_CSR(value)                   (CAN_CCCR_CSR_Msk & ((value) << CAN_CCCR_CSR_Pos))
#define CAN_CCCR_MON_Pos                      (5U)                                           /**< (CAN_CCCR) Bus Monitoring Mode Position */
#define CAN_CCCR_MON_Msk                      (0x1U << CAN_CCCR_MON_Pos)                     /**< (CAN_CCCR) Bus Monitoring Mode Mask */
#define CAN_CCCR_MON(value)                   (CAN_CCCR_MON_Msk & ((value) << CAN_CCCR_MON_Pos))
#define CAN_CCCR_DAR_Pos                      (6U)                                           /**< (CAN_CCCR) Disable Automatic Retransmission Position */
#define CAN_CCCR_DAR_Msk                      (0x1U << CAN_CCCR_DAR_Pos)                     /**< (CAN_CCCR) Disable Automatic Retransmission Mask */
#define CAN_CCCR_DAR(value)                   (CAN_CCCR_DAR_Msk & ((value) << CAN_CCCR_DAR_Pos))
#define CAN_CCCR_TEST_Pos                     (7U)                                           /**< (CAN_CCCR) Test Mode Enable Position */
#define CAN_CCCR_TEST_Msk                     (0x1U << CAN_CCCR_TEST_Pos)                    /**< (CAN_CCCR) Test Mode Enable Mask */
#define CAN_CCCR_TEST(value)                  (CAN_CCCR_TEST_Msk & ((value) << CAN_CCCR_TEST_Pos))
#define CAN_CCCR_FDOE_Pos                     (8U)                                           /**< (CAN_CCCR) FD Operation Enable Position */
#define CAN_CCCR_FDOE_Msk                     (0x1U << CAN_CCCR_FDOE_Pos)                    /**< (CAN_CCCR) FD Operation Enable Mask */
#define CAN_CCCR_FDOE(value)                  (CAN_CCCR_FDOE_Msk & ((value) << CAN_CCCR_FDOE_Pos))
#define CAN_CCCR_BRSE_Pos                     (9U)                                           /**< (CAN_CCCR) Bit Rate Switch Enable Position */
#define CAN_CCCR_BRSE_Msk                     (0x1U << CAN_CCCR_BRSE_Pos)                    /**< (CAN_CCCR) Bit Rate Switch Enable Mask */
#define CAN_CCCR_BRSE(value)                  (CAN_CCCR_BRSE_Msk & ((value) << CAN_CCCR_BRSE_Pos))
#define CAN_CCCR_PXHD_Pos                     (12U)                                          /**< (CAN_CCCR) Protocol Exception Handling Disable Position */
#define CAN_CCCR_PXHD_Msk                     (0x1U << CAN_CCCR_PXHD_Pos)                    /**< (CAN_CCCR) Protocol Exception Handling Disable Mask */
#define CAN_CCCR_PXHD(value)                  (CAN_CCCR_PXHD_Msk & ((value) << CAN_CCCR_PXHD_Pos))
#define CAN_CCCR_EFBI_Pos                     (13U)                                          /**< (CAN_CCCR) Edge Filtering during Bus Integration Position */
#define CAN_CCCR_EFBI_Msk                     (0x1U << CAN_CCCR_EFBI_Pos)                    /**< (CAN_CCCR) Edge Filtering during Bus Integration Mask */
#define CAN_CCCR_EFBI(value)                  (CAN_CCCR_EFBI_Msk & ((value) << CAN_CCCR_EFBI_Pos))
#define CAN_CCCR_TXP_Pos                      (14U)                                          /**< (CAN_CCCR) Transmit Pause Position */
#define CAN_CCCR_TXP_Msk                      (0x1U << CAN_CCCR_TXP_Pos)                     /**< (CAN_CCCR) Transmit Pause Mask */
#define CAN_CCCR_TXP(value)                   (CAN_CCCR_TXP_Msk & ((value) << CAN_CCCR_TXP_Pos))
#define CAN_CCCR_NISO_Pos                     (15U)                                          /**< (CAN_CCCR) Non ISO Operation Position */
#define CAN_CCCR_NISO_Msk                     (0x1U << CAN_CCCR_NISO_Pos)                    /**< (CAN_CCCR) Non ISO Operation Mask */
#define CAN_CCCR_NISO(value)                  (CAN_CCCR_NISO_Msk & ((value) << CAN_CCCR_NISO_Pos))
#define CAN_CCCR_Msk                          (0x0000F3FFUL)                                 /**< (CAN_CCCR) Register Mask  */

/* -------- CAN_NBTP : (CAN Offset: 0x1C) (R/W 32) Nominal Bit Timing and Prescaler -------- */
#define CAN_NBTP_NTSEG2_Pos                   (0U)                                           /**< (CAN_NBTP) Nominal Time segment after sample point Position */
#define CAN_NBTP_NTSEG2_Msk                   (0x7FU << CAN_NBTP_NTSEG2_Pos)                 /**< (CAN_NBTP) Nominal Time segment after sample point Mask */
#define CAN_NBTP_NTSEG2(value)                (CAN_NBTP_NTSEG2_Msk & ((value) << CAN_NBTP_NTSEG2_Pos))
#define CAN_NBTP_NTSEG1_Pos                   (8U)                                           /**< (CAN_NBTP) Nominal Time segment before sample point Position */
#define CAN_NBTP_NTSEG1_Msk                   (0xFFU << CAN_NBTP_NTSEG1_Pos)                 /**< (CAN_NBTP) Nominal Time segment before sample point Mask */
#define CAN_NBTP_NTSEG1(value)                (CAN_NBTP_NTSEG1_Msk & ((value) << CAN_NBTP_NTSEG1_Pos))
#define CAN_NBTP_NBRP_Pos                     (16U)                                          /**< (CAN_NBTP) Nominal Baud Rate Prescaler Position */
#define CAN_NBTP_NBRP_Msk                     (0x1FFU << CAN_NBTP_NBRP_Pos)                  /**< (CAN_NBTP) Nominal Baud Rate Prescaler Mask */
#define CAN_NBTP_NBRP(value)                  (CAN_NBTP_NBRP_Msk & ((value) << CAN_NBTP_NBRP_Pos))
#define CAN_NBTP_NSJW_Pos                     (25U)                                          /**< (CAN_NBTP) Nominal (Re)Synchronization Jump Width Position */
#define CAN_NBTP_NSJW_Msk                     (0x7FU << CAN_NBTP_NSJW_Pos)                   /**< (CAN_NBTP) Nominal (Re)Synchronization Jump Width Mask */
#define CAN_NBTP_NSJW(value)                  (CAN_NBTP_NSJW_Msk & ((value) << CAN_NBTP_NSJW_Pos))
#define CAN_NBTP_Msk                          (0xFFFFFF7FUL)                                 /**< (CAN_NBTP) Register Mask  */

/* -------- CAN_TSCC : (CAN Offset: 0x20) (R/W 32) Timestamp Counter Configuration -------- */
#define CAN_TSCC_TSS_Pos                      (0U)                                           /**< (CAN_TSCC) Timestamp Select Position */
#define CAN_TSCC_TSS_Msk                      (0x3U << CAN_TSCC_TSS_Pos)                     /**< (CAN_TSCC) Timestamp Select Mask */
#define CAN_TSCC_TSS(value)                   (CAN_TSCC_TSS_Msk & ((value) << CAN_TSCC_TSS_Pos))
#define   CAN_TSCC_TSS_ZERO_Val               (0U)                                           /**< (CAN_TSCC) Timestamp counter value always 0x0000  */
#define   CAN_TSCC_TSS_INC_Val                (1U)                                           /**< (CAN_TSCC) Timestamp counter value incremented by TCP  */
#define   CAN_TSCC_TSS_EXT_Val                (2U)                                           /**< (CAN_TSCC) External timestamp counter value used  */
#define CAN_TSCC_TSS_ZERO                     (CAN_TSCC_TSS_ZERO_Val << CAN_TSCC_TSS_Pos)    /**< (CAN_TSCC) Timestamp counter value always 0x0000 Position  */
#define CAN_TSCC_TSS_INC                      (CAN_TSCC_TSS_INC_Val << CAN_TSCC_TSS_Pos)     /**< (CAN_TSCC) Timestamp counter value incremented by TCP Position  */
#define CAN_TSCC_TSS_EXT                      (CAN_TSCC_TSS_EXT_Val << CAN_TSCC_TSS_Pos)     /**< (CAN_TSCC) External timestamp counter value used Position  */
#define CAN_TSCC_TCP_Pos                      (16U)                                          /**< (CAN_TSCC) Timestamp Counter Prescaler Position */
#define CAN_TSCC_TCP_Msk                      (0xFU << CAN_TSCC_TCP_Pos)                     /**< (CAN_TSCC) Timestamp Counter Prescaler Mask */
#define CAN_TSCC_TCP(value)                   (CAN_TSCC_TCP_Msk & ((value) << CAN_TSCC_TCP_Pos))
#define CAN_TSCC_Msk                          (0x000F0003UL)                                 /**< (CAN_TSCC) Register Mask  */

/* -------- CAN_TSCV : (CAN Offset: 0x24) (R/  32) Timestamp Counter Value -------- */
#define CAN_TSCV_TSC_Pos                      (0U)                                           /**< (CAN_TSCV) Timestamp Counter Position */
#define CAN_TSCV_TSC_Msk                      (0xFFFFU << CAN_TSCV_TSC_Pos)                  /**< (CAN_TSCV) Timestamp Counter Mask */
#define CAN_TSCV_TSC(value)                   (CAN_TSCV_TSC_Msk & ((value) << CAN_TSCV_TSC_Pos))
#define CAN_TSCV_Msk                          (0x0000FFFFUL)                                 /**< (CAN_TSCV) Register Mask  */

/* -------- CAN_TOCC : (CAN Offset: 0x28) (R/W 32) Timeout Counter Configuration -------- */
#define CAN_TOCC_ETOC_Pos                     (0U)                                           /**< (CAN_TOCC) Enable Timeout Counter Position */
#define CAN_TOCC_ETOC_Msk                     (0x1U << CAN_TOCC_ETOC_Pos)                    /**< (CAN_TOCC) Enable Timeout Counter Mask */
#define CAN_TOCC_ETOC(value)                  (CAN_TOCC_ETOC_Msk & ((value) << CAN_TOCC_ETOC_Pos))
#define CAN_TOCC_TOS_Pos                      (1U)                                           /**< (CAN_TOCC) Timeout Select Position */
#define CAN_TOCC_TOS_Msk                      (0x3U << CAN_TOCC_TOS_Pos)                     /**< (CAN_TOCC) Timeout Select Mask */
#define CAN_TOCC_TOS(value)                   (CAN_TOCC_TOS_Msk & ((value) << CAN_TOCC_TOS_Pos))
#define   CAN_TOCC_TOS_CONT_Val               (0U)                                           /**< (CAN_TOCC) Continuout operation  */
#define   CAN_TOCC_TOS_TXEF_Val               (1U)                                           /**< (CAN_TOCC) Timeout controlled by TX Event FIFO  */
#define   CAN_TOCC_TOS_RXF0_Val               (2U)                                           /**< (CAN_TOCC) Timeout controlled by Rx FIFO 0  */
#define   CAN_TOCC_TOS_RXF1_Val               (3U)                                           /**< (CAN_TOCC) Timeout controlled by Rx FIFO 1  */
#define CAN_TOCC_TOS_CONT                     (CAN_TOCC_TOS_CONT_Val << CAN_TOCC_TOS_Pos)    /**< (CAN_TOCC) Continuout operation Position  */
#define CAN_TOCC_TOS_TXEF                     (CAN_TOCC_TOS_TXEF_Val << CAN_TOCC_TOS_Pos)    /**< (CAN_TOCC) Timeout controlled by TX Event FIFO Position  */
#define CAN_TOCC_TOS_RXF0                     (CAN_TOCC_TOS_RXF0_Val << CAN_TOCC_TOS_Pos)    /**< (CAN_TOCC) Timeout controlled by Rx FIFO 0 Position  */
#define CAN_TOCC_TOS_RXF1                     (CAN_TOCC_TOS_RXF1_Val << CAN_TOCC_TOS_Pos)    /**< (CAN_TOCC) Timeout controlled by Rx FIFO 1 Position  */
#define CAN_TOCC_TOP_Pos                      (16U)                                          /**< (CAN_TOCC) Timeout Period Position */
#define CAN_TOCC_TOP_Msk                      (0xFFFFU << CAN_TOCC_TOP_Pos)                  /**< (CAN_TOCC) Timeout Period Mask */
#define CAN_TOCC_TOP(value)                   (CAN_TOCC_TOP_Msk & ((value) << CAN_TOCC_TOP_Pos))
#define CAN_TOCC_Msk                          (0xFFFF0007UL)                                 /**< (CAN_TOCC) Register Mask  */

/* -------- CAN_TOCV : (CAN Offset: 0x2C) (R/W 32) Timeout Counter Value -------- */
#define CAN_TOCV_TOC_Pos                      (0U)                                           /**< (CAN_TOCV) Timeout Counter Position */
#define CAN_TOCV_TOC_Msk                      (0xFFFFU << CAN_TOCV_TOC_Pos)                  /**< (CAN_TOCV) Timeout Counter Mask */
#define CAN_TOCV_TOC(value)                   (CAN_TOCV_TOC_Msk & ((value) << CAN_TOCV_TOC_Pos))
#define CAN_TOCV_Msk                          (0x0000FFFFUL)                                 /**< (CAN_TOCV) Register Mask  */

/* -------- CAN_ECR : (CAN Offset: 0x40) (R/  32) Error Counter -------- */
#define CAN_ECR_TEC_Pos                       (0U)                                           /**< (CAN_ECR) Transmit Error Counter Position */
#define CAN_ECR_TEC_Msk                       (0xFFU << CAN_ECR_TEC_Pos)                     /**< (CAN_ECR) Transmit Error Counter Mask */
#define CAN_ECR_TEC(value)                    (CAN_ECR_TEC_Msk & ((value) << CAN_ECR_TEC_Pos))
#define CAN_ECR_REC_Pos                       (8U)                                           /**< (CAN_ECR) Receive Error Counter Position */
#define CAN_ECR_REC_Msk                       (0x7FU << CAN_ECR_REC_Pos)                     /**< (CAN_ECR) Receive Error Counter Mask */
#define CAN_ECR_REC(value)                    (CAN_ECR_REC_Msk & ((value) << CAN_ECR_REC_Pos))
#define CAN_ECR_RP_Pos                        (15U)                                          /**< (CAN_ECR) Receive Error Passive Position */
#define CAN_ECR_RP_Msk                        (0x1U << CAN_ECR_RP_Pos)                       /**< (CAN_ECR) Receive Error Passive Mask */
#define CAN_ECR_RP(value)                     (CAN_ECR_RP_Msk & ((value) << CAN_ECR_RP_Pos))
#define CAN_ECR_CEL_Pos                       (16U)                                          /**< (CAN_ECR) CAN Error Logging Position */
#define CAN_ECR_CEL_Msk                       (0xFFU << CAN_ECR_CEL_Pos)                     /**< (CAN_ECR) CAN Error Logging Mask */
#define CAN_ECR_CEL(value)                    (CAN_ECR_CEL_Msk & ((value) << CAN_ECR_CEL_Pos))
#define CAN_ECR_Msk                           (0x00FFFFFFUL)                                 /**< (CAN_ECR) Register Mask  */

/* -------- CAN_PSR : (CAN Offset: 0x44) (R/  32) Protocol Status -------- */
#define CAN_PSR_LEC_Pos                       (0U)                                           /**< (CAN_PSR) Last Error Code Position */
#define CAN_PSR_LEC_Msk                       (0x7U << CAN_PSR_LEC_Pos)                      /**< (CAN_PSR) Last Error Code Mask */
#define CAN_PSR_LEC(value)                    (CAN_PSR_LEC_Msk & ((value) << CAN_PSR_LEC_Pos))
#define   CAN_PSR_LEC_NONE_Val                (0U)                                           /**< (CAN_PSR) No Error  */
#define   CAN_PSR_LEC_STUFF_Val               (1U)                                           /**< (CAN_PSR) Stuff Error  */
#define   CAN_PSR_LEC_FORM_Val                (2U)                                           /**< (CAN_PSR) Form Error  */
#define   CAN_PSR_LEC_ACK_Val                 (3U)                                           /**< (CAN_PSR) Ack Error  */
#define   CAN_PSR_LEC_BIT1_Val                (4U)                                           /**< (CAN_PSR) Bit1 Error  */
#define   CAN_PSR_LEC_BIT0_Val                (5U)                                           /**< (CAN_PSR) Bit0 Error  */
#define   CAN_PSR_LEC_CRC_Val                 (6U)                                           /**< (CAN_PSR) CRC Error  */
#define   CAN_PSR_LEC_NC_Val                  (7U)                                           /**< (CAN_PSR) No Change  */
#define CAN_PSR_LEC_NONE                      (CAN_PSR_LEC_NONE_Val << CAN_PSR_LEC_Pos)      /**< (CAN_PSR) No Error Position  */
#define CAN_PSR_LEC_STUFF                     (CAN_PSR_LEC_STUFF_Val << CAN_PSR_LEC_Pos)     /**< (CAN_PSR) Stuff Error Position  */
#define CAN_PSR_LEC_FORM                      (CAN_PSR_LEC_FORM_Val << CAN_PSR_LEC_Pos)      /**< (CAN_PSR) Form Error Position  */
#define CAN_PSR_LEC_ACK                       (CAN_PSR_LEC_ACK_Val << CAN_PSR_LEC_Pos)       /**< (CAN_PSR) Ack Error Position  */
#define CAN_PSR_LEC_BIT1                      (CAN_PSR_LEC_BIT1_Val << CAN_PSR_LEC_Pos)      /**< (CAN_PSR) Bit1 Error Position  */
#define CAN_PSR_LEC_BIT0                      (CAN_PSR_LEC_BIT0_Val << CAN_PSR_LEC_Pos)      /**< (CAN_PSR) Bit0 Error Position  */
#define CAN_PSR_LEC_CRC                       (CAN_PSR_LEC_CRC_Val << CAN_PSR_LEC_Pos)       /**< (CAN_PSR) CRC Error Position  */
#define CAN_PSR_LEC_NC                        (CAN_PSR_LEC_NC_Val << CAN_PSR_LEC_Pos)        /**< (CAN_PSR) No Change Position  */
#define CAN_PSR_ACT_Pos                       (3U)                                           /**< (CAN_PSR) Activity Position */
#define CAN_PSR_ACT_Msk                       (0x3U << CAN_PSR_ACT_Pos)                      /**< (CAN_PSR) Activity Mask */
#define CAN_PSR_ACT(value)                    (CAN_PSR_ACT_Msk & ((value) << CAN_PSR_ACT_Pos))
#define   CAN_PSR_ACT_SYNC_Val                (0U)                                           /**< (CAN_PSR) Node is synchronizing on CAN communication  */
#define   CAN_PSR_ACT_IDLE_Val                (1U)                                           /**< (CAN_PSR) Node is neither receiver nor transmitter  */
#define   CAN_PSR_ACT_RX_Val                  (2U)                                           /**< (CAN_PSR) Node is operating as receiver  */
#define   CAN_PSR_ACT_TX_Val                  (3U)                                           /**< (CAN_PSR) Node is operating as transmitter  */
#define CAN_PSR_ACT_SYNC                      (CAN_PSR_ACT_SYNC_Val << CAN_PSR_ACT_Pos)      /**< (CAN_PSR) Node is synchronizing on CAN communication Position  */
#define CAN_PSR_ACT_IDLE                      (CAN_PSR_ACT_IDLE_Val << CAN_PSR_ACT_Pos)      /**< (CAN_PSR) Node is neither receiver nor transmitter Position  */
#define CAN_PSR_ACT_RX                        (CAN_PSR_ACT_RX_Val << CAN_PSR_ACT_Pos)        /**< (CAN_PSR) Node is operating as receiver Position  */
#define CAN_PSR_ACT_TX                        (CAN_PSR_ACT_TX_Val << CAN_PSR_ACT_Pos)        /**< (CAN_PSR) Node is operating as transmitter Position  */
#define CAN_PSR_EP_Pos                        (5U)                                           /**< (CAN_PSR) Error Passive Position */
#define CAN_PSR_EP_Msk                        (0x1U << CAN_PSR_EP_Pos)                       /**< (CAN_PSR) Error Passive Mask */
#define CAN_PSR_EP(value)                     (CAN_PSR_EP_Msk & ((value) << CAN_PSR_EP_Pos))
#define CAN_PSR_EW_Pos                        (6U)                                           /**< (CAN_PSR) Warning Status Position */
#define CAN_PSR_EW_Msk                        (0x1U << CAN_PSR_EW_Pos)                       /**< (CAN_PSR) Warning Status Mask */
#define CAN_PSR_EW(value)                     (CAN_PSR_EW_Msk & ((value) << CAN_PSR_EW_Pos))
#define CAN_PSR_BO_Pos                        (7U)                                           /**< (CAN_PSR) Bus_Off Status Position */
#define CAN_PSR_BO_Msk                        (0x1U << CAN_PSR_BO_Pos)                       /**< (CAN_PSR) Bus_Off Status Mask */
#define CAN_PSR_BO(value)                     (CAN_PSR_BO_Msk & ((value) << CAN_PSR_BO_Pos))
#define CAN_PSR_DLEC_Pos                      (8U)                                           /**< (CAN_PSR) Data Phase Last Error Code Position */
#define CAN_PSR_DLEC_Msk                      (0x7U << CAN_PSR_DLEC_Pos)                     /**< (CAN_PSR) Data Phase Last Error Code Mask */
#define CAN_PSR_DLEC(value)                   (CAN_PSR_DLEC_Msk & ((value) << CAN_PSR_DLEC_Pos))
#define   CAN_PSR_DLEC_NONE_Val               (0U)                                           /**< (CAN_PSR) No Error  */
#define   CAN_PSR_DLEC_STUFF_Val              (1U)                                           /**< (CAN_PSR) Stuff Error  */
#define   CAN_PSR_DLEC_FORM_Val               (2U)                                           /**< (CAN_PSR) Form Error  */
#define   CAN_PSR_DLEC_ACK_Val                (3U)                                           /**< (CAN_PSR) Ack Error  */
#define   CAN_PSR_DLEC_BIT1_Val               (4U)                                           /**< (CAN_PSR) Bit1 Error  */
#define   CAN_PSR_DLEC_BIT0_Val               (5U)                                           /**< (CAN_PSR) Bit0 Error  */
#define   CAN_PSR_DLEC_CRC_Val                (6U)                                           /**< (CAN_PSR) CRC Error  */
#define   CAN_PSR_DLEC_NC_Val                 (7U)                                           /**< (CAN_PSR) No Change  */
#define CAN_PSR_DLEC_NONE                     (CAN_PSR_DLEC_NONE_Val << CAN_PSR_DLEC_Pos)    /**< (CAN_PSR) No Error Position  */
#define CAN_PSR_DLEC_STUFF                    (CAN_PSR_DLEC_STUFF_Val << CAN_PSR_DLEC_Pos)   /**< (CAN_PSR) Stuff Error Position  */
#define CAN_PSR_DLEC_FORM                     (CAN_PSR_DLEC_FORM_Val << CAN_PSR_DLEC_Pos)    /**< (CAN_PSR) Form Error Position  */
#define CAN_PSR_DLEC_ACK                      (CAN_PSR_DLEC_ACK_Val << CAN_PSR_DLEC_Pos)     /**< (CAN_PSR) Ack Error Position  */
#define CAN_PSR_DLEC_BIT1                     (CAN_PSR_DLEC_BIT1_Val << CAN_PSR_DLEC_Pos)    /**< (CAN_PSR) Bit1 Error Position  */
#define CAN_PSR_DLEC_BIT0                     (CAN_PSR_DLEC_BIT0_Val << CAN_PSR_DLEC_Pos)    /**< (CAN_PSR) Bit0 Error Position  */
#define CAN_PSR_DLEC_CRC                      (CAN_PSR_DLEC_CRC_Val << CAN_PSR_DLEC_Pos)     /**< (CAN_PSR) CRC Error Position  */
#define CAN_PSR_DLEC_NC                       (CAN_PSR_DLEC_NC_Val << CAN_PSR_DLEC_Pos)      /**< (CAN_PSR) No Change Position  */
#define CAN_PSR_RESI_Pos                      (11U)                                          /**< (CAN_PSR) ESI flag of last received CAN FD Message Position */
#define CAN_PSR_RESI_Msk                      (0x1U << CAN_PSR_RESI_Pos)                     /**< (CAN_PSR) ESI flag of last received CAN FD Message Mask */
#define CAN_PSR_RESI(value)                   (CAN_PSR_RESI_Msk & ((value) << CAN_PSR_RESI_Pos))
#define CAN_PSR_RBRS_Pos                      (12U)                                          /**< (CAN_PSR) BRS flag of last received CAN FD Message Position */
#define CAN_PSR_RBRS_Msk                      (0x1U << CAN_PSR_RBRS_Pos)                     /**< (CAN_PSR) BRS flag of last received CAN FD Message Mask */
#define CAN_PSR_RBRS(value)                   (CAN_PSR_RBRS_Msk & ((value) << CAN_PSR_RBRS_Pos))
#define CAN_PSR_RFDF_Pos                      (13U)                                          /**< (CAN_PSR) Received a CAN FD Message Position */
#define CAN_PSR_RFDF_Msk                      (0x1U << CAN_PSR_RFDF_Pos)                     /**< (CAN_PSR) Received a CAN FD Message Mask */
#define CAN_PSR_RFDF(value)                   (CAN_PSR_RFDF_Msk & ((value) << CAN_PSR_RFDF_Pos))
#define CAN_PSR_PXE_Pos                       (14U)                                          /**< (CAN_PSR) Protocol Exception Event Position */
#define CAN_PSR_PXE_Msk                       (0x1U << CAN_PSR_PXE_Pos)                      /**< (CAN_PSR) Protocol Exception Event Mask */
#define CAN_PSR_PXE(value)                    (CAN_PSR_PXE_Msk & ((value) << CAN_PSR_PXE_Pos))
#define CAN_PSR_TDCV_Pos                      (16U)                                          /**< (CAN_PSR) Transmitter Delay Compensation Value Position */
#define CAN_PSR_TDCV_Msk                      (0x7FU << CAN_PSR_TDCV_Pos)                    /**< (CAN_PSR) Transmitter Delay Compensation Value Mask */
#define CAN_PSR_TDCV(value)                   (CAN_PSR_TDCV_Msk & ((value) << CAN_PSR_TDCV_Pos))
#define CAN_PSR_Msk                           (0x007F7FFFUL)                                 /**< (CAN_PSR) Register Mask  */

/* -------- CAN_TDCR : (CAN Offset: 0x48) (R/W 32) Extended ID Filter Configuration -------- */
#define CAN_TDCR_TDCF_Pos                     (0U)                                           /**< (CAN_TDCR) Transmitter Delay Compensation Filter Length Position */
#define CAN_TDCR_TDCF_Msk                     (0x7FU << CAN_TDCR_TDCF_Pos)                   /**< (CAN_TDCR) Transmitter Delay Compensation Filter Length Mask */
#define CAN_TDCR_TDCF(value)                  (CAN_TDCR_TDCF_Msk & ((value) << CAN_TDCR_TDCF_Pos))
#define CAN_TDCR_TDCO_Pos                     (8U)                                           /**< (CAN_TDCR) Transmitter Delay Compensation Offset Position */
#define CAN_TDCR_TDCO_Msk                     (0x7FU << CAN_TDCR_TDCO_Pos)                   /**< (CAN_TDCR) Transmitter Delay Compensation Offset Mask */
#define CAN_TDCR_TDCO(value)                  (CAN_TDCR_TDCO_Msk & ((value) << CAN_TDCR_TDCO_Pos))
#define CAN_TDCR_Msk                          (0x00007F7FUL)                                 /**< (CAN_TDCR) Register Mask  */

/* -------- CAN_IR : (CAN Offset: 0x50) (R/W 32) Interrupt -------- */
#define CAN_IR_RF0N_Pos                       (0U)                                           /**< (CAN_IR) Rx FIFO 0 New Message Position */
#define CAN_IR_RF0N_Msk                       (0x1U << CAN_IR_RF0N_Pos)                      /**< (CAN_IR) Rx FIFO 0 New Message Mask */
#define CAN_IR_RF0N(value)                    (CAN_IR_RF0N_Msk & ((value) << CAN_IR_RF0N_Pos))
#define CAN_IR_RF0W_Pos                       (1U)                                           /**< (CAN_IR) Rx FIFO 0 Watermark Reached Position */
#define CAN_IR_RF0W_Msk                       (0x1U << CAN_IR_RF0W_Pos)                      /**< (CAN_IR) Rx FIFO 0 Watermark Reached Mask */
#define CAN_IR_RF0W(value)                    (CAN_IR_RF0W_Msk & ((value) << CAN_IR_RF0W_Pos))
#define CAN_IR_RF0F_Pos                       (2U)                                           /**< (CAN_IR) Rx FIFO 0 Full Position */
#define CAN_IR_RF0F_Msk                       (0x1U << CAN_IR_RF0F_Pos)                      /**< (CAN_IR) Rx FIFO 0 Full Mask */
#define CAN_IR_RF0F(value)                    (CAN_IR_RF0F_Msk & ((value) << CAN_IR_RF0F_Pos))
#define CAN_IR_RF0L_Pos                       (3U)                                           /**< (CAN_IR) Rx FIFO 0 Message Lost Position */
#define CAN_IR_RF0L_Msk                       (0x1U << CAN_IR_RF0L_Pos)                      /**< (CAN_IR) Rx FIFO 0 Message Lost Mask */
#define CAN_IR_RF0L(value)                    (CAN_IR_RF0L_Msk & ((value) << CAN_IR_RF0L_Pos))
#define CAN_IR_RF1N_Pos                       (4U)                                           /**< (CAN_IR) Rx FIFO 1 New Message Position */
#define CAN_IR_RF1N_Msk                       (0x1U << CAN_IR_RF1N_Pos)                      /**< (CAN_IR) Rx FIFO 1 New Message Mask */
#define CAN_IR_RF1N(value)                    (CAN_IR_RF1N_Msk & ((value) << CAN_IR_RF1N_Pos))
#define CAN_IR_RF1W_Pos                       (5U)                                           /**< (CAN_IR) Rx FIFO 1 Watermark Reached Position */
#define CAN_IR_RF1W_Msk                       (0x1U << CAN_IR_RF1W_Pos)                      /**< (CAN_IR) Rx FIFO 1 Watermark Reached Mask */
#define CAN_IR_RF1W(value)                    (CAN_IR_RF1W_Msk & ((value) << CAN_IR_RF1W_Pos))
#define CAN_IR_RF1F_Pos                       (6U)                                           /**< (CAN_IR) Rx FIFO 1 FIFO Full Position */
#define CAN_IR_RF1F_Msk                       (0x1U << CAN_IR_RF1F_Pos)                      /**< (CAN_IR) Rx FIFO 1 FIFO Full Mask */
#define CAN_IR_RF1F(value)                    (CAN_IR_RF1F_Msk & ((value) << CAN_IR_RF1F_Pos))
#define CAN_IR_RF1L_Pos                       (7U)                                           /**< (CAN_IR) Rx FIFO 1 Message Lost Position */
#define CAN_IR_RF1L_Msk                       (0x1U << CAN_IR_RF1L_Pos)                      /**< (CAN_IR) Rx FIFO 1 Message Lost Mask */
#define CAN_IR_RF1L(value)                    (CAN_IR_RF1L_Msk & ((value) << CAN_IR_RF1L_Pos))
#define CAN_IR_HPM_Pos                        (8U)                                           /**< (CAN_IR) High Priority Message Position */
#define CAN_IR_HPM_Msk                        (0x1U << CAN_IR_HPM_Pos)                       /**< (CAN_IR) High Priority Message Mask */
#define CAN_IR_HPM(value)                     (CAN_IR_HPM_Msk & ((value) << CAN_IR_HPM_Pos))
#define CAN_IR_TC_Pos                         (9U)                                           /**< (CAN_IR) Timestamp Completed Position */
#define CAN_IR_TC_Msk                         (0x1U << CAN_IR_TC_Pos)                        /**< (CAN_IR) Timestamp Completed Mask */
#define CAN_IR_TC(value)                      (CAN_IR_TC_Msk & ((value) << CAN_IR_TC_Pos))  
#define CAN_IR_TCF_Pos                        (10U)                                          /**< (CAN_IR) Transmission Cancellation Finished Position */
#define CAN_IR_TCF_Msk                        (0x1U << CAN_IR_TCF_Pos)                       /**< (CAN_IR) Transmission Cancellation Finished Mask */
#define CAN_IR_TCF(value)                     (CAN_IR_TCF_Msk & ((value) << CAN_IR_TCF_Pos))
#define CAN_IR_TFE_Pos                        (11U)                                          /**< (CAN_IR) Tx FIFO Empty Position */
#define CAN_IR_TFE_Msk                        (0x1U << CAN_IR_TFE_Pos)                       /**< (CAN_IR) Tx FIFO Empty Mask */
#define CAN_IR_TFE(value)                     (CAN_IR_TFE_Msk & ((value) << CAN_IR_TFE_Pos))
#define CAN_IR_TEFN_Pos                       (12U)                                          /**< (CAN_IR) Tx Event FIFO New Entry Position */
#define CAN_IR_TEFN_Msk                       (0x1U << CAN_IR_TEFN_Pos)                      /**< (CAN_IR) Tx Event FIFO New Entry Mask */
#define CAN_IR_TEFN(value)                    (CAN_IR_TEFN_Msk & ((value) << CAN_IR_TEFN_Pos))
#define CAN_IR_TEFW_Pos                       (13U)                                          /**< (CAN_IR) Tx Event FIFO Watermark Reached Position */
#define CAN_IR_TEFW_Msk                       (0x1U << CAN_IR_TEFW_Pos)                      /**< (CAN_IR) Tx Event FIFO Watermark Reached Mask */
#define CAN_IR_TEFW(value)                    (CAN_IR_TEFW_Msk & ((value) << CAN_IR_TEFW_Pos))
#define CAN_IR_TEFF_Pos                       (14U)                                          /**< (CAN_IR) Tx Event FIFO Full Position */
#define CAN_IR_TEFF_Msk                       (0x1U << CAN_IR_TEFF_Pos)                      /**< (CAN_IR) Tx Event FIFO Full Mask */
#define CAN_IR_TEFF(value)                    (CAN_IR_TEFF_Msk & ((value) << CAN_IR_TEFF_Pos))
#define CAN_IR_TEFL_Pos                       (15U)                                          /**< (CAN_IR) Tx Event FIFO Element Lost Position */
#define CAN_IR_TEFL_Msk                       (0x1U << CAN_IR_TEFL_Pos)                      /**< (CAN_IR) Tx Event FIFO Element Lost Mask */
#define CAN_IR_TEFL(value)                    (CAN_IR_TEFL_Msk & ((value) << CAN_IR_TEFL_Pos))
#define CAN_IR_TSW_Pos                        (16U)                                          /**< (CAN_IR) Timestamp Wraparound Position */
#define CAN_IR_TSW_Msk                        (0x1U << CAN_IR_TSW_Pos)                       /**< (CAN_IR) Timestamp Wraparound Mask */
#define CAN_IR_TSW(value)                     (CAN_IR_TSW_Msk & ((value) << CAN_IR_TSW_Pos))
#define CAN_IR_MRAF_Pos                       (17U)                                          /**< (CAN_IR) Message RAM Access Failure Position */
#define CAN_IR_MRAF_Msk                       (0x1U << CAN_IR_MRAF_Pos)                      /**< (CAN_IR) Message RAM Access Failure Mask */
#define CAN_IR_MRAF(value)                    (CAN_IR_MRAF_Msk & ((value) << CAN_IR_MRAF_Pos))
#define CAN_IR_TOO_Pos                        (18U)                                          /**< (CAN_IR) Timeout Occurred Position */
#define CAN_IR_TOO_Msk                        (0x1U << CAN_IR_TOO_Pos)                       /**< (CAN_IR) Timeout Occurred Mask */
#define CAN_IR_TOO(value)                     (CAN_IR_TOO_Msk & ((value) << CAN_IR_TOO_Pos))
#define CAN_IR_DRX_Pos                        (19U)                                          /**< (CAN_IR) Message stored to Dedicated Rx Buffer Position */
#define CAN_IR_DRX_Msk                        (0x1U << CAN_IR_DRX_Pos)                       /**< (CAN_IR) Message stored to Dedicated Rx Buffer Mask */
#define CAN_IR_DRX(value)                     (CAN_IR_DRX_Msk & ((value) << CAN_IR_DRX_Pos))
#define CAN_IR_BEC_Pos                        (20U)                                          /**< (CAN_IR) Bit Error Corrected Position */
#define CAN_IR_BEC_Msk                        (0x1U << CAN_IR_BEC_Pos)                       /**< (CAN_IR) Bit Error Corrected Mask */
#define CAN_IR_BEC(value)                     (CAN_IR_BEC_Msk & ((value) << CAN_IR_BEC_Pos))
#define CAN_IR_BEU_Pos                        (21U)                                          /**< (CAN_IR) Bit Error Uncorrected Position */
#define CAN_IR_BEU_Msk                        (0x1U << CAN_IR_BEU_Pos)                       /**< (CAN_IR) Bit Error Uncorrected Mask */
#define CAN_IR_BEU(value)                     (CAN_IR_BEU_Msk & ((value) << CAN_IR_BEU_Pos))
#define CAN_IR_ELO_Pos                        (22U)                                          /**< (CAN_IR) Error Logging Overflow Position */
#define CAN_IR_ELO_Msk                        (0x1U << CAN_IR_ELO_Pos)                       /**< (CAN_IR) Error Logging Overflow Mask */
#define CAN_IR_ELO(value)                     (CAN_IR_ELO_Msk & ((value) << CAN_IR_ELO_Pos))
#define CAN_IR_EP_Pos                         (23U)                                          /**< (CAN_IR) Error Passive Position */
#define CAN_IR_EP_Msk                         (0x1U << CAN_IR_EP_Pos)                        /**< (CAN_IR) Error Passive Mask */
#define CAN_IR_EP(value)                      (CAN_IR_EP_Msk & ((value) << CAN_IR_EP_Pos))  
#define CAN_IR_EW_Pos                         (24U)                                          /**< (CAN_IR) Warning Status Position */
#define CAN_IR_EW_Msk                         (0x1U << CAN_IR_EW_Pos)                        /**< (CAN_IR) Warning Status Mask */
#define CAN_IR_EW(value)                      (CAN_IR_EW_Msk & ((value) << CAN_IR_EW_Pos))  
#define CAN_IR_BO_Pos                         (25U)                                          /**< (CAN_IR) Bus_Off Status Position */
#define CAN_IR_BO_Msk                         (0x1U << CAN_IR_BO_Pos)                        /**< (CAN_IR) Bus_Off Status Mask */
#define CAN_IR_BO(value)                      (CAN_IR_BO_Msk & ((value) << CAN_IR_BO_Pos))  
#define CAN_IR_WDI_Pos                        (26U)                                          /**< (CAN_IR) Watchdog Interrupt Position */
#define CAN_IR_WDI_Msk                        (0x1U << CAN_IR_WDI_Pos)                       /**< (CAN_IR) Watchdog Interrupt Mask */
#define CAN_IR_WDI(value)                     (CAN_IR_WDI_Msk & ((value) << CAN_IR_WDI_Pos))
#define CAN_IR_PEA_Pos                        (27U)                                          /**< (CAN_IR) Protocol Error in Arbitration Phase Position */
#define CAN_IR_PEA_Msk                        (0x1U << CAN_IR_PEA_Pos)                       /**< (CAN_IR) Protocol Error in Arbitration Phase Mask */
#define CAN_IR_PEA(value)                     (CAN_IR_PEA_Msk & ((value) << CAN_IR_PEA_Pos))
#define CAN_IR_PED_Pos                        (28U)                                          /**< (CAN_IR) Protocol Error in Data Phase Position */
#define CAN_IR_PED_Msk                        (0x1U << CAN_IR_PED_Pos)                       /**< (CAN_IR) Protocol Error in Data Phase Mask */
#define CAN_IR_PED(value)                     (CAN_IR_PED_Msk & ((value) << CAN_IR_PED_Pos))
#define CAN_IR_ARA_Pos                        (29U)                                          /**< (CAN_IR) Access to Reserved Address Position */
#define CAN_IR_ARA_Msk                        (0x1U << CAN_IR_ARA_Pos)                       /**< (CAN_IR) Access to Reserved Address Mask */
#define CAN_IR_ARA(value)                     (CAN_IR_ARA_Msk & ((value) << CAN_IR_ARA_Pos))
#define CAN_IR_Msk                            (0x3FFFFFFFUL)                                 /**< (CAN_IR) Register Mask  */

/* -------- CAN_IE : (CAN Offset: 0x54) (R/W 32) Interrupt Enable -------- */
#define CAN_IE_RF0NE_Pos                      (0U)                                           /**< (CAN_IE) Rx FIFO 0 New Message Interrupt Enable Position */
#define CAN_IE_RF0NE_Msk                      (0x1U << CAN_IE_RF0NE_Pos)                     /**< (CAN_IE) Rx FIFO 0 New Message Interrupt Enable Mask */
#define CAN_IE_RF0NE(value)                   (CAN_IE_RF0NE_Msk & ((value) << CAN_IE_RF0NE_Pos))
#define CAN_IE_RF0WE_Pos                      (1U)                                           /**< (CAN_IE) Rx FIFO 0 Watermark Reached Interrupt Enable Position */
#define CAN_IE_RF0WE_Msk                      (0x1U << CAN_IE_RF0WE_Pos)                     /**< (CAN_IE) Rx FIFO 0 Watermark Reached Interrupt Enable Mask */
#define CAN_IE_RF0WE(value)                   (CAN_IE_RF0WE_Msk & ((value) << CAN_IE_RF0WE_Pos))
#define CAN_IE_RF0FE_Pos                      (2U)                                           /**< (CAN_IE) Rx FIFO 0 Full Interrupt Enable Position */
#define CAN_IE_RF0FE_Msk                      (0x1U << CAN_IE_RF0FE_Pos)                     /**< (CAN_IE) Rx FIFO 0 Full Interrupt Enable Mask */
#define CAN_IE_RF0FE(value)                   (CAN_IE_RF0FE_Msk & ((value) << CAN_IE_RF0FE_Pos))
#define CAN_IE_RF0LE_Pos                      (3U)                                           /**< (CAN_IE) Rx FIFO 0 Message Lost Interrupt Enable Position */
#define CAN_IE_RF0LE_Msk                      (0x1U << CAN_IE_RF0LE_Pos)                     /**< (CAN_IE) Rx FIFO 0 Message Lost Interrupt Enable Mask */
#define CAN_IE_RF0LE(value)                   (CAN_IE_RF0LE_Msk & ((value) << CAN_IE_RF0LE_Pos))
#define CAN_IE_RF1NE_Pos                      (4U)                                           /**< (CAN_IE) Rx FIFO 1 New Message Interrupt Enable Position */
#define CAN_IE_RF1NE_Msk                      (0x1U << CAN_IE_RF1NE_Pos)                     /**< (CAN_IE) Rx FIFO 1 New Message Interrupt Enable Mask */
#define CAN_IE_RF1NE(value)                   (CAN_IE_RF1NE_Msk & ((value) << CAN_IE_RF1NE_Pos))
#define CAN_IE_RF1WE_Pos                      (5U)                                           /**< (CAN_IE) Rx FIFO 1 Watermark Reached Interrupt Enable Position */
#define CAN_IE_RF1WE_Msk                      (0x1U << CAN_IE_RF1WE_Pos)                     /**< (CAN_IE) Rx FIFO 1 Watermark Reached Interrupt Enable Mask */
#define CAN_IE_RF1WE(value)                   (CAN_IE_RF1WE_Msk & ((value) << CAN_IE_RF1WE_Pos))
#define CAN_IE_RF1FE_Pos                      (6U)                                           /**< (CAN_IE) Rx FIFO 1 FIFO Full Interrupt Enable Position */
#define CAN_IE_RF1FE_Msk                      (0x1U << CAN_IE_RF1FE_Pos)                     /**< (CAN_IE) Rx FIFO 1 FIFO Full Interrupt Enable Mask */
#define CAN_IE_RF1FE(value)                   (CAN_IE_RF1FE_Msk & ((value) << CAN_IE_RF1FE_Pos))
#define CAN_IE_RF1LE_Pos                      (7U)                                           /**< (CAN_IE) Rx FIFO 1 Message Lost Interrupt Enable Position */
#define CAN_IE_RF1LE_Msk                      (0x1U << CAN_IE_RF1LE_Pos)                     /**< (CAN_IE) Rx FIFO 1 Message Lost Interrupt Enable Mask */
#define CAN_IE_RF1LE(value)                   (CAN_IE_RF1LE_Msk & ((value) << CAN_IE_RF1LE_Pos))
#define CAN_IE_HPME_Pos                       (8U)                                           /**< (CAN_IE) High Priority Message Interrupt Enable Position */
#define CAN_IE_HPME_Msk                       (0x1U << CAN_IE_HPME_Pos)                      /**< (CAN_IE) High Priority Message Interrupt Enable Mask */
#define CAN_IE_HPME(value)                    (CAN_IE_HPME_Msk & ((value) << CAN_IE_HPME_Pos))
#define CAN_IE_TCE_Pos                        (9U)                                           /**< (CAN_IE) Timestamp Completed Interrupt Enable Position */
#define CAN_IE_TCE_Msk                        (0x1U << CAN_IE_TCE_Pos)                       /**< (CAN_IE) Timestamp Completed Interrupt Enable Mask */
#define CAN_IE_TCE(value)                     (CAN_IE_TCE_Msk & ((value) << CAN_IE_TCE_Pos))
#define CAN_IE_TCFE_Pos                       (10U)                                          /**< (CAN_IE) Transmission Cancellation Finished Interrupt Enable Position */
#define CAN_IE_TCFE_Msk                       (0x1U << CAN_IE_TCFE_Pos)                      /**< (CAN_IE) Transmission Cancellation Finished Interrupt Enable Mask */
#define CAN_IE_TCFE(value)                    (CAN_IE_TCFE_Msk & ((value) << CAN_IE_TCFE_Pos))
#define CAN_IE_TFEE_Pos                       (11U)                                          /**< (CAN_IE) Tx FIFO Empty Interrupt Enable Position */
#define CAN_IE_TFEE_Msk                       (0x1U << CAN_IE_TFEE_Pos)                      /**< (CAN_IE) Tx FIFO Empty Interrupt Enable Mask */
#define CAN_IE_TFEE(value)                    (CAN_IE_TFEE_Msk & ((value) << CAN_IE_TFEE_Pos))
#define CAN_IE_TEFNE_Pos                      (12U)                                          /**< (CAN_IE) Tx Event FIFO New Entry Interrupt Enable Position */
#define CAN_IE_TEFNE_Msk                      (0x1U << CAN_IE_TEFNE_Pos)                     /**< (CAN_IE) Tx Event FIFO New Entry Interrupt Enable Mask */
#define CAN_IE_TEFNE(value)                   (CAN_IE_TEFNE_Msk & ((value) << CAN_IE_TEFNE_Pos))
#define CAN_IE_TEFWE_Pos                      (13U)                                          /**< (CAN_IE) Tx Event FIFO Watermark Reached Interrupt Enable Position */
#define CAN_IE_TEFWE_Msk                      (0x1U << CAN_IE_TEFWE_Pos)                     /**< (CAN_IE) Tx Event FIFO Watermark Reached Interrupt Enable Mask */
#define CAN_IE_TEFWE(value)                   (CAN_IE_TEFWE_Msk & ((value) << CAN_IE_TEFWE_Pos))
#define CAN_IE_TEFFE_Pos                      (14U)                                          /**< (CAN_IE) Tx Event FIFO Full Interrupt Enable Position */
#define CAN_IE_TEFFE_Msk                      (0x1U << CAN_IE_TEFFE_Pos)                     /**< (CAN_IE) Tx Event FIFO Full Interrupt Enable Mask */
#define CAN_IE_TEFFE(value)                   (CAN_IE_TEFFE_Msk & ((value) << CAN_IE_TEFFE_Pos))
#define CAN_IE_TEFLE_Pos                      (15U)                                          /**< (CAN_IE) Tx Event FIFO Element Lost Interrupt Enable Position */
#define CAN_IE_TEFLE_Msk                      (0x1U << CAN_IE_TEFLE_Pos)                     /**< (CAN_IE) Tx Event FIFO Element Lost Interrupt Enable Mask */
#define CAN_IE_TEFLE(value)                   (CAN_IE_TEFLE_Msk & ((value) << CAN_IE_TEFLE_Pos))
#define CAN_IE_TSWE_Pos                       (16U)                                          /**< (CAN_IE) Timestamp Wraparound Interrupt Enable Position */
#define CAN_IE_TSWE_Msk                       (0x1U << CAN_IE_TSWE_Pos)                      /**< (CAN_IE) Timestamp Wraparound Interrupt Enable Mask */
#define CAN_IE_TSWE(value)                    (CAN_IE_TSWE_Msk & ((value) << CAN_IE_TSWE_Pos))
#define CAN_IE_MRAFE_Pos                      (17U)                                          /**< (CAN_IE) Message RAM Access Failure Interrupt Enable Position */
#define CAN_IE_MRAFE_Msk                      (0x1U << CAN_IE_MRAFE_Pos)                     /**< (CAN_IE) Message RAM Access Failure Interrupt Enable Mask */
#define CAN_IE_MRAFE(value)                   (CAN_IE_MRAFE_Msk & ((value) << CAN_IE_MRAFE_Pos))
#define CAN_IE_TOOE_Pos                       (18U)                                          /**< (CAN_IE) Timeout Occurred Interrupt Enable Position */
#define CAN_IE_TOOE_Msk                       (0x1U << CAN_IE_TOOE_Pos)                      /**< (CAN_IE) Timeout Occurred Interrupt Enable Mask */
#define CAN_IE_TOOE(value)                    (CAN_IE_TOOE_Msk & ((value) << CAN_IE_TOOE_Pos))
#define CAN_IE_DRXE_Pos                       (19U)                                          /**< (CAN_IE) Message stored to Dedicated Rx Buffer Interrupt Enable Position */
#define CAN_IE_DRXE_Msk                       (0x1U << CAN_IE_DRXE_Pos)                      /**< (CAN_IE) Message stored to Dedicated Rx Buffer Interrupt Enable Mask */
#define CAN_IE_DRXE(value)                    (CAN_IE_DRXE_Msk & ((value) << CAN_IE_DRXE_Pos))
#define CAN_IE_BECE_Pos                       (20U)                                          /**< (CAN_IE) Bit Error Corrected Interrupt Enable Position */
#define CAN_IE_BECE_Msk                       (0x1U << CAN_IE_BECE_Pos)                      /**< (CAN_IE) Bit Error Corrected Interrupt Enable Mask */
#define CAN_IE_BECE(value)                    (CAN_IE_BECE_Msk & ((value) << CAN_IE_BECE_Pos))
#define CAN_IE_BEUE_Pos                       (21U)                                          /**< (CAN_IE) Bit Error Uncorrected Interrupt Enable Position */
#define CAN_IE_BEUE_Msk                       (0x1U << CAN_IE_BEUE_Pos)                      /**< (CAN_IE) Bit Error Uncorrected Interrupt Enable Mask */
#define CAN_IE_BEUE(value)                    (CAN_IE_BEUE_Msk & ((value) << CAN_IE_BEUE_Pos))
#define CAN_IE_ELOE_Pos                       (22U)                                          /**< (CAN_IE) Error Logging Overflow Interrupt Enable Position */
#define CAN_IE_ELOE_Msk                       (0x1U << CAN_IE_ELOE_Pos)                      /**< (CAN_IE) Error Logging Overflow Interrupt Enable Mask */
#define CAN_IE_ELOE(value)                    (CAN_IE_ELOE_Msk & ((value) << CAN_IE_ELOE_Pos))
#define CAN_IE_EPE_Pos                        (23U)                                          /**< (CAN_IE) Error Passive Interrupt Enable Position */
#define CAN_IE_EPE_Msk                        (0x1U << CAN_IE_EPE_Pos)                       /**< (CAN_IE) Error Passive Interrupt Enable Mask */
#define CAN_IE_EPE(value)                     (CAN_IE_EPE_Msk & ((value) << CAN_IE_EPE_Pos))
#define CAN_IE_EWE_Pos                        (24U)                                          /**< (CAN_IE) Warning Status Interrupt Enable Position */
#define CAN_IE_EWE_Msk                        (0x1U << CAN_IE_EWE_Pos)                       /**< (CAN_IE) Warning Status Interrupt Enable Mask */
#define CAN_IE_EWE(value)                     (CAN_IE_EWE_Msk & ((value) << CAN_IE_EWE_Pos))
#define CAN_IE_BOE_Pos                        (25U)                                          /**< (CAN_IE) Bus_Off Status Interrupt Enable Position */
#define CAN_IE_BOE_Msk                        (0x1U << CAN_IE_BOE_Pos)                       /**< (CAN_IE) Bus_Off Status Interrupt Enable Mask */
#define CAN_IE_BOE(value)                     (CAN_IE_BOE_Msk & ((value) << CAN_IE_BOE_Pos))
#define CAN_IE_WDIE_Pos                       (26U)                                          /**< (CAN_IE) Watchdog Interrupt Interrupt Enable Position */
#define CAN_IE_WDIE_Msk                       (0x1U << CAN_IE_WDIE_Pos)                      /**< (CAN_IE) Watchdog Interrupt Interrupt Enable Mask */
#define CAN_IE_WDIE(value)                    (CAN_IE_WDIE_Msk & ((value) << CAN_IE_WDIE_Pos))
#define CAN_IE_PEAE_Pos                       (27U)                                          /**< (CAN_IE) Protocol Error in Arbitration Phase Enable Position */
#define CAN_IE_PEAE_Msk                       (0x1U << CAN_IE_PEAE_Pos)                      /**< (CAN_IE) Protocol Error in Arbitration Phase Enable Mask */
#define CAN_IE_PEAE(value)                    (CAN_IE_PEAE_Msk & ((value) << CAN_IE_PEAE_Pos))
#define CAN_IE_PEDE_Pos                       (28U)                                          /**< (CAN_IE) Protocol Error in Data Phase Enable Position */
#define CAN_IE_PEDE_Msk                       (0x1U << CAN_IE_PEDE_Pos)                      /**< (CAN_IE) Protocol Error in Data Phase Enable Mask */
#define CAN_IE_PEDE(value)                    (CAN_IE_PEDE_Msk & ((value) << CAN_IE_PEDE_Pos))
#define CAN_IE_ARAE_Pos                       (29U)                                          /**< (CAN_IE) Access to Reserved Address Enable Position */
#define CAN_IE_ARAE_Msk                       (0x1U << CAN_IE_ARAE_Pos)                      /**< (CAN_IE) Access to Reserved Address Enable Mask */
#define CAN_IE_ARAE(value)                    (CAN_IE_ARAE_Msk & ((value) << CAN_IE_ARAE_Pos))
#define CAN_IE_Msk                            (0x3FFFFFFFUL)                                 /**< (CAN_IE) Register Mask  */

/* -------- CAN_ILS : (CAN Offset: 0x58) (R/W 32) Interrupt Line Select -------- */
#define CAN_ILS_RF0NL_Pos                     (0U)                                           /**< (CAN_ILS) Rx FIFO 0 New Message Interrupt Line Position */
#define CAN_ILS_RF0NL_Msk                     (0x1U << CAN_ILS_RF0NL_Pos)                    /**< (CAN_ILS) Rx FIFO 0 New Message Interrupt Line Mask */
#define CAN_ILS_RF0NL(value)                  (CAN_ILS_RF0NL_Msk & ((value) << CAN_ILS_RF0NL_Pos))
#define CAN_ILS_RF0WL_Pos                     (1U)                                           /**< (CAN_ILS) Rx FIFO 0 Watermark Reached Interrupt Line Position */
#define CAN_ILS_RF0WL_Msk                     (0x1U << CAN_ILS_RF0WL_Pos)                    /**< (CAN_ILS) Rx FIFO 0 Watermark Reached Interrupt Line Mask */
#define CAN_ILS_RF0WL(value)                  (CAN_ILS_RF0WL_Msk & ((value) << CAN_ILS_RF0WL_Pos))
#define CAN_ILS_RF0FL_Pos                     (2U)                                           /**< (CAN_ILS) Rx FIFO 0 Full Interrupt Line Position */
#define CAN_ILS_RF0FL_Msk                     (0x1U << CAN_ILS_RF0FL_Pos)                    /**< (CAN_ILS) Rx FIFO 0 Full Interrupt Line Mask */
#define CAN_ILS_RF0FL(value)                  (CAN_ILS_RF0FL_Msk & ((value) << CAN_ILS_RF0FL_Pos))
#define CAN_ILS_RF0LL_Pos                     (3U)                                           /**< (CAN_ILS) Rx FIFO 0 Message Lost Interrupt Line Position */
#define CAN_ILS_RF0LL_Msk                     (0x1U << CAN_ILS_RF0LL_Pos)                    /**< (CAN_ILS) Rx FIFO 0 Message Lost Interrupt Line Mask */
#define CAN_ILS_RF0LL(value)                  (CAN_ILS_RF0LL_Msk & ((value) << CAN_ILS_RF0LL_Pos))
#define CAN_ILS_RF1NL_Pos                     (4U)                                           /**< (CAN_ILS) Rx FIFO 1 New Message Interrupt Line Position */
#define CAN_ILS_RF1NL_Msk                     (0x1U << CAN_ILS_RF1NL_Pos)                    /**< (CAN_ILS) Rx FIFO 1 New Message Interrupt Line Mask */
#define CAN_ILS_RF1NL(value)                  (CAN_ILS_RF1NL_Msk & ((value) << CAN_ILS_RF1NL_Pos))
#define CAN_ILS_RF1WL_Pos                     (5U)                                           /**< (CAN_ILS) Rx FIFO 1 Watermark Reached Interrupt Line Position */
#define CAN_ILS_RF1WL_Msk                     (0x1U << CAN_ILS_RF1WL_Pos)                    /**< (CAN_ILS) Rx FIFO 1 Watermark Reached Interrupt Line Mask */
#define CAN_ILS_RF1WL(value)                  (CAN_ILS_RF1WL_Msk & ((value) << CAN_ILS_RF1WL_Pos))
#define CAN_ILS_RF1FL_Pos                     (6U)                                           /**< (CAN_ILS) Rx FIFO 1 FIFO Full Interrupt Line Position */
#define CAN_ILS_RF1FL_Msk                     (0x1U << CAN_ILS_RF1FL_Pos)                    /**< (CAN_ILS) Rx FIFO 1 FIFO Full Interrupt Line Mask */
#define CAN_ILS_RF1FL(value)                  (CAN_ILS_RF1FL_Msk & ((value) << CAN_ILS_RF1FL_Pos))
#define CAN_ILS_RF1LL_Pos                     (7U)                                           /**< (CAN_ILS) Rx FIFO 1 Message Lost Interrupt Line Position */
#define CAN_ILS_RF1LL_Msk                     (0x1U << CAN_ILS_RF1LL_Pos)                    /**< (CAN_ILS) Rx FIFO 1 Message Lost Interrupt Line Mask */
#define CAN_ILS_RF1LL(value)                  (CAN_ILS_RF1LL_Msk & ((value) << CAN_ILS_RF1LL_Pos))
#define CAN_ILS_HPML_Pos                      (8U)                                           /**< (CAN_ILS) High Priority Message Interrupt Line Position */
#define CAN_ILS_HPML_Msk                      (0x1U << CAN_ILS_HPML_Pos)                     /**< (CAN_ILS) High Priority Message Interrupt Line Mask */
#define CAN_ILS_HPML(value)                   (CAN_ILS_HPML_Msk & ((value) << CAN_ILS_HPML_Pos))
#define CAN_ILS_TCL_Pos                       (9U)                                           /**< (CAN_ILS) Timestamp Completed Interrupt Line Position */
#define CAN_ILS_TCL_Msk                       (0x1U << CAN_ILS_TCL_Pos)                      /**< (CAN_ILS) Timestamp Completed Interrupt Line Mask */
#define CAN_ILS_TCL(value)                    (CAN_ILS_TCL_Msk & ((value) << CAN_ILS_TCL_Pos))
#define CAN_ILS_TCFL_Pos                      (10U)                                          /**< (CAN_ILS) Transmission Cancellation Finished Interrupt Line Position */
#define CAN_ILS_TCFL_Msk                      (0x1U << CAN_ILS_TCFL_Pos)                     /**< (CAN_ILS) Transmission Cancellation Finished Interrupt Line Mask */
#define CAN_ILS_TCFL(value)                   (CAN_ILS_TCFL_Msk & ((value) << CAN_ILS_TCFL_Pos))
#define CAN_ILS_TFEL_Pos                      (11U)                                          /**< (CAN_ILS) Tx FIFO Empty Interrupt Line Position */
#define CAN_ILS_TFEL_Msk                      (0x1U << CAN_ILS_TFEL_Pos)                     /**< (CAN_ILS) Tx FIFO Empty Interrupt Line Mask */
#define CAN_ILS_TFEL(value)                   (CAN_ILS_TFEL_Msk & ((value) << CAN_ILS_TFEL_Pos))
#define CAN_ILS_TEFNL_Pos                     (12U)                                          /**< (CAN_ILS) Tx Event FIFO New Entry Interrupt Line Position */
#define CAN_ILS_TEFNL_Msk                     (0x1U << CAN_ILS_TEFNL_Pos)                    /**< (CAN_ILS) Tx Event FIFO New Entry Interrupt Line Mask */
#define CAN_ILS_TEFNL(value)                  (CAN_ILS_TEFNL_Msk & ((value) << CAN_ILS_TEFNL_Pos))
#define CAN_ILS_TEFWL_Pos                     (13U)                                          /**< (CAN_ILS) Tx Event FIFO Watermark Reached Interrupt Line Position */
#define CAN_ILS_TEFWL_Msk                     (0x1U << CAN_ILS_TEFWL_Pos)                    /**< (CAN_ILS) Tx Event FIFO Watermark Reached Interrupt Line Mask */
#define CAN_ILS_TEFWL(value)                  (CAN_ILS_TEFWL_Msk & ((value) << CAN_ILS_TEFWL_Pos))
#define CAN_ILS_TEFFL_Pos                     (14U)                                          /**< (CAN_ILS) Tx Event FIFO Full Interrupt Line Position */
#define CAN_ILS_TEFFL_Msk                     (0x1U << CAN_ILS_TEFFL_Pos)                    /**< (CAN_ILS) Tx Event FIFO Full Interrupt Line Mask */
#define CAN_ILS_TEFFL(value)                  (CAN_ILS_TEFFL_Msk & ((value) << CAN_ILS_TEFFL_Pos))
#define CAN_ILS_TEFLL_Pos                     (15U)                                          /**< (CAN_ILS) Tx Event FIFO Element Lost Interrupt Line Position */
#define CAN_ILS_TEFLL_Msk                     (0x1U << CAN_ILS_TEFLL_Pos)                    /**< (CAN_ILS) Tx Event FIFO Element Lost Interrupt Line Mask */
#define CAN_ILS_TEFLL(value)                  (CAN_ILS_TEFLL_Msk & ((value) << CAN_ILS_TEFLL_Pos))
#define CAN_ILS_TSWL_Pos                      (16U)                                          /**< (CAN_ILS) Timestamp Wraparound Interrupt Line Position */
#define CAN_ILS_TSWL_Msk                      (0x1U << CAN_ILS_TSWL_Pos)                     /**< (CAN_ILS) Timestamp Wraparound Interrupt Line Mask */
#define CAN_ILS_TSWL(value)                   (CAN_ILS_TSWL_Msk & ((value) << CAN_ILS_TSWL_Pos))
#define CAN_ILS_MRAFL_Pos                     (17U)                                          /**< (CAN_ILS) Message RAM Access Failure Interrupt Line Position */
#define CAN_ILS_MRAFL_Msk                     (0x1U << CAN_ILS_MRAFL_Pos)                    /**< (CAN_ILS) Message RAM Access Failure Interrupt Line Mask */
#define CAN_ILS_MRAFL(value)                  (CAN_ILS_MRAFL_Msk & ((value) << CAN_ILS_MRAFL_Pos))
#define CAN_ILS_TOOL_Pos                      (18U)                                          /**< (CAN_ILS) Timeout Occurred Interrupt Line Position */
#define CAN_ILS_TOOL_Msk                      (0x1U << CAN_ILS_TOOL_Pos)                     /**< (CAN_ILS) Timeout Occurred Interrupt Line Mask */
#define CAN_ILS_TOOL(value)                   (CAN_ILS_TOOL_Msk & ((value) << CAN_ILS_TOOL_Pos))
#define CAN_ILS_DRXL_Pos                      (19U)                                          /**< (CAN_ILS) Message stored to Dedicated Rx Buffer Interrupt Line Position */
#define CAN_ILS_DRXL_Msk                      (0x1U << CAN_ILS_DRXL_Pos)                     /**< (CAN_ILS) Message stored to Dedicated Rx Buffer Interrupt Line Mask */
#define CAN_ILS_DRXL(value)                   (CAN_ILS_DRXL_Msk & ((value) << CAN_ILS_DRXL_Pos))
#define CAN_ILS_BECL_Pos                      (20U)                                          /**< (CAN_ILS) Bit Error Corrected Interrupt Line Position */
#define CAN_ILS_BECL_Msk                      (0x1U << CAN_ILS_BECL_Pos)                     /**< (CAN_ILS) Bit Error Corrected Interrupt Line Mask */
#define CAN_ILS_BECL(value)                   (CAN_ILS_BECL_Msk & ((value) << CAN_ILS_BECL_Pos))
#define CAN_ILS_BEUL_Pos                      (21U)                                          /**< (CAN_ILS) Bit Error Uncorrected Interrupt Line Position */
#define CAN_ILS_BEUL_Msk                      (0x1U << CAN_ILS_BEUL_Pos)                     /**< (CAN_ILS) Bit Error Uncorrected Interrupt Line Mask */
#define CAN_ILS_BEUL(value)                   (CAN_ILS_BEUL_Msk & ((value) << CAN_ILS_BEUL_Pos))
#define CAN_ILS_ELOL_Pos                      (22U)                                          /**< (CAN_ILS) Error Logging Overflow Interrupt Line Position */
#define CAN_ILS_ELOL_Msk                      (0x1U << CAN_ILS_ELOL_Pos)                     /**< (CAN_ILS) Error Logging Overflow Interrupt Line Mask */
#define CAN_ILS_ELOL(value)                   (CAN_ILS_ELOL_Msk & ((value) << CAN_ILS_ELOL_Pos))
#define CAN_ILS_EPL_Pos                       (23U)                                          /**< (CAN_ILS) Error Passive Interrupt Line Position */
#define CAN_ILS_EPL_Msk                       (0x1U << CAN_ILS_EPL_Pos)                      /**< (CAN_ILS) Error Passive Interrupt Line Mask */
#define CAN_ILS_EPL(value)                    (CAN_ILS_EPL_Msk & ((value) << CAN_ILS_EPL_Pos))
#define CAN_ILS_EWL_Pos                       (24U)                                          /**< (CAN_ILS) Warning Status Interrupt Line Position */
#define CAN_ILS_EWL_Msk                       (0x1U << CAN_ILS_EWL_Pos)                      /**< (CAN_ILS) Warning Status Interrupt Line Mask */
#define CAN_ILS_EWL(value)                    (CAN_ILS_EWL_Msk & ((value) << CAN_ILS_EWL_Pos))
#define CAN_ILS_BOL_Pos                       (25U)                                          /**< (CAN_ILS) Bus_Off Status Interrupt Line Position */
#define CAN_ILS_BOL_Msk                       (0x1U << CAN_ILS_BOL_Pos)                      /**< (CAN_ILS) Bus_Off Status Interrupt Line Mask */
#define CAN_ILS_BOL(value)                    (CAN_ILS_BOL_Msk & ((value) << CAN_ILS_BOL_Pos))
#define CAN_ILS_WDIL_Pos                      (26U)                                          /**< (CAN_ILS) Watchdog Interrupt Interrupt Line Position */
#define CAN_ILS_WDIL_Msk                      (0x1U << CAN_ILS_WDIL_Pos)                     /**< (CAN_ILS) Watchdog Interrupt Interrupt Line Mask */
#define CAN_ILS_WDIL(value)                   (CAN_ILS_WDIL_Msk & ((value) << CAN_ILS_WDIL_Pos))
#define CAN_ILS_PEAL_Pos                      (27U)                                          /**< (CAN_ILS) Protocol Error in Arbitration Phase Line Position */
#define CAN_ILS_PEAL_Msk                      (0x1U << CAN_ILS_PEAL_Pos)                     /**< (CAN_ILS) Protocol Error in Arbitration Phase Line Mask */
#define CAN_ILS_PEAL(value)                   (CAN_ILS_PEAL_Msk & ((value) << CAN_ILS_PEAL_Pos))
#define CAN_ILS_PEDL_Pos                      (28U)                                          /**< (CAN_ILS) Protocol Error in Data Phase Line Position */
#define CAN_ILS_PEDL_Msk                      (0x1U << CAN_ILS_PEDL_Pos)                     /**< (CAN_ILS) Protocol Error in Data Phase Line Mask */
#define CAN_ILS_PEDL(value)                   (CAN_ILS_PEDL_Msk & ((value) << CAN_ILS_PEDL_Pos))
#define CAN_ILS_ARAL_Pos                      (29U)                                          /**< (CAN_ILS) Access to Reserved Address Line Position */
#define CAN_ILS_ARAL_Msk                      (0x1U << CAN_ILS_ARAL_Pos)                     /**< (CAN_ILS) Access to Reserved Address Line Mask */
#define CAN_ILS_ARAL(value)                   (CAN_ILS_ARAL_Msk & ((value) << CAN_ILS_ARAL_Pos))
#define CAN_ILS_Msk                           (0x3FFFFFFFUL)                                 /**< (CAN_ILS) Register Mask  */

/* -------- CAN_ILE : (CAN Offset: 0x5C) (R/W 32) Interrupt Line Enable -------- */
#define CAN_ILE_EINT0_Pos                     (0U)                                           /**< (CAN_ILE) Enable Interrupt Line 0 Position */
#define CAN_ILE_EINT0_Msk                     (0x1U << CAN_ILE_EINT0_Pos)                    /**< (CAN_ILE) Enable Interrupt Line 0 Mask */
#define CAN_ILE_EINT0(value)                  (CAN_ILE_EINT0_Msk & ((value) << CAN_ILE_EINT0_Pos))
#define CAN_ILE_EINT1_Pos                     (1U)                                           /**< (CAN_ILE) Enable Interrupt Line 1 Position */
#define CAN_ILE_EINT1_Msk                     (0x1U << CAN_ILE_EINT1_Pos)                    /**< (CAN_ILE) Enable Interrupt Line 1 Mask */
#define CAN_ILE_EINT1(value)                  (CAN_ILE_EINT1_Msk & ((value) << CAN_ILE_EINT1_Pos))
#define CAN_ILE_Msk                           (0x00000003UL)                                 /**< (CAN_ILE) Register Mask  */

/* -------- CAN_GFC : (CAN Offset: 0x80) (R/W 32) Global Filter Configuration -------- */
#define CAN_GFC_RRFE_Pos                      (0U)                                           /**< (CAN_GFC) Reject Remote Frames Extended Position */
#define CAN_GFC_RRFE_Msk                      (0x1U << CAN_GFC_RRFE_Pos)                     /**< (CAN_GFC) Reject Remote Frames Extended Mask */
#define CAN_GFC_RRFE(value)                   (CAN_GFC_RRFE_Msk & ((value) << CAN_GFC_RRFE_Pos))
#define CAN_GFC_RRFS_Pos                      (1U)                                           /**< (CAN_GFC) Reject Remote Frames Standard Position */
#define CAN_GFC_RRFS_Msk                      (0x1U << CAN_GFC_RRFS_Pos)                     /**< (CAN_GFC) Reject Remote Frames Standard Mask */
#define CAN_GFC_RRFS(value)                   (CAN_GFC_RRFS_Msk & ((value) << CAN_GFC_RRFS_Pos))
#define CAN_GFC_ANFE_Pos                      (2U)                                           /**< (CAN_GFC) Accept Non-matching Frames Extended Position */
#define CAN_GFC_ANFE_Msk                      (0x3U << CAN_GFC_ANFE_Pos)                     /**< (CAN_GFC) Accept Non-matching Frames Extended Mask */
#define CAN_GFC_ANFE(value)                   (CAN_GFC_ANFE_Msk & ((value) << CAN_GFC_ANFE_Pos))
#define   CAN_GFC_ANFE_RXF0_Val               (0U)                                           /**< (CAN_GFC) Accept in Rx FIFO 0  */
#define   CAN_GFC_ANFE_RXF1_Val               (1U)                                           /**< (CAN_GFC) Accept in Rx FIFO 1  */
#define   CAN_GFC_ANFE_REJECT_Val             (2U)                                           /**< (CAN_GFC) Reject  */
#define CAN_GFC_ANFE_RXF0                     (CAN_GFC_ANFE_RXF0_Val << CAN_GFC_ANFE_Pos)    /**< (CAN_GFC) Accept in Rx FIFO 0 Position  */
#define CAN_GFC_ANFE_RXF1                     (CAN_GFC_ANFE_RXF1_Val << CAN_GFC_ANFE_Pos)    /**< (CAN_GFC) Accept in Rx FIFO 1 Position  */
#define CAN_GFC_ANFE_REJECT                   (CAN_GFC_ANFE_REJECT_Val << CAN_GFC_ANFE_Pos)  /**< (CAN_GFC) Reject Position  */
#define CAN_GFC_ANFS_Pos                      (4U)                                           /**< (CAN_GFC) Accept Non-matching Frames Standard Position */
#define CAN_GFC_ANFS_Msk                      (0x3U << CAN_GFC_ANFS_Pos)                     /**< (CAN_GFC) Accept Non-matching Frames Standard Mask */
#define CAN_GFC_ANFS(value)                   (CAN_GFC_ANFS_Msk & ((value) << CAN_GFC_ANFS_Pos))
#define   CAN_GFC_ANFS_RXF0_Val               (0U)                                           /**< (CAN_GFC) Accept in Rx FIFO 0  */
#define   CAN_GFC_ANFS_RXF1_Val               (1U)                                           /**< (CAN_GFC) Accept in Rx FIFO 1  */
#define   CAN_GFC_ANFS_REJECT_Val             (2U)                                           /**< (CAN_GFC) Reject  */
#define CAN_GFC_ANFS_RXF0                     (CAN_GFC_ANFS_RXF0_Val << CAN_GFC_ANFS_Pos)    /**< (CAN_GFC) Accept in Rx FIFO 0 Position  */
#define CAN_GFC_ANFS_RXF1                     (CAN_GFC_ANFS_RXF1_Val << CAN_GFC_ANFS_Pos)    /**< (CAN_GFC) Accept in Rx FIFO 1 Position  */
#define CAN_GFC_ANFS_REJECT                   (CAN_GFC_ANFS_REJECT_Val << CAN_GFC_ANFS_Pos)  /**< (CAN_GFC) Reject Position  */
#define CAN_GFC_Msk                           (0x0000003FUL)                                 /**< (CAN_GFC) Register Mask  */

/* -------- CAN_SIDFC : (CAN Offset: 0x84) (R/W 32) Standard ID Filter Configuration -------- */
#define CAN_SIDFC_FLSSA_Pos                   (0U)                                           /**< (CAN_SIDFC) Filter List Standard Start Address Position */
#define CAN_SIDFC_FLSSA_Msk                   (0xFFFFU << CAN_SIDFC_FLSSA_Pos)               /**< (CAN_SIDFC) Filter List Standard Start Address Mask */
#define CAN_SIDFC_FLSSA(value)                (CAN_SIDFC_FLSSA_Msk & ((value) << CAN_SIDFC_FLSSA_Pos))
#define CAN_SIDFC_LSS_Pos                     (16U)                                          /**< (CAN_SIDFC) List Size Standard Position */
#define CAN_SIDFC_LSS_Msk                     (0xFFU << CAN_SIDFC_LSS_Pos)                   /**< (CAN_SIDFC) List Size Standard Mask */
#define CAN_SIDFC_LSS(value)                  (CAN_SIDFC_LSS_Msk & ((value) << CAN_SIDFC_LSS_Pos))
#define CAN_SIDFC_Msk                         (0x00FFFFFFUL)                                 /**< (CAN_SIDFC) Register Mask  */

/* -------- CAN_XIDFC : (CAN Offset: 0x88) (R/W 32) Extended ID Filter Configuration -------- */
#define CAN_XIDFC_FLESA_Pos                   (0U)                                           /**< (CAN_XIDFC) Filter List Extended Start Address Position */
#define CAN_XIDFC_FLESA_Msk                   (0xFFFFU << CAN_XIDFC_FLESA_Pos)               /**< (CAN_XIDFC) Filter List Extended Start Address Mask */
#define CAN_XIDFC_FLESA(value)                (CAN_XIDFC_FLESA_Msk & ((value) << CAN_XIDFC_FLESA_Pos))
#define CAN_XIDFC_LSE_Pos                     (16U)                                          /**< (CAN_XIDFC) List Size Extended Position */
#define CAN_XIDFC_LSE_Msk                     (0x7FU << CAN_XIDFC_LSE_Pos)                   /**< (CAN_XIDFC) List Size Extended Mask */
#define CAN_XIDFC_LSE(value)                  (CAN_XIDFC_LSE_Msk & ((value) << CAN_XIDFC_LSE_Pos))
#define CAN_XIDFC_Msk                         (0x007FFFFFUL)                                 /**< (CAN_XIDFC) Register Mask  */

/* -------- CAN_XIDAM : (CAN Offset: 0x90) (R/W 32) Extended ID AND Mask -------- */
#define CAN_XIDAM_EIDM_Pos                    (0U)                                           /**< (CAN_XIDAM) Extended ID Mask Position */
#define CAN_XIDAM_EIDM_Msk                    (0x1FFFFFFFU << CAN_XIDAM_EIDM_Pos)            /**< (CAN_XIDAM) Extended ID Mask Mask */
#define CAN_XIDAM_EIDM(value)                 (CAN_XIDAM_EIDM_Msk & ((value) << CAN_XIDAM_EIDM_Pos))
#define CAN_XIDAM_Msk                         (0x1FFFFFFFUL)                                 /**< (CAN_XIDAM) Register Mask  */

/* -------- CAN_HPMS : (CAN Offset: 0x94) (R/  32) High Priority Message Status -------- */
#define CAN_HPMS_BIDX_Pos                     (0U)                                           /**< (CAN_HPMS) Buffer Index Position */
#define CAN_HPMS_BIDX_Msk                     (0x3FU << CAN_HPMS_BIDX_Pos)                   /**< (CAN_HPMS) Buffer Index Mask */
#define CAN_HPMS_BIDX(value)                  (CAN_HPMS_BIDX_Msk & ((value) << CAN_HPMS_BIDX_Pos))
#define CAN_HPMS_MSI_Pos                      (6U)                                           /**< (CAN_HPMS) Message Storage Indicator Position */
#define CAN_HPMS_MSI_Msk                      (0x3U << CAN_HPMS_MSI_Pos)                     /**< (CAN_HPMS) Message Storage Indicator Mask */
#define CAN_HPMS_MSI(value)                   (CAN_HPMS_MSI_Msk & ((value) << CAN_HPMS_MSI_Pos))
#define   CAN_HPMS_MSI_NONE_Val               (0U)                                           /**< (CAN_HPMS) No FIFO selected  */
#define   CAN_HPMS_MSI_LOST_Val               (1U)                                           /**< (CAN_HPMS) FIFO message lost  */
#define   CAN_HPMS_MSI_FIFO0_Val              (2U)                                           /**< (CAN_HPMS) Message stored in FIFO 0  */
#define   CAN_HPMS_MSI_FIFO1_Val              (3U)                                           /**< (CAN_HPMS) Message stored in FIFO 1  */
#define CAN_HPMS_MSI_NONE                     (CAN_HPMS_MSI_NONE_Val << CAN_HPMS_MSI_Pos)    /**< (CAN_HPMS) No FIFO selected Position  */
#define CAN_HPMS_MSI_LOST                     (CAN_HPMS_MSI_LOST_Val << CAN_HPMS_MSI_Pos)    /**< (CAN_HPMS) FIFO message lost Position  */
#define CAN_HPMS_MSI_FIFO0                    (CAN_HPMS_MSI_FIFO0_Val << CAN_HPMS_MSI_Pos)   /**< (CAN_HPMS) Message stored in FIFO 0 Position  */
#define CAN_HPMS_MSI_FIFO1                    (CAN_HPMS_MSI_FIFO1_Val << CAN_HPMS_MSI_Pos)   /**< (CAN_HPMS) Message stored in FIFO 1 Position  */
#define CAN_HPMS_FIDX_Pos                     (8U)                                           /**< (CAN_HPMS) Filter Index Position */
#define CAN_HPMS_FIDX_Msk                     (0x7FU << CAN_HPMS_FIDX_Pos)                   /**< (CAN_HPMS) Filter Index Mask */
#define CAN_HPMS_FIDX(value)                  (CAN_HPMS_FIDX_Msk & ((value) << CAN_HPMS_FIDX_Pos))
#define CAN_HPMS_FLST_Pos                     (15U)                                          /**< (CAN_HPMS) Filter List Position */
#define CAN_HPMS_FLST_Msk                     (0x1U << CAN_HPMS_FLST_Pos)                    /**< (CAN_HPMS) Filter List Mask */
#define CAN_HPMS_FLST(value)                  (CAN_HPMS_FLST_Msk & ((value) << CAN_HPMS_FLST_Pos))
#define CAN_HPMS_Msk                          (0x0000FFFFUL)                                 /**< (CAN_HPMS) Register Mask  */

/* -------- CAN_NDAT1 : (CAN Offset: 0x98) (R/W 32) New Data 1 -------- */
#define CAN_NDAT1_ND0_Pos                     (0U)                                           /**< (CAN_NDAT1) New Data 0 Position */
#define CAN_NDAT1_ND0_Msk                     (0x1U << CAN_NDAT1_ND0_Pos)                    /**< (CAN_NDAT1) New Data 0 Mask */
#define CAN_NDAT1_ND0(value)                  (CAN_NDAT1_ND0_Msk & ((value) << CAN_NDAT1_ND0_Pos))
#define CAN_NDAT1_ND1_Pos                     (1U)                                           /**< (CAN_NDAT1) New Data 1 Position */
#define CAN_NDAT1_ND1_Msk                     (0x1U << CAN_NDAT1_ND1_Pos)                    /**< (CAN_NDAT1) New Data 1 Mask */
#define CAN_NDAT1_ND1(value)                  (CAN_NDAT1_ND1_Msk & ((value) << CAN_NDAT1_ND1_Pos))
#define CAN_NDAT1_ND2_Pos                     (2U)                                           /**< (CAN_NDAT1) New Data 2 Position */
#define CAN_NDAT1_ND2_Msk                     (0x1U << CAN_NDAT1_ND2_Pos)                    /**< (CAN_NDAT1) New Data 2 Mask */
#define CAN_NDAT1_ND2(value)                  (CAN_NDAT1_ND2_Msk & ((value) << CAN_NDAT1_ND2_Pos))
#define CAN_NDAT1_ND3_Pos                     (3U)                                           /**< (CAN_NDAT1) New Data 3 Position */
#define CAN_NDAT1_ND3_Msk                     (0x1U << CAN_NDAT1_ND3_Pos)                    /**< (CAN_NDAT1) New Data 3 Mask */
#define CAN_NDAT1_ND3(value)                  (CAN_NDAT1_ND3_Msk & ((value) << CAN_NDAT1_ND3_Pos))
#define CAN_NDAT1_ND4_Pos                     (4U)                                           /**< (CAN_NDAT1) New Data 4 Position */
#define CAN_NDAT1_ND4_Msk                     (0x1U << CAN_NDAT1_ND4_Pos)                    /**< (CAN_NDAT1) New Data 4 Mask */
#define CAN_NDAT1_ND4(value)                  (CAN_NDAT1_ND4_Msk & ((value) << CAN_NDAT1_ND4_Pos))
#define CAN_NDAT1_ND5_Pos                     (5U)                                           /**< (CAN_NDAT1) New Data 5 Position */
#define CAN_NDAT1_ND5_Msk                     (0x1U << CAN_NDAT1_ND5_Pos)                    /**< (CAN_NDAT1) New Data 5 Mask */
#define CAN_NDAT1_ND5(value)                  (CAN_NDAT1_ND5_Msk & ((value) << CAN_NDAT1_ND5_Pos))
#define CAN_NDAT1_ND6_Pos                     (6U)                                           /**< (CAN_NDAT1) New Data 6 Position */
#define CAN_NDAT1_ND6_Msk                     (0x1U << CAN_NDAT1_ND6_Pos)                    /**< (CAN_NDAT1) New Data 6 Mask */
#define CAN_NDAT1_ND6(value)                  (CAN_NDAT1_ND6_Msk & ((value) << CAN_NDAT1_ND6_Pos))
#define CAN_NDAT1_ND7_Pos                     (7U)                                           /**< (CAN_NDAT1) New Data 7 Position */
#define CAN_NDAT1_ND7_Msk                     (0x1U << CAN_NDAT1_ND7_Pos)                    /**< (CAN_NDAT1) New Data 7 Mask */
#define CAN_NDAT1_ND7(value)                  (CAN_NDAT1_ND7_Msk & ((value) << CAN_NDAT1_ND7_Pos))
#define CAN_NDAT1_ND8_Pos                     (8U)                                           /**< (CAN_NDAT1) New Data 8 Position */
#define CAN_NDAT1_ND8_Msk                     (0x1U << CAN_NDAT1_ND8_Pos)                    /**< (CAN_NDAT1) New Data 8 Mask */
#define CAN_NDAT1_ND8(value)                  (CAN_NDAT1_ND8_Msk & ((value) << CAN_NDAT1_ND8_Pos))
#define CAN_NDAT1_ND9_Pos                     (9U)                                           /**< (CAN_NDAT1) New Data 9 Position */
#define CAN_NDAT1_ND9_Msk                     (0x1U << CAN_NDAT1_ND9_Pos)                    /**< (CAN_NDAT1) New Data 9 Mask */
#define CAN_NDAT1_ND9(value)                  (CAN_NDAT1_ND9_Msk & ((value) << CAN_NDAT1_ND9_Pos))
#define CAN_NDAT1_ND10_Pos                    (10U)                                          /**< (CAN_NDAT1) New Data 10 Position */
#define CAN_NDAT1_ND10_Msk                    (0x1U << CAN_NDAT1_ND10_Pos)                   /**< (CAN_NDAT1) New Data 10 Mask */
#define CAN_NDAT1_ND10(value)                 (CAN_NDAT1_ND10_Msk & ((value) << CAN_NDAT1_ND10_Pos))
#define CAN_NDAT1_ND11_Pos                    (11U)                                          /**< (CAN_NDAT1) New Data 11 Position */
#define CAN_NDAT1_ND11_Msk                    (0x1U << CAN_NDAT1_ND11_Pos)                   /**< (CAN_NDAT1) New Data 11 Mask */
#define CAN_NDAT1_ND11(value)                 (CAN_NDAT1_ND11_Msk & ((value) << CAN_NDAT1_ND11_Pos))
#define CAN_NDAT1_ND12_Pos                    (12U)                                          /**< (CAN_NDAT1) New Data 12 Position */
#define CAN_NDAT1_ND12_Msk                    (0x1U << CAN_NDAT1_ND12_Pos)                   /**< (CAN_NDAT1) New Data 12 Mask */
#define CAN_NDAT1_ND12(value)                 (CAN_NDAT1_ND12_Msk & ((value) << CAN_NDAT1_ND12_Pos))
#define CAN_NDAT1_ND13_Pos                    (13U)                                          /**< (CAN_NDAT1) New Data 13 Position */
#define CAN_NDAT1_ND13_Msk                    (0x1U << CAN_NDAT1_ND13_Pos)                   /**< (CAN_NDAT1) New Data 13 Mask */
#define CAN_NDAT1_ND13(value)                 (CAN_NDAT1_ND13_Msk & ((value) << CAN_NDAT1_ND13_Pos))
#define CAN_NDAT1_ND14_Pos                    (14U)                                          /**< (CAN_NDAT1) New Data 14 Position */
#define CAN_NDAT1_ND14_Msk                    (0x1U << CAN_NDAT1_ND14_Pos)                   /**< (CAN_NDAT1) New Data 14 Mask */
#define CAN_NDAT1_ND14(value)                 (CAN_NDAT1_ND14_Msk & ((value) << CAN_NDAT1_ND14_Pos))
#define CAN_NDAT1_ND15_Pos                    (15U)                                          /**< (CAN_NDAT1) New Data 15 Position */
#define CAN_NDAT1_ND15_Msk                    (0x1U << CAN_NDAT1_ND15_Pos)                   /**< (CAN_NDAT1) New Data 15 Mask */
#define CAN_NDAT1_ND15(value)                 (CAN_NDAT1_ND15_Msk & ((value) << CAN_NDAT1_ND15_Pos))
#define CAN_NDAT1_ND16_Pos                    (16U)                                          /**< (CAN_NDAT1) New Data 16 Position */
#define CAN_NDAT1_ND16_Msk                    (0x1U << CAN_NDAT1_ND16_Pos)                   /**< (CAN_NDAT1) New Data 16 Mask */
#define CAN_NDAT1_ND16(value)                 (CAN_NDAT1_ND16_Msk & ((value) << CAN_NDAT1_ND16_Pos))
#define CAN_NDAT1_ND17_Pos                    (17U)                                          /**< (CAN_NDAT1) New Data 17 Position */
#define CAN_NDAT1_ND17_Msk                    (0x1U << CAN_NDAT1_ND17_Pos)                   /**< (CAN_NDAT1) New Data 17 Mask */
#define CAN_NDAT1_ND17(value)                 (CAN_NDAT1_ND17_Msk & ((value) << CAN_NDAT1_ND17_Pos))
#define CAN_NDAT1_ND18_Pos                    (18U)                                          /**< (CAN_NDAT1) New Data 18 Position */
#define CAN_NDAT1_ND18_Msk                    (0x1U << CAN_NDAT1_ND18_Pos)                   /**< (CAN_NDAT1) New Data 18 Mask */
#define CAN_NDAT1_ND18(value)                 (CAN_NDAT1_ND18_Msk & ((value) << CAN_NDAT1_ND18_Pos))
#define CAN_NDAT1_ND19_Pos                    (19U)                                          /**< (CAN_NDAT1) New Data 19 Position */
#define CAN_NDAT1_ND19_Msk                    (0x1U << CAN_NDAT1_ND19_Pos)                   /**< (CAN_NDAT1) New Data 19 Mask */
#define CAN_NDAT1_ND19(value)                 (CAN_NDAT1_ND19_Msk & ((value) << CAN_NDAT1_ND19_Pos))
#define CAN_NDAT1_ND20_Pos                    (20U)                                          /**< (CAN_NDAT1) New Data 20 Position */
#define CAN_NDAT1_ND20_Msk                    (0x1U << CAN_NDAT1_ND20_Pos)                   /**< (CAN_NDAT1) New Data 20 Mask */
#define CAN_NDAT1_ND20(value)                 (CAN_NDAT1_ND20_Msk & ((value) << CAN_NDAT1_ND20_Pos))
#define CAN_NDAT1_ND21_Pos                    (21U)                                          /**< (CAN_NDAT1) New Data 21 Position */
#define CAN_NDAT1_ND21_Msk                    (0x1U << CAN_NDAT1_ND21_Pos)                   /**< (CAN_NDAT1) New Data 21 Mask */
#define CAN_NDAT1_ND21(value)                 (CAN_NDAT1_ND21_Msk & ((value) << CAN_NDAT1_ND21_Pos))
#define CAN_NDAT1_ND22_Pos                    (22U)                                          /**< (CAN_NDAT1) New Data 22 Position */
#define CAN_NDAT1_ND22_Msk                    (0x1U << CAN_NDAT1_ND22_Pos)                   /**< (CAN_NDAT1) New Data 22 Mask */
#define CAN_NDAT1_ND22(value)                 (CAN_NDAT1_ND22_Msk & ((value) << CAN_NDAT1_ND22_Pos))
#define CAN_NDAT1_ND23_Pos                    (23U)                                          /**< (CAN_NDAT1) New Data 23 Position */
#define CAN_NDAT1_ND23_Msk                    (0x1U << CAN_NDAT1_ND23_Pos)                   /**< (CAN_NDAT1) New Data 23 Mask */
#define CAN_NDAT1_ND23(value)                 (CAN_NDAT1_ND23_Msk & ((value) << CAN_NDAT1_ND23_Pos))
#define CAN_NDAT1_ND24_Pos                    (24U)                                          /**< (CAN_NDAT1) New Data 24 Position */
#define CAN_NDAT1_ND24_Msk                    (0x1U << CAN_NDAT1_ND24_Pos)                   /**< (CAN_NDAT1) New Data 24 Mask */
#define CAN_NDAT1_ND24(value)                 (CAN_NDAT1_ND24_Msk & ((value) << CAN_NDAT1_ND24_Pos))
#define CAN_NDAT1_ND25_Pos                    (25U)                                          /**< (CAN_NDAT1) New Data 25 Position */
#define CAN_NDAT1_ND25_Msk                    (0x1U << CAN_NDAT1_ND25_Pos)                   /**< (CAN_NDAT1) New Data 25 Mask */
#define CAN_NDAT1_ND25(value)                 (CAN_NDAT1_ND25_Msk & ((value) << CAN_NDAT1_ND25_Pos))
#define CAN_NDAT1_ND26_Pos                    (26U)                                          /**< (CAN_NDAT1) New Data 26 Position */
#define CAN_NDAT1_ND26_Msk                    (0x1U << CAN_NDAT1_ND26_Pos)                   /**< (CAN_NDAT1) New Data 26 Mask */
#define CAN_NDAT1_ND26(value)                 (CAN_NDAT1_ND26_Msk & ((value) << CAN_NDAT1_ND26_Pos))
#define CAN_NDAT1_ND27_Pos                    (27U)                                          /**< (CAN_NDAT1) New Data 27 Position */
#define CAN_NDAT1_ND27_Msk                    (0x1U << CAN_NDAT1_ND27_Pos)                   /**< (CAN_NDAT1) New Data 27 Mask */
#define CAN_NDAT1_ND27(value)                 (CAN_NDAT1_ND27_Msk & ((value) << CAN_NDAT1_ND27_Pos))
#define CAN_NDAT1_ND28_Pos                    (28U)                                          /**< (CAN_NDAT1) New Data 28 Position */
#define CAN_NDAT1_ND28_Msk                    (0x1U << CAN_NDAT1_ND28_Pos)                   /**< (CAN_NDAT1) New Data 28 Mask */
#define CAN_NDAT1_ND28(value)                 (CAN_NDAT1_ND28_Msk & ((value) << CAN_NDAT1_ND28_Pos))
#define CAN_NDAT1_ND29_Pos                    (29U)                                          /**< (CAN_NDAT1) New Data 29 Position */
#define CAN_NDAT1_ND29_Msk                    (0x1U << CAN_NDAT1_ND29_Pos)                   /**< (CAN_NDAT1) New Data 29 Mask */
#define CAN_NDAT1_ND29(value)                 (CAN_NDAT1_ND29_Msk & ((value) << CAN_NDAT1_ND29_Pos))
#define CAN_NDAT1_ND30_Pos                    (30U)                                          /**< (CAN_NDAT1) New Data 30 Position */
#define CAN_NDAT1_ND30_Msk                    (0x1U << CAN_NDAT1_ND30_Pos)                   /**< (CAN_NDAT1) New Data 30 Mask */
#define CAN_NDAT1_ND30(value)                 (CAN_NDAT1_ND30_Msk & ((value) << CAN_NDAT1_ND30_Pos))
#define CAN_NDAT1_ND31_Pos                    (31U)                                          /**< (CAN_NDAT1) New Data 31 Position */
#define CAN_NDAT1_ND31_Msk                    (0x1U << CAN_NDAT1_ND31_Pos)                   /**< (CAN_NDAT1) New Data 31 Mask */
#define CAN_NDAT1_ND31(value)                 (CAN_NDAT1_ND31_Msk & ((value) << CAN_NDAT1_ND31_Pos))
#define CAN_NDAT1_Msk                         (0xFFFFFFFFUL)                                 /**< (CAN_NDAT1) Register Mask  */

/* -------- CAN_NDAT2 : (CAN Offset: 0x9C) (R/W 32) New Data 2 -------- */
#define CAN_NDAT2_ND32_Pos                    (0U)                                           /**< (CAN_NDAT2) New Data 32 Position */
#define CAN_NDAT2_ND32_Msk                    (0x1U << CAN_NDAT2_ND32_Pos)                   /**< (CAN_NDAT2) New Data 32 Mask */
#define CAN_NDAT2_ND32(value)                 (CAN_NDAT2_ND32_Msk & ((value) << CAN_NDAT2_ND32_Pos))
#define CAN_NDAT2_ND33_Pos                    (1U)                                           /**< (CAN_NDAT2) New Data 33 Position */
#define CAN_NDAT2_ND33_Msk                    (0x1U << CAN_NDAT2_ND33_Pos)                   /**< (CAN_NDAT2) New Data 33 Mask */
#define CAN_NDAT2_ND33(value)                 (CAN_NDAT2_ND33_Msk & ((value) << CAN_NDAT2_ND33_Pos))
#define CAN_NDAT2_ND34_Pos                    (2U)                                           /**< (CAN_NDAT2) New Data 34 Position */
#define CAN_NDAT2_ND34_Msk                    (0x1U << CAN_NDAT2_ND34_Pos)                   /**< (CAN_NDAT2) New Data 34 Mask */
#define CAN_NDAT2_ND34(value)                 (CAN_NDAT2_ND34_Msk & ((value) << CAN_NDAT2_ND34_Pos))
#define CAN_NDAT2_ND35_Pos                    (3U)                                           /**< (CAN_NDAT2) New Data 35 Position */
#define CAN_NDAT2_ND35_Msk                    (0x1U << CAN_NDAT2_ND35_Pos)                   /**< (CAN_NDAT2) New Data 35 Mask */
#define CAN_NDAT2_ND35(value)                 (CAN_NDAT2_ND35_Msk & ((value) << CAN_NDAT2_ND35_Pos))
#define CAN_NDAT2_ND36_Pos                    (4U)                                           /**< (CAN_NDAT2) New Data 36 Position */
#define CAN_NDAT2_ND36_Msk                    (0x1U << CAN_NDAT2_ND36_Pos)                   /**< (CAN_NDAT2) New Data 36 Mask */
#define CAN_NDAT2_ND36(value)                 (CAN_NDAT2_ND36_Msk & ((value) << CAN_NDAT2_ND36_Pos))
#define CAN_NDAT2_ND37_Pos                    (5U)                                           /**< (CAN_NDAT2) New Data 37 Position */
#define CAN_NDAT2_ND37_Msk                    (0x1U << CAN_NDAT2_ND37_Pos)                   /**< (CAN_NDAT2) New Data 37 Mask */
#define CAN_NDAT2_ND37(value)                 (CAN_NDAT2_ND37_Msk & ((value) << CAN_NDAT2_ND37_Pos))
#define CAN_NDAT2_ND38_Pos                    (6U)                                           /**< (CAN_NDAT2) New Data 38 Position */
#define CAN_NDAT2_ND38_Msk                    (0x1U << CAN_NDAT2_ND38_Pos)                   /**< (CAN_NDAT2) New Data 38 Mask */
#define CAN_NDAT2_ND38(value)                 (CAN_NDAT2_ND38_Msk & ((value) << CAN_NDAT2_ND38_Pos))
#define CAN_NDAT2_ND39_Pos                    (7U)                                           /**< (CAN_NDAT2) New Data 39 Position */
#define CAN_NDAT2_ND39_Msk                    (0x1U << CAN_NDAT2_ND39_Pos)                   /**< (CAN_NDAT2) New Data 39 Mask */
#define CAN_NDAT2_ND39(value)                 (CAN_NDAT2_ND39_Msk & ((value) << CAN_NDAT2_ND39_Pos))
#define CAN_NDAT2_ND40_Pos                    (8U)                                           /**< (CAN_NDAT2) New Data 40 Position */
#define CAN_NDAT2_ND40_Msk                    (0x1U << CAN_NDAT2_ND40_Pos)                   /**< (CAN_NDAT2) New Data 40 Mask */
#define CAN_NDAT2_ND40(value)                 (CAN_NDAT2_ND40_Msk & ((value) << CAN_NDAT2_ND40_Pos))
#define CAN_NDAT2_ND41_Pos                    (9U)                                           /**< (CAN_NDAT2) New Data 41 Position */
#define CAN_NDAT2_ND41_Msk                    (0x1U << CAN_NDAT2_ND41_Pos)                   /**< (CAN_NDAT2) New Data 41 Mask */
#define CAN_NDAT2_ND41(value)                 (CAN_NDAT2_ND41_Msk & ((value) << CAN_NDAT2_ND41_Pos))
#define CAN_NDAT2_ND42_Pos                    (10U)                                          /**< (CAN_NDAT2) New Data 42 Position */
#define CAN_NDAT2_ND42_Msk                    (0x1U << CAN_NDAT2_ND42_Pos)                   /**< (CAN_NDAT2) New Data 42 Mask */
#define CAN_NDAT2_ND42(value)                 (CAN_NDAT2_ND42_Msk & ((value) << CAN_NDAT2_ND42_Pos))
#define CAN_NDAT2_ND43_Pos                    (11U)                                          /**< (CAN_NDAT2) New Data 43 Position */
#define CAN_NDAT2_ND43_Msk                    (0x1U << CAN_NDAT2_ND43_Pos)                   /**< (CAN_NDAT2) New Data 43 Mask */
#define CAN_NDAT2_ND43(value)                 (CAN_NDAT2_ND43_Msk & ((value) << CAN_NDAT2_ND43_Pos))
#define CAN_NDAT2_ND44_Pos                    (12U)                                          /**< (CAN_NDAT2) New Data 44 Position */
#define CAN_NDAT2_ND44_Msk                    (0x1U << CAN_NDAT2_ND44_Pos)                   /**< (CAN_NDAT2) New Data 44 Mask */
#define CAN_NDAT2_ND44(value)                 (CAN_NDAT2_ND44_Msk & ((value) << CAN_NDAT2_ND44_Pos))
#define CAN_NDAT2_ND45_Pos                    (13U)                                          /**< (CAN_NDAT2) New Data 45 Position */
#define CAN_NDAT2_ND45_Msk                    (0x1U << CAN_NDAT2_ND45_Pos)                   /**< (CAN_NDAT2) New Data 45 Mask */
#define CAN_NDAT2_ND45(value)                 (CAN_NDAT2_ND45_Msk & ((value) << CAN_NDAT2_ND45_Pos))
#define CAN_NDAT2_ND46_Pos                    (14U)                                          /**< (CAN_NDAT2) New Data 46 Position */
#define CAN_NDAT2_ND46_Msk                    (0x1U << CAN_NDAT2_ND46_Pos)                   /**< (CAN_NDAT2) New Data 46 Mask */
#define CAN_NDAT2_ND46(value)                 (CAN_NDAT2_ND46_Msk & ((value) << CAN_NDAT2_ND46_Pos))
#define CAN_NDAT2_ND47_Pos                    (15U)                                          /**< (CAN_NDAT2) New Data 47 Position */
#define CAN_NDAT2_ND47_Msk                    (0x1U << CAN_NDAT2_ND47_Pos)                   /**< (CAN_NDAT2) New Data 47 Mask */
#define CAN_NDAT2_ND47(value)                 (CAN_NDAT2_ND47_Msk & ((value) << CAN_NDAT2_ND47_Pos))
#define CAN_NDAT2_ND48_Pos                    (16U)                                          /**< (CAN_NDAT2) New Data 48 Position */
#define CAN_NDAT2_ND48_Msk                    (0x1U << CAN_NDAT2_ND48_Pos)                   /**< (CAN_NDAT2) New Data 48 Mask */
#define CAN_NDAT2_ND48(value)                 (CAN_NDAT2_ND48_Msk & ((value) << CAN_NDAT2_ND48_Pos))
#define CAN_NDAT2_ND49_Pos                    (17U)                                          /**< (CAN_NDAT2) New Data 49 Position */
#define CAN_NDAT2_ND49_Msk                    (0x1U << CAN_NDAT2_ND49_Pos)                   /**< (CAN_NDAT2) New Data 49 Mask */
#define CAN_NDAT2_ND49(value)                 (CAN_NDAT2_ND49_Msk & ((value) << CAN_NDAT2_ND49_Pos))
#define CAN_NDAT2_ND50_Pos                    (18U)                                          /**< (CAN_NDAT2) New Data 50 Position */
#define CAN_NDAT2_ND50_Msk                    (0x1U << CAN_NDAT2_ND50_Pos)                   /**< (CAN_NDAT2) New Data 50 Mask */
#define CAN_NDAT2_ND50(value)                 (CAN_NDAT2_ND50_Msk & ((value) << CAN_NDAT2_ND50_Pos))
#define CAN_NDAT2_ND51_Pos                    (19U)                                          /**< (CAN_NDAT2) New Data 51 Position */
#define CAN_NDAT2_ND51_Msk                    (0x1U << CAN_NDAT2_ND51_Pos)                   /**< (CAN_NDAT2) New Data 51 Mask */
#define CAN_NDAT2_ND51(value)                 (CAN_NDAT2_ND51_Msk & ((value) << CAN_NDAT2_ND51_Pos))
#define CAN_NDAT2_ND52_Pos                    (20U)                                          /**< (CAN_NDAT2) New Data 52 Position */
#define CAN_NDAT2_ND52_Msk                    (0x1U << CAN_NDAT2_ND52_Pos)                   /**< (CAN_NDAT2) New Data 52 Mask */
#define CAN_NDAT2_ND52(value)                 (CAN_NDAT2_ND52_Msk & ((value) << CAN_NDAT2_ND52_Pos))
#define CAN_NDAT2_ND53_Pos                    (21U)                                          /**< (CAN_NDAT2) New Data 53 Position */
#define CAN_NDAT2_ND53_Msk                    (0x1U << CAN_NDAT2_ND53_Pos)                   /**< (CAN_NDAT2) New Data 53 Mask */
#define CAN_NDAT2_ND53(value)                 (CAN_NDAT2_ND53_Msk & ((value) << CAN_NDAT2_ND53_Pos))
#define CAN_NDAT2_ND54_Pos                    (22U)                                          /**< (CAN_NDAT2) New Data 54 Position */
#define CAN_NDAT2_ND54_Msk                    (0x1U << CAN_NDAT2_ND54_Pos)                   /**< (CAN_NDAT2) New Data 54 Mask */
#define CAN_NDAT2_ND54(value)                 (CAN_NDAT2_ND54_Msk & ((value) << CAN_NDAT2_ND54_Pos))
#define CAN_NDAT2_ND55_Pos                    (23U)                                          /**< (CAN_NDAT2) New Data 55 Position */
#define CAN_NDAT2_ND55_Msk                    (0x1U << CAN_NDAT2_ND55_Pos)                   /**< (CAN_NDAT2) New Data 55 Mask */
#define CAN_NDAT2_ND55(value)                 (CAN_NDAT2_ND55_Msk & ((value) << CAN_NDAT2_ND55_Pos))
#define CAN_NDAT2_ND56_Pos                    (24U)                                          /**< (CAN_NDAT2) New Data 56 Position */
#define CAN_NDAT2_ND56_Msk                    (0x1U << CAN_NDAT2_ND56_Pos)                   /**< (CAN_NDAT2) New Data 56 Mask */
#define CAN_NDAT2_ND56(value)                 (CAN_NDAT2_ND56_Msk & ((value) << CAN_NDAT2_ND56_Pos))
#define CAN_NDAT2_ND57_Pos                    (25U)                                          /**< (CAN_NDAT2) New Data 57 Position */
#define CAN_NDAT2_ND57_Msk                    (0x1U << CAN_NDAT2_ND57_Pos)                   /**< (CAN_NDAT2) New Data 57 Mask */
#define CAN_NDAT2_ND57(value)                 (CAN_NDAT2_ND57_Msk & ((value) << CAN_NDAT2_ND57_Pos))
#define CAN_NDAT2_ND58_Pos                    (26U)                                          /**< (CAN_NDAT2) New Data 58 Position */
#define CAN_NDAT2_ND58_Msk                    (0x1U << CAN_NDAT2_ND58_Pos)                   /**< (CAN_NDAT2) New Data 58 Mask */
#define CAN_NDAT2_ND58(value)                 (CAN_NDAT2_ND58_Msk & ((value) << CAN_NDAT2_ND58_Pos))
#define CAN_NDAT2_ND59_Pos                    (27U)                                          /**< (CAN_NDAT2) New Data 59 Position */
#define CAN_NDAT2_ND59_Msk                    (0x1U << CAN_NDAT2_ND59_Pos)                   /**< (CAN_NDAT2) New Data 59 Mask */
#define CAN_NDAT2_ND59(value)                 (CAN_NDAT2_ND59_Msk & ((value) << CAN_NDAT2_ND59_Pos))
#define CAN_NDAT2_ND60_Pos                    (28U)                                          /**< (CAN_NDAT2) New Data 60 Position */
#define CAN_NDAT2_ND60_Msk                    (0x1U << CAN_NDAT2_ND60_Pos)                   /**< (CAN_NDAT2) New Data 60 Mask */
#define CAN_NDAT2_ND60(value)                 (CAN_NDAT2_ND60_Msk & ((value) << CAN_NDAT2_ND60_Pos))
#define CAN_NDAT2_ND61_Pos                    (29U)                                          /**< (CAN_NDAT2) New Data 61 Position */
#define CAN_NDAT2_ND61_Msk                    (0x1U << CAN_NDAT2_ND61_Pos)                   /**< (CAN_NDAT2) New Data 61 Mask */
#define CAN_NDAT2_ND61(value)                 (CAN_NDAT2_ND61_Msk & ((value) << CAN_NDAT2_ND61_Pos))
#define CAN_NDAT2_ND62_Pos                    (30U)                                          /**< (CAN_NDAT2) New Data 62 Position */
#define CAN_NDAT2_ND62_Msk                    (0x1U << CAN_NDAT2_ND62_Pos)                   /**< (CAN_NDAT2) New Data 62 Mask */
#define CAN_NDAT2_ND62(value)                 (CAN_NDAT2_ND62_Msk & ((value) << CAN_NDAT2_ND62_Pos))
#define CAN_NDAT2_ND63_Pos                    (31U)                                          /**< (CAN_NDAT2) New Data 63 Position */
#define CAN_NDAT2_ND63_Msk                    (0x1U << CAN_NDAT2_ND63_Pos)                   /**< (CAN_NDAT2) New Data 63 Mask */
#define CAN_NDAT2_ND63(value)                 (CAN_NDAT2_ND63_Msk & ((value) << CAN_NDAT2_ND63_Pos))
#define CAN_NDAT2_Msk                         (0xFFFFFFFFUL)                                 /**< (CAN_NDAT2) Register Mask  */

/* -------- CAN_RXF0C : (CAN Offset: 0xA0) (R/W 32) Rx FIFO 0 Configuration -------- */
#define CAN_RXF0C_F0SA_Pos                    (0U)                                           /**< (CAN_RXF0C) Rx FIFO 0 Start Address Position */
#define CAN_RXF0C_F0SA_Msk                    (0xFFFFU << CAN_RXF0C_F0SA_Pos)                /**< (CAN_RXF0C) Rx FIFO 0 Start Address Mask */
#define CAN_RXF0C_F0SA(value)                 (CAN_RXF0C_F0SA_Msk & ((value) << CAN_RXF0C_F0SA_Pos))
#define CAN_RXF0C_F0S_Pos                     (16U)                                          /**< (CAN_RXF0C) Rx FIFO 0 Size Position */
#define CAN_RXF0C_F0S_Msk                     (0x7FU << CAN_RXF0C_F0S_Pos)                   /**< (CAN_RXF0C) Rx FIFO 0 Size Mask */
#define CAN_RXF0C_F0S(value)                  (CAN_RXF0C_F0S_Msk & ((value) << CAN_RXF0C_F0S_Pos))
#define CAN_RXF0C_F0WM_Pos                    (24U)                                          /**< (CAN_RXF0C) Rx FIFO 0 Watermark Position */
#define CAN_RXF0C_F0WM_Msk                    (0x7FU << CAN_RXF0C_F0WM_Pos)                  /**< (CAN_RXF0C) Rx FIFO 0 Watermark Mask */
#define CAN_RXF0C_F0WM(value)                 (CAN_RXF0C_F0WM_Msk & ((value) << CAN_RXF0C_F0WM_Pos))
#define CAN_RXF0C_F0OM_Pos                    (31U)                                          /**< (CAN_RXF0C) FIFO 0 Operation Mode Position */
#define CAN_RXF0C_F0OM_Msk                    (0x1U << CAN_RXF0C_F0OM_Pos)                   /**< (CAN_RXF0C) FIFO 0 Operation Mode Mask */
#define CAN_RXF0C_F0OM(value)                 (CAN_RXF0C_F0OM_Msk & ((value) << CAN_RXF0C_F0OM_Pos))
#define CAN_RXF0C_Msk                         (0xFF7FFFFFUL)                                 /**< (CAN_RXF0C) Register Mask  */

/* -------- CAN_RXF0S : (CAN Offset: 0xA4) (R/  32) Rx FIFO 0 Status -------- */
#define CAN_RXF0S_F0FL_Pos                    (0U)                                           /**< (CAN_RXF0S) Rx FIFO 0 Fill Level Position */
#define CAN_RXF0S_F0FL_Msk                    (0x7FU << CAN_RXF0S_F0FL_Pos)                  /**< (CAN_RXF0S) Rx FIFO 0 Fill Level Mask */
#define CAN_RXF0S_F0FL(value)                 (CAN_RXF0S_F0FL_Msk & ((value) << CAN_RXF0S_F0FL_Pos))
#define CAN_RXF0S_F0GI_Pos                    (8U)                                           /**< (CAN_RXF0S) Rx FIFO 0 Get Index Position */
#define CAN_RXF0S_F0GI_Msk                    (0x3FU << CAN_RXF0S_F0GI_Pos)                  /**< (CAN_RXF0S) Rx FIFO 0 Get Index Mask */
#define CAN_RXF0S_F0GI(value)                 (CAN_RXF0S_F0GI_Msk & ((value) << CAN_RXF0S_F0GI_Pos))
#define CAN_RXF0S_F0PI_Pos                    (16U)                                          /**< (CAN_RXF0S) Rx FIFO 0 Put Index Position */
#define CAN_RXF0S_F0PI_Msk                    (0x3FU << CAN_RXF0S_F0PI_Pos)                  /**< (CAN_RXF0S) Rx FIFO 0 Put Index Mask */
#define CAN_RXF0S_F0PI(value)                 (CAN_RXF0S_F0PI_Msk & ((value) << CAN_RXF0S_F0PI_Pos))
#define CAN_RXF0S_F0F_Pos                     (24U)                                          /**< (CAN_RXF0S) Rx FIFO 0 Full Position */
#define CAN_RXF0S_F0F_Msk                     (0x1U << CAN_RXF0S_F0F_Pos)                    /**< (CAN_RXF0S) Rx FIFO 0 Full Mask */
#define CAN_RXF0S_F0F(value)                  (CAN_RXF0S_F0F_Msk & ((value) << CAN_RXF0S_F0F_Pos))
#define CAN_RXF0S_RF0L_Pos                    (25U)                                          /**< (CAN_RXF0S) Rx FIFO 0 Message Lost Position */
#define CAN_RXF0S_RF0L_Msk                    (0x1U << CAN_RXF0S_RF0L_Pos)                   /**< (CAN_RXF0S) Rx FIFO 0 Message Lost Mask */
#define CAN_RXF0S_RF0L(value)                 (CAN_RXF0S_RF0L_Msk & ((value) << CAN_RXF0S_RF0L_Pos))
#define CAN_RXF0S_Msk                         (0x033F3F7FUL)                                 /**< (CAN_RXF0S) Register Mask  */

/* -------- CAN_RXF0A : (CAN Offset: 0xA8) (R/W 32) Rx FIFO 0 Acknowledge -------- */
#define CAN_RXF0A_F0AI_Pos                    (0U)                                           /**< (CAN_RXF0A) Rx FIFO 0 Acknowledge Index Position */
#define CAN_RXF0A_F0AI_Msk                    (0x3FU << CAN_RXF0A_F0AI_Pos)                  /**< (CAN_RXF0A) Rx FIFO 0 Acknowledge Index Mask */
#define CAN_RXF0A_F0AI(value)                 (CAN_RXF0A_F0AI_Msk & ((value) << CAN_RXF0A_F0AI_Pos))
#define CAN_RXF0A_Msk                         (0x0000003FUL)                                 /**< (CAN_RXF0A) Register Mask  */

/* -------- CAN_RXBC : (CAN Offset: 0xAC) (R/W 32) Rx Buffer Configuration -------- */
#define CAN_RXBC_RBSA_Pos                     (0U)                                           /**< (CAN_RXBC) Rx Buffer Start Address Position */
#define CAN_RXBC_RBSA_Msk                     (0xFFFFU << CAN_RXBC_RBSA_Pos)                 /**< (CAN_RXBC) Rx Buffer Start Address Mask */
#define CAN_RXBC_RBSA(value)                  (CAN_RXBC_RBSA_Msk & ((value) << CAN_RXBC_RBSA_Pos))
#define CAN_RXBC_Msk                          (0x0000FFFFUL)                                 /**< (CAN_RXBC) Register Mask  */

/* -------- CAN_RXF1C : (CAN Offset: 0xB0) (R/W 32) Rx FIFO 1 Configuration -------- */
#define CAN_RXF1C_F1SA_Pos                    (0U)                                           /**< (CAN_RXF1C) Rx FIFO 1 Start Address Position */
#define CAN_RXF1C_F1SA_Msk                    (0xFFFFU << CAN_RXF1C_F1SA_Pos)                /**< (CAN_RXF1C) Rx FIFO 1 Start Address Mask */
#define CAN_RXF1C_F1SA(value)                 (CAN_RXF1C_F1SA_Msk & ((value) << CAN_RXF1C_F1SA_Pos))
#define CAN_RXF1C_F1S_Pos                     (16U)                                          /**< (CAN_RXF1C) Rx FIFO 1 Size Position */
#define CAN_RXF1C_F1S_Msk                     (0x7FU << CAN_RXF1C_F1S_Pos)                   /**< (CAN_RXF1C) Rx FIFO 1 Size Mask */
#define CAN_RXF1C_F1S(value)                  (CAN_RXF1C_F1S_Msk & ((value) << CAN_RXF1C_F1S_Pos))
#define CAN_RXF1C_F1WM_Pos                    (24U)                                          /**< (CAN_RXF1C) Rx FIFO 1 Watermark Position */
#define CAN_RXF1C_F1WM_Msk                    (0x7FU << CAN_RXF1C_F1WM_Pos)                  /**< (CAN_RXF1C) Rx FIFO 1 Watermark Mask */
#define CAN_RXF1C_F1WM(value)                 (CAN_RXF1C_F1WM_Msk & ((value) << CAN_RXF1C_F1WM_Pos))
#define CAN_RXF1C_F1OM_Pos                    (31U)                                          /**< (CAN_RXF1C) FIFO 1 Operation Mode Position */
#define CAN_RXF1C_F1OM_Msk                    (0x1U << CAN_RXF1C_F1OM_Pos)                   /**< (CAN_RXF1C) FIFO 1 Operation Mode Mask */
#define CAN_RXF1C_F1OM(value)                 (CAN_RXF1C_F1OM_Msk & ((value) << CAN_RXF1C_F1OM_Pos))
#define CAN_RXF1C_Msk                         (0xFF7FFFFFUL)                                 /**< (CAN_RXF1C) Register Mask  */

/* -------- CAN_RXF1S : (CAN Offset: 0xB4) (R/  32) Rx FIFO 1 Status -------- */
#define CAN_RXF1S_F1FL_Pos                    (0U)                                           /**< (CAN_RXF1S) Rx FIFO 1 Fill Level Position */
#define CAN_RXF1S_F1FL_Msk                    (0x7FU << CAN_RXF1S_F1FL_Pos)                  /**< (CAN_RXF1S) Rx FIFO 1 Fill Level Mask */
#define CAN_RXF1S_F1FL(value)                 (CAN_RXF1S_F1FL_Msk & ((value) << CAN_RXF1S_F1FL_Pos))
#define CAN_RXF1S_F1GI_Pos                    (8U)                                           /**< (CAN_RXF1S) Rx FIFO 1 Get Index Position */
#define CAN_RXF1S_F1GI_Msk                    (0x3FU << CAN_RXF1S_F1GI_Pos)                  /**< (CAN_RXF1S) Rx FIFO 1 Get Index Mask */
#define CAN_RXF1S_F1GI(value)                 (CAN_RXF1S_F1GI_Msk & ((value) << CAN_RXF1S_F1GI_Pos))
#define CAN_RXF1S_F1PI_Pos                    (16U)                                          /**< (CAN_RXF1S) Rx FIFO 1 Put Index Position */
#define CAN_RXF1S_F1PI_Msk                    (0x3FU << CAN_RXF1S_F1PI_Pos)                  /**< (CAN_RXF1S) Rx FIFO 1 Put Index Mask */
#define CAN_RXF1S_F1PI(value)                 (CAN_RXF1S_F1PI_Msk & ((value) << CAN_RXF1S_F1PI_Pos))
#define CAN_RXF1S_F1F_Pos                     (24U)                                          /**< (CAN_RXF1S) Rx FIFO 1 Full Position */
#define CAN_RXF1S_F1F_Msk                     (0x1U << CAN_RXF1S_F1F_Pos)                    /**< (CAN_RXF1S) Rx FIFO 1 Full Mask */
#define CAN_RXF1S_F1F(value)                  (CAN_RXF1S_F1F_Msk & ((value) << CAN_RXF1S_F1F_Pos))
#define CAN_RXF1S_RF1L_Pos                    (25U)                                          /**< (CAN_RXF1S) Rx FIFO 1 Message Lost Position */
#define CAN_RXF1S_RF1L_Msk                    (0x1U << CAN_RXF1S_RF1L_Pos)                   /**< (CAN_RXF1S) Rx FIFO 1 Message Lost Mask */
#define CAN_RXF1S_RF1L(value)                 (CAN_RXF1S_RF1L_Msk & ((value) << CAN_RXF1S_RF1L_Pos))
#define CAN_RXF1S_DMS_Pos                     (30U)                                          /**< (CAN_RXF1S) Debug Message Status Position */
#define CAN_RXF1S_DMS_Msk                     (0x3U << CAN_RXF1S_DMS_Pos)                    /**< (CAN_RXF1S) Debug Message Status Mask */
#define CAN_RXF1S_DMS(value)                  (CAN_RXF1S_DMS_Msk & ((value) << CAN_RXF1S_DMS_Pos))
#define   CAN_RXF1S_DMS_IDLE_Val              (0U)                                           /**< (CAN_RXF1S) Idle state  */
#define   CAN_RXF1S_DMS_DBGA_Val              (1U)                                           /**< (CAN_RXF1S) Debug message A received  */
#define   CAN_RXF1S_DMS_DBGB_Val              (2U)                                           /**< (CAN_RXF1S) Debug message A/B received  */
#define   CAN_RXF1S_DMS_DBGC_Val              (3U)                                           /**< (CAN_RXF1S) Debug message A/B/C received, DMA request set  */
#define CAN_RXF1S_DMS_IDLE                    (CAN_RXF1S_DMS_IDLE_Val << CAN_RXF1S_DMS_Pos)  /**< (CAN_RXF1S) Idle state Position  */
#define CAN_RXF1S_DMS_DBGA                    (CAN_RXF1S_DMS_DBGA_Val << CAN_RXF1S_DMS_Pos)  /**< (CAN_RXF1S) Debug message A received Position  */
#define CAN_RXF1S_DMS_DBGB                    (CAN_RXF1S_DMS_DBGB_Val << CAN_RXF1S_DMS_Pos)  /**< (CAN_RXF1S) Debug message A/B received Position  */
#define CAN_RXF1S_DMS_DBGC                    (CAN_RXF1S_DMS_DBGC_Val << CAN_RXF1S_DMS_Pos)  /**< (CAN_RXF1S) Debug message A/B/C received, DMA request set Position  */
#define CAN_RXF1S_Msk                         (0xC33F3F7FUL)                                 /**< (CAN_RXF1S) Register Mask  */

/* -------- CAN_RXF1A : (CAN Offset: 0xB8) (R/W 32) Rx FIFO 1 Acknowledge -------- */
#define CAN_RXF1A_F1AI_Pos                    (0U)                                           /**< (CAN_RXF1A) Rx FIFO 1 Acknowledge Index Position */
#define CAN_RXF1A_F1AI_Msk                    (0x3FU << CAN_RXF1A_F1AI_Pos)                  /**< (CAN_RXF1A) Rx FIFO 1 Acknowledge Index Mask */
#define CAN_RXF1A_F1AI(value)                 (CAN_RXF1A_F1AI_Msk & ((value) << CAN_RXF1A_F1AI_Pos))
#define CAN_RXF1A_Msk                         (0x0000003FUL)                                 /**< (CAN_RXF1A) Register Mask  */

/* -------- CAN_RXESC : (CAN Offset: 0xBC) (R/W 32) Rx Buffer / FIFO Element Size Configuration -------- */
#define CAN_RXESC_F0DS_Pos                    (0U)                                           /**< (CAN_RXESC) Rx FIFO 0 Data Field Size Position */
#define CAN_RXESC_F0DS_Msk                    (0x7U << CAN_RXESC_F0DS_Pos)                   /**< (CAN_RXESC) Rx FIFO 0 Data Field Size Mask */
#define CAN_RXESC_F0DS(value)                 (CAN_RXESC_F0DS_Msk & ((value) << CAN_RXESC_F0DS_Pos))
#define   CAN_RXESC_F0DS_DATA8_Val            (0U)                                           /**< (CAN_RXESC) 8 byte data field  */
#define   CAN_RXESC_F0DS_DATA12_Val           (1U)                                           /**< (CAN_RXESC) 12 byte data field  */
#define   CAN_RXESC_F0DS_DATA16_Val           (2U)                                           /**< (CAN_RXESC) 16 byte data field  */
#define   CAN_RXESC_F0DS_DATA20_Val           (3U)                                           /**< (CAN_RXESC) 20 byte data field  */
#define   CAN_RXESC_F0DS_DATA24_Val           (4U)                                           /**< (CAN_RXESC) 24 byte data field  */
#define   CAN_RXESC_F0DS_DATA32_Val           (5U)                                           /**< (CAN_RXESC) 32 byte data field  */
#define   CAN_RXESC_F0DS_DATA48_Val           (6U)                                           /**< (CAN_RXESC) 48 byte data field  */
#define   CAN_RXESC_F0DS_DATA64_Val           (7U)                                           /**< (CAN_RXESC) 64 byte data field  */
#define CAN_RXESC_F0DS_DATA8                  (CAN_RXESC_F0DS_DATA8_Val << CAN_RXESC_F0DS_Pos) /**< (CAN_RXESC) 8 byte data field Position  */
#define CAN_RXESC_F0DS_DATA12                 (CAN_RXESC_F0DS_DATA12_Val << CAN_RXESC_F0DS_Pos) /**< (CAN_RXESC) 12 byte data field Position  */
#define CAN_RXESC_F0DS_DATA16                 (CAN_RXESC_F0DS_DATA16_Val << CAN_RXESC_F0DS_Pos) /**< (CAN_RXESC) 16 byte data field Position  */
#define CAN_RXESC_F0DS_DATA20                 (CAN_RXESC_F0DS_DATA20_Val << CAN_RXESC_F0DS_Pos) /**< (CAN_RXESC) 20 byte data field Position  */
#define CAN_RXESC_F0DS_DATA24                 (CAN_RXESC_F0DS_DATA24_Val << CAN_RXESC_F0DS_Pos) /**< (CAN_RXESC) 24 byte data field Position  */
#define CAN_RXESC_F0DS_DATA32                 (CAN_RXESC_F0DS_DATA32_Val << CAN_RXESC_F0DS_Pos) /**< (CAN_RXESC) 32 byte data field Position  */
#define CAN_RXESC_F0DS_DATA48                 (CAN_RXESC_F0DS_DATA48_Val << CAN_RXESC_F0DS_Pos) /**< (CAN_RXESC) 48 byte data field Position  */
#define CAN_RXESC_F0DS_DATA64                 (CAN_RXESC_F0DS_DATA64_Val << CAN_RXESC_F0DS_Pos) /**< (CAN_RXESC) 64 byte data field Position  */
#define CAN_RXESC_F1DS_Pos                    (4U)                                           /**< (CAN_RXESC) Rx FIFO 1 Data Field Size Position */
#define CAN_RXESC_F1DS_Msk                    (0x7U << CAN_RXESC_F1DS_Pos)                   /**< (CAN_RXESC) Rx FIFO 1 Data Field Size Mask */
#define CAN_RXESC_F1DS(value)                 (CAN_RXESC_F1DS_Msk & ((value) << CAN_RXESC_F1DS_Pos))
#define   CAN_RXESC_F1DS_DATA8_Val            (0U)                                           /**< (CAN_RXESC) 8 byte data field  */
#define   CAN_RXESC_F1DS_DATA12_Val           (1U)                                           /**< (CAN_RXESC) 12 byte data field  */
#define   CAN_RXESC_F1DS_DATA16_Val           (2U)                                           /**< (CAN_RXESC) 16 byte data field  */
#define   CAN_RXESC_F1DS_DATA20_Val           (3U)                                           /**< (CAN_RXESC) 20 byte data field  */
#define   CAN_RXESC_F1DS_DATA24_Val           (4U)                                           /**< (CAN_RXESC) 24 byte data field  */
#define   CAN_RXESC_F1DS_DATA32_Val           (5U)                                           /**< (CAN_RXESC) 32 byte data field  */
#define   CAN_RXESC_F1DS_DATA48_Val           (6U)                                           /**< (CAN_RXESC) 48 byte data field  */
#define   CAN_RXESC_F1DS_DATA64_Val           (7U)                                           /**< (CAN_RXESC) 64 byte data field  */
#define CAN_RXESC_F1DS_DATA8                  (CAN_RXESC_F1DS_DATA8_Val << CAN_RXESC_F1DS_Pos) /**< (CAN_RXESC) 8 byte data field Position  */
#define CAN_RXESC_F1DS_DATA12                 (CAN_RXESC_F1DS_DATA12_Val << CAN_RXESC_F1DS_Pos) /**< (CAN_RXESC) 12 byte data field Position  */
#define CAN_RXESC_F1DS_DATA16                 (CAN_RXESC_F1DS_DATA16_Val << CAN_RXESC_F1DS_Pos) /**< (CAN_RXESC) 16 byte data field Position  */
#define CAN_RXESC_F1DS_DATA20                 (CAN_RXESC_F1DS_DATA20_Val << CAN_RXESC_F1DS_Pos) /**< (CAN_RXESC) 20 byte data field Position  */
#define CAN_RXESC_F1DS_DATA24                 (CAN_RXESC_F1DS_DATA24_Val << CAN_RXESC_F1DS_Pos) /**< (CAN_RXESC) 24 byte data field Position  */
#define CAN_RXESC_F1DS_DATA32                 (CAN_RXESC_F1DS_DATA32_Val << CAN_RXESC_F1DS_Pos) /**< (CAN_RXESC) 32 byte data field Position  */
#define CAN_RXESC_F1DS_DATA48                 (CAN_RXESC_F1DS_DATA48_Val << CAN_RXESC_F1DS_Pos) /**< (CAN_RXESC) 48 byte data field Position  */
#define CAN_RXESC_F1DS_DATA64                 (CAN_RXESC_F1DS_DATA64_Val << CAN_RXESC_F1DS_Pos) /**< (CAN_RXESC) 64 byte data field Position  */
#define CAN_RXESC_RBDS_Pos                    (8U)                                           /**< (CAN_RXESC) Rx Buffer Data Field Size Position */
#define CAN_RXESC_RBDS_Msk                    (0x7U << CAN_RXESC_RBDS_Pos)                   /**< (CAN_RXESC) Rx Buffer Data Field Size Mask */
#define CAN_RXESC_RBDS(value)                 (CAN_RXESC_RBDS_Msk & ((value) << CAN_RXESC_RBDS_Pos))
#define   CAN_RXESC_RBDS_DATA8_Val            (0U)                                           /**< (CAN_RXESC) 8 byte data field  */
#define   CAN_RXESC_RBDS_DATA12_Val           (1U)                                           /**< (CAN_RXESC) 12 byte data field  */
#define   CAN_RXESC_RBDS_DATA16_Val           (2U)                                           /**< (CAN_RXESC) 16 byte data field  */
#define   CAN_RXESC_RBDS_DATA20_Val           (3U)                                           /**< (CAN_RXESC) 20 byte data field  */
#define   CAN_RXESC_RBDS_DATA24_Val           (4U)                                           /**< (CAN_RXESC) 24 byte data field  */
#define   CAN_RXESC_RBDS_DATA32_Val           (5U)                                           /**< (CAN_RXESC) 32 byte data field  */
#define   CAN_RXESC_RBDS_DATA48_Val           (6U)                                           /**< (CAN_RXESC) 48 byte data field  */
#define   CAN_RXESC_RBDS_DATA64_Val           (7U)                                           /**< (CAN_RXESC) 64 byte data field  */
#define CAN_RXESC_RBDS_DATA8                  (CAN_RXESC_RBDS_DATA8_Val << CAN_RXESC_RBDS_Pos) /**< (CAN_RXESC) 8 byte data field Position  */
#define CAN_RXESC_RBDS_DATA12                 (CAN_RXESC_RBDS_DATA12_Val << CAN_RXESC_RBDS_Pos) /**< (CAN_RXESC) 12 byte data field Position  */
#define CAN_RXESC_RBDS_DATA16                 (CAN_RXESC_RBDS_DATA16_Val << CAN_RXESC_RBDS_Pos) /**< (CAN_RXESC) 16 byte data field Position  */
#define CAN_RXESC_RBDS_DATA20                 (CAN_RXESC_RBDS_DATA20_Val << CAN_RXESC_RBDS_Pos) /**< (CAN_RXESC) 20 byte data field Position  */
#define CAN_RXESC_RBDS_DATA24                 (CAN_RXESC_RBDS_DATA24_Val << CAN_RXESC_RBDS_Pos) /**< (CAN_RXESC) 24 byte data field Position  */
#define CAN_RXESC_RBDS_DATA32                 (CAN_RXESC_RBDS_DATA32_Val << CAN_RXESC_RBDS_Pos) /**< (CAN_RXESC) 32 byte data field Position  */
#define CAN_RXESC_RBDS_DATA48                 (CAN_RXESC_RBDS_DATA48_Val << CAN_RXESC_RBDS_Pos) /**< (CAN_RXESC) 48 byte data field Position  */
#define CAN_RXESC_RBDS_DATA64                 (CAN_RXESC_RBDS_DATA64_Val << CAN_RXESC_RBDS_Pos) /**< (CAN_RXESC) 64 byte data field Position  */
#define CAN_RXESC_Msk                         (0x00000777UL)                                 /**< (CAN_RXESC) Register Mask  */

/* -------- CAN_TXBC : (CAN Offset: 0xC0) (R/W 32) Tx Buffer Configuration -------- */
#define CAN_TXBC_TBSA_Pos                     (0U)                                           /**< (CAN_TXBC) Tx Buffers Start Address Position */
#define CAN_TXBC_TBSA_Msk                     (0xFFFFU << CAN_TXBC_TBSA_Pos)                 /**< (CAN_TXBC) Tx Buffers Start Address Mask */
#define CAN_TXBC_TBSA(value)                  (CAN_TXBC_TBSA_Msk & ((value) << CAN_TXBC_TBSA_Pos))
#define CAN_TXBC_NDTB_Pos                     (16U)                                          /**< (CAN_TXBC) Number of Dedicated Transmit Buffers Position */
#define CAN_TXBC_NDTB_Msk                     (0x3FU << CAN_TXBC_NDTB_Pos)                   /**< (CAN_TXBC) Number of Dedicated Transmit Buffers Mask */
#define CAN_TXBC_NDTB(value)                  (CAN_TXBC_NDTB_Msk & ((value) << CAN_TXBC_NDTB_Pos))
#define CAN_TXBC_TFQS_Pos                     (24U)                                          /**< (CAN_TXBC) Transmit FIFO/Queue Size Position */
#define CAN_TXBC_TFQS_Msk                     (0x3FU << CAN_TXBC_TFQS_Pos)                   /**< (CAN_TXBC) Transmit FIFO/Queue Size Mask */
#define CAN_TXBC_TFQS(value)                  (CAN_TXBC_TFQS_Msk & ((value) << CAN_TXBC_TFQS_Pos))
#define CAN_TXBC_TFQM_Pos                     (30U)                                          /**< (CAN_TXBC) Tx FIFO/Queue Mode Position */
#define CAN_TXBC_TFQM_Msk                     (0x1U << CAN_TXBC_TFQM_Pos)                    /**< (CAN_TXBC) Tx FIFO/Queue Mode Mask */
#define CAN_TXBC_TFQM(value)                  (CAN_TXBC_TFQM_Msk & ((value) << CAN_TXBC_TFQM_Pos))
#define CAN_TXBC_Msk                          (0x7F3FFFFFUL)                                 /**< (CAN_TXBC) Register Mask  */

/* -------- CAN_TXFQS : (CAN Offset: 0xC4) (R/  32) Tx FIFO / Queue Status -------- */
#define CAN_TXFQS_TFFL_Pos                    (0U)                                           /**< (CAN_TXFQS) Tx FIFO Free Level Position */
#define CAN_TXFQS_TFFL_Msk                    (0x3FU << CAN_TXFQS_TFFL_Pos)                  /**< (CAN_TXFQS) Tx FIFO Free Level Mask */
#define CAN_TXFQS_TFFL(value)                 (CAN_TXFQS_TFFL_Msk & ((value) << CAN_TXFQS_TFFL_Pos))
#define CAN_TXFQS_TFGI_Pos                    (8U)                                           /**< (CAN_TXFQS) Tx FIFO Get Index Position */
#define CAN_TXFQS_TFGI_Msk                    (0x1FU << CAN_TXFQS_TFGI_Pos)                  /**< (CAN_TXFQS) Tx FIFO Get Index Mask */
#define CAN_TXFQS_TFGI(value)                 (CAN_TXFQS_TFGI_Msk & ((value) << CAN_TXFQS_TFGI_Pos))
#define CAN_TXFQS_TFQPI_Pos                   (16U)                                          /**< (CAN_TXFQS) Tx FIFO/Queue Put Index Position */
#define CAN_TXFQS_TFQPI_Msk                   (0x1FU << CAN_TXFQS_TFQPI_Pos)                 /**< (CAN_TXFQS) Tx FIFO/Queue Put Index Mask */
#define CAN_TXFQS_TFQPI(value)                (CAN_TXFQS_TFQPI_Msk & ((value) << CAN_TXFQS_TFQPI_Pos))
#define CAN_TXFQS_TFQF_Pos                    (21U)                                          /**< (CAN_TXFQS) Tx FIFO/Queue Full Position */
#define CAN_TXFQS_TFQF_Msk                    (0x1U << CAN_TXFQS_TFQF_Pos)                   /**< (CAN_TXFQS) Tx FIFO/Queue Full Mask */
#define CAN_TXFQS_TFQF(value)                 (CAN_TXFQS_TFQF_Msk & ((value) << CAN_TXFQS_TFQF_Pos))
#define CAN_TXFQS_Msk                         (0x003F1F3FUL)                                 /**< (CAN_TXFQS) Register Mask  */

/* -------- CAN_TXESC : (CAN Offset: 0xC8) (R/W 32) Tx Buffer Element Size Configuration -------- */
#define CAN_TXESC_TBDS_Pos                    (0U)                                           /**< (CAN_TXESC) Tx Buffer Data Field Size Position */
#define CAN_TXESC_TBDS_Msk                    (0x7U << CAN_TXESC_TBDS_Pos)                   /**< (CAN_TXESC) Tx Buffer Data Field Size Mask */
#define CAN_TXESC_TBDS(value)                 (CAN_TXESC_TBDS_Msk & ((value) << CAN_TXESC_TBDS_Pos))
#define   CAN_TXESC_TBDS_DATA8_Val            (0U)                                           /**< (CAN_TXESC) 8 byte data field  */
#define   CAN_TXESC_TBDS_DATA12_Val           (1U)                                           /**< (CAN_TXESC) 12 byte data field  */
#define   CAN_TXESC_TBDS_DATA16_Val           (2U)                                           /**< (CAN_TXESC) 16 byte data field  */
#define   CAN_TXESC_TBDS_DATA20_Val           (3U)                                           /**< (CAN_TXESC) 20 byte data field  */
#define   CAN_TXESC_TBDS_DATA24_Val           (4U)                                           /**< (CAN_TXESC) 24 byte data field  */
#define   CAN_TXESC_TBDS_DATA32_Val           (5U)                                           /**< (CAN_TXESC) 32 byte data field  */
#define   CAN_TXESC_TBDS_DATA48_Val           (6U)                                           /**< (CAN_TXESC) 48 byte data field  */
#define   CAN_TXESC_TBDS_DATA64_Val           (7U)                                           /**< (CAN_TXESC) 64 byte data field  */
#define CAN_TXESC_TBDS_DATA8                  (CAN_TXESC_TBDS_DATA8_Val << CAN_TXESC_TBDS_Pos) /**< (CAN_TXESC) 8 byte data field Position  */
#define CAN_TXESC_TBDS_DATA12                 (CAN_TXESC_TBDS_DATA12_Val << CAN_TXESC_TBDS_Pos) /**< (CAN_TXESC) 12 byte data field Position  */
#define CAN_TXESC_TBDS_DATA16                 (CAN_TXESC_TBDS_DATA16_Val << CAN_TXESC_TBDS_Pos) /**< (CAN_TXESC) 16 byte data field Position  */
#define CAN_TXESC_TBDS_DATA20                 (CAN_TXESC_TBDS_DATA20_Val << CAN_TXESC_TBDS_Pos) /**< (CAN_TXESC) 20 byte data field Position  */
#define CAN_TXESC_TBDS_DATA24                 (CAN_TXESC_TBDS_DATA24_Val << CAN_TXESC_TBDS_Pos) /**< (CAN_TXESC) 24 byte data field Position  */
#define CAN_TXESC_TBDS_DATA32                 (CAN_TXESC_TBDS_DATA32_Val << CAN_TXESC_TBDS_Pos) /**< (CAN_TXESC) 32 byte data field Position  */
#define CAN_TXESC_TBDS_DATA48                 (CAN_TXESC_TBDS_DATA48_Val << CAN_TXESC_TBDS_Pos) /**< (CAN_TXESC) 48 byte data field Position  */
#define CAN_TXESC_TBDS_DATA64                 (CAN_TXESC_TBDS_DATA64_Val << CAN_TXESC_TBDS_Pos) /**< (CAN_TXESC) 64 byte data field Position  */
#define CAN_TXESC_Msk                         (0x00000007UL)                                 /**< (CAN_TXESC) Register Mask  */

/* -------- CAN_TXBRP : (CAN Offset: 0xCC) (R/  32) Tx Buffer Request Pending -------- */
#define CAN_TXBRP_TRP0_Pos                    (0U)                                           /**< (CAN_TXBRP) Transmission Request Pending 0 Position */
#define CAN_TXBRP_TRP0_Msk                    (0x1U << CAN_TXBRP_TRP0_Pos)                   /**< (CAN_TXBRP) Transmission Request Pending 0 Mask */
#define CAN_TXBRP_TRP0(value)                 (CAN_TXBRP_TRP0_Msk & ((value) << CAN_TXBRP_TRP0_Pos))
#define CAN_TXBRP_TRP1_Pos                    (1U)                                           /**< (CAN_TXBRP) Transmission Request Pending 1 Position */
#define CAN_TXBRP_TRP1_Msk                    (0x1U << CAN_TXBRP_TRP1_Pos)                   /**< (CAN_TXBRP) Transmission Request Pending 1 Mask */
#define CAN_TXBRP_TRP1(value)                 (CAN_TXBRP_TRP1_Msk & ((value) << CAN_TXBRP_TRP1_Pos))
#define CAN_TXBRP_TRP2_Pos                    (2U)                                           /**< (CAN_TXBRP) Transmission Request Pending 2 Position */
#define CAN_TXBRP_TRP2_Msk                    (0x1U << CAN_TXBRP_TRP2_Pos)                   /**< (CAN_TXBRP) Transmission Request Pending 2 Mask */
#define CAN_TXBRP_TRP2(value)                 (CAN_TXBRP_TRP2_Msk & ((value) << CAN_TXBRP_TRP2_Pos))
#define CAN_TXBRP_TRP3_Pos                    (3U)                                           /**< (CAN_TXBRP) Transmission Request Pending 3 Position */
#define CAN_TXBRP_TRP3_Msk                    (0x1U << CAN_TXBRP_TRP3_Pos)                   /**< (CAN_TXBRP) Transmission Request Pending 3 Mask */
#define CAN_TXBRP_TRP3(value)                 (CAN_TXBRP_TRP3_Msk & ((value) << CAN_TXBRP_TRP3_Pos))
#define CAN_TXBRP_TRP4_Pos                    (4U)                                           /**< (CAN_TXBRP) Transmission Request Pending 4 Position */
#define CAN_TXBRP_TRP4_Msk                    (0x1U << CAN_TXBRP_TRP4_Pos)                   /**< (CAN_TXBRP) Transmission Request Pending 4 Mask */
#define CAN_TXBRP_TRP4(value)                 (CAN_TXBRP_TRP4_Msk & ((value) << CAN_TXBRP_TRP4_Pos))
#define CAN_TXBRP_TRP5_Pos                    (5U)                                           /**< (CAN_TXBRP) Transmission Request Pending 5 Position */
#define CAN_TXBRP_TRP5_Msk                    (0x1U << CAN_TXBRP_TRP5_Pos)                   /**< (CAN_TXBRP) Transmission Request Pending 5 Mask */
#define CAN_TXBRP_TRP5(value)                 (CAN_TXBRP_TRP5_Msk & ((value) << CAN_TXBRP_TRP5_Pos))
#define CAN_TXBRP_TRP6_Pos                    (6U)                                           /**< (CAN_TXBRP) Transmission Request Pending 6 Position */
#define CAN_TXBRP_TRP6_Msk                    (0x1U << CAN_TXBRP_TRP6_Pos)                   /**< (CAN_TXBRP) Transmission Request Pending 6 Mask */
#define CAN_TXBRP_TRP6(value)                 (CAN_TXBRP_TRP6_Msk & ((value) << CAN_TXBRP_TRP6_Pos))
#define CAN_TXBRP_TRP7_Pos                    (7U)                                           /**< (CAN_TXBRP) Transmission Request Pending 7 Position */
#define CAN_TXBRP_TRP7_Msk                    (0x1U << CAN_TXBRP_TRP7_Pos)                   /**< (CAN_TXBRP) Transmission Request Pending 7 Mask */
#define CAN_TXBRP_TRP7(value)                 (CAN_TXBRP_TRP7_Msk & ((value) << CAN_TXBRP_TRP7_Pos))
#define CAN_TXBRP_TRP8_Pos                    (8U)                                           /**< (CAN_TXBRP) Transmission Request Pending 8 Position */
#define CAN_TXBRP_TRP8_Msk                    (0x1U << CAN_TXBRP_TRP8_Pos)                   /**< (CAN_TXBRP) Transmission Request Pending 8 Mask */
#define CAN_TXBRP_TRP8(value)                 (CAN_TXBRP_TRP8_Msk & ((value) << CAN_TXBRP_TRP8_Pos))
#define CAN_TXBRP_TRP9_Pos                    (9U)                                           /**< (CAN_TXBRP) Transmission Request Pending 9 Position */
#define CAN_TXBRP_TRP9_Msk                    (0x1U << CAN_TXBRP_TRP9_Pos)                   /**< (CAN_TXBRP) Transmission Request Pending 9 Mask */
#define CAN_TXBRP_TRP9(value)                 (CAN_TXBRP_TRP9_Msk & ((value) << CAN_TXBRP_TRP9_Pos))
#define CAN_TXBRP_TRP10_Pos                   (10U)                                          /**< (CAN_TXBRP) Transmission Request Pending 10 Position */
#define CAN_TXBRP_TRP10_Msk                   (0x1U << CAN_TXBRP_TRP10_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 10 Mask */
#define CAN_TXBRP_TRP10(value)                (CAN_TXBRP_TRP10_Msk & ((value) << CAN_TXBRP_TRP10_Pos))
#define CAN_TXBRP_TRP11_Pos                   (11U)                                          /**< (CAN_TXBRP) Transmission Request Pending 11 Position */
#define CAN_TXBRP_TRP11_Msk                   (0x1U << CAN_TXBRP_TRP11_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 11 Mask */
#define CAN_TXBRP_TRP11(value)                (CAN_TXBRP_TRP11_Msk & ((value) << CAN_TXBRP_TRP11_Pos))
#define CAN_TXBRP_TRP12_Pos                   (12U)                                          /**< (CAN_TXBRP) Transmission Request Pending 12 Position */
#define CAN_TXBRP_TRP12_Msk                   (0x1U << CAN_TXBRP_TRP12_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 12 Mask */
#define CAN_TXBRP_TRP12(value)                (CAN_TXBRP_TRP12_Msk & ((value) << CAN_TXBRP_TRP12_Pos))
#define CAN_TXBRP_TRP13_Pos                   (13U)                                          /**< (CAN_TXBRP) Transmission Request Pending 13 Position */
#define CAN_TXBRP_TRP13_Msk                   (0x1U << CAN_TXBRP_TRP13_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 13 Mask */
#define CAN_TXBRP_TRP13(value)                (CAN_TXBRP_TRP13_Msk & ((value) << CAN_TXBRP_TRP13_Pos))
#define CAN_TXBRP_TRP14_Pos                   (14U)                                          /**< (CAN_TXBRP) Transmission Request Pending 14 Position */
#define CAN_TXBRP_TRP14_Msk                   (0x1U << CAN_TXBRP_TRP14_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 14 Mask */
#define CAN_TXBRP_TRP14(value)                (CAN_TXBRP_TRP14_Msk & ((value) << CAN_TXBRP_TRP14_Pos))
#define CAN_TXBRP_TRP15_Pos                   (15U)                                          /**< (CAN_TXBRP) Transmission Request Pending 15 Position */
#define CAN_TXBRP_TRP15_Msk                   (0x1U << CAN_TXBRP_TRP15_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 15 Mask */
#define CAN_TXBRP_TRP15(value)                (CAN_TXBRP_TRP15_Msk & ((value) << CAN_TXBRP_TRP15_Pos))
#define CAN_TXBRP_TRP16_Pos                   (16U)                                          /**< (CAN_TXBRP) Transmission Request Pending 16 Position */
#define CAN_TXBRP_TRP16_Msk                   (0x1U << CAN_TXBRP_TRP16_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 16 Mask */
#define CAN_TXBRP_TRP16(value)                (CAN_TXBRP_TRP16_Msk & ((value) << CAN_TXBRP_TRP16_Pos))
#define CAN_TXBRP_TRP17_Pos                   (17U)                                          /**< (CAN_TXBRP) Transmission Request Pending 17 Position */
#define CAN_TXBRP_TRP17_Msk                   (0x1U << CAN_TXBRP_TRP17_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 17 Mask */
#define CAN_TXBRP_TRP17(value)                (CAN_TXBRP_TRP17_Msk & ((value) << CAN_TXBRP_TRP17_Pos))
#define CAN_TXBRP_TRP18_Pos                   (18U)                                          /**< (CAN_TXBRP) Transmission Request Pending 18 Position */
#define CAN_TXBRP_TRP18_Msk                   (0x1U << CAN_TXBRP_TRP18_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 18 Mask */
#define CAN_TXBRP_TRP18(value)                (CAN_TXBRP_TRP18_Msk & ((value) << CAN_TXBRP_TRP18_Pos))
#define CAN_TXBRP_TRP19_Pos                   (19U)                                          /**< (CAN_TXBRP) Transmission Request Pending 19 Position */
#define CAN_TXBRP_TRP19_Msk                   (0x1U << CAN_TXBRP_TRP19_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 19 Mask */
#define CAN_TXBRP_TRP19(value)                (CAN_TXBRP_TRP19_Msk & ((value) << CAN_TXBRP_TRP19_Pos))
#define CAN_TXBRP_TRP20_Pos                   (20U)                                          /**< (CAN_TXBRP) Transmission Request Pending 20 Position */
#define CAN_TXBRP_TRP20_Msk                   (0x1U << CAN_TXBRP_TRP20_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 20 Mask */
#define CAN_TXBRP_TRP20(value)                (CAN_TXBRP_TRP20_Msk & ((value) << CAN_TXBRP_TRP20_Pos))
#define CAN_TXBRP_TRP21_Pos                   (21U)                                          /**< (CAN_TXBRP) Transmission Request Pending 21 Position */
#define CAN_TXBRP_TRP21_Msk                   (0x1U << CAN_TXBRP_TRP21_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 21 Mask */
#define CAN_TXBRP_TRP21(value)                (CAN_TXBRP_TRP21_Msk & ((value) << CAN_TXBRP_TRP21_Pos))
#define CAN_TXBRP_TRP22_Pos                   (22U)                                          /**< (CAN_TXBRP) Transmission Request Pending 22 Position */
#define CAN_TXBRP_TRP22_Msk                   (0x1U << CAN_TXBRP_TRP22_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 22 Mask */
#define CAN_TXBRP_TRP22(value)                (CAN_TXBRP_TRP22_Msk & ((value) << CAN_TXBRP_TRP22_Pos))
#define CAN_TXBRP_TRP23_Pos                   (23U)                                          /**< (CAN_TXBRP) Transmission Request Pending 23 Position */
#define CAN_TXBRP_TRP23_Msk                   (0x1U << CAN_TXBRP_TRP23_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 23 Mask */
#define CAN_TXBRP_TRP23(value)                (CAN_TXBRP_TRP23_Msk & ((value) << CAN_TXBRP_TRP23_Pos))
#define CAN_TXBRP_TRP24_Pos                   (24U)                                          /**< (CAN_TXBRP) Transmission Request Pending 24 Position */
#define CAN_TXBRP_TRP24_Msk                   (0x1U << CAN_TXBRP_TRP24_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 24 Mask */
#define CAN_TXBRP_TRP24(value)                (CAN_TXBRP_TRP24_Msk & ((value) << CAN_TXBRP_TRP24_Pos))
#define CAN_TXBRP_TRP25_Pos                   (25U)                                          /**< (CAN_TXBRP) Transmission Request Pending 25 Position */
#define CAN_TXBRP_TRP25_Msk                   (0x1U << CAN_TXBRP_TRP25_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 25 Mask */
#define CAN_TXBRP_TRP25(value)                (CAN_TXBRP_TRP25_Msk & ((value) << CAN_TXBRP_TRP25_Pos))
#define CAN_TXBRP_TRP26_Pos                   (26U)                                          /**< (CAN_TXBRP) Transmission Request Pending 26 Position */
#define CAN_TXBRP_TRP26_Msk                   (0x1U << CAN_TXBRP_TRP26_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 26 Mask */
#define CAN_TXBRP_TRP26(value)                (CAN_TXBRP_TRP26_Msk & ((value) << CAN_TXBRP_TRP26_Pos))
#define CAN_TXBRP_TRP27_Pos                   (27U)                                          /**< (CAN_TXBRP) Transmission Request Pending 27 Position */
#define CAN_TXBRP_TRP27_Msk                   (0x1U << CAN_TXBRP_TRP27_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 27 Mask */
#define CAN_TXBRP_TRP27(value)                (CAN_TXBRP_TRP27_Msk & ((value) << CAN_TXBRP_TRP27_Pos))
#define CAN_TXBRP_TRP28_Pos                   (28U)                                          /**< (CAN_TXBRP) Transmission Request Pending 28 Position */
#define CAN_TXBRP_TRP28_Msk                   (0x1U << CAN_TXBRP_TRP28_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 28 Mask */
#define CAN_TXBRP_TRP28(value)                (CAN_TXBRP_TRP28_Msk & ((value) << CAN_TXBRP_TRP28_Pos))
#define CAN_TXBRP_TRP29_Pos                   (29U)                                          /**< (CAN_TXBRP) Transmission Request Pending 29 Position */
#define CAN_TXBRP_TRP29_Msk                   (0x1U << CAN_TXBRP_TRP29_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 29 Mask */
#define CAN_TXBRP_TRP29(value)                (CAN_TXBRP_TRP29_Msk & ((value) << CAN_TXBRP_TRP29_Pos))
#define CAN_TXBRP_TRP30_Pos                   (30U)                                          /**< (CAN_TXBRP) Transmission Request Pending 30 Position */
#define CAN_TXBRP_TRP30_Msk                   (0x1U << CAN_TXBRP_TRP30_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 30 Mask */
#define CAN_TXBRP_TRP30(value)                (CAN_TXBRP_TRP30_Msk & ((value) << CAN_TXBRP_TRP30_Pos))
#define CAN_TXBRP_TRP31_Pos                   (31U)                                          /**< (CAN_TXBRP) Transmission Request Pending 31 Position */
#define CAN_TXBRP_TRP31_Msk                   (0x1U << CAN_TXBRP_TRP31_Pos)                  /**< (CAN_TXBRP) Transmission Request Pending 31 Mask */
#define CAN_TXBRP_TRP31(value)                (CAN_TXBRP_TRP31_Msk & ((value) << CAN_TXBRP_TRP31_Pos))
#define CAN_TXBRP_Msk                         (0xFFFFFFFFUL)                                 /**< (CAN_TXBRP) Register Mask  */

/* -------- CAN_TXBAR : (CAN Offset: 0xD0) (R/W 32) Tx Buffer Add Request -------- */
#define CAN_TXBAR_AR0_Pos                     (0U)                                           /**< (CAN_TXBAR) Add Request 0 Position */
#define CAN_TXBAR_AR0_Msk                     (0x1U << CAN_TXBAR_AR0_Pos)                    /**< (CAN_TXBAR) Add Request 0 Mask */
#define CAN_TXBAR_AR0(value)                  (CAN_TXBAR_AR0_Msk & ((value) << CAN_TXBAR_AR0_Pos))
#define CAN_TXBAR_AR1_Pos                     (1U)                                           /**< (CAN_TXBAR) Add Request 1 Position */
#define CAN_TXBAR_AR1_Msk                     (0x1U << CAN_TXBAR_AR1_Pos)                    /**< (CAN_TXBAR) Add Request 1 Mask */
#define CAN_TXBAR_AR1(value)                  (CAN_TXBAR_AR1_Msk & ((value) << CAN_TXBAR_AR1_Pos))
#define CAN_TXBAR_AR2_Pos                     (2U)                                           /**< (CAN_TXBAR) Add Request 2 Position */
#define CAN_TXBAR_AR2_Msk                     (0x1U << CAN_TXBAR_AR2_Pos)                    /**< (CAN_TXBAR) Add Request 2 Mask */
#define CAN_TXBAR_AR2(value)                  (CAN_TXBAR_AR2_Msk & ((value) << CAN_TXBAR_AR2_Pos))
#define CAN_TXBAR_AR3_Pos                     (3U)                                           /**< (CAN_TXBAR) Add Request 3 Position */
#define CAN_TXBAR_AR3_Msk                     (0x1U << CAN_TXBAR_AR3_Pos)                    /**< (CAN_TXBAR) Add Request 3 Mask */
#define CAN_TXBAR_AR3(value)                  (CAN_TXBAR_AR3_Msk & ((value) << CAN_TXBAR_AR3_Pos))
#define CAN_TXBAR_AR4_Pos                     (4U)                                           /**< (CAN_TXBAR) Add Request 4 Position */
#define CAN_TXBAR_AR4_Msk                     (0x1U << CAN_TXBAR_AR4_Pos)                    /**< (CAN_TXBAR) Add Request 4 Mask */
#define CAN_TXBAR_AR4(value)                  (CAN_TXBAR_AR4_Msk & ((value) << CAN_TXBAR_AR4_Pos))
#define CAN_TXBAR_AR5_Pos                     (5U)                                           /**< (CAN_TXBAR) Add Request 5 Position */
#define CAN_TXBAR_AR5_Msk                     (0x1U << CAN_TXBAR_AR5_Pos)                    /**< (CAN_TXBAR) Add Request 5 Mask */
#define CAN_TXBAR_AR5(value)                  (CAN_TXBAR_AR5_Msk & ((value) << CAN_TXBAR_AR5_Pos))
#define CAN_TXBAR_AR6_Pos                     (6U)                                           /**< (CAN_TXBAR) Add Request 6 Position */
#define CAN_TXBAR_AR6_Msk                     (0x1U << CAN_TXBAR_AR6_Pos)                    /**< (CAN_TXBAR) Add Request 6 Mask */
#define CAN_TXBAR_AR6(value)                  (CAN_TXBAR_AR6_Msk & ((value) << CAN_TXBAR_AR6_Pos))
#define CAN_TXBAR_AR7_Pos                     (7U)                                           /**< (CAN_TXBAR) Add Request 7 Position */
#define CAN_TXBAR_AR7_Msk                     (0x1U << CAN_TXBAR_AR7_Pos)                    /**< (CAN_TXBAR) Add Request 7 Mask */
#define CAN_TXBAR_AR7(value)                  (CAN_TXBAR_AR7_Msk & ((value) << CAN_TXBAR_AR7_Pos))
#define CAN_TXBAR_AR8_Pos                     (8U)                                           /**< (CAN_TXBAR) Add Request 8 Position */
#define CAN_TXBAR_AR8_Msk                     (0x1U << CAN_TXBAR_AR8_Pos)                    /**< (CAN_TXBAR) Add Request 8 Mask */
#define CAN_TXBAR_AR8(value)                  (CAN_TXBAR_AR8_Msk & ((value) << CAN_TXBAR_AR8_Pos))
#define CAN_TXBAR_AR9_Pos                     (9U)                                           /**< (CAN_TXBAR) Add Request 9 Position */
#define CAN_TXBAR_AR9_Msk                     (0x1U << CAN_TXBAR_AR9_Pos)                    /**< (CAN_TXBAR) Add Request 9 Mask */
#define CAN_TXBAR_AR9(value)                  (CAN_TXBAR_AR9_Msk & ((value) << CAN_TXBAR_AR9_Pos))
#define CAN_TXBAR_AR10_Pos                    (10U)                                          /**< (CAN_TXBAR) Add Request 10 Position */
#define CAN_TXBAR_AR10_Msk                    (0x1U << CAN_TXBAR_AR10_Pos)                   /**< (CAN_TXBAR) Add Request 10 Mask */
#define CAN_TXBAR_AR10(value)                 (CAN_TXBAR_AR10_Msk & ((value) << CAN_TXBAR_AR10_Pos))
#define CAN_TXBAR_AR11_Pos                    (11U)                                          /**< (CAN_TXBAR) Add Request 11 Position */
#define CAN_TXBAR_AR11_Msk                    (0x1U << CAN_TXBAR_AR11_Pos)                   /**< (CAN_TXBAR) Add Request 11 Mask */
#define CAN_TXBAR_AR11(value)                 (CAN_TXBAR_AR11_Msk & ((value) << CAN_TXBAR_AR11_Pos))
#define CAN_TXBAR_AR12_Pos                    (12U)                                          /**< (CAN_TXBAR) Add Request 12 Position */
#define CAN_TXBAR_AR12_Msk                    (0x1U << CAN_TXBAR_AR12_Pos)                   /**< (CAN_TXBAR) Add Request 12 Mask */
#define CAN_TXBAR_AR12(value)                 (CAN_TXBAR_AR12_Msk & ((value) << CAN_TXBAR_AR12_Pos))
#define CAN_TXBAR_AR13_Pos                    (13U)                                          /**< (CAN_TXBAR) Add Request 13 Position */
#define CAN_TXBAR_AR13_Msk                    (0x1U << CAN_TXBAR_AR13_Pos)                   /**< (CAN_TXBAR) Add Request 13 Mask */
#define CAN_TXBAR_AR13(value)                 (CAN_TXBAR_AR13_Msk & ((value) << CAN_TXBAR_AR13_Pos))
#define CAN_TXBAR_AR14_Pos                    (14U)                                          /**< (CAN_TXBAR) Add Request 14 Position */
#define CAN_TXBAR_AR14_Msk                    (0x1U << CAN_TXBAR_AR14_Pos)                   /**< (CAN_TXBAR) Add Request 14 Mask */
#define CAN_TXBAR_AR14(value)                 (CAN_TXBAR_AR14_Msk & ((value) << CAN_TXBAR_AR14_Pos))
#define CAN_TXBAR_AR15_Pos                    (15U)                                          /**< (CAN_TXBAR) Add Request 15 Position */
#define CAN_TXBAR_AR15_Msk                    (0x1U << CAN_TXBAR_AR15_Pos)                   /**< (CAN_TXBAR) Add Request 15 Mask */
#define CAN_TXBAR_AR15(value)                 (CAN_TXBAR_AR15_Msk & ((value) << CAN_TXBAR_AR15_Pos))
#define CAN_TXBAR_AR16_Pos                    (16U)                                          /**< (CAN_TXBAR) Add Request 16 Position */
#define CAN_TXBAR_AR16_Msk                    (0x1U << CAN_TXBAR_AR16_Pos)                   /**< (CAN_TXBAR) Add Request 16 Mask */
#define CAN_TXBAR_AR16(value)                 (CAN_TXBAR_AR16_Msk & ((value) << CAN_TXBAR_AR16_Pos))
#define CAN_TXBAR_AR17_Pos                    (17U)                                          /**< (CAN_TXBAR) Add Request 17 Position */
#define CAN_TXBAR_AR17_Msk                    (0x1U << CAN_TXBAR_AR17_Pos)                   /**< (CAN_TXBAR) Add Request 17 Mask */
#define CAN_TXBAR_AR17(value)                 (CAN_TXBAR_AR17_Msk & ((value) << CAN_TXBAR_AR17_Pos))
#define CAN_TXBAR_AR18_Pos                    (18U)                                          /**< (CAN_TXBAR) Add Request 18 Position */
#define CAN_TXBAR_AR18_Msk                    (0x1U << CAN_TXBAR_AR18_Pos)                   /**< (CAN_TXBAR) Add Request 18 Mask */
#define CAN_TXBAR_AR18(value)                 (CAN_TXBAR_AR18_Msk & ((value) << CAN_TXBAR_AR18_Pos))
#define CAN_TXBAR_AR19_Pos                    (19U)                                          /**< (CAN_TXBAR) Add Request 19 Position */
#define CAN_TXBAR_AR19_Msk                    (0x1U << CAN_TXBAR_AR19_Pos)                   /**< (CAN_TXBAR) Add Request 19 Mask */
#define CAN_TXBAR_AR19(value)                 (CAN_TXBAR_AR19_Msk & ((value) << CAN_TXBAR_AR19_Pos))
#define CAN_TXBAR_AR20_Pos                    (20U)                                          /**< (CAN_TXBAR) Add Request 20 Position */
#define CAN_TXBAR_AR20_Msk                    (0x1U << CAN_TXBAR_AR20_Pos)                   /**< (CAN_TXBAR) Add Request 20 Mask */
#define CAN_TXBAR_AR20(value)                 (CAN_TXBAR_AR20_Msk & ((value) << CAN_TXBAR_AR20_Pos))
#define CAN_TXBAR_AR21_Pos                    (21U)                                          /**< (CAN_TXBAR) Add Request 21 Position */
#define CAN_TXBAR_AR21_Msk                    (0x1U << CAN_TXBAR_AR21_Pos)                   /**< (CAN_TXBAR) Add Request 21 Mask */
#define CAN_TXBAR_AR21(value)                 (CAN_TXBAR_AR21_Msk & ((value) << CAN_TXBAR_AR21_Pos))
#define CAN_TXBAR_AR22_Pos                    (22U)                                          /**< (CAN_TXBAR) Add Request 22 Position */
#define CAN_TXBAR_AR22_Msk                    (0x1U << CAN_TXBAR_AR22_Pos)                   /**< (CAN_TXBAR) Add Request 22 Mask */
#define CAN_TXBAR_AR22(value)                 (CAN_TXBAR_AR22_Msk & ((value) << CAN_TXBAR_AR22_Pos))
#define CAN_TXBAR_AR23_Pos                    (23U)                                          /**< (CAN_TXBAR) Add Request 23 Position */
#define CAN_TXBAR_AR23_Msk                    (0x1U << CAN_TXBAR_AR23_Pos)                   /**< (CAN_TXBAR) Add Request 23 Mask */
#define CAN_TXBAR_AR23(value)                 (CAN_TXBAR_AR23_Msk & ((value) << CAN_TXBAR_AR23_Pos))
#define CAN_TXBAR_AR24_Pos                    (24U)                                          /**< (CAN_TXBAR) Add Request 24 Position */
#define CAN_TXBAR_AR24_Msk                    (0x1U << CAN_TXBAR_AR24_Pos)                   /**< (CAN_TXBAR) Add Request 24 Mask */
#define CAN_TXBAR_AR24(value)                 (CAN_TXBAR_AR24_Msk & ((value) << CAN_TXBAR_AR24_Pos))
#define CAN_TXBAR_AR25_Pos                    (25U)                                          /**< (CAN_TXBAR) Add Request 25 Position */
#define CAN_TXBAR_AR25_Msk                    (0x1U << CAN_TXBAR_AR25_Pos)                   /**< (CAN_TXBAR) Add Request 25 Mask */
#define CAN_TXBAR_AR25(value)                 (CAN_TXBAR_AR25_Msk & ((value) << CAN_TXBAR_AR25_Pos))
#define CAN_TXBAR_AR26_Pos                    (26U)                                          /**< (CAN_TXBAR) Add Request 26 Position */
#define CAN_TXBAR_AR26_Msk                    (0x1U << CAN_TXBAR_AR26_Pos)                   /**< (CAN_TXBAR) Add Request 26 Mask */
#define CAN_TXBAR_AR26(value)                 (CAN_TXBAR_AR26_Msk & ((value) << CAN_TXBAR_AR26_Pos))
#define CAN_TXBAR_AR27_Pos                    (27U)                                          /**< (CAN_TXBAR) Add Request 27 Position */
#define CAN_TXBAR_AR27_Msk                    (0x1U << CAN_TXBAR_AR27_Pos)                   /**< (CAN_TXBAR) Add Request 27 Mask */
#define CAN_TXBAR_AR27(value)                 (CAN_TXBAR_AR27_Msk & ((value) << CAN_TXBAR_AR27_Pos))
#define CAN_TXBAR_AR28_Pos                    (28U)                                          /**< (CAN_TXBAR) Add Request 28 Position */
#define CAN_TXBAR_AR28_Msk                    (0x1U << CAN_TXBAR_AR28_Pos)                   /**< (CAN_TXBAR) Add Request 28 Mask */
#define CAN_TXBAR_AR28(value)                 (CAN_TXBAR_AR28_Msk & ((value) << CAN_TXBAR_AR28_Pos))
#define CAN_TXBAR_AR29_Pos                    (29U)                                          /**< (CAN_TXBAR) Add Request 29 Position */
#define CAN_TXBAR_AR29_Msk                    (0x1U << CAN_TXBAR_AR29_Pos)                   /**< (CAN_TXBAR) Add Request 29 Mask */
#define CAN_TXBAR_AR29(value)                 (CAN_TXBAR_AR29_Msk & ((value) << CAN_TXBAR_AR29_Pos))
#define CAN_TXBAR_AR30_Pos                    (30U)                                          /**< (CAN_TXBAR) Add Request 30 Position */
#define CAN_TXBAR_AR30_Msk                    (0x1U << CAN_TXBAR_AR30_Pos)                   /**< (CAN_TXBAR) Add Request 30 Mask */
#define CAN_TXBAR_AR30(value)                 (CAN_TXBAR_AR30_Msk & ((value) << CAN_TXBAR_AR30_Pos))
#define CAN_TXBAR_AR31_Pos                    (31U)                                          /**< (CAN_TXBAR) Add Request 31 Position */
#define CAN_TXBAR_AR31_Msk                    (0x1U << CAN_TXBAR_AR31_Pos)                   /**< (CAN_TXBAR) Add Request 31 Mask */
#define CAN_TXBAR_AR31(value)                 (CAN_TXBAR_AR31_Msk & ((value) << CAN_TXBAR_AR31_Pos))
#define CAN_TXBAR_Msk                         (0xFFFFFFFFUL)                                 /**< (CAN_TXBAR) Register Mask  */

/* -------- CAN_TXBCR : (CAN Offset: 0xD4) (R/W 32) Tx Buffer Cancellation Request -------- */
#define CAN_TXBCR_CR0_Pos                     (0U)                                           /**< (CAN_TXBCR) Cancellation Request 0 Position */
#define CAN_TXBCR_CR0_Msk                     (0x1U << CAN_TXBCR_CR0_Pos)                    /**< (CAN_TXBCR) Cancellation Request 0 Mask */
#define CAN_TXBCR_CR0(value)                  (CAN_TXBCR_CR0_Msk & ((value) << CAN_TXBCR_CR0_Pos))
#define CAN_TXBCR_CR1_Pos                     (1U)                                           /**< (CAN_TXBCR) Cancellation Request 1 Position */
#define CAN_TXBCR_CR1_Msk                     (0x1U << CAN_TXBCR_CR1_Pos)                    /**< (CAN_TXBCR) Cancellation Request 1 Mask */
#define CAN_TXBCR_CR1(value)                  (CAN_TXBCR_CR1_Msk & ((value) << CAN_TXBCR_CR1_Pos))
#define CAN_TXBCR_CR2_Pos                     (2U)                                           /**< (CAN_TXBCR) Cancellation Request 2 Position */
#define CAN_TXBCR_CR2_Msk                     (0x1U << CAN_TXBCR_CR2_Pos)                    /**< (CAN_TXBCR) Cancellation Request 2 Mask */
#define CAN_TXBCR_CR2(value)                  (CAN_TXBCR_CR2_Msk & ((value) << CAN_TXBCR_CR2_Pos))
#define CAN_TXBCR_CR3_Pos                     (3U)                                           /**< (CAN_TXBCR) Cancellation Request 3 Position */
#define CAN_TXBCR_CR3_Msk                     (0x1U << CAN_TXBCR_CR3_Pos)                    /**< (CAN_TXBCR) Cancellation Request 3 Mask */
#define CAN_TXBCR_CR3(value)                  (CAN_TXBCR_CR3_Msk & ((value) << CAN_TXBCR_CR3_Pos))
#define CAN_TXBCR_CR4_Pos                     (4U)                                           /**< (CAN_TXBCR) Cancellation Request 4 Position */
#define CAN_TXBCR_CR4_Msk                     (0x1U << CAN_TXBCR_CR4_Pos)                    /**< (CAN_TXBCR) Cancellation Request 4 Mask */
#define CAN_TXBCR_CR4(value)                  (CAN_TXBCR_CR4_Msk & ((value) << CAN_TXBCR_CR4_Pos))
#define CAN_TXBCR_CR5_Pos                     (5U)                                           /**< (CAN_TXBCR) Cancellation Request 5 Position */
#define CAN_TXBCR_CR5_Msk                     (0x1U << CAN_TXBCR_CR5_Pos)                    /**< (CAN_TXBCR) Cancellation Request 5 Mask */
#define CAN_TXBCR_CR5(value)                  (CAN_TXBCR_CR5_Msk & ((value) << CAN_TXBCR_CR5_Pos))
#define CAN_TXBCR_CR6_Pos                     (6U)                                           /**< (CAN_TXBCR) Cancellation Request 6 Position */
#define CAN_TXBCR_CR6_Msk                     (0x1U << CAN_TXBCR_CR6_Pos)                    /**< (CAN_TXBCR) Cancellation Request 6 Mask */
#define CAN_TXBCR_CR6(value)                  (CAN_TXBCR_CR6_Msk & ((value) << CAN_TXBCR_CR6_Pos))
#define CAN_TXBCR_CR7_Pos                     (7U)                                           /**< (CAN_TXBCR) Cancellation Request 7 Position */
#define CAN_TXBCR_CR7_Msk                     (0x1U << CAN_TXBCR_CR7_Pos)                    /**< (CAN_TXBCR) Cancellation Request 7 Mask */
#define CAN_TXBCR_CR7(value)                  (CAN_TXBCR_CR7_Msk & ((value) << CAN_TXBCR_CR7_Pos))
#define CAN_TXBCR_CR8_Pos                     (8U)                                           /**< (CAN_TXBCR) Cancellation Request 8 Position */
#define CAN_TXBCR_CR8_Msk                     (0x1U << CAN_TXBCR_CR8_Pos)                    /**< (CAN_TXBCR) Cancellation Request 8 Mask */
#define CAN_TXBCR_CR8(value)                  (CAN_TXBCR_CR8_Msk & ((value) << CAN_TXBCR_CR8_Pos))
#define CAN_TXBCR_CR9_Pos                     (9U)                                           /**< (CAN_TXBCR) Cancellation Request 9 Position */
#define CAN_TXBCR_CR9_Msk                     (0x1U << CAN_TXBCR_CR9_Pos)                    /**< (CAN_TXBCR) Cancellation Request 9 Mask */
#define CAN_TXBCR_CR9(value)                  (CAN_TXBCR_CR9_Msk & ((value) << CAN_TXBCR_CR9_Pos))
#define CAN_TXBCR_CR10_Pos                    (10U)                                          /**< (CAN_TXBCR) Cancellation Request 10 Position */
#define CAN_TXBCR_CR10_Msk                    (0x1U << CAN_TXBCR_CR10_Pos)                   /**< (CAN_TXBCR) Cancellation Request 10 Mask */
#define CAN_TXBCR_CR10(value)                 (CAN_TXBCR_CR10_Msk & ((value) << CAN_TXBCR_CR10_Pos))
#define CAN_TXBCR_CR11_Pos                    (11U)                                          /**< (CAN_TXBCR) Cancellation Request 11 Position */
#define CAN_TXBCR_CR11_Msk                    (0x1U << CAN_TXBCR_CR11_Pos)                   /**< (CAN_TXBCR) Cancellation Request 11 Mask */
#define CAN_TXBCR_CR11(value)                 (CAN_TXBCR_CR11_Msk & ((value) << CAN_TXBCR_CR11_Pos))
#define CAN_TXBCR_CR12_Pos                    (12U)                                          /**< (CAN_TXBCR) Cancellation Request 12 Position */
#define CAN_TXBCR_CR12_Msk                    (0x1U << CAN_TXBCR_CR12_Pos)                   /**< (CAN_TXBCR) Cancellation Request 12 Mask */
#define CAN_TXBCR_CR12(value)                 (CAN_TXBCR_CR12_Msk & ((value) << CAN_TXBCR_CR12_Pos))
#define CAN_TXBCR_CR13_Pos                    (13U)                                          /**< (CAN_TXBCR) Cancellation Request 13 Position */
#define CAN_TXBCR_CR13_Msk                    (0x1U << CAN_TXBCR_CR13_Pos)                   /**< (CAN_TXBCR) Cancellation Request 13 Mask */
#define CAN_TXBCR_CR13(value)                 (CAN_TXBCR_CR13_Msk & ((value) << CAN_TXBCR_CR13_Pos))
#define CAN_TXBCR_CR14_Pos                    (14U)                                          /**< (CAN_TXBCR) Cancellation Request 14 Position */
#define CAN_TXBCR_CR14_Msk                    (0x1U << CAN_TXBCR_CR14_Pos)                   /**< (CAN_TXBCR) Cancellation Request 14 Mask */
#define CAN_TXBCR_CR14(value)                 (CAN_TXBCR_CR14_Msk & ((value) << CAN_TXBCR_CR14_Pos))
#define CAN_TXBCR_CR15_Pos                    (15U)                                          /**< (CAN_TXBCR) Cancellation Request 15 Position */
#define CAN_TXBCR_CR15_Msk                    (0x1U << CAN_TXBCR_CR15_Pos)                   /**< (CAN_TXBCR) Cancellation Request 15 Mask */
#define CAN_TXBCR_CR15(value)                 (CAN_TXBCR_CR15_Msk & ((value) << CAN_TXBCR_CR15_Pos))
#define CAN_TXBCR_CR16_Pos                    (16U)                                          /**< (CAN_TXBCR) Cancellation Request 16 Position */
#define CAN_TXBCR_CR16_Msk                    (0x1U << CAN_TXBCR_CR16_Pos)                   /**< (CAN_TXBCR) Cancellation Request 16 Mask */
#define CAN_TXBCR_CR16(value)                 (CAN_TXBCR_CR16_Msk & ((value) << CAN_TXBCR_CR16_Pos))
#define CAN_TXBCR_CR17_Pos                    (17U)                                          /**< (CAN_TXBCR) Cancellation Request 17 Position */
#define CAN_TXBCR_CR17_Msk                    (0x1U << CAN_TXBCR_CR17_Pos)                   /**< (CAN_TXBCR) Cancellation Request 17 Mask */
#define CAN_TXBCR_CR17(value)                 (CAN_TXBCR_CR17_Msk & ((value) << CAN_TXBCR_CR17_Pos))
#define CAN_TXBCR_CR18_Pos                    (18U)                                          /**< (CAN_TXBCR) Cancellation Request 18 Position */
#define CAN_TXBCR_CR18_Msk                    (0x1U << CAN_TXBCR_CR18_Pos)                   /**< (CAN_TXBCR) Cancellation Request 18 Mask */
#define CAN_TXBCR_CR18(value)                 (CAN_TXBCR_CR18_Msk & ((value) << CAN_TXBCR_CR18_Pos))
#define CAN_TXBCR_CR19_Pos                    (19U)                                          /**< (CAN_TXBCR) Cancellation Request 19 Position */
#define CAN_TXBCR_CR19_Msk                    (0x1U << CAN_TXBCR_CR19_Pos)                   /**< (CAN_TXBCR) Cancellation Request 19 Mask */
#define CAN_TXBCR_CR19(value)                 (CAN_TXBCR_CR19_Msk & ((value) << CAN_TXBCR_CR19_Pos))
#define CAN_TXBCR_CR20_Pos                    (20U)                                          /**< (CAN_TXBCR) Cancellation Request 20 Position */
#define CAN_TXBCR_CR20_Msk                    (0x1U << CAN_TXBCR_CR20_Pos)                   /**< (CAN_TXBCR) Cancellation Request 20 Mask */
#define CAN_TXBCR_CR20(value)                 (CAN_TXBCR_CR20_Msk & ((value) << CAN_TXBCR_CR20_Pos))
#define CAN_TXBCR_CR21_Pos                    (21U)                                          /**< (CAN_TXBCR) Cancellation Request 21 Position */
#define CAN_TXBCR_CR21_Msk                    (0x1U << CAN_TXBCR_CR21_Pos)                   /**< (CAN_TXBCR) Cancellation Request 21 Mask */
#define CAN_TXBCR_CR21(value)                 (CAN_TXBCR_CR21_Msk & ((value) << CAN_TXBCR_CR21_Pos))
#define CAN_TXBCR_CR22_Pos                    (22U)                                          /**< (CAN_TXBCR) Cancellation Request 22 Position */
#define CAN_TXBCR_CR22_Msk                    (0x1U << CAN_TXBCR_CR22_Pos)                   /**< (CAN_TXBCR) Cancellation Request 22 Mask */
#define CAN_TXBCR_CR22(value)                 (CAN_TXBCR_CR22_Msk & ((value) << CAN_TXBCR_CR22_Pos))
#define CAN_TXBCR_CR23_Pos                    (23U)                                          /**< (CAN_TXBCR) Cancellation Request 23 Position */
#define CAN_TXBCR_CR23_Msk                    (0x1U << CAN_TXBCR_CR23_Pos)                   /**< (CAN_TXBCR) Cancellation Request 23 Mask */
#define CAN_TXBCR_CR23(value)                 (CAN_TXBCR_CR23_Msk & ((value) << CAN_TXBCR_CR23_Pos))
#define CAN_TXBCR_CR24_Pos                    (24U)                                          /**< (CAN_TXBCR) Cancellation Request 24 Position */
#define CAN_TXBCR_CR24_Msk                    (0x1U << CAN_TXBCR_CR24_Pos)                   /**< (CAN_TXBCR) Cancellation Request 24 Mask */
#define CAN_TXBCR_CR24(value)                 (CAN_TXBCR_CR24_Msk & ((value) << CAN_TXBCR_CR24_Pos))
#define CAN_TXBCR_CR25_Pos                    (25U)                                          /**< (CAN_TXBCR) Cancellation Request 25 Position */
#define CAN_TXBCR_CR25_Msk                    (0x1U << CAN_TXBCR_CR25_Pos)                   /**< (CAN_TXBCR) Cancellation Request 25 Mask */
#define CAN_TXBCR_CR25(value)                 (CAN_TXBCR_CR25_Msk & ((value) << CAN_TXBCR_CR25_Pos))
#define CAN_TXBCR_CR26_Pos                    (26U)                                          /**< (CAN_TXBCR) Cancellation Request 26 Position */
#define CAN_TXBCR_CR26_Msk                    (0x1U << CAN_TXBCR_CR26_Pos)                   /**< (CAN_TXBCR) Cancellation Request 26 Mask */
#define CAN_TXBCR_CR26(value)                 (CAN_TXBCR_CR26_Msk & ((value) << CAN_TXBCR_CR26_Pos))
#define CAN_TXBCR_CR27_Pos                    (27U)                                          /**< (CAN_TXBCR) Cancellation Request 27 Position */
#define CAN_TXBCR_CR27_Msk                    (0x1U << CAN_TXBCR_CR27_Pos)                   /**< (CAN_TXBCR) Cancellation Request 27 Mask */
#define CAN_TXBCR_CR27(value)                 (CAN_TXBCR_CR27_Msk & ((value) << CAN_TXBCR_CR27_Pos))
#define CAN_TXBCR_CR28_Pos                    (28U)                                          /**< (CAN_TXBCR) Cancellation Request 28 Position */
#define CAN_TXBCR_CR28_Msk                    (0x1U << CAN_TXBCR_CR28_Pos)                   /**< (CAN_TXBCR) Cancellation Request 28 Mask */
#define CAN_TXBCR_CR28(value)                 (CAN_TXBCR_CR28_Msk & ((value) << CAN_TXBCR_CR28_Pos))
#define CAN_TXBCR_CR29_Pos                    (29U)                                          /**< (CAN_TXBCR) Cancellation Request 29 Position */
#define CAN_TXBCR_CR29_Msk                    (0x1U << CAN_TXBCR_CR29_Pos)                   /**< (CAN_TXBCR) Cancellation Request 29 Mask */
#define CAN_TXBCR_CR29(value)                 (CAN_TXBCR_CR29_Msk & ((value) << CAN_TXBCR_CR29_Pos))
#define CAN_TXBCR_CR30_Pos                    (30U)                                          /**< (CAN_TXBCR) Cancellation Request 30 Position */
#define CAN_TXBCR_CR30_Msk                    (0x1U << CAN_TXBCR_CR30_Pos)                   /**< (CAN_TXBCR) Cancellation Request 30 Mask */
#define CAN_TXBCR_CR30(value)                 (CAN_TXBCR_CR30_Msk & ((value) << CAN_TXBCR_CR30_Pos))
#define CAN_TXBCR_CR31_Pos                    (31U)                                          /**< (CAN_TXBCR) Cancellation Request 31 Position */
#define CAN_TXBCR_CR31_Msk                    (0x1U << CAN_TXBCR_CR31_Pos)                   /**< (CAN_TXBCR) Cancellation Request 31 Mask */
#define CAN_TXBCR_CR31(value)                 (CAN_TXBCR_CR31_Msk & ((value) << CAN_TXBCR_CR31_Pos))
#define CAN_TXBCR_Msk                         (0xFFFFFFFFUL)                                 /**< (CAN_TXBCR) Register Mask  */

/* -------- CAN_TXBTO : (CAN Offset: 0xD8) (R/  32) Tx Buffer Transmission Occurred -------- */
#define CAN_TXBTO_TO0_Pos                     (0U)                                           /**< (CAN_TXBTO) Transmission Occurred 0 Position */
#define CAN_TXBTO_TO0_Msk                     (0x1U << CAN_TXBTO_TO0_Pos)                    /**< (CAN_TXBTO) Transmission Occurred 0 Mask */
#define CAN_TXBTO_TO0(value)                  (CAN_TXBTO_TO0_Msk & ((value) << CAN_TXBTO_TO0_Pos))
#define CAN_TXBTO_TO1_Pos                     (1U)                                           /**< (CAN_TXBTO) Transmission Occurred 1 Position */
#define CAN_TXBTO_TO1_Msk                     (0x1U << CAN_TXBTO_TO1_Pos)                    /**< (CAN_TXBTO) Transmission Occurred 1 Mask */
#define CAN_TXBTO_TO1(value)                  (CAN_TXBTO_TO1_Msk & ((value) << CAN_TXBTO_TO1_Pos))
#define CAN_TXBTO_TO2_Pos                     (2U)                                           /**< (CAN_TXBTO) Transmission Occurred 2 Position */
#define CAN_TXBTO_TO2_Msk                     (0x1U << CAN_TXBTO_TO2_Pos)                    /**< (CAN_TXBTO) Transmission Occurred 2 Mask */
#define CAN_TXBTO_TO2(value)                  (CAN_TXBTO_TO2_Msk & ((value) << CAN_TXBTO_TO2_Pos))
#define CAN_TXBTO_TO3_Pos                     (3U)                                           /**< (CAN_TXBTO) Transmission Occurred 3 Position */
#define CAN_TXBTO_TO3_Msk                     (0x1U << CAN_TXBTO_TO3_Pos)                    /**< (CAN_TXBTO) Transmission Occurred 3 Mask */
#define CAN_TXBTO_TO3(value)                  (CAN_TXBTO_TO3_Msk & ((value) << CAN_TXBTO_TO3_Pos))
#define CAN_TXBTO_TO4_Pos                     (4U)                                           /**< (CAN_TXBTO) Transmission Occurred 4 Position */
#define CAN_TXBTO_TO4_Msk                     (0x1U << CAN_TXBTO_TO4_Pos)                    /**< (CAN_TXBTO) Transmission Occurred 4 Mask */
#define CAN_TXBTO_TO4(value)                  (CAN_TXBTO_TO4_Msk & ((value) << CAN_TXBTO_TO4_Pos))
#define CAN_TXBTO_TO5_Pos                     (5U)                                           /**< (CAN_TXBTO) Transmission Occurred 5 Position */
#define CAN_TXBTO_TO5_Msk                     (0x1U << CAN_TXBTO_TO5_Pos)                    /**< (CAN_TXBTO) Transmission Occurred 5 Mask */
#define CAN_TXBTO_TO5(value)                  (CAN_TXBTO_TO5_Msk & ((value) << CAN_TXBTO_TO5_Pos))
#define CAN_TXBTO_TO6_Pos                     (6U)                                           /**< (CAN_TXBTO) Transmission Occurred 6 Position */
#define CAN_TXBTO_TO6_Msk                     (0x1U << CAN_TXBTO_TO6_Pos)                    /**< (CAN_TXBTO) Transmission Occurred 6 Mask */
#define CAN_TXBTO_TO6(value)                  (CAN_TXBTO_TO6_Msk & ((value) << CAN_TXBTO_TO6_Pos))
#define CAN_TXBTO_TO7_Pos                     (7U)                                           /**< (CAN_TXBTO) Transmission Occurred 7 Position */
#define CAN_TXBTO_TO7_Msk                     (0x1U << CAN_TXBTO_TO7_Pos)                    /**< (CAN_TXBTO) Transmission Occurred 7 Mask */
#define CAN_TXBTO_TO7(value)                  (CAN_TXBTO_TO7_Msk & ((value) << CAN_TXBTO_TO7_Pos))
#define CAN_TXBTO_TO8_Pos                     (8U)                                           /**< (CAN_TXBTO) Transmission Occurred 8 Position */
#define CAN_TXBTO_TO8_Msk                     (0x1U << CAN_TXBTO_TO8_Pos)                    /**< (CAN_TXBTO) Transmission Occurred 8 Mask */
#define CAN_TXBTO_TO8(value)                  (CAN_TXBTO_TO8_Msk & ((value) << CAN_TXBTO_TO8_Pos))
#define CAN_TXBTO_TO9_Pos                     (9U)                                           /**< (CAN_TXBTO) Transmission Occurred 9 Position */
#define CAN_TXBTO_TO9_Msk                     (0x1U << CAN_TXBTO_TO9_Pos)                    /**< (CAN_TXBTO) Transmission Occurred 9 Mask */
#define CAN_TXBTO_TO9(value)                  (CAN_TXBTO_TO9_Msk & ((value) << CAN_TXBTO_TO9_Pos))
#define CAN_TXBTO_TO10_Pos                    (10U)                                          /**< (CAN_TXBTO) Transmission Occurred 10 Position */
#define CAN_TXBTO_TO10_Msk                    (0x1U << CAN_TXBTO_TO10_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 10 Mask */
#define CAN_TXBTO_TO10(value)                 (CAN_TXBTO_TO10_Msk & ((value) << CAN_TXBTO_TO10_Pos))
#define CAN_TXBTO_TO11_Pos                    (11U)                                          /**< (CAN_TXBTO) Transmission Occurred 11 Position */
#define CAN_TXBTO_TO11_Msk                    (0x1U << CAN_TXBTO_TO11_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 11 Mask */
#define CAN_TXBTO_TO11(value)                 (CAN_TXBTO_TO11_Msk & ((value) << CAN_TXBTO_TO11_Pos))
#define CAN_TXBTO_TO12_Pos                    (12U)                                          /**< (CAN_TXBTO) Transmission Occurred 12 Position */
#define CAN_TXBTO_TO12_Msk                    (0x1U << CAN_TXBTO_TO12_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 12 Mask */
#define CAN_TXBTO_TO12(value)                 (CAN_TXBTO_TO12_Msk & ((value) << CAN_TXBTO_TO12_Pos))
#define CAN_TXBTO_TO13_Pos                    (13U)                                          /**< (CAN_TXBTO) Transmission Occurred 13 Position */
#define CAN_TXBTO_TO13_Msk                    (0x1U << CAN_TXBTO_TO13_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 13 Mask */
#define CAN_TXBTO_TO13(value)                 (CAN_TXBTO_TO13_Msk & ((value) << CAN_TXBTO_TO13_Pos))
#define CAN_TXBTO_TO14_Pos                    (14U)                                          /**< (CAN_TXBTO) Transmission Occurred 14 Position */
#define CAN_TXBTO_TO14_Msk                    (0x1U << CAN_TXBTO_TO14_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 14 Mask */
#define CAN_TXBTO_TO14(value)                 (CAN_TXBTO_TO14_Msk & ((value) << CAN_TXBTO_TO14_Pos))
#define CAN_TXBTO_TO15_Pos                    (15U)                                          /**< (CAN_TXBTO) Transmission Occurred 15 Position */
#define CAN_TXBTO_TO15_Msk                    (0x1U << CAN_TXBTO_TO15_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 15 Mask */
#define CAN_TXBTO_TO15(value)                 (CAN_TXBTO_TO15_Msk & ((value) << CAN_TXBTO_TO15_Pos))
#define CAN_TXBTO_TO16_Pos                    (16U)                                          /**< (CAN_TXBTO) Transmission Occurred 16 Position */
#define CAN_TXBTO_TO16_Msk                    (0x1U << CAN_TXBTO_TO16_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 16 Mask */
#define CAN_TXBTO_TO16(value)                 (CAN_TXBTO_TO16_Msk & ((value) << CAN_TXBTO_TO16_Pos))
#define CAN_TXBTO_TO17_Pos                    (17U)                                          /**< (CAN_TXBTO) Transmission Occurred 17 Position */
#define CAN_TXBTO_TO17_Msk                    (0x1U << CAN_TXBTO_TO17_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 17 Mask */
#define CAN_TXBTO_TO17(value)                 (CAN_TXBTO_TO17_Msk & ((value) << CAN_TXBTO_TO17_Pos))
#define CAN_TXBTO_TO18_Pos                    (18U)                                          /**< (CAN_TXBTO) Transmission Occurred 18 Position */
#define CAN_TXBTO_TO18_Msk                    (0x1U << CAN_TXBTO_TO18_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 18 Mask */
#define CAN_TXBTO_TO18(value)                 (CAN_TXBTO_TO18_Msk & ((value) << CAN_TXBTO_TO18_Pos))
#define CAN_TXBTO_TO19_Pos                    (19U)                                          /**< (CAN_TXBTO) Transmission Occurred 19 Position */
#define CAN_TXBTO_TO19_Msk                    (0x1U << CAN_TXBTO_TO19_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 19 Mask */
#define CAN_TXBTO_TO19(value)                 (CAN_TXBTO_TO19_Msk & ((value) << CAN_TXBTO_TO19_Pos))
#define CAN_TXBTO_TO20_Pos                    (20U)                                          /**< (CAN_TXBTO) Transmission Occurred 20 Position */
#define CAN_TXBTO_TO20_Msk                    (0x1U << CAN_TXBTO_TO20_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 20 Mask */
#define CAN_TXBTO_TO20(value)                 (CAN_TXBTO_TO20_Msk & ((value) << CAN_TXBTO_TO20_Pos))
#define CAN_TXBTO_TO21_Pos                    (21U)                                          /**< (CAN_TXBTO) Transmission Occurred 21 Position */
#define CAN_TXBTO_TO21_Msk                    (0x1U << CAN_TXBTO_TO21_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 21 Mask */
#define CAN_TXBTO_TO21(value)                 (CAN_TXBTO_TO21_Msk & ((value) << CAN_TXBTO_TO21_Pos))
#define CAN_TXBTO_TO22_Pos                    (22U)                                          /**< (CAN_TXBTO) Transmission Occurred 22 Position */
#define CAN_TXBTO_TO22_Msk                    (0x1U << CAN_TXBTO_TO22_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 22 Mask */
#define CAN_TXBTO_TO22(value)                 (CAN_TXBTO_TO22_Msk & ((value) << CAN_TXBTO_TO22_Pos))
#define CAN_TXBTO_TO23_Pos                    (23U)                                          /**< (CAN_TXBTO) Transmission Occurred 23 Position */
#define CAN_TXBTO_TO23_Msk                    (0x1U << CAN_TXBTO_TO23_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 23 Mask */
#define CAN_TXBTO_TO23(value)                 (CAN_TXBTO_TO23_Msk & ((value) << CAN_TXBTO_TO23_Pos))
#define CAN_TXBTO_TO24_Pos                    (24U)                                          /**< (CAN_TXBTO) Transmission Occurred 24 Position */
#define CAN_TXBTO_TO24_Msk                    (0x1U << CAN_TXBTO_TO24_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 24 Mask */
#define CAN_TXBTO_TO24(value)                 (CAN_TXBTO_TO24_Msk & ((value) << CAN_TXBTO_TO24_Pos))
#define CAN_TXBTO_TO25_Pos                    (25U)                                          /**< (CAN_TXBTO) Transmission Occurred 25 Position */
#define CAN_TXBTO_TO25_Msk                    (0x1U << CAN_TXBTO_TO25_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 25 Mask */
#define CAN_TXBTO_TO25(value)                 (CAN_TXBTO_TO25_Msk & ((value) << CAN_TXBTO_TO25_Pos))
#define CAN_TXBTO_TO26_Pos                    (26U)                                          /**< (CAN_TXBTO) Transmission Occurred 26 Position */
#define CAN_TXBTO_TO26_Msk                    (0x1U << CAN_TXBTO_TO26_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 26 Mask */
#define CAN_TXBTO_TO26(value)                 (CAN_TXBTO_TO26_Msk & ((value) << CAN_TXBTO_TO26_Pos))
#define CAN_TXBTO_TO27_Pos                    (27U)                                          /**< (CAN_TXBTO) Transmission Occurred 27 Position */
#define CAN_TXBTO_TO27_Msk                    (0x1U << CAN_TXBTO_TO27_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 27 Mask */
#define CAN_TXBTO_TO27(value)                 (CAN_TXBTO_TO27_Msk & ((value) << CAN_TXBTO_TO27_Pos))
#define CAN_TXBTO_TO28_Pos                    (28U)                                          /**< (CAN_TXBTO) Transmission Occurred 28 Position */
#define CAN_TXBTO_TO28_Msk                    (0x1U << CAN_TXBTO_TO28_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 28 Mask */
#define CAN_TXBTO_TO28(value)                 (CAN_TXBTO_TO28_Msk & ((value) << CAN_TXBTO_TO28_Pos))
#define CAN_TXBTO_TO29_Pos                    (29U)                                          /**< (CAN_TXBTO) Transmission Occurred 29 Position */
#define CAN_TXBTO_TO29_Msk                    (0x1U << CAN_TXBTO_TO29_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 29 Mask */
#define CAN_TXBTO_TO29(value)                 (CAN_TXBTO_TO29_Msk & ((value) << CAN_TXBTO_TO29_Pos))
#define CAN_TXBTO_TO30_Pos                    (30U)                                          /**< (CAN_TXBTO) Transmission Occurred 30 Position */
#define CAN_TXBTO_TO30_Msk                    (0x1U << CAN_TXBTO_TO30_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 30 Mask */
#define CAN_TXBTO_TO30(value)                 (CAN_TXBTO_TO30_Msk & ((value) << CAN_TXBTO_TO30_Pos))
#define CAN_TXBTO_TO31_Pos                    (31U)                                          /**< (CAN_TXBTO) Transmission Occurred 31 Position */
#define CAN_TXBTO_TO31_Msk                    (0x1U << CAN_TXBTO_TO31_Pos)                   /**< (CAN_TXBTO) Transmission Occurred 31 Mask */
#define CAN_TXBTO_TO31(value)                 (CAN_TXBTO_TO31_Msk & ((value) << CAN_TXBTO_TO31_Pos))
#define CAN_TXBTO_Msk                         (0xFFFFFFFFUL)                                 /**< (CAN_TXBTO) Register Mask  */

/* -------- CAN_TXBCF : (CAN Offset: 0xDC) (R/  32) Tx Buffer Cancellation Finished -------- */
#define CAN_TXBCF_CF0_Pos                     (0U)                                           /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 0 Position */
#define CAN_TXBCF_CF0_Msk                     (0x1U << CAN_TXBCF_CF0_Pos)                    /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 0 Mask */
#define CAN_TXBCF_CF0(value)                  (CAN_TXBCF_CF0_Msk & ((value) << CAN_TXBCF_CF0_Pos))
#define CAN_TXBCF_CF1_Pos                     (1U)                                           /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 1 Position */
#define CAN_TXBCF_CF1_Msk                     (0x1U << CAN_TXBCF_CF1_Pos)                    /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 1 Mask */
#define CAN_TXBCF_CF1(value)                  (CAN_TXBCF_CF1_Msk & ((value) << CAN_TXBCF_CF1_Pos))
#define CAN_TXBCF_CF2_Pos                     (2U)                                           /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 2 Position */
#define CAN_TXBCF_CF2_Msk                     (0x1U << CAN_TXBCF_CF2_Pos)                    /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 2 Mask */
#define CAN_TXBCF_CF2(value)                  (CAN_TXBCF_CF2_Msk & ((value) << CAN_TXBCF_CF2_Pos))
#define CAN_TXBCF_CF3_Pos                     (3U)                                           /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 3 Position */
#define CAN_TXBCF_CF3_Msk                     (0x1U << CAN_TXBCF_CF3_Pos)                    /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 3 Mask */
#define CAN_TXBCF_CF3(value)                  (CAN_TXBCF_CF3_Msk & ((value) << CAN_TXBCF_CF3_Pos))
#define CAN_TXBCF_CF4_Pos                     (4U)                                           /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 4 Position */
#define CAN_TXBCF_CF4_Msk                     (0x1U << CAN_TXBCF_CF4_Pos)                    /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 4 Mask */
#define CAN_TXBCF_CF4(value)                  (CAN_TXBCF_CF4_Msk & ((value) << CAN_TXBCF_CF4_Pos))
#define CAN_TXBCF_CF5_Pos                     (5U)                                           /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 5 Position */
#define CAN_TXBCF_CF5_Msk                     (0x1U << CAN_TXBCF_CF5_Pos)                    /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 5 Mask */
#define CAN_TXBCF_CF5(value)                  (CAN_TXBCF_CF5_Msk & ((value) << CAN_TXBCF_CF5_Pos))
#define CAN_TXBCF_CF6_Pos                     (6U)                                           /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 6 Position */
#define CAN_TXBCF_CF6_Msk                     (0x1U << CAN_TXBCF_CF6_Pos)                    /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 6 Mask */
#define CAN_TXBCF_CF6(value)                  (CAN_TXBCF_CF6_Msk & ((value) << CAN_TXBCF_CF6_Pos))
#define CAN_TXBCF_CF7_Pos                     (7U)                                           /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 7 Position */
#define CAN_TXBCF_CF7_Msk                     (0x1U << CAN_TXBCF_CF7_Pos)                    /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 7 Mask */
#define CAN_TXBCF_CF7(value)                  (CAN_TXBCF_CF7_Msk & ((value) << CAN_TXBCF_CF7_Pos))
#define CAN_TXBCF_CF8_Pos                     (8U)                                           /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 8 Position */
#define CAN_TXBCF_CF8_Msk                     (0x1U << CAN_TXBCF_CF8_Pos)                    /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 8 Mask */
#define CAN_TXBCF_CF8(value)                  (CAN_TXBCF_CF8_Msk & ((value) << CAN_TXBCF_CF8_Pos))
#define CAN_TXBCF_CF9_Pos                     (9U)                                           /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 9 Position */
#define CAN_TXBCF_CF9_Msk                     (0x1U << CAN_TXBCF_CF9_Pos)                    /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 9 Mask */
#define CAN_TXBCF_CF9(value)                  (CAN_TXBCF_CF9_Msk & ((value) << CAN_TXBCF_CF9_Pos))
#define CAN_TXBCF_CF10_Pos                    (10U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 10 Position */
#define CAN_TXBCF_CF10_Msk                    (0x1U << CAN_TXBCF_CF10_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 10 Mask */
#define CAN_TXBCF_CF10(value)                 (CAN_TXBCF_CF10_Msk & ((value) << CAN_TXBCF_CF10_Pos))
#define CAN_TXBCF_CF11_Pos                    (11U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 11 Position */
#define CAN_TXBCF_CF11_Msk                    (0x1U << CAN_TXBCF_CF11_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 11 Mask */
#define CAN_TXBCF_CF11(value)                 (CAN_TXBCF_CF11_Msk & ((value) << CAN_TXBCF_CF11_Pos))
#define CAN_TXBCF_CF12_Pos                    (12U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 12 Position */
#define CAN_TXBCF_CF12_Msk                    (0x1U << CAN_TXBCF_CF12_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 12 Mask */
#define CAN_TXBCF_CF12(value)                 (CAN_TXBCF_CF12_Msk & ((value) << CAN_TXBCF_CF12_Pos))
#define CAN_TXBCF_CF13_Pos                    (13U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 13 Position */
#define CAN_TXBCF_CF13_Msk                    (0x1U << CAN_TXBCF_CF13_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 13 Mask */
#define CAN_TXBCF_CF13(value)                 (CAN_TXBCF_CF13_Msk & ((value) << CAN_TXBCF_CF13_Pos))
#define CAN_TXBCF_CF14_Pos                    (14U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 14 Position */
#define CAN_TXBCF_CF14_Msk                    (0x1U << CAN_TXBCF_CF14_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 14 Mask */
#define CAN_TXBCF_CF14(value)                 (CAN_TXBCF_CF14_Msk & ((value) << CAN_TXBCF_CF14_Pos))
#define CAN_TXBCF_CF15_Pos                    (15U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 15 Position */
#define CAN_TXBCF_CF15_Msk                    (0x1U << CAN_TXBCF_CF15_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 15 Mask */
#define CAN_TXBCF_CF15(value)                 (CAN_TXBCF_CF15_Msk & ((value) << CAN_TXBCF_CF15_Pos))
#define CAN_TXBCF_CF16_Pos                    (16U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 16 Position */
#define CAN_TXBCF_CF16_Msk                    (0x1U << CAN_TXBCF_CF16_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 16 Mask */
#define CAN_TXBCF_CF16(value)                 (CAN_TXBCF_CF16_Msk & ((value) << CAN_TXBCF_CF16_Pos))
#define CAN_TXBCF_CF17_Pos                    (17U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 17 Position */
#define CAN_TXBCF_CF17_Msk                    (0x1U << CAN_TXBCF_CF17_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 17 Mask */
#define CAN_TXBCF_CF17(value)                 (CAN_TXBCF_CF17_Msk & ((value) << CAN_TXBCF_CF17_Pos))
#define CAN_TXBCF_CF18_Pos                    (18U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 18 Position */
#define CAN_TXBCF_CF18_Msk                    (0x1U << CAN_TXBCF_CF18_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 18 Mask */
#define CAN_TXBCF_CF18(value)                 (CAN_TXBCF_CF18_Msk & ((value) << CAN_TXBCF_CF18_Pos))
#define CAN_TXBCF_CF19_Pos                    (19U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 19 Position */
#define CAN_TXBCF_CF19_Msk                    (0x1U << CAN_TXBCF_CF19_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 19 Mask */
#define CAN_TXBCF_CF19(value)                 (CAN_TXBCF_CF19_Msk & ((value) << CAN_TXBCF_CF19_Pos))
#define CAN_TXBCF_CF20_Pos                    (20U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 20 Position */
#define CAN_TXBCF_CF20_Msk                    (0x1U << CAN_TXBCF_CF20_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 20 Mask */
#define CAN_TXBCF_CF20(value)                 (CAN_TXBCF_CF20_Msk & ((value) << CAN_TXBCF_CF20_Pos))
#define CAN_TXBCF_CF21_Pos                    (21U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 21 Position */
#define CAN_TXBCF_CF21_Msk                    (0x1U << CAN_TXBCF_CF21_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 21 Mask */
#define CAN_TXBCF_CF21(value)                 (CAN_TXBCF_CF21_Msk & ((value) << CAN_TXBCF_CF21_Pos))
#define CAN_TXBCF_CF22_Pos                    (22U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 22 Position */
#define CAN_TXBCF_CF22_Msk                    (0x1U << CAN_TXBCF_CF22_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 22 Mask */
#define CAN_TXBCF_CF22(value)                 (CAN_TXBCF_CF22_Msk & ((value) << CAN_TXBCF_CF22_Pos))
#define CAN_TXBCF_CF23_Pos                    (23U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 23 Position */
#define CAN_TXBCF_CF23_Msk                    (0x1U << CAN_TXBCF_CF23_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 23 Mask */
#define CAN_TXBCF_CF23(value)                 (CAN_TXBCF_CF23_Msk & ((value) << CAN_TXBCF_CF23_Pos))
#define CAN_TXBCF_CF24_Pos                    (24U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 24 Position */
#define CAN_TXBCF_CF24_Msk                    (0x1U << CAN_TXBCF_CF24_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 24 Mask */
#define CAN_TXBCF_CF24(value)                 (CAN_TXBCF_CF24_Msk & ((value) << CAN_TXBCF_CF24_Pos))
#define CAN_TXBCF_CF25_Pos                    (25U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 25 Position */
#define CAN_TXBCF_CF25_Msk                    (0x1U << CAN_TXBCF_CF25_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 25 Mask */
#define CAN_TXBCF_CF25(value)                 (CAN_TXBCF_CF25_Msk & ((value) << CAN_TXBCF_CF25_Pos))
#define CAN_TXBCF_CF26_Pos                    (26U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 26 Position */
#define CAN_TXBCF_CF26_Msk                    (0x1U << CAN_TXBCF_CF26_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 26 Mask */
#define CAN_TXBCF_CF26(value)                 (CAN_TXBCF_CF26_Msk & ((value) << CAN_TXBCF_CF26_Pos))
#define CAN_TXBCF_CF27_Pos                    (27U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 27 Position */
#define CAN_TXBCF_CF27_Msk                    (0x1U << CAN_TXBCF_CF27_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 27 Mask */
#define CAN_TXBCF_CF27(value)                 (CAN_TXBCF_CF27_Msk & ((value) << CAN_TXBCF_CF27_Pos))
#define CAN_TXBCF_CF28_Pos                    (28U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 28 Position */
#define CAN_TXBCF_CF28_Msk                    (0x1U << CAN_TXBCF_CF28_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 28 Mask */
#define CAN_TXBCF_CF28(value)                 (CAN_TXBCF_CF28_Msk & ((value) << CAN_TXBCF_CF28_Pos))
#define CAN_TXBCF_CF29_Pos                    (29U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 29 Position */
#define CAN_TXBCF_CF29_Msk                    (0x1U << CAN_TXBCF_CF29_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 29 Mask */
#define CAN_TXBCF_CF29(value)                 (CAN_TXBCF_CF29_Msk & ((value) << CAN_TXBCF_CF29_Pos))
#define CAN_TXBCF_CF30_Pos                    (30U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 30 Position */
#define CAN_TXBCF_CF30_Msk                    (0x1U << CAN_TXBCF_CF30_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 30 Mask */
#define CAN_TXBCF_CF30(value)                 (CAN_TXBCF_CF30_Msk & ((value) << CAN_TXBCF_CF30_Pos))
#define CAN_TXBCF_CF31_Pos                    (31U)                                          /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 31 Position */
#define CAN_TXBCF_CF31_Msk                    (0x1U << CAN_TXBCF_CF31_Pos)                   /**< (CAN_TXBCF) Tx Buffer Cancellation Finished 31 Mask */
#define CAN_TXBCF_CF31(value)                 (CAN_TXBCF_CF31_Msk & ((value) << CAN_TXBCF_CF31_Pos))
#define CAN_TXBCF_Msk                         (0xFFFFFFFFUL)                                 /**< (CAN_TXBCF) Register Mask  */

/* -------- CAN_TXBTIE : (CAN Offset: 0xE0) (R/W 32) Tx Buffer Transmission Interrupt Enable -------- */
#define CAN_TXBTIE_TIE0_Pos                   (0U)                                           /**< (CAN_TXBTIE) Transmission Interrupt Enable 0 Position */
#define CAN_TXBTIE_TIE0_Msk                   (0x1U << CAN_TXBTIE_TIE0_Pos)                  /**< (CAN_TXBTIE) Transmission Interrupt Enable 0 Mask */
#define CAN_TXBTIE_TIE0(value)                (CAN_TXBTIE_TIE0_Msk & ((value) << CAN_TXBTIE_TIE0_Pos))
#define CAN_TXBTIE_TIE1_Pos                   (1U)                                           /**< (CAN_TXBTIE) Transmission Interrupt Enable 1 Position */
#define CAN_TXBTIE_TIE1_Msk                   (0x1U << CAN_TXBTIE_TIE1_Pos)                  /**< (CAN_TXBTIE) Transmission Interrupt Enable 1 Mask */
#define CAN_TXBTIE_TIE1(value)                (CAN_TXBTIE_TIE1_Msk & ((value) << CAN_TXBTIE_TIE1_Pos))
#define CAN_TXBTIE_TIE2_Pos                   (2U)                                           /**< (CAN_TXBTIE) Transmission Interrupt Enable 2 Position */
#define CAN_TXBTIE_TIE2_Msk                   (0x1U << CAN_TXBTIE_TIE2_Pos)                  /**< (CAN_TXBTIE) Transmission Interrupt Enable 2 Mask */
#define CAN_TXBTIE_TIE2(value)                (CAN_TXBTIE_TIE2_Msk & ((value) << CAN_TXBTIE_TIE2_Pos))
#define CAN_TXBTIE_TIE3_Pos                   (3U)                                           /**< (CAN_TXBTIE) Transmission Interrupt Enable 3 Position */
#define CAN_TXBTIE_TIE3_Msk                   (0x1U << CAN_TXBTIE_TIE3_Pos)                  /**< (CAN_TXBTIE) Transmission Interrupt Enable 3 Mask */
#define CAN_TXBTIE_TIE3(value)                (CAN_TXBTIE_TIE3_Msk & ((value) << CAN_TXBTIE_TIE3_Pos))
#define CAN_TXBTIE_TIE4_Pos                   (4U)                                           /**< (CAN_TXBTIE) Transmission Interrupt Enable 4 Position */
#define CAN_TXBTIE_TIE4_Msk                   (0x1U << CAN_TXBTIE_TIE4_Pos)                  /**< (CAN_TXBTIE) Transmission Interrupt Enable 4 Mask */
#define CAN_TXBTIE_TIE4(value)                (CAN_TXBTIE_TIE4_Msk & ((value) << CAN_TXBTIE_TIE4_Pos))
#define CAN_TXBTIE_TIE5_Pos                   (5U)                                           /**< (CAN_TXBTIE) Transmission Interrupt Enable 5 Position */
#define CAN_TXBTIE_TIE5_Msk                   (0x1U << CAN_TXBTIE_TIE5_Pos)                  /**< (CAN_TXBTIE) Transmission Interrupt Enable 5 Mask */
#define CAN_TXBTIE_TIE5(value)                (CAN_TXBTIE_TIE5_Msk & ((value) << CAN_TXBTIE_TIE5_Pos))
#define CAN_TXBTIE_TIE6_Pos                   (6U)                                           /**< (CAN_TXBTIE) Transmission Interrupt Enable 6 Position */
#define CAN_TXBTIE_TIE6_Msk                   (0x1U << CAN_TXBTIE_TIE6_Pos)                  /**< (CAN_TXBTIE) Transmission Interrupt Enable 6 Mask */
#define CAN_TXBTIE_TIE6(value)                (CAN_TXBTIE_TIE6_Msk & ((value) << CAN_TXBTIE_TIE6_Pos))
#define CAN_TXBTIE_TIE7_Pos                   (7U)                                           /**< (CAN_TXBTIE) Transmission Interrupt Enable 7 Position */
#define CAN_TXBTIE_TIE7_Msk                   (0x1U << CAN_TXBTIE_TIE7_Pos)                  /**< (CAN_TXBTIE) Transmission Interrupt Enable 7 Mask */
#define CAN_TXBTIE_TIE7(value)                (CAN_TXBTIE_TIE7_Msk & ((value) << CAN_TXBTIE_TIE7_Pos))
#define CAN_TXBTIE_TIE8_Pos                   (8U)                                           /**< (CAN_TXBTIE) Transmission Interrupt Enable 8 Position */
#define CAN_TXBTIE_TIE8_Msk                   (0x1U << CAN_TXBTIE_TIE8_Pos)                  /**< (CAN_TXBTIE) Transmission Interrupt Enable 8 Mask */
#define CAN_TXBTIE_TIE8(value)                (CAN_TXBTIE_TIE8_Msk & ((value) << CAN_TXBTIE_TIE8_Pos))
#define CAN_TXBTIE_TIE9_Pos                   (9U)                                           /**< (CAN_TXBTIE) Transmission Interrupt Enable 9 Position */
#define CAN_TXBTIE_TIE9_Msk                   (0x1U << CAN_TXBTIE_TIE9_Pos)                  /**< (CAN_TXBTIE) Transmission Interrupt Enable 9 Mask */
#define CAN_TXBTIE_TIE9(value)                (CAN_TXBTIE_TIE9_Msk & ((value) << CAN_TXBTIE_TIE9_Pos))
#define CAN_TXBTIE_TIE10_Pos                  (10U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 10 Position */
#define CAN_TXBTIE_TIE10_Msk                  (0x1U << CAN_TXBTIE_TIE10_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 10 Mask */
#define CAN_TXBTIE_TIE10(value)               (CAN_TXBTIE_TIE10_Msk & ((value) << CAN_TXBTIE_TIE10_Pos))
#define CAN_TXBTIE_TIE11_Pos                  (11U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 11 Position */
#define CAN_TXBTIE_TIE11_Msk                  (0x1U << CAN_TXBTIE_TIE11_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 11 Mask */
#define CAN_TXBTIE_TIE11(value)               (CAN_TXBTIE_TIE11_Msk & ((value) << CAN_TXBTIE_TIE11_Pos))
#define CAN_TXBTIE_TIE12_Pos                  (12U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 12 Position */
#define CAN_TXBTIE_TIE12_Msk                  (0x1U << CAN_TXBTIE_TIE12_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 12 Mask */
#define CAN_TXBTIE_TIE12(value)               (CAN_TXBTIE_TIE12_Msk & ((value) << CAN_TXBTIE_TIE12_Pos))
#define CAN_TXBTIE_TIE13_Pos                  (13U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 13 Position */
#define CAN_TXBTIE_TIE13_Msk                  (0x1U << CAN_TXBTIE_TIE13_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 13 Mask */
#define CAN_TXBTIE_TIE13(value)               (CAN_TXBTIE_TIE13_Msk & ((value) << CAN_TXBTIE_TIE13_Pos))
#define CAN_TXBTIE_TIE14_Pos                  (14U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 14 Position */
#define CAN_TXBTIE_TIE14_Msk                  (0x1U << CAN_TXBTIE_TIE14_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 14 Mask */
#define CAN_TXBTIE_TIE14(value)               (CAN_TXBTIE_TIE14_Msk & ((value) << CAN_TXBTIE_TIE14_Pos))
#define CAN_TXBTIE_TIE15_Pos                  (15U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 15 Position */
#define CAN_TXBTIE_TIE15_Msk                  (0x1U << CAN_TXBTIE_TIE15_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 15 Mask */
#define CAN_TXBTIE_TIE15(value)               (CAN_TXBTIE_TIE15_Msk & ((value) << CAN_TXBTIE_TIE15_Pos))
#define CAN_TXBTIE_TIE16_Pos                  (16U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 16 Position */
#define CAN_TXBTIE_TIE16_Msk                  (0x1U << CAN_TXBTIE_TIE16_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 16 Mask */
#define CAN_TXBTIE_TIE16(value)               (CAN_TXBTIE_TIE16_Msk & ((value) << CAN_TXBTIE_TIE16_Pos))
#define CAN_TXBTIE_TIE17_Pos                  (17U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 17 Position */
#define CAN_TXBTIE_TIE17_Msk                  (0x1U << CAN_TXBTIE_TIE17_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 17 Mask */
#define CAN_TXBTIE_TIE17(value)               (CAN_TXBTIE_TIE17_Msk & ((value) << CAN_TXBTIE_TIE17_Pos))
#define CAN_TXBTIE_TIE18_Pos                  (18U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 18 Position */
#define CAN_TXBTIE_TIE18_Msk                  (0x1U << CAN_TXBTIE_TIE18_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 18 Mask */
#define CAN_TXBTIE_TIE18(value)               (CAN_TXBTIE_TIE18_Msk & ((value) << CAN_TXBTIE_TIE18_Pos))
#define CAN_TXBTIE_TIE19_Pos                  (19U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 19 Position */
#define CAN_TXBTIE_TIE19_Msk                  (0x1U << CAN_TXBTIE_TIE19_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 19 Mask */
#define CAN_TXBTIE_TIE19(value)               (CAN_TXBTIE_TIE19_Msk & ((value) << CAN_TXBTIE_TIE19_Pos))
#define CAN_TXBTIE_TIE20_Pos                  (20U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 20 Position */
#define CAN_TXBTIE_TIE20_Msk                  (0x1U << CAN_TXBTIE_TIE20_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 20 Mask */
#define CAN_TXBTIE_TIE20(value)               (CAN_TXBTIE_TIE20_Msk & ((value) << CAN_TXBTIE_TIE20_Pos))
#define CAN_TXBTIE_TIE21_Pos                  (21U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 21 Position */
#define CAN_TXBTIE_TIE21_Msk                  (0x1U << CAN_TXBTIE_TIE21_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 21 Mask */
#define CAN_TXBTIE_TIE21(value)               (CAN_TXBTIE_TIE21_Msk & ((value) << CAN_TXBTIE_TIE21_Pos))
#define CAN_TXBTIE_TIE22_Pos                  (22U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 22 Position */
#define CAN_TXBTIE_TIE22_Msk                  (0x1U << CAN_TXBTIE_TIE22_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 22 Mask */
#define CAN_TXBTIE_TIE22(value)               (CAN_TXBTIE_TIE22_Msk & ((value) << CAN_TXBTIE_TIE22_Pos))
#define CAN_TXBTIE_TIE23_Pos                  (23U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 23 Position */
#define CAN_TXBTIE_TIE23_Msk                  (0x1U << CAN_TXBTIE_TIE23_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 23 Mask */
#define CAN_TXBTIE_TIE23(value)               (CAN_TXBTIE_TIE23_Msk & ((value) << CAN_TXBTIE_TIE23_Pos))
#define CAN_TXBTIE_TIE24_Pos                  (24U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 24 Position */
#define CAN_TXBTIE_TIE24_Msk                  (0x1U << CAN_TXBTIE_TIE24_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 24 Mask */
#define CAN_TXBTIE_TIE24(value)               (CAN_TXBTIE_TIE24_Msk & ((value) << CAN_TXBTIE_TIE24_Pos))
#define CAN_TXBTIE_TIE25_Pos                  (25U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 25 Position */
#define CAN_TXBTIE_TIE25_Msk                  (0x1U << CAN_TXBTIE_TIE25_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 25 Mask */
#define CAN_TXBTIE_TIE25(value)               (CAN_TXBTIE_TIE25_Msk & ((value) << CAN_TXBTIE_TIE25_Pos))
#define CAN_TXBTIE_TIE26_Pos                  (26U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 26 Position */
#define CAN_TXBTIE_TIE26_Msk                  (0x1U << CAN_TXBTIE_TIE26_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 26 Mask */
#define CAN_TXBTIE_TIE26(value)               (CAN_TXBTIE_TIE26_Msk & ((value) << CAN_TXBTIE_TIE26_Pos))
#define CAN_TXBTIE_TIE27_Pos                  (27U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 27 Position */
#define CAN_TXBTIE_TIE27_Msk                  (0x1U << CAN_TXBTIE_TIE27_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 27 Mask */
#define CAN_TXBTIE_TIE27(value)               (CAN_TXBTIE_TIE27_Msk & ((value) << CAN_TXBTIE_TIE27_Pos))
#define CAN_TXBTIE_TIE28_Pos                  (28U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 28 Position */
#define CAN_TXBTIE_TIE28_Msk                  (0x1U << CAN_TXBTIE_TIE28_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 28 Mask */
#define CAN_TXBTIE_TIE28(value)               (CAN_TXBTIE_TIE28_Msk & ((value) << CAN_TXBTIE_TIE28_Pos))
#define CAN_TXBTIE_TIE29_Pos                  (29U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 29 Position */
#define CAN_TXBTIE_TIE29_Msk                  (0x1U << CAN_TXBTIE_TIE29_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 29 Mask */
#define CAN_TXBTIE_TIE29(value)               (CAN_TXBTIE_TIE29_Msk & ((value) << CAN_TXBTIE_TIE29_Pos))
#define CAN_TXBTIE_TIE30_Pos                  (30U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 30 Position */
#define CAN_TXBTIE_TIE30_Msk                  (0x1U << CAN_TXBTIE_TIE30_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 30 Mask */
#define CAN_TXBTIE_TIE30(value)               (CAN_TXBTIE_TIE30_Msk & ((value) << CAN_TXBTIE_TIE30_Pos))
#define CAN_TXBTIE_TIE31_Pos                  (31U)                                          /**< (CAN_TXBTIE) Transmission Interrupt Enable 31 Position */
#define CAN_TXBTIE_TIE31_Msk                  (0x1U << CAN_TXBTIE_TIE31_Pos)                 /**< (CAN_TXBTIE) Transmission Interrupt Enable 31 Mask */
#define CAN_TXBTIE_TIE31(value)               (CAN_TXBTIE_TIE31_Msk & ((value) << CAN_TXBTIE_TIE31_Pos))
#define CAN_TXBTIE_Msk                        (0xFFFFFFFFUL)                                 /**< (CAN_TXBTIE) Register Mask  */

/* -------- CAN_TXBCIE : (CAN Offset: 0xE4) (R/W 32) Tx Buffer Cancellation Finished Interrupt Enable -------- */
#define CAN_TXBCIE_CFIE0_Pos                  (0U)                                           /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 0 Position */
#define CAN_TXBCIE_CFIE0_Msk                  (0x1U << CAN_TXBCIE_CFIE0_Pos)                 /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 0 Mask */
#define CAN_TXBCIE_CFIE0(value)               (CAN_TXBCIE_CFIE0_Msk & ((value) << CAN_TXBCIE_CFIE0_Pos))
#define CAN_TXBCIE_CFIE1_Pos                  (1U)                                           /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 1 Position */
#define CAN_TXBCIE_CFIE1_Msk                  (0x1U << CAN_TXBCIE_CFIE1_Pos)                 /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 1 Mask */
#define CAN_TXBCIE_CFIE1(value)               (CAN_TXBCIE_CFIE1_Msk & ((value) << CAN_TXBCIE_CFIE1_Pos))
#define CAN_TXBCIE_CFIE2_Pos                  (2U)                                           /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 2 Position */
#define CAN_TXBCIE_CFIE2_Msk                  (0x1U << CAN_TXBCIE_CFIE2_Pos)                 /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 2 Mask */
#define CAN_TXBCIE_CFIE2(value)               (CAN_TXBCIE_CFIE2_Msk & ((value) << CAN_TXBCIE_CFIE2_Pos))
#define CAN_TXBCIE_CFIE3_Pos                  (3U)                                           /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 3 Position */
#define CAN_TXBCIE_CFIE3_Msk                  (0x1U << CAN_TXBCIE_CFIE3_Pos)                 /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 3 Mask */
#define CAN_TXBCIE_CFIE3(value)               (CAN_TXBCIE_CFIE3_Msk & ((value) << CAN_TXBCIE_CFIE3_Pos))
#define CAN_TXBCIE_CFIE4_Pos                  (4U)                                           /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 4 Position */
#define CAN_TXBCIE_CFIE4_Msk                  (0x1U << CAN_TXBCIE_CFIE4_Pos)                 /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 4 Mask */
#define CAN_TXBCIE_CFIE4(value)               (CAN_TXBCIE_CFIE4_Msk & ((value) << CAN_TXBCIE_CFIE4_Pos))
#define CAN_TXBCIE_CFIE5_Pos                  (5U)                                           /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 5 Position */
#define CAN_TXBCIE_CFIE5_Msk                  (0x1U << CAN_TXBCIE_CFIE5_Pos)                 /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 5 Mask */
#define CAN_TXBCIE_CFIE5(value)               (CAN_TXBCIE_CFIE5_Msk & ((value) << CAN_TXBCIE_CFIE5_Pos))
#define CAN_TXBCIE_CFIE6_Pos                  (6U)                                           /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 6 Position */
#define CAN_TXBCIE_CFIE6_Msk                  (0x1U << CAN_TXBCIE_CFIE6_Pos)                 /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 6 Mask */
#define CAN_TXBCIE_CFIE6(value)               (CAN_TXBCIE_CFIE6_Msk & ((value) << CAN_TXBCIE_CFIE6_Pos))
#define CAN_TXBCIE_CFIE7_Pos                  (7U)                                           /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 7 Position */
#define CAN_TXBCIE_CFIE7_Msk                  (0x1U << CAN_TXBCIE_CFIE7_Pos)                 /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 7 Mask */
#define CAN_TXBCIE_CFIE7(value)               (CAN_TXBCIE_CFIE7_Msk & ((value) << CAN_TXBCIE_CFIE7_Pos))
#define CAN_TXBCIE_CFIE8_Pos                  (8U)                                           /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 8 Position */
#define CAN_TXBCIE_CFIE8_Msk                  (0x1U << CAN_TXBCIE_CFIE8_Pos)                 /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 8 Mask */
#define CAN_TXBCIE_CFIE8(value)               (CAN_TXBCIE_CFIE8_Msk & ((value) << CAN_TXBCIE_CFIE8_Pos))
#define CAN_TXBCIE_CFIE9_Pos                  (9U)                                           /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 9 Position */
#define CAN_TXBCIE_CFIE9_Msk                  (0x1U << CAN_TXBCIE_CFIE9_Pos)                 /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 9 Mask */
#define CAN_TXBCIE_CFIE9(value)               (CAN_TXBCIE_CFIE9_Msk & ((value) << CAN_TXBCIE_CFIE9_Pos))
#define CAN_TXBCIE_CFIE10_Pos                 (10U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 10 Position */
#define CAN_TXBCIE_CFIE10_Msk                 (0x1U << CAN_TXBCIE_CFIE10_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 10 Mask */
#define CAN_TXBCIE_CFIE10(value)              (CAN_TXBCIE_CFIE10_Msk & ((value) << CAN_TXBCIE_CFIE10_Pos))
#define CAN_TXBCIE_CFIE11_Pos                 (11U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 11 Position */
#define CAN_TXBCIE_CFIE11_Msk                 (0x1U << CAN_TXBCIE_CFIE11_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 11 Mask */
#define CAN_TXBCIE_CFIE11(value)              (CAN_TXBCIE_CFIE11_Msk & ((value) << CAN_TXBCIE_CFIE11_Pos))
#define CAN_TXBCIE_CFIE12_Pos                 (12U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 12 Position */
#define CAN_TXBCIE_CFIE12_Msk                 (0x1U << CAN_TXBCIE_CFIE12_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 12 Mask */
#define CAN_TXBCIE_CFIE12(value)              (CAN_TXBCIE_CFIE12_Msk & ((value) << CAN_TXBCIE_CFIE12_Pos))
#define CAN_TXBCIE_CFIE13_Pos                 (13U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 13 Position */
#define CAN_TXBCIE_CFIE13_Msk                 (0x1U << CAN_TXBCIE_CFIE13_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 13 Mask */
#define CAN_TXBCIE_CFIE13(value)              (CAN_TXBCIE_CFIE13_Msk & ((value) << CAN_TXBCIE_CFIE13_Pos))
#define CAN_TXBCIE_CFIE14_Pos                 (14U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 14 Position */
#define CAN_TXBCIE_CFIE14_Msk                 (0x1U << CAN_TXBCIE_CFIE14_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 14 Mask */
#define CAN_TXBCIE_CFIE14(value)              (CAN_TXBCIE_CFIE14_Msk & ((value) << CAN_TXBCIE_CFIE14_Pos))
#define CAN_TXBCIE_CFIE15_Pos                 (15U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 15 Position */
#define CAN_TXBCIE_CFIE15_Msk                 (0x1U << CAN_TXBCIE_CFIE15_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 15 Mask */
#define CAN_TXBCIE_CFIE15(value)              (CAN_TXBCIE_CFIE15_Msk & ((value) << CAN_TXBCIE_CFIE15_Pos))
#define CAN_TXBCIE_CFIE16_Pos                 (16U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 16 Position */
#define CAN_TXBCIE_CFIE16_Msk                 (0x1U << CAN_TXBCIE_CFIE16_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 16 Mask */
#define CAN_TXBCIE_CFIE16(value)              (CAN_TXBCIE_CFIE16_Msk & ((value) << CAN_TXBCIE_CFIE16_Pos))
#define CAN_TXBCIE_CFIE17_Pos                 (17U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 17 Position */
#define CAN_TXBCIE_CFIE17_Msk                 (0x1U << CAN_TXBCIE_CFIE17_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 17 Mask */
#define CAN_TXBCIE_CFIE17(value)              (CAN_TXBCIE_CFIE17_Msk & ((value) << CAN_TXBCIE_CFIE17_Pos))
#define CAN_TXBCIE_CFIE18_Pos                 (18U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 18 Position */
#define CAN_TXBCIE_CFIE18_Msk                 (0x1U << CAN_TXBCIE_CFIE18_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 18 Mask */
#define CAN_TXBCIE_CFIE18(value)              (CAN_TXBCIE_CFIE18_Msk & ((value) << CAN_TXBCIE_CFIE18_Pos))
#define CAN_TXBCIE_CFIE19_Pos                 (19U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 19 Position */
#define CAN_TXBCIE_CFIE19_Msk                 (0x1U << CAN_TXBCIE_CFIE19_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 19 Mask */
#define CAN_TXBCIE_CFIE19(value)              (CAN_TXBCIE_CFIE19_Msk & ((value) << CAN_TXBCIE_CFIE19_Pos))
#define CAN_TXBCIE_CFIE20_Pos                 (20U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 20 Position */
#define CAN_TXBCIE_CFIE20_Msk                 (0x1U << CAN_TXBCIE_CFIE20_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 20 Mask */
#define CAN_TXBCIE_CFIE20(value)              (CAN_TXBCIE_CFIE20_Msk & ((value) << CAN_TXBCIE_CFIE20_Pos))
#define CAN_TXBCIE_CFIE21_Pos                 (21U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 21 Position */
#define CAN_TXBCIE_CFIE21_Msk                 (0x1U << CAN_TXBCIE_CFIE21_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 21 Mask */
#define CAN_TXBCIE_CFIE21(value)              (CAN_TXBCIE_CFIE21_Msk & ((value) << CAN_TXBCIE_CFIE21_Pos))
#define CAN_TXBCIE_CFIE22_Pos                 (22U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 22 Position */
#define CAN_TXBCIE_CFIE22_Msk                 (0x1U << CAN_TXBCIE_CFIE22_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 22 Mask */
#define CAN_TXBCIE_CFIE22(value)              (CAN_TXBCIE_CFIE22_Msk & ((value) << CAN_TXBCIE_CFIE22_Pos))
#define CAN_TXBCIE_CFIE23_Pos                 (23U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 23 Position */
#define CAN_TXBCIE_CFIE23_Msk                 (0x1U << CAN_TXBCIE_CFIE23_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 23 Mask */
#define CAN_TXBCIE_CFIE23(value)              (CAN_TXBCIE_CFIE23_Msk & ((value) << CAN_TXBCIE_CFIE23_Pos))
#define CAN_TXBCIE_CFIE24_Pos                 (24U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 24 Position */
#define CAN_TXBCIE_CFIE24_Msk                 (0x1U << CAN_TXBCIE_CFIE24_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 24 Mask */
#define CAN_TXBCIE_CFIE24(value)              (CAN_TXBCIE_CFIE24_Msk & ((value) << CAN_TXBCIE_CFIE24_Pos))
#define CAN_TXBCIE_CFIE25_Pos                 (25U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 25 Position */
#define CAN_TXBCIE_CFIE25_Msk                 (0x1U << CAN_TXBCIE_CFIE25_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 25 Mask */
#define CAN_TXBCIE_CFIE25(value)              (CAN_TXBCIE_CFIE25_Msk & ((value) << CAN_TXBCIE_CFIE25_Pos))
#define CAN_TXBCIE_CFIE26_Pos                 (26U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 26 Position */
#define CAN_TXBCIE_CFIE26_Msk                 (0x1U << CAN_TXBCIE_CFIE26_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 26 Mask */
#define CAN_TXBCIE_CFIE26(value)              (CAN_TXBCIE_CFIE26_Msk & ((value) << CAN_TXBCIE_CFIE26_Pos))
#define CAN_TXBCIE_CFIE27_Pos                 (27U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 27 Position */
#define CAN_TXBCIE_CFIE27_Msk                 (0x1U << CAN_TXBCIE_CFIE27_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 27 Mask */
#define CAN_TXBCIE_CFIE27(value)              (CAN_TXBCIE_CFIE27_Msk & ((value) << CAN_TXBCIE_CFIE27_Pos))
#define CAN_TXBCIE_CFIE28_Pos                 (28U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 28 Position */
#define CAN_TXBCIE_CFIE28_Msk                 (0x1U << CAN_TXBCIE_CFIE28_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 28 Mask */
#define CAN_TXBCIE_CFIE28(value)              (CAN_TXBCIE_CFIE28_Msk & ((value) << CAN_TXBCIE_CFIE28_Pos))
#define CAN_TXBCIE_CFIE29_Pos                 (29U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 29 Position */
#define CAN_TXBCIE_CFIE29_Msk                 (0x1U << CAN_TXBCIE_CFIE29_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 29 Mask */
#define CAN_TXBCIE_CFIE29(value)              (CAN_TXBCIE_CFIE29_Msk & ((value) << CAN_TXBCIE_CFIE29_Pos))
#define CAN_TXBCIE_CFIE30_Pos                 (30U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 30 Position */
#define CAN_TXBCIE_CFIE30_Msk                 (0x1U << CAN_TXBCIE_CFIE30_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 30 Mask */
#define CAN_TXBCIE_CFIE30(value)              (CAN_TXBCIE_CFIE30_Msk & ((value) << CAN_TXBCIE_CFIE30_Pos))
#define CAN_TXBCIE_CFIE31_Pos                 (31U)                                          /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 31 Position */
#define CAN_TXBCIE_CFIE31_Msk                 (0x1U << CAN_TXBCIE_CFIE31_Pos)                /**< (CAN_TXBCIE) Cancellation Finished Interrupt Enable 31 Mask */
#define CAN_TXBCIE_CFIE31(value)              (CAN_TXBCIE_CFIE31_Msk & ((value) << CAN_TXBCIE_CFIE31_Pos))
#define CAN_TXBCIE_Msk                        (0xFFFFFFFFUL)                                 /**< (CAN_TXBCIE) Register Mask  */

/* -------- CAN_TXEFC : (CAN Offset: 0xF0) (R/W 32) Tx Event FIFO Configuration -------- */
#define CAN_TXEFC_EFSA_Pos                    (0U)                                           /**< (CAN_TXEFC) Event FIFO Start Address Position */
#define CAN_TXEFC_EFSA_Msk                    (0xFFFFU << CAN_TXEFC_EFSA_Pos)                /**< (CAN_TXEFC) Event FIFO Start Address Mask */
#define CAN_TXEFC_EFSA(value)                 (CAN_TXEFC_EFSA_Msk & ((value) << CAN_TXEFC_EFSA_Pos))
#define CAN_TXEFC_EFS_Pos                     (16U)                                          /**< (CAN_TXEFC) Event FIFO Size Position */
#define CAN_TXEFC_EFS_Msk                     (0x3FU << CAN_TXEFC_EFS_Pos)                   /**< (CAN_TXEFC) Event FIFO Size Mask */
#define CAN_TXEFC_EFS(value)                  (CAN_TXEFC_EFS_Msk & ((value) << CAN_TXEFC_EFS_Pos))
#define CAN_TXEFC_EFWM_Pos                    (24U)                                          /**< (CAN_TXEFC) Event FIFO Watermark Position */
#define CAN_TXEFC_EFWM_Msk                    (0x3FU << CAN_TXEFC_EFWM_Pos)                  /**< (CAN_TXEFC) Event FIFO Watermark Mask */
#define CAN_TXEFC_EFWM(value)                 (CAN_TXEFC_EFWM_Msk & ((value) << CAN_TXEFC_EFWM_Pos))
#define CAN_TXEFC_Msk                         (0x3F3FFFFFUL)                                 /**< (CAN_TXEFC) Register Mask  */

/* -------- CAN_TXEFS : (CAN Offset: 0xF4) (R/  32) Tx Event FIFO Status -------- */
#define CAN_TXEFS_EFFL_Pos                    (0U)                                           /**< (CAN_TXEFS) Event FIFO Fill Level Position */
#define CAN_TXEFS_EFFL_Msk                    (0x3FU << CAN_TXEFS_EFFL_Pos)                  /**< (CAN_TXEFS) Event FIFO Fill Level Mask */
#define CAN_TXEFS_EFFL(value)                 (CAN_TXEFS_EFFL_Msk & ((value) << CAN_TXEFS_EFFL_Pos))
#define CAN_TXEFS_EFGI_Pos                    (8U)                                           /**< (CAN_TXEFS) Event FIFO Get Index Position */
#define CAN_TXEFS_EFGI_Msk                    (0x1FU << CAN_TXEFS_EFGI_Pos)                  /**< (CAN_TXEFS) Event FIFO Get Index Mask */
#define CAN_TXEFS_EFGI(value)                 (CAN_TXEFS_EFGI_Msk & ((value) << CAN_TXEFS_EFGI_Pos))
#define CAN_TXEFS_EFPI_Pos                    (16U)                                          /**< (CAN_TXEFS) Event FIFO Put Index Position */
#define CAN_TXEFS_EFPI_Msk                    (0x1FU << CAN_TXEFS_EFPI_Pos)                  /**< (CAN_TXEFS) Event FIFO Put Index Mask */
#define CAN_TXEFS_EFPI(value)                 (CAN_TXEFS_EFPI_Msk & ((value) << CAN_TXEFS_EFPI_Pos))
#define CAN_TXEFS_EFF_Pos                     (24U)                                          /**< (CAN_TXEFS) Event FIFO Full Position */
#define CAN_TXEFS_EFF_Msk                     (0x1U << CAN_TXEFS_EFF_Pos)                    /**< (CAN_TXEFS) Event FIFO Full Mask */
#define CAN_TXEFS_EFF(value)                  (CAN_TXEFS_EFF_Msk & ((value) << CAN_TXEFS_EFF_Pos))
#define CAN_TXEFS_TEFL_Pos                    (25U)                                          /**< (CAN_TXEFS) Tx Event FIFO Element Lost Position */
#define CAN_TXEFS_TEFL_Msk                    (0x1U << CAN_TXEFS_TEFL_Pos)                   /**< (CAN_TXEFS) Tx Event FIFO Element Lost Mask */
#define CAN_TXEFS_TEFL(value)                 (CAN_TXEFS_TEFL_Msk & ((value) << CAN_TXEFS_TEFL_Pos))
#define CAN_TXEFS_Msk                         (0x031F1F3FUL)                                 /**< (CAN_TXEFS) Register Mask  */

/* -------- CAN_TXEFA : (CAN Offset: 0xF8) (R/W 32) Tx Event FIFO Acknowledge -------- */
#define CAN_TXEFA_EFAI_Pos                    (0U)                                           /**< (CAN_TXEFA) Event FIFO Acknowledge Index Position */
#define CAN_TXEFA_EFAI_Msk                    (0x1FU << CAN_TXEFA_EFAI_Pos)                  /**< (CAN_TXEFA) Event FIFO Acknowledge Index Mask */
#define CAN_TXEFA_EFAI(value)                 (CAN_TXEFA_EFAI_Msk & ((value) << CAN_TXEFA_EFAI_Pos))
#define CAN_TXEFA_Msk                         (0x0000001FUL)                                 /**< (CAN_TXEFA) Register Mask  */

/** \brief CAN register offsets definitions */
#define CAN_CREL_OFFSET                (0x00)         /**< (CAN_CREL) Core Release Offset */
#define CAN_ENDN_OFFSET                (0x04)         /**< (CAN_ENDN) Endian Offset */
#define CAN_MRCFG_OFFSET               (0x08)         /**< (CAN_MRCFG) Message RAM Configuration Offset */
#define CAN_DBTP_OFFSET                (0x0C)         /**< (CAN_DBTP) Fast Bit Timing and Prescaler Offset */
#define CAN_TEST_OFFSET                (0x10)         /**< (CAN_TEST) Test Offset */
#define CAN_RWD_OFFSET                 (0x14)         /**< (CAN_RWD) RAM Watchdog Offset */
#define CAN_CCCR_OFFSET                (0x18)         /**< (CAN_CCCR) CC Control Offset */
#define CAN_NBTP_OFFSET                (0x1C)         /**< (CAN_NBTP) Nominal Bit Timing and Prescaler Offset */
#define CAN_TSCC_OFFSET                (0x20)         /**< (CAN_TSCC) Timestamp Counter Configuration Offset */
#define CAN_TSCV_OFFSET                (0x24)         /**< (CAN_TSCV) Timestamp Counter Value Offset */
#define CAN_TOCC_OFFSET                (0x28)         /**< (CAN_TOCC) Timeout Counter Configuration Offset */
#define CAN_TOCV_OFFSET                (0x2C)         /**< (CAN_TOCV) Timeout Counter Value Offset */
#define CAN_ECR_OFFSET                 (0x40)         /**< (CAN_ECR) Error Counter Offset */
#define CAN_PSR_OFFSET                 (0x44)         /**< (CAN_PSR) Protocol Status Offset */
#define CAN_TDCR_OFFSET                (0x48)         /**< (CAN_TDCR) Extended ID Filter Configuration Offset */
#define CAN_IR_OFFSET                  (0x50)         /**< (CAN_IR) Interrupt Offset */
#define CAN_IE_OFFSET                  (0x54)         /**< (CAN_IE) Interrupt Enable Offset */
#define CAN_ILS_OFFSET                 (0x58)         /**< (CAN_ILS) Interrupt Line Select Offset */
#define CAN_ILE_OFFSET                 (0x5C)         /**< (CAN_ILE) Interrupt Line Enable Offset */
#define CAN_GFC_OFFSET                 (0x80)         /**< (CAN_GFC) Global Filter Configuration Offset */
#define CAN_SIDFC_OFFSET               (0x84)         /**< (CAN_SIDFC) Standard ID Filter Configuration Offset */
#define CAN_XIDFC_OFFSET               (0x88)         /**< (CAN_XIDFC) Extended ID Filter Configuration Offset */
#define CAN_XIDAM_OFFSET               (0x90)         /**< (CAN_XIDAM) Extended ID AND Mask Offset */
#define CAN_HPMS_OFFSET                (0x94)         /**< (CAN_HPMS) High Priority Message Status Offset */
#define CAN_NDAT1_OFFSET               (0x98)         /**< (CAN_NDAT1) New Data 1 Offset */
#define CAN_NDAT2_OFFSET               (0x9C)         /**< (CAN_NDAT2) New Data 2 Offset */
#define CAN_RXF0C_OFFSET               (0xA0)         /**< (CAN_RXF0C) Rx FIFO 0 Configuration Offset */
#define CAN_RXF0S_OFFSET               (0xA4)         /**< (CAN_RXF0S) Rx FIFO 0 Status Offset */
#define CAN_RXF0A_OFFSET               (0xA8)         /**< (CAN_RXF0A) Rx FIFO 0 Acknowledge Offset */
#define CAN_RXBC_OFFSET                (0xAC)         /**< (CAN_RXBC) Rx Buffer Configuration Offset */
#define CAN_RXF1C_OFFSET               (0xB0)         /**< (CAN_RXF1C) Rx FIFO 1 Configuration Offset */
#define CAN_RXF1S_OFFSET               (0xB4)         /**< (CAN_RXF1S) Rx FIFO 1 Status Offset */
#define CAN_RXF1A_OFFSET               (0xB8)         /**< (CAN_RXF1A) Rx FIFO 1 Acknowledge Offset */
#define CAN_RXESC_OFFSET               (0xBC)         /**< (CAN_RXESC) Rx Buffer / FIFO Element Size Configuration Offset */
#define CAN_TXBC_OFFSET                (0xC0)         /**< (CAN_TXBC) Tx Buffer Configuration Offset */
#define CAN_TXFQS_OFFSET               (0xC4)         /**< (CAN_TXFQS) Tx FIFO / Queue Status Offset */
#define CAN_TXESC_OFFSET               (0xC8)         /**< (CAN_TXESC) Tx Buffer Element Size Configuration Offset */
#define CAN_TXBRP_OFFSET               (0xCC)         /**< (CAN_TXBRP) Tx Buffer Request Pending Offset */
#define CAN_TXBAR_OFFSET               (0xD0)         /**< (CAN_TXBAR) Tx Buffer Add Request Offset */
#define CAN_TXBCR_OFFSET               (0xD4)         /**< (CAN_TXBCR) Tx Buffer Cancellation Request Offset */
#define CAN_TXBTO_OFFSET               (0xD8)         /**< (CAN_TXBTO) Tx Buffer Transmission Occurred Offset */
#define CAN_TXBCF_OFFSET               (0xDC)         /**< (CAN_TXBCF) Tx Buffer Cancellation Finished Offset */
#define CAN_TXBTIE_OFFSET              (0xE0)         /**< (CAN_TXBTIE) Tx Buffer Transmission Interrupt Enable Offset */
#define CAN_TXBCIE_OFFSET              (0xE4)         /**< (CAN_TXBCIE) Tx Buffer Cancellation Finished Interrupt Enable Offset */
#define CAN_TXEFC_OFFSET               (0xF0)         /**< (CAN_TXEFC) Tx Event FIFO Configuration Offset */
#define CAN_TXEFS_OFFSET               (0xF4)         /**< (CAN_TXEFS) Tx Event FIFO Status Offset */
#define CAN_TXEFA_OFFSET               (0xF8)         /**< (CAN_TXEFA) Tx Event FIFO Acknowledge Offset */

/** \brief CAN register API structure */
typedef struct
{
  __I   uint32_t                       CAN_CREL;        /**< Offset: 0x00 (R/   32) Core Release */
  __I   uint32_t                       CAN_ENDN;        /**< Offset: 0x04 (R/   32) Endian */
  __IO  uint32_t                       CAN_MRCFG;       /**< Offset: 0x08 (R/W  32) Message RAM Configuration */
  __IO  uint32_t                       CAN_DBTP;        /**< Offset: 0x0c (R/W  32) Fast Bit Timing and Prescaler */
  __IO  uint32_t                       CAN_TEST;        /**< Offset: 0x10 (R/W  32) Test */
  __IO  uint32_t                       CAN_RWD;         /**< Offset: 0x14 (R/W  32) RAM Watchdog */
  __IO  uint32_t                       CAN_CCCR;        /**< Offset: 0x18 (R/W  32) CC Control */
  __IO  uint32_t                       CAN_NBTP;        /**< Offset: 0x1c (R/W  32) Nominal Bit Timing and Prescaler */
  __IO  uint32_t                       CAN_TSCC;        /**< Offset: 0x20 (R/W  32) Timestamp Counter Configuration */
  __I   uint32_t                       CAN_TSCV;        /**< Offset: 0x24 (R/   32) Timestamp Counter Value */
  __IO  uint32_t                       CAN_TOCC;        /**< Offset: 0x28 (R/W  32) Timeout Counter Configuration */
  __IO  uint32_t                       CAN_TOCV;        /**< Offset: 0x2c (R/W  32) Timeout Counter Value */
  __I   uint8_t                        Reserved1[0x10];
  __I   uint32_t                       CAN_ECR;         /**< Offset: 0x40 (R/   32) Error Counter */
  __I   uint32_t                       CAN_PSR;         /**< Offset: 0x44 (R/   32) Protocol Status */
  __IO  uint32_t                       CAN_TDCR;        /**< Offset: 0x48 (R/W  32) Extended ID Filter Configuration */
  __I   uint8_t                        Reserved2[0x04];
  __IO  uint32_t                       CAN_IR;          /**< Offset: 0x50 (R/W  32) Interrupt */
  __IO  uint32_t                       CAN_IE;          /**< Offset: 0x54 (R/W  32) Interrupt Enable */
  __IO  uint32_t                       CAN_ILS;         /**< Offset: 0x58 (R/W  32) Interrupt Line Select */
  __IO  uint32_t                       CAN_ILE;         /**< Offset: 0x5c (R/W  32) Interrupt Line Enable */
  __I   uint8_t                        Reserved3[0x20];
  __IO  uint32_t                       CAN_GFC;         /**< Offset: 0x80 (R/W  32) Global Filter Configuration */
  __IO  uint32_t                       CAN_SIDFC;       /**< Offset: 0x84 (R/W  32) Standard ID Filter Configuration */
  __IO  uint32_t                       CAN_XIDFC;       /**< Offset: 0x88 (R/W  32) Extended ID Filter Configuration */
  __I   uint8_t                        Reserved4[0x04];
  __IO  uint32_t                       CAN_XIDAM;       /**< Offset: 0x90 (R/W  32) Extended ID AND Mask */
  __I   uint32_t                       CAN_HPMS;        /**< Offset: 0x94 (R/   32) High Priority Message Status */
  __IO  uint32_t                       CAN_NDAT1;       /**< Offset: 0x98 (R/W  32) New Data 1 */
  __IO  uint32_t                       CAN_NDAT2;       /**< Offset: 0x9c (R/W  32) New Data 2 */
  __IO  uint32_t                       CAN_RXF0C;       /**< Offset: 0xa0 (R/W  32) Rx FIFO 0 Configuration */
  __I   uint32_t                       CAN_RXF0S;       /**< Offset: 0xa4 (R/   32) Rx FIFO 0 Status */
  __IO  uint32_t                       CAN_RXF0A;       /**< Offset: 0xa8 (R/W  32) Rx FIFO 0 Acknowledge */
  __IO  uint32_t                       CAN_RXBC;        /**< Offset: 0xac (R/W  32) Rx Buffer Configuration */
  __IO  uint32_t                       CAN_RXF1C;       /**< Offset: 0xb0 (R/W  32) Rx FIFO 1 Configuration */
  __I   uint32_t                       CAN_RXF1S;       /**< Offset: 0xb4 (R/   32) Rx FIFO 1 Status */
  __IO  uint32_t                       CAN_RXF1A;       /**< Offset: 0xb8 (R/W  32) Rx FIFO 1 Acknowledge */
  __IO  uint32_t                       CAN_RXESC;       /**< Offset: 0xbc (R/W  32) Rx Buffer / FIFO Element Size Configuration */
  __IO  uint32_t                       CAN_TXBC;        /**< Offset: 0xc0 (R/W  32) Tx Buffer Configuration */
  __I   uint32_t                       CAN_TXFQS;       /**< Offset: 0xc4 (R/   32) Tx FIFO / Queue Status */
  __IO  uint32_t                       CAN_TXESC;       /**< Offset: 0xc8 (R/W  32) Tx Buffer Element Size Configuration */
  __I   uint32_t                       CAN_TXBRP;       /**< Offset: 0xcc (R/   32) Tx Buffer Request Pending */
  __IO  uint32_t                       CAN_TXBAR;       /**< Offset: 0xd0 (R/W  32) Tx Buffer Add Request */
  __IO  uint32_t                       CAN_TXBCR;       /**< Offset: 0xd4 (R/W  32) Tx Buffer Cancellation Request */
  __I   uint32_t                       CAN_TXBTO;       /**< Offset: 0xd8 (R/   32) Tx Buffer Transmission Occurred */
  __I   uint32_t                       CAN_TXBCF;       /**< Offset: 0xdc (R/   32) Tx Buffer Cancellation Finished */
  __IO  uint32_t                       CAN_TXBTIE;      /**< Offset: 0xe0 (R/W  32) Tx Buffer Transmission Interrupt Enable */
  __IO  uint32_t                       CAN_TXBCIE;      /**< Offset: 0xe4 (R/W  32) Tx Buffer Cancellation Finished Interrupt Enable */
  __I   uint8_t                        Reserved5[0x08];
  __IO  uint32_t                       CAN_TXEFC;       /**< Offset: 0xf0 (R/W  32) Tx Event FIFO Configuration */
  __I   uint32_t                       CAN_TXEFS;       /**< Offset: 0xf4 (R/   32) Tx Event FIFO Status */
  __IO  uint32_t                       CAN_TXEFA;       /**< Offset: 0xf8 (R/W  32) Tx Event FIFO Acknowledge */
} can_registers_t;
/** @}  end of Control Area Network */

#endif /* SAMC_SAMC21_CAN_MODULE_H */

