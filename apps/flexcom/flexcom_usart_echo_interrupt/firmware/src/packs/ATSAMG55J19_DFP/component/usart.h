/**
 * \brief Header file for SAMG/SAMG55 USART
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
#ifndef SAMG_SAMG55_USART_MODULE_H
#define SAMG_SAMG55_USART_MODULE_H

/** \addtogroup SAMG_SAMG55 Universal Synchronous Asynchronous Receiver Transmitter
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_USART                                 */
/* ========================================================================== */

/* -------- US_CR : (USART Offset: 0x00) ( /W 32) Control Register -------- */
#define US_CR_RSTRX_Pos                       (2U)                                           /**< (US_CR) Reset Receiver Position */
#define US_CR_RSTRX_Msk                       (0x1U << US_CR_RSTRX_Pos)                      /**< (US_CR) Reset Receiver Mask */
#define US_CR_RSTRX(value)                    (US_CR_RSTRX_Msk & ((value) << US_CR_RSTRX_Pos))
#define US_CR_RSTTX_Pos                       (3U)                                           /**< (US_CR) Reset Transmitter Position */
#define US_CR_RSTTX_Msk                       (0x1U << US_CR_RSTTX_Pos)                      /**< (US_CR) Reset Transmitter Mask */
#define US_CR_RSTTX(value)                    (US_CR_RSTTX_Msk & ((value) << US_CR_RSTTX_Pos))
#define US_CR_RXEN_Pos                        (4U)                                           /**< (US_CR) Receiver Enable Position */
#define US_CR_RXEN_Msk                        (0x1U << US_CR_RXEN_Pos)                       /**< (US_CR) Receiver Enable Mask */
#define US_CR_RXEN(value)                     (US_CR_RXEN_Msk & ((value) << US_CR_RXEN_Pos))
#define US_CR_RXDIS_Pos                       (5U)                                           /**< (US_CR) Receiver Disable Position */
#define US_CR_RXDIS_Msk                       (0x1U << US_CR_RXDIS_Pos)                      /**< (US_CR) Receiver Disable Mask */
#define US_CR_RXDIS(value)                    (US_CR_RXDIS_Msk & ((value) << US_CR_RXDIS_Pos))
#define US_CR_TXEN_Pos                        (6U)                                           /**< (US_CR) Transmitter Enable Position */
#define US_CR_TXEN_Msk                        (0x1U << US_CR_TXEN_Pos)                       /**< (US_CR) Transmitter Enable Mask */
#define US_CR_TXEN(value)                     (US_CR_TXEN_Msk & ((value) << US_CR_TXEN_Pos))
#define US_CR_TXDIS_Pos                       (7U)                                           /**< (US_CR) Transmitter Disable Position */
#define US_CR_TXDIS_Msk                       (0x1U << US_CR_TXDIS_Pos)                      /**< (US_CR) Transmitter Disable Mask */
#define US_CR_TXDIS(value)                    (US_CR_TXDIS_Msk & ((value) << US_CR_TXDIS_Pos))
#define US_CR_RSTSTA_Pos                      (8U)                                           /**< (US_CR) Reset Status Bits Position */
#define US_CR_RSTSTA_Msk                      (0x1U << US_CR_RSTSTA_Pos)                     /**< (US_CR) Reset Status Bits Mask */
#define US_CR_RSTSTA(value)                   (US_CR_RSTSTA_Msk & ((value) << US_CR_RSTSTA_Pos))
#define US_CR_STTBRK_Pos                      (9U)                                           /**< (US_CR) Start Break Position */
#define US_CR_STTBRK_Msk                      (0x1U << US_CR_STTBRK_Pos)                     /**< (US_CR) Start Break Mask */
#define US_CR_STTBRK(value)                   (US_CR_STTBRK_Msk & ((value) << US_CR_STTBRK_Pos))
#define US_CR_STPBRK_Pos                      (10U)                                          /**< (US_CR) Stop Break Position */
#define US_CR_STPBRK_Msk                      (0x1U << US_CR_STPBRK_Pos)                     /**< (US_CR) Stop Break Mask */
#define US_CR_STPBRK(value)                   (US_CR_STPBRK_Msk & ((value) << US_CR_STPBRK_Pos))
#define US_CR_STTTO_Pos                       (11U)                                          /**< (US_CR) Clear TIMEOUT Flag and Start Time-out After Next Character Received Position */
#define US_CR_STTTO_Msk                       (0x1U << US_CR_STTTO_Pos)                      /**< (US_CR) Clear TIMEOUT Flag and Start Time-out After Next Character Received Mask */
#define US_CR_STTTO(value)                    (US_CR_STTTO_Msk & ((value) << US_CR_STTTO_Pos))
#define US_CR_SENDA_Pos                       (12U)                                          /**< (US_CR) Send Address Position */
#define US_CR_SENDA_Msk                       (0x1U << US_CR_SENDA_Pos)                      /**< (US_CR) Send Address Mask */
#define US_CR_SENDA(value)                    (US_CR_SENDA_Msk & ((value) << US_CR_SENDA_Pos))
#define US_CR_RSTIT_Pos                       (13U)                                          /**< (US_CR) Reset Iterations Position */
#define US_CR_RSTIT_Msk                       (0x1U << US_CR_RSTIT_Pos)                      /**< (US_CR) Reset Iterations Mask */
#define US_CR_RSTIT(value)                    (US_CR_RSTIT_Msk & ((value) << US_CR_RSTIT_Pos))
#define US_CR_RSTNACK_Pos                     (14U)                                          /**< (US_CR) Reset Non Acknowledge Position */
#define US_CR_RSTNACK_Msk                     (0x1U << US_CR_RSTNACK_Pos)                    /**< (US_CR) Reset Non Acknowledge Mask */
#define US_CR_RSTNACK(value)                  (US_CR_RSTNACK_Msk & ((value) << US_CR_RSTNACK_Pos))
#define US_CR_RETTO_Pos                       (15U)                                          /**< (US_CR) Start Time-out Immediately Position */
#define US_CR_RETTO_Msk                       (0x1U << US_CR_RETTO_Pos)                      /**< (US_CR) Start Time-out Immediately Mask */
#define US_CR_RETTO(value)                    (US_CR_RETTO_Msk & ((value) << US_CR_RETTO_Pos))
#define US_CR_RTSEN_Pos                       (18U)                                          /**< (US_CR) Request to Send Enable Position */
#define US_CR_RTSEN_Msk                       (0x1U << US_CR_RTSEN_Pos)                      /**< (US_CR) Request to Send Enable Mask */
#define US_CR_RTSEN(value)                    (US_CR_RTSEN_Msk & ((value) << US_CR_RTSEN_Pos))
#define US_CR_RTSDIS_Pos                      (19U)                                          /**< (US_CR) Request to Send Disable Position */
#define US_CR_RTSDIS_Msk                      (0x1U << US_CR_RTSDIS_Pos)                     /**< (US_CR) Request to Send Disable Mask */
#define US_CR_RTSDIS(value)                   (US_CR_RTSDIS_Msk & ((value) << US_CR_RTSDIS_Pos))
#define US_CR_LINABT_Pos                      (20U)                                          /**< (US_CR) Abort LIN Transmission Position */
#define US_CR_LINABT_Msk                      (0x1U << US_CR_LINABT_Pos)                     /**< (US_CR) Abort LIN Transmission Mask */
#define US_CR_LINABT(value)                   (US_CR_LINABT_Msk & ((value) << US_CR_LINABT_Pos))
#define US_CR_LINWKUP_Pos                     (21U)                                          /**< (US_CR) Send LIN Wakeup Signal Position */
#define US_CR_LINWKUP_Msk                     (0x1U << US_CR_LINWKUP_Pos)                    /**< (US_CR) Send LIN Wakeup Signal Mask */
#define US_CR_LINWKUP(value)                  (US_CR_LINWKUP_Msk & ((value) << US_CR_LINWKUP_Pos))
#define US_CR_REQCLR_Pos                      (28U)                                          /**< (US_CR) Request to Clear the Comparison Trigger Position */
#define US_CR_REQCLR_Msk                      (0x1U << US_CR_REQCLR_Pos)                     /**< (US_CR) Request to Clear the Comparison Trigger Mask */
#define US_CR_REQCLR(value)                   (US_CR_REQCLR_Msk & ((value) << US_CR_REQCLR_Pos))
#define US_CR_Msk                             (0x103CFFFCUL)                                 /**< (US_CR) Register Mask  */

/* -------- US_MR : (USART Offset: 0x04) (R/W 32) Mode Register -------- */
#define US_MR_USART_MODE_Pos                  (0U)                                           /**< (US_MR) USART Mode of Operation Position */
#define US_MR_USART_MODE_Msk                  (0xFU << US_MR_USART_MODE_Pos)                 /**< (US_MR) USART Mode of Operation Mask */
#define US_MR_USART_MODE(value)               (US_MR_USART_MODE_Msk & ((value) << US_MR_USART_MODE_Pos))
#define   US_MR_USART_MODE_NORMAL_Val         (0U)                                           /**< (US_MR) Normal mode  */
#define   US_MR_USART_MODE_RS485_Val          (1U)                                           /**< (US_MR) RS485 mode  */
#define   US_MR_USART_MODE_HW_HANDSHAKING_Val (2U)                                           /**< (US_MR) Hardware Handshaking  */
#define   US_MR_USART_MODE_IS07816_T_0_Val    (4U)                                           /**< (US_MR) IS07816 Protocol: T = 0  */
#define   US_MR_USART_MODE_IS07816_T_1_Val    (6U)                                           /**< (US_MR) IS07816 Protocol: T = 1  */
#define   US_MR_USART_MODE_IRDA_Val           (8U)                                           /**< (US_MR) IrDA mode  */
#define   US_MR_USART_MODE_LIN_MASTER_Val     (10U)                                          /**< (US_MR) LIN master mode  */
#define   US_MR_USART_MODE_LIN_SLAVE_Val      (11U)                                          /**< (US_MR) LIN Slave mode  */
#define   US_MR_USART_MODE_SPI_MASTER_Val     (14U)                                          /**< (US_MR) SPI master mode  */
#define   US_MR_USART_MODE_SPI_SLAVE_Val      (15U)                                          /**< (US_MR) SPI Slave mode  */
#define US_MR_USART_MODE_NORMAL               (US_MR_USART_MODE_NORMAL_Val << US_MR_USART_MODE_Pos) /**< (US_MR) Normal mode Position  */
#define US_MR_USART_MODE_RS485                (US_MR_USART_MODE_RS485_Val << US_MR_USART_MODE_Pos) /**< (US_MR) RS485 mode Position  */
#define US_MR_USART_MODE_HW_HANDSHAKING       (US_MR_USART_MODE_HW_HANDSHAKING_Val << US_MR_USART_MODE_Pos) /**< (US_MR) Hardware Handshaking Position  */
#define US_MR_USART_MODE_IS07816_T_0          (US_MR_USART_MODE_IS07816_T_0_Val << US_MR_USART_MODE_Pos) /**< (US_MR) IS07816 Protocol: T = 0 Position  */
#define US_MR_USART_MODE_IS07816_T_1          (US_MR_USART_MODE_IS07816_T_1_Val << US_MR_USART_MODE_Pos) /**< (US_MR) IS07816 Protocol: T = 1 Position  */
#define US_MR_USART_MODE_IRDA                 (US_MR_USART_MODE_IRDA_Val << US_MR_USART_MODE_Pos) /**< (US_MR) IrDA mode Position  */
#define US_MR_USART_MODE_LIN_MASTER           (US_MR_USART_MODE_LIN_MASTER_Val << US_MR_USART_MODE_Pos) /**< (US_MR) LIN master mode Position  */
#define US_MR_USART_MODE_LIN_SLAVE            (US_MR_USART_MODE_LIN_SLAVE_Val << US_MR_USART_MODE_Pos) /**< (US_MR) LIN Slave mode Position  */
#define US_MR_USART_MODE_SPI_MASTER           (US_MR_USART_MODE_SPI_MASTER_Val << US_MR_USART_MODE_Pos) /**< (US_MR) SPI master mode Position  */
#define US_MR_USART_MODE_SPI_SLAVE            (US_MR_USART_MODE_SPI_SLAVE_Val << US_MR_USART_MODE_Pos) /**< (US_MR) SPI Slave mode Position  */
#define US_MR_USCLKS_Pos                      (4U)                                           /**< (US_MR) Clock Selection Position */
#define US_MR_USCLKS_Msk                      (0x3U << US_MR_USCLKS_Pos)                     /**< (US_MR) Clock Selection Mask */
#define US_MR_USCLKS(value)                   (US_MR_USCLKS_Msk & ((value) << US_MR_USCLKS_Pos))
#define   US_MR_USCLKS_MCK_Val                (0U)                                           /**< (US_MR) Peripheral clock is selected  */
#define   US_MR_USCLKS_DIV_Val                (1U)                                           /**< (US_MR) Peripheral clock divided (DIV=8) is selected  */
#define   US_MR_USCLKS_PMC_PCK_Val            (2U)                                           /**< (US_MR) PMC programmable clock (PCK) is selected.If the SCK pin is driven (CLKO=1), the CD field must be greater than 1.  */
#define   US_MR_USCLKS_SCK_Val                (3U)                                           /**< (US_MR) External pin (SCK) is selected  */
#define US_MR_USCLKS_MCK                      (US_MR_USCLKS_MCK_Val << US_MR_USCLKS_Pos)     /**< (US_MR) Peripheral clock is selected Position  */
#define US_MR_USCLKS_DIV                      (US_MR_USCLKS_DIV_Val << US_MR_USCLKS_Pos)     /**< (US_MR) Peripheral clock divided (DIV=8) is selected Position  */
#define US_MR_USCLKS_PMC_PCK                  (US_MR_USCLKS_PMC_PCK_Val << US_MR_USCLKS_Pos) /**< (US_MR) PMC programmable clock (PCK) is selected.If the SCK pin is driven (CLKO=1), the CD field must be greater than 1. Position  */
#define US_MR_USCLKS_SCK                      (US_MR_USCLKS_SCK_Val << US_MR_USCLKS_Pos)     /**< (US_MR) External pin (SCK) is selected Position  */
#define US_MR_CHRL_Pos                        (6U)                                           /**< (US_MR) Character Length Position */
#define US_MR_CHRL_Msk                        (0x3U << US_MR_CHRL_Pos)                       /**< (US_MR) Character Length Mask */
#define US_MR_CHRL(value)                     (US_MR_CHRL_Msk & ((value) << US_MR_CHRL_Pos))
#define   US_MR_CHRL_5_BIT_Val                (0U)                                           /**< (US_MR) Character length is 5 bits  */
#define   US_MR_CHRL_6_BIT_Val                (1U)                                           /**< (US_MR) Character length is 6 bits  */
#define   US_MR_CHRL_7_BIT_Val                (2U)                                           /**< (US_MR) Character length is 7 bits  */
#define   US_MR_CHRL_8_BIT_Val                (3U)                                           /**< (US_MR) Character length is 8 bits  */
#define US_MR_CHRL_5_BIT                      (US_MR_CHRL_5_BIT_Val << US_MR_CHRL_Pos)       /**< (US_MR) Character length is 5 bits Position  */
#define US_MR_CHRL_6_BIT                      (US_MR_CHRL_6_BIT_Val << US_MR_CHRL_Pos)       /**< (US_MR) Character length is 6 bits Position  */
#define US_MR_CHRL_7_BIT                      (US_MR_CHRL_7_BIT_Val << US_MR_CHRL_Pos)       /**< (US_MR) Character length is 7 bits Position  */
#define US_MR_CHRL_8_BIT                      (US_MR_CHRL_8_BIT_Val << US_MR_CHRL_Pos)       /**< (US_MR) Character length is 8 bits Position  */
#define US_MR_SYNC_Pos                        (8U)                                           /**< (US_MR) Synchronous Mode Select Position */
#define US_MR_SYNC_Msk                        (0x1U << US_MR_SYNC_Pos)                       /**< (US_MR) Synchronous Mode Select Mask */
#define US_MR_SYNC(value)                     (US_MR_SYNC_Msk & ((value) << US_MR_SYNC_Pos))
#define US_MR_PAR_Pos                         (9U)                                           /**< (US_MR) Parity Type Position */
#define US_MR_PAR_Msk                         (0x7U << US_MR_PAR_Pos)                        /**< (US_MR) Parity Type Mask */
#define US_MR_PAR(value)                      (US_MR_PAR_Msk & ((value) << US_MR_PAR_Pos))  
#define   US_MR_PAR_EVEN_Val                  (0U)                                           /**< (US_MR) Even parity  */
#define   US_MR_PAR_ODD_Val                   (1U)                                           /**< (US_MR) Odd parity  */
#define   US_MR_PAR_SPACE_Val                 (2U)                                           /**< (US_MR) Parity forced to 0 (Space)  */
#define   US_MR_PAR_MARK_Val                  (3U)                                           /**< (US_MR) Parity forced to 1 (Mark)  */
#define   US_MR_PAR_NO_Val                    (4U)                                           /**< (US_MR) No parity  */
#define   US_MR_PAR_MULTIDROP_Val             (6U)                                           /**< (US_MR) Multidrop mode  */
#define US_MR_PAR_EVEN                        (US_MR_PAR_EVEN_Val << US_MR_PAR_Pos)          /**< (US_MR) Even parity Position  */
#define US_MR_PAR_ODD                         (US_MR_PAR_ODD_Val << US_MR_PAR_Pos)           /**< (US_MR) Odd parity Position  */
#define US_MR_PAR_SPACE                       (US_MR_PAR_SPACE_Val << US_MR_PAR_Pos)         /**< (US_MR) Parity forced to 0 (Space) Position  */
#define US_MR_PAR_MARK                        (US_MR_PAR_MARK_Val << US_MR_PAR_Pos)          /**< (US_MR) Parity forced to 1 (Mark) Position  */
#define US_MR_PAR_NO                          (US_MR_PAR_NO_Val << US_MR_PAR_Pos)            /**< (US_MR) No parity Position  */
#define US_MR_PAR_MULTIDROP                   (US_MR_PAR_MULTIDROP_Val << US_MR_PAR_Pos)     /**< (US_MR) Multidrop mode Position  */
#define US_MR_NBSTOP_Pos                      (12U)                                          /**< (US_MR) Number of Stop Bits Position */
#define US_MR_NBSTOP_Msk                      (0x3U << US_MR_NBSTOP_Pos)                     /**< (US_MR) Number of Stop Bits Mask */
#define US_MR_NBSTOP(value)                   (US_MR_NBSTOP_Msk & ((value) << US_MR_NBSTOP_Pos))
#define   US_MR_NBSTOP_1_BIT_Val              (0U)                                           /**< (US_MR) 1 stop bit  */
#define   US_MR_NBSTOP_1_5_BIT_Val            (1U)                                           /**< (US_MR) 1.5 stop bits (SYNC = 0) or reserved (SYNC = 1)  */
#define   US_MR_NBSTOP_2_BIT_Val              (2U)                                           /**< (US_MR) 2 stop bits  */
#define US_MR_NBSTOP_1_BIT                    (US_MR_NBSTOP_1_BIT_Val << US_MR_NBSTOP_Pos)   /**< (US_MR) 1 stop bit Position  */
#define US_MR_NBSTOP_1_5_BIT                  (US_MR_NBSTOP_1_5_BIT_Val << US_MR_NBSTOP_Pos) /**< (US_MR) 1.5 stop bits (SYNC = 0) or reserved (SYNC = 1) Position  */
#define US_MR_NBSTOP_2_BIT                    (US_MR_NBSTOP_2_BIT_Val << US_MR_NBSTOP_Pos)   /**< (US_MR) 2 stop bits Position  */
#define US_MR_CHMODE_Pos                      (14U)                                          /**< (US_MR) Channel Mode Position */
#define US_MR_CHMODE_Msk                      (0x3U << US_MR_CHMODE_Pos)                     /**< (US_MR) Channel Mode Mask */
#define US_MR_CHMODE(value)                   (US_MR_CHMODE_Msk & ((value) << US_MR_CHMODE_Pos))
#define   US_MR_CHMODE_NORMAL_Val             (0U)                                           /**< (US_MR) Normal mode  */
#define   US_MR_CHMODE_AUTOMATIC_Val          (1U)                                           /**< (US_MR) Automatic Echo. Receiver input is connected to the TXD pin.  */
#define   US_MR_CHMODE_LOCAL_LOOPBACK_Val     (2U)                                           /**< (US_MR) Local Loopback. Transmitter output is connected to the Receiver Input.  */
#define   US_MR_CHMODE_REMOTE_LOOPBACK_Val    (3U)                                           /**< (US_MR) Remote Loopback. RXD pin is internally connected to the TXD pin.  */
#define US_MR_CHMODE_NORMAL                   (US_MR_CHMODE_NORMAL_Val << US_MR_CHMODE_Pos)  /**< (US_MR) Normal mode Position  */
#define US_MR_CHMODE_AUTOMATIC                (US_MR_CHMODE_AUTOMATIC_Val << US_MR_CHMODE_Pos) /**< (US_MR) Automatic Echo. Receiver input is connected to the TXD pin. Position  */
#define US_MR_CHMODE_LOCAL_LOOPBACK           (US_MR_CHMODE_LOCAL_LOOPBACK_Val << US_MR_CHMODE_Pos) /**< (US_MR) Local Loopback. Transmitter output is connected to the Receiver Input. Position  */
#define US_MR_CHMODE_REMOTE_LOOPBACK          (US_MR_CHMODE_REMOTE_LOOPBACK_Val << US_MR_CHMODE_Pos) /**< (US_MR) Remote Loopback. RXD pin is internally connected to the TXD pin. Position  */
#define US_MR_MSBF_Pos                        (16U)                                          /**< (US_MR) Bit Order Position */
#define US_MR_MSBF_Msk                        (0x1U << US_MR_MSBF_Pos)                       /**< (US_MR) Bit Order Mask */
#define US_MR_MSBF(value)                     (US_MR_MSBF_Msk & ((value) << US_MR_MSBF_Pos))
#define US_MR_MODE9_Pos                       (17U)                                          /**< (US_MR) 9-bit Character Length Position */
#define US_MR_MODE9_Msk                       (0x1U << US_MR_MODE9_Pos)                      /**< (US_MR) 9-bit Character Length Mask */
#define US_MR_MODE9(value)                    (US_MR_MODE9_Msk & ((value) << US_MR_MODE9_Pos))
#define US_MR_CLKO_Pos                        (18U)                                          /**< (US_MR) Clock Output Select Position */
#define US_MR_CLKO_Msk                        (0x1U << US_MR_CLKO_Pos)                       /**< (US_MR) Clock Output Select Mask */
#define US_MR_CLKO(value)                     (US_MR_CLKO_Msk & ((value) << US_MR_CLKO_Pos))
#define US_MR_OVER_Pos                        (19U)                                          /**< (US_MR) Oversampling Mode Position */
#define US_MR_OVER_Msk                        (0x1U << US_MR_OVER_Pos)                       /**< (US_MR) Oversampling Mode Mask */
#define US_MR_OVER(value)                     (US_MR_OVER_Msk & ((value) << US_MR_OVER_Pos))
#define US_MR_INACK_Pos                       (20U)                                          /**< (US_MR) Inhibit Non Acknowledge Position */
#define US_MR_INACK_Msk                       (0x1U << US_MR_INACK_Pos)                      /**< (US_MR) Inhibit Non Acknowledge Mask */
#define US_MR_INACK(value)                    (US_MR_INACK_Msk & ((value) << US_MR_INACK_Pos))
#define US_MR_DSNACK_Pos                      (21U)                                          /**< (US_MR) Disable Successive NACK Position */
#define US_MR_DSNACK_Msk                      (0x1U << US_MR_DSNACK_Pos)                     /**< (US_MR) Disable Successive NACK Mask */
#define US_MR_DSNACK(value)                   (US_MR_DSNACK_Msk & ((value) << US_MR_DSNACK_Pos))
#define US_MR_INVDATA_Pos                     (23U)                                          /**< (US_MR) Inverted Data Position */
#define US_MR_INVDATA_Msk                     (0x1U << US_MR_INVDATA_Pos)                    /**< (US_MR) Inverted Data Mask */
#define US_MR_INVDATA(value)                  (US_MR_INVDATA_Msk & ((value) << US_MR_INVDATA_Pos))
#define US_MR_MAX_ITERATION_Pos               (24U)                                          /**< (US_MR) Maximum Number of Automatic Iteration Position */
#define US_MR_MAX_ITERATION_Msk               (0x7U << US_MR_MAX_ITERATION_Pos)              /**< (US_MR) Maximum Number of Automatic Iteration Mask */
#define US_MR_MAX_ITERATION(value)            (US_MR_MAX_ITERATION_Msk & ((value) << US_MR_MAX_ITERATION_Pos))
#define US_MR_FILTER_Pos                      (28U)                                          /**< (US_MR) Receive Line Filter Position */
#define US_MR_FILTER_Msk                      (0x1U << US_MR_FILTER_Pos)                     /**< (US_MR) Receive Line Filter Mask */
#define US_MR_FILTER(value)                   (US_MR_FILTER_Msk & ((value) << US_MR_FILTER_Pos))
#define US_MR_Msk                             (0x17BFFFFFUL)                                 /**< (US_MR) Register Mask  */

/* -------- US_IER : (USART Offset: 0x08) ( /W 32) Interrupt Enable Register -------- */
#define US_IER_RXRDY_Pos                      (0U)                                           /**< (US_IER) RXRDY Interrupt Enable Position */
#define US_IER_RXRDY_Msk                      (0x1U << US_IER_RXRDY_Pos)                     /**< (US_IER) RXRDY Interrupt Enable Mask */
#define US_IER_RXRDY(value)                   (US_IER_RXRDY_Msk & ((value) << US_IER_RXRDY_Pos))
#define US_IER_TXRDY_Pos                      (1U)                                           /**< (US_IER) TXRDY Interrupt Enable Position */
#define US_IER_TXRDY_Msk                      (0x1U << US_IER_TXRDY_Pos)                     /**< (US_IER) TXRDY Interrupt Enable Mask */
#define US_IER_TXRDY(value)                   (US_IER_TXRDY_Msk & ((value) << US_IER_TXRDY_Pos))
#define US_IER_RXBRK_Pos                      (2U)                                           /**< (US_IER) Receiver Break Interrupt Enable Position */
#define US_IER_RXBRK_Msk                      (0x1U << US_IER_RXBRK_Pos)                     /**< (US_IER) Receiver Break Interrupt Enable Mask */
#define US_IER_RXBRK(value)                   (US_IER_RXBRK_Msk & ((value) << US_IER_RXBRK_Pos))
#define US_IER_ENDRX_Pos                      (3U)                                           /**< (US_IER) End of Receive Buffer Interrupt Enable (available in all USART modes of operation) Position */
#define US_IER_ENDRX_Msk                      (0x1U << US_IER_ENDRX_Pos)                     /**< (US_IER) End of Receive Buffer Interrupt Enable (available in all USART modes of operation) Mask */
#define US_IER_ENDRX(value)                   (US_IER_ENDRX_Msk & ((value) << US_IER_ENDRX_Pos))
#define US_IER_ENDTX_Pos                      (4U)                                           /**< (US_IER) End of Transmit Buffer Interrupt Enable (available in all USART modes of operation) Position */
#define US_IER_ENDTX_Msk                      (0x1U << US_IER_ENDTX_Pos)                     /**< (US_IER) End of Transmit Buffer Interrupt Enable (available in all USART modes of operation) Mask */
#define US_IER_ENDTX(value)                   (US_IER_ENDTX_Msk & ((value) << US_IER_ENDTX_Pos))
#define US_IER_OVRE_Pos                       (5U)                                           /**< (US_IER) Overrun Error Interrupt Enable Position */
#define US_IER_OVRE_Msk                       (0x1U << US_IER_OVRE_Pos)                      /**< (US_IER) Overrun Error Interrupt Enable Mask */
#define US_IER_OVRE(value)                    (US_IER_OVRE_Msk & ((value) << US_IER_OVRE_Pos))
#define US_IER_FRAME_Pos                      (6U)                                           /**< (US_IER) Framing Error Interrupt Enable Position */
#define US_IER_FRAME_Msk                      (0x1U << US_IER_FRAME_Pos)                     /**< (US_IER) Framing Error Interrupt Enable Mask */
#define US_IER_FRAME(value)                   (US_IER_FRAME_Msk & ((value) << US_IER_FRAME_Pos))
#define US_IER_PARE_Pos                       (7U)                                           /**< (US_IER) Parity Error Interrupt Enable Position */
#define US_IER_PARE_Msk                       (0x1U << US_IER_PARE_Pos)                      /**< (US_IER) Parity Error Interrupt Enable Mask */
#define US_IER_PARE(value)                    (US_IER_PARE_Msk & ((value) << US_IER_PARE_Pos))
#define US_IER_TIMEOUT_Pos                    (8U)                                           /**< (US_IER) Time-out Interrupt Enable Position */
#define US_IER_TIMEOUT_Msk                    (0x1U << US_IER_TIMEOUT_Pos)                   /**< (US_IER) Time-out Interrupt Enable Mask */
#define US_IER_TIMEOUT(value)                 (US_IER_TIMEOUT_Msk & ((value) << US_IER_TIMEOUT_Pos))
#define US_IER_TXEMPTY_Pos                    (9U)                                           /**< (US_IER) TXEMPTY Interrupt Enable Position */
#define US_IER_TXEMPTY_Msk                    (0x1U << US_IER_TXEMPTY_Pos)                   /**< (US_IER) TXEMPTY Interrupt Enable Mask */
#define US_IER_TXEMPTY(value)                 (US_IER_TXEMPTY_Msk & ((value) << US_IER_TXEMPTY_Pos))
#define US_IER_ITER_Pos                       (10U)                                          /**< (US_IER) Max number of Repetitions Reached Interrupt Enable Position */
#define US_IER_ITER_Msk                       (0x1U << US_IER_ITER_Pos)                      /**< (US_IER) Max number of Repetitions Reached Interrupt Enable Mask */
#define US_IER_ITER(value)                    (US_IER_ITER_Msk & ((value) << US_IER_ITER_Pos))
#define US_IER_TXBUFE_Pos                     (11U)                                          /**< (US_IER) Transmit Buffer Empty Interrupt Enable (available in all USART modes of operation) Position */
#define US_IER_TXBUFE_Msk                     (0x1U << US_IER_TXBUFE_Pos)                    /**< (US_IER) Transmit Buffer Empty Interrupt Enable (available in all USART modes of operation) Mask */
#define US_IER_TXBUFE(value)                  (US_IER_TXBUFE_Msk & ((value) << US_IER_TXBUFE_Pos))
#define US_IER_RXBUFF_Pos                     (12U)                                          /**< (US_IER) Receive Buffer Full Interrupt Enable (available in all USART modes of operation) Position */
#define US_IER_RXBUFF_Msk                     (0x1U << US_IER_RXBUFF_Pos)                    /**< (US_IER) Receive Buffer Full Interrupt Enable (available in all USART modes of operation) Mask */
#define US_IER_RXBUFF(value)                  (US_IER_RXBUFF_Msk & ((value) << US_IER_RXBUFF_Pos))
#define US_IER_NACK_Pos                       (13U)                                          /**< (US_IER) Non Acknowledge Interrupt Enable Position */
#define US_IER_NACK_Msk                       (0x1U << US_IER_NACK_Pos)                      /**< (US_IER) Non Acknowledge Interrupt Enable Mask */
#define US_IER_NACK(value)                    (US_IER_NACK_Msk & ((value) << US_IER_NACK_Pos))
#define US_IER_CTSIC_Pos                      (19U)                                          /**< (US_IER) Clear to Send Input Change Interrupt Enable Position */
#define US_IER_CTSIC_Msk                      (0x1U << US_IER_CTSIC_Pos)                     /**< (US_IER) Clear to Send Input Change Interrupt Enable Mask */
#define US_IER_CTSIC(value)                   (US_IER_CTSIC_Msk & ((value) << US_IER_CTSIC_Pos))
#define US_IER_CMP_Pos                        (22U)                                          /**< (US_IER) Comparison Interrupt Enable Position */
#define US_IER_CMP_Msk                        (0x1U << US_IER_CMP_Pos)                       /**< (US_IER) Comparison Interrupt Enable Mask */
#define US_IER_CMP(value)                     (US_IER_CMP_Msk & ((value) << US_IER_CMP_Pos))
#define US_IER_Msk                            (0x00483FFFUL)                                 /**< (US_IER) Register Mask  */

/* -------- US_IDR : (USART Offset: 0x0C) ( /W 32) Interrupt Disable Register -------- */
#define US_IDR_RXRDY_Pos                      (0U)                                           /**< (US_IDR) RXRDY Interrupt Disable Position */
#define US_IDR_RXRDY_Msk                      (0x1U << US_IDR_RXRDY_Pos)                     /**< (US_IDR) RXRDY Interrupt Disable Mask */
#define US_IDR_RXRDY(value)                   (US_IDR_RXRDY_Msk & ((value) << US_IDR_RXRDY_Pos))
#define US_IDR_TXRDY_Pos                      (1U)                                           /**< (US_IDR) TXRDY Interrupt Disable Position */
#define US_IDR_TXRDY_Msk                      (0x1U << US_IDR_TXRDY_Pos)                     /**< (US_IDR) TXRDY Interrupt Disable Mask */
#define US_IDR_TXRDY(value)                   (US_IDR_TXRDY_Msk & ((value) << US_IDR_TXRDY_Pos))
#define US_IDR_RXBRK_Pos                      (2U)                                           /**< (US_IDR) Receiver Break Interrupt Disable Position */
#define US_IDR_RXBRK_Msk                      (0x1U << US_IDR_RXBRK_Pos)                     /**< (US_IDR) Receiver Break Interrupt Disable Mask */
#define US_IDR_RXBRK(value)                   (US_IDR_RXBRK_Msk & ((value) << US_IDR_RXBRK_Pos))
#define US_IDR_ENDRX_Pos                      (3U)                                           /**< (US_IDR) End of Receive Buffer Interrupt Enable (available in all USART modes of operation) Position */
#define US_IDR_ENDRX_Msk                      (0x1U << US_IDR_ENDRX_Pos)                     /**< (US_IDR) End of Receive Buffer Interrupt Enable (available in all USART modes of operation) Mask */
#define US_IDR_ENDRX(value)                   (US_IDR_ENDRX_Msk & ((value) << US_IDR_ENDRX_Pos))
#define US_IDR_ENDTX_Pos                      (4U)                                           /**< (US_IDR) End of Transmit Buffer Interrupt Disable (available in all USART modes of operation) Position */
#define US_IDR_ENDTX_Msk                      (0x1U << US_IDR_ENDTX_Pos)                     /**< (US_IDR) End of Transmit Buffer Interrupt Disable (available in all USART modes of operation) Mask */
#define US_IDR_ENDTX(value)                   (US_IDR_ENDTX_Msk & ((value) << US_IDR_ENDTX_Pos))
#define US_IDR_OVRE_Pos                       (5U)                                           /**< (US_IDR) Overrun Error Interrupt Enable Position */
#define US_IDR_OVRE_Msk                       (0x1U << US_IDR_OVRE_Pos)                      /**< (US_IDR) Overrun Error Interrupt Enable Mask */
#define US_IDR_OVRE(value)                    (US_IDR_OVRE_Msk & ((value) << US_IDR_OVRE_Pos))
#define US_IDR_FRAME_Pos                      (6U)                                           /**< (US_IDR) Framing Error Interrupt Disable Position */
#define US_IDR_FRAME_Msk                      (0x1U << US_IDR_FRAME_Pos)                     /**< (US_IDR) Framing Error Interrupt Disable Mask */
#define US_IDR_FRAME(value)                   (US_IDR_FRAME_Msk & ((value) << US_IDR_FRAME_Pos))
#define US_IDR_PARE_Pos                       (7U)                                           /**< (US_IDR) Parity Error Interrupt Disable Position */
#define US_IDR_PARE_Msk                       (0x1U << US_IDR_PARE_Pos)                      /**< (US_IDR) Parity Error Interrupt Disable Mask */
#define US_IDR_PARE(value)                    (US_IDR_PARE_Msk & ((value) << US_IDR_PARE_Pos))
#define US_IDR_TIMEOUT_Pos                    (8U)                                           /**< (US_IDR) Time-out Interrupt Disable Position */
#define US_IDR_TIMEOUT_Msk                    (0x1U << US_IDR_TIMEOUT_Pos)                   /**< (US_IDR) Time-out Interrupt Disable Mask */
#define US_IDR_TIMEOUT(value)                 (US_IDR_TIMEOUT_Msk & ((value) << US_IDR_TIMEOUT_Pos))
#define US_IDR_TXEMPTY_Pos                    (9U)                                           /**< (US_IDR) TXEMPTY Interrupt Disable Position */
#define US_IDR_TXEMPTY_Msk                    (0x1U << US_IDR_TXEMPTY_Pos)                   /**< (US_IDR) TXEMPTY Interrupt Disable Mask */
#define US_IDR_TXEMPTY(value)                 (US_IDR_TXEMPTY_Msk & ((value) << US_IDR_TXEMPTY_Pos))
#define US_IDR_ITER_Pos                       (10U)                                          /**< (US_IDR) Max Number of Repetitions Reached Interrupt Disable Position */
#define US_IDR_ITER_Msk                       (0x1U << US_IDR_ITER_Pos)                      /**< (US_IDR) Max Number of Repetitions Reached Interrupt Disable Mask */
#define US_IDR_ITER(value)                    (US_IDR_ITER_Msk & ((value) << US_IDR_ITER_Pos))
#define US_IDR_TXBUFE_Pos                     (11U)                                          /**< (US_IDR) Transmit Buffer Empty Interrupt Enable (available in all USART modes of operation) Position */
#define US_IDR_TXBUFE_Msk                     (0x1U << US_IDR_TXBUFE_Pos)                    /**< (US_IDR) Transmit Buffer Empty Interrupt Enable (available in all USART modes of operation) Mask */
#define US_IDR_TXBUFE(value)                  (US_IDR_TXBUFE_Msk & ((value) << US_IDR_TXBUFE_Pos))
#define US_IDR_RXBUFF_Pos                     (12U)                                          /**< (US_IDR) Receive Buffer Full Interrupt Enable (available in all USART modes of operation) Position */
#define US_IDR_RXBUFF_Msk                     (0x1U << US_IDR_RXBUFF_Pos)                    /**< (US_IDR) Receive Buffer Full Interrupt Enable (available in all USART modes of operation) Mask */
#define US_IDR_RXBUFF(value)                  (US_IDR_RXBUFF_Msk & ((value) << US_IDR_RXBUFF_Pos))
#define US_IDR_NACK_Pos                       (13U)                                          /**< (US_IDR) Non Acknowledge Interrupt Disable Position */
#define US_IDR_NACK_Msk                       (0x1U << US_IDR_NACK_Pos)                      /**< (US_IDR) Non Acknowledge Interrupt Disable Mask */
#define US_IDR_NACK(value)                    (US_IDR_NACK_Msk & ((value) << US_IDR_NACK_Pos))
#define US_IDR_CTSIC_Pos                      (19U)                                          /**< (US_IDR) Clear to Send Input Change Interrupt Disable Position */
#define US_IDR_CTSIC_Msk                      (0x1U << US_IDR_CTSIC_Pos)                     /**< (US_IDR) Clear to Send Input Change Interrupt Disable Mask */
#define US_IDR_CTSIC(value)                   (US_IDR_CTSIC_Msk & ((value) << US_IDR_CTSIC_Pos))
#define US_IDR_CMP_Pos                        (22U)                                          /**< (US_IDR) Comparison Interrupt Disable Position */
#define US_IDR_CMP_Msk                        (0x1U << US_IDR_CMP_Pos)                       /**< (US_IDR) Comparison Interrupt Disable Mask */
#define US_IDR_CMP(value)                     (US_IDR_CMP_Msk & ((value) << US_IDR_CMP_Pos))
#define US_IDR_Msk                            (0x00483FFFUL)                                 /**< (US_IDR) Register Mask  */

/* -------- US_IMR : (USART Offset: 0x10) (R/  32) Interrupt Mask Register -------- */
#define US_IMR_RXRDY_Pos                      (0U)                                           /**< (US_IMR) RXRDY Interrupt Mask Position */
#define US_IMR_RXRDY_Msk                      (0x1U << US_IMR_RXRDY_Pos)                     /**< (US_IMR) RXRDY Interrupt Mask Mask */
#define US_IMR_RXRDY(value)                   (US_IMR_RXRDY_Msk & ((value) << US_IMR_RXRDY_Pos))
#define US_IMR_TXRDY_Pos                      (1U)                                           /**< (US_IMR) TXRDY Interrupt Mask Position */
#define US_IMR_TXRDY_Msk                      (0x1U << US_IMR_TXRDY_Pos)                     /**< (US_IMR) TXRDY Interrupt Mask Mask */
#define US_IMR_TXRDY(value)                   (US_IMR_TXRDY_Msk & ((value) << US_IMR_TXRDY_Pos))
#define US_IMR_RXBRK_Pos                      (2U)                                           /**< (US_IMR) Receiver Break Interrupt Mask Position */
#define US_IMR_RXBRK_Msk                      (0x1U << US_IMR_RXBRK_Pos)                     /**< (US_IMR) Receiver Break Interrupt Mask Mask */
#define US_IMR_RXBRK(value)                   (US_IMR_RXBRK_Msk & ((value) << US_IMR_RXBRK_Pos))
#define US_IMR_ENDRX_Pos                      (3U)                                           /**< (US_IMR) End of Receive Buffer Interrupt Mask (available in all USART modes of operation) Position */
#define US_IMR_ENDRX_Msk                      (0x1U << US_IMR_ENDRX_Pos)                     /**< (US_IMR) End of Receive Buffer Interrupt Mask (available in all USART modes of operation) Mask */
#define US_IMR_ENDRX(value)                   (US_IMR_ENDRX_Msk & ((value) << US_IMR_ENDRX_Pos))
#define US_IMR_ENDTX_Pos                      (4U)                                           /**< (US_IMR) End of Transmit Buffer Interrupt Mask (available in all USART modes of operation) Position */
#define US_IMR_ENDTX_Msk                      (0x1U << US_IMR_ENDTX_Pos)                     /**< (US_IMR) End of Transmit Buffer Interrupt Mask (available in all USART modes of operation) Mask */
#define US_IMR_ENDTX(value)                   (US_IMR_ENDTX_Msk & ((value) << US_IMR_ENDTX_Pos))
#define US_IMR_OVRE_Pos                       (5U)                                           /**< (US_IMR) Overrun Error Interrupt Mask Position */
#define US_IMR_OVRE_Msk                       (0x1U << US_IMR_OVRE_Pos)                      /**< (US_IMR) Overrun Error Interrupt Mask Mask */
#define US_IMR_OVRE(value)                    (US_IMR_OVRE_Msk & ((value) << US_IMR_OVRE_Pos))
#define US_IMR_FRAME_Pos                      (6U)                                           /**< (US_IMR) Framing Error Interrupt Mask Position */
#define US_IMR_FRAME_Msk                      (0x1U << US_IMR_FRAME_Pos)                     /**< (US_IMR) Framing Error Interrupt Mask Mask */
#define US_IMR_FRAME(value)                   (US_IMR_FRAME_Msk & ((value) << US_IMR_FRAME_Pos))
#define US_IMR_PARE_Pos                       (7U)                                           /**< (US_IMR) Parity Error Interrupt Mask Position */
#define US_IMR_PARE_Msk                       (0x1U << US_IMR_PARE_Pos)                      /**< (US_IMR) Parity Error Interrupt Mask Mask */
#define US_IMR_PARE(value)                    (US_IMR_PARE_Msk & ((value) << US_IMR_PARE_Pos))
#define US_IMR_TIMEOUT_Pos                    (8U)                                           /**< (US_IMR) Time-out Interrupt Mask Position */
#define US_IMR_TIMEOUT_Msk                    (0x1U << US_IMR_TIMEOUT_Pos)                   /**< (US_IMR) Time-out Interrupt Mask Mask */
#define US_IMR_TIMEOUT(value)                 (US_IMR_TIMEOUT_Msk & ((value) << US_IMR_TIMEOUT_Pos))
#define US_IMR_TXEMPTY_Pos                    (9U)                                           /**< (US_IMR) TXEMPTY Interrupt Mask Position */
#define US_IMR_TXEMPTY_Msk                    (0x1U << US_IMR_TXEMPTY_Pos)                   /**< (US_IMR) TXEMPTY Interrupt Mask Mask */
#define US_IMR_TXEMPTY(value)                 (US_IMR_TXEMPTY_Msk & ((value) << US_IMR_TXEMPTY_Pos))
#define US_IMR_ITER_Pos                       (10U)                                          /**< (US_IMR) Max Number of Repetitions Reached Interrupt Mask Position */
#define US_IMR_ITER_Msk                       (0x1U << US_IMR_ITER_Pos)                      /**< (US_IMR) Max Number of Repetitions Reached Interrupt Mask Mask */
#define US_IMR_ITER(value)                    (US_IMR_ITER_Msk & ((value) << US_IMR_ITER_Pos))
#define US_IMR_TXBUFE_Pos                     (11U)                                          /**< (US_IMR) Transmit Buffer Empty Interrupt Mask (available in all USART modes of operation) Position */
#define US_IMR_TXBUFE_Msk                     (0x1U << US_IMR_TXBUFE_Pos)                    /**< (US_IMR) Transmit Buffer Empty Interrupt Mask (available in all USART modes of operation) Mask */
#define US_IMR_TXBUFE(value)                  (US_IMR_TXBUFE_Msk & ((value) << US_IMR_TXBUFE_Pos))
#define US_IMR_RXBUFF_Pos                     (12U)                                          /**< (US_IMR) Receive Buffer Full Interrupt Mask (available in all USART modes of operation) Position */
#define US_IMR_RXBUFF_Msk                     (0x1U << US_IMR_RXBUFF_Pos)                    /**< (US_IMR) Receive Buffer Full Interrupt Mask (available in all USART modes of operation) Mask */
#define US_IMR_RXBUFF(value)                  (US_IMR_RXBUFF_Msk & ((value) << US_IMR_RXBUFF_Pos))
#define US_IMR_NACK_Pos                       (13U)                                          /**< (US_IMR) Non Acknowledge Interrupt Mask Position */
#define US_IMR_NACK_Msk                       (0x1U << US_IMR_NACK_Pos)                      /**< (US_IMR) Non Acknowledge Interrupt Mask Mask */
#define US_IMR_NACK(value)                    (US_IMR_NACK_Msk & ((value) << US_IMR_NACK_Pos))
#define US_IMR_CTSIC_Pos                      (19U)                                          /**< (US_IMR) Clear to Send Input Change Interrupt Mask Position */
#define US_IMR_CTSIC_Msk                      (0x1U << US_IMR_CTSIC_Pos)                     /**< (US_IMR) Clear to Send Input Change Interrupt Mask Mask */
#define US_IMR_CTSIC(value)                   (US_IMR_CTSIC_Msk & ((value) << US_IMR_CTSIC_Pos))
#define US_IMR_CMP_Pos                        (22U)                                          /**< (US_IMR) Comparison Interrupt Mask Position */
#define US_IMR_CMP_Msk                        (0x1U << US_IMR_CMP_Pos)                       /**< (US_IMR) Comparison Interrupt Mask Mask */
#define US_IMR_CMP(value)                     (US_IMR_CMP_Msk & ((value) << US_IMR_CMP_Pos))
#define US_IMR_Msk                            (0x00483FFFUL)                                 /**< (US_IMR) Register Mask  */

/* -------- US_CSR : (USART Offset: 0x14) (R/  32) Channel Status Register -------- */
#define US_CSR_RXRDY_Pos                      (0U)                                           /**< (US_CSR) Receiver Ready (cleared by reading US_RHR) Position */
#define US_CSR_RXRDY_Msk                      (0x1U << US_CSR_RXRDY_Pos)                     /**< (US_CSR) Receiver Ready (cleared by reading US_RHR) Mask */
#define US_CSR_RXRDY(value)                   (US_CSR_RXRDY_Msk & ((value) << US_CSR_RXRDY_Pos))
#define US_CSR_TXRDY_Pos                      (1U)                                           /**< (US_CSR) Transmitter Ready (cleared by writing US_THR) Position */
#define US_CSR_TXRDY_Msk                      (0x1U << US_CSR_TXRDY_Pos)                     /**< (US_CSR) Transmitter Ready (cleared by writing US_THR) Mask */
#define US_CSR_TXRDY(value)                   (US_CSR_TXRDY_Msk & ((value) << US_CSR_TXRDY_Pos))
#define US_CSR_RXBRK_Pos                      (2U)                                           /**< (US_CSR) Break Received/End of Break (cleared by writing a one to the bit US_CR.RSTSTA) Position */
#define US_CSR_RXBRK_Msk                      (0x1U << US_CSR_RXBRK_Pos)                     /**< (US_CSR) Break Received/End of Break (cleared by writing a one to the bit US_CR.RSTSTA) Mask */
#define US_CSR_RXBRK(value)                   (US_CSR_RXBRK_Msk & ((value) << US_CSR_RXBRK_Pos))
#define US_CSR_ENDRX_Pos                      (3U)                                           /**< (US_CSR) End of RX Buffer (cleared by writing US_RCR or US_RNCR) Position */
#define US_CSR_ENDRX_Msk                      (0x1U << US_CSR_ENDRX_Pos)                     /**< (US_CSR) End of RX Buffer (cleared by writing US_RCR or US_RNCR) Mask */
#define US_CSR_ENDRX(value)                   (US_CSR_ENDRX_Msk & ((value) << US_CSR_ENDRX_Pos))
#define US_CSR_ENDTX_Pos                      (4U)                                           /**< (US_CSR) End of TX Buffer (cleared by writing US_TCR or US_TNCR) Position */
#define US_CSR_ENDTX_Msk                      (0x1U << US_CSR_ENDTX_Pos)                     /**< (US_CSR) End of TX Buffer (cleared by writing US_TCR or US_TNCR) Mask */
#define US_CSR_ENDTX(value)                   (US_CSR_ENDTX_Msk & ((value) << US_CSR_ENDTX_Pos))
#define US_CSR_OVRE_Pos                       (5U)                                           /**< (US_CSR) Overrun Error (cleared by writing a one to the bit US_CR.RSTSTA) Position */
#define US_CSR_OVRE_Msk                       (0x1U << US_CSR_OVRE_Pos)                      /**< (US_CSR) Overrun Error (cleared by writing a one to the bit US_CR.RSTSTA) Mask */
#define US_CSR_OVRE(value)                    (US_CSR_OVRE_Msk & ((value) << US_CSR_OVRE_Pos))
#define US_CSR_FRAME_Pos                      (6U)                                           /**< (US_CSR) Framing Error (cleared by writing a one to the bit US_CR.RSTSTA) Position */
#define US_CSR_FRAME_Msk                      (0x1U << US_CSR_FRAME_Pos)                     /**< (US_CSR) Framing Error (cleared by writing a one to the bit US_CR.RSTSTA) Mask */
#define US_CSR_FRAME(value)                   (US_CSR_FRAME_Msk & ((value) << US_CSR_FRAME_Pos))
#define US_CSR_PARE_Pos                       (7U)                                           /**< (US_CSR) Parity Error (cleared by writing a one to the US_CR.RSTSTA) Position */
#define US_CSR_PARE_Msk                       (0x1U << US_CSR_PARE_Pos)                      /**< (US_CSR) Parity Error (cleared by writing a one to the US_CR.RSTSTA) Mask */
#define US_CSR_PARE(value)                    (US_CSR_PARE_Msk & ((value) << US_CSR_PARE_Pos))
#define US_CSR_TIMEOUT_Pos                    (8U)                                           /**< (US_CSR) Receiver Time-out (cleared by writing a one to the bit US_CR.STTTO) Position */
#define US_CSR_TIMEOUT_Msk                    (0x1U << US_CSR_TIMEOUT_Pos)                   /**< (US_CSR) Receiver Time-out (cleared by writing a one to the bit US_CR.STTTO) Mask */
#define US_CSR_TIMEOUT(value)                 (US_CSR_TIMEOUT_Msk & ((value) << US_CSR_TIMEOUT_Pos))
#define US_CSR_TXEMPTY_Pos                    (9U)                                           /**< (US_CSR) Transmitter Empty (cleared by writing US_THR) Position */
#define US_CSR_TXEMPTY_Msk                    (0x1U << US_CSR_TXEMPTY_Pos)                   /**< (US_CSR) Transmitter Empty (cleared by writing US_THR) Mask */
#define US_CSR_TXEMPTY(value)                 (US_CSR_TXEMPTY_Msk & ((value) << US_CSR_TXEMPTY_Pos))
#define US_CSR_ITER_Pos                       (10U)                                          /**< (US_CSR) Max Number of Repetitions Reached (cleared by writing a one to the bit US_CR.RSTIT) Position */
#define US_CSR_ITER_Msk                       (0x1U << US_CSR_ITER_Pos)                      /**< (US_CSR) Max Number of Repetitions Reached (cleared by writing a one to the bit US_CR.RSTIT) Mask */
#define US_CSR_ITER(value)                    (US_CSR_ITER_Msk & ((value) << US_CSR_ITER_Pos))
#define US_CSR_TXBUFE_Pos                     (11U)                                          /**< (US_CSR) TX Buffer Empty (cleared by writing US_TCR or US_TNCR) Position */
#define US_CSR_TXBUFE_Msk                     (0x1U << US_CSR_TXBUFE_Pos)                    /**< (US_CSR) TX Buffer Empty (cleared by writing US_TCR or US_TNCR) Mask */
#define US_CSR_TXBUFE(value)                  (US_CSR_TXBUFE_Msk & ((value) << US_CSR_TXBUFE_Pos))
#define US_CSR_RXBUFF_Pos                     (12U)                                          /**< (US_CSR) RX Buffer Full (cleared by writing US_RCR or US_RNCR) Position */
#define US_CSR_RXBUFF_Msk                     (0x1U << US_CSR_RXBUFF_Pos)                    /**< (US_CSR) RX Buffer Full (cleared by writing US_RCR or US_RNCR) Mask */
#define US_CSR_RXBUFF(value)                  (US_CSR_RXBUFF_Msk & ((value) << US_CSR_RXBUFF_Pos))
#define US_CSR_NACK_Pos                       (13U)                                          /**< (US_CSR) Non Acknowledge Interrupt (cleared by writing a one to the bit US_CR.RSTNACK) Position */
#define US_CSR_NACK_Msk                       (0x1U << US_CSR_NACK_Pos)                      /**< (US_CSR) Non Acknowledge Interrupt (cleared by writing a one to the bit US_CR.RSTNACK) Mask */
#define US_CSR_NACK(value)                    (US_CSR_NACK_Msk & ((value) << US_CSR_NACK_Pos))
#define US_CSR_CTSIC_Pos                      (19U)                                          /**< (US_CSR) Clear to Send Input Change Flag (cleared on read) Position */
#define US_CSR_CTSIC_Msk                      (0x1U << US_CSR_CTSIC_Pos)                     /**< (US_CSR) Clear to Send Input Change Flag (cleared on read) Mask */
#define US_CSR_CTSIC(value)                   (US_CSR_CTSIC_Msk & ((value) << US_CSR_CTSIC_Pos))
#define US_CSR_CMP_Pos                        (22U)                                          /**< (US_CSR) Comparison Status (cleared by writing a one to the bit US_CR.RSTSTA command) Position */
#define US_CSR_CMP_Msk                        (0x1U << US_CSR_CMP_Pos)                       /**< (US_CSR) Comparison Status (cleared by writing a one to the bit US_CR.RSTSTA command) Mask */
#define US_CSR_CMP(value)                     (US_CSR_CMP_Msk & ((value) << US_CSR_CMP_Pos))
#define US_CSR_CTS_Pos                        (23U)                                          /**< (US_CSR) Image of CTS Input Position */
#define US_CSR_CTS_Msk                        (0x1U << US_CSR_CTS_Pos)                       /**< (US_CSR) Image of CTS Input Mask */
#define US_CSR_CTS(value)                     (US_CSR_CTS_Msk & ((value) << US_CSR_CTS_Pos))
#define US_CSR_Msk                            (0x00C83FFFUL)                                 /**< (US_CSR) Register Mask  */

/* -------- US_RHR : (USART Offset: 0x18) (R/  32) Receive Holding Register -------- */
#define US_RHR_RXCHR_Pos                      (0U)                                           /**< (US_RHR) Received Character Position */
#define US_RHR_RXCHR_Msk                      (0x1FFU << US_RHR_RXCHR_Pos)                   /**< (US_RHR) Received Character Mask */
#define US_RHR_RXCHR(value)                   (US_RHR_RXCHR_Msk & ((value) << US_RHR_RXCHR_Pos))
#define US_RHR_RXSYNH_Pos                     (15U)                                          /**< (US_RHR) Received Sync Position */
#define US_RHR_RXSYNH_Msk                     (0x1U << US_RHR_RXSYNH_Pos)                    /**< (US_RHR) Received Sync Mask */
#define US_RHR_RXSYNH(value)                  (US_RHR_RXSYNH_Msk & ((value) << US_RHR_RXSYNH_Pos))
#define US_RHR_Msk                            (0x000081FFUL)                                 /**< (US_RHR) Register Mask  */

/* -------- US_THR : (USART Offset: 0x1C) ( /W 32) Transmit Holding Register -------- */
#define US_THR_TXCHR_Pos                      (0U)                                           /**< (US_THR) Character to be Transmitted Position */
#define US_THR_TXCHR_Msk                      (0x1FFU << US_THR_TXCHR_Pos)                   /**< (US_THR) Character to be Transmitted Mask */
#define US_THR_TXCHR(value)                   (US_THR_TXCHR_Msk & ((value) << US_THR_TXCHR_Pos))
#define US_THR_TXSYNH_Pos                     (15U)                                          /**< (US_THR) Sync Field to be Transmitted Position */
#define US_THR_TXSYNH_Msk                     (0x1U << US_THR_TXSYNH_Pos)                    /**< (US_THR) Sync Field to be Transmitted Mask */
#define US_THR_TXSYNH(value)                  (US_THR_TXSYNH_Msk & ((value) << US_THR_TXSYNH_Pos))
#define US_THR_Msk                            (0x000081FFUL)                                 /**< (US_THR) Register Mask  */

/* -------- US_BRGR : (USART Offset: 0x20) (R/W 32) Baud Rate Generator Register -------- */
#define US_BRGR_CD_Pos                        (0U)                                           /**< (US_BRGR) Clock Divider Position */
#define US_BRGR_CD_Msk                        (0xFFFFU << US_BRGR_CD_Pos)                    /**< (US_BRGR) Clock Divider Mask */
#define US_BRGR_CD(value)                     (US_BRGR_CD_Msk & ((value) << US_BRGR_CD_Pos))
#define US_BRGR_FP_Pos                        (16U)                                          /**< (US_BRGR) Fractional Part Position */
#define US_BRGR_FP_Msk                        (0x7U << US_BRGR_FP_Pos)                       /**< (US_BRGR) Fractional Part Mask */
#define US_BRGR_FP(value)                     (US_BRGR_FP_Msk & ((value) << US_BRGR_FP_Pos))
#define US_BRGR_Msk                           (0x0007FFFFUL)                                 /**< (US_BRGR) Register Mask  */

/* -------- US_RTOR : (USART Offset: 0x24) (R/W 32) Receiver Time-out Register -------- */
#define US_RTOR_TO_Pos                        (0U)                                           /**< (US_RTOR) Time-out Value Position */
#define US_RTOR_TO_Msk                        (0x1FFFFU << US_RTOR_TO_Pos)                   /**< (US_RTOR) Time-out Value Mask */
#define US_RTOR_TO(value)                     (US_RTOR_TO_Msk & ((value) << US_RTOR_TO_Pos))
#define US_RTOR_Msk                           (0x0001FFFFUL)                                 /**< (US_RTOR) Register Mask  */

/* -------- US_TTGR : (USART Offset: 0x28) (R/W 32) Transmitter Timeguard Register -------- */
#define US_TTGR_TG_Pos                        (0U)                                           /**< (US_TTGR) Timeguard Value Position */
#define US_TTGR_TG_Msk                        (0xFFU << US_TTGR_TG_Pos)                      /**< (US_TTGR) Timeguard Value Mask */
#define US_TTGR_TG(value)                     (US_TTGR_TG_Msk & ((value) << US_TTGR_TG_Pos))
#define US_TTGR_Msk                           (0x000000FFUL)                                 /**< (US_TTGR) Register Mask  */

/* -------- US_FIDI : (USART Offset: 0x40) (R/W 32) FI DI Ratio Register -------- */
#define US_FIDI_FI_DI_RATIO_Pos               (0U)                                           /**< (US_FIDI) FI Over DI Ratio Value Position */
#define US_FIDI_FI_DI_RATIO_Msk               (0xFFFFU << US_FIDI_FI_DI_RATIO_Pos)           /**< (US_FIDI) FI Over DI Ratio Value Mask */
#define US_FIDI_FI_DI_RATIO(value)            (US_FIDI_FI_DI_RATIO_Msk & ((value) << US_FIDI_FI_DI_RATIO_Pos))
#define US_FIDI_Msk                           (0x0000FFFFUL)                                 /**< (US_FIDI) Register Mask  */

/* -------- US_NER : (USART Offset: 0x44) (R/  32) Number of Errors Register -------- */
#define US_NER_NB_ERRORS_Pos                  (0U)                                           /**< (US_NER) Number of Errors Position */
#define US_NER_NB_ERRORS_Msk                  (0xFFU << US_NER_NB_ERRORS_Pos)                /**< (US_NER) Number of Errors Mask */
#define US_NER_NB_ERRORS(value)               (US_NER_NB_ERRORS_Msk & ((value) << US_NER_NB_ERRORS_Pos))
#define US_NER_Msk                            (0x000000FFUL)                                 /**< (US_NER) Register Mask  */

/* -------- US_IF : (USART Offset: 0x4C) (R/W 32) IrDA Filter Register -------- */
#define US_IF_IRDA_FILTER_Pos                 (0U)                                           /**< (US_IF) IrDA Filter Position */
#define US_IF_IRDA_FILTER_Msk                 (0xFFU << US_IF_IRDA_FILTER_Pos)               /**< (US_IF) IrDA Filter Mask */
#define US_IF_IRDA_FILTER(value)              (US_IF_IRDA_FILTER_Msk & ((value) << US_IF_IRDA_FILTER_Pos))
#define US_IF_Msk                             (0x000000FFUL)                                 /**< (US_IF) Register Mask  */

/* -------- US_LINMR : (USART Offset: 0x54) (R/W 32) LIN Mode Register -------- */
#define US_LINMR_NACT_Pos                     (0U)                                           /**< (US_LINMR) LIN Node Action Position */
#define US_LINMR_NACT_Msk                     (0x3U << US_LINMR_NACT_Pos)                    /**< (US_LINMR) LIN Node Action Mask */
#define US_LINMR_NACT(value)                  (US_LINMR_NACT_Msk & ((value) << US_LINMR_NACT_Pos))
#define   US_LINMR_NACT_PUBLISH_Val           (0U)                                           /**< (US_LINMR) The USART transmits the response.  */
#define   US_LINMR_NACT_SUBSCRIBE_Val         (1U)                                           /**< (US_LINMR) The USART receives the response.  */
#define   US_LINMR_NACT_IGNORE_Val            (2U)                                           /**< (US_LINMR) The USART does not transmit and does not receive the response.  */
#define US_LINMR_NACT_PUBLISH                 (US_LINMR_NACT_PUBLISH_Val << US_LINMR_NACT_Pos) /**< (US_LINMR) The USART transmits the response. Position  */
#define US_LINMR_NACT_SUBSCRIBE               (US_LINMR_NACT_SUBSCRIBE_Val << US_LINMR_NACT_Pos) /**< (US_LINMR) The USART receives the response. Position  */
#define US_LINMR_NACT_IGNORE                  (US_LINMR_NACT_IGNORE_Val << US_LINMR_NACT_Pos) /**< (US_LINMR) The USART does not transmit and does not receive the response. Position  */
#define US_LINMR_PARDIS_Pos                   (2U)                                           /**< (US_LINMR) Parity Disable Position */
#define US_LINMR_PARDIS_Msk                   (0x1U << US_LINMR_PARDIS_Pos)                  /**< (US_LINMR) Parity Disable Mask */
#define US_LINMR_PARDIS(value)                (US_LINMR_PARDIS_Msk & ((value) << US_LINMR_PARDIS_Pos))
#define US_LINMR_CHKDIS_Pos                   (3U)                                           /**< (US_LINMR) Checksum Disable Position */
#define US_LINMR_CHKDIS_Msk                   (0x1U << US_LINMR_CHKDIS_Pos)                  /**< (US_LINMR) Checksum Disable Mask */
#define US_LINMR_CHKDIS(value)                (US_LINMR_CHKDIS_Msk & ((value) << US_LINMR_CHKDIS_Pos))
#define US_LINMR_CHKTYP_Pos                   (4U)                                           /**< (US_LINMR) Checksum Type Position */
#define US_LINMR_CHKTYP_Msk                   (0x1U << US_LINMR_CHKTYP_Pos)                  /**< (US_LINMR) Checksum Type Mask */
#define US_LINMR_CHKTYP(value)                (US_LINMR_CHKTYP_Msk & ((value) << US_LINMR_CHKTYP_Pos))
#define US_LINMR_DLM_Pos                      (5U)                                           /**< (US_LINMR) Data Length Mode Position */
#define US_LINMR_DLM_Msk                      (0x1U << US_LINMR_DLM_Pos)                     /**< (US_LINMR) Data Length Mode Mask */
#define US_LINMR_DLM(value)                   (US_LINMR_DLM_Msk & ((value) << US_LINMR_DLM_Pos))
#define US_LINMR_FSDIS_Pos                    (6U)                                           /**< (US_LINMR) Frame Slot Mode Disable Position */
#define US_LINMR_FSDIS_Msk                    (0x1U << US_LINMR_FSDIS_Pos)                   /**< (US_LINMR) Frame Slot Mode Disable Mask */
#define US_LINMR_FSDIS(value)                 (US_LINMR_FSDIS_Msk & ((value) << US_LINMR_FSDIS_Pos))
#define US_LINMR_WKUPTYP_Pos                  (7U)                                           /**< (US_LINMR) Wakeup Signal Type Position */
#define US_LINMR_WKUPTYP_Msk                  (0x1U << US_LINMR_WKUPTYP_Pos)                 /**< (US_LINMR) Wakeup Signal Type Mask */
#define US_LINMR_WKUPTYP(value)               (US_LINMR_WKUPTYP_Msk & ((value) << US_LINMR_WKUPTYP_Pos))
#define US_LINMR_DLC_Pos                      (8U)                                           /**< (US_LINMR) Data Length Control Position */
#define US_LINMR_DLC_Msk                      (0xFFU << US_LINMR_DLC_Pos)                    /**< (US_LINMR) Data Length Control Mask */
#define US_LINMR_DLC(value)                   (US_LINMR_DLC_Msk & ((value) << US_LINMR_DLC_Pos))
#define US_LINMR_PDCM_Pos                     (16U)                                          /**< (US_LINMR) PDC Mode Position */
#define US_LINMR_PDCM_Msk                     (0x1U << US_LINMR_PDCM_Pos)                    /**< (US_LINMR) PDC Mode Mask */
#define US_LINMR_PDCM(value)                  (US_LINMR_PDCM_Msk & ((value) << US_LINMR_PDCM_Pos))
#define US_LINMR_SYNCDIS_Pos                  (17U)                                          /**< (US_LINMR) Synchronization Disable Position */
#define US_LINMR_SYNCDIS_Msk                  (0x1U << US_LINMR_SYNCDIS_Pos)                 /**< (US_LINMR) Synchronization Disable Mask */
#define US_LINMR_SYNCDIS(value)               (US_LINMR_SYNCDIS_Msk & ((value) << US_LINMR_SYNCDIS_Pos))
#define US_LINMR_Msk                          (0x0003FFFFUL)                                 /**< (US_LINMR) Register Mask  */

/* -------- US_LINIR : (USART Offset: 0x58) (R/W 32) LIN Identifier Register -------- */
#define US_LINIR_IDCHR_Pos                    (0U)                                           /**< (US_LINIR) Identifier Character Position */
#define US_LINIR_IDCHR_Msk                    (0xFFU << US_LINIR_IDCHR_Pos)                  /**< (US_LINIR) Identifier Character Mask */
#define US_LINIR_IDCHR(value)                 (US_LINIR_IDCHR_Msk & ((value) << US_LINIR_IDCHR_Pos))
#define US_LINIR_Msk                          (0x000000FFUL)                                 /**< (US_LINIR) Register Mask  */

/* -------- US_LINBRR : (USART Offset: 0x5C) (R/  32) LIN Baud Rate Register -------- */
#define US_LINBRR_LINCD_Pos                   (0U)                                           /**< (US_LINBRR) Clock Divider after Synchronization Position */
#define US_LINBRR_LINCD_Msk                   (0xFFFFU << US_LINBRR_LINCD_Pos)               /**< (US_LINBRR) Clock Divider after Synchronization Mask */
#define US_LINBRR_LINCD(value)                (US_LINBRR_LINCD_Msk & ((value) << US_LINBRR_LINCD_Pos))
#define US_LINBRR_LINFP_Pos                   (16U)                                          /**< (US_LINBRR) Fractional Part after Synchronization Position */
#define US_LINBRR_LINFP_Msk                   (0x7U << US_LINBRR_LINFP_Pos)                  /**< (US_LINBRR) Fractional Part after Synchronization Mask */
#define US_LINBRR_LINFP(value)                (US_LINBRR_LINFP_Msk & ((value) << US_LINBRR_LINFP_Pos))
#define US_LINBRR_Msk                         (0x0007FFFFUL)                                 /**< (US_LINBRR) Register Mask  */

/* -------- US_CMPR : (USART Offset: 0x90) (R/W 32) Comparison Register -------- */
#define US_CMPR_VAL1_Pos                      (0U)                                           /**< (US_CMPR) First Comparison Value for Received Character Position */
#define US_CMPR_VAL1_Msk                      (0x1FFU << US_CMPR_VAL1_Pos)                   /**< (US_CMPR) First Comparison Value for Received Character Mask */
#define US_CMPR_VAL1(value)                   (US_CMPR_VAL1_Msk & ((value) << US_CMPR_VAL1_Pos))
#define US_CMPR_CMPMODE_Pos                   (12U)                                          /**< (US_CMPR) Comparison Mode Position */
#define US_CMPR_CMPMODE_Msk                   (0x1U << US_CMPR_CMPMODE_Pos)                  /**< (US_CMPR) Comparison Mode Mask */
#define US_CMPR_CMPMODE(value)                (US_CMPR_CMPMODE_Msk & ((value) << US_CMPR_CMPMODE_Pos))
#define   US_CMPR_CMPMODE_FLAG_ONLY_Val       (0U)                                           /**< (US_CMPR) Any character is received and comparison function drives CMP flag.  */
#define   US_CMPR_CMPMODE_START_CONDITION_Val (1U)                                           /**< (US_CMPR) Comparison condition must be met to start reception of all incoming charactersuntil REQCLR is set.  */
#define US_CMPR_CMPMODE_FLAG_ONLY             (US_CMPR_CMPMODE_FLAG_ONLY_Val << US_CMPR_CMPMODE_Pos) /**< (US_CMPR) Any character is received and comparison function drives CMP flag. Position  */
#define US_CMPR_CMPMODE_START_CONDITION       (US_CMPR_CMPMODE_START_CONDITION_Val << US_CMPR_CMPMODE_Pos) /**< (US_CMPR) Comparison condition must be met to start reception of all incoming charactersuntil REQCLR is set. Position  */
#define US_CMPR_CMPPAR_Pos                    (14U)                                          /**< (US_CMPR) Compare Parity Position */
#define US_CMPR_CMPPAR_Msk                    (0x1U << US_CMPR_CMPPAR_Pos)                   /**< (US_CMPR) Compare Parity Mask */
#define US_CMPR_CMPPAR(value)                 (US_CMPR_CMPPAR_Msk & ((value) << US_CMPR_CMPPAR_Pos))
#define US_CMPR_VAL2_Pos                      (16U)                                          /**< (US_CMPR) Second Comparison Value for Received Character Position */
#define US_CMPR_VAL2_Msk                      (0x1FFU << US_CMPR_VAL2_Pos)                   /**< (US_CMPR) Second Comparison Value for Received Character Mask */
#define US_CMPR_VAL2(value)                   (US_CMPR_VAL2_Msk & ((value) << US_CMPR_VAL2_Pos))
#define US_CMPR_Msk                           (0x01FF51FFUL)                                 /**< (US_CMPR) Register Mask  */

/* -------- US_WPMR : (USART Offset: 0xE4) (R/W 32) Write Protection Mode Register -------- */
#define US_WPMR_WPEN_Pos                      (0U)                                           /**< (US_WPMR) Write Protection Enable Position */
#define US_WPMR_WPEN_Msk                      (0x1U << US_WPMR_WPEN_Pos)                     /**< (US_WPMR) Write Protection Enable Mask */
#define US_WPMR_WPEN(value)                   (US_WPMR_WPEN_Msk & ((value) << US_WPMR_WPEN_Pos))
#define US_WPMR_WPKEY_Pos                     (8U)                                           /**< (US_WPMR) Write Protection Key Position */
#define US_WPMR_WPKEY_Msk                     (0xFFFFFFU << US_WPMR_WPKEY_Pos)               /**< (US_WPMR) Write Protection Key Mask */
#define US_WPMR_WPKEY(value)                  (US_WPMR_WPKEY_Msk & ((value) << US_WPMR_WPKEY_Pos))
#define   US_WPMR_WPKEY_PASSWD_Val            (5591873U)                                     /**< (US_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit. Always reads as 0.  */
#define US_WPMR_WPKEY_PASSWD                  (US_WPMR_WPKEY_PASSWD_Val << US_WPMR_WPKEY_Pos) /**< (US_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit. Always reads as 0. Position  */
#define US_WPMR_Msk                           (0xFFFFFF01UL)                                 /**< (US_WPMR) Register Mask  */

/* -------- US_WPSR : (USART Offset: 0xE8) (R/  32) Write Protection Status Register -------- */
#define US_WPSR_WPVS_Pos                      (0U)                                           /**< (US_WPSR) Write Protection Violation Status Position */
#define US_WPSR_WPVS_Msk                      (0x1U << US_WPSR_WPVS_Pos)                     /**< (US_WPSR) Write Protection Violation Status Mask */
#define US_WPSR_WPVS(value)                   (US_WPSR_WPVS_Msk & ((value) << US_WPSR_WPVS_Pos))
#define US_WPSR_WPVSRC_Pos                    (8U)                                           /**< (US_WPSR) Write Protection Violation Source Position */
#define US_WPSR_WPVSRC_Msk                    (0xFFFFU << US_WPSR_WPVSRC_Pos)                /**< (US_WPSR) Write Protection Violation Source Mask */
#define US_WPSR_WPVSRC(value)                 (US_WPSR_WPVSRC_Msk & ((value) << US_WPSR_WPVSRC_Pos))
#define US_WPSR_Msk                           (0x00FFFF01UL)                                 /**< (US_WPSR) Register Mask  */

/* -------- US_RPR : (USART Offset: 0x100) (R/W 32) Receive Pointer Register -------- */
#define US_RPR_RXPTR_Pos                      (0U)                                           /**< (US_RPR) Receive Pointer Register Position */
#define US_RPR_RXPTR_Msk                      (0xFFFFFFFFU << US_RPR_RXPTR_Pos)              /**< (US_RPR) Receive Pointer Register Mask */
#define US_RPR_RXPTR(value)                   (US_RPR_RXPTR_Msk & ((value) << US_RPR_RXPTR_Pos))
#define US_RPR_Msk                            (0xFFFFFFFFUL)                                 /**< (US_RPR) Register Mask  */

/* -------- US_RCR : (USART Offset: 0x104) (R/W 32) Receive Counter Register -------- */
#define US_RCR_RXCTR_Pos                      (0U)                                           /**< (US_RCR) Receive Counter Register Position */
#define US_RCR_RXCTR_Msk                      (0xFFFFU << US_RCR_RXCTR_Pos)                  /**< (US_RCR) Receive Counter Register Mask */
#define US_RCR_RXCTR(value)                   (US_RCR_RXCTR_Msk & ((value) << US_RCR_RXCTR_Pos))
#define US_RCR_Msk                            (0x0000FFFFUL)                                 /**< (US_RCR) Register Mask  */

/* -------- US_TPR : (USART Offset: 0x108) (R/W 32) Transmit Pointer Register -------- */
#define US_TPR_TXPTR_Pos                      (0U)                                           /**< (US_TPR) Transmit Counter Register Position */
#define US_TPR_TXPTR_Msk                      (0xFFFFFFFFU << US_TPR_TXPTR_Pos)              /**< (US_TPR) Transmit Counter Register Mask */
#define US_TPR_TXPTR(value)                   (US_TPR_TXPTR_Msk & ((value) << US_TPR_TXPTR_Pos))
#define US_TPR_Msk                            (0xFFFFFFFFUL)                                 /**< (US_TPR) Register Mask  */

/* -------- US_TCR : (USART Offset: 0x10C) (R/W 32) Transmit Counter Register -------- */
#define US_TCR_TXCTR_Pos                      (0U)                                           /**< (US_TCR) Transmit Counter Register Position */
#define US_TCR_TXCTR_Msk                      (0xFFFFU << US_TCR_TXCTR_Pos)                  /**< (US_TCR) Transmit Counter Register Mask */
#define US_TCR_TXCTR(value)                   (US_TCR_TXCTR_Msk & ((value) << US_TCR_TXCTR_Pos))
#define US_TCR_Msk                            (0x0000FFFFUL)                                 /**< (US_TCR) Register Mask  */

/* -------- US_RNPR : (USART Offset: 0x110) (R/W 32) Receive Next Pointer Register -------- */
#define US_RNPR_RXNPTR_Pos                    (0U)                                           /**< (US_RNPR) Receive Next Pointer Position */
#define US_RNPR_RXNPTR_Msk                    (0xFFFFFFFFU << US_RNPR_RXNPTR_Pos)            /**< (US_RNPR) Receive Next Pointer Mask */
#define US_RNPR_RXNPTR(value)                 (US_RNPR_RXNPTR_Msk & ((value) << US_RNPR_RXNPTR_Pos))
#define US_RNPR_Msk                           (0xFFFFFFFFUL)                                 /**< (US_RNPR) Register Mask  */

/* -------- US_RNCR : (USART Offset: 0x114) (R/W 32) Receive Next Counter Register -------- */
#define US_RNCR_RXNCTR_Pos                    (0U)                                           /**< (US_RNCR) Receive Next Counter Position */
#define US_RNCR_RXNCTR_Msk                    (0xFFFFU << US_RNCR_RXNCTR_Pos)                /**< (US_RNCR) Receive Next Counter Mask */
#define US_RNCR_RXNCTR(value)                 (US_RNCR_RXNCTR_Msk & ((value) << US_RNCR_RXNCTR_Pos))
#define US_RNCR_Msk                           (0x0000FFFFUL)                                 /**< (US_RNCR) Register Mask  */

/* -------- US_TNPR : (USART Offset: 0x118) (R/W 32) Transmit Next Pointer Register -------- */
#define US_TNPR_TXNPTR_Pos                    (0U)                                           /**< (US_TNPR) Transmit Next Pointer Position */
#define US_TNPR_TXNPTR_Msk                    (0xFFFFFFFFU << US_TNPR_TXNPTR_Pos)            /**< (US_TNPR) Transmit Next Pointer Mask */
#define US_TNPR_TXNPTR(value)                 (US_TNPR_TXNPTR_Msk & ((value) << US_TNPR_TXNPTR_Pos))
#define US_TNPR_Msk                           (0xFFFFFFFFUL)                                 /**< (US_TNPR) Register Mask  */

/* -------- US_TNCR : (USART Offset: 0x11C) (R/W 32) Transmit Next Counter Register -------- */
#define US_TNCR_TXNCTR_Pos                    (0U)                                           /**< (US_TNCR) Transmit Counter Next Position */
#define US_TNCR_TXNCTR_Msk                    (0xFFFFU << US_TNCR_TXNCTR_Pos)                /**< (US_TNCR) Transmit Counter Next Mask */
#define US_TNCR_TXNCTR(value)                 (US_TNCR_TXNCTR_Msk & ((value) << US_TNCR_TXNCTR_Pos))
#define US_TNCR_Msk                           (0x0000FFFFUL)                                 /**< (US_TNCR) Register Mask  */

/* -------- US_PTCR : (USART Offset: 0x120) ( /W 32) Transfer Control Register -------- */
#define US_PTCR_RXTEN_Pos                     (0U)                                           /**< (US_PTCR) Receiver Transfer Enable Position */
#define US_PTCR_RXTEN_Msk                     (0x1U << US_PTCR_RXTEN_Pos)                    /**< (US_PTCR) Receiver Transfer Enable Mask */
#define US_PTCR_RXTEN(value)                  (US_PTCR_RXTEN_Msk & ((value) << US_PTCR_RXTEN_Pos))
#define US_PTCR_RXTDIS_Pos                    (1U)                                           /**< (US_PTCR) Receiver Transfer Disable Position */
#define US_PTCR_RXTDIS_Msk                    (0x1U << US_PTCR_RXTDIS_Pos)                   /**< (US_PTCR) Receiver Transfer Disable Mask */
#define US_PTCR_RXTDIS(value)                 (US_PTCR_RXTDIS_Msk & ((value) << US_PTCR_RXTDIS_Pos))
#define US_PTCR_TXTEN_Pos                     (8U)                                           /**< (US_PTCR) Transmitter Transfer Enable Position */
#define US_PTCR_TXTEN_Msk                     (0x1U << US_PTCR_TXTEN_Pos)                    /**< (US_PTCR) Transmitter Transfer Enable Mask */
#define US_PTCR_TXTEN(value)                  (US_PTCR_TXTEN_Msk & ((value) << US_PTCR_TXTEN_Pos))
#define US_PTCR_TXTDIS_Pos                    (9U)                                           /**< (US_PTCR) Transmitter Transfer Disable Position */
#define US_PTCR_TXTDIS_Msk                    (0x1U << US_PTCR_TXTDIS_Pos)                   /**< (US_PTCR) Transmitter Transfer Disable Mask */
#define US_PTCR_TXTDIS(value)                 (US_PTCR_TXTDIS_Msk & ((value) << US_PTCR_TXTDIS_Pos))
#define US_PTCR_RXCBEN_Pos                    (16U)                                          /**< (US_PTCR) Receiver Circular Buffer Enable Position */
#define US_PTCR_RXCBEN_Msk                    (0x1U << US_PTCR_RXCBEN_Pos)                   /**< (US_PTCR) Receiver Circular Buffer Enable Mask */
#define US_PTCR_RXCBEN(value)                 (US_PTCR_RXCBEN_Msk & ((value) << US_PTCR_RXCBEN_Pos))
#define US_PTCR_RXCBDIS_Pos                   (17U)                                          /**< (US_PTCR) Receiver Circular Buffer Disable Position */
#define US_PTCR_RXCBDIS_Msk                   (0x1U << US_PTCR_RXCBDIS_Pos)                  /**< (US_PTCR) Receiver Circular Buffer Disable Mask */
#define US_PTCR_RXCBDIS(value)                (US_PTCR_RXCBDIS_Msk & ((value) << US_PTCR_RXCBDIS_Pos))
#define US_PTCR_TXCBEN_Pos                    (18U)                                          /**< (US_PTCR) Transmitter Circular Buffer Enable Position */
#define US_PTCR_TXCBEN_Msk                    (0x1U << US_PTCR_TXCBEN_Pos)                   /**< (US_PTCR) Transmitter Circular Buffer Enable Mask */
#define US_PTCR_TXCBEN(value)                 (US_PTCR_TXCBEN_Msk & ((value) << US_PTCR_TXCBEN_Pos))
#define US_PTCR_TXCBDIS_Pos                   (19U)                                          /**< (US_PTCR) Transmitter Circular Buffer Disable Position */
#define US_PTCR_TXCBDIS_Msk                   (0x1U << US_PTCR_TXCBDIS_Pos)                  /**< (US_PTCR) Transmitter Circular Buffer Disable Mask */
#define US_PTCR_TXCBDIS(value)                (US_PTCR_TXCBDIS_Msk & ((value) << US_PTCR_TXCBDIS_Pos))
#define US_PTCR_ERRCLR_Pos                    (24U)                                          /**< (US_PTCR) Transfer Bus Error Clear Position */
#define US_PTCR_ERRCLR_Msk                    (0x1U << US_PTCR_ERRCLR_Pos)                   /**< (US_PTCR) Transfer Bus Error Clear Mask */
#define US_PTCR_ERRCLR(value)                 (US_PTCR_ERRCLR_Msk & ((value) << US_PTCR_ERRCLR_Pos))
#define US_PTCR_Msk                           (0x010F0303UL)                                 /**< (US_PTCR) Register Mask  */

/* -------- US_PTSR : (USART Offset: 0x124) (R/  32) Transfer Status Register -------- */
#define US_PTSR_RXTEN_Pos                     (0U)                                           /**< (US_PTSR) Receiver Transfer Enable Position */
#define US_PTSR_RXTEN_Msk                     (0x1U << US_PTSR_RXTEN_Pos)                    /**< (US_PTSR) Receiver Transfer Enable Mask */
#define US_PTSR_RXTEN(value)                  (US_PTSR_RXTEN_Msk & ((value) << US_PTSR_RXTEN_Pos))
#define US_PTSR_TXTEN_Pos                     (8U)                                           /**< (US_PTSR) Transmitter Transfer Enable Position */
#define US_PTSR_TXTEN_Msk                     (0x1U << US_PTSR_TXTEN_Pos)                    /**< (US_PTSR) Transmitter Transfer Enable Mask */
#define US_PTSR_TXTEN(value)                  (US_PTSR_TXTEN_Msk & ((value) << US_PTSR_TXTEN_Pos))
#define US_PTSR_RXCBEN_Pos                    (16U)                                          /**< (US_PTSR) Receiver Circular Buffer Enable Position */
#define US_PTSR_RXCBEN_Msk                    (0x1U << US_PTSR_RXCBEN_Pos)                   /**< (US_PTSR) Receiver Circular Buffer Enable Mask */
#define US_PTSR_RXCBEN(value)                 (US_PTSR_RXCBEN_Msk & ((value) << US_PTSR_RXCBEN_Pos))
#define US_PTSR_TXCBEN_Pos                    (18U)                                          /**< (US_PTSR) Transmitter Circular Buffer Enable Position */
#define US_PTSR_TXCBEN_Msk                    (0x1U << US_PTSR_TXCBEN_Pos)                   /**< (US_PTSR) Transmitter Circular Buffer Enable Mask */
#define US_PTSR_TXCBEN(value)                 (US_PTSR_TXCBEN_Msk & ((value) << US_PTSR_TXCBEN_Pos))
#define US_PTSR_ERR_Pos                       (24U)                                          /**< (US_PTSR) Transfer Bus Error Position */
#define US_PTSR_ERR_Msk                       (0x1U << US_PTSR_ERR_Pos)                      /**< (US_PTSR) Transfer Bus Error Mask */
#define US_PTSR_ERR(value)                    (US_PTSR_ERR_Msk & ((value) << US_PTSR_ERR_Pos))
#define US_PTSR_Msk                           (0x01050101UL)                                 /**< (US_PTSR) Register Mask  */

/** \brief USART register offsets definitions */
#define US_CR_OFFSET                   (0x00)         /**< (US_CR) Control Register Offset */
#define US_MR_OFFSET                   (0x04)         /**< (US_MR) Mode Register Offset */
#define US_IER_OFFSET                  (0x08)         /**< (US_IER) Interrupt Enable Register Offset */
#define US_IDR_OFFSET                  (0x0C)         /**< (US_IDR) Interrupt Disable Register Offset */
#define US_IMR_OFFSET                  (0x10)         /**< (US_IMR) Interrupt Mask Register Offset */
#define US_CSR_OFFSET                  (0x14)         /**< (US_CSR) Channel Status Register Offset */
#define US_RHR_OFFSET                  (0x18)         /**< (US_RHR) Receive Holding Register Offset */
#define US_THR_OFFSET                  (0x1C)         /**< (US_THR) Transmit Holding Register Offset */
#define US_BRGR_OFFSET                 (0x20)         /**< (US_BRGR) Baud Rate Generator Register Offset */
#define US_RTOR_OFFSET                 (0x24)         /**< (US_RTOR) Receiver Time-out Register Offset */
#define US_TTGR_OFFSET                 (0x28)         /**< (US_TTGR) Transmitter Timeguard Register Offset */
#define US_FIDI_OFFSET                 (0x40)         /**< (US_FIDI) FI DI Ratio Register Offset */
#define US_NER_OFFSET                  (0x44)         /**< (US_NER) Number of Errors Register Offset */
#define US_IF_OFFSET                   (0x4C)         /**< (US_IF) IrDA Filter Register Offset */
#define US_LINMR_OFFSET                (0x54)         /**< (US_LINMR) LIN Mode Register Offset */
#define US_LINIR_OFFSET                (0x58)         /**< (US_LINIR) LIN Identifier Register Offset */
#define US_LINBRR_OFFSET               (0x5C)         /**< (US_LINBRR) LIN Baud Rate Register Offset */
#define US_CMPR_OFFSET                 (0x90)         /**< (US_CMPR) Comparison Register Offset */
#define US_WPMR_OFFSET                 (0xE4)         /**< (US_WPMR) Write Protection Mode Register Offset */
#define US_WPSR_OFFSET                 (0xE8)         /**< (US_WPSR) Write Protection Status Register Offset */
#define US_RPR_OFFSET                  (0x100)        /**< (US_RPR) Receive Pointer Register Offset */
#define US_RCR_OFFSET                  (0x104)        /**< (US_RCR) Receive Counter Register Offset */
#define US_TPR_OFFSET                  (0x108)        /**< (US_TPR) Transmit Pointer Register Offset */
#define US_TCR_OFFSET                  (0x10C)        /**< (US_TCR) Transmit Counter Register Offset */
#define US_RNPR_OFFSET                 (0x110)        /**< (US_RNPR) Receive Next Pointer Register Offset */
#define US_RNCR_OFFSET                 (0x114)        /**< (US_RNCR) Receive Next Counter Register Offset */
#define US_TNPR_OFFSET                 (0x118)        /**< (US_TNPR) Transmit Next Pointer Register Offset */
#define US_TNCR_OFFSET                 (0x11C)        /**< (US_TNCR) Transmit Next Counter Register Offset */
#define US_PTCR_OFFSET                 (0x120)        /**< (US_PTCR) Transfer Control Register Offset */
#define US_PTSR_OFFSET                 (0x124)        /**< (US_PTSR) Transfer Status Register Offset */

/** \brief USART register API structure */
typedef struct
{
  __O   uint32_t                       US_CR;           /**< Offset: 0x00 ( /W  32) Control Register */
  __IO  uint32_t                       US_MR;           /**< Offset: 0x04 (R/W  32) Mode Register */
  __O   uint32_t                       US_IER;          /**< Offset: 0x08 ( /W  32) Interrupt Enable Register */
  __O   uint32_t                       US_IDR;          /**< Offset: 0x0c ( /W  32) Interrupt Disable Register */
  __I   uint32_t                       US_IMR;          /**< Offset: 0x10 (R/   32) Interrupt Mask Register */
  __I   uint32_t                       US_CSR;          /**< Offset: 0x14 (R/   32) Channel Status Register */
  __I   uint32_t                       US_RHR;          /**< Offset: 0x18 (R/   32) Receive Holding Register */
  __O   uint32_t                       US_THR;          /**< Offset: 0x1c ( /W  32) Transmit Holding Register */
  __IO  uint32_t                       US_BRGR;         /**< Offset: 0x20 (R/W  32) Baud Rate Generator Register */
  __IO  uint32_t                       US_RTOR;         /**< Offset: 0x24 (R/W  32) Receiver Time-out Register */
  __IO  uint32_t                       US_TTGR;         /**< Offset: 0x28 (R/W  32) Transmitter Timeguard Register */
  __I   uint8_t                        Reserved1[0x14];
  __IO  uint32_t                       US_FIDI;         /**< Offset: 0x40 (R/W  32) FI DI Ratio Register */
  __I   uint32_t                       US_NER;          /**< Offset: 0x44 (R/   32) Number of Errors Register */
  __I   uint8_t                        Reserved2[0x04];
  __IO  uint32_t                       US_IF;           /**< Offset: 0x4c (R/W  32) IrDA Filter Register */
  __I   uint8_t                        Reserved3[0x04];
  __IO  uint32_t                       US_LINMR;        /**< Offset: 0x54 (R/W  32) LIN Mode Register */
  __IO  uint32_t                       US_LINIR;        /**< Offset: 0x58 (R/W  32) LIN Identifier Register */
  __I   uint32_t                       US_LINBRR;       /**< Offset: 0x5c (R/   32) LIN Baud Rate Register */
  __I   uint8_t                        Reserved4[0x30];
  __IO  uint32_t                       US_CMPR;         /**< Offset: 0x90 (R/W  32) Comparison Register */
  __I   uint8_t                        Reserved5[0x50];
  __IO  uint32_t                       US_WPMR;         /**< Offset: 0xe4 (R/W  32) Write Protection Mode Register */
  __I   uint32_t                       US_WPSR;         /**< Offset: 0xe8 (R/   32) Write Protection Status Register */
  __I   uint8_t                        Reserved6[0x14];
  __IO  uint32_t                       US_RPR;          /**< Offset: 0x100 (R/W  32) Receive Pointer Register */
  __IO  uint32_t                       US_RCR;          /**< Offset: 0x104 (R/W  32) Receive Counter Register */
  __IO  uint32_t                       US_TPR;          /**< Offset: 0x108 (R/W  32) Transmit Pointer Register */
  __IO  uint32_t                       US_TCR;          /**< Offset: 0x10c (R/W  32) Transmit Counter Register */
  __IO  uint32_t                       US_RNPR;         /**< Offset: 0x110 (R/W  32) Receive Next Pointer Register */
  __IO  uint32_t                       US_RNCR;         /**< Offset: 0x114 (R/W  32) Receive Next Counter Register */
  __IO  uint32_t                       US_TNPR;         /**< Offset: 0x118 (R/W  32) Transmit Next Pointer Register */
  __IO  uint32_t                       US_TNCR;         /**< Offset: 0x11c (R/W  32) Transmit Next Counter Register */
  __O   uint32_t                       US_PTCR;         /**< Offset: 0x120 ( /W  32) Transfer Control Register */
  __I   uint32_t                       US_PTSR;         /**< Offset: 0x124 (R/   32) Transfer Status Register */
} usart_registers_t;
/** @}  end of Universal Synchronous Asynchronous Receiver Transmitter */

#endif /* SAMG_SAMG55_USART_MODULE_H */

