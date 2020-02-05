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
#include "trustZone/veneer.h"

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

enum
{
  ADD = 'a',
  MULTIPLY = 'b',
}MATH_OPERATIONS;

uint8_t cmd = 0;

void display_menu (void)
{
    printf("\n\n\n\rSelect the Math Operation");
    printf("\n\ra) Add");
    printf("\n\rb) Multiply"); 
    printf("\n\rEnter your choice");    
    scanf("%c", &cmd);
}
int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    printf("\n\r-------------------------------------------------------------");
    printf("\n\r\t\t TrustZone DEMO\t\t");
    printf("\n\r-------------------------------------------------------------");
    display_menu();
    
    uint16_t x = 0;
    uint16_t y = 0;
    uint32_t result = 0;
    while(1)
    {
        switch(cmd)
        {
            case ADD:
            {
                printf("\n\rEnter the first 16 bit unsigned number:- \t");
                scanf("%hu", &x);
                printf("\n\rEnter the second 16 bit unsigned number:- \t");
                scanf("%hu", &y);
                result = secure_add(x, y);

                printf("\n\rThe first 16 bit unsigned number is:- %hu\t", x);
                printf("\n\rThe first 16 bit unsigned number is:- %hu\t", y);
                printf("\n\rThe result is:- \t%lu", result);

                display_menu();
                break;
            }
            case MULTIPLY:
            {
                printf("\n\rEnter the first 16 bit unsigned number:- \t");
                scanf("%hu", &x);
                printf("\n\rEnter the second 16 bit unsigned number:- \t");
                scanf("%hu", &y);
                result = secure_multiply(x, y);
                
                printf("\n\rThe first 16 bit unsigned number is:- %hu\t", x);
                printf("\n\rThe first 16 bit unsigned number is:- %hu\t", y);
                printf("\n\rThe result is:- \t%lu", result);
                display_menu();
                break;
            }
            default:
            {
                if ((int)(cmd) != 13)
                {
                    printf("\n\rInvalid choice:- %c", cmd);
                    display_menu();
                }
                else
                {
                    scanf("%c", &cmd);
                }
                
                break;
            }
        } 
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

