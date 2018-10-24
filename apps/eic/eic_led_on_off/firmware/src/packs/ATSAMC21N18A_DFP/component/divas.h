/**
 * \brief Header file for SAMC/SAMC21 DIVAS
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
#ifndef SAMC_SAMC21_DIVAS_MODULE_H
#define SAMC_SAMC21_DIVAS_MODULE_H

/** \addtogroup SAMC_SAMC21 Divide and Square Root Accelerator
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_DIVAS                                 */
/* ========================================================================== */

/* -------- DIVAS_CTRLA : (DIVAS Offset: 0x00) (R/W 8) Control -------- */
#define DIVAS_CTRLA_SIGNED_Pos                (0U)                                           /**< (DIVAS_CTRLA) Signed Position */
#define DIVAS_CTRLA_SIGNED_Msk                (0x1U << DIVAS_CTRLA_SIGNED_Pos)               /**< (DIVAS_CTRLA) Signed Mask */
#define DIVAS_CTRLA_SIGNED(value)             (DIVAS_CTRLA_SIGNED_Msk & ((value) << DIVAS_CTRLA_SIGNED_Pos))
#define DIVAS_CTRLA_DLZ_Pos                   (1U)                                           /**< (DIVAS_CTRLA) Disable Leading Zero Optimization Position */
#define DIVAS_CTRLA_DLZ_Msk                   (0x1U << DIVAS_CTRLA_DLZ_Pos)                  /**< (DIVAS_CTRLA) Disable Leading Zero Optimization Mask */
#define DIVAS_CTRLA_DLZ(value)                (DIVAS_CTRLA_DLZ_Msk & ((value) << DIVAS_CTRLA_DLZ_Pos))
#define DIVAS_CTRLA_Msk                       (0x00000003UL)                                 /**< (DIVAS_CTRLA) Register Mask  */

/* -------- DIVAS_STATUS : (DIVAS Offset: 0x04) (R/W 8) Status -------- */
#define DIVAS_STATUS_BUSY_Pos                 (0U)                                           /**< (DIVAS_STATUS) DIVAS Accelerator Busy Position */
#define DIVAS_STATUS_BUSY_Msk                 (0x1U << DIVAS_STATUS_BUSY_Pos)                /**< (DIVAS_STATUS) DIVAS Accelerator Busy Mask */
#define DIVAS_STATUS_BUSY(value)              (DIVAS_STATUS_BUSY_Msk & ((value) << DIVAS_STATUS_BUSY_Pos))
#define DIVAS_STATUS_DBZ_Pos                  (1U)                                           /**< (DIVAS_STATUS) Writing a one to this bit clears DBZ to zero Position */
#define DIVAS_STATUS_DBZ_Msk                  (0x1U << DIVAS_STATUS_DBZ_Pos)                 /**< (DIVAS_STATUS) Writing a one to this bit clears DBZ to zero Mask */
#define DIVAS_STATUS_DBZ(value)               (DIVAS_STATUS_DBZ_Msk & ((value) << DIVAS_STATUS_DBZ_Pos))
#define DIVAS_STATUS_Msk                      (0x00000003UL)                                 /**< (DIVAS_STATUS) Register Mask  */

/* -------- DIVAS_DIVIDEND : (DIVAS Offset: 0x08) (R/W 32) Dividend -------- */
#define DIVAS_DIVIDEND_DIVIDEND_Pos           (0U)                                           /**< (DIVAS_DIVIDEND) DIVIDEND Position */
#define DIVAS_DIVIDEND_DIVIDEND_Msk           (0xFFFFFFFFU << DIVAS_DIVIDEND_DIVIDEND_Pos)   /**< (DIVAS_DIVIDEND) DIVIDEND Mask */
#define DIVAS_DIVIDEND_DIVIDEND(value)        (DIVAS_DIVIDEND_DIVIDEND_Msk & ((value) << DIVAS_DIVIDEND_DIVIDEND_Pos))
#define DIVAS_DIVIDEND_Msk                    (0xFFFFFFFFUL)                                 /**< (DIVAS_DIVIDEND) Register Mask  */

/* -------- DIVAS_DIVISOR : (DIVAS Offset: 0x0C) (R/W 32) Divisor -------- */
#define DIVAS_DIVISOR_DIVISOR_Pos             (0U)                                           /**< (DIVAS_DIVISOR) DIVISOR Position */
#define DIVAS_DIVISOR_DIVISOR_Msk             (0xFFFFFFFFU << DIVAS_DIVISOR_DIVISOR_Pos)     /**< (DIVAS_DIVISOR) DIVISOR Mask */
#define DIVAS_DIVISOR_DIVISOR(value)          (DIVAS_DIVISOR_DIVISOR_Msk & ((value) << DIVAS_DIVISOR_DIVISOR_Pos))
#define DIVAS_DIVISOR_Msk                     (0xFFFFFFFFUL)                                 /**< (DIVAS_DIVISOR) Register Mask  */

/* -------- DIVAS_RESULT : (DIVAS Offset: 0x10) (R/  32) Result -------- */
#define DIVAS_RESULT_RESULT_Pos               (0U)                                           /**< (DIVAS_RESULT) RESULT Position */
#define DIVAS_RESULT_RESULT_Msk               (0xFFFFFFFFU << DIVAS_RESULT_RESULT_Pos)       /**< (DIVAS_RESULT) RESULT Mask */
#define DIVAS_RESULT_RESULT(value)            (DIVAS_RESULT_RESULT_Msk & ((value) << DIVAS_RESULT_RESULT_Pos))
#define DIVAS_RESULT_Msk                      (0xFFFFFFFFUL)                                 /**< (DIVAS_RESULT) Register Mask  */

/* -------- DIVAS_REM : (DIVAS Offset: 0x14) (R/  32) Remainder -------- */
#define DIVAS_REM_REM_Pos                     (0U)                                           /**< (DIVAS_REM) REM Position */
#define DIVAS_REM_REM_Msk                     (0xFFFFFFFFU << DIVAS_REM_REM_Pos)             /**< (DIVAS_REM) REM Mask */
#define DIVAS_REM_REM(value)                  (DIVAS_REM_REM_Msk & ((value) << DIVAS_REM_REM_Pos))
#define DIVAS_REM_Msk                         (0xFFFFFFFFUL)                                 /**< (DIVAS_REM) Register Mask  */

/* -------- DIVAS_SQRNUM : (DIVAS Offset: 0x18) (R/W 32) Square Root Input -------- */
#define DIVAS_SQRNUM_SQRNUM_Pos               (0U)                                           /**< (DIVAS_SQRNUM) Square Root Input Position */
#define DIVAS_SQRNUM_SQRNUM_Msk               (0xFFFFFFFFU << DIVAS_SQRNUM_SQRNUM_Pos)       /**< (DIVAS_SQRNUM) Square Root Input Mask */
#define DIVAS_SQRNUM_SQRNUM(value)            (DIVAS_SQRNUM_SQRNUM_Msk & ((value) << DIVAS_SQRNUM_SQRNUM_Pos))
#define DIVAS_SQRNUM_Msk                      (0xFFFFFFFFUL)                                 /**< (DIVAS_SQRNUM) Register Mask  */

/** \brief DIVAS register offsets definitions */
#define DIVAS_CTRLA_OFFSET             (0x00)         /**< (DIVAS_CTRLA) Control Offset */
#define DIVAS_STATUS_OFFSET            (0x04)         /**< (DIVAS_STATUS) Status Offset */
#define DIVAS_DIVIDEND_OFFSET          (0x08)         /**< (DIVAS_DIVIDEND) Dividend Offset */
#define DIVAS_DIVISOR_OFFSET           (0x0C)         /**< (DIVAS_DIVISOR) Divisor Offset */
#define DIVAS_RESULT_OFFSET            (0x10)         /**< (DIVAS_RESULT) Result Offset */
#define DIVAS_REM_OFFSET               (0x14)         /**< (DIVAS_REM) Remainder Offset */
#define DIVAS_SQRNUM_OFFSET            (0x18)         /**< (DIVAS_SQRNUM) Square Root Input Offset */

/** \brief DIVAS register API structure */
typedef struct
{
  __IO  uint8_t                        DIVAS_CTRLA;     /**< Offset: 0x00 (R/W  8) Control */
  __I   uint8_t                        Reserved1[0x03];
  __IO  uint8_t                        DIVAS_STATUS;    /**< Offset: 0x04 (R/W  8) Status */
  __I   uint8_t                        Reserved2[0x03];
  __IO  uint32_t                       DIVAS_DIVIDEND;  /**< Offset: 0x08 (R/W  32) Dividend */
  __IO  uint32_t                       DIVAS_DIVISOR;   /**< Offset: 0x0c (R/W  32) Divisor */
  __I   uint32_t                       DIVAS_RESULT;    /**< Offset: 0x10 (R/   32) Result */
  __I   uint32_t                       DIVAS_REM;       /**< Offset: 0x14 (R/   32) Remainder */
  __IO  uint32_t                       DIVAS_SQRNUM;    /**< Offset: 0x18 (R/W  32) Square Root Input */
} divas_registers_t;
/** @}  end of Divide and Square Root Accelerator */

#endif /* SAMC_SAMC21_DIVAS_MODULE_H */

