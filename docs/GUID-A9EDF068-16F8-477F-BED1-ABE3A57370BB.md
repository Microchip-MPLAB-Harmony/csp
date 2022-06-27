# RTC\_LastTimeStampGet Function

**Parent topic:**[Real-time Clock \(RTC\)](GUID-86211A91-DA87-4BCB-9088-7A54971C4325.md)

## C

```c
void RTC_LastTimeStampGet(struct tm * sysTime, RTC_TAMP_INPUT tamperInput);
```

## Summary

Reads the timestamp for last occurrence of given tamper input

## Description

This function is used to read the timestamp for last occurrence of given tamper input.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|sysTime|This is an output parameter that will be filled with the timestamp|
|tamperInput|RTC tamper input number|

## Returns

None

## Example

```c
struct tm dateTime;
//get the timestamp for last occurrence of given tamper input
RTC_LastTimeStampGet(&dateTime, RTC_TAMP_INPUT_0);
```

