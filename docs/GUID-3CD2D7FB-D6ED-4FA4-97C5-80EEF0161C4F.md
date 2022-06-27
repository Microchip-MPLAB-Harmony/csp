# RSWDT\_CALLBACK Typedef

**Parent topic:**[Reinforced Safety Watchdog Timer \(RSWDT\)](GUID-17C65C1B-EC26-4F1C-9599-EA23E3B7D00B.md)

## C

```c
typedef void (*RSWDT_CALLBACK)(uintptr_t context)
```

## Summary

Defines the data type and function signature for the RSWDT peripheral callback function.

## Description

This data type defines the function signature for the RSWDT peripheral callback function. The RSWDT peripheral will call back the client's function with this signature when the Timeout event has occurred. This feature may or may not be available based on device.

## Precondition

RSWDT\_Initialize must have been called for the given RSWDT peripheral instance and RSWDT\_CallbackRegister must have been called to set the function to be called.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointerto the callers context for multi-instance clients\)|

## Returns

None.

## Remarks

None.

