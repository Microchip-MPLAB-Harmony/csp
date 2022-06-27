# SPIx\_Ready Function

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-246C53F6-3912-4437-AEC8-C2262CEF3EF6.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-CBD5BFEF-57AB-4CA0-92C0-00CB1A72D686.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-84F93473-4002-4DDD-A28F-9BF9DB6B7C3E.md)

## C

```c
/* x = SPI instance number */

/* SPI slave mode */
void SPIx_Ready(void)
```

## Summary

Drives the SPI slave busy line to ready \(not busy\) state

## Description

This function drives the SPI slave busy line to ready state. The slave busy line is driven to active state \(busy\) when the chip select is driven active by the SPI master. When the data transfer is complete, the chip select is driven inactive and a callback is given to the application. The application can parse the received data and prepare a response for the SPI master. Once the response is ready, the SPI slave can release the busy line by calling this API which drives the busy line to inactive state \(not busy\). All this while the SPI master must wait for the busy line to become inactive \(not busy\) before initiating a new transfer with the SPI slave.

## Precondition

The SPIx\_Initialize\(\) should have been called.

## Parameters

None

## Returns

None

## Example

```c
uint8_t APP_TxData[10];
size_t nBytesRead;

void SPIEventHandler(uintptr_t context )
{
    if (SPI1_ErrorGet() == SPI_SLAVE_ERROR_NONE)
    {
        nBytesRead = SPI1_Read(APP_RxData, SPI1_ReadCountGet());
        
        switch(APP_RxData[0])
        {
            case APP_CMD_WRITE:
            // SPI master is writing data to SPI slave
            // Keep the busy line asserted until the write operation is complete
            // Busy line will be de-asserted later when the write operation is complete
            appData.status.busy = 1;
            
            // Change the state to perform write operation
            state = APP_STATE_WRITE;
            
            break;
            
            case APP_CMD_READ:
            
            // SPI master is reading data from SPI slave
            // Provide the requested data and drive the busy line inactive
            SPI1_Write(APP_TxData, 10);
            break;
        }
        
        if (appData.status.busy == 0)
        {
            // Indicate to SPI Master that slave is ready for data transfer
            // This if condition will be executed for the APP_CMD_READ case.
            SPI1_Ready();
        }
    }
}
```

## Remarks

This API is available only if the Busy signal feature is enabled in MHC.

