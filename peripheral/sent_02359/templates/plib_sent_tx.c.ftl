<#assign nibbleLengthOptions = ["Reserved","ONE","TWO","THREE","FOUR","FIVE","SIX"]>
/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}.c
 
  Summary:
    ${moduleName?lower_case} PLIB Source File
 
  Description:
    None
 
*******************************************************************************/
 
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

// Section: Included Files

#include <stddef.h>
#include <stdbool.h>
#include "device.h"
#include "plib_sent${SENT_INSTANCE}_tx.h"
<#if core.CoreSysIntFile == true & SENT_INTERRUPT_MODE == true>
#include "interrupts.h"
</#if>

/*indicates the status of data transmission*/
static volatile bool bDataTransmitted = true;

<#if SENT_INTERRUPT_MODE == true>
volatile static SENT_TRANSMIT_COMPLETE_OBJECT txCompleteObj;
</#if> 

<#list nibbleLengthOptions as options>
<#if options != "Reserved">
#define SENT${SENT_INSTANCE}CON1_NIBCNT_${options}      ((uint32_t)(_SENT${SENT_INSTANCE}CON1_NIBCNT_MASK & ((uint32_t)(${options_index}) << _SENT${SENT_INSTANCE}CON1_NIBCNT_POSITION))) 
</#if>
</#list>

// Section: SENT${SENT_INSTANCE} Module APIs

void SENT${SENT_INSTANCE}_Initialize(void)
{
    SENT${SENT_INSTANCE}CON1 = (SENT${SENT_INSTANCE}CON1_NIBCNT_${nibbleLengthOptions[SENT_CON1__NIBCNT?number]}<#if SENT_CON1__SPCEN == "1">
	        |_SENT${SENT_INSTANCE}CON1_SPCEN_MASK</#if><#if SENT_CON1__PPP == true>
	        |_SENT${SENT_INSTANCE}CON1_PPP_MASK</#if><#if SENT_CON1__CRCEN == true>
			|_SENT${SENT_INSTANCE}CON1_CRCEN_MASK</#if><#if SENT_CON1__TXPOL == "Inverted">
			|_SENT${SENT_INSTANCE}CON1_TXPOL_MASK</#if><#if SENT_CON1__TXM == "Synchronous">
			|_SENT${SENT_INSTANCE}CON1_TXM_MASK</#if><#if SENT_CON1__RCVEN == "Receiver">
			|_SENT${SENT_INSTANCE}CON1_RCVEN_MASK</#if><#if SENT_CON1__PS == "Divide-by-4">
			|_SENT${SENT_INSTANCE}CON1_PS_MASK</#if><#if SENT_CON1__SIDL == "1">
			|_SENT${SENT_INSTANCE}CON1_SIDL_MASK</#if><#if SENT_CON1__ON == "1">
			|_SENT${SENT_INSTANCE}CON1_ON_MASK</#if>);
	//Tick Time
	SENT${SENT_INSTANCE}CON2 = 0x${TICK_TIME}UL;
	//Frame Time
	<#if SENT_CON1__PPP == false>
	SENT${SENT_INSTANCE}CON3 = 0x0UL;
	<#else>
	SENT${SENT_INSTANCE}CON3 = 0x${FRAME_TIME}UL;
	</#if>
	<#if SENT_INTERRUPT_MODE == true>
    /*clear the tx interrupt flag*/
    IFS3bits.SENT${SENT_INSTANCE}IF = 0U;
    /*enable the tx interrupt*/
    IEC3bits.SENT${SENT_INSTANCE}IE = 1U;
    </#if>
    <#if SENT_INTERRUPT_MODE == true>
    /* clear the error interrupt flag*/
    IFS3bits.SENT${SENT_INSTANCE}EIF = 0U;
    /* enable the error interrupt*/
    IEC3bits.SENT${SENT_INSTANCE}EIE = 1U;
	</#if>
	
	<#if SENT_INTERRUPT_MODE == true>
	txCompleteObj.callback_fn = NULL;
	</#if>
}

void SENT${SENT_INSTANCE}_Deinitialize(void)
{
    SENT${SENT_INSTANCE}_Disable(); 
	
	IFS3bits.SENT${SENT_INSTANCE}IF = 0U;
	IEC3bits.SENT${SENT_INSTANCE}IE = 0U;
	
	IFS3bits.SENT${SENT_INSTANCE}EIF = 0U;
	IEC3bits.SENT${SENT_INSTANCE}EIE = 0U;
	
	/* De-initializing registers to POR values */
	SENT${SENT_INSTANCE}CON1 = ${CON1_REG_POR};
	SENT${SENT_INSTANCE}CON2 = ${CON2_REG_POR};
	SENT${SENT_INSTANCE}CON3 = ${CON3_REG_POR};
}

void SENT${SENT_INSTANCE}_Enable(void)
{
  SENT${SENT_INSTANCE}CON1bits.ON = 1U;
}

void SENT${SENT_INSTANCE}_Disable(void)
{
  SENT${SENT_INSTANCE}CON1bits.ON = 0U;
}

void SENT${SENT_INSTANCE}_TransmitModeSet(SENT_TRANSMIT_MODE mode)
{
  SENT${SENT_INSTANCE}CON1bits.TXM = (uint8_t)mode;
}

void SENT${SENT_INSTANCE}_Transmit(const SENT_DATA_TRANSMIT *sentData)
{
    <#if SENT_INTERRUPT_MODE == true>
    bDataTransmitted = false;
    </#if>
    <#if SENT_CON1__NIBCNT == "6">
    SENT${SENT_INSTANCE}DATbits.STAT = sentData->status;
    SENT${SENT_INSTANCE}DATbits.DATA1 = sentData->data1;
    SENT${SENT_INSTANCE}DATbits.DATA2 = sentData->data2;
    SENT${SENT_INSTANCE}DATbits.DATA3 = sentData->data3;
    SENT${SENT_INSTANCE}DATbits.DATA4 = sentData->data4;
    SENT${SENT_INSTANCE}DATbits.DATA5 = sentData->data5;
    SENT${SENT_INSTANCE}DATbits.DATA6 = sentData->data6;
    </#if>
    <#if SENT_CON1__NIBCNT == "5">
    SENT${SENT_INSTANCE}DATbits.STAT = sentData->status;
    SENT${SENT_INSTANCE}DATbits.DATA1 = sentData->data1;
    SENT${SENT_INSTANCE}DATbits.DATA2 = sentData->data2;
    SENT${SENT_INSTANCE}DATbits.DATA3 = sentData->data3;
    SENT${SENT_INSTANCE}DATbits.DATA4 = sentData->data4;
    SENT${SENT_INSTANCE}DATbits.DATA5 = sentData->data5;
    </#if>
    <#if SENT_CON1__NIBCNT == "4">
    SENT${SENT_INSTANCE}DATbits.STAT = sentData->status;
    SENT${SENT_INSTANCE}DATbits.DATA1 = sentData->data1;
    SENT${SENT_INSTANCE}DATbits.DATA2 = sentData->data2;
    SENT${SENT_INSTANCE}DATbits.DATA3 = sentData->data3;
    SENT${SENT_INSTANCE}DATbits.DATA4 = sentData->data4;
    </#if>
    <#if SENT_CON1__NIBCNT == "3">
    SENT${SENT_INSTANCE}DATbits.STAT = sentData->status;
    SENT${SENT_INSTANCE}DATbits.DATA1 = sentData->data1;
    SENT${SENT_INSTANCE}DATbits.DATA2 = sentData->data2;
    SENT${SENT_INSTANCE}DATbits.DATA3 = sentData->data3;
    </#if>
    <#if SENT_CON1__NIBCNT == "2">
    SENT${SENT_INSTANCE}DATbits.STAT = sentData->status;
    SENT${SENT_INSTANCE}DATbits.DATA1 = sentData->data1;
    SENT${SENT_INSTANCE}DATbits.DATA2 = sentData->data2;
    </#if>
    <#if SENT_CON1__NIBCNT == "1">
    SENT${SENT_INSTANCE}DATbits.STAT = sentData->status;
    SENT${SENT_INSTANCE}DATbits.DATA1 = sentData->data1;
    </#if>
    if(SENT${SENT_INSTANCE}CON1bits.TXM == 1U)
    {
        SENT${SENT_INSTANCE}STATbits.SYNCTXEN = 1U;
    }
}

bool SENT${SENT_INSTANCE}_IsTransmissionComplete(void)
{
<#if SENT_INTERRUPT_MODE == true>
    return bDataTransmitted;
<#else>
    while(IFS3bits.SENT${SENT_INSTANCE}IF == 0U)
    {
      
    }
	IFS3bits.SENT${SENT_INSTANCE}IF = 0U;
    return true;
</#if>
}

SENT_TRANSMIT_STATUS SENT${SENT_INSTANCE}_TransmitStatusGet(void)
{
    return (SENT_TRANSMIT_STATUS)SENT${SENT_INSTANCE}STAT;
}

<#if SENT_INTERRUPT_MODE == true>
void SENT${SENT_INSTANCE}_TransmitCompleteCallbackRegister(SENT_TRANSMIT_COMPLETE_CALLBACK callback_fn, uintptr_t context)
{
    /* Save callback_fn and context in local memory */
    txCompleteObj.callback_fn = callback_fn;
    txCompleteObj.context = context;
}

void __attribute__ ( ( used ) ) ${moduleName}_InterruptHandler( void )
{	
	if(txCompleteObj.callback_fn != NULL )
    {
        uintptr_t context = txCompleteObj.context;
        txCompleteObj.callback_fn(context);
    }
	if(SENT${SENT_INSTANCE}CON1bits.TXM == 0U)
    {
        bDataTransmitted = true;
    }
    else if(SENT${SENT_INSTANCE}STATbits.SYNCTXEN == 0U)
    {
        bDataTransmitted = true;
    }    
    else
    {
        bDataTransmitted = false;
    }
	IFS3bits.SENT${SENT_INSTANCE}IF = 0;
}
</#if>

/**
 End of File
*/