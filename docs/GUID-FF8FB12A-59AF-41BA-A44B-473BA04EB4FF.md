# MCANx\_SleepModeEnter Function

**Parent topic:**[Controller Area Network \(MCAN\)](GUID-C9F1E50C-1EF0-4941-A9CB-89808C7C54AF.md)

## C

```c
void MCANx_SleepModeEnter(void) // x - Instance of the MCAN peripheral
```

## Summary

Puts the MCAN Peripheral in sleep mode \(clock stop request\).

## Precondition

MCANx\_Initialize and MCANx\_MessageRAMConfigSet must have been called for the associated MCAN instance.

## Parameters

None.

## Returns

None.

## Example

```c
MCAN0_SleepModeEnter();
```

## Remarks

None.

