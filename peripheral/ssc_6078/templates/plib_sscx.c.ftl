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
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "plib_${SSC_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${SSC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

// Since there is only one SSC module, the registers are accessed using ${SSC_INSTANCE_NAME}_REGS
// instead of SSCn->REGS, where n is the instance number

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

    ${SSC_INSTANCE_NAME}_REGS->SSC_CMR = 0x0;       // not used when SSC is in slave mode

    ${SSC_INSTANCE_NAME}_REGS->SSC_CR = SSC_CR_TXEN_Msk | SSC_CR_RXEN_Msk;        
}

void ${SSC_INSTANCE_NAME}_BaudSet(const uint32_t baud)
{
    // not used when SSC is in slave mode
}

/*******************************************************************************
 End of File
*/

