/*******************************************************************************
  Comparator (CMP) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CMP_INSTANCE_NAME?lower_case}.c

  Summary:
    CMP Source File

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

#include "plib_${CMP_INSTANCE_NAME?lower_case}.h"

<#--Implementation-->
// *****************************************************************************

<#if CMP_CM1CON_EVPOL != "0">CMP_OBJECT cmp1Obj;</#if>
<#if CMP_CM2CON_EVPOL != "0">CMP_OBJECT cmp2Obj;</#if>

// *****************************************************************************
// Section: CMP Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Function:
   void ${CMP_INSTANCE_NAME}_Initialize (void)

  Summary:
    Initialization function for both CMP1 & CMP2 channels of the CMP peripheral

  Description:
    This function initializes the CMP peripheral with user input from the
    configurator.

  Parameters:
    none

  Returns:
    void
*/

void ${CMP_INSTANCE_NAME}_Initialize (void)
{
    /*  Setup CM1CON    */
    /*  CCH     = ${CMP_CM1CON_CCH}     */
    /*  CREF    = ${CMP_CM1CON_CREF}        */
    /*  EVPOL   = ${CMP_CM1CON_EVPOL}       */
    /*  CPOL    = ${CMP_CM1CON_CPOL?then('true', 'false')}  */
    /*  COE     = ${CMP_CM1CON_COE?then('true', 'false')}   */

    CM1CON = 0x${CM1CON_VALUE};
<#if CMP_CM1CON_EVPOL != "0">

    ${CMP1_IEC_REG}SET = _${CMP1_IEC_REG}_${CMP_INSTANCE_NAME}1IE_MASK;
</#if>

    /*  Setup CM2CON    */
    /*  CCH     = ${CMP_CM2CON_CCH}     */
    /*  CREF    = ${CMP_CM2CON_CREF}        */
    /*  EVPOL   = ${CMP_CM2CON_EVPOL}       */
    /*  CPOL    = ${CMP_CM2CON_CPOL?then('true', 'false')}  */
    /*  COE     = ${CMP_CM2CON_COE?then('true', 'false')}   */

    CM2CON = 0x${CM2CON_VALUE};
<#if CMP_CM2CON_EVPOL != "0">

    ${CMP2_IEC_REG}SET = _${CMP2_IEC_REG}_${CMP_INSTANCE_NAME}2IE_MASK;
</#if>
}

// *****************************************************************************
/* Function:
   void ${CMP_INSTANCE_NAME}_1_CompareEnable (void)

  Summary:
    Enable function of the CMP1 Channel

  Description:
    This function enables the CMP1 Channel

  Parameters:
    none

  Returns:
    void
*/

void ${CMP_INSTANCE_NAME}_1_CompareEnable (void)
{
    CM1CONSET = _CM1CON_ON_MASK;
}

// *****************************************************************************
/* Function:
   void ${CMP_INSTANCE_NAME}_1_CompareDisable (void)

  Summary:
    Disable function of the CMP1 Channel

  Description:
    This function disables the CMP1 Channel

  Parameters:
    none

  Returns:
    void
*/

void ${CMP_INSTANCE_NAME}_1_CompareDisable (void)
{
    CM1CONCLR = _CM1CON_ON_MASK;
}

// *****************************************************************************
/* Function:
   void ${CMP_INSTANCE_NAME}_2_CompareEnable (void)

  Summary:
    Enable function of the CMP2 Channel

  Description:
    This function enables the CMP2 Channel

  Parameters:
    none

  Returns:
    void
*/

void ${CMP_INSTANCE_NAME}_2_CompareEnable (void)
{
    CM2CONSET = _CM2CON_ON_MASK;
}

// *****************************************************************************
/* Function:
   void ${CMP_INSTANCE_NAME}_2_CompareDisable (void)

  Summary:
    Disable function of the CMP2 Channel

  Description:
    This function disables the CMP2 Channel

  Parameters:
    none

  Returns:
    void
*/

void ${CMP_INSTANCE_NAME}_2_CompareDisable (void)
{
    CM2CONCLR = _CM2CON_ON_MASK;
}

// *****************************************************************************
/* Function:
   void ${CMP_INSTANCE_NAME}_StatusGet (CMP_STATUS_SOURCE source)

  Summary:
    CMP Channel status

  Description:
    Returns the current state of requested CMP Channel

  Parameters:
    source  cmp channel

  Returns:
    bool    current value of cmp channel output
*/

bool ${CMP_INSTANCE_NAME}_StatusGet (CMP_STATUS_SOURCE ch_status)
{
    return ((CMSTAT >> ch_status) & 0x1);
}

<#if CMP_CM1CON_EVPOL != "0">
// *****************************************************************************
/* Function:
  void ${CMP_INSTANCE_NAME}_1_CallbackRegister( CMP_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a cmp interrupt.

  Description:
    This function sets the callback function that will be called when the CMP
    value is reached.

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

void ${CMP_INSTANCE_NAME}_1_CallbackRegister(CMP_CALLBACK callback, uintptr_t context)
{
    cmp1Obj.callback = callback;

    cmp1Obj.context = context;
}

// *****************************************************************************
/* Function:
  void COMPARATOR_1_InterruptHandler( void )

  Summary:
    Is run when interrupt occurs, or during polling.  Calls the callback function if present.

  Description:
    This function is called when the comparator 1 interrupt occurs.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    void
*/
void COMPARATOR_1_InterruptHandler(void)
{
    ${CMP1_IFS_REG}CLR = _${CMP1_IFS_REG}_${CMP_INSTANCE_NAME}1IF_MASK; //Clear IRQ flag

    if(cmp1Obj.callback != NULL)
    {
        cmp1Obj.callback(cmp1Obj.context);
    }
}

</#if>

<#if CMP_CM2CON_EVPOL != "0">
// *****************************************************************************
/* Function:
  void ${CMP_INSTANCE_NAME}_2_CallbackRegister( CMP_CALLBACK callback, uintptr_t context )

  Summary:
    Sets the callback function for a cmp interrupt.

  Description:
    This function sets the callback function that will be called when the CMP
    value is reached.

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
void ${CMP_INSTANCE_NAME}_2_CallbackRegister(CMP_CALLBACK callback, uintptr_t context)
{
    cmp2Obj.callback = callback;

    cmp2Obj.context = context;
}

// *****************************************************************************
/* Function:
  void COMPARATOR_2_InterruptHandler( void )

  Summary:
    Is run when interrupt occurs, or during polling.  Calls the callback function if present.

  Description:
    This function is called when the comparator 2 interrupt occurs.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    void
*/
void COMPARATOR_2_InterruptHandler(void)
{
    ${CMP2_IFS_REG}CLR = _${CMP2_IFS_REG}_${CMP_INSTANCE_NAME}2IF_MASK; //Clear IRQ flag

    if(cmp2Obj.callback != NULL)
    {
        cmp2Obj.callback(cmp2Obj.context);
    }
}
</#if>

<#--
/*******************************************************************************
 End of File
*/
-->

