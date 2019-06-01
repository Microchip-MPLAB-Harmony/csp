/**
 * \brief Component description for FPB
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
#ifndef _SAML10_FPB_COMPONENT_H_
#define _SAML10_FPB_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR FPB                                          */
/* ************************************************************************** */

/* -------- FPB_FP_CTRL : (FPB Offset: 0x00) (R/W 32) Flash Patch Control Register -------- */
#define FPB_FP_CTRL_ENABLE_Pos                _U_(0)                                         /**< (FPB_FP_CTRL) Flash Patch global enable Position */
#define FPB_FP_CTRL_ENABLE_Msk                (_U_(0x1) << FPB_FP_CTRL_ENABLE_Pos)           /**< (FPB_FP_CTRL) Flash Patch global enable Mask */
#define FPB_FP_CTRL_KEY_Pos                   _U_(1)                                         /**< (FPB_FP_CTRL) FP_CTRL write-enable key Position */
#define FPB_FP_CTRL_KEY_Msk                   (_U_(0x1) << FPB_FP_CTRL_KEY_Pos)              /**< (FPB_FP_CTRL) FP_CTRL write-enable key Mask */
#define FPB_FP_CTRL_NUM_CODE_Pos              _U_(4)                                         /**< (FPB_FP_CTRL) Number of implemented code comparators bits [3:0] Position */
#define FPB_FP_CTRL_NUM_CODE_Msk              (_U_(0xF) << FPB_FP_CTRL_NUM_CODE_Pos)         /**< (FPB_FP_CTRL) Number of implemented code comparators bits [3:0] Mask */
#define FPB_FP_CTRL_NUM_CODE(value)           (FPB_FP_CTRL_NUM_CODE_Msk & ((value) << FPB_FP_CTRL_NUM_CODE_Pos))
#define FPB_FP_CTRL_NUM_LIT_Pos               _U_(8)                                         /**< (FPB_FP_CTRL) Number of literal comparators Position */
#define FPB_FP_CTRL_NUM_LIT_Msk               (_U_(0xF) << FPB_FP_CTRL_NUM_LIT_Pos)          /**< (FPB_FP_CTRL) Number of literal comparators Mask */
#define FPB_FP_CTRL_NUM_LIT(value)            (FPB_FP_CTRL_NUM_LIT_Msk & ((value) << FPB_FP_CTRL_NUM_LIT_Pos))
#define FPB_FP_CTRL_NUM_CODE_1_Pos            _U_(12)                                        /**< (FPB_FP_CTRL) Number of implemented code comparators bits [6:4] Position */
#define FPB_FP_CTRL_NUM_CODE_1_Msk            (_U_(0x7) << FPB_FP_CTRL_NUM_CODE_1_Pos)       /**< (FPB_FP_CTRL) Number of implemented code comparators bits [6:4] Mask */
#define FPB_FP_CTRL_NUM_CODE_1(value)         (FPB_FP_CTRL_NUM_CODE_1_Msk & ((value) << FPB_FP_CTRL_NUM_CODE_1_Pos))
#define FPB_FP_CTRL_REV_Pos                   _U_(28)                                        /**< (FPB_FP_CTRL) Revision Position */
#define FPB_FP_CTRL_REV_Msk                   (_U_(0xF) << FPB_FP_CTRL_REV_Pos)              /**< (FPB_FP_CTRL) Revision Mask */
#define FPB_FP_CTRL_REV(value)                (FPB_FP_CTRL_REV_Msk & ((value) << FPB_FP_CTRL_REV_Pos))
#define FPB_FP_CTRL_Msk                       _U_(0xF0007FF3)                                /**< (FPB_FP_CTRL) Register Mask  */


/* -------- FPB_FP_REMAP : (FPB Offset: 0x04) ( R/ 32) Flash Patch Remap Register -------- */
#define FPB_FP_REMAP_REMAP_Pos                _U_(5)                                         /**< (FPB_FP_REMAP) Remap address Position */
#define FPB_FP_REMAP_REMAP_Msk                (_U_(0xFFFFFF) << FPB_FP_REMAP_REMAP_Pos)      /**< (FPB_FP_REMAP) Remap address Mask */
#define FPB_FP_REMAP_REMAP(value)             (FPB_FP_REMAP_REMAP_Msk & ((value) << FPB_FP_REMAP_REMAP_Pos))
#define FPB_FP_REMAP_RMPSPT_Pos               _U_(29)                                        /**< (FPB_FP_REMAP) Remap supported Position */
#define FPB_FP_REMAP_RMPSPT_Msk               (_U_(0x1) << FPB_FP_REMAP_RMPSPT_Pos)          /**< (FPB_FP_REMAP) Remap supported Mask */
#define FPB_FP_REMAP_Msk                      _U_(0x3FFFFFE0)                                /**< (FPB_FP_REMAP) Register Mask  */


/* -------- FPB_FP_COMP : (FPB Offset: 0x08) (R/W 32) Flash Patch Comparator Register n -------- */
#define FPB_FP_COMP_BE_Pos                    _U_(0)                                         /**< (FPB_FP_COMP) Breakpoint enable Position */
#define FPB_FP_COMP_BE_Msk                    (_U_(0x1) << FPB_FP_COMP_BE_Pos)               /**< (FPB_FP_COMP) Breakpoint enable Mask */
#define FPB_FP_COMP_FPADDR_Pos                _U_(2)                                         /**< (FPB_FP_COMP) Flash Patch address Position */
#define FPB_FP_COMP_FPADDR_Msk                (_U_(0x7FFFFFF) << FPB_FP_COMP_FPADDR_Pos)     /**< (FPB_FP_COMP) Flash Patch address Mask */
#define FPB_FP_COMP_FPADDR(value)             (FPB_FP_COMP_FPADDR_Msk & ((value) << FPB_FP_COMP_FPADDR_Pos))
#define FPB_FP_COMP_FE_Pos                    _U_(31)                                        /**< (FPB_FP_COMP) Flash Patch enable Position */
#define FPB_FP_COMP_FE_Msk                    (_U_(0x1) << FPB_FP_COMP_FE_Pos)               /**< (FPB_FP_COMP) Flash Patch enable Mask */
#define FPB_FP_COMP_Msk                       _U_(0x9FFFFFFD)                                /**< (FPB_FP_COMP) Register Mask  */

/* BREAKPOINT mode */
#define FPB_FP_COMP_BREAKPOINT_BPADDR_Pos     _U_(1)                                         /**< (FPB_FP_COMP) Breakpoint address Position */
#define FPB_FP_COMP_BREAKPOINT_BPADDR_Msk     (_U_(0x7FFFFFFF) << FPB_FP_COMP_BREAKPOINT_BPADDR_Pos) /**< (FPB_FP_COMP) Breakpoint address Mask */
#define FPB_FP_COMP_BREAKPOINT_BPADDR(value)  (FPB_FP_COMP_BREAKPOINT_BPADDR_Msk & ((value) << FPB_FP_COMP_BREAKPOINT_BPADDR_Pos))
#define FPB_FP_COMP_BREAKPOINT_Msk          _U_(0xFFFFFFFE)                                 /**< (FPB_FP_COMP_BREAKPOINT) Register Mask  */


/* -------- FPB_FP_LAR : (FPB Offset: 0xFB0) ( /W 32) FPB Software Lock Access Register -------- */
#define FPB_FP_LAR_KEY_Pos                    _U_(0)                                         /**< (FPB_FP_LAR) Lock access control Position */
#define FPB_FP_LAR_KEY_Msk                    (_U_(0xFFFFFFFF) << FPB_FP_LAR_KEY_Pos)        /**< (FPB_FP_LAR) Lock access control Mask */
#define FPB_FP_LAR_KEY(value)                 (FPB_FP_LAR_KEY_Msk & ((value) << FPB_FP_LAR_KEY_Pos))
#define   FPB_FP_LAR_KEY_UNLOCK_Val           _U_(0xC5ACCE55)                                /**< (FPB_FP_LAR) Unlock key value  */
#define FPB_FP_LAR_KEY_UNLOCK                 (FPB_FP_LAR_KEY_UNLOCK_Val << FPB_FP_LAR_KEY_Pos) /**< (FPB_FP_LAR) Unlock key value Position  */
#define FPB_FP_LAR_Msk                        _U_(0xFFFFFFFF)                                /**< (FPB_FP_LAR) Register Mask  */


/* -------- FPB_FP_LSR : (FPB Offset: 0xFB4) ( R/ 32) FPB Software Lock Status Register -------- */
#define FPB_FP_LSR_SLI_Pos                    _U_(0)                                         /**< (FPB_FP_LSR) Software Lock implemented Position */
#define FPB_FP_LSR_SLI_Msk                    (_U_(0x1) << FPB_FP_LSR_SLI_Pos)               /**< (FPB_FP_LSR) Software Lock implemented Mask */
#define FPB_FP_LSR_SLK_Pos                    _U_(1)                                         /**< (FPB_FP_LSR) Software Lock status Position */
#define FPB_FP_LSR_SLK_Msk                    (_U_(0x1) << FPB_FP_LSR_SLK_Pos)               /**< (FPB_FP_LSR) Software Lock status Mask */
#define FPB_FP_LSR_nTT_Pos                    _U_(2)                                         /**< (FPB_FP_LSR) Not thirty-two bit Position */
#define FPB_FP_LSR_nTT_Msk                    (_U_(0x1) << FPB_FP_LSR_nTT_Pos)               /**< (FPB_FP_LSR) Not thirty-two bit Mask */
#define FPB_FP_LSR_Msk                        _U_(0x00000007)                                /**< (FPB_FP_LSR) Register Mask  */


/* -------- FPB_FP_DEVARCH : (FPB Offset: 0xFBC) ( R/ 32) FPB Device Architecture Register -------- */
#define FPB_FP_DEVARCH_RESETVALUE           _U_(0x47701A03)                               /**<  (FPB_FP_DEVARCH) FPB Device Architecture Register  Reset Value */

#define FPB_FP_DEVARCH_ARCHPART_Pos           _U_(0)                                         /**< (FPB_FP_DEVARCH) Architecture Part Position */
#define FPB_FP_DEVARCH_ARCHPART_Msk           (_U_(0xFFF) << FPB_FP_DEVARCH_ARCHPART_Pos)    /**< (FPB_FP_DEVARCH) Architecture Part Mask */
#define FPB_FP_DEVARCH_ARCHPART(value)        (FPB_FP_DEVARCH_ARCHPART_Msk & ((value) << FPB_FP_DEVARCH_ARCHPART_Pos))
#define FPB_FP_DEVARCH_ARCHVER_Pos            _U_(12)                                        /**< (FPB_FP_DEVARCH) Architecture Version Position */
#define FPB_FP_DEVARCH_ARCHVER_Msk            (_U_(0xF) << FPB_FP_DEVARCH_ARCHVER_Pos)       /**< (FPB_FP_DEVARCH) Architecture Version Mask */
#define FPB_FP_DEVARCH_ARCHVER(value)         (FPB_FP_DEVARCH_ARCHVER_Msk & ((value) << FPB_FP_DEVARCH_ARCHVER_Pos))
#define FPB_FP_DEVARCH_REVISION_Pos           _U_(16)                                        /**< (FPB_FP_DEVARCH) Revision Position */
#define FPB_FP_DEVARCH_REVISION_Msk           (_U_(0xF) << FPB_FP_DEVARCH_REVISION_Pos)      /**< (FPB_FP_DEVARCH) Revision Mask */
#define FPB_FP_DEVARCH_REVISION(value)        (FPB_FP_DEVARCH_REVISION_Msk & ((value) << FPB_FP_DEVARCH_REVISION_Pos))
#define FPB_FP_DEVARCH_PRESENT_Pos            _U_(20)                                        /**< (FPB_FP_DEVARCH) DEVARCH Present Position */
#define FPB_FP_DEVARCH_PRESENT_Msk            (_U_(0x1) << FPB_FP_DEVARCH_PRESENT_Pos)       /**< (FPB_FP_DEVARCH) DEVARCH Present Mask */
#define FPB_FP_DEVARCH_ARCHITECT_Pos          _U_(21)                                        /**< (FPB_FP_DEVARCH) Architect Position */
#define FPB_FP_DEVARCH_ARCHITECT_Msk          (_U_(0x7FF) << FPB_FP_DEVARCH_ARCHITECT_Pos)   /**< (FPB_FP_DEVARCH) Architect Mask */
#define FPB_FP_DEVARCH_ARCHITECT(value)       (FPB_FP_DEVARCH_ARCHITECT_Msk & ((value) << FPB_FP_DEVARCH_ARCHITECT_Pos))
#define FPB_FP_DEVARCH_Msk                    _U_(0xFFFFFFFF)                                /**< (FPB_FP_DEVARCH) Register Mask  */


/* -------- FPB_FP_DEVTYPE : (FPB Offset: 0xFCC) ( R/ 32) FPB Device Type Register -------- */
#define FPB_FP_DEVTYPE_RESETVALUE           _U_(0x00)                                     /**<  (FPB_FP_DEVTYPE) FPB Device Type Register  Reset Value */

#define FPB_FP_DEVTYPE_MAJOR_Pos              _U_(0)                                         /**< (FPB_FP_DEVTYPE) Major type Position */
#define FPB_FP_DEVTYPE_MAJOR_Msk              (_U_(0xF) << FPB_FP_DEVTYPE_MAJOR_Pos)         /**< (FPB_FP_DEVTYPE) Major type Mask */
#define FPB_FP_DEVTYPE_MAJOR(value)           (FPB_FP_DEVTYPE_MAJOR_Msk & ((value) << FPB_FP_DEVTYPE_MAJOR_Pos))
#define FPB_FP_DEVTYPE_SUB_Pos                _U_(4)                                         /**< (FPB_FP_DEVTYPE) Sub-type Position */
#define FPB_FP_DEVTYPE_SUB_Msk                (_U_(0xF) << FPB_FP_DEVTYPE_SUB_Pos)           /**< (FPB_FP_DEVTYPE) Sub-type Mask */
#define FPB_FP_DEVTYPE_SUB(value)             (FPB_FP_DEVTYPE_SUB_Msk & ((value) << FPB_FP_DEVTYPE_SUB_Pos))
#define FPB_FP_DEVTYPE_Msk                    _U_(0x000000FF)                                /**< (FPB_FP_DEVTYPE) Register Mask  */


/* -------- FPB_FP_PIDR4 : (FPB Offset: 0xFD0) ( R/ 32) FP Peripheral Identification Register 4 -------- */
#define FPB_FP_PIDR4_DES_2_Pos                _U_(0)                                         /**< (FPB_FP_PIDR4) JEP106 continuation code Position */
#define FPB_FP_PIDR4_DES_2_Msk                (_U_(0xF) << FPB_FP_PIDR4_DES_2_Pos)           /**< (FPB_FP_PIDR4) JEP106 continuation code Mask */
#define FPB_FP_PIDR4_DES_2(value)             (FPB_FP_PIDR4_DES_2_Msk & ((value) << FPB_FP_PIDR4_DES_2_Pos))
#define FPB_FP_PIDR4_SIZE_Pos                 _U_(4)                                         /**< (FPB_FP_PIDR4) 4KB count Position */
#define FPB_FP_PIDR4_SIZE_Msk                 (_U_(0xF) << FPB_FP_PIDR4_SIZE_Pos)            /**< (FPB_FP_PIDR4) 4KB count Mask */
#define FPB_FP_PIDR4_SIZE(value)              (FPB_FP_PIDR4_SIZE_Msk & ((value) << FPB_FP_PIDR4_SIZE_Pos))
#define FPB_FP_PIDR4_Msk                      _U_(0x000000FF)                                /**< (FPB_FP_PIDR4) Register Mask  */


/* -------- FPB_FP_PIDR5 : (FPB Offset: 0xFD4) ( R/ 32) FP Peripheral Identification Register 5 -------- */
#define FPB_FP_PIDR5_RESETVALUE             _U_(0x00)                                     /**<  (FPB_FP_PIDR5) FP Peripheral Identification Register 5  Reset Value */

#define FPB_FP_PIDR5_Msk                      _U_(0x00000000)                                /**< (FPB_FP_PIDR5) Register Mask  */


/* -------- FPB_FP_PIDR6 : (FPB Offset: 0xFD8) ( R/ 32) FP Peripheral Identification Register 6 -------- */
#define FPB_FP_PIDR6_RESETVALUE             _U_(0x00)                                     /**<  (FPB_FP_PIDR6) FP Peripheral Identification Register 6  Reset Value */

#define FPB_FP_PIDR6_Msk                      _U_(0x00000000)                                /**< (FPB_FP_PIDR6) Register Mask  */


/* -------- FPB_FP_PIDR7 : (FPB Offset: 0xFDC) ( R/ 32) FP Peripheral Identification Register 7 -------- */
#define FPB_FP_PIDR7_RESETVALUE             _U_(0x00)                                     /**<  (FPB_FP_PIDR7) FP Peripheral Identification Register 7  Reset Value */

#define FPB_FP_PIDR7_Msk                      _U_(0x00000000)                                /**< (FPB_FP_PIDR7) Register Mask  */


/* -------- FPB_FP_PIDR0 : (FPB Offset: 0xFE0) ( R/ 32) FP Peripheral Identification Register 0 -------- */
#define FPB_FP_PIDR0_PART_0_Pos               _U_(0)                                         /**< (FPB_FP_PIDR0) Part number bits[7:0] Position */
#define FPB_FP_PIDR0_PART_0_Msk               (_U_(0xFF) << FPB_FP_PIDR0_PART_0_Pos)         /**< (FPB_FP_PIDR0) Part number bits[7:0] Mask */
#define FPB_FP_PIDR0_PART_0(value)            (FPB_FP_PIDR0_PART_0_Msk & ((value) << FPB_FP_PIDR0_PART_0_Pos))
#define FPB_FP_PIDR0_Msk                      _U_(0x000000FF)                                /**< (FPB_FP_PIDR0) Register Mask  */


/* -------- FPB_FP_PIDR1 : (FPB Offset: 0xFE4) ( R/ 32) FP Peripheral Identification Register 1 -------- */
#define FPB_FP_PIDR1_PART_1_Pos               _U_(0)                                         /**< (FPB_FP_PIDR1) Part number bits[11:8] Position */
#define FPB_FP_PIDR1_PART_1_Msk               (_U_(0xF) << FPB_FP_PIDR1_PART_1_Pos)          /**< (FPB_FP_PIDR1) Part number bits[11:8] Mask */
#define FPB_FP_PIDR1_PART_1(value)            (FPB_FP_PIDR1_PART_1_Msk & ((value) << FPB_FP_PIDR1_PART_1_Pos))
#define FPB_FP_PIDR1_DES_0_Pos                _U_(4)                                         /**< (FPB_FP_PIDR1) JEP106 identification code bits [3:0] Position */
#define FPB_FP_PIDR1_DES_0_Msk                (_U_(0xF) << FPB_FP_PIDR1_DES_0_Pos)           /**< (FPB_FP_PIDR1) JEP106 identification code bits [3:0] Mask */
#define FPB_FP_PIDR1_DES_0(value)             (FPB_FP_PIDR1_DES_0_Msk & ((value) << FPB_FP_PIDR1_DES_0_Pos))
#define FPB_FP_PIDR1_Msk                      _U_(0x000000FF)                                /**< (FPB_FP_PIDR1) Register Mask  */


/* -------- FPB_FP_PIDR2 : (FPB Offset: 0xFE8) ( R/ 32) FP Peripheral Identification Register 2 -------- */
#define FPB_FP_PIDR2_DES_1_Pos                _U_(0)                                         /**< (FPB_FP_PIDR2) JEP106 identification code bits[6:4] Position */
#define FPB_FP_PIDR2_DES_1_Msk                (_U_(0x7) << FPB_FP_PIDR2_DES_1_Pos)           /**< (FPB_FP_PIDR2) JEP106 identification code bits[6:4] Mask */
#define FPB_FP_PIDR2_DES_1(value)             (FPB_FP_PIDR2_DES_1_Msk & ((value) << FPB_FP_PIDR2_DES_1_Pos))
#define FPB_FP_PIDR2_JEDEC_Pos                _U_(3)                                         /**< (FPB_FP_PIDR2) JEDEC assignee value is used Position */
#define FPB_FP_PIDR2_JEDEC_Msk                (_U_(0x1) << FPB_FP_PIDR2_JEDEC_Pos)           /**< (FPB_FP_PIDR2) JEDEC assignee value is used Mask */
#define FPB_FP_PIDR2_REVISION_Pos             _U_(4)                                         /**< (FPB_FP_PIDR2) Component revision Position */
#define FPB_FP_PIDR2_REVISION_Msk             (_U_(0xF) << FPB_FP_PIDR2_REVISION_Pos)        /**< (FPB_FP_PIDR2) Component revision Mask */
#define FPB_FP_PIDR2_REVISION(value)          (FPB_FP_PIDR2_REVISION_Msk & ((value) << FPB_FP_PIDR2_REVISION_Pos))
#define FPB_FP_PIDR2_Msk                      _U_(0x000000FF)                                /**< (FPB_FP_PIDR2) Register Mask  */


/* -------- FPB_FP_PIDR3 : (FPB Offset: 0xFEC) ( R/ 32) FP Peripheral Identification Register 3 -------- */
#define FPB_FP_PIDR3_CMOD_Pos                 _U_(0)                                         /**< (FPB_FP_PIDR3) Customer Modified Position */
#define FPB_FP_PIDR3_CMOD_Msk                 (_U_(0xF) << FPB_FP_PIDR3_CMOD_Pos)            /**< (FPB_FP_PIDR3) Customer Modified Mask */
#define FPB_FP_PIDR3_CMOD(value)              (FPB_FP_PIDR3_CMOD_Msk & ((value) << FPB_FP_PIDR3_CMOD_Pos))
#define FPB_FP_PIDR3_REVAND_Pos               _U_(4)                                         /**< (FPB_FP_PIDR3) RevAnd Position */
#define FPB_FP_PIDR3_REVAND_Msk               (_U_(0xF) << FPB_FP_PIDR3_REVAND_Pos)          /**< (FPB_FP_PIDR3) RevAnd Mask */
#define FPB_FP_PIDR3_REVAND(value)            (FPB_FP_PIDR3_REVAND_Msk & ((value) << FPB_FP_PIDR3_REVAND_Pos))
#define FPB_FP_PIDR3_Msk                      _U_(0x000000FF)                                /**< (FPB_FP_PIDR3) Register Mask  */


/* -------- FPB_FP_CIDR0 : (FPB Offset: 0xFF0) ( R/ 32) FP Component Identification Register 0 -------- */
#define FPB_FP_CIDR0_RESETVALUE             _U_(0x0D)                                     /**<  (FPB_FP_CIDR0) FP Component Identification Register 0  Reset Value */

#define FPB_FP_CIDR0_PRMBL_0_Pos              _U_(0)                                         /**< (FPB_FP_CIDR0) CoreSight component identification preamble Position */
#define FPB_FP_CIDR0_PRMBL_0_Msk              (_U_(0xFF) << FPB_FP_CIDR0_PRMBL_0_Pos)        /**< (FPB_FP_CIDR0) CoreSight component identification preamble Mask */
#define FPB_FP_CIDR0_PRMBL_0(value)           (FPB_FP_CIDR0_PRMBL_0_Msk & ((value) << FPB_FP_CIDR0_PRMBL_0_Pos))
#define FPB_FP_CIDR0_Msk                      _U_(0x000000FF)                                /**< (FPB_FP_CIDR0) Register Mask  */


/* -------- FPB_FP_CIDR1 : (FPB Offset: 0xFF4) ( R/ 32) FP Component Identification Register 1 -------- */
#define FPB_FP_CIDR1_RESETVALUE             _U_(0x90)                                     /**<  (FPB_FP_CIDR1) FP Component Identification Register 1  Reset Value */

#define FPB_FP_CIDR1_PRMBL_1_Pos              _U_(0)                                         /**< (FPB_FP_CIDR1) CoreSight component identification preamble Position */
#define FPB_FP_CIDR1_PRMBL_1_Msk              (_U_(0xF) << FPB_FP_CIDR1_PRMBL_1_Pos)         /**< (FPB_FP_CIDR1) CoreSight component identification preamble Mask */
#define FPB_FP_CIDR1_PRMBL_1(value)           (FPB_FP_CIDR1_PRMBL_1_Msk & ((value) << FPB_FP_CIDR1_PRMBL_1_Pos))
#define FPB_FP_CIDR1_CLASS_Pos                _U_(4)                                         /**< (FPB_FP_CIDR1) CoreSight component class Position */
#define FPB_FP_CIDR1_CLASS_Msk                (_U_(0xF) << FPB_FP_CIDR1_CLASS_Pos)           /**< (FPB_FP_CIDR1) CoreSight component class Mask */
#define FPB_FP_CIDR1_CLASS(value)             (FPB_FP_CIDR1_CLASS_Msk & ((value) << FPB_FP_CIDR1_CLASS_Pos))
#define FPB_FP_CIDR1_Msk                      _U_(0x000000FF)                                /**< (FPB_FP_CIDR1) Register Mask  */


/* -------- FPB_FP_CIDR2 : (FPB Offset: 0xFF8) ( R/ 32) FP Component Identification Register 2 -------- */
#define FPB_FP_CIDR2_RESETVALUE             _U_(0x05)                                     /**<  (FPB_FP_CIDR2) FP Component Identification Register 2  Reset Value */

#define FPB_FP_CIDR2_PRMBL_2_Pos              _U_(0)                                         /**< (FPB_FP_CIDR2) CoreSight component identification preamble Position */
#define FPB_FP_CIDR2_PRMBL_2_Msk              (_U_(0xFF) << FPB_FP_CIDR2_PRMBL_2_Pos)        /**< (FPB_FP_CIDR2) CoreSight component identification preamble Mask */
#define FPB_FP_CIDR2_PRMBL_2(value)           (FPB_FP_CIDR2_PRMBL_2_Msk & ((value) << FPB_FP_CIDR2_PRMBL_2_Pos))
#define FPB_FP_CIDR2_Msk                      _U_(0x000000FF)                                /**< (FPB_FP_CIDR2) Register Mask  */


/* -------- FPB_FP_CIDR3 : (FPB Offset: 0xFFC) ( R/ 32) FP Component Identification Register 3 -------- */
#define FPB_FP_CIDR3_RESETVALUE             _U_(0xB1)                                     /**<  (FPB_FP_CIDR3) FP Component Identification Register 3  Reset Value */

#define FPB_FP_CIDR3_PRMBL_3_Pos              _U_(0)                                         /**< (FPB_FP_CIDR3) CoreSight component identification preamble Position */
#define FPB_FP_CIDR3_PRMBL_3_Msk              (_U_(0xFF) << FPB_FP_CIDR3_PRMBL_3_Pos)        /**< (FPB_FP_CIDR3) CoreSight component identification preamble Mask */
#define FPB_FP_CIDR3_PRMBL_3(value)           (FPB_FP_CIDR3_PRMBL_3_Msk & ((value) << FPB_FP_CIDR3_PRMBL_3_Pos))
#define FPB_FP_CIDR3_Msk                      _U_(0x000000FF)                                /**< (FPB_FP_CIDR3) Register Mask  */


/** \brief FPB register offsets definitions */
#define FPB_FP_CTRL_REG_OFST           (0x00)         /**< (FPB_FP_CTRL) Flash Patch Control Register Offset */
#define FPB_FP_REMAP_REG_OFST          (0x04)         /**< (FPB_FP_REMAP) Flash Patch Remap Register Offset */
#define FPB_FP_COMP_REG_OFST           (0x08)         /**< (FPB_FP_COMP) Flash Patch Comparator Register n Offset */
#define FPB_FP_LAR_REG_OFST            (0xFB0)        /**< (FPB_FP_LAR) FPB Software Lock Access Register Offset */
#define FPB_FP_LSR_REG_OFST            (0xFB4)        /**< (FPB_FP_LSR) FPB Software Lock Status Register Offset */
#define FPB_FP_DEVARCH_REG_OFST        (0xFBC)        /**< (FPB_FP_DEVARCH) FPB Device Architecture Register Offset */
#define FPB_FP_DEVTYPE_REG_OFST        (0xFCC)        /**< (FPB_FP_DEVTYPE) FPB Device Type Register Offset */
#define FPB_FP_PIDR4_REG_OFST          (0xFD0)        /**< (FPB_FP_PIDR4) FP Peripheral Identification Register 4 Offset */
#define FPB_FP_PIDR5_REG_OFST          (0xFD4)        /**< (FPB_FP_PIDR5) FP Peripheral Identification Register 5 Offset */
#define FPB_FP_PIDR6_REG_OFST          (0xFD8)        /**< (FPB_FP_PIDR6) FP Peripheral Identification Register 6 Offset */
#define FPB_FP_PIDR7_REG_OFST          (0xFDC)        /**< (FPB_FP_PIDR7) FP Peripheral Identification Register 7 Offset */
#define FPB_FP_PIDR0_REG_OFST          (0xFE0)        /**< (FPB_FP_PIDR0) FP Peripheral Identification Register 0 Offset */
#define FPB_FP_PIDR1_REG_OFST          (0xFE4)        /**< (FPB_FP_PIDR1) FP Peripheral Identification Register 1 Offset */
#define FPB_FP_PIDR2_REG_OFST          (0xFE8)        /**< (FPB_FP_PIDR2) FP Peripheral Identification Register 2 Offset */
#define FPB_FP_PIDR3_REG_OFST          (0xFEC)        /**< (FPB_FP_PIDR3) FP Peripheral Identification Register 3 Offset */
#define FPB_FP_CIDR0_REG_OFST          (0xFF0)        /**< (FPB_FP_CIDR0) FP Component Identification Register 0 Offset */
#define FPB_FP_CIDR1_REG_OFST          (0xFF4)        /**< (FPB_FP_CIDR1) FP Component Identification Register 1 Offset */
#define FPB_FP_CIDR2_REG_OFST          (0xFF8)        /**< (FPB_FP_CIDR2) FP Component Identification Register 2 Offset */
#define FPB_FP_CIDR3_REG_OFST          (0xFFC)        /**< (FPB_FP_CIDR3) FP Component Identification Register 3 Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief FPB register API structure */
typedef struct
{  /* Flash Patch and Breakpoint */
  __IO  uint32_t                       FPB_FP_CTRL;     /**< Offset: 0x00 (R/W  32) Flash Patch Control Register */
  __I   uint32_t                       FPB_FP_REMAP;    /**< Offset: 0x04 (R/   32) Flash Patch Remap Register */
  __IO  uint32_t                       FPB_FP_COMP[4];  /**< Offset: 0x08 (R/W  32) Flash Patch Comparator Register n */
  __I   uint8_t                        Reserved1[0xF98];
  __O   uint32_t                       FPB_FP_LAR;      /**< Offset: 0xFB0 ( /W  32) FPB Software Lock Access Register */
  __I   uint32_t                       FPB_FP_LSR;      /**< Offset: 0xFB4 (R/   32) FPB Software Lock Status Register */
  __I   uint8_t                        Reserved2[0x04];
  __I   uint32_t                       FPB_FP_DEVARCH;  /**< Offset: 0xFBC (R/   32) FPB Device Architecture Register */
  __I   uint8_t                        Reserved3[0x0C];
  __I   uint32_t                       FPB_FP_DEVTYPE;  /**< Offset: 0xFCC (R/   32) FPB Device Type Register */
  __I   uint32_t                       FPB_FP_PIDR4;    /**< Offset: 0xFD0 (R/   32) FP Peripheral Identification Register 4 */
  __I   uint32_t                       FPB_FP_PIDR5;    /**< Offset: 0xFD4 (R/   32) FP Peripheral Identification Register 5 */
  __I   uint32_t                       FPB_FP_PIDR6;    /**< Offset: 0xFD8 (R/   32) FP Peripheral Identification Register 6 */
  __I   uint32_t                       FPB_FP_PIDR7;    /**< Offset: 0xFDC (R/   32) FP Peripheral Identification Register 7 */
  __I   uint32_t                       FPB_FP_PIDR0;    /**< Offset: 0xFE0 (R/   32) FP Peripheral Identification Register 0 */
  __I   uint32_t                       FPB_FP_PIDR1;    /**< Offset: 0xFE4 (R/   32) FP Peripheral Identification Register 1 */
  __I   uint32_t                       FPB_FP_PIDR2;    /**< Offset: 0xFE8 (R/   32) FP Peripheral Identification Register 2 */
  __I   uint32_t                       FPB_FP_PIDR3;    /**< Offset: 0xFEC (R/   32) FP Peripheral Identification Register 3 */
  __I   uint32_t                       FPB_FP_CIDR0;    /**< Offset: 0xFF0 (R/   32) FP Component Identification Register 0 */
  __I   uint32_t                       FPB_FP_CIDR1;    /**< Offset: 0xFF4 (R/   32) FP Component Identification Register 1 */
  __I   uint32_t                       FPB_FP_CIDR2;    /**< Offset: 0xFF8 (R/   32) FP Component Identification Register 2 */
  __I   uint32_t                       FPB_FP_CIDR3;    /**< Offset: 0xFFC (R/   32) FP Component Identification Register 3 */
} fpb_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAML10_FPB_COMPONENT_H_ */
