/*******************************************************************************
  System Initialization File

  File Name:
    initialization.c

  Summary:
    This file contains source code necessary to initialize the system.

  Description:
    This file contains source code necessary to initialize the system.  It
    implements the "SYS_Initialize" function, defines the configuration bits,
    and allocates any necessary global system resources,
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
<#if HarmonyCore??>
    <#if HarmonyCore.ENABLE_APP_FILE == true >
        <#lt>#include "configuration.h"
    </#if>
</#if>
#include "definitions.h"
#include "device.h"



// ****************************************************************************
// ****************************************************************************
// Section: Configuration Bits
// ****************************************************************************
// ****************************************************************************
${LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION}


// *****************************************************************************
// *****************************************************************************
// Section: Driver Initialization Data
// *****************************************************************************
// *****************************************************************************
${LIST_SYSTEM_INIT_C_DRIVER_INITIALIZATION_DATA}

// *****************************************************************************
// *****************************************************************************
// Section: System Data
// *****************************************************************************
// *****************************************************************************
<#if HarmonyCore??>
    <#if HarmonyCore.ENABLE_APP_FILE == true >
        <#lt>/* Structure to hold the object handles for the modules in the system. */
        <#lt>SYSTEM_OBJECTS sysObj;
    </#if>
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Library/Stack Initialization Data
// *****************************************************************************
// *****************************************************************************
${LIST_SYSTEM_INIT_C_LIBRARY_INITIALIZATION_DATA}

// *****************************************************************************
// *****************************************************************************
// Section: System Initialization
// *****************************************************************************
// *****************************************************************************
${LIST_SYSTEM_INIT_C_SYSTEM_INITIALIZATION}


/*******************************************************************************
  Function:
    void SYS_Initialize ( void *data )

  Summary:
    Initializes the board, services, drivers, application and other modules.

  Remarks:
 */

void SYS_Initialize ( void* data )
{
    <#lt>${LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START}  <#-- global disable of interrupts before initializing anything -->
    <#lt>${LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE}
    <#lt>${LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS}
    <#lt>${LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS}
    <#lt>${LIST_SYSTEM_INIT_C_INITIALIZE_SYSTEM_SERVICES}
    <#lt>${LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE}
    <#if HarmonyCore??>
        <#lt><#if HarmonyCore.ENABLE_APP_FILE == true >
                <#lt>${LIST_SYSTEM_INIT_C_APP_INITIALIZE_DATA}
        <#lt></#if>
    </#if>
    <#lt>${LIST_SYSTEM_INIT_INTERRUPTS}
}


/*******************************************************************************
 End of File
*/
