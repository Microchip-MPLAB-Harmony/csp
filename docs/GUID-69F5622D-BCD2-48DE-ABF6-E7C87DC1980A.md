# PIT64B\_TimerPeriodHasExpired Function

**Parent topic:**[Periodic Interval Timer 64-bit \(PIT64B\)](GUID-B475B881-2B64-4953-9C9F-B287601A380E.md)

## C

```c
/* x = PIT64B instance number */
bool PIT64Bx_TimerPeriodHasExpired(void)
```

## Summary

Return whether or not the Timer Period has expired.

## Description

Check the PIT64B Status register to determine if period has expired.

## Precondition

None.

## Parameters

None.

## Returns

True if period has expired, false otherwise

