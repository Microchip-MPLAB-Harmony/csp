/**
 * \brief Header file for SAMG/SAMG55 CRCCU
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
#ifndef SAMG_SAMG55_CRCCU_MODULE_H
#define SAMG_SAMG55_CRCCU_MODULE_H

/** \addtogroup SAMG_SAMG55 Cyclic Redundancy Check Calculation Unit
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_CRCCU                                 */
/* ========================================================================== */

/* -------- CRCCU_DSCR : (CRCCU Offset: 0x00) (R/W 32) CRCCU Descriptor Base Register -------- */
#define CRCCU_DSCR_DSCR_Pos                   (9U)                                           /**< (CRCCU_DSCR) Descriptor Base Address Position */
#define CRCCU_DSCR_DSCR_Msk                   (0x7FFFFFU << CRCCU_DSCR_DSCR_Pos)             /**< (CRCCU_DSCR) Descriptor Base Address Mask */
#define CRCCU_DSCR_DSCR(value)                (CRCCU_DSCR_DSCR_Msk & ((value) << CRCCU_DSCR_DSCR_Pos))
#define CRCCU_DSCR_Msk                        (0xFFFFFE00UL)                                 /**< (CRCCU_DSCR) Register Mask  */

/* -------- CRCCU_DMA_EN : (CRCCU Offset: 0x08) ( /W 32) CRCCU DMA Enable Register -------- */
#define CRCCU_DMA_EN_DMAEN_Pos                (0U)                                           /**< (CRCCU_DMA_EN) DMA Enable Position */
#define CRCCU_DMA_EN_DMAEN_Msk                (0x1U << CRCCU_DMA_EN_DMAEN_Pos)               /**< (CRCCU_DMA_EN) DMA Enable Mask */
#define CRCCU_DMA_EN_DMAEN(value)             (CRCCU_DMA_EN_DMAEN_Msk & ((value) << CRCCU_DMA_EN_DMAEN_Pos))
#define CRCCU_DMA_EN_Msk                      (0x00000001UL)                                 /**< (CRCCU_DMA_EN) Register Mask  */

/* -------- CRCCU_DMA_DIS : (CRCCU Offset: 0x0C) ( /W 32) CRCCU DMA Disable Register -------- */
#define CRCCU_DMA_DIS_DMADIS_Pos              (0U)                                           /**< (CRCCU_DMA_DIS) DMA Disable Position */
#define CRCCU_DMA_DIS_DMADIS_Msk              (0x1U << CRCCU_DMA_DIS_DMADIS_Pos)             /**< (CRCCU_DMA_DIS) DMA Disable Mask */
#define CRCCU_DMA_DIS_DMADIS(value)           (CRCCU_DMA_DIS_DMADIS_Msk & ((value) << CRCCU_DMA_DIS_DMADIS_Pos))
#define CRCCU_DMA_DIS_Msk                     (0x00000001UL)                                 /**< (CRCCU_DMA_DIS) Register Mask  */

/* -------- CRCCU_DMA_SR : (CRCCU Offset: 0x10) (R/  32) CRCCU DMA Status Register -------- */
#define CRCCU_DMA_SR_DMASR_Pos                (0U)                                           /**< (CRCCU_DMA_SR) DMA Status Position */
#define CRCCU_DMA_SR_DMASR_Msk                (0x1U << CRCCU_DMA_SR_DMASR_Pos)               /**< (CRCCU_DMA_SR) DMA Status Mask */
#define CRCCU_DMA_SR_DMASR(value)             (CRCCU_DMA_SR_DMASR_Msk & ((value) << CRCCU_DMA_SR_DMASR_Pos))
#define CRCCU_DMA_SR_Msk                      (0x00000001UL)                                 /**< (CRCCU_DMA_SR) Register Mask  */

/* -------- CRCCU_DMA_IER : (CRCCU Offset: 0x14) ( /W 32) CRCCU DMA Interrupt Enable Register -------- */
#define CRCCU_DMA_IER_DMAIER_Pos              (0U)                                           /**< (CRCCU_DMA_IER) Interrupt Enable Position */
#define CRCCU_DMA_IER_DMAIER_Msk              (0x1U << CRCCU_DMA_IER_DMAIER_Pos)             /**< (CRCCU_DMA_IER) Interrupt Enable Mask */
#define CRCCU_DMA_IER_DMAIER(value)           (CRCCU_DMA_IER_DMAIER_Msk & ((value) << CRCCU_DMA_IER_DMAIER_Pos))
#define CRCCU_DMA_IER_Msk                     (0x00000001UL)                                 /**< (CRCCU_DMA_IER) Register Mask  */

/* -------- CRCCU_DMA_IDR : (CRCCU Offset: 0x18) ( /W 32) CRCCU DMA Interrupt Disable Register -------- */
#define CRCCU_DMA_IDR_DMAIDR_Pos              (0U)                                           /**< (CRCCU_DMA_IDR) Interrupt Disable Position */
#define CRCCU_DMA_IDR_DMAIDR_Msk              (0x1U << CRCCU_DMA_IDR_DMAIDR_Pos)             /**< (CRCCU_DMA_IDR) Interrupt Disable Mask */
#define CRCCU_DMA_IDR_DMAIDR(value)           (CRCCU_DMA_IDR_DMAIDR_Msk & ((value) << CRCCU_DMA_IDR_DMAIDR_Pos))
#define CRCCU_DMA_IDR_Msk                     (0x00000001UL)                                 /**< (CRCCU_DMA_IDR) Register Mask  */

/* -------- CRCCU_DMA_IMR : (CRCCU Offset: 0x1C) (R/  32) CRCCU DMA Interrupt Mask Register -------- */
#define CRCCU_DMA_IMR_DMAIMR_Pos              (0U)                                           /**< (CRCCU_DMA_IMR) Interrupt Mask Position */
#define CRCCU_DMA_IMR_DMAIMR_Msk              (0x1U << CRCCU_DMA_IMR_DMAIMR_Pos)             /**< (CRCCU_DMA_IMR) Interrupt Mask Mask */
#define CRCCU_DMA_IMR_DMAIMR(value)           (CRCCU_DMA_IMR_DMAIMR_Msk & ((value) << CRCCU_DMA_IMR_DMAIMR_Pos))
#define CRCCU_DMA_IMR_Msk                     (0x00000001UL)                                 /**< (CRCCU_DMA_IMR) Register Mask  */

/* -------- CRCCU_DMA_ISR : (CRCCU Offset: 0x20) (R/  32) CRCCU DMA Interrupt Status Register -------- */
#define CRCCU_DMA_ISR_DMAISR_Pos              (0U)                                           /**< (CRCCU_DMA_ISR) Interrupt Status Position */
#define CRCCU_DMA_ISR_DMAISR_Msk              (0x1U << CRCCU_DMA_ISR_DMAISR_Pos)             /**< (CRCCU_DMA_ISR) Interrupt Status Mask */
#define CRCCU_DMA_ISR_DMAISR(value)           (CRCCU_DMA_ISR_DMAISR_Msk & ((value) << CRCCU_DMA_ISR_DMAISR_Pos))
#define CRCCU_DMA_ISR_Msk                     (0x00000001UL)                                 /**< (CRCCU_DMA_ISR) Register Mask  */

/* -------- CRCCU_CR : (CRCCU Offset: 0x34) ( /W 32) CRCCU Control Register -------- */
#define CRCCU_CR_RESET_Pos                    (0U)                                           /**< (CRCCU_CR) CRC Computation Reset Position */
#define CRCCU_CR_RESET_Msk                    (0x1U << CRCCU_CR_RESET_Pos)                   /**< (CRCCU_CR) CRC Computation Reset Mask */
#define CRCCU_CR_RESET(value)                 (CRCCU_CR_RESET_Msk & ((value) << CRCCU_CR_RESET_Pos))
#define CRCCU_CR_Msk                          (0x00000001UL)                                 /**< (CRCCU_CR) Register Mask  */

/* -------- CRCCU_MR : (CRCCU Offset: 0x38) (R/W 32) CRCCU Mode Register -------- */
#define CRCCU_MR_ENABLE_Pos                   (0U)                                           /**< (CRCCU_MR) CRC Enable Position */
#define CRCCU_MR_ENABLE_Msk                   (0x1U << CRCCU_MR_ENABLE_Pos)                  /**< (CRCCU_MR) CRC Enable Mask */
#define CRCCU_MR_ENABLE(value)                (CRCCU_MR_ENABLE_Msk & ((value) << CRCCU_MR_ENABLE_Pos))
#define CRCCU_MR_COMPARE_Pos                  (1U)                                           /**< (CRCCU_MR) CRC Compare Position */
#define CRCCU_MR_COMPARE_Msk                  (0x1U << CRCCU_MR_COMPARE_Pos)                 /**< (CRCCU_MR) CRC Compare Mask */
#define CRCCU_MR_COMPARE(value)               (CRCCU_MR_COMPARE_Msk & ((value) << CRCCU_MR_COMPARE_Pos))
#define CRCCU_MR_PTYPE_Pos                    (2U)                                           /**< (CRCCU_MR) Primitive Polynomial Position */
#define CRCCU_MR_PTYPE_Msk                    (0x3U << CRCCU_MR_PTYPE_Pos)                   /**< (CRCCU_MR) Primitive Polynomial Mask */
#define CRCCU_MR_PTYPE(value)                 (CRCCU_MR_PTYPE_Msk & ((value) << CRCCU_MR_PTYPE_Pos))
#define   CRCCU_MR_PTYPE_CCITT8023_Val        (0U)                                           /**< (CRCCU_MR) Polynom 0x04C11DB7  */
#define   CRCCU_MR_PTYPE_CASTAGNOLI_Val       (1U)                                           /**< (CRCCU_MR) Polynom 0x1EDC6F41  */
#define   CRCCU_MR_PTYPE_CCITT16_Val          (2U)                                           /**< (CRCCU_MR) Polynom 0x1021  */
#define CRCCU_MR_PTYPE_CCITT8023              (CRCCU_MR_PTYPE_CCITT8023_Val << CRCCU_MR_PTYPE_Pos) /**< (CRCCU_MR) Polynom 0x04C11DB7 Position  */
#define CRCCU_MR_PTYPE_CASTAGNOLI             (CRCCU_MR_PTYPE_CASTAGNOLI_Val << CRCCU_MR_PTYPE_Pos) /**< (CRCCU_MR) Polynom 0x1EDC6F41 Position  */
#define CRCCU_MR_PTYPE_CCITT16                (CRCCU_MR_PTYPE_CCITT16_Val << CRCCU_MR_PTYPE_Pos) /**< (CRCCU_MR) Polynom 0x1021 Position  */
#define CRCCU_MR_DIVIDER_Pos                  (4U)                                           /**< (CRCCU_MR) Request Divider Position */
#define CRCCU_MR_DIVIDER_Msk                  (0xFU << CRCCU_MR_DIVIDER_Pos)                 /**< (CRCCU_MR) Request Divider Mask */
#define CRCCU_MR_DIVIDER(value)               (CRCCU_MR_DIVIDER_Msk & ((value) << CRCCU_MR_DIVIDER_Pos))
#define CRCCU_MR_BITORDER_Pos                 (17U)                                          /**< (CRCCU_MR) Precomputation Bit Swap Operation of the CRC Position */
#define CRCCU_MR_BITORDER_Msk                 (0x1U << CRCCU_MR_BITORDER_Pos)                /**< (CRCCU_MR) Precomputation Bit Swap Operation of the CRC Mask */
#define CRCCU_MR_BITORDER(value)              (CRCCU_MR_BITORDER_Msk & ((value) << CRCCU_MR_BITORDER_Pos))
#define   CRCCU_MR_BITORDER_MSBFIRST_Val      (0U)                                           /**< (CRCCU_MR) CRC computation is performed from the most significant bit to the least significant bit  */
#define   CRCCU_MR_BITORDER_LSBFIRST_Val      (1U)                                           /**< (CRCCU_MR) CRC computation is performed from the least significant bit to the most significant bit  */
#define CRCCU_MR_BITORDER_MSBFIRST            (CRCCU_MR_BITORDER_MSBFIRST_Val << CRCCU_MR_BITORDER_Pos) /**< (CRCCU_MR) CRC computation is performed from the most significant bit to the least significant bit Position  */
#define CRCCU_MR_BITORDER_LSBFIRST            (CRCCU_MR_BITORDER_LSBFIRST_Val << CRCCU_MR_BITORDER_Pos) /**< (CRCCU_MR) CRC computation is performed from the least significant bit to the most significant bit Position  */
#define CRCCU_MR_Msk                          (0x000200FFUL)                                 /**< (CRCCU_MR) Register Mask  */

/* -------- CRCCU_SR : (CRCCU Offset: 0x3C) (R/  32) CRCCU Status Register -------- */
#define CRCCU_SR_CRC_Pos                      (0U)                                           /**< (CRCCU_SR) Cyclic Redundancy Check Value Position */
#define CRCCU_SR_CRC_Msk                      (0xFFFFFFFFU << CRCCU_SR_CRC_Pos)              /**< (CRCCU_SR) Cyclic Redundancy Check Value Mask */
#define CRCCU_SR_CRC(value)                   (CRCCU_SR_CRC_Msk & ((value) << CRCCU_SR_CRC_Pos))
#define CRCCU_SR_Msk                          (0xFFFFFFFFUL)                                 /**< (CRCCU_SR) Register Mask  */

/* -------- CRCCU_IER : (CRCCU Offset: 0x40) ( /W 32) CRCCU Interrupt Enable Register -------- */
#define CRCCU_IER_ERRIER_Pos                  (0U)                                           /**< (CRCCU_IER) CRC Error Interrupt Enable Position */
#define CRCCU_IER_ERRIER_Msk                  (0x1U << CRCCU_IER_ERRIER_Pos)                 /**< (CRCCU_IER) CRC Error Interrupt Enable Mask */
#define CRCCU_IER_ERRIER(value)               (CRCCU_IER_ERRIER_Msk & ((value) << CRCCU_IER_ERRIER_Pos))
#define CRCCU_IER_Msk                         (0x00000001UL)                                 /**< (CRCCU_IER) Register Mask  */

/* -------- CRCCU_IDR : (CRCCU Offset: 0x44) ( /W 32) CRCCU Interrupt Disable Register -------- */
#define CRCCU_IDR_ERRIDR_Pos                  (0U)                                           /**< (CRCCU_IDR) CRC Error Interrupt Disable Position */
#define CRCCU_IDR_ERRIDR_Msk                  (0x1U << CRCCU_IDR_ERRIDR_Pos)                 /**< (CRCCU_IDR) CRC Error Interrupt Disable Mask */
#define CRCCU_IDR_ERRIDR(value)               (CRCCU_IDR_ERRIDR_Msk & ((value) << CRCCU_IDR_ERRIDR_Pos))
#define CRCCU_IDR_Msk                         (0x00000001UL)                                 /**< (CRCCU_IDR) Register Mask  */

/* -------- CRCCU_IMR : (CRCCU Offset: 0x48) (R/  32) CRCCU Interrupt Mask Register -------- */
#define CRCCU_IMR_ERRIMR_Pos                  (0U)                                           /**< (CRCCU_IMR) CRC Error Interrupt Mask Position */
#define CRCCU_IMR_ERRIMR_Msk                  (0x1U << CRCCU_IMR_ERRIMR_Pos)                 /**< (CRCCU_IMR) CRC Error Interrupt Mask Mask */
#define CRCCU_IMR_ERRIMR(value)               (CRCCU_IMR_ERRIMR_Msk & ((value) << CRCCU_IMR_ERRIMR_Pos))
#define CRCCU_IMR_Msk                         (0x00000001UL)                                 /**< (CRCCU_IMR) Register Mask  */

/* -------- CRCCU_ISR : (CRCCU Offset: 0x4C) (R/  32) CRCCU Interrupt Status Register -------- */
#define CRCCU_ISR_ERRISR_Pos                  (0U)                                           /**< (CRCCU_ISR) CRC Error Interrupt Status Position */
#define CRCCU_ISR_ERRISR_Msk                  (0x1U << CRCCU_ISR_ERRISR_Pos)                 /**< (CRCCU_ISR) CRC Error Interrupt Status Mask */
#define CRCCU_ISR_ERRISR(value)               (CRCCU_ISR_ERRISR_Msk & ((value) << CRCCU_ISR_ERRISR_Pos))
#define CRCCU_ISR_Msk                         (0x00000001UL)                                 /**< (CRCCU_ISR) Register Mask  */

/** \brief CRCCU register offsets definitions */
#define CRCCU_DSCR_OFFSET              (0x00)         /**< (CRCCU_DSCR) CRCCU Descriptor Base Register Offset */
#define CRCCU_DMA_EN_OFFSET            (0x08)         /**< (CRCCU_DMA_EN) CRCCU DMA Enable Register Offset */
#define CRCCU_DMA_DIS_OFFSET           (0x0C)         /**< (CRCCU_DMA_DIS) CRCCU DMA Disable Register Offset */
#define CRCCU_DMA_SR_OFFSET            (0x10)         /**< (CRCCU_DMA_SR) CRCCU DMA Status Register Offset */
#define CRCCU_DMA_IER_OFFSET           (0x14)         /**< (CRCCU_DMA_IER) CRCCU DMA Interrupt Enable Register Offset */
#define CRCCU_DMA_IDR_OFFSET           (0x18)         /**< (CRCCU_DMA_IDR) CRCCU DMA Interrupt Disable Register Offset */
#define CRCCU_DMA_IMR_OFFSET           (0x1C)         /**< (CRCCU_DMA_IMR) CRCCU DMA Interrupt Mask Register Offset */
#define CRCCU_DMA_ISR_OFFSET           (0x20)         /**< (CRCCU_DMA_ISR) CRCCU DMA Interrupt Status Register Offset */
#define CRCCU_CR_OFFSET                (0x34)         /**< (CRCCU_CR) CRCCU Control Register Offset */
#define CRCCU_MR_OFFSET                (0x38)         /**< (CRCCU_MR) CRCCU Mode Register Offset */
#define CRCCU_SR_OFFSET                (0x3C)         /**< (CRCCU_SR) CRCCU Status Register Offset */
#define CRCCU_IER_OFFSET               (0x40)         /**< (CRCCU_IER) CRCCU Interrupt Enable Register Offset */
#define CRCCU_IDR_OFFSET               (0x44)         /**< (CRCCU_IDR) CRCCU Interrupt Disable Register Offset */
#define CRCCU_IMR_OFFSET               (0x48)         /**< (CRCCU_IMR) CRCCU Interrupt Mask Register Offset */
#define CRCCU_ISR_OFFSET               (0x4C)         /**< (CRCCU_ISR) CRCCU Interrupt Status Register Offset */

/** \brief CRCCU register API structure */
typedef struct
{
  __IO  uint32_t                       CRCCU_DSCR;      /**< Offset: 0x00 (R/W  32) CRCCU Descriptor Base Register */
  __I   uint8_t                        Reserved1[0x04];
  __O   uint32_t                       CRCCU_DMA_EN;    /**< Offset: 0x08 ( /W  32) CRCCU DMA Enable Register */
  __O   uint32_t                       CRCCU_DMA_DIS;   /**< Offset: 0x0c ( /W  32) CRCCU DMA Disable Register */
  __I   uint32_t                       CRCCU_DMA_SR;    /**< Offset: 0x10 (R/   32) CRCCU DMA Status Register */
  __O   uint32_t                       CRCCU_DMA_IER;   /**< Offset: 0x14 ( /W  32) CRCCU DMA Interrupt Enable Register */
  __O   uint32_t                       CRCCU_DMA_IDR;   /**< Offset: 0x18 ( /W  32) CRCCU DMA Interrupt Disable Register */
  __I   uint32_t                       CRCCU_DMA_IMR;   /**< Offset: 0x1c (R/   32) CRCCU DMA Interrupt Mask Register */
  __I   uint32_t                       CRCCU_DMA_ISR;   /**< Offset: 0x20 (R/   32) CRCCU DMA Interrupt Status Register */
  __I   uint8_t                        Reserved2[0x10];
  __O   uint32_t                       CRCCU_CR;        /**< Offset: 0x34 ( /W  32) CRCCU Control Register */
  __IO  uint32_t                       CRCCU_MR;        /**< Offset: 0x38 (R/W  32) CRCCU Mode Register */
  __I   uint32_t                       CRCCU_SR;        /**< Offset: 0x3c (R/   32) CRCCU Status Register */
  __O   uint32_t                       CRCCU_IER;       /**< Offset: 0x40 ( /W  32) CRCCU Interrupt Enable Register */
  __O   uint32_t                       CRCCU_IDR;       /**< Offset: 0x44 ( /W  32) CRCCU Interrupt Disable Register */
  __I   uint32_t                       CRCCU_IMR;       /**< Offset: 0x48 (R/   32) CRCCU Interrupt Mask Register */
  __I   uint32_t                       CRCCU_ISR;       /**< Offset: 0x4c (R/   32) CRCCU Interrupt Status Register */
} crccu_registers_t;
/** @}  end of Cyclic Redundancy Check Calculation Unit */

#endif /* SAMG_SAMG55_CRCCU_MODULE_H */

