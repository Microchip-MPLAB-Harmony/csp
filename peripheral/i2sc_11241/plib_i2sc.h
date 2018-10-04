/*******************************************************************************
  I2SC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_i2sc.h

  Summary:
    I2SC PLIB Header File for documentation

  Description:
    This library provides documentation of all the interfaces which can be used
    to control and interact with an instance of an Inter-IC Sound Controller (I2SC).
    This file must not be included in any MPLAB Project.
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

// *****************************************************************************
/* Function:
    void I2SCx_Initialize (void);
    
  Summary:
    Initializes I2SCx module of the device
    
  Description:
    This function initializes I2SCx module of the device with the values
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
        I2SC0_Initialize();
    </code>
    
  Remarks:
    This function must be called only once and before any other I2SC function is
    called.                                            
*/
void I2SCx_Initialize (void);

// *****************************************************************************
/* Function:
    uint32_t I2SCx_LRCLK_Get(void);
    
  Summary:
    Get the level of the I2S LRCLK (left/right clock) signal
    
  Description:
    This function returns the state of the I2S LRCLK (left/right clock) signal.
    In the case where this signal is generated from a codec or other external
    source, this allows the caller to synchronize itself to the LRCLK signal.
  
  Precondition:
    None.
  
  Parameters:
    None.
  
  Returns:
    State of the LRCLK pin for the I2SCx module -- 1 if high, 0 if low
    
  Example:
    <code>
        I2SC1_LRCLK_Get();
    </code>
    
  Remarks:
    None.                                            
*/
uint32_t I2SCx_LRCLK_Get(void);
