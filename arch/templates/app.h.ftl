<#assign APP_TASK_NAME_STR = "${APP_NAME}">
<#assign APP_TASK_NAME = APP_TASK_NAME_STR?eval>
/*******************************************************************************
  MPLAB Harmony Application Header File

  Company:
    Microchip Technology Inc.

  File Name:
    ${APP_TASK_NAME?lower_case}.h

  Summary:
    This header file provides prototypes and definitions for the application.

  Description:
    This header file provides function prototypes and data type definitions for
    the application.  Some of these are required by the system (such as the
    "${APP_TASK_NAME?upper_case}_Initialize" and "${APP_TASK_NAME?upper_case}_Tasks" prototypes) and some of them are only used
    internally by the application (such as the "${APP_TASK_NAME?upper_case}_STATES" definition).  Both
    are defined here for convenience.
*******************************************************************************/

#ifndef _${APP_TASK_NAME?upper_case}_H
#define _${APP_TASK_NAME?upper_case}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>
#include "configuration.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Type Definitions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Application states

  Summary:
    Application states enumeration

  Description:
    This enumeration defines the valid application states.  These states
    determine the behavior of the application at various times.
*/

typedef enum
{
    /* Application's state machine's initial state. */
    ${APP_TASK_NAME?upper_case}_STATE_INIT=0,
    ${APP_TASK_NAME?upper_case}_STATE_SERVICE_TASKS,
    /* TODO: Define states used by the application state machine. */

} ${APP_TASK_NAME?upper_case}_STATES;


// *****************************************************************************
/* Application Data

  Summary:
    Holds application data

  Description:
    This structure holds the application's data.

  Remarks:
    Application strings and buffers are be defined outside this structure.
 */

typedef struct
{
    /* The application's current state */
    ${APP_TASK_NAME?upper_case}_STATES state;

    /* TODO: Define any additional data used by the application. */

} ${APP_TASK_NAME?upper_case}_DATA;


// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Routines
// *****************************************************************************
// *****************************************************************************
/* These routines are called by drivers when certain events occur.
*/

// *****************************************************************************
// *****************************************************************************
// Section: Application Initialization and State Machine Functions
// *****************************************************************************
// *****************************************************************************

/*******************************************************************************
  Function:
    void ${APP_TASK_NAME?upper_case}_Initialize ( void )

  Summary:
     MPLAB Harmony application initialization routine.

  Description:
    This function initializes the Harmony application.  It places the
    application in its initial state and prepares it to run so that its
    APP_Tasks function can be called.

  Precondition:
    All other system initialization routines should be called before calling
    this routine (in "SYS_Initialize").

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    ${APP_TASK_NAME?upper_case}_Initialize();
    </code>

  Remarks:
    This routine must be called from the SYS_Initialize function.
*/

void ${APP_TASK_NAME?upper_case}_Initialize ( void );


/*******************************************************************************
  Function:
    void ${APP_TASK_NAME?upper_case}_Tasks ( void )

  Summary:
    MPLAB Harmony Demo application tasks function

  Description:
    This routine is the Harmony Demo application's tasks function.  It
    defines the application's state machine and core logic.

  Precondition:
    The system and application initialization ("SYS_Initialize") should be
    called before calling this.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
    ${APP_TASK_NAME?upper_case}_Tasks();
    </code>

  Remarks:
    This routine must be called from SYS_Tasks() routine.
 */

void ${APP_TASK_NAME?upper_case}_Tasks( void );



#endif /* _${APP_TASK_NAME?upper_case}_H */

//DOM-IGNORE-BEGIN
#ifdef __cplusplus
}
#endif
//DOM-IGNORE-END

/*******************************************************************************
 End of File
 */

