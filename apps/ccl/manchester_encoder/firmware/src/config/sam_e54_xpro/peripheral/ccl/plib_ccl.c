/*******************************************************************************
  Configurable Custom Logic (CCL) Peripheral Library Source File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ccl.c

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
#include "plib_ccl.h"

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
// CCL PLib Interface Routines
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
/* Function:
    void CCL_Initialize(void)

   Summary:
    Initializes the CCL peripheral.

   Precondition:
    None.

   Parameters:
    None.

   Returns:
    None
*/
void CCL_Initialize(void)
{
    /* First, reset CCL registers to their initial states */
    /* SWRST = 1 */
    CCL_REGS->CCL_CTRL = 0x1;
    
    /* SEQSEL = 0x0 */
    CCL_REGS->CCL_SEQCTRL[0] = 0x0;

    /* SEQSEL = 0x0 */
    CCL_REGS->CCL_SEQCTRL[1] = 0x0;

    /* ENABLE  = true */
    /* FILTSEL = 2   */
    /* EDGESEL = 0   */
    /* INSEL0  = 0   */
    /* INSEL1  = 9   */
    /* INSEL2  = 4   */
    /* INVEI   = 0   */
    /* LUTEI   = 0   */
    /* LUTEO   = 0   */
    /* TRUTH   = 14   */
    CCL_REGS->CCL_LUTCTRL[0] = 0x14049022;
    
    /* ENABLE  = false */
    /* FILTSEL = 0   */
    /* EDGESEL = 0   */
    /* INSEL0  = 0   */
    /* INSEL1  = 0   */
    /* INSEL2  = 0   */
    /* INVEI   = 0   */
    /* LUTEI   = 0   */
    /* LUTEO   = 0   */
    /* TRUTH   = 0   */
    CCL_REGS->CCL_LUTCTRL[1] = 0x0;
    
    /* ENABLE  = false */
    /* FILTSEL = 0   */
    /* EDGESEL = 0   */
    /* INSEL0  = 0   */
    /* INSEL1  = 0   */
    /* INSEL2  = 0   */
    /* INVEI   = 0   */
    /* LUTEI   = 0   */
    /* LUTEO   = 0   */
    /* TRUTH   = 0   */
    CCL_REGS->CCL_LUTCTRL[2] = 0x0;
    
    /* ENABLE  = false */
    /* FILTSEL = 0   */
    /* EDGESEL = 0   */
    /* INSEL0  = 0   */
    /* INSEL1  = 0   */
    /* INSEL2  = 0   */
    /* INVEI   = 0   */
    /* LUTEI   = 0   */
    /* LUTEO   = 0   */
    /* TRUTH   = 0   */
    CCL_REGS->CCL_LUTCTRL[3] = 0x0;
    
    /* SWRST    = 0 */
    /* ENABLE   = 1 */
    /* RUNSTDBY = 0 */
    CCL_REGS->CCL_CTRL = 0x2;
    
}


/*******************************************************************************
 End of File
*/
