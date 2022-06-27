# FLEXCOM\_TWI\_SLAVE\_TRANSFER\_DIR Enum

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c

/* TWI slave mode */

typedef enum
{
    /* FLEXCOM TWI Master is writing to slave */
    FLEXCOM_TWI_SLAVE_TRANSFER_DIR_WRITE = 0,

    /* FLEXCOM TWI Master is reading from slave */
    FLEXCOM_TWI_SLAVE_TRANSFER_DIR_READ  = 1,
}FLEXCOM_TWI_SLAVE_TRANSFER_DIR;

```

## Summary

Defines the enum for TWI data transfer direction.

## Description

Defines the enum for TWI data transfer direction. The enumeration of this type is returned by the FLEXCOMx\_TWI\_TransferDirGet\(\) function.

## Remarks

None.

