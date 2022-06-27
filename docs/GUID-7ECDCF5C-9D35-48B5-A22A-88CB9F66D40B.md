# DWT\_CounterGet Function

**Parent topic:**[Data Watchpoint and Trace \(DWT\)](GUID-E1AD558F-6AA8-4D5F-90A6-8820A72C3777.md)

## C

```c
uint32_t DWT_CounterGet(void)
```

## Summary

Get the cycle counter current Value

## Description

This function returns the cycle counter current value

## Precondition

DWT\_Initialize must have been called

## Parameters

None.

## Returns

Returns cycle counter current Value

## Example

```c
uint32_t value;

value = DWT_CounterGet();
```

