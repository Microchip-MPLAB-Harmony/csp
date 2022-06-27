# SUPC\_BOD33CallbackRegister Function

**Parent topic:**[Supply Controller \(SUPC\)](GUID-CAEF0560-90E6-45AA-96D0-FAEAF26EDC48.md)

## C

```c
void SUPC_BOD33CallbackRegister( SUPC_BOD33_CALLBACK callback, uintptr_t context );
```

## Summary

Registers the function to be called when a Brown Out Event has occurred.

## Description

This function registers the callback function to be called when a Brown Out<br />event has occurred. Note that the callback function will be called only if<br />the BOD33 action setting is configured to generate an interrupt<br />and not reset the system.

## Precondition

SUPC\_Initialize\(\) must have been called before registering a callback.

## Parameters

|Param|Description|
|-----|-----------|
|callback|callback function pointer.|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\).|

## Returns

None.

## Example

```c
MY_APP_OBJ myAppObj;

void APP_SUPC_CallbackFunction (uintptr_t context)
{
    // The context was set to an application specific object.
    // It is now retrievable easily in the event handler.
    MY_APP_OBJ myAppObj = (MY_APP_OBJ *) context;

    //Application related tasks
}

SUPC_BOD33CallbackRegister(APP_SUPC_CallbackFunction, (uintptr_t)&myAppObj);
```

## Remarks

Context value can be set to NULL if not required. To disable callback function, pass NULL for the callback parameter

