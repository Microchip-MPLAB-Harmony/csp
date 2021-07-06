/*******************************************************************************
  CCP Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_ccp_common.h

  Summary
    TMR peripheral library interface.

  Description
    This file defines the interface to the CCP peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_CCP_COMMON_H    // Guards against multiple inclusion
#define PLIB_CCP_COMMON_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/
#include <stddef.h>

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
    interface and should be considered part of it.
*/


// *****************************************************************************
/* CCP_TIMER_CALLBACK

  Summary:
    Use to register a callback with the TMR.

  Description:
    When a match is asserted, a callback can be activated.
    Use CCP_CALLBACK as the function pointer to register the callback
    with the match.

  Remarks:
    The callback should look like:
      void callback(handle, context);
	Make sure the return value and parameters of the callback are correct.
*/

typedef void (*CCP_TIMER_CALLBACK)(uint32_t status, uintptr_t context);

// *****************************************************************************

typedef struct
{
    /*TMR callback function happens on Period match*/
    CCP_TIMER_CALLBACK callback_fn;
    /* - Client data (Event Context) that will be passed to callback */
    uintptr_t context;

}CCP_TIMER_OBJECT;

// *****************************************************************************
/* CCP_CAPTURE_CALLBACK

  Summary:
    Use to register a callback with the TMR.

  Description:
    When a match is asserted, a callback can be activated.
    Use CCP_CAPTURE_CALLBACK as the function pointer to register the callback
    with the match.

  Remarks:
    The callback should look like:
      void callback(context);
*/

typedef void (*CCP_CAPTURE_CALLBACK)(uintptr_t context);

// *****************************************************************************

typedef struct
{
    /*TMR callback function happens on Period match*/
    CCP_CAPTURE_CALLBACK callback_fn;
    /* - Client data (Event Context) that will be passed to callback */
    uintptr_t context;

}CCP_CAPTURE_OBJECT;

// *****************************************************************************
/* CCP_COMPARE_CALLBACK

  Summary:
    Use to register a callback with the CCP Compare module.

  Description:
    When a match is asserted, a callback can be activated.
    Use CCP_COMPARE_CALLBACK as the function pointer to register the callback
    with the match.

  Remarks:
    The callback should look like:
      void callback(context);
*/

typedef void (*CCP_COMPARE_CALLBACK)(uintptr_t context);

// *****************************************************************************

typedef struct
{
    /*TMR callback function happens on comapre match*/
    CCP_COMPARE_CALLBACK callback_fn;

    /* - Client data (Event Context) that will be passed to callback */
    uintptr_t context;
}CCP_COMPARE_OBJECT;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

}

#endif
// DOM-IGNORE-END

#endif //_PLIB_TMR_COMMON_H

/**
 End of File
*/
