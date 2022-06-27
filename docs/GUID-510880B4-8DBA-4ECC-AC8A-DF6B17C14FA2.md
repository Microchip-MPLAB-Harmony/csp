# CANx\_TxFIFOIsFull Function

**Parent topic:**[Controller Area Network \(CAN\)](GUID-87A954BC-99B5-448D-BC6D-4C2250A9B58E.md)

## C

```c
bool CANx_TxFIFOIsFull(uint8_t fifoNum) // x - Instance of the CAN peripheral
```

## Summary

Returns true if Tx FIFO is full otherwise false.

## Description

This routine returns true if Tx FIFO is full otherwise false.

## Precondition

CANx\_Initialize must have been called for the associated CAN instance.

## Parameters

|Param|Description|
|-----|-----------|
|fifoNum|FIFO number|

## Returns

*true* - Tx FIFO is full.

*false* - Tx FIFO is not full.

## Example

```c
if (CAN0_TxFIFOIsFull(1) == false)
{
    // Tx FIFO is not full
}
```

## Remarks

None.

