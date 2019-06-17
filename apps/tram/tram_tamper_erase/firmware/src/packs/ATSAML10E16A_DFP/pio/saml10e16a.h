/**
 * \brief Peripheral I/O description for SAML10E16A
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

/* file generated from device description version 2019-06-07T05:54:14Z */
#ifndef _SAML10E16A_GPIO_H_
#define _SAML10E16A_GPIO_H_

/* ========== Peripheral I/O pin numbers ========== */
#define PIN_PA00                    (  0  )  /**< Pin Number for PA00 */
#define PIN_PA01                    (  1  )  /**< Pin Number for PA01 */
#define PIN_PA02                    (  2  )  /**< Pin Number for PA02 */
#define PIN_PA03                    (  3  )  /**< Pin Number for PA03 */
#define PIN_PA04                    (  4  )  /**< Pin Number for PA04 */
#define PIN_PA05                    (  5  )  /**< Pin Number for PA05 */
#define PIN_PA06                    (  6  )  /**< Pin Number for PA06 */
#define PIN_PA07                    (  7  )  /**< Pin Number for PA07 */
#define PIN_PA08                    (  8  )  /**< Pin Number for PA08 */
#define PIN_PA09                    (  9  )  /**< Pin Number for PA09 */
#define PIN_PA10                    ( 10  )  /**< Pin Number for PA10 */
#define PIN_PA11                    ( 11  )  /**< Pin Number for PA11 */
#define PIN_PA14                    ( 14  )  /**< Pin Number for PA14 */
#define PIN_PA15                    ( 15  )  /**< Pin Number for PA15 */
#define PIN_PA16                    ( 16  )  /**< Pin Number for PA16 */
#define PIN_PA17                    ( 17  )  /**< Pin Number for PA17 */
#define PIN_PA18                    ( 18  )  /**< Pin Number for PA18 */
#define PIN_PA19                    ( 19  )  /**< Pin Number for PA19 */
#define PIN_PA22                    ( 22  )  /**< Pin Number for PA22 */
#define PIN_PA23                    ( 23  )  /**< Pin Number for PA23 */
#define PIN_PA24                    ( 24  )  /**< Pin Number for PA24 */
#define PIN_PA25                    ( 25  )  /**< Pin Number for PA25 */
#define PIN_PA27                    ( 27  )  /**< Pin Number for PA27 */
#define PIN_PA30                    ( 30  )  /**< Pin Number for PA30 */
#define PIN_PA31                    ( 31  )  /**< Pin Number for PA31 */

/* ========== Peripheral I/O masks ========== */
#define PORT_PA00                   _UL_(1 << 0)    /**< PORT mask for PA00 */
#define PORT_PA01                   _UL_(1 << 1)    /**< PORT mask for PA01 */
#define PORT_PA02                   _UL_(1 << 2)    /**< PORT mask for PA02 */
#define PORT_PA03                   _UL_(1 << 3)    /**< PORT mask for PA03 */
#define PORT_PA04                   _UL_(1 << 4)    /**< PORT mask for PA04 */
#define PORT_PA05                   _UL_(1 << 5)    /**< PORT mask for PA05 */
#define PORT_PA06                   _UL_(1 << 6)    /**< PORT mask for PA06 */
#define PORT_PA07                   _UL_(1 << 7)    /**< PORT mask for PA07 */
#define PORT_PA08                   _UL_(1 << 8)    /**< PORT mask for PA08 */
#define PORT_PA09                   _UL_(1 << 9)    /**< PORT mask for PA09 */
#define PORT_PA10                   _UL_(1 << 10)   /**< PORT mask for PA10 */
#define PORT_PA11                   _UL_(1 << 11)   /**< PORT mask for PA11 */
#define PORT_PA14                   _UL_(1 << 14)   /**< PORT mask for PA14 */
#define PORT_PA15                   _UL_(1 << 15)   /**< PORT mask for PA15 */
#define PORT_PA16                   _UL_(1 << 16)   /**< PORT mask for PA16 */
#define PORT_PA17                   _UL_(1 << 17)   /**< PORT mask for PA17 */
#define PORT_PA18                   _UL_(1 << 18)   /**< PORT mask for PA18 */
#define PORT_PA19                   _UL_(1 << 19)   /**< PORT mask for PA19 */
#define PORT_PA22                   _UL_(1 << 22)   /**< PORT mask for PA22 */
#define PORT_PA23                   _UL_(1 << 23)   /**< PORT mask for PA23 */
#define PORT_PA24                   _UL_(1 << 24)   /**< PORT mask for PA24 */
#define PORT_PA25                   _UL_(1 << 25)   /**< PORT mask for PA25 */
#define PORT_PA27                   _UL_(1 << 27)   /**< PORT mask for PA27 */
#define PORT_PA30                   _UL_(1 << 30)   /**< PORT mask for PA30 */
#define PORT_PA31                   _UL_(1 << 31)   /**< PORT mask for PA31 */

/* ========== PORT definition for AC peripheral ========== */
#define PIN_PA04B_AC_AIN0                          (4L)         
#define MUX_PA04B_AC_AIN0                          (1L)        
#define PINMUX_PA04B_AC_AIN0                       ((PIN_PA04B_AC_AIN0 << 16) | MUX_PA04B_AC_AIN0)
#define PORT_PA04B_AC_AIN0                         ((1UL) << 4)

#define PIN_PA05B_AC_AIN1                          (5L)         
#define MUX_PA05B_AC_AIN1                          (1L)        
#define PINMUX_PA05B_AC_AIN1                       ((PIN_PA05B_AC_AIN1 << 16) | MUX_PA05B_AC_AIN1)
#define PORT_PA05B_AC_AIN1                         ((1UL) << 5)

#define PIN_PA06B_AC_AIN2                          (6L)         
#define MUX_PA06B_AC_AIN2                          (1L)        
#define PINMUX_PA06B_AC_AIN2                       ((PIN_PA06B_AC_AIN2 << 16) | MUX_PA06B_AC_AIN2)
#define PORT_PA06B_AC_AIN2                         ((1UL) << 6)

#define PIN_PA07B_AC_AIN3                          (7L)         
#define MUX_PA07B_AC_AIN3                          (1L)        
#define PINMUX_PA07B_AC_AIN3                       ((PIN_PA07B_AC_AIN3 << 16) | MUX_PA07B_AC_AIN3)
#define PORT_PA07B_AC_AIN3                         ((1UL) << 7)

#define PIN_PA18H_AC_CMP0                          (18L)        
#define MUX_PA18H_AC_CMP0                          (7L)        
#define PINMUX_PA18H_AC_CMP0                       ((PIN_PA18H_AC_CMP0 << 16) | MUX_PA18H_AC_CMP0)
#define PORT_PA18H_AC_CMP0                         ((1UL) << 18)

#define PIN_PA19H_AC_CMP1                          (19L)        
#define MUX_PA19H_AC_CMP1                          (7L)        
#define PINMUX_PA19H_AC_CMP1                       ((PIN_PA19H_AC_CMP1 << 16) | MUX_PA19H_AC_CMP1)
#define PORT_PA19H_AC_CMP1                         ((1UL) << 19)

/* ========== PORT definition for ADC peripheral ========== */
#define PIN_PA02B_ADC_AIN0                         (2L)         
#define MUX_PA02B_ADC_AIN0                         (1L)        
#define PINMUX_PA02B_ADC_AIN0                      ((PIN_PA02B_ADC_AIN0 << 16) | MUX_PA02B_ADC_AIN0)
#define PORT_PA02B_ADC_AIN0                        ((1UL) << 2)

#define PIN_PA03B_ADC_AIN1                         (3L)         
#define MUX_PA03B_ADC_AIN1                         (1L)        
#define PINMUX_PA03B_ADC_AIN1                      ((PIN_PA03B_ADC_AIN1 << 16) | MUX_PA03B_ADC_AIN1)
#define PORT_PA03B_ADC_AIN1                        ((1UL) << 3)

#define PIN_PA04B_ADC_AIN2                         (4L)         
#define MUX_PA04B_ADC_AIN2                         (1L)        
#define PINMUX_PA04B_ADC_AIN2                      ((PIN_PA04B_ADC_AIN2 << 16) | MUX_PA04B_ADC_AIN2)
#define PORT_PA04B_ADC_AIN2                        ((1UL) << 4)

#define PIN_PA05B_ADC_AIN3                         (5L)         
#define MUX_PA05B_ADC_AIN3                         (1L)        
#define PINMUX_PA05B_ADC_AIN3                      ((PIN_PA05B_ADC_AIN3 << 16) | MUX_PA05B_ADC_AIN3)
#define PORT_PA05B_ADC_AIN3                        ((1UL) << 5)

#define PIN_PA06B_ADC_AIN4                         (6L)         
#define MUX_PA06B_ADC_AIN4                         (1L)        
#define PINMUX_PA06B_ADC_AIN4                      ((PIN_PA06B_ADC_AIN4 << 16) | MUX_PA06B_ADC_AIN4)
#define PORT_PA06B_ADC_AIN4                        ((1UL) << 6)

#define PIN_PA07B_ADC_AIN5                         (7L)         
#define MUX_PA07B_ADC_AIN5                         (1L)        
#define PINMUX_PA07B_ADC_AIN5                      ((PIN_PA07B_ADC_AIN5 << 16) | MUX_PA07B_ADC_AIN5)
#define PORT_PA07B_ADC_AIN5                        ((1UL) << 7)

#define PIN_PA08B_ADC_AIN6                         (8L)         
#define MUX_PA08B_ADC_AIN6                         (1L)        
#define PINMUX_PA08B_ADC_AIN6                      ((PIN_PA08B_ADC_AIN6 << 16) | MUX_PA08B_ADC_AIN6)
#define PORT_PA08B_ADC_AIN6                        ((1UL) << 8)

#define PIN_PA09B_ADC_AIN7                         (9L)         
#define MUX_PA09B_ADC_AIN7                         (1L)        
#define PINMUX_PA09B_ADC_AIN7                      ((PIN_PA09B_ADC_AIN7 << 16) | MUX_PA09B_ADC_AIN7)
#define PORT_PA09B_ADC_AIN7                        ((1UL) << 9)

#define PIN_PA10B_ADC_AIN8                         (10L)        
#define MUX_PA10B_ADC_AIN8                         (1L)        
#define PINMUX_PA10B_ADC_AIN8                      ((PIN_PA10B_ADC_AIN8 << 16) | MUX_PA10B_ADC_AIN8)
#define PORT_PA10B_ADC_AIN8                        ((1UL) << 10)

#define PIN_PA11B_ADC_AIN9                         (11L)        
#define MUX_PA11B_ADC_AIN9                         (1L)        
#define PINMUX_PA11B_ADC_AIN9                      ((PIN_PA11B_ADC_AIN9 << 16) | MUX_PA11B_ADC_AIN9)
#define PORT_PA11B_ADC_AIN9                        ((1UL) << 11)

#define PIN_PA04B_ADC_VREFP                        (4L)         
#define MUX_PA04B_ADC_VREFP                        (1L)        
#define PINMUX_PA04B_ADC_VREFP                     ((PIN_PA04B_ADC_VREFP << 16) | MUX_PA04B_ADC_VREFP)
#define PORT_PA04B_ADC_VREFP                       ((1UL) << 4)

/* ========== PORT definition for CCL peripheral ========== */
#define PIN_PA04I_CCL_IN0                          (4L)         
#define MUX_PA04I_CCL_IN0                          (8L)        
#define PINMUX_PA04I_CCL_IN0                       ((PIN_PA04I_CCL_IN0 << 16) | MUX_PA04I_CCL_IN0)
#define PORT_PA04I_CCL_IN0                         ((1UL) << 4)

#define PIN_PA16I_CCL_IN0                          (16L)        
#define MUX_PA16I_CCL_IN0                          (8L)        
#define PINMUX_PA16I_CCL_IN0                       ((PIN_PA16I_CCL_IN0 << 16) | MUX_PA16I_CCL_IN0)
#define PORT_PA16I_CCL_IN0                         ((1UL) << 16)

#define PIN_PA05I_CCL_IN1                          (5L)         
#define MUX_PA05I_CCL_IN1                          (8L)        
#define PINMUX_PA05I_CCL_IN1                       ((PIN_PA05I_CCL_IN1 << 16) | MUX_PA05I_CCL_IN1)
#define PORT_PA05I_CCL_IN1                         ((1UL) << 5)

#define PIN_PA17I_CCL_IN1                          (17L)        
#define MUX_PA17I_CCL_IN1                          (8L)        
#define PINMUX_PA17I_CCL_IN1                       ((PIN_PA17I_CCL_IN1 << 16) | MUX_PA17I_CCL_IN1)
#define PORT_PA17I_CCL_IN1                         ((1UL) << 17)

#define PIN_PA06I_CCL_IN2                          (6L)         
#define MUX_PA06I_CCL_IN2                          (8L)        
#define PINMUX_PA06I_CCL_IN2                       ((PIN_PA06I_CCL_IN2 << 16) | MUX_PA06I_CCL_IN2)
#define PORT_PA06I_CCL_IN2                         ((1UL) << 6)

#define PIN_PA18I_CCL_IN2                          (18L)        
#define MUX_PA18I_CCL_IN2                          (8L)        
#define PINMUX_PA18I_CCL_IN2                       ((PIN_PA18I_CCL_IN2 << 16) | MUX_PA18I_CCL_IN2)
#define PORT_PA18I_CCL_IN2                         ((1UL) << 18)

#define PIN_PA08I_CCL_IN3                          (8L)         
#define MUX_PA08I_CCL_IN3                          (8L)        
#define PINMUX_PA08I_CCL_IN3                       ((PIN_PA08I_CCL_IN3 << 16) | MUX_PA08I_CCL_IN3)
#define PORT_PA08I_CCL_IN3                         ((1UL) << 8)

#define PIN_PA30I_CCL_IN3                          (30L)        
#define MUX_PA30I_CCL_IN3                          (8L)        
#define PINMUX_PA30I_CCL_IN3                       ((PIN_PA30I_CCL_IN3 << 16) | MUX_PA30I_CCL_IN3)
#define PORT_PA30I_CCL_IN3                         ((1UL) << 30)

#define PIN_PA09I_CCL_IN4                          (9L)         
#define MUX_PA09I_CCL_IN4                          (8L)        
#define PINMUX_PA09I_CCL_IN4                       ((PIN_PA09I_CCL_IN4 << 16) | MUX_PA09I_CCL_IN4)
#define PORT_PA09I_CCL_IN4                         ((1UL) << 9)

#define PIN_PA10I_CCL_IN5                          (10L)        
#define MUX_PA10I_CCL_IN5                          (8L)        
#define PINMUX_PA10I_CCL_IN5                       ((PIN_PA10I_CCL_IN5 << 16) | MUX_PA10I_CCL_IN5)
#define PORT_PA10I_CCL_IN5                         ((1UL) << 10)

#define PIN_PA07I_CCL_OUT0                         (7L)         
#define MUX_PA07I_CCL_OUT0                         (8L)        
#define PINMUX_PA07I_CCL_OUT0                      ((PIN_PA07I_CCL_OUT0 << 16) | MUX_PA07I_CCL_OUT0)
#define PORT_PA07I_CCL_OUT0                        ((1UL) << 7)

#define PIN_PA19I_CCL_OUT0                         (19L)        
#define MUX_PA19I_CCL_OUT0                         (8L)        
#define PINMUX_PA19I_CCL_OUT0                      ((PIN_PA19I_CCL_OUT0 << 16) | MUX_PA19I_CCL_OUT0)
#define PORT_PA19I_CCL_OUT0                        ((1UL) << 19)

#define PIN_PA11I_CCL_OUT1                         (11L)        
#define MUX_PA11I_CCL_OUT1                         (8L)        
#define PINMUX_PA11I_CCL_OUT1                      ((PIN_PA11I_CCL_OUT1 << 16) | MUX_PA11I_CCL_OUT1)
#define PORT_PA11I_CCL_OUT1                        ((1UL) << 11)

#define PIN_PA31I_CCL_OUT1                         (31L)        
#define MUX_PA31I_CCL_OUT1                         (8L)        
#define PINMUX_PA31I_CCL_OUT1                      ((PIN_PA31I_CCL_OUT1 << 16) | MUX_PA31I_CCL_OUT1)
#define PORT_PA31I_CCL_OUT1                        ((1UL) << 31)

/* ========== PORT definition for DAC peripheral ========== */
#define PIN_PA02B_DAC_VOUT                         (2L)         
#define MUX_PA02B_DAC_VOUT                         (1L)        
#define PINMUX_PA02B_DAC_VOUT                      ((PIN_PA02B_DAC_VOUT << 16) | MUX_PA02B_DAC_VOUT)
#define PORT_PA02B_DAC_VOUT                        ((1UL) << 2)

#define PIN_PA03B_DAC_VREFP                        (3L)         
#define MUX_PA03B_DAC_VREFP                        (1L)        
#define PINMUX_PA03B_DAC_VREFP                     ((PIN_PA03B_DAC_VREFP << 16) | MUX_PA03B_DAC_VREFP)
#define PORT_PA03B_DAC_VREFP                       ((1UL) << 3)

/* ========== PORT definition for EIC peripheral ========== */
#define PIN_PA09A_EIC_EXTINT0                      (9L)         
#define MUX_PA09A_EIC_EXTINT0                      (0L)        
#define PINMUX_PA09A_EIC_EXTINT0                   ((PIN_PA09A_EIC_EXTINT0 << 16) | MUX_PA09A_EIC_EXTINT0)
#define PORT_PA09A_EIC_EXTINT0                     ((1UL) << 9)
#define PIN_PA09A_EIC_EXTINT_NUM                   _L_(0)       /**< EIC signal: PIN_PA09 External Interrupt Line */

#define PIN_PA19A_EIC_EXTINT0                      (19L)        
#define MUX_PA19A_EIC_EXTINT0                      (0L)        
#define PINMUX_PA19A_EIC_EXTINT0                   ((PIN_PA19A_EIC_EXTINT0 << 16) | MUX_PA19A_EIC_EXTINT0)
#define PORT_PA19A_EIC_EXTINT0                     ((1UL) << 19)
#define PIN_PA19A_EIC_EXTINT_NUM                   _L_(0)       /**< EIC signal: PIN_PA19 External Interrupt Line */

#define PIN_PA00A_EIC_EXTINT0                      (0L)         
#define MUX_PA00A_EIC_EXTINT0                      (0L)        
#define PINMUX_PA00A_EIC_EXTINT0                   ((PIN_PA00A_EIC_EXTINT0 << 16) | MUX_PA00A_EIC_EXTINT0)
#define PORT_PA00A_EIC_EXTINT0                     ((1UL) << 0)
#define PIN_PA00A_EIC_EXTINT_NUM                   _L_(0)       /**< EIC signal: PIN_PA00 External Interrupt Line */

#define PIN_PA10A_EIC_EXTINT1                      (10L)        
#define MUX_PA10A_EIC_EXTINT1                      (0L)        
#define PINMUX_PA10A_EIC_EXTINT1                   ((PIN_PA10A_EIC_EXTINT1 << 16) | MUX_PA10A_EIC_EXTINT1)
#define PORT_PA10A_EIC_EXTINT1                     ((1UL) << 10)
#define PIN_PA10A_EIC_EXTINT_NUM                   _L_(1)       /**< EIC signal: PIN_PA10 External Interrupt Line */

#define PIN_PA22A_EIC_EXTINT1                      (22L)        
#define MUX_PA22A_EIC_EXTINT1                      (0L)        
#define PINMUX_PA22A_EIC_EXTINT1                   ((PIN_PA22A_EIC_EXTINT1 << 16) | MUX_PA22A_EIC_EXTINT1)
#define PORT_PA22A_EIC_EXTINT1                     ((1UL) << 22)
#define PIN_PA22A_EIC_EXTINT_NUM                   _L_(1)       /**< EIC signal: PIN_PA22 External Interrupt Line */

#define PIN_PA01A_EIC_EXTINT1                      (1L)         
#define MUX_PA01A_EIC_EXTINT1                      (0L)        
#define PINMUX_PA01A_EIC_EXTINT1                   ((PIN_PA01A_EIC_EXTINT1 << 16) | MUX_PA01A_EIC_EXTINT1)
#define PORT_PA01A_EIC_EXTINT1                     ((1UL) << 1)
#define PIN_PA01A_EIC_EXTINT_NUM                   _L_(1)       /**< EIC signal: PIN_PA01 External Interrupt Line */

#define PIN_PA02A_EIC_EXTINT2                      (2L)         
#define MUX_PA02A_EIC_EXTINT2                      (0L)        
#define PINMUX_PA02A_EIC_EXTINT2                   ((PIN_PA02A_EIC_EXTINT2 << 16) | MUX_PA02A_EIC_EXTINT2)
#define PORT_PA02A_EIC_EXTINT2                     ((1UL) << 2)
#define PIN_PA02A_EIC_EXTINT_NUM                   _L_(2)       /**< EIC signal: PIN_PA02 External Interrupt Line */

#define PIN_PA11A_EIC_EXTINT2                      (11L)        
#define MUX_PA11A_EIC_EXTINT2                      (0L)        
#define PINMUX_PA11A_EIC_EXTINT2                   ((PIN_PA11A_EIC_EXTINT2 << 16) | MUX_PA11A_EIC_EXTINT2)
#define PORT_PA11A_EIC_EXTINT2                     ((1UL) << 11)
#define PIN_PA11A_EIC_EXTINT_NUM                   _L_(2)       /**< EIC signal: PIN_PA11 External Interrupt Line */

#define PIN_PA23A_EIC_EXTINT2                      (23L)        
#define MUX_PA23A_EIC_EXTINT2                      (0L)        
#define PINMUX_PA23A_EIC_EXTINT2                   ((PIN_PA23A_EIC_EXTINT2 << 16) | MUX_PA23A_EIC_EXTINT2)
#define PORT_PA23A_EIC_EXTINT2                     ((1UL) << 23)
#define PIN_PA23A_EIC_EXTINT_NUM                   _L_(2)       /**< EIC signal: PIN_PA23 External Interrupt Line */

#define PIN_PA03A_EIC_EXTINT3                      (3L)         
#define MUX_PA03A_EIC_EXTINT3                      (0L)        
#define PINMUX_PA03A_EIC_EXTINT3                   ((PIN_PA03A_EIC_EXTINT3 << 16) | MUX_PA03A_EIC_EXTINT3)
#define PORT_PA03A_EIC_EXTINT3                     ((1UL) << 3)
#define PIN_PA03A_EIC_EXTINT_NUM                   _L_(3)       /**< EIC signal: PIN_PA03 External Interrupt Line */

#define PIN_PA14A_EIC_EXTINT3                      (14L)        
#define MUX_PA14A_EIC_EXTINT3                      (0L)        
#define PINMUX_PA14A_EIC_EXTINT3                   ((PIN_PA14A_EIC_EXTINT3 << 16) | MUX_PA14A_EIC_EXTINT3)
#define PORT_PA14A_EIC_EXTINT3                     ((1UL) << 14)
#define PIN_PA14A_EIC_EXTINT_NUM                   _L_(3)       /**< EIC signal: PIN_PA14 External Interrupt Line */

#define PIN_PA24A_EIC_EXTINT3                      (24L)        
#define MUX_PA24A_EIC_EXTINT3                      (0L)        
#define PINMUX_PA24A_EIC_EXTINT3                   ((PIN_PA24A_EIC_EXTINT3 << 16) | MUX_PA24A_EIC_EXTINT3)
#define PORT_PA24A_EIC_EXTINT3                     ((1UL) << 24)
#define PIN_PA24A_EIC_EXTINT_NUM                   _L_(3)       /**< EIC signal: PIN_PA24 External Interrupt Line */

#define PIN_PA04A_EIC_EXTINT4                      (4L)         
#define MUX_PA04A_EIC_EXTINT4                      (0L)        
#define PINMUX_PA04A_EIC_EXTINT4                   ((PIN_PA04A_EIC_EXTINT4 << 16) | MUX_PA04A_EIC_EXTINT4)
#define PORT_PA04A_EIC_EXTINT4                     ((1UL) << 4)
#define PIN_PA04A_EIC_EXTINT_NUM                   _L_(4)       /**< EIC signal: PIN_PA04 External Interrupt Line */

#define PIN_PA15A_EIC_EXTINT4                      (15L)        
#define MUX_PA15A_EIC_EXTINT4                      (0L)        
#define PINMUX_PA15A_EIC_EXTINT4                   ((PIN_PA15A_EIC_EXTINT4 << 16) | MUX_PA15A_EIC_EXTINT4)
#define PORT_PA15A_EIC_EXTINT4                     ((1UL) << 15)
#define PIN_PA15A_EIC_EXTINT_NUM                   _L_(4)       /**< EIC signal: PIN_PA15 External Interrupt Line */

#define PIN_PA25A_EIC_EXTINT4                      (25L)        
#define MUX_PA25A_EIC_EXTINT4                      (0L)        
#define PINMUX_PA25A_EIC_EXTINT4                   ((PIN_PA25A_EIC_EXTINT4 << 16) | MUX_PA25A_EIC_EXTINT4)
#define PORT_PA25A_EIC_EXTINT4                     ((1UL) << 25)
#define PIN_PA25A_EIC_EXTINT_NUM                   _L_(4)       /**< EIC signal: PIN_PA25 External Interrupt Line */

#define PIN_PA05A_EIC_EXTINT5                      (5L)         
#define MUX_PA05A_EIC_EXTINT5                      (0L)        
#define PINMUX_PA05A_EIC_EXTINT5                   ((PIN_PA05A_EIC_EXTINT5 << 16) | MUX_PA05A_EIC_EXTINT5)
#define PORT_PA05A_EIC_EXTINT5                     ((1UL) << 5)
#define PIN_PA05A_EIC_EXTINT_NUM                   _L_(5)       /**< EIC signal: PIN_PA05 External Interrupt Line */

#define PIN_PA16A_EIC_EXTINT5                      (16L)        
#define MUX_PA16A_EIC_EXTINT5                      (0L)        
#define PINMUX_PA16A_EIC_EXTINT5                   ((PIN_PA16A_EIC_EXTINT5 << 16) | MUX_PA16A_EIC_EXTINT5)
#define PORT_PA16A_EIC_EXTINT5                     ((1UL) << 16)
#define PIN_PA16A_EIC_EXTINT_NUM                   _L_(5)       /**< EIC signal: PIN_PA16 External Interrupt Line */

#define PIN_PA27A_EIC_EXTINT5                      (27L)        
#define MUX_PA27A_EIC_EXTINT5                      (0L)        
#define PINMUX_PA27A_EIC_EXTINT5                   ((PIN_PA27A_EIC_EXTINT5 << 16) | MUX_PA27A_EIC_EXTINT5)
#define PORT_PA27A_EIC_EXTINT5                     ((1UL) << 27)
#define PIN_PA27A_EIC_EXTINT_NUM                   _L_(5)       /**< EIC signal: PIN_PA27 External Interrupt Line */

#define PIN_PA06A_EIC_EXTINT6                      (6L)         
#define MUX_PA06A_EIC_EXTINT6                      (0L)        
#define PINMUX_PA06A_EIC_EXTINT6                   ((PIN_PA06A_EIC_EXTINT6 << 16) | MUX_PA06A_EIC_EXTINT6)
#define PORT_PA06A_EIC_EXTINT6                     ((1UL) << 6)
#define PIN_PA06A_EIC_EXTINT_NUM                   _L_(6)       /**< EIC signal: PIN_PA06 External Interrupt Line */

#define PIN_PA17A_EIC_EXTINT6                      (17L)        
#define MUX_PA17A_EIC_EXTINT6                      (0L)        
#define PINMUX_PA17A_EIC_EXTINT6                   ((PIN_PA17A_EIC_EXTINT6 << 16) | MUX_PA17A_EIC_EXTINT6)
#define PORT_PA17A_EIC_EXTINT6                     ((1UL) << 17)
#define PIN_PA17A_EIC_EXTINT_NUM                   _L_(6)       /**< EIC signal: PIN_PA17 External Interrupt Line */

#define PIN_PA30A_EIC_EXTINT6                      (30L)        
#define MUX_PA30A_EIC_EXTINT6                      (0L)        
#define PINMUX_PA30A_EIC_EXTINT6                   ((PIN_PA30A_EIC_EXTINT6 << 16) | MUX_PA30A_EIC_EXTINT6)
#define PORT_PA30A_EIC_EXTINT6                     ((1UL) << 30)
#define PIN_PA30A_EIC_EXTINT_NUM                   _L_(6)       /**< EIC signal: PIN_PA30 External Interrupt Line */

#define PIN_PA07A_EIC_EXTINT7                      (7L)         
#define MUX_PA07A_EIC_EXTINT7                      (0L)        
#define PINMUX_PA07A_EIC_EXTINT7                   ((PIN_PA07A_EIC_EXTINT7 << 16) | MUX_PA07A_EIC_EXTINT7)
#define PORT_PA07A_EIC_EXTINT7                     ((1UL) << 7)
#define PIN_PA07A_EIC_EXTINT_NUM                   _L_(7)       /**< EIC signal: PIN_PA07 External Interrupt Line */

#define PIN_PA18A_EIC_EXTINT7                      (18L)        
#define MUX_PA18A_EIC_EXTINT7                      (0L)        
#define PINMUX_PA18A_EIC_EXTINT7                   ((PIN_PA18A_EIC_EXTINT7 << 16) | MUX_PA18A_EIC_EXTINT7)
#define PORT_PA18A_EIC_EXTINT7                     ((1UL) << 18)
#define PIN_PA18A_EIC_EXTINT_NUM                   _L_(7)       /**< EIC signal: PIN_PA18 External Interrupt Line */

#define PIN_PA31A_EIC_EXTINT7                      (31L)        
#define MUX_PA31A_EIC_EXTINT7                      (0L)        
#define PINMUX_PA31A_EIC_EXTINT7                   ((PIN_PA31A_EIC_EXTINT7 << 16) | MUX_PA31A_EIC_EXTINT7)
#define PORT_PA31A_EIC_EXTINT7                     ((1UL) << 31)
#define PIN_PA31A_EIC_EXTINT_NUM                   _L_(7)       /**< EIC signal: PIN_PA31 External Interrupt Line */

#define PIN_PA08A_EIC_NMI                          (8L)         
#define MUX_PA08A_EIC_NMI                          (0L)        
#define PINMUX_PA08A_EIC_NMI                       ((PIN_PA08A_EIC_NMI << 16) | MUX_PA08A_EIC_NMI)
#define PORT_PA08A_EIC_NMI                         ((1UL) << 8)

/* ========== PORT definition for GCLK peripheral ========== */
#define PIN_PA30H_GCLK_IO0                         (30L)        
#define MUX_PA30H_GCLK_IO0                         (7L)        
#define PINMUX_PA30H_GCLK_IO0                      ((PIN_PA30H_GCLK_IO0 << 16) | MUX_PA30H_GCLK_IO0)
#define PORT_PA30H_GCLK_IO0                        ((1UL) << 30)

#define PIN_PA14H_GCLK_IO0                         (14L)        
#define MUX_PA14H_GCLK_IO0                         (7L)        
#define PINMUX_PA14H_GCLK_IO0                      ((PIN_PA14H_GCLK_IO0 << 16) | MUX_PA14H_GCLK_IO0)
#define PORT_PA14H_GCLK_IO0                        ((1UL) << 14)

#define PIN_PA27H_GCLK_IO0                         (27L)        
#define MUX_PA27H_GCLK_IO0                         (7L)        
#define PINMUX_PA27H_GCLK_IO0                      ((PIN_PA27H_GCLK_IO0 << 16) | MUX_PA27H_GCLK_IO0)
#define PORT_PA27H_GCLK_IO0                        ((1UL) << 27)

#define PIN_PA23H_GCLK_IO1                         (23L)        
#define MUX_PA23H_GCLK_IO1                         (7L)        
#define PINMUX_PA23H_GCLK_IO1                      ((PIN_PA23H_GCLK_IO1 << 16) | MUX_PA23H_GCLK_IO1)
#define PORT_PA23H_GCLK_IO1                        ((1UL) << 23)

#define PIN_PA15H_GCLK_IO1                         (15L)        
#define MUX_PA15H_GCLK_IO1                         (7L)        
#define PINMUX_PA15H_GCLK_IO1                      ((PIN_PA15H_GCLK_IO1 << 16) | MUX_PA15H_GCLK_IO1)
#define PORT_PA15H_GCLK_IO1                        ((1UL) << 15)

#define PIN_PA16H_GCLK_IO2                         (16L)        
#define MUX_PA16H_GCLK_IO2                         (7L)        
#define PINMUX_PA16H_GCLK_IO2                      ((PIN_PA16H_GCLK_IO2 << 16) | MUX_PA16H_GCLK_IO2)
#define PORT_PA16H_GCLK_IO2                        ((1UL) << 16)

#define PIN_PA22H_GCLK_IO2                         (22L)        
#define MUX_PA22H_GCLK_IO2                         (7L)        
#define PINMUX_PA22H_GCLK_IO2                      ((PIN_PA22H_GCLK_IO2 << 16) | MUX_PA22H_GCLK_IO2)
#define PORT_PA22H_GCLK_IO2                        ((1UL) << 22)

#define PIN_PA11H_GCLK_IO3                         (11L)        
#define MUX_PA11H_GCLK_IO3                         (7L)        
#define PINMUX_PA11H_GCLK_IO3                      ((PIN_PA11H_GCLK_IO3 << 16) | MUX_PA11H_GCLK_IO3)
#define PORT_PA11H_GCLK_IO3                        ((1UL) << 11)

#define PIN_PA17H_GCLK_IO3                         (17L)        
#define MUX_PA17H_GCLK_IO3                         (7L)        
#define PINMUX_PA17H_GCLK_IO3                      ((PIN_PA17H_GCLK_IO3 << 16) | MUX_PA17H_GCLK_IO3)
#define PORT_PA17H_GCLK_IO3                        ((1UL) << 17)

#define PIN_PA10H_GCLK_IO4                         (10L)        
#define MUX_PA10H_GCLK_IO4                         (7L)        
#define PINMUX_PA10H_GCLK_IO4                      ((PIN_PA10H_GCLK_IO4 << 16) | MUX_PA10H_GCLK_IO4)
#define PORT_PA10H_GCLK_IO4                        ((1UL) << 10)

/* ========== PORT definition for OPAMP peripheral ========== */
#define PIN_PA02B_OPAMP_OANEG0                     (2L)         
#define MUX_PA02B_OPAMP_OANEG0                     (1L)        
#define PINMUX_PA02B_OPAMP_OANEG0                  ((PIN_PA02B_OPAMP_OANEG0 << 16) | MUX_PA02B_OPAMP_OANEG0)
#define PORT_PA02B_OPAMP_OANEG0                    ((1UL) << 2)

#define PIN_PA00B_OPAMP_OANEG1                     (0L)         
#define MUX_PA00B_OPAMP_OANEG1                     (1L)        
#define PINMUX_PA00B_OPAMP_OANEG1                  ((PIN_PA00B_OPAMP_OANEG1 << 16) | MUX_PA00B_OPAMP_OANEG1)
#define PORT_PA00B_OPAMP_OANEG1                    ((1UL) << 0)

#define PIN_PA03B_OPAMP_OANEG2                     (3L)         
#define MUX_PA03B_OPAMP_OANEG2                     (1L)        
#define PINMUX_PA03B_OPAMP_OANEG2                  ((PIN_PA03B_OPAMP_OANEG2 << 16) | MUX_PA03B_OPAMP_OANEG2)
#define PORT_PA03B_OPAMP_OANEG2                    ((1UL) << 3)

#define PIN_PA07B_OPAMP_OAOUT0                     (7L)         
#define MUX_PA07B_OPAMP_OAOUT0                     (1L)        
#define PINMUX_PA07B_OPAMP_OAOUT0                  ((PIN_PA07B_OPAMP_OAOUT0 << 16) | MUX_PA07B_OPAMP_OAOUT0)
#define PORT_PA07B_OPAMP_OAOUT0                    ((1UL) << 7)

#define PIN_PA04B_OPAMP_OAOUT2                     (4L)         
#define MUX_PA04B_OPAMP_OAOUT2                     (1L)        
#define PINMUX_PA04B_OPAMP_OAOUT2                  ((PIN_PA04B_OPAMP_OAOUT2 << 16) | MUX_PA04B_OPAMP_OAOUT2)
#define PORT_PA04B_OPAMP_OAOUT2                    ((1UL) << 4)

#define PIN_PA06B_OPAMP_OAPOS0                     (6L)         
#define MUX_PA06B_OPAMP_OAPOS0                     (1L)        
#define PINMUX_PA06B_OPAMP_OAPOS0                  ((PIN_PA06B_OPAMP_OAPOS0 << 16) | MUX_PA06B_OPAMP_OAPOS0)
#define PORT_PA06B_OPAMP_OAPOS0                    ((1UL) << 6)

#define PIN_PA01B_OPAMP_OAPOS1                     (1L)         
#define MUX_PA01B_OPAMP_OAPOS1                     (1L)        
#define PINMUX_PA01B_OPAMP_OAPOS1                  ((PIN_PA01B_OPAMP_OAPOS1 << 16) | MUX_PA01B_OPAMP_OAPOS1)
#define PORT_PA01B_OPAMP_OAPOS1                    ((1UL) << 1)

#define PIN_PA05B_OPAMP_OAPOS2                     (5L)         
#define MUX_PA05B_OPAMP_OAPOS2                     (1L)        
#define PINMUX_PA05B_OPAMP_OAPOS2                  ((PIN_PA05B_OPAMP_OAPOS2 << 16) | MUX_PA05B_OPAMP_OAPOS2)
#define PORT_PA05B_OPAMP_OAPOS2                    ((1UL) << 5)

/* ========== PORT definition for PTC peripheral ========== */
#define PIN_PA00F_PTC_DRV0                         (0L)         
#define MUX_PA00F_PTC_DRV0                         (5L)        
#define PINMUX_PA00F_PTC_DRV0                      ((PIN_PA00F_PTC_DRV0 << 16) | MUX_PA00F_PTC_DRV0)
#define PORT_PA00F_PTC_DRV0                        ((1UL) << 0)

#define PIN_PA01F_PTC_DRV1                         (1L)         
#define MUX_PA01F_PTC_DRV1                         (5L)        
#define PINMUX_PA01F_PTC_DRV1                      ((PIN_PA01F_PTC_DRV1 << 16) | MUX_PA01F_PTC_DRV1)
#define PORT_PA01F_PTC_DRV1                        ((1UL) << 1)

#define PIN_PA02F_PTC_DRV2                         (2L)         
#define MUX_PA02F_PTC_DRV2                         (5L)        
#define PINMUX_PA02F_PTC_DRV2                      ((PIN_PA02F_PTC_DRV2 << 16) | MUX_PA02F_PTC_DRV2)
#define PORT_PA02F_PTC_DRV2                        ((1UL) << 2)

#define PIN_PA03F_PTC_DRV3                         (3L)         
#define MUX_PA03F_PTC_DRV3                         (5L)        
#define PINMUX_PA03F_PTC_DRV3                      ((PIN_PA03F_PTC_DRV3 << 16) | MUX_PA03F_PTC_DRV3)
#define PORT_PA03F_PTC_DRV3                        ((1UL) << 3)

#define PIN_PA05F_PTC_DRV4                         (5L)         
#define MUX_PA05F_PTC_DRV4                         (5L)        
#define PINMUX_PA05F_PTC_DRV4                      ((PIN_PA05F_PTC_DRV4 << 16) | MUX_PA05F_PTC_DRV4)
#define PORT_PA05F_PTC_DRV4                        ((1UL) << 5)

#define PIN_PA06F_PTC_DRV5                         (6L)         
#define MUX_PA06F_PTC_DRV5                         (5L)        
#define PINMUX_PA06F_PTC_DRV5                      ((PIN_PA06F_PTC_DRV5 << 16) | MUX_PA06F_PTC_DRV5)
#define PORT_PA06F_PTC_DRV5                        ((1UL) << 6)

#define PIN_PA08F_PTC_DRV6                         (8L)         
#define MUX_PA08F_PTC_DRV6                         (5L)        
#define PINMUX_PA08F_PTC_DRV6                      ((PIN_PA08F_PTC_DRV6 << 16) | MUX_PA08F_PTC_DRV6)
#define PORT_PA08F_PTC_DRV6                        ((1UL) << 8)

#define PIN_PA09F_PTC_DRV7                         (9L)         
#define MUX_PA09F_PTC_DRV7                         (5L)        
#define PINMUX_PA09F_PTC_DRV7                      ((PIN_PA09F_PTC_DRV7 << 16) | MUX_PA09F_PTC_DRV7)
#define PORT_PA09F_PTC_DRV7                        ((1UL) << 9)

#define PIN_PA10F_PTC_DRV8                         (10L)        
#define MUX_PA10F_PTC_DRV8                         (5L)        
#define PINMUX_PA10F_PTC_DRV8                      ((PIN_PA10F_PTC_DRV8 << 16) | MUX_PA10F_PTC_DRV8)
#define PORT_PA10F_PTC_DRV8                        ((1UL) << 10)

#define PIN_PA11F_PTC_DRV9                         (11L)        
#define MUX_PA11F_PTC_DRV9                         (5L)        
#define PINMUX_PA11F_PTC_DRV9                      ((PIN_PA11F_PTC_DRV9 << 16) | MUX_PA11F_PTC_DRV9)
#define PORT_PA11F_PTC_DRV9                        ((1UL) << 11)

#define PIN_PA14F_PTC_DRV10                        (14L)        
#define MUX_PA14F_PTC_DRV10                        (5L)        
#define PINMUX_PA14F_PTC_DRV10                     ((PIN_PA14F_PTC_DRV10 << 16) | MUX_PA14F_PTC_DRV10)
#define PORT_PA14F_PTC_DRV10                       ((1UL) << 14)

#define PIN_PA15F_PTC_DRV11                        (15L)        
#define MUX_PA15F_PTC_DRV11                        (5L)        
#define PINMUX_PA15F_PTC_DRV11                     ((PIN_PA15F_PTC_DRV11 << 16) | MUX_PA15F_PTC_DRV11)
#define PORT_PA15F_PTC_DRV11                       ((1UL) << 15)

#define PIN_PA16F_PTC_DRV12                        (16L)        
#define MUX_PA16F_PTC_DRV12                        (5L)        
#define PINMUX_PA16F_PTC_DRV12                     ((PIN_PA16F_PTC_DRV12 << 16) | MUX_PA16F_PTC_DRV12)
#define PORT_PA16F_PTC_DRV12                       ((1UL) << 16)

#define PIN_PA17F_PTC_DRV13                        (17L)        
#define MUX_PA17F_PTC_DRV13                        (5L)        
#define PINMUX_PA17F_PTC_DRV13                     ((PIN_PA17F_PTC_DRV13 << 16) | MUX_PA17F_PTC_DRV13)
#define PORT_PA17F_PTC_DRV13                       ((1UL) << 17)

#define PIN_PA18F_PTC_DRV14                        (18L)        
#define MUX_PA18F_PTC_DRV14                        (5L)        
#define PINMUX_PA18F_PTC_DRV14                     ((PIN_PA18F_PTC_DRV14 << 16) | MUX_PA18F_PTC_DRV14)
#define PORT_PA18F_PTC_DRV14                       ((1UL) << 18)

#define PIN_PA19F_PTC_DRV15                        (19L)        
#define MUX_PA19F_PTC_DRV15                        (5L)        
#define PINMUX_PA19F_PTC_DRV15                     ((PIN_PA19F_PTC_DRV15 << 16) | MUX_PA19F_PTC_DRV15)
#define PORT_PA19F_PTC_DRV15                       ((1UL) << 19)

#define PIN_PA22F_PTC_DRV16                        (22L)        
#define MUX_PA22F_PTC_DRV16                        (5L)        
#define PINMUX_PA22F_PTC_DRV16                     ((PIN_PA22F_PTC_DRV16 << 16) | MUX_PA22F_PTC_DRV16)
#define PORT_PA22F_PTC_DRV16                       ((1UL) << 22)

#define PIN_PA23F_PTC_DRV17                        (23L)        
#define MUX_PA23F_PTC_DRV17                        (5L)        
#define PINMUX_PA23F_PTC_DRV17                     ((PIN_PA23F_PTC_DRV17 << 16) | MUX_PA23F_PTC_DRV17)
#define PORT_PA23F_PTC_DRV17                       ((1UL) << 23)

#define PIN_PA30F_PTC_DRV18                        (30L)        
#define MUX_PA30F_PTC_DRV18                        (5L)        
#define PINMUX_PA30F_PTC_DRV18                     ((PIN_PA30F_PTC_DRV18 << 16) | MUX_PA30F_PTC_DRV18)
#define PORT_PA30F_PTC_DRV18                       ((1UL) << 30)

#define PIN_PA31F_PTC_DRV19                        (31L)        
#define MUX_PA31F_PTC_DRV19                        (5L)        
#define PINMUX_PA31F_PTC_DRV19                     ((PIN_PA31F_PTC_DRV19 << 16) | MUX_PA31F_PTC_DRV19)
#define PORT_PA31F_PTC_DRV19                       ((1UL) << 31)

#define PIN_PA03B_PTC_ECI0                         (3L)         
#define MUX_PA03B_PTC_ECI0                         (1L)        
#define PINMUX_PA03B_PTC_ECI0                      ((PIN_PA03B_PTC_ECI0 << 16) | MUX_PA03B_PTC_ECI0)
#define PORT_PA03B_PTC_ECI0                        ((1UL) << 3)

#define PIN_PA04B_PTC_ECI1                         (4L)         
#define MUX_PA04B_PTC_ECI1                         (1L)        
#define PINMUX_PA04B_PTC_ECI1                      ((PIN_PA04B_PTC_ECI1 << 16) | MUX_PA04B_PTC_ECI1)
#define PORT_PA04B_PTC_ECI1                        ((1UL) << 4)

#define PIN_PA05B_PTC_ECI2                         (5L)         
#define MUX_PA05B_PTC_ECI2                         (1L)        
#define PINMUX_PA05B_PTC_ECI2                      ((PIN_PA05B_PTC_ECI2 << 16) | MUX_PA05B_PTC_ECI2)
#define PORT_PA05B_PTC_ECI2                        ((1UL) << 5)

#define PIN_PA06B_PTC_ECI3                         (6L)         
#define MUX_PA06B_PTC_ECI3                         (1L)        
#define PINMUX_PA06B_PTC_ECI3                      ((PIN_PA06B_PTC_ECI3 << 16) | MUX_PA06B_PTC_ECI3)
#define PORT_PA06B_PTC_ECI3                        ((1UL) << 6)

#define PIN_PA00B_PTC_X0                           (0L)         
#define MUX_PA00B_PTC_X0                           (1L)        
#define PINMUX_PA00B_PTC_X0                        ((PIN_PA00B_PTC_X0 << 16) | MUX_PA00B_PTC_X0)
#define PORT_PA00B_PTC_X0                          ((1UL) << 0)

#define PIN_PA00B_PTC_Y0                           (0L)         
#define MUX_PA00B_PTC_Y0                           (1L)        
#define PINMUX_PA00B_PTC_Y0                        ((PIN_PA00B_PTC_Y0 << 16) | MUX_PA00B_PTC_Y0)
#define PORT_PA00B_PTC_Y0                          ((1UL) << 0)

#define PIN_PA01B_PTC_X1                           (1L)         
#define MUX_PA01B_PTC_X1                           (1L)        
#define PINMUX_PA01B_PTC_X1                        ((PIN_PA01B_PTC_X1 << 16) | MUX_PA01B_PTC_X1)
#define PORT_PA01B_PTC_X1                          ((1UL) << 1)

#define PIN_PA01B_PTC_Y1                           (1L)         
#define MUX_PA01B_PTC_Y1                           (1L)        
#define PINMUX_PA01B_PTC_Y1                        ((PIN_PA01B_PTC_Y1 << 16) | MUX_PA01B_PTC_Y1)
#define PORT_PA01B_PTC_Y1                          ((1UL) << 1)

#define PIN_PA02B_PTC_X2                           (2L)         
#define MUX_PA02B_PTC_X2                           (1L)        
#define PINMUX_PA02B_PTC_X2                        ((PIN_PA02B_PTC_X2 << 16) | MUX_PA02B_PTC_X2)
#define PORT_PA02B_PTC_X2                          ((1UL) << 2)

#define PIN_PA02B_PTC_Y2                           (2L)         
#define MUX_PA02B_PTC_Y2                           (1L)        
#define PINMUX_PA02B_PTC_Y2                        ((PIN_PA02B_PTC_Y2 << 16) | MUX_PA02B_PTC_Y2)
#define PORT_PA02B_PTC_Y2                          ((1UL) << 2)

#define PIN_PA03B_PTC_X3                           (3L)         
#define MUX_PA03B_PTC_X3                           (1L)        
#define PINMUX_PA03B_PTC_X3                        ((PIN_PA03B_PTC_X3 << 16) | MUX_PA03B_PTC_X3)
#define PORT_PA03B_PTC_X3                          ((1UL) << 3)

#define PIN_PA03B_PTC_Y3                           (3L)         
#define MUX_PA03B_PTC_Y3                           (1L)        
#define PINMUX_PA03B_PTC_Y3                        ((PIN_PA03B_PTC_Y3 << 16) | MUX_PA03B_PTC_Y3)
#define PORT_PA03B_PTC_Y3                          ((1UL) << 3)

#define PIN_PA05B_PTC_X4                           (5L)         
#define MUX_PA05B_PTC_X4                           (1L)        
#define PINMUX_PA05B_PTC_X4                        ((PIN_PA05B_PTC_X4 << 16) | MUX_PA05B_PTC_X4)
#define PORT_PA05B_PTC_X4                          ((1UL) << 5)

#define PIN_PA05B_PTC_Y4                           (5L)         
#define MUX_PA05B_PTC_Y4                           (1L)        
#define PINMUX_PA05B_PTC_Y4                        ((PIN_PA05B_PTC_Y4 << 16) | MUX_PA05B_PTC_Y4)
#define PORT_PA05B_PTC_Y4                          ((1UL) << 5)

#define PIN_PA06B_PTC_X5                           (6L)         
#define MUX_PA06B_PTC_X5                           (1L)        
#define PINMUX_PA06B_PTC_X5                        ((PIN_PA06B_PTC_X5 << 16) | MUX_PA06B_PTC_X5)
#define PORT_PA06B_PTC_X5                          ((1UL) << 6)

#define PIN_PA06B_PTC_Y5                           (6L)         
#define MUX_PA06B_PTC_Y5                           (1L)        
#define PINMUX_PA06B_PTC_Y5                        ((PIN_PA06B_PTC_Y5 << 16) | MUX_PA06B_PTC_Y5)
#define PORT_PA06B_PTC_Y5                          ((1UL) << 6)

#define PIN_PA08B_PTC_X6                           (8L)         
#define MUX_PA08B_PTC_X6                           (1L)        
#define PINMUX_PA08B_PTC_X6                        ((PIN_PA08B_PTC_X6 << 16) | MUX_PA08B_PTC_X6)
#define PORT_PA08B_PTC_X6                          ((1UL) << 8)

#define PIN_PA08B_PTC_Y6                           (8L)         
#define MUX_PA08B_PTC_Y6                           (1L)        
#define PINMUX_PA08B_PTC_Y6                        ((PIN_PA08B_PTC_Y6 << 16) | MUX_PA08B_PTC_Y6)
#define PORT_PA08B_PTC_Y6                          ((1UL) << 8)

#define PIN_PA09B_PTC_X7                           (9L)         
#define MUX_PA09B_PTC_X7                           (1L)        
#define PINMUX_PA09B_PTC_X7                        ((PIN_PA09B_PTC_X7 << 16) | MUX_PA09B_PTC_X7)
#define PORT_PA09B_PTC_X7                          ((1UL) << 9)

#define PIN_PA09B_PTC_Y7                           (9L)         
#define MUX_PA09B_PTC_Y7                           (1L)        
#define PINMUX_PA09B_PTC_Y7                        ((PIN_PA09B_PTC_Y7 << 16) | MUX_PA09B_PTC_Y7)
#define PORT_PA09B_PTC_Y7                          ((1UL) << 9)

#define PIN_PA10B_PTC_X8                           (10L)        
#define MUX_PA10B_PTC_X8                           (1L)        
#define PINMUX_PA10B_PTC_X8                        ((PIN_PA10B_PTC_X8 << 16) | MUX_PA10B_PTC_X8)
#define PORT_PA10B_PTC_X8                          ((1UL) << 10)

#define PIN_PA10B_PTC_Y8                           (10L)        
#define MUX_PA10B_PTC_Y8                           (1L)        
#define PINMUX_PA10B_PTC_Y8                        ((PIN_PA10B_PTC_Y8 << 16) | MUX_PA10B_PTC_Y8)
#define PORT_PA10B_PTC_Y8                          ((1UL) << 10)

#define PIN_PA11B_PTC_X9                           (11L)        
#define MUX_PA11B_PTC_X9                           (1L)        
#define PINMUX_PA11B_PTC_X9                        ((PIN_PA11B_PTC_X9 << 16) | MUX_PA11B_PTC_X9)
#define PORT_PA11B_PTC_X9                          ((1UL) << 11)

#define PIN_PA11B_PTC_Y9                           (11L)        
#define MUX_PA11B_PTC_Y9                           (1L)        
#define PINMUX_PA11B_PTC_Y9                        ((PIN_PA11B_PTC_Y9 << 16) | MUX_PA11B_PTC_Y9)
#define PORT_PA11B_PTC_Y9                          ((1UL) << 11)

#define PIN_PA14B_PTC_X10                          (14L)        
#define MUX_PA14B_PTC_X10                          (1L)        
#define PINMUX_PA14B_PTC_X10                       ((PIN_PA14B_PTC_X10 << 16) | MUX_PA14B_PTC_X10)
#define PORT_PA14B_PTC_X10                         ((1UL) << 14)

#define PIN_PA14B_PTC_Y10                          (14L)        
#define MUX_PA14B_PTC_Y10                          (1L)        
#define PINMUX_PA14B_PTC_Y10                       ((PIN_PA14B_PTC_Y10 << 16) | MUX_PA14B_PTC_Y10)
#define PORT_PA14B_PTC_Y10                         ((1UL) << 14)

#define PIN_PA15B_PTC_X11                          (15L)        
#define MUX_PA15B_PTC_X11                          (1L)        
#define PINMUX_PA15B_PTC_X11                       ((PIN_PA15B_PTC_X11 << 16) | MUX_PA15B_PTC_X11)
#define PORT_PA15B_PTC_X11                         ((1UL) << 15)

#define PIN_PA15B_PTC_Y11                          (15L)        
#define MUX_PA15B_PTC_Y11                          (1L)        
#define PINMUX_PA15B_PTC_Y11                       ((PIN_PA15B_PTC_Y11 << 16) | MUX_PA15B_PTC_Y11)
#define PORT_PA15B_PTC_Y11                         ((1UL) << 15)

#define PIN_PA16B_PTC_X12                          (16L)        
#define MUX_PA16B_PTC_X12                          (1L)        
#define PINMUX_PA16B_PTC_X12                       ((PIN_PA16B_PTC_X12 << 16) | MUX_PA16B_PTC_X12)
#define PORT_PA16B_PTC_X12                         ((1UL) << 16)

#define PIN_PA16B_PTC_Y12                          (16L)        
#define MUX_PA16B_PTC_Y12                          (1L)        
#define PINMUX_PA16B_PTC_Y12                       ((PIN_PA16B_PTC_Y12 << 16) | MUX_PA16B_PTC_Y12)
#define PORT_PA16B_PTC_Y12                         ((1UL) << 16)

#define PIN_PA17B_PTC_X13                          (17L)        
#define MUX_PA17B_PTC_X13                          (1L)        
#define PINMUX_PA17B_PTC_X13                       ((PIN_PA17B_PTC_X13 << 16) | MUX_PA17B_PTC_X13)
#define PORT_PA17B_PTC_X13                         ((1UL) << 17)

#define PIN_PA17B_PTC_Y13                          (17L)        
#define MUX_PA17B_PTC_Y13                          (1L)        
#define PINMUX_PA17B_PTC_Y13                       ((PIN_PA17B_PTC_Y13 << 16) | MUX_PA17B_PTC_Y13)
#define PORT_PA17B_PTC_Y13                         ((1UL) << 17)

#define PIN_PA18B_PTC_X14                          (18L)        
#define MUX_PA18B_PTC_X14                          (1L)        
#define PINMUX_PA18B_PTC_X14                       ((PIN_PA18B_PTC_X14 << 16) | MUX_PA18B_PTC_X14)
#define PORT_PA18B_PTC_X14                         ((1UL) << 18)

#define PIN_PA18B_PTC_Y14                          (18L)        
#define MUX_PA18B_PTC_Y14                          (1L)        
#define PINMUX_PA18B_PTC_Y14                       ((PIN_PA18B_PTC_Y14 << 16) | MUX_PA18B_PTC_Y14)
#define PORT_PA18B_PTC_Y14                         ((1UL) << 18)

#define PIN_PA19B_PTC_X15                          (19L)        
#define MUX_PA19B_PTC_X15                          (1L)        
#define PINMUX_PA19B_PTC_X15                       ((PIN_PA19B_PTC_X15 << 16) | MUX_PA19B_PTC_X15)
#define PORT_PA19B_PTC_X15                         ((1UL) << 19)

#define PIN_PA19B_PTC_Y15                          (19L)        
#define MUX_PA19B_PTC_Y15                          (1L)        
#define PINMUX_PA19B_PTC_Y15                       ((PIN_PA19B_PTC_Y15 << 16) | MUX_PA19B_PTC_Y15)
#define PORT_PA19B_PTC_Y15                         ((1UL) << 19)

#define PIN_PA22B_PTC_X16                          (22L)        
#define MUX_PA22B_PTC_X16                          (1L)        
#define PINMUX_PA22B_PTC_X16                       ((PIN_PA22B_PTC_X16 << 16) | MUX_PA22B_PTC_X16)
#define PORT_PA22B_PTC_X16                         ((1UL) << 22)

#define PIN_PA22B_PTC_Y16                          (22L)        
#define MUX_PA22B_PTC_Y16                          (1L)        
#define PINMUX_PA22B_PTC_Y16                       ((PIN_PA22B_PTC_Y16 << 16) | MUX_PA22B_PTC_Y16)
#define PORT_PA22B_PTC_Y16                         ((1UL) << 22)

#define PIN_PA23B_PTC_X17                          (23L)        
#define MUX_PA23B_PTC_X17                          (1L)        
#define PINMUX_PA23B_PTC_X17                       ((PIN_PA23B_PTC_X17 << 16) | MUX_PA23B_PTC_X17)
#define PORT_PA23B_PTC_X17                         ((1UL) << 23)

#define PIN_PA23B_PTC_Y17                          (23L)        
#define MUX_PA23B_PTC_Y17                          (1L)        
#define PINMUX_PA23B_PTC_Y17                       ((PIN_PA23B_PTC_Y17 << 16) | MUX_PA23B_PTC_Y17)
#define PORT_PA23B_PTC_Y17                         ((1UL) << 23)

#define PIN_PA30B_PTC_X18                          (30L)        
#define MUX_PA30B_PTC_X18                          (1L)        
#define PINMUX_PA30B_PTC_X18                       ((PIN_PA30B_PTC_X18 << 16) | MUX_PA30B_PTC_X18)
#define PORT_PA30B_PTC_X18                         ((1UL) << 30)

#define PIN_PA30B_PTC_Y18                          (30L)        
#define MUX_PA30B_PTC_Y18                          (1L)        
#define PINMUX_PA30B_PTC_Y18                       ((PIN_PA30B_PTC_Y18 << 16) | MUX_PA30B_PTC_Y18)
#define PORT_PA30B_PTC_Y18                         ((1UL) << 30)

#define PIN_PA31B_PTC_X19                          (31L)        
#define MUX_PA31B_PTC_X19                          (1L)        
#define PINMUX_PA31B_PTC_X19                       ((PIN_PA31B_PTC_X19 << 16) | MUX_PA31B_PTC_X19)
#define PORT_PA31B_PTC_X19                         ((1UL) << 31)

#define PIN_PA31B_PTC_Y19                          (31L)        
#define MUX_PA31B_PTC_Y19                          (1L)        
#define PINMUX_PA31B_PTC_Y19                       ((PIN_PA31B_PTC_Y19 << 16) | MUX_PA31B_PTC_Y19)
#define PORT_PA31B_PTC_Y19                         ((1UL) << 31)

/* ========== PORT definition for RTC peripheral ========== */
#define PIN_PA08G_RTC_IN0                          (8L)         
#define MUX_PA08G_RTC_IN0                          (6L)        
#define PINMUX_PA08G_RTC_IN0                       ((PIN_PA08G_RTC_IN0 << 16) | MUX_PA08G_RTC_IN0)
#define PORT_PA08G_RTC_IN0                         ((1UL) << 8)

#define PIN_PA09G_RTC_IN1                          (9L)         
#define MUX_PA09G_RTC_IN1                          (6L)        
#define PINMUX_PA09G_RTC_IN1                       ((PIN_PA09G_RTC_IN1 << 16) | MUX_PA09G_RTC_IN1)
#define PORT_PA09G_RTC_IN1                         ((1UL) << 9)

#define PIN_PA16G_RTC_IN2                          (16L)        
#define MUX_PA16G_RTC_IN2                          (6L)        
#define PINMUX_PA16G_RTC_IN2                       ((PIN_PA16G_RTC_IN2 << 16) | MUX_PA16G_RTC_IN2)
#define PORT_PA16G_RTC_IN2                         ((1UL) << 16)

#define PIN_PA17G_RTC_IN3                          (17L)        
#define MUX_PA17G_RTC_IN3                          (6L)        
#define PINMUX_PA17G_RTC_IN3                       ((PIN_PA17G_RTC_IN3 << 16) | MUX_PA17G_RTC_IN3)
#define PORT_PA17G_RTC_IN3                         ((1UL) << 17)

#define PIN_PA18G_RTC_OUT0                         (18L)        
#define MUX_PA18G_RTC_OUT0                         (6L)        
#define PINMUX_PA18G_RTC_OUT0                      ((PIN_PA18G_RTC_OUT0 << 16) | MUX_PA18G_RTC_OUT0)
#define PORT_PA18G_RTC_OUT0                        ((1UL) << 18)

#define PIN_PA19G_RTC_OUT1                         (19L)        
#define MUX_PA19G_RTC_OUT1                         (6L)        
#define PINMUX_PA19G_RTC_OUT1                      ((PIN_PA19G_RTC_OUT1 << 16) | MUX_PA19G_RTC_OUT1)
#define PORT_PA19G_RTC_OUT1                        ((1UL) << 19)

#define PIN_PA22G_RTC_OUT2                         (22L)        
#define MUX_PA22G_RTC_OUT2                         (6L)        
#define PINMUX_PA22G_RTC_OUT2                      ((PIN_PA22G_RTC_OUT2 << 16) | MUX_PA22G_RTC_OUT2)
#define PORT_PA22G_RTC_OUT2                        ((1UL) << 22)

#define PIN_PA23G_RTC_OUT3                         (23L)        
#define MUX_PA23G_RTC_OUT3                         (6L)        
#define PINMUX_PA23G_RTC_OUT3                      ((PIN_PA23G_RTC_OUT3 << 16) | MUX_PA23G_RTC_OUT3)
#define PORT_PA23G_RTC_OUT3                        ((1UL) << 23)

/* ========== PORT definition for SERCOM0 peripheral ========== */
#define PIN_PA04D_SERCOM0_PAD0                     (4L)         
#define MUX_PA04D_SERCOM0_PAD0                     (3L)        
#define PINMUX_PA04D_SERCOM0_PAD0                  ((PIN_PA04D_SERCOM0_PAD0 << 16) | MUX_PA04D_SERCOM0_PAD0)
#define PORT_PA04D_SERCOM0_PAD0                    ((1UL) << 4)

#define PIN_PA16D_SERCOM0_PAD0                     (16L)        
#define MUX_PA16D_SERCOM0_PAD0                     (3L)        
#define PINMUX_PA16D_SERCOM0_PAD0                  ((PIN_PA16D_SERCOM0_PAD0 << 16) | MUX_PA16D_SERCOM0_PAD0)
#define PORT_PA16D_SERCOM0_PAD0                    ((1UL) << 16)

#define PIN_PA22C_SERCOM0_PAD0                     (22L)        
#define MUX_PA22C_SERCOM0_PAD0                     (2L)        
#define PINMUX_PA22C_SERCOM0_PAD0                  ((PIN_PA22C_SERCOM0_PAD0 << 16) | MUX_PA22C_SERCOM0_PAD0)
#define PORT_PA22C_SERCOM0_PAD0                    ((1UL) << 22)

#define PIN_PA05D_SERCOM0_PAD1                     (5L)         
#define MUX_PA05D_SERCOM0_PAD1                     (3L)        
#define PINMUX_PA05D_SERCOM0_PAD1                  ((PIN_PA05D_SERCOM0_PAD1 << 16) | MUX_PA05D_SERCOM0_PAD1)
#define PORT_PA05D_SERCOM0_PAD1                    ((1UL) << 5)

#define PIN_PA17D_SERCOM0_PAD1                     (17L)        
#define MUX_PA17D_SERCOM0_PAD1                     (3L)        
#define PINMUX_PA17D_SERCOM0_PAD1                  ((PIN_PA17D_SERCOM0_PAD1 << 16) | MUX_PA17D_SERCOM0_PAD1)
#define PORT_PA17D_SERCOM0_PAD1                    ((1UL) << 17)

#define PIN_PA23C_SERCOM0_PAD1                     (23L)        
#define MUX_PA23C_SERCOM0_PAD1                     (2L)        
#define PINMUX_PA23C_SERCOM0_PAD1                  ((PIN_PA23C_SERCOM0_PAD1 << 16) | MUX_PA23C_SERCOM0_PAD1)
#define PORT_PA23C_SERCOM0_PAD1                    ((1UL) << 23)

#define PIN_PA06D_SERCOM0_PAD2                     (6L)         
#define MUX_PA06D_SERCOM0_PAD2                     (3L)        
#define PINMUX_PA06D_SERCOM0_PAD2                  ((PIN_PA06D_SERCOM0_PAD2 << 16) | MUX_PA06D_SERCOM0_PAD2)
#define PORT_PA06D_SERCOM0_PAD2                    ((1UL) << 6)

#define PIN_PA14D_SERCOM0_PAD2                     (14L)        
#define MUX_PA14D_SERCOM0_PAD2                     (3L)        
#define PINMUX_PA14D_SERCOM0_PAD2                  ((PIN_PA14D_SERCOM0_PAD2 << 16) | MUX_PA14D_SERCOM0_PAD2)
#define PORT_PA14D_SERCOM0_PAD2                    ((1UL) << 14)

#define PIN_PA18D_SERCOM0_PAD2                     (18L)        
#define MUX_PA18D_SERCOM0_PAD2                     (3L)        
#define PINMUX_PA18D_SERCOM0_PAD2                  ((PIN_PA18D_SERCOM0_PAD2 << 16) | MUX_PA18D_SERCOM0_PAD2)
#define PORT_PA18D_SERCOM0_PAD2                    ((1UL) << 18)

#define PIN_PA24C_SERCOM0_PAD2                     (24L)        
#define MUX_PA24C_SERCOM0_PAD2                     (2L)        
#define PINMUX_PA24C_SERCOM0_PAD2                  ((PIN_PA24C_SERCOM0_PAD2 << 16) | MUX_PA24C_SERCOM0_PAD2)
#define PORT_PA24C_SERCOM0_PAD2                    ((1UL) << 24)

#define PIN_PA02D_SERCOM0_PAD2                     (2L)         
#define MUX_PA02D_SERCOM0_PAD2                     (3L)        
#define PINMUX_PA02D_SERCOM0_PAD2                  ((PIN_PA02D_SERCOM0_PAD2 << 16) | MUX_PA02D_SERCOM0_PAD2)
#define PORT_PA02D_SERCOM0_PAD2                    ((1UL) << 2)

#define PIN_PA07D_SERCOM0_PAD3                     (7L)         
#define MUX_PA07D_SERCOM0_PAD3                     (3L)        
#define PINMUX_PA07D_SERCOM0_PAD3                  ((PIN_PA07D_SERCOM0_PAD3 << 16) | MUX_PA07D_SERCOM0_PAD3)
#define PORT_PA07D_SERCOM0_PAD3                    ((1UL) << 7)

#define PIN_PA15D_SERCOM0_PAD3                     (15L)        
#define MUX_PA15D_SERCOM0_PAD3                     (3L)        
#define PINMUX_PA15D_SERCOM0_PAD3                  ((PIN_PA15D_SERCOM0_PAD3 << 16) | MUX_PA15D_SERCOM0_PAD3)
#define PORT_PA15D_SERCOM0_PAD3                    ((1UL) << 15)

#define PIN_PA19D_SERCOM0_PAD3                     (19L)        
#define MUX_PA19D_SERCOM0_PAD3                     (3L)        
#define PINMUX_PA19D_SERCOM0_PAD3                  ((PIN_PA19D_SERCOM0_PAD3 << 16) | MUX_PA19D_SERCOM0_PAD3)
#define PORT_PA19D_SERCOM0_PAD3                    ((1UL) << 19)

#define PIN_PA25C_SERCOM0_PAD3                     (25L)        
#define MUX_PA25C_SERCOM0_PAD3                     (2L)        
#define PINMUX_PA25C_SERCOM0_PAD3                  ((PIN_PA25C_SERCOM0_PAD3 << 16) | MUX_PA25C_SERCOM0_PAD3)
#define PORT_PA25C_SERCOM0_PAD3                    ((1UL) << 25)

#define PIN_PA03D_SERCOM0_PAD3                     (3L)         
#define MUX_PA03D_SERCOM0_PAD3                     (3L)        
#define PINMUX_PA03D_SERCOM0_PAD3                  ((PIN_PA03D_SERCOM0_PAD3 << 16) | MUX_PA03D_SERCOM0_PAD3)
#define PORT_PA03D_SERCOM0_PAD3                    ((1UL) << 3)

/* ========== PORT definition for SERCOM1 peripheral ========== */
#define PIN_PA16C_SERCOM1_PAD0                     (16L)        
#define MUX_PA16C_SERCOM1_PAD0                     (2L)        
#define PINMUX_PA16C_SERCOM1_PAD0                  ((PIN_PA16C_SERCOM1_PAD0 << 16) | MUX_PA16C_SERCOM1_PAD0)
#define PORT_PA16C_SERCOM1_PAD0                    ((1UL) << 16)

#define PIN_PA08C_SERCOM1_PAD0                     (8L)         
#define MUX_PA08C_SERCOM1_PAD0                     (2L)        
#define PINMUX_PA08C_SERCOM1_PAD0                  ((PIN_PA08C_SERCOM1_PAD0 << 16) | MUX_PA08C_SERCOM1_PAD0)
#define PORT_PA08C_SERCOM1_PAD0                    ((1UL) << 8)

#define PIN_PA00D_SERCOM1_PAD0                     (0L)         
#define MUX_PA00D_SERCOM1_PAD0                     (3L)        
#define PINMUX_PA00D_SERCOM1_PAD0                  ((PIN_PA00D_SERCOM1_PAD0 << 16) | MUX_PA00D_SERCOM1_PAD0)
#define PORT_PA00D_SERCOM1_PAD0                    ((1UL) << 0)

#define PIN_PA17C_SERCOM1_PAD1                     (17L)        
#define MUX_PA17C_SERCOM1_PAD1                     (2L)        
#define PINMUX_PA17C_SERCOM1_PAD1                  ((PIN_PA17C_SERCOM1_PAD1 << 16) | MUX_PA17C_SERCOM1_PAD1)
#define PORT_PA17C_SERCOM1_PAD1                    ((1UL) << 17)

#define PIN_PA09C_SERCOM1_PAD1                     (9L)         
#define MUX_PA09C_SERCOM1_PAD1                     (2L)        
#define PINMUX_PA09C_SERCOM1_PAD1                  ((PIN_PA09C_SERCOM1_PAD1 << 16) | MUX_PA09C_SERCOM1_PAD1)
#define PORT_PA09C_SERCOM1_PAD1                    ((1UL) << 9)

#define PIN_PA01D_SERCOM1_PAD1                     (1L)         
#define MUX_PA01D_SERCOM1_PAD1                     (3L)        
#define PINMUX_PA01D_SERCOM1_PAD1                  ((PIN_PA01D_SERCOM1_PAD1 << 16) | MUX_PA01D_SERCOM1_PAD1)
#define PORT_PA01D_SERCOM1_PAD1                    ((1UL) << 1)

#define PIN_PA18C_SERCOM1_PAD2                     (18L)        
#define MUX_PA18C_SERCOM1_PAD2                     (2L)        
#define PINMUX_PA18C_SERCOM1_PAD2                  ((PIN_PA18C_SERCOM1_PAD2 << 16) | MUX_PA18C_SERCOM1_PAD2)
#define PORT_PA18C_SERCOM1_PAD2                    ((1UL) << 18)

#define PIN_PA10C_SERCOM1_PAD2                     (10L)        
#define MUX_PA10C_SERCOM1_PAD2                     (2L)        
#define PINMUX_PA10C_SERCOM1_PAD2                  ((PIN_PA10C_SERCOM1_PAD2 << 16) | MUX_PA10C_SERCOM1_PAD2)
#define PORT_PA10C_SERCOM1_PAD2                    ((1UL) << 10)

#define PIN_PA30D_SERCOM1_PAD2                     (30L)        
#define MUX_PA30D_SERCOM1_PAD2                     (3L)        
#define PINMUX_PA30D_SERCOM1_PAD2                  ((PIN_PA30D_SERCOM1_PAD2 << 16) | MUX_PA30D_SERCOM1_PAD2)
#define PORT_PA30D_SERCOM1_PAD2                    ((1UL) << 30)

#define PIN_PA19C_SERCOM1_PAD3                     (19L)        
#define MUX_PA19C_SERCOM1_PAD3                     (2L)        
#define PINMUX_PA19C_SERCOM1_PAD3                  ((PIN_PA19C_SERCOM1_PAD3 << 16) | MUX_PA19C_SERCOM1_PAD3)
#define PORT_PA19C_SERCOM1_PAD3                    ((1UL) << 19)

#define PIN_PA11C_SERCOM1_PAD3                     (11L)        
#define MUX_PA11C_SERCOM1_PAD3                     (2L)        
#define PINMUX_PA11C_SERCOM1_PAD3                  ((PIN_PA11C_SERCOM1_PAD3 << 16) | MUX_PA11C_SERCOM1_PAD3)
#define PORT_PA11C_SERCOM1_PAD3                    ((1UL) << 11)

#define PIN_PA31D_SERCOM1_PAD3                     (31L)        
#define MUX_PA31D_SERCOM1_PAD3                     (3L)        
#define PINMUX_PA31D_SERCOM1_PAD3                  ((PIN_PA31D_SERCOM1_PAD3 << 16) | MUX_PA31D_SERCOM1_PAD3)
#define PORT_PA31D_SERCOM1_PAD3                    ((1UL) << 31)

/* ========== PORT definition for SERCOM2 peripheral ========== */
#define PIN_PA08D_SERCOM2_PAD0                     (8L)         
#define MUX_PA08D_SERCOM2_PAD0                     (3L)        
#define PINMUX_PA08D_SERCOM2_PAD0                  ((PIN_PA08D_SERCOM2_PAD0 << 16) | MUX_PA08D_SERCOM2_PAD0)
#define PORT_PA08D_SERCOM2_PAD0                    ((1UL) << 8)

#define PIN_PA22D_SERCOM2_PAD0                     (22L)        
#define MUX_PA22D_SERCOM2_PAD0                     (3L)        
#define PINMUX_PA22D_SERCOM2_PAD0                  ((PIN_PA22D_SERCOM2_PAD0 << 16) | MUX_PA22D_SERCOM2_PAD0)
#define PORT_PA22D_SERCOM2_PAD0                    ((1UL) << 22)

#define PIN_PA09D_SERCOM2_PAD1                     (9L)         
#define MUX_PA09D_SERCOM2_PAD1                     (3L)        
#define PINMUX_PA09D_SERCOM2_PAD1                  ((PIN_PA09D_SERCOM2_PAD1 << 16) | MUX_PA09D_SERCOM2_PAD1)
#define PORT_PA09D_SERCOM2_PAD1                    ((1UL) << 9)

#define PIN_PA23D_SERCOM2_PAD1                     (23L)        
#define MUX_PA23D_SERCOM2_PAD1                     (3L)        
#define PINMUX_PA23D_SERCOM2_PAD1                  ((PIN_PA23D_SERCOM2_PAD1 << 16) | MUX_PA23D_SERCOM2_PAD1)
#define PORT_PA23D_SERCOM2_PAD1                    ((1UL) << 23)

#define PIN_PA10D_SERCOM2_PAD2                     (10L)        
#define MUX_PA10D_SERCOM2_PAD2                     (3L)        
#define PINMUX_PA10D_SERCOM2_PAD2                  ((PIN_PA10D_SERCOM2_PAD2 << 16) | MUX_PA10D_SERCOM2_PAD2)
#define PORT_PA10D_SERCOM2_PAD2                    ((1UL) << 10)

#define PIN_PA24D_SERCOM2_PAD2                     (24L)        
#define MUX_PA24D_SERCOM2_PAD2                     (3L)        
#define PINMUX_PA24D_SERCOM2_PAD2                  ((PIN_PA24D_SERCOM2_PAD2 << 16) | MUX_PA24D_SERCOM2_PAD2)
#define PORT_PA24D_SERCOM2_PAD2                    ((1UL) << 24)

#define PIN_PA14C_SERCOM2_PAD2                     (14L)        
#define MUX_PA14C_SERCOM2_PAD2                     (2L)        
#define PINMUX_PA14C_SERCOM2_PAD2                  ((PIN_PA14C_SERCOM2_PAD2 << 16) | MUX_PA14C_SERCOM2_PAD2)
#define PORT_PA14C_SERCOM2_PAD2                    ((1UL) << 14)

#define PIN_PA11D_SERCOM2_PAD3                     (11L)        
#define MUX_PA11D_SERCOM2_PAD3                     (3L)        
#define PINMUX_PA11D_SERCOM2_PAD3                  ((PIN_PA11D_SERCOM2_PAD3 << 16) | MUX_PA11D_SERCOM2_PAD3)
#define PORT_PA11D_SERCOM2_PAD3                    ((1UL) << 11)

#define PIN_PA25D_SERCOM2_PAD3                     (25L)        
#define MUX_PA25D_SERCOM2_PAD3                     (3L)        
#define PINMUX_PA25D_SERCOM2_PAD3                  ((PIN_PA25D_SERCOM2_PAD3 << 16) | MUX_PA25D_SERCOM2_PAD3)
#define PORT_PA25D_SERCOM2_PAD3                    ((1UL) << 25)

#define PIN_PA15C_SERCOM2_PAD3                     (15L)        
#define MUX_PA15C_SERCOM2_PAD3                     (2L)        
#define PINMUX_PA15C_SERCOM2_PAD3                  ((PIN_PA15C_SERCOM2_PAD3 << 16) | MUX_PA15C_SERCOM2_PAD3)
#define PORT_PA15C_SERCOM2_PAD3                    ((1UL) << 15)

/* ========== PORT definition for TC0 peripheral ========== */
#define PIN_PA04E_TC0_WO0                          (4L)         
#define MUX_PA04E_TC0_WO0                          (4L)        
#define PINMUX_PA04E_TC0_WO0                       ((PIN_PA04E_TC0_WO0 << 16) | MUX_PA04E_TC0_WO0)
#define PORT_PA04E_TC0_WO0                         ((1UL) << 4)

#define PIN_PA14E_TC0_WO0                          (14L)        
#define MUX_PA14E_TC0_WO0                          (4L)        
#define PINMUX_PA14E_TC0_WO0                       ((PIN_PA14E_TC0_WO0 << 16) | MUX_PA14E_TC0_WO0)
#define PORT_PA14E_TC0_WO0                         ((1UL) << 14)

#define PIN_PA22E_TC0_WO0                          (22L)        
#define MUX_PA22E_TC0_WO0                          (4L)        
#define PINMUX_PA22E_TC0_WO0                       ((PIN_PA22E_TC0_WO0 << 16) | MUX_PA22E_TC0_WO0)
#define PORT_PA22E_TC0_WO0                         ((1UL) << 22)

#define PIN_PA05E_TC0_WO1                          (5L)         
#define MUX_PA05E_TC0_WO1                          (4L)        
#define PINMUX_PA05E_TC0_WO1                       ((PIN_PA05E_TC0_WO1 << 16) | MUX_PA05E_TC0_WO1)
#define PORT_PA05E_TC0_WO1                         ((1UL) << 5)

#define PIN_PA15E_TC0_WO1                          (15L)        
#define MUX_PA15E_TC0_WO1                          (4L)        
#define PINMUX_PA15E_TC0_WO1                       ((PIN_PA15E_TC0_WO1 << 16) | MUX_PA15E_TC0_WO1)
#define PORT_PA15E_TC0_WO1                         ((1UL) << 15)

#define PIN_PA23E_TC0_WO1                          (23L)        
#define MUX_PA23E_TC0_WO1                          (4L)        
#define PINMUX_PA23E_TC0_WO1                       ((PIN_PA23E_TC0_WO1 << 16) | MUX_PA23E_TC0_WO1)
#define PORT_PA23E_TC0_WO1                         ((1UL) << 23)

/* ========== PORT definition for TC1 peripheral ========== */
#define PIN_PA06E_TC1_WO0                          (6L)         
#define MUX_PA06E_TC1_WO0                          (4L)        
#define PINMUX_PA06E_TC1_WO0                       ((PIN_PA06E_TC1_WO0 << 16) | MUX_PA06E_TC1_WO0)
#define PORT_PA06E_TC1_WO0                         ((1UL) << 6)

#define PIN_PA24E_TC1_WO0                          (24L)        
#define MUX_PA24E_TC1_WO0                          (4L)        
#define PINMUX_PA24E_TC1_WO0                       ((PIN_PA24E_TC1_WO0 << 16) | MUX_PA24E_TC1_WO0)
#define PORT_PA24E_TC1_WO0                         ((1UL) << 24)

#define PIN_PA30E_TC1_WO0                          (30L)        
#define MUX_PA30E_TC1_WO0                          (4L)        
#define PINMUX_PA30E_TC1_WO0                       ((PIN_PA30E_TC1_WO0 << 16) | MUX_PA30E_TC1_WO0)
#define PORT_PA30E_TC1_WO0                         ((1UL) << 30)

#define PIN_PA07E_TC1_WO1                          (7L)         
#define MUX_PA07E_TC1_WO1                          (4L)        
#define PINMUX_PA07E_TC1_WO1                       ((PIN_PA07E_TC1_WO1 << 16) | MUX_PA07E_TC1_WO1)
#define PORT_PA07E_TC1_WO1                         ((1UL) << 7)

#define PIN_PA25E_TC1_WO1                          (25L)        
#define MUX_PA25E_TC1_WO1                          (4L)        
#define PINMUX_PA25E_TC1_WO1                       ((PIN_PA25E_TC1_WO1 << 16) | MUX_PA25E_TC1_WO1)
#define PORT_PA25E_TC1_WO1                         ((1UL) << 25)

#define PIN_PA31E_TC1_WO1                          (31L)        
#define MUX_PA31E_TC1_WO1                          (4L)        
#define PINMUX_PA31E_TC1_WO1                       ((PIN_PA31E_TC1_WO1 << 16) | MUX_PA31E_TC1_WO1)
#define PORT_PA31E_TC1_WO1                         ((1UL) << 31)

/* ========== PORT definition for TC2 peripheral ========== */
#define PIN_PA00E_TC2_WO0                          (0L)         
#define MUX_PA00E_TC2_WO0                          (4L)        
#define PINMUX_PA00E_TC2_WO0                       ((PIN_PA00E_TC2_WO0 << 16) | MUX_PA00E_TC2_WO0)
#define PORT_PA00E_TC2_WO0                         ((1UL) << 0)

#define PIN_PA18E_TC2_WO0                          (18L)        
#define MUX_PA18E_TC2_WO0                          (4L)        
#define PINMUX_PA18E_TC2_WO0                       ((PIN_PA18E_TC2_WO0 << 16) | MUX_PA18E_TC2_WO0)
#define PORT_PA18E_TC2_WO0                         ((1UL) << 18)

#define PIN_PA01E_TC2_WO1                          (1L)         
#define MUX_PA01E_TC2_WO1                          (4L)        
#define PINMUX_PA01E_TC2_WO1                       ((PIN_PA01E_TC2_WO1 << 16) | MUX_PA01E_TC2_WO1)
#define PORT_PA01E_TC2_WO1                         ((1UL) << 1)

#define PIN_PA19E_TC2_WO1                          (19L)        
#define MUX_PA19E_TC2_WO1                          (4L)        
#define PINMUX_PA19E_TC2_WO1                       ((PIN_PA19E_TC2_WO1 << 16) | MUX_PA19E_TC2_WO1)
#define PORT_PA19E_TC2_WO1                         ((1UL) << 19)



#endif /* _SAML10E16A_GPIO_H_ */

