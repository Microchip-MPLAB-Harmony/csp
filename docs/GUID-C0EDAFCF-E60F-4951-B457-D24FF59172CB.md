# TWIHSx\_Initialize Function

**Parent topic:**[Two-wire Interface - TWIHS](GUID-C8012FE8-F7B4-4CE6-84B4-61EAAFAB03B0.md)

## C

```c
/* x = TWIHS instance number */

/* TWIHS master and slave mode */
void TWIHSx_Initialize(void)
```

## Summary

Initializes the instance of the TWIHS peripheral in either master or slave mode.

## Description

This function initializes the given instance of the TWIHS peripheral as configured by the user from the MHC.

## Precondition

None.

## Parameters

None.

## Returns

None

## Example

```c
TWIHS1_Initialize();
```

## Remarks

Resets the TWIHS module if it was already running and reinitializes it.

