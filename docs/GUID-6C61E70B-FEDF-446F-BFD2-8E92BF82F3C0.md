# TMRx\_PeriodSet Function

**Parent topic:**[Timer\(TMR\)](GUID-493DD237-5B81-441C-B4FC-53AA6191C224.md)

**Parent topic:**[Timer\(TMR\)](GUID-4FD9BFDE-4887-4C40-B254-C39D2B1DE0F5.md)

## C

```c
void TMRx_PeriodSet(uint16_t period);
```

## Summary

Sets the period value of a given timer.

## Description

This function writes the period value. When timer counter matches period value counter is reset and interrupt can be generated.

## Precondition

TMRx\_Initialize\(\) function must have been called first for the given timer.

## Parameters

|Param|Description|
|-----|-----------|
|period|new period value to set|

## Returns

None.

## Example

```c
uint16_t period = 0x100;
TMR2_Initialize();
TMR2_PeriodSet(period);
```

## Remarks

If timer is operating on 32 bit mode then argument should be uint32\_t type.

