# SDMMC\_CALLBACK Typedef

**Parent topic:**[Secure Digital MultiMedia Card Controller \(SDMMC\)](GUID-670F0003-D51D-457F-BF15-845C30D30C12.md)

**Parent topic:**[Secure Digital MultiMedia Card Controller \(SDMMC\)](GUID-9384AD3C-4E33-479E-B7BB-005772421CB2.md)

## C

```c
typedef void (*SDMMC_CALLBACK) (SDMMC_XFER_STATUS xferStatus, uintptr_t context);

```

## Summary

The prototype of the SDMMC callback function

## Description

The clients must define an event handler confirming to this prototype and<br />register this event handler with the SDMMC PLIB by passing the address of the<br />event handler.

## Remarks

None

