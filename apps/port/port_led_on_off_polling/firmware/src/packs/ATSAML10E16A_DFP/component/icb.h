/**
 * \brief Component description for ICB
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
#ifndef _SAML10_ICB_COMPONENT_H_
#define _SAML10_ICB_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR ICB                                          */
/* ************************************************************************** */

/* -------- ICB_ICTR : (ICB Offset: 0x04) ( R/ 32) Interrupt Controller Type Register -------- */
#define ICB_ICTR_INTLINESNUM_Pos              _U_(0)                                         /**< (ICB_ICTR) Interrupt line set number Position */
#define ICB_ICTR_INTLINESNUM_Msk              (_U_(0xF) << ICB_ICTR_INTLINESNUM_Pos)         /**< (ICB_ICTR) Interrupt line set number Mask */
#define ICB_ICTR_INTLINESNUM(value)           (ICB_ICTR_INTLINESNUM_Msk & ((value) << ICB_ICTR_INTLINESNUM_Pos))
#define ICB_ICTR_Msk                          _U_(0x0000000F)                                /**< (ICB_ICTR) Register Mask  */


/* -------- ICB_ACTLR : (ICB Offset: 0x08) (R/W 32) Auxiliary Control Register -------- */
#define ICB_ACTLR_Msk                         _U_(0x00000000)                                /**< (ICB_ACTLR) Register Mask  */


/** \brief ICB register offsets definitions */
#define ICB_ICTR_REG_OFST              (0x04)         /**< (ICB_ICTR) Interrupt Controller Type Register Offset */
#define ICB_ACTLR_REG_OFST             (0x08)         /**< (ICB_ACTLR) Auxiliary Control Register Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief ICB register API structure */
typedef struct
{  /* Implementation Control Block */
  __I   uint8_t                        Reserved1[0x04];
  __I   uint32_t                       ICB_ICTR;        /**< Offset: 0x04 (R/   32) Interrupt Controller Type Register */
  __IO  uint32_t                       ICB_ACTLR;       /**< Offset: 0x08 (R/W  32) Auxiliary Control Register */
} icb_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAML10_ICB_COMPONENT_H_ */
