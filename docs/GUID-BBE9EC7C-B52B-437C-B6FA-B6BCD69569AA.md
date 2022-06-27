# GENERIC\_TIMER\_DelayUs Function

**Parent topic:**[ARM Cortex A Generic timer \(GENERIC\_TIMER\)](GUID-D781FC89-91D3-4EFD-8877-25F1D125D366.md)

## C

```c
void GENERIC_TIMER_DelayUs(uint32_t delay_us);
```

## Summary

Delays processing for x microseconds.

## Description

Delays execution by using the generic timer to determine when given number of<br />microseconds has expired.

## Precondition

generic timer is configured, running with interrupt enabled.

## Parameters

|Param|Description|
|-----|-----------|
|delay\_ms|number of microseconds to delay|

## Returns

None.

