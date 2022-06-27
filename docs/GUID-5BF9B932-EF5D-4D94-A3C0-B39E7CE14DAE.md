# TCx\_Compare8bitPeriodGet Function

**Parent topic:**[Basic Timer Counter \(TC\)](GUID-D805E0EA-6923-41A3-A27E-5A159783D12C.md)

## C

```c
/* x = TC instance number */
uint8_t TCx_Compare8bitPeriodGet( void );
```

## Summary

Reads the period value of given timer.

## Description

This function reads the value of period.

## Precondition

TCx\_CompareInitialize\(\) function must have been called first.

## Parameters

None.

## Returns

Timer's period value

## Example

```c
uint8_t period = 0;
TC0_CompareInitialize();
period = TC0_Compare8bitPeriodGet();
```

## Remarks

The caller must know the number of significant bytes of timer. Period value is right-aligned.

