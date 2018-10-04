/*******************************************************************************
  Power Manager(${PM_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${PM_INSTANCE_NAME?lower_case}.c

  Summary
    ${PM_INSTANCE_NAME} PLIB Implementation File.

  Description
    This file defines the interface to the PM peripheral library. This
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
#include "plib_${PM_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${PM_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void ${PM_INSTANCE_NAME}_Initialize( void );

  Summary:
    Initializes given instance of PM peripheral.

  Description:
    This function initializes the specified instance of PM peripheral with the
    values configured in MHC GUI.

  Remarks:
    plib_${PM_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${PM_INSTANCE_NAME}_Initialize( void )
{
    /* Configure back biasing & VREG switching mode */
    <@compress single_line=true>${PM_INSTANCE_NAME}_REGS->PM_STDBYCFG = PM_STDBYCFG_BBIASHS(${PM_STDBYCFG_BBIASHS?then('1', '0')})
                                                       | PM_STDBYCFG_VREGSMOD_${PM_STDBYCFG_VREGSMOD};</@compress>
}

// *****************************************************************************
/* Function:
    void ${PM_INSTANCE_NAME}_SleepModeEnter( PM_SLEEP_MODE sleepMode );

  Summary:
    Puts the device into the specified sleep mode.

  Description:
    This function places the device in the specified sleep mode. The sleepMode
    parameter specifies the sleep mode that the device should be placed in. Once
    in sleep mode, the CPU will not execute any instruction unless it it woken
    up by a peripheral that is configured to operate in the specified sleep
    mode.

  Remarks:
    plib_${PM_INSTANCE_NAME?lower_case}.h for usage information.
*/

void ${PM_INSTANCE_NAME}_SleepModeEnter( PM_SLEEP_MODE sleepMode )
{
    switch (sleepMode)
    {
        case PM_SLEEP_MODE_IDLE:
        {
            /* APB clock is OFF */
            ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_IDLE2;

            break;
        }
        case PM_SLEEP_MODE_STANDBY:
        {
            /* All clocks are OFF */
            ${PM_INSTANCE_NAME}_REGS->PM_SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_STANDBY;

            break;
        }
    }

    /* Wait for interrupt instruction execution */
    __WFI();
}
