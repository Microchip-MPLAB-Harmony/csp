# USART\_CALLBACK Typedef

**Parent topic:**[Universal Synchronous Asynchronous Receiver Transceiver \(USART\)](GUID-5ED4F08A-8227-486D-9727-78BD47CA0866.md)

## C

```c

/* Non-blocking mode */

typedef void (*USART_CALLBACK)( uintptr_t context );

```

## Summary

Defines the data type and function signature of the USART peripheral library callback function.

## Description

This data type defines the function signature of the USART peripheral callback function. The USART peripheral will call back the client's function with this signature to notify the application when a transfer has completed or when a transfer error has occured.

## Precondition

USARTx\_Initialize must have been called for the given USART peripheral instance and USARTx\_CallbackRegister must have been called to set the function to be called.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer tothe callers context for multi-instance clients\).|

## Returns

None.

## Example

```c

void MyUsartReadCallback(uintptr_t context)
{
    // This function will be called when a USART read has completed.
}

void MyUsartWriteCallback(uintptr_t context)
{
    // This function will be called when a USART write has completed.
}

USART1_ReadCallbackRegister(MyUsartReadCallback, (uintptr_t)NULL);
USART1_WriteCallbackRegister(MyUsartWriteCallback, (uintptr_t)NULL);
```

## Remarks

Code within the callback function will execute in an interrupt context. The application should avoid calling hardware blocking functions or interrupt in-sensitive code in this function.

