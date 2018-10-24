/**
 * \brief Header file for SAMC21N18A
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
#ifndef SAMC21N18A_H
#define SAMC21N18A_H

// Header version uses Semantic Versioning 2.0.0 (https://semver.org/)
#define HEADER_FORMAT_VERSION "2.0.0"

#define HEADER_FORMAT_VERSION_MAJOR (2)
#define HEADER_FORMAT_VERSION_MINOR (0)

/** \addtogroup SAMC21N18A_definitions SAMC21N18A definitions
  This file defines all structures and symbols for SAMC21N18A:
    - registers and bitfields
    - peripheral base address
    - peripheral ID
    - PIO definitions
 *  @{
 */

#ifdef __cplusplus
 extern "C" {
#endif

#include <stdint.h>

/** \addtogroup SAMC21N18A_cmsis CMSIS Definitions
 *  @{
 */

/* ************************************************************************** */
/*   CMSIS DEFINITIONS FOR SAMC21N18A                                         */
/* ************************************************************************** */
/** Interrupt Number Definition */
typedef enum IRQn
{
/******  CORTEX-0PLUS Processor Exceptions Numbers ******************************/
  Reset_IRQn                = -15, /**< -15 Reset Vector, invoked on Power up and warm reset */
  NonMaskableInt_IRQn       = -14, /**< -14 Non maskable Interrupt, cannot be stopped or preempted */
  HardFault_IRQn            = -13, /**< -13 Hard Fault, all classes of Fault    */
  SVCall_IRQn               =  -5, /**< -5  System Service Call via SVC instruction */
  PendSV_IRQn               =  -2, /**< -2  Pendable request for system service */
  SysTick_IRQn              =  -1, /**< -1  System Tick Timer                   */
/******  SAMC21N18A specific Interrupt Numbers ***********************************/
  MCLK_IRQn                 = 0  , /**< 0   Main Clock (MCLK)                   */
  OSCCTRL_IRQn              = 0  , /**< 0   Oscillators Control (OSCCTRL)       */
  OSC32KCTRL_IRQn           = 0  , /**< 0   32k Oscillators Control (OSC32KCTRL) */
  PAC_IRQn                  = 0  , /**< 0   Peripheral Access Controller (PAC)  */
  PM_IRQn                   = 0  , /**< 0   Power Manager (PM)                  */
  SUPC_IRQn                 = 0  , /**< 0   Supply Controller (SUPC)            */
  WDT_IRQn                  = 1  , /**< 1   Watchdog Timer (WDT)                */
  RTC_IRQn                  = 2  , /**< 2   Real-Time Counter (RTC)             */
  EIC_IRQn                  = 3  , /**< 3   External Interrupt Controller (EIC) */
  FREQM_IRQn                = 4  , /**< 4   Frequency Meter (FREQM)             */
  TSENS_IRQn                = 5  , /**< 5   Temperature Sensor (TSENS)          */
  NVMCTRL_IRQn              = 6  , /**< 6   Non-Volatile Memory Controller (NVMCTRL) */
  DMAC_IRQn                 = 7  , /**< 7   Direct Memory Access Controller (DMAC) */
  EVSYS_IRQn                = 8  , /**< 8   Event System Interface (EVSYS)      */
  SERCOM0_IRQn              = 9  , /**< 9   Serial Communication Interface (SERCOM0) */
  SERCOM6_IRQn              = 9  , /**< 9   Serial Communication Interface (SERCOM6) */
  SERCOM1_IRQn              = 10 , /**< 10  Serial Communication Interface (SERCOM1) */
  SERCOM7_IRQn              = 10 , /**< 10  Serial Communication Interface (SERCOM7) */
  SERCOM2_IRQn              = 11 , /**< 11  Serial Communication Interface (SERCOM2) */
  SERCOM3_IRQn              = 12 , /**< 12  Serial Communication Interface (SERCOM3) */
  SERCOM4_IRQn              = 13 , /**< 13  Serial Communication Interface (SERCOM4) */
  SERCOM5_IRQn              = 14 , /**< 14  Serial Communication Interface (SERCOM5) */
  CAN0_IRQn                 = 15 , /**< 15  Control Area Network (CAN0)         */
  CAN1_IRQn                 = 16 , /**< 16  Control Area Network (CAN1)         */
  TCC0_IRQn                 = 17 , /**< 17  Timer Counter Control (TCC0)        */
  TCC1_IRQn                 = 18 , /**< 18  Timer Counter Control (TCC1)        */
  TCC2_IRQn                 = 19 , /**< 19  Timer Counter Control (TCC2)        */
  TC0_IRQn                  = 20 , /**< 20  Basic Timer Counter (TC0)           */
  TC5_IRQn                  = 20 , /**< 20  Basic Timer Counter (TC5)           */
  TC1_IRQn                  = 21 , /**< 21  Basic Timer Counter (TC1)           */
  TC6_IRQn                  = 21 , /**< 21  Basic Timer Counter (TC6)           */
  TC2_IRQn                  = 22 , /**< 22  Basic Timer Counter (TC2)           */
  TC7_IRQn                  = 22 , /**< 22  Basic Timer Counter (TC7)           */
  TC3_IRQn                  = 23 , /**< 23  Basic Timer Counter (TC3)           */
  TC4_IRQn                  = 24 , /**< 24  Basic Timer Counter (TC4)           */
  ADC0_IRQn                 = 25 , /**< 25  Analog Digital Converter (ADC0)     */
  ADC1_IRQn                 = 26 , /**< 26  Analog Digital Converter (ADC1)     */
  AC_IRQn                   = 27 , /**< 27  Analog Comparators (AC)             */
  DAC_IRQn                  = 28 , /**< 28  Digital Analog Converter (DAC)      */
  SDADC_IRQn                = 29 , /**< 29  Sigma-Delta Analog Digital Converter (SDADC) */
  PTC_IRQn                  = 30 , /**< 30  Peripheral Touch Controller (PTC)   */

  PERIPH_MAX_IRQn           = 30   /**< Number of peripheral IDs */
} IRQn_Type;

typedef struct _DeviceVectors
{
  /* Stack pointer */
  void* pvStack;
  /* Cortex-M handlers */
  void* pfnReset_Handler;                        /* -15 Reset Vector, invoked on Power up and warm reset */
  void* pfnNonMaskableInt_Handler;               /* -14 Non maskable Interrupt, cannot be stopped or preempted */
  void* pfnHardFault_Handler;                    /* -13 Hard Fault, all classes of Fault */
  void* pvReservedC12;
  void* pvReservedC11;
  void* pvReservedC10;
  void* pvReservedC9;
  void* pvReservedC8;
  void* pvReservedC7;
  void* pvReservedC6;
  void* pfnSVCall_Handler;                       /*  -5 System Service Call via SVC instruction */
  void* pvReservedC4;
  void* pvReservedC3;
  void* pfnPendSV_Handler;                       /*  -2 Pendable request for system service */
  void* pfnSysTick_Handler;                      /*  -1 System Tick Timer */

  /* Peripheral handlers */
  void* pfnSYSTEM_Handler;                       /*   0 Main Clock (MCLK OSCCTRL OSC32KCTRL PAC PM SUPC) */
  void* pfnWDT_Handler;                          /*   1 Watchdog Timer (WDT) */
  void* pfnRTC_Handler;                          /*   2 Real-Time Counter (RTC) */
  void* pfnEIC_Handler;                          /*   3 External Interrupt Controller (EIC) */
  void* pfnFREQM_Handler;                        /*   4 Frequency Meter (FREQM) */
  void* pfnTSENS_Handler;                        /*   5 Temperature Sensor (TSENS) */
  void* pfnNVMCTRL_Handler;                      /*   6 Non-Volatile Memory Controller (NVMCTRL) */
  void* pfnDMAC_Handler;                         /*   7 Direct Memory Access Controller (DMAC) */
  void* pfnEVSYS_Handler;                        /*   8 Event System Interface (EVSYS) */
  void* pfnSERCOM0_6_Handler;                    /*   9 Serial Communication Interface (SERCOM0 SERCOM6) */
  void* pfnSERCOM1_7_Handler;                    /*  10 Serial Communication Interface (SERCOM1 SERCOM7) */
  void* pfnSERCOM2_Handler;                      /*  11 Serial Communication Interface (SERCOM2) */
  void* pfnSERCOM3_Handler;                      /*  12 Serial Communication Interface (SERCOM3) */
  void* pfnSERCOM4_Handler;                      /*  13 Serial Communication Interface (SERCOM4) */
  void* pfnSERCOM5_Handler;                      /*  14 Serial Communication Interface (SERCOM5) */
  void* pfnCAN0_Handler;                         /*  15 Control Area Network (CAN0) */
  void* pfnCAN1_Handler;                         /*  16 Control Area Network (CAN1) */
  void* pfnTCC0_Handler;                         /*  17 Timer Counter Control (TCC0) */
  void* pfnTCC1_Handler;                         /*  18 Timer Counter Control (TCC1) */
  void* pfnTCC2_Handler;                         /*  19 Timer Counter Control (TCC2) */
  void* pfnTC0_5_Handler;                        /*  20 Basic Timer Counter (TC0 TC5) */
  void* pfnTC1_6_Handler;                        /*  21 Basic Timer Counter (TC1 TC6) */
  void* pfnTC2_7_Handler;                        /*  22 Basic Timer Counter (TC2 TC7) */
  void* pfnTC3_Handler;                          /*  23 Basic Timer Counter (TC3) */
  void* pfnTC4_Handler;                          /*  24 Basic Timer Counter (TC4) */
  void* pfnADC0_Handler;                         /*  25 Analog Digital Converter (ADC0) */
  void* pfnADC1_Handler;                         /*  26 Analog Digital Converter (ADC1) */
  void* pfnAC_Handler;                           /*  27 Analog Comparators (AC) */
  void* pfnDAC_Handler;                          /*  28 Digital Analog Converter (DAC) */
  void* pfnSDADC_Handler;                        /*  29 Sigma-Delta Analog Digital Converter (SDADC) */
  void* pfnPTC_Handler;                          /*  30 Peripheral Touch Controller (PTC) */
} DeviceVectors;

/* CORTEX-M0PLUS exception handlers */
void Reset_Handler                 ( void );
void NonMaskableInt_Handler        ( void );
void HardFault_Handler             ( void );
void SVCall_Handler                ( void );
void PendSV_Handler                ( void );
void SysTick_Handler               ( void );

/* Peripherals interrupt handlers */
void SYSTEM_Handler                ( void );
void WDT_Handler                   ( void );
void RTC_Handler                   ( void );
void EIC_Handler                   ( void );
void FREQM_Handler                 ( void );
void TSENS_Handler                 ( void );
void NVMCTRL_Handler               ( void );
void DMAC_Handler                  ( void );
void EVSYS_Handler                 ( void );
void SERCOM0_6_Handler             ( void );
void SERCOM1_7_Handler             ( void );
void SERCOM2_Handler               ( void );
void SERCOM3_Handler               ( void );
void SERCOM4_Handler               ( void );
void SERCOM5_Handler               ( void );
void CAN0_Handler                  ( void );
void CAN1_Handler                  ( void );
void TCC0_Handler                  ( void );
void TCC1_Handler                  ( void );
void TCC2_Handler                  ( void );
void TC0_5_Handler                 ( void );
void TC1_6_Handler                 ( void );
void TC2_7_Handler                 ( void );
void TC3_Handler                   ( void );
void TC4_Handler                   ( void );
void ADC0_Handler                  ( void );
void ADC1_Handler                  ( void );
void AC_Handler                    ( void );
void DAC_Handler                   ( void );
void SDADC_Handler                 ( void );
void PTC_Handler                   ( void );

/*
 * \brief Configuration of the CORTEX-M0PLUS Processor and Core Peripherals
 */
#define __MPU_PRESENT                  1 /**< MPU present or not                                                        */
#define __NVIC_PRIO_BITS               2 /**< Number of Bits used for Priority Levels                                   */
#define __VTOR_PRESENT                 1 /**< Vector Table Offset Register present or not                               */
#define __Vendor_SysTickConfig         0 /**< Set to 1 if different SysTick Config is used                              */
#define __ARCH_ARM                     1
#define __ARCH_ARM_CORTEX_M            1
#define __DEVICE_IS_SAM                1

/*
 * \brief CMSIS includes
 */
#include "core_cm0plus.h"

/** @}  end of SAMC21N18A_cmsis CMSIS Definitions */

/** \defgroup SAMC21N18A_api Peripheral Software API
 *  @{
 */

/* ************************************************************************** */
/**  SOFTWARE PERIPHERAL API DEFINITION FOR SAMC21N18A                        */
/* ************************************************************************** */
#include "component/ac.h"
#include "component/adc.h"
#include "component/can.h"
#include "component/ccl.h"
#include "component/dac.h"
#include "component/divas.h"
#include "component/dmac.h"
#include "component/dsu.h"
#include "component/eic.h"
#include "component/evsys.h"
#include "component/freqm.h"
#include "component/gclk.h"
#include "component/hmatrixb.h"
#include "component/mclk.h"
#include "component/mtb.h"
#include "component/nvmctrl.h"
#include "component/osc32kctrl.h"
#include "component/oscctrl.h"
#include "component/pac.h"
#include "component/pm.h"
#include "component/port.h"
#include "component/ptc.h"
#include "component/rstc.h"
#include "component/rtc.h"
#include "component/sdadc.h"
#include "component/sercom.h"
#include "component/supc.h"
#include "component/tc.h"
#include "component/tcc.h"
#include "component/tsens.h"
#include "component/wdt.h"

/** @}  end of Peripheral Software API */

/** \addtogroup SAMC21N18A_id Peripheral Ids Definitions
 *  @{
 */

/* ************************************************************************** */
/*  PERIPHERAL ID DEFINITIONS FOR SAMC21N18A                                  */
/* ************************************************************************** */
#define ID_AC            ( 84) /**< \brief Analog Comparators (AC) */
#define ID_ADC0          ( 81) /**< \brief Analog Digital Converter (ADC0) */
#define ID_ADC1          ( 82) /**< \brief Analog Digital Converter (ADC1) */
#define ID_CAN0          ( 71) /**< \brief Control Area Network (CAN0) */
#define ID_CAN1          ( 72) /**< \brief Control Area Network (CAN1) */
#define ID_CCL           ( 87) /**< \brief Configurable Custom Logic (CCL) */
#define ID_DAC           ( 85) /**< \brief Digital Analog Converter (DAC) */
#define ID_DMAC          ( 35) /**< \brief Direct Memory Access Controller (DMAC) */
#define ID_DSU           ( 33) /**< \brief Device Service Unit (DSU) */
#define ID_EIC           ( 10) /**< \brief External Interrupt Controller (EIC) */
#define ID_EVSYS         ( 64) /**< \brief Event System Interface (EVSYS) */
#define ID_FREQM         ( 11) /**< \brief Frequency Meter (FREQM) */
#define ID_GCLK          (  7) /**< \brief Generic Clock Generator (GCLK) */
#define ID_HMATRIXHS     ( 37) /**< \brief HSB Matrix (HMATRIXHS) */
#define ID_MCLK          (  2) /**< \brief Main Clock (MCLK) */
#define ID_MTB           ( 36) /**< \brief Cortex-M0+ Micro-Trace Buffer (MTB) */
#define ID_NVMCTRL       ( 34) /**< \brief Non-Volatile Memory Controller (NVMCTRL) */
#define ID_OSC32KCTRL    (  5) /**< \brief 32k Oscillators Control (OSC32KCTRL) */
#define ID_OSCCTRL       (  4) /**< \brief Oscillators Control (OSCCTRL) */
#define ID_PM            (  1) /**< \brief Power Manager (PM) */
#define ID_PORT          ( 32) /**< \brief Port Module (PORT) */
#define ID_PTC           ( 86) /**< \brief Peripheral Touch Controller (PTC) */
#define ID_RSTC          (  3) /**< \brief Reset Controller (RSTC) */
#define ID_RTC           (  9) /**< \brief Real-Time Counter (RTC) */
#define ID_SDADC         ( 83) /**< \brief Sigma-Delta Analog Digital Converter (SDADC) */
#define ID_SERCOM0       ( 65) /**< \brief Serial Communication Interface (SERCOM0) */
#define ID_SERCOM1       ( 66) /**< \brief Serial Communication Interface (SERCOM1) */
#define ID_SERCOM2       ( 67) /**< \brief Serial Communication Interface (SERCOM2) */
#define ID_SERCOM3       ( 68) /**< \brief Serial Communication Interface (SERCOM3) */
#define ID_SERCOM4       ( 69) /**< \brief Serial Communication Interface (SERCOM4) */
#define ID_SERCOM5       ( 70) /**< \brief Serial Communication Interface (SERCOM5) */
#define ID_SERCOM6       ( 96) /**< \brief Serial Communication Interface (SERCOM6) */
#define ID_SERCOM7       ( 97) /**< \brief Serial Communication Interface (SERCOM7) */
#define ID_SUPC          (  6) /**< \brief Supply Controller (SUPC) */
#define ID_TC0           ( 76) /**< \brief Basic Timer Counter (TC0) */
#define ID_TC1           ( 77) /**< \brief Basic Timer Counter (TC1) */
#define ID_TC2           ( 78) /**< \brief Basic Timer Counter (TC2) */
#define ID_TC3           ( 79) /**< \brief Basic Timer Counter (TC3) */
#define ID_TC4           ( 80) /**< \brief Basic Timer Counter (TC4) */
#define ID_TC5           ( 98) /**< \brief Basic Timer Counter (TC5) */
#define ID_TC6           ( 99) /**< \brief Basic Timer Counter (TC6) */
#define ID_TC7           (100) /**< \brief Basic Timer Counter (TC7) */
#define ID_TCC0          ( 73) /**< \brief Timer Counter Control (TCC0) */
#define ID_TCC1          ( 74) /**< \brief Timer Counter Control (TCC1) */
#define ID_TCC2          ( 75) /**< \brief Timer Counter Control (TCC2) */
#define ID_TSENS         ( 12) /**< \brief Temperature Sensor (TSENS) */
#define ID_WDT           (  8) /**< \brief Watchdog Timer (WDT) */

#define ID_PERIPH_MAX  (101) /**< \brief Number of peripheral IDs */

/** @}  end of Peripheral Ids Definitions */

/** \addtogroup SAMC21N18A_base Peripheral Base Address Definitions
 *  @{
 */

/* ************************************************************************** */
/*   REGISTER STRUCTURE ADDRESS DEFINITIONS FOR SAMC21N18A                    */
/* ************************************************************************** */
#define AC_REGS                          ((ac_registers_t*)0x42005000)                 /**< \brief AC Registers Address         */
#define ADC0_REGS                        ((adc_registers_t*)0x42004400)                /**< \brief ADC0 Registers Address       */
#define ADC1_REGS                        ((adc_registers_t*)0x42004800)                /**< \brief ADC1 Registers Address       */
#define CAN0_REGS                        ((can_registers_t*)0x42001c00)                /**< \brief CAN0 Registers Address       */
#define CAN1_REGS                        ((can_registers_t*)0x42002000)                /**< \brief CAN1 Registers Address       */
#define CCL_REGS                         ((ccl_registers_t*)0x42005c00)                /**< \brief CCL Registers Address        */
#define DAC_REGS                         ((dac_registers_t*)0x42005400)                /**< \brief DAC Registers Address        */
#define DIVAS_REGS                       ((divas_registers_t*)0x48000000)              /**< \brief DIVAS Registers Address      */
#define DMAC_REGS                        ((dmac_registers_t*)0x41006000)               /**< \brief DMAC Registers Address       */
#define DSU_REGS                         ((dsu_registers_t*)0x41002000)                /**< \brief DSU Registers Address        */
#define EIC_REGS                         ((eic_registers_t*)0x40002800)                /**< \brief EIC Registers Address        */
#define EVSYS_REGS                       ((evsys_registers_t*)0x42000000)              /**< \brief EVSYS Registers Address      */
#define FREQM_REGS                       ((freqm_registers_t*)0x40002c00)              /**< \brief FREQM Registers Address      */
#define GCLK_REGS                        ((gclk_registers_t*)0x40001c00)               /**< \brief GCLK Registers Address       */
#define HMATRIXHS_REGS                   ((hmatrixb_registers_t*)0x4100a000)           /**< \brief HMATRIXHS Registers Address  */
#define MCLK_REGS                        ((mclk_registers_t*)0x40000800)               /**< \brief MCLK Registers Address       */
#define MTB_REGS                         ((mtb_registers_t*)0x41008000)                /**< \brief MTB Registers Address        */
#define NVMCTRL_REGS                     ((nvmctrl_registers_t*)0x41004000)            /**< \brief NVMCTRL Registers Address    */
#define OSCCTRL_REGS                     ((oscctrl_registers_t*)0x40001000)            /**< \brief OSCCTRL Registers Address    */
#define OSC32KCTRL_REGS                  ((osc32kctrl_registers_t*)0x40001400)         /**< \brief OSC32KCTRL Registers Address */
#define PAC_REGS                         ((pac_registers_t*)0x40000000)                /**< \brief PAC Registers Address        */
#define PM_REGS                          ((pm_registers_t*)0x40000400)                 /**< \brief PM Registers Address         */
#define PORTA_REGS                       ((port_registers_t*)0x41000000)               /**< \brief PORTA Registers Address       */
#define PORTB_REGS                       ((port_registers_t*)0x41000080)               /**< \brief PORTB Registers Address       */
#define PORTC_REGS                       ((port_registers_t*)0x41000100)               /**< \brief PORTC Registers Address       */
#define PTC_REGS                         ((ptc_registers_t*)0x42005800)                /**< \brief PTC Registers Address        */
#define RSTC_REGS                        ((rstc_registers_t*)0x40000c00)               /**< \brief RSTC Registers Address       */
#define RTC_REGS                         ((rtc_registers_t*)0x40002400)                /**< \brief RTC Registers Address        */
#define SDADC_REGS                       ((sdadc_registers_t*)0x42004c00)              /**< \brief SDADC Registers Address      */
#define SERCOM0_REGS                     ((sercom_registers_t*)0x42000400)             /**< \brief SERCOM0 Registers Address    */
#define SERCOM1_REGS                     ((sercom_registers_t*)0x42000800)             /**< \brief SERCOM1 Registers Address    */
#define SERCOM2_REGS                     ((sercom_registers_t*)0x42000c00)             /**< \brief SERCOM2 Registers Address    */
#define SERCOM3_REGS                     ((sercom_registers_t*)0x42001000)             /**< \brief SERCOM3 Registers Address    */
#define SERCOM4_REGS                     ((sercom_registers_t*)0x42001400)             /**< \brief SERCOM4 Registers Address    */
#define SERCOM5_REGS                     ((sercom_registers_t*)0x42001800)             /**< \brief SERCOM5 Registers Address    */
#define SERCOM6_REGS                     ((sercom_registers_t*)0x43000000)             /**< \brief SERCOM6 Registers Address    */
#define SERCOM7_REGS                     ((sercom_registers_t*)0x43000400)             /**< \brief SERCOM7 Registers Address    */
#define SUPC_REGS                        ((supc_registers_t*)0x40001800)               /**< \brief SUPC Registers Address       */
#define TC0_REGS                         ((tc_registers_t*)0x42003000)                 /**< \brief TC0 Registers Address        */
#define TC1_REGS                         ((tc_registers_t*)0x42003400)                 /**< \brief TC1 Registers Address        */
#define TC2_REGS                         ((tc_registers_t*)0x42003800)                 /**< \brief TC2 Registers Address        */
#define TC3_REGS                         ((tc_registers_t*)0x42003c00)                 /**< \brief TC3 Registers Address        */
#define TC4_REGS                         ((tc_registers_t*)0x42004000)                 /**< \brief TC4 Registers Address        */
#define TC5_REGS                         ((tc_registers_t*)0x43000800)                 /**< \brief TC5 Registers Address        */
#define TC6_REGS                         ((tc_registers_t*)0x43000c00)                 /**< \brief TC6 Registers Address        */
#define TC7_REGS                         ((tc_registers_t*)0x43001000)                 /**< \brief TC7 Registers Address        */
#define TCC0_REGS                        ((tcc_registers_t*)0x42002400)                /**< \brief TCC0 Registers Address       */
#define TCC1_REGS                        ((tcc_registers_t*)0x42002800)                /**< \brief TCC1 Registers Address       */
#define TCC2_REGS                        ((tcc_registers_t*)0x42002c00)                /**< \brief TCC2 Registers Address       */
#define TSENS_REGS                       ((tsens_registers_t*)0x40003000)              /**< \brief TSENS Registers Address      */
#define WDT_REGS                         ((wdt_registers_t*)0x40002000)                /**< \brief WDT Registers Address        */

/* ************************************************************************** */
/*   BASE ADDRESS DEFINITIONS FOR SAMC21N18A                                  */
/* ************************************************************************** */

#define AC_BASE_ADDRESS                  (0x42005000UL)                                /**< \brief AC Base Address              */
#define ADC0_BASE_ADDRESS                (0x42004400UL)                                /**< \brief ADC0 Base Address            */
#define ADC1_BASE_ADDRESS                (0x42004800UL)                                /**< \brief ADC1 Base Address            */
#define CAN0_BASE_ADDRESS                (0x42001c00UL)                                /**< \brief CAN0 Base Address            */
#define CAN1_BASE_ADDRESS                (0x42002000UL)                                /**< \brief CAN1 Base Address            */
#define CCL_BASE_ADDRESS                 (0x42005c00UL)                                /**< \brief CCL Base Address             */
#define DAC_BASE_ADDRESS                 (0x42005400UL)                                /**< \brief DAC Base Address             */
#define DIVAS_BASE_ADDRESS               (0x48000000UL)                                /**< \brief DIVAS Base Address           */
#define DMAC_BASE_ADDRESS                (0x41006000UL)                                /**< \brief DMAC Base Address            */
#define DSU_BASE_ADDRESS                 (0x41002000UL)                                /**< \brief DSU Base Address             */
#define EIC_BASE_ADDRESS                 (0x40002800UL)                                /**< \brief EIC Base Address             */
#define EVSYS_BASE_ADDRESS               (0x42000000UL)                                /**< \brief EVSYS Base Address           */
#define FREQM_BASE_ADDRESS               (0x40002c00UL)                                /**< \brief FREQM Base Address           */
#define GCLK_BASE_ADDRESS                (0x40001c00UL)                                /**< \brief GCLK Base Address            */
#define HMATRIXHS_BASE_ADDRESS           (0x4100a000UL)                                /**< \brief HMATRIXHS Base Address       */
#define MCLK_BASE_ADDRESS                (0x40000800UL)                                /**< \brief MCLK Base Address            */
#define MTB_BASE_ADDRESS                 (0x41008000UL)                                /**< \brief MTB Base Address             */
#define NVMCTRL_BASE_ADDRESS             (0x41004000UL)                                /**< \brief NVMCTRL Base Address         */
#define OSCCTRL_BASE_ADDRESS             (0x40001000UL)                                /**< \brief OSCCTRL Base Address         */
#define OSC32KCTRL_BASE_ADDRESS          (0x40001400UL)                                /**< \brief OSC32KCTRL Base Address      */
#define PAC_BASE_ADDRESS                 (0x40000000UL)                                /**< \brief PAC Base Address             */
#define PM_BASE_ADDRESS                  (0x40000400UL)                                /**< \brief PM Base Address              */
#define PORTA_BASE_ADDRESS               (0x41000000UL)                                /**< \brief PORTA Base Address           */
#define PORTB_BASE_ADDRESS               (0x41000080UL)                                /**< \brief PORTB Base Address           */
#define PORTC_BASE_ADDRESS               (0x41000100UL)                                /**< \brief PORTC Base Address           */
#define PTC_BASE_ADDRESS                 (0x42005800UL)                                /**< \brief PTC Base Address             */
#define RSTC_BASE_ADDRESS                (0x40000c00UL)                                /**< \brief RSTC Base Address            */
#define RTC_BASE_ADDRESS                 (0x40002400UL)                                /**< \brief RTC Base Address             */
#define SDADC_BASE_ADDRESS               (0x42004c00UL)                                /**< \brief SDADC Base Address           */
#define SERCOM0_BASE_ADDRESS             (0x42000400UL)                                /**< \brief SERCOM0 Base Address         */
#define SERCOM1_BASE_ADDRESS             (0x42000800UL)                                /**< \brief SERCOM1 Base Address         */
#define SERCOM2_BASE_ADDRESS             (0x42000c00UL)                                /**< \brief SERCOM2 Base Address         */
#define SERCOM3_BASE_ADDRESS             (0x42001000UL)                                /**< \brief SERCOM3 Base Address         */
#define SERCOM4_BASE_ADDRESS             (0x42001400UL)                                /**< \brief SERCOM4 Base Address         */
#define SERCOM5_BASE_ADDRESS             (0x42001800UL)                                /**< \brief SERCOM5 Base Address         */
#define SERCOM6_BASE_ADDRESS             (0x43000000UL)                                /**< \brief SERCOM6 Base Address         */
#define SERCOM7_BASE_ADDRESS             (0x43000400UL)                                /**< \brief SERCOM7 Base Address         */
#define SUPC_BASE_ADDRESS                (0x40001800UL)                                /**< \brief SUPC Base Address            */
#define TC0_BASE_ADDRESS                 (0x42003000UL)                                /**< \brief TC0 Base Address             */
#define TC1_BASE_ADDRESS                 (0x42003400UL)                                /**< \brief TC1 Base Address             */
#define TC2_BASE_ADDRESS                 (0x42003800UL)                                /**< \brief TC2 Base Address             */
#define TC3_BASE_ADDRESS                 (0x42003c00UL)                                /**< \brief TC3 Base Address             */
#define TC4_BASE_ADDRESS                 (0x42004000UL)                                /**< \brief TC4 Base Address             */
#define TC5_BASE_ADDRESS                 (0x43000800UL)                                /**< \brief TC5 Base Address             */
#define TC6_BASE_ADDRESS                 (0x43000c00UL)                                /**< \brief TC6 Base Address             */
#define TC7_BASE_ADDRESS                 (0x43001000UL)                                /**< \brief TC7 Base Address             */
#define TCC0_BASE_ADDRESS                (0x42002400UL)                                /**< \brief TCC0 Base Address            */
#define TCC1_BASE_ADDRESS                (0x42002800UL)                                /**< \brief TCC1 Base Address            */
#define TCC2_BASE_ADDRESS                (0x42002c00UL)                                /**< \brief TCC2 Base Address            */
#define TSENS_BASE_ADDRESS               (0x40003000UL)                                /**< \brief TSENS Base Address           */
#define WDT_BASE_ADDRESS                 (0x40002000UL)                                /**< \brief WDT Base Address             */

/** \addtogroup SAMC21N18A_pio Peripheral Pio Definitions
 *  @{
 */

/* ************************************************************************** */
/*   PIO DEFINITIONS FOR SAMC21N18A                                           */
/* ************************************************************************** */
#include "pio/samc21n18a.h"

/** @}  end of Peripheral Pio Definitions */

/* ************************************************************************** */
/*   MEMORY MAPPING DEFINITIONS FOR SAMC21N18A                                */
/* ************************************************************************** */

#define FLASH_SIZE                     (0x00040000UL)      /*  256kB Memory segment type: flash */
#define FLASH_PAGE_SIZE                (0x00000040UL)
#define FLASH_NB_OF_PAGES              (0x00001000UL)
#define CAL_SIZE                       (0x00000008UL)      /*    0kB Memory segment type: fuses */
#define LOCKBIT_SIZE                   (0x00000004UL)      /*    0kB Memory segment type: fuses */
#define OTP1_SIZE                      (0x00000008UL)      /*    0kB Memory segment type: fuses */
#define OTP2_SIZE                      (0x00000008UL)      /*    0kB Memory segment type: fuses */
#define OTP3_SIZE                      (0x00000008UL)      /*    0kB Memory segment type: fuses */
#define OTP4_SIZE                      (0x00000008UL)      /*    0kB Memory segment type: fuses */
#define OTP5_SIZE                      (0x00000008UL)      /*    0kB Memory segment type: fuses */
#define TEMP_LOG_SIZE                  (0x00000008UL)      /*    0kB Memory segment type: fuses */
#define USER_PAGE_SIZE                 (0x00000100UL)      /*    0kB Memory segment type: user_page */
#define USER_PAGE_PAGE_SIZE            (0x00000040UL)
#define USER_PAGE_NB_OF_PAGES          (0x00000004UL)
#define RWW_SIZE                       (0x00002000UL)      /*    8kB Memory segment type: flash */
#define RWW_PAGE_SIZE                  (0x00000040UL)
#define RWW_NB_OF_PAGES                (0x00000080UL)
#define HSRAM_SIZE                     (0x00008000UL)      /*   32kB Memory segment type: ram */
#define HPB0_SIZE                      (0x00004000UL)      /*   16kB Memory segment type: io */
#define HPB1_SIZE                      (0x00010000UL)      /*   64kB Memory segment type: io */
#define HPB2_SIZE                      (0x00008000UL)      /*   32kB Memory segment type: io */
#define HPB3_SIZE                      (0x00008000UL)      /*   32kB Memory segment type: io */
#define DIVAS_SIZE                     (0x00000020UL)      /*    0kB Memory segment type: io */
#define PPB_SIZE                       (0x00100000UL)      /* 1024kB Memory segment type: io */
#define SCS_SIZE                       (0x00001000UL)      /*    4kB Memory segment type: io */
#define PERIPHERALS_SIZE               (0x20000000UL)      /* 524288kB Memory segment type: io */
#define FLASH_ADDR                     (0x00000000UL)      /**< FLASH base address (type: flash) */
#define CAL_ADDR                       (0x00800000UL)      /**< CAL base address (type: fuses) */
#define LOCKBIT_ADDR                   (0x00802000UL)      /**< LOCKBIT base address (type: fuses) */
#define OTP1_ADDR                      (0x00806000UL)      /**< OTP1 base address (type: fuses) */
#define OTP2_ADDR                      (0x00806008UL)      /**< OTP2 base address (type: fuses) */
#define OTP3_ADDR                      (0x00806010UL)      /**< OTP3 base address (type: fuses) */
#define OTP4_ADDR                      (0x00806018UL)      /**< OTP4 base address (type: fuses) */
#define OTP5_ADDR                      (0x00806020UL)      /**< OTP5 base address (type: fuses) */
#define TEMP_LOG_ADDR                  (0x00806030UL)      /**< TEMP_LOG base address (type: fuses) */
#define USER_PAGE_ADDR                 (0x00804000UL)      /**< USER_PAGE base address (type: user_page) */
#define RWW_ADDR                       (0x00400000UL)      /**< RWW base address (type: flash) */
#define HSRAM_ADDR                     (0x20000000UL)      /**< HSRAM base address (type: ram) */
#define HPB0_ADDR                      (0x40000000UL)      /**< HPB0 base address (type: io) */
#define HPB1_ADDR                      (0x41000000UL)      /**< HPB1 base address (type: io) */
#define HPB2_ADDR                      (0x42000000UL)      /**< HPB2 base address (type: io) */
#define HPB3_ADDR                      (0x43000000UL)      /**< HPB3 base address (type: io) */
#define DIVAS_ADDR                     (0x48000000UL)      /**< DIVAS base address (type: io) */
#define PPB_ADDR                       (0xe0000000UL)      /**< PPB base address (type: io) */
#define SCS_ADDR                       (0xe000e000UL)      /**< SCS base address (type: io) */
#define PERIPHERALS_ADDR               (0x40000000UL)      /**< PERIPHERALS base address (type: io) */

/* ************************************************************************** */
/**  DEVICE SIGNATURES FOR SAMC21N18A                                         */
/* ************************************************************************** */
#define DSU_DID                        (0x11011420UL)

/* ************************************************************************** */
/**  ELECTRICAL DEFINITIONS FOR SAMC21N18A                                    */
/* ************************************************************************** */

#ifdef __cplusplus
}
#endif

/** @}  end of SAMC21N18A definitions */

#endif /* SAMC21N18A_H */

