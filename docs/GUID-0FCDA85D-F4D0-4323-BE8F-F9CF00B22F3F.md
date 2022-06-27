# GENERIC\_TIMER\_CallbackRegister Function

**Parent topic:**[ARM Cortex A Generic timer \(GENERIC\_TIMER\)](GUID-D781FC89-91D3-4EFD-8877-25F1D125D366.md)

## C

```c
void GENERIC_TIMER_CallbackRegister(GENERIC_TIMER_CALLBACK pCallback, uintptr_t context);
```

## Summary

Register callback for generic timer interrupt.

## Description

When the timer interrupt occurs the given callback will called with the given context.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|callback|Callback function|
|context|parameter to callback function|

## Returns

None.

