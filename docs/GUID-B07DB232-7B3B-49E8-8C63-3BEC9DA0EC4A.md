# PAC\_CallbackRegister Function

**Parent topic:**[Peripheral Access Controller \(PAC\)](GUID-A41A49A1-F4C5-4355-8F72-3471A2AFF354.md)

## C

```c
void PAC_CallbackRegister( PAC_CALLBACK callback, uintptr_t context )
```

## Summary

Registers the function to be called when a PAC error has occurred.

## Description

This function registers the callback function to be called when a PAC error has occurred. The function is available only when the module interrupt is enabled in MHC.

## Precondition

PAC\_Initialize\(\) function should have been called once. Interrupt option in MHC should have been enabled.

## Parameters

|Param|Description|
|-----|-----------|
|callback|callback function pointer. Setting this to NULL will disable the callback feature.|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\).|

## Returns

None.

## Example

```c
void APP_PACErrorCallback( uintptr_t context )
{
    // PAC Error occurred. Fix the root-cause so that PAC error never occurs.
}

PAC_CallbackRegister(APP_PACErrorCallback, NULL);
```

## Remarks

Context value can be set to NULL if this is not required.

