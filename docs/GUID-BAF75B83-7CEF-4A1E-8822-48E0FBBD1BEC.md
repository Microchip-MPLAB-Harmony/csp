# ADCHS\_CallbackRegister Function

**Parent topic:**[Analog to Digital Converter \(ADCHS\)](GUID-8740EC52-3365-4B31-B19A-227EC55268DD.md)

## C

```c
void ADCHS_CallbackRegister (ADCHS_CHANNEL_NUM channel, ADCHS_CALLBACK callback, uintptr_t context)
```

## Summary

Registers the function to be called from interrupt

## Description

This function registers the callback function to be called from interrupt

## Precondition

ADCHS\_Initialize\(\) must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|channel|Analog channel number|
|callback|callback function pointer|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\)|

## Returns

None.

## Example

```c
void ADCHS_Callback_Fn(ADCHS_CHANNEL_NUM channel, uintptr_t context)
{
}

ADCHS_Initialize();
ADCHS_CallbackRegister(ADCHS_CH0, ADCHS_Callback_Fn, NULL);
```

## Remarks

Context value can be set to NULL if not required. To disable callback function, pass NULL for the callback parameter.

