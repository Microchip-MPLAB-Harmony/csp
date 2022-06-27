# High Speed MultiMedia Card Interface \(HSMCI\)

The HSMCI PLIB provides low level APIs to configure and transfer data using HSMCI. The HSMCI PLIB supports default and high speed data transfer, 1-bit and 4-bit data bus configurations. The PLIB performs the transfers in non-blocking mode. Transfers involving a data stage are performed using ADMA.

**Using The Library**<br />The example code demonstrates sending a SD command to read a single block of data from the SD card. This example assumes that the SD card is already initialized by the application and is ready to accept read and write requests. The example application does not show the larger SD protocol required in order to communicate with the SD card.

```c
uint16_t cmd_error;
uint16_t data_error;
bool isCommandCompleted = false;
bool isDataCompleted = false;
uint8_t readBuffer[512];

static void HSMCI_TransferEventHandler(
        HSMCI_XFER_STATUS xferStatus,
        uintptr_t contextHandle
)
{
    if (xferStatus & HSMCI_XFER_STATUS_CMD_COMPLETED)
    {
        // Command transfer complete, read the command error status.
        cmd_error = HSMCI_CommandErrorGet();
        isCommandCompleted = true;
    }
    if (xferStatus & HSMCI_XFER_STATUS_DATA_COMPLETED)
    {
        // Data transfer complete, read the data error status.
        data_error = HSMCI_DataErrorGet();
        isDataCompleted = true;
    }
}

int main ( void )
{
    /* Initialize all modules */
    SYS_Initialize ( NULL );

    // Register event handler with the HSMCI PLIB. This is usually done once.
    HSMCI_CallbackRegister(HSMCI_TransferEventHandler, (uintptr_t) 0);

    HSMCI_DataTransferFlags transferFlags;

    transferFlags.isDataPresent  = true;
    transferFlags.transferDir = HSMCI_DATA_TRANSFER_DIR_READ;
    transferFlags.transferType = HSMCI_DATA_TRANSFER_TYPE_SINGLE;

    // Set the block size to 512 bytes
    HSMCI_BlockSizeSet(512);

    // Set the block count to 1
    HSMCI_BlockCountSet(1);

    // Set up the DMA to read 512 btyes of data
    HSMCI_DmaSetup(readBuffer, 512, HSMCI_DATA_TRANSFER_DIR_READ);

    // Send command to read one block of data from SD card starting at block address 100
    HSMCI_CommandSend(17, 100, HSMCI_CMD_RESP_R1, transferFlags);

    // Check the status of isCommandCompleted and isDataCompleted

    // Other tasks ..
}

```

**Library Interface**

High Speed MultiMedia Card Interface peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|HSMCI\_BusWidthSet|Configures the width of the data bus|
|HSMCI\_SpeedModeSet|Sets the bus speed|
|HSMCI\_BlockSizeSet|Sets the size of the one data block of transfer|
|HSMCI\_BlockCountSet|Sets the number of blocks to transfer|
|HSMCI\_IsCmdLineBusy|Returns the status of the command line|
|HSMCI\_IsDatLineBusy|Returns the status of the data line|
|HSMCI\_ClockSet|Sets the High Speed MultiMedia Card Interface clock frequency|
|HSMCI\_CommandErrorGet|Returns the errors associated with a command transfer|
|HSMCI\_DataErrorGet|Returns the errors associated with a data transfer|
|HSMCI\_ResponseRead|Reads the specified response register|
|HSMCI\_Initialize|Initializes the HSMCI peripheral and the internal data structures used by the peripheral library|
|HSMCI\_ModuleInit|Initializes the HSMCI peripheral|
|HSMCI\_CallbackRegister|This function allows a HSMCI PLIB client to set an event handler|
|HSMCI\_CommandSend|This function allows the client to send a SD command on the HSMCI interface|
|HSMCI\_DmaSetup|Sets up the DMA for data tranfers|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|HSMCI\_DATA\_TRANSFER\_TYPE|Enum|The enumeration lists single or multi block data transfer type|
|HSMCI\_DATA\_TRANSFER\_DIR|Enum|The enumeration lists the direction of the data transfer|
|HSMCI\_DataTransferFlags|Struct|The data structure is used by the client to provide information about the data trasnfer to the HSMCI PLIB|
|HSMCI\_ERROR\_FLAGS|Enum|The enumeration lists the possible error types for a command and data transfer|
|HSMCI\_BUS\_WIDTH|Enum|The enumeration lists the bus widths for the HSMCI bus|
|HSMCI\_SPEED\_MODE|Enum|The enumeration lists the bus widths for the HSMCI bus|
|HSMCI\_READ\_RESPONSE\_REG|Enum|The enumeration lists the response registers that can be read for a given command|
|HSMCI\_XFER\_STATUS|Enum|The enumeration lists the status of the transfer|
|HSMCI\_CALLBACK|Typedef|The prototype of the HSMCI callback function|
|HSMCI\_CMD\_ERROR|Macro|The macro is a bit wise OR of all the possible errors corresponding to a command transfer|

-   **[HSMCI\_SpeedModeSet Function](GUID-10EC2A79-E161-4D16-B395-1EC8E7247294.md)**  

-   **[HSMCI\_ResponseRead Function](GUID-E48DD992-650C-4562-BE47-4ADC165539E4.md)**  

-   **[HSMCI\_ModuleInit Function](GUID-4CD2F627-1E9E-4073-9EAD-A644DE1C2EA5.md)**  

-   **[HSMCI\_IsDatLineBusy Function](GUID-B71DCB4C-4AE6-43CA-AEC8-726C5D0CAF35.md)**  

-   **[HSMCI\_IsCmdLineBusy Function](GUID-BEC25B4C-79A7-45F5-8C11-DE7337C59A94.md)**  

-   **[HSMCI\_Initialize Function](GUID-9C096487-44ED-4781-A869-3F521F3D21D8.md)**  

-   **[HSMCI\_DmaSetup Function](GUID-87894B22-B84C-4EA0-B015-7D4A3F8F7BC3.md)**  

-   **[HSMCI\_DataErrorGet Function](GUID-D6ADC59A-275D-4622-BBE6-80C17FFC7129.md)**  

-   **[HSMCI\_CommandSend Function](GUID-FC1B3BB4-8BB2-42C6-B280-F6DD940759E8.md)**  

-   **[HSMCI\_CommandErrorGet Function](GUID-FF57DAFA-56C3-4AC4-A22B-D099C8E48B1B.md)**  

-   **[HSMCI\_ClockSet Function](GUID-4861AC7E-4CA5-4A4A-8D62-FFAC188D30C0.md)**  

-   **[HSMCI\_CallbackRegister Function](GUID-DB14C941-5A42-4BF3-9205-A970A1898095.md)**  

-   **[HSMCI\_BusWidthSet Function](GUID-BC7684D5-5B32-4F19-A031-67460C7BB726.md)**  

-   **[HSMCI\_BlockSizeSet Function](GUID-12A5CB25-A9A3-43C9-BCE7-F8073AC66AE4.md)**  

-   **[HSMCI\_BlockCountSet Function](GUID-92CFA299-748F-4706-BB4A-687D02F02997.md)**  

-   **[HSMCI\_XFER\_STATUS Enum](GUID-771A082F-5F54-4340-B86E-2EC30B53F14F.md)**  

-   **[HSMCI\_SPEED\_MODE Enum](GUID-5BB9C006-901A-411A-9926-E0B635B53CDB.md)**  

-   **[HSMCI\_READ\_RESPONSE\_REG Enum](GUID-294F3EA1-C7C1-482D-BC53-E852306489C4.md)**  

-   **[HSMCI\_ERROR\_FLAGS Enum](GUID-0B0E70C1-CC25-479E-8929-935C41C6D3DA.md)**  

-   **[HSMCI\_DataTransferFlags Struct](GUID-A9966FEF-E3AB-4469-A794-20F9F02FCE19.md)**  

-   **[HSMCI\_DATA\_TRANSFER\_TYPE Enum](GUID-8002C614-BBFC-4161-9DC9-1B7A8335E5EB.md)**  

-   **[HSMCI\_DATA\_TRANSFER\_DIR Enum](GUID-9B56AD28-C991-48BB-BAC2-433D7F013EBB.md)**  

-   **[HSMCI\_CMD\_ERROR Macro](GUID-AC9B7B69-B753-4409-8DBB-24442F1D30AC.md)**  

-   **[HSMCI\_CALLBACK Typedef](GUID-AE0533CD-5D16-408A-A672-12F07262A249.md)**  

-   **[HSMCI\_BUS\_WIDTH Enum](GUID-B7E9A0E0-0396-4722-8E69-8595CF1F51AF.md)**  


**Parent topic:**[SAM E70 S70 V70 V71 Peripheral Libraries](GUID-6E45C146-6F6D-452A-A2E2-228C3CC905D7.md)

