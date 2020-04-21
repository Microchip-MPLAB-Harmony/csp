/**
 * \brief Component description for PAC
 *
 * Copyright (c) 2020 Microchip Technology Inc. and its subsidiaries.
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

/* file generated from device description version 2020-02-04T13:16:04Z */
#ifndef _SAML10_PAC_COMPONENT_H_
#define _SAML10_PAC_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR PAC                                          */
/* ************************************************************************** */

/* -------- PAC_WRCTRL : (PAC Offset: 0x00) (R/W 32) Write control -------- */
#define PAC_WRCTRL_RESETVALUE                 _U_(0x00)                                            /**<  (PAC_WRCTRL) Write control  Reset Value */

#define PAC_WRCTRL_PERID_Pos                  _U_(0)                                               /**< (PAC_WRCTRL) Peripheral identifier Position */
#define PAC_WRCTRL_PERID_Msk                  (_U_(0xFFFF) << PAC_WRCTRL_PERID_Pos)                /**< (PAC_WRCTRL) Peripheral identifier Mask */
#define PAC_WRCTRL_PERID(value)               (PAC_WRCTRL_PERID_Msk & ((value) << PAC_WRCTRL_PERID_Pos))
#define PAC_WRCTRL_KEY_Pos                    _U_(16)                                              /**< (PAC_WRCTRL) Peripheral access control key Position */
#define PAC_WRCTRL_KEY_Msk                    (_U_(0xFF) << PAC_WRCTRL_KEY_Pos)                    /**< (PAC_WRCTRL) Peripheral access control key Mask */
#define PAC_WRCTRL_KEY(value)                 (PAC_WRCTRL_KEY_Msk & ((value) << PAC_WRCTRL_KEY_Pos))
#define   PAC_WRCTRL_KEY_OFF_Val              _U_(0x0)                                             /**< (PAC_WRCTRL) No action  */
#define   PAC_WRCTRL_KEY_CLEAR_Val            _U_(0x1)                                             /**< (PAC_WRCTRL) Clear protection  */
#define   PAC_WRCTRL_KEY_SET_Val              _U_(0x2)                                             /**< (PAC_WRCTRL) Set protection  */
#define   PAC_WRCTRL_KEY_LOCK_Val             _U_(0x3)                                             /**< (PAC_WRCTRL) Set and lock protection  */
#define PAC_WRCTRL_KEY_OFF                    (PAC_WRCTRL_KEY_OFF_Val << PAC_WRCTRL_KEY_Pos)       /**< (PAC_WRCTRL) No action Position  */
#define PAC_WRCTRL_KEY_CLEAR                  (PAC_WRCTRL_KEY_CLEAR_Val << PAC_WRCTRL_KEY_Pos)     /**< (PAC_WRCTRL) Clear protection Position  */
#define PAC_WRCTRL_KEY_SET                    (PAC_WRCTRL_KEY_SET_Val << PAC_WRCTRL_KEY_Pos)       /**< (PAC_WRCTRL) Set protection Position  */
#define PAC_WRCTRL_KEY_LOCK                   (PAC_WRCTRL_KEY_LOCK_Val << PAC_WRCTRL_KEY_Pos)      /**< (PAC_WRCTRL) Set and lock protection Position  */
#define PAC_WRCTRL_Msk                        _U_(0x00FFFFFF)                                      /**< (PAC_WRCTRL) Register Mask  */


/* -------- PAC_EVCTRL : (PAC Offset: 0x04) (R/W 8) Event control -------- */
#define PAC_EVCTRL_RESETVALUE                 _U_(0x00)                                            /**<  (PAC_EVCTRL) Event control  Reset Value */

#define PAC_EVCTRL_ERREO_Pos                  _U_(0)                                               /**< (PAC_EVCTRL) Peripheral acess error event output Position */
#define PAC_EVCTRL_ERREO_Msk                  (_U_(0x1) << PAC_EVCTRL_ERREO_Pos)                   /**< (PAC_EVCTRL) Peripheral acess error event output Mask */
#define PAC_EVCTRL_ERREO(value)               (PAC_EVCTRL_ERREO_Msk & ((value) << PAC_EVCTRL_ERREO_Pos))
#define PAC_EVCTRL_Msk                        _U_(0x01)                                            /**< (PAC_EVCTRL) Register Mask  */


/* -------- PAC_INTENCLR : (PAC Offset: 0x08) (R/W 8) Interrupt enable clear -------- */
#define PAC_INTENCLR_RESETVALUE               _U_(0x00)                                            /**<  (PAC_INTENCLR) Interrupt enable clear  Reset Value */

#define PAC_INTENCLR_ERR_Pos                  _U_(0)                                               /**< (PAC_INTENCLR) Peripheral access error interrupt disable Position */
#define PAC_INTENCLR_ERR_Msk                  (_U_(0x1) << PAC_INTENCLR_ERR_Pos)                   /**< (PAC_INTENCLR) Peripheral access error interrupt disable Mask */
#define PAC_INTENCLR_ERR(value)               (PAC_INTENCLR_ERR_Msk & ((value) << PAC_INTENCLR_ERR_Pos))
#define PAC_INTENCLR_Msk                      _U_(0x01)                                            /**< (PAC_INTENCLR) Register Mask  */


/* -------- PAC_INTENSET : (PAC Offset: 0x09) (R/W 8) Interrupt enable set -------- */
#define PAC_INTENSET_RESETVALUE               _U_(0x00)                                            /**<  (PAC_INTENSET) Interrupt enable set  Reset Value */

#define PAC_INTENSET_ERR_Pos                  _U_(0)                                               /**< (PAC_INTENSET) Peripheral access error interrupt enable Position */
#define PAC_INTENSET_ERR_Msk                  (_U_(0x1) << PAC_INTENSET_ERR_Pos)                   /**< (PAC_INTENSET) Peripheral access error interrupt enable Mask */
#define PAC_INTENSET_ERR(value)               (PAC_INTENSET_ERR_Msk & ((value) << PAC_INTENSET_ERR_Pos))
#define PAC_INTENSET_Msk                      _U_(0x01)                                            /**< (PAC_INTENSET) Register Mask  */


/* -------- PAC_INTFLAGAHB : (PAC Offset: 0x10) (R/W 32) Bridge interrupt flag status -------- */
#define PAC_INTFLAGAHB_RESETVALUE             _U_(0x00)                                            /**<  (PAC_INTFLAGAHB) Bridge interrupt flag status  Reset Value */

#define PAC_INTFLAGAHB_FLASH_Pos              _U_(0)                                               /**< (PAC_INTFLAGAHB) FLASH Position */
#define PAC_INTFLAGAHB_FLASH_Msk              (_U_(0x1) << PAC_INTFLAGAHB_FLASH_Pos)               /**< (PAC_INTFLAGAHB) FLASH Mask */
#define PAC_INTFLAGAHB_FLASH(value)           (PAC_INTFLAGAHB_FLASH_Msk & ((value) << PAC_INTFLAGAHB_FLASH_Pos))
#define PAC_INTFLAGAHB_APBA_Pos               _U_(1)                                               /**< (PAC_INTFLAGAHB) AHB-APB Bridge A Position */
#define PAC_INTFLAGAHB_APBA_Msk               (_U_(0x1) << PAC_INTFLAGAHB_APBA_Pos)                /**< (PAC_INTFLAGAHB) AHB-APB Bridge A Mask */
#define PAC_INTFLAGAHB_APBA(value)            (PAC_INTFLAGAHB_APBA_Msk & ((value) << PAC_INTFLAGAHB_APBA_Pos))
#define PAC_INTFLAGAHB_APBB_Pos               _U_(2)                                               /**< (PAC_INTFLAGAHB) AHB-APB Bridge B Position */
#define PAC_INTFLAGAHB_APBB_Msk               (_U_(0x1) << PAC_INTFLAGAHB_APBB_Pos)                /**< (PAC_INTFLAGAHB) AHB-APB Bridge B Mask */
#define PAC_INTFLAGAHB_APBB(value)            (PAC_INTFLAGAHB_APBB_Msk & ((value) << PAC_INTFLAGAHB_APBB_Pos))
#define PAC_INTFLAGAHB_APBC_Pos               _U_(3)                                               /**< (PAC_INTFLAGAHB) AHB-APB Bridge C Position */
#define PAC_INTFLAGAHB_APBC_Msk               (_U_(0x1) << PAC_INTFLAGAHB_APBC_Pos)                /**< (PAC_INTFLAGAHB) AHB-APB Bridge C Mask */
#define PAC_INTFLAGAHB_APBC(value)            (PAC_INTFLAGAHB_APBC_Msk & ((value) << PAC_INTFLAGAHB_APBC_Pos))
#define PAC_INTFLAGAHB_HSRAMCPU_Pos           _U_(4)                                               /**< (PAC_INTFLAGAHB) HSRAMCPU Position */
#define PAC_INTFLAGAHB_HSRAMCPU_Msk           (_U_(0x1) << PAC_INTFLAGAHB_HSRAMCPU_Pos)            /**< (PAC_INTFLAGAHB) HSRAMCPU Mask */
#define PAC_INTFLAGAHB_HSRAMCPU(value)        (PAC_INTFLAGAHB_HSRAMCPU_Msk & ((value) << PAC_INTFLAGAHB_HSRAMCPU_Pos))
#define PAC_INTFLAGAHB_HSRAMDMAC_Pos          _U_(5)                                               /**< (PAC_INTFLAGAHB) HSRAMDMAC Position */
#define PAC_INTFLAGAHB_HSRAMDMAC_Msk          (_U_(0x1) << PAC_INTFLAGAHB_HSRAMDMAC_Pos)           /**< (PAC_INTFLAGAHB) HSRAMDMAC Mask */
#define PAC_INTFLAGAHB_HSRAMDMAC(value)       (PAC_INTFLAGAHB_HSRAMDMAC_Msk & ((value) << PAC_INTFLAGAHB_HSRAMDMAC_Pos))
#define PAC_INTFLAGAHB_HSRAMDSU_Pos           _U_(6)                                               /**< (PAC_INTFLAGAHB) HSRAMDSU Position */
#define PAC_INTFLAGAHB_HSRAMDSU_Msk           (_U_(0x1) << PAC_INTFLAGAHB_HSRAMDSU_Pos)            /**< (PAC_INTFLAGAHB) HSRAMDSU Mask */
#define PAC_INTFLAGAHB_HSRAMDSU(value)        (PAC_INTFLAGAHB_HSRAMDSU_Msk & ((value) << PAC_INTFLAGAHB_HSRAMDSU_Pos))
#define PAC_INTFLAGAHB_BROM_Pos               _U_(7)                                               /**< (PAC_INTFLAGAHB) BROM Position */
#define PAC_INTFLAGAHB_BROM_Msk               (_U_(0x1) << PAC_INTFLAGAHB_BROM_Pos)                /**< (PAC_INTFLAGAHB) BROM Mask */
#define PAC_INTFLAGAHB_BROM(value)            (PAC_INTFLAGAHB_BROM_Msk & ((value) << PAC_INTFLAGAHB_BROM_Pos))
#define PAC_INTFLAGAHB_Msk                    _U_(0x000000FF)                                      /**< (PAC_INTFLAGAHB) Register Mask  */


/* -------- PAC_INTFLAGA : (PAC Offset: 0x14) (R/W 32) Peripheral interrupt flag status - Bridge A -------- */
#define PAC_INTFLAGA_RESETVALUE               _U_(0x00)                                            /**<  (PAC_INTFLAGA) Peripheral interrupt flag status - Bridge A  Reset Value */

#define PAC_INTFLAGA_PAC_Pos                  _U_(0)                                               /**< (PAC_INTFLAGA) PAC Position */
#define PAC_INTFLAGA_PAC_Msk                  (_U_(0x1) << PAC_INTFLAGA_PAC_Pos)                   /**< (PAC_INTFLAGA) PAC Mask */
#define PAC_INTFLAGA_PAC(value)               (PAC_INTFLAGA_PAC_Msk & ((value) << PAC_INTFLAGA_PAC_Pos))
#define PAC_INTFLAGA_PM_Pos                   _U_(1)                                               /**< (PAC_INTFLAGA) PM Position */
#define PAC_INTFLAGA_PM_Msk                   (_U_(0x1) << PAC_INTFLAGA_PM_Pos)                    /**< (PAC_INTFLAGA) PM Mask */
#define PAC_INTFLAGA_PM(value)                (PAC_INTFLAGA_PM_Msk & ((value) << PAC_INTFLAGA_PM_Pos))
#define PAC_INTFLAGA_MCLK_Pos                 _U_(2)                                               /**< (PAC_INTFLAGA) MCLK Position */
#define PAC_INTFLAGA_MCLK_Msk                 (_U_(0x1) << PAC_INTFLAGA_MCLK_Pos)                  /**< (PAC_INTFLAGA) MCLK Mask */
#define PAC_INTFLAGA_MCLK(value)              (PAC_INTFLAGA_MCLK_Msk & ((value) << PAC_INTFLAGA_MCLK_Pos))
#define PAC_INTFLAGA_RSTC_Pos                 _U_(3)                                               /**< (PAC_INTFLAGA) RSTC Position */
#define PAC_INTFLAGA_RSTC_Msk                 (_U_(0x1) << PAC_INTFLAGA_RSTC_Pos)                  /**< (PAC_INTFLAGA) RSTC Mask */
#define PAC_INTFLAGA_RSTC(value)              (PAC_INTFLAGA_RSTC_Msk & ((value) << PAC_INTFLAGA_RSTC_Pos))
#define PAC_INTFLAGA_OSCCTRL_Pos              _U_(4)                                               /**< (PAC_INTFLAGA) OSCCTRL Position */
#define PAC_INTFLAGA_OSCCTRL_Msk              (_U_(0x1) << PAC_INTFLAGA_OSCCTRL_Pos)               /**< (PAC_INTFLAGA) OSCCTRL Mask */
#define PAC_INTFLAGA_OSCCTRL(value)           (PAC_INTFLAGA_OSCCTRL_Msk & ((value) << PAC_INTFLAGA_OSCCTRL_Pos))
#define PAC_INTFLAGA_OSC32KCTRL_Pos           _U_(5)                                               /**< (PAC_INTFLAGA) OSC32KCTRL Position */
#define PAC_INTFLAGA_OSC32KCTRL_Msk           (_U_(0x1) << PAC_INTFLAGA_OSC32KCTRL_Pos)            /**< (PAC_INTFLAGA) OSC32KCTRL Mask */
#define PAC_INTFLAGA_OSC32KCTRL(value)        (PAC_INTFLAGA_OSC32KCTRL_Msk & ((value) << PAC_INTFLAGA_OSC32KCTRL_Pos))
#define PAC_INTFLAGA_SUPC_Pos                 _U_(6)                                               /**< (PAC_INTFLAGA) SUPC Position */
#define PAC_INTFLAGA_SUPC_Msk                 (_U_(0x1) << PAC_INTFLAGA_SUPC_Pos)                  /**< (PAC_INTFLAGA) SUPC Mask */
#define PAC_INTFLAGA_SUPC(value)              (PAC_INTFLAGA_SUPC_Msk & ((value) << PAC_INTFLAGA_SUPC_Pos))
#define PAC_INTFLAGA_GCLK_Pos                 _U_(7)                                               /**< (PAC_INTFLAGA) GCLK Position */
#define PAC_INTFLAGA_GCLK_Msk                 (_U_(0x1) << PAC_INTFLAGA_GCLK_Pos)                  /**< (PAC_INTFLAGA) GCLK Mask */
#define PAC_INTFLAGA_GCLK(value)              (PAC_INTFLAGA_GCLK_Msk & ((value) << PAC_INTFLAGA_GCLK_Pos))
#define PAC_INTFLAGA_WDT_Pos                  _U_(8)                                               /**< (PAC_INTFLAGA) WDT Position */
#define PAC_INTFLAGA_WDT_Msk                  (_U_(0x1) << PAC_INTFLAGA_WDT_Pos)                   /**< (PAC_INTFLAGA) WDT Mask */
#define PAC_INTFLAGA_WDT(value)               (PAC_INTFLAGA_WDT_Msk & ((value) << PAC_INTFLAGA_WDT_Pos))
#define PAC_INTFLAGA_RTC_Pos                  _U_(9)                                               /**< (PAC_INTFLAGA) RTC Position */
#define PAC_INTFLAGA_RTC_Msk                  (_U_(0x1) << PAC_INTFLAGA_RTC_Pos)                   /**< (PAC_INTFLAGA) RTC Mask */
#define PAC_INTFLAGA_RTC(value)               (PAC_INTFLAGA_RTC_Msk & ((value) << PAC_INTFLAGA_RTC_Pos))
#define PAC_INTFLAGA_EIC_Pos                  _U_(10)                                              /**< (PAC_INTFLAGA) EIC Position */
#define PAC_INTFLAGA_EIC_Msk                  (_U_(0x1) << PAC_INTFLAGA_EIC_Pos)                   /**< (PAC_INTFLAGA) EIC Mask */
#define PAC_INTFLAGA_EIC(value)               (PAC_INTFLAGA_EIC_Msk & ((value) << PAC_INTFLAGA_EIC_Pos))
#define PAC_INTFLAGA_FREQM_Pos                _U_(11)                                              /**< (PAC_INTFLAGA) FREQM Position */
#define PAC_INTFLAGA_FREQM_Msk                (_U_(0x1) << PAC_INTFLAGA_FREQM_Pos)                 /**< (PAC_INTFLAGA) FREQM Mask */
#define PAC_INTFLAGA_FREQM(value)             (PAC_INTFLAGA_FREQM_Msk & ((value) << PAC_INTFLAGA_FREQM_Pos))
#define PAC_INTFLAGA_PORT_Pos                 _U_(12)                                              /**< (PAC_INTFLAGA) PORT Position */
#define PAC_INTFLAGA_PORT_Msk                 (_U_(0x1) << PAC_INTFLAGA_PORT_Pos)                  /**< (PAC_INTFLAGA) PORT Mask */
#define PAC_INTFLAGA_PORT(value)              (PAC_INTFLAGA_PORT_Msk & ((value) << PAC_INTFLAGA_PORT_Pos))
#define PAC_INTFLAGA_AC_Pos                   _U_(13)                                              /**< (PAC_INTFLAGA) AC Position */
#define PAC_INTFLAGA_AC_Msk                   (_U_(0x1) << PAC_INTFLAGA_AC_Pos)                    /**< (PAC_INTFLAGA) AC Mask */
#define PAC_INTFLAGA_AC(value)                (PAC_INTFLAGA_AC_Msk & ((value) << PAC_INTFLAGA_AC_Pos))
#define PAC_INTFLAGA_Msk                      _U_(0x00003FFF)                                      /**< (PAC_INTFLAGA) Register Mask  */


/* -------- PAC_INTFLAGB : (PAC Offset: 0x18) (R/W 32) Peripheral interrupt flag status - Bridge B -------- */
#define PAC_INTFLAGB_RESETVALUE               _U_(0x00)                                            /**<  (PAC_INTFLAGB) Peripheral interrupt flag status - Bridge B  Reset Value */

#define PAC_INTFLAGB_IDAU_Pos                 _U_(0)                                               /**< (PAC_INTFLAGB) IDAU Position */
#define PAC_INTFLAGB_IDAU_Msk                 (_U_(0x1) << PAC_INTFLAGB_IDAU_Pos)                  /**< (PAC_INTFLAGB) IDAU Mask */
#define PAC_INTFLAGB_IDAU(value)              (PAC_INTFLAGB_IDAU_Msk & ((value) << PAC_INTFLAGB_IDAU_Pos))
#define PAC_INTFLAGB_DSU_Pos                  _U_(1)                                               /**< (PAC_INTFLAGB) DSU Position */
#define PAC_INTFLAGB_DSU_Msk                  (_U_(0x1) << PAC_INTFLAGB_DSU_Pos)                   /**< (PAC_INTFLAGB) DSU Mask */
#define PAC_INTFLAGB_DSU(value)               (PAC_INTFLAGB_DSU_Msk & ((value) << PAC_INTFLAGB_DSU_Pos))
#define PAC_INTFLAGB_NVMCTRL_Pos              _U_(2)                                               /**< (PAC_INTFLAGB) NVMCTRL Position */
#define PAC_INTFLAGB_NVMCTRL_Msk              (_U_(0x1) << PAC_INTFLAGB_NVMCTRL_Pos)               /**< (PAC_INTFLAGB) NVMCTRL Mask */
#define PAC_INTFLAGB_NVMCTRL(value)           (PAC_INTFLAGB_NVMCTRL_Msk & ((value) << PAC_INTFLAGB_NVMCTRL_Pos))
#define PAC_INTFLAGB_DMAC_Pos                 _U_(3)                                               /**< (PAC_INTFLAGB) DMAC Position */
#define PAC_INTFLAGB_DMAC_Msk                 (_U_(0x1) << PAC_INTFLAGB_DMAC_Pos)                  /**< (PAC_INTFLAGB) DMAC Mask */
#define PAC_INTFLAGB_DMAC(value)              (PAC_INTFLAGB_DMAC_Msk & ((value) << PAC_INTFLAGB_DMAC_Pos))
#define PAC_INTFLAGB_Msk                      _U_(0x0000000F)                                      /**< (PAC_INTFLAGB) Register Mask  */


/* -------- PAC_INTFLAGC : (PAC Offset: 0x1C) (R/W 32) Peripheral interrupt flag status - Bridge C -------- */
#define PAC_INTFLAGC_RESETVALUE               _U_(0x00)                                            /**<  (PAC_INTFLAGC) Peripheral interrupt flag status - Bridge C  Reset Value */

#define PAC_INTFLAGC_EVSYS_Pos                _U_(0)                                               /**< (PAC_INTFLAGC) EVSYS Position */
#define PAC_INTFLAGC_EVSYS_Msk                (_U_(0x1) << PAC_INTFLAGC_EVSYS_Pos)                 /**< (PAC_INTFLAGC) EVSYS Mask */
#define PAC_INTFLAGC_EVSYS(value)             (PAC_INTFLAGC_EVSYS_Msk & ((value) << PAC_INTFLAGC_EVSYS_Pos))
#define PAC_INTFLAGC_SERCOM0_Pos              _U_(1)                                               /**< (PAC_INTFLAGC) SERCOM0 Position */
#define PAC_INTFLAGC_SERCOM0_Msk              (_U_(0x1) << PAC_INTFLAGC_SERCOM0_Pos)               /**< (PAC_INTFLAGC) SERCOM0 Mask */
#define PAC_INTFLAGC_SERCOM0(value)           (PAC_INTFLAGC_SERCOM0_Msk & ((value) << PAC_INTFLAGC_SERCOM0_Pos))
#define PAC_INTFLAGC_SERCOM1_Pos              _U_(2)                                               /**< (PAC_INTFLAGC) SERCOM1 Position */
#define PAC_INTFLAGC_SERCOM1_Msk              (_U_(0x1) << PAC_INTFLAGC_SERCOM1_Pos)               /**< (PAC_INTFLAGC) SERCOM1 Mask */
#define PAC_INTFLAGC_SERCOM1(value)           (PAC_INTFLAGC_SERCOM1_Msk & ((value) << PAC_INTFLAGC_SERCOM1_Pos))
#define PAC_INTFLAGC_SERCOM2_Pos              _U_(3)                                               /**< (PAC_INTFLAGC) SERCOM2 Position */
#define PAC_INTFLAGC_SERCOM2_Msk              (_U_(0x1) << PAC_INTFLAGC_SERCOM2_Pos)               /**< (PAC_INTFLAGC) SERCOM2 Mask */
#define PAC_INTFLAGC_SERCOM2(value)           (PAC_INTFLAGC_SERCOM2_Msk & ((value) << PAC_INTFLAGC_SERCOM2_Pos))
#define PAC_INTFLAGC_TC0_Pos                  _U_(4)                                               /**< (PAC_INTFLAGC) TC0 Position */
#define PAC_INTFLAGC_TC0_Msk                  (_U_(0x1) << PAC_INTFLAGC_TC0_Pos)                   /**< (PAC_INTFLAGC) TC0 Mask */
#define PAC_INTFLAGC_TC0(value)               (PAC_INTFLAGC_TC0_Msk & ((value) << PAC_INTFLAGC_TC0_Pos))
#define PAC_INTFLAGC_TC1_Pos                  _U_(5)                                               /**< (PAC_INTFLAGC) TC1 Position */
#define PAC_INTFLAGC_TC1_Msk                  (_U_(0x1) << PAC_INTFLAGC_TC1_Pos)                   /**< (PAC_INTFLAGC) TC1 Mask */
#define PAC_INTFLAGC_TC1(value)               (PAC_INTFLAGC_TC1_Msk & ((value) << PAC_INTFLAGC_TC1_Pos))
#define PAC_INTFLAGC_TC2_Pos                  _U_(6)                                               /**< (PAC_INTFLAGC) TC2 Position */
#define PAC_INTFLAGC_TC2_Msk                  (_U_(0x1) << PAC_INTFLAGC_TC2_Pos)                   /**< (PAC_INTFLAGC) TC2 Mask */
#define PAC_INTFLAGC_TC2(value)               (PAC_INTFLAGC_TC2_Msk & ((value) << PAC_INTFLAGC_TC2_Pos))
#define PAC_INTFLAGC_ADC_Pos                  _U_(7)                                               /**< (PAC_INTFLAGC) ADC Position */
#define PAC_INTFLAGC_ADC_Msk                  (_U_(0x1) << PAC_INTFLAGC_ADC_Pos)                   /**< (PAC_INTFLAGC) ADC Mask */
#define PAC_INTFLAGC_ADC(value)               (PAC_INTFLAGC_ADC_Msk & ((value) << PAC_INTFLAGC_ADC_Pos))
#define PAC_INTFLAGC_DAC_Pos                  _U_(8)                                               /**< (PAC_INTFLAGC) DAC Position */
#define PAC_INTFLAGC_DAC_Msk                  (_U_(0x1) << PAC_INTFLAGC_DAC_Pos)                   /**< (PAC_INTFLAGC) DAC Mask */
#define PAC_INTFLAGC_DAC(value)               (PAC_INTFLAGC_DAC_Msk & ((value) << PAC_INTFLAGC_DAC_Pos))
#define PAC_INTFLAGC_PTC_Pos                  _U_(9)                                               /**< (PAC_INTFLAGC) PTC Position */
#define PAC_INTFLAGC_PTC_Msk                  (_U_(0x1) << PAC_INTFLAGC_PTC_Pos)                   /**< (PAC_INTFLAGC) PTC Mask */
#define PAC_INTFLAGC_PTC(value)               (PAC_INTFLAGC_PTC_Msk & ((value) << PAC_INTFLAGC_PTC_Pos))
#define PAC_INTFLAGC_TRNG_Pos                 _U_(10)                                              /**< (PAC_INTFLAGC) TRNG Position */
#define PAC_INTFLAGC_TRNG_Msk                 (_U_(0x1) << PAC_INTFLAGC_TRNG_Pos)                  /**< (PAC_INTFLAGC) TRNG Mask */
#define PAC_INTFLAGC_TRNG(value)              (PAC_INTFLAGC_TRNG_Msk & ((value) << PAC_INTFLAGC_TRNG_Pos))
#define PAC_INTFLAGC_CCL_Pos                  _U_(11)                                              /**< (PAC_INTFLAGC) CCL Position */
#define PAC_INTFLAGC_CCL_Msk                  (_U_(0x1) << PAC_INTFLAGC_CCL_Pos)                   /**< (PAC_INTFLAGC) CCL Mask */
#define PAC_INTFLAGC_CCL(value)               (PAC_INTFLAGC_CCL_Msk & ((value) << PAC_INTFLAGC_CCL_Pos))
#define PAC_INTFLAGC_OPAMP_Pos                _U_(12)                                              /**< (PAC_INTFLAGC) OPAMP Position */
#define PAC_INTFLAGC_OPAMP_Msk                (_U_(0x1) << PAC_INTFLAGC_OPAMP_Pos)                 /**< (PAC_INTFLAGC) OPAMP Mask */
#define PAC_INTFLAGC_OPAMP(value)             (PAC_INTFLAGC_OPAMP_Msk & ((value) << PAC_INTFLAGC_OPAMP_Pos))
#define PAC_INTFLAGC_TRAM_Pos                 _U_(13)                                              /**< (PAC_INTFLAGC) TRAM Position */
#define PAC_INTFLAGC_TRAM_Msk                 (_U_(0x1) << PAC_INTFLAGC_TRAM_Pos)                  /**< (PAC_INTFLAGC) TRAM Mask */
#define PAC_INTFLAGC_TRAM(value)              (PAC_INTFLAGC_TRAM_Msk & ((value) << PAC_INTFLAGC_TRAM_Pos))
#define PAC_INTFLAGC_Msk                      _U_(0x00003FFF)                                      /**< (PAC_INTFLAGC) Register Mask  */

#define PAC_INTFLAGC_SERCOM_Pos               _U_(1)                                               /**< (PAC_INTFLAGC Position) SERCOMx */
#define PAC_INTFLAGC_SERCOM_Msk               (_U_(0x7) << PAC_INTFLAGC_SERCOM_Pos)                /**< (PAC_INTFLAGC Mask) SERCOM */
#define PAC_INTFLAGC_SERCOM(value)            (PAC_INTFLAGC_SERCOM_Msk & ((value) << PAC_INTFLAGC_SERCOM_Pos)) 
#define PAC_INTFLAGC_TC_Pos                   _U_(4)                                               /**< (PAC_INTFLAGC Position) TCx */
#define PAC_INTFLAGC_TC_Msk                   (_U_(0x7) << PAC_INTFLAGC_TC_Pos)                    /**< (PAC_INTFLAGC Mask) TC */
#define PAC_INTFLAGC_TC(value)                (PAC_INTFLAGC_TC_Msk & ((value) << PAC_INTFLAGC_TC_Pos)) 

/* -------- PAC_STATUSA : (PAC Offset: 0x34) ( R/ 32) Peripheral write protection status - Bridge A -------- */
#define PAC_STATUSA_RESETVALUE                _U_(0xC000)                                          /**<  (PAC_STATUSA) Peripheral write protection status - Bridge A  Reset Value */

#define PAC_STATUSA_PAC_Pos                   _U_(0)                                               /**< (PAC_STATUSA) PAC APB Protect Enable Position */
#define PAC_STATUSA_PAC_Msk                   (_U_(0x1) << PAC_STATUSA_PAC_Pos)                    /**< (PAC_STATUSA) PAC APB Protect Enable Mask */
#define PAC_STATUSA_PAC(value)                (PAC_STATUSA_PAC_Msk & ((value) << PAC_STATUSA_PAC_Pos))
#define PAC_STATUSA_PM_Pos                    _U_(1)                                               /**< (PAC_STATUSA) PM APB Protect Enable Position */
#define PAC_STATUSA_PM_Msk                    (_U_(0x1) << PAC_STATUSA_PM_Pos)                     /**< (PAC_STATUSA) PM APB Protect Enable Mask */
#define PAC_STATUSA_PM(value)                 (PAC_STATUSA_PM_Msk & ((value) << PAC_STATUSA_PM_Pos))
#define PAC_STATUSA_MCLK_Pos                  _U_(2)                                               /**< (PAC_STATUSA) MCLK APB Protect Enable Position */
#define PAC_STATUSA_MCLK_Msk                  (_U_(0x1) << PAC_STATUSA_MCLK_Pos)                   /**< (PAC_STATUSA) MCLK APB Protect Enable Mask */
#define PAC_STATUSA_MCLK(value)               (PAC_STATUSA_MCLK_Msk & ((value) << PAC_STATUSA_MCLK_Pos))
#define PAC_STATUSA_RSTC_Pos                  _U_(3)                                               /**< (PAC_STATUSA) RSTC APB Protect Enable Position */
#define PAC_STATUSA_RSTC_Msk                  (_U_(0x1) << PAC_STATUSA_RSTC_Pos)                   /**< (PAC_STATUSA) RSTC APB Protect Enable Mask */
#define PAC_STATUSA_RSTC(value)               (PAC_STATUSA_RSTC_Msk & ((value) << PAC_STATUSA_RSTC_Pos))
#define PAC_STATUSA_OSCCTRL_Pos               _U_(4)                                               /**< (PAC_STATUSA) OSCCTRL APB Protect Enable Position */
#define PAC_STATUSA_OSCCTRL_Msk               (_U_(0x1) << PAC_STATUSA_OSCCTRL_Pos)                /**< (PAC_STATUSA) OSCCTRL APB Protect Enable Mask */
#define PAC_STATUSA_OSCCTRL(value)            (PAC_STATUSA_OSCCTRL_Msk & ((value) << PAC_STATUSA_OSCCTRL_Pos))
#define PAC_STATUSA_OSC32KCTRL_Pos            _U_(5)                                               /**< (PAC_STATUSA) OSC32KCTRL APB Protect Enable Position */
#define PAC_STATUSA_OSC32KCTRL_Msk            (_U_(0x1) << PAC_STATUSA_OSC32KCTRL_Pos)             /**< (PAC_STATUSA) OSC32KCTRL APB Protect Enable Mask */
#define PAC_STATUSA_OSC32KCTRL(value)         (PAC_STATUSA_OSC32KCTRL_Msk & ((value) << PAC_STATUSA_OSC32KCTRL_Pos))
#define PAC_STATUSA_SUPC_Pos                  _U_(6)                                               /**< (PAC_STATUSA) SUPC APB Protect Enable Position */
#define PAC_STATUSA_SUPC_Msk                  (_U_(0x1) << PAC_STATUSA_SUPC_Pos)                   /**< (PAC_STATUSA) SUPC APB Protect Enable Mask */
#define PAC_STATUSA_SUPC(value)               (PAC_STATUSA_SUPC_Msk & ((value) << PAC_STATUSA_SUPC_Pos))
#define PAC_STATUSA_GCLK_Pos                  _U_(7)                                               /**< (PAC_STATUSA) GCLK APB Protect Enable Position */
#define PAC_STATUSA_GCLK_Msk                  (_U_(0x1) << PAC_STATUSA_GCLK_Pos)                   /**< (PAC_STATUSA) GCLK APB Protect Enable Mask */
#define PAC_STATUSA_GCLK(value)               (PAC_STATUSA_GCLK_Msk & ((value) << PAC_STATUSA_GCLK_Pos))
#define PAC_STATUSA_WDT_Pos                   _U_(8)                                               /**< (PAC_STATUSA) WDT APB Protect Enable Position */
#define PAC_STATUSA_WDT_Msk                   (_U_(0x1) << PAC_STATUSA_WDT_Pos)                    /**< (PAC_STATUSA) WDT APB Protect Enable Mask */
#define PAC_STATUSA_WDT(value)                (PAC_STATUSA_WDT_Msk & ((value) << PAC_STATUSA_WDT_Pos))
#define PAC_STATUSA_RTC_Pos                   _U_(9)                                               /**< (PAC_STATUSA) RTC APB Protect Enable Position */
#define PAC_STATUSA_RTC_Msk                   (_U_(0x1) << PAC_STATUSA_RTC_Pos)                    /**< (PAC_STATUSA) RTC APB Protect Enable Mask */
#define PAC_STATUSA_RTC(value)                (PAC_STATUSA_RTC_Msk & ((value) << PAC_STATUSA_RTC_Pos))
#define PAC_STATUSA_EIC_Pos                   _U_(10)                                              /**< (PAC_STATUSA) EIC APB Protect Enable Position */
#define PAC_STATUSA_EIC_Msk                   (_U_(0x1) << PAC_STATUSA_EIC_Pos)                    /**< (PAC_STATUSA) EIC APB Protect Enable Mask */
#define PAC_STATUSA_EIC(value)                (PAC_STATUSA_EIC_Msk & ((value) << PAC_STATUSA_EIC_Pos))
#define PAC_STATUSA_FREQM_Pos                 _U_(11)                                              /**< (PAC_STATUSA) FREQM APB Protect Enable Position */
#define PAC_STATUSA_FREQM_Msk                 (_U_(0x1) << PAC_STATUSA_FREQM_Pos)                  /**< (PAC_STATUSA) FREQM APB Protect Enable Mask */
#define PAC_STATUSA_FREQM(value)              (PAC_STATUSA_FREQM_Msk & ((value) << PAC_STATUSA_FREQM_Pos))
#define PAC_STATUSA_PORT_Pos                  _U_(12)                                              /**< (PAC_STATUSA) PORT APB Protect Enable Position */
#define PAC_STATUSA_PORT_Msk                  (_U_(0x1) << PAC_STATUSA_PORT_Pos)                   /**< (PAC_STATUSA) PORT APB Protect Enable Mask */
#define PAC_STATUSA_PORT(value)               (PAC_STATUSA_PORT_Msk & ((value) << PAC_STATUSA_PORT_Pos))
#define PAC_STATUSA_AC_Pos                    _U_(13)                                              /**< (PAC_STATUSA) AC APB Protect Enable Position */
#define PAC_STATUSA_AC_Msk                    (_U_(0x1) << PAC_STATUSA_AC_Pos)                     /**< (PAC_STATUSA) AC APB Protect Enable Mask */
#define PAC_STATUSA_AC(value)                 (PAC_STATUSA_AC_Msk & ((value) << PAC_STATUSA_AC_Pos))
#define PAC_STATUSA_Msk                       _U_(0x00003FFF)                                      /**< (PAC_STATUSA) Register Mask  */


/* -------- PAC_STATUSB : (PAC Offset: 0x38) ( R/ 32) Peripheral write protection status - Bridge B -------- */
#define PAC_STATUSB_RESETVALUE                _U_(0x02)                                            /**<  (PAC_STATUSB) Peripheral write protection status - Bridge B  Reset Value */

#define PAC_STATUSB_IDAU_Pos                  _U_(0)                                               /**< (PAC_STATUSB) IDAU APB Protect Enable Position */
#define PAC_STATUSB_IDAU_Msk                  (_U_(0x1) << PAC_STATUSB_IDAU_Pos)                   /**< (PAC_STATUSB) IDAU APB Protect Enable Mask */
#define PAC_STATUSB_IDAU(value)               (PAC_STATUSB_IDAU_Msk & ((value) << PAC_STATUSB_IDAU_Pos))
#define PAC_STATUSB_DSU_Pos                   _U_(1)                                               /**< (PAC_STATUSB) DSU APB Protect Enable Position */
#define PAC_STATUSB_DSU_Msk                   (_U_(0x1) << PAC_STATUSB_DSU_Pos)                    /**< (PAC_STATUSB) DSU APB Protect Enable Mask */
#define PAC_STATUSB_DSU(value)                (PAC_STATUSB_DSU_Msk & ((value) << PAC_STATUSB_DSU_Pos))
#define PAC_STATUSB_NVMCTRL_Pos               _U_(2)                                               /**< (PAC_STATUSB) NVMCTRL APB Protect Enable Position */
#define PAC_STATUSB_NVMCTRL_Msk               (_U_(0x1) << PAC_STATUSB_NVMCTRL_Pos)                /**< (PAC_STATUSB) NVMCTRL APB Protect Enable Mask */
#define PAC_STATUSB_NVMCTRL(value)            (PAC_STATUSB_NVMCTRL_Msk & ((value) << PAC_STATUSB_NVMCTRL_Pos))
#define PAC_STATUSB_DMAC_Pos                  _U_(3)                                               /**< (PAC_STATUSB) DMAC APB Protect Enable Position */
#define PAC_STATUSB_DMAC_Msk                  (_U_(0x1) << PAC_STATUSB_DMAC_Pos)                   /**< (PAC_STATUSB) DMAC APB Protect Enable Mask */
#define PAC_STATUSB_DMAC(value)               (PAC_STATUSB_DMAC_Msk & ((value) << PAC_STATUSB_DMAC_Pos))
#define PAC_STATUSB_Msk                       _U_(0x0000000F)                                      /**< (PAC_STATUSB) Register Mask  */


/* -------- PAC_STATUSC : (PAC Offset: 0x3C) ( R/ 32) Peripheral write protection status - Bridge C -------- */
#define PAC_STATUSC_RESETVALUE                _U_(0x00)                                            /**<  (PAC_STATUSC) Peripheral write protection status - Bridge C  Reset Value */

#define PAC_STATUSC_EVSYS_Pos                 _U_(0)                                               /**< (PAC_STATUSC) EVSYS APB Protect Enable Position */
#define PAC_STATUSC_EVSYS_Msk                 (_U_(0x1) << PAC_STATUSC_EVSYS_Pos)                  /**< (PAC_STATUSC) EVSYS APB Protect Enable Mask */
#define PAC_STATUSC_EVSYS(value)              (PAC_STATUSC_EVSYS_Msk & ((value) << PAC_STATUSC_EVSYS_Pos))
#define PAC_STATUSC_SERCOM0_Pos               _U_(1)                                               /**< (PAC_STATUSC) SERCOM0 APB Protect Enable Position */
#define PAC_STATUSC_SERCOM0_Msk               (_U_(0x1) << PAC_STATUSC_SERCOM0_Pos)                /**< (PAC_STATUSC) SERCOM0 APB Protect Enable Mask */
#define PAC_STATUSC_SERCOM0(value)            (PAC_STATUSC_SERCOM0_Msk & ((value) << PAC_STATUSC_SERCOM0_Pos))
#define PAC_STATUSC_SERCOM1_Pos               _U_(2)                                               /**< (PAC_STATUSC) SERCOM1 APB Protect Enable Position */
#define PAC_STATUSC_SERCOM1_Msk               (_U_(0x1) << PAC_STATUSC_SERCOM1_Pos)                /**< (PAC_STATUSC) SERCOM1 APB Protect Enable Mask */
#define PAC_STATUSC_SERCOM1(value)            (PAC_STATUSC_SERCOM1_Msk & ((value) << PAC_STATUSC_SERCOM1_Pos))
#define PAC_STATUSC_SERCOM2_Pos               _U_(3)                                               /**< (PAC_STATUSC) SERCOM2 APB Protect Enable Position */
#define PAC_STATUSC_SERCOM2_Msk               (_U_(0x1) << PAC_STATUSC_SERCOM2_Pos)                /**< (PAC_STATUSC) SERCOM2 APB Protect Enable Mask */
#define PAC_STATUSC_SERCOM2(value)            (PAC_STATUSC_SERCOM2_Msk & ((value) << PAC_STATUSC_SERCOM2_Pos))
#define PAC_STATUSC_TC0_Pos                   _U_(4)                                               /**< (PAC_STATUSC) TC0 APB Protect Enable Position */
#define PAC_STATUSC_TC0_Msk                   (_U_(0x1) << PAC_STATUSC_TC0_Pos)                    /**< (PAC_STATUSC) TC0 APB Protect Enable Mask */
#define PAC_STATUSC_TC0(value)                (PAC_STATUSC_TC0_Msk & ((value) << PAC_STATUSC_TC0_Pos))
#define PAC_STATUSC_TC1_Pos                   _U_(5)                                               /**< (PAC_STATUSC) TC1 APB Protect Enable Position */
#define PAC_STATUSC_TC1_Msk                   (_U_(0x1) << PAC_STATUSC_TC1_Pos)                    /**< (PAC_STATUSC) TC1 APB Protect Enable Mask */
#define PAC_STATUSC_TC1(value)                (PAC_STATUSC_TC1_Msk & ((value) << PAC_STATUSC_TC1_Pos))
#define PAC_STATUSC_TC2_Pos                   _U_(6)                                               /**< (PAC_STATUSC) TC2 APB Protect Enable Position */
#define PAC_STATUSC_TC2_Msk                   (_U_(0x1) << PAC_STATUSC_TC2_Pos)                    /**< (PAC_STATUSC) TC2 APB Protect Enable Mask */
#define PAC_STATUSC_TC2(value)                (PAC_STATUSC_TC2_Msk & ((value) << PAC_STATUSC_TC2_Pos))
#define PAC_STATUSC_ADC_Pos                   _U_(7)                                               /**< (PAC_STATUSC) ADC APB Protect Enable Position */
#define PAC_STATUSC_ADC_Msk                   (_U_(0x1) << PAC_STATUSC_ADC_Pos)                    /**< (PAC_STATUSC) ADC APB Protect Enable Mask */
#define PAC_STATUSC_ADC(value)                (PAC_STATUSC_ADC_Msk & ((value) << PAC_STATUSC_ADC_Pos))
#define PAC_STATUSC_DAC_Pos                   _U_(8)                                               /**< (PAC_STATUSC) DAC APB Protect Enable Position */
#define PAC_STATUSC_DAC_Msk                   (_U_(0x1) << PAC_STATUSC_DAC_Pos)                    /**< (PAC_STATUSC) DAC APB Protect Enable Mask */
#define PAC_STATUSC_DAC(value)                (PAC_STATUSC_DAC_Msk & ((value) << PAC_STATUSC_DAC_Pos))
#define PAC_STATUSC_PTC_Pos                   _U_(9)                                               /**< (PAC_STATUSC) PTC APB Protect Enable Position */
#define PAC_STATUSC_PTC_Msk                   (_U_(0x1) << PAC_STATUSC_PTC_Pos)                    /**< (PAC_STATUSC) PTC APB Protect Enable Mask */
#define PAC_STATUSC_PTC(value)                (PAC_STATUSC_PTC_Msk & ((value) << PAC_STATUSC_PTC_Pos))
#define PAC_STATUSC_TRNG_Pos                  _U_(10)                                              /**< (PAC_STATUSC) TRNG APB Protect Enable Position */
#define PAC_STATUSC_TRNG_Msk                  (_U_(0x1) << PAC_STATUSC_TRNG_Pos)                   /**< (PAC_STATUSC) TRNG APB Protect Enable Mask */
#define PAC_STATUSC_TRNG(value)               (PAC_STATUSC_TRNG_Msk & ((value) << PAC_STATUSC_TRNG_Pos))
#define PAC_STATUSC_CCL_Pos                   _U_(11)                                              /**< (PAC_STATUSC) CCL APB Protect Enable Position */
#define PAC_STATUSC_CCL_Msk                   (_U_(0x1) << PAC_STATUSC_CCL_Pos)                    /**< (PAC_STATUSC) CCL APB Protect Enable Mask */
#define PAC_STATUSC_CCL(value)                (PAC_STATUSC_CCL_Msk & ((value) << PAC_STATUSC_CCL_Pos))
#define PAC_STATUSC_OPAMP_Pos                 _U_(12)                                              /**< (PAC_STATUSC) OPAMP APB Protect Enable Position */
#define PAC_STATUSC_OPAMP_Msk                 (_U_(0x1) << PAC_STATUSC_OPAMP_Pos)                  /**< (PAC_STATUSC) OPAMP APB Protect Enable Mask */
#define PAC_STATUSC_OPAMP(value)              (PAC_STATUSC_OPAMP_Msk & ((value) << PAC_STATUSC_OPAMP_Pos))
#define PAC_STATUSC_TRAM_Pos                  _U_(13)                                              /**< (PAC_STATUSC) TRAM APB Protect Enable Position */
#define PAC_STATUSC_TRAM_Msk                  (_U_(0x1) << PAC_STATUSC_TRAM_Pos)                   /**< (PAC_STATUSC) TRAM APB Protect Enable Mask */
#define PAC_STATUSC_TRAM(value)               (PAC_STATUSC_TRAM_Msk & ((value) << PAC_STATUSC_TRAM_Pos))
#define PAC_STATUSC_Msk                       _U_(0x00003FFF)                                      /**< (PAC_STATUSC) Register Mask  */

#define PAC_STATUSC_SERCOM_Pos                _U_(1)                                               /**< (PAC_STATUSC Position) SERCOMx APB Protect Enable */
#define PAC_STATUSC_SERCOM_Msk                (_U_(0x7) << PAC_STATUSC_SERCOM_Pos)                 /**< (PAC_STATUSC Mask) SERCOM */
#define PAC_STATUSC_SERCOM(value)             (PAC_STATUSC_SERCOM_Msk & ((value) << PAC_STATUSC_SERCOM_Pos)) 
#define PAC_STATUSC_TC_Pos                    _U_(4)                                               /**< (PAC_STATUSC Position) TCx APB Protect Enable */
#define PAC_STATUSC_TC_Msk                    (_U_(0x7) << PAC_STATUSC_TC_Pos)                     /**< (PAC_STATUSC Mask) TC */
#define PAC_STATUSC_TC(value)                 (PAC_STATUSC_TC_Msk & ((value) << PAC_STATUSC_TC_Pos)) 

/* -------- PAC_NONSECA : (PAC Offset: 0x54) ( R/ 32) Peripheral non-secure status - Bridge A -------- */
#define PAC_NONSECA_RESETVALUE                _U_(0x00)                                            /**<  (PAC_NONSECA) Peripheral non-secure status - Bridge A  Reset Value */

#define PAC_NONSECA_PAC_Pos                   _U_(0)                                               /**< (PAC_NONSECA) PAC Non-Secure Position */
#define PAC_NONSECA_PAC_Msk                   (_U_(0x1) << PAC_NONSECA_PAC_Pos)                    /**< (PAC_NONSECA) PAC Non-Secure Mask */
#define PAC_NONSECA_PAC(value)                (PAC_NONSECA_PAC_Msk & ((value) << PAC_NONSECA_PAC_Pos))
#define PAC_NONSECA_PM_Pos                    _U_(1)                                               /**< (PAC_NONSECA) PM Non-Secure Position */
#define PAC_NONSECA_PM_Msk                    (_U_(0x1) << PAC_NONSECA_PM_Pos)                     /**< (PAC_NONSECA) PM Non-Secure Mask */
#define PAC_NONSECA_PM(value)                 (PAC_NONSECA_PM_Msk & ((value) << PAC_NONSECA_PM_Pos))
#define PAC_NONSECA_MCLK_Pos                  _U_(2)                                               /**< (PAC_NONSECA) MCLK Non-Secure Position */
#define PAC_NONSECA_MCLK_Msk                  (_U_(0x1) << PAC_NONSECA_MCLK_Pos)                   /**< (PAC_NONSECA) MCLK Non-Secure Mask */
#define PAC_NONSECA_MCLK(value)               (PAC_NONSECA_MCLK_Msk & ((value) << PAC_NONSECA_MCLK_Pos))
#define PAC_NONSECA_RSTC_Pos                  _U_(3)                                               /**< (PAC_NONSECA) RSTC Non-Secure Position */
#define PAC_NONSECA_RSTC_Msk                  (_U_(0x1) << PAC_NONSECA_RSTC_Pos)                   /**< (PAC_NONSECA) RSTC Non-Secure Mask */
#define PAC_NONSECA_RSTC(value)               (PAC_NONSECA_RSTC_Msk & ((value) << PAC_NONSECA_RSTC_Pos))
#define PAC_NONSECA_OSCCTRL_Pos               _U_(4)                                               /**< (PAC_NONSECA) OSCCTRL Non-Secure Position */
#define PAC_NONSECA_OSCCTRL_Msk               (_U_(0x1) << PAC_NONSECA_OSCCTRL_Pos)                /**< (PAC_NONSECA) OSCCTRL Non-Secure Mask */
#define PAC_NONSECA_OSCCTRL(value)            (PAC_NONSECA_OSCCTRL_Msk & ((value) << PAC_NONSECA_OSCCTRL_Pos))
#define PAC_NONSECA_OSC32KCTRL_Pos            _U_(5)                                               /**< (PAC_NONSECA) OSC32KCTRL Non-Secure Position */
#define PAC_NONSECA_OSC32KCTRL_Msk            (_U_(0x1) << PAC_NONSECA_OSC32KCTRL_Pos)             /**< (PAC_NONSECA) OSC32KCTRL Non-Secure Mask */
#define PAC_NONSECA_OSC32KCTRL(value)         (PAC_NONSECA_OSC32KCTRL_Msk & ((value) << PAC_NONSECA_OSC32KCTRL_Pos))
#define PAC_NONSECA_SUPC_Pos                  _U_(6)                                               /**< (PAC_NONSECA) SUPC Non-Secure Position */
#define PAC_NONSECA_SUPC_Msk                  (_U_(0x1) << PAC_NONSECA_SUPC_Pos)                   /**< (PAC_NONSECA) SUPC Non-Secure Mask */
#define PAC_NONSECA_SUPC(value)               (PAC_NONSECA_SUPC_Msk & ((value) << PAC_NONSECA_SUPC_Pos))
#define PAC_NONSECA_GCLK_Pos                  _U_(7)                                               /**< (PAC_NONSECA) GCLK Non-Secure Position */
#define PAC_NONSECA_GCLK_Msk                  (_U_(0x1) << PAC_NONSECA_GCLK_Pos)                   /**< (PAC_NONSECA) GCLK Non-Secure Mask */
#define PAC_NONSECA_GCLK(value)               (PAC_NONSECA_GCLK_Msk & ((value) << PAC_NONSECA_GCLK_Pos))
#define PAC_NONSECA_WDT_Pos                   _U_(8)                                               /**< (PAC_NONSECA) WDT Non-Secure Position */
#define PAC_NONSECA_WDT_Msk                   (_U_(0x1) << PAC_NONSECA_WDT_Pos)                    /**< (PAC_NONSECA) WDT Non-Secure Mask */
#define PAC_NONSECA_WDT(value)                (PAC_NONSECA_WDT_Msk & ((value) << PAC_NONSECA_WDT_Pos))
#define PAC_NONSECA_RTC_Pos                   _U_(9)                                               /**< (PAC_NONSECA) RTC Non-Secure Position */
#define PAC_NONSECA_RTC_Msk                   (_U_(0x1) << PAC_NONSECA_RTC_Pos)                    /**< (PAC_NONSECA) RTC Non-Secure Mask */
#define PAC_NONSECA_RTC(value)                (PAC_NONSECA_RTC_Msk & ((value) << PAC_NONSECA_RTC_Pos))
#define PAC_NONSECA_EIC_Pos                   _U_(10)                                              /**< (PAC_NONSECA) EIC Non-Secure Position */
#define PAC_NONSECA_EIC_Msk                   (_U_(0x1) << PAC_NONSECA_EIC_Pos)                    /**< (PAC_NONSECA) EIC Non-Secure Mask */
#define PAC_NONSECA_EIC(value)                (PAC_NONSECA_EIC_Msk & ((value) << PAC_NONSECA_EIC_Pos))
#define PAC_NONSECA_FREQM_Pos                 _U_(11)                                              /**< (PAC_NONSECA) FREQM Non-Secure Position */
#define PAC_NONSECA_FREQM_Msk                 (_U_(0x1) << PAC_NONSECA_FREQM_Pos)                  /**< (PAC_NONSECA) FREQM Non-Secure Mask */
#define PAC_NONSECA_FREQM(value)              (PAC_NONSECA_FREQM_Msk & ((value) << PAC_NONSECA_FREQM_Pos))
#define PAC_NONSECA_PORT_Pos                  _U_(12)                                              /**< (PAC_NONSECA) PORT Non-Secure Position */
#define PAC_NONSECA_PORT_Msk                  (_U_(0x1) << PAC_NONSECA_PORT_Pos)                   /**< (PAC_NONSECA) PORT Non-Secure Mask */
#define PAC_NONSECA_PORT(value)               (PAC_NONSECA_PORT_Msk & ((value) << PAC_NONSECA_PORT_Pos))
#define PAC_NONSECA_AC_Pos                    _U_(13)                                              /**< (PAC_NONSECA) AC Non-Secure Position */
#define PAC_NONSECA_AC_Msk                    (_U_(0x1) << PAC_NONSECA_AC_Pos)                     /**< (PAC_NONSECA) AC Non-Secure Mask */
#define PAC_NONSECA_AC(value)                 (PAC_NONSECA_AC_Msk & ((value) << PAC_NONSECA_AC_Pos))
#define PAC_NONSECA_Msk                       _U_(0x00003FFF)                                      /**< (PAC_NONSECA) Register Mask  */


/* -------- PAC_NONSECB : (PAC Offset: 0x58) ( R/ 32) Peripheral non-secure status - Bridge B -------- */
#define PAC_NONSECB_RESETVALUE                _U_(0x02)                                            /**<  (PAC_NONSECB) Peripheral non-secure status - Bridge B  Reset Value */

#define PAC_NONSECB_IDAU_Pos                  _U_(0)                                               /**< (PAC_NONSECB) IDAU Non-Secure Position */
#define PAC_NONSECB_IDAU_Msk                  (_U_(0x1) << PAC_NONSECB_IDAU_Pos)                   /**< (PAC_NONSECB) IDAU Non-Secure Mask */
#define PAC_NONSECB_IDAU(value)               (PAC_NONSECB_IDAU_Msk & ((value) << PAC_NONSECB_IDAU_Pos))
#define PAC_NONSECB_DSU_Pos                   _U_(1)                                               /**< (PAC_NONSECB) DSU Non-Secure Position */
#define PAC_NONSECB_DSU_Msk                   (_U_(0x1) << PAC_NONSECB_DSU_Pos)                    /**< (PAC_NONSECB) DSU Non-Secure Mask */
#define PAC_NONSECB_DSU(value)                (PAC_NONSECB_DSU_Msk & ((value) << PAC_NONSECB_DSU_Pos))
#define PAC_NONSECB_NVMCTRL_Pos               _U_(2)                                               /**< (PAC_NONSECB) NVMCTRL Non-Secure Position */
#define PAC_NONSECB_NVMCTRL_Msk               (_U_(0x1) << PAC_NONSECB_NVMCTRL_Pos)                /**< (PAC_NONSECB) NVMCTRL Non-Secure Mask */
#define PAC_NONSECB_NVMCTRL(value)            (PAC_NONSECB_NVMCTRL_Msk & ((value) << PAC_NONSECB_NVMCTRL_Pos))
#define PAC_NONSECB_DMAC_Pos                  _U_(3)                                               /**< (PAC_NONSECB) DMAC Non-Secure Position */
#define PAC_NONSECB_DMAC_Msk                  (_U_(0x1) << PAC_NONSECB_DMAC_Pos)                   /**< (PAC_NONSECB) DMAC Non-Secure Mask */
#define PAC_NONSECB_DMAC(value)               (PAC_NONSECB_DMAC_Msk & ((value) << PAC_NONSECB_DMAC_Pos))
#define PAC_NONSECB_Msk                       _U_(0x0000000F)                                      /**< (PAC_NONSECB) Register Mask  */


/* -------- PAC_NONSECC : (PAC Offset: 0x5C) ( R/ 32) Peripheral non-secure status - Bridge C -------- */
#define PAC_NONSECC_RESETVALUE                _U_(0x00)                                            /**<  (PAC_NONSECC) Peripheral non-secure status - Bridge C  Reset Value */

#define PAC_NONSECC_EVSYS_Pos                 _U_(0)                                               /**< (PAC_NONSECC) EVSYS Non-Secure Position */
#define PAC_NONSECC_EVSYS_Msk                 (_U_(0x1) << PAC_NONSECC_EVSYS_Pos)                  /**< (PAC_NONSECC) EVSYS Non-Secure Mask */
#define PAC_NONSECC_EVSYS(value)              (PAC_NONSECC_EVSYS_Msk & ((value) << PAC_NONSECC_EVSYS_Pos))
#define PAC_NONSECC_SERCOM0_Pos               _U_(1)                                               /**< (PAC_NONSECC) SERCOM0 Non-Secure Position */
#define PAC_NONSECC_SERCOM0_Msk               (_U_(0x1) << PAC_NONSECC_SERCOM0_Pos)                /**< (PAC_NONSECC) SERCOM0 Non-Secure Mask */
#define PAC_NONSECC_SERCOM0(value)            (PAC_NONSECC_SERCOM0_Msk & ((value) << PAC_NONSECC_SERCOM0_Pos))
#define PAC_NONSECC_SERCOM1_Pos               _U_(2)                                               /**< (PAC_NONSECC) SERCOM1 Non-Secure Position */
#define PAC_NONSECC_SERCOM1_Msk               (_U_(0x1) << PAC_NONSECC_SERCOM1_Pos)                /**< (PAC_NONSECC) SERCOM1 Non-Secure Mask */
#define PAC_NONSECC_SERCOM1(value)            (PAC_NONSECC_SERCOM1_Msk & ((value) << PAC_NONSECC_SERCOM1_Pos))
#define PAC_NONSECC_SERCOM2_Pos               _U_(3)                                               /**< (PAC_NONSECC) SERCOM2 Non-Secure Position */
#define PAC_NONSECC_SERCOM2_Msk               (_U_(0x1) << PAC_NONSECC_SERCOM2_Pos)                /**< (PAC_NONSECC) SERCOM2 Non-Secure Mask */
#define PAC_NONSECC_SERCOM2(value)            (PAC_NONSECC_SERCOM2_Msk & ((value) << PAC_NONSECC_SERCOM2_Pos))
#define PAC_NONSECC_TC0_Pos                   _U_(4)                                               /**< (PAC_NONSECC) TC0 Non-Secure Position */
#define PAC_NONSECC_TC0_Msk                   (_U_(0x1) << PAC_NONSECC_TC0_Pos)                    /**< (PAC_NONSECC) TC0 Non-Secure Mask */
#define PAC_NONSECC_TC0(value)                (PAC_NONSECC_TC0_Msk & ((value) << PAC_NONSECC_TC0_Pos))
#define PAC_NONSECC_TC1_Pos                   _U_(5)                                               /**< (PAC_NONSECC) TC1 Non-Secure Position */
#define PAC_NONSECC_TC1_Msk                   (_U_(0x1) << PAC_NONSECC_TC1_Pos)                    /**< (PAC_NONSECC) TC1 Non-Secure Mask */
#define PAC_NONSECC_TC1(value)                (PAC_NONSECC_TC1_Msk & ((value) << PAC_NONSECC_TC1_Pos))
#define PAC_NONSECC_TC2_Pos                   _U_(6)                                               /**< (PAC_NONSECC) TC2 Non-Secure Position */
#define PAC_NONSECC_TC2_Msk                   (_U_(0x1) << PAC_NONSECC_TC2_Pos)                    /**< (PAC_NONSECC) TC2 Non-Secure Mask */
#define PAC_NONSECC_TC2(value)                (PAC_NONSECC_TC2_Msk & ((value) << PAC_NONSECC_TC2_Pos))
#define PAC_NONSECC_ADC_Pos                   _U_(7)                                               /**< (PAC_NONSECC) ADC Non-Secure Position */
#define PAC_NONSECC_ADC_Msk                   (_U_(0x1) << PAC_NONSECC_ADC_Pos)                    /**< (PAC_NONSECC) ADC Non-Secure Mask */
#define PAC_NONSECC_ADC(value)                (PAC_NONSECC_ADC_Msk & ((value) << PAC_NONSECC_ADC_Pos))
#define PAC_NONSECC_DAC_Pos                   _U_(8)                                               /**< (PAC_NONSECC) DAC Non-Secure Position */
#define PAC_NONSECC_DAC_Msk                   (_U_(0x1) << PAC_NONSECC_DAC_Pos)                    /**< (PAC_NONSECC) DAC Non-Secure Mask */
#define PAC_NONSECC_DAC(value)                (PAC_NONSECC_DAC_Msk & ((value) << PAC_NONSECC_DAC_Pos))
#define PAC_NONSECC_PTC_Pos                   _U_(9)                                               /**< (PAC_NONSECC) PTC Non-Secure Position */
#define PAC_NONSECC_PTC_Msk                   (_U_(0x1) << PAC_NONSECC_PTC_Pos)                    /**< (PAC_NONSECC) PTC Non-Secure Mask */
#define PAC_NONSECC_PTC(value)                (PAC_NONSECC_PTC_Msk & ((value) << PAC_NONSECC_PTC_Pos))
#define PAC_NONSECC_TRNG_Pos                  _U_(10)                                              /**< (PAC_NONSECC) TRNG Non-Secure Position */
#define PAC_NONSECC_TRNG_Msk                  (_U_(0x1) << PAC_NONSECC_TRNG_Pos)                   /**< (PAC_NONSECC) TRNG Non-Secure Mask */
#define PAC_NONSECC_TRNG(value)               (PAC_NONSECC_TRNG_Msk & ((value) << PAC_NONSECC_TRNG_Pos))
#define PAC_NONSECC_CCL_Pos                   _U_(11)                                              /**< (PAC_NONSECC) CCL Non-Secure Position */
#define PAC_NONSECC_CCL_Msk                   (_U_(0x1) << PAC_NONSECC_CCL_Pos)                    /**< (PAC_NONSECC) CCL Non-Secure Mask */
#define PAC_NONSECC_CCL(value)                (PAC_NONSECC_CCL_Msk & ((value) << PAC_NONSECC_CCL_Pos))
#define PAC_NONSECC_OPAMP_Pos                 _U_(12)                                              /**< (PAC_NONSECC) OPAMP Non-Secure Position */
#define PAC_NONSECC_OPAMP_Msk                 (_U_(0x1) << PAC_NONSECC_OPAMP_Pos)                  /**< (PAC_NONSECC) OPAMP Non-Secure Mask */
#define PAC_NONSECC_OPAMP(value)              (PAC_NONSECC_OPAMP_Msk & ((value) << PAC_NONSECC_OPAMP_Pos))
#define PAC_NONSECC_TRAM_Pos                  _U_(13)                                              /**< (PAC_NONSECC) TRAM Non-Secure Position */
#define PAC_NONSECC_TRAM_Msk                  (_U_(0x1) << PAC_NONSECC_TRAM_Pos)                   /**< (PAC_NONSECC) TRAM Non-Secure Mask */
#define PAC_NONSECC_TRAM(value)               (PAC_NONSECC_TRAM_Msk & ((value) << PAC_NONSECC_TRAM_Pos))
#define PAC_NONSECC_Msk                       _U_(0x00003FFF)                                      /**< (PAC_NONSECC) Register Mask  */

#define PAC_NONSECC_SERCOM_Pos                _U_(1)                                               /**< (PAC_NONSECC Position) SERCOMx Non-Secure */
#define PAC_NONSECC_SERCOM_Msk                (_U_(0x7) << PAC_NONSECC_SERCOM_Pos)                 /**< (PAC_NONSECC Mask) SERCOM */
#define PAC_NONSECC_SERCOM(value)             (PAC_NONSECC_SERCOM_Msk & ((value) << PAC_NONSECC_SERCOM_Pos)) 
#define PAC_NONSECC_TC_Pos                    _U_(4)                                               /**< (PAC_NONSECC Position) TCx Non-Secure */
#define PAC_NONSECC_TC_Msk                    (_U_(0x7) << PAC_NONSECC_TC_Pos)                     /**< (PAC_NONSECC Mask) TC */
#define PAC_NONSECC_TC(value)                 (PAC_NONSECC_TC_Msk & ((value) << PAC_NONSECC_TC_Pos)) 

/** \brief PAC register offsets definitions */
#define PAC_WRCTRL_REG_OFST            (0x00)              /**< (PAC_WRCTRL) Write control Offset */
#define PAC_EVCTRL_REG_OFST            (0x04)              /**< (PAC_EVCTRL) Event control Offset */
#define PAC_INTENCLR_REG_OFST          (0x08)              /**< (PAC_INTENCLR) Interrupt enable clear Offset */
#define PAC_INTENSET_REG_OFST          (0x09)              /**< (PAC_INTENSET) Interrupt enable set Offset */
#define PAC_INTFLAGAHB_REG_OFST        (0x10)              /**< (PAC_INTFLAGAHB) Bridge interrupt flag status Offset */
#define PAC_INTFLAGA_REG_OFST          (0x14)              /**< (PAC_INTFLAGA) Peripheral interrupt flag status - Bridge A Offset */
#define PAC_INTFLAGB_REG_OFST          (0x18)              /**< (PAC_INTFLAGB) Peripheral interrupt flag status - Bridge B Offset */
#define PAC_INTFLAGC_REG_OFST          (0x1C)              /**< (PAC_INTFLAGC) Peripheral interrupt flag status - Bridge C Offset */
#define PAC_STATUSA_REG_OFST           (0x34)              /**< (PAC_STATUSA) Peripheral write protection status - Bridge A Offset */
#define PAC_STATUSB_REG_OFST           (0x38)              /**< (PAC_STATUSB) Peripheral write protection status - Bridge B Offset */
#define PAC_STATUSC_REG_OFST           (0x3C)              /**< (PAC_STATUSC) Peripheral write protection status - Bridge C Offset */
#define PAC_NONSECA_REG_OFST           (0x54)              /**< (PAC_NONSECA) Peripheral non-secure status - Bridge A Offset */
#define PAC_NONSECB_REG_OFST           (0x58)              /**< (PAC_NONSECB) Peripheral non-secure status - Bridge B Offset */
#define PAC_NONSECC_REG_OFST           (0x5C)              /**< (PAC_NONSECC) Peripheral non-secure status - Bridge C Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief PAC register API structure */
typedef struct
{  /* Peripheral Access Controller */
  __IO  uint32_t                       PAC_WRCTRL;         /**< Offset: 0x00 (R/W  32) Write control */
  __IO  uint8_t                        PAC_EVCTRL;         /**< Offset: 0x04 (R/W  8) Event control */
  __I   uint8_t                        Reserved1[0x03];
  __IO  uint8_t                        PAC_INTENCLR;       /**< Offset: 0x08 (R/W  8) Interrupt enable clear */
  __IO  uint8_t                        PAC_INTENSET;       /**< Offset: 0x09 (R/W  8) Interrupt enable set */
  __I   uint8_t                        Reserved2[0x06];
  __IO  uint32_t                       PAC_INTFLAGAHB;     /**< Offset: 0x10 (R/W  32) Bridge interrupt flag status */
  __IO  uint32_t                       PAC_INTFLAGA;       /**< Offset: 0x14 (R/W  32) Peripheral interrupt flag status - Bridge A */
  __IO  uint32_t                       PAC_INTFLAGB;       /**< Offset: 0x18 (R/W  32) Peripheral interrupt flag status - Bridge B */
  __IO  uint32_t                       PAC_INTFLAGC;       /**< Offset: 0x1C (R/W  32) Peripheral interrupt flag status - Bridge C */
  __I   uint8_t                        Reserved3[0x14];
  __I   uint32_t                       PAC_STATUSA;        /**< Offset: 0x34 (R/   32) Peripheral write protection status - Bridge A */
  __I   uint32_t                       PAC_STATUSB;        /**< Offset: 0x38 (R/   32) Peripheral write protection status - Bridge B */
  __I   uint32_t                       PAC_STATUSC;        /**< Offset: 0x3C (R/   32) Peripheral write protection status - Bridge C */
  __I   uint8_t                        Reserved4[0x14];
  __I   uint32_t                       PAC_NONSECA;        /**< Offset: 0x54 (R/   32) Peripheral non-secure status - Bridge A */
  __I   uint32_t                       PAC_NONSECB;        /**< Offset: 0x58 (R/   32) Peripheral non-secure status - Bridge B */
  __I   uint32_t                       PAC_NONSECC;        /**< Offset: 0x5C (R/   32) Peripheral non-secure status - Bridge C */
} pac_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAML10_PAC_COMPONENT_H_ */
