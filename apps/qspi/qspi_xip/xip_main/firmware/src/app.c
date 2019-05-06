/*******************************************************************************
  Application Source File

  Company:
    Microchip Technology Inc.

  File Name:
    app.c

  Summary:
    This file contains the source code for QSPI PLIB Demonstration

  Description:
    This file contains the source code for QSPI PLIB Demonstration.
    It implements the logic of Erasing, reading and writing to QSPI Flash memory

 *******************************************************************************/

//DOM-IGNORE-BEGIN
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
//DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "app.h"
#include "xip_image_pattern_hex.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************

#define BUFFER_SIZE                sizeof(xip_image_pattern)

// *****************************************************************************
/* Application Data

  Summary:
    Holds application data

  Description:
    This structure holds the application's data.

  Remarks:
    This structure should be initialized by the APP_Initialize function.

    Application strings and buffers are be defined outside this structure.
*/

APP_DATA appData;

static uint32_t write_index = 0;

qspi_command_xfer_t qspi_command_xfer = { 0 };
qspi_register_xfer_t qspi_register_xfer = { 0 };
qspi_memory_xfer_t qspi_memory_xfer = { 0 };

uint8_t *read_memory = (uint8_t *)(QSPIMEM_ADDR | MEM_ADDRESS );

uint32_t __start_sp;
uint32_t (*__start_new)(void);
uint32_t xip_image_buffer[4];

// *****************************************************************************
// *****************************************************************************
// Section: Application Callback Functions
// *****************************************************************************
// *****************************************************************************

/* TODO:  Add any necessary callback functions.
*/

// *****************************************************************************
// *****************************************************************************
// Section: Application Local Functions
// *****************************************************************************
// *****************************************************************************

/* This function resets the flash by sending down the reset enable command
 * followed by the reset command. */

static APP_TRANSFER_STATUS APP_ResetFlash(void)
{
    memset((void *)&qspi_command_xfer, 0, sizeof(qspi_command_xfer_t));

    qspi_command_xfer.instruction = SST26_CMD_FLASH_RESET_ENABLE;
    qspi_command_xfer.width = SINGLE_BIT_SPI;

    if (QSPI_CommandWrite(&qspi_command_xfer, 0) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    qspi_command_xfer.instruction = SST26_CMD_FLASH_RESET;
    qspi_command_xfer.width = SINGLE_BIT_SPI;

    if (QSPI_CommandWrite(&qspi_command_xfer, 0) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    return APP_TRANSFER_COMPLETED;
}

/* Disables the QUAD IO on the flash */
static APP_TRANSFER_STATUS APP_DisableQuadIO(void)
{
    memset((void *)&qspi_command_xfer, 0, sizeof(qspi_command_xfer_t));

    qspi_command_xfer.instruction = SST26_CMD_RESET_QUAD_IO;
    qspi_command_xfer.width = QUAD_CMD;

    if (QSPI_CommandWrite(&qspi_command_xfer, 0) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    return APP_TRANSFER_COMPLETED;
}

/* Enables the QUAD IO on the flash */
static APP_TRANSFER_STATUS APP_EnableQuadIO(void)
{
    memset((void *)&qspi_command_xfer, 0, sizeof(qspi_command_xfer_t));

    qspi_command_xfer.instruction = SST26_CMD_ENABLE_QUAD_IO;
    qspi_command_xfer.width = SINGLE_BIT_SPI;

    if (QSPI_CommandWrite(&qspi_command_xfer, 0) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    return APP_TRANSFER_COMPLETED;
}

/* Sends Write Enable command to flash */
static APP_TRANSFER_STATUS APP_WriteEnable(void)
{
    memset((void *)&qspi_command_xfer, 0, sizeof(qspi_command_xfer_t));

    qspi_command_xfer.instruction = SST26_CMD_WRITE_ENABLE;
    qspi_command_xfer.width = QUAD_CMD;

    if (QSPI_CommandWrite(&qspi_command_xfer, 0) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    return APP_TRANSFER_COMPLETED;
}

/* This function sends down command to perform a global unprotect of the flash. */
static APP_TRANSFER_STATUS APP_UnlockFlash(void)
{
    if (APP_TRANSFER_COMPLETED != APP_WriteEnable())
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    memset((void *)&qspi_command_xfer, 0, sizeof(qspi_command_xfer_t));

    qspi_command_xfer.instruction = SST26_CMD_UNPROTECT_GLOBAL;
    qspi_command_xfer.width = QUAD_CMD;

    if (QSPI_CommandWrite(&qspi_command_xfer, 0) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    return APP_TRANSFER_COMPLETED;
}

/* This function reads and stores the flash id. */
static APP_TRANSFER_STATUS APP_ReadJedecId(uint32_t *jedec_id)
{
    memset((void *)&qspi_register_xfer, 0, sizeof(qspi_register_xfer_t));

    qspi_register_xfer.instruction = SST26_CMD_QUAD_JEDEC_ID_READ;
    qspi_register_xfer.width = QUAD_CMD;
    qspi_register_xfer.dummy_cycles = 2;

    if (QSPI_RegisterRead(&qspi_register_xfer, jedec_id, 3) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    return APP_TRANSFER_COMPLETED;
}

/* Function to read the status register of the flash. */
static APP_TRANSFER_STATUS APP_ReadStatus( uint32_t *rx_data, uint32_t rx_data_length )
{
    memset((void *)&qspi_register_xfer, 0, sizeof(qspi_register_xfer_t));

    qspi_register_xfer.instruction = SST26_CMD_READ_STATUS_REG;
    qspi_register_xfer.width = QUAD_CMD;
    qspi_register_xfer.dummy_cycles = 2;

    if (QSPI_RegisterRead(&qspi_register_xfer, rx_data, rx_data_length) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }
    return APP_TRANSFER_COMPLETED;
}

/* Function to read the configuration register of the flash. */
static APP_TRANSFER_STATUS APP_ReadConfig( uint32_t *rx_data, uint32_t rx_data_length )
{
    memset((void *)&qspi_register_xfer, 0, sizeof(qspi_register_xfer_t));

    qspi_register_xfer.instruction = SST26_CMD_READ_CONFIG_REG;
    qspi_register_xfer.width = QUAD_CMD;
    qspi_register_xfer.dummy_cycles = 2;

    if (QSPI_RegisterRead(&qspi_register_xfer, rx_data, rx_data_length) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }
    return APP_TRANSFER_COMPLETED;
}

static APP_TRANSFER_STATUS APP_GetConfig(uint16_t *config)
{
    uint8_t reg_status = 0;
    uint8_t reg_config = 0;

    if (APP_ReadStatus((uint32_t *)&reg_status, 1) != APP_TRANSFER_COMPLETED)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    if (APP_ReadConfig((uint32_t *)&reg_config, 1) != APP_TRANSFER_COMPLETED)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    *config = (reg_status | (reg_config << 8));

    return APP_TRANSFER_COMPLETED;
}

/* Function to write to configuration register of the flash. */
static APP_TRANSFER_STATUS APP_WriteConfig(uint16_t *config)
{
    if (APP_WriteEnable() != APP_TRANSFER_COMPLETED)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    memset((void *)&qspi_register_xfer, 0, sizeof(qspi_register_xfer_t));

    qspi_register_xfer.instruction = SST26_CMD_WRITE_CONFIG_REG;
    qspi_register_xfer.width = QUAD_CMD;

    if (QSPI_RegisterWrite(&qspi_register_xfer, (uint32_t *)config, 2) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }
    return APP_TRANSFER_COMPLETED;

}

/* Checks for any pending transfers Erase/Write */
static APP_TRANSFER_STATUS APP_TransferStatusCheck(void)
{
    uint8_t reg_status = 0;

    if (APP_ReadStatus((uint32_t *)&reg_status, 1) != APP_TRANSFER_COMPLETED)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    if(reg_status & (1<<0))
        return APP_TRANSFER_BUSY;
    else
        return APP_TRANSFER_COMPLETED;
}

/* Reads n Bytes of data from the flash memory */
static APP_TRANSFER_STATUS APP_MemoryRead( uint32_t *rx_data, uint32_t rx_data_length, uint32_t address )
{
    memset((void *)&qspi_memory_xfer, 0, sizeof(qspi_memory_xfer_t));

    qspi_memory_xfer.instruction = SST26_CMD_HIGH_SPEED_READ;
    qspi_memory_xfer.width = QUAD_CMD;
    qspi_memory_xfer.dummy_cycles = 6;

    if (QSPI_MemoryRead(&qspi_memory_xfer, rx_data, rx_data_length, address) == false) {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }
    return APP_TRANSFER_COMPLETED;
}

/* Reads n Bytes of data from the flash memory */
static APP_TRANSFER_STATUS APP_MemoryReadContinuous( uint32_t address )
{
    uint32_t data;
    uint16_t config = 0;

    if (APP_GetConfig(&config) != APP_TRANSFER_COMPLETED)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    config |= (SET_IOC_BIT << 8);

    if (APP_WriteConfig(&config) != APP_TRANSFER_COMPLETED)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    if (APP_DisableQuadIO() != APP_TRANSFER_COMPLETED)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    memset((void *)&qspi_memory_xfer, 0, sizeof(qspi_memory_xfer_t));

    qspi_memory_xfer.instruction = SST26_CMD_QUADIO_READ;
    qspi_memory_xfer.option = 0xA;
    qspi_memory_xfer.width = QUAD_IO;
    qspi_memory_xfer.dummy_cycles = 5;
    qspi_memory_xfer.option_en = true;
    qspi_memory_xfer.option_len = OPTL_4_BIT;
    qspi_memory_xfer.continuous_read_en = true;

    if (QSPI_MemoryRead(&qspi_memory_xfer, &data, 1, address) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }
    return APP_TRANSFER_COMPLETED;
}

/* Writes n Bytes of data to the flash memory */
static APP_TRANSFER_STATUS APP_MemoryWrite( uint32_t *tx_data, uint32_t tx_data_length, uint32_t address )
{
    if (APP_WriteEnable() != APP_TRANSFER_COMPLETED)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    memset((void *)&qspi_memory_xfer, 0, sizeof(qspi_memory_xfer_t));

    qspi_memory_xfer.instruction = SST26_CMD_PAGE_PROGRAM;
    qspi_memory_xfer.width = QUAD_CMD;

    if (QSPI_MemoryWrite(&qspi_memory_xfer, tx_data, tx_data_length, address) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    return APP_TRANSFER_COMPLETED;
}

/* Sends Erase command to flash */
static APP_TRANSFER_STATUS APP_Erase(uint8_t instruction, uint32_t address)
{
    if (APP_WriteEnable() != APP_TRANSFER_COMPLETED)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    qspi_command_xfer.instruction = instruction;
    qspi_command_xfer.width = QUAD_CMD;
    qspi_command_xfer.addr_en = 1;

    if (QSPI_CommandWrite(&qspi_command_xfer, address) == false)
    {
        return APP_TRANSFER_ERROR_UNKNOWN;
    }

    return APP_TRANSFER_COMPLETED;
}

static APP_TRANSFER_STATUS APP_BulkErase(uint32_t address)
{
    return (APP_Erase(SST26_CMD_BULK_ERASE_64K, address));
}

// *****************************************************************************
// *****************************************************************************
// Section: Application Initialization and State Machine Functions
// *****************************************************************************
// *****************************************************************************

/*******************************************************************************
  Function:
    void APP_Initialize ( void )

  Remarks:
    See prototype in app.h.
 */

void APP_Initialize ( void )
{
    /* Place the App state machine in its initial state. */
    appData.state = APP_STATE_INIT;

    LED_OFF();

    SYSTICK_TimerStart();

    SYSTICK_DelayMs(1000);
}


/******************************************************************************
  Function:
    void APP_Tasks ( void )

  Remarks:
    See prototype in app.h.
 */

void APP_Tasks ( void )
{
    uint32_t idx;

    /* Check the application's current state. */
    switch ( appData.state )
    {
        /* Application's initial state. */
        case APP_STATE_INIT:
        {
            appData.state = APP_STATE_RESET_FLASH;
        }

        case APP_STATE_RESET_FLASH:
        {
            if (APP_ResetFlash() != APP_TRANSFER_COMPLETED)
            {
                appData.state = APP_STATE_ERROR;
            }
            else
            {
                appData.state = APP_STATE_ENABLE_QUAD_IO;
            }
            break;
        }

        case APP_STATE_ENABLE_QUAD_IO:
        {
            if (APP_EnableQuadIO() != APP_TRANSFER_COMPLETED)
            {
                appData.state = APP_STATE_ERROR;
            }
            else
            {
                appData.state = APP_STATE_UNLOCK_FLASH;
            }
            break;
        }

        case APP_STATE_UNLOCK_FLASH:
        {
            if (APP_UnlockFlash() != APP_TRANSFER_COMPLETED)
            {
                appData.state = APP_STATE_ERROR;
            }
            else
            {
                appData.state = APP_STATE_READ_JEDEC_ID;
            }
            break;
        }

        case APP_STATE_READ_JEDEC_ID:
        {
            if (APP_ReadJedecId(&appData.jedec_id) != APP_TRANSFER_COMPLETED)
            {
                appData.state = APP_STATE_ERROR;
                break;
            }

            if (appData.jedec_id != SST26VF032B_JEDEC_ID)
            {
                appData.state = APP_STATE_ERROR;
                break;
            }

            appData.state = APP_STATE_ERASE_FLASH;

            break;
        }

        case APP_STATE_ERASE_FLASH:
        {
            if (APP_BulkErase(MEM_ADDRESS) != APP_TRANSFER_COMPLETED)
            {
                appData.state = APP_STATE_ERROR;
                break;
            }

            appData.state = APP_STATE_ERASE_WAIT;

            break;
        }

        case APP_STATE_ERASE_WAIT:
        {
            if (APP_TransferStatusCheck() == APP_TRANSFER_COMPLETED)
            {
                appData.state = APP_STATE_WRITE_MEMORY;
            }
            break;
        }

        case APP_STATE_WRITE_MEMORY:
        {
            if (APP_MemoryWrite((uint32_t *)&xip_image_pattern[write_index], PAGE_SIZE, (MEM_ADDRESS + write_index)) != APP_TRANSFER_COMPLETED)
            {
                appData.state = APP_STATE_ERROR;
                break;
            }

            appData.state = APP_STATE_WRITE_WAIT;

            break;
        }

        case APP_STATE_WRITE_WAIT:
        {
            if (APP_TransferStatusCheck() == APP_TRANSFER_COMPLETED)
            {
                write_index += PAGE_SIZE;
                if (write_index < BUFFER_SIZE)
                {
                    appData.state = APP_STATE_WRITE_MEMORY;
                }
                else
                {
                    appData.state = APP_STATE_READ_MEMORY;
                }
            }
            break;
        }

        case APP_STATE_READ_MEMORY:
        {
            if (APP_MemoryRead((uint32_t *)&xip_image_buffer[0], sizeof(xip_image_buffer), MEM_ADDRESS) != APP_TRANSFER_COMPLETED)
            {
                appData.state = APP_STATE_ERROR;
                break;
            }

            appData.state = APP_STATE_READ_CONTINUOUS;

            break;
        }

        case APP_STATE_READ_CONTINUOUS:
        {
            appData.state = APP_STATE_SUCCESS;

            if (APP_MemoryReadContinuous(MEM_ADDRESS) != APP_TRANSFER_COMPLETED)
            {
                appData.state = APP_STATE_ERROR;
                break;
            }

            for (idx = 0; idx < BUFFER_SIZE; idx++)
            {
                if(*(read_memory) != xip_image_pattern[idx])
                {
                    appData.state = APP_STATE_ERROR;
                    break;

                }
                read_memory++;
            }

            break;
        }

        case APP_STATE_SUCCESS:
        {
            /* Set PC and SP of the XIP Image application programmed in QSPI Flash memory*/

            /* Pointer to Reset Handler of the XIP Image Application */
            __start_new = (uint32_t(*) (void)) xip_image_buffer[1];
            __start_sp = xip_image_buffer[0];


            __set_MSP(__start_sp);

            /* Rebase the vector table base address */
            SCB->VTOR = ((uint32_t) QSPIMEM_ADDR & SCB_VTOR_TBLOFF_Msk);

            /* Run XIP Image Application */
            __start_new();

            /* Should never reach here */
            break;
        }

        case APP_STATE_ERROR:
        default:
            LED_ON();

    }
}

/*******************************************************************************
 End of File
 */
