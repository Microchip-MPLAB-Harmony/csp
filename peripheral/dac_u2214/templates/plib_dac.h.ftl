/*******************************************************************************
  Digital-to-Analog Converter (DAC${DAC_INDEX}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_dac${DAC_INDEX}.h

  Summary:
    DAC${DAC_INDEX} PLIB Header file

  Description:
    This file defines the interface to the DAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#ifndef PLIB_DAC${DAC_INDEX}_H
#define PLIB_DAC${DAC_INDEX}_H

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
    void DAC${DAC_INDEX}_Initialize(void)

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
        DAC${DAC_INDEX}_Initialize();
    </code>

  Remarks:
    Stops the DAC if it was already running and reinitializes it.
*/

void DAC${DAC_INDEX}_Initialize(void);

// *****************************************************************************
/* Function:
    void DAC${DAC_INDEX}_DataWrite(uint16_t data)

  Summary:
    This function will write the specified value to the DAC and start the
    conversion.

  Description:
    This function will write the specified value to the DAC and start the
    conversion. The internal and/or external DAC outputs will be updated if
    these output were enabled.  The analog output voltage will depend on the
    choice of the DAC reference (configured via MHC). This function should only
    be called when the DAC${DAC_INDEX}_IsReady() returns true. Calling this 
    function when the DAC is not ready will result in the in-determinate 
    operation. 

  Precondition:
    DAC${DAC_INDEX}_Initialize must have been called for the associated DAC 
    instance. The DAC${DAC_INDEX}_IsReady() function should have returned true.

  Parameters:
    data - Digital value to be converted. 

  Returns:
    None.

  Example:
    <code>
        DAC${DAC_INDEX}_Initialize();
        if(DAC${DAC_INDEX}_IsReady() == true)
        {
            DAC${DAC_INDEX}_DataWrite(data);
        }
    </code>

  Remarks:
    None.
*/

void DAC${DAC_INDEX}_DataWrite(uint16_t data);

// *****************************************************************************
/* Function:
    bool DAC${DAC_INDEX}_IsReady(void);

  Summary:
    Checks whether DAC is ready for receiving next sample value.

  Description:
    This function checks for the readiness of the DAC to receive the next sample
    value. The application should call the DAC${DAC_INDEX}_DataWrite() function 
    only when this function returns true. Calling DAC${DAC_INDEX}_DataWrite() 
    function when this function returns false will result in in-determinate 
    operation.

  Precondition:
    DAC${DAC_INDEX}_Initialize must have been called for the associated DAC 
    instance.

  Parameters:
    None.

  Returns:
    true  - Ready for receiving next sample value for conversion.
    false - DAC is BUSY. Not ready for receiving next sample value.

  Example:
    <code>
        DAC${DAC_INDEX}_Initialize();
        if (DAC${DAC_INDEX}_IsReady())
        {
            DAC${DAC_INDEX}_DataWrite(0xFF);
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

bool DAC${DAC_INDEX}_IsReady(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_DAC${DAC_INDEX}_H */
