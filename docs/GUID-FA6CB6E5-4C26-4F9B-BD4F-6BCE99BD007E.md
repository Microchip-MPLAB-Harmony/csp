# TMR1\_CounterGet Function

**Parent topic:**[Timer1\(TMR1\)](GUID-FBA83258-F84E-46B4-9CAA-9B5B03A70F0B.md)

## C

```c
uint16_t TMR1_CounterGet(void);
```

## Summary

Reads the timer counter value.

## Description

This function reads the timer counter value.

## Precondition

TMR1\_Initialize\(\) function must have been called first.

## Parameters

None.

## Returns

The timer's current count value.

## Example

```c
uint16_t counter;

TMR1_Initialize();
TMR1_Start();
counter = TMR1_CounterGet();
```

## Remarks

None

