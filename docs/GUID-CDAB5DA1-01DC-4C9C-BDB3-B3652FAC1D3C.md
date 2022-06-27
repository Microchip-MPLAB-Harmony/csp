# MCPWM\_CallbackRegister Function

**Parent topic:**[Motor Control Pulse-Width Modulation \(MCPWM\)](GUID-89C7FC43-0090-4047-99CD-F7EE4881E28E.md)

## C

```c
void MCPWM_CallbackRegister (MCPWM_CH_NUM channel, MCPWM_CH_CALLBACK callback, uintptr_t context)
```

## Summary

Registers the function to be called from interrupt

## Description

This function registers the callback function to be called from interrupt

## Precondition

MCPWM\_Initialize\(\) must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|channel|MCPWM channel number|
|callback|callback function pointer|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\)|

## Returns

None.

## Example

```c
void MCPWM_Callback_Fn(MCPWM_CH_STATUS status, uintptr_t context);

MCPWM_Initialize();
MCPWM_CallbackRegister(MCPWM_CH_0, MCPWM_Callback_Fn, NULL);
```

## Remarks

Context value can be set to NULL if not required. To disable callback function, pass NULL for the callback parameter.

