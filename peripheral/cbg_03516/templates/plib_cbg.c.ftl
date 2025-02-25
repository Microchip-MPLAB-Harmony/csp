/*******************************************************************************
  CBG Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CBG_INSTANCE?lower_case}.c

  Summary:
    CBG Source File

  Description:
    None

*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2025 Microchip Technology Inc. and its subsidiaries.
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

// Section: Included Files

#include "plib_${CBG_INSTANCE?lower_case}.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

void ${CBG_INSTANCE}_Initialize (void)
{
<#list 0..(CURRENT_QUANTITY - 1) as i>
    <#if (.vars["USE_ISCR" + i] == true)>
        <#if (.vars["SOURCE_TYPE" + i] == "ISRC" + i)>
    IBIASCONbits.I10EN${i} = 1;
        <#elseif (.vars["SOURCE_TYPE" + i] == "IBIAS" + i)>
    IBIASCONbits.ISELOUT${i} = ${.vars["IBIAS_VALUE" + i]};
        </#if>
    </#if>
</#list>
}

void ${CBG_INSTANCE}_Deinitialize (void)
{
  IBIASCON = ${IBIAS_CON_REG_POR};
}

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif
// DOM-IGNORE-END