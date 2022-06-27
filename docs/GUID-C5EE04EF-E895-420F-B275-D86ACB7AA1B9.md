# CCPx\_CompareStart Function

**Parent topic:**[Capture/Compare/PWM \(CCP\)](GUID-615BEA57-7216-4351-87D8-94C8B0BF6E7D.md)

## C

```c
/* x = CCP instance number */

void CCPx_CompareStart( void )
```

## Summary

Starts the timer for given CCP instance.

## Description

This function enables the clock and starts the timer.

## Precondition

CCPx\_CompareInitialize\(\) function must have been called first.

## Parameters

None.

## Returns

None.

## Example

```c
CCP1_CompareInitialize();
CCP1_CompareStart();
```

## Remarks

None.

