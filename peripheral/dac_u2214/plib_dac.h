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
Copyright (c) 2017 released Microchip Technology Inc. All rights reserved.

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
    DACx_Initialize and DACx_InternalOutputEnable or DACx_ExternalOutputEnable
    must have been called for the associated DAC instance. The DACx_IsReady()
    function should have returned true.

  Parameters:
    data - Digital value to be converted. 

  Returns:
    None.

  Example:
    <code>
        DACx_Initialize();
        DACx_ExternalOutputEnable(true);
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
    DACx_Initialize and DACx_InternalOutputEnable or DACx_ExternalOutputEnable
    must have been called for the associated DAC instance.

  Parameters:
    None.

  Returns:
    true  - Ready for receiving next sample value for conversion.
    false - DAC is BUSY. Not ready for receiving next sample value.

  Example:
    <code>
        DACx_Initialize();
        DACx_ExternalOutputEnable(true);
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

// *****************************************************************************
/* Function:
    void DACx_ExternalOutputEnable ( bool enable )

  Summary:
    Enable/Disable the external DAC output.

  Description:
    This function allows the application to enables and disable the external DAC
    output.

  Precondition:
    DACx_Initialize must have been called for the associated DAC instance.

  Parameters:
    true  - Enable external DAC output.
    false - Disable external DAC output.

  Returns:
    None.

  Example:
    <code>
        DACx_Initialize();
        DACx_ExternalOutputEnable(True);
    </code>

  Remarks:
    None.
*/

void DACx_ExternalOutputEnable ( bool enable );

// *****************************************************************************
/* Function:
    void DACx_InternalOutputEnable ( bool enable )

  Summary:
    Enable/Disable the internal DAC output.

  Description:
    This function allows the application to enable and disable the internal DAC
    output to the Analog Comparator, ADC and the SDADC peripherals.

  Precondition:
    DACx_Initialize must have been called for the associated DAC instance.

  Parameters:
    true  - Enable internal DAC output.
    false - Disable internal DAC output.

  Returns:
    None.

  Example:
    <code>
        DACx_Initialize();
        DACx_InternalOutputEnable(True);
    </code>

  Remarks:
    None.
*/

void DACx_InternalOutputEnable ( bool enable );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_DACx_H */
