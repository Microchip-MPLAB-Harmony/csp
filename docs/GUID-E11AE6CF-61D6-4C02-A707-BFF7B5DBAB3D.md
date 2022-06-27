# I2Cx\_Read Function

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-9FF2770C-87B8-47A2-830B-AA9EB23ACFEC.md)

**Parent topic:**[Inter-Integrated Circuit - I2C](GUID-84B7C9F3-533A-4A83-9104-9196F8070FF2.md)

## C

```c
/* x = I2C instance number */

/* I2C master mode */
bool I2Cx_Read(uint16_t address, uint8_t *pdata, size_t length)
```

## Summary

Reads data from the slave.

## Description

This function reads the data from a slave on the bus. The function will attempt to read length number of bytes into pdata buffer from a slave whose address is specified as address. The I2C Master generates a Start condition, reads the data and then generates a Stop Condition. If the slave NAKs the request or a bus error is encountered on the bus, the transfer is terminated. The application can call I2Cx\_ErrorGet\(\) function to know the cause of the error. The function is non-blocking. It initiates bus activity and returns immediately. The transfer is completed in the peripheral interrupt. A transfer request cannot be placed when another transfer is in progress. Calling the read function when another function is already in progress will cause the function to return false. The library will call the registered callback function when the transfer has completed if callback is registered.

## Precondition

I2Cx\_Initialize must have been called for the associated I2C instance.

## Parameters

|Param|Description|
|-----|-----------|
|address|7-bit / 10-bit slave address.|
|pdata|pointer to destination data buffer where the received data should be stored.|
|length|Number of bytes to be read|

## Returns

*true* - The request was placed successfully and the bus activity was initiated

*false* - The request fails, if there was already a transfer in progress when this function was called

## Example

```c
uint8_t myData [NUM_BYTES];
uint8_t myData [NUM_BYTES];
void MyI2CCallback(uintptr_t context)
{
    // This function will be called when the transfer completes. Note
    // that this function executes in the context of the I2C interrupt.
}

I2C1_Initialize();
I2C1_CallbackRegister(MyI2CCallback, NULL);

if(!I2C1_Read( SLAVE_ADDR, &myData[0], NUM_BYTES ))
{
    // error handling
}

```

## Remarks

None

