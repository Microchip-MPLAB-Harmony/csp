# TMR1\_InterruptDisable Function

**Parent topic:**[Timer1\(TMR1\)](GUID-FBA83258-F84E-46B4-9CAA-9B5B03A70F0B.md)

## C

```c
void TMR1_InterruptDisable(void);
```

## Summary

Disable TMR overflow interrupt

## Description

This function disables TMR overflow interrupt.

## Precondition

TMR1\_Initialize\(\) function must have been called first.

## Parameters

None.

## Returns

None.

## Example

```c
TMR1_Initialize();
TMR1_InterruptDisable();
```

## Remarks

None.

