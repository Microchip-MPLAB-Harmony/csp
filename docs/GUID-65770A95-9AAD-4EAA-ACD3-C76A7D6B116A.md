# MCSPIx\_Initialize Function

**Parent topic:**[Multi Channel Serial Peripheral Interface \(MCSPI\)](GUID-A3A5277D-BAE3-4BD0-91E9-D4E7E0608BE7.md)

## C

```c
/* x = MCSPI instance number */

/* MCSPI master and slave mode */
void MCSPIx_Initialize (void)
```

## Summary

Initializes MCSPI module of the device

## Description

This function initializes MCSPI PLIB of the device with the values configured in MCC GUI. Once the peripheral is initialized, transfer APIs can be used to transfer the data.

## Precondition

MCC GUI should be configured with the right values.

## Parameters

None.

## Returns

None.

## Example

```c
MCSPI1_Initialize();
```

## Remarks

This function must be called only once and before any other MCSPI function is called.

