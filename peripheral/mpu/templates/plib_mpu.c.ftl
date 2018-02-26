/*******************************************************************************
  MPU PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_mpu.h

  Summary:
    MPU PLIB Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "plib_mpu.h"
#include "plib_mpu_local.h"


// *****************************************************************************
// *****************************************************************************
// Section: MPU Implementation
// *****************************************************************************
// *****************************************************************************

void MPU_Initialize(void)
{
	/*** Disable MPU			***/
	MPU->CTRL = 0;
	
	/*** Configure MPU Regions	***/
<#list 0..15 as i>
    <#assign MPU_ENABLE = "MPU_Region_" + i + "_Enable">    
    <#assign MPU_ADDRESS = "MPU_Region_" + i + "_Address">
    <#assign MPU_SIZE = "MPU_Region_" + i + "_Size">
    <#assign MPU_TYPE = "MPU_Region_" + i + "_Type">
    <#assign MPU_ACCESS = "MPU_Region_" + i + "_Access">
    <#assign MPU_EXECUTE = "MPU_Region_" + i + "_Execute">
    <#assign MPU_SHARE = "MPU_Region_" + i + "_Share">
	<#assign MPU_NAME = "MPU_Region_Name"+i>
	<#assign MPU_LENGTH = "MPU_Region_" + i + "_Length">
    
    <#if .vars[MPU_ENABLE]?has_content>
    <#if (.vars[MPU_ENABLE] != false)>          
	/* Region ${i} Name: ${.vars[MPU_NAME]}, Base Address: 0x${.vars[MPU_ADDRESS]}, Size: ${.vars[MPU_LENGTH]}  */
	MPU->RBAR = MPU_REGION(${i}, 0x${.vars[MPU_ADDRESS]});
	MPU->RASR = MPU_REGION_SIZE(${.vars[MPU_SIZE]}) | MPU_RASR_AP(${.vars[MPU_ACCESS]}) | ${.vars[MPU_TYPE]} \
	            | MPU_ATTR_ENABLE ${.vars[MPU_EXECUTE]?then('', '| MPU_ATTR_EXECUTE_NEVER')} ${.vars[MPU_SHARE]?then('| MPU_ATTR_SHAREABLE', '')};      
    </#if>  
	</#if>   
</#list>
	
	/*** Enable MPU			***/
	SCB->SHCSR |= (SCB_SHCSR_MEMFAULTENA_Msk | SCB_SHCSR_BUSFAULTENA_Msk |  SCB_SHCSR_USGFAULTENA_Msk);
	MPU->CTRL = MPU_CTRL_ENABLE_Msk ${CoreMPU_HFNMIENA?then('| MPU_CTRL_HFNMIENA_Msk', '')} ${CoreMPU_PRIVDEFENA?then('| MPU_CTRL_PRIVDEFENA_Msk', '')};

    __DSB();
    __ISB();
}

