/*******************************************************************************
  TRAM Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_tram.c

  Summary:
    TRAM Source File

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

#include "device.h"
#include "plib_tram.h"

void TRAM_Initialize( void )
{
    TRAM_REGS->TRAM_CTRLA = TRAM_CTRLA_SWRST_Msk;
    while((TRAM_REGS->TRAM_SYNCBUSY & TRAM_SYNCBUSY_SWRST_Msk) == TRAM_SYNCBUSY_SWRST_Msk)
    {
        //wait for synchronization
    }

    TRAM_REGS->TRAM_CTRLA = TRAM_CTRLA_ENABLE_Msk | TRAM_CTRLA_TAMPERS_Msk;
    
    while((TRAM_REGS->TRAM_SYNCBUSY & TRAM_SYNCBUSY_ENABLE_Msk) == TRAM_SYNCBUSY_ENABLE_Msk)
    {
        //wait for synchronization
    }

}

