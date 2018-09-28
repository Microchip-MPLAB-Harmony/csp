/*******************************************************************************
Data Type definition of Reset Controller (RSTC) Peripheral Library (PLIB).

 Company:
    Microchip Technology Inc.

 File Name:
    plib_rstc.h

 Summary:
    Data Type definition of the RSTC Peripheral Interface Plib.

 Description:
    This file defines the Data Types for the RSTC Plib.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_RSTC_COMMON_H // Guards against multiple inclusion
#define PLIB_RSTC_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/* This section lists the other files that are included in this file.
*/

#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

/* User Reset type

  Summary:
    Identifies the type of reset.

  Description:
    This enums identifies either General, Backup, Watchdog, Software or User 
    Reset

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/

typedef enum
{
    /* First power reset */
    RSTC_GENERAL_RESET = RSTC_SR_RSTTYP_GENERAL_RST, 

    /* Reset after Return from Backup mode */
    RSTC_BACKUP_RESET = RSTC_SR_RSTTYP_BACKUP_RST,

    /* Reset when Watchdog fault occurred */
    RSTC_WATCHDOG_RESET = RSTC_SR_RSTTYP_WDT_RST,

    /* Reset caused by dedicated software instruction */
    RSTC_SOFTWARE_RESET = RSTC_SR_RSTTYP_SOFT_RST,

    /* Reset occurs when NRST pin is detected low */
    RSTC_USER_RESET = RSTC_SR_RSTTYP_USER_RST,

} RSTC_RESET_CAUSE;

/* Reset type

   Summary:
    Identifies the type of reset, either Processor reset or External Reset.

   Description:
    This enums identifies either Processor reset or External Reset.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/

typedef enum
{
    /* Processor reset */
    RSTC_RESET_PROC = RSTC_CR_PROCRST_Msk,

    /* External reset */
    RSTC_RESET_EXT = RSTC_CR_EXTRST_Msk,

    /* Processor and External reset */
    RSTC_RESET_EXT_PROC = (RSTC_CR_PROCRST_Msk | RSTC_CR_EXTRST_Msk) 

} RSTC_RESET_TYPE;

typedef void (*RSTC_CALLBACK) (uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

typedef struct
{
    RSTC_CALLBACK callback; 
    uintptr_t     context;
    
} RSTC_OBJECT ;


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_RSTC_COMMON_H