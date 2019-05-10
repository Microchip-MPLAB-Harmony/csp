/**
 * \brief Header file for SAMG/SAMG55 TC
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
#ifndef SAMG_SAMG55_TC_MODULE_H
#define SAMG_SAMG55_TC_MODULE_H

/** \addtogroup SAMG_SAMG55 Timer Counter
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMG55_TC                                    */
/* ========================================================================== */

/* -------- TC_CCR : (TC Offset: 0x00) ( /W 32) Channel Control Register -------- */
#define TC_CCR_CLKEN_Pos                      (0U)                                           /**< (TC_CCR) Counter Clock Enable Command Position */
#define TC_CCR_CLKEN_Msk                      (0x1U << TC_CCR_CLKEN_Pos)                     /**< (TC_CCR) Counter Clock Enable Command Mask */
#define TC_CCR_CLKEN(value)                   (TC_CCR_CLKEN_Msk & ((value) << TC_CCR_CLKEN_Pos))
#define TC_CCR_CLKDIS_Pos                     (1U)                                           /**< (TC_CCR) Counter Clock Disable Command Position */
#define TC_CCR_CLKDIS_Msk                     (0x1U << TC_CCR_CLKDIS_Pos)                    /**< (TC_CCR) Counter Clock Disable Command Mask */
#define TC_CCR_CLKDIS(value)                  (TC_CCR_CLKDIS_Msk & ((value) << TC_CCR_CLKDIS_Pos))
#define TC_CCR_SWTRG_Pos                      (2U)                                           /**< (TC_CCR) Software Trigger Command Position */
#define TC_CCR_SWTRG_Msk                      (0x1U << TC_CCR_SWTRG_Pos)                     /**< (TC_CCR) Software Trigger Command Mask */
#define TC_CCR_SWTRG(value)                   (TC_CCR_SWTRG_Msk & ((value) << TC_CCR_SWTRG_Pos))
#define TC_CCR_Msk                            (0x00000007UL)                                 /**< (TC_CCR) Register Mask  */

/* -------- TC_CMR : (TC Offset: 0x04) (R/W 32) Channel Mode Register -------- */
#define TC_CMR_TCCLKS_Pos                     (0U)                                           /**< (TC_CMR) Clock Selection Position */
#define TC_CMR_TCCLKS_Msk                     (0x7U << TC_CMR_TCCLKS_Pos)                    /**< (TC_CMR) Clock Selection Mask */
#define TC_CMR_TCCLKS(value)                  (TC_CMR_TCCLKS_Msk & ((value) << TC_CMR_TCCLKS_Pos))
#define   TC_CMR_TCCLKS_TIMER_CLOCK1_Val      (0U)                                           /**< (TC_CMR) Clock selected: internal PCK3 clock signal (from PMC)  */
#define   TC_CMR_TCCLKS_TIMER_CLOCK2_Val      (1U)                                           /**< (TC_CMR) Clock selected: internal MCK/8 clock signal (from PMC)  */
#define   TC_CMR_TCCLKS_TIMER_CLOCK3_Val      (2U)                                           /**< (TC_CMR) Clock selected: internal MCK/32 clock signal (from PMC)  */
#define   TC_CMR_TCCLKS_TIMER_CLOCK4_Val      (3U)                                           /**< (TC_CMR) Clock selected: internal MCK/128 clock signal (from PMC)  */
#define   TC_CMR_TCCLKS_TIMER_CLOCK5_Val      (4U)                                           /**< (TC_CMR) Clock selected: internal SLCK clock signal (from PMC)  */
#define   TC_CMR_TCCLKS_XC0_Val               (5U)                                           /**< (TC_CMR) Clock selected: XC0  */
#define   TC_CMR_TCCLKS_XC1_Val               (6U)                                           /**< (TC_CMR) Clock selected: XC1  */
#define   TC_CMR_TCCLKS_XC2_Val               (7U)                                           /**< (TC_CMR) Clock selected: XC2  */
#define TC_CMR_TCCLKS_TIMER_CLOCK1            (TC_CMR_TCCLKS_TIMER_CLOCK1_Val << TC_CMR_TCCLKS_Pos) /**< (TC_CMR) Clock selected: internal PCK3 clock signal (from PMC) Position  */
#define TC_CMR_TCCLKS_TIMER_CLOCK2            (TC_CMR_TCCLKS_TIMER_CLOCK2_Val << TC_CMR_TCCLKS_Pos) /**< (TC_CMR) Clock selected: internal MCK/8 clock signal (from PMC) Position  */
#define TC_CMR_TCCLKS_TIMER_CLOCK3            (TC_CMR_TCCLKS_TIMER_CLOCK3_Val << TC_CMR_TCCLKS_Pos) /**< (TC_CMR) Clock selected: internal MCK/32 clock signal (from PMC) Position  */
#define TC_CMR_TCCLKS_TIMER_CLOCK4            (TC_CMR_TCCLKS_TIMER_CLOCK4_Val << TC_CMR_TCCLKS_Pos) /**< (TC_CMR) Clock selected: internal MCK/128 clock signal (from PMC) Position  */
#define TC_CMR_TCCLKS_TIMER_CLOCK5            (TC_CMR_TCCLKS_TIMER_CLOCK5_Val << TC_CMR_TCCLKS_Pos) /**< (TC_CMR) Clock selected: internal SLCK clock signal (from PMC) Position  */
#define TC_CMR_TCCLKS_XC0                     (TC_CMR_TCCLKS_XC0_Val << TC_CMR_TCCLKS_Pos)   /**< (TC_CMR) Clock selected: XC0 Position  */
#define TC_CMR_TCCLKS_XC1                     (TC_CMR_TCCLKS_XC1_Val << TC_CMR_TCCLKS_Pos)   /**< (TC_CMR) Clock selected: XC1 Position  */
#define TC_CMR_TCCLKS_XC2                     (TC_CMR_TCCLKS_XC2_Val << TC_CMR_TCCLKS_Pos)   /**< (TC_CMR) Clock selected: XC2 Position  */
#define TC_CMR_CLKI_Pos                       (3U)                                           /**< (TC_CMR) Clock Invert Position */
#define TC_CMR_CLKI_Msk                       (0x1U << TC_CMR_CLKI_Pos)                      /**< (TC_CMR) Clock Invert Mask */
#define TC_CMR_CLKI(value)                    (TC_CMR_CLKI_Msk & ((value) << TC_CMR_CLKI_Pos))
#define TC_CMR_BURST_Pos                      (4U)                                           /**< (TC_CMR) Burst Signal Selection Position */
#define TC_CMR_BURST_Msk                      (0x3U << TC_CMR_BURST_Pos)                     /**< (TC_CMR) Burst Signal Selection Mask */
#define TC_CMR_BURST(value)                   (TC_CMR_BURST_Msk & ((value) << TC_CMR_BURST_Pos))
#define   TC_CMR_BURST_NONE_Val               (0U)                                           /**< (TC_CMR) The clock is not gated by an external signal.  */
#define   TC_CMR_BURST_XC0_Val                (1U)                                           /**< (TC_CMR) XC0 is ANDed with the selected clock.  */
#define   TC_CMR_BURST_XC1_Val                (2U)                                           /**< (TC_CMR) XC1 is ANDed with the selected clock.  */
#define   TC_CMR_BURST_XC2_Val                (3U)                                           /**< (TC_CMR) XC2 is ANDed with the selected clock.  */
#define TC_CMR_BURST_NONE                     (TC_CMR_BURST_NONE_Val << TC_CMR_BURST_Pos)    /**< (TC_CMR) The clock is not gated by an external signal. Position  */
#define TC_CMR_BURST_XC0                      (TC_CMR_BURST_XC0_Val << TC_CMR_BURST_Pos)     /**< (TC_CMR) XC0 is ANDed with the selected clock. Position  */
#define TC_CMR_BURST_XC1                      (TC_CMR_BURST_XC1_Val << TC_CMR_BURST_Pos)     /**< (TC_CMR) XC1 is ANDed with the selected clock. Position  */
#define TC_CMR_BURST_XC2                      (TC_CMR_BURST_XC2_Val << TC_CMR_BURST_Pos)     /**< (TC_CMR) XC2 is ANDed with the selected clock. Position  */
#define TC_CMR_LDBSTOP_Pos                    (6U)                                           /**< (TC_CMR) Counter Clock Stopped with RB Loading Position */
#define TC_CMR_LDBSTOP_Msk                    (0x1U << TC_CMR_LDBSTOP_Pos)                   /**< (TC_CMR) Counter Clock Stopped with RB Loading Mask */
#define TC_CMR_LDBSTOP(value)                 (TC_CMR_LDBSTOP_Msk & ((value) << TC_CMR_LDBSTOP_Pos))
#define TC_CMR_CPCSTOP_Pos                    (6U)                                           /**< (TC_CMR) Counter Clock Stopped with RC Compare Position */
#define TC_CMR_CPCSTOP_Msk                    (0x1U << TC_CMR_CPCSTOP_Pos)                   /**< (TC_CMR) Counter Clock Stopped with RC Compare Mask */
#define TC_CMR_CPCSTOP(value)                 (TC_CMR_CPCSTOP_Msk & ((value) << TC_CMR_CPCSTOP_Pos))
#define TC_CMR_LDBDIS_Pos                     (7U)                                           /**< (TC_CMR) Counter Clock Disable with RB Loading Position */
#define TC_CMR_LDBDIS_Msk                     (0x1U << TC_CMR_LDBDIS_Pos)                    /**< (TC_CMR) Counter Clock Disable with RB Loading Mask */
#define TC_CMR_LDBDIS(value)                  (TC_CMR_LDBDIS_Msk & ((value) << TC_CMR_LDBDIS_Pos))
#define TC_CMR_CPCDIS_Pos                     (7U)                                           /**< (TC_CMR) Counter Clock Disable with RC Loading Position */
#define TC_CMR_CPCDIS_Msk                     (0x1U << TC_CMR_CPCDIS_Pos)                    /**< (TC_CMR) Counter Clock Disable with RC Loading Mask */
#define TC_CMR_CPCDIS(value)                  (TC_CMR_CPCDIS_Msk & ((value) << TC_CMR_CPCDIS_Pos))
#define TC_CMR_ETRGEDG_Pos                    (8U)                                           /**< (TC_CMR) External Trigger Edge Selection Position */
#define TC_CMR_ETRGEDG_Msk                    (0x3U << TC_CMR_ETRGEDG_Pos)                   /**< (TC_CMR) External Trigger Edge Selection Mask */
#define TC_CMR_ETRGEDG(value)                 (TC_CMR_ETRGEDG_Msk & ((value) << TC_CMR_ETRGEDG_Pos))
#define   TC_CMR_ETRGEDG_NONE_Val             (0U)                                           /**< (TC_CMR) The clock is not gated by an external signal.  */
#define   TC_CMR_ETRGEDG_RISING_Val           (1U)                                           /**< (TC_CMR) Rising edge  */
#define   TC_CMR_ETRGEDG_FALLING_Val          (2U)                                           /**< (TC_CMR) Falling edge  */
#define   TC_CMR_ETRGEDG_EDGE_Val             (3U)                                           /**< (TC_CMR) Each edge  */
#define TC_CMR_ETRGEDG_NONE                   (TC_CMR_ETRGEDG_NONE_Val << TC_CMR_ETRGEDG_Pos) /**< (TC_CMR) The clock is not gated by an external signal. Position  */
#define TC_CMR_ETRGEDG_RISING                 (TC_CMR_ETRGEDG_RISING_Val << TC_CMR_ETRGEDG_Pos) /**< (TC_CMR) Rising edge Position  */
#define TC_CMR_ETRGEDG_FALLING                (TC_CMR_ETRGEDG_FALLING_Val << TC_CMR_ETRGEDG_Pos) /**< (TC_CMR) Falling edge Position  */
#define TC_CMR_ETRGEDG_EDGE                   (TC_CMR_ETRGEDG_EDGE_Val << TC_CMR_ETRGEDG_Pos) /**< (TC_CMR) Each edge Position  */
#define TC_CMR_EEVTEDG_Pos                    (8U)                                           /**< (TC_CMR) External Event Edge Selection Position */
#define TC_CMR_EEVTEDG_Msk                    (0x3U << TC_CMR_EEVTEDG_Pos)                   /**< (TC_CMR) External Event Edge Selection Mask */
#define TC_CMR_EEVTEDG(value)                 (TC_CMR_EEVTEDG_Msk & ((value) << TC_CMR_EEVTEDG_Pos))
#define   TC_CMR_EEVTEDG_NONE_Val             (0U)                                           /**< (TC_CMR) None  */
#define   TC_CMR_EEVTEDG_RISING_Val           (1U)                                           /**< (TC_CMR) Rising edge  */
#define   TC_CMR_EEVTEDG_FALLING_Val          (2U)                                           /**< (TC_CMR) Falling edge  */
#define   TC_CMR_EEVTEDG_EDGE_Val             (3U)                                           /**< (TC_CMR) Each edges  */
#define TC_CMR_EEVTEDG_NONE                   (TC_CMR_EEVTEDG_NONE_Val << TC_CMR_EEVTEDG_Pos) /**< (TC_CMR) None Position  */
#define TC_CMR_EEVTEDG_RISING                 (TC_CMR_EEVTEDG_RISING_Val << TC_CMR_EEVTEDG_Pos) /**< (TC_CMR) Rising edge Position  */
#define TC_CMR_EEVTEDG_FALLING                (TC_CMR_EEVTEDG_FALLING_Val << TC_CMR_EEVTEDG_Pos) /**< (TC_CMR) Falling edge Position  */
#define TC_CMR_EEVTEDG_EDGE                   (TC_CMR_EEVTEDG_EDGE_Val << TC_CMR_EEVTEDG_Pos) /**< (TC_CMR) Each edges Position  */
#define TC_CMR_ABETRG_Pos                     (10U)                                          /**< (TC_CMR) TIOAx or TIOBx External Trigger Selection Position */
#define TC_CMR_ABETRG_Msk                     (0x1U << TC_CMR_ABETRG_Pos)                    /**< (TC_CMR) TIOAx or TIOBx External Trigger Selection Mask */
#define TC_CMR_ABETRG(value)                  (TC_CMR_ABETRG_Msk & ((value) << TC_CMR_ABETRG_Pos))
#define TC_CMR_EEVT_Pos                       (10U)                                          /**< (TC_CMR) External Event Selection Position */
#define TC_CMR_EEVT_Msk                       (0x3U << TC_CMR_EEVT_Pos)                      /**< (TC_CMR) External Event Selection Mask */
#define TC_CMR_EEVT(value)                    (TC_CMR_EEVT_Msk & ((value) << TC_CMR_EEVT_Pos))
#define   TC_CMR_EEVT_TIOB_Val                (0U)                                           /**< (TC_CMR) TIOB  */
#define   TC_CMR_EEVT_XC0_Val                 (1U)                                           /**< (TC_CMR) XC0  */
#define   TC_CMR_EEVT_XC1_Val                 (2U)                                           /**< (TC_CMR) XC1  */
#define   TC_CMR_EEVT_XC2_Val                 (3U)                                           /**< (TC_CMR) XC2  */
#define TC_CMR_EEVT_TIOB                      (TC_CMR_EEVT_TIOB_Val << TC_CMR_EEVT_Pos)      /**< (TC_CMR) TIOB Position  */
#define TC_CMR_EEVT_XC0                       (TC_CMR_EEVT_XC0_Val << TC_CMR_EEVT_Pos)       /**< (TC_CMR) XC0 Position  */
#define TC_CMR_EEVT_XC1                       (TC_CMR_EEVT_XC1_Val << TC_CMR_EEVT_Pos)       /**< (TC_CMR) XC1 Position  */
#define TC_CMR_EEVT_XC2                       (TC_CMR_EEVT_XC2_Val << TC_CMR_EEVT_Pos)       /**< (TC_CMR) XC2 Position  */
#define TC_CMR_ENETRG_Pos                     (12U)                                          /**< (TC_CMR) External Event Trigger Enable Position */
#define TC_CMR_ENETRG_Msk                     (0x1U << TC_CMR_ENETRG_Pos)                    /**< (TC_CMR) External Event Trigger Enable Mask */
#define TC_CMR_ENETRG(value)                  (TC_CMR_ENETRG_Msk & ((value) << TC_CMR_ENETRG_Pos))
#define TC_CMR_WAVSEL_Pos                     (13U)                                          /**< (TC_CMR) Waveform Selection Position */
#define TC_CMR_WAVSEL_Msk                     (0x3U << TC_CMR_WAVSEL_Pos)                    /**< (TC_CMR) Waveform Selection Mask */
#define TC_CMR_WAVSEL(value)                  (TC_CMR_WAVSEL_Msk & ((value) << TC_CMR_WAVSEL_Pos))
#define   TC_CMR_WAVSEL_UP_Val                (0U)                                           /**< (TC_CMR) UP mode without automatic trigger on RC Compare  */
#define   TC_CMR_WAVSEL_UPDOWN_Val            (1U)                                           /**< (TC_CMR) UPDOWN mode without automatic trigger on RC Compare  */
#define   TC_CMR_WAVSEL_UP_RC_Val             (2U)                                           /**< (TC_CMR) UP mode with automatic trigger on RC Compare  */
#define   TC_CMR_WAVSEL_UPDOWN_RC_Val         (3U)                                           /**< (TC_CMR) UPDOWN mode with automatic trigger on RC Compare  */
#define TC_CMR_WAVSEL_UP                      (TC_CMR_WAVSEL_UP_Val << TC_CMR_WAVSEL_Pos)    /**< (TC_CMR) UP mode without automatic trigger on RC Compare Position  */
#define TC_CMR_WAVSEL_UPDOWN                  (TC_CMR_WAVSEL_UPDOWN_Val << TC_CMR_WAVSEL_Pos) /**< (TC_CMR) UPDOWN mode without automatic trigger on RC Compare Position  */
#define TC_CMR_WAVSEL_UP_RC                   (TC_CMR_WAVSEL_UP_RC_Val << TC_CMR_WAVSEL_Pos) /**< (TC_CMR) UP mode with automatic trigger on RC Compare Position  */
#define TC_CMR_WAVSEL_UPDOWN_RC               (TC_CMR_WAVSEL_UPDOWN_RC_Val << TC_CMR_WAVSEL_Pos) /**< (TC_CMR) UPDOWN mode with automatic trigger on RC Compare Position  */
#define TC_CMR_CPCTRG_Pos                     (14U)                                          /**< (TC_CMR) RC Compare Trigger Enable Position */
#define TC_CMR_CPCTRG_Msk                     (0x1U << TC_CMR_CPCTRG_Pos)                    /**< (TC_CMR) RC Compare Trigger Enable Mask */
#define TC_CMR_CPCTRG(value)                  (TC_CMR_CPCTRG_Msk & ((value) << TC_CMR_CPCTRG_Pos))
#define TC_CMR_WAVE_Pos                       (15U)                                          /**< (TC_CMR) Waveform Mode Position */
#define TC_CMR_WAVE_Msk                       (0x1U << TC_CMR_WAVE_Pos)                      /**< (TC_CMR) Waveform Mode Mask */
#define TC_CMR_WAVE(value)                    (TC_CMR_WAVE_Msk & ((value) << TC_CMR_WAVE_Pos))
#define TC_CMR_LDRA_Pos                       (16U)                                          /**< (TC_CMR) RA Loading Edge Selection Position */
#define TC_CMR_LDRA_Msk                       (0x3U << TC_CMR_LDRA_Pos)                      /**< (TC_CMR) RA Loading Edge Selection Mask */
#define TC_CMR_LDRA(value)                    (TC_CMR_LDRA_Msk & ((value) << TC_CMR_LDRA_Pos))
#define   TC_CMR_LDRA_NONE_Val                (0U)                                           /**< (TC_CMR) None  */
#define   TC_CMR_LDRA_RISING_Val              (1U)                                           /**< (TC_CMR) Rising edge of TIOAx  */
#define   TC_CMR_LDRA_FALLING_Val             (2U)                                           /**< (TC_CMR) Falling edge of TIOAx  */
#define   TC_CMR_LDRA_EDGE_Val                (3U)                                           /**< (TC_CMR) Each edge of TIOAx  */
#define TC_CMR_LDRA_NONE                      (TC_CMR_LDRA_NONE_Val << TC_CMR_LDRA_Pos)      /**< (TC_CMR) None Position  */
#define TC_CMR_LDRA_RISING                    (TC_CMR_LDRA_RISING_Val << TC_CMR_LDRA_Pos)    /**< (TC_CMR) Rising edge of TIOAx Position  */
#define TC_CMR_LDRA_FALLING                   (TC_CMR_LDRA_FALLING_Val << TC_CMR_LDRA_Pos)   /**< (TC_CMR) Falling edge of TIOAx Position  */
#define TC_CMR_LDRA_EDGE                      (TC_CMR_LDRA_EDGE_Val << TC_CMR_LDRA_Pos)      /**< (TC_CMR) Each edge of TIOAx Position  */
#define TC_CMR_ACPA_Pos                       (16U)                                          /**< (TC_CMR) RA Compare Effect on TIOAx Position */
#define TC_CMR_ACPA_Msk                       (0x3U << TC_CMR_ACPA_Pos)                      /**< (TC_CMR) RA Compare Effect on TIOAx Mask */
#define TC_CMR_ACPA(value)                    (TC_CMR_ACPA_Msk & ((value) << TC_CMR_ACPA_Pos))
#define   TC_CMR_ACPA_NONE_Val                (0U)                                           /**< (TC_CMR) NONE  */
#define   TC_CMR_ACPA_SET_Val                 (1U)                                           /**< (TC_CMR) SET  */
#define   TC_CMR_ACPA_CLEAR_Val               (2U)                                           /**< (TC_CMR) CLEAR  */
#define   TC_CMR_ACPA_TOGGLE_Val              (3U)                                           /**< (TC_CMR) TOGGLE  */
#define TC_CMR_ACPA_NONE                      (TC_CMR_ACPA_NONE_Val << TC_CMR_ACPA_Pos)      /**< (TC_CMR) NONE Position  */
#define TC_CMR_ACPA_SET                       (TC_CMR_ACPA_SET_Val << TC_CMR_ACPA_Pos)       /**< (TC_CMR) SET Position  */
#define TC_CMR_ACPA_CLEAR                     (TC_CMR_ACPA_CLEAR_Val << TC_CMR_ACPA_Pos)     /**< (TC_CMR) CLEAR Position  */
#define TC_CMR_ACPA_TOGGLE                    (TC_CMR_ACPA_TOGGLE_Val << TC_CMR_ACPA_Pos)    /**< (TC_CMR) TOGGLE Position  */
#define TC_CMR_LDRB_Pos                       (18U)                                          /**< (TC_CMR) RB Loading Edge Selection Position */
#define TC_CMR_LDRB_Msk                       (0x3U << TC_CMR_LDRB_Pos)                      /**< (TC_CMR) RB Loading Edge Selection Mask */
#define TC_CMR_LDRB(value)                    (TC_CMR_LDRB_Msk & ((value) << TC_CMR_LDRB_Pos))
#define   TC_CMR_LDRB_NONE_Val                (0U)                                           /**< (TC_CMR) None  */
#define   TC_CMR_LDRB_RISING_Val              (1U)                                           /**< (TC_CMR) Rising edge of TIOAx  */
#define   TC_CMR_LDRB_FALLING_Val             (2U)                                           /**< (TC_CMR) Falling edge of TIOAx  */
#define   TC_CMR_LDRB_EDGE_Val                (3U)                                           /**< (TC_CMR) Each edge of TIOAx  */
#define TC_CMR_LDRB_NONE                      (TC_CMR_LDRB_NONE_Val << TC_CMR_LDRB_Pos)      /**< (TC_CMR) None Position  */
#define TC_CMR_LDRB_RISING                    (TC_CMR_LDRB_RISING_Val << TC_CMR_LDRB_Pos)    /**< (TC_CMR) Rising edge of TIOAx Position  */
#define TC_CMR_LDRB_FALLING                   (TC_CMR_LDRB_FALLING_Val << TC_CMR_LDRB_Pos)   /**< (TC_CMR) Falling edge of TIOAx Position  */
#define TC_CMR_LDRB_EDGE                      (TC_CMR_LDRB_EDGE_Val << TC_CMR_LDRB_Pos)      /**< (TC_CMR) Each edge of TIOAx Position  */
#define TC_CMR_ACPC_Pos                       (18U)                                          /**< (TC_CMR) RC Compare Effect on TIOAx Position */
#define TC_CMR_ACPC_Msk                       (0x3U << TC_CMR_ACPC_Pos)                      /**< (TC_CMR) RC Compare Effect on TIOAx Mask */
#define TC_CMR_ACPC(value)                    (TC_CMR_ACPC_Msk & ((value) << TC_CMR_ACPC_Pos))
#define   TC_CMR_ACPC_NONE_Val                (0U)                                           /**< (TC_CMR) NONE  */
#define   TC_CMR_ACPC_SET_Val                 (1U)                                           /**< (TC_CMR) SET  */
#define   TC_CMR_ACPC_CLEAR_Val               (2U)                                           /**< (TC_CMR) CLEAR  */
#define   TC_CMR_ACPC_TOGGLE_Val              (3U)                                           /**< (TC_CMR) TOGGLE  */
#define TC_CMR_ACPC_NONE                      (TC_CMR_ACPC_NONE_Val << TC_CMR_ACPC_Pos)      /**< (TC_CMR) NONE Position  */
#define TC_CMR_ACPC_SET                       (TC_CMR_ACPC_SET_Val << TC_CMR_ACPC_Pos)       /**< (TC_CMR) SET Position  */
#define TC_CMR_ACPC_CLEAR                     (TC_CMR_ACPC_CLEAR_Val << TC_CMR_ACPC_Pos)     /**< (TC_CMR) CLEAR Position  */
#define TC_CMR_ACPC_TOGGLE                    (TC_CMR_ACPC_TOGGLE_Val << TC_CMR_ACPC_Pos)    /**< (TC_CMR) TOGGLE Position  */
#define TC_CMR_SBSMPLR_Pos                    (20U)                                          /**< (TC_CMR) Loading Edge Subsampling Ratio Position */
#define TC_CMR_SBSMPLR_Msk                    (0x7U << TC_CMR_SBSMPLR_Pos)                   /**< (TC_CMR) Loading Edge Subsampling Ratio Mask */
#define TC_CMR_SBSMPLR(value)                 (TC_CMR_SBSMPLR_Msk & ((value) << TC_CMR_SBSMPLR_Pos))
#define   TC_CMR_SBSMPLR_ONE_Val              (0U)                                           /**< (TC_CMR) Load a Capture Register each selected edge  */
#define   TC_CMR_SBSMPLR_HALF_Val             (1U)                                           /**< (TC_CMR) Load a Capture Register every 2 selected edges  */
#define   TC_CMR_SBSMPLR_FOURTH_Val           (2U)                                           /**< (TC_CMR) Load a Capture Register every 4 selected edges  */
#define   TC_CMR_SBSMPLR_EIGHTH_Val           (3U)                                           /**< (TC_CMR) Load a Capture Register every 8 selected edges  */
#define   TC_CMR_SBSMPLR_SIXTEENTH_Val        (4U)                                           /**< (TC_CMR) Load a Capture Register every 16 selected edges  */
#define TC_CMR_SBSMPLR_ONE                    (TC_CMR_SBSMPLR_ONE_Val << TC_CMR_SBSMPLR_Pos) /**< (TC_CMR) Load a Capture Register each selected edge Position  */
#define TC_CMR_SBSMPLR_HALF                   (TC_CMR_SBSMPLR_HALF_Val << TC_CMR_SBSMPLR_Pos) /**< (TC_CMR) Load a Capture Register every 2 selected edges Position  */
#define TC_CMR_SBSMPLR_FOURTH                 (TC_CMR_SBSMPLR_FOURTH_Val << TC_CMR_SBSMPLR_Pos) /**< (TC_CMR) Load a Capture Register every 4 selected edges Position  */
#define TC_CMR_SBSMPLR_EIGHTH                 (TC_CMR_SBSMPLR_EIGHTH_Val << TC_CMR_SBSMPLR_Pos) /**< (TC_CMR) Load a Capture Register every 8 selected edges Position  */
#define TC_CMR_SBSMPLR_SIXTEENTH              (TC_CMR_SBSMPLR_SIXTEENTH_Val << TC_CMR_SBSMPLR_Pos) /**< (TC_CMR) Load a Capture Register every 16 selected edges Position  */
#define TC_CMR_AEEVT_Pos                      (20U)                                          /**< (TC_CMR) External Event Effect on TIOAx Position */
#define TC_CMR_AEEVT_Msk                      (0x3U << TC_CMR_AEEVT_Pos)                     /**< (TC_CMR) External Event Effect on TIOAx Mask */
#define TC_CMR_AEEVT(value)                   (TC_CMR_AEEVT_Msk & ((value) << TC_CMR_AEEVT_Pos))
#define   TC_CMR_AEEVT_NONE_Val               (0U)                                           /**< (TC_CMR) NONE  */
#define   TC_CMR_AEEVT_SET_Val                (1U)                                           /**< (TC_CMR) SET  */
#define   TC_CMR_AEEVT_CLEAR_Val              (2U)                                           /**< (TC_CMR) CLEAR  */
#define   TC_CMR_AEEVT_TOGGLE_Val             (3U)                                           /**< (TC_CMR) TOGGLE  */
#define TC_CMR_AEEVT_NONE                     (TC_CMR_AEEVT_NONE_Val << TC_CMR_AEEVT_Pos)    /**< (TC_CMR) NONE Position  */
#define TC_CMR_AEEVT_SET                      (TC_CMR_AEEVT_SET_Val << TC_CMR_AEEVT_Pos)     /**< (TC_CMR) SET Position  */
#define TC_CMR_AEEVT_CLEAR                    (TC_CMR_AEEVT_CLEAR_Val << TC_CMR_AEEVT_Pos)   /**< (TC_CMR) CLEAR Position  */
#define TC_CMR_AEEVT_TOGGLE                   (TC_CMR_AEEVT_TOGGLE_Val << TC_CMR_AEEVT_Pos)  /**< (TC_CMR) TOGGLE Position  */
#define TC_CMR_ASWTRG_Pos                     (22U)                                          /**< (TC_CMR) Software Trigger Effect on TIOAx Position */
#define TC_CMR_ASWTRG_Msk                     (0x3U << TC_CMR_ASWTRG_Pos)                    /**< (TC_CMR) Software Trigger Effect on TIOAx Mask */
#define TC_CMR_ASWTRG(value)                  (TC_CMR_ASWTRG_Msk & ((value) << TC_CMR_ASWTRG_Pos))
#define   TC_CMR_ASWTRG_NONE_Val              (0U)                                           /**< (TC_CMR) NONE  */
#define   TC_CMR_ASWTRG_SET_Val               (1U)                                           /**< (TC_CMR) SET  */
#define   TC_CMR_ASWTRG_CLEAR_Val             (2U)                                           /**< (TC_CMR) CLEAR  */
#define   TC_CMR_ASWTRG_TOGGLE_Val            (3U)                                           /**< (TC_CMR) TOGGLE  */
#define TC_CMR_ASWTRG_NONE                    (TC_CMR_ASWTRG_NONE_Val << TC_CMR_ASWTRG_Pos)  /**< (TC_CMR) NONE Position  */
#define TC_CMR_ASWTRG_SET                     (TC_CMR_ASWTRG_SET_Val << TC_CMR_ASWTRG_Pos)   /**< (TC_CMR) SET Position  */
#define TC_CMR_ASWTRG_CLEAR                   (TC_CMR_ASWTRG_CLEAR_Val << TC_CMR_ASWTRG_Pos) /**< (TC_CMR) CLEAR Position  */
#define TC_CMR_ASWTRG_TOGGLE                  (TC_CMR_ASWTRG_TOGGLE_Val << TC_CMR_ASWTRG_Pos) /**< (TC_CMR) TOGGLE Position  */
#define TC_CMR_BCPB_Pos                       (24U)                                          /**< (TC_CMR) RB Compare Effect on TIOBx Position */
#define TC_CMR_BCPB_Msk                       (0x3U << TC_CMR_BCPB_Pos)                      /**< (TC_CMR) RB Compare Effect on TIOBx Mask */
#define TC_CMR_BCPB(value)                    (TC_CMR_BCPB_Msk & ((value) << TC_CMR_BCPB_Pos))
#define   TC_CMR_BCPB_NONE_Val                (0U)                                           /**< (TC_CMR) NONE  */
#define   TC_CMR_BCPB_SET_Val                 (1U)                                           /**< (TC_CMR) SET  */
#define   TC_CMR_BCPB_CLEAR_Val               (2U)                                           /**< (TC_CMR) CLEAR  */
#define   TC_CMR_BCPB_TOGGLE_Val              (3U)                                           /**< (TC_CMR) TOGGLE  */
#define TC_CMR_BCPB_NONE                      (TC_CMR_BCPB_NONE_Val << TC_CMR_BCPB_Pos)      /**< (TC_CMR) NONE Position  */
#define TC_CMR_BCPB_SET                       (TC_CMR_BCPB_SET_Val << TC_CMR_BCPB_Pos)       /**< (TC_CMR) SET Position  */
#define TC_CMR_BCPB_CLEAR                     (TC_CMR_BCPB_CLEAR_Val << TC_CMR_BCPB_Pos)     /**< (TC_CMR) CLEAR Position  */
#define TC_CMR_BCPB_TOGGLE                    (TC_CMR_BCPB_TOGGLE_Val << TC_CMR_BCPB_Pos)    /**< (TC_CMR) TOGGLE Position  */
#define TC_CMR_BCPC_Pos                       (26U)                                          /**< (TC_CMR) RC Compare Effect on TIOBx Position */
#define TC_CMR_BCPC_Msk                       (0x3U << TC_CMR_BCPC_Pos)                      /**< (TC_CMR) RC Compare Effect on TIOBx Mask */
#define TC_CMR_BCPC(value)                    (TC_CMR_BCPC_Msk & ((value) << TC_CMR_BCPC_Pos))
#define   TC_CMR_BCPC_NONE_Val                (0U)                                           /**< (TC_CMR) NONE  */
#define   TC_CMR_BCPC_SET_Val                 (1U)                                           /**< (TC_CMR) SET  */
#define   TC_CMR_BCPC_CLEAR_Val               (2U)                                           /**< (TC_CMR) CLEAR  */
#define   TC_CMR_BCPC_TOGGLE_Val              (3U)                                           /**< (TC_CMR) TOGGLE  */
#define TC_CMR_BCPC_NONE                      (TC_CMR_BCPC_NONE_Val << TC_CMR_BCPC_Pos)      /**< (TC_CMR) NONE Position  */
#define TC_CMR_BCPC_SET                       (TC_CMR_BCPC_SET_Val << TC_CMR_BCPC_Pos)       /**< (TC_CMR) SET Position  */
#define TC_CMR_BCPC_CLEAR                     (TC_CMR_BCPC_CLEAR_Val << TC_CMR_BCPC_Pos)     /**< (TC_CMR) CLEAR Position  */
#define TC_CMR_BCPC_TOGGLE                    (TC_CMR_BCPC_TOGGLE_Val << TC_CMR_BCPC_Pos)    /**< (TC_CMR) TOGGLE Position  */
#define TC_CMR_BEEVT_Pos                      (28U)                                          /**< (TC_CMR) External Event Effect on TIOBx Position */
#define TC_CMR_BEEVT_Msk                      (0x3U << TC_CMR_BEEVT_Pos)                     /**< (TC_CMR) External Event Effect on TIOBx Mask */
#define TC_CMR_BEEVT(value)                   (TC_CMR_BEEVT_Msk & ((value) << TC_CMR_BEEVT_Pos))
#define   TC_CMR_BEEVT_NONE_Val               (0U)                                           /**< (TC_CMR) NONE  */
#define   TC_CMR_BEEVT_SET_Val                (1U)                                           /**< (TC_CMR) SET  */
#define   TC_CMR_BEEVT_CLEAR_Val              (2U)                                           /**< (TC_CMR) CLEAR  */
#define   TC_CMR_BEEVT_TOGGLE_Val             (3U)                                           /**< (TC_CMR) TOGGLE  */
#define TC_CMR_BEEVT_NONE                     (TC_CMR_BEEVT_NONE_Val << TC_CMR_BEEVT_Pos)    /**< (TC_CMR) NONE Position  */
#define TC_CMR_BEEVT_SET                      (TC_CMR_BEEVT_SET_Val << TC_CMR_BEEVT_Pos)     /**< (TC_CMR) SET Position  */
#define TC_CMR_BEEVT_CLEAR                    (TC_CMR_BEEVT_CLEAR_Val << TC_CMR_BEEVT_Pos)   /**< (TC_CMR) CLEAR Position  */
#define TC_CMR_BEEVT_TOGGLE                   (TC_CMR_BEEVT_TOGGLE_Val << TC_CMR_BEEVT_Pos)  /**< (TC_CMR) TOGGLE Position  */
#define TC_CMR_BSWTRG_Pos                     (30U)                                          /**< (TC_CMR) Software Trigger Effect on TIOBx Position */
#define TC_CMR_BSWTRG_Msk                     (0x3U << TC_CMR_BSWTRG_Pos)                    /**< (TC_CMR) Software Trigger Effect on TIOBx Mask */
#define TC_CMR_BSWTRG(value)                  (TC_CMR_BSWTRG_Msk & ((value) << TC_CMR_BSWTRG_Pos))
#define   TC_CMR_BSWTRG_NONE_Val              (0U)                                           /**< (TC_CMR) NONE  */
#define   TC_CMR_BSWTRG_SET_Val               (1U)                                           /**< (TC_CMR) SET  */
#define   TC_CMR_BSWTRG_CLEAR_Val             (2U)                                           /**< (TC_CMR) CLEAR  */
#define   TC_CMR_BSWTRG_TOGGLE_Val            (3U)                                           /**< (TC_CMR) TOGGLE  */
#define TC_CMR_BSWTRG_NONE                    (TC_CMR_BSWTRG_NONE_Val << TC_CMR_BSWTRG_Pos)  /**< (TC_CMR) NONE Position  */
#define TC_CMR_BSWTRG_SET                     (TC_CMR_BSWTRG_SET_Val << TC_CMR_BSWTRG_Pos)   /**< (TC_CMR) SET Position  */
#define TC_CMR_BSWTRG_CLEAR                   (TC_CMR_BSWTRG_CLEAR_Val << TC_CMR_BSWTRG_Pos) /**< (TC_CMR) CLEAR Position  */
#define TC_CMR_BSWTRG_TOGGLE                  (TC_CMR_BSWTRG_TOGGLE_Val << TC_CMR_BSWTRG_Pos) /**< (TC_CMR) TOGGLE Position  */
#define TC_CMR_Msk                            (0xFFFFFFFFUL)                                 /**< (TC_CMR) Register Mask  */

/* -------- TC_SMMR : (TC Offset: 0x08) (R/W 32) Stepper Motor Mode Register -------- */
#define TC_SMMR_GCEN_Pos                      (0U)                                           /**< (TC_SMMR) Gray Count Enable Position */
#define TC_SMMR_GCEN_Msk                      (0x1U << TC_SMMR_GCEN_Pos)                     /**< (TC_SMMR) Gray Count Enable Mask */
#define TC_SMMR_GCEN(value)                   (TC_SMMR_GCEN_Msk & ((value) << TC_SMMR_GCEN_Pos))
#define TC_SMMR_DOWN_Pos                      (1U)                                           /**< (TC_SMMR) Down Count Position */
#define TC_SMMR_DOWN_Msk                      (0x1U << TC_SMMR_DOWN_Pos)                     /**< (TC_SMMR) Down Count Mask */
#define TC_SMMR_DOWN(value)                   (TC_SMMR_DOWN_Msk & ((value) << TC_SMMR_DOWN_Pos))
#define TC_SMMR_Msk                           (0x00000003UL)                                 /**< (TC_SMMR) Register Mask  */

/* -------- TC_RAB : (TC Offset: 0x0C) (R/  32) Register AB -------- */
#define TC_RAB_RAB_Pos                        (0U)                                           /**< (TC_RAB) Register A or Register B Position */
#define TC_RAB_RAB_Msk                        (0xFFFFFFFFU << TC_RAB_RAB_Pos)                /**< (TC_RAB) Register A or Register B Mask */
#define TC_RAB_RAB(value)                     (TC_RAB_RAB_Msk & ((value) << TC_RAB_RAB_Pos))
#define TC_RAB_Msk                            (0xFFFFFFFFUL)                                 /**< (TC_RAB) Register Mask  */

/* -------- TC_CV : (TC Offset: 0x10) (R/  32) Counter Value -------- */
#define TC_CV_CV_Pos                          (0U)                                           /**< (TC_CV) Counter Value Position */
#define TC_CV_CV_Msk                          (0xFFFFFFFFU << TC_CV_CV_Pos)                  /**< (TC_CV) Counter Value Mask */
#define TC_CV_CV(value)                       (TC_CV_CV_Msk & ((value) << TC_CV_CV_Pos))    
#define TC_CV_Msk                             (0xFFFFFFFFUL)                                 /**< (TC_CV) Register Mask  */

/* -------- TC_RA : (TC Offset: 0x14) (R/W 32) Register A -------- */
#define TC_RA_RA_Pos                          (0U)                                           /**< (TC_RA) Register A Position */
#define TC_RA_RA_Msk                          (0xFFFFFFFFU << TC_RA_RA_Pos)                  /**< (TC_RA) Register A Mask */
#define TC_RA_RA(value)                       (TC_RA_RA_Msk & ((value) << TC_RA_RA_Pos))    
#define TC_RA_Msk                             (0xFFFFFFFFUL)                                 /**< (TC_RA) Register Mask  */

/* -------- TC_RB : (TC Offset: 0x18) (R/W 32) Register B -------- */
#define TC_RB_RB_Pos                          (0U)                                           /**< (TC_RB) Register B Position */
#define TC_RB_RB_Msk                          (0xFFFFFFFFU << TC_RB_RB_Pos)                  /**< (TC_RB) Register B Mask */
#define TC_RB_RB(value)                       (TC_RB_RB_Msk & ((value) << TC_RB_RB_Pos))    
#define TC_RB_Msk                             (0xFFFFFFFFUL)                                 /**< (TC_RB) Register Mask  */

/* -------- TC_RC : (TC Offset: 0x1C) (R/W 32) Register C -------- */
#define TC_RC_RC_Pos                          (0U)                                           /**< (TC_RC) Register C Position */
#define TC_RC_RC_Msk                          (0xFFFFFFFFU << TC_RC_RC_Pos)                  /**< (TC_RC) Register C Mask */
#define TC_RC_RC(value)                       (TC_RC_RC_Msk & ((value) << TC_RC_RC_Pos))    
#define TC_RC_Msk                             (0xFFFFFFFFUL)                                 /**< (TC_RC) Register Mask  */

/* -------- TC_SR : (TC Offset: 0x20) (R/  32) Status Register -------- */
#define TC_SR_COVFS_Pos                       (0U)                                           /**< (TC_SR) Counter Overflow Status (cleared on read) Position */
#define TC_SR_COVFS_Msk                       (0x1U << TC_SR_COVFS_Pos)                      /**< (TC_SR) Counter Overflow Status (cleared on read) Mask */
#define TC_SR_COVFS(value)                    (TC_SR_COVFS_Msk & ((value) << TC_SR_COVFS_Pos))
#define TC_SR_LOVRS_Pos                       (1U)                                           /**< (TC_SR) Load Overrun Status (cleared on read) Position */
#define TC_SR_LOVRS_Msk                       (0x1U << TC_SR_LOVRS_Pos)                      /**< (TC_SR) Load Overrun Status (cleared on read) Mask */
#define TC_SR_LOVRS(value)                    (TC_SR_LOVRS_Msk & ((value) << TC_SR_LOVRS_Pos))
#define TC_SR_CPAS_Pos                        (2U)                                           /**< (TC_SR) RA Compare Status (cleared on read) Position */
#define TC_SR_CPAS_Msk                        (0x1U << TC_SR_CPAS_Pos)                       /**< (TC_SR) RA Compare Status (cleared on read) Mask */
#define TC_SR_CPAS(value)                     (TC_SR_CPAS_Msk & ((value) << TC_SR_CPAS_Pos))
#define TC_SR_CPBS_Pos                        (3U)                                           /**< (TC_SR) RB Compare Status (cleared on read) Position */
#define TC_SR_CPBS_Msk                        (0x1U << TC_SR_CPBS_Pos)                       /**< (TC_SR) RB Compare Status (cleared on read) Mask */
#define TC_SR_CPBS(value)                     (TC_SR_CPBS_Msk & ((value) << TC_SR_CPBS_Pos))
#define TC_SR_CPCS_Pos                        (4U)                                           /**< (TC_SR) RC Compare Status (cleared on read) Position */
#define TC_SR_CPCS_Msk                        (0x1U << TC_SR_CPCS_Pos)                       /**< (TC_SR) RC Compare Status (cleared on read) Mask */
#define TC_SR_CPCS(value)                     (TC_SR_CPCS_Msk & ((value) << TC_SR_CPCS_Pos))
#define TC_SR_LDRAS_Pos                       (5U)                                           /**< (TC_SR) RA Loading Status (cleared on read) Position */
#define TC_SR_LDRAS_Msk                       (0x1U << TC_SR_LDRAS_Pos)                      /**< (TC_SR) RA Loading Status (cleared on read) Mask */
#define TC_SR_LDRAS(value)                    (TC_SR_LDRAS_Msk & ((value) << TC_SR_LDRAS_Pos))
#define TC_SR_LDRBS_Pos                       (6U)                                           /**< (TC_SR) RB Loading Status (cleared on read) Position */
#define TC_SR_LDRBS_Msk                       (0x1U << TC_SR_LDRBS_Pos)                      /**< (TC_SR) RB Loading Status (cleared on read) Mask */
#define TC_SR_LDRBS(value)                    (TC_SR_LDRBS_Msk & ((value) << TC_SR_LDRBS_Pos))
#define TC_SR_ETRGS_Pos                       (7U)                                           /**< (TC_SR) External Trigger Status (cleared on read) Position */
#define TC_SR_ETRGS_Msk                       (0x1U << TC_SR_ETRGS_Pos)                      /**< (TC_SR) External Trigger Status (cleared on read) Mask */
#define TC_SR_ETRGS(value)                    (TC_SR_ETRGS_Msk & ((value) << TC_SR_ETRGS_Pos))
#define TC_SR_CLKSTA_Pos                      (16U)                                          /**< (TC_SR) Clock Enabling Status Position */
#define TC_SR_CLKSTA_Msk                      (0x1U << TC_SR_CLKSTA_Pos)                     /**< (TC_SR) Clock Enabling Status Mask */
#define TC_SR_CLKSTA(value)                   (TC_SR_CLKSTA_Msk & ((value) << TC_SR_CLKSTA_Pos))
#define TC_SR_MTIOA_Pos                       (17U)                                          /**< (TC_SR) TIOAx Mirror Position */
#define TC_SR_MTIOA_Msk                       (0x1U << TC_SR_MTIOA_Pos)                      /**< (TC_SR) TIOAx Mirror Mask */
#define TC_SR_MTIOA(value)                    (TC_SR_MTIOA_Msk & ((value) << TC_SR_MTIOA_Pos))
#define TC_SR_MTIOB_Pos                       (18U)                                          /**< (TC_SR) TIOBx Mirror Position */
#define TC_SR_MTIOB_Msk                       (0x1U << TC_SR_MTIOB_Pos)                      /**< (TC_SR) TIOBx Mirror Mask */
#define TC_SR_MTIOB(value)                    (TC_SR_MTIOB_Msk & ((value) << TC_SR_MTIOB_Pos))
#define TC_SR_Msk                             (0x000700FFUL)                                 /**< (TC_SR) Register Mask  */

/* -------- TC_IER : (TC Offset: 0x24) ( /W 32) Interrupt Enable Register -------- */
#define TC_IER_COVFS_Pos                      (0U)                                           /**< (TC_IER) Counter Overflow Position */
#define TC_IER_COVFS_Msk                      (0x1U << TC_IER_COVFS_Pos)                     /**< (TC_IER) Counter Overflow Mask */
#define TC_IER_COVFS(value)                   (TC_IER_COVFS_Msk & ((value) << TC_IER_COVFS_Pos))
#define TC_IER_LOVRS_Pos                      (1U)                                           /**< (TC_IER) Load Overrun Position */
#define TC_IER_LOVRS_Msk                      (0x1U << TC_IER_LOVRS_Pos)                     /**< (TC_IER) Load Overrun Mask */
#define TC_IER_LOVRS(value)                   (TC_IER_LOVRS_Msk & ((value) << TC_IER_LOVRS_Pos))
#define TC_IER_CPAS_Pos                       (2U)                                           /**< (TC_IER) RA Compare Position */
#define TC_IER_CPAS_Msk                       (0x1U << TC_IER_CPAS_Pos)                      /**< (TC_IER) RA Compare Mask */
#define TC_IER_CPAS(value)                    (TC_IER_CPAS_Msk & ((value) << TC_IER_CPAS_Pos))
#define TC_IER_CPBS_Pos                       (3U)                                           /**< (TC_IER) RB Compare Position */
#define TC_IER_CPBS_Msk                       (0x1U << TC_IER_CPBS_Pos)                      /**< (TC_IER) RB Compare Mask */
#define TC_IER_CPBS(value)                    (TC_IER_CPBS_Msk & ((value) << TC_IER_CPBS_Pos))
#define TC_IER_CPCS_Pos                       (4U)                                           /**< (TC_IER) RC Compare Position */
#define TC_IER_CPCS_Msk                       (0x1U << TC_IER_CPCS_Pos)                      /**< (TC_IER) RC Compare Mask */
#define TC_IER_CPCS(value)                    (TC_IER_CPCS_Msk & ((value) << TC_IER_CPCS_Pos))
#define TC_IER_LDRAS_Pos                      (5U)                                           /**< (TC_IER) RA Loading Position */
#define TC_IER_LDRAS_Msk                      (0x1U << TC_IER_LDRAS_Pos)                     /**< (TC_IER) RA Loading Mask */
#define TC_IER_LDRAS(value)                   (TC_IER_LDRAS_Msk & ((value) << TC_IER_LDRAS_Pos))
#define TC_IER_LDRBS_Pos                      (6U)                                           /**< (TC_IER) RB Loading Position */
#define TC_IER_LDRBS_Msk                      (0x1U << TC_IER_LDRBS_Pos)                     /**< (TC_IER) RB Loading Mask */
#define TC_IER_LDRBS(value)                   (TC_IER_LDRBS_Msk & ((value) << TC_IER_LDRBS_Pos))
#define TC_IER_ETRGS_Pos                      (7U)                                           /**< (TC_IER) External Trigger Position */
#define TC_IER_ETRGS_Msk                      (0x1U << TC_IER_ETRGS_Pos)                     /**< (TC_IER) External Trigger Mask */
#define TC_IER_ETRGS(value)                   (TC_IER_ETRGS_Msk & ((value) << TC_IER_ETRGS_Pos))
#define TC_IER_ENDRX_Pos                      (8U)                                           /**< (TC_IER) End of Receiver Transfer Position */
#define TC_IER_ENDRX_Msk                      (0x1U << TC_IER_ENDRX_Pos)                     /**< (TC_IER) End of Receiver Transfer Mask */
#define TC_IER_ENDRX(value)                   (TC_IER_ENDRX_Msk & ((value) << TC_IER_ENDRX_Pos))
#define TC_IER_RXBUFF_Pos                     (9U)                                           /**< (TC_IER) Reception Buffer Full Position */
#define TC_IER_RXBUFF_Msk                     (0x1U << TC_IER_RXBUFF_Pos)                    /**< (TC_IER) Reception Buffer Full Mask */
#define TC_IER_RXBUFF(value)                  (TC_IER_RXBUFF_Msk & ((value) << TC_IER_RXBUFF_Pos))
#define TC_IER_Msk                            (0x000003FFUL)                                 /**< (TC_IER) Register Mask  */

/* -------- TC_IDR : (TC Offset: 0x28) ( /W 32) Interrupt Disable Register -------- */
#define TC_IDR_COVFS_Pos                      (0U)                                           /**< (TC_IDR) Counter Overflow Position */
#define TC_IDR_COVFS_Msk                      (0x1U << TC_IDR_COVFS_Pos)                     /**< (TC_IDR) Counter Overflow Mask */
#define TC_IDR_COVFS(value)                   (TC_IDR_COVFS_Msk & ((value) << TC_IDR_COVFS_Pos))
#define TC_IDR_LOVRS_Pos                      (1U)                                           /**< (TC_IDR) Load Overrun Position */
#define TC_IDR_LOVRS_Msk                      (0x1U << TC_IDR_LOVRS_Pos)                     /**< (TC_IDR) Load Overrun Mask */
#define TC_IDR_LOVRS(value)                   (TC_IDR_LOVRS_Msk & ((value) << TC_IDR_LOVRS_Pos))
#define TC_IDR_CPAS_Pos                       (2U)                                           /**< (TC_IDR) RA Compare Position */
#define TC_IDR_CPAS_Msk                       (0x1U << TC_IDR_CPAS_Pos)                      /**< (TC_IDR) RA Compare Mask */
#define TC_IDR_CPAS(value)                    (TC_IDR_CPAS_Msk & ((value) << TC_IDR_CPAS_Pos))
#define TC_IDR_CPBS_Pos                       (3U)                                           /**< (TC_IDR) RB Compare Position */
#define TC_IDR_CPBS_Msk                       (0x1U << TC_IDR_CPBS_Pos)                      /**< (TC_IDR) RB Compare Mask */
#define TC_IDR_CPBS(value)                    (TC_IDR_CPBS_Msk & ((value) << TC_IDR_CPBS_Pos))
#define TC_IDR_CPCS_Pos                       (4U)                                           /**< (TC_IDR) RC Compare Position */
#define TC_IDR_CPCS_Msk                       (0x1U << TC_IDR_CPCS_Pos)                      /**< (TC_IDR) RC Compare Mask */
#define TC_IDR_CPCS(value)                    (TC_IDR_CPCS_Msk & ((value) << TC_IDR_CPCS_Pos))
#define TC_IDR_LDRAS_Pos                      (5U)                                           /**< (TC_IDR) RA Loading Position */
#define TC_IDR_LDRAS_Msk                      (0x1U << TC_IDR_LDRAS_Pos)                     /**< (TC_IDR) RA Loading Mask */
#define TC_IDR_LDRAS(value)                   (TC_IDR_LDRAS_Msk & ((value) << TC_IDR_LDRAS_Pos))
#define TC_IDR_LDRBS_Pos                      (6U)                                           /**< (TC_IDR) RB Loading Position */
#define TC_IDR_LDRBS_Msk                      (0x1U << TC_IDR_LDRBS_Pos)                     /**< (TC_IDR) RB Loading Mask */
#define TC_IDR_LDRBS(value)                   (TC_IDR_LDRBS_Msk & ((value) << TC_IDR_LDRBS_Pos))
#define TC_IDR_ETRGS_Pos                      (7U)                                           /**< (TC_IDR) External Trigger Position */
#define TC_IDR_ETRGS_Msk                      (0x1U << TC_IDR_ETRGS_Pos)                     /**< (TC_IDR) External Trigger Mask */
#define TC_IDR_ETRGS(value)                   (TC_IDR_ETRGS_Msk & ((value) << TC_IDR_ETRGS_Pos))
#define TC_IDR_ENDRX_Pos                      (8U)                                           /**< (TC_IDR) End of Receiver Transfer Position */
#define TC_IDR_ENDRX_Msk                      (0x1U << TC_IDR_ENDRX_Pos)                     /**< (TC_IDR) End of Receiver Transfer Mask */
#define TC_IDR_ENDRX(value)                   (TC_IDR_ENDRX_Msk & ((value) << TC_IDR_ENDRX_Pos))
#define TC_IDR_RXBUFF_Pos                     (9U)                                           /**< (TC_IDR) Reception Buffer Full Position */
#define TC_IDR_RXBUFF_Msk                     (0x1U << TC_IDR_RXBUFF_Pos)                    /**< (TC_IDR) Reception Buffer Full Mask */
#define TC_IDR_RXBUFF(value)                  (TC_IDR_RXBUFF_Msk & ((value) << TC_IDR_RXBUFF_Pos))
#define TC_IDR_Msk                            (0x000003FFUL)                                 /**< (TC_IDR) Register Mask  */

/* -------- TC_IMR : (TC Offset: 0x2C) (R/  32) Interrupt Mask Register -------- */
#define TC_IMR_COVFS_Pos                      (0U)                                           /**< (TC_IMR) Counter Overflow Position */
#define TC_IMR_COVFS_Msk                      (0x1U << TC_IMR_COVFS_Pos)                     /**< (TC_IMR) Counter Overflow Mask */
#define TC_IMR_COVFS(value)                   (TC_IMR_COVFS_Msk & ((value) << TC_IMR_COVFS_Pos))
#define TC_IMR_LOVRS_Pos                      (1U)                                           /**< (TC_IMR) Load Overrun Position */
#define TC_IMR_LOVRS_Msk                      (0x1U << TC_IMR_LOVRS_Pos)                     /**< (TC_IMR) Load Overrun Mask */
#define TC_IMR_LOVRS(value)                   (TC_IMR_LOVRS_Msk & ((value) << TC_IMR_LOVRS_Pos))
#define TC_IMR_CPAS_Pos                       (2U)                                           /**< (TC_IMR) RA Compare Position */
#define TC_IMR_CPAS_Msk                       (0x1U << TC_IMR_CPAS_Pos)                      /**< (TC_IMR) RA Compare Mask */
#define TC_IMR_CPAS(value)                    (TC_IMR_CPAS_Msk & ((value) << TC_IMR_CPAS_Pos))
#define TC_IMR_CPBS_Pos                       (3U)                                           /**< (TC_IMR) RB Compare Position */
#define TC_IMR_CPBS_Msk                       (0x1U << TC_IMR_CPBS_Pos)                      /**< (TC_IMR) RB Compare Mask */
#define TC_IMR_CPBS(value)                    (TC_IMR_CPBS_Msk & ((value) << TC_IMR_CPBS_Pos))
#define TC_IMR_CPCS_Pos                       (4U)                                           /**< (TC_IMR) RC Compare Position */
#define TC_IMR_CPCS_Msk                       (0x1U << TC_IMR_CPCS_Pos)                      /**< (TC_IMR) RC Compare Mask */
#define TC_IMR_CPCS(value)                    (TC_IMR_CPCS_Msk & ((value) << TC_IMR_CPCS_Pos))
#define TC_IMR_LDRAS_Pos                      (5U)                                           /**< (TC_IMR) RA Loading Position */
#define TC_IMR_LDRAS_Msk                      (0x1U << TC_IMR_LDRAS_Pos)                     /**< (TC_IMR) RA Loading Mask */
#define TC_IMR_LDRAS(value)                   (TC_IMR_LDRAS_Msk & ((value) << TC_IMR_LDRAS_Pos))
#define TC_IMR_LDRBS_Pos                      (6U)                                           /**< (TC_IMR) RB Loading Position */
#define TC_IMR_LDRBS_Msk                      (0x1U << TC_IMR_LDRBS_Pos)                     /**< (TC_IMR) RB Loading Mask */
#define TC_IMR_LDRBS(value)                   (TC_IMR_LDRBS_Msk & ((value) << TC_IMR_LDRBS_Pos))
#define TC_IMR_ETRGS_Pos                      (7U)                                           /**< (TC_IMR) External Trigger Position */
#define TC_IMR_ETRGS_Msk                      (0x1U << TC_IMR_ETRGS_Pos)                     /**< (TC_IMR) External Trigger Mask */
#define TC_IMR_ETRGS(value)                   (TC_IMR_ETRGS_Msk & ((value) << TC_IMR_ETRGS_Pos))
#define TC_IMR_ENDRX_Pos                      (8U)                                           /**< (TC_IMR) End of Receiver Transfer Position */
#define TC_IMR_ENDRX_Msk                      (0x1U << TC_IMR_ENDRX_Pos)                     /**< (TC_IMR) End of Receiver Transfer Mask */
#define TC_IMR_ENDRX(value)                   (TC_IMR_ENDRX_Msk & ((value) << TC_IMR_ENDRX_Pos))
#define TC_IMR_RXBUFF_Pos                     (9U)                                           /**< (TC_IMR) Reception Buffer Full Position */
#define TC_IMR_RXBUFF_Msk                     (0x1U << TC_IMR_RXBUFF_Pos)                    /**< (TC_IMR) Reception Buffer Full Mask */
#define TC_IMR_RXBUFF(value)                  (TC_IMR_RXBUFF_Msk & ((value) << TC_IMR_RXBUFF_Pos))
#define TC_IMR_Msk                            (0x000003FFUL)                                 /**< (TC_IMR) Register Mask  */

/* -------- TC_BCR : (TC Offset: 0xC0) ( /W 32) Block Control Register -------- */
#define TC_BCR_SYNC_Pos                       (0U)                                           /**< (TC_BCR) Synchro Command Position */
#define TC_BCR_SYNC_Msk                       (0x1U << TC_BCR_SYNC_Pos)                      /**< (TC_BCR) Synchro Command Mask */
#define TC_BCR_SYNC(value)                    (TC_BCR_SYNC_Msk & ((value) << TC_BCR_SYNC_Pos))
#define TC_BCR_Msk                            (0x00000001UL)                                 /**< (TC_BCR) Register Mask  */

/* -------- TC_BMR : (TC Offset: 0xC4) (R/W 32) Block Mode Register -------- */
#define TC_BMR_TC0XC0S_Pos                    (0U)                                           /**< (TC_BMR) External Clock Signal 0 Selection Position */
#define TC_BMR_TC0XC0S_Msk                    (0x3U << TC_BMR_TC0XC0S_Pos)                   /**< (TC_BMR) External Clock Signal 0 Selection Mask */
#define TC_BMR_TC0XC0S(value)                 (TC_BMR_TC0XC0S_Msk & ((value) << TC_BMR_TC0XC0S_Pos))
#define   TC_BMR_TC0XC0S_TCLK0_Val            (0U)                                           /**< (TC_BMR) Signal connected to XC0: TCLK0  */
#define   TC_BMR_TC0XC0S_TIOA1_Val            (2U)                                           /**< (TC_BMR) Signal connected to XC0: TIOA1  */
#define   TC_BMR_TC0XC0S_TIOA2_Val            (3U)                                           /**< (TC_BMR) Signal connected to XC0: TIOA2  */
#define TC_BMR_TC0XC0S_TCLK0                  (TC_BMR_TC0XC0S_TCLK0_Val << TC_BMR_TC0XC0S_Pos) /**< (TC_BMR) Signal connected to XC0: TCLK0 Position  */
#define TC_BMR_TC0XC0S_TIOA1                  (TC_BMR_TC0XC0S_TIOA1_Val << TC_BMR_TC0XC0S_Pos) /**< (TC_BMR) Signal connected to XC0: TIOA1 Position  */
#define TC_BMR_TC0XC0S_TIOA2                  (TC_BMR_TC0XC0S_TIOA2_Val << TC_BMR_TC0XC0S_Pos) /**< (TC_BMR) Signal connected to XC0: TIOA2 Position  */
#define TC_BMR_TC1XC1S_Pos                    (2U)                                           /**< (TC_BMR) External Clock Signal 1 Selection Position */
#define TC_BMR_TC1XC1S_Msk                    (0x3U << TC_BMR_TC1XC1S_Pos)                   /**< (TC_BMR) External Clock Signal 1 Selection Mask */
#define TC_BMR_TC1XC1S(value)                 (TC_BMR_TC1XC1S_Msk & ((value) << TC_BMR_TC1XC1S_Pos))
#define   TC_BMR_TC1XC1S_TCLK1_Val            (0U)                                           /**< (TC_BMR) Signal connected to XC1: TCLK1  */
#define   TC_BMR_TC1XC1S_TIOA0_Val            (2U)                                           /**< (TC_BMR) Signal connected to XC1: TIOA0  */
#define   TC_BMR_TC1XC1S_TIOA2_Val            (3U)                                           /**< (TC_BMR) Signal connected to XC1: TIOA2  */
#define TC_BMR_TC1XC1S_TCLK1                  (TC_BMR_TC1XC1S_TCLK1_Val << TC_BMR_TC1XC1S_Pos) /**< (TC_BMR) Signal connected to XC1: TCLK1 Position  */
#define TC_BMR_TC1XC1S_TIOA0                  (TC_BMR_TC1XC1S_TIOA0_Val << TC_BMR_TC1XC1S_Pos) /**< (TC_BMR) Signal connected to XC1: TIOA0 Position  */
#define TC_BMR_TC1XC1S_TIOA2                  (TC_BMR_TC1XC1S_TIOA2_Val << TC_BMR_TC1XC1S_Pos) /**< (TC_BMR) Signal connected to XC1: TIOA2 Position  */
#define TC_BMR_TC2XC2S_Pos                    (4U)                                           /**< (TC_BMR) External Clock Signal 2 Selection Position */
#define TC_BMR_TC2XC2S_Msk                    (0x3U << TC_BMR_TC2XC2S_Pos)                   /**< (TC_BMR) External Clock Signal 2 Selection Mask */
#define TC_BMR_TC2XC2S(value)                 (TC_BMR_TC2XC2S_Msk & ((value) << TC_BMR_TC2XC2S_Pos))
#define   TC_BMR_TC2XC2S_TCLK2_Val            (0U)                                           /**< (TC_BMR) Signal connected to XC2: TCLK2  */
#define   TC_BMR_TC2XC2S_TIOA0_Val            (2U)                                           /**< (TC_BMR) Signal connected to XC2: TIOA0  */
#define   TC_BMR_TC2XC2S_TIOA1_Val            (3U)                                           /**< (TC_BMR) Signal connected to XC2: TIOA1  */
#define TC_BMR_TC2XC2S_TCLK2                  (TC_BMR_TC2XC2S_TCLK2_Val << TC_BMR_TC2XC2S_Pos) /**< (TC_BMR) Signal connected to XC2: TCLK2 Position  */
#define TC_BMR_TC2XC2S_TIOA0                  (TC_BMR_TC2XC2S_TIOA0_Val << TC_BMR_TC2XC2S_Pos) /**< (TC_BMR) Signal connected to XC2: TIOA0 Position  */
#define TC_BMR_TC2XC2S_TIOA1                  (TC_BMR_TC2XC2S_TIOA1_Val << TC_BMR_TC2XC2S_Pos) /**< (TC_BMR) Signal connected to XC2: TIOA1 Position  */
#define TC_BMR_Msk                            (0x0000003FUL)                                 /**< (TC_BMR) Register Mask  */

/* -------- TC_WPMR : (TC Offset: 0xE4) (R/W 32) Write Protection Mode Register -------- */
#define TC_WPMR_WPEN_Pos                      (0U)                                           /**< (TC_WPMR) Write Protection Enable Position */
#define TC_WPMR_WPEN_Msk                      (0x1U << TC_WPMR_WPEN_Pos)                     /**< (TC_WPMR) Write Protection Enable Mask */
#define TC_WPMR_WPEN(value)                   (TC_WPMR_WPEN_Msk & ((value) << TC_WPMR_WPEN_Pos))
#define TC_WPMR_WPKEY_Pos                     (8U)                                           /**< (TC_WPMR) Write Protection Key Position */
#define TC_WPMR_WPKEY_Msk                     (0xFFFFFFU << TC_WPMR_WPKEY_Pos)               /**< (TC_WPMR) Write Protection Key Mask */
#define TC_WPMR_WPKEY(value)                  (TC_WPMR_WPKEY_Msk & ((value) << TC_WPMR_WPKEY_Pos))
#define   TC_WPMR_WPKEY_PASSWD_Val            (5523789U)                                     /**< (TC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0.  */
#define TC_WPMR_WPKEY_PASSWD                  (TC_WPMR_WPKEY_PASSWD_Val << TC_WPMR_WPKEY_Pos) /**< (TC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0. Position  */
#define TC_WPMR_Msk                           (0xFFFFFF01UL)                                 /**< (TC_WPMR) Register Mask  */

/* -------- TC_RPR0 : (TC Offset: 0x100) (R/W 32) Receive Pointer Register -------- */
#define TC_RPR0_RXPTR_Pos                     (0U)                                           /**< (TC_RPR0) Receive Pointer Register Position */
#define TC_RPR0_RXPTR_Msk                     (0xFFFFFFFFU << TC_RPR0_RXPTR_Pos)             /**< (TC_RPR0) Receive Pointer Register Mask */
#define TC_RPR0_RXPTR(value)                  (TC_RPR0_RXPTR_Msk & ((value) << TC_RPR0_RXPTR_Pos))
#define TC_RPR0_Msk                           (0xFFFFFFFFUL)                                 /**< (TC_RPR0) Register Mask  */

/* -------- TC_RNPR0 : (TC Offset: 0x110) (R/W 32) Receive Next Pointer Register -------- */
#define TC_RNPR0_RXNPTR_Pos                   (0U)                                           /**< (TC_RNPR0) Receive Next Pointer Position */
#define TC_RNPR0_RXNPTR_Msk                   (0xFFFFFFFFU << TC_RNPR0_RXNPTR_Pos)           /**< (TC_RNPR0) Receive Next Pointer Mask */
#define TC_RNPR0_RXNPTR(value)                (TC_RNPR0_RXNPTR_Msk & ((value) << TC_RNPR0_RXNPTR_Pos))
#define TC_RNPR0_Msk                          (0xFFFFFFFFUL)                                 /**< (TC_RNPR0) Register Mask  */

/* -------- TC_RNCR0 : (TC Offset: 0x114) (R/W 32) Receive Next Counter Register -------- */
#define TC_RNCR0_RXNCTR_Pos                   (0U)                                           /**< (TC_RNCR0) Receive Next Counter Position */
#define TC_RNCR0_RXNCTR_Msk                   (0xFFFFU << TC_RNCR0_RXNCTR_Pos)               /**< (TC_RNCR0) Receive Next Counter Mask */
#define TC_RNCR0_RXNCTR(value)                (TC_RNCR0_RXNCTR_Msk & ((value) << TC_RNCR0_RXNCTR_Pos))
#define TC_RNCR0_Msk                          (0x0000FFFFUL)                                 /**< (TC_RNCR0) Register Mask  */

/* -------- TC_PTCR0 : (TC Offset: 0x120) ( /W 32) Transfer Control Register -------- */
#define TC_PTCR0_RXTEN_Pos                    (0U)                                           /**< (TC_PTCR0) Receiver Transfer Enable Position */
#define TC_PTCR0_RXTEN_Msk                    (0x1U << TC_PTCR0_RXTEN_Pos)                   /**< (TC_PTCR0) Receiver Transfer Enable Mask */
#define TC_PTCR0_RXTEN(value)                 (TC_PTCR0_RXTEN_Msk & ((value) << TC_PTCR0_RXTEN_Pos))
#define TC_PTCR0_RXTDIS_Pos                   (1U)                                           /**< (TC_PTCR0) Receiver Transfer Disable Position */
#define TC_PTCR0_RXTDIS_Msk                   (0x1U << TC_PTCR0_RXTDIS_Pos)                  /**< (TC_PTCR0) Receiver Transfer Disable Mask */
#define TC_PTCR0_RXTDIS(value)                (TC_PTCR0_RXTDIS_Msk & ((value) << TC_PTCR0_RXTDIS_Pos))
#define TC_PTCR0_TXTEN_Pos                    (8U)                                           /**< (TC_PTCR0) Transmitter Transfer Enable Position */
#define TC_PTCR0_TXTEN_Msk                    (0x1U << TC_PTCR0_TXTEN_Pos)                   /**< (TC_PTCR0) Transmitter Transfer Enable Mask */
#define TC_PTCR0_TXTEN(value)                 (TC_PTCR0_TXTEN_Msk & ((value) << TC_PTCR0_TXTEN_Pos))
#define TC_PTCR0_TXTDIS_Pos                   (9U)                                           /**< (TC_PTCR0) Transmitter Transfer Disable Position */
#define TC_PTCR0_TXTDIS_Msk                   (0x1U << TC_PTCR0_TXTDIS_Pos)                  /**< (TC_PTCR0) Transmitter Transfer Disable Mask */
#define TC_PTCR0_TXTDIS(value)                (TC_PTCR0_TXTDIS_Msk & ((value) << TC_PTCR0_TXTDIS_Pos))
#define TC_PTCR0_RXCBEN_Pos                   (16U)                                          /**< (TC_PTCR0) Receiver Circular Buffer Enable Position */
#define TC_PTCR0_RXCBEN_Msk                   (0x1U << TC_PTCR0_RXCBEN_Pos)                  /**< (TC_PTCR0) Receiver Circular Buffer Enable Mask */
#define TC_PTCR0_RXCBEN(value)                (TC_PTCR0_RXCBEN_Msk & ((value) << TC_PTCR0_RXCBEN_Pos))
#define TC_PTCR0_RXCBDIS_Pos                  (17U)                                          /**< (TC_PTCR0) Receiver Circular Buffer Disable Position */
#define TC_PTCR0_RXCBDIS_Msk                  (0x1U << TC_PTCR0_RXCBDIS_Pos)                 /**< (TC_PTCR0) Receiver Circular Buffer Disable Mask */
#define TC_PTCR0_RXCBDIS(value)               (TC_PTCR0_RXCBDIS_Msk & ((value) << TC_PTCR0_RXCBDIS_Pos))
#define TC_PTCR0_TXCBEN_Pos                   (18U)                                          /**< (TC_PTCR0) Transmitter Circular Buffer Enable Position */
#define TC_PTCR0_TXCBEN_Msk                   (0x1U << TC_PTCR0_TXCBEN_Pos)                  /**< (TC_PTCR0) Transmitter Circular Buffer Enable Mask */
#define TC_PTCR0_TXCBEN(value)                (TC_PTCR0_TXCBEN_Msk & ((value) << TC_PTCR0_TXCBEN_Pos))
#define TC_PTCR0_TXCBDIS_Pos                  (19U)                                          /**< (TC_PTCR0) Transmitter Circular Buffer Disable Position */
#define TC_PTCR0_TXCBDIS_Msk                  (0x1U << TC_PTCR0_TXCBDIS_Pos)                 /**< (TC_PTCR0) Transmitter Circular Buffer Disable Mask */
#define TC_PTCR0_TXCBDIS(value)               (TC_PTCR0_TXCBDIS_Msk & ((value) << TC_PTCR0_TXCBDIS_Pos))
#define TC_PTCR0_ERRCLR_Pos                   (24U)                                          /**< (TC_PTCR0) Transfer Bus Error Clear Position */
#define TC_PTCR0_ERRCLR_Msk                   (0x1U << TC_PTCR0_ERRCLR_Pos)                  /**< (TC_PTCR0) Transfer Bus Error Clear Mask */
#define TC_PTCR0_ERRCLR(value)                (TC_PTCR0_ERRCLR_Msk & ((value) << TC_PTCR0_ERRCLR_Pos))
#define TC_PTCR0_Msk                          (0x010F0303UL)                                 /**< (TC_PTCR0) Register Mask  */

/* -------- TC_PTSR0 : (TC Offset: 0x124) (R/  32) Transfer Status Register -------- */
#define TC_PTSR0_RXTEN_Pos                    (0U)                                           /**< (TC_PTSR0) Receiver Transfer Enable Position */
#define TC_PTSR0_RXTEN_Msk                    (0x1U << TC_PTSR0_RXTEN_Pos)                   /**< (TC_PTSR0) Receiver Transfer Enable Mask */
#define TC_PTSR0_RXTEN(value)                 (TC_PTSR0_RXTEN_Msk & ((value) << TC_PTSR0_RXTEN_Pos))
#define TC_PTSR0_TXTEN_Pos                    (8U)                                           /**< (TC_PTSR0) Transmitter Transfer Enable Position */
#define TC_PTSR0_TXTEN_Msk                    (0x1U << TC_PTSR0_TXTEN_Pos)                   /**< (TC_PTSR0) Transmitter Transfer Enable Mask */
#define TC_PTSR0_TXTEN(value)                 (TC_PTSR0_TXTEN_Msk & ((value) << TC_PTSR0_TXTEN_Pos))
#define TC_PTSR0_RXCBEN_Pos                   (16U)                                          /**< (TC_PTSR0) Receiver Circular Buffer Enable Position */
#define TC_PTSR0_RXCBEN_Msk                   (0x1U << TC_PTSR0_RXCBEN_Pos)                  /**< (TC_PTSR0) Receiver Circular Buffer Enable Mask */
#define TC_PTSR0_RXCBEN(value)                (TC_PTSR0_RXCBEN_Msk & ((value) << TC_PTSR0_RXCBEN_Pos))
#define TC_PTSR0_TXCBEN_Pos                   (18U)                                          /**< (TC_PTSR0) Transmitter Circular Buffer Enable Position */
#define TC_PTSR0_TXCBEN_Msk                   (0x1U << TC_PTSR0_TXCBEN_Pos)                  /**< (TC_PTSR0) Transmitter Circular Buffer Enable Mask */
#define TC_PTSR0_TXCBEN(value)                (TC_PTSR0_TXCBEN_Msk & ((value) << TC_PTSR0_TXCBEN_Pos))
#define TC_PTSR0_ERR_Pos                      (24U)                                          /**< (TC_PTSR0) Transfer Bus Error Position */
#define TC_PTSR0_ERR_Msk                      (0x1U << TC_PTSR0_ERR_Pos)                     /**< (TC_PTSR0) Transfer Bus Error Mask */
#define TC_PTSR0_ERR(value)                   (TC_PTSR0_ERR_Msk & ((value) << TC_PTSR0_ERR_Pos))
#define TC_PTSR0_Msk                          (0x01050101UL)                                 /**< (TC_PTSR0) Register Mask  */

/** \brief TC register offsets definitions */
#define TC_CHANNEL_OFFSET              (0x00)         /**< (TC_CHANNEL) Channel Control Register Offset */
  #define TC_CCR_OFFSET                  (0x00)         /**< (TC_CCR) Channel Control Register Offset */
  #define TC_CMR_OFFSET                  (0x04)         /**< (TC_CMR) Channel Mode Register Offset */
  #define TC_SMMR_OFFSET                 (0x08)         /**< (TC_SMMR) Stepper Motor Mode Register Offset */
  #define TC_RAB_OFFSET                  (0x0C)         /**< (TC_RAB) Register AB Offset */
  #define TC_CV_OFFSET                   (0x10)         /**< (TC_CV) Counter Value Offset */
  #define TC_RA_OFFSET                   (0x14)         /**< (TC_RA) Register A Offset */
  #define TC_RB_OFFSET                   (0x18)         /**< (TC_RB) Register B Offset */
  #define TC_RC_OFFSET                   (0x1C)         /**< (TC_RC) Register C Offset */
  #define TC_SR_OFFSET                   (0x20)         /**< (TC_SR) Status Register Offset */
  #define TC_IER_OFFSET                  (0x24)         /**< (TC_IER) Interrupt Enable Register Offset */
  #define TC_IDR_OFFSET                  (0x28)         /**< (TC_IDR) Interrupt Disable Register Offset */
  #define TC_IMR_OFFSET                  (0x2C)         /**< (TC_IMR) Interrupt Mask Register Offset */
#define TC_BCR_OFFSET                  (0xC0)         /**< (TC_BCR) Block Control Register Offset */
#define TC_BMR_OFFSET                  (0xC4)         /**< (TC_BMR) Block Mode Register Offset */
#define TC_WPMR_OFFSET                 (0xE4)         /**< (TC_WPMR) Write Protection Mode Register Offset */
#define TC_RPR0_OFFSET                 (0x100)        /**< (TC_RPR0) Receive Pointer Register Offset */
#define TC_RNPR0_OFFSET                (0x110)        /**< (TC_RNPR0) Receive Next Pointer Register Offset */
#define TC_RNCR0_OFFSET                (0x114)        /**< (TC_RNCR0) Receive Next Counter Register Offset */
#define TC_PTCR0_OFFSET                (0x120)        /**< (TC_PTCR0) Transfer Control Register Offset */
#define TC_PTSR0_OFFSET                (0x124)        /**< (TC_PTSR0) Transfer Status Register Offset */

/** \brief TC_CHANNEL register API structure */
typedef struct
{
  __O   uint32_t                       TC_CCR;          /**< Offset: 0x00 ( /W  32) Channel Control Register */
  __IO  uint32_t                       TC_CMR;          /**< Offset: 0x04 (R/W  32) Channel Mode Register */
  __IO  uint32_t                       TC_SMMR;         /**< Offset: 0x08 (R/W  32) Stepper Motor Mode Register */
  __I   uint32_t                       TC_RAB;          /**< Offset: 0x0c (R/   32) Register AB */
  __I   uint32_t                       TC_CV;           /**< Offset: 0x10 (R/   32) Counter Value */
  __IO  uint32_t                       TC_RA;           /**< Offset: 0x14 (R/W  32) Register A */
  __IO  uint32_t                       TC_RB;           /**< Offset: 0x18 (R/W  32) Register B */
  __IO  uint32_t                       TC_RC;           /**< Offset: 0x1c (R/W  32) Register C */
  __I   uint32_t                       TC_SR;           /**< Offset: 0x20 (R/   32) Status Register */
  __O   uint32_t                       TC_IER;          /**< Offset: 0x24 ( /W  32) Interrupt Enable Register */
  __O   uint32_t                       TC_IDR;          /**< Offset: 0x28 ( /W  32) Interrupt Disable Register */
  __I   uint32_t                       TC_IMR;          /**< Offset: 0x2c (R/   32) Interrupt Mask Register */
  __I   uint8_t                        Reserved1[0x10];
} tc_channel_registers_t;
#define TC_CHANNEL_NUMBER (3U)

/** \brief TC register API structure */
typedef struct
{
        tc_channel_registers_t         TC_CHANNEL[TC_CHANNEL_NUMBER]; /**< Offset: 0x00 Channel Control Register */
  __O   uint32_t                       TC_BCR;          /**< Offset: 0xc0 ( /W  32) Block Control Register */
  __IO  uint32_t                       TC_BMR;          /**< Offset: 0xc4 (R/W  32) Block Mode Register */
  __I   uint8_t                        Reserved1[0x1C];
  __IO  uint32_t                       TC_WPMR;         /**< Offset: 0xe4 (R/W  32) Write Protection Mode Register */
  __I   uint8_t                        Reserved2[0x18];
  __IO  uint32_t                       TC_RPR0;         /**< Offset: 0x100 (R/W  32) Receive Pointer Register */
  __I   uint8_t                        Reserved3[0x0C];
  __IO  uint32_t                       TC_RNPR0;        /**< Offset: 0x110 (R/W  32) Receive Next Pointer Register */
  __IO  uint32_t                       TC_RNCR0;        /**< Offset: 0x114 (R/W  32) Receive Next Counter Register */
  __I   uint8_t                        Reserved4[0x08];
  __O   uint32_t                       TC_PTCR0;        /**< Offset: 0x120 ( /W  32) Transfer Control Register */
  __I   uint32_t                       TC_PTSR0;        /**< Offset: 0x124 (R/   32) Transfer Status Register */
} tc_registers_t;
/** @}  end of Timer Counter */

#endif /* SAMG_SAMG55_TC_MODULE_H */

