# WDT\_Enable Function

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-516654BB-A119-4984-BC8E-A7890E6C958E.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-150A6728-E8C8-4A67-9FCB-E524A8863357.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-05787A14-6089-477B-842C-EA6DBC92D2D2.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-947B7882-C762-4E93-BF77-6EF42FB0F89D.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-E3301363-4446-4B9B-B20B-EE813B1232EC.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-8A37E31C-D55D-4230-B1FE-0180D3B32410.md)

## C

```c
void WDT_Enable( void );
```

## Summary

Enables the WDT peripheral.

## Description

This function enables the WDT peripheral. Calling this function will cause the WDT to start counting up to the configured timeout value.

For devices which have Early Warning interrupt support, This function also enables the Early Warning interrupt if it has been enabled in MHC.

## Preconditions

None.

## Parameters

None.

## Returns

None.

## Example

```c
WDT_Enable();
```

## Remarks

For some device families this API is generated to enable the WDT in firmware if the WDT is disabled by setting FWDTEN fuse bit to OFF in MHC device configuration.

