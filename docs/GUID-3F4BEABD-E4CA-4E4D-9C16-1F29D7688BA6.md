# SPIx\_WriteRead Function

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-246C53F6-3912-4437-AEC8-C2262CEF3EF6.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-CBD5BFEF-57AB-4CA0-92C0-00CB1A72D686.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-84F93473-4002-4DDD-A28F-9BF9DB6B7C3E.md)

## C

```c
/* x = SPI instance number */

/* SPI master mode */

bool SPIx_WriteRead ( void* pTransmitData, size_t txSize, void* pReceiveData, size_t rxSize)
```

## Summary

Write and Read data on SPI peripheral.

## Description

This function transmits "txSize" number of bytes and receives "rxSize" number of bytes on SPI module. Data pointed by pTransmitData is transmitted and received data is saved in the location pointed by pReceiveData. The function will transfer the maximum of "txSize" or "rxSize" data units towards completion.

When interrupt is disabled, this function will be blocking in nature. In this mode, the function will not return until all the requested data is transferred. The function returns true after transferring all the data. This indicates that the operation has been completed.

When interrupt is enabled, the function will be non-blocking in nature. The function returns immediately. The data transfer process continues in the peripheral interrupt. The application specified transmit and receive buffer are owned by the library until the data transfer is complete and should not be modified by the application till the transfer is complete. Only one transfer is allowed at any time. The Application can use a callback function or a polling function to check for completion of the transfer. If a callback is required, this should be registered prior to calling the SPIx\_WriteRead function. The application can use the SPIx\_IsBusy to poll for completion.

## Precondition

The SPIx\_Initialize function must have been called. If the peripheral instance has been configured for Interrupt mode and transfer completion status needs to be communicated back to application via callback, a callback should have been registered using SPIx\_CallbackRegister function.

## Parameters

|Param|Description|
|-----|-----------|
|pTransmitData|Pointer to the data which has to be transmitted. In a case where only data reception is required, this pointer can be set to NULL. The size of this buffer should be txSize.|
|txSize|Number of bytes to be transmitted. This value is the byte size of the buffer irrespective of 8/16/32 bit transfer mode.|
|pReceiveData|Pointer to the location where the received data has to be stored. It is user's responsibility to ensure that this location has sufficient memory to store rxSize amount of data. In a case where only data transmission is required, this pointer can be set to NULL.|
|rxSize|Number of bytes to be received. rxSize must be sum of txSize plus the number of bytes to receive. For example, if 3 bytes are transmitted and 10 bytes are to be received, then the rxSize must be 13. This value is the byte size of the buffer irrespective of 8/16/32 bit transfer mode.|

## Returns

*true* - If configured for blocking mode, the function has received and transmitted the requested number of bytes. If configured for non-blocking mode, the request was accepted successfully and will be processed in the interrupt.

*false* - If both pTransmitData and pReceiveData are NULL, or if both txSize and rxSize are 0 or if txSize is non-zero but the pTransmitData is set to NULL or rxSize is non-zero but pReceiveData is NULL. In non-blocking mode, the function returns false if there is an on-going data transfer at the time of calling the function.

## Example

*Non-blocking mode*

```c
// The following code snippet shows an example using the
// SPIx_WriteRead() function in interrupt mode operation using the
// callback function.

uint8_t txBuffer[4];
uint8_t rxBuffer[10];
size_t txSize = 4;
size_t rxSize = 10;

void APP_SPITransferHandler(uintptr_t context)
{
    //Transfer was completed without error, do something else now.
}

SPI1_Initialize();
SPI1_CallbackRegister(&APP_SPITransferHandler, (uintptr_t)NULL);
if(SPI1_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize))
{
    // request got accepted
}
else
{
    // request didn't get accepted, try again later with correct arguments
}
```

*Blocking mode*

```c
// The following code snippet shows non-interrupt or blocking mode
// operation.

uint8_t txBuffer[4];
uint8_t rxBuffer[10];
size_t txSize = 4;
size_t rxSize = 10;

SPI1_Initialize();

// This function call will block.
SPI1_WriteRead(&txBuffer, txSize, &rxBuffer, rxSize);

```

## Remarks

None

