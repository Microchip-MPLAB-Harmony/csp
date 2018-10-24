/**
 * \brief Header file for SAMC/SAMC21 DSU
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
#ifndef SAMC_SAMC21_DSU_MODULE_H
#define SAMC_SAMC21_DSU_MODULE_H

/** \addtogroup SAMC_SAMC21 Device Service Unit
 *  @{
 */
/* ========================================================================== */
/**  SOFTWARE API DEFINITION FOR SAMC21_DSU                                   */
/* ========================================================================== */

/* -------- DSU_CTRL : (DSU Offset: 0x00) ( /W 8) Control -------- */
#define DSU_CTRL_SWRST_Pos                    (0U)                                           /**< (DSU_CTRL) Software Reset Position */
#define DSU_CTRL_SWRST_Msk                    (0x1U << DSU_CTRL_SWRST_Pos)                   /**< (DSU_CTRL) Software Reset Mask */
#define DSU_CTRL_SWRST(value)                 (DSU_CTRL_SWRST_Msk & ((value) << DSU_CTRL_SWRST_Pos))
#define DSU_CTRL_CRC_Pos                      (2U)                                           /**< (DSU_CTRL) 32-bit Cyclic Redundancy Code Position */
#define DSU_CTRL_CRC_Msk                      (0x1U << DSU_CTRL_CRC_Pos)                     /**< (DSU_CTRL) 32-bit Cyclic Redundancy Code Mask */
#define DSU_CTRL_CRC(value)                   (DSU_CTRL_CRC_Msk & ((value) << DSU_CTRL_CRC_Pos))
#define DSU_CTRL_MBIST_Pos                    (3U)                                           /**< (DSU_CTRL) Memory built-in self-test Position */
#define DSU_CTRL_MBIST_Msk                    (0x1U << DSU_CTRL_MBIST_Pos)                   /**< (DSU_CTRL) Memory built-in self-test Mask */
#define DSU_CTRL_MBIST(value)                 (DSU_CTRL_MBIST_Msk & ((value) << DSU_CTRL_MBIST_Pos))
#define DSU_CTRL_CE_Pos                       (4U)                                           /**< (DSU_CTRL) Chip-Erase Position */
#define DSU_CTRL_CE_Msk                       (0x1U << DSU_CTRL_CE_Pos)                      /**< (DSU_CTRL) Chip-Erase Mask */
#define DSU_CTRL_CE(value)                    (DSU_CTRL_CE_Msk & ((value) << DSU_CTRL_CE_Pos))
#define DSU_CTRL_ARR_Pos                      (6U)                                           /**< (DSU_CTRL) Auxiliary Row Read Position */
#define DSU_CTRL_ARR_Msk                      (0x1U << DSU_CTRL_ARR_Pos)                     /**< (DSU_CTRL) Auxiliary Row Read Mask */
#define DSU_CTRL_ARR(value)                   (DSU_CTRL_ARR_Msk & ((value) << DSU_CTRL_ARR_Pos))
#define DSU_CTRL_SMSA_Pos                     (7U)                                           /**< (DSU_CTRL) Start Memory Stream Access Position */
#define DSU_CTRL_SMSA_Msk                     (0x1U << DSU_CTRL_SMSA_Pos)                    /**< (DSU_CTRL) Start Memory Stream Access Mask */
#define DSU_CTRL_SMSA(value)                  (DSU_CTRL_SMSA_Msk & ((value) << DSU_CTRL_SMSA_Pos))
#define DSU_CTRL_Msk                          (0x000000DDUL)                                 /**< (DSU_CTRL) Register Mask  */

/* -------- DSU_STATUSA : (DSU Offset: 0x01) (R/W 8) Status A -------- */
#define DSU_STATUSA_DONE_Pos                  (0U)                                           /**< (DSU_STATUSA) Done Position */
#define DSU_STATUSA_DONE_Msk                  (0x1U << DSU_STATUSA_DONE_Pos)                 /**< (DSU_STATUSA) Done Mask */
#define DSU_STATUSA_DONE(value)               (DSU_STATUSA_DONE_Msk & ((value) << DSU_STATUSA_DONE_Pos))
#define DSU_STATUSA_CRSTEXT_Pos               (1U)                                           /**< (DSU_STATUSA) CPU Reset Phase Extension Position */
#define DSU_STATUSA_CRSTEXT_Msk               (0x1U << DSU_STATUSA_CRSTEXT_Pos)              /**< (DSU_STATUSA) CPU Reset Phase Extension Mask */
#define DSU_STATUSA_CRSTEXT(value)            (DSU_STATUSA_CRSTEXT_Msk & ((value) << DSU_STATUSA_CRSTEXT_Pos))
#define DSU_STATUSA_BERR_Pos                  (2U)                                           /**< (DSU_STATUSA) Bus Error Position */
#define DSU_STATUSA_BERR_Msk                  (0x1U << DSU_STATUSA_BERR_Pos)                 /**< (DSU_STATUSA) Bus Error Mask */
#define DSU_STATUSA_BERR(value)               (DSU_STATUSA_BERR_Msk & ((value) << DSU_STATUSA_BERR_Pos))
#define DSU_STATUSA_FAIL_Pos                  (3U)                                           /**< (DSU_STATUSA) Failure Position */
#define DSU_STATUSA_FAIL_Msk                  (0x1U << DSU_STATUSA_FAIL_Pos)                 /**< (DSU_STATUSA) Failure Mask */
#define DSU_STATUSA_FAIL(value)               (DSU_STATUSA_FAIL_Msk & ((value) << DSU_STATUSA_FAIL_Pos))
#define DSU_STATUSA_PERR_Pos                  (4U)                                           /**< (DSU_STATUSA) Protection Error Position */
#define DSU_STATUSA_PERR_Msk                  (0x1U << DSU_STATUSA_PERR_Pos)                 /**< (DSU_STATUSA) Protection Error Mask */
#define DSU_STATUSA_PERR(value)               (DSU_STATUSA_PERR_Msk & ((value) << DSU_STATUSA_PERR_Pos))
#define DSU_STATUSA_Msk                       (0x0000001FUL)                                 /**< (DSU_STATUSA) Register Mask  */

/* -------- DSU_STATUSB : (DSU Offset: 0x02) (R/  8) Status B -------- */
#define DSU_STATUSB_PROT_Pos                  (0U)                                           /**< (DSU_STATUSB) Protected Position */
#define DSU_STATUSB_PROT_Msk                  (0x1U << DSU_STATUSB_PROT_Pos)                 /**< (DSU_STATUSB) Protected Mask */
#define DSU_STATUSB_PROT(value)               (DSU_STATUSB_PROT_Msk & ((value) << DSU_STATUSB_PROT_Pos))
#define DSU_STATUSB_DBGPRES_Pos               (1U)                                           /**< (DSU_STATUSB) Debugger Present Position */
#define DSU_STATUSB_DBGPRES_Msk               (0x1U << DSU_STATUSB_DBGPRES_Pos)              /**< (DSU_STATUSB) Debugger Present Mask */
#define DSU_STATUSB_DBGPRES(value)            (DSU_STATUSB_DBGPRES_Msk & ((value) << DSU_STATUSB_DBGPRES_Pos))
#define DSU_STATUSB_DCCD0_Pos                 (2U)                                           /**< (DSU_STATUSB) Debug Communication Channel 0 Dirty Position */
#define DSU_STATUSB_DCCD0_Msk                 (0x1U << DSU_STATUSB_DCCD0_Pos)                /**< (DSU_STATUSB) Debug Communication Channel 0 Dirty Mask */
#define DSU_STATUSB_DCCD0(value)              (DSU_STATUSB_DCCD0_Msk & ((value) << DSU_STATUSB_DCCD0_Pos))
#define DSU_STATUSB_DCCD1_Pos                 (3U)                                           /**< (DSU_STATUSB) Debug Communication Channel 1 Dirty Position */
#define DSU_STATUSB_DCCD1_Msk                 (0x1U << DSU_STATUSB_DCCD1_Pos)                /**< (DSU_STATUSB) Debug Communication Channel 1 Dirty Mask */
#define DSU_STATUSB_DCCD1(value)              (DSU_STATUSB_DCCD1_Msk & ((value) << DSU_STATUSB_DCCD1_Pos))
#define DSU_STATUSB_HPE_Pos                   (4U)                                           /**< (DSU_STATUSB) Hot-Plugging Enable Position */
#define DSU_STATUSB_HPE_Msk                   (0x1U << DSU_STATUSB_HPE_Pos)                  /**< (DSU_STATUSB) Hot-Plugging Enable Mask */
#define DSU_STATUSB_HPE(value)                (DSU_STATUSB_HPE_Msk & ((value) << DSU_STATUSB_HPE_Pos))
#define DSU_STATUSB_Msk                       (0x0000001FUL)                                 /**< (DSU_STATUSB) Register Mask  */

/* -------- DSU_ADDR : (DSU Offset: 0x04) (R/W 32) Address -------- */
#define DSU_ADDR_AMOD_Pos                     (0U)                                           /**< (DSU_ADDR) Access Mode Position */
#define DSU_ADDR_AMOD_Msk                     (0x3U << DSU_ADDR_AMOD_Pos)                    /**< (DSU_ADDR) Access Mode Mask */
#define DSU_ADDR_AMOD(value)                  (DSU_ADDR_AMOD_Msk & ((value) << DSU_ADDR_AMOD_Pos))
#define DSU_ADDR_ADDR_Pos                     (2U)                                           /**< (DSU_ADDR) Address Position */
#define DSU_ADDR_ADDR_Msk                     (0x3FFFFFFFU << DSU_ADDR_ADDR_Pos)             /**< (DSU_ADDR) Address Mask */
#define DSU_ADDR_ADDR(value)                  (DSU_ADDR_ADDR_Msk & ((value) << DSU_ADDR_ADDR_Pos))
#define DSU_ADDR_Msk                          (0xFFFFFFFFUL)                                 /**< (DSU_ADDR) Register Mask  */

/* -------- DSU_LENGTH : (DSU Offset: 0x08) (R/W 32) Length -------- */
#define DSU_LENGTH_LENGTH_Pos                 (2U)                                           /**< (DSU_LENGTH) Length Position */
#define DSU_LENGTH_LENGTH_Msk                 (0x3FFFFFFFU << DSU_LENGTH_LENGTH_Pos)         /**< (DSU_LENGTH) Length Mask */
#define DSU_LENGTH_LENGTH(value)              (DSU_LENGTH_LENGTH_Msk & ((value) << DSU_LENGTH_LENGTH_Pos))
#define DSU_LENGTH_Msk                        (0xFFFFFFFCUL)                                 /**< (DSU_LENGTH) Register Mask  */

/* -------- DSU_DATA : (DSU Offset: 0x0C) (R/W 32) Data -------- */
#define DSU_DATA_DATA_Pos                     (0U)                                           /**< (DSU_DATA) Data Position */
#define DSU_DATA_DATA_Msk                     (0xFFFFFFFFU << DSU_DATA_DATA_Pos)             /**< (DSU_DATA) Data Mask */
#define DSU_DATA_DATA(value)                  (DSU_DATA_DATA_Msk & ((value) << DSU_DATA_DATA_Pos))
#define DSU_DATA_Msk                          (0xFFFFFFFFUL)                                 /**< (DSU_DATA) Register Mask  */

/* -------- DSU_DCC : (DSU Offset: 0x10) (R/W 32) Debug Communication Channel n -------- */
#define DSU_DCC_DATA_Pos                      (0U)                                           /**< (DSU_DCC) Data Position */
#define DSU_DCC_DATA_Msk                      (0xFFFFFFFFU << DSU_DCC_DATA_Pos)              /**< (DSU_DCC) Data Mask */
#define DSU_DCC_DATA(value)                   (DSU_DCC_DATA_Msk & ((value) << DSU_DCC_DATA_Pos))
#define DSU_DCC_Msk                           (0xFFFFFFFFUL)                                 /**< (DSU_DCC) Register Mask  */

/* -------- DSU_DID : (DSU Offset: 0x18) (R/  32) Device Identification -------- */
#define DSU_DID_DEVSEL_Pos                    (0U)                                           /**< (DSU_DID) Device Select Position */
#define DSU_DID_DEVSEL_Msk                    (0xFFU << DSU_DID_DEVSEL_Pos)                  /**< (DSU_DID) Device Select Mask */
#define DSU_DID_DEVSEL(value)                 (DSU_DID_DEVSEL_Msk & ((value) << DSU_DID_DEVSEL_Pos))
#define DSU_DID_REVISION_Pos                  (8U)                                           /**< (DSU_DID) Revision Number Position */
#define DSU_DID_REVISION_Msk                  (0xFU << DSU_DID_REVISION_Pos)                 /**< (DSU_DID) Revision Number Mask */
#define DSU_DID_REVISION(value)               (DSU_DID_REVISION_Msk & ((value) << DSU_DID_REVISION_Pos))
#define DSU_DID_DIE_Pos                       (12U)                                          /**< (DSU_DID) Die Number Position */
#define DSU_DID_DIE_Msk                       (0xFU << DSU_DID_DIE_Pos)                      /**< (DSU_DID) Die Number Mask */
#define DSU_DID_DIE(value)                    (DSU_DID_DIE_Msk & ((value) << DSU_DID_DIE_Pos))
#define DSU_DID_SERIES_Pos                    (16U)                                          /**< (DSU_DID) Series Position */
#define DSU_DID_SERIES_Msk                    (0x3FU << DSU_DID_SERIES_Pos)                  /**< (DSU_DID) Series Mask */
#define DSU_DID_SERIES(value)                 (DSU_DID_SERIES_Msk & ((value) << DSU_DID_SERIES_Pos))
#define   DSU_DID_SERIES_0_Val                (0U)                                           /**< (DSU_DID) Cortex-M0+ processor, basic feature set  */
#define   DSU_DID_SERIES_1_Val                (1U)                                           /**< (DSU_DID) Cortex-M0+ processor, USB  */
#define DSU_DID_SERIES_0                      (DSU_DID_SERIES_0_Val << DSU_DID_SERIES_Pos)   /**< (DSU_DID) Cortex-M0+ processor, basic feature set Position  */
#define DSU_DID_SERIES_1                      (DSU_DID_SERIES_1_Val << DSU_DID_SERIES_Pos)   /**< (DSU_DID) Cortex-M0+ processor, USB Position  */
#define DSU_DID_FAMILY_Pos                    (23U)                                          /**< (DSU_DID) Family Position */
#define DSU_DID_FAMILY_Msk                    (0x1FU << DSU_DID_FAMILY_Pos)                  /**< (DSU_DID) Family Mask */
#define DSU_DID_FAMILY(value)                 (DSU_DID_FAMILY_Msk & ((value) << DSU_DID_FAMILY_Pos))
#define   DSU_DID_FAMILY_0_Val                (0U)                                           /**< (DSU_DID) General purpose microcontroller  */
#define   DSU_DID_FAMILY_1_Val                (1U)                                           /**< (DSU_DID) PicoPower  */
#define   DSU_DID_FAMILY_2_Val                (2U)                                           /**< (DSU_DID) 5V Industrial  */
#define DSU_DID_FAMILY_0                      (DSU_DID_FAMILY_0_Val << DSU_DID_FAMILY_Pos)   /**< (DSU_DID) General purpose microcontroller Position  */
#define DSU_DID_FAMILY_1                      (DSU_DID_FAMILY_1_Val << DSU_DID_FAMILY_Pos)   /**< (DSU_DID) PicoPower Position  */
#define DSU_DID_FAMILY_2                      (DSU_DID_FAMILY_2_Val << DSU_DID_FAMILY_Pos)   /**< (DSU_DID) 5V Industrial Position  */
#define DSU_DID_PROCESSOR_Pos                 (28U)                                          /**< (DSU_DID) Processor Position */
#define DSU_DID_PROCESSOR_Msk                 (0xFU << DSU_DID_PROCESSOR_Pos)                /**< (DSU_DID) Processor Mask */
#define DSU_DID_PROCESSOR(value)              (DSU_DID_PROCESSOR_Msk & ((value) << DSU_DID_PROCESSOR_Pos))
#define   DSU_DID_PROCESSOR_0_Val             (0U)                                           /**< (DSU_DID) Cortex-M0  */
#define   DSU_DID_PROCESSOR_1_Val             (1U)                                           /**< (DSU_DID) Cortex-M0+  */
#define   DSU_DID_PROCESSOR_2_Val             (2U)                                           /**< (DSU_DID) Cortex-M3  */
#define   DSU_DID_PROCESSOR_3_Val             (3U)                                           /**< (DSU_DID) Cortex-M4  */
#define DSU_DID_PROCESSOR_0                   (DSU_DID_PROCESSOR_0_Val << DSU_DID_PROCESSOR_Pos) /**< (DSU_DID) Cortex-M0 Position  */
#define DSU_DID_PROCESSOR_1                   (DSU_DID_PROCESSOR_1_Val << DSU_DID_PROCESSOR_Pos) /**< (DSU_DID) Cortex-M0+ Position  */
#define DSU_DID_PROCESSOR_2                   (DSU_DID_PROCESSOR_2_Val << DSU_DID_PROCESSOR_Pos) /**< (DSU_DID) Cortex-M3 Position  */
#define DSU_DID_PROCESSOR_3                   (DSU_DID_PROCESSOR_3_Val << DSU_DID_PROCESSOR_Pos) /**< (DSU_DID) Cortex-M4 Position  */
#define DSU_DID_Msk                           (0xFFBFFFFFUL)                                 /**< (DSU_DID) Register Mask  */

/* -------- DSU_DCFG : (DSU Offset: 0xF0) (R/W 32) Device Configuration -------- */
#define DSU_DCFG_DCFG_Pos                     (0U)                                           /**< (DSU_DCFG) Device Configuration Position */
#define DSU_DCFG_DCFG_Msk                     (0xFFFFFFFFU << DSU_DCFG_DCFG_Pos)             /**< (DSU_DCFG) Device Configuration Mask */
#define DSU_DCFG_DCFG(value)                  (DSU_DCFG_DCFG_Msk & ((value) << DSU_DCFG_DCFG_Pos))
#define DSU_DCFG_Msk                          (0xFFFFFFFFUL)                                 /**< (DSU_DCFG) Register Mask  */

/* -------- DSU_ENTRY0 : (DSU Offset: 0x1000) (R/  32) CoreSight ROM Table Entry 0 -------- */
#define DSU_ENTRY0_EPRES_Pos                  (0U)                                           /**< (DSU_ENTRY0) Entry Present Position */
#define DSU_ENTRY0_EPRES_Msk                  (0x1U << DSU_ENTRY0_EPRES_Pos)                 /**< (DSU_ENTRY0) Entry Present Mask */
#define DSU_ENTRY0_EPRES(value)               (DSU_ENTRY0_EPRES_Msk & ((value) << DSU_ENTRY0_EPRES_Pos))
#define DSU_ENTRY0_FMT_Pos                    (1U)                                           /**< (DSU_ENTRY0) Format Position */
#define DSU_ENTRY0_FMT_Msk                    (0x1U << DSU_ENTRY0_FMT_Pos)                   /**< (DSU_ENTRY0) Format Mask */
#define DSU_ENTRY0_FMT(value)                 (DSU_ENTRY0_FMT_Msk & ((value) << DSU_ENTRY0_FMT_Pos))
#define DSU_ENTRY0_ADDOFF_Pos                 (12U)                                          /**< (DSU_ENTRY0) Address Offset Position */
#define DSU_ENTRY0_ADDOFF_Msk                 (0xFFFFFU << DSU_ENTRY0_ADDOFF_Pos)            /**< (DSU_ENTRY0) Address Offset Mask */
#define DSU_ENTRY0_ADDOFF(value)              (DSU_ENTRY0_ADDOFF_Msk & ((value) << DSU_ENTRY0_ADDOFF_Pos))
#define DSU_ENTRY0_Msk                        (0xFFFFF003UL)                                 /**< (DSU_ENTRY0) Register Mask  */

/* -------- DSU_ENTRY1 : (DSU Offset: 0x1004) (R/  32) CoreSight ROM Table Entry 1 -------- */
#define DSU_ENTRY1_Msk                        (0x00000000UL)                                 /**< (DSU_ENTRY1) Register Mask  */

/* -------- DSU_END : (DSU Offset: 0x1008) (R/  32) CoreSight ROM Table End -------- */
#define DSU_END_END_Pos                       (0U)                                           /**< (DSU_END) End Marker Position */
#define DSU_END_END_Msk                       (0xFFFFFFFFU << DSU_END_END_Pos)               /**< (DSU_END) End Marker Mask */
#define DSU_END_END(value)                    (DSU_END_END_Msk & ((value) << DSU_END_END_Pos))
#define DSU_END_Msk                           (0xFFFFFFFFUL)                                 /**< (DSU_END) Register Mask  */

/* -------- DSU_MEMTYPE : (DSU Offset: 0x1FCC) (R/  32) CoreSight ROM Table Memory Type -------- */
#define DSU_MEMTYPE_SMEMP_Pos                 (0U)                                           /**< (DSU_MEMTYPE) System Memory Present Position */
#define DSU_MEMTYPE_SMEMP_Msk                 (0x1U << DSU_MEMTYPE_SMEMP_Pos)                /**< (DSU_MEMTYPE) System Memory Present Mask */
#define DSU_MEMTYPE_SMEMP(value)              (DSU_MEMTYPE_SMEMP_Msk & ((value) << DSU_MEMTYPE_SMEMP_Pos))
#define DSU_MEMTYPE_Msk                       (0x00000001UL)                                 /**< (DSU_MEMTYPE) Register Mask  */

/* -------- DSU_PID4 : (DSU Offset: 0x1FD0) (R/  32) Peripheral Identification 4 -------- */
#define DSU_PID4_JEPCC_Pos                    (0U)                                           /**< (DSU_PID4) JEP-106 Continuation Code Position */
#define DSU_PID4_JEPCC_Msk                    (0xFU << DSU_PID4_JEPCC_Pos)                   /**< (DSU_PID4) JEP-106 Continuation Code Mask */
#define DSU_PID4_JEPCC(value)                 (DSU_PID4_JEPCC_Msk & ((value) << DSU_PID4_JEPCC_Pos))
#define DSU_PID4_FKBC_Pos                     (4U)                                           /**< (DSU_PID4) 4KB count Position */
#define DSU_PID4_FKBC_Msk                     (0xFU << DSU_PID4_FKBC_Pos)                    /**< (DSU_PID4) 4KB count Mask */
#define DSU_PID4_FKBC(value)                  (DSU_PID4_FKBC_Msk & ((value) << DSU_PID4_FKBC_Pos))
#define DSU_PID4_Msk                          (0x000000FFUL)                                 /**< (DSU_PID4) Register Mask  */

/* -------- DSU_PID5 : (DSU Offset: 0x1FD4) (R/  32) Peripheral Identification 5 -------- */
#define DSU_PID5_Msk                          (0x00000000UL)                                 /**< (DSU_PID5) Register Mask  */

/* -------- DSU_PID6 : (DSU Offset: 0x1FD8) (R/  32) Peripheral Identification 6 -------- */
#define DSU_PID6_Msk                          (0x00000000UL)                                 /**< (DSU_PID6) Register Mask  */

/* -------- DSU_PID7 : (DSU Offset: 0x1FDC) (R/  32) Peripheral Identification 7 -------- */
#define DSU_PID7_Msk                          (0x00000000UL)                                 /**< (DSU_PID7) Register Mask  */

/* -------- DSU_PID0 : (DSU Offset: 0x1FE0) (R/  32) Peripheral Identification 0 -------- */
#define DSU_PID0_PARTNBL_Pos                  (0U)                                           /**< (DSU_PID0) Part Number Low Position */
#define DSU_PID0_PARTNBL_Msk                  (0xFFU << DSU_PID0_PARTNBL_Pos)                /**< (DSU_PID0) Part Number Low Mask */
#define DSU_PID0_PARTNBL(value)               (DSU_PID0_PARTNBL_Msk & ((value) << DSU_PID0_PARTNBL_Pos))
#define DSU_PID0_Msk                          (0x000000FFUL)                                 /**< (DSU_PID0) Register Mask  */

/* -------- DSU_PID1 : (DSU Offset: 0x1FE4) (R/  32) Peripheral Identification 1 -------- */
#define DSU_PID1_PARTNBH_Pos                  (0U)                                           /**< (DSU_PID1) Part Number High Position */
#define DSU_PID1_PARTNBH_Msk                  (0xFU << DSU_PID1_PARTNBH_Pos)                 /**< (DSU_PID1) Part Number High Mask */
#define DSU_PID1_PARTNBH(value)               (DSU_PID1_PARTNBH_Msk & ((value) << DSU_PID1_PARTNBH_Pos))
#define DSU_PID1_JEPIDCL_Pos                  (4U)                                           /**< (DSU_PID1) Low part of the JEP-106 Identity Code Position */
#define DSU_PID1_JEPIDCL_Msk                  (0xFU << DSU_PID1_JEPIDCL_Pos)                 /**< (DSU_PID1) Low part of the JEP-106 Identity Code Mask */
#define DSU_PID1_JEPIDCL(value)               (DSU_PID1_JEPIDCL_Msk & ((value) << DSU_PID1_JEPIDCL_Pos))
#define DSU_PID1_Msk                          (0x000000FFUL)                                 /**< (DSU_PID1) Register Mask  */

/* -------- DSU_PID2 : (DSU Offset: 0x1FE8) (R/  32) Peripheral Identification 2 -------- */
#define DSU_PID2_JEPIDCH_Pos                  (0U)                                           /**< (DSU_PID2) JEP-106 Identity Code High Position */
#define DSU_PID2_JEPIDCH_Msk                  (0x7U << DSU_PID2_JEPIDCH_Pos)                 /**< (DSU_PID2) JEP-106 Identity Code High Mask */
#define DSU_PID2_JEPIDCH(value)               (DSU_PID2_JEPIDCH_Msk & ((value) << DSU_PID2_JEPIDCH_Pos))
#define DSU_PID2_JEPU_Pos                     (3U)                                           /**< (DSU_PID2) JEP-106 Identity Code is used Position */
#define DSU_PID2_JEPU_Msk                     (0x1U << DSU_PID2_JEPU_Pos)                    /**< (DSU_PID2) JEP-106 Identity Code is used Mask */
#define DSU_PID2_JEPU(value)                  (DSU_PID2_JEPU_Msk & ((value) << DSU_PID2_JEPU_Pos))
#define DSU_PID2_REVISION_Pos                 (4U)                                           /**< (DSU_PID2) Revision Number Position */
#define DSU_PID2_REVISION_Msk                 (0xFU << DSU_PID2_REVISION_Pos)                /**< (DSU_PID2) Revision Number Mask */
#define DSU_PID2_REVISION(value)              (DSU_PID2_REVISION_Msk & ((value) << DSU_PID2_REVISION_Pos))
#define DSU_PID2_Msk                          (0x000000FFUL)                                 /**< (DSU_PID2) Register Mask  */

/* -------- DSU_PID3 : (DSU Offset: 0x1FEC) (R/  32) Peripheral Identification 3 -------- */
#define DSU_PID3_CUSMOD_Pos                   (0U)                                           /**< (DSU_PID3) ARM CUSMOD Position */
#define DSU_PID3_CUSMOD_Msk                   (0xFU << DSU_PID3_CUSMOD_Pos)                  /**< (DSU_PID3) ARM CUSMOD Mask */
#define DSU_PID3_CUSMOD(value)                (DSU_PID3_CUSMOD_Msk & ((value) << DSU_PID3_CUSMOD_Pos))
#define DSU_PID3_REVAND_Pos                   (4U)                                           /**< (DSU_PID3) Revision Number Position */
#define DSU_PID3_REVAND_Msk                   (0xFU << DSU_PID3_REVAND_Pos)                  /**< (DSU_PID3) Revision Number Mask */
#define DSU_PID3_REVAND(value)                (DSU_PID3_REVAND_Msk & ((value) << DSU_PID3_REVAND_Pos))
#define DSU_PID3_Msk                          (0x000000FFUL)                                 /**< (DSU_PID3) Register Mask  */

/* -------- DSU_CID0 : (DSU Offset: 0x1FF0) (R/  32) Component Identification 0 -------- */
#define DSU_CID0_PREAMBLEB0_Pos               (0U)                                           /**< (DSU_CID0) Preamble Byte 0 Position */
#define DSU_CID0_PREAMBLEB0_Msk               (0xFFU << DSU_CID0_PREAMBLEB0_Pos)             /**< (DSU_CID0) Preamble Byte 0 Mask */
#define DSU_CID0_PREAMBLEB0(value)            (DSU_CID0_PREAMBLEB0_Msk & ((value) << DSU_CID0_PREAMBLEB0_Pos))
#define DSU_CID0_Msk                          (0x000000FFUL)                                 /**< (DSU_CID0) Register Mask  */

/* -------- DSU_CID1 : (DSU Offset: 0x1FF4) (R/  32) Component Identification 1 -------- */
#define DSU_CID1_PREAMBLE_Pos                 (0U)                                           /**< (DSU_CID1) Preamble Position */
#define DSU_CID1_PREAMBLE_Msk                 (0xFU << DSU_CID1_PREAMBLE_Pos)                /**< (DSU_CID1) Preamble Mask */
#define DSU_CID1_PREAMBLE(value)              (DSU_CID1_PREAMBLE_Msk & ((value) << DSU_CID1_PREAMBLE_Pos))
#define DSU_CID1_CCLASS_Pos                   (4U)                                           /**< (DSU_CID1) Component Class Position */
#define DSU_CID1_CCLASS_Msk                   (0xFU << DSU_CID1_CCLASS_Pos)                  /**< (DSU_CID1) Component Class Mask */
#define DSU_CID1_CCLASS(value)                (DSU_CID1_CCLASS_Msk & ((value) << DSU_CID1_CCLASS_Pos))
#define DSU_CID1_Msk                          (0x000000FFUL)                                 /**< (DSU_CID1) Register Mask  */

/* -------- DSU_CID2 : (DSU Offset: 0x1FF8) (R/  32) Component Identification 2 -------- */
#define DSU_CID2_PREAMBLEB2_Pos               (0U)                                           /**< (DSU_CID2) Preamble Byte 2 Position */
#define DSU_CID2_PREAMBLEB2_Msk               (0xFFU << DSU_CID2_PREAMBLEB2_Pos)             /**< (DSU_CID2) Preamble Byte 2 Mask */
#define DSU_CID2_PREAMBLEB2(value)            (DSU_CID2_PREAMBLEB2_Msk & ((value) << DSU_CID2_PREAMBLEB2_Pos))
#define DSU_CID2_Msk                          (0x000000FFUL)                                 /**< (DSU_CID2) Register Mask  */

/* -------- DSU_CID3 : (DSU Offset: 0x1FFC) (R/  32) Component Identification 3 -------- */
#define DSU_CID3_PREAMBLEB3_Pos               (0U)                                           /**< (DSU_CID3) Preamble Byte 3 Position */
#define DSU_CID3_PREAMBLEB3_Msk               (0xFFU << DSU_CID3_PREAMBLEB3_Pos)             /**< (DSU_CID3) Preamble Byte 3 Mask */
#define DSU_CID3_PREAMBLEB3(value)            (DSU_CID3_PREAMBLEB3_Msk & ((value) << DSU_CID3_PREAMBLEB3_Pos))
#define DSU_CID3_Msk                          (0x000000FFUL)                                 /**< (DSU_CID3) Register Mask  */

/** \brief DSU register offsets definitions */
#define DSU_CTRL_OFFSET                (0x00)         /**< (DSU_CTRL) Control Offset */
#define DSU_STATUSA_OFFSET             (0x01)         /**< (DSU_STATUSA) Status A Offset */
#define DSU_STATUSB_OFFSET             (0x02)         /**< (DSU_STATUSB) Status B Offset */
#define DSU_ADDR_OFFSET                (0x04)         /**< (DSU_ADDR) Address Offset */
#define DSU_LENGTH_OFFSET              (0x08)         /**< (DSU_LENGTH) Length Offset */
#define DSU_DATA_OFFSET                (0x0C)         /**< (DSU_DATA) Data Offset */
#define DSU_DCC_OFFSET                 (0x10)         /**< (DSU_DCC) Debug Communication Channel n Offset */
#define DSU_DID_OFFSET                 (0x18)         /**< (DSU_DID) Device Identification Offset */
#define DSU_DCFG_OFFSET                (0xF0)         /**< (DSU_DCFG) Device Configuration Offset */
#define DSU_ENTRY0_OFFSET              (0x1000)       /**< (DSU_ENTRY0) CoreSight ROM Table Entry 0 Offset */
#define DSU_ENTRY1_OFFSET              (0x1004)       /**< (DSU_ENTRY1) CoreSight ROM Table Entry 1 Offset */
#define DSU_END_OFFSET                 (0x1008)       /**< (DSU_END) CoreSight ROM Table End Offset */
#define DSU_MEMTYPE_OFFSET             (0x1FCC)       /**< (DSU_MEMTYPE) CoreSight ROM Table Memory Type Offset */
#define DSU_PID4_OFFSET                (0x1FD0)       /**< (DSU_PID4) Peripheral Identification 4 Offset */
#define DSU_PID5_OFFSET                (0x1FD4)       /**< (DSU_PID5) Peripheral Identification 5 Offset */
#define DSU_PID6_OFFSET                (0x1FD8)       /**< (DSU_PID6) Peripheral Identification 6 Offset */
#define DSU_PID7_OFFSET                (0x1FDC)       /**< (DSU_PID7) Peripheral Identification 7 Offset */
#define DSU_PID0_OFFSET                (0x1FE0)       /**< (DSU_PID0) Peripheral Identification 0 Offset */
#define DSU_PID1_OFFSET                (0x1FE4)       /**< (DSU_PID1) Peripheral Identification 1 Offset */
#define DSU_PID2_OFFSET                (0x1FE8)       /**< (DSU_PID2) Peripheral Identification 2 Offset */
#define DSU_PID3_OFFSET                (0x1FEC)       /**< (DSU_PID3) Peripheral Identification 3 Offset */
#define DSU_CID0_OFFSET                (0x1FF0)       /**< (DSU_CID0) Component Identification 0 Offset */
#define DSU_CID1_OFFSET                (0x1FF4)       /**< (DSU_CID1) Component Identification 1 Offset */
#define DSU_CID2_OFFSET                (0x1FF8)       /**< (DSU_CID2) Component Identification 2 Offset */
#define DSU_CID3_OFFSET                (0x1FFC)       /**< (DSU_CID3) Component Identification 3 Offset */

/** \brief DSU register API structure */
typedef struct
{
  __O   uint8_t                        DSU_CTRL;        /**< Offset: 0x00 ( /W  8) Control */
  __IO  uint8_t                        DSU_STATUSA;     /**< Offset: 0x01 (R/W  8) Status A */
  __I   uint8_t                        DSU_STATUSB;     /**< Offset: 0x02 (R/   8) Status B */
  __I   uint8_t                        Reserved1[0x01];
  __IO  uint32_t                       DSU_ADDR;        /**< Offset: 0x04 (R/W  32) Address */
  __IO  uint32_t                       DSU_LENGTH;      /**< Offset: 0x08 (R/W  32) Length */
  __IO  uint32_t                       DSU_DATA;        /**< Offset: 0x0c (R/W  32) Data */
  __IO  uint32_t                       DSU_DCC[2];      /**< Offset: 0x10 (R/W  32) Debug Communication Channel n */
  __I   uint32_t                       DSU_DID;         /**< Offset: 0x18 (R/   32) Device Identification */
  __I   uint8_t                        Reserved2[0xD4];
  __IO  uint32_t                       DSU_DCFG[2];     /**< Offset: 0xf0 (R/W  32) Device Configuration */
  __I   uint8_t                        Reserved3[0xF08];
  __I   uint32_t                       DSU_ENTRY0;      /**< Offset: 0x1000 (R/   32) CoreSight ROM Table Entry 0 */
  __I   uint32_t                       DSU_ENTRY1;      /**< Offset: 0x1004 (R/   32) CoreSight ROM Table Entry 1 */
  __I   uint32_t                       DSU_END;         /**< Offset: 0x1008 (R/   32) CoreSight ROM Table End */
  __I   uint8_t                        Reserved4[0xFC0];
  __I   uint32_t                       DSU_MEMTYPE;     /**< Offset: 0x1fcc (R/   32) CoreSight ROM Table Memory Type */
  __I   uint32_t                       DSU_PID4;        /**< Offset: 0x1fd0 (R/   32) Peripheral Identification 4 */
  __I   uint32_t                       DSU_PID5;        /**< Offset: 0x1fd4 (R/   32) Peripheral Identification 5 */
  __I   uint32_t                       DSU_PID6;        /**< Offset: 0x1fd8 (R/   32) Peripheral Identification 6 */
  __I   uint32_t                       DSU_PID7;        /**< Offset: 0x1fdc (R/   32) Peripheral Identification 7 */
  __I   uint32_t                       DSU_PID0;        /**< Offset: 0x1fe0 (R/   32) Peripheral Identification 0 */
  __I   uint32_t                       DSU_PID1;        /**< Offset: 0x1fe4 (R/   32) Peripheral Identification 1 */
  __I   uint32_t                       DSU_PID2;        /**< Offset: 0x1fe8 (R/   32) Peripheral Identification 2 */
  __I   uint32_t                       DSU_PID3;        /**< Offset: 0x1fec (R/   32) Peripheral Identification 3 */
  __I   uint32_t                       DSU_CID0;        /**< Offset: 0x1ff0 (R/   32) Component Identification 0 */
  __I   uint32_t                       DSU_CID1;        /**< Offset: 0x1ff4 (R/   32) Component Identification 1 */
  __I   uint32_t                       DSU_CID2;        /**< Offset: 0x1ff8 (R/   32) Component Identification 2 */
  __I   uint32_t                       DSU_CID3;        /**< Offset: 0x1ffc (R/   32) Component Identification 3 */
} dsu_registers_t;
/** @}  end of Device Service Unit */

#endif /* SAMC_SAMC21_DSU_MODULE_H */

