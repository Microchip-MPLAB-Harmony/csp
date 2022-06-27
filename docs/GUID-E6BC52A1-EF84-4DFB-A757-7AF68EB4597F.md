# FLEXCOM\_TWI\_CALLBACK Typedef

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c
/* TWI master mode */

typedef void (*FLEXCOM_TWI_CALLBACK) (uintptr_t contextHandle)

```

## Summary

Defines the data type and function signature for the FLEXCOM TWI peripheral callback function in TWI master mode.

## Description

This data type defines the function signature for the FLEXCOM TWI peripheral callback function. The FLEXCOM TWI peripheral will call back the client's function with this signature when the FLEXCOM TWI Transfer has completed.

## Precondition

FLEXCOMx\_TWI\_Initialize must have been called for the given FLEXCOM TWI peripheral instance and FLEXCOMx\_TWI\_CallbackRegister must have been called to set the function to be called. The callback register function should have been called before a I2C transfer has been initiated.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context\).|

## Returns

None.

## Example

```c
void FLEXCOM0_TWI_Callback(uintptr_t context)
{
    if(FLEXCOM0_TWI_ErrorGet() == FLEXCOM_TWI_ERROR_NONE)
    {
        //Transfer is completed successfully
    }
    else
    {
        //Error occurred during transfer.
    }
}

// Register Callback function which is defined above
FLEXCOM0_TWI_CallbackRegister(FLEXCOM0_TWI_Callback, (uintptr_t)NULL);

```

## Remarks

None

