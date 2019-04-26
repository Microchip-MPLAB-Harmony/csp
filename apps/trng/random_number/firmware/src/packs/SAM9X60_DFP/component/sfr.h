/**
 * \brief Component description for SFR
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
#ifndef _SAM9X_SFR_COMPONENT_H_
#define _SAM9X_SFR_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR SFR                                          */
/* ************************************************************************** */

/* -------- SFR_CCFG_EBICSA : (SFR Offset: 0x04) (R/W 32) EBI Chip Select Register -------- */
#define SFR_CCFG_EBICSA_EBI_CS1A_Pos          _U_(1)                                               /**< (SFR_CCFG_EBICSA) EBI Chip Select 1 Assignment Position */
#define SFR_CCFG_EBICSA_EBI_CS1A_Msk          (_U_(0x1) << SFR_CCFG_EBICSA_EBI_CS1A_Pos)           /**< (SFR_CCFG_EBICSA) EBI Chip Select 1 Assignment Mask */
#define SFR_CCFG_EBICSA_EBI_CS1A(value)       (SFR_CCFG_EBICSA_EBI_CS1A_Msk & ((value) << SFR_CCFG_EBICSA_EBI_CS1A_Pos))
#define SFR_CCFG_EBICSA_EBI_CS3A_Pos          _U_(3)                                               /**< (SFR_CCFG_EBICSA) EBI Chip Select 3 Assignment Position */
#define SFR_CCFG_EBICSA_EBI_CS3A_Msk          (_U_(0x1) << SFR_CCFG_EBICSA_EBI_CS3A_Pos)           /**< (SFR_CCFG_EBICSA) EBI Chip Select 3 Assignment Mask */
#define SFR_CCFG_EBICSA_EBI_CS3A(value)       (SFR_CCFG_EBICSA_EBI_CS3A_Msk & ((value) << SFR_CCFG_EBICSA_EBI_CS3A_Pos))
#define SFR_CCFG_EBICSA_EBI_CS4A_Pos          _U_(4)                                               /**< (SFR_CCFG_EBICSA) EBI Chip Select 4 Assignment Position */
#define SFR_CCFG_EBICSA_EBI_CS4A_Msk          (_U_(0x1) << SFR_CCFG_EBICSA_EBI_CS4A_Pos)           /**< (SFR_CCFG_EBICSA) EBI Chip Select 4 Assignment Mask */
#define SFR_CCFG_EBICSA_EBI_CS4A(value)       (SFR_CCFG_EBICSA_EBI_CS4A_Msk & ((value) << SFR_CCFG_EBICSA_EBI_CS4A_Pos))
#define SFR_CCFG_EBICSA_EBI_CS5A_Pos          _U_(5)                                               /**< (SFR_CCFG_EBICSA) EBI Chip Select 5 Assignment Position */
#define SFR_CCFG_EBICSA_EBI_CS5A_Msk          (_U_(0x1) << SFR_CCFG_EBICSA_EBI_CS5A_Pos)           /**< (SFR_CCFG_EBICSA) EBI Chip Select 5 Assignment Mask */
#define SFR_CCFG_EBICSA_EBI_CS5A(value)       (SFR_CCFG_EBICSA_EBI_CS5A_Msk & ((value) << SFR_CCFG_EBICSA_EBI_CS5A_Pos))
#define SFR_CCFG_EBICSA_EBI_DBPUC_Pos         _U_(8)                                               /**< (SFR_CCFG_EBICSA) EBI Data Bus Pullup Configuration Position */
#define SFR_CCFG_EBICSA_EBI_DBPUC_Msk         (_U_(0x1) << SFR_CCFG_EBICSA_EBI_DBPUC_Pos)          /**< (SFR_CCFG_EBICSA) EBI Data Bus Pullup Configuration Mask */
#define SFR_CCFG_EBICSA_EBI_DBPUC(value)      (SFR_CCFG_EBICSA_EBI_DBPUC_Msk & ((value) << SFR_CCFG_EBICSA_EBI_DBPUC_Pos))
#define SFR_CCFG_EBICSA_EBI_DBPDC_Pos         _U_(9)                                               /**< (SFR_CCFG_EBICSA) EBI Data Bus Pulldown Configuration Position */
#define SFR_CCFG_EBICSA_EBI_DBPDC_Msk         (_U_(0x1) << SFR_CCFG_EBICSA_EBI_DBPDC_Pos)          /**< (SFR_CCFG_EBICSA) EBI Data Bus Pulldown Configuration Mask */
#define SFR_CCFG_EBICSA_EBI_DBPDC(value)      (SFR_CCFG_EBICSA_EBI_DBPDC_Msk & ((value) << SFR_CCFG_EBICSA_EBI_DBPDC_Pos))
#define SFR_CCFG_EBICSA_EBI_DRIVE_Pos         _U_(16)                                              /**< (SFR_CCFG_EBICSA) EBI I/O Drive Configuration Position */
#define SFR_CCFG_EBICSA_EBI_DRIVE_Msk         (_U_(0x1) << SFR_CCFG_EBICSA_EBI_DRIVE_Pos)          /**< (SFR_CCFG_EBICSA) EBI I/O Drive Configuration Mask */
#define SFR_CCFG_EBICSA_EBI_DRIVE(value)      (SFR_CCFG_EBICSA_EBI_DRIVE_Msk & ((value) << SFR_CCFG_EBICSA_EBI_DRIVE_Pos))
#define SFR_CCFG_EBICSA_DQIEN_F_Pos           _U_(20)                                              /**< (SFR_CCFG_EBICSA) Force Analog Input Comparator Configuration Position */
#define SFR_CCFG_EBICSA_DQIEN_F_Msk           (_U_(0x1) << SFR_CCFG_EBICSA_DQIEN_F_Pos)            /**< (SFR_CCFG_EBICSA) Force Analog Input Comparator Configuration Mask */
#define SFR_CCFG_EBICSA_DQIEN_F(value)        (SFR_CCFG_EBICSA_DQIEN_F_Msk & ((value) << SFR_CCFG_EBICSA_DQIEN_F_Pos))
#define SFR_CCFG_EBICSA_NFD0_ON_D16_Pos       _U_(24)                                              /**< (SFR_CCFG_EBICSA) NAND Flash Databus Selection Position */
#define SFR_CCFG_EBICSA_NFD0_ON_D16_Msk       (_U_(0x1) << SFR_CCFG_EBICSA_NFD0_ON_D16_Pos)        /**< (SFR_CCFG_EBICSA) NAND Flash Databus Selection Mask */
#define SFR_CCFG_EBICSA_NFD0_ON_D16(value)    (SFR_CCFG_EBICSA_NFD0_ON_D16_Msk & ((value) << SFR_CCFG_EBICSA_NFD0_ON_D16_Pos))
#define SFR_CCFG_EBICSA_DDR_MP_EN_Pos         _U_(25)                                              /**< (SFR_CCFG_EBICSA) DDR Multi-port Enable Position */
#define SFR_CCFG_EBICSA_DDR_MP_EN_Msk         (_U_(0x1) << SFR_CCFG_EBICSA_DDR_MP_EN_Pos)          /**< (SFR_CCFG_EBICSA) DDR Multi-port Enable Mask */
#define SFR_CCFG_EBICSA_DDR_MP_EN(value)      (SFR_CCFG_EBICSA_DDR_MP_EN_Msk & ((value) << SFR_CCFG_EBICSA_DDR_MP_EN_Pos))
#define SFR_CCFG_EBICSA_Msk                   _U_(0x0311033A)                                      /**< (SFR_CCFG_EBICSA) Register Mask  */

#define SFR_CCFG_EBICSA_NFD0_ON_D_Pos         _U_(24)                                              /**< (SFR_CCFG_EBICSA Position) NAND Flash Databus Selection */
#define SFR_CCFG_EBICSA_NFD0_ON_D_Msk         (_U_(0x1) << SFR_CCFG_EBICSA_NFD0_ON_D_Pos)          /**< (SFR_CCFG_EBICSA Mask) NFD0_ON_D */
#define SFR_CCFG_EBICSA_NFD0_ON_D(value)      (SFR_CCFG_EBICSA_NFD0_ON_D_Msk & ((value) << SFR_CCFG_EBICSA_NFD0_ON_D_Pos)) 

/* -------- SFR_OHCIICR : (SFR Offset: 0x10) (R/W 32) OHCI Interrupt Configuration Register -------- */
#define SFR_OHCIICR_RES0_Pos                  _U_(0)                                               /**< (SFR_OHCIICR) USB PORTx Reset Position */
#define SFR_OHCIICR_RES0_Msk                  (_U_(0x1) << SFR_OHCIICR_RES0_Pos)                   /**< (SFR_OHCIICR) USB PORTx Reset Mask */
#define SFR_OHCIICR_RES0(value)               (SFR_OHCIICR_RES0_Msk & ((value) << SFR_OHCIICR_RES0_Pos))
#define SFR_OHCIICR_RES1_Pos                  _U_(1)                                               /**< (SFR_OHCIICR) USB PORTx Reset Position */
#define SFR_OHCIICR_RES1_Msk                  (_U_(0x1) << SFR_OHCIICR_RES1_Pos)                   /**< (SFR_OHCIICR) USB PORTx Reset Mask */
#define SFR_OHCIICR_RES1(value)               (SFR_OHCIICR_RES1_Msk & ((value) << SFR_OHCIICR_RES1_Pos))
#define SFR_OHCIICR_RES2_Pos                  _U_(2)                                               /**< (SFR_OHCIICR) USB PORTx Reset Position */
#define SFR_OHCIICR_RES2_Msk                  (_U_(0x1) << SFR_OHCIICR_RES2_Pos)                   /**< (SFR_OHCIICR) USB PORTx Reset Mask */
#define SFR_OHCIICR_RES2(value)               (SFR_OHCIICR_RES2_Msk & ((value) << SFR_OHCIICR_RES2_Pos))
#define SFR_OHCIICR_ARIE_Pos                  _U_(4)                                               /**< (SFR_OHCIICR) OHCI Asynchronous Resume Interrupt Enable Position */
#define SFR_OHCIICR_ARIE_Msk                  (_U_(0x1) << SFR_OHCIICR_ARIE_Pos)                   /**< (SFR_OHCIICR) OHCI Asynchronous Resume Interrupt Enable Mask */
#define SFR_OHCIICR_ARIE(value)               (SFR_OHCIICR_ARIE_Msk & ((value) << SFR_OHCIICR_ARIE_Pos))
#define SFR_OHCIICR_APPSTART_Pos              _U_(5)                                               /**< (SFR_OHCIICR) OHCI Clock Start Position */
#define SFR_OHCIICR_APPSTART_Msk              (_U_(0x1) << SFR_OHCIICR_APPSTART_Pos)               /**< (SFR_OHCIICR) OHCI Clock Start Mask */
#define SFR_OHCIICR_APPSTART(value)           (SFR_OHCIICR_APPSTART_Msk & ((value) << SFR_OHCIICR_APPSTART_Pos))
#define SFR_OHCIICR_SUSP0_Pos                 _U_(8)                                               /**< (SFR_OHCIICR) USB PORTx Position */
#define SFR_OHCIICR_SUSP0_Msk                 (_U_(0x1) << SFR_OHCIICR_SUSP0_Pos)                  /**< (SFR_OHCIICR) USB PORTx Mask */
#define SFR_OHCIICR_SUSP0(value)              (SFR_OHCIICR_SUSP0_Msk & ((value) << SFR_OHCIICR_SUSP0_Pos))
#define SFR_OHCIICR_SUSP1_Pos                 _U_(9)                                               /**< (SFR_OHCIICR) USB PORTx Position */
#define SFR_OHCIICR_SUSP1_Msk                 (_U_(0x1) << SFR_OHCIICR_SUSP1_Pos)                  /**< (SFR_OHCIICR) USB PORTx Mask */
#define SFR_OHCIICR_SUSP1(value)              (SFR_OHCIICR_SUSP1_Msk & ((value) << SFR_OHCIICR_SUSP1_Pos))
#define SFR_OHCIICR_SUSP2_Pos                 _U_(10)                                              /**< (SFR_OHCIICR) USB PORTx Position */
#define SFR_OHCIICR_SUSP2_Msk                 (_U_(0x1) << SFR_OHCIICR_SUSP2_Pos)                  /**< (SFR_OHCIICR) USB PORTx Mask */
#define SFR_OHCIICR_SUSP2(value)              (SFR_OHCIICR_SUSP2_Msk & ((value) << SFR_OHCIICR_SUSP2_Pos))
#define SFR_OHCIICR_UDPPUDIS_Pos              _U_(23)                                              /**< (SFR_OHCIICR) USB Device Pullup Disable Position */
#define SFR_OHCIICR_UDPPUDIS_Msk              (_U_(0x1) << SFR_OHCIICR_UDPPUDIS_Pos)               /**< (SFR_OHCIICR) USB Device Pullup Disable Mask */
#define SFR_OHCIICR_UDPPUDIS(value)           (SFR_OHCIICR_UDPPUDIS_Msk & ((value) << SFR_OHCIICR_UDPPUDIS_Pos))
#define SFR_OHCIICR_Msk                       _U_(0x00800737)                                      /**< (SFR_OHCIICR) Register Mask  */

#define SFR_OHCIICR_RES_Pos                   _U_(0)                                               /**< (SFR_OHCIICR Position) USB PORTx Reset */
#define SFR_OHCIICR_RES_Msk                   (_U_(0x7) << SFR_OHCIICR_RES_Pos)                    /**< (SFR_OHCIICR Mask) RES */
#define SFR_OHCIICR_RES(value)                (SFR_OHCIICR_RES_Msk & ((value) << SFR_OHCIICR_RES_Pos)) 
#define SFR_OHCIICR_SUSP_Pos                  _U_(8)                                               /**< (SFR_OHCIICR Position) USB PORTx */
#define SFR_OHCIICR_SUSP_Msk                  (_U_(0x7) << SFR_OHCIICR_SUSP_Pos)                   /**< (SFR_OHCIICR Mask) SUSP */
#define SFR_OHCIICR_SUSP(value)               (SFR_OHCIICR_SUSP_Msk & ((value) << SFR_OHCIICR_SUSP_Pos)) 

/* -------- SFR_OHCIISR : (SFR Offset: 0x14) ( R/ 32) OHCI Interrupt Status Register -------- */
#define SFR_OHCIISR_RIS0_Pos                  _U_(0)                                               /**< (SFR_OHCIISR) OHCI Resume Interrupt Status Port 0 Position */
#define SFR_OHCIISR_RIS0_Msk                  (_U_(0x1) << SFR_OHCIISR_RIS0_Pos)                   /**< (SFR_OHCIISR) OHCI Resume Interrupt Status Port 0 Mask */
#define SFR_OHCIISR_RIS0(value)               (SFR_OHCIISR_RIS0_Msk & ((value) << SFR_OHCIISR_RIS0_Pos))
#define SFR_OHCIISR_RIS1_Pos                  _U_(1)                                               /**< (SFR_OHCIISR) OHCI Resume Interrupt Status Port 1 Position */
#define SFR_OHCIISR_RIS1_Msk                  (_U_(0x1) << SFR_OHCIISR_RIS1_Pos)                   /**< (SFR_OHCIISR) OHCI Resume Interrupt Status Port 1 Mask */
#define SFR_OHCIISR_RIS1(value)               (SFR_OHCIISR_RIS1_Msk & ((value) << SFR_OHCIISR_RIS1_Pos))
#define SFR_OHCIISR_RIS2_Pos                  _U_(2)                                               /**< (SFR_OHCIISR) OHCI Resume Interrupt Status Port 2 Position */
#define SFR_OHCIISR_RIS2_Msk                  (_U_(0x1) << SFR_OHCIISR_RIS2_Pos)                   /**< (SFR_OHCIISR) OHCI Resume Interrupt Status Port 2 Mask */
#define SFR_OHCIISR_RIS2(value)               (SFR_OHCIISR_RIS2_Msk & ((value) << SFR_OHCIISR_RIS2_Pos))
#define SFR_OHCIISR_Msk                       _U_(0x00000007)                                      /**< (SFR_OHCIISR) Register Mask  */

#define SFR_OHCIISR_RIS_Pos                   _U_(0)                                               /**< (SFR_OHCIISR Position) OHCI Resume Interrupt Status Port 2 */
#define SFR_OHCIISR_RIS_Msk                   (_U_(0x7) << SFR_OHCIISR_RIS_Pos)                    /**< (SFR_OHCIISR Mask) RIS */
#define SFR_OHCIISR_RIS(value)                (SFR_OHCIISR_RIS_Msk & ((value) << SFR_OHCIISR_RIS_Pos)) 

/* -------- SFR_BU_OTPC_CONF_R0 : (SFR Offset: 0x18) (R/W 32) OTPC Configuration 0 Register (BackUp) -------- */
#define SFR_BU_OTPC_CONF_R0_ROM_READ_Pos      _U_(0)                                               /**< (SFR_BU_OTPC_CONF_R0) Reading of ROM (OTP part only) Position */
#define SFR_BU_OTPC_CONF_R0_ROM_READ_Msk      (_U_(0x1) << SFR_BU_OTPC_CONF_R0_ROM_READ_Pos)       /**< (SFR_BU_OTPC_CONF_R0) Reading of ROM (OTP part only) Mask */
#define SFR_BU_OTPC_CONF_R0_ROM_READ(value)   (SFR_BU_OTPC_CONF_R0_ROM_READ_Msk & ((value) << SFR_BU_OTPC_CONF_R0_ROM_READ_Pos))
#define   SFR_BU_OTPC_CONF_R0_ROM_READ_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables reading of the ROM (OTP part only).  */
#define   SFR_BU_OTPC_CONF_R0_ROM_READ_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables reading of the ROM (OTP part only).  */
#define SFR_BU_OTPC_CONF_R0_ROM_READ_ENABLE   (SFR_BU_OTPC_CONF_R0_ROM_READ_ENABLE_Val << SFR_BU_OTPC_CONF_R0_ROM_READ_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables reading of the ROM (OTP part only). Position  */
#define SFR_BU_OTPC_CONF_R0_ROM_READ_DISABLE  (SFR_BU_OTPC_CONF_R0_ROM_READ_DISABLE_Val << SFR_BU_OTPC_CONF_R0_ROM_READ_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables reading of the ROM (OTP part only). Position  */
#define SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_Pos   _U_(1)                                               /**< (SFR_BU_OTPC_CONF_R0) Programming of ROM (OTP part only) Position */
#define SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_Msk   (_U_(0x1) << SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_Pos)    /**< (SFR_BU_OTPC_CONF_R0) Programming of ROM (OTP part only) Mask */
#define SFR_BU_OTPC_CONF_R0_ROM_PROGRAM(value) (SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the ROM (OTP part only).  */
#define   SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the ROM (OTP part only).  */
#define SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the ROM (OTP part only). Position  */
#define SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R0_ROM_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the ROM (OTP part only). Position  */
#define SFR_BU_OTPC_CONF_R0_PU_READ_Pos       _U_(2)                                               /**< (SFR_BU_OTPC_CONF_R0) Reading of Patch Unit Position */
#define SFR_BU_OTPC_CONF_R0_PU_READ_Msk       (_U_(0x1) << SFR_BU_OTPC_CONF_R0_PU_READ_Pos)        /**< (SFR_BU_OTPC_CONF_R0) Reading of Patch Unit Mask */
#define SFR_BU_OTPC_CONF_R0_PU_READ(value)    (SFR_BU_OTPC_CONF_R0_PU_READ_Msk & ((value) << SFR_BU_OTPC_CONF_R0_PU_READ_Pos))
#define   SFR_BU_OTPC_CONF_R0_PU_READ_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables reading of the patch unit.  */
#define   SFR_BU_OTPC_CONF_R0_PU_READ_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables reading of the patch unit.  */
#define SFR_BU_OTPC_CONF_R0_PU_READ_ENABLE    (SFR_BU_OTPC_CONF_R0_PU_READ_ENABLE_Val << SFR_BU_OTPC_CONF_R0_PU_READ_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables reading of the patch unit. Position  */
#define SFR_BU_OTPC_CONF_R0_PU_READ_DISABLE   (SFR_BU_OTPC_CONF_R0_PU_READ_DISABLE_Val << SFR_BU_OTPC_CONF_R0_PU_READ_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables reading of the patch unit. Position  */
#define SFR_BU_OTPC_CONF_R0_PU_PROGRAM_Pos    _U_(3)                                               /**< (SFR_BU_OTPC_CONF_R0) Programming of Patch Unit Position */
#define SFR_BU_OTPC_CONF_R0_PU_PROGRAM_Msk    (_U_(0x1) << SFR_BU_OTPC_CONF_R0_PU_PROGRAM_Pos)     /**< (SFR_BU_OTPC_CONF_R0) Programming of Patch Unit Mask */
#define SFR_BU_OTPC_CONF_R0_PU_PROGRAM(value) (SFR_BU_OTPC_CONF_R0_PU_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R0_PU_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R0_PU_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the patch unit.  */
#define   SFR_BU_OTPC_CONF_R0_PU_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the patch unit.  */
#define SFR_BU_OTPC_CONF_R0_PU_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R0_PU_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R0_PU_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the patch unit. Position  */
#define SFR_BU_OTPC_CONF_R0_PU_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R0_PU_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R0_PU_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the patch unit. Position  */
#define SFR_BU_OTPC_CONF_R0_ENGI_READ_Pos     _U_(4)                                               /**< (SFR_BU_OTPC_CONF_R0) Reading of Engineering Area Position */
#define SFR_BU_OTPC_CONF_R0_ENGI_READ_Msk     (_U_(0x1) << SFR_BU_OTPC_CONF_R0_ENGI_READ_Pos)      /**< (SFR_BU_OTPC_CONF_R0) Reading of Engineering Area Mask */
#define SFR_BU_OTPC_CONF_R0_ENGI_READ(value)  (SFR_BU_OTPC_CONF_R0_ENGI_READ_Msk & ((value) << SFR_BU_OTPC_CONF_R0_ENGI_READ_Pos))
#define   SFR_BU_OTPC_CONF_R0_ENGI_READ_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables reading of the engineering area.  */
#define   SFR_BU_OTPC_CONF_R0_ENGI_READ_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables reading of the engineering area.  */
#define SFR_BU_OTPC_CONF_R0_ENGI_READ_ENABLE  (SFR_BU_OTPC_CONF_R0_ENGI_READ_ENABLE_Val << SFR_BU_OTPC_CONF_R0_ENGI_READ_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables reading of the engineering area. Position  */
#define SFR_BU_OTPC_CONF_R0_ENGI_READ_DISABLE (SFR_BU_OTPC_CONF_R0_ENGI_READ_DISABLE_Val << SFR_BU_OTPC_CONF_R0_ENGI_READ_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables reading of the engineering area. Position  */
#define SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_Pos  _U_(5)                                               /**< (SFR_BU_OTPC_CONF_R0) Programming of Engineering Area Position */
#define SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_Msk  (_U_(0x1) << SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_Pos)   /**< (SFR_BU_OTPC_CONF_R0) Programming of Engineering Area Mask */
#define SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM(value) (SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the engineering area.  */
#define   SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the engineering area.  */
#define SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the engineering area. Position  */
#define SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R0_ENGI_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the engineering area. Position  */
#define SFR_BU_OTPC_CONF_R0_USER_READ_Pos     _U_(6)                                               /**< (SFR_BU_OTPC_CONF_R0) Reading of User Area Position */
#define SFR_BU_OTPC_CONF_R0_USER_READ_Msk     (_U_(0x1) << SFR_BU_OTPC_CONF_R0_USER_READ_Pos)      /**< (SFR_BU_OTPC_CONF_R0) Reading of User Area Mask */
#define SFR_BU_OTPC_CONF_R0_USER_READ(value)  (SFR_BU_OTPC_CONF_R0_USER_READ_Msk & ((value) << SFR_BU_OTPC_CONF_R0_USER_READ_Pos))
#define   SFR_BU_OTPC_CONF_R0_USER_READ_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables reading of the user area.  */
#define   SFR_BU_OTPC_CONF_R0_USER_READ_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables reading of the user area.  */
#define SFR_BU_OTPC_CONF_R0_USER_READ_ENABLE  (SFR_BU_OTPC_CONF_R0_USER_READ_ENABLE_Val << SFR_BU_OTPC_CONF_R0_USER_READ_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables reading of the user area. Position  */
#define SFR_BU_OTPC_CONF_R0_USER_READ_DISABLE (SFR_BU_OTPC_CONF_R0_USER_READ_DISABLE_Val << SFR_BU_OTPC_CONF_R0_USER_READ_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables reading of the user area. Position  */
#define SFR_BU_OTPC_CONF_R0_USER_PROGRAM_Pos  _U_(7)                                               /**< (SFR_BU_OTPC_CONF_R0) Programming of User Area Position */
#define SFR_BU_OTPC_CONF_R0_USER_PROGRAM_Msk  (_U_(0x1) << SFR_BU_OTPC_CONF_R0_USER_PROGRAM_Pos)   /**< (SFR_BU_OTPC_CONF_R0) Programming of User Area Mask */
#define SFR_BU_OTPC_CONF_R0_USER_PROGRAM(value) (SFR_BU_OTPC_CONF_R0_USER_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R0_USER_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R0_USER_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the user area.  */
#define   SFR_BU_OTPC_CONF_R0_USER_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the user area.  */
#define SFR_BU_OTPC_CONF_R0_USER_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R0_USER_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R0_USER_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the user area. Position  */
#define SFR_BU_OTPC_CONF_R0_USER_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R0_USER_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R0_USER_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the user area. Position  */
#define SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_Pos _U_(8)                                               /**< (SFR_BU_OTPC_CONF_R0) Invalidation of Product UID Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_Msk (_U_(0x1) << SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Invalidation of Product UID Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE(value) (SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_Pos))
#define   SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the Product UID special packet.  */
#define   SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the Product UID special packet.  */
#define SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_ENABLE (SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the Product UID special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_DISABLE (SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_PUID_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the Product UID special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_PUID_LOCK_Pos     _U_(9)                                               /**< (SFR_BU_OTPC_CONF_R0) Lock of Product UID Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_PUID_LOCK_Msk     (_U_(0x1) << SFR_BU_OTPC_CONF_R0_PUID_LOCK_Pos)      /**< (SFR_BU_OTPC_CONF_R0) Lock of Product UID Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_PUID_LOCK(value)  (SFR_BU_OTPC_CONF_R0_PUID_LOCK_Msk & ((value) << SFR_BU_OTPC_CONF_R0_PUID_LOCK_Pos))
#define   SFR_BU_OTPC_CONF_R0_PUID_LOCK_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the Product UID special packet.  */
#define   SFR_BU_OTPC_CONF_R0_PUID_LOCK_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the Product UID special packet.  */
#define SFR_BU_OTPC_CONF_R0_PUID_LOCK_ENABLE  (SFR_BU_OTPC_CONF_R0_PUID_LOCK_ENABLE_Val << SFR_BU_OTPC_CONF_R0_PUID_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the Product UID special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_PUID_LOCK_DISABLE (SFR_BU_OTPC_CONF_R0_PUID_LOCK_DISABLE_Val << SFR_BU_OTPC_CONF_R0_PUID_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the Product UID special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_PUID_PARSE_Pos    _U_(10)                                              /**< (SFR_BU_OTPC_CONF_R0) Parsing of Product UID Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_PUID_PARSE_Msk    (_U_(0x1) << SFR_BU_OTPC_CONF_R0_PUID_PARSE_Pos)     /**< (SFR_BU_OTPC_CONF_R0) Parsing of Product UID Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_PUID_PARSE(value) (SFR_BU_OTPC_CONF_R0_PUID_PARSE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_PUID_PARSE_Pos))
#define   SFR_BU_OTPC_CONF_R0_PUID_PARSE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the Product UID special packet.  */
#define   SFR_BU_OTPC_CONF_R0_PUID_PARSE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the Product UID special packet.  */
#define SFR_BU_OTPC_CONF_R0_PUID_PARSE_ENABLE (SFR_BU_OTPC_CONF_R0_PUID_PARSE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_PUID_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the Product UID special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_PUID_PARSE_DISABLE (SFR_BU_OTPC_CONF_R0_PUID_PARSE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_PUID_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the Product UID special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_Pos  _U_(11)                                              /**< (SFR_BU_OTPC_CONF_R0) Programming of Product UID Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_Msk  (_U_(0x1) << SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_Pos)   /**< (SFR_BU_OTPC_CONF_R0) Programming of Product UID Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_PUID_PROGRAM(value) (SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the Product UID special packet.  */
#define   SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the Product UID special packet.  */
#define SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the Product UID special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R0_PUID_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the Product UID special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_Pos _U_(12)                                              /**< (SFR_BU_OTPC_CONF_R0) Invalidation of Engineering Hardware Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_Msk (_U_(0x1) << SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Invalidation of Engineering Hardware Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE(value) (SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_Pos))
#define   SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the Engineering Hardware Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the Engineering Hardware Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_ENABLE (SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the Engineering Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_DISABLE (SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_EHC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the Engineering Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_EHC_LOCK_Pos      _U_(13)                                              /**< (SFR_BU_OTPC_CONF_R0) Lock of Engineering Hardware Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_EHC_LOCK_Msk      (_U_(0x1) << SFR_BU_OTPC_CONF_R0_EHC_LOCK_Pos)       /**< (SFR_BU_OTPC_CONF_R0) Lock of Engineering Hardware Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_EHC_LOCK(value)   (SFR_BU_OTPC_CONF_R0_EHC_LOCK_Msk & ((value) << SFR_BU_OTPC_CONF_R0_EHC_LOCK_Pos))
#define   SFR_BU_OTPC_CONF_R0_EHC_LOCK_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the Engineering Hardware Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_EHC_LOCK_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the Engineering Hardware Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_EHC_LOCK_ENABLE   (SFR_BU_OTPC_CONF_R0_EHC_LOCK_ENABLE_Val << SFR_BU_OTPC_CONF_R0_EHC_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the Engineering Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_EHC_LOCK_DISABLE  (SFR_BU_OTPC_CONF_R0_EHC_LOCK_DISABLE_Val << SFR_BU_OTPC_CONF_R0_EHC_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the Engineering Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_EHC_PARSE_Pos     _U_(14)                                              /**< (SFR_BU_OTPC_CONF_R0) Parsing of Engineering Hardware Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_EHC_PARSE_Msk     (_U_(0x1) << SFR_BU_OTPC_CONF_R0_EHC_PARSE_Pos)      /**< (SFR_BU_OTPC_CONF_R0) Parsing of Engineering Hardware Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_EHC_PARSE(value)  (SFR_BU_OTPC_CONF_R0_EHC_PARSE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_EHC_PARSE_Pos))
#define   SFR_BU_OTPC_CONF_R0_EHC_PARSE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the Engineering Hardware Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_EHC_PARSE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the Engineering Hardware Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_EHC_PARSE_ENABLE  (SFR_BU_OTPC_CONF_R0_EHC_PARSE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_EHC_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the Engineering Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_EHC_PARSE_DISABLE (SFR_BU_OTPC_CONF_R0_EHC_PARSE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_EHC_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the Engineering Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_Pos   _U_(15)                                              /**< (SFR_BU_OTPC_CONF_R0) Programming of Engineering Hardware Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_Msk   (_U_(0x1) << SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_Pos)    /**< (SFR_BU_OTPC_CONF_R0) Programming of Engineering Hardware Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_EHC_PROGRAM(value) (SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the Engineering Hardware Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the Engineering Hardware Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the Engineering Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R0_EHC_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the Engineering Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_Pos _U_(16)                                              /**< (SFR_BU_OTPC_CONF_R0) Invalidation of Engineering Security Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_Msk (_U_(0x1) << SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Invalidation of Engineering Security Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE(value) (SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_Pos))
#define   SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the Engineering Security Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the Engineering Security Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_ENABLE (SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the Engineering Security Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_DISABLE (SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_ESC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the Engineering Security Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_ESC_LOCK_Pos      _U_(17)                                              /**< (SFR_BU_OTPC_CONF_R0) Lock of Engineering Security Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_ESC_LOCK_Msk      (_U_(0x1) << SFR_BU_OTPC_CONF_R0_ESC_LOCK_Pos)       /**< (SFR_BU_OTPC_CONF_R0) Lock of Engineering Security Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_ESC_LOCK(value)   (SFR_BU_OTPC_CONF_R0_ESC_LOCK_Msk & ((value) << SFR_BU_OTPC_CONF_R0_ESC_LOCK_Pos))
#define   SFR_BU_OTPC_CONF_R0_ESC_LOCK_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the Engineering Security Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_ESC_LOCK_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the Engineering Security Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_ESC_LOCK_ENABLE   (SFR_BU_OTPC_CONF_R0_ESC_LOCK_ENABLE_Val << SFR_BU_OTPC_CONF_R0_ESC_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the Engineering Security Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_ESC_LOCK_DISABLE  (SFR_BU_OTPC_CONF_R0_ESC_LOCK_DISABLE_Val << SFR_BU_OTPC_CONF_R0_ESC_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the Engineering Security Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_ESC_PARSE_Pos     _U_(18)                                              /**< (SFR_BU_OTPC_CONF_R0) Parsing of Engineering Security Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_ESC_PARSE_Msk     (_U_(0x1) << SFR_BU_OTPC_CONF_R0_ESC_PARSE_Pos)      /**< (SFR_BU_OTPC_CONF_R0) Parsing of Engineering Security Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_ESC_PARSE(value)  (SFR_BU_OTPC_CONF_R0_ESC_PARSE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_ESC_PARSE_Pos))
#define   SFR_BU_OTPC_CONF_R0_ESC_PARSE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the Engineering Security Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_ESC_PARSE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the Engineering Security Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_ESC_PARSE_ENABLE  (SFR_BU_OTPC_CONF_R0_ESC_PARSE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_ESC_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the Engineering Security Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_ESC_PARSE_DISABLE (SFR_BU_OTPC_CONF_R0_ESC_PARSE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_ESC_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the Engineering Security Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_Pos   _U_(19)                                              /**< (SFR_BU_OTPC_CONF_R0) Programming of Engineering Security Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_Msk   (_U_(0x1) << SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_Pos)    /**< (SFR_BU_OTPC_CONF_R0) Programming of Engineering Security Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_ESC_PROGRAM(value) (SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the Engineering Security Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the Engineering Security Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the Engineering Security Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R0_ESC_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the Engineering Security Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_Pos _U_(20)                                              /**< (SFR_BU_OTPC_CONF_R0) Invalidation of User Hardware Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_Msk (_U_(0x1) << SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Invalidation of User Hardware Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE(value) (SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_Pos))
#define   SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the User Hardware Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the User Hardware Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_ENABLE (SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the User Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_DISABLE (SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_UHC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the User Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_UHC_LOCK_Pos      _U_(21)                                              /**< (SFR_BU_OTPC_CONF_R0) Lock of User Hardware Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_UHC_LOCK_Msk      (_U_(0x1) << SFR_BU_OTPC_CONF_R0_UHC_LOCK_Pos)       /**< (SFR_BU_OTPC_CONF_R0) Lock of User Hardware Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_UHC_LOCK(value)   (SFR_BU_OTPC_CONF_R0_UHC_LOCK_Msk & ((value) << SFR_BU_OTPC_CONF_R0_UHC_LOCK_Pos))
#define   SFR_BU_OTPC_CONF_R0_UHC_LOCK_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the User Hardware Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_UHC_LOCK_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the User Hardware Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_UHC_LOCK_ENABLE   (SFR_BU_OTPC_CONF_R0_UHC_LOCK_ENABLE_Val << SFR_BU_OTPC_CONF_R0_UHC_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the User Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_UHC_LOCK_DISABLE  (SFR_BU_OTPC_CONF_R0_UHC_LOCK_DISABLE_Val << SFR_BU_OTPC_CONF_R0_UHC_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the User Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_UHC_PARSE_Pos     _U_(22)                                              /**< (SFR_BU_OTPC_CONF_R0) Parsing of User Hardware Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_UHC_PARSE_Msk     (_U_(0x1) << SFR_BU_OTPC_CONF_R0_UHC_PARSE_Pos)      /**< (SFR_BU_OTPC_CONF_R0) Parsing of User Hardware Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_UHC_PARSE(value)  (SFR_BU_OTPC_CONF_R0_UHC_PARSE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_UHC_PARSE_Pos))
#define   SFR_BU_OTPC_CONF_R0_UHC_PARSE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the User Hardware Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_UHC_PARSE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the User Hardware Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_UHC_PARSE_ENABLE  (SFR_BU_OTPC_CONF_R0_UHC_PARSE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_UHC_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the User Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_UHC_PARSE_DISABLE (SFR_BU_OTPC_CONF_R0_UHC_PARSE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_UHC_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the User Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_Pos   _U_(23)                                              /**< (SFR_BU_OTPC_CONF_R0) Programming of User Hardware Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_Msk   (_U_(0x1) << SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_Pos)    /**< (SFR_BU_OTPC_CONF_R0) Programming of User Hardware Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_UHC_PROGRAM(value) (SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the User Hardware Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the User Hardware Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the User Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R0_UHC_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the User Hardware Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_Pos _U_(24)                                              /**< (SFR_BU_OTPC_CONF_R0) Invalidation of User Boot Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_Msk (_U_(0x1) << SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_Pos)  /**< (SFR_BU_OTPC_CONF_R0) Invalidation of User Boot Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_BC_INVALIDATE(value) (SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_Pos))
#define   SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the User Boot Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the User Boot Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_ENABLE (SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the User Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_DISABLE (SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_BC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the User Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_BC_LOCK_Pos       _U_(25)                                              /**< (SFR_BU_OTPC_CONF_R0) Lock of User Boot Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_BC_LOCK_Msk       (_U_(0x1) << SFR_BU_OTPC_CONF_R0_BC_LOCK_Pos)        /**< (SFR_BU_OTPC_CONF_R0) Lock of User Boot Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_BC_LOCK(value)    (SFR_BU_OTPC_CONF_R0_BC_LOCK_Msk & ((value) << SFR_BU_OTPC_CONF_R0_BC_LOCK_Pos))
#define   SFR_BU_OTPC_CONF_R0_BC_LOCK_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the User Boot Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_BC_LOCK_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the User Boot Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_BC_LOCK_ENABLE    (SFR_BU_OTPC_CONF_R0_BC_LOCK_ENABLE_Val << SFR_BU_OTPC_CONF_R0_BC_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the User Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_BC_LOCK_DISABLE   (SFR_BU_OTPC_CONF_R0_BC_LOCK_DISABLE_Val << SFR_BU_OTPC_CONF_R0_BC_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the User Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_BC_PARSE_Pos      _U_(26)                                              /**< (SFR_BU_OTPC_CONF_R0) Parsing of User Boot Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_BC_PARSE_Msk      (_U_(0x1) << SFR_BU_OTPC_CONF_R0_BC_PARSE_Pos)       /**< (SFR_BU_OTPC_CONF_R0) Parsing of User Boot Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_BC_PARSE(value)   (SFR_BU_OTPC_CONF_R0_BC_PARSE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_BC_PARSE_Pos))
#define   SFR_BU_OTPC_CONF_R0_BC_PARSE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the User Boot Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_BC_PARSE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the User Boot Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_BC_PARSE_ENABLE   (SFR_BU_OTPC_CONF_R0_BC_PARSE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_BC_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the User Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_BC_PARSE_DISABLE  (SFR_BU_OTPC_CONF_R0_BC_PARSE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_BC_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the User Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_BC_PROGRAM_Pos    _U_(27)                                              /**< (SFR_BU_OTPC_CONF_R0) Programming of User Boot Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_BC_PROGRAM_Msk    (_U_(0x1) << SFR_BU_OTPC_CONF_R0_BC_PROGRAM_Pos)     /**< (SFR_BU_OTPC_CONF_R0) Programming of User Boot Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_BC_PROGRAM(value) (SFR_BU_OTPC_CONF_R0_BC_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R0_BC_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R0_BC_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the User Boot Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_BC_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the User Boot Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_BC_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R0_BC_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R0_BC_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the User Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_BC_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R0_BC_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R0_BC_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the User Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_Pos _U_(28)                                              /**< (SFR_BU_OTPC_CONF_R0) Invalidation of User Secure Boot Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_Msk (_U_(0x1) << SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Invalidation of User Secure Boot Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE(value) (SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_Pos))
#define   SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the User Secure Boot Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the User Secure Boot Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_ENABLE (SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables invalidation of the User Secure Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_DISABLE (SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_SBD_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables invalidation of the User Secure Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_SBD_LOCK_Pos      _U_(29)                                              /**< (SFR_BU_OTPC_CONF_R0) Lock of User Secure Boot Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_SBD_LOCK_Msk      (_U_(0x1) << SFR_BU_OTPC_CONF_R0_SBD_LOCK_Pos)       /**< (SFR_BU_OTPC_CONF_R0) Lock of User Secure Boot Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_SBD_LOCK(value)   (SFR_BU_OTPC_CONF_R0_SBD_LOCK_Msk & ((value) << SFR_BU_OTPC_CONF_R0_SBD_LOCK_Pos))
#define   SFR_BU_OTPC_CONF_R0_SBD_LOCK_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the User Secure Boot Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_SBD_LOCK_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the User Secure Boot Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_SBD_LOCK_ENABLE   (SFR_BU_OTPC_CONF_R0_SBD_LOCK_ENABLE_Val << SFR_BU_OTPC_CONF_R0_SBD_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables lock of the User Secure Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_SBD_LOCK_DISABLE  (SFR_BU_OTPC_CONF_R0_SBD_LOCK_DISABLE_Val << SFR_BU_OTPC_CONF_R0_SBD_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables lock of the User Secure Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_SBD_PARSE_Pos     _U_(30)                                              /**< (SFR_BU_OTPC_CONF_R0) Parsing of User Secure Boot Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_SBD_PARSE_Msk     (_U_(0x1) << SFR_BU_OTPC_CONF_R0_SBD_PARSE_Pos)      /**< (SFR_BU_OTPC_CONF_R0) Parsing of User Secure Boot Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_SBD_PARSE(value)  (SFR_BU_OTPC_CONF_R0_SBD_PARSE_Msk & ((value) << SFR_BU_OTPC_CONF_R0_SBD_PARSE_Pos))
#define   SFR_BU_OTPC_CONF_R0_SBD_PARSE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the User Secure Boot Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_SBD_PARSE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the User Secure Boot Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_SBD_PARSE_ENABLE  (SFR_BU_OTPC_CONF_R0_SBD_PARSE_ENABLE_Val << SFR_BU_OTPC_CONF_R0_SBD_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables parsing of the User Secure Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_SBD_PARSE_DISABLE (SFR_BU_OTPC_CONF_R0_SBD_PARSE_DISABLE_Val << SFR_BU_OTPC_CONF_R0_SBD_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables parsing of the User Secure Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_Pos   _U_(31)                                              /**< (SFR_BU_OTPC_CONF_R0) Programming of User Secure Boot Configuration Special Packet Position */
#define SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_Msk   (_U_(0x1) << SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_Pos)    /**< (SFR_BU_OTPC_CONF_R0) Programming of User Secure Boot Configuration Special Packet Mask */
#define SFR_BU_OTPC_CONF_R0_SBD_PROGRAM(value) (SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the User Secure Boot Configuration special packet.  */
#define   SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the User Secure Boot Configuration special packet.  */
#define SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Enables programming of the User Secure Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R0_SBD_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R0) Disables programming of the User Secure Boot Configuration special packet. Position  */
#define SFR_BU_OTPC_CONF_R0_Msk               _U_(0xFFFFFFFF)                                      /**< (SFR_BU_OTPC_CONF_R0) Register Mask  */


/* -------- SFR_BU_OTPC_CONF_R1 : (SFR Offset: 0x1C) (R/W 32) OTPC Configuration 1 Register (BackUp) -------- */
#define SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_Pos _U_(0)                                               /**< (SFR_BU_OTPC_CONF_R1) Invalidation of User Custom Special Packet (Secure World) Position */
#define SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_Msk (_U_(0x1) << SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_Pos)  /**< (SFR_BU_OTPC_CONF_R1) Invalidation of User Custom Special Packet (Secure World) Mask */
#define SFR_BU_OTPC_CONF_R1_SC_INVALIDATE(value) (SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_Msk & ((value) << SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_Pos))
#define   SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R1) Enables invalidation of the User Custom special packet (for Secure World).  */
#define   SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R1) Disables invalidation of the User Custom special packet (for Secure World).  */
#define SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_ENABLE (SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_ENABLE_Val << SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R1) Enables invalidation of the User Custom special packet (for Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_DISABLE (SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_DISABLE_Val << SFR_BU_OTPC_CONF_R1_SC_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R1) Disables invalidation of the User Custom special packet (for Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_SC_LOCK_Pos       _U_(1)                                               /**< (SFR_BU_OTPC_CONF_R1) Lock of User Custom Special Packet (Secure World) Position */
#define SFR_BU_OTPC_CONF_R1_SC_LOCK_Msk       (_U_(0x1) << SFR_BU_OTPC_CONF_R1_SC_LOCK_Pos)        /**< (SFR_BU_OTPC_CONF_R1) Lock of User Custom Special Packet (Secure World) Mask */
#define SFR_BU_OTPC_CONF_R1_SC_LOCK(value)    (SFR_BU_OTPC_CONF_R1_SC_LOCK_Msk & ((value) << SFR_BU_OTPC_CONF_R1_SC_LOCK_Pos))
#define   SFR_BU_OTPC_CONF_R1_SC_LOCK_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R1) Enables lock of the User Custom special packet (for Secure World).  */
#define   SFR_BU_OTPC_CONF_R1_SC_LOCK_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R1) Disables lock of the User Custom special packet (for Secure World).  */
#define SFR_BU_OTPC_CONF_R1_SC_LOCK_ENABLE    (SFR_BU_OTPC_CONF_R1_SC_LOCK_ENABLE_Val << SFR_BU_OTPC_CONF_R1_SC_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R1) Enables lock of the User Custom special packet (for Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_SC_LOCK_DISABLE   (SFR_BU_OTPC_CONF_R1_SC_LOCK_DISABLE_Val << SFR_BU_OTPC_CONF_R1_SC_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R1) Disables lock of the User Custom special packet (for Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_SC_PARSE_Pos      _U_(2)                                               /**< (SFR_BU_OTPC_CONF_R1) Parsing of the User Custom Special Packet (Secure World) Position */
#define SFR_BU_OTPC_CONF_R1_SC_PARSE_Msk      (_U_(0x1) << SFR_BU_OTPC_CONF_R1_SC_PARSE_Pos)       /**< (SFR_BU_OTPC_CONF_R1) Parsing of the User Custom Special Packet (Secure World) Mask */
#define SFR_BU_OTPC_CONF_R1_SC_PARSE(value)   (SFR_BU_OTPC_CONF_R1_SC_PARSE_Msk & ((value) << SFR_BU_OTPC_CONF_R1_SC_PARSE_Pos))
#define   SFR_BU_OTPC_CONF_R1_SC_PARSE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R1) Enables parsing of the User Custom special packet (for Secure World).  */
#define   SFR_BU_OTPC_CONF_R1_SC_PARSE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R1) Disables parsing of the User Custom special packet (for Secure World).  */
#define SFR_BU_OTPC_CONF_R1_SC_PARSE_ENABLE   (SFR_BU_OTPC_CONF_R1_SC_PARSE_ENABLE_Val << SFR_BU_OTPC_CONF_R1_SC_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R1) Enables parsing of the User Custom special packet (for Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_SC_PARSE_DISABLE  (SFR_BU_OTPC_CONF_R1_SC_PARSE_DISABLE_Val << SFR_BU_OTPC_CONF_R1_SC_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R1) Disables parsing of the User Custom special packet (for Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_SC_PROGRAM_Pos    _U_(3)                                               /**< (SFR_BU_OTPC_CONF_R1) Programming of User Custom Special Packet (Secure World) Position */
#define SFR_BU_OTPC_CONF_R1_SC_PROGRAM_Msk    (_U_(0x1) << SFR_BU_OTPC_CONF_R1_SC_PROGRAM_Pos)     /**< (SFR_BU_OTPC_CONF_R1) Programming of User Custom Special Packet (Secure World) Mask */
#define SFR_BU_OTPC_CONF_R1_SC_PROGRAM(value) (SFR_BU_OTPC_CONF_R1_SC_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R1_SC_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R1_SC_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R1) Enables programming of the User Custom special packet (for Secure World).  */
#define   SFR_BU_OTPC_CONF_R1_SC_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R1) Disables programming of the User Custom special packet (for Secure World).  */
#define SFR_BU_OTPC_CONF_R1_SC_PROGRAM_ENABLE (SFR_BU_OTPC_CONF_R1_SC_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R1_SC_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R1) Enables programming of the User Custom special packet (for Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_SC_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R1_SC_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R1_SC_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R1) Disables programming of the User Custom special packet (for Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_C_INVALIDATE_Pos  _U_(4)                                               /**< (SFR_BU_OTPC_CONF_R1) Invalidation of User Custom Special Packet (Non-Secure World) Position */
#define SFR_BU_OTPC_CONF_R1_C_INVALIDATE_Msk  (_U_(0x1) << SFR_BU_OTPC_CONF_R1_C_INVALIDATE_Pos)   /**< (SFR_BU_OTPC_CONF_R1) Invalidation of User Custom Special Packet (Non-Secure World) Mask */
#define SFR_BU_OTPC_CONF_R1_C_INVALIDATE(value) (SFR_BU_OTPC_CONF_R1_C_INVALIDATE_Msk & ((value) << SFR_BU_OTPC_CONF_R1_C_INVALIDATE_Pos))
#define   SFR_BU_OTPC_CONF_R1_C_INVALIDATE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R1) Enables invalidation of the User Custom special packet (for Non-Secure World).  */
#define   SFR_BU_OTPC_CONF_R1_C_INVALIDATE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R1) Disables invalidation of the User Custom special packet (for Non-Secure World).  */
#define SFR_BU_OTPC_CONF_R1_C_INVALIDATE_ENABLE (SFR_BU_OTPC_CONF_R1_C_INVALIDATE_ENABLE_Val << SFR_BU_OTPC_CONF_R1_C_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R1) Enables invalidation of the User Custom special packet (for Non-Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_C_INVALIDATE_DISABLE (SFR_BU_OTPC_CONF_R1_C_INVALIDATE_DISABLE_Val << SFR_BU_OTPC_CONF_R1_C_INVALIDATE_Pos) /**< (SFR_BU_OTPC_CONF_R1) Disables invalidation of the User Custom special packet (for Non-Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_C_LOCK_Pos        _U_(5)                                               /**< (SFR_BU_OTPC_CONF_R1) Lock of User Custom Special Packet (Non-Secure World) Position */
#define SFR_BU_OTPC_CONF_R1_C_LOCK_Msk        (_U_(0x1) << SFR_BU_OTPC_CONF_R1_C_LOCK_Pos)         /**< (SFR_BU_OTPC_CONF_R1) Lock of User Custom Special Packet (Non-Secure World) Mask */
#define SFR_BU_OTPC_CONF_R1_C_LOCK(value)     (SFR_BU_OTPC_CONF_R1_C_LOCK_Msk & ((value) << SFR_BU_OTPC_CONF_R1_C_LOCK_Pos))
#define   SFR_BU_OTPC_CONF_R1_C_LOCK_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R1) Enables lock of the User Custom special packet (for Non-Secure World).  */
#define   SFR_BU_OTPC_CONF_R1_C_LOCK_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R1) Disables lock of the User Custom special packet (for Non-Secure World).  */
#define SFR_BU_OTPC_CONF_R1_C_LOCK_ENABLE     (SFR_BU_OTPC_CONF_R1_C_LOCK_ENABLE_Val << SFR_BU_OTPC_CONF_R1_C_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R1) Enables lock of the User Custom special packet (for Non-Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_C_LOCK_DISABLE    (SFR_BU_OTPC_CONF_R1_C_LOCK_DISABLE_Val << SFR_BU_OTPC_CONF_R1_C_LOCK_Pos) /**< (SFR_BU_OTPC_CONF_R1) Disables lock of the User Custom special packet (for Non-Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_C_PARSE_Pos       _U_(6)                                               /**< (SFR_BU_OTPC_CONF_R1) Parsing of User Custom Special Packet (Non-Secure World) Position */
#define SFR_BU_OTPC_CONF_R1_C_PARSE_Msk       (_U_(0x1) << SFR_BU_OTPC_CONF_R1_C_PARSE_Pos)        /**< (SFR_BU_OTPC_CONF_R1) Parsing of User Custom Special Packet (Non-Secure World) Mask */
#define SFR_BU_OTPC_CONF_R1_C_PARSE(value)    (SFR_BU_OTPC_CONF_R1_C_PARSE_Msk & ((value) << SFR_BU_OTPC_CONF_R1_C_PARSE_Pos))
#define   SFR_BU_OTPC_CONF_R1_C_PARSE_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R1) Enables parsing of the User Custom special packet (for Non-Secure World).  */
#define   SFR_BU_OTPC_CONF_R1_C_PARSE_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R1) Disables parsing of the User Custom special packet (for Non-Secure World).  */
#define SFR_BU_OTPC_CONF_R1_C_PARSE_ENABLE    (SFR_BU_OTPC_CONF_R1_C_PARSE_ENABLE_Val << SFR_BU_OTPC_CONF_R1_C_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R1) Enables parsing of the User Custom special packet (for Non-Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_C_PARSE_DISABLE   (SFR_BU_OTPC_CONF_R1_C_PARSE_DISABLE_Val << SFR_BU_OTPC_CONF_R1_C_PARSE_Pos) /**< (SFR_BU_OTPC_CONF_R1) Disables parsing of the User Custom special packet (for Non-Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_C_PROGRAM_Pos     _U_(7)                                               /**< (SFR_BU_OTPC_CONF_R1) Programming of User Custom Special Packet (Non-Secure World) Position */
#define SFR_BU_OTPC_CONF_R1_C_PROGRAM_Msk     (_U_(0x1) << SFR_BU_OTPC_CONF_R1_C_PROGRAM_Pos)      /**< (SFR_BU_OTPC_CONF_R1) Programming of User Custom Special Packet (Non-Secure World) Mask */
#define SFR_BU_OTPC_CONF_R1_C_PROGRAM(value)  (SFR_BU_OTPC_CONF_R1_C_PROGRAM_Msk & ((value) << SFR_BU_OTPC_CONF_R1_C_PROGRAM_Pos))
#define   SFR_BU_OTPC_CONF_R1_C_PROGRAM_ENABLE_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R1) Enables programming of the User Custom special packet (for Non-Secure World).  */
#define   SFR_BU_OTPC_CONF_R1_C_PROGRAM_DISABLE_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R1) Disables programming of the User Custom special packet (for Non-Secure World).  */
#define SFR_BU_OTPC_CONF_R1_C_PROGRAM_ENABLE  (SFR_BU_OTPC_CONF_R1_C_PROGRAM_ENABLE_Val << SFR_BU_OTPC_CONF_R1_C_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R1) Enables programming of the User Custom special packet (for Non-Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_C_PROGRAM_DISABLE (SFR_BU_OTPC_CONF_R1_C_PROGRAM_DISABLE_Val << SFR_BU_OTPC_CONF_R1_C_PROGRAM_Pos) /**< (SFR_BU_OTPC_CONF_R1) Disables programming of the User Custom special packet (for Non-Secure World). Position  */
#define SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_Pos  _U_(8)                                               /**< (SFR_BU_OTPC_CONF_R1) Engineering Area Refresh Position */
#define SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_Msk  (_U_(0x1) << SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_Pos)   /**< (SFR_BU_OTPC_CONF_R1) Engineering Area Refresh Mask */
#define SFR_BU_OTPC_CONF_R1_ENGI_REFRESH(value) (SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_Msk & ((value) << SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_Pos))
#define   SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_ALLOWED_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R1) Allows refresh of the Engineering Area.  */
#define   SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_FORBIDDEN_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R1) Forbids refresh of the Engineering Area.  */
#define SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_ALLOWED (SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_ALLOWED_Val << SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_Pos) /**< (SFR_BU_OTPC_CONF_R1) Allows refresh of the Engineering Area. Position  */
#define SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_FORBIDDEN (SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_FORBIDDEN_Val << SFR_BU_OTPC_CONF_R1_ENGI_REFRESH_Pos) /**< (SFR_BU_OTPC_CONF_R1) Forbids refresh of the Engineering Area. Position  */
#define SFR_BU_OTPC_CONF_R1_USER_REFRESH_Pos  _U_(9)                                               /**< (SFR_BU_OTPC_CONF_R1) User Area Refresh Position */
#define SFR_BU_OTPC_CONF_R1_USER_REFRESH_Msk  (_U_(0x1) << SFR_BU_OTPC_CONF_R1_USER_REFRESH_Pos)   /**< (SFR_BU_OTPC_CONF_R1) User Area Refresh Mask */
#define SFR_BU_OTPC_CONF_R1_USER_REFRESH(value) (SFR_BU_OTPC_CONF_R1_USER_REFRESH_Msk & ((value) << SFR_BU_OTPC_CONF_R1_USER_REFRESH_Pos))
#define   SFR_BU_OTPC_CONF_R1_USER_REFRESH_ALLOWED_Val _U_(0x0)                                             /**< (SFR_BU_OTPC_CONF_R1) Allows refresh of the User Area.  */
#define   SFR_BU_OTPC_CONF_R1_USER_REFRESH_FORBIDDEN_Val _U_(0x1)                                             /**< (SFR_BU_OTPC_CONF_R1) Forbids refresh of the User Area.  */
#define SFR_BU_OTPC_CONF_R1_USER_REFRESH_ALLOWED (SFR_BU_OTPC_CONF_R1_USER_REFRESH_ALLOWED_Val << SFR_BU_OTPC_CONF_R1_USER_REFRESH_Pos) /**< (SFR_BU_OTPC_CONF_R1) Allows refresh of the User Area. Position  */
#define SFR_BU_OTPC_CONF_R1_USER_REFRESH_FORBIDDEN (SFR_BU_OTPC_CONF_R1_USER_REFRESH_FORBIDDEN_Val << SFR_BU_OTPC_CONF_R1_USER_REFRESH_Pos) /**< (SFR_BU_OTPC_CONF_R1) Forbids refresh of the User Area. Position  */
#define SFR_BU_OTPC_CONF_R1_FROM_SFRBU_ONLY_Pos _U_(24)                                              /**< (SFR_BU_OTPC_CONF_R1) OTPC Configuration Signal Position */
#define SFR_BU_OTPC_CONF_R1_FROM_SFRBU_ONLY_Msk (_U_(0x1) << SFR_BU_OTPC_CONF_R1_FROM_SFRBU_ONLY_Pos) /**< (SFR_BU_OTPC_CONF_R1) OTPC Configuration Signal Mask */
#define SFR_BU_OTPC_CONF_R1_FROM_SFRBU_ONLY(value) (SFR_BU_OTPC_CONF_R1_FROM_SFRBU_ONLY_Msk & ((value) << SFR_BU_OTPC_CONF_R1_FROM_SFRBU_ONLY_Pos))
#define SFR_BU_OTPC_CONF_R1_Msk               _U_(0x010003FF)                                      /**< (SFR_BU_OTPC_CONF_R1) Register Mask  */


/* -------- SFR_BU_RC_XTAL_TRIM : (SFR Offset: 0x20) (R/W 32) RC and XTAL Oscillator Trimming Register (BackUp) -------- */
#define SFR_BU_RC_XTAL_TRIM_XTAL_TRIM_Pos     _U_(0)                                               /**< (SFR_BU_RC_XTAL_TRIM) 32.768 kHz Crystal Oscillator Trimming Value Position */
#define SFR_BU_RC_XTAL_TRIM_XTAL_TRIM_Msk     (_U_(0x3) << SFR_BU_RC_XTAL_TRIM_XTAL_TRIM_Pos)      /**< (SFR_BU_RC_XTAL_TRIM) 32.768 kHz Crystal Oscillator Trimming Value Mask */
#define SFR_BU_RC_XTAL_TRIM_XTAL_TRIM(value)  (SFR_BU_RC_XTAL_TRIM_XTAL_TRIM_Msk & ((value) << SFR_BU_RC_XTAL_TRIM_XTAL_TRIM_Pos))
#define SFR_BU_RC_XTAL_TRIM_XTAL_SEL_Pos      _U_(4)                                               /**< (SFR_BU_RC_XTAL_TRIM) 32.768 kHz Crystal Oscillator Trimming Select Position */
#define SFR_BU_RC_XTAL_TRIM_XTAL_SEL_Msk      (_U_(0x1) << SFR_BU_RC_XTAL_TRIM_XTAL_SEL_Pos)       /**< (SFR_BU_RC_XTAL_TRIM) 32.768 kHz Crystal Oscillator Trimming Select Mask */
#define SFR_BU_RC_XTAL_TRIM_XTAL_SEL(value)   (SFR_BU_RC_XTAL_TRIM_XTAL_SEL_Msk & ((value) << SFR_BU_RC_XTAL_TRIM_XTAL_SEL_Pos))
#define SFR_BU_RC_XTAL_TRIM_RC_TRIM_Pos       _U_(8)                                               /**< (SFR_BU_RC_XTAL_TRIM) 32 kHz RC Oscillator Trimming Value Position */
#define SFR_BU_RC_XTAL_TRIM_RC_TRIM_Msk       (_U_(0x7F) << SFR_BU_RC_XTAL_TRIM_RC_TRIM_Pos)       /**< (SFR_BU_RC_XTAL_TRIM) 32 kHz RC Oscillator Trimming Value Mask */
#define SFR_BU_RC_XTAL_TRIM_RC_TRIM(value)    (SFR_BU_RC_XTAL_TRIM_RC_TRIM_Msk & ((value) << SFR_BU_RC_XTAL_TRIM_RC_TRIM_Pos))
#define SFR_BU_RC_XTAL_TRIM_RC_SEL_Pos        _U_(15)                                              /**< (SFR_BU_RC_XTAL_TRIM) 32 kHz RC Oscillator Trimming Select Position */
#define SFR_BU_RC_XTAL_TRIM_RC_SEL_Msk        (_U_(0x1) << SFR_BU_RC_XTAL_TRIM_RC_SEL_Pos)         /**< (SFR_BU_RC_XTAL_TRIM) 32 kHz RC Oscillator Trimming Select Mask */
#define SFR_BU_RC_XTAL_TRIM_RC_SEL(value)     (SFR_BU_RC_XTAL_TRIM_RC_SEL_Msk & ((value) << SFR_BU_RC_XTAL_TRIM_RC_SEL_Pos))
#define SFR_BU_RC_XTAL_TRIM_Msk               _U_(0x0000FF13)                                      /**< (SFR_BU_RC_XTAL_TRIM) Register Mask  */


/* -------- SFR_UTMICKTRIM : (SFR Offset: 0x30) (R/W 32) UTMI Clock Trimming Register -------- */
#define SFR_UTMICKTRIM_VBG_Pos                _U_(16)                                              /**< (SFR_UTMICKTRIM) UTMI Band Gap Voltage Trimming Position */
#define SFR_UTMICKTRIM_VBG_Msk                (_U_(0x3) << SFR_UTMICKTRIM_VBG_Pos)                 /**< (SFR_UTMICKTRIM) UTMI Band Gap Voltage Trimming Mask */
#define SFR_UTMICKTRIM_VBG(value)             (SFR_UTMICKTRIM_VBG_Msk & ((value) << SFR_UTMICKTRIM_VBG_Pos))
#define SFR_UTMICKTRIM_Msk                    _U_(0x00030000)                                      /**< (SFR_UTMICKTRIM) Register Mask  */


/* -------- SFR_UTMIHSTRIM : (SFR Offset: 0x34) (R/W 32) UTMI High-Speed Trimming Register -------- */
#define SFR_UTMIHSTRIM_SQUELCH_Pos            _U_(0)                                               /**< (SFR_UTMIHSTRIM) UTMI HS Squelch Voltage Trimming Position */
#define SFR_UTMIHSTRIM_SQUELCH_Msk            (_U_(0x7) << SFR_UTMIHSTRIM_SQUELCH_Pos)             /**< (SFR_UTMIHSTRIM) UTMI HS Squelch Voltage Trimming Mask */
#define SFR_UTMIHSTRIM_SQUELCH(value)         (SFR_UTMIHSTRIM_SQUELCH_Msk & ((value) << SFR_UTMIHSTRIM_SQUELCH_Pos))
#define SFR_UTMIHSTRIM_DISC_Pos               _U_(4)                                               /**< (SFR_UTMIHSTRIM) UTMI Disconnect Voltage Trimming Position */
#define SFR_UTMIHSTRIM_DISC_Msk               (_U_(0x7) << SFR_UTMIHSTRIM_DISC_Pos)                /**< (SFR_UTMIHSTRIM) UTMI Disconnect Voltage Trimming Mask */
#define SFR_UTMIHSTRIM_DISC(value)            (SFR_UTMIHSTRIM_DISC_Msk & ((value) << SFR_UTMIHSTRIM_DISC_Pos))
#define SFR_UTMIHSTRIM_SLOPE0_Pos             _U_(8)                                               /**< (SFR_UTMIHSTRIM) UTMI HS PORTx Transceiver Slope Trimming Position */
#define SFR_UTMIHSTRIM_SLOPE0_Msk             (_U_(0x7) << SFR_UTMIHSTRIM_SLOPE0_Pos)              /**< (SFR_UTMIHSTRIM) UTMI HS PORTx Transceiver Slope Trimming Mask */
#define SFR_UTMIHSTRIM_SLOPE0(value)          (SFR_UTMIHSTRIM_SLOPE0_Msk & ((value) << SFR_UTMIHSTRIM_SLOPE0_Pos))
#define SFR_UTMIHSTRIM_SLOPE1_Pos             _U_(12)                                              /**< (SFR_UTMIHSTRIM) UTMI HS PORTx Transceiver Slope Trimming Position */
#define SFR_UTMIHSTRIM_SLOPE1_Msk             (_U_(0x7) << SFR_UTMIHSTRIM_SLOPE1_Pos)              /**< (SFR_UTMIHSTRIM) UTMI HS PORTx Transceiver Slope Trimming Mask */
#define SFR_UTMIHSTRIM_SLOPE1(value)          (SFR_UTMIHSTRIM_SLOPE1_Msk & ((value) << SFR_UTMIHSTRIM_SLOPE1_Pos))
#define SFR_UTMIHSTRIM_SLOPE2_Pos             _U_(16)                                              /**< (SFR_UTMIHSTRIM) UTMI HS PORTx Transceiver Slope Trimming Position */
#define SFR_UTMIHSTRIM_SLOPE2_Msk             (_U_(0x7) << SFR_UTMIHSTRIM_SLOPE2_Pos)              /**< (SFR_UTMIHSTRIM) UTMI HS PORTx Transceiver Slope Trimming Mask */
#define SFR_UTMIHSTRIM_SLOPE2(value)          (SFR_UTMIHSTRIM_SLOPE2_Msk & ((value) << SFR_UTMIHSTRIM_SLOPE2_Pos))
#define SFR_UTMIHSTRIM_Msk                    _U_(0x00077777)                                      /**< (SFR_UTMIHSTRIM) Register Mask  */


/* -------- SFR_UTMIFSTRIM : (SFR Offset: 0x38) (R/W 32) UTMI Full-Speed Trimming Register -------- */
#define SFR_UTMIFSTRIM_RISE_Pos               _U_(0)                                               /**< (SFR_UTMIFSTRIM) FS Transceiver Output Rising Slope Trimming Position */
#define SFR_UTMIFSTRIM_RISE_Msk               (_U_(0x7) << SFR_UTMIFSTRIM_RISE_Pos)                /**< (SFR_UTMIFSTRIM) FS Transceiver Output Rising Slope Trimming Mask */
#define SFR_UTMIFSTRIM_RISE(value)            (SFR_UTMIFSTRIM_RISE_Msk & ((value) << SFR_UTMIFSTRIM_RISE_Pos))
#define SFR_UTMIFSTRIM_FALL_Pos               _U_(4)                                               /**< (SFR_UTMIFSTRIM) FS Transceiver Output Falling Slope Trimming Position */
#define SFR_UTMIFSTRIM_FALL_Msk               (_U_(0x7) << SFR_UTMIFSTRIM_FALL_Pos)                /**< (SFR_UTMIFSTRIM) FS Transceiver Output Falling Slope Trimming Mask */
#define SFR_UTMIFSTRIM_FALL(value)            (SFR_UTMIFSTRIM_FALL_Msk & ((value) << SFR_UTMIFSTRIM_FALL_Pos))
#define SFR_UTMIFSTRIM_XCVR_Pos               _U_(8)                                               /**< (SFR_UTMIFSTRIM) FS Transceiver Crossover Voltage Trimming Position */
#define SFR_UTMIFSTRIM_XCVR_Msk               (_U_(0x3) << SFR_UTMIFSTRIM_XCVR_Pos)                /**< (SFR_UTMIFSTRIM) FS Transceiver Crossover Voltage Trimming Mask */
#define SFR_UTMIFSTRIM_XCVR(value)            (SFR_UTMIFSTRIM_XCVR_Msk & ((value) << SFR_UTMIFSTRIM_XCVR_Pos))
#define SFR_UTMIFSTRIM_ZN_Pos                 _U_(16)                                              /**< (SFR_UTMIFSTRIM) FS Transceiver NMOS Impedance Trimming Position */
#define SFR_UTMIFSTRIM_ZN_Msk                 (_U_(0x7) << SFR_UTMIFSTRIM_ZN_Pos)                  /**< (SFR_UTMIFSTRIM) FS Transceiver NMOS Impedance Trimming Mask */
#define SFR_UTMIFSTRIM_ZN(value)              (SFR_UTMIFSTRIM_ZN_Msk & ((value) << SFR_UTMIFSTRIM_ZN_Pos))
#define SFR_UTMIFSTRIM_ZP_Pos                 _U_(20)                                              /**< (SFR_UTMIFSTRIM) FS Transceiver PMOS Impedance Trimming Position */
#define SFR_UTMIFSTRIM_ZP_Msk                 (_U_(0x7) << SFR_UTMIFSTRIM_ZP_Pos)                  /**< (SFR_UTMIFSTRIM) FS Transceiver PMOS Impedance Trimming Mask */
#define SFR_UTMIFSTRIM_ZP(value)              (SFR_UTMIFSTRIM_ZP_Msk & ((value) << SFR_UTMIFSTRIM_ZP_Pos))
#define SFR_UTMIFSTRIM_ZN_CAL_Pos             _U_(24)                                              /**< (SFR_UTMIFSTRIM) FS Transceiver NMOS Impedance Calibration Position */
#define SFR_UTMIFSTRIM_ZN_CAL_Msk             (_U_(0x7) << SFR_UTMIFSTRIM_ZN_CAL_Pos)              /**< (SFR_UTMIFSTRIM) FS Transceiver NMOS Impedance Calibration Mask */
#define SFR_UTMIFSTRIM_ZN_CAL(value)          (SFR_UTMIFSTRIM_ZN_CAL_Msk & ((value) << SFR_UTMIFSTRIM_ZN_CAL_Pos))
#define SFR_UTMIFSTRIM_ZP_CAL_Pos             _U_(28)                                              /**< (SFR_UTMIFSTRIM) FS Transceiver PMOS Impedance Calibration Position */
#define SFR_UTMIFSTRIM_ZP_CAL_Msk             (_U_(0x7) << SFR_UTMIFSTRIM_ZP_CAL_Pos)              /**< (SFR_UTMIFSTRIM) FS Transceiver PMOS Impedance Calibration Mask */
#define SFR_UTMIFSTRIM_ZP_CAL(value)          (SFR_UTMIFSTRIM_ZP_CAL_Msk & ((value) << SFR_UTMIFSTRIM_ZP_CAL_Pos))
#define SFR_UTMIFSTRIM_Msk                    _U_(0x77770377)                                      /**< (SFR_UTMIFSTRIM) Register Mask  */


/* -------- SFR_UTMISWAP : (SFR Offset: 0x3C) (R/W 32) UTMI DP/DM Pin Swapping Register -------- */
#define SFR_UTMISWAP_PORT0_Pos                _U_(0)                                               /**< (SFR_UTMISWAP) PORT 0 DP/DM Pin Swapping Position */
#define SFR_UTMISWAP_PORT0_Msk                (_U_(0x1) << SFR_UTMISWAP_PORT0_Pos)                 /**< (SFR_UTMISWAP) PORT 0 DP/DM Pin Swapping Mask */
#define SFR_UTMISWAP_PORT0(value)             (SFR_UTMISWAP_PORT0_Msk & ((value) << SFR_UTMISWAP_PORT0_Pos))
#define   SFR_UTMISWAP_PORT0_NORMAL_Val       _U_(0x0)                                             /**< (SFR_UTMISWAP) DP/DM normal pinout.  */
#define   SFR_UTMISWAP_PORT0_SWAPPED_Val      _U_(0x1)                                             /**< (SFR_UTMISWAP) DP/DM swapped pinout.  */
#define SFR_UTMISWAP_PORT0_NORMAL             (SFR_UTMISWAP_PORT0_NORMAL_Val << SFR_UTMISWAP_PORT0_Pos) /**< (SFR_UTMISWAP) DP/DM normal pinout. Position  */
#define SFR_UTMISWAP_PORT0_SWAPPED            (SFR_UTMISWAP_PORT0_SWAPPED_Val << SFR_UTMISWAP_PORT0_Pos) /**< (SFR_UTMISWAP) DP/DM swapped pinout. Position  */
#define SFR_UTMISWAP_PORT1_Pos                _U_(1)                                               /**< (SFR_UTMISWAP) PORT 1 DP/DM Pin Swapping Position */
#define SFR_UTMISWAP_PORT1_Msk                (_U_(0x1) << SFR_UTMISWAP_PORT1_Pos)                 /**< (SFR_UTMISWAP) PORT 1 DP/DM Pin Swapping Mask */
#define SFR_UTMISWAP_PORT1(value)             (SFR_UTMISWAP_PORT1_Msk & ((value) << SFR_UTMISWAP_PORT1_Pos))
#define   SFR_UTMISWAP_PORT1_NORMAL_Val       _U_(0x0)                                             /**< (SFR_UTMISWAP) DP/DM normal pinout.  */
#define   SFR_UTMISWAP_PORT1_SWAPPED_Val      _U_(0x1)                                             /**< (SFR_UTMISWAP) DP/DM swapped pinout.  */
#define SFR_UTMISWAP_PORT1_NORMAL             (SFR_UTMISWAP_PORT1_NORMAL_Val << SFR_UTMISWAP_PORT1_Pos) /**< (SFR_UTMISWAP) DP/DM normal pinout. Position  */
#define SFR_UTMISWAP_PORT1_SWAPPED            (SFR_UTMISWAP_PORT1_SWAPPED_Val << SFR_UTMISWAP_PORT1_Pos) /**< (SFR_UTMISWAP) DP/DM swapped pinout. Position  */
#define SFR_UTMISWAP_PORT2_Pos                _U_(2)                                               /**< (SFR_UTMISWAP) PORT 2 DP/DM Pin Swapping Position */
#define SFR_UTMISWAP_PORT2_Msk                (_U_(0x1) << SFR_UTMISWAP_PORT2_Pos)                 /**< (SFR_UTMISWAP) PORT 2 DP/DM Pin Swapping Mask */
#define SFR_UTMISWAP_PORT2(value)             (SFR_UTMISWAP_PORT2_Msk & ((value) << SFR_UTMISWAP_PORT2_Pos))
#define   SFR_UTMISWAP_PORT2_NORMAL_Val       _U_(0x0)                                             /**< (SFR_UTMISWAP) DP/DM normal pinout.  */
#define   SFR_UTMISWAP_PORT2_SWAPPED_Val      _U_(0x1)                                             /**< (SFR_UTMISWAP) DP/DM swapped pinout.  */
#define SFR_UTMISWAP_PORT2_NORMAL             (SFR_UTMISWAP_PORT2_NORMAL_Val << SFR_UTMISWAP_PORT2_Pos) /**< (SFR_UTMISWAP) DP/DM normal pinout. Position  */
#define SFR_UTMISWAP_PORT2_SWAPPED            (SFR_UTMISWAP_PORT2_SWAPPED_Val << SFR_UTMISWAP_PORT2_Pos) /**< (SFR_UTMISWAP) DP/DM swapped pinout. Position  */
#define SFR_UTMISWAP_Msk                      _U_(0x00000007)                                      /**< (SFR_UTMISWAP) Register Mask  */

#define SFR_UTMISWAP_PORT_Pos                 _U_(0)                                               /**< (SFR_UTMISWAP Position) PORT 2 DP/DM Pin Swapping */
#define SFR_UTMISWAP_PORT_Msk                 (_U_(0x7) << SFR_UTMISWAP_PORT_Pos)                  /**< (SFR_UTMISWAP Mask) PORT */
#define SFR_UTMISWAP_PORT(value)              (SFR_UTMISWAP_PORT_Msk & ((value) << SFR_UTMISWAP_PORT_Pos)) 

/* -------- SFR_RM0 : (SFR Offset: 0x5C) (R/W 32) Read Margin0 Register -------- */
#define SFR_RM0_RM00_Pos                      _U_(0)                                               /**< (SFR_RM0) READ_MARGIN Value: i_bank0_msb_rf2p, i_bank0_lsb_rf2p, i_bank1_msb_rf2p, i_bank1_lsb_rf2p - 512 bytes (rf2p) - gfx2d_bank_rf2p_dc_32x32sw1 (GFX2D) Position */
#define SFR_RM0_RM00_Msk                      (_U_(0xF) << SFR_RM0_RM00_Pos)                       /**< (SFR_RM0) READ_MARGIN Value: i_bank0_msb_rf2p, i_bank0_lsb_rf2p, i_bank1_msb_rf2p, i_bank1_lsb_rf2p - 512 bytes (rf2p) - gfx2d_bank_rf2p_dc_32x32sw1 (GFX2D) Mask */
#define SFR_RM0_RM00(value)                   (SFR_RM0_RM00_Msk & ((value) << SFR_RM0_RM00_Pos))  
#define SFR_RM0_RM01_Pos                      _U_(4)                                               /**< (SFR_RM0) WRITE_MARGIN Value: i_bank0_msb_rf2p, i_bank0_lsb_rf2p, i_bank1_msb_rf2p, i_bank1_lsb_rf2p - 512 bytes (rf2p) - gfx2d_bank_rf2p_dc_32x32sw1 (GFX2D) Position */
#define SFR_RM0_RM01_Msk                      (_U_(0xF) << SFR_RM0_RM01_Pos)                       /**< (SFR_RM0) WRITE_MARGIN Value: i_bank0_msb_rf2p, i_bank0_lsb_rf2p, i_bank1_msb_rf2p, i_bank1_lsb_rf2p - 512 bytes (rf2p) - gfx2d_bank_rf2p_dc_32x32sw1 (GFX2D) Mask */
#define SFR_RM0_RM01(value)                   (SFR_RM0_RM01_Msk & ((value) << SFR_RM0_RM01_Pos))  
#define SFR_RM0_RM02_Pos                      _U_(8)                                               /**< (SFR_RM0) READ_MARGIN Value: i_clut_rf1p - 2 Kbytes (rf1p) - gfx2d_clut_rf_sc_512x32 (GFX2D) Position */
#define SFR_RM0_RM02_Msk                      (_U_(0xF) << SFR_RM0_RM02_Pos)                       /**< (SFR_RM0) READ_MARGIN Value: i_clut_rf1p - 2 Kbytes (rf1p) - gfx2d_clut_rf_sc_512x32 (GFX2D) Mask */
#define SFR_RM0_RM02(value)                   (SFR_RM0_RM02_Msk & ((value) << SFR_RM0_RM02_Pos))  
#define SFR_RM0_RM03_Pos                      _U_(12)                                              /**< (SFR_RM0) READ_MARGIN Value: i_queue_rf2p - 68 bytes (rf2p) - gfx2d_queue_rf2p_dc_8x68 (GFX2D) Position */
#define SFR_RM0_RM03_Msk                      (_U_(0xF) << SFR_RM0_RM03_Pos)                       /**< (SFR_RM0) READ_MARGIN Value: i_queue_rf2p - 68 bytes (rf2p) - gfx2d_queue_rf2p_dc_8x68 (GFX2D) Mask */
#define SFR_RM0_RM03(value)                   (SFR_RM0_RM03_Msk & ((value) << SFR_RM0_RM03_Pos))  
#define SFR_RM0_RM04_Pos                      _U_(16)                                              /**< (SFR_RM0) WRITE_MARGIN Value: i_queue_rf2p - 68 bytes (rf2p) - gfx2d_queue_rf2p_dc_8x68 (GFX2D) Position */
#define SFR_RM0_RM04_Msk                      (_U_(0xF) << SFR_RM0_RM04_Pos)                       /**< (SFR_RM0) WRITE_MARGIN Value: i_queue_rf2p - 68 bytes (rf2p) - gfx2d_queue_rf2p_dc_8x68 (GFX2D) Mask */
#define SFR_RM0_RM04(value)                   (SFR_RM0_RM04_Msk & ((value) << SFR_RM0_RM04_Pos))  
#define SFR_RM0_Msk                           _U_(0x000FFFFF)                                      /**< (SFR_RM0) Register Mask  */


/* -------- SFR_RM1 : (SFR Offset: 0x60) (R/W 32) Read Margin1 Register -------- */
#define SFR_RM1_RM10_Pos                      _U_(0)                                               /**< (SFR_RM1) READ_MARGIN Value: i_lcd_base_clut, i_lcd_heo_clut - 2 Kbytes (rf1p) - hlcdc_clut_rf_sc_256x32sw1 (HLCDC5) Position */
#define SFR_RM1_RM10_Msk                      (_U_(0xF) << SFR_RM1_RM10_Pos)                       /**< (SFR_RM1) READ_MARGIN Value: i_lcd_base_clut, i_lcd_heo_clut - 2 Kbytes (rf1p) - hlcdc_clut_rf_sc_256x32sw1 (HLCDC5) Mask */
#define SFR_RM1_RM10(value)                   (SFR_RM1_RM10_Msk & ((value) << SFR_RM1_RM10_Pos))  
#define SFR_RM1_RM11_Pos                      _U_(4)                                               /**< (SFR_RM1) READ_MARGIN Value: i_lcd_base_fifo, i_lcd_ovr1_rf2p, i_lcd_ovr2_rf2p, i_lcd_heo_fifo, i_lcd_heop1_fifo, i_lcd_heop2_fifo - 816 bytes (rf2p) - hlcdc_fifo_rf2p_dc_32x34 (HLCDC5) Position */
#define SFR_RM1_RM11_Msk                      (_U_(0xF) << SFR_RM1_RM11_Pos)                       /**< (SFR_RM1) READ_MARGIN Value: i_lcd_base_fifo, i_lcd_ovr1_rf2p, i_lcd_ovr2_rf2p, i_lcd_heo_fifo, i_lcd_heop1_fifo, i_lcd_heop2_fifo - 816 bytes (rf2p) - hlcdc_fifo_rf2p_dc_32x34 (HLCDC5) Mask */
#define SFR_RM1_RM11(value)                   (SFR_RM1_RM11_Msk & ((value) << SFR_RM1_RM11_Pos))  
#define SFR_RM1_RM12_Pos                      _U_(8)                                               /**< (SFR_RM1) WRITE_MARGIN Value: i_lcd_base_fifo, i_lcd_ovr1_rf2p, i_lcd_ovr2_rf2p, i_lcd_heo_fifo, i_lcd_heop1_fifo, i_lcd_heop2_fifo - 816 bytes (rf2p) - hlcdc_fifo_rf2p_dc_32x34 (HLCDC5) Position */
#define SFR_RM1_RM12_Msk                      (_U_(0xF) << SFR_RM1_RM12_Pos)                       /**< (SFR_RM1) WRITE_MARGIN Value: i_lcd_base_fifo, i_lcd_ovr1_rf2p, i_lcd_ovr2_rf2p, i_lcd_heo_fifo, i_lcd_heop1_fifo, i_lcd_heop2_fifo - 816 bytes (rf2p) - hlcdc_fifo_rf2p_dc_32x34 (HLCDC5) Mask */
#define SFR_RM1_RM12(value)                   (SFR_RM1_RM12_Msk & ((value) << SFR_RM1_RM12_Pos))  
#define SFR_RM1_RM13_Pos                      _U_(12)                                              /**< (SFR_RM1) READ_MARGIN Value: i_lcd_output_fifo - 1.5 Kbytes (rf2p) - hlcdc_fifo_rf2p_dc_512x24 (HLCDC5) Position */
#define SFR_RM1_RM13_Msk                      (_U_(0xF) << SFR_RM1_RM13_Pos)                       /**< (SFR_RM1) READ_MARGIN Value: i_lcd_output_fifo - 1.5 Kbytes (rf2p) - hlcdc_fifo_rf2p_dc_512x24 (HLCDC5) Mask */
#define SFR_RM1_RM13(value)                   (SFR_RM1_RM13_Msk & ((value) << SFR_RM1_RM13_Pos))  
#define SFR_RM1_RM14_Pos                      _U_(16)                                              /**< (SFR_RM1) WRITE_MARGIN Value: i_lcd_output_fifo - 1.5 Kbytes (rf2p) - hlcdc_fifo_rf2p_dc_512x24 (HLCDC5) Position */
#define SFR_RM1_RM14_Msk                      (_U_(0xF) << SFR_RM1_RM14_Pos)                       /**< (SFR_RM1) WRITE_MARGIN Value: i_lcd_output_fifo - 1.5 Kbytes (rf2p) - hlcdc_fifo_rf2p_dc_512x24 (HLCDC5) Mask */
#define SFR_RM1_RM14(value)                   (SFR_RM1_RM14_Msk & ((value) << SFR_RM1_RM14_Pos))  
#define SFR_RM1_RM15_Pos                      _U_(20)                                              /**< (SFR_RM1) READ_MARGIN Value: i_lcd_heo_scaler0, i_lcd_heo_scaler1, i_lcd_heo_scaler2 - 3 Kbytes (sram) hlcdc_heoscaler_sram_1024x24sw1 (HLCDC5) Position */
#define SFR_RM1_RM15_Msk                      (_U_(0xF) << SFR_RM1_RM15_Pos)                       /**< (SFR_RM1) READ_MARGIN Value: i_lcd_heo_scaler0, i_lcd_heo_scaler1, i_lcd_heo_scaler2 - 3 Kbytes (sram) hlcdc_heoscaler_sram_1024x24sw1 (HLCDC5) Mask */
#define SFR_RM1_RM15(value)                   (SFR_RM1_RM15_Msk & ((value) << SFR_RM1_RM15_Pos))  
#define SFR_RM1_RM16_Pos                      _U_(24)                                              /**< (SFR_RM1) READ_MARGIN Value: i_lcd_ovr1_sram, i_lcd_ovr2_sram - 2 Kbytes (sram) hlcdc_ovr_sram_256x32sw1 (HLCDC5) Position */
#define SFR_RM1_RM16_Msk                      (_U_(0xF) << SFR_RM1_RM16_Pos)                       /**< (SFR_RM1) READ_MARGIN Value: i_lcd_ovr1_sram, i_lcd_ovr2_sram - 2 Kbytes (sram) hlcdc_ovr_sram_256x32sw1 (HLCDC5) Mask */
#define SFR_RM1_RM16(value)                   (SFR_RM1_RM16_Msk & ((value) << SFR_RM1_RM16_Pos))  
#define SFR_RM1_RM17_Pos                      _U_(28)                                              /**< (SFR_RM1) READ_MARGIN Value: i_lcd_heo_cue0, i_lcd_heo_cue1 - 2 Kbytes (rf1p) - hlcdc_heocue_rf_sc_512x16sw1 (HLCDC5) Position */
#define SFR_RM1_RM17_Msk                      (_U_(0xF) << SFR_RM1_RM17_Pos)                       /**< (SFR_RM1) READ_MARGIN Value: i_lcd_heo_cue0, i_lcd_heo_cue1 - 2 Kbytes (rf1p) - hlcdc_heocue_rf_sc_512x16sw1 (HLCDC5) Mask */
#define SFR_RM1_RM17(value)                   (SFR_RM1_RM17_Msk & ((value) << SFR_RM1_RM17_Pos))  
#define SFR_RM1_Msk                           _U_(0xFFFFFFFF)                                      /**< (SFR_RM1) Register Mask  */


/* -------- SFR_RM2 : (SFR Offset: 0x64) (R/W 32) Read Margin2 Register -------- */
#define SFR_RM2_RM20_Pos                      _U_(0)                                               /**< (SFR_RM2) READ-WRITE_MARGIN Value Port A: SDMMC0.i_dpram, SDMMC1.i_dpram - 2 Kbytes (dpsram) sdmmc_dpram_256x32sw1 (SDMMC) Position */
#define SFR_RM2_RM20_Msk                      (_U_(0xF) << SFR_RM2_RM20_Pos)                       /**< (SFR_RM2) READ-WRITE_MARGIN Value Port A: SDMMC0.i_dpram, SDMMC1.i_dpram - 2 Kbytes (dpsram) sdmmc_dpram_256x32sw1 (SDMMC) Mask */
#define SFR_RM2_RM20(value)                   (SFR_RM2_RM20_Msk & ((value) << SFR_RM2_RM20_Pos))  
#define SFR_RM2_RM21_Pos                      _U_(4)                                               /**< (SFR_RM2) READ-WRITE_MARGIN Value Port B SDMMC0.i_dpram, SDMMC1.i_dpram - 2 Kbytes (dpsram) sdmmc_dpram_256x32sw1 (SDMMC) Position */
#define SFR_RM2_RM21_Msk                      (_U_(0xF) << SFR_RM2_RM21_Pos)                       /**< (SFR_RM2) READ-WRITE_MARGIN Value Port B SDMMC0.i_dpram, SDMMC1.i_dpram - 2 Kbytes (dpsram) sdmmc_dpram_256x32sw1 (SDMMC) Mask */
#define SFR_RM2_RM21(value)                   (SFR_RM2_RM21_Msk & ((value) << SFR_RM2_RM21_Pos))  
#define SFR_RM2_RM22_Pos                      _U_(8)                                               /**< (SFR_RM2) READ-WRITE_MARGIN Value Port A: i_husb2dev_dpram_4112x32 - 16.5 Kbytes (dpsram) husb2dev_dpram_4224x32sw1 (HUSB) Position */
#define SFR_RM2_RM22_Msk                      (_U_(0xF) << SFR_RM2_RM22_Pos)                       /**< (SFR_RM2) READ-WRITE_MARGIN Value Port A: i_husb2dev_dpram_4112x32 - 16.5 Kbytes (dpsram) husb2dev_dpram_4224x32sw1 (HUSB) Mask */
#define SFR_RM2_RM22(value)                   (SFR_RM2_RM22_Msk & ((value) << SFR_RM2_RM22_Pos))  
#define SFR_RM2_RM23_Pos                      _U_(12)                                              /**< (SFR_RM2) READ-WRITE_MARGIN Value Port B: i_husb2dev_dpram_4112x32 - 16.5 Kbytes (dpsram) husb2dev_dpram_4224x32sw1 (HUSB) Position */
#define SFR_RM2_RM23_Msk                      (_U_(0xF) << SFR_RM2_RM23_Pos)                       /**< (SFR_RM2) READ-WRITE_MARGIN Value Port B: i_husb2dev_dpram_4112x32 - 16.5 Kbytes (dpsram) husb2dev_dpram_4224x32sw1 (HUSB) Mask */
#define SFR_RM2_RM23(value)                   (SFR_RM2_RM23_Msk & ((value) << SFR_RM2_RM23_Pos))  
#define SFR_RM2_Msk                           _U_(0x0000FFFF)                                      /**< (SFR_RM2) Register Mask  */


/* -------- SFR_RM3 : (SFR Offset: 0x68) (R/W 32) Read Margin3 Register -------- */
#define SFR_RM3_RM30_Pos                      _U_(0)                                               /**< (SFR_RM3) READ-WRITE_MARGIN Value Port A: i_dpram_1056x32 - 4.125 Kbytes (dpsram) hxdma_dpram_1056x32sw1 (HXDMA) Position */
#define SFR_RM3_RM30_Msk                      (_U_(0xF) << SFR_RM3_RM30_Pos)                       /**< (SFR_RM3) READ-WRITE_MARGIN Value Port A: i_dpram_1056x32 - 4.125 Kbytes (dpsram) hxdma_dpram_1056x32sw1 (HXDMA) Mask */
#define SFR_RM3_RM30(value)                   (SFR_RM3_RM30_Msk & ((value) << SFR_RM3_RM30_Pos))  
#define SFR_RM3_RM31_Pos                      _U_(4)                                               /**< (SFR_RM3) READ-WRITE_MARGIN Value Port B: i_dpram_1056x32 - 4.125 Kbytes (dpsram) hxdma_dpram_1056x32sw1 (HXDMA) Position */
#define SFR_RM3_RM31_Msk                      (_U_(0xF) << SFR_RM3_RM31_Pos)                       /**< (SFR_RM3) READ-WRITE_MARGIN Value Port B: i_dpram_1056x32 - 4.125 Kbytes (dpsram) hxdma_dpram_1056x32sw1 (HXDMA) Mask */
#define SFR_RM3_RM31(value)                   (SFR_RM3_RM31_Msk & ((value) << SFR_RM3_RM31_Pos))  
#define SFR_RM3_RM32_Pos                      _U_(8)                                               /**< (SFR_RM3) READ-WRITE_MARGIN Value: i_daram - 4 Kbytes (rf1p) - uhp_rf_sc_512x64 (EHCI/OHCI) Position */
#define SFR_RM3_RM32_Msk                      (_U_(0xF) << SFR_RM3_RM32_Pos)                       /**< (SFR_RM3) READ-WRITE_MARGIN Value: i_daram - 4 Kbytes (rf1p) - uhp_rf_sc_512x64 (EHCI/OHCI) Mask */
#define SFR_RM3_RM32(value)                   (SFR_RM3_RM32_Msk & ((value) << SFR_RM3_RM32_Pos))  
#define SFR_RM3_RM33_Pos                      _U_(12)                                              /**< (SFR_RM3) READ-WRITE_MARGIN Value: i_descram- 320 bytes (rf1p) - uhp_rf_sc_80x32 (EHCI/OHCI) Position */
#define SFR_RM3_RM33_Msk                      (_U_(0xF) << SFR_RM3_RM33_Pos)                       /**< (SFR_RM3) READ-WRITE_MARGIN Value: i_descram- 320 bytes (rf1p) - uhp_rf_sc_80x32 (EHCI/OHCI) Mask */
#define SFR_RM3_RM33(value)                   (SFR_RM3_RM33_Msk & ((value) << SFR_RM3_RM33_Pos))  
#define SFR_RM3_Msk                           _U_(0x0000FFFF)                                      /**< (SFR_RM3) Register Mask  */


/* -------- SFR_RM4 : (SFR Offset: 0x6C) (R/W 32) Read Margin4 Register -------- */
#define SFR_RM4_RM40_Pos                      _U_(0)                                               /**< (SFR_RM4) READ-WRITE_MARGIN Value: i_ahb_sram - 64 Kbytes (sram) - system_sram_16384x32sw1 (SRAM0) Position */
#define SFR_RM4_RM40_Msk                      (_U_(0xF) << SFR_RM4_RM40_Pos)                       /**< (SFR_RM4) READ-WRITE_MARGIN Value: i_ahb_sram - 64 Kbytes (sram) - system_sram_16384x32sw1 (SRAM0) Mask */
#define SFR_RM4_RM40(value)                   (SFR_RM4_RM40_Msk & ((value) << SFR_RM4_RM40_Pos))  
#define SFR_RM4_RM41_Pos                      _U_(4)                                               /**< (SFR_RM4) READ-WRITE_MARGIN Value: i_ahb_sram_otpc - 4 Kbytes (sram) - otpc_sram_1024x32sw1 (SRAM1 (OTPC)) Position */
#define SFR_RM4_RM41_Msk                      (_U_(0xF) << SFR_RM4_RM41_Pos)                       /**< (SFR_RM4) READ-WRITE_MARGIN Value: i_ahb_sram_otpc - 4 Kbytes (sram) - otpc_sram_1024x32sw1 (SRAM1 (OTPC)) Mask */
#define SFR_RM4_RM41(value)                   (SFR_RM4_RM41_Msk & ((value) << SFR_RM4_RM41_Pos))  
#define SFR_RM4_RM42_Pos                      _U_(8)                                               /**< (SFR_RM4) READ_MARGIN Value: i_rom_16384x32_sys - 64 Kbytes - (rom) - rom_system_rom_16384x32 (ROM) Position */
#define SFR_RM4_RM42_Msk                      (_U_(0xF) << SFR_RM4_RM42_Pos)                       /**< (SFR_RM4) READ_MARGIN Value: i_rom_16384x32_sys - 64 Kbytes - (rom) - rom_system_rom_16384x32 (ROM) Mask */
#define SFR_RM4_RM42(value)                   (SFR_RM4_RM42_Msk & ((value) << SFR_RM4_RM42_Pos))  
#define SFR_RM4_RM43_Pos                      _U_(12)                                              /**< (SFR_RM4) READ_MARGIN Value: i_rom_24576x32_ecc - 96 Kbytes - (rom) - rom_system_rom_24576x32 (ROM) Position */
#define SFR_RM4_RM43_Msk                      (_U_(0xF) << SFR_RM4_RM43_Pos)                       /**< (SFR_RM4) READ_MARGIN Value: i_rom_24576x32_ecc - 96 Kbytes - (rom) - rom_system_rom_24576x32 (ROM) Mask */
#define SFR_RM4_RM43(value)                   (SFR_RM4_RM43_Msk & ((value) << SFR_RM4_RM43_Pos))  
#define SFR_RM4_RM44_Pos                      _U_(16)                                              /**< (SFR_RM4) READ-WRITE_MARGIN Value: i_otpc_rf_sc_264x32sw1 - 1 Kbyte (rf1p) - otpc_rf_sc_264x32sw1 (OTPC) Position */
#define SFR_RM4_RM44_Msk                      (_U_(0xF) << SFR_RM4_RM44_Pos)                       /**< (SFR_RM4) READ-WRITE_MARGIN Value: i_otpc_rf_sc_264x32sw1 - 1 Kbyte (rf1p) - otpc_rf_sc_264x32sw1 (OTPC) Mask */
#define SFR_RM4_RM44(value)                   (SFR_RM4_RM44_Msk & ((value) << SFR_RM4_RM44_Pos))  
#define SFR_RM4_Msk                           _U_(0x000FFFFF)                                      /**< (SFR_RM4) Register Mask  */


/* -------- SFR_RM5 : (SFR Offset: 0x70) (R/W 32) Read Margin5 Register -------- */
#define SFR_RM5_RM50_Pos                      _U_(0)                                               /**< (SFR_RM5) READ-WRITE_MARGIN Value: uICTagRam0, uICTagRam1, uICTagRam2, uICTagRam3 - 2.75 Kbytes (rf1p) - rf_256x22 (ARM926) Position */
#define SFR_RM5_RM50_Msk                      (_U_(0xF) << SFR_RM5_RM50_Pos)                       /**< (SFR_RM5) READ-WRITE_MARGIN Value: uICTagRam0, uICTagRam1, uICTagRam2, uICTagRam3 - 2.75 Kbytes (rf1p) - rf_256x22 (ARM926) Mask */
#define SFR_RM5_RM50(value)                   (SFR_RM5_RM50_Msk & ((value) << SFR_RM5_RM50_Pos))  
#define SFR_RM5_RM51_Pos                      _U_(4)                                               /**< (SFR_RM5) READ-WRITE_MARGIN Value: uICValidRam, uDCValidRam - 384 bytes (rf1p) - rf_64x24 (ARM926) Position */
#define SFR_RM5_RM51_Msk                      (_U_(0xF) << SFR_RM5_RM51_Pos)                       /**< (SFR_RM5) READ-WRITE_MARGIN Value: uICValidRam, uDCValidRam - 384 bytes (rf1p) - rf_64x24 (ARM926) Mask */
#define SFR_RM5_RM51(value)                   (SFR_RM5_RM51_Msk & ((value) << SFR_RM5_RM51_Pos))  
#define SFR_RM5_RM52_Pos                      _U_(8)                                               /**< (SFR_RM5) READ_MARGIN Value: uDCTagRam0, uDCTagRam1, uDCTagRam2, uDCTagRam3 - 5.5 Kbytes (rf1p) - rf_512x22 (ARM926) Position */
#define SFR_RM5_RM52_Msk                      (_U_(0xF) << SFR_RM5_RM52_Pos)                       /**< (SFR_RM5) READ_MARGIN Value: uDCTagRam0, uDCTagRam1, uDCTagRam2, uDCTagRam3 - 5.5 Kbytes (rf1p) - rf_512x22 (ARM926) Mask */
#define SFR_RM5_RM52(value)                   (SFR_RM5_RM52_Msk & ((value) << SFR_RM5_RM52_Pos))  
#define SFR_RM5_RM53_Pos                      _U_(12)                                              /**< (SFR_RM5) READ_MARGIN Value: uDCDirtyRam - 256 bytes (rf1p) - rf_256x8 (ARM926) Position */
#define SFR_RM5_RM53_Msk                      (_U_(0xF) << SFR_RM5_RM53_Pos)                       /**< (SFR_RM5) READ_MARGIN Value: uDCDirtyRam - 256 bytes (rf1p) - rf_256x8 (ARM926) Mask */
#define SFR_RM5_RM53(value)                   (SFR_RM5_RM53_Msk & ((value) << SFR_RM5_RM53_Pos))  
#define SFR_RM5_RM54_Pos                      _U_(16)                                              /**< (SFR_RM5) READ-WRITE_MARGIN Value: uMMU1, uMMU3 - 240 bytes (rf1p) - rf_32x30 (ARM926) Position */
#define SFR_RM5_RM54_Msk                      (_U_(0xF) << SFR_RM5_RM54_Pos)                       /**< (SFR_RM5) READ-WRITE_MARGIN Value: uMMU1, uMMU3 - 240 bytes (rf1p) - rf_32x30 (ARM926) Mask */
#define SFR_RM5_RM54(value)                   (SFR_RM5_RM54_Msk & ((value) << SFR_RM5_RM54_Pos))  
#define SFR_RM5_RM55_Pos                      _U_(20)                                              /**< (SFR_RM5) READ-WRITE_MARGIN Value: uMMU0, uMMU2 - 208 bytes (rf1p) - rf_32x26 (ARM926) Position */
#define SFR_RM5_RM55_Msk                      (_U_(0xF) << SFR_RM5_RM55_Pos)                       /**< (SFR_RM5) READ-WRITE_MARGIN Value: uMMU0, uMMU2 - 208 bytes (rf1p) - rf_32x26 (ARM926) Mask */
#define SFR_RM5_RM55(value)                   (SFR_RM5_RM55_Msk & ((value) << SFR_RM5_RM55_Pos))  
#define SFR_RM5_RM56_Pos                      _U_(24)                                              /**< (SFR_RM5) READ-WRITE_MARGIN Value: uICDataRam0, uICDataRam1, uICDataRam2, uICDataRam3,- 32 Kbytes (sram) - sram_2048x32 (ARM926). uDCDataRam0, uDCDataRam1, uDCDataRam2, uDCDataRam3 - 32 Kbytes (sram) - sram_2048x32sw1 (ARM926) Position */
#define SFR_RM5_RM56_Msk                      (_U_(0xF) << SFR_RM5_RM56_Pos)                       /**< (SFR_RM5) READ-WRITE_MARGIN Value: uICDataRam0, uICDataRam1, uICDataRam2, uICDataRam3,- 32 Kbytes (sram) - sram_2048x32 (ARM926). uDCDataRam0, uDCDataRam1, uDCDataRam2, uDCDataRam3 - 32 Kbytes (sram) - sram_2048x32sw1 (ARM926) Mask */
#define SFR_RM5_RM56(value)                   (SFR_RM5_RM56_Msk & ((value) << SFR_RM5_RM56_Pos))  
#define SFR_RM5_Msk                           _U_(0x0FFFFFFF)                                      /**< (SFR_RM5) Register Mask  */


/* -------- SFR_LS : (SFR Offset: 0x7C) (R/W 32) Light Sleep Register -------- */
#define SFR_LS_LS0_Pos                        _U_(0)                                               /**< (SFR_LS) Light Sleep Value (GFX2D) Position */
#define SFR_LS_LS0_Msk                        (_U_(0x1) << SFR_LS_LS0_Pos)                         /**< (SFR_LS) Light Sleep Value (GFX2D) Mask */
#define SFR_LS_LS0(value)                     (SFR_LS_LS0_Msk & ((value) << SFR_LS_LS0_Pos))      
#define SFR_LS_LS1_Pos                        _U_(1)                                               /**< (SFR_LS) Light Sleep Value (HLCDC5) Position */
#define SFR_LS_LS1_Msk                        (_U_(0x1) << SFR_LS_LS1_Pos)                         /**< (SFR_LS) Light Sleep Value (HLCDC5) Mask */
#define SFR_LS_LS1(value)                     (SFR_LS_LS1_Msk & ((value) << SFR_LS_LS1_Pos))      
#define SFR_LS_LS2_Pos                        _U_(2)                                               /**< (SFR_LS) Light Sleep Value (SDMMC) Position */
#define SFR_LS_LS2_Msk                        (_U_(0x1) << SFR_LS_LS2_Pos)                         /**< (SFR_LS) Light Sleep Value (SDMMC) Mask */
#define SFR_LS_LS2(value)                     (SFR_LS_LS2_Msk & ((value) << SFR_LS_LS2_Pos))      
#define SFR_LS_LS3_Pos                        _U_(3)                                               /**< (SFR_LS) Light Sleep Value (HUSB) Position */
#define SFR_LS_LS3_Msk                        (_U_(0x1) << SFR_LS_LS3_Pos)                         /**< (SFR_LS) Light Sleep Value (HUSB) Mask */
#define SFR_LS_LS3(value)                     (SFR_LS_LS3_Msk & ((value) << SFR_LS_LS3_Pos))      
#define SFR_LS_LS4_Pos                        _U_(4)                                               /**< (SFR_LS) Light Sleep Value (HXDMA) Position */
#define SFR_LS_LS4_Msk                        (_U_(0x1) << SFR_LS_LS4_Pos)                         /**< (SFR_LS) Light Sleep Value (HXDMA) Mask */
#define SFR_LS_LS4(value)                     (SFR_LS_LS4_Msk & ((value) << SFR_LS_LS4_Pos))      
#define SFR_LS_LS5_Pos                        _U_(5)                                               /**< (SFR_LS) Light Sleep Value (EHCI/OHCI) Position */
#define SFR_LS_LS5_Msk                        (_U_(0x1) << SFR_LS_LS5_Pos)                         /**< (SFR_LS) Light Sleep Value (EHCI/OHCI) Mask */
#define SFR_LS_LS5(value)                     (SFR_LS_LS5_Msk & ((value) << SFR_LS_LS5_Pos))      
#define SFR_LS_LS6_Pos                        _U_(6)                                               /**< (SFR_LS) Light Sleep Value (SRAM0) Position */
#define SFR_LS_LS6_Msk                        (_U_(0x1) << SFR_LS_LS6_Pos)                         /**< (SFR_LS) Light Sleep Value (SRAM0) Mask */
#define SFR_LS_LS6(value)                     (SFR_LS_LS6_Msk & ((value) << SFR_LS_LS6_Pos))      
#define SFR_LS_LS7_Pos                        _U_(7)                                               /**< (SFR_LS) Light Sleep Value (SRAM1 (OTPC)) (This bit is used by i_ahb_sram_otpc) Position */
#define SFR_LS_LS7_Msk                        (_U_(0x1) << SFR_LS_LS7_Pos)                         /**< (SFR_LS) Light Sleep Value (SRAM1 (OTPC)) (This bit is used by i_ahb_sram_otpc) Mask */
#define SFR_LS_LS7(value)                     (SFR_LS_LS7_Msk & ((value) << SFR_LS_LS7_Pos))      
#define SFR_LS_LS8_Pos                        _U_(8)                                               /**< (SFR_LS) Light Sleep Value (ROM + OTPC) (This bit is used by rom_16384x32_sys, rom_24576x32_ecc and otpc_rf_sc_264x32sw1) Position */
#define SFR_LS_LS8_Msk                        (_U_(0x1) << SFR_LS_LS8_Pos)                         /**< (SFR_LS) Light Sleep Value (ROM + OTPC) (This bit is used by rom_16384x32_sys, rom_24576x32_ecc and otpc_rf_sc_264x32sw1) Mask */
#define SFR_LS_LS8(value)                     (SFR_LS_LS8_Msk & ((value) << SFR_LS_LS8_Pos))      
#define SFR_LS_LS9_Pos                        _U_(9)                                               /**< (SFR_LS) Light Sleep Value (ARM926) Position */
#define SFR_LS_LS9_Msk                        (_U_(0x1) << SFR_LS_LS9_Pos)                         /**< (SFR_LS) Light Sleep Value (ARM926) Mask */
#define SFR_LS_LS9(value)                     (SFR_LS_LS9_Msk & ((value) << SFR_LS_LS9_Pos))      
#define SFR_LS_MEM_POWER_GATING_ULP1_EN_Pos   _U_(16)                                              /**< (SFR_LS) Light Sleep Value for ULP1 Power-Gated Memories Position */
#define SFR_LS_MEM_POWER_GATING_ULP1_EN_Msk   (_U_(0x1) << SFR_LS_MEM_POWER_GATING_ULP1_EN_Pos)    /**< (SFR_LS) Light Sleep Value for ULP1 Power-Gated Memories Mask */
#define SFR_LS_MEM_POWER_GATING_ULP1_EN(value) (SFR_LS_MEM_POWER_GATING_ULP1_EN_Msk & ((value) << SFR_LS_MEM_POWER_GATING_ULP1_EN_Pos))
#define SFR_LS_Msk                            _U_(0x000103FF)                                      /**< (SFR_LS) Register Mask  */

#define SFR_LS_LS_Pos                         _U_(0)                                               /**< (SFR_LS Position) Light Sleep Value (GFX2D) */
#define SFR_LS_LS_Msk                         (_U_(0x3FF) << SFR_LS_LS_Pos)                        /**< (SFR_LS Mask) LS */
#define SFR_LS_LS(value)                      (SFR_LS_LS_Msk & ((value) << SFR_LS_LS_Pos))         

/* -------- SFR_CAL0 : (SFR Offset: 0xB0) (R/W 32) I/O Calibration 0 Register -------- */
#define SFR_CAL0_CALN_P0_Pos                  _U_(0)                                               /**< (SFR_CAL0) Calibration of Low Level Output Impedance of Pads with VDDIOP0 Supply Position */
#define SFR_CAL0_CALN_P0_Msk                  (_U_(0xF) << SFR_CAL0_CALN_P0_Pos)                   /**< (SFR_CAL0) Calibration of Low Level Output Impedance of Pads with VDDIOP0 Supply Mask */
#define SFR_CAL0_CALN_P0(value)               (SFR_CAL0_CALN_P0_Msk & ((value) << SFR_CAL0_CALN_P0_Pos))
#define SFR_CAL0_CALP_P0_Pos                  _U_(4)                                               /**< (SFR_CAL0) Calibration of High Level Output Impedance of Pads with VDDIOP0 Supply Position */
#define SFR_CAL0_CALP_P0_Msk                  (_U_(0xF) << SFR_CAL0_CALP_P0_Pos)                   /**< (SFR_CAL0) Calibration of High Level Output Impedance of Pads with VDDIOP0 Supply Mask */
#define SFR_CAL0_CALP_P0(value)               (SFR_CAL0_CALP_P0_Msk & ((value) << SFR_CAL0_CALP_P0_Pos))
#define SFR_CAL0_CALN_P1_Pos                  _U_(8)                                               /**< (SFR_CAL0) Calibration of Low Level Output Impedance of Pads with VDDIOP1 Supply Position */
#define SFR_CAL0_CALN_P1_Msk                  (_U_(0xF) << SFR_CAL0_CALN_P1_Pos)                   /**< (SFR_CAL0) Calibration of Low Level Output Impedance of Pads with VDDIOP1 Supply Mask */
#define SFR_CAL0_CALN_P1(value)               (SFR_CAL0_CALN_P1_Msk & ((value) << SFR_CAL0_CALN_P1_Pos))
#define SFR_CAL0_CALP_P1_Pos                  _U_(12)                                              /**< (SFR_CAL0) Calibration of High Level Output Impedance of Pads with VDDIOP1 Supply Position */
#define SFR_CAL0_CALP_P1_Msk                  (_U_(0xF) << SFR_CAL0_CALP_P1_Pos)                   /**< (SFR_CAL0) Calibration of High Level Output Impedance of Pads with VDDIOP1 Supply Mask */
#define SFR_CAL0_CALP_P1(value)               (SFR_CAL0_CALP_P1_Msk & ((value) << SFR_CAL0_CALP_P1_Pos))
#define SFR_CAL0_CALN_ANA_Pos                 _U_(16)                                              /**< (SFR_CAL0) Calibration of Low Level Output Impedance of Pads with VDDANA Supply Position */
#define SFR_CAL0_CALN_ANA_Msk                 (_U_(0xF) << SFR_CAL0_CALN_ANA_Pos)                  /**< (SFR_CAL0) Calibration of Low Level Output Impedance of Pads with VDDANA Supply Mask */
#define SFR_CAL0_CALN_ANA(value)              (SFR_CAL0_CALN_ANA_Msk & ((value) << SFR_CAL0_CALN_ANA_Pos))
#define SFR_CAL0_CALP_ANA_Pos                 _U_(20)                                              /**< (SFR_CAL0) Calibration of High Level Output Impedance of Pads with VDDANA Supply Position */
#define SFR_CAL0_CALP_ANA_Msk                 (_U_(0xF) << SFR_CAL0_CALP_ANA_Pos)                  /**< (SFR_CAL0) Calibration of High Level Output Impedance of Pads with VDDANA Supply Mask */
#define SFR_CAL0_CALP_ANA(value)              (SFR_CAL0_CALP_ANA_Msk & ((value) << SFR_CAL0_CALP_ANA_Pos))
#define SFR_CAL0_CALN_QSPI_Pos                _U_(24)                                              /**< (SFR_CAL0) Calibration of Low Level Output Impedance of Pads with VDDQSPI Supply Position */
#define SFR_CAL0_CALN_QSPI_Msk                (_U_(0xF) << SFR_CAL0_CALN_QSPI_Pos)                 /**< (SFR_CAL0) Calibration of Low Level Output Impedance of Pads with VDDQSPI Supply Mask */
#define SFR_CAL0_CALN_QSPI(value)             (SFR_CAL0_CALN_QSPI_Msk & ((value) << SFR_CAL0_CALN_QSPI_Pos))
#define SFR_CAL0_CALP_QSPI_Pos                _U_(28)                                              /**< (SFR_CAL0) Calibration of High Level Output Impedance of Pads with VDDQSPI Supply Position */
#define SFR_CAL0_CALP_QSPI_Msk                (_U_(0xF) << SFR_CAL0_CALP_QSPI_Pos)                 /**< (SFR_CAL0) Calibration of High Level Output Impedance of Pads with VDDQSPI Supply Mask */
#define SFR_CAL0_CALP_QSPI(value)             (SFR_CAL0_CALP_QSPI_Msk & ((value) << SFR_CAL0_CALP_QSPI_Pos))
#define SFR_CAL0_Msk                          _U_(0xFFFFFFFF)                                      /**< (SFR_CAL0) Register Mask  */


/* -------- SFR_CAL1 : (SFR Offset: 0xB4) (R/W 32) I/O Calibration 1 Register -------- */
#define SFR_CAL1_CALN_M_Pos                   _U_(0)                                               /**< (SFR_CAL1) Calibration of Low Level Output Impedance of Pads with VDDIOM Supply Position */
#define SFR_CAL1_CALN_M_Msk                   (_U_(0xF) << SFR_CAL1_CALN_M_Pos)                    /**< (SFR_CAL1) Calibration of Low Level Output Impedance of Pads with VDDIOM Supply Mask */
#define SFR_CAL1_CALN_M(value)                (SFR_CAL1_CALN_M_Msk & ((value) << SFR_CAL1_CALN_M_Pos))
#define SFR_CAL1_CALP_M_Pos                   _U_(4)                                               /**< (SFR_CAL1) Calibration of High Level Output Impedance of Pads with VDDIOM Supply Position */
#define SFR_CAL1_CALP_M_Msk                   (_U_(0xF) << SFR_CAL1_CALP_M_Pos)                    /**< (SFR_CAL1) Calibration of High Level Output Impedance of Pads with VDDIOM Supply Mask */
#define SFR_CAL1_CALP_M(value)                (SFR_CAL1_CALP_M_Msk & ((value) << SFR_CAL1_CALP_M_Pos))
#define SFR_CAL1_TEST_M_Pos                   _U_(8)                                               /**< (SFR_CAL1) Enable Calibration of Low/High Level Output Impedance of Pads with VDDIOM Supply Position */
#define SFR_CAL1_TEST_M_Msk                   (_U_(0x1) << SFR_CAL1_TEST_M_Pos)                    /**< (SFR_CAL1) Enable Calibration of Low/High Level Output Impedance of Pads with VDDIOM Supply Mask */
#define SFR_CAL1_TEST_M(value)                (SFR_CAL1_TEST_M_Msk & ((value) << SFR_CAL1_TEST_M_Pos))
#define SFR_CAL1_Msk                          _U_(0x000001FF)                                      /**< (SFR_CAL1) Register Mask  */


/* -------- SFR_WPMR : (SFR Offset: 0xE4) (R/W 32) Write Protection Mode Register -------- */
#define SFR_WPMR_WPEN_Pos                     _U_(0)                                               /**< (SFR_WPMR) Write Protection Enable Position */
#define SFR_WPMR_WPEN_Msk                     (_U_(0x1) << SFR_WPMR_WPEN_Pos)                      /**< (SFR_WPMR) Write Protection Enable Mask */
#define SFR_WPMR_WPEN(value)                  (SFR_WPMR_WPEN_Msk & ((value) << SFR_WPMR_WPEN_Pos))
#define SFR_WPMR_WPKEY_Pos                    _U_(8)                                               /**< (SFR_WPMR) Write Protection Key Position */
#define SFR_WPMR_WPKEY_Msk                    (_U_(0xFFFFFF) << SFR_WPMR_WPKEY_Pos)                /**< (SFR_WPMR) Write Protection Key Mask */
#define SFR_WPMR_WPKEY(value)                 (SFR_WPMR_WPKEY_Msk & ((value) << SFR_WPMR_WPKEY_Pos))
#define   SFR_WPMR_WPKEY_PASSWD_Val           _U_(0x534652)                                        /**< (SFR_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0.  */
#define SFR_WPMR_WPKEY_PASSWD                 (SFR_WPMR_WPKEY_PASSWD_Val << SFR_WPMR_WPKEY_Pos)    /**< (SFR_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0. Position  */
#define SFR_WPMR_Msk                          _U_(0xFFFFFF01)                                      /**< (SFR_WPMR) Register Mask  */


/* -------- SFR_SPARE : (SFR Offset: 0x100) (R/W 32) Spare Register -------- */
#define SFR_SPARE_VALUE_Pos                   _U_(0)                                               /**< (SFR_SPARE) Spare Position */
#define SFR_SPARE_VALUE_Msk                   (_U_(0xFFFFFFFF) << SFR_SPARE_VALUE_Pos)             /**< (SFR_SPARE) Spare Mask */
#define SFR_SPARE_VALUE(value)                (SFR_SPARE_VALUE_Msk & ((value) << SFR_SPARE_VALUE_Pos))
#define SFR_SPARE_Msk                         _U_(0xFFFFFFFF)                                      /**< (SFR_SPARE) Register Mask  */


/* -------- SFR_BU_SPARE : (SFR Offset: 0x104) (R/W 32) Spare Register (BackUp) -------- */
#define SFR_BU_SPARE_VALUE_Pos                _U_(0)                                               /**< (SFR_BU_SPARE) Spare Position */
#define SFR_BU_SPARE_VALUE_Msk                (_U_(0xFFFF) << SFR_BU_SPARE_VALUE_Pos)              /**< (SFR_BU_SPARE) Spare Mask */
#define SFR_BU_SPARE_VALUE(value)             (SFR_BU_SPARE_VALUE_Msk & ((value) << SFR_BU_SPARE_VALUE_Pos))
#define SFR_BU_SPARE_Msk                      _U_(0x0000FFFF)                                      /**< (SFR_BU_SPARE) Register Mask  */


/** \brief SFR register offsets definitions */
#define SFR_CCFG_EBICSA_REG_OFST       (0x04)              /**< (SFR_CCFG_EBICSA) EBI Chip Select Register Offset */
#define SFR_OHCIICR_REG_OFST           (0x10)              /**< (SFR_OHCIICR) OHCI Interrupt Configuration Register Offset */
#define SFR_OHCIISR_REG_OFST           (0x14)              /**< (SFR_OHCIISR) OHCI Interrupt Status Register Offset */
#define SFR_BU_OTPC_CONF_R0_REG_OFST   (0x18)              /**< (SFR_BU_OTPC_CONF_R0) OTPC Configuration 0 Register (BackUp) Offset */
#define SFR_BU_OTPC_CONF_R1_REG_OFST   (0x1C)              /**< (SFR_BU_OTPC_CONF_R1) OTPC Configuration 1 Register (BackUp) Offset */
#define SFR_BU_RC_XTAL_TRIM_REG_OFST   (0x20)              /**< (SFR_BU_RC_XTAL_TRIM) RC and XTAL Oscillator Trimming Register (BackUp) Offset */
#define SFR_UTMICKTRIM_REG_OFST        (0x30)              /**< (SFR_UTMICKTRIM) UTMI Clock Trimming Register Offset */
#define SFR_UTMIHSTRIM_REG_OFST        (0x34)              /**< (SFR_UTMIHSTRIM) UTMI High-Speed Trimming Register Offset */
#define SFR_UTMIFSTRIM_REG_OFST        (0x38)              /**< (SFR_UTMIFSTRIM) UTMI Full-Speed Trimming Register Offset */
#define SFR_UTMISWAP_REG_OFST          (0x3C)              /**< (SFR_UTMISWAP) UTMI DP/DM Pin Swapping Register Offset */
#define SFR_RM0_REG_OFST               (0x5C)              /**< (SFR_RM0) Read Margin0 Register Offset */
#define SFR_RM1_REG_OFST               (0x60)              /**< (SFR_RM1) Read Margin1 Register Offset */
#define SFR_RM2_REG_OFST               (0x64)              /**< (SFR_RM2) Read Margin2 Register Offset */
#define SFR_RM3_REG_OFST               (0x68)              /**< (SFR_RM3) Read Margin3 Register Offset */
#define SFR_RM4_REG_OFST               (0x6C)              /**< (SFR_RM4) Read Margin4 Register Offset */
#define SFR_RM5_REG_OFST               (0x70)              /**< (SFR_RM5) Read Margin5 Register Offset */
#define SFR_LS_REG_OFST                (0x7C)              /**< (SFR_LS) Light Sleep Register Offset */
#define SFR_CAL0_REG_OFST              (0xB0)              /**< (SFR_CAL0) I/O Calibration 0 Register Offset */
#define SFR_CAL1_REG_OFST              (0xB4)              /**< (SFR_CAL1) I/O Calibration 1 Register Offset */
#define SFR_WPMR_REG_OFST              (0xE4)              /**< (SFR_WPMR) Write Protection Mode Register Offset */
#define SFR_SPARE_REG_OFST             (0x100)             /**< (SFR_SPARE) Spare Register Offset */
#define SFR_BU_SPARE_REG_OFST          (0x104)             /**< (SFR_BU_SPARE) Spare Register (BackUp) Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief SFR register API structure */
typedef struct
{
  __I   uint8_t                        Reserved1[0x04];
  __IO  uint32_t                       SFR_CCFG_EBICSA;    /**< Offset: 0x04 (R/W  32) EBI Chip Select Register */
  __I   uint8_t                        Reserved2[0x08];
  __IO  uint32_t                       SFR_OHCIICR;        /**< Offset: 0x10 (R/W  32) OHCI Interrupt Configuration Register */
  __I   uint32_t                       SFR_OHCIISR;        /**< Offset: 0x14 (R/   32) OHCI Interrupt Status Register */
  __IO  uint32_t                       SFR_BU_OTPC_CONF_R0; /**< Offset: 0x18 (R/W  32) OTPC Configuration 0 Register (BackUp) */
  __IO  uint32_t                       SFR_BU_OTPC_CONF_R1; /**< Offset: 0x1C (R/W  32) OTPC Configuration 1 Register (BackUp) */
  __IO  uint32_t                       SFR_BU_RC_XTAL_TRIM; /**< Offset: 0x20 (R/W  32) RC and XTAL Oscillator Trimming Register (BackUp) */
  __I   uint8_t                        Reserved3[0x0C];
  __IO  uint32_t                       SFR_UTMICKTRIM;     /**< Offset: 0x30 (R/W  32) UTMI Clock Trimming Register */
  __IO  uint32_t                       SFR_UTMIHSTRIM;     /**< Offset: 0x34 (R/W  32) UTMI High-Speed Trimming Register */
  __IO  uint32_t                       SFR_UTMIFSTRIM;     /**< Offset: 0x38 (R/W  32) UTMI Full-Speed Trimming Register */
  __IO  uint32_t                       SFR_UTMISWAP;       /**< Offset: 0x3C (R/W  32) UTMI DP/DM Pin Swapping Register */
  __I   uint8_t                        Reserved4[0x1C];
  __IO  uint32_t                       SFR_RM0;            /**< Offset: 0x5C (R/W  32) Read Margin0 Register */
  __IO  uint32_t                       SFR_RM1;            /**< Offset: 0x60 (R/W  32) Read Margin1 Register */
  __IO  uint32_t                       SFR_RM2;            /**< Offset: 0x64 (R/W  32) Read Margin2 Register */
  __IO  uint32_t                       SFR_RM3;            /**< Offset: 0x68 (R/W  32) Read Margin3 Register */
  __IO  uint32_t                       SFR_RM4;            /**< Offset: 0x6C (R/W  32) Read Margin4 Register */
  __IO  uint32_t                       SFR_RM5;            /**< Offset: 0x70 (R/W  32) Read Margin5 Register */
  __I   uint8_t                        Reserved5[0x08];
  __IO  uint32_t                       SFR_LS;             /**< Offset: 0x7C (R/W  32) Light Sleep Register */
  __I   uint8_t                        Reserved6[0x30];
  __IO  uint32_t                       SFR_CAL0;           /**< Offset: 0xB0 (R/W  32) I/O Calibration 0 Register */
  __IO  uint32_t                       SFR_CAL1;           /**< Offset: 0xB4 (R/W  32) I/O Calibration 1 Register */
  __I   uint8_t                        Reserved7[0x2C];
  __IO  uint32_t                       SFR_WPMR;           /**< Offset: 0xE4 (R/W  32) Write Protection Mode Register */
  __I   uint8_t                        Reserved8[0x18];
  __IO  uint32_t                       SFR_SPARE;          /**< Offset: 0x100 (R/W  32) Spare Register */
  __IO  uint32_t                       SFR_BU_SPARE;       /**< Offset: 0x104 (R/W  32) Spare Register (BackUp) */
} sfr_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAM9X_SFR_COMPONENT_H_ */
