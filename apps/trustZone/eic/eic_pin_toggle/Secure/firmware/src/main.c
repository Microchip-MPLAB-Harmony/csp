/*******************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

#define TZ_START_NS 0x00008000

/* typedef for non-secure callback functions */
typedef void (*funcptr_void) (void) __attribute__((cmse_nonsecure_call));

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
void SWITCH_handler(uintptr_t context)
{
	LED_SECURE_Toggle();
    
}
int main ( void )
{
    volatile funcptr_void NonSecure_ResetHandler;

    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    EIC_CallbackRegister(EIC_PIN_5, SWITCH_handler,  (uintptr_t) NULL);

    /* Set non-secure main stack (MSP_NS) */
    __TZ_set_MSP_NS(*((uint32_t *)(TZ_START_NS)));
    
    /* Get non-secure reset handler */
    NonSecure_ResetHandler = (funcptr_void)(*((uint32_t *)((TZ_START_NS) + 4U)));
    
    /* Start non-secure state software application */
    NonSecure_ResetHandler();

    /* Execution should not come here during normal operation */
    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

