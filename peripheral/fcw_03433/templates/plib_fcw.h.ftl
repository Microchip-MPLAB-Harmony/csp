/*******************************************************************************
  Non-Volatile Memory Controller(${FCW_INSTANCE_NAME}) PLIB.

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FCW_INSTANCE_NAME?lower_case}.h

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

#ifndef PLIB_${FCW_INSTANCE_NAME}_H
#define PLIB_${FCW_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"     // For device registers and uint32_t
#include <stdbool.h>    // For bool

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif

// DOM-IGNORE-END

#define ${FCW_INSTANCE_NAME}_FLASH_START_ADDRESS    (${.vars["FLASH_START_ADDRESS"]}U)
#define ${FCW_INSTANCE_NAME}_FLASH_ROWSIZE          (${FLASH_PROGRAM_SIZE}U)
#define ${FCW_INSTANCE_NAME}_FLASH_PAGESIZE         (${FLASH_ERASE_SIZE}U)

<#if DRV_MEMORY_CONNECTED == true>
    <#lt>#define ${FCW_INSTANCE_NAME}_START_ADDRESS              (0x${START_ADDRESS}U)
    <#lt>#define ${FCW_INSTANCE_NAME}_MEDIA_SIZE                 (${MEMORY_MEDIA_SIZE}U)
    <#lt>#define ${FCW_INSTANCE_NAME}_ERASE_BUFFER_SIZE          (${ERASE_BUFFER_SIZE}U)
</#if>


 /* Bank/Panel 1 */
#define    PROGRAM_FLASH_BANK_1    (0U)

/* Bank/Panel 2 */
#define    PROGRAM_FLASH_BANK_2    (1U)

typedef uint32_t PROGRAM_FLASH_BANK;

    /* Boot Flash Page 0 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_0     (0

    /* Boot Flash Page 1 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_1     (1)

    /* Boot Flash Page 2 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_2     (2)

    /* Boot Flash Page 3 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_3     (3)

    /* Boot Flash Page 4 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_4     (4)

    /* Boot Flash Page 5 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_5     (5)

    /* Boot Flash Page 6 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_6     (6)

    /* Boot Flash Page 7 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_7     (7)

    /* Boot Flash Page 8 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_8     (8)

    /* Boot Flash Page 9 Write Protect */
#define   FCW_BOOT_WRITE_PROTECT_PAGE_9      (9)

    /* Boot Flash Page 10 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_10    (10)

    /* Boot Flash Page 11 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_11    (11)

    /* Boot Flash Page 12 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_12    (12)

    /* Boot Flash Page 13 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_13    (13)

    /* Boot Flash Page 14 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_14    (14)

    /* Boot Flash Page15 Write Protect */
#define    FCW_BOOT_WRITE_PROTECT_PAGE_15    (15)

typedef uint32_t FCW_BOOT_FLASH_WRITE_PROTECT;


/* No error */
#define    FCW_ERROR_NONE                  (0x0U)

/* FCW key error */
#define     FCW_ERROR_KEY                  (FCW_INTFLAG_KEYERR_Msk)

/* FCW configuration error */
#define     FCW_ERROR_CONFIGURATION        (FCW_INTFLAG_CFGERR_Msk)

/* FCW FIFO underrun error */    
#define     FCW_ERROR_FIFO_UNDERRUN        (FCW_INTFLAG_FIFOERR_Msk)

/* FCW AHB bus error */    
#define     FCW_ERROR_BUS_AHB              (FCW_INTFLAG_BUSERR_Msk)

/* FCW write protection error */    
#define     FCW_ERROR_WRITE_PROTECTION     (FCW_INTFLAG_WPERR_Msk)

/* FCW operation error */    
#define     FCW_ERROR_OPERATION            (FCW_INTFLAG_OPERR_Msk)

/* FCW security violation error */    
#define     FCW_ERROR_SECURITY_VIOLATION   (FCW_INTFLAG_SECERR_Msk)

/* FCW High Temperature detect error */    
#define     FCW_ERROR_HIGH_TEMP_DETECT     (FCW_INTFLAG_HTDPGM_Msk)

/* FCW Reset or Brown out detect error */    
#define     FCW_ERROR_RESET                (FCW_INTFLAG_BORERR_Msk)

/* FCW write error */
#define     FCW_ERROR_WRITE                (FCW_INTFLAG_WRERR_Msk)

typedef uint32_t FCW_ERROR;



typedef enum
{
    /* Bank/Panel 1 */
    BOOT_FLASH_BANK_1,

    /* Bank/Panel 2 */
    BOOT_FLASH_BANK_2

}BOOT_FLASH_BANK;
typedef enum{
    PFM_WP_REGION_0,
    PFM_WP_REGION_1,
    PFM_WP_REGION_2,
    PFM_WP_REGION_3,
    PFM_WP_REGION_4,
    PFM_WP_REGION_5,
    PFM_WP_REGION_6,
    PFM_WP_REGION_7,
}PFM_WP_REGION;

typedef struct
{
    uint32_t    regionBaseAddress;
    bool        mirrorEnable;
    uint32_t    regionSize;
}PFM_WP_REGION_SETUP; 


<#if INTERRUPT_ENABLE == true>
    <#lt>typedef void (*FCW_CALLBACK)( uintptr_t context );
</#if>

void ${FCW_INSTANCE_NAME}_Initialize( void );

bool ${FCW_INSTANCE_NAME}_Read( uint32_t *data, uint32_t length, const uint32_t address );

bool ${FCW_INSTANCE_NAME}_SingleDoubleWordWrite( uint32_t *data, uint32_t address );

bool ${FCW_INSTANCE_NAME}_QuadDoubleWordWrite( uint32_t *data, uint32_t address );

bool ${FCW_INSTANCE_NAME}_RowWrite( uint32_t *data, uint32_t address );

bool ${FCW_INSTANCE_NAME}_PageErase( uint32_t address );

FCW_ERROR ${FCW_INSTANCE_NAME}_ErrorGet( void );

bool ${FCW_INSTANCE_NAME}_IsBusy( void );

void ${FCW_INSTANCE_NAME}_ProgramFlashBankSelect( PROGRAM_FLASH_BANK pfmBank );

PROGRAM_FLASH_BANK ${FCW_INSTANCE_NAME}_ProgramFlashBankGet(void);

void ${FCW_INSTANCE_NAME}_PFM_WriteProtectRegionSetup( PFM_WP_REGION region, PFM_WP_REGION_SETUP setupStruct );

void ${FCW_INSTANCE_NAME}_PFM_WriteProtectEnable(PFM_WP_REGION region);

void ${FCW_INSTANCE_NAME}_PFM_WriteProtectDisable(PFM_WP_REGION region);

void ${FCW_INSTANCE_NAME}_PFM_WriteProtectLock(PFM_WP_REGION region);

void ${FCW_INSTANCE_NAME}_BootFlashWriteProtectEnable( BOOT_FLASH_BANK bootBank, FCW_BOOT_FLASH_WRITE_PROTECT writeProtectPage );

void ${FCW_INSTANCE_NAME}_BootFlashWriteProtectDisable(BOOT_FLASH_BANK bootBank, FCW_BOOT_FLASH_WRITE_PROTECT writeProtectPage );

void ${FCW_INSTANCE_NAME}_BootFlashWriteProtectLock( BOOT_FLASH_BANK bootBank );

<#if INTERRUPT_ENABLE == true>
    <#lt>void ${FCW_INSTANCE_NAME}_CallbackRegister( FCW_CALLBACK callback, uintptr_t context );
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif

// DOM-IGNORE-END
#endif // PLIB_${FCW_INSTANCE_NAME}_H
