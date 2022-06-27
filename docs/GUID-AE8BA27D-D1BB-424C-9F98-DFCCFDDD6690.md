# USARTx\_SPI\_Write Function

**Parent topic:**[Universal Synchronous Asynchronous Receiver Transceiver \(USART\)](GUID-5ED4F08A-8227-486D-9727-78BD47CA0866.md)

## C

```c
/* x = USART SPI instance number */

/* USART SPI master mode */
bool USARTx_SPI_Write(void* pWrBuffer, size_t txSize)		
```

## Summary

Writes data to SPI peripheral

## Description

This function writes "txSize" number of bytes on SPI module. Data pointed by pWrBuffer is transmitted. When interrupt is disabled, this function will be blocking in nature. In this mode, the function will not return until all the requested data is transferred. The function returns true after transferring all the data. This indicates that the operation has been completed. When interrupt is enabled, the function will be non-blocking in nature. The function returns immediately. The data transfer process continues in the peripheral interrupt. The application specified transmit buffer is owned by the library until the data transfer is complete and should not be modified by the application till the transfer is complete. Only one transfer is allowed at any time. The application can use a callback function or a polling function to check for completion of the transfer. If a callback is required, this should be registered prior to calling the USARTx\_SPI\_Write\(\) function. The application can use the USARTx\_SPI\_IsBusy\(\) to poll for completion of transfer.

## Precondition

The USARTx\_SPI\_Initialize function must have been called. Callback can be registered using USARTx\_SPI\_CallbackRegister API if the PLIB is configured in Interrupt mode and transfer completion status needs to be communicated back to application via callback.

## Parameters

|Param|Description|
|-----|-----------|
|pWrBuffer|Pointer to the buffer containing the data which has to betransmitted. In "Interrupt Mode", this buffer should not be modified after calling the function and before the callback function has been called or the USARTx\_SPI\_IsBusy\(\) function returns false.|
|txSize|Number of bytes to be transmitted. This value is the byte size of the buffer irrespective of 8/16/32 bit transfer mode.|

## Returns

*true* - If configured for Non-interrupt mode, the function has transmitted the requested number of bytes. If configured for Interrupt mode, the request was accepted successfully and will be processed in the interrupt.

*false* - If pWrBuffer is NULL or txSize is 0. In Interrupt mode, the function will additionally return false if there is an on-going data transfer at the time of calling the function.

## Example

```c
uint8_t txBuffer[4];
size_t txSize = 4;

void APP_SPITransferHandler(uintptr_t context)
{
    //Transfer was completed without error, do something else now.
}

USART1_SPI_Initialize();
USART1_SPI_CallbackRegister(&APP_SPITransferHandler, (uintptr_t)NULL);
if(USART1_SPI_Write(&txBuffer, txSize))
{
    // request got accepted
}
else
{
    // request didn't get accepted, try again later with correct arguments
}

```

## Remarks

None

