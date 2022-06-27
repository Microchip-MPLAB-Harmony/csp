# ICAPx\_CaptureStatusGet Function

**Parent topic:**[Input Capture \(ICAP\)](GUID-E126A9DC-A2E6-405E-85E7-9FB676BDEBD2.md)

## C

```c

/* x = ICAP instance number */

bool ICAPx_CaptureStatusGet (void)
```

## Summary

Reads and returns the capture status

## Description

Reads and returns the capture status

## Precondition

ICAPx\_Initialize\(\) function must have been called first.

## Parameters

None.

## Returns

bool - Capture status of channel 0.

## Example

```c
bool captureStatus;
ICAP1_Enable();
captureStatus = ICAP1_CaptureStatusGet();
```

## Remarks

None.

