/*******************************************************************************
  FREQUENCY METER(${FREQM_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FREQM_INSTANCE_NAME?lower_case}.c

  Summary:
    ${FREQM_INSTANCE_NAME} PLIB Implementation File.

  Description:
    This file defines the interface to the FREQM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_${FREQM_INSTANCE_NAME?lower_case}.h"
#include "device.h"

// *****************************************************************************
/* FREQM Object

  Summary:
    Defines the data type for the data structures used for peripheral
    operations.

  Description:
    This may be for used for FREQM operations.

  Remarks:
    None.
*/

typedef struct
{
   <#if FREQM_INTERRUPT_MODE == true >
    /* FREQM Event handler  */
    FREQM_CALLBACK callback;

    /* client context*/
    uintptr_t context;
   </#if>

    /* Variable for the reference clock frequency */
    uint32_t refFreqValue;

}FREQM_OBJECT;

/* Reference Object created for the FREQM */
FREQM_OBJECT ${FREQM_INSTANCE_NAME?lower_case}Obj;

// *****************************************************************************
// *****************************************************************************
// Section: FREQM Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void ${FREQM_INSTANCE_NAME}_Initialize (void);

  Summary:
    Initializes ${FREQM_INSTANCE_NAME} module.

  Description:
    This function initializes ${FREQM_INSTANCE_NAME} module with the values
   configured in MHC GUI. Once the peripheral is initialized, measurement APIs
   can be called to perform frequency measurement.

  Remarks:
    Refer plib_${FREQM_INSTANCE_NAME?lower_case}.h for more information.
*/

void ${FREQM_INSTANCE_NAME}_Initialize (void)
{
<#if FREQM_INTERRUPT_MODE == true >
    /* Instantiate the FREQM Object */
    ${FREQM_INSTANCE_NAME?lower_case}Obj.callback = NULL;

    ${FREQM_INSTANCE_NAME?lower_case}Obj.context = (uintptr_t)NULL;
</#if>
    ${FREQM_INSTANCE_NAME?lower_case}Obj.refFreqValue = 4000000U;

    /* FreqM Enabling on the APBA Bridge */
    MCLK_REGS->MCLK_APBAMASK |= MCLK_APBAMASK_FREQM__Msk;

    /* Enabling the GCLK for the FREQM Measure clock  */
    GCLK_REGS->GCLK_PCHCTRL[3] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Enabling the GCLK for the FREQM Reference clock  */
    GCLK_REGS->GCLK_PCHCTRL[4] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Resetting the FREQM Module */
    ${FREQM_INSTANCE_NAME}_REGS->FREQM_CTRLA |= FREQM_CTRLA_SWRST_Msk;

    while((${FREQM_INSTANCE_NAME}_REGS->FREQM_SYNCBUSY & FREQM_SYNCBUSY_SWRST_Msk) == FREQM_SYNCBUSY_SWRST_Msk)
    {
        /* Waiting for the FREQM Module to Reset */
    }

    /* Selection of the No. of Reference Cycles and Division Reference */
    ${FREQM_INSTANCE_NAME}_REGS->FREQM_CFGA |= FREQM_CFGA_REFNUM(${REF_CLK_CYCLES}) ${REF_CLK_DIV?then('| FREQM_CFGA_DIVREF_Msk', '')};

    /* Enabling FREQM */
    ${FREQM_INSTANCE_NAME}_REGS->FREQM_CTRLA |= FREQM_CTRLA_ENABLE_Msk;

    while((${FREQM_INSTANCE_NAME}_REGS->FREQM_SYNCBUSY & FREQM_SYNCBUSY_ENABLE_Msk) == FREQM_SYNCBUSY_ENABLE_Msk)
    {
        /* Waiting for the FREQM to Enable */
    }
}

// *****************************************************************************
/* Function:
    void ${FREQM_INSTANCE_NAME}_MeasurementStart();

  Summary:
    This function starts the frequency measurement.

  Description:
    This function starts the frequency measurement. This function is always
    non-blocking. Calling this function when a frequency measurement is already
    in progress will result in a functional no operation. The ${FREQM_INSTANCE_NAME}_IsBusy()
    function will return true when a frequency measurement is in progress. The
    completion of the measurement operation is indicated by the ${FREQM_INSTANCE_NAME}_IsBusy()
    function returning false or a registered callback function being called.

    Starting a measurement will reset all module errors.

  Remarks:
    Refer plib_${FREQM_INSTANCE_NAME?lower_case}.h for more information.
*/

void ${FREQM_INSTANCE_NAME}_MeasurementStart(void)
{
    if((${FREQM_INSTANCE_NAME}_REGS->FREQM_STATUS & FREQM_STATUS_BUSY_Msk) != FREQM_STATUS_BUSY_Msk )
    {
        /* Clearing the Done Interrupt flag  */
        ${FREQM_INSTANCE_NAME}_REGS->FREQM_INTFLAG = FREQM_INTFLAG_DONE_Msk ;

        /* Clearing the overflow flag  */
        ${FREQM_INSTANCE_NAME}_REGS->FREQM_STATUS |= FREQM_STATUS_OVF_Msk;

        /* Triggering the measurement to start */
        ${FREQM_INSTANCE_NAME}_REGS->FREQM_CTRLB |= FREQM_CTRLB_START_Msk;

    <#if FREQM_INTERRUPT_MODE == true >
        /* Enabling the Done Interrupt */
        ${FREQM_INSTANCE_NAME}_REGS->FREQM_INTENSET = FREQM_INTENSET_DONE_Msk;
    </#if>
    }

}

// *****************************************************************************
/* Function:
    uint32_t ${FREQM_INSTANCE_NAME}_FrequencyGet()

  Summary:
    Returns the measured frequency in Hz.

  Description:
    This function returns the measured frequency in Hz. It should be called when
    a frequency measurement is complete and no errors have occurred. This
    function is non-blocking when the library is generated for interrupt
    operation. In interrupt mode, the function should be called only after a
    callback function was called or after the ${FREQM_INSTANCE_NAME}_IsBusy()
    function returns false indicating that an on-going frequency measurement
    operation has completed.

    The function will block when the library is generated for non-interrupt
    operation.  The function will block till the frequency measurement operation
    has completed. In this case, the return value of the function is only valid
    if the ${FREQM_INSTANCE_NAME}_ErrorGet() function returns FREQM_ERROR_NONE.

  Remarks:
    Refer plib_${FREQM_INSTANCE_NAME?lower_case}.h for more information.
*/

uint32_t ${FREQM_INSTANCE_NAME}_FrequencyGet()
{
    /* Initializing the local variables */
    uint32_t refNum = 0;
    uint32_t resultCalculated = 0;
    uint32_t measuredValue = 0;

<#if FREQM_INTERRUPT_MODE = false >
    while((${FREQM_INSTANCE_NAME}_REGS->FREQM_STATUS & FREQM_STATUS_BUSY_Msk) == FREQM_STATUS_BUSY_Msk)
    {
        /* Waiting for the measurement to complete */
    }
</#if>

    /* Read the Value Register */
    resultCalculated = ${FREQM_INSTANCE_NAME}_REGS->FREQM_VALUE;

    /* Reading the ref number of the cycles */
    refNum = (${FREQM_INSTANCE_NAME}_REGS->FREQM_CFGA & FREQM_CFGA_REFNUM_Msk) >> FREQM_CFGA_REFNUM_Pos;

    /* Calculating the Resultant Measured Frequency Value */
    measuredValue = (resultCalculated/ refNum) * ${FREQM_INSTANCE_NAME?lower_case}Obj.refFreqValue;

    return measuredValue;
}

<#if FREQM_INTERRUPT_MODE == true>
/// *****************************************************************************
/* Function:
    void FREQMx_CallbackRegister( FREQM_CALLBACK freqmCallback,
                                                     uintptr_t context);

  Summary:
    Allows application to register a callback function.

  Description:
    This function allows the application to register a callback function that
    will be called when a frequency measurement operation has completed. The
    callback feature is only available if the Interrupt operation in the GUI was
    enabled.  If a callback mechanism is desired, then a callback function
    should be registered via this function before starting a frequency
    measurement. The application can read the measured frequency value and the
    check for errors in the callback function. Calling this function at any time
    with callback function as NULL will disable the callback feature.

  Remarks:
    Refer plib_${FREQM_INSTANCE_NAME?lower_case}.h for more information.
*/

void ${FREQM_INSTANCE_NAME}_CallbackRegister(FREQM_CALLBACK freqmCallback, uintptr_t context)
{
    ${FREQM_INSTANCE_NAME?lower_case}Obj.callback = freqmCallback;
    ${FREQM_INSTANCE_NAME?lower_case}Obj.context = context;
}

// *****************************************************************************
/* Function:
    void ${FREQM_INSTANCE_NAME}_InterruptHandler(void);

  Summary:
    Frequency Measurement interrupt handler.

  Description:
    This Function is called from the FREQM handler to handle the Frequency
    Measurement interrupts when the Measurement Done interrupt occurs.

  Remarks:
    None.
*/

void ${FREQM_INSTANCE_NAME}_InterruptHandler(void)
{
    /* Check if data ready needs to be serviced */
    if (${FREQM_INSTANCE_NAME}_REGS->FREQM_INTFLAG & FREQM_INTFLAG_DONE_Msk)
    {
        /* Disable the DONE interrupt */
        ${FREQM_INSTANCE_NAME}_REGS->FREQM_INTENCLR = FREQM_INTENCLR_DONE_Msk;

        if(${FREQM_INSTANCE_NAME?lower_case}Obj.callback != NULL)
        {
            /* Calling the callback function, if registered */
            ${FREQM_INSTANCE_NAME?lower_case}Obj.callback(${FREQM_INSTANCE_NAME?lower_case}Obj.context);
        }
    }
}
</#if>
// *****************************************************************************
/* Function:
    bool ${FREQM_INSTANCE_NAME}_IsBusy (void)

  Summary:
    Returns the measurement status of an on-going frequency measurement
    operation.

  Description:
    This function returns the measurement status of an on-going frequency
    measurement operation. The function returns true when the
    ${FREQM_INSTANCE_NAME}_MeasurementStart() function has been called to start a
    measurement and measurement has not completed. It returns false, when the
    measurement operation has completed. The function should be called after
    measurement operation was initiated, to poll the completion of the
    measurement operation.

    This function can be used as an alternative to the callback function. In
    that, the application can call this function periodically to check for
    operation completion instead of waiting for callback to be called.

  Remarks:
    Refer plib_${FREQM_INSTANCE_NAME?lower_case}.h for more information.
*/

bool ${FREQM_INSTANCE_NAME}_IsBusy(void)
{
   bool result = false;

    if((${FREQM_INSTANCE_NAME}_REGS->FREQM_STATUS & FREQM_STATUS_BUSY_Msk) == FREQM_STATUS_BUSY_Msk)
    {
        result = true;
    }

    return result;
}

// *****************************************************************************
/* Function:
    FREQM_ERROR ${FREQM_INSTANCE_NAME}_ErrorGet( void )

  Summary:
    Returns error that may have occurred during the frequency measurement
    process.

  Description:
    This function returns the error that may have occurred during the frequency
    measurement process. The function returns the error for the last completed
    operation.

  Remarks:
    Refer plib_${FREQM_INSTANCE_NAME?lower_case}.h for more information.
*/

FREQM_ERROR ${FREQM_INSTANCE_NAME}_ErrorGet(void)
{
    FREQM_ERROR returnValue = FREQM_ERROR_NONE;

    returnValue = (FREQM_ERROR) ${FREQM_INSTANCE_NAME}_REGS->FREQM_STATUS & FREQM_STATUS_OVF_Msk;

    return returnValue;
}

<#if FREQM_SETUPMODE == true>
// *****************************************************************************
/* Function:
    void ${FREQM_INSTANCE_NAME}_Setup(uint32_t referenceFrequency)

  Summary:
    Allows the application to respecify the FREQM module reference clock
    frequency.

  Description:
    This function allows the application to respecify the FREQM module reference
    clock frequency. The application may need to call this function in a case
    where the system clock frequency may have changed. It is not necessary to
    call this function otherwise.

  Remarks:
    Refer plib_${FREQM_INSTANCE_NAME?lower_case}.h for more information.
*/

void ${FREQM_INSTANCE_NAME}_Setup(uint32_t referenceFrequency)
{
    ${FREQM_INSTANCE_NAME?lower_case}Obj.refFreqValue = referenceFrequency;
}
</#if>
