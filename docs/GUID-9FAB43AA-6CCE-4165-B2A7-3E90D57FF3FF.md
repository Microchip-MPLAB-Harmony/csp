# MCPWM\_Start Function

**Parent topic:**[Motor Control Pulse-Width Modulation \(MCPWM\)](GUID-89C7FC43-0090-4047-99CD-F7EE4881E28E.md)

## C

```c
void MCPWM_Start (void)
```

## Summary

Starts the MCPWM module

## Description

This function enables the MCPWM module.

## Precondition

MCPWM\_Initialize\(\) function must have been called first for the associated instance.

## Parameters

None

## Returns

None.

## Example

```c
MCPWM_Initialize();
MCPWM_Start();
```

## Remarks

None

