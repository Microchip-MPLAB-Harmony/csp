# TMRx\_Start Function

**Parent topic:**[Timer\(TMR\)](GUID-493DD237-5B81-441C-B4FC-53AA6191C224.md)

**Parent topic:**[Timer\(TMR\)](GUID-4FD9BFDE-4887-4C40-B254-C39D2B1DE0F5.md)

## C

```c
/* x = TMR instance number */
void TMRx_Start(void);
```

## Summary

Starts the given Timer.

## Description

This function enables the clock and starts the counter of the timer.

## Precondition

TMRx\_Initialize\(\) function must have been called first.

## Parameters

None.

## Returns

None.

## Example

```c
TMR2_Initialize();
TMR2_Start();
```

## Remarks

None.

