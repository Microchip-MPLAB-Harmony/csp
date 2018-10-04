/*******************************************************************************
  Digital-to-Analog Converter Controller (DACC) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DACC_INSTANCE_NAME?lower_case}.c

  Summary:
    DACC Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

#include "device.h"
#include "plib_${DACC_INSTANCE_NAME?lower_case}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: DACC Implementation
// *****************************************************************************
// *****************************************************************************

void ${DACC_INSTANCE_NAME}_Initialize (void)
{
	<#if (DACC_CHER_CH0 || DACC_CHER_CH1)>
	
    /* Reset DACC Peripheral */
    ${DACC_INSTANCE_NAME}_REGS->DACC_CR = DACC_CR_SWRST_Msk;

    ${DACC_INSTANCE_NAME}_REGS->DACC_MR = DACC_MR_PRESCALER(${DACC_MR_PRESCALER}) ${DACC_MR_MAXS0?then('| DACC_MR_MAXS0_Msk', '')}${DACC_MR_MAXS1?then('| DACC_MR_MAXS1_Msk', '')}<#if DACC_MR_DIFF == "DIFFERENTIAL">| DACC_MR_DIFF_Msk </#if>;
    
	<#if (DACC_TRIGR_TRGEN0 && (!DACC_TRIGR_TRGEN1))>
    /* Configure Trigger Source and Over sample ratio for interpolation filter */
    ${DACC_INSTANCE_NAME}_REGS->DACC_TRIGR = DACC_TRIGR_TRGEN0_Msk | DACC_TRIGR_TRGSEL0(DACC_TRIGR_TRGSEL0_${DACC_TRIGR_TRGSEL0}_Val) | DACC_TRIGR_OSR0(DACC_TRIGR_OSR0_${DACC_TRIGR_OSR0}_Val);
    
	<#elseif ((!DACC_TRIGR_TRGEN0) && DACC_TRIGR_TRGEN1)>
    /* Configure Trigger Source and Over sample ratio for interpolation filter */
    ${DACC_INSTANCE_NAME}_REGS->DACC_TRIGR = DACC_TRIGR_TRGEN1_Msk | DACC_TRIGR_TRGSEL1(DACC_TRIGR_TRGSEL1_${DACC_TRIGR_TRGSEL1}_Val) | DACC_TRIGR_OSR1(DACC_TRIGR_OSR1_${DACC_TRIGR_OSR1}_Val);
    
    <#elseif (DACC_TRIGR_TRGEN0 && DACC_TRIGR_TRGEN1)>
    /* Configure Trigger Source and Over sample ratio for interpolation filter */
    ${DACC_INSTANCE_NAME}_REGS->DACC_TRIGR = (DACC_TRIGR_TRGEN0_Msk | DACC_TRIGR_TRGSEL0(DACC_TRIGR_TRGSEL0_${DACC_TRIGR_TRGSEL0}_Val) | DACC_TRIGR_OSR0(DACC_TRIGR_OSR0_${DACC_TRIGR_OSR0}_Val)) |\
                               (DACC_TRIGR_TRGEN1_Msk | DACC_TRIGR_TRGSEL1(DACC_TRIGR_TRGSEL1_${DACC_TRIGR_TRGSEL1}_Val) | DACC_TRIGR_OSR1(DACC_TRIGR_OSR1_${DACC_TRIGR_OSR1}_Val)); 
                               
    </#if>
    <#if ((DACC_CHER_CH0 && !DACC_CHER_CH1) && (DACC_MR_DIFF != "DIFFERENTIAL"))>
    /* Configure DACC Bias Current */
    ${DACC_INSTANCE_NAME}_REGS->DACC_ACR = DACC_ACR_IBCTLCH0(${DACC_ACR_IBCTLCH0});
    <#elseif ((!DACC_CHER_CH0 && DACC_CHER_CH1) && (DACC_MR_DIFF != "DIFFERENTIAL"))>
    /* Configure DACC Bias Current */
    ${DACC_INSTANCE_NAME}_REGS->DACC_ACR = DACC_ACR_IBCTLCH1(${DACC_ACR_IBCTLCH1});
    <#elseif ((DACC_CHER_CH0 && DACC_CHER_CH1) || (DACC_MR_DIFF == "DIFFERENTIAL"))>
    /* Configure DACC Bias Current */
	${DACC_INSTANCE_NAME}_REGS->DACC_ACR = DACC_ACR_IBCTLCH0(${DACC_ACR_IBCTLCH0}) | DACC_ACR_IBCTLCH1(${DACC_ACR_IBCTLCH1});
	</#if>
	
	/* Enable DAC Channel */
	${DACC_INSTANCE_NAME}_REGS->DACC_CHER = ${(DACC_CHER_CH0 && !DACC_CHER_CH1)?then('DACC_CHER_CH0_Msk', '')}${(!DACC_CHER_CH0 && DACC_CHER_CH1)?then('DACC_CHER_CH1_Msk', '')}${(DACC_CHER_CH0 && DACC_CHER_CH1)?then('DACC_CHER_CH0_Msk | DACC_CHER_CH1_Msk', '')};

	<#if (DACC_CHER_CH0 && (!DACC_CHER_CH1))>
    /* Wait until DAC Channel 0 is ready*/
    while(!(${DACC_INSTANCE_NAME}_REGS->DACC_CHSR& DACC_CHSR_DACRDY0_Msk));
    <#elseif ((!DACC_CHER_CH0) && DACC_CHER_CH1)>
    /* Wait until DAC Channel 1 is ready*/
    while(!(${DACC_INSTANCE_NAME}_REGS->DACC_CHSR& DACC_CHSR_DACRDY1_Msk));
    <#elseif (DACC_CHER_CH0 && DACC_CHER_CH1)>
    /* Wait until DAC Channel 0 and Channel 1 is ready*/
    while(!(${DACC_INSTANCE_NAME}_REGS->DACC_CHSR& (DACC_CHSR_DACRDY0_Msk | DACC_CHSR_DACRDY1_Msk)));
	</#if>
    </#if>
}

bool ${DACC_INSTANCE_NAME}_IsReady (DACC_CHANNEL_NUM channel)
{
    return (bool)(((${DACC_INSTANCE_NAME}_REGS->DACC_ISR>> channel) & DACC_ISR_TXRDY0_Msk) == DACC_ISR_TXRDY0_Msk);
}

void ${DACC_INSTANCE_NAME}_DataWrite (DACC_CHANNEL_NUM channel, uint32_t data)
{
    ${DACC_INSTANCE_NAME}_REGS->DACC_CDR[channel]= data;  
}
