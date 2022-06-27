# RTC\_Timer32CounterSet Function

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-3578D06D-FEC5-4769-ADC7-0D46730CD973.md)

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-C95E1695-55CC-4546-9F2C-315F5C908FC1.md)

## C

```c
void RTC_Timer32CounterSet ( uint32_t count )
```

## Summary

Set the 32-bit Timer Counter Value.

## Description

This function sets the 32-bit timer counter value. The counter will start to<br />count up from this count value. The application may typically set the<br />counter to 0 before starting a timing or counting operation. Calling this<br />function when the timer is running will overwrite the current counter value.

## Precondition

RTC\_Initialize, RTC\_Timer32Start must have been called for the associated RTC instance. The RTC peripheral should have been configured in 32-bit Timer Counter mode

## Parameters

|Param|Description|
|-----|-----------|
|count|32-bit value to be loaded in the counter|

## Returns

None.

## Example

```c
// Refer to the description of the RTC_Timer32CounterHasOverflowed()
// function for example usage of the RTC_Timer32CounterSet() function.
```

## Remarks

None.

