# SD/MMC Host Controller \(SDHC\)

The SDHC PLIB provides low level APIs to configure and transfer data using the SD host controller. The SDHC PLIB supports default and high speed data transfer, 1-bit and 4-bit data bus configurations. The PLIB performs the transfers in non-blocking mode. Transfers involving a data stage are performed using ADMA.

**Using The Library**

The example code demonstrates sending a SD command to read a single block of data from the SD card. This example assumes that the SD card is already initialized by the application and is ready to accept read and write requests. The example application does not show the larger SD protocol required in order to communicate with the SD card.

```c

uint16_t cmd_error;
uint16_t data_error;
bool isCommandCompleted = false;
bool isDataCompleted = false;
uint8_t readBuffer[512];

static void SDHC_TransferEventHandler(
        SDHC_XFER_STATUS xferStatus,
        uintptr_t contextHandle
)
{
    if (xferStatus & SDHC_XFER_STATUS_CMD_COMPLETED)
    {
        // Command transfer complete, read the command error status.
        cmd_error = SDHC1_CommandErrorGet();
        isCommandCompleted = true;
    }
    if (xferStatus & SDHC_XFER_STATUS_DATA_COMPLETED)
    {
        // Data transfer complete, read the data error status.
        data_error = SDHC1_DataErrorGet();
        isDataCompleted = true;
    }
}

int main(void)
{
	/* Initialize all modules */
    SYS_Initialize ( NULL );
	
    // Register event handler with the SDHC PLIB. This is usually done once.
    SDHC1_CallbackRegister(SDHC_TransferEventHandler, (uintptr_t) 0);

    SDHC_DataTransferFlags transferFlags;

    transferFlags.isDataPresent  = true;
    transferFlags.transferDir = SDHC_DATA_TRANSFER_DIR_READ;
    transferFlags.transferType = SDHC_DATA_TRANSFER_TYPE_SINGLE;

    // Set the block size to 512 bytes
    SDHC1_BlockSizeSet(512);

    // Set the block count to 1
    SDHC1_BlockCountSet(1);

    // Set up the DMA to read 512 btyes of data
    SDHC1_DmaSetup(readBuffer, 512, SDHC_DATA_TRANSFER_DIR_READ);

    // Send command to read one block of data from SD card starting at block address 100
    SDHC1_CommandSend(17, 100, SDHC_CMD_RESP_R1, transferFlags);

    // Check the status of isCommandCompleted and isDataCompleted

    // Other tasks ...
}

```

**Library Interface**

SDHC peripheral library provides the following interfaces:

**Functions**

|Name|Description|
|----|-----------|
|SDHCx\_BusWidthSet|Configures the width of the data bus|
|SDHCx\_SpeedModeSet|Sets the bus speed|
|SDHCx\_BlockSizeSet|Sets the size of the one data block of transfer|
|SDHCx\_BlockCountSet|Sets the number of blocks to transfer|
|SDHCx\_IsCmdLineBusy|Returns the status of the command line|
|SDHCx\_IsDatLineBusy|Returns the status of the data line|
|SDHCx\_IsWriteProtected|Returns the write protect switch pin level|
|SDHCx\_IsCardAttached|Indicates if the card is attached or detached|
|SDHCx\_ClockSet|Sets the SDHC clock frequency|
|SDHCx\_ClockEnable|Enable SDHC clock|
|SDHCx\_ClockDisable|Disable SDHC clock|
|SDHCx\_CommandErrorGet|Returns the errors associated with a command transfer|
|SDHCx\_DataErrorGet|Returns the errors associated with a data transfer|
|SDHCx\_ErrorReset|Resets errors as specified by the resetType|
|SDHCx\_ResponseRead|Reads the response to a given command|
|SDHCx\_ModuleInit|Initializes the SDHC peripheral|
|SDHCx\_Initialize|Initializes the SDHC peripheral and the internal data structures used by the peripheral library|
|SDHCx\_CallbackRegister|This function allows a SDHC PLIB client to set an event handler|
|SDHCx\_CommandSend|This function allows the client to send a SD command on the SDHC interface|
|SDHCx\_DmaSetup|Sets up the DMA for data tranfers|

**Data types and constants**

|Name|Type|Description|
|----|----|-----------|
|SDHC\_BUS\_WIDTH|Enum|The enumeration lists the bus widths for the SDHC bus|
|SDHC\_SPEED\_MODE|Enum|The enumeration lists the bus widths for the SDHC bus|
|SDHC\_CMD\_RESP\_TYPE|Enum|The enumeration lists the supported response types|
|SDHC\_READ\_RESPONSE\_REG|Enum|The enumeration lists the response registers that can be read for a given command|
|SDHC\_RESET\_TYPE|Enum|The enumeration lists error type to reset|
|SDHC\_CLK\_MODE|Enum|The enumeration lists the clock modes|
|SDHC\_XFER\_STATUS|Enum|The enumeration lists the status of the transfer|
|SDHC\_DATA\_TRANSFER\_TYPE|Enum|The enumeration lists single or multi block data transfer type|
|SDHC\_DATA\_TRANSFER\_DIR|Enum|The enumeration lists the direction of the data transfer|
|SDHC\_DataTransferFlags|Struct|The data structure is used by the client to provide information about the data trasnfer to the SDHC PLIB|
|SDHC\_CALLBACK|Typedef|The prototype of the SDHC callback function|

-   **[SDHCx\_SpeedModeSet Function](GUID-2FC470AF-8A80-4C0F-BC87-FD4630E0212F.md)**  

-   **[SDHCx\_ResponseRead Function](GUID-1F010F1A-FA73-4834-BCE5-537C96701F22.md)**  

-   **[SDHCx\_ModuleInit Function](GUID-46D868ED-CF04-4512-8176-1FF8BB7DFCDE.md)**  

-   **[SDHCx\_IsWriteProtected Function](GUID-E197506D-09EC-4AA3-BFE3-9E1732E738EB.md)**  

-   **[SDHCx\_IsDatLineBusy Function](GUID-6AA3C336-24FC-4A01-B8C3-62570D189962.md)**  

-   **[SDHCx\_IsCmdLineBusy Function](GUID-DB807161-E023-4300-A51C-BB373A715DB6.md)**  

-   **[SDHCx\_IsCardAttached Function](GUID-77E2AD88-D01E-41BE-8776-62B3DB8A21E7.md)**  

-   **[SDHCx\_Initialize Function](GUID-DAFC2F65-9408-47FE-A7E1-1048BD7E5672.md)**  

-   **[SDHCx\_ErrorReset Function](GUID-EB09C95E-D99A-4B1F-991F-7893C2DE73F7.md)**  

-   **[SDHCx\_DmaSetup Function](GUID-D3E371BB-BFAD-4AB5-A07A-F0764E47E566.md)**  

-   **[SDHCx\_DataErrorGet Function](GUID-CBA52C7F-690D-4D66-8993-785405B59F71.md)**  

-   **[SDHCx\_CommandSend Function](GUID-A7AF7D64-32F3-4649-975B-8D5930CED530.md)**  

-   **[SDHCx\_CommandErrorGet Function](GUID-FE068C8F-25D6-46D1-BAF3-4BE0C8F4F196.md)**  

-   **[SDHCx\_ClockSet Function](GUID-0F2C2A97-459D-4FC7-87B4-62EDB28EDDEF.md)**  

-   **[SDHCx\_ClockEnable Function](GUID-EDE7C6FC-3B60-4C09-BF10-BDABBB550458.md)**  

-   **[SDHCx\_ClockDisable Function](GUID-55203009-3FE1-479D-809D-E428CCB61BE5.md)**  

-   **[SDHCx\_CallbackRegister Function](GUID-61713F6C-A9A4-4706-B6C0-A5FEFB4D7793.md)**  

-   **[SDHCx\_BusWidthSet Function](GUID-269F8EFA-7A1F-4D11-A9E0-2BD8F4037703.md)**  

-   **[SDHCx\_BlockSizeSet Function](GUID-274281BC-9508-49F1-BFEB-A0C5EDDFC192.md)**  

-   **[SDHCx\_BlockCountSet Function](GUID-4CDA2387-720C-4540-AE36-7A266733359C.md)**  

-   **[SDHC\_XFER\_STATUS Enum](GUID-63680A80-BA0D-4C0A-905E-D62664A41016.md)**  

-   **[SDHC\_SPEED\_MODE Enum](GUID-4966EE4D-A6AC-4C12-90F4-068E6233472D.md)**  

-   **[SDHC\_RESET\_TYPE Enum](GUID-91797D74-A6ED-4D59-ADBB-C4B5AFCDC346.md)**  

-   **[SDHC\_READ\_RESPONSE\_REG Enum](GUID-21C1E828-1D86-4ECD-B9DD-55107A902555.md)**  

-   **[SDHC\_DataTransferFlags Struct](GUID-08563E5F-059C-42F4-9E03-E2B3ACB42A32.md)**  

-   **[SDHC\_DATA\_TRANSFER\_TYPE Enum](GUID-9746CCD0-D8E5-493D-BAD5-D61DFF3AB2F0.md)**  

-   **[SDHC\_DATA\_TRANSFER\_DIR Enum](GUID-C6B4B5E4-BF2B-4193-9AF3-6EE712FDCA50.md)**  

-   **[SDHC\_CMD\_RESP\_TYPE Enum](GUID-D08BB7D1-3399-4037-9B57-49610C8428BD.md)**  

-   **[SDHC\_CLK\_MODE Enum](GUID-8D59FCA2-F5A7-45DA-85EB-56294660C4BA.md)**  

-   **[SDHC\_CALLBACK Typedef](GUID-37CA6E97-F81B-4D6A-8F5C-ADDE7E1A4401.md)**  

-   **[SDHC\_BUS\_WIDTH Enum](GUID-9401F8C8-1D57-48E5-B6CC-512E56864634.md)**  


**Parent topic:**[SAM D51 E51 E53 E54 Peripheral Libraries](GUID-E33B93DD-6680-477E-AA96-966208DC9A50.md)

