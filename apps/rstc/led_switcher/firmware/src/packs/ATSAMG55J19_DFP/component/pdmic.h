/**
 * \brief Header file for SAMG/SAMG55 PDMIC
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
#ifndef SAMG_SAMG55_PDMIC_MODULE_H
#define SAMG_SAMG55_PDMIC_MODULE_H

/** \addtogroup SAMG_SAMG55 Pulse Density Modulation Interface Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_PDMIC                                 */
/* ========================================================================== */

/* -------- PDMIC_CR : (PDMIC Offset: 0x00) (R/W 32) Control Register -------- */
#define PDMIC_CR_SWRST_Pos                    (0U)                                           /**< (PDMIC_CR) Software Reset Position */
#define PDMIC_CR_SWRST_Msk                    (0x1U << PDMIC_CR_SWRST_Pos)                   /**< (PDMIC_CR) Software Reset Mask */
#define PDMIC_CR_SWRST(value)                 (PDMIC_CR_SWRST_Msk & ((value) << PDMIC_CR_SWRST_Pos))
#define PDMIC_CR_ENPDM_Pos                    (4U)                                           /**< (PDMIC_CR) Enable PDM Position */
#define PDMIC_CR_ENPDM_Msk                    (0x1U << PDMIC_CR_ENPDM_Pos)                   /**< (PDMIC_CR) Enable PDM Mask */
#define PDMIC_CR_ENPDM(value)                 (PDMIC_CR_ENPDM_Msk & ((value) << PDMIC_CR_ENPDM_Pos))
#define PDMIC_CR_Msk                          (0x00000011UL)                                 /**< (PDMIC_CR) Register Mask  */

/* -------- PDMIC_MR : (PDMIC Offset: 0x04) (R/W 32) Mode Register -------- */
#define PDMIC_MR_CLKS_Pos                     (4U)                                           /**< (PDMIC_MR) Clock Source Selection Position */
#define PDMIC_MR_CLKS_Msk                     (0x1U << PDMIC_MR_CLKS_Pos)                    /**< (PDMIC_MR) Clock Source Selection Mask */
#define PDMIC_MR_CLKS(value)                  (PDMIC_MR_CLKS_Msk & ((value) << PDMIC_MR_CLKS_Pos))
#define PDMIC_MR_PRESCAL_Pos                  (8U)                                           /**< (PDMIC_MR) Prescaler Rate Selection Position */
#define PDMIC_MR_PRESCAL_Msk                  (0x7FU << PDMIC_MR_PRESCAL_Pos)                /**< (PDMIC_MR) Prescaler Rate Selection Mask */
#define PDMIC_MR_PRESCAL(value)               (PDMIC_MR_PRESCAL_Msk & ((value) << PDMIC_MR_PRESCAL_Pos))
#define PDMIC_MR_Msk                          (0x00007F10UL)                                 /**< (PDMIC_MR) Register Mask  */

/* -------- PDMIC_CDR : (PDMIC Offset: 0x14) (R/  32) Converted Data Register -------- */
#define PDMIC_CDR_DATA_Pos                    (0U)                                           /**< (PDMIC_CDR) Data Converted Position */
#define PDMIC_CDR_DATA_Msk                    (0xFFFFFFFFU << PDMIC_CDR_DATA_Pos)            /**< (PDMIC_CDR) Data Converted Mask */
#define PDMIC_CDR_DATA(value)                 (PDMIC_CDR_DATA_Msk & ((value) << PDMIC_CDR_DATA_Pos))
#define PDMIC_CDR_Msk                         (0xFFFFFFFFUL)                                 /**< (PDMIC_CDR) Register Mask  */

/* -------- PDMIC_IER : (PDMIC Offset: 0x18) ( /W 32) Interrupt Enable Register -------- */
#define PDMIC_IER_DRDY_Pos                    (24U)                                          /**< (PDMIC_IER) Data Ready Interrupt Enable Position */
#define PDMIC_IER_DRDY_Msk                    (0x1U << PDMIC_IER_DRDY_Pos)                   /**< (PDMIC_IER) Data Ready Interrupt Enable Mask */
#define PDMIC_IER_DRDY(value)                 (PDMIC_IER_DRDY_Msk & ((value) << PDMIC_IER_DRDY_Pos))
#define PDMIC_IER_OVRE_Pos                    (25U)                                          /**< (PDMIC_IER) Overrun Error Interrupt Enable Position */
#define PDMIC_IER_OVRE_Msk                    (0x1U << PDMIC_IER_OVRE_Pos)                   /**< (PDMIC_IER) Overrun Error Interrupt Enable Mask */
#define PDMIC_IER_OVRE(value)                 (PDMIC_IER_OVRE_Msk & ((value) << PDMIC_IER_OVRE_Pos))
#define PDMIC_IER_ENDRX_Pos                   (27U)                                          /**< (PDMIC_IER) End of Receive Buffer Interrupt Enable Position */
#define PDMIC_IER_ENDRX_Msk                   (0x1U << PDMIC_IER_ENDRX_Pos)                  /**< (PDMIC_IER) End of Receive Buffer Interrupt Enable Mask */
#define PDMIC_IER_ENDRX(value)                (PDMIC_IER_ENDRX_Msk & ((value) << PDMIC_IER_ENDRX_Pos))
#define PDMIC_IER_RXBUFF_Pos                  (28U)                                          /**< (PDMIC_IER) Receive Buffer Full Interrupt Enable Position */
#define PDMIC_IER_RXBUFF_Msk                  (0x1U << PDMIC_IER_RXBUFF_Pos)                 /**< (PDMIC_IER) Receive Buffer Full Interrupt Enable Mask */
#define PDMIC_IER_RXBUFF(value)               (PDMIC_IER_RXBUFF_Msk & ((value) << PDMIC_IER_RXBUFF_Pos))
#define PDMIC_IER_Msk                         (0x1B000000UL)                                 /**< (PDMIC_IER) Register Mask  */

/* -------- PDMIC_IDR : (PDMIC Offset: 0x1C) ( /W 32) Interrupt Disable Register -------- */
#define PDMIC_IDR_DRDY_Pos                    (24U)                                          /**< (PDMIC_IDR) Data Ready Interrupt Disable Position */
#define PDMIC_IDR_DRDY_Msk                    (0x1U << PDMIC_IDR_DRDY_Pos)                   /**< (PDMIC_IDR) Data Ready Interrupt Disable Mask */
#define PDMIC_IDR_DRDY(value)                 (PDMIC_IDR_DRDY_Msk & ((value) << PDMIC_IDR_DRDY_Pos))
#define PDMIC_IDR_OVRE_Pos                    (25U)                                          /**< (PDMIC_IDR) General Overrun Error Interrupt Disable Position */
#define PDMIC_IDR_OVRE_Msk                    (0x1U << PDMIC_IDR_OVRE_Pos)                   /**< (PDMIC_IDR) General Overrun Error Interrupt Disable Mask */
#define PDMIC_IDR_OVRE(value)                 (PDMIC_IDR_OVRE_Msk & ((value) << PDMIC_IDR_OVRE_Pos))
#define PDMIC_IDR_ENDRX_Pos                   (27U)                                          /**< (PDMIC_IDR) End of Receive Buffer Interrupt Disable Position */
#define PDMIC_IDR_ENDRX_Msk                   (0x1U << PDMIC_IDR_ENDRX_Pos)                  /**< (PDMIC_IDR) End of Receive Buffer Interrupt Disable Mask */
#define PDMIC_IDR_ENDRX(value)                (PDMIC_IDR_ENDRX_Msk & ((value) << PDMIC_IDR_ENDRX_Pos))
#define PDMIC_IDR_RXBUFF_Pos                  (28U)                                          /**< (PDMIC_IDR) Receive Buffer Full Interrupt Disable Position */
#define PDMIC_IDR_RXBUFF_Msk                  (0x1U << PDMIC_IDR_RXBUFF_Pos)                 /**< (PDMIC_IDR) Receive Buffer Full Interrupt Disable Mask */
#define PDMIC_IDR_RXBUFF(value)               (PDMIC_IDR_RXBUFF_Msk & ((value) << PDMIC_IDR_RXBUFF_Pos))
#define PDMIC_IDR_Msk                         (0x1B000000UL)                                 /**< (PDMIC_IDR) Register Mask  */

/* -------- PDMIC_IMR : (PDMIC Offset: 0x20) (R/  32) Interrupt Mask Register -------- */
#define PDMIC_IMR_DRDY_Pos                    (24U)                                          /**< (PDMIC_IMR) Data Ready Interrupt Mask Position */
#define PDMIC_IMR_DRDY_Msk                    (0x1U << PDMIC_IMR_DRDY_Pos)                   /**< (PDMIC_IMR) Data Ready Interrupt Mask Mask */
#define PDMIC_IMR_DRDY(value)                 (PDMIC_IMR_DRDY_Msk & ((value) << PDMIC_IMR_DRDY_Pos))
#define PDMIC_IMR_OVRE_Pos                    (25U)                                          /**< (PDMIC_IMR) General Overrun Error Interrupt Mask Position */
#define PDMIC_IMR_OVRE_Msk                    (0x1U << PDMIC_IMR_OVRE_Pos)                   /**< (PDMIC_IMR) General Overrun Error Interrupt Mask Mask */
#define PDMIC_IMR_OVRE(value)                 (PDMIC_IMR_OVRE_Msk & ((value) << PDMIC_IMR_OVRE_Pos))
#define PDMIC_IMR_ENDRX_Pos                   (27U)                                          /**< (PDMIC_IMR) End of Receive Buffer Interrupt Mask Position */
#define PDMIC_IMR_ENDRX_Msk                   (0x1U << PDMIC_IMR_ENDRX_Pos)                  /**< (PDMIC_IMR) End of Receive Buffer Interrupt Mask Mask */
#define PDMIC_IMR_ENDRX(value)                (PDMIC_IMR_ENDRX_Msk & ((value) << PDMIC_IMR_ENDRX_Pos))
#define PDMIC_IMR_RXBUFF_Pos                  (28U)                                          /**< (PDMIC_IMR) Receive Buffer Full Interrupt Mask Position */
#define PDMIC_IMR_RXBUFF_Msk                  (0x1U << PDMIC_IMR_RXBUFF_Pos)                 /**< (PDMIC_IMR) Receive Buffer Full Interrupt Mask Mask */
#define PDMIC_IMR_RXBUFF(value)               (PDMIC_IMR_RXBUFF_Msk & ((value) << PDMIC_IMR_RXBUFF_Pos))
#define PDMIC_IMR_Msk                         (0x1B000000UL)                                 /**< (PDMIC_IMR) Register Mask  */

/* -------- PDMIC_ISR : (PDMIC Offset: 0x24) (R/  32) Interrupt Status Register -------- */
#define PDMIC_ISR_FIFOCNT_Pos                 (16U)                                          /**< (PDMIC_ISR) FIFO Count Position */
#define PDMIC_ISR_FIFOCNT_Msk                 (0xFFU << PDMIC_ISR_FIFOCNT_Pos)               /**< (PDMIC_ISR) FIFO Count Mask */
#define PDMIC_ISR_FIFOCNT(value)              (PDMIC_ISR_FIFOCNT_Msk & ((value) << PDMIC_ISR_FIFOCNT_Pos))
#define PDMIC_ISR_DRDY_Pos                    (24U)                                          /**< (PDMIC_ISR) Data Ready Position */
#define PDMIC_ISR_DRDY_Msk                    (0x1U << PDMIC_ISR_DRDY_Pos)                   /**< (PDMIC_ISR) Data Ready Mask */
#define PDMIC_ISR_DRDY(value)                 (PDMIC_ISR_DRDY_Msk & ((value) << PDMIC_ISR_DRDY_Pos))
#define PDMIC_ISR_OVRE_Pos                    (25U)                                          /**< (PDMIC_ISR) Overrun Error Position */
#define PDMIC_ISR_OVRE_Msk                    (0x1U << PDMIC_ISR_OVRE_Pos)                   /**< (PDMIC_ISR) Overrun Error Mask */
#define PDMIC_ISR_OVRE(value)                 (PDMIC_ISR_OVRE_Msk & ((value) << PDMIC_ISR_OVRE_Pos))
#define PDMIC_ISR_ENDRX_Pos                   (27U)                                          /**< (PDMIC_ISR) End of RX Buffer Position */
#define PDMIC_ISR_ENDRX_Msk                   (0x1U << PDMIC_ISR_ENDRX_Pos)                  /**< (PDMIC_ISR) End of RX Buffer Mask */
#define PDMIC_ISR_ENDRX(value)                (PDMIC_ISR_ENDRX_Msk & ((value) << PDMIC_ISR_ENDRX_Pos))
#define PDMIC_ISR_RXBUFF_Pos                  (28U)                                          /**< (PDMIC_ISR) RX Buffer Full Position */
#define PDMIC_ISR_RXBUFF_Msk                  (0x1U << PDMIC_ISR_RXBUFF_Pos)                 /**< (PDMIC_ISR) RX Buffer Full Mask */
#define PDMIC_ISR_RXBUFF(value)               (PDMIC_ISR_RXBUFF_Msk & ((value) << PDMIC_ISR_RXBUFF_Pos))
#define PDMIC_ISR_Msk                         (0x1BFF0000UL)                                 /**< (PDMIC_ISR) Register Mask  */

/* -------- PDMIC_DSPR0 : (PDMIC Offset: 0x58) (R/W 32) DSP Configuration Register 0 -------- */
#define PDMIC_DSPR0_HPFBYP_Pos                (1U)                                           /**< (PDMIC_DSPR0) High-Pass Filter Bypass Position */
#define PDMIC_DSPR0_HPFBYP_Msk                (0x1U << PDMIC_DSPR0_HPFBYP_Pos)               /**< (PDMIC_DSPR0) High-Pass Filter Bypass Mask */
#define PDMIC_DSPR0_HPFBYP(value)             (PDMIC_DSPR0_HPFBYP_Msk & ((value) << PDMIC_DSPR0_HPFBYP_Pos))
#define PDMIC_DSPR0_SINBYP_Pos                (2U)                                           /**< (PDMIC_DSPR0) SINCC Filter Bypass Position */
#define PDMIC_DSPR0_SINBYP_Msk                (0x1U << PDMIC_DSPR0_SINBYP_Pos)               /**< (PDMIC_DSPR0) SINCC Filter Bypass Mask */
#define PDMIC_DSPR0_SINBYP(value)             (PDMIC_DSPR0_SINBYP_Msk & ((value) << PDMIC_DSPR0_SINBYP_Pos))
#define PDMIC_DSPR0_SIZE_Pos                  (3U)                                           /**< (PDMIC_DSPR0) Data Size Position */
#define PDMIC_DSPR0_SIZE_Msk                  (0x1U << PDMIC_DSPR0_SIZE_Pos)                 /**< (PDMIC_DSPR0) Data Size Mask */
#define PDMIC_DSPR0_SIZE(value)               (PDMIC_DSPR0_SIZE_Msk & ((value) << PDMIC_DSPR0_SIZE_Pos))
#define PDMIC_DSPR0_OSR_Pos                   (4U)                                           /**< (PDMIC_DSPR0) Oversampling Ratio Position */
#define PDMIC_DSPR0_OSR_Msk                   (0x7U << PDMIC_DSPR0_OSR_Pos)                  /**< (PDMIC_DSPR0) Oversampling Ratio Mask */
#define PDMIC_DSPR0_OSR(value)                (PDMIC_DSPR0_OSR_Msk & ((value) << PDMIC_DSPR0_OSR_Pos))
#define   PDMIC_DSPR0_OSR_128_Val             (0U)                                           /**< (PDMIC_DSPR0) Oversampling ratio is 128  */
#define   PDMIC_DSPR0_OSR_64_Val              (1U)                                           /**< (PDMIC_DSPR0) Oversampling ratio is 64  */
#define PDMIC_DSPR0_OSR_128                   (PDMIC_DSPR0_OSR_128_Val << PDMIC_DSPR0_OSR_Pos) /**< (PDMIC_DSPR0) Oversampling ratio is 128 Position  */
#define PDMIC_DSPR0_OSR_64                    (PDMIC_DSPR0_OSR_64_Val << PDMIC_DSPR0_OSR_Pos) /**< (PDMIC_DSPR0) Oversampling ratio is 64 Position  */
#define PDMIC_DSPR0_SCALE_Pos                 (8U)                                           /**< (PDMIC_DSPR0) Data Scale Position */
#define PDMIC_DSPR0_SCALE_Msk                 (0xFU << PDMIC_DSPR0_SCALE_Pos)                /**< (PDMIC_DSPR0) Data Scale Mask */
#define PDMIC_DSPR0_SCALE(value)              (PDMIC_DSPR0_SCALE_Msk & ((value) << PDMIC_DSPR0_SCALE_Pos))
#define PDMIC_DSPR0_SHIFT_Pos                 (12U)                                          /**< (PDMIC_DSPR0) Data Shift Position */
#define PDMIC_DSPR0_SHIFT_Msk                 (0xFU << PDMIC_DSPR0_SHIFT_Pos)                /**< (PDMIC_DSPR0) Data Shift Mask */
#define PDMIC_DSPR0_SHIFT(value)              (PDMIC_DSPR0_SHIFT_Msk & ((value) << PDMIC_DSPR0_SHIFT_Pos))
#define PDMIC_DSPR0_Msk                       (0x0000FF7EUL)                                 /**< (PDMIC_DSPR0) Register Mask  */

/* -------- PDMIC_DSPR1 : (PDMIC Offset: 0x5C) (R/W 32) DSP Configuration Register 1 -------- */
#define PDMIC_DSPR1_DGAIN_Pos                 (0U)                                           /**< (PDMIC_DSPR1) Gain Correction Position */
#define PDMIC_DSPR1_DGAIN_Msk                 (0x7FFFU << PDMIC_DSPR1_DGAIN_Pos)             /**< (PDMIC_DSPR1) Gain Correction Mask */
#define PDMIC_DSPR1_DGAIN(value)              (PDMIC_DSPR1_DGAIN_Msk & ((value) << PDMIC_DSPR1_DGAIN_Pos))
#define PDMIC_DSPR1_OFST_Pos                  (16U)                                          /**< (PDMIC_DSPR1) Offset Correction Position */
#define PDMIC_DSPR1_OFST_Msk                  (0xFFFFU << PDMIC_DSPR1_OFST_Pos)              /**< (PDMIC_DSPR1) Offset Correction Mask */
#define PDMIC_DSPR1_OFST(value)               (PDMIC_DSPR1_OFST_Msk & ((value) << PDMIC_DSPR1_OFST_Pos))
#define PDMIC_DSPR1_Msk                       (0xFFFF7FFFUL)                                 /**< (PDMIC_DSPR1) Register Mask  */

/* -------- PDMIC_WPMR : (PDMIC Offset: 0xE4) (R/W 32) Write Protection Mode Register -------- */
#define PDMIC_WPMR_WPEN_Pos                   (0U)                                           /**< (PDMIC_WPMR) Write Protection Enable Position */
#define PDMIC_WPMR_WPEN_Msk                   (0x1U << PDMIC_WPMR_WPEN_Pos)                  /**< (PDMIC_WPMR) Write Protection Enable Mask */
#define PDMIC_WPMR_WPEN(value)                (PDMIC_WPMR_WPEN_Msk & ((value) << PDMIC_WPMR_WPEN_Pos))
#define PDMIC_WPMR_WPKEY_Pos                  (8U)                                           /**< (PDMIC_WPMR) Write Protect Key Position */
#define PDMIC_WPMR_WPKEY_Msk                  (0xFFFFFFU << PDMIC_WPMR_WPKEY_Pos)            /**< (PDMIC_WPMR) Write Protect Key Mask */
#define PDMIC_WPMR_WPKEY(value)               (PDMIC_WPMR_WPKEY_Msk & ((value) << PDMIC_WPMR_WPKEY_Pos))
#define   PDMIC_WPMR_WPKEY_PASSWD_Val         (4277315U)                                     /**< (PDMIC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0.  */
#define PDMIC_WPMR_WPKEY_PASSWD               (PDMIC_WPMR_WPKEY_PASSWD_Val << PDMIC_WPMR_WPKEY_Pos) /**< (PDMIC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0. Position  */
#define PDMIC_WPMR_Msk                        (0xFFFFFF01UL)                                 /**< (PDMIC_WPMR) Register Mask  */

/* -------- PDMIC_WPSR : (PDMIC Offset: 0xE8) (R/  32) Write Protection Status Register -------- */
#define PDMIC_WPSR_WPVS_Pos                   (0U)                                           /**< (PDMIC_WPSR) Write Protection Violation Status Position */
#define PDMIC_WPSR_WPVS_Msk                   (0x1U << PDMIC_WPSR_WPVS_Pos)                  /**< (PDMIC_WPSR) Write Protection Violation Status Mask */
#define PDMIC_WPSR_WPVS(value)                (PDMIC_WPSR_WPVS_Msk & ((value) << PDMIC_WPSR_WPVS_Pos))
#define PDMIC_WPSR_WPVSRC_Pos                 (8U)                                           /**< (PDMIC_WPSR) Write Protection Violation Source Position */
#define PDMIC_WPSR_WPVSRC_Msk                 (0xFFFFU << PDMIC_WPSR_WPVSRC_Pos)             /**< (PDMIC_WPSR) Write Protection Violation Source Mask */
#define PDMIC_WPSR_WPVSRC(value)              (PDMIC_WPSR_WPVSRC_Msk & ((value) << PDMIC_WPSR_WPVSRC_Pos))
#define PDMIC_WPSR_Msk                        (0x00FFFF01UL)                                 /**< (PDMIC_WPSR) Register Mask  */

/* -------- PDMIC_RPR : (PDMIC Offset: 0x100) (R/W 32) Receive Pointer Register -------- */
#define PDMIC_RPR_RXPTR_Pos                   (0U)                                           /**< (PDMIC_RPR) Receive Pointer Register Position */
#define PDMIC_RPR_RXPTR_Msk                   (0xFFFFFFFFU << PDMIC_RPR_RXPTR_Pos)           /**< (PDMIC_RPR) Receive Pointer Register Mask */
#define PDMIC_RPR_RXPTR(value)                (PDMIC_RPR_RXPTR_Msk & ((value) << PDMIC_RPR_RXPTR_Pos))
#define PDMIC_RPR_Msk                         (0xFFFFFFFFUL)                                 /**< (PDMIC_RPR) Register Mask  */

/* -------- PDMIC_RCR : (PDMIC Offset: 0x104) (R/W 32) Receive Counter Register -------- */
#define PDMIC_RCR_RXCTR_Pos                   (0U)                                           /**< (PDMIC_RCR) Receive Counter Register Position */
#define PDMIC_RCR_RXCTR_Msk                   (0xFFFFU << PDMIC_RCR_RXCTR_Pos)               /**< (PDMIC_RCR) Receive Counter Register Mask */
#define PDMIC_RCR_RXCTR(value)                (PDMIC_RCR_RXCTR_Msk & ((value) << PDMIC_RCR_RXCTR_Pos))
#define PDMIC_RCR_Msk                         (0x0000FFFFUL)                                 /**< (PDMIC_RCR) Register Mask  */

/* -------- PDMIC_RNPR : (PDMIC Offset: 0x110) (R/W 32) Receive Next Pointer Register -------- */
#define PDMIC_RNPR_RXNPTR_Pos                 (0U)                                           /**< (PDMIC_RNPR) Receive Next Pointer Position */
#define PDMIC_RNPR_RXNPTR_Msk                 (0xFFFFFFFFU << PDMIC_RNPR_RXNPTR_Pos)         /**< (PDMIC_RNPR) Receive Next Pointer Mask */
#define PDMIC_RNPR_RXNPTR(value)              (PDMIC_RNPR_RXNPTR_Msk & ((value) << PDMIC_RNPR_RXNPTR_Pos))
#define PDMIC_RNPR_Msk                        (0xFFFFFFFFUL)                                 /**< (PDMIC_RNPR) Register Mask  */

/* -------- PDMIC_RNCR : (PDMIC Offset: 0x114) (R/W 32) Receive Next Counter Register -------- */
#define PDMIC_RNCR_RXNCTR_Pos                 (0U)                                           /**< (PDMIC_RNCR) Receive Next Counter Position */
#define PDMIC_RNCR_RXNCTR_Msk                 (0xFFFFU << PDMIC_RNCR_RXNCTR_Pos)             /**< (PDMIC_RNCR) Receive Next Counter Mask */
#define PDMIC_RNCR_RXNCTR(value)              (PDMIC_RNCR_RXNCTR_Msk & ((value) << PDMIC_RNCR_RXNCTR_Pos))
#define PDMIC_RNCR_Msk                        (0x0000FFFFUL)                                 /**< (PDMIC_RNCR) Register Mask  */

/* -------- PDMIC_PTCR : (PDMIC Offset: 0x120) ( /W 32) Transfer Control Register -------- */
#define PDMIC_PTCR_RXTEN_Pos                  (0U)                                           /**< (PDMIC_PTCR) Receiver Transfer Enable Position */
#define PDMIC_PTCR_RXTEN_Msk                  (0x1U << PDMIC_PTCR_RXTEN_Pos)                 /**< (PDMIC_PTCR) Receiver Transfer Enable Mask */
#define PDMIC_PTCR_RXTEN(value)               (PDMIC_PTCR_RXTEN_Msk & ((value) << PDMIC_PTCR_RXTEN_Pos))
#define PDMIC_PTCR_RXTDIS_Pos                 (1U)                                           /**< (PDMIC_PTCR) Receiver Transfer Disable Position */
#define PDMIC_PTCR_RXTDIS_Msk                 (0x1U << PDMIC_PTCR_RXTDIS_Pos)                /**< (PDMIC_PTCR) Receiver Transfer Disable Mask */
#define PDMIC_PTCR_RXTDIS(value)              (PDMIC_PTCR_RXTDIS_Msk & ((value) << PDMIC_PTCR_RXTDIS_Pos))
#define PDMIC_PTCR_TXTEN_Pos                  (8U)                                           /**< (PDMIC_PTCR) Transmitter Transfer Enable Position */
#define PDMIC_PTCR_TXTEN_Msk                  (0x1U << PDMIC_PTCR_TXTEN_Pos)                 /**< (PDMIC_PTCR) Transmitter Transfer Enable Mask */
#define PDMIC_PTCR_TXTEN(value)               (PDMIC_PTCR_TXTEN_Msk & ((value) << PDMIC_PTCR_TXTEN_Pos))
#define PDMIC_PTCR_TXTDIS_Pos                 (9U)                                           /**< (PDMIC_PTCR) Transmitter Transfer Disable Position */
#define PDMIC_PTCR_TXTDIS_Msk                 (0x1U << PDMIC_PTCR_TXTDIS_Pos)                /**< (PDMIC_PTCR) Transmitter Transfer Disable Mask */
#define PDMIC_PTCR_TXTDIS(value)              (PDMIC_PTCR_TXTDIS_Msk & ((value) << PDMIC_PTCR_TXTDIS_Pos))
#define PDMIC_PTCR_RXCBEN_Pos                 (16U)                                          /**< (PDMIC_PTCR) Receiver Circular Buffer Enable Position */
#define PDMIC_PTCR_RXCBEN_Msk                 (0x1U << PDMIC_PTCR_RXCBEN_Pos)                /**< (PDMIC_PTCR) Receiver Circular Buffer Enable Mask */
#define PDMIC_PTCR_RXCBEN(value)              (PDMIC_PTCR_RXCBEN_Msk & ((value) << PDMIC_PTCR_RXCBEN_Pos))
#define PDMIC_PTCR_RXCBDIS_Pos                (17U)                                          /**< (PDMIC_PTCR) Receiver Circular Buffer Disable Position */
#define PDMIC_PTCR_RXCBDIS_Msk                (0x1U << PDMIC_PTCR_RXCBDIS_Pos)               /**< (PDMIC_PTCR) Receiver Circular Buffer Disable Mask */
#define PDMIC_PTCR_RXCBDIS(value)             (PDMIC_PTCR_RXCBDIS_Msk & ((value) << PDMIC_PTCR_RXCBDIS_Pos))
#define PDMIC_PTCR_TXCBEN_Pos                 (18U)                                          /**< (PDMIC_PTCR) Transmitter Circular Buffer Enable Position */
#define PDMIC_PTCR_TXCBEN_Msk                 (0x1U << PDMIC_PTCR_TXCBEN_Pos)                /**< (PDMIC_PTCR) Transmitter Circular Buffer Enable Mask */
#define PDMIC_PTCR_TXCBEN(value)              (PDMIC_PTCR_TXCBEN_Msk & ((value) << PDMIC_PTCR_TXCBEN_Pos))
#define PDMIC_PTCR_TXCBDIS_Pos                (19U)                                          /**< (PDMIC_PTCR) Transmitter Circular Buffer Disable Position */
#define PDMIC_PTCR_TXCBDIS_Msk                (0x1U << PDMIC_PTCR_TXCBDIS_Pos)               /**< (PDMIC_PTCR) Transmitter Circular Buffer Disable Mask */
#define PDMIC_PTCR_TXCBDIS(value)             (PDMIC_PTCR_TXCBDIS_Msk & ((value) << PDMIC_PTCR_TXCBDIS_Pos))
#define PDMIC_PTCR_ERRCLR_Pos                 (24U)                                          /**< (PDMIC_PTCR) Transfer Bus Error Clear Position */
#define PDMIC_PTCR_ERRCLR_Msk                 (0x1U << PDMIC_PTCR_ERRCLR_Pos)                /**< (PDMIC_PTCR) Transfer Bus Error Clear Mask */
#define PDMIC_PTCR_ERRCLR(value)              (PDMIC_PTCR_ERRCLR_Msk & ((value) << PDMIC_PTCR_ERRCLR_Pos))
#define PDMIC_PTCR_Msk                        (0x010F0303UL)                                 /**< (PDMIC_PTCR) Register Mask  */

/* -------- PDMIC_PTSR : (PDMIC Offset: 0x124) (R/  32) Transfer Status Register -------- */
#define PDMIC_PTSR_RXTEN_Pos                  (0U)                                           /**< (PDMIC_PTSR) Receiver Transfer Enable Position */
#define PDMIC_PTSR_RXTEN_Msk                  (0x1U << PDMIC_PTSR_RXTEN_Pos)                 /**< (PDMIC_PTSR) Receiver Transfer Enable Mask */
#define PDMIC_PTSR_RXTEN(value)               (PDMIC_PTSR_RXTEN_Msk & ((value) << PDMIC_PTSR_RXTEN_Pos))
#define PDMIC_PTSR_TXTEN_Pos                  (8U)                                           /**< (PDMIC_PTSR) Transmitter Transfer Enable Position */
#define PDMIC_PTSR_TXTEN_Msk                  (0x1U << PDMIC_PTSR_TXTEN_Pos)                 /**< (PDMIC_PTSR) Transmitter Transfer Enable Mask */
#define PDMIC_PTSR_TXTEN(value)               (PDMIC_PTSR_TXTEN_Msk & ((value) << PDMIC_PTSR_TXTEN_Pos))
#define PDMIC_PTSR_RXCBEN_Pos                 (16U)                                          /**< (PDMIC_PTSR) Receiver Circular Buffer Enable Position */
#define PDMIC_PTSR_RXCBEN_Msk                 (0x1U << PDMIC_PTSR_RXCBEN_Pos)                /**< (PDMIC_PTSR) Receiver Circular Buffer Enable Mask */
#define PDMIC_PTSR_RXCBEN(value)              (PDMIC_PTSR_RXCBEN_Msk & ((value) << PDMIC_PTSR_RXCBEN_Pos))
#define PDMIC_PTSR_TXCBEN_Pos                 (18U)                                          /**< (PDMIC_PTSR) Transmitter Circular Buffer Enable Position */
#define PDMIC_PTSR_TXCBEN_Msk                 (0x1U << PDMIC_PTSR_TXCBEN_Pos)                /**< (PDMIC_PTSR) Transmitter Circular Buffer Enable Mask */
#define PDMIC_PTSR_TXCBEN(value)              (PDMIC_PTSR_TXCBEN_Msk & ((value) << PDMIC_PTSR_TXCBEN_Pos))
#define PDMIC_PTSR_ERR_Pos                    (24U)                                          /**< (PDMIC_PTSR) Transfer Bus Error Position */
#define PDMIC_PTSR_ERR_Msk                    (0x1U << PDMIC_PTSR_ERR_Pos)                   /**< (PDMIC_PTSR) Transfer Bus Error Mask */
#define PDMIC_PTSR_ERR(value)                 (PDMIC_PTSR_ERR_Msk & ((value) << PDMIC_PTSR_ERR_Pos))
#define PDMIC_PTSR_Msk                        (0x01050101UL)                                 /**< (PDMIC_PTSR) Register Mask  */

/** \brief PDMIC register offsets definitions */
#define PDMIC_CR_OFFSET                (0x00)         /**< (PDMIC_CR) Control Register Offset */
#define PDMIC_MR_OFFSET                (0x04)         /**< (PDMIC_MR) Mode Register Offset */
#define PDMIC_CDR_OFFSET               (0x14)         /**< (PDMIC_CDR) Converted Data Register Offset */
#define PDMIC_IER_OFFSET               (0x18)         /**< (PDMIC_IER) Interrupt Enable Register Offset */
#define PDMIC_IDR_OFFSET               (0x1C)         /**< (PDMIC_IDR) Interrupt Disable Register Offset */
#define PDMIC_IMR_OFFSET               (0x20)         /**< (PDMIC_IMR) Interrupt Mask Register Offset */
#define PDMIC_ISR_OFFSET               (0x24)         /**< (PDMIC_ISR) Interrupt Status Register Offset */
#define PDMIC_DSPR0_OFFSET             (0x58)         /**< (PDMIC_DSPR0) DSP Configuration Register 0 Offset */
#define PDMIC_DSPR1_OFFSET             (0x5C)         /**< (PDMIC_DSPR1) DSP Configuration Register 1 Offset */
#define PDMIC_WPMR_OFFSET              (0xE4)         /**< (PDMIC_WPMR) Write Protection Mode Register Offset */
#define PDMIC_WPSR_OFFSET              (0xE8)         /**< (PDMIC_WPSR) Write Protection Status Register Offset */
#define PDMIC_RPR_OFFSET               (0x100)        /**< (PDMIC_RPR) Receive Pointer Register Offset */
#define PDMIC_RCR_OFFSET               (0x104)        /**< (PDMIC_RCR) Receive Counter Register Offset */
#define PDMIC_RNPR_OFFSET              (0x110)        /**< (PDMIC_RNPR) Receive Next Pointer Register Offset */
#define PDMIC_RNCR_OFFSET              (0x114)        /**< (PDMIC_RNCR) Receive Next Counter Register Offset */
#define PDMIC_PTCR_OFFSET              (0x120)        /**< (PDMIC_PTCR) Transfer Control Register Offset */
#define PDMIC_PTSR_OFFSET              (0x124)        /**< (PDMIC_PTSR) Transfer Status Register Offset */

/** \brief PDMIC register API structure */
typedef struct
{
  __IO  uint32_t                       PDMIC_CR;        /**< Offset: 0x00 (R/W  32) Control Register */
  __IO  uint32_t                       PDMIC_MR;        /**< Offset: 0x04 (R/W  32) Mode Register */
  __I   uint8_t                        Reserved1[0x0C];
  __I   uint32_t                       PDMIC_CDR;       /**< Offset: 0x14 (R/   32) Converted Data Register */
  __O   uint32_t                       PDMIC_IER;       /**< Offset: 0x18 ( /W  32) Interrupt Enable Register */
  __O   uint32_t                       PDMIC_IDR;       /**< Offset: 0x1c ( /W  32) Interrupt Disable Register */
  __I   uint32_t                       PDMIC_IMR;       /**< Offset: 0x20 (R/   32) Interrupt Mask Register */
  __I   uint32_t                       PDMIC_ISR;       /**< Offset: 0x24 (R/   32) Interrupt Status Register */
  __I   uint8_t                        Reserved2[0x30];
  __IO  uint32_t                       PDMIC_DSPR0;     /**< Offset: 0x58 (R/W  32) DSP Configuration Register 0 */
  __IO  uint32_t                       PDMIC_DSPR1;     /**< Offset: 0x5c (R/W  32) DSP Configuration Register 1 */
  __I   uint8_t                        Reserved3[0x84];
  __IO  uint32_t                       PDMIC_WPMR;      /**< Offset: 0xe4 (R/W  32) Write Protection Mode Register */
  __I   uint32_t                       PDMIC_WPSR;      /**< Offset: 0xe8 (R/   32) Write Protection Status Register */
  __I   uint8_t                        Reserved4[0x14];
  __IO  uint32_t                       PDMIC_RPR;       /**< Offset: 0x100 (R/W  32) Receive Pointer Register */
  __IO  uint32_t                       PDMIC_RCR;       /**< Offset: 0x104 (R/W  32) Receive Counter Register */
  __I   uint8_t                        Reserved5[0x08];
  __IO  uint32_t                       PDMIC_RNPR;      /**< Offset: 0x110 (R/W  32) Receive Next Pointer Register */
  __IO  uint32_t                       PDMIC_RNCR;      /**< Offset: 0x114 (R/W  32) Receive Next Counter Register */
  __I   uint8_t                        Reserved6[0x08];
  __O   uint32_t                       PDMIC_PTCR;      /**< Offset: 0x120 ( /W  32) Transfer Control Register */
  __I   uint32_t                       PDMIC_PTSR;      /**< Offset: 0x124 (R/   32) Transfer Status Register */
} pdmic_registers_t;
/** @}  end of Pulse Density Modulation Interface Controller */

#endif /* SAMG_SAMG55_PDMIC_MODULE_H */

