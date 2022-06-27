# QEIx\_CallbackRegister Function

**Parent topic:**[Quadrature Encoder Interface \(QEI\)](GUID-62A23819-A256-4FB3-9682-BA733F4B45AA.md)

## C

```c

/* x = QEI instance number */

void QEIx_CallbackRegister ( QEI_CALLBACK callback, uintptr_t context )
```

## Summary

Registers the function to be called from interrupt.

## Description

This function registers the callback function to be called from interrupt

## Precondition

QEIx\_Initialize must have been called first.

## Parameters

|Param|Description|
|-----|-----------|
|callback|Callback function pointer|
|context|Value provided back to the caller by the callback \(usually a pointer to the caller's context for multi-instance clients\)|

## Returns

None.

## Example

```c
void QEI_CallbackFn(QEI__STATUS status, uintptr_t context);

QEI_Initialize();
QEI_CallbackRegister(QEI_CallbackFn, NULL);
```

## Remarks

Context value can be set to NULL if not required. To disable callback function, pass NULL for the callback parameter.

