# AFECx\_ChannelResultIsReady Function

**Parent topic:**[Analog Front-End Controller \(AFEC\)](GUID-89A24A8B-C8CE-48B6-9F65-764983A80D78.md)

## C

```c
bool AFECx_ChannelResultIsReady(AFEC_CHANNEL channel) // x - Instance of the AFEC peripheral
```

## Summary

Returns the status of the channel conversion

## Description

This function returns the status of the channel whether conversion is complete and result is<br />available

## Precondition

AFECx\_Initialize\(\) function must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|channel|channel number|

## Returns

*false* - channel is disabled or conversion is not yet finished<br />*true* - channel is enabled and result is available

## Example

```c
bool ch_status;
AFEC0_Initialize();
AFEC0_ChannelsEnable(AFEC_CH0);
AFEC0_ConversionStart();
ch_status = AFEC0_ChannelResultIsReady(AFEC_CH0);
```

## Remarks

None

