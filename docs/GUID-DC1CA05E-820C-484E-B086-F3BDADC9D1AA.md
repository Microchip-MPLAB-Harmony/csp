# CMP\_2\_CallbackRegister Function

**Parent topic:**[Comparator \(CMP\)](GUID-5BD1D290-3AAC-4ABB-A328-057E411239D0.md)

**Parent topic:**[Comparator \(CMP\)](GUID-F17BE981-0CE8-4C1F-8A22-280FD64FEC4B.md)

## C

```c
void CMP_2_CallbackRegister(CMP_CALLBACK callback, uintptr_t context);
```

## Summary

Registers the function to be called from interrupt.

## Description

This function registers the callback function to be called from interrupt.

## Precondition

CMP\_Initialize must have been called.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\).|

## Returns

None.

## Example

```c
uintptr_t cmp2_context = 0;
void cmp2_cb(uintptr_t context)

CMP_2_CallbackRegister(cmp2_cb, cmp2_context);
```

## Remarks

None.

