/**
 * \brief Component description for DIB
 *
 * © 2019 Microchip Technology Inc. and its subsidiaries.
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

/* file generated from device description version 2019-05-31T10:20:47Z */
#ifndef _SAML10_DIB_COMPONENT_H_
#define _SAML10_DIB_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR DIB                                          */
/* ************************************************************************** */

/* -------- DIB_DLAR : (DIB Offset: 0x00) ( /W 32) SCS Software Lock Access Register -------- */
#define DIB_DLAR_KEY_Pos                      _U_(0)                                         /**< (DIB_DLAR) Lock access control Position */
#define DIB_DLAR_KEY_Msk                      (_U_(0xFFFFFFFF) << DIB_DLAR_KEY_Pos)          /**< (DIB_DLAR) Lock access control Mask */
#define DIB_DLAR_KEY(value)                   (DIB_DLAR_KEY_Msk & ((value) << DIB_DLAR_KEY_Pos))
#define   DIB_DLAR_KEY_UNLOCK_Val             _U_(0xC5ACCE55)                                /**< (DIB_DLAR) Unlock key value  */
#define DIB_DLAR_KEY_UNLOCK                   (DIB_DLAR_KEY_UNLOCK_Val << DIB_DLAR_KEY_Pos)  /**< (DIB_DLAR) Unlock key value Position  */
#define DIB_DLAR_Msk                          _U_(0xFFFFFFFF)                                /**< (DIB_DLAR) Register Mask  */


/* -------- DIB_DLSR : (DIB Offset: 0x04) ( R/ 32) SCS Software Lock Status Register -------- */
#define DIB_DLSR_SLI_Pos                      _U_(0)                                         /**< (DIB_DLSR) Software Lock implemented Position */
#define DIB_DLSR_SLI_Msk                      (_U_(0x1) << DIB_DLSR_SLI_Pos)                 /**< (DIB_DLSR) Software Lock implemented Mask */
#define DIB_DLSR_SLK_Pos                      _U_(1)                                         /**< (DIB_DLSR) Software Lock status Position */
#define DIB_DLSR_SLK_Msk                      (_U_(0x1) << DIB_DLSR_SLK_Pos)                 /**< (DIB_DLSR) Software Lock status Mask */
#define DIB_DLSR_nTT_Pos                      _U_(2)                                         /**< (DIB_DLSR) Not thirty-two bit Position */
#define DIB_DLSR_nTT_Msk                      (_U_(0x1) << DIB_DLSR_nTT_Pos)                 /**< (DIB_DLSR) Not thirty-two bit Mask */
#define DIB_DLSR_Msk                          _U_(0x00000007)                                /**< (DIB_DLSR) Register Mask  */


/* -------- DIB_DAUTHSTATUS : (DIB Offset: 0x08) ( R/ 32) Debug Authentication Status Register -------- */
#define DIB_DAUTHSTATUS_SID_Pos               _U_(4)                                         /**< (DIB_DAUTHSTATUS)  Position */
#define DIB_DAUTHSTATUS_SID_Msk               (_U_(0x3) << DIB_DAUTHSTATUS_SID_Pos)          /**< (DIB_DAUTHSTATUS)  Mask */
#define DIB_DAUTHSTATUS_SID(value)            (DIB_DAUTHSTATUS_SID_Msk & ((value) << DIB_DAUTHSTATUS_SID_Pos))
#define   DIB_DAUTHSTATUS_SID_NOSEC_Val       _U_(0x0)                                       /**< (DIB_DAUTHSTATUS) Security Extension not implemented  */
#define   DIB_DAUTHSTATUS_SID_NO_Val          _U_(0x2)                                       /**< (DIB_DAUTHSTATUS) Secure invasive debug prohibited  */
#define   DIB_DAUTHSTATUS_SID_YES_Val         _U_(0x3)                                       /**< (DIB_DAUTHSTATUS) Secure invasive debug allowed  */
#define DIB_DAUTHSTATUS_SID_NOSEC             (DIB_DAUTHSTATUS_SID_NOSEC_Val << DIB_DAUTHSTATUS_SID_Pos) /**< (DIB_DAUTHSTATUS) Security Extension not implemented Position  */
#define DIB_DAUTHSTATUS_SID_NO                (DIB_DAUTHSTATUS_SID_NO_Val << DIB_DAUTHSTATUS_SID_Pos) /**< (DIB_DAUTHSTATUS) Secure invasive debug prohibited Position  */
#define DIB_DAUTHSTATUS_SID_YES               (DIB_DAUTHSTATUS_SID_YES_Val << DIB_DAUTHSTATUS_SID_Pos) /**< (DIB_DAUTHSTATUS) Secure invasive debug allowed Position  */
#define DIB_DAUTHSTATUS_SNID_Pos              _U_(6)                                         /**< (DIB_DAUTHSTATUS)  Position */
#define DIB_DAUTHSTATUS_SNID_Msk              (_U_(0x3) << DIB_DAUTHSTATUS_SNID_Pos)         /**< (DIB_DAUTHSTATUS)  Mask */
#define DIB_DAUTHSTATUS_SNID(value)           (DIB_DAUTHSTATUS_SNID_Msk & ((value) << DIB_DAUTHSTATUS_SNID_Pos))
#define   DIB_DAUTHSTATUS_SNID_NOSEC_Val      _U_(0x0)                                       /**< (DIB_DAUTHSTATUS) Security Extension not implemented  */
#define   DIB_DAUTHSTATUS_SNID_NO_Val         _U_(0x2)                                       /**< (DIB_DAUTHSTATUS) Secure non-invasive debug prohibited  */
#define   DIB_DAUTHSTATUS_SNID_YES_Val        _U_(0x3)                                       /**< (DIB_DAUTHSTATUS) Secure non-invasive debug allowed  */
#define DIB_DAUTHSTATUS_SNID_NOSEC            (DIB_DAUTHSTATUS_SNID_NOSEC_Val << DIB_DAUTHSTATUS_SNID_Pos) /**< (DIB_DAUTHSTATUS) Security Extension not implemented Position  */
#define DIB_DAUTHSTATUS_SNID_NO               (DIB_DAUTHSTATUS_SNID_NO_Val << DIB_DAUTHSTATUS_SNID_Pos) /**< (DIB_DAUTHSTATUS) Secure non-invasive debug prohibited Position  */
#define DIB_DAUTHSTATUS_SNID_YES              (DIB_DAUTHSTATUS_SNID_YES_Val << DIB_DAUTHSTATUS_SNID_Pos) /**< (DIB_DAUTHSTATUS) Secure non-invasive debug allowed Position  */
#define DIB_DAUTHSTATUS_Msk                   _U_(0x000000F0)                                /**< (DIB_DAUTHSTATUS) Register Mask  */


/* -------- DIB_DDEVARCH : (DIB Offset: 0x0C) ( R/ 32) SCS Device Architecture Register -------- */
#define DIB_DDEVARCH_RESETVALUE             _U_(0x47702A04)                               /**<  (DIB_DDEVARCH) SCS Device Architecture Register  Reset Value */

#define DIB_DDEVARCH_ARCHPART_Pos             _U_(0)                                         /**< (DIB_DDEVARCH) Architecture Part Position */
#define DIB_DDEVARCH_ARCHPART_Msk             (_U_(0xFFF) << DIB_DDEVARCH_ARCHPART_Pos)      /**< (DIB_DDEVARCH) Architecture Part Mask */
#define DIB_DDEVARCH_ARCHPART(value)          (DIB_DDEVARCH_ARCHPART_Msk & ((value) << DIB_DDEVARCH_ARCHPART_Pos))
#define DIB_DDEVARCH_ARCHVER_Pos              _U_(12)                                        /**< (DIB_DDEVARCH) Architecture Version Position */
#define DIB_DDEVARCH_ARCHVER_Msk              (_U_(0xF) << DIB_DDEVARCH_ARCHVER_Pos)         /**< (DIB_DDEVARCH) Architecture Version Mask */
#define DIB_DDEVARCH_ARCHVER(value)           (DIB_DDEVARCH_ARCHVER_Msk & ((value) << DIB_DDEVARCH_ARCHVER_Pos))
#define DIB_DDEVARCH_REVISION_Pos             _U_(16)                                        /**< (DIB_DDEVARCH) Revision Position */
#define DIB_DDEVARCH_REVISION_Msk             (_U_(0xF) << DIB_DDEVARCH_REVISION_Pos)        /**< (DIB_DDEVARCH) Revision Mask */
#define DIB_DDEVARCH_REVISION(value)          (DIB_DDEVARCH_REVISION_Msk & ((value) << DIB_DDEVARCH_REVISION_Pos))
#define DIB_DDEVARCH_PRESENT_Pos              _U_(20)                                        /**< (DIB_DDEVARCH) DEVARCH Present Position */
#define DIB_DDEVARCH_PRESENT_Msk              (_U_(0x1) << DIB_DDEVARCH_PRESENT_Pos)         /**< (DIB_DDEVARCH) DEVARCH Present Mask */
#define DIB_DDEVARCH_ARCHITECT_Pos            _U_(21)                                        /**< (DIB_DDEVARCH) Architect Position */
#define DIB_DDEVARCH_ARCHITECT_Msk            (_U_(0x7FF) << DIB_DDEVARCH_ARCHITECT_Pos)     /**< (DIB_DDEVARCH) Architect Mask */
#define DIB_DDEVARCH_ARCHITECT(value)         (DIB_DDEVARCH_ARCHITECT_Msk & ((value) << DIB_DDEVARCH_ARCHITECT_Pos))
#define DIB_DDEVARCH_Msk                      _U_(0xFFFFFFFF)                                /**< (DIB_DDEVARCH) Register Mask  */


/* -------- DIB_DDEVTYPE : (DIB Offset: 0x1C) ( R/ 32) SCS Device Type Register -------- */
#define DIB_DDEVTYPE_RESETVALUE             _U_(0x00)                                     /**<  (DIB_DDEVTYPE) SCS Device Type Register  Reset Value */

#define DIB_DDEVTYPE_MAJOR_Pos                _U_(0)                                         /**< (DIB_DDEVTYPE) Major type Position */
#define DIB_DDEVTYPE_MAJOR_Msk                (_U_(0xF) << DIB_DDEVTYPE_MAJOR_Pos)           /**< (DIB_DDEVTYPE) Major type Mask */
#define DIB_DDEVTYPE_MAJOR(value)             (DIB_DDEVTYPE_MAJOR_Msk & ((value) << DIB_DDEVTYPE_MAJOR_Pos))
#define DIB_DDEVTYPE_SUB_Pos                  _U_(4)                                         /**< (DIB_DDEVTYPE) Sub-type Position */
#define DIB_DDEVTYPE_SUB_Msk                  (_U_(0xF) << DIB_DDEVTYPE_SUB_Pos)             /**< (DIB_DDEVTYPE) Sub-type Mask */
#define DIB_DDEVTYPE_SUB(value)               (DIB_DDEVTYPE_SUB_Msk & ((value) << DIB_DDEVTYPE_SUB_Pos))
#define DIB_DDEVTYPE_Msk                      _U_(0x000000FF)                                /**< (DIB_DDEVTYPE) Register Mask  */


/* -------- DIB_DPIDR4 : (DIB Offset: 0x20) ( R/ 32) SCS Peripheral Identification Register 4 -------- */
#define DIB_DPIDR4_DES_2_Pos                  _U_(0)                                         /**< (DIB_DPIDR4) JEP106 continuation code Position */
#define DIB_DPIDR4_DES_2_Msk                  (_U_(0xF) << DIB_DPIDR4_DES_2_Pos)             /**< (DIB_DPIDR4) JEP106 continuation code Mask */
#define DIB_DPIDR4_DES_2(value)               (DIB_DPIDR4_DES_2_Msk & ((value) << DIB_DPIDR4_DES_2_Pos))
#define DIB_DPIDR4_SIZE_Pos                   _U_(4)                                         /**< (DIB_DPIDR4) 4KB count Position */
#define DIB_DPIDR4_SIZE_Msk                   (_U_(0xF) << DIB_DPIDR4_SIZE_Pos)              /**< (DIB_DPIDR4) 4KB count Mask */
#define DIB_DPIDR4_SIZE(value)                (DIB_DPIDR4_SIZE_Msk & ((value) << DIB_DPIDR4_SIZE_Pos))
#define DIB_DPIDR4_Msk                        _U_(0x000000FF)                                /**< (DIB_DPIDR4) Register Mask  */


/* -------- DIB_DPIDR5 : (DIB Offset: 0x24) ( R/ 32) SCS Peripheral Identification Register 5 -------- */
#define DIB_DPIDR5_RESETVALUE               _U_(0x00)                                     /**<  (DIB_DPIDR5) SCS Peripheral Identification Register 5  Reset Value */

#define DIB_DPIDR5_Msk                        _U_(0x00000000)                                /**< (DIB_DPIDR5) Register Mask  */


/* -------- DIB_DPIDR6 : (DIB Offset: 0x28) ( R/ 32) SCS Peripheral Identification Register 6 -------- */
#define DIB_DPIDR6_RESETVALUE               _U_(0x00)                                     /**<  (DIB_DPIDR6) SCS Peripheral Identification Register 6  Reset Value */

#define DIB_DPIDR6_Msk                        _U_(0x00000000)                                /**< (DIB_DPIDR6) Register Mask  */


/* -------- DIB_DPIDR7 : (DIB Offset: 0x2C) ( R/ 32) SCS Peripheral Identification Register 7 -------- */
#define DIB_DPIDR7_RESETVALUE               _U_(0x00)                                     /**<  (DIB_DPIDR7) SCS Peripheral Identification Register 7  Reset Value */

#define DIB_DPIDR7_Msk                        _U_(0x00000000)                                /**< (DIB_DPIDR7) Register Mask  */


/* -------- DIB_DPIDR0 : (DIB Offset: 0x30) ( R/ 32) SCS Peripheral Identification Register 0 -------- */
#define DIB_DPIDR0_PART_0_Pos                 _U_(0)                                         /**< (DIB_DPIDR0) Part number bits[7:0] Position */
#define DIB_DPIDR0_PART_0_Msk                 (_U_(0xFF) << DIB_DPIDR0_PART_0_Pos)           /**< (DIB_DPIDR0) Part number bits[7:0] Mask */
#define DIB_DPIDR0_PART_0(value)              (DIB_DPIDR0_PART_0_Msk & ((value) << DIB_DPIDR0_PART_0_Pos))
#define DIB_DPIDR0_Msk                        _U_(0x000000FF)                                /**< (DIB_DPIDR0) Register Mask  */


/* -------- DIB_DPIDR1 : (DIB Offset: 0x34) ( R/ 32) SCS Peripheral Identification Register 1 -------- */
#define DIB_DPIDR1_PART_1_Pos                 _U_(0)                                         /**< (DIB_DPIDR1) Part number bits[11:8] Position */
#define DIB_DPIDR1_PART_1_Msk                 (_U_(0xF) << DIB_DPIDR1_PART_1_Pos)            /**< (DIB_DPIDR1) Part number bits[11:8] Mask */
#define DIB_DPIDR1_PART_1(value)              (DIB_DPIDR1_PART_1_Msk & ((value) << DIB_DPIDR1_PART_1_Pos))
#define DIB_DPIDR1_DES_0_Pos                  _U_(4)                                         /**< (DIB_DPIDR1) JEP106 identification code bits [3:0] Position */
#define DIB_DPIDR1_DES_0_Msk                  (_U_(0xF) << DIB_DPIDR1_DES_0_Pos)             /**< (DIB_DPIDR1) JEP106 identification code bits [3:0] Mask */
#define DIB_DPIDR1_DES_0(value)               (DIB_DPIDR1_DES_0_Msk & ((value) << DIB_DPIDR1_DES_0_Pos))
#define DIB_DPIDR1_Msk                        _U_(0x000000FF)                                /**< (DIB_DPIDR1) Register Mask  */


/* -------- DIB_DPIDR2 : (DIB Offset: 0x38) ( R/ 32) SCS Peripheral Identification Register 2 -------- */
#define DIB_DPIDR2_DES_1_Pos                  _U_(0)                                         /**< (DIB_DPIDR2) JEP106 identification code bits[6:4] Position */
#define DIB_DPIDR2_DES_1_Msk                  (_U_(0x7) << DIB_DPIDR2_DES_1_Pos)             /**< (DIB_DPIDR2) JEP106 identification code bits[6:4] Mask */
#define DIB_DPIDR2_DES_1(value)               (DIB_DPIDR2_DES_1_Msk & ((value) << DIB_DPIDR2_DES_1_Pos))
#define DIB_DPIDR2_JEDEC_Pos                  _U_(3)                                         /**< (DIB_DPIDR2) JEDEC assignee value is used Position */
#define DIB_DPIDR2_JEDEC_Msk                  (_U_(0x1) << DIB_DPIDR2_JEDEC_Pos)             /**< (DIB_DPIDR2) JEDEC assignee value is used Mask */
#define DIB_DPIDR2_REVISION_Pos               _U_(4)                                         /**< (DIB_DPIDR2) Component revision Position */
#define DIB_DPIDR2_REVISION_Msk               (_U_(0xF) << DIB_DPIDR2_REVISION_Pos)          /**< (DIB_DPIDR2) Component revision Mask */
#define DIB_DPIDR2_REVISION(value)            (DIB_DPIDR2_REVISION_Msk & ((value) << DIB_DPIDR2_REVISION_Pos))
#define DIB_DPIDR2_Msk                        _U_(0x000000FF)                                /**< (DIB_DPIDR2) Register Mask  */


/* -------- DIB_DPIDR3 : (DIB Offset: 0x3C) ( R/ 32) SCS Peripheral Identification Register 3 -------- */
#define DIB_DPIDR3_CMOD_Pos                   _U_(0)                                         /**< (DIB_DPIDR3) Customer Modified Position */
#define DIB_DPIDR3_CMOD_Msk                   (_U_(0xF) << DIB_DPIDR3_CMOD_Pos)              /**< (DIB_DPIDR3) Customer Modified Mask */
#define DIB_DPIDR3_CMOD(value)                (DIB_DPIDR3_CMOD_Msk & ((value) << DIB_DPIDR3_CMOD_Pos))
#define DIB_DPIDR3_REVAND_Pos                 _U_(4)                                         /**< (DIB_DPIDR3) RevAnd Position */
#define DIB_DPIDR3_REVAND_Msk                 (_U_(0xF) << DIB_DPIDR3_REVAND_Pos)            /**< (DIB_DPIDR3) RevAnd Mask */
#define DIB_DPIDR3_REVAND(value)              (DIB_DPIDR3_REVAND_Msk & ((value) << DIB_DPIDR3_REVAND_Pos))
#define DIB_DPIDR3_Msk                        _U_(0x000000FF)                                /**< (DIB_DPIDR3) Register Mask  */


/* -------- DIB_DCIDR0 : (DIB Offset: 0x40) ( R/ 32) SCS Component Identification Register 0 -------- */
#define DIB_DCIDR0_RESETVALUE               _U_(0x0D)                                     /**<  (DIB_DCIDR0) SCS Component Identification Register 0  Reset Value */

#define DIB_DCIDR0_PRMBL_0_Pos                _U_(0)                                         /**< (DIB_DCIDR0) CoreSight component identification preamble Position */
#define DIB_DCIDR0_PRMBL_0_Msk                (_U_(0xFF) << DIB_DCIDR0_PRMBL_0_Pos)          /**< (DIB_DCIDR0) CoreSight component identification preamble Mask */
#define DIB_DCIDR0_PRMBL_0(value)             (DIB_DCIDR0_PRMBL_0_Msk & ((value) << DIB_DCIDR0_PRMBL_0_Pos))
#define DIB_DCIDR0_Msk                        _U_(0x000000FF)                                /**< (DIB_DCIDR0) Register Mask  */


/* -------- DIB_DCIDR1 : (DIB Offset: 0x44) ( R/ 32) SCS Component Identification Register 1 -------- */
#define DIB_DCIDR1_RESETVALUE               _U_(0x90)                                     /**<  (DIB_DCIDR1) SCS Component Identification Register 1  Reset Value */

#define DIB_DCIDR1_PRMBL_1_Pos                _U_(0)                                         /**< (DIB_DCIDR1) CoreSight component identification preamble Position */
#define DIB_DCIDR1_PRMBL_1_Msk                (_U_(0xF) << DIB_DCIDR1_PRMBL_1_Pos)           /**< (DIB_DCIDR1) CoreSight component identification preamble Mask */
#define DIB_DCIDR1_PRMBL_1(value)             (DIB_DCIDR1_PRMBL_1_Msk & ((value) << DIB_DCIDR1_PRMBL_1_Pos))
#define DIB_DCIDR1_CLASS_Pos                  _U_(4)                                         /**< (DIB_DCIDR1) CoreSight component class Position */
#define DIB_DCIDR1_CLASS_Msk                  (_U_(0xF) << DIB_DCIDR1_CLASS_Pos)             /**< (DIB_DCIDR1) CoreSight component class Mask */
#define DIB_DCIDR1_CLASS(value)               (DIB_DCIDR1_CLASS_Msk & ((value) << DIB_DCIDR1_CLASS_Pos))
#define DIB_DCIDR1_Msk                        _U_(0x000000FF)                                /**< (DIB_DCIDR1) Register Mask  */


/* -------- DIB_DCIDR2 : (DIB Offset: 0x48) ( R/ 32) SCS Component Identification Register 2 -------- */
#define DIB_DCIDR2_RESETVALUE               _U_(0x05)                                     /**<  (DIB_DCIDR2) SCS Component Identification Register 2  Reset Value */

#define DIB_DCIDR2_PRMBL_2_Pos                _U_(0)                                         /**< (DIB_DCIDR2) CoreSight component identification preamble Position */
#define DIB_DCIDR2_PRMBL_2_Msk                (_U_(0xFF) << DIB_DCIDR2_PRMBL_2_Pos)          /**< (DIB_DCIDR2) CoreSight component identification preamble Mask */
#define DIB_DCIDR2_PRMBL_2(value)             (DIB_DCIDR2_PRMBL_2_Msk & ((value) << DIB_DCIDR2_PRMBL_2_Pos))
#define DIB_DCIDR2_Msk                        _U_(0x000000FF)                                /**< (DIB_DCIDR2) Register Mask  */


/* -------- DIB_DCIDR3 : (DIB Offset: 0x4C) ( R/ 32) SCS Component Identification Register 3 -------- */
#define DIB_DCIDR3_RESETVALUE               _U_(0xB1)                                     /**<  (DIB_DCIDR3) SCS Component Identification Register 3  Reset Value */

#define DIB_DCIDR3_PRMBL_3_Pos                _U_(0)                                         /**< (DIB_DCIDR3) CoreSight component identification preamble Position */
#define DIB_DCIDR3_PRMBL_3_Msk                (_U_(0xFF) << DIB_DCIDR3_PRMBL_3_Pos)          /**< (DIB_DCIDR3) CoreSight component identification preamble Mask */
#define DIB_DCIDR3_PRMBL_3(value)             (DIB_DCIDR3_PRMBL_3_Msk & ((value) << DIB_DCIDR3_PRMBL_3_Pos))
#define DIB_DCIDR3_Msk                        _U_(0x000000FF)                                /**< (DIB_DCIDR3) Register Mask  */


/** \brief DIB register offsets definitions */
#define DIB_DLAR_REG_OFST              (0x00)         /**< (DIB_DLAR) SCS Software Lock Access Register Offset */
#define DIB_DLSR_REG_OFST              (0x04)         /**< (DIB_DLSR) SCS Software Lock Status Register Offset */
#define DIB_DAUTHSTATUS_REG_OFST       (0x08)         /**< (DIB_DAUTHSTATUS) Debug Authentication Status Register Offset */
#define DIB_DDEVARCH_REG_OFST          (0x0C)         /**< (DIB_DDEVARCH) SCS Device Architecture Register Offset */
#define DIB_DDEVTYPE_REG_OFST          (0x1C)         /**< (DIB_DDEVTYPE) SCS Device Type Register Offset */
#define DIB_DPIDR4_REG_OFST            (0x20)         /**< (DIB_DPIDR4) SCS Peripheral Identification Register 4 Offset */
#define DIB_DPIDR5_REG_OFST            (0x24)         /**< (DIB_DPIDR5) SCS Peripheral Identification Register 5 Offset */
#define DIB_DPIDR6_REG_OFST            (0x28)         /**< (DIB_DPIDR6) SCS Peripheral Identification Register 6 Offset */
#define DIB_DPIDR7_REG_OFST            (0x2C)         /**< (DIB_DPIDR7) SCS Peripheral Identification Register 7 Offset */
#define DIB_DPIDR0_REG_OFST            (0x30)         /**< (DIB_DPIDR0) SCS Peripheral Identification Register 0 Offset */
#define DIB_DPIDR1_REG_OFST            (0x34)         /**< (DIB_DPIDR1) SCS Peripheral Identification Register 1 Offset */
#define DIB_DPIDR2_REG_OFST            (0x38)         /**< (DIB_DPIDR2) SCS Peripheral Identification Register 2 Offset */
#define DIB_DPIDR3_REG_OFST            (0x3C)         /**< (DIB_DPIDR3) SCS Peripheral Identification Register 3 Offset */
#define DIB_DCIDR0_REG_OFST            (0x40)         /**< (DIB_DCIDR0) SCS Component Identification Register 0 Offset */
#define DIB_DCIDR1_REG_OFST            (0x44)         /**< (DIB_DCIDR1) SCS Component Identification Register 1 Offset */
#define DIB_DCIDR2_REG_OFST            (0x48)         /**< (DIB_DCIDR2) SCS Component Identification Register 2 Offset */
#define DIB_DCIDR3_REG_OFST            (0x4C)         /**< (DIB_DCIDR3) SCS Component Identification Register 3 Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief DIB register API structure */
typedef struct
{  /* Debug Identification Block */
  __O   uint32_t                       DIB_DLAR;        /**< Offset: 0x00 ( /W  32) SCS Software Lock Access Register */
  __I   uint32_t                       DIB_DLSR;        /**< Offset: 0x04 (R/   32) SCS Software Lock Status Register */
  __I   uint32_t                       DIB_DAUTHSTATUS; /**< Offset: 0x08 (R/   32) Debug Authentication Status Register */
  __I   uint32_t                       DIB_DDEVARCH;    /**< Offset: 0x0C (R/   32) SCS Device Architecture Register */
  __I   uint8_t                        Reserved1[0x0C];
  __I   uint32_t                       DIB_DDEVTYPE;    /**< Offset: 0x1C (R/   32) SCS Device Type Register */
  __I   uint32_t                       DIB_DPIDR4;      /**< Offset: 0x20 (R/   32) SCS Peripheral Identification Register 4 */
  __I   uint32_t                       DIB_DPIDR5;      /**< Offset: 0x24 (R/   32) SCS Peripheral Identification Register 5 */
  __I   uint32_t                       DIB_DPIDR6;      /**< Offset: 0x28 (R/   32) SCS Peripheral Identification Register 6 */
  __I   uint32_t                       DIB_DPIDR7;      /**< Offset: 0x2C (R/   32) SCS Peripheral Identification Register 7 */
  __I   uint32_t                       DIB_DPIDR0;      /**< Offset: 0x30 (R/   32) SCS Peripheral Identification Register 0 */
  __I   uint32_t                       DIB_DPIDR1;      /**< Offset: 0x34 (R/   32) SCS Peripheral Identification Register 1 */
  __I   uint32_t                       DIB_DPIDR2;      /**< Offset: 0x38 (R/   32) SCS Peripheral Identification Register 2 */
  __I   uint32_t                       DIB_DPIDR3;      /**< Offset: 0x3C (R/   32) SCS Peripheral Identification Register 3 */
  __I   uint32_t                       DIB_DCIDR0;      /**< Offset: 0x40 (R/   32) SCS Component Identification Register 0 */
  __I   uint32_t                       DIB_DCIDR1;      /**< Offset: 0x44 (R/   32) SCS Component Identification Register 1 */
  __I   uint32_t                       DIB_DCIDR2;      /**< Offset: 0x48 (R/   32) SCS Component Identification Register 2 */
  __I   uint32_t                       DIB_DCIDR3;      /**< Offset: 0x4C (R/   32) SCS Component Identification Register 3 */
} dib_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAML10_DIB_COMPONENT_H_ */
