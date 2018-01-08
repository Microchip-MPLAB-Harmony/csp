/*******************************************************************************
  PIO Plib Local

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pio_local.h

  Summary:
    PIO Plib local Header File

  Description:
    This library provides local interface and enums to be used internally in the
    implementation of Parallel Input/Output controller (PIO) PLIB.

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#ifndef PLIB_PIO_LOCAL_H
#define PLIB_PIO_LOCAL_H

#include <xc.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <sys/attribs.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data types and constants
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* PIO Pin Callback Object

  Summary:
    Structure to hold callback related details

  Description:
    This structure is used internally by the PIO Plib to hold pin specific
    callback details.

  Remarks:
    None.
*/
typedef struct {

    /* target pin */
    PIO_PIN                 pin;

    /* Callback for event on target pin*/
    PIO_EVENT_HANDLER       callback;

    /* Callback Context */
    void*               context;

} PIO_PIN_CALLBACK_OBJ;

// *****************************************************************************
/* Function:
    void _PIO_Interrupt_Handler ( PIO_CHANNEL channel )

  Summary:
    Interrupt handler for a selected channel.

  Description:
    This function defines the Interrupt handler for a selected channel.

  Remarks:
	It is an internal function used by the library, user need not call it.
*/
void _PIO_Interrupt_Handler ( PIO_CHANNEL channel );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_PIO_LOCAL_H