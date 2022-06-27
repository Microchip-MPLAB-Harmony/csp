# WDT\_ClearWithSync Function

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-516654BB-A119-4984-BC8E-A7890E6C958E.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-8A37E31C-D55D-4230-B1FE-0180D3B32410.md)

## C

```c
void WDT_ClearWithSync( void )
```

## Summary

Restarts the WDT counter with write sync.

## Description

This API must be used if application intends to enter low power mode after clearing WDT. It waits for write synchronization to complete as the device must not enter low power mode while write sync is in progress.

## Precondition

WDT must be enabled using WDT\_Enable\(\).

## Parameters

None.

## Returns

None.

## Example

```c
//Application

WDT_Initialize();

WDT_Enable();

while(true)
{
    // Application Code executes here.
    // Clear the WDT periodically.
    WDT_ClearWithSync();
}

```

## Remarks

None.

