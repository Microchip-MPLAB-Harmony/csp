# ADC\_CompareEnable Function

**Parent topic:**[Analog-to-Digital Converter \(ADC\)](GUID-FA022CD9-1025-47D5-B8BC-A27AC49112D8.md)

## C

```c
void ADC_CompareEnable(ADC_CORE_NUM core, ADC_CHANNEL_NUM channel)
```

## Summary

Enables digital comparisons for the given channel on the specified ADC core

## Description

This function enables digital comparisons for the given channel on the specified ADC core.

## Precondition

ADCx\_Initialize\(\) function must have been called first for the associated instance.

## Parameters

|Param|Description|
|-----|-----------|
|core|ADC core n|
|channel|channel number on ADC core n|

## Returns

None.

## Example

```c
ADC_CompareEnable(ADC_CORE_NUM1, ADC_CH0);
```

## Remarks

None

