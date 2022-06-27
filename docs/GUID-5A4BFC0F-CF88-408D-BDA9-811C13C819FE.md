# MCANx\_ErrorGet Function

**Parent topic:**[Controller Area Network \(MCAN\)](GUID-C9F1E50C-1EF0-4941-A9CB-89808C7C54AF.md)

## C

```c
MCAN_ERROR MCANx_ErrorGet(void) // x - Instance of the MCAN peripheral
```

## Summary

Returns the error during transfer.

## Precondition

MCANx\_Initialize must have been called for the associated MCAN instance.

## Parameters

None.

## Returns

Error during transfer.

## Example

```c
MCAN_ERROR error;
error = MCAN0_ErrorGet();
```

## Remarks

None.

