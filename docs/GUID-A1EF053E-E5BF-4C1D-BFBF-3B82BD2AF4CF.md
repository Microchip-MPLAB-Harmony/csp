# RTT\_TimerValueGet Function

**Parent topic:**[Real-time Timer \(RTT\)](GUID-2A29BDE4-A969-4CEB-A21C-AF161D295289.md)

## C

```c
uint32_t RTT_TimerValueGet(void);
```

## Summary

Returns the current timer value

## Description

This function is used the counter value of RTT. This value can be<br />use to calculate the time elapsed.

## Precondition

None.

## Parameters

None.

## Returns

The current timer count

## Example

```c
uint32_t frequency = 0;
uint32_t count = 0;
uint64_t time_elapsed;

frequency = RTT_FrequencyGet();
count = RTT_TimerValueGet();

time_elapsed = count/frequency;
```

