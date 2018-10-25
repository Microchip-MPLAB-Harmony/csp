/**
 * \brief Header file for SAMC/SAMC21 RSTC
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
#ifndef SAMC_SAMC21_RSTC_MODULE_H
#define SAMC_SAMC21_RSTC_MODULE_H

/** \addtogroup SAMC_SAMC21 Reset Controller
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_RSTC                                  */
/* ========================================================================== */

/* -------- RSTC_RCAUSE : (RSTC Offset: 0x00) (R/  8) Reset Cause -------- */
#define RSTC_RCAUSE_POR_Pos                   (0U)                                           /**< (RSTC_RCAUSE) Power On Reset Position */
#define RSTC_RCAUSE_POR_Msk                   (0x1U << RSTC_RCAUSE_POR_Pos)                  /**< (RSTC_RCAUSE) Power On Reset Mask */
#define RSTC_RCAUSE_POR(value)                (RSTC_RCAUSE_POR_Msk & ((value) << RSTC_RCAUSE_POR_Pos))
#define RSTC_RCAUSE_BODCORE_Pos               (1U)                                           /**< (RSTC_RCAUSE) Brown Out CORE Detector Reset Position */
#define RSTC_RCAUSE_BODCORE_Msk               (0x1U << RSTC_RCAUSE_BODCORE_Pos)              /**< (RSTC_RCAUSE) Brown Out CORE Detector Reset Mask */
#define RSTC_RCAUSE_BODCORE(value)            (RSTC_RCAUSE_BODCORE_Msk & ((value) << RSTC_RCAUSE_BODCORE_Pos))
#define RSTC_RCAUSE_BODVDD_Pos                (2U)                                           /**< (RSTC_RCAUSE) Brown Out VDD Detector Reset Position */
#define RSTC_RCAUSE_BODVDD_Msk                (0x1U << RSTC_RCAUSE_BODVDD_Pos)               /**< (RSTC_RCAUSE) Brown Out VDD Detector Reset Mask */
#define RSTC_RCAUSE_BODVDD(value)             (RSTC_RCAUSE_BODVDD_Msk & ((value) << RSTC_RCAUSE_BODVDD_Pos))
#define RSTC_RCAUSE_EXT_Pos                   (4U)                                           /**< (RSTC_RCAUSE) External Reset Position */
#define RSTC_RCAUSE_EXT_Msk                   (0x1U << RSTC_RCAUSE_EXT_Pos)                  /**< (RSTC_RCAUSE) External Reset Mask */
#define RSTC_RCAUSE_EXT(value)                (RSTC_RCAUSE_EXT_Msk & ((value) << RSTC_RCAUSE_EXT_Pos))
#define RSTC_RCAUSE_WDT_Pos                   (5U)                                           /**< (RSTC_RCAUSE) Watchdog Reset Position */
#define RSTC_RCAUSE_WDT_Msk                   (0x1U << RSTC_RCAUSE_WDT_Pos)                  /**< (RSTC_RCAUSE) Watchdog Reset Mask */
#define RSTC_RCAUSE_WDT(value)                (RSTC_RCAUSE_WDT_Msk & ((value) << RSTC_RCAUSE_WDT_Pos))
#define RSTC_RCAUSE_SYST_Pos                  (6U)                                           /**< (RSTC_RCAUSE) System Reset Request Position */
#define RSTC_RCAUSE_SYST_Msk                  (0x1U << RSTC_RCAUSE_SYST_Pos)                 /**< (RSTC_RCAUSE) System Reset Request Mask */
#define RSTC_RCAUSE_SYST(value)               (RSTC_RCAUSE_SYST_Msk & ((value) << RSTC_RCAUSE_SYST_Pos))
#define RSTC_RCAUSE_Msk                       (0x00000077UL)                                 /**< (RSTC_RCAUSE) Register Mask  */

/** \brief RSTC register offsets definitions */
#define RSTC_RCAUSE_OFFSET             (0x00)         /**< (RSTC_RCAUSE) Reset Cause Offset */

/** \brief RSTC register API structure */
typedef struct
{
  __I   uint8_t                        RSTC_RCAUSE;     /**< Offset: 0x00 (R/   8) Reset Cause */
} rstc_registers_t;
/** @}  end of Reset Controller */

#endif /* SAMC_SAMC21_RSTC_MODULE_H */

