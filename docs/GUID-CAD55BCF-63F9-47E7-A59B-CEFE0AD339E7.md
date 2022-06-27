# TCCx\_PWMPeriodInterruptEnable Function

**Parent topic:**[Timer Counter for Control Applications \(TCC\)](GUID-CCA150A8-2C66-40B2-9C35-D7F3473720AE.md)

## C

```c
/* x = TCC instance number */
void TCCx_PWMPeriodInterruptEnable(void);
```

## Summary

Enables period interrupt

## Description

This function enables period interrupt when counter matches period value while counting UP or<br />when counter matches zero while counting DOWN

## Precondition

TCCx\_PWMInitialize function must have been called first for the given channel

## Parameters

None

## Returns

None

## Example

```c
TCC0_PWMInitialize();
TCC0_PWMPeriodInterruptEnable();
```

## Remarks

None

