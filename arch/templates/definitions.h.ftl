/*******************************************************************************
  System Definitions

  File Name:
    definitions.h

  Summary:
    project system definitions.

  Description:
    This file contains the system-wide prototypes and definitions for a project.

 *******************************************************************************/

//DOM-IGNORE-BEGIN
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
//DOM-IGNORE-END

#ifndef DEFINITIONS_H
#define DEFINITIONS_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
<#if stdio?? >
    <#lt>#include <stdio.h>
</#if>
<#compress>
${LIST_SYSTEM_DEFINITIONS_H_INCLUDES}
</#compress>

<#if HarmonyCore??>
    <#if HarmonyCore.ENABLE_APP_FILE == true >
        <#lt>${LIST_SYSTEM_APP_DEFINITIONS_H_INCLUDES}
    </#if>
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

extern "C" {

#endif
// DOM-IGNORE-END

/* CPU clock frequency */
#define CPU_CLOCK_FREQUENCY ${CPU_CLOCK_FREQUENCY}

// *****************************************************************************
// *****************************************************************************
// Section: System Functions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* System Initialization Function

  Function:
    void SYS_Initialize( void *data )

  Summary:
    Function that initializes all modules in the system.

  Description:
    This function initializes all modules in the system, including any drivers,
    services, middleware, and applications.

  Precondition:
    None.

  Parameters:
    data            - Pointer to the data structure containing any data
                      necessary to initialize the module. This pointer may
                      be null if no data is required and default initialization
                      is to be used.

  Returns:
    None.

  Example:
    <code>
    SYS_Initialize ( NULL );

    while ( true )
    {
        SYS_Tasks ( );
    }
    </code>

  Remarks:
    This function will only be called once, after system reset.
*/

void SYS_Initialize( void *data );

<#if HarmonyCore??>
    <#if HarmonyCore.ENABLE_DRV_COMMON == true ||
         HarmonyCore.ENABLE_SYS_COMMON == true ||
         HarmonyCore.ENABLE_APP_FILE == true >
        <#lt>// *****************************************************************************
        <#lt>/* System Tasks Function

        <#lt>Function:
        <#lt>    void SYS_Tasks ( void );

        <#lt>Summary:
        <#lt>    Function that performs all polled system tasks.

        <#lt>Description:
        <#lt>    This function performs all polled system tasks by calling the state machine
        <#lt>    "tasks" functions for all polled modules in the system, including drivers,
        <#lt>    services, middleware and applications.

        <#lt>Precondition:
        <#lt>    The SYS_Initialize function must have been called and completed.

        <#lt>Parameters:
        <#lt>    None.

        <#lt>Returns:
        <#lt>    None.

        <#lt>Example:
        <#lt>    <code>
        <#lt>    SYS_Initialize ( NULL );

        <#lt>    while ( true )
        <#lt>    {
        <#lt>        SYS_Tasks ( );
        <#lt>    }
        <#lt>    </code>

        <#lt>Remarks:
        <#lt>    If the module is interrupt driven, the system will call this routine from
        <#lt>    an interrupt context.
        <#lt>*/

        <#lt>void SYS_Tasks ( void );

        <#if HarmonyCore.ENABLE_DRV_COMMON == true ||
            HarmonyCore.ENABLE_SYS_COMMON == true >
            <#lt>// *****************************************************************************
            <#lt>// *****************************************************************************
            <#lt>// Section: Type Definitions
            <#lt>// *****************************************************************************
            <#lt>// *****************************************************************************

            <#lt>// *****************************************************************************
            <#lt>/* System Objects

            <#lt>Summary:
            <#lt>    Structure holding the system's object handles

            <#lt>Description:
            <#lt>    This structure contains the object handles for all objects in the
            <#lt>    MPLAB Harmony project's system configuration.

            <#lt>Remarks:
            <#lt>    These handles are returned from the "Initialize" functions for each module
            <#lt>    and must be passed into the "Tasks" function for each module.
            <#lt>*/

            <#lt>typedef struct
            <#lt>{
            <#if LIST_SYSTEM_DEFINITIONS_H_OBJECTS?length gt 0>
                <#lt>${LIST_SYSTEM_DEFINITIONS_H_OBJECTS}
            <#else>
                <#lt>    char RESERVED;
            </#if>
            <#lt>} SYSTEM_OBJECTS;
        </#if>
    <#else>
        <#lt>/* Nullify SYS_Tasks() if only PLIBs are used. */
        <#lt>#define     SYS_Tasks()
    </#if>
<#else>
    <#lt>/* Nullify SYS_Tasks() if only PLIBs are used. */
    <#lt>#define     SYS_Tasks()
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: extern declarations
// *****************************************************************************
// *****************************************************************************

${LIST_SYSTEM_DEFINITIONS_H_EXTERNS}

<#if HarmonyCore??>
    <#if HarmonyCore.ENABLE_DRV_COMMON == true ||
         HarmonyCore.ENABLE_SYS_COMMON == true >
        <#lt>extern SYSTEM_OBJECTS sysObj;
    </#if>
</#if>

//DOM-IGNORE-BEGIN
#ifdef __cplusplus
}
#endif
//DOM-IGNORE-END

#endif /* DEFINITIONS_H */
/*******************************************************************************
 End of File
*/

