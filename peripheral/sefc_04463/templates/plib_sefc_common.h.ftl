/*******************************************************************************
 Common definition of SEFCx PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_sefc_common.h

 Summary:
    Common definition of SEFCx Plib.

 Description:
    This file defines data types and definitions for the SEFCx Plib.
*******************************************************************************/

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

#ifndef SEFC_COMMON_H    // Guards against multiple inclusion
#define SEFC_COMMON_H

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>
#include <sys/attribs.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

#define SEFC_ERROR_NONE              0x1
/* In-valid command */
#define SEFC_CMD_ERROR               0x2
/* Flash region is locked */
#define SEFC_LOCK_ERROR              0x4
/* Flash Error */
#define SEFC_FLERR_ERROR             0x8
/* Write Protection Error */
#define SEFC_WPERR_ERROR             0x10
/* Flash Suspended Status */
#define SEFC_FLSUSP_STATUS           0x20
/* Flash Encountered an ECC error */
#define SEFC_ECC_ERROR               0xFF0000

typedef enum
{
    /* Block 0 of user signature. Erasable by erase signal */
    BLOCK_0 = 1,
    /* Block 1 of user signature. Erasable by erase signal */
    BLOCK_1,
    /* Block 2 of user signature. Erasable by erase signal */
    BLOCK_2,
    /* Block 3 of user signature. No erasable by erase signal */
    BLOCK_3,
    /* Block 4 of user signature. No erasable by erase signal */
    BLOCK_4,
    /* Block 5 of user signature. No erasable by erase signal */
    BLOCK_5,
} SEFC_USERSIGNATURE_BLOCK;

typedef enum
{
    PAGE_0 = 0,
    PAGE_1,
    PAGE_2,
    PAGE_3,
    PAGE_4,
    PAGE_5,
    PAGE_6,
    PAGE_7,
} SEFC_USERSIGNATURE_PAGE;

typedef uint32_t SEFC_ERROR;

typedef void (*SEFC_CALLBACK)(uintptr_t context);

typedef struct
{
    SEFC_CALLBACK callback;
    uintptr_t     context;
    uint32_t      panelBaseAddr;
} SEFC_OBJECT;

<#if SEFC_DUAL_PANEL == true>

typedef enum
{
    SEFC_FLASH_PANEL0 = 0,
    SEFC_FLASH_PANEL1,
    
}SEFC_FLASH_PANEL;

__longramfunc__ uint32_t SEFC_GpnvmBitRead(void);
__longramfunc__ void SEFC_GpnvmBitSet(uint8_t GpnvmBitNumber);
__longramfunc__ void SEFC_GpnvmBitClear(uint8_t GpnvmBitNumber);
SEFC_FLASH_PANEL SEFC_FlashPanelGet(uint32_t address);
bool SEFC_SectorErase( uint32_t address );
bool SEFC_PageBufferWrite( uint32_t *data, const uint32_t address);
bool SEFC_PageBufferCommit( const uint32_t address);
bool SEFC_PageWrite( uint32_t *data, uint32_t address );
bool SEFC_QuadWordWrite( uint32_t *data, uint32_t address );
void SEFC_RegionLock(uint32_t address);
void SEFC_RegionUnlock(uint32_t address);
bool SEFC_IsBusy(uint32_t address);
SEFC_ERROR SEFC_ErrorGet(uint32_t address);

</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif //SEFC_COMMON_H
