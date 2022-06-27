# POWER\_WakeupSourceClear Function

**Parent topic:**[Low Power Modes \(Power\)](GUID-E9B62E77-7033-44DD-BDB2-16E93E627057.md)

## C

```c
void POWER_WakeupSourceClear( POWER_WAKEUP_SOURCE wakeupSource )
```

## Summary

Clears the wakeup source

## Description

This function clears the wakeup \(from deep sleep\) source information from<br />the register so that next time updated wakeup source can be found.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|wakeupSource|wakeup source to be cleared|

## Returns

None.

## Example

```c
POWER_WakeupSourceClear(POWER_WAKEUP_SOURCE_DSINT0);
```

## Remarks

This function is only available for the devices which has deep sleep controller. MHC will generate this function only for the selected devices accordingly. Check device datasheet for more information.

