/*******************************************************************************
  MPLAB Harmony Application Source File

  Company:
    Microchip Technology Inc.

  File Name:
    app_e54.c

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "app_e54.h"

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
    This structure should be initialized by the APP_E54_Initialize function.

    Application strings and buffers are be defined outside this structure.
*/

APP_E54_DATA app_e54Data;

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
    void APP_E54_Initialize ( void )

  Remarks:
    See prototype in app_e54.h.
 */

void APP_E54_Initialize ( void )
{
    /* Place the App state machine in its initial state. */
    app_e54Data.state = APP_E54_STATE_INIT;



    /* TODO: Initialize your application's state machine and other
     * parameters.
     */
}


/******************************************************************************
  Function:
    void APP_E54_Tasks ( void )

  Remarks:
    See prototype in app_e54.h.
 */

void APP_E54_Tasks ( void )
{

    /* Check the application's current state. */
    switch ( app_e54Data.state )
    {
        /* Application's initial state. */
        case APP_E54_STATE_INIT:
        {
            bool appInitialized = true;


            if (appInitialized)
            {

                app_e54Data.state = APP_E54_STATE_SERVICE_TASKS;
            }
            break;
        }

        case APP_E54_STATE_SERVICE_TASKS:
        {
            SERCOM0_SPI_Write(mybuffer, SIZE);
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
