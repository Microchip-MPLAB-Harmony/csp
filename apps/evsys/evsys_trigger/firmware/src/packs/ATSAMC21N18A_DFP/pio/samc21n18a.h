/**
 * \brief Peripheral I/O description for /SAMC21N18A
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
#ifndef SAMC21N18A_GPIO_H
#define SAMC21N18A_GPIO_H

/* ========== Peripheral I/O pin numbers ========== */
#define PIN_PA00                    (  0)  /**< Pin Number for PA00 */
#define PIN_PA01                    (  1)  /**< Pin Number for PA01 */
#define PIN_PA02                    (  2)  /**< Pin Number for PA02 */
#define PIN_PA03                    (  3)  /**< Pin Number for PA03 */
#define PIN_PA04                    (  4)  /**< Pin Number for PA04 */
#define PIN_PA05                    (  5)  /**< Pin Number for PA05 */
#define PIN_PA06                    (  6)  /**< Pin Number for PA06 */
#define PIN_PA07                    (  7)  /**< Pin Number for PA07 */
#define PIN_PA08                    (  8)  /**< Pin Number for PA08 */
#define PIN_PA09                    (  9)  /**< Pin Number for PA09 */
#define PIN_PA10                    ( 10)  /**< Pin Number for PA10 */
#define PIN_PA11                    ( 11)  /**< Pin Number for PA11 */
#define PIN_PA12                    ( 12)  /**< Pin Number for PA12 */
#define PIN_PA13                    ( 13)  /**< Pin Number for PA13 */
#define PIN_PA14                    ( 14)  /**< Pin Number for PA14 */
#define PIN_PA15                    ( 15)  /**< Pin Number for PA15 */
#define PIN_PA16                    ( 16)  /**< Pin Number for PA16 */
#define PIN_PA17                    ( 17)  /**< Pin Number for PA17 */
#define PIN_PA18                    ( 18)  /**< Pin Number for PA18 */
#define PIN_PA19                    ( 19)  /**< Pin Number for PA19 */
#define PIN_PA20                    ( 20)  /**< Pin Number for PA20 */
#define PIN_PA21                    ( 21)  /**< Pin Number for PA21 */
#define PIN_PA22                    ( 22)  /**< Pin Number for PA22 */
#define PIN_PA23                    ( 23)  /**< Pin Number for PA23 */
#define PIN_PA24                    ( 24)  /**< Pin Number for PA24 */
#define PIN_PA25                    ( 25)  /**< Pin Number for PA25 */
#define PIN_PA27                    ( 27)  /**< Pin Number for PA27 */
#define PIN_PA28                    ( 28)  /**< Pin Number for PA28 */
#define PIN_PA30                    ( 30)  /**< Pin Number for PA30 */
#define PIN_PA31                    ( 31)  /**< Pin Number for PA31 */
#define PIN_PB00                    ( 32)  /**< Pin Number for PB00 */
#define PIN_PB01                    ( 33)  /**< Pin Number for PB01 */
#define PIN_PB02                    ( 34)  /**< Pin Number for PB02 */
#define PIN_PB03                    ( 35)  /**< Pin Number for PB03 */
#define PIN_PB04                    ( 36)  /**< Pin Number for PB04 */
#define PIN_PB05                    ( 37)  /**< Pin Number for PB05 */
#define PIN_PB06                    ( 38)  /**< Pin Number for PB06 */
#define PIN_PB07                    ( 39)  /**< Pin Number for PB07 */
#define PIN_PB08                    ( 40)  /**< Pin Number for PB08 */
#define PIN_PB09                    ( 41)  /**< Pin Number for PB09 */
#define PIN_PB10                    ( 42)  /**< Pin Number for PB10 */
#define PIN_PB11                    ( 43)  /**< Pin Number for PB11 */
#define PIN_PB12                    ( 44)  /**< Pin Number for PB12 */
#define PIN_PB13                    ( 45)  /**< Pin Number for PB13 */
#define PIN_PB14                    ( 46)  /**< Pin Number for PB14 */
#define PIN_PB15                    ( 47)  /**< Pin Number for PB15 */
#define PIN_PB16                    ( 48)  /**< Pin Number for PB16 */
#define PIN_PB17                    ( 49)  /**< Pin Number for PB17 */
#define PIN_PB18                    ( 50)  /**< Pin Number for PB18 */
#define PIN_PB19                    ( 51)  /**< Pin Number for PB19 */
#define PIN_PB20                    ( 52)  /**< Pin Number for PB20 */
#define PIN_PB21                    ( 53)  /**< Pin Number for PB21 */
#define PIN_PB22                    ( 54)  /**< Pin Number for PB22 */
#define PIN_PB23                    ( 55)  /**< Pin Number for PB23 */
#define PIN_PB24                    ( 56)  /**< Pin Number for PB24 */
#define PIN_PB25                    ( 57)  /**< Pin Number for PB25 */
#define PIN_PB30                    ( 62)  /**< Pin Number for PB30 */
#define PIN_PB31                    ( 63)  /**< Pin Number for PB31 */
#define PIN_PC00                    ( 64)  /**< Pin Number for PC00 */
#define PIN_PC01                    ( 65)  /**< Pin Number for PC01 */
#define PIN_PC02                    ( 66)  /**< Pin Number for PC02 */
#define PIN_PC03                    ( 67)  /**< Pin Number for PC03 */
#define PIN_PC05                    ( 69)  /**< Pin Number for PC05 */
#define PIN_PC06                    ( 70)  /**< Pin Number for PC06 */
#define PIN_PC07                    ( 71)  /**< Pin Number for PC07 */
#define PIN_PC08                    ( 72)  /**< Pin Number for PC08 */
#define PIN_PC09                    ( 73)  /**< Pin Number for PC09 */
#define PIN_PC10                    ( 74)  /**< Pin Number for PC10 */
#define PIN_PC11                    ( 75)  /**< Pin Number for PC11 */
#define PIN_PC12                    ( 76)  /**< Pin Number for PC12 */
#define PIN_PC13                    ( 77)  /**< Pin Number for PC13 */
#define PIN_PC14                    ( 78)  /**< Pin Number for PC14 */
#define PIN_PC15                    ( 79)  /**< Pin Number for PC15 */
#define PIN_PC16                    ( 80)  /**< Pin Number for PC16 */
#define PIN_PC17                    ( 81)  /**< Pin Number for PC17 */
#define PIN_PC18                    ( 82)  /**< Pin Number for PC18 */
#define PIN_PC19                    ( 83)  /**< Pin Number for PC19 */
#define PIN_PC20                    ( 84)  /**< Pin Number for PC20 */
#define PIN_PC21                    ( 85)  /**< Pin Number for PC21 */
#define PIN_PC24                    ( 88)  /**< Pin Number for PC24 */
#define PIN_PC25                    ( 89)  /**< Pin Number for PC25 */
#define PIN_PC26                    ( 90)  /**< Pin Number for PC26 */
#define PIN_PC27                    ( 91)  /**< Pin Number for PC27 */
#define PIN_PC28                    ( 92)  /**< Pin Number for PC28 */

/* ========== Peripheral I/O masks ========== */
#define PORT_PA00                    (1UL << 0)  /**< PORT mask for PA00 */
#define PORT_PA01                    (1UL << 1)  /**< PORT mask for PA01 */
#define PORT_PA02                    (1UL << 2)  /**< PORT mask for PA02 */
#define PORT_PA03                    (1UL << 3)  /**< PORT mask for PA03 */
#define PORT_PA04                    (1UL << 4)  /**< PORT mask for PA04 */
#define PORT_PA05                    (1UL << 5)  /**< PORT mask for PA05 */
#define PORT_PA06                    (1UL << 6)  /**< PORT mask for PA06 */
#define PORT_PA07                    (1UL << 7)  /**< PORT mask for PA07 */
#define PORT_PA08                    (1UL << 8)  /**< PORT mask for PA08 */
#define PORT_PA09                    (1UL << 9)  /**< PORT mask for PA09 */
#define PORT_PA10                    (1UL << 10)  /**< PORT mask for PA10 */
#define PORT_PA11                    (1UL << 11)  /**< PORT mask for PA11 */
#define PORT_PA12                    (1UL << 12)  /**< PORT mask for PA12 */
#define PORT_PA13                    (1UL << 13)  /**< PORT mask for PA13 */
#define PORT_PA14                    (1UL << 14)  /**< PORT mask for PA14 */
#define PORT_PA15                    (1UL << 15)  /**< PORT mask for PA15 */
#define PORT_PA16                    (1UL << 16)  /**< PORT mask for PA16 */
#define PORT_PA17                    (1UL << 17)  /**< PORT mask for PA17 */
#define PORT_PA18                    (1UL << 18)  /**< PORT mask for PA18 */
#define PORT_PA19                    (1UL << 19)  /**< PORT mask for PA19 */
#define PORT_PA20                    (1UL << 20)  /**< PORT mask for PA20 */
#define PORT_PA21                    (1UL << 21)  /**< PORT mask for PA21 */
#define PORT_PA22                    (1UL << 22)  /**< PORT mask for PA22 */
#define PORT_PA23                    (1UL << 23)  /**< PORT mask for PA23 */
#define PORT_PA24                    (1UL << 24)  /**< PORT mask for PA24 */
#define PORT_PA25                    (1UL << 25)  /**< PORT mask for PA25 */
#define PORT_PA27                    (1UL << 27)  /**< PORT mask for PA27 */
#define PORT_PA28                    (1UL << 28)  /**< PORT mask for PA28 */
#define PORT_PA30                    (1UL << 30)  /**< PORT mask for PA30 */
#define PORT_PA31                    (1UL << 31)  /**< PORT mask for PA31 */
#define PORT_PB00                    (1UL << 0)  /**< PORT mask for PB00 */
#define PORT_PB01                    (1UL << 1)  /**< PORT mask for PB01 */
#define PORT_PB02                    (1UL << 2)  /**< PORT mask for PB02 */
#define PORT_PB03                    (1UL << 3)  /**< PORT mask for PB03 */
#define PORT_PB04                    (1UL << 4)  /**< PORT mask for PB04 */
#define PORT_PB05                    (1UL << 5)  /**< PORT mask for PB05 */
#define PORT_PB06                    (1UL << 6)  /**< PORT mask for PB06 */
#define PORT_PB07                    (1UL << 7)  /**< PORT mask for PB07 */
#define PORT_PB08                    (1UL << 8)  /**< PORT mask for PB08 */
#define PORT_PB09                    (1UL << 9)  /**< PORT mask for PB09 */
#define PORT_PB10                    (1UL << 10)  /**< PORT mask for PB10 */
#define PORT_PB11                    (1UL << 11)  /**< PORT mask for PB11 */
#define PORT_PB12                    (1UL << 12)  /**< PORT mask for PB12 */
#define PORT_PB13                    (1UL << 13)  /**< PORT mask for PB13 */
#define PORT_PB14                    (1UL << 14)  /**< PORT mask for PB14 */
#define PORT_PB15                    (1UL << 15)  /**< PORT mask for PB15 */
#define PORT_PB16                    (1UL << 16)  /**< PORT mask for PB16 */
#define PORT_PB17                    (1UL << 17)  /**< PORT mask for PB17 */
#define PORT_PB18                    (1UL << 18)  /**< PORT mask for PB18 */
#define PORT_PB19                    (1UL << 19)  /**< PORT mask for PB19 */
#define PORT_PB20                    (1UL << 20)  /**< PORT mask for PB20 */
#define PORT_PB21                    (1UL << 21)  /**< PORT mask for PB21 */
#define PORT_PB22                    (1UL << 22)  /**< PORT mask for PB22 */
#define PORT_PB23                    (1UL << 23)  /**< PORT mask for PB23 */
#define PORT_PB24                    (1UL << 24)  /**< PORT mask for PB24 */
#define PORT_PB25                    (1UL << 25)  /**< PORT mask for PB25 */
#define PORT_PB30                    (1UL << 30)  /**< PORT mask for PB30 */
#define PORT_PB31                    (1UL << 31)  /**< PORT mask for PB31 */
#define PORT_PC00                    (1UL << 0)  /**< PORT mask for PC00 */
#define PORT_PC01                    (1UL << 1)  /**< PORT mask for PC01 */
#define PORT_PC02                    (1UL << 2)  /**< PORT mask for PC02 */
#define PORT_PC03                    (1UL << 3)  /**< PORT mask for PC03 */
#define PORT_PC05                    (1UL << 5)  /**< PORT mask for PC05 */
#define PORT_PC06                    (1UL << 6)  /**< PORT mask for PC06 */
#define PORT_PC07                    (1UL << 7)  /**< PORT mask for PC07 */
#define PORT_PC08                    (1UL << 8)  /**< PORT mask for PC08 */
#define PORT_PC09                    (1UL << 9)  /**< PORT mask for PC09 */
#define PORT_PC10                    (1UL << 10)  /**< PORT mask for PC10 */
#define PORT_PC11                    (1UL << 11)  /**< PORT mask for PC11 */
#define PORT_PC12                    (1UL << 12)  /**< PORT mask for PC12 */
#define PORT_PC13                    (1UL << 13)  /**< PORT mask for PC13 */
#define PORT_PC14                    (1UL << 14)  /**< PORT mask for PC14 */
#define PORT_PC15                    (1UL << 15)  /**< PORT mask for PC15 */
#define PORT_PC16                    (1UL << 16)  /**< PORT mask for PC16 */
#define PORT_PC17                    (1UL << 17)  /**< PORT mask for PC17 */
#define PORT_PC18                    (1UL << 18)  /**< PORT mask for PC18 */
#define PORT_PC19                    (1UL << 19)  /**< PORT mask for PC19 */
#define PORT_PC20                    (1UL << 20)  /**< PORT mask for PC20 */
#define PORT_PC21                    (1UL << 21)  /**< PORT mask for PC21 */
#define PORT_PC24                    (1UL << 24)  /**< PORT mask for PC24 */
#define PORT_PC25                    (1UL << 25)  /**< PORT mask for PC25 */
#define PORT_PC26                    (1UL << 26)  /**< PORT mask for PC26 */
#define PORT_PC27                    (1UL << 27)  /**< PORT mask for PC27 */
#define PORT_PC28                    (1UL << 28)  /**< PORT mask for PC28 */

/* ========== PIO definition for AC peripheral ========== */
#define PIN_PA04B_AC_AIN0                          (4L)         /**< AC signal: AC_AIN0 on PA04 mux B*/
#define MUX_PA04B_AC_AIN0                          (1L)         /**< AC signal line function value: AC_AIN0 */
#define PORT_PA04B_AC_AIN0                         (1UL << 4)   /**< AC signal: ACAIN0 */
#define PIN_PA05B_AC_AIN1                          (5L)         /**< AC signal: AC_AIN1 on PA05 mux B*/
#define MUX_PA05B_AC_AIN1                          (1L)         /**< AC signal line function value: AC_AIN1 */
#define PORT_PA05B_AC_AIN1                         (1UL << 5)   /**< AC signal: ACAIN1 */
#define PIN_PA06B_AC_AIN2                          (6L)         /**< AC signal: AC_AIN2 on PA06 mux B*/
#define MUX_PA06B_AC_AIN2                          (1L)         /**< AC signal line function value: AC_AIN2 */
#define PORT_PA06B_AC_AIN2                         (1UL << 6)   /**< AC signal: ACAIN2 */
#define PIN_PA07B_AC_AIN3                          (7L)         /**< AC signal: AC_AIN3 on PA07 mux B*/
#define MUX_PA07B_AC_AIN3                          (1L)         /**< AC signal line function value: AC_AIN3 */
#define PORT_PA07B_AC_AIN3                         (1UL << 7)   /**< AC signal: ACAIN3 */
#define PIN_PA02B_AC_AIN4                          (2L)         /**< AC signal: AC_AIN4 on PA02 mux B*/
#define MUX_PA02B_AC_AIN4                          (1L)         /**< AC signal line function value: AC_AIN4 */
#define PORT_PA02B_AC_AIN4                         (1UL << 2)   /**< AC signal: ACAIN4 */
#define PIN_PB04B_AC_AIN5                          (36L)        /**< AC signal: AC_AIN5 on PB04 mux B*/
#define MUX_PB04B_AC_AIN5                          (1L)         /**< AC signal line function value: AC_AIN5 */
#define PORT_PB04B_AC_AIN5                         (1UL << 4)   /**< AC signal: ACAIN5 */
#define PIN_PB05B_AC_AIN6                          (37L)        /**< AC signal: AC_AIN6 on PB05 mux B*/
#define MUX_PB05B_AC_AIN6                          (1L)         /**< AC signal line function value: AC_AIN6 */
#define PORT_PB05B_AC_AIN6                         (1UL << 5)   /**< AC signal: ACAIN6 */
#define PIN_PB06B_AC_AIN7                          (38L)        /**< AC signal: AC_AIN7 on PB06 mux B*/
#define MUX_PB06B_AC_AIN7                          (1L)         /**< AC signal line function value: AC_AIN7 */
#define PORT_PB06B_AC_AIN7                         (1UL << 6)   /**< AC signal: ACAIN7 */
#define PIN_PA12H_AC_CMP0                          (12L)        /**< AC signal: AC_CMP0 on PA12 mux H*/
#define MUX_PA12H_AC_CMP0                          (7L)         /**< AC signal line function value: AC_CMP0 */
#define PORT_PA12H_AC_CMP0                         (1UL << 12)  /**< AC signal: ACCMP0 */
#define PIN_PA18H_AC_CMP0                          (18L)        /**< AC signal: AC_CMP0 on PA18 mux H*/
#define MUX_PA18H_AC_CMP0                          (7L)         /**< AC signal line function value: AC_CMP0 */
#define PORT_PA18H_AC_CMP0                         (1UL << 18)  /**< AC signal: ACCMP0 */
#define PIN_PB24H_AC_CMP0                          (56L)        /**< AC signal: AC_CMP0 on PB24 mux H*/
#define MUX_PB24H_AC_CMP0                          (7L)         /**< AC signal line function value: AC_CMP0 */
#define PORT_PB24H_AC_CMP0                         (1UL << 24)  /**< AC signal: ACCMP0 */
#define PIN_PA13H_AC_CMP1                          (13L)        /**< AC signal: AC_CMP1 on PA13 mux H*/
#define MUX_PA13H_AC_CMP1                          (7L)         /**< AC signal line function value: AC_CMP1 */
#define PORT_PA13H_AC_CMP1                         (1UL << 13)  /**< AC signal: ACCMP1 */
#define PIN_PA19H_AC_CMP1                          (19L)        /**< AC signal: AC_CMP1 on PA19 mux H*/
#define MUX_PA19H_AC_CMP1                          (7L)         /**< AC signal line function value: AC_CMP1 */
#define PORT_PA19H_AC_CMP1                         (1UL << 19)  /**< AC signal: ACCMP1 */
#define PIN_PB25H_AC_CMP1                          (57L)        /**< AC signal: AC_CMP1 on PB25 mux H*/
#define MUX_PB25H_AC_CMP1                          (7L)         /**< AC signal line function value: AC_CMP1 */
#define PORT_PB25H_AC_CMP1                         (1UL << 25)  /**< AC signal: ACCMP1 */
#define PIN_PA00H_AC_CMP2                          (0L)         /**< AC signal: AC_CMP2 on PA00 mux H*/
#define MUX_PA00H_AC_CMP2                          (7L)         /**< AC signal line function value: AC_CMP2 */
#define PORT_PA00H_AC_CMP2                         (1UL << 0)   /**< AC signal: ACCMP2 */
#define PIN_PA24H_AC_CMP2                          (24L)        /**< AC signal: AC_CMP2 on PA24 mux H*/
#define MUX_PA24H_AC_CMP2                          (7L)         /**< AC signal line function value: AC_CMP2 */
#define PORT_PA24H_AC_CMP2                         (1UL << 24)  /**< AC signal: ACCMP2 */
#define PIN_PB30H_AC_CMP2                          (62L)        /**< AC signal: AC_CMP2 on PB30 mux H*/
#define MUX_PB30H_AC_CMP2                          (7L)         /**< AC signal line function value: AC_CMP2 */
#define PORT_PB30H_AC_CMP2                         (1UL << 30)  /**< AC signal: ACCMP2 */
#define PIN_PA01H_AC_CMP3                          (1L)         /**< AC signal: AC_CMP3 on PA01 mux H*/
#define MUX_PA01H_AC_CMP3                          (7L)         /**< AC signal line function value: AC_CMP3 */
#define PORT_PA01H_AC_CMP3                         (1UL << 1)   /**< AC signal: ACCMP3 */
#define PIN_PA25H_AC_CMP3                          (25L)        /**< AC signal: AC_CMP3 on PA25 mux H*/
#define MUX_PA25H_AC_CMP3                          (7L)         /**< AC signal line function value: AC_CMP3 */
#define PORT_PA25H_AC_CMP3                         (1UL << 25)  /**< AC signal: ACCMP3 */
#define PIN_PB31H_AC_CMP3                          (63L)        /**< AC signal: AC_CMP3 on PB31 mux H*/
#define MUX_PB31H_AC_CMP3                          (7L)         /**< AC signal line function value: AC_CMP3 */
#define PORT_PB31H_AC_CMP3                         (1UL << 31)  /**< AC signal: ACCMP3 */
/* ========== PIO definition for ADC0 peripheral ========== */
#define PIN_PA02B_ADC0_AIN0                        (2L)         /**< ADC0 signal: ADC0_AIN0 on PA02 mux B*/
#define MUX_PA02B_ADC0_AIN0                        (1L)         /**< ADC0 signal line function value: ADC0_AIN0 */
#define PORT_PA02B_ADC0_AIN0                       (1UL << 2)   /**< ADC0 signal: ADC0AIN0 */
#define PIN_PA03B_ADC0_AIN1                        (3L)         /**< ADC0 signal: ADC0_AIN1 on PA03 mux B*/
#define MUX_PA03B_ADC0_AIN1                        (1L)         /**< ADC0 signal line function value: ADC0_AIN1 */
#define PORT_PA03B_ADC0_AIN1                       (1UL << 3)   /**< ADC0 signal: ADC0AIN1 */
#define PIN_PB08B_ADC0_AIN2                        (40L)        /**< ADC0 signal: ADC0_AIN2 on PB08 mux B*/
#define MUX_PB08B_ADC0_AIN2                        (1L)         /**< ADC0 signal line function value: ADC0_AIN2 */
#define PORT_PB08B_ADC0_AIN2                       (1UL << 8)   /**< ADC0 signal: ADC0AIN2 */
#define PIN_PB09B_ADC0_AIN3                        (41L)        /**< ADC0 signal: ADC0_AIN3 on PB09 mux B*/
#define MUX_PB09B_ADC0_AIN3                        (1L)         /**< ADC0 signal line function value: ADC0_AIN3 */
#define PORT_PB09B_ADC0_AIN3                       (1UL << 9)   /**< ADC0 signal: ADC0AIN3 */
#define PIN_PA04B_ADC0_AIN4                        (4L)         /**< ADC0 signal: ADC0_AIN4 on PA04 mux B*/
#define MUX_PA04B_ADC0_AIN4                        (1L)         /**< ADC0 signal line function value: ADC0_AIN4 */
#define PORT_PA04B_ADC0_AIN4                       (1UL << 4)   /**< ADC0 signal: ADC0AIN4 */
#define PIN_PA05B_ADC0_AIN5                        (5L)         /**< ADC0 signal: ADC0_AIN5 on PA05 mux B*/
#define MUX_PA05B_ADC0_AIN5                        (1L)         /**< ADC0 signal line function value: ADC0_AIN5 */
#define PORT_PA05B_ADC0_AIN5                       (1UL << 5)   /**< ADC0 signal: ADC0AIN5 */
#define PIN_PA06B_ADC0_AIN6                        (6L)         /**< ADC0 signal: ADC0_AIN6 on PA06 mux B*/
#define MUX_PA06B_ADC0_AIN6                        (1L)         /**< ADC0 signal line function value: ADC0_AIN6 */
#define PORT_PA06B_ADC0_AIN6                       (1UL << 6)   /**< ADC0 signal: ADC0AIN6 */
#define PIN_PA07B_ADC0_AIN7                        (7L)         /**< ADC0 signal: ADC0_AIN7 on PA07 mux B*/
#define MUX_PA07B_ADC0_AIN7                        (1L)         /**< ADC0 signal line function value: ADC0_AIN7 */
#define PORT_PA07B_ADC0_AIN7                       (1UL << 7)   /**< ADC0 signal: ADC0AIN7 */
#define PIN_PC00B_ADC0_AIN8                        (64L)        /**< ADC0 signal: ADC0_AIN8 on PC00 mux B*/
#define MUX_PC00B_ADC0_AIN8                        (1L)         /**< ADC0 signal line function value: ADC0_AIN8 */
#define PORT_PC00B_ADC0_AIN8                       (1UL << 0)   /**< ADC0 signal: ADC0AIN8 */
#define PIN_PC01B_ADC0_AIN9                        (65L)        /**< ADC0 signal: ADC0_AIN9 on PC01 mux B*/
#define MUX_PC01B_ADC0_AIN9                        (1L)         /**< ADC0 signal line function value: ADC0_AIN9 */
#define PORT_PC01B_ADC0_AIN9                       (1UL << 1)   /**< ADC0 signal: ADC0AIN9 */
#define PIN_PC02B_ADC0_AIN10                       (66L)        /**< ADC0 signal: ADC0_AIN10 on PC02 mux B*/
#define MUX_PC02B_ADC0_AIN10                       (1L)         /**< ADC0 signal line function value: ADC0_AIN10 */
#define PORT_PC02B_ADC0_AIN10                      (1UL << 2)   /**< ADC0 signal: ADC0AIN10 */
#define PIN_PC03B_ADC0_AIN11                       (67L)        /**< ADC0 signal: ADC0_AIN11 on PC03 mux B*/
#define MUX_PC03B_ADC0_AIN11                       (1L)         /**< ADC0 signal line function value: ADC0_AIN11 */
#define PORT_PC03B_ADC0_AIN11                      (1UL << 3)   /**< ADC0 signal: ADC0AIN11 */
#define PIN_PA03B_ADC0_VREFP                       (3L)         /**< ADC0 signal: ADC0_VREFP on PA03 mux B*/
#define MUX_PA03B_ADC0_VREFP                       (1L)         /**< ADC0 signal line function value: ADC0_VREFP */
#define PORT_PA03B_ADC0_VREFP                      (1UL << 3)   /**< ADC0 signal: ADC0VREFP */
/* ========== PIO definition for ADC1 peripheral ========== */
#define PIN_PB00B_ADC1_AIN0                        (32L)        /**< ADC1 signal: ADC1_AIN0 on PB00 mux B*/
#define MUX_PB00B_ADC1_AIN0                        (1L)         /**< ADC1 signal line function value: ADC1_AIN0 */
#define PORT_PB00B_ADC1_AIN0                       (1UL << 0)   /**< ADC1 signal: ADC1AIN0 */
#define PIN_PB01B_ADC1_AIN1                        (33L)        /**< ADC1 signal: ADC1_AIN1 on PB01 mux B*/
#define MUX_PB01B_ADC1_AIN1                        (1L)         /**< ADC1 signal line function value: ADC1_AIN1 */
#define PORT_PB01B_ADC1_AIN1                       (1UL << 1)   /**< ADC1 signal: ADC1AIN1 */
#define PIN_PB02B_ADC1_AIN2                        (34L)        /**< ADC1 signal: ADC1_AIN2 on PB02 mux B*/
#define MUX_PB02B_ADC1_AIN2                        (1L)         /**< ADC1 signal line function value: ADC1_AIN2 */
#define PORT_PB02B_ADC1_AIN2                       (1UL << 2)   /**< ADC1 signal: ADC1AIN2 */
#define PIN_PB03B_ADC1_AIN3                        (35L)        /**< ADC1 signal: ADC1_AIN3 on PB03 mux B*/
#define MUX_PB03B_ADC1_AIN3                        (1L)         /**< ADC1 signal line function value: ADC1_AIN3 */
#define PORT_PB03B_ADC1_AIN3                       (1UL << 3)   /**< ADC1 signal: ADC1AIN3 */
#define PIN_PB08B_ADC1_AIN4                        (40L)        /**< ADC1 signal: ADC1_AIN4 on PB08 mux B*/
#define MUX_PB08B_ADC1_AIN4                        (1L)         /**< ADC1 signal line function value: ADC1_AIN4 */
#define PORT_PB08B_ADC1_AIN4                       (1UL << 8)   /**< ADC1 signal: ADC1AIN4 */
#define PIN_PB09B_ADC1_AIN5                        (41L)        /**< ADC1 signal: ADC1_AIN5 on PB09 mux B*/
#define MUX_PB09B_ADC1_AIN5                        (1L)         /**< ADC1 signal line function value: ADC1_AIN5 */
#define PORT_PB09B_ADC1_AIN5                       (1UL << 9)   /**< ADC1 signal: ADC1AIN5 */
#define PIN_PB04B_ADC1_AIN6                        (36L)        /**< ADC1 signal: ADC1_AIN6 on PB04 mux B*/
#define MUX_PB04B_ADC1_AIN6                        (1L)         /**< ADC1 signal line function value: ADC1_AIN6 */
#define PORT_PB04B_ADC1_AIN6                       (1UL << 4)   /**< ADC1 signal: ADC1AIN6 */
#define PIN_PB05B_ADC1_AIN7                        (37L)        /**< ADC1 signal: ADC1_AIN7 on PB05 mux B*/
#define MUX_PB05B_ADC1_AIN7                        (1L)         /**< ADC1 signal line function value: ADC1_AIN7 */
#define PORT_PB05B_ADC1_AIN7                       (1UL << 5)   /**< ADC1 signal: ADC1AIN7 */
#define PIN_PB06B_ADC1_AIN8                        (38L)        /**< ADC1 signal: ADC1_AIN8 on PB06 mux B*/
#define MUX_PB06B_ADC1_AIN8                        (1L)         /**< ADC1 signal line function value: ADC1_AIN8 */
#define PORT_PB06B_ADC1_AIN8                       (1UL << 6)   /**< ADC1 signal: ADC1AIN8 */
#define PIN_PB07B_ADC1_AIN9                        (39L)        /**< ADC1 signal: ADC1_AIN9 on PB07 mux B*/
#define MUX_PB07B_ADC1_AIN9                        (1L)         /**< ADC1 signal line function value: ADC1_AIN9 */
#define PORT_PB07B_ADC1_AIN9                       (1UL << 7)   /**< ADC1 signal: ADC1AIN9 */
#define PIN_PA08B_ADC1_AIN10                       (8L)         /**< ADC1 signal: ADC1_AIN10 on PA08 mux B*/
#define MUX_PA08B_ADC1_AIN10                       (1L)         /**< ADC1 signal line function value: ADC1_AIN10 */
#define PORT_PA08B_ADC1_AIN10                      (1UL << 8)   /**< ADC1 signal: ADC1AIN10 */
#define PIN_PA09B_ADC1_AIN11                       (9L)         /**< ADC1 signal: ADC1_AIN11 on PA09 mux B*/
#define MUX_PA09B_ADC1_AIN11                       (1L)         /**< ADC1 signal line function value: ADC1_AIN11 */
#define PORT_PA09B_ADC1_AIN11                      (1UL << 9)   /**< ADC1 signal: ADC1AIN11 */
/* ========== PIO definition for CAN0 peripheral ========== */
#define PIN_PA23G_CAN0_RX                          (23L)        /**< CAN0 signal: CAN0_RX on PA23 mux G*/
#define MUX_PA23G_CAN0_RX                          (6L)         /**< CAN0 signal line function value: CAN0_RX */
#define PORT_PA23G_CAN0_RX                         (1UL << 23)  /**< CAN0 signal: CAN0RX */
#define PIN_PA25G_CAN0_RX                          (25L)        /**< CAN0 signal: CAN0_RX on PA25 mux G*/
#define MUX_PA25G_CAN0_RX                          (6L)         /**< CAN0 signal line function value: CAN0_RX */
#define PORT_PA25G_CAN0_RX                         (1UL << 25)  /**< CAN0 signal: CAN0RX */
#define PIN_PA22G_CAN0_TX                          (22L)        /**< CAN0 signal: CAN0_TX on PA22 mux G*/
#define MUX_PA22G_CAN0_TX                          (6L)         /**< CAN0 signal line function value: CAN0_TX */
#define PORT_PA22G_CAN0_TX                         (1UL << 22)  /**< CAN0 signal: CAN0TX */
#define PIN_PA24G_CAN0_TX                          (24L)        /**< CAN0 signal: CAN0_TX on PA24 mux G*/
#define MUX_PA24G_CAN0_TX                          (6L)         /**< CAN0 signal line function value: CAN0_TX */
#define PORT_PA24G_CAN0_TX                         (1UL << 24)  /**< CAN0 signal: CAN0TX */
/* ========== PIO definition for CAN1 peripheral ========== */
#define PIN_PB13G_CAN1_RX                          (45L)        /**< CAN1 signal: CAN1_RX on PB13 mux G*/
#define MUX_PB13G_CAN1_RX                          (6L)         /**< CAN1 signal line function value: CAN1_RX */
#define PORT_PB13G_CAN1_RX                         (1UL << 13)  /**< CAN1 signal: CAN1RX */
#define PIN_PB15G_CAN1_RX                          (47L)        /**< CAN1 signal: CAN1_RX on PB15 mux G*/
#define MUX_PB15G_CAN1_RX                          (6L)         /**< CAN1 signal line function value: CAN1_RX */
#define PORT_PB15G_CAN1_RX                         (1UL << 15)  /**< CAN1 signal: CAN1RX */
#define PIN_PB12G_CAN1_TX                          (44L)        /**< CAN1 signal: CAN1_TX on PB12 mux G*/
#define MUX_PB12G_CAN1_TX                          (6L)         /**< CAN1 signal line function value: CAN1_TX */
#define PORT_PB12G_CAN1_TX                         (1UL << 12)  /**< CAN1 signal: CAN1TX */
#define PIN_PB14G_CAN1_TX                          (46L)        /**< CAN1 signal: CAN1_TX on PB14 mux G*/
#define MUX_PB14G_CAN1_TX                          (6L)         /**< CAN1 signal line function value: CAN1_TX */
#define PORT_PB14G_CAN1_TX                         (1UL << 14)  /**< CAN1 signal: CAN1TX */
/* ========== PIO definition for CCL peripheral ========== */
#define PIN_PA04I_CCL_IN0                          (4L)         /**< CCL signal: CCL_IN0 on PA04 mux I*/
#define MUX_PA04I_CCL_IN0                          (8L)         /**< CCL signal line function value: CCL_IN0 */
#define PORT_PA04I_CCL_IN0                         (1UL << 4)   /**< CCL signal: CCLIN0 */
#define PIN_PA16I_CCL_IN0                          (16L)        /**< CCL signal: CCL_IN0 on PA16 mux I*/
#define MUX_PA16I_CCL_IN0                          (8L)         /**< CCL signal line function value: CCL_IN0 */
#define PORT_PA16I_CCL_IN0                         (1UL << 16)  /**< CCL signal: CCLIN0 */
#define PIN_PB22I_CCL_IN0                          (54L)        /**< CCL signal: CCL_IN0 on PB22 mux I*/
#define MUX_PB22I_CCL_IN0                          (8L)         /**< CCL signal line function value: CCL_IN0 */
#define PORT_PB22I_CCL_IN0                         (1UL << 22)  /**< CCL signal: CCLIN0 */
#define PIN_PA05I_CCL_IN1                          (5L)         /**< CCL signal: CCL_IN1 on PA05 mux I*/
#define MUX_PA05I_CCL_IN1                          (8L)         /**< CCL signal line function value: CCL_IN1 */
#define PORT_PA05I_CCL_IN1                         (1UL << 5)   /**< CCL signal: CCLIN1 */
#define PIN_PA17I_CCL_IN1                          (17L)        /**< CCL signal: CCL_IN1 on PA17 mux I*/
#define MUX_PA17I_CCL_IN1                          (8L)         /**< CCL signal line function value: CCL_IN1 */
#define PORT_PA17I_CCL_IN1                         (1UL << 17)  /**< CCL signal: CCLIN1 */
#define PIN_PB00I_CCL_IN1                          (32L)        /**< CCL signal: CCL_IN1 on PB00 mux I*/
#define MUX_PB00I_CCL_IN1                          (8L)         /**< CCL signal line function value: CCL_IN1 */
#define PORT_PB00I_CCL_IN1                         (1UL << 0)   /**< CCL signal: CCLIN1 */
#define PIN_PA06I_CCL_IN2                          (6L)         /**< CCL signal: CCL_IN2 on PA06 mux I*/
#define MUX_PA06I_CCL_IN2                          (8L)         /**< CCL signal line function value: CCL_IN2 */
#define PORT_PA06I_CCL_IN2                         (1UL << 6)   /**< CCL signal: CCLIN2 */
#define PIN_PA18I_CCL_IN2                          (18L)        /**< CCL signal: CCL_IN2 on PA18 mux I*/
#define MUX_PA18I_CCL_IN2                          (8L)         /**< CCL signal line function value: CCL_IN2 */
#define PORT_PA18I_CCL_IN2                         (1UL << 18)  /**< CCL signal: CCLIN2 */
#define PIN_PB01I_CCL_IN2                          (33L)        /**< CCL signal: CCL_IN2 on PB01 mux I*/
#define MUX_PB01I_CCL_IN2                          (8L)         /**< CCL signal line function value: CCL_IN2 */
#define PORT_PB01I_CCL_IN2                         (1UL << 1)   /**< CCL signal: CCLIN2 */
#define PIN_PA08I_CCL_IN3                          (8L)         /**< CCL signal: CCL_IN3 on PA08 mux I*/
#define MUX_PA08I_CCL_IN3                          (8L)         /**< CCL signal line function value: CCL_IN3 */
#define PORT_PA08I_CCL_IN3                         (1UL << 8)   /**< CCL signal: CCLIN3 */
#define PIN_PA30I_CCL_IN3                          (30L)        /**< CCL signal: CCL_IN3 on PA30 mux I*/
#define MUX_PA30I_CCL_IN3                          (8L)         /**< CCL signal line function value: CCL_IN3 */
#define PORT_PA30I_CCL_IN3                         (1UL << 30)  /**< CCL signal: CCLIN3 */
#define PIN_PA09I_CCL_IN4                          (9L)         /**< CCL signal: CCL_IN4 on PA09 mux I*/
#define MUX_PA09I_CCL_IN4                          (8L)         /**< CCL signal line function value: CCL_IN4 */
#define PORT_PA09I_CCL_IN4                         (1UL << 9)   /**< CCL signal: CCLIN4 */
#define PIN_PC27I_CCL_IN4                          (91L)        /**< CCL signal: CCL_IN4 on PC27 mux I*/
#define MUX_PC27I_CCL_IN4                          (8L)         /**< CCL signal line function value: CCL_IN4 */
#define PORT_PC27I_CCL_IN4                         (1UL << 27)  /**< CCL signal: CCLIN4 */
#define PIN_PA10I_CCL_IN5                          (10L)        /**< CCL signal: CCL_IN5 on PA10 mux I*/
#define MUX_PA10I_CCL_IN5                          (8L)         /**< CCL signal line function value: CCL_IN5 */
#define PORT_PA10I_CCL_IN5                         (1UL << 10)  /**< CCL signal: CCLIN5 */
#define PIN_PB10I_CCL_IN5                          (42L)        /**< CCL signal: CCL_IN5 on PB10 mux I*/
#define MUX_PB10I_CCL_IN5                          (8L)         /**< CCL signal line function value: CCL_IN5 */
#define PORT_PB10I_CCL_IN5                         (1UL << 10)  /**< CCL signal: CCLIN5 */
#define PIN_PC28I_CCL_IN5                          (92L)        /**< CCL signal: CCL_IN5 on PC28 mux I*/
#define MUX_PC28I_CCL_IN5                          (8L)         /**< CCL signal line function value: CCL_IN5 */
#define PORT_PC28I_CCL_IN5                         (1UL << 28)  /**< CCL signal: CCLIN5 */
#define PIN_PA22I_CCL_IN6                          (22L)        /**< CCL signal: CCL_IN6 on PA22 mux I*/
#define MUX_PA22I_CCL_IN6                          (8L)         /**< CCL signal line function value: CCL_IN6 */
#define PORT_PA22I_CCL_IN6                         (1UL << 22)  /**< CCL signal: CCLIN6 */
#define PIN_PB06I_CCL_IN6                          (38L)        /**< CCL signal: CCL_IN6 on PB06 mux I*/
#define MUX_PB06I_CCL_IN6                          (8L)         /**< CCL signal line function value: CCL_IN6 */
#define PORT_PB06I_CCL_IN6                         (1UL << 6)   /**< CCL signal: CCLIN6 */
#define PIN_PB07I_CCL_IN7                          (39L)        /**< CCL signal: CCL_IN7 on PB07 mux I*/
#define MUX_PB07I_CCL_IN7                          (8L)         /**< CCL signal line function value: CCL_IN7 */
#define PORT_PB07I_CCL_IN7                         (1UL << 7)   /**< CCL signal: CCLIN7 */
#define PIN_PA23I_CCL_IN7                          (23L)        /**< CCL signal: CCL_IN7 on PA23 mux I*/
#define MUX_PA23I_CCL_IN7                          (8L)         /**< CCL signal line function value: CCL_IN7 */
#define PORT_PA23I_CCL_IN7                         (1UL << 23)  /**< CCL signal: CCLIN7 */
#define PIN_PB08I_CCL_IN8                          (40L)        /**< CCL signal: CCL_IN8 on PB08 mux I*/
#define MUX_PB08I_CCL_IN8                          (8L)         /**< CCL signal line function value: CCL_IN8 */
#define PORT_PB08I_CCL_IN8                         (1UL << 8)   /**< CCL signal: CCLIN8 */
#define PIN_PA24I_CCL_IN8                          (24L)        /**< CCL signal: CCL_IN8 on PA24 mux I*/
#define MUX_PA24I_CCL_IN8                          (8L)         /**< CCL signal line function value: CCL_IN8 */
#define PORT_PA24I_CCL_IN8                         (1UL << 24)  /**< CCL signal: CCLIN8 */
#define PIN_PB14I_CCL_IN9                          (46L)        /**< CCL signal: CCL_IN9 on PB14 mux I*/
#define MUX_PB14I_CCL_IN9                          (8L)         /**< CCL signal line function value: CCL_IN9 */
#define PORT_PB14I_CCL_IN9                         (1UL << 14)  /**< CCL signal: CCLIN9 */
#define PIN_PC20I_CCL_IN9                          (84L)        /**< CCL signal: CCL_IN9 on PC20 mux I*/
#define MUX_PC20I_CCL_IN9                          (8L)         /**< CCL signal line function value: CCL_IN9 */
#define PORT_PC20I_CCL_IN9                         (1UL << 20)  /**< CCL signal: CCLIN9 */
#define PIN_PB15I_CCL_IN10                         (47L)        /**< CCL signal: CCL_IN10 on PB15 mux I*/
#define MUX_PB15I_CCL_IN10                         (8L)         /**< CCL signal line function value: CCL_IN10 */
#define PORT_PB15I_CCL_IN10                        (1UL << 15)  /**< CCL signal: CCLIN10 */
#define PIN_PC21I_CCL_IN10                         (85L)        /**< CCL signal: CCL_IN10 on PC21 mux I*/
#define MUX_PC21I_CCL_IN10                         (8L)         /**< CCL signal line function value: CCL_IN10 */
#define PORT_PC21I_CCL_IN10                        (1UL << 21)  /**< CCL signal: CCLIN10 */
#define PIN_PB16I_CCL_IN11                         (48L)        /**< CCL signal: CCL_IN11 on PB16 mux I*/
#define MUX_PB16I_CCL_IN11                         (8L)         /**< CCL signal line function value: CCL_IN11 */
#define PORT_PB16I_CCL_IN11                        (1UL << 16)  /**< CCL signal: CCLIN11 */
#define PIN_PA07I_CCL_OUT0                         (7L)         /**< CCL signal: CCL_OUT0 on PA07 mux I*/
#define MUX_PA07I_CCL_OUT0                         (8L)         /**< CCL signal line function value: CCL_OUT0 */
#define PORT_PA07I_CCL_OUT0                        (1UL << 7)   /**< CCL signal: CCLOUT0 */
#define PIN_PA19I_CCL_OUT0                         (19L)        /**< CCL signal: CCL_OUT0 on PA19 mux I*/
#define MUX_PA19I_CCL_OUT0                         (8L)         /**< CCL signal line function value: CCL_OUT0 */
#define PORT_PA19I_CCL_OUT0                        (1UL << 19)  /**< CCL signal: CCLOUT0 */
#define PIN_PB02I_CCL_OUT0                         (34L)        /**< CCL signal: CCL_OUT0 on PB02 mux I*/
#define MUX_PB02I_CCL_OUT0                         (8L)         /**< CCL signal line function value: CCL_OUT0 */
#define PORT_PB02I_CCL_OUT0                        (1UL << 2)   /**< CCL signal: CCLOUT0 */
#define PIN_PB23I_CCL_OUT0                         (55L)        /**< CCL signal: CCL_OUT0 on PB23 mux I*/
#define MUX_PB23I_CCL_OUT0                         (8L)         /**< CCL signal line function value: CCL_OUT0 */
#define PORT_PB23I_CCL_OUT0                        (1UL << 23)  /**< CCL signal: CCLOUT0 */
#define PIN_PA11I_CCL_OUT1                         (11L)        /**< CCL signal: CCL_OUT1 on PA11 mux I*/
#define MUX_PA11I_CCL_OUT1                         (8L)         /**< CCL signal line function value: CCL_OUT1 */
#define PORT_PA11I_CCL_OUT1                        (1UL << 11)  /**< CCL signal: CCLOUT1 */
#define PIN_PA31I_CCL_OUT1                         (31L)        /**< CCL signal: CCL_OUT1 on PA31 mux I*/
#define MUX_PA31I_CCL_OUT1                         (8L)         /**< CCL signal line function value: CCL_OUT1 */
#define PORT_PA31I_CCL_OUT1                        (1UL << 31)  /**< CCL signal: CCLOUT1 */
#define PIN_PB11I_CCL_OUT1                         (43L)        /**< CCL signal: CCL_OUT1 on PB11 mux I*/
#define MUX_PB11I_CCL_OUT1                         (8L)         /**< CCL signal line function value: CCL_OUT1 */
#define PORT_PB11I_CCL_OUT1                        (1UL << 11)  /**< CCL signal: CCLOUT1 */
#define PIN_PA25I_CCL_OUT2                         (25L)        /**< CCL signal: CCL_OUT2 on PA25 mux I*/
#define MUX_PA25I_CCL_OUT2                         (8L)         /**< CCL signal line function value: CCL_OUT2 */
#define PORT_PA25I_CCL_OUT2                        (1UL << 25)  /**< CCL signal: CCLOUT2 */
#define PIN_PB09I_CCL_OUT2                         (41L)        /**< CCL signal: CCL_OUT2 on PB09 mux I*/
#define MUX_PB09I_CCL_OUT2                         (8L)         /**< CCL signal line function value: CCL_OUT2 */
#define PORT_PB09I_CCL_OUT2                        (1UL << 9)   /**< CCL signal: CCLOUT2 */
#define PIN_PB17I_CCL_OUT3                         (49L)        /**< CCL signal: CCL_OUT3 on PB17 mux I*/
#define MUX_PB17I_CCL_OUT3                         (8L)         /**< CCL signal line function value: CCL_OUT3 */
#define PORT_PB17I_CCL_OUT3                        (1UL << 17)  /**< CCL signal: CCLOUT3 */
/* ========== PIO definition for DAC peripheral ========== */
#define PIN_PA02B_DAC_VOUT                         (2L)         /**< DAC signal: DAC_VOUT on PA02 mux B*/
#define MUX_PA02B_DAC_VOUT                         (1L)         /**< DAC signal line function value: DAC_VOUT */
#define PORT_PA02B_DAC_VOUT                        (1UL << 2)   /**< DAC signal: DACVOUT */
#define PIN_PA03B_DAC_VREFP                        (3L)         /**< DAC signal: DAC_VREFP on PA03 mux B*/
#define MUX_PA03B_DAC_VREFP                        (1L)         /**< DAC signal line function value: DAC_VREFP */
#define PORT_PA03B_DAC_VREFP                       (1UL << 3)   /**< DAC signal: DACVREFP */
/* ========== PIO definition for EIC peripheral ========== */
#define PIN_PA16A_EIC_EXTINT0                      (16L)        /**< EIC signal: EIC_EXTINT0 on PA16 mux A*/
#define MUX_PA16A_EIC_EXTINT0                      (0L)         /**< EIC signal line function value: EIC_EXTINT0 */
#define PORT_PA16A_EIC_EXTINT0                     (1UL << 16)  /**< EIC signal: EICEXTINT0 */
#define PIN_PB00A_EIC_EXTINT0                      (32L)        /**< EIC signal: EIC_EXTINT0 on PB00 mux A*/
#define MUX_PB00A_EIC_EXTINT0                      (0L)         /**< EIC signal line function value: EIC_EXTINT0 */
#define PORT_PB00A_EIC_EXTINT0                     (1UL << 0)   /**< EIC signal: EICEXTINT0 */
#define PIN_PB16A_EIC_EXTINT0                      (48L)        /**< EIC signal: EIC_EXTINT0 on PB16 mux A*/
#define MUX_PB16A_EIC_EXTINT0                      (0L)         /**< EIC signal line function value: EIC_EXTINT0 */
#define PORT_PB16A_EIC_EXTINT0                     (1UL << 16)  /**< EIC signal: EICEXTINT0 */
#define PIN_PC08A_EIC_EXTINT0                      (72L)        /**< EIC signal: EIC_EXTINT0 on PC08 mux A*/
#define MUX_PC08A_EIC_EXTINT0                      (0L)         /**< EIC signal line function value: EIC_EXTINT0 */
#define PORT_PC08A_EIC_EXTINT0                     (1UL << 8)   /**< EIC signal: EICEXTINT0 */
#define PIN_PC24A_EIC_EXTINT0                      (88L)        /**< EIC signal: EIC_EXTINT0 on PC24 mux A*/
#define MUX_PC24A_EIC_EXTINT0                      (0L)         /**< EIC signal line function value: EIC_EXTINT0 */
#define PORT_PC24A_EIC_EXTINT0                     (1UL << 24)  /**< EIC signal: EICEXTINT0 */
#define PIN_PA00A_EIC_EXTINT0                      (0L)         /**< EIC signal: EIC_EXTINT0 on PA00 mux A*/
#define MUX_PA00A_EIC_EXTINT0                      (0L)         /**< EIC signal line function value: EIC_EXTINT0 */
#define PORT_PA00A_EIC_EXTINT0                     (1UL << 0)   /**< EIC signal: EICEXTINT0 */
#define PIN_PA17A_EIC_EXTINT1                      (17L)        /**< EIC signal: EIC_EXTINT1 on PA17 mux A*/
#define MUX_PA17A_EIC_EXTINT1                      (0L)         /**< EIC signal line function value: EIC_EXTINT1 */
#define PORT_PA17A_EIC_EXTINT1                     (1UL << 17)  /**< EIC signal: EICEXTINT1 */
#define PIN_PB01A_EIC_EXTINT1                      (33L)        /**< EIC signal: EIC_EXTINT1 on PB01 mux A*/
#define MUX_PB01A_EIC_EXTINT1                      (0L)         /**< EIC signal line function value: EIC_EXTINT1 */
#define PORT_PB01A_EIC_EXTINT1                     (1UL << 1)   /**< EIC signal: EICEXTINT1 */
#define PIN_PB17A_EIC_EXTINT1                      (49L)        /**< EIC signal: EIC_EXTINT1 on PB17 mux A*/
#define MUX_PB17A_EIC_EXTINT1                      (0L)         /**< EIC signal line function value: EIC_EXTINT1 */
#define PORT_PB17A_EIC_EXTINT1                     (1UL << 17)  /**< EIC signal: EICEXTINT1 */
#define PIN_PC09A_EIC_EXTINT1                      (73L)        /**< EIC signal: EIC_EXTINT1 on PC09 mux A*/
#define MUX_PC09A_EIC_EXTINT1                      (0L)         /**< EIC signal line function value: EIC_EXTINT1 */
#define PORT_PC09A_EIC_EXTINT1                     (1UL << 9)   /**< EIC signal: EICEXTINT1 */
#define PIN_PC25A_EIC_EXTINT1                      (89L)        /**< EIC signal: EIC_EXTINT1 on PC25 mux A*/
#define MUX_PC25A_EIC_EXTINT1                      (0L)         /**< EIC signal line function value: EIC_EXTINT1 */
#define PORT_PC25A_EIC_EXTINT1                     (1UL << 25)  /**< EIC signal: EICEXTINT1 */
#define PIN_PA01A_EIC_EXTINT1                      (1L)         /**< EIC signal: EIC_EXTINT1 on PA01 mux A*/
#define MUX_PA01A_EIC_EXTINT1                      (0L)         /**< EIC signal line function value: EIC_EXTINT1 */
#define PORT_PA01A_EIC_EXTINT1                     (1UL << 1)   /**< EIC signal: EICEXTINT1 */
#define PIN_PA02A_EIC_EXTINT2                      (2L)         /**< EIC signal: EIC_EXTINT2 on PA02 mux A*/
#define MUX_PA02A_EIC_EXTINT2                      (0L)         /**< EIC signal line function value: EIC_EXTINT2 */
#define PORT_PA02A_EIC_EXTINT2                     (1UL << 2)   /**< EIC signal: EICEXTINT2 */
#define PIN_PA18A_EIC_EXTINT2                      (18L)        /**< EIC signal: EIC_EXTINT2 on PA18 mux A*/
#define MUX_PA18A_EIC_EXTINT2                      (0L)         /**< EIC signal line function value: EIC_EXTINT2 */
#define PORT_PA18A_EIC_EXTINT2                     (1UL << 18)  /**< EIC signal: EICEXTINT2 */
#define PIN_PB02A_EIC_EXTINT2                      (34L)        /**< EIC signal: EIC_EXTINT2 on PB02 mux A*/
#define MUX_PB02A_EIC_EXTINT2                      (0L)         /**< EIC signal line function value: EIC_EXTINT2 */
#define PORT_PB02A_EIC_EXTINT2                     (1UL << 2)   /**< EIC signal: EICEXTINT2 */
#define PIN_PB18A_EIC_EXTINT2                      (50L)        /**< EIC signal: EIC_EXTINT2 on PB18 mux A*/
#define MUX_PB18A_EIC_EXTINT2                      (0L)         /**< EIC signal line function value: EIC_EXTINT2 */
#define PORT_PB18A_EIC_EXTINT2                     (1UL << 18)  /**< EIC signal: EICEXTINT2 */
#define PIN_PC10A_EIC_EXTINT2                      (74L)        /**< EIC signal: EIC_EXTINT2 on PC10 mux A*/
#define MUX_PC10A_EIC_EXTINT2                      (0L)         /**< EIC signal line function value: EIC_EXTINT2 */
#define PORT_PC10A_EIC_EXTINT2                     (1UL << 10)  /**< EIC signal: EICEXTINT2 */
#define PIN_PC26A_EIC_EXTINT2                      (90L)        /**< EIC signal: EIC_EXTINT2 on PC26 mux A*/
#define MUX_PC26A_EIC_EXTINT2                      (0L)         /**< EIC signal line function value: EIC_EXTINT2 */
#define PORT_PC26A_EIC_EXTINT2                     (1UL << 26)  /**< EIC signal: EICEXTINT2 */
#define PIN_PA03A_EIC_EXTINT3                      (3L)         /**< EIC signal: EIC_EXTINT3 on PA03 mux A*/
#define MUX_PA03A_EIC_EXTINT3                      (0L)         /**< EIC signal line function value: EIC_EXTINT3 */
#define PORT_PA03A_EIC_EXTINT3                     (1UL << 3)   /**< EIC signal: EICEXTINT3 */
#define PIN_PA19A_EIC_EXTINT3                      (19L)        /**< EIC signal: EIC_EXTINT3 on PA19 mux A*/
#define MUX_PA19A_EIC_EXTINT3                      (0L)         /**< EIC signal line function value: EIC_EXTINT3 */
#define PORT_PA19A_EIC_EXTINT3                     (1UL << 19)  /**< EIC signal: EICEXTINT3 */
#define PIN_PB03A_EIC_EXTINT3                      (35L)        /**< EIC signal: EIC_EXTINT3 on PB03 mux A*/
#define MUX_PB03A_EIC_EXTINT3                      (0L)         /**< EIC signal line function value: EIC_EXTINT3 */
#define PORT_PB03A_EIC_EXTINT3                     (1UL << 3)   /**< EIC signal: EICEXTINT3 */
#define PIN_PB19A_EIC_EXTINT3                      (51L)        /**< EIC signal: EIC_EXTINT3 on PB19 mux A*/
#define MUX_PB19A_EIC_EXTINT3                      (0L)         /**< EIC signal line function value: EIC_EXTINT3 */
#define PORT_PB19A_EIC_EXTINT3                     (1UL << 19)  /**< EIC signal: EICEXTINT3 */
#define PIN_PC11A_EIC_EXTINT3                      (75L)        /**< EIC signal: EIC_EXTINT3 on PC11 mux A*/
#define MUX_PC11A_EIC_EXTINT3                      (0L)         /**< EIC signal line function value: EIC_EXTINT3 */
#define PORT_PC11A_EIC_EXTINT3                     (1UL << 11)  /**< EIC signal: EICEXTINT3 */
#define PIN_PC27A_EIC_EXTINT3                      (91L)        /**< EIC signal: EIC_EXTINT3 on PC27 mux A*/
#define MUX_PC27A_EIC_EXTINT3                      (0L)         /**< EIC signal line function value: EIC_EXTINT3 */
#define PORT_PC27A_EIC_EXTINT3                     (1UL << 27)  /**< EIC signal: EICEXTINT3 */
#define PIN_PA04A_EIC_EXTINT4                      (4L)         /**< EIC signal: EIC_EXTINT4 on PA04 mux A*/
#define MUX_PA04A_EIC_EXTINT4                      (0L)         /**< EIC signal line function value: EIC_EXTINT4 */
#define PORT_PA04A_EIC_EXTINT4                     (1UL << 4)   /**< EIC signal: EICEXTINT4 */
#define PIN_PA20A_EIC_EXTINT4                      (20L)        /**< EIC signal: EIC_EXTINT4 on PA20 mux A*/
#define MUX_PA20A_EIC_EXTINT4                      (0L)         /**< EIC signal line function value: EIC_EXTINT4 */
#define PORT_PA20A_EIC_EXTINT4                     (1UL << 20)  /**< EIC signal: EICEXTINT4 */
#define PIN_PB04A_EIC_EXTINT4                      (36L)        /**< EIC signal: EIC_EXTINT4 on PB04 mux A*/
#define MUX_PB04A_EIC_EXTINT4                      (0L)         /**< EIC signal line function value: EIC_EXTINT4 */
#define PORT_PB04A_EIC_EXTINT4                     (1UL << 4)   /**< EIC signal: EICEXTINT4 */
#define PIN_PB20A_EIC_EXTINT4                      (52L)        /**< EIC signal: EIC_EXTINT4 on PB20 mux A*/
#define MUX_PB20A_EIC_EXTINT4                      (0L)         /**< EIC signal line function value: EIC_EXTINT4 */
#define PORT_PB20A_EIC_EXTINT4                     (1UL << 20)  /**< EIC signal: EICEXTINT4 */
#define PIN_PC12A_EIC_EXTINT4                      (76L)        /**< EIC signal: EIC_EXTINT4 on PC12 mux A*/
#define MUX_PC12A_EIC_EXTINT4                      (0L)         /**< EIC signal line function value: EIC_EXTINT4 */
#define PORT_PC12A_EIC_EXTINT4                     (1UL << 12)  /**< EIC signal: EICEXTINT4 */
#define PIN_PC28A_EIC_EXTINT4                      (92L)        /**< EIC signal: EIC_EXTINT4 on PC28 mux A*/
#define MUX_PC28A_EIC_EXTINT4                      (0L)         /**< EIC signal line function value: EIC_EXTINT4 */
#define PORT_PC28A_EIC_EXTINT4                     (1UL << 28)  /**< EIC signal: EICEXTINT4 */
#define PIN_PA05A_EIC_EXTINT5                      (5L)         /**< EIC signal: EIC_EXTINT5 on PA05 mux A*/
#define MUX_PA05A_EIC_EXTINT5                      (0L)         /**< EIC signal line function value: EIC_EXTINT5 */
#define PORT_PA05A_EIC_EXTINT5                     (1UL << 5)   /**< EIC signal: EICEXTINT5 */
#define PIN_PA21A_EIC_EXTINT5                      (21L)        /**< EIC signal: EIC_EXTINT5 on PA21 mux A*/
#define MUX_PA21A_EIC_EXTINT5                      (0L)         /**< EIC signal line function value: EIC_EXTINT5 */
#define PORT_PA21A_EIC_EXTINT5                     (1UL << 21)  /**< EIC signal: EICEXTINT5 */
#define PIN_PB05A_EIC_EXTINT5                      (37L)        /**< EIC signal: EIC_EXTINT5 on PB05 mux A*/
#define MUX_PB05A_EIC_EXTINT5                      (0L)         /**< EIC signal line function value: EIC_EXTINT5 */
#define PORT_PB05A_EIC_EXTINT5                     (1UL << 5)   /**< EIC signal: EICEXTINT5 */
#define PIN_PB21A_EIC_EXTINT5                      (53L)        /**< EIC signal: EIC_EXTINT5 on PB21 mux A*/
#define MUX_PB21A_EIC_EXTINT5                      (0L)         /**< EIC signal line function value: EIC_EXTINT5 */
#define PORT_PB21A_EIC_EXTINT5                     (1UL << 21)  /**< EIC signal: EICEXTINT5 */
#define PIN_PC13A_EIC_EXTINT5                      (77L)        /**< EIC signal: EIC_EXTINT5 on PC13 mux A*/
#define MUX_PC13A_EIC_EXTINT5                      (0L)         /**< EIC signal line function value: EIC_EXTINT5 */
#define PORT_PC13A_EIC_EXTINT5                     (1UL << 13)  /**< EIC signal: EICEXTINT5 */
#define PIN_PA06A_EIC_EXTINT6                      (6L)         /**< EIC signal: EIC_EXTINT6 on PA06 mux A*/
#define MUX_PA06A_EIC_EXTINT6                      (0L)         /**< EIC signal line function value: EIC_EXTINT6 */
#define PORT_PA06A_EIC_EXTINT6                     (1UL << 6)   /**< EIC signal: EICEXTINT6 */
#define PIN_PA22A_EIC_EXTINT6                      (22L)        /**< EIC signal: EIC_EXTINT6 on PA22 mux A*/
#define MUX_PA22A_EIC_EXTINT6                      (0L)         /**< EIC signal line function value: EIC_EXTINT6 */
#define PORT_PA22A_EIC_EXTINT6                     (1UL << 22)  /**< EIC signal: EICEXTINT6 */
#define PIN_PB06A_EIC_EXTINT6                      (38L)        /**< EIC signal: EIC_EXTINT6 on PB06 mux A*/
#define MUX_PB06A_EIC_EXTINT6                      (0L)         /**< EIC signal line function value: EIC_EXTINT6 */
#define PORT_PB06A_EIC_EXTINT6                     (1UL << 6)   /**< EIC signal: EICEXTINT6 */
#define PIN_PB22A_EIC_EXTINT6                      (54L)        /**< EIC signal: EIC_EXTINT6 on PB22 mux A*/
#define MUX_PB22A_EIC_EXTINT6                      (0L)         /**< EIC signal line function value: EIC_EXTINT6 */
#define PORT_PB22A_EIC_EXTINT6                     (1UL << 22)  /**< EIC signal: EICEXTINT6 */
#define PIN_PC14A_EIC_EXTINT6                      (78L)        /**< EIC signal: EIC_EXTINT6 on PC14 mux A*/
#define MUX_PC14A_EIC_EXTINT6                      (0L)         /**< EIC signal line function value: EIC_EXTINT6 */
#define PORT_PC14A_EIC_EXTINT6                     (1UL << 14)  /**< EIC signal: EICEXTINT6 */
#define PIN_PA07A_EIC_EXTINT7                      (7L)         /**< EIC signal: EIC_EXTINT7 on PA07 mux A*/
#define MUX_PA07A_EIC_EXTINT7                      (0L)         /**< EIC signal line function value: EIC_EXTINT7 */
#define PORT_PA07A_EIC_EXTINT7                     (1UL << 7)   /**< EIC signal: EICEXTINT7 */
#define PIN_PA23A_EIC_EXTINT7                      (23L)        /**< EIC signal: EIC_EXTINT7 on PA23 mux A*/
#define MUX_PA23A_EIC_EXTINT7                      (0L)         /**< EIC signal line function value: EIC_EXTINT7 */
#define PORT_PA23A_EIC_EXTINT7                     (1UL << 23)  /**< EIC signal: EICEXTINT7 */
#define PIN_PB07A_EIC_EXTINT7                      (39L)        /**< EIC signal: EIC_EXTINT7 on PB07 mux A*/
#define MUX_PB07A_EIC_EXTINT7                      (0L)         /**< EIC signal line function value: EIC_EXTINT7 */
#define PORT_PB07A_EIC_EXTINT7                     (1UL << 7)   /**< EIC signal: EICEXTINT7 */
#define PIN_PB23A_EIC_EXTINT7                      (55L)        /**< EIC signal: EIC_EXTINT7 on PB23 mux A*/
#define MUX_PB23A_EIC_EXTINT7                      (0L)         /**< EIC signal line function value: EIC_EXTINT7 */
#define PORT_PB23A_EIC_EXTINT7                     (1UL << 23)  /**< EIC signal: EICEXTINT7 */
#define PIN_PC15A_EIC_EXTINT7                      (79L)        /**< EIC signal: EIC_EXTINT7 on PC15 mux A*/
#define MUX_PC15A_EIC_EXTINT7                      (0L)         /**< EIC signal line function value: EIC_EXTINT7 */
#define PORT_PC15A_EIC_EXTINT7                     (1UL << 15)  /**< EIC signal: EICEXTINT7 */
#define PIN_PB08A_EIC_EXTINT8                      (40L)        /**< EIC signal: EIC_EXTINT8 on PB08 mux A*/
#define MUX_PB08A_EIC_EXTINT8                      (0L)         /**< EIC signal line function value: EIC_EXTINT8 */
#define PORT_PB08A_EIC_EXTINT8                     (1UL << 8)   /**< EIC signal: EICEXTINT8 */
#define PIN_PB24A_EIC_EXTINT8                      (56L)        /**< EIC signal: EIC_EXTINT8 on PB24 mux A*/
#define MUX_PB24A_EIC_EXTINT8                      (0L)         /**< EIC signal line function value: EIC_EXTINT8 */
#define PORT_PB24A_EIC_EXTINT8                     (1UL << 24)  /**< EIC signal: EICEXTINT8 */
#define PIN_PC00A_EIC_EXTINT8                      (64L)        /**< EIC signal: EIC_EXTINT8 on PC00 mux A*/
#define MUX_PC00A_EIC_EXTINT8                      (0L)         /**< EIC signal line function value: EIC_EXTINT8 */
#define PORT_PC00A_EIC_EXTINT8                     (1UL << 0)   /**< EIC signal: EICEXTINT8 */
#define PIN_PC16A_EIC_EXTINT8                      (80L)        /**< EIC signal: EIC_EXTINT8 on PC16 mux A*/
#define MUX_PC16A_EIC_EXTINT8                      (0L)         /**< EIC signal line function value: EIC_EXTINT8 */
#define PORT_PC16A_EIC_EXTINT8                     (1UL << 16)  /**< EIC signal: EICEXTINT8 */
#define PIN_PA28A_EIC_EXTINT8                      (28L)        /**< EIC signal: EIC_EXTINT8 on PA28 mux A*/
#define MUX_PA28A_EIC_EXTINT8                      (0L)         /**< EIC signal line function value: EIC_EXTINT8 */
#define PORT_PA28A_EIC_EXTINT8                     (1UL << 28)  /**< EIC signal: EICEXTINT8 */
#define PIN_PA09A_EIC_EXTINT9                      (9L)         /**< EIC signal: EIC_EXTINT9 on PA09 mux A*/
#define MUX_PA09A_EIC_EXTINT9                      (0L)         /**< EIC signal line function value: EIC_EXTINT9 */
#define PORT_PA09A_EIC_EXTINT9                     (1UL << 9)   /**< EIC signal: EICEXTINT9 */
#define PIN_PB09A_EIC_EXTINT9                      (41L)        /**< EIC signal: EIC_EXTINT9 on PB09 mux A*/
#define MUX_PB09A_EIC_EXTINT9                      (0L)         /**< EIC signal line function value: EIC_EXTINT9 */
#define PORT_PB09A_EIC_EXTINT9                     (1UL << 9)   /**< EIC signal: EICEXTINT9 */
#define PIN_PB25A_EIC_EXTINT9                      (57L)        /**< EIC signal: EIC_EXTINT9 on PB25 mux A*/
#define MUX_PB25A_EIC_EXTINT9                      (0L)         /**< EIC signal line function value: EIC_EXTINT9 */
#define PORT_PB25A_EIC_EXTINT9                     (1UL << 25)  /**< EIC signal: EICEXTINT9 */
#define PIN_PC01A_EIC_EXTINT9                      (65L)        /**< EIC signal: EIC_EXTINT9 on PC01 mux A*/
#define MUX_PC01A_EIC_EXTINT9                      (0L)         /**< EIC signal line function value: EIC_EXTINT9 */
#define PORT_PC01A_EIC_EXTINT9                     (1UL << 1)   /**< EIC signal: EICEXTINT9 */
#define PIN_PC17A_EIC_EXTINT9                      (81L)        /**< EIC signal: EIC_EXTINT9 on PC17 mux A*/
#define MUX_PC17A_EIC_EXTINT9                      (0L)         /**< EIC signal line function value: EIC_EXTINT9 */
#define PORT_PC17A_EIC_EXTINT9                     (1UL << 17)  /**< EIC signal: EICEXTINT9 */
#define PIN_PA10A_EIC_EXTINT10                     (10L)        /**< EIC signal: EIC_EXTINT10 on PA10 mux A*/
#define MUX_PA10A_EIC_EXTINT10                     (0L)         /**< EIC signal line function value: EIC_EXTINT10 */
#define PORT_PA10A_EIC_EXTINT10                    (1UL << 10)  /**< EIC signal: EICEXTINT10 */
#define PIN_PA30A_EIC_EXTINT10                     (30L)        /**< EIC signal: EIC_EXTINT10 on PA30 mux A*/
#define MUX_PA30A_EIC_EXTINT10                     (0L)         /**< EIC signal line function value: EIC_EXTINT10 */
#define PORT_PA30A_EIC_EXTINT10                    (1UL << 30)  /**< EIC signal: EICEXTINT10 */
#define PIN_PB10A_EIC_EXTINT10                     (42L)        /**< EIC signal: EIC_EXTINT10 on PB10 mux A*/
#define MUX_PB10A_EIC_EXTINT10                     (0L)         /**< EIC signal line function value: EIC_EXTINT10 */
#define PORT_PB10A_EIC_EXTINT10                    (1UL << 10)  /**< EIC signal: EICEXTINT10 */
#define PIN_PC02A_EIC_EXTINT10                     (66L)        /**< EIC signal: EIC_EXTINT10 on PC02 mux A*/
#define MUX_PC02A_EIC_EXTINT10                     (0L)         /**< EIC signal line function value: EIC_EXTINT10 */
#define PORT_PC02A_EIC_EXTINT10                    (1UL << 2)   /**< EIC signal: EICEXTINT10 */
#define PIN_PC18A_EIC_EXTINT10                     (82L)        /**< EIC signal: EIC_EXTINT10 on PC18 mux A*/
#define MUX_PC18A_EIC_EXTINT10                     (0L)         /**< EIC signal line function value: EIC_EXTINT10 */
#define PORT_PC18A_EIC_EXTINT10                    (1UL << 18)  /**< EIC signal: EICEXTINT10 */
#define PIN_PA11A_EIC_EXTINT11                     (11L)        /**< EIC signal: EIC_EXTINT11 on PA11 mux A*/
#define MUX_PA11A_EIC_EXTINT11                     (0L)         /**< EIC signal line function value: EIC_EXTINT11 */
#define PORT_PA11A_EIC_EXTINT11                    (1UL << 11)  /**< EIC signal: EICEXTINT11 */
#define PIN_PA31A_EIC_EXTINT11                     (31L)        /**< EIC signal: EIC_EXTINT11 on PA31 mux A*/
#define MUX_PA31A_EIC_EXTINT11                     (0L)         /**< EIC signal line function value: EIC_EXTINT11 */
#define PORT_PA31A_EIC_EXTINT11                    (1UL << 31)  /**< EIC signal: EICEXTINT11 */
#define PIN_PB11A_EIC_EXTINT11                     (43L)        /**< EIC signal: EIC_EXTINT11 on PB11 mux A*/
#define MUX_PB11A_EIC_EXTINT11                     (0L)         /**< EIC signal line function value: EIC_EXTINT11 */
#define PORT_PB11A_EIC_EXTINT11                    (1UL << 11)  /**< EIC signal: EICEXTINT11 */
#define PIN_PC03A_EIC_EXTINT11                     (67L)        /**< EIC signal: EIC_EXTINT11 on PC03 mux A*/
#define MUX_PC03A_EIC_EXTINT11                     (0L)         /**< EIC signal line function value: EIC_EXTINT11 */
#define PORT_PC03A_EIC_EXTINT11                    (1UL << 3)   /**< EIC signal: EICEXTINT11 */
#define PIN_PC19A_EIC_EXTINT11                     (83L)        /**< EIC signal: EIC_EXTINT11 on PC19 mux A*/
#define MUX_PC19A_EIC_EXTINT11                     (0L)         /**< EIC signal line function value: EIC_EXTINT11 */
#define PORT_PC19A_EIC_EXTINT11                    (1UL << 19)  /**< EIC signal: EICEXTINT11 */
#define PIN_PA12A_EIC_EXTINT12                     (12L)        /**< EIC signal: EIC_EXTINT12 on PA12 mux A*/
#define MUX_PA12A_EIC_EXTINT12                     (0L)         /**< EIC signal line function value: EIC_EXTINT12 */
#define PORT_PA12A_EIC_EXTINT12                    (1UL << 12)  /**< EIC signal: EICEXTINT12 */
#define PIN_PA24A_EIC_EXTINT12                     (24L)        /**< EIC signal: EIC_EXTINT12 on PA24 mux A*/
#define MUX_PA24A_EIC_EXTINT12                     (0L)         /**< EIC signal line function value: EIC_EXTINT12 */
#define PORT_PA24A_EIC_EXTINT12                    (1UL << 24)  /**< EIC signal: EICEXTINT12 */
#define PIN_PB12A_EIC_EXTINT12                     (44L)        /**< EIC signal: EIC_EXTINT12 on PB12 mux A*/
#define MUX_PB12A_EIC_EXTINT12                     (0L)         /**< EIC signal line function value: EIC_EXTINT12 */
#define PORT_PB12A_EIC_EXTINT12                    (1UL << 12)  /**< EIC signal: EICEXTINT12 */
#define PIN_PC20A_EIC_EXTINT12                     (84L)        /**< EIC signal: EIC_EXTINT12 on PC20 mux A*/
#define MUX_PC20A_EIC_EXTINT12                     (0L)         /**< EIC signal line function value: EIC_EXTINT12 */
#define PORT_PC20A_EIC_EXTINT12                    (1UL << 20)  /**< EIC signal: EICEXTINT12 */
#define PIN_PA13A_EIC_EXTINT13                     (13L)        /**< EIC signal: EIC_EXTINT13 on PA13 mux A*/
#define MUX_PA13A_EIC_EXTINT13                     (0L)         /**< EIC signal line function value: EIC_EXTINT13 */
#define PORT_PA13A_EIC_EXTINT13                    (1UL << 13)  /**< EIC signal: EICEXTINT13 */
#define PIN_PA25A_EIC_EXTINT13                     (25L)        /**< EIC signal: EIC_EXTINT13 on PA25 mux A*/
#define MUX_PA25A_EIC_EXTINT13                     (0L)         /**< EIC signal line function value: EIC_EXTINT13 */
#define PORT_PA25A_EIC_EXTINT13                    (1UL << 25)  /**< EIC signal: EICEXTINT13 */
#define PIN_PB13A_EIC_EXTINT13                     (45L)        /**< EIC signal: EIC_EXTINT13 on PB13 mux A*/
#define MUX_PB13A_EIC_EXTINT13                     (0L)         /**< EIC signal line function value: EIC_EXTINT13 */
#define PORT_PB13A_EIC_EXTINT13                    (1UL << 13)  /**< EIC signal: EICEXTINT13 */
#define PIN_PC05A_EIC_EXTINT13                     (69L)        /**< EIC signal: EIC_EXTINT13 on PC05 mux A*/
#define MUX_PC05A_EIC_EXTINT13                     (0L)         /**< EIC signal line function value: EIC_EXTINT13 */
#define PORT_PC05A_EIC_EXTINT13                    (1UL << 5)   /**< EIC signal: EICEXTINT13 */
#define PIN_PC21A_EIC_EXTINT13                     (85L)        /**< EIC signal: EIC_EXTINT13 on PC21 mux A*/
#define MUX_PC21A_EIC_EXTINT13                     (0L)         /**< EIC signal line function value: EIC_EXTINT13 */
#define PORT_PC21A_EIC_EXTINT13                    (1UL << 21)  /**< EIC signal: EICEXTINT13 */
#define PIN_PB14A_EIC_EXTINT14                     (46L)        /**< EIC signal: EIC_EXTINT14 on PB14 mux A*/
#define MUX_PB14A_EIC_EXTINT14                     (0L)         /**< EIC signal line function value: EIC_EXTINT14 */
#define PORT_PB14A_EIC_EXTINT14                    (1UL << 14)  /**< EIC signal: EICEXTINT14 */
#define PIN_PB30A_EIC_EXTINT14                     (62L)        /**< EIC signal: EIC_EXTINT14 on PB30 mux A*/
#define MUX_PB30A_EIC_EXTINT14                     (0L)         /**< EIC signal line function value: EIC_EXTINT14 */
#define PORT_PB30A_EIC_EXTINT14                    (1UL << 30)  /**< EIC signal: EICEXTINT14 */
#define PIN_PC06A_EIC_EXTINT14                     (70L)        /**< EIC signal: EIC_EXTINT14 on PC06 mux A*/
#define MUX_PC06A_EIC_EXTINT14                     (0L)         /**< EIC signal line function value: EIC_EXTINT14 */
#define PORT_PC06A_EIC_EXTINT14                    (1UL << 6)   /**< EIC signal: EICEXTINT14 */
#define PIN_PA14A_EIC_EXTINT14                     (14L)        /**< EIC signal: EIC_EXTINT14 on PA14 mux A*/
#define MUX_PA14A_EIC_EXTINT14                     (0L)         /**< EIC signal line function value: EIC_EXTINT14 */
#define PORT_PA14A_EIC_EXTINT14                    (1UL << 14)  /**< EIC signal: EICEXTINT14 */
#define PIN_PA27A_EIC_EXTINT15                     (27L)        /**< EIC signal: EIC_EXTINT15 on PA27 mux A*/
#define MUX_PA27A_EIC_EXTINT15                     (0L)         /**< EIC signal line function value: EIC_EXTINT15 */
#define PORT_PA27A_EIC_EXTINT15                    (1UL << 27)  /**< EIC signal: EICEXTINT15 */
#define PIN_PB15A_EIC_EXTINT15                     (47L)        /**< EIC signal: EIC_EXTINT15 on PB15 mux A*/
#define MUX_PB15A_EIC_EXTINT15                     (0L)         /**< EIC signal line function value: EIC_EXTINT15 */
#define PORT_PB15A_EIC_EXTINT15                    (1UL << 15)  /**< EIC signal: EICEXTINT15 */
#define PIN_PB31A_EIC_EXTINT15                     (63L)        /**< EIC signal: EIC_EXTINT15 on PB31 mux A*/
#define MUX_PB31A_EIC_EXTINT15                     (0L)         /**< EIC signal line function value: EIC_EXTINT15 */
#define PORT_PB31A_EIC_EXTINT15                    (1UL << 31)  /**< EIC signal: EICEXTINT15 */
#define PIN_PC07A_EIC_EXTINT15                     (71L)        /**< EIC signal: EIC_EXTINT15 on PC07 mux A*/
#define MUX_PC07A_EIC_EXTINT15                     (0L)         /**< EIC signal line function value: EIC_EXTINT15 */
#define PORT_PC07A_EIC_EXTINT15                    (1UL << 7)   /**< EIC signal: EICEXTINT15 */
#define PIN_PA15A_EIC_EXTINT15                     (15L)        /**< EIC signal: EIC_EXTINT15 on PA15 mux A*/
#define MUX_PA15A_EIC_EXTINT15                     (0L)         /**< EIC signal line function value: EIC_EXTINT15 */
#define PORT_PA15A_EIC_EXTINT15                    (1UL << 15)  /**< EIC signal: EICEXTINT15 */
#define PIN_PA08A_EIC_NMI                          (8L)         /**< EIC signal: EIC_NMI on PA08 mux A*/
#define MUX_PA08A_EIC_NMI                          (0L)         /**< EIC signal line function value: EIC_NMI */
#define PORT_PA08A_EIC_NMI                         (1UL << 8)   /**< EIC signal: EICNMI */
/* ========== PIO definition for GCLK peripheral ========== */
#define PIN_PB14H_GCLK_IO0                         (46L)        /**< GCLK signal: GCLK_IO0 on PB14 mux H*/
#define MUX_PB14H_GCLK_IO0                         (7L)         /**< GCLK signal line function value: GCLK_IO0 */
#define PORT_PB14H_GCLK_IO0                        (1UL << 14)  /**< GCLK signal: GCLKIO0 */
#define PIN_PB22H_GCLK_IO0                         (54L)        /**< GCLK signal: GCLK_IO0 on PB22 mux H*/
#define MUX_PB22H_GCLK_IO0                         (7L)         /**< GCLK signal line function value: GCLK_IO0 */
#define PORT_PB22H_GCLK_IO0                        (1UL << 22)  /**< GCLK signal: GCLKIO0 */
#define PIN_PA14H_GCLK_IO0                         (14L)        /**< GCLK signal: GCLK_IO0 on PA14 mux H*/
#define MUX_PA14H_GCLK_IO0                         (7L)         /**< GCLK signal line function value: GCLK_IO0 */
#define PORT_PA14H_GCLK_IO0                        (1UL << 14)  /**< GCLK signal: GCLKIO0 */
#define PIN_PA27H_GCLK_IO0                         (27L)        /**< GCLK signal: GCLK_IO0 on PA27 mux H*/
#define MUX_PA27H_GCLK_IO0                         (7L)         /**< GCLK signal line function value: GCLK_IO0 */
#define PORT_PA27H_GCLK_IO0                        (1UL << 27)  /**< GCLK signal: GCLKIO0 */
#define PIN_PA28H_GCLK_IO0                         (28L)        /**< GCLK signal: GCLK_IO0 on PA28 mux H*/
#define MUX_PA28H_GCLK_IO0                         (7L)         /**< GCLK signal line function value: GCLK_IO0 */
#define PORT_PA28H_GCLK_IO0                        (1UL << 28)  /**< GCLK signal: GCLKIO0 */
#define PIN_PA30H_GCLK_IO0                         (30L)        /**< GCLK signal: GCLK_IO0 on PA30 mux H*/
#define MUX_PA30H_GCLK_IO0                         (7L)         /**< GCLK signal line function value: GCLK_IO0 */
#define PORT_PA30H_GCLK_IO0                        (1UL << 30)  /**< GCLK signal: GCLKIO0 */
#define PIN_PB23H_GCLK_IO1                         (55L)        /**< GCLK signal: GCLK_IO1 on PB23 mux H*/
#define MUX_PB23H_GCLK_IO1                         (7L)         /**< GCLK signal line function value: GCLK_IO1 */
#define PORT_PB23H_GCLK_IO1                        (1UL << 23)  /**< GCLK signal: GCLKIO1 */
#define PIN_PA15H_GCLK_IO1                         (15L)        /**< GCLK signal: GCLK_IO1 on PA15 mux H*/
#define MUX_PA15H_GCLK_IO1                         (7L)         /**< GCLK signal line function value: GCLK_IO1 */
#define PORT_PA15H_GCLK_IO1                        (1UL << 15)  /**< GCLK signal: GCLKIO1 */
#define PIN_PB15H_GCLK_IO1                         (47L)        /**< GCLK signal: GCLK_IO1 on PB15 mux H*/
#define MUX_PB15H_GCLK_IO1                         (7L)         /**< GCLK signal line function value: GCLK_IO1 */
#define PORT_PB15H_GCLK_IO1                        (1UL << 15)  /**< GCLK signal: GCLKIO1 */
#define PIN_PB16H_GCLK_IO2                         (48L)        /**< GCLK signal: GCLK_IO2 on PB16 mux H*/
#define MUX_PB16H_GCLK_IO2                         (7L)         /**< GCLK signal line function value: GCLK_IO2 */
#define PORT_PB16H_GCLK_IO2                        (1UL << 16)  /**< GCLK signal: GCLKIO2 */
#define PIN_PA16H_GCLK_IO2                         (16L)        /**< GCLK signal: GCLK_IO2 on PA16 mux H*/
#define MUX_PA16H_GCLK_IO2                         (7L)         /**< GCLK signal line function value: GCLK_IO2 */
#define PORT_PA16H_GCLK_IO2                        (1UL << 16)  /**< GCLK signal: GCLKIO2 */
#define PIN_PA17H_GCLK_IO3                         (17L)        /**< GCLK signal: GCLK_IO3 on PA17 mux H*/
#define MUX_PA17H_GCLK_IO3                         (7L)         /**< GCLK signal line function value: GCLK_IO3 */
#define PORT_PA17H_GCLK_IO3                        (1UL << 17)  /**< GCLK signal: GCLKIO3 */
#define PIN_PB17H_GCLK_IO3                         (49L)        /**< GCLK signal: GCLK_IO3 on PB17 mux H*/
#define MUX_PB17H_GCLK_IO3                         (7L)         /**< GCLK signal line function value: GCLK_IO3 */
#define PORT_PB17H_GCLK_IO3                        (1UL << 17)  /**< GCLK signal: GCLKIO3 */
#define PIN_PA10H_GCLK_IO4                         (10L)        /**< GCLK signal: GCLK_IO4 on PA10 mux H*/
#define MUX_PA10H_GCLK_IO4                         (7L)         /**< GCLK signal line function value: GCLK_IO4 */
#define PORT_PA10H_GCLK_IO4                        (1UL << 10)  /**< GCLK signal: GCLKIO4 */
#define PIN_PB10H_GCLK_IO4                         (42L)        /**< GCLK signal: GCLK_IO4 on PB10 mux H*/
#define MUX_PB10H_GCLK_IO4                         (7L)         /**< GCLK signal line function value: GCLK_IO4 */
#define PORT_PB10H_GCLK_IO4                        (1UL << 10)  /**< GCLK signal: GCLKIO4 */
#define PIN_PB18H_GCLK_IO4                         (50L)        /**< GCLK signal: GCLK_IO4 on PB18 mux H*/
#define MUX_PB18H_GCLK_IO4                         (7L)         /**< GCLK signal line function value: GCLK_IO4 */
#define PORT_PB18H_GCLK_IO4                        (1UL << 18)  /**< GCLK signal: GCLKIO4 */
#define PIN_PA20H_GCLK_IO4                         (20L)        /**< GCLK signal: GCLK_IO4 on PA20 mux H*/
#define MUX_PA20H_GCLK_IO4                         (7L)         /**< GCLK signal line function value: GCLK_IO4 */
#define PORT_PA20H_GCLK_IO4                        (1UL << 20)  /**< GCLK signal: GCLKIO4 */
#define PIN_PA11H_GCLK_IO5                         (11L)        /**< GCLK signal: GCLK_IO5 on PA11 mux H*/
#define MUX_PA11H_GCLK_IO5                         (7L)         /**< GCLK signal line function value: GCLK_IO5 */
#define PORT_PA11H_GCLK_IO5                        (1UL << 11)  /**< GCLK signal: GCLKIO5 */
#define PIN_PA21H_GCLK_IO5                         (21L)        /**< GCLK signal: GCLK_IO5 on PA21 mux H*/
#define MUX_PA21H_GCLK_IO5                         (7L)         /**< GCLK signal line function value: GCLK_IO5 */
#define PORT_PA21H_GCLK_IO5                        (1UL << 21)  /**< GCLK signal: GCLKIO5 */
#define PIN_PB11H_GCLK_IO5                         (43L)        /**< GCLK signal: GCLK_IO5 on PB11 mux H*/
#define MUX_PB11H_GCLK_IO5                         (7L)         /**< GCLK signal line function value: GCLK_IO5 */
#define PORT_PB11H_GCLK_IO5                        (1UL << 11)  /**< GCLK signal: GCLKIO5 */
#define PIN_PB19H_GCLK_IO5                         (51L)        /**< GCLK signal: GCLK_IO5 on PB19 mux H*/
#define MUX_PB19H_GCLK_IO5                         (7L)         /**< GCLK signal line function value: GCLK_IO5 */
#define PORT_PB19H_GCLK_IO5                        (1UL << 19)  /**< GCLK signal: GCLKIO5 */
#define PIN_PA22H_GCLK_IO6                         (22L)        /**< GCLK signal: GCLK_IO6 on PA22 mux H*/
#define MUX_PA22H_GCLK_IO6                         (7L)         /**< GCLK signal line function value: GCLK_IO6 */
#define PORT_PA22H_GCLK_IO6                        (1UL << 22)  /**< GCLK signal: GCLKIO6 */
#define PIN_PB12H_GCLK_IO6                         (44L)        /**< GCLK signal: GCLK_IO6 on PB12 mux H*/
#define MUX_PB12H_GCLK_IO6                         (7L)         /**< GCLK signal line function value: GCLK_IO6 */
#define PORT_PB12H_GCLK_IO6                        (1UL << 12)  /**< GCLK signal: GCLKIO6 */
#define PIN_PB20H_GCLK_IO6                         (52L)        /**< GCLK signal: GCLK_IO6 on PB20 mux H*/
#define MUX_PB20H_GCLK_IO6                         (7L)         /**< GCLK signal line function value: GCLK_IO6 */
#define PORT_PB20H_GCLK_IO6                        (1UL << 20)  /**< GCLK signal: GCLKIO6 */
#define PIN_PB13H_GCLK_IO7                         (45L)        /**< GCLK signal: GCLK_IO7 on PB13 mux H*/
#define MUX_PB13H_GCLK_IO7                         (7L)         /**< GCLK signal line function value: GCLK_IO7 */
#define PORT_PB13H_GCLK_IO7                        (1UL << 13)  /**< GCLK signal: GCLKIO7 */
#define PIN_PA23H_GCLK_IO7                         (23L)        /**< GCLK signal: GCLK_IO7 on PA23 mux H*/
#define MUX_PA23H_GCLK_IO7                         (7L)         /**< GCLK signal line function value: GCLK_IO7 */
#define PORT_PA23H_GCLK_IO7                        (1UL << 23)  /**< GCLK signal: GCLKIO7 */
#define PIN_PB21H_GCLK_IO7                         (53L)        /**< GCLK signal: GCLK_IO7 on PB21 mux H*/
#define MUX_PB21H_GCLK_IO7                         (7L)         /**< GCLK signal line function value: GCLK_IO7 */
#define PORT_PB21H_GCLK_IO7                        (1UL << 21)  /**< GCLK signal: GCLKIO7 */
/* ========== PIO definition for NVMCTRL peripheral ========== */
/* ========== PIO definition for OSCCTRL peripheral ========== */
#define PIN_PA14XIN_OSCCTRL_XIN                    (14L)        /**< OSCCTRL signal: OSCCTRL_XIN on PA14 mux XIN*/
#define MUX_PA14XIN_OSCCTRL_XIN                    (L)          /**< OSCCTRL signal line function value: OSCCTRL_XIN */
#define PORT_PA14XIN_OSCCTRL_XIN                   (1UL << 14)  /**< OSCCTRL signal: OSCCTRLXIN */
#define PIN_PA15XOUT_OSCCTRL_XOUT                  (15L)        /**< OSCCTRL signal: OSCCTRL_XOUT on PA15 mux XOUT*/
#define MUX_PA15XOUT_OSCCTRL_XOUT                  (L)          /**< OSCCTRL signal line function value: OSCCTRL_XOUT */
#define PORT_PA15XOUT_OSCCTRL_XOUT                 (1UL << 15)  /**< OSCCTRL signal: OSCCTRLXOUT */
/* ========== PIO definition for OSC32KCTRL peripheral ========== */
#define PIN_PA00XIN32_OSC32KCTRL_XIN32             (0L)         /**< OSC32KCTRL signal: OSC32KCTRL_XIN32 on PA00 mux XIN32*/
#define MUX_PA00XIN32_OSC32KCTRL_XIN32             (L)          /**< OSC32KCTRL signal line function value: OSC32KCTRL_XIN32 */
#define PORT_PA00XIN32_OSC32KCTRL_XIN32            (1UL << 0)   /**< OSC32KCTRL signal: OSC32KCTRLXIN32 */
#define PIN_PA01XOUT32_OSC32KCTRL_XOUT32           (1L)         /**< OSC32KCTRL signal: OSC32KCTRL_XOUT32 on PA01 mux XOUT32*/
#define MUX_PA01XOUT32_OSC32KCTRL_XOUT32           (L)          /**< OSC32KCTRL signal line function value: OSC32KCTRL_XOUT32 */
#define PORT_PA01XOUT32_OSC32KCTRL_XOUT32          (1UL << 1)   /**< OSC32KCTRL signal: OSC32KCTRLXOUT32 */
/* ========== PIO definition for PM peripheral ========== */
/* ========== PIO definition for PTC peripheral ========== */
#define PIN_PA08B_PTC_X0                           (8L)         /**< PTC signal: PTC_X0 on PA08 mux B*/
#define MUX_PA08B_PTC_X0                           (1L)         /**< PTC signal line function value: PTC_X0 */
#define PORT_PA08B_PTC_X0                          (1UL << 8)   /**< PTC signal: PTCX0 */
#define PIN_PA09B_PTC_X1                           (9L)         /**< PTC signal: PTC_X1 on PA09 mux B*/
#define MUX_PA09B_PTC_X1                           (1L)         /**< PTC signal line function value: PTC_X1 */
#define PORT_PA09B_PTC_X1                          (1UL << 9)   /**< PTC signal: PTCX1 */
#define PIN_PA10B_PTC_X2                           (10L)        /**< PTC signal: PTC_X2 on PA10 mux B*/
#define MUX_PA10B_PTC_X2                           (1L)         /**< PTC signal line function value: PTC_X2 */
#define PORT_PA10B_PTC_X2                          (1UL << 10)  /**< PTC signal: PTCX2 */
#define PIN_PA11B_PTC_X3                           (11L)        /**< PTC signal: PTC_X3 on PA11 mux B*/
#define MUX_PA11B_PTC_X3                           (1L)         /**< PTC signal line function value: PTC_X3 */
#define PORT_PA11B_PTC_X3                          (1UL << 11)  /**< PTC signal: PTCX3 */
#define PIN_PA16B_PTC_X4                           (16L)        /**< PTC signal: PTC_X4 on PA16 mux B*/
#define MUX_PA16B_PTC_X4                           (1L)         /**< PTC signal line function value: PTC_X4 */
#define PORT_PA16B_PTC_X4                          (1UL << 16)  /**< PTC signal: PTCX4 */
#define PIN_PA17B_PTC_X5                           (17L)        /**< PTC signal: PTC_X5 on PA17 mux B*/
#define MUX_PA17B_PTC_X5                           (1L)         /**< PTC signal line function value: PTC_X5 */
#define PORT_PA17B_PTC_X5                          (1UL << 17)  /**< PTC signal: PTCX5 */
#define PIN_PA18B_PTC_X6                           (18L)        /**< PTC signal: PTC_X6 on PA18 mux B*/
#define MUX_PA18B_PTC_X6                           (1L)         /**< PTC signal line function value: PTC_X6 */
#define PORT_PA18B_PTC_X6                          (1UL << 18)  /**< PTC signal: PTCX6 */
#define PIN_PA19B_PTC_X7                           (19L)        /**< PTC signal: PTC_X7 on PA19 mux B*/
#define MUX_PA19B_PTC_X7                           (1L)         /**< PTC signal line function value: PTC_X7 */
#define PORT_PA19B_PTC_X7                          (1UL << 19)  /**< PTC signal: PTCX7 */
#define PIN_PA20B_PTC_X8                           (20L)        /**< PTC signal: PTC_X8 on PA20 mux B*/
#define MUX_PA20B_PTC_X8                           (1L)         /**< PTC signal line function value: PTC_X8 */
#define PORT_PA20B_PTC_X8                          (1UL << 20)  /**< PTC signal: PTCX8 */
#define PIN_PA21B_PTC_X9                           (21L)        /**< PTC signal: PTC_X9 on PA21 mux B*/
#define MUX_PA21B_PTC_X9                           (1L)         /**< PTC signal line function value: PTC_X9 */
#define PORT_PA21B_PTC_X9                          (1UL << 21)  /**< PTC signal: PTCX9 */
#define PIN_PA22B_PTC_X10                          (22L)        /**< PTC signal: PTC_X10 on PA22 mux B*/
#define MUX_PA22B_PTC_X10                          (1L)         /**< PTC signal line function value: PTC_X10 */
#define PORT_PA22B_PTC_X10                         (1UL << 22)  /**< PTC signal: PTCX10 */
#define PIN_PA23B_PTC_X11                          (23L)        /**< PTC signal: PTC_X11 on PA23 mux B*/
#define MUX_PA23B_PTC_X11                          (1L)         /**< PTC signal line function value: PTC_X11 */
#define PORT_PA23B_PTC_X11                         (1UL << 23)  /**< PTC signal: PTCX11 */
#define PIN_PB12B_PTC_X12                          (44L)        /**< PTC signal: PTC_X12 on PB12 mux B*/
#define MUX_PB12B_PTC_X12                          (1L)         /**< PTC signal line function value: PTC_X12 */
#define PORT_PB12B_PTC_X12                         (1UL << 12)  /**< PTC signal: PTCX12 */
#define PIN_PB13B_PTC_X13                          (45L)        /**< PTC signal: PTC_X13 on PB13 mux B*/
#define MUX_PB13B_PTC_X13                          (1L)         /**< PTC signal line function value: PTC_X13 */
#define PORT_PB13B_PTC_X13                         (1UL << 13)  /**< PTC signal: PTCX13 */
#define PIN_PB14B_PTC_X14                          (46L)        /**< PTC signal: PTC_X14 on PB14 mux B*/
#define MUX_PB14B_PTC_X14                          (1L)         /**< PTC signal line function value: PTC_X14 */
#define PORT_PB14B_PTC_X14                         (1UL << 14)  /**< PTC signal: PTCX14 */
#define PIN_PB15B_PTC_X15                          (47L)        /**< PTC signal: PTC_X15 on PB15 mux B*/
#define MUX_PB15B_PTC_X15                          (1L)         /**< PTC signal line function value: PTC_X15 */
#define PORT_PB15B_PTC_X15                         (1UL << 15)  /**< PTC signal: PTCX15 */
#define PIN_PA02B_PTC_Y0                           (2L)         /**< PTC signal: PTC_Y0 on PA02 mux B*/
#define MUX_PA02B_PTC_Y0                           (1L)         /**< PTC signal line function value: PTC_Y0 */
#define PORT_PA02B_PTC_Y0                          (1UL << 2)   /**< PTC signal: PTCY0 */
#define PIN_PA03B_PTC_Y1                           (3L)         /**< PTC signal: PTC_Y1 on PA03 mux B*/
#define MUX_PA03B_PTC_Y1                           (1L)         /**< PTC signal line function value: PTC_Y1 */
#define PORT_PA03B_PTC_Y1                          (1UL << 3)   /**< PTC signal: PTCY1 */
#define PIN_PA04B_PTC_Y2                           (4L)         /**< PTC signal: PTC_Y2 on PA04 mux B*/
#define MUX_PA04B_PTC_Y2                           (1L)         /**< PTC signal line function value: PTC_Y2 */
#define PORT_PA04B_PTC_Y2                          (1UL << 4)   /**< PTC signal: PTCY2 */
#define PIN_PA05B_PTC_Y3                           (5L)         /**< PTC signal: PTC_Y3 on PA05 mux B*/
#define MUX_PA05B_PTC_Y3                           (1L)         /**< PTC signal line function value: PTC_Y3 */
#define PORT_PA05B_PTC_Y3                          (1UL << 5)   /**< PTC signal: PTCY3 */
#define PIN_PA06B_PTC_Y4                           (6L)         /**< PTC signal: PTC_Y4 on PA06 mux B*/
#define MUX_PA06B_PTC_Y4                           (1L)         /**< PTC signal line function value: PTC_Y4 */
#define PORT_PA06B_PTC_Y4                          (1UL << 6)   /**< PTC signal: PTCY4 */
#define PIN_PA07B_PTC_Y5                           (7L)         /**< PTC signal: PTC_Y5 on PA07 mux B*/
#define MUX_PA07B_PTC_Y5                           (1L)         /**< PTC signal line function value: PTC_Y5 */
#define PORT_PA07B_PTC_Y5                          (1UL << 7)   /**< PTC signal: PTCY5 */
#define PIN_PB00B_PTC_Y6                           (32L)        /**< PTC signal: PTC_Y6 on PB00 mux B*/
#define MUX_PB00B_PTC_Y6                           (1L)         /**< PTC signal line function value: PTC_Y6 */
#define PORT_PB00B_PTC_Y6                          (1UL << 0)   /**< PTC signal: PTCY6 */
#define PIN_PB01B_PTC_Y7                           (33L)        /**< PTC signal: PTC_Y7 on PB01 mux B*/
#define MUX_PB01B_PTC_Y7                           (1L)         /**< PTC signal line function value: PTC_Y7 */
#define PORT_PB01B_PTC_Y7                          (1UL << 1)   /**< PTC signal: PTCY7 */
#define PIN_PB02B_PTC_Y8                           (34L)        /**< PTC signal: PTC_Y8 on PB02 mux B*/
#define MUX_PB02B_PTC_Y8                           (1L)         /**< PTC signal line function value: PTC_Y8 */
#define PORT_PB02B_PTC_Y8                          (1UL << 2)   /**< PTC signal: PTCY8 */
#define PIN_PB03B_PTC_Y9                           (35L)        /**< PTC signal: PTC_Y9 on PB03 mux B*/
#define MUX_PB03B_PTC_Y9                           (1L)         /**< PTC signal line function value: PTC_Y9 */
#define PORT_PB03B_PTC_Y9                          (1UL << 3)   /**< PTC signal: PTCY9 */
#define PIN_PB04B_PTC_Y10                          (36L)        /**< PTC signal: PTC_Y10 on PB04 mux B*/
#define MUX_PB04B_PTC_Y10                          (1L)         /**< PTC signal line function value: PTC_Y10 */
#define PORT_PB04B_PTC_Y10                         (1UL << 4)   /**< PTC signal: PTCY10 */
#define PIN_PB05B_PTC_Y11                          (37L)        /**< PTC signal: PTC_Y11 on PB05 mux B*/
#define MUX_PB05B_PTC_Y11                          (1L)         /**< PTC signal line function value: PTC_Y11 */
#define PORT_PB05B_PTC_Y11                         (1UL << 5)   /**< PTC signal: PTCY11 */
#define PIN_PB06B_PTC_Y12                          (38L)        /**< PTC signal: PTC_Y12 on PB06 mux B*/
#define MUX_PB06B_PTC_Y12                          (1L)         /**< PTC signal line function value: PTC_Y12 */
#define PORT_PB06B_PTC_Y12                         (1UL << 6)   /**< PTC signal: PTCY12 */
#define PIN_PB07B_PTC_Y13                          (39L)        /**< PTC signal: PTC_Y13 on PB07 mux B*/
#define MUX_PB07B_PTC_Y13                          (1L)         /**< PTC signal line function value: PTC_Y13 */
#define PORT_PB07B_PTC_Y13                         (1UL << 7)   /**< PTC signal: PTCY13 */
#define PIN_PB08B_PTC_Y14                          (40L)        /**< PTC signal: PTC_Y14 on PB08 mux B*/
#define MUX_PB08B_PTC_Y14                          (1L)         /**< PTC signal line function value: PTC_Y14 */
#define PORT_PB08B_PTC_Y14                         (1UL << 8)   /**< PTC signal: PTCY14 */
#define PIN_PB09B_PTC_Y15                          (41L)        /**< PTC signal: PTC_Y15 on PB09 mux B*/
#define MUX_PB09B_PTC_Y15                          (1L)         /**< PTC signal line function value: PTC_Y15 */
#define PORT_PB09B_PTC_Y15                         (1UL << 9)   /**< PTC signal: PTCY15 */
#define PIN_PA08B_PTC_Y16                          (8L)         /**< PTC signal: PTC_Y16 on PA08 mux B*/
#define MUX_PA08B_PTC_Y16                          (1L)         /**< PTC signal line function value: PTC_Y16 */
#define PORT_PA08B_PTC_Y16                         (1UL << 8)   /**< PTC signal: PTCY16 */
#define PIN_PA09B_PTC_Y17                          (9L)         /**< PTC signal: PTC_Y17 on PA09 mux B*/
#define MUX_PA09B_PTC_Y17                          (1L)         /**< PTC signal line function value: PTC_Y17 */
#define PORT_PA09B_PTC_Y17                         (1UL << 9)   /**< PTC signal: PTCY17 */
#define PIN_PA10B_PTC_Y18                          (10L)        /**< PTC signal: PTC_Y18 on PA10 mux B*/
#define MUX_PA10B_PTC_Y18                          (1L)         /**< PTC signal line function value: PTC_Y18 */
#define PORT_PA10B_PTC_Y18                         (1UL << 10)  /**< PTC signal: PTCY18 */
#define PIN_PA11B_PTC_Y19                          (11L)        /**< PTC signal: PTC_Y19 on PA11 mux B*/
#define MUX_PA11B_PTC_Y19                          (1L)         /**< PTC signal line function value: PTC_Y19 */
#define PORT_PA11B_PTC_Y19                         (1UL << 11)  /**< PTC signal: PTCY19 */
#define PIN_PA16B_PTC_Y20                          (16L)        /**< PTC signal: PTC_Y20 on PA16 mux B*/
#define MUX_PA16B_PTC_Y20                          (1L)         /**< PTC signal line function value: PTC_Y20 */
#define PORT_PA16B_PTC_Y20                         (1UL << 16)  /**< PTC signal: PTCY20 */
#define PIN_PA17B_PTC_Y21                          (17L)        /**< PTC signal: PTC_Y21 on PA17 mux B*/
#define MUX_PA17B_PTC_Y21                          (1L)         /**< PTC signal line function value: PTC_Y21 */
#define PORT_PA17B_PTC_Y21                         (1UL << 17)  /**< PTC signal: PTCY21 */
#define PIN_PA18B_PTC_Y22                          (18L)        /**< PTC signal: PTC_Y22 on PA18 mux B*/
#define MUX_PA18B_PTC_Y22                          (1L)         /**< PTC signal line function value: PTC_Y22 */
#define PORT_PA18B_PTC_Y22                         (1UL << 18)  /**< PTC signal: PTCY22 */
#define PIN_PA19B_PTC_Y23                          (19L)        /**< PTC signal: PTC_Y23 on PA19 mux B*/
#define MUX_PA19B_PTC_Y23                          (1L)         /**< PTC signal line function value: PTC_Y23 */
#define PORT_PA19B_PTC_Y23                         (1UL << 19)  /**< PTC signal: PTCY23 */
#define PIN_PA20B_PTC_Y24                          (20L)        /**< PTC signal: PTC_Y24 on PA20 mux B*/
#define MUX_PA20B_PTC_Y24                          (1L)         /**< PTC signal line function value: PTC_Y24 */
#define PORT_PA20B_PTC_Y24                         (1UL << 20)  /**< PTC signal: PTCY24 */
#define PIN_PA21B_PTC_Y25                          (21L)        /**< PTC signal: PTC_Y25 on PA21 mux B*/
#define MUX_PA21B_PTC_Y25                          (1L)         /**< PTC signal line function value: PTC_Y25 */
#define PORT_PA21B_PTC_Y25                         (1UL << 21)  /**< PTC signal: PTCY25 */
#define PIN_PA22B_PTC_Y26                          (22L)        /**< PTC signal: PTC_Y26 on PA22 mux B*/
#define MUX_PA22B_PTC_Y26                          (1L)         /**< PTC signal line function value: PTC_Y26 */
#define PORT_PA22B_PTC_Y26                         (1UL << 22)  /**< PTC signal: PTCY26 */
#define PIN_PA23B_PTC_Y27                          (23L)        /**< PTC signal: PTC_Y27 on PA23 mux B*/
#define MUX_PA23B_PTC_Y27                          (1L)         /**< PTC signal line function value: PTC_Y27 */
#define PORT_PA23B_PTC_Y27                         (1UL << 23)  /**< PTC signal: PTCY27 */
#define PIN_PB12B_PTC_Y28                          (44L)        /**< PTC signal: PTC_Y28 on PB12 mux B*/
#define MUX_PB12B_PTC_Y28                          (1L)         /**< PTC signal line function value: PTC_Y28 */
#define PORT_PB12B_PTC_Y28                         (1UL << 12)  /**< PTC signal: PTCY28 */
#define PIN_PB13B_PTC_Y29                          (45L)        /**< PTC signal: PTC_Y29 on PB13 mux B*/
#define MUX_PB13B_PTC_Y29                          (1L)         /**< PTC signal line function value: PTC_Y29 */
#define PORT_PB13B_PTC_Y29                         (1UL << 13)  /**< PTC signal: PTCY29 */
#define PIN_PB14B_PTC_Y30                          (46L)        /**< PTC signal: PTC_Y30 on PB14 mux B*/
#define MUX_PB14B_PTC_Y30                          (1L)         /**< PTC signal line function value: PTC_Y30 */
#define PORT_PB14B_PTC_Y30                         (1UL << 14)  /**< PTC signal: PTCY30 */
#define PIN_PB15B_PTC_Y31                          (47L)        /**< PTC signal: PTC_Y31 on PB15 mux B*/
#define MUX_PB15B_PTC_Y31                          (1L)         /**< PTC signal line function value: PTC_Y31 */
#define PORT_PB15B_PTC_Y31                         (1UL << 15)  /**< PTC signal: PTCY31 */
/* ========== PIO definition for RSTC peripheral ========== */
#define PIN_PA00A_RSTC_EXTWAKE0                    (0L)         /**< RSTC signal: RSTC_EXTWAKE0 on PA00 mux A*/
#define MUX_PA00A_RSTC_EXTWAKE0                    (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE0 */
#define PORT_PA00A_RSTC_EXTWAKE0                   (1UL << 0)   /**< RSTC signal: RSTCEXTWAKE0 */
#define PIN_PA01A_RSTC_EXTWAKE1                    (1L)         /**< RSTC signal: RSTC_EXTWAKE1 on PA01 mux A*/
#define MUX_PA01A_RSTC_EXTWAKE1                    (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE1 */
#define PORT_PA01A_RSTC_EXTWAKE1                   (1UL << 1)   /**< RSTC signal: RSTCEXTWAKE1 */
#define PIN_PA02A_RSTC_EXTWAKE2                    (2L)         /**< RSTC signal: RSTC_EXTWAKE2 on PA02 mux A*/
#define MUX_PA02A_RSTC_EXTWAKE2                    (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE2 */
#define PORT_PA02A_RSTC_EXTWAKE2                   (1UL << 2)   /**< RSTC signal: RSTCEXTWAKE2 */
#define PIN_PA03A_RSTC_EXTWAKE3                    (3L)         /**< RSTC signal: RSTC_EXTWAKE3 on PA03 mux A*/
#define MUX_PA03A_RSTC_EXTWAKE3                    (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE3 */
#define PORT_PA03A_RSTC_EXTWAKE3                   (1UL << 3)   /**< RSTC signal: RSTCEXTWAKE3 */
#define PIN_PA04A_RSTC_EXTWAKE4                    (4L)         /**< RSTC signal: RSTC_EXTWAKE4 on PA04 mux A*/
#define MUX_PA04A_RSTC_EXTWAKE4                    (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE4 */
#define PORT_PA04A_RSTC_EXTWAKE4                   (1UL << 4)   /**< RSTC signal: RSTCEXTWAKE4 */
#define PIN_PA05A_RSTC_EXTWAKE5                    (5L)         /**< RSTC signal: RSTC_EXTWAKE5 on PA05 mux A*/
#define MUX_PA05A_RSTC_EXTWAKE5                    (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE5 */
#define PORT_PA05A_RSTC_EXTWAKE5                   (1UL << 5)   /**< RSTC signal: RSTCEXTWAKE5 */
#define PIN_PA06A_RSTC_EXTWAKE6                    (6L)         /**< RSTC signal: RSTC_EXTWAKE6 on PA06 mux A*/
#define MUX_PA06A_RSTC_EXTWAKE6                    (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE6 */
#define PORT_PA06A_RSTC_EXTWAKE6                   (1UL << 6)   /**< RSTC signal: RSTCEXTWAKE6 */
#define PIN_PA07A_RSTC_EXTWAKE7                    (7L)         /**< RSTC signal: RSTC_EXTWAKE7 on PA07 mux A*/
#define MUX_PA07A_RSTC_EXTWAKE7                    (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE7 */
#define PORT_PA07A_RSTC_EXTWAKE7                   (1UL << 7)   /**< RSTC signal: RSTCEXTWAKE7 */
#define PIN_PA08A_RSTC_EXTWAKE8                    (8L)         /**< RSTC signal: RSTC_EXTWAKE8 on PA08 mux A*/
#define MUX_PA08A_RSTC_EXTWAKE8                    (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE8 */
#define PORT_PA08A_RSTC_EXTWAKE8                   (1UL << 8)   /**< RSTC signal: RSTCEXTWAKE8 */
#define PIN_PA09A_RSTC_EXTWAKE9                    (9L)         /**< RSTC signal: RSTC_EXTWAKE9 on PA09 mux A*/
#define MUX_PA09A_RSTC_EXTWAKE9                    (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE9 */
#define PORT_PA09A_RSTC_EXTWAKE9                   (1UL << 9)   /**< RSTC signal: RSTCEXTWAKE9 */
#define PIN_PA10A_RSTC_EXTWAKE10                   (10L)        /**< RSTC signal: RSTC_EXTWAKE10 on PA10 mux A*/
#define MUX_PA10A_RSTC_EXTWAKE10                   (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE10 */
#define PORT_PA10A_RSTC_EXTWAKE10                  (1UL << 10)  /**< RSTC signal: RSTCEXTWAKE10 */
#define PIN_PA11A_RSTC_EXTWAKE11                   (11L)        /**< RSTC signal: RSTC_EXTWAKE11 on PA11 mux A*/
#define MUX_PA11A_RSTC_EXTWAKE11                   (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE11 */
#define PORT_PA11A_RSTC_EXTWAKE11                  (1UL << 11)  /**< RSTC signal: RSTCEXTWAKE11 */
#define PIN_PA12A_RSTC_EXTWAKE12                   (12L)        /**< RSTC signal: RSTC_EXTWAKE12 on PA12 mux A*/
#define MUX_PA12A_RSTC_EXTWAKE12                   (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE12 */
#define PORT_PA12A_RSTC_EXTWAKE12                  (1UL << 12)  /**< RSTC signal: RSTCEXTWAKE12 */
#define PIN_PA13A_RSTC_EXTWAKE13                   (13L)        /**< RSTC signal: RSTC_EXTWAKE13 on PA13 mux A*/
#define MUX_PA13A_RSTC_EXTWAKE13                   (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE13 */
#define PORT_PA13A_RSTC_EXTWAKE13                  (1UL << 13)  /**< RSTC signal: RSTCEXTWAKE13 */
#define PIN_PA14A_RSTC_EXTWAKE14                   (14L)        /**< RSTC signal: RSTC_EXTWAKE14 on PA14 mux A*/
#define MUX_PA14A_RSTC_EXTWAKE14                   (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE14 */
#define PORT_PA14A_RSTC_EXTWAKE14                  (1UL << 14)  /**< RSTC signal: RSTCEXTWAKE14 */
#define PIN_PA15A_RSTC_EXTWAKE15                   (15L)        /**< RSTC signal: RSTC_EXTWAKE15 on PA15 mux A*/
#define MUX_PA15A_RSTC_EXTWAKE15                   (0L)         /**< RSTC signal line function value: RSTC_EXTWAKE15 */
#define PORT_PA15A_RSTC_EXTWAKE15                  (1UL << 15)  /**< RSTC signal: RSTCEXTWAKE15 */
/* ========== PIO definition for SDADC peripheral ========== */
#define PIN_PA06B_SDADC_INN0                       (6L)         /**< SDADC signal: SDADC_INN0 on PA06 mux B*/
#define MUX_PA06B_SDADC_INN0                       (1L)         /**< SDADC signal line function value: SDADC_INN0 */
#define PORT_PA06B_SDADC_INN0                      (1UL << 6)   /**< SDADC signal: SDADCINN0 */
#define PIN_PB08B_SDADC_INN1                       (40L)        /**< SDADC signal: SDADC_INN1 on PB08 mux B*/
#define MUX_PB08B_SDADC_INN1                       (1L)         /**< SDADC signal line function value: SDADC_INN1 */
#define PORT_PB08B_SDADC_INN1                      (1UL << 8)   /**< SDADC signal: SDADCINN1 */
#define PIN_PB06B_SDADC_INN2                       (38L)        /**< SDADC signal: SDADC_INN2 on PB06 mux B*/
#define MUX_PB06B_SDADC_INN2                       (1L)         /**< SDADC signal line function value: SDADC_INN2 */
#define PORT_PB06B_SDADC_INN2                      (1UL << 6)   /**< SDADC signal: SDADCINN2 */
#define PIN_PA07B_SDADC_INP0                       (7L)         /**< SDADC signal: SDADC_INP0 on PA07 mux B*/
#define MUX_PA07B_SDADC_INP0                       (1L)         /**< SDADC signal line function value: SDADC_INP0 */
#define PORT_PA07B_SDADC_INP0                      (1UL << 7)   /**< SDADC signal: SDADCINP0 */
#define PIN_PB09B_SDADC_INP1                       (41L)        /**< SDADC signal: SDADC_INP1 on PB09 mux B*/
#define MUX_PB09B_SDADC_INP1                       (1L)         /**< SDADC signal line function value: SDADC_INP1 */
#define PORT_PB09B_SDADC_INP1                      (1UL << 9)   /**< SDADC signal: SDADCINP1 */
#define PIN_PB07B_SDADC_INP2                       (39L)        /**< SDADC signal: SDADC_INP2 on PB07 mux B*/
#define MUX_PB07B_SDADC_INP2                       (1L)         /**< SDADC signal line function value: SDADC_INP2 */
#define PORT_PB07B_SDADC_INP2                      (1UL << 7)   /**< SDADC signal: SDADCINP2 */
#define PIN_PA04B_SDADC_VREFP                      (4L)         /**< SDADC signal: SDADC_VREFP on PA04 mux B*/
#define MUX_PA04B_SDADC_VREFP                      (1L)         /**< SDADC signal line function value: SDADC_VREFP */
#define PORT_PA04B_SDADC_VREFP                     (1UL << 4)   /**< SDADC signal: SDADCVREFP */
/* ========== PIO definition for SERCOM0 peripheral ========== */
#define PIN_PA04D_SERCOM0_PAD0                     (4L)         /**< SERCOM0 signal: SERCOM0_PAD0 on PA04 mux D*/
#define MUX_PA04D_SERCOM0_PAD0                     (3L)         /**< SERCOM0 signal line function value: SERCOM0_PAD0 */
#define PORT_PA04D_SERCOM0_PAD0                    (1UL << 4)   /**< SERCOM0 signal: SERCOM0PAD0 */
#define PIN_PA08C_SERCOM0_PAD0                     (8L)         /**< SERCOM0 signal: SERCOM0_PAD0 on PA08 mux C*/
#define MUX_PA08C_SERCOM0_PAD0                     (2L)         /**< SERCOM0 signal line function value: SERCOM0_PAD0 */
#define PORT_PA08C_SERCOM0_PAD0                    (1UL << 8)   /**< SERCOM0 signal: SERCOM0PAD0 */
#define PIN_PB24C_SERCOM0_PAD0                     (56L)        /**< SERCOM0 signal: SERCOM0_PAD0 on PB24 mux C*/
#define MUX_PB24C_SERCOM0_PAD0                     (2L)         /**< SERCOM0 signal line function value: SERCOM0_PAD0 */
#define PORT_PB24C_SERCOM0_PAD0                    (1UL << 24)  /**< SERCOM0 signal: SERCOM0PAD0 */
#define PIN_PA05D_SERCOM0_PAD1                     (5L)         /**< SERCOM0 signal: SERCOM0_PAD1 on PA05 mux D*/
#define MUX_PA05D_SERCOM0_PAD1                     (3L)         /**< SERCOM0 signal line function value: SERCOM0_PAD1 */
#define PORT_PA05D_SERCOM0_PAD1                    (1UL << 5)   /**< SERCOM0 signal: SERCOM0PAD1 */
#define PIN_PA09C_SERCOM0_PAD1                     (9L)         /**< SERCOM0 signal: SERCOM0_PAD1 on PA09 mux C*/
#define MUX_PA09C_SERCOM0_PAD1                     (2L)         /**< SERCOM0 signal line function value: SERCOM0_PAD1 */
#define PORT_PA09C_SERCOM0_PAD1                    (1UL << 9)   /**< SERCOM0 signal: SERCOM0PAD1 */
#define PIN_PB25C_SERCOM0_PAD1                     (57L)        /**< SERCOM0 signal: SERCOM0_PAD1 on PB25 mux C*/
#define MUX_PB25C_SERCOM0_PAD1                     (2L)         /**< SERCOM0 signal line function value: SERCOM0_PAD1 */
#define PORT_PB25C_SERCOM0_PAD1                    (1UL << 25)  /**< SERCOM0 signal: SERCOM0PAD1 */
#define PIN_PA06D_SERCOM0_PAD2                     (6L)         /**< SERCOM0 signal: SERCOM0_PAD2 on PA06 mux D*/
#define MUX_PA06D_SERCOM0_PAD2                     (3L)         /**< SERCOM0 signal line function value: SERCOM0_PAD2 */
#define PORT_PA06D_SERCOM0_PAD2                    (1UL << 6)   /**< SERCOM0 signal: SERCOM0PAD2 */
#define PIN_PB22C_SERCOM0_PAD2                     (54L)        /**< SERCOM0 signal: SERCOM0_PAD2 on PB22 mux C*/
#define MUX_PB22C_SERCOM0_PAD2                     (2L)         /**< SERCOM0 signal line function value: SERCOM0_PAD2 */
#define PORT_PB22C_SERCOM0_PAD2                    (1UL << 22)  /**< SERCOM0 signal: SERCOM0PAD2 */
#define PIN_PA10C_SERCOM0_PAD2                     (10L)        /**< SERCOM0 signal: SERCOM0_PAD2 on PA10 mux C*/
#define MUX_PA10C_SERCOM0_PAD2                     (2L)         /**< SERCOM0 signal line function value: SERCOM0_PAD2 */
#define PORT_PA10C_SERCOM0_PAD2                    (1UL << 10)  /**< SERCOM0 signal: SERCOM0PAD2 */
#define PIN_PC24C_SERCOM0_PAD2                     (88L)        /**< SERCOM0 signal: SERCOM0_PAD2 on PC24 mux C*/
#define MUX_PC24C_SERCOM0_PAD2                     (2L)         /**< SERCOM0 signal line function value: SERCOM0_PAD2 */
#define PORT_PC24C_SERCOM0_PAD2                    (1UL << 24)  /**< SERCOM0 signal: SERCOM0PAD2 */
#define PIN_PA07D_SERCOM0_PAD3                     (7L)         /**< SERCOM0 signal: SERCOM0_PAD3 on PA07 mux D*/
#define MUX_PA07D_SERCOM0_PAD3                     (3L)         /**< SERCOM0 signal line function value: SERCOM0_PAD3 */
#define PORT_PA07D_SERCOM0_PAD3                    (1UL << 7)   /**< SERCOM0 signal: SERCOM0PAD3 */
#define PIN_PA11C_SERCOM0_PAD3                     (11L)        /**< SERCOM0 signal: SERCOM0_PAD3 on PA11 mux C*/
#define MUX_PA11C_SERCOM0_PAD3                     (2L)         /**< SERCOM0 signal line function value: SERCOM0_PAD3 */
#define PORT_PA11C_SERCOM0_PAD3                    (1UL << 11)  /**< SERCOM0 signal: SERCOM0PAD3 */
#define PIN_PB23C_SERCOM0_PAD3                     (55L)        /**< SERCOM0 signal: SERCOM0_PAD3 on PB23 mux C*/
#define MUX_PB23C_SERCOM0_PAD3                     (2L)         /**< SERCOM0 signal line function value: SERCOM0_PAD3 */
#define PORT_PB23C_SERCOM0_PAD3                    (1UL << 23)  /**< SERCOM0 signal: SERCOM0PAD3 */
#define PIN_PC25C_SERCOM0_PAD3                     (89L)        /**< SERCOM0 signal: SERCOM0_PAD3 on PC25 mux C*/
#define MUX_PC25C_SERCOM0_PAD3                     (2L)         /**< SERCOM0 signal line function value: SERCOM0_PAD3 */
#define PORT_PC25C_SERCOM0_PAD3                    (1UL << 25)  /**< SERCOM0 signal: SERCOM0PAD3 */
/* ========== PIO definition for SERCOM1 peripheral ========== */
#define PIN_PC27D_SERCOM1_PAD0                     (91L)        /**< SERCOM1 signal: SERCOM1_PAD0 on PC27 mux D*/
#define MUX_PC27D_SERCOM1_PAD0                     (3L)         /**< SERCOM1 signal line function value: SERCOM1_PAD0 */
#define PORT_PC27D_SERCOM1_PAD0                    (1UL << 27)  /**< SERCOM1 signal: SERCOM1PAD0 */
#define PIN_PA16C_SERCOM1_PAD0                     (16L)        /**< SERCOM1 signal: SERCOM1_PAD0 on PA16 mux C*/
#define MUX_PA16C_SERCOM1_PAD0                     (2L)         /**< SERCOM1 signal line function value: SERCOM1_PAD0 */
#define PORT_PA16C_SERCOM1_PAD0                    (1UL << 16)  /**< SERCOM1 signal: SERCOM1PAD0 */
#define PIN_PB30C_SERCOM1_PAD0                     (62L)        /**< SERCOM1 signal: SERCOM1_PAD0 on PB30 mux C*/
#define MUX_PB30C_SERCOM1_PAD0                     (2L)         /**< SERCOM1 signal line function value: SERCOM1_PAD0 */
#define PORT_PB30C_SERCOM1_PAD0                    (1UL << 30)  /**< SERCOM1 signal: SERCOM1PAD0 */
#define PIN_PA00D_SERCOM1_PAD0                     (0L)         /**< SERCOM1 signal: SERCOM1_PAD0 on PA00 mux D*/
#define MUX_PA00D_SERCOM1_PAD0                     (3L)         /**< SERCOM1 signal line function value: SERCOM1_PAD0 */
#define PORT_PA00D_SERCOM1_PAD0                    (1UL << 0)   /**< SERCOM1 signal: SERCOM1PAD0 */
#define PIN_PC28D_SERCOM1_PAD1                     (92L)        /**< SERCOM1 signal: SERCOM1_PAD1 on PC28 mux D*/
#define MUX_PC28D_SERCOM1_PAD1                     (3L)         /**< SERCOM1 signal line function value: SERCOM1_PAD1 */
#define PORT_PC28D_SERCOM1_PAD1                    (1UL << 28)  /**< SERCOM1 signal: SERCOM1PAD1 */
#define PIN_PA17C_SERCOM1_PAD1                     (17L)        /**< SERCOM1 signal: SERCOM1_PAD1 on PA17 mux C*/
#define MUX_PA17C_SERCOM1_PAD1                     (2L)         /**< SERCOM1 signal line function value: SERCOM1_PAD1 */
#define PORT_PA17C_SERCOM1_PAD1                    (1UL << 17)  /**< SERCOM1 signal: SERCOM1PAD1 */
#define PIN_PB31C_SERCOM1_PAD1                     (63L)        /**< SERCOM1 signal: SERCOM1_PAD1 on PB31 mux C*/
#define MUX_PB31C_SERCOM1_PAD1                     (2L)         /**< SERCOM1 signal line function value: SERCOM1_PAD1 */
#define PORT_PB31C_SERCOM1_PAD1                    (1UL << 31)  /**< SERCOM1 signal: SERCOM1PAD1 */
#define PIN_PA01D_SERCOM1_PAD1                     (1L)         /**< SERCOM1 signal: SERCOM1_PAD1 on PA01 mux D*/
#define MUX_PA01D_SERCOM1_PAD1                     (3L)         /**< SERCOM1 signal line function value: SERCOM1_PAD1 */
#define PORT_PA01D_SERCOM1_PAD1                    (1UL << 1)   /**< SERCOM1 signal: SERCOM1PAD1 */
#define PIN_PA30D_SERCOM1_PAD2                     (30L)        /**< SERCOM1 signal: SERCOM1_PAD2 on PA30 mux D*/
#define MUX_PA30D_SERCOM1_PAD2                     (3L)         /**< SERCOM1 signal line function value: SERCOM1_PAD2 */
#define PORT_PA30D_SERCOM1_PAD2                    (1UL << 30)  /**< SERCOM1 signal: SERCOM1PAD2 */
#define PIN_PA18C_SERCOM1_PAD2                     (18L)        /**< SERCOM1 signal: SERCOM1_PAD2 on PA18 mux C*/
#define MUX_PA18C_SERCOM1_PAD2                     (2L)         /**< SERCOM1 signal line function value: SERCOM1_PAD2 */
#define PORT_PA18C_SERCOM1_PAD2                    (1UL << 18)  /**< SERCOM1 signal: SERCOM1PAD2 */
#define PIN_PA31D_SERCOM1_PAD3                     (31L)        /**< SERCOM1 signal: SERCOM1_PAD3 on PA31 mux D*/
#define MUX_PA31D_SERCOM1_PAD3                     (3L)         /**< SERCOM1 signal line function value: SERCOM1_PAD3 */
#define PORT_PA31D_SERCOM1_PAD3                    (1UL << 31)  /**< SERCOM1 signal: SERCOM1PAD3 */
#define PIN_PA19C_SERCOM1_PAD3                     (19L)        /**< SERCOM1 signal: SERCOM1_PAD3 on PA19 mux C*/
#define MUX_PA19C_SERCOM1_PAD3                     (2L)         /**< SERCOM1 signal line function value: SERCOM1_PAD3 */
#define PORT_PA19C_SERCOM1_PAD3                    (1UL << 19)  /**< SERCOM1 signal: SERCOM1PAD3 */
/* ========== PIO definition for SERCOM2 peripheral ========== */
#define PIN_PA08D_SERCOM2_PAD0                     (8L)         /**< SERCOM2 signal: SERCOM2_PAD0 on PA08 mux D*/
#define MUX_PA08D_SERCOM2_PAD0                     (3L)         /**< SERCOM2 signal line function value: SERCOM2_PAD0 */
#define PORT_PA08D_SERCOM2_PAD0                    (1UL << 8)   /**< SERCOM2 signal: SERCOM2PAD0 */
#define PIN_PB20D_SERCOM2_PAD0                     (52L)        /**< SERCOM2 signal: SERCOM2_PAD0 on PB20 mux D*/
#define MUX_PB20D_SERCOM2_PAD0                     (3L)         /**< SERCOM2 signal line function value: SERCOM2_PAD0 */
#define PORT_PB20D_SERCOM2_PAD0                    (1UL << 20)  /**< SERCOM2 signal: SERCOM2PAD0 */
#define PIN_PA12C_SERCOM2_PAD0                     (12L)        /**< SERCOM2 signal: SERCOM2_PAD0 on PA12 mux C*/
#define MUX_PA12C_SERCOM2_PAD0                     (2L)         /**< SERCOM2 signal line function value: SERCOM2_PAD0 */
#define PORT_PA12C_SERCOM2_PAD0                    (1UL << 12)  /**< SERCOM2 signal: SERCOM2PAD0 */
#define PIN_PA09D_SERCOM2_PAD1                     (9L)         /**< SERCOM2 signal: SERCOM2_PAD1 on PA09 mux D*/
#define MUX_PA09D_SERCOM2_PAD1                     (3L)         /**< SERCOM2 signal line function value: SERCOM2_PAD1 */
#define PORT_PA09D_SERCOM2_PAD1                    (1UL << 9)   /**< SERCOM2 signal: SERCOM2PAD1 */
#define PIN_PB21D_SERCOM2_PAD1                     (53L)        /**< SERCOM2 signal: SERCOM2_PAD1 on PB21 mux D*/
#define MUX_PB21D_SERCOM2_PAD1                     (3L)         /**< SERCOM2 signal line function value: SERCOM2_PAD1 */
#define PORT_PB21D_SERCOM2_PAD1                    (1UL << 21)  /**< SERCOM2 signal: SERCOM2PAD1 */
#define PIN_PA13C_SERCOM2_PAD1                     (13L)        /**< SERCOM2 signal: SERCOM2_PAD1 on PA13 mux C*/
#define MUX_PA13C_SERCOM2_PAD1                     (2L)         /**< SERCOM2 signal line function value: SERCOM2_PAD1 */
#define PORT_PA13C_SERCOM2_PAD1                    (1UL << 13)  /**< SERCOM2 signal: SERCOM2PAD1 */
#define PIN_PA10D_SERCOM2_PAD2                     (10L)        /**< SERCOM2 signal: SERCOM2_PAD2 on PA10 mux D*/
#define MUX_PA10D_SERCOM2_PAD2                     (3L)         /**< SERCOM2 signal line function value: SERCOM2_PAD2 */
#define PORT_PA10D_SERCOM2_PAD2                    (1UL << 10)  /**< SERCOM2 signal: SERCOM2PAD2 */
#define PIN_PA14C_SERCOM2_PAD2                     (14L)        /**< SERCOM2 signal: SERCOM2_PAD2 on PA14 mux C*/
#define MUX_PA14C_SERCOM2_PAD2                     (2L)         /**< SERCOM2 signal line function value: SERCOM2_PAD2 */
#define PORT_PA14C_SERCOM2_PAD2                    (1UL << 14)  /**< SERCOM2 signal: SERCOM2PAD2 */
#define PIN_PA11D_SERCOM2_PAD3                     (11L)        /**< SERCOM2 signal: SERCOM2_PAD3 on PA11 mux D*/
#define MUX_PA11D_SERCOM2_PAD3                     (3L)         /**< SERCOM2 signal line function value: SERCOM2_PAD3 */
#define PORT_PA11D_SERCOM2_PAD3                    (1UL << 11)  /**< SERCOM2 signal: SERCOM2PAD3 */
#define PIN_PA15C_SERCOM2_PAD3                     (15L)        /**< SERCOM2 signal: SERCOM2_PAD3 on PA15 mux C*/
#define MUX_PA15C_SERCOM2_PAD3                     (2L)         /**< SERCOM2 signal line function value: SERCOM2_PAD3 */
#define PORT_PA15C_SERCOM2_PAD3                    (1UL << 15)  /**< SERCOM2 signal: SERCOM2PAD3 */
/* ========== PIO definition for SERCOM3 peripheral ========== */
#define PIN_PA16D_SERCOM3_PAD0                     (16L)        /**< SERCOM3 signal: SERCOM3_PAD0 on PA16 mux D*/
#define MUX_PA16D_SERCOM3_PAD0                     (3L)         /**< SERCOM3 signal line function value: SERCOM3_PAD0 */
#define PORT_PA16D_SERCOM3_PAD0                    (1UL << 16)  /**< SERCOM3 signal: SERCOM3PAD0 */
#define PIN_PA22C_SERCOM3_PAD0                     (22L)        /**< SERCOM3 signal: SERCOM3_PAD0 on PA22 mux C*/
#define MUX_PA22C_SERCOM3_PAD0                     (2L)         /**< SERCOM3 signal line function value: SERCOM3_PAD0 */
#define PORT_PA22C_SERCOM3_PAD0                    (1UL << 22)  /**< SERCOM3 signal: SERCOM3PAD0 */
#define PIN_PB20C_SERCOM3_PAD0                     (52L)        /**< SERCOM3 signal: SERCOM3_PAD0 on PB20 mux C*/
#define MUX_PB20C_SERCOM3_PAD0                     (2L)         /**< SERCOM3 signal line function value: SERCOM3_PAD0 */
#define PORT_PB20C_SERCOM3_PAD0                    (1UL << 20)  /**< SERCOM3 signal: SERCOM3PAD0 */
#define PIN_PA17D_SERCOM3_PAD1                     (17L)        /**< SERCOM3 signal: SERCOM3_PAD1 on PA17 mux D*/
#define MUX_PA17D_SERCOM3_PAD1                     (3L)         /**< SERCOM3 signal line function value: SERCOM3_PAD1 */
#define PORT_PA17D_SERCOM3_PAD1                    (1UL << 17)  /**< SERCOM3 signal: SERCOM3PAD1 */
#define PIN_PA23C_SERCOM3_PAD1                     (23L)        /**< SERCOM3 signal: SERCOM3_PAD1 on PA23 mux C*/
#define MUX_PA23C_SERCOM3_PAD1                     (2L)         /**< SERCOM3 signal line function value: SERCOM3_PAD1 */
#define PORT_PA23C_SERCOM3_PAD1                    (1UL << 23)  /**< SERCOM3 signal: SERCOM3PAD1 */
#define PIN_PB21C_SERCOM3_PAD1                     (53L)        /**< SERCOM3 signal: SERCOM3_PAD1 on PB21 mux C*/
#define MUX_PB21C_SERCOM3_PAD1                     (2L)         /**< SERCOM3 signal line function value: SERCOM3_PAD1 */
#define PORT_PB21C_SERCOM3_PAD1                    (1UL << 21)  /**< SERCOM3 signal: SERCOM3PAD1 */
#define PIN_PA18D_SERCOM3_PAD2                     (18L)        /**< SERCOM3 signal: SERCOM3_PAD2 on PA18 mux D*/
#define MUX_PA18D_SERCOM3_PAD2                     (3L)         /**< SERCOM3 signal line function value: SERCOM3_PAD2 */
#define PORT_PA18D_SERCOM3_PAD2                    (1UL << 18)  /**< SERCOM3 signal: SERCOM3PAD2 */
#define PIN_PB18D_SERCOM3_PAD2                     (50L)        /**< SERCOM3 signal: SERCOM3_PAD2 on PB18 mux D*/
#define MUX_PB18D_SERCOM3_PAD2                     (3L)         /**< SERCOM3 signal line function value: SERCOM3_PAD2 */
#define PORT_PB18D_SERCOM3_PAD2                    (1UL << 18)  /**< SERCOM3 signal: SERCOM3PAD2 */
#define PIN_PA20D_SERCOM3_PAD2                     (20L)        /**< SERCOM3 signal: SERCOM3_PAD2 on PA20 mux D*/
#define MUX_PA20D_SERCOM3_PAD2                     (3L)         /**< SERCOM3 signal line function value: SERCOM3_PAD2 */
#define PORT_PA20D_SERCOM3_PAD2                    (1UL << 20)  /**< SERCOM3 signal: SERCOM3PAD2 */
#define PIN_PA24C_SERCOM3_PAD2                     (24L)        /**< SERCOM3 signal: SERCOM3_PAD2 on PA24 mux C*/
#define MUX_PA24C_SERCOM3_PAD2                     (2L)         /**< SERCOM3 signal line function value: SERCOM3_PAD2 */
#define PORT_PA24C_SERCOM3_PAD2                    (1UL << 24)  /**< SERCOM3 signal: SERCOM3PAD2 */
#define PIN_PA19D_SERCOM3_PAD3                     (19L)        /**< SERCOM3 signal: SERCOM3_PAD3 on PA19 mux D*/
#define MUX_PA19D_SERCOM3_PAD3                     (3L)         /**< SERCOM3 signal line function value: SERCOM3_PAD3 */
#define PORT_PA19D_SERCOM3_PAD3                    (1UL << 19)  /**< SERCOM3 signal: SERCOM3PAD3 */
#define PIN_PA25C_SERCOM3_PAD3                     (25L)        /**< SERCOM3 signal: SERCOM3_PAD3 on PA25 mux C*/
#define MUX_PA25C_SERCOM3_PAD3                     (2L)         /**< SERCOM3 signal line function value: SERCOM3_PAD3 */
#define PORT_PA25C_SERCOM3_PAD3                    (1UL << 25)  /**< SERCOM3 signal: SERCOM3PAD3 */
#define PIN_PA21D_SERCOM3_PAD3                     (21L)        /**< SERCOM3 signal: SERCOM3_PAD3 on PA21 mux D*/
#define MUX_PA21D_SERCOM3_PAD3                     (3L)         /**< SERCOM3 signal line function value: SERCOM3_PAD3 */
#define PORT_PA21D_SERCOM3_PAD3                    (1UL << 21)  /**< SERCOM3 signal: SERCOM3PAD3 */
#define PIN_PB19D_SERCOM3_PAD3                     (51L)        /**< SERCOM3 signal: SERCOM3_PAD3 on PB19 mux D*/
#define MUX_PB19D_SERCOM3_PAD3                     (3L)         /**< SERCOM3 signal line function value: SERCOM3_PAD3 */
#define PORT_PB19D_SERCOM3_PAD3                    (1UL << 19)  /**< SERCOM3 signal: SERCOM3PAD3 */
/* ========== PIO definition for SERCOM4 peripheral ========== */
#define PIN_PA12D_SERCOM4_PAD0                     (12L)        /**< SERCOM4 signal: SERCOM4_PAD0 on PA12 mux D*/
#define MUX_PA12D_SERCOM4_PAD0                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD0 */
#define PORT_PA12D_SERCOM4_PAD0                    (1UL << 12)  /**< SERCOM4 signal: SERCOM4PAD0 */
#define PIN_PB24D_SERCOM4_PAD0                     (56L)        /**< SERCOM4 signal: SERCOM4_PAD0 on PB24 mux D*/
#define MUX_PB24D_SERCOM4_PAD0                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD0 */
#define PORT_PB24D_SERCOM4_PAD0                    (1UL << 24)  /**< SERCOM4 signal: SERCOM4PAD0 */
#define PIN_PB12C_SERCOM4_PAD0                     (44L)        /**< SERCOM4 signal: SERCOM4_PAD0 on PB12 mux C*/
#define MUX_PB12C_SERCOM4_PAD0                     (2L)         /**< SERCOM4 signal line function value: SERCOM4_PAD0 */
#define PORT_PB12C_SERCOM4_PAD0                    (1UL << 12)  /**< SERCOM4 signal: SERCOM4PAD0 */
#define PIN_PA13D_SERCOM4_PAD1                     (13L)        /**< SERCOM4 signal: SERCOM4_PAD1 on PA13 mux D*/
#define MUX_PA13D_SERCOM4_PAD1                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD1 */
#define PORT_PA13D_SERCOM4_PAD1                    (1UL << 13)  /**< SERCOM4 signal: SERCOM4PAD1 */
#define PIN_PB09D_SERCOM4_PAD1                     (41L)        /**< SERCOM4 signal: SERCOM4_PAD1 on PB09 mux D*/
#define MUX_PB09D_SERCOM4_PAD1                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD1 */
#define PORT_PB09D_SERCOM4_PAD1                    (1UL << 9)   /**< SERCOM4 signal: SERCOM4PAD1 */
#define PIN_PB25D_SERCOM4_PAD1                     (57L)        /**< SERCOM4 signal: SERCOM4_PAD1 on PB25 mux D*/
#define MUX_PB25D_SERCOM4_PAD1                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD1 */
#define PORT_PB25D_SERCOM4_PAD1                    (1UL << 25)  /**< SERCOM4 signal: SERCOM4PAD1 */
#define PIN_PB13C_SERCOM4_PAD1                     (45L)        /**< SERCOM4 signal: SERCOM4_PAD1 on PB13 mux C*/
#define MUX_PB13C_SERCOM4_PAD1                     (2L)         /**< SERCOM4 signal line function value: SERCOM4_PAD1 */
#define PORT_PB13C_SERCOM4_PAD1                    (1UL << 13)  /**< SERCOM4 signal: SERCOM4PAD1 */
#define PIN_PA14D_SERCOM4_PAD2                     (14L)        /**< SERCOM4 signal: SERCOM4_PAD2 on PA14 mux D*/
#define MUX_PA14D_SERCOM4_PAD2                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD2 */
#define PORT_PA14D_SERCOM4_PAD2                    (1UL << 14)  /**< SERCOM4 signal: SERCOM4PAD2 */
#define PIN_PB10D_SERCOM4_PAD2                     (42L)        /**< SERCOM4 signal: SERCOM4_PAD2 on PB10 mux D*/
#define MUX_PB10D_SERCOM4_PAD2                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD2 */
#define PORT_PB10D_SERCOM4_PAD2                    (1UL << 10)  /**< SERCOM4 signal: SERCOM4PAD2 */
#define PIN_PB14C_SERCOM4_PAD2                     (46L)        /**< SERCOM4 signal: SERCOM4_PAD2 on PB14 mux C*/
#define MUX_PB14C_SERCOM4_PAD2                     (2L)         /**< SERCOM4 signal line function value: SERCOM4_PAD2 */
#define PORT_PB14C_SERCOM4_PAD2                    (1UL << 14)  /**< SERCOM4 signal: SERCOM4PAD2 */
#define PIN_PC24D_SERCOM4_PAD2                     (88L)        /**< SERCOM4 signal: SERCOM4_PAD2 on PC24 mux D*/
#define MUX_PC24D_SERCOM4_PAD2                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD2 */
#define PORT_PC24D_SERCOM4_PAD2                    (1UL << 24)  /**< SERCOM4 signal: SERCOM4PAD2 */
#define PIN_PA15D_SERCOM4_PAD3                     (15L)        /**< SERCOM4 signal: SERCOM4_PAD3 on PA15 mux D*/
#define MUX_PA15D_SERCOM4_PAD3                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD3 */
#define PORT_PA15D_SERCOM4_PAD3                    (1UL << 15)  /**< SERCOM4 signal: SERCOM4PAD3 */
#define PIN_PB11D_SERCOM4_PAD3                     (43L)        /**< SERCOM4 signal: SERCOM4_PAD3 on PB11 mux D*/
#define MUX_PB11D_SERCOM4_PAD3                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD3 */
#define PORT_PB11D_SERCOM4_PAD3                    (1UL << 11)  /**< SERCOM4 signal: SERCOM4PAD3 */
#define PIN_PC25D_SERCOM4_PAD3                     (89L)        /**< SERCOM4 signal: SERCOM4_PAD3 on PC25 mux D*/
#define MUX_PC25D_SERCOM4_PAD3                     (3L)         /**< SERCOM4 signal line function value: SERCOM4_PAD3 */
#define PORT_PC25D_SERCOM4_PAD3                    (1UL << 25)  /**< SERCOM4 signal: SERCOM4PAD3 */
#define PIN_PB15C_SERCOM4_PAD3                     (47L)        /**< SERCOM4 signal: SERCOM4_PAD3 on PB15 mux C*/
#define MUX_PB15C_SERCOM4_PAD3                     (2L)         /**< SERCOM4 signal line function value: SERCOM4_PAD3 */
#define PORT_PB15C_SERCOM4_PAD3                    (1UL << 15)  /**< SERCOM4 signal: SERCOM4PAD3 */
/* ========== PIO definition for SERCOM5 peripheral ========== */
#define PIN_PA22D_SERCOM5_PAD0                     (22L)        /**< SERCOM5 signal: SERCOM5_PAD0 on PA22 mux D*/
#define MUX_PA22D_SERCOM5_PAD0                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD0 */
#define PORT_PA22D_SERCOM5_PAD0                    (1UL << 22)  /**< SERCOM5 signal: SERCOM5PAD0 */
#define PIN_PB02D_SERCOM5_PAD0                     (34L)        /**< SERCOM5 signal: SERCOM5_PAD0 on PB02 mux D*/
#define MUX_PB02D_SERCOM5_PAD0                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD0 */
#define PORT_PB02D_SERCOM5_PAD0                    (1UL << 2)   /**< SERCOM5 signal: SERCOM5PAD0 */
#define PIN_PB16C_SERCOM5_PAD0                     (48L)        /**< SERCOM5 signal: SERCOM5_PAD0 on PB16 mux C*/
#define MUX_PB16C_SERCOM5_PAD0                     (2L)         /**< SERCOM5 signal line function value: SERCOM5_PAD0 */
#define PORT_PB16C_SERCOM5_PAD0                    (1UL << 16)  /**< SERCOM5 signal: SERCOM5PAD0 */
#define PIN_PB30D_SERCOM5_PAD0                     (62L)        /**< SERCOM5 signal: SERCOM5_PAD0 on PB30 mux D*/
#define MUX_PB30D_SERCOM5_PAD0                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD0 */
#define PORT_PB30D_SERCOM5_PAD0                    (1UL << 30)  /**< SERCOM5 signal: SERCOM5PAD0 */
#define PIN_PB03D_SERCOM5_PAD1                     (35L)        /**< SERCOM5 signal: SERCOM5_PAD1 on PB03 mux D*/
#define MUX_PB03D_SERCOM5_PAD1                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD1 */
#define PORT_PB03D_SERCOM5_PAD1                    (1UL << 3)   /**< SERCOM5 signal: SERCOM5PAD1 */
#define PIN_PB31D_SERCOM5_PAD1                     (63L)        /**< SERCOM5 signal: SERCOM5_PAD1 on PB31 mux D*/
#define MUX_PB31D_SERCOM5_PAD1                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD1 */
#define PORT_PB31D_SERCOM5_PAD1                    (1UL << 31)  /**< SERCOM5 signal: SERCOM5PAD1 */
#define PIN_PB17C_SERCOM5_PAD1                     (49L)        /**< SERCOM5 signal: SERCOM5_PAD1 on PB17 mux C*/
#define MUX_PB17C_SERCOM5_PAD1                     (2L)         /**< SERCOM5 signal line function value: SERCOM5_PAD1 */
#define PORT_PB17C_SERCOM5_PAD1                    (1UL << 17)  /**< SERCOM5 signal: SERCOM5PAD1 */
#define PIN_PA23D_SERCOM5_PAD1                     (23L)        /**< SERCOM5 signal: SERCOM5_PAD1 on PA23 mux D*/
#define MUX_PA23D_SERCOM5_PAD1                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD1 */
#define PORT_PA23D_SERCOM5_PAD1                    (1UL << 23)  /**< SERCOM5 signal: SERCOM5PAD1 */
#define PIN_PB00D_SERCOM5_PAD2                     (32L)        /**< SERCOM5 signal: SERCOM5_PAD2 on PB00 mux D*/
#define MUX_PB00D_SERCOM5_PAD2                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD2 */
#define PORT_PB00D_SERCOM5_PAD2                    (1UL << 0)   /**< SERCOM5 signal: SERCOM5PAD2 */
#define PIN_PB22D_SERCOM5_PAD2                     (54L)        /**< SERCOM5 signal: SERCOM5_PAD2 on PB22 mux D*/
#define MUX_PB22D_SERCOM5_PAD2                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD2 */
#define PORT_PB22D_SERCOM5_PAD2                    (1UL << 22)  /**< SERCOM5 signal: SERCOM5PAD2 */
#define PIN_PB18C_SERCOM5_PAD2                     (50L)        /**< SERCOM5 signal: SERCOM5_PAD2 on PB18 mux C*/
#define MUX_PB18C_SERCOM5_PAD2                     (2L)         /**< SERCOM5 signal line function value: SERCOM5_PAD2 */
#define PORT_PB18C_SERCOM5_PAD2                    (1UL << 18)  /**< SERCOM5 signal: SERCOM5PAD2 */
#define PIN_PA24D_SERCOM5_PAD2                     (24L)        /**< SERCOM5 signal: SERCOM5_PAD2 on PA24 mux D*/
#define MUX_PA24D_SERCOM5_PAD2                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD2 */
#define PORT_PA24D_SERCOM5_PAD2                    (1UL << 24)  /**< SERCOM5 signal: SERCOM5PAD2 */
#define PIN_PA20C_SERCOM5_PAD2                     (20L)        /**< SERCOM5 signal: SERCOM5_PAD2 on PA20 mux C*/
#define MUX_PA20C_SERCOM5_PAD2                     (2L)         /**< SERCOM5 signal line function value: SERCOM5_PAD2 */
#define PORT_PA20C_SERCOM5_PAD2                    (1UL << 20)  /**< SERCOM5 signal: SERCOM5PAD2 */
#define PIN_PA25D_SERCOM5_PAD3                     (25L)        /**< SERCOM5 signal: SERCOM5_PAD3 on PA25 mux D*/
#define MUX_PA25D_SERCOM5_PAD3                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD3 */
#define PORT_PA25D_SERCOM5_PAD3                    (1UL << 25)  /**< SERCOM5 signal: SERCOM5PAD3 */
#define PIN_PB01D_SERCOM5_PAD3                     (33L)        /**< SERCOM5 signal: SERCOM5_PAD3 on PB01 mux D*/
#define MUX_PB01D_SERCOM5_PAD3                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD3 */
#define PORT_PB01D_SERCOM5_PAD3                    (1UL << 1)   /**< SERCOM5 signal: SERCOM5PAD3 */
#define PIN_PB23D_SERCOM5_PAD3                     (55L)        /**< SERCOM5 signal: SERCOM5_PAD3 on PB23 mux D*/
#define MUX_PB23D_SERCOM5_PAD3                     (3L)         /**< SERCOM5 signal line function value: SERCOM5_PAD3 */
#define PORT_PB23D_SERCOM5_PAD3                    (1UL << 23)  /**< SERCOM5 signal: SERCOM5PAD3 */
#define PIN_PA21C_SERCOM5_PAD3                     (21L)        /**< SERCOM5 signal: SERCOM5_PAD3 on PA21 mux C*/
#define MUX_PA21C_SERCOM5_PAD3                     (2L)         /**< SERCOM5 signal line function value: SERCOM5_PAD3 */
#define PORT_PA21C_SERCOM5_PAD3                    (1UL << 21)  /**< SERCOM5 signal: SERCOM5PAD3 */
#define PIN_PB19C_SERCOM5_PAD3                     (51L)        /**< SERCOM5 signal: SERCOM5_PAD3 on PB19 mux C*/
#define MUX_PB19C_SERCOM5_PAD3                     (2L)         /**< SERCOM5 signal line function value: SERCOM5_PAD3 */
#define PORT_PB19C_SERCOM5_PAD3                    (1UL << 19)  /**< SERCOM5 signal: SERCOM5PAD3 */
/* ========== PIO definition for SERCOM6 peripheral ========== */
#define PIN_PC06C_SERCOM6_PAD0                     (70L)        /**< SERCOM6 signal: SERCOM6_PAD0 on PC06 mux C*/
#define MUX_PC06C_SERCOM6_PAD0                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD0 */
#define PORT_PC06C_SERCOM6_PAD0                    (1UL << 6)   /**< SERCOM6 signal: SERCOM6PAD0 */
#define PIN_PC16C_SERCOM6_PAD0                     (80L)        /**< SERCOM6 signal: SERCOM6_PAD0 on PC16 mux C*/
#define MUX_PC16C_SERCOM6_PAD0                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD0 */
#define PORT_PC16C_SERCOM6_PAD0                    (1UL << 16)  /**< SERCOM6 signal: SERCOM6PAD0 */
#define PIN_PC08C_SERCOM6_PAD0                     (72L)        /**< SERCOM6 signal: SERCOM6_PAD0 on PC08 mux C*/
#define MUX_PC08C_SERCOM6_PAD0                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD0 */
#define PORT_PC08C_SERCOM6_PAD0                    (1UL << 8)   /**< SERCOM6 signal: SERCOM6PAD0 */
#define PIN_PC07C_SERCOM6_PAD1                     (71L)        /**< SERCOM6 signal: SERCOM6_PAD1 on PC07 mux C*/
#define MUX_PC07C_SERCOM6_PAD1                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD1 */
#define PORT_PC07C_SERCOM6_PAD1                    (1UL << 7)   /**< SERCOM6 signal: SERCOM6PAD1 */
#define PIN_PC17C_SERCOM6_PAD1                     (81L)        /**< SERCOM6 signal: SERCOM6_PAD1 on PC17 mux C*/
#define MUX_PC17C_SERCOM6_PAD1                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD1 */
#define PORT_PC17C_SERCOM6_PAD1                    (1UL << 17)  /**< SERCOM6 signal: SERCOM6PAD1 */
#define PIN_PC09C_SERCOM6_PAD1                     (73L)        /**< SERCOM6 signal: SERCOM6_PAD1 on PC09 mux C*/
#define MUX_PC09C_SERCOM6_PAD1                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD1 */
#define PORT_PC09C_SERCOM6_PAD1                    (1UL << 9)   /**< SERCOM6 signal: SERCOM6PAD1 */
#define PIN_PC18C_SERCOM6_PAD2                     (82L)        /**< SERCOM6 signal: SERCOM6_PAD2 on PC18 mux C*/
#define MUX_PC18C_SERCOM6_PAD2                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD2 */
#define PORT_PC18C_SERCOM6_PAD2                    (1UL << 18)  /**< SERCOM6 signal: SERCOM6PAD2 */
#define PIN_PC10C_SERCOM6_PAD2                     (74L)        /**< SERCOM6 signal: SERCOM6_PAD2 on PC10 mux C*/
#define MUX_PC10C_SERCOM6_PAD2                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD2 */
#define PORT_PC10C_SERCOM6_PAD2                    (1UL << 10)  /**< SERCOM6 signal: SERCOM6PAD2 */
#define PIN_PC05C_SERCOM6_PAD3                     (69L)        /**< SERCOM6 signal: SERCOM6_PAD3 on PC05 mux C*/
#define MUX_PC05C_SERCOM6_PAD3                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD3 */
#define PORT_PC05C_SERCOM6_PAD3                    (1UL << 5)   /**< SERCOM6 signal: SERCOM6PAD3 */
#define PIN_PC11C_SERCOM6_PAD3                     (75L)        /**< SERCOM6 signal: SERCOM6_PAD3 on PC11 mux C*/
#define MUX_PC11C_SERCOM6_PAD3                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD3 */
#define PORT_PC11C_SERCOM6_PAD3                    (1UL << 11)  /**< SERCOM6 signal: SERCOM6PAD3 */
#define PIN_PC19C_SERCOM6_PAD3                     (83L)        /**< SERCOM6 signal: SERCOM6_PAD3 on PC19 mux C*/
#define MUX_PC19C_SERCOM6_PAD3                     (2L)         /**< SERCOM6 signal line function value: SERCOM6_PAD3 */
#define PORT_PC19C_SERCOM6_PAD3                    (1UL << 19)  /**< SERCOM6 signal: SERCOM6PAD3 */
/* ========== PIO definition for SERCOM7 peripheral ========== */
#define PIN_PC08D_SERCOM7_PAD0                     (72L)        /**< SERCOM7 signal: SERCOM7_PAD0 on PC08 mux D*/
#define MUX_PC08D_SERCOM7_PAD0                     (3L)         /**< SERCOM7 signal line function value: SERCOM7_PAD0 */
#define PORT_PC08D_SERCOM7_PAD0                    (1UL << 8)   /**< SERCOM7 signal: SERCOM7PAD0 */
#define PIN_PC03C_SERCOM7_PAD0                     (67L)        /**< SERCOM7 signal: SERCOM7_PAD0 on PC03 mux C*/
#define MUX_PC03C_SERCOM7_PAD0                     (2L)         /**< SERCOM7 signal line function value: SERCOM7_PAD0 */
#define PORT_PC03C_SERCOM7_PAD0                    (1UL << 3)   /**< SERCOM7 signal: SERCOM7PAD0 */
#define PIN_PC12C_SERCOM7_PAD0                     (76L)        /**< SERCOM7 signal: SERCOM7_PAD0 on PC12 mux C*/
#define MUX_PC12C_SERCOM7_PAD0                     (2L)         /**< SERCOM7 signal line function value: SERCOM7_PAD0 */
#define PORT_PC12C_SERCOM7_PAD0                    (1UL << 12)  /**< SERCOM7 signal: SERCOM7PAD0 */
#define PIN_PC09D_SERCOM7_PAD1                     (73L)        /**< SERCOM7 signal: SERCOM7_PAD1 on PC09 mux D*/
#define MUX_PC09D_SERCOM7_PAD1                     (3L)         /**< SERCOM7 signal line function value: SERCOM7_PAD1 */
#define PORT_PC09D_SERCOM7_PAD1                    (1UL << 9)   /**< SERCOM7 signal: SERCOM7PAD1 */
#define PIN_PB06C_SERCOM7_PAD1                     (38L)        /**< SERCOM7 signal: SERCOM7_PAD1 on PB06 mux C*/
#define MUX_PB06C_SERCOM7_PAD1                     (2L)         /**< SERCOM7 signal line function value: SERCOM7_PAD1 */
#define PORT_PB06C_SERCOM7_PAD1                    (1UL << 6)   /**< SERCOM7 signal: SERCOM7PAD1 */
#define PIN_PC13C_SERCOM7_PAD1                     (77L)        /**< SERCOM7 signal: SERCOM7_PAD1 on PC13 mux C*/
#define MUX_PC13C_SERCOM7_PAD1                     (2L)         /**< SERCOM7 signal line function value: SERCOM7_PAD1 */
#define PORT_PC13C_SERCOM7_PAD1                    (1UL << 13)  /**< SERCOM7 signal: SERCOM7PAD1 */
#define PIN_PB07D_SERCOM7_PAD2                     (39L)        /**< SERCOM7 signal: SERCOM7_PAD2 on PB07 mux D*/
#define MUX_PB07D_SERCOM7_PAD2                     (3L)         /**< SERCOM7 signal line function value: SERCOM7_PAD2 */
#define PORT_PB07D_SERCOM7_PAD2                    (1UL << 7)   /**< SERCOM7 signal: SERCOM7PAD2 */
#define PIN_PC10D_SERCOM7_PAD2                     (74L)        /**< SERCOM7 signal: SERCOM7_PAD2 on PC10 mux D*/
#define MUX_PC10D_SERCOM7_PAD2                     (3L)         /**< SERCOM7 signal line function value: SERCOM7_PAD2 */
#define PORT_PC10D_SERCOM7_PAD2                    (1UL << 10)  /**< SERCOM7 signal: SERCOM7PAD2 */
#define PIN_PB08C_SERCOM7_PAD2                     (40L)        /**< SERCOM7 signal: SERCOM7_PAD2 on PB08 mux C*/
#define MUX_PB08C_SERCOM7_PAD2                     (2L)         /**< SERCOM7 signal line function value: SERCOM7_PAD2 */
#define PORT_PB08C_SERCOM7_PAD2                    (1UL << 8)   /**< SERCOM7 signal: SERCOM7PAD2 */
#define PIN_PC14C_SERCOM7_PAD2                     (78L)        /**< SERCOM7 signal: SERCOM7_PAD2 on PC14 mux C*/
#define MUX_PC14C_SERCOM7_PAD2                     (2L)         /**< SERCOM7 signal line function value: SERCOM7_PAD2 */
#define PORT_PC14C_SERCOM7_PAD2                    (1UL << 14)  /**< SERCOM7 signal: SERCOM7PAD2 */
#define PIN_PB08D_SERCOM7_PAD3                     (40L)        /**< SERCOM7 signal: SERCOM7_PAD3 on PB08 mux D*/
#define MUX_PB08D_SERCOM7_PAD3                     (3L)         /**< SERCOM7 signal line function value: SERCOM7_PAD3 */
#define PORT_PB08D_SERCOM7_PAD3                    (1UL << 8)   /**< SERCOM7 signal: SERCOM7PAD3 */
#define PIN_PC11D_SERCOM7_PAD3                     (75L)        /**< SERCOM7 signal: SERCOM7_PAD3 on PC11 mux D*/
#define MUX_PC11D_SERCOM7_PAD3                     (3L)         /**< SERCOM7 signal line function value: SERCOM7_PAD3 */
#define PORT_PC11D_SERCOM7_PAD3                    (1UL << 11)  /**< SERCOM7 signal: SERCOM7PAD3 */
#define PIN_PB07C_SERCOM7_PAD3                     (39L)        /**< SERCOM7 signal: SERCOM7_PAD3 on PB07 mux C*/
#define MUX_PB07C_SERCOM7_PAD3                     (2L)         /**< SERCOM7 signal line function value: SERCOM7_PAD3 */
#define PORT_PB07C_SERCOM7_PAD3                    (1UL << 7)   /**< SERCOM7 signal: SERCOM7PAD3 */
#define PIN_PC15C_SERCOM7_PAD3                     (79L)        /**< SERCOM7 signal: SERCOM7_PAD3 on PC15 mux C*/
#define MUX_PC15C_SERCOM7_PAD3                     (2L)         /**< SERCOM7 signal line function value: SERCOM7_PAD3 */
#define PORT_PC15C_SERCOM7_PAD3                    (1UL << 15)  /**< SERCOM7 signal: SERCOM7PAD3 */
/* ========== PIO definition for TC0 peripheral ========== */
#define PIN_PA08E_TC0_WO0                          (8L)         /**< TC0 signal: TC0_WO0 on PA08 mux E*/
#define MUX_PA08E_TC0_WO0                          (4L)         /**< TC0 signal line function value: TC0_WO0 */
#define PORT_PA08E_TC0_WO0                         (1UL << 8)   /**< TC0 signal: TC0WO0 */
#define PIN_PA04E_TC0_WO0                          (4L)         /**< TC0 signal: TC0_WO0 on PA04 mux E*/
#define MUX_PA04E_TC0_WO0                          (4L)         /**< TC0 signal line function value: TC0_WO0 */
#define PORT_PA04E_TC0_WO0                         (1UL << 4)   /**< TC0 signal: TC0WO0 */
#define PIN_PB30E_TC0_WO0                          (62L)        /**< TC0 signal: TC0_WO0 on PB30 mux E*/
#define MUX_PB30E_TC0_WO0                          (4L)         /**< TC0 signal line function value: TC0_WO0 */
#define PORT_PB30E_TC0_WO0                         (1UL << 30)  /**< TC0 signal: TC0WO0 */
#define PIN_PA09E_TC0_WO1                          (9L)         /**< TC0 signal: TC0_WO1 on PA09 mux E*/
#define MUX_PA09E_TC0_WO1                          (4L)         /**< TC0 signal line function value: TC0_WO1 */
#define PORT_PA09E_TC0_WO1                         (1UL << 9)   /**< TC0 signal: TC0WO1 */
#define PIN_PA05E_TC0_WO1                          (5L)         /**< TC0 signal: TC0_WO1 on PA05 mux E*/
#define MUX_PA05E_TC0_WO1                          (4L)         /**< TC0 signal line function value: TC0_WO1 */
#define PORT_PA05E_TC0_WO1                         (1UL << 5)   /**< TC0 signal: TC0WO1 */
#define PIN_PB31E_TC0_WO1                          (63L)        /**< TC0 signal: TC0_WO1 on PB31 mux E*/
#define MUX_PB31E_TC0_WO1                          (4L)         /**< TC0 signal line function value: TC0_WO1 */
#define PORT_PB31E_TC0_WO1                         (1UL << 31)  /**< TC0 signal: TC0WO1 */
/* ========== PIO definition for TC1 peripheral ========== */
#define PIN_PA10E_TC1_WO0                          (10L)        /**< TC1 signal: TC1_WO0 on PA10 mux E*/
#define MUX_PA10E_TC1_WO0                          (4L)         /**< TC1 signal line function value: TC1_WO0 */
#define PORT_PA10E_TC1_WO0                         (1UL << 10)  /**< TC1 signal: TC1WO0 */
#define PIN_PA06E_TC1_WO0                          (6L)         /**< TC1 signal: TC1_WO0 on PA06 mux E*/
#define MUX_PA06E_TC1_WO0                          (4L)         /**< TC1 signal line function value: TC1_WO0 */
#define PORT_PA06E_TC1_WO0                         (1UL << 6)   /**< TC1 signal: TC1WO0 */
#define PIN_PA30E_TC1_WO0                          (30L)        /**< TC1 signal: TC1_WO0 on PA30 mux E*/
#define MUX_PA30E_TC1_WO0                          (4L)         /**< TC1 signal line function value: TC1_WO0 */
#define PORT_PA30E_TC1_WO0                         (1UL << 30)  /**< TC1 signal: TC1WO0 */
#define PIN_PA11E_TC1_WO1                          (11L)        /**< TC1 signal: TC1_WO1 on PA11 mux E*/
#define MUX_PA11E_TC1_WO1                          (4L)         /**< TC1 signal line function value: TC1_WO1 */
#define PORT_PA11E_TC1_WO1                         (1UL << 11)  /**< TC1 signal: TC1WO1 */
#define PIN_PA07E_TC1_WO1                          (7L)         /**< TC1 signal: TC1_WO1 on PA07 mux E*/
#define MUX_PA07E_TC1_WO1                          (4L)         /**< TC1 signal line function value: TC1_WO1 */
#define PORT_PA07E_TC1_WO1                         (1UL << 7)   /**< TC1 signal: TC1WO1 */
#define PIN_PA31E_TC1_WO1                          (31L)        /**< TC1 signal: TC1_WO1 on PA31 mux E*/
#define MUX_PA31E_TC1_WO1                          (4L)         /**< TC1 signal line function value: TC1_WO1 */
#define PORT_PA31E_TC1_WO1                         (1UL << 31)  /**< TC1 signal: TC1WO1 */
/* ========== PIO definition for TC2 peripheral ========== */
#define PIN_PA12E_TC2_WO0                          (12L)        /**< TC2 signal: TC2_WO0 on PA12 mux E*/
#define MUX_PA12E_TC2_WO0                          (4L)         /**< TC2 signal line function value: TC2_WO0 */
#define PORT_PA12E_TC2_WO0                         (1UL << 12)  /**< TC2 signal: TC2WO0 */
#define PIN_PA16E_TC2_WO0                          (16L)        /**< TC2 signal: TC2_WO0 on PA16 mux E*/
#define MUX_PA16E_TC2_WO0                          (4L)         /**< TC2 signal line function value: TC2_WO0 */
#define PORT_PA16E_TC2_WO0                         (1UL << 16)  /**< TC2 signal: TC2WO0 */
#define PIN_PA00E_TC2_WO0                          (0L)         /**< TC2 signal: TC2_WO0 on PA00 mux E*/
#define MUX_PA00E_TC2_WO0                          (4L)         /**< TC2 signal line function value: TC2_WO0 */
#define PORT_PA00E_TC2_WO0                         (1UL << 0)   /**< TC2 signal: TC2WO0 */
#define PIN_PA01E_TC2_WO1                          (1L)         /**< TC2 signal: TC2_WO1 on PA01 mux E*/
#define MUX_PA01E_TC2_WO1                          (4L)         /**< TC2 signal line function value: TC2_WO1 */
#define PORT_PA01E_TC2_WO1                         (1UL << 1)   /**< TC2 signal: TC2WO1 */
#define PIN_PA13E_TC2_WO1                          (13L)        /**< TC2 signal: TC2_WO1 on PA13 mux E*/
#define MUX_PA13E_TC2_WO1                          (4L)         /**< TC2 signal line function value: TC2_WO1 */
#define PORT_PA13E_TC2_WO1                         (1UL << 13)  /**< TC2 signal: TC2WO1 */
#define PIN_PA17E_TC2_WO1                          (17L)        /**< TC2 signal: TC2_WO1 on PA17 mux E*/
#define MUX_PA17E_TC2_WO1                          (4L)         /**< TC2 signal line function value: TC2_WO1 */
#define PORT_PA17E_TC2_WO1                         (1UL << 17)  /**< TC2 signal: TC2WO1 */
/* ========== PIO definition for TC3 peripheral ========== */
#define PIN_PA18E_TC3_WO0                          (18L)        /**< TC3 signal: TC3_WO0 on PA18 mux E*/
#define MUX_PA18E_TC3_WO0                          (4L)         /**< TC3 signal line function value: TC3_WO0 */
#define PORT_PA18E_TC3_WO0                         (1UL << 18)  /**< TC3 signal: TC3WO0 */
#define PIN_PA14E_TC3_WO0                          (14L)        /**< TC3 signal: TC3_WO0 on PA14 mux E*/
#define MUX_PA14E_TC3_WO0                          (4L)         /**< TC3 signal line function value: TC3_WO0 */
#define PORT_PA14E_TC3_WO0                         (1UL << 14)  /**< TC3 signal: TC3WO0 */
#define PIN_PA15E_TC3_WO1                          (15L)        /**< TC3 signal: TC3_WO1 on PA15 mux E*/
#define MUX_PA15E_TC3_WO1                          (4L)         /**< TC3 signal line function value: TC3_WO1 */
#define PORT_PA15E_TC3_WO1                         (1UL << 15)  /**< TC3 signal: TC3WO1 */
#define PIN_PA19E_TC3_WO1                          (19L)        /**< TC3 signal: TC3_WO1 on PA19 mux E*/
#define MUX_PA19E_TC3_WO1                          (4L)         /**< TC3 signal line function value: TC3_WO1 */
#define PORT_PA19E_TC3_WO1                         (1UL << 19)  /**< TC3 signal: TC3WO1 */
/* ========== PIO definition for TC4 peripheral ========== */
#define PIN_PB12E_TC4_WO0                          (44L)        /**< TC4 signal: TC4_WO0 on PB12 mux E*/
#define MUX_PB12E_TC4_WO0                          (4L)         /**< TC4 signal line function value: TC4_WO0 */
#define PORT_PB12E_TC4_WO0                         (1UL << 12)  /**< TC4 signal: TC4WO0 */
#define PIN_PA22E_TC4_WO0                          (22L)        /**< TC4 signal: TC4_WO0 on PA22 mux E*/
#define MUX_PA22E_TC4_WO0                          (4L)         /**< TC4 signal line function value: TC4_WO0 */
#define PORT_PA22E_TC4_WO0                         (1UL << 22)  /**< TC4 signal: TC4WO0 */
#define PIN_PB08E_TC4_WO0                          (40L)        /**< TC4 signal: TC4_WO0 on PB08 mux E*/
#define MUX_PB08E_TC4_WO0                          (4L)         /**< TC4 signal line function value: TC4_WO0 */
#define PORT_PB08E_TC4_WO0                         (1UL << 8)   /**< TC4 signal: TC4WO0 */
#define PIN_PB09E_TC4_WO1                          (41L)        /**< TC4 signal: TC4_WO1 on PB09 mux E*/
#define MUX_PB09E_TC4_WO1                          (4L)         /**< TC4 signal line function value: TC4_WO1 */
#define PORT_PB09E_TC4_WO1                         (1UL << 9)   /**< TC4 signal: TC4WO1 */
#define PIN_PA23E_TC4_WO1                          (23L)        /**< TC4 signal: TC4_WO1 on PA23 mux E*/
#define MUX_PA23E_TC4_WO1                          (4L)         /**< TC4 signal line function value: TC4_WO1 */
#define PORT_PA23E_TC4_WO1                         (1UL << 23)  /**< TC4 signal: TC4WO1 */
#define PIN_PB13E_TC4_WO1                          (45L)        /**< TC4 signal: TC4_WO1 on PB13 mux E*/
#define MUX_PB13E_TC4_WO1                          (4L)         /**< TC4 signal line function value: TC4_WO1 */
#define PORT_PB13E_TC4_WO1                         (1UL << 13)  /**< TC4 signal: TC4WO1 */
/* ========== PIO definition for TC5 peripheral ========== */
#define PIN_PB14E_TC5_WO0                          (46L)        /**< TC5 signal: TC5_WO0 on PB14 mux E*/
#define MUX_PB14E_TC5_WO0                          (4L)         /**< TC5 signal line function value: TC5_WO0 */
#define PORT_PB14E_TC5_WO0                         (1UL << 14)  /**< TC5 signal: TC5WO0 */
#define PIN_PA24E_TC5_WO0                          (24L)        /**< TC5 signal: TC5_WO0 on PA24 mux E*/
#define MUX_PA24E_TC5_WO0                          (4L)         /**< TC5 signal line function value: TC5_WO0 */
#define PORT_PA24E_TC5_WO0                         (1UL << 24)  /**< TC5 signal: TC5WO0 */
#define PIN_PB10E_TC5_WO0                          (42L)        /**< TC5 signal: TC5_WO0 on PB10 mux E*/
#define MUX_PB10E_TC5_WO0                          (4L)         /**< TC5 signal line function value: TC5_WO0 */
#define PORT_PB10E_TC5_WO0                         (1UL << 10)  /**< TC5 signal: TC5WO0 */
#define PIN_PA25E_TC5_WO1                          (25L)        /**< TC5 signal: TC5_WO1 on PA25 mux E*/
#define MUX_PA25E_TC5_WO1                          (4L)         /**< TC5 signal line function value: TC5_WO1 */
#define PORT_PA25E_TC5_WO1                         (1UL << 25)  /**< TC5 signal: TC5WO1 */
#define PIN_PB11E_TC5_WO1                          (43L)        /**< TC5 signal: TC5_WO1 on PB11 mux E*/
#define MUX_PB11E_TC5_WO1                          (4L)         /**< TC5 signal line function value: TC5_WO1 */
#define PORT_PB11E_TC5_WO1                         (1UL << 11)  /**< TC5 signal: TC5WO1 */
#define PIN_PB15E_TC5_WO1                          (47L)        /**< TC5 signal: TC5_WO1 on PB15 mux E*/
#define MUX_PB15E_TC5_WO1                          (4L)         /**< TC5 signal line function value: TC5_WO1 */
#define PORT_PB15E_TC5_WO1                         (1UL << 15)  /**< TC5 signal: TC5WO1 */
/* ========== PIO definition for TC6 peripheral ========== */
#define PIN_PB16E_TC6_WO0                          (48L)        /**< TC6 signal: TC6_WO0 on PB16 mux E*/
#define MUX_PB16E_TC6_WO0                          (4L)         /**< TC6 signal line function value: TC6_WO0 */
#define PORT_PB16E_TC6_WO0                         (1UL << 16)  /**< TC6 signal: TC6WO0 */
#define PIN_PB02E_TC6_WO0                          (34L)        /**< TC6 signal: TC6_WO0 on PB02 mux E*/
#define MUX_PB02E_TC6_WO0                          (4L)         /**< TC6 signal line function value: TC6_WO0 */
#define PORT_PB02E_TC6_WO0                         (1UL << 2)   /**< TC6 signal: TC6WO0 */
#define PIN_PB17E_TC6_WO1                          (49L)        /**< TC6 signal: TC6_WO1 on PB17 mux E*/
#define MUX_PB17E_TC6_WO1                          (4L)         /**< TC6 signal line function value: TC6_WO1 */
#define PORT_PB17E_TC6_WO1                         (1UL << 17)  /**< TC6 signal: TC6WO1 */
#define PIN_PB03E_TC6_WO1                          (35L)        /**< TC6 signal: TC6_WO1 on PB03 mux E*/
#define MUX_PB03E_TC6_WO1                          (4L)         /**< TC6 signal line function value: TC6_WO1 */
#define PORT_PB03E_TC6_WO1                         (1UL << 3)   /**< TC6 signal: TC6WO1 */
/* ========== PIO definition for TC7 peripheral ========== */
#define PIN_PB22E_TC7_WO0                          (54L)        /**< TC7 signal: TC7_WO0 on PB22 mux E*/
#define MUX_PB22E_TC7_WO0                          (4L)         /**< TC7 signal line function value: TC7_WO0 */
#define PORT_PB22E_TC7_WO0                         (1UL << 22)  /**< TC7 signal: TC7WO0 */
#define PIN_PA20E_TC7_WO0                          (20L)        /**< TC7 signal: TC7_WO0 on PA20 mux E*/
#define MUX_PA20E_TC7_WO0                          (4L)         /**< TC7 signal line function value: TC7_WO0 */
#define PORT_PA20E_TC7_WO0                         (1UL << 20)  /**< TC7 signal: TC7WO0 */
#define PIN_PB00E_TC7_WO0                          (32L)        /**< TC7 signal: TC7_WO0 on PB00 mux E*/
#define MUX_PB00E_TC7_WO0                          (4L)         /**< TC7 signal line function value: TC7_WO0 */
#define PORT_PB00E_TC7_WO0                         (1UL << 0)   /**< TC7 signal: TC7WO0 */
#define PIN_PB01E_TC7_WO1                          (33L)        /**< TC7 signal: TC7_WO1 on PB01 mux E*/
#define MUX_PB01E_TC7_WO1                          (4L)         /**< TC7 signal line function value: TC7_WO1 */
#define PORT_PB01E_TC7_WO1                         (1UL << 1)   /**< TC7 signal: TC7WO1 */
#define PIN_PA21E_TC7_WO1                          (21L)        /**< TC7 signal: TC7_WO1 on PA21 mux E*/
#define MUX_PA21E_TC7_WO1                          (4L)         /**< TC7 signal line function value: TC7_WO1 */
#define PORT_PA21E_TC7_WO1                         (1UL << 21)  /**< TC7 signal: TC7WO1 */
#define PIN_PB23E_TC7_WO1                          (55L)        /**< TC7 signal: TC7_WO1 on PB23 mux E*/
#define MUX_PB23E_TC7_WO1                          (4L)         /**< TC7 signal line function value: TC7_WO1 */
#define PORT_PB23E_TC7_WO1                         (1UL << 23)  /**< TC7 signal: TC7WO1 */
/* ========== PIO definition for TCC0 peripheral ========== */
#define PIN_PA08F_TCC0_WO0                         (8L)         /**< TCC0 signal: TCC0_WO0 on PA08 mux F*/
#define MUX_PA08F_TCC0_WO0                         (5L)         /**< TCC0 signal line function value: TCC0_WO0 */
#define PORT_PA08F_TCC0_WO0                        (1UL << 8)   /**< TCC0 signal: TCC0WO0 */
#define PIN_PA09F_TCC0_WO1                         (9L)         /**< TCC0 signal: TCC0_WO1 on PA09 mux F*/
#define MUX_PA09F_TCC0_WO1                         (5L)         /**< TCC0 signal line function value: TCC0_WO1 */
#define PORT_PA09F_TCC0_WO1                        (1UL << 9)   /**< TCC0 signal: TCC0WO1 */
#define PIN_PA10F_TCC0_WO2                         (10L)        /**< TCC0 signal: TCC0_WO2 on PA10 mux F*/
#define MUX_PA10F_TCC0_WO2                         (5L)         /**< TCC0 signal line function value: TCC0_WO2 */
#define PORT_PA10F_TCC0_WO2                        (1UL << 10)  /**< TCC0 signal: TCC0WO2 */
#define PIN_PA11F_TCC0_WO3                         (11L)        /**< TCC0 signal: TCC0_WO3 on PA11 mux F*/
#define MUX_PA11F_TCC0_WO3                         (5L)         /**< TCC0 signal line function value: TCC0_WO3 */
#define PORT_PA11F_TCC0_WO3                        (1UL << 11)  /**< TCC0 signal: TCC0WO3 */
#define PIN_PB10F_TCC0_WO4                         (42L)        /**< TCC0 signal: TCC0_WO4 on PB10 mux F*/
#define MUX_PB10F_TCC0_WO4                         (5L)         /**< TCC0 signal line function value: TCC0_WO4 */
#define PORT_PB10F_TCC0_WO4                        (1UL << 10)  /**< TCC0 signal: TCC0WO4 */
#define PIN_PB11F_TCC0_WO5                         (43L)        /**< TCC0 signal: TCC0_WO5 on PB11 mux F*/
#define MUX_PB11F_TCC0_WO5                         (5L)         /**< TCC0 signal line function value: TCC0_WO5 */
#define PORT_PB11F_TCC0_WO5                        (1UL << 11)  /**< TCC0 signal: TCC0WO5 */
#define PIN_PA12F_TCC0_WO6                         (12L)        /**< TCC0 signal: TCC0_WO6 on PA12 mux F*/
#define MUX_PA12F_TCC0_WO6                         (5L)         /**< TCC0 signal line function value: TCC0_WO6 */
#define PORT_PA12F_TCC0_WO6                        (1UL << 12)  /**< TCC0 signal: TCC0WO6 */
#define PIN_PB12F_TCC0_WO6                         (44L)        /**< TCC0 signal: TCC0_WO6 on PB12 mux F*/
#define MUX_PB12F_TCC0_WO6                         (5L)         /**< TCC0 signal line function value: TCC0_WO6 */
#define PORT_PB12F_TCC0_WO6                        (1UL << 12)  /**< TCC0 signal: TCC0WO6 */
#define PIN_PA13F_TCC0_WO7                         (13L)        /**< TCC0 signal: TCC0_WO7 on PA13 mux F*/
#define MUX_PA13F_TCC0_WO7                         (5L)         /**< TCC0 signal line function value: TCC0_WO7 */
#define PORT_PA13F_TCC0_WO7                        (1UL << 13)  /**< TCC0 signal: TCC0WO7 */
#define PIN_PB13F_TCC0_WO7                         (45L)        /**< TCC0 signal: TCC0_WO7 on PB13 mux F*/
#define MUX_PB13F_TCC0_WO7                         (5L)         /**< TCC0 signal line function value: TCC0_WO7 */
#define PORT_PB13F_TCC0_WO7                        (1UL << 13)  /**< TCC0 signal: TCC0WO7 */
/* ========== PIO definition for TCC1 peripheral ========== */
#define PIN_PA16F_TCC1_WO0                         (16L)        /**< TCC1 signal: TCC1_WO0 on PA16 mux F*/
#define MUX_PA16F_TCC1_WO0                         (5L)         /**< TCC1 signal line function value: TCC1_WO0 */
#define PORT_PA16F_TCC1_WO0                        (1UL << 16)  /**< TCC1 signal: TCC1WO0 */
#define PIN_PA22F_TCC1_WO0                         (22L)        /**< TCC1 signal: TCC1_WO0 on PA22 mux F*/
#define MUX_PA22F_TCC1_WO0                         (5L)         /**< TCC1 signal line function value: TCC1_WO0 */
#define PORT_PA22F_TCC1_WO0                        (1UL << 22)  /**< TCC1 signal: TCC1WO0 */
#define PIN_PA17F_TCC1_WO1                         (17L)        /**< TCC1 signal: TCC1_WO1 on PA17 mux F*/
#define MUX_PA17F_TCC1_WO1                         (5L)         /**< TCC1 signal line function value: TCC1_WO1 */
#define PORT_PA17F_TCC1_WO1                        (1UL << 17)  /**< TCC1 signal: TCC1WO1 */
#define PIN_PA23F_TCC1_WO1                         (23L)        /**< TCC1 signal: TCC1_WO1 on PA23 mux F*/
#define MUX_PA23F_TCC1_WO1                         (5L)         /**< TCC1 signal line function value: TCC1_WO1 */
#define PORT_PA23F_TCC1_WO1                        (1UL << 23)  /**< TCC1 signal: TCC1WO1 */
#define PIN_PA18F_TCC1_WO2                         (18L)        /**< TCC1 signal: TCC1_WO2 on PA18 mux F*/
#define MUX_PA18F_TCC1_WO2                         (5L)         /**< TCC1 signal line function value: TCC1_WO2 */
#define PORT_PA18F_TCC1_WO2                        (1UL << 18)  /**< TCC1 signal: TCC1WO2 */
#define PIN_PB22F_TCC1_WO2                         (54L)        /**< TCC1 signal: TCC1_WO2 on PB22 mux F*/
#define MUX_PB22F_TCC1_WO2                         (5L)         /**< TCC1 signal line function value: TCC1_WO2 */
#define PORT_PB22F_TCC1_WO2                        (1UL << 22)  /**< TCC1 signal: TCC1WO2 */
#define PIN_PA19F_TCC1_WO3                         (19L)        /**< TCC1 signal: TCC1_WO3 on PA19 mux F*/
#define MUX_PA19F_TCC1_WO3                         (5L)         /**< TCC1 signal line function value: TCC1_WO3 */
#define PORT_PA19F_TCC1_WO3                        (1UL << 19)  /**< TCC1 signal: TCC1WO3 */
#define PIN_PB23F_TCC1_WO3                         (55L)        /**< TCC1 signal: TCC1_WO3 on PB23 mux F*/
#define MUX_PB23F_TCC1_WO3                         (5L)         /**< TCC1 signal line function value: TCC1_WO3 */
#define PORT_PB23F_TCC1_WO3                        (1UL << 23)  /**< TCC1 signal: TCC1WO3 */
/* ========== PIO definition for TCC2 peripheral ========== */
#define PIN_PC03F_TCC2_WO0                         (67L)        /**< TCC2 signal: TCC2_WO0 on PC03 mux F*/
#define MUX_PC03F_TCC2_WO0                         (5L)         /**< TCC2 signal line function value: TCC2_WO0 */
#define PORT_PC03F_TCC2_WO0                        (1UL << 3)   /**< TCC2 signal: TCC2WO0 */
#define PIN_PA20F_TCC2_WO0                         (20L)        /**< TCC2 signal: TCC2_WO0 on PA20 mux F*/
#define MUX_PA20F_TCC2_WO0                         (5L)         /**< TCC2 signal line function value: TCC2_WO0 */
#define PORT_PA20F_TCC2_WO0                        (1UL << 20)  /**< TCC2 signal: TCC2WO0 */
#define PIN_PA24F_TCC2_WO0                         (24L)        /**< TCC2 signal: TCC2_WO0 on PA24 mux F*/
#define MUX_PA24F_TCC2_WO0                         (5L)         /**< TCC2 signal line function value: TCC2_WO0 */
#define PORT_PA24F_TCC2_WO0                        (1UL << 24)  /**< TCC2 signal: TCC2WO0 */
#define PIN_PA25F_TCC2_WO1                         (25L)        /**< TCC2 signal: TCC2_WO1 on PA25 mux F*/
#define MUX_PA25F_TCC2_WO1                         (5L)         /**< TCC2 signal line function value: TCC2_WO1 */
#define PORT_PA25F_TCC2_WO1                        (1UL << 25)  /**< TCC2 signal: TCC2WO1 */
#define PIN_PA21F_TCC2_WO1                         (21L)        /**< TCC2 signal: TCC2_WO1 on PA21 mux F*/
#define MUX_PA21F_TCC2_WO1                         (5L)         /**< TCC2 signal line function value: TCC2_WO1 */
#define PORT_PA21F_TCC2_WO1                        (1UL << 21)  /**< TCC2 signal: TCC2WO1 */
#define PIN_PC05F_TCC2_WO1                         (69L)        /**< TCC2 signal: TCC2_WO1 on PC05 mux F*/
#define MUX_PC05F_TCC2_WO1                         (5L)         /**< TCC2 signal line function value: TCC2_WO1 */
#define PORT_PC05F_TCC2_WO1                        (1UL << 5)   /**< TCC2 signal: TCC2WO1 */

#endif /* SAMC21N18A_GPIO_H */

