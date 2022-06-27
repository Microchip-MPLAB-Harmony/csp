# SYSTICK\_TimerPeriodSet Function

**Parent topic:**[System timer \(SysTick\)](GUID-A4B9F359-3129-4377-B43E-71415C6B19F2.md)

## C

```c
void SYSTICK_TimerPeriodSet( uint32_t period )
```

## Summary

Set the SysTick Load Value

## Description

This function is used to update SysTick Load value

## Preconditions

Systick should be stopped prior to setting up the new Load value by calling SYSTICK\_TimerStop. This will make sure that the new value is used for the next Tick

## Parameters

|Param|Description|
|-----|-----------|
|period|The period is specified as a number of clock ticks between SysTick interrupt. It must be between 1 and 16,777,216, inclusive.|

## Returns

None.

## Example

```c
SYSTICK_TimerStop();

SYSTICK_TimerPeriodSet(0x00004567);

SYSTICK_TimerStart();
```

