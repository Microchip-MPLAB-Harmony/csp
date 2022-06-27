# UART\_CALLBACK Typedef

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-3C0B743B-4792-4E9A-AD13-6E911B56B2D0.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-E963A84D-73EE-4E3C-A248-B4FA24F54183.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-12BEB185-3D34-4589-A74C-34A758C5DAB7.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-AA31911E-0C81-4A7D-A72F-20D9976E9E6E.md)

## C

```c

/* Non-blocking mode */

typedef void (*UART_CALLBACK)( uintptr_t context )

```

## Summary

Defines the data type and function signature of the UART peripheral library callback function.

## Description

This data type defines the function signature of the UART peripheral callback function. The UART peripheral will call back the client's function with this signature to notify the application when a transfer has completed or when a transfer error has occured.

## Precondition

UARTx\_Initialize must have been called for the given UART peripheral instance and UARTx\_CallbackRegister must have been called to set the function to be called.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer tothe callers context for multi-instance clients\).|

## Returns

None.

## Example

```c

void UARTReadCallback(uintptr_t context)
{
    // This function will be called when a UART read has completed.
}

void UARTWriteCallback(uintptr_t context)
{
    // This function will be called when a UART write has completed.
}

UART1_ReadCallbackRegister(UARTReadCallback, 0);
UART1_WriteCallbackRegister(UARTWriteCallback, 0);
```

## Remarks

Code within the callback function will execute in an interrupt context. The application should avoid calling hardware blocking functions or interrupt in-sensitive code in this function.

