/*******************************************************************************
  Supply Controller(${SUPC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${SUPC_INSTANCE_NAME?lower_case}.c

  Summary
    ${SUPC_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the SUPC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_${SUPC_INSTANCE_NAME?lower_case}.h"

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

SUPC_BODVDD_CALLBACK_OBJ ${SUPC_INSTANCE_NAME?lower_case}CallbackObject;

// *****************************************************************************
// *****************************************************************************
// Section: ${SUPC_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void ${SUPC_INSTANCE_NAME}_Initialize( void );

  Summary:
    Initializes given instance of SUPC peripheral.

  Description:
    This function initializes given instance of SUPC peripheral of the device
    with the values configured in MHC GUI.

  Remarks:
    plib_${SUPC_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${SUPC_INSTANCE_NAME}_Initialize( void )
{
    /* Clear all flags */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_INTFLAG = SUPC_INTFLAG_Msk;

    <#if SUPC_BODVDD_ACTCFG == "1" || (SUPC_BODVDD_STDBYCFG == "1" && SUPC_BODVDD_RUNSTDBY == true)>
    /* Configure Brown out detector prescaler & standby/active mode */
    <@compress single_line=true>${SUPC_INSTANCE_NAME}_REGS->SUPC_BODVDD |= SUPC_BODVDD_PSEL_${SUPC_BODVDD_PSEL}
                                                          ${SUPC_BODVDD_RUNSTDBY?then('| SUPC_BODVDD_RUNSTDBY_Msk', '')}
                                                          ${(SUPC_BODVDD_ACTCFG == "1")?then('| SUPC_BODVDD_ACTCFG_Msk', '')}
                                                          ${((SUPC_BODVDD_STDBYCFG == "1") && (SUPC_BODVDD_RUNSTDBY == true))?then('| SUPC_BODVDD_STDBYCFG_Msk', '')};</@compress>
    <#else>
        <#if SUPC_BODVDD_RUNSTDBY == true>
    /* Configure Brown out detector standby sleep mode */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_BODVDD |= SUPC_BODVDD_RUNSTDBY_Msk;
        </#if>
    </#if>

    <#if SUPC_VREG_RUNSTDBY == "1">
    /* Configure voltage regulator standby sleep mode */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREG |= SUPC_VREG_RUNSTDBY_Msk;
    </#if>

    /* Enable BODVDD detect interrupt */
    ${SUPC_INSTANCE_NAME}_REGS->SUPC_INTENSET = SUPC_INTFLAG_BODVDDDET_Msk;

    /* Configure VREF reference, level, availability */
    <@compress single_line=true>${SUPC_INSTANCE_NAME}_REGS->SUPC_VREF = SUPC_VREF_SEL_${SUPC_VREF_SEL}
                                                       ${SUPC_VREF_VREFOE?then('| SUPC_VREF_VREFOE_Msk', '')}
                                                       ${(SUPC_VREF_RUNSTDBY == "1")?then('| SUPC_VREF_RUNSTDBY_Msk', '')}
                                                       ${(SUPC_VREF_ONDEMAND == "1")?then('| SUPC_VREF_ONDEMAND_Msk', '')};</@compress>
}

// *****************************************************************************
/* Function:
    void ${SUPC_INSTANCE_NAME}_VoltageRegulatorEnable( bool enable );

  Summary:
    Enable/Disable voltage regulator.

  Description:
    This function will enable or disable the main voltage regulator.

  Remarks:
    plib_${SUPC_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${SUPC_INSTANCE_NAME}_VoltageRegulatorEnable( bool enable )
{
    if(enable == true)
    {
        /* Enable voltage regulator */
        ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREG |= SUPC_VREG_ENABLE_Msk;
    }
    else
    {
        /* Disable voltage regulator */
        ${SUPC_INSTANCE_NAME}_REGS->SUPC_VREG &= ~SUPC_VREG_ENABLE_Msk;
    }
}

// *****************************************************************************
/* Function:
    void ${SUPC_INSTANCE_NAME}_BODVDDCallbackRegister( SUPC_BODVDD_CALLBACK callback,
                                                    uintptr_t context );

  Summary:
    Registers the function to be called when a Brown Out Event has occurred.

  Description
    This function registers the callback function to be called when a Brown Out
    event has occurred. Note that the callback function will be called only if
    the BODVDD action setting in NVM User Row is configured to generate an
    interrupt and not reset the system.

  Remarks:
    plib_${SUPC_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${SUPC_INSTANCE_NAME}_BODVDDCallbackRegister( SUPC_BODVDD_CALLBACK callback, uintptr_t context )
{
    ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback = callback;

    ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.context = context;
}

// *****************************************************************************
/* Function:
    void ${SUPC_INSTANCE_NAME}_InterruptHandler( void );

  Summary:
    SUPC interrupt handler for BODVDD event action.

  Description
    This function will trigger BODVDD callback.

  Remarks:
    plib_${SUPC_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${SUPC_INSTANCE_NAME}_InterruptHandler( void )
{
    if ((${SUPC_INSTANCE_NAME}_REGS->SUPC_INTFLAG & SUPC_INTFLAG_BODVDDDET_Msk) == SUPC_INTFLAG_BODVDDDET_Msk)
    {
        if (${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback != NULL)
        {
            ${SUPC_INSTANCE_NAME?lower_case}CallbackObject.callback(${SUPC_INSTANCE_NAME?lower_case}CallbackObject.context);
        }

        ${SUPC_INSTANCE_NAME}_REGS->SUPC_INTFLAG = SUPC_INTFLAG_BODVDDDET_Msk;
    }
}
