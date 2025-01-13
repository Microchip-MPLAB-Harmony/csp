/*******************************************************************************
Interface definition of ${SEFC_INSTANCE_NAME} PLIB.

Company:
Microchip Technology Inc.

File Name:
plib_sefc_common.c

Summary:
Interface definition of SEFC Common Plib.

Description:
This file defines the interface for the SEFC Common Plib.
It allows user to Program, Erase and lock the on-chip FLASH memory.
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

#include <string.h>
#include "device.h"
#include "plib_sefc_common.h"
#include "plib_sefc0.h"
#include "plib_sefc1.h"

__longramfunc__ uint32_t SEFC_GpnvmBitRead(void)
{
    return SEFC0_GpnvmBitRead();
}

__longramfunc__ void SEFC_GpnvmBitSet(uint8_t GpnvmBitNumber)
{
    SEFC0_GpnvmBitSet(GpnvmBitNumber);
}

__longramfunc__ void SEFC_GpnvmBitClear(uint8_t GpnvmBitNumber)
{
    SEFC0_GpnvmBitClear(GpnvmBitNumber);
}

SEFC_FLASH_PANEL SEFC_FlashPanelGet(uint32_t address)
{
    bool isPanelSwap = ((SEFC_GpnvmBitRead() & FUSES_GPNVMBITS_PLANE_SELECTION_Msk) == FUSES_GPNVMBITS_PLANE_SELECTION_Msk) ? true: false;

    if (address < IFLASH1_ADDR)
    {
        return isPanelSwap == false? SEFC_FLASH_PANEL0 : SEFC_FLASH_PANEL1;
    }
    else
    {
        return isPanelSwap == false? SEFC_FLASH_PANEL1 : SEFC_FLASH_PANEL0;
    }
}

void SEFC_BankSwap(void)
{
    bool isPanelSwap = ((SEFC_GpnvmBitRead() & FUSES_GPNVMBITS_PLANE_SELECTION_Msk) == FUSES_GPNVMBITS_PLANE_SELECTION_Msk);
    isPanelSwap == true ? SEFC_GpnvmBitClear(FUSES_GPNVMBITS_PLANE_SELECTION_Pos) : SEFC_GpnvmBitSet(FUSES_GPNVMBITS_PLANE_SELECTION_Pos);
}

bool SEFC_SectorErase( uint32_t address )
{
    SEFC_FLASH_PANEL flash_panel = SEFC_FlashPanelGet(address);

    return (flash_panel == SEFC_FLASH_PANEL0)? SEFC0_SectorErase(address) : SEFC1_SectorErase(address);
}

bool SEFC_PageErase( uint32_t address )
{
    SEFC_FLASH_PANEL flash_panel = SEFC_FlashPanelGet(address);

    return (flash_panel == SEFC_FLASH_PANEL0)? SEFC0_PageErase(address) : SEFC1_PageErase(address);
}

bool SEFC_PageBufferWrite( uint32_t *data, const uint32_t address)
{
    SEFC_FLASH_PANEL flash_panel = SEFC_FlashPanelGet(address);

    return (flash_panel == SEFC_FLASH_PANEL0)? SEFC0_PageBufferWrite(data, address) : SEFC1_PageBufferWrite(data, address);
}

bool SEFC_PageBufferCommit( const uint32_t address)
{
    SEFC_FLASH_PANEL flash_panel = SEFC_FlashPanelGet(address);

    return (flash_panel == SEFC_FLASH_PANEL0)? SEFC0_PageBufferCommit(address) : SEFC1_PageBufferCommit(address);
}

bool SEFC_PageWrite( uint32_t *data, uint32_t address )
{
    SEFC_FLASH_PANEL flash_panel = SEFC_FlashPanelGet(address);

    return (flash_panel == SEFC_FLASH_PANEL0)? SEFC0_PageWrite(data, address) : SEFC1_PageWrite(data, address);
}

bool SEFC_QuadWordWrite( uint32_t *data, uint32_t address )
{
    SEFC_FLASH_PANEL flash_panel = SEFC_FlashPanelGet(address);

    return (flash_panel == SEFC_FLASH_PANEL0)? SEFC0_QuadWordWrite(data, address) : SEFC1_QuadWordWrite(data, address);
}

void SEFC_RegionLock(uint32_t address)
{
    SEFC_FLASH_PANEL flash_panel = SEFC_FlashPanelGet(address);

    return (flash_panel == SEFC_FLASH_PANEL0)? SEFC0_RegionLock(address) : SEFC1_RegionLock(address);
}

void SEFC_RegionUnlock(uint32_t address)
{
    SEFC_FLASH_PANEL flash_panel = SEFC_FlashPanelGet(address);

    return (flash_panel == SEFC_FLASH_PANEL0)? SEFC0_RegionUnlock(address) : SEFC1_RegionUnlock(address);
}

bool SEFC_IsBusy(uint32_t address)
{
    SEFC_FLASH_PANEL flash_panel = SEFC_FlashPanelGet(address);

    return (flash_panel == SEFC_FLASH_PANEL0)? SEFC0_IsBusy() : SEFC1_IsBusy();
}

SEFC_ERROR SEFC_ErrorGet(uint32_t address)
{
    SEFC_FLASH_PANEL flash_panel = SEFC_FlashPanelGet(address);

    return (flash_panel == SEFC_FLASH_PANEL0)? SEFC0_ErrorGet() : SEFC1_ErrorGet();
}
