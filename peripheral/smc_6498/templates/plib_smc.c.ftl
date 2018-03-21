/*******************************************************************
  Company:
    Microchip Technology Inc.
    Memory System Service SMC Initialization File

  File Name:
    plib_smc${INDEX}.c

  Summary:
    Static Memory Controller (SMC).
    This file contains the source code to initialize the SMC controller

  Description:
    SMC configuration interface
    The SMC System Memory interface provides a simple interface to manage 8-bit and 16-bit
    parallel devices.

  *******************************************************************/

/*******************************************************************************
Copyright (c) 2017-18 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
#include "plib_smc${INDEX}.h"
#include "${__PROCESSOR?lower_case}.h"

/* Function:
	void SMC${INDEX}_Initialize( void )

  Summary:
	Initializes hardware and data for the given instance of the SMC module.

  Description:
	This function initializes the SMC timings according to the external parralel device requirements.

  Returns:
  None.
 */

void SMC${INDEX?string}_Initialize( void )
{
	volatile uint32_t config = 0x0;
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
	<#assign SMC_TDF_MODE_CS = "SMC_TDF_MODE_CS" + i>
	<#assign SMC_TDF_CYCLES_CS = "SMC_TDF_CYCLES_CS" +i>
	<#assign SMC_NWAIT_MODE_CS = "SMC_NWAIT_MODE_CS" +i>
	<#assign SMC_PMEN_CS = "SMC_PMEN_CS" + i>
	<#assign SMC_MEM_SCRAMBLING_CS = "SMC_MEM_SCRAMBLING_CS" + i>
	<#assign SMC_OCMS_CSSE_MASK = "SMC_OCMS_CS" + i>
	<#assign SMC_WRITE_MODE_CS = "SMC_WRITE_MODE_CS" + i>
	<#assign SMC_READ_MODE_CS = "SMC_READ_MODE_CS" + i>
	<#assign SMC_BAT_CS = "SMC_BAT_CS" + i>
	<#if .vars[SMC_CHIP_SELECT]?has_content>
		<#if (.vars[SMC_CHIP_SELECT] != false)>

	/* Chip Select CS${i} Timings */
	/* Setup SMC SETUP register */
	_SMC_REGS->SMC_CS_NUMBER[${i}].SMC_SETUP.w = SMC_SETUP_NWE_SETUP(${.vars[SMC_NWE_SETUP_CS]}) | SMC_SETUP_NCS_WR_SETUP(${.vars[SMC_NCS_WR_SETUP_CS]}) | SMC_SETUP_NRD_SETUP(${.vars[SMC_NRD_SETUP_CS]}) | SMC_SETUP_NCS_RD_SETUP(${.vars[SMC_NCS_RD_SETUP_CS]});

	/* Setup SMC CYCLE register */
	_SMC_REGS->SMC_CS_NUMBER[${i}].SMC_CYCLE.w = SMC_CYCLE_NWE_CYCLE(${.vars[SMC_NWE_CYCLE_CS]}) | SMC_CYCLE_NRD_CYCLE(${.vars[SMC_NRD_CYCLE_CS]});

	/* Setup SMC_PULSE register */
	_SMC_REGS->SMC_CS_NUMBER[${i}].SMC_PULSE.w = SMC_PULSE_NWE_PULSE(${.vars[SMC_NWE_PULSE_CS]}) | SMC_PULSE_NCS_WR_PULSE(${.vars[SMC_NCS_WR_PULSE_CS]}) | SMC_PULSE_NRD_PULSE(${.vars[SMC_NRD_PULSE_CS]}) | SMC_PULSE_NCS_RD_PULSE(${.vars[SMC_NCS_RD_PULSE_CS]});

	/* Setup SMC MODE register */
	config = (( SMC_MODE_READ_MODE_Msk & ((${.vars[SMC_READ_MODE_CS]}) <<  SMC_MODE_READ_MODE_Pos)) | (SMC_MODE_WRITE_MODE_Msk & ((${.vars[SMC_WRITE_MODE_CS]}) <<  SMC_MODE_WRITE_MODE_Pos)) | ${.vars[SMC_NWAIT_MODE_CS]} | (SMC_MODE_TDF_MODE_Msk & ((${.vars[SMC_TDF_MODE_CS]}) << SMC_MODE_TDF_MODE_Pos)) | SMC_MODE_TDF_CYCLES(${.vars[SMC_TDF_CYCLES_CS]}));

	/* Byte Access Type Configurations */
			<#if (.vars[SMC_DATA_BUS_CS] == "SMC_MODE_DBW_16_BIT") && (.vars[SMC_BAT_CS] == "SMC_MODE_BAT_BYTE_WRITE")>
	/* Byte Access Type  setup is configured for 16-bit data bus width and byte write mode */
	config |= SMC_MODE_DBW_16_BIT | SMC_MODE_BAT_BYTE_WRITE;
			</#if>
			<#if (.vars[SMC_DATA_BUS_CS] == "SMC_MODE_DBW_16_BIT") && (.vars[SMC_BAT_CS] == "SMC_MODE_BAT_BYTE_SELECT")>
	/* Byte Access Type  setup is configured for 16-bit data bus width and byte select mode */
	config |= SMC_MODE_DBW_16_BIT | SMC_MODE_BAT_BYTE_SELECT;
			</#if>
			<#if (.vars[SMC_DATA_BUS_CS] == "SMC_MODE_DBW_8_BIT")>
	/* 8-bit Byte Access Type Selected */
	config |= SMC_MODE_DBW_8_BIT;
			</#if>

			<#if (.vars[SMC_PMEN_CS] == true)>
	/* Enabled External Memory Page mode */
	config |= SMC_MODE_PMEN_Msk | ${.vars[SMC_PS_CS]};
			</#if>

	_SMC_REGS->SMC_CS_NUMBER[${i}].SMC_MODE.w = (uint32_t)config;

			<#if (.vars[SMC_MEM_SCRAMBLING_CS] == true)>
	/* Enabled Off-chip Memory Scrambling */
	_SMC_REGS->SMC_OCMS.w |= SMC_OCMS_CS${i}SE_Msk;
			</#if>
		</#if>
	</#if>
	/* End of Chip Select CS${i} Settings */
</#list>

<#if SMC_WRITE_PROTECTION>
	/* Enable Write Protection */
	_SMC_REGS->SMC_WPMR.w = (SMC_WPMR_WPKEY_PASSWD | SMC_WPMR_WPEN_Msk);
</#if>
} /* SMC${INDEX?string}_Initialize */

/*******************************************************************************
 End of File
*/
