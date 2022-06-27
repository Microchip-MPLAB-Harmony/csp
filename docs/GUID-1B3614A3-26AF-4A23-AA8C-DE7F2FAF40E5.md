# MCSPIx\_ErrorGet Function

**Parent topic:**[Multi Channel Serial Peripheral Interface \(MCSPI\)](GUID-A3A5277D-BAE3-4BD0-91E9-D4E7E0608BE7.md)

## C

```c
/* x = MCSPI instance number */

/* MCSPI slave mode */
MCSPI_SLAVE_ERROR MCSPIx_ErrorGet(void)
```

## Summary

Returns the status of MCSPI transfer

## Description

This function returns the error status of the last MCSPI transfer. Applicaiton must check the status of a transfer in the application callback and take appropriate action in case there is an error during the data transfer. Calling this API clears the error status flags.

## Precondition

The MCSPIx\_Initialize\(\) should have been called.

## Parameters

None.

## Returns

*MCSPI\_SLAVE\_ERROR* - MCSPI Slave Errors

## Example

```c
void MCSPIEventHandler(uintptr_t context )
{
    if (MCSPI1_ErrorGet() == MCSPI_SLAVE_ERROR_NONE)
    {
        nBytesAvailable = MCSPI1_ReadCountGet();
        
        nBytesRead = MCSPI1_Read(APP_RxData, nBytesAvailable);
    }
    else
    {
        // Handle error
    }
    
}

MCSPI1_CallbackRegister(MCSPIEventHandler, (uintptr_t) 0);
```

## Remarks

None.

