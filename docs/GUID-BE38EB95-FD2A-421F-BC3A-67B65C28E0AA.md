# MCANx\_TxEventFifoRead Function

**Parent topic:**[Controller Area Network \(MCAN\)](GUID-C9F1E50C-1EF0-4941-A9CB-89808C7C54AF.md)

## C

```c
bool MCANx_TxEventFifoRead(uint8_t numberOfTxEvent, MCAN_TX_EVENT_FIFO *txEventFifo) // x - Instance of the MCAN peripheral
```

## Summary

Read Tx Event FIFO for the transmitted messages.

## Description

This routine reads Tx Event FIFO for the transmitted messages.

## Precondition

MCANx\_Initialize has been called.

## Parameters

|Param|Description|
|-----|-----------|
|numberOfTxEvent|Total number of Tx Event|
|txEventFifo|Pointer to Tx Event FIFO|

## Returns

Request status.<br />*true* - Request was successful.

*false* - Request has failed.

## Example

```c
MCAN_TX_EVENT_FIFO txEventFifo;
// Read 1 Tx Event FIFO Element
MCAN0_TxEventFifoRead(1, &txEventFifo);
```

## Remarks

None.

