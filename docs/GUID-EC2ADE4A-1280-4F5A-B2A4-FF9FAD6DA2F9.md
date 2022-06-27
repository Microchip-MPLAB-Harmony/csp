# USARTx\_WriteByte Function

**Parent topic:**[Universal Synchronous Asynchronous Receiver Transceiver \(USART\)](GUID-5ED4F08A-8227-486D-9727-78BD47CA0866.md)

## C

```c
/* x = USART instance number */

/* Blocking mode */
void USARTx_WriteByte( int data )
```

## Summary

Submits a byte of data to the given USART peripheral to transfer.

## Description

This function submits a byte of data to the USART peripheral to transfer. This Function is available only in non-interrupt mode.

## Precondition

-   USARTx\_Initialize must have been called for the associated USART instance.

-   Transmitter readiness must be confirmed using USARTx\_TransmitterIsReady.


## Parameters

|Param|Description|
|-----|-----------|
|data|Data byte to be transferred.|

## Returns

None

## Example

```c
USART1_WriteByte(0xAA);
```

## Remarks

None.

