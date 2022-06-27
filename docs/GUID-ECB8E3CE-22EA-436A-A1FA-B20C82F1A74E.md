# I2Cx\_ErrorGet Function

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-9FF2770C-87B8-47A2-830B-AA9EB23ACFEC.md)

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-84B7C9F3-533A-4A83-9104-9196F8070FF2.md)

## C

```c
/* x = I2C instance number */

/* I2C master mode */
I2C_ERROR I2Cx_ErrorGet(void)	

/* I2C slave mode */		
I2C_SLAVE_ERROR I2Cx_ErrorGet(void)	
```

## Summary

Returns the I2C error that occurred on the bus.

## Description

This function returns the I2C error that occurred on the bus. The function can be called to identify the error cause.

## Precondition

I2Cx\_Initialize must have been called for the associated I2C instance.

## Parameters

None.

## Returns

Returns error of type I2C\_ERROR \(when I2C is in master mode\) or I2C\_SLAVE\_ERROR \(when I2C is in slave mode\), identifying the error that has occurred.

## Example

*I2C in master mode:*

```c
if(I2C1_ErrorGet() == I2C_ERROR_NONE)
{
    //Transfer is completed successfully
}
else
{
    //Error occurred during transfer.
}
```

*I2C in slave mode:*

```c
if(I2C1_ErrorGet() == I2C_SLAVE_ERROR_NONE)
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

