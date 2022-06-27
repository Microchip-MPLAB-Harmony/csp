# DWDT\_NS\_Clear Function

**Parent topic:**[Dual Watchdog Timer \(DWDT\)](GUID-A1DD4B6F-25A6-404C-828C-396AB3D1C637.md)

## C

```c
void DWDT_NS_Clear(void)
```

## Summary

Clears the never secure watchdog timer

## Description

This function clears the never secure watchdog timer \(NSWDT\).

## Precondition

DWT\_Initialize must have been called

## Parameters

None

## Returns

None.

## Example

```c
DWDT_Initialize();

// Clears the watchdog timer so that it restarts the count
DWDT_NS_Clear();
```

