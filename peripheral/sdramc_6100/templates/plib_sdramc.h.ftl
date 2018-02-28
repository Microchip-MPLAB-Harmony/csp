/*******************************************************************
  Company:
    Microchip Technology Inc.
    Memory System Service SDRAMC Initialization File

  File Name:
    plib_sdramc${INDEX}.h

  Summary:
    SDRAMC Controller (SDRAMC). 

  Description:
    The SDRAMC System Memory interface provides a simple interface to manage
    the externally connected SDRAM device. This file contains the source code
    to initialize the SDRAMC controller

 Remarks:
    This header is for documentation only.  The actual sdramc<x> headers will be
    generated as required by the MCC (where <x> is the peripheral instance 
    number).

    Every interface symbol has a lower-case 'x' in it following the "SDRAMC" 
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


#ifndef _PLIB_SDRAMC${INDEX?string}_H
#define _PLIB_SDRAMC${INDEX?string}_H

// *****************************************************************************
// *****************************************************************************
// Section: Include Files
// *****************************************************************************
// *****************************************************************************
#include "${__PROCESSOR?lower_case?lower_case}.h"
#include <stdint.h>
#include <sys/attribs.h>

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

//*******************************************************************************
/* Data Bus Width

  Summary:
    Enumerated data type listing supported data bus widths.

  Description:
    These enumerated values list the various data bus widths supported by the
    SDRAM Controller.

  Remarks:
    None.
*/
typedef enum {
    SDRAMC_DATA_BUS_WIDTH_16BIT = 1,
} SDRAMC_DATA_BUS_WIDTH;

//*******************************************************************************
/* Burst Type

  Summary:
    Enumerated data type listing supported burst types.

  Description:
    These enumerated values list the burst types supported by the SDRAM
    Controller.

  Remarks:
    None.
*/
typedef enum {
    SDRAMC_BURST_TYPE_SEQUENTIAL = 0,
    SDRAMC_BURST_TYPE_INTERLEAVED
} SDRAMC_BURST_TYPE;

//*******************************************************************************
/* Row configuration

  Summary:
    Enumerated data type listing the various Row sizes supported.

  Description:
    These enumerated values list the various Row sizes supported.

  Remarks:
    None.
*/
typedef enum {
    SDRAMC_NUM_ROWS_2048 = 0,
    SDRAMC_NUM_ROWS_4096,
    SDRAMC_NUM_ROWS_8192,
} SDRAMC_NUM_ROWS;

//*******************************************************************************
/* Column configuration

  Summary:
    Enumerated data type listing the various Column sizes supported.

  Description:
    These enumerated values list the various Column sizes supported.

  Remarks:
    None.
*/
typedef enum {
    SDRAMC_NUM_COLS_256 = 0,
    SDRAMC_NUM_COLS_512,
    SDRAMC_NUM_COLS_1024,
    SDRAMC_NUM_COLS_2048,
} SDRAMC_NUM_COLS;

//*******************************************************************************
/* Bank configuration

  Summary:
    Enumerated data type listing number of banks supported.

  Description:
    These enumerated values list the number of banks supported.

  Remarks:
    None.
*/
typedef enum {
    SDRAMC_NUM_BANKS_2 = 0,
    SDRAMC_NUM_BANKS_4
} SDRAMC_NUM_BANKS;

//*******************************************************************************
/* SDRAM Device Type

  Summary:
    Enumerated data type listing type of SDRAM devices supported.

  Description:
    These enumerated values list the type of SDRAM devices supported.

  Remarks:
    None.
*/
typedef enum
{
    SDRAM = 0,
    SDRAM_LOW_POWER
} SDRAMC_DEVICE_TYPE;

//*******************************************************************************
/* SDRAM Low Power configuration

  Summary:
    Enumerated data type listing the low power configuration options.

  Description:
    These enumerated values list the SDRAM low power configuration options.

  Remarks:
    None.
*/
typedef enum
{
    SDRAMC_LP_DISABLED = 0,
    SDRAMC_LP_SELF_REFRESH,
    SDRAMC_LP_POWER_DOWN,
    SDRAMC_LP_DEEP_POWER_DOWN,
} SDRAMC_LP_CONFIG;

//*******************************************************************************
/* SDRAM Low Power Timeout

  Summary:
    Enumerated data type listing the times when low power is enabled.

  Description:
    These enumerated values list the times when the low power is enabled.

  Remarks:
    None.
*/
typedef enum
{
    LAST_TRANSFER_NO_WAIT = 0,
    LAST_TRANSFER_64_CYCLES,
    LAST_TRANSFER_128_CYCLES,
} SDRAMC_LP_TIMEOUT;

/* Get Core Clock Frequency */
#define SDRAMC_CORE_CLOCK_FREQ 		${SDRAMC_CORE_CLK_FREQ}

/* Get Core Clock Frequency */
#define SDRAMC_MASTER_CLOCK_FREQ 	${SDRAMC_MASTER_CLK_FREQ}

/* SDRAM Device features. */
<#if SDRAMC_MDR == "SDRAM">
#define SDRAMC_DEVICE_TYPE       	(SDRAM)
<#else>
#define SDRAMC_DEVICE_TYPE       	(SDRAM_LOW_POWER)
</#if>
<#if SDRAMC_CR_NR == "2048_ROWS">
#define SDRAMC_NUM_ROWS          	(SDRAMC_NUM_ROWS_2048)
<#elseif SDRAMC_CR_NR == "4096_ROWS">
#define SDRAMC_NUM_ROWS          	(SDRAMC_NUM_ROWS_4096)
<#else>
#define SDRAMC_NUM_ROWS          	(SDRAMC_NUM_ROWS_8192)
</#if>
#define SDRAMC_NUM_ROWS_BITS     	(SDRAMC_NUM_ROWS + 11)
<#if SDRAMC_CR_NC == "256_COLS">
#define SDRAMC_NUM_COLS          	(SDRAMC_NUM_COLS_256)
<#elseif SDRAMC_CR_NC == "512_COLS">
#define SDRAMC_NUM_COLS          	(SDRAMC_NUM_COLS_512)
<#elseif SDRAMC_CR_NC == "1024_COLS">
#define SDRAMC_NUM_COLS          	(SDRAMC_NUM_COLS_1024)
<#else>
#define SDRAMC_NUM_COLS          	(SDRAMC_NUM_COLS_2048)
</#if>
#define SDRAMC_NUM_COLS_BITS     	(SDRAMC_NUM_COLS + 8)
<#if SDRAMC_CR_NB == "2_BANKS">
#define SDRAMC_NUM_BANKS         	(SDRAMC_NUM_BANKS_2)
<#else>
#define SDRAMC_NUM_BANKS         	(SDRAMC_NUM_BANKS_4)
</#if>
#define SDRAMC_BUS_WIDTH         	(SDRAMC_DATA_BUS_WIDTH_16BIT)
<#if SDRAMC_OCMS_SDR_SE == true>

/* Off-chip Memory Scrambling Keys. */
#define SDRAMC_MEMORY_SCRAMBING_KEY1	${SDRAMC_OCMS_KEY1}
#define SDRAMC_MEMORY_SCRAMBING_KEY2 	${SDRAMC_OCMS_KEY2}
</#if>

/* SDRAM Mode configuration parameters. */
#define SDRAMC_BURST_LENGTH     	${SDRAMC_BURST_LENGTH}
/* Burst Type. */
<#if SDRAMC_BURST_TYPE == "SEQUENTIAL">
#define SDRAMC_BURST_TYPE        	(SDRAMC_BURST_TYPE_SEQUENTIAL)
<#else>
#define SDRAMC_BURST_TYPE        	(SDRAMC_BURST_TYPE_INTERLEAVED)
</#if>

/* SDRAM timing parameters. */
#define SDRAMC_TRCD_DELAY        	${SDRAMC_CR_TRCD}
#define SDRAMC_CAS_LATENCY       	${SDRAMC_CR_CAS}
#define SDRAMC_TRAS_DELAY        	${SDRAMC_CR_TRAS}
#define SDRAMC_TRP_DELAY         	${SDRAMC_CR_TRP}
#define SDRAMC_TRC_TRFC_DELAY    	${SDRAMC_CR_TRC_TRFC}
#define SDRAMC_TWR_DELAY         	${SDRAMC_CR_TWR}
#define SDRAMC_TMRD_DELAY        	${SDRAMC_CFR1_TMRD}

<#if SDRAMC_MDR == "LOW_POWER_SDRAM">
/* Low-power configuration parameters. */
<#if SDRAMC_LPR_LPCB == "DISABLED">
#define SDRAMC_LOW_POWER_CONFIG  	(SDRAMC_LP_DISABLED)
<#elseif SDRAMC_LPR_LPCB == "SELF_REFRESH">
#define SDRAMC_LOW_POWER_CONFIG  	(SDRAMC_LP_SELF_REFRESH)
<#elseif SDRAMC_LPR_LPCB == "POWER_DOWN">
#define SDRAMC_LOW_POWER_CONFIG  	(SDRAMC_LP_POWER_DOWN)
<#else>
#define SDRAMC_LOW_POWER_CONFIG  	(SDRAMC_LP_DEEP_POWER_DOWN)
</#if>
<#if SDRAMC_LPR_TIMEOUT == "LAST_TRANSFER_NO_WAIT">
#define SDRAMC_LOW_POWER_TIMEOUT 	(LAST_TRANSFER_NO_WAIT)
<#elseif SDRAMC_LPR_TIMEOUT == "LAST_TRANSFER_64_CYCLES">
#define SDRAMC_LOW_POWER_TIMEOUT 	(LAST_TRANSFER_64_CYCLES)
<#else>
#define SDRAMC_LOW_POWER_TIMEOUT 	(LAST_TRANSFER_128_CYCLES)
</#if>
#define SDRAMC_TXSR_DELAY        	${SDRAMC_CR_TXSR}
#define SDRAMC_PASR              	${SDRAMC_LPR_PASR}
#define SDRAMC_TCSR              	${SDRAMC_LPR_TCSR}
#define SDRAMC_DS                	${SDRAMC_LPR_DS}
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
void SDRAMC${INDEX?string}_Initialize( void );

#endif // #ifndef _PLIB_SDRAMC${INDEX?string}_H
/*******************************************************************************
 End of File
*/
