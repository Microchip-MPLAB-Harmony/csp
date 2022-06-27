# FLEXCOMx\_USART\_TransmitterIsReady Function

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c
/* x = FLEXCOM instance number */

/* Blocking mode */

bool FLEXCOMx_USART_TransmitterIsReady( void )
```

## Summary

Returns the hardware status of the USART Transmitter

## Description

This function returns the hardware status associated with the transmit hardware FIFO of the given USART peripheral instance. When the transmitter is ready, user can submit data to be transmitted. This function is available only in blocking \(non-interrupt\) mode of operation. It can be used to achieve non-blocking behavior of write request in the non-interrupt mode. If non-blocking behavior is desired, this function should be called to check if the transmitter is ready and then the FLEXCOMx\_USART\_Write function should be called with a buffer size of 1.

## Precondition

FLEXCOMx\_USART\_Initialize must have been called for the associated USART instance.

## Parameters

None.

## Returns

*true* - if transmit hardware FIFO has empty space to accept data.

*false* - if transmit hardware FIFO is full.

## Example

```c
if(true == FLEXCOM0_USART_TransmitterIsReady())
{
    // Empty space is available in Transmitter FIFO, hence can write a byte
    FLEXCOM0_USART_Write("A", 1);
}
else
{
    //Transmitter is busy
}
```

## Remarks

None

