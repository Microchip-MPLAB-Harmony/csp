# CMP\_CALLBACK Typedef

**Parent topic:**[Comparator \(CMP\)](GUID-5BD1D290-3AAC-4ABB-A328-057E411239D0.md)

**Parent topic:**[Comparator \(CMP\)](GUID-F17BE981-0CE8-4C1F-8A22-280FD64FEC4B.md)

## C

```c
typedef void (*CMP_CALLBACK) (uintptr_t context);
```

## Summary

Defines the function pointer data type and function signature for the CMP callback function.

## Description

The library will call back the client's function with this signature,<br />from the interrupt routine.

## Precondition

CMP\_Initialize must have been called. CMP\_x\_CallbackRegister must have been called to register the function to be called for a specific comparator.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\).|

## Returns

None.

## Example

```c
uintptr_t cmp1_context = 0;
void cmp1_cb(uintptr_t context)

CMP_1_CallbackRegister(cmp1_cb, cmp1_context);
```

## Remarks

None.

