/*******************************************************************************
  SDHC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_sdhc_common.h

  Summary:
    Contains definitions common to all the instances of SDHC PLIB

  Description:
    None

*******************************************************************************/

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

#ifndef PLIB_SDHC_COMMON_H
#define PLIB_SDHC_COMMON_H

#include <stddef.h>
#include <stdbool.h>
#include <stdint.h>
#include "device.h"

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

    extern "C" {

#endif
// DOM-IGNORE-END

/* ADMA Descriptor Table Attribute Mask */
#define SDHC_DESC_TABLE_ATTR_NO_OP          (0x00U << 4U)
#define SDHC_DESC_TABLE_ATTR_RSVD           (0x01U << 4U)
#define SDHC_DESC_TABLE_ATTR_XFER_DATA      (0x02U << 4U)
#define SDHC_DESC_TABLE_ATTR_LINK_DESC      (0x03U << 4U)

#define SDHC_DESC_TABLE_ATTR_VALID          (1U << 0U)
#define SDHC_DESC_TABLE_ATTR_END            (1UL << 1U)
#define SDHC_DESC_TABLE_ATTR_INTR           (1U << 2U)

#define SDHC_CLOCK_FREQ_400_KHZ             (400000U)
#define SDHC_CLOCK_FREQ_DS_25_MHZ           (25000000U)
#define SDHC_CLOCK_FREQ_HS_50_MHZ           (50000000U)

#define SDHC_CLOCK_FREQ_HS_26_MHZ           (26000000U)
#define SDHC_CLOCK_FREQ_HS_52_MHZ           (52000000U)

 
#define SDHC_XFER_STATUS_CMD_COMPLETED      (0x01U)
#define SDHC_XFER_STATUS_DATA_COMPLETED     (0x02U)
#define SDHC_XFER_STATUS_CARD_INSERTED      (0x04U)
#define SDHC_XFER_STATUS_CARD_REMOVED       (0x08U)

typedef uint32_t SDHC_XFER_STATUS;

/* Command code to reset the SD card */
#define SDHC_CMD_GO_IDLE_STATE              (0U)

/* Command code to initialize the SD card */
#define SDHC_CMD_SEND_OP_COND               (1U)

/* Broadcast command code to get all card IDs */
#define SDHC_CMD_ALL_SEND_CID               (2U)

/* Command card to respond with its RCA tells it to go to standby state */
#define SDHC_CMD_SEND_RCA                   (3U)

/* ACMD6 sets the card's bus width between 1-bit and 4-bit only available when the card is unlocked */
#define SDHC_CMD_SET_BUS_WIDTH              (6U)

/* Command to switch functions in ext csd register in emmc */
#define SDHC_CMD_SWITCH                     (6U)

/* Select/Deselect card message sends the card to transfer state */
#define SDHC_CMD_SELECT_DESELECT_CARD       (7U)

/* This macro defined the command code to check for sector addressing */
#define SDHC_CMD_SEND_IF_COND               (8U)

/* for MMC CMD8 is used to fetch ext csd */
#define SDHC_CMD_SEND_EXT_CSD               (8U)

/* Command code to get the Card Specific Data */
#define SDHC_CMD_SEND_CSD                   (9U)

/* Command code to get the Card Information */
#define SDHC_CMD_SEND_CID                   (10U)

/* Command code to stop transmission during a multi-block read */
#define SDHC_CMD_STOP_TRANSMISSION          (12U)

/* Command code to get the card status information */
#define SDHC_CMD_SEND_STATUS                (13U)

/* Command code to set the block length of the card */
#define SDHC_CMD_SET_BLOCKLEN               (16U)

/* Command code to read one block from the card */
#define SDHC_CMD_READ_SINGLE_BLOCK          (17U)

/* Command code to read multiple blocks from the card */
#define SDHC_CMD_READ_MULTI_BLOCK           (18U)

/* Command code to tell the media how many blocks to pre-erase */
#define SDHC_CMD_SET_WR_BLK_ERASE_COUNT     (23U)

/* Command code to write one block to the card */
#define SDHC_CMD_WRITE_SINGLE_BLOCK         (24U)

/* Command code to write multiple blocks to the card */
#define SDHC_CMD_WRITE_MULTI_BLOCK          (25U)

/* Command code to set the address of the start of an erase operation */
#define SDHC_CMD_TAG_SECTOR_START           (32U)

/* Command code to set the address of the end of an erase operation */
#define SDHC_CMD_TAG_SECTOR_END             (33U)

/* Command code to erase all previously selected blocks */
#define SDHC_CMD_ERASE                      (38U)

/* Command code to initialize an SD card and provide the CSD register value */
#define SDHC_CMD_SD_SEND_OP_COND            (41U)

/* Command code to get the SCR register information from the card */
#define SDHC_CMD_READ_SCR                   (51U)

/* Command code to begin application specific command inputs */
#define SDHC_CMD_APP_CMD                    (55U)

/* Command code to get the OCR register information from the card */
#define SDHC_CMD_READ_OCR                   (58U)

/* Command code to disable CRC checking */
#define SDHC_CMD_CRC_ON_OFF                 (59U)

typedef uint32_t SDHC_SD_COMMAND;


#define  SDHC_CMD_RESP_NONE                (0U)  /*!< no response type */
#define  SDHC_CMD_RESP_R1                  (1U)  /*!< normal response command */
#define  SDHC_CMD_RESP_R1B                 (2U)  /*!< normal with busy signal */
#define  SDHC_CMD_RESP_R2                  (3U)  /*!< CID, CSD register */
#define  SDHC_CMD_RESP_R3                  (4U)  /*!< OCR register */
#define  SDHC_CMD_RESP_R4                  (5U)  /*!< */
#define  SDHC_CMD_RESP_R5                  (6U)  /*!< */
#define  SDHC_CMD_RESP_R6                  (7U)  /*!< Published RCA response  */
#define  SDHC_CMD_RESP_R7                  (8U)  /*!< Card interface condition  */

typedef uint8_t SDHC_CMD_RESP_TYPE;

typedef enum
{
    SDHC_BUS_WIDTH_1_BIT = 0,
    SDHC_BUS_WIDTH_4_BIT

} SDHC_BUS_WIDTH;

typedef enum
{
    SDHC_SPEED_MODE_NORMAL = 0,
    SDHC_SPEED_MODE_HIGH

} SDHC_SPEED_MODE;

typedef enum
{
    SDHC_READ_RESP_REG_0 = 0,
    SDHC_READ_RESP_REG_1,
    SDHC_READ_RESP_REG_2,
    SDHC_READ_RESP_REG_3,
    SDHC_READ_RESP_REG_ALL

} SDHC_READ_RESPONSE_REG;

typedef enum
{
    SDHC_RESET_ALL = 0x01,
    SDHC_RESET_CMD = 0x02,
    SDHC_RESET_DAT = 0x04

} SDHC_RESET_TYPE;

typedef enum
{
    SDHC_DIVIDED_CLK_MODE = 0,
    SDHC_PROGRAMMABLE_CLK_MODE

}SDHC_CLK_MODE;

typedef enum
{
    SDHC_DATA_TRANSFER_TYPE_SINGLE = 0,
    SDHC_DATA_TRANSFER_TYPE_MULTI,

}SDHC_DATA_TRANSFER_TYPE;

typedef enum
{
    SDHC_DATA_TRANSFER_DIR_WRITE = 0,
    SDHC_DATA_TRANSFER_DIR_READ

}SDHC_DATA_TRANSFER_DIR;

typedef struct
{
    bool                                isDataPresent;
    SDHC_DATA_TRANSFER_DIR              transferDir;
    SDHC_DATA_TRANSFER_TYPE             transferType;

}SDHC_DataTransferFlags;

typedef struct
{
    uint16_t                            attribute;
    uint16_t                            length;
    uint32_t                            address;
} SDHC_ADMA_DESCR;

typedef  void (*SDHC_CALLBACK) (SDHC_XFER_STATUS xferStatus, uintptr_t context);

typedef struct
{
    bool                                isCmdInProgress;
    bool                                isDataInProgress;
    uint16_t                            errorStatus;
    SDHC_CALLBACK                       callback;
    uintptr_t                           context;

} SDHC_OBJECT;

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility
    }
#endif

// DOM-IGNORE-END
#endif // PLIB_SDHC_COMMON_H
