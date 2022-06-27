# AIC\_INT\_IrqDisable Function

**Parent topic:**[Advanced Interrupt Controller \(AIC\)](GUID-309D6533-41C2-4E5F-9866-44891492168E.md)

## C

```c
bool AIC_INT_IrqDisable ( void )
```

## Summary

Disable interrupt to the processor.

## Description

AIC will not generate interrupts to the processor when an interrupt condition is met.

## Precondition

AIC should be initialized with a call to AIC\_Initialize\(\) function.

## Parameters

None.

## Returns

Current interrupt state.

## Example

```c
bool state = AIC_INT_IrqDisable ( );

```

## Remarks

None.

