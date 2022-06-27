# CORETIMER\_FrequencyGet Function

**Parent topic:**[MIPS Core Timer \(CORETIMER\)](GUID-0707DBF2-5D28-4D37-BAE7-EB194F1CB63C.md)

## C

```c
uint32_t CORETIMER_FrequencyGet(void);
```

## Summary

Provides the given Core timer's counter-increment frequency.

## Description

This function provides the frequency at which the given counter increments. It can be used to convert differences between counter values to real time or real-time intervals to timer period values.

## Precondition

CORETIMER\_Initialize\(\) function must have been called first.

## Parameters

None.

## Returns

*frequency* - The frequency \(in Hz\) at which the timer counter increments.

## Example

```c
uint32_t frequency;

CORETIMER_Initialize();
frequency = CORETIMER_FrequencyGet();
```

## Remarks

Should be generated for interrupt mode only.

