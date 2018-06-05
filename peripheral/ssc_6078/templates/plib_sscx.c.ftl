/*******************************************************************************
  SSC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ssc${SSC_INDEX?string}.c

  Summary:
    SSC${SSC_INDEX?string} Source File

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

#include "plib_ssc${SSC_INDEX?string}.h"

// *****************************************************************************
// *****************************************************************************
// Section: SSC${SSC_INDEX?string} Implementation
// *****************************************************************************
// *****************************************************************************

// Since there is only one SSC module, the registers are accessed using SSC_REGS
// instead of SSCn->REGS, where n is the instance number

void SSC${SSC_INDEX?string}_Initialize ( void )
{
    /* Disable and Reset the SSC*/
    SSC_REGS->SSC_CR = SSC_CR_TXDIS_Msk | SSC_CR_RXDIS_Msk;

    SSC_REGS->SSC_CR = SSC_CR_SWRST_Msk;
             
    /* Receiver Configurations */
    SSC_REGS->SSC_RCMR =  SSC_RCMR_CKS(${SSC_RCMR_CKS}) |
                           SSC_RCMR_CKO(${SSC_RCMR_CKO}) |
                           SSC_RCMR_CKI(${SSC_RCMR_CKI}) |
                           SSC_RCMR_CKG(${SSC_RCMR_CKG}) |
                           SSC_RCMR_START(${SSC_RCMR_START}) |
                           SSC_RCMR_STOP(${SSC_RCMR_STOP}) | 
                           SSC_RCMR_STTDLY(${SSC_RCMR_STTDLY}) |
                           SSC_RCMR_PERIOD(${SSC_RCMR_PERIOD}) ;

    SSC_REGS->SSC_RFMR =  SSC_RFMR_DATLEN(${SSC_RFMR_DATLEN}) |
                           SSC_RFMR_LOOP(${SSC_RFMR_LOOP}) |
                           SSC_RFMR_MSBF(${SSC_RFMR_MSBF}) |
                           SSC_RFMR_DATNB(${SSC_RFMR_DATNB}) |
                           SSC_RFMR_FSLEN(${SSC_RFMR_FSLEN}) |
                           SSC_RFMR_FSOS(${SSC_RFMR_FSOS}) |
                           SSC_RFMR_FSEDGE(${SSC_RFMR_FSEDGE}) |
                           SSC_RFMR_FSLEN_EXT(${SSC_RFMR_FSLEN_EXT}) ;
    
    /* Transmitter Configurations */

    SSC_REGS->SSC_TCMR =  SSC_TCMR_CKS(${SSC_TCMR_CKS}) |
                           SSC_TCMR_CKO(${SSC_TCMR_CKO}) |
                           SSC_TCMR_CKI(${SSC_TCMR_CKI}) |
                           SSC_TCMR_CKG(${SSC_TCMR_CKG}) |
                           SSC_TCMR_START(${SSC_TCMR_START}) |
                           SSC_TCMR_STTDLY(${SSC_TCMR_STTDLY}) |
                           SSC_TCMR_PERIOD(${SSC_TCMR_PERIOD}) ;

    SSC_REGS->SSC_TFMR = SSC_TFMR_DATLEN(${SSC_TFMR_DATLEN}) |
                           SSC_TFMR_DATDEF(${SSC_TFMR_DATDEF}) |
                           SSC_TFMR_MSBF(${SSC_TFMR_MSBF}) |
                           SSC_TFMR_DATNB(${SSC_TFMR_DATNB}) |
                           SSC_TFMR_FSLEN(${SSC_TFMR_FSLEN}) |
                           SSC_TFMR_FSOS(${SSC_TFMR_FSOS}) |
                           SSC_TFMR_FSDEN(${SSC_TFMR_FSDEN}) |
                           SSC_TFMR_FSEDGE(${SSC_TFMR_FSEDGE}) |
                           SSC_TFMR_FSLEN_EXT(${SSC_TFMR_FSLEN_EXT}) ;        
}

void SSC${SSC_INDEX?string}_BaudSet(const uint32_t baud)
{
}

/*******************************************************************************
 End of File
*/

