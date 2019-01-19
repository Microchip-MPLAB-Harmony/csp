/*******************************************************************************
  Output Compare (OCMP${INDEX}) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ocmp${INDEX}.c

  Summary:
    OCMP${INDEX} Source File

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
#include "plib_ocmp${INDEX}.h"

<#--Implementation-->
// *****************************************************************************

// *****************************************************************************
// Section: OCMP${INDEX} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void OCMP${INDEX}_Initialize (void)

  Summary:
    Initialization function OCMP${INDEX} peripheral

  Description:
    This function initializes the OCMP${INDEX} peripheral with user input 
	from the configurator.

  Parameters:
    none

  Returns:
    void
*/
void OCMP${INDEX}_Initialize (void)
{
	/*Setup OC${INDEX}CON		*/
	/*OCM 		= ${OCMP_OCxCON_OCM}		*/
	/*OCTSEL	= ${OCMP_OCxCON_OCTSEL}		*/
	/*OC32	 	= ${OCMP_OCxCON_OC32}		*/
	/*SIDL 		= ${OCMP_OCxCON_SIDL?then('true', 'false')}	*/
	
	OC${INDEX}CON = 0x${OCxCON_VALUE};
	<#if OCMP_INTERRUPT_ENABLE?c == 'true'>
	
	/*Setup OCMP${INDEX} Interrupt*/
	/*Priority		= ${IPC_PRI_VALUE}	*/
	/*Subpriority	= ${IPC_SUBPRI_VALUE}	*/
	
	${IPC_REG} = 0x${IPC_VALUE};
	${IEC_REG} = _${IEC_REG}_OC${INDEX}IE_MASK;
	</#if>
}

// *****************************************************************************
/* Function:
   void OCMP${INDEX}_Enable (void)

  Summary:
    Enable function OCMP${INDEX} peripheral

  Description:
    This function enables the OCMP${INDEX} peripheral

  Parameters:
    none

  Returns:
    void
*/
void OCMP${INDEX}_Enable (void)
{
	OC${INDEX}CONSET = _OC${INDEX}CON_ON_MASK;
}

// *****************************************************************************
/* Function:
   void OCMP${INDEX}_Disable (void)

  Summary:
    Disable function OCMP${INDEX} peripheral

  Description:
    This function disables the OCMP${INDEX} peripheral.

  Parameters:
    none

  Returns:
    void
*/
void OCMP${INDEX}_Disable (void)
{
	OC${INDEX}CONCLR = _OC${INDEX}CON_ON_MASK;
}

// *****************************************************************************
/* Function:
   bool OCMP${INDEX}_StatusGet (void)

  Summary:
    Get OCMP${INDEX} status

  Description:
    Returns the current state of PWM Fault Condition status bit

  Parameters:
    void

  Returns:
    bool
*/
bool OCMP${INDEX}_StatusGet (void)
{
	bool status = OC${INDEX}CON & _OC${INDEX}CON_OCFLT_MASK;
	
	return status;
}

// *****************************************************************************
/* Function:
   void OCMP${INDEX}_CompareValueSet (uint32_t value)

  Summary:
    Set OCMP${INDEX} Compare Register

  Description:
    Sets the value in the Compare Register

  Parameters:
    uint32_t 

  Returns:
    void
*/
void OCMP${INDEX}_CompareValueSet (uint32_t value)
{
	OC${INDEX}R = value;
}

// *****************************************************************************
/* Function:
   void OCMP${INDEX}_CompareSecondaryValueSet (uint32_t value)

  Summary:
    Set OCMP${INDEX} Secondary Compare Register

  Description:
    Sets the value in the Secondary Compare Register

  Parameters:
    uint32_t 

  Returns:
    void
*/
void OCMP${INDEX}_CompareSecondaryValueSet (uint32_t value)
{
	OC${INDEX}RS = value;
}

// *****************************************************************************
/* Function:
   uint32_t OCMP${INDEX}_CompareValueGet (void)

  Summary:
    Get OCMP${INDEX} Compare Register

  Description:
    Gets the value in the Compare Register

  Parameters:
    void 

  Returns:
    uint32_t
*/
uint32_t OCMP${INDEX}_CompareValueGet (void)
{
	uint32_t value = OC${INDEX}R;
	
	return value;
}

// *****************************************************************************
/* Function:
   uint32_t OCMP${INDEX}_CompareSecondaryValueGet (void)

  Summary:
    Get OCMP${INDEX} Secondary Compare Register

  Description:
    Gets the value in the Secondary Compare Register

  Parameters:
    void 

  Returns:
    uint32_t
*/
uint32_t OCMP${INDEX}_CompareSecondaryValueGet (void)
{
	uint32_t value = OC${INDEX}RS;
	
	return value;
}
<#if OCMP_INTERRUPT_ENABLE?c == "true">

OCMP_OBJECT ocmp${INDEX}Obj;

// *****************************************************************************
/* Function:
  void OCMP${INDEX}_CallbackRegister( OCMP_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a ocmp interrupt.

  Description:
    This function sets the callback function that will be called when the OCMP
    conditions are met.

  Precondition:
    None.

  Parameters:
    *callback   - a pointer to the function to be called when value is reached.
                  Use NULL to Un Register the compare callback

    context     - a pointer to user defined data to be used when the callback
                  function is called. NULL can be passed in if no data needed.

  Returns:
    void
*/
void OCMP${INDEX}_CallbackRegister(OCMP_CALLBACK callback, uintptr_t context)
{
    ocmp${INDEX}Obj.callback = callback;
    ocmp${INDEX}Obj.context = context;
}

void __ISR(_OUTPUT_COMPARE_${INDEX}_VECTOR, ipl${IPC_PRI_VALUE}AUTO) ${ISR_HANDLER_NAME} (void)
{
	${IFS_REG}CLR = _${IFS_REG}_IC${INDEX}IF_MASK;	//Clear IRQ flag

	if( (ocmp${INDEX}Obj.callback != NULL))
	{
		ocmp${INDEX}Obj.callback(ocmp${INDEX}Obj.context);
	}
}
</#if>