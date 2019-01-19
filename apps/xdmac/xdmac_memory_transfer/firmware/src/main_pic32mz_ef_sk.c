/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project.  The
    "main" function calls the "SYS_Initialize" function to initialize the state
    machines of all modules in the system
 *******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// This is an app for demonstrating functionality of DMA.
// This will demonstrate a DMA memory-to-memory transfer, triggered from an 
// external (RTCC) interrupt.  DMA transfer occurs 10 seconds after the app
// starts.
//
// Put breakpoints near the end of main( ) below.  Comments are indicated in
// the code to show where to place them.
//
// Run the app to see which breakpoint is reached.
// *****************************************************************************
// *****************************************************************************


// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
/* Globals used in app.  Are global so that will be visible to user in debugger. */
volatile bool completeStatus = false; /* indicator of whether DMA xfer was completed */
volatile bool errorStatus = false;    /* indicator of whether DMA xfer was in error */
volatile bool compareStatus = false;  /* indicator of whether DMA xfer was successful */
volatile uint8_t transfersDone = 0;   /* number of DMA transfers that have occurred */

#define TRANSFER_SIZE 10 /* Amount of data to send. */
/* The 'const' puts the source data into an uncached memory region, which is what
   DMA needs.  See DS60001117H for more details.                                 */
const char __attribute__ ((aligned (32))) source[10] = {"123456789"};
uint8_t __attribute__((coherent)) destination[20] = {};


/*******************************************************************************
  Callback from DMA channel ISR.  This function being called demonstrates 
  proper registering of the callback function has taken place during DMA setup. 
*******************************************************************************/
void DMA_Callback(DMA_TRANSFER_EVENT status, uintptr_t context)
{
    transfersDone++;
    /* Status comes from the DMA channel ISR that was called.  This
       flag indicates whether the DMA indicated a completed transfer. */
    if(status == DMA_TRANSFER_EVENT_COMPLETE)
    {
        completeStatus = true;
    }
    else
    {
        errorStatus = true;
    }
}

int main ( void )
{
    struct tm time;
    struct tm date;
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    /* RTCC setup needed for peripheral-initiated DMA transfer. */
    /* RTCC-related */    
    time.tm_hour = 13;
    time.tm_min = 23;
    time.tm_sec = 40;
    time.tm_year = 18;
    time.tm_mon = 10;
    time.tm_mday = 29;
    time.tm_wday = 1;
    
    RTCC_TimeSet(&time);

    /* Set alarm time 10 seconds after RTC time. */
    time.tm_hour = 13;
    time.tm_min = 23;
    time.tm_sec = 50;
    time.tm_year = 18;
    time.tm_mon = 10;
    time.tm_mday = 29;
    time.tm_wday = 1;
    RTCC_AlarmSet(&time, RTC_ALARM_MASK_SS);
    /* end of RTCC-related setup */    
    
    /* Code used in all DMA apps */
    DMAC_ChannelCallbackRegister(DMA_CHANNEL_0, DMA_Callback, 0);
    DMAC_ChannelTransfer(DMA_CHANNEL_0,source, destination, TRANSFER_SIZE );
    /* When the DMA transfer is done, an interrupt will be called, which will call the
       callback function at the top of this file.                                     */
    while ( true )
    {
      if(transfersDone == 1)  /* This flag is only incremented in the callback function. */
      {
          if(memcmp(source, destination, TRANSFER_SIZE) == 0)
          {
/*******************************************************************************              
                      Put breakpoint at line below.
*******************************************************************************/
              compareStatus = true; /* Success case.  DMA transfer was good. */
              while(1)
                  ;
          }
          else
          {
/*******************************************************************************              
                      Put breakpoint at line below.
*******************************************************************************/
              compareStatus = false;
              while(1)
                  ;
          }
      }        
      /* Maintain state machines of all polled MPLAB Harmony modules. */
      SYS_Tasks ( );
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

