# Two-wire Interface - TWIHS

The TWIHS PLIB can be configured in master or slave mode.

**TWIHS master mode**

The TWIHS peripheral library supports the following TWIHS transfers:

Master Write: The master writes a block of data to the slave<br />Master Read: The master reads a block of data from the slave<br />Master Write/Read: The master writes and then reads back a block of data from slave.

The block of data is transferred in a non-blocking manner using a peripheral interrupt. Application can either use a callback or IsBusy API to check for completion of data transfer.

**TWIHS slave mode**

TWIHS slave PLIB can be configured with peripheral interrupt enabled or disabled. When peripheral interrupt is enabled, application must register a callback, to get notified of the TWIHS events such as address match, transmitter ready, receiver ready etc. When peripheral interrupt is disabled, PLIB provides APIs to read the interrupt status flags. Application can call this API to determine the TWIHS event and then use the ReadByte/WriteByte APIs to read/write over the TWIHS bus

*TWIHS Master mode*

```c
// Following code demonstrates TWIHS write operation using polling method

#define APP_SLAVE_ADDR 0x0057
#define NUM_BYTES      10

uint8_t myWriteData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!',};

int main(void)
{
	/* Initialize all modules */
    SYS_Initialize ( NULL );
	
    /* Write data to the TWIHS Slave */
    TWIHS1_Write(APP_SLAVE_ADDR, &myWriteData[0], NUM_BYTES);

    /* Poll and wait for the transfer to complete */
    while(TWIHS1_IsBusy());

    /* Check if any error occurred */
    if(TWIHS1_ErrorGet() == TWIHS_ERROR_NONE)
    {
        //Transfer is completed successfully
    }
    else
    {
        //Error occurred during transfer.
    }
	...
}
```

```c
// Following code demonstrates TWIHS write operation using callback method

#define APP_SLAVE_ADDR 0x0057
#define NUM_BYTES      10

uint8_t myWriteData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!',};

void TWIHS1_Callback(uintptr_t context)
{
    if(TWIHS1_ErrorGet() == TWIHS_ERROR_NONE)
    {
        //Transfer is completed successfully
    }
    else
    {
        //Error occurred during transfer.
    }
}

int main(void)
{
	/* Initialize all modules */
    SYS_Initialize ( NULL );
	
    /* Register Callback function */
    TWIHS1_CallbackRegister(TWIHS1_Callback, (uintptr_t)NULL);

    /* Submit Write Request */
    TWIHS1_Write(APP_SLAVE_ADDR, &myWriteData[0], NUM_BYTES);
	
	...
}
```

*TWIHS Slave mode*

This example uses the TWIHS peripheral library in slave mode and emulates an EEPROM of 512 bytes. There are two pages each of size 256 bytes. TWIHS slave expects two bytes of memory address from the TWIHS master and the memory address can range from 0x00 to 0x1FF.

```c
#define EEPROM_PAGE_SIZE_BYTES                  256
#define EEPROM_PAGE_SIZE_MASK                   0xFF
#define EEPROM_SIZE_BYTES                       512

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

void delay(uint32_t count)
{
    uint32_t i;
        
    for (i = 0; i < count; i++)
    {
        asm("NOP");asm("NOP");asm("NOP");asm("NOP");asm("NOP");asm("NOP");
        asm("NOP");asm("NOP");asm("NOP");asm("NOP");asm("NOP");asm("NOP");
        asm("NOP");asm("NOP");asm("NOP");asm("NOP");asm("NOP");asm("NOP");
        asm("NOP");asm("NOP");asm("NOP");asm("NOP");asm("NOP");asm("NOP");        
    }
}

bool APP_TWIHS_Callback ( TWIHS_SLAVE_TRANSFER_EVENT event, uintptr_t contextHandle )
{
    uint8_t rxByte;
    
    switch(event)
    {
        case TWIHS_SLAVE_TRANSFER_EVENT_ADDR_MATCH:
            if (eepromData.internalWriteInProgress == false)
            {                              
                /* Reset the indexes */
                eepromData.addrIndex = 0;
                eepromData.wrBufferIndex = 0;                
            }
            break;

        case TWIHS_SLAVE_TRANSFER_EVENT_RX_READY:
            
            rxByte = TWIHS0_ReadByte();
            
            if (eepromData.internalWriteInProgress == false)
            {
                /* Read the data sent by I2C Master */
                if (eepromData.addrIndex < 2)
                {
                    ((uint8_t*)&eepromData.currentAddrPtr)[eepromData.addrIndex++] = rxByte;
                }
                else
                {
                    eepromData.wrBuffer[(eepromData.wrBufferIndex & EEPROM_PAGE_SIZE_MASK)] = rxByte;
                    eepromData.wrBufferIndex++;
                }
            }
            break;

        case TWIHS_SLAVE_TRANSFER_EVENT_TX_READY:
            /* Provide the EEPROM data requested by the I2C Master */
            TWIHS0_WriteByte(EEPROM_EmulationBuffer[eepromData.currentAddrPtr++]);
            if (eepromData.currentAddrPtr >= EEPROM_SIZE_BYTES)
            {
                eepromData.currentAddrPtr = 0;
            }
            break;

        case TWIHS_SLAVE_TRANSFER_EVENT_TRANSMISSION_COMPLETE:
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
                
                /* Send NACK for next data packets from I2C master */
                TWIHS0_NACKDataPhase(true);
                
                eepromData.eepromCommand = EEPROM_CMD_WRITE;
            }
            break;
        default:
            break;
    }

    return true;
}

void EEPROM_StateMachine(void)
{
    switch(eepromData.eepromCommand)
    {
        case EEPROM_CMD_WRITE:
            memcpy(&EEPROM_EmulationBuffer[eepromData.wrAddr], &eepromData.wrBuffer[0], eepromData.nWrBytes);
            
            /* Simulate busy condition. NACK will be sent while application loops through the delay. */
            delay(10000);
            
            eepromData.internalWriteInProgress = false;
            eepromData.eepromCommand = EEPROM_CMD_IDLE;
            
            /* Internal write is not in progress. ACK the data packets. */
            TWIHS0_NACKDataPhase(false);
            
            break;
        case EEPROM_CMD_IDLE:
            /* Do nothing */
            break;
    }
}

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    eepromData.eepromCommand = EEPROM_CMD_IDLE;

    TWIHS0_CallbackRegister(APP_TWIHS_Callback, 0);

    while ( true )
    {
        EEPROM_StateMachine();
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
```

**Library Interface**

**Functions**

|Name|Description|Master mode|Slave mode \(interrupt disabled\)|Slave mode \(interrupt enabled\)|
|----|-----------|-----------|---------------------------------|--------------------------------|
|TWIHSx\_Initialize|Initializes the instance of the TWIHS peripheral in either master or slave mode|Yes|Yes|Yes|
|TWIHSx\_Read|Reads data from the TWIHS slave|Yes|No|No|
|TWIHSx\_Write|Writes data to the TWIHS slave|Yes|No|No|
|TWIHSx\_WriteRead|Write and Read data from Slave|Yes|No|No|
|TWIHSx\_IsBusy|Returns the peripheral busy status|Yes|No|Yes|
|TWIHSx\_ErrorGet|Returns the TWIHS error that occurred on the bus|Yes|No|No|
|TWIHSx\_TransferSetup|Dynamic setup of TWIHS Peripheral|Yes|No|No|
|TWIHSx\_CallbackRegister|Sets the pointer to the function \(and it's context\) to be called when the given TWIHS's transfer events occur|Yes|No|Yes|
|TWIHSx\_ReadByte|Read the received TWIHS byte|No|Yes|Yes|
|TWIHSx\_WriteByte|Write a data byte to TWIHS master|No|Yes|Yes|
|TWIHSx\_TransferDirGet|Returns the TWIHS transfer direction|No|Yes|Yes|
|TWIHSx\_LastByteAckStatusGet|Returns the ACK status of the last byte written to the TWIHS master|No|Yes|Yes|
|TWIHSx\_NACKDataPhase|Configures the hardware to send NAK for the next data phase|No|Yes|Yes|
|TWIHSx\_StatusGet|Returns the TWIHS hardware status flags|No|Yes|No|

**Data types and constants**

|Name|Type|Description|Master mode|Slave mode \(interrupt disabled\)|Slave mode \(interrupt enabled\)|
|----|----|-----------|-----------|---------------------------------|--------------------------------|
|TWIHS\_ERROR|Enum|Defines the possible errors that the TWIHS peripheral can generate in TWIHS master mode|Yes|No|No|
|TWIHS\_TRANSFER\_SETUP|Struct|TWIHS transfer setup data structure|Yes|No|No|
|TWIHS\_CALLBACK|Typedef|Defines the data type and function signature for the TWIHS peripheral callback function in master mode|Yes|No|No|
|TWIHS\_SLAVE\_TRANSFER\_DIR|Enum|Defines the enum for TWIHS data transfer direction|No|Yes|Yes|
|TWIHS\_SLAVE\_ACK\_STATUS|Enum|Defines the enum for the TWIHS acknowledgement|No|Yes|Yes|
|TWIHS\_SLAVE\_TRANSFER\_EVENT|Enum|Defines the enum for the TWIHS slave transfer event|No|No|Yes|
|TWIHS\_SLAVE\_CALLBACK|Typedef|Defines the data type and function signature for the TWIHS Slave callback function|No|No|Yes|
|TWIHS\_SLAVE\_STATUS\_FLAG|Enum|Defines the list of possible TWIHS slave events|No|Yes|No|

-   **[TWIHSx\_WriteRead Function](GUID-1588E6D4-5193-457B-9F5C-93AFC774C4B0.md)**  

-   **[TWIHSx\_WriteByte Function](GUID-DCC76F54-3D40-4F0E-9645-79C4DAC2D241.md)**  

-   **[TWIHSx\_Write Function](GUID-CD98FEC3-1AC7-40EA-93F7-FB7360CE0862.md)**  

-   **[TWIHSx\_TransferSetup Function](GUID-245E08D3-2877-4851-8D3A-42E5E8E72620.md)**  

-   **[TWIHSx\_TransferDirGet Function](GUID-E14A1E9F-1D96-4B65-BBEA-203729659655.md)**  

-   **[TWIHSx\_StatusGet Function](GUID-2485327D-7553-4E78-9C5C-00AC73D01E5E.md)**  

-   **[TWIHSx\_ReadByte Function](GUID-7F759331-B5A5-40BA-990B-EDAE29A1CE3D.md)**  

-   **[TWIHSx\_Read Function](GUID-FE940BEE-D4A2-4214-918E-67F953C50946.md)**  

-   **[TWIHSx\_NACKDataPhase Function](GUID-FB397B29-7393-4947-B9ED-DFAA2FB12990.md)**  

-   **[TWIHSx\_LastByteAckStatusGet Function](GUID-490C2897-FAA4-4A27-B4AB-62761F5923E7.md)**  

-   **[TWIHSx\_IsBusy Function](GUID-50C44E31-E503-48C6-B076-F0A6BFD7B756.md)**  

-   **[TWIHSx\_Initialize Function](GUID-C0EDAFCF-E60F-4951-B457-D24FF59172CB.md)**  

-   **[TWIHSx\_ErrorGet Function](GUID-9EC2F47E-127D-4EFC-B01C-C50F9292BCF4.md)**  

-   **[TWIHSx\_CallbackRegister Function](GUID-5439E7AD-429C-419A-94A9-952B64B733F2.md)**  

-   **[TWIHS\_TRANSFER\_SETUP Struct](GUID-127489D2-8C92-4A4B-BEE9-9C72B4FB0383.md)**  

-   **[TWIHS\_SLAVE\_TRANSFER\_EVENT Enum](GUID-52331BA0-279E-4A79-87BD-52AB32289277.md)**  

-   **[TWIHS\_SLAVE\_TRANSFER\_DIR Enum](GUID-6B800F98-3CFB-449A-8786-CE188F3DF337.md)**  

-   **[TWIHS\_SLAVE\_STATUS\_FLAG Enum](GUID-CA062E31-5AB5-479F-8FB2-9CE861401616.md)**  

-   **[TWIHS\_SLAVE\_CALLBACK Typedef](GUID-FF44E414-7FCC-4ADB-82E5-3A4453F7BBF4.md)**  

-   **[TWIHS\_SLAVE\_ACK\_STATUS Enum](GUID-87AA2424-60DF-4106-B157-75EDCC6A4C16.md)**  

-   **[TWIHS\_ERROR Enum](GUID-8346097D-A3E7-4DEF-B510-11E34B5FFCA1.md)**  

-   **[TWIHS\_CALLBACK Typedef](GUID-DC896EB8-3E13-4FA0-9DF8-4B9603C2985E.md)**  


**Parent topic:**[SAM A5D2 Peripheral Libraries](GUID-F6605EDC-FC71-4081-8560-0C1681C1FA8D.md)

**Parent topic:**[SAM E70 S70 V70 V71 Peripheral Libraries](GUID-6E45C146-6F6D-452A-A2E2-228C3CC905D7.md)

**Parent topic:**[SAM G51 G53 G54 Peripheral Libraries](GUID-E97B8116-033B-411A-925B-E8E6252A1E15.md)

