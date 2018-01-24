/*******************************************************************************
  Power Manager(PM${PM_INDEX}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_pm${PM_INDEX}.c

  Summary
    PM${PM_INDEX} PLIB Implementation File.

  Description
    This file defines the interface to the PM peripheral library. This
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
#include "plib_pm${PM_INDEX}.h"

// *****************************************************************************
// *****************************************************************************
// Section: PM${PM_INDEX} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void PM${PM_INDEX}_Initialize( void );

  Summary:
    Initializes given instance of PM peripheral.

  Description:
    This function initializes the specified instance of PM peripheral with the
    values configured in MHC GUI.

  Remarks:
    plib_pm${PM_INDEX}.h for usage information.
*/

void PM${PM_INDEX}_Initialize( void )
{
    /* Configure back biasing & VREG switching mode */
    <@compress single_line=true>PM_REGS->STDBYCFG = PM_STDBYCFG_BBIASHS(${PM_STDBYCFG_BBIASHS?then('1', '0')})
                                                       | PM_STDBYCFG_VREGSMOD_${PM_STDBYCFG_VREGSMOD};</@compress>
}

// *****************************************************************************
/* Function:
    void PM${PM_INDEX}_SleepModeEnter( PM_SLEEP_MODE sleepMode );

  Summary:
    Puts the device into the specified sleep mode.

  Description:
    This function places the device in the specified sleep mode. The sleepMode
    parameter specifies the sleep mode that the device should be placed in. Once
    in sleep mode, the CPU will not execute any instruction unless it it woken
    up by a peripheral that is configured to operate in the specified sleep
    mode.

  Remarks:
    plib_pm${PM_INDEX}.h for usage information.
*/

void PM${PM_INDEX}_SleepModeEnter( PM_SLEEP_MODE sleepMode )
{
    switch (sleepMode)
    {
        case PM_SLEEP_MODE_IDLE:
        {
            /* APB clock is OFF */
            PM_REGS->SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_IDLE2;

            break;
        }
        case PM_SLEEP_MODE_STANDBY:
        {
            /* All clocks are OFF */
            PM_REGS->SLEEPCFG = PM_SLEEPCFG_SLEEPMODE_STANDBY;

            break;
        }
    }

    /* Wait for interrupt instruction execution */
    __WFI();
}
