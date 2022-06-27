# CLC\_CALLBACK Typedef

**Parent topic:**[Configurable Logic Cell \(CLC\)](GUID-ED2CC8FC-B5F9-4657-9B82-EC3DF8D1E096.md)

## C

```c
typedef void (*CLC_CALLBACK)( uintptr_t context)

```

## Summary

Defines the data type and function signature for the CLC peripheral callback function.

## Description

This data type defines the function signature for the CLC peripheral<br />callback function. The CLC peripheral will call back the client's<br />function with this signature when a CLC interrupt occurs.

## Precondition

CLC\_CallbackRegister must have been called to set the function to be called.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\)|

## Returns

None.

