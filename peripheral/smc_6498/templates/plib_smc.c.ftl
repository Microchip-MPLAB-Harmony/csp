/*******************************************************************
  Company:
    Microchip Technology Inc.
    Memory System Service SMC Initialization File

  File Name:
    plib_${SMC_INSTANCE_NAME?lower_case}.c

  Summary:
    Static Memory Controller (SMC).
    This file contains the source code to initialize the SMC controller

  Description:
    SMC configuration interface
    The SMC System Memory interface provides a simple interface to manage 8-bit and 16-bit
    parallel devices.

  *******************************************************************/

/*******************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_${SMC_INSTANCE_NAME?lower_case}.h"
#include "device.h"

<#compress>
<#assign SMC_OCMS = "">
<#list 0..(SMC_CHIP_SELECT_COUNT - 1) as i>

<#assign ENABLE = "SMC_MEM_SCRAMBLING_CS" + i>

<#if .vars[ENABLE] == true>
    <#if SMC_OCMS != "">
        <#assign SMC_OCMS = SMC_OCMS + " | " + "SMC_OCMS_CS" + i +"SE_Msk">
    <#else>
        <#assign SMC_OCMS = "SMC_OCMS_CS" + i +"SE_Msk">
    </#if>
</#if>

</#list>
</#compress>

/* Function:
    void ${SMC_INSTANCE_NAME}_Initialize( void )

  Summary:
    Initializes hardware and data for the given instance of the SMC module.

  Description:
    This function initializes the SMC timings according to the external parralel device requirements.

  Returns:
  None.
 */

void ${SMC_INSTANCE_NAME}_Initialize( void )
{
<#list 0..(SMC_CHIP_SELECT_COUNT - 1) as i>
    <#assign SMC_CHIP_SELECT = "SMC_CHIP_SELECT" + i>
    <#assign SMC_DATA_BUS_CS = "SMC_DATA_BUS_CS" + i>
    <#assign SMC_NWE_SETUP_CS = "SMC_NWE_SETUP_CS" + i>
    <#assign SMC_NCS_WR_SETUP_CS = "SMC_NCS_WR_SETUP_CS" + i>
    <#assign SMC_NRD_SETUP_CS = "SMC_NRD_SETUP_CS" + i>
    <#assign SMC_NCS_RD_SETUP_CS = "SMC_NCS_RD_SETUP_CS" + i>
    <#assign SMC_NWE_PULSE_CS = "SMC_NWE_PULSE_CS" + i>
    <#assign SMC_NCS_WR_PULSE_CS = "SMC_NCS_WR_PULSE_CS" + i>
    <#assign SMC_NRD_PULSE_CS = "SMC_NRD_PULSE_CS" + i>
    <#assign SMC_NCS_RD_PULSE_CS = "SMC_NCS_RD_PULSE_CS" +i>
    <#assign SMC_NWE_CYCLE_CS = "SMC_NWE_CYCLE_CS" + i>
    <#assign SMC_NRD_CYCLE_CS = "SMC_NRD_CYCLE_CS" + i>
    <#assign SMC_PS_CS = "SMC_PS_CS" +i>
    <#assign SMC_TDF_MODE_CS = "SMC_TDF_OPTIMIZATION_CS" + i>
    <#assign SMC_TDF_CYCLES_CS = "SMC_TDF_CYCLES_CS" +i>
    <#assign SMC_NWAIT_MODE_CS = "SMC_NWAIT_MODE_CS" +i>
    <#assign SMC_PMEN_CS = "SMC_PMEN_CS" + i>
    <#assign SMC_OCMS_CSSE_MASK = "SMC_OCMS_CS" + i>
    <#assign SMC_WRITE_MODE_CS = "SMC_WRITE_ENABLE_MODE_CS" + i>
    <#assign SMC_READ_MODE_CS = "SMC_READ_ENABLE_MODE_CS" + i>
    <#assign SMC_BAT_CS = "SMC_BAT_CS" + i>
    <#if .vars[SMC_CHIP_SELECT]?has_content>

    <#if (.vars[SMC_CHIP_SELECT] != false)>

    /* Chip Select CS${i} Timings */
    /* Setup SMC SETUP register */
    ${SMC_INSTANCE_NAME}_REGS->SMC_CS_NUMBER[${i}].SMC_SETUP= SMC_SETUP_NWE_SETUP(${.vars[SMC_NWE_SETUP_CS]}) | SMC_SETUP_NCS_WR_SETUP(${.vars[SMC_NCS_WR_SETUP_CS]}) | SMC_SETUP_NRD_SETUP(${.vars[SMC_NRD_SETUP_CS]}) | SMC_SETUP_NCS_RD_SETUP(${.vars[SMC_NCS_RD_SETUP_CS]});

    /* Setup SMC CYCLE register */
    ${SMC_INSTANCE_NAME}_REGS->SMC_CS_NUMBER[${i}].SMC_CYCLE= SMC_CYCLE_NWE_CYCLE(${.vars[SMC_NWE_CYCLE_CS]}) | SMC_CYCLE_NRD_CYCLE(${.vars[SMC_NRD_CYCLE_CS]});

    /* Setup SMC_PULSE register */
    ${SMC_INSTANCE_NAME}_REGS->SMC_CS_NUMBER[${i}].SMC_PULSE= SMC_PULSE_NWE_PULSE(${.vars[SMC_NWE_PULSE_CS]}) | SMC_PULSE_NCS_WR_PULSE(${.vars[SMC_NCS_WR_PULSE_CS]}) | SMC_PULSE_NRD_PULSE(${.vars[SMC_NRD_PULSE_CS]}) | SMC_PULSE_NCS_RD_PULSE(${.vars[SMC_NCS_RD_PULSE_CS]});

    /* Setup SMC MODE register */
    ${SMC_INSTANCE_NAME}_REGS->SMC_CS_NUMBER[${i}].SMC_MODE= ${.vars[SMC_NWAIT_MODE_CS]} <#if (.vars[SMC_PMEN_CS] == true)>| SMC_MODE_PMEN_Msk | ${.vars[SMC_PS_CS]}</#if> <#if (.vars[SMC_TDF_MODE_CS] == true)>| SMC_MODE_TDF_MODE_Msk | SMC_MODE_TDF_CYCLES(${.vars[SMC_TDF_CYCLES_CS]})</#if>  \
                                          <#if (.vars[SMC_WRITE_MODE_CS] == true)>| SMC_MODE_WRITE_MODE_Msk</#if> <#if (.vars[SMC_READ_MODE_CS] == true)>| SMC_MODE_READ_MODE_Msk</#if>  | ${.vars[SMC_DATA_BUS_CS]} | ${.vars[SMC_BAT_CS]};
    </#if>
    </#if>
</#list>

    <#if SMC_OCMS != "">
    /* Configure scrambling key and enable scrambling */
    ${SMC_INSTANCE_NAME}_REGS->SMC_KEY1 = 0x${SMC_KEY1};
    ${SMC_INSTANCE_NAME}_REGS->SMC_KEY2 = 0x${SMC_KEY2};
    ${SMC_INSTANCE_NAME}_REGS->SMC_OCMS = ${SMC_OCMS} | SMC_OCMS_SMSE_Msk;
    </#if>

<#if SMC_WRITE_PROTECTION>
    /* Enable Write Protection */
    ${SMC_INSTANCE_NAME}_REGS->SMC_WPMR = (SMC_WPMR_WPKEY_PASSWD | SMC_WPMR_WPEN_Msk);
</#if>
} /* ${SMC_INSTANCE_NAME}_Initialize */

/*******************************************************************************
 End of File
*/
