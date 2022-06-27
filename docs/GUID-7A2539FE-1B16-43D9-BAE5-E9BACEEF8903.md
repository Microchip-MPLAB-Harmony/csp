# SERCOMx\_USART\_WriteBufferSizeGet Function

**Parent topic:**[Serial Communication Interface \(SERCOM\)](GUID-76AE7205-E3EF-4EE6-AC28-5153E3565982.md)

## C

```c
/* x = SERCOM instance number */

/* Ring buffer mode */

size_t SERCOMx_USART_WriteBufferSizeGet(void)
```

## Summary

Returns the size of the internal transmit ring buffer

## Description

This function returns the size of the transmit ring buffer, which is same as the size of the transmit ring buffer configured in MHC.

## Precondition

SERCOMx\_USART\_Initialize must have been called for the associated SERCOM\_USART instance.

## Parameters

None

## Returns

The API returns the size of the transmit ring buffer. If 9-bit mode is enabled, then the return value indicates the number of 9-bit data that can be copied to the internal transmit ring buffer.

## Example

```c
size_t txBufferSize;

txBufferSize = SERCOM0_USART_WriteBufferSizeGet();

// Set a threshold to get notification when the transmit ring buffer is empty
SERCOM0_USART_WriteThresholdSet(txBufferSize);

```

## Remarks

None

