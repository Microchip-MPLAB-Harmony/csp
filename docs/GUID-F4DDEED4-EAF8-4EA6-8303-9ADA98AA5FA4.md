# TCx\_Compare8bitCounterSet Function

**Parent topic:**[Basic Timer Counter \(TC\)](GUID-D805E0EA-6923-41A3-A27E-5A159783D12C.md)

## C

```c
/* x = TC instance number */
void TCx_Compare8bitCounterSet( uint8_t count );
```

## Summary

Sets new timer counter value.

## Description

This function sets new timer counter value.

## Precondition

TCx\_CompareInitialize\(\) function must have been called first.

## Parameters

|Param|Description|
|-----|-----------|
|count|new counter value to set|

## Returns

None.

## Example

```c
uint8_t count = 0x10U;
TC0_CompareInitialize();
TC0_CompareStart();
TC0_Compare8bitCounterSet(count);
```

## Remarks

The caller must know the number of significant bytes of timer. Counter value is right-aligned.

