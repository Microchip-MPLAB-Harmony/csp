/*******************************************************************************
  FREQUENCY METER(FREQM) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_freqm.c

  Summary:
    FREQM PLIB Implementation File.

  Description:
    This file defines the interface to the FREQM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

*******************************************************************************/

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_freqm.h"
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

    /* Variable for the reference clock frequency */
    uint32_t refFreqValue;

}FREQM_OBJECT;

/* Reference Object created for the FREQM */
FREQM_OBJECT freqmObj;

// *****************************************************************************
// *****************************************************************************
// Section: FREQM Implementation
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
    void FREQM_Initialize (void);

  Summary:
    Initializes FREQM module.

  Description:
    This function initializes FREQM module with the values
   configured in MHC GUI. Once the peripheral is initialized, measurement APIs
   can be called to perform frequency measurement.

  Remarks:
    Refer plib_freqm.h for more information.
*/

void FREQM_Initialize (void)
{
    freqmObj.refFreqValue = 4000000U;

    /* FreqM Enabling on the APBA Bridge */
    MCLK_REGS->MCLK_APBAMASK |= MCLK_APBAMASK_FREQM__Msk;

    /* Enabling the GCLK for the FREQM Measure clock  */
    GCLK_REGS->GCLK_PCHCTRL[3] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Enabling the GCLK for the FREQM Reference clock  */
    GCLK_REGS->GCLK_PCHCTRL[4] |= GCLK_PCHCTRL_CHEN_Msk;

    /* Resetting the FREQM Module */
    FREQM_REGS->FREQM_CTRLA |= FREQM_CTRLA_SWRST_Msk;

    while((FREQM_REGS->FREQM_SYNCBUSY & FREQM_SYNCBUSY_SWRST_Msk) == FREQM_SYNCBUSY_SWRST_Msk)
    {
        /* Waiting for the FREQM Module to Reset */
    }

    /* Selection of the No. of Reference Cycles and Division Reference */
    FREQM_REGS->FREQM_CFGA |= FREQM_CFGA_REFNUM(1) ;

    /* Enabling FREQM */
    FREQM_REGS->FREQM_CTRLA |= FREQM_CTRLA_ENABLE_Msk;

    while((FREQM_REGS->FREQM_SYNCBUSY & FREQM_SYNCBUSY_ENABLE_Msk) == FREQM_SYNCBUSY_ENABLE_Msk)
    {
        /* Waiting for the FREQM to Enable */
    }
}

// *****************************************************************************
/* Function:
    void FREQM_MeasurementStart();

  Summary:
    This function starts the frequency measurement.

  Description:
    This function starts the frequency measurement. This function is always
    non-blocking. Calling this function when a frequency measurement is already
    in progress will result in a functional no operation. The FREQM_IsBusy()
    function will return true when a frequency measurement is in progress. The
    completion of the measurement operation is indicated by the FREQM_IsBusy()
    function returning false or a registered callback function being called.

    Starting a measurement will reset all module errors.

  Remarks:
    Refer plib_freqm.h for more information.
*/

void FREQM_MeasurementStart(void)
{
    if((FREQM_REGS->FREQM_STATUS & FREQM_STATUS_BUSY_Msk) != FREQM_STATUS_BUSY_Msk )
    {
        /* Clearing the Done Interrupt flag  */
        FREQM_REGS->FREQM_INTFLAG = FREQM_INTFLAG_DONE_Msk ;

        /* Clearing the overflow flag  */
        FREQM_REGS->FREQM_STATUS |= FREQM_STATUS_OVF_Msk;

        /* Triggering the measurement to start */
        FREQM_REGS->FREQM_CTRLB |= FREQM_CTRLB_START_Msk;

    }

}

// *****************************************************************************
/* Function:
    uint32_t FREQM_FrequencyGet()

  Summary:
    Returns the measured frequency in Hz.

  Description:
    This function returns the measured frequency in Hz. It should be called when
    a frequency measurement is complete and no errors have occurred. This
    function is non-blocking when the library is generated for interrupt
    operation. In interrupt mode, the function should be called only after a
    callback function was called or after the FREQM_IsBusy()
    function returns false indicating that an on-going frequency measurement
    operation has completed.

    The function will block when the library is generated for non-interrupt
    operation.  The function will block till the frequency measurement operation
    has completed. In this case, the return value of the function is only valid
    if the FREQM_ErrorGet() function returns FREQM_ERROR_NONE.

  Remarks:
    Refer plib_freqm.h for more information.
*/

uint32_t FREQM_FrequencyGet()
{
    /* Initializing the local variables */
    uint32_t refNum = 0;
    uint32_t resultCalculated = 0;
    uint32_t measuredValue = 0;

    while((FREQM_REGS->FREQM_STATUS & FREQM_STATUS_BUSY_Msk) == FREQM_STATUS_BUSY_Msk)
    {
        /* Waiting for the measurement to complete */
    }

    /* Read the Value Register */
    resultCalculated = FREQM_REGS->FREQM_VALUE;

    /* Reading the ref number of the cycles */
    refNum = (FREQM_REGS->FREQM_CFGA & FREQM_CFGA_REFNUM_Msk) >> FREQM_CFGA_REFNUM_Pos;

    /* Calculating the Resultant Measured Frequency Value */
    measuredValue = (resultCalculated/ refNum) * freqmObj.refFreqValue;

    return measuredValue;
}

// *****************************************************************************
/* Function:
    bool FREQM_IsBusy (void)

  Summary:
    Returns the measurement status of an on-going frequency measurement
    operation.

  Description:
    This function returns the measurement status of an on-going frequency
    measurement operation. The function returns true when the
    FREQM_MeasurementStart() function has been called to start a
    measurement and measurement has not completed. It returns false, when the
    measurement operation has completed. The function should be called after
    measurement operation was initiated, to poll the completion of the
    measurement operation.

    This function can be used as an alternative to the callback function. In
    that, the application can call this function periodically to check for
    operation completion instead of waiting for callback to be called.

  Remarks:
    Refer plib_freqm.h for more information.
*/

bool FREQM_IsBusy(void)
{
   bool result = false;

    if((FREQM_REGS->FREQM_STATUS & FREQM_STATUS_BUSY_Msk) == FREQM_STATUS_BUSY_Msk)
    {
        result = true;
    }

    return result;
}

// *****************************************************************************
/* Function:
    FREQM_ERROR FREQM_ErrorGet( void )

  Summary:
    Returns error that may have occurred during the frequency measurement
    process.

  Description:
    This function returns the error that may have occurred during the frequency
    measurement process. The function returns the error for the last completed
    operation.

  Remarks:
    Refer plib_freqm.h for more information.
*/

FREQM_ERROR FREQM_ErrorGet(void)
{
    FREQM_ERROR returnValue = FREQM_ERROR_NONE;

    returnValue = (FREQM_ERROR) FREQM_REGS->FREQM_STATUS & FREQM_STATUS_OVF_Msk;

    return returnValue;
}

