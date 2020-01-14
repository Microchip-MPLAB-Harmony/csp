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

/*******************************************************************************
  Main Source File

  Company:
    Microchip Technology Inc.

  File Name:
    main.c

  Summary:
    This file contains the "main" function for a project.

  Description:
    This file contains the "main" function for a project.  The
    "main" function calls the "SYS_Initialize" function to initialize the state
    machines of all modules in the system
 *******************************************************************************/

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include <string.h>
#include "definitions.h"                // SYS function prototypes

#define EEPROM_PAGE_SIZE_BYTES                  256
#define EEPROM_PAGE_SIZE_MASK                   0xFF
#define EEPROM_SIZE_BYTES                       512

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
typedef enum
{
    EEPROM_CMD_WRITE,
    EEPROM_CMD_IDLE,
}EEPROM_CMD;

typedef struct
{
    /* currentAddrPtr - to allow for sequential read (from the current address) */
    uint16_t                    currentAddrPtr;
    /* addrIndex - used to copy 2 bytes of EEPROM memory address */
    uint8_t                     addrIndex;
    /* wrBuffer - holds the incoming data from the I2C master */
    uint8_t                     wrBuffer[EEPROM_PAGE_SIZE_BYTES];
    /* wrBufferIndex - Index into the wrBuffer[] */
    uint16_t                    wrBufferIndex;
    /* wrAddr - indicates the starting address of the EEPROM emulation memory to write to */
    volatile uint16_t           wrAddr;
    /* nWrBytes - indicates the number of bytes to write to EEPROM emulation buffer */
    volatile uint8_t            nWrBytes;
    /* internalWriteInProgress - indicates that EEPROM is busy with internal writes */
    bool                        internalWriteInProgress;
    /* eepromCommand - used to trigger write to the EEPROM emulation buffer */
    EEPROM_CMD                  eepromCommand;
}EEPROM_DATA;

EEPROM_DATA         eepromData;

uint8_t EEPROM_EmulationBuffer[EEPROM_SIZE_BYTES] =
{
    0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f,
    0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a,0x1b,0x1c,0x1d,0x1e,0x1f,
    0x20,0x21,0x22,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x2a,0x2b,0x2c,0x2d,0x2e,0x2f,
    0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x3a,0x3b,0x3c,0x3d,0x3e,0x3f,
    0x40,0x41,0x42,0x43,0x44,0x45,0x46,0x47,0x48,0x49,0x4a,0x4b,0x4c,0x4d,0x4e,0x4f,
    0x50,0x51,0x52,0x53,0x54,0x55,0x56,0x57,0x58,0x59,0x5a,0x5b,0x5c,0x5d,0x5e,0x5f,
    0x60,0x61,0x62,0x63,0x64,0x65,0x66,0x67,0x68,0x69,0x6a,0x6b,0x6c,0x6d,0x6e,0x6f,
    0x70,0x71,0x72,0x73,0x74,0x75,0x76,0x77,0x78,0x79,0x7a,0x7b,0x7c,0x7d,0x7e,0x7f,
    0x80,0x81,0x82,0x83,0x84,0x85,0x86,0x87,0x88,0x89,0x8a,0x8b,0x8c,0x8d,0x8e,0x8f,
    0x90,0x91,0x92,0x93,0x94,0x95,0x96,0x97,0x98,0x99,0x9a,0x9b,0x9c,0x9d,0x9e,0x9f,
    0xa0,0xa1,0xa2,0xa3,0xa4,0xa5,0xa6,0xa7,0xa8,0xa9,0xaa,0xab,0xac,0xad,0xae,0xaf,
    0xb0,0xb1,0xb2,0xb3,0xb4,0xb5,0xb6,0xb7,0xb8,0xb9,0xba,0xbb,0xbc,0xbd,0xbe,0xbf,
    0xc0,0xc1,0xc2,0xc3,0xc4,0xc5,0xc6,0xc7,0xc8,0xc9,0xca,0xcb,0xcc,0xcd,0xce,0xcf,
    0xd0,0xd1,0xd2,0xd3,0xd4,0xd5,0xd6,0xd7,0xd8,0xd9,0xda,0xdb,0xdc,0xdd,0xde,0xdf,
    0xe0,0xe1,0xe2,0xe3,0xe4,0xe5,0xe6,0xe7,0xe8,0xe9,0xea,0xeb,0xec,0xed,0xee,0xef,
    0xf0,0xf1,0xf2,0xf3,0xf4,0xf5,0xf6,0xf7,0xf8,0xf9,0xfa,0xfb,0xfc,0xfd,0xfe,0xff,

    0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0a,0x0b,0x0c,0x0d,0x0e,0x0f,
    0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,0x1a,0x1b,0x1c,0x1d,0x1e,0x1f,
    0x20,0x21,0x22,0x23,0x24,0x25,0x26,0x27,0x28,0x29,0x2a,0x2b,0x2c,0x2d,0x2e,0x2f,
    0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x3a,0x3b,0x3c,0x3d,0x3e,0x3f,
    0x40,0x41,0x42,0x43,0x44,0x45,0x46,0x47,0x48,0x49,0x4a,0x4b,0x4c,0x4d,0x4e,0x4f,
    0x50,0x51,0x52,0x53,0x54,0x55,0x56,0x57,0x58,0x59,0x5a,0x5b,0x5c,0x5d,0x5e,0x5f,
    0x60,0x61,0x62,0x63,0x64,0x65,0x66,0x67,0x68,0x69,0x6a,0x6b,0x6c,0x6d,0x6e,0x6f,
    0x70,0x71,0x72,0x73,0x74,0x75,0x76,0x77,0x78,0x79,0x7a,0x7b,0x7c,0x7d,0x7e,0x7f,
    0x80,0x81,0x82,0x83,0x84,0x85,0x86,0x87,0x88,0x89,0x8a,0x8b,0x8c,0x8d,0x8e,0x8f,
    0x90,0x91,0x92,0x93,0x94,0x95,0x96,0x97,0x98,0x99,0x9a,0x9b,0x9c,0x9d,0x9e,0x9f,
    0xa0,0xa1,0xa2,0xa3,0xa4,0xa5,0xa6,0xa7,0xa8,0xa9,0xaa,0xab,0xac,0xad,0xae,0xaf,
    0xb0,0xb1,0xb2,0xb3,0xb4,0xb5,0xb6,0xb7,0xb8,0xb9,0xba,0xbb,0xbc,0xbd,0xbe,0xbf,
    0xc0,0xc1,0xc2,0xc3,0xc4,0xc5,0xc6,0xc7,0xc8,0xc9,0xca,0xcb,0xcc,0xcd,0xce,0xcf,
    0xd0,0xd1,0xd2,0xd3,0xd4,0xd5,0xd6,0xd7,0xd8,0xd9,0xda,0xdb,0xdc,0xdd,0xde,0xdf,
    0xe0,0xe1,0xe2,0xe3,0xe4,0xe5,0xe6,0xe7,0xe8,0xe9,0xea,0xeb,0xec,0xed,0xee,0xef,
    0xf0,0xf1,0xf2,0xf3,0xf4,0xf5,0xf6,0xf7,0xf8,0xf9,0xfa,0xfb,0xfc,0xfd,0xfe,0xff
};

bool APP_SERCOM_I2C_Callback ( SERCOM_I2C_SLAVE_TRANSFER_EVENT event, uintptr_t contextHandle )
{
    bool isSuccess = true;

    switch(event)
    {
        case SERCOM_I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH:
            if ((SERCOM3_I2C_TransferDirGet() == SERCOM_I2C_SLAVE_TRANSFER_DIR_WRITE) && (eepromData.internalWriteInProgress == true))
            {
                /* EEPROM is busy. Send NAK */
                isSuccess = false;
            }
            else
            {
                /* Reset the indexes */
                eepromData.addrIndex = 0;
                eepromData.wrBufferIndex = 0;
            }
            break;

        case SERCOM_I2C_SLAVE_TRANSFER_EVENT_RX_READY:
            /* Read the data sent by I2C Master */
            if (eepromData.addrIndex < 2)
            {
                ((uint8_t*)&eepromData.currentAddrPtr)[eepromData.addrIndex++] = SERCOM3_I2C_ReadByte();
            }
            else
            {
                eepromData.wrBuffer[(eepromData.wrBufferIndex & EEPROM_PAGE_SIZE_MASK)] = SERCOM3_I2C_ReadByte();
                eepromData.wrBufferIndex++;
            }
            break;

        case SERCOM_I2C_SLAVE_TRANSFER_EVENT_TX_READY:
            /* Provide the EEPROM data requested by the I2C Master */
            SERCOM3_I2C_WriteByte(EEPROM_EmulationBuffer[eepromData.currentAddrPtr++]);
            if (eepromData.currentAddrPtr >= EEPROM_SIZE_BYTES)
            {
                eepromData.currentAddrPtr = 0;
            }
            break;

        case SERCOM_I2C_SLAVE_TRANSFER_EVENT_STOP_BIT_RECEIVED:
            if (eepromData.wrBufferIndex > 0)
            {
                if (eepromData.wrBufferIndex > EEPROM_PAGE_SIZE_BYTES)
                {
                    eepromData.wrBufferIndex = EEPROM_PAGE_SIZE_BYTES;
                }
                eepromData.wrAddr = eepromData.currentAddrPtr;
                eepromData.nWrBytes = eepromData.wrBufferIndex;

                /* Update the current address pointer to allow for sequential read */
                eepromData.currentAddrPtr += eepromData.wrBufferIndex;

                /* Reset the indexes */
                eepromData.addrIndex = 0;
                eepromData.wrBufferIndex = 0;

                /* Set busy flag to send NAK for any write requests */
                eepromData.internalWriteInProgress = true;
                eepromData.eepromCommand = EEPROM_CMD_WRITE;
            }
            break;
        default:
            break;
    }

    return isSuccess;
}

void EEPROM_StateMachine(void)
{
    switch(eepromData.eepromCommand)
    {
        case EEPROM_CMD_WRITE:
            memcpy(&EEPROM_EmulationBuffer[eepromData.wrAddr], &eepromData.wrBuffer[0], eepromData.nWrBytes);
            eepromData.internalWriteInProgress = false;
            eepromData.eepromCommand = EEPROM_CMD_IDLE;
            break;
        case EEPROM_CMD_IDLE:
            /* Do Nothing */
            break;
    }
}

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    eepromData.eepromCommand = EEPROM_CMD_IDLE;

    SERCOM3_I2C_CallbackRegister(APP_SERCOM_I2C_Callback, 0);

    while ( true )
    {
        EEPROM_StateMachine();
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

