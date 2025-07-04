/*******************************************************************************
  Non-Volatile Memory Controller(${FCW_INSTANCE_NAME}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FCW_INSTANCE_NAME?lower_case}.c

  Summary:
    Interface definition of ${FCW_INSTANCE_NAME} Plib.

  Description:
    This file defines the interface for the ${FCW_INSTANCE_NAME} Plib.
    It allows user to Program, Erase and lock the on-chip Non Volatile Flash
    Memory.
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <string.h>
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${FCW_INSTANCE_NAME?lower_case}.h"
#include "device_cache.h"

/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 10.3 deviated 2 times.  Deviation record ID -  H3_MISRAC_2012_R_10_3_DR_1 */
<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
    <#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
    </#if>
#pragma coverity compliance block deviate:2 "MISRA C-2012 Rule 10.3" "H3_MISRAC_2012_R_10_3_DR_1"
</#if>

/* ************************************************************************** */
/* ************************************************************************** */
/* Section: File Scope or Global Data                                         */
/* ************************************************************************** */
/* ************************************************************************** */
// *****************************************************************************

/*******************************************
 * Internal operation type
 ******************************************/
typedef enum
{
    PROGRAM_ERASE_OPERATION                 = 0x7,
    PAGE_ERASE_OPERATION                    = 0x4,
    ROW_PROGRAM_OPERATION                   = 0x3,
    QUAD_WORD_PROGRAM_OPERATION             = 0x2,
    SINGLE_WORD_PROGRAM_OPERATION           = 0x1,
    NO_OPERATION                            = 0x0,
} FCW_OPERATION_MODE;

/*******************************************
 * Internal Flash Programming Unlock Keys
 ******************************************/
typedef enum
{
    FCW_UNLOCK_WRKEY = 0x91C32C01,
    FCW_UNLOCK_SWAPKEY = 0x91C32C02,
    FCW_UNLOCK_CFGKEY = 0x91C32C04
} FCW_UNLOCK_KEY;

<#if INTERRUPT_ENABLE == true>
typedef struct
{
    FCW_CALLBACK CallbackFunc;
    uintptr_t Context;
}fcwCallbackObjType;

static volatile fcwCallbackObjType ${FCW_INSTANCE_NAME?lower_case}CallbackObj;
</#if>

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Local Functions                                                   */
/* ************************************************************************** */
/* ************************************************************************** */

// *****************************************************************************
// *****************************************************************************
// Section: ${FCW_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************
void ${FCW_INSTANCE_NAME}_PFM_PageWriteProtectRestore(uint32_t* pwp_region)
{
    for (uint32_t region = 0; region < (uint32_t)FCW_PWP_REGIONS; region++)
    {
        if ((*pwp_region & ((uint32_t)1 << region)) != 0U)
        {
           ${FCW_INSTANCE_NAME}_PFM_WriteProtectEnable(region);
        }
    }
}

bool ${FCW_INSTANCE_NAME}_PFM_PageWriteProtectDisable(uint32_t pageStartAddr, uint32_t* pwp_region)
{
    uint32_t region_start_addr;
    uint32_t region_end_addr;
    bool status = false;

    *pwp_region = 0;

    if ((pageStartAddr >= FCW_FLASH_START_ADDRESS) && (pageStartAddr < (FCW_FLASH_START_ADDRESS + FCW_FLASH_PFM_SIZE)))
    {
        for (uint32_t region = 0; region < (uint32_t)FCW_PWP_REGIONS; region++)
        {
            if ((FCW_REGS->FCW_PWP[region] & FCW_PWP_PWPEN_Msk) != 0U)
            {
                region_start_addr = FCW_FLASH_START_ADDRESS;
                region_start_addr += (FCW_REGS->FCW_PWP[region] & FCW_PWP_PWPBASE_Msk >> FCW_PWP_PWPBASE_Pos) << 12U;

                region_end_addr = region_start_addr;

                region_end_addr += ((FCW_REGS->FCW_PWP[region] & FCW_PWP_PWPSIZE_Msk) + 1U) << 12U;

                if (pageStartAddr >= region_start_addr && pageStartAddr < region_end_addr)
                {
                    ${FCW_INSTANCE_NAME}_PFM_WriteProtectDisable(region);
                    status = true;
                    *pwp_region |= ((uint32_t)1 << region);
                }
            }
        }
    }

    return status;
}

<#if INTERRUPT_ENABLE == true>

    <#lt>void ${FCW_INSTANCE_NAME}_CallbackRegister( FCW_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    /* Register callback function */
    <#lt>    ${FCW_INSTANCE_NAME?lower_case}CallbackObj.CallbackFunc    = callback;
    <#lt>    ${FCW_INSTANCE_NAME?lower_case}CallbackObj.Context         = context;
    <#lt>}

    <#lt>void __attribute__((used)) ${FCW_INSTANCE_NAME}_InterruptHandler( void )
    <#lt>{
    <#lt>    uintptr_t context_var;
    <#lt>    ${FCW_INSTANCE_NAME}_REGS->FCW_INTFLAG = FCW_INTFLAG_DONE_Msk;

    <#lt>    if(${FCW_INSTANCE_NAME?lower_case}CallbackObj.CallbackFunc != NULL)
    <#lt>    {
    <#lt>        context_var = ${FCW_INSTANCE_NAME?lower_case}CallbackObj.Context;
    <#lt>        ${FCW_INSTANCE_NAME?lower_case}CallbackObj.CallbackFunc(context_var);
    <#lt>    }
    <#lt>}
</#if>

static void ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_KEY key)
{
    ${FCW_INSTANCE_NAME}_REGS->FCW_KEY = (uint32_t)key;
}

static void ${FCW_INSTANCE_NAME}_StartOperationAtAddress( uint32_t address,  FCW_OPERATION_MODE operation )
{

    ${FCW_INSTANCE_NAME}_REGS->FCW_ADDR = address;

    // Set the flash operation:
    /***************************************************************************
     * Page erase: Erases the entire page which includes the target address
     *    (ADDR) if it is not write-protected.
     * Double Word (64-bit) program: Programs the 64 bit word in DATA[0] and DATA[1]
     *    to the flash address selected by ADDR, if it is not write-protected.
     * Quad Double Word (256-bit) program: Programs the 256 bit in DATA[0]
     *    through DATA[7] to flash address selected by ADDR, if it they are
     *    not write-protected.
     * Row program: Programs the entire row from the physical address in
     *    SRCADDR to the flash address selected by ADDR if it is not
     *    write-protected
     **************************************************************************/

<#if INTERRUPT_ENABLE == true>
    ${FCW_INSTANCE_NAME}_REGS->FCW_INTENSET = FCW_INTENSET_DONE_Msk;
</#if>

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_WRKEY);
<#if FCW_PRE_PRGM_ENABLE == true>
    ${FCW_INSTANCE_NAME}_REGS->FCW_CTRLOP = FCW_CTRLOP_PREPG_Msk | (FCW_CTRLOP_NVMOP_Msk & (((uint32_t)operation) << FCW_CTRLOP_NVMOP_Pos));
<#else>
    ${FCW_INSTANCE_NAME}_REGS->FCW_CTRLOP = (FCW_CTRLOP_NVMOP_Msk & (((uint32_t)operation) << FCW_CTRLOP_NVMOP_Pos));
</#if>
}

<#if core.COVERITY_SUPPRESS_DEVIATION?? && core.COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 10.3"
    <#if core.COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic pop
    </#if>
</#if>
/* MISRAC 2012 deviation block end */

/* ************************************************************************** */
/* ************************************************************************** */
// Section: Interface Functions                                               */
/* ************************************************************************** */
/* ************************************************************************** */

void ${FCW_INSTANCE_NAME}_Initialize( void )
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_StartOperationAtAddress( ${FCW_INSTANCE_NAME}_REGS->FCW_ADDR,  NO_OPERATION );
}

bool ${FCW_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address )
{
    /* Add this as per the misra rule 11.6 */
    uint32_t *xaddress = (uint32_t *)address;
    (void) memcpy(data, xaddress, length);

    return true;
}

bool ${FCW_INSTANCE_NAME}_SingleWordWrite( uint32_t *data, uint32_t address )
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_REGS->FCW_DATA[0] = *data;
    data++;

    ${FCW_INSTANCE_NAME}_StartOperationAtAddress( address,  SINGLE_WORD_PROGRAM_OPERATION);

    return true;
}

bool ${FCW_INSTANCE_NAME}_QuadWordWrite( uint32_t *data, uint32_t address )
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_REGS->FCW_DATA[0] = *data;
    data++;
    ${FCW_INSTANCE_NAME}_REGS->FCW_DATA[1] = *data;
    data++;
    ${FCW_INSTANCE_NAME}_REGS->FCW_DATA[2] = *data;
    data++;
    ${FCW_INSTANCE_NAME}_REGS->FCW_DATA[3] = *data;
    data++;

    ${FCW_INSTANCE_NAME}_StartOperationAtAddress( address,  QUAD_WORD_PROGRAM_OPERATION);

    return true;
}

bool ${FCW_INSTANCE_NAME}_RowWrite( uint32_t *data, uint32_t address )
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

<#if core.CoreArchitecture != "CORTEX-M4" && core.CoreArchitecture != "CORTEX-M33" && core.DATA_CACHE_ENABLE?? && core.DATA_CACHE_ENABLE == true >
    if (DATA_CACHE_IS_ENABLED() != 0U)
    {
        DCACHE_CLEAN_BY_ADDR(data, (int32_t)${FCW_INSTANCE_NAME}_FLASH_ROWSIZE);
    }
</#if>

    ${FCW_INSTANCE_NAME}_REGS->FCW_SRCADDR = (uint32_t )(data);

    ${FCW_INSTANCE_NAME}_StartOperationAtAddress( address,  ROW_PROGRAM_OPERATION);

    return true;
}

bool ${FCW_INSTANCE_NAME}_PageErase( uint32_t address )
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_StartOperationAtAddress(address,  PAGE_ERASE_OPERATION);

    return true;
}

FCW_ERROR ${FCW_INSTANCE_NAME}_ErrorGet( void )
{
    return(${FCW_INSTANCE_NAME}_REGS->FCW_INTFLAG & (~FCW_INTFLAG_DONE_Msk));
}

bool ${FCW_INSTANCE_NAME}_IsBusy( void )
{
    return ((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk) != 0U);
}

void ${FCW_INSTANCE_NAME}_ProgramFlashBankSelect(PROGRAM_FLASH_BANK pfmBank)
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_SWAPKEY);

    if (pfmBank == PROGRAM_FLASH_BANK_1)
    {
        ${FCW_INSTANCE_NAME}_REGS->FCW_SWAP &= (~FCW_SWAP_PFSWAP_Msk);
    }
    else
    {
        ${FCW_INSTANCE_NAME}_REGS->FCW_SWAP |= (FCW_SWAP_PFSWAP_Msk);
    }
}

PROGRAM_FLASH_BANK ${FCW_INSTANCE_NAME}_ProgramFlashBankGet(void)
{
    return((PROGRAM_FLASH_BANK)((${FCW_INSTANCE_NAME}_REGS->FCW_SWAP & FCW_SWAP_PFSWAP_Msk) >> FCW_SWAP_PFSWAP_Pos));
}

void ${FCW_INSTANCE_NAME}_PFM_WriteProtectRegionSetup( PFM_WP_REGION region, PFM_WP_REGION_SETUP setupStruct )
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }


    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_CFGKEY);
    ${FCW_INSTANCE_NAME}_REGS->FCW_PWP[region] = (FCW_PWP_PWPBASE(setupStruct.regionBaseAddress) | \
                                                     FCW_PWP_PWPSIZE(setupStruct.regionSize) | \
                                                     FCW_PWP_PWPMIR((uint32_t)(setupStruct.mirrorEnable)));
}

void ${FCW_INSTANCE_NAME}_PFM_WriteProtectEnable(PFM_WP_REGION region)
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_CFGKEY);

    ${FCW_INSTANCE_NAME}_REGS->FCW_PWP[region] |= FCW_PWP_PWPEN_Msk;
}

void ${FCW_INSTANCE_NAME}_PFM_WriteProtectDisable(PFM_WP_REGION region)
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_CFGKEY);

    ${FCW_INSTANCE_NAME}_REGS->FCW_PWP[region] &= (~FCW_PWP_PWPEN_Msk);
}

void ${FCW_INSTANCE_NAME}_BootConfig_WriteProtectEnable(void)
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_CFGKEY);

    ${FCW_INSTANCE_NAME}_REGS->FCW_CWP |= (FCW_CWP_BC1WP_Msk | FCW_CWP_BC1AWP_Msk);
}

uint32_t ${FCW_INSTANCE_NAME}_BootConfig_WriteProtectDisable(void)
{
    uint32_t previous_val;

    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_CFGKEY);

    previous_val = ${FCW_INSTANCE_NAME}_REGS->FCW_CWP;

    ${FCW_INSTANCE_NAME}_REGS->FCW_CWP &= ~(FCW_CWP_BC1WP_Msk | FCW_CWP_BC1AWP_Msk);

    return previous_val;
}

void ${FCW_INSTANCE_NAME}_BootConfig_WriteProtectRestore(uint32_t previous_val)
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_CFGKEY);

    ${FCW_INSTANCE_NAME}_REGS->FCW_CWP = previous_val;
}

void ${FCW_INSTANCE_NAME}_PFM_WriteProtectLock(PFM_WP_REGION region)
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_CFGKEY);

    ${FCW_INSTANCE_NAME}_REGS->FCW_PWP[region] |= (FCW_PWP_PWPLOCK_Msk);
}

void ${FCW_INSTANCE_NAME}_BootFlashWriteProtectEnable( BOOT_FLASH_BANK bootBank, FCW_BOOT_FLASH_WRITE_PROTECT writeProtectPage )
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_CFGKEY);

    if (bootBank == BOOT_FLASH_BANK_1)
    {
        ${FCW_INSTANCE_NAME}_REGS->FCW_LBWP |= (uint32_t)writeProtectPage;
    }
    else
    {
        ${FCW_INSTANCE_NAME}_REGS->FCW_UBWP |= (uint32_t)writeProtectPage;
    }
}

void ${FCW_INSTANCE_NAME}_BootFlashWriteProtectDisable(BOOT_FLASH_BANK bootBank, FCW_BOOT_FLASH_WRITE_PROTECT writeProtectPage )
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_CFGKEY);

    if (bootBank == BOOT_FLASH_BANK_1)
    {
        ${FCW_INSTANCE_NAME}_REGS->FCW_LBWP &= (uint32_t)(~writeProtectPage);
    }
    else
    {
        ${FCW_INSTANCE_NAME}_REGS->FCW_UBWP &= (uint32_t)(~writeProtectPage);
    }
}

void ${FCW_INSTANCE_NAME}_BootFlashWriteProtectLock(BOOT_FLASH_BANK bootBank)
{
    while(((${FCW_INSTANCE_NAME}_REGS->FCW_STATUS & FCW_STATUS_BUSY_Msk)) != 0U)
    {
        /* Do Nothing */
    }

    ${FCW_INSTANCE_NAME}_UnlockSequence(FCW_UNLOCK_CFGKEY);

    if (bootBank == BOOT_FLASH_BANK_1)
    {
        ${FCW_INSTANCE_NAME}_REGS->FCW_LBWP |= (FCW_LBWP_LBWPLOCK_Msk);
    }
    else
    {
        ${FCW_INSTANCE_NAME}_REGS->FCW_UBWP |= (FCW_UBWP_UBWPLOCK_Msk);
    }
}