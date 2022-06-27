# MCPWM\_ChannelPinsOverrideDisable Function

**Parent topic:**[Motor Control Pulse-Width Modulation \(MCPWM\)](GUID-89C7FC43-0090-4047-99CD-F7EE4881E28E.md)

## C

```c
void MCPWM_ChannelPinsOverrideDisable (MCPWM_CH_NUM channel)
```

## Summary

Disables PWM output pins override function

## Description

This function disables override function for PWM output pins PWMH and PWML.<br />When override is disabled, PWM generation logic controls the PWMH and PWML states.

## Precondition

MCPWM\_Initialize\(\) must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|channel|MCPWM channel number|

## Returns

None.

## Example

```c
MCPWM_Initialize();
MCPWM_ChannelPinsOverrideDisable(MCPWM_CH_0);
```

## Remarks

None

