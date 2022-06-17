/*******************************************************************************
  PCR PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pcr.h

  Summary:
    PCR PLIB Header File.

  Description:
    The PCR PLIB initializes all the oscillators based on the
    requirements.

*******************************************************************************/

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

#ifndef PLIB_PCR_H
#define PLIB_PCR_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/
#include <device.h>
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

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


<#list 0..(NUM_SLEEP_EN_REGS-1) as n>
<#assign PCR_SLEEP_EN         = "PCR_SLEEP_ENABLE" + n + "_REG_INDEX">
<#assign PCR_SLEEP_EN_LIST    = "PCR_SLEEP_ENABLE" + n + "_ENUM_LIST">
typedef enum
{
    ${.vars[PCR_SLEEP_EN_LIST]}
}PCR_SLEEP_EN${.vars[PCR_SLEEP_EN]};

</#list>

<#list 0..(NUM_PRIV_EN_REGS-1) as n>
<#assign PCR_PRIV_EN         = "PCR_PRIV_ENABLE" + n + "_REG_INDEX">
<#assign PCR_PRIV_EN_LIST    = "PCR_PRIV_ENABLE" + n + "_ENUM_LIST">
typedef enum
{
    ${.vars[PCR_PRIV_EN_LIST]}
}PCR_PRIV_EN${.vars[PCR_PRIV_EN]};

</#list>

<#list 0..(NUM_RESET_EN_REGS-1) as n>
<#assign PCR_RESET_EN         = "PCR_RESET_ENABLE" + n + "_REG_INDEX">
<#assign PCR_RESET_EN_LIST    = "PCR_RESET_ENABLE" + n + "_ENUM_LIST">
typedef enum
{
    ${.vars[PCR_RESET_EN_LIST]}
}PCR_RESET_EN${.vars[PCR_RESET_EN]};

</#list>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
this interface.
*/

// *****************************************************************************
/* Function:
    void PCR_Initialize (void);

  Summary:
    Initializes all the modules related to PCR.

  Description:
    This function initializes the clock as defined by the MCC and Clock Manager
    selections.

  Precondition:
    MCC GUI should be configured with the right values. Incorrect configuration
    of the Clock will result in incorrect peripheral behavior or a non
    functional device.

  Parameters:
    None.

  Returns:
    None.

  Example:
    <code>
        PCR_Initialize();
    </code>

  Remarks:
    This function should be called before calling other Clock library functions.
*/

void PCR_Initialize (void);

void PCR_PeripheralResetLock (void);

void PCR_PeripheralResetUnLock (void);

void PCR_PrivilegeEnLock (void);

void PCR_PrivilegeEnUnLock (void);

<#list 0..(NUM_SLEEP_EN_REGS-1) as n>
<#assign PCR_SLEEP_EN         = "PCR_SLEEP_ENABLE" + n + "_REG_INDEX">
void PCR_SleepEnable${.vars[PCR_SLEEP_EN]} (PCR_SLEEP_EN${.vars[PCR_SLEEP_EN]} blockId);
void PCR_SleepDisable${.vars[PCR_SLEEP_EN]} (PCR_SLEEP_EN${.vars[PCR_SLEEP_EN]} blockId);
</#list>

<#list 0..(NUM_PRIV_EN_REGS-1) as n>
<#assign PCR_PRIV_EN         = "PCR_PRIV_ENABLE" + n + "_REG_INDEX">
void PCR_PrivilegeEnable${.vars[PCR_PRIV_EN]} (PCR_PRIV_EN${.vars[PCR_PRIV_EN]} blockId);
void PCR_PrivilegeDisable${.vars[PCR_PRIV_EN]} (PCR_PRIV_EN${.vars[PCR_PRIV_EN]} blockId);
</#list>

<#list 0..(NUM_RESET_EN_REGS-1) as n>
<#assign PCR_RESET_EN         = "PCR_RESET_ENABLE" + n + "_REG_INDEX">
void PCR_ResetEnable${.vars[PCR_RESET_EN]} (PCR_RESET_EN${.vars[PCR_RESET_EN]} blockId);
</#list>


#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif /* PLIB_CLOCK_H */
