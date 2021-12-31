/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
#ifndef PLIB_GIC_H
#define PLIB_GIC_H

#include <stddef.h>
#include <stdbool.h>
#include "device.h"

#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif


// *****************************************************************************
// *****************************************************************************
// Section: Data types
// *****************************************************************************
// *****************************************************************************
typedef void (*SGI_HANDLER)(uint32_t sgiID, uint32_t cpuID);

typedef void (*PPI_SPI_HANDLER)(void);

// *****************************************************************************
// *****************************************************************************
// Section: Interface routines
// *****************************************************************************
// *****************************************************************************
void GIC_Initialize(void);
void GIC_RegisterSGIInterruptHandler(SGI_HANDLER pHandler);
void GIC_RegisterPeripheralInterruptHandler(IRQn_Type irqID, PPI_SPI_HANDLER pHandler);
void GIC_INT_IrqEnable(void);
bool GIC_INT_IrqDisable(void);
void GIC_INT_IrqRestore(bool state);

#ifdef __cplusplus
}
#endif

#endif //PLIB_GIC_H