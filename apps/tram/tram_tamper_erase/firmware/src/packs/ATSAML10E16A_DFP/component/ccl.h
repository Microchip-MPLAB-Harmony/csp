/**
 * \brief Component description for CCL
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

/* file generated from device description version 2019-06-03T17:11:15Z */
#ifndef _SAML10_CCL_COMPONENT_H_
#define _SAML10_CCL_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR CCL                                          */
/* ************************************************************************** */

/* -------- CCL_CTRL : (CCL Offset: 0x00) (R/W 8) Control -------- */
#define CCL_CTRL_RESETVALUE                 _U_(0x00)                                     /**<  (CCL_CTRL) Control  Reset Value */

#define CCL_CTRL_SWRST_Pos                    _U_(0)                                         /**< (CCL_CTRL) Software Reset Position */
#define CCL_CTRL_SWRST_Msk                    (_U_(0x1) << CCL_CTRL_SWRST_Pos)               /**< (CCL_CTRL) Software Reset Mask */
#define CCL_CTRL_ENABLE_Pos                   _U_(1)                                         /**< (CCL_CTRL) Enable Position */
#define CCL_CTRL_ENABLE_Msk                   (_U_(0x1) << CCL_CTRL_ENABLE_Pos)              /**< (CCL_CTRL) Enable Mask */
#define   CCL_CTRL_ENABLE_OFF_Val             _U_(0x0)                                       /**< (CCL_CTRL) The peripheral is disabled  */
#define   CCL_CTRL_ENABLE_ON_Val              _U_(0x1)                                       /**< (CCL_CTRL) The peripheral is enabled  */
#define CCL_CTRL_ENABLE_OFF                   (CCL_CTRL_ENABLE_OFF_Val << CCL_CTRL_ENABLE_Pos) /**< (CCL_CTRL) The peripheral is disabled Position  */
#define CCL_CTRL_ENABLE_ON                    (CCL_CTRL_ENABLE_ON_Val << CCL_CTRL_ENABLE_Pos) /**< (CCL_CTRL) The peripheral is enabled Position  */
#define CCL_CTRL_RUNSTDBY_Pos                 _U_(6)                                         /**< (CCL_CTRL) Run in Standby Position */
#define CCL_CTRL_RUNSTDBY_Msk                 (_U_(0x1) << CCL_CTRL_RUNSTDBY_Pos)            /**< (CCL_CTRL) Run in Standby Mask */
#define   CCL_CTRL_RUNSTDBY_OFF_Val           _U_(0x0)                                       /**< (CCL_CTRL) Generic clock is not required in standby sleep mode  */
#define   CCL_CTRL_RUNSTDBY_ON_Val            _U_(0x1)                                       /**< (CCL_CTRL) Generic clock is required in standby sleep mode  */
#define CCL_CTRL_RUNSTDBY_OFF                 (CCL_CTRL_RUNSTDBY_OFF_Val << CCL_CTRL_RUNSTDBY_Pos) /**< (CCL_CTRL) Generic clock is not required in standby sleep mode Position  */
#define CCL_CTRL_RUNSTDBY_ON                  (CCL_CTRL_RUNSTDBY_ON_Val << CCL_CTRL_RUNSTDBY_Pos) /**< (CCL_CTRL) Generic clock is required in standby sleep mode Position  */
#define CCL_CTRL_Msk                          _U_(0x43)                                      /**< (CCL_CTRL) Register Mask  */


/* -------- CCL_SEQCTRL0 : (CCL Offset: 0x04) (R/W 8) SEQ Control 0 -------- */
#define CCL_SEQCTRL0_RESETVALUE             _U_(0x00)                                     /**<  (CCL_SEQCTRL0) SEQ Control 0  Reset Value */

#define CCL_SEQCTRL0_SEQSEL_Pos               _U_(0)                                         /**< (CCL_SEQCTRL0) Sequential Selection 0 Position */
#define CCL_SEQCTRL0_SEQSEL_Msk               (_U_(0xF) << CCL_SEQCTRL0_SEQSEL_Pos)          /**< (CCL_SEQCTRL0) Sequential Selection 0 Mask */
#define CCL_SEQCTRL0_SEQSEL(value)            (CCL_SEQCTRL0_SEQSEL_Msk & ((value) << CCL_SEQCTRL0_SEQSEL_Pos))
#define   CCL_SEQCTRL0_SEQSEL_DISABLE_Val     _U_(0x0)                                       /**< (CCL_SEQCTRL0) Sequential logic is disabled  */
#define   CCL_SEQCTRL0_SEQSEL_DFF_Val         _U_(0x1)                                       /**< (CCL_SEQCTRL0) D flip flop  */
#define   CCL_SEQCTRL0_SEQSEL_JK_Val          _U_(0x2)                                       /**< (CCL_SEQCTRL0) JK flip flop  */
#define   CCL_SEQCTRL0_SEQSEL_LATCH_Val       _U_(0x3)                                       /**< (CCL_SEQCTRL0) D latch  */
#define   CCL_SEQCTRL0_SEQSEL_RS_Val          _U_(0x4)                                       /**< (CCL_SEQCTRL0) RS latch  */
#define CCL_SEQCTRL0_SEQSEL_DISABLE           (CCL_SEQCTRL0_SEQSEL_DISABLE_Val << CCL_SEQCTRL0_SEQSEL_Pos) /**< (CCL_SEQCTRL0) Sequential logic is disabled Position  */
#define CCL_SEQCTRL0_SEQSEL_DFF               (CCL_SEQCTRL0_SEQSEL_DFF_Val << CCL_SEQCTRL0_SEQSEL_Pos) /**< (CCL_SEQCTRL0) D flip flop Position  */
#define CCL_SEQCTRL0_SEQSEL_JK                (CCL_SEQCTRL0_SEQSEL_JK_Val << CCL_SEQCTRL0_SEQSEL_Pos) /**< (CCL_SEQCTRL0) JK flip flop Position  */
#define CCL_SEQCTRL0_SEQSEL_LATCH             (CCL_SEQCTRL0_SEQSEL_LATCH_Val << CCL_SEQCTRL0_SEQSEL_Pos) /**< (CCL_SEQCTRL0) D latch Position  */
#define CCL_SEQCTRL0_SEQSEL_RS                (CCL_SEQCTRL0_SEQSEL_RS_Val << CCL_SEQCTRL0_SEQSEL_Pos) /**< (CCL_SEQCTRL0) RS latch Position  */
#define CCL_SEQCTRL0_Msk                      _U_(0x0F)                                      /**< (CCL_SEQCTRL0) Register Mask  */


/* -------- CCL_LUTCTRL0 : (CCL Offset: 0x08) (R/W 32) LUT Control 0 -------- */
#define CCL_LUTCTRL0_RESETVALUE             _U_(0x00)                                     /**<  (CCL_LUTCTRL0) LUT Control 0  Reset Value */

#define CCL_LUTCTRL0_ENABLE_Pos               _U_(1)                                         /**< (CCL_LUTCTRL0) LUT Enable Position */
#define CCL_LUTCTRL0_ENABLE_Msk               (_U_(0x1) << CCL_LUTCTRL0_ENABLE_Pos)          /**< (CCL_LUTCTRL0) LUT Enable Mask */
#define   CCL_LUTCTRL0_ENABLE_DISABLE_Val     _U_(0x0)                                       /**< (CCL_LUTCTRL0) The LUT is disabled  */
#define   CCL_LUTCTRL0_ENABLE_ENABLE_Val      _U_(0x1)                                       /**< (CCL_LUTCTRL0) The LUT is enabled  */
#define CCL_LUTCTRL0_ENABLE_DISABLE           (CCL_LUTCTRL0_ENABLE_DISABLE_Val << CCL_LUTCTRL0_ENABLE_Pos) /**< (CCL_LUTCTRL0) The LUT is disabled Position  */
#define CCL_LUTCTRL0_ENABLE_ENABLE            (CCL_LUTCTRL0_ENABLE_ENABLE_Val << CCL_LUTCTRL0_ENABLE_Pos) /**< (CCL_LUTCTRL0) The LUT is enabled Position  */
#define CCL_LUTCTRL0_FILTSEL_Pos              _U_(4)                                         /**< (CCL_LUTCTRL0) Filter Selection Position */
#define CCL_LUTCTRL0_FILTSEL_Msk              (_U_(0x3) << CCL_LUTCTRL0_FILTSEL_Pos)         /**< (CCL_LUTCTRL0) Filter Selection Mask */
#define CCL_LUTCTRL0_FILTSEL(value)           (CCL_LUTCTRL0_FILTSEL_Msk & ((value) << CCL_LUTCTRL0_FILTSEL_Pos))
#define   CCL_LUTCTRL0_FILTSEL_DISABLE_Val    _U_(0x0)                                       /**< (CCL_LUTCTRL0) Filter disabled  */
#define   CCL_LUTCTRL0_FILTSEL_SYNCH_Val      _U_(0x1)                                       /**< (CCL_LUTCTRL0) Synchronizer enabled  */
#define   CCL_LUTCTRL0_FILTSEL_FILTER_Val     _U_(0x2)                                       /**< (CCL_LUTCTRL0) Filter enabled  */
#define CCL_LUTCTRL0_FILTSEL_DISABLE          (CCL_LUTCTRL0_FILTSEL_DISABLE_Val << CCL_LUTCTRL0_FILTSEL_Pos) /**< (CCL_LUTCTRL0) Filter disabled Position  */
#define CCL_LUTCTRL0_FILTSEL_SYNCH            (CCL_LUTCTRL0_FILTSEL_SYNCH_Val << CCL_LUTCTRL0_FILTSEL_Pos) /**< (CCL_LUTCTRL0) Synchronizer enabled Position  */
#define CCL_LUTCTRL0_FILTSEL_FILTER           (CCL_LUTCTRL0_FILTSEL_FILTER_Val << CCL_LUTCTRL0_FILTSEL_Pos) /**< (CCL_LUTCTRL0) Filter enabled Position  */
#define CCL_LUTCTRL0_EDGESEL_Pos              _U_(7)                                         /**< (CCL_LUTCTRL0) Edge Selection Position */
#define CCL_LUTCTRL0_EDGESEL_Msk              (_U_(0x1) << CCL_LUTCTRL0_EDGESEL_Pos)         /**< (CCL_LUTCTRL0) Edge Selection Mask */
#define   CCL_LUTCTRL0_EDGESEL_DISABLED_Val   _U_(0x0)                                       /**< (CCL_LUTCTRL0) Edge detector is disabled  */
#define   CCL_LUTCTRL0_EDGESEL_ENABLED_Val    _U_(0x1)                                       /**< (CCL_LUTCTRL0) Edge detector is enabled  */
#define CCL_LUTCTRL0_EDGESEL_DISABLED         (CCL_LUTCTRL0_EDGESEL_DISABLED_Val << CCL_LUTCTRL0_EDGESEL_Pos) /**< (CCL_LUTCTRL0) Edge detector is disabled Position  */
#define CCL_LUTCTRL0_EDGESEL_ENABLED          (CCL_LUTCTRL0_EDGESEL_ENABLED_Val << CCL_LUTCTRL0_EDGESEL_Pos) /**< (CCL_LUTCTRL0) Edge detector is enabled Position  */
#define CCL_LUTCTRL0_INSEL0_Pos               _U_(8)                                         /**< (CCL_LUTCTRL0) Input Selection 0 Position */
#define CCL_LUTCTRL0_INSEL0_Msk               (_U_(0xF) << CCL_LUTCTRL0_INSEL0_Pos)          /**< (CCL_LUTCTRL0) Input Selection 0 Mask */
#define CCL_LUTCTRL0_INSEL0(value)            (CCL_LUTCTRL0_INSEL0_Msk & ((value) << CCL_LUTCTRL0_INSEL0_Pos))
#define   CCL_LUTCTRL0_INSEL0_MASK_Val        _U_(0x0)                                       /**< (CCL_LUTCTRL0) Masked input  */
#define   CCL_LUTCTRL0_INSEL0_FEEDBACK_Val    _U_(0x1)                                       /**< (CCL_LUTCTRL0) Feedback input source  */
#define   CCL_LUTCTRL0_INSEL0_LINK_Val        _U_(0x2)                                       /**< (CCL_LUTCTRL0) Linked LUT input source  */
#define   CCL_LUTCTRL0_INSEL0_EVENT_Val       _U_(0x3)                                       /**< (CCL_LUTCTRL0) Event input source  */
#define   CCL_LUTCTRL0_INSEL0_IO_Val          _U_(0x4)                                       /**< (CCL_LUTCTRL0) I/O pin input source  */
#define   CCL_LUTCTRL0_INSEL0_AC_Val          _U_(0x5)                                       /**< (CCL_LUTCTRL0) AC input source  */
#define   CCL_LUTCTRL0_INSEL0_TC_Val          _U_(0x6)                                       /**< (CCL_LUTCTRL0) TC input source  */
#define   CCL_LUTCTRL0_INSEL0_ALTTC_Val       _U_(0x7)                                       /**< (CCL_LUTCTRL0) Alternate TC input source  */
#define   CCL_LUTCTRL0_INSEL0_SERCOM_Val      _U_(0x9)                                       /**< (CCL_LUTCTRL0) SERCOM input source  */
#define   CCL_LUTCTRL0_INSEL0_ASYNCEVENT_Val  _U_(0xB)                                       /**< (CCL_LUTCTRL0) Asynchronous event input source  */
#define CCL_LUTCTRL0_INSEL0_MASK              (CCL_LUTCTRL0_INSEL0_MASK_Val << CCL_LUTCTRL0_INSEL0_Pos) /**< (CCL_LUTCTRL0) Masked input Position  */
#define CCL_LUTCTRL0_INSEL0_FEEDBACK          (CCL_LUTCTRL0_INSEL0_FEEDBACK_Val << CCL_LUTCTRL0_INSEL0_Pos) /**< (CCL_LUTCTRL0) Feedback input source Position  */
#define CCL_LUTCTRL0_INSEL0_LINK              (CCL_LUTCTRL0_INSEL0_LINK_Val << CCL_LUTCTRL0_INSEL0_Pos) /**< (CCL_LUTCTRL0) Linked LUT input source Position  */
#define CCL_LUTCTRL0_INSEL0_EVENT             (CCL_LUTCTRL0_INSEL0_EVENT_Val << CCL_LUTCTRL0_INSEL0_Pos) /**< (CCL_LUTCTRL0) Event input source Position  */
#define CCL_LUTCTRL0_INSEL0_IO                (CCL_LUTCTRL0_INSEL0_IO_Val << CCL_LUTCTRL0_INSEL0_Pos) /**< (CCL_LUTCTRL0) I/O pin input source Position  */
#define CCL_LUTCTRL0_INSEL0_AC                (CCL_LUTCTRL0_INSEL0_AC_Val << CCL_LUTCTRL0_INSEL0_Pos) /**< (CCL_LUTCTRL0) AC input source Position  */
#define CCL_LUTCTRL0_INSEL0_TC                (CCL_LUTCTRL0_INSEL0_TC_Val << CCL_LUTCTRL0_INSEL0_Pos) /**< (CCL_LUTCTRL0) TC input source Position  */
#define CCL_LUTCTRL0_INSEL0_ALTTC             (CCL_LUTCTRL0_INSEL0_ALTTC_Val << CCL_LUTCTRL0_INSEL0_Pos) /**< (CCL_LUTCTRL0) Alternate TC input source Position  */
#define CCL_LUTCTRL0_INSEL0_SERCOM            (CCL_LUTCTRL0_INSEL0_SERCOM_Val << CCL_LUTCTRL0_INSEL0_Pos) /**< (CCL_LUTCTRL0) SERCOM input source Position  */
#define CCL_LUTCTRL0_INSEL0_ASYNCEVENT        (CCL_LUTCTRL0_INSEL0_ASYNCEVENT_Val << CCL_LUTCTRL0_INSEL0_Pos) /**< (CCL_LUTCTRL0) Asynchronous event input source Position  */
#define CCL_LUTCTRL0_INSEL1_Pos               _U_(12)                                        /**< (CCL_LUTCTRL0) Input Selection 1 Position */
#define CCL_LUTCTRL0_INSEL1_Msk               (_U_(0xF) << CCL_LUTCTRL0_INSEL1_Pos)          /**< (CCL_LUTCTRL0) Input Selection 1 Mask */
#define CCL_LUTCTRL0_INSEL1(value)            (CCL_LUTCTRL0_INSEL1_Msk & ((value) << CCL_LUTCTRL0_INSEL1_Pos))
#define   CCL_LUTCTRL0_INSEL1_MASK_Val        _U_(0x0)                                       /**< (CCL_LUTCTRL0) Masked input  */
#define   CCL_LUTCTRL0_INSEL1_FEEDBACK_Val    _U_(0x1)                                       /**< (CCL_LUTCTRL0) Feedback input source  */
#define   CCL_LUTCTRL0_INSEL1_LINK_Val        _U_(0x2)                                       /**< (CCL_LUTCTRL0) Linked LUT input source  */
#define   CCL_LUTCTRL0_INSEL1_EVENT_Val       _U_(0x3)                                       /**< (CCL_LUTCTRL0) Event input source  */
#define   CCL_LUTCTRL0_INSEL1_IO_Val          _U_(0x4)                                       /**< (CCL_LUTCTRL0) I/O pin input source  */
#define   CCL_LUTCTRL0_INSEL1_AC_Val          _U_(0x5)                                       /**< (CCL_LUTCTRL0) AC input source  */
#define   CCL_LUTCTRL0_INSEL1_TC_Val          _U_(0x6)                                       /**< (CCL_LUTCTRL0) TC input source  */
#define   CCL_LUTCTRL0_INSEL1_ALTTC_Val       _U_(0x7)                                       /**< (CCL_LUTCTRL0) Alternate TC input source  */
#define   CCL_LUTCTRL0_INSEL1_SERCOM_Val      _U_(0x9)                                       /**< (CCL_LUTCTRL0) SERCOM input source  */
#define   CCL_LUTCTRL0_INSEL1_ASYNCEVENT_Val  _U_(0xB)                                       /**< (CCL_LUTCTRL0) Asynchronous event input source  */
#define CCL_LUTCTRL0_INSEL1_MASK              (CCL_LUTCTRL0_INSEL1_MASK_Val << CCL_LUTCTRL0_INSEL1_Pos) /**< (CCL_LUTCTRL0) Masked input Position  */
#define CCL_LUTCTRL0_INSEL1_FEEDBACK          (CCL_LUTCTRL0_INSEL1_FEEDBACK_Val << CCL_LUTCTRL0_INSEL1_Pos) /**< (CCL_LUTCTRL0) Feedback input source Position  */
#define CCL_LUTCTRL0_INSEL1_LINK              (CCL_LUTCTRL0_INSEL1_LINK_Val << CCL_LUTCTRL0_INSEL1_Pos) /**< (CCL_LUTCTRL0) Linked LUT input source Position  */
#define CCL_LUTCTRL0_INSEL1_EVENT             (CCL_LUTCTRL0_INSEL1_EVENT_Val << CCL_LUTCTRL0_INSEL1_Pos) /**< (CCL_LUTCTRL0) Event input source Position  */
#define CCL_LUTCTRL0_INSEL1_IO                (CCL_LUTCTRL0_INSEL1_IO_Val << CCL_LUTCTRL0_INSEL1_Pos) /**< (CCL_LUTCTRL0) I/O pin input source Position  */
#define CCL_LUTCTRL0_INSEL1_AC                (CCL_LUTCTRL0_INSEL1_AC_Val << CCL_LUTCTRL0_INSEL1_Pos) /**< (CCL_LUTCTRL0) AC input source Position  */
#define CCL_LUTCTRL0_INSEL1_TC                (CCL_LUTCTRL0_INSEL1_TC_Val << CCL_LUTCTRL0_INSEL1_Pos) /**< (CCL_LUTCTRL0) TC input source Position  */
#define CCL_LUTCTRL0_INSEL1_ALTTC             (CCL_LUTCTRL0_INSEL1_ALTTC_Val << CCL_LUTCTRL0_INSEL1_Pos) /**< (CCL_LUTCTRL0) Alternate TC input source Position  */
#define CCL_LUTCTRL0_INSEL1_SERCOM            (CCL_LUTCTRL0_INSEL1_SERCOM_Val << CCL_LUTCTRL0_INSEL1_Pos) /**< (CCL_LUTCTRL0) SERCOM input source Position  */
#define CCL_LUTCTRL0_INSEL1_ASYNCEVENT        (CCL_LUTCTRL0_INSEL1_ASYNCEVENT_Val << CCL_LUTCTRL0_INSEL1_Pos) /**< (CCL_LUTCTRL0) Asynchronous event input source Position  */
#define CCL_LUTCTRL0_INSEL2_Pos               _U_(16)                                        /**< (CCL_LUTCTRL0) Input Selection 2 Position */
#define CCL_LUTCTRL0_INSEL2_Msk               (_U_(0xF) << CCL_LUTCTRL0_INSEL2_Pos)          /**< (CCL_LUTCTRL0) Input Selection 2 Mask */
#define CCL_LUTCTRL0_INSEL2(value)            (CCL_LUTCTRL0_INSEL2_Msk & ((value) << CCL_LUTCTRL0_INSEL2_Pos))
#define   CCL_LUTCTRL0_INSEL2_MASK_Val        _U_(0x0)                                       /**< (CCL_LUTCTRL0) Masked input  */
#define   CCL_LUTCTRL0_INSEL2_FEEDBACK_Val    _U_(0x1)                                       /**< (CCL_LUTCTRL0) Feedback input source  */
#define   CCL_LUTCTRL0_INSEL2_LINK_Val        _U_(0x2)                                       /**< (CCL_LUTCTRL0) Linked LUT input source  */
#define   CCL_LUTCTRL0_INSEL2_EVENT_Val       _U_(0x3)                                       /**< (CCL_LUTCTRL0) Event input source  */
#define   CCL_LUTCTRL0_INSEL2_IO_Val          _U_(0x4)                                       /**< (CCL_LUTCTRL0) I/O pin input source  */
#define   CCL_LUTCTRL0_INSEL2_AC_Val          _U_(0x5)                                       /**< (CCL_LUTCTRL0) AC input source  */
#define   CCL_LUTCTRL0_INSEL2_TC_Val          _U_(0x6)                                       /**< (CCL_LUTCTRL0) TC input source  */
#define   CCL_LUTCTRL0_INSEL2_ALTTC_Val       _U_(0x7)                                       /**< (CCL_LUTCTRL0) Alternate TC input source  */
#define   CCL_LUTCTRL0_INSEL2_SERCOM_Val      _U_(0x9)                                       /**< (CCL_LUTCTRL0) SERCOM input source  */
#define   CCL_LUTCTRL0_INSEL2_ASYNCEVENT_Val  _U_(0xB)                                       /**< (CCL_LUTCTRL0) Asynchronous event input source  */
#define CCL_LUTCTRL0_INSEL2_MASK              (CCL_LUTCTRL0_INSEL2_MASK_Val << CCL_LUTCTRL0_INSEL2_Pos) /**< (CCL_LUTCTRL0) Masked input Position  */
#define CCL_LUTCTRL0_INSEL2_FEEDBACK          (CCL_LUTCTRL0_INSEL2_FEEDBACK_Val << CCL_LUTCTRL0_INSEL2_Pos) /**< (CCL_LUTCTRL0) Feedback input source Position  */
#define CCL_LUTCTRL0_INSEL2_LINK              (CCL_LUTCTRL0_INSEL2_LINK_Val << CCL_LUTCTRL0_INSEL2_Pos) /**< (CCL_LUTCTRL0) Linked LUT input source Position  */
#define CCL_LUTCTRL0_INSEL2_EVENT             (CCL_LUTCTRL0_INSEL2_EVENT_Val << CCL_LUTCTRL0_INSEL2_Pos) /**< (CCL_LUTCTRL0) Event input source Position  */
#define CCL_LUTCTRL0_INSEL2_IO                (CCL_LUTCTRL0_INSEL2_IO_Val << CCL_LUTCTRL0_INSEL2_Pos) /**< (CCL_LUTCTRL0) I/O pin input source Position  */
#define CCL_LUTCTRL0_INSEL2_AC                (CCL_LUTCTRL0_INSEL2_AC_Val << CCL_LUTCTRL0_INSEL2_Pos) /**< (CCL_LUTCTRL0) AC input source Position  */
#define CCL_LUTCTRL0_INSEL2_TC                (CCL_LUTCTRL0_INSEL2_TC_Val << CCL_LUTCTRL0_INSEL2_Pos) /**< (CCL_LUTCTRL0) TC input source Position  */
#define CCL_LUTCTRL0_INSEL2_ALTTC             (CCL_LUTCTRL0_INSEL2_ALTTC_Val << CCL_LUTCTRL0_INSEL2_Pos) /**< (CCL_LUTCTRL0) Alternate TC input source Position  */
#define CCL_LUTCTRL0_INSEL2_SERCOM            (CCL_LUTCTRL0_INSEL2_SERCOM_Val << CCL_LUTCTRL0_INSEL2_Pos) /**< (CCL_LUTCTRL0) SERCOM input source Position  */
#define CCL_LUTCTRL0_INSEL2_ASYNCEVENT        (CCL_LUTCTRL0_INSEL2_ASYNCEVENT_Val << CCL_LUTCTRL0_INSEL2_Pos) /**< (CCL_LUTCTRL0) Asynchronous event input source Position  */
#define CCL_LUTCTRL0_INVEI_Pos                _U_(20)                                        /**< (CCL_LUTCTRL0) Inverted Event Input Enable Position */
#define CCL_LUTCTRL0_INVEI_Msk                (_U_(0x1) << CCL_LUTCTRL0_INVEI_Pos)           /**< (CCL_LUTCTRL0) Inverted Event Input Enable Mask */
#define   CCL_LUTCTRL0_INVEI_NORMAL_Val       _U_(0x0)                                       /**< (CCL_LUTCTRL0) Incoming event is not inverted  */
#define   CCL_LUTCTRL0_INVEI_INVERTED_Val     _U_(0x1)                                       /**< (CCL_LUTCTRL0) Incoming event is inverted  */
#define CCL_LUTCTRL0_INVEI_NORMAL             (CCL_LUTCTRL0_INVEI_NORMAL_Val << CCL_LUTCTRL0_INVEI_Pos) /**< (CCL_LUTCTRL0) Incoming event is not inverted Position  */
#define CCL_LUTCTRL0_INVEI_INVERTED           (CCL_LUTCTRL0_INVEI_INVERTED_Val << CCL_LUTCTRL0_INVEI_Pos) /**< (CCL_LUTCTRL0) Incoming event is inverted Position  */
#define CCL_LUTCTRL0_LUTEI_Pos                _U_(21)                                        /**< (CCL_LUTCTRL0) LUT Event Input Enable Position */
#define CCL_LUTCTRL0_LUTEI_Msk                (_U_(0x1) << CCL_LUTCTRL0_LUTEI_Pos)           /**< (CCL_LUTCTRL0) LUT Event Input Enable Mask */
#define   CCL_LUTCTRL0_LUTEI_DISABLE_Val      _U_(0x0)                                       /**< (CCL_LUTCTRL0) LUT incoming event is disabled  */
#define   CCL_LUTCTRL0_LUTEI_ENABLE_Val       _U_(0x1)                                       /**< (CCL_LUTCTRL0) LUT incoming event is enabled  */
#define CCL_LUTCTRL0_LUTEI_DISABLE            (CCL_LUTCTRL0_LUTEI_DISABLE_Val << CCL_LUTCTRL0_LUTEI_Pos) /**< (CCL_LUTCTRL0) LUT incoming event is disabled Position  */
#define CCL_LUTCTRL0_LUTEI_ENABLE             (CCL_LUTCTRL0_LUTEI_ENABLE_Val << CCL_LUTCTRL0_LUTEI_Pos) /**< (CCL_LUTCTRL0) LUT incoming event is enabled Position  */
#define CCL_LUTCTRL0_LUTEO_Pos                _U_(22)                                        /**< (CCL_LUTCTRL0) LUT Event Output Enable Position */
#define CCL_LUTCTRL0_LUTEO_Msk                (_U_(0x1) << CCL_LUTCTRL0_LUTEO_Pos)           /**< (CCL_LUTCTRL0) LUT Event Output Enable Mask */
#define   CCL_LUTCTRL0_LUTEO_DISABLE_Val      _U_(0x0)                                       /**< (CCL_LUTCTRL0) LUT event output is disabled  */
#define   CCL_LUTCTRL0_LUTEO_ENABLE_Val       _U_(0x1)                                       /**< (CCL_LUTCTRL0) LUT event output is enabled  */
#define CCL_LUTCTRL0_LUTEO_DISABLE            (CCL_LUTCTRL0_LUTEO_DISABLE_Val << CCL_LUTCTRL0_LUTEO_Pos) /**< (CCL_LUTCTRL0) LUT event output is disabled Position  */
#define CCL_LUTCTRL0_LUTEO_ENABLE             (CCL_LUTCTRL0_LUTEO_ENABLE_Val << CCL_LUTCTRL0_LUTEO_Pos) /**< (CCL_LUTCTRL0) LUT event output is enabled Position  */
#define CCL_LUTCTRL0_TRUTH_Pos                _U_(24)                                        /**< (CCL_LUTCTRL0) Truth Value Position */
#define CCL_LUTCTRL0_TRUTH_Msk                (_U_(0xFF) << CCL_LUTCTRL0_TRUTH_Pos)          /**< (CCL_LUTCTRL0) Truth Value Mask */
#define CCL_LUTCTRL0_TRUTH(value)             (CCL_LUTCTRL0_TRUTH_Msk & ((value) << CCL_LUTCTRL0_TRUTH_Pos))
#define CCL_LUTCTRL0_Msk                      _U_(0xFF7FFFB2)                                /**< (CCL_LUTCTRL0) Register Mask  */


/* -------- CCL_LUTCTRL1 : (CCL Offset: 0x0C) (R/W 32) LUT Control 1 -------- */
#define CCL_LUTCTRL1_RESETVALUE             _U_(0x00)                                     /**<  (CCL_LUTCTRL1) LUT Control 1  Reset Value */

#define CCL_LUTCTRL1_ENABLE_Pos               _U_(1)                                         /**< (CCL_LUTCTRL1) LUT Enable Position */
#define CCL_LUTCTRL1_ENABLE_Msk               (_U_(0x1) << CCL_LUTCTRL1_ENABLE_Pos)          /**< (CCL_LUTCTRL1) LUT Enable Mask */
#define   CCL_LUTCTRL1_ENABLE_DISABLE_Val     _U_(0x0)                                       /**< (CCL_LUTCTRL1) The LUT is disabled  */
#define   CCL_LUTCTRL1_ENABLE_ENABLE_Val      _U_(0x1)                                       /**< (CCL_LUTCTRL1) The LUT is enabled  */
#define CCL_LUTCTRL1_ENABLE_DISABLE           (CCL_LUTCTRL1_ENABLE_DISABLE_Val << CCL_LUTCTRL1_ENABLE_Pos) /**< (CCL_LUTCTRL1) The LUT is disabled Position  */
#define CCL_LUTCTRL1_ENABLE_ENABLE            (CCL_LUTCTRL1_ENABLE_ENABLE_Val << CCL_LUTCTRL1_ENABLE_Pos) /**< (CCL_LUTCTRL1) The LUT is enabled Position  */
#define CCL_LUTCTRL1_FILTSEL_Pos              _U_(4)                                         /**< (CCL_LUTCTRL1) Filter Selection Position */
#define CCL_LUTCTRL1_FILTSEL_Msk              (_U_(0x3) << CCL_LUTCTRL1_FILTSEL_Pos)         /**< (CCL_LUTCTRL1) Filter Selection Mask */
#define CCL_LUTCTRL1_FILTSEL(value)           (CCL_LUTCTRL1_FILTSEL_Msk & ((value) << CCL_LUTCTRL1_FILTSEL_Pos))
#define   CCL_LUTCTRL1_FILTSEL_DISABLE_Val    _U_(0x0)                                       /**< (CCL_LUTCTRL1) Filter disabled  */
#define   CCL_LUTCTRL1_FILTSEL_SYNCH_Val      _U_(0x1)                                       /**< (CCL_LUTCTRL1) Synchronizer enabled  */
#define   CCL_LUTCTRL1_FILTSEL_FILTER_Val     _U_(0x2)                                       /**< (CCL_LUTCTRL1) Filter enabled  */
#define CCL_LUTCTRL1_FILTSEL_DISABLE          (CCL_LUTCTRL1_FILTSEL_DISABLE_Val << CCL_LUTCTRL1_FILTSEL_Pos) /**< (CCL_LUTCTRL1) Filter disabled Position  */
#define CCL_LUTCTRL1_FILTSEL_SYNCH            (CCL_LUTCTRL1_FILTSEL_SYNCH_Val << CCL_LUTCTRL1_FILTSEL_Pos) /**< (CCL_LUTCTRL1) Synchronizer enabled Position  */
#define CCL_LUTCTRL1_FILTSEL_FILTER           (CCL_LUTCTRL1_FILTSEL_FILTER_Val << CCL_LUTCTRL1_FILTSEL_Pos) /**< (CCL_LUTCTRL1) Filter enabled Position  */
#define CCL_LUTCTRL1_EDGESEL_Pos              _U_(7)                                         /**< (CCL_LUTCTRL1) Edge Selection Position */
#define CCL_LUTCTRL1_EDGESEL_Msk              (_U_(0x1) << CCL_LUTCTRL1_EDGESEL_Pos)         /**< (CCL_LUTCTRL1) Edge Selection Mask */
#define   CCL_LUTCTRL1_EDGESEL_DISABLED_Val   _U_(0x0)                                       /**< (CCL_LUTCTRL1) Edge detector is disabled  */
#define   CCL_LUTCTRL1_EDGESEL_ENABLED_Val    _U_(0x1)                                       /**< (CCL_LUTCTRL1) Edge detector is enabled  */
#define CCL_LUTCTRL1_EDGESEL_DISABLED         (CCL_LUTCTRL1_EDGESEL_DISABLED_Val << CCL_LUTCTRL1_EDGESEL_Pos) /**< (CCL_LUTCTRL1) Edge detector is disabled Position  */
#define CCL_LUTCTRL1_EDGESEL_ENABLED          (CCL_LUTCTRL1_EDGESEL_ENABLED_Val << CCL_LUTCTRL1_EDGESEL_Pos) /**< (CCL_LUTCTRL1) Edge detector is enabled Position  */
#define CCL_LUTCTRL1_INSEL0_Pos               _U_(8)                                         /**< (CCL_LUTCTRL1) Input Selection 0 Position */
#define CCL_LUTCTRL1_INSEL0_Msk               (_U_(0xF) << CCL_LUTCTRL1_INSEL0_Pos)          /**< (CCL_LUTCTRL1) Input Selection 0 Mask */
#define CCL_LUTCTRL1_INSEL0(value)            (CCL_LUTCTRL1_INSEL0_Msk & ((value) << CCL_LUTCTRL1_INSEL0_Pos))
#define   CCL_LUTCTRL1_INSEL0_MASK_Val        _U_(0x0)                                       /**< (CCL_LUTCTRL1) Masked input  */
#define   CCL_LUTCTRL1_INSEL0_FEEDBACK_Val    _U_(0x1)                                       /**< (CCL_LUTCTRL1) Feedback input source  */
#define   CCL_LUTCTRL1_INSEL0_LINK_Val        _U_(0x2)                                       /**< (CCL_LUTCTRL1) Linked LUT input source  */
#define   CCL_LUTCTRL1_INSEL0_EVENT_Val       _U_(0x3)                                       /**< (CCL_LUTCTRL1) Event input source  */
#define   CCL_LUTCTRL1_INSEL0_IO_Val          _U_(0x4)                                       /**< (CCL_LUTCTRL1) I/O pin input source  */
#define   CCL_LUTCTRL1_INSEL0_AC_Val          _U_(0x5)                                       /**< (CCL_LUTCTRL1) AC input source  */
#define   CCL_LUTCTRL1_INSEL0_TC_Val          _U_(0x6)                                       /**< (CCL_LUTCTRL1) TC input source  */
#define   CCL_LUTCTRL1_INSEL0_ALTTC_Val       _U_(0x7)                                       /**< (CCL_LUTCTRL1) Alternate TC input source  */
#define   CCL_LUTCTRL1_INSEL0_SERCOM_Val      _U_(0x9)                                       /**< (CCL_LUTCTRL1) SERCOM input source  */
#define   CCL_LUTCTRL1_INSEL0_ASYNCEVENT_Val  _U_(0xB)                                       /**< (CCL_LUTCTRL1) Asynchronous event input source  */
#define CCL_LUTCTRL1_INSEL0_MASK              (CCL_LUTCTRL1_INSEL0_MASK_Val << CCL_LUTCTRL1_INSEL0_Pos) /**< (CCL_LUTCTRL1) Masked input Position  */
#define CCL_LUTCTRL1_INSEL0_FEEDBACK          (CCL_LUTCTRL1_INSEL0_FEEDBACK_Val << CCL_LUTCTRL1_INSEL0_Pos) /**< (CCL_LUTCTRL1) Feedback input source Position  */
#define CCL_LUTCTRL1_INSEL0_LINK              (CCL_LUTCTRL1_INSEL0_LINK_Val << CCL_LUTCTRL1_INSEL0_Pos) /**< (CCL_LUTCTRL1) Linked LUT input source Position  */
#define CCL_LUTCTRL1_INSEL0_EVENT             (CCL_LUTCTRL1_INSEL0_EVENT_Val << CCL_LUTCTRL1_INSEL0_Pos) /**< (CCL_LUTCTRL1) Event input source Position  */
#define CCL_LUTCTRL1_INSEL0_IO                (CCL_LUTCTRL1_INSEL0_IO_Val << CCL_LUTCTRL1_INSEL0_Pos) /**< (CCL_LUTCTRL1) I/O pin input source Position  */
#define CCL_LUTCTRL1_INSEL0_AC                (CCL_LUTCTRL1_INSEL0_AC_Val << CCL_LUTCTRL1_INSEL0_Pos) /**< (CCL_LUTCTRL1) AC input source Position  */
#define CCL_LUTCTRL1_INSEL0_TC                (CCL_LUTCTRL1_INSEL0_TC_Val << CCL_LUTCTRL1_INSEL0_Pos) /**< (CCL_LUTCTRL1) TC input source Position  */
#define CCL_LUTCTRL1_INSEL0_ALTTC             (CCL_LUTCTRL1_INSEL0_ALTTC_Val << CCL_LUTCTRL1_INSEL0_Pos) /**< (CCL_LUTCTRL1) Alternate TC input source Position  */
#define CCL_LUTCTRL1_INSEL0_SERCOM            (CCL_LUTCTRL1_INSEL0_SERCOM_Val << CCL_LUTCTRL1_INSEL0_Pos) /**< (CCL_LUTCTRL1) SERCOM input source Position  */
#define CCL_LUTCTRL1_INSEL0_ASYNCEVENT        (CCL_LUTCTRL1_INSEL0_ASYNCEVENT_Val << CCL_LUTCTRL1_INSEL0_Pos) /**< (CCL_LUTCTRL1) Asynchronous event input source Position  */
#define CCL_LUTCTRL1_INSEL1_Pos               _U_(12)                                        /**< (CCL_LUTCTRL1) Input Selection 1 Position */
#define CCL_LUTCTRL1_INSEL1_Msk               (_U_(0xF) << CCL_LUTCTRL1_INSEL1_Pos)          /**< (CCL_LUTCTRL1) Input Selection 1 Mask */
#define CCL_LUTCTRL1_INSEL1(value)            (CCL_LUTCTRL1_INSEL1_Msk & ((value) << CCL_LUTCTRL1_INSEL1_Pos))
#define   CCL_LUTCTRL1_INSEL1_MASK_Val        _U_(0x0)                                       /**< (CCL_LUTCTRL1) Masked input  */
#define   CCL_LUTCTRL1_INSEL1_FEEDBACK_Val    _U_(0x1)                                       /**< (CCL_LUTCTRL1) Feedback input source  */
#define   CCL_LUTCTRL1_INSEL1_LINK_Val        _U_(0x2)                                       /**< (CCL_LUTCTRL1) Linked LUT input source  */
#define   CCL_LUTCTRL1_INSEL1_EVENT_Val       _U_(0x3)                                       /**< (CCL_LUTCTRL1) Event input source  */
#define   CCL_LUTCTRL1_INSEL1_IO_Val          _U_(0x4)                                       /**< (CCL_LUTCTRL1) I/O pin input source  */
#define   CCL_LUTCTRL1_INSEL1_AC_Val          _U_(0x5)                                       /**< (CCL_LUTCTRL1) AC input source  */
#define   CCL_LUTCTRL1_INSEL1_TC_Val          _U_(0x6)                                       /**< (CCL_LUTCTRL1) TC input source  */
#define   CCL_LUTCTRL1_INSEL1_ALTTC_Val       _U_(0x7)                                       /**< (CCL_LUTCTRL1) Alternate TC input source  */
#define   CCL_LUTCTRL1_INSEL1_SERCOM_Val      _U_(0x9)                                       /**< (CCL_LUTCTRL1) SERCOM input source  */
#define   CCL_LUTCTRL1_INSEL1_ASYNCEVENT_Val  _U_(0xB)                                       /**< (CCL_LUTCTRL1) Asynchronous event input source  */
#define CCL_LUTCTRL1_INSEL1_MASK              (CCL_LUTCTRL1_INSEL1_MASK_Val << CCL_LUTCTRL1_INSEL1_Pos) /**< (CCL_LUTCTRL1) Masked input Position  */
#define CCL_LUTCTRL1_INSEL1_FEEDBACK          (CCL_LUTCTRL1_INSEL1_FEEDBACK_Val << CCL_LUTCTRL1_INSEL1_Pos) /**< (CCL_LUTCTRL1) Feedback input source Position  */
#define CCL_LUTCTRL1_INSEL1_LINK              (CCL_LUTCTRL1_INSEL1_LINK_Val << CCL_LUTCTRL1_INSEL1_Pos) /**< (CCL_LUTCTRL1) Linked LUT input source Position  */
#define CCL_LUTCTRL1_INSEL1_EVENT             (CCL_LUTCTRL1_INSEL1_EVENT_Val << CCL_LUTCTRL1_INSEL1_Pos) /**< (CCL_LUTCTRL1) Event input source Position  */
#define CCL_LUTCTRL1_INSEL1_IO                (CCL_LUTCTRL1_INSEL1_IO_Val << CCL_LUTCTRL1_INSEL1_Pos) /**< (CCL_LUTCTRL1) I/O pin input source Position  */
#define CCL_LUTCTRL1_INSEL1_AC                (CCL_LUTCTRL1_INSEL1_AC_Val << CCL_LUTCTRL1_INSEL1_Pos) /**< (CCL_LUTCTRL1) AC input source Position  */
#define CCL_LUTCTRL1_INSEL1_TC                (CCL_LUTCTRL1_INSEL1_TC_Val << CCL_LUTCTRL1_INSEL1_Pos) /**< (CCL_LUTCTRL1) TC input source Position  */
#define CCL_LUTCTRL1_INSEL1_ALTTC             (CCL_LUTCTRL1_INSEL1_ALTTC_Val << CCL_LUTCTRL1_INSEL1_Pos) /**< (CCL_LUTCTRL1) Alternate TC input source Position  */
#define CCL_LUTCTRL1_INSEL1_SERCOM            (CCL_LUTCTRL1_INSEL1_SERCOM_Val << CCL_LUTCTRL1_INSEL1_Pos) /**< (CCL_LUTCTRL1) SERCOM input source Position  */
#define CCL_LUTCTRL1_INSEL1_ASYNCEVENT        (CCL_LUTCTRL1_INSEL1_ASYNCEVENT_Val << CCL_LUTCTRL1_INSEL1_Pos) /**< (CCL_LUTCTRL1) Asynchronous event input source Position  */
#define CCL_LUTCTRL1_INSEL2_Pos               _U_(16)                                        /**< (CCL_LUTCTRL1) Input Selection 2 Position */
#define CCL_LUTCTRL1_INSEL2_Msk               (_U_(0xF) << CCL_LUTCTRL1_INSEL2_Pos)          /**< (CCL_LUTCTRL1) Input Selection 2 Mask */
#define CCL_LUTCTRL1_INSEL2(value)            (CCL_LUTCTRL1_INSEL2_Msk & ((value) << CCL_LUTCTRL1_INSEL2_Pos))
#define   CCL_LUTCTRL1_INSEL2_MASK_Val        _U_(0x0)                                       /**< (CCL_LUTCTRL1) Masked input  */
#define   CCL_LUTCTRL1_INSEL2_FEEDBACK_Val    _U_(0x1)                                       /**< (CCL_LUTCTRL1) Feedback input source  */
#define   CCL_LUTCTRL1_INSEL2_LINK_Val        _U_(0x2)                                       /**< (CCL_LUTCTRL1) Linked LUT input source  */
#define   CCL_LUTCTRL1_INSEL2_EVENT_Val       _U_(0x3)                                       /**< (CCL_LUTCTRL1) Event input source  */
#define   CCL_LUTCTRL1_INSEL2_IO_Val          _U_(0x4)                                       /**< (CCL_LUTCTRL1) I/O pin input source  */
#define   CCL_LUTCTRL1_INSEL2_AC_Val          _U_(0x5)                                       /**< (CCL_LUTCTRL1) AC input source  */
#define   CCL_LUTCTRL1_INSEL2_TC_Val          _U_(0x6)                                       /**< (CCL_LUTCTRL1) TC input source  */
#define   CCL_LUTCTRL1_INSEL2_ALTTC_Val       _U_(0x7)                                       /**< (CCL_LUTCTRL1) Alternate TC input source  */
#define   CCL_LUTCTRL1_INSEL2_SERCOM_Val      _U_(0x9)                                       /**< (CCL_LUTCTRL1) SERCOM input source  */
#define   CCL_LUTCTRL1_INSEL2_ASYNCEVENT_Val  _U_(0xB)                                       /**< (CCL_LUTCTRL1) Asynchronous event input source  */
#define CCL_LUTCTRL1_INSEL2_MASK              (CCL_LUTCTRL1_INSEL2_MASK_Val << CCL_LUTCTRL1_INSEL2_Pos) /**< (CCL_LUTCTRL1) Masked input Position  */
#define CCL_LUTCTRL1_INSEL2_FEEDBACK          (CCL_LUTCTRL1_INSEL2_FEEDBACK_Val << CCL_LUTCTRL1_INSEL2_Pos) /**< (CCL_LUTCTRL1) Feedback input source Position  */
#define CCL_LUTCTRL1_INSEL2_LINK              (CCL_LUTCTRL1_INSEL2_LINK_Val << CCL_LUTCTRL1_INSEL2_Pos) /**< (CCL_LUTCTRL1) Linked LUT input source Position  */
#define CCL_LUTCTRL1_INSEL2_EVENT             (CCL_LUTCTRL1_INSEL2_EVENT_Val << CCL_LUTCTRL1_INSEL2_Pos) /**< (CCL_LUTCTRL1) Event input source Position  */
#define CCL_LUTCTRL1_INSEL2_IO                (CCL_LUTCTRL1_INSEL2_IO_Val << CCL_LUTCTRL1_INSEL2_Pos) /**< (CCL_LUTCTRL1) I/O pin input source Position  */
#define CCL_LUTCTRL1_INSEL2_AC                (CCL_LUTCTRL1_INSEL2_AC_Val << CCL_LUTCTRL1_INSEL2_Pos) /**< (CCL_LUTCTRL1) AC input source Position  */
#define CCL_LUTCTRL1_INSEL2_TC                (CCL_LUTCTRL1_INSEL2_TC_Val << CCL_LUTCTRL1_INSEL2_Pos) /**< (CCL_LUTCTRL1) TC input source Position  */
#define CCL_LUTCTRL1_INSEL2_ALTTC             (CCL_LUTCTRL1_INSEL2_ALTTC_Val << CCL_LUTCTRL1_INSEL2_Pos) /**< (CCL_LUTCTRL1) Alternate TC input source Position  */
#define CCL_LUTCTRL1_INSEL2_SERCOM            (CCL_LUTCTRL1_INSEL2_SERCOM_Val << CCL_LUTCTRL1_INSEL2_Pos) /**< (CCL_LUTCTRL1) SERCOM input source Position  */
#define CCL_LUTCTRL1_INSEL2_ASYNCEVENT        (CCL_LUTCTRL1_INSEL2_ASYNCEVENT_Val << CCL_LUTCTRL1_INSEL2_Pos) /**< (CCL_LUTCTRL1) Asynchronous event input source Position  */
#define CCL_LUTCTRL1_INVEI_Pos                _U_(20)                                        /**< (CCL_LUTCTRL1) Inverted Event Input Enable Position */
#define CCL_LUTCTRL1_INVEI_Msk                (_U_(0x1) << CCL_LUTCTRL1_INVEI_Pos)           /**< (CCL_LUTCTRL1) Inverted Event Input Enable Mask */
#define   CCL_LUTCTRL1_INVEI_NORMAL_Val       _U_(0x0)                                       /**< (CCL_LUTCTRL1) Incoming event is not inverted  */
#define   CCL_LUTCTRL1_INVEI_INVERTED_Val     _U_(0x1)                                       /**< (CCL_LUTCTRL1) Incoming event is inverted  */
#define CCL_LUTCTRL1_INVEI_NORMAL             (CCL_LUTCTRL1_INVEI_NORMAL_Val << CCL_LUTCTRL1_INVEI_Pos) /**< (CCL_LUTCTRL1) Incoming event is not inverted Position  */
#define CCL_LUTCTRL1_INVEI_INVERTED           (CCL_LUTCTRL1_INVEI_INVERTED_Val << CCL_LUTCTRL1_INVEI_Pos) /**< (CCL_LUTCTRL1) Incoming event is inverted Position  */
#define CCL_LUTCTRL1_LUTEI_Pos                _U_(21)                                        /**< (CCL_LUTCTRL1) LUT Event Input Enable Position */
#define CCL_LUTCTRL1_LUTEI_Msk                (_U_(0x1) << CCL_LUTCTRL1_LUTEI_Pos)           /**< (CCL_LUTCTRL1) LUT Event Input Enable Mask */
#define   CCL_LUTCTRL1_LUTEI_DISABLE_Val      _U_(0x0)                                       /**< (CCL_LUTCTRL1) LUT incoming event is disabled  */
#define   CCL_LUTCTRL1_LUTEI_ENABLE_Val       _U_(0x1)                                       /**< (CCL_LUTCTRL1) LUT incoming event is enabled  */
#define CCL_LUTCTRL1_LUTEI_DISABLE            (CCL_LUTCTRL1_LUTEI_DISABLE_Val << CCL_LUTCTRL1_LUTEI_Pos) /**< (CCL_LUTCTRL1) LUT incoming event is disabled Position  */
#define CCL_LUTCTRL1_LUTEI_ENABLE             (CCL_LUTCTRL1_LUTEI_ENABLE_Val << CCL_LUTCTRL1_LUTEI_Pos) /**< (CCL_LUTCTRL1) LUT incoming event is enabled Position  */
#define CCL_LUTCTRL1_LUTEO_Pos                _U_(22)                                        /**< (CCL_LUTCTRL1) LUT Event Output Enable Position */
#define CCL_LUTCTRL1_LUTEO_Msk                (_U_(0x1) << CCL_LUTCTRL1_LUTEO_Pos)           /**< (CCL_LUTCTRL1) LUT Event Output Enable Mask */
#define   CCL_LUTCTRL1_LUTEO_DISABLE_Val      _U_(0x0)                                       /**< (CCL_LUTCTRL1) LUT event output is disabled  */
#define   CCL_LUTCTRL1_LUTEO_ENABLE_Val       _U_(0x1)                                       /**< (CCL_LUTCTRL1) LUT event output is enabled  */
#define CCL_LUTCTRL1_LUTEO_DISABLE            (CCL_LUTCTRL1_LUTEO_DISABLE_Val << CCL_LUTCTRL1_LUTEO_Pos) /**< (CCL_LUTCTRL1) LUT event output is disabled Position  */
#define CCL_LUTCTRL1_LUTEO_ENABLE             (CCL_LUTCTRL1_LUTEO_ENABLE_Val << CCL_LUTCTRL1_LUTEO_Pos) /**< (CCL_LUTCTRL1) LUT event output is enabled Position  */
#define CCL_LUTCTRL1_TRUTH_Pos                _U_(24)                                        /**< (CCL_LUTCTRL1) Truth Value Position */
#define CCL_LUTCTRL1_TRUTH_Msk                (_U_(0xFF) << CCL_LUTCTRL1_TRUTH_Pos)          /**< (CCL_LUTCTRL1) Truth Value Mask */
#define CCL_LUTCTRL1_TRUTH(value)             (CCL_LUTCTRL1_TRUTH_Msk & ((value) << CCL_LUTCTRL1_TRUTH_Pos))
#define CCL_LUTCTRL1_Msk                      _U_(0xFF7FFFB2)                                /**< (CCL_LUTCTRL1) Register Mask  */


/** \brief CCL register offsets definitions */
#define CCL_CTRL_REG_OFST              (0x00)         /**< (CCL_CTRL) Control Offset */
#define CCL_SEQCTRL0_REG_OFST          (0x04)         /**< (CCL_SEQCTRL0) SEQ Control 0 Offset */
#define CCL_LUTCTRL0_REG_OFST          (0x08)         /**< (CCL_LUTCTRL0) LUT Control 0 Offset */
#define CCL_LUTCTRL1_REG_OFST          (0x0C)         /**< (CCL_LUTCTRL1) LUT Control 1 Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief CCL register API structure */
typedef struct
{  /* Configurable Custom Logic */
  __IO  uint8_t                        CCL_CTRL;        /**< Offset: 0x00 (R/W  8) Control */
  __I   uint8_t                        Reserved1[0x03];
  __IO  uint8_t                        CCL_SEQCTRL0;    /**< Offset: 0x04 (R/W  8) SEQ Control 0 */
  __I   uint8_t                        Reserved2[0x03];
  __IO  uint32_t                       CCL_LUTCTRL0;    /**< Offset: 0x08 (R/W  32) LUT Control 0 */
  __IO  uint32_t                       CCL_LUTCTRL1;    /**< Offset: 0x0C (R/W  32) LUT Control 1 */
} ccl_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAML10_CCL_COMPONENT_H_ */
