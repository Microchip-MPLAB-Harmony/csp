/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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


//------------------------------------------------------------------------------
//         Definitions
//------------------------------------------------------------------------------

#define GICD_BASE        0xE8C11000
#define GICC_BASE        0xE8C12000
#define GICC_IAR         0x0C
#define GICC_EOIR        0x10

#define MODE_MSK         0x1F

#define ARM_MODE_FIQ     0x11
#define ARM_MODE_IRQ     0x12
#define ARM_MODE_SVC     0x13
#define ARM_MODE_ABT     0x17
#define ARM_MODE_UND     0x1B
#define ARM_MODE_SYS     0x1F

#define I_BIT            0x80
#define F_BIT            0x40

#define FPU_NON_SECURE_ACCESS_OFFSET 10
#define FPU_ACCESS_CONTROL_OFFSET    20
#define FPU_FPEXC_EN_BIT             0x40000000

#define SRAM_BASE 0x00100000

//------------------------------------------------------------------------------
//         Startup routine
//------------------------------------------------------------------------------

	.align      4
	.arm

/* Exception vectors
 *******************/
	.section    .vectors, code

resetVector:
/* Reset */
	ldr     pc, =resetHandler
/* Undefined Instruction */
	ldr     pc, =undefined_instruction_irq_handler
/* Software Interrupt */
<#if USE_FREERTOS_VECTORS>
	ldr     pc, =FreeRTOS_SWI_Handler
<#else>
	ldr     pc, =software_interrupt_irq_handler
</#if>
/* Prefetch Abort */
	ldr     pc, =prefetch_abort_irq_handler
/* Data Abort */
	ldr     pc, =data_abort_irq_handler
/* Reserved for future use */
	.word   0
/* Interrupt */
<#if USE_FREERTOS_VECTORS>
	ldr     pc, =FreeRTOS_IRQ_Handler
<#elseif USE_THREADX_VECTORS>
	ldr     pc, =ThreadX_IRQ_Handler
<#else>
	ldr     pc, =irqHandler
</#if>
/* Fast interrupt */
	ldr     pc, =fiqHandler

	.section    .text, code

//------------------------------------------------------------------------------
/// Handles a fast interrupt request by branching to the address defined in the
/// GIC.
//------------------------------------------------------------------------------
fiqHandler:
    // Return to the interrupted instruction.
    sub     lr, lr, #4

    // Push the return address and SPSR
    push    {lr}
    mrs    lr, SPSR
    push    {lr}

    // Change to supervisor mode to allow reentry.
    cps     #ARM_MODE_SVC

    // Push used registers.
    push    {r0-r4, r12}

    // Acknowledge the interrupt and get the interrupt ID
    ldr     r1, =GICC_BASE
    ldr     r0, [r1, #GICC_IAR]

    // Synchronize access upto this point
    dsb

    // Save r0(we need its value to mark EOI) and lr
    push    {r0, lr}
    // Jump to Handler
    ldr    r1, =GIC_FIQHandler
    blx    r1
    // Pop back r0 and lr
    pop    {r0, lr}

    // Disable interrupt if enabled by the FIQ handler
    cpsid    i

    // Write the value read from ICCIAR to ICCEOIR
    ldr    r1, =GICC_BASE
    STR    r0, [r1, #GICC_EOIR]

    // Restore used registers
    pop    {r0-r4, r12}
    // Switch back to IRQ mode
    cps    #ARM_MODE_FIQ
    // Restore SPSR and lr_IRQ before returning
    pop    {lr}
    msr    SPSR_cxsf, lr
    pop    {lr}
    movs    pc, lr

//------------------------------------------------------------------------------
/// Handles incoming interrupt requests by branching to the corresponding
/// handler, as defined in the AIC. Supports interrupt nesting.
//------------------------------------------------------------------------------
irqHandler:
    // Return to the interrupted instruction.
    sub     lr, lr, #4

    // Push the return address and SPSR
    push    {lr}
    mrs    lr, SPSR
    push    {lr}

    // Change to supervisor mode to allow reentry.
    cps     #ARM_MODE_SVC

    // Push used registers.
    push    {r0-r4, r12}

    // Acknowledge the interrupt and get the interrupt ID
    ldr     r1, =GICC_BASE
    ldr     r0, [r1, #GICC_IAR]
    
    // Synchronize access upto this point
    dsb

    // Save r0(we need its value to mark EOI) and lr
    push    {r0, lr}
    
    // Jump to Handler
    ldr    r1, =GIC_IRQHandler
    blx    r1
    
    // Pop back r0 and lr
    pop    {r0, lr}

    // Disable interrupt if enabled by the IRQ handler
    cpsid    i

    // Write the value read from ICCIAR to ICCEOIR
    ldr    r1, =GICC_BASE
    STR    r0, [r1, #GICC_EOIR]

    // Restore used registers
    pop    {r0-r4, r12}
    
    // Switch back to IRQ mode
    cps    #ARM_MODE_IRQ
    
    // Restore SPSR and lr_IRQ before returning
    pop    {lr}
    msr    SPSR_cxsf, lr
    pop    {lr}
    movs    pc, lr

//------------------------------------------------------------------------------
/// Initializes the chip and branches to the main() function.
//------------------------------------------------------------------------------
	.section    .textEntry, code
	.global     entry

entry:
	/* Dummy vector table for ROM-code for cases when the real vector table
	 * is relocated (QSPI-XIP) */
	ldr     pc, =resetHandler
	ldr     pc, =resetHandler
	ldr     pc, =resetHandler
	ldr     pc, =resetHandler
	ldr     pc, =resetHandler
	.word   0
	ldr     pc, =resetHandler
	ldr     pc, =resetHandler

resetHandler:

/* Set up the fast interrupt stack pointer */

	mrs     r0, CPSR
	bic     r0, r0, #MODE_MSK
	orr     r0, r0, #ARM_MODE_FIQ
	msr     CPSR_c, r0
	ldr     sp, =_fiqstack
	bic     sp, sp, #0x7

/* Set up the normal interrupt stack pointer */

	bic     r0, r0, #MODE_MSK
	orr     r0, r0, #ARM_MODE_IRQ
	msr     CPSR_c, r0
	ldr     sp, =_irqstack
	bic     sp, sp, #0x7

/* Set up the abort mode stack pointer */

	bic     r0, r0, #MODE_MSK
	orr     r0, r0, #ARM_MODE_ABT
	msr     CPSR_c, r0
	ldr     sp, =_abtstack
	bic     sp, sp, #0x7

/* Set up the undefined mode stack pointer */

	bic     r0, r0, #MODE_MSK
	orr     r0, r0, #ARM_MODE_UND
	msr     CPSR_c, r0
	ldr     sp, =_undstack
	bic     sp, sp, #0x7

/* Set up the user/system mode stack pointer */

	bic     r0, r0, #MODE_MSK
	orr     r0, r0, #ARM_MODE_SYS
	msr     CPSR_c, r0
	ldr     sp, =_cstack
	bic     sp, sp, #0x7

/* Set up the supervisor mode stack pointer */

	bic     r0, r0, #MODE_MSK
	orr     r0, r0, #ARM_MODE_SVC
	msr     CPSR_c, r0
	ldr     sp, =_svcstack
	bic     sp, sp, #0x7

/* Relocate */
	ldr     r0, =_etext
	ldr     r1, =_srelocate
	ldr     r2, =_erelocate
1:
	cmp     r1, r2
	ldrcc   r3, [r0], #4
	strcc   r3, [r1], #4
	bcc     1b

/* Clear the zero segment */
	ldr     r0, =_szero
	ldr     r1, =_ezero
	mov     r2, #0
1:
	cmp     r0, r1
	strcc   r2, [r0], #4
	bcc     1b

/* Iinvalidate I Cache */
    mov     r0, #0
    mcr     p15, 0, r0, c7, c5, 0

/* Configure VBAR for the reset vectors to be at the start of SRAM */
	mov	    r2, #SRAM_BASE
	mcr	    p15, 0, r2, c12, c0, 0

/* Enable fpu */
	/* Grant non secure access for CP10 and CP11 */
	mrc	p15, 0, r0, c1, c1, 2
	orr     r0, r0, #3 << FPU_NON_SECURE_ACCESS_OFFSET
	mcr	p15, 0, r0, c1, c1, 2
	/* Set CP10 and CP11 access permission (Privileged and User mode) */
	ldr	r0, =(0xF << FPU_ACCESS_CONTROL_OFFSET)
	mcr	p15, 0, r0, c1, c0, 2
	/* Set the FPEXC EN bit to enable the FPU (and NEON instructions) */
	mov	r1, #FPU_FPEXC_EN_BIT
	vmsr	FPEXC, r1

/* Initialize the C library */

	bl      __libc_init_array

/* Branch to main() */

	bl      main

/* Loop indefinitely when program is finished */

1:
	b       1b
