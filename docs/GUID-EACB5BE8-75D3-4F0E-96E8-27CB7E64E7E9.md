# RTC\_Timer16Compare0Set Function

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-3578D06D-FEC5-4769-ADC7-0D46730CD973.md)

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-C95E1695-55CC-4546-9F2C-315F5C908FC1.md)

## C

```c
void RTC_Timer16Compare0Set ( uint16_t comparisionValue )
```

## Summary

Set the 16-Bit Counter Compare 0 Value.

## Description

This function will set the Counter Compare 0 Value. The module will compare<br />the counter against this value and will signal a match when the counter<br />equals the compare value. If the library was configured for interrupt mode,<br />the Compare 0 event is enabled and if a valid callback is registered, the<br />library will call the registered callback function with the<br />RTC\_TIMER16\_INT\_MASK\_COMP0 / RTC\_TIMER16\_INT\_MASK\_COMPARE0\_MATCH event. The RTC\_Timer16Compare0HasMatched\(\)<br />function will return true when the match occurs.

## Precondition

RTC\_Initialize, RTC\_Timer16Start must have been called for the associated RTC instance. The module should have configured for 16-bit Timer Counter operation.

## Parameters

None.

## Returns

16-bit compare value compares with the current counter value.

## Example

```c
// Refer to the description of the RTC_Timer16Compare0HasMatched()
// function for example usage of the RTC_Timer16Compare0Set() function.

```

## Remarks

None.

