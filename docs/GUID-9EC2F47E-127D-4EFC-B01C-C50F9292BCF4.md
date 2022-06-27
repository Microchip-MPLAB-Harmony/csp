# TWIHSx\_ErrorGet Function

**Parent topic:**[Two-wire Interface - TWIHS](GUID-C8012FE8-F7B4-4CE6-84B4-61EAAFAB03B0.md)

## C

```c
/* x = TWIHS instance number */

/* TWIHS master mode */
TWIHS_ERROR TWIHSx_ErrorGet(void)
```

## Summary

Returns the TWIHS error that occurred on the bus.

## Description

This function returns the TWIHS error that occurred on the bus. The function can be called to identify the error cause.

## Precondition

TWIHSx\_Initialize must have been called for the associated TWIHS instance.

## Parameters

None.

## Returns

Returns error of type TWIHS\_ERROR, identifying the error that has occurred.

## Example

```c
if(TWIHS1_ErrorGet() == TWIHS_ERROR_NONE)
{
    //Transfer is completed successfully
}
else
{
    //Error occurred during transfer.
}
```

## Remarks

None

