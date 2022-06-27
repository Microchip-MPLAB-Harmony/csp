# UARTx\_WriteIsBusy Function

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-3C0B743B-4792-4E9A-AD13-6E911B56B2D0.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-E963A84D-73EE-4E3C-A248-B4FA24F54183.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-12BEB185-3D34-4589-A74C-34A758C5DAB7.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-AA31911E-0C81-4A7D-A72F-20D9976E9E6E.md)

## C

```c
/* x = UART instance number */

/* Non-blocking mode */

bool UARTx_WriteIsBusy( void )
```

## Summary

Returns the write request status associated with the given UART peripheral instance

## Description

This function returns the write request status associated with the given UART peripheral instance. It can be used to check the completion status of the UARTx\_Write\(\) function when the library is configured for non-blocking \(interrupt\) mode. In that, the function can be used as an alternative to using a callback function to check for completion.

## Precondition

UARTx\_Initialize must have been called for the associated UART instance.

## Parameters

None.

## Returns

*true* - UART is busy in processing the previous write request.

*false* - UART is free and ready to accept a new write request.

## Example

```c
if(UART1_WriteIsBusy() == true)
{
    //UART is currently processing the previous write request.
    //Wait to submit new request.
}

```

## Remarks

None

