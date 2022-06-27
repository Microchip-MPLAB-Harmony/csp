# I2C\_CALLBACK Typedef

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-9FF2770C-87B8-47A2-830B-AA9EB23ACFEC.md)

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-84B7C9F3-533A-4A83-9104-9196F8070FF2.md)

## C

```c
/* I2C master mode */

typedef void (*I2C_CALLBACK) (uintptr_t contextHandle)

```

## Summary

Defines the data type and function signature for the I2C peripheral callback function in I2C master mode.

## Description

This data type defines the function signature for the I2C peripheral callback function. The I2C peripheral will call back the client's function with this signature when the I2C transfer has completed.

## Precondition

I2Cx\_Initialize must have been called for the given I2C peripheral instance and I2Cx\_CallbackRegister must have been called to set the function to be called. The callback register function should have been called before a I2C transfer has been initiated.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context\).|

## Returns

None.

## Example

```c
void I2C1_Callback(uintptr_t context)
{
    if(I2C1_ErrorGet() == I2C_ERROR_NONE)
    {
        //Transfer is completed successfully
    }
    else
    {
        //Error occurred during transfer.
    }
}

// Register Callback function which is defined above
I2C1_CallbackRegister(I2C1_Callback, (uintptr_t)NULL);

```

## Remarks

None

