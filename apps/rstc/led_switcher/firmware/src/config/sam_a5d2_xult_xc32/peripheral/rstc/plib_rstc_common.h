#ifndef PLIB_RSTC_COMMON_H
#define PLIB_RSTC_COMMON_H
/*******************************************************************************
  Reset Controller Peripheral Library, RSTC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rstc.h

  Summary:
    RSTC PLIB header file

  Description:
    Interface and data type declarations for the RSTC PLIB.
    The RSTC PLIB provides access to and control of the associated
    reset controller.

  Remarks:
    None

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

/* Reset cause

  Summary:
    Identifiers for the cause of reset.

  Description:
    This enumeration provides identifiers for General, Backup, Watchdog,
    Software or User reset causes.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/
typedef enum
{
    /* First power reset */
    RSTC_GENERAL_RESET =    RSTC_SR_RSTTYP_GENERAL_RST,
    /* Reset after wake up mode */
    RSTC_WAKEUP_RESET =     RSTC_SR_RSTTYP_WKUP_RST,
    /* Reset when Watchdog fault occurred */
    RSTC_WATCHDOG_RESET =   RSTC_SR_RSTTYP_WDT_RST,
    /* Reset caused by dedicated software instruction */
    RSTC_SOFTWARE_RESET =   RSTC_SR_RSTTYP_SOFT_RST,
    /* Reset occurs when NRST pin is detected low */
    RSTC_USER_RESET =       RSTC_SR_RSTTYP_USER_RST
} RSTC_RESET_CAUSE;

/* Reset type

  Summary:
    Identifiers for the type of reset.

  Description:
    This enumeration provides identifiers for use with the reset command.

  Remarks:
    Currently processor reset is the sole stimulus.
*/
typedef enum
{
    /* Processor reset */
    RSTC_RESET_PROC = 		RSTC_CR_PROCRST_Msk
} RSTC_RESET_TYPE;

typedef void (* RSTC_CALLBACK)(uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************
typedef struct
{
    RSTC_CALLBACK	callback;
    uintptr_t     	context;
} RSTC_OBJECT;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_RSTC_COMMON_H

