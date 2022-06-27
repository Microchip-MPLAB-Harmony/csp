# CANx\_RxBufferNumberGet Function

**Parent topic:**[Control Area Network \(CAN\)](GUID-B5AC476B-B06A-4C89-AB15-1BB515862877.md)

## C

```c
bool CANx_RxBufferNumberGet(uint8_t* bufferNumber) // x - Instance of the CAN peripheral
```

## Summary

Get Rx Buffer Number.

## Description

This routine gets Rx Buffer Number.

## Precondition

CANx\_Initialize has been called.

## Parameters

|Param|Description|
|-----|-----------|
|bufferNumber|Rx Buffer Number to be received|

## Returns

Request status.<br />*true* - Request was successful.

*false* - Request has failed.

## Example

```c
uint8_t bufferNumber = 0;
uint8_t rxBuffer[CAN0_RX_BUFFER_SIZE];

CAN0_RxBufferNumberGet(&bufferNumber);
memset(rxBuffer, 0x00, CAN0_RX_BUFFER_ELEMENT_SIZE);
CAN0_MessageReceive(bufferNumber, (CAN_RX_BUFFER *)rxBuffer);
```

## Remarks

None.

