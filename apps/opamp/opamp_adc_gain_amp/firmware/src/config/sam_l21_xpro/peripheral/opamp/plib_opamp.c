/*******************************************************************************
  Operational Amplifier  PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_opamp.c

  Summary:
    OPAMP Source File

  Description:
    This file defines the interface to the OPAMP peripheral library.
    This library provides access to and control of the associated
    Operational Amplifier .

  Remarks:
    None.

*******************************************************************************/
// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END
#include "plib_opamp.h"

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void OPAMP_Initialize(void)
{
    /* Reset the peripheral */
    OPAMP_REGS->OPAMP_CTRLA = OPAMP_CTRLA_SWRST_Msk;
    /* Configure OPAMPCTRL2 */
    OPAMP_REGS->OPAMP_OPAMPCTRL2 = OPAMP_OPAMPCTRL2_MUXPOS(0) | OPAMP_OPAMPCTRL2_MUXNEG(1) | OPAMP_OPAMPCTRL2_BIAS(0) | OPAMP_OPAMPCTRL2_RES1MUX(3) | OPAMP_OPAMPCTRL2_POTMUX(1) | OPAMP_OPAMPCTRL2_ANAOUT_Msk | OPAMP_OPAMPCTRL2_RES2OUT_Msk | OPAMP_OPAMPCTRL2_RES1EN_Msk | OPAMP_OPAMPCTRL2_ENABLE_Msk ;
    
    /* Enable the peripheral */
    OPAMP_REGS->OPAMP_CTRLA = OPAMP_CTRLA_ENABLE_Msk  | OPAMP_CTRLA_LPMUX_Msk;
}
