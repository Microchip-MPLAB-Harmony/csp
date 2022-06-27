# DBGU\_WriteNotificationEnable Function

**Parent topic:**[Debug Unit \(DBGU\)](GUID-97C41240-2AC0-4D05-A97E-83EB780C57A2.md)

## C

```c

/* Ring buffer mode */
bool DBGU_WriteNotificationEnable(bool isEnabled, bool isPersistent)
```

## Summary

This API lets the application turn the transmit notifications on/off

## Description

This API allows the application to enable or disable transmit notifications. Further the application can choose to get notified persistently until the threshold condition is true. For example, if the transmit threshold is set to 5, which means a notification is given when the internal transmit buffer has free space for at-least 5 characters. If persistent notification is turned off, the application is notified only once when there is free space for 5 characters in the transmit buffer. However, if persistent notification is turned on, the application is notified every time a byte is transmitted out and the transmit buffer has free space for 5 or more characters.

## Precondition

DBGU\_Initialize must have been called for the associated DBGU instance.

## Parameters

|Param|Description|
|-----|-----------|
|isEnabled|A true value turns on notification, false value turns off notification|
|isPersistent|A true value turns on persistent notification. A false value disablespersistent notifications|

## Returns

The API returns the previous state of notifications. A true value indicates notifications were previously enabled; false value indicates notifications were perviously disabled.

## Example

```c
uint8_t txBuffer[50];
uint32_t nBytes;

volatile bool txThresholdEventReceived = false;

void usartWriteEventHandler(DBGU_EVENT event, uintptr_t context )
{
    txThresholdEventReceived = true;
}

//----------------------------------------------------------//

// Register a callback for write events
DBGU_WriteCallbackRegister(usartWriteEventHandler, (uintptr_t) NULL);

// Set TX threshold - TX buffer is empty
DBGU_WriteThresholdSet(DBGU_WriteBufferSizeGet());

// Enable notifications. Disable persistent notifications.
DBGU_WriteNotificationEnable(true, false);

DBGU_Write((uint8_t*)txBuffer, nBytes);

if (txThresholdEventReceived == true)
{
    // Transmit buffer is empty
}

```

## Remarks

None

