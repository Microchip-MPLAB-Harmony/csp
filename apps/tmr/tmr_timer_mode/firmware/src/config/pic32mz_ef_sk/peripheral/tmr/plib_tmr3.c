/*******************************************************************************
  TMR Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_tmr3.c

  Summary
    TMR3 peripheral library source file.

  Description
    This file implements the interface to the TMR peripheral library.  This
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
#include "plib_tmr3.h"

// *****************************************************************************
/* Timer1 System Service Object
*/
static TMR_TIMER_OBJECT tmr3Obj;


// *****************************************************************************
/* Function:
   void TIMER_3_Handler (void);

  Summary:
    Interrupt handler for tmr interrupts.

  Description:
    This function calls the user-registered callback_fn, if registered.
    Also clears the interrupt source bit to allow future tmr interrupts to occur.

  Parameters:
    none

  Returns:
    void
*/

void TIMER_3_Tasks (void)
{
  
  IFS0CLR = _IFS0_T3IF_MASK;
  if( (tmr3Obj.callback_fn != NULL))
  {
      tmr3Obj.callback_fn(tmr3Obj.context);
  }

}

// *****************************************************************************
/* Function:
   void TMR3_InterruptEnable(TMR_INT_MASK interrupt);

  Summary:
    Enable TMR interrupts.

  Description:
    This function enables TMR interrupts.  The mask is not used in the PIC32MZ 
    family, so the argument is ignored.  This maintains the existing API for H3.

  Parameters:
    none

  Returns:
    void
*/
void TMR3_InterruptEnable(void)
{
    IEC0SET = _IEC0_T3IE_MASK;  
}

// *****************************************************************************
/* Function:
   void TMR3_InterruptDisable(TMR_INT_MASK interrupt);

  Summary:
    Disable TMR interrupts.

  Description:
    This function disables TMR interrupts.  The mask is not used in the PIC32MZ 
    family, so the argument is ignored.  This maintains the existing API for H3.

  Parameters:
    none

  Returns:
    void
*/
void TMR3_InterruptDisable(void)
{
      IEC0CLR = _IEC0_T3IE_MASK;      
}

// *****************************************************************************
/* Function:
  void TMR3_CallbackRegister( TMR_CALLBACK callback_fn, uintptr_t context );

  Summary:
    Sets the callback_fn function for an match.

  Description:
    This function sets the callback_fn function that will be called when the TMR
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
void TMR3_CallbackRegister( TMR_CALLBACK callback_fn, uintptr_t context )
{
 
    /* - Un-register callback_fn if NULL */
    if (callback_fn == NULL)
    {
        tmr3Obj.callback_fn = NULL;
        tmr3Obj.context = (uintptr_t) NULL;
        return;
    }
    /* - Save callback_fn and context in local memory */
    tmr3Obj.callback_fn = callback_fn;
    tmr3Obj.context = context;
}



// *****************************************************************************
/* Function:
    void TMR3_Initialize (void);
   
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
    TMR3_Initialize();
    </code>
   
  Remarks:
    This function must be called before any other Timer function is
    called.  This function is normally only be called once during system
    initialization.                                         
*/
void TMR3_Initialize(void)
{
    /* Disable Timer */
    T3CONCLR = _T3CON_ON_MASK;

    /* 
    SIDL = 0 
    TCKPS =7
    T32   = 0
    TCS = 0
    */
    T3CONSET = 0x70;

    /* Clear counter */
    TMR3 = 0x0;

    /*Set period */ 
    PR3 = 64000;

    /* Setup TMR Interrupt */
    /* TMR interrupt priority and subpriority.  Clear field then write new value. */
    /* Priority	= 7	*/
	/* Sub-priority	= 0	*/
    IPC3SET = 0x1c0000;

    TMR3_InterruptEnable();  /* Enable interrupt on the way out */

   
    /* start the TMR */
    T3CONSET = _T3CON_ON_MASK;
    
 }
 
 // *****************************************************************************
/* Function:
    void TMR3_Start (void);
   
  Summary:
    Starts the given Timer
   
  Description:
    This function enables the clock and starts the counter of the timer. 
 
  Precondition:
    TMR3_Initialize() function must have been called first.
 
  Parameters:
    None
 
  Returns:
    None.
   
  Example:
    <code>
    TMR3_Initialize();
    TMR3_Start();
    </code>
   
  Remarks:
    None
*/
void TMR3_Start(void)
{
   T3CONSET = _T3CON_ON_MASK;
}


 // *****************************************************************************
/* Function:
void TMR3_Stop (void);
   
Summary:
  Stops the given Timer counter

Description:
  This function stops the clock and thus counter. 

Precondition:
   TMR3_Initialize() function must have been called first for the given 
  timer.

Parameters:
  None

Returns:
  None.

Example:
  <code>
  TMR3_Initialize();
  TMR3_Start();
  TMR3_Stop();
  </code>

Remarks:
  None
*/
void TMR3_Stop (void)
{
   T3CONCLR = _T3CON_ON_MASK;
}


// *****************************************************************************
/* Function:
    TMR3_PeriodSet ( uint16_t period );
   
  Summary:
    Sets the period value of a given timer.
   
  Description:
    This function writes the period value.  When timer counter matches period 
    value counter is reset and interrupt can be generated.
 
  Precondition:
    TMR3_Initialize() function must have been called first for the given 
    timer.
 
  Parameters:
    None.
 
  Returns:
    None.
   
  Example:
    <code>
    TMR3_Initialize();
    TMR3_PeriodSet();
    </code>
   
  Remarks:
    None.
*/
void TMR3_PeriodSet(uint16_t period)
{
   PR3  = period;
}

// *****************************************************************************
/* Function:
    uint16_t TMR3_PeriodGet(void);
   
  Summary:
    Reads the period value of given timer 
   
  Description:
    This function reads the value of period of given timer .    
 
  Precondition:
    TMR3_Initialize() function must have been called first. 
 
  Parameters:
    None
 
  Returns:
    The timer's period value.
   
  Example:
    <code>
    uint16_t period;

    TMR3_Initialize();
    period =  TMR3_PeriodGet();;
    </code>
   
  Remarks:
    None
*/
uint16_t TMR3_PeriodGet(void)
{
   return (uint16_t)PR3;
}

// *****************************************************************************
/* Function:
    uint16_t TMR3_CounterGet ( void );
   
  Summary:
    Reads the timer counter value
   
  Description:
    This function reads the timer counter value.
 
  Precondition:
    TMR3_Initialize() function must have been called first.
 
  Parameters:
    None
 
  Returns:
    The timer's counter value
   
  Example:
    <code>
    uint16_t counter;

    TMR3_Initialize();
    TMR3_Start();
    counter =  TMR3_CounterGet;
    </code>
   
  Remarks:
    None
*/

uint16_t TMR3_CounterGet(void)
{
   return(TMR3);
}

// *****************************************************************************
/* Function:
    uint16_t TMR3_FrequencyGet ( void );
   
  Summary:
    Provides the given timer's counter-increment frequency.
   
  Description:
    This function provides the frequency at which the given counter
    increments. It can be used to convert differences between counter values
    to real time or real-time intervals to timer period values.
 
  Precondition:
     TMR3_Initialize() function must have been called first.
 
  Parameters:
    None
 
  Returns:
      The frequency (in Hz) at which the timer's counter increments.
   
  Example:
    <code>
    uint16_t frequency;

     TMR3_Initialize();
    frequency =  TMR3_Initialize();;
    </code>
   
  Remarks:
    None
*/
  
uint32_t TMR3_FrequencyGet(void)
{
    uint32_t prescale, tmrBaseFreq;
    if( _T3CON_TCS_MASK == T3CON & _T3CON_TCS_MASK)
    {
      /* Set external clock Freq fed through TCK pin */
      tmrBaseFreq = TIMER3_EXT_CLOCK_INPUT_FREQ;
    }
    else
    {
      tmrBaseFreq = 100000000;
    }
    
    prescale = 256;
    return ( tmrBaseFreq / prescale );
}


/*
 End of File
*/
