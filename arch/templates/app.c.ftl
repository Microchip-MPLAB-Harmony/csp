<#assign APP_TASK_NAME_STR = "${APP_NAME}">
<#assign APP_TASK_NAME = APP_TASK_NAME_STR?eval>
/*******************************************************************************
  MPLAB Harmony Application Source File

  Company:
    Microchip Technology Inc.

  File Name:
    ${APP_TASK_NAME?lower_case}.c

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

#include "${APP_TASK_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Application Data

  Summary:
    Holds application data

  Description:
    This structure holds the application's data.

  Remarks:
    This structure should be initialized by the ${APP_TASK_NAME?upper_case}_Initialize function.

    Application strings and buffers are be defined outside this structure.
*/

${APP_TASK_NAME?upper_case}_DATA ${APP_TASK_NAME?lower_case}Data;

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
    void ${APP_TASK_NAME?upper_case}_Initialize ( void )

  Remarks:
    See prototype in ${APP_TASK_NAME?lower_case}.h.
 */

void ${APP_TASK_NAME?upper_case}_Initialize ( void )
{
    /* Place the App state machine in its initial state. */
    ${APP_TASK_NAME?lower_case}Data.state = ${APP_TASK_NAME?upper_case}_STATE_INIT;



    /* TODO: Initialize your application's state machine and other
     * parameters.
     */
}


/******************************************************************************
  Function:
    void ${APP_TASK_NAME?upper_case}_Tasks ( void )

  Remarks:
    See prototype in ${APP_TASK_NAME?lower_case}.h.
 */

void ${APP_TASK_NAME?upper_case}_Tasks ( void )
{

    /* Check the application's current state. */
    switch ( ${APP_TASK_NAME?lower_case}Data.state )
    {
        /* Application's initial state. */
        case ${APP_TASK_NAME?upper_case}_STATE_INIT:
        {
            bool appInitialized = true;


            if (appInitialized)
            {

                ${APP_TASK_NAME?lower_case}Data.state = ${APP_TASK_NAME?upper_case}_STATE_SERVICE_TASKS;
            }
            break;
        }

        case ${APP_TASK_NAME?upper_case}_STATE_SERVICE_TASKS:
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
