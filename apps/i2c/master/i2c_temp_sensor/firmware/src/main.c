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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include <stddef.h>                     // Defines NULL
#include <stdbool.h>                    // Defines true
#include <stdlib.h>                     // Defines EXIT_FAILURE
#include "definitions.h"                // SYS function prototypes
#include <string.h>

#define USER_SWITCH_PRESSED                     0
#define USER_SWITCH_RELEASED                    1

#define APP_TEMP_SENSOR_SLAVE_ADDR              0x0018
#define APP_TEMPERATURE_MEM_ADDR                0x05
#define APP_MFG_ID_MEM_ADDR                     0x06
#define APP_DEV_REV_ID_MEM_ADDR                 0x07

typedef enum
{
    APP_STATE_TEMP_SENSOR_STATUS_VERIFY,
    APP_STATE_CHECK_TEMP_SENSOR_READY,
    APP_STATE_READ_MFG_ID,
    APP_STATE_READ_DEV_REV_ID,
    APP_STATE_WAIT_DEV_REV_ID_READ_COMPLETE,
    APP_STATE_WAIT_SWITCH_PRESS,
    APP_STATE_READ_TEMPERATURE,    
    APP_STATE_PRINT_TEMPERATURE,
    APP_STATE_WAIT_SWITCH_RELEASE,
    APP_STATE_XFER_ERROR,
    APP_STATE_IDLE

} APP_STATES;

typedef enum
{
    APP_TRANSFER_STATUS_IN_PROGRESS,
    APP_TRANSFER_STATUS_SUCCESS,
    APP_TRANSFER_STATUS_ERROR,
    APP_TRANSFER_STATUS_IDLE,

} APP_TRANSFER_STATUS;

static uint8_t wrData;
static uint8_t rdData[2];
static uint16_t temperature;
static APP_STATES state;
static volatile APP_TRANSFER_STATUS transferStatus;

static void APP_I2CCallback(uintptr_t context )
{
    APP_TRANSFER_STATUS* pTransferStatus = (APP_TRANSFER_STATUS*)context;

    if(I2C2_ErrorGet() == I2C_ERROR_NONE)
    {
        if (pTransferStatus)
        {
            *pTransferStatus = APP_TRANSFER_STATUS_SUCCESS;
        }
    }
    else
    {
        if (pTransferStatus)
        {
            *pTransferStatus = APP_TRANSFER_STATUS_ERROR;
        }
    }
}

static uint16_t APP_CalculateTemperature(uint16_t rawTemperature)
{
    uint16_t calcTemperature;
    uint8_t upperByte = (uint8_t)rawTemperature;
    uint8_t lowerByte = ((uint8_t*)&rawTemperature)[1];
        
    upperByte = upperByte & 0x1F;
    if ((upperByte & 0x10) == 0x10)     // Ta < 0 degC
    {
        upperByte = upperByte & 0x0F;       // Clear sign bit
        calcTemperature = 256 - ((upperByte * 16) + lowerByte/16);
    }
    else
    {
        calcTemperature = ((upperByte * 16) + lowerByte/16);
    }
    
    return calcTemperature;
    
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{    
    uint8_t ackData = 0;

    /* Initialize all modules */
    SYS_Initialize ( NULL );
    
    /* Set the initial state */
    state = APP_STATE_TEMP_SENSOR_STATUS_VERIFY;

    while(1)
    {
        /* Check the application's current state. */
        switch (state)
        {
            case APP_STATE_TEMP_SENSOR_STATUS_VERIFY:

                /* Register the TWIHS Callback with transfer status as context */
                I2C2_CallbackRegister( APP_I2CCallback, (uintptr_t)&transferStatus );

               /* Verify if Temperature Sensor is ready */
                transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                if (I2C2_Write(APP_TEMP_SENSOR_SLAVE_ADDR, &ackData, 1) == false)
                {
                    state = APP_STATE_XFER_ERROR;
                }
                else
                {
                    state = APP_STATE_CHECK_TEMP_SENSOR_READY;
                }                             
                break;

            case APP_STATE_CHECK_TEMP_SENSOR_READY:

                if (transferStatus == APP_TRANSFER_STATUS_SUCCESS)
                {
                    /* Temperature sensor is ready. Print message on the console */
                    /* TODO: Print message on console */
                    
                    state = APP_STATE_READ_MFG_ID;
                }
                else if (transferStatus == APP_TRANSFER_STATUS_ERROR)
                {
                    /* Temperature sensor is not ready. 
                     * Keep checking until it is ready. */
                    transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                    if (I2C2_Write(APP_TEMP_SENSOR_SLAVE_ADDR, &ackData, 1) == false)
                    {
                        state = APP_STATE_XFER_ERROR;
                    }
                }
                break;
                
            case APP_STATE_READ_MFG_ID:
                
                wrData = APP_MFG_ID_MEM_ADDR;
                transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                if (I2C2_WriteRead(APP_TEMP_SENSOR_SLAVE_ADDR, &wrData, 1, &rdData[0], 2) == false)
                {
                    state = APP_STATE_XFER_ERROR;
                }
                else
                {
                    state = APP_STATE_READ_DEV_REV_ID;
                }
                break;
                
            case APP_STATE_READ_DEV_REV_ID:
                if (transferStatus == APP_TRANSFER_STATUS_SUCCESS)
                {
                    printf("Manufacturer ID: 0x%04x, ", ((uint16_t)rdData[0] << 8) | ((uint16_t)rdData[1]));
                    
                    /* Read Device/Revision ID */
                    wrData = APP_DEV_REV_ID_MEM_ADDR;
                    transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                    if (I2C2_WriteRead(APP_TEMP_SENSOR_SLAVE_ADDR, &wrData, 1, &rdData[0], 2) == false)
                    {
                        state = APP_STATE_XFER_ERROR;
                    }
                    else
                    {
                        state = APP_STATE_WAIT_DEV_REV_ID_READ_COMPLETE;
                    }                    
                }
                else if (transferStatus == APP_TRANSFER_STATUS_ERROR)
                {
                    state = APP_STATE_XFER_ERROR;
                }
                break;
                
            case APP_STATE_WAIT_DEV_REV_ID_READ_COMPLETE:
                if (transferStatus == APP_TRANSFER_STATUS_SUCCESS)
                {
                    printf("Device ID: 0x%02x, Revision ID: 0x%02x \r\n", rdData[0] , rdData[1]);
                    state = APP_STATE_WAIT_SWITCH_PRESS;
                }
                else if (transferStatus == APP_TRANSFER_STATUS_ERROR)
                {
                    state = APP_STATE_XFER_ERROR;
                }
                break;

            case APP_STATE_WAIT_SWITCH_PRESS:
                
                if (USER_SWITCH_Get() == USER_SWITCH_PRESSED)
                {
                    state = APP_STATE_READ_TEMPERATURE;
                }
                break;
                
            case APP_STATE_READ_TEMPERATURE:
                 
                wrData = APP_TEMPERATURE_MEM_ADDR;
                transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                
                if (I2C2_WriteRead(APP_TEMP_SENSOR_SLAVE_ADDR, &wrData, 1, &rdData[0], 2) == false)
                {
                    state = APP_STATE_XFER_ERROR;
                }
                else
                {
                    state = APP_STATE_PRINT_TEMPERATURE;
                }                
                break;            

            case APP_STATE_PRINT_TEMPERATURE:

                if (transferStatus == APP_TRANSFER_STATUS_SUCCESS)
                {
                    temperature = APP_CalculateTemperature(*((uint16_t*)rdData));
                    printf("Temperature = %d C\r\n", temperature);
                    
                    state = APP_STATE_WAIT_SWITCH_RELEASE;
                }
                else if (transferStatus == APP_TRANSFER_STATUS_ERROR)
                {
                    state = APP_STATE_XFER_ERROR;
                }
                break;
            
            case APP_STATE_WAIT_SWITCH_RELEASE:
                
                if (USER_SWITCH_Get() == USER_SWITCH_RELEASED)
                {
                    state = APP_STATE_WAIT_SWITCH_PRESS;
                }                
                break;
            
            case APP_STATE_XFER_ERROR:
            
                printf("I2C Transfer Error!");
                state = APP_STATE_IDLE;
                break;
            
            case APP_STATE_IDLE:
                break;
                
            default:
                break;
        }
    }
}
/*******************************************************************************
 End of File
*/

