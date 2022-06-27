# USARTx\_WriteIsBusy Function

**Parent topic:**[Universal Synchronous Asynchronous Receiver Transceiver \(USART\)](GUID-5ED4F08A-8227-486D-9727-78BD47CA0866.md)

## C

```c
/* x = USART instance number */

/* Non-blocking mode */
bool USARTx_WriteIsBusy( void )
```

## Summary

Returns the write request status associated with the given USART peripheral instance.

## Description

This function returns the write request status associated with the given USART peripheral instance. It can be used to check the completion status of the USARTx\_Write\(\) function when the library is configured for non-blocking \(interrupt\) mode. In that, the function can be used as an alternative to using a callback function to check for completion.

## Precondition

USARTx\_Initialize must have been called for the associated USART instance.

## Parameters

None.

## Returns

*true* - USART is busy in processing the previous write request.

*false* - USART is free and ready to accept a new write request.

## Example

```c
if(USART1_WriteIsBusy() == true)
{
    //USART is currently processing the write request.
}
else
{
    // write is completed.
}

```

## Remarks

None

