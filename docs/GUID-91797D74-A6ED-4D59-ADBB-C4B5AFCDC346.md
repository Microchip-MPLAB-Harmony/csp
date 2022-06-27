# SDHC\_RESET\_TYPE Enum

**Parent topic:**[SD/MMC Host Controller \(SDHC\)](GUID-8769733F-B27A-4567-BE7D-7BEA8C76F05E.md)

**Parent topic:**[SD/MMC Host Controller \(SDHC\)](GUID-D440DD4B-CA37-46F4-A6AA-4D57D9DAEF97.md)

## C

```c
typedef enum
{
    // Reset all errors
    SDHC_RESET_ALL = 0x01,
    // Reset command errors
    SDHC_RESET_CMD = 0x02,
    // Reset data errors
    SDHC_RESET_DAT = 0x04
    
} SDHC_RESET_TYPE;

```

## Summary

The enumeration lists the types of errors application can reset

## Description

The enumeration is used to select the error type to reset.

## Remarks

None.

