# Inter-Integrated Circuit - I2C

The I2C PLIB can be configured in master or slave mode.

**I2C master mode**<br />The I2C peripheral library supports the following I2C transfers:

Master Write: The master writes a block of data to the slave<br />Master Read: The master reads a block of data from the slave<br />Master Write/Read: The master writes and then reads back a block of data from slave.

Additionally, a forced write API allows writes even if the address or data is NACKed by the slave.

The block of data is transferred in a non-blocking manner using a peripheral interrupt. Application can either use a callback or IsBusy API to check for completion of data transfer.

**I2C slave mode**

I2C slave PLIB works with peripheral interrupt enabled. Application must register a callback, to get notified of the I2C events such as address match, transmitter ready, receiver ready etc.

*I2C Master mode*

```c
// Following code demonstrates I2C write operation using polling method

#define APP_SLAVE_ADDR 0x0057
#define NUM_BYTES      10

uint8_t myWriteData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!',};

int main(void)
{
	/* Initialize all modules */
    SYS_Initialize ( NULL );
	
    /* Write data to the I2C Slave */
    I2C1_Write(APP_SLAVE_ADDR, &myWriteData[0], NUM_BYTES);

    /* Poll and wait for the transfer to complete */
    while(I2C1_IsBusy());

    /* Check if any error occurred */
    if(I2C1_ErrorGet() == I2C_ERROR_NONE)
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
// Following code demonstrates I2C write operation using callback method

#define APP_SLAVE_ADDR 0x0057
#define NUM_BYTES      10

uint8_t myWriteData [NUM_BYTES] = {'1', '0', ' ', 'B', 'Y', 'T', 'E', 'S', '!', '!',};

void I2C1_Callback(uintptr_t context)
{
    if(I2C1_ErrorGet() == I2C_ERROR_NONE)
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
    I2C1_CallbackRegister(I2C1_Callback, (uintptr_t)NULL);

    /* Submit Write Request */
    I2C1_Write(APP_SLAVE_ADDR, &myWriteData[0], NUM_BYTES);
	
	...
}
```

*I2C Slave mode*

This example uses the I2C peripheral library in slave mode and emulates an EEPROM of 512 bytes. There are two pages each of size 256 bytes. I2C slave expects two bytes of memory address from the I2C master and the memory address can range from 0x00 to 0x1FF.

```c
#define EEPROM_PAGE_SIZE_BYTES                  256
#define EEPROM_PAGE_SIZE_MASK                   0xFF
#define EEPROM_SIZE_BYTES                       512

// *****************************************************************************
// *****************************************************************************
// Section: Main Entry Point
// *****************************************************************************
// *****************************************************************************

typedef struct
{
    /* currentAddrPtr - to allow for sequential read (from the current address) */
    uint16_t                    currentAddrPtr;
    /* addrIndex - used to copy 2 bytes of EEPROM memory address */
    uint8_t                     addrIndex;        
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

bool APP_I2C_SLAVE_Callback ( I2C_SLAVE_TRANSFER_EVENT event, uintptr_t contextHandle )
{
    bool isSuccess = true;

    switch(event)
    {
        case I2C_SLAVE_TRANSFER_EVENT_ADDR_MATCH:
            
            /* Reset the index. MSB address is sent first followed by LSB. */
            eepromData.addrIndex = 2;
            
            break;

        case I2C_SLAVE_TRANSFER_EVENT_RX_READY:
            /* Read the data sent by I2C Master */
            if (eepromData.addrIndex > 0)
            {
                ((uint8_t*)&eepromData.currentAddrPtr)[--eepromData.addrIndex] = I2C1_ReadByte();
            }
            else
            {
                EEPROM_EmulationBuffer[eepromData.currentAddrPtr++] = I2C1_ReadByte();
                
                /* If exceeding the page boundary, rollover to the start of the page */
                if ((eepromData.currentAddrPtr % EEPROM_PAGE_SIZE_BYTES) == 0)
                {
                    eepromData.currentAddrPtr -= EEPROM_PAGE_SIZE_BYTES;
                }                                                              
            }
            break;

        case I2C_SLAVE_TRANSFER_EVENT_TX_READY:
            
            /* Provide the EEPROM data requested by the I2C Master */
            I2C1_WriteByte(EEPROM_EmulationBuffer[eepromData.currentAddrPtr++]);
            if (eepromData.currentAddrPtr >= EEPROM_SIZE_BYTES)
            {
                eepromData.currentAddrPtr = 0;
            }
            break;
        
        default:
            break;
    }

    return isSuccess;
}

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    I2C1_CallbackRegister(APP_I2C_SLAVE_Callback, 0);

    while ( true )
    {
        
    }

    /* Execution should not come here during normal operation */

    return ( EXIT_FAILURE );
}
```

**Library Interface**

**I2C Mode**

**Functions**

|Name|Description|Master mode|Slave mode|
|----|-----------|-----------|----------|
|I2Cx\_Initialize|Initializes the instance of the I2C peripheral in either master or slave mode|Yes|Yes|
|I2Cx\_Read|Reads data from the slave|Yes|No|
|I2Cx\_Write|Writes data to the slave|Yes|No|
|I2Cx\_WriteRead|Write and Read data from Slave|Yes|No|
|I2Cx\_WriteForced|Forced write data to the slave|Yes|No|
|I2Cx\_IsBusy|Returns the Peripheral busy status|Yes|Yes|
|I2Cx\_ErrorGet|Returns the I2C error that occurred on the bus|Yes|Yes|
|I2Cx\_TransferSetup|Dynamic setup of I2C Peripheral|Yes|No|
|I2Cx\_CallbackRegister|Sets the pointer to the function \(and it's context\) to be called when the given I2C's transfer events occur|Yes|Yes|
|I2Cx\_ReadByte|Read the received I2C byte|No|Yes|
|I2Cx\_WriteByte|Write a data byte to I2C master|No|Yes|
|I2Cx\_TransferDirGet|Returns the I2C transfer direction|No|Yes|
|I2Cx\_LastByteAckStatusGet|Returns the ACK status of the last byte written to the I2C master|No|Yes|

**Data types and constants**

|Name|Type|Description|Master mode|Slave mode|
|----|----|-----------|-----------|----------|
|I2C\_ERROR|Enum|Defines the possible errors that the I2C peripheral can generate in I2C master mode|Yes|No|
|I2C\_TRANSFER\_SETUP|Struct|I2C transfer setup data structure|Yes|No|
|I2C\_CALLBACK|Typedef|Defines the data type and function signature for the I2C peripheral callback function in I2C master mode|Yes|No|
|I2C\_SLAVE\_TRANSFER\_DIR|Enum|Defines the enum for I2C data transfer direction|No|Yes|
|I2C\_SLAVE\_ACK\_STATUS|Enum|Defines the enum for the I2C acknowledgement|No|Yes|
|I2C\_SLAVE\_TRANSFER\_EVENT|Enum|Defines the enum for the I2C slave transfer event|No|Yes|
|I2C\_SLAVE\_ERROR|Enum|Defines errors associated with I2C in slave mode|No|Yes|
|I2C\_SLAVE\_CALLBACK|Typedef|Defines the data type and function signature for the I2C Slave callback function|No|Yes|

-   **[I2Cx\_WriteRead Function](GUID-FBA8FDDD-907E-4B06-9D9F-021A5530F32F.md)**  

-   **[I2Cx\_WriteForced Function](GUID-496FE450-EDD6-4323-888C-BABF3238A7C8.md)**  

-   **[I2Cx\_WriteByte Function](GUID-2DC5C5E3-FED9-42AC-B5EA-659A88077205.md)**  

-   **[I2Cx\_Write Function](GUID-5D4C9415-8501-4593-85CC-8488CC514814.md)**  

-   **[I2Cx\_TransferSetup Function](GUID-D92C4882-1149-434A-8CA3-44F2A85F13F5.md)**  

-   **[I2Cx\_TransferDirGet Function](GUID-2B5F31EE-587B-4523-B7B8-C43D6A49311B.md)**  

-   **[I2Cx\_ReadByte Function](GUID-491ECC89-EB7A-471D-A073-4BC5B775DA65.md)**  

-   **[I2Cx\_Read Function](GUID-E11AE6CF-61D6-4C02-A707-BFF7B5DBAB3D.md)**  

-   **[I2Cx\_LastByteAckStatusGet Function](GUID-3A64D00B-536E-44B1-9750-AF28E20441BA.md)**  

-   **[I2Cx\_IsBusy Function](GUID-2280CFF4-E980-4BE0-B09A-B0FE51C0AEE6.md)**  

-   **[I2Cx\_Initialize Function](GUID-5ACE267C-EC6E-4B89-900C-B012624CFFCF.md)**  

-   **[I2Cx\_ErrorGet Function](GUID-ECB8E3CE-22EA-436A-A1FA-B20C82F1A74E.md)**  

-   **[I2Cx\_CallbackRegister Function](GUID-5DF92459-D2AF-4816-A7D8-0B8125B6E97F.md)**  

-   **[I2C\_TRANSFER\_SETUP Struct](GUID-7C648D00-87F9-4D1D-907C-4547F1CCE468.md)**  

-   **[I2C\_SLAVE\_TRANSFER\_EVENT Enum](GUID-DE9BC9E4-A5B3-4BE0-8561-ED89D0F988FE.md)**  

-   **[I2C\_SLAVE\_TRANSFER\_DIR Enum](GUID-200D448E-1132-42FE-884E-1524562F47EE.md)**  

-   **[I2C\_SLAVE\_ERROR Enum](GUID-890CFA36-5C7D-4FF1-AC83-9FC3DC4FE429.md)**  

-   **[I2C\_SLAVE\_CALLBACK Typedef](GUID-9F830AB9-8AB1-4127-85C5-F4A49675240D.md)**  

-   **[I2C\_SLAVE\_ACK\_STATUS Enum](GUID-2368E833-B37F-44B1-9459-D557E62A40DE.md)**  

-   **[I2C\_ERROR Enum](GUID-984093D9-F83F-4A40-8161-6656569DE9F1.md)**  

-   **[I2C\_CALLBACK Typedef](GUID-FD05FB9D-B104-4ACB-AA06-1DBECF02EA70.md)**  


**Parent topic:**[PIC32MK GPG MCJ Peripheral Libraries](GUID-A0350A48-03F7-4370-A6C5-612386A4ABAC.md)

**Parent topic:**[PIC32MK GPK MCM Peripheral Libraries](GUID-801B9DE7-4616-4E38-BF86-C82B78A4F430.md)

**Parent topic:**[PIC32MK MCA Peripheral Libraries](GUID-E11C5899-DD12-4B78-8076-8A415C20F144.md)

**Parent topic:**[PIC32MM GPM Peripheral Libraries](GUID-CB22E113-2DFF-40FB-BA9B-BFA1C8003FEC.md)

**Parent topic:**[PIC32MZ DA Peripheral Libraries](GUID-02A4B196-FE06-48DB-BC12-D3A68B6D983E.md)

**Parent topic:**[PIC32MZ EF Peripheral Libraries](GUID-F47955F5-89DE-43B0-8C2C-DE0070EBA152.md)

**Parent topic:**[PIC32MZ W1 Peripheral Libraries](GUID-EBD28D67-7F6E-46D1-9ABE-2BDE1973D143.md)

