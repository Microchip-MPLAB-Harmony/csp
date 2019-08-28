/*********************************************************************
 *
 *                  General Exception
 *
 *********************************************************************
 * Filename:        general-exception-context.S
 *
 * Processor:       PIC32
 *
 * Compiler:        MPLAB XC32 v1.00
 *                  MPLAB X IDE
 * Company:         Microchip Technology Inc.
 *
 * Software License Agreement
 *
 * This software is developed by Microchip Technology Inc. and its
 * subsidiaries ("Microchip").
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * 1.      Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 *
 * 2.      Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution.
 *
 * 3.      Microchip's name may not be used to endorse or promote products
 * derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY MICROCHIP "AS IS" AND ANY EXPRESS OR IMPLIED
 * WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL
 * MICROCHIP BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING BUT NOT LIMITED TO
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA OR PROFITS;
 * OR BUSINESS INTERRUPTION) HOWSOEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
 * OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 * ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 ********************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
//DOM-IGNORE-END

#include <xc.h>
#ifdef __LIBBUILD__
   .file 1 "general-exception-context.S"
   .loc 1 0
#endif
  ###################
  # Default general exception handler
  ###################

  .section .text.general_exception, code
  .set noreorder
  .set noat
  .globl _general_exception_context
  .ent _general_exception_context

_general_exception_context:

# Save off the non-callee saved registers that may get mucked with
  addiu sp, sp, -112
  sw    fp, 16(sp)
  addiu fp, sp, 16
#; save regs
  sw $1,  4(fp)
  sw v0,  8(fp)
  sw v1, 12(fp)
  sw a0, 16(fp)
  sw a1, 20(fp)
  sw a2, 24(fp)
  sw a3, 28(fp)
  sw t0, 32(fp)
  sw t1, 36(fp)
  sw t2, 40(fp)
  sw t3, 44(fp)
  sw t4, 48(fp)
  sw t5, 52(fp)
  sw t6, 56(fp)
  sw t7, 60(fp)
  sw t8, 64(fp)
  sw t9, 68(fp)
  sw ra, 72(fp)
  mflo t0       // note this is for M4K only, as it does not include the other ac registers
  mfhi t1
  sw t0, 76(fp)
  sw t1, 80(fp)
  mfc0 t0, _CP0_CAUSE
  mfc0 t1, _CP0_STATUS
  mfc0 t2, _CP0_EPC
  sw   t0, 84(fp)
  sw   t1, 88(fp)
  sw   t2, 92(fp)
  jal _general_exception_handler
  addiu    a0, fp, 4  // send pointer to fp to exception handler

#; return from _general_exception_handler
  addiu fp, sp, 16

  lw $1,  4(fp)
  lw v0,  8(fp)
  lw v1, 12(fp)
  lw a0, 16(fp)
  lw a1, 20(fp)
  lw a2, 24(fp)
  lw a3, 28(fp)

  lw t0, 76(fp)  // using temp registers to reload hi and lo
  lw t1, 80(fp)
  mtlo t0
  mthi t1

  lw t0, 32(fp)
  lw t1, 36(fp)
  lw t2, 40(fp)
  lw t3, 44(fp)
  lw t4, 48(fp)
  lw t5, 52(fp)
  lw t6, 56(fp)
  lw t7, 60(fp)
  lw t8, 64(fp)
  lw t9, 68(fp)
  lw ra, 72(fp)


  di
  ehb

  lw k0, 84(fp)
  lw k1, 88(fp)
  mtc0  k0, _CP0_CAUSE
  lw k0, 92(fp)
  mtc0  k1, _CP0_STATUS
  mtc0  k0, _CP0_EPC
  lw    fp, 16(sp)
  addiu sp, sp, 112
  ehb
  eret

  .end _general_exception_context

