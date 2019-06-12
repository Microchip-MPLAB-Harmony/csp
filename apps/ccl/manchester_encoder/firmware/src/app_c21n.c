/*******************************************************************************
  MPLAB Harmony Application Source File

  Company:
    Microchip Technology Inc.

  File Name:
    app_c21n.c

  Summary:
    This file contains the source code for the MPLAB Harmony application.

  Description:
    This file contains the source code for the MPLAB Harmony application.  It
    implements the logic of the application's state machine and it may call
    API routines of other MPLAB Harmony modules in the system, such as drivers,
    system services, and middleware.  However, it does not call any of the
    system interfaces (such as the "Initialize" and "Tasks" functions) of any of
    the modules in the system or make any assumptions about when those functions
    are called.  That is the responsibility of the configuration-specific system
    files.
 *******************************************************************************/
/*******************************************************************************
   The intent of this app is to show how to configure the CCL in order to 
   generate manchester-encoded data.  Data is output via CCL_OUT[1], which 
   is configured on pin PA11.  The source data is in a 10-character buffer
   called mybuffer[], and is sent out via an open-loop SPI Tx in code below.
   The source data is in the MOSI line, on pin PA16 and the clock is pin PA17.
*******************************************************************************/


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "app_c21n.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************
#define SIZE 10
char mybuffer[SIZE]="0123456789";

// *****************************************************************************
/* Application Data

  Summary:
    Holds application data

  Description:
    This structure holds the application's data.

  Remarks:
    This structure should be initialized by the APP_C21N_Initialize function.

    Application strings and buffers are be defined outside this structure.
*/

APP_C21N_DATA app_c21nData;

// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Functions
// *****************************************************************************
// *****************************************************************************

/* TODO:  Add any necessary callback functions.
*/

// *****************************************************************************
// *****************************************************************************
// Section: Application Local Functions
// *****************************************************************************
// *****************************************************************************


/* TODO:  Add any necessary local functions.
*/


// *****************************************************************************
// *****************************************************************************
// Section: Application Initialization and State Machine Functions
// *****************************************************************************
// *****************************************************************************

/*******************************************************************************
  Function:
    void APP_C21N_Initialize ( void )

  Remarks:
    See prototype in app_c21n.h.
 */

void APP_C21N_Initialize ( void )
{
    /* Place the App state machine in its initial state. */
    app_c21nData.state = APP_C21N_STATE_INIT;



    /* TODO: Initialize your application's state machine and other
     * parameters.
     */
}


/******************************************************************************
  Function:
    void APP_C21N_Tasks ( void )

  Remarks:
    See prototype in app_c21n.h.
 */

void APP_C21N_Tasks ( void )
{

    /* Check the application's current state. */
    switch ( app_c21nData.state )
    {
        /* Application's initial state. */
        case APP_C21N_STATE_INIT:
        {
            bool appInitialized = true;


            if (appInitialized)
            {

                app_c21nData.state = APP_C21N_STATE_SERVICE_TASKS;
            }
            break;
        }

        case APP_C21N_STATE_SERVICE_TASKS:
        {
            SERCOM1_SPI_Write(mybuffer, SIZE);
            break;
        }

        /* TODO: implement your application state machine.*/


        /* The default state should never be executed. */
        default:
        {
            /* TODO: Handle error in application's state machine. */
            break;
        }
    }
}


/*******************************************************************************
 End of File
 */
