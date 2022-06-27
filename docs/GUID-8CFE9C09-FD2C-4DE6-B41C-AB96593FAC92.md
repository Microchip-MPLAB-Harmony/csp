# TCCx\_Capture24bitValueGet Function

**Parent topic:**[Timer Counter for Control Applications \(TCC\)](GUID-CCA150A8-2C66-40B2-9C35-D7F3473720AE.md)

## C

```c
/* x = TCC instance number */
uint32_t TCCx_Capture24bitValueGet( TCCx_CHANNEL_NUM channel );
```

## Summary

Reads capture value from given channel

## Description

This function reads the captured value stored in CC.<br />Value can be read from interrupt routine or by polling.

## Precondition

TCCx\_CaptureInitialize\(\) function must have been called first.

## Parameters

|Param|Description|
|-----|-----------|
|channel|capture channel number|

## Returns

Captured value from given channel

## Example

```c
uint32_t captureValue = 0;
TCC0_CaptureInitialize();
TCC0_CaptureStart();
captureValue = TCC0_Capture24bitValueGet(TCC0_CHANNEL0);
```

## Remarks

None.

