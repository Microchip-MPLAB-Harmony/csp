# SPIx\_Write Function

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-246C53F6-3912-4437-AEC8-C2262CEF3EF6.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-CBD5BFEF-57AB-4CA0-92C0-00CB1A72D686.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-84F93473-4002-4DDD-A28F-9BF9DB6B7C3E.md)

## C

```c
/* x = SPI instance number */

/* SPI master mode */
bool SPIx_Write(void* pWrBuffer, size_t txSize)		
```

```c
/* x = SPI instance number */

/* SPI slave mode */
size_t SPIx_Write(void* pWrBuffer, size_t txSize )			
```

## Summary

Writes data to SPI peripheral

## Description

*SPI master mode*

This function writes "txSize" number of bytes on SPI module. Data pointed by pWrBuffer is transmitted. When interrupt is disabled, this function will be blocking in nature. In this mode, the function will not return until all the requested data is transferred. The function returns true after transferring all the data. This indicates that the operation has been completed. When interrupt is enabled, the function will be non-blocking in nature. The function returns immediately. The data transfer process continues in the peripheral interrupt. The application specified transmit buffer is owned by the library until the data transfer is complete and should not be modified by the application till the transfer is complete. Only one transfer is allowed at any time. The application can use a callback function or a polling function to check for completion of the transfer. If a callback is required, this should be registered prior to calling the SPIx\_Write\(\) function. The application can use the SPIx\_IsBusy\(\) to poll for completion of transfer.

*SPI slave mode*

This function writes "txSize" number of bytes on SPI module. Data pointed by pWrBuffer is transmitted. This function returns immediately after copying the data pointed by pWrBuffer into the PLIB's internal buffer. The actual data transfer happens when a SPI transfer is initiated by the SPI master. Upon completion a callback is given to the application.

## Precondition

The SPIx\_Initialize function must have been called.

*SPI master mode*

Callback can be registered using SPIx\_CallbackRegister API if the PLIB is configured in Interrupt mode and transfer completion status needs to be communicated back to application via callback.

*SPI slave mode*

Callback must have been registered using SPIx\_CallbackRegister API to get notified when the transfer is complete.

## Parameters

*SPI master mode*

|Param|Description|
|-----|-----------|
|pWrBuffer|Pointer to the buffer containing the data which has to betransmitted. In "Interrupt Mode", this buffer should not be modified after calling the function and before the callback function has been called or the SPIx\_IsBusy\(\) function returns false.|
|txSize|Number of bytes to be transmitted. This value is the byte size of the buffer irrespective of 8/16/32 bit transfer mode.|

*SPI slave mode*

|Param|Description|
|-----|-----------|
|pWrBuffer|Pointer to the buffer where the data must be copied to the PLIB's internal buffer|
|txSize|Number of bytes to copy. If 16/32 bit modes are supported, the rxSize must be specified in terms of 16/32 bit words.|

## Returns

*SPI master mode*

*true* - If configured for Non-interrupt mode, the function has transmitted the requested number of bytes. If configured for Interrupt mode, the request was accepted successfully and will be processed in the interrupt.

*false* - If pWrBuffer is NULL or txSize is 0. In Interrupt mode, the function will additionally return false if there is an on-going data transfer at the time of calling the function.

*SPI slave mode*

Returns the number of bytes actually copied from the pWrBuffer. If 16/32 bit modes are supported, the return value is specified in terms of 16/32 bit words.

## Example

*SPI master mode*

```c
uint8_t txBuffer[4];
size_t txSize = 4;

void APP_SPITransferHandler(uintptr_t context)
{
    //Transfer was completed without error, do something else now.
}

SPI1_Initialize();
SPI1_CallbackRegister(&APP_SPITransferHandler, (uintptr_t)NULL);
if(SPI1_Write(&txBuffer, txSize))
{
    // request got accepted
}
else
{
    // request didn't get accepted, try again later with correct arguments
}

```

*SPI slave mode*

```c
uint8_t APP_TxData[4];
uint8_t APP_RxData[10];
size_t txSize = 4;

void SPIEventHandler(uintptr_t context )
{
    if (SPI1_ErrorGet() == SPI_SLAVE_ERROR_NONE)
    {
        // Read out the received data. This could be meaningful data if SPI master is
        // writing to slave or it could be dummy data if SPI master is reading from slave.
        // However, irrespective of whether slave is expecting meaningful data or dummy
        // data from master, SPI slave must always read out the data to clear the PLIB's
        // internal receive buffer.

        appData.nBytesRead = SPI1_Read(APP_RxData, SPI1_ReadCountGet());
    }
    else
    {
        // Handle error
    }

}

SPI1_CallbackRegister(SPIEventHandler, (uintptr_t) 0);
SPI1_Write(APP_TxData, txSize);
```

## Remarks

*SPI slave mode*

This function returns immediately. Application must register a callback to get notified, when the data transfer is complete. A data transfer is considered as complete, when the Chip Select line is driven to inactive state by the SPI master.

