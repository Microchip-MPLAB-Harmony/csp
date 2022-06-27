# DBGU\_ReadThresholdSet Function

**Parent topic:**[Debug Unit \(DBGU\)](GUID-97C41240-2AC0-4D05-A97E-83EB780C57A2.md)

## C

```c

/* Ring buffer mode */
void DBGU_ReadThresholdSet(uint32_t nBytesThreshold)
```

## Summary

This API allows the application to set a threshold level on the number of bytes of data available in the receive buffer

## Description

This API allows the application to set a threshold level on the number of bytes of data available in the receive buffer. Once the threshold is reached a notification is given to the application if it is enabled.

## Precondition

DBGU\_Initialize must have been called for the associated DBGU instance.

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

void usartReadEventHandler(DBGU_EVENT event, uintptr_t context )
{
    uint32_t nBytesAvailable = 0;
    
    if (event == DBGU_EVENT_READ_THRESHOLD_REACHED)
    {
        // Receiver should have the thershold number of bytes in the ring buffer
        nBytesAvailable = DBGU_ReadCountGet();
        
        nBytesRead += DBGU_Read((uint8_t*)&rxBuffer[nBytesRead], nBytesAvailable);
    }
}

//----------------------------------------------------------//

// Register a callback for read events
DBGU_ReadCallbackRegister(usartReadEventHandler, (uintptr_t) NULL);

// Set a threshold value to receive a callback after every 10 characters are received
DBGU_ReadThresholdSet(10);

// Enable RX event notifications
DBGU_ReadNotificationEnable(true, false);

```

## Remarks

None

