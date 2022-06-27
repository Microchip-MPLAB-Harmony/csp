# PIT64B\_TimerCallbackSet Function

**Parent topic:**[Periodic Interval Timer 64-bit \(PIT64B\)](GUID-B475B881-2B64-4953-9C9F-B287601A380E.md)

## C

```c
/* x = PIT64B instance number */
void PIT64Bx_TimerCallbackSet(PIT64B_CALLBACK callback, uintptr_t context)
```

## Summary

Register callback for PIT64B interrupt.

## Description

When the timer interrupt occurs the given callback will called with the given context.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|callback|Callback function|
|context|paramter to callback function|

## Returns

None.

