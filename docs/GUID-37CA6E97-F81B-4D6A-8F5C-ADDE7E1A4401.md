# SDHC\_CALLBACK Typedef

**Parent topic:**[SD/MMC Host Controller \(SDHC\)](GUID-8769733F-B27A-4567-BE7D-7BEA8C76F05E.md)

**Parent topic:**[SD/MMC Host Controller \(SDHC\)](GUID-D440DD4B-CA37-46F4-A6AA-4D57D9DAEF97.md)

## C

```c
typedef void (*SDHC_CALLBACK) (SDHC_XFER_STATUS xferStatus, uintptr_t context);

```

## Summary

Defines the prototype of the SDHC callback function

## Description

Application must define an event handler confirming to this prototype and<br />register this event handler with the SDHC PLIB by passing the address of the<br />event handler. The event handler will be called by the SDHC PLIB when a SDHC interrupt<br />occurs to notify the application of the transfer status.

## Remarks

None.

