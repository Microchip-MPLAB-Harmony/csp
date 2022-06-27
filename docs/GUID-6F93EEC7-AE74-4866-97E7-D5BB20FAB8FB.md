# FLEXCOMx\_USART\_ReadFreeBufferCountGet Function

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-137968B9-4089-44C6-9B5A-2F30929F6852.md)

**Parent topic:**[Flexible Serial Communication Controller \(FLEXCOM\)](GUID-1F0CC449-4122-4C77-A199-A7874C524FDD.md)

## C

```c
/* x = FLEXCOM instance number */

/* Ring buffer mode */

size_t FLEXCOMx_USART_ReadFreeBufferCountGet(void)
```

## Summary

Returns the number of bytes of free space available in the internal receive buffer

## Description

This API returns the number of bytes of free space available in the internal receive buffer. This API can be used to determine how many bytes can be received before the receive buffer becomes full.

## Precondition

FLEXCOMx\_USART\_Initialize must have been called for the associated FLEXCOM\_USART instance.

## Parameters

None

## Returns

The API returns the number of bytes of free space in the receive buffer. If 9-bit mode is enabled, then the return value indicates number of 9-bit data that can be copied into the internal receive buffer.

## Example

```c
size_t nRxFreeSpace;

nRxFreeSpace = FLEXCOM0_USART_ReadFreeBufferCountGet();

```

## Remarks

None

