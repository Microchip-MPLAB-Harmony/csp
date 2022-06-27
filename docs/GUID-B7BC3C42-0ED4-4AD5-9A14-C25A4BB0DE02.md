# CANx\_InterruptDisable Function

**Parent topic:**[Controller Area Network \(CAN\)](GUID-F5B9ED1E-1BBD-4120-8CF5-C3104BED03CA.md)

## C

```c
void CANx_InterruptDisable(CAN_INTERRUPT_MASK interruptMask) // x - Instance of the CAN peripheral
```

## Summary

Disables CAN Interrupt.

## Precondition

CANx\_Initialize must have been called for the associated CAN instance.

## Parameters

|Param|Description|
|-----|-----------|
|interruptMask|Interrupt to be disabled|

## Returns

None

## Example

```c
CAN_INTERRUPT_MASK interruptMask = CAN_INTERRUPT_MB0_MASK;
CAN0_InterruptDisable(interruptMask);
```

## Remarks

None.

