# UARTx\_ReadThresholdSet Function

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-3C0B743B-4792-4E9A-AD13-6E911B56B2D0.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-E963A84D-73EE-4E3C-A248-B4FA24F54183.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-12BEB185-3D34-4589-A74C-34A758C5DAB7.md)

**Parent topic:**[Universal Asynchronous Receiver Transmitter \(UART\)](GUID-AA31911E-0C81-4A7D-A72F-20D9976E9E6E.md)

## C

```c
/* x = UART instance number */

/* Ring buffer mode */
void UARTx_ReadThresholdSet(uint32_t nBytesThreshold)
```

## Summary

This API allows the application to set a threshold level on the number of bytes of data available in the receive buffer

## Description

This API allows the application to set a threshold level on the number of bytes of data available in the receive buffer. Once the threshold is reached a notification is given to the application if it is enabled.

## Precondition

UARTx\_Initialize must have been called for the associated UART instance.

## Parameters

|Param|Description|
|-----|-----------|
|nBytesThreshold|Threshold value for number of bytes available in the receive buffer after which a notification must be given|

## Returns

None

## Example

```c
uint8_t rxBuffer[50];
uint32_t nBytes;

void usartReadEventHandler(UART_EVENT event, uintptr_t context )
{
    uint32_t nBytesAvailable = 0;
    
    if (event == UART_EVENT_READ_THRESHOLD_REACHED)
    {
        // Receiver should have the thershold number of bytes in the ring buffer
        nBytesAvailable = UART1_ReadCountGet();
        
        nBytesRead += UART1_Read((uint8_t*)&rxBuffer[nBytesRead], nBytesAvailable);
    }
}

//----------------------------------------------------------//

// Register a callback for read events
UART1_ReadCallbackRegister(usartReadEventHandler, (uintptr_t) NULL);

// Set a threshold value to receive a callback after every 10 characters are received
UART1_ReadThresholdSet(10);

// Enable RX event notifications
UART1_ReadNotificationEnable(true, false);

```

## Remarks

None

