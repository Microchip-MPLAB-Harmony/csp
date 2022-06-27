# TCCx\_Timer24bitCounterGet Function

**Parent topic:**[Timer Counter for Control Applications \(TCC\)](GUID-CCA150A8-2C66-40B2-9C35-D7F3473720AE.md)

## C

```c
/* x = TCC instance number */
uint32_t TCCx_Timer24bitCounterGet( void );
```

## Summary

Reads the timer current count value.

## Description

This function reads the timer count value.

## Precondition

TCCx\_TimerInitialize\(\) function must have been called first.

## Parameters

None.

## Returns

Timer's current count value.

## Example

```c
uint32_t counter = 0;
TCC0_TimerInitialize();
TCC0_TimerStart();
counter = TCC0_Timer24bitCounterGet();
```

## Remarks

The caller must know the number of significant bytes of timer. Period value is right-aligned.

