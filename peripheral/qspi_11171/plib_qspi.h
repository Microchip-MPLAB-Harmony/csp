/*******************************************************************************
Interface definition of QSPI PLIB.

 Company:
    Microchip Technology Inc.

 File Name:
    plib_qspi.h

 Summary:
    Interface definition of the Quad Serial Peripheral Interface Plib (QSPI).

 Description:
    This file defines the interface for the QSPI Plib.
    It allows user to setup QSPI and transfer data to and from slave devices
    attached.
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

#ifndef PLIB_QSPI_H // Guards against multiple inclusion
#define PLIB_QSPI_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

/* This section lists the other files that are included in this file.
*/

#include "PIC32CZ2038CA70144.h"
#include <stdbool.h>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
    extern "C" {
#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: Data Types
// *****************************************************************************
// *****************************************************************************

/* QSPI Address Length 

   Summary:
    Defines the data type to specify address length 

   Description:
    This may be used to to specify the address length for QSPI transaction

   Remarks:
    None.
*/

typedef enum
{
    ADDRL_24_BIT = QSPI_IFR_ADDRL_24_BIT,
    ADDRL_32_BIT = QSPI_IFR_ADDRL_32_BIT
} QSPI_ADDRESS_LENGTH;

/* QSPI Lane Width 
   Summary:
    Defines the data type to specify lane width 

   Description:
    This may be used to to specify the lane length to be used for QSPI transaction

   Remarks:
    None.
*/

typedef enum
{
    SINGLE_BIT_SPI = QSPI_IFR_WIDTH_SINGLE_BIT_SPI,
    DUAL_OUTPUT = QSPI_IFR_WIDTH_DUAL_OUTPUT,
    QUAD_OUTPUT = QSPI_IFR_WIDTH_QUAD_OUTPUT,
    DUAL_IO = QSPI_IFR_WIDTH_DUAL_IO,
    QUAD_IO = QSPI_IFR_WIDTH_QUAD_IO,
    DUAL_CMD = QSPI_IFR_WIDTH_DUAL_CMD,
    QUAD_CMD = QSPI_IFR_WIDTH_QUAD_CMD	
} QSPI_LANE_WIDTH;

/* QSPI Option Length 
   Summary:
    Defines the data type to specify option length 

   Description:
    This may be used to to specify the option length for QSPI transaction

   Remarks:
    None.
*/

typedef enum
{
    OPTL_1_BIT = QSPI_IFR_OPTL_OPTION_1BIT,
    OPTL_2_BIT = QSPI_IFR_OPTL_OPTION_2BIT,
    OPTL_4_BIT = QSPI_IFR_OPTL_OPTION_4BIT,
    OPTL_8_BIT = QSPI_IFR_OPTL_OPTION_8BIT
} QSPI_OPTION_LENGTH;

/* QSPI Command Transfer structure
 Summary:
    Defines the data type for the QSPI commands transfer.

 Description:
    This data type should be used to send the QSPI instruction code register and
    instruction frame register information for sending a command to QSPI slave.

 Remarks:
    None.
*/

typedef struct {
    /* QSPI instruction code */
    uint8_t instruction;
    /* QSPI instruction Frame register informations */
    QSPI_LANE_WIDTH width;
    bool addr_en;
    QSPI_ADDRESS_LENGTH addr_len;
} qspi_command_xfer_t;

/* QSPI Register Transfer structure
 Summary:
    Defines the data type for the QSPI register data transfer.

 Description:
    This data type should be used to send the QSPI instruction code register and
    instruction frame register information for reading/writing QSPI slave registers.

 Remarks:
    None.
*/

typedef struct {
    /* QSPI instruction code */
    uint8_t instruction;
    /* QSPI instruction Frame register informations */
    QSPI_LANE_WIDTH width;
    /* For Read Register */
    uint8_t dummy_cycles;
} qspi_register_xfer_t;

/* QSPI Memory Transfer structure
 Summary:
    Defines the data type for the QSPI memory transfer.

 Description:
    This data type should be used to send the QSPI instruction code register and
    instruction frame register information for reading/writing QSPI slave memory.

 Remarks:
    None.
*/

typedef struct {
    /* QSPI instruction code */
    uint8_t instruction;
    /* QSPI option code */
    uint8_t option;
    /* QSPI instruction Frame register informations */
    QSPI_LANE_WIDTH width;
    QSPI_ADDRESS_LENGTH addr_len;
    bool option_en;
    QSPI_OPTION_LENGTH option_len;
    bool continuous_read_en;
    /* For Read memory */
    uint8_t dummy_cycles;
} qspi_memory_xfer_t;

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

/* The following functions make up the methods (set of possible operations) of
this interface.
*/

// *****************************************************************************
/* Function:
    void QSPI_Initialize( void )

 Summary:
    Initializes given instance of the QSPI peripheral.

 Description:
    This function initializes the given instance of the QSPI peripheral as
    configured by the user.

 Precondition:
    Memory Protection Unit(MPU) has to be enabled and configured for QSPI memory.

 Parameters:
    None.

 Returns:
    None.

 Example:
    <code>
        QSPI_Initialize();
    </code>
*/
void QSPI_Initialize( void );

/* Function:
    bool QSPI_CommandWrite( qspi_command_xfer_t *qspi_command_xfer, uint32_t address )

 Summary:
    Writes command to QSPI slave device.

 Description:
    This function can be used to send commands to QSPI slave device which does
    not include any exchange of data.

 Precondition:
    QSPI_Initialize must have been called for the associated QSPI instance.

 Parameters:
    *qspi_command_xfer - pointer to QSPI command transfer structure holding the instruction
    code register and instruction frame register information.

    address - Instruction address to be sent with the instruction frame. Can be
    passed as 0 if no address associated with instruction.

 Returns:
    True on transfer request success.
    False on transfer request failure.

 Example:
    <code>

        #define WRITE_ENABLE_CODE 0x06

        static qspi_command_xfer_t qspi_command_xfer;

        //Initialize QSPI
        QSPI_Initialize();

        // Use QAUD SPI Lane
        qspi_command_xfer.width = QUAD_CMD;

        // Send Write enable command
        qspi_command_xfer->qspi_code.instruction = WRITE_ENABLE_CODE;

        if (TRUE != QSPI_CommandWrite(&qspi_command_xfer, 0))
        {
            // Handle Error
        }

    </code>
*/
bool QSPI_CommandWrite( qspi_command_xfer_t *qspi_command_xfer, uint32_t address );

/* Function:
    bool QSPI_RegisterRead( qspi_register_xfer_t *qspi_register_xfer, uint32_t *rx_data, uint8_t rx_data_length )

 Summary:
    Reads particular register of QSPI slave device.

 Description:
    This function can be used to read a particular register of QSPI slave device
    which has a command code associated to it.

 Precondition:
    QSPI_Initialize must have been called for the associated QSPI instance.

 Parameters:
    *qspi_register_xfer - pointer to QSPI register transfer structure holding the instruction
    code register and instruction frame register information.

    *rx_data - Pointer to receive buffer where the register data will be stored.

    rx_data_length - Register width in bytes.

 Returns:
    True on transfer request success.
    False on transfer request failure.

 Example:
    <code>

        #define READ_STATUS_REG_CODE 0x05

        static qspi_register_xfer_t qspi_register_xfer;
        static uint8_t reg_data;

        //Initialize QSPI
        QSPI_Initialize();

        // Use QAUD SPI Lane
        qspi_register_xfer.width = QUAD_CMD;
        qspi_register_xfer.dummy_cycles = 2;

        // Read status register of 1 Byte width
        qspi_register_xfer.instruction = READ_STATUS_REG_CODE;

        if (TRUE != QSPI_RegisterRead(&qspi_register_xfer, (uint32_t *)&reg_data, 1))
        {
            // Handle Error
        }

    </code>
*/
bool QSPI_RegisterRead( qspi_register_xfer_t *qspi_register_xfer, uint32_t *rx_data, uint8_t rx_data_length );

/* Function:
    bool QSPI_RegisterWrite( qspi_register_xfer_t *qspi_register_xfer, uint32_t *tx_data, uint8_t tx_data_length )

 Summary:
    Writes to particular register of QSPI slave device.

 Description:
    This function can be used to write to a particular register of QSPI slave device
    which has a command code associated to it.

 Precondition:
    QSPI_Initialize must have been called for the associated QSPI instance.

    Write enable command has to be sent before write register request and

 Parameters:
    *qspi_register_xfer - pointer to QSPI register transfer structure holding the instruction
    code register and instruction frame register information.

    *tx_data - Pointer to transmit buffer holding the data to write into register.

    tx_data_length - Register width in bytes.

 Returns:
    True on transfer request success.
    False on transfer request failure.

 Example:
    <code>

        #define WRITE_ENABLE_CODE     0x06
        #define WRITE_STATUS_REG_CODE 0x01
        #define READ_STATUS_REG_CODE  0x05

        #define QUAD_ENABLE_BIT       (1 << 1)

        static qspi_command_xfer_t qspi_command_xfer;
        static qspi_register_xfer_t qspi_register_xfer;
        static uint8_t reg_data;

        //Initialize QSPI
        QSPI_Initialize();

        // Use QAUD SPI Lane
        qspi_register_xfer.width = QUAD_CMD;
        qspi_register_xfer.dummy_cycles = 2;

        // Read status register of 1 Byte width
        qspi_register_xfer.instruction = READ_STATUS_REG_CODE;

        if (TRUE != QSPI_RegisterRead(&qspi_register_xfer, (uint32_t *)&reg_data, 1))
        {
            // Handle Error
        }

        // Send Write enable command
        qspi_command_xfer.instruction = WRITE_ENABLE_CODE;

        // Use QAUD SPI Lane
        qspi_command_xfer.width = QUAD_CMD;

        if (TRUE != QSPI_CommandWrite(&qspi_command_xfer, 0))
        {
            // Handle Error
        }

        // Set Slave device in QUAD mode
        reg_data |= QUAD_ENABLE_BIT;

        qspi_register_xfer.width = QUAD_CMD;

        // Write status register of 1 Byte width
        qspi_register_xfer.instruction = WRITE_STATUS_REG_CODE;

        if (TRUE != QSPI_RegisterWrite(&qspi_register_xfer, (uint32_t *)&reg_data, 1))
        {
            // Handle Error
        }

    </code>
*/
bool QSPI_RegisterWrite( qspi_register_xfer_t *qspi_register_xfer, uint32_t *tx_data, uint8_t tx_data_length );

/* Function:
    bool QSPI_MemoryRead( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *rx_data, uint32_t rx_data_length, uint32_t address )

 Summary:
    Reads from the specified address of the serial flash device.

 Description:
    This function can be used to read n bytes of data from the specified address
    of the serial flash device connected as a QSPI slave.

 Precondition:
    QSPI_Initialize must have been called for the associated QSPI instance.

 Parameters:
    *qspi_memory_xfer - pointer to QSPI memory transfer structure holding the instruction
    code register and instruction frame register information.

    *rx_data - Pointer to receive buffer where the data read from memory will be stored.

    rx_data_length - number of bytes to read.

    address - Memory location to read from.

 Returns:
    True on transfer request success.
    False on transfer request failure.

 Example:
    <code>

        #define READ_MEMORY_CODE  0x0B

        static qspi_memory_xfer_t qspi_memory_xfer;
        static uint32_t buffer[4];
        uint32_t address = 0x0

        //Initialize QSPI
        QSPI_Initialize();

        // Read memory location starting from address 0x0
        qspi_memory_xfer.instruction = READ_MEMORY_CODE;

        // Use QAUD SPI Lane
        qspi_memory_xfer.width = QUAD_CMD;
        qspi_memory_xfer.dummy_cycles = 6;

        if (TRUE != QSPI_MemoryRead(&qspi_memory_xfer, buffer, sizeof(buffer), address))
        {
            // Handle Error
        }

    </code>
*/
bool QSPI_MemoryRead( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *rx_data, uint32_t rx_data_length, uint32_t address )

/* Function:
    bool QSPI_MemoryWrite( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *tx_data, uint32_t tx_data_length, uint32_t address )

 Summary:
    Writes to the specified address of the serial flash device.

 Description:
    This function can be used to write maximum of one page of data to the specified address
    of the serial flash device connected as a QSPI slave.
    If the number of bytes to written is greater than the page size then QSPI_WriteMemory API
    needs to be called multiple times.

 Precondition:
    QSPI_Initialize must have been called for the associated QSPI instance.

    Write enable command has to be sent before write memory request.

 Parameters:
    *qspi_memory_xfer - pointer to QSPI memory transfer structure holding the instruction
    code register and instruction frame register information.

    *tx_data - Pointer to transmit buffer holding the data to write into memory.

    tx_data_length - number of bytes to write.

    address - Memory location to write to.

 Returns:
    True on transfer request success.
    False on transfer request failure.

 Example:
    <code>

        #define WRITE_ENABLE_CODE     0x06
        #define WRITE_PAGE_CODE       0x02
        #define WRITE_IN_POGRESS      (1 << 0)

        static qspi_command_xfer_t qspi_command_xfer;
        static qspi_memory_xfer_t qspi_memory_xfer;
        static uint8_t buffer[256];
        uint32_t address = 0x0;

        //Initialize QSPI
        QSPI_Initialize();

        // Send Write enable command
        qspi_command_xfer.instruction = WRITE_ENABLE_CODE;

        // Use QAUD SPI Lane
        qspi_command_xfer.width = QUAD_CMD;

        if (TRUE != QSPI_CommandWrite(qspi_command_xfer, 0))
        {
            // Handle Error
        }

        for (int i = 0; i < 256; i++)
            buffer[i] = i;

        // Write to memory location starting from address 0x0
        qspi_memory_xfer.instruction = WRITE_PAGE_CODE;

        // Use QAUD SPI Lane
        qspi_memory_xfer.width = QUAD_CMD;

        if (TRUE != QSPI_MemoryWrite(&qspi_memory_xfer, buffer, sizeof(buffer), address))
        {
            // Handle Error
        }
        
        // Query the status register and wait until WIP bit is cleared.
        while(status_register_read() & WRITE_IN_POGRESS);

    </code>
*/
bool QSPI_MemoryWrite( qspi_memory_xfer_t *qspi_memory_xfer, uint32_t *tx_data, uint32_t tx_data_length, uint32_t address );

// DOM-IGNORE-BEGIN
#ifdef __cplusplus // Provide C++ Compatibility
}
#endif
// DOM-IGNORE-END

#endif /* PLIB_QSPI_H */
