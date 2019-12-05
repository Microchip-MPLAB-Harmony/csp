/*******************************************************************************
  OTP Memory controller (OTPC) PLIB

  Company
    Microchip Technology Inc.

  File Name
    plib_otpc.h

  Summary
    OTPC PLIB Header File.

  Description
    This file defines the interface to the OTPC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.
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

#ifndef PLIB_OTPC_H  // Guards against multiple inclusion
#define PLIB_OTPC_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stdbool.h>
#include <stddef.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *

typedef enum {
	OTP_PCKT_REGULAR,
	OTP_PCKT_KEY,
	OTP_PCKT_BOOT_CONFIGURATION,
	OTP_PCKT_SECURE_BOOT_CONFIGURATION,
	OTP_PCKT_HARDWARE_CONFIGURATION,
	OTP_PCKT_CUSTOM,

	OTP_PCKT_MAX_TYPE
}OTPC_PACKET_TYPE;

typedef struct {
	OTPC_PACKET_TYPE   type;
	uint32_t                size; 
}OTPC_NEW_PACKET;

typedef enum
{
    /* definitions of error code */
    OTPC_NO_ERROR                           =    0x00,
    OTPC_ERROR_HW_WRITE_DISABLED            =    0x01,
    OTPC_ERROR_PACKET_OVERLAPPED            =    0x02,
    OTPC_ERROR_CANNOT_ACTIVATE_EMULATION    =    0x03,
    OTPC_ERROR_PACKET_NOT_FOUND             =    0x04,
    OTPC_ERROR_BUFFER_OVERFLOW              =    0x05,
    OTPC_ERROR_PACKET_INVALIDATED           =    0x06,
    OTPC_CANNOT_START_PROGRAMMING           =    0x09,
    OTPC_CANNOT_START_READING               =    0x0A,
    OTPC_PACKET_TOO_BIG                     =    0x0B,
    OTPC_FLUSHING_DID_NOT_END               =    0x0C,
    OTPC_READING_DID_NOT_START              =    0x0D,
    OTPC_READING_DID_NOT_STOP               =    0x0E,
    OTPC_CANNOT_LOCK                        =    0x0F,
    OTPC_CANNOT_INVALIDATE                  =    0x10,
    OTPC_CANNOT_REFRESH                     =    0x11,
    OTPC_CANNOT_TRANSFER_KEY                =    0x12,
    OTPC_CANNOT_START_HIDING                =    0x13,
    OTPC_CANNOT_PERFORM_HIDING              =    0x14,
    OTPC_ERROR_PACKET_IS_INVALID            =    0x15,
    OTPC_ERROR_BAD_HEADER                   =    0x16
}otpc_error_code_t;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void OTPC_Initialize( void );

otpc_error_code_t OTPC_WritePacket(const OTPC_NEW_PACKET *packet,
                         const uint32_t *payload,
                         uint16_t *headerAddress,
                         uint16_t *sizeWritten);

otpc_error_code_t OTPC_UpdatePayload(uint16_t headerAddress, const uint32_t * payload);

otpc_error_code_t OTPC_ReadPacket( uint16_t headerAddress,
                                          uint32_t *readBuffer,
                                          uint16_t bufferSize,
                                          uint16_t *sizeRead);

otpc_error_code_t OTPC_LockPacket(uint16_t headerAddress);

otpc_error_code_t OTPC_InvalidatePacket(uint16_t headerAddress);

otpc_error_code_t OTPC_HidePacket(uint16_t headerAddress);

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility

    }

#endif
// DOM-IGNORE-END

#endif /* PLIB_OTPC_H */