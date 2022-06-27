# WDT\_Clear Function

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-516654BB-A119-4984-BC8E-A7890E6C958E.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-150A6728-E8C8-4A67-9FCB-E524A8863357.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-05787A14-6089-477B-842C-EA6DBC92D2D2.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-947B7882-C762-4E93-BF77-6EF42FB0F89D.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-E3301363-4446-4B9B-B20B-EE813B1232EC.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-FA9631BE-AD37-4EF9-8C69-2BF8C5941388.md)

**Parent topic:**[Watchdog Timer \(WDT\)](GUID-8A37E31C-D55D-4230-B1FE-0180D3B32410.md)

## C

```c
void WDT_Clear( void )
```

## Summary

Restarts the WDT counter.

## Description

This function is used to restart the WDT counter to avoid timeout. Calling this will clear the WDT timeout counter and restart the counting from 0. Failure to call this function before the WDT timeout period will cause the system to reset.

## Precondition

WDT must be enabled using WDT\_Enable\(\).

## Parameters

None.

## Returns

None.

## Example

```c
//Application

WDT_Enable();

while (true)
{
    // Application Code executes here.
    // Clear the WDT periodically.
    WDT_Clear();
}
```

## Remarks

None.

