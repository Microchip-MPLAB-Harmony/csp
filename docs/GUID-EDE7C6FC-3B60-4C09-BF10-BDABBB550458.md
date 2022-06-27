# SDHCx\_ClockEnable Function

**Parent topic:**[SD/MMC Host Controller \(SDHC\)](GUID-8769733F-B27A-4567-BE7D-7BEA8C76F05E.md)

**Parent topic:**[SD/MMC Host Controller \(SDHC\)](GUID-D440DD4B-CA37-46F4-A6AA-4D57D9DAEF97.md)

## C

```c

/* x = SDHC instance number (x is applicable only on devices with more than one instances of SDHC) */

void SDHCx_ClockEnable ( void )
```

## Summary

Enable SDHC clock

## Description

Enables SDHC clock

## Precondition

SDHCx\_Initialize\(\) must have been called first for the associated instance.

## Parameters

None.

## Returns

None.

## Example

```c
SDHC1_ClockEnable();
```

## Remarks

None.

