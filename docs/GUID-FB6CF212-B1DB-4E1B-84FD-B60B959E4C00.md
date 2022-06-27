# QEIx\_RevolutionsGet Function

**Parent topic:**[Quadrature Encoder Interface \(QEI\)](GUID-62A23819-A256-4FB3-9682-BA733F4B45AA.md)

## C

```c

/* x = QEI instance number */

uint32_t QEIx_RevolutionsGet ( void )
```

## Summary

Reads the number of revolutions tracked by the quadrature encoder.

## Description

This function reads the revolution counter. The contents of the counter represent<br />the number of revolutions tracked by the quadrature encoder.

## Precondition

QEIx\_Initialize function must have been called first for the given channel.

## Parameters

None.

## Returns

*revolutions* - number of revolutions

## Example

```c
uint32_t velocity;

QEI1_Initialize();
QEI1_Start();
velocity = QEI1_RevolutionsGet();
```

## Remarks

Revolution counter is updated every index signal.

