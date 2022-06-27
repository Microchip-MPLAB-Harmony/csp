# CCPx\_TimerStart Function

**Parent topic:**[Capture/Compare/PWM \(CCP\)](GUID-615BEA57-7216-4351-87D8-94C8B0BF6E7D.md)

## C

```c
/* x = CCP instance number */

void CCPx_TimerStart( void );
```

## Summary

Starts the timer for given CCP instance.

## Description

This function enables the clock and starts the timer.

## Precondition

CCPx\_TimerInitialize\(\) function must have been called first.

## Parameters

None.

## Returns

None.

## Example

```c
CCP1_TimerInitialize();
CCP1_TimerStart();
```

## Remarks

None.

