/*******************************************************************************
  SHDWC PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_shdwc.c

  Summary:
    Shutdown Controller PLIB

  Description:
    Shutdown Controller PLIB Implementation
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

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

#ifndef PLIB_${SHDWC_INSTANCE_NAME}_H
#define PLIB_${SHDWC_INSTANCE_NAME}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/


#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif


// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
/* Function:
    int void ${SHDWC_INSTANCE_NAME}_Initialize(void)

  Summary:
    Initialize shutdown controller.

  Description:
    Initialize shutdown controller by enabling configured wake-up events.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.

  Example:
    <code>
    ${SHDWC_INSTANCE_NAME}_Initialize();
    </code>

*/

void ${SHDWC_INSTANCE_NAME}_Initialize(void);


// *****************************************************************************
/* Function:
    void ${SHDWC_INSTANCE_NAME}_Shutdown(void)

  Summary:
    Assert the shutdown signal.

  Description:
    Assert the shutdown signal and enter low-power mode.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    None.

  Example:
    <code>
    ${SHDWC_INSTANCE_NAME}_Shutdown();
    </code>

*/

void ${SHDWC_INSTANCE_NAME}_Shutdown(void);

// *****************************************************************************
/* Function:
   uint32_t ${SHDWC_INSTANCE_NAME}_GetWakeup(void)

  Summary:
    Read and clear the status register.

  Description:
    Reads the cause of the wake-up.  Since multiple wake-up events can occur
    before this register is read a bitmask is returned rather than a single
    enumerated value.

  Precondition:
    None.

  Parameters:
    None.
  
  Returns:
    A bitmask of all wake-up events that occured since the last read of the status
    register.

  Example:
    <code>
    uint32_t wakeupEvents = ${SHDWC_INSTANCE_NAME}_GetWakeup(void);
    if (wakeupEvenets & SHDW_SR_RTCWK_Msk) {
        //Handle RTC wake-up event 
    }
    </code>

*/

uint32_t ${SHDWC_INSTANCE_NAME}_GetWakeup(void);


#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

#endif // PLIB_${SHDWC_INSTANCE_NAME}_H

/*******************************************************************************
 End of File
*/

