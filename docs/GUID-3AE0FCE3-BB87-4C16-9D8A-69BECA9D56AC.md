# MCPWM\_Initialize Function

**Parent topic:**[Motor Control Pulse-Width Modulation \(MCPWM\)](GUID-89C7FC43-0090-4047-99CD-F7EE4881E28E.md)

## C

```c
void MCPWM_Initialize (void)
```

## Summary

Initializes given instance of MCPWM peripheral

## Description

This function initializes given instance of MCPWM peripheral with the values<br />configured in MCC GUI. This initializes all the selected generators of given peripheral in MCC GUI.

## Precondition

MCC GUI should be configured with the right values.

## Parameters

None.

## Returns

None.

## Example

```c
MCPWM_Initialize();
```

## Remarks

This function must be called before any other MCPWM function is called. This function should only be called once during system initialization.

