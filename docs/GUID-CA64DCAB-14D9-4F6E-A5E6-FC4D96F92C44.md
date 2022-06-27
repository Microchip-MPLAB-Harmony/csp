# TWI\_CALLBACK Typedef

**Parent topic:**[Two-wire Interface - TWI](GUID-384E478E-B880-4F6B-83D6-792074118820.md)

## C

```c
/* TWI master mode */
typedef void (*TWI_CALLBACK) (uintptr_t contextHandle);

```

## Summary

Defines the data type and function signature for the TWI peripheral callback function in TWI master mode.

## Description

This data type defines the function signature for the TWI peripheral callback function. The TWI peripheral will call back the client's function with this signature when the TWI Transfer event has occurred.

## Precondition

TWIx\_Initialize must have been called for the given TWI peripheral instance and TWIx\_CallbackRegister must have been called to set the function to be called.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context\).|

## Returns

None.

## Example

```c
void TWI1_Callback(uintptr_t context)
{
    if(TWI1_ErrorGet() == TWI_ERROR_NONE)
    {
        //Transfer is completed successfully
    }
    else
    {
        //Error occurred during transfer.
    }
}

// Register Callback function which is defined above
TWI1_CallbackRegister(TWI1_Callback, (uintptr_t)NULL);

```

## Remarks

None

