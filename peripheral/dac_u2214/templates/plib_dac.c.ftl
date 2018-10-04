/*******************************************************************************
  Digital-to-Analog Converter (${DAC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DAC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${DAC_INSTANCE_NAME} PLIB Implementation file

  Description:
    This file defines the interface to the DAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#include "plib_${DAC_INSTANCE_NAME?lower_case}.h"
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
    void ${DAC_INSTANCE_NAME}_Initialize(void)

  Summary:
    Initializes given instance of the DAC peripheral.

  Description:
    This function initializes the given instance of the DAC peripheral as
    configured by the user within the MHC.

  Remarks:
    Refer plib_${DAC_INSTANCE_NAME?lower_case}.h for more information.
*/

void ${DAC_INSTANCE_NAME}_Initialize(void)
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

    <#if DAC_RUNSTDBY == true>
    /* Enable DAC Output Buffer in Standby Sleep Mode */
    DAC_REGS->DAC_CTRLA |= DAC_CTRLA_RUNSTDBY_Msk;
    </#if>

    /* Set Reference Voltage */
    DAC_REGS->DAC_CTRLB |= DAC_CTRLB_REFSEL(${DAC_REFERENCE_SELECTION});

    <#if DAC_VOLTAGE_PUMP_DISABLED == true>
    /* Set Voltage Pump */
    DAC_REGS->DAC_CTRLB |= DAC_CTRLB_VPD_Msk;
    </#if>

    /* Clear all Interrupts */
    DAC_REGS->DAC_INTFLAG |= DAC_INTFLAG_Msk;

    <#if DAC_DITHERING_MODE == true>
    /* Enable DAC Dithering operation */
    DAC_REGS->DAC_CTRLB |= DAC_CTRLB_DITHER_Msk;
    </#if>

    <#if DAC_OUTPUT_MODE == "ANALOG_COMPARATOR">
    /* Enable Internal Output */
    DAC_REGS->DAC_CTRLB |= DAC_CTRLB_IOEN_Msk;
    <#elseif DAC_OUTPUT_MODE == "INTERNAL_AND_EXTERNAL_OUTPUT">
    /* Enable Internal and External output */
    DAC_REGS->DAC_CTRLB |= (DAC_CTRLB_IOEN_Msk | DAC_CTRLB_EOEN_Msk);
    <#elseif DAC_OUTPUT_MODE == "EXTERNAL_OUTPUT">
    /* Enable External Output */
    DAC_REGS->DAC_CTRLB |= DAC_CTRLB_EOEN_Msk;
    </#if>

    /* Enable DAC */
    DAC_REGS->DAC_CTRLA |= DAC_CTRLA_ENABLE_Msk;

    while((DAC_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_ENABLE_Msk) == DAC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for Synchronization after Enabling DAC */
    }
}

// *****************************************************************************
/* Function:
    void ${DAC_INSTANCE_NAME}_DataWrite(uint16_t data)

  Summary:
    This function will write the specified value to the DAC and start the
    conversion.

  Description:
    This function will write the specified value to the DAC and start the
    conversion. The internal and/or external DAC outputs will be updated if
    these output were enabled.  The analog output voltage will depend on the
    choice of the DAC reference (configured via MHC). This function should only
    be called when the ${DAC_INSTANCE_NAME}_IsReady() returns true. Calling this function when
    the DAC is not ready will result in the in-determinate operation.

  Remarks:
    Refer plib_${DAC_INSTANCE_NAME?lower_case}.h for more information.
*/

void ${DAC_INSTANCE_NAME}_DataWrite(uint16_t data)
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
    bool ${DAC_INSTANCE_NAME}_IsReady(void);

  Summary:
    Checks whether DAC is ready for receiving next sample value.

  Description:
    This function checks for the readiness of the DAC to receive the next sample
    value. The application should call the ${DAC_INSTANCE_NAME}_DataWrite() function only when
    this function returns true. Calling the ${DAC_INSTANCE_NAME}_DataWrite() function when this
    function returns false will result in in-determinate operation.

  Remarks:
    Refer plib_${DAC_INSTANCE_NAME?lower_case}.h for more information.
*/

bool ${DAC_INSTANCE_NAME}_IsReady(void)
{
    bool dacIsReady = false;

    /* Check DAC is Ready for Conversion */
    if((DAC_REGS->DAC_STATUS & DAC_STATUS_READY_Msk) == DAC_STATUS_READY_Msk)
    {
        dacIsReady = true;
    }

    return dacIsReady;
}
