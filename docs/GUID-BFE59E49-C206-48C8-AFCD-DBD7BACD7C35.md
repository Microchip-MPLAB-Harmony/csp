# ADCHS\_EOSStatusGet Function

**Parent topic:**[Analog to Digital Converter \(ADCHS\)](GUID-8740EC52-3365-4B31-B19A-227EC55268DD.md)

## C

```c
bool ADCHS_EOSStatusGet(void)
```

## Summary

Returns the status of the end of scan interrupt flag

## Description

This function returns the status of the end of scan interrupt flag. End Of Scan \(EOS\) interrupt is set after the last channel in the scan sequence completes the conversion.

## Precondition

ADCHS\_Initialize\(\) function must have been called first for the associated instance.

## Parameters

None

## Returns

*false* - scan sequence conversion ongoing<br />*true* - scan sequence conversion is complete

## Example

```c
bool ch_status;
ADCHS_Initialize();
ADCHS_ModulesEnable(ADCHS_MODULE0_MASK);
ADCHS_ConversionStart();
ch_status = ADCHS_EOSStatusGet();
```

## Remarks

None

