/*******************************************************************************
  FREQUENCY METER(FREQM${FREQM_INDEX}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_freqm${FREQM_INDEX}.c

  Summary:
    FREQM${FREQM_INDEX} PLIB Implementation File.

  Description:
    This file defines the interface to the FREQM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_freqm${FREQM_INDEX}.h"
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
	<#if FREQM_INTERRUPT_MODE = true >
    /* FREQM Event handler  */
    FREQM_CALLBACK callback;

    /* client context*/
    uintptr_t context;
	</#if>

    /* Variable for the reference clock frequency */
    uint32_t refFreqValue;

}FREQM_OBJECT;

/* Reference Object created for the FREQM */
FREQM_OBJECT freqm${FREQM_INDEX}Obj;

// *****************************************************************************
// *****************************************************************************
// Section: FREQM Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void FREQM${FREQM_INDEX}_Initialize (void);

  Summary:
    Initializes FREQM${FREQM_INDEX} module.

  Description:
    This function initializes FREQM${FREQM_INDEX} module with the values
	configured in MHC GUI. Once the peripheral is initialized, measurement APIs
	can be called to perform frequency measurement.

  Remarks:
    Refer plib_freqm${FREQM_INDEX}.h for more information.
*/

void FREQM${FREQM_INDEX}_Initialize (void)
{
<#if FREQM_INTERRUPT_MODE = true >
    /* Instantiate the FREQM Object */
    freqm${FREQM_INDEX}Obj.callback = NULL;

    freqm${FREQM_INDEX}Obj.context = NULL;
</#if>
	freqm${FREQM_INDEX}Obj.refFreqValue = 4000000U;

	/* FreqM Enabling on the APBA Bridge */
   MCLK_REGS->APBAMASK |= MCLK_APBAMASK_FREQM__Msk;

   /* Enabling the GCLK for the FREQM Measure clock  */
   GCLK_REGS->PCHCTRL[3] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Enabling the GCLK for the FREQM Reference clock  */
   GCLK_REGS->PCHCTRL[4] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Resetting the FREQM Module */
    FREQM_REGS->CTRLA |= FREQM_CTRLA_SWRST_Msk;

    while((FREQM_REGS->SYNCBUSY & FREQM_SYNCBUSY_SWRST_Msk) == FREQM_SYNCBUSY_SWRST_Msk)
	{
		/* Waiting for the FREQM Module to Reset */
	}

    /* Selection of the No. of Reference Cycles and Division Reference */
    FREQM_REGS->CFGA |= FREQM_CFGA_REFNUM(${REF_CLK_CYCLES}) ${REF_CLK_DIV?then('| FREQM_CFGA_DIVREF_Msk', '')};

	/* Clearing the Done Interrupt flag  */
	FREQM_REGS->INTFLAG = FREQM_INTFLAG_DONE_Msk ;

	/* Clearing the overflow flag  */
	FREQM_REGS->STATUS |= FREQM_STATUS_OVF_Msk;

    /* Enabling FREQM */
    FREQM_REGS->CTRLA |= FREQM_CTRLA_ENABLE_Msk;

    while((FREQM_REGS->SYNCBUSY & FREQM_SYNCBUSY_ENABLE_Msk) == FREQM_SYNCBUSY_ENABLE_Msk)
	{
		/* Waiting for the FREQM to Enable */
	}
}

// *****************************************************************************
/* Function:
    void FREQM${FREQM_INDEX}_MeasurementStart();

  Summary:
    This function starts the frequency measurement.

  Description:
    This function starts the frequency measurement. This function is always
    non-blocking. Calling this function when a frequency measurement is already
    in progress will result in a functional no operation. The FREQM${FREQM_INDEX}_IsBusy()
    function will return true when a frequency measurement is in progress. The
    completion of the measurement operation is indicated by the FREQM${FREQM_INDEX}_IsBusy()
    function returning false or a registered callback function being called.

    Starting a measurement will reset all module errors.

  Remarks:
    Refer plib_freqm${FREQM_INDEX}.h for more information.
*/

void FREQM${FREQM_INDEX}_MeasurementStart(void)
{
    if((FREQM_REGS->STATUS & FREQM_STATUS_BUSY_Msk) != FREQM_STATUS_BUSY_Msk )
    {
		/* Clearing the Done Interrupt flag  */
		FREQM_REGS->INTFLAG = FREQM_INTFLAG_DONE_Msk ;

		/* Clearing the overflow flag  */
		FREQM_REGS->STATUS |= FREQM_STATUS_OVF_Msk;

		/* Triggering the measurement to start */
		FREQM_REGS->CTRLB |= FREQM_CTRLB_START_Msk;

	<#if FREQM_INTERRUPT_MODE = true >
        /* Enabling the Done Interrupt */
        FREQM_REGS->INTENSET |= FREQM_INTENSET_DONE_Msk;
	</#if>
    }

}

// *****************************************************************************
/* Function:
    uint32_t FREQM${FREQM_INDEX}_FrequencyGet()

  Summary:
    Returns the measured frequency in Hz.

  Description:
    This function returns the measured frequency in Hz. It should be called when
    a frequency measurement is complete and no error have occurred. This
    function is non-blocking when the library is generated for interrupt
    operation. In this mode, the function should be called only after a callback
    function was called or after the FREQM${FREQM_INDEX}_IsBusy() function returns false
    indicating that an og-going frequency measurement operation has completed.

    It is blocking when the library is generated for non-interrupt operation.
    The function will block till the frequency measurement operation has
    completed. In this case, the return value of the function is only valid if
    the FREQM${FREQM_INDEX}_ErrorGet() function return FREQM_ERROR_NONE.

  Remarks:
    Refer plib_freqm${FREQM_INDEX}.h for more information.
*/

uint32_t FREQM${FREQM_INDEX}_FrequencyGet()
{
	/* Initializing the local variables */
    uint32_t refNum = 0;
    uint32_t resultCalculated = 0;
    uint32_t measuredValue = 0;

<#if FREQM_INTERRUPT_MODE = false >
	while((FREQM_REGS->STATUS & FREQM_STATUS_BUSY_Msk) == FREQM_STATUS_BUSY_Msk)
	{
		/* Waiting for the measurement to complete */
	}
</#if>

    /* Read the Value Register */
    resultCalculated = FREQM_REGS->VALUE;

    /* Reading the ref number of the cycles */
    refNum = FREQM_REGS->CFGA.REFNUM;

    /* Calculating the Resultant Measured Frequency Value */
    measuredValue = (resultCalculated/ refNum) * freqm${FREQM_INDEX}Obj.refFreqValue;

    return measuredValue;
}

<#if FREQM_INTERRUPT_MODE = true>
/// *****************************************************************************
/* Function:
    void FREQMx_CallbackRegister( FREQM_CALLBACK freqmcallback,
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
    Refer plib_freqm${FREQM_INDEX}.h for more information.
*/

void FREQM${FREQM_INDEX}_CallbackRegister(FREQM_CALLBACK freqmcallback, uintptr_t context)
{
    freqm${FREQM_INDEX}Obj.callback = freqmcallback;
    freqm${FREQM_INDEX}Obj.context = context;
}

// *****************************************************************************
/* Function:
    void FREQM${FREQM_INDEX}_InterruptHandler(void);

  Summary:
    Frequency Measurement interrupt handler.

  Description:
    This Function is called from the FREQM handler to handle the Frequency
    Measurement interrupts when the Measurement Done interrupt occurs.

  Remarks:
    None.
*/

void FREQM${FREQM_INDEX}_InterruptHandler(void)
{
    /* Check if data ready needs to be serviced */
    if (FREQM_REGS->INTFLAG & FREQM_INTFLAG_DONE_Msk)
    {
        /* Disable the DONE interrupt */
        FREQM_REGS->INTENCLR = FREQM_INTENCLR_DONE_Msk;

		if( NULL != freqm${FREQM_INDEX}Obj.callback)
		{
			/* Calling the callback function ,if registered */
			freqm${FREQM_INDEX}Obj.callback(freqm${FREQM_INDEX}Obj.context);
		}
    }
}

// *****************************************************************************
/* Function:
    bool FREQM${FREQM_INDEX}_IsBusy (void)

  Summary:
    Returns the measurement status of an on-going frequency measurement
    operation.

  Description:
    This function returns the measurement status of an on-going frequency
    measurement operation.  The function returns true when the
    FREQM${FREQM_INDEX}_MeasurementStart() function has been called to start a measurement.
    It returns false, when the  measurement operation has completed.  The
    function should be called only after a measurement operation was initiated.
    Once initiated, this function can be called to poll the completion of the
    measurement operation.

    This function can be used as an alternative to the callback function. In
    that, the application can call this function periodically to check for
    operation completion instead of waiting for callback to be called.

  Remarks:
    Refer plib_freqm${FREQM_INDEX}.h for more information.
*/

bool FREQM${FREQM_INDEX}_IsBusy(void)
{
	bool result = false;

	if((FREQM_REGS->STATUS & FREQM_STATUS_BUSY_Msk) == FREQM_STATUS_BUSY_Msk)
	{
		result = true;
	}

	return result;
}
</#if>

// *****************************************************************************
/* Function:
    FREQM_ERROR FREQM${FREQM_INDEX}_ErrorGet( void )

  Summary:
    Returns error that may have occurred during the frequency measurement
    process.

  Description:
    This function returns the error that may have occurred during the frequency
    measurement process. The function returns the error for the last completed
    operation.

  Remarks:
    Refer plib_freqm${FREQM_INDEX}.h for more information.
*/

FREQM_ERROR FREQM${FREQM_INDEX}_ErrorGet(void)
{
    FREQM_ERROR returnValue = FREQM_ERROR_NONE;

	returnValue = (FREQM_ERROR) FREQM_REGS->STATUS & FREQM_STATUS_OVF_Msk;

    return returnValue;
}

<#if FREQM_SETUPMODE = true>
// *****************************************************************************
/* Function:
    void FREQM${FREQM_INDEX}_Setup(uint32_t referenceFrequency)

  Summary:
    Allows the application to respecify the FREQM module reference clock
    frequency.

  Description:
    This function allows the application to respecify the FREQM module reference
    clock frequency. The application may need to call this function in a case
    where the system clock frequency may have changed. It is not necessary to
    call this function otherwise.

  Remarks:
    Refer plib_freqm${FREQM_INDEX}.h for more information.
*/

void FREQM${FREQM_INDEX}_Setup(uint32_t referenceFrequency)
{
	freqm${FREQM_INDEX}Obj.refFreqValue = referenceFrequency;
}
</#if>
