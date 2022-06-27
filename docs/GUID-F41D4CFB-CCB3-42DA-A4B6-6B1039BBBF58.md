# TCCx\_PWMDeadTimeSet Function

**Parent topic:**[Timer Counter for Control Applications \(TCC\)](GUID-CCA150A8-2C66-40B2-9C35-D7F3473720AE.md)

## C

```c
/* x = TCC instance number */
void TCCx_PWMDeadTimeSet(uint8_t deadtime_high, uint8_t deadtime_low);
```

## Summary

Sets the dead time of a given TCC module.

## Description

This function updates low-side and high-side dead time.<br />Dead time values are applicable to all the channels of the TCC module.

## Precondition

TCCx\_PWMInitialize function must have been called first for the given channel. And TCC module is in disabled \(stopped\) state.

## Parameters

|Param|Description|
|-----|-----------|
|deadtime\_high|dead-time for high side|
|deadtime\_low|dead-time for low side|

## Returns

none

## Example

```c
TCC0_PWMInitialize();
TCC0_PWMDeadTimeSet(0x100U, 0x100U);
```

## Remarks

This function can be called only when TCC module is disabled.

