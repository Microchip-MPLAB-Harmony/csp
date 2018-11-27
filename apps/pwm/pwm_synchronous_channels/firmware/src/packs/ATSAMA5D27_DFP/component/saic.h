/**
 * \brief Component description for SAIC
 *
 * © 2018 Microchip Technology Inc. and its subsidiaries.
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

/* file generated from device description version 2018-11-07T20:03:00Z */
#ifndef _SAMA5D2_SAIC_COMPONENT_H_
#define _SAMA5D2_SAIC_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR SAIC                                         */
/* ************************************************************************** */

/* -------- SAIC_AIC_SSR : (SAIC Offset: 0x00) (R/W 32) Source Select Register -------- */
#define SAIC_AIC_SSR_INTSEL_Pos               _U_(0)                                               /**< (SAIC_AIC_SSR) Interrupt Line Selection Position */
#define SAIC_AIC_SSR_INTSEL_Msk               (_U_(0x7F) << SAIC_AIC_SSR_INTSEL_Pos)               /**< (SAIC_AIC_SSR) Interrupt Line Selection Mask */
#define SAIC_AIC_SSR_INTSEL(value)            (SAIC_AIC_SSR_INTSEL_Msk & ((value) << SAIC_AIC_SSR_INTSEL_Pos))
#define SAIC_AIC_SSR_Msk                      _U_(0x0000007F)                                      /**< (SAIC_AIC_SSR) Register Mask  */


/* -------- SAIC_AIC_SMR : (SAIC Offset: 0x04) (R/W 32) Source Mode Register -------- */
#define SAIC_AIC_SMR_PRIOR_Pos                _U_(0)                                               /**< (SAIC_AIC_SMR) Priority Level Position */
#define SAIC_AIC_SMR_PRIOR_Msk                (_U_(0x7) << SAIC_AIC_SMR_PRIOR_Pos)                 /**< (SAIC_AIC_SMR) Priority Level Mask */
#define SAIC_AIC_SMR_PRIOR(value)             (SAIC_AIC_SMR_PRIOR_Msk & ((value) << SAIC_AIC_SMR_PRIOR_Pos))
#define SAIC_AIC_SMR_SRCTYPE_Pos              _U_(5)                                               /**< (SAIC_AIC_SMR) Interrupt Source Type Position */
#define SAIC_AIC_SMR_SRCTYPE_Msk              (_U_(0x3) << SAIC_AIC_SMR_SRCTYPE_Pos)               /**< (SAIC_AIC_SMR) Interrupt Source Type Mask */
#define SAIC_AIC_SMR_SRCTYPE(value)           (SAIC_AIC_SMR_SRCTYPE_Msk & ((value) << SAIC_AIC_SMR_SRCTYPE_Pos))
#define   SAIC_AIC_SMR_SRCTYPE_INT_LEVEL_SENSITIVE_Val _U_(0x0)                                             /**< (SAIC_AIC_SMR) High-level sensitive for internal sourceLow-level sensitive for external source  */
#define   SAIC_AIC_SMR_SRCTYPE_EXT_NEGATIVE_EDGE_Val _U_(0x1)                                             /**< (SAIC_AIC_SMR) Negative-edge triggered for external source  */
#define   SAIC_AIC_SMR_SRCTYPE_EXT_HIGH_LEVEL_Val _U_(0x2)                                             /**< (SAIC_AIC_SMR) High-level sensitive for internal sourceHigh-level sensitive for external source  */
#define   SAIC_AIC_SMR_SRCTYPE_EXT_POSITIVE_EDGE_Val _U_(0x3)                                             /**< (SAIC_AIC_SMR) Positive-edge triggered for external source  */
#define SAIC_AIC_SMR_SRCTYPE_INT_LEVEL_SENSITIVE (SAIC_AIC_SMR_SRCTYPE_INT_LEVEL_SENSITIVE_Val << SAIC_AIC_SMR_SRCTYPE_Pos) /**< (SAIC_AIC_SMR) High-level sensitive for internal sourceLow-level sensitive for external source Position  */
#define SAIC_AIC_SMR_SRCTYPE_EXT_NEGATIVE_EDGE (SAIC_AIC_SMR_SRCTYPE_EXT_NEGATIVE_EDGE_Val << SAIC_AIC_SMR_SRCTYPE_Pos) /**< (SAIC_AIC_SMR) Negative-edge triggered for external source Position  */
#define SAIC_AIC_SMR_SRCTYPE_EXT_HIGH_LEVEL   (SAIC_AIC_SMR_SRCTYPE_EXT_HIGH_LEVEL_Val << SAIC_AIC_SMR_SRCTYPE_Pos) /**< (SAIC_AIC_SMR) High-level sensitive for internal sourceHigh-level sensitive for external source Position  */
#define SAIC_AIC_SMR_SRCTYPE_EXT_POSITIVE_EDGE (SAIC_AIC_SMR_SRCTYPE_EXT_POSITIVE_EDGE_Val << SAIC_AIC_SMR_SRCTYPE_Pos) /**< (SAIC_AIC_SMR) Positive-edge triggered for external source Position  */
#define SAIC_AIC_SMR_Msk                      _U_(0x00000067)                                      /**< (SAIC_AIC_SMR) Register Mask  */


/* -------- SAIC_AIC_SVR : (SAIC Offset: 0x08) (R/W 32) Source Vector Register -------- */
#define SAIC_AIC_SVR_VECTOR_Pos               _U_(0)                                               /**< (SAIC_AIC_SVR) Source Vector Position */
#define SAIC_AIC_SVR_VECTOR_Msk               (_U_(0xFFFFFFFF) << SAIC_AIC_SVR_VECTOR_Pos)         /**< (SAIC_AIC_SVR) Source Vector Mask */
#define SAIC_AIC_SVR_VECTOR(value)            (SAIC_AIC_SVR_VECTOR_Msk & ((value) << SAIC_AIC_SVR_VECTOR_Pos))
#define SAIC_AIC_SVR_Msk                      _U_(0xFFFFFFFF)                                      /**< (SAIC_AIC_SVR) Register Mask  */


/* -------- SAIC_AIC_IVR : (SAIC Offset: 0x10) ( R/ 32) Interrupt Vector Register -------- */
#define SAIC_AIC_IVR_IRQV_Pos                 _U_(0)                                               /**< (SAIC_AIC_IVR) Interrupt Vector Register Position */
#define SAIC_AIC_IVR_IRQV_Msk                 (_U_(0xFFFFFFFF) << SAIC_AIC_IVR_IRQV_Pos)           /**< (SAIC_AIC_IVR) Interrupt Vector Register Mask */
#define SAIC_AIC_IVR_IRQV(value)              (SAIC_AIC_IVR_IRQV_Msk & ((value) << SAIC_AIC_IVR_IRQV_Pos))
#define SAIC_AIC_IVR_Msk                      _U_(0xFFFFFFFF)                                      /**< (SAIC_AIC_IVR) Register Mask  */


/* -------- SAIC_AIC_FVR : (SAIC Offset: 0x14) ( R/ 32) FIQ Vector Register -------- */
#define SAIC_AIC_FVR_FIQV_Pos                 _U_(0)                                               /**< (SAIC_AIC_FVR) FIQ Vector Register Position */
#define SAIC_AIC_FVR_FIQV_Msk                 (_U_(0xFFFFFFFF) << SAIC_AIC_FVR_FIQV_Pos)           /**< (SAIC_AIC_FVR) FIQ Vector Register Mask */
#define SAIC_AIC_FVR_FIQV(value)              (SAIC_AIC_FVR_FIQV_Msk & ((value) << SAIC_AIC_FVR_FIQV_Pos))
#define SAIC_AIC_FVR_Msk                      _U_(0xFFFFFFFF)                                      /**< (SAIC_AIC_FVR) Register Mask  */


/* -------- SAIC_AIC_ISR : (SAIC Offset: 0x18) ( R/ 32) Interrupt Status Register -------- */
#define SAIC_AIC_ISR_IRQID_Pos                _U_(0)                                               /**< (SAIC_AIC_ISR) Current Interrupt Identifier Position */
#define SAIC_AIC_ISR_IRQID_Msk                (_U_(0x7F) << SAIC_AIC_ISR_IRQID_Pos)                /**< (SAIC_AIC_ISR) Current Interrupt Identifier Mask */
#define SAIC_AIC_ISR_IRQID(value)             (SAIC_AIC_ISR_IRQID_Msk & ((value) << SAIC_AIC_ISR_IRQID_Pos))
#define SAIC_AIC_ISR_Msk                      _U_(0x0000007F)                                      /**< (SAIC_AIC_ISR) Register Mask  */


/* -------- SAIC_AIC_IPR0 : (SAIC Offset: 0x20) ( R/ 32) Interrupt Pending Register 0 -------- */
#define SAIC_AIC_IPR0_FIQ_Pos                 _U_(0)                                               /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_FIQ_Msk                 (_U_(0x1) << SAIC_AIC_IPR0_FIQ_Pos)                  /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_FIQ(value)              (SAIC_AIC_IPR0_FIQ_Msk & ((value) << SAIC_AIC_IPR0_FIQ_Pos))
#define SAIC_AIC_IPR0_PID1_Pos                _U_(1)                                               /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID1_Msk                (_U_(0x1) << SAIC_AIC_IPR0_PID1_Pos)                 /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID1(value)             (SAIC_AIC_IPR0_PID1_Msk & ((value) << SAIC_AIC_IPR0_PID1_Pos))
#define SAIC_AIC_IPR0_PID2_Pos                _U_(2)                                               /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID2_Msk                (_U_(0x1) << SAIC_AIC_IPR0_PID2_Pos)                 /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID2(value)             (SAIC_AIC_IPR0_PID2_Msk & ((value) << SAIC_AIC_IPR0_PID2_Pos))
#define SAIC_AIC_IPR0_PID3_Pos                _U_(3)                                               /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID3_Msk                (_U_(0x1) << SAIC_AIC_IPR0_PID3_Pos)                 /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID3(value)             (SAIC_AIC_IPR0_PID3_Msk & ((value) << SAIC_AIC_IPR0_PID3_Pos))
#define SAIC_AIC_IPR0_PID4_Pos                _U_(4)                                               /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID4_Msk                (_U_(0x1) << SAIC_AIC_IPR0_PID4_Pos)                 /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID4(value)             (SAIC_AIC_IPR0_PID4_Msk & ((value) << SAIC_AIC_IPR0_PID4_Pos))
#define SAIC_AIC_IPR0_PID5_Pos                _U_(5)                                               /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID5_Msk                (_U_(0x1) << SAIC_AIC_IPR0_PID5_Pos)                 /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID5(value)             (SAIC_AIC_IPR0_PID5_Msk & ((value) << SAIC_AIC_IPR0_PID5_Pos))
#define SAIC_AIC_IPR0_PID6_Pos                _U_(6)                                               /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID6_Msk                (_U_(0x1) << SAIC_AIC_IPR0_PID6_Pos)                 /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID6(value)             (SAIC_AIC_IPR0_PID6_Msk & ((value) << SAIC_AIC_IPR0_PID6_Pos))
#define SAIC_AIC_IPR0_PID7_Pos                _U_(7)                                               /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID7_Msk                (_U_(0x1) << SAIC_AIC_IPR0_PID7_Pos)                 /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID7(value)             (SAIC_AIC_IPR0_PID7_Msk & ((value) << SAIC_AIC_IPR0_PID7_Pos))
#define SAIC_AIC_IPR0_PID8_Pos                _U_(8)                                               /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID8_Msk                (_U_(0x1) << SAIC_AIC_IPR0_PID8_Pos)                 /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID8(value)             (SAIC_AIC_IPR0_PID8_Msk & ((value) << SAIC_AIC_IPR0_PID8_Pos))
#define SAIC_AIC_IPR0_PID9_Pos                _U_(9)                                               /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID9_Msk                (_U_(0x1) << SAIC_AIC_IPR0_PID9_Pos)                 /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID9(value)             (SAIC_AIC_IPR0_PID9_Msk & ((value) << SAIC_AIC_IPR0_PID9_Pos))
#define SAIC_AIC_IPR0_PID10_Pos               _U_(10)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID10_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID10_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID10(value)            (SAIC_AIC_IPR0_PID10_Msk & ((value) << SAIC_AIC_IPR0_PID10_Pos))
#define SAIC_AIC_IPR0_PID11_Pos               _U_(11)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID11_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID11_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID11(value)            (SAIC_AIC_IPR0_PID11_Msk & ((value) << SAIC_AIC_IPR0_PID11_Pos))
#define SAIC_AIC_IPR0_PID12_Pos               _U_(12)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID12_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID12_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID12(value)            (SAIC_AIC_IPR0_PID12_Msk & ((value) << SAIC_AIC_IPR0_PID12_Pos))
#define SAIC_AIC_IPR0_PID13_Pos               _U_(13)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID13_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID13_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID13(value)            (SAIC_AIC_IPR0_PID13_Msk & ((value) << SAIC_AIC_IPR0_PID13_Pos))
#define SAIC_AIC_IPR0_PID14_Pos               _U_(14)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID14_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID14_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID14(value)            (SAIC_AIC_IPR0_PID14_Msk & ((value) << SAIC_AIC_IPR0_PID14_Pos))
#define SAIC_AIC_IPR0_PID15_Pos               _U_(15)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID15_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID15_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID15(value)            (SAIC_AIC_IPR0_PID15_Msk & ((value) << SAIC_AIC_IPR0_PID15_Pos))
#define SAIC_AIC_IPR0_PID16_Pos               _U_(16)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID16_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID16_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID16(value)            (SAIC_AIC_IPR0_PID16_Msk & ((value) << SAIC_AIC_IPR0_PID16_Pos))
#define SAIC_AIC_IPR0_PID17_Pos               _U_(17)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID17_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID17_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID17(value)            (SAIC_AIC_IPR0_PID17_Msk & ((value) << SAIC_AIC_IPR0_PID17_Pos))
#define SAIC_AIC_IPR0_PID18_Pos               _U_(18)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID18_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID18_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID18(value)            (SAIC_AIC_IPR0_PID18_Msk & ((value) << SAIC_AIC_IPR0_PID18_Pos))
#define SAIC_AIC_IPR0_PID19_Pos               _U_(19)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID19_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID19_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID19(value)            (SAIC_AIC_IPR0_PID19_Msk & ((value) << SAIC_AIC_IPR0_PID19_Pos))
#define SAIC_AIC_IPR0_PID20_Pos               _U_(20)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID20_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID20_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID20(value)            (SAIC_AIC_IPR0_PID20_Msk & ((value) << SAIC_AIC_IPR0_PID20_Pos))
#define SAIC_AIC_IPR0_PID21_Pos               _U_(21)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID21_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID21_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID21(value)            (SAIC_AIC_IPR0_PID21_Msk & ((value) << SAIC_AIC_IPR0_PID21_Pos))
#define SAIC_AIC_IPR0_PID22_Pos               _U_(22)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID22_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID22_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID22(value)            (SAIC_AIC_IPR0_PID22_Msk & ((value) << SAIC_AIC_IPR0_PID22_Pos))
#define SAIC_AIC_IPR0_PID23_Pos               _U_(23)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID23_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID23_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID23(value)            (SAIC_AIC_IPR0_PID23_Msk & ((value) << SAIC_AIC_IPR0_PID23_Pos))
#define SAIC_AIC_IPR0_PID24_Pos               _U_(24)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID24_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID24_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID24(value)            (SAIC_AIC_IPR0_PID24_Msk & ((value) << SAIC_AIC_IPR0_PID24_Pos))
#define SAIC_AIC_IPR0_PID25_Pos               _U_(25)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID25_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID25_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID25(value)            (SAIC_AIC_IPR0_PID25_Msk & ((value) << SAIC_AIC_IPR0_PID25_Pos))
#define SAIC_AIC_IPR0_PID26_Pos               _U_(26)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID26_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID26_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID26(value)            (SAIC_AIC_IPR0_PID26_Msk & ((value) << SAIC_AIC_IPR0_PID26_Pos))
#define SAIC_AIC_IPR0_PID27_Pos               _U_(27)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID27_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID27_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID27(value)            (SAIC_AIC_IPR0_PID27_Msk & ((value) << SAIC_AIC_IPR0_PID27_Pos))
#define SAIC_AIC_IPR0_PID28_Pos               _U_(28)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID28_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID28_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID28(value)            (SAIC_AIC_IPR0_PID28_Msk & ((value) << SAIC_AIC_IPR0_PID28_Pos))
#define SAIC_AIC_IPR0_PID29_Pos               _U_(29)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID29_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID29_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID29(value)            (SAIC_AIC_IPR0_PID29_Msk & ((value) << SAIC_AIC_IPR0_PID29_Pos))
#define SAIC_AIC_IPR0_PID30_Pos               _U_(30)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID30_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID30_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID30(value)            (SAIC_AIC_IPR0_PID30_Msk & ((value) << SAIC_AIC_IPR0_PID30_Pos))
#define SAIC_AIC_IPR0_PID31_Pos               _U_(31)                                              /**< (SAIC_AIC_IPR0) Interrupt Pending Position */
#define SAIC_AIC_IPR0_PID31_Msk               (_U_(0x1) << SAIC_AIC_IPR0_PID31_Pos)                /**< (SAIC_AIC_IPR0) Interrupt Pending Mask */
#define SAIC_AIC_IPR0_PID31(value)            (SAIC_AIC_IPR0_PID31_Msk & ((value) << SAIC_AIC_IPR0_PID31_Pos))
#define SAIC_AIC_IPR0_Msk                     _U_(0xFFFFFFFF)                                      /**< (SAIC_AIC_IPR0) Register Mask  */

#define SAIC_AIC_IPR0_PID_Pos                 _U_(1)                                               /**< (SAIC_AIC_IPR0 Position) Interrupt Pending */
#define SAIC_AIC_IPR0_PID_Msk                 (_U_(0x7FFFFFFF) << SAIC_AIC_IPR0_PID_Pos)           /**< (SAIC_AIC_IPR0 Mask) PID */
#define SAIC_AIC_IPR0_PID(value)              (SAIC_AIC_IPR0_PID_Msk & ((value) << SAIC_AIC_IPR0_PID_Pos)) 

/* -------- SAIC_AIC_IPR1 : (SAIC Offset: 0x24) ( R/ 32) Interrupt Pending Register 1 -------- */
#define SAIC_AIC_IPR1_PID32_Pos               _U_(0)                                               /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID32_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID32_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID32(value)            (SAIC_AIC_IPR1_PID32_Msk & ((value) << SAIC_AIC_IPR1_PID32_Pos))
#define SAIC_AIC_IPR1_PID33_Pos               _U_(1)                                               /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID33_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID33_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID33(value)            (SAIC_AIC_IPR1_PID33_Msk & ((value) << SAIC_AIC_IPR1_PID33_Pos))
#define SAIC_AIC_IPR1_PID34_Pos               _U_(2)                                               /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID34_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID34_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID34(value)            (SAIC_AIC_IPR1_PID34_Msk & ((value) << SAIC_AIC_IPR1_PID34_Pos))
#define SAIC_AIC_IPR1_PID35_Pos               _U_(3)                                               /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID35_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID35_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID35(value)            (SAIC_AIC_IPR1_PID35_Msk & ((value) << SAIC_AIC_IPR1_PID35_Pos))
#define SAIC_AIC_IPR1_PID36_Pos               _U_(4)                                               /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID36_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID36_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID36(value)            (SAIC_AIC_IPR1_PID36_Msk & ((value) << SAIC_AIC_IPR1_PID36_Pos))
#define SAIC_AIC_IPR1_PID37_Pos               _U_(5)                                               /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID37_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID37_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID37(value)            (SAIC_AIC_IPR1_PID37_Msk & ((value) << SAIC_AIC_IPR1_PID37_Pos))
#define SAIC_AIC_IPR1_PID38_Pos               _U_(6)                                               /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID38_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID38_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID38(value)            (SAIC_AIC_IPR1_PID38_Msk & ((value) << SAIC_AIC_IPR1_PID38_Pos))
#define SAIC_AIC_IPR1_PID39_Pos               _U_(7)                                               /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID39_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID39_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID39(value)            (SAIC_AIC_IPR1_PID39_Msk & ((value) << SAIC_AIC_IPR1_PID39_Pos))
#define SAIC_AIC_IPR1_PID40_Pos               _U_(8)                                               /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID40_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID40_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID40(value)            (SAIC_AIC_IPR1_PID40_Msk & ((value) << SAIC_AIC_IPR1_PID40_Pos))
#define SAIC_AIC_IPR1_PID41_Pos               _U_(9)                                               /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID41_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID41_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID41(value)            (SAIC_AIC_IPR1_PID41_Msk & ((value) << SAIC_AIC_IPR1_PID41_Pos))
#define SAIC_AIC_IPR1_PID42_Pos               _U_(10)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID42_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID42_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID42(value)            (SAIC_AIC_IPR1_PID42_Msk & ((value) << SAIC_AIC_IPR1_PID42_Pos))
#define SAIC_AIC_IPR1_PID43_Pos               _U_(11)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID43_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID43_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID43(value)            (SAIC_AIC_IPR1_PID43_Msk & ((value) << SAIC_AIC_IPR1_PID43_Pos))
#define SAIC_AIC_IPR1_PID44_Pos               _U_(12)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID44_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID44_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID44(value)            (SAIC_AIC_IPR1_PID44_Msk & ((value) << SAIC_AIC_IPR1_PID44_Pos))
#define SAIC_AIC_IPR1_PID45_Pos               _U_(13)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID45_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID45_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID45(value)            (SAIC_AIC_IPR1_PID45_Msk & ((value) << SAIC_AIC_IPR1_PID45_Pos))
#define SAIC_AIC_IPR1_PID46_Pos               _U_(14)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID46_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID46_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID46(value)            (SAIC_AIC_IPR1_PID46_Msk & ((value) << SAIC_AIC_IPR1_PID46_Pos))
#define SAIC_AIC_IPR1_PID47_Pos               _U_(15)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID47_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID47_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID47(value)            (SAIC_AIC_IPR1_PID47_Msk & ((value) << SAIC_AIC_IPR1_PID47_Pos))
#define SAIC_AIC_IPR1_PID48_Pos               _U_(16)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID48_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID48_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID48(value)            (SAIC_AIC_IPR1_PID48_Msk & ((value) << SAIC_AIC_IPR1_PID48_Pos))
#define SAIC_AIC_IPR1_PID49_Pos               _U_(17)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID49_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID49_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID49(value)            (SAIC_AIC_IPR1_PID49_Msk & ((value) << SAIC_AIC_IPR1_PID49_Pos))
#define SAIC_AIC_IPR1_PID50_Pos               _U_(18)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID50_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID50_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID50(value)            (SAIC_AIC_IPR1_PID50_Msk & ((value) << SAIC_AIC_IPR1_PID50_Pos))
#define SAIC_AIC_IPR1_PID51_Pos               _U_(19)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID51_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID51_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID51(value)            (SAIC_AIC_IPR1_PID51_Msk & ((value) << SAIC_AIC_IPR1_PID51_Pos))
#define SAIC_AIC_IPR1_PID52_Pos               _U_(20)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID52_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID52_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID52(value)            (SAIC_AIC_IPR1_PID52_Msk & ((value) << SAIC_AIC_IPR1_PID52_Pos))
#define SAIC_AIC_IPR1_PID53_Pos               _U_(21)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID53_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID53_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID53(value)            (SAIC_AIC_IPR1_PID53_Msk & ((value) << SAIC_AIC_IPR1_PID53_Pos))
#define SAIC_AIC_IPR1_PID54_Pos               _U_(22)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID54_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID54_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID54(value)            (SAIC_AIC_IPR1_PID54_Msk & ((value) << SAIC_AIC_IPR1_PID54_Pos))
#define SAIC_AIC_IPR1_PID55_Pos               _U_(23)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID55_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID55_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID55(value)            (SAIC_AIC_IPR1_PID55_Msk & ((value) << SAIC_AIC_IPR1_PID55_Pos))
#define SAIC_AIC_IPR1_PID56_Pos               _U_(24)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID56_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID56_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID56(value)            (SAIC_AIC_IPR1_PID56_Msk & ((value) << SAIC_AIC_IPR1_PID56_Pos))
#define SAIC_AIC_IPR1_PID57_Pos               _U_(25)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID57_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID57_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID57(value)            (SAIC_AIC_IPR1_PID57_Msk & ((value) << SAIC_AIC_IPR1_PID57_Pos))
#define SAIC_AIC_IPR1_PID58_Pos               _U_(26)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID58_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID58_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID58(value)            (SAIC_AIC_IPR1_PID58_Msk & ((value) << SAIC_AIC_IPR1_PID58_Pos))
#define SAIC_AIC_IPR1_PID59_Pos               _U_(27)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID59_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID59_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID59(value)            (SAIC_AIC_IPR1_PID59_Msk & ((value) << SAIC_AIC_IPR1_PID59_Pos))
#define SAIC_AIC_IPR1_PID60_Pos               _U_(28)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID60_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID60_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID60(value)            (SAIC_AIC_IPR1_PID60_Msk & ((value) << SAIC_AIC_IPR1_PID60_Pos))
#define SAIC_AIC_IPR1_PID61_Pos               _U_(29)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID61_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID61_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID61(value)            (SAIC_AIC_IPR1_PID61_Msk & ((value) << SAIC_AIC_IPR1_PID61_Pos))
#define SAIC_AIC_IPR1_PID62_Pos               _U_(30)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID62_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID62_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID62(value)            (SAIC_AIC_IPR1_PID62_Msk & ((value) << SAIC_AIC_IPR1_PID62_Pos))
#define SAIC_AIC_IPR1_PID63_Pos               _U_(31)                                              /**< (SAIC_AIC_IPR1) Interrupt Pending Position */
#define SAIC_AIC_IPR1_PID63_Msk               (_U_(0x1) << SAIC_AIC_IPR1_PID63_Pos)                /**< (SAIC_AIC_IPR1) Interrupt Pending Mask */
#define SAIC_AIC_IPR1_PID63(value)            (SAIC_AIC_IPR1_PID63_Msk & ((value) << SAIC_AIC_IPR1_PID63_Pos))
#define SAIC_AIC_IPR1_Msk                     _U_(0xFFFFFFFF)                                      /**< (SAIC_AIC_IPR1) Register Mask  */

#define SAIC_AIC_IPR1_PID_Pos                 _U_(0)                                               /**< (SAIC_AIC_IPR1 Position) Interrupt Pending */
#define SAIC_AIC_IPR1_PID_Msk                 (_U_(0xFFFFFFFF) << SAIC_AIC_IPR1_PID_Pos)           /**< (SAIC_AIC_IPR1 Mask) PID */
#define SAIC_AIC_IPR1_PID(value)              (SAIC_AIC_IPR1_PID_Msk & ((value) << SAIC_AIC_IPR1_PID_Pos)) 

/* -------- SAIC_AIC_IPR2 : (SAIC Offset: 0x28) ( R/ 32) Interrupt Pending Register 2 -------- */
#define SAIC_AIC_IPR2_PID64_Pos               _U_(0)                                               /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID64_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID64_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID64(value)            (SAIC_AIC_IPR2_PID64_Msk & ((value) << SAIC_AIC_IPR2_PID64_Pos))
#define SAIC_AIC_IPR2_PID65_Pos               _U_(1)                                               /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID65_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID65_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID65(value)            (SAIC_AIC_IPR2_PID65_Msk & ((value) << SAIC_AIC_IPR2_PID65_Pos))
#define SAIC_AIC_IPR2_PID66_Pos               _U_(2)                                               /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID66_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID66_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID66(value)            (SAIC_AIC_IPR2_PID66_Msk & ((value) << SAIC_AIC_IPR2_PID66_Pos))
#define SAIC_AIC_IPR2_PID67_Pos               _U_(3)                                               /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID67_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID67_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID67(value)            (SAIC_AIC_IPR2_PID67_Msk & ((value) << SAIC_AIC_IPR2_PID67_Pos))
#define SAIC_AIC_IPR2_PID68_Pos               _U_(4)                                               /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID68_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID68_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID68(value)            (SAIC_AIC_IPR2_PID68_Msk & ((value) << SAIC_AIC_IPR2_PID68_Pos))
#define SAIC_AIC_IPR2_PID69_Pos               _U_(5)                                               /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID69_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID69_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID69(value)            (SAIC_AIC_IPR2_PID69_Msk & ((value) << SAIC_AIC_IPR2_PID69_Pos))
#define SAIC_AIC_IPR2_PID70_Pos               _U_(6)                                               /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID70_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID70_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID70(value)            (SAIC_AIC_IPR2_PID70_Msk & ((value) << SAIC_AIC_IPR2_PID70_Pos))
#define SAIC_AIC_IPR2_PID71_Pos               _U_(7)                                               /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID71_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID71_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID71(value)            (SAIC_AIC_IPR2_PID71_Msk & ((value) << SAIC_AIC_IPR2_PID71_Pos))
#define SAIC_AIC_IPR2_PID72_Pos               _U_(8)                                               /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID72_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID72_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID72(value)            (SAIC_AIC_IPR2_PID72_Msk & ((value) << SAIC_AIC_IPR2_PID72_Pos))
#define SAIC_AIC_IPR2_PID73_Pos               _U_(9)                                               /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID73_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID73_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID73(value)            (SAIC_AIC_IPR2_PID73_Msk & ((value) << SAIC_AIC_IPR2_PID73_Pos))
#define SAIC_AIC_IPR2_SYS_Pos                 _U_(10)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_SYS_Msk                 (_U_(0x1) << SAIC_AIC_IPR2_SYS_Pos)                  /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_SYS(value)              (SAIC_AIC_IPR2_SYS_Msk & ((value) << SAIC_AIC_IPR2_SYS_Pos))
#define SAIC_AIC_IPR2_PID75_Pos               _U_(11)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID75_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID75_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID75(value)            (SAIC_AIC_IPR2_PID75_Msk & ((value) << SAIC_AIC_IPR2_PID75_Pos))
#define SAIC_AIC_IPR2_PID76_Pos               _U_(12)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID76_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID76_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID76(value)            (SAIC_AIC_IPR2_PID76_Msk & ((value) << SAIC_AIC_IPR2_PID76_Pos))
#define SAIC_AIC_IPR2_PID77_Pos               _U_(13)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID77_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID77_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID77(value)            (SAIC_AIC_IPR2_PID77_Msk & ((value) << SAIC_AIC_IPR2_PID77_Pos))
#define SAIC_AIC_IPR2_PID78_Pos               _U_(14)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID78_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID78_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID78(value)            (SAIC_AIC_IPR2_PID78_Msk & ((value) << SAIC_AIC_IPR2_PID78_Pos))
#define SAIC_AIC_IPR2_PID79_Pos               _U_(15)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID79_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID79_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID79(value)            (SAIC_AIC_IPR2_PID79_Msk & ((value) << SAIC_AIC_IPR2_PID79_Pos))
#define SAIC_AIC_IPR2_PID80_Pos               _U_(16)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID80_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID80_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID80(value)            (SAIC_AIC_IPR2_PID80_Msk & ((value) << SAIC_AIC_IPR2_PID80_Pos))
#define SAIC_AIC_IPR2_PID81_Pos               _U_(17)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID81_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID81_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID81(value)            (SAIC_AIC_IPR2_PID81_Msk & ((value) << SAIC_AIC_IPR2_PID81_Pos))
#define SAIC_AIC_IPR2_PID82_Pos               _U_(18)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID82_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID82_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID82(value)            (SAIC_AIC_IPR2_PID82_Msk & ((value) << SAIC_AIC_IPR2_PID82_Pos))
#define SAIC_AIC_IPR2_PID83_Pos               _U_(19)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID83_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID83_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID83(value)            (SAIC_AIC_IPR2_PID83_Msk & ((value) << SAIC_AIC_IPR2_PID83_Pos))
#define SAIC_AIC_IPR2_PID84_Pos               _U_(20)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID84_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID84_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID84(value)            (SAIC_AIC_IPR2_PID84_Msk & ((value) << SAIC_AIC_IPR2_PID84_Pos))
#define SAIC_AIC_IPR2_PID85_Pos               _U_(21)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID85_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID85_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID85(value)            (SAIC_AIC_IPR2_PID85_Msk & ((value) << SAIC_AIC_IPR2_PID85_Pos))
#define SAIC_AIC_IPR2_PID86_Pos               _U_(22)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID86_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID86_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID86(value)            (SAIC_AIC_IPR2_PID86_Msk & ((value) << SAIC_AIC_IPR2_PID86_Pos))
#define SAIC_AIC_IPR2_PID87_Pos               _U_(23)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID87_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID87_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID87(value)            (SAIC_AIC_IPR2_PID87_Msk & ((value) << SAIC_AIC_IPR2_PID87_Pos))
#define SAIC_AIC_IPR2_PID88_Pos               _U_(24)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID88_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID88_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID88(value)            (SAIC_AIC_IPR2_PID88_Msk & ((value) << SAIC_AIC_IPR2_PID88_Pos))
#define SAIC_AIC_IPR2_PID89_Pos               _U_(25)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID89_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID89_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID89(value)            (SAIC_AIC_IPR2_PID89_Msk & ((value) << SAIC_AIC_IPR2_PID89_Pos))
#define SAIC_AIC_IPR2_PID90_Pos               _U_(26)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID90_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID90_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID90(value)            (SAIC_AIC_IPR2_PID90_Msk & ((value) << SAIC_AIC_IPR2_PID90_Pos))
#define SAIC_AIC_IPR2_PID91_Pos               _U_(27)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID91_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID91_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID91(value)            (SAIC_AIC_IPR2_PID91_Msk & ((value) << SAIC_AIC_IPR2_PID91_Pos))
#define SAIC_AIC_IPR2_PID92_Pos               _U_(28)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID92_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID92_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID92(value)            (SAIC_AIC_IPR2_PID92_Msk & ((value) << SAIC_AIC_IPR2_PID92_Pos))
#define SAIC_AIC_IPR2_PID93_Pos               _U_(29)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID93_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID93_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID93(value)            (SAIC_AIC_IPR2_PID93_Msk & ((value) << SAIC_AIC_IPR2_PID93_Pos))
#define SAIC_AIC_IPR2_PID94_Pos               _U_(30)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID94_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID94_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID94(value)            (SAIC_AIC_IPR2_PID94_Msk & ((value) << SAIC_AIC_IPR2_PID94_Pos))
#define SAIC_AIC_IPR2_PID95_Pos               _U_(31)                                              /**< (SAIC_AIC_IPR2) Interrupt Pending Position */
#define SAIC_AIC_IPR2_PID95_Msk               (_U_(0x1) << SAIC_AIC_IPR2_PID95_Pos)                /**< (SAIC_AIC_IPR2) Interrupt Pending Mask */
#define SAIC_AIC_IPR2_PID95(value)            (SAIC_AIC_IPR2_PID95_Msk & ((value) << SAIC_AIC_IPR2_PID95_Pos))
#define SAIC_AIC_IPR2_Msk                     _U_(0xFFFFFFFF)                                      /**< (SAIC_AIC_IPR2) Register Mask  */


/* -------- SAIC_AIC_IPR3 : (SAIC Offset: 0x2C) ( R/ 32) Interrupt Pending Register 3 -------- */
#define SAIC_AIC_IPR3_PID96_Pos               _U_(0)                                               /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID96_Msk               (_U_(0x1) << SAIC_AIC_IPR3_PID96_Pos)                /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID96(value)            (SAIC_AIC_IPR3_PID96_Msk & ((value) << SAIC_AIC_IPR3_PID96_Pos))
#define SAIC_AIC_IPR3_PID97_Pos               _U_(1)                                               /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID97_Msk               (_U_(0x1) << SAIC_AIC_IPR3_PID97_Pos)                /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID97(value)            (SAIC_AIC_IPR3_PID97_Msk & ((value) << SAIC_AIC_IPR3_PID97_Pos))
#define SAIC_AIC_IPR3_PID98_Pos               _U_(2)                                               /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID98_Msk               (_U_(0x1) << SAIC_AIC_IPR3_PID98_Pos)                /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID98(value)            (SAIC_AIC_IPR3_PID98_Msk & ((value) << SAIC_AIC_IPR3_PID98_Pos))
#define SAIC_AIC_IPR3_PID99_Pos               _U_(3)                                               /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID99_Msk               (_U_(0x1) << SAIC_AIC_IPR3_PID99_Pos)                /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID99(value)            (SAIC_AIC_IPR3_PID99_Msk & ((value) << SAIC_AIC_IPR3_PID99_Pos))
#define SAIC_AIC_IPR3_PID100_Pos              _U_(4)                                               /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID100_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID100_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID100(value)           (SAIC_AIC_IPR3_PID100_Msk & ((value) << SAIC_AIC_IPR3_PID100_Pos))
#define SAIC_AIC_IPR3_PID101_Pos              _U_(5)                                               /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID101_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID101_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID101(value)           (SAIC_AIC_IPR3_PID101_Msk & ((value) << SAIC_AIC_IPR3_PID101_Pos))
#define SAIC_AIC_IPR3_PID102_Pos              _U_(6)                                               /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID102_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID102_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID102(value)           (SAIC_AIC_IPR3_PID102_Msk & ((value) << SAIC_AIC_IPR3_PID102_Pos))
#define SAIC_AIC_IPR3_PID103_Pos              _U_(7)                                               /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID103_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID103_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID103(value)           (SAIC_AIC_IPR3_PID103_Msk & ((value) << SAIC_AIC_IPR3_PID103_Pos))
#define SAIC_AIC_IPR3_PID104_Pos              _U_(8)                                               /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID104_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID104_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID104(value)           (SAIC_AIC_IPR3_PID104_Msk & ((value) << SAIC_AIC_IPR3_PID104_Pos))
#define SAIC_AIC_IPR3_PID105_Pos              _U_(9)                                               /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID105_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID105_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID105(value)           (SAIC_AIC_IPR3_PID105_Msk & ((value) << SAIC_AIC_IPR3_PID105_Pos))
#define SAIC_AIC_IPR3_PID106_Pos              _U_(10)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID106_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID106_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID106(value)           (SAIC_AIC_IPR3_PID106_Msk & ((value) << SAIC_AIC_IPR3_PID106_Pos))
#define SAIC_AIC_IPR3_PID107_Pos              _U_(11)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID107_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID107_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID107(value)           (SAIC_AIC_IPR3_PID107_Msk & ((value) << SAIC_AIC_IPR3_PID107_Pos))
#define SAIC_AIC_IPR3_PID108_Pos              _U_(12)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID108_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID108_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID108(value)           (SAIC_AIC_IPR3_PID108_Msk & ((value) << SAIC_AIC_IPR3_PID108_Pos))
#define SAIC_AIC_IPR3_PID109_Pos              _U_(13)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID109_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID109_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID109(value)           (SAIC_AIC_IPR3_PID109_Msk & ((value) << SAIC_AIC_IPR3_PID109_Pos))
#define SAIC_AIC_IPR3_PID110_Pos              _U_(14)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID110_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID110_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID110(value)           (SAIC_AIC_IPR3_PID110_Msk & ((value) << SAIC_AIC_IPR3_PID110_Pos))
#define SAIC_AIC_IPR3_PID111_Pos              _U_(15)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID111_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID111_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID111(value)           (SAIC_AIC_IPR3_PID111_Msk & ((value) << SAIC_AIC_IPR3_PID111_Pos))
#define SAIC_AIC_IPR3_PID112_Pos              _U_(16)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID112_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID112_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID112(value)           (SAIC_AIC_IPR3_PID112_Msk & ((value) << SAIC_AIC_IPR3_PID112_Pos))
#define SAIC_AIC_IPR3_PID113_Pos              _U_(17)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID113_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID113_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID113(value)           (SAIC_AIC_IPR3_PID113_Msk & ((value) << SAIC_AIC_IPR3_PID113_Pos))
#define SAIC_AIC_IPR3_PID114_Pos              _U_(18)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID114_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID114_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID114(value)           (SAIC_AIC_IPR3_PID114_Msk & ((value) << SAIC_AIC_IPR3_PID114_Pos))
#define SAIC_AIC_IPR3_PID115_Pos              _U_(19)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID115_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID115_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID115(value)           (SAIC_AIC_IPR3_PID115_Msk & ((value) << SAIC_AIC_IPR3_PID115_Pos))
#define SAIC_AIC_IPR3_PID116_Pos              _U_(20)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID116_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID116_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID116(value)           (SAIC_AIC_IPR3_PID116_Msk & ((value) << SAIC_AIC_IPR3_PID116_Pos))
#define SAIC_AIC_IPR3_PID117_Pos              _U_(21)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID117_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID117_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID117(value)           (SAIC_AIC_IPR3_PID117_Msk & ((value) << SAIC_AIC_IPR3_PID117_Pos))
#define SAIC_AIC_IPR3_PID118_Pos              _U_(22)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID118_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID118_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID118(value)           (SAIC_AIC_IPR3_PID118_Msk & ((value) << SAIC_AIC_IPR3_PID118_Pos))
#define SAIC_AIC_IPR3_PID119_Pos              _U_(23)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID119_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID119_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID119(value)           (SAIC_AIC_IPR3_PID119_Msk & ((value) << SAIC_AIC_IPR3_PID119_Pos))
#define SAIC_AIC_IPR3_PID120_Pos              _U_(24)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID120_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID120_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID120(value)           (SAIC_AIC_IPR3_PID120_Msk & ((value) << SAIC_AIC_IPR3_PID120_Pos))
#define SAIC_AIC_IPR3_PID121_Pos              _U_(25)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID121_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID121_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID121(value)           (SAIC_AIC_IPR3_PID121_Msk & ((value) << SAIC_AIC_IPR3_PID121_Pos))
#define SAIC_AIC_IPR3_PID122_Pos              _U_(26)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID122_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID122_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID122(value)           (SAIC_AIC_IPR3_PID122_Msk & ((value) << SAIC_AIC_IPR3_PID122_Pos))
#define SAIC_AIC_IPR3_PID123_Pos              _U_(27)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID123_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID123_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID123(value)           (SAIC_AIC_IPR3_PID123_Msk & ((value) << SAIC_AIC_IPR3_PID123_Pos))
#define SAIC_AIC_IPR3_PID124_Pos              _U_(28)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID124_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID124_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID124(value)           (SAIC_AIC_IPR3_PID124_Msk & ((value) << SAIC_AIC_IPR3_PID124_Pos))
#define SAIC_AIC_IPR3_PID125_Pos              _U_(29)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID125_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID125_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID125(value)           (SAIC_AIC_IPR3_PID125_Msk & ((value) << SAIC_AIC_IPR3_PID125_Pos))
#define SAIC_AIC_IPR3_PID126_Pos              _U_(30)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID126_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID126_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID126(value)           (SAIC_AIC_IPR3_PID126_Msk & ((value) << SAIC_AIC_IPR3_PID126_Pos))
#define SAIC_AIC_IPR3_PID127_Pos              _U_(31)                                              /**< (SAIC_AIC_IPR3) Interrupt Pending Position */
#define SAIC_AIC_IPR3_PID127_Msk              (_U_(0x1) << SAIC_AIC_IPR3_PID127_Pos)               /**< (SAIC_AIC_IPR3) Interrupt Pending Mask */
#define SAIC_AIC_IPR3_PID127(value)           (SAIC_AIC_IPR3_PID127_Msk & ((value) << SAIC_AIC_IPR3_PID127_Pos))
#define SAIC_AIC_IPR3_Msk                     _U_(0xFFFFFFFF)                                      /**< (SAIC_AIC_IPR3) Register Mask  */

#define SAIC_AIC_IPR3_PID_Pos                 _U_(0)                                               /**< (SAIC_AIC_IPR3 Position) Interrupt Pending */
#define SAIC_AIC_IPR3_PID_Msk                 (_U_(0xFFFFFFFF) << SAIC_AIC_IPR3_PID_Pos)           /**< (SAIC_AIC_IPR3 Mask) PID */
#define SAIC_AIC_IPR3_PID(value)              (SAIC_AIC_IPR3_PID_Msk & ((value) << SAIC_AIC_IPR3_PID_Pos)) 

/* -------- SAIC_AIC_IMR : (SAIC Offset: 0x30) ( R/ 32) Interrupt Mask Register -------- */
#define SAIC_AIC_IMR_INTM_Pos                 _U_(0)                                               /**< (SAIC_AIC_IMR) Interrupt Mask Position */
#define SAIC_AIC_IMR_INTM_Msk                 (_U_(0x1) << SAIC_AIC_IMR_INTM_Pos)                  /**< (SAIC_AIC_IMR) Interrupt Mask Mask */
#define SAIC_AIC_IMR_INTM(value)              (SAIC_AIC_IMR_INTM_Msk & ((value) << SAIC_AIC_IMR_INTM_Pos))
#define SAIC_AIC_IMR_Msk                      _U_(0x00000001)                                      /**< (SAIC_AIC_IMR) Register Mask  */


/* -------- SAIC_AIC_CISR : (SAIC Offset: 0x34) ( R/ 32) Core Interrupt Status Register -------- */
#define SAIC_AIC_CISR_NFIQ_Pos                _U_(0)                                               /**< (SAIC_AIC_CISR) NFIQ Status Position */
#define SAIC_AIC_CISR_NFIQ_Msk                (_U_(0x1) << SAIC_AIC_CISR_NFIQ_Pos)                 /**< (SAIC_AIC_CISR) NFIQ Status Mask */
#define SAIC_AIC_CISR_NFIQ(value)             (SAIC_AIC_CISR_NFIQ_Msk & ((value) << SAIC_AIC_CISR_NFIQ_Pos))
#define SAIC_AIC_CISR_NIRQ_Pos                _U_(1)                                               /**< (SAIC_AIC_CISR) NIRQ Status Position */
#define SAIC_AIC_CISR_NIRQ_Msk                (_U_(0x1) << SAIC_AIC_CISR_NIRQ_Pos)                 /**< (SAIC_AIC_CISR) NIRQ Status Mask */
#define SAIC_AIC_CISR_NIRQ(value)             (SAIC_AIC_CISR_NIRQ_Msk & ((value) << SAIC_AIC_CISR_NIRQ_Pos))
#define SAIC_AIC_CISR_Msk                     _U_(0x00000003)                                      /**< (SAIC_AIC_CISR) Register Mask  */


/* -------- SAIC_AIC_EOICR : (SAIC Offset: 0x38) ( /W 32) End of Interrupt Command Register -------- */
#define SAIC_AIC_EOICR_ENDIT_Pos              _U_(0)                                               /**< (SAIC_AIC_EOICR) Interrupt Processing Complete Command Position */
#define SAIC_AIC_EOICR_ENDIT_Msk              (_U_(0x1) << SAIC_AIC_EOICR_ENDIT_Pos)               /**< (SAIC_AIC_EOICR) Interrupt Processing Complete Command Mask */
#define SAIC_AIC_EOICR_ENDIT(value)           (SAIC_AIC_EOICR_ENDIT_Msk & ((value) << SAIC_AIC_EOICR_ENDIT_Pos))
#define SAIC_AIC_EOICR_Msk                    _U_(0x00000001)                                      /**< (SAIC_AIC_EOICR) Register Mask  */


/* -------- SAIC_AIC_SPU : (SAIC Offset: 0x3C) (R/W 32) Spurious Interrupt Vector Register -------- */
#define SAIC_AIC_SPU_SIVR_Pos                 _U_(0)                                               /**< (SAIC_AIC_SPU) Spurious Interrupt Vector Register Position */
#define SAIC_AIC_SPU_SIVR_Msk                 (_U_(0xFFFFFFFF) << SAIC_AIC_SPU_SIVR_Pos)           /**< (SAIC_AIC_SPU) Spurious Interrupt Vector Register Mask */
#define SAIC_AIC_SPU_SIVR(value)              (SAIC_AIC_SPU_SIVR_Msk & ((value) << SAIC_AIC_SPU_SIVR_Pos))
#define SAIC_AIC_SPU_Msk                      _U_(0xFFFFFFFF)                                      /**< (SAIC_AIC_SPU) Register Mask  */


/* -------- SAIC_AIC_IECR : (SAIC Offset: 0x40) ( /W 32) Interrupt Enable Command Register -------- */
#define SAIC_AIC_IECR_INTEN_Pos               _U_(0)                                               /**< (SAIC_AIC_IECR) Interrupt Enable Position */
#define SAIC_AIC_IECR_INTEN_Msk               (_U_(0x1) << SAIC_AIC_IECR_INTEN_Pos)                /**< (SAIC_AIC_IECR) Interrupt Enable Mask */
#define SAIC_AIC_IECR_INTEN(value)            (SAIC_AIC_IECR_INTEN_Msk & ((value) << SAIC_AIC_IECR_INTEN_Pos))
#define SAIC_AIC_IECR_Msk                     _U_(0x00000001)                                      /**< (SAIC_AIC_IECR) Register Mask  */


/* -------- SAIC_AIC_IDCR : (SAIC Offset: 0x44) ( /W 32) Interrupt Disable Command Register -------- */
#define SAIC_AIC_IDCR_INTD_Pos                _U_(0)                                               /**< (SAIC_AIC_IDCR) Interrupt Disable Position */
#define SAIC_AIC_IDCR_INTD_Msk                (_U_(0x1) << SAIC_AIC_IDCR_INTD_Pos)                 /**< (SAIC_AIC_IDCR) Interrupt Disable Mask */
#define SAIC_AIC_IDCR_INTD(value)             (SAIC_AIC_IDCR_INTD_Msk & ((value) << SAIC_AIC_IDCR_INTD_Pos))
#define SAIC_AIC_IDCR_Msk                     _U_(0x00000001)                                      /**< (SAIC_AIC_IDCR) Register Mask  */


/* -------- SAIC_AIC_ICCR : (SAIC Offset: 0x48) ( /W 32) Interrupt Clear Command Register -------- */
#define SAIC_AIC_ICCR_INTCLR_Pos              _U_(0)                                               /**< (SAIC_AIC_ICCR) Interrupt Clear Position */
#define SAIC_AIC_ICCR_INTCLR_Msk              (_U_(0x1) << SAIC_AIC_ICCR_INTCLR_Pos)               /**< (SAIC_AIC_ICCR) Interrupt Clear Mask */
#define SAIC_AIC_ICCR_INTCLR(value)           (SAIC_AIC_ICCR_INTCLR_Msk & ((value) << SAIC_AIC_ICCR_INTCLR_Pos))
#define SAIC_AIC_ICCR_Msk                     _U_(0x00000001)                                      /**< (SAIC_AIC_ICCR) Register Mask  */


/* -------- SAIC_AIC_ISCR : (SAIC Offset: 0x4C) ( /W 32) Interrupt Set Command Register -------- */
#define SAIC_AIC_ISCR_INTSET_Pos              _U_(0)                                               /**< (SAIC_AIC_ISCR) Interrupt Set Position */
#define SAIC_AIC_ISCR_INTSET_Msk              (_U_(0x1) << SAIC_AIC_ISCR_INTSET_Pos)               /**< (SAIC_AIC_ISCR) Interrupt Set Mask */
#define SAIC_AIC_ISCR_INTSET(value)           (SAIC_AIC_ISCR_INTSET_Msk & ((value) << SAIC_AIC_ISCR_INTSET_Pos))
#define SAIC_AIC_ISCR_Msk                     _U_(0x00000001)                                      /**< (SAIC_AIC_ISCR) Register Mask  */


/* -------- SAIC_AIC_DCR : (SAIC Offset: 0x6C) (R/W 32) Debug Control Register -------- */
#define SAIC_AIC_DCR_PROT_Pos                 _U_(0)                                               /**< (SAIC_AIC_DCR) Protection Mode Position */
#define SAIC_AIC_DCR_PROT_Msk                 (_U_(0x1) << SAIC_AIC_DCR_PROT_Pos)                  /**< (SAIC_AIC_DCR) Protection Mode Mask */
#define SAIC_AIC_DCR_PROT(value)              (SAIC_AIC_DCR_PROT_Msk & ((value) << SAIC_AIC_DCR_PROT_Pos))
#define SAIC_AIC_DCR_GMSK_Pos                 _U_(1)                                               /**< (SAIC_AIC_DCR) General Interrupt Mask Position */
#define SAIC_AIC_DCR_GMSK_Msk                 (_U_(0x1) << SAIC_AIC_DCR_GMSK_Pos)                  /**< (SAIC_AIC_DCR) General Interrupt Mask Mask */
#define SAIC_AIC_DCR_GMSK(value)              (SAIC_AIC_DCR_GMSK_Msk & ((value) << SAIC_AIC_DCR_GMSK_Pos))
#define SAIC_AIC_DCR_Msk                      _U_(0x00000003)                                      /**< (SAIC_AIC_DCR) Register Mask  */


/* -------- SAIC_AIC_WPMR : (SAIC Offset: 0xE4) (R/W 32) Write Protection Mode Register -------- */
#define SAIC_AIC_WPMR_WPEN_Pos                _U_(0)                                               /**< (SAIC_AIC_WPMR) Write Protection Enable Position */
#define SAIC_AIC_WPMR_WPEN_Msk                (_U_(0x1) << SAIC_AIC_WPMR_WPEN_Pos)                 /**< (SAIC_AIC_WPMR) Write Protection Enable Mask */
#define SAIC_AIC_WPMR_WPEN(value)             (SAIC_AIC_WPMR_WPEN_Msk & ((value) << SAIC_AIC_WPMR_WPEN_Pos))
#define SAIC_AIC_WPMR_WPKEY_Pos               _U_(8)                                               /**< (SAIC_AIC_WPMR) Write Protection Key Position */
#define SAIC_AIC_WPMR_WPKEY_Msk               (_U_(0xFFFFFF) << SAIC_AIC_WPMR_WPKEY_Pos)           /**< (SAIC_AIC_WPMR) Write Protection Key Mask */
#define SAIC_AIC_WPMR_WPKEY(value)            (SAIC_AIC_WPMR_WPKEY_Msk & ((value) << SAIC_AIC_WPMR_WPKEY_Pos))
#define   SAIC_AIC_WPMR_WPKEY_PASSWD_Val      _U_(0x414943)                                        /**< (SAIC_AIC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0.  */
#define SAIC_AIC_WPMR_WPKEY_PASSWD            (SAIC_AIC_WPMR_WPKEY_PASSWD_Val << SAIC_AIC_WPMR_WPKEY_Pos) /**< (SAIC_AIC_WPMR) Writing any other value in this field aborts the write operation of the WPEN bit.Always reads as 0. Position  */
#define SAIC_AIC_WPMR_Msk                     _U_(0xFFFFFF01)                                      /**< (SAIC_AIC_WPMR) Register Mask  */


/* -------- SAIC_AIC_WPSR : (SAIC Offset: 0xE8) ( R/ 32) Write Protection Status Register -------- */
#define SAIC_AIC_WPSR_WPVS_Pos                _U_(0)                                               /**< (SAIC_AIC_WPSR) Write Protection Violation Status Position */
#define SAIC_AIC_WPSR_WPVS_Msk                (_U_(0x1) << SAIC_AIC_WPSR_WPVS_Pos)                 /**< (SAIC_AIC_WPSR) Write Protection Violation Status Mask */
#define SAIC_AIC_WPSR_WPVS(value)             (SAIC_AIC_WPSR_WPVS_Msk & ((value) << SAIC_AIC_WPSR_WPVS_Pos))
#define SAIC_AIC_WPSR_WPVSRC_Pos              _U_(8)                                               /**< (SAIC_AIC_WPSR) Write Protection Violation Source Position */
#define SAIC_AIC_WPSR_WPVSRC_Msk              (_U_(0xFFFF) << SAIC_AIC_WPSR_WPVSRC_Pos)            /**< (SAIC_AIC_WPSR) Write Protection Violation Source Mask */
#define SAIC_AIC_WPSR_WPVSRC(value)           (SAIC_AIC_WPSR_WPVSRC_Msk & ((value) << SAIC_AIC_WPSR_WPVSRC_Pos))
#define SAIC_AIC_WPSR_Msk                     _U_(0x00FFFF01)                                      /**< (SAIC_AIC_WPSR) Register Mask  */


/* -------- SAIC_AIC_VERSION : (SAIC Offset: 0xFC) ( R/ 32) AIC Version Register -------- */
#define SAIC_AIC_VERSION_VERSION_Pos          _U_(0)                                               /**< (SAIC_AIC_VERSION) Version of the Hardware Module Position */
#define SAIC_AIC_VERSION_VERSION_Msk          (_U_(0xFFF) << SAIC_AIC_VERSION_VERSION_Pos)         /**< (SAIC_AIC_VERSION) Version of the Hardware Module Mask */
#define SAIC_AIC_VERSION_VERSION(value)       (SAIC_AIC_VERSION_VERSION_Msk & ((value) << SAIC_AIC_VERSION_VERSION_Pos))
#define SAIC_AIC_VERSION_MFN_Pos              _U_(16)                                              /**< (SAIC_AIC_VERSION) Metal Fix Number Position */
#define SAIC_AIC_VERSION_MFN_Msk              (_U_(0x7) << SAIC_AIC_VERSION_MFN_Pos)               /**< (SAIC_AIC_VERSION) Metal Fix Number Mask */
#define SAIC_AIC_VERSION_MFN(value)           (SAIC_AIC_VERSION_MFN_Msk & ((value) << SAIC_AIC_VERSION_MFN_Pos))
#define SAIC_AIC_VERSION_Msk                  _U_(0x00070FFF)                                      /**< (SAIC_AIC_VERSION) Register Mask  */


/** \brief SAIC register offsets definitions */
#define SAIC_AIC_SSR_REG_OFST          (0x00)              /**< (SAIC_AIC_SSR) Source Select Register Offset */
#define SAIC_AIC_SMR_REG_OFST          (0x04)              /**< (SAIC_AIC_SMR) Source Mode Register Offset */
#define SAIC_AIC_SVR_REG_OFST          (0x08)              /**< (SAIC_AIC_SVR) Source Vector Register Offset */
#define SAIC_AIC_IVR_REG_OFST          (0x10)              /**< (SAIC_AIC_IVR) Interrupt Vector Register Offset */
#define SAIC_AIC_FVR_REG_OFST          (0x14)              /**< (SAIC_AIC_FVR) FIQ Vector Register Offset */
#define SAIC_AIC_ISR_REG_OFST          (0x18)              /**< (SAIC_AIC_ISR) Interrupt Status Register Offset */
#define SAIC_AIC_IPR0_REG_OFST         (0x20)              /**< (SAIC_AIC_IPR0) Interrupt Pending Register 0 Offset */
#define SAIC_AIC_IPR1_REG_OFST         (0x24)              /**< (SAIC_AIC_IPR1) Interrupt Pending Register 1 Offset */
#define SAIC_AIC_IPR2_REG_OFST         (0x28)              /**< (SAIC_AIC_IPR2) Interrupt Pending Register 2 Offset */
#define SAIC_AIC_IPR3_REG_OFST         (0x2C)              /**< (SAIC_AIC_IPR3) Interrupt Pending Register 3 Offset */
#define SAIC_AIC_IMR_REG_OFST          (0x30)              /**< (SAIC_AIC_IMR) Interrupt Mask Register Offset */
#define SAIC_AIC_CISR_REG_OFST         (0x34)              /**< (SAIC_AIC_CISR) Core Interrupt Status Register Offset */
#define SAIC_AIC_EOICR_REG_OFST        (0x38)              /**< (SAIC_AIC_EOICR) End of Interrupt Command Register Offset */
#define SAIC_AIC_SPU_REG_OFST          (0x3C)              /**< (SAIC_AIC_SPU) Spurious Interrupt Vector Register Offset */
#define SAIC_AIC_IECR_REG_OFST         (0x40)              /**< (SAIC_AIC_IECR) Interrupt Enable Command Register Offset */
#define SAIC_AIC_IDCR_REG_OFST         (0x44)              /**< (SAIC_AIC_IDCR) Interrupt Disable Command Register Offset */
#define SAIC_AIC_ICCR_REG_OFST         (0x48)              /**< (SAIC_AIC_ICCR) Interrupt Clear Command Register Offset */
#define SAIC_AIC_ISCR_REG_OFST         (0x4C)              /**< (SAIC_AIC_ISCR) Interrupt Set Command Register Offset */
#define SAIC_AIC_DCR_REG_OFST          (0x6C)              /**< (SAIC_AIC_DCR) Debug Control Register Offset */
#define SAIC_AIC_WPMR_REG_OFST         (0xE4)              /**< (SAIC_AIC_WPMR) Write Protection Mode Register Offset */
#define SAIC_AIC_WPSR_REG_OFST         (0xE8)              /**< (SAIC_AIC_WPSR) Write Protection Status Register Offset */
#define SAIC_AIC_VERSION_REG_OFST      (0xFC)              /**< (SAIC_AIC_VERSION) AIC Version Register Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief SAIC register API structure */
typedef struct
{
  __IO  uint32_t                       SAIC_AIC_SSR;       /**< Offset: 0x00 (R/W  32) Source Select Register */
  __IO  uint32_t                       SAIC_AIC_SMR;       /**< Offset: 0x04 (R/W  32) Source Mode Register */
  __IO  uint32_t                       SAIC_AIC_SVR;       /**< Offset: 0x08 (R/W  32) Source Vector Register */
  __I   uint8_t                        Reserved1[0x04];
  __I   uint32_t                       SAIC_AIC_IVR;       /**< Offset: 0x10 (R/   32) Interrupt Vector Register */
  __I   uint32_t                       SAIC_AIC_FVR;       /**< Offset: 0x14 (R/   32) FIQ Vector Register */
  __I   uint32_t                       SAIC_AIC_ISR;       /**< Offset: 0x18 (R/   32) Interrupt Status Register */
  __I   uint8_t                        Reserved2[0x04];
  __I   uint32_t                       SAIC_AIC_IPR0;      /**< Offset: 0x20 (R/   32) Interrupt Pending Register 0 */
  __I   uint32_t                       SAIC_AIC_IPR1;      /**< Offset: 0x24 (R/   32) Interrupt Pending Register 1 */
  __I   uint32_t                       SAIC_AIC_IPR2;      /**< Offset: 0x28 (R/   32) Interrupt Pending Register 2 */
  __I   uint32_t                       SAIC_AIC_IPR3;      /**< Offset: 0x2C (R/   32) Interrupt Pending Register 3 */
  __I   uint32_t                       SAIC_AIC_IMR;       /**< Offset: 0x30 (R/   32) Interrupt Mask Register */
  __I   uint32_t                       SAIC_AIC_CISR;      /**< Offset: 0x34 (R/   32) Core Interrupt Status Register */
  __O   uint32_t                       SAIC_AIC_EOICR;     /**< Offset: 0x38 ( /W  32) End of Interrupt Command Register */
  __IO  uint32_t                       SAIC_AIC_SPU;       /**< Offset: 0x3C (R/W  32) Spurious Interrupt Vector Register */
  __O   uint32_t                       SAIC_AIC_IECR;      /**< Offset: 0x40 ( /W  32) Interrupt Enable Command Register */
  __O   uint32_t                       SAIC_AIC_IDCR;      /**< Offset: 0x44 ( /W  32) Interrupt Disable Command Register */
  __O   uint32_t                       SAIC_AIC_ICCR;      /**< Offset: 0x48 ( /W  32) Interrupt Clear Command Register */
  __O   uint32_t                       SAIC_AIC_ISCR;      /**< Offset: 0x4C ( /W  32) Interrupt Set Command Register */
  __I   uint8_t                        Reserved3[0x1C];
  __IO  uint32_t                       SAIC_AIC_DCR;       /**< Offset: 0x6C (R/W  32) Debug Control Register */
  __I   uint8_t                        Reserved4[0x74];
  __IO  uint32_t                       SAIC_AIC_WPMR;      /**< Offset: 0xE4 (R/W  32) Write Protection Mode Register */
  __I   uint32_t                       SAIC_AIC_WPSR;      /**< Offset: 0xE8 (R/   32) Write Protection Status Register */
  __I   uint8_t                        Reserved5[0x10];
  __I   uint32_t                       SAIC_AIC_VERSION;   /**< Offset: 0xFC (R/   32) AIC Version Register */
} saic_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAMA5D2_SAIC_COMPONENT_H_ */
