# PMECC\_CallbackRegister Function

**Parent topic:**[Static Memory Controller \(SMC\)](GUID-415D2D33-E3CB-4AD9-961C-49606E718EF0.md)

## C

```c
void PMECC_CallbackRegister( PMECC_CALLBACK callback, uintptr_t context )
```

## Summary

Sets the pointer to the function \(and it's context\) to be called when the given PMECC's interrupt occurred.

## Description

This function sets the pointer to a client function to be called "back" when the given PMECC's interrupt occurred. It also passes a context value \(usually a pointer to a context structure\) that is passed into the function when it is called. This function is available only in interrupt mode of operation.

## Precondition

PMECC\_Initialize must have been called for the associated PMECC instance.

## Parameters

|Param|Description|
|-----|-----------|
|callback|A pointer to a function with a calling signature defined by thePMECC\_CALLBACK data type|
|context|A value \(usually a pointer\) passed \(unused\) into the functionidentified by the callback parameter|

## Returns

None.

## Example

```c
void pmeccCallback( uintptr_t context, uint32_t interruptStatus )
{
}

PMECC_CallbackRegister(pmeccCallback, (uintptr_t)NULL);
```

## Remarks

The context parameter is ignored if the pointer passed is NULL. To disable the callback function, pass a NULL for the callback parameter. See the PMECC\_CALLBACK type definition for additional information.

