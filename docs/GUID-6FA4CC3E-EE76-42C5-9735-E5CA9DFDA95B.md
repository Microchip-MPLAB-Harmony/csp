# ADC\_WINMODE Enum

**Parent topic:**[Analog Digital Converter \(ADC\)](GUID-6E851777-3AFA-4FC5-A7DE-14CB9DD2E033.md)

## C

```c
typedef enum
{
    /* Window comparison is disabled */
    ADC_WINMODE_DISABLED = ADC_CTRLB_WINMODE_DISABLE_Val,
    /* Result is greater than lower threshold */
    ADC_WINMODE_GREATER_THAN_WINLT = ADC_CTRLB_WINMODE_MODE1_Val,
    /* Result is less than upper threshold */
    ADC_WINMODE_LESS_THAN_WINUT = ADC_CTRLB_WINMODE_MODE2_Val,
    /* Result is in between lower threshold and upper threshold */
    ADC_WINMODE_BETWEEN_WINLT_AND_WINUT = ADC_CTRLB_WINMODE_MODE3_Val,
    /* Result is outside lower threshold and upper threshold */
    ADC_WINMODE_OUTSIDE_WINLT_AND_WINUT = ADC_CTRLB_WINMODE_MODE4_Val
}ADC_WINMODE;
```

## Summary

Identifies ADC window comparison modes

## Description

Enum for the ADC window comparison mode. This can be used in the API to change the window mode runtime.

## Remarks

None.

