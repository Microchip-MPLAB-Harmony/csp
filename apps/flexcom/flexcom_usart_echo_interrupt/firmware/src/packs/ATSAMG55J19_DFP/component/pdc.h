/**
 * \brief Header file for SAMG/SAMG55 PDC
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
#ifndef SAMG_SAMG55_PDC_MODULE_H
#define SAMG_SAMG55_PDC_MODULE_H

/** \addtogroup SAMG_SAMG55 Peripheral DMA Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_PDC                                   */
/* ========================================================================== */

/* -------- PERIPH_RPR : (PDC Offset: 0x00) (R/W 32) Receive Pointer Register -------- */
#define PERIPH_RPR_RXPTR_Pos                  (0U)                                           /**< (PERIPH_RPR) Receive Pointer Register Position */
#define PERIPH_RPR_RXPTR_Msk                  (0xFFFFFFFFU << PERIPH_RPR_RXPTR_Pos)          /**< (PERIPH_RPR) Receive Pointer Register Mask */
#define PERIPH_RPR_RXPTR(value)               (PERIPH_RPR_RXPTR_Msk & ((value) << PERIPH_RPR_RXPTR_Pos))
#define PERIPH_RPR_Msk                        (0xFFFFFFFFUL)                                 /**< (PERIPH_RPR) Register Mask  */

/* -------- PERIPH_RCR : (PDC Offset: 0x04) (R/W 32) Receive Counter Register -------- */
#define PERIPH_RCR_RXCTR_Pos                  (0U)                                           /**< (PERIPH_RCR) Receive Counter Register Position */
#define PERIPH_RCR_RXCTR_Msk                  (0xFFFFU << PERIPH_RCR_RXCTR_Pos)              /**< (PERIPH_RCR) Receive Counter Register Mask */
#define PERIPH_RCR_RXCTR(value)               (PERIPH_RCR_RXCTR_Msk & ((value) << PERIPH_RCR_RXCTR_Pos))
#define PERIPH_RCR_Msk                        (0x0000FFFFUL)                                 /**< (PERIPH_RCR) Register Mask  */

/* -------- PERIPH_TPR : (PDC Offset: 0x08) (R/W 32) Transmit Pointer Register -------- */
#define PERIPH_TPR_TXPTR_Pos                  (0U)                                           /**< (PERIPH_TPR) Transmit Counter Register Position */
#define PERIPH_TPR_TXPTR_Msk                  (0xFFFFFFFFU << PERIPH_TPR_TXPTR_Pos)          /**< (PERIPH_TPR) Transmit Counter Register Mask */
#define PERIPH_TPR_TXPTR(value)               (PERIPH_TPR_TXPTR_Msk & ((value) << PERIPH_TPR_TXPTR_Pos))
#define PERIPH_TPR_Msk                        (0xFFFFFFFFUL)                                 /**< (PERIPH_TPR) Register Mask  */

/* -------- PERIPH_TCR : (PDC Offset: 0x0C) (R/W 32) Transmit Counter Register -------- */
#define PERIPH_TCR_TXCTR_Pos                  (0U)                                           /**< (PERIPH_TCR) Transmit Counter Register Position */
#define PERIPH_TCR_TXCTR_Msk                  (0xFFFFU << PERIPH_TCR_TXCTR_Pos)              /**< (PERIPH_TCR) Transmit Counter Register Mask */
#define PERIPH_TCR_TXCTR(value)               (PERIPH_TCR_TXCTR_Msk & ((value) << PERIPH_TCR_TXCTR_Pos))
#define PERIPH_TCR_Msk                        (0x0000FFFFUL)                                 /**< (PERIPH_TCR) Register Mask  */

/* -------- PERIPH_RNPR : (PDC Offset: 0x10) (R/W 32) Receive Next Pointer Register -------- */
#define PERIPH_RNPR_RXNPTR_Pos                (0U)                                           /**< (PERIPH_RNPR) Receive Next Pointer Position */
#define PERIPH_RNPR_RXNPTR_Msk                (0xFFFFFFFFU << PERIPH_RNPR_RXNPTR_Pos)        /**< (PERIPH_RNPR) Receive Next Pointer Mask */
#define PERIPH_RNPR_RXNPTR(value)             (PERIPH_RNPR_RXNPTR_Msk & ((value) << PERIPH_RNPR_RXNPTR_Pos))
#define PERIPH_RNPR_Msk                       (0xFFFFFFFFUL)                                 /**< (PERIPH_RNPR) Register Mask  */

/* -------- PERIPH_RNCR : (PDC Offset: 0x14) (R/W 32) Receive Next Counter Register -------- */
#define PERIPH_RNCR_RXNCTR_Pos                (0U)                                           /**< (PERIPH_RNCR) Receive Next Counter Position */
#define PERIPH_RNCR_RXNCTR_Msk                (0xFFFFU << PERIPH_RNCR_RXNCTR_Pos)            /**< (PERIPH_RNCR) Receive Next Counter Mask */
#define PERIPH_RNCR_RXNCTR(value)             (PERIPH_RNCR_RXNCTR_Msk & ((value) << PERIPH_RNCR_RXNCTR_Pos))
#define PERIPH_RNCR_Msk                       (0x0000FFFFUL)                                 /**< (PERIPH_RNCR) Register Mask  */

/* -------- PERIPH_TNPR : (PDC Offset: 0x18) (R/W 32) Transmit Next Pointer Register -------- */
#define PERIPH_TNPR_TXNPTR_Pos                (0U)                                           /**< (PERIPH_TNPR) Transmit Next Pointer Position */
#define PERIPH_TNPR_TXNPTR_Msk                (0xFFFFFFFFU << PERIPH_TNPR_TXNPTR_Pos)        /**< (PERIPH_TNPR) Transmit Next Pointer Mask */
#define PERIPH_TNPR_TXNPTR(value)             (PERIPH_TNPR_TXNPTR_Msk & ((value) << PERIPH_TNPR_TXNPTR_Pos))
#define PERIPH_TNPR_Msk                       (0xFFFFFFFFUL)                                 /**< (PERIPH_TNPR) Register Mask  */

/* -------- PERIPH_TNCR : (PDC Offset: 0x1C) (R/W 32) Transmit Next Counter Register -------- */
#define PERIPH_TNCR_TXNCTR_Pos                (0U)                                           /**< (PERIPH_TNCR) Transmit Counter Next Position */
#define PERIPH_TNCR_TXNCTR_Msk                (0xFFFFU << PERIPH_TNCR_TXNCTR_Pos)            /**< (PERIPH_TNCR) Transmit Counter Next Mask */
#define PERIPH_TNCR_TXNCTR(value)             (PERIPH_TNCR_TXNCTR_Msk & ((value) << PERIPH_TNCR_TXNCTR_Pos))
#define PERIPH_TNCR_Msk                       (0x0000FFFFUL)                                 /**< (PERIPH_TNCR) Register Mask  */

/* -------- PERIPH_PTCR : (PDC Offset: 0x20) ( /W 32) Transfer Control Register -------- */
#define PERIPH_PTCR_RXTEN_Pos                 (0U)                                           /**< (PERIPH_PTCR) Receiver Transfer Enable Position */
#define PERIPH_PTCR_RXTEN_Msk                 (0x1U << PERIPH_PTCR_RXTEN_Pos)                /**< (PERIPH_PTCR) Receiver Transfer Enable Mask */
#define PERIPH_PTCR_RXTEN(value)              (PERIPH_PTCR_RXTEN_Msk & ((value) << PERIPH_PTCR_RXTEN_Pos))
#define PERIPH_PTCR_RXTDIS_Pos                (1U)                                           /**< (PERIPH_PTCR) Receiver Transfer Disable Position */
#define PERIPH_PTCR_RXTDIS_Msk                (0x1U << PERIPH_PTCR_RXTDIS_Pos)               /**< (PERIPH_PTCR) Receiver Transfer Disable Mask */
#define PERIPH_PTCR_RXTDIS(value)             (PERIPH_PTCR_RXTDIS_Msk & ((value) << PERIPH_PTCR_RXTDIS_Pos))
#define PERIPH_PTCR_TXTEN_Pos                 (8U)                                           /**< (PERIPH_PTCR) Transmitter Transfer Enable Position */
#define PERIPH_PTCR_TXTEN_Msk                 (0x1U << PERIPH_PTCR_TXTEN_Pos)                /**< (PERIPH_PTCR) Transmitter Transfer Enable Mask */
#define PERIPH_PTCR_TXTEN(value)              (PERIPH_PTCR_TXTEN_Msk & ((value) << PERIPH_PTCR_TXTEN_Pos))
#define PERIPH_PTCR_TXTDIS_Pos                (9U)                                           /**< (PERIPH_PTCR) Transmitter Transfer Disable Position */
#define PERIPH_PTCR_TXTDIS_Msk                (0x1U << PERIPH_PTCR_TXTDIS_Pos)               /**< (PERIPH_PTCR) Transmitter Transfer Disable Mask */
#define PERIPH_PTCR_TXTDIS(value)             (PERIPH_PTCR_TXTDIS_Msk & ((value) << PERIPH_PTCR_TXTDIS_Pos))
#define PERIPH_PTCR_RXCBEN_Pos                (16U)                                          /**< (PERIPH_PTCR) Receiver Circular Buffer Enable Position */
#define PERIPH_PTCR_RXCBEN_Msk                (0x1U << PERIPH_PTCR_RXCBEN_Pos)               /**< (PERIPH_PTCR) Receiver Circular Buffer Enable Mask */
#define PERIPH_PTCR_RXCBEN(value)             (PERIPH_PTCR_RXCBEN_Msk & ((value) << PERIPH_PTCR_RXCBEN_Pos))
#define PERIPH_PTCR_RXCBDIS_Pos               (17U)                                          /**< (PERIPH_PTCR) Receiver Circular Buffer Disable Position */
#define PERIPH_PTCR_RXCBDIS_Msk               (0x1U << PERIPH_PTCR_RXCBDIS_Pos)              /**< (PERIPH_PTCR) Receiver Circular Buffer Disable Mask */
#define PERIPH_PTCR_RXCBDIS(value)            (PERIPH_PTCR_RXCBDIS_Msk & ((value) << PERIPH_PTCR_RXCBDIS_Pos))
#define PERIPH_PTCR_TXCBEN_Pos                (18U)                                          /**< (PERIPH_PTCR) Transmitter Circular Buffer Enable Position */
#define PERIPH_PTCR_TXCBEN_Msk                (0x1U << PERIPH_PTCR_TXCBEN_Pos)               /**< (PERIPH_PTCR) Transmitter Circular Buffer Enable Mask */
#define PERIPH_PTCR_TXCBEN(value)             (PERIPH_PTCR_TXCBEN_Msk & ((value) << PERIPH_PTCR_TXCBEN_Pos))
#define PERIPH_PTCR_TXCBDIS_Pos               (19U)                                          /**< (PERIPH_PTCR) Transmitter Circular Buffer Disable Position */
#define PERIPH_PTCR_TXCBDIS_Msk               (0x1U << PERIPH_PTCR_TXCBDIS_Pos)              /**< (PERIPH_PTCR) Transmitter Circular Buffer Disable Mask */
#define PERIPH_PTCR_TXCBDIS(value)            (PERIPH_PTCR_TXCBDIS_Msk & ((value) << PERIPH_PTCR_TXCBDIS_Pos))
#define PERIPH_PTCR_ERRCLR_Pos                (24U)                                          /**< (PERIPH_PTCR) Transfer Bus Error Clear Position */
#define PERIPH_PTCR_ERRCLR_Msk                (0x1U << PERIPH_PTCR_ERRCLR_Pos)               /**< (PERIPH_PTCR) Transfer Bus Error Clear Mask */
#define PERIPH_PTCR_ERRCLR(value)             (PERIPH_PTCR_ERRCLR_Msk & ((value) << PERIPH_PTCR_ERRCLR_Pos))
#define PERIPH_PTCR_Msk                       (0x010F0303UL)                                 /**< (PERIPH_PTCR) Register Mask  */

/* -------- PERIPH_PTSR : (PDC Offset: 0x24) (R/  32) Transfer Status Register -------- */
#define PERIPH_PTSR_RXTEN_Pos                 (0U)                                           /**< (PERIPH_PTSR) Receiver Transfer Enable Position */
#define PERIPH_PTSR_RXTEN_Msk                 (0x1U << PERIPH_PTSR_RXTEN_Pos)                /**< (PERIPH_PTSR) Receiver Transfer Enable Mask */
#define PERIPH_PTSR_RXTEN(value)              (PERIPH_PTSR_RXTEN_Msk & ((value) << PERIPH_PTSR_RXTEN_Pos))
#define PERIPH_PTSR_TXTEN_Pos                 (8U)                                           /**< (PERIPH_PTSR) Transmitter Transfer Enable Position */
#define PERIPH_PTSR_TXTEN_Msk                 (0x1U << PERIPH_PTSR_TXTEN_Pos)                /**< (PERIPH_PTSR) Transmitter Transfer Enable Mask */
#define PERIPH_PTSR_TXTEN(value)              (PERIPH_PTSR_TXTEN_Msk & ((value) << PERIPH_PTSR_TXTEN_Pos))
#define PERIPH_PTSR_RXCBEN_Pos                (16U)                                          /**< (PERIPH_PTSR) Receiver Circular Buffer Enable Position */
#define PERIPH_PTSR_RXCBEN_Msk                (0x1U << PERIPH_PTSR_RXCBEN_Pos)               /**< (PERIPH_PTSR) Receiver Circular Buffer Enable Mask */
#define PERIPH_PTSR_RXCBEN(value)             (PERIPH_PTSR_RXCBEN_Msk & ((value) << PERIPH_PTSR_RXCBEN_Pos))
#define PERIPH_PTSR_TXCBEN_Pos                (18U)                                          /**< (PERIPH_PTSR) Transmitter Circular Buffer Enable Position */
#define PERIPH_PTSR_TXCBEN_Msk                (0x1U << PERIPH_PTSR_TXCBEN_Pos)               /**< (PERIPH_PTSR) Transmitter Circular Buffer Enable Mask */
#define PERIPH_PTSR_TXCBEN(value)             (PERIPH_PTSR_TXCBEN_Msk & ((value) << PERIPH_PTSR_TXCBEN_Pos))
#define PERIPH_PTSR_ERR_Pos                   (24U)                                          /**< (PERIPH_PTSR) Transfer Bus Error Position */
#define PERIPH_PTSR_ERR_Msk                   (0x1U << PERIPH_PTSR_ERR_Pos)                  /**< (PERIPH_PTSR) Transfer Bus Error Mask */
#define PERIPH_PTSR_ERR(value)                (PERIPH_PTSR_ERR_Msk & ((value) << PERIPH_PTSR_ERR_Pos))
#define PERIPH_PTSR_Msk                       (0x01050101UL)                                 /**< (PERIPH_PTSR) Register Mask  */

/** \brief PDC register offsets definitions */
#define PERIPH_RPR_OFFSET              (0x00)         /**< (PERIPH_RPR) Receive Pointer Register Offset */
#define PERIPH_RCR_OFFSET              (0x04)         /**< (PERIPH_RCR) Receive Counter Register Offset */
#define PERIPH_TPR_OFFSET              (0x08)         /**< (PERIPH_TPR) Transmit Pointer Register Offset */
#define PERIPH_TCR_OFFSET              (0x0C)         /**< (PERIPH_TCR) Transmit Counter Register Offset */
#define PERIPH_RNPR_OFFSET             (0x10)         /**< (PERIPH_RNPR) Receive Next Pointer Register Offset */
#define PERIPH_RNCR_OFFSET             (0x14)         /**< (PERIPH_RNCR) Receive Next Counter Register Offset */
#define PERIPH_TNPR_OFFSET             (0x18)         /**< (PERIPH_TNPR) Transmit Next Pointer Register Offset */
#define PERIPH_TNCR_OFFSET             (0x1C)         /**< (PERIPH_TNCR) Transmit Next Counter Register Offset */
#define PERIPH_PTCR_OFFSET             (0x20)         /**< (PERIPH_PTCR) Transfer Control Register Offset */
#define PERIPH_PTSR_OFFSET             (0x24)         /**< (PERIPH_PTSR) Transfer Status Register Offset */

/** \brief PDC register API structure */
typedef struct
{
  __IO  uint32_t                       PERIPH_RPR;      /**< Offset: 0x00 (R/W  32) Receive Pointer Register */
  __IO  uint32_t                       PERIPH_RCR;      /**< Offset: 0x04 (R/W  32) Receive Counter Register */
  __IO  uint32_t                       PERIPH_TPR;      /**< Offset: 0x08 (R/W  32) Transmit Pointer Register */
  __IO  uint32_t                       PERIPH_TCR;      /**< Offset: 0x0c (R/W  32) Transmit Counter Register */
  __IO  uint32_t                       PERIPH_RNPR;     /**< Offset: 0x10 (R/W  32) Receive Next Pointer Register */
  __IO  uint32_t                       PERIPH_RNCR;     /**< Offset: 0x14 (R/W  32) Receive Next Counter Register */
  __IO  uint32_t                       PERIPH_TNPR;     /**< Offset: 0x18 (R/W  32) Transmit Next Pointer Register */
  __IO  uint32_t                       PERIPH_TNCR;     /**< Offset: 0x1c (R/W  32) Transmit Next Counter Register */
  __O   uint32_t                       PERIPH_PTCR;     /**< Offset: 0x20 ( /W  32) Transfer Control Register */
  __I   uint32_t                       PERIPH_PTSR;     /**< Offset: 0x24 (R/   32) Transfer Status Register */
} pdc_registers_t;
/** @}  end of Peripheral DMA Controller */

#endif /* SAMG_SAMG55_PDC_MODULE_H */

