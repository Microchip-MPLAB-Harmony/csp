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

// *****************************************************************************

// *****************************************************************************
// Section: EBI Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void EBI_Initialize (void)

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
	/*EBICS0*/
	EBICS0 = 0x20000000;
	
	/* Setup EBIMSK0	*/
	/* MEMSIZE = 6		*/
	/* MEMTYPE = 1		*/
	/* REGSEL  = 0		*/
	EBIMSK0 = 0x26;
	
	/* Setup EBISMT0	*/
	/* TRC 	= 2		*/
	/* TAS 	= 2			*/
	/* TWR  = 1			*/
	/* TWP 	= 10		*/
	/* TBTA = 0			*/
	/* TPRC = 0			*/	
	/* PAGEMODE = false	*/	
	/* PAGESIZE = 0		*/	
	/* RDYMODE  = false	*/	
	EBISMT0 = 0x2982;
	
	/* Setup EBISMT1	*/
	/* TRC 	= 11		*/
	/* TAS 	= 1			*/
	/* TWR  = 1			*/
	/* TWP 	= 11		*/
	/* TBTA = 4			*/
	/* TPRC = 3			*/	
	/* PAGEMODE = false	*/	
	/* PAGESIZE = 0		*/	
	/* RDYMODE  = false	*/		
	EBISMT1 = 0x41c2d4b;	

	/* Setup EBISMT2	*/
	/* TRC 	= 11		*/
	/* TAS 	= 1			*/
	/* TWR  = 1			*/
	/* TWP 	= 11   		*/
	/* TBTA = 4			*/
	/* TPRC = 3			*/	
	/* PAGEMODE = false	*/	
	/* PAGESIZE = 0		*/	
	/* RDYMODE  = false	*/		
	EBISMT2 = 0x41c2d4b;	
	
	/* EBIFTRPD*/
	EBIFTRPD = 0xc8;
	
	/* Setup EBISMCON	*/
	/* SMDWIDTH0 = 0	*/
	/* SMDWIDTH1 = 0	*/
	/* SMDWIDTH2 = 0	*/
	EBISMCON = 0x1;
	
	/* Setup CFGEBIA	*/
	CFGEBIA = 0x800fffffL;

	/* Setup CFGEBIC	*/
	/* EBIRDYINV3 = false	*/
	/* EBIRDYINV2 = false	*/
	/* EBIRDYINV1 = false	*/
	/* EBIRDYEN3  = false	*/
	/* EBIRDYEN2  = false	*/
	/* EBIRDYEN1  = false	*/
	/* EBIRDYLVL  = false	*/
	/* EBIRPEN    = false	*/
	/* EBIWEEN    = true	*/
	/* EBIOEEN    = true	*/
	/* EBIBSEN1   = true	*/
	/* EBIBSEN0   = true	*/
	/* EBICSEN3   = false	*/
	/* EBICSEN2   = false	*/
	/* EBICSEN1   = false	*/
	/* EBICSEN0   = true	*/
	/* EBIDEN1    = true	*/
	/* EBIDEN0    = true	*/
	CFGEBIC = 0x3313;
}
