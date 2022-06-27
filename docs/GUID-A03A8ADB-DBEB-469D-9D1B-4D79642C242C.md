# PIT64B\_TimerStart Function

**Parent topic:**[Periodic Interval Timer 64-bit \(PIT64B\)](GUID-B475B881-2B64-4953-9C9F-B287601A380E.md)

## C

```c
/* x = PIT64B instance number */
void PIT64Bx_TimerStart(void)
```

## Summary

Start the PIT64B counter.

## Description

Start the PIT64B counter. If interrupts are enabled an interrupt will occur every time the period value is reached.

## Precondition

None.

## Parameters

None.

## Returns

None.

