/*******************************************************************
  Company:
    Microchip Technology Inc.
    Memory System Service SDRAMC Initialization File

  File Name:
    plib_sdramc0.h

  Summary:
    SDRAMC Controller (SDRAMC). 

  Description:
    The SDRAMC System Memory interface provides a simple interface to manage
    the externally connected SDRAM device. This file contains the source code
    to initialize the SDRAMC controller

 Remarks:
    This header is for documentation only.  The actual sdramc<x> headers will be
    generated as required by the MCC (where <x> is the peripheral instance 
    number).

    Every interface symbol has a lower-case 'x' in it following the "SDRAMC" 
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017-18 released Microchip Technology Inc.  All rights reserved.

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


#ifndef _PLIB_SDRAMC0_H
#define _PLIB_SDRAMC0_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

//******************************************************************************
/* Function:
    void SDRAMC0_Initialize ( void )

  Summary:
    Initializes and Enables the SDRAM Controller.

  Description:
    This function Enables the external memory controller module(s).

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.

  Example:
  <code>
    SDRAMC0_Initialize();
  </code>

  Remarks:
    This routine must be called before any attempt to access external
    memory.

    Not all features are available on all devices. Refer to the specific
	device data sheet to determine availability.
*/
void SDRAMC0_Initialize(void);

//DOM-IGNORE-BEGIN
#ifdef __cplusplus
}
#endif
//DOM-IGNORE-END

#endif // #ifndef _PLIB_SDRAMC0_H

/*******************************************************************************
 End of File
*/
