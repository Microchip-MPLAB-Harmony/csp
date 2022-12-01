/*******************************************************************************
  FLEXCOM SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_flexcom_spi_master_common.h

  Summary:
   FLEXCOM SPI Master PLIB Common Header File.

  Description:
    This file has prototype of all the interfaces which are common for all the
    FLEXCOM SPI peripherals.

  Remarks:
    None.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#ifndef PLIB_FLEXCOM_SPI_MASTER_COMMON_H  // Guards against multiple inclusion
#define PLIB_FLEXCOM_SPI_MASTER_COMMON_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

extern "C" {

#endif

// DOM-IGNORE-END
/****************************** ${FLEXCOM_INSTANCE_NAME} SPI Interface *********************************/

typedef enum
{
    FLEXCOM_SPI_CLOCK_PHASE_TRAILING_EDGE = 0 << FLEX_SPI_CSR_NCPHA_Pos,
    FLEXCOM_SPI_CLOCK_PHASE_LEADING_EDGE = 1 << FLEX_SPI_CSR_NCPHA_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    FLEXCOM_SPI_CLOCK_PHASE_INVALID = 0xFFFFFFFF

}FLEXCOM_SPI_CLOCK_PHASE;

typedef enum
{
    FLEXCOM_SPI_CLOCK_POLARITY_IDLE_LOW = 0 << FLEX_SPI_CSR_CPOL_Pos,
    FLEXCOM_SPI_CLOCK_POLARITY_IDLE_HIGH = 1 << FLEX_SPI_CSR_CPOL_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    FLEXCOM_SPI_CLOCK_POLARITY_INVALID = 0xFFFFFFFF

}FLEXCOM_SPI_CLOCK_POLARITY;

typedef enum
{
    FLEXCOM_SPI_CHIP_SELECT_NPCS0 = ${FLEXCOM_SPI_MR_PCS_NPCS0},
<#if FLEXCOM_SPI_EN_NPCS1?? >
    FLEXCOM_SPI_CHIP_SELECT_NPCS1 = ${FLEXCOM_SPI_MR_PCS_NPCS1},
</#if>
<#if FLEXCOM_SPI_EN_NPCS2?? >
	FLEXCOM_SPI_CHIP_SELECT_NPCS2 = ${FLEXCOM_SPI_MR_PCS_NPCS2},
</#if>
<#if FLEXCOM_SPI_EN_NPCS3?? >
	FLEXCOM_SPI_CHIP_SELECT_NPCS3 = ${FLEXCOM_SPI_MR_PCS_NPCS3},
</#if>
}FLEXCOM_SPI_CHIP_SELECT;

typedef enum
{
    FLEXCOM_SPI_DATA_BITS_8 = FLEX_SPI_CSR_BITS_8_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_9 = FLEX_SPI_CSR_BITS_9_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_10 = FLEX_SPI_CSR_BITS_10_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_11 = FLEX_SPI_CSR_BITS_11_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_12 = FLEX_SPI_CSR_BITS_12_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_13 = FLEX_SPI_CSR_BITS_13_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_14 = FLEX_SPI_CSR_BITS_14_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_15 = FLEX_SPI_CSR_BITS_15_BIT_Val << FLEX_SPI_CSR_BITS_Pos,
    FLEXCOM_SPI_DATA_BITS_16 = FLEX_SPI_CSR_BITS_16_BIT_Val << FLEX_SPI_CSR_BITS_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    FLEXCOM_SPI_DATA_BITS_INVALID = 0xFFFFFFFF

}FLEXCOM_SPI_DATA_BITS;

typedef struct
{
    uint32_t    clockFrequency;
    FLEXCOM_SPI_CLOCK_PHASE clockPhase;
    FLEXCOM_SPI_CLOCK_POLARITY clockPolarity;
    FLEXCOM_SPI_DATA_BITS   dataBits;

}FLEXCOM_SPI_TRANSFER_SETUP;

typedef  void (*FLEXCOM_SPI_CALLBACK) (uintptr_t context);

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
    FLEXCOM_SPI_CALLBACK    callback;
    uintptr_t               context;
    uint32_t                status;
    /* Number of bytes transferred */
    size_t                  nBytesTransferred;

} FLEXCOM_SPI_OBJECT ;

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif /* PLIB_FLEXCOM_SPI_MASTER_COMMON_H */

/*******************************************************************************
 End of File
*/