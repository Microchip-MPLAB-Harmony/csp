/*******************************************************************************
  Digital-to-Analog Converter (DAC) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_dac.h

  Summary:
    DAC PLIB Header file

  Description:
    This file defines the interface to the DAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.
    The 'x' be replaced with DAC plib index.
*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_DACx_H
#define PLIB_DACx_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
    this interface.
*/

// *****************************************************************************
/* Function:
    void DACx_Initialize(void)

  Summary:
    Initializes given instance of the DAC peripheral.

  Description:
    This function initializes the given instance of the DAC peripheral as
    configured by the user within the MHC.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        DACx_Initialize();
    </code>

  Remarks:
    Calling this function will stop the DAC if it was already running and
    reinitializes it.
*/

void DACx_Initialize(void);

// *****************************************************************************
/* Function:
    void DACx_DataWrite(uint16_t data)

  Summary:
    This function will write the specified value to the DAC and start the
    conversion.

  Description:
    This function will write the specified value to the DAC and start the
    conversion. The internal and/or external DAC outputs will be updated if
    these output were enabled.  The analog output voltage will depend on the
    choice of the DAC reference (configured via MHC). This function should only
    be called when the DACx_IsReady() returns true. Calling this function when
    the DAC is not ready will result in the in-determinate operation. 

  Precondition:
    DACx_Initialize must have been called for the associated DAC instance. 
    The DACx_IsReady() function should have returned true.

  Parameters:
    data - Digital value to be converted. 

  Returns:
    None.

  Example:
    <code>
        DACx_Initialize();
        if(DACx_IsReady() == true)
        {
            DACx_DataWrite(data);
        }
    </code>

  Remarks:
    None.
*/

void DACx_DataWrite(uint16_t data);

// *****************************************************************************
/* Function:
    bool DACx_IsReady(void);

  Summary:
    Checks whether DAC is ready for receiving next sample value.

  Description:
    This function checks for the readiness of the DAC to receive the next sample
    value. The application should call the DACx_DataWrite() function only when
    this function returns true. Calling the DACx_DataWrite() function when this
    function returns false will result in in-determinate operation.

  Precondition:
    DACx_Initialize must have been called for the associated DAC instance.

  Parameters:
    None.

  Returns:
    true  - Ready for receiving next sample value for conversion.
    false - DAC is BUSY. Not ready for receiving next sample value.

  Example:
    <code>
        DACx_Initialize();
        if (DACx_IsReady())
        {
            DACx_DataWrite(0xFF);
        }
        else
        {
            // Not ready to accept new conversion request.
            // User Application code.
        }
    </code>

  Remarks:
    None.
*/

bool DACx_IsReady(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_DACx_H */
