# ACC\_CALLBACK Typedef

**Parent topic:**[Analog Comparator Controller \(ACC\)](GUID-113695BA-6EDE-4E03-83C0-A23EE4A11753.md)

## C

```c
typedef void (*ACC_CALLBACK) (uintptr_t context);

```

## Summary

Pointer to a ACC callback function

## Description

This data type defines the required function signature for the ACC callback function. Application must register a pointer to a callback function whose function signature \(parameter and return value types\) match the types specified by this function pointer in order to receive callback from the PLIB.

The parameters and return values are described here and a partial example implementation is provided.

## Parameters

context Value identifying the context of the application that registered the callback function.

## Returns

None.

## Example

```c
ACC_CallbackRegister (&APP_ACC_CallbackFunction, NULL);
void APP_ACC_CallbackFunction (uintptr_t context)
{
    //Application related tasks
}
```

## Remarks

The context parameter contains the a handle to the client context, provided at the time the callback function was registered using the ACC\_CallbackRegister function. This context handle value is passed back to the client as the "context" parameter. It can be any value \(such as a pointer to the client's data\) necessary to identify the client context or instance of the client that made the data transfer request. The callback function executes in the PLIB's interrupt context. It is recommended of the application to not perform process intensive or blocking operations with in this function.

