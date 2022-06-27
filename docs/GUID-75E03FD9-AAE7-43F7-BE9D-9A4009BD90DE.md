# SERCOMx\_USART\_ReadIsBusy Function

**Parent topic:**[Serial Communication Interface \(SERCOM\)](GUID-76AE7205-E3EF-4EE6-AC28-5153E3565982.md)

## C

```c
/* x = SERCOM instance number */

/* Non-blocking mode */

bool SERCOMx_USART_ReadIsBusy( void )
```

## Summary

Returns the read request status associated with the given USART peripheral instance

## Description

This function returns the read request status associated with the given USART peripheral instance. It can be used to check the completion status of the SERCOMx\_USART\_Read\(\) function when the library is configured for interrupt \(non-blocking\) mode. In that, the function can be used as an alternative to using a callback function to check for completion.

## Precondition

SERCOMx\_USART\_Initialize must have been called for the associated USART instance.

## Parameters

None.

## Returns

*true* - USART is busy in processing the previous read request

*false* - USART is free and ready to accept the new read request

## Example

```c
if(SERCOM0_USART_ReadIsBusy() == true)
{
    //USART is currently processing the previous read request.
    //Wait to submit new request.
}

```

## Remarks

None

