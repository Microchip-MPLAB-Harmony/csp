# RTC\_TimeSet Function

**Parent topic:**[Real-time Clock \(RTC\)](GUID-86211A91-DA87-4BCB-9088-7A54971C4325.md)

**Parent topic:**[Real-time Clock \(RTC\)](GUID-B5657E72-3DDB-4D39-94DC-B9B64B89C2DE.md)

## C

```c
bool RTC_TimeSet( struct tm *time )
```

## Summary

Sets the Time for the RTC peripheral.

## Description

This function updates the time for RTC peripheral as<br />configured by the user.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|time|Pointer to struct tm|

## Returns

True if Valid Time and/or Date is configured, False otherwise.

## Example

```c
struct tm dateTime;
//Hour
dateTime.tm_hour = 12;
//second
dateTime.tm_sec = 0;
//Minute
dateTime.tm_min = 34;
//Month
dateTime.tm_mon = 11;
//Year
dateTime.tm_year = 2017;
//day of the month
dateTime.tm_mday = 14;
//day of the week
dateTime.tm_wday = 1;
RTC_TimeSet( &dateTime );
```

## Remarks

The structure can be deleted once the API returns to free up the memory

