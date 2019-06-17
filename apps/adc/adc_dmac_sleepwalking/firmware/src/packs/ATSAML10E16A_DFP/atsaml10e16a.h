/**
 * \brief Header file for ATSAML10E16A
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
#ifndef _SAML10E16A_H_
#define _SAML10E16A_H_

// Header version uses Semantic Versioning 2.0.0 (https://semver.org/)
#define HEADER_FORMAT_VERSION "2.0.0"

#define HEADER_FORMAT_VERSION_MAJOR (2)
#define HEADER_FORMAT_VERSION_MINOR (0)

/** \addtogroup SAML10E16A_definitions SAML10E16A definitions
  This file defines all structures and symbols for SAML10E16A:
    - registers and bitfields
    - peripheral base address
    - peripheral ID
    - PIO definitions
 *  @{
 */

#ifdef __cplusplus
 extern "C" {
#endif

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
#  include <stdint.h>
#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */

#if !defined(SKIP_INTEGER_LITERALS)
#  if defined(_U_) || defined(_L_) || defined(_UL_)
#    error "Integer Literals macros already defined elsewhere"
#  endif

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/* Macros that deal with adding suffixes to integer literal constants for C/C++ */
#  define _U_(x) (x ## U)    /**< C code: Unsigned integer literal constant value */
#  define _L_(x) (x ## L)    /**< C code: Long integer literal constant value */
#  define _UL_(x) (x ## UL)  /**< C code: Unsigned Long integer literal constant value */

#else /* Assembler */

#  define _U_(x) x    /**< Assembler: Unsigned integer literal constant value */
#  define _L_(x) x    /**< Assembler: Long integer literal constant value */
#  define _UL_(x) x   /**< Assembler: Unsigned Long integer literal constant value */
#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* SKIP_INTEGER_LITERALS */
/** @}  end of Atmel Global Defines */

/* ************************************************************************** */
/*   CMSIS DEFINITIONS FOR SAML10E16A                                         */
/* ************************************************************************** */
#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** Interrupt Number Definition */
typedef enum IRQn
{
/******  CORTEX-M23 Processor Exceptions Numbers ******************************/
  Reset_IRQn                = -15, /**< -15 Reset Vector, invoked on Power up and warm reset */
  NonMaskableInt_IRQn       = -14, /**< -14 Non maskable Interrupt, cannot be stopped or preempted */
  HardFault_IRQn            = -13, /**< -13 Hard Fault, all classes of Fault    */
  SVCall_IRQn               =  -5, /**< -5  System Service Call via SVC instruction */
  PendSV_IRQn               =  -2, /**< -2  Pendable request for system service */
  SysTick_IRQn              =  -1, /**< -1  System Tick Timer                   */
/******  SAML10E16A specific Interrupt Numbers ***********************************/
  MCLK_IRQn                 =   0, /**< 0   Shared between MCLK OSCCTRL OSC32KCTRL PM SUPC (MCLK) */
  OSCCTRL_IRQn              =   0, /**< 0   Shared between MCLK OSCCTRL OSC32KCTRL PM SUPC (OSCCTRL) */
  OSC32KCTRL_IRQn           =   0, /**< 0   Shared between MCLK OSCCTRL OSC32KCTRL PM SUPC (OSC32KCTRL) */
  PM_IRQn                   =   0, /**< 0   Shared between MCLK OSCCTRL OSC32KCTRL PM SUPC (PM) */
  SUPC_IRQn                 =   0, /**< 0   Shared between MCLK OSCCTRL OSC32KCTRL PM SUPC (SUPC) */
  WDT_IRQn                  =   1, /**< 1   Watchdog Timer (WDT)                */
  RTC_IRQn                  =   2, /**< 2   Real-Time Counter (RTC)             */
  EIC_0_IRQn                =   3, /**< 3   External Interrupt Controller (EIC) */
  EIC_1_IRQn                =   4, /**< 4   External Interrupt Controller (EIC) */
  EIC_2_IRQn                =   5, /**< 5   External Interrupt Controller (EIC) */
  EIC_3_IRQn                =   6, /**< 6   External Interrupt Controller (EIC) */
  EIC_OTHER_IRQn            =   7, /**< 7   External Interrupt Controller (EIC) */
  FREQM_IRQn                =   8, /**< 8   Frequency Meter (FREQM)             */
  NVMCTRL_IRQn              =   9, /**< 9   Non-Volatile Memory Controller (NVMCTRL) */
  PORT_IRQn                 =  10, /**< 10  Port Module (PORT)                  */
  DMAC_0_IRQn               =  11, /**< 11  Direct Memory Access Controller (DMAC) */
  DMAC_1_IRQn               =  12, /**< 12  Direct Memory Access Controller (DMAC) */
  DMAC_2_IRQn               =  13, /**< 13  Direct Memory Access Controller (DMAC) */
  DMAC_3_IRQn               =  14, /**< 14  Direct Memory Access Controller (DMAC) */
  DMAC_OTHER_IRQn           =  15, /**< 15  Direct Memory Access Controller (DMAC) */
  EVSYS_0_IRQn              =  16, /**< 16  Event System Interface (EVSYS)      */
  EVSYS_1_IRQn              =  17, /**< 17  Event System Interface (EVSYS)      */
  EVSYS_2_IRQn              =  18, /**< 18  Event System Interface (EVSYS)      */
  EVSYS_3_IRQn              =  19, /**< 19  Event System Interface (EVSYS)      */
  EVSYS_NSCHK_IRQn          =  20, /**< 20  Event System Interface (EVSYS)      */
  PAC_IRQn                  =  21, /**< 21  Peripheral Access Controller (PAC)  */
  SERCOM0_0_IRQn            =  22, /**< 22  Serial Communication Interface (SERCOM0) */
  SERCOM0_1_IRQn            =  23, /**< 23  Serial Communication Interface (SERCOM0) */
  SERCOM0_2_IRQn            =  24, /**< 24  Serial Communication Interface (SERCOM0) */
  SERCOM0_OTHER_IRQn        =  25, /**< 25  Serial Communication Interface (SERCOM0) */
  SERCOM1_0_IRQn            =  26, /**< 26  Serial Communication Interface (SERCOM1) */
  SERCOM1_1_IRQn            =  27, /**< 27  Serial Communication Interface (SERCOM1) */
  SERCOM1_2_IRQn            =  28, /**< 28  Serial Communication Interface (SERCOM1) */
  SERCOM1_OTHER_IRQn        =  29, /**< 29  Serial Communication Interface (SERCOM1) */
  SERCOM2_0_IRQn            =  30, /**< 30  Serial Communication Interface (SERCOM2) */
  SERCOM2_1_IRQn            =  31, /**< 31  Serial Communication Interface (SERCOM2) */
  SERCOM2_2_IRQn            =  32, /**< 32  Serial Communication Interface (SERCOM2) */
  SERCOM2_OTHER_IRQn        =  33, /**< 33  Serial Communication Interface (SERCOM2) */
  TC0_IRQn                  =  34, /**< 34  Basic Timer Counter (TC0)           */
  TC1_IRQn                  =  35, /**< 35  Basic Timer Counter (TC1)           */
  TC2_IRQn                  =  36, /**< 36  Basic Timer Counter (TC2)           */
  ADC_OTHER_IRQn            =  37, /**< 37  Analog Digital Converter (ADC)      */
  ADC_RESRDY_IRQn           =  38, /**< 38  Analog Digital Converter (ADC)      */
  AC_IRQn                   =  39, /**< 39  Analog Comparators (AC)             */
  DAC_UNDERRUN_A_IRQn       =  40, /**< 40  Digital Analog Converter (DAC)      */
  DAC_EMPTY_IRQn            =  41, /**< 41  Digital Analog Converter (DAC)      */
  PTC_IRQn                  =  42, /**< 42  Peripheral Touch Controller (PTC)   */
  TRNG_IRQn                 =  43, /**< 43  True Random Generator (TRNG)        */
  TRAM_IRQn                 =  44, /**< 44  TrustRAM (TRAM)                     */

  PERIPH_MAX_IRQn           =  44  /**< Max peripheral ID */
} IRQn_Type;
#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
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
  void* pfnSYSTEM_Handler;                       /*   0 System peripherals shared interrupt (MCLK OSCCTRL OSC32KCTRL PM SUPC) */
  void* pfnWDT_Handler;                          /*   1 Watchdog Timer (WDT) */
  void* pfnRTC_Handler;                          /*   2 Real-Time Counter (RTC) */
  void* pfnEIC_0_Handler;                        /*   3 External Interrupt Controller (EIC) */
  void* pfnEIC_1_Handler;                        /*   4 External Interrupt Controller (EIC) */
  void* pfnEIC_2_Handler;                        /*   5 External Interrupt Controller (EIC) */
  void* pfnEIC_3_Handler;                        /*   6 External Interrupt Controller (EIC) */
  void* pfnEIC_OTHER_Handler;                    /*   7 External Interrupt Controller (EIC) */
  void* pfnFREQM_Handler;                        /*   8 Frequency Meter (FREQM) */
  void* pfnNVMCTRL_Handler;                      /*   9 Non-Volatile Memory Controller (NVMCTRL) */
  void* pfnPORT_Handler;                         /*  10 Port Module (PORT) */
  void* pfnDMAC_0_Handler;                       /*  11 Direct Memory Access Controller (DMAC) */
  void* pfnDMAC_1_Handler;                       /*  12 Direct Memory Access Controller (DMAC) */
  void* pfnDMAC_2_Handler;                       /*  13 Direct Memory Access Controller (DMAC) */
  void* pfnDMAC_3_Handler;                       /*  14 Direct Memory Access Controller (DMAC) */
  void* pfnDMAC_OTHER_Handler;                   /*  15 Direct Memory Access Controller (DMAC) */
  void* pfnEVSYS_0_Handler;                      /*  16 Event System Interface (EVSYS) */
  void* pfnEVSYS_1_Handler;                      /*  17 Event System Interface (EVSYS) */
  void* pfnEVSYS_2_Handler;                      /*  18 Event System Interface (EVSYS) */
  void* pfnEVSYS_3_Handler;                      /*  19 Event System Interface (EVSYS) */
  void* pfnEVSYS_NSCHK_Handler;                  /*  20 Event System Interface (EVSYS) */
  void* pfnPAC_Handler;                          /*  21 Peripheral Access Controller (PAC) */
  void* pfnSERCOM0_0_Handler;                    /*  22 Serial Communication Interface (SERCOM0) */
  void* pfnSERCOM0_1_Handler;                    /*  23 Serial Communication Interface (SERCOM0) */
  void* pfnSERCOM0_2_Handler;                    /*  24 Serial Communication Interface (SERCOM0) */
  void* pfnSERCOM0_OTHER_Handler;                /*  25 Serial Communication Interface (SERCOM0) */
  void* pfnSERCOM1_0_Handler;                    /*  26 Serial Communication Interface (SERCOM1) */
  void* pfnSERCOM1_1_Handler;                    /*  27 Serial Communication Interface (SERCOM1) */
  void* pfnSERCOM1_2_Handler;                    /*  28 Serial Communication Interface (SERCOM1) */
  void* pfnSERCOM1_OTHER_Handler;                /*  29 Serial Communication Interface (SERCOM1) */
  void* pfnSERCOM2_0_Handler;                    /*  30 Serial Communication Interface (SERCOM2) */
  void* pfnSERCOM2_1_Handler;                    /*  31 Serial Communication Interface (SERCOM2) */
  void* pfnSERCOM2_2_Handler;                    /*  32 Serial Communication Interface (SERCOM2) */
  void* pfnSERCOM2_OTHER_Handler;                /*  33 Serial Communication Interface (SERCOM2) */
  void* pfnTC0_Handler;                          /*  34 Basic Timer Counter (TC0) */
  void* pfnTC1_Handler;                          /*  35 Basic Timer Counter (TC1) */
  void* pfnTC2_Handler;                          /*  36 Basic Timer Counter (TC2) */
  void* pfnADC_OTHER_Handler;                    /*  37 Analog Digital Converter (ADC) */
  void* pfnADC_RESRDY_Handler;                   /*  38 Analog Digital Converter (ADC) */
  void* pfnAC_Handler;                           /*  39 Analog Comparators (AC) */
  void* pfnDAC_UNDERRUN_A_Handler;               /*  40 Digital Analog Converter (DAC) */
  void* pfnDAC_EMPTY_Handler;                    /*  41 Digital Analog Converter (DAC) */
  void* pfnPTC_Handler;                          /*  42 Peripheral Touch Controller (PTC) */
  void* pfnTRNG_Handler;                         /*  43 True Random Generator (TRNG) */
  void* pfnTRAM_Handler;                         /*  44 TrustRAM (TRAM) */
} DeviceVectors;

#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
#if !defined DONT_USE_PREDEFINED_CORE_HANDLERS
/* CORTEX-M23 exception handlers */
void Reset_Handler                 ( void );
void NonMaskableInt_Handler        ( void );
void HardFault_Handler             ( void );
void SVCall_Handler                ( void );
void PendSV_Handler                ( void );
void SysTick_Handler               ( void );
#endif /* DONT_USE_PREDEFINED_CORE_HANDLERS */

#if !defined DONT_USE_PREDEFINED_PERIPHERALS_HANDLERS
/* Peripherals interrupt handlers */
void SYSTEM_Handler                ( void );
void WDT_Handler                   ( void );
void RTC_Handler                   ( void );
void EIC_0_Handler                 ( void );
void EIC_1_Handler                 ( void );
void EIC_2_Handler                 ( void );
void EIC_3_Handler                 ( void );
void EIC_OTHER_Handler             ( void );
void FREQM_Handler                 ( void );
void NVMCTRL_Handler               ( void );
void PORT_Handler                  ( void );
void DMAC_0_Handler                ( void );
void DMAC_1_Handler                ( void );
void DMAC_2_Handler                ( void );
void DMAC_3_Handler                ( void );
void DMAC_OTHER_Handler            ( void );
void EVSYS_0_Handler               ( void );
void EVSYS_1_Handler               ( void );
void EVSYS_2_Handler               ( void );
void EVSYS_3_Handler               ( void );
void EVSYS_NSCHK_Handler           ( void );
void PAC_Handler                   ( void );
void SERCOM0_0_Handler             ( void );
void SERCOM0_1_Handler             ( void );
void SERCOM0_2_Handler             ( void );
void SERCOM0_OTHER_Handler         ( void );
void SERCOM1_0_Handler             ( void );
void SERCOM1_1_Handler             ( void );
void SERCOM1_2_Handler             ( void );
void SERCOM1_OTHER_Handler         ( void );
void SERCOM2_0_Handler             ( void );
void SERCOM2_1_Handler             ( void );
void SERCOM2_2_Handler             ( void );
void SERCOM2_OTHER_Handler         ( void );
void TC0_Handler                   ( void );
void TC1_Handler                   ( void );
void TC2_Handler                   ( void );
void ADC_OTHER_Handler             ( void );
void ADC_RESRDY_Handler            ( void );
void AC_Handler                    ( void );
void DAC_UNDERRUN_A_Handler        ( void );
void DAC_EMPTY_Handler             ( void );
void PTC_Handler                   ( void );
void TRNG_Handler                  ( void );
void TRAM_Handler                  ( void );
#endif /* DONT_USE_PREDEFINED_PERIPHERALS_HANDLERS */
#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */

/*
 * \brief Configuration of the CORTEX-M23 Processor and Core Peripherals
 */
#define __FPU_PRESENT                  0 /**< FPU present or not                                                        */
#define __MPU_PRESENT                  1 /**< MPU present or not                                                        */
#define __NVIC_PRIO_BITS               2 /**< Number of Bits used for Priority Levels                                   */
#define __VTOR_PRESENT                 1 /**< Vector Table Offset Register present or not                               */
#define __Vendor_SysTickConfig         0 /**< Set to 1 if different SysTick Config is used                              */
#define __ARCH_ARM                     1
#define __ARCH_ARM_CORTEX_M            1

/*
 * \brief CMSIS includes
 */
#include "core_cm23.h"
#if defined USE_CMSIS_INIT
#include "system_saml10.h"
#endif /* USE_CMSIS_INIT */

/** \defgroup SAML10E16A_api Peripheral Software API
 *  @{
 */

/* ************************************************************************** */
/**  SOFTWARE PERIPHERAL API DEFINITION FOR SAML10E16A                        */
/* ************************************************************************** */
#include "component/ac.h"
#include "component/adc.h"
#include "component/ccl.h"
#include "component/dac.h"
#include "component/dmac.h"
#include "component/dsu.h"
#include "component/eic.h"
#include "component/evsys.h"
#include "component/freqm.h"
#include "component/gclk.h"
#include "component/idau.h"
#include "component/mclk.h"
#include "component/nvmctrl.h"
#include "component/opamp.h"
#include "component/oscctrl.h"
#include "component/osc32kctrl.h"
#include "component/pac.h"
#include "component/pm.h"
#include "component/port.h"
#include "component/ptc.h"
#include "component/rstc.h"
#include "component/rtc.h"
#include "component/sercom.h"
#include "component/supc.h"
#include "component/tc.h"
#include "component/tram.h"
#include "component/trng.h"
#include "component/wdt.h"
/** @}  end of Peripheral Software API */

/** \addtogroup SAML10E16A_id Peripheral Ids Definitions
 *  @{
 */

/* ************************************************************************** */
/*  PERIPHERAL ID DEFINITIONS FOR SAML10E16A                                  */
/* ************************************************************************** */
#define ID_PAC           (  0) /**< \brief Peripheral Access Controller (PAC) */
#define ID_PM            (  1) /**< \brief Power Manager (PM) */
#define ID_MCLK          (  2) /**< \brief Main Clock (MCLK) */
#define ID_RSTC          (  3) /**< \brief Reset Controller (RSTC) */
#define ID_OSCCTRL       (  4) /**< \brief Oscillators Control (OSCCTRL) */
#define ID_OSC32KCTRL    (  5) /**< \brief 32k Oscillators Control (OSC32KCTRL) */
#define ID_SUPC          (  6) /**< \brief Supply Controller (SUPC) */
#define ID_GCLK          (  7) /**< \brief Generic Clock Generator (GCLK) */
#define ID_WDT           (  8) /**< \brief Watchdog Timer (WDT) */
#define ID_RTC           (  9) /**< \brief Real-Time Counter (RTC) */
#define ID_EIC           ( 10) /**< \brief External Interrupt Controller (EIC) */
#define ID_FREQM         ( 11) /**< \brief Frequency Meter (FREQM) */
#define ID_PORT          ( 12) /**< \brief Port Module (PORT) */
#define ID_AC            ( 13) /**< \brief Analog Comparators (AC) */
#define ID_IDAU          ( 32) /**< \brief Implementation Defined Attribution Unit (IDAU) */
#define ID_DSU           ( 33) /**< \brief Device Service Unit (DSU) */
#define ID_NVMCTRL       ( 34) /**< \brief Non-Volatile Memory Controller (NVMCTRL) */
#define ID_DMAC          ( 35) /**< \brief Direct Memory Access Controller (DMAC) */
#define ID_EVSYS         ( 64) /**< \brief Event System Interface (EVSYS) */
#define ID_SERCOM0       ( 65) /**< \brief Serial Communication Interface (SERCOM0) */
#define ID_SERCOM1       ( 66) /**< \brief Serial Communication Interface (SERCOM1) */
#define ID_SERCOM2       ( 67) /**< \brief Serial Communication Interface (SERCOM2) */
#define ID_TC0           ( 68) /**< \brief Basic Timer Counter (TC0) */
#define ID_TC1           ( 69) /**< \brief Basic Timer Counter (TC1) */
#define ID_TC2           ( 70) /**< \brief Basic Timer Counter (TC2) */
#define ID_ADC           ( 71) /**< \brief Analog Digital Converter (ADC) */
#define ID_DAC           ( 72) /**< \brief Digital Analog Converter (DAC) */
#define ID_PTC           ( 73) /**< \brief Peripheral Touch Controller (PTC) */
#define ID_TRNG          ( 74) /**< \brief True Random Generator (TRNG) */
#define ID_CCL           ( 75) /**< \brief Configurable Custom Logic (CCL) */
#define ID_OPAMP         ( 76) /**< \brief Operational Amplifier (OPAMP) */
#define ID_TRAM          ( 77) /**< \brief TrustRAM (TRAM) */

#define ID_PERIPH_MAX    ( 77) /**< \brief Number of peripheral IDs */
/** @}  end of Peripheral Ids Definitions */

/** \addtogroup SAML10E16A_base Peripheral Base Address Definitions
 *  @{
 */

/* ************************************************************************** */
/*   REGISTER STRUCTURE ADDRESS DEFINITIONS FOR SAML10E16A                    */
/* ************************************************************************** */
#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
#define AC_REGS                          ((ac_registers_t*)0x40003400)                 /**< \brief AC Registers Address         */
#define ADC_REGS                         ((adc_registers_t*)0x42001c00)                /**< \brief ADC Registers Address        */
#define CCL_REGS                         ((ccl_registers_t*)0x42002c00)                /**< \brief CCL Registers Address        */
#define DAC_REGS                         ((dac_registers_t*)0x42002000)                /**< \brief DAC Registers Address        */
#define DMAC_REGS                        ((dmac_registers_t*)0x41006000)               /**< \brief DMAC Registers Address       */
#define DSU_REGS                         ((dsu_registers_t*)0x41002000)                /**< \brief DSU Registers Address        */
#define DSU_EXT_REGS                     ((dsu_registers_t*)0x41002100)                /**< \brief DSU Registers Address        */
#define EIC_REGS                         ((eic_registers_t*)0x40002800)                /**< \brief EIC Registers Address        */
#define EVSYS_REGS                       ((evsys_registers_t*)0x42000000)              /**< \brief EVSYS Registers Address      */
#define FREQM_REGS                       ((freqm_registers_t*)0x40002c00)              /**< \brief FREQM Registers Address      */
#define GCLK_REGS                        ((gclk_registers_t*)0x40001c00)               /**< \brief GCLK Registers Address       */
#define IDAU_REGS                        ((idau_registers_t*)0x41000000)               /**< \brief IDAU Registers Address       */
#define MCLK_REGS                        ((mclk_registers_t*)0x40000800)               /**< \brief MCLK Registers Address       */
#define NVMCTRL_REGS                     ((nvmctrl_registers_t*)0x41004000)            /**< \brief NVMCTRL Registers Address    */
#define OPAMP_REGS                       ((opamp_registers_t*)0x42003000)              /**< \brief OPAMP Registers Address      */
#define OSCCTRL_REGS                     ((oscctrl_registers_t*)0x40001000)            /**< \brief OSCCTRL Registers Address    */
#define OSC32KCTRL_REGS                  ((osc32kctrl_registers_t*)0x40001400)         /**< \brief OSC32KCTRL Registers Address */
#define PAC_REGS                         ((pac_registers_t*)0x40000000)                /**< \brief PAC Registers Address        */
#define PM_REGS                          ((pm_registers_t*)0x40000400)                 /**< \brief PM Registers Address         */
#define PORT_REGS                        ((port_registers_t*)0x40003000)               /**< \brief PORT Registers Address       */
#define PORT_IOBUS_REGS                  ((port_registers_t*)0x60000000)               /**< \brief PORT Registers Address       */
#define PTC_REGS                         ((ptc_registers_t*)0x42002400)                /**< \brief PTC Registers Address        */
#define RSTC_REGS                        ((rstc_registers_t*)0x40000c00)               /**< \brief RSTC Registers Address       */
#define RTC_REGS                         ((rtc_registers_t*)0x40002400)                /**< \brief RTC Registers Address        */
#define SERCOM0_REGS                     ((sercom_registers_t*)0x42000400)             /**< \brief SERCOM0 Registers Address    */
#define SERCOM1_REGS                     ((sercom_registers_t*)0x42000800)             /**< \brief SERCOM1 Registers Address    */
#define SERCOM2_REGS                     ((sercom_registers_t*)0x42000c00)             /**< \brief SERCOM2 Registers Address    */
#define SUPC_REGS                        ((supc_registers_t*)0x40001800)               /**< \brief SUPC Registers Address       */
#define TC0_REGS                         ((tc_registers_t*)0x42001000)                 /**< \brief TC0 Registers Address        */
#define TC1_REGS                         ((tc_registers_t*)0x42001400)                 /**< \brief TC1 Registers Address        */
#define TC2_REGS                         ((tc_registers_t*)0x42001800)                 /**< \brief TC2 Registers Address        */
#define TRAM_REGS                        ((tram_registers_t*)0x42003400)               /**< \brief TRAM Registers Address       */
#define TRNG_REGS                        ((trng_registers_t*)0x42002800)               /**< \brief TRNG Registers Address       */
#define WDT_REGS                         ((wdt_registers_t*)0x40002000)                /**< \brief WDT Registers Address        */
#endif /* (defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
/** @}  end of Peripheral Base Address Definitions */

/** \addtogroup SAML10E16A_base Peripheral Base Address Definitions
 *  @{
 */

/* ************************************************************************** */
/*   BASE ADDRESS DEFINITIONS FOR SAML10E16A                                  */
/* ************************************************************************** */
#define AC_BASE_ADDRESS                  _UL_(0x40003400)                              /**< \brief AC Base Address */
#define ADC_BASE_ADDRESS                 _UL_(0x42001c00)                              /**< \brief ADC Base Address */
#define CCL_BASE_ADDRESS                 _UL_(0x42002c00)                              /**< \brief CCL Base Address */
#define DAC_BASE_ADDRESS                 _UL_(0x42002000)                              /**< \brief DAC Base Address */
#define DMAC_BASE_ADDRESS                _UL_(0x41006000)                              /**< \brief DMAC Base Address */
#define DSU_BASE_ADDRESS                 _UL_(0x41002000)                              /**< \brief DSU Base Address */
#define DSU_EXT_BASE_ADDRESS             _UL_(0x41002100)                              /**< \brief DSU Base Address */
#define EIC_BASE_ADDRESS                 _UL_(0x40002800)                              /**< \brief EIC Base Address */
#define EVSYS_BASE_ADDRESS               _UL_(0x42000000)                              /**< \brief EVSYS Base Address */
#define FREQM_BASE_ADDRESS               _UL_(0x40002c00)                              /**< \brief FREQM Base Address */
#define GCLK_BASE_ADDRESS                _UL_(0x40001c00)                              /**< \brief GCLK Base Address */
#define IDAU_BASE_ADDRESS                _UL_(0x41000000)                              /**< \brief IDAU Base Address */
#define MCLK_BASE_ADDRESS                _UL_(0x40000800)                              /**< \brief MCLK Base Address */
#define NVMCTRL_BASE_ADDRESS             _UL_(0x41004000)                              /**< \brief NVMCTRL Base Address */
#define OPAMP_BASE_ADDRESS               _UL_(0x42003000)                              /**< \brief OPAMP Base Address */
#define OSCCTRL_BASE_ADDRESS             _UL_(0x40001000)                              /**< \brief OSCCTRL Base Address */
#define OSC32KCTRL_BASE_ADDRESS          _UL_(0x40001400)                              /**< \brief OSC32KCTRL Base Address */
#define PAC_BASE_ADDRESS                 _UL_(0x40000000)                              /**< \brief PAC Base Address */
#define PM_BASE_ADDRESS                  _UL_(0x40000400)                              /**< \brief PM Base Address */
#define PORT_BASE_ADDRESS                _UL_(0x40003000)                              /**< \brief PORT Base Address */
#define PORT_IOBUS_BASE_ADDRESS          _UL_(0x60000000)                              /**< \brief PORT Base Address */
#define PTC_BASE_ADDRESS                 _UL_(0x42002400)                              /**< \brief PTC Base Address */
#define RSTC_BASE_ADDRESS                _UL_(0x40000c00)                              /**< \brief RSTC Base Address */
#define RTC_BASE_ADDRESS                 _UL_(0x40002400)                              /**< \brief RTC Base Address */
#define SERCOM0_BASE_ADDRESS             _UL_(0x42000400)                              /**< \brief SERCOM0 Base Address */
#define SERCOM1_BASE_ADDRESS             _UL_(0x42000800)                              /**< \brief SERCOM1 Base Address */
#define SERCOM2_BASE_ADDRESS             _UL_(0x42000c00)                              /**< \brief SERCOM2 Base Address */
#define SUPC_BASE_ADDRESS                _UL_(0x40001800)                              /**< \brief SUPC Base Address */
#define TC0_BASE_ADDRESS                 _UL_(0x42001000)                              /**< \brief TC0 Base Address */
#define TC1_BASE_ADDRESS                 _UL_(0x42001400)                              /**< \brief TC1 Base Address */
#define TC2_BASE_ADDRESS                 _UL_(0x42001800)                              /**< \brief TC2 Base Address */
#define TRAM_BASE_ADDRESS                _UL_(0x42003400)                              /**< \brief TRAM Base Address */
#define TRNG_BASE_ADDRESS                _UL_(0x42002800)                              /**< \brief TRNG Base Address */
#define WDT_BASE_ADDRESS                 _UL_(0x40002000)                              /**< \brief WDT Base Address */
/** @}  end of Peripheral Base Address Definitions */

/** \addtogroup SAML10E16A_pio Peripheral Pio Definitions
 *  @{
 */

/* ************************************************************************** */
/*   PIO DEFINITIONS FOR SAML10E16A                                           */
/* ************************************************************************** */
#include "pio/saml10e16a.h"
/** @}  end of Peripheral Pio Definitions */

/* ************************************************************************** */
/*   MEMORY MAPPING DEFINITIONS FOR SAML10E16A                                */
/* ************************************************************************** */

#define FLASH_SIZE                     _UL_(0x00010000)    /*   64kB Memory segment type: flash */
#define FLASH_PAGE_SIZE                _UL_(        64)
#define FLASH_NB_OF_PAGES              _UL_(      1024)

#define AUX_SIZE                       _UL_(0x00000100)    /*    0kB Memory segment type: fuses */
#define AUX_PAGE_SIZE                  _UL_(        64)
#define AUX_NB_OF_PAGES                _UL_(         4)

#define BOCOR_SIZE                     _UL_(0x00000100)    /*    0kB Memory segment type: fuses */
#define BOCOR_PAGE_SIZE                _UL_(        64)
#define BOCOR_NB_OF_PAGES              _UL_(         4)

#define DATAFLASH_SIZE                 _UL_(0x00000800)    /*    2kB Memory segment type: flash */
#define DATAFLASH_PAGE_SIZE            _UL_(        64)
#define DATAFLASH_NB_OF_PAGES          _UL_(        32)

#define SW_CALIB_SIZE                  _UL_(0x00000008)    /*    0kB Memory segment type: fuses */
#define TEMP_LOG_SIZE                  _UL_(0x00000008)    /*    0kB Memory segment type: fuses */
#define USER_PAGE_SIZE                 _UL_(0x00000100)    /*    0kB Memory segment type: user_page */
#define USER_PAGE_PAGE_SIZE            _UL_(        64)
#define USER_PAGE_NB_OF_PAGES          _UL_(         4)

#define HSRAM_SIZE                     _UL_(0x00004000)    /*   16kB Memory segment type: ram */
#define APBA_SIZE                      _UL_(0x00008000)    /*   32kB Memory segment type: io */
#define APBB_SIZE                      _UL_(0x00010000)    /*   64kB Memory segment type: io */
#define APBC_SIZE                      _UL_(0x00004000)    /*   16kB Memory segment type: io */
#define PPB_SIZE                       _UL_(0x00100000)    /* 1024kB Memory segment type: io */
#define SCS_SIZE                       _UL_(0x00001000)    /*    4kB Memory segment type: io */
#define PERIPHERALS_SIZE               _UL_(0x20000000)    /* 524288kB Memory segment type: io */

#define FLASH_ADDR                     _UL_(0x00000000)    /**< FLASH base address (type: flash)*/
#define AUX_ADDR                       _UL_(0x00806000)    /**< AUX base address (type: fuses)*/
#define BOCOR_ADDR                     _UL_(0x0080c000)    /**< BOCOR base address (type: fuses)*/
#define DATAFLASH_ADDR                 _UL_(0x00400000)    /**< DATAFLASH base address (type: flash)*/
#define SW_CALIB_ADDR                  _UL_(0x00806020)    /**< SW_CALIB base address (type: fuses)*/
#define TEMP_LOG_ADDR                  _UL_(0x00806038)    /**< TEMP_LOG base address (type: fuses)*/
#define USER_PAGE_ADDR                 _UL_(0x00804000)    /**< USER_PAGE base address (type: user_page)*/
#define HSRAM_ADDR                     _UL_(0x20000000)    /**< HSRAM base address (type: ram)*/
#define APBA_ADDR                      _UL_(0x40000000)    /**< APBA base address (type: io)*/
#define APBB_ADDR                      _UL_(0x41000000)    /**< APBB base address (type: io)*/
#define APBC_ADDR                      _UL_(0x42000000)    /**< APBC base address (type: io)*/
#define PPB_ADDR                       _UL_(0xe0000000)    /**< PPB base address (type: io)*/
#define SCS_ADDR                       _UL_(0xe000e000)    /**< SCS base address (type: io)*/
#define PERIPHERALS_ADDR               _UL_(0x40000000)    /**< PERIPHERALS base address (type: io)*/

/* ************************************************************************** */
/**  DEVICE SIGNATURES FOR SAML10E16A                                         */
/* ************************************************************************** */
#define DSU_DID                        _UL_(0X20840000)

/* ************************************************************************** */
/**  ELECTRICAL DEFINITIONS FOR SAML10E16A                                    */
/* ************************************************************************** */

/* ************************************************************************** */
/** Event Generator IDs for SAML10E16A */
/* ************************************************************************** */
#define EVENT_ID_GEN_OSCCTRL_CLKFAIL                      1 /**< ID for OSCCTRL event generator CLKFAIL */
#define EVENT_ID_GEN_OSC32KCTRL_CLKFAIL                   2 /**< ID for OSC32KCTRL event generator CLKFAIL */
#define EVENT_ID_GEN_SUPC_BOD33DET                        3 /**< ID for SUPC event generator BOD33DET */
#define EVENT_ID_GEN_RTC_PER_0                            4 /**< ID for RTC event generator PER_0 */
#define EVENT_ID_GEN_RTC_PER_1                            5 /**< ID for RTC event generator PER_1 */
#define EVENT_ID_GEN_RTC_PER_2                            6 /**< ID for RTC event generator PER_2 */
#define EVENT_ID_GEN_RTC_PER_3                            7 /**< ID for RTC event generator PER_3 */
#define EVENT_ID_GEN_RTC_PER_4                            8 /**< ID for RTC event generator PER_4 */
#define EVENT_ID_GEN_RTC_PER_5                            9 /**< ID for RTC event generator PER_5 */
#define EVENT_ID_GEN_RTC_PER_6                           10 /**< ID for RTC event generator PER_6 */
#define EVENT_ID_GEN_RTC_PER_7                           11 /**< ID for RTC event generator PER_7 */
#define EVENT_ID_GEN_RTC_ALARM_0                         12 /**< ID for RTC event generator ALARM_0 */
#define EVENT_ID_GEN_RTC_CMP_0                           12 /**< ID for RTC event generator CMP_0 */
#define EVENT_ID_GEN_RTC_CMP_1                           13 /**< ID for RTC event generator CMP_1 */
#define EVENT_ID_GEN_RTC_TAMPER                          14 /**< ID for RTC event generator TAMPER */
#define EVENT_ID_GEN_RTC_OVF                             15 /**< ID for RTC event generator OVF */
#define EVENT_ID_GEN_RTC_PERD                            16 /**< ID for RTC event generator PERD */
#define EVENT_ID_GEN_EIC_EXTINT_0                        17 /**< ID for EIC event generator EXTINT_0 */
#define EVENT_ID_GEN_EIC_EXTINT_1                        18 /**< ID for EIC event generator EXTINT_1 */
#define EVENT_ID_GEN_EIC_EXTINT_2                        19 /**< ID for EIC event generator EXTINT_2 */
#define EVENT_ID_GEN_EIC_EXTINT_3                        20 /**< ID for EIC event generator EXTINT_3 */
#define EVENT_ID_GEN_EIC_EXTINT_4                        21 /**< ID for EIC event generator EXTINT_4 */
#define EVENT_ID_GEN_EIC_EXTINT_5                        22 /**< ID for EIC event generator EXTINT_5 */
#define EVENT_ID_GEN_EIC_EXTINT_6                        23 /**< ID for EIC event generator EXTINT_6 */
#define EVENT_ID_GEN_EIC_EXTINT_7                        24 /**< ID for EIC event generator EXTINT_7 */
#define EVENT_ID_GEN_DMAC_CH_0                           25 /**< ID for DMAC event generator CH_0 */
#define EVENT_ID_GEN_DMAC_CH_1                           26 /**< ID for DMAC event generator CH_1 */
#define EVENT_ID_GEN_DMAC_CH_2                           27 /**< ID for DMAC event generator CH_2 */
#define EVENT_ID_GEN_DMAC_CH_3                           28 /**< ID for DMAC event generator CH_3 */
#define EVENT_ID_GEN_TC0_OVF                             29 /**< ID for TC0 event generator OVF */
#define EVENT_ID_GEN_TC0_MCX_0                           30 /**< ID for TC0 event generator MCX_0 */
#define EVENT_ID_GEN_TC0_MCX_1                           31 /**< ID for TC0 event generator MCX_1 */
#define EVENT_ID_GEN_TC1_OVF                             32 /**< ID for TC1 event generator OVF */
#define EVENT_ID_GEN_TC1_MCX_0                           33 /**< ID for TC1 event generator MCX_0 */
#define EVENT_ID_GEN_TC1_MCX_1                           34 /**< ID for TC1 event generator MCX_1 */
#define EVENT_ID_GEN_TC2_OVF                             35 /**< ID for TC2 event generator OVF */
#define EVENT_ID_GEN_TC2_MCX_0                           36 /**< ID for TC2 event generator MCX_0 */
#define EVENT_ID_GEN_TC2_MCX_1                           37 /**< ID for TC2 event generator MCX_1 */
#define EVENT_ID_GEN_ADC_RESRDY                          38 /**< ID for ADC event generator RESRDY */
#define EVENT_ID_GEN_ADC_WINMON                          39 /**< ID for ADC event generator WINMON */
#define EVENT_ID_GEN_AC_COMP_0                           40 /**< ID for AC event generator COMP_0 */
#define EVENT_ID_GEN_AC_COMP_1                           41 /**< ID for AC event generator COMP_1 */
#define EVENT_ID_GEN_AC_WIN_0                            42 /**< ID for AC event generator WIN_0 */
#define EVENT_ID_GEN_DAC_EMPTY                           43 /**< ID for DAC event generator EMPTY */
#define EVENT_ID_GEN_TRNG_DATARDY                        46 /**< ID for TRNG event generator DATARDY */
#define EVENT_ID_GEN_CCL_LUT_0                           47 /**< ID for CCL event generator LUT_0 */
#define EVENT_ID_GEN_CCL_LUT_1                           48 /**< ID for CCL event generator LUT_1 */
#define EVENT_ID_GEN_PAC_ERR                             49 /**< ID for PAC event generator ERR */

/* ************************************************************************** */
/** Event User IDs for SAML10E16A */
/* ************************************************************************** */
#define EVENT_ID_USER_OSCCTRL_TUNE                        0 /**< ID for OSCCTRL event user TUNE */
#define EVENT_ID_USER_RTC_TAMPEVT                         1 /**< ID for RTC event user TAMPEVT */
#define EVENT_ID_USER_NVMCTRL_AUTOW                       2 /**< ID for NVMCTRL event user AUTOW */
#define EVENT_ID_USER_PORT_EV_0                           3 /**< ID for PORT event user EV_0 */
#define EVENT_ID_USER_PORT_EV_1                           4 /**< ID for PORT event user EV_1 */
#define EVENT_ID_USER_PORT_EV_2                           5 /**< ID for PORT event user EV_2 */
#define EVENT_ID_USER_PORT_EV_3                           6 /**< ID for PORT event user EV_3 */
#define EVENT_ID_USER_DMAC_CH_0                           7 /**< ID for DMAC event user CH_0 */
#define EVENT_ID_USER_DMAC_CH_1                           8 /**< ID for DMAC event user CH_1 */
#define EVENT_ID_USER_DMAC_CH_2                           9 /**< ID for DMAC event user CH_2 */
#define EVENT_ID_USER_DMAC_CH_3                          10 /**< ID for DMAC event user CH_3 */
#define EVENT_ID_USER_TC0_EVU                            11 /**< ID for TC0 event user EVU */
#define EVENT_ID_USER_TC1_EVU                            12 /**< ID for TC1 event user EVU */
#define EVENT_ID_USER_TC2_EVU                            13 /**< ID for TC2 event user EVU */
#define EVENT_ID_USER_ADC_START                          14 /**< ID for ADC event user START */
#define EVENT_ID_USER_ADC_FLUSH                          15 /**< ID for ADC event user FLUSH */
#define EVENT_ID_USER_AC_COMP_0                          16 /**< ID for AC event user COMP_0 */
#define EVENT_ID_USER_AC_COMP_1                          17 /**< ID for AC event user COMP_1 */
#define EVENT_ID_USER_DAC_START                          18 /**< ID for DAC event user START */
#define EVENT_ID_USER_CCL_LUT_0                          21 /**< ID for CCL event user LUT_0 */
#define EVENT_ID_USER_CCL_LUT_1                          22 /**< ID for CCL event user LUT_1 */

#ifdef __cplusplus
}
#endif

/** @}  end of SAML10E16A definitions */


#endif /* _SAML10E16A_H_ */

