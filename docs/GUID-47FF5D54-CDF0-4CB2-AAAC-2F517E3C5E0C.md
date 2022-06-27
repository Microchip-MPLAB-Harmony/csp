# RTT\_CALLBACK Typedef

**Parent topic:**[Real-time Timer \(RTT\)](GUID-2A29BDE4-A969-4CEB-A21C-AF161D295289.md)

## C

```c
typedef void (*RTT_CALLBACK)(RTT_INTERRUPT_TYPE type, uintptr_t context);

```

## Summary

Defines the data type and function signature for the RTT peripheral callback function.

## Description

This data type defines the function signature for the RTT peripheral callback function. The RTT peripheral will call back the client's function with this signature once the alarm match or periodic interrupt occurs.

## Precondition

RTT\_CallbackRegister must have been called to set the function to be called.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\)|
|type|Reason for the interrupt|

## Returns

None.

