/*******************************************************************************
  MCSPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_mcspi_master_common.h

  Summary:
    MCSPI PLIB Master Common Header File

  Description:
    This file has prototype of all the interfaces which are common for all the
    MCSPI peripherals.

*******************************************************************************/

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

#ifndef PLIB_MCSPI_MASTER_COMMON_H
#define PLIB_MCSPI_MASTER_COMMON_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>


/* Provide C++ Compatibility */
#ifdef __cplusplus

    extern "C" {

#endif

typedef enum
{
    MCSPI_CLOCK_PHASE_TRAILING_EDGE = 0 << MCSPI_CSR_NCPHA_Pos,
    MCSPI_CLOCK_PHASE_LEADING_EDGE = 1 << MCSPI_CSR_NCPHA_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    MCSPI_CLOCK_PHASE_INVALID = 0xFFFFFFFF

}MCSPI_CLOCK_PHASE;

typedef enum
{
    MCSPI_CLOCK_POLARITY_IDLE_LOW = 0 << MCSPI_CSR_CPOL_Pos,
    MCSPI_CLOCK_POLARITY_IDLE_HIGH = 1 << MCSPI_CSR_CPOL_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    MCSPI_CLOCK_POLARITY_INVALID = 0xFFFFFFFF

}MCSPI_CLOCK_POLARITY;

typedef enum
{
    MCSPI_DATA_BITS_8 = MCSPI_CSR_BITS_8_BIT_Val << MCSPI_CSR_BITS_Pos,
    MCSPI_DATA_BITS_9 = MCSPI_CSR_BITS_9_BIT_Val << MCSPI_CSR_BITS_Pos,
    MCSPI_DATA_BITS_10 = MCSPI_CSR_BITS_10_BIT_Val << MCSPI_CSR_BITS_Pos,
    MCSPI_DATA_BITS_11 = MCSPI_CSR_BITS_11_BIT_Val << MCSPI_CSR_BITS_Pos,
    MCSPI_DATA_BITS_12 = MCSPI_CSR_BITS_12_BIT_Val << MCSPI_CSR_BITS_Pos,
    MCSPI_DATA_BITS_13 = MCSPI_CSR_BITS_13_BIT_Val << MCSPI_CSR_BITS_Pos,
    MCSPI_DATA_BITS_14 = MCSPI_CSR_BITS_14_BIT_Val << MCSPI_CSR_BITS_Pos,
    MCSPI_DATA_BITS_15 = MCSPI_CSR_BITS_15_BIT_Val << MCSPI_CSR_BITS_Pos,
    MCSPI_DATA_BITS_16 = MCSPI_CSR_BITS_16_BIT_Val << MCSPI_CSR_BITS_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    MCSPI_DATA_BITS_INVALID = 0xFFFFFFFF

}MCSPI_DATA_BITS;

typedef enum
{
    MCSPI_CHIP_SELECT_NPCS0 = ${MCSPI_MR_PCS_NPCS0},
<#if MCSPI_EN_NPCS1?? >
    MCSPI_CHIP_SELECT_NPCS1 = ${MCSPI_MR_PCS_NPCS1},
</#if>
<#if MCSPI_EN_NPCS2?? >
    MCSPI_CHIP_SELECT_NPCS2 = ${MCSPI_MR_PCS_NPCS2},
</#if>
<#if MCSPI_EN_NPCS3?? >
    MCSPI_CHIP_SELECT_NPCS3 = ${MCSPI_MR_PCS_NPCS3},
</#if>

}MCSPI_CHIP_SELECT;

typedef struct
{
    uint32_t    clockFrequency;
    MCSPI_CLOCK_PHASE clockPhase;
    MCSPI_CLOCK_POLARITY clockPolarity;
    MCSPI_DATA_BITS   dataBits;

}MCSPI_TRANSFER_SETUP;

typedef  void (*MCSPI_CALLBACK) (uintptr_t context);

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

typedef struct
{
    void*                   txBuffer;
    void*                   rxBuffer;
    size_t                  txSize;
    size_t                  rxSize;
    size_t                  dummySize;
    size_t                  rxCount;
    size_t                  txCount;
    bool                    transferIsBusy;
    MCSPI_CALLBACK            callback;
    uintptr_t               context;
    /* Number of bytes transferred */
    size_t                  nBytesTransferred;
} MCSPI_OBJECT ;

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }

#endif

#endif // PLIB_MCSPI_MASTER_COMMON_H

/*******************************************************************************
 End of File
*/