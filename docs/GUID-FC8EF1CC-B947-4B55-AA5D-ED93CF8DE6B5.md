# CORETIMER\_Initialize Function

**Parent topic:**[MIPS Core Timer \(CORETIMER\)](GUID-0707DBF2-5D28-4D37-BAE7-EB194F1CB63C.md)

## C

```c
void CORETIMER_Initialize(void);
```

## Summary

Initializes given instance of CORETIMER.

## Description

This function initializes given instance of timer with the options configured in MHC GUI.

## Precondition

MHC GUI should be configured with the desired values.

## Parameters

None.

## Returns

None.

## Example

```c
CORETIMER_Initialize();
```

## Remarks

This function must be called before any other Timer function is called. This function is normally only be called once during system initialization.

