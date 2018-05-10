/*******************************************************************************
  External Interrupt Controller (EIC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_eic${EIC_INDEX}.c

  Summary
    Source for EIC peripheral library interface Implementation.

  Description
    This file defines the interface to the EIC peripheral library. This
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

#include "plib_eic${EIC_INDEX}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

/* EIC Pin Count */
#define EXTINT_COUNT                        (${EIC_INT_COUNT}U)

// *****************************************************************************
/* Callback function structure

  Summary:
    Stores EIC channel callback function and associated context.

  Description:
    This may be used to save the callback function and associated context for
    channel end of conversion interrupt source.

  Remarks:
    None.
*/

typedef struct
{
	/* EIC Callback Handler */
    EIC_CALLBACK    callback;
	
	/* PAC Client context */
    uintptr_t       context;
	
	/* External Interrupt Pin number */
    EIC_PIN         eicPinNo;

} EIC_CALLBACK_OBJ;

// *****************************************************************************
/* Callback function structure

  Summary:
    Stores EIC channel callback function and associated context.

  Description:
    This may be used to save the callback function and associated context for
    channel end of conversion interrupt source.

  Remarks:
    None.
*/

typedef struct
{
	/* NMI Callback Handler */
    EIC_NMI_CALLBACK callback;

	/* NMI Client context */
    uintptr_t       context;

} EIC_NMI_CALLBACK_OBJ;

/* EIC Channel Callback object */
EIC_CALLBACK_OBJ    eic${EIC_INDEX}CallbackObject[EXTINT_COUNT];

/* EIC NMI Callback object */
EIC_NMI_CALLBACK_OBJ eic${EIC_INDEX}NMICallbackObject;

// *****************************************************************************
// *****************************************************************************
// Section: EIC PLib Interface Implementations
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void EIC${EIC_INDEX}_Initialize (void);

   Summary:
    Initializes given instance of EIC peripheral.

   Description:
    This function initializes given instance of EIC peripheral of the device
    with the values configured in MHC GUI.

   Remarks:
    Refer plib_eic${EIC_INDEX}.h for usage information.
*/

void EIC${EIC_INDEX}_Initialize (void)
{
    /* Disable the EIC */
    EIC_REGS->CTRLA &= ~EIC_CTRLA_ENABLE_Msk;

    while((EIC_REGS->SYNCBUSY & EIC_SYNCBUSY_ENABLE_Msk) == EIC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for sync */
    }

    /* 
	 * Reset all registers in the EIC module to their initial state and 
	 * EIC will be disabled. 
	 */
    EIC_REGS->CTRLA |= EIC_CTRLA_SWRST_Msk;

    while((EIC_REGS->SYNCBUSY & EIC_SYNCBUSY_SWRST_Msk) == EIC_SYNCBUSY_SWRST_Msk)
    {
        /* Wait for sync */
    }

    /* CTRLA Register - Clock Selection */
    EIC_REGS->CTRLA |= ${(EIC_CLKSEL == "1")?then('EIC_CTRLA_CKSEL_Msk' , 'EIC_CTRLA_RESETVALUE')};

    /* NMI Control register - Write */
    <#if NMI_CTRL == true>
    <@compress single_line=true>EIC_REGS->NMICTRL =  EIC_ASYNCH_ASYNCH(${NMI_ASYNCH})
                                                        | EIC_NMICTRL_NMISENSE_${NMI_SENSE}
                                                        ${NMI_FILTEN?then('| EIC_NMICTRL_NMIFILTEN_Msk', '')};</@compress>
    <#else>
    EIC_REGS->NMICTRL = EIC_NMICTRL_RESETVALUE;
    </#if>

    /* Config 0 register (EXTINT channels [7:0]) - Write */
    EIC_REGS->CONFIG[0] =  EIC_CONFIG_SENSE0_${EIC_CONFIG_SENSE_0} ${EIC_CONFIG_FILTEN_0?then('| EIC_CONFIG_FILTEN0_Msk', '')} |
                              EIC_CONFIG_SENSE1_${EIC_CONFIG_SENSE_1} ${EIC_CONFIG_FILTEN_1?then('| EIC_CONFIG_FILTEN1_Msk', '')} |
                              EIC_CONFIG_SENSE2_${EIC_CONFIG_SENSE_2} ${EIC_CONFIG_FILTEN_2?then('| EIC_CONFIG_FILTEN2_Msk', '')} |
                              EIC_CONFIG_SENSE3_${EIC_CONFIG_SENSE_3} ${EIC_CONFIG_FILTEN_3?then('| EIC_CONFIG_FILTEN3_Msk', '')} |
                              EIC_CONFIG_SENSE4_${EIC_CONFIG_SENSE_4} ${EIC_CONFIG_FILTEN_4?then('| EIC_CONFIG_FILTEN4_Msk', '')} |
                              EIC_CONFIG_SENSE5_${EIC_CONFIG_SENSE_5} ${EIC_CONFIG_FILTEN_5?then('| EIC_CONFIG_FILTEN5_Msk', '')} |
                              EIC_CONFIG_SENSE6_${EIC_CONFIG_SENSE_6} ${EIC_CONFIG_FILTEN_6?then('| EIC_CONFIG_FILTEN6_Msk', '')} |
                              EIC_CONFIG_SENSE7_${EIC_CONFIG_SENSE_7} ${EIC_CONFIG_FILTEN_7?then('| EIC_CONFIG_FILTEN7_Msk', '')};

    /* Config 1 register (EXTINT channels [15:8])- Write */
    EIC_REGS->CONFIG[1] =  EIC_CONFIG_SENSE0_${EIC_CONFIG_SENSE_8} ${EIC_CONFIG_FILTEN_8?then('| EIC_CONFIG_FILTEN0_Msk', '')} |
                              EIC_CONFIG_SENSE1_${EIC_CONFIG_SENSE_9} ${EIC_CONFIG_FILTEN_9?then('| EIC_CONFIG_FILTEN1_Msk', '')} |
                              EIC_CONFIG_SENSE2_${EIC_CONFIG_SENSE_10} ${EIC_CONFIG_FILTEN_10?then('| EIC_CONFIG_FILTEN2_Msk', '')} |
                              EIC_CONFIG_SENSE3_${EIC_CONFIG_SENSE_11} ${EIC_CONFIG_FILTEN_11?then('| EIC_CONFIG_FILTEN3_Msk', '')} |
                              EIC_CONFIG_SENSE4_${EIC_CONFIG_SENSE_12} ${EIC_CONFIG_FILTEN_12?then('| EIC_CONFIG_FILTEN4_Msk', '')} |
                              EIC_CONFIG_SENSE5_${EIC_CONFIG_SENSE_13} ${EIC_CONFIG_FILTEN_13?then('| EIC_CONFIG_FILTEN5_Msk', '')} |
                              EIC_CONFIG_SENSE6_${EIC_CONFIG_SENSE_14} ${EIC_CONFIG_FILTEN_14?then('| EIC_CONFIG_FILTEN6_Msk', '')} |
                              EIC_CONFIG_SENSE7_${EIC_CONFIG_SENSE_15} ${EIC_CONFIG_FILTEN_15?then('| EIC_CONFIG_FILTEN7_Msk', '')};

    /* External Interrupt Asynchronous Mode register - Write */
    <@compress single_line=true>EIC_REGS->ASYNCH = EIC_ASYNCH_RESETVALUE
    <#list 0..EIC_INT_COUNT as i>
        <#assign EIC_ASYNCH = "EIC_ASYNCH_" + i>
        <#assign EIC_INT_CHANNEL = "EIC_INT_CHAN_" + i>
            <#if .vars[EIC_INT_CHANNEL]?has_content>
                <#if (.vars[EIC_INT_CHANNEL] != false)>
                    <#if .vars[EIC_ASYNCH]?has_content>
                        <#if (.vars[EIC_ASYNCH] != "0")>
<#lt>                       | EIC_ASYNCH_ASYNCH(1 << ${i})
                        </#if>
                    </#if>
                </#if>
            </#if>
    </#list>
    ;</@compress>

    /* Debouncen register - Write */
    <@compress single_line=true>EIC_REGS->DEBOUNCEN = EIC_DEBOUNCEN_RESETVALUE
    <#list 0..EIC_INT_COUNT as i>
        <#assign EIC_DEBOUNCEN = "EIC_DEBOUNCEN_" + i>
        <#assign EIC_INT_CHANNEL = "EIC_INT_CHAN_" + i>
            <#if .vars[EIC_INT_CHANNEL]?has_content>
                <#if (.vars[EIC_INT_CHANNEL] != false)>
                    <#if .vars[EIC_DEBOUNCEN]?has_content>
                        <#if (.vars[EIC_DEBOUNCEN] != false)>
<#lt>                       | EIC_DEBOUNCEN_DEBOUNCEN(1 << ${i})
                        </#if>
                    </#if>
                </#if>
            </#if>
    </#list>
    ;</@compress>

    /* Event Control register - Write */
    <@compress single_line=true>EIC_REGS->EVCTRL = EIC_EVCTRL_RESETVALUE
    <#list 0..EIC_INT_COUNT as i>
        <#assign EIC_EVCTRL_EXTINTEO = "EIC_EVCTRL_EXTINTEO_" + i>
        <#assign EIC_INT_CHANNEL = "EIC_INT_CHAN_" + i>
            <#if .vars[EIC_INT_CHANNEL]?has_content>
                <#if (.vars[EIC_INT_CHANNEL] != false)>
                    <#if .vars[EIC_EVCTRL_EXTINTEO]?has_content>
                        <#if (.vars[EIC_EVCTRL_EXTINTEO] != false)>
<#lt>                       | EIC_EVCTRL_EXTINTEO(1 << ${i})
                        </#if>
                    </#if>
                </#if>
            </#if>
    </#list>
    ;</@compress>

    /* Interrupt enable register - Write */
    <@compress single_line=true>EIC_REGS->INTENSET = EIC_INTENSET_RESETVALUE
    <#list 0..EIC_INT_COUNT as i>
        <#assign EIC_INT_CHANNEL = "EIC_INT_CHAN_" + i>
            <#if .vars[EIC_INT_CHANNEL]?has_content>
                <#if (.vars[EIC_INT_CHANNEL] != false)>
<#lt>                       | EIC_INTENSET_EXTINT(1 << ${i})
                </#if>
            </#if>
    </#list>
    ;</@compress>

    /* Debouncer Prescaler register - Write */
    <@compress single_line=true>EIC_REGS->DPRESCALER = EIC_DPRESCALER_PRESCALER0(${EIC_DEBOUNCER_PRESCALER_0})
                                                        | EIC_DPRESCALER_PRESCALER1(${EIC_DEBOUNCER_PRESCALER_1})
                                                        ${(EIC_PRESCALER_TICKON == "1")?then('| EIC_DPRESCALER_TICKON_Msk' , '')}
                                                        ${(EIC_DEBOUNCER_NO_STATES_0 == "1")?then('| EIC_DPRESCALER_STATES0_Msk' , '')}
                                                        ${(EIC_DEBOUNCER_NO_STATES_1 == "1")?then('| EIC_DPRESCALER_STATES1_Msk' , '')};</@compress>

    /* Callbacks for enabled interrupts */
    <#list 0..EIC_INT_COUNT as i>
        <#assign EIC_INT_CHANNEL = "EIC_INT_CHAN_" + i>
            <#if .vars[EIC_INT_CHANNEL]?has_content>
                <#if (.vars[EIC_INT_CHANNEL] != false)>
    <#lt>    eic${EIC_INDEX}CallbackObject[${i}].eicPinNo = EIC_PIN_${i};

                <#else>
    <#lt>    eic${EIC_INDEX}CallbackObject[${i}].eicPinNo = EIC_PIN_MAX;

                </#if>
        </#if>
    </#list>

    /* Enable the EIC */
    EIC_REGS->CTRLA |= EIC_CTRLA_ENABLE_Msk;

    while((EIC_REGS->SYNCBUSY & EIC_SYNCBUSY_ENABLE_Msk) == EIC_SYNCBUSY_ENABLE_Msk)
    {
        /* Wait for sync */
    }
}

// *****************************************************************************
/* Function:
    void EIC${EIC_INDEX}_InterruptEnable (EIC_PIN pin, bool enable)

  Summary:
    Enables and disables interrupts on a pin.

  Description
    This function enables and disables interrupts on an external interrupt pin.
    When enabled, the interrupt pin sense will be configured as per the
    configuration set in MHC.

  Remarks:
    Refer plib_eic${EIC_INDEX}.h for usage information.
*/

void EIC${EIC_INDEX}_InterruptEnable (EIC_PIN pin, bool enable)
{
    if (enable == true)
    {
        EIC_REGS->INTENSET |= (1UL << pin);
    }
    else
    {
        EIC_REGS->INTENCLR &= (1UL << pin);
    }
}

// *****************************************************************************
/* Function:
    void EIC${EIC_INDEX}_CallbackRegister   (EIC_PIN pin, EIC_CALLBACK callback
                                            uintptr_t context);

  Summary:
    Registers the function to be called from interrupt.

  Description
    This function registers the callback function to be called from interrupt

  Remarks:
    Refer plib_eic${EIC_INDEX}.h for usage information.
*/

void EIC${EIC_INDEX}_CallbackRegister(EIC_PIN pin, EIC_CALLBACK callback, uintptr_t context)
{
    if (eic${EIC_INDEX}CallbackObject[pin].eicPinNo == pin)
    {
        eic${EIC_INDEX}CallbackObject[pin].callback = callback;

        eic${EIC_INDEX}CallbackObject[pin].context  = context;
    }
}

// *****************************************************************************
/* Function:
    void EIC${EIC_INDEX}_NMICallbackRegister    (EIC_NMI_CALLBACK callback,
                                                uintptr_t context);

  Summary:
    Registers the function to be called from interrupt.

  Description
    This function registers the callback function to be called from interrupt

  Remarks:
    Refer plib_eic${EIC_INDEX}.h for usage information.
*/

void EIC${EIC_INDEX}_NMICallbackRegister(EIC_NMI_CALLBACK callback, uintptr_t context)
{
    eic${EIC_INDEX}NMICallbackObject.callback = callback;

    eic${EIC_INDEX}NMICallbackObject.context  = context;
}

// *****************************************************************************
/* Function:
    bool EIC${EIC_INDEX}_PinDebounceStateGet ( EIC_PIN pin )

  Summary:
    Gets the De-bounce state of the EIC Pin.

  Description
    This function gets the De-bounce state of the EIC Pin.

  Remarks:
    Refer plib_eic${EIC_INDEX}.h for usage information.
*/

bool EIC${EIC_INDEX}_PinDebounceStateGet (EIC_PIN pin)
{
    return ((EIC_REGS->DEBOUNCEN) & (1UL << pin));
}

// *****************************************************************************
/* Function:
    void EIC${EIC_INDEX}_InterruptHandler ( void )

  Summary:
    External Interrupt Controller (EIC) Interrupt Handler.

  Description
    This EIC Interrupt handler function handles interrupts on enabled EXINT Pins.

  Remarks:
    Refer plib_eic${EIC_INDEX}.h for usage information.
*/

void EIC${EIC_INDEX}_InterruptHandler(void)
{
    uint8_t currentChannel = 0;
    uint32_t eicIntFlagStatus = 0;

    /* Find any triggered channels, run associated callback handlers */
    for (currentChannel = 0; currentChannel < EXTINT_COUNT; currentChannel++)
    {
        /* Verify if the EXTINT x Interrupt Pin is enabled */
        if ((eic${EIC_INDEX}CallbackObject[currentChannel].eicPinNo == currentChannel))
        {
            /* Read the interrupt flag status */
            eicIntFlagStatus = EIC_REGS->INTFLAG & (1UL << currentChannel);

            if (eicIntFlagStatus)
            {
                /* Find any associated callback entries in the callback table */
                if ((eic${EIC_INDEX}CallbackObject[currentChannel].callback != NULL))
                {
                    eic${EIC_INDEX}CallbackObject[currentChannel].callback(eic${EIC_INDEX}CallbackObject[currentChannel].context);
                }

                /* Clear interrupt flag */
                EIC_REGS->INTFLAG = (1UL << currentChannel);
            }
        }
    }
}

// *****************************************************************************
/* Function:
    void NMI${EIC_INDEX}_InterruptHandler ( void )

  Summary:
    External Interrupt Controller (EIC) NMI Interrupt Handler.

  Description
    This EIC Interrupt handler function handles interrupts on NMI Pin

  Remarks:
    Refer plib_eic${EIC_INDEX}.h for usage information.
*/

void NMI${EIC_INDEX}_InterruptHandler(void)
{
    /* Find the triggered, run associated callback handlers */
    if ((EIC_REGS->NMIFLAG & EIC_NMIFLAG_NMI_Msk) == EIC_NMIFLAG_NMI_Msk)
    {
        /* Clear flag */
        EIC_REGS->NMIFLAG = EIC_NMIFLAG_NMI_Msk;

        /* Find any associated callback entries in the callback table */
        if (eic0NMICallbackObject.callback != NULL)
        {
            eic0NMICallbackObject.callback(eic0NMICallbackObject.context);
        }
    }
}
