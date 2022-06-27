# WDT\_WindowEnable Function

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-150A6728-E8C8-4A67-9FCB-E524A8863357.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-05787A14-6089-477B-842C-EA6DBC92D2D2.md)

## C

```c
void WDT_WindowEnable( void );
```

## Summary

Enables the WDT window mode.

## Description

This function enables the WDT window mode.

## Preconditions

This API is generated to enable the Window mode in firmware if the window mode is disabled by setting WINDIS fuse bit to OFF/NORMAL in MHC device configuration.

## Parameters

None.

## Returns

None.

## Example

```c
WDT_WindowEnable();
```

## Remarks

None.

