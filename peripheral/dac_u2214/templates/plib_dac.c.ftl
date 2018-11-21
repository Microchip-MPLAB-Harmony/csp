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

<#assign DAC_REGS = "DAC_CTRLB_REFSEL(" + DAC_REFERENCE_SELECTION + ") " + DAC_VOLTAGE_PUMP_DISABLED?then('| DAC_CTRLB_VPD_Msk ','') +
					DAC_DEVICE_NAME?contains("SAMC2")?then(DAC_DITHERING_MODE?then('| DAC_CTRLB_DITHER_Msk ',''),'') + (DAC_OUTPUT_MODE == "ANALOG_COMPARATOR")?then('| DAC_CTRLB_IOEN_Msk ','') +
					(DAC_OUTPUT_MODE == "INTERNAL_AND_EXTERNAL_OUTPUT")?then('| DAC_CTRLB_IOEN_Msk | DAC_CTRLB_EOEN_Msk ','') + (DAC_OUTPUT_MODE == "EXTERNAL_OUTPUT")?then('| DAC_CTRLB_EOEN_Msk ','')>

/* (DAC DATA) Mask DATA[15:10] Bit */
#define DAC_DATA_MSB_MASK                    (0x03FFU)


void ${DAC_INSTANCE_NAME}_Initialize(void)
{
    /* Set Reference Voltage */
    ${DAC_INSTANCE_NAME}_REGS->DAC_CTRLB = ${DAC_REGS};

    ${DAC_INSTANCE_NAME}_REGS->DAC_EVCTRL = ${DAC_EVCTRL};
    
    /* Enable DAC */
    ${DAC_INSTANCE_NAME}_REGS->DAC_CTRLA = DAC_CTRLA_ENABLE_Msk ${DAC_RUNSTDBY?then('| DAC_CTRLA_RUNSTDBY_Msk',' ')};	

    <#if DAC_DEVICE_NAME?contains("SAMC2")>while((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_ENABLE_Msk) == DAC_SYNCBUSY_ENABLE_Msk)<#else>while(${DAC_INSTANCE_NAME}_REGS->DAC_STATUS)</#if>	
    {
        /* Wait for Synchronization after Enabling DAC */
    }
    
}

void ${DAC_INSTANCE_NAME}_DataWrite(uint16_t data)
{
    /* Write Data to DATA Register for conversion(DATA[9:0]) */
    ${DAC_INSTANCE_NAME}_REGS->DAC_DATA = DAC_DATA_MSB_MASK & DAC_DATA_DATA(data);

    <#if DAC_DEVICE_NAME?contains("SAMC2")>while((${DAC_INSTANCE_NAME}_REGS->DAC_SYNCBUSY & DAC_SYNCBUSY_DATA_Msk) == DAC_SYNCBUSY_DATA_Msk)<#else>while(${DAC_INSTANCE_NAME}_REGS->DAC_STATUS)</#if>	
    {
        /* Wait for Synchronization after writing Data to DATA Register */
    }
}

<#if DAC_DEVICE_NAME?contains("SAMC2")>bool ${DAC_INSTANCE_NAME}_IsReady(void)
{
    return ((${DAC_INSTANCE_NAME}_REGS->DAC_STATUS & DAC_STATUS_READY_Msk) == DAC_STATUS_READY_Msk);
}
</#if>