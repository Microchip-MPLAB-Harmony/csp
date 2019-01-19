/*******************************************************************************
  TMR1 Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_tmr1.c

  Summary
    TMR1 peripheral library source file.

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

/*  This section lists the other files that are included in this file.
*/
#include "device.h"
#include "plib_tmr1.h"

// *****************************************************************************
/* Timer1 System Service Object
*/
static TMR1_TIMER_OBJECT tmr1Obj;


// *****************************************************************************
/* Function:
   void TIMER_1_Handler (void)

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

void TIMER_1_Tasks (void)
{
  
  IFS0CLR = _IFS0_T1IF_MASK;
  if( (tmr1Obj.callback_fn != NULL))
  {
      tmr1Obj.callback_fn(tmr1Obj.context);
  }

}

// *****************************************************************************
/* Function:
   void TMR1_InterruptEnable(TMR1_INT_MASK interrupt)

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
void TMR1_InterruptEnable(void)
{
    IEC0SET = _IEC0_T1IE_MASK;  
}

// *****************************************************************************
/* Function:
   void TMR1_InterruptDisable(TMR1_INT_MASK interrupt)

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
void TMR1_InterruptDisable(void)
{
      IEC0CLR = _IEC0_T1IE_MASK;      
}

// *****************************************************************************
/* Function:
  void TMR1_CallbackRegister( TMR1_CALLBACK callback_fn, uintptr_t context )

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
void TMR1_CallbackRegister( TMR1_CALLBACK callback_fn, uintptr_t context )
{
 
    /* - Un-register callback_fn if NULL */
    if (callback_fn == NULL)
    {
        tmr1Obj.callback_fn = NULL;
        tmr1Obj.context = (uintptr_t) NULL;
        return;
    }
    /* - Save callback_fn and context in local memory */
    tmr1Obj.callback_fn = callback_fn;
    tmr1Obj.context = context;
}



// *****************************************************************************
/* Function:
    void TMR1_Initialize (void);
   
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
    TMR1_Initialize();
    </code>
   
  Remarks:
    This function must be called before any other Timer function is
    called.  This function is normally only be called once during system
    initialization.                                         
*/

void TMR1_Initialize(void)
{
    /* Disable Timer */
    T1CONCLR = _T1CON_ON_MASK;

    /* 
    SIDL = 0 
    TCKPS =3
    TSYNC   = 1
    TCS = 0
    */
    T1CONSET = 0x38;

    /* Clear counter */
    TMR1 = 0x0;

    /*Set period */ 
    PR1 = 64000;

    /* Setup TMR1 Interrupt */
    /* TMR1 interrupt priority and subpriority.  Clear field then write new value. */
    /* Priority	= 7	*/
	/* Sub-priority	= 0	*/
    IPC1SET = 0x1c;

    TMR1_InterruptEnable();  /* Enable interrupt on the way out */

   
    /* start the TMR1 */
    T1CONSET = _T1CON_ON_MASK;
    
 }
 
 
// *****************************************************************************
/* Function:
    void TMR1_Start (void);
   
  Summary:
    Starts the given Timer
   
  Description:
    This function enables the clock and starts the counter of the timer. 
 
  Precondition:
    TMR1_Initialize() function must have been called first.
 
  Parameters:
    None
 
  Returns:
    None.
   
  Example:
    <code>
    TMR1_Initialize();
    TMR1_Start();
    </code>
   
  Remarks:
    None
*/

void TMR1_Start (void)
{
   T1CONSET = _T1CON_ON_MASK;
}

// *****************************************************************************
/* Function:
void TMR1_Stop (void);
   
Summary:
  Stops the given Timer counter

Description:
  This function stops the clock and thus counter. 

Precondition:
   TMR1_Initialize() function must have been called first for the given 
  timer.

Parameters:
  None

Returns:
  None.

Example:
  <code>
  TMR1_Initialize();
  TMR1_Start();
  TMR1_Stop();
  </code>

Remarks:
  None
*/

void TMR1_Stop (void)
{
   T1CONCLR = _T1CON_ON_MASK;
}


// *****************************************************************************
/* Function:
    TMR1_PeriodSet ( uint16_t period );
   
  Summary:
    Sets the period value of a given timer.
   
  Description:
    This function writes the period value.  When timer counter matches period 
    value counter is reset and interrupt can be generated.
 
  Precondition:
    TMR1_Initialize() function must have been called first for the given 
    timer.
 
  Parameters:
    None.
 
  Returns:
    None.
   
  Example:
    <code>
    TMR1_Initialize();
    TMR1_PeriodSet();
    </code>
   
  Remarks:
    None.
*/

void TMR1_PeriodSet(uint16_t period)
{
   PR1  = period;
}

// *****************************************************************************
/* Function:
    uint16_t TMR1_PeriodGet(void);
   
  Summary:
    Reads the period value of given timer 
   
  Description:
    This function reads the value of period of given timer .    
 
  Precondition:
    TMR1_Initialize() function must have been called first. 
 
  Parameters:
    None
 
  Returns:
    The timer's period value.
   
  Example:
    <code>
    uint16_t period;

    TMR1_Initialize();
    period =  TMR1_PeriodGet();;
    </code>
   
  Remarks:
    None
*/

uint16_t TMR1_PeriodGet(void)
{
   return (uint16_t)PR1;
}

// *****************************************************************************
/* Function:
    uint16_t TMR1_CounterGet ( void );
   
  Summary:
    Reads the timer counter value
   
  Description:
    This function reads the timer counter value.
 
  Precondition:
    TMR1_Initialize() function must have been called first.
 
  Parameters:
    None
 
  Returns:
    The timer's counter value
   
  Example:
    <code>
    uint16_t counter;

    TMR1_Initialize();
    TMR1_Start();
    counter =  TMR1_CounterGet;
    </code>
   
  Remarks:
    None
*/
  

uint16_t TMR1_CounterGet(void)
{
   return(TMR1);
}

// *****************************************************************************
/* Function:
    uint16_t TMR1_FrequencyGet ( void );
   
  Summary:
    Provides the given timer's counter-increment frequency.
   
  Description:
    This function provides the frequency at which the given counter
    increments. It can be used to convert differences between counter values
    to real time or real-time intervals to timer period values.
 
  Precondition:
     TMR1_Initialize() function must have been called first.
 
  Parameters:
    None
 
  Returns:
      The frequency (in Hz) at which the timer's counter increments.
   
  Example:
    <code>
    uint16_t frequency;

     TMR1_Initialize();
    frequency =  TMR1_Initialize();;
    </code>
   
  Remarks:
    None
*/
  

uint32_t TMR1_FrequencyGet(void)
{
    uint32_t prescale, tmr1BaseFreq;
    if( _T1CON_TCS_MASK == T1CON & _T1CON_TCS_MASK)
    {
      /* Set external clock Freq fed through TCK pin */
      tmr1BaseFreq = TIMER1_EXT_CLOCK_INPUT_FREQ;
    }
    else
    {
      tmr1BaseFreq = 100000000;
    }
    
    prescale = 256;
    return ( tmr1BaseFreq / prescale );
}



/**
 End of File
*/
