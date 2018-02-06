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
		<#if .vars[SMC_CHIP_SELECT]?has_content>
			<#if (.vars[SMC_CHIP_SELECT] != false)>

	/* Chip Select CS${i} Timings */
	/* Setup SMC SETUP register */
	config = 0x01010101; /* Setup register reset value */
	config = SMC_SETUP_NWE_SETUP(SMC_NWE_SETUP_CS${i}) | SMC_SETUP_NCS_WR_SETUP(SMC_NCS_WR_SETUP_CS${i}) | SMC_SETUP_NRD_SETUP(SMC_NRD_SETUP_CS${i}) | SMC_SETUP_NCS_RD_SETUP(SMC_NCS_RD_SETUP_CS${i});
	_SMC_REGS->SMC_CS_NUMBER[${i}].SMC_SETUP.w = (uint32_t)(config << 0);
		
	/* Setup SMC CYCLE register */
    config = 0x00030003; /* Cycle register reset value */
    config = SMC_CYCLE_NWE_CYCLE(SMC_NWE_CYCLE_CS${i}) | SMC_CYCLE_NRD_CYCLE(SMC_NRD_CYCLE_CS${i});
    _SMC_REGS->SMC_CS_NUMBER[${i}].SMC_CYCLE.w = (uint32_t)config;
	
	/* Setup SMC_PULSE register */
    config = 0x01010101; /* Pulse register reset value */
    config = SMC_PULSE_NWE_PULSE(SMC_NWE_PULSE_CS${i}) | SMC_PULSE_NCS_WR_PULSE(SMC_NCS_WR_PULSE_CS${i}) | SMC_PULSE_NRD_PULSE(SMC_NRD_PULSE_CS${i}) | SMC_PULSE_NCS_RD_PULSE(SMC_NCS_RD_PULSE_CS${i});
    _SMC_REGS->SMC_CS_NUMBER[${i}].SMC_PULSE.w = (uint32_t)config;

	/* Setup SMC MODE register */
    config = 0x10001003; /* Mode register reset value */
    config = (( SMC_MODE_READ_MODE_Msk & ((SMC_READ_MODE_CS${i}) <<  SMC_MODE_READ_MODE_Pos)) | (SMC_MODE_WRITE_MODE_Msk & ((SMC_WRITE_MODE_CS${i}) <<  SMC_MODE_WRITE_MODE_Pos)) | SMC_NWAIT_MODE_CS${i} | (SMC_MODE_TDF_MODE_Msk & ((SMC_TDF_MODE_CS${i}) << SMC_MODE_TDF_MODE_Pos)) | SMC_MODE_TDF_CYCLES(SMC_TDF_CYCLES_CS${i}));

	/* Byte Access Type  setup , used only in 16-bit data bus */
    if (SMC_DATA_BUS_CS${i} == SMC_DATA_BUS_WIDTH_16_BIT && SMC_BAT_CS${i} == BAT_TYPE_WRITE)
    {
        config |= SMC_DATA_BUS_CS${i} | BAT_BYTE_WRITE;
    }
    if (SMC_DATA_BUS_CS${i} == SMC_DATA_BUS_WIDTH_16_BIT && SMC_BAT_CS${i} == BAT_TYPE_SELECT)
    {
        config |= SMC_DATA_BUS_CS${i} | BAT_BYTE_SELECT;
    }
    if (SMC_DATA_BUS_CS${i} ==  SMC_DATA_BUS_WIDTH_8_BIT)
    {
        config |= SMC_DATA_BUS_CS${i};
    }

    if (SMC_PMEN_CS${i} == ASYNC_READ_PAGE_MODE)
    {
        config |= ASYNC_READ_PAGE_MODE | SMC_PS_CS${i};
    }
    else
    {
        config |= STD_READ_PAGE_MODE;
    }
	
    _SMC_REGS->SMC_CS_NUMBER[${i}].SMC_MODE.w = (uint32_t)config;
    
	config = 0x0;
	/* Enable Off-chip Memory Scrambling */
    if (SMC_MEM_SCRAMBLING_CS${i} == MEM_SCRAMBLING_ON)
    {
		_SMC_REGS->SMC_OCMS.w |= SMC_OCMS_CS${i}SE_Msk;
    }
    else // SMC_MEM_SCRAMBLING_CS0 == MEM_SCRAMBLING_OFF
    {
		_SMC_REGS->SMC_OCMS.w &= ~(SMC_OCMS_CS${i}SE_Msk);
    }
	/* End of Chip Select CS${i} Settings */
			</#if>
		</#if>
    </#list>
} /* SMC${INDEX?string}_Initialize */

/*******************************************************************************
 End of File
*/
