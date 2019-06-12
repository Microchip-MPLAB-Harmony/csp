/*******************************************************************************
  MPLAB Harmony Application Source File

  Company:
    Microchip Technology Inc.

  File Name:
    app_l21.c

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
 * The intent of this app is to show how to configure the CCL in order to 
 * generate manchester-encoded data.  Data is output via CCL_OUT[0], which 
 * is configured on pin PA07.  The source data is in a 10-character buffer
 * called mybuffer[], and is sent out via an open-loop SPI Tx in code below.
 * The source data is in the MOSI line, on pin PA08 and the clock is pin PA09.
*******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "app_l21.h"

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
    This structure should be initialized by the APP_L21_Initialize function.

    Application strings and buffers are be defined outside this structure.
*/

APP_L21_DATA app_l21Data;

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
SERCOM_SPI_CALLBACK mycallback(uintptr_t context)
{
     SERCOM0_SPI_Write(mybuffer, SIZE);
}

// *****************************************************************************
// *****************************************************************************
// Section: Application Initialization and State Machine Functions
// *****************************************************************************
// *****************************************************************************

/*******************************************************************************
  Function:
    void APP_L21_Initialize ( void )

  Remarks:
    See prototype in app_l21.h.
 */

void APP_L21_Initialize ( void )
{
    /* Place the App state machine in its initial state. */
    app_l21Data.state = APP_L21_STATE_INIT;



    /* TODO: Initialize your application's state machine and other
     * parameters.
     */
}


/******************************************************************************
  Function:
    void APP_L21_Tasks ( void )

  Remarks:
    See prototype in app_l21.h.
 */

void APP_L21_Tasks ( void )
{

    /* Check the application's current state. */
    switch ( app_l21Data.state )
    {
        /* Application's initial state. */
        case APP_L21_STATE_INIT:
        {
            bool appInitialized = true;


            if (appInitialized)
            {
                SERCOM0_SPI_CallbackRegister(mycallback, NULL);
                SERCOM0_SPI_Write(mybuffer, SIZE);
                app_l21Data.state = APP_L21_STATE_SERVICE_TASKS;
            }
            break;
        }

        case APP_L21_STATE_SERVICE_TASKS:
        {
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
