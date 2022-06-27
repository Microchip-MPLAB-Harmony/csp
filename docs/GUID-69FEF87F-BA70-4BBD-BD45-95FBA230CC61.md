# CANx\_RxFifoCallbackRegister Function

**Parent topic:**[Control Area Network \(CAN\)](GUID-B5AC476B-B06A-4C89-AB15-1BB515862877.md)

## C

```c
void CANx_RxFifoCallbackRegister(CAN_RX_FIFO_NUM rxFifoNum, CAN_RX_FIFO_CALLBACK callback, uintptr_t contextHandle) // x - Instance of the CAN peripheral
```

## Summary

Sets the pointer to the function \(and it's contextHandle\) to be called when the given CAN's Rx transfer events occur.

## Precondition

CANx\_Initialize must have been called for the associated CAN instance.

## Parameters

|Param|Description|
|-----|-----------|
|rxFifoNum|Rx FIFO Number|
|callback|A pointer to callback function which function prototype definedby the CAN\_RX\_FIFO\_CALLBACK data type.|
|contextHandle|A value passed into the callback function as callback parameter.|

## Returns

None.

## Example

```c
void APP_CAN_RxFifo0Callback(uint8_t numberOfMessage, uintptr_t context)
{
}

CAN0_RxFifoCallbackRegister(CAN_RX_FIFO_0, APP_CAN_RxFifo0Callback, NULL);
```

## Remarks

None.

