# SERCOMx\_USART\_FrequencyGet Function

**Parent topic:**[Serial Communication Interface \(SERCOM\)](GUID-76AE7205-E3EF-4EE6-AC28-5153E3565982.md)

## C

```c
/* x = SERCOM instance number */

/* Blocking, non-blocking and ring buffer mode */

uint32_t SERCOMx_USART_FrequencyGet( void )
```

## Summary

Provides the given SERCOM peripheral frequency.

## Description

This function provides the frequency at which the given SERCOM operates.

## Precondition

SERCOMx\_USART\_Initialize must have been called for the associated USART instance.

## Parameters

None.

## Returns

The frequency \(in Hz\) at which the timer's counter increments.

## Example

```c
uint32_t frequency = 0;

SERCOM0_USART_Initialize();
frequency = SERCOM0_USART_FrequencyGet();
```

## Remarks

None.

