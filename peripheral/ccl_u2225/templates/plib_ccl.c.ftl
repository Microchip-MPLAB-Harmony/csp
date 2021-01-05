/*******************************************************************************
  Configurable Custom Logic (CCL) Peripheral Library Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CCL_INSTANCE_NAME?lower_case}.c

  Summary:
    CCL peripheral library interface.

  Description:
    This file defines the interface to the CCL peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
//DOM-IGNORE-END
// *****************************************************************************
// *****************************************************************************
// Header Includes
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_${CCL_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************


/******************************************************************************
Local Functions
******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// ${CCL_INSTANCE_NAME} PLib Interface Routines
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* Function:
    void ${CCL_INSTANCE_NAME}_Initialize(void)

   Summary:
    Initializes the CCL peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None
*/
void ${CCL_INSTANCE_NAME}_Initialize(void)
{
    /* First, reset CCL registers to their initial states */
    /* SWRST = 1 */
    CCL_REGS->CCL_CTRL = 0x${CCL_CTRL_SWRST_MASK}U;
    
<#list 0..NUM_SEQUENTIAL_BLOCKS - 1 as i>
    <#assign SEQ_REGVALUE = "CCL_SEQCTRL_REGVALUE" + i>
    <#assign SEQ_SEQSEL = "SEQCTRL" + i + "__SEQSEL">
    /* SEQSEL = 0x${.vars[SEQ_SEQSEL]} */
    CCL_REGS->CCL_SEQCTRL[${i}] = 0x${.vars[SEQ_REGVALUE]}U;

</#list>
<#list 0..NUM_LUT_BLOCKS - 1 as i>
    <#assign LUTCTRL_REGVALUE = "CCL_LUTCTRL_REGVALUE" + i>
    <#assign LUTCTRL_ENABLE = "LUTCTRL" + i + "__ENABLE">
    <#assign LUTCTRL_FILTSEL = "LUTCTRL" + i + "__FILTSEL">
    <#assign LUTCTRL_EDGESEL = "LUTCTRL" + i + "__EDGESEL">
    <#assign LUTCTRL_INSEL0 = "LUTCTRL" + i + "__INSEL0">
    <#assign LUTCTRL_INSEL1 = "LUTCTRL" + i + "__INSEL1">
    <#assign LUTCTRL_INSEL2 = "LUTCTRL" + i + "__INSEL2">
    <#assign LUTCTRL_INVEI = "LUTCTRL" + i + "__INVEI">
    <#assign LUTCTRL_LUTEI = "LUTCTRL" + i + "__LUTEI">
    <#assign LUTCTRL_LUTEO = "LUTCTRL" + i + "__LUTEO">
    <#assign LUTCTRL_TRUTH = "LUTCTRL" + i + "__TRUTH">
    /* ENABLE  = ${.vars[LUTCTRL_ENABLE]?string} */
    /* FILTSEL = ${.vars[LUTCTRL_FILTSEL]}   */
    /* EDGESEL = ${.vars[LUTCTRL_EDGESEL]}   */
    /* INSEL0  = ${.vars[LUTCTRL_INSEL0]}   */
    /* INSEL1  = ${.vars[LUTCTRL_INSEL1]}   */
    /* INSEL2  = ${.vars[LUTCTRL_INSEL2]}   */
    /* INVEI   = ${.vars[LUTCTRL_INVEI]}   */
    /* LUTEI   = ${.vars[LUTCTRL_LUTEI]}   */
    /* LUTEO   = ${.vars[LUTCTRL_LUTEO]}   */
    /* TRUTH   = ${.vars[LUTCTRL_TRUTH]}   */
    CCL_REGS->CCL_LUTCTRL[${i}] = 0x${.vars[LUTCTRL_REGVALUE]}U;
    
</#list>
    /* SWRST    = 0 */
    /* ENABLE   = ${CTRL0__ENABLE} */
    /* RUNSTDBY = ${CTRL0__RUNSTDBY} */
    CCL_REGS->CCL_CTRL = 0x${CCL_CTRL_REGVALUE}U;
    
}


/*******************************************************************************
 End of File
*/
