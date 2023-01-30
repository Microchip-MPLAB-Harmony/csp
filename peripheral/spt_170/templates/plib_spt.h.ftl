/*******************************************************************************
  SPI Peripheral Target Peripheral Library Interface Header File

  Company
    Microchip Technology Inc.

  File Name
    plib_${SPT_INSTANCE_NAME?lower_case}.h

  Summary
    ${SPT_INSTANCE_NAME} peripheral library interface.

  Description
    This file defines the interface to the SPI Peripheral Target library.  This
    library provides access to and control of the associated peripheral
    instance.

******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

#ifndef PLIB_${SPT_INSTANCE_NAME}_H    // Guards against multiple inclusion
#define PLIB_${SPT_INSTANCE_NAME}_H


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/*  This section lists the other files that are included in this file.
*/

#include "plib_spt_common.h"
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

extern "C" {

#endif

// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************
/*  The following data type definitions are used by the functions in this
    interface and should be considered part it.
*/

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************
/* The following functions make up the methods (set of possible operations) of
   this interface.
*/
void ${SPT_INSTANCE_NAME}_Initialize(void);

<#if SPT_MODE == "Advanced">

void ${SPT_INSTANCE_NAME}_WaitTimeSet(uint8_t wait_time);

void ${SPT_INSTANCE_NAME}_TARTimeSet(uint8_t tar_cycles);

void ${SPT_INSTANCE_NAME}_QuadModeEnable(void);

void ${SPT_INSTANCE_NAME}_QuadModeDisable(void);

void ${SPT_INSTANCE_NAME}_ECInterruptEnable(SPT_EC_INT int_en);

uint32_t ${SPT_INSTANCE_NAME}_MailBoxRead(void);

void ${SPT_INSTANCE_NAME}_MailBoxWrite(uint32_t data);

void ${SPT_INSTANCE_NAME}_CallbackRegister( SPT_CALLBACK callback, uintptr_t context );

<#else>

void ${SPT_INSTANCE_NAME}_ECDataAvailableSet(void);

</#if>

uint32_t ${SPT_INSTANCE_NAME}_ECStatusRegGet(void);

void ${SPT_INSTANCE_NAME}_ECStatusRegClear(uint32_t bitmask);

void ${SPT_INSTANCE_NAME}_MEM0Config(uint32_t bar, uint32_t wr_lim, uint32_t rd_lim);

void ${SPT_INSTANCE_NAME}_MEM1Config(uint32_t bar, uint32_t wr_lim, uint32_t rd_lim);

void ${SPT_INSTANCE_NAME}_MEM0Enable(void);

void ${SPT_INSTANCE_NAME}_MEM1Enable(void);

void ${SPT_INSTANCE_NAME}_MEM0Disable(void);

void ${SPT_INSTANCE_NAME}_MEM1Disable(void);

uint32_t ${SPT_INSTANCE_NAME}_RXFIFOByteCountGet(void);

uint32_t ${SPT_INSTANCE_NAME}_TXFIFOByteCountGet(void);

uint32_t ${SPT_INSTANCE_NAME}_RXFIFOBaseAddrGet(void);

uint32_t ${SPT_INSTANCE_NAME}_TXFIFOBaseAddrGet(void);

void ${SPT_INSTANCE_NAME}_Enable(void);

void ${SPT_INSTANCE_NAME}_Disable(void);

uint32_t ${SPT_INSTANCE_NAME}_HostToECMBXRead(void);

void ${SPT_INSTANCE_NAME}_HostToECMBXClr(void);

void ${SPT_INSTANCE_NAME}_ECToHostMBXWrite(uint32_t val);

uint32_t ${SPT_INSTANCE_NAME}_ECToHostMBXRead(void);


#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif //PLIB_${SPT_INSTANCE_NAME}_H

/**
 End of File
*/
