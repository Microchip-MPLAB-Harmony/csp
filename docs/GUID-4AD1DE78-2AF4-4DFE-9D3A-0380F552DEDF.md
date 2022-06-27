# PIT64B\_DelayUs Function

**Parent topic:**[Periodic Interval Timer 64-bit \(PIT64B\)](GUID-B475B881-2B64-4953-9C9F-B287601A380E.md)

## C

```c
/* x = PIT64B instance number */
void PIT64Bx_DelayUs(uint32_t ms)
```

## Summary

Delays processing for x microseconds.

## Description

Delays execution by using the PIT64B timer to determine when given number of microseconds has expired.

## Precondition

PIT64B is configured and enabled. The PIT64B interrupt is also enabled.

## Parameters

|Param|Description|
|-----|-----------|
|us|number of microseconds to delay|

## Returns

None.

