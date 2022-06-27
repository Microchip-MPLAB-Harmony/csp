# TCCx\_Compare16bitCounterGet Function

**Parent topic:**[Timer Counter for Control Applications \(TCC\)](GUID-CCA150A8-2C66-40B2-9C35-D7F3473720AE.md)

## C

```c
/* x = TCC instance number */
uint16_t TCCx_Compare16bitCounterGet( void );
```

## Summary

Reads the timer current count value.

## Description

This function reads the timer count value.

## Precondition

TCCx\_CompareInitialize\(\) function must have been called first.

## Parameters

None.

## Returns

Timer's current count value.

## Example

```c
uint16_t counter = 0;
TCC0_CompareInitialize();
TCC0_CompareStart();
counter = TCC0_Compare16bitCounterGet();
```

## Remarks

The caller must know the number of significant bytes of timer. Period value is right-aligned.

