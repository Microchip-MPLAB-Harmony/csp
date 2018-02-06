/*******************************************************************
  Company:
    Microchip Technology Inc.
    Memory System Service SMC Initialization File

  File Name:
    plib_smc${INDEX?string}.h

  Summary:
    Static Memory Controller (SMC) peripheral library interface.
	This file contains the source code to initialize the SMC controller

  Description
    This file defines the interface to the SMC peripheral library.  This 
    library provides access to and control of the associated peripheral 
    instance.

  Remarks:
    This header is for documentation only.  The actual smc<x> headers will be
    generated as required by the MCC (where <x> is the peripheral instance 
    number).

    Every interface symbol has a lower-case 'x' in it following the "SMC" 
    abbreviation.  This 'x' will be replaced by the peripheral instance number
    in the generated headers.  These are the actual functions that should be
    used.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2017-18 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.
SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
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
// DOM-IGNORE-END

#ifndef _PLIB_SMC${INDEX?string}_H
#define _PLIB_SMC${INDEX?string}_H


// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************

#include "${__PROCESSOR?lower_case}.h"
#include <stdint.h>
#include <sys/attribs.h>

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
typedef enum {
    SMC_DATA_BUS_WIDTH_8_BIT	= SMC_MODE_DBW_8_BIT, /* 8-bit data bus width*/
    SMC_DATA_BUS_WIDTH_16_BIT  	= SMC_MODE_DBW_16_BIT /* 16-bit data bus width*/
} SMC_DATA_BUS_WIDTH; /* Data bus size */

typedef enum {
  BAT_TYPE_SELECT 	= 0x0, 	/* Byte Select Access Type */
  BAT_TYPE_WRITE 	= 0x1 	/* Byte Write Access Type */
}SMC_BAT_TYPE; /* SMC Byte Access Type Register */

typedef enum {
	BAT_BYTE_SELECT	= SMC_MODE_BAT_BYTE_SELECT, /* Write operation is controlled using NCS,NWE,NBS0-1 Read operation is controlled using NCS,NRD,NBS0-1 */
	BAT_BYTE_WRITE 	= SMC_MODE_BAT_BYTE_WRITE 	/* Write operation is controlled using NCS,NWR0-1 Read operation is controlled using NCS,NRD */
}SMC_BAT; /* Byte Access Type */

typedef enum {
  WRITE_PROTECT_OFF = 0x0, 	/* Write Protection is OFF */
  WRITE_PROTECT_ON 	= 0x1 	/* Write Protection is ON, ALL the chips Select timings registers are in read-only access */
}SMC_WRITE_PROTECT; /* SMC Timings register write protection feature */

typedef enum {
  NWAIT_DISABLED_MODE 	= SMC_MODE_EXNW_MODE_DISABLED, 	/* NWAIT input signal is ignored on the corresponding chip select */
  NWAIT_FROZEN_MODE 	= SMC_MODE_EXNW_MODE_FROZEN, 	/* NWAIT signal freezes the current read or write cycle */
  NWAIT_READY_MODE 		= SMC_MODE_EXNW_MODE_READY 		/* NWAIT signal indicated the availability of the external device at the end of the pulse read or wirte signal */
}SMC_NWAIT_MODE; /* NWAIT signal is used to extend the current read or write signal */

typedef enum {
  MEM_SCRAMBLING_OFF 	= 0x0, 	/* SMC Memory scrambling is disabled */
  MEM_SCRAMBLING_ON		= 0x1 	/* SMC Memory scrambling is enabled */
}SMC_MEM_SCRAMBLING; /* The External data bus can be scrambled to prevent recovery of data*/

typedef enum {
  WRITE_MODE_OFF = (0x0u << SMC_MODE_WRITE_MODE_Pos), 	/* Write mode operation is controlled by NCS signal*/
  WRITE_MODE_ON  = SMC_MODE_WRITE_MODE_Msk 				/* Write mode opeeration is controlled by NWE signal */
}SMC_WRITE_MODE;

typedef enum {
  STD_READ_PAGE_MODE 	= (0x0u << SMC_MODE_PMEN_Pos), 	/* Standard Read*/
  ASYNC_READ_PAGE_MODE 	= SMC_MODE_PMEN_Msk 			/* Asynchronous burst resd in page mode is applied on the corresponding chip select*/
}SMC_PAGE_MODE;

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

//********************** SMC Global Features ***********************************

#define TDF_MODE_ON 			0x1
#define TDF_MODE_OFF	 		0x0
#define WRITE_MODE_ON 			0x1
#define WRITE_MODE_OFF	 		0x0
#define READ_MODE_ON 			0x1
#define READ_MODE_OFF	 		0x0
<#if SMC_WRITE_PROTECTION == true>
#define SMC_WRITE_PROTECTION 	WRITE_PROTECT_ON
<#else> 
#define SMC_WRITE_PROTECTION 	WRITE_PROTECT_OFF
</#if>
<#if SMC_MEM_SCRAMBLING == true>
#define SMC_MEMORY_SCRAMBLING 	MEM_SCRAMBLING_ON
<#else>
#define SMC_MEMORY_SCRAMBLING 	MEM_SCRAMBLING_OFF
</#if>

<#list 0..(SMC_CHIP_SELECT_COUNT - 1) as i>
<#assign SMC_CHIP_SELECT = "SMC_CHIP_SELECT" + i>
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
<#assign SMC_DATA_BUS_CS = "SMC_DATA_BUS_CS" + i>
<#assign SMC_TDF_MODE_CS = "SMC_TDF_MODE_CS" + i>
<#assign SMC_TDF_CYCLES_CS = "SMC_TDF_CYCLES_CS" +i>
<#assign SMC_NWAIT_MODE_CS = "SMC_NWAIT_MODE_CS" +i>
<#assign SMC_PMEN_CS = "SMC_PMEN_CS" + i>
<#assign SMC_MEM_SCRAMBLING_CS = "SMC_MEM_SCRAMBLING_CS" + i>
<#assign SMC_OCMS_CSSE_MASK = "SMC_OCMS_CS" + i>
<#assign SMC_WRITE_MODE_CS = "SMC_WRITE_MODE_CS" + i>
<#assign SMC_READ_MODE_CS = "SMC_READ_MODE_CS" + i>
	<#if .vars[SMC_CHIP_SELECT]?has_content>
		<#if (.vars[SMC_CHIP_SELECT] != false)>

// *****************************************************************************
// ********** Chip Select ${i} Configuration (Enabled per default)*****************
// *****************************************************************************
<#if (.vars[SMC_MEM_SCRAMBLING_CS] == true)>
#define SMC_MEM_SCRAMBLING_CS${i} 	MEM_SCRAMBLING_ON
<#else> 
#define SMC_MEM_SCRAMBLING_CS${i} 	MEM_SCRAMBLING_OFF
</#if>

// Setup Register
#define SMC_NWE_SETUP_CS${i} 		${.vars[SMC_NWE_SETUP_CS]}
#define SMC_NCS_WR_SETUP_CS${i}	${.vars[SMC_NCS_WR_SETUP_CS]}
#define SMC_NRD_SETUP_CS${i} 		${.vars[SMC_NRD_SETUP_CS]}
#define SMC_NCS_RD_SETUP_CS${i} 	${.vars[SMC_NCS_RD_SETUP_CS]}

// Pulse Register
#define SMC_NWE_PULSE_CS${i} 		${.vars[SMC_NWE_PULSE_CS]}
#define SMC_NCS_WR_PULSE_CS${i} 	${.vars[SMC_NCS_WR_PULSE_CS]}
#define SMC_NRD_PULSE_CS${i} 		${.vars[SMC_NRD_PULSE_CS]}
#define SMC_NCS_RD_PULSE_CS${i} 	${.vars[SMC_NCS_RD_PULSE_CS]}

//Cycle Register
#define SMC_NWE_CYCLE_CS${i} 		${.vars[SMC_NWE_CYCLE_CS]}
#define SMC_NRD_CYCLE_CS${i} 		${.vars[SMC_NRD_CYCLE_CS]}

// Mode Register
<#if (.vars[SMC_PMEN_CS] == true)>
#define SMC_PMEN_CS${i} 			ASYNC_READ_PAGE_MODE
#define SMC_PS_CS${i} 				SMC_MODE_PS${.vars[SMC_PS_CS]}
<#else>
#define SMC_PMEN_CS${i} 			STD_READ_PAGE_MODE
#define SMC_PS_CS${i} 				SMC_MODE_PS_4_BYTE
</#if>

#define SMC_DATA_BUS_CS${i} 		SMC_DATA_BUS_WIDTH${.vars[SMC_DATA_BUS_CS]}
<#if (.vars[SMC_DATA_BUS_CS] == "SMC_DATA_BUS_WIDTH_16_BIT")>
#define SMC_BAT_CS${i} 			BAT_TYPE_WRITE
<#else>
#define SMC_BAT_CS${i} 			BAT_TYPE_SELECT
</#if>

<#if (.vars[SMC_TDF_MODE_CS] == true)>
#define SMC_TDF_MODE_CS${i} 		TDF_MODE_ON
#define SMC_TDF_CYCLES_CS${i} 		${.vars[SMC_TDF_CYCLES_CS]}
<#else>
#define SMC_TDF_MODE_CS${i} 		TDF_MODE_OFF
#define SMC_TDF_CYCLES_CS${i} 		TDF_MODE_OFF
</#if>

#define SMC_NWAIT_MODE_CS${i} 		SMC_MODE_EXNW_MODE_${.vars[SMC_NWAIT_MODE_CS]}

<#if (.vars[SMC_WRITE_MODE_CS] == true)>
#define SMC_WRITE_MODE_CS${i} 		WRITE_MODE_ON
<#else>
#define SMC_WRITE_MODE_CS${i} 		WRITE_MODE_OFF
</#if>

<#if (.vars[SMC_READ_MODE_CS] == true)>
#define SMC_READ_MODE_CS${i} 		READ_MODE_ON
<#else>
#define SMC_READ_MODE_CS${i} 		READ_MODE_OFF
</#if>

// ************************ End Chip Select ${i} Settings *************************
		</#if>
	</#if>
</#list>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
void SMC${INDEX?string}_Initialize( void );

#endif // _PLIB_SMC${INDEX?string}_H

/*******************************************************************************
 End of File
*/
