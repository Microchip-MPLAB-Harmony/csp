# MCANx\_TxBufferIsBusy Function

**Parent topic:**[Controller Area Network \(MCAN\)](GUID-C9F1E50C-1EF0-4941-A9CB-89808C7C54AF.md)

## C

```c
bool MCANx_TxBufferIsBusy(uint8_t bufferNumber) // x - Instance of the MCAN peripheral
```

## Summary

Check if Transmission request is pending for the specific Tx buffer.

## Description

Check if Transmission request is pending for the specific Tx buffer.

## Precondition

MCANx\_Initialize has been called.

## Parameters

|Param|Description|
|-----|-----------|
|bufferNumber|Tx buffer number|

## Returns

*true* - Transmission request is pending.

*false* - Transmission request is not pending.

## Example

```c
// Check if Transmission request is pending for the Tx buffer 0
if (MCAN0_TxBufferIsBusy(0) == false)
{
    //Transmission request is not pending
}
```

## Remarks

None.

