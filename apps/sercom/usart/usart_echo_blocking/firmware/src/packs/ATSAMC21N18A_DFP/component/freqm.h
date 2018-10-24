/**
 * \brief Header file for SAMC/SAMC21 FREQM
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
#ifndef SAMC_SAMC21_FREQM_MODULE_H
#define SAMC_SAMC21_FREQM_MODULE_H

/** \addtogroup SAMC_SAMC21 Frequency Meter
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_FREQM                                 */
/* ========================================================================== */

/* -------- FREQM_CTRLA : (FREQM Offset: 0x00) (R/W 8) Control A Register -------- */
#define FREQM_CTRLA_SWRST_Pos                 (0U)                                           /**< (FREQM_CTRLA) Software Reset Position */
#define FREQM_CTRLA_SWRST_Msk                 (0x1U << FREQM_CTRLA_SWRST_Pos)                /**< (FREQM_CTRLA) Software Reset Mask */
#define FREQM_CTRLA_SWRST(value)              (FREQM_CTRLA_SWRST_Msk & ((value) << FREQM_CTRLA_SWRST_Pos))
#define FREQM_CTRLA_ENABLE_Pos                (1U)                                           /**< (FREQM_CTRLA) Enable Position */
#define FREQM_CTRLA_ENABLE_Msk                (0x1U << FREQM_CTRLA_ENABLE_Pos)               /**< (FREQM_CTRLA) Enable Mask */
#define FREQM_CTRLA_ENABLE(value)             (FREQM_CTRLA_ENABLE_Msk & ((value) << FREQM_CTRLA_ENABLE_Pos))
#define FREQM_CTRLA_Msk                       (0x00000003UL)                                 /**< (FREQM_CTRLA) Register Mask  */

/* -------- FREQM_CTRLB : (FREQM Offset: 0x01) ( /W 8) Control B Register -------- */
#define FREQM_CTRLB_START_Pos                 (0U)                                           /**< (FREQM_CTRLB) Start Measurement Position */
#define FREQM_CTRLB_START_Msk                 (0x1U << FREQM_CTRLB_START_Pos)                /**< (FREQM_CTRLB) Start Measurement Mask */
#define FREQM_CTRLB_START(value)              (FREQM_CTRLB_START_Msk & ((value) << FREQM_CTRLB_START_Pos))
#define FREQM_CTRLB_Msk                       (0x00000001UL)                                 /**< (FREQM_CTRLB) Register Mask  */

/* -------- FREQM_CFGA : (FREQM Offset: 0x02) (R/W 16) Config A register -------- */
#define FREQM_CFGA_REFNUM_Pos                 (0U)                                           /**< (FREQM_CFGA) Number of Reference Clock Cycles Position */
#define FREQM_CFGA_REFNUM_Msk                 (0xFFU << FREQM_CFGA_REFNUM_Pos)               /**< (FREQM_CFGA) Number of Reference Clock Cycles Mask */
#define FREQM_CFGA_REFNUM(value)              (FREQM_CFGA_REFNUM_Msk & ((value) << FREQM_CFGA_REFNUM_Pos))
#define FREQM_CFGA_DIVREF_Pos                 (15U)                                          /**< (FREQM_CFGA) Divide Reference Clock Position */
#define FREQM_CFGA_DIVREF_Msk                 (0x1U << FREQM_CFGA_DIVREF_Pos)                /**< (FREQM_CFGA) Divide Reference Clock Mask */
#define FREQM_CFGA_DIVREF(value)              (FREQM_CFGA_DIVREF_Msk & ((value) << FREQM_CFGA_DIVREF_Pos))
#define FREQM_CFGA_Msk                        (0x000080FFUL)                                 /**< (FREQM_CFGA) Register Mask  */

/* -------- FREQM_INTENCLR : (FREQM Offset: 0x08) (R/W 8) Interrupt Enable Clear Register -------- */
#define FREQM_INTENCLR_DONE_Pos               (0U)                                           /**< (FREQM_INTENCLR) Measurement Done Interrupt Enable Position */
#define FREQM_INTENCLR_DONE_Msk               (0x1U << FREQM_INTENCLR_DONE_Pos)              /**< (FREQM_INTENCLR) Measurement Done Interrupt Enable Mask */
#define FREQM_INTENCLR_DONE(value)            (FREQM_INTENCLR_DONE_Msk & ((value) << FREQM_INTENCLR_DONE_Pos))
#define FREQM_INTENCLR_Msk                    (0x00000001UL)                                 /**< (FREQM_INTENCLR) Register Mask  */

/* -------- FREQM_INTENSET : (FREQM Offset: 0x09) (R/W 8) Interrupt Enable Set Register -------- */
#define FREQM_INTENSET_DONE_Pos               (0U)                                           /**< (FREQM_INTENSET) Measurement Done Interrupt Enable Position */
#define FREQM_INTENSET_DONE_Msk               (0x1U << FREQM_INTENSET_DONE_Pos)              /**< (FREQM_INTENSET) Measurement Done Interrupt Enable Mask */
#define FREQM_INTENSET_DONE(value)            (FREQM_INTENSET_DONE_Msk & ((value) << FREQM_INTENSET_DONE_Pos))
#define FREQM_INTENSET_Msk                    (0x00000001UL)                                 /**< (FREQM_INTENSET) Register Mask  */

/* -------- FREQM_INTFLAG : (FREQM Offset: 0x0A) (R/W 8) Interrupt Flag Register -------- */
#define FREQM_INTFLAG_DONE_Pos                (0U)                                           /**< (FREQM_INTFLAG) Measurement Done Position */
#define FREQM_INTFLAG_DONE_Msk                (0x1U << FREQM_INTFLAG_DONE_Pos)               /**< (FREQM_INTFLAG) Measurement Done Mask */
#define FREQM_INTFLAG_DONE(value)             (FREQM_INTFLAG_DONE_Msk & ((value) << FREQM_INTFLAG_DONE_Pos))
#define FREQM_INTFLAG_Msk                     (0x00000001UL)                                 /**< (FREQM_INTFLAG) Register Mask  */

/* -------- FREQM_STATUS : (FREQM Offset: 0x0B) (R/W 8) Status Register -------- */
#define FREQM_STATUS_BUSY_Pos                 (0U)                                           /**< (FREQM_STATUS) FREQM Status Position */
#define FREQM_STATUS_BUSY_Msk                 (0x1U << FREQM_STATUS_BUSY_Pos)                /**< (FREQM_STATUS) FREQM Status Mask */
#define FREQM_STATUS_BUSY(value)              (FREQM_STATUS_BUSY_Msk & ((value) << FREQM_STATUS_BUSY_Pos))
#define FREQM_STATUS_OVF_Pos                  (1U)                                           /**< (FREQM_STATUS) Sticky Count Value Overflow Position */
#define FREQM_STATUS_OVF_Msk                  (0x1U << FREQM_STATUS_OVF_Pos)                 /**< (FREQM_STATUS) Sticky Count Value Overflow Mask */
#define FREQM_STATUS_OVF(value)               (FREQM_STATUS_OVF_Msk & ((value) << FREQM_STATUS_OVF_Pos))
#define FREQM_STATUS_Msk                      (0x00000003UL)                                 /**< (FREQM_STATUS) Register Mask  */

/* -------- FREQM_SYNCBUSY : (FREQM Offset: 0x0C) (R/  32) Synchronization Busy Register -------- */
#define FREQM_SYNCBUSY_SWRST_Pos              (0U)                                           /**< (FREQM_SYNCBUSY) Software Reset Position */
#define FREQM_SYNCBUSY_SWRST_Msk              (0x1U << FREQM_SYNCBUSY_SWRST_Pos)             /**< (FREQM_SYNCBUSY) Software Reset Mask */
#define FREQM_SYNCBUSY_SWRST(value)           (FREQM_SYNCBUSY_SWRST_Msk & ((value) << FREQM_SYNCBUSY_SWRST_Pos))
#define FREQM_SYNCBUSY_ENABLE_Pos             (1U)                                           /**< (FREQM_SYNCBUSY) Enable Position */
#define FREQM_SYNCBUSY_ENABLE_Msk             (0x1U << FREQM_SYNCBUSY_ENABLE_Pos)            /**< (FREQM_SYNCBUSY) Enable Mask */
#define FREQM_SYNCBUSY_ENABLE(value)          (FREQM_SYNCBUSY_ENABLE_Msk & ((value) << FREQM_SYNCBUSY_ENABLE_Pos))
#define FREQM_SYNCBUSY_Msk                    (0x00000003UL)                                 /**< (FREQM_SYNCBUSY) Register Mask  */

/* -------- FREQM_VALUE : (FREQM Offset: 0x10) (R/  32) Count Value Register -------- */
#define FREQM_VALUE_VALUE_Pos                 (0U)                                           /**< (FREQM_VALUE) Measurement Value Position */
#define FREQM_VALUE_VALUE_Msk                 (0xFFFFFFU << FREQM_VALUE_VALUE_Pos)           /**< (FREQM_VALUE) Measurement Value Mask */
#define FREQM_VALUE_VALUE(value)              (FREQM_VALUE_VALUE_Msk & ((value) << FREQM_VALUE_VALUE_Pos))
#define FREQM_VALUE_Msk                       (0x00FFFFFFUL)                                 /**< (FREQM_VALUE) Register Mask  */

/** \brief FREQM register offsets definitions */
#define FREQM_CTRLA_OFFSET             (0x00)         /**< (FREQM_CTRLA) Control A Register Offset */
#define FREQM_CTRLB_OFFSET             (0x01)         /**< (FREQM_CTRLB) Control B Register Offset */
#define FREQM_CFGA_OFFSET              (0x02)         /**< (FREQM_CFGA) Config A register Offset */
#define FREQM_INTENCLR_OFFSET          (0x08)         /**< (FREQM_INTENCLR) Interrupt Enable Clear Register Offset */
#define FREQM_INTENSET_OFFSET          (0x09)         /**< (FREQM_INTENSET) Interrupt Enable Set Register Offset */
#define FREQM_INTFLAG_OFFSET           (0x0A)         /**< (FREQM_INTFLAG) Interrupt Flag Register Offset */
#define FREQM_STATUS_OFFSET            (0x0B)         /**< (FREQM_STATUS) Status Register Offset */
#define FREQM_SYNCBUSY_OFFSET          (0x0C)         /**< (FREQM_SYNCBUSY) Synchronization Busy Register Offset */
#define FREQM_VALUE_OFFSET             (0x10)         /**< (FREQM_VALUE) Count Value Register Offset */

/** \brief FREQM register API structure */
typedef struct
{
  __IO  uint8_t                        FREQM_CTRLA;     /**< Offset: 0x00 (R/W  8) Control A Register */
  __O   uint8_t                        FREQM_CTRLB;     /**< Offset: 0x01 ( /W  8) Control B Register */
  __IO  uint16_t                       FREQM_CFGA;      /**< Offset: 0x02 (R/W  16) Config A register */
  __I   uint8_t                        Reserved1[0x04];
  __IO  uint8_t                        FREQM_INTENCLR;  /**< Offset: 0x08 (R/W  8) Interrupt Enable Clear Register */
  __IO  uint8_t                        FREQM_INTENSET;  /**< Offset: 0x09 (R/W  8) Interrupt Enable Set Register */
  __IO  uint8_t                        FREQM_INTFLAG;   /**< Offset: 0x0a (R/W  8) Interrupt Flag Register */
  __IO  uint8_t                        FREQM_STATUS;    /**< Offset: 0x0b (R/W  8) Status Register */
  __I   uint32_t                       FREQM_SYNCBUSY;  /**< Offset: 0x0c (R/   32) Synchronization Busy Register */
  __I   uint32_t                       FREQM_VALUE;     /**< Offset: 0x10 (R/   32) Count Value Register */
} freqm_registers_t;
/** @}  end of Frequency Meter */

#endif /* SAMC_SAMC21_FREQM_MODULE_H */

