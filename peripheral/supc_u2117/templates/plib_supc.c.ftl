/*******************************************************************************
  Supply Controller(SUPC${SUPC_INDEX}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_supc${SUPC_INDEX}.c

  Summary
    SUPC${SUPC_INDEX} PLIB Implementation File.

  Description
    This file defines the interface to the SUPC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

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

#include "device.h"
#include "plib_supc${SUPC_INDEX}.h"

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

SUPC_BODVDD_CALLBACK_OBJ supc${SUPC_INDEX}CallbackObject;

// *****************************************************************************
// *****************************************************************************
// Section: SUPC${SUPC_INDEX} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void SUPC${SUPC_INDEX}_Initialize( void );

  Summary:
    Initializes given instance of SUPC peripheral.

  Description:
    This function initializes given instance of SUPC peripheral of the device
    with the values configured in MHC GUI.

  Remarks:
    plib_supc${SUPC_INDEX}.h for usage information.
*/

void SUPC${SUPC_INDEX}_Initialize( void )
{
    /* Clear all flags */
    SUPC_REGS->INTFLAG = SUPC_INTFLAG_Msk;

    <#if SUPC_BODVDD_ACTCFG = "Sampling Mode" || SUPC_BODVDD_STDBYCFG = "Sampling Mode">
    /* Configure Brown out detector prescaler & standby/active mode */
    <@compress single_line=true>SUPC_REGS->BODVDD |= SUPC_BODVDD_PSEL_${SUPC_BODVDD_PSEL}
                                                        ${SUPC_BODVDD_RUNSTDBY?then('| SUPC_BODVDD_RUNSTDBY_Msk', '')}
                                                        ${(SUPC_BODVDD_ACTCFG?starts_with("Sampling"))?then('| SUPC_BODVDD_ACTCFG_Msk', '')}
                                                        ${(SUPC_BODVDD_STDBYCFG?starts_with("Sampling"))?then('| SUPC_BODVDD_STDBYCFG_Msk', '')};</@compress>
    <#else>
    /* Configure Brown out detector standby sleep mode */
    SUPC_REGS->BODVDD |= SUPC_BODVDD_RESETVALUE ${SUPC_BODVDD_RUNSTDBY?then('| SUPC_BODVDD_RUNSTDBY_Msk', '')};
    </#if>

    /* Configure voltage regulator standby sleep mode */
    SUPC_REGS->VREG |= SUPC_VREG_RESETVALUE ${(SUPC_VREG_RUNSTDBY?starts_with("Normal"))?then('| SUPC_VREG_RUNSTDBY_Msk', '')};

    /* Enable BODVDD detect interrupt */
    SUPC_REGS->INTENSET = SUPC_INTFLAG_BODVDDDET_Msk;

    /* Configure VREF reference, level, availability */
    <@compress single_line=true>SUPC_REGS->VREF = SUPC_VREF_SEL_${SUPC_VREF_SEL}
                                                     ${SUPC_VREF_VREFOE?then('| SUPC_VREF_VREFOE_Msk', '')}
                                                     ${(SUPC_VREF_RUNSTDBY?starts_with("Available"))?then('| SUPC_VREF_RUNSTDBY_Msk', '')}
                                                     ${(SUPC_VREF_ONDEMAND?starts_with("Only"))?then('| SUPC_VREF_ONDEMAND_Msk', '')};</@compress>
}

// *****************************************************************************
/* Function:
    void SUPC${SUPC_INDEX}_VoltageRegulatorEnable( bool enable );

  Summary:
    Enable/Disable voltage regulator.

  Description:
    This function will enable or disable the main voltage regulator.

  Remarks:
    plib_supc${SUPC_INDEX}.h for usage information.
*/

void SUPC${SUPC_INDEX}_VoltageRegulatorEnable( bool enable )
{
    if(enable == true)
    {
        /* Enable voltage regulator */
        SUPC_REGS->VREG |= SUPC_VREG_ENABLE_Msk;
    }
    else
    {
        /* Disable voltage regulator */
        SUPC_REGS->VREG &= ~SUPC_VREG_ENABLE_Msk;
    }
}

// *****************************************************************************
/* Function:
    void SUPC${SUPC_INDEX}_BODVDDCallbackRegister( SUPC_BODVDD_CALLBACK callback,
                                                    uintptr_t context );

  Summary:
    Registers the function to be called when a Brown Out Event has occurred.

  Description
    This function registers the callback function to be called when a Brown Out
    event has occurred. Note that the callback function will be called only if
    the BODVDD action setting in NVM User Row is configured to generate an
    interrupt and not reset the system.

  Remarks:
    plib_supc${SUPC_INDEX}.h for usage information.
*/

void SUPC${SUPC_INDEX}_BODVDDCallbackRegister( SUPC_BODVDD_CALLBACK callback, uintptr_t context )
{
    supc${SUPC_INDEX}CallbackObject.callback = callback;

    supc${SUPC_INDEX}CallbackObject.context = context;
}

// *****************************************************************************
/* Function:
    void SUPC${SUPC_INDEX}_InterruptHandler( void );

  Summary:
    SUPC interrupt handler for BODVDD event action.

  Description
    This function will trigger BODVDD callback.

  Remarks:
    None.
*/

void SUPC${SUPC_INDEX}_InterruptHandler( void )
{
    if ((SUPC_REGS->INTFLAG & SUPC_INTFLAG_BODVDDDET_Msk) == SUPC_INTFLAG_BODVDDDET_Msk)
    {
        if (supc${SUPC_INDEX}CallbackObject.callback != NULL)
        {
            supc${SUPC_INDEX}CallbackObject.callback(supc0CallbackObject.context);
        }

        SUPC_REGS->INTFLAG = SUPC_INTFLAG_BODVDDDET_Msk;
    }
}
