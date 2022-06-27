# SERCOM\_I2C\_ERROR Enum

**Parent topic:**[Serial Communication Interface \(SERCOM\)](GUID-76AE7205-E3EF-4EE6-AC28-5153E3565982.md)

## C

```c

/* I2C master mode */

typedef enum
{
    /* No error has occurred. */
    SERCOM_I2C_ERROR_NONE,
    
    /* A bus transaction was NAK'ed */
    SERCOM_I2C_ERROR_NAK,
    
    /* A bus error has occurred. */
    SERCOM_I2C_ERROR_BUS,
    
} SERCOM_I2C_ERROR;

```

## Summary

Defines the possible errors that the SERCOM I2C peripheral can generate in I2C master mode.

## Description

This enum defines the possible error the SERCOM I2C peripheral can generate when it is configured in master mode. An error of this type is returned by the SERCOMx\_I2C\_ErrorGet\(\) function.

## Remarks

None

