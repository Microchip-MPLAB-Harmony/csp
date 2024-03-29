/*******************************************************************************
  Reset Controller(${RSTC_INSTANCE_NAME}) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_${RSTC_INSTANCE_NAME?lower_case}.h

  Summary
    ${RSTC_INSTANCE_NAME} PLIB Header File.

  Description
    This file defines the interface to the RSTC peripheral library.
    This library provides access to and control of the associated
    Reset Controller.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${RSTC_INSTANCE_NAME}_H      // Guards against multiple inclusion
#define PLIB_${RSTC_INSTANCE_NAME}_H

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
// Section:Preprocessor macros
// *****************************************************************************
// *****************************************************************************

<#list 0..(RSTC_RCAUSE_LENGTH - 1) as i>
<#assign resetReason = "RSTC_RCAUSE" + i>
#define RSTC_RESET_CAUSE_${.vars[resetReason]}_RESET  RSTC_RCAUSE_${.vars[resetReason]}_Msk

</#list>

<#list 0..(RSTC_BKUPEXIT_LENGTH - 1) as i>
<#assign resetBckup = "RSTC_BKUPEXIT" + i>
#define RSTC_BKUPEXIT_CAUSE_${.vars[resetBckup]}  RSTC_BKUPEXIT_${.vars[resetBckup]}_Msk

</#list>

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
    This enums identifies either Power On Reset, Brown Out CORE Detector Reset,
    Brown Out VDDREG Detector Reset, Brown Out VDDA Detector Reset, Brown Out VDDIO Detector Reset,
    External Reset, Watchdog Reset, System Reset, Backup Reset or Lockup Reset.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/

typedef uint32_t RSTC_RESET_CAUSE;

typedef uint32_t RSTC_BKUPEXIT_CAUSE;

RSTC_BKUPEXIT_CAUSE RSTC_BackupExitCauseGet(void);

RSTC_RESET_CAUSE ${RSTC_INSTANCE_NAME}_ResetCauseGet(void);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif

#endif /* PLIB_${RSTC_INSTANCE_NAME}_H */
