# HEFC\_CallbackRegister Function

**Parent topic:**[Harden Embedded Flash Controller \(HEFC\)](GUID-483B2DE9-95CB-4DD4-9F85-592F15C38EFA.md)

## C

```c
void HEFC_CallbackRegister( HEFC_CALLBACK callback, uintptr_t context )
```

## Summary

Sets the pointer to the function \(and it's context\) to be called when the operation is complete.

## Description

This function sets the pointer to a client function to be called "back" when the HEFC is ready to receive new command. It also passes a context value that is passed into the function when it is called. This function is available only in interrupt mode of operation.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|callback|A pointer to a function with a calling signature definedby the HEFC\_CALLBACK data type.|
|context|A value \(usually a pointer\) passed \(unused\) into the functionidentified by the callback parameter.|

## Returns

None.

## Example

```c
HEFC_CallbackRegister(MyCallback, &myData);
```

## Remarks

The context value may be set to NULL if it is not required. Note that the value of NULL will still be passed to the callback function. To disable the callback function, pass a NULL for the callback parameter. See the HEFC\_CALLBACK type definition for additional information.

