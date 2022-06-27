# RSTC\_Reset Function

**Parent topic:**[Reset Controller \(RSTC\)](GUID-BEFBE2F0-70E9-476E-803B-94AC73E1B2D9.md)

**Parent topic:**[Reset Controller \(RSTC\)](GUID-D165B5DE-1124-4CD7-A662-798BCF303830.md)

**Parent topic:**[Reset Controller \(RSTC\)](GUID-2C223FAB-85E5-4B23-85E5-0FEC7A51B34D.md)

## C

```c
void RSTC_Reset (RSTC_RESET_TYPE type)
```

## Summary

Resets the processor and all the embedded peripherals.

## Description

This function resets the processor and all the embedded peripherals including the memory system and, in particular, the Remap Command or this function asserts NRST Pin.

## Precondition

None.

## Parameters

|Param|Description|
|-----|-----------|
|RSTC\_RESET\_TYPE|Reset type|

## Returns

None.

## Example

```c
RSTC_Reset(RSTC_RESET_PROC);
```

## Remarks

None.

