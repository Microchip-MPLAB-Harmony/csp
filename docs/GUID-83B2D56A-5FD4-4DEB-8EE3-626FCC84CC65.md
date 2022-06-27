# RTC\_RTCCTimeSet Function

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-3578D06D-FEC5-4769-ADC7-0D46730CD973.md)

**Parent topic:**[Real-Time Counter \(RTC\)](GUID-C95E1695-55CC-4546-9F2C-315F5C908FC1.md)

## C

```c
bool RTC_RTCCTimeSet (struct tm * initialTime )
```

## Summary

Sets the Real Time Clock Calendar time and date.

## Description

This function sets the Real Time Clock Calendar time and date. The time and<br />date should be specified via the struct tm structure. The isdst, tm\_wday,<br />tm\_yday member of the initialTime data structure is ignored.

The reference year parameter in MHC should be adjusted to be within 64 years of<br />the input year range. In that, the function will subtract the reference year<br />from the input year while setting the calendar year.

## Precondition

RTC\_Initialize must have been called for the associated RTC instance. The RTC should have been configured for Real Time Clock Calendar operation.

## Parameters

|Param|Description|
|-----|-----------|
|initialTime|Initial time value from the user of type tm structure defined in the time.h header file|

## Returns

bool.

## Example

```c
struct tm initialTime;

RTC_Initialize();

// Set the time as 22:31:23 and date as 7 April 1980.
// The Reference Year Configuration in MHC should be within
// 64 years of 1980. Also note that tm structure needs the tm_year to
// specified as years since 1900.

initialTime.tm_sec = 23;
initialTime.tm_min = 31;
initialTime.tm_hour = 22;
initialTime.tm_mday = 7;
initialTime.tm_mon = 3;
initialTime.tm_year = 80;

if(RTC_RTCCTimeSet(&initialTime) == false)
{
    //incorrect format
}
```

## Remarks

None.

