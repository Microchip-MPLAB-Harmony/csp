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

