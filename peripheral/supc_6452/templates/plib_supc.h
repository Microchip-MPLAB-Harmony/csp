/*******************************************************************************
Data Type definition of Supply Controller (SUPC) Peripheral Library (PLIB).

 Company:
    Microchip Technology Inc.

 File Name:
    plib_supc.h

 Summary:
    Data Type definition of the SUPC Peripheral Interface Plib.

 Description:
    This file defines the Data Types for the SUPC Plib.

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

#ifndef PLIB_SUPC_H // Guards against multiple inclusion
#define PLIB_SUPC_H

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

typedef enum 
{
	WAITMODE_WKUP_WKUP0     = PMC_FSMR_FSTT0_Msk,      // WKUP0 Pin
	WAITMODE_WKUP_WKUP1     = PMC_FSMR_FSTT1_Msk,      // WKUP1 Pin
	WAITMODE_WKUP_WKUP2     = PMC_FSMR_FSTT2_Msk,      // WKUP2 Pin
	WAITMODE_WKUP_WKUP3     = PMC_FSMR_FSTT3_Msk,      // WKUP3 Pin
	WAITMODE_WKUP_WKUP4     = PMC_FSMR_FSTT4_Msk,      // WKUP4 Pin
	WAITMODE_WKUP_WKUP5     = PMC_FSMR_FSTT5_Msk,      // WKUP5 Pin
	WAITMODE_WKUP_WKUP6     = PMC_FSMR_FSTT6_Msk,      // WKUP6 Pin
	WAITMODE_WKUP_WKUP7     = PMC_FSMR_FSTT7_Msk,      // WKUP7 Pin
	WAITMODE_WKUP_WKUP8     = PMC_FSMR_FSTT8_Msk,      // WKUP8 Pin
	WAITMODE_WKUP_WKUP9     = PMC_FSMR_FSTT9_Msk,      // WKUP9 Pin
	WAITMODE_WKUP_WKUP10    = PMC_FSMR_FSTT10_Msk,     // WKUP10 Pin
	WAITMODE_WKUP_WKUP11    = PMC_FSMR_FSTT11_Msk,     // WKUP11 Pin            
	WAITMODE_WKUP_WKUP12    = PMC_FSMR_FSTT12_Msk,     // WKUP12 Pin
	WAITMODE_WKUP_WKUP13    = PMC_FSMR_FSTT13_Msk,     // WKUP13 Pin
	WAITMODE_WKUP_GMAC      = PMC_FSMR_FSTT14_Msk,     // GMAC          
	WAITMODE_WKUP_DEBUG     = PMC_FSMR_FSTT15_Msk,     // DEBUG
	WAITMODE_WKUP_RTT       = PMC_FSMR_RTTAL_Msk,      // RTT            
	WAITMODE_WKUP_RTC       = PMC_FSMR_RTCAL_Msk,      // RTC 
	WAITMODE_WKUP_USB       = PMC_FSMR_USBAL_Msk,      // USB             
} WAITMODE_WKUP_SOURCE;	

typedef enum 
{ 
    WAITMODE_FLASH_STANDBY = PMC_FSMR_FLPM_FLASH_STANDBY,
    WAITMODE_FLASH_DEEPSLEEP = PMC_FSMR_FLPM_FLASH_DEEP_POWERDOWN,
 } WAITMODE_FLASH_STATE;


typedef void (*SUPC_CALLBACK) (uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

typedef struct
{
    SUPC_CALLBACK callback; 
    uintptr_t     context;
} SUPC_OBJECT ;


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_SUPC_H