/*******************************************************************************
  TWI Peripheral Library Source File

  Company
    Microchip Technology Inc.

  File Name
    twi.c

  Summary
    TWI peripheral library interface.

  Description

  Remarks:
    
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
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
// DOM-IGNORE-END

#include "${__PROCESSOR?lower_case}.h"
#include "plib_twi${INDEX?string}.h"

static TWI_OBJ twi${INDEX?string}Obj;
static TWI_TRANSACTION_REQUEST_BLOCK twi${INDEX?string}TRBsList[${TWI_NUM_TRBS}];
static twi_registers_t *TWI${INDEX?string}_Module = (twi_registers_t *)TWI_ID_${INDEX?string};

// *****************************************************************************
/* Function:
    void TWIx_Initialize(void)

   Summary:
    Initializes given instance of the TWI peripheral.

   Precondition:
    None.
	
   Parameters:
    None.
	
   Returns:
    None
*/

void TWI${INDEX?string}_Initialize(void)
{    
    // Reset the i2c Module
    TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_SWRST_Msk;
        
    // Disable the I2C Master/Slave Mode
    TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_MSDIS_Msk | 
	                                      TWI_CR_SVDIS_Msk;
	
    // Set Baud rate 
	TWI${INDEX?string}_Module->TWI_CWGR.w = ( TWI_CWGR_HOLD_Msk & TWI${INDEX?string}_Module->TWI_CWGR.w ) |
											( TWI_CWGR_CLDIV(${TWI_CWGR_CLDIV}) | 
											  TWI_CWGR_CHDIV(${TWI_CWGR_CHDIV}) | 
											  TWI_CWGR_CKDIV(${TWI_CWGR_CKDIV}) );
	
	// Starts the transfer by clearing the transmit hold register 
    TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_THRCLR_Msk;
	
	// Enables interrupt on nack and arbitration lost 
    TWI${INDEX?string}_Module->TWI_IER.w = TWI_IER_NACK_Msk | 
	                                       TWI_IER_ARBLST_Msk;
	
	// Enable Master Mode 
    TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_MSEN_Msk;
	
	// Initialize the twi PLib Object
	twi${INDEX?string}Obj.status  = TWI_TRANSFER_SUCCESS;
	twi${INDEX?string}Obj.state   = TWI_STATE_IDLE;
	twi${INDEX?string}Obj.numTRBs = 0;		
}


// *****************************************************************************
/* Function:
    bool TWIx_ReadTRBBuild(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Allocates and Builds the Read Transaction Request Block.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy.

   Parameters:
    address - 7-bit / 10-bit slave address.
	pdata   - pointer to destination data buffer
	length  - length of data buffer in number of bytes.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.
*/

bool TWI${INDEX?string}_ReadTRBBuild(uint16_t address, uint8_t *pdata, uint8_t length)
{
	TWI_TRANSACTION_REQUEST_BLOCK * trb = NULL;
	
	// current TRB index cannot be more than available TRB's
    if( twi${INDEX?string}Obj.numTRBs >= ${TWI_NUM_TRBS})
	{
	    return false;
	}
	
	// Check for ongoing transfer
	if( twi${INDEX?string}Obj.state != TWI_STATE_IDLE )
	{
	    return false;
	}
	
	trb = &twi${INDEX?string}TRBsList[twi${INDEX?string}Obj.numTRBs];
	
	// Fill the TRB
	trb->address = address;
	trb->read    = true;
	trb->length  = length;
	trb->pbuffer = pdata;
	
	// Increment current TRB index
	twi${INDEX?string}Obj.numTRBs++;
	
	return true;
}

// *****************************************************************************
/* Function:
    bool TWIx_WriteTRBBuild(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Allocates and Builds the Read Transaction Request Block.
	
   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy.

   Parameters:
    address - 7-bit / 10-bit slave address.
	pdata   - pointer to source data buffer
	length  - length of data buffer in number of bytes.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.
*/

bool TWI${INDEX?string}_WriteTRBBuild(uint16_t address, uint8_t *pdata, uint8_t length)
{
    TWI_TRANSACTION_REQUEST_BLOCK * trb = NULL;
	
	// current TRB index cannot be more than available TRB's
    if( twi${INDEX?string}Obj.numTRBs >= ${TWI_NUM_TRBS})
	{
	    return false;
	}
	
	// Check for ongoing transfer
	if( twi${INDEX?string}Obj.state != TWI_STATE_IDLE )
	{
	    return false;
	}
	
	trb = &twi${INDEX?string}TRBsList[twi${INDEX?string}Obj.numTRBs];
	
	// Fill the TRB
	trb->address = address;
	trb->read    = false;
	trb->length  = length;
	trb->pbuffer = pdata;
	
	// Increment current TRB index
	twi${INDEX?string}Obj.numTRBs++;
	
	return true;
}

// *****************************************************************************
/* Function:
    bool TWIx_TRBTransfer(void)
	
   Summary:
    Submits all TRB's build for processing. 
	
   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWIx_TRBTransfer.

   Parameters:
    None.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.
*/

bool TWI${INDEX?string}_TRBTransfer(void)
{
    // Minimum one filled TRB must be available
    if(  twi${INDEX?string}Obj.numTRBs == 0 )
	{
	    return false;
	}
	
	// Check for ongoing transfer
    if( twi${INDEX?string}Obj.state != TWI_STATE_IDLE )
	{
	    return false;
	}
	
	// Initiate Transfer
	twi${INDEX?string}Obj.state = TWI_STATE_ADDR_SEND;
	twi${INDEX?string}Obj.status = TWI_TRANSFER_BUSY;
	
	TWI${INDEX?string}_Module->TWI_IER.w = TWI_IER_TXCOMP_Msk | 
	                                       TWI_IER_TXRDY_Msk  |
                                           TWI_IER_RXRDY_Msk;
						   
	return true;
}

// *****************************************************************************
/* Function:
    bool TWIx_Read(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Reads data from the slave.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWIx_TRBTransfer.
	Minimum one TRB should be available.

   Parameters:
    address - 7-bit / 10-bit slave address.
	pdata   - pointer to destination data buffer
	length  - length of data buffer in number of bytes.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.
*/

bool TWI${INDEX?string}_Read(uint16_t address, uint8_t *pdata, uint8_t length)
{
    // Build Read TRB
    if ( !TWI${INDEX?string}_ReadTRBBuild( address, pdata, length ) )
	{
	    return false;
	}
	
	// Initiate transfer
	if ( !TWI${INDEX?string}_TRBTransfer( ) )
	{
	    return false;
	}
	
	return true;
}

// *****************************************************************************
/* Function:
    bool TWIx_Write(uint16_t address, uint8_t *pdata, uint8_t length)
	
   Summary:
    Writes data onto the slave.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWIx_TRBTransfer.
	Minimum one TRB should be available.

   Parameters:
    address - 7-bit / 10-bit slave address.
	pdata   - pointer to source data buffer
	length  - length of data buffer in number of bytes.
	
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.
*/

bool TWI${INDEX?string}_Write(uint16_t address, uint8_t *pdata, uint8_t length)
{
    // Build Write TRB
    if ( !TWI${INDEX?string}_WriteTRBBuild( address, pdata, length ) )
	{
	    return false;
	}
	
	// Initiate transfer
	if ( !TWI${INDEX?string}_TRBTransfer( ) )
	{
	    return false;
	}
	
	return true;
}

// *****************************************************************************
/* Function:
    bool TWIx_WriteRead(uint16_t address, uint8_t *wdata, uint8_t wlength, uint8_t *rdata, uint8_t rlength)
	
   Summary:
    Write and Read data from Slave.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.
	The transfer status should not be busy before calling TWIx_TRBTransfer.
	Minimum two TRB's should be available.

   Parameters:
    address - 7-bit / 10-bit slave address.
	wdata   - pointer to write data buffer
	wlength - write data length in bytes.
	rdata   - pointer to read data buffer.
	rlength - read data length in bytes.
  
   Returns:
    true  - TRB submitted Successfully.
	false - Failure while submitting TRB.
*/

bool TWI${INDEX?string}_WriteRead(uint16_t address, uint8_t *wdata, uint8_t wlength, uint8_t *rdata, uint8_t rlength)
{
    // Build Write TRB
    if ( !TWI${INDEX?string}_WriteTRBBuild( address, wdata, wlength ) )
	{
	    return false;
	}
	
	// Build Read TRB
	if ( !TWI${INDEX?string}_ReadTRBBuild( address, rdata, rlength ) )
	{
	    return false;
	}
	
	// Initiate transfer
	if ( !TWI${INDEX?string}_TRBTransfer( ) )
	{
	    return false;
	}
	
	return true;
}

// *****************************************************************************
/* Function:
    TWI_TRANSFER_STATUS TWIx_TransferStatusGet(void)
	
   Summary:
    Returns the transfer status associated with the given TWI peripheral instance.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.

   Parameters:
    None.
	
   Returns:
    Status of the transfer.
*/

TWI_TRANSFER_STATUS TWI${INDEX?string}_TransferStatusGet(void)
{
    return twi${INDEX?string}Obj.status;
}

// *****************************************************************************
/* Function:
    void TWIx_CallbackRegister(TWI_CALLBACK callback, uintptr_t contextHandle)
	
   Summary:
    Sets the pointer to the function (and it's context) to be called when the 
    given TWI's transfer events occur.

   Precondition:
    TWIx_Initialize must have been called for the associated TWI instance.

   Parameters:
    callback - A pointer to a function with a calling signature defined 
	by the TWI_CALLBACK data type.

    context - A value (usually a pointer) passed (unused) into the function 
	identified by the callback parameter.
  
   Returns:
    None.
*/

void TWI${INDEX?string}_CallbackRegister(TWI_CALLBACK callback, uintptr_t contextHandle)
{
    if (callback == NULL)
	{
	    return;
	}
	
	twi${INDEX?string}Obj.callback = callback;
	twi${INDEX?string}Obj.context = contextHandle;
}

// *****************************************************************************
/* Function:

   Summary:

   Description:

   Precondition:

   Parameters:
  
   Returns:

   Remarks:
*/

void TWI${INDEX?string}_InterruptHandler(void)
{
    uint32_t status;
	static uint32_t currentTRB = 0;
	TWI_TRANSACTION_REQUEST_BLOCK * trb;
	
	// check if transfer is initiated
    if ( twi${INDEX?string}Obj.state == TWI_STATE_IDLE )
	{
	    return;
	}
	
	// Minimum one filled TRB must be available
	if ( twi${INDEX?string}Obj.numTRBs == 0 )
	{
	    return;
	}
	
	// Read the peripheral status
	status = TWI${INDEX?string}_Module->TWI_SR.w;
	
	/* checks if Slave has Nacked */
    if( status & TWI_SR_NACK_Msk ) 
    {
        twi${INDEX?string}Obj.state = TWI_STATE_ERROR;
    }

    /* checks if the arbitration is lost in multi-master scenario */
    if( status & TWI_SR_ARBLST_Msk )
    {
        /* Re-initiate the transfer if arbitration is lost in 
         * between of the transfer 
         */
        twi${INDEX?string}Obj.state = TWI_STATE_ADDR_SEND;
    }
	
	trb = &twi${INDEX?string}TRBsList[currentTRB];
	
    switch( twi${INDEX?string}Obj.state )
	{	
		case TWI_STATE_TRANSFER_READ:
		{
		    /* checks if master has received the data */
            if( status & TWI_SR_RXRDY_Msk )
            {
			    trb->length --;
				
                if( 1 == trb->length )
                {
				    // check for last TRB
                    if( currentTRB == (twi${INDEX?string}Obj.numTRBs - 1) )
                    {
                        // Send Stop before last byte is received
                        TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_STOP_Msk;
                    }
					// not the last TRB
                    else
                    {
                        // Send a Repeated Start
                        TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_START_Msk;
                    }
                }

                /* read the received data */
                *(trb->pbuffer++) = TWI${INDEX?string}_Module->TWI_RHR.RXDATA;
                
                /* checks if transmission has reached at the end */
                if( 0 == trb->length )
                {
				    // check for last TRB
                    if( currentTRB == (twi${INDEX?string}Obj.numTRBs - 1) )
                    {
                        /* read the module status again to know if 
                           tranmission complete flag is set */
                        status = TWI${INDEX?string}_Module->TWI_SR.w;
                        if( status & TWI_SR_TXCOMP_Msk )
                        {
                            twi${INDEX?string}Obj.state = TWI_STATE_TRANSFER_DONE;					
                        }
                        else
                        {
                            twi${INDEX?string}Obj.state = TWI_STATE_WAIT_FOR_TXCOMP;    
                        }
                    }
					// not the last TRB
                    else
                    {
                        twi${INDEX?string}Obj.state = TWI_STATE_TRANSFER_DONE;
                    }
                    
                    /* Disable the RXRDY interrupt*/
                    TWI${INDEX?string}_Module->TWI_IDR.w = TWI_IDR_RXRDY_Msk;
                }
			}
		    break;
		}
		
		case TWI_STATE_TRANSFER_WRITE:
		{
		    /* checks if master is ready to transmit */
            if( status & TWI_SR_TXRDY_Msk )
            {
                /* byte by byte data transmit */
                TWI${INDEX?string}_Module->TWI_THR.w = TWI_THR_TXDATA(*(trb->pbuffer++));
                trb->length--;
                
                if( 0 == trb->length )
				{
				    // check for last TRB
                    if( currentTRB == (twi${INDEX?string}Obj.numTRBs - 1))
                    {
                        // Sends a stop bit
                        TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_STOP_Msk;

                        /* read the module status again to know if 
                           tranmission complete flag is set */
                        status = TWI${INDEX?string}_Module->TWI_SR.w;
                        if( status & TWI_SR_TXCOMP_Msk )
                        {
                            twi${INDEX?string}Obj.state = TWI_STATE_TRANSFER_DONE;
                        }
                        else
                        {
                            twi${INDEX?string}Obj.state = TWI_STATE_WAIT_FOR_TXCOMP;    
                        }
                    }
					// not the last TRB
                    else
                    {
                        twi${INDEX?string}Obj.state = TWI_STATE_TRANSFER_DONE;
                    }
                    
                    // Disable the RXRDY interrupt
                    TWI${INDEX?string}_Module->TWI_IDR.w = TWI_IDR_TXRDY_Msk;
				}
			}

		    break;
		}
		
		case TWI_STATE_WAIT_FOR_TXCOMP:
		{
		    if( status & TWI_SR_TXCOMP_Msk )
            {
                twi${INDEX?string}Obj.state = TWI_STATE_TRANSFER_DONE;					
            }
		    break;
		}
		
		default:
		{
		    break;
		}
	}
	
	/* Check for error during transmission */
    if( TWI_STATE_ERROR == twi${INDEX?string}Obj.state )
    {
	    twi${INDEX?string}Obj.status = TWI_TRANSFER_ERROR;
		
		if ( twi${INDEX?string}Obj.callback != NULL )
		{
		    twi${INDEX?string}Obj.callback( twi${INDEX?string}Obj.status, twi${INDEX?string}Obj.context );
		}
		
		// Reset the PLib objects and Interrupts
		twi${INDEX?string}Obj.numTRBs = 0;
		currentTRB = 0;
        twi${INDEX?string}Obj.state = TWI_STATE_IDLE;
        TWI${INDEX?string}_Module->TWI_IDR.w = TWI_IDR_TXCOMP_Msk | 
                                 TWI_IDR_TXRDY_Msk  |
                                 TWI_IDR_RXRDY_Msk;
	}
	
	// check for completion of transfer
	if( TWI_STATE_TRANSFER_DONE  == twi${INDEX?string}Obj.state )
	{
	    // Call callback on completion of last TRB.
	    if ( currentTRB == (twi${INDEX?string}Obj.numTRBs - 1) )
		{
		    twi${INDEX?string}Obj.status = TWI_TRANSFER_SUCCESS;
			
			if ( twi${INDEX?string}Obj.callback != NULL )
		    {
		        twi${INDEX?string}Obj.callback( twi${INDEX?string}Obj.status, twi${INDEX?string}Obj.context );
		    }
			
			// Reset the PLib objects and Interrupts
			twi${INDEX?string}Obj.numTRBs = 0;
            currentTRB = 0;
            twi${INDEX?string}Obj.state = TWI_STATE_IDLE;
            TWI${INDEX?string}_Module->TWI_IDR.w = TWI_IDR_TXCOMP_Msk | 
                                     TWI_IDR_TXRDY_Msk  |
                                     TWI_IDR_RXRDY_Msk;

			return;
		}
		
        currentTRB ++;
		twi${INDEX?string}Obj.state = TWI_STATE_ADDR_SEND;   
	}
    
    if( TWI_STATE_ADDR_SEND  == twi${INDEX?string}Obj.state )
    {
        trb = &twi${INDEX?string}TRBsList[currentTRB];
        
        TWI${INDEX?string}_Module->TWI_MMR.w = 0;
        
        // 10-bit Slave Address
        if( trb->address > 0x007F)
        {
            TWI${INDEX?string}_Module->TWI_MMR.w = TWI_MMR_DADR((trb->address & 0x00007F00) >> 8) | 
                                                   TWI_MMR_IADRSZ(1);

            // Set internal address
            TWI${INDEX?string}_Module->TWI_IADR.w = TWI_IADR_IADR( trb->address & 0x000000FF );
        }
        // 7-bit Slave Address
        else
        {
            TWI${INDEX?string}_Module->TWI_MMR.w = TWI_MMR_DADR(trb->address) | 
                                                   TWI_MMR_IADRSZ(0);
        }

        if( trb->read )
        {
            TWI${INDEX?string}_Module->TWI_MMR.w |= TWI_MMR_MREAD_Msk; 

            // Send a START Condition
            TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_START_Msk;

            if( 1 == trb->length )
            {
                if( currentTRB == (twi${INDEX?string}Obj.numTRBs - 1) )
                {
                    /* Send Stop at the same time as start 
                     * if size of data to be received is 1*/
                    TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_STOP_Msk;
                }
                else
                {
                    // Send a Repeated Start
                    TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_START_Msk;
                }
            }

            twi${INDEX?string}Obj.state = TWI_STATE_TRANSFER_READ;
            TWI${INDEX?string}_Module->TWI_IDR.w = TWI_IDR_TXRDY_Msk;
            TWI${INDEX?string}_Module->TWI_IER.w = TWI_IER_RXRDY_Msk;
        }
        else
        {
            if( currentTRB > 0 )
            {
                // Send a Repeated Start
                TWI${INDEX?string}_Module->TWI_CR.w = TWI_CR_START_Msk;
            }
            
            twi${INDEX?string}Obj.state = TWI_STATE_TRANSFER_WRITE;
            TWI${INDEX?string}_Module->TWI_IDR.w = TWI_IDR_RXRDY_Msk;
            TWI${INDEX?string}_Module->TWI_IER.w = TWI_IER_TXRDY_Msk;
        }
    }
	
	return;
}	

/*******************************************************************************
 End of File
*/
