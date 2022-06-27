# CACHE\_InstructionCacheLineSizeGet Function

**Parent topic:**[Cache Controller \(Cache\)](GUID-FA7730F3-DFC4-4DED-92DE-B53A0AF23AC6.md)

## C

```c
size_t CACHE_InstructionCacheLineSizeGet(void)
```

## Summary

Returns the instruction cache line size.

## Description

Returns the instruction cache line size.

## Parameters

None.

## Returns

*size\_t* - number of ways in the data cache.

## Example

```c
size_t instructionCacheLineSize;
instructionCacheLineSize = CACHE_InstructionCacheLineSizeGet();
```

## Remarks

None.

