# TCx\_Compare8bitCounterGet Function

**Parent topic:**[Basic Timer Counter \(TC\)](GUID-D805E0EA-6923-41A3-A27E-5A159783D12C.md)

## C

```c
/* x = TC instance number */
uint8_t TCx_Compare8bitCounterGet( void );
```

## Summary

Reads the timer current count value.

## Description

This function reads the timer count value.

## Precondition

TCx\_CompareInitialize\(\) function must have been called first.

## Parameters

None.

## Returns

Timer's current count value.

## Example

```c
uint8_t counter = 0;
TC0_CompareInitialize();
TC0_CompareStart();
counter = TC0_Compare8bitCounterGet();
```

## Remarks

The caller must know the number of significant bytes of timer. Period value is right-aligned.

