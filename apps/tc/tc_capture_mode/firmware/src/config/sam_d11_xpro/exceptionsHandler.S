;/*******************************************************************************
;  System Exceptions File
;
;  File Name:
;    exceptionsHandler.s
;
;  Summary:
;    This file contains a function which overrides the default _weak_ exception
;    handlers provided by the interrupt.c file.
;
;  Description:
;    This file redefines the default _weak_  exception handler with a more debug
;    friendly one. If an unexpected exception occurs the code will stop in a
;    while(1) loop.
;*******************************************************************************/
;
;// DOM-IGNORE-BEGIN
;/*******************************************************************************
;* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
;*
;* Subject to your compliance with these terms, you may use Microchip software
;* and any derivatives exclusively with Microchip products. It is your
;* responsibility to comply with third party license terms applicable to your
;* use of third party software (including open source software) that may
;* accompany Microchip software.
;*
;* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
;* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
;* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
;* PARTICULAR PURPOSE.
;*
;* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
;* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
;* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
;* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
;* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
;* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
;* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
;*******************************************************************************/
;// DOM-IGNORE-END

/*
;*******************************************************************************
;* Hard Fault Handler
;*******************************************************************************
*/

.global HardFault_Handler
.type HardFault_Handler, function
.extern HardFault_Handler_C

.syntax unified
.thumb
.balign 4
.text

.thumb_func
HardFault_Handler:
    MOVS    R0, #4
    MOV     R1, LR
    TST     R0, R1              // Check bit 2 of LR (EXC_RETURN) is 0?.
    BEQ     stacking_used_MSP
    MRS     R0, PSP             // PSP is used
    B       get_LR_and_branch

stacking_used_MSP:
    MRS     R0, MSP             // PSP is used

get_LR_and_branch:
    LDR     R2,=HardFault_Handler_C
    BX      R2                  // R0=Stack Pointer, R1 = Link Register





    .end






