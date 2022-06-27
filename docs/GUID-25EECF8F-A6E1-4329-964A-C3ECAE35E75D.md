# ADC\_ChannelConversionStart Function

**Parent topic:**[Analog-to-Digital Converter \(ADC\)](GUID-FA022CD9-1025-47D5-B8BC-A27AC49112D8.md)

## C

```c
ADC_ChannelConversionStart(void)
```

## Summary

Starts conversion on the ADC core and channel that was specified using the ADC\_SoftwareControlledConversionEnable\(\) API

## Description

Starts conversion on the ADC core and channel that was specified using the ADC\_SoftwareControlledConversionEnable\(\) API

## Precondition

ADCx\_Initialize\(\) function must have been called first for the associated instance.

## Parameters

None

## Returns

None

## Example

```c
ADC_ChannelConversionStart();
```

## Remarks

None

