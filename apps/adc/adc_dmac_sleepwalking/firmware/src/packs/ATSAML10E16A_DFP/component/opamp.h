/**
 * \brief Component description for OPAMP
 *
 * Copyright (c) 2019 Microchip Technology Inc. and its subsidiaries.
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

/* file generated from device description version 2019-01-31T10:50:35Z */
#ifndef _SAML10_OPAMP_COMPONENT_H_
#define _SAML10_OPAMP_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR OPAMP                                        */
/* ************************************************************************** */

/* -------- OPAMP_CTRLA : (OPAMP Offset: 0x00) (R/W 8) Control A -------- */
#define OPAMP_CTRLA_RESETVALUE                _U_(0x00)                                            /**<  (OPAMP_CTRLA) Control A  Reset Value */

#define OPAMP_CTRLA_SWRST_Pos                 _U_(0)                                               /**< (OPAMP_CTRLA) Software Reset Position */
#define OPAMP_CTRLA_SWRST_Msk                 (_U_(0x1) << OPAMP_CTRLA_SWRST_Pos)                  /**< (OPAMP_CTRLA) Software Reset Mask */
#define OPAMP_CTRLA_SWRST(value)              (OPAMP_CTRLA_SWRST_Msk & ((value) << OPAMP_CTRLA_SWRST_Pos))
#define OPAMP_CTRLA_ENABLE_Pos                _U_(1)                                               /**< (OPAMP_CTRLA) Enable Position */
#define OPAMP_CTRLA_ENABLE_Msk                (_U_(0x1) << OPAMP_CTRLA_ENABLE_Pos)                 /**< (OPAMP_CTRLA) Enable Mask */
#define OPAMP_CTRLA_ENABLE(value)             (OPAMP_CTRLA_ENABLE_Msk & ((value) << OPAMP_CTRLA_ENABLE_Pos))
#define OPAMP_CTRLA_LPMUX_Pos                 _U_(7)                                               /**< (OPAMP_CTRLA) Low-Power Mux Position */
#define OPAMP_CTRLA_LPMUX_Msk                 (_U_(0x1) << OPAMP_CTRLA_LPMUX_Pos)                  /**< (OPAMP_CTRLA) Low-Power Mux Mask */
#define OPAMP_CTRLA_LPMUX(value)              (OPAMP_CTRLA_LPMUX_Msk & ((value) << OPAMP_CTRLA_LPMUX_Pos))
#define OPAMP_CTRLA_Msk                       _U_(0x83)                                            /**< (OPAMP_CTRLA) Register Mask  */


/* -------- OPAMP_STATUS : (OPAMP Offset: 0x02) ( R/ 8) Status -------- */
#define OPAMP_STATUS_RESETVALUE               _U_(0x00)                                            /**<  (OPAMP_STATUS) Status  Reset Value */

#define OPAMP_STATUS_READY0_Pos               _U_(0)                                               /**< (OPAMP_STATUS) OPAMP 0 Ready Position */
#define OPAMP_STATUS_READY0_Msk               (_U_(0x1) << OPAMP_STATUS_READY0_Pos)                /**< (OPAMP_STATUS) OPAMP 0 Ready Mask */
#define OPAMP_STATUS_READY0(value)            (OPAMP_STATUS_READY0_Msk & ((value) << OPAMP_STATUS_READY0_Pos))
#define OPAMP_STATUS_READY1_Pos               _U_(1)                                               /**< (OPAMP_STATUS) OPAMP 1 Ready Position */
#define OPAMP_STATUS_READY1_Msk               (_U_(0x1) << OPAMP_STATUS_READY1_Pos)                /**< (OPAMP_STATUS) OPAMP 1 Ready Mask */
#define OPAMP_STATUS_READY1(value)            (OPAMP_STATUS_READY1_Msk & ((value) << OPAMP_STATUS_READY1_Pos))
#define OPAMP_STATUS_READY2_Pos               _U_(2)                                               /**< (OPAMP_STATUS) OPAMP 2 Ready Position */
#define OPAMP_STATUS_READY2_Msk               (_U_(0x1) << OPAMP_STATUS_READY2_Pos)                /**< (OPAMP_STATUS) OPAMP 2 Ready Mask */
#define OPAMP_STATUS_READY2(value)            (OPAMP_STATUS_READY2_Msk & ((value) << OPAMP_STATUS_READY2_Pos))
#define OPAMP_STATUS_Msk                      _U_(0x07)                                            /**< (OPAMP_STATUS) Register Mask  */

#define OPAMP_STATUS_READY_Pos                _U_(0)                                               /**< (OPAMP_STATUS Position) OPAMP 2 Ready */
#define OPAMP_STATUS_READY_Msk                (_U_(0x7) << OPAMP_STATUS_READY_Pos)                 /**< (OPAMP_STATUS Mask) READY */
#define OPAMP_STATUS_READY(value)             (OPAMP_STATUS_READY_Msk & ((value) << OPAMP_STATUS_READY_Pos)) 

/* -------- OPAMP_OPAMPCTRL : (OPAMP Offset: 0x04) (R/W 32) OPAMP n Control -------- */
#define OPAMP_OPAMPCTRL_RESETVALUE            _U_(0x00)                                            /**<  (OPAMP_OPAMPCTRL) OPAMP n Control  Reset Value */

#define OPAMP_OPAMPCTRL_ENABLE_Pos            _U_(1)                                               /**< (OPAMP_OPAMPCTRL) Operational Amplifier Enable Position */
#define OPAMP_OPAMPCTRL_ENABLE_Msk            (_U_(0x1) << OPAMP_OPAMPCTRL_ENABLE_Pos)             /**< (OPAMP_OPAMPCTRL) Operational Amplifier Enable Mask */
#define OPAMP_OPAMPCTRL_ENABLE(value)         (OPAMP_OPAMPCTRL_ENABLE_Msk & ((value) << OPAMP_OPAMPCTRL_ENABLE_Pos))
#define OPAMP_OPAMPCTRL_ANAOUT_Pos            _U_(2)                                               /**< (OPAMP_OPAMPCTRL) Analog Output Position */
#define OPAMP_OPAMPCTRL_ANAOUT_Msk            (_U_(0x1) << OPAMP_OPAMPCTRL_ANAOUT_Pos)             /**< (OPAMP_OPAMPCTRL) Analog Output Mask */
#define OPAMP_OPAMPCTRL_ANAOUT(value)         (OPAMP_OPAMPCTRL_ANAOUT_Msk & ((value) << OPAMP_OPAMPCTRL_ANAOUT_Pos))
#define OPAMP_OPAMPCTRL_BIAS_Pos              _U_(3)                                               /**< (OPAMP_OPAMPCTRL) Bias Selection Position */
#define OPAMP_OPAMPCTRL_BIAS_Msk              (_U_(0x3) << OPAMP_OPAMPCTRL_BIAS_Pos)               /**< (OPAMP_OPAMPCTRL) Bias Selection Mask */
#define OPAMP_OPAMPCTRL_BIAS(value)           (OPAMP_OPAMPCTRL_BIAS_Msk & ((value) << OPAMP_OPAMPCTRL_BIAS_Pos))
#define OPAMP_OPAMPCTRL_RES2VCC_Pos           _U_(5)                                               /**< (OPAMP_OPAMPCTRL) Resistor ladder To VCC Position */
#define OPAMP_OPAMPCTRL_RES2VCC_Msk           (_U_(0x1) << OPAMP_OPAMPCTRL_RES2VCC_Pos)            /**< (OPAMP_OPAMPCTRL) Resistor ladder To VCC Mask */
#define OPAMP_OPAMPCTRL_RES2VCC(value)        (OPAMP_OPAMPCTRL_RES2VCC_Msk & ((value) << OPAMP_OPAMPCTRL_RES2VCC_Pos))
#define OPAMP_OPAMPCTRL_RUNSTDBY_Pos          _U_(6)                                               /**< (OPAMP_OPAMPCTRL) Run in Standby Position */
#define OPAMP_OPAMPCTRL_RUNSTDBY_Msk          (_U_(0x1) << OPAMP_OPAMPCTRL_RUNSTDBY_Pos)           /**< (OPAMP_OPAMPCTRL) Run in Standby Mask */
#define OPAMP_OPAMPCTRL_RUNSTDBY(value)       (OPAMP_OPAMPCTRL_RUNSTDBY_Msk & ((value) << OPAMP_OPAMPCTRL_RUNSTDBY_Pos))
#define OPAMP_OPAMPCTRL_ONDEMAND_Pos          _U_(7)                                               /**< (OPAMP_OPAMPCTRL) On Demand Control Position */
#define OPAMP_OPAMPCTRL_ONDEMAND_Msk          (_U_(0x1) << OPAMP_OPAMPCTRL_ONDEMAND_Pos)           /**< (OPAMP_OPAMPCTRL) On Demand Control Mask */
#define OPAMP_OPAMPCTRL_ONDEMAND(value)       (OPAMP_OPAMPCTRL_ONDEMAND_Msk & ((value) << OPAMP_OPAMPCTRL_ONDEMAND_Pos))
#define OPAMP_OPAMPCTRL_RES2OUT_Pos           _U_(8)                                               /**< (OPAMP_OPAMPCTRL) Resistor ladder To Output Position */
#define OPAMP_OPAMPCTRL_RES2OUT_Msk           (_U_(0x1) << OPAMP_OPAMPCTRL_RES2OUT_Pos)            /**< (OPAMP_OPAMPCTRL) Resistor ladder To Output Mask */
#define OPAMP_OPAMPCTRL_RES2OUT(value)        (OPAMP_OPAMPCTRL_RES2OUT_Msk & ((value) << OPAMP_OPAMPCTRL_RES2OUT_Pos))
#define OPAMP_OPAMPCTRL_RES1EN_Pos            _U_(9)                                               /**< (OPAMP_OPAMPCTRL) Resistor 1 Enable Position */
#define OPAMP_OPAMPCTRL_RES1EN_Msk            (_U_(0x1) << OPAMP_OPAMPCTRL_RES1EN_Pos)             /**< (OPAMP_OPAMPCTRL) Resistor 1 Enable Mask */
#define OPAMP_OPAMPCTRL_RES1EN(value)         (OPAMP_OPAMPCTRL_RES1EN_Msk & ((value) << OPAMP_OPAMPCTRL_RES1EN_Pos))
#define OPAMP_OPAMPCTRL_RES1MUX_Pos           _U_(10)                                              /**< (OPAMP_OPAMPCTRL) Resistor 1 Mux Position */
#define OPAMP_OPAMPCTRL_RES1MUX_Msk           (_U_(0x7) << OPAMP_OPAMPCTRL_RES1MUX_Pos)            /**< (OPAMP_OPAMPCTRL) Resistor 1 Mux Mask */
#define OPAMP_OPAMPCTRL_RES1MUX(value)        (OPAMP_OPAMPCTRL_RES1MUX_Msk & ((value) << OPAMP_OPAMPCTRL_RES1MUX_Pos))
#define OPAMP_OPAMPCTRL_POTMUX_Pos            _U_(13)                                              /**< (OPAMP_OPAMPCTRL) Potentiometer Selection Position */
#define OPAMP_OPAMPCTRL_POTMUX_Msk            (_U_(0x7) << OPAMP_OPAMPCTRL_POTMUX_Pos)             /**< (OPAMP_OPAMPCTRL) Potentiometer Selection Mask */
#define OPAMP_OPAMPCTRL_POTMUX(value)         (OPAMP_OPAMPCTRL_POTMUX_Msk & ((value) << OPAMP_OPAMPCTRL_POTMUX_Pos))
#define OPAMP_OPAMPCTRL_MUXPOS_Pos            _U_(16)                                              /**< (OPAMP_OPAMPCTRL) Positive Input Mux Selection Position */
#define OPAMP_OPAMPCTRL_MUXPOS_Msk            (_U_(0xF) << OPAMP_OPAMPCTRL_MUXPOS_Pos)             /**< (OPAMP_OPAMPCTRL) Positive Input Mux Selection Mask */
#define OPAMP_OPAMPCTRL_MUXPOS(value)         (OPAMP_OPAMPCTRL_MUXPOS_Msk & ((value) << OPAMP_OPAMPCTRL_MUXPOS_Pos))
#define OPAMP_OPAMPCTRL_MUXNEG_Pos            _U_(20)                                              /**< (OPAMP_OPAMPCTRL) Negative Input Mux Selection Position */
#define OPAMP_OPAMPCTRL_MUXNEG_Msk            (_U_(0xF) << OPAMP_OPAMPCTRL_MUXNEG_Pos)             /**< (OPAMP_OPAMPCTRL) Negative Input Mux Selection Mask */
#define OPAMP_OPAMPCTRL_MUXNEG(value)         (OPAMP_OPAMPCTRL_MUXNEG_Msk & ((value) << OPAMP_OPAMPCTRL_MUXNEG_Pos))
#define OPAMP_OPAMPCTRL_Msk                   _U_(0x00FFFFFE)                                      /**< (OPAMP_OPAMPCTRL) Register Mask  */


/* -------- OPAMP_RESCTRL : (OPAMP Offset: 0x10) (R/W 8) Resister Control -------- */
#define OPAMP_RESCTRL_RESETVALUE              _U_(0x00)                                            /**<  (OPAMP_RESCTRL) Resister Control  Reset Value */

#define OPAMP_RESCTRL_RES2OUT_Pos             _U_(0)                                               /**< (OPAMP_RESCTRL) Resistor ladder To Output Position */
#define OPAMP_RESCTRL_RES2OUT_Msk             (_U_(0x1) << OPAMP_RESCTRL_RES2OUT_Pos)              /**< (OPAMP_RESCTRL) Resistor ladder To Output Mask */
#define OPAMP_RESCTRL_RES2OUT(value)          (OPAMP_RESCTRL_RES2OUT_Msk & ((value) << OPAMP_RESCTRL_RES2OUT_Pos))
#define OPAMP_RESCTRL_RES1EN_Pos              _U_(1)                                               /**< (OPAMP_RESCTRL) Resistor 1 Enable Position */
#define OPAMP_RESCTRL_RES1EN_Msk              (_U_(0x1) << OPAMP_RESCTRL_RES1EN_Pos)               /**< (OPAMP_RESCTRL) Resistor 1 Enable Mask */
#define OPAMP_RESCTRL_RES1EN(value)           (OPAMP_RESCTRL_RES1EN_Msk & ((value) << OPAMP_RESCTRL_RES1EN_Pos))
#define OPAMP_RESCTRL_RES1MUX_Pos             _U_(2)                                               /**< (OPAMP_RESCTRL) Resistor 1 Mux Position */
#define OPAMP_RESCTRL_RES1MUX_Msk             (_U_(0x1) << OPAMP_RESCTRL_RES1MUX_Pos)              /**< (OPAMP_RESCTRL) Resistor 1 Mux Mask */
#define OPAMP_RESCTRL_RES1MUX(value)          (OPAMP_RESCTRL_RES1MUX_Msk & ((value) << OPAMP_RESCTRL_RES1MUX_Pos))
#define OPAMP_RESCTRL_POTMUX_Pos              _U_(3)                                               /**< (OPAMP_RESCTRL) Potentiometer Selection Position */
#define OPAMP_RESCTRL_POTMUX_Msk              (_U_(0x7) << OPAMP_RESCTRL_POTMUX_Pos)               /**< (OPAMP_RESCTRL) Potentiometer Selection Mask */
#define OPAMP_RESCTRL_POTMUX(value)           (OPAMP_RESCTRL_POTMUX_Msk & ((value) << OPAMP_RESCTRL_POTMUX_Pos))
#define OPAMP_RESCTRL_REFBUFLEVEL_Pos         _U_(6)                                               /**< (OPAMP_RESCTRL) Reference output voltage level select Position */
#define OPAMP_RESCTRL_REFBUFLEVEL_Msk         (_U_(0x3) << OPAMP_RESCTRL_REFBUFLEVEL_Pos)          /**< (OPAMP_RESCTRL) Reference output voltage level select Mask */
#define OPAMP_RESCTRL_REFBUFLEVEL(value)      (OPAMP_RESCTRL_REFBUFLEVEL_Msk & ((value) << OPAMP_RESCTRL_REFBUFLEVEL_Pos))
#define OPAMP_RESCTRL_Msk                     _U_(0xFF)                                            /**< (OPAMP_RESCTRL) Register Mask  */


/** \brief OPAMP register offsets definitions */
#define OPAMP_CTRLA_REG_OFST           (0x00)              /**< (OPAMP_CTRLA) Control A Offset */
#define OPAMP_STATUS_REG_OFST          (0x02)              /**< (OPAMP_STATUS) Status Offset */
#define OPAMP_OPAMPCTRL_REG_OFST       (0x04)              /**< (OPAMP_OPAMPCTRL) OPAMP n Control Offset */
#define OPAMP_RESCTRL_REG_OFST         (0x10)              /**< (OPAMP_RESCTRL) Resister Control Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief OPAMP register API structure */
typedef struct
{  /* Operational Amplifier */
  __IO  uint8_t                        OPAMP_CTRLA;        /**< Offset: 0x00 (R/W  8) Control A */
  __I   uint8_t                        Reserved1[0x01];
  __I   uint8_t                        OPAMP_STATUS;       /**< Offset: 0x02 (R/   8) Status */
  __I   uint8_t                        Reserved2[0x01];
  __IO  uint32_t                       OPAMP_OPAMPCTRL[3]; /**< Offset: 0x04 (R/W  32) OPAMP n Control */
  __IO  uint8_t                        OPAMP_RESCTRL;      /**< Offset: 0x10 (R/W  8) Resister Control */
} opamp_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAML10_OPAMP_COMPONENT_H_ */
