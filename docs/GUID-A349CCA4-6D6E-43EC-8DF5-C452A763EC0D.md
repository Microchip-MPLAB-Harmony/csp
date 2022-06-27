# SERCOMx\_SPI\_WriteBufferSizeGet Function

**Parent topic:**[Serial Communication Interface \(SERCOM\)](GUID-76AE7205-E3EF-4EE6-AC28-5153E3565982.md)

## C

```c
/* x = SERCOM instance number */

/* SPI slave mode */

size_t SERCOMx_SPI_WriteBufferSizeGet(void)
```

## Summary

Returns the size of the PLIB's internal transmit buffer

## Description

This function returns the size of the SPI PLIB's internal transmit buffer. The transmit buffer size will be the same as configured in MHC.

## Precondition

None

## Parameters

None

## Returns

*size\_t* - Size of the PLIB's internal transmit buffer

## Example

```c
size_t txBufferSize;

txBufferSize = SERCOM0_SPI_WriteBufferSizeGet();

```

## Remarks

None.

