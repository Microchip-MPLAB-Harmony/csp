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

#include "plib_mpu.h"
#include "plib_mpu_local.h"


// *****************************************************************************
// *****************************************************************************
// Section: MPU Implementation
// *****************************************************************************
// *****************************************************************************

void MPU_Initialize(void)
{
    /*** Disable MPU            ***/
    MPU->CTRL = 0;

    /*** Configure MPU Regions  ***/
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

    /* Enable Memory Management Fault */
    SCB->SHCSR |= (SCB_SHCSR_MEMFAULTENA_Msk);

    /* Enable MPU */
    MPU->CTRL = MPU_CTRL_ENABLE_Msk ${CoreMPU_HFNMIENA?then('| MPU_CTRL_HFNMIENA_Msk', '')} ${CoreMPU_PRIVDEFENA?then('| MPU_CTRL_PRIVDEFENA_Msk', '')};

    __DSB();
    __ISB();
}

