/**
 * \brief Header file for SAMG55J19
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
#ifndef SAMG55J19_H
#define SAMG55J19_H

// Header version uses Semantic Versioning 2.0.0 (https://semver.org/)
#define HEADER_FORMAT_VERSION "2.0.0"

#define HEADER_FORMAT_VERSION_MAJOR (2)
#define HEADER_FORMAT_VERSION_MINOR (0)

/** \addtogroup SAMG55J19_definitions SAMG55J19 definitions
  This file defines all structures and symbols for SAMG55J19:
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

/** \addtogroup SAMG55J19_cmsis CMSIS Definitions
 *  @{
 */

/* ************************************************************************** */
/*   CMSIS DEFINITIONS FOR SAMG55J19                                          */
/* ************************************************************************** */
/** Interrupt Number Definition */
typedef enum IRQn
{
/******  CORTEX-4 Processor Exceptions Numbers ******************************/
  Reset_IRQn                = -15, /**< -15 Reset Vector, invoked on Power up and warm reset */
  NonMaskableInt_IRQn       = -14, /**< -14 Non maskable Interrupt, cannot be stopped or preempted */
  HardFault_IRQn            = -13, /**< -13 Hard Fault, all classes of Fault    */
  MemoryManagement_IRQn     = -12, /**< -12 Memory Management, MPU mismatch, including Access Violation and No Match */
  BusFault_IRQn             = -11, /**< -11 Bus Fault, Pre-Fetch-, Memory Access Fault, other address/memory related Fault */
  UsageFault_IRQn           = -10, /**< -10 Usage Fault, i.e. Undef Instruction, Illegal State Transition */
  SVCall_IRQn               =  -5, /**< -5  System Service Call via SVC instruction */
  DebugMonitor_IRQn         =  -4, /**< -4  Debug Monitor                       */
  PendSV_IRQn               =  -2, /**< -2  Pendable request for system service */
  SysTick_IRQn              =  -1, /**< -1  System Tick Timer                   */
/******  SAMG55J19 specific Interrupt Numbers ***********************************/
  SUPC_IRQn                 =   0, /**< 0   Supply Controller (SUPC)            */
  RSTC_IRQn                 =   1, /**< 1   Reset Controller (RSTC)             */
  RTC_IRQn                  =   2, /**< 2   Real-time Clock (RTC)               */
  RTT_IRQn                  =   3, /**< 3   Real-time Timer (RTT)               */
  WDT_IRQn                  =   4, /**< 4   Watchdog Timer (WDT)                */
  PMC_IRQn                  =   5, /**< 5   Power Management Controller (PMC)   */
  EFC_IRQn                  =   6, /**< 6   Embedded Flash Controller (EFC)     */
  FLEXCOM7_IRQn             =   7, /**< 7   Flexible Serial Communication (FLEXCOM7) */
  FLEXCOM0_IRQn             =   8, /**< 8   Flexible Serial Communication (FLEXCOM0) */
  FLEXCOM1_IRQn             =   9, /**< 9   Flexible Serial Communication (FLEXCOM1) */
  PIOA_IRQn                 =  11, /**< 11  Parallel Input/Output Controller (PIOA) */
  PIOB_IRQn                 =  12, /**< 12  Parallel Input/Output Controller (PIOB) */
  PDMIC0_IRQn               =  13, /**< 13  Pulse Density Modulation Interface Controller (PDMIC0) */
  FLEXCOM2_IRQn             =  14, /**< 14  Flexible Serial Communication (FLEXCOM2) */
  MEM2MEM_IRQn              =  15, /**< 15  Memory to Memory (MEM2MEM)          */
  I2SC0_IRQn                =  16, /**< 16  Inter-IC Sound Controller (I2SC0)   */
  I2SC1_IRQn                =  17, /**< 17  Inter-IC Sound Controller (I2SC1)   */
  PDMIC1_IRQn               =  18, /**< 18  Pulse Density Modulation Interface Controller (PDMIC1) */
  FLEXCOM3_IRQn             =  19, /**< 19  Flexible Serial Communication (FLEXCOM3) */
  FLEXCOM4_IRQn             =  20, /**< 20  Flexible Serial Communication (FLEXCOM4) */
  FLEXCOM5_IRQn             =  21, /**< 21  Flexible Serial Communication (FLEXCOM5) */
  FLEXCOM6_IRQn             =  22, /**< 22  Flexible Serial Communication (FLEXCOM6) */
  TC0_IRQn                  =  23, /**< 23  Timer Counter (TC0)                 */
  TC1_IRQn                  =  24, /**< 24  Timer Counter (TC0)                 */
  TC2_IRQn                  =  25, /**< 25  Timer Counter (TC0)                 */
  TC3_IRQn                  =  26, /**< 26  Timer Counter (TC1)                 */
  TC4_IRQn                  =  27, /**< 27  Timer Counter (TC1)                 */
  TC5_IRQn                  =  28, /**< 28  Timer Counter (TC1)                 */
  ADC_IRQn                  =  29, /**< 29  Analog-to-Digital Converter (ADC)   */
  UHP_IRQn                  =  47, /**< 47  USB Host Port (UHP)                 */
  UDP_IRQn                  =  48, /**< 48  USB Device Port (UDP)               */
  CRCCU_IRQn                =  49, /**< 49  Cyclic Redundancy Check Calculation Unit (CRCCU) */

  PERIPH_MAX_IRQn           =  49 /**< Number of peripheral IDs */
} IRQn_Type;

typedef struct _DeviceVectors
{
  /* Stack pointer */
  void* pvStack;
  /* Cortex-M handlers */
  void* pfnReset_Handler;                        /* -15 Reset Vector, invoked on Power up and warm reset */
  void* pfnNonMaskableInt_Handler;               /* -14 Non maskable Interrupt, cannot be stopped or preempted */
  void* pfnHardFault_Handler;                    /* -13 Hard Fault, all classes of Fault */
  void* pfnMemoryManagement_Handler;             /* -12 Memory Management, MPU mismatch, including Access Violation and No Match */
  void* pfnBusFault_Handler;                     /* -11 Bus Fault, Pre-Fetch-, Memory Access Fault, other address/memory related Fault */
  void* pfnUsageFault_Handler;                   /* -10 Usage Fault, i.e. Undef Instruction, Illegal State Transition */
  void* pvReservedC9;
  void* pvReservedC8;
  void* pvReservedC7;
  void* pvReservedC6;
  void* pfnSVCall_Handler;                       /*  -5 System Service Call via SVC instruction */
  void* pfnDebugMonitor_Handler;                 /*  -4 Debug Monitor */
  void* pvReservedC3;
  void* pfnPendSV_Handler;                       /*  -2 Pendable request for system service */
  void* pfnSysTick_Handler;                      /*  -1 System Tick Timer */

  /* Peripheral handlers */
  void* pfnSUPC_Handler;                         /*   0 Supply Controller (SUPC) */
  void* pfnRSTC_Handler;                         /*   1 Reset Controller (RSTC) */
  void* pfnRTC_Handler;                          /*   2 Real-time Clock (RTC) */
  void* pfnRTT_Handler;                          /*   3 Real-time Timer (RTT) */
  void* pfnWDT_Handler;                          /*   4 Watchdog Timer (WDT) */
  void* pfnPMC_Handler;                          /*   5 Power Management Controller (PMC) */
  void* pfnEFC_Handler;                          /*   6 Embedded Flash Controller (EFC) */
  void* pfnFLEXCOM7_Handler;                     /*   7 Flexible Serial Communication (FLEXCOM7) */
  void* pfnFLEXCOM0_Handler;                     /*   8 Flexible Serial Communication (FLEXCOM0) */
  void* pfnFLEXCOM1_Handler;                     /*   9 Flexible Serial Communication (FLEXCOM1) */
  void* pvReserved10;
  void* pfnPIOA_Handler;                         /*  11 Parallel Input/Output Controller (PIOA) */
  void* pfnPIOB_Handler;                         /*  12 Parallel Input/Output Controller (PIOB) */
  void* pfnPDMIC0_Handler;                       /*  13 Pulse Density Modulation Interface Controller (PDMIC0) */
  void* pfnFLEXCOM2_Handler;                     /*  14 Flexible Serial Communication (FLEXCOM2) */
  void* pfnMEM2MEM_Handler;                      /*  15 Memory to Memory (MEM2MEM) */
  void* pfnI2SC0_Handler;                        /*  16 Inter-IC Sound Controller (I2SC0) */
  void* pfnI2SC1_Handler;                        /*  17 Inter-IC Sound Controller (I2SC1) */
  void* pfnPDMIC1_Handler;                       /*  18 Pulse Density Modulation Interface Controller (PDMIC1) */
  void* pfnFLEXCOM3_Handler;                     /*  19 Flexible Serial Communication (FLEXCOM3) */
  void* pfnFLEXCOM4_Handler;                     /*  20 Flexible Serial Communication (FLEXCOM4) */
  void* pfnFLEXCOM5_Handler;                     /*  21 Flexible Serial Communication (FLEXCOM5) */
  void* pfnFLEXCOM6_Handler;                     /*  22 Flexible Serial Communication (FLEXCOM6) */
  void* pfnTC0_Handler;                          /*  23 Timer Counter (TC0) */
  void* pfnTC1_Handler;                          /*  24 Timer Counter (TC0) */
  void* pfnTC2_Handler;                          /*  25 Timer Counter (TC0) */
  void* pfnTC3_Handler;                          /*  26 Timer Counter (TC1) */
  void* pfnTC4_Handler;                          /*  27 Timer Counter (TC1) */
  void* pfnTC5_Handler;                          /*  28 Timer Counter (TC1) */
  void* pfnADC_Handler;                          /*  29 Analog-to-Digital Converter (ADC) */
  void* pvReserved30;
  void* pvReserved31;
  void* pvReserved32;
  void* pvReserved33;
  void* pvReserved34;
  void* pvReserved35;
  void* pvReserved36;
  void* pvReserved37;
  void* pvReserved38;
  void* pvReserved39;
  void* pvReserved40;
  void* pvReserved41;
  void* pvReserved42;
  void* pvReserved43;
  void* pvReserved44;
  void* pvReserved45;
  void* pvReserved46;
  void* pfnUHP_Handler;                          /*  47 USB Host Port (UHP) */
  void* pfnUDP_Handler;                          /*  48 USB Device Port (UDP) */
  void* pfnCRCCU_Handler;                        /*  49 Cyclic Redundancy Check Calculation Unit (CRCCU) */
} DeviceVectors;

/* CORTEX-M4 exception handlers */
void Reset_Handler                 ( void );
void NonMaskableInt_Handler        ( void );
void HardFault_Handler             ( void );
void MemoryManagement_Handler      ( void );
void BusFault_Handler              ( void );
void UsageFault_Handler            ( void );
void SVCall_Handler                ( void );
void DebugMonitor_Handler          ( void );
void PendSV_Handler                ( void );
void SysTick_Handler               ( void );

/* Peripherals interrupt handlers */
void SUPC_Handler                  ( void );
void RSTC_Handler                  ( void );
void RTC_Handler                   ( void );
void RTT_Handler                   ( void );
void WDT_Handler                   ( void );
void PMC_Handler                   ( void );
void EFC_Handler                   ( void );
void FLEXCOM7_Handler              ( void );
void FLEXCOM0_Handler              ( void );
void FLEXCOM1_Handler              ( void );
void PIOA_Handler                  ( void );
void PIOB_Handler                  ( void );
void PDMIC0_Handler                ( void );
void FLEXCOM2_Handler              ( void );
void MEM2MEM_Handler               ( void );
void I2SC0_Handler                 ( void );
void I2SC1_Handler                 ( void );
void PDMIC1_Handler                ( void );
void FLEXCOM3_Handler              ( void );
void FLEXCOM4_Handler              ( void );
void FLEXCOM5_Handler              ( void );
void FLEXCOM6_Handler              ( void );
void TC0_Handler                   ( void );
void TC1_Handler                   ( void );
void TC2_Handler                   ( void );
void TC3_Handler                   ( void );
void TC4_Handler                   ( void );
void TC5_Handler                   ( void );
void ADC_Handler                   ( void );
void UHP_Handler                   ( void );
void UDP_Handler                   ( void );
void CRCCU_Handler                 ( void );

/*
 * \brief Configuration of the CORTEX-M4 Processor and Core Peripherals
 */
#define __CM4_REV                 0x0001 /**< CM4 Core Revision                                                         */
#define __NVIC_PRIO_BITS               4 /**< Number of Bits used for Priority Levels                                   */
#define __Vendor_SysTickConfig         0 /**< Set to 1 if different SysTick Config is used                              */
#define __MPU_PRESENT                  1 /**< MPU present or not                                                        */
#define __VTOR_PRESENT                 1 /**< Vector Table Offset Register present or not                               */
#define __FPU_PRESENT                  1 /**< FPU present or not                                                        */
#define __ARCH_ARM                     1
#define __ARCH_ARM_CORTEX_M            1
#define __DEVICE_IS_SAM                1

/*
 * \brief CMSIS includes
 */
#include <core_cm4.h>

/** @}  end of SAMG55J19_cmsis CMSIS Definitions */

/** \defgroup SAMG55J19_api Peripheral Software API
 *  @{
 */

/* ************************************************************************** */
/**  SOFTWARE PERIPHERAL API DEFINITION FOR SAMG55J19                         */
/* ************************************************************************** */
#include "component/adc.h"
#include "component/chipid.h"
#include "component/cmcc.h"
#include "component/crccu.h"
#include "component/efc.h"
#include "component/flexcom.h"
#include "component/gpbr.h"
#include "component/i2sc.h"
#include "component/matrix.h"
#include "component/mem2mem.h"
#include "component/pdmic.h"
#include "component/pio.h"
#include "component/pmc.h"
#include "component/rstc.h"
#include "component/rtc.h"
#include "component/rtt.h"
#include "component/spi.h"
#include "component/supc.h"
#include "component/tc.h"
#include "component/twi.h"
#include "component/udp.h"
#include "component/uhp.h"
#include "component/usart.h"
#include "component/wdt.h"

/** @}  end of Peripheral Software API */

/** \addtogroup SAMG55J19_id Peripheral Ids Definitions
 *  @{
 */

/* ************************************************************************** */
/*  PERIPHERAL ID DEFINITIONS FOR SAMG55J19                                   */
/* ************************************************************************** */
#define ID_ADC           ( 29) /**< \brief Analog-to-Digital Converter (ADC) */
#define ID_CRCCU         ( 49) /**< \brief Cyclic Redundancy Check Calculation Unit (CRCCU) */
#define ID_EFC           (  6) /**< \brief Embedded Flash Controller (EFC) */
#define ID_FLEXCOM0      (  8) /**< \brief Flexible Serial Communication (FLEXCOM0) */
#define ID_FLEXCOM1      (  9) /**< \brief Flexible Serial Communication (FLEXCOM1) */
#define ID_FLEXCOM2      ( 14) /**< \brief Flexible Serial Communication (FLEXCOM2) */
#define ID_FLEXCOM3      ( 19) /**< \brief Flexible Serial Communication (FLEXCOM3) */
#define ID_FLEXCOM4      ( 20) /**< \brief Flexible Serial Communication (FLEXCOM4) */
#define ID_FLEXCOM5      ( 21) /**< \brief Flexible Serial Communication (FLEXCOM5) */
#define ID_FLEXCOM6      ( 22) /**< \brief Flexible Serial Communication (FLEXCOM6) */
#define ID_FLEXCOM7      (  7) /**< \brief Flexible Serial Communication (FLEXCOM7) */
#define ID_I2SC0         ( 16) /**< \brief Inter-IC Sound Controller (I2SC0) */
#define ID_I2SC1         ( 17) /**< \brief Inter-IC Sound Controller (I2SC1) */
#define ID_MEM2MEM       ( 15) /**< \brief Memory to Memory (MEM2MEM) */
#define ID_PDMIC0        ( 13) /**< \brief Pulse Density Modulation Interface Controller (PDMIC0) */
#define ID_PDMIC1        ( 18) /**< \brief Pulse Density Modulation Interface Controller (PDMIC1) */
#define ID_PIOA          ( 11) /**< \brief Parallel Input/Output Controller (PIOA) */
#define ID_PIOB          ( 12) /**< \brief Parallel Input/Output Controller (PIOB) */
#define ID_PMC           (  5) /**< \brief Power Management Controller (PMC) */
#define ID_RSTC          (  1) /**< \brief Reset Controller (RSTC) */
#define ID_RTC           (  2) /**< \brief Real-time Clock (RTC) */
#define ID_RTT           (  3) /**< \brief Real-time Timer (RTT) */
#define ID_UDP           ( 48) /**< \brief USB Device Port (UDP) */
#define ID_UHP           ( 47) /**< \brief USB Host Port (UHP) */
#define ID_WDT           (  4) /**< \brief Watchdog Timer (WDT) */

#define ID_PERIPH_MAX  ( 50) /**< \brief Number of peripheral IDs */

/** @}  end of Peripheral Ids Definitions */

/** \addtogroup SAMG55J19_base Peripheral Base Address Definitions
 *  @{
 */

/* ************************************************************************** */
/*   REGISTER STRUCTURE ADDRESS DEFINITIONS FOR SAMG55J19                     */
/* ************************************************************************** */
#define ADC_REGS                         ((adc_registers_t*)0x40038000)                /**< \brief ADC Registers Address        */
#define CHIPID_REGS                      ((chipid_registers_t*)0x400e0740)             /**< \brief CHIPID Registers Address     */
#define CMCC_REGS                        ((cmcc_registers_t*)0x4003c000)               /**< \brief CMCC Registers Address       */
#define CRCCU_REGS                       ((crccu_registers_t*)0x40048000)              /**< \brief CRCCU Registers Address      */
#define EFC_REGS                         ((efc_registers_t*)0x400e0a00)                /**< \brief EFC Registers Address        */
#define FLEXCOM0_REGS                    ((flexcom_registers_t*)0x4000c000)            /**< \brief FLEXCOM0 Registers Address   */
#define FLEXCOM1_REGS                    ((flexcom_registers_t*)0x40020000)            /**< \brief FLEXCOM1 Registers Address   */
#define FLEXCOM2_REGS                    ((flexcom_registers_t*)0x40024000)            /**< \brief FLEXCOM2 Registers Address   */
#define FLEXCOM3_REGS                    ((flexcom_registers_t*)0x40018000)            /**< \brief FLEXCOM3 Registers Address   */
#define FLEXCOM4_REGS                    ((flexcom_registers_t*)0x4001c000)            /**< \brief FLEXCOM4 Registers Address   */
#define FLEXCOM5_REGS                    ((flexcom_registers_t*)0x40008000)            /**< \brief FLEXCOM5 Registers Address   */
#define FLEXCOM6_REGS                    ((flexcom_registers_t*)0x40040000)            /**< \brief FLEXCOM6 Registers Address   */
#define FLEXCOM7_REGS                    ((flexcom_registers_t*)0x40034000)            /**< \brief FLEXCOM7 Registers Address   */
#define GPBR_REGS                        ((gpbr_registers_t*)0x400e1490)               /**< \brief GPBR Registers Address       */
#define I2SC0_REGS                       ((i2sc_registers_t*)0x40000000)               /**< \brief I2SC0 Registers Address      */
#define I2SC1_REGS                       ((i2sc_registers_t*)0x40004000)               /**< \brief I2SC1 Registers Address      */
#define MATRIX_REGS                      ((matrix_registers_t*)0x400e0200)             /**< \brief MATRIX Registers Address     */
#define MEM2MEM_REGS                     ((mem2mem_registers_t*)0x40028000)            /**< \brief MEM2MEM Registers Address    */
#define PDMIC0_REGS                      ((pdmic_registers_t*)0x4002c000)              /**< \brief PDMIC0 Registers Address     */
#define PDMIC1_REGS                      ((pdmic_registers_t*)0x40030000)              /**< \brief PDMIC1 Registers Address     */
#define PIOA_REGS                        ((pio_registers_t*)0x400e0e00)                /**< \brief PIOA Registers Address       */
#define PIOB_REGS                        ((pio_registers_t*)0x400e1000)                /**< \brief PIOB Registers Address       */
#define PMC_REGS                         ((pmc_registers_t*)0x400e0400)                /**< \brief PMC Registers Address        */
#define RSTC_REGS                        ((rstc_registers_t*)0x400e1400)               /**< \brief RSTC Registers Address       */
#define RTC_REGS                         ((rtc_registers_t*)0x400e1460)                /**< \brief RTC Registers Address        */
#define RTT_REGS                         ((rtt_registers_t*)0x400e1430)                /**< \brief RTT Registers Address        */
#define SPI0_REGS                        ((spi_registers_t*)0x4000c400)                /**< \brief SPI0 Registers Address       */
#define SPI1_REGS                        ((spi_registers_t*)0x40020400)                /**< \brief SPI1 Registers Address       */
#define SPI2_REGS                        ((spi_registers_t*)0x40024400)                /**< \brief SPI2 Registers Address       */
#define SPI3_REGS                        ((spi_registers_t*)0x40018400)                /**< \brief SPI3 Registers Address       */
#define SPI4_REGS                        ((spi_registers_t*)0x4001c400)                /**< \brief SPI4 Registers Address       */
#define SPI5_REGS                        ((spi_registers_t*)0x40008400)                /**< \brief SPI5 Registers Address       */
#define SPI6_REGS                        ((spi_registers_t*)0x40040400)                /**< \brief SPI6 Registers Address       */
#define SPI7_REGS                        ((spi_registers_t*)0x40034400)                /**< \brief SPI7 Registers Address       */
#define SUPC_REGS                        ((supc_registers_t*)0x400e1410)               /**< \brief SUPC Registers Address       */
#define TC0_REGS                         ((tc_registers_t*)0x40010000)                 /**< \brief TC0 Registers Address        */
#define TC1_REGS                         ((tc_registers_t*)0x40014000)                 /**< \brief TC1 Registers Address        */
#define TWI0_REGS                        ((twi_registers_t*)0x4000c600)                /**< \brief TWI0 Registers Address       */
#define TWI1_REGS                        ((twi_registers_t*)0x40020600)                /**< \brief TWI1 Registers Address       */
#define TWI2_REGS                        ((twi_registers_t*)0x40024600)                /**< \brief TWI2 Registers Address       */
#define TWI3_REGS                        ((twi_registers_t*)0x40018600)                /**< \brief TWI3 Registers Address       */
#define TWI4_REGS                        ((twi_registers_t*)0x4001c600)                /**< \brief TWI4 Registers Address       */
#define TWI5_REGS                        ((twi_registers_t*)0x40008600)                /**< \brief TWI5 Registers Address       */
#define TWI6_REGS                        ((twi_registers_t*)0x40040600)                /**< \brief TWI6 Registers Address       */
#define TWI7_REGS                        ((twi_registers_t*)0x40034600)                /**< \brief TWI7 Registers Address       */
#define UDP_REGS                         ((udp_registers_t*)0x40044000)                /**< \brief UDP Registers Address        */
#define UHP_REGS                         ((uhp_registers_t*)0x4004c000)                /**< \brief UHP Registers Address        */
#define USART0_REGS                      ((usart_registers_t*)0x4000c200)              /**< \brief USART0 Registers Address     */
#define USART1_REGS                      ((usart_registers_t*)0x40020200)              /**< \brief USART1 Registers Address     */
#define USART2_REGS                      ((usart_registers_t*)0x40024200)              /**< \brief USART2 Registers Address     */
#define USART3_REGS                      ((usart_registers_t*)0x40018200)              /**< \brief USART3 Registers Address     */
#define USART4_REGS                      ((usart_registers_t*)0x4001c200)              /**< \brief USART4 Registers Address     */
#define USART5_REGS                      ((usart_registers_t*)0x40008200)              /**< \brief USART5 Registers Address     */
#define USART6_REGS                      ((usart_registers_t*)0x40040200)              /**< \brief USART6 Registers Address     */
#define USART7_REGS                      ((usart_registers_t*)0x40034200)              /**< \brief USART7 Registers Address     */
#define WDT_REGS                         ((wdt_registers_t*)0x400e1450)                /**< \brief WDT Registers Address        */

/* ************************************************************************** */
/*   BASE ADDRESS DEFINITIONS FOR SAMG55J19                                   */
/* ************************************************************************** */

#define ADC_BASE_ADDRESS                 (0x40038000UL)                                /**< \brief ADC Base Address             */
#define CHIPID_BASE_ADDRESS              (0x400e0740UL)                                /**< \brief CHIPID Base Address          */
#define CMCC_BASE_ADDRESS                (0x4003c000UL)                                /**< \brief CMCC Base Address            */
#define CRCCU_BASE_ADDRESS               (0x40048000UL)                                /**< \brief CRCCU Base Address           */
#define EFC_BASE_ADDRESS                 (0x400e0a00UL)                                /**< \brief EFC Base Address             */
#define FLEXCOM0_BASE_ADDRESS            (0x4000c000UL)                                /**< \brief FLEXCOM0 Base Address        */
#define FLEXCOM1_BASE_ADDRESS            (0x40020000UL)                                /**< \brief FLEXCOM1 Base Address        */
#define FLEXCOM2_BASE_ADDRESS            (0x40024000UL)                                /**< \brief FLEXCOM2 Base Address        */
#define FLEXCOM3_BASE_ADDRESS            (0x40018000UL)                                /**< \brief FLEXCOM3 Base Address        */
#define FLEXCOM4_BASE_ADDRESS            (0x4001c000UL)                                /**< \brief FLEXCOM4 Base Address        */
#define FLEXCOM5_BASE_ADDRESS            (0x40008000UL)                                /**< \brief FLEXCOM5 Base Address        */
#define FLEXCOM6_BASE_ADDRESS            (0x40040000UL)                                /**< \brief FLEXCOM6 Base Address        */
#define FLEXCOM7_BASE_ADDRESS            (0x40034000UL)                                /**< \brief FLEXCOM7 Base Address        */
#define GPBR_BASE_ADDRESS                (0x400e1490UL)                                /**< \brief GPBR Base Address            */
#define I2SC0_BASE_ADDRESS               (0x40000000UL)                                /**< \brief I2SC0 Base Address           */
#define I2SC1_BASE_ADDRESS               (0x40004000UL)                                /**< \brief I2SC1 Base Address           */
#define MATRIX_BASE_ADDRESS              (0x400e0200UL)                                /**< \brief MATRIX Base Address          */
#define MEM2MEM_BASE_ADDRESS             (0x40028000UL)                                /**< \brief MEM2MEM Base Address         */
#define PDMIC0_BASE_ADDRESS              (0x4002c000UL)                                /**< \brief PDMIC0 Base Address          */
#define PDMIC1_BASE_ADDRESS              (0x40030000UL)                                /**< \brief PDMIC1 Base Address          */
#define PIOA_BASE_ADDRESS                (0x400e0e00UL)                                /**< \brief PIOA Base Address            */
#define PIOB_BASE_ADDRESS                (0x400e1000UL)                                /**< \brief PIOB Base Address            */
#define PMC_BASE_ADDRESS                 (0x400e0400UL)                                /**< \brief PMC Base Address             */
#define RSTC_BASE_ADDRESS                (0x400e1400UL)                                /**< \brief RSTC Base Address            */
#define RTC_BASE_ADDRESS                 (0x400e1460UL)                                /**< \brief RTC Base Address             */
#define RTT_BASE_ADDRESS                 (0x400e1430UL)                                /**< \brief RTT Base Address             */
#define SPI0_BASE_ADDRESS                (0x4000c400UL)                                /**< \brief SPI0 Base Address            */
#define SPI1_BASE_ADDRESS                (0x40020400UL)                                /**< \brief SPI1 Base Address            */
#define SPI2_BASE_ADDRESS                (0x40024400UL)                                /**< \brief SPI2 Base Address            */
#define SPI3_BASE_ADDRESS                (0x40018400UL)                                /**< \brief SPI3 Base Address            */
#define SPI4_BASE_ADDRESS                (0x4001c400UL)                                /**< \brief SPI4 Base Address            */
#define SPI5_BASE_ADDRESS                (0x40008400UL)                                /**< \brief SPI5 Base Address            */
#define SPI6_BASE_ADDRESS                (0x40040400UL)                                /**< \brief SPI6 Base Address            */
#define SPI7_BASE_ADDRESS                (0x40034400UL)                                /**< \brief SPI7 Base Address            */
#define SUPC_BASE_ADDRESS                (0x400e1410UL)                                /**< \brief SUPC Base Address            */
#define TC0_BASE_ADDRESS                 (0x40010000UL)                                /**< \brief TC0 Base Address             */
#define TC1_BASE_ADDRESS                 (0x40014000UL)                                /**< \brief TC1 Base Address             */
#define TWI0_BASE_ADDRESS                (0x4000c600UL)                                /**< \brief TWI0 Base Address            */
#define TWI1_BASE_ADDRESS                (0x40020600UL)                                /**< \brief TWI1 Base Address            */
#define TWI2_BASE_ADDRESS                (0x40024600UL)                                /**< \brief TWI2 Base Address            */
#define TWI3_BASE_ADDRESS                (0x40018600UL)                                /**< \brief TWI3 Base Address            */
#define TWI4_BASE_ADDRESS                (0x4001c600UL)                                /**< \brief TWI4 Base Address            */
#define TWI5_BASE_ADDRESS                (0x40008600UL)                                /**< \brief TWI5 Base Address            */
#define TWI6_BASE_ADDRESS                (0x40040600UL)                                /**< \brief TWI6 Base Address            */
#define TWI7_BASE_ADDRESS                (0x40034600UL)                                /**< \brief TWI7 Base Address            */
#define UDP_BASE_ADDRESS                 (0x40044000UL)                                /**< \brief UDP Base Address             */
#define UHP_BASE_ADDRESS                 (0x4004c000UL)                                /**< \brief UHP Base Address             */
#define USART0_BASE_ADDRESS              (0x4000c200UL)                                /**< \brief USART0 Base Address          */
#define USART1_BASE_ADDRESS              (0x40020200UL)                                /**< \brief USART1 Base Address          */
#define USART2_BASE_ADDRESS              (0x40024200UL)                                /**< \brief USART2 Base Address          */
#define USART3_BASE_ADDRESS              (0x40018200UL)                                /**< \brief USART3 Base Address          */
#define USART4_BASE_ADDRESS              (0x4001c200UL)                                /**< \brief USART4 Base Address          */
#define USART5_BASE_ADDRESS              (0x40008200UL)                                /**< \brief USART5 Base Address          */
#define USART6_BASE_ADDRESS              (0x40040200UL)                                /**< \brief USART6 Base Address          */
#define USART7_BASE_ADDRESS              (0x40034200UL)                                /**< \brief USART7 Base Address          */
#define WDT_BASE_ADDRESS                 (0x400e1450UL)                                /**< \brief WDT Base Address             */

/** \addtogroup SAMG55J19_pio Peripheral Pio Definitions
 *  @{
 */

/* ************************************************************************** */
/*   PIO DEFINITIONS FOR SAMG55J19                                            */
/* ************************************************************************** */
#include "pio/samg55j19.h"

/** @}  end of Peripheral Pio Definitions */

/* ************************************************************************** */
/*   MEMORY MAPPING DEFINITIONS FOR SAMG55J19                                 */
/* ************************************************************************** */

#define PERIPHERALS_SIZE               (0x20000000UL)      /* 524288kB Memory segment type: io */
#define SYSTEM_SIZE                    (0x10000000UL)      /* 262144kB Memory segment type: io */
#define IFLASH_SIZE                    (0x00080000UL)      /*  512kB Memory segment type: flash */
#define IFLASH_PAGE_SIZE               (0x00000200UL)
#define IFLASH_NB_OF_PAGES             (0x00000400UL)
#define IROM_SIZE                      (0x00400000UL)      /* 4096kB Memory segment type: rom */
#define IRAM_SIZE                      (0x00028000UL)      /*  160kB Memory segment type: ram */
#define CMCC_SIZE                      (0x00004000UL)      /*   16kB Memory segment type: other */
#define PERIPHERALS_ADDR               (0x40000000UL)      /**< PERIPHERALS base address (type: io) */
#define SYSTEM_ADDR                    (0xe0000000UL)      /**< SYSTEM base address (type: io) */
#define IFLASH_ADDR                    (0x00400000UL)      /**< IFLASH base address (type: flash) */
#define IROM_ADDR                      (0x00800000UL)      /**< IROM base address (type: rom) */
#define IRAM_ADDR                      (0x20000000UL)      /**< IRAM base address (type: ram) */
#define CMCC_ADDR                      (0x1fc00000UL)      /**< CMCC base address (type: other) */

/* ************************************************************************** */
/**  DEVICE SIGNATURES FOR SAMG55J19                                          */
/* ************************************************************************** */
#define CHIP_JTAGID                    (0x05b3e03fUL)
#define CHIP_CIDR                      (0x24570ae0UL)
#define CHIP_EXID                      (0x00000000UL)

/* ************************************************************************** */
/**  ELECTRICAL DEFINITIONS FOR SAMG55J19                                     */
/* ************************************************************************** */
#define CHIP_FREQ_SLCK_RC_MIN               (20000UL)
#define CHIP_FREQ_SLCK_RC                   (32000UL)      /**< \brief Typical Slow Clock Internal RC frequency */
#define CHIP_FREQ_SLCK_RC_MAX               (44000UL)
#define CHIP_FREQ_MAINCK_RC_8MHZ          (8000000UL)
#define CHIP_FREQ_MAINCK_RC_16MHZ        (16000000UL)
#define CHIP_FREQ_MAINCK_RC_24MHZ        (24000000UL)
#define CHIP_FREQ_CPU_MAX               (120000000UL)
#define CHIP_FREQ_XTAL_32K                  (32768UL)
#define CHIP_FLASH_WRITE_WAIT_STATE             (8UL)      /**< \brief Embedded Flash Write Wait State */
#define CHIP_FREQ_FWS_0                  (14000000UL)      /**< \brief Maximum operating frequency when FWS is 0 */
#define CHIP_FREQ_FWS_1                  (28000000UL)      /**< \brief Maximum operating frequency when FWS is 1 */
#define CHIP_FREQ_FWS_2                  (42000000UL)      /**< \brief Maximum operating frequency when FWS is 2 */
#define CHIP_FREQ_FWS_3                  (56000000UL)      /**< \brief Maximum operating frequency when FWS is 3 */
#define CHIP_FREQ_FWS_4                  (70000000UL)      /**< \brief Maximum operating frequency when FWS is 4 */
#define CHIP_FREQ_FWS_5                  (84000000UL)      /**< \brief Maximum operating frequency when FWS is 5 */
#define CHIP_FREQ_FWS_6                  (96000000UL)      /**< \brief Maximum operating frequency when FWS is 6 */
#define CHIP_FREQ_FWS_7                 (108000000UL)      /**< \brief Maximum operating frequency when FWS is 7 */
#define CHIP_FREQ_FWS_8                 (120000000UL)      /**< \brief Maximum operating frequency when FWS is 8 */
#define CHIP_FREQ_FWS_NUMBER                    (9UL)      /**< \brief Number of FWS ranges */

#ifdef __cplusplus
}
#endif

/** @}  end of SAMG55J19 definitions */

#endif /* SAMG55J19_H */

