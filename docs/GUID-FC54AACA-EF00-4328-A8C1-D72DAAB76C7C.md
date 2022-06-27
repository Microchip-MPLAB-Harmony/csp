# DBGU\_ErrorGet Function

**Parent topic:**[Debug Unit \(DBGU\)](GUID-97C41240-2AC0-4D05-A97E-83EB780C57A2.md)

## C

```c

/* x = DBGU instance number */

/* Blocking, non-blocking and ring buffer mode */

DBGU_ERROR DBGU_ErrorGet( void )
```

## Summary

Gets the error of the given DBGU peripheral instance.

## Description

This function returns the errors associated with the given DBGU peripheral instance. Multiple error conditions may be active. The function return value should be matched against each member of the DBGU\_ERROR enumeration to handle all error cases. Calling the DBGUx\_Read will clear the errors, hence error handling must be performed before.

*Blocking mode*

Calling this API clears the hardware errors

*Non-blocking and ring-buffer mode*

Error flags are saved in a register and hardware errors are cleared in the Error interrupt handler. Calling this API clears the error flags saved in the register.

## Precondition

DBGU\_Initialize must have been called for the associated DBGU instance.

## Parameters

None.

## Returns

Errors occurred as listed by DBGU\_ERROR.

## Example

```c
if ((DBGU_ERROR_OVERRUN & DBGU_ErrorGet()) == DBGU_ERROR_OVERRUN)
{
    //Errors are cleared by the API call, take respective action
    //for the overrun error case.
}
```

## Remarks

DBGU errors are normally associated with the receiver. Hence, it is recommended to use this function in receive context only.

