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

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

