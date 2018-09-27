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
#include "definitions.h"                // SYS function prototypes
#include <string.h>

#define LED1_On()                       LED1_Clear()
#define LED1_Off()                      LED1_Set()

// *****************************************************************************
/* I2C Address for the on-board EEPROM AT24MAC402.

  Summary:
    Defines the on-board EEPROM AT24MAC402's I2C Address.

  Description:
    This macro defines the on-board EEPROM AT24MAC402's I2C Address. 
*/

#define APP_AT24MAC_DEVICE_ADDR             (0x0057)

// *****************************************************************************
/* EEPROM AT24MAC402 memory address.

  Summary:
    Defines the on-board EEPROM AT24MAC402 memory address.

  Description:
    This macro defines the on-board EEPROM AT24MAC402 memory Address. Data is
    read/write from/to the location starting from this address.
 */

#define APP_AT24MAC_MEMORY_ADDR             (0x00)

// *****************************************************************************
/* Transmit data length.

  Summary:
    Defines the length of the data to be transmitted to on-board EEPROM AT24MAC402.

  Description:
    This macro defines the size of one page on the AT24 EEPROM.
 */

#define APP_AT24MAC_PAGE_SIZE               (16)
// *****************************************************************************
/* Transmit data length.

  Summary:
    Defines the length of the data to be transmitted to on-board EEPROM AT24MAC402.

  Description:
    This macro defines the length of the data to be tranmitted to the on-board
    EEPROM AT24MAC402. The length must be sufficient to hold the data and the 
    AT24 memory address.
 */

#define APP_TRANSMIT_DATA_LENGTH            (APP_AT24MAC_PAGE_SIZE + 1)

// *****************************************************************************
/* Receive data length.

  Summary:
    Defines the length of the data to be received from on-board EEPROM AT24MAC402.

  Description:
    This macro defines the length of the data to be received from the on-board
    EEPROM AT24MAC402. 
 */

#define APP_RECEIVE_DATA_LENGTH             (APP_AT24MAC_PAGE_SIZE)

// *****************************************************************************
/* Acknowledge polling data length.

  Summary:
    Defines the length of the data to be transmitted to on-board EEPROM AT24MAC402
    during Acknowledge polling.

  Description:
    This macro defines the length of the data to be tranmitted to the on-board
    EEPROM AT24MAC402 during Acknowledge polling. This define is used by the TWIHS
    PLib Write API.
 */

#define APP_ACK_DATA_LENGTH                 (1)

// *****************************************************************************
/* Application Test Transmit Data array

  Summary:
    Holds the application test transmit data.

  Description:
    This array holds the application's test transmit data.

  Remarks:
    None.
*/

static uint8_t testTxData[APP_TRANSMIT_DATA_LENGTH] =
{
	APP_AT24MAC_MEMORY_ADDR,
    'A', 'T', 'S', 'A', 'M', ' ', 'T', 'W', 'I', 'H', 'S', ' ', 'D', 'e', 'm', 'o',
};

// *****************************************************************************
/* Application Test receive Data array.

  Summary:
    Holds the application received test data.

  Description:
    This array holds the application's received test data.

  Remarks:
    None.
*/

static uint8_t  testRxData[APP_RECEIVE_DATA_LENGTH];

// *****************************************************************************
/* Application's state machine enum 

  Summary:
    Enumerator to define app states.

  Description:
    This enumerator defines all the possible application states.

  Remarks:
    None.
*/
typedef enum
{    
    APP_STATE_EEPROM_STATUS_VERIFY,
    APP_STATE_EEPROM_WRITE,
    APP_STATE_EEPROM_WAIT_INTERNAL_WRITE_COMPLETE,
    APP_STATE_EEPROM_READ,
    APP_STATE_VERIFY,
    APP_STATE_IDLE,    
    APP_STATE_XFER_SUCCESSFUL,
    APP_STATE_XFER_ERROR
            
} APP_STATES;

// *****************************************************************************
/* Transfer status enum 

  Summary:
    Enumerator to define transfer status.

  Description:
    This enumerator defines all the possible transfer states.

  Remarks:
    None.
*/
typedef enum
{
    APP_TRANSFER_STATUS_IN_PROGRESS,
    APP_TRANSFER_STATUS_SUCCESS,
    APP_TRANSFER_STATUS_ERROR,
    APP_TRANSFER_STATUS_IDLE,
            
} APP_TRANSFER_STATUS;

// *****************************************************************************
// *****************************************************************************
// Section: Local functions
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* void APP_TWIHSCallback(uintptr_t context)

  Summary:
    Function called by TWIHS PLIB upon transfer completion

  Description:
    This function will be called by TWIHS PLIB when transfer is completed.
    In this function, transferStatus variable is obtained from the context
    parameter and is updated based on the value returned by the TWIHS PLIB
    error get API.

  Remarks:
    None.
*/

void APP_TWIHSCallback(uintptr_t context )
{
    APP_TRANSFER_STATUS* transferStatus = (APP_TRANSFER_STATUS*)context;
    
    if(TWIHS0_ErrorGet() == TWIHS_ERROR_NONE)
    {
        *transferStatus = APP_TRANSFER_STATUS_SUCCESS;
    }
    else
    {
        *transferStatus = APP_TRANSFER_STATUS_ERROR;
    }        
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************
    
int main ( void )
{
    APP_STATES currState = APP_STATE_EEPROM_STATUS_VERIFY;
    APP_STATES nextState = APP_STATE_IDLE;    
    volatile APP_TRANSFER_STATUS transferStatus = APP_TRANSFER_STATUS_ERROR;
    uint8_t ackData = 0;
    bool isInternalWriteCheckInProgress = false;
           
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        /* Check the application's current state. */
        switch (currState)
        {
            case APP_STATE_EEPROM_STATUS_VERIFY:
            
                /* Register the TWIHS Callback with current state as context */
                TWIHS0_CallbackRegister( APP_TWIHSCallback, (uintptr_t)&transferStatus );
                
                /* Verify if EEPROM is ready to accept new requests */
                transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                TWIHS0_Write(APP_AT24MAC_DEVICE_ADDR, &ackData, APP_ACK_DATA_LENGTH);

                currState = APP_STATE_IDLE; 
                nextState = APP_STATE_EEPROM_WRITE;
                break;
            
            case APP_STATE_EEPROM_WRITE:
                            
                /* Write 1 page of data to EEPROM */
                transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                TWIHS0_Write(APP_AT24MAC_DEVICE_ADDR, &testTxData[0], APP_TRANSMIT_DATA_LENGTH);
                
                currState = APP_STATE_IDLE;  
                nextState = APP_STATE_EEPROM_WAIT_INTERNAL_WRITE_COMPLETE;
                break;
            
            case APP_STATE_EEPROM_WAIT_INTERNAL_WRITE_COMPLETE:
            
                /* Check whether EEPROM's internal write cycle is complete */
                if (transferStatus == APP_TRANSFER_STATUS_SUCCESS)
                {
                    isInternalWriteCheckInProgress = false;
                    currState = APP_STATE_EEPROM_READ;
                }
                else
                {
                    /* EEPROM's internal write cycle is not complete. Keep checking. */
                    transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                    TWIHS0_Write(APP_AT24MAC_DEVICE_ADDR, &ackData, APP_ACK_DATA_LENGTH);
                
                    isInternalWriteCheckInProgress = true;
                    currState = APP_STATE_IDLE; 
                    nextState = APP_STATE_EEPROM_WAIT_INTERNAL_WRITE_COMPLETE;
                }
                break;            

            case APP_STATE_EEPROM_READ:
                            
                /* Read the data from the page written earlier */
                transferStatus = APP_TRANSFER_STATUS_IN_PROGRESS;
                TWIHS0_Read(APP_AT24MAC_DEVICE_ADDR, &testRxData[0], APP_RECEIVE_DATA_LENGTH);
                
                currState = APP_STATE_IDLE; 
                nextState = APP_STATE_VERIFY;
                break;
                
            case APP_STATE_VERIFY:
                
                /* Verify the read data */
                if (memcmp(&testTxData[1], &testRxData[0], APP_RECEIVE_DATA_LENGTH) == 0)
                {
                    /* It means received data is same as transmitted data */
                    currState = APP_STATE_XFER_SUCCESSFUL;                    
                }
                else
                {
                    /* It means received data is not same as transmitted data */
                    currState = APP_STATE_XFER_ERROR;
                }
                break;                
            
            case APP_STATE_IDLE:
            
                /* Wait for the transfer to complete, and go to the next state if
                 * the last transfer was successful. If the EEPROM internal write
                 * cycle is been checked, then repeat the check if the EEPROM 
                 * returns NAK (transferStatus == APP_TRANSFER_STATUS_ERROR).
                 */
                if (transferStatus == APP_TRANSFER_STATUS_SUCCESS)
                {                    
                    /* Reset the transfer status if the internal write cycle check
                     * is not in progress.
                     */
                    if (isInternalWriteCheckInProgress == false)
                    {
                        transferStatus = APP_TRANSFER_STATUS_IDLE;
                    }
                    currState = nextState;
                }   
                else if (transferStatus == APP_TRANSFER_STATUS_ERROR)
                {
                    /* Reset the transfer status if the internal write cycle check
                     * is not in progress. If internal write check is in progress
                     * then continue checking the internal write status; else
                     * enter error state.
                     */
                    if (isInternalWriteCheckInProgress == false)
                    {
                        transferStatus = APP_TRANSFER_STATUS_IDLE;
                        currState = APP_STATE_XFER_ERROR;                        
                    }
                    else
                    {
                        currState = nextState;
                    }
                }
                break;
                
            case APP_STATE_XFER_SUCCESSFUL:
            
                LED1_On();
                break;
            
            case APP_STATE_XFER_ERROR:
            
                LED1_Off();
                break;
            
            default:
                break;
        }
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

