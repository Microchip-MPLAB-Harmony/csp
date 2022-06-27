# RTC\_ALARM\_MASK Enum

**Parent topic:**[Real-Time Clock and Calendar\(RTCC\)](GUID-B5E44A99-95D2-4582-B651-D06671D5F8D8.md)

**Parent topic:**[\(RTCC\)](GUID-2CD86BA1-3631-4EAD-91D1-C1C3C26A895C.md)

**Parent topic:**[Real-Time Clock and Calendar\(RTCC\)](GUID-A833F419-C31F-45F9-A851-9E23B8B6854A.md)

## C

```c
typedef enum
{
    RTC_ALARM_MASK_HALF_SECOND, // Every half-second
    RTC_ALARM_MASK_SECOND, // Every second
    RTC_ALARM_MASK_10_SECONDS, // Every 10 seconds
    RTC_ALARM_MASK_SS, // Every minute
    RTC_ALARM_MASK_10_MINUTES, // Every 10 minutes
    RTC_ALARM_MASK_HOUR, // Every hour
    RTC_ALARM_MASK_HHMISS, // Once a day
    RTC_ALARM_MASK_WEEK, // Once a week
    RTC_ALARM_MASK_MONTH, // Once a month
    RTC_ALARM_MASK_YEAR, // Once a year
    RTC_ALARM_MASK_OFF // Disabled
    
} RTC_ALARM_MASK;

```

## Summary

Possible options for recurrence of RTCC alarm.

## Description

This enumeration defines the possible options for recurrence of RTCC alarm.<br />Used as the second parameter for RTCC\_AlarmSet\(\) function.

## Remarks

None.

