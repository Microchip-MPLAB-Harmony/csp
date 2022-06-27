# NVM\_ERROR Enum

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-A1DC59E3-704B-445E-BE7D-D91D9DADD4A1.md)

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-04191B57-EC62-4B95-AF5B-93EDB447F6D9.md)

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-C41BA1D1-EFF7-435E-901E-9A87AC140FE6.md)

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-12DDB483-6D09-44C5-85F0-913D0B5A77E8.md)

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-DBFE92F8-C187-4C24-98FB-E04BB9C2248E.md)

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-06D0A6A6-55BF-4C5F-8CFB-864ED17D97ED.md)

**Parent topic:**[Non-Volatile Memory \(NVM\)](GUID-B0854C03-A30D-4E50-A3A5-948BE02E7EE8.md)

## C

```c
typedef enum
{
    /* No error */
    NVM_ERROR_NONE = 0x0,

    /* NVM write error */
    NVM_ERROR_WRITE = _NVMCON_WRERR_MASK,

    /* NVM Low Voltage Detect error */
    NVM_ERROR_LOWVOLTAGE = _NVMCON_LVDERR_MASK,

} NVM_ERROR;

```

## Summary

Defines the NVM Error Type.

## Description

This enumeration defines the NVM Error type.

## Remarks

The NVM\_ErrorGet function returns a value of this type.

