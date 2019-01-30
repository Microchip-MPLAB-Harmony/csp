/*******************************************************************************
  TMR1 Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${TMR1_INSTANCE_NAME?lower_case}.c

  Summary
    ${TMR1_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the TMR1 peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

#include "device.h"
#include "plib_${TMR1_INSTANCE_NAME?lower_case}.h"

<#if TMR1_INTERRUPT_MODE == true>
static TMR1_TIMER_OBJECT ${TMR1_INSTANCE_NAME?lower_case}Obj;
</#if>

// *****************************************************************************
/* Function:
    void ${TMR1_INSTANCE_NAME}_Initialize (void);

  Summary:
    Initializes timer

  Description:
    This function initializes given instance of timer with
    the options configured in MCC GUI.

  Precondition:
    MCC GUI should be configured with the desired values.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    ${TMR1_INSTANCE_NAME}_Initialize();
    </code>

  Remarks:
    This function must be called before any other Timer function is
    called.  This function is normally only be called once during system
    initialization.
*/

void ${TMR1_INSTANCE_NAME}_Initialize(void)
{
    /* Disable Timer */
    T1CONCLR = _T1CON_ON_MASK;

    /*
    SIDL = ${TIMER1_SIDL}
    TCKPS =${TIMER1_PRE_SCALER}
    TSYNC   = ${TIMER1_TSYNC_SEL}
    TCS = ${TIMER1_SRC_SEL}
    */
    T1CONSET = 0x${TCON_REG_VALUE};

    /* Clear counter */
    TMR1 = 0x0;

    /*Set period */
    PR1 = ${TIMER1_PERIOD};

    /* Setup TMR1 Interrupt */
    <#if TMR1_INTERRUPT_MODE == true>
    ${TMR1_INSTANCE_NAME}_InterruptEnable();  /* Enable interrupt on the way out */

    </#if>
    /* start the TMR1 */
    T1CONSET = _T1CON_ON_MASK;
}

// *****************************************************************************
/* Function:
    void ${TMR1_INSTANCE_NAME}_Start (void);

  Summary:
    Starts the given Timer

  Description:
    This function enables the clock and starts the counter of the timer.

  Precondition:
    ${TMR1_INSTANCE_NAME}_Initialize() function must have been called first.

  Parameters:
    None

  Returns:
    None.

  Example:
    <code>
    ${TMR1_INSTANCE_NAME}_Initialize();
    ${TMR1_INSTANCE_NAME}_Start();
    </code>

  Remarks:
    None
*/

void ${TMR1_INSTANCE_NAME}_Start (void)
{
    T1CONSET = _T1CON_ON_MASK;
}

// *****************************************************************************
/* Function:
void ${TMR1_INSTANCE_NAME}_Stop (void);

Summary:
  Stops the given Timer counter

Description:
  This function stops the clock and thus counter.

Precondition:
   ${TMR1_INSTANCE_NAME}_Initialize() function must have been called first for the given
  timer.

Parameters:
  None

Returns:
  None.

Example:
  <code>
  ${TMR1_INSTANCE_NAME}_Initialize();
  ${TMR1_INSTANCE_NAME}_Start();
  ${TMR1_INSTANCE_NAME}_Stop();
  </code>

Remarks:
  None
*/

void ${TMR1_INSTANCE_NAME}_Stop (void)
{
    T1CONCLR = _T1CON_ON_MASK;
}

// *****************************************************************************
/* Function:
    ${TMR1_INSTANCE_NAME}_PeriodSet ( uint16_t period );

  Summary:
    Sets the period value of a given timer.

  Description:
    This function writes the period value.  When timer counter matches period
    value counter is reset and interrupt can be generated.

  Precondition:
    ${TMR1_INSTANCE_NAME}_Initialize() function must have been called first for the given
    timer.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    ${TMR1_INSTANCE_NAME}_Initialize();
    ${TMR1_INSTANCE_NAME}_PeriodSet();
    </code>

  Remarks:
    None.
*/

void ${TMR1_INSTANCE_NAME}_PeriodSet(uint16_t period)
{
    PR1 = period;
}

// *****************************************************************************
/* Function:
    uint16_t ${TMR1_INSTANCE_NAME}_PeriodGet(void);

  Summary:
    Reads the period value of given timer

  Description:
    This function reads the value of period of given timer .

  Precondition:
    ${TMR1_INSTANCE_NAME}_Initialize() function must have been called first.

  Parameters:
    None

  Returns:
    The timer's period value.

  Example:
    <code>
    uint16_t period;

    ${TMR1_INSTANCE_NAME}_Initialize();
    period =  ${TMR1_INSTANCE_NAME}_PeriodGet();;
    </code>

  Remarks:
    None
*/

uint16_t ${TMR1_INSTANCE_NAME}_PeriodGet(void)
{
    return (uint16_t)PR1;
}

// *****************************************************************************
/* Function:
    uint16_t ${TMR1_INSTANCE_NAME}_CounterGet ( void );

  Summary:
    Reads the timer counter value

  Description:
    This function reads the timer counter value.

  Precondition:
    ${TMR1_INSTANCE_NAME}_Initialize() function must have been called first.

  Parameters:
    None

  Returns:
    The timer's counter value

  Example:
    <code>
    uint16_t counter;

    ${TMR1_INSTANCE_NAME}_Initialize();
    ${TMR1_INSTANCE_NAME}_Start();
    counter =  ${TMR1_INSTANCE_NAME}_CounterGet;
    </code>

  Remarks:
    None
*/

uint16_t ${TMR1_INSTANCE_NAME}_CounterGet(void)
{
    return(TMR1);
}

// *****************************************************************************
/* Function:
    uint16_t ${TMR1_INSTANCE_NAME}_FrequencyGet ( void );

  Summary:
    Provides the given timer's counter-increment frequency.

  Description:
    This function provides the frequency at which the given counter
    increments. It can be used to convert differences between counter values
    to real time or real-time intervals to timer period values.

  Precondition:
    ${TMR1_INSTANCE_NAME}_Initialize() function must have been called first.

  Parameters:
    None

  Returns:
    The frequency (in Hz) at which the timer's counter increments.

  Example:
    <code>
    uint16_t frequency;

    ${TMR1_INSTANCE_NAME}_Initialize();
    frequency =  ${TMR1_INSTANCE_NAME}_Initialize();;
    </code>

  Remarks:
    None
*/

uint32_t ${TMR1_INSTANCE_NAME}_FrequencyGet(void)
{
    uint32_t prescale, tmr1BaseFreq;

    if( _T1CON_TCS_MASK == (T1CON & _T1CON_TCS_MASK))
    {
        /* Set external clock Freq fed through TCK pin */
        tmr1BaseFreq = TIMER1_EXT_CLOCK_INPUT_FREQ;
    }
    else
    {
        tmr1BaseFreq = ${core.CONFIG_SYS_CLK_PBCLK2_FREQ};
    }

    prescale = ${TMR1_PRESCALER_VALUE};

    return ( tmr1BaseFreq / prescale );
}

<#if TMR1_INTERRUPT_MODE == true>
// *****************************************************************************
/* Function:
   void TIMER_1_InterruptHandler (void)

  Summary:
    Interrupt handler for tmr1 interrupts.

  Description:
    This function calls the user-registered callback_fn, if registered.
    Also clears the interrupt source bit to allow future tmr1 interrupts to occur.

  Parameters:
    none

  Returns:
    void
*/

void TIMER_1_InterruptHandler (void)
{
    ${TMR1_IFS_REG}CLR = _${TMR1_IFS_REG}_T1IF_MASK;

    if((${TMR1_INSTANCE_NAME?lower_case}Obj.callback_fn != NULL))
    {
        ${TMR1_INSTANCE_NAME?lower_case}Obj.callback_fn(${TMR1_INSTANCE_NAME?lower_case}Obj.context);
    }
}

// *****************************************************************************
/* Function:
   void ${TMR1_INSTANCE_NAME}_InterruptEnable(TMR1_INT_MASK interrupt)

  Summary:
    Enable TMR1 interrupts.

  Description:
    This function enables TMR1 interrupts.  The mask is not used in the PIC32MZ
    family, so the argument is ignored.  This maintains the existing API for H3.

  Parameters:
    none

  Returns:
    void
*/
void ${TMR1_INSTANCE_NAME}_InterruptEnable(void)
{
    ${TMR1_IEC_REG}SET = _${TMR1_IEC_REG}_T1IE_MASK;
}

// *****************************************************************************
/* Function:
   void ${TMR1_INSTANCE_NAME}_InterruptDisable(TMR1_INT_MASK interrupt)

  Summary:
    Disable TMR1 interrupts.

  Description:
    This function disables TMR1 interrupts.  The mask is not used in the PIC32MZ
    family, so the argument is ignored.  This maintains the existing API for H3.

  Parameters:
    none

  Returns:
    void
*/
void ${TMR1_INSTANCE_NAME}_InterruptDisable(void)
{
    ${TMR1_IEC_REG}CLR = _${TMR1_IEC_REG}_T1IE_MASK;
}

// *****************************************************************************
/* Function:
  void ${TMR1_INSTANCE_NAME}_CallbackRegister( TMR1_CALLBACK callback_fn, uintptr_t context )

  Summary:
    Sets the callback_fn function for an match.

  Description:
    This function sets the callback_fn function that will be called when the TMR1
    match is reached.

  Precondition:
    None.

  Parameters:
    *callback_fn   - a pointer to the function to be called when match is reached.
                  Use NULL to Un Register the match callback_fn

    context     - a pointer to user defined data to be used when the callback_fn
                  function is called. NULL can be passed in if no data needed.

  Returns:
    None
*/
void ${TMR1_INSTANCE_NAME}_CallbackRegister( TMR1_CALLBACK callback_fn, uintptr_t context )
{

    /* - Un-register callback_fn if NULL */
    if (callback_fn == NULL)
    {
        ${TMR1_INSTANCE_NAME?lower_case}Obj.callback_fn = NULL;
        ${TMR1_INSTANCE_NAME?lower_case}Obj.context = (uintptr_t) NULL;
        return;
    }

    /* - Save callback_fn and context in local memory */
    ${TMR1_INSTANCE_NAME?lower_case}Obj.callback_fn = callback_fn;
    ${TMR1_INSTANCE_NAME?lower_case}Obj.context = context;
}
</#if>