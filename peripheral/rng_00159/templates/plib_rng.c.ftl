/*******************************************************************************
  Random Number Generator (${RNG_INSTANCE_NAME}) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RNG_INSTANCE_NAME}.c

  Summary:
    ${RNG_INSTANCE_NAME} Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_rng.h"

<#--Implementation-->
// *****************************************************************************

// *****************************************************************************
// Section: ${RNG_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${RNG_INSTANCE_NAME}_Initialize (void)
{
	/* Setup ${RNG_INSTANCE_NAME}CON		*/
	/* PLEN 	= ${RNGCON_PLEN}	*/
	/* TRNGEN	= ${RNGCON_TRNGEN}		*/
	/* PRNGEN	= ${RNGCON_PRNGEN}		*/
	/* CONT 	= ${RNGCON_CONT}		*/
	/* TRNGMODE	= ${RNGCON_TRNGMODE} 	*/
	
	${RNG_INSTANCE_NAME}CON = 0x${RNGCON_VALUE};
}

void ${RNG_INSTANCE_NAME}_TrngEnable(void)
{
    ${RNG_INSTANCE_NAME}CONbits.TRNGEN = 1;
}

void ${RNG_INSTANCE_NAME}_TrngDisable(void)
{
    ${RNG_INSTANCE_NAME}CONbits.TRNGEN = 0;
}

void ${RNG_INSTANCE_NAME}_WaitForTrngCnt(void)
{
    /* Random number is ready when RNGCNT value reaches PRNG Polynomial Length */
    while (RNGCNT < ${RNGCON_PLEN});
}

uint32_t ${RNG_INSTANCE_NAME}_Seed1Get (void)
{
	uint32_t seed = ${RNG_INSTANCE_NAME}SEED1;
	
	return seed;
}

uint32_t ${RNG_INSTANCE_NAME}_Seed2Get (void)
{
	uint32_t seed = ${RNG_INSTANCE_NAME}SEED2;
	
	return seed;
}

void ${RNG_INSTANCE_NAME}_PrngEnable(void)
{
    ${RNG_INSTANCE_NAME}CONbits.PRNGEN = 1;
}

void ${RNG_INSTANCE_NAME}_PrngDisable(void)
{
    ${RNG_INSTANCE_NAME}CONbits.PRNGEN = 0;
}

void ${RNG_INSTANCE_NAME}_LoadSet (void)
{
	${RNG_INSTANCE_NAME}CON |= _${RNG_INSTANCE_NAME}CON_LOAD_MASK;
}

bool ${RNG_INSTANCE_NAME}_LoadGet (void)
{
	bool load = (${RNG_INSTANCE_NAME}CON & _${RNG_INSTANCE_NAME}CON_LOAD_MASK) >> _RNGCON_LOAD_POSITION;
	
	return load;
}

void ${RNG_INSTANCE_NAME}_Poly1Set (uint32_t poly)
{
	${RNG_INSTANCE_NAME}POLY1 = poly;
}

void ${RNG_INSTANCE_NAME}_Poly2Set (uint32_t poly)
{
	${RNG_INSTANCE_NAME}POLY2 = poly;
}

uint32_t ${RNG_INSTANCE_NAME}_Poly1Get (void)
{
	uint32_t poly = ${RNG_INSTANCE_NAME}POLY1;
	
	return poly;
}

uint32_t ${RNG_INSTANCE_NAME}_Poly2Get (void)
{
	uint32_t poly = ${RNG_INSTANCE_NAME}POLY2;
	
	return poly;
}

void ${RNG_INSTANCE_NAME}_NumGen1Set (uint32_t numgen)
{
	${RNG_INSTANCE_NAME}NUMGEN1 = numgen;
}

void ${RNG_INSTANCE_NAME}_NumGen2Set (uint32_t numgen)
{
	${RNG_INSTANCE_NAME}NUMGEN2 = numgen;
}

/* Ensure to wait for ${RNGCON_PLEN} cycles (Polynomial length) after
 * enabling PRNG, for the random number generation operation to be completed
 * and result to be available in ${RNG_INSTANCE_NAME}NUMGENx
 */
uint32_t ${RNG_INSTANCE_NAME}_NumGen1Get (void)
{
	uint32_t numgen = ${RNG_INSTANCE_NAME}NUMGEN1;
	
	return numgen;
}

/* Ensure to wait for ${RNGCON_PLEN} cycles (Polynomial length) after
 * enabling PRNG, for the random number generation operation to be completed
 * and result to be available in ${RNG_INSTANCE_NAME}NUMGENx
 */
uint32_t ${RNG_INSTANCE_NAME}_NumGen2Get (void)
{
	uint32_t numgen = ${RNG_INSTANCE_NAME}NUMGEN2;
	
	return numgen;
}
