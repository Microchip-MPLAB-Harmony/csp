/**
 * \brief Header file for SAMG/SAMG55 SPI
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
#ifndef SAMG_SAMG55_SPI_MODULE_H
#define SAMG_SAMG55_SPI_MODULE_H

/** \addtogroup SAMG_SAMG55 Serial Peripheral Interface
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_SPI                                   */
/* ========================================================================== */

/* -------- SPI_CR : (SPI Offset: 0x00) ( /W 32) SPI Control Register -------- */
#define SPI_CR_SPIEN_Pos                      (0U)                                           /**< (SPI_CR) SPI Enable Position */
#define SPI_CR_SPIEN_Msk                      (0x1U << SPI_CR_SPIEN_Pos)                     /**< (SPI_CR) SPI Enable Mask */
#define SPI_CR_SPIEN(value)                   (SPI_CR_SPIEN_Msk & ((value) << SPI_CR_SPIEN_Pos))
#define SPI_CR_SPIDIS_Pos                     (1U)                                           /**< (SPI_CR) SPI Disable Position */
#define SPI_CR_SPIDIS_Msk                     (0x1U << SPI_CR_SPIDIS_Pos)                    /**< (SPI_CR) SPI Disable Mask */
#define SPI_CR_SPIDIS(value)                  (SPI_CR_SPIDIS_Msk & ((value) << SPI_CR_SPIDIS_Pos))
#define SPI_CR_SWRST_Pos                      (7U)                                           /**< (SPI_CR) SPI Software Reset Position */
#define SPI_CR_SWRST_Msk                      (0x1U << SPI_CR_SWRST_Pos)                     /**< (SPI_CR) SPI Software Reset Mask */
#define SPI_CR_SWRST(value)                   (SPI_CR_SWRST_Msk & ((value) << SPI_CR_SWRST_Pos))
#define SPI_CR_REQCLR_Pos                     (12U)                                          /**< (SPI_CR) Request to Clear the Comparison Trigger Position */
#define SPI_CR_REQCLR_Msk                     (0x1U << SPI_CR_REQCLR_Pos)                    /**< (SPI_CR) Request to Clear the Comparison Trigger Mask */
#define SPI_CR_REQCLR(value)                  (SPI_CR_REQCLR_Msk & ((value) << SPI_CR_REQCLR_Pos))
#define SPI_CR_LASTXFER_Pos                   (24U)                                          /**< (SPI_CR) Last Transfer Position */
#define SPI_CR_LASTXFER_Msk                   (0x1U << SPI_CR_LASTXFER_Pos)                  /**< (SPI_CR) Last Transfer Mask */
#define SPI_CR_LASTXFER(value)                (SPI_CR_LASTXFER_Msk & ((value) << SPI_CR_LASTXFER_Pos))
#define SPI_CR_Msk                            (0x01001083UL)                                 /**< (SPI_CR) Register Mask  */

/* -------- SPI_MR : (SPI Offset: 0x04) (R/W 32) SPI Mode Register -------- */
#define SPI_MR_MSTR_Pos                       (0U)                                           /**< (SPI_MR) Master/Slave Mode Position */
#define SPI_MR_MSTR_Msk                       (0x1U << SPI_MR_MSTR_Pos)                      /**< (SPI_MR) Master/Slave Mode Mask */
#define SPI_MR_MSTR(value)                    (SPI_MR_MSTR_Msk & ((value) << SPI_MR_MSTR_Pos))
#define SPI_MR_PS_Pos                         (1U)                                           /**< (SPI_MR) Peripheral Select Position */
#define SPI_MR_PS_Msk                         (0x1U << SPI_MR_PS_Pos)                        /**< (SPI_MR) Peripheral Select Mask */
#define SPI_MR_PS(value)                      (SPI_MR_PS_Msk & ((value) << SPI_MR_PS_Pos))  
#define SPI_MR_PCSDEC_Pos                     (2U)                                           /**< (SPI_MR) Chip Select Decode Position */
#define SPI_MR_PCSDEC_Msk                     (0x1U << SPI_MR_PCSDEC_Pos)                    /**< (SPI_MR) Chip Select Decode Mask */
#define SPI_MR_PCSDEC(value)                  (SPI_MR_PCSDEC_Msk & ((value) << SPI_MR_PCSDEC_Pos))
#define SPI_MR_BRSRCCLK_Pos                   (3U)                                           /**< (SPI_MR) Bit Rate Source Clock Position */
#define SPI_MR_BRSRCCLK_Msk                   (0x1U << SPI_MR_BRSRCCLK_Pos)                  /**< (SPI_MR) Bit Rate Source Clock Mask */
#define SPI_MR_BRSRCCLK(value)                (SPI_MR_BRSRCCLK_Msk & ((value) << SPI_MR_BRSRCCLK_Pos))
#define   SPI_MR_BRSRCCLK_PERIPH_CLK_Val      (0U)                                           /**< (SPI_MR) The peripheral clock is the source clock for the bit rate generation.  */
#define   SPI_MR_BRSRCCLK_PMC_PCK_Val         (1U)                                           /**< (SPI_MR) PMC PCKx is the source clock for the bit rate generation, thus the bit rate can be independent of the core/peripheral clock.  */
#define SPI_MR_BRSRCCLK_PERIPH_CLK            (SPI_MR_BRSRCCLK_PERIPH_CLK_Val << SPI_MR_BRSRCCLK_Pos) /**< (SPI_MR) The peripheral clock is the source clock for the bit rate generation. Position  */
#define SPI_MR_BRSRCCLK_PMC_PCK               (SPI_MR_BRSRCCLK_PMC_PCK_Val << SPI_MR_BRSRCCLK_Pos) /**< (SPI_MR) PMC PCKx is the source clock for the bit rate generation, thus the bit rate can be independent of the core/peripheral clock. Position  */
#define SPI_MR_MODFDIS_Pos                    (4U)                                           /**< (SPI_MR) Mode Fault Detection Position */
#define SPI_MR_MODFDIS_Msk                    (0x1U << SPI_MR_MODFDIS_Pos)                   /**< (SPI_MR) Mode Fault Detection Mask */
#define SPI_MR_MODFDIS(value)                 (SPI_MR_MODFDIS_Msk & ((value) << SPI_MR_MODFDIS_Pos))
#define SPI_MR_WDRBT_Pos                      (5U)                                           /**< (SPI_MR) Wait Data Read Before Transfer Position */
#define SPI_MR_WDRBT_Msk                      (0x1U << SPI_MR_WDRBT_Pos)                     /**< (SPI_MR) Wait Data Read Before Transfer Mask */
#define SPI_MR_WDRBT(value)                   (SPI_MR_WDRBT_Msk & ((value) << SPI_MR_WDRBT_Pos))
#define SPI_MR_LLB_Pos                        (7U)                                           /**< (SPI_MR) Local Loopback Enable Position */
#define SPI_MR_LLB_Msk                        (0x1U << SPI_MR_LLB_Pos)                       /**< (SPI_MR) Local Loopback Enable Mask */
#define SPI_MR_LLB(value)                     (SPI_MR_LLB_Msk & ((value) << SPI_MR_LLB_Pos))
#define SPI_MR_CMPMODE_Pos                    (12U)                                          /**< (SPI_MR) Comparison Mode Position */
#define SPI_MR_CMPMODE_Msk                    (0x1U << SPI_MR_CMPMODE_Pos)                   /**< (SPI_MR) Comparison Mode Mask */
#define SPI_MR_CMPMODE(value)                 (SPI_MR_CMPMODE_Msk & ((value) << SPI_MR_CMPMODE_Pos))
#define   SPI_MR_CMPMODE_FLAG_ONLY_Val        (0U)                                           /**< (SPI_MR) Any character is received and comparison function drives CMP flag.  */
#define   SPI_MR_CMPMODE_START_CONDITION_Val  (1U)                                           /**< (SPI_MR) Comparison condition must be met to start reception of all incoming characters until REQCLR is set.  */
#define SPI_MR_CMPMODE_FLAG_ONLY              (SPI_MR_CMPMODE_FLAG_ONLY_Val << SPI_MR_CMPMODE_Pos) /**< (SPI_MR) Any character is received and comparison function drives CMP flag. Position  */
#define SPI_MR_CMPMODE_START_CONDITION        (SPI_MR_CMPMODE_START_CONDITION_Val << SPI_MR_CMPMODE_Pos) /**< (SPI_MR) Comparison condition must be met to start reception of all incoming characters until REQCLR is set. Position  */
#define SPI_MR_PCS_Pos                        (16U)                                          /**< (SPI_MR) Peripheral Chip Select Position */
#define SPI_MR_PCS_Msk                        (0x3U << SPI_MR_PCS_Pos)                       /**< (SPI_MR) Peripheral Chip Select Mask */
#define SPI_MR_PCS(value)                     (SPI_MR_PCS_Msk & ((value) << SPI_MR_PCS_Pos))
#define SPI_MR_DLYBCS_Pos                     (24U)                                          /**< (SPI_MR) Delay Between Chip Selects Position */
#define SPI_MR_DLYBCS_Msk                     (0xFFU << SPI_MR_DLYBCS_Pos)                   /**< (SPI_MR) Delay Between Chip Selects Mask */
#define SPI_MR_DLYBCS(value)                  (SPI_MR_DLYBCS_Msk & ((value) << SPI_MR_DLYBCS_Pos))
#define SPI_MR_Msk                            (0xFF0310BFUL)                                 /**< (SPI_MR) Register Mask  */

/* -------- SPI_RDR : (SPI Offset: 0x08) (R/  32) SPI Receive Data Register -------- */
#define SPI_RDR_RD_Pos                        (0U)                                           /**< (SPI_RDR) Receive Data Position */
#define SPI_RDR_RD_Msk                        (0xFFFFU << SPI_RDR_RD_Pos)                    /**< (SPI_RDR) Receive Data Mask */
#define SPI_RDR_RD(value)                     (SPI_RDR_RD_Msk & ((value) << SPI_RDR_RD_Pos))
#define SPI_RDR_PCS_Pos                       (16U)                                          /**< (SPI_RDR) Peripheral Chip Select Position */
#define SPI_RDR_PCS_Msk                       (0xFU << SPI_RDR_PCS_Pos)                      /**< (SPI_RDR) Peripheral Chip Select Mask */
#define SPI_RDR_PCS(value)                    (SPI_RDR_PCS_Msk & ((value) << SPI_RDR_PCS_Pos))
#define SPI_RDR_Msk                           (0x000FFFFFUL)                                 /**< (SPI_RDR) Register Mask  */

/* -------- SPI_TDR : (SPI Offset: 0x0C) ( /W 32) SPI Transmit Data Register -------- */
#define SPI_TDR_TD_Pos                        (0U)                                           /**< (SPI_TDR) Transmit Data Position */
#define SPI_TDR_TD_Msk                        (0xFFFFU << SPI_TDR_TD_Pos)                    /**< (SPI_TDR) Transmit Data Mask */
#define SPI_TDR_TD(value)                     (SPI_TDR_TD_Msk & ((value) << SPI_TDR_TD_Pos))
#define SPI_TDR_PCS_Pos                       (16U)                                          /**< (SPI_TDR) Peripheral Chip Select Position */
#define SPI_TDR_PCS_Msk                       (0xFU << SPI_TDR_PCS_Pos)                      /**< (SPI_TDR) Peripheral Chip Select Mask */
#define SPI_TDR_PCS(value)                    (SPI_TDR_PCS_Msk & ((value) << SPI_TDR_PCS_Pos))
#define SPI_TDR_LASTXFER_Pos                  (24U)                                          /**< (SPI_TDR) Last Transfer Position */
#define SPI_TDR_LASTXFER_Msk                  (0x1U << SPI_TDR_LASTXFER_Pos)                 /**< (SPI_TDR) Last Transfer Mask */
#define SPI_TDR_LASTXFER(value)               (SPI_TDR_LASTXFER_Msk & ((value) << SPI_TDR_LASTXFER_Pos))
#define SPI_TDR_Msk                           (0x010FFFFFUL)                                 /**< (SPI_TDR) Register Mask  */

/* -------- SPI_SR : (SPI Offset: 0x10) (R/  32) SPI Status Register -------- */
#define SPI_SR_RDRF_Pos                       (0U)                                           /**< (SPI_SR) Receive Data Register Full (cleared by reading SPI_RDR) Position */
#define SPI_SR_RDRF_Msk                       (0x1U << SPI_SR_RDRF_Pos)                      /**< (SPI_SR) Receive Data Register Full (cleared by reading SPI_RDR) Mask */
#define SPI_SR_RDRF(value)                    (SPI_SR_RDRF_Msk & ((value) << SPI_SR_RDRF_Pos))
#define SPI_SR_TDRE_Pos                       (1U)                                           /**< (SPI_SR) Transmit Data Register Empty (cleared by writing SPI_TDR) Position */
#define SPI_SR_TDRE_Msk                       (0x1U << SPI_SR_TDRE_Pos)                      /**< (SPI_SR) Transmit Data Register Empty (cleared by writing SPI_TDR) Mask */
#define SPI_SR_TDRE(value)                    (SPI_SR_TDRE_Msk & ((value) << SPI_SR_TDRE_Pos))
#define SPI_SR_MODF_Pos                       (2U)                                           /**< (SPI_SR) Mode Fault Error (cleared on read) Position */
#define SPI_SR_MODF_Msk                       (0x1U << SPI_SR_MODF_Pos)                      /**< (SPI_SR) Mode Fault Error (cleared on read) Mask */
#define SPI_SR_MODF(value)                    (SPI_SR_MODF_Msk & ((value) << SPI_SR_MODF_Pos))
#define SPI_SR_OVRES_Pos                      (3U)                                           /**< (SPI_SR) Overrun Error Status (cleared on read) Position */
#define SPI_SR_OVRES_Msk                      (0x1U << SPI_SR_OVRES_Pos)                     /**< (SPI_SR) Overrun Error Status (cleared on read) Mask */
#define SPI_SR_OVRES(value)                   (SPI_SR_OVRES_Msk & ((value) << SPI_SR_OVRES_Pos))
#define SPI_SR_ENDRX_Pos                      (4U)                                           /**< (SPI_SR) End of RX buffer (cleared by writing SPI_RCR or SPI_RNCR) Position */
#define SPI_SR_ENDRX_Msk                      (0x1U << SPI_SR_ENDRX_Pos)                     /**< (SPI_SR) End of RX buffer (cleared by writing SPI_RCR or SPI_RNCR) Mask */
#define SPI_SR_ENDRX(value)                   (SPI_SR_ENDRX_Msk & ((value) << SPI_SR_ENDRX_Pos))
#define SPI_SR_ENDTX_Pos                      (5U)                                           /**< (SPI_SR) End of TX buffer (cleared by writing SPI_TCR or SPI_TNCR) Position */
#define SPI_SR_ENDTX_Msk                      (0x1U << SPI_SR_ENDTX_Pos)                     /**< (SPI_SR) End of TX buffer (cleared by writing SPI_TCR or SPI_TNCR) Mask */
#define SPI_SR_ENDTX(value)                   (SPI_SR_ENDTX_Msk & ((value) << SPI_SR_ENDTX_Pos))
#define SPI_SR_RXBUFF_Pos                     (6U)                                           /**< (SPI_SR) RX Buffer Full (cleared by writing SPI_RCR or SPI_RNCR) Position */
#define SPI_SR_RXBUFF_Msk                     (0x1U << SPI_SR_RXBUFF_Pos)                    /**< (SPI_SR) RX Buffer Full (cleared by writing SPI_RCR or SPI_RNCR) Mask */
#define SPI_SR_RXBUFF(value)                  (SPI_SR_RXBUFF_Msk & ((value) << SPI_SR_RXBUFF_Pos))
#define SPI_SR_TXBUFE_Pos                     (7U)                                           /**< (SPI_SR) TX Buffer Empty (cleared by writing SPI_TCR or SPI_TNCR) Position */
#define SPI_SR_TXBUFE_Msk                     (0x1U << SPI_SR_TXBUFE_Pos)                    /**< (SPI_SR) TX Buffer Empty (cleared by writing SPI_TCR or SPI_TNCR) Mask */
#define SPI_SR_TXBUFE(value)                  (SPI_SR_TXBUFE_Msk & ((value) << SPI_SR_TXBUFE_Pos))
#define SPI_SR_NSSR_Pos                       (8U)                                           /**< (SPI_SR) NSS Rising (cleared on read) Position */
#define SPI_SR_NSSR_Msk                       (0x1U << SPI_SR_NSSR_Pos)                      /**< (SPI_SR) NSS Rising (cleared on read) Mask */
#define SPI_SR_NSSR(value)                    (SPI_SR_NSSR_Msk & ((value) << SPI_SR_NSSR_Pos))
#define SPI_SR_TXEMPTY_Pos                    (9U)                                           /**< (SPI_SR) Transmission Registers Empty (cleared by writing SPI_TDR) Position */
#define SPI_SR_TXEMPTY_Msk                    (0x1U << SPI_SR_TXEMPTY_Pos)                   /**< (SPI_SR) Transmission Registers Empty (cleared by writing SPI_TDR) Mask */
#define SPI_SR_TXEMPTY(value)                 (SPI_SR_TXEMPTY_Msk & ((value) << SPI_SR_TXEMPTY_Pos))
#define SPI_SR_UNDES_Pos                      (10U)                                          /**< (SPI_SR) Underrun Error Status (slave mode only) (cleared on read) Position */
#define SPI_SR_UNDES_Msk                      (0x1U << SPI_SR_UNDES_Pos)                     /**< (SPI_SR) Underrun Error Status (slave mode only) (cleared on read) Mask */
#define SPI_SR_UNDES(value)                   (SPI_SR_UNDES_Msk & ((value) << SPI_SR_UNDES_Pos))
#define SPI_SR_CMP_Pos                        (11U)                                          /**< (SPI_SR) Comparison Status (cleared on read) Position */
#define SPI_SR_CMP_Msk                        (0x1U << SPI_SR_CMP_Pos)                       /**< (SPI_SR) Comparison Status (cleared on read) Mask */
#define SPI_SR_CMP(value)                     (SPI_SR_CMP_Msk & ((value) << SPI_SR_CMP_Pos))
#define SPI_SR_SPIENS_Pos                     (16U)                                          /**< (SPI_SR) SPI Enable Status Position */
#define SPI_SR_SPIENS_Msk                     (0x1U << SPI_SR_SPIENS_Pos)                    /**< (SPI_SR) SPI Enable Status Mask */
#define SPI_SR_SPIENS(value)                  (SPI_SR_SPIENS_Msk & ((value) << SPI_SR_SPIENS_Pos))
#define SPI_SR_Msk                            (0x00010FFFUL)                                 /**< (SPI_SR) Register Mask  */

/* -------- SPI_IER : (SPI Offset: 0x14) ( /W 32) SPI Interrupt Enable Register -------- */
#define SPI_IER_RDRF_Pos                      (0U)                                           /**< (SPI_IER) Receive Data Register Full Interrupt Enable Position */
#define SPI_IER_RDRF_Msk                      (0x1U << SPI_IER_RDRF_Pos)                     /**< (SPI_IER) Receive Data Register Full Interrupt Enable Mask */
#define SPI_IER_RDRF(value)                   (SPI_IER_RDRF_Msk & ((value) << SPI_IER_RDRF_Pos))
#define SPI_IER_TDRE_Pos                      (1U)                                           /**< (SPI_IER) SPI Transmit Data Register Empty Interrupt Enable Position */
#define SPI_IER_TDRE_Msk                      (0x1U << SPI_IER_TDRE_Pos)                     /**< (SPI_IER) SPI Transmit Data Register Empty Interrupt Enable Mask */
#define SPI_IER_TDRE(value)                   (SPI_IER_TDRE_Msk & ((value) << SPI_IER_TDRE_Pos))
#define SPI_IER_MODF_Pos                      (2U)                                           /**< (SPI_IER) Mode Fault Error Interrupt Enable Position */
#define SPI_IER_MODF_Msk                      (0x1U << SPI_IER_MODF_Pos)                     /**< (SPI_IER) Mode Fault Error Interrupt Enable Mask */
#define SPI_IER_MODF(value)                   (SPI_IER_MODF_Msk & ((value) << SPI_IER_MODF_Pos))
#define SPI_IER_OVRES_Pos                     (3U)                                           /**< (SPI_IER) Overrun Error Interrupt Enable Position */
#define SPI_IER_OVRES_Msk                     (0x1U << SPI_IER_OVRES_Pos)                    /**< (SPI_IER) Overrun Error Interrupt Enable Mask */
#define SPI_IER_OVRES(value)                  (SPI_IER_OVRES_Msk & ((value) << SPI_IER_OVRES_Pos))
#define SPI_IER_ENDRX_Pos                     (4U)                                           /**< (SPI_IER) End of Receive Buffer Interrupt Enable Position */
#define SPI_IER_ENDRX_Msk                     (0x1U << SPI_IER_ENDRX_Pos)                    /**< (SPI_IER) End of Receive Buffer Interrupt Enable Mask */
#define SPI_IER_ENDRX(value)                  (SPI_IER_ENDRX_Msk & ((value) << SPI_IER_ENDRX_Pos))
#define SPI_IER_ENDTX_Pos                     (5U)                                           /**< (SPI_IER) End of Transmit Buffer Interrupt Enable Position */
#define SPI_IER_ENDTX_Msk                     (0x1U << SPI_IER_ENDTX_Pos)                    /**< (SPI_IER) End of Transmit Buffer Interrupt Enable Mask */
#define SPI_IER_ENDTX(value)                  (SPI_IER_ENDTX_Msk & ((value) << SPI_IER_ENDTX_Pos))
#define SPI_IER_RXBUFF_Pos                    (6U)                                           /**< (SPI_IER) Receive Buffer Full Interrupt Enable Position */
#define SPI_IER_RXBUFF_Msk                    (0x1U << SPI_IER_RXBUFF_Pos)                   /**< (SPI_IER) Receive Buffer Full Interrupt Enable Mask */
#define SPI_IER_RXBUFF(value)                 (SPI_IER_RXBUFF_Msk & ((value) << SPI_IER_RXBUFF_Pos))
#define SPI_IER_TXBUFE_Pos                    (7U)                                           /**< (SPI_IER) Transmit Buffer Empty Interrupt Enable Position */
#define SPI_IER_TXBUFE_Msk                    (0x1U << SPI_IER_TXBUFE_Pos)                   /**< (SPI_IER) Transmit Buffer Empty Interrupt Enable Mask */
#define SPI_IER_TXBUFE(value)                 (SPI_IER_TXBUFE_Msk & ((value) << SPI_IER_TXBUFE_Pos))
#define SPI_IER_NSSR_Pos                      (8U)                                           /**< (SPI_IER) NSS Rising Interrupt Enable Position */
#define SPI_IER_NSSR_Msk                      (0x1U << SPI_IER_NSSR_Pos)                     /**< (SPI_IER) NSS Rising Interrupt Enable Mask */
#define SPI_IER_NSSR(value)                   (SPI_IER_NSSR_Msk & ((value) << SPI_IER_NSSR_Pos))
#define SPI_IER_TXEMPTY_Pos                   (9U)                                           /**< (SPI_IER) Transmission Registers Empty Enable Position */
#define SPI_IER_TXEMPTY_Msk                   (0x1U << SPI_IER_TXEMPTY_Pos)                  /**< (SPI_IER) Transmission Registers Empty Enable Mask */
#define SPI_IER_TXEMPTY(value)                (SPI_IER_TXEMPTY_Msk & ((value) << SPI_IER_TXEMPTY_Pos))
#define SPI_IER_UNDES_Pos                     (10U)                                          /**< (SPI_IER) Underrun Error Interrupt Enable Position */
#define SPI_IER_UNDES_Msk                     (0x1U << SPI_IER_UNDES_Pos)                    /**< (SPI_IER) Underrun Error Interrupt Enable Mask */
#define SPI_IER_UNDES(value)                  (SPI_IER_UNDES_Msk & ((value) << SPI_IER_UNDES_Pos))
#define SPI_IER_CMP_Pos                       (11U)                                          /**< (SPI_IER) Comparison Interrupt Enable Position */
#define SPI_IER_CMP_Msk                       (0x1U << SPI_IER_CMP_Pos)                      /**< (SPI_IER) Comparison Interrupt Enable Mask */
#define SPI_IER_CMP(value)                    (SPI_IER_CMP_Msk & ((value) << SPI_IER_CMP_Pos))
#define SPI_IER_Msk                           (0x00000FFFUL)                                 /**< (SPI_IER) Register Mask  */

/* -------- SPI_IDR : (SPI Offset: 0x18) ( /W 32) SPI Interrupt Disable Register -------- */
#define SPI_IDR_RDRF_Pos                      (0U)                                           /**< (SPI_IDR) Receive Data Register Full Interrupt Disable Position */
#define SPI_IDR_RDRF_Msk                      (0x1U << SPI_IDR_RDRF_Pos)                     /**< (SPI_IDR) Receive Data Register Full Interrupt Disable Mask */
#define SPI_IDR_RDRF(value)                   (SPI_IDR_RDRF_Msk & ((value) << SPI_IDR_RDRF_Pos))
#define SPI_IDR_TDRE_Pos                      (1U)                                           /**< (SPI_IDR) SPI Transmit Data Register Empty Interrupt Disable Position */
#define SPI_IDR_TDRE_Msk                      (0x1U << SPI_IDR_TDRE_Pos)                     /**< (SPI_IDR) SPI Transmit Data Register Empty Interrupt Disable Mask */
#define SPI_IDR_TDRE(value)                   (SPI_IDR_TDRE_Msk & ((value) << SPI_IDR_TDRE_Pos))
#define SPI_IDR_MODF_Pos                      (2U)                                           /**< (SPI_IDR) Mode Fault Error Interrupt Disable Position */
#define SPI_IDR_MODF_Msk                      (0x1U << SPI_IDR_MODF_Pos)                     /**< (SPI_IDR) Mode Fault Error Interrupt Disable Mask */
#define SPI_IDR_MODF(value)                   (SPI_IDR_MODF_Msk & ((value) << SPI_IDR_MODF_Pos))
#define SPI_IDR_OVRES_Pos                     (3U)                                           /**< (SPI_IDR) Overrun Error Interrupt Disable Position */
#define SPI_IDR_OVRES_Msk                     (0x1U << SPI_IDR_OVRES_Pos)                    /**< (SPI_IDR) Overrun Error Interrupt Disable Mask */
#define SPI_IDR_OVRES(value)                  (SPI_IDR_OVRES_Msk & ((value) << SPI_IDR_OVRES_Pos))
#define SPI_IDR_ENDRX_Pos                     (4U)                                           /**< (SPI_IDR) End of Receive Buffer Interrupt Disable Position */
#define SPI_IDR_ENDRX_Msk                     (0x1U << SPI_IDR_ENDRX_Pos)                    /**< (SPI_IDR) End of Receive Buffer Interrupt Disable Mask */
#define SPI_IDR_ENDRX(value)                  (SPI_IDR_ENDRX_Msk & ((value) << SPI_IDR_ENDRX_Pos))
#define SPI_IDR_ENDTX_Pos                     (5U)                                           /**< (SPI_IDR) End of Transmit Buffer Interrupt Disable Position */
#define SPI_IDR_ENDTX_Msk                     (0x1U << SPI_IDR_ENDTX_Pos)                    /**< (SPI_IDR) End of Transmit Buffer Interrupt Disable Mask */
#define SPI_IDR_ENDTX(value)                  (SPI_IDR_ENDTX_Msk & ((value) << SPI_IDR_ENDTX_Pos))
#define SPI_IDR_RXBUFF_Pos                    (6U)                                           /**< (SPI_IDR) Receive Buffer Full Interrupt Disable Position */
#define SPI_IDR_RXBUFF_Msk                    (0x1U << SPI_IDR_RXBUFF_Pos)                   /**< (SPI_IDR) Receive Buffer Full Interrupt Disable Mask */
#define SPI_IDR_RXBUFF(value)                 (SPI_IDR_RXBUFF_Msk & ((value) << SPI_IDR_RXBUFF_Pos))
#define SPI_IDR_TXBUFE_Pos                    (7U)                                           /**< (SPI_IDR) Transmit Buffer Empty Interrupt Disable Position */
#define SPI_IDR_TXBUFE_Msk                    (0x1U << SPI_IDR_TXBUFE_Pos)                   /**< (SPI_IDR) Transmit Buffer Empty Interrupt Disable Mask */
#define SPI_IDR_TXBUFE(value)                 (SPI_IDR_TXBUFE_Msk & ((value) << SPI_IDR_TXBUFE_Pos))
#define SPI_IDR_NSSR_Pos                      (8U)                                           /**< (SPI_IDR) NSS Rising Interrupt Disable Position */
#define SPI_IDR_NSSR_Msk                      (0x1U << SPI_IDR_NSSR_Pos)                     /**< (SPI_IDR) NSS Rising Interrupt Disable Mask */
#define SPI_IDR_NSSR(value)                   (SPI_IDR_NSSR_Msk & ((value) << SPI_IDR_NSSR_Pos))
#define SPI_IDR_TXEMPTY_Pos                   (9U)                                           /**< (SPI_IDR) Transmission Registers Empty Disable Position */
#define SPI_IDR_TXEMPTY_Msk                   (0x1U << SPI_IDR_TXEMPTY_Pos)                  /**< (SPI_IDR) Transmission Registers Empty Disable Mask */
#define SPI_IDR_TXEMPTY(value)                (SPI_IDR_TXEMPTY_Msk & ((value) << SPI_IDR_TXEMPTY_Pos))
#define SPI_IDR_UNDES_Pos                     (10U)                                          /**< (SPI_IDR) Underrun Error Interrupt Disable Position */
#define SPI_IDR_UNDES_Msk                     (0x1U << SPI_IDR_UNDES_Pos)                    /**< (SPI_IDR) Underrun Error Interrupt Disable Mask */
#define SPI_IDR_UNDES(value)                  (SPI_IDR_UNDES_Msk & ((value) << SPI_IDR_UNDES_Pos))
#define SPI_IDR_CMP_Pos                       (11U)                                          /**< (SPI_IDR) Comparison Interrupt Disable Position */
#define SPI_IDR_CMP_Msk                       (0x1U << SPI_IDR_CMP_Pos)                      /**< (SPI_IDR) Comparison Interrupt Disable Mask */
#define SPI_IDR_CMP(value)                    (SPI_IDR_CMP_Msk & ((value) << SPI_IDR_CMP_Pos))
#define SPI_IDR_Msk                           (0x00000FFFUL)                                 /**< (SPI_IDR) Register Mask  */

/* -------- SPI_IMR : (SPI Offset: 0x1C) (R/  32) SPI Interrupt Mask Register -------- */
#define SPI_IMR_RDRF_Pos                      (0U)                                           /**< (SPI_IMR) Receive Data Register Full Interrupt Mask Position */
#define SPI_IMR_RDRF_Msk                      (0x1U << SPI_IMR_RDRF_Pos)                     /**< (SPI_IMR) Receive Data Register Full Interrupt Mask Mask */
#define SPI_IMR_RDRF(value)                   (SPI_IMR_RDRF_Msk & ((value) << SPI_IMR_RDRF_Pos))
#define SPI_IMR_TDRE_Pos                      (1U)                                           /**< (SPI_IMR) SPI Transmit Data Register Empty Interrupt Mask Position */
#define SPI_IMR_TDRE_Msk                      (0x1U << SPI_IMR_TDRE_Pos)                     /**< (SPI_IMR) SPI Transmit Data Register Empty Interrupt Mask Mask */
#define SPI_IMR_TDRE(value)                   (SPI_IMR_TDRE_Msk & ((value) << SPI_IMR_TDRE_Pos))
#define SPI_IMR_MODF_Pos                      (2U)                                           /**< (SPI_IMR) Mode Fault Error Interrupt Mask Position */
#define SPI_IMR_MODF_Msk                      (0x1U << SPI_IMR_MODF_Pos)                     /**< (SPI_IMR) Mode Fault Error Interrupt Mask Mask */
#define SPI_IMR_MODF(value)                   (SPI_IMR_MODF_Msk & ((value) << SPI_IMR_MODF_Pos))
#define SPI_IMR_OVRES_Pos                     (3U)                                           /**< (SPI_IMR) Overrun Error Interrupt Mask Position */
#define SPI_IMR_OVRES_Msk                     (0x1U << SPI_IMR_OVRES_Pos)                    /**< (SPI_IMR) Overrun Error Interrupt Mask Mask */
#define SPI_IMR_OVRES(value)                  (SPI_IMR_OVRES_Msk & ((value) << SPI_IMR_OVRES_Pos))
#define SPI_IMR_ENDRX_Pos                     (4U)                                           /**< (SPI_IMR) End of Receive Buffer Interrupt Mask Position */
#define SPI_IMR_ENDRX_Msk                     (0x1U << SPI_IMR_ENDRX_Pos)                    /**< (SPI_IMR) End of Receive Buffer Interrupt Mask Mask */
#define SPI_IMR_ENDRX(value)                  (SPI_IMR_ENDRX_Msk & ((value) << SPI_IMR_ENDRX_Pos))
#define SPI_IMR_ENDTX_Pos                     (5U)                                           /**< (SPI_IMR) End of Transmit Buffer Interrupt Mask Position */
#define SPI_IMR_ENDTX_Msk                     (0x1U << SPI_IMR_ENDTX_Pos)                    /**< (SPI_IMR) End of Transmit Buffer Interrupt Mask Mask */
#define SPI_IMR_ENDTX(value)                  (SPI_IMR_ENDTX_Msk & ((value) << SPI_IMR_ENDTX_Pos))
#define SPI_IMR_RXBUFF_Pos                    (6U)                                           /**< (SPI_IMR) Receive Buffer Full Interrupt Mask Position */
#define SPI_IMR_RXBUFF_Msk                    (0x1U << SPI_IMR_RXBUFF_Pos)                   /**< (SPI_IMR) Receive Buffer Full Interrupt Mask Mask */
#define SPI_IMR_RXBUFF(value)                 (SPI_IMR_RXBUFF_Msk & ((value) << SPI_IMR_RXBUFF_Pos))
#define SPI_IMR_TXBUFE_Pos                    (7U)                                           /**< (SPI_IMR) Transmit Buffer Empty Interrupt Mask Position */
#define SPI_IMR_TXBUFE_Msk                    (0x1U << SPI_IMR_TXBUFE_Pos)                   /**< (SPI_IMR) Transmit Buffer Empty Interrupt Mask Mask */
#define SPI_IMR_TXBUFE(value)                 (SPI_IMR_TXBUFE_Msk & ((value) << SPI_IMR_TXBUFE_Pos))
#define SPI_IMR_NSSR_Pos                      (8U)                                           /**< (SPI_IMR) NSS Rising Interrupt Mask Position */
#define SPI_IMR_NSSR_Msk                      (0x1U << SPI_IMR_NSSR_Pos)                     /**< (SPI_IMR) NSS Rising Interrupt Mask Mask */
#define SPI_IMR_NSSR(value)                   (SPI_IMR_NSSR_Msk & ((value) << SPI_IMR_NSSR_Pos))
#define SPI_IMR_TXEMPTY_Pos                   (9U)                                           /**< (SPI_IMR) Transmission Registers Empty Mask Position */
#define SPI_IMR_TXEMPTY_Msk                   (0x1U << SPI_IMR_TXEMPTY_Pos)                  /**< (SPI_IMR) Transmission Registers Empty Mask Mask */
#define SPI_IMR_TXEMPTY(value)                (SPI_IMR_TXEMPTY_Msk & ((value) << SPI_IMR_TXEMPTY_Pos))
#define SPI_IMR_UNDES_Pos                     (10U)                                          /**< (SPI_IMR) Underrun Error Interrupt Mask Position */
#define SPI_IMR_UNDES_Msk                     (0x1U << SPI_IMR_UNDES_Pos)                    /**< (SPI_IMR) Underrun Error Interrupt Mask Mask */
#define SPI_IMR_UNDES(value)                  (SPI_IMR_UNDES_Msk & ((value) << SPI_IMR_UNDES_Pos))
#define SPI_IMR_CMP_Pos                       (11U)                                          /**< (SPI_IMR) Comparison Interrupt Mask Position */
#define SPI_IMR_CMP_Msk                       (0x1U << SPI_IMR_CMP_Pos)                      /**< (SPI_IMR) Comparison Interrupt Mask Mask */
#define SPI_IMR_CMP(value)                    (SPI_IMR_CMP_Msk & ((value) << SPI_IMR_CMP_Pos))
#define SPI_IMR_Msk                           (0x00000FFFUL)                                 /**< (SPI_IMR) Register Mask  */

/* -------- SPI_CSR : (SPI Offset: 0x30) (R/W 32) SPI Chip Select Register 0 -------- */
#define SPI_CSR_CPOL_Pos                      (0U)                                           /**< (SPI_CSR) Clock Polarity Position */
#define SPI_CSR_CPOL_Msk                      (0x1U << SPI_CSR_CPOL_Pos)                     /**< (SPI_CSR) Clock Polarity Mask */
#define SPI_CSR_CPOL(value)                   (SPI_CSR_CPOL_Msk & ((value) << SPI_CSR_CPOL_Pos))
#define SPI_CSR_NCPHA_Pos                     (1U)                                           /**< (SPI_CSR) Clock Phase Position */
#define SPI_CSR_NCPHA_Msk                     (0x1U << SPI_CSR_NCPHA_Pos)                    /**< (SPI_CSR) Clock Phase Mask */
#define SPI_CSR_NCPHA(value)                  (SPI_CSR_NCPHA_Msk & ((value) << SPI_CSR_NCPHA_Pos))
#define SPI_CSR_CSNAAT_Pos                    (2U)                                           /**< (SPI_CSR) Chip Select Not Active After Transfer (Ignored if CSAAT = 1) Position */
#define SPI_CSR_CSNAAT_Msk                    (0x1U << SPI_CSR_CSNAAT_Pos)                   /**< (SPI_CSR) Chip Select Not Active After Transfer (Ignored if CSAAT = 1) Mask */
#define SPI_CSR_CSNAAT(value)                 (SPI_CSR_CSNAAT_Msk & ((value) << SPI_CSR_CSNAAT_Pos))
#define SPI_CSR_CSAAT_Pos                     (3U)                                           /**< (SPI_CSR) Chip Select Active After Transfer Position */
#define SPI_CSR_CSAAT_Msk                     (0x1U << SPI_CSR_CSAAT_Pos)                    /**< (SPI_CSR) Chip Select Active After Transfer Mask */
#define SPI_CSR_CSAAT(value)                  (SPI_CSR_CSAAT_Msk & ((value) << SPI_CSR_CSAAT_Pos))
#define SPI_CSR_BITS_Pos                      (4U)                                           /**< (SPI_CSR) Bits Per Transfer Position */
#define SPI_CSR_BITS_Msk                      (0xFU << SPI_CSR_BITS_Pos)                     /**< (SPI_CSR) Bits Per Transfer Mask */
#define SPI_CSR_BITS(value)                   (SPI_CSR_BITS_Msk & ((value) << SPI_CSR_BITS_Pos))
#define   SPI_CSR_BITS_8_BIT_Val              (0U)                                           /**< (SPI_CSR) 8 bits for transfer  */
#define   SPI_CSR_BITS_9_BIT_Val              (1U)                                           /**< (SPI_CSR) 9 bits for transfer  */
#define   SPI_CSR_BITS_10_BIT_Val             (2U)                                           /**< (SPI_CSR) 10 bits for transfer  */
#define   SPI_CSR_BITS_11_BIT_Val             (3U)                                           /**< (SPI_CSR) 11 bits for transfer  */
#define   SPI_CSR_BITS_12_BIT_Val             (4U)                                           /**< (SPI_CSR) 12 bits for transfer  */
#define   SPI_CSR_BITS_13_BIT_Val             (5U)                                           /**< (SPI_CSR) 13 bits for transfer  */
#define   SPI_CSR_BITS_14_BIT_Val             (6U)                                           /**< (SPI_CSR) 14 bits for transfer  */
#define   SPI_CSR_BITS_15_BIT_Val             (7U)                                           /**< (SPI_CSR) 15 bits for transfer  */
#define   SPI_CSR_BITS_16_BIT_Val             (8U)                                           /**< (SPI_CSR) 16 bits for transfer  */
#define SPI_CSR_BITS_8_BIT                    (SPI_CSR_BITS_8_BIT_Val << SPI_CSR_BITS_Pos)   /**< (SPI_CSR) 8 bits for transfer Position  */
#define SPI_CSR_BITS_9_BIT                    (SPI_CSR_BITS_9_BIT_Val << SPI_CSR_BITS_Pos)   /**< (SPI_CSR) 9 bits for transfer Position  */
#define SPI_CSR_BITS_10_BIT                   (SPI_CSR_BITS_10_BIT_Val << SPI_CSR_BITS_Pos)  /**< (SPI_CSR) 10 bits for transfer Position  */
#define SPI_CSR_BITS_11_BIT                   (SPI_CSR_BITS_11_BIT_Val << SPI_CSR_BITS_Pos)  /**< (SPI_CSR) 11 bits for transfer Position  */
#define SPI_CSR_BITS_12_BIT                   (SPI_CSR_BITS_12_BIT_Val << SPI_CSR_BITS_Pos)  /**< (SPI_CSR) 12 bits for transfer Position  */
#define SPI_CSR_BITS_13_BIT                   (SPI_CSR_BITS_13_BIT_Val << SPI_CSR_BITS_Pos)  /**< (SPI_CSR) 13 bits for transfer Position  */
#define SPI_CSR_BITS_14_BIT                   (SPI_CSR_BITS_14_BIT_Val << SPI_CSR_BITS_Pos)  /**< (SPI_CSR) 14 bits for transfer Position  */
#define SPI_CSR_BITS_15_BIT                   (SPI_CSR_BITS_15_BIT_Val << SPI_CSR_BITS_Pos)  /**< (SPI_CSR) 15 bits for transfer Position  */
#define SPI_CSR_BITS_16_BIT                   (SPI_CSR_BITS_16_BIT_Val << SPI_CSR_BITS_Pos)  /**< (SPI_CSR) 16 bits for transfer Position  */
#define SPI_CSR_SCBR_Pos                      (8U)                                           /**< (SPI_CSR) Serial Clock Bit Rate Position */
#define SPI_CSR_SCBR_Msk                      (0xFFU << SPI_CSR_SCBR_Pos)                    /**< (SPI_CSR) Serial Clock Bit Rate Mask */
#define SPI_CSR_SCBR(value)                   (SPI_CSR_SCBR_Msk & ((value) << SPI_CSR_SCBR_Pos))
#define SPI_CSR_DLYBS_Pos                     (16U)                                          /**< (SPI_CSR) Delay Before SPCK Position */
#define SPI_CSR_DLYBS_Msk                     (0xFFU << SPI_CSR_DLYBS_Pos)                   /**< (SPI_CSR) Delay Before SPCK Mask */
#define SPI_CSR_DLYBS(value)                  (SPI_CSR_DLYBS_Msk & ((value) << SPI_CSR_DLYBS_Pos))
#define SPI_CSR_DLYBCT_Pos                    (24U)                                          /**< (SPI_CSR) Delay Between Consecutive Transfers Position */
#define SPI_CSR_DLYBCT_Msk                    (0xFFU << SPI_CSR_DLYBCT_Pos)                  /**< (SPI_CSR) Delay Between Consecutive Transfers Mask */
#define SPI_CSR_DLYBCT(value)                 (SPI_CSR_DLYBCT_Msk & ((value) << SPI_CSR_DLYBCT_Pos))
#define SPI_CSR_Msk                           (0xFFFFFFFFUL)                                 /**< (SPI_CSR) Register Mask  */

/* -------- SPI_CMPR : (SPI Offset: 0x48) (R/W 32) SPI Comparison Register -------- */
#define SPI_CMPR_VAL1_Pos                     (0U)                                           /**< (SPI_CMPR) First Comparison Value for Received Character Position */
#define SPI_CMPR_VAL1_Msk                     (0xFFFFU << SPI_CMPR_VAL1_Pos)                 /**< (SPI_CMPR) First Comparison Value for Received Character Mask */
#define SPI_CMPR_VAL1(value)                  (SPI_CMPR_VAL1_Msk & ((value) << SPI_CMPR_VAL1_Pos))
#define SPI_CMPR_VAL2_Pos                     (16U)                                          /**< (SPI_CMPR) Second Comparison Value for Received Character Position */
#define SPI_CMPR_VAL2_Msk                     (0xFFFFU << SPI_CMPR_VAL2_Pos)                 /**< (SPI_CMPR) Second Comparison Value for Received Character Mask */
#define SPI_CMPR_VAL2(value)                  (SPI_CMPR_VAL2_Msk & ((value) << SPI_CMPR_VAL2_Pos))
#define SPI_CMPR_Msk                          (0xFFFFFFFFUL)                                 /**< (SPI_CMPR) Register Mask  */

/* -------- SPI_WPMR : (SPI Offset: 0xE4) (R/W 32) SPI Write Protection Mode Register -------- */
#define SPI_WPMR_WPEN_Pos                     (0U)                                           /**< (SPI_WPMR) Write Protection Enable Position */
#define SPI_WPMR_WPEN_Msk                     (0x1U << SPI_WPMR_WPEN_Pos)                    /**< (SPI_WPMR) Write Protection Enable Mask */
#define SPI_WPMR_WPEN(value)                  (SPI_WPMR_WPEN_Msk & ((value) << SPI_WPMR_WPEN_Pos))
#define SPI_WPMR_WPKEY_Pos                    (8U)                                           /**< (SPI_WPMR) Write Protect Key Position */
#define SPI_WPMR_WPKEY_Msk                    (0xFFFFFFU << SPI_WPMR_WPKEY_Pos)              /**< (SPI_WPMR) Write Protect Key Mask */
#define SPI_WPMR_WPKEY(value)                 (SPI_WPMR_WPKEY_Msk & ((value) << SPI_WPMR_WPKEY_Pos))
#define   SPI_WPMR_WPKEY_PASSWD_Val           (5460041U)                                     /**< (SPI_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0  */
#define SPI_WPMR_WPKEY_PASSWD                 (SPI_WPMR_WPKEY_PASSWD_Val << SPI_WPMR_WPKEY_Pos) /**< (SPI_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0 Position  */
#define SPI_WPMR_Msk                          (0xFFFFFF01UL)                                 /**< (SPI_WPMR) Register Mask  */

/* -------- SPI_WPSR : (SPI Offset: 0xE8) (R/  32) SPI Write Protection Status Register -------- */
#define SPI_WPSR_WPVS_Pos                     (0U)                                           /**< (SPI_WPSR) Write Protection Violation Status Position */
#define SPI_WPSR_WPVS_Msk                     (0x1U << SPI_WPSR_WPVS_Pos)                    /**< (SPI_WPSR) Write Protection Violation Status Mask */
#define SPI_WPSR_WPVS(value)                  (SPI_WPSR_WPVS_Msk & ((value) << SPI_WPSR_WPVS_Pos))
#define SPI_WPSR_WPVSRC_Pos                   (8U)                                           /**< (SPI_WPSR) Write Protection Violation Source Position */
#define SPI_WPSR_WPVSRC_Msk                   (0xFFU << SPI_WPSR_WPVSRC_Pos)                 /**< (SPI_WPSR) Write Protection Violation Source Mask */
#define SPI_WPSR_WPVSRC(value)                (SPI_WPSR_WPVSRC_Msk & ((value) << SPI_WPSR_WPVSRC_Pos))
#define SPI_WPSR_Msk                          (0x0000FF01UL)                                 /**< (SPI_WPSR) Register Mask  */

/* -------- SPI_RPR : (SPI Offset: 0x100) (R/W 32) Receive Pointer Register -------- */
#define SPI_RPR_RXPTR_Pos                     (0U)                                           /**< (SPI_RPR) Receive Pointer Register Position */
#define SPI_RPR_RXPTR_Msk                     (0xFFFFFFFFU << SPI_RPR_RXPTR_Pos)             /**< (SPI_RPR) Receive Pointer Register Mask */
#define SPI_RPR_RXPTR(value)                  (SPI_RPR_RXPTR_Msk & ((value) << SPI_RPR_RXPTR_Pos))
#define SPI_RPR_Msk                           (0xFFFFFFFFUL)                                 /**< (SPI_RPR) Register Mask  */

/* -------- SPI_RCR : (SPI Offset: 0x104) (R/W 32) Receive Counter Register -------- */
#define SPI_RCR_RXCTR_Pos                     (0U)                                           /**< (SPI_RCR) Receive Counter Register Position */
#define SPI_RCR_RXCTR_Msk                     (0xFFFFU << SPI_RCR_RXCTR_Pos)                 /**< (SPI_RCR) Receive Counter Register Mask */
#define SPI_RCR_RXCTR(value)                  (SPI_RCR_RXCTR_Msk & ((value) << SPI_RCR_RXCTR_Pos))
#define SPI_RCR_Msk                           (0x0000FFFFUL)                                 /**< (SPI_RCR) Register Mask  */

/* -------- SPI_TPR : (SPI Offset: 0x108) (R/W 32) Transmit Pointer Register -------- */
#define SPI_TPR_TXPTR_Pos                     (0U)                                           /**< (SPI_TPR) Transmit Counter Register Position */
#define SPI_TPR_TXPTR_Msk                     (0xFFFFFFFFU << SPI_TPR_TXPTR_Pos)             /**< (SPI_TPR) Transmit Counter Register Mask */
#define SPI_TPR_TXPTR(value)                  (SPI_TPR_TXPTR_Msk & ((value) << SPI_TPR_TXPTR_Pos))
#define SPI_TPR_Msk                           (0xFFFFFFFFUL)                                 /**< (SPI_TPR) Register Mask  */

/* -------- SPI_TCR : (SPI Offset: 0x10C) (R/W 32) Transmit Counter Register -------- */
#define SPI_TCR_TXCTR_Pos                     (0U)                                           /**< (SPI_TCR) Transmit Counter Register Position */
#define SPI_TCR_TXCTR_Msk                     (0xFFFFU << SPI_TCR_TXCTR_Pos)                 /**< (SPI_TCR) Transmit Counter Register Mask */
#define SPI_TCR_TXCTR(value)                  (SPI_TCR_TXCTR_Msk & ((value) << SPI_TCR_TXCTR_Pos))
#define SPI_TCR_Msk                           (0x0000FFFFUL)                                 /**< (SPI_TCR) Register Mask  */

/* -------- SPI_RNPR : (SPI Offset: 0x110) (R/W 32) Receive Next Pointer Register -------- */
#define SPI_RNPR_RXNPTR_Pos                   (0U)                                           /**< (SPI_RNPR) Receive Next Pointer Position */
#define SPI_RNPR_RXNPTR_Msk                   (0xFFFFFFFFU << SPI_RNPR_RXNPTR_Pos)           /**< (SPI_RNPR) Receive Next Pointer Mask */
#define SPI_RNPR_RXNPTR(value)                (SPI_RNPR_RXNPTR_Msk & ((value) << SPI_RNPR_RXNPTR_Pos))
#define SPI_RNPR_Msk                          (0xFFFFFFFFUL)                                 /**< (SPI_RNPR) Register Mask  */

/* -------- SPI_RNCR : (SPI Offset: 0x114) (R/W 32) Receive Next Counter Register -------- */
#define SPI_RNCR_RXNCTR_Pos                   (0U)                                           /**< (SPI_RNCR) Receive Next Counter Position */
#define SPI_RNCR_RXNCTR_Msk                   (0xFFFFU << SPI_RNCR_RXNCTR_Pos)               /**< (SPI_RNCR) Receive Next Counter Mask */
#define SPI_RNCR_RXNCTR(value)                (SPI_RNCR_RXNCTR_Msk & ((value) << SPI_RNCR_RXNCTR_Pos))
#define SPI_RNCR_Msk                          (0x0000FFFFUL)                                 /**< (SPI_RNCR) Register Mask  */

/* -------- SPI_TNPR : (SPI Offset: 0x118) (R/W 32) Transmit Next Pointer Register -------- */
#define SPI_TNPR_TXNPTR_Pos                   (0U)                                           /**< (SPI_TNPR) Transmit Next Pointer Position */
#define SPI_TNPR_TXNPTR_Msk                   (0xFFFFFFFFU << SPI_TNPR_TXNPTR_Pos)           /**< (SPI_TNPR) Transmit Next Pointer Mask */
#define SPI_TNPR_TXNPTR(value)                (SPI_TNPR_TXNPTR_Msk & ((value) << SPI_TNPR_TXNPTR_Pos))
#define SPI_TNPR_Msk                          (0xFFFFFFFFUL)                                 /**< (SPI_TNPR) Register Mask  */

/* -------- SPI_TNCR : (SPI Offset: 0x11C) (R/W 32) Transmit Next Counter Register -------- */
#define SPI_TNCR_TXNCTR_Pos                   (0U)                                           /**< (SPI_TNCR) Transmit Counter Next Position */
#define SPI_TNCR_TXNCTR_Msk                   (0xFFFFU << SPI_TNCR_TXNCTR_Pos)               /**< (SPI_TNCR) Transmit Counter Next Mask */
#define SPI_TNCR_TXNCTR(value)                (SPI_TNCR_TXNCTR_Msk & ((value) << SPI_TNCR_TXNCTR_Pos))
#define SPI_TNCR_Msk                          (0x0000FFFFUL)                                 /**< (SPI_TNCR) Register Mask  */

/* -------- SPI_PTCR : (SPI Offset: 0x120) ( /W 32) Transfer Control Register -------- */
#define SPI_PTCR_RXTEN_Pos                    (0U)                                           /**< (SPI_PTCR) Receiver Transfer Enable Position */
#define SPI_PTCR_RXTEN_Msk                    (0x1U << SPI_PTCR_RXTEN_Pos)                   /**< (SPI_PTCR) Receiver Transfer Enable Mask */
#define SPI_PTCR_RXTEN(value)                 (SPI_PTCR_RXTEN_Msk & ((value) << SPI_PTCR_RXTEN_Pos))
#define SPI_PTCR_RXTDIS_Pos                   (1U)                                           /**< (SPI_PTCR) Receiver Transfer Disable Position */
#define SPI_PTCR_RXTDIS_Msk                   (0x1U << SPI_PTCR_RXTDIS_Pos)                  /**< (SPI_PTCR) Receiver Transfer Disable Mask */
#define SPI_PTCR_RXTDIS(value)                (SPI_PTCR_RXTDIS_Msk & ((value) << SPI_PTCR_RXTDIS_Pos))
#define SPI_PTCR_TXTEN_Pos                    (8U)                                           /**< (SPI_PTCR) Transmitter Transfer Enable Position */
#define SPI_PTCR_TXTEN_Msk                    (0x1U << SPI_PTCR_TXTEN_Pos)                   /**< (SPI_PTCR) Transmitter Transfer Enable Mask */
#define SPI_PTCR_TXTEN(value)                 (SPI_PTCR_TXTEN_Msk & ((value) << SPI_PTCR_TXTEN_Pos))
#define SPI_PTCR_TXTDIS_Pos                   (9U)                                           /**< (SPI_PTCR) Transmitter Transfer Disable Position */
#define SPI_PTCR_TXTDIS_Msk                   (0x1U << SPI_PTCR_TXTDIS_Pos)                  /**< (SPI_PTCR) Transmitter Transfer Disable Mask */
#define SPI_PTCR_TXTDIS(value)                (SPI_PTCR_TXTDIS_Msk & ((value) << SPI_PTCR_TXTDIS_Pos))
#define SPI_PTCR_RXCBEN_Pos                   (16U)                                          /**< (SPI_PTCR) Receiver Circular Buffer Enable Position */
#define SPI_PTCR_RXCBEN_Msk                   (0x1U << SPI_PTCR_RXCBEN_Pos)                  /**< (SPI_PTCR) Receiver Circular Buffer Enable Mask */
#define SPI_PTCR_RXCBEN(value)                (SPI_PTCR_RXCBEN_Msk & ((value) << SPI_PTCR_RXCBEN_Pos))
#define SPI_PTCR_RXCBDIS_Pos                  (17U)                                          /**< (SPI_PTCR) Receiver Circular Buffer Disable Position */
#define SPI_PTCR_RXCBDIS_Msk                  (0x1U << SPI_PTCR_RXCBDIS_Pos)                 /**< (SPI_PTCR) Receiver Circular Buffer Disable Mask */
#define SPI_PTCR_RXCBDIS(value)               (SPI_PTCR_RXCBDIS_Msk & ((value) << SPI_PTCR_RXCBDIS_Pos))
#define SPI_PTCR_TXCBEN_Pos                   (18U)                                          /**< (SPI_PTCR) Transmitter Circular Buffer Enable Position */
#define SPI_PTCR_TXCBEN_Msk                   (0x1U << SPI_PTCR_TXCBEN_Pos)                  /**< (SPI_PTCR) Transmitter Circular Buffer Enable Mask */
#define SPI_PTCR_TXCBEN(value)                (SPI_PTCR_TXCBEN_Msk & ((value) << SPI_PTCR_TXCBEN_Pos))
#define SPI_PTCR_TXCBDIS_Pos                  (19U)                                          /**< (SPI_PTCR) Transmitter Circular Buffer Disable Position */
#define SPI_PTCR_TXCBDIS_Msk                  (0x1U << SPI_PTCR_TXCBDIS_Pos)                 /**< (SPI_PTCR) Transmitter Circular Buffer Disable Mask */
#define SPI_PTCR_TXCBDIS(value)               (SPI_PTCR_TXCBDIS_Msk & ((value) << SPI_PTCR_TXCBDIS_Pos))
#define SPI_PTCR_ERRCLR_Pos                   (24U)                                          /**< (SPI_PTCR) Transfer Bus Error Clear Position */
#define SPI_PTCR_ERRCLR_Msk                   (0x1U << SPI_PTCR_ERRCLR_Pos)                  /**< (SPI_PTCR) Transfer Bus Error Clear Mask */
#define SPI_PTCR_ERRCLR(value)                (SPI_PTCR_ERRCLR_Msk & ((value) << SPI_PTCR_ERRCLR_Pos))
#define SPI_PTCR_Msk                          (0x010F0303UL)                                 /**< (SPI_PTCR) Register Mask  */

/* -------- SPI_PTSR : (SPI Offset: 0x124) (R/  32) Transfer Status Register -------- */
#define SPI_PTSR_RXTEN_Pos                    (0U)                                           /**< (SPI_PTSR) Receiver Transfer Enable Position */
#define SPI_PTSR_RXTEN_Msk                    (0x1U << SPI_PTSR_RXTEN_Pos)                   /**< (SPI_PTSR) Receiver Transfer Enable Mask */
#define SPI_PTSR_RXTEN(value)                 (SPI_PTSR_RXTEN_Msk & ((value) << SPI_PTSR_RXTEN_Pos))
#define SPI_PTSR_TXTEN_Pos                    (8U)                                           /**< (SPI_PTSR) Transmitter Transfer Enable Position */
#define SPI_PTSR_TXTEN_Msk                    (0x1U << SPI_PTSR_TXTEN_Pos)                   /**< (SPI_PTSR) Transmitter Transfer Enable Mask */
#define SPI_PTSR_TXTEN(value)                 (SPI_PTSR_TXTEN_Msk & ((value) << SPI_PTSR_TXTEN_Pos))
#define SPI_PTSR_RXCBEN_Pos                   (16U)                                          /**< (SPI_PTSR) Receiver Circular Buffer Enable Position */
#define SPI_PTSR_RXCBEN_Msk                   (0x1U << SPI_PTSR_RXCBEN_Pos)                  /**< (SPI_PTSR) Receiver Circular Buffer Enable Mask */
#define SPI_PTSR_RXCBEN(value)                (SPI_PTSR_RXCBEN_Msk & ((value) << SPI_PTSR_RXCBEN_Pos))
#define SPI_PTSR_TXCBEN_Pos                   (18U)                                          /**< (SPI_PTSR) Transmitter Circular Buffer Enable Position */
#define SPI_PTSR_TXCBEN_Msk                   (0x1U << SPI_PTSR_TXCBEN_Pos)                  /**< (SPI_PTSR) Transmitter Circular Buffer Enable Mask */
#define SPI_PTSR_TXCBEN(value)                (SPI_PTSR_TXCBEN_Msk & ((value) << SPI_PTSR_TXCBEN_Pos))
#define SPI_PTSR_ERR_Pos                      (24U)                                          /**< (SPI_PTSR) Transfer Bus Error Position */
#define SPI_PTSR_ERR_Msk                      (0x1U << SPI_PTSR_ERR_Pos)                     /**< (SPI_PTSR) Transfer Bus Error Mask */
#define SPI_PTSR_ERR(value)                   (SPI_PTSR_ERR_Msk & ((value) << SPI_PTSR_ERR_Pos))
#define SPI_PTSR_Msk                          (0x01050101UL)                                 /**< (SPI_PTSR) Register Mask  */

/** \brief SPI register offsets definitions */
#define SPI_CR_OFFSET                  (0x00)         /**< (SPI_CR) SPI Control Register Offset */
#define SPI_MR_OFFSET                  (0x04)         /**< (SPI_MR) SPI Mode Register Offset */
#define SPI_RDR_OFFSET                 (0x08)         /**< (SPI_RDR) SPI Receive Data Register Offset */
#define SPI_TDR_OFFSET                 (0x0C)         /**< (SPI_TDR) SPI Transmit Data Register Offset */
#define SPI_SR_OFFSET                  (0x10)         /**< (SPI_SR) SPI Status Register Offset */
#define SPI_IER_OFFSET                 (0x14)         /**< (SPI_IER) SPI Interrupt Enable Register Offset */
#define SPI_IDR_OFFSET                 (0x18)         /**< (SPI_IDR) SPI Interrupt Disable Register Offset */
#define SPI_IMR_OFFSET                 (0x1C)         /**< (SPI_IMR) SPI Interrupt Mask Register Offset */
#define SPI_CSR_OFFSET                 (0x30)         /**< (SPI_CSR) SPI Chip Select Register 0 Offset */
#define SPI_CMPR_OFFSET                (0x48)         /**< (SPI_CMPR) SPI Comparison Register Offset */
#define SPI_WPMR_OFFSET                (0xE4)         /**< (SPI_WPMR) SPI Write Protection Mode Register Offset */
#define SPI_WPSR_OFFSET                (0xE8)         /**< (SPI_WPSR) SPI Write Protection Status Register Offset */
#define SPI_RPR_OFFSET                 (0x100)        /**< (SPI_RPR) Receive Pointer Register Offset */
#define SPI_RCR_OFFSET                 (0x104)        /**< (SPI_RCR) Receive Counter Register Offset */
#define SPI_TPR_OFFSET                 (0x108)        /**< (SPI_TPR) Transmit Pointer Register Offset */
#define SPI_TCR_OFFSET                 (0x10C)        /**< (SPI_TCR) Transmit Counter Register Offset */
#define SPI_RNPR_OFFSET                (0x110)        /**< (SPI_RNPR) Receive Next Pointer Register Offset */
#define SPI_RNCR_OFFSET                (0x114)        /**< (SPI_RNCR) Receive Next Counter Register Offset */
#define SPI_TNPR_OFFSET                (0x118)        /**< (SPI_TNPR) Transmit Next Pointer Register Offset */
#define SPI_TNCR_OFFSET                (0x11C)        /**< (SPI_TNCR) Transmit Next Counter Register Offset */
#define SPI_PTCR_OFFSET                (0x120)        /**< (SPI_PTCR) Transfer Control Register Offset */
#define SPI_PTSR_OFFSET                (0x124)        /**< (SPI_PTSR) Transfer Status Register Offset */

/** \brief SPI register API structure */
typedef struct
{
  __O   uint32_t                       SPI_CR;          /**< Offset: 0x00 ( /W  32) SPI Control Register */
  __IO  uint32_t                       SPI_MR;          /**< Offset: 0x04 (R/W  32) SPI Mode Register */
  __I   uint32_t                       SPI_RDR;         /**< Offset: 0x08 (R/   32) SPI Receive Data Register */
  __O   uint32_t                       SPI_TDR;         /**< Offset: 0x0c ( /W  32) SPI Transmit Data Register */
  __I   uint32_t                       SPI_SR;          /**< Offset: 0x10 (R/   32) SPI Status Register */
  __O   uint32_t                       SPI_IER;         /**< Offset: 0x14 ( /W  32) SPI Interrupt Enable Register */
  __O   uint32_t                       SPI_IDR;         /**< Offset: 0x18 ( /W  32) SPI Interrupt Disable Register */
  __I   uint32_t                       SPI_IMR;         /**< Offset: 0x1c (R/   32) SPI Interrupt Mask Register */
  __I   uint8_t                        Reserved1[0x10];
  __IO  uint32_t                       SPI_CSR[2];      /**< Offset: 0x30 (R/W  32) SPI Chip Select Register 0 */
  __I   uint8_t                        Reserved2[0x10];
  __IO  uint32_t                       SPI_CMPR;        /**< Offset: 0x48 (R/W  32) SPI Comparison Register */
  __I   uint8_t                        Reserved3[0x98];
  __IO  uint32_t                       SPI_WPMR;        /**< Offset: 0xe4 (R/W  32) SPI Write Protection Mode Register */
  __I   uint32_t                       SPI_WPSR;        /**< Offset: 0xe8 (R/   32) SPI Write Protection Status Register */
  __I   uint8_t                        Reserved4[0x14];
  __IO  uint32_t                       SPI_RPR;         /**< Offset: 0x100 (R/W  32) Receive Pointer Register */
  __IO  uint32_t                       SPI_RCR;         /**< Offset: 0x104 (R/W  32) Receive Counter Register */
  __IO  uint32_t                       SPI_TPR;         /**< Offset: 0x108 (R/W  32) Transmit Pointer Register */
  __IO  uint32_t                       SPI_TCR;         /**< Offset: 0x10c (R/W  32) Transmit Counter Register */
  __IO  uint32_t                       SPI_RNPR;        /**< Offset: 0x110 (R/W  32) Receive Next Pointer Register */
  __IO  uint32_t                       SPI_RNCR;        /**< Offset: 0x114 (R/W  32) Receive Next Counter Register */
  __IO  uint32_t                       SPI_TNPR;        /**< Offset: 0x118 (R/W  32) Transmit Next Pointer Register */
  __IO  uint32_t                       SPI_TNCR;        /**< Offset: 0x11c (R/W  32) Transmit Next Counter Register */
  __O   uint32_t                       SPI_PTCR;        /**< Offset: 0x120 ( /W  32) Transfer Control Register */
  __I   uint32_t                       SPI_PTSR;        /**< Offset: 0x124 (R/   32) Transfer Status Register */
} spi_registers_t;
/** @}  end of Serial Peripheral Interface */

#endif /* SAMG_SAMG55_SPI_MODULE_H */

