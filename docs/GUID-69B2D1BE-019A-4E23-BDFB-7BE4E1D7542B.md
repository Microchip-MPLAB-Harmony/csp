# TCx\_TimerPeriodHasExpired Function

**Parent topic:**[Basic Timer Counter \(TC\)](GUID-D805E0EA-6923-41A3-A27E-5A159783D12C.md)

## C

```c
/* x = TC instance number */
bool TCx_TimerPeriodHasExpired( void );
```

## Summary

Checks whether timer period is elapsed.

## Description

This function checks the status of the timer period interrupt.

## Precondition

TCx\_TimerInitialize\(\) function must have been called first.

## Parameters

None.

## Returns

Timer period elapsed status.

## Example

```c
bool timerPeriodStatus = false;
TC0_TimerInitialize();
timerPeriodStatus = TC0_TimerPeriodHasExpired();
```

## Remarks

None.

