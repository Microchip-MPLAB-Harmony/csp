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

#ifndef PLIB_SHDWC_H
#define PLIB_SHDWC_H


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
    int void SHDWC_Initialize(void)

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
    SHDWC_Initialize();
    </code>

*/

void SHDWC_Initialize(void);


// *****************************************************************************
/* Function:
    void SHDWC_Shutdown(void)

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
    SHDWC_Shutdown();
    </code>

*/

void SHDWC_Shutdown(void);

// *****************************************************************************
/* Function:
   uint32_t SHDWC_GetWakeup(void)

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
    uint32_t wakeupEvents = SHDWC_GetWakeup(void);
    if (wakeupEvenets & SHDW_SR_RTCWK_Msk) {
        //Handle RTC wake-up event 
    }
    </code>

*/

uint32_t SHDWC_GetWakeup(void);


#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

#endif // PLIB_SHDWC_H

/*******************************************************************************
 End of File
*/

