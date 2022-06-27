# FLEXCOMx\_SPI\_ReadCountGet Function

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c
/* x = FLEXCOM instance number */

/* SPI slave mode */

size_t FLEXCOMx_SPI_ReadCountGet(void)
```

## Summary

Returns the number of bytes pending to be read out from the PLIB's internal receive buffer

## Description

This function returns the number of unread bytes availabe in the SPI slave PLIB's internal receive buffer. Application can call this API to know the bytes available in PLIBs internal buffer before calling the FLEXCOMx\_SPI\_Read API.

## Precondition

The FLEXCOMx\_SPI\_Initialize function must have been called

## Parameters

None

## Returns

*size\_t* - Number of bytes available in the PLIB's internal receive buffer. If 16/32 bit modes are supported, the return value is specified in terms of 16/32 bit words.

## Example

```c
uint8_t APP_RxData[10];
size_t nBytesAvailable;
size_t nBytesRead;

void SPIEventHandler(uintptr_t context )
{
    if (FLEXCOM0_SPI_ErrorGet() == SPI_SLAVE_ERROR_NONE)
    {
        nBytesAvailable = FLEXCOM0_SPI_ReadCountGet();
        
        nBytesRead = FLEXCOM0_SPI_Read(APP_RxData, nBytesAvailable);
    }
    else
    {
        // Handle error
    }
    
}

FLEXCOM0_SPI_CallbackRegister(SPIEventHandler, (uintptr_t) 0);
```

## Remarks

None.

