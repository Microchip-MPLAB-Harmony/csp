# SYSTICK\_TimerPeriodHasExpired Function

**Parent topic:**[System timer \(SysTick\)](GUID-A4B9F359-3129-4377-B43E-71415C6B19F2.md)

## C

```c
bool SYSTICK_TimerPeriodHasExpired( void )
```

## Summary

Returns the current status of the systick

## Description

This function is used to identify if the Systick underflow has happened.

This API is generated only in polling mode

## Precondition

SYSTICK\_Initialize should have been called to set up SysTick.

## Parameters

None.

## Returns

*True* - timer period has expired

*False* - timer period is not expired

## Example

```c
SYSTICK_Initialize();

SYSTICK_TimerStart();

if(SYSTICK_TimerPeriodHasExpired())
{
    //application code
}
```

