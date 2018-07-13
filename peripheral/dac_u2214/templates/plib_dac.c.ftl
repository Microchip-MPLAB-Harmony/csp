/*******************************************************************************
  Digital-to-Analog Converter (DAC${DAC_INDEX}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_dac${DAC_INDEX}.c

  Summary:
    DAC${DAC_INDEX} PLIB Implementation file

  Description:
    This file defines the interface to the DAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include "plib_dac${DAC_INDEX}.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

/* (GCLK_PCHCTRL) Peripheral Channel Index */
#define DAC_PERIPHERAL_CHANNEL_INDEX         (36U)

/* (DAC DATA) Mask DATA[15:10] Bit */
#define DAC_DATA_MSB_MASK                    (0x03FFU)

// *****************************************************************************
// *****************************************************************************
// Section: DAC Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void DAC${DAC_INDEX}_Initialize(void)

  Summary:
    Initializes given instance of the DAC peripheral.

  Description:
    This function initializes the given instance of the DAC peripheral as
    configured by the user within the MHC.

  Remarks:
    Refer plib_dac${DAC_INDEX}.h for more information.
*/

void DAC${DAC_INDEX}_Initialize(void)
{
    /* Enabling the APBC Bus */
    MCLK_REGS->MCLK_APBCMASK |= MCLK_APBCMASK_DAC__Msk;

    /* Enabling the Peripheral Clock */
    GCLK_REGS->GCLK_PCHCTRL[DAC_PERIPHERAL_CHANNEL_INDEX] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Software Reset */
    DAC_REGS->DAC_CTRLA |= DAC_CTRLA_SWRST_Msk;

    while((DAC_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_SWRST_Msk) == DAC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for Synchronization after Software Reset */
    }

    /* Enable DAC Output Buffer in Standby Sleep Mode */
    DAC_REGS->DAC_CTRLA |= DAC_CTRLA_RESETVALUE ${DAC_RUNSTDBY?then(' | DAC_CTRLA_RUNSTDBY_Msk','')};

    /* Set Reference Voltage */
    DAC_REGS->DAC_CTRLB |= DAC_CTRLB_REFSEL(${DAC_REFERENCE_SELECTION});

    /* Set Voltage Pump */
    DAC_REGS->DAC_CTRLB |= DAC_CTRLB_RESETVALUE ${DAC_VOLTAGE_PUMP_DISABLED?then(' | DAC_CTRLB_VPD_Msk','')};

    /* Clear all Interrupts */
    DAC_REGS->DAC_INTFLAG |= DAC_INTFLAG_Msk;
}

// *****************************************************************************
/* Function:
    void DAC${DAC_INDEX}_DataWrite(uint16_t data)

  Summary:
    This function will write the specified value to the DAC and start the
    conversion.

  Description:
    This function will write the specified value to the DAC and start the
    conversion. The internal and/or external DAC outputs will be updated if
    these output were enabled.  The analog output voltage will depend on the
    choice of the DAC reference (configured via MHC). This function should only
    be called when the DAC${DAC_INDEX}_IsReady() returns true. Calling this function when
    the DAC is not ready will result in the in-determinate operation. 

  Remarks:
    Refer plib_dac${DAC_INDEX}.h for more information.
*/

void DAC${DAC_INDEX}_DataWrite(uint16_t data)
{
    /* Write Data to DATA Register for conversion(DATA[9:0]) */
    DAC_REGS->DAC_DATA = DAC_DATA_MSB_MASK & DAC_DATA_DATA(data);

    while((DAC_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA_Msk) == DAC_SYNCBUSY_DATA_Msk)
    {
        /* Wait for Synchronization after writing Data to DATA Register */
    }
}

// *****************************************************************************
/* Function:
    bool DAC${DAC_INDEX}_IsReady(void);

  Summary:
    Checks whether DAC is ready for receiving next sample value.

  Description:
    This function checks for the readiness of the DAC to receive the next sample
    value. The application should call the DAC${DAC_INDEX}_DataWrite() function only when
    this function returns true. Calling the DAC${DAC_INDEX}_DataWrite() function when this
    function returns false will result in in-determinate operation.

  Remarks:
    Refer plib_dac${DAC_INDEX}.h for more information.
*/

bool DAC${DAC_INDEX}_IsReady(void)
{
    bool dacIsReady = false;

    /* Check DAC is Ready for Conversion */
    if((DAC_REGS->DAC_STATUS & DAC_STATUS_READY_Msk) == DAC_STATUS_READY_Msk)
    {
        dacIsReady = true;
    }

    return dacIsReady;
}

// *****************************************************************************
/* Function:
    void DAC${DAC_INDEX}_ExternalOutputEnable ( bool enable )

  Summary:
    Enable/Disable the external DAC output.

  Description:
    This function allows the application to enables and disable the external DAC
    output.

  Remarks:
    Refer plib_dac${DAC_INDEX}.h for more information.
*/

void DAC${DAC_INDEX}_ExternalOutputEnable ( bool enable )
{
    /* Disable DAC Module */
    DAC_REGS->DAC_CTRLA &= ~(DAC_CTRLA_ENABLE_Msk);

    while((DAC_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_ENABLE_Msk) == DAC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization after Disabling DAC */
    }

    if(enable)
    {
        /* Enable External Output */
        DAC_REGS->DAC_CTRLB |= DAC_CTRLB_EOEN_Msk;
    }
    else
    {
        DAC_REGS->DAC_CTRLB &= ~(DAC_CTRLB_EOEN_Msk);
    }

    /* Enable DAC */
    DAC_REGS->DAC_CTRLA |= DAC_CTRLA_ENABLE_Msk;

    while((DAC_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_ENABLE_Msk) == DAC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization after Enabling DAC */
    }
}

// *****************************************************************************
/* Function:
    void DAC${DAC_INDEX}_InternalOutputEnable ( bool enable )

  Summary:
    Enable/Disable the internal DAC output.

  Description:
    This function allows the application to enable and disable the internal DAC
    output to the Analog Comparator, ADC and the SDADC peripherals.

  Remarks:
    Refer plib_dac${DAC_INDEX}.h for more information.
*/

void DAC${DAC_INDEX}_InternalOutputEnable ( bool enable )
{
    /* Disable DAC Module */
    DAC_REGS->DAC_CTRLA &= ~(DAC_CTRLA_ENABLE_Msk);

    while((DAC_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_ENABLE_Msk) == DAC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization after Disabling DAC */
    }

    if(enable)
    {
        /* Enable Internal Output */
        DAC_REGS->DAC_CTRLB |= DAC_CTRLB_IOEN_Msk;
    }
    else
    {
        DAC_REGS->DAC_CTRLB &= ~(DAC_CTRLB_IOEN_Msk);
    }

    /* Enable DAC */
    DAC_REGS->DAC_CTRLA |= DAC_CTRLA_ENABLE_Msk;

    while((DAC_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_ENABLE_Msk) == DAC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization after Enabling DAC */
    }
}
