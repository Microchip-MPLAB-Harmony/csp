# TWIx\_Initialize Function

**Parent topic:**[Two-wire Interface - TWI](GUID-384E478E-B880-4F6B-83D6-792074118820.md)

## C

```c
/* x = TWI instance number */

/* TWI master mode */
void TWIx_Initialize(void)
```

## Summary

Initializes given instance of the TWI peripheral.

## Description

This function initializes the given instance of the TWI peripheral as configured by the user from the MHC.

## Precondition

None.

## Parameters

None.

## Returns

None

## Example

```c
TWI1_Initialize();
```

## Remarks

Resets the TWI module if it was already running and reinitializes it

