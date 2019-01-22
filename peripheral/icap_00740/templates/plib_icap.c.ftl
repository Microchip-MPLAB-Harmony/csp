/*******************************************************************************
  Input Capture (ICAP${INDEX}) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_icap${INDEX}.c

  Summary:
    ICAP${INDEX} Source File

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
#include "plib_icap${INDEX}.h"

<#--Implementation-->
// *****************************************************************************

// *****************************************************************************
// Section: ICAP${INDEX} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void ICAP${INDEX}_Initialize (void)

  Summary:
    Initialization function ICAP${INDEX} peripheral

  Description:
    This function initializes the ICAP${INDEX} peripheral with user input 
	from the configurator.

  Parameters:
    none

  Returns:
    void
*/
void ICAP${INDEX}_Initialize (void)
{
	/*Setup IC${INDEX}CON	*/
	/*ICM 	= ${ICAP_ICxCON_ICM}		*/
	/*ICI 	= ${ICAP_ICxCON_ICI}		*/
	/*ICTMR = ${ICAP_ICxCON_ICTMR}		*/
	/*C32 	= ${ICAP_ICxCON_C32}		*/
	/*FEDGE = ${ICAP_ICxCON_FEDGE}		*/
	/*SIDL 	= ${ICAP_ICxCON_SIDL?then('true', 'false')}	*/

	IC${INDEX}CON = 0x${ICxCON_VALUE};
    <#if ICAP_INTERRUPT_ENABLE?c == 'true'>
    ${ICAPx_IEC_REG}SET = _${ICAPx_IEC_REG}_IC${INDEX}IE_MASK;
    </#if>
    <#if ICAP_ERROR_INTERRUPT_ENABLE?c == 'true'>
    ${ERROR_IEC_REG}SET = _${ERROR_IEC_REG}_IC${INDEX}EIE_MASK;
    </#if>
}

// *****************************************************************************
/* Function:
   void ICAP${INDEX}_CaptureEnable (void)

  Summary:
    Enable function for the ICAP${INDEX} peripheral

  Description:
    This function enables the ICAP${INDEX} peripheral.

  Parameters:
    none

  Returns:
    void
*/
void ICAP${INDEX}_CaptureEnable (void)
{
	IC${INDEX}CONSET = _IC${INDEX}CON_ON_MASK;
}

// *****************************************************************************
/* Function:
   void ICAP${INDEX}_CaptureDisable (void)

  Summary:
    Disable function for the ICAP${INDEX} peripheral

  Description:
    This function disables the ICAP${INDEX} peripheral.

  Parameters:
    none

  Returns:
    void
*/
void ICAP${INDEX}_CaptureDisable (void)
{
	IC${INDEX}CONCLR = _IC${INDEX}CON_ON_MASK;
}

// *****************************************************************************
/* Function:
   uint32_t ICAP${INDEX}_BufferRead (void)

  Summary:
    Read buffer function ICAP${INDEX} peripheral

  Description:
    This function will return the value contained in the ICAP${INDEX} peripheral 
	buffer.

  Parameters:
    none

  Returns:
    uint32_t
*/
uint32_t ICAP${INDEX}_CaptureReadBuffer (void)
{
	uint32_t buffer = IC${INDEX}BUF;
	return buffer;
}

// *****************************************************************************
/* Function:
   void ICAP${INDEX}_StatusGet (void)

  Summary:
    ICAP${INDEX} status

  Description:
    Returns the current state overflow or buffer not empty flags

  Parameters:
    source	overFlow, buffNotEmpty

  Returns:
    bool
*/
bool ICAP${INDEX}_StatusGet (ICAP_STATUS_SOURCE source)
{
	return ((IC${INDEX}CON >> source) & 0x1);
}
<#if ICAP_INTERRUPT_ENABLE?c == "true">

ICAP_OBJECT icap${INDEX}Obj;

// *****************************************************************************
/* Function:
  void ICAP${INDEX}_CallbackRegister( ICAP_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a icap interrupt.

  Description:
    This function sets the callback function that will be called when the ICAP
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
void ICAP${INDEX}_CallbackRegister(ICAP_CALLBACK callback, uintptr_t context)
{
    icap${INDEX}Obj.callback = callback;
    icap${INDEX}Obj.context = context;
}

// *****************************************************************************
/* Function:
  void INPUT_CAPTURE_${INDEX}_Tasks( void )

  Summary:
    Interrupt handler.
  Description:
    This function does the PLIB-specific actions, and is called by the actual handler
    function.
  Precondition:
    None.
  Parameters:
    None.
  Returns:
    void
*/
void INPUT_CAPTURE_${INDEX}_Tasks (void)
{
    ${ICAPx_IFS_REG}CLR = _${ICAPx_IFS_REG}_IC${INDEX}IF_MASK;	//Clear IRQ flag

	if( (icap${INDEX}Obj.callback != NULL))
	{
		icap${INDEX}Obj.callback(icap${INDEX}Obj.context);
	}
}
</#if>
<#if ICAP_ERROR_INTERRUPT_ENABLE?c == "true">

ICAP_OBJECT icap${INDEX}errObj;

// *****************************************************************************
/* Function:
  void ICAP${INDEX}_Error_CallbackRegister( ICAP_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a icap error interrupt.

  Description:
    This function sets the callback function that will be called when the ICAP
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
void ICAP${INDEX}_Error_CallbackRegister(ICAP_CALLBACK callback, uintptr_t context)
{
    icap${INDEX}errObj.callback = callback;
    icap${INDEX}errObj.context = context;
}


// *****************************************************************************
/* Function:
  void INPUT_CAPTURE_${INDEX}_ERROR_Tasks (void)
  Summary:
    Error interrupt handler.
  Description:
    This function does the PLIB-specific actions, and is called by the actual handler
    function.
  Precondition:
    None.
  Parameters:
    None.
  Returns:
    void
*/
void INPUT_CAPTURE_${INDEX}_ERROR_Tasks (void)
{
    ${ICAPx_IFS_REG}CLR = _${ICAPx_IFS_REG}_IC${INDEX}EIF_MASK;	//Clear IRQ flag

	if( (icap${INDEX}errObj.callback != NULL))
	{
		icap${INDEX}errObj.callback(icap${INDEX}errObj.context);
	}
}
</#if>