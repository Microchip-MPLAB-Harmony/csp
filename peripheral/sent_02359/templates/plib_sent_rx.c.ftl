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
#include "plib_sent${SENT_INSTANCE}_rx.h"
<#if core.CoreSysIntFile == true & SENT_INTERRUPT_MODE == true>
#include "interrupts.h"
</#if>

static volatile bool bDataReceived = false;

<#if SENT_INTERRUPT_MODE == true>
void ${moduleName}_InterruptHandler( void );
volatile static SENT_RECEIVE_COMPLETE_CALLBACK_OBJECT rxCompleteObj;

void ${moduleName}E_InterruptHandler( void );
volatile static SENT_ERROR_OBJECT rxErrorObj;
</#if>

<#list nibbleLengthOptions as options>
<#if options != "Reserved">
#define SENT${SENT_INSTANCE}CON1_NIBCNT_${options}      ((uint32_t)(_SENT${SENT_INSTANCE}CON1_NIBCNT_MASK & ((uint32_t)(${options_index}) << _SENT${SENT_INSTANCE}CON1_NIBCNT_POSITION))) 
</#if>
</#list>

// Section: ${moduleName} Module APIs

void SENT${SENT_INSTANCE}_Initialize(void)
{
    SENT${SENT_INSTANCE}CON1 = (SENT${SENT_INSTANCE}CON1_NIBCNT_${nibbleLengthOptions[SENT_CON1__NIBCNT?number]}<#if SENT_CON1__SPCEN == "1">
	        |_SENT${SENT_INSTANCE}CON1_SPCEN_MASK</#if><#if SENT_CON1__PPP == true>
	        |_SENT${SENT_INSTANCE}CON1_PPP_MASK</#if><#if SENT_CON1__CRCEN == true>
			|_SENT${SENT_INSTANCE}CON1_CRCEN_MASK</#if><#if SENT_CON1__TXPOL == "Inverted">
			|_SENT${SENT_INSTANCE}CON1_TXPOL_MASK</#if><#if SENT_CON1__TXM == "Synchronous">
			|_SENT${SENT_INSTANCE}CON1_TXM_MASK</#if><#if SENT_CON1__RCVEN == "Receiver">
			|_SENT${SENT_INSTANCE}CON1_RCVEN_MASK</#if><#if SENT_CON1__SIDL == "1">
			|_SENT${SENT_INSTANCE}CON1_SIDL_MASK</#if><#if SENT_CON1__ON == "1">
			|_SENT${SENT_INSTANCE}CON1_ON_MASK</#if>);
			
	/* SYNC MAX */
	SENT${SENT_INSTANCE}CON2 = 0x${SYNC_MAX}UL;
	/* SYNC MIN */
	SENT${SENT_INSTANCE}CON3 = 0x${SYNC_MIN}UL;
	<#if SENT_INTERRUPT_MODE == true>
	// clear the rx/tx interrupt flag
    IFS3bits.SENT${SENT_INSTANCE}IF = 0U;
    // enable the rx/tx interrupt
    IEC3bits.SENT${SENT_INSTANCE}IE = 1U;
    </#if>
    <#if SENT_INTERRUPT_MODE == true>
    // clear the error interrupt flag
    IFS3bits.SENT${SENT_INSTANCE}EIF = 0U;
    // enable the error interrupt
    IEC3bits.SENT${SENT_INSTANCE}EIE = 1U;
	</#if>
	
	<#if SENT_INTERRUPT_MODE == true>
	rxCompleteObj.callback_fn = NULL;
	rxErrorObj.callback_fn = NULL;
	</#if>
}

void SENT${SENT_INSTANCE}_Deinitialize(void)
{
    ${moduleName}_Disable(); 
	
	IFS3bits.SENT${SENT_INSTANCE}IF= 0U;
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

SENT_DATA_RECEIVE SENT${SENT_INSTANCE}_Receive(void)
{
    SENT_DATA_RECEIVE sentData = {0};
    <#if SENT_CON1__NIBCNT == "6">
    sentData.status =   SENT${SENT_INSTANCE}DATbits.STAT;
    sentData.data1  =   SENT${SENT_INSTANCE}DATbits.DATA1;
    sentData.data2  =   SENT${SENT_INSTANCE}DATbits.DATA2;
    sentData.data3  =   SENT${SENT_INSTANCE}DATbits.DATA3; 
    sentData.data4  =   SENT${SENT_INSTANCE}DATbits.DATA4;
    sentData.data5  =   SENT${SENT_INSTANCE}DATbits.DATA5; 
    sentData.data6  =   SENT${SENT_INSTANCE}DATbits.DATA6; 
    </#if>
    <#if SENT_CON1__NIBCNT == "5">
    sentData.status =  SENT${SENT_INSTANCE}DATbits.STAT;
    sentData.data1  =  SENT${SENT_INSTANCE}DATbits.DATA1;
    sentData.data2  =  SENT${SENT_INSTANCE}DATbits.DATA2;
    sentData.data3  =  SENT${SENT_INSTANCE}DATbits.DATA3; 
    sentData.data4  =  SENT${SENT_INSTANCE}DATbits.DATA4;
    sentData.data5  =  SENT${SENT_INSTANCE}DATbits.DATA5; 
    </#if>
    <#if SENT_CON1__NIBCNT == "4">
    sentData.status =   SENT${SENT_INSTANCE}DATbits.STAT;
    sentData.data1  =   SENT${SENT_INSTANCE}DATbits.DATA1;
    sentData.data2  =   SENT${SENT_INSTANCE}DATbits.DATA2;
    sentData.data3  =   SENT${SENT_INSTANCE}DATbits.DATA3; 
    sentData.data4  =   SENT${SENT_INSTANCE}DATbits.DATA4;
    </#if>
    <#if SENT_CON1__NIBCNT == "3">
    sentData.status =   SENT${SENT_INSTANCE}DATbits.STAT;
    sentData.data1  =   SENT${SENT_INSTANCE}DATbits.DATA1;
    sentData.data2  =   SENT${SENT_INSTANCE}DATbits.DATA2;
    sentData.data3  =   SENT${SENT_INSTANCE}DATbits.DATA3;
    </#if>
    <#if SENT_CON1__NIBCNT == "2">
    sentData.status =   SENT${SENT_INSTANCE}DATbits.STAT;
    sentData.data1  =   SENT${SENT_INSTANCE}DATbits.DATA1;
    sentData.data2  =   SENT${SENT_INSTANCE}DATbits.DATA2;
    </#if>
    <#if SENT_CON1__NIBCNT == "1">
    sentData.status =  SENT${SENT_INSTANCE}DATbits.STAT;
    sentData.data1  =  SENT${SENT_INSTANCE}DATbits.DATA1;
    </#if>
    <#if SENT_INTERRUPT_MODE == true>
    bDataReceived = false;
    </#if>
    return sentData;
}

bool SENT${SENT_INSTANCE}_IsDataReceived(void)
{
<#if SENT_INTERRUPT_MODE == true>
   return bDataReceived;
<#else>
   while(IFS3bits.SENT${SENT_INSTANCE}IF == 0U)
   {
   }
   IFS3bits.SENT${SENT_INSTANCE}IF = 0U;
   return true;
</#if>
}

SENT_RECEIVE_STATUS SENT${SENT_INSTANCE}_ReceiveStatusGet(void)
{
    return (SENT${SENT_INSTANCE}STAT);
}

SENT_ERROR_CODE ReceiveErrorGet(void)
{
	if(IFS3bits.SENT${SENT_INSTANCE}EIF == 0x1)
	{
		SENT_ERROR_CODE errorCode = NO_ERROR;
		
		if(SENT1STATbits.CRCERR == 0x1)
		{
			SENT1STATbits.CRCERR = 0;
			errorCode = CRC_ERROR;
		}
		else if(SENT1STATbits.FRMERR == 0x1)
		{
			SENT1STATbits.FRMERR = 0;
			errorCode = FRAME_ERROR;
		}
		else if(SENT1STATbits.RXIDLE == 0x1)
		{
			SENT1STATbits.RXIDLE = 0;
			errorCode = RX_IDLE_ERROR;
		}
		else
		{
			//Nothing to process
		}
		IFS3bits.SENT${SENT_INSTANCE}EIF = 0;
		return errorCode;
	}
	return NO_ERROR;
}
			
<#if SENT_INTERRUPT_MODE == true>
void SENT${SENT_INSTANCE}_ReceiveCompleteCallbackRegister(SENT_RECEIVE_COMPLETE_CALLBACK callback_fn, uintptr_t context)
{
    /* - Save callback_fn and context in local memory */
    rxCompleteObj.callback_fn = callback_fn;
    rxCompleteObj.context = context;
}

void SENT${SENT_INSTANCE}_ErrorCallbackRegister(SENT_ERROR_CALLBACK callback_fn, uintptr_t context)
{
    rxErrorObj.callback_fn = callback_fn;
    rxErrorObj.context = context;
}

void __attribute__ ( ( used ) ) ${moduleName}_InterruptHandler( void )
{	
	if(rxCompleteObj.callback_fn != NULL )
    {
        uintptr_t context = rxCompleteObj.context;
        rxCompleteObj.callback_fn(context);
    }
    
    bDataReceived = true;
    IFS3bits.SENT${SENT_INSTANCE}IF = 0;
}

void __attribute__ ( ( used ) ) ${moduleName}E_InterruptHandler (void)
{	
    
	if(rxErrorObj.callback_fn != NULL)
    {
        uintptr_t context = rxErrorObj.context;
        rxErrorObj.callback_fn(context);
    }
	
	if(SENT${SENT_INSTANCE}STATbits.FRMERR == 1U)
    {
        SENT${SENT_INSTANCE}STATbits.FRMERR = 0U;
    }
    if(SENT${SENT_INSTANCE}STATbits.CRCERR == 1U)
    {
        SENT${SENT_INSTANCE}STATbits.CRCERR = 0U;
    }
	IFS3bits.SENT${SENT_INSTANCE}EIF = 0U;
}
</#if>

/**
 End of File
*/