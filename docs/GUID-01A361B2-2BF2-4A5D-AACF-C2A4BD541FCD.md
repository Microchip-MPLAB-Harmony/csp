# TMRx\_InterruptDisable Function

**Parent topic:**[Timer\(TMR\)](GUID-493DD237-5B81-441C-B4FC-53AA6191C224.md)

**Parent topic:**[Timer\(TMR\)](GUID-4FD9BFDE-4887-4C40-B254-C39D2B1DE0F5.md)

## C

```c
/* x = TMR instance number */
void TMRx_InterruptDisable(void);
```

## Summary

Disable TMR overflow interrupt

## Description

This function disables TMR overflow interrupt.

## Precondition

TMRx\_Initialize\(\) function must have been called first.

## Parameters

None.

## Returns

None.

## Example

```c
TMR2_Initialize();
TMR2_InterruptDisable();
```

## Remarks

None.

