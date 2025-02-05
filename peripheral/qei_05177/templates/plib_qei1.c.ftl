<#function pow base exponent>
    <#assign result = 1>
    <#list 1..exponent as i>
        <#assign result = result * base>
    </#list>
    <#return result>
</#function>

<#assign PrescalarOptions = ["1"]>
<#list 1..7 as i>
    <#assign PrescalarOptions = PrescalarOptions + [pow(2, i)]>
</#list>

<#assign PCInitMode = ["FREE_RUNNING", "RESET", "INIT_ON_NEXT_INDEX", "INIT_ON_FIRST_INDEX", "INIT_ON_SECOND_INDEX", "RESET_ON_EQUAL", "MODULO", "MODULO_AND_RESET"]>
/*******************************************************************************
  ${moduleName?lower_case} PLIB
 
  Company:
    Microchip Technology Inc.
 
  File Name:
    plib_${moduleName?lower_case}.c
 
  Summary:
    ${moduleName?lower_case} PLIB Source File
 
  Description:
    None
 
*******************************************************************************/
 
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

// Section: Included Files
#include "plib_${moduleName?lower_case}.h"
#include <stdbool.h>
#include "device.h"


//Section: Macro Definitions

//Timer Input Clock Division
<#list PrescalarOptions as options>
#define QEI1CON_INTDIV_1_${options}      ((uint32_t)(_QEI1CON_INTDIV_MASK & ((uint32_t)(${options_index}) <<_QEI1CON_INTDIV_POSITION))) 
</#list>

//Digital Input Filter Clock Division
<#list PrescalarOptions as options>
#define QEI1IOC_QFDIV_1_${options}		 ((uint32_t)(_QEI1IOC_QFDIV_MASK & ((uint32_t)(${options_index}) <<_QEI1IOC_QFDIV_POSITION)))
</#list>

//QEI Modes
<#list PCInitMode as options>
<#if options == "FREE_RUNNING" || options == "RESET" || options == "MODULO">
#define QEI1CON_PIMOD_${options}      ((uint32_t)(_QEI1CON_PIMOD_MASK & ((uint32_t)(${options_index}) <<_QEI1CON_PIMOD_POSITION))) 
</#if>
</#list>

// Section: ${moduleName} PLIB Routines

void ${moduleName}_Initialize(void)
{
	${moduleName}CON = (QEI1CON_INTDIV_1_${PrescalarOptions[QEI_CON__INTDIV?number]}
			  |QEI1CON_PIMOD_${PCInitMode[QEI_CON__PIMOD?number]});
								 
    ${moduleName}IOC = (QEI1IOC_QFDIV_1_${PrescalarOptions[QEI_IOC__QFDIV?number]}<#if QEI_IOC__FLTREN == true>
              |_QEI1IOC_FLTREN_MASK</#if><#if QEI_IOC__IDXPOL == true>
              |_QEI1IOC_IDXPOL_MASK</#if><#if QEI_IOC__HOMPOL == true>
              |_QEI1IOC_HOMPOL_MASK</#if><#if QEI_IOC__QCAPEN == true>
              |_QEI1IOC_QCAPEN_MASK</#if><#if QEI_IOC__HCAPEN == true>
              |_QEI1IOC_HCAPEN_MASK</#if>);
			                     
    ${moduleName}STAT = 0x0UL;
    /* POSCNT 0x0; */
    POS1CNT = 0x0UL;
    /* POSHLD 0x0; */
    POS1HLD = 0x0UL;
    /* VELCNT 0x0; */
    VEL1CNT = 0x0UL;
    /* VELHLD 0x0; */
    VEL1HLD = 0x0UL;
    /* INTTMR 0x0; */
    INT1TMR = 0x0UL;
    /* INTHLD 0x0; */
    INT1HLD = 0x0UL;
    /* INDXCNT 0x0; */
    INDX1CNT = 0x0UL;
    /* INDXHLD 0x0; */
    INDX1HLD = 0x0UL;
    /* ${moduleName}GEC 0; */
    ${moduleName}GEC = 0x${QEIxGEC}UL;
    /* ${moduleName}LEC 0x0; */
    ${moduleName}LEC = 0x${QEIxLEC}UL;
}

void QEI1_Deinitialize(void)
{
    // Disable QEI
    QEI1_Disable();

	// De-initializing registers to POR values
${regPorSet}
}




