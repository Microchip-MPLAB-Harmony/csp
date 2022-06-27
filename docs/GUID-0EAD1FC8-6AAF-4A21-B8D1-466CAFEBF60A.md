# DWDT\_NS\_RegisterCallback Function

**Parent topic:**[Dual Watchdog Timer \(DWDT\)](GUID-A1DD4B6F-25A6-404C-828C-396AB3D1C637.md)

## C

```c
void DWDT_NS_RegisterCallback(DWDT_CALLBACK pCallback, void* pContext);
```

## Summary

Allows application to register callback with PLIB

## Description

This function allows application to register a callback function for the<br />PLIB to call back when never secure interrupt occurred.

At any point if application wants to stop the callback, it can call this<br />function with "callback" value as NULL.

## Precondition

The DWDT\_Initialize function must have been called and one of the never secure interrupts is enabled.

## Parameters

|Param|Description|
|-----|-----------|
|callback|Pointer to the callback function implemented by the user.|
|pContext|The value of parameter will be passed back to the application unchanged, when the callback function is called. It can be used to identify any application specific value that identifies the instance of the client module \(for example, it may be a pointer to the client module's state structure\).|

## Returns

None.

## Example

```c
MY_APP_OBJ myAppObj;

void APP_DWDT_CallbackFunction (bool interruptStatus, void* pContext)
{
    // The context was set to an application specific object.
    // It is now retrievable easily in Callback function.
    MY_APP_OBJ myAppObj = (MY_APP_OBJ *) context;
    //Application related tasks
}

DWDT_NS_RegisterCallback (APP_DWDT_CallbackFunction, &myAppObj);
```

## Remarks

None.

