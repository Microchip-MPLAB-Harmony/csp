/*******************************************************************************
  SSC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SSC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${SSC_INSTANCE_NAME} Source File

  Description:
    This file has implementation of all the interfaces provided for particular
    SSC peripheral.

*******************************************************************************/

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

#include "plib_${SSC_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${SSC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${SSC_INSTANCE_NAME}_Initialize ( void )
{
    /* Disable and Reset the SSC*/
    ${SSC_INSTANCE_NAME}_REGS->SSC_CR = SSC_CR_TXDIS_Msk | SSC_CR_RXDIS_Msk;

    ${SSC_INSTANCE_NAME}_REGS->SSC_CR = SSC_CR_SWRST_Msk;
             
    /* Receiver Configurations */
    ${SSC_INSTANCE_NAME}_REGS->SSC_RCMR =  SSC_RCMR_CKS(${SSC_RCMR_CKS}) |
                           SSC_RCMR_CKO(${SSC_RCMR_CKO}) |
                           SSC_RCMR_CKI(${SSC_RCMR_CKI}) |
                           SSC_RCMR_CKG(${SSC_RCMR_CKG}) |
                           SSC_RCMR_START(${SSC_RCMR_START}) |
                           SSC_RCMR_STOP(${SSC_RCMR_STOP}) | 
                           SSC_RCMR_STTDLY(${SSC_RCMR_STTDLY}) |
                           SSC_RCMR_PERIOD(${SSC_RCMR_PERIOD}) ;

    ${SSC_INSTANCE_NAME}_REGS->SSC_RFMR =  SSC_RFMR_DATLEN(${SSC_RFMR_DATLEN}) |
                           SSC_RFMR_LOOP(${SSC_RFMR_LOOP}) |
                           SSC_RFMR_MSBF(${SSC_RFMR_MSBF}) |
                           SSC_RFMR_DATNB(${SSC_RFMR_DATNB}) |
                           SSC_RFMR_FSLEN(${SSC_RFMR_FSLEN}) |
                           SSC_RFMR_FSOS(${SSC_RFMR_FSOS}) |
                           SSC_RFMR_FSEDGE(${SSC_RFMR_FSEDGE}) |
                           SSC_RFMR_FSLEN_EXT(${SSC_RFMR_FSLEN_EXT}) ;
    
    /* Transmitter Configurations */

    ${SSC_INSTANCE_NAME}_REGS->SSC_TCMR =  SSC_TCMR_CKS(${SSC_TCMR_CKS}) |
                           SSC_TCMR_CKO(${SSC_TCMR_CKO}) |
                           SSC_TCMR_CKI(${SSC_TCMR_CKI}) |
                           SSC_TCMR_CKG(${SSC_TCMR_CKG}) |
                           SSC_TCMR_START(${SSC_TCMR_START}) |
                           SSC_TCMR_STTDLY(${SSC_TCMR_STTDLY}) |
                           SSC_TCMR_PERIOD(${SSC_TCMR_PERIOD}) ;

    ${SSC_INSTANCE_NAME}_REGS->SSC_TFMR = SSC_TFMR_DATLEN(${SSC_TFMR_DATLEN}) |
                           SSC_TFMR_DATDEF(${SSC_TFMR_DATDEF}) |
                           SSC_TFMR_MSBF(${SSC_TFMR_MSBF}) |
                           SSC_TFMR_DATNB(${SSC_TFMR_DATNB}) |
                           SSC_TFMR_FSLEN(${SSC_TFMR_FSLEN}) |
                           SSC_TFMR_FSOS(${SSC_TFMR_FSOS}) |
                           SSC_TFMR_FSDEN(${SSC_TFMR_FSDEN}) |
                           SSC_TFMR_FSEDGE(${SSC_TFMR_FSEDGE}) |
                           SSC_TFMR_FSLEN_EXT(${SSC_TFMR_FSLEN_EXT}) ;

    ${SSC_INSTANCE_NAME}_REGS->SSC_CMR = ${SSC_CMR_DIV};       // not used when SSC is in slave mode

    ${SSC_INSTANCE_NAME}_REGS->SSC_CR = SSC_CR_TXEN_Msk | SSC_CR_RXEN_Msk;        
}

void ${SSC_INSTANCE_NAME}_BaudSet(const uint32_t baud)
{
    // not used when SSC is in slave mode
}

<#if SSC_AUDIO_PROTOCOL == "AUDIO_LJ">
uint32_t ${SSC_INSTANCE_NAME}_LRCLK_Get(void)
{
    // for left-justified format, will sync on high to low transition
    volatile uint32_t ret = 1-${SSC_LRCLK_PIN_DEFINE};
    return ret;    
}
<#else>
uint32_t ${SSC_INSTANCE_NAME}_LRCLK_Get(void)
{
    // for I2S format, will sync on low to high transition
    volatile uint32_t ret = ${SSC_LRCLK_PIN_DEFINE};
    return ret;    
}
</#if>

/*******************************************************************************
 End of File
*/

