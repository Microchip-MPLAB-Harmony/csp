# SPIx\_CallbackRegister Function

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-246C53F6-3912-4437-AEC8-C2262CEF3EF6.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-CBD5BFEF-57AB-4CA0-92C0-00CB1A72D686.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-84F93473-4002-4DDD-A28F-9BF9DB6B7C3E.md)

## C

```c
/* x = SPI instance number */

/* SPI master (non-blocking mode) mode */

void SPIx_CallbackRegister(SPI_CALLBACK callback, uintptr_t context )

/* SPI slave mode */

void SPIx_CallbackRegister(SPI_SLAVE_CALLBACK callBack, uintptr_t context )
```

## Summary

This function allows application to register a callback function for the PLIB to call back when the requested data transfer operation has completed.

## Description

This function sets the pointer to a client/application function to be called "back" when the given SPI's transfer events occur. It also passes a context value \(usually a pointer to a context structure\) that is passed into the function when it is called. The specified callback function will be called from the peripheral interrupt context. The callback should be registered before a transfer operation is requested.

## Precondition

The SPIx\_Initialize function must have been called. This function is only available if the library is configured for interrupt operation mode.

## Parameters

|Param|Description|
|-----|-----------|
|callback|A pointer to a function with a calling signature defined by the SPI\_CALLBACK or SPI\_SLAVE\_CALLBACK data type. Setting this to NULL disables the callback feature.|
|context|A value \(usually a pointer\) which is passed \(unused\) into the function identified by the callback parameter|

## Returns

None.

## Example

*SPI master \(non-blocking mode\) mode*

```c
uint8_t txBuffer[4];
uint8_t rxBuffer[10];
size_t txSize = 4;
size_t rxSize = 10;
bool reqAccepted;

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

*SPI slave mode*

```c
uint8_t APP_RxData[10];
size_t nBytesAvailable;
size_t nBytesRead;

void SPIEventHandler(uintptr_t context )
{
    if (SPI1_ErrorGet() == SPI_SLAVE_ERROR_NONE)
    {
        nBytesAvailable = SPI1_ReadCountGet();

        nBytesRead = SPI1_Read(APP_RxData, nBytesAvailable);
    }
    else
    {
        // Handle error
    }

}

SPI1_CallbackRegister(SPIEventHandler, (uintptr_t) 0);
```

## Remarks

None

