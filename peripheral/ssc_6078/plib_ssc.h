/*******************************************************************************
  SSC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ssc.h

  Summary:
    SSC PLIB Header File for documentation

  Description:
    This library provides documentation of all the interfaces which can be used
    to control and interact with an instance of a Serial Synchronous Controller
   (SSC).
    This file must not be included in any MPLAB Project.
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

// *****************************************************************************
/* Function:
    void SSCx_Initialize (void);
    
  Summary:
    Initializes SSCx module of the device
    
  Description:
    This function initializes SSCx module of the device with the values
    configured in MHC GUI. Once the peripheral is initialized, transfer
    APIs can be used to transfer the data.
  
  Precondition:
    MHC GUI should be configured with the right values.
  
  Parameters:
    None.
  
  Returns:
    None.
    
  Example:
    <code>
        SSC0_Initialize();
    </code>
    
  Remarks:
    This function must be called only once and before any other SSC function is
    called.                                            
*/
void SSCx_Initialize (void);
   
// *****************************************************************************
/* Function:
    void SSCx_BaudSet (const uint32_t baud);
    
  Summary:
    Changes the baud rate (samples/second) of the interface.
    
  Description:
    This function Cchanges the baud rate, or samples/second of the interface.
  
  Precondition:
    None.
  
  Parameters:
    baud          New baud rate, i.e. samples/second, e.g. 8000, 44100 or 48000
  
  Returns:
    None.
    
  Example:
    <code>
        SSCx_BaudSet(44100);
    </code>
    
  Remarks:
    None.
*/
void SSCx_BaudSet (const uint32_t baud);