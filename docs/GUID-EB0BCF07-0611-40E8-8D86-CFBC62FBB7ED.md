# EFC\_CALLBACK Typedef

**Parent topic:**[Embedded Flash Controller \(EFC\)](GUID-9D57DC2E-2BF0-4D75-9E5E-FE57C7CDCC4C.md)

## C

```c
typedef void (*EFC_CALLBACK)(uintptr_t context);

```

## Summary

Defines the data type and function signature for the EFC peripheral callback function.

## Description

This data type defines the function signature for the EFC peripheral callback function. The EFC peripheral will callback the client's function with this signature when EFC is ready to accept new operation.

## Precondition

EFC\_CallbackRegister must have been called to set the function to be called.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointerto the callers context for multi-instance clients\).|

## Returns

None.

