# I2Cx\_IsBusy Function

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-9FF2770C-87B8-47A2-830B-AA9EB23ACFEC.md)

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-84B7C9F3-533A-4A83-9104-9196F8070FF2.md)

## C

```c
/* x = I2C instance number */

/* I2C master mode and slave mode */

bool I2Cx_IsBusy(void)
```

## Summary

Returns the Peripheral busy status.

## Description

*I2C master mode*

In master mode, this function returns true if the I2Cx module is busy with a transfer. The application can use this function to check if I2Cx module is busy before calling any of the data transfer functions. The library does not allow a data transfer operation if another transfer operation is already in progress.

*I2C slave mode*

In slave mode, the function returns true if a start bit has been detected last on the bus by the peripheral. The application can use this API to ensure no I2C transfer is in progress.

## Precondition

I2Cx\_Initialize must have been called for the associated I2C instance.

## Parameters

None.

## Returns

*true* - Busy

*false* - Not busy

## Example

```c
// wait for the current transfer to complete
while(I2C1_IsBusy());

```

## Remarks

None.

