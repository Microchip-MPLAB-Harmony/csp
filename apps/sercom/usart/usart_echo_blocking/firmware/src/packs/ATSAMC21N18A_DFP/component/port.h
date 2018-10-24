/**
 * \brief Header file for SAMC/SAMC21 PORT
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
#ifndef SAMC_SAMC21_PORT_MODULE_H
#define SAMC_SAMC21_PORT_MODULE_H

/** \addtogroup SAMC_SAMC21 Port Module
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_PORT                                  */
/* ========================================================================== */

/* -------- PORT_DIR : (PORT Offset: 0x00) (R/W 32) Data Direction -------- */
#define PORT_DIR_Msk                         (0x00000000UL)                                 /**< (PORT_DIR) Register Mask  */

/* -------- PORT_DIRCLR : (PORT Offset: 0x04) (R/W 32) Data Direction Clear -------- */
#define PORT_DIRCLR_Msk                      (0x00000000UL)                                 /**< (PORT_DIRCLR) Register Mask  */

/* -------- PORT_DIRSET : (PORT Offset: 0x08) (R/W 32) Data Direction Set -------- */
#define PORT_DIRSET_Msk                      (0x00000000UL)                                 /**< (PORT_DIRSET) Register Mask  */

/* -------- PORT_DIRTGL : (PORT Offset: 0x0C) (R/W 32) Data Direction Toggle -------- */
#define PORT_DIRTGL_Msk                      (0x00000000UL)                                 /**< (PORT_DIRTGL) Register Mask  */

/* -------- PORT_OUT : (PORT Offset: 0x10) (R/W 32) Data Output Value -------- */
#define PORT_OUT_Msk                         (0x00000000UL)                                 /**< (PORT_OUT) Register Mask  */

/* -------- PORT_OUTCLR : (PORT Offset: 0x14) (R/W 32) Data Output Value Clear -------- */
#define PORT_OUTCLR_Msk                      (0x00000000UL)                                 /**< (PORT_OUTCLR) Register Mask  */

/* -------- PORT_OUTSET : (PORT Offset: 0x18) (R/W 32) Data Output Value Set -------- */
#define PORT_OUTSET_Msk                      (0x00000000UL)                                 /**< (PORT_OUTSET) Register Mask  */

/* -------- PORT_OUTTGL : (PORT Offset: 0x1C) (R/W 32) Data Output Value Toggle -------- */
#define PORT_OUTTGL_Msk                      (0x00000000UL)                                 /**< (PORT_OUTTGL) Register Mask  */

/* -------- PORT_IN : (PORT Offset: 0x20) (R/  32) Data Input Value -------- */
#define PORT_IN_Msk                          (0x00000000UL)                                 /**< (PORT_IN) Register Mask  */

/* -------- PORT_CTRL : (PORT Offset: 0x24) (R/W 32) Control -------- */
#define PORT_CTRL_SAMPLING_Pos               (0U)                                           /**< (PORT_CTRL) Input Sampling Mode Position */
#define PORT_CTRL_SAMPLING_Msk               (0xFFFFFFFFU << PORT_CTRL_SAMPLING_Pos)       /**< (PORT_CTRL) Input Sampling Mode Mask */
#define PORT_CTRL_SAMPLING(value)            (PORT_CTRL_SAMPLING_Msk & ((value) << PORT_CTRL_SAMPLING_Pos))
#define PORT_CTRL_Msk                        (0xFFFFFFFFUL)                                 /**< (PORT_CTRL) Register Mask  */

/* -------- PORT_WRCONFIG : (PORT Offset: 0x28) ( /W 32) Write Configuration -------- */
#define PORT_WRCONFIG_PINMASK_Pos            (0U)                                           /**< (PORT_WRCONFIG) Pin Mask for Multiple Pin Configuration Position */
#define PORT_WRCONFIG_PINMASK_Msk            (0xFFFFU << PORT_WRCONFIG_PINMASK_Pos)        /**< (PORT_WRCONFIG) Pin Mask for Multiple Pin Configuration Mask */
#define PORT_WRCONFIG_PINMASK(value)         (PORT_WRCONFIG_PINMASK_Msk & ((value) << PORT_WRCONFIG_PINMASK_Pos))
#define PORT_WRCONFIG_PMUXEN_Pos             (16U)                                          /**< (PORT_WRCONFIG) Select Peripheral Multiplexer Position */
#define PORT_WRCONFIG_PMUXEN_Msk             (0x1U << PORT_WRCONFIG_PMUXEN_Pos)            /**< (PORT_WRCONFIG) Select Peripheral Multiplexer Mask */
#define PORT_WRCONFIG_PMUXEN(value)          (PORT_WRCONFIG_PMUXEN_Msk & ((value) << PORT_WRCONFIG_PMUXEN_Pos))
#define PORT_WRCONFIG_INEN_Pos               (17U)                                          /**< (PORT_WRCONFIG) Input Enable Position */
#define PORT_WRCONFIG_INEN_Msk               (0x1U << PORT_WRCONFIG_INEN_Pos)              /**< (PORT_WRCONFIG) Input Enable Mask */
#define PORT_WRCONFIG_INEN(value)            (PORT_WRCONFIG_INEN_Msk & ((value) << PORT_WRCONFIG_INEN_Pos))
#define PORT_WRCONFIG_PULLEN_Pos             (18U)                                          /**< (PORT_WRCONFIG) Pull Enable Position */
#define PORT_WRCONFIG_PULLEN_Msk             (0x1U << PORT_WRCONFIG_PULLEN_Pos)            /**< (PORT_WRCONFIG) Pull Enable Mask */
#define PORT_WRCONFIG_PULLEN(value)          (PORT_WRCONFIG_PULLEN_Msk & ((value) << PORT_WRCONFIG_PULLEN_Pos))
#define PORT_WRCONFIG_DRVSTR_Pos             (22U)                                          /**< (PORT_WRCONFIG) Output Driver Strength Selection Position */
#define PORT_WRCONFIG_DRVSTR_Msk             (0x1U << PORT_WRCONFIG_DRVSTR_Pos)            /**< (PORT_WRCONFIG) Output Driver Strength Selection Mask */
#define PORT_WRCONFIG_DRVSTR(value)          (PORT_WRCONFIG_DRVSTR_Msk & ((value) << PORT_WRCONFIG_DRVSTR_Pos))
#define PORT_WRCONFIG_PMUX_Pos               (24U)                                          /**< (PORT_WRCONFIG) Peripheral Multiplexing Template Position */
#define PORT_WRCONFIG_PMUX_Msk               (0xFU << PORT_WRCONFIG_PMUX_Pos)              /**< (PORT_WRCONFIG) Peripheral Multiplexing Template Mask */
#define PORT_WRCONFIG_PMUX(value)            (PORT_WRCONFIG_PMUX_Msk & ((value) << PORT_WRCONFIG_PMUX_Pos))
#define PORT_WRCONFIG_WRPMUX_Pos             (28U)                                          /**< (PORT_WRCONFIG) Write PMUX Registers Position */
#define PORT_WRCONFIG_WRPMUX_Msk             (0x1U << PORT_WRCONFIG_WRPMUX_Pos)            /**< (PORT_WRCONFIG) Write PMUX Registers Mask */
#define PORT_WRCONFIG_WRPMUX(value)          (PORT_WRCONFIG_WRPMUX_Msk & ((value) << PORT_WRCONFIG_WRPMUX_Pos))
#define PORT_WRCONFIG_WRPINCFG_Pos           (30U)                                          /**< (PORT_WRCONFIG) Write PINCFG Registers Position */
#define PORT_WRCONFIG_WRPINCFG_Msk           (0x1U << PORT_WRCONFIG_WRPINCFG_Pos)          /**< (PORT_WRCONFIG) Write PINCFG Registers Mask */
#define PORT_WRCONFIG_WRPINCFG(value)        (PORT_WRCONFIG_WRPINCFG_Msk & ((value) << PORT_WRCONFIG_WRPINCFG_Pos))
#define PORT_WRCONFIG_HWSEL_Pos              (31U)                                          /**< (PORT_WRCONFIG) Half-Word Select Position */
#define PORT_WRCONFIG_HWSEL_Msk              (0x1U << PORT_WRCONFIG_HWSEL_Pos)             /**< (PORT_WRCONFIG) Half-Word Select Mask */
#define PORT_WRCONFIG_HWSEL(value)           (PORT_WRCONFIG_HWSEL_Msk & ((value) << PORT_WRCONFIG_HWSEL_Pos))
#define PORT_WRCONFIG_Msk                    (0xDF47FFFFUL)                                 /**< (PORT_WRCONFIG) Register Mask  */

/* -------- PORT_EVCTRL : (PORT Offset: 0x2C) (R/W 32) Event Input Control -------- */
#define PORT_EVCTRL_PID0_Pos                 (0U)                                           /**< (PORT_EVCTRL) Port Event Pin Identifier 0 Position */
#define PORT_EVCTRL_PID0_Msk                 (0x1FU << PORT_EVCTRL_PID0_Pos)               /**< (PORT_EVCTRL) Port Event Pin Identifier 0 Mask */
#define PORT_EVCTRL_PID0(value)              (PORT_EVCTRL_PID0_Msk & ((value) << PORT_EVCTRL_PID0_Pos))
#define PORT_EVCTRL_EVACT0_Pos               (5U)                                           /**< (PORT_EVCTRL) Port Event Action 0 Position */
#define PORT_EVCTRL_EVACT0_Msk               (0x3U << PORT_EVCTRL_EVACT0_Pos)              /**< (PORT_EVCTRL) Port Event Action 0 Mask */
#define PORT_EVCTRL_EVACT0(value)            (PORT_EVCTRL_EVACT0_Msk & ((value) << PORT_EVCTRL_EVACT0_Pos))
#define   PORT_EVCTRL_EVACT0_OUT_Val         (0U)                                           /**< (PORT_EVCTRL) Event output to pin  */
#define   PORT_EVCTRL_EVACT0_SET_Val         (1U)                                           /**< (PORT_EVCTRL) Set output register of pin on event  */
#define   PORT_EVCTRL_EVACT0_CLR_Val         (2U)                                           /**< (PORT_EVCTRL) Clear output register of pin on event  */
#define   PORT_EVCTRL_EVACT0_TGL_Val         (3U)                                           /**< (PORT_EVCTRL) Toggle output register of pin on event  */
#define PORT_EVCTRL_EVACT0_OUT               (PORT_EVCTRL_EVACT0_OUT_Val << PORT_EVCTRL_EVACT0_Pos) /**< (PORT_EVCTRL) Event output to pin Position  */
#define PORT_EVCTRL_EVACT0_SET               (PORT_EVCTRL_EVACT0_SET_Val << PORT_EVCTRL_EVACT0_Pos) /**< (PORT_EVCTRL) Set output register of pin on event Position  */
#define PORT_EVCTRL_EVACT0_CLR               (PORT_EVCTRL_EVACT0_CLR_Val << PORT_EVCTRL_EVACT0_Pos) /**< (PORT_EVCTRL) Clear output register of pin on event Position  */
#define PORT_EVCTRL_EVACT0_TGL               (PORT_EVCTRL_EVACT0_TGL_Val << PORT_EVCTRL_EVACT0_Pos) /**< (PORT_EVCTRL) Toggle output register of pin on event Position  */
#define PORT_EVCTRL_PORTEI0_Pos              (7U)                                           /**< (PORT_EVCTRL) Port Event Enable Input 0 Position */
#define PORT_EVCTRL_PORTEI0_Msk              (0x1U << PORT_EVCTRL_PORTEI0_Pos)             /**< (PORT_EVCTRL) Port Event Enable Input 0 Mask */
#define PORT_EVCTRL_PORTEI0(value)           (PORT_EVCTRL_PORTEI0_Msk & ((value) << PORT_EVCTRL_PORTEI0_Pos))
#define PORT_EVCTRL_PID1_Pos                 (8U)                                           /**< (PORT_EVCTRL) Port Event Pin Identifier 1 Position */
#define PORT_EVCTRL_PID1_Msk                 (0x1FU << PORT_EVCTRL_PID1_Pos)               /**< (PORT_EVCTRL) Port Event Pin Identifier 1 Mask */
#define PORT_EVCTRL_PID1(value)              (PORT_EVCTRL_PID1_Msk & ((value) << PORT_EVCTRL_PID1_Pos))
#define PORT_EVCTRL_EVACT1_Pos               (13U)                                          /**< (PORT_EVCTRL) Port Event Action 1 Position */
#define PORT_EVCTRL_EVACT1_Msk               (0x3U << PORT_EVCTRL_EVACT1_Pos)              /**< (PORT_EVCTRL) Port Event Action 1 Mask */
#define PORT_EVCTRL_EVACT1(value)            (PORT_EVCTRL_EVACT1_Msk & ((value) << PORT_EVCTRL_EVACT1_Pos))
#define PORT_EVCTRL_PORTEI1_Pos              (15U)                                          /**< (PORT_EVCTRL) Port Event Enable Input 1 Position */
#define PORT_EVCTRL_PORTEI1_Msk              (0x1U << PORT_EVCTRL_PORTEI1_Pos)             /**< (PORT_EVCTRL) Port Event Enable Input 1 Mask */
#define PORT_EVCTRL_PORTEI1(value)           (PORT_EVCTRL_PORTEI1_Msk & ((value) << PORT_EVCTRL_PORTEI1_Pos))
#define PORT_EVCTRL_PID2_Pos                 (16U)                                          /**< (PORT_EVCTRL) Port Event Pin Identifier 2 Position */
#define PORT_EVCTRL_PID2_Msk                 (0x1FU << PORT_EVCTRL_PID2_Pos)               /**< (PORT_EVCTRL) Port Event Pin Identifier 2 Mask */
#define PORT_EVCTRL_PID2(value)              (PORT_EVCTRL_PID2_Msk & ((value) << PORT_EVCTRL_PID2_Pos))
#define PORT_EVCTRL_EVACT2_Pos               (21U)                                          /**< (PORT_EVCTRL) Port Event Action 2 Position */
#define PORT_EVCTRL_EVACT2_Msk               (0x3U << PORT_EVCTRL_EVACT2_Pos)              /**< (PORT_EVCTRL) Port Event Action 2 Mask */
#define PORT_EVCTRL_EVACT2(value)            (PORT_EVCTRL_EVACT2_Msk & ((value) << PORT_EVCTRL_EVACT2_Pos))
#define PORT_EVCTRL_PORTEI2_Pos              (23U)                                          /**< (PORT_EVCTRL) Port Event Enable Input 2 Position */
#define PORT_EVCTRL_PORTEI2_Msk              (0x1U << PORT_EVCTRL_PORTEI2_Pos)             /**< (PORT_EVCTRL) Port Event Enable Input 2 Mask */
#define PORT_EVCTRL_PORTEI2(value)           (PORT_EVCTRL_PORTEI2_Msk & ((value) << PORT_EVCTRL_PORTEI2_Pos))
#define PORT_EVCTRL_PID3_Pos                 (24U)                                          /**< (PORT_EVCTRL) Port Event Pin Identifier 3 Position */
#define PORT_EVCTRL_PID3_Msk                 (0x1FU << PORT_EVCTRL_PID3_Pos)               /**< (PORT_EVCTRL) Port Event Pin Identifier 3 Mask */
#define PORT_EVCTRL_PID3(value)              (PORT_EVCTRL_PID3_Msk & ((value) << PORT_EVCTRL_PID3_Pos))
#define PORT_EVCTRL_EVACT3_Pos               (29U)                                          /**< (PORT_EVCTRL) Port Event Action 3 Position */
#define PORT_EVCTRL_EVACT3_Msk               (0x3U << PORT_EVCTRL_EVACT3_Pos)              /**< (PORT_EVCTRL) Port Event Action 3 Mask */
#define PORT_EVCTRL_EVACT3(value)            (PORT_EVCTRL_EVACT3_Msk & ((value) << PORT_EVCTRL_EVACT3_Pos))
#define PORT_EVCTRL_PORTEI3_Pos              (31U)                                          /**< (PORT_EVCTRL) Port Event Enable Input 3 Position */
#define PORT_EVCTRL_PORTEI3_Msk              (0x1U << PORT_EVCTRL_PORTEI3_Pos)             /**< (PORT_EVCTRL) Port Event Enable Input 3 Mask */
#define PORT_EVCTRL_PORTEI3(value)           (PORT_EVCTRL_PORTEI3_Msk & ((value) << PORT_EVCTRL_PORTEI3_Pos))
#define PORT_EVCTRL_Msk                      (0xFFFFFFFFUL)                                 /**< (PORT_EVCTRL) Register Mask  */

/* -------- PORT_PMUX : (PORT Offset: 0x30) (R/W 8) Peripheral Multiplexing n -------- */
#define PORT_PMUX_PMUXE_Pos                  (0U)                                           /**< (PORT_PMUX) Peripheral Multiplexing for Even-Numbered Pin Position */
#define PORT_PMUX_PMUXE_Msk                  (0xFU << PORT_PMUX_PMUXE_Pos)                 /**< (PORT_PMUX) Peripheral Multiplexing for Even-Numbered Pin Mask */
#define PORT_PMUX_PMUXE(value)               (PORT_PMUX_PMUXE_Msk & ((value) << PORT_PMUX_PMUXE_Pos))
#define PORT_PMUX_PMUXO_Pos                  (4U)                                           /**< (PORT_PMUX) Peripheral Multiplexing for Odd-Numbered Pin Position */
#define PORT_PMUX_PMUXO_Msk                  (0xFU << PORT_PMUX_PMUXO_Pos)                 /**< (PORT_PMUX) Peripheral Multiplexing for Odd-Numbered Pin Mask */
#define PORT_PMUX_PMUXO(value)               (PORT_PMUX_PMUXO_Msk & ((value) << PORT_PMUX_PMUXO_Pos))
#define PORT_PMUX_Msk                        (0x000000FFUL)                                 /**< (PORT_PMUX) Register Mask  */

/* -------- PORT_PINCFG : (PORT Offset: 0x40) (R/W 8) Pin Configuration n -------- */
#define PORT_PINCFG_PMUXEN_Pos               (0U)                                           /**< (PORT_PINCFG) Select Peripheral Multiplexer Position */
#define PORT_PINCFG_PMUXEN_Msk               (0x1U << PORT_PINCFG_PMUXEN_Pos)              /**< (PORT_PINCFG) Select Peripheral Multiplexer Mask */
#define PORT_PINCFG_PMUXEN(value)            (PORT_PINCFG_PMUXEN_Msk & ((value) << PORT_PINCFG_PMUXEN_Pos))
#define PORT_PINCFG_INEN_Pos                 (1U)                                           /**< (PORT_PINCFG) Input Enable Position */
#define PORT_PINCFG_INEN_Msk                 (0x1U << PORT_PINCFG_INEN_Pos)                /**< (PORT_PINCFG) Input Enable Mask */
#define PORT_PINCFG_INEN(value)              (PORT_PINCFG_INEN_Msk & ((value) << PORT_PINCFG_INEN_Pos))
#define PORT_PINCFG_PULLEN_Pos               (2U)                                           /**< (PORT_PINCFG) Pull Enable Position */
#define PORT_PINCFG_PULLEN_Msk               (0x1U << PORT_PINCFG_PULLEN_Pos)              /**< (PORT_PINCFG) Pull Enable Mask */
#define PORT_PINCFG_PULLEN(value)            (PORT_PINCFG_PULLEN_Msk & ((value) << PORT_PINCFG_PULLEN_Pos))
#define PORT_PINCFG_DRVSTR_Pos               (6U)                                           /**< (PORT_PINCFG) Output Driver Strength Selection Position */
#define PORT_PINCFG_DRVSTR_Msk               (0x1U << PORT_PINCFG_DRVSTR_Pos)              /**< (PORT_PINCFG) Output Driver Strength Selection Mask */
#define PORT_PINCFG_DRVSTR(value)            (PORT_PINCFG_DRVSTR_Msk & ((value) << PORT_PINCFG_DRVSTR_Pos))
#define PORT_PINCFG_Msk                      (0x00000047UL)                                 /**< (PORT_PINCFG) Register Mask  */

/** \brief PORT register offsets definitions */
#define PORT_OFFSET                   (0x00)         /**< (GROUP)  Offset */
  #define PORT_DIR_OFFSET               (0x00)         /**< (PORT_DIR) Data Direction Offset */
  #define PORT_DIRCLR_OFFSET            (0x04)         /**< (PORT_DIRCLR) Data Direction Clear Offset */
  #define PORT_DIRSET_OFFSET            (0x08)         /**< (PORT_DIRSET) Data Direction Set Offset */
  #define PORT_DIRTGL_OFFSET            (0x0C)         /**< (PORT_DIRTGL) Data Direction Toggle Offset */
  #define PORT_OUT_OFFSET               (0x10)         /**< (PORT_OUT) Data Output Value Offset */
  #define PORT_OUTCLR_OFFSET            (0x14)         /**< (PORT_OUTCLR) Data Output Value Clear Offset */
  #define PORT_OUTSET_OFFSET            (0x18)         /**< (PORT_OUTSET) Data Output Value Set Offset */
  #define PORT_OUTTGL_OFFSET            (0x1C)         /**< (PORT_OUTTGL) Data Output Value Toggle Offset */
  #define PORT_IN_OFFSET                (0x20)         /**< (PORT_IN) Data Input Value Offset */
  #define PORT_CTRL_OFFSET              (0x24)         /**< (PORT_CTRL) Control Offset */
  #define PORT_WRCONFIG_OFFSET          (0x28)         /**< (PORT_WRCONFIG) Write Configuration Offset */
  #define PORT_EVCTRL_OFFSET            (0x2C)         /**< (PORT_EVCTRL) Event Input Control Offset */
  #define PORT_PMUX_OFFSET              (0x30)         /**< (PORT_PMUX) Peripheral Multiplexing n Offset */
  #define PORT_PINCFG_OFFSET            (0x40)         /**< (PORT_PINCFG) Pin Configuration n Offset */

/** \brief GROUP register API structure */
typedef struct
{
  __IO  uint32_t                       PORT_DIR;       /**< Offset: 0x00 (R/W  32) Data Direction */
  __IO  uint32_t                       PORT_DIRCLR;    /**< Offset: 0x04 (R/W  32) Data Direction Clear */
  __IO  uint32_t                       PORT_DIRSET;    /**< Offset: 0x08 (R/W  32) Data Direction Set */
  __IO  uint32_t                       PORT_DIRTGL;    /**< Offset: 0x0c (R/W  32) Data Direction Toggle */
  __IO  uint32_t                       PORT_OUT;       /**< Offset: 0x10 (R/W  32) Data Output Value */
  __IO  uint32_t                       PORT_OUTCLR;    /**< Offset: 0x14 (R/W  32) Data Output Value Clear */
  __IO  uint32_t                       PORT_OUTSET;    /**< Offset: 0x18 (R/W  32) Data Output Value Set */
  __IO  uint32_t                       PORT_OUTTGL;    /**< Offset: 0x1c (R/W  32) Data Output Value Toggle */
  __I   uint32_t                       PORT_IN;        /**< Offset: 0x20 (R/   32) Data Input Value */
  __IO  uint32_t                       PORT_CTRL;      /**< Offset: 0x24 (R/W  32) Control */
  __O   uint32_t                       PORT_WRCONFIG;  /**< Offset: 0x28 ( /W  32) Write Configuration */
  __IO  uint32_t                       PORT_EVCTRL;    /**< Offset: 0x2c (R/W  32) Event Input Control */
  __IO  uint8_t                        PORT_PMUX[16];  /**< Offset: 0x30 (R/W  8) Peripheral Multiplexing n */
  __IO  uint8_t                        PORT_PINCFG[32]; /**< Offset: 0x40 (R/W  8) Pin Configuration n */
  __I   uint8_t                        Reserved1[0x20];
} port_registers_t;

#endif /* SAMC_SAMC21_PORT_MODULE_H */

