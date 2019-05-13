/**
 * \brief Header file for SAMG/SAMG55 MEM2MEM
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
#ifndef SAMG_SAMG55_MEM2MEM_MODULE_H
#define SAMG_SAMG55_MEM2MEM_MODULE_H

/** \addtogroup SAMG_SAMG55 Memory to Memory
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_MEM2MEM                               */
/* ========================================================================== */

/* -------- MEM2MEM_THR : (MEM2MEM Offset: 0x00) (R/W 32) Memory to Memory Transfer Holding Register -------- */
#define MEM2MEM_THR_THDATA_Pos                (0U)                                           /**< (MEM2MEM_THR) Transfer Holding Data Position */
#define MEM2MEM_THR_THDATA_Msk                (0xFFFFFFFFU << MEM2MEM_THR_THDATA_Pos)        /**< (MEM2MEM_THR) Transfer Holding Data Mask */
#define MEM2MEM_THR_THDATA(value)             (MEM2MEM_THR_THDATA_Msk & ((value) << MEM2MEM_THR_THDATA_Pos))
#define MEM2MEM_THR_Msk                       (0xFFFFFFFFUL)                                 /**< (MEM2MEM_THR) Register Mask  */

/* -------- MEM2MEM_MR : (MEM2MEM Offset: 0x04) (R/W 32) Memory to Memory Mode Register -------- */
#define MEM2MEM_MR_TSIZE_Pos                  (0U)                                           /**< (MEM2MEM_MR) Transfer Size Position */
#define MEM2MEM_MR_TSIZE_Msk                  (0x3U << MEM2MEM_MR_TSIZE_Pos)                 /**< (MEM2MEM_MR) Transfer Size Mask */
#define MEM2MEM_MR_TSIZE(value)               (MEM2MEM_MR_TSIZE_Msk & ((value) << MEM2MEM_MR_TSIZE_Pos))
#define   MEM2MEM_MR_TSIZE_T_8BIT_Val         (0U)                                           /**< (MEM2MEM_MR) The buffer size is defined in byte.  */
#define   MEM2MEM_MR_TSIZE_T_16BIT_Val        (1U)                                           /**< (MEM2MEM_MR) The buffer size is defined in half-word (16-bit).  */
#define   MEM2MEM_MR_TSIZE_T_32BIT_Val        (2U)                                           /**< (MEM2MEM_MR) The buffer size is defined in word (32-bit). Default value.  */
#define MEM2MEM_MR_TSIZE_T_8BIT               (MEM2MEM_MR_TSIZE_T_8BIT_Val << MEM2MEM_MR_TSIZE_Pos) /**< (MEM2MEM_MR) The buffer size is defined in byte. Position  */
#define MEM2MEM_MR_TSIZE_T_16BIT              (MEM2MEM_MR_TSIZE_T_16BIT_Val << MEM2MEM_MR_TSIZE_Pos) /**< (MEM2MEM_MR) The buffer size is defined in half-word (16-bit). Position  */
#define MEM2MEM_MR_TSIZE_T_32BIT              (MEM2MEM_MR_TSIZE_T_32BIT_Val << MEM2MEM_MR_TSIZE_Pos) /**< (MEM2MEM_MR) The buffer size is defined in word (32-bit). Default value. Position  */
#define MEM2MEM_MR_Msk                        (0x00000003UL)                                 /**< (MEM2MEM_MR) Register Mask  */

/* -------- MEM2MEM_IER : (MEM2MEM Offset: 0x08) ( /W 32) Memory to Memory Interrupt Enable Register -------- */
#define MEM2MEM_IER_RXEND_Pos                 (0U)                                           /**< (MEM2MEM_IER) End of Transfer Interrupt Enable Position */
#define MEM2MEM_IER_RXEND_Msk                 (0x1U << MEM2MEM_IER_RXEND_Pos)                /**< (MEM2MEM_IER) End of Transfer Interrupt Enable Mask */
#define MEM2MEM_IER_RXEND(value)              (MEM2MEM_IER_RXEND_Msk & ((value) << MEM2MEM_IER_RXEND_Pos))
#define MEM2MEM_IER_RXBUFF_Pos                (1U)                                           /**< (MEM2MEM_IER) Buffer Full Interrupt Enable Position */
#define MEM2MEM_IER_RXBUFF_Msk                (0x1U << MEM2MEM_IER_RXBUFF_Pos)               /**< (MEM2MEM_IER) Buffer Full Interrupt Enable Mask */
#define MEM2MEM_IER_RXBUFF(value)             (MEM2MEM_IER_RXBUFF_Msk & ((value) << MEM2MEM_IER_RXBUFF_Pos))
#define MEM2MEM_IER_Msk                       (0x00000003UL)                                 /**< (MEM2MEM_IER) Register Mask  */

/* -------- MEM2MEM_IDR : (MEM2MEM Offset: 0x0C) ( /W 32) Memory to Memory Interrupt Disable Register -------- */
#define MEM2MEM_IDR_RXEND_Pos                 (0U)                                           /**< (MEM2MEM_IDR) End of Transfer Interrupt Disable Position */
#define MEM2MEM_IDR_RXEND_Msk                 (0x1U << MEM2MEM_IDR_RXEND_Pos)                /**< (MEM2MEM_IDR) End of Transfer Interrupt Disable Mask */
#define MEM2MEM_IDR_RXEND(value)              (MEM2MEM_IDR_RXEND_Msk & ((value) << MEM2MEM_IDR_RXEND_Pos))
#define MEM2MEM_IDR_RXBUFF_Pos                (1U)                                           /**< (MEM2MEM_IDR) Buffer Full Interrupt Disable Position */
#define MEM2MEM_IDR_RXBUFF_Msk                (0x1U << MEM2MEM_IDR_RXBUFF_Pos)               /**< (MEM2MEM_IDR) Buffer Full Interrupt Disable Mask */
#define MEM2MEM_IDR_RXBUFF(value)             (MEM2MEM_IDR_RXBUFF_Msk & ((value) << MEM2MEM_IDR_RXBUFF_Pos))
#define MEM2MEM_IDR_Msk                       (0x00000003UL)                                 /**< (MEM2MEM_IDR) Register Mask  */

/* -------- MEM2MEM_IMR : (MEM2MEM Offset: 0x10) (R/  32) Memory to Memory Interrupt Mask Register -------- */
#define MEM2MEM_IMR_RXEND_Pos                 (0U)                                           /**< (MEM2MEM_IMR) End of Transfer Interrupt Mask Position */
#define MEM2MEM_IMR_RXEND_Msk                 (0x1U << MEM2MEM_IMR_RXEND_Pos)                /**< (MEM2MEM_IMR) End of Transfer Interrupt Mask Mask */
#define MEM2MEM_IMR_RXEND(value)              (MEM2MEM_IMR_RXEND_Msk & ((value) << MEM2MEM_IMR_RXEND_Pos))
#define MEM2MEM_IMR_RXBUFF_Pos                (1U)                                           /**< (MEM2MEM_IMR) Buffer Full Interrupt Mask Position */
#define MEM2MEM_IMR_RXBUFF_Msk                (0x1U << MEM2MEM_IMR_RXBUFF_Pos)               /**< (MEM2MEM_IMR) Buffer Full Interrupt Mask Mask */
#define MEM2MEM_IMR_RXBUFF(value)             (MEM2MEM_IMR_RXBUFF_Msk & ((value) << MEM2MEM_IMR_RXBUFF_Pos))
#define MEM2MEM_IMR_Msk                       (0x00000003UL)                                 /**< (MEM2MEM_IMR) Register Mask  */

/* -------- MEM2MEM_ISR : (MEM2MEM Offset: 0x14) (R/  32) Memory to Memory Interrupt Status Register -------- */
#define MEM2MEM_ISR_RXEND_Pos                 (0U)                                           /**< (MEM2MEM_ISR) End of Transfer Position */
#define MEM2MEM_ISR_RXEND_Msk                 (0x1U << MEM2MEM_ISR_RXEND_Pos)                /**< (MEM2MEM_ISR) End of Transfer Mask */
#define MEM2MEM_ISR_RXEND(value)              (MEM2MEM_ISR_RXEND_Msk & ((value) << MEM2MEM_ISR_RXEND_Pos))
#define MEM2MEM_ISR_RXBUFF_Pos                (1U)                                           /**< (MEM2MEM_ISR) Buffer Full Position */
#define MEM2MEM_ISR_RXBUFF_Msk                (0x1U << MEM2MEM_ISR_RXBUFF_Pos)               /**< (MEM2MEM_ISR) Buffer Full Mask */
#define MEM2MEM_ISR_RXBUFF(value)             (MEM2MEM_ISR_RXBUFF_Msk & ((value) << MEM2MEM_ISR_RXBUFF_Pos))
#define MEM2MEM_ISR_Msk                       (0x00000003UL)                                 /**< (MEM2MEM_ISR) Register Mask  */

/* -------- MEM2MEM_RPR : (MEM2MEM Offset: 0x100) (R/W 32) Receive Pointer Register -------- */
#define MEM2MEM_RPR_RXPTR_Pos                 (0U)                                           /**< (MEM2MEM_RPR) Receive Pointer Register Position */
#define MEM2MEM_RPR_RXPTR_Msk                 (0xFFFFFFFFU << MEM2MEM_RPR_RXPTR_Pos)         /**< (MEM2MEM_RPR) Receive Pointer Register Mask */
#define MEM2MEM_RPR_RXPTR(value)              (MEM2MEM_RPR_RXPTR_Msk & ((value) << MEM2MEM_RPR_RXPTR_Pos))
#define MEM2MEM_RPR_Msk                       (0xFFFFFFFFUL)                                 /**< (MEM2MEM_RPR) Register Mask  */

/* -------- MEM2MEM_RCR : (MEM2MEM Offset: 0x104) (R/W 32) Receive Counter Register -------- */
#define MEM2MEM_RCR_RXCTR_Pos                 (0U)                                           /**< (MEM2MEM_RCR) Receive Counter Register Position */
#define MEM2MEM_RCR_RXCTR_Msk                 (0xFFFFU << MEM2MEM_RCR_RXCTR_Pos)             /**< (MEM2MEM_RCR) Receive Counter Register Mask */
#define MEM2MEM_RCR_RXCTR(value)              (MEM2MEM_RCR_RXCTR_Msk & ((value) << MEM2MEM_RCR_RXCTR_Pos))
#define MEM2MEM_RCR_Msk                       (0x0000FFFFUL)                                 /**< (MEM2MEM_RCR) Register Mask  */

/* -------- MEM2MEM_TPR : (MEM2MEM Offset: 0x108) (R/W 32) Transmit Pointer Register -------- */
#define MEM2MEM_TPR_TXPTR_Pos                 (0U)                                           /**< (MEM2MEM_TPR) Transmit Counter Register Position */
#define MEM2MEM_TPR_TXPTR_Msk                 (0xFFFFFFFFU << MEM2MEM_TPR_TXPTR_Pos)         /**< (MEM2MEM_TPR) Transmit Counter Register Mask */
#define MEM2MEM_TPR_TXPTR(value)              (MEM2MEM_TPR_TXPTR_Msk & ((value) << MEM2MEM_TPR_TXPTR_Pos))
#define MEM2MEM_TPR_Msk                       (0xFFFFFFFFUL)                                 /**< (MEM2MEM_TPR) Register Mask  */

/* -------- MEM2MEM_TCR : (MEM2MEM Offset: 0x10C) (R/W 32) Transmit Counter Register -------- */
#define MEM2MEM_TCR_TXCTR_Pos                 (0U)                                           /**< (MEM2MEM_TCR) Transmit Counter Register Position */
#define MEM2MEM_TCR_TXCTR_Msk                 (0xFFFFU << MEM2MEM_TCR_TXCTR_Pos)             /**< (MEM2MEM_TCR) Transmit Counter Register Mask */
#define MEM2MEM_TCR_TXCTR(value)              (MEM2MEM_TCR_TXCTR_Msk & ((value) << MEM2MEM_TCR_TXCTR_Pos))
#define MEM2MEM_TCR_Msk                       (0x0000FFFFUL)                                 /**< (MEM2MEM_TCR) Register Mask  */

/* -------- MEM2MEM_RNPR : (MEM2MEM Offset: 0x110) (R/W 32) Receive Next Pointer Register -------- */
#define MEM2MEM_RNPR_RXNPTR_Pos               (0U)                                           /**< (MEM2MEM_RNPR) Receive Next Pointer Position */
#define MEM2MEM_RNPR_RXNPTR_Msk               (0xFFFFFFFFU << MEM2MEM_RNPR_RXNPTR_Pos)       /**< (MEM2MEM_RNPR) Receive Next Pointer Mask */
#define MEM2MEM_RNPR_RXNPTR(value)            (MEM2MEM_RNPR_RXNPTR_Msk & ((value) << MEM2MEM_RNPR_RXNPTR_Pos))
#define MEM2MEM_RNPR_Msk                      (0xFFFFFFFFUL)                                 /**< (MEM2MEM_RNPR) Register Mask  */

/* -------- MEM2MEM_RNCR : (MEM2MEM Offset: 0x114) (R/W 32) Receive Next Counter Register -------- */
#define MEM2MEM_RNCR_RXNCTR_Pos               (0U)                                           /**< (MEM2MEM_RNCR) Receive Next Counter Position */
#define MEM2MEM_RNCR_RXNCTR_Msk               (0xFFFFU << MEM2MEM_RNCR_RXNCTR_Pos)           /**< (MEM2MEM_RNCR) Receive Next Counter Mask */
#define MEM2MEM_RNCR_RXNCTR(value)            (MEM2MEM_RNCR_RXNCTR_Msk & ((value) << MEM2MEM_RNCR_RXNCTR_Pos))
#define MEM2MEM_RNCR_Msk                      (0x0000FFFFUL)                                 /**< (MEM2MEM_RNCR) Register Mask  */

/* -------- MEM2MEM_TNPR : (MEM2MEM Offset: 0x118) (R/W 32) Transmit Next Pointer Register -------- */
#define MEM2MEM_TNPR_TXNPTR_Pos               (0U)                                           /**< (MEM2MEM_TNPR) Transmit Next Pointer Position */
#define MEM2MEM_TNPR_TXNPTR_Msk               (0xFFFFFFFFU << MEM2MEM_TNPR_TXNPTR_Pos)       /**< (MEM2MEM_TNPR) Transmit Next Pointer Mask */
#define MEM2MEM_TNPR_TXNPTR(value)            (MEM2MEM_TNPR_TXNPTR_Msk & ((value) << MEM2MEM_TNPR_TXNPTR_Pos))
#define MEM2MEM_TNPR_Msk                      (0xFFFFFFFFUL)                                 /**< (MEM2MEM_TNPR) Register Mask  */

/* -------- MEM2MEM_TNCR : (MEM2MEM Offset: 0x11C) (R/W 32) Transmit Next Counter Register -------- */
#define MEM2MEM_TNCR_TXNCTR_Pos               (0U)                                           /**< (MEM2MEM_TNCR) Transmit Counter Next Position */
#define MEM2MEM_TNCR_TXNCTR_Msk               (0xFFFFU << MEM2MEM_TNCR_TXNCTR_Pos)           /**< (MEM2MEM_TNCR) Transmit Counter Next Mask */
#define MEM2MEM_TNCR_TXNCTR(value)            (MEM2MEM_TNCR_TXNCTR_Msk & ((value) << MEM2MEM_TNCR_TXNCTR_Pos))
#define MEM2MEM_TNCR_Msk                      (0x0000FFFFUL)                                 /**< (MEM2MEM_TNCR) Register Mask  */

/* -------- MEM2MEM_PTCR : (MEM2MEM Offset: 0x120) ( /W 32) Transfer Control Register -------- */
#define MEM2MEM_PTCR_RXTEN_Pos                (0U)                                           /**< (MEM2MEM_PTCR) Receiver Transfer Enable Position */
#define MEM2MEM_PTCR_RXTEN_Msk                (0x1U << MEM2MEM_PTCR_RXTEN_Pos)               /**< (MEM2MEM_PTCR) Receiver Transfer Enable Mask */
#define MEM2MEM_PTCR_RXTEN(value)             (MEM2MEM_PTCR_RXTEN_Msk & ((value) << MEM2MEM_PTCR_RXTEN_Pos))
#define MEM2MEM_PTCR_RXTDIS_Pos               (1U)                                           /**< (MEM2MEM_PTCR) Receiver Transfer Disable Position */
#define MEM2MEM_PTCR_RXTDIS_Msk               (0x1U << MEM2MEM_PTCR_RXTDIS_Pos)              /**< (MEM2MEM_PTCR) Receiver Transfer Disable Mask */
#define MEM2MEM_PTCR_RXTDIS(value)            (MEM2MEM_PTCR_RXTDIS_Msk & ((value) << MEM2MEM_PTCR_RXTDIS_Pos))
#define MEM2MEM_PTCR_TXTEN_Pos                (8U)                                           /**< (MEM2MEM_PTCR) Transmitter Transfer Enable Position */
#define MEM2MEM_PTCR_TXTEN_Msk                (0x1U << MEM2MEM_PTCR_TXTEN_Pos)               /**< (MEM2MEM_PTCR) Transmitter Transfer Enable Mask */
#define MEM2MEM_PTCR_TXTEN(value)             (MEM2MEM_PTCR_TXTEN_Msk & ((value) << MEM2MEM_PTCR_TXTEN_Pos))
#define MEM2MEM_PTCR_TXTDIS_Pos               (9U)                                           /**< (MEM2MEM_PTCR) Transmitter Transfer Disable Position */
#define MEM2MEM_PTCR_TXTDIS_Msk               (0x1U << MEM2MEM_PTCR_TXTDIS_Pos)              /**< (MEM2MEM_PTCR) Transmitter Transfer Disable Mask */
#define MEM2MEM_PTCR_TXTDIS(value)            (MEM2MEM_PTCR_TXTDIS_Msk & ((value) << MEM2MEM_PTCR_TXTDIS_Pos))
#define MEM2MEM_PTCR_RXCBEN_Pos               (16U)                                          /**< (MEM2MEM_PTCR) Receiver Circular Buffer Enable Position */
#define MEM2MEM_PTCR_RXCBEN_Msk               (0x1U << MEM2MEM_PTCR_RXCBEN_Pos)              /**< (MEM2MEM_PTCR) Receiver Circular Buffer Enable Mask */
#define MEM2MEM_PTCR_RXCBEN(value)            (MEM2MEM_PTCR_RXCBEN_Msk & ((value) << MEM2MEM_PTCR_RXCBEN_Pos))
#define MEM2MEM_PTCR_RXCBDIS_Pos              (17U)                                          /**< (MEM2MEM_PTCR) Receiver Circular Buffer Disable Position */
#define MEM2MEM_PTCR_RXCBDIS_Msk              (0x1U << MEM2MEM_PTCR_RXCBDIS_Pos)             /**< (MEM2MEM_PTCR) Receiver Circular Buffer Disable Mask */
#define MEM2MEM_PTCR_RXCBDIS(value)           (MEM2MEM_PTCR_RXCBDIS_Msk & ((value) << MEM2MEM_PTCR_RXCBDIS_Pos))
#define MEM2MEM_PTCR_TXCBEN_Pos               (18U)                                          /**< (MEM2MEM_PTCR) Transmitter Circular Buffer Enable Position */
#define MEM2MEM_PTCR_TXCBEN_Msk               (0x1U << MEM2MEM_PTCR_TXCBEN_Pos)              /**< (MEM2MEM_PTCR) Transmitter Circular Buffer Enable Mask */
#define MEM2MEM_PTCR_TXCBEN(value)            (MEM2MEM_PTCR_TXCBEN_Msk & ((value) << MEM2MEM_PTCR_TXCBEN_Pos))
#define MEM2MEM_PTCR_TXCBDIS_Pos              (19U)                                          /**< (MEM2MEM_PTCR) Transmitter Circular Buffer Disable Position */
#define MEM2MEM_PTCR_TXCBDIS_Msk              (0x1U << MEM2MEM_PTCR_TXCBDIS_Pos)             /**< (MEM2MEM_PTCR) Transmitter Circular Buffer Disable Mask */
#define MEM2MEM_PTCR_TXCBDIS(value)           (MEM2MEM_PTCR_TXCBDIS_Msk & ((value) << MEM2MEM_PTCR_TXCBDIS_Pos))
#define MEM2MEM_PTCR_ERRCLR_Pos               (24U)                                          /**< (MEM2MEM_PTCR) Transfer Bus Error Clear Position */
#define MEM2MEM_PTCR_ERRCLR_Msk               (0x1U << MEM2MEM_PTCR_ERRCLR_Pos)              /**< (MEM2MEM_PTCR) Transfer Bus Error Clear Mask */
#define MEM2MEM_PTCR_ERRCLR(value)            (MEM2MEM_PTCR_ERRCLR_Msk & ((value) << MEM2MEM_PTCR_ERRCLR_Pos))
#define MEM2MEM_PTCR_Msk                      (0x010F0303UL)                                 /**< (MEM2MEM_PTCR) Register Mask  */

/* -------- MEM2MEM_PTSR : (MEM2MEM Offset: 0x124) (R/  32) Transfer Status Register -------- */
#define MEM2MEM_PTSR_RXTEN_Pos                (0U)                                           /**< (MEM2MEM_PTSR) Receiver Transfer Enable Position */
#define MEM2MEM_PTSR_RXTEN_Msk                (0x1U << MEM2MEM_PTSR_RXTEN_Pos)               /**< (MEM2MEM_PTSR) Receiver Transfer Enable Mask */
#define MEM2MEM_PTSR_RXTEN(value)             (MEM2MEM_PTSR_RXTEN_Msk & ((value) << MEM2MEM_PTSR_RXTEN_Pos))
#define MEM2MEM_PTSR_TXTEN_Pos                (8U)                                           /**< (MEM2MEM_PTSR) Transmitter Transfer Enable Position */
#define MEM2MEM_PTSR_TXTEN_Msk                (0x1U << MEM2MEM_PTSR_TXTEN_Pos)               /**< (MEM2MEM_PTSR) Transmitter Transfer Enable Mask */
#define MEM2MEM_PTSR_TXTEN(value)             (MEM2MEM_PTSR_TXTEN_Msk & ((value) << MEM2MEM_PTSR_TXTEN_Pos))
#define MEM2MEM_PTSR_RXCBEN_Pos               (16U)                                          /**< (MEM2MEM_PTSR) Receiver Circular Buffer Enable Position */
#define MEM2MEM_PTSR_RXCBEN_Msk               (0x1U << MEM2MEM_PTSR_RXCBEN_Pos)              /**< (MEM2MEM_PTSR) Receiver Circular Buffer Enable Mask */
#define MEM2MEM_PTSR_RXCBEN(value)            (MEM2MEM_PTSR_RXCBEN_Msk & ((value) << MEM2MEM_PTSR_RXCBEN_Pos))
#define MEM2MEM_PTSR_TXCBEN_Pos               (18U)                                          /**< (MEM2MEM_PTSR) Transmitter Circular Buffer Enable Position */
#define MEM2MEM_PTSR_TXCBEN_Msk               (0x1U << MEM2MEM_PTSR_TXCBEN_Pos)              /**< (MEM2MEM_PTSR) Transmitter Circular Buffer Enable Mask */
#define MEM2MEM_PTSR_TXCBEN(value)            (MEM2MEM_PTSR_TXCBEN_Msk & ((value) << MEM2MEM_PTSR_TXCBEN_Pos))
#define MEM2MEM_PTSR_ERR_Pos                  (24U)                                          /**< (MEM2MEM_PTSR) Transfer Bus Error Position */
#define MEM2MEM_PTSR_ERR_Msk                  (0x1U << MEM2MEM_PTSR_ERR_Pos)                 /**< (MEM2MEM_PTSR) Transfer Bus Error Mask */
#define MEM2MEM_PTSR_ERR(value)               (MEM2MEM_PTSR_ERR_Msk & ((value) << MEM2MEM_PTSR_ERR_Pos))
#define MEM2MEM_PTSR_Msk                      (0x01050101UL)                                 /**< (MEM2MEM_PTSR) Register Mask  */

/** \brief MEM2MEM register offsets definitions */
#define MEM2MEM_THR_OFFSET             (0x00)         /**< (MEM2MEM_THR) Memory to Memory Transfer Holding Register Offset */
#define MEM2MEM_MR_OFFSET              (0x04)         /**< (MEM2MEM_MR) Memory to Memory Mode Register Offset */
#define MEM2MEM_IER_OFFSET             (0x08)         /**< (MEM2MEM_IER) Memory to Memory Interrupt Enable Register Offset */
#define MEM2MEM_IDR_OFFSET             (0x0C)         /**< (MEM2MEM_IDR) Memory to Memory Interrupt Disable Register Offset */
#define MEM2MEM_IMR_OFFSET             (0x10)         /**< (MEM2MEM_IMR) Memory to Memory Interrupt Mask Register Offset */
#define MEM2MEM_ISR_OFFSET             (0x14)         /**< (MEM2MEM_ISR) Memory to Memory Interrupt Status Register Offset */
#define MEM2MEM_RPR_OFFSET             (0x100)        /**< (MEM2MEM_RPR) Receive Pointer Register Offset */
#define MEM2MEM_RCR_OFFSET             (0x104)        /**< (MEM2MEM_RCR) Receive Counter Register Offset */
#define MEM2MEM_TPR_OFFSET             (0x108)        /**< (MEM2MEM_TPR) Transmit Pointer Register Offset */
#define MEM2MEM_TCR_OFFSET             (0x10C)        /**< (MEM2MEM_TCR) Transmit Counter Register Offset */
#define MEM2MEM_RNPR_OFFSET            (0x110)        /**< (MEM2MEM_RNPR) Receive Next Pointer Register Offset */
#define MEM2MEM_RNCR_OFFSET            (0x114)        /**< (MEM2MEM_RNCR) Receive Next Counter Register Offset */
#define MEM2MEM_TNPR_OFFSET            (0x118)        /**< (MEM2MEM_TNPR) Transmit Next Pointer Register Offset */
#define MEM2MEM_TNCR_OFFSET            (0x11C)        /**< (MEM2MEM_TNCR) Transmit Next Counter Register Offset */
#define MEM2MEM_PTCR_OFFSET            (0x120)        /**< (MEM2MEM_PTCR) Transfer Control Register Offset */
#define MEM2MEM_PTSR_OFFSET            (0x124)        /**< (MEM2MEM_PTSR) Transfer Status Register Offset */

/** \brief MEM2MEM register API structure */
typedef struct
{
  __IO  uint32_t                       MEM2MEM_THR;     /**< Offset: 0x00 (R/W  32) Memory to Memory Transfer Holding Register */
  __IO  uint32_t                       MEM2MEM_MR;      /**< Offset: 0x04 (R/W  32) Memory to Memory Mode Register */
  __O   uint32_t                       MEM2MEM_IER;     /**< Offset: 0x08 ( /W  32) Memory to Memory Interrupt Enable Register */
  __O   uint32_t                       MEM2MEM_IDR;     /**< Offset: 0x0c ( /W  32) Memory to Memory Interrupt Disable Register */
  __I   uint32_t                       MEM2MEM_IMR;     /**< Offset: 0x10 (R/   32) Memory to Memory Interrupt Mask Register */
  __I   uint32_t                       MEM2MEM_ISR;     /**< Offset: 0x14 (R/   32) Memory to Memory Interrupt Status Register */
  __I   uint8_t                        Reserved1[0xE8];
  __IO  uint32_t                       MEM2MEM_RPR;     /**< Offset: 0x100 (R/W  32) Receive Pointer Register */
  __IO  uint32_t                       MEM2MEM_RCR;     /**< Offset: 0x104 (R/W  32) Receive Counter Register */
  __IO  uint32_t                       MEM2MEM_TPR;     /**< Offset: 0x108 (R/W  32) Transmit Pointer Register */
  __IO  uint32_t                       MEM2MEM_TCR;     /**< Offset: 0x10c (R/W  32) Transmit Counter Register */
  __IO  uint32_t                       MEM2MEM_RNPR;    /**< Offset: 0x110 (R/W  32) Receive Next Pointer Register */
  __IO  uint32_t                       MEM2MEM_RNCR;    /**< Offset: 0x114 (R/W  32) Receive Next Counter Register */
  __IO  uint32_t                       MEM2MEM_TNPR;    /**< Offset: 0x118 (R/W  32) Transmit Next Pointer Register */
  __IO  uint32_t                       MEM2MEM_TNCR;    /**< Offset: 0x11c (R/W  32) Transmit Next Counter Register */
  __O   uint32_t                       MEM2MEM_PTCR;    /**< Offset: 0x120 ( /W  32) Transfer Control Register */
  __I   uint32_t                       MEM2MEM_PTSR;    /**< Offset: 0x124 (R/   32) Transfer Status Register */
} mem2mem_registers_t;
/** @}  end of Memory to Memory */

#endif /* SAMG_SAMG55_MEM2MEM_MODULE_H */

