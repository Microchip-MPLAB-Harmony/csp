# SDADC\_Disable Function

**Parent topic:**[Sigma-Delta Analog Digital Converter \(SDADC\)](GUID-67D47E4E-A9CC-4485-9552-A56F2E6825A3.md)

## C

```c
void SDADC_Disable( void )
```

## Summary

Disables the SDADC module

## Description

This function disables the clock to the SDADC module and stops the peripheral.

## Precondition

MCC GUI should be configured with the right values.

## Parameters

None.

## Returns

None.

## Example

```c
SDADC_Initialize();
SDADC_Disable();
```

## Remarks

None.

