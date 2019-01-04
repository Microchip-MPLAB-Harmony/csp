/*******************************************************************************
  Reset Controller(RSTC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_rstc.h

  Summary
    RSTC PLIB Header File.

  Description
    This file defines the interface to the RSTC peripheral library.
    This library provides access to and control of the associated
    Reset Controller.

  Remarks:
    None.

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

#ifndef PLIB_RSTC_H      // Guards against multiple inclusion
#define PLIB_RSTC_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdbool.h>
#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/* The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************
/* User Reset type

  Summary:
    Identifies the type of reset.

  Description:
    This enums identifies either General, Backup, Watchdog, Software
    or User Reset.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/

typedef enum
{

    RSTC_RESET_CAUSE_POR_RESET = RSTC_RCAUSE_POR_Msk,

    RSTC_RESET_CAUSE_BODCORE_RESET = RSTC_RCAUSE_BODCORE_Msk,

    RSTC_RESET_CAUSE_BODVDD_RESET = RSTC_RCAUSE_BODVDD_Msk,

    RSTC_RESET_CAUSE_NVM_RESET = RSTC_RCAUSE_NVM_Msk,

    RSTC_RESET_CAUSE_EXT_RESET = RSTC_RCAUSE_EXT_Msk,

    RSTC_RESET_CAUSE_WDT_RESET = RSTC_RCAUSE_WDT_Msk,

    RSTC_RESET_CAUSE_SYST_RESET = RSTC_RCAUSE_SYST_Msk,

    RSTC_RESET_CAUSE_BACKUP_RESET = RSTC_RCAUSE_BACKUP_Msk,

} RSTC_RESET_CAUSE;

typedef enum
{

    RSTC_BKUPEXIT_CAUSE_RTC = RSTC_BKUPEXIT_RTC_Msk,

    RSTC_BKUPEXIT_CAUSE_BBPS = RSTC_BKUPEXIT_BBPS_Msk,

    RSTC_BKUPEXIT_CAUSE_HIB = RSTC_BKUPEXIT_HIB_Msk,

} RSTC_BKUPEXIT_CAUSE;

RSTC_BKUPEXIT_CAUSE RSTC_BackupExitCauseGet (void);

RSTC_RESET_CAUSE RSTC_ResetCauseGet (void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

#endif /* PLIB_RSTC_H */
