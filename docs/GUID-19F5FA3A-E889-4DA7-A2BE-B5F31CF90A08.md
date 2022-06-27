# RTCC\_TimeSet Function

**Parent topic:**[Real-Time Clock and Calendar\(RTCC\)](GUID-B5E44A99-95D2-4582-B651-D06671D5F8D8.md)

**Parent topic:**[\(RTCC\)](GUID-2CD86BA1-3631-4EAD-91D1-C1C3C26A895C.md)

**Parent topic:**[Real-Time Clock and Calendar\(RTCC\)](GUID-A833F419-C31F-45F9-A851-9E23B8B6854A.md)

## C

```c
bool RTCC_TimeSet(struct tm *Time );
```

## Summary

Sets time and date in the RTCC peripheral.

## Description

This functions sets time and date in the RTCC peripheral.

## Precondition

The RTCC\_Initialize\(\) function should have been called to initialize the RTCC peripheral.

## Parameters

|Param|Description|
|-----|-----------|
|sys\_time|Input parameter structure which holds time and date.|

## Returns

Always return true. Discard the return value at the application level. This return is to satisfy the function signature requirement of drivers which uses different RTC PLIBs.

## Example

```c
struct tm sys_time;
//15-01-2018 23:55:52 Monday
sys_time.tm_hour = 23;
sys_time.tm_min = 59;
sys_time.tm_sec = 52;

sys_time.tm_year = 18;
sys_time.tm_mon = 12;
sys_time.tm_mday = 31;
sys_time.tm_wday = 1;

RTCC_TimeSet(&sys_time);
```

## Remarks

This function checks RTCSYNC before writing into RTCTIME and RTCDATE registers. Thus no separate check for the bit is needed.

