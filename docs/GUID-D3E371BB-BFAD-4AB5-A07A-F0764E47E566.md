# SDHCx\_DmaSetup Function

**Parent topic:**[SD/MMC Host Controller \(SDHC\)](GUID-8769733F-B27A-4567-BE7D-7BEA8C76F05E.md)

**Parent topic:**[SD/MMC Host Controller \(SDHC\)](GUID-D440DD4B-CA37-46F4-A6AA-4D57D9DAEF97.md)

## C

```c

/* x = SDHC instance number (x is applicable only on devices with more than one instances of SDHC) */

void SDHCx_DmaSetup (
	uint8_t* buffer,
	uint32_t numBytes,
	SDHC_DATA_TRANSFER_DIR direction
)
```

## Summary

Sets up the DMA for data tranfers.

## Description

The client of the SDHC PLIB must set up the DMA before initiating a data<br />transfer.

## Precondition

SDHCx\_Initialize\(\) must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|buffer|Pointer to the read or write buffer \(depending on the direction argument\)|
|numBytes|Number of bytes to read or write|
|direction|Direction of the data transfer, SDHC\_DATA\_TRANSFER\_DIR\_READ or SDHC\_DATA\_TRANSFER\_DIR\_WRITE.|

## Returns

None.

## Example

```c
uint8_t readBuffer[512];
SDHC_DataTransferFlags transferFlags;

transferFlags.isDataPresent = true;
transferFlags.transferDir = SDHC_DATA_TRANSFER_DIR_READ;
transferFlags.transferType = SDHC_DATA_TRANSFER_TYPE_SINGLE;

// Set up the DMA to read 512 btyes of data
SDHC1_DmaSetup(readBuffer, 512, SDHC_DATA_TRANSFER_DIR_READ);

// Send command to read one block of data from SD card starting at block address 100
SDHC1_CommandSend(17, 100, SDHC_CMD_RESP_R1, transferFlags);
```

## Remarks

None.

