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

/*******************************************************************************
Copyright (c) 2017-18 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
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
#include <string.h>

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

bool result = true;
#define BUFFER_SIZE         ((256 * 1024) / 4)   // 256 KB
#define WRITE_READ_SIZE     256

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    uint32_t readBuf[BUFFER_SIZE];
    uint32_t *addr;
    bool result = true;

    printf("\n\r-------------------------------------------------------");
    printf("\n\r               SDRAM WRITE - READ Example");
    printf("\n\r-------------------------------------------------------");

    addr = (uint32_t *)SDRAM_CS_ADDR;
    for (int i = 0; i < 8; i++)
    {
        printf("\n\r Writing \t%d \tto %d KB data to SDRAM.", (i * WRITE_READ_SIZE), ((i + 1) * WRITE_READ_SIZE));
        for (uint32_t i = 0; i < BUFFER_SIZE; i++)
        {
           *addr = ((i << 16) + i);
           addr++;
        }
    }

    printf("\n");
    addr = (uint32_t *)SDRAM_CS_ADDR;

    memset(readBuf, 0, sizeof(BUFFER_SIZE * 4));

    for (int i = 0; i < 8; i++)
    {
        printf("\n\r Reading \t%d \tto %d KB data from SDRAM.", (i * WRITE_READ_SIZE), ((i + 1) * WRITE_READ_SIZE));
        for (uint32_t i = 0; i < BUFFER_SIZE; i++)
        {
           readBuf[i] = *addr;
           addr++;
        }

        printf("\n\r Comparing \t%d \tto %d KB data.", (i * WRITE_READ_SIZE), ((i + 1) * WRITE_READ_SIZE));
        for (uint32_t i = 0; i < BUFFER_SIZE; i++)
        {
           if (readBuf[i] != (i << 16) + i)
           {
               result = false;
               break;
           }
        }
    }

    if(result)
    {
        printf("\n\n\r Test Pass....");
    }
    else
    {
        printf("\n\n\rTest Fail....");
    }

    while(1);
}


/*******************************************************************************
 End of File
*/

