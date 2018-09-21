/*******************************************************************************
  I2SC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_i2sc${I2SC_INDEX?string}.c

  Summary:
    I2SC${I2SC_INDEX?string} Source File

  Description:
    This file has the implementation of all the interfaces provided for one
    particular instance of the Inter-IC Sound Controller (I2SC) peripheral.

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

#include "plib_i2sc${I2SC_INDEX?string}.h"

// *****************************************************************************
// *****************************************************************************
// Section: I2SC${I2SC_INDEX?string} Implementation
// *****************************************************************************
// *****************************************************************************

void I2SC${I2SC_INDEX?string}_Initialize ( void )
{
    // Disable and reset the I2SC
    I2SC${I2SC_INDEX?string}_REGS->I2SC_CR = I2SC_CR_TXDIS_Msk | I2SC_CR_RXDIS_Msk | I2SC_CR_CKDIS_Msk;
    I2SC${I2SC_INDEX?string}_REGS->I2SC_CR = I2SC_CR_SWRST_Msk;
       
    I2SC${I2SC_INDEX?string}_REGS->I2SC_MR = I2SC_MR_MODE(${I2SC_MR_MODE}) |		// Master/Slave Mode		
                            I2SC_MR_DATALENGTH(${I2SC_MR_DATALENGTH}) |	// Data Word Length
                            I2SC_MR_RXMONO(${I2SC_MR_RXMONO}) |		// Receiver Mono/Stereo
                            I2SC_MR_RXDMA(${I2SC_MR_RXDMA}) |		// # of DMA Channels for Receiver
                            I2SC_MR_RXLOOP(${I2SC_MR_RXLOOP}) | 	// Loopback Test Mode
                            I2SC_MR_TXMONO(${I2SC_MR_TXMONO}) |		// Transmitter Mono/Stereo
                            I2SC_MR_TXDMA(${I2SC_MR_TXDMA}) |		// # of DMA Channels for Transmitter
                            I2SC_MR_TXSAME(${I2SC_MR_TXSAME}) |		// Transmit Data When Underrun
                            I2SC_MR_IMCKDIV(${I2SC_MR_IMCKDIV}) |	// Selected Clock to IMCK Ratio
                            I2SC_MR_IMCKFS(${I2SC_MR_IMCKFS}) |		// Master Clock to Sample Rate Ratio
                            I2SC_MR_IMCKMODE(${I2SC_MR_IMCKMODE}) |	// Master Clock Mode
                            I2SC_MR_IWS(${I2SC_MR_IWS});		// Slot Width
    
    // Enable the I2SC
    I2SC${I2SC_INDEX?string}_REGS->I2SC_CR = I2SC_CR_TXEN_Msk | I2SC_CR_RXEN_Msk | I2SC_CR_CKEN_Msk;
    
    while(!(I2SC${I2SC_INDEX?string}_REGS->I2SC_SR & I2SC_SR_TXEN_Msk));
}

/*******************************************************************************
 End of File
*/

