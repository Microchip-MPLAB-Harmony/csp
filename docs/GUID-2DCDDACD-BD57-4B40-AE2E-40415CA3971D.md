# FLEXCOM\_SPI\_CALLBACK Typedef

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c
/* SPI master (non-blocking mode) mode */

typedef void (*FLEXCOM_SPI_CALLBACK) (uintptr_t context)

```

## Summary

Defines the data type and function signature for the FLEXCOM SPI peripheral callback function.

## Description

This data type defines the function signature for the FLEXCOM SPI peripheral callback function. The FLEXCOM SPI peripheral will call back the client's function with this signature when the FLEXCOM SPI Transfer has completed.

## Precondition

FLEXCOMx\_SPI\_Initialize must have been called for the given FLEXCOM SPI peripheral instance and FLEXCOMx\_SPI\_CallbackRegister must have been called to set the function to be called. The callback register function must be called before initiating the SPI transfer.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\).|

## Returns

None

## Example

```c
FLEXCOM0_SPI_CallbackRegister(&APP_SPITransferHandler, NULL);

void APP_SPITransferHandler(uintptr_t context)
{
    //Transfer completed
}
```

## Remarks

None

