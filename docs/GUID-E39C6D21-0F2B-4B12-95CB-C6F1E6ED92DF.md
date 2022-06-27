# ADC\_GlobalLevelConversionStart Function

**Parent topic:**[Analog-to-Digital Converter \(ADC\)](GUID-FA022CD9-1025-47D5-B8BC-A27AC49112D8.md)

## C

```c
void ADC_GlobalLevelConversionStart(void)
```

## Summary

Starts global level trigger and starts conversion on channels configured with Global level as the trigger source

## Description

This function starts generation of global level trigger and starts conversion on<br />channels configured with Global level as the trigger source

## Precondition

ADCx\_Initialize\(\) function must have been called first for the associated instance.

## Parameters

None

## Returns

None

## Example

```c
ADC_GlobalLevelConversionStart();
```

## Remarks

None

