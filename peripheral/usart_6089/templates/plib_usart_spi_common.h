/*******************************************************************************
  USART SPI PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_usart_spi_common.h

  Summary:
    USART SPI PLIB Common Global Header File

  Description:
    None

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

#ifndef PLIB_USART_SPI_COMMON_H
#define PLIB_USART_SPI_COMMON_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Interface
// *****************************************************************************
// *****************************************************************************

typedef enum
{
    USART_SPI_CLOCK_PHASE_TRAILING_EDGE = 0 << US_MR_SPI_CPHA_Pos,
    USART_SPI_CLOCK_PHASE_LEADING_EDGE = 1 << US_MR_SPI_CPHA_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    USART_SPI_CLOCK_PHASE_INVALID = 0xFFFFFFFF

}USART_SPI_CLOCK_PHASE;

typedef enum
{
    USART_SPI_CLOCK_POLARITY_IDLE_LOW = 0 << US_MR_SPI_CPOL_Pos,
    USART_SPI_CLOCK_POLARITY_IDLE_HIGH = 1 << US_MR_SPI_CPOL_Pos,

    /* Force the compiler to reserve 32-bit space for each enum value */
    USART_SPI_CLOCK_POLARITY_INVALID = 0xFFFFFFFF

}USART_SPI_CLOCK_POLARITY;

typedef enum
{
    USART_SPI_DATA_BITS_8 = US_MR_SPI_CHRL_8_BIT,

    /* Force the compiler to reserve 32-bit space for each enum value */
    USART_SPI_DATA_BITS_INVALID = 0xFFFFFFFF

}USART_SPI_DATA_BITS;

typedef struct
{
    uint32_t                    clockFrequency;
    USART_SPI_CLOCK_PHASE       clockPhase;
    USART_SPI_CLOCK_POLARITY    clockPolarity;
    USART_SPI_DATA_BITS         dataBits;

}USART_SPI_TRANSFER_SETUP;

typedef  void (*USART_SPI_CALLBACK) (uintptr_t context);

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
    USART_SPI_CALLBACK      callback;
    uintptr_t               context;
    /* Number of bytes transferred */
    size_t                  nBytesTransferred;
} USART_SPI_OBJECT;


// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END
#endif // PLIB_USART_SPI_COMMON_H
