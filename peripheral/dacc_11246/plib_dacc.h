/*******************************************************************************
  Digital-to-Analog Converter Controller (DACC) Peripheral Library(PLIB) 
  Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_dacc.h

  Summary
    DACC peripheral library interface.

  Description
    This file defines the interface to the DACC peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

  Remarks:
    This header is for documentation only.  The actual dacc<x> headers will be
    generated as required by the MCC (where <x> is the peripheral instance 
    number).

    Every interface symbol has a lower-case 'x' in it following the "DACC" 
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third-party product
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

#ifndef PLIB_DACCx_H    // Guards against multiple inclusion
#define PLIB_DACCx_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END


// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/*  The following data type definitions are used by the functions in this 
    interface and should be considered part it.
*/

// *****************************************************************************
/* DACC Channel Index

  Summary:
    Identifies the Channel index of DACC module.

  Description:
    This data type identifies the Channel index of DACC module.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/

typedef enum
{
    /* Channel 0 */
    DACC_CHANNEL_0, 
            
    /* Channel 1 */
    DACC_CHANNEL_1         
        
} DACC_CHANNEL_NUM

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
    void DACCx_Initialize (void)

   Summary:
     Initializes given instance of the DACC peripheral.

   Description:
     This function initializes the given instance of the DACC peripheral as
     configured in MCC.  

   Precondition:
     None.

   Parameters:
    None.
  
   Returns:
    None.

   Example:
    <code>
    DACC0_Initialize();
    </code>

   Remarks:
    None.
*/

void DACCx_Initialize (void);

// *****************************************************************************
/* Function:
    bool DACCx_IsReady (DACC_CHANNEL_NUM channel)

   Summary:
    Checks whether DACC is ready to accecpt new conversion request or not.

   Description:
    This function checks whether DACC is ready to accecpt new conversion request
    or not. 
    
   Precondition:
    DACCx_Initialize must have been called for the associated DACC instance.

   Parameters:
    channel   - Points to DACC Channel.
  
   Returns:
    true      - When DACC is ready to accept new conversion request.
    false     - When DACC is not ready to accept new conversion request.

  Example:
    <code>
    
    bool status = false;

    if (true == DACC0_IsReady (DACC_CHANNEL_1))
    {
       DACC0_DataWrite (DACC_CHANNEL_1, 0xff) 
    }
    else
    {
       //DACC is not ready to accept new conversion request
       //User Application code
    }
    
    </code>

  Remarks:
    None.
*/

bool DACCx_IsReady (DACC_CHANNEL_NUM channel);

// *****************************************************************************
/* Function:
    void DACCx_DataWrite (DACC_CHANNEL_NUM channel, uint32_t data)

   Summary:
    Converts a Digital data to Analog value.

   Description:
    This function converts a Digital data to Analog value.
    The behavior of this function call will vary based on the mode selected 
    within MCC.
    This function call is always blocking. 
    
   Precondition:
    DACCx_Initialize must have been called for the associated DACC instance.

   Parameters:
    channel - Channel number
    data    - Digital data to be converted to Analog value.
  
   Returns:
    None

  Example:
    <code>
    //Example to use in polled and blocking mode
    char myData[COUNT] = {"0xff","0x3E","0x7A","0x3F"};//COUNT is user dependent
    bool status = false;
    
    //considering count=4
    for (uint8_t i = 0; i<4; i++)
    {
       DACC0_DataWrite (DACC_CHANNEL_0, myData[i]);
    }
    
    </code>

  Remarks:
    None.
*/
void DACCx_DataWrite (DACC_CHANNEL_NUM channel, uint32_t data);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif //PLIB_DACCx_H

/**
 End of File
*/

