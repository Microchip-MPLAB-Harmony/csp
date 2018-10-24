/*******************************************************************************
  Supply Controller(SUPC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_supc.c

  Summary
    SUPC PLIB Implementation File.

  Description
    This file defines the interface to the SUPC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "device.h"
#include "plib_supc.h"

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************
/* SUPC Callback Object

  Summary:
    SUPC peripheral callback object.

  Description:
    This local data object holds the function signature for the SUPC peripheral
    callback function for BODVDD events.

  Remarks:
    None.
*/

typedef struct
{
    SUPC_BODVDD_CALLBACK callback;

    uintptr_t context;

} SUPC_BODVDD_CALLBACK_OBJ;

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

SUPC_BODVDD_CALLBACK_OBJ supcCallbackObject;

// *****************************************************************************
// *****************************************************************************
// Section: SUPC Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void SUPC_Initialize( void );

  Summary:
    Initializes given instance of SUPC peripheral.

  Description:
    This function initializes given instance of SUPC peripheral of the device
    with the values configured in MHC GUI.

  Remarks:
    plib_supc.h for usage information.
*/

void SUPC_Initialize( void )
{
    /* Clear all flags */
    SUPC_REGS->SUPC_INTFLAG = SUPC_INTFLAG_Msk;



    /* Enable BODVDD detect interrupt */
    SUPC_REGS->SUPC_INTENSET = SUPC_INTFLAG_BODVDDDET_Msk;

    /* Configure VREF reference, level, availability */
    SUPC_REGS->SUPC_VREF = SUPC_VREF_SEL_1V024 ;
}

// *****************************************************************************
/* Function:
    void SUPC_VoltageRegulatorEnable( bool enable );

  Summary:
    Enable/Disable voltage regulator.

  Description:
    This function will enable or disable the main voltage regulator.

  Remarks:
    plib_supc.h for usage information.
*/

void SUPC_VoltageRegulatorEnable( bool enable )
{
    if(enable == true)
    {
        /* Enable voltage regulator */
        SUPC_REGS->SUPC_VREG |= SUPC_VREG_ENABLE_Msk;
    }
    else
    {
        /* Disable voltage regulator */
        SUPC_REGS->SUPC_VREG &= ~SUPC_VREG_ENABLE_Msk;
    }
}

// *****************************************************************************
/* Function:
    void SUPC_BODVDDCallbackRegister( SUPC_BODVDD_CALLBACK callback,
                                                    uintptr_t context );

  Summary:
    Registers the function to be called when a Brown Out Event has occurred.

  Description
    This function registers the callback function to be called when a Brown Out
    event has occurred. Note that the callback function will be called only if
    the BODVDD action setting in NVM User Row is configured to generate an
    interrupt and not reset the system.

  Remarks:
    plib_supc.h for usage information.
*/

void SUPC_BODVDDCallbackRegister( SUPC_BODVDD_CALLBACK callback, uintptr_t context )
{
    supcCallbackObject.callback = callback;

    supcCallbackObject.context = context;
}

// *****************************************************************************
/* Function:
    void SUPC_InterruptHandler( void );

  Summary:
    SUPC interrupt handler for BODVDD event action.

  Description
    This function will trigger BODVDD callback.

  Remarks:
    plib_supc.h for usage information.
*/

void SUPC_InterruptHandler( void )
{
    if ((SUPC_REGS->SUPC_INTFLAG & SUPC_INTFLAG_BODVDDDET_Msk) == SUPC_INTFLAG_BODVDDDET_Msk)
    {
        if (supcCallbackObject.callback != NULL)
        {
            supcCallbackObject.callback(supcCallbackObject.context);
        }

        SUPC_REGS->SUPC_INTFLAG = SUPC_INTFLAG_BODVDDDET_Msk;
    }
}
