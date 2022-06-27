# CLC\_CallbackRegister Function

**Parent topic:**[Configurable Logic Cell \(CLC\)](GUID-ED2CC8FC-B5F9-4657-9B82-EC3DF8D1E096.md)

## C

```c
/* x = CLC instance number */

void CLC_CallbackRegister (CLC_CALLBACK callback, uintptr_t context)
```

## Summary

Registers the function to be called from interrupt

## Description

This function registers the callback function to be called from interrupt

## Precondition

CLC\_Initialize\(\) must have been called.

## Parameters

|Param|Description|
|-----|-----------|
|callback|callback function pointer|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\).|

## Returns

None.

## Example

```c
void CLC_Callback_Fn(uintptr_t context);

CLC1_Initialize();
CLC1_CallbackRegister(CLC_Callback_Fn, NULL);
```

## Remarks

Context value can be set to NULL if not required. To disable callback function, pass NULL for the callback parameter.

