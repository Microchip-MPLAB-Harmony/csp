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

#define LED_ON                      LED_Clear
#define LED_OFF                     LED_Set
#define LED_TOGGLE                  LED_Toggle

volatile uint8_t rwwee_erase_complete;
bool success_flag;
uint8_t nvm_mainarray_read_status;

void populate_buffer(uint32_t* data, int32_t pattern, uint32_t size)
{
    int i = 0;

    for (i = 0; i < (size/4); i++)
    {
        *(data + i) = pattern;
    }
}


void Nvmctrl_callback(uintptr_t context)
{
    rwwee_erase_complete = true;
}
// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint32_t page_data [NVMCTRL_FLASH_PAGESIZE] = {0};
    uint32_t row_data [NVMCTRL_FLASH_ROWSIZE] = {0};    
    uint32_t read_page_data_rwwee [NVMCTRL_RWWEEPROM_PAGESIZE] = {0};    
    uint32_t start_address = NVMCTRL_FLASH_START_ADDRESS + 0x20000;
    uint32_t start_address_rwwee = NVMCTRL_RWWEEPROM_START_ADDRESS;  
    int8_t index;
    rwwee_erase_complete = false;
    nvm_mainarray_read_status = 0;
    success_flag = false;    
    
    /* Initialize all modules */
    SYS_Initialize ( NULL );
    SYSTICK_TimerStart();
    LED_OFF();
        
    /* Populate RWEE page with data pattern 0x12 */
    populate_buffer(page_data, 0x12121212,NVMCTRL_RWWEEPROM_PAGESIZE);       

    while(NVMCTRL_IsBusy());
    /* Erase the RWWEE row */
    NVMCTRL_RWWEEPROM_RowErase(start_address_rwwee);
    while(NVMCTRL_IsBusy());    
    /* Program 64 byte page to RWWEE section */
    NVMCTRL_RWWEEPROM_PageWrite(page_data, start_address_rwwee);            
    
    /* Populate main area page with data pattern 0x04 */
    populate_buffer(page_data, 0x04040404,NVMCTRL_FLASH_PAGESIZE);       
    while(NVMCTRL_IsBusy());
    /* Erase the row */
    NVMCTRL_RowErase(start_address);
    while(NVMCTRL_IsBusy()); 
    /* Program row with data pattern 0x04 */    
    for (index=0; index < (NVMCTRL_FLASH_ROWSIZE/NVMCTRL_FLASH_PAGESIZE); index++)
    {
        NVMCTRL_PageWrite(page_data, (start_address+(NVMCTRL_FLASH_PAGESIZE*index)));            
        while(NVMCTRL_IsBusy());             
    }

    /* Register callback to get event when erasing of RWWEE row is completed */
    NVMCTRL_CallbackRegister(Nvmctrl_callback,0);       
    NVMCTRL_RWWEEPROM_RowErase(start_address_rwwee);        

    if(rwwee_erase_complete == true)
    {
        rwwee_erase_complete = false;
    }
    else
    {    
        /* While the erasing of RWWEE row is under progress, perform read
         * from NVM main area  */                
        populate_buffer(row_data, 0x04040404,NVMCTRL_FLASH_ROWSIZE);                          
        /* Verify the data read from NVM main area */
        if (!memcmp(row_data, (void *)start_address, NVMCTRL_FLASH_ROWSIZE))
        {        
            LED_ON();            
            nvm_mainarray_read_status = 1;            
        }
    }   
    
    while ( true )
    {
        /* Maintain state machines of all polled MPLAB Harmony modules. */
        SYS_Tasks ( );

        /* Read from NVM main area is success  */        
        if(nvm_mainarray_read_status == 1)
        {
            /* Check if the erase on RWWEE row is completed */
            if(rwwee_erase_complete == true)
            {
                nvm_mainarray_read_status = 2;
            }
        }
        else if (nvm_mainarray_read_status == 2)
        {
            populate_buffer(page_data, 0x12121212,NVMCTRL_RWWEEPROM_PAGESIZE);              
            NVMCTRL_RWWEEPROM_Read((uint32_t *)read_page_data_rwwee, sizeof(read_page_data_rwwee),start_address_rwwee);
            /* Verify that the written data from page in RWWEE is erased */
            if (memcmp(page_data, read_page_data_rwwee, NVMCTRL_RWWEEPROM_PAGESIZE))
            {        
                success_flag = true;    
                nvm_mainarray_read_status = 0;
            }            

        }
        else
        {
            if(success_flag == true)
            {
                SYSTICK_DelayMs(1000);
                LED_TOGGLE();            
            }
            else
            {
                ;
            }
        }        
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

