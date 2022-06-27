# USART\_STOP\_BIT Enum

**Parent topic:**[Universal Synchronous Asynchronous Receiver Transceiver \(USART\)](GUID-5ED4F08A-8227-486D-9727-78BD47CA0866.md)

## C

```c

/* Blocking, non-blocking and ring buffer mode */

typedef enum
{
    USART_STOP_1_BIT = US_MR_USART_NBSTOP_1_BIT,
    USART_STOP_1_5_BIT = US_MR_USART_NBSTOP_1_5_BIT,
    USART_STOP_2_BIT = US_MR_USART_NBSTOP_2_BIT,

    /* Force the compiler to reserve 32-bit memory for each enum */
    USART_STOP_INVALID = 0xFFFFFFFF

} USART_STOP;

```

## Summary

Defines the length of stop bits.

## Description

This may be in the USRTx\_SerialSetup API to change the UART stop bits configuration

## Remarks

None.

