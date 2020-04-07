/**
 * \brief Component description for NVMCTRL
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
#ifndef _SAML10_NVMCTRL_COMPONENT_H_
#define _SAML10_NVMCTRL_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR NVMCTRL                                      */
/* ************************************************************************** */

/* -------- NVMCTRL_CTRLA : (NVMCTRL Offset: 0x00) ( /W 16) Control A -------- */
#define NVMCTRL_CTRLA_RESETVALUE              _U_(0x00)                                            /**<  (NVMCTRL_CTRLA) Control A  Reset Value */

#define NVMCTRL_CTRLA_CMD_Pos                 _U_(0)                                               /**< (NVMCTRL_CTRLA) Command Position */
#define NVMCTRL_CTRLA_CMD_Msk                 (_U_(0x7F) << NVMCTRL_CTRLA_CMD_Pos)                 /**< (NVMCTRL_CTRLA) Command Mask */
#define NVMCTRL_CTRLA_CMD(value)              (NVMCTRL_CTRLA_CMD_Msk & ((value) << NVMCTRL_CTRLA_CMD_Pos))
#define   NVMCTRL_CTRLA_CMD_ER_Val            _U_(0x2)                                             /**< (NVMCTRL_CTRLA) Erase Row - Erases the row addressed by the ADDR register.  */
#define   NVMCTRL_CTRLA_CMD_WP_Val            _U_(0x4)                                             /**< (NVMCTRL_CTRLA) Write Page - Writes the contents of the page buffer to the page addressed by the ADDR register.  */
#define   NVMCTRL_CTRLA_CMD_SPRM_Val          _U_(0x42)                                            /**< (NVMCTRL_CTRLA) Sets the power reduction mode.  */
#define   NVMCTRL_CTRLA_CMD_CPRM_Val          _U_(0x43)                                            /**< (NVMCTRL_CTRLA) Clears the power reduction mode.  */
#define   NVMCTRL_CTRLA_CMD_PBC_Val           _U_(0x44)                                            /**< (NVMCTRL_CTRLA) Page Buffer Clear - Clears the page buffer.  */
#define   NVMCTRL_CTRLA_CMD_INVALL_Val        _U_(0x46)                                            /**< (NVMCTRL_CTRLA) Invalidate all cache lines.  */
#define   NVMCTRL_CTRLA_CMD_SDAL0_Val         _U_(0x4B)                                            /**< (NVMCTRL_CTRLA) Set DAL=0  */
#define NVMCTRL_CTRLA_CMD_ER                  (NVMCTRL_CTRLA_CMD_ER_Val << NVMCTRL_CTRLA_CMD_Pos)  /**< (NVMCTRL_CTRLA) Erase Row - Erases the row addressed by the ADDR register. Position  */
#define NVMCTRL_CTRLA_CMD_WP                  (NVMCTRL_CTRLA_CMD_WP_Val << NVMCTRL_CTRLA_CMD_Pos)  /**< (NVMCTRL_CTRLA) Write Page - Writes the contents of the page buffer to the page addressed by the ADDR register. Position  */
#define NVMCTRL_CTRLA_CMD_SPRM                (NVMCTRL_CTRLA_CMD_SPRM_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Sets the power reduction mode. Position  */
#define NVMCTRL_CTRLA_CMD_CPRM                (NVMCTRL_CTRLA_CMD_CPRM_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Clears the power reduction mode. Position  */
#define NVMCTRL_CTRLA_CMD_PBC                 (NVMCTRL_CTRLA_CMD_PBC_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Page Buffer Clear - Clears the page buffer. Position  */
#define NVMCTRL_CTRLA_CMD_INVALL              (NVMCTRL_CTRLA_CMD_INVALL_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Invalidate all cache lines. Position  */
#define NVMCTRL_CTRLA_CMD_SDAL0               (NVMCTRL_CTRLA_CMD_SDAL0_Val << NVMCTRL_CTRLA_CMD_Pos) /**< (NVMCTRL_CTRLA) Set DAL=0 Position  */
#define NVMCTRL_CTRLA_CMDEX_Pos               _U_(8)                                               /**< (NVMCTRL_CTRLA) Command Execution Position */
#define NVMCTRL_CTRLA_CMDEX_Msk               (_U_(0xFF) << NVMCTRL_CTRLA_CMDEX_Pos)               /**< (NVMCTRL_CTRLA) Command Execution Mask */
#define NVMCTRL_CTRLA_CMDEX(value)            (NVMCTRL_CTRLA_CMDEX_Msk & ((value) << NVMCTRL_CTRLA_CMDEX_Pos))
#define   NVMCTRL_CTRLA_CMDEX_KEY_Val         _U_(0xA5)                                            /**< (NVMCTRL_CTRLA) Execution Key  */
#define NVMCTRL_CTRLA_CMDEX_KEY               (NVMCTRL_CTRLA_CMDEX_KEY_Val << NVMCTRL_CTRLA_CMDEX_Pos) /**< (NVMCTRL_CTRLA) Execution Key Position  */
#define NVMCTRL_CTRLA_Msk                     _U_(0xFF7F)                                          /**< (NVMCTRL_CTRLA) Register Mask  */


/* -------- NVMCTRL_CTRLB : (NVMCTRL Offset: 0x04) (R/W 32) Control B -------- */
#define NVMCTRL_CTRLB_RESETVALUE              _U_(0x00)                                            /**<  (NVMCTRL_CTRLB) Control B  Reset Value */

#define NVMCTRL_CTRLB_RWS_Pos                 _U_(1)                                               /**< (NVMCTRL_CTRLB) NVM Read Wait States Position */
#define NVMCTRL_CTRLB_RWS_Msk                 (_U_(0xF) << NVMCTRL_CTRLB_RWS_Pos)                  /**< (NVMCTRL_CTRLB) NVM Read Wait States Mask */
#define NVMCTRL_CTRLB_RWS(value)              (NVMCTRL_CTRLB_RWS_Msk & ((value) << NVMCTRL_CTRLB_RWS_Pos))
#define NVMCTRL_CTRLB_SLEEPPRM_Pos            _U_(8)                                               /**< (NVMCTRL_CTRLB) Power Reduction Mode during Sleep Position */
#define NVMCTRL_CTRLB_SLEEPPRM_Msk            (_U_(0x3) << NVMCTRL_CTRLB_SLEEPPRM_Pos)             /**< (NVMCTRL_CTRLB) Power Reduction Mode during Sleep Mask */
#define NVMCTRL_CTRLB_SLEEPPRM(value)         (NVMCTRL_CTRLB_SLEEPPRM_Msk & ((value) << NVMCTRL_CTRLB_SLEEPPRM_Pos))
#define   NVMCTRL_CTRLB_SLEEPPRM_WAKEONACCESS_Val _U_(0x0)                                             /**< (NVMCTRL_CTRLB) NVM block enters low-power mode when entering sleep.NVM block exits low-power mode upon first access.  */
#define   NVMCTRL_CTRLB_SLEEPPRM_WAKEUPINSTANT_Val _U_(0x1)                                             /**< (NVMCTRL_CTRLB) NVM block enters low-power mode when entering sleep.NVM block exits low-power mode when exiting sleep.  */
#define   NVMCTRL_CTRLB_SLEEPPRM_DISABLED_Val _U_(0x3)                                             /**< (NVMCTRL_CTRLB) Auto power reduction disabled.  */
#define NVMCTRL_CTRLB_SLEEPPRM_WAKEONACCESS   (NVMCTRL_CTRLB_SLEEPPRM_WAKEONACCESS_Val << NVMCTRL_CTRLB_SLEEPPRM_Pos) /**< (NVMCTRL_CTRLB) NVM block enters low-power mode when entering sleep.NVM block exits low-power mode upon first access. Position  */
#define NVMCTRL_CTRLB_SLEEPPRM_WAKEUPINSTANT  (NVMCTRL_CTRLB_SLEEPPRM_WAKEUPINSTANT_Val << NVMCTRL_CTRLB_SLEEPPRM_Pos) /**< (NVMCTRL_CTRLB) NVM block enters low-power mode when entering sleep.NVM block exits low-power mode when exiting sleep. Position  */
#define NVMCTRL_CTRLB_SLEEPPRM_DISABLED       (NVMCTRL_CTRLB_SLEEPPRM_DISABLED_Val << NVMCTRL_CTRLB_SLEEPPRM_Pos) /**< (NVMCTRL_CTRLB) Auto power reduction disabled. Position  */
#define NVMCTRL_CTRLB_FWUP_Pos                _U_(11)                                              /**< (NVMCTRL_CTRLB) fast wake-up Position */
#define NVMCTRL_CTRLB_FWUP_Msk                (_U_(0x1) << NVMCTRL_CTRLB_FWUP_Pos)                 /**< (NVMCTRL_CTRLB) fast wake-up Mask */
#define NVMCTRL_CTRLB_FWUP(value)             (NVMCTRL_CTRLB_FWUP_Msk & ((value) << NVMCTRL_CTRLB_FWUP_Pos))
#define NVMCTRL_CTRLB_READMODE_Pos            _U_(16)                                              /**< (NVMCTRL_CTRLB) NVMCTRL Read Mode Position */
#define NVMCTRL_CTRLB_READMODE_Msk            (_U_(0x3) << NVMCTRL_CTRLB_READMODE_Pos)             /**< (NVMCTRL_CTRLB) NVMCTRL Read Mode Mask */
#define NVMCTRL_CTRLB_READMODE(value)         (NVMCTRL_CTRLB_READMODE_Msk & ((value) << NVMCTRL_CTRLB_READMODE_Pos))
#define   NVMCTRL_CTRLB_READMODE_NO_MISS_PENALTY_Val _U_(0x0)                                             /**< (NVMCTRL_CTRLB) The NVM Controller (cache system) does not insert wait states on a cache miss. Gives the best system performance.  */
#define   NVMCTRL_CTRLB_READMODE_LOW_POWER_Val _U_(0x1)                                             /**< (NVMCTRL_CTRLB) Reduces power consumption of the cache system, but inserts a wait state each time there is a cache miss. This mode may not be relevant if CPU performance is required, as the application will be stalled and may lead to increase run time.  */
#define   NVMCTRL_CTRLB_READMODE_DETERMINISTIC_Val _U_(0x2)                                             /**< (NVMCTRL_CTRLB) The cache system ensures that a cache hit or miss takes the same amount of time, determined by the number of programmed flash wait states. This mode can be used for real-time applications that require deterministic execution timings.  */
#define NVMCTRL_CTRLB_READMODE_NO_MISS_PENALTY (NVMCTRL_CTRLB_READMODE_NO_MISS_PENALTY_Val << NVMCTRL_CTRLB_READMODE_Pos) /**< (NVMCTRL_CTRLB) The NVM Controller (cache system) does not insert wait states on a cache miss. Gives the best system performance. Position  */
#define NVMCTRL_CTRLB_READMODE_LOW_POWER      (NVMCTRL_CTRLB_READMODE_LOW_POWER_Val << NVMCTRL_CTRLB_READMODE_Pos) /**< (NVMCTRL_CTRLB) Reduces power consumption of the cache system, but inserts a wait state each time there is a cache miss. This mode may not be relevant if CPU performance is required, as the application will be stalled and may lead to increase run time. Position  */
#define NVMCTRL_CTRLB_READMODE_DETERMINISTIC  (NVMCTRL_CTRLB_READMODE_DETERMINISTIC_Val << NVMCTRL_CTRLB_READMODE_Pos) /**< (NVMCTRL_CTRLB) The cache system ensures that a cache hit or miss takes the same amount of time, determined by the number of programmed flash wait states. This mode can be used for real-time applications that require deterministic execution timings. Position  */
#define NVMCTRL_CTRLB_CACHEDIS_Pos            _U_(18)                                              /**< (NVMCTRL_CTRLB) Cache Disable Position */
#define NVMCTRL_CTRLB_CACHEDIS_Msk            (_U_(0x1) << NVMCTRL_CTRLB_CACHEDIS_Pos)             /**< (NVMCTRL_CTRLB) Cache Disable Mask */
#define NVMCTRL_CTRLB_CACHEDIS(value)         (NVMCTRL_CTRLB_CACHEDIS_Msk & ((value) << NVMCTRL_CTRLB_CACHEDIS_Pos))
#define NVMCTRL_CTRLB_Msk                     _U_(0x00070B1E)                                      /**< (NVMCTRL_CTRLB) Register Mask  */


/* -------- NVMCTRL_CTRLC : (NVMCTRL Offset: 0x08) (R/W 8) Control C -------- */
#define NVMCTRL_CTRLC_RESETVALUE              _U_(0x01)                                            /**<  (NVMCTRL_CTRLC) Control C  Reset Value */

#define NVMCTRL_CTRLC_MANW_Pos                _U_(0)                                               /**< (NVMCTRL_CTRLC) Manual Write Position */
#define NVMCTRL_CTRLC_MANW_Msk                (_U_(0x1) << NVMCTRL_CTRLC_MANW_Pos)                 /**< (NVMCTRL_CTRLC) Manual Write Mask */
#define NVMCTRL_CTRLC_MANW(value)             (NVMCTRL_CTRLC_MANW_Msk & ((value) << NVMCTRL_CTRLC_MANW_Pos))
#define NVMCTRL_CTRLC_Msk                     _U_(0x01)                                            /**< (NVMCTRL_CTRLC) Register Mask  */


/* -------- NVMCTRL_EVCTRL : (NVMCTRL Offset: 0x0A) (R/W 8) Event Control -------- */
#define NVMCTRL_EVCTRL_RESETVALUE             _U_(0x00)                                            /**<  (NVMCTRL_EVCTRL) Event Control  Reset Value */

#define NVMCTRL_EVCTRL_AUTOWEI_Pos            _U_(0)                                               /**< (NVMCTRL_EVCTRL) Auto Write Event Enable Position */
#define NVMCTRL_EVCTRL_AUTOWEI_Msk            (_U_(0x1) << NVMCTRL_EVCTRL_AUTOWEI_Pos)             /**< (NVMCTRL_EVCTRL) Auto Write Event Enable Mask */
#define NVMCTRL_EVCTRL_AUTOWEI(value)         (NVMCTRL_EVCTRL_AUTOWEI_Msk & ((value) << NVMCTRL_EVCTRL_AUTOWEI_Pos))
#define NVMCTRL_EVCTRL_AUTOWINV_Pos           _U_(1)                                               /**< (NVMCTRL_EVCTRL) Auto Write Event Polarity Inverted Position */
#define NVMCTRL_EVCTRL_AUTOWINV_Msk           (_U_(0x1) << NVMCTRL_EVCTRL_AUTOWINV_Pos)            /**< (NVMCTRL_EVCTRL) Auto Write Event Polarity Inverted Mask */
#define NVMCTRL_EVCTRL_AUTOWINV(value)        (NVMCTRL_EVCTRL_AUTOWINV_Msk & ((value) << NVMCTRL_EVCTRL_AUTOWINV_Pos))
#define NVMCTRL_EVCTRL_Msk                    _U_(0x03)                                            /**< (NVMCTRL_EVCTRL) Register Mask  */


/* -------- NVMCTRL_INTENCLR : (NVMCTRL Offset: 0x0C) (R/W 8) Interrupt Enable Clear -------- */
#define NVMCTRL_INTENCLR_RESETVALUE           _U_(0x00)                                            /**<  (NVMCTRL_INTENCLR) Interrupt Enable Clear  Reset Value */

#define NVMCTRL_INTENCLR_DONE_Pos             _U_(0)                                               /**< (NVMCTRL_INTENCLR) NVM Done Interrupt Clear Position */
#define NVMCTRL_INTENCLR_DONE_Msk             (_U_(0x1) << NVMCTRL_INTENCLR_DONE_Pos)              /**< (NVMCTRL_INTENCLR) NVM Done Interrupt Clear Mask */
#define NVMCTRL_INTENCLR_DONE(value)          (NVMCTRL_INTENCLR_DONE_Msk & ((value) << NVMCTRL_INTENCLR_DONE_Pos))
#define NVMCTRL_INTENCLR_PROGE_Pos            _U_(1)                                               /**< (NVMCTRL_INTENCLR) Programming Error Status Interrupt Clear Position */
#define NVMCTRL_INTENCLR_PROGE_Msk            (_U_(0x1) << NVMCTRL_INTENCLR_PROGE_Pos)             /**< (NVMCTRL_INTENCLR) Programming Error Status Interrupt Clear Mask */
#define NVMCTRL_INTENCLR_PROGE(value)         (NVMCTRL_INTENCLR_PROGE_Msk & ((value) << NVMCTRL_INTENCLR_PROGE_Pos))
#define NVMCTRL_INTENCLR_LOCKE_Pos            _U_(2)                                               /**< (NVMCTRL_INTENCLR) Lock Error Status Interrupt Clear Position */
#define NVMCTRL_INTENCLR_LOCKE_Msk            (_U_(0x1) << NVMCTRL_INTENCLR_LOCKE_Pos)             /**< (NVMCTRL_INTENCLR) Lock Error Status Interrupt Clear Mask */
#define NVMCTRL_INTENCLR_LOCKE(value)         (NVMCTRL_INTENCLR_LOCKE_Msk & ((value) << NVMCTRL_INTENCLR_LOCKE_Pos))
#define NVMCTRL_INTENCLR_NVME_Pos             _U_(3)                                               /**< (NVMCTRL_INTENCLR) NVM Error Interrupt Clear Position */
#define NVMCTRL_INTENCLR_NVME_Msk             (_U_(0x1) << NVMCTRL_INTENCLR_NVME_Pos)              /**< (NVMCTRL_INTENCLR) NVM Error Interrupt Clear Mask */
#define NVMCTRL_INTENCLR_NVME(value)          (NVMCTRL_INTENCLR_NVME_Msk & ((value) << NVMCTRL_INTENCLR_NVME_Pos))
#define NVMCTRL_INTENCLR_KEYE_Pos             _U_(4)                                               /**< (NVMCTRL_INTENCLR) Key Write Error Interrupt Clear Position */
#define NVMCTRL_INTENCLR_KEYE_Msk             (_U_(0x1) << NVMCTRL_INTENCLR_KEYE_Pos)              /**< (NVMCTRL_INTENCLR) Key Write Error Interrupt Clear Mask */
#define NVMCTRL_INTENCLR_KEYE(value)          (NVMCTRL_INTENCLR_KEYE_Msk & ((value) << NVMCTRL_INTENCLR_KEYE_Pos))
#define NVMCTRL_INTENCLR_NSCHK_Pos            _U_(5)                                               /**< (NVMCTRL_INTENCLR) NS configuration change detected Interrupt Clear Position */
#define NVMCTRL_INTENCLR_NSCHK_Msk            (_U_(0x1) << NVMCTRL_INTENCLR_NSCHK_Pos)             /**< (NVMCTRL_INTENCLR) NS configuration change detected Interrupt Clear Mask */
#define NVMCTRL_INTENCLR_NSCHK(value)         (NVMCTRL_INTENCLR_NSCHK_Msk & ((value) << NVMCTRL_INTENCLR_NSCHK_Pos))
#define NVMCTRL_INTENCLR_Msk                  _U_(0x3F)                                            /**< (NVMCTRL_INTENCLR) Register Mask  */


/* -------- NVMCTRL_INTENSET : (NVMCTRL Offset: 0x10) (R/W 8) Interrupt Enable Set -------- */
#define NVMCTRL_INTENSET_RESETVALUE           _U_(0x00)                                            /**<  (NVMCTRL_INTENSET) Interrupt Enable Set  Reset Value */

#define NVMCTRL_INTENSET_DONE_Pos             _U_(0)                                               /**< (NVMCTRL_INTENSET) NVM Done Interrupt Enable Position */
#define NVMCTRL_INTENSET_DONE_Msk             (_U_(0x1) << NVMCTRL_INTENSET_DONE_Pos)              /**< (NVMCTRL_INTENSET) NVM Done Interrupt Enable Mask */
#define NVMCTRL_INTENSET_DONE(value)          (NVMCTRL_INTENSET_DONE_Msk & ((value) << NVMCTRL_INTENSET_DONE_Pos))
#define NVMCTRL_INTENSET_PROGE_Pos            _U_(1)                                               /**< (NVMCTRL_INTENSET) Programming Error Status Interrupt Enable Position */
#define NVMCTRL_INTENSET_PROGE_Msk            (_U_(0x1) << NVMCTRL_INTENSET_PROGE_Pos)             /**< (NVMCTRL_INTENSET) Programming Error Status Interrupt Enable Mask */
#define NVMCTRL_INTENSET_PROGE(value)         (NVMCTRL_INTENSET_PROGE_Msk & ((value) << NVMCTRL_INTENSET_PROGE_Pos))
#define NVMCTRL_INTENSET_LOCKE_Pos            _U_(2)                                               /**< (NVMCTRL_INTENSET) Lock Error Status Interrupt Enable Position */
#define NVMCTRL_INTENSET_LOCKE_Msk            (_U_(0x1) << NVMCTRL_INTENSET_LOCKE_Pos)             /**< (NVMCTRL_INTENSET) Lock Error Status Interrupt Enable Mask */
#define NVMCTRL_INTENSET_LOCKE(value)         (NVMCTRL_INTENSET_LOCKE_Msk & ((value) << NVMCTRL_INTENSET_LOCKE_Pos))
#define NVMCTRL_INTENSET_NVME_Pos             _U_(3)                                               /**< (NVMCTRL_INTENSET) NVM Error Interrupt Enable Position */
#define NVMCTRL_INTENSET_NVME_Msk             (_U_(0x1) << NVMCTRL_INTENSET_NVME_Pos)              /**< (NVMCTRL_INTENSET) NVM Error Interrupt Enable Mask */
#define NVMCTRL_INTENSET_NVME(value)          (NVMCTRL_INTENSET_NVME_Msk & ((value) << NVMCTRL_INTENSET_NVME_Pos))
#define NVMCTRL_INTENSET_KEYE_Pos             _U_(4)                                               /**< (NVMCTRL_INTENSET) Key Write Error Interrupt Enable Position */
#define NVMCTRL_INTENSET_KEYE_Msk             (_U_(0x1) << NVMCTRL_INTENSET_KEYE_Pos)              /**< (NVMCTRL_INTENSET) Key Write Error Interrupt Enable Mask */
#define NVMCTRL_INTENSET_KEYE(value)          (NVMCTRL_INTENSET_KEYE_Msk & ((value) << NVMCTRL_INTENSET_KEYE_Pos))
#define NVMCTRL_INTENSET_NSCHK_Pos            _U_(5)                                               /**< (NVMCTRL_INTENSET) NS configuration change detected Interrupt Enable Position */
#define NVMCTRL_INTENSET_NSCHK_Msk            (_U_(0x1) << NVMCTRL_INTENSET_NSCHK_Pos)             /**< (NVMCTRL_INTENSET) NS configuration change detected Interrupt Enable Mask */
#define NVMCTRL_INTENSET_NSCHK(value)         (NVMCTRL_INTENSET_NSCHK_Msk & ((value) << NVMCTRL_INTENSET_NSCHK_Pos))
#define NVMCTRL_INTENSET_Msk                  _U_(0x3F)                                            /**< (NVMCTRL_INTENSET) Register Mask  */


/* -------- NVMCTRL_INTFLAG : (NVMCTRL Offset: 0x14) (R/W 8) Interrupt Flag Status and Clear -------- */
#define NVMCTRL_INTFLAG_RESETVALUE            _U_(0x00)                                            /**<  (NVMCTRL_INTFLAG) Interrupt Flag Status and Clear  Reset Value */

#define NVMCTRL_INTFLAG_DONE_Pos              _U_(0)                                               /**< (NVMCTRL_INTFLAG) NVM Done Position */
#define NVMCTRL_INTFLAG_DONE_Msk              (_U_(0x1) << NVMCTRL_INTFLAG_DONE_Pos)               /**< (NVMCTRL_INTFLAG) NVM Done Mask */
#define NVMCTRL_INTFLAG_DONE(value)           (NVMCTRL_INTFLAG_DONE_Msk & ((value) << NVMCTRL_INTFLAG_DONE_Pos))
#define NVMCTRL_INTFLAG_PROGE_Pos             _U_(1)                                               /**< (NVMCTRL_INTFLAG) Programming Error Status Position */
#define NVMCTRL_INTFLAG_PROGE_Msk             (_U_(0x1) << NVMCTRL_INTFLAG_PROGE_Pos)              /**< (NVMCTRL_INTFLAG) Programming Error Status Mask */
#define NVMCTRL_INTFLAG_PROGE(value)          (NVMCTRL_INTFLAG_PROGE_Msk & ((value) << NVMCTRL_INTFLAG_PROGE_Pos))
#define NVMCTRL_INTFLAG_LOCKE_Pos             _U_(2)                                               /**< (NVMCTRL_INTFLAG) Lock Error Status Position */
#define NVMCTRL_INTFLAG_LOCKE_Msk             (_U_(0x1) << NVMCTRL_INTFLAG_LOCKE_Pos)              /**< (NVMCTRL_INTFLAG) Lock Error Status Mask */
#define NVMCTRL_INTFLAG_LOCKE(value)          (NVMCTRL_INTFLAG_LOCKE_Msk & ((value) << NVMCTRL_INTFLAG_LOCKE_Pos))
#define NVMCTRL_INTFLAG_NVME_Pos              _U_(3)                                               /**< (NVMCTRL_INTFLAG) NVM Error Position */
#define NVMCTRL_INTFLAG_NVME_Msk              (_U_(0x1) << NVMCTRL_INTFLAG_NVME_Pos)               /**< (NVMCTRL_INTFLAG) NVM Error Mask */
#define NVMCTRL_INTFLAG_NVME(value)           (NVMCTRL_INTFLAG_NVME_Msk & ((value) << NVMCTRL_INTFLAG_NVME_Pos))
#define NVMCTRL_INTFLAG_KEYE_Pos              _U_(4)                                               /**< (NVMCTRL_INTFLAG) KEY Write Error Position */
#define NVMCTRL_INTFLAG_KEYE_Msk              (_U_(0x1) << NVMCTRL_INTFLAG_KEYE_Pos)               /**< (NVMCTRL_INTFLAG) KEY Write Error Mask */
#define NVMCTRL_INTFLAG_KEYE(value)           (NVMCTRL_INTFLAG_KEYE_Msk & ((value) << NVMCTRL_INTFLAG_KEYE_Pos))
#define NVMCTRL_INTFLAG_NSCHK_Pos             _U_(5)                                               /**< (NVMCTRL_INTFLAG) NS configuration change detected Position */
#define NVMCTRL_INTFLAG_NSCHK_Msk             (_U_(0x1) << NVMCTRL_INTFLAG_NSCHK_Pos)              /**< (NVMCTRL_INTFLAG) NS configuration change detected Mask */
#define NVMCTRL_INTFLAG_NSCHK(value)          (NVMCTRL_INTFLAG_NSCHK_Msk & ((value) << NVMCTRL_INTFLAG_NSCHK_Pos))
#define NVMCTRL_INTFLAG_Msk                   _U_(0x3F)                                            /**< (NVMCTRL_INTFLAG) Register Mask  */


/* -------- NVMCTRL_STATUS : (NVMCTRL Offset: 0x18) ( R/ 16) Status -------- */
#define NVMCTRL_STATUS_RESETVALUE             _U_(0x00)                                            /**<  (NVMCTRL_STATUS) Status  Reset Value */

#define NVMCTRL_STATUS_PRM_Pos                _U_(0)                                               /**< (NVMCTRL_STATUS) Power Reduction Mode Position */
#define NVMCTRL_STATUS_PRM_Msk                (_U_(0x1) << NVMCTRL_STATUS_PRM_Pos)                 /**< (NVMCTRL_STATUS) Power Reduction Mode Mask */
#define NVMCTRL_STATUS_PRM(value)             (NVMCTRL_STATUS_PRM_Msk & ((value) << NVMCTRL_STATUS_PRM_Pos))
#define NVMCTRL_STATUS_LOAD_Pos               _U_(1)                                               /**< (NVMCTRL_STATUS) NVM Page Buffer Active Loading Position */
#define NVMCTRL_STATUS_LOAD_Msk               (_U_(0x1) << NVMCTRL_STATUS_LOAD_Pos)                /**< (NVMCTRL_STATUS) NVM Page Buffer Active Loading Mask */
#define NVMCTRL_STATUS_LOAD(value)            (NVMCTRL_STATUS_LOAD_Msk & ((value) << NVMCTRL_STATUS_LOAD_Pos))
#define NVMCTRL_STATUS_READY_Pos              _U_(2)                                               /**< (NVMCTRL_STATUS) NVM Ready Position */
#define NVMCTRL_STATUS_READY_Msk              (_U_(0x1) << NVMCTRL_STATUS_READY_Pos)               /**< (NVMCTRL_STATUS) NVM Ready Mask */
#define NVMCTRL_STATUS_READY(value)           (NVMCTRL_STATUS_READY_Msk & ((value) << NVMCTRL_STATUS_READY_Pos))
#define NVMCTRL_STATUS_DALFUSE_Pos            _U_(3)                                               /**< (NVMCTRL_STATUS) Debug Access Level Fuse Position */
#define NVMCTRL_STATUS_DALFUSE_Msk            (_U_(0x3) << NVMCTRL_STATUS_DALFUSE_Pos)             /**< (NVMCTRL_STATUS) Debug Access Level Fuse Mask */
#define NVMCTRL_STATUS_DALFUSE(value)         (NVMCTRL_STATUS_DALFUSE_Msk & ((value) << NVMCTRL_STATUS_DALFUSE_Pos))
#define   NVMCTRL_STATUS_DALFUSE_DAL0_Val     _U_(0x0)                                             /**< (NVMCTRL_STATUS) NO DEBUG  */
#define   NVMCTRL_STATUS_DALFUSE_DAL2_Val     _U_(0x2)                                             /**< (NVMCTRL_STATUS) FULL DEBUG  */
#define NVMCTRL_STATUS_DALFUSE_DAL0           (NVMCTRL_STATUS_DALFUSE_DAL0_Val << NVMCTRL_STATUS_DALFUSE_Pos) /**< (NVMCTRL_STATUS) NO DEBUG Position  */
#define NVMCTRL_STATUS_DALFUSE_DAL2           (NVMCTRL_STATUS_DALFUSE_DAL2_Val << NVMCTRL_STATUS_DALFUSE_Pos) /**< (NVMCTRL_STATUS) FULL DEBUG Position  */
#define NVMCTRL_STATUS_Msk                    _U_(0x001F)                                          /**< (NVMCTRL_STATUS) Register Mask  */


/* -------- NVMCTRL_ADDR : (NVMCTRL Offset: 0x1C) (R/W 32) Address -------- */
#define NVMCTRL_ADDR_RESETVALUE               _U_(0x00)                                            /**<  (NVMCTRL_ADDR) Address  Reset Value */

#define NVMCTRL_ADDR_AOFFSET_Pos              _U_(0)                                               /**< (NVMCTRL_ADDR) NVM Address Offset In The Selected Array Position */
#define NVMCTRL_ADDR_AOFFSET_Msk              (_U_(0xFFFF) << NVMCTRL_ADDR_AOFFSET_Pos)            /**< (NVMCTRL_ADDR) NVM Address Offset In The Selected Array Mask */
#define NVMCTRL_ADDR_AOFFSET(value)           (NVMCTRL_ADDR_AOFFSET_Msk & ((value) << NVMCTRL_ADDR_AOFFSET_Pos))
#define NVMCTRL_ADDR_ARRAY_Pos                _U_(22)                                              /**< (NVMCTRL_ADDR) Array Select Position */
#define NVMCTRL_ADDR_ARRAY_Msk                (_U_(0x3) << NVMCTRL_ADDR_ARRAY_Pos)                 /**< (NVMCTRL_ADDR) Array Select Mask */
#define NVMCTRL_ADDR_ARRAY(value)             (NVMCTRL_ADDR_ARRAY_Msk & ((value) << NVMCTRL_ADDR_ARRAY_Pos))
#define   NVMCTRL_ADDR_ARRAY_FLASH_Val        _U_(0x0)                                             /**< (NVMCTRL_ADDR) FLASH Array  */
#define   NVMCTRL_ADDR_ARRAY_DATAFLASH_Val    _U_(0x1)                                             /**< (NVMCTRL_ADDR) DATA FLASH Array  */
#define   NVMCTRL_ADDR_ARRAY_NVMROWS_Val      _U_(0x2)                                             /**< (NVMCTRL_ADDR) NVM Rows  */
#define NVMCTRL_ADDR_ARRAY_FLASH              (NVMCTRL_ADDR_ARRAY_FLASH_Val << NVMCTRL_ADDR_ARRAY_Pos) /**< (NVMCTRL_ADDR) FLASH Array Position  */
#define NVMCTRL_ADDR_ARRAY_DATAFLASH          (NVMCTRL_ADDR_ARRAY_DATAFLASH_Val << NVMCTRL_ADDR_ARRAY_Pos) /**< (NVMCTRL_ADDR) DATA FLASH Array Position  */
#define NVMCTRL_ADDR_ARRAY_NVMROWS            (NVMCTRL_ADDR_ARRAY_NVMROWS_Val << NVMCTRL_ADDR_ARRAY_Pos) /**< (NVMCTRL_ADDR) NVM Rows Position  */
#define NVMCTRL_ADDR_Msk                      _U_(0x00C0FFFF)                                      /**< (NVMCTRL_ADDR) Register Mask  */


/* -------- NVMCTRL_SULCK : (NVMCTRL Offset: 0x20) (R/W 16) Secure Unlock Register -------- */
#define NVMCTRL_SULCK_BS_Pos                  _U_(0)                                               /**< (NVMCTRL_SULCK) Secure Boot Region Position */
#define NVMCTRL_SULCK_BS_Msk                  (_U_(0x1) << NVMCTRL_SULCK_BS_Pos)                   /**< (NVMCTRL_SULCK) Secure Boot Region Mask */
#define NVMCTRL_SULCK_BS(value)               (NVMCTRL_SULCK_BS_Msk & ((value) << NVMCTRL_SULCK_BS_Pos))
#define NVMCTRL_SULCK_AS_Pos                  _U_(1)                                               /**< (NVMCTRL_SULCK) Secure Application Region Position */
#define NVMCTRL_SULCK_AS_Msk                  (_U_(0x1) << NVMCTRL_SULCK_AS_Pos)                   /**< (NVMCTRL_SULCK) Secure Application Region Mask */
#define NVMCTRL_SULCK_AS(value)               (NVMCTRL_SULCK_AS_Msk & ((value) << NVMCTRL_SULCK_AS_Pos))
#define NVMCTRL_SULCK_DS_Pos                  _U_(2)                                               /**< (NVMCTRL_SULCK) Data Secure Region Position */
#define NVMCTRL_SULCK_DS_Msk                  (_U_(0x1) << NVMCTRL_SULCK_DS_Pos)                   /**< (NVMCTRL_SULCK) Data Secure Region Mask */
#define NVMCTRL_SULCK_DS(value)               (NVMCTRL_SULCK_DS_Msk & ((value) << NVMCTRL_SULCK_DS_Pos))
#define NVMCTRL_SULCK_SLKEY_Pos               _U_(8)                                               /**< (NVMCTRL_SULCK) Write Key Position */
#define NVMCTRL_SULCK_SLKEY_Msk               (_U_(0xFF) << NVMCTRL_SULCK_SLKEY_Pos)               /**< (NVMCTRL_SULCK) Write Key Mask */
#define NVMCTRL_SULCK_SLKEY(value)            (NVMCTRL_SULCK_SLKEY_Msk & ((value) << NVMCTRL_SULCK_SLKEY_Pos))
#define   NVMCTRL_SULCK_SLKEY_KEY_Val         _U_(0xA5)                                            /**< (NVMCTRL_SULCK) Write Key  */
#define NVMCTRL_SULCK_SLKEY_KEY               (NVMCTRL_SULCK_SLKEY_KEY_Val << NVMCTRL_SULCK_SLKEY_Pos) /**< (NVMCTRL_SULCK) Write Key Position  */
#define NVMCTRL_SULCK_Msk                     _U_(0xFF07)                                          /**< (NVMCTRL_SULCK) Register Mask  */


/* -------- NVMCTRL_NSULCK : (NVMCTRL Offset: 0x22) (R/W 16) Non-Secure Unlock Register -------- */
#define NVMCTRL_NSULCK_BNS_Pos                _U_(0)                                               /**< (NVMCTRL_NSULCK) Non-Secure Boot Region Position */
#define NVMCTRL_NSULCK_BNS_Msk                (_U_(0x1) << NVMCTRL_NSULCK_BNS_Pos)                 /**< (NVMCTRL_NSULCK) Non-Secure Boot Region Mask */
#define NVMCTRL_NSULCK_BNS(value)             (NVMCTRL_NSULCK_BNS_Msk & ((value) << NVMCTRL_NSULCK_BNS_Pos))
#define NVMCTRL_NSULCK_ANS_Pos                _U_(1)                                               /**< (NVMCTRL_NSULCK) Non-Secure Application Region Position */
#define NVMCTRL_NSULCK_ANS_Msk                (_U_(0x1) << NVMCTRL_NSULCK_ANS_Pos)                 /**< (NVMCTRL_NSULCK) Non-Secure Application Region Mask */
#define NVMCTRL_NSULCK_ANS(value)             (NVMCTRL_NSULCK_ANS_Msk & ((value) << NVMCTRL_NSULCK_ANS_Pos))
#define NVMCTRL_NSULCK_DNS_Pos                _U_(2)                                               /**< (NVMCTRL_NSULCK) Non-Secure Data Region Position */
#define NVMCTRL_NSULCK_DNS_Msk                (_U_(0x1) << NVMCTRL_NSULCK_DNS_Pos)                 /**< (NVMCTRL_NSULCK) Non-Secure Data Region Mask */
#define NVMCTRL_NSULCK_DNS(value)             (NVMCTRL_NSULCK_DNS_Msk & ((value) << NVMCTRL_NSULCK_DNS_Pos))
#define NVMCTRL_NSULCK_NSLKEY_Pos             _U_(8)                                               /**< (NVMCTRL_NSULCK) Write Key Position */
#define NVMCTRL_NSULCK_NSLKEY_Msk             (_U_(0xFF) << NVMCTRL_NSULCK_NSLKEY_Pos)             /**< (NVMCTRL_NSULCK) Write Key Mask */
#define NVMCTRL_NSULCK_NSLKEY(value)          (NVMCTRL_NSULCK_NSLKEY_Msk & ((value) << NVMCTRL_NSULCK_NSLKEY_Pos))
#define   NVMCTRL_NSULCK_NSLKEY_KEY_Val       _U_(0xA5)                                            /**< (NVMCTRL_NSULCK) Write Key  */
#define NVMCTRL_NSULCK_NSLKEY_KEY             (NVMCTRL_NSULCK_NSLKEY_KEY_Val << NVMCTRL_NSULCK_NSLKEY_Pos) /**< (NVMCTRL_NSULCK) Write Key Position  */
#define NVMCTRL_NSULCK_Msk                    _U_(0xFF07)                                          /**< (NVMCTRL_NSULCK) Register Mask  */


/* -------- NVMCTRL_PARAM : (NVMCTRL Offset: 0x24) (R/W 32) NVM Parameter -------- */
#define NVMCTRL_PARAM_RESETVALUE              _U_(0x00)                                            /**<  (NVMCTRL_PARAM) NVM Parameter  Reset Value */

#define NVMCTRL_PARAM_FLASHP_Pos              _U_(0)                                               /**< (NVMCTRL_PARAM) FLASH Pages Position */
#define NVMCTRL_PARAM_FLASHP_Msk              (_U_(0xFFFF) << NVMCTRL_PARAM_FLASHP_Pos)            /**< (NVMCTRL_PARAM) FLASH Pages Mask */
#define NVMCTRL_PARAM_FLASHP(value)           (NVMCTRL_PARAM_FLASHP_Msk & ((value) << NVMCTRL_PARAM_FLASHP_Pos))
#define NVMCTRL_PARAM_PSZ_Pos                 _U_(16)                                              /**< (NVMCTRL_PARAM) Page Size Position */
#define NVMCTRL_PARAM_PSZ_Msk                 (_U_(0x7) << NVMCTRL_PARAM_PSZ_Pos)                  /**< (NVMCTRL_PARAM) Page Size Mask */
#define NVMCTRL_PARAM_PSZ(value)              (NVMCTRL_PARAM_PSZ_Msk & ((value) << NVMCTRL_PARAM_PSZ_Pos))
#define   NVMCTRL_PARAM_PSZ_8_Val             _U_(0x0)                                             /**< (NVMCTRL_PARAM) 8 bytes  */
#define   NVMCTRL_PARAM_PSZ_16_Val            _U_(0x1)                                             /**< (NVMCTRL_PARAM) 16 bytes  */
#define   NVMCTRL_PARAM_PSZ_32_Val            _U_(0x2)                                             /**< (NVMCTRL_PARAM) 32 bytes  */
#define   NVMCTRL_PARAM_PSZ_64_Val            _U_(0x3)                                             /**< (NVMCTRL_PARAM) 64 bytes  */
#define   NVMCTRL_PARAM_PSZ_128_Val           _U_(0x4)                                             /**< (NVMCTRL_PARAM) 128 bytes  */
#define   NVMCTRL_PARAM_PSZ_256_Val           _U_(0x5)                                             /**< (NVMCTRL_PARAM) 256 bytes  */
#define   NVMCTRL_PARAM_PSZ_512_Val           _U_(0x6)                                             /**< (NVMCTRL_PARAM) 512 bytes  */
#define   NVMCTRL_PARAM_PSZ_1024_Val          _U_(0x7)                                             /**< (NVMCTRL_PARAM) 1024 bytes  */
#define NVMCTRL_PARAM_PSZ_8                   (NVMCTRL_PARAM_PSZ_8_Val << NVMCTRL_PARAM_PSZ_Pos)   /**< (NVMCTRL_PARAM) 8 bytes Position  */
#define NVMCTRL_PARAM_PSZ_16                  (NVMCTRL_PARAM_PSZ_16_Val << NVMCTRL_PARAM_PSZ_Pos)  /**< (NVMCTRL_PARAM) 16 bytes Position  */
#define NVMCTRL_PARAM_PSZ_32                  (NVMCTRL_PARAM_PSZ_32_Val << NVMCTRL_PARAM_PSZ_Pos)  /**< (NVMCTRL_PARAM) 32 bytes Position  */
#define NVMCTRL_PARAM_PSZ_64                  (NVMCTRL_PARAM_PSZ_64_Val << NVMCTRL_PARAM_PSZ_Pos)  /**< (NVMCTRL_PARAM) 64 bytes Position  */
#define NVMCTRL_PARAM_PSZ_128                 (NVMCTRL_PARAM_PSZ_128_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 128 bytes Position  */
#define NVMCTRL_PARAM_PSZ_256                 (NVMCTRL_PARAM_PSZ_256_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 256 bytes Position  */
#define NVMCTRL_PARAM_PSZ_512                 (NVMCTRL_PARAM_PSZ_512_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 512 bytes Position  */
#define NVMCTRL_PARAM_PSZ_1024                (NVMCTRL_PARAM_PSZ_1024_Val << NVMCTRL_PARAM_PSZ_Pos) /**< (NVMCTRL_PARAM) 1024 bytes Position  */
#define NVMCTRL_PARAM_DFLASHP_Pos             _U_(20)                                              /**< (NVMCTRL_PARAM) DATAFLASH Pages Position */
#define NVMCTRL_PARAM_DFLASHP_Msk             (_U_(0xFFF) << NVMCTRL_PARAM_DFLASHP_Pos)            /**< (NVMCTRL_PARAM) DATAFLASH Pages Mask */
#define NVMCTRL_PARAM_DFLASHP(value)          (NVMCTRL_PARAM_DFLASHP_Msk & ((value) << NVMCTRL_PARAM_DFLASHP_Pos))
#define NVMCTRL_PARAM_Msk                     _U_(0xFFF7FFFF)                                      /**< (NVMCTRL_PARAM) Register Mask  */


/* -------- NVMCTRL_DSCC : (NVMCTRL Offset: 0x30) ( /W 32) Data Scramble Configuration -------- */
#define NVMCTRL_DSCC_RESETVALUE               _U_(0x00)                                            /**<  (NVMCTRL_DSCC) Data Scramble Configuration  Reset Value */

#define NVMCTRL_DSCC_DSCKEY_Pos               _U_(0)                                               /**< (NVMCTRL_DSCC) Data Scramble Key Position */
#define NVMCTRL_DSCC_DSCKEY_Msk               (_U_(0x3FFFFFFF) << NVMCTRL_DSCC_DSCKEY_Pos)         /**< (NVMCTRL_DSCC) Data Scramble Key Mask */
#define NVMCTRL_DSCC_DSCKEY(value)            (NVMCTRL_DSCC_DSCKEY_Msk & ((value) << NVMCTRL_DSCC_DSCKEY_Pos))
#define NVMCTRL_DSCC_Msk                      _U_(0x3FFFFFFF)                                      /**< (NVMCTRL_DSCC) Register Mask  */


/* -------- NVMCTRL_SECCTRL : (NVMCTRL Offset: 0x34) (R/W 32) Security Control -------- */
#define NVMCTRL_SECCTRL_RESETVALUE            _U_(0x30)                                            /**<  (NVMCTRL_SECCTRL) Security Control  Reset Value */

#define NVMCTRL_SECCTRL_TAMPEEN_Pos           _U_(0)                                               /**< (NVMCTRL_SECCTRL) Tamper Erase Enable Position */
#define NVMCTRL_SECCTRL_TAMPEEN_Msk           (_U_(0x1) << NVMCTRL_SECCTRL_TAMPEEN_Pos)            /**< (NVMCTRL_SECCTRL) Tamper Erase Enable Mask */
#define NVMCTRL_SECCTRL_TAMPEEN(value)        (NVMCTRL_SECCTRL_TAMPEEN_Msk & ((value) << NVMCTRL_SECCTRL_TAMPEEN_Pos))
#define NVMCTRL_SECCTRL_SILACC_Pos            _U_(2)                                               /**< (NVMCTRL_SECCTRL) Silent Access Position */
#define NVMCTRL_SECCTRL_SILACC_Msk            (_U_(0x1) << NVMCTRL_SECCTRL_SILACC_Pos)             /**< (NVMCTRL_SECCTRL) Silent Access Mask */
#define NVMCTRL_SECCTRL_SILACC(value)         (NVMCTRL_SECCTRL_SILACC_Msk & ((value) << NVMCTRL_SECCTRL_SILACC_Pos))
#define NVMCTRL_SECCTRL_DSCEN_Pos             _U_(3)                                               /**< (NVMCTRL_SECCTRL) Data Scramble Enable Position */
#define NVMCTRL_SECCTRL_DSCEN_Msk             (_U_(0x1) << NVMCTRL_SECCTRL_DSCEN_Pos)              /**< (NVMCTRL_SECCTRL) Data Scramble Enable Mask */
#define NVMCTRL_SECCTRL_DSCEN(value)          (NVMCTRL_SECCTRL_DSCEN_Msk & ((value) << NVMCTRL_SECCTRL_DSCEN_Pos))
#define NVMCTRL_SECCTRL_DXN_Pos               _U_(6)                                               /**< (NVMCTRL_SECCTRL) Data Flash is eXecute Never Position */
#define NVMCTRL_SECCTRL_DXN_Msk               (_U_(0x1) << NVMCTRL_SECCTRL_DXN_Pos)                /**< (NVMCTRL_SECCTRL) Data Flash is eXecute Never Mask */
#define NVMCTRL_SECCTRL_DXN(value)            (NVMCTRL_SECCTRL_DXN_Msk & ((value) << NVMCTRL_SECCTRL_DXN_Pos))
#define NVMCTRL_SECCTRL_TEROW_Pos             _U_(8)                                               /**< (NVMCTRL_SECCTRL) Tamper Rease Row Position */
#define NVMCTRL_SECCTRL_TEROW_Msk             (_U_(0x7) << NVMCTRL_SECCTRL_TEROW_Pos)              /**< (NVMCTRL_SECCTRL) Tamper Rease Row Mask */
#define NVMCTRL_SECCTRL_TEROW(value)          (NVMCTRL_SECCTRL_TEROW_Msk & ((value) << NVMCTRL_SECCTRL_TEROW_Pos))
#define NVMCTRL_SECCTRL_KEY_Pos               _U_(24)                                              /**< (NVMCTRL_SECCTRL) Write Key Position */
#define NVMCTRL_SECCTRL_KEY_Msk               (_U_(0xFF) << NVMCTRL_SECCTRL_KEY_Pos)               /**< (NVMCTRL_SECCTRL) Write Key Mask */
#define NVMCTRL_SECCTRL_KEY(value)            (NVMCTRL_SECCTRL_KEY_Msk & ((value) << NVMCTRL_SECCTRL_KEY_Pos))
#define   NVMCTRL_SECCTRL_KEY_KEY_Val         _U_(0xA5)                                            /**< (NVMCTRL_SECCTRL) Write Key  */
#define NVMCTRL_SECCTRL_KEY_KEY               (NVMCTRL_SECCTRL_KEY_KEY_Val << NVMCTRL_SECCTRL_KEY_Pos) /**< (NVMCTRL_SECCTRL) Write Key Position  */
#define NVMCTRL_SECCTRL_Msk                   _U_(0xFF00074D)                                      /**< (NVMCTRL_SECCTRL) Register Mask  */


/* -------- NVMCTRL_SCFGB : (NVMCTRL Offset: 0x38) (R/W 32) Secure Boot Configuration -------- */
#define NVMCTRL_SCFGB_RESETVALUE              _U_(0x03)                                            /**<  (NVMCTRL_SCFGB) Secure Boot Configuration  Reset Value */

#define NVMCTRL_SCFGB_BCREN_Pos               _U_(0)                                               /**< (NVMCTRL_SCFGB) Boot Configuration Row Read Enable Position */
#define NVMCTRL_SCFGB_BCREN_Msk               (_U_(0x1) << NVMCTRL_SCFGB_BCREN_Pos)                /**< (NVMCTRL_SCFGB) Boot Configuration Row Read Enable Mask */
#define NVMCTRL_SCFGB_BCREN(value)            (NVMCTRL_SCFGB_BCREN_Msk & ((value) << NVMCTRL_SCFGB_BCREN_Pos))
#define NVMCTRL_SCFGB_BCWEN_Pos               _U_(1)                                               /**< (NVMCTRL_SCFGB) Boot Configuration Row Write Enable Position */
#define NVMCTRL_SCFGB_BCWEN_Msk               (_U_(0x1) << NVMCTRL_SCFGB_BCWEN_Pos)                /**< (NVMCTRL_SCFGB) Boot Configuration Row Write Enable Mask */
#define NVMCTRL_SCFGB_BCWEN(value)            (NVMCTRL_SCFGB_BCWEN_Msk & ((value) << NVMCTRL_SCFGB_BCWEN_Pos))
#define NVMCTRL_SCFGB_Msk                     _U_(0x00000003)                                      /**< (NVMCTRL_SCFGB) Register Mask  */


/* -------- NVMCTRL_SCFGAD : (NVMCTRL Offset: 0x3C) (R/W 32) Secure Application and Data Configuration -------- */
#define NVMCTRL_SCFGAD_RESETVALUE             _U_(0x01)                                            /**<  (NVMCTRL_SCFGAD) Secure Application and Data Configuration  Reset Value */

#define NVMCTRL_SCFGAD_URWEN_Pos              _U_(0)                                               /**< (NVMCTRL_SCFGAD) User Row Write Enable Position */
#define NVMCTRL_SCFGAD_URWEN_Msk              (_U_(0x1) << NVMCTRL_SCFGAD_URWEN_Pos)               /**< (NVMCTRL_SCFGAD) User Row Write Enable Mask */
#define NVMCTRL_SCFGAD_URWEN(value)           (NVMCTRL_SCFGAD_URWEN_Msk & ((value) << NVMCTRL_SCFGAD_URWEN_Pos))
#define NVMCTRL_SCFGAD_Msk                    _U_(0x00000001)                                      /**< (NVMCTRL_SCFGAD) Register Mask  */


/* -------- NVMCTRL_NONSEC : (NVMCTRL Offset: 0x40) (R/W 32) Non-secure Write Enable -------- */
#define NVMCTRL_NONSEC_RESETVALUE             _U_(0x01)                                            /**<  (NVMCTRL_NONSEC) Non-secure Write Enable  Reset Value */

#define NVMCTRL_NONSEC_WRITE_Pos              _U_(0)                                               /**< (NVMCTRL_NONSEC) Non-secure APB alias write enable, non-secure AHB writes to non-secure regions enable Position */
#define NVMCTRL_NONSEC_WRITE_Msk              (_U_(0x1) << NVMCTRL_NONSEC_WRITE_Pos)               /**< (NVMCTRL_NONSEC) Non-secure APB alias write enable, non-secure AHB writes to non-secure regions enable Mask */
#define NVMCTRL_NONSEC_WRITE(value)           (NVMCTRL_NONSEC_WRITE_Msk & ((value) << NVMCTRL_NONSEC_WRITE_Pos))
#define NVMCTRL_NONSEC_Msk                    _U_(0x00000001)                                      /**< (NVMCTRL_NONSEC) Register Mask  */


/* -------- NVMCTRL_NSCHK : (NVMCTRL Offset: 0x44) (R/W 32) Non-secure Write Reference Value -------- */
#define NVMCTRL_NSCHK_RESETVALUE              _U_(0x01)                                            /**<  (NVMCTRL_NSCHK) Non-secure Write Reference Value  Reset Value */

#define NVMCTRL_NSCHK_WRITE_Pos               _U_(0)                                               /**< (NVMCTRL_NSCHK) Reference value to be checked against NONSEC.WRITE Position */
#define NVMCTRL_NSCHK_WRITE_Msk               (_U_(0x1) << NVMCTRL_NSCHK_WRITE_Pos)                /**< (NVMCTRL_NSCHK) Reference value to be checked against NONSEC.WRITE Mask */
#define NVMCTRL_NSCHK_WRITE(value)            (NVMCTRL_NSCHK_WRITE_Msk & ((value) << NVMCTRL_NSCHK_WRITE_Pos))
#define NVMCTRL_NSCHK_Msk                     _U_(0x00000001)                                      /**< (NVMCTRL_NSCHK) Register Mask  */


/** \brief NVMCTRL register offsets definitions */
#define NVMCTRL_CTRLA_REG_OFST         (0x00)              /**< (NVMCTRL_CTRLA) Control A Offset */
#define NVMCTRL_CTRLB_REG_OFST         (0x04)              /**< (NVMCTRL_CTRLB) Control B Offset */
#define NVMCTRL_CTRLC_REG_OFST         (0x08)              /**< (NVMCTRL_CTRLC) Control C Offset */
#define NVMCTRL_EVCTRL_REG_OFST        (0x0A)              /**< (NVMCTRL_EVCTRL) Event Control Offset */
#define NVMCTRL_INTENCLR_REG_OFST      (0x0C)              /**< (NVMCTRL_INTENCLR) Interrupt Enable Clear Offset */
#define NVMCTRL_INTENSET_REG_OFST      (0x10)              /**< (NVMCTRL_INTENSET) Interrupt Enable Set Offset */
#define NVMCTRL_INTFLAG_REG_OFST       (0x14)              /**< (NVMCTRL_INTFLAG) Interrupt Flag Status and Clear Offset */
#define NVMCTRL_STATUS_REG_OFST        (0x18)              /**< (NVMCTRL_STATUS) Status Offset */
#define NVMCTRL_ADDR_REG_OFST          (0x1C)              /**< (NVMCTRL_ADDR) Address Offset */
#define NVMCTRL_SULCK_REG_OFST         (0x20)              /**< (NVMCTRL_SULCK) Secure Unlock Register Offset */
#define NVMCTRL_NSULCK_REG_OFST        (0x22)              /**< (NVMCTRL_NSULCK) Non-Secure Unlock Register Offset */
#define NVMCTRL_PARAM_REG_OFST         (0x24)              /**< (NVMCTRL_PARAM) NVM Parameter Offset */
#define NVMCTRL_DSCC_REG_OFST          (0x30)              /**< (NVMCTRL_DSCC) Data Scramble Configuration Offset */
#define NVMCTRL_SECCTRL_REG_OFST       (0x34)              /**< (NVMCTRL_SECCTRL) Security Control Offset */
#define NVMCTRL_SCFGB_REG_OFST         (0x38)              /**< (NVMCTRL_SCFGB) Secure Boot Configuration Offset */
#define NVMCTRL_SCFGAD_REG_OFST        (0x3C)              /**< (NVMCTRL_SCFGAD) Secure Application and Data Configuration Offset */
#define NVMCTRL_NONSEC_REG_OFST        (0x40)              /**< (NVMCTRL_NONSEC) Non-secure Write Enable Offset */
#define NVMCTRL_NSCHK_REG_OFST         (0x44)              /**< (NVMCTRL_NSCHK) Non-secure Write Reference Value Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief NVMCTRL register API structure */
typedef struct
{  /* Non-Volatile Memory Controller */
  __O   uint16_t                       NVMCTRL_CTRLA;      /**< Offset: 0x00 ( /W  16) Control A */
  __I   uint8_t                        Reserved1[0x02];
  __IO  uint32_t                       NVMCTRL_CTRLB;      /**< Offset: 0x04 (R/W  32) Control B */
  __IO  uint8_t                        NVMCTRL_CTRLC;      /**< Offset: 0x08 (R/W  8) Control C */
  __I   uint8_t                        Reserved2[0x01];
  __IO  uint8_t                        NVMCTRL_EVCTRL;     /**< Offset: 0x0A (R/W  8) Event Control */
  __I   uint8_t                        Reserved3[0x01];
  __IO  uint8_t                        NVMCTRL_INTENCLR;   /**< Offset: 0x0C (R/W  8) Interrupt Enable Clear */
  __I   uint8_t                        Reserved4[0x03];
  __IO  uint8_t                        NVMCTRL_INTENSET;   /**< Offset: 0x10 (R/W  8) Interrupt Enable Set */
  __I   uint8_t                        Reserved5[0x03];
  __IO  uint8_t                        NVMCTRL_INTFLAG;    /**< Offset: 0x14 (R/W  8) Interrupt Flag Status and Clear */
  __I   uint8_t                        Reserved6[0x03];
  __I   uint16_t                       NVMCTRL_STATUS;     /**< Offset: 0x18 (R/   16) Status */
  __I   uint8_t                        Reserved7[0x02];
  __IO  uint32_t                       NVMCTRL_ADDR;       /**< Offset: 0x1C (R/W  32) Address */
  __IO  uint16_t                       NVMCTRL_SULCK;      /**< Offset: 0x20 (R/W  16) Secure Unlock Register */
  __IO  uint16_t                       NVMCTRL_NSULCK;     /**< Offset: 0x22 (R/W  16) Non-Secure Unlock Register */
  __IO  uint32_t                       NVMCTRL_PARAM;      /**< Offset: 0x24 (R/W  32) NVM Parameter */
  __I   uint8_t                        Reserved8[0x08];
  __O   uint32_t                       NVMCTRL_DSCC;       /**< Offset: 0x30 ( /W  32) Data Scramble Configuration */
  __IO  uint32_t                       NVMCTRL_SECCTRL;    /**< Offset: 0x34 (R/W  32) Security Control */
  __IO  uint32_t                       NVMCTRL_SCFGB;      /**< Offset: 0x38 (R/W  32) Secure Boot Configuration */
  __IO  uint32_t                       NVMCTRL_SCFGAD;     /**< Offset: 0x3C (R/W  32) Secure Application and Data Configuration */
  __IO  uint32_t                       NVMCTRL_NONSEC;     /**< Offset: 0x40 (R/W  32) Non-secure Write Enable */
  __IO  uint32_t                       NVMCTRL_NSCHK;      /**< Offset: 0x44 (R/W  32) Non-secure Write Reference Value */
} nvmctrl_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#if defined (__GNUC__) || defined (__CC_ARM)
  #define SECTION_AUX                  __attribute__ ((section(".flash")))
  #define SECTION_BOCOR                __attribute__ ((section(".flash")))
  #define SECTION_DATAFLASH            __attribute__ ((section(".flash")))
  #define SECTION_SW_CALIB             __attribute__ ((section(".flash")))
  #define SECTION_TEMP_LOG             __attribute__ ((section(".flash")))
  #define SECTION_USER_PAGE            __attribute__ ((section(".flash")))

#elif defined(__ICCARM__)
  #define SECTION_AUX                  @".flash"
  #define SECTION_BOCOR                @".flash"
  #define SECTION_DATAFLASH            @".flash"
  #define SECTION_SW_CALIB             @".flash"
  #define SECTION_TEMP_LOG             @".flash"
  #define SECTION_USER_PAGE            @".flash"

#endif

/** \addtogroup fuses_api Peripheral Software API
 *  @{
 */

/* ************************************************************************** */
/**  SOFTWARE PERIPHERAL API DEFINITION FOR NON-VOLATILE FUSES */
/* ************************************************************************** */
#define ADC_FUSES_BIASCOMP_ADDR     SW_CALIB_ADDR
#define ADC_FUSES_BIASCOMP_Pos      3            /**< \brief (SW_CALIB_ADDR) ADC Comparator Scaling */
#define ADC_FUSES_BIASCOMP_Msk      (_U_(0x7) << ADC_FUSES_BIASCOMP_Pos)
#define ADC_FUSES_BIASCOMP(value)   (ADC_FUSES_BIASCOMP_Msk & ((value) << ADC_FUSES_BIASCOMP_Pos))

#define ADC_FUSES_BIASREFBUF_ADDR   SW_CALIB_ADDR
#define ADC_FUSES_BIASREFBUF_Pos    0            /**< \brief (SW_CALIB_ADDR) ADC Bias Reference Buffer Scaling */
#define ADC_FUSES_BIASREFBUF_Msk    (_U_(0x7) << ADC_FUSES_BIASREFBUF_Pos)
#define ADC_FUSES_BIASREFBUF(value) (ADC_FUSES_BIASREFBUF_Msk & ((value) << ADC_FUSES_BIASREFBUF_Pos))

#define FUSES_BOD33USERLEVEL_ADDR   USER_PAGE_ADDR
#define FUSES_BOD33USERLEVEL_Pos    7            /**< \brief (USER_PAGE_ADDR) BOD33 User Level */
#define FUSES_BOD33USERLEVEL_Msk    (_U_(0x3F) << FUSES_BOD33USERLEVEL_Pos)
#define FUSES_BOD33USERLEVEL(value) (FUSES_BOD33USERLEVEL_Msk & ((value) << FUSES_BOD33USERLEVEL_Pos))

#define FUSES_BOD33_ACTION_ADDR     USER_PAGE_ADDR
#define FUSES_BOD33_ACTION_Pos      14           /**< \brief (USER_PAGE_ADDR) BOD33 Action */
#define FUSES_BOD33_ACTION_Msk      (_U_(0x3) << FUSES_BOD33_ACTION_Pos)
#define FUSES_BOD33_ACTION(value)   (FUSES_BOD33_ACTION_Msk & ((value) << FUSES_BOD33_ACTION_Pos))

#define FUSES_BOD33_DIS_ADDR        USER_PAGE_ADDR
#define FUSES_BOD33_DIS_Pos         13           /**< \brief (USER_PAGE_ADDR) BOD33 Disable */
#define FUSES_BOD33_DIS_Msk         (_U_(0x1) << FUSES_BOD33_DIS_Pos)

#define FUSES_BOD33_HYST_ADDR       (USER_PAGE_ADDR + 4)
#define FUSES_BOD33_HYST_Pos        9            /**< \brief (USER_PAGE_ADDR) BOD33 Hysteresis */
#define FUSES_BOD33_HYST_Msk        (_U_(0x1) << FUSES_BOD33_HYST_Pos)

#define FUSES_BOOTROM_BOCORCRC_ADDR (BOCOR_ADDR + 8)
#define FUSES_BOOTROM_BOCORCRC_Pos  0            /**< \brief (BOCOR_ADDR) CRC for BOCOR0 DWORD */
#define FUSES_BOOTROM_BOCORCRC_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOCORCRC_Pos)
#define FUSES_BOOTROM_BOCORCRC(value) (FUSES_BOOTROM_BOCORCRC_Msk & ((value) << FUSES_BOOTROM_BOCORCRC_Pos))

#define FUSES_BOOTROM_BOCORHASH_0_ADDR (BOCOR_ADDR + 224)
#define FUSES_BOOTROM_BOCORHASH_0_Pos 0            /**< \brief (BOCOR_ADDR) Boot Configuration Row Hash bits 31:0 */
#define FUSES_BOOTROM_BOCORHASH_0_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOCORHASH_0_Pos)
#define FUSES_BOOTROM_BOCORHASH_0(value) (FUSES_BOOTROM_BOCORHASH_0_Msk & ((value) << FUSES_BOOTROM_BOCORHASH_0_Pos))

#define FUSES_BOOTROM_BOCORHASH_1_ADDR (BOCOR_ADDR + 228)
#define FUSES_BOOTROM_BOCORHASH_1_Pos 0            /**< \brief (BOCOR_ADDR) Boot Configuration Row Hash bits 63:32 */
#define FUSES_BOOTROM_BOCORHASH_1_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOCORHASH_1_Pos)
#define FUSES_BOOTROM_BOCORHASH_1(value) (FUSES_BOOTROM_BOCORHASH_1_Msk & ((value) << FUSES_BOOTROM_BOCORHASH_1_Pos))

#define FUSES_BOOTROM_BOCORHASH_2_ADDR (BOCOR_ADDR + 232)
#define FUSES_BOOTROM_BOCORHASH_2_Pos 0            /**< \brief (BOCOR_ADDR) Boot Configuration Row Hash bits 95:64 */
#define FUSES_BOOTROM_BOCORHASH_2_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOCORHASH_2_Pos)
#define FUSES_BOOTROM_BOCORHASH_2(value) (FUSES_BOOTROM_BOCORHASH_2_Msk & ((value) << FUSES_BOOTROM_BOCORHASH_2_Pos))

#define FUSES_BOOTROM_BOCORHASH_3_ADDR (BOCOR_ADDR + 236)
#define FUSES_BOOTROM_BOCORHASH_3_Pos 0            /**< \brief (BOCOR_ADDR) Boot Configuration Row Hash bits 127:96 */
#define FUSES_BOOTROM_BOCORHASH_3_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOCORHASH_3_Pos)
#define FUSES_BOOTROM_BOCORHASH_3(value) (FUSES_BOOTROM_BOCORHASH_3_Msk & ((value) << FUSES_BOOTROM_BOCORHASH_3_Pos))

#define FUSES_BOOTROM_BOCORHASH_4_ADDR (BOCOR_ADDR + 240)
#define FUSES_BOOTROM_BOCORHASH_4_Pos 0            /**< \brief (BOCOR_ADDR) Boot Configuration Row Hash bits 159:128 */
#define FUSES_BOOTROM_BOCORHASH_4_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOCORHASH_4_Pos)
#define FUSES_BOOTROM_BOCORHASH_4(value) (FUSES_BOOTROM_BOCORHASH_4_Msk & ((value) << FUSES_BOOTROM_BOCORHASH_4_Pos))

#define FUSES_BOOTROM_BOCORHASH_5_ADDR (BOCOR_ADDR + 244)
#define FUSES_BOOTROM_BOCORHASH_5_Pos 0            /**< \brief (BOCOR_ADDR) Boot Configuration Row Hash bits 191:160 */
#define FUSES_BOOTROM_BOCORHASH_5_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOCORHASH_5_Pos)
#define FUSES_BOOTROM_BOCORHASH_5(value) (FUSES_BOOTROM_BOCORHASH_5_Msk & ((value) << FUSES_BOOTROM_BOCORHASH_5_Pos))

#define FUSES_BOOTROM_BOCORHASH_6_ADDR (BOCOR_ADDR + 248)
#define FUSES_BOOTROM_BOCORHASH_6_Pos 0            /**< \brief (BOCOR_ADDR) Boot Configuration Row Hash bits 223:192 */
#define FUSES_BOOTROM_BOCORHASH_6_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOCORHASH_6_Pos)
#define FUSES_BOOTROM_BOCORHASH_6(value) (FUSES_BOOTROM_BOCORHASH_6_Msk & ((value) << FUSES_BOOTROM_BOCORHASH_6_Pos))

#define FUSES_BOOTROM_BOCORHASH_7_ADDR (BOCOR_ADDR + 252)
#define FUSES_BOOTROM_BOCORHASH_7_Pos 0            /**< \brief (BOCOR_ADDR) Boot Configuration Row Hash bits 255:224 */
#define FUSES_BOOTROM_BOCORHASH_7_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOCORHASH_7_Pos)
#define FUSES_BOOTROM_BOCORHASH_7(value) (FUSES_BOOTROM_BOCORHASH_7_Msk & ((value) << FUSES_BOOTROM_BOCORHASH_7_Pos))

#define FUSES_BOOTROM_BOOTKEY_0_ADDR (BOCOR_ADDR + 80)
#define FUSES_BOOTROM_BOOTKEY_0_Pos 0            /**< \brief (BOCOR_ADDR) Secure Boot Key bits 31:0 */
#define FUSES_BOOTROM_BOOTKEY_0_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOOTKEY_0_Pos)
#define FUSES_BOOTROM_BOOTKEY_0(value) (FUSES_BOOTROM_BOOTKEY_0_Msk & ((value) << FUSES_BOOTROM_BOOTKEY_0_Pos))

#define FUSES_BOOTROM_BOOTKEY_1_ADDR (BOCOR_ADDR + 84)
#define FUSES_BOOTROM_BOOTKEY_1_Pos 0            /**< \brief (BOCOR_ADDR) Secure Boot Key bits 63:32 */
#define FUSES_BOOTROM_BOOTKEY_1_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOOTKEY_1_Pos)
#define FUSES_BOOTROM_BOOTKEY_1(value) (FUSES_BOOTROM_BOOTKEY_1_Msk & ((value) << FUSES_BOOTROM_BOOTKEY_1_Pos))

#define FUSES_BOOTROM_BOOTKEY_2_ADDR (BOCOR_ADDR + 88)
#define FUSES_BOOTROM_BOOTKEY_2_Pos 0            /**< \brief (BOCOR_ADDR) Secure Boot Key bits 95:64 */
#define FUSES_BOOTROM_BOOTKEY_2_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOOTKEY_2_Pos)
#define FUSES_BOOTROM_BOOTKEY_2(value) (FUSES_BOOTROM_BOOTKEY_2_Msk & ((value) << FUSES_BOOTROM_BOOTKEY_2_Pos))

#define FUSES_BOOTROM_BOOTKEY_3_ADDR (BOCOR_ADDR + 92)
#define FUSES_BOOTROM_BOOTKEY_3_Pos 0            /**< \brief (BOCOR_ADDR) Secure Boot Key bits 127:96 */
#define FUSES_BOOTROM_BOOTKEY_3_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOOTKEY_3_Pos)
#define FUSES_BOOTROM_BOOTKEY_3(value) (FUSES_BOOTROM_BOOTKEY_3_Msk & ((value) << FUSES_BOOTROM_BOOTKEY_3_Pos))

#define FUSES_BOOTROM_BOOTKEY_4_ADDR (BOCOR_ADDR + 96)
#define FUSES_BOOTROM_BOOTKEY_4_Pos 0            /**< \brief (BOCOR_ADDR) Secure Boot Key bits 159:128 */
#define FUSES_BOOTROM_BOOTKEY_4_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOOTKEY_4_Pos)
#define FUSES_BOOTROM_BOOTKEY_4(value) (FUSES_BOOTROM_BOOTKEY_4_Msk & ((value) << FUSES_BOOTROM_BOOTKEY_4_Pos))

#define FUSES_BOOTROM_BOOTKEY_5_ADDR (BOCOR_ADDR + 100)
#define FUSES_BOOTROM_BOOTKEY_5_Pos 0            /**< \brief (BOCOR_ADDR) Secure Boot Key bits 191:160 */
#define FUSES_BOOTROM_BOOTKEY_5_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOOTKEY_5_Pos)
#define FUSES_BOOTROM_BOOTKEY_5(value) (FUSES_BOOTROM_BOOTKEY_5_Msk & ((value) << FUSES_BOOTROM_BOOTKEY_5_Pos))

#define FUSES_BOOTROM_BOOTKEY_6_ADDR (BOCOR_ADDR + 104)
#define FUSES_BOOTROM_BOOTKEY_6_Pos 0            /**< \brief (BOCOR_ADDR) Secure Boot Key bits 223:192 */
#define FUSES_BOOTROM_BOOTKEY_6_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOOTKEY_6_Pos)
#define FUSES_BOOTROM_BOOTKEY_6(value) (FUSES_BOOTROM_BOOTKEY_6_Msk & ((value) << FUSES_BOOTROM_BOOTKEY_6_Pos))

#define FUSES_BOOTROM_BOOTKEY_7_ADDR (BOCOR_ADDR + 108)
#define FUSES_BOOTROM_BOOTKEY_7_Pos 0            /**< \brief (BOCOR_ADDR) Secure Boot Key bits 255:224 */
#define FUSES_BOOTROM_BOOTKEY_7_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_BOOTKEY_7_Pos)
#define FUSES_BOOTROM_BOOTKEY_7(value) (FUSES_BOOTROM_BOOTKEY_7_Msk & ((value) << FUSES_BOOTROM_BOOTKEY_7_Pos))

#define FUSES_BOOTROM_BOOTOPT_ADDR  BOCOR_ADDR
#define FUSES_BOOTROM_BOOTOPT_Pos   24           /**< \brief (BOCOR_ADDR) Boot Option */
#define FUSES_BOOTROM_BOOTOPT_Msk   (_U_(0xFF) << FUSES_BOOTROM_BOOTOPT_Pos)
#define FUSES_BOOTROM_BOOTOPT(value) (FUSES_BOOTROM_BOOTOPT_Msk & ((value) << FUSES_BOOTROM_BOOTOPT_Pos))

#define FUSES_BOOTROM_CEKEY0_0_ADDR (BOCOR_ADDR + 16)
#define FUSES_BOOTROM_CEKEY0_0_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 0 bits 31:0 */
#define FUSES_BOOTROM_CEKEY0_0_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY0_0_Pos)
#define FUSES_BOOTROM_CEKEY0_0(value) (FUSES_BOOTROM_CEKEY0_0_Msk & ((value) << FUSES_BOOTROM_CEKEY0_0_Pos))

#define FUSES_BOOTROM_CEKEY0_1_ADDR (BOCOR_ADDR + 20)
#define FUSES_BOOTROM_CEKEY0_1_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 0 bits 63:32 */
#define FUSES_BOOTROM_CEKEY0_1_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY0_1_Pos)
#define FUSES_BOOTROM_CEKEY0_1(value) (FUSES_BOOTROM_CEKEY0_1_Msk & ((value) << FUSES_BOOTROM_CEKEY0_1_Pos))

#define FUSES_BOOTROM_CEKEY0_2_ADDR (BOCOR_ADDR + 24)
#define FUSES_BOOTROM_CEKEY0_2_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 0 bits 95:64 */
#define FUSES_BOOTROM_CEKEY0_2_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY0_2_Pos)
#define FUSES_BOOTROM_CEKEY0_2(value) (FUSES_BOOTROM_CEKEY0_2_Msk & ((value) << FUSES_BOOTROM_CEKEY0_2_Pos))

#define FUSES_BOOTROM_CEKEY0_3_ADDR (BOCOR_ADDR + 28)
#define FUSES_BOOTROM_CEKEY0_3_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 0 bits 127:96 */
#define FUSES_BOOTROM_CEKEY0_3_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY0_3_Pos)
#define FUSES_BOOTROM_CEKEY0_3(value) (FUSES_BOOTROM_CEKEY0_3_Msk & ((value) << FUSES_BOOTROM_CEKEY0_3_Pos))

#define FUSES_BOOTROM_CEKEY1_0_ADDR (BOCOR_ADDR + 32)
#define FUSES_BOOTROM_CEKEY1_0_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 1 bits 31:0 */
#define FUSES_BOOTROM_CEKEY1_0_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY1_0_Pos)
#define FUSES_BOOTROM_CEKEY1_0(value) (FUSES_BOOTROM_CEKEY1_0_Msk & ((value) << FUSES_BOOTROM_CEKEY1_0_Pos))

#define FUSES_BOOTROM_CEKEY1_1_ADDR (BOCOR_ADDR + 36)
#define FUSES_BOOTROM_CEKEY1_1_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 1 bits 63:32 */
#define FUSES_BOOTROM_CEKEY1_1_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY1_1_Pos)
#define FUSES_BOOTROM_CEKEY1_1(value) (FUSES_BOOTROM_CEKEY1_1_Msk & ((value) << FUSES_BOOTROM_CEKEY1_1_Pos))

#define FUSES_BOOTROM_CEKEY1_2_ADDR (BOCOR_ADDR + 40)
#define FUSES_BOOTROM_CEKEY1_2_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 1 bits 95:64 */
#define FUSES_BOOTROM_CEKEY1_2_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY1_2_Pos)
#define FUSES_BOOTROM_CEKEY1_2(value) (FUSES_BOOTROM_CEKEY1_2_Msk & ((value) << FUSES_BOOTROM_CEKEY1_2_Pos))

#define FUSES_BOOTROM_CEKEY1_3_ADDR (BOCOR_ADDR + 44)
#define FUSES_BOOTROM_CEKEY1_3_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 1 bits 127:96 */
#define FUSES_BOOTROM_CEKEY1_3_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY1_3_Pos)
#define FUSES_BOOTROM_CEKEY1_3(value) (FUSES_BOOTROM_CEKEY1_3_Msk & ((value) << FUSES_BOOTROM_CEKEY1_3_Pos))

#define FUSES_BOOTROM_CEKEY2_0_ADDR (BOCOR_ADDR + 48)
#define FUSES_BOOTROM_CEKEY2_0_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 2 bits 31:0 */
#define FUSES_BOOTROM_CEKEY2_0_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY2_0_Pos)
#define FUSES_BOOTROM_CEKEY2_0(value) (FUSES_BOOTROM_CEKEY2_0_Msk & ((value) << FUSES_BOOTROM_CEKEY2_0_Pos))

#define FUSES_BOOTROM_CEKEY2_1_ADDR (BOCOR_ADDR + 52)
#define FUSES_BOOTROM_CEKEY2_1_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 2 bits 63:32 */
#define FUSES_BOOTROM_CEKEY2_1_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY2_1_Pos)
#define FUSES_BOOTROM_CEKEY2_1(value) (FUSES_BOOTROM_CEKEY2_1_Msk & ((value) << FUSES_BOOTROM_CEKEY2_1_Pos))

#define FUSES_BOOTROM_CEKEY2_2_ADDR (BOCOR_ADDR + 56)
#define FUSES_BOOTROM_CEKEY2_2_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 2 bits 95:64 */
#define FUSES_BOOTROM_CEKEY2_2_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY2_2_Pos)
#define FUSES_BOOTROM_CEKEY2_2(value) (FUSES_BOOTROM_CEKEY2_2_Msk & ((value) << FUSES_BOOTROM_CEKEY2_2_Pos))

#define FUSES_BOOTROM_CEKEY2_3_ADDR (BOCOR_ADDR + 60)
#define FUSES_BOOTROM_CEKEY2_3_Pos  0            /**< \brief (BOCOR_ADDR) Chip Erase Key 2 bits 127:96 */
#define FUSES_BOOTROM_CEKEY2_3_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CEKEY2_3_Pos)
#define FUSES_BOOTROM_CEKEY2_3(value) (FUSES_BOOTROM_CEKEY2_3_Msk & ((value) << FUSES_BOOTROM_CEKEY2_3_Pos))

#define FUSES_BOOTROM_CRCKEY_0_ADDR (BOCOR_ADDR + 64)
#define FUSES_BOOTROM_CRCKEY_0_Pos  0            /**< \brief (BOCOR_ADDR) CRC Key bits 31:0 */
#define FUSES_BOOTROM_CRCKEY_0_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CRCKEY_0_Pos)
#define FUSES_BOOTROM_CRCKEY_0(value) (FUSES_BOOTROM_CRCKEY_0_Msk & ((value) << FUSES_BOOTROM_CRCKEY_0_Pos))

#define FUSES_BOOTROM_CRCKEY_1_ADDR (BOCOR_ADDR + 68)
#define FUSES_BOOTROM_CRCKEY_1_Pos  0            /**< \brief (BOCOR_ADDR) CRC Key bits 63:32 */
#define FUSES_BOOTROM_CRCKEY_1_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CRCKEY_1_Pos)
#define FUSES_BOOTROM_CRCKEY_1(value) (FUSES_BOOTROM_CRCKEY_1_Msk & ((value) << FUSES_BOOTROM_CRCKEY_1_Pos))

#define FUSES_BOOTROM_CRCKEY_2_ADDR (BOCOR_ADDR + 72)
#define FUSES_BOOTROM_CRCKEY_2_Pos  0            /**< \brief (BOCOR_ADDR) CRC Key bits 95:64 */
#define FUSES_BOOTROM_CRCKEY_2_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CRCKEY_2_Pos)
#define FUSES_BOOTROM_CRCKEY_2(value) (FUSES_BOOTROM_CRCKEY_2_Msk & ((value) << FUSES_BOOTROM_CRCKEY_2_Pos))

#define FUSES_BOOTROM_CRCKEY_3_ADDR (BOCOR_ADDR + 76)
#define FUSES_BOOTROM_CRCKEY_3_Pos  0            /**< \brief (BOCOR_ADDR) CRC Key bits 127:96 */
#define FUSES_BOOTROM_CRCKEY_3_Msk  (_U_(0xFFFFFFFF) << FUSES_BOOTROM_CRCKEY_3_Pos)
#define FUSES_BOOTROM_CRCKEY_3(value) (FUSES_BOOTROM_CRCKEY_3_Msk & ((value) << FUSES_BOOTROM_CRCKEY_3_Pos))

#define FUSES_BOOTROM_DXN_ADDR      (USER_PAGE_ADDR + 4)
#define FUSES_BOOTROM_DXN_Pos       12           /**< \brief (USER_PAGE_ADDR) DATA FLASH is eXecute Never */
#define FUSES_BOOTROM_DXN_Msk       (_U_(0x1) << FUSES_BOOTROM_DXN_Pos)

#define FUSES_BOOTROM_NONSECA_ADDR  (USER_PAGE_ADDR + 16)
#define FUSES_BOOTROM_NONSECA_Pos   0            /**< \brief (USER_PAGE_ADDR) NONSEC fuses for the bridgeA peripherals */
#define FUSES_BOOTROM_NONSECA_Msk   (_U_(0xFFFFFFFF) << FUSES_BOOTROM_NONSECA_Pos)
#define FUSES_BOOTROM_NONSECA(value) (FUSES_BOOTROM_NONSECA_Msk & ((value) << FUSES_BOOTROM_NONSECA_Pos))

#define FUSES_BOOTROM_NONSECB_ADDR  (USER_PAGE_ADDR + 20)
#define FUSES_BOOTROM_NONSECB_Pos   0            /**< \brief (USER_PAGE_ADDR) NONSEC fuses for the bridgeB peripherals */
#define FUSES_BOOTROM_NONSECB_Msk   (_U_(0xFFFFFFFF) << FUSES_BOOTROM_NONSECB_Pos)
#define FUSES_BOOTROM_NONSECB(value) (FUSES_BOOTROM_NONSECB_Msk & ((value) << FUSES_BOOTROM_NONSECB_Pos))

#define FUSES_BOOTROM_NONSECC_ADDR  (USER_PAGE_ADDR + 24)
#define FUSES_BOOTROM_NONSECC_Pos   0            /**< \brief (USER_PAGE_ADDR) NONSEC fuses for the bridgeC peripherals */
#define FUSES_BOOTROM_NONSECC_Msk   (_U_(0xFFFFFFFF) << FUSES_BOOTROM_NONSECC_Pos)
#define FUSES_BOOTROM_NONSECC(value) (FUSES_BOOTROM_NONSECC_Msk & ((value) << FUSES_BOOTROM_NONSECC_Pos))

#define FUSES_BOOTROM_ROMVERSION_ADDR (BOCOR_ADDR + 12)
#define FUSES_BOOTROM_ROMVERSION_Pos 0            /**< \brief (BOCOR_ADDR) BOOTROM Version */
#define FUSES_BOOTROM_ROMVERSION_Msk (_U_(0xFFFFFFFF) << FUSES_BOOTROM_ROMVERSION_Pos)
#define FUSES_BOOTROM_ROMVERSION(value) (FUSES_BOOTROM_ROMVERSION_Msk & ((value) << FUSES_BOOTROM_ROMVERSION_Pos))

#define FUSES_BOOTROM_RXN_ADDR      (USER_PAGE_ADDR + 4)
#define FUSES_BOOTROM_RXN_Pos       11           /**< \brief (USER_PAGE_ADDR) RAM is eXecute Never */
#define FUSES_BOOTROM_RXN_Msk       (_U_(0x1) << FUSES_BOOTROM_RXN_Pos)

#define FUSES_BOOTROM_USERCRC_ADDR  (USER_PAGE_ADDR + 28)
#define FUSES_BOOTROM_USERCRC_Pos   0            /**< \brief (USER_PAGE_ADDR) CRC for USER[1,2,3] DWORDS */
#define FUSES_BOOTROM_USERCRC_Msk   (_U_(0xFFFFFFFF) << FUSES_BOOTROM_USERCRC_Pos)
#define FUSES_BOOTROM_USERCRC(value) (FUSES_BOOTROM_USERCRC_Msk & ((value) << FUSES_BOOTROM_USERCRC_Pos))

#define FUSES_DFLLULP_DIV_PL0_ADDR  SW_CALIB_ADDR
#define FUSES_DFLLULP_DIV_PL0_Pos   6            /**< \brief (SW_CALIB_ADDR) DFLLULP DIV at PL0 */
#define FUSES_DFLLULP_DIV_PL0_Msk   (_U_(0x7) << FUSES_DFLLULP_DIV_PL0_Pos)
#define FUSES_DFLLULP_DIV_PL0(value) (FUSES_DFLLULP_DIV_PL0_Msk & ((value) << FUSES_DFLLULP_DIV_PL0_Pos))

#define FUSES_DFLLULP_DIV_PL2_ADDR  SW_CALIB_ADDR
#define FUSES_DFLLULP_DIV_PL2_Pos   9            /**< \brief (SW_CALIB_ADDR) DFLLULP DIV at PL2 */
#define FUSES_DFLLULP_DIV_PL2_Msk   (_U_(0x7) << FUSES_DFLLULP_DIV_PL2_Pos)
#define FUSES_DFLLULP_DIV_PL2(value) (FUSES_DFLLULP_DIV_PL2_Msk & ((value) << FUSES_DFLLULP_DIV_PL2_Pos))

#define FUSES_HOT_ADC_VAL_PTAT_ADDR (TEMP_LOG_ADDR + 4)
#define FUSES_HOT_ADC_VAL_PTAT_Pos  20           /**< \brief (TEMP_LOG_ADDR) 12-bit ADC conversion at hot temperature PTAT */
#define FUSES_HOT_ADC_VAL_PTAT_Msk  (_U_(0xFFF) << FUSES_HOT_ADC_VAL_PTAT_Pos)
#define FUSES_HOT_ADC_VAL_PTAT(value) (FUSES_HOT_ADC_VAL_PTAT_Msk & ((value) << FUSES_HOT_ADC_VAL_PTAT_Pos))

#define FUSES_HOT_INT1V_VAL_ADDR    (TEMP_LOG_ADDR + 4)
#define FUSES_HOT_INT1V_VAL_Pos     0            /**< \brief (TEMP_LOG_ADDR) 2's complement of the internal 1V reference drift at hot temperature (versus a 1.0 centered value) */
#define FUSES_HOT_INT1V_VAL_Msk     (_U_(0xFF) << FUSES_HOT_INT1V_VAL_Pos)
#define FUSES_HOT_INT1V_VAL(value)  (FUSES_HOT_INT1V_VAL_Msk & ((value) << FUSES_HOT_INT1V_VAL_Pos))

#define FUSES_HOT_TEMP_VAL_DEC_ADDR TEMP_LOG_ADDR
#define FUSES_HOT_TEMP_VAL_DEC_Pos  20           /**< \brief (TEMP_LOG_ADDR) Decimal part of hot temperature */
#define FUSES_HOT_TEMP_VAL_DEC_Msk  (_U_(0xF) << FUSES_HOT_TEMP_VAL_DEC_Pos)
#define FUSES_HOT_TEMP_VAL_DEC(value) (FUSES_HOT_TEMP_VAL_DEC_Msk & ((value) << FUSES_HOT_TEMP_VAL_DEC_Pos))

#define FUSES_HOT_TEMP_VAL_INT_ADDR TEMP_LOG_ADDR
#define FUSES_HOT_TEMP_VAL_INT_Pos  12           /**< \brief (TEMP_LOG_ADDR) Integer part of hot temperature in oC */
#define FUSES_HOT_TEMP_VAL_INT_Msk  (_U_(0xFF) << FUSES_HOT_TEMP_VAL_INT_Pos)
#define FUSES_HOT_TEMP_VAL_INT(value) (FUSES_HOT_TEMP_VAL_INT_Msk & ((value) << FUSES_HOT_TEMP_VAL_INT_Pos))

#define FUSES_ROOM_ADC_VAL_PTAT_ADDR (TEMP_LOG_ADDR + 4)
#define FUSES_ROOM_ADC_VAL_PTAT_Pos 8            /**< \brief (TEMP_LOG_ADDR) 12-bit ADC conversion at room temperature PTAT */
#define FUSES_ROOM_ADC_VAL_PTAT_Msk (_U_(0xFFF) << FUSES_ROOM_ADC_VAL_PTAT_Pos)
#define FUSES_ROOM_ADC_VAL_PTAT(value) (FUSES_ROOM_ADC_VAL_PTAT_Msk & ((value) << FUSES_ROOM_ADC_VAL_PTAT_Pos))

#define FUSES_ROOM_INT1V_VAL_ADDR   TEMP_LOG_ADDR
#define FUSES_ROOM_INT1V_VAL_Pos    24           /**< \brief (TEMP_LOG_ADDR) 2's complement of the internal 1V reference drift at room temperature (versus a 1.0 centered value) */
#define FUSES_ROOM_INT1V_VAL_Msk    (_U_(0xFF) << FUSES_ROOM_INT1V_VAL_Pos)
#define FUSES_ROOM_INT1V_VAL(value) (FUSES_ROOM_INT1V_VAL_Msk & ((value) << FUSES_ROOM_INT1V_VAL_Pos))

#define FUSES_ROOM_TEMP_VAL_DEC_ADDR TEMP_LOG_ADDR
#define FUSES_ROOM_TEMP_VAL_DEC_Pos 8            /**< \brief (TEMP_LOG_ADDR) Decimal part of room temperature */
#define FUSES_ROOM_TEMP_VAL_DEC_Msk (_U_(0xF) << FUSES_ROOM_TEMP_VAL_DEC_Pos)
#define FUSES_ROOM_TEMP_VAL_DEC(value) (FUSES_ROOM_TEMP_VAL_DEC_Msk & ((value) << FUSES_ROOM_TEMP_VAL_DEC_Pos))

#define FUSES_ROOM_TEMP_VAL_INT_ADDR TEMP_LOG_ADDR
#define FUSES_ROOM_TEMP_VAL_INT_Pos 0            /**< \brief (TEMP_LOG_ADDR) Integer part of room temperature in oC */
#define FUSES_ROOM_TEMP_VAL_INT_Msk (_U_(0xFF) << FUSES_ROOM_TEMP_VAL_INT_Pos)
#define FUSES_ROOM_TEMP_VAL_INT(value) (FUSES_ROOM_TEMP_VAL_INT_Msk & ((value) << FUSES_ROOM_TEMP_VAL_INT_Pos))

#define NVMCTRL_FUSES_BCREN_ADDR    (BOCOR_ADDR + 4)
#define NVMCTRL_FUSES_BCREN_Pos     17           /**< \brief (BOCOR_ADDR) Boot Configuration Read Enable */
#define NVMCTRL_FUSES_BCREN_Msk     (_U_(0x1) << NVMCTRL_FUSES_BCREN_Pos)

#define NVMCTRL_FUSES_BCWEN_ADDR    (BOCOR_ADDR + 4)
#define NVMCTRL_FUSES_BCWEN_Pos     16           /**< \brief (BOCOR_ADDR) Boot Configuration Write Enable */
#define NVMCTRL_FUSES_BCWEN_Msk     (_U_(0x1) << NVMCTRL_FUSES_BCWEN_Pos)

#define NVMCTRL_FUSES_NSULCK_ADDR   USER_PAGE_ADDR
#define NVMCTRL_FUSES_NSULCK_Pos    3            /**< \brief (USER_PAGE_ADDR) NVM Non-Secure Region Locks */
#define NVMCTRL_FUSES_NSULCK_Msk    (_U_(0x7) << NVMCTRL_FUSES_NSULCK_Pos)
#define NVMCTRL_FUSES_NSULCK(value) (NVMCTRL_FUSES_NSULCK_Msk & ((value) << NVMCTRL_FUSES_NSULCK_Pos))

#define NVMCTRL_FUSES_SULCK_ADDR    USER_PAGE_ADDR
#define NVMCTRL_FUSES_SULCK_Pos     0            /**< \brief (USER_PAGE_ADDR) NVM Secure Region Locks */
#define NVMCTRL_FUSES_SULCK_Msk     (_U_(0x7) << NVMCTRL_FUSES_SULCK_Pos)
#define NVMCTRL_FUSES_SULCK(value)  (NVMCTRL_FUSES_SULCK_Msk & ((value) << NVMCTRL_FUSES_SULCK_Pos))

#define NVMCTRL_FUSES_URWEN_ADDR    (USER_PAGE_ADDR + 12)
#define NVMCTRL_FUSES_URWEN_Pos     0            /**< \brief (USER_PAGE_ADDR) User Row Write Enable */
#define NVMCTRL_FUSES_URWEN_Msk     (_U_(0x1) << NVMCTRL_FUSES_URWEN_Pos)

#define WDT_FUSES_ALWAYSON_ADDR     USER_PAGE_ADDR
#define WDT_FUSES_ALWAYSON_Pos      27           /**< \brief (USER_PAGE_ADDR) WDT Always On */
#define WDT_FUSES_ALWAYSON_Msk      (_U_(0x1) << WDT_FUSES_ALWAYSON_Pos)

#define WDT_FUSES_ENABLE_ADDR       USER_PAGE_ADDR
#define WDT_FUSES_ENABLE_Pos        26           /**< \brief (USER_PAGE_ADDR) WDT Enable */
#define WDT_FUSES_ENABLE_Msk        (_U_(0x1) << WDT_FUSES_ENABLE_Pos)

#define WDT_FUSES_EWOFFSET_ADDR     (USER_PAGE_ADDR + 4)
#define WDT_FUSES_EWOFFSET_Pos      4            /**< \brief (USER_PAGE_ADDR) WDT Early Warning Offset */
#define WDT_FUSES_EWOFFSET_Msk      (_U_(0xF) << WDT_FUSES_EWOFFSET_Pos)
#define WDT_FUSES_EWOFFSET(value)   (WDT_FUSES_EWOFFSET_Msk & ((value) << WDT_FUSES_EWOFFSET_Pos))

#define WDT_FUSES_PER_ADDR          USER_PAGE_ADDR
#define WDT_FUSES_PER_Pos           28           /**< \brief (USER_PAGE_ADDR) WDT Period */
#define WDT_FUSES_PER_Msk           (_U_(0xF) << WDT_FUSES_PER_Pos)
#define WDT_FUSES_PER(value)        (WDT_FUSES_PER_Msk & ((value) << WDT_FUSES_PER_Pos))

#define WDT_FUSES_RUNSTDBY_ADDR     USER_PAGE_ADDR
#define WDT_FUSES_RUNSTDBY_Pos      25           /**< \brief (USER_PAGE_ADDR) WDT Run During Standby */
#define WDT_FUSES_RUNSTDBY_Msk      (_U_(0x1) << WDT_FUSES_RUNSTDBY_Pos)

#define WDT_FUSES_WEN_ADDR          (USER_PAGE_ADDR + 4)
#define WDT_FUSES_WEN_Pos           8            /**< \brief (USER_PAGE_ADDR) WDT Window Mode Enable */
#define WDT_FUSES_WEN_Msk           (_U_(0x1) << WDT_FUSES_WEN_Pos)

#define WDT_FUSES_WINDOW_ADDR       (USER_PAGE_ADDR + 4)
#define WDT_FUSES_WINDOW_Pos        0            /**< \brief (USER_PAGE_ADDR) WDT Window */
#define WDT_FUSES_WINDOW_Msk        (_U_(0xF) << WDT_FUSES_WINDOW_Pos)
#define WDT_FUSES_WINDOW(value)     (WDT_FUSES_WINDOW_Msk & ((value) << WDT_FUSES_WINDOW_Pos))

/** @}  end of Peripheral Software API */

#endif /* _SAML10_NVMCTRL_COMPONENT_H_ */
