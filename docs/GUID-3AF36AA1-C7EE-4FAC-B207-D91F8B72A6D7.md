# DBGU\_SERIAL\_SETUP Struct

**Parent topic:**[Debug Unit \(DBGU\)](GUID-97C41240-2AC0-4D05-A97E-83EB780C57A2.md)

## C

```c

/* Blocking, non-blocking and ring buffer mode */

typedef struct
{
    uint32_t baudRate;

    DBGU_PARITY parity;

} DBGU_SERIAL_SETUP;

```

## Summary

Defines the data type for the DBGU serial setup.

## Description

This can be used to define a serial setup which may then be used to change the serial setup of the DBGU dynamically by passing an instance of this struct as an argument to the DBGU\_SerialSetup API.

## Remarks

None

