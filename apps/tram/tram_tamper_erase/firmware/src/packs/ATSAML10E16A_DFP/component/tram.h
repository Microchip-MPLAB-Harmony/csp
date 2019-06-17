/**
 * \brief Component description for TRAM
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

/* file generated from device description version 2019-06-07T05:54:14Z */
#ifndef _SAML10_TRAM_COMPONENT_H_
#define _SAML10_TRAM_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR TRAM                                         */
/* ************************************************************************** */

/* -------- TRAM_CTRLA : (TRAM Offset: 0x00) (R/W 8) Control -------- */
#define TRAM_CTRLA_RESETVALUE                 _U_(0x00)                                            /**<  (TRAM_CTRLA) Control  Reset Value */

#define TRAM_CTRLA_SWRST_Pos                  _U_(0)                                               /**< (TRAM_CTRLA) Software Reset Position */
#define TRAM_CTRLA_SWRST_Msk                  (_U_(0x1) << TRAM_CTRLA_SWRST_Pos)                   /**< (TRAM_CTRLA) Software Reset Mask */
#define TRAM_CTRLA_SWRST(value)               (TRAM_CTRLA_SWRST_Msk & ((value) << TRAM_CTRLA_SWRST_Pos))
#define TRAM_CTRLA_ENABLE_Pos                 _U_(1)                                               /**< (TRAM_CTRLA) Enable Position */
#define TRAM_CTRLA_ENABLE_Msk                 (_U_(0x1) << TRAM_CTRLA_ENABLE_Pos)                  /**< (TRAM_CTRLA) Enable Mask */
#define TRAM_CTRLA_ENABLE(value)              (TRAM_CTRLA_ENABLE_Msk & ((value) << TRAM_CTRLA_ENABLE_Pos))
#define TRAM_CTRLA_TAMPERS_Pos                _U_(4)                                               /**< (TRAM_CTRLA) Tamper Erase Position */
#define TRAM_CTRLA_TAMPERS_Msk                (_U_(0x1) << TRAM_CTRLA_TAMPERS_Pos)                 /**< (TRAM_CTRLA) Tamper Erase Mask */
#define TRAM_CTRLA_TAMPERS(value)             (TRAM_CTRLA_TAMPERS_Msk & ((value) << TRAM_CTRLA_TAMPERS_Pos))
#define TRAM_CTRLA_DRP_Pos                    _U_(6)                                               /**< (TRAM_CTRLA) Data Remanence Prevention Position */
#define TRAM_CTRLA_DRP_Msk                    (_U_(0x1) << TRAM_CTRLA_DRP_Pos)                     /**< (TRAM_CTRLA) Data Remanence Prevention Mask */
#define TRAM_CTRLA_DRP(value)                 (TRAM_CTRLA_DRP_Msk & ((value) << TRAM_CTRLA_DRP_Pos))
#define TRAM_CTRLA_SILACC_Pos                 _U_(7)                                               /**< (TRAM_CTRLA) Silent Access Position */
#define TRAM_CTRLA_SILACC_Msk                 (_U_(0x1) << TRAM_CTRLA_SILACC_Pos)                  /**< (TRAM_CTRLA) Silent Access Mask */
#define TRAM_CTRLA_SILACC(value)              (TRAM_CTRLA_SILACC_Msk & ((value) << TRAM_CTRLA_SILACC_Pos))
#define TRAM_CTRLA_Msk                        _U_(0xD3)                                            /**< (TRAM_CTRLA) Register Mask  */


/* -------- TRAM_INTENCLR : (TRAM Offset: 0x04) (R/W 8) Interrupt Enable Clear -------- */
#define TRAM_INTENCLR_RESETVALUE              _U_(0x00)                                            /**<  (TRAM_INTENCLR) Interrupt Enable Clear  Reset Value */

#define TRAM_INTENCLR_ERR_Pos                 _U_(0)                                               /**< (TRAM_INTENCLR) TrustRAM Readout Error Interrupt Enable Position */
#define TRAM_INTENCLR_ERR_Msk                 (_U_(0x1) << TRAM_INTENCLR_ERR_Pos)                  /**< (TRAM_INTENCLR) TrustRAM Readout Error Interrupt Enable Mask */
#define TRAM_INTENCLR_ERR(value)              (TRAM_INTENCLR_ERR_Msk & ((value) << TRAM_INTENCLR_ERR_Pos))
#define TRAM_INTENCLR_DRP_Pos                 _U_(1)                                               /**< (TRAM_INTENCLR) Data Remanence Prevention Ended Interrupt Enable Position */
#define TRAM_INTENCLR_DRP_Msk                 (_U_(0x1) << TRAM_INTENCLR_DRP_Pos)                  /**< (TRAM_INTENCLR) Data Remanence Prevention Ended Interrupt Enable Mask */
#define TRAM_INTENCLR_DRP(value)              (TRAM_INTENCLR_DRP_Msk & ((value) << TRAM_INTENCLR_DRP_Pos))
#define TRAM_INTENCLR_Msk                     _U_(0x03)                                            /**< (TRAM_INTENCLR) Register Mask  */


/* -------- TRAM_INTENSET : (TRAM Offset: 0x05) (R/W 8) Interrupt Enable Set -------- */
#define TRAM_INTENSET_RESETVALUE              _U_(0x00)                                            /**<  (TRAM_INTENSET) Interrupt Enable Set  Reset Value */

#define TRAM_INTENSET_ERR_Pos                 _U_(0)                                               /**< (TRAM_INTENSET) TrustRAM Readout Error Interrupt Enable Position */
#define TRAM_INTENSET_ERR_Msk                 (_U_(0x1) << TRAM_INTENSET_ERR_Pos)                  /**< (TRAM_INTENSET) TrustRAM Readout Error Interrupt Enable Mask */
#define TRAM_INTENSET_ERR(value)              (TRAM_INTENSET_ERR_Msk & ((value) << TRAM_INTENSET_ERR_Pos))
#define TRAM_INTENSET_DRP_Pos                 _U_(1)                                               /**< (TRAM_INTENSET) Data Remanence Prevention Ended Interrupt Enable Position */
#define TRAM_INTENSET_DRP_Msk                 (_U_(0x1) << TRAM_INTENSET_DRP_Pos)                  /**< (TRAM_INTENSET) Data Remanence Prevention Ended Interrupt Enable Mask */
#define TRAM_INTENSET_DRP(value)              (TRAM_INTENSET_DRP_Msk & ((value) << TRAM_INTENSET_DRP_Pos))
#define TRAM_INTENSET_Msk                     _U_(0x03)                                            /**< (TRAM_INTENSET) Register Mask  */


/* -------- TRAM_INTFLAG : (TRAM Offset: 0x06) (R/W 8) Interrupt Flag Status and Clear -------- */
#define TRAM_INTFLAG_RESETVALUE               _U_(0x00)                                            /**<  (TRAM_INTFLAG) Interrupt Flag Status and Clear  Reset Value */

#define TRAM_INTFLAG_ERR_Pos                  _U_(0)                                               /**< (TRAM_INTFLAG) TrustRAM Readout Error Position */
#define TRAM_INTFLAG_ERR_Msk                  (_U_(0x1) << TRAM_INTFLAG_ERR_Pos)                   /**< (TRAM_INTFLAG) TrustRAM Readout Error Mask */
#define TRAM_INTFLAG_ERR(value)               (TRAM_INTFLAG_ERR_Msk & ((value) << TRAM_INTFLAG_ERR_Pos))
#define TRAM_INTFLAG_DRP_Pos                  _U_(1)                                               /**< (TRAM_INTFLAG) Data Remanence Prevention Ended Position */
#define TRAM_INTFLAG_DRP_Msk                  (_U_(0x1) << TRAM_INTFLAG_DRP_Pos)                   /**< (TRAM_INTFLAG) Data Remanence Prevention Ended Mask */
#define TRAM_INTFLAG_DRP(value)               (TRAM_INTFLAG_DRP_Msk & ((value) << TRAM_INTFLAG_DRP_Pos))
#define TRAM_INTFLAG_Msk                      _U_(0x03)                                            /**< (TRAM_INTFLAG) Register Mask  */


/* -------- TRAM_STATUS : (TRAM Offset: 0x07) ( R/ 8) Status -------- */
#define TRAM_STATUS_RESETVALUE                _U_(0x00)                                            /**<  (TRAM_STATUS) Status  Reset Value */

#define TRAM_STATUS_RAMINV_Pos                _U_(0)                                               /**< (TRAM_STATUS) RAM Inversion Bit Position */
#define TRAM_STATUS_RAMINV_Msk                (_U_(0x1) << TRAM_STATUS_RAMINV_Pos)                 /**< (TRAM_STATUS) RAM Inversion Bit Mask */
#define TRAM_STATUS_RAMINV(value)             (TRAM_STATUS_RAMINV_Msk & ((value) << TRAM_STATUS_RAMINV_Pos))
#define TRAM_STATUS_DRP_Pos                   _U_(1)                                               /**< (TRAM_STATUS) Data Remanence Prevention Ongoing Position */
#define TRAM_STATUS_DRP_Msk                   (_U_(0x1) << TRAM_STATUS_DRP_Pos)                    /**< (TRAM_STATUS) Data Remanence Prevention Ongoing Mask */
#define TRAM_STATUS_DRP(value)                (TRAM_STATUS_DRP_Msk & ((value) << TRAM_STATUS_DRP_Pos))
#define TRAM_STATUS_Msk                       _U_(0x03)                                            /**< (TRAM_STATUS) Register Mask  */


/* -------- TRAM_SYNCBUSY : (TRAM Offset: 0x08) ( R/ 32) Synchronization Busy Status -------- */
#define TRAM_SYNCBUSY_RESETVALUE              _U_(0x00)                                            /**<  (TRAM_SYNCBUSY) Synchronization Busy Status  Reset Value */

#define TRAM_SYNCBUSY_SWRST_Pos               _U_(0)                                               /**< (TRAM_SYNCBUSY) Software Reset Busy Position */
#define TRAM_SYNCBUSY_SWRST_Msk               (_U_(0x1) << TRAM_SYNCBUSY_SWRST_Pos)                /**< (TRAM_SYNCBUSY) Software Reset Busy Mask */
#define TRAM_SYNCBUSY_SWRST(value)            (TRAM_SYNCBUSY_SWRST_Msk & ((value) << TRAM_SYNCBUSY_SWRST_Pos))
#define TRAM_SYNCBUSY_ENABLE_Pos              _U_(1)                                               /**< (TRAM_SYNCBUSY) Enable Busy Position */
#define TRAM_SYNCBUSY_ENABLE_Msk              (_U_(0x1) << TRAM_SYNCBUSY_ENABLE_Pos)               /**< (TRAM_SYNCBUSY) Enable Busy Mask */
#define TRAM_SYNCBUSY_ENABLE(value)           (TRAM_SYNCBUSY_ENABLE_Msk & ((value) << TRAM_SYNCBUSY_ENABLE_Pos))
#define TRAM_SYNCBUSY_Msk                     _U_(0x00000003)                                      /**< (TRAM_SYNCBUSY) Register Mask  */


/* -------- TRAM_DSCC : (TRAM Offset: 0x0C) ( /W 32) Data Scramble Control -------- */
#define TRAM_DSCC_RESETVALUE                  _U_(0x00)                                            /**<  (TRAM_DSCC) Data Scramble Control  Reset Value */

#define TRAM_DSCC_DSCKEY_Pos                  _U_(0)                                               /**< (TRAM_DSCC) Data Scramble Key Position */
#define TRAM_DSCC_DSCKEY_Msk                  (_U_(0x3FFFFFFF) << TRAM_DSCC_DSCKEY_Pos)            /**< (TRAM_DSCC) Data Scramble Key Mask */
#define TRAM_DSCC_DSCKEY(value)               (TRAM_DSCC_DSCKEY_Msk & ((value) << TRAM_DSCC_DSCKEY_Pos))
#define TRAM_DSCC_DSCEN_Pos                   _U_(31)                                              /**< (TRAM_DSCC) Data Scramble Enable Position */
#define TRAM_DSCC_DSCEN_Msk                   (_U_(0x1) << TRAM_DSCC_DSCEN_Pos)                    /**< (TRAM_DSCC) Data Scramble Enable Mask */
#define TRAM_DSCC_DSCEN(value)                (TRAM_DSCC_DSCEN_Msk & ((value) << TRAM_DSCC_DSCEN_Pos))
#define TRAM_DSCC_Msk                         _U_(0xBFFFFFFF)                                      /**< (TRAM_DSCC) Register Mask  */


/* -------- TRAM_PERMW : (TRAM Offset: 0x10) ( /W 8) Permutation Write -------- */
#define TRAM_PERMW_RESETVALUE                 _U_(0x00)                                            /**<  (TRAM_PERMW) Permutation Write  Reset Value */

#define TRAM_PERMW_DATA_Pos                   _U_(0)                                               /**< (TRAM_PERMW) Permutation Scrambler Data Input Position */
#define TRAM_PERMW_DATA_Msk                   (_U_(0x7) << TRAM_PERMW_DATA_Pos)                    /**< (TRAM_PERMW) Permutation Scrambler Data Input Mask */
#define TRAM_PERMW_DATA(value)                (TRAM_PERMW_DATA_Msk & ((value) << TRAM_PERMW_DATA_Pos))
#define TRAM_PERMW_Msk                        _U_(0x07)                                            /**< (TRAM_PERMW) Register Mask  */


/* -------- TRAM_PERMR : (TRAM Offset: 0x11) ( R/ 8) Permutation Read -------- */
#define TRAM_PERMR_RESETVALUE                 _U_(0x00)                                            /**<  (TRAM_PERMR) Permutation Read  Reset Value */

#define TRAM_PERMR_DATA_Pos                   _U_(0)                                               /**< (TRAM_PERMR) Permutation Scrambler Data Output Position */
#define TRAM_PERMR_DATA_Msk                   (_U_(0x7) << TRAM_PERMR_DATA_Pos)                    /**< (TRAM_PERMR) Permutation Scrambler Data Output Mask */
#define TRAM_PERMR_DATA(value)                (TRAM_PERMR_DATA_Msk & ((value) << TRAM_PERMR_DATA_Pos))
#define TRAM_PERMR_Msk                        _U_(0x07)                                            /**< (TRAM_PERMR) Register Mask  */


/* -------- TRAM_RAM : (TRAM Offset: 0x100) (R/W 32) TrustRAM -------- */
#define TRAM_RAM_RESETVALUE                   _U_(0x00)                                            /**<  (TRAM_RAM) TrustRAM  Reset Value */

#define TRAM_RAM_DATA_Pos                     _U_(0)                                               /**< (TRAM_RAM) Trust RAM Data Position */
#define TRAM_RAM_DATA_Msk                     (_U_(0xFFFFFFFF) << TRAM_RAM_DATA_Pos)               /**< (TRAM_RAM) Trust RAM Data Mask */
#define TRAM_RAM_DATA(value)                  (TRAM_RAM_DATA_Msk & ((value) << TRAM_RAM_DATA_Pos))
#define TRAM_RAM_Msk                          _U_(0xFFFFFFFF)                                      /**< (TRAM_RAM) Register Mask  */


/** \brief TRAM register offsets definitions */
#define TRAM_CTRLA_REG_OFST            (0x00)              /**< (TRAM_CTRLA) Control Offset */
#define TRAM_INTENCLR_REG_OFST         (0x04)              /**< (TRAM_INTENCLR) Interrupt Enable Clear Offset */
#define TRAM_INTENSET_REG_OFST         (0x05)              /**< (TRAM_INTENSET) Interrupt Enable Set Offset */
#define TRAM_INTFLAG_REG_OFST          (0x06)              /**< (TRAM_INTFLAG) Interrupt Flag Status and Clear Offset */
#define TRAM_STATUS_REG_OFST           (0x07)              /**< (TRAM_STATUS) Status Offset */
#define TRAM_SYNCBUSY_REG_OFST         (0x08)              /**< (TRAM_SYNCBUSY) Synchronization Busy Status Offset */
#define TRAM_DSCC_REG_OFST             (0x0C)              /**< (TRAM_DSCC) Data Scramble Control Offset */
#define TRAM_PERMW_REG_OFST            (0x10)              /**< (TRAM_PERMW) Permutation Write Offset */
#define TRAM_PERMR_REG_OFST            (0x11)              /**< (TRAM_PERMR) Permutation Read Offset */
#define TRAM_RAM_REG_OFST              (0x100)             /**< (TRAM_RAM) TrustRAM Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief TRAM register API structure */
typedef struct
{  /* TrustRAM */
  __IO  uint8_t                        TRAM_CTRLA;         /**< Offset: 0x00 (R/W  8) Control */
  __I   uint8_t                        Reserved1[0x03];
  __IO  uint8_t                        TRAM_INTENCLR;      /**< Offset: 0x04 (R/W  8) Interrupt Enable Clear */
  __IO  uint8_t                        TRAM_INTENSET;      /**< Offset: 0x05 (R/W  8) Interrupt Enable Set */
  __IO  uint8_t                        TRAM_INTFLAG;       /**< Offset: 0x06 (R/W  8) Interrupt Flag Status and Clear */
  __I   uint8_t                        TRAM_STATUS;        /**< Offset: 0x07 (R/   8) Status */
  __I   uint32_t                       TRAM_SYNCBUSY;      /**< Offset: 0x08 (R/   32) Synchronization Busy Status */
  __O   uint32_t                       TRAM_DSCC;          /**< Offset: 0x0C ( /W  32) Data Scramble Control */
  __O   uint8_t                        TRAM_PERMW;         /**< Offset: 0x10 ( /W  8) Permutation Write */
  __I   uint8_t                        TRAM_PERMR;         /**< Offset: 0x11 (R/   8) Permutation Read */
  __I   uint8_t                        Reserved2[0xEE];
  __IO  uint32_t                       TRAM_RAM[64];       /**< Offset: 0x100 (R/W  32) TrustRAM */
} tram_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAML10_TRAM_COMPONENT_H_ */
