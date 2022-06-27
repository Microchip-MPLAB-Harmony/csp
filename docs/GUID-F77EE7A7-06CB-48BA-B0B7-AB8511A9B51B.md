# POWER\_WakeupSourceGet Function

**Parent topic:**[Low Power Modes \(Power\)](GUID-E9B62E77-7033-44DD-BDB2-16E93E627057.md)

## C

```c
POWER_WAKEUP_SOURCE POWER_WakeupSourceGet( void );
```

## Summary

Returns the source of wakeup from deep sleep

## Description

This function returns the name of the source which woke up the device from<br />deep sleep.

## Precondition

None.

## Parameters

None.

## Returns

*POWER\_WAKEUP\_SOURCE* - wakeup source

## Example

```c
if (POWER_WakeupSourceGet() == POWER_WAKEUP_SOURCE_DSINT0)
{
    // wakeup source was INT0
}
```

## Remarks

This function is only available for the devices which has deep sleep controller. MHC will generate this function only for the selected devices accordingly. Check device datasheet for more information.

