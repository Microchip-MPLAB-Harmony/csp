/*******************************************************************************
  Position Decoder(${PDEC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PDEC_INSTANCE_NAME?lower_case}.c

  Summary
    ${PDEC_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the PDEC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_${PDEC_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************
<#assign PDEC_INTERRUPT = false>
<#assign PDEC_MAIN_INTERRUPT = false>
<#if PDEC_INTENSET_OVF || PDEC_INTENSET_VLC || PDEC_INTENSET_DIR || PDEC_INTENSET_MC_0 || PDEC_INTENSET_MC_1>
    <#assign PDEC_INTERRUPT = true>
</#if>
<#if PDEC_INTENSET_OVF || PDEC_INTENSET_VLC || PDEC_INTENSET_DIR >
<#assign PDEC_MAIN_INTERRUPT = true>
</#if>
<#if PDEC_INTERRUPT == true>
    <#lt>/* Object to hold callback function and context */
   static volatile <#lt>PDEC_${PDEC_CTRLA_MODE}_CALLBACK_OBJ ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${PDEC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Initialize the PDEC module in Quadrature mode */
void ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}Initialize( void )
{
    /* Reset PDEC */
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_CTRLA = PDEC_CTRLA_SWRST_Msk;

    while((${PDEC_INSTANCE_NAME}_REGS->PDEC_SYNCBUSY & PDEC_SYNCBUSY_SWRST_Msk) == PDEC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Write Synchronization */
    }

    /* Configure quadrature control settings */
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_CTRLA = PDEC_CTRLA_MODE_${PDEC_CTRLA_MODE}
                  | PDEC_CTRLA_PINEN(0x${PDEC_HALL_PIN}U) | PDEC_CTRLA_PINVEN(0x${PDEC_HALL_PIN_INV}U)<#rt>
                  <#lt>${PDEC_CTRLA_RUNSTDBY?then(' | PDEC_CTRLA_RUNSTDBY_Msk', '')}; <#rt>

    ${PDEC_INSTANCE_NAME}_REGS->PDEC_PRESC = PDEC_PRESC_PRESC_${PDEC_PRESC_PRESC};
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_FILTER = PDEC_FILTER_FILTER(${PDEC_FILTER}U);

    /* Clear all interrupt flags */
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_INTFLAG = PDEC_INTFLAG_Msk;

<#if PDEC_INTERRUPT == true>
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_INTENSET = 0x${PDEC_INTENSET};
    ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.callback = NULL;
</#if>

    ${PDEC_INSTANCE_NAME}_REGS->PDEC_EVCTRL = 0x${PDEC_HALL_EVCTRL};

    while((${PDEC_INSTANCE_NAME}_REGS->PDEC_SYNCBUSY)!= 0U)
    {
        /* Wait for Write Synchronization */
    }
}

/* Enable and start the hall operation */
void ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}Start( void )
{
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_CTRLA |= PDEC_CTRLA_ENABLE_Msk;
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_CTRLBSET = PDEC_CTRLBSET_CMD_START;
    while((${PDEC_INSTANCE_NAME}_REGS->PDEC_SYNCBUSY)!= 0U)
    {
        /* Wait for Write Synchronization */
    }
}

/* Disable and stop the hall operation */
void ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}Stop( void )
{
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_CTRLBSET = PDEC_CTRLBSET_CMD_STOP;
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_CTRLA &= ~PDEC_CTRLA_ENABLE_Msk;
    while((${PDEC_INSTANCE_NAME}_REGS->PDEC_SYNCBUSY)!= 0U)
    {
        /* Wait for Write Synchronization */
    }
}

/* Read the hall pattern */
uint8_t ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}PatternGet( void )
{
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_CTRLBSET = PDEC_CTRLBSET_CMD_READSYNC;
    while((${PDEC_INSTANCE_NAME}_REGS->PDEC_SYNCBUSY & PDEC_SYNCBUSY_CTRLB_Msk) == PDEC_SYNCBUSY_CTRLB_Msk)
    {
        /* Wait for read Synchronization */
    }
    while((${PDEC_INSTANCE_NAME}_REGS->PDEC_CTRLBSET & PDEC_CTRLBSET_CMD_Msk) != PDEC_CTRLBSET_CMD_NONE)
    {
        /* Wait for CMD to become zero */
    }
    return (uint8_t)(${PDEC_INSTANCE_NAME}_REGS->PDEC_COUNT & 0x07U);
}


/* Set the hall pattern */
bool ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}PatternSet( uint8_t pattern )
{
    bool status = false;
    if((${PDEC_INSTANCE_NAME}_REGS->PDEC_STATUS & PDEC_STATUS_CCBUFV0_Msk) == 0U)
    {
        ${PDEC_INSTANCE_NAME}_REGS->PDEC_CCBUF[0] =((uint32_t)pattern & 0x07U);
        status = true;
    }
    return status;
}

bool ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}TimeWindowSet(uint16_t low_window, uint16_t high_window)
{
    bool status = false;
    if((${PDEC_INSTANCE_NAME}_REGS->PDEC_STATUS & PDEC_STATUS_CCBUFV0_Msk) == 0U)
    {
        ${PDEC_INSTANCE_NAME}_REGS->PDEC_CCBUF[0] =(uint32_t)low_window << 16;
        if((${PDEC_INSTANCE_NAME}_REGS->PDEC_STATUS & PDEC_STATUS_CCBUFV1_Msk) == 0U)
        {
            ${PDEC_INSTANCE_NAME}_REGS->PDEC_CCBUF[1] = (uint32_t)high_window << 16;
            status = true;
        }
    }
    return status;
}


<#if PDEC_INTERRUPT == true>
void ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}CallbackRegister( PDEC_${PDEC_CTRLA_MODE}_CALLBACK callback, uintptr_t context )
{
    ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.callback = callback;
    ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.context = context;
}
<#else>
PDEC_${PDEC_CTRLA_MODE}_STATUS ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}StatusGet( void )
{
    PDEC_${PDEC_CTRLA_MODE}_STATUS status;
    status = (PDEC_${PDEC_CTRLA_MODE}_STATUS) ${PDEC_INSTANCE_NAME}_REGS->PDEC_INTFLAG;
    /* Clear interrupt flags */
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_INTFLAG = status;
    return status;
}
</#if>

<#if (PDEC_MAIN_INTERRUPT == true) || ((PDEC_NUM_INT_LINES == 0) && (PDEC_INTERRUPT == true))>
void __attribute__((used)) ${PDEC_INSTANCE_NAME}_InterruptHandler( void )
{
    PDEC_${PDEC_CTRLA_MODE}_STATUS status;
    /* Additional local variable to prevent MISRA C violations (Rule 13.x) */
    uintptr_t context;
    context  =${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.context;
    status = ${PDEC_INSTANCE_NAME}_REGS->PDEC_INTFLAG;
    /* Clear interrupt flags */
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_INTFLAG = 0xFF;
    if (${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.callback != NULL)
    {
        ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.callback(status, context);
    }

}
</#if>

<#if (PDEC_INTENSET_MC_0 == true) && (PDEC_NUM_INT_LINES != 0)>
void __attribute__((used)) ${PDEC_INSTANCE_NAME}_MC0_InterruptHandler( void )
{
    PDEC_${PDEC_CTRLA_MODE}_STATUS status;
    /* Additional local variable to prevent MISRA C violations (Rule 13.x) */
    uintptr_t context;
    context  =${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.context;
    status =  ${PDEC_INSTANCE_NAME}_REGS->PDEC_INTFLAG & PDEC_INTFLAG_MC0_Msk;
    /* Clear interrupt flags */
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_INTFLAG = PDEC_INTFLAG_MC0_Msk;
    if (${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.callback != NULL)
    {
        ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.callback(status, context);
    }
}
</#if>

<#if (PDEC_INTENSET_MC_1 == true) && (PDEC_NUM_INT_LINES != 0)>
void __attribute__((used)) ${PDEC_INSTANCE_NAME}_MC1_InterruptHandler( void )
{
    PDEC_${PDEC_CTRLA_MODE}_STATUS status;
    /* Additional local variable to prevent MISRA C violations (Rule 13.x) */
    uintptr_t context;
    context  =${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.context;
    status = ${PDEC_INSTANCE_NAME}_REGS->PDEC_INTFLAG & PDEC_INTFLAG_MC1_Msk;
    /* Clear interrupt flags */
    ${PDEC_INSTANCE_NAME}_REGS->PDEC_INTFLAG = PDEC_INTFLAG_MC1_Msk;
    if (${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.callback != NULL)
    {
        ${PDEC_INSTANCE_NAME}_${PDEC_CTRLA_MODE}_CallbackObj.callback(status, context);
    }
}
</#if>
