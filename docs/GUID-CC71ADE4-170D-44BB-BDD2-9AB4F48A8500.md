# CACHE\_DataCacheLineSizeGet Function

**Parent topic:**[Cache Controller \(Cache\)](GUID-FA7730F3-DFC4-4DED-92DE-B53A0AF23AC6.md)

## C

```c
size_t CACHE_DataCacheLineSizeGet(void)
```

## Summary

Returns the data cache line size.

## Description

Returns the data cache line size.

## Parameters

None.

## Returns

*size\_t* - number of ways in the data cache.

## Example

```c
size_t dataCacheSize;
instructionCacheSize = CACHE_DataCacheLineSizeGet();
```

## Remarks

None.

