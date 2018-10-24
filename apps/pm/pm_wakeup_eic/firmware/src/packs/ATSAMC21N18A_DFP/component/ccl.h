/**
 * \brief Header file for SAMC/SAMC21 CCL
 *
 * Copyright (c) 2017-2018 Microchip Technology Inc.
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

/* file generated from device description version 2018-06-27T08:27:01Z */
#ifndef SAMC_SAMC21_CCL_MODULE_H
#define SAMC_SAMC21_CCL_MODULE_H

/** \addtogroup SAMC_SAMC21 Configurable Custom Logic
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_CCL                                   */
/* ========================================================================== */

/* -------- CCL_CTRL : (CCL Offset: 0x00) (R/W 8) Control -------- */
#define CCL_CTRL_SWRST_Pos                    (0U)                                           /**< (CCL_CTRL) Software Reset Position */
#define CCL_CTRL_SWRST_Msk                    (0x1U << CCL_CTRL_SWRST_Pos)                   /**< (CCL_CTRL) Software Reset Mask */
#define CCL_CTRL_SWRST(value)                 (CCL_CTRL_SWRST_Msk & ((value) << CCL_CTRL_SWRST_Pos))
#define CCL_CTRL_ENABLE_Pos                   (1U)                                           /**< (CCL_CTRL) Enable Position */
#define CCL_CTRL_ENABLE_Msk                   (0x1U << CCL_CTRL_ENABLE_Pos)                  /**< (CCL_CTRL) Enable Mask */
#define CCL_CTRL_ENABLE(value)                (CCL_CTRL_ENABLE_Msk & ((value) << CCL_CTRL_ENABLE_Pos))
#define CCL_CTRL_RUNSTDBY_Pos                 (6U)                                           /**< (CCL_CTRL) Run during Standby Position */
#define CCL_CTRL_RUNSTDBY_Msk                 (0x1U << CCL_CTRL_RUNSTDBY_Pos)                /**< (CCL_CTRL) Run during Standby Mask */
#define CCL_CTRL_RUNSTDBY(value)              (CCL_CTRL_RUNSTDBY_Msk & ((value) << CCL_CTRL_RUNSTDBY_Pos))
#define CCL_CTRL_Msk                          (0x00000043UL)                                 /**< (CCL_CTRL) Register Mask  */

/* -------- CCL_SEQCTRL : (CCL Offset: 0x04) (R/W 8) SEQ Control x -------- */
#define CCL_SEQCTRL_SEQSEL_Pos                (0U)                                           /**< (CCL_SEQCTRL) Sequential Selection Position */
#define CCL_SEQCTRL_SEQSEL_Msk                (0xFU << CCL_SEQCTRL_SEQSEL_Pos)               /**< (CCL_SEQCTRL) Sequential Selection Mask */
#define CCL_SEQCTRL_SEQSEL(value)             (CCL_SEQCTRL_SEQSEL_Msk & ((value) << CCL_SEQCTRL_SEQSEL_Pos))
#define   CCL_SEQCTRL_SEQSEL_DISABLE_Val      (0U)                                           /**< (CCL_SEQCTRL) Sequential logic is disabled  */
#define   CCL_SEQCTRL_SEQSEL_DFF_Val          (1U)                                           /**< (CCL_SEQCTRL) D flip flop  */
#define   CCL_SEQCTRL_SEQSEL_JK_Val           (2U)                                           /**< (CCL_SEQCTRL) JK flip flop  */
#define   CCL_SEQCTRL_SEQSEL_LATCH_Val        (3U)                                           /**< (CCL_SEQCTRL) D latch  */
#define   CCL_SEQCTRL_SEQSEL_RS_Val           (4U)                                           /**< (CCL_SEQCTRL) RS latch  */
#define CCL_SEQCTRL_SEQSEL_DISABLE            (CCL_SEQCTRL_SEQSEL_DISABLE_Val << CCL_SEQCTRL_SEQSEL_Pos) /**< (CCL_SEQCTRL) Sequential logic is disabled Position  */
#define CCL_SEQCTRL_SEQSEL_DFF                (CCL_SEQCTRL_SEQSEL_DFF_Val << CCL_SEQCTRL_SEQSEL_Pos) /**< (CCL_SEQCTRL) D flip flop Position  */
#define CCL_SEQCTRL_SEQSEL_JK                 (CCL_SEQCTRL_SEQSEL_JK_Val << CCL_SEQCTRL_SEQSEL_Pos) /**< (CCL_SEQCTRL) JK flip flop Position  */
#define CCL_SEQCTRL_SEQSEL_LATCH              (CCL_SEQCTRL_SEQSEL_LATCH_Val << CCL_SEQCTRL_SEQSEL_Pos) /**< (CCL_SEQCTRL) D latch Position  */
#define CCL_SEQCTRL_SEQSEL_RS                 (CCL_SEQCTRL_SEQSEL_RS_Val << CCL_SEQCTRL_SEQSEL_Pos) /**< (CCL_SEQCTRL) RS latch Position  */
#define CCL_SEQCTRL_Msk                       (0x0000000FUL)                                 /**< (CCL_SEQCTRL) Register Mask  */

/* -------- CCL_LUTCTRL : (CCL Offset: 0x08) (R/W 32) LUT Control x -------- */
#define CCL_LUTCTRL_ENABLE_Pos                (1U)                                           /**< (CCL_LUTCTRL) LUT Enable Position */
#define CCL_LUTCTRL_ENABLE_Msk                (0x1U << CCL_LUTCTRL_ENABLE_Pos)               /**< (CCL_LUTCTRL) LUT Enable Mask */
#define CCL_LUTCTRL_ENABLE(value)             (CCL_LUTCTRL_ENABLE_Msk & ((value) << CCL_LUTCTRL_ENABLE_Pos))
#define CCL_LUTCTRL_FILTSEL_Pos               (4U)                                           /**< (CCL_LUTCTRL) Filter Selection Position */
#define CCL_LUTCTRL_FILTSEL_Msk               (0x3U << CCL_LUTCTRL_FILTSEL_Pos)              /**< (CCL_LUTCTRL) Filter Selection Mask */
#define CCL_LUTCTRL_FILTSEL(value)            (CCL_LUTCTRL_FILTSEL_Msk & ((value) << CCL_LUTCTRL_FILTSEL_Pos))
#define   CCL_LUTCTRL_FILTSEL_DISABLE_Val     (0U)                                           /**< (CCL_LUTCTRL) Filter disabled  */
#define   CCL_LUTCTRL_FILTSEL_SYNCH_Val       (1U)                                           /**< (CCL_LUTCTRL) Synchronizer enabled  */
#define   CCL_LUTCTRL_FILTSEL_FILTER_Val      (2U)                                           /**< (CCL_LUTCTRL) Filter enabled  */
#define CCL_LUTCTRL_FILTSEL_DISABLE           (CCL_LUTCTRL_FILTSEL_DISABLE_Val << CCL_LUTCTRL_FILTSEL_Pos) /**< (CCL_LUTCTRL) Filter disabled Position  */
#define CCL_LUTCTRL_FILTSEL_SYNCH             (CCL_LUTCTRL_FILTSEL_SYNCH_Val << CCL_LUTCTRL_FILTSEL_Pos) /**< (CCL_LUTCTRL) Synchronizer enabled Position  */
#define CCL_LUTCTRL_FILTSEL_FILTER            (CCL_LUTCTRL_FILTSEL_FILTER_Val << CCL_LUTCTRL_FILTSEL_Pos) /**< (CCL_LUTCTRL) Filter enabled Position  */
#define CCL_LUTCTRL_EDGESEL_Pos               (7U)                                           /**< (CCL_LUTCTRL) Edge Selection Position */
#define CCL_LUTCTRL_EDGESEL_Msk               (0x1U << CCL_LUTCTRL_EDGESEL_Pos)              /**< (CCL_LUTCTRL) Edge Selection Mask */
#define CCL_LUTCTRL_EDGESEL(value)            (CCL_LUTCTRL_EDGESEL_Msk & ((value) << CCL_LUTCTRL_EDGESEL_Pos))
#define CCL_LUTCTRL_INSEL0_Pos                (8U)                                           /**< (CCL_LUTCTRL) Input Selection 0 Position */
#define CCL_LUTCTRL_INSEL0_Msk                (0xFU << CCL_LUTCTRL_INSEL0_Pos)               /**< (CCL_LUTCTRL) Input Selection 0 Mask */
#define CCL_LUTCTRL_INSEL0(value)             (CCL_LUTCTRL_INSEL0_Msk & ((value) << CCL_LUTCTRL_INSEL0_Pos))
#define   CCL_LUTCTRL_INSEL0_MASK_Val         (0U)                                           /**< (CCL_LUTCTRL) Masked input  */
#define   CCL_LUTCTRL_INSEL0_FEEDBACK_Val     (1U)                                           /**< (CCL_LUTCTRL) Feedback input source  */
#define   CCL_LUTCTRL_INSEL0_LINK_Val         (2U)                                           /**< (CCL_LUTCTRL) Linked LUT input source  */
#define   CCL_LUTCTRL_INSEL0_EVENT_Val        (3U)                                           /**< (CCL_LUTCTRL) Event in put source  */
#define   CCL_LUTCTRL_INSEL0_IO_Val           (4U)                                           /**< (CCL_LUTCTRL) I/O pin input source  */
#define   CCL_LUTCTRL_INSEL0_AC_Val           (5U)                                           /**< (CCL_LUTCTRL) AC input source  */
#define   CCL_LUTCTRL_INSEL0_TC_Val           (6U)                                           /**< (CCL_LUTCTRL) TC input source  */
#define   CCL_LUTCTRL_INSEL0_ALTTC_Val        (7U)                                           /**< (CCL_LUTCTRL) Alternate TC input source  */
#define   CCL_LUTCTRL_INSEL0_TCC_Val          (8U)                                           /**< (CCL_LUTCTRL) TCC input source  */
#define   CCL_LUTCTRL_INSEL0_SERCOM_Val       (9U)                                           /**< (CCL_LUTCTRL) SERCOM inout source  */
#define   CCL_LUTCTRL_INSEL0_ALT2TC_Val       (10U)                                          /**< (CCL_LUTCTRL) Alternate 2 TC input source  */
#define   CCL_LUTCTRL_INSEL0_ASYNCEVENT_Val   (11U)                                          /**< (CCL_LUTCTRL) ASYNC EVENT input source. The EVENT input will bypass edge detection logic.  */
#define CCL_LUTCTRL_INSEL0_MASK               (CCL_LUTCTRL_INSEL0_MASK_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) Masked input Position  */
#define CCL_LUTCTRL_INSEL0_FEEDBACK           (CCL_LUTCTRL_INSEL0_FEEDBACK_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) Feedback input source Position  */
#define CCL_LUTCTRL_INSEL0_LINK               (CCL_LUTCTRL_INSEL0_LINK_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) Linked LUT input source Position  */
#define CCL_LUTCTRL_INSEL0_EVENT              (CCL_LUTCTRL_INSEL0_EVENT_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) Event in put source Position  */
#define CCL_LUTCTRL_INSEL0_IO                 (CCL_LUTCTRL_INSEL0_IO_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) I/O pin input source Position  */
#define CCL_LUTCTRL_INSEL0_AC                 (CCL_LUTCTRL_INSEL0_AC_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) AC input source Position  */
#define CCL_LUTCTRL_INSEL0_TC                 (CCL_LUTCTRL_INSEL0_TC_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) TC input source Position  */
#define CCL_LUTCTRL_INSEL0_ALTTC              (CCL_LUTCTRL_INSEL0_ALTTC_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) Alternate TC input source Position  */
#define CCL_LUTCTRL_INSEL0_TCC                (CCL_LUTCTRL_INSEL0_TCC_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) TCC input source Position  */
#define CCL_LUTCTRL_INSEL0_SERCOM             (CCL_LUTCTRL_INSEL0_SERCOM_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) SERCOM inout source Position  */
#define CCL_LUTCTRL_INSEL0_ALT2TC             (CCL_LUTCTRL_INSEL0_ALT2TC_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) Alternate 2 TC input source Position  */
#define CCL_LUTCTRL_INSEL0_ASYNCEVENT         (CCL_LUTCTRL_INSEL0_ASYNCEVENT_Val << CCL_LUTCTRL_INSEL0_Pos) /**< (CCL_LUTCTRL) ASYNC EVENT input source. The EVENT input will bypass edge detection logic. Position  */
#define CCL_LUTCTRL_INSEL1_Pos                (12U)                                          /**< (CCL_LUTCTRL) Input Selection 1 Position */
#define CCL_LUTCTRL_INSEL1_Msk                (0xFU << CCL_LUTCTRL_INSEL1_Pos)               /**< (CCL_LUTCTRL) Input Selection 1 Mask */
#define CCL_LUTCTRL_INSEL1(value)             (CCL_LUTCTRL_INSEL1_Msk & ((value) << CCL_LUTCTRL_INSEL1_Pos))
#define CCL_LUTCTRL_INSEL2_Pos                (16U)                                          /**< (CCL_LUTCTRL) Input Selection 2 Position */
#define CCL_LUTCTRL_INSEL2_Msk                (0xFU << CCL_LUTCTRL_INSEL2_Pos)               /**< (CCL_LUTCTRL) Input Selection 2 Mask */
#define CCL_LUTCTRL_INSEL2(value)             (CCL_LUTCTRL_INSEL2_Msk & ((value) << CCL_LUTCTRL_INSEL2_Pos))
#define CCL_LUTCTRL_INVEI_Pos                 (20U)                                          /**< (CCL_LUTCTRL) Input Event Invert Position */
#define CCL_LUTCTRL_INVEI_Msk                 (0x1U << CCL_LUTCTRL_INVEI_Pos)                /**< (CCL_LUTCTRL) Input Event Invert Mask */
#define CCL_LUTCTRL_INVEI(value)              (CCL_LUTCTRL_INVEI_Msk & ((value) << CCL_LUTCTRL_INVEI_Pos))
#define CCL_LUTCTRL_LUTEI_Pos                 (21U)                                          /**< (CCL_LUTCTRL) Event Input Enable Position */
#define CCL_LUTCTRL_LUTEI_Msk                 (0x1U << CCL_LUTCTRL_LUTEI_Pos)                /**< (CCL_LUTCTRL) Event Input Enable Mask */
#define CCL_LUTCTRL_LUTEI(value)              (CCL_LUTCTRL_LUTEI_Msk & ((value) << CCL_LUTCTRL_LUTEI_Pos))
#define CCL_LUTCTRL_LUTEO_Pos                 (22U)                                          /**< (CCL_LUTCTRL) Event Output Enable Position */
#define CCL_LUTCTRL_LUTEO_Msk                 (0x1U << CCL_LUTCTRL_LUTEO_Pos)                /**< (CCL_LUTCTRL) Event Output Enable Mask */
#define CCL_LUTCTRL_LUTEO(value)              (CCL_LUTCTRL_LUTEO_Msk & ((value) << CCL_LUTCTRL_LUTEO_Pos))
#define CCL_LUTCTRL_TRUTH_Pos                 (24U)                                          /**< (CCL_LUTCTRL) Truth Value Position */
#define CCL_LUTCTRL_TRUTH_Msk                 (0xFFU << CCL_LUTCTRL_TRUTH_Pos)               /**< (CCL_LUTCTRL) Truth Value Mask */
#define CCL_LUTCTRL_TRUTH(value)              (CCL_LUTCTRL_TRUTH_Msk & ((value) << CCL_LUTCTRL_TRUTH_Pos))
#define CCL_LUTCTRL_Msk                       (0xFF7FFFB2UL)                                 /**< (CCL_LUTCTRL) Register Mask  */

/** \brief CCL register offsets definitions */
#define CCL_CTRL_OFFSET                (0x00)         /**< (CCL_CTRL) Control Offset */
#define CCL_SEQCTRL_OFFSET             (0x04)         /**< (CCL_SEQCTRL) SEQ Control x Offset */
#define CCL_LUTCTRL_OFFSET             (0x08)         /**< (CCL_LUTCTRL) LUT Control x Offset */

/** \brief CCL register API structure */
typedef struct
{
  __IO  uint8_t                        CCL_CTRL;        /**< Offset: 0x00 (R/W  8) Control */
  __I   uint8_t                        Reserved1[0x03];
  __IO  uint8_t                        CCL_SEQCTRL[2];  /**< Offset: 0x04 (R/W  8) SEQ Control x */
  __I   uint8_t                        Reserved2[0x02];
  __IO  uint32_t                       CCL_LUTCTRL[4];  /**< Offset: 0x08 (R/W  32) LUT Control x */
} ccl_registers_t;
/** @}  end of Configurable Custom Logic */

#endif /* SAMC_SAMC21_CCL_MODULE_H */

