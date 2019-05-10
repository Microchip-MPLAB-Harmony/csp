/**
 * \brief Component description for DBGU
 *
 * Copyright (c) 2019 Microchip Technology Inc. and its subsidiaries.
 *
 * Subject to your compliance with these terms, you may use Microchip software and any derivatives
 * exclusively with Microchip products. It is your responsibility to comply with third party license
 * terms applicable to your use of third party software (including open source software) that may
 * accompany Microchip software.
 *
 * THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER EXPRESS, IMPLIED OR STATUTORY,
 * APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND
 * FITNESS FOR A PARTICULAR PURPOSE.
 *
 * IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, INCIDENTAL OR CONSEQUENTIAL
 * LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF
 * MICROCHIP HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE FULLEST EXTENT
 * ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN ANY WAY RELATED TO THIS SOFTWARE WILL NOT
 * EXCEED THE AMOUNT OF FEES, IF ANY, THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 *
 */

/* file generated from device description version 2019-04-23T19:01:17Z */
#ifndef _SAM9X_DBGU_COMPONENT_H_
#define _SAM9X_DBGU_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR DBGU                                         */
/* ************************************************************************** */

/* -------- DBGU_CR : (DBGU Offset: 0x00) ( /W 32) Control Register -------- */
#define DBGU_CR_RSTRX_Pos                     _U_(2)                                               /**< (DBGU_CR) Reset Receiver Position */
#define DBGU_CR_RSTRX_Msk                     (_U_(0x1) << DBGU_CR_RSTRX_Pos)                      /**< (DBGU_CR) Reset Receiver Mask */
#define DBGU_CR_RSTRX(value)                  (DBGU_CR_RSTRX_Msk & ((value) << DBGU_CR_RSTRX_Pos))
#define DBGU_CR_RSTTX_Pos                     _U_(3)                                               /**< (DBGU_CR) Reset Transmitter Position */
#define DBGU_CR_RSTTX_Msk                     (_U_(0x1) << DBGU_CR_RSTTX_Pos)                      /**< (DBGU_CR) Reset Transmitter Mask */
#define DBGU_CR_RSTTX(value)                  (DBGU_CR_RSTTX_Msk & ((value) << DBGU_CR_RSTTX_Pos))
#define DBGU_CR_RXEN_Pos                      _U_(4)                                               /**< (DBGU_CR) Receiver Enable Position */
#define DBGU_CR_RXEN_Msk                      (_U_(0x1) << DBGU_CR_RXEN_Pos)                       /**< (DBGU_CR) Receiver Enable Mask */
#define DBGU_CR_RXEN(value)                   (DBGU_CR_RXEN_Msk & ((value) << DBGU_CR_RXEN_Pos))  
#define DBGU_CR_RXDIS_Pos                     _U_(5)                                               /**< (DBGU_CR) Receiver Disable Position */
#define DBGU_CR_RXDIS_Msk                     (_U_(0x1) << DBGU_CR_RXDIS_Pos)                      /**< (DBGU_CR) Receiver Disable Mask */
#define DBGU_CR_RXDIS(value)                  (DBGU_CR_RXDIS_Msk & ((value) << DBGU_CR_RXDIS_Pos))
#define DBGU_CR_TXEN_Pos                      _U_(6)                                               /**< (DBGU_CR) Transmitter Enable Position */
#define DBGU_CR_TXEN_Msk                      (_U_(0x1) << DBGU_CR_TXEN_Pos)                       /**< (DBGU_CR) Transmitter Enable Mask */
#define DBGU_CR_TXEN(value)                   (DBGU_CR_TXEN_Msk & ((value) << DBGU_CR_TXEN_Pos))  
#define DBGU_CR_TXDIS_Pos                     _U_(7)                                               /**< (DBGU_CR) Transmitter Disable Position */
#define DBGU_CR_TXDIS_Msk                     (_U_(0x1) << DBGU_CR_TXDIS_Pos)                      /**< (DBGU_CR) Transmitter Disable Mask */
#define DBGU_CR_TXDIS(value)                  (DBGU_CR_TXDIS_Msk & ((value) << DBGU_CR_TXDIS_Pos))
#define DBGU_CR_RSTSTA_Pos                    _U_(8)                                               /**< (DBGU_CR) Reset Status Position */
#define DBGU_CR_RSTSTA_Msk                    (_U_(0x1) << DBGU_CR_RSTSTA_Pos)                     /**< (DBGU_CR) Reset Status Mask */
#define DBGU_CR_RSTSTA(value)                 (DBGU_CR_RSTSTA_Msk & ((value) << DBGU_CR_RSTSTA_Pos))
#define DBGU_CR_RETTO_Pos                     _U_(10)                                              /**< (DBGU_CR) Rearm Timeout Position */
#define DBGU_CR_RETTO_Msk                     (_U_(0x1) << DBGU_CR_RETTO_Pos)                      /**< (DBGU_CR) Rearm Timeout Mask */
#define DBGU_CR_RETTO(value)                  (DBGU_CR_RETTO_Msk & ((value) << DBGU_CR_RETTO_Pos))
#define DBGU_CR_STTTO_Pos                     _U_(11)                                              /**< (DBGU_CR) Start Timeout Position */
#define DBGU_CR_STTTO_Msk                     (_U_(0x1) << DBGU_CR_STTTO_Pos)                      /**< (DBGU_CR) Start Timeout Mask */
#define DBGU_CR_STTTO(value)                  (DBGU_CR_STTTO_Msk & ((value) << DBGU_CR_STTTO_Pos))
#define DBGU_CR_DBGE_Pos                      _U_(15)                                              /**< (DBGU_CR) Debug Enable Position */
#define DBGU_CR_DBGE_Msk                      (_U_(0x1) << DBGU_CR_DBGE_Pos)                       /**< (DBGU_CR) Debug Enable Mask */
#define DBGU_CR_DBGE(value)                   (DBGU_CR_DBGE_Msk & ((value) << DBGU_CR_DBGE_Pos))  
#define DBGU_CR_Msk                           _U_(0x00008DFC)                                      /**< (DBGU_CR) Register Mask  */


/* -------- DBGU_MR : (DBGU Offset: 0x04) (R/W 32) Mode Register -------- */
#define DBGU_MR_FILTER_Pos                    _U_(4)                                               /**< (DBGU_MR) Receiver Digital Filter Position */
#define DBGU_MR_FILTER_Msk                    (_U_(0x1) << DBGU_MR_FILTER_Pos)                     /**< (DBGU_MR) Receiver Digital Filter Mask */
#define DBGU_MR_FILTER(value)                 (DBGU_MR_FILTER_Msk & ((value) << DBGU_MR_FILTER_Pos))
#define   DBGU_MR_FILTER_DISABLED_Val         _U_(0x0)                                             /**< (DBGU_MR) DBGU does not filter the receive line.  */
#define   DBGU_MR_FILTER_ENABLED_Val          _U_(0x1)                                             /**< (DBGU_MR) DBGU filters the receive line using a three-sample filter (16x-bit clock) (2 over 3 majority).  */
#define DBGU_MR_FILTER_DISABLED               (DBGU_MR_FILTER_DISABLED_Val << DBGU_MR_FILTER_Pos)  /**< (DBGU_MR) DBGU does not filter the receive line. Position  */
#define DBGU_MR_FILTER_ENABLED                (DBGU_MR_FILTER_ENABLED_Val << DBGU_MR_FILTER_Pos)   /**< (DBGU_MR) DBGU filters the receive line using a three-sample filter (16x-bit clock) (2 over 3 majority). Position  */
#define DBGU_MR_PAR_Pos                       _U_(9)                                               /**< (DBGU_MR) Parity Type Position */
#define DBGU_MR_PAR_Msk                       (_U_(0x7) << DBGU_MR_PAR_Pos)                        /**< (DBGU_MR) Parity Type Mask */
#define DBGU_MR_PAR(value)                    (DBGU_MR_PAR_Msk & ((value) << DBGU_MR_PAR_Pos))    
#define   DBGU_MR_PAR_EVEN_Val                _U_(0x0)                                             /**< (DBGU_MR) Even Parity  */
#define   DBGU_MR_PAR_ODD_Val                 _U_(0x1)                                             /**< (DBGU_MR) Odd Parity  */
#define   DBGU_MR_PAR_SPACE_Val               _U_(0x2)                                             /**< (DBGU_MR) Space: parity forced to 0  */
#define   DBGU_MR_PAR_MARK_Val                _U_(0x3)                                             /**< (DBGU_MR) Mark: parity forced to 1  */
#define   DBGU_MR_PAR_NO_Val                  _U_(0x4)                                             /**< (DBGU_MR) No parity  */
#define DBGU_MR_PAR_EVEN                      (DBGU_MR_PAR_EVEN_Val << DBGU_MR_PAR_Pos)            /**< (DBGU_MR) Even Parity Position  */
#define DBGU_MR_PAR_ODD                       (DBGU_MR_PAR_ODD_Val << DBGU_MR_PAR_Pos)             /**< (DBGU_MR) Odd Parity Position  */
#define DBGU_MR_PAR_SPACE                     (DBGU_MR_PAR_SPACE_Val << DBGU_MR_PAR_Pos)           /**< (DBGU_MR) Space: parity forced to 0 Position  */
#define DBGU_MR_PAR_MARK                      (DBGU_MR_PAR_MARK_Val << DBGU_MR_PAR_Pos)            /**< (DBGU_MR) Mark: parity forced to 1 Position  */
#define DBGU_MR_PAR_NO                        (DBGU_MR_PAR_NO_Val << DBGU_MR_PAR_Pos)              /**< (DBGU_MR) No parity Position  */
#define DBGU_MR_BRSRCCK_Pos                   _U_(12)                                              /**< (DBGU_MR) Baud Rate Source Clock Position */
#define DBGU_MR_BRSRCCK_Msk                   (_U_(0x1) << DBGU_MR_BRSRCCK_Pos)                    /**< (DBGU_MR) Baud Rate Source Clock Mask */
#define DBGU_MR_BRSRCCK(value)                (DBGU_MR_BRSRCCK_Msk & ((value) << DBGU_MR_BRSRCCK_Pos))
#define   DBGU_MR_BRSRCCK_PERIPH_CLK_Val      _U_(0x0)                                             /**< (DBGU_MR) The baud rate is driven by the peripheral clock  */
#define   DBGU_MR_BRSRCCK_PMC_PCKGCLK_Val     _U_(0x1)                                             /**< (DBGU_MR) The baud rate is driven by a PMC-programmable clock PCKGCLK  */
#define DBGU_MR_BRSRCCK_PERIPH_CLK            (DBGU_MR_BRSRCCK_PERIPH_CLK_Val << DBGU_MR_BRSRCCK_Pos) /**< (DBGU_MR) The baud rate is driven by the peripheral clock Position  */
#define DBGU_MR_BRSRCCK_PMC_PCKGCLK           (DBGU_MR_BRSRCCK_PMC_PCKGCLK_Val << DBGU_MR_BRSRCCK_Pos) /**< (DBGU_MR) The baud rate is driven by a PMC-programmable clock PCKGCLK Position  */
#define DBGU_MR_CHMODE_Pos                    _U_(14)                                              /**< (DBGU_MR) Channel Mode Position */
#define DBGU_MR_CHMODE_Msk                    (_U_(0x3) << DBGU_MR_CHMODE_Pos)                     /**< (DBGU_MR) Channel Mode Mask */
#define DBGU_MR_CHMODE(value)                 (DBGU_MR_CHMODE_Msk & ((value) << DBGU_MR_CHMODE_Pos))
#define   DBGU_MR_CHMODE_NORMAL_Val           _U_(0x0)                                             /**< (DBGU_MR) Normal mode  */
#define   DBGU_MR_CHMODE_AUTOMATIC_Val        _U_(0x1)                                             /**< (DBGU_MR) Automatic echo  */
#define   DBGU_MR_CHMODE_LOCAL_LOOPBACK_Val   _U_(0x2)                                             /**< (DBGU_MR) Local loopback  */
#define   DBGU_MR_CHMODE_REMOTE_LOOPBACK_Val  _U_(0x3)                                             /**< (DBGU_MR) Remote loopback  */
#define DBGU_MR_CHMODE_NORMAL                 (DBGU_MR_CHMODE_NORMAL_Val << DBGU_MR_CHMODE_Pos)    /**< (DBGU_MR) Normal mode Position  */
#define DBGU_MR_CHMODE_AUTOMATIC              (DBGU_MR_CHMODE_AUTOMATIC_Val << DBGU_MR_CHMODE_Pos) /**< (DBGU_MR) Automatic echo Position  */
#define DBGU_MR_CHMODE_LOCAL_LOOPBACK         (DBGU_MR_CHMODE_LOCAL_LOOPBACK_Val << DBGU_MR_CHMODE_Pos) /**< (DBGU_MR) Local loopback Position  */
#define DBGU_MR_CHMODE_REMOTE_LOOPBACK        (DBGU_MR_CHMODE_REMOTE_LOOPBACK_Val << DBGU_MR_CHMODE_Pos) /**< (DBGU_MR) Remote loopback Position  */
#define DBGU_MR_Msk                           _U_(0x0000DE10)                                      /**< (DBGU_MR) Register Mask  */


/* -------- DBGU_IER : (DBGU Offset: 0x08) ( /W 32) Interrupt Enable Register -------- */
#define DBGU_IER_RXRDY_Pos                    _U_(0)                                               /**< (DBGU_IER) Enable RXRDY Interrupt Position */
#define DBGU_IER_RXRDY_Msk                    (_U_(0x1) << DBGU_IER_RXRDY_Pos)                     /**< (DBGU_IER) Enable RXRDY Interrupt Mask */
#define DBGU_IER_RXRDY(value)                 (DBGU_IER_RXRDY_Msk & ((value) << DBGU_IER_RXRDY_Pos))
#define DBGU_IER_TXRDY_Pos                    _U_(1)                                               /**< (DBGU_IER) Enable TXRDY Interrupt Position */
#define DBGU_IER_TXRDY_Msk                    (_U_(0x1) << DBGU_IER_TXRDY_Pos)                     /**< (DBGU_IER) Enable TXRDY Interrupt Mask */
#define DBGU_IER_TXRDY(value)                 (DBGU_IER_TXRDY_Msk & ((value) << DBGU_IER_TXRDY_Pos))
#define DBGU_IER_OVRE_Pos                     _U_(5)                                               /**< (DBGU_IER) Enable Overrun Error Interrupt Position */
#define DBGU_IER_OVRE_Msk                     (_U_(0x1) << DBGU_IER_OVRE_Pos)                      /**< (DBGU_IER) Enable Overrun Error Interrupt Mask */
#define DBGU_IER_OVRE(value)                  (DBGU_IER_OVRE_Msk & ((value) << DBGU_IER_OVRE_Pos))
#define DBGU_IER_FRAME_Pos                    _U_(6)                                               /**< (DBGU_IER) Enable Framing Error Interrupt Position */
#define DBGU_IER_FRAME_Msk                    (_U_(0x1) << DBGU_IER_FRAME_Pos)                     /**< (DBGU_IER) Enable Framing Error Interrupt Mask */
#define DBGU_IER_FRAME(value)                 (DBGU_IER_FRAME_Msk & ((value) << DBGU_IER_FRAME_Pos))
#define DBGU_IER_PARE_Pos                     _U_(7)                                               /**< (DBGU_IER) Enable Parity Error Interrupt Position */
#define DBGU_IER_PARE_Msk                     (_U_(0x1) << DBGU_IER_PARE_Pos)                      /**< (DBGU_IER) Enable Parity Error Interrupt Mask */
#define DBGU_IER_PARE(value)                  (DBGU_IER_PARE_Msk & ((value) << DBGU_IER_PARE_Pos))
#define DBGU_IER_TIMEOUT_Pos                  _U_(8)                                               /**< (DBGU_IER) Enable Timeout Interrupt Position */
#define DBGU_IER_TIMEOUT_Msk                  (_U_(0x1) << DBGU_IER_TIMEOUT_Pos)                   /**< (DBGU_IER) Enable Timeout Interrupt Mask */
#define DBGU_IER_TIMEOUT(value)               (DBGU_IER_TIMEOUT_Msk & ((value) << DBGU_IER_TIMEOUT_Pos))
#define DBGU_IER_TXEMPTY_Pos                  _U_(9)                                               /**< (DBGU_IER) Enable TXEMPTY Interrupt Position */
#define DBGU_IER_TXEMPTY_Msk                  (_U_(0x1) << DBGU_IER_TXEMPTY_Pos)                   /**< (DBGU_IER) Enable TXEMPTY Interrupt Mask */
#define DBGU_IER_TXEMPTY(value)               (DBGU_IER_TXEMPTY_Msk & ((value) << DBGU_IER_TXEMPTY_Pos))
#define DBGU_IER_COMMTX_Pos                   _U_(30)                                              /**< (DBGU_IER) Enable COMMTX (from ARM) Interrupt Position */
#define DBGU_IER_COMMTX_Msk                   (_U_(0x1) << DBGU_IER_COMMTX_Pos)                    /**< (DBGU_IER) Enable COMMTX (from ARM) Interrupt Mask */
#define DBGU_IER_COMMTX(value)                (DBGU_IER_COMMTX_Msk & ((value) << DBGU_IER_COMMTX_Pos))
#define DBGU_IER_COMMRX_Pos                   _U_(31)                                              /**< (DBGU_IER) Enable COMMRX (from ARM) Interrupt Position */
#define DBGU_IER_COMMRX_Msk                   (_U_(0x1) << DBGU_IER_COMMRX_Pos)                    /**< (DBGU_IER) Enable COMMRX (from ARM) Interrupt Mask */
#define DBGU_IER_COMMRX(value)                (DBGU_IER_COMMRX_Msk & ((value) << DBGU_IER_COMMRX_Pos))
#define DBGU_IER_Msk                          _U_(0xC00003E3)                                      /**< (DBGU_IER) Register Mask  */


/* -------- DBGU_IDR : (DBGU Offset: 0x0C) ( /W 32) Interrupt Disable Register -------- */
#define DBGU_IDR_RXRDY_Pos                    _U_(0)                                               /**< (DBGU_IDR) Disable RXRDY Interrupt Position */
#define DBGU_IDR_RXRDY_Msk                    (_U_(0x1) << DBGU_IDR_RXRDY_Pos)                     /**< (DBGU_IDR) Disable RXRDY Interrupt Mask */
#define DBGU_IDR_RXRDY(value)                 (DBGU_IDR_RXRDY_Msk & ((value) << DBGU_IDR_RXRDY_Pos))
#define DBGU_IDR_TXRDY_Pos                    _U_(1)                                               /**< (DBGU_IDR) Disable TXRDY Interrupt Position */
#define DBGU_IDR_TXRDY_Msk                    (_U_(0x1) << DBGU_IDR_TXRDY_Pos)                     /**< (DBGU_IDR) Disable TXRDY Interrupt Mask */
#define DBGU_IDR_TXRDY(value)                 (DBGU_IDR_TXRDY_Msk & ((value) << DBGU_IDR_TXRDY_Pos))
#define DBGU_IDR_OVRE_Pos                     _U_(5)                                               /**< (DBGU_IDR) Disable Overrun Error Interrupt Position */
#define DBGU_IDR_OVRE_Msk                     (_U_(0x1) << DBGU_IDR_OVRE_Pos)                      /**< (DBGU_IDR) Disable Overrun Error Interrupt Mask */
#define DBGU_IDR_OVRE(value)                  (DBGU_IDR_OVRE_Msk & ((value) << DBGU_IDR_OVRE_Pos))
#define DBGU_IDR_FRAME_Pos                    _U_(6)                                               /**< (DBGU_IDR) Disable Framing Error Interrupt Position */
#define DBGU_IDR_FRAME_Msk                    (_U_(0x1) << DBGU_IDR_FRAME_Pos)                     /**< (DBGU_IDR) Disable Framing Error Interrupt Mask */
#define DBGU_IDR_FRAME(value)                 (DBGU_IDR_FRAME_Msk & ((value) << DBGU_IDR_FRAME_Pos))
#define DBGU_IDR_PARE_Pos                     _U_(7)                                               /**< (DBGU_IDR) Disable Parity Error Interrupt Position */
#define DBGU_IDR_PARE_Msk                     (_U_(0x1) << DBGU_IDR_PARE_Pos)                      /**< (DBGU_IDR) Disable Parity Error Interrupt Mask */
#define DBGU_IDR_PARE(value)                  (DBGU_IDR_PARE_Msk & ((value) << DBGU_IDR_PARE_Pos))
#define DBGU_IDR_TIMEOUT_Pos                  _U_(8)                                               /**< (DBGU_IDR) Disable Timeout Interrupt Position */
#define DBGU_IDR_TIMEOUT_Msk                  (_U_(0x1) << DBGU_IDR_TIMEOUT_Pos)                   /**< (DBGU_IDR) Disable Timeout Interrupt Mask */
#define DBGU_IDR_TIMEOUT(value)               (DBGU_IDR_TIMEOUT_Msk & ((value) << DBGU_IDR_TIMEOUT_Pos))
#define DBGU_IDR_TXEMPTY_Pos                  _U_(9)                                               /**< (DBGU_IDR) Disable TXEMPTY Interrupt Position */
#define DBGU_IDR_TXEMPTY_Msk                  (_U_(0x1) << DBGU_IDR_TXEMPTY_Pos)                   /**< (DBGU_IDR) Disable TXEMPTY Interrupt Mask */
#define DBGU_IDR_TXEMPTY(value)               (DBGU_IDR_TXEMPTY_Msk & ((value) << DBGU_IDR_TXEMPTY_Pos))
#define DBGU_IDR_COMMTX_Pos                   _U_(30)                                              /**< (DBGU_IDR) Disable COMMTX (from ARM) Interrupt Position */
#define DBGU_IDR_COMMTX_Msk                   (_U_(0x1) << DBGU_IDR_COMMTX_Pos)                    /**< (DBGU_IDR) Disable COMMTX (from ARM) Interrupt Mask */
#define DBGU_IDR_COMMTX(value)                (DBGU_IDR_COMMTX_Msk & ((value) << DBGU_IDR_COMMTX_Pos))
#define DBGU_IDR_COMMRX_Pos                   _U_(31)                                              /**< (DBGU_IDR) Disable COMMRX (from ARM) Interrupt Position */
#define DBGU_IDR_COMMRX_Msk                   (_U_(0x1) << DBGU_IDR_COMMRX_Pos)                    /**< (DBGU_IDR) Disable COMMRX (from ARM) Interrupt Mask */
#define DBGU_IDR_COMMRX(value)                (DBGU_IDR_COMMRX_Msk & ((value) << DBGU_IDR_COMMRX_Pos))
#define DBGU_IDR_Msk                          _U_(0xC00003E3)                                      /**< (DBGU_IDR) Register Mask  */


/* -------- DBGU_IMR : (DBGU Offset: 0x10) ( R/ 32) Interrupt Mask Register -------- */
#define DBGU_IMR_RXRDY_Pos                    _U_(0)                                               /**< (DBGU_IMR) Mask RXRDY Interrupt Position */
#define DBGU_IMR_RXRDY_Msk                    (_U_(0x1) << DBGU_IMR_RXRDY_Pos)                     /**< (DBGU_IMR) Mask RXRDY Interrupt Mask */
#define DBGU_IMR_RXRDY(value)                 (DBGU_IMR_RXRDY_Msk & ((value) << DBGU_IMR_RXRDY_Pos))
#define DBGU_IMR_TXRDY_Pos                    _U_(1)                                               /**< (DBGU_IMR) Disable TXRDY Interrupt Position */
#define DBGU_IMR_TXRDY_Msk                    (_U_(0x1) << DBGU_IMR_TXRDY_Pos)                     /**< (DBGU_IMR) Disable TXRDY Interrupt Mask */
#define DBGU_IMR_TXRDY(value)                 (DBGU_IMR_TXRDY_Msk & ((value) << DBGU_IMR_TXRDY_Pos))
#define DBGU_IMR_OVRE_Pos                     _U_(5)                                               /**< (DBGU_IMR) Mask Overrun Error Interrupt Position */
#define DBGU_IMR_OVRE_Msk                     (_U_(0x1) << DBGU_IMR_OVRE_Pos)                      /**< (DBGU_IMR) Mask Overrun Error Interrupt Mask */
#define DBGU_IMR_OVRE(value)                  (DBGU_IMR_OVRE_Msk & ((value) << DBGU_IMR_OVRE_Pos))
#define DBGU_IMR_FRAME_Pos                    _U_(6)                                               /**< (DBGU_IMR) Mask Framing Error Interrupt Position */
#define DBGU_IMR_FRAME_Msk                    (_U_(0x1) << DBGU_IMR_FRAME_Pos)                     /**< (DBGU_IMR) Mask Framing Error Interrupt Mask */
#define DBGU_IMR_FRAME(value)                 (DBGU_IMR_FRAME_Msk & ((value) << DBGU_IMR_FRAME_Pos))
#define DBGU_IMR_PARE_Pos                     _U_(7)                                               /**< (DBGU_IMR) Mask Parity Error Interrupt Position */
#define DBGU_IMR_PARE_Msk                     (_U_(0x1) << DBGU_IMR_PARE_Pos)                      /**< (DBGU_IMR) Mask Parity Error Interrupt Mask */
#define DBGU_IMR_PARE(value)                  (DBGU_IMR_PARE_Msk & ((value) << DBGU_IMR_PARE_Pos))
#define DBGU_IMR_TIMEOUT_Pos                  _U_(8)                                               /**< (DBGU_IMR) Mask Timeout Interrupt Position */
#define DBGU_IMR_TIMEOUT_Msk                  (_U_(0x1) << DBGU_IMR_TIMEOUT_Pos)                   /**< (DBGU_IMR) Mask Timeout Interrupt Mask */
#define DBGU_IMR_TIMEOUT(value)               (DBGU_IMR_TIMEOUT_Msk & ((value) << DBGU_IMR_TIMEOUT_Pos))
#define DBGU_IMR_TXEMPTY_Pos                  _U_(9)                                               /**< (DBGU_IMR) Mask TXEMPTY Interrupt Position */
#define DBGU_IMR_TXEMPTY_Msk                  (_U_(0x1) << DBGU_IMR_TXEMPTY_Pos)                   /**< (DBGU_IMR) Mask TXEMPTY Interrupt Mask */
#define DBGU_IMR_TXEMPTY(value)               (DBGU_IMR_TXEMPTY_Msk & ((value) << DBGU_IMR_TXEMPTY_Pos))
#define DBGU_IMR_COMMTX_Pos                   _U_(30)                                              /**< (DBGU_IMR) Mask COMMTX (from ARM) Interrupt Position */
#define DBGU_IMR_COMMTX_Msk                   (_U_(0x1) << DBGU_IMR_COMMTX_Pos)                    /**< (DBGU_IMR) Mask COMMTX (from ARM) Interrupt Mask */
#define DBGU_IMR_COMMTX(value)                (DBGU_IMR_COMMTX_Msk & ((value) << DBGU_IMR_COMMTX_Pos))
#define DBGU_IMR_COMMRX_Pos                   _U_(31)                                              /**< (DBGU_IMR) Mask COMMRX (from ARM) Interrupt Position */
#define DBGU_IMR_COMMRX_Msk                   (_U_(0x1) << DBGU_IMR_COMMRX_Pos)                    /**< (DBGU_IMR) Mask COMMRX (from ARM) Interrupt Mask */
#define DBGU_IMR_COMMRX(value)                (DBGU_IMR_COMMRX_Msk & ((value) << DBGU_IMR_COMMRX_Pos))
#define DBGU_IMR_Msk                          _U_(0xC00003E3)                                      /**< (DBGU_IMR) Register Mask  */


/* -------- DBGU_SR : (DBGU Offset: 0x14) ( R/ 32) Status Register -------- */
#define DBGU_SR_RXRDY_Pos                     _U_(0)                                               /**< (DBGU_SR) Receiver Ready Position */
#define DBGU_SR_RXRDY_Msk                     (_U_(0x1) << DBGU_SR_RXRDY_Pos)                      /**< (DBGU_SR) Receiver Ready Mask */
#define DBGU_SR_RXRDY(value)                  (DBGU_SR_RXRDY_Msk & ((value) << DBGU_SR_RXRDY_Pos))
#define DBGU_SR_TXRDY_Pos                     _U_(1)                                               /**< (DBGU_SR) Transmitter Ready Position */
#define DBGU_SR_TXRDY_Msk                     (_U_(0x1) << DBGU_SR_TXRDY_Pos)                      /**< (DBGU_SR) Transmitter Ready Mask */
#define DBGU_SR_TXRDY(value)                  (DBGU_SR_TXRDY_Msk & ((value) << DBGU_SR_TXRDY_Pos))
#define DBGU_SR_OVRE_Pos                      _U_(5)                                               /**< (DBGU_SR) Overrun Error Position */
#define DBGU_SR_OVRE_Msk                      (_U_(0x1) << DBGU_SR_OVRE_Pos)                       /**< (DBGU_SR) Overrun Error Mask */
#define DBGU_SR_OVRE(value)                   (DBGU_SR_OVRE_Msk & ((value) << DBGU_SR_OVRE_Pos))  
#define DBGU_SR_FRAME_Pos                     _U_(6)                                               /**< (DBGU_SR) Framing Error Position */
#define DBGU_SR_FRAME_Msk                     (_U_(0x1) << DBGU_SR_FRAME_Pos)                      /**< (DBGU_SR) Framing Error Mask */
#define DBGU_SR_FRAME(value)                  (DBGU_SR_FRAME_Msk & ((value) << DBGU_SR_FRAME_Pos))
#define DBGU_SR_PARE_Pos                      _U_(7)                                               /**< (DBGU_SR) Parity Error Position */
#define DBGU_SR_PARE_Msk                      (_U_(0x1) << DBGU_SR_PARE_Pos)                       /**< (DBGU_SR) Parity Error Mask */
#define DBGU_SR_PARE(value)                   (DBGU_SR_PARE_Msk & ((value) << DBGU_SR_PARE_Pos))  
#define DBGU_SR_TIMEOUT_Pos                   _U_(8)                                               /**< (DBGU_SR) Receiver Timeout Position */
#define DBGU_SR_TIMEOUT_Msk                   (_U_(0x1) << DBGU_SR_TIMEOUT_Pos)                    /**< (DBGU_SR) Receiver Timeout Mask */
#define DBGU_SR_TIMEOUT(value)                (DBGU_SR_TIMEOUT_Msk & ((value) << DBGU_SR_TIMEOUT_Pos))
#define DBGU_SR_TXEMPTY_Pos                   _U_(9)                                               /**< (DBGU_SR) Transmitter Empty Position */
#define DBGU_SR_TXEMPTY_Msk                   (_U_(0x1) << DBGU_SR_TXEMPTY_Pos)                    /**< (DBGU_SR) Transmitter Empty Mask */
#define DBGU_SR_TXEMPTY(value)                (DBGU_SR_TXEMPTY_Msk & ((value) << DBGU_SR_TXEMPTY_Pos))
#define DBGU_SR_SWES_Pos                      _U_(21)                                              /**< (DBGU_SR) SleepWalking Enable Status Position */
#define DBGU_SR_SWES_Msk                      (_U_(0x1) << DBGU_SR_SWES_Pos)                       /**< (DBGU_SR) SleepWalking Enable Status Mask */
#define DBGU_SR_SWES(value)                   (DBGU_SR_SWES_Msk & ((value) << DBGU_SR_SWES_Pos))  
#define DBGU_SR_CLKREQ_Pos                    _U_(22)                                              /**< (DBGU_SR) Clock Request Position */
#define DBGU_SR_CLKREQ_Msk                    (_U_(0x1) << DBGU_SR_CLKREQ_Pos)                     /**< (DBGU_SR) Clock Request Mask */
#define DBGU_SR_CLKREQ(value)                 (DBGU_SR_CLKREQ_Msk & ((value) << DBGU_SR_CLKREQ_Pos))
#define DBGU_SR_WKUPREQ_Pos                   _U_(23)                                              /**< (DBGU_SR) Wakeup Request Position */
#define DBGU_SR_WKUPREQ_Msk                   (_U_(0x1) << DBGU_SR_WKUPREQ_Pos)                    /**< (DBGU_SR) Wakeup Request Mask */
#define DBGU_SR_WKUPREQ(value)                (DBGU_SR_WKUPREQ_Msk & ((value) << DBGU_SR_WKUPREQ_Pos))
#define DBGU_SR_COMMTX_Pos                    _U_(30)                                              /**< (DBGU_SR) Debug Communication Channel Write Status Position */
#define DBGU_SR_COMMTX_Msk                    (_U_(0x1) << DBGU_SR_COMMTX_Pos)                     /**< (DBGU_SR) Debug Communication Channel Write Status Mask */
#define DBGU_SR_COMMTX(value)                 (DBGU_SR_COMMTX_Msk & ((value) << DBGU_SR_COMMTX_Pos))
#define DBGU_SR_COMMRX_Pos                    _U_(31)                                              /**< (DBGU_SR) Debug Communication Channel Read Status Position */
#define DBGU_SR_COMMRX_Msk                    (_U_(0x1) << DBGU_SR_COMMRX_Pos)                     /**< (DBGU_SR) Debug Communication Channel Read Status Mask */
#define DBGU_SR_COMMRX(value)                 (DBGU_SR_COMMRX_Msk & ((value) << DBGU_SR_COMMRX_Pos))
#define DBGU_SR_Msk                           _U_(0xC0E003E3)                                      /**< (DBGU_SR) Register Mask  */


/* -------- DBGU_RHR : (DBGU Offset: 0x18) ( R/ 32) Receive Holding Register -------- */
#define DBGU_RHR_RXCHR_Pos                    _U_(0)                                               /**< (DBGU_RHR) Received Character Position */
#define DBGU_RHR_RXCHR_Msk                    (_U_(0xFF) << DBGU_RHR_RXCHR_Pos)                    /**< (DBGU_RHR) Received Character Mask */
#define DBGU_RHR_RXCHR(value)                 (DBGU_RHR_RXCHR_Msk & ((value) << DBGU_RHR_RXCHR_Pos))
#define DBGU_RHR_Msk                          _U_(0x000000FF)                                      /**< (DBGU_RHR) Register Mask  */


/* -------- DBGU_THR : (DBGU Offset: 0x1C) ( /W 32) Transmit Holding Register -------- */
#define DBGU_THR_TXCHR_Pos                    _U_(0)                                               /**< (DBGU_THR) Character to be Transmitted Position */
#define DBGU_THR_TXCHR_Msk                    (_U_(0xFF) << DBGU_THR_TXCHR_Pos)                    /**< (DBGU_THR) Character to be Transmitted Mask */
#define DBGU_THR_TXCHR(value)                 (DBGU_THR_TXCHR_Msk & ((value) << DBGU_THR_TXCHR_Pos))
#define DBGU_THR_Msk                          _U_(0x000000FF)                                      /**< (DBGU_THR) Register Mask  */


/* -------- DBGU_BRGR : (DBGU Offset: 0x20) (R/W 32) Baud Rate Generator Register -------- */
#define DBGU_BRGR_CD_Pos                      _U_(0)                                               /**< (DBGU_BRGR) Clock Divisor Position */
#define DBGU_BRGR_CD_Msk                      (_U_(0xFFFF) << DBGU_BRGR_CD_Pos)                    /**< (DBGU_BRGR) Clock Divisor Mask */
#define DBGU_BRGR_CD(value)                   (DBGU_BRGR_CD_Msk & ((value) << DBGU_BRGR_CD_Pos))  
#define DBGU_BRGR_Msk                         _U_(0x0000FFFF)                                      /**< (DBGU_BRGR) Register Mask  */


/* -------- DBGU_RTOR : (DBGU Offset: 0x28) (R/W 32) Receiver Timeout Register -------- */
#define DBGU_RTOR_TO_Pos                      _U_(0)                                               /**< (DBGU_RTOR) Timeout Value Position */
#define DBGU_RTOR_TO_Msk                      (_U_(0xFF) << DBGU_RTOR_TO_Pos)                      /**< (DBGU_RTOR) Timeout Value Mask */
#define DBGU_RTOR_TO(value)                   (DBGU_RTOR_TO_Msk & ((value) << DBGU_RTOR_TO_Pos))  
#define DBGU_RTOR_Msk                         _U_(0x000000FF)                                      /**< (DBGU_RTOR) Register Mask  */


/* -------- DBGU_CIDR : (DBGU Offset: 0x40) ( R/ 32) Chip ID Register -------- */
#define DBGU_CIDR_VERSION_Pos                 _U_(0)                                               /**< (DBGU_CIDR) Version of the Device Position */
#define DBGU_CIDR_VERSION_Msk                 (_U_(0x1F) << DBGU_CIDR_VERSION_Pos)                 /**< (DBGU_CIDR) Version of the Device Mask */
#define DBGU_CIDR_VERSION(value)              (DBGU_CIDR_VERSION_Msk & ((value) << DBGU_CIDR_VERSION_Pos))
#define DBGU_CIDR_EPROC_Pos                   _U_(5)                                               /**< (DBGU_CIDR) Embedded Processor Position */
#define DBGU_CIDR_EPROC_Msk                   (_U_(0x7) << DBGU_CIDR_EPROC_Pos)                    /**< (DBGU_CIDR) Embedded Processor Mask */
#define DBGU_CIDR_EPROC(value)                (DBGU_CIDR_EPROC_Msk & ((value) << DBGU_CIDR_EPROC_Pos))
#define   DBGU_CIDR_EPROC_ARM946ES_Val        _U_(0x1)                                             /**< (DBGU_CIDR) ARM946ES  */
#define   DBGU_CIDR_EPROC_ARM7TDMI_Val        _U_(0x2)                                             /**< (DBGU_CIDR) ARM7TDMI  */
#define   DBGU_CIDR_EPROC_CM3_Val             _U_(0x3)                                             /**< (DBGU_CIDR) Cortex-M3  */
#define   DBGU_CIDR_EPROC_ARM920T_Val         _U_(0x4)                                             /**< (DBGU_CIDR) ARM920T  */
#define   DBGU_CIDR_EPROC_ARM926EJS_Val       _U_(0x5)                                             /**< (DBGU_CIDR) ARM926EJ-S  */
#define   DBGU_CIDR_EPROC_CA5_Val             _U_(0x6)                                             /**< (DBGU_CIDR) Cortex-A5  */
#define DBGU_CIDR_EPROC_ARM946ES              (DBGU_CIDR_EPROC_ARM946ES_Val << DBGU_CIDR_EPROC_Pos) /**< (DBGU_CIDR) ARM946ES Position  */
#define DBGU_CIDR_EPROC_ARM7TDMI              (DBGU_CIDR_EPROC_ARM7TDMI_Val << DBGU_CIDR_EPROC_Pos) /**< (DBGU_CIDR) ARM7TDMI Position  */
#define DBGU_CIDR_EPROC_CM3                   (DBGU_CIDR_EPROC_CM3_Val << DBGU_CIDR_EPROC_Pos)     /**< (DBGU_CIDR) Cortex-M3 Position  */
#define DBGU_CIDR_EPROC_ARM920T               (DBGU_CIDR_EPROC_ARM920T_Val << DBGU_CIDR_EPROC_Pos) /**< (DBGU_CIDR) ARM920T Position  */
#define DBGU_CIDR_EPROC_ARM926EJS             (DBGU_CIDR_EPROC_ARM926EJS_Val << DBGU_CIDR_EPROC_Pos) /**< (DBGU_CIDR) ARM926EJ-S Position  */
#define DBGU_CIDR_EPROC_CA5                   (DBGU_CIDR_EPROC_CA5_Val << DBGU_CIDR_EPROC_Pos)     /**< (DBGU_CIDR) Cortex-A5 Position  */
#define DBGU_CIDR_NVPSIZ_Pos                  _U_(8)                                               /**< (DBGU_CIDR) Nonvolatile Program Memory Size Position */
#define DBGU_CIDR_NVPSIZ_Msk                  (_U_(0xF) << DBGU_CIDR_NVPSIZ_Pos)                   /**< (DBGU_CIDR) Nonvolatile Program Memory Size Mask */
#define DBGU_CIDR_NVPSIZ(value)               (DBGU_CIDR_NVPSIZ_Msk & ((value) << DBGU_CIDR_NVPSIZ_Pos))
#define   DBGU_CIDR_NVPSIZ_NONE_Val           _U_(0x0)                                             /**< (DBGU_CIDR) None  */
#define   DBGU_CIDR_NVPSIZ_8K_Val             _U_(0x1)                                             /**< (DBGU_CIDR) 8 Kbytes  */
#define   DBGU_CIDR_NVPSIZ_16K_Val            _U_(0x2)                                             /**< (DBGU_CIDR) 16 Kbytes  */
#define   DBGU_CIDR_NVPSIZ_32K_Val            _U_(0x3)                                             /**< (DBGU_CIDR) 32 Kbytes  */
#define   DBGU_CIDR_NVPSIZ_64K_Val            _U_(0x5)                                             /**< (DBGU_CIDR) 64 Kbytes  */
#define   DBGU_CIDR_NVPSIZ_128K_Val           _U_(0x7)                                             /**< (DBGU_CIDR) 128 Kbytes  */
#define   DBGU_CIDR_NVPSIZ_256K_Val           _U_(0x9)                                             /**< (DBGU_CIDR) 256 Kbytes  */
#define   DBGU_CIDR_NVPSIZ_512K_Val           _U_(0xA)                                             /**< (DBGU_CIDR) 512 Kbytes  */
#define   DBGU_CIDR_NVPSIZ_1024K_Val          _U_(0xC)                                             /**< (DBGU_CIDR) 1024 Kbytes  */
#define   DBGU_CIDR_NVPSIZ_2048K_Val          _U_(0xE)                                             /**< (DBGU_CIDR) 2048 Kbytes  */
#define DBGU_CIDR_NVPSIZ_NONE                 (DBGU_CIDR_NVPSIZ_NONE_Val << DBGU_CIDR_NVPSIZ_Pos)  /**< (DBGU_CIDR) None Position  */
#define DBGU_CIDR_NVPSIZ_8K                   (DBGU_CIDR_NVPSIZ_8K_Val << DBGU_CIDR_NVPSIZ_Pos)    /**< (DBGU_CIDR) 8 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ_16K                  (DBGU_CIDR_NVPSIZ_16K_Val << DBGU_CIDR_NVPSIZ_Pos)   /**< (DBGU_CIDR) 16 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ_32K                  (DBGU_CIDR_NVPSIZ_32K_Val << DBGU_CIDR_NVPSIZ_Pos)   /**< (DBGU_CIDR) 32 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ_64K                  (DBGU_CIDR_NVPSIZ_64K_Val << DBGU_CIDR_NVPSIZ_Pos)   /**< (DBGU_CIDR) 64 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ_128K                 (DBGU_CIDR_NVPSIZ_128K_Val << DBGU_CIDR_NVPSIZ_Pos)  /**< (DBGU_CIDR) 128 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ_256K                 (DBGU_CIDR_NVPSIZ_256K_Val << DBGU_CIDR_NVPSIZ_Pos)  /**< (DBGU_CIDR) 256 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ_512K                 (DBGU_CIDR_NVPSIZ_512K_Val << DBGU_CIDR_NVPSIZ_Pos)  /**< (DBGU_CIDR) 512 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ_1024K                (DBGU_CIDR_NVPSIZ_1024K_Val << DBGU_CIDR_NVPSIZ_Pos) /**< (DBGU_CIDR) 1024 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ_2048K                (DBGU_CIDR_NVPSIZ_2048K_Val << DBGU_CIDR_NVPSIZ_Pos) /**< (DBGU_CIDR) 2048 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ2_Pos                 _U_(12)                                              /**< (DBGU_CIDR) Second Nonvolatile Program Memory Size Position */
#define DBGU_CIDR_NVPSIZ2_Msk                 (_U_(0xF) << DBGU_CIDR_NVPSIZ2_Pos)                  /**< (DBGU_CIDR) Second Nonvolatile Program Memory Size Mask */
#define DBGU_CIDR_NVPSIZ2(value)              (DBGU_CIDR_NVPSIZ2_Msk & ((value) << DBGU_CIDR_NVPSIZ2_Pos))
#define   DBGU_CIDR_NVPSIZ2_NONE_Val          _U_(0x0)                                             /**< (DBGU_CIDR) None  */
#define   DBGU_CIDR_NVPSIZ2_8K_Val            _U_(0x1)                                             /**< (DBGU_CIDR) 8 Kbytes  */
#define   DBGU_CIDR_NVPSIZ2_16K_Val           _U_(0x2)                                             /**< (DBGU_CIDR) 16 Kbytes  */
#define   DBGU_CIDR_NVPSIZ2_32K_Val           _U_(0x3)                                             /**< (DBGU_CIDR) 32 Kbytes  */
#define   DBGU_CIDR_NVPSIZ2_64K_Val           _U_(0x5)                                             /**< (DBGU_CIDR) 64 Kbytes  */
#define   DBGU_CIDR_NVPSIZ2_128K_Val          _U_(0x7)                                             /**< (DBGU_CIDR) 128 Kbytes  */
#define   DBGU_CIDR_NVPSIZ2_256K_Val          _U_(0x9)                                             /**< (DBGU_CIDR) 256 Kbytes  */
#define   DBGU_CIDR_NVPSIZ2_512K_Val          _U_(0xA)                                             /**< (DBGU_CIDR) 512 Kbytes  */
#define   DBGU_CIDR_NVPSIZ2_1024K_Val         _U_(0xC)                                             /**< (DBGU_CIDR) 1024 Kbytes  */
#define   DBGU_CIDR_NVPSIZ2_2048K_Val         _U_(0xE)                                             /**< (DBGU_CIDR) 2048 Kbytes  */
#define DBGU_CIDR_NVPSIZ2_NONE                (DBGU_CIDR_NVPSIZ2_NONE_Val << DBGU_CIDR_NVPSIZ2_Pos) /**< (DBGU_CIDR) None Position  */
#define DBGU_CIDR_NVPSIZ2_8K                  (DBGU_CIDR_NVPSIZ2_8K_Val << DBGU_CIDR_NVPSIZ2_Pos)  /**< (DBGU_CIDR) 8 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ2_16K                 (DBGU_CIDR_NVPSIZ2_16K_Val << DBGU_CIDR_NVPSIZ2_Pos) /**< (DBGU_CIDR) 16 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ2_32K                 (DBGU_CIDR_NVPSIZ2_32K_Val << DBGU_CIDR_NVPSIZ2_Pos) /**< (DBGU_CIDR) 32 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ2_64K                 (DBGU_CIDR_NVPSIZ2_64K_Val << DBGU_CIDR_NVPSIZ2_Pos) /**< (DBGU_CIDR) 64 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ2_128K                (DBGU_CIDR_NVPSIZ2_128K_Val << DBGU_CIDR_NVPSIZ2_Pos) /**< (DBGU_CIDR) 128 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ2_256K                (DBGU_CIDR_NVPSIZ2_256K_Val << DBGU_CIDR_NVPSIZ2_Pos) /**< (DBGU_CIDR) 256 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ2_512K                (DBGU_CIDR_NVPSIZ2_512K_Val << DBGU_CIDR_NVPSIZ2_Pos) /**< (DBGU_CIDR) 512 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ2_1024K               (DBGU_CIDR_NVPSIZ2_1024K_Val << DBGU_CIDR_NVPSIZ2_Pos) /**< (DBGU_CIDR) 1024 Kbytes Position  */
#define DBGU_CIDR_NVPSIZ2_2048K               (DBGU_CIDR_NVPSIZ2_2048K_Val << DBGU_CIDR_NVPSIZ2_Pos) /**< (DBGU_CIDR) 2048 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_Pos                 _U_(16)                                              /**< (DBGU_CIDR) Internal SRAM Size Position */
#define DBGU_CIDR_SRAMSIZ_Msk                 (_U_(0xF) << DBGU_CIDR_SRAMSIZ_Pos)                  /**< (DBGU_CIDR) Internal SRAM Size Mask */
#define DBGU_CIDR_SRAMSIZ(value)              (DBGU_CIDR_SRAMSIZ_Msk & ((value) << DBGU_CIDR_SRAMSIZ_Pos))
#define   DBGU_CIDR_SRAMSIZ_1K_Val            _U_(0x1)                                             /**< (DBGU_CIDR) 1 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_2K_Val            _U_(0x2)                                             /**< (DBGU_CIDR) 2 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_6K_Val            _U_(0x3)                                             /**< (DBGU_CIDR) 6 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_112K_Val          _U_(0x4)                                             /**< (DBGU_CIDR) 112 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_4K_Val            _U_(0x5)                                             /**< (DBGU_CIDR) 4 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_80K_Val           _U_(0x6)                                             /**< (DBGU_CIDR) 80 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_160K_Val          _U_(0x7)                                             /**< (DBGU_CIDR) 160 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_8K_Val            _U_(0x8)                                             /**< (DBGU_CIDR) 8 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_16K_Val           _U_(0x9)                                             /**< (DBGU_CIDR) 16 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_32K_Val           _U_(0xA)                                             /**< (DBGU_CIDR) 32 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_64K_Val           _U_(0xB)                                             /**< (DBGU_CIDR) 64 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_128K_Val          _U_(0xC)                                             /**< (DBGU_CIDR) 128 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_256K_Val          _U_(0xD)                                             /**< (DBGU_CIDR) 256 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_96K_Val           _U_(0xE)                                             /**< (DBGU_CIDR) 96 Kbytes  */
#define   DBGU_CIDR_SRAMSIZ_512K_Val          _U_(0xF)                                             /**< (DBGU_CIDR) 512 Kbytes  */
#define DBGU_CIDR_SRAMSIZ_1K                  (DBGU_CIDR_SRAMSIZ_1K_Val << DBGU_CIDR_SRAMSIZ_Pos)  /**< (DBGU_CIDR) 1 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_2K                  (DBGU_CIDR_SRAMSIZ_2K_Val << DBGU_CIDR_SRAMSIZ_Pos)  /**< (DBGU_CIDR) 2 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_6K                  (DBGU_CIDR_SRAMSIZ_6K_Val << DBGU_CIDR_SRAMSIZ_Pos)  /**< (DBGU_CIDR) 6 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_112K                (DBGU_CIDR_SRAMSIZ_112K_Val << DBGU_CIDR_SRAMSIZ_Pos) /**< (DBGU_CIDR) 112 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_4K                  (DBGU_CIDR_SRAMSIZ_4K_Val << DBGU_CIDR_SRAMSIZ_Pos)  /**< (DBGU_CIDR) 4 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_80K                 (DBGU_CIDR_SRAMSIZ_80K_Val << DBGU_CIDR_SRAMSIZ_Pos) /**< (DBGU_CIDR) 80 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_160K                (DBGU_CIDR_SRAMSIZ_160K_Val << DBGU_CIDR_SRAMSIZ_Pos) /**< (DBGU_CIDR) 160 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_8K                  (DBGU_CIDR_SRAMSIZ_8K_Val << DBGU_CIDR_SRAMSIZ_Pos)  /**< (DBGU_CIDR) 8 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_16K                 (DBGU_CIDR_SRAMSIZ_16K_Val << DBGU_CIDR_SRAMSIZ_Pos) /**< (DBGU_CIDR) 16 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_32K                 (DBGU_CIDR_SRAMSIZ_32K_Val << DBGU_CIDR_SRAMSIZ_Pos) /**< (DBGU_CIDR) 32 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_64K                 (DBGU_CIDR_SRAMSIZ_64K_Val << DBGU_CIDR_SRAMSIZ_Pos) /**< (DBGU_CIDR) 64 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_128K                (DBGU_CIDR_SRAMSIZ_128K_Val << DBGU_CIDR_SRAMSIZ_Pos) /**< (DBGU_CIDR) 128 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_256K                (DBGU_CIDR_SRAMSIZ_256K_Val << DBGU_CIDR_SRAMSIZ_Pos) /**< (DBGU_CIDR) 256 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_96K                 (DBGU_CIDR_SRAMSIZ_96K_Val << DBGU_CIDR_SRAMSIZ_Pos) /**< (DBGU_CIDR) 96 Kbytes Position  */
#define DBGU_CIDR_SRAMSIZ_512K                (DBGU_CIDR_SRAMSIZ_512K_Val << DBGU_CIDR_SRAMSIZ_Pos) /**< (DBGU_CIDR) 512 Kbytes Position  */
#define DBGU_CIDR_ARCH_Pos                    _U_(20)                                              /**< (DBGU_CIDR) Architecture Identifier Position */
#define DBGU_CIDR_ARCH_Msk                    (_U_(0xFF) << DBGU_CIDR_ARCH_Pos)                    /**< (DBGU_CIDR) Architecture Identifier Mask */
#define DBGU_CIDR_ARCH(value)                 (DBGU_CIDR_ARCH_Msk & ((value) << DBGU_CIDR_ARCH_Pos))
#define   DBGU_CIDR_ARCH_AT91SAM9xx_Val       _U_(0x19)                                            /**< (DBGU_CIDR) AT91SAM9xx Series  */
#define   DBGU_CIDR_ARCH_AT91SAM9XExx_Val     _U_(0x29)                                            /**< (DBGU_CIDR) AT91SAM9XExx Series  */
#define   DBGU_CIDR_ARCH_AT91x34_Val          _U_(0x34)                                            /**< (DBGU_CIDR) AT91x34 Series  */
#define   DBGU_CIDR_ARCH_CAP7_Val             _U_(0x37)                                            /**< (DBGU_CIDR) CAP7 Series  */
#define   DBGU_CIDR_ARCH_CAP9_Val             _U_(0x39)                                            /**< (DBGU_CIDR) CAP9 Series  */
#define   DBGU_CIDR_ARCH_CAP11_Val            _U_(0x3B)                                            /**< (DBGU_CIDR) CAP11 Series  */
#define   DBGU_CIDR_ARCH_AT91x40_Val          _U_(0x40)                                            /**< (DBGU_CIDR) AT91x40 Series  */
#define   DBGU_CIDR_ARCH_AT91x42_Val          _U_(0x42)                                            /**< (DBGU_CIDR) AT91x42 Series  */
#define   DBGU_CIDR_ARCH_AT91x55_Val          _U_(0x55)                                            /**< (DBGU_CIDR) AT91x55 Series  */
#define   DBGU_CIDR_ARCH_AT91SAM7Axx_Val      _U_(0x60)                                            /**< (DBGU_CIDR) AT91SAM7Axx Series  */
#define   DBGU_CIDR_ARCH_AT91SAM7AQxx_Val     _U_(0x61)                                            /**< (DBGU_CIDR) AT91SAM7AQxx Series  */
#define   DBGU_CIDR_ARCH_AT91x63_Val          _U_(0x63)                                            /**< (DBGU_CIDR) AT91x63 Series  */
#define   DBGU_CIDR_ARCH_AT91SAM7Sxx_Val      _U_(0x70)                                            /**< (DBGU_CIDR) AT91SAM7Sxx Series  */
#define   DBGU_CIDR_ARCH_AT91SAM7XCxx_Val     _U_(0x71)                                            /**< (DBGU_CIDR) AT91SAM7XCxx Series  */
#define   DBGU_CIDR_ARCH_AT91SAM7SExx_Val     _U_(0x72)                                            /**< (DBGU_CIDR) AT91SAM7SExx Series  */
#define   DBGU_CIDR_ARCH_AT91SAM7Lxx_Val      _U_(0x73)                                            /**< (DBGU_CIDR) AT91SAM7Lxx Series  */
#define   DBGU_CIDR_ARCH_AT91SAM7Xxx_Val      _U_(0x75)                                            /**< (DBGU_CIDR) AT91SAM7Xxx Series  */
#define   DBGU_CIDR_ARCH_AT91SAM7SLxx_Val     _U_(0x76)                                            /**< (DBGU_CIDR) AT91SAM7SLxx Series  */
#define   DBGU_CIDR_ARCH_ATSAM3UxC_Val        _U_(0x80)                                            /**< (DBGU_CIDR) ATSAM3UxC Series (100-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3UxE_Val        _U_(0x81)                                            /**< (DBGU_CIDR) ATSAM3UxE Series (144-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3AxC_Val        _U_(0x83)                                            /**< (DBGU_CIDR) ATSAM3AxC Series (100-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3XxC_Val        _U_(0x84)                                            /**< (DBGU_CIDR) ATSAM3XxC Series (100-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3XxE_Val        _U_(0x85)                                            /**< (DBGU_CIDR) ATSAM3XxE Series (144-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3XxG_Val        _U_(0x86)                                            /**< (DBGU_CIDR) ATSAM3XxG Series (208/217-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3SxA_Val        _U_(0x88)                                            /**< (DBGU_CIDR) ATSAM3SxA Series (48-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3SxB_Val        _U_(0x89)                                            /**< (DBGU_CIDR) ATSAM3SxB Series (64-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3SxC_Val        _U_(0x8A)                                            /**< (DBGU_CIDR) ATSAM3SxC Series (100-pin version)  */
#define   DBGU_CIDR_ARCH_AT91x92_Val          _U_(0x92)                                            /**< (DBGU_CIDR) AT91x92 Series  */
#define   DBGU_CIDR_ARCH_ATSAM3NxA_Val        _U_(0x93)                                            /**< (DBGU_CIDR) ATSAM3NxA Series (48-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3NxB_Val        _U_(0x94)                                            /**< (DBGU_CIDR) ATSAM3NxB Series (64-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3NxC_Val        _U_(0x95)                                            /**< (DBGU_CIDR) ATSAM3NxC Series (100-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3SDxA_Val       _U_(0x98)                                            /**< (DBGU_CIDR) ATSAM3SDxA Series (48-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3SDxB_Val       _U_(0x99)                                            /**< (DBGU_CIDR) ATSAM3SDxB Series (64-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAM3SDxC_Val       _U_(0x9A)                                            /**< (DBGU_CIDR) ATSAM3SDxC Series (100-pin version)  */
#define   DBGU_CIDR_ARCH_ATSAMA5xx_Val        _U_(0xA5)                                            /**< (DBGU_CIDR) ATSAMA5xx Series  */
#define   DBGU_CIDR_ARCH_AT75Cxx_Val          _U_(0xF0)                                            /**< (DBGU_CIDR) AT75Cxx Series  */
#define DBGU_CIDR_ARCH_AT91SAM9xx             (DBGU_CIDR_ARCH_AT91SAM9xx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) AT91SAM9xx Series Position  */
#define DBGU_CIDR_ARCH_AT91SAM9XExx           (DBGU_CIDR_ARCH_AT91SAM9XExx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) AT91SAM9XExx Series Position  */
#define DBGU_CIDR_ARCH_AT91x34                (DBGU_CIDR_ARCH_AT91x34_Val << DBGU_CIDR_ARCH_Pos)   /**< (DBGU_CIDR) AT91x34 Series Position  */
#define DBGU_CIDR_ARCH_CAP7                   (DBGU_CIDR_ARCH_CAP7_Val << DBGU_CIDR_ARCH_Pos)      /**< (DBGU_CIDR) CAP7 Series Position  */
#define DBGU_CIDR_ARCH_CAP9                   (DBGU_CIDR_ARCH_CAP9_Val << DBGU_CIDR_ARCH_Pos)      /**< (DBGU_CIDR) CAP9 Series Position  */
#define DBGU_CIDR_ARCH_CAP11                  (DBGU_CIDR_ARCH_CAP11_Val << DBGU_CIDR_ARCH_Pos)     /**< (DBGU_CIDR) CAP11 Series Position  */
#define DBGU_CIDR_ARCH_AT91x40                (DBGU_CIDR_ARCH_AT91x40_Val << DBGU_CIDR_ARCH_Pos)   /**< (DBGU_CIDR) AT91x40 Series Position  */
#define DBGU_CIDR_ARCH_AT91x42                (DBGU_CIDR_ARCH_AT91x42_Val << DBGU_CIDR_ARCH_Pos)   /**< (DBGU_CIDR) AT91x42 Series Position  */
#define DBGU_CIDR_ARCH_AT91x55                (DBGU_CIDR_ARCH_AT91x55_Val << DBGU_CIDR_ARCH_Pos)   /**< (DBGU_CIDR) AT91x55 Series Position  */
#define DBGU_CIDR_ARCH_AT91SAM7Axx            (DBGU_CIDR_ARCH_AT91SAM7Axx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) AT91SAM7Axx Series Position  */
#define DBGU_CIDR_ARCH_AT91SAM7AQxx           (DBGU_CIDR_ARCH_AT91SAM7AQxx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) AT91SAM7AQxx Series Position  */
#define DBGU_CIDR_ARCH_AT91x63                (DBGU_CIDR_ARCH_AT91x63_Val << DBGU_CIDR_ARCH_Pos)   /**< (DBGU_CIDR) AT91x63 Series Position  */
#define DBGU_CIDR_ARCH_AT91SAM7Sxx            (DBGU_CIDR_ARCH_AT91SAM7Sxx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) AT91SAM7Sxx Series Position  */
#define DBGU_CIDR_ARCH_AT91SAM7XCxx           (DBGU_CIDR_ARCH_AT91SAM7XCxx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) AT91SAM7XCxx Series Position  */
#define DBGU_CIDR_ARCH_AT91SAM7SExx           (DBGU_CIDR_ARCH_AT91SAM7SExx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) AT91SAM7SExx Series Position  */
#define DBGU_CIDR_ARCH_AT91SAM7Lxx            (DBGU_CIDR_ARCH_AT91SAM7Lxx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) AT91SAM7Lxx Series Position  */
#define DBGU_CIDR_ARCH_AT91SAM7Xxx            (DBGU_CIDR_ARCH_AT91SAM7Xxx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) AT91SAM7Xxx Series Position  */
#define DBGU_CIDR_ARCH_AT91SAM7SLxx           (DBGU_CIDR_ARCH_AT91SAM7SLxx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) AT91SAM7SLxx Series Position  */
#define DBGU_CIDR_ARCH_ATSAM3UxC              (DBGU_CIDR_ARCH_ATSAM3UxC_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3UxC Series (100-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3UxE              (DBGU_CIDR_ARCH_ATSAM3UxE_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3UxE Series (144-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3AxC              (DBGU_CIDR_ARCH_ATSAM3AxC_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3AxC Series (100-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3XxC              (DBGU_CIDR_ARCH_ATSAM3XxC_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3XxC Series (100-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3XxE              (DBGU_CIDR_ARCH_ATSAM3XxE_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3XxE Series (144-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3XxG              (DBGU_CIDR_ARCH_ATSAM3XxG_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3XxG Series (208/217-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3SxA              (DBGU_CIDR_ARCH_ATSAM3SxA_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3SxA Series (48-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3SxB              (DBGU_CIDR_ARCH_ATSAM3SxB_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3SxB Series (64-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3SxC              (DBGU_CIDR_ARCH_ATSAM3SxC_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3SxC Series (100-pin version) Position  */
#define DBGU_CIDR_ARCH_AT91x92                (DBGU_CIDR_ARCH_AT91x92_Val << DBGU_CIDR_ARCH_Pos)   /**< (DBGU_CIDR) AT91x92 Series Position  */
#define DBGU_CIDR_ARCH_ATSAM3NxA              (DBGU_CIDR_ARCH_ATSAM3NxA_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3NxA Series (48-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3NxB              (DBGU_CIDR_ARCH_ATSAM3NxB_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3NxB Series (64-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3NxC              (DBGU_CIDR_ARCH_ATSAM3NxC_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3NxC Series (100-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3SDxA             (DBGU_CIDR_ARCH_ATSAM3SDxA_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3SDxA Series (48-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3SDxB             (DBGU_CIDR_ARCH_ATSAM3SDxB_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3SDxB Series (64-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAM3SDxC             (DBGU_CIDR_ARCH_ATSAM3SDxC_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAM3SDxC Series (100-pin version) Position  */
#define DBGU_CIDR_ARCH_ATSAMA5xx              (DBGU_CIDR_ARCH_ATSAMA5xx_Val << DBGU_CIDR_ARCH_Pos) /**< (DBGU_CIDR) ATSAMA5xx Series Position  */
#define DBGU_CIDR_ARCH_AT75Cxx                (DBGU_CIDR_ARCH_AT75Cxx_Val << DBGU_CIDR_ARCH_Pos)   /**< (DBGU_CIDR) AT75Cxx Series Position  */
#define DBGU_CIDR_NVPTYP_Pos                  _U_(28)                                              /**< (DBGU_CIDR) Nonvolatile Program Memory Type Position */
#define DBGU_CIDR_NVPTYP_Msk                  (_U_(0x7) << DBGU_CIDR_NVPTYP_Pos)                   /**< (DBGU_CIDR) Nonvolatile Program Memory Type Mask */
#define DBGU_CIDR_NVPTYP(value)               (DBGU_CIDR_NVPTYP_Msk & ((value) << DBGU_CIDR_NVPTYP_Pos))
#define   DBGU_CIDR_NVPTYP_ROM_Val            _U_(0x0)                                             /**< (DBGU_CIDR) ROM  */
#define   DBGU_CIDR_NVPTYP_ROMLESS_Val        _U_(0x1)                                             /**< (DBGU_CIDR) ROMless or on-chip Flash  */
#define   DBGU_CIDR_NVPTYP_FLASH_Val          _U_(0x2)                                             /**< (DBGU_CIDR) Embedded Flash Memory  */
#define   DBGU_CIDR_NVPTYP_ROM_FLASH_Val      _U_(0x3)                                             /**< (DBGU_CIDR) ROM and Embedded Flash MemoryNVPSIZ is ROM size NVPSIZ2 is Flash size  */
#define   DBGU_CIDR_NVPTYP_SRAM_Val           _U_(0x4)                                             /**< (DBGU_CIDR) SRAM emulating ROM  */
#define DBGU_CIDR_NVPTYP_ROM                  (DBGU_CIDR_NVPTYP_ROM_Val << DBGU_CIDR_NVPTYP_Pos)   /**< (DBGU_CIDR) ROM Position  */
#define DBGU_CIDR_NVPTYP_ROMLESS              (DBGU_CIDR_NVPTYP_ROMLESS_Val << DBGU_CIDR_NVPTYP_Pos) /**< (DBGU_CIDR) ROMless or on-chip Flash Position  */
#define DBGU_CIDR_NVPTYP_FLASH                (DBGU_CIDR_NVPTYP_FLASH_Val << DBGU_CIDR_NVPTYP_Pos) /**< (DBGU_CIDR) Embedded Flash Memory Position  */
#define DBGU_CIDR_NVPTYP_ROM_FLASH            (DBGU_CIDR_NVPTYP_ROM_FLASH_Val << DBGU_CIDR_NVPTYP_Pos) /**< (DBGU_CIDR) ROM and Embedded Flash MemoryNVPSIZ is ROM size NVPSIZ2 is Flash size Position  */
#define DBGU_CIDR_NVPTYP_SRAM                 (DBGU_CIDR_NVPTYP_SRAM_Val << DBGU_CIDR_NVPTYP_Pos)  /**< (DBGU_CIDR) SRAM emulating ROM Position  */
#define DBGU_CIDR_EXT_Pos                     _U_(31)                                              /**< (DBGU_CIDR) Extension Flag Position */
#define DBGU_CIDR_EXT_Msk                     (_U_(0x1) << DBGU_CIDR_EXT_Pos)                      /**< (DBGU_CIDR) Extension Flag Mask */
#define DBGU_CIDR_EXT(value)                  (DBGU_CIDR_EXT_Msk & ((value) << DBGU_CIDR_EXT_Pos))
#define DBGU_CIDR_Msk                         _U_(0xFFFFFFFF)                                      /**< (DBGU_CIDR) Register Mask  */


/* -------- DBGU_EXID : (DBGU Offset: 0x44) ( R/ 32) Chip ID Extension Register -------- */
#define DBGU_EXID_EXID_Pos                    _U_(0)                                               /**< (DBGU_EXID) Chip ID Extension Position */
#define DBGU_EXID_EXID_Msk                    (_U_(0xFFFFFFFF) << DBGU_EXID_EXID_Pos)              /**< (DBGU_EXID) Chip ID Extension Mask */
#define DBGU_EXID_EXID(value)                 (DBGU_EXID_EXID_Msk & ((value) << DBGU_EXID_EXID_Pos))
#define DBGU_EXID_Msk                         _U_(0xFFFFFFFF)                                      /**< (DBGU_EXID) Register Mask  */


/* -------- DBGU_FNR : (DBGU Offset: 0x48) (R/W 32) Force NTRST Register -------- */
#define DBGU_FNR_FNTRST_Pos                   _U_(0)                                               /**< (DBGU_FNR) Force NTRST Position */
#define DBGU_FNR_FNTRST_Msk                   (_U_(0x1) << DBGU_FNR_FNTRST_Pos)                    /**< (DBGU_FNR) Force NTRST Mask */
#define DBGU_FNR_FNTRST(value)                (DBGU_FNR_FNTRST_Msk & ((value) << DBGU_FNR_FNTRST_Pos))
#define DBGU_FNR_Msk                          _U_(0x00000001)                                      /**< (DBGU_FNR) Register Mask  */


/* -------- DBGU_WPMR : (DBGU Offset: 0xE4) (R/W 32) Write Protection Mode Register -------- */
#define DBGU_WPMR_WPEN_Pos                    _U_(0)                                               /**< (DBGU_WPMR) Write Protection Enable Position */
#define DBGU_WPMR_WPEN_Msk                    (_U_(0x1) << DBGU_WPMR_WPEN_Pos)                     /**< (DBGU_WPMR) Write Protection Enable Mask */
#define DBGU_WPMR_WPEN(value)                 (DBGU_WPMR_WPEN_Msk & ((value) << DBGU_WPMR_WPEN_Pos))
#define DBGU_WPMR_WPKEY_Pos                   _U_(8)                                               /**< (DBGU_WPMR) Write Protection Key Position */
#define DBGU_WPMR_WPKEY_Msk                   (_U_(0xFFFFFF) << DBGU_WPMR_WPKEY_Pos)               /**< (DBGU_WPMR) Write Protection Key Mask */
#define DBGU_WPMR_WPKEY(value)                (DBGU_WPMR_WPKEY_Msk & ((value) << DBGU_WPMR_WPKEY_Pos))
#define   DBGU_WPMR_WPKEY_PASSWD_Val          _U_(0x554152)                                        /**< (DBGU_WPMR) Writing any other value in this field aborts the write operation.Always reads as 0.  */
#define DBGU_WPMR_WPKEY_PASSWD                (DBGU_WPMR_WPKEY_PASSWD_Val << DBGU_WPMR_WPKEY_Pos)  /**< (DBGU_WPMR) Writing any other value in this field aborts the write operation.Always reads as 0. Position  */
#define DBGU_WPMR_Msk                         _U_(0xFFFFFF01)                                      /**< (DBGU_WPMR) Register Mask  */


/* -------- DBGU_VERSION : (DBGU Offset: 0xFC) ( R/ 32) Version Register -------- */
#define DBGU_VERSION_VERSION_Pos              _U_(0)                                               /**< (DBGU_VERSION) Hardware Module Version Position */
#define DBGU_VERSION_VERSION_Msk              (_U_(0xFFF) << DBGU_VERSION_VERSION_Pos)             /**< (DBGU_VERSION) Hardware Module Version Mask */
#define DBGU_VERSION_VERSION(value)           (DBGU_VERSION_VERSION_Msk & ((value) << DBGU_VERSION_VERSION_Pos))
#define DBGU_VERSION_MFN_Pos                  _U_(16)                                              /**< (DBGU_VERSION) Metal Fix Number Position */
#define DBGU_VERSION_MFN_Msk                  (_U_(0x7) << DBGU_VERSION_MFN_Pos)                   /**< (DBGU_VERSION) Metal Fix Number Mask */
#define DBGU_VERSION_MFN(value)               (DBGU_VERSION_MFN_Msk & ((value) << DBGU_VERSION_MFN_Pos))
#define DBGU_VERSION_Msk                      _U_(0x00070FFF)                                      /**< (DBGU_VERSION) Register Mask  */


/** \brief DBGU register offsets definitions */
#define DBGU_CR_REG_OFST               (0x00)              /**< (DBGU_CR) Control Register Offset */
#define DBGU_MR_REG_OFST               (0x04)              /**< (DBGU_MR) Mode Register Offset */
#define DBGU_IER_REG_OFST              (0x08)              /**< (DBGU_IER) Interrupt Enable Register Offset */
#define DBGU_IDR_REG_OFST              (0x0C)              /**< (DBGU_IDR) Interrupt Disable Register Offset */
#define DBGU_IMR_REG_OFST              (0x10)              /**< (DBGU_IMR) Interrupt Mask Register Offset */
#define DBGU_SR_REG_OFST               (0x14)              /**< (DBGU_SR) Status Register Offset */
#define DBGU_RHR_REG_OFST              (0x18)              /**< (DBGU_RHR) Receive Holding Register Offset */
#define DBGU_THR_REG_OFST              (0x1C)              /**< (DBGU_THR) Transmit Holding Register Offset */
#define DBGU_BRGR_REG_OFST             (0x20)              /**< (DBGU_BRGR) Baud Rate Generator Register Offset */
#define DBGU_RTOR_REG_OFST             (0x28)              /**< (DBGU_RTOR) Receiver Timeout Register Offset */
#define DBGU_CIDR_REG_OFST             (0x40)              /**< (DBGU_CIDR) Chip ID Register Offset */
#define DBGU_EXID_REG_OFST             (0x44)              /**< (DBGU_EXID) Chip ID Extension Register Offset */
#define DBGU_FNR_REG_OFST              (0x48)              /**< (DBGU_FNR) Force NTRST Register Offset */
#define DBGU_WPMR_REG_OFST             (0xE4)              /**< (DBGU_WPMR) Write Protection Mode Register Offset */
#define DBGU_VERSION_REG_OFST          (0xFC)              /**< (DBGU_VERSION) Version Register Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief DBGU register API structure */
typedef struct
{
  __O   uint32_t                       DBGU_CR;            /**< Offset: 0x00 ( /W  32) Control Register */
  __IO  uint32_t                       DBGU_MR;            /**< Offset: 0x04 (R/W  32) Mode Register */
  __O   uint32_t                       DBGU_IER;           /**< Offset: 0x08 ( /W  32) Interrupt Enable Register */
  __O   uint32_t                       DBGU_IDR;           /**< Offset: 0x0C ( /W  32) Interrupt Disable Register */
  __I   uint32_t                       DBGU_IMR;           /**< Offset: 0x10 (R/   32) Interrupt Mask Register */
  __I   uint32_t                       DBGU_SR;            /**< Offset: 0x14 (R/   32) Status Register */
  __I   uint32_t                       DBGU_RHR;           /**< Offset: 0x18 (R/   32) Receive Holding Register */
  __O   uint32_t                       DBGU_THR;           /**< Offset: 0x1C ( /W  32) Transmit Holding Register */
  __IO  uint32_t                       DBGU_BRGR;          /**< Offset: 0x20 (R/W  32) Baud Rate Generator Register */
  __I   uint8_t                        Reserved1[0x04];
  __IO  uint32_t                       DBGU_RTOR;          /**< Offset: 0x28 (R/W  32) Receiver Timeout Register */
  __I   uint8_t                        Reserved2[0x14];
  __I   uint32_t                       DBGU_CIDR;          /**< Offset: 0x40 (R/   32) Chip ID Register */
  __I   uint32_t                       DBGU_EXID;          /**< Offset: 0x44 (R/   32) Chip ID Extension Register */
  __IO  uint32_t                       DBGU_FNR;           /**< Offset: 0x48 (R/W  32) Force NTRST Register */
  __I   uint8_t                        Reserved3[0x98];
  __IO  uint32_t                       DBGU_WPMR;          /**< Offset: 0xE4 (R/W  32) Write Protection Mode Register */
  __I   uint8_t                        Reserved4[0x14];
  __I   uint32_t                       DBGU_VERSION;       /**< Offset: 0xFC (R/   32) Version Register */
} dbgu_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAM9X_DBGU_COMPONENT_H_ */
