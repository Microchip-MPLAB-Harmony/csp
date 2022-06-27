# I2Cx\_Initialize Function

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-9FF2770C-87B8-47A2-830B-AA9EB23ACFEC.md)

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-84B7C9F3-533A-4A83-9104-9196F8070FF2.md)

## C

```c
/* x = I2C instance number */

/* TWI master and slave mode */
void I2Cx_Initialize(void)
```

## Summary

Initializes the instance of the I2C peripheral in either master or slave mode.

## Description

This function initializes the given instance of the I2C peripheral as configured by the user from the MHC.

## Precondition

None

## Parameters

None.

## Returns

None.

## Example

```c
I2C1_Initialize();
```

## Remarks

None

