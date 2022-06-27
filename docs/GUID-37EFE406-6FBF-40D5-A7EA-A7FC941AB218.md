# POWER\_ReleaseGPIO Function

**Parent topic:**[Low Power Modes \(Power\)](GUID-E9B62E77-7033-44DD-BDB2-16E93E627057.md)

## C

```c
void POWER_ReleaseGPIO( void );
```

## Summary

Release GPIO pins

## Description

This function release GPIO pins after wakeup from deep sleep.

## Precondition

None.

## Parameters

None.

## Returns

None.

## Example

```c
POWER_ReleaseGPIO();
```

## Remarks

This function is only available for the devices which has deep sleep controller. MHC will generate this function only for the selected devices accordingly. Check device datasheet for more information.

