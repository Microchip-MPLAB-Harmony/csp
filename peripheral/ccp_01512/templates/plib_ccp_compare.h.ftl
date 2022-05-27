/*******************************************************************************
  Capture/Compare/PWM/Timer Module (CCP) Peripheral Library Interface Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CCP_INSTANCE_NAME?lower_case}.h

  Summary:
    CCP PLIB Header File

  Description:
    None

*******************************************************************************/

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

#ifndef PLIB_${CCP_INSTANCE_NAME}_H
#define PLIB_${CCP_INSTANCE_NAME}_H

#include <stddef.h>
#include <stdint.h>
#include "device.h"
#include "plib_ccp_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END


// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************
<#assign mode = CCP_COMP_CCPCON1_MOD?number>

/*************************** ${CCP_INSTANCE_NAME} API ****************************************/
// *****************************************************************************
/* Function:
   void ${CCP_INSTANCE_NAME}_CompareInitialize (void)

  Summary:
    Initialization function ${CCP_INSTANCE_NAME} peripheral

  Description:
    This function initializes the ${CCP_INSTANCE_NAME} peripheral with user input
	from the configurator.

  Parameters:
    void

  Returns:
    void
*/
void ${CCP_INSTANCE_NAME}_CompareInitialize (void);

// *****************************************************************************
/* Function:
   void ${CCP_INSTANCE_NAME}_CompareStart (void)

  Summary:
    Enable function ${CCP_INSTANCE_NAME} peripheral

  Description:
    This function enables the ${CCP_INSTANCE_NAME} peripheral

  Parameters:
    void

  Returns:
    void
*/
void ${CCP_INSTANCE_NAME}_CompareStart (void);

// *****************************************************************************
/* Function:
   void ${CCP_INSTANCE_NAME}_CompareStop (void)

  Summary:
    Disable function ${CCP_INSTANCE_NAME} peripheral

  Description:
    This function disables the ${CCP_INSTANCE_NAME} peripheral.

  Parameters:
    void

  Returns:
    void
*/
void ${CCP_INSTANCE_NAME}_CompareStop (void);

void ${CCP_INSTANCE_NAME}_CompareAutoShutdownClear (void);

void ${CCP_INSTANCE_NAME}_CompareAutoShutdownSet (void);


<#if mode lt 4>
<#if CCP_CCPCON1_T32 == true>
void ${CCP_INSTANCE_NAME}_Compare32bitValueSet (uint32_t value);

uint32_t ${CCP_INSTANCE_NAME}_Compare32bitValueGet (void);

void ${CCP_INSTANCE_NAME}_Compare32bitPeriodValueSet (uint32_t value);

uint32_t ${CCP_INSTANCE_NAME}_Compare32bitPeriodValueGet (void);

<#else>
void ${CCP_INSTANCE_NAME}_Compare16bitValueSet (uint16_t value);

uint16_t ${CCP_INSTANCE_NAME}_Compare16bitValueGet (void);

void ${CCP_INSTANCE_NAME}_Compare16bitPeriodValueSet (uint16_t value);

uint16_t ${CCP_INSTANCE_NAME}_Compare16bitPeriodValueGet (void);
</#if>
</#if>

<#if mode gt 3 >
void ${CCP_INSTANCE_NAME}_Compare16bitPeriodValueSet (uint16_t value);

uint16_t ${CCP_INSTANCE_NAME}_Compare16bitPeriodValueGet (void);

void ${CCP_INSTANCE_NAME}_Compare16bitRAValueSet (uint16_t value);

uint16_t ${CCP_INSTANCE_NAME}_Compare16bitRAValueGet (void);

void ${CCP_INSTANCE_NAME}_Compare16bitRBValueSet (uint16_t value);

uint16_t ${CCP_INSTANCE_NAME}_Compare16bitRBValueGet (void);
</#if>


<#if CCP_TIMER_INTERRUPT == true>
// *****************************************************************************
/* Function:
  void ${CCP_INSTANCE_NAME}_TimerCallbackRegister( CCP_TIMER_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a ocmp interrupt.

  Description:
    This function sets the callback function that will be called when the timer overflows.

  Precondition:
    None.

  Parameters:
    *callback   - a pointer to the function to be called when value is reached.
                  Use NULL to Un Register the timer callback

    context     - a pointer to user defined data to be used when the callback
                  function is called. NULL can be passed in if no data needed.

  Returns:
    void
*/
void ${CCP_INSTANCE_NAME}_TimerCallbackRegister(CCP_TIMER_CALLBACK callback, uintptr_t context);
</#if>

<#if CCP_COMP_INTERRUPT == true>
// *****************************************************************************
/* Function:
  void ${CCP_INSTANCE_NAME}_CompareCallbackRegister( CCP_COMPARE_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a ocmp interrupt.

  Description:
    This function sets the callback function that will be called when the compare match occurs.

  Precondition:
    None.

  Parameters:
    *callback   - a pointer to the function to be called when value is reached.
                  Use NULL to Un Register the compare callback

    context     - a pointer to user defined data to be used when the callback
                  function is called. NULL can be passed in if no data needed.

  Returns:
    void
*/
void ${CCP_INSTANCE_NAME}_CompareCallbackRegister(CCP_COMPARE_CALLBACK callback, uintptr_t context);
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // _PLIB_${CCP_INSTANCE_NAME}_H
