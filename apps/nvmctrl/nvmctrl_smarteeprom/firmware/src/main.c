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

/* Define the NVMCTRL_SEESBLK_MASK_BITS to extract the NVMCTRL_SEESBLK bits(35:32) from NVM User Page Mapping(0x00804000) */
#define NVMCTRL_SEESBLK_MASK_BITS   0x0F

/* Define the NVMCTRL_SEEPSZ_MASK_BITS to extract the NVMCTRL_SEEPSZ bits(38:36) from NVM User Page Mapping(0x00804000) */
#define NVMCTRL_SEEPSZ_MASK_BITS    0x07

/* A specific byte pattern stored at the begining of SmartEEPROM data area.
 * When the application comes from a reset, if it finds this signature,
 * the assumption is that the SmartEEPROM has some valid data.
 */
#define SMEE_CUSTOM_SIG         0x5a5a5a5a

/* Define the number of bytes to be read when a read request comes */
#define MAX_BUFF_SIZE          256

/* The application toggles SmartEEPROM data at the following address
 * each time the device is reset. This address must be within the total
 * number of EEPROM data bytes ( Defined by SBLK and PSZ fuse values).
 */
#define SEEP_TEST_ADDR          32

/* This example demo assumes fuses SBLK = 1 and PSZ = 3, thus total size is 4096 bytes */
#define SEEP_FINAL_BYTE_INDEX   4095

/* Define a pointer to access SmartEEPROM as bytes */
uint8_t *SmartEEPROM8       = (uint8_t *)SEEPROM_ADDR;

/* Define a pointer to access SmartEEPROM as words (32-bits) */
uint32_t *SmartEEPROM32     = (uint32_t *)SEEPROM_ADDR;

uint8_t menu[]              = "\r\n******** Enter choice ******** \
\r\n1. Read SmartEEPROM \r\n2. Write SmartEEPROM\r\n3. Reset device to \
validate written data, is EEPROM holding user data even after reset\r\n";
typedef enum {ReadSmartEEPROM = '1', WriteSmartEEPROM = '2', ResetDevice = '3', NoSelection = 0} MenuOptions;
uint8_t data_8;
uint8_t eeprom_data_buffer[MAX_BUFF_SIZE] = {0};


/**
 * \brief Invert a byte in SmartEEPROM
 *
 * To invert the data at the given index in SmartEEPROM
 */
void invert_seep_byte(uint8_t index)
{
	/* Wait till the SmartEEPROM is free */
	while (NVMCTRL_SmartEEPROM_IsBusy());

	/* Read the data, invert it, and write it back */
	data_8              = SmartEEPROM8[index];
	printf("\r\nData at test address %d is = %d\r\n", index, (int)data_8);
	SmartEEPROM8[index] = !data_8;
	printf("\r\nInverted the data at test address and written\r\n");
}

/**
 * \brief Verify the custom data in SmartEEPROM
 *
 * Verify the custom data at initial 4 bytes of SmartEEPROM
 */
int8_t verify_seep_signature(void)
{
    uint32_t        NVMCTRL_SEESBLK_FuseConfig    = ((*(uint32_t *)(USER_PAGE_ADDR + 4)) >> 0) & NVMCTRL_SEESBLK_MASK_BITS;
	int8_t          ret_val                       = 0;

	/* If SBLK fuse is not configured, inform the user and wait here */
	if (!NVMCTRL_SEESBLK_FuseConfig)
    {
		printf("\r\nPlease configure SBLK fuse to allocate SmartEEPROM area\r\n");
		while (1);
	}

	if (SMEE_CUSTOM_SIG != SmartEEPROM32[0])
    {
		ret_val = 0x4;
	}

	return ret_val;
}

/**
 * \brief Print a buffer as hex values
 *
 * Print a given array as a hex values
 */
void print_hex_array(void *mem, uint16_t len)
{
	unsigned char *p = (unsigned char *)mem;

	for(uint32_t i = 0; i < len; i++)
    {
		if ((i != 0) && (!(i & 0x7)))
        {
			printf("\r\n");
        }
		printf("%03d ", p[i]);
	}
	printf("\r\n");
}

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

int main ( void )
{
    uint32_t    NVMCTRL_SEESBLK_FuseConfig  = ((*(uint32_t *)(USER_PAGE_ADDR + 4)) >> 0) & NVMCTRL_SEESBLK_MASK_BITS;
    uint32_t    NVMCTRL_SEEPSZ_FuseConfig   = ((*(uint32_t *)(USER_PAGE_ADDR + 4)) >> 4) & NVMCTRL_SEEPSZ_MASK_BITS;
	MenuOptions user_selection              = NoSelection;
	uint32_t    num_of_bytes_to_read        = 0;
	uint32_t    eeprom_data                 = 0;
	uint32_t    eeprom_addr                 = 0;
	uint32_t    eeprom_data_buf_start_index = 0;

    /* Initialize all modules */
    SYS_Initialize ( NULL );

	printf("\r\n\r\n=============SmartEEPROM Example=============\r\n");

	if (verify_seep_signature() == 0)
    {
		printf("\r\nSmartEEPROM contains valid data \r\n");
	}
    else
    {
		printf("\r\nStoring signature to SmartEEPROM address 0x00 to 0x03\r\n");
        /* Wait till the SmartEEPROM is free */
        while (NVMCTRL_SmartEEPROM_IsBusy())
        {
            ;
        }

		SmartEEPROM32[0] = SMEE_CUSTOM_SIG;
	}
	printf("\r\nFuse values for SBLK = %d, PSZ = %d. See the table 'SmartEEPROM Virtual \
	Size in Bytes' in the Datasheet to calculate total available bytes \r\n",
	       (int)NVMCTRL_SEESBLK_FuseConfig,
	       (int)NVMCTRL_SEEPSZ_FuseConfig);

	/* Toggle a SmartEEPROM byte and give indication with LED0 on SAM E54 Xpro */
	invert_seep_byte(SEEP_TEST_ADDR);

	/* Check the data at test address and show indication on LED0 */
	if (SmartEEPROM8[SEEP_TEST_ADDR])
    {
        LED_ON();
	}
    else
    {
        LED_OFF();
	}

    while ( true )
    {
		printf("%s", menu);
		if (scanf("%c", (char *)&user_selection) == 0)
        {
			/* If its not a number, flush stdin */
			fflush(stdin);
			continue;
		}
		printf("\r\nSelected option is %c\r\n", user_selection);
		switch (user_selection)
        {
            case ReadSmartEEPROM:
                /* Code to read from EEPROM */
                printf("\r\nEnter read address >> ");
                scanf("%d", (int *)&eeprom_addr);
                /* This demo is defined NVMCTRL fuses with SBLK = 1 and PSZ = 03
                 * Thus the highest address is 4095 (See data sheet for the more)
                 * details.
                 */
                if (eeprom_addr > SEEP_FINAL_BYTE_INDEX) {
                    printf("\r\nERROR: Address invalid. Try again \r\n");
                    break;
                }
                printf("\r\nEnter number bytes need to read >> ");
                scanf("%d", (int *)&num_of_bytes_to_read);
                fflush(stdin);              /* Removing if any null characters are there in Rx register after reading number of bytes to read value */ 
                if (num_of_bytes_to_read > MAX_BUFF_SIZE)
                {
                    printf("\r\nERROR: In this Demo, at a time demo can able to \
                            print 256 bytes. Try again \r\n");
                    break;
                }
                /* Checking end address limit when reading data */
                if((eeprom_addr + num_of_bytes_to_read) > SEEP_FINAL_BYTE_INDEX)
                {
                    num_of_bytes_to_read    = (SEEP_FINAL_BYTE_INDEX + 1 - eeprom_addr);
                }
                for (uint32_t  i = 0; i < num_of_bytes_to_read; i++)
                {
                    eeprom_data_buffer[i]   = SmartEEPROM8[eeprom_addr + i];
                }
                printf("\r\nEEPROM Data from location: %d to location: %d: \r\n", 
                        (int)eeprom_addr, (int)(eeprom_addr + num_of_bytes_to_read - 1));
                print_hex_array(eeprom_data_buffer, num_of_bytes_to_read);
                break;

            case WriteSmartEEPROM:
                /* Code to write EEPROM */
                printf("\r\nEnter write address >> ");
                scanf("%d", (int *)&eeprom_addr);
                /* This demo is defined NVMCTRL fuses with SBLK = 1 and PSZ = 03
                 * Thus the highest address is 4095 (See data sheet for the more)
                 * details.
                 */
                if (eeprom_addr > SEEP_FINAL_BYTE_INDEX) {
                    printf("\r\nERROR: Address invalid. Try again \r\n");
                    break;
                }
                printf("\r\nEnter data >> ");
                scanf("%d", (int *)&eeprom_data);
                fflush(stdin);              /* Removing if any null characters are there in Rx register after reading eeprom data value */ 
                SmartEEPROM8[eeprom_addr] = eeprom_data;
                printf("\r\nWritten %d at %d", (int)eeprom_data, (int)eeprom_addr);
                eeprom_data_buf_start_index = (eeprom_addr & (~0xFF));
                for (uint32_t  i = 0; i < MAX_BUFF_SIZE; i++)
                {
                    eeprom_data_buffer[i] = SmartEEPROM8[eeprom_data_buf_start_index + i];
                }
                printf("\r\nEEPROM Data from location: %d  to location: %d: \r\n", 
                        (int)(eeprom_addr & (~0xFF)), (int)((eeprom_addr & (~0xFF)) + MAX_BUFF_SIZE - 1));
                print_hex_array(eeprom_data_buffer, MAX_BUFF_SIZE);
                break;

            case ResetDevice:
                NVIC_SystemReset();
                break;

            default:
                printf("\r\nInvalid option \r\n");
                break;
		}
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}


/*******************************************************************************
 End of File
*/

