# SPIx\_ReadBufferSizeGet Function

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-246C53F6-3912-4437-AEC8-C2262CEF3EF6.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-CBD5BFEF-57AB-4CA0-92C0-00CB1A72D686.md)

**Parent topic:**[Serial Peripheral Interface \(SPI\)](GUID-84F93473-4002-4DDD-A28F-9BF9DB6B7C3E.md)

## C

```c
/* x = SPI instance number */

/* SPI slave mode */
size_t SPIx_ReadBufferSizeGet(void)
```

## Summary

Returns the size of the PLIB's internal receive buffer

## Description

This function returns the size of the SPI PLIB's internal receive buffer. The receive buffer size will be the same as configured in MHC

## Precondition

None

## Parameters

None

## Returns

*size\_t* - Size of the PLIB's internal receive buffer

## Example

```c
size_t rxBufferSize;

rxBufferSize = SPI1_ReadBufferSizeGet();

```

## Remarks

None

