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