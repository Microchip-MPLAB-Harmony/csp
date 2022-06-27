# DAC\_Initialize Function

**Parent topic:**[Digital-to-Analog Converter \(DAC\)](GUID-95143D2D-ED7E-452A-83FC-96902B1A6273.md)

**Parent topic:**[Digital-to-Analog Converter \(DAC\)](GUID-E495F067-A363-45EF-A07D-09E16FF6E4DD.md)

**Parent topic:**[Digital-to-Analog Converter \(DAC\)](GUID-953A92EF-D699-41B9-8D61-9D393C74DCFF.md)

## C

```c
void DAC_Initialize (void);
```

## Summary

Initializes DAC module of the device

## Description

This function initializes DAC module of the device with the values<br />configured in MHC GUI. Once the peripheral is initialized, APIs can be used<br />to convert the data.

## Precondition

MHC GUI should be configured with the right values.

## Parameters

None.

## Returns

None.

## Example

```c
DAC_Initialize();
```

## Remarks

None.

