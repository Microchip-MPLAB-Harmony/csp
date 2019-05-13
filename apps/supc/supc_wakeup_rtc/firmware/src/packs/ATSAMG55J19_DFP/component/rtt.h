/**
 * \brief Header file for SAMG/SAMG55 RTT
 *
 * Copyright (c) 2017-2019 Microchip Technology Inc.
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

/* file generated from device description version 2019-05-09T03:59:29Z */
#ifndef SAMG_SAMG55_RTT_MODULE_H
#define SAMG_SAMG55_RTT_MODULE_H

/** \addtogroup SAMG_SAMG55 Real-time Timer
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_RTT                                   */
/* ========================================================================== */

/* -------- RTT_MR : (RTT Offset: 0x00) (R/W 32) Mode Register -------- */
#define RTT_MR_RTPRES_Pos                     (0U)                                           /**< (RTT_MR) Real-time Timer Prescaler Value Position */
#define RTT_MR_RTPRES_Msk                     (0xFFFFU << RTT_MR_RTPRES_Pos)                 /**< (RTT_MR) Real-time Timer Prescaler Value Mask */
#define RTT_MR_RTPRES(value)                  (RTT_MR_RTPRES_Msk & ((value) << RTT_MR_RTPRES_Pos))
#define RTT_MR_ALMIEN_Pos                     (16U)                                          /**< (RTT_MR) Alarm Interrupt Enable Position */
#define RTT_MR_ALMIEN_Msk                     (0x1U << RTT_MR_ALMIEN_Pos)                    /**< (RTT_MR) Alarm Interrupt Enable Mask */
#define RTT_MR_ALMIEN(value)                  (RTT_MR_ALMIEN_Msk & ((value) << RTT_MR_ALMIEN_Pos))
#define RTT_MR_RTTINCIEN_Pos                  (17U)                                          /**< (RTT_MR) Real-time Timer Increment Interrupt Enable Position */
#define RTT_MR_RTTINCIEN_Msk                  (0x1U << RTT_MR_RTTINCIEN_Pos)                 /**< (RTT_MR) Real-time Timer Increment Interrupt Enable Mask */
#define RTT_MR_RTTINCIEN(value)               (RTT_MR_RTTINCIEN_Msk & ((value) << RTT_MR_RTTINCIEN_Pos))
#define RTT_MR_RTTRST_Pos                     (18U)                                          /**< (RTT_MR) Real-time Timer Restart Position */
#define RTT_MR_RTTRST_Msk                     (0x1U << RTT_MR_RTTRST_Pos)                    /**< (RTT_MR) Real-time Timer Restart Mask */
#define RTT_MR_RTTRST(value)                  (RTT_MR_RTTRST_Msk & ((value) << RTT_MR_RTTRST_Pos))
#define RTT_MR_RTTDIS_Pos                     (20U)                                          /**< (RTT_MR) Real-time Timer Disable Position */
#define RTT_MR_RTTDIS_Msk                     (0x1U << RTT_MR_RTTDIS_Pos)                    /**< (RTT_MR) Real-time Timer Disable Mask */
#define RTT_MR_RTTDIS(value)                  (RTT_MR_RTTDIS_Msk & ((value) << RTT_MR_RTTDIS_Pos))
#define RTT_MR_INC2AEN_Pos                    (21U)                                          /**< (RTT_MR) RTTINC2 Alarm Enable Position */
#define RTT_MR_INC2AEN_Msk                    (0x1U << RTT_MR_INC2AEN_Pos)                   /**< (RTT_MR) RTTINC2 Alarm Enable Mask */
#define RTT_MR_INC2AEN(value)                 (RTT_MR_INC2AEN_Msk & ((value) << RTT_MR_INC2AEN_Pos))
#define RTT_MR_EVAEN_Pos                      (22U)                                          /**< (RTT_MR) Trigger Event Alarm Enable Position */
#define RTT_MR_EVAEN_Msk                      (0x1U << RTT_MR_EVAEN_Pos)                     /**< (RTT_MR) Trigger Event Alarm Enable Mask */
#define RTT_MR_EVAEN(value)                   (RTT_MR_EVAEN_Msk & ((value) << RTT_MR_EVAEN_Pos))
#define RTT_MR_RTC1HZ_Pos                     (24U)                                          /**< (RTT_MR) Real-Time Clock 1Hz Clock Selection Position */
#define RTT_MR_RTC1HZ_Msk                     (0x1U << RTT_MR_RTC1HZ_Pos)                    /**< (RTT_MR) Real-Time Clock 1Hz Clock Selection Mask */
#define RTT_MR_RTC1HZ(value)                  (RTT_MR_RTC1HZ_Msk & ((value) << RTT_MR_RTC1HZ_Pos))
#define RTT_MR_Msk                            (0x0177FFFFUL)                                 /**< (RTT_MR) Register Mask  */

/* -------- RTT_AR : (RTT Offset: 0x04) (R/W 32) Alarm Register -------- */
#define RTT_AR_ALMV_Pos                       (0U)                                           /**< (RTT_AR) Alarm Value Position */
#define RTT_AR_ALMV_Msk                       (0xFFFFFFFFU << RTT_AR_ALMV_Pos)               /**< (RTT_AR) Alarm Value Mask */
#define RTT_AR_ALMV(value)                    (RTT_AR_ALMV_Msk & ((value) << RTT_AR_ALMV_Pos))
#define RTT_AR_Msk                            (0xFFFFFFFFUL)                                 /**< (RTT_AR) Register Mask  */

/* -------- RTT_VR : (RTT Offset: 0x08) (R/  32) Value Register -------- */
#define RTT_VR_CRTV_Pos                       (0U)                                           /**< (RTT_VR) Current Real-time Value Position */
#define RTT_VR_CRTV_Msk                       (0xFFFFFFFFU << RTT_VR_CRTV_Pos)               /**< (RTT_VR) Current Real-time Value Mask */
#define RTT_VR_CRTV(value)                    (RTT_VR_CRTV_Msk & ((value) << RTT_VR_CRTV_Pos))
#define RTT_VR_Msk                            (0xFFFFFFFFUL)                                 /**< (RTT_VR) Register Mask  */

/* -------- RTT_SR : (RTT Offset: 0x0C) (R/  32) Status Register -------- */
#define RTT_SR_ALMS_Pos                       (0U)                                           /**< (RTT_SR) Real-time Alarm Status (cleared on read) Position */
#define RTT_SR_ALMS_Msk                       (0x1U << RTT_SR_ALMS_Pos)                      /**< (RTT_SR) Real-time Alarm Status (cleared on read) Mask */
#define RTT_SR_ALMS(value)                    (RTT_SR_ALMS_Msk & ((value) << RTT_SR_ALMS_Pos))
#define RTT_SR_RTTINC_Pos                     (1U)                                           /**< (RTT_SR) Prescaler Roll-over Status (cleared on read) Position */
#define RTT_SR_RTTINC_Msk                     (0x1U << RTT_SR_RTTINC_Pos)                    /**< (RTT_SR) Prescaler Roll-over Status (cleared on read) Mask */
#define RTT_SR_RTTINC(value)                  (RTT_SR_RTTINC_Msk & ((value) << RTT_SR_RTTINC_Pos))
#define RTT_SR_RTTINC2_Pos                    (2U)                                           /**< (RTT_SR) Predefined Number of Prescaler Roll-over Status (cleared on read) Position */
#define RTT_SR_RTTINC2_Msk                    (0x1U << RTT_SR_RTTINC2_Pos)                   /**< (RTT_SR) Predefined Number of Prescaler Roll-over Status (cleared on read) Mask */
#define RTT_SR_RTTINC2(value)                 (RTT_SR_RTTINC2_Msk & ((value) << RTT_SR_RTTINC2_Pos))
#define RTT_SR_Msk                            (0x00000007UL)                                 /**< (RTT_SR) Register Mask  */

/* -------- RTT_MODR : (RTT Offset: 0x10) (R/W 32) Modulo Selection Register -------- */
#define RTT_MODR_SELINC2_Pos                  (0U)                                           /**< (RTT_MODR) Selection of the 32-bit Counter Modulo to generate RTTINC2 flag Position */
#define RTT_MODR_SELINC2_Msk                  (0x7U << RTT_MODR_SELINC2_Pos)                 /**< (RTT_MODR) Selection of the 32-bit Counter Modulo to generate RTTINC2 flag Mask */
#define RTT_MODR_SELINC2(value)               (RTT_MODR_SELINC2_Msk & ((value) << RTT_MODR_SELINC2_Pos))
#define   RTT_MODR_SELINC2_NO_RTTINC2_Val     (0U)                                           /**< (RTT_MODR) The RTTINC2 flag never rises  */
#define   RTT_MODR_SELINC2_MOD64_Val          (1U)                                           /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 64 equals 0  */
#define   RTT_MODR_SELINC2_MOD128_Val         (2U)                                           /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 128 equals 0  */
#define   RTT_MODR_SELINC2_MOD256_Val         (3U)                                           /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 256 equals 0  */
#define   RTT_MODR_SELINC2_MOD512_Val         (4U)                                           /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 512 equals 0  */
#define   RTT_MODR_SELINC2_MOD1024_Val        (5U)                                           /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 1024 equals 0.Example: If RTPRES=32 then RTTINC2 flag rises once per second if the slow clock is 32.768 kHz.  */
#define   RTT_MODR_SELINC2_MOD2048_Val        (6U)                                           /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 2048 equals 0  */
#define   RTT_MODR_SELINC2_MOD4096_Val        (7U)                                           /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 4096 equals 0  */
#define RTT_MODR_SELINC2_NO_RTTINC2           (RTT_MODR_SELINC2_NO_RTTINC2_Val << RTT_MODR_SELINC2_Pos) /**< (RTT_MODR) The RTTINC2 flag never rises Position  */
#define RTT_MODR_SELINC2_MOD64                (RTT_MODR_SELINC2_MOD64_Val << RTT_MODR_SELINC2_Pos) /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 64 equals 0 Position  */
#define RTT_MODR_SELINC2_MOD128               (RTT_MODR_SELINC2_MOD128_Val << RTT_MODR_SELINC2_Pos) /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 128 equals 0 Position  */
#define RTT_MODR_SELINC2_MOD256               (RTT_MODR_SELINC2_MOD256_Val << RTT_MODR_SELINC2_Pos) /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 256 equals 0 Position  */
#define RTT_MODR_SELINC2_MOD512               (RTT_MODR_SELINC2_MOD512_Val << RTT_MODR_SELINC2_Pos) /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 512 equals 0 Position  */
#define RTT_MODR_SELINC2_MOD1024              (RTT_MODR_SELINC2_MOD1024_Val << RTT_MODR_SELINC2_Pos) /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 1024 equals 0.Example: If RTPRES=32 then RTTINC2 flag rises once per second if the slow clock is 32.768 kHz. Position  */
#define RTT_MODR_SELINC2_MOD2048              (RTT_MODR_SELINC2_MOD2048_Val << RTT_MODR_SELINC2_Pos) /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 2048 equals 0 Position  */
#define RTT_MODR_SELINC2_MOD4096              (RTT_MODR_SELINC2_MOD4096_Val << RTT_MODR_SELINC2_Pos) /**< (RTT_MODR) The RTTINC2 flag is set when CRTV modulo 4096 equals 0 Position  */
#define RTT_MODR_SELTRGEV_Pos                 (8U)                                           /**< (RTT_MODR) Selection of the 32-bit Counter Modulo to generate the trigger event Position */
#define RTT_MODR_SELTRGEV_Msk                 (0x7U << RTT_MODR_SELTRGEV_Pos)                /**< (RTT_MODR) Selection of the 32-bit Counter Modulo to generate the trigger event Mask */
#define RTT_MODR_SELTRGEV(value)              (RTT_MODR_SELTRGEV_Msk & ((value) << RTT_MODR_SELTRGEV_Pos))
#define   RTT_MODR_SELTRGEV_NO_EVENT_Val      (0U)                                           /**< (RTT_MODR) No event generated  */
#define   RTT_MODR_SELTRGEV_MOD2_Val          (1U)                                           /**< (RTT_MODR) Event occurs when CRTV modulo 2 equals 0  */
#define   RTT_MODR_SELTRGEV_MOD4_Val          (2U)                                           /**< (RTT_MODR) Event occurs when CRTV modulo 4 equals 0  */
#define   RTT_MODR_SELTRGEV_MOD8_Val          (3U)                                           /**< (RTT_MODR) Event occurs when CRTV modulo 8 equals 0  */
#define   RTT_MODR_SELTRGEV_MOD16_Val         (4U)                                           /**< (RTT_MODR) Event occurs when CRTV modulo 16 equals 0  */
#define   RTT_MODR_SELTRGEV_MOD32_Val         (5U)                                           /**< (RTT_MODR) Event occurs when CRTV modulo 32 equals 0  */
#define   RTT_MODR_SELTRGEV_MOD64_Val         (6U)                                           /**< (RTT_MODR) Event occurs when CRTV modulo 64 equals 0  */
#define   RTT_MODR_SELTRGEV_MOD128_Val        (7U)                                           /**< (RTT_MODR) Event occurs when CRTV modulo 128 equals 0  */
#define RTT_MODR_SELTRGEV_NO_EVENT            (RTT_MODR_SELTRGEV_NO_EVENT_Val << RTT_MODR_SELTRGEV_Pos) /**< (RTT_MODR) No event generated Position  */
#define RTT_MODR_SELTRGEV_MOD2                (RTT_MODR_SELTRGEV_MOD2_Val << RTT_MODR_SELTRGEV_Pos) /**< (RTT_MODR) Event occurs when CRTV modulo 2 equals 0 Position  */
#define RTT_MODR_SELTRGEV_MOD4                (RTT_MODR_SELTRGEV_MOD4_Val << RTT_MODR_SELTRGEV_Pos) /**< (RTT_MODR) Event occurs when CRTV modulo 4 equals 0 Position  */
#define RTT_MODR_SELTRGEV_MOD8                (RTT_MODR_SELTRGEV_MOD8_Val << RTT_MODR_SELTRGEV_Pos) /**< (RTT_MODR) Event occurs when CRTV modulo 8 equals 0 Position  */
#define RTT_MODR_SELTRGEV_MOD16               (RTT_MODR_SELTRGEV_MOD16_Val << RTT_MODR_SELTRGEV_Pos) /**< (RTT_MODR) Event occurs when CRTV modulo 16 equals 0 Position  */
#define RTT_MODR_SELTRGEV_MOD32               (RTT_MODR_SELTRGEV_MOD32_Val << RTT_MODR_SELTRGEV_Pos) /**< (RTT_MODR) Event occurs when CRTV modulo 32 equals 0 Position  */
#define RTT_MODR_SELTRGEV_MOD64               (RTT_MODR_SELTRGEV_MOD64_Val << RTT_MODR_SELTRGEV_Pos) /**< (RTT_MODR) Event occurs when CRTV modulo 64 equals 0 Position  */
#define RTT_MODR_SELTRGEV_MOD128              (RTT_MODR_SELTRGEV_MOD128_Val << RTT_MODR_SELTRGEV_Pos) /**< (RTT_MODR) Event occurs when CRTV modulo 128 equals 0 Position  */
#define RTT_MODR_Msk                          (0x00000707UL)                                 /**< (RTT_MODR) Register Mask  */

/** \brief RTT register offsets definitions */
#define RTT_MR_OFFSET                  (0x00)         /**< (RTT_MR) Mode Register Offset */
#define RTT_AR_OFFSET                  (0x04)         /**< (RTT_AR) Alarm Register Offset */
#define RTT_VR_OFFSET                  (0x08)         /**< (RTT_VR) Value Register Offset */
#define RTT_SR_OFFSET                  (0x0C)         /**< (RTT_SR) Status Register Offset */
#define RTT_MODR_OFFSET                (0x10)         /**< (RTT_MODR) Modulo Selection Register Offset */

/** \brief RTT register API structure */
typedef struct
{
  __IO  uint32_t                       RTT_MR;          /**< Offset: 0x00 (R/W  32) Mode Register */
  __IO  uint32_t                       RTT_AR;          /**< Offset: 0x04 (R/W  32) Alarm Register */
  __I   uint32_t                       RTT_VR;          /**< Offset: 0x08 (R/   32) Value Register */
  __I   uint32_t                       RTT_SR;          /**< Offset: 0x0c (R/   32) Status Register */
  __IO  uint32_t                       RTT_MODR;        /**< Offset: 0x10 (R/W  32) Modulo Selection Register */
} rtt_registers_t;
/** @}  end of Real-time Timer */

#endif /* SAMG_SAMG55_RTT_MODULE_H */

