# CCPx\_TimerInterruptDisable Function

**Parent topic:**[Capture/Compare/PWM \(CCP\)](GUID-615BEA57-7216-4351-87D8-94C8B0BF6E7D.md)

## C

```c
/* x = CCP instance number */

void CCPx_TimerInterruptDisable(void)
```

## Summary

Disables timer interrupt.

## Description

This function disables timer interrupt.

## Precondition

CCPx\_TimerInitialize\(\) must have been called first.

## Parameters

None.

## Returns

None.

## Example

```c
CCP1_TimerInterruptDisable();
```

## Remarks

None.

