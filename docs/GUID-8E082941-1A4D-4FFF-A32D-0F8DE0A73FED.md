# POWER\_LowPowerModeEnter Function

**Parent topic:**[Low Power Modes \(Power\)](GUID-DD684FA8-1232-40DE-931B-5F99EF766752.md)

**Parent topic:**[Low Power Modes \(Power\)](GUID-E9B62E77-7033-44DD-BDB2-16E93E627057.md)

## C

```c
void POWER_LowPowerModeEnter( POWER_LOW_POWER_MODE mode );
```

## Summary

Puts the device in selected low power mode

## Description

This function puts the device in selected low power mode. Before entering<br />into low power mode using this API, user application should have made<br />appropriate provision to wake up the device from low power mode.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|mode|Low power mode which has to be entered.|

## Returns

None.

## Example

```c
// Puts the device in sleep mode
POWER_LowPowerModeEnter( LOW_POWER_SLEEP_MODE );
```

## Remarks

None.

