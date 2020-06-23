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

/* typedef for non-secure callback functions */
typedef void (*funcptr_void) (void) __attribute__((cmse_nonsecure_call));
<#if GENERATE_SECURE_BOOT_MAIN_FILE?? && GENERATE_SECURE_BOOT_MAIN_FILE == true>
/* typedef for secure callback functions */
typedef void (*secureFuncptr_void) (void);
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint32_t msp_ns = *((uint32_t *)(TZ_START_NS));
<#if GENERATE_SECURE_BOOT_MAIN_FILE?? && GENERATE_SECURE_BOOT_MAIN_FILE == true>
    uint32_t msp_s = *((uint32_t *)(TZ_START_S));
</#if>
    volatile funcptr_void NonSecure_ResetHandler;
<#if GENERATE_SECURE_BOOT_MAIN_FILE?? && GENERATE_SECURE_BOOT_MAIN_FILE == true>
    volatile secureFuncptr_void Secure_ResetHandler;
</#if>

    /* Initialize all modules */
    SYS_Initialize ( NULL );

<#if GENERATE_SECURE_BOOT_MAIN_FILE?? && GENERATE_SECURE_BOOT_MAIN_FILE == true>
    if (msp_s != 0xFFFFFFFF)
    {
        /* Set secure main stack (MSP) */
        __set_MSP(msp_s);

        /* Get secure reset handler */
        Secure_ResetHandler = (secureFuncptr_void)(*((uint32_t *)((TZ_START_S) + 4U)));

        /* Start secure state software application */
        Secure_ResetHandler();
    }
    else <#else>    </#if>if (msp_ns != 0xFFFFFFFF)
    {
        /* Set non-secure main stack (MSP_NS) */
        __TZ_set_MSP_NS(msp_ns);

        /* Get non-secure reset handler */
        NonSecure_ResetHandler = (funcptr_void)(*((uint32_t *)((TZ_START_NS) + 4U)));

        /* Start non-secure state software application */
        NonSecure_ResetHandler();
    }

    while ( true )
    {
    }

    /* Execution should not come here during normal operation */
    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

