# RTC\_Timer16Compare1HasMatched Function

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-3578D06D-FEC5-4769-ADC7-0D46730CD973.md)

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-C95E1695-55CC-4546-9F2C-315F5C908FC1.md)

## C

```c
bool RTC_Timer16Compare1HasMatched(void)
```

## Summary

Returns true if the 16-bit Timer Compare 1 value has matched the counter.

## Description

This function returns true if the 16-bit Timer Compare 1 value has matched<br />the counter. When operating in 16-bit Timer Counter mode, the RTC<br />peripheral compares the counter value with two defined compare values<br />\(Compare 1 and Compare 1\). This function will return true if the counter<br />value has matched the Compare 1 value and also resets the hardware status<br />flags if when match has occurred.

The Compare 1 Value could have been configured via MHC or at run time by<br />calling the RTC\_Timer16Compare1Set\(\) function. The<br />RTC\_Timer16Compare1ValueMatched\(\) function allows the application to poll<br />for the compare value match.

## Precondition

RTC\_Initialize, RTC\_Timer16Start must have been called for the associated RTC instance. The RTC value should have been configured for 16-bit Timer Counter Mode. The Generate Compare 1 API option in MHC should have been enabled.

## Parameters

None.

## Returns

True if Counter has matched Compare 1 Value, False otherwise.

## Example

```c
RTC_Initialize();
RTC_Timer16CounterSet(0);
RTC_Timer16PeriodSet(0xFFF);

// Calling the RTC_Timer16Compare1Set() function will override the
// Compare 1 value that was set via MHC.
RTC_Timer16Compare1Set(0x3F);
RTC_Timer16Start();

// Wait till the Compare 1 value has matched.
while(!RTC_Timer16Compare1HasMatched());
```

## Remarks

None.

