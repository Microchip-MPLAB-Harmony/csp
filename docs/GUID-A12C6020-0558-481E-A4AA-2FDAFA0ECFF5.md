# USARTx\_SPI\_Read Function

**Parent topic:**[Universal Synchronous Asynchronous Receiver Transceiver \(USART\)](GUID-5ED4F08A-8227-486D-9727-78BD47CA0866.md)

## C

```c
/* x = USART SPI instance number */

/* USART SPI master mode */

bool USARTx_SPI_Read(void* pRdBuffer, size_t rxSize)	
```

## Summary

Reads data on the SPI peripheral.

## Description

This function reads "rxSize" number of bytes on SPI module. The received data is stored in the buffer pointed by pRdBuffer. When the interrupt is disabled in the PLIB, this function will be blocking in nature. In this mode, the function will not return until all the requested data is transferred. The function returns true after receiving "rxSize" number of bytes. This indicates that the operation has been completed. When interrupt is enabled, the function will be non-blocking in nature. The function returns immediately. The data transfer process continues from the peripheral interrupt. The application specified receive buffer is owned by the PLIB until the data transfer is complete and should not be modified by the application till the transfer is complete. Only one transfer is allowed at any time. The application can use a callback function or a polling function to check for completion of the transfer. If a callback is required then it should be registered prior to calling the SPIx\_Read\(\) function. The application can use the USARTx\_SPI\_IsBusy\(\) to poll for completion of transfer.

## Precondition

The USARTx\_SPI\_Initialize function must have been called.

Callback can be registered using USARTx\_SPI\_CallbackRegister API if the PLIB is configured in Interrupt mode and transfer completion status needs to be communicated back to application via callback.

## Parameters

|Param|Description|
|-----|-----------|
|pRdBuffer|Pointer to the buffer where the received data will be stored. In "Interrupt Mode", this buffer should not be modified after calling the function and before the callback function has been called or the USARTx\_SPI\_IsBusy\(\) function returns false.|
|rxSize|Number of bytes to be received. This value is the byte size of the buffer irrespective of 8/16/32 bit transfer mode.|

## Returns

*SPI master mode*

*true* - If configured for non-interrupt mode, the function has received the requested number of bytes. If configured for Interrupt mode, the request was accepted successfully and will be processed in the interrupt.

*false* - If pRdBuffer is NULL or rxSize is 0. In Interrupt mode, the function will additionally return false if there is an on-going data transfer at the time of calling the function.

## Example

```c
uint8_t rxBuffer[10];
size_t rxSize = 10;

void USART_SPIEventHandler(uintptr_t context)
{
    //Transfer was completed without error, do something else now.
}

USART1_SPI_Initialize();
USART1_SPI_CallbackRegister(USART_SPIEventHandler, (uintptr_t)0);
if(USART1_SPI_Read(&rxBuffer, rxSize))
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

