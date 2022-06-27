# UARTx\_Initialize Function

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-3C0B743B-4792-4E9A-AD13-6E911B56B2D0.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-E963A84D-73EE-4E3C-A248-B4FA24F54183.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-12BEB185-3D34-4589-A74C-34A758C5DAB7.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-AA31911E-0C81-4A7D-A72F-20D9976E9E6E.md)

## C

```c
/* x = UART instance number */

/* Blocking, non-blocking and ring buffer mode */

void UARTx_Initialize( void )
```

## Summary

Initializes given instance of the UART peripheral.

## Description

This function initializes the given instance of the UART peripheral as configured by the user in MHC.

## Precondition

None.

## Parameters

None.

## Returns

None.

## Example

```c
UART1_Initialize();
```

## Remarks

None

