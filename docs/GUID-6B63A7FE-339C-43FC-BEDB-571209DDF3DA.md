# ADC\_FastWakeupEnable Function

**Parent topic:**[Analog-to-Digital Converter \(ADC\)](GUID-056D5DD2-57C5-445D-95F9-F4FCAA2DFDE1.md)

**Parent topic:**[Analog-to-Digital Converter \(ADC\)](GUID-92E9F62C-DBB2-4C9A-B8AD-EDEE1E2F2BDF.md)

## C

```c
void ADC_FastWakeupEnable(void)
```

## Summary

This function enables ADC Fast Wakeup.

## Description

This function enables ADC Fast Wakeup.

## Precondition

ADC\_Initialize\(\) function must have been called first for the associated instance.

## Parameters

None.

## Returns

None

## Example

```c
ADC_Initialize();
ADC_FastWakeupEnable();
```

## Remarks

None

