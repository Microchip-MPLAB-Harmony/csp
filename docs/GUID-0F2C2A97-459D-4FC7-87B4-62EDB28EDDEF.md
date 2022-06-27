# SDHCx\_ClockSet Function

**Parent topic:**[SD/MMC Host Controller \(SDHC\)](GUID-8769733F-B27A-4567-BE7D-7BEA8C76F05E.md)

**Parent topic:**[SD/MMC Host Controller \(SDHC\)](GUID-D440DD4B-CA37-46F4-A6AA-4D57D9DAEF97.md)

## C

```c

/* x = SDHC instance number (x is applicable only on devices with more than one instances of SDHC) */

bool SDHCx_ClockSet ( uint32_t clock)
```

## Summary

Sets the SDHC clock frequency

## Description

Sets the SDHC clock frequency

## Precondition

SDHCx\_Initialize\(\) must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|clock|SDHC clock frequency|

## Returns

None.

## Example

```c
SDHC1_ClockSet(400000);
```

## Remarks

None.

