/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/

        MODULE  ?cstartup

        ;; Forward declaration of sections.
        SECTION IRQ_STACK:DATA:NOROOT(2)
        SECTION FIQ_STACK:DATA:NOROOT(2)
        SECTION ABT_STACK:DATA:NOROOT(2)
        SECTION UND_STACK:DATA:NOROOT(2)
        SECTION SVC_STACK:DATA:NOROOT(3)
        SECTION CSTACK:DATA:NOROOT(3)

//------------------------------------------------------------------------------
//         Headers
//------------------------------------------------------------------------------

#define __ASSEMBLY__

//------------------------------------------------------------------------------
//         Definitions
//------------------------------------------------------------------------------

GICD_BASE       DEFINE 0xE8C11000
GICC_BASE       DEFINE 0xE8C12000
GICC_IAR        DEFINE 0x0C
GICC_EOIR       DEFINE 0x10

MODE_MSK        DEFINE 0x1F  ; Bit mask for mode bits in CPSR

ARM_MODE_ABT    DEFINE 0x17
ARM_MODE_FIQ    DEFINE 0x11
ARM_MODE_IRQ    DEFINE 0x12
ARM_MODE_SVC    DEFINE 0x13
ARM_MODE_SYS    DEFINE 0x1F
ARM_MODE_UND    DEFINE 0x1B

I_BIT           DEFINE 0x80
F_BIT           DEFINE 0x40

ICACHE_BIT      DEFINE 0x1000
DCACHE_BIT      DEFINE 0x04
MMU_BIT         DEFINE 0x01

SRAM_BASE       DEFINE 0x00100000

//------------------------------------------------------------------------------
//         Startup routine
//------------------------------------------------------------------------------

        SECTION .vectors:CODE:NOROOT(2)

        PUBLIC  _reset_vector
        PUBLIC  __iar_program_start
        PUBWEAK  irqHandler
        PUBLIC  fiqHandler

        EXTERN  undefined_instruction_irq_handler
        EXTERN  prefetch_abort_irq_handler
        EXTERN  data_abort_irq_handler
        EXTERN  software_interrupt_irq_handler
        <#if USE_FREERTOS_VECTORS>
        EXTERN FreeRTOS_IRQ_Handler
        EXTERN FreeRTOS_SWI_Handler
        </#if>
        <#if USE_THREADX_VECTORS>
        EXTERN ThreadX_IRQ_Handler
        </#if>
        EXTERN GIC_IRQHandler
        EXTERN GIC_FIQHandler


        DATA

__iar_init$$done:               ; The vector table is not needed
                                ; until after copy initialization is done

_reset_vector:                  ; Make this a DATA label, so that stack usage
                                ; analysis doesn't consider it an uncalled fun

        ARM

        ldr     pc, reset_addr          ; 0x0 Reset
        ldr     pc, undefined_addr      ; 0x4 Undefined instructions
        ldr     pc, soft_int_addr       ; 0x8 Software interrupt (SWI/SVC)
        ldr     pc, prefetch_abt_addr   ; 0xc Prefetch abort
        ldr     pc, data_abt_addr       ; 0x10 Data abort
        DCD     0                       ; 0x14 RESERVED
        ldr     pc, irq_addr            ; 0x18 IRQ
        ldr     pc, fiq_addr            ; 0x1c FIQ

        DATA

; All default handlers (except reset, irq and fiq) are
; defined as weak symbol definitions.
; If a handler is defined by the application it will take precedence.
reset_addr:        DCD   __iar_program_start
undefined_addr:    DCD   undefined_instruction_irq_handler
<#if USE_FREERTOS_VECTORS>
soft_int_addr:     DCD   FreeRTOS_SWI_Handler
<#else>
soft_int_addr:     DCD   software_interrupt_irq_handler
</#if>
prefetch_abt_addr: DCD   prefetch_abort_irq_handler
data_abt_addr:     DCD   data_abort_irq_handler
<#if USE_FREERTOS_VECTORS>
irq_addr:          DCD   FreeRTOS_IRQ_Handler
<#elseif USE_THREADX_VECTORS>
irq_addr:          DCD   ThreadX_IRQ_Handler
<#else>
irq_addr:          DCD   irqHandler
</#if>
fiq_addr:          DCD   fiqHandler

;------------------------------------------------------------------------------
; Handles a fast interrupt request by branching to the address defined in the
; GIC.
;------------------------------------------------------------------------------
        SECTION .text:CODE:NOROOT(2)
        ARM
fiqHandler:
    ; Return to the interrupted instruction
    sub     lr, lr, #4

    ; Push the return address and SPSR
    push    {lr}
    mrs    lr, SPSR
    push    {lr}

    ; Change to supervisor mode to allow reentry
    cps     #ARM_MODE_SVC

    ; Push used registers
    push    {r0-r4, r12}

    ; Acknowledge the interrupt and get the interrupt ID
    ldr     r1, =GICC_BASE
    ldr     r0, [r1, #GICC_IAR]
    
    ; synchronize access upto this point
    dsb

    ; save r0(we need its value to mark EOI) and lr
    push    {r0, lr}
    
    ;Jump to Handler
    ldr    r1, =GIC_FIQHandler
    blx    r1
    
    ;Pop back r0 and lr
    pop    {r0, lr}

    ;disable interrupt if enabled by the IRQ handler
    cpsid    i

    ; Write the value read from ICCIAR to ICCEOIR
    ldr    r1, =GICC_BASE
    STR    r0, [r1, #GICC_EOIR]

    ;Restore used registers
    pop    {r0-r4, r12}
    
    ; Switch back to IRQ mode
    cps    #ARM_MODE_FIQ
    
    ; Restore SPSR and lr_IRQ before returning
    pop    {lr}
    msr    SPSR_cxsf, lr
    pop    {lr}
    movs    pc, lr


;------------------------------------------------------------------------------
; Handles incoming interrupt requests by branching to the corresponding
; handler, as defined in the AIC. Supports interrupt nesting.
;------------------------------------------------------------------------------
        SECTION .text:CODE:NOROOT(2)
        ARM
irqHandler:
    ; Return to the interrupted instruction
    sub     lr, lr, #4

    ; Push the return address and SPSR
    push    {lr}
    mrs    lr, SPSR
    push    {lr}

    ; Change to supervisor mode to allow reentry
    cps     #ARM_MODE_SVC

    ; Push used registers
    push    {r0-r4, r12}

    ; Acknowledge the interrupt and get the interrupt ID
    ldr     r1, =GICC_BASE
    ldr     r0, [r1, #GICC_IAR]
    
    ; synchronize access upto this point
    dsb

    ; save r0(we need its value to mark EOI) and lr
    push    {r0, lr}
    
    ;Jump to Handler
    ldr    r1, =GIC_IRQHandler
    blx    r1
    
    ;Pop back r0 and lr
    pop    {r0, lr}

    ;Disable interrupt if enabled by the IRQ handler
    cpsid    i

    ; Write the value read from ICCIAR to ICCEOIR
    ldr    r1, =GICC_BASE
    STR    r0, [r1, #GICC_EOIR]

    ;Restore used registers
    pop    {r0-r4, r12}
    
    ; Switch back to IRQ mode
    cps    #ARM_MODE_IRQ
    
    ; Restore SPSR and lr_IRQ before returning
    pop    {lr}
    msr    SPSR_cxsf, lr
    pop    {lr}
    movs    pc, lr

//------------------------------------------------------------------------------
/// Initializes the chip and branches to the main() function.
//------------------------------------------------------------------------------

        SECTION .cstartup:CODE:NOROOT(2)
        PUBLIC  __iar_program_start
        EXTERN  main
        REQUIRE _reset_vector

        EXTWEAK __iar_data_init3
        EXTWEAK __iar_init_core
        EXTWEAK __iar_init_vfp
        EXTWEAK __iar_argc_argv

        ARM

        /* Dummy vector table for ROM-code for cases when the real vector table
         * is relocated (QSPI-XIP) */
        ldr     pc, =__iar_program_start
        ldr     pc, =__iar_program_start
        ldr     pc, =__iar_program_start
        ldr     pc, =__iar_program_start
        ldr     pc, =__iar_program_start
        DCD     0
        ldr     pc, =__iar_program_start
        ldr     pc, =__iar_program_start

__iar_program_start:
?cstartup:

        ; Set up the fast interrupt stack pointer

        mrs     r0, CPSR
        bic     r0, r0, #MODE_MSK
        orr     r0, r0, #ARM_MODE_FIQ
        msr     cpsr_c, r0
        ldr     sp, =SFE(FIQ_STACK)
        bic     sp, sp, #0x7

        ; Set up the normal interrupt stack pointer

        bic     r0, r0, #MODE_MSK
        orr     r0, r0, #ARM_MODE_IRQ
        msr     CPSR_c, r0
        ldr     sp, =SFE(IRQ_STACK)
        bic     sp, sp, #0x7

        ; Set up the abort mode stack pointer

        bic     r0, r0, #MODE_MSK
        orr     r0, r0, #ARM_MODE_ABT
        msr     CPSR_c, r0
        ldr     sp, =SFE(ABT_STACK)
        bic     sp, sp, #0x7

        ; Set up the undefined mode stack pointer

        bic     r0, r0, #MODE_MSK
        orr     r0, r0, #ARM_MODE_UND
        msr     CPSR_c, r0
        ldr     sp, =SFE(UND_STACK)
        bic     sp, sp, #0x7

        ; Set up the user/system mode stack pointer

        bic     r0, r0, #MODE_MSK
        orr     r0, r0, #ARM_MODE_SYS
        msr     CPSR_c, r0
        ldr     sp, =SFE(CSTACK)
        bic     sp, sp, #0x7

        ; Set up the supervisor mode stack pointer

        bic     r0 ,r0, #MODE_MSK
        orr     r0 ,r0, #ARM_MODE_SVC
        msr     cpsr_c, r0
        ldr     sp, =SFE(SVC_STACK)
        bic     sp, sp, #0x7

        ; Execute relocations & zero BSS

        FUNCALL __iar_program_start, __iar_data_init3
        bl      __iar_data_init3

        ; Iinvalidate I Cache

        mov     r0, #0
        mcr     p15, 0, r0, c7, c5, 0

        ; Configure VBAR for the reset vectors to be at the start of SRAM

        mov	    r2, #SRAM_BASE
        mcr	    p15, 0, r2, c12, c0, 0

        ; Turn on core features assumed to be enabled

        FUNCALL __iar_program_start, __iar_init_core
        bl      __iar_init_core

        ; Initialize VFP (if needed)

        FUNCALL __iar_program_start, __iar_init_vfp
        bl      __iar_init_vfp

        ; Setup command line

        mov     r0, #0
        FUNCALL __iar_program_start, __iar_argc_argv
        bl      __iar_argc_argv

        ; Call main()

        FUNCALL __iar_program_start, main
        bl      main

       ;; Loop indefinitely when program is finished
loop4:  b       loop4

        END
