/**
 * \brief Component description for CoreDebug
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
#ifndef _SAML10_CoreDebug_COMPONENT_H_
#define _SAML10_CoreDebug_COMPONENT_H_

/* ************************************************************************** */
/*   SOFTWARE API DEFINITION FOR CoreDebug                                    */
/* ************************************************************************** */

/* -------- CoreDebug_DHCSR : (CoreDebug Offset: 0x00) (R/W 32) Debug Halting Control and Status Register -------- */
#define CoreDebug_DHCSR_C_DEBUGEN_Pos         _U_(0)                                         /**< (CoreDebug_DHCSR) Enable Halting debug Position */
#define CoreDebug_DHCSR_C_DEBUGEN_Msk         (_U_(0x1) << CoreDebug_DHCSR_C_DEBUGEN_Pos)    /**< (CoreDebug_DHCSR) Enable Halting debug Mask */
#define CoreDebug_DHCSR_C_HALT_Pos            _U_(1)                                         /**< (CoreDebug_DHCSR) Halt processor Position */
#define CoreDebug_DHCSR_C_HALT_Msk            (_U_(0x1) << CoreDebug_DHCSR_C_HALT_Pos)       /**< (CoreDebug_DHCSR) Halt processor Mask */
#define CoreDebug_DHCSR_C_STEP_Pos            _U_(2)                                         /**< (CoreDebug_DHCSR) Enable single step Position */
#define CoreDebug_DHCSR_C_STEP_Msk            (_U_(0x1) << CoreDebug_DHCSR_C_STEP_Pos)       /**< (CoreDebug_DHCSR) Enable single step Mask */
#define CoreDebug_DHCSR_C_MASKINTS_Pos        _U_(3)                                         /**< (CoreDebug_DHCSR) Mask PendSV, SysTick and external configurable interrupts Position */
#define CoreDebug_DHCSR_C_MASKINTS_Msk        (_U_(0x1) << CoreDebug_DHCSR_C_MASKINTS_Pos)   /**< (CoreDebug_DHCSR) Mask PendSV, SysTick and external configurable interrupts Mask */
#define CoreDebug_DHCSR_S_SNAPSTALL_Pos       _U_(5)                                         /**< (CoreDebug_DHCSR) Snap stall control Position */
#define CoreDebug_DHCSR_S_SNAPSTALL_Msk       (_U_(0x1) << CoreDebug_DHCSR_S_SNAPSTALL_Pos)  /**< (CoreDebug_DHCSR) Snap stall control Mask */
#define CoreDebug_DHCSR_S_REGRDY_Pos          _U_(16)                                        /**< (CoreDebug_DHCSR) Register ready status Position */
#define CoreDebug_DHCSR_S_REGRDY_Msk          (_U_(0x1) << CoreDebug_DHCSR_S_REGRDY_Pos)     /**< (CoreDebug_DHCSR) Register ready status Mask */
#define CoreDebug_DHCSR_S_HALT_Pos            _U_(17)                                        /**< (CoreDebug_DHCSR) Halted status Position */
#define CoreDebug_DHCSR_S_HALT_Msk            (_U_(0x1) << CoreDebug_DHCSR_S_HALT_Pos)       /**< (CoreDebug_DHCSR) Halted status Mask */
#define CoreDebug_DHCSR_S_SLEEP_Pos           _U_(18)                                        /**< (CoreDebug_DHCSR) Sleeping status Position */
#define CoreDebug_DHCSR_S_SLEEP_Msk           (_U_(0x1) << CoreDebug_DHCSR_S_SLEEP_Pos)      /**< (CoreDebug_DHCSR) Sleeping status Mask */
#define CoreDebug_DHCSR_S_LOCKUP_Pos          _U_(19)                                        /**< (CoreDebug_DHCSR) Lockup status Position */
#define CoreDebug_DHCSR_S_LOCKUP_Msk          (_U_(0x1) << CoreDebug_DHCSR_S_LOCKUP_Pos)     /**< (CoreDebug_DHCSR) Lockup status Mask */
#define CoreDebug_DHCSR_S_SDE_Pos             _U_(20)                                        /**< (CoreDebug_DHCSR) Secure debug enabled Position */
#define CoreDebug_DHCSR_S_SDE_Msk             (_U_(0x1) << CoreDebug_DHCSR_S_SDE_Pos)        /**< (CoreDebug_DHCSR) Secure debug enabled Mask */
#define CoreDebug_DHCSR_S_RETIRE_ST_Pos       _U_(24)                                        /**< (CoreDebug_DHCSR) Retire sticky status Position */
#define CoreDebug_DHCSR_S_RETIRE_ST_Msk       (_U_(0x1) << CoreDebug_DHCSR_S_RETIRE_ST_Pos)  /**< (CoreDebug_DHCSR) Retire sticky status Mask */
#define CoreDebug_DHCSR_S_RESET_ST_Pos        _U_(25)                                        /**< (CoreDebug_DHCSR) Reset sticky status Position */
#define CoreDebug_DHCSR_S_RESET_ST_Msk        (_U_(0x1) << CoreDebug_DHCSR_S_RESET_ST_Pos)   /**< (CoreDebug_DHCSR) Reset sticky status Mask */
#define CoreDebug_DHCSR_S_RESTART_ST_Pos      _U_(26)                                        /**< (CoreDebug_DHCSR) Restart sticky status Position */
#define CoreDebug_DHCSR_S_RESTART_ST_Msk      (_U_(0x1) << CoreDebug_DHCSR_S_RESTART_ST_Pos) /**< (CoreDebug_DHCSR) Restart sticky status Mask */
#define CoreDebug_DHCSR_Msk                   _U_(0x071F002F)                                /**< (CoreDebug_DHCSR) Register Mask  */


/* -------- CoreDebug_DCRSR : (CoreDebug Offset: 0x04) ( /W 32) Debug Core Register Select Register -------- */
#define CoreDebug_DCRSR_REGSEL_Pos            _U_(0)                                         /**< (CoreDebug_DCRSR) Register selector Position */
#define CoreDebug_DCRSR_REGSEL_Msk            (_U_(0x7F) << CoreDebug_DCRSR_REGSEL_Pos)      /**< (CoreDebug_DCRSR) Register selector Mask */
#define CoreDebug_DCRSR_REGSEL(value)         (CoreDebug_DCRSR_REGSEL_Msk & ((value) << CoreDebug_DCRSR_REGSEL_Pos))
#define CoreDebug_DCRSR_REGWnR_Pos            _U_(16)                                        /**< (CoreDebug_DCRSR) Register write/not-read access Position */
#define CoreDebug_DCRSR_REGWnR_Msk            (_U_(0x1) << CoreDebug_DCRSR_REGWnR_Pos)       /**< (CoreDebug_DCRSR) Register write/not-read access Mask */
#define CoreDebug_DCRSR_Msk                   _U_(0x0001007F)                                /**< (CoreDebug_DCRSR) Register Mask  */


/* -------- CoreDebug_DEMCR : (CoreDebug Offset: 0x0C) (R/W 32) Debug Exception and Monitor Control Register -------- */
#define CoreDebug_DEMCR_VC_CORERESET_Pos      _U_(0)                                         /**< (CoreDebug_DEMCR) Core reset Halting debug vector catch enable Position */
#define CoreDebug_DEMCR_VC_CORERESET_Msk      (_U_(0x1) << CoreDebug_DEMCR_VC_CORERESET_Pos) /**< (CoreDebug_DEMCR) Core reset Halting debug vector catch enable Mask */
#define CoreDebug_DEMCR_VC_MMERR_Pos          _U_(4)                                         /**< (CoreDebug_DEMCR) MemManage exception Halting debug vector catch enable Position */
#define CoreDebug_DEMCR_VC_MMERR_Msk          (_U_(0x1) << CoreDebug_DEMCR_VC_MMERR_Pos)     /**< (CoreDebug_DEMCR) MemManage exception Halting debug vector catch enable Mask */
#define CoreDebug_DEMCR_VC_NOCPERR_Pos        _U_(5)                                         /**< (CoreDebug_DEMCR) UsageFault exception coprocessor access Halting debug vector catch enable Position */
#define CoreDebug_DEMCR_VC_NOCPERR_Msk        (_U_(0x1) << CoreDebug_DEMCR_VC_NOCPERR_Pos)   /**< (CoreDebug_DEMCR) UsageFault exception coprocessor access Halting debug vector catch enable Mask */
#define CoreDebug_DEMCR_VC_CHKERR_Pos         _U_(6)                                         /**< (CoreDebug_DEMCR) UsageFault exception checking error Halting debug vector catch enable Position */
#define CoreDebug_DEMCR_VC_CHKERR_Msk         (_U_(0x1) << CoreDebug_DEMCR_VC_CHKERR_Pos)    /**< (CoreDebug_DEMCR) UsageFault exception checking error Halting debug vector catch enable Mask */
#define CoreDebug_DEMCR_VC_STATERR_Pos        _U_(7)                                         /**< (CoreDebug_DEMCR) UsageFault exception state information error Halting debug vector catch enable Position */
#define CoreDebug_DEMCR_VC_STATERR_Msk        (_U_(0x1) << CoreDebug_DEMCR_VC_STATERR_Pos)   /**< (CoreDebug_DEMCR) UsageFault exception state information error Halting debug vector catch enable Mask */
#define CoreDebug_DEMCR_VC_BUSERR_Pos         _U_(8)                                         /**< (CoreDebug_DEMCR) BusFault exception Halting debug vector catch enable Position */
#define CoreDebug_DEMCR_VC_BUSERR_Msk         (_U_(0x1) << CoreDebug_DEMCR_VC_BUSERR_Pos)    /**< (CoreDebug_DEMCR) BusFault exception Halting debug vector catch enable Mask */
#define CoreDebug_DEMCR_VC_INTERR_Pos         _U_(9)                                         /**< (CoreDebug_DEMCR) Excception entry and return faults Halting debug vector catch enable Position */
#define CoreDebug_DEMCR_VC_INTERR_Msk         (_U_(0x1) << CoreDebug_DEMCR_VC_INTERR_Pos)    /**< (CoreDebug_DEMCR) Excception entry and return faults Halting debug vector catch enable Mask */
#define CoreDebug_DEMCR_VC_HARDERR_Pos        _U_(10)                                        /**< (CoreDebug_DEMCR) HardFault exception Halting debug vector catch enable Position */
#define CoreDebug_DEMCR_VC_HARDERR_Msk        (_U_(0x1) << CoreDebug_DEMCR_VC_HARDERR_Pos)   /**< (CoreDebug_DEMCR) HardFault exception Halting debug vector catch enable Mask */
#define CoreDebug_DEMCR_VC_SFERR_Pos          _U_(11)                                        /**< (CoreDebug_DEMCR) SecureFault exception Halting debug vector catch enable Position */
#define CoreDebug_DEMCR_VC_SFERR_Msk          (_U_(0x1) << CoreDebug_DEMCR_VC_SFERR_Pos)     /**< (CoreDebug_DEMCR) SecureFault exception Halting debug vector catch enable Mask */
#define CoreDebug_DEMCR_MON_EN_Pos            _U_(16)                                        /**< (CoreDebug_DEMCR) DebugMonitor enable Position */
#define CoreDebug_DEMCR_MON_EN_Msk            (_U_(0x1) << CoreDebug_DEMCR_MON_EN_Pos)       /**< (CoreDebug_DEMCR) DebugMonitor enable Mask */
#define CoreDebug_DEMCR_MON_PEND_Pos          _U_(17)                                        /**< (CoreDebug_DEMCR) DebugMonitor pending state Position */
#define CoreDebug_DEMCR_MON_PEND_Msk          (_U_(0x1) << CoreDebug_DEMCR_MON_PEND_Pos)     /**< (CoreDebug_DEMCR) DebugMonitor pending state Mask */
#define CoreDebug_DEMCR_MON_STEP_Pos          _U_(18)                                        /**< (CoreDebug_DEMCR) Enable DebugMonitor stepping Position */
#define CoreDebug_DEMCR_MON_STEP_Msk          (_U_(0x1) << CoreDebug_DEMCR_MON_STEP_Pos)     /**< (CoreDebug_DEMCR) Enable DebugMonitor stepping Mask */
#define CoreDebug_DEMCR_MON_REQ_Pos           _U_(19)                                        /**< (CoreDebug_DEMCR) DebugMonitor semaphore bit Position */
#define CoreDebug_DEMCR_MON_REQ_Msk           (_U_(0x1) << CoreDebug_DEMCR_MON_REQ_Pos)      /**< (CoreDebug_DEMCR) DebugMonitor semaphore bit Mask */
#define CoreDebug_DEMCR_SDME_Pos              _U_(20)                                        /**< (CoreDebug_DEMCR) Secure DebugMonitor enable Position */
#define CoreDebug_DEMCR_SDME_Msk              (_U_(0x1) << CoreDebug_DEMCR_SDME_Pos)         /**< (CoreDebug_DEMCR) Secure DebugMonitor enable Mask */
#define CoreDebug_DEMCR_TRCENA_Pos            _U_(24)                                        /**< (CoreDebug_DEMCR) Global DWT and ITM features enable Position */
#define CoreDebug_DEMCR_TRCENA_Msk            (_U_(0x1) << CoreDebug_DEMCR_TRCENA_Pos)       /**< (CoreDebug_DEMCR) Global DWT and ITM features enable Mask */
#define CoreDebug_DEMCR_Msk                   _U_(0x011F0FF1)                                /**< (CoreDebug_DEMCR) Register Mask  */


/* -------- CoreDebug_DSCSR : (CoreDebug Offset: 0x18) (R/W 32) Debug Security Control and Status Register -------- */
#define CoreDebug_DSCSR_SBRSELEN_Pos          _U_(0)                                         /**< (CoreDebug_DSCSR) Secure Banked register select enable Position */
#define CoreDebug_DSCSR_SBRSELEN_Msk          (_U_(0x1) << CoreDebug_DSCSR_SBRSELEN_Pos)     /**< (CoreDebug_DSCSR) Secure Banked register select enable Mask */
#define CoreDebug_DSCSR_SBRSEL_Pos            _U_(1)                                         /**< (CoreDebug_DSCSR) Secure Banked register select Position */
#define CoreDebug_DSCSR_SBRSEL_Msk            (_U_(0x1) << CoreDebug_DSCSR_SBRSEL_Pos)       /**< (CoreDebug_DSCSR) Secure Banked register select Mask */
#define CoreDebug_DSCSR_CDS_Pos               _U_(16)                                        /**< (CoreDebug_DSCSR) Current domain Secure Position */
#define CoreDebug_DSCSR_CDS_Msk               (_U_(0x1) << CoreDebug_DSCSR_CDS_Pos)          /**< (CoreDebug_DSCSR) Current domain Secure Mask */
#define CoreDebug_DSCSR_CDSKEY_Pos            _U_(17)                                        /**< (CoreDebug_DSCSR) CDS field write-enable key Position */
#define CoreDebug_DSCSR_CDSKEY_Msk            (_U_(0x1) << CoreDebug_DSCSR_CDSKEY_Pos)       /**< (CoreDebug_DSCSR) CDS field write-enable key Mask */
#define CoreDebug_DSCSR_Msk                   _U_(0x00030003)                                /**< (CoreDebug_DSCSR) Register Mask  */


/** \brief CoreDebug register offsets definitions */
#define CoreDebug_DHCSR_REG_OFST       (0x00)         /**< (CoreDebug_DHCSR) Debug Halting Control and Status Register Offset */
#define CoreDebug_DCRSR_REG_OFST       (0x04)         /**< (CoreDebug_DCRSR) Debug Core Register Select Register Offset */
#define CoreDebug_DEMCR_REG_OFST       (0x0C)         /**< (CoreDebug_DEMCR) Debug Exception and Monitor Control Register Offset */
#define CoreDebug_DSCSR_REG_OFST       (0x18)         /**< (CoreDebug_DSCSR) Debug Security Control and Status Register Offset */

#if !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__))
/** \brief CoreDebug register API structure */
typedef struct
{  /* Debug Control Block */
  __IO  uint32_t                       CoreDebug_DHCSR; /**< Offset: 0x00 (R/W  32) Debug Halting Control and Status Register */
  __O   uint32_t                       CoreDebug_DCRSR; /**< Offset: 0x04 ( /W  32) Debug Core Register Select Register */
  __I   uint8_t                        Reserved1[0x04];
  __IO  uint32_t                       CoreDebug_DEMCR; /**< Offset: 0x0C (R/W  32) Debug Exception and Monitor Control Register */
  __I   uint8_t                        Reserved2[0x08];
  __IO  uint32_t                       CoreDebug_DSCSR; /**< Offset: 0x18 (R/W  32) Debug Security Control and Status Register */
} coredebug_registers_t;


#endif /* !(defined(__ASSEMBLER__) || defined(__IAR_SYSTEMS_ASM__)) */
#endif /* _SAML10_CoreDebug_COMPONENT_H_ */
