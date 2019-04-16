/*******************************************************************************
  ${SDMMC_INSTANCE_NAME} PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${SDMMC_INSTANCE_NAME?lower_case}.h

  Summary:
    ${SDMMC_INSTANCE_NAME} PLIB Header File

  Description:
    None

*******************************************************************************/

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
#ifndef PLIB_${SDMMC_INSTANCE_NAME}_H
#define PLIB_${SDMMC_INSTANCE_NAME}_H

#include "plib_sdmmc_common.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

#include <stdint.h>
#include <stdbool.h>

void ${SDMMC_INSTANCE_NAME}_BusWidthSet ( SDMMC_BUS_WIDTH busWidth );

void ${SDMMC_INSTANCE_NAME}_SpeedModeSet( SDMMC_SPEED_MODE speedMode );

void ${SDMMC_INSTANCE_NAME}_BlockSizeSet ( uint16_t blockSize );

void ${SDMMC_INSTANCE_NAME}_BlockCountSet( uint16_t numBlocks );

bool ${SDMMC_INSTANCE_NAME}_IsCmdLineBusy ( void );

bool ${SDMMC_INSTANCE_NAME}_IsDatLineBusy ( void );
<#if SDCARD_SDWP_SUPPORT == true>

bool ${SDMMC_INSTANCE_NAME}_IsWriteProtected ( void );
</#if>
<#if SDCARD_SDCD_SUPPORT == true>

bool ${SDMMC_INSTANCE_NAME}_IsCardAttached ( void );
</#if>

bool ${SDMMC_INSTANCE_NAME}_ClockSet ( uint32_t freq );

void ${SDMMC_INSTANCE_NAME}_ClockEnable ( void );

void ${SDMMC_INSTANCE_NAME}_ClockDisable ( void );

uint16_t ${SDMMC_INSTANCE_NAME}_ErrorGet( void );

uint16_t ${SDMMC_INSTANCE_NAME}_CommandErrorGet( void );

uint16_t ${SDMMC_INSTANCE_NAME}_DataErrorGet( void );

void ${SDMMC_INSTANCE_NAME}_ErrorReset ( SDMMC_RESET_TYPE resetType );

void ${SDMMC_INSTANCE_NAME}_ResponseRead( SDMMC_READ_RESPONSE_REG respReg, uint32_t* response );

void ${SDMMC_INSTANCE_NAME}_ModuleInit( void );

void ${SDMMC_INSTANCE_NAME}_Initialize( void );

void ${SDMMC_INSTANCE_NAME}_CallbackRegister( SDMMC_CALLBACK callback, uintptr_t contextHandle );

void ${SDMMC_INSTANCE_NAME}_CommandSend(
    uint8_t opCode, 
    uint32_t argument,
    uint8_t respType, 
    SDMMC_DataTransferFlags transferFlags
);

void ${SDMMC_INSTANCE_NAME}_DmaSetup(
    uint8_t* buffer,
    uint32_t numBytes,
    SDMMC_DATA_TRANSFER_DIR direction
);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_${SDMMC_INSTANCE_NAME}_H

