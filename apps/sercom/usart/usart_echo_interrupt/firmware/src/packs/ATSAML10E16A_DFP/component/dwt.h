/**
 * \brief Component description for DWT
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
#ifndef _SAML10_DWT_COMPONENT_H_
#define _SAML10_DWT_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR DWT                                          */
/* ************************************************************************** */

/* -------- DWT_COMP : (DWT Offset: 0x00) (R/W 32) DWT Comparator Register n -------- */
#define DWT_COMP_VALUE_Pos                    _U_(0)                                         /**< (DWT_COMP) Cycle/PC/data value or data address Position */
#define DWT_COMP_VALUE_Msk                    (_U_(0xFFFFFFFF) << DWT_COMP_VALUE_Pos)        /**< (DWT_COMP) Cycle/PC/data value or data address Mask */
#define DWT_COMP_VALUE(value)                 (DWT_COMP_VALUE_Msk & ((value) << DWT_COMP_VALUE_Pos))
#define DWT_COMP_Msk                          _U_(0xFFFFFFFF)                                /**< (DWT_COMP) Register Mask  */


/* -------- DWT_FUNCTION : (DWT Offset: 0x08) (R/W 32) DWT Function Register x -------- */
#define DWT_FUNCTION_MATCH_Pos                _U_(0)                                         /**< (DWT_FUNCTION) Match type Position */
#define DWT_FUNCTION_MATCH_Msk                (_U_(0xF) << DWT_FUNCTION_MATCH_Pos)           /**< (DWT_FUNCTION) Match type Mask */
#define DWT_FUNCTION_MATCH(value)             (DWT_FUNCTION_MATCH_Msk & ((value) << DWT_FUNCTION_MATCH_Pos))
#define DWT_FUNCTION_ACTION_Pos               _U_(4)                                         /**< (DWT_FUNCTION) Action on match Position */
#define DWT_FUNCTION_ACTION_Msk               (_U_(0x3) << DWT_FUNCTION_ACTION_Pos)          /**< (DWT_FUNCTION) Action on match Mask */
#define DWT_FUNCTION_ACTION(value)            (DWT_FUNCTION_ACTION_Msk & ((value) << DWT_FUNCTION_ACTION_Pos))
#define DWT_FUNCTION_DATAVSIZE_Pos            _U_(10)                                        /**< (DWT_FUNCTION) Data value size Position */
#define DWT_FUNCTION_DATAVSIZE_Msk            (_U_(0x3) << DWT_FUNCTION_DATAVSIZE_Pos)       /**< (DWT_FUNCTION) Data value size Mask */
#define DWT_FUNCTION_DATAVSIZE(value)         (DWT_FUNCTION_DATAVSIZE_Msk & ((value) << DWT_FUNCTION_DATAVSIZE_Pos))
#define DWT_FUNCTION_MATCHED_Pos              _U_(24)                                        /**< (DWT_FUNCTION) Comparator matched Position */
#define DWT_FUNCTION_MATCHED_Msk              (_U_(0x1) << DWT_FUNCTION_MATCHED_Pos)         /**< (DWT_FUNCTION) Comparator matched Mask */
#define DWT_FUNCTION_ID_Pos                   _U_(27)                                        /**< (DWT_FUNCTION) Identify capability Position */
#define DWT_FUNCTION_ID_Msk                   (_U_(0x1F) << DWT_FUNCTION_ID_Pos)             /**< (DWT_FUNCTION) Identify capability Mask */
#define DWT_FUNCTION_ID(value)                (DWT_FUNCTION_ID_Msk & ((value) << DWT_FUNCTION_ID_Pos))
#define DWT_FUNCTION_Msk                      _U_(0xF9000C3F)                                /**< (DWT_FUNCTION) Register Mask  */


/* -------- DWT_CTRL : (DWT Offset: 0x00) (R/W 32) DWT Control Register -------- */
#define DWT_CTRL_RESETVALUE                 _U_(0xB000000)                                /**<  (DWT_CTRL) DWT Control Register  Reset Value */

#define DWT_CTRL_CYCCNTENA_Pos                _U_(0)                                         /**< (DWT_CTRL) CYCCNT enable Position */
#define DWT_CTRL_CYCCNTENA_Msk                (_U_(0x1) << DWT_CTRL_CYCCNTENA_Pos)           /**< (DWT_CTRL) CYCCNT enable Mask */
#define DWT_CTRL_POSTPRESET_Pos               _U_(1)                                         /**< (DWT_CTRL) POSTCNT preset Position */
#define DWT_CTRL_POSTPRESET_Msk               (_U_(0xF) << DWT_CTRL_POSTPRESET_Pos)          /**< (DWT_CTRL) POSTCNT preset Mask */
#define DWT_CTRL_POSTPRESET(value)            (DWT_CTRL_POSTPRESET_Msk & ((value) << DWT_CTRL_POSTPRESET_Pos))
#define DWT_CTRL_POSTINIT_Pos                 _U_(5)                                         /**< (DWT_CTRL) POSTCNT initial Position */
#define DWT_CTRL_POSTINIT_Msk                 (_U_(0xF) << DWT_CTRL_POSTINIT_Pos)            /**< (DWT_CTRL) POSTCNT initial Mask */
#define DWT_CTRL_POSTINIT(value)              (DWT_CTRL_POSTINIT_Msk & ((value) << DWT_CTRL_POSTINIT_Pos))
#define DWT_CTRL_CYCTAP_Pos                   _U_(9)                                         /**< (DWT_CTRL) Cycle count tap Position */
#define DWT_CTRL_CYCTAP_Msk                   (_U_(0x1) << DWT_CTRL_CYCTAP_Pos)              /**< (DWT_CTRL) Cycle count tap Mask */
#define DWT_CTRL_SYNCTAP_Pos                  _U_(10)                                        /**< (DWT_CTRL) Synchronization tap Position */
#define DWT_CTRL_SYNCTAP_Msk                  (_U_(0x3) << DWT_CTRL_SYNCTAP_Pos)             /**< (DWT_CTRL) Synchronization tap Mask */
#define DWT_CTRL_SYNCTAP(value)               (DWT_CTRL_SYNCTAP_Msk & ((value) << DWT_CTRL_SYNCTAP_Pos))
#define DWT_CTRL_PCSAMPLENA_Pos               _U_(12)                                        /**< (DWT_CTRL) PC sample enable Position */
#define DWT_CTRL_PCSAMPLENA_Msk               (_U_(0x1) << DWT_CTRL_PCSAMPLENA_Pos)          /**< (DWT_CTRL) PC sample enable Mask */
#define DWT_CTRL_EXCTRCENA_Pos                _U_(16)                                        /**< (DWT_CTRL) Exception trace enable Position */
#define DWT_CTRL_EXCTRCENA_Msk                (_U_(0x1) << DWT_CTRL_EXCTRCENA_Pos)           /**< (DWT_CTRL) Exception trace enable Mask */
#define DWT_CTRL_CPIEVTENA_Pos                _U_(17)                                        /**< (DWT_CTRL) CPI event enable Position */
#define DWT_CTRL_CPIEVTENA_Msk                (_U_(0x1) << DWT_CTRL_CPIEVTENA_Pos)           /**< (DWT_CTRL) CPI event enable Mask */
#define DWT_CTRL_EXCEVTENA_Pos                _U_(18)                                        /**< (DWT_CTRL) Exception event enable Position */
#define DWT_CTRL_EXCEVTENA_Msk                (_U_(0x1) << DWT_CTRL_EXCEVTENA_Pos)           /**< (DWT_CTRL) Exception event enable Mask */
#define DWT_CTRL_SLEEPEVTENA_Pos              _U_(19)                                        /**< (DWT_CTRL) Sleep event enable Position */
#define DWT_CTRL_SLEEPEVTENA_Msk              (_U_(0x1) << DWT_CTRL_SLEEPEVTENA_Pos)         /**< (DWT_CTRL) Sleep event enable Mask */
#define DWT_CTRL_LSUEVTENA_Pos                _U_(20)                                        /**< (DWT_CTRL) LSU event enable Position */
#define DWT_CTRL_LSUEVTENA_Msk                (_U_(0x1) << DWT_CTRL_LSUEVTENA_Pos)           /**< (DWT_CTRL) LSU event enable Mask */
#define DWT_CTRL_FOLDEVTENA_Pos               _U_(21)                                        /**< (DWT_CTRL) Fold event enable Position */
#define DWT_CTRL_FOLDEVTENA_Msk               (_U_(0x1) << DWT_CTRL_FOLDEVTENA_Pos)          /**< (DWT_CTRL) Fold event enable Mask */
#define DWT_CTRL_CYCEVTENA_Pos                _U_(22)                                        /**< (DWT_CTRL) Cycle event enable Position */
#define DWT_CTRL_CYCEVTENA_Msk                (_U_(0x1) << DWT_CTRL_CYCEVTENA_Pos)           /**< (DWT_CTRL) Cycle event enable Mask */
#define DWT_CTRL_CYCDISS_Pos                  _U_(23)                                        /**< (DWT_CTRL) Cycle counter disabled secure Position */
#define DWT_CTRL_CYCDISS_Msk                  (_U_(0x1) << DWT_CTRL_CYCDISS_Pos)             /**< (DWT_CTRL) Cycle counter disabled secure Mask */
#define DWT_CTRL_NOPRFCNT_Pos                 _U_(24)                                        /**< (DWT_CTRL) No profile counters Position */
#define DWT_CTRL_NOPRFCNT_Msk                 (_U_(0x1) << DWT_CTRL_NOPRFCNT_Pos)            /**< (DWT_CTRL) No profile counters Mask */
#define DWT_CTRL_NOCYCCNT_Pos                 _U_(25)                                        /**< (DWT_CTRL) No cycle count Position */
#define DWT_CTRL_NOCYCCNT_Msk                 (_U_(0x1) << DWT_CTRL_NOCYCCNT_Pos)            /**< (DWT_CTRL) No cycle count Mask */
#define DWT_CTRL_NOEXTTRIG_Pos                _U_(26)                                        /**< (DWT_CTRL) No external triggers Position */
#define DWT_CTRL_NOEXTTRIG_Msk                (_U_(0x1) << DWT_CTRL_NOEXTTRIG_Pos)           /**< (DWT_CTRL) No external triggers Mask */
#define DWT_CTRL_NOTRCPKT_Pos                 _U_(27)                                        /**< (DWT_CTRL) No trace packets Position */
#define DWT_CTRL_NOTRCPKT_Msk                 (_U_(0x1) << DWT_CTRL_NOTRCPKT_Pos)            /**< (DWT_CTRL) No trace packets Mask */
#define DWT_CTRL_NUMCOMP_Pos                  _U_(28)                                        /**< (DWT_CTRL) Number of comparators Position */
#define DWT_CTRL_NUMCOMP_Msk                  (_U_(0xF) << DWT_CTRL_NUMCOMP_Pos)             /**< (DWT_CTRL) Number of comparators Mask */
#define DWT_CTRL_NUMCOMP(value)               (DWT_CTRL_NUMCOMP_Msk & ((value) << DWT_CTRL_NUMCOMP_Pos))
#define DWT_CTRL_Msk                          _U_(0xFFFF1FFF)                                /**< (DWT_CTRL) Register Mask  */


/* -------- DWT_PCSR : (DWT Offset: 0x1C) ( R/ 32) DWT Program Counter Sample Register -------- */
#define DWT_PCSR_EIASAMPLE_Pos                _U_(0)                                         /**< (DWT_PCSR) Executed instruction address sample Position */
#define DWT_PCSR_EIASAMPLE_Msk                (_U_(0xFFFFFFFF) << DWT_PCSR_EIASAMPLE_Pos)    /**< (DWT_PCSR) Executed instruction address sample Mask */
#define DWT_PCSR_EIASAMPLE(value)             (DWT_PCSR_EIASAMPLE_Msk & ((value) << DWT_PCSR_EIASAMPLE_Pos))
#define DWT_PCSR_Msk                          _U_(0xFFFFFFFF)                                /**< (DWT_PCSR) Register Mask  */


/* -------- DWT_LAR : (DWT Offset: 0xFB0) ( /W 32) DWT Software Lock Access Register -------- */
#define DWT_LAR_KEY_Pos                       _U_(0)                                         /**< (DWT_LAR) Lock access control Position */
#define DWT_LAR_KEY_Msk                       (_U_(0xFFFFFFFF) << DWT_LAR_KEY_Pos)           /**< (DWT_LAR) Lock access control Mask */
#define DWT_LAR_KEY(value)                    (DWT_LAR_KEY_Msk & ((value) << DWT_LAR_KEY_Pos))
#define   DWT_LAR_KEY_UNLOCK_Val              _U_(0xC5ACCE55)                                /**< (DWT_LAR) Unlock key value  */
#define DWT_LAR_KEY_UNLOCK                    (DWT_LAR_KEY_UNLOCK_Val << DWT_LAR_KEY_Pos)    /**< (DWT_LAR) Unlock key value Position  */
#define DWT_LAR_Msk                           _U_(0xFFFFFFFF)                                /**< (DWT_LAR) Register Mask  */


/* -------- DWT_LSR : (DWT Offset: 0xFB4) ( R/ 32) DWT Software Lock Status Register -------- */
#define DWT_LSR_SLI_Pos                       _U_(0)                                         /**< (DWT_LSR) Software Lock implemented Position */
#define DWT_LSR_SLI_Msk                       (_U_(0x1) << DWT_LSR_SLI_Pos)                  /**< (DWT_LSR) Software Lock implemented Mask */
#define DWT_LSR_SLK_Pos                       _U_(1)                                         /**< (DWT_LSR) Software Lock status Position */
#define DWT_LSR_SLK_Msk                       (_U_(0x1) << DWT_LSR_SLK_Pos)                  /**< (DWT_LSR) Software Lock status Mask */
#define DWT_LSR_nTT_Pos                       _U_(2)                                         /**< (DWT_LSR) Not thirty-two bit Position */
#define DWT_LSR_nTT_Msk                       (_U_(0x1) << DWT_LSR_nTT_Pos)                  /**< (DWT_LSR) Not thirty-two bit Mask */
#define DWT_LSR_Msk                           _U_(0x00000007)                                /**< (DWT_LSR) Register Mask  */


/* -------- DWT_DEVARCH : (DWT Offset: 0xFBC) ( R/ 32) DWT Device Architecture Register -------- */
#define DWT_DEVARCH_RESETVALUE              _U_(0x47701A02)                               /**<  (DWT_DEVARCH) DWT Device Architecture Register  Reset Value */

#define DWT_DEVARCH_ARCHPART_Pos              _U_(0)                                         /**< (DWT_DEVARCH) Architecture Part Position */
#define DWT_DEVARCH_ARCHPART_Msk              (_U_(0xFFF) << DWT_DEVARCH_ARCHPART_Pos)       /**< (DWT_DEVARCH) Architecture Part Mask */
#define DWT_DEVARCH_ARCHPART(value)           (DWT_DEVARCH_ARCHPART_Msk & ((value) << DWT_DEVARCH_ARCHPART_Pos))
#define DWT_DEVARCH_ARCHVER_Pos               _U_(12)                                        /**< (DWT_DEVARCH) Architecture Version Position */
#define DWT_DEVARCH_ARCHVER_Msk               (_U_(0xF) << DWT_DEVARCH_ARCHVER_Pos)          /**< (DWT_DEVARCH) Architecture Version Mask */
#define DWT_DEVARCH_ARCHVER(value)            (DWT_DEVARCH_ARCHVER_Msk & ((value) << DWT_DEVARCH_ARCHVER_Pos))
#define DWT_DEVARCH_REVISION_Pos              _U_(16)                                        /**< (DWT_DEVARCH) Revision Position */
#define DWT_DEVARCH_REVISION_Msk              (_U_(0xF) << DWT_DEVARCH_REVISION_Pos)         /**< (DWT_DEVARCH) Revision Mask */
#define DWT_DEVARCH_REVISION(value)           (DWT_DEVARCH_REVISION_Msk & ((value) << DWT_DEVARCH_REVISION_Pos))
#define DWT_DEVARCH_PRESENT_Pos               _U_(20)                                        /**< (DWT_DEVARCH) DEVARCH Present Position */
#define DWT_DEVARCH_PRESENT_Msk               (_U_(0x1) << DWT_DEVARCH_PRESENT_Pos)          /**< (DWT_DEVARCH) DEVARCH Present Mask */
#define DWT_DEVARCH_ARCHITECT_Pos             _U_(21)                                        /**< (DWT_DEVARCH) Architect Position */
#define DWT_DEVARCH_ARCHITECT_Msk             (_U_(0x7FF) << DWT_DEVARCH_ARCHITECT_Pos)      /**< (DWT_DEVARCH) Architect Mask */
#define DWT_DEVARCH_ARCHITECT(value)          (DWT_DEVARCH_ARCHITECT_Msk & ((value) << DWT_DEVARCH_ARCHITECT_Pos))
#define DWT_DEVARCH_Msk                       _U_(0xFFFFFFFF)                                /**< (DWT_DEVARCH) Register Mask  */


/* -------- DWT_DEVTYPE : (DWT Offset: 0xFCC) ( R/ 32) DWT Device Type Register -------- */
#define DWT_DEVTYPE_RESETVALUE              _U_(0x00)                                     /**<  (DWT_DEVTYPE) DWT Device Type Register  Reset Value */

#define DWT_DEVTYPE_MAJOR_Pos                 _U_(0)                                         /**< (DWT_DEVTYPE) Major type Position */
#define DWT_DEVTYPE_MAJOR_Msk                 (_U_(0xF) << DWT_DEVTYPE_MAJOR_Pos)            /**< (DWT_DEVTYPE) Major type Mask */
#define DWT_DEVTYPE_MAJOR(value)              (DWT_DEVTYPE_MAJOR_Msk & ((value) << DWT_DEVTYPE_MAJOR_Pos))
#define DWT_DEVTYPE_SUB_Pos                   _U_(4)                                         /**< (DWT_DEVTYPE) Sub-type Position */
#define DWT_DEVTYPE_SUB_Msk                   (_U_(0xF) << DWT_DEVTYPE_SUB_Pos)              /**< (DWT_DEVTYPE) Sub-type Mask */
#define DWT_DEVTYPE_SUB(value)                (DWT_DEVTYPE_SUB_Msk & ((value) << DWT_DEVTYPE_SUB_Pos))
#define DWT_DEVTYPE_Msk                       _U_(0x000000FF)                                /**< (DWT_DEVTYPE) Register Mask  */


/* -------- DWT_PIDR4 : (DWT Offset: 0xFD0) ( R/ 32) DWT Peripheral Identification Register 4 -------- */
#define DWT_PIDR4_DES_2_Pos                   _U_(0)                                         /**< (DWT_PIDR4) JEP106 continuation code Position */
#define DWT_PIDR4_DES_2_Msk                   (_U_(0xF) << DWT_PIDR4_DES_2_Pos)              /**< (DWT_PIDR4) JEP106 continuation code Mask */
#define DWT_PIDR4_DES_2(value)                (DWT_PIDR4_DES_2_Msk & ((value) << DWT_PIDR4_DES_2_Pos))
#define DWT_PIDR4_SIZE_Pos                    _U_(4)                                         /**< (DWT_PIDR4) 4KB count Position */
#define DWT_PIDR4_SIZE_Msk                    (_U_(0xF) << DWT_PIDR4_SIZE_Pos)               /**< (DWT_PIDR4) 4KB count Mask */
#define DWT_PIDR4_SIZE(value)                 (DWT_PIDR4_SIZE_Msk & ((value) << DWT_PIDR4_SIZE_Pos))
#define DWT_PIDR4_Msk                         _U_(0x000000FF)                                /**< (DWT_PIDR4) Register Mask  */


/* -------- DWT_PIDR5 : (DWT Offset: 0xFD4) ( R/ 32) DWT Peripheral Identification Register 5 -------- */
#define DWT_PIDR5_RESETVALUE                _U_(0x00)                                     /**<  (DWT_PIDR5) DWT Peripheral Identification Register 5  Reset Value */

#define DWT_PIDR5_Msk                         _U_(0x00000000)                                /**< (DWT_PIDR5) Register Mask  */


/* -------- DWT_PIDR6 : (DWT Offset: 0xFD8) ( R/ 32) DWT Peripheral Identification Register 6 -------- */
#define DWT_PIDR6_RESETVALUE                _U_(0x00)                                     /**<  (DWT_PIDR6) DWT Peripheral Identification Register 6  Reset Value */

#define DWT_PIDR6_Msk                         _U_(0x00000000)                                /**< (DWT_PIDR6) Register Mask  */


/* -------- DWT_PIDR7 : (DWT Offset: 0xFDC) ( R/ 32) DWT Peripheral Identification Register 7 -------- */
#define DWT_PIDR7_RESETVALUE                _U_(0x00)                                     /**<  (DWT_PIDR7) DWT Peripheral Identification Register 7  Reset Value */

#define DWT_PIDR7_Msk                         _U_(0x00000000)                                /**< (DWT_PIDR7) Register Mask  */


/* -------- DWT_PIDR0 : (DWT Offset: 0xFE0) ( R/ 32) DWT Peripheral Identification Register 0 -------- */
#define DWT_PIDR0_PART_0_Pos                  _U_(0)                                         /**< (DWT_PIDR0) Part number bits[7:0] Position */
#define DWT_PIDR0_PART_0_Msk                  (_U_(0xFF) << DWT_PIDR0_PART_0_Pos)            /**< (DWT_PIDR0) Part number bits[7:0] Mask */
#define DWT_PIDR0_PART_0(value)               (DWT_PIDR0_PART_0_Msk & ((value) << DWT_PIDR0_PART_0_Pos))
#define DWT_PIDR0_Msk                         _U_(0x000000FF)                                /**< (DWT_PIDR0) Register Mask  */


/* -------- DWT_PIDR1 : (DWT Offset: 0xFE4) ( R/ 32) DWT Peripheral Identification Register 1 -------- */
#define DWT_PIDR1_PART_1_Pos                  _U_(0)                                         /**< (DWT_PIDR1) Part number bits[11:8] Position */
#define DWT_PIDR1_PART_1_Msk                  (_U_(0xF) << DWT_PIDR1_PART_1_Pos)             /**< (DWT_PIDR1) Part number bits[11:8] Mask */
#define DWT_PIDR1_PART_1(value)               (DWT_PIDR1_PART_1_Msk & ((value) << DWT_PIDR1_PART_1_Pos))
#define DWT_PIDR1_DES_0_Pos                   _U_(4)                                         /**< (DWT_PIDR1) JEP106 identification code bits [3:0] Position */
#define DWT_PIDR1_DES_0_Msk                   (_U_(0xF) << DWT_PIDR1_DES_0_Pos)              /**< (DWT_PIDR1) JEP106 identification code bits [3:0] Mask */
#define DWT_PIDR1_DES_0(value)                (DWT_PIDR1_DES_0_Msk & ((value) << DWT_PIDR1_DES_0_Pos))
#define DWT_PIDR1_Msk                         _U_(0x000000FF)                                /**< (DWT_PIDR1) Register Mask  */


/* -------- DWT_PIDR2 : (DWT Offset: 0xFE8) ( R/ 32) DWT Peripheral Identification Register 2 -------- */
#define DWT_PIDR2_DES_1_Pos                   _U_(0)                                         /**< (DWT_PIDR2) JEP106 identification code bits[6:4] Position */
#define DWT_PIDR2_DES_1_Msk                   (_U_(0x7) << DWT_PIDR2_DES_1_Pos)              /**< (DWT_PIDR2) JEP106 identification code bits[6:4] Mask */
#define DWT_PIDR2_DES_1(value)                (DWT_PIDR2_DES_1_Msk & ((value) << DWT_PIDR2_DES_1_Pos))
#define DWT_PIDR2_JEDEC_Pos                   _U_(3)                                         /**< (DWT_PIDR2) JEDEC assignee value is used Position */
#define DWT_PIDR2_JEDEC_Msk                   (_U_(0x1) << DWT_PIDR2_JEDEC_Pos)              /**< (DWT_PIDR2) JEDEC assignee value is used Mask */
#define DWT_PIDR2_REVISION_Pos                _U_(4)                                         /**< (DWT_PIDR2) Component revision Position */
#define DWT_PIDR2_REVISION_Msk                (_U_(0xF) << DWT_PIDR2_REVISION_Pos)           /**< (DWT_PIDR2) Component revision Mask */
#define DWT_PIDR2_REVISION(value)             (DWT_PIDR2_REVISION_Msk & ((value) << DWT_PIDR2_REVISION_Pos))
#define DWT_PIDR2_Msk                         _U_(0x000000FF)                                /**< (DWT_PIDR2) Register Mask  */


/* -------- DWT_PIDR3 : (DWT Offset: 0xFEC) ( R/ 32) DWT Peripheral Identification Register 3 -------- */
#define DWT_PIDR3_CMOD_Pos                    _U_(0)                                         /**< (DWT_PIDR3) Customer Modified Position */
#define DWT_PIDR3_CMOD_Msk                    (_U_(0xF) << DWT_PIDR3_CMOD_Pos)               /**< (DWT_PIDR3) Customer Modified Mask */
#define DWT_PIDR3_CMOD(value)                 (DWT_PIDR3_CMOD_Msk & ((value) << DWT_PIDR3_CMOD_Pos))
#define DWT_PIDR3_REVAND_Pos                  _U_(4)                                         /**< (DWT_PIDR3) RevAnd Position */
#define DWT_PIDR3_REVAND_Msk                  (_U_(0xF) << DWT_PIDR3_REVAND_Pos)             /**< (DWT_PIDR3) RevAnd Mask */
#define DWT_PIDR3_REVAND(value)               (DWT_PIDR3_REVAND_Msk & ((value) << DWT_PIDR3_REVAND_Pos))
#define DWT_PIDR3_Msk                         _U_(0x000000FF)                                /**< (DWT_PIDR3) Register Mask  */


/* -------- DWT_CIDR0 : (DWT Offset: 0xFF0) ( R/ 32) DWT Component Identification Register 0 -------- */
#define DWT_CIDR0_RESETVALUE                _U_(0x0D)                                     /**<  (DWT_CIDR0) DWT Component Identification Register 0  Reset Value */

#define DWT_CIDR0_PRMBL_0_Pos                 _U_(0)                                         /**< (DWT_CIDR0) CoreSight component identification preamble Position */
#define DWT_CIDR0_PRMBL_0_Msk                 (_U_(0xFF) << DWT_CIDR0_PRMBL_0_Pos)           /**< (DWT_CIDR0) CoreSight component identification preamble Mask */
#define DWT_CIDR0_PRMBL_0(value)              (DWT_CIDR0_PRMBL_0_Msk & ((value) << DWT_CIDR0_PRMBL_0_Pos))
#define DWT_CIDR0_Msk                         _U_(0x000000FF)                                /**< (DWT_CIDR0) Register Mask  */


/* -------- DWT_CIDR1 : (DWT Offset: 0xFF4) ( R/ 32) DWT Component Identification Register 1 -------- */
#define DWT_CIDR1_RESETVALUE                _U_(0x90)                                     /**<  (DWT_CIDR1) DWT Component Identification Register 1  Reset Value */

#define DWT_CIDR1_PRMBL_1_Pos                 _U_(0)                                         /**< (DWT_CIDR1) CoreSight component identification preamble Position */
#define DWT_CIDR1_PRMBL_1_Msk                 (_U_(0xF) << DWT_CIDR1_PRMBL_1_Pos)            /**< (DWT_CIDR1) CoreSight component identification preamble Mask */
#define DWT_CIDR1_PRMBL_1(value)              (DWT_CIDR1_PRMBL_1_Msk & ((value) << DWT_CIDR1_PRMBL_1_Pos))
#define DWT_CIDR1_CLASS_Pos                   _U_(4)                                         /**< (DWT_CIDR1) CoreSight component class Position */
#define DWT_CIDR1_CLASS_Msk                   (_U_(0xF) << DWT_CIDR1_CLASS_Pos)              /**< (DWT_CIDR1) CoreSight component class Mask */
#define DWT_CIDR1_CLASS(value)                (DWT_CIDR1_CLASS_Msk & ((value) << DWT_CIDR1_CLASS_Pos))
#define DWT_CIDR1_Msk                         _U_(0x000000FF)                                /**< (DWT_CIDR1) Register Mask  */


/* -------- DWT_CIDR2 : (DWT Offset: 0xFF8) ( R/ 32) DWT Component Identification Register 2 -------- */
#define DWT_CIDR2_RESETVALUE                _U_(0x05)                                     /**<  (DWT_CIDR2) DWT Component Identification Register 2  Reset Value */

#define DWT_CIDR2_PRMBL_2_Pos                 _U_(0)                                         /**< (DWT_CIDR2) CoreSight component identification preamble Position */
#define DWT_CIDR2_PRMBL_2_Msk                 (_U_(0xFF) << DWT_CIDR2_PRMBL_2_Pos)           /**< (DWT_CIDR2) CoreSight component identification preamble Mask */
#define DWT_CIDR2_PRMBL_2(value)              (DWT_CIDR2_PRMBL_2_Msk & ((value) << DWT_CIDR2_PRMBL_2_Pos))
#define DWT_CIDR2_Msk                         _U_(0x000000FF)                                /**< (DWT_CIDR2) Register Mask  */


/* -------- DWT_CIDR3 : (DWT Offset: 0xFFC) ( R/ 32) DWT Component Identification Register 3 -------- */
#define DWT_CIDR3_RESETVALUE                _U_(0xB1)                                     /**<  (DWT_CIDR3) DWT Component Identification Register 3  Reset Value */

#define DWT_CIDR3_PRMBL_3_Pos                 _U_(0)                                         /**< (DWT_CIDR3) CoreSight component identification preamble Position */
#define DWT_CIDR3_PRMBL_3_Msk                 (_U_(0xFF) << DWT_CIDR3_PRMBL_3_Pos)           /**< (DWT_CIDR3) CoreSight component identification preamble Mask */
#define DWT_CIDR3_PRMBL_3(value)              (DWT_CIDR3_PRMBL_3_Msk & ((value) << DWT_CIDR3_PRMBL_3_Pos))
#define DWT_CIDR3_Msk                         _U_(0x000000FF)                                /**< (DWT_CIDR3) Register Mask  */


/** \brief DWT register offsets definitions */
#define DWT_COMP_REG_OFST              (0x00)         /**< (DWT_COMP) DWT Comparator Register n Offset */
#define DWT_FUNCTION_REG_OFST          (0x08)         /**< (DWT_FUNCTION) DWT Function Register x Offset */
#define DWT_CTRL_REG_OFST              (0x00)         /**< (DWT_CTRL) DWT Control Register Offset */
#define DWT_PCSR_REG_OFST              (0x1C)         /**< (DWT_PCSR) DWT Program Counter Sample Register Offset */
#define DWT_LAR_REG_OFST               (0xFB0)        /**< (DWT_LAR) DWT Software Lock Access Register Offset */
#define DWT_LSR_REG_OFST               (0xFB4)        /**< (DWT_LSR) DWT Software Lock Status Register Offset */
#define DWT_DEVARCH_REG_OFST           (0xFBC)        /**< (DWT_DEVARCH) DWT Device Architecture Register Offset */
#define DWT_DEVTYPE_REG_OFST           (0xFCC)        /**< (DWT_DEVTYPE) DWT Device Type Register Offset */
#define DWT_PIDR4_REG_OFST             (0xFD0)        /**< (DWT_PIDR4) DWT Peripheral Identification Register 4 Offset */
#define DWT_PIDR5_REG_OFST             (0xFD4)        /**< (DWT_PIDR5) DWT Peripheral Identification Register 5 Offset */
#define DWT_PIDR6_REG_OFST             (0xFD8)        /**< (DWT_PIDR6) DWT Peripheral Identification Register 6 Offset */
#define DWT_PIDR7_REG_OFST             (0xFDC)        /**< (DWT_PIDR7) DWT Peripheral Identification Register 7 Offset */
#define DWT_PIDR0_REG_OFST             (0xFE0)        /**< (DWT_PIDR0) DWT Peripheral Identification Register 0 Offset */
#define DWT_PIDR1_REG_OFST             (0xFE4)        /**< (DWT_PIDR1) DWT Peripheral Identification Register 1 Offset */
#define DWT_PIDR2_REG_OFST             (0xFE8)        /**< (DWT_PIDR2) DWT Peripheral Identification Register 2 Offset */
#define DWT_PIDR3_REG_OFST             (0xFEC)        /**< (DWT_PIDR3) DWT Peripheral Identification Register 3 Offset */
#define DWT_CIDR0_REG_OFST             (0xFF0)        /**< (DWT_CIDR0) DWT Component Identification Register 0 Offset */
#define DWT_CIDR1_REG_OFST             (0xFF4)        /**< (DWT_CIDR1) DWT Component Identification Register 1 Offset */
#define DWT_CIDR2_REG_OFST             (0xFF8)        /**< (DWT_CIDR2) DWT Component Identification Register 2 Offset */
#define DWT_CIDR3_REG_OFST             (0xFFC)        /**< (DWT_CIDR3) DWT Component Identification Register 3 Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief COMPARATOR register API structure */
typedef struct
{
  __IO  uint32_t                       DWT_COMP;        /**< Offset: 0x00 (R/W  32) DWT Comparator Register n */
  __I   uint8_t                        Reserved1[0x04];
  __IO  uint32_t                       DWT_FUNCTION;    /**< Offset: 0x08 (R/W  32) DWT Function Register x */
  __I   uint8_t                        Reserved2[0x04];
} dwt_comparator_registers_t;

#define COMPARATOR_NUMBER _U_(2)

/** \brief DWT register API structure */
typedef struct
{  /* Data Watchpoint and Trace */
  __IO  uint32_t                       DWT_CTRL;        /**< Offset: 0x00 (R/W  32) DWT Control Register */
  __I   uint8_t                        Reserved1[0x18];
  __I   uint32_t                       DWT_PCSR;        /**< Offset: 0x1C (R/   32) DWT Program Counter Sample Register */
        dwt_comparator_registers_t     COMPARATOR[COMPARATOR_NUMBER]; /**< Offset: 0x20  */
  __I   uint8_t                        Reserved2[0xF70];
  __O   uint32_t                       DWT_LAR;         /**< Offset: 0xFB0 ( /W  32) DWT Software Lock Access Register */
  __I   uint32_t                       DWT_LSR;         /**< Offset: 0xFB4 (R/   32) DWT Software Lock Status Register */
  __I   uint8_t                        Reserved3[0x04];
  __I   uint32_t                       DWT_DEVARCH;     /**< Offset: 0xFBC (R/   32) DWT Device Architecture Register */
  __I   uint8_t                        Reserved4[0x0C];
  __I   uint32_t                       DWT_DEVTYPE;     /**< Offset: 0xFCC (R/   32) DWT Device Type Register */
  __I   uint32_t                       DWT_PIDR4;       /**< Offset: 0xFD0 (R/   32) DWT Peripheral Identification Register 4 */
  __I   uint32_t                       DWT_PIDR5;       /**< Offset: 0xFD4 (R/   32) DWT Peripheral Identification Register 5 */
  __I   uint32_t                       DWT_PIDR6;       /**< Offset: 0xFD8 (R/   32) DWT Peripheral Identification Register 6 */
  __I   uint32_t                       DWT_PIDR7;       /**< Offset: 0xFDC (R/   32) DWT Peripheral Identification Register 7 */
  __I   uint32_t                       DWT_PIDR0;       /**< Offset: 0xFE0 (R/   32) DWT Peripheral Identification Register 0 */
  __I   uint32_t                       DWT_PIDR1;       /**< Offset: 0xFE4 (R/   32) DWT Peripheral Identification Register 1 */
  __I   uint32_t                       DWT_PIDR2;       /**< Offset: 0xFE8 (R/   32) DWT Peripheral Identification Register 2 */
  __I   uint32_t                       DWT_PIDR3;       /**< Offset: 0xFEC (R/   32) DWT Peripheral Identification Register 3 */
  __I   uint32_t                       DWT_CIDR0;       /**< Offset: 0xFF0 (R/   32) DWT Component Identification Register 0 */
  __I   uint32_t                       DWT_CIDR1;       /**< Offset: 0xFF4 (R/   32) DWT Component Identification Register 1 */
  __I   uint32_t                       DWT_CIDR2;       /**< Offset: 0xFF8 (R/   32) DWT Component Identification Register 2 */
  __I   uint32_t                       DWT_CIDR3;       /**< Offset: 0xFFC (R/   32) DWT Component Identification Register 3 */
} dwt_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAML10_DWT_COMPONENT_H_ */
