/*******************************************************************************
  Reset Controller (RSTC) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RSTC_INSTANCE_NAME?lower_case}.h

  Summary:
    Interface definition of the RSTC PLIB Header File

  Description:
    None

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${RSTC_INSTANCE_NAME}_H // Guards against multiple inclusion
#define PLIB_${RSTC_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include <stdbool.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

typedef enum
{
    /* Processor reset */
    RSTC_PROCESSOR_RESET = RSTC_CR_PROCRST_Msk${RSTC_PERRST_SUPPORT?string(" | RSTC_CR_PERRST_Msk", "")},

    /* External reset */
    RSTC_EXTERNAL_RESET = RSTC_CR_EXTRST_Msk,

    /* Processor and External reset */
    RSTC_ALL_RESET = RSTC_CR_EXTRST_Msk | RSTC_CR_PROCRST_Msk${RSTC_PERRST_SUPPORT?string(" | RSTC_CR_PERRST_Msk", "")},

} RSTC_RESET_TYPE;

/* Reset cause

  Summary:
    Identifiers for the cause of reset.

  Description:
    This enumeration provides identifiers for General, Backup, Watchdog,
    Software or User reset causes.

  Remarks:
    Refer to the specific device data sheet to determine availability.
*/

#define    RSTC_GENERAL_RESET      (RSTC_SR_RSTTYP_GENERAL_RST_Val)         // First power reset
#define    RSTC_BACKUP_RESET       (RSTC_SR_RSTTYP_BACKUP_RST_Val)          // VDD Core reset. Wakeup from Backup mode
#define    RSTC_WDT0_RESET         (RSTC_SR_RSTTYP_WDT0_RST_Val)            // Watchdog 0 fault occurred
#define    RSTC_SOFTWARE_RESET     (RSTC_SR_RSTTYP_SOFT_RST_Val)            // Processor reset requested by the software
#define    RSTC_USER_RESET         (RSTC_SR_RSTTYP_USER_RST_Val)            // NRST pin detected low 
#define    RSTC_CORE_SM_RESET      (RSTC_SR_RSTTYP_CORE_SM_RST_Val)         // Core Supply Monitor reset
#define    RSTC_CPU_FAIL_RESET     (RSTC_SR_RSTTYP_CPU_FAIL_RST_Val)        // CPU clock failure detection occurred
#define    RSTC_SLCK_XTAL_RESET    (RSTC_SR_RSTTYP_SLCK_XTAL_RST_Val)       // 32.768 kHz crystal failure detection fault
#define    RSTC_WDT1_RESET         (RSTC_SR_RSTTYP_WDT1_RST_Val)            // Watchdog 1 fault occurred
#define    RSTC_PORVDD3V3_RESET    (RSTC_SR_RSTTYP_PORVDD3V3_RST_Val)       // VDD3V3 PORVDD3V3 reset occurred

typedef uint32_t RSTC_RESET_CAUSE;

typedef void (*RSTC_CALLBACK) (uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
void ${RSTC_INSTANCE_NAME}_Initialize (void);

void ${RSTC_INSTANCE_NAME}_Reset (RSTC_RESET_TYPE type);

RSTC_RESET_CAUSE ${RSTC_INSTANCE_NAME}_ResetCauseGet (void);
<#if RSTC_MR_URSTEN == "No action">

bool ${RSTC_INSTANCE_NAME}_NRSTPinRead (void);
</#if>
<#if RSTC_MR_CPROCEN??>

void ${RSTC_INSTANCE_NAME}_CoProcessorEnable(bool enable);
</#if>
<#if RSTC_MR_CPEREN??>

void ${RSTC_INSTANCE_NAME}_CoProcessorPeripheralEnable(bool enable);
</#if>
<#if INTERRUPT_ENABLE>

void ${RSTC_INSTANCE_NAME}_CallbackRegister(RSTC_CALLBACK pCallback, uintptr_t context);
</#if>


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END

#endif // PLIB_${RSTC_INSTANCE_NAME}_H