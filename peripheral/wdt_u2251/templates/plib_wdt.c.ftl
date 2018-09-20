/*******************************************************************************
  Watchdog Timer PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${WDT_INSTANCE_NAME?lower_case}.c

  Summary:
    Interface definition of ${WDT_INSTANCE_NAME} PLIB.

  Description:
    This file defines the interface for the WDT Plib.
    It allows user to setup timeout duration and restart watch dog timer.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2016 released Microchip Technology Inc. All rights reserved.
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_${WDT_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

<#if WDT_EW_ENABLE = true>
// *****************************************************************************
/* WDT Callback Object

  Summary:
    Defines the data type for the data structures used for peripheral
    operations.

  Description:
    This may be for used for peripheral operations.

  Remarks:
    None.
*/
typedef struct
{
    WDT_CALLBACK      callback;

    uintptr_t         context;

} WDT_CALLBACK_OBJECT ;

WDT_CALLBACK_OBJECT ${WDT_INSTANCE_NAME?lower_case}CallbackObj;
</#if>

// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_Initialize( void )

  Summary:
    Initializes given instance of the WDT peripheral.

  Description:
    This function initializes the given instance of the WDT peripheral as
    configured by the user from within the MCC.

  Remarks:
    Refer plib_${WDT_INSTANCE_NAME?lower_case}.h file for more information.
*/

void ${WDT_INSTANCE_NAME}_Initialize( void )
{
    /* Empty Implementation */
}

// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_Enable( void )

  Summary:
    Enables the WDT peripheral.

  Description:
    This function enables the WDT peripheral. Calling this function will cause
    the WDT to start counting up to the configured timeout value.

  Remarks:
    Refer plib_${WDT_INSTANCE_NAME?lower_case}.h file for more information.
*/

void ${WDT_INSTANCE_NAME}_Enable( void )
{
    /* Checking if Always On Bit is Enabled */
    if((WDT_REGS->WDT_CTRLA & WDT_CTRLA_ALWAYSON_Msk) != WDT_CTRLA_ALWAYSON_Msk)
    {
        /* Enable Watchdog */
        WDT_REGS->WDT_CTRLA |= WDT_CTRLA_ENABLE_Msk;

        while((WDT_REGS->WDT_SYNCBUSY & WDT_SYNCBUSY_ENABLE_Msk) == WDT_SYNCBUSY_ENABLE_Msk)
        {
            /* Wait for synchronization */
        }
    }

<#if WDT_EW_ENABLE = true>
    /* Enable early warning interrupt */
    WDT_REGS->WDT_INTENSET |= WDT_INTENSET_EW_Msk;
</#if>
}

// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_Disable( void )

  Summary:
    Disables the WDT peripheral.

  Description:
    This function is used to stop the WDT counter and disable WDT peripheral.

  Remarks:
    Refer plib_${WDT_INSTANCE_NAME?lower_case}.h file for more information.
*/

void ${WDT_INSTANCE_NAME}_Disable( void )
{
    /* Disable Watchdog */
    WDT_REGS->WDT_CTRLA &= ~(WDT_CTRLA_ENABLE_Msk);

<#if WDT_EW_ENABLE = true>
    /* Disable Early Watchdog Interrupt */
    WDT_REGS->WDT_INTENCLR = WDT_INTENCLR_EW_Msk;
</#if>
}

// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_Clear( void )

  Summary:
    Restarts the WDT counter.

  Description:
    This function is used to restart the WDT counter to avoid timeout. Calling
    this will clear the WDT timeout counter and restart the counting from 0.
    Failure to call this function before the WDT timeout period will cause the
    system to reset.

  Remarks:
    Refer plib_${WDT_INSTANCE_NAME?lower_case}.h file for more information.
*/

void ${WDT_INSTANCE_NAME}_Clear( void )
{
    /* Clear WDT and reset the WDT timer before the
       timeout occurs */
    WDT_REGS->WDT_CLEAR = WDT_CLEAR_CLEAR_KEY;
}

<#if WDT_EW_ENABLE = true>
// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_CallbackRegister( WDT_CALLBACK callback,
                                           uintptr_t context )

  Summary:
    Sets the pointer to the function (and it's context) to be called when the
    Timeout events occur.

  Description:
    This function sets the pointer to a client function to be called "back" when
    the WDT Early Warning event occurs. It also passes a context value that is
    passed into the callback function when it is called.  This function is
    available only if the Early Warning option (in MHC) is enabled at the time
    of generating the peripheral library.

    The time at which the Early warning interrupt occurs is defined by the Early
    Warning setting in the NVM User row. This is configured by using the
    compiler provided fuse options. Specifying the Early Warning offset to be
    larger than the WDT time out value will cause the Early Warning mechanism to
    be in-active.

Remarks:
    Refer plib_${WDT_INSTANCE_NAME?lower_case}.h file for more information.
*/

void ${WDT_INSTANCE_NAME}_CallbackRegister( WDT_CALLBACK callback, uintptr_t context)
{
    ${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback = callback;

    ${WDT_INSTANCE_NAME?lower_case}CallbackObj.context = context;
}

// *****************************************************************************
/* Function:
    void ${WDT_INSTANCE_NAME}_InterruptHandler( void )

  Summary:
    WDT Interrupt Handler.

  Description:
    This function handles all the interrupts evoked in the WDT module.

  Remarks:
    None.
*/

void ${WDT_INSTANCE_NAME}_InterruptHandler( void )
{
    /* Clear Early Watchdog Interrupt */
    WDT_REGS->WDT_INTFLAG = WDT_INTFLAG_EW_Msk;

    if( ${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback != NULL )
    {
        ${WDT_INSTANCE_NAME?lower_case}CallbackObj.callback(${WDT_INSTANCE_NAME?lower_case}CallbackObj.context);
    }
}
</#if>
