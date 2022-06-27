# SUPC\_CALLBACK Typedef

**Parent topic:**[Supply Controller \(SUPC\)](GUID-09165D4A-27D7-4560-B218-E23AC70218F8.md)

**Parent topic:**[Supply Controller \(SUPC\)](GUID-AAEA9536-A589-47D4-B8D4-9C401B40C9AC.md)

**Parent topic:**[Supply Controller \(SUPC\)](GUID-9BDF339F-E2FE-41C7-96E3-E550DAE91D45.md)

## C

```c
typedef void (*SUPC_CALLBACK)( uintptr_t context );

```

## Summary

Pointer to a SUPC peripheral callback function.

## Description

This data type defines the function signature for the SUPC peripheral<br />callback function. Application must register a pointer to a callback<br />function whose function signature \(parameter and return value types\) match<br />the types specified by this function pointer in order to receive callback<br />from the PLIB.

**On some devices** the SUPC peripheral library will call back the client's<br />function with this signature when a Brown Out event has been detected.<br />The function will be called only if the BOD33 action in the NVM user row<br />is set to interrupt.

## Remarks

SUPC\_Initialize\(\) must have been called for the supc peripheral before registering a callback.

SUPC\_CallbackRegister\(\) must have been called to set the function to be called.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\).|

## Returns

None.

## Example

```c
void APP_SUPC_CallbackFunction( uintptr_t context )
{
    // Code to perform any quick action before the supply dies.
}

SUPC_CallbackRegister(APP_SUPC_CallbackFunction, (uintptr_t)NULL);
```

## Remarks

The context parameter contains a handle to the client context, provided at the time the callback function was registered using the SUPC\_CallbackRegister\(\) function.

This context handle value is passed back to the client as the "context" parameter. It can be any value \(such as a pointer to the client's data\) necessary to identify the client context or instance of the client that made the request.

The callback function executes in the PLIB's interrupt context. It is recommended of the application to not perform process intensive or blocking operations with in this function.

