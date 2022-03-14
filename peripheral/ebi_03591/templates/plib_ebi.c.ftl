/*******************************************************************
  Company:
    Microchip Technology Inc.
    Memory System Service EBI Initialization File

  File Name:
    plib_${EBI_INSTANCE_NAME?lower_case}.c

  Summary:
    External Bus Interface (EBI).
    This file contains the source code to initialize the EBI.

  Description:
    EBI-SMC configuration interface
    The EBI-SMC System Memory interface provides a simple interface to manage 8-bit and 16-bit
    parallel devices.

  *******************************************************************/

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
#include "plib_${EBI_INSTANCE_NAME?lower_case}.h"
#include "device.h"

/* Function:
    void ${EBI_INSTANCE_NAME}_Initialize( void )

  Summary:
    Initializes hardware and data for the given instance of the EBI module.

  Description:
    This function initializes the SMC timings according to the external parralel device requirements.

  Returns:
  None.
 */

void ${EBI_INSTANCE_NAME}_Initialize( void )
{
<#list 0..(EBI_SMC_CHIP_SELECT_COUNT - 1) as i>
    <#assign EBI_SMC_CHIP_SELECT = "EBI_SMC_CHIP_SELECT" + i>
    <#assign EBI_SMC_DATA_BUS_CS = "EBI_SMC_DATA_BUS_CS" + i>
    <#assign EBI_SMC_NWE_SETUP_CS = "EBI_SMC_NWE_SETUP_CS" + i>
    <#assign EBI_SMC_NCS_WR_SETUP_CS = "EBI_SMC_NCS_WR_SETUP_CS" + i>
    <#assign EBI_SMC_NRD_SETUP_CS = "EBI_SMC_NRD_SETUP_CS" + i>
    <#assign EBI_SMC_NCS_RD_SETUP_CS = "EBI_SMC_NCS_RD_SETUP_CS" + i>
    <#assign EBI_SMC_NWE_PULSE_CS = "EBI_SMC_NWE_PULSE_CS" + i>
    <#assign EBI_SMC_NCS_WR_PULSE_CS = "EBI_SMC_NCS_WR_PULSE_CS" + i>
    <#assign EBI_SMC_NRD_PULSE_CS = "EBI_SMC_NRD_PULSE_CS" + i>
    <#assign EBI_SMC_NCS_RD_PULSE_CS = "EBI_SMC_NCS_RD_PULSE_CS" +i>
    <#assign EBI_SMC_NWE_CYCLE_CS = "EBI_SMC_NWE_CYCLE_CS" + i>
    <#assign EBI_SMC_NRD_CYCLE_CS = "EBI_SMC_NRD_CYCLE_CS" + i>
    <#assign EBI_SMC_PS_CS = "EBI_SMC_PS_CS" +i>
    <#assign EBI_SMC_TDF_MODE_CS = "EBI_SMC_TDF_OPTIMIZATION_CS" + i>
    <#assign EBI_SMC_TDF_CYCLES_CS = "EBI_SMC_TDF_CYCLES_CS" +i>
    <#assign EBI_SMC_NWAIT_MODE_CS = "EBI_SMC_NWAIT_MODE_CS" +i>
    <#assign EBI_SMC_PMEN_CS = "EBI_SMC_PMEN_CS" + i>
    <#assign EBI_SMC_WRITE_MODE_CS = "EBI_SMC_WRITE_ENABLE_MODE_CS" + i>
    <#assign EBI_SMC_READ_MODE_CS = "EBI_SMC_READ_ENABLE_MODE_CS" + i>
    <#assign EBI_SMC_BAT_CS = "EBI_SMC_BAT_CS" + i>
    <#if .vars[EBI_SMC_CHIP_SELECT]?has_content>

    <#if (.vars[EBI_SMC_CHIP_SELECT] != false)>

    /* Chip Select CS${i} Timings */
    /* Setup EBI SMC SETUP register */
    ${EBI_INSTANCE_NAME}_REGS->CS_X[${i}].EBI_SMC_SETUP = EBI_SMC_SETUP_NWE_SETUP(${.vars[EBI_SMC_NWE_SETUP_CS]}) | EBI_SMC_SETUP_NCS_WR_SETUP(${.vars[EBI_SMC_NCS_WR_SETUP_CS]}) | EBI_SMC_SETUP_NRD_SETUP(${.vars[EBI_SMC_NRD_SETUP_CS]}) | EBI_SMC_SETUP_NCS_RD_SETUP(${.vars[EBI_SMC_NCS_RD_SETUP_CS]});

    /* Setup EBI SMC CYCLE register */
    ${EBI_INSTANCE_NAME}_REGS->CS_X[${i}].EBI_SMC_CYCLE = EBI_SMC_CYCLE_NWE_CYCLE(${.vars[EBI_SMC_NWE_CYCLE_CS]}) | EBI_SMC_CYCLE_NRD_CYCLE(${.vars[EBI_SMC_NRD_CYCLE_CS]});

    /* Setup EBI SMC_PULSE register */
    ${EBI_INSTANCE_NAME}_REGS->CS_X[${i}].EBI_SMC_PULSE = EBI_SMC_PULSE_NWE_PULSE(${.vars[EBI_SMC_NWE_PULSE_CS]}) | EBI_SMC_PULSE_NCS_WR_PULSE(${.vars[EBI_SMC_NCS_WR_PULSE_CS]}) | EBI_SMC_PULSE_NRD_PULSE(${.vars[EBI_SMC_NRD_PULSE_CS]}) | EBI_SMC_PULSE_NCS_RD_PULSE(${.vars[EBI_SMC_NCS_RD_PULSE_CS]});

    /* Setup EBI SMC MODE register */
    ${EBI_INSTANCE_NAME}_REGS->CS_X[${i}].EBI_SMC_MODE = ${.vars[EBI_SMC_NWAIT_MODE_CS]} <#if (.vars[EBI_SMC_PMEN_CS] == true)>| EBI_SMC_MODE_PMEN_Msk | ${.vars[EBI_SMC_PS_CS]}</#if> <#if (.vars[EBI_SMC_TDF_MODE_CS] == true)>| EBI_SMC_MODE_TDF_MODE_Msk | EBI_SMC_MODE_TDF_CYCLES(${.vars[EBI_SMC_TDF_CYCLES_CS]})</#if>  \
                                          <#if (.vars[EBI_SMC_WRITE_MODE_CS] == true)>| EBI_SMC_MODE_WRITE_MODE_Msk</#if> <#if (.vars[EBI_SMC_READ_MODE_CS] == true)>| EBI_SMC_MODE_READ_MODE_Msk</#if>  | ${.vars[EBI_SMC_DATA_BUS_CS]} | ${.vars[EBI_SMC_BAT_CS]};
    </#if>
    </#if>
</#list>

<#if EBI_SMC_WRITE_PROTECTION>
    /* Enable Write Protection */
    ${EBI_INSTANCE_NAME}_REGS->EBI_SMC_WPMR = (EBI_SMC_WPMR_WPKEY_PASSWD | EBI_SMC_WPMR_WPEN_Msk);
</#if>
} /* ${EBI_INSTANCE_NAME}_Initialize */

/*******************************************************************************
 End of File
*/
