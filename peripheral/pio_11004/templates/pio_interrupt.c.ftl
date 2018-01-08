<#--
/*******************************************************************************
  Port System Service Interrupt Handler Template File

  File Name:
    pio_interrupt.c

  Summary:
    This file contains source code necessary to initialize the system.

  Description:
    This file contains source code necessary to initialize the system.  It
    implements the "SYS_Initialize" function, configuration bits, and allocates
    any necessary global system resources, such as the systemObjects structure
    that contains the object handles to all the MPLAB Harmony module objects in
    the system.
 *******************************************************************************/

/*******************************************************************************
Copyright (c) 2013-2014 released Microchip Technology Inc.  All rights reserved.

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
 -->
<#macro PIO_ISR_HANDLER PIO_CHANNEL>

void PORT${PIO_CHANNEL}_Handler(void)
{
    /* PIO Interrupt Handler */
    _PIO_Interrupt_Handler(PIO_CHANNEL_${PIO_CHANNEL});
}
</#macro>
<#if PIO_INST_IDX0 == true && PIO_A_INTERRUPT_USED == true>
<@PIO_ISR_HANDLER
PIO_CHANNEL="A"
/>
</#if>
<#if PIO_INST_IDX1 == true && PIO_B_INTERRUPT_USED == true>
<@PIO_ISR_HANDLER
PIO_CHANNEL="B"
/>
</#if>
<#if PIO_INST_IDX2 == true && PIO_C_INTERRUPT_USED == true>
<@PIO_ISR_HANDLER
PIO_CHANNEL="C"
/>
</#if>
<#if PIO_INST_IDX3 == true && PIO_D_INTERRUPT_USED == true>
<@PIO_ISR_HANDLER
PIO_CHANNEL="D"
/>
</#if>
<#if PIO_INST_IDX4 == true && PIO_E_INTERRUPT_USED == true>
<@PIO_ISR_HANDLER
PIO_CHANNEL="E"
/>
</#if>

<#--
/*******************************************************************************
 End of File
*/
-->
