/*******************************************************************************
  DWT PLIB Header File

  Company:
    Microchip Technology Inc.

  File Name:
    plib_dwt.h

  Summary:
    Interface definition of the Data Watchpoint and Trace (DWT) Plib.

  Description:
    This file defines the interface for the Data Watchpoint and Trace (DWT) Plib.
*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_DWT_H    // Guards against multiple inclusion
#define PLIB_DWT_H

#include <stdint.h>
#include <stddef.h>

#ifdef __cplusplus // Provide C++ Compatibility
    extern "C" {
#endif

// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************
void DWT_Initialize(void);
void DWT_DelayUs(uint32_t delay_us);
void DWT_DelayMs(uint32_t delay_ms);
void DWT_CounterReset(void);
void DWT_CounterEnable(void);
void DWT_CounterDisable(void);
uint32_t DWT_CounterGet(void);

#ifdef __cplusplus // Provide C++ Compatibility
 }
#endif

#endif //PLIB_DWT_H
