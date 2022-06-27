# DBGU\_PARITY Enum

**Parent topic:**[Debug Unit \(DBGU\)](GUID-97C41240-2AC0-4D05-A97E-83EB780C57A2.md)

## C

```c
/* Blocking, non-blocking and ring buffer mode */

typedef enum
{
    DBGU_PARITY_NONE = DBGU_MR_PAR_NO,

    DBGU_PARITY_ODD = DBGU_MR_PAR_ODD,

    DBGU_PARITY_EVEN = DBGU_MR_PAR_EVEN,

    DBGU_PARITY_MARK = DBGU_MR_PAR_MARK,

    DBGU_PARITY_SPACE = DBGU_MR_PAR_SPACE,

    /* Force the compiler to reserve 32-bit space for each enum */
    DBGU_PARITY_INVALID = 0xFFFFFFFF

} DBGU_PARITY;

```

## Summary

Defines the type of parity for DBGU peripheral.

## Description

This may be in the DBGU\_SerialSetup API to change the parity configuration

## Remarks

None

