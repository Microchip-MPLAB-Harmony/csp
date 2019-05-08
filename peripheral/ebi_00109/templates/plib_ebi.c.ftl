/*******************************************************************************
  External Bus Interface (EBI) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ebi.c

  Summary:
    EBI Source File

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
#include "plib_ebi.h"

<#--Implementation-->
// *****************************************************************************

// *****************************************************************************
// Section: EBI Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void ${EBI_INSTANCE_NAME}_Initialize (void)

  Summary:
    Initialization function EBI peripheral

  Description:
    This function initializes the EBI peripheral with user input from the 
	configurator.

  Parameters:
    none

  Returns:
    void
*/

void EBI_Initialize (void)
{
	<#if CFGEBIC_EBICSEN0?c == "true">
	/*EBICS0*/
	EBICS0 = 0x${EBICS0_CSADDR};
	
	/* Setup EBIMSK0	*/
	/* MEMSIZE = ${EBIMSK0_MEMSIZE}		*/
	/* MEMTYPE = ${EBIMSK0_MEMTYPE}		*/
	/* REGSEL  = ${EBIMSK0_REGSEL}		*/
	EBIMSK0 = 0x${EBIMSK0_VALUE};
	
	</#if>
	<#if CFGEBIC_EBICSEN1?c == "true">
	/*EBICS1*/
	EBICS1 = 0x${EBICS1_CSADDR};
	
	/* Setup EBIMSK1	*/
	/* MEMSIZE = ${EBIMSK1_MEMSIZE}		*/
	/* MEMTYPE = ${EBIMSK1_MEMTYPE}		*/
	/* REGSEL  = ${EBIMSK1_REGSEL}		*/
	EBIMSK1 = 0x${EBIMSK1_VALUE};
	
	</#if>
	<#if CFGEBIC_EBICSEN2?c == "true">
	/*EBICS2*/
	EBICS2 = 0x${EBICS2_CSADDR};
	
	/* Setup EBIMSK2	*/
	/* MEMSIZE = ${EBIMSK2_MEMSIZE}		*/
	/* MEMTYPE = ${EBIMSK2_MEMTYPE}		*/
	/* REGSEL  = ${EBIMSK2_REGSEL}		*/
	EBIMSK2 = 0x${EBIMSK2_VALUE};
	
	</#if>
	<#if CFGEBIC_EBICSEN3?c == "true">
	/*EBICS3*/
	EBICS3 = 0x${EBICS3_CSADDR};

	/* Setup EBIMSK3	*/
	/* MEMSIZE = ${EBIMSK3_MEMSIZE}		*/
	/* MEMTYPE = ${EBIMSK3_MEMTYPE}		*/
	/* REGSEL  = ${EBIMSK3_REGSEL}		*/
	EBIMSK3 = 0x${EBIMSK3_VALUE};
	
	</#if>
	/* Setup EBISMT0	*/
	/* TRC 	= ${EBISMT0_TRC}		*/
	/* TAS 	= ${EBISMT0_TAS}			*/
	/* TWR  = ${EBISMT0_TWR}			*/
	/* TWP 	= ${EBISMT0_TWP}		*/
	/* TBTA = ${EBISMT0_TBTA}			*/
	/* TPRC = ${EBISMT0_TPRC}			*/	
	/* PAGEMODE = ${EBISMT0_PAGEMODE?then('true', 'false')}	*/	
	/* PAGESIZE = ${EBISMT0_PAGESIZE}		*/	
	/* RDYMODE  = ${EBISMT0_RDYMODE?then('true', 'false')}	*/	
	EBISMT0 = 0x${EBISMT0_VALUE};
	
	/* Setup EBISMT1	*/
	/* TRC 	= ${EBISMT1_TRC}		*/
	/* TAS 	= ${EBISMT1_TAS}			*/
	/* TWR  = ${EBISMT1_TWR}			*/
	/* TWP 	= ${EBISMT1_TWP}		*/
	/* TBTA = ${EBISMT1_TBTA}			*/
	/* TPRC = ${EBISMT1_TPRC}			*/	
	/* PAGEMODE = ${EBISMT1_PAGEMODE?then('true', 'false')}	*/	
	/* PAGESIZE = ${EBISMT1_PAGESIZE}		*/	
	/* RDYMODE  = ${EBISMT1_RDYMODE?then('true', 'false')}	*/		
	EBISMT1 = 0x${EBISMT1_VALUE};	

	/* Setup EBISMT2	*/
	/* TRC 	= ${EBISMT2_TRC}		*/
	/* TAS 	= ${EBISMT2_TAS}			*/
	/* TWR  = ${EBISMT2_TWR}			*/
	/* TWP 	= ${EBISMT2_TWP}   		*/
	/* TBTA = ${EBISMT2_TBTA}			*/
	/* TPRC = ${EBISMT2_TPRC}			*/	
	/* PAGEMODE = ${EBISMT2_PAGEMODE?then('true', 'false')}	*/	
	/* PAGESIZE = ${EBISMT2_PAGESIZE}		*/	
	/* RDYMODE  = ${EBISMT2_RDYMODE?then('true', 'false')}	*/		
	EBISMT2 = 0x${EBISMT2_VALUE};	
	
	/* EBIFTRPD*/
	EBIFTRPD = 0x${EBIFTRPD_TRPD};
	
	/* Setup EBISMCON	*/
	/* SMDWIDTH0 = ${EBISMCON_SMDWIDTH0}	*/
	/* SMDWIDTH1 = ${EBISMCON_SMDWIDTH1}	*/
	/* SMDWIDTH2 = ${EBISMCON_SMDWIDTH2}	*/
	EBISMCON = 0x${EBISMCON_VALUE};
	
	/* Setup CFGEBIA	*/
	CFGEBIA = ${CFGEBIA_EBIADD};

	/* Setup CFGEBIC	*/
	/* EBIRDYINV3 = ${CFGEBIC_EBIRDYINV3?then('true', 'false')}	*/
	/* EBIRDYINV2 = ${CFGEBIC_EBIRDYINV2?then('true', 'false')}	*/
	/* EBIRDYINV1 = ${CFGEBIC_EBIRDYINV1?then('true', 'false')}	*/
	/* EBIRDYEN3  = ${CFGEBIC_EBIRDYEN3?then('true', 'false')}	*/
	/* EBIRDYEN2  = ${CFGEBIC_EBIRDYEN2?then('true', 'false')}	*/
	/* EBIRDYEN1  = ${CFGEBIC_EBIRDYEN1?then('true', 'false')}	*/
	/* EBIRDYLVL  = ${CFGEBIC_EBIRDYLVL?then('true', 'false')}	*/
	/* EBIRPEN    = ${CFGEBIC_EBIRPEN?then('true', 'false')}	*/
	/* EBIWEEN    = ${CFGEBIC_EBIWEEN?then('true', 'false')}	*/
	/* EBIOEEN    = ${CFGEBIC_EBIOEEN?then('true', 'false')}	*/
	/* EBIBSEN1   = ${CFGEBIC_EBIBSEN0?then('true', 'false')}	*/
	/* EBIBSEN0   = ${CFGEBIC_EBIBSEN1?then('true', 'false')}	*/
	/* EBICSEN3   = ${CFGEBIC_EBICSEN3?then('true', 'false')}	*/
	/* EBICSEN2   = ${CFGEBIC_EBICSEN2?then('true', 'false')}	*/
	/* EBICSEN1   = ${CFGEBIC_EBICSEN1?then('true', 'false')}	*/
	/* EBICSEN0   = ${CFGEBIC_EBICSEN0?then('true', 'false')}	*/
	/* EBIDEN1    = ${CFGEBIC_EBIDAT1?then('true', 'false')}	*/
	/* EBIDEN0    = ${CFGEBIC_EBIDAT0?then('true', 'false')}	*/
	CFGEBIC = 0x${CFGEBIC_VALUE};
}
<#--
/*******************************************************************************
 End of File
*/
-->
