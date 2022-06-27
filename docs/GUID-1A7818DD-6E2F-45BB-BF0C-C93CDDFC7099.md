# MCSPI\_CALLBACK Typedef

**Parent topic:**[Multi Channel Serial Peripheral Interface \(MCSPI\)](GUID-A3A5277D-BAE3-4BD0-91E9-D4E7E0608BE7.md)

## C

```c
/* MCSPI master (non-blocking mode) mode */

typedef void (*MCSPI_CALLBACK) (uintptr_t context)

```

## Summary

Defines the data type and function signature for the MCSPI \(master\) peripheral callback function.

## Description

This data type defines the function signature for the MCSPI \(master\) peripheral callback function. The MCSPI peripheral will call back the client's function with this signature when the MCSPI Transfer has completed.

## Precondition

MCSPIx\_Initialize must have been called for the given MCSPI peripheral instance and MCSPIx\_CallbackRegister must have been called to set the function to be called. The callback register function must be called before initiating the MCSPI transfer.

## Parameters

|Param|Description|
|-----|-----------|
|context|Allows the caller to provide a context value \(usually a pointer to the callers context for multi-instance clients\).|

## Returns

None

## Example

```c

void APP_MCSPITransferHandler(uintptr_t context)
{
    //Transfer completed
}

MCSPI1_CallbackRegister(&APP_MCSPITransferHandler, (uintptr_t)NULL);

```

## Remarks

None

