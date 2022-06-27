# CANx\_SleepModeEnter Function

**Parent topic:**[Control Area Network \(CAN\)](GUID-B5AC476B-B06A-4C89-AB15-1BB515862877.md)

## C

```c
void CANx_SleepModeEnter(void) // x - Instance of the CAN peripheral
```

## Summary

Puts the CAN Peripheral in sleep mode \(clock stop request\).

## Precondition

CANx\_Initialize and CANx\_MessageRAMConfigSet must have been called for the associated CAN instance.

## Parameters

None.

## Returns

None.

## Example

```c
CAN0_SleepModeEnter();
```

## Remarks

None.

